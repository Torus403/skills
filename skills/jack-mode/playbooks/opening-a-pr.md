### Opening a PR

Invoked at the end of every other playbook that changes code.

**Branch.** Work on a branch off the default branch named `type/short-desc`, with the same types as the commits, such as `feat/saved-searches`, `fix/login-redirect`, or `chore/bump-deps`. Lowercase, hyphenated, no ticket ids. Subagents inherit it. Parallel subagents on the same branch each get their own worktree.

**Commits.** Conventional Commits `type(scope): subject`, no trailing period. Type such as `feat`, `fix`, `docs`, `refactor`, `test`, `chore`, `perf`, `build`, or `ci`. Commit as often as is useful. Size does not matter, because the PR squash-merges. Commit bodies don't restate the subject.

**Review waterfall.** Before the PR opens, run these gates in order, one todo item each. A gate passes when its checks are green and every finding that holds up is fixed. Never start a gate before the one above it passes.

1. **Clean.** The **deslop** skill over the diff, then the **no-comments** skill. The diff holds only the task's code: no spec, ADR, glossary, log, note, or generated skill (see Files you write in a repo in `../references/harness.md`).
2. **Architecture.** The **spec-review** skill. The diff builds the agreed plan in the agreed shape and follows the repo's written standards. A wrong shape goes back to the design step of the calling playbook, not to a patch.
3. **Mechanical.** The repo's own format, lint, typecheck, and build commands, from `CLAUDE.md`, `AGENTS.md`, the package scripts, or the CI config. Zero errors and no new warnings. Never disable a rule or add an ignore to pass.
4. **Rules.** The `style-reviewer` subagent, for Jack's style and the language's best practices.
5. **Tests.** The repo's existing test suite is green. Add no tests unless Jack asked for them (Standing rules in `../SKILL.md`). A test that broke because the behavior changed on purpose is updated or deleted in this PR. Never skip or loosen a test to hide a real bug. When Jack did ask for tests, each new behavior has one that fails without the change, per **principle-test-behavior-not-implementation**.
6. **Live.** The change works on the real surface at the current head, through the **control-ui** or **control-cli** skill, with the **verify-this** skill for a load-bearing claim. Write `n/a: <reason>` only when the change has no runtime surface, such as docs or skills.
7. **Deep review.** The **thermos** skill, for bugs, security, breakage, and maintainability.
8. **Fit and scope.** The `consistency-reviewer` subagent, on the final diff, with the goal in one sentence. It checks the repo's conventions, reuse of the existing code paths, and that every hunk serves the goal. Drop or split out each hunk it flags as out of scope.

A fix sends you back up. A fix that changes the shape restarts at gate 2, and any other code change restarts at gate 3. Each gate keeps a receipt: the command and its result, or the reviewer's verdict, with the commit it ran on. Every receipt must be from the final head. Summarize them under `## Evidence`.

**Prose.** Write the title, the description, and commit bodies with the **technical-writing** skill, then the **unslop** skill.

**Title.** Conventional Commits `type(scope): subject`. Scope is the area. Subject is short, imperative, and names a real symbol when one carries the change, for example `feat(search): add saved searches`. The title becomes the squash commit subject.

**Size.** One PR per piece of work. A feature or epic is one big PR on one branch. A small fix or ticket is its own small PR. Never stack PRs.

**Description.** A one-minute briefing for a reviewer who has the diff. Short, simple sentences. Use these `##` headings in this order, and drop a section with nothing to say:

- `## Why`: Jack's goal and the problem, 1 to 3 short sentences.
- `## Summary`: the smallest visual that makes the change clear, per the **pr** skill: a call tree, file tree, component tree, pseudocode, a `diff` sketch, or a Mermaid diagram.
- `## What changed`: 1 to 5 short bullets. Name a real symbol or path only when it carries the change.
- `## Evidence`: before and after. Screenshots for a visual change. Otherwise the repro or command that failed and now passes, or the real run and its output.
- `## Tradeoffs`: only alternatives a reviewer would otherwise ask about. Skip when there was no real choice.
- `## Blast Radius`: one-way or two-way door, then 1 to 2 sentences on who or what it touches and why that is safe or risky. Name every migration and API contract change.

The spec and ADRs live in the untracked Jack folder, so never link them. Put what a reviewer needs from them in the body. The body becomes the squash commit body, so keep it under about 40 lines.

**Open it.** Use `gh pr create`, ready, never a draft. Run `gh pr view <number>` before you refer to PR status.

**After opening.** Post the URL. Opening a PR does not start a babysit. Run the **Babysit** playbook when Jack asks, or when CI goes red on a PR you own. Never merge. Merging is the **Shipping** playbook, on Jack's call only.
