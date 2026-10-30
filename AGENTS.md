# Agent rules for this repo

This repo holds Jack's skills. Every skill in `skills/` installs into both Claude Code and Codex.

- **One folder per skill.** `skills/<name>/SKILL.md` with `name` equal to the folder name and a `description`. Put references beside it.
- **Codex file.** Every skill has `agents/openai.yaml` with `interface.display_name` and `interface.short_description`. A skill with `disable-model-invocation: true` also sets `policy.allow_implicit_invocation: false`, and no other skill does.
- **Cross-references.** Name another skill as "the **name** skill" or link `../<name>/SKILL.md`. It must exist.
- **No model routing.** Subagents run on the session's model. Never name a model.
- **Harness names.** Write tool and path names the way `skills/jack-mode/references/harness.md` maps them. Add a row there instead of special-casing a harness in a skill.
- **Never edit `upstream/`.** Refresh it with `python3 scripts/sync_upstream.py`, which replaces each changed folder wholesale and updates `upstream/sources.json` and `upstream/README.md`. A weekly workflow runs it and opens a `chore/sync-upstream` PR. Port upstream changes into `skills/` in a separate PR. To add a source, add it to `upstream/sources.json` and the table, and map renamed skills under `feeds`.
- **Writing.** Follow the **writing-for-agents** and **unslop** skills. No long dashes.
- **Plugin.** The repo root is both the `jack-skills` marketplace and the `jack` plugin (`.claude-plugin/`). Leave `version` out of both manifests so installs track commits.
- **Check before every PR.** Run `python3 scripts/check.py`, `claude plugin validate .`, and `./install.sh` into a scratch `HOME`. The validator's warnings about the missing `version` and the root `CLAUDE.md` are expected.
- **Ship as a PR.** Branch `type/short-desc`, Conventional Commits, a conventional PR title, squash merge.
