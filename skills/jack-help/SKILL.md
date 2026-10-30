---
name: jack-help
description: Which skill or playbook fits this? A map of Jack's skills. Type /jack-help with a question.
disable-model-invocation: true
---

# Jack help

Find out what Jack is trying to do, then point at the skill or playbook that fits and give the exact thing to type. Before you describe what a skill does or suggest skipping one, read its `SKILL.md` at `../<name>/SKILL.md`. The one-liners below are for orientation only. In Claude Code a skill is typed `/name`. In Codex it is `$name`.

## Start here

Most work starts with **`/jack-mode`** and a sentence about the task. It aligns with the codebase, grills you, writes a spec or ADR for big work, builds to the end, verifies, reviews, and opens a PR. It picks a playbook (feature, bug fix, refactoring, investigation, perf, babysit, shipping, and more) and pulls in the skills below as the steps need them. Reach for a skill directly only for a one-off job.

## Plan and align

| Want to | Type |
| --- | --- |
| Get interviewed about a plan until every decision is made | `/grill-me` |
| The same, while writing ADRs and glossary terms into the repo | `/grill-with-docs` |
| Turn the conversation into a spec file in `.jack/specs/`, kept out of git | `/to-spec` |
| Have the agent play back your goal before it starts | `/in-your-own-words` |
| Make a prompt deeper before you send it | `/sharpen` |
| Settle the types and module shape before code | `/architect` |
| Find modules worth deepening in a codebase | `/improve-codebase-architecture` |
| Get a bespoke playbook for a big, unusual task | `/figure-it-out` |
| Set up a repo's docs layout for these skills | `/setup-repo` |

## Understand

| Want to | Type |
| --- | --- |
| Learn how a subsystem works | `/how` |
| Learn why something was built this way | `/why` |
| Get a plain, diagram-led explanation of a change | `/teach` |
| Rebuild your recent context on a topic | `/recall` |
| Research a question against primary sources | `research` (the agent picks it up) |
| Catch up on what changed in this chat | `/ketchup` |
| Have the last message said again plainly | `/wait-what` |

## Build and verify

| Want to | Type |
| --- | --- |
| Read Jack's coding style and examples | `code-style` |
| Build test-first | `tdd` |
| Diagnose a hard bug or a perf regression | `diagnosing-bugs` |
| Run N attempts at one task and keep the best parts | `/arena` |
| Fan out N parallel workers into one report | `/swarm` |
| Check a small change for breakage elsewhere | `/blast-radius` |
| Prove a claim with fresh evidence | `/verify-this` |
| Vet a benchmark number | `/benchmark-checklist` |
| Drive a web UI or a CLI to check behavior | `control-ui`, `control-cli` |
| Generate or refresh a repo's verification skill | `/create-verification-skill`, `/maintain-verification-skill` |
| Build a throwaway prototype | `prototype` |
| Walk a human through steps only they can do | `wizard` |
| Keep a decision log for a long run | `/show-me-your-work` |

## Review and ship

| Want to | Type |
| --- | --- |
| Strip AI slop from the diff | `/deslop` |
| Strip comments before review | `/no-comments` |
| Deep bug, security, and maintainability review | `/thermos` |
| Check a diff against Jack's coding style | the `style-reviewer` subagent, or `/jack-mode review the style of this branch` |
| Check the diff matches the spec | `spec-review` |
| Check the diff follows the repo's conventions and code paths and stays in scope | the `consistency-reviewer` subagent, or `/jack-mode check this branch fits the codebase` |
| Fix failing CI | `/fix-ci` |
| Resolve merge conflicts | `/fix-merge-conflicts` |
| Get a PR to green | `/jack-mode babysit this PR` |
| Merge a PR | `/jack-mode merge it` |

## Improve the skills and the repo

| Want to | Type |
| --- | --- |
| Capture what a session taught into skill or repo changes | `/reflect` |
| Turn repeated agent mistakes into checks | `/correct` |
| Write or edit a skill | `/jack-mode write a skill for X` |
| Hand the work to a fresh session | `/handoff` |

## Principles

Short rules that `jack-mode` reads at task start, in `principle-*` folders. Jack's own are `principle-align-with-existing-practices`, `principle-fewest-moving-parts`, and `principle-ask-up-front-then-run`. The rest come from pstack.
