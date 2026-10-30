# Upstream sources

Verbatim copies of the skill repos this one builds on. Nothing in this folder is edited by hand. Each folder keeps its original `LICENSE` where the source ships one, and every source is MIT licensed. The Vercel repo has no `LICENSE` file, so its folders carry none.

| Folder | Source | Commit | Licence |
| --- | --- | --- | --- |
| `pstack/` | [cursor/plugins `pstack/`](https://github.com/cursor/plugins/tree/main/pstack) by Lauren Tan (poteto), v0.15.36 | `1ba91fc25c0977741dd0e267849e6234b037ed0a` | MIT, Copyright (c) 2026 Lauren Tan |
| `pstack-claude-code-harness/` | [cursor/plugins `harness/pstack/`](https://github.com/cursor/plugins/tree/main/harness/pstack), the generated Claude Code build of pstack that `/plugin install pstack@cursor-plugins` installs | `1ba91fc25c0977741dd0e267849e6234b037ed0a` | MIT, Copyright (c) 2026 Lauren Tan |
| `thermos/` | [cursor/plugins `thermos/`](https://github.com/cursor/plugins/tree/main/thermos) by Cursor, v1.0.0. Thermo-nuclear branch review. | `1ba91fc25c0977741dd0e267849e6234b037ed0a` | MIT, Copyright (c) 2026 Cursor |
| `cursor-team-kit/` | [cursor/plugins `cursor-team-kit/`](https://github.com/cursor/plugins/tree/main/cursor-team-kit) by Cursor. Holds `deslop`, which pstack calls but does not ship. | `1ba91fc25c0977741dd0e267849e6234b037ed0a` | MIT, Copyright (c) 2026 Cursor |
| `mattpocock-skills/` | [mattpocock/skills](https://github.com/mattpocock/skills) by Matt Pocock, v1.3.2 | `a496f5513d4a4cf889bc48e189e579f4b0bdf6aa` | MIT, Copyright (c) 2026 Matt Pocock |
| `vercel-react-best-practices/` | [vercel-labs/agent-skills `skills/react-best-practices/`](https://github.com/vercel-labs/agent-skills/tree/main/skills/react-best-practices) by Vercel. React and Next.js performance rules. | `1a2c79d4e6c4a2283dc2c614b6538cbe1ed5ca62` | MIT, stated in the skill's frontmatter and the repo README |
| `vercel-composition-patterns/` | [vercel-labs/agent-skills `skills/composition-patterns/`](https://github.com/vercel-labs/agent-skills/tree/main/skills/composition-patterns) by Vercel. React component composition patterns. | `1a2c79d4e6c4a2283dc2c614b6538cbe1ed5ca62` | MIT, stated in the skill's frontmatter and the repo README |

`sources.json` names the repo, branch, and path behind each folder, and the commit it was copied at. Its `feeds` map says which of Jack's skills grew from an upstream skill with a different name.

To refresh, run `python3 scripts/sync_upstream.py`. It replaces each folder whose upstream tree changed and updates the commits here. `.github/workflows/sync-upstream.yml` runs it every Monday and opens a `chore/sync-upstream` PR that lists the changed upstream skills next to Jack's versions to check. It never touches `skills/` or `agents/`.
