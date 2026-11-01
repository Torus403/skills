---
name: setup-repo
description: "Set up a repo for Jack's skills: the untracked .jack/ folder, an Agent setup section with the repo's stage (pre-launch or launched), one check command with CI, and the docs layout. Run once per repo, and again when the repo launches."
disable-model-invocation: true
---

# Set up a repo

Adapted from Matt Pocock's `setup-matt-pocock-skills`, without the issue tracker or triage labels. It sets up three things:

1. **The Jack folder**, `.jack/`, which git never tracks, for specs, scratch, and decision logs.
2. **An `## Agent setup` section** in the repo's `AGENTS.md` (or `CLAUDE.md` when there is no `AGENTS.md`) that every skill reads: the stage, the check command, and where the docs live.
3. **A mechanical baseline**: one `check` command and a CI job that runs it on every PR. NASA's tenth rule and Google's presubmits make this non-negotiable, because a rule a tool enforces never needs repeating.

This is a prompt-driven skill, not a script. Explore, present what you found with a recommendation, confirm with Jack, then write. Items 2 and 3 change tracked files, so they ship as a PR on `chore/agent-setup` through the Opening a PR playbook in `../jack-mode/playbooks/opening-a-pr.md`.

## 1. Explore

Read whatever exists. Don't assume.

- `.jack/` at the root of the main checkout, and `/.jack/` in `.git/info/exclude`.
- An existing `## Agent setup` section in `AGENTS.md` or `CLAUDE.md`.
- `GLOSSARY.md`, `GLOSSARY-MAP.md`, the legacy `CONTEXT.md` or `CONTEXT-MAP.md`, `docs/adr/`, and any other folder the repo uses for decisions.
- Monorepo signals: `pnpm-workspace.yaml`, a `workspaces` field in `package.json`, a `uv` workspace, or several `packages/*` each with its own source.
- The tools already in place: formatter, linter and its rules, type checker and how strict it is, test runner, lockfile, CI workflows, and any audit or secret scan.
- Signs of real users: a production deploy config, a live domain, production database migrations already applied.

## 2. Present and ask

Summarize what's there and what's missing. Ask each item with your recommendation first, so Jack can accept in a word.

**Stage.** `pre-launch` or `launched`. Recommend from the signs of real users. The stage decides how jack-mode treats migrations and contracts (Standing rules in `../jack-mode/SKILL.md`). Anything other than an explicit `launched` counts as pre-launch.

**Check command.** One command that runs every fast check and exits non-zero on any failure. Use the repo's package manager and tools. Recommend what's missing from this list:

| Check | TypeScript | Python |
| --- | --- | --- |
| Format | the repo's formatter in check mode (`prettier --check`, `biome format`) | `ruff format --check` |
| Lint, errors only, no warnings | `eslint --max-warnings 0` with `typescript-eslint` recommended rules, or `biome lint` | `ruff check` |
| Strict types | `tsc --noEmit` with `strict: true` | `pyright` (strict for new code) or `mypy --strict` |
| Existing tests | the repo's runner | `pytest` |
| Dependency audit | `npm audit --audit-level=high` or the package manager's equivalent | `pip-audit` |
| Secrets | `gitleaks detect` in CI | the same |

Name it `check` where the ecosystem allows it: a `check` script in `package.json`, a `check` target in a `Makefile`, or `scripts/check`. Never weaken an existing rule to make the baseline pass. Fix the code, or list the existing violations for Jack and recommend fixing them in this PR when there are few.

**CI.** A workflow that runs the check command on every pull request, plus the secret scan. Reuse an existing workflow if one exists.

**Docs layout.** Recommend a single context: `GLOSSARY.md` at the root and `docs/adr/`, both tracked, plus `.jack/specs/` for specs. Offer multi-context (`GLOSSARY-MAP.md` pointing to `docs/contexts/<context>/GLOSSARY.md` per package) only when exploration found monorepo signals.

## 3. Confirm and write

Show the draft section and the check command, and let Jack edit before writing.

1. Set up the Jack folder and its exclude line per the Files you write in a repo section of `../jack-mode/references/harness.md`.
2. Write the section:

   ```md
   ## Agent setup

   - Stage: pre-launch
   - Check: `pnpm check`
   - Glossary: `GLOSSARY.md`. Decisions: `docs/adr/`. Specs: `.jack/specs/` (untracked).
   ```

   Add a `Runbook:` line once the **production-readiness** skill writes one.
3. Add the check command, its config, and the CI workflow.
4. Run the check command and show it passing.
5. Open the PR.

Don't create `GLOSSARY.md` or `docs/adr/` up front. The **domain-modeling** skill creates them when there is something to put in them.

## 4. Done

Tell Jack the stage, the check command, and the PR link. Every skill now runs the check command before each commit, and the Opening a PR playbook uses it as its mechanical gate.

**When the repo launches**, run this skill again to flip `Stage:` to `launched`, then run the **production-readiness** skill.
