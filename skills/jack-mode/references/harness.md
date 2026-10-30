# Running these skills in Claude Code and Codex

These skills were written for Cursor (pstack, thermos, the team kit) and for several harnesses (Matt Pocock's). Read this once per session, then map each name with the tables below. If a field has no row, drop it and say so. Never pass a field or value the tool schema rejects.

## Running another skill

All skills install side by side, so every skill sits at `../<name>/SKILL.md` from any other skill's folder. That holds for `install.sh` and for the `jack` plugin alike.

Installed as the `jack` Claude Code plugin, every skill and subagent name gets a `jack:` prefix. Where a row below gives a bare `name`, use `jack:name` if Claude Code rejects the bare one.

| A skill says | Do this |
| --- | --- |
| "the **name** skill", `/name`, or "call the Skill tool with name" | Read `../<name>/SKILL.md` and follow it. This works for every skill, including the ones only Jack can start, which the Skill tool refuses. |
| Tell the user to type a skill | Claude Code: `/name`, or `/jack:name` in the plugin install. Codex: `$name`. |

## Tools

| Name in a skill | Claude Code | Codex |
| --- | --- | --- |
| `Task`, "spawn a subagent" | `Agent` | Its subagent tool if the session has one. Otherwise do the work yourself, one piece at a time, and say so. |
| `AskQuestion`, `AskUserQuestion` | `AskUserQuestion`, or plain text in `-p` mode | Ask in plain text. |
| Open a todo list | `TodoWrite` | `update_plan` |
| `Grep`, `Glob` | `Grep`, `Glob` | `rg` in the shell |
| `/loop` | `/loop`, or `ScheduleWakeup` where the session offers it | Keep working in the same turn until the exit condition holds. |

## Subagent fields

| Cursor field | Claude Code | Codex |
| --- | --- | --- |
| `subagent_type: "poteto-agent"` or `"jack-agent"` | `subagent_type: "jack-agent"`, or `"jack:jack-agent"` in the plugin install | A subagent briefed to read `../jack-mode/SKILL.md` first |
| `subagent_type: "comment-sicko"`, `"style-reviewer"`, `"consistency-reviewer"`, or a `thermo-nuclear-*-subagent` | The same `subagent_type`, with a `jack:` prefix in the plugin install | A subagent briefed with the body of `~/.claude/agents/<name>.md`, or do the review yourself with that body as the instructions |
| `subagent_type: generalPurpose` | `"general-purpose"` | Any subagent |
| `readonly: true` | `subagent_type: "Explore"`, and say "do not edit files" in the brief | Say "do not edit files" in the brief |
| `run_in_background: true` | Omit. Subagents already run in the background. | Omit |
| `resume` | Spawn a new agent and paste the earlier result into its brief | Same |
| `model`, any model slug | Omit. Every subagent runs on the session's model. | Omit |
| `environment: "cloud"` | `isolation: "worktree"` | A separate git worktree you create |

## Paths

| Cursor path | Claude Code | Codex |
| --- | --- | --- |
| `.cursor/skills/`, `~/.cursor/skills/` | `.claude/skills/`, `~/.claude/skills/`, or the plugin's copy under `~/.claude/plugins/cache/` | `.agents/skills/`, `~/.agents/skills/` |
| `.cursor/rules/*.mdc`, always-applied rules | `CLAUDE.md` | `AGENTS.md` |
| Chat transcripts in `~/.cursor/projects/<slug>/agent-transcripts/` | `~/.claude/projects/<slug>/<session>.jsonl`. The slug is the workspace path with each `/` and `.` changed to `-`. Read only this workspace's folder. | `~/.codex/sessions/`. Read only sessions whose working directory is this workspace. |

## Files you write in a repo

Nothing these skills write into a repo is tracked by git or reaches GitHub. The code change a task asks for is the one exception: it ships on its branch as usual. Commit any other file only when Jack asks for that file by name.

Everything else goes in the **Jack folder**: `.jack/` at the root of the repo's main checkout. Before the first write in a session, run this from anywhere in the repo:

```bash
common="$(git rev-parse --path-format=absolute --git-common-dir)"
jack="$(dirname "$common")/.jack"
mkdir -p "$jack" "$common/info"
grep -qxF '/.jack/' "$common/info/exclude" 2>/dev/null || echo '/.jack/' >> "$common/info/exclude"
```

`.git/info/exclude` is git's own ignore list for one clone. Git never commits it, every worktree of the clone shares it, and the repo's `.gitignore` stays untouched. Never add the Jack folder to `.gitignore`, and never `git add -f` a file in it.

| File | Path |
| --- | --- |
| Spec | `.jack/specs/<feature>.md` |
| ADR | `.jack/adr/NNNN-slug.md` |
| Glossary | `.jack/GLOSSARY.md`. For several contexts, `.jack/GLOSSARY-MAP.md` plus `.jack/contexts/<context>/GLOSSARY.md` and `.jack/contexts/<context>/adr/` |
| How skills read the domain docs | `.jack/domain.md` |
| Decision log | `.jack/audit/<task-slug>.tsv` |
| Wizard, one-off script, notes | `.jack/scratch/<task-slug>/` |
| Prototype, evidence, screenshots | The OS temp dir as the skill says, or `.jack/scratch/<task-slug>/` when it must sit beside the code |

A generated project skill has to sit where the harness loads it: `.claude/skills/<name>/` and its `.agents/skills/<name>` symlink. Add both to the same exclude file with the same `grep -qxF ... || echo ...` line, as `/.claude/skills/<name>/` and `/.agents/skills/<name>`.

The repo's tracked docs (`GLOSSARY.md`, `docs/adr/`, `docs/specs/`, `CLAUDE.md`, `AGENTS.md`) belong to the repo's team. Read them alongside the Jack folder, and where the two disagree, say so. Never edit or add to them unless Jack asks.

Before every commit, run `git status --porcelain` and confirm that only the task's code is staged.

A cloud session starts from a fresh clone, so its Jack folder starts empty and goes away with the session. Put anything Jack should keep in the reply, or in the session's shared or persistent folder if it has one.

## Cursor-only features

Claude Code and Codex have no Bugbot, Cursor Automations, Cursor cloud agents, Origin, or built-in PR tool. When a step needs one, put one line in your reply, `Skipped: <step>. <reason>.`, and go on. Use `gh` for every PR operation.
