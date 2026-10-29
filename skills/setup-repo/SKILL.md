---
name: setup-repo
description: "Set up a repo for Jack's skills: where specs, ADRs, and the glossary live, and the agent-skills block in AGENTS.md and CLAUDE.md. Run once per repo."
disable-model-invocation: true
---

# Set up a repo

Adapted from Matt Pocock's `setup-matt-pocock-skills`, without the issue tracker or triage labels. Jack plans in conversation and keeps only big decisions in the repo.

Scaffold the per-repo configuration the skills assume:

- **Docs layout**: where `GLOSSARY.md`, ADRs, and specs live.
- **Agent file**: a short `## Agent skills` block that points agents at those docs, readable from both Claude Code and Codex.

This is a prompt-driven skill, not a script. Explore, present what you found with a recommendation, confirm with Jack, then write.

## 1. Explore

Read whatever exists. Don't assume.

- `AGENTS.md` and `CLAUDE.md` at the repo root. Does either exist? Does either already have an `## Agent skills` section? Does `CLAUDE.md` already import `@AGENTS.md`?
- `GLOSSARY.md` and `GLOSSARY-MAP.md` at the repo root, and the legacy `CONTEXT.md` or `CONTEXT-MAP.md`. If a legacy file exists, offer to `git mv` it to its `GLOSSARY` name.
- `docs/adr/`, `docs/specs/`, and any existing docs folder the repo already uses for decisions or specs. Prefer the repo's existing folder over a new one (the **principle-align-with-existing-practices** skill).
- `docs/agents/`: does this skill's earlier output already exist?
- Monorepo signals: `pnpm-workspace.yaml`, a `workspaces` field in `package.json`, a `uv` workspace, or several `packages/*` each with its own source.

## 2. Present and ask

Summarize what's there and what's missing. Then ask, one section at a time, leading with the recommendation so Jack can accept it in a word.

**A. Docs layout.** Recommend a single context: `GLOSSARY.md` at the root, `docs/adr/` for architecture decisions, and `docs/specs/` for feature specs. Offer multi-context (a root `GLOSSARY-MAP.md` pointing to one `GLOSSARY.md` per package) only when exploration found monorepo signals.

**B. Agent file.** Both tools need to read the same rules. Claude Code reads `CLAUDE.md`. Codex reads `AGENTS.md`. Recommend keeping the rules in `AGENTS.md` and making `CLAUDE.md` a one-line `@AGENTS.md` import. If only one file exists and it has real content, recommend moving that content into `AGENTS.md` and leaving the import behind. Never delete content without Jack's yes.

## 3. Confirm and write

Show a draft of the `## Agent skills` block and of `docs/agents/domain.md`, and let Jack edit before writing.

The block:

```markdown
## Agent skills

### Domain docs

[single-context or multi-context]. See `docs/agents/domain.md`.

### Specs and decisions

Specs for new features, core logic, and architecture live in `docs/specs/`. Architecture decisions live in `docs/adr/`. Small work gets no doc.
```

If an `## Agent skills` block already exists, update it in place. Don't touch the surrounding sections.

Write `docs/agents/domain.md` from [domain.md](./domain.md). Don't create `GLOSSARY.md`, `docs/adr/`, or `docs/specs/` up front. The **domain-modeling** and **to-spec** skills create them when there is something to put in them.

Make these changes on a `chore/setup-agent-docs` branch and open a PR per **jack-mode**'s Opening a PR playbook.

## 4. Done

Tell Jack the setup is done and which skills read these files: `jack-mode`, `grill-with-docs`, `domain-modeling`, `to-spec`, `spec-review`, `tdd`, and `improve-codebase-architecture`.
