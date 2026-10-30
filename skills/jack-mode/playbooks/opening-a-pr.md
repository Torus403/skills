### Opening a PR

Invoked at the end of every other playbook that changes code.

**Branch.** Work on a branch off the default branch named `type/short-desc`, with the same types as the commits, such as `feat/saved-searches`, `fix/login-redirect`, or `chore/bump-deps`. Lowercase, hyphenated, no ticket ids. Subagents inherit it. Parallel subagents on the same branch each get their own worktree.

**Commits.** Conventional Commits `type(scope): subject`, no trailing period. Type such as `feat`, `fix`, `docs`, `refactor`, `test`, `chore`, `perf`, `build`, or `ci`. Commit as often as is useful. Size does not matter, because the PR squash-merges. Commit bodies don't restate the subject.

**Before review.** Run the **deslop** skill over the diff, then the **no-comments** skill. Then run the **thermos** skill, the **spec-review** skill, and the `style-reviewer` subagent side by side, and fix every finding that holds up. Then run the `consistency-reviewer` subagent last, on the final diff, with the goal in one sentence. It checks the repo's conventions, reuse of the existing code paths, and that every hunk serves the goal. Drop or split out each hunk it flags as out of scope, and fix the rest that holds up. Run the repo's lint, typecheck, and tests. Write the title, the description, and commit bodies with the **technical-writing** skill, then the **unslop** skill.

**Title.** Conventional Commits `type(scope): subject`. Scope is the area. Subject is short, imperative, and names a real symbol when one carries the change, for example `feat(search): add saved searches`. The title becomes the squash commit subject.

**Size.** One PR per piece of work. A feature or epic is one big PR on one branch. A small fix or ticket is its own small PR. Never stack PRs.

**Description.** A one-minute briefing for a reviewer who has the diff. Short, simple sentences. Use these `##` headings in this order, and drop a section with nothing to say:

- `## Why`: Jack's goal and the problem, 1 to 3 short sentences.
- `## Summary`: the smallest visual that makes the change clear, per the **pr** skill: a call tree, file tree, component tree, pseudocode, a `diff` sketch, or a Mermaid diagram.
- `## What changed`: 1 to 5 short bullets. Name a real symbol or path only when it carries the change.
- `## Evidence`: before and after. Screenshots for a visual change. Otherwise the test or command that failed and now passes, or the real run and its output.
- `## Tradeoffs`: only alternatives a reviewer would otherwise ask about. Skip when there was no real choice.
- `## Blast Radius`: one-way or two-way door, then 1 to 2 sentences on who or what it touches and why that is safe or risky.

Link the spec or ADR when there is one. The body becomes the squash commit body, so keep it under about 40 lines.

**Open it.** Use `gh pr create`, ready, never a draft. Run `gh pr view <number>` before you refer to PR status.

**After opening.** Post the URL. Opening a PR does not start a babysit. Run the **Babysit** playbook when Jack asks, or when CI goes red on a PR you own. Never merge. Merging is the **Shipping** playbook, on Jack's call only.
