# skills

Jack's agent skills for Claude Code and Codex. They are built from [pstack](https://github.com/cursor/plugins/tree/main/pstack) by poteto, [Matt Pocock's skills](https://github.com/mattpocock/skills), and Cursor's [thermos](https://github.com/cursor/plugins/tree/main/thermos) and [team kit](https://github.com/cursor/plugins/tree/main/cursor-team-kit), then adapted to how Jack works.

## How Jack works

- **Align first.** Match how the codebase already does things before inventing anything.
- **Plan deeply, up front.** The agent grills Jack with questions and recommendations until nothing is left to guess, then builds to the end without stopping.
- **Simple wins.** The least fancy design with the fewest moving parts and the least logic, with no bugs, crashes, or surprises.
- **Docs only for big things.** Specs for new features, core logic, and architecture go in `.jack/specs/`. Architecture decisions go in `.jack/adr/`. Small work gets none.
- **Nothing extra in git.** Every file the skills write into a repo, other than the task's code, goes in the repo's `.jack/` folder. The skills keep it out of git with `.git/info/exclude`, so it never shows on GitHub and the repo's `.gitignore` stays untouched.
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

### Cloud sessions (claude.ai/code and project threads)

Cloud sessions start from a fresh clone and never install a plugin that a repo's `.claude/settings.json` turns on, so committing that file would not help. Install the skills from the environment's setup script instead. The script lives in the environment settings on claude.ai, not in any repo:

```bash
#!/bin/bash
git clone --depth 1 https://github.com/Torus403/skills.git /tmp/jack-skills && /tmp/jack-skills/install.sh || true
mkdir -p ~/.config/git && grep -qxF '.jack/' ~/.config/git/ignore 2>/dev/null || echo '.jack/' >> ~/.config/git/ignore
```

Add it under **Setup script** on each environment you use. For a project, pick or add that environment in the project's settings. The environment caches the script's result for about seven days, so a new commit here reaches cloud sessions within a week. Edit the script to refresh it sooner.

### Your own machine

The skills add `.jack/` to each clone's `.git/info/exclude` on first write. To cover every repo at once, also add it to your global git ignore file:

```bash
mkdir -p ~/.config/git && grep -qxF '.jack/' ~/.config/git/ignore 2>/dev/null || echo '.jack/' >> ~/.config/git/ignore
```

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
| `agents/` | Subagents for Claude Code: `jack-agent`, `comment-sicko`, `style-reviewer`, `consistency-reviewer`, and the two thermos reviewers. |
| `upstream/` | Untouched copies of every source, with their licences. Never loaded as skills. |
| `scripts/check.py` | Checks every skill's frontmatter, Codex file, and cross-references. |
| `scripts/sync_upstream.py` | Refreshes `upstream/` from the sources in `upstream/sources.json`. `.github/workflows/sync-upstream.yml` runs it weekly and opens a PR. |

## Credits

The skills in `skills/` are adapted from MIT-licensed work by Lauren Tan (poteto), Matt Pocock, and Cursor. The original licences and an unedited copy of each source live in [`upstream/`](./upstream/README.md). The four `ui-*` skills are adapted from unslop by Damir Sokolovsky (CC BY 4.0), Anthropic's frontend-design and Paul Bakaus's Impeccable (Apache 2.0), and MIT-licensed work by Vercel, Emil Kowalski, Jakub Krehel and Leonxlnx. They are not tracked in `upstream/`, and each skill's `NOTICE.md` lists its sources, changes and licences. Seven of Emil Kowalski's skills (`emil-design-eng`, `animate`, `review-animations`, `animation-performance`, `mobile-native`, `pick-ui-library`, `break-ui`) ship unchanged apart from dropping their canned first reply, with the MIT licence in each folder. The `seo` skill is adapted from MIT-licensed work by Addy Osmani, Corey Haines, agricidaniel and TanStack, checked against Google Search Central (CC BY 4.0), and its `NOTICE.md` lists its sources. The `aeo` skill is adapted from Corey Haines's MIT-licensed ai-seo skill and checked against the crawler and search docs of OpenAI, Anthropic, Google, Perplexity, Apple and Meta, and its `NOTICE.md` lists its sources.
