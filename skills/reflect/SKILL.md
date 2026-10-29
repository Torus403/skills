---
name: reflect
description: Review a finished session with four parallel reviewers, then route each learning to a skill edit or a change to the repo's agent environment (checks, CLAUDE.md, AGENTS.md, tooling). Use when the user says reflect or retro.
disable-model-invocation: true
---

# Reflect

Mine the current conversation for durable learnings, then route them into skill edits and environment improvements. This merges pstack's `reflect` with Matt Pocock's `retro`.

Invoke when the user says "reflect", "retro", or "/reflect". Skip when the conversation is trivial, off-topic, or already covered by an existing skill the parent followed correctly. One-offs are not learnings.

## 1. Locate the active transcript

Before fanning out, find this conversation's transcript in this workspace's transcript folder (see `../jack-mode/references/harness.md`). Never read another workspace's transcripts. List the newest few files, read the first line of each, and take the one that contains the conversation's opening user prompt. If none matches, pass a tight digest of the session instead.

## 2. Spawn four reviewers in parallel

One message, four subagents, on the session's model, each allowed to use MCP tools (do not use a read-only type that strips them). Reviewers need MCP access to look up the threads and traces the transcript references.

| Lens | Prompt template |
|---|---|
| Judgment | `references/judgment-reviewer.md` |
| Tooling | `references/tooling-reviewer.md` |
| Divergent | `references/divergent-reviewer.md` |
| Environment | `references/environment-reviewer.md` |

Pass each template verbatim, substituting the transcript path or digest where marked. Reviewers return findings in their response.

## 3. Synthesize

One fresh subagent, with MCP access. It spot-verifies citations through MCP. Pass `references/synthesizer.md` verbatim, with each reviewer's full output inlined where marked. It returns an Accepted / Rejected / Backlog list.

## 4. Structural enforcement check

Move any Accepted item that a lint rule, script, metadata flag, or runtime check would enforce more reliably to Backlog. See the **encode-lessons-in-structure** principle skill.

## 5. Apply

Present the synthesizer's full Accepted / Rejected / Backlog output and wait for explicit approval before applying any Accepted edit. The user picks the subset and may redirect routings. Skill changes affect every future agent in the org. Do not auto-apply.

List the Backlog items in the summary. There is no tracker. Only the Accepted list waits for approval.

Never edit an installed copy under `~/.claude/skills/` or `~/.agents/skills/`. Skill edits go to Jack's skills repo (`Torus403/skills`, under `skills/<name>/`) on a branch, as a PR that follows the **Opening a PR** playbook. Environment edits (checks, `CLAUDE.md`, `AGENTS.md`, tooling) go to the repo the session worked in, also as a PR. Show each destination before approval.

Follow each approved row's Routing exactly:

- Trivial existing-skill edit (a one-line bullet, a tightened sentence, a stale fact corrected): the parent does it directly.
- Substantive existing-skill edit (a new section, a new pattern table, more than ~10 lines): follow the **writing-for-agents** skill and the Authoring a skill playbook of **jack-mode**.
- `tune description: <skill path>` (the skill exists but didn't trigger when it should have): rewrite the description per the **writing-for-agents** skill.
- `new skill via create-skill: <kebab-name>`: create it per the **writing-for-agents** skill. Do not invent the shape ad hoc.
- Environment change: make the edit the environment reviewer named, preferring a check over a written rule.

If your environment ships a SKILL.md validator, run it on every touched skill before declaring done.

## 6. Summarize for the user

Short list, no preamble:

- Edits applied: `<skill path>`. What changed, one line each, with the PR link.
- Environment changes: `<file>`. What changed, one line each, with the PR link.
- New skills created: `<skill path>`. One line each (rare).
- Backlog: one line each.
- Dropped: one line per rejected finding + reason from the synthesizer.
