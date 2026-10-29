import re
import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
SKILLS = ROOT / "skills"
BANNED = ["grok-", "pstack-models", "setup-pstack", "poteto-mode", "poteto-agent", "~/.cursor", "cursor-team-kit"]
SKILL_REF = re.compile(r"\*\*([a-z0-9-]+)\*\*(?: principle)? skill")
TOOL_REF = re.compile(r'Skill tool (?:with|twice, for) "([a-z0-9-]+)"')
LINK_REF = re.compile(r"\.\./([a-z0-9-]+)/SKILL\.md")
PRINCIPLE_REF = re.compile(r"\*\*(principle-[a-z0-9-]+)\*\*")
NOT_SKILLS = {"name", "model-invoked", "user-invoked"}


def frontmatter(path: Path) -> dict:
    text = path.read_text()
    if not text.startswith("---\n"):
        raise ValueError("no frontmatter")
    return yaml.safe_load(text.split("---", 2)[1])


def resolves(name: str, names: set[str]) -> bool:
    return name in names or f"principle-{name}" in names


def main() -> int:
    names = {p.name for p in SKILLS.iterdir() if p.is_dir()}
    errors: list[str] = []
    for skill in sorted(SKILLS.iterdir()):
        md = skill / "SKILL.md"
        if not md.exists():
            errors.append(f"{skill.name}: missing SKILL.md")
            continue
        meta = frontmatter(md)
        if meta.get("name") != skill.name:
            errors.append(f"{skill.name}: frontmatter name is {meta.get('name')!r}")
        if not meta.get("description"):
            errors.append(f"{skill.name}: empty description")
        codex = skill / "agents" / "openai.yaml"
        if not codex.exists():
            errors.append(f"{skill.name}: missing agents/openai.yaml")
        else:
            policy = (yaml.safe_load(codex.read_text()) or {}).get("policy", {})
            user_only = meta.get("disable-model-invocation") is True
            if user_only != (policy.get("allow_implicit_invocation") is False):
                errors.append(f"{skill.name}: disable-model-invocation and openai.yaml policy disagree")
    for path in sorted([*SKILLS.rglob("*.md"), *(ROOT / "agents").glob("*.md")]):
        text = path.read_text()
        rel = path.relative_to(ROOT)
        for word in BANNED:
            if word in text and rel.name != "harness.md":
                errors.append(f"{rel}: mentions {word}")
        refs = {*SKILL_REF.findall(text), *TOOL_REF.findall(text), *LINK_REF.findall(text), *PRINCIPLE_REF.findall(text)}
        for ref in refs - NOT_SKILLS:
            if not resolves(ref, names):
                errors.append(f"{rel}: references missing skill {ref}")
    for error in errors:
        print(error)
    print(f"{len(names)} skills, {len(errors)} problems")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
