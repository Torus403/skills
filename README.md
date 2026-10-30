# skills

Jack's agent skills for Claude Code and Codex. They are built from [pstack](https://github.com/cursor/plugins/tree/main/pstack) by poteto, [Matt Pocock's skills](https://github.com/mattpocock/skills), and Cursor's [thermos](https://github.com/cursor/plugins/tree/main/thermos) and [team kit](https://github.com/cursor/plugins/tree/main/cursor-team-kit), then adapted to how Jack works.

## How Jack works

- **Align first.** Match how the codebase already does things before inventing anything.
- **Plan deeply, up front.** The agent grills Jack with questions and recommendations until nothing is left to guess, then builds to the end without stopping.
- **Simple wins.** The least fancy design with the fewest moving parts and the least logic, with no bugs, crashes, or surprises.
- **Docs only for big things.** Specs for new features, core logic, and architecture go in `docs/specs/`. Architecture decisions go in `docs/adr/`. Small work gets none.
- **Everything is a PR.** Branch `type/short-desc`, Conventional Commits, a conventional PR title. A feature is one big PR. Squash-merged, and only when Jack says so.
- **Plain, readable code.** Deep modules, inlined single-use helpers, long descriptive names, blank lines between steps, and almost no comments. The **code-style** skill holds the rules and examples.
- **Verified for real.** The change runs the way a user would run it before anyone calls it done.

## Install

### Claude Code plugin

In a Claude Code session:

```text
/plugin marketplace add Torus403/skills
/plugin install jack@jack-skills
```

On Claude Code 2.1.275 or later, `/plugin install jack --marketplace Torus403/skills` does both in one step. This needs no GitHub sign-in, because the repo is public. If the clone fails on a machine with no GitHub SSH key, start Claude Code with `CLAUDE_CODE_PLUGIN_PREFER_HTTPS=1` and run the commands again.

The plugin prefixes every name with `jack:`, so type `/jack:jack-mode` and `/jack:jack-help`.

To update, run `/plugin marketplace update jack-skills`, then `/reload-plugins` or start a new session. To update on its own, open `/plugin`, go to **Marketplaces**, pick `jack-skills`, and select **Enable auto-update**. The plugin has no version number, so every new commit on `main` counts as an update.

### Script (Claude Code and Codex)

Codex needs the script. Use one way per machine, not both, or Claude Code loads every skill twice.

```bash
git clone https://github.com/Torus403/skills.git
cd skills
./install.sh
```

`install.sh` copies every skill in `skills/` into `~/.claude/skills/` (Claude Code) and `~/.agents/skills/` (Codex), and the subagents in `agents/` into `~/.claude/agents/`. To update, run `git pull && ./install.sh`. It only replaces skills it installed, so your other skills stay put.

## Use

Start most work with `jack-mode` and one sentence about the task. Type `/jack-mode` in Claude Code (`/jack:jack-mode` with the plugin) or `$jack-mode` in Codex.

```text
/jack-mode add saved searches to the search page
/jack-mode the export button does nothing on Safari. repro first, then fix
/jack-mode babysit this PR
```

Not sure which skill fits? Type `/jack-help` (or `$jack-help`) with a question.

## Layout

| Path | What it holds |
| --- | --- |
| `skills/<name>/` | One skill per folder: `SKILL.md`, any references, and `agents/openai.yaml` for Codex. |
| `skills/jack-mode/` | The router, its playbooks, and `references/harness.md`, which maps tool names to Claude Code and Codex. |
| `skills/principle-*/` | Short rules that `jack-mode` reads at task start. |
| `.claude-plugin/` | The `jack-skills` marketplace and the `jack` plugin manifest. |
| `agents/` | Subagents for Claude Code: `jack-agent`, `comment-sicko`, `style-reviewer`, and the two thermos reviewers. |
| `upstream/` | Untouched copies of every source, with their licences. Never loaded as skills. |
| `scripts/check.py` | Checks every skill's frontmatter, Codex file, and cross-references. |

## Credits

The skills in `skills/` are adapted from MIT-licensed work by Lauren Tan (poteto), Matt Pocock, and Cursor. The original licences and an unedited copy of each source live in [`upstream/`](./upstream/README.md).
