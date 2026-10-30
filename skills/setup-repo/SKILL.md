---
name: setup-repo
description: "Set up a repo for Jack's skills: create the untracked .jack/ folder where specs, ADRs, and the glossary live, and keep it out of git. Run once per clone."
disable-model-invocation: true
---

# Set up a repo

Adapted from Matt Pocock's `setup-matt-pocock-skills`, without the issue tracker or triage labels. Jack plans in conversation and keeps big decisions in the Jack folder, `.jack/`, which git never tracks. This skill changes no tracked file: no `AGENTS.md` or `CLAUDE.md` block, no `docs/` folder, no `.gitignore` line, no branch, and no PR.

This is a prompt-driven skill, not a script. Explore, present what you found with a recommendation, confirm with Jack, then write.

## 1. Explore

Read whatever exists. Don't assume.

- `.jack/` at the root of the main checkout, and `/.jack/` in `.git/info/exclude`: does this skill's earlier output already exist?
- The repo's tracked docs: `GLOSSARY.md`, `GLOSSARY-MAP.md`, the legacy `CONTEXT.md` or `CONTEXT-MAP.md`, `docs/adr/`, `docs/specs/`, and any other folder the repo uses for decisions or specs. These belong to the team. The skills read them and never write to them.
- Monorepo signals: `pnpm-workspace.yaml`, a `workspaces` field in `package.json`, a `uv` workspace, or several `packages/*` each with its own source.

## 2. Present and ask

Summarize what's there and what's missing. Then ask, leading with the recommendation so Jack can accept it in a word.

**Docs layout.** Recommend a single context: `.jack/GLOSSARY.md`, `.jack/adr/`, and `.jack/specs/`. Offer multi-context (`.jack/GLOSSARY-MAP.md` pointing to `.jack/contexts/<context>/GLOSSARY.md` per package) only when exploration found monorepo signals. Name any tracked docs the skills will read as the team's.

## 3. Confirm and write

Show a draft of `.jack/domain.md` and let Jack edit before writing.

1. Set up the Jack folder and its exclude line per the Files you write in a repo section of `../jack-mode/references/harness.md`.
2. Write `.jack/domain.md` from [domain.md](./domain.md), with the layout Jack chose and a line naming any tracked docs the repo already has.
3. Run `git status --porcelain` and confirm it shows nothing new.

Don't create `GLOSSARY.md`, `adr/`, or `specs/` up front. The **domain-modeling** and **to-spec** skills create them when there is something to put in them.

## 4. Done

Tell Jack the setup is done, that `git status` is clean, and which skills read these files: `jack-mode`, `grill-with-docs`, `domain-modeling`, `to-spec`, `spec-review`, `tdd`, and `improve-codebase-architecture`.

A cloud session starts from a fresh clone, so `.jack/` starts empty there. The skills create it again on their first write.
