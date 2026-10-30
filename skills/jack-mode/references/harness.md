# Running these skills in Claude Code and Codex

These skills were written for Cursor (pstack, thermos, the team kit) and for several harnesses (Matt Pocock's). Read this once per session, then map each name with the tables below. If a field has no row, drop it and say so. Never pass a field or value the tool schema rejects.

## Running another skill

All skills install side by side, so every skill sits at `../<name>/SKILL.md` from any other skill's folder.

| A skill says | Do this |
| --- | --- |
| "the **name** skill", `/name`, or "call the Skill tool with name" | Read `../<name>/SKILL.md` and follow it. This works for every skill, including the ones only Jack can start, which the Skill tool refuses. |
| Tell the user to type a skill | Claude Code: `/name`. Codex: `$name`. |

## Tools

| Name in a skill | Claude Code | Codex |
| --- | --- | --- |
| `Task`, "spawn a subagent" | `Agent` | Its subagent tool if the session has one. Otherwise do the work yourself, one piece at a time, and say so. |
| `AskQuestion`, `AskUserQuestion`, "ask the user" | `AskUserQuestion`. See [Asking questions](#asking-questions). | `request_user_input`. See [Asking questions](#asking-questions). |
| Present a plan or design for approval | `ExitPlanMode` when the session is in plan mode | A `<proposed_plan>` block when the session is in Plan mode |
| Open a todo list | `TodoWrite` | `update_plan` |
| `Grep`, `Glob` | `Grep`, `Glob` | `rg` in the shell |
| `/loop` | `/loop`, or `ScheduleWakeup` where the session offers it | Keep working in the same turn until the exit condition holds. |

## Asking questions

Ask Jack through the harness's question tool, so each question shows as a card he answers with one click.

| | Claude Code `AskUserQuestion` | Codex `request_user_input` |
| --- | --- | --- |
| Questions per call | 1 to 4 | 1 to 3 |
| Options per question | 2 to 4 | 2 to 3 |
| Fields per question | `question`, `header` (12 characters or fewer), `options` of `label` and `description`, `multiSelect` | `id` (snake_case), `header` (12 characters or fewer), `question` (one sentence), `options` of `label` and `description` |
| Where it works | The main session. Not in subagents or `-p` mode. | Plan mode. Default mode only when `default_mode_request_user_input = true` is set under `[features]` in `~/.codex/config.toml`. |

- Put the recommended option first and end its label with "(Recommended)".
- Both tools add a free-text "Other" choice. Never add one yourself.
- Keep each option's `description` to one sentence on what picking it means. Put context that won't fit in a short message before the call.
- When a round has more questions than one call takes, make the next call as soon as the first is answered. It is still the same round.
- Fall back to plain text when the tool is missing or a question has no sensible options. Use the asking skill's text format.

To present a finished plan or design for approval in plan mode, use `ExitPlanMode` in Claude Code or one `<proposed_plan>` block in Codex, each holding the whole plan. Both show Jack an approve-and-build prompt. Outside plan mode, write the plan in a message and ask for the go.

## Subagent fields

| Cursor field | Claude Code | Codex |
| --- | --- | --- |
| `subagent_type: "poteto-agent"` or `"jack-agent"` | `subagent_type: "jack-agent"` | A subagent briefed to read `../jack-mode/SKILL.md` first |
| `subagent_type: "comment-sicko"`, `"style-reviewer"`, or a `thermo-nuclear-*-subagent` | The same `subagent_type` | A subagent briefed with the body of `~/.claude/agents/<name>.md`, or do the review yourself with that body as the instructions |
| `subagent_type: generalPurpose` | `"general-purpose"` | Any subagent |
| `readonly: true` | `subagent_type: "Explore"`, and say "do not edit files" in the brief | Say "do not edit files" in the brief |
| `run_in_background: true` | Omit. Subagents already run in the background. | Omit |
| `resume` | Spawn a new agent and paste the earlier result into its brief | Same |
| `model`, any model slug | Omit. Every subagent runs on the session's model. | Omit |
| `environment: "cloud"` | `isolation: "worktree"` | A separate git worktree you create |

## Paths

| Cursor path | Claude Code | Codex |
| --- | --- | --- |
| `.cursor/skills/`, `~/.cursor/skills/` | `.claude/skills/`, `~/.claude/skills/` | `.agents/skills/`, `~/.agents/skills/` |
| `.cursor/rules/*.mdc`, always-applied rules | `CLAUDE.md` | `AGENTS.md` |
| Chat transcripts in `~/.cursor/projects/<slug>/agent-transcripts/` | `~/.claude/projects/<slug>/<session>.jsonl`. The slug is the workspace path with each `/` and `.` changed to `-`. Read only this workspace's folder. | `~/.codex/sessions/`. Read only sessions whose working directory is this workspace. |

## Cursor-only features

Claude Code and Codex have no Bugbot, Cursor Automations, Cursor cloud agents, Origin, or built-in PR tool. When a step needs one, put one line in your reply, `Skipped: <step>. <reason>.`, and go on. Use `gh` for every PR operation.
