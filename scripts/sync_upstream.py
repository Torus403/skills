import argparse
import filecmp
import json
import re
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
UPSTREAM = ROOT / "upstream"
SOURCES = UPSTREAM / "sources.json"
TABLE = UPSTREAM / "README.md"
MANIFESTS = ["plugin.json", ".cursor-plugin/plugin.json", ".claude-plugin/plugin.json"]


def clone(repo: str, branch: str, into: Path) -> str:
    subprocess.run(
        ["git", "clone", "--quiet", "--depth", "1", "--branch", branch, f"https://github.com/{repo}.git", str(into)],
        check=True,
    )
    return subprocess.run(["git", "-C", str(into), "rev-parse", "HEAD"], check=True, capture_output=True, text=True).stdout.strip()


def files_under(folder: Path) -> set[str]:
    if not folder.exists():
        return set()
    return {
        path.relative_to(folder).as_posix()
        for path in folder.rglob("*")
        if path.is_file() and ".git" not in path.relative_to(folder).parts
    }


def changed_files(old: Path, new: Path) -> dict[str, str]:
    old_files = files_under(old)
    new_files = files_under(new)
    changes = {path: "added" for path in new_files - old_files}
    changes |= {path: "removed" for path in old_files - new_files}
    for path in old_files & new_files:
        old_path, new_path = old / path, new / path
        if old_path.is_symlink() or new_path.is_symlink():
            same = old_path.is_symlink() and new_path.is_symlink() and old_path.readlink() == new_path.readlink()
        else:
            same = filecmp.cmp(old_path, new_path, shallow=False)
        if not same:
            changes[path] = "modified"
    return changes


def owner(path: str, old: Path, new: Path) -> str | None:
    parts = path.split("/")
    for depth in range(len(parts) - 1, 0, -1):
        folder = "/".join(parts[:depth])
        if (old / folder / "SKILL.md").exists() or (new / folder / "SKILL.md").exists():
            return parts[depth - 1]
    if len(parts) >= 2 and parts[-2] == "agents" and parts[-1].endswith(".md"):
        return parts[-1].removesuffix(".md")
    return None


def jack_versions(name: str, feeds: dict[str, list[str]]) -> list[str]:
    ours = {path.name for path in (ROOT / "skills").iterdir()} | {path.stem for path in (ROOT / "agents").glob("*.md")}
    return [target for target in feeds.get(name, [name]) if target in ours]


def manifest_version(folder: Path) -> str | None:
    for manifest in MANIFESTS:
        path = folder / manifest
        if path.exists():
            return json.loads(path.read_text()).get("version")
    return None


def update_table_row(folder: str, old_commit: str, new_commit: str, old_version: str | None, new_version: str | None) -> None:
    lines = TABLE.read_text().splitlines(keepends=True)
    for index, line in enumerate(lines):
        if not line.startswith(f"| `{folder}/` |"):
            continue
        line = line.replace(old_commit, new_commit)
        if old_version and new_version:
            line = re.sub(rf"\bv{re.escape(old_version)}\b", f"v{new_version}", line)
        lines[index] = line
    TABLE.write_text("".join(lines))


def report_section(source: dict, new_commit: str, changes: dict[str, str], old: Path, new: Path, feeds: dict[str, list[str]]) -> str:
    by_owner: dict[str, list[str]] = {}
    loose: list[str] = []
    for path, change in sorted(changes.items()):
        name = owner(path, old, new)
        if name:
            by_owner.setdefault(name, []).append(f"{change} `{path}`")
        else:
            loose.append(f"{change} `{path}`")

    compare = f"https://github.com/{source['repo']}/compare/{source['commit'][:12]}...{new_commit[:12]}"
    lines = [f"### `{source['folder']}/`", "", f"Files changed: {len(changes)}. [Upstream diff]({compare}).", ""]
    if by_owner:
        lines += ["| Upstream | Jack's version to check | Files |", "| --- | --- | --- |"]
        for name, entries in sorted(by_owner.items()):
            ours = ", ".join(f"`{target}`" for target in jack_versions(name, feeds)) or "not shipped"
            lines.append(f"| `{name}` | {ours} | {'<br>'.join(entries)} |")
        lines.append("")
    if loose:
        lines += ["Other files:", "", *(f"- {entry}" for entry in loose), ""]
    return "\n".join(lines)


def main() -> int:
    parser = argparse.ArgumentParser(description="Replace each upstream/ folder with its source's latest tree.")
    parser.add_argument("--report", type=Path, help="write a Markdown summary of what changed here")
    args = parser.parse_args()

    config = json.loads(SOURCES.read_text())
    sections: list[str] = []

    with tempfile.TemporaryDirectory() as scratch:
        clones: dict[tuple[str, str], tuple[Path, str]] = {}
        for source in config["sources"]:
            key = (source["repo"], source["branch"])
            if key not in clones:
                into = Path(scratch) / str(len(clones))
                clones[key] = (into, clone(source["repo"], source["branch"], into))
            checkout, new_commit = clones[key]

            fresh = checkout / source["path"]
            vendored = UPSTREAM / source["folder"]
            changes = changed_files(vendored, fresh)
            if not changes:
                print(f"{source['folder']}: up to date")
                continue

            print(f"{source['folder']}: changed, {len(changes)} files")
            sections.append(report_section(source, new_commit, changes, vendored, fresh, config["feeds"]))
            old_version = manifest_version(vendored)
            if vendored.exists():
                shutil.rmtree(vendored)
            shutil.copytree(fresh, vendored, symlinks=True, ignore=shutil.ignore_patterns(".git"))
            update_table_row(source["folder"], source["commit"], new_commit, old_version, manifest_version(vendored))
            source["commit"] = new_commit

    SOURCES.write_text(json.dumps(config, indent=2) + "\n")
    if args.report and sections:
        intro = "Upstream changed. Each folder below was replaced wholesale. Nothing in `skills/` or `agents/` was touched, so check the listed versions by hand and port what you want."
        args.report.write_text("\n\n".join([intro, *sections]) + "\n")
    return 0


if __name__ == "__main__":
    sys.exit(main())
