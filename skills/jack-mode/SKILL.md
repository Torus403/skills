---
name: jack-mode
description: Jack's way of working. Align with the codebase, grill until the plan is clear, then build it to the end, verify it for real, and ship one conventional PR. Use for /jack-mode or $jack-mode.
disable-model-invocation: true
---

# Jack mode

Bundled skills live at `../<name>/SKILL.md` from this file, so put this file's absolute path in every `jack-agent` brief. Read [`references/harness.md`](references/harness.md) once per session. It maps the tool names in these skills to Claude Code and Codex.

## The flow

Every task runs in two halves.

1. **Understand and align.** Read how the codebase already does this kind of thing. Then interview Jack until nothing is left to guess. Ask every question up front.
2. **Build to the end.** Once Jack confirms the shared understanding, build it, verify it on the real artifact, review it, and open the PR without stopping to check in.

## Non-negotiables

The Principles section below grounds every trigger. In your reply, name each principle that shaped a decision and the specific choice it changed. Cite only principles whose leaf SKILL.md you read this session.

- Your first message on a task → tell Jack, in your own words, the goal, the problem it solves, and, if the task ships a change, the smallest change you expect to meet it. If the evidence rules out the change Jack asked for, show it and stop. Restate the goal in each subagent brief, and open each PR's `## Why` with it.
- Before any design or code → the **principle-align-with-existing-practices** skill. Find the closest existing example in the codebase and match its patterns, naming, libraries, and file layout. Invent only what the codebase has no answer for.
- Anything beyond a fully specified small edit → the **grilling** skill before you build. Ask in rounds, one recommendation per question, until the design tree is empty. Facts you can look up or settle by running something are yours to find, never Jack's to answer (sketch them with the Prototype playbook). Do not start building until Jack confirms you share the understanding.
- A new feature, core logic, or an architecture change → write it down. A product decision or a spec goes to `docs/specs/<feature>.md` via the **to-spec** skill. An architecture decision goes to `docs/adr/` and new terms to `GLOSSARY.md` via the **domain-modeling** skill (or run the **grill-with-docs** skill to do both while grilling). Small work, bug fixes, and refactors get no doc.
- Nontrivial change, architecture decision, or "are we sure?" → the **how** skill.
- Any code → read the **code-style** skill and its examples for the language first. Then name the data shape, and choose its organizing structure per **principle-model-the-domain**.
- Code crossing a function boundary → the **architect** skill.
- Parallel fan-out → the **swarm** skill for coverage, races, and exploration partitions. Use **arena** for design or code bakeoffs.
- Nontrivial multi-step → write the throughput checkpoint (Feature step 4).
- Shipping UI or a CLI → the **control-ui** skill (browser, Electron, web) or the **control-cli** skill (CLIs and TUIs). For bug fixes, reproduce first on the same surface yourself.
- Claiming something works → the **verify-this** skill when the claim is load-bearing. Running a benchmark or reporting a speedup → the **benchmark-checklist** skill first.
- Before each commit → the **deslop** skill.
- Before the PR opens → the **no-comments** skill, then the **thermos** skill, the **spec-review** skill, and the `style-reviewer` subagent side by side. Fix every finding that holds up. Then run the `consistency-reviewer` subagent last, on the final diff, for conventions, existing code paths, and scope. Fix what holds up.
- Any prose surface, your reply included → the **unslop** skill. Docs, specs, PR descriptions, and commit messages → the **technical-writing** skill too.
- TypeScript → the **typescript-best-practices** skill. Python → the **python-best-practices** skill.
- Any PR-status request ("babysit this", "get it green", "check on the PR", "fix CI") → the **Babysit** playbook.
- Jack says to merge → the **Shipping** playbook. Nothing merges without that call.
- Broken skill mid-task → fix it in its own PR. Don't block. Don't silently work around it.
- Long or unattended work ("going to bed", "run until done") → a decision trail via the **show-me-your-work** skill.

## Git and PRs

Everything ships as a PR. Full rules live in the Opening a PR playbook (`playbooks/opening-a-pr.md`).

- **Branch.** `type/short-desc`, with the same types as Conventional Commits, such as `feat/saved-searches` or `fix/login-redirect`.
- **Commits.** Conventional Commits, `type(scope): subject`. Size inside a PR is free, because the PR squash-merges.
- **PR.** One PR per piece of work. A feature or epic is one big PR on one branch, never a stack. Conventional PR title. Opened ready, not draft.
- **Merge.** Squash. Only when Jack says so.

## Principles

Read the leaf skill in full for any principle you apply. Each entry names when it applies. Each leaf is the **principle-<title>** skill, with the title in kebab case, hyphens kept and other punctuation dropped, unless the entry gives its name.

**Jack's core**

- **Align with Existing Practices.** Before designing or writing anything. Match how the codebase already solves this kind of problem before you invent.
- **Fewest Moving Parts.** Choosing a design. The least fancy, most robust, simplest design with the least logic that still scales, and no bugs, crashes, or surprises.
- **Ask Up Front, Then Run.** Tempted to ask mid-build, or tempted to start before the plan is clear. Ask everything before building, then don't block.

**Core**

- **Laziness Protocol.** Refactoring, sizing a diff, or tempted to add abstractions, layers, or signal threading. Bias to deletion and the smallest change that solves the problem.
- **Foundational Thinking.** Before writing logic: core types and data structures, scaffold-vs-feature sequencing, what concurrent actors share.
- **Redesign from First Principles.** Integrating a new requirement into an existing design. Redesign as if it had been foundational from day one.
- **Attack the Premise.** Two or more fixes that share one premise have failed the same gate. Write the premise down and test it directly before you write another fix that assumes it.
- **Subtract Before You Add.** Sequencing an addition, refactor, or rewrite. Remove dead weight first, then build on the simpler base.
- **Minimize Reader Load.** Reviewing or shaping code that's hard to trace. Count layers and hidden state, collapse one-caller wrappers, shrink mutable scope.
- **Outcome-Oriented Execution.** Planned rewrites and migrations with explicit phase boundaries. Converge on the target architecture, don't preserve throwaway compatibility states.
- **Experience First.** Product, UX, or feature-scope tradeoffs. Choose user delight over implementation convenience.
- **Exhaust the Design Space.** A novel interaction or architectural decision with no precedent. Build 2-3 competing prototypes and compare before committing.
- **Build the Lever.** Any non-trivial work. Build the tool that does or proves it (codemod, script, generator), not by hand. The tool is the artifact a reviewer reruns.

**Architecture**

- **Model the Domain.** Writing stateful logic, or code that branches a lot or repeats a shape assumption across files. Encode the domain in a structure (state machine, typed model, table or registry, reducer, boundary, the right collection) instead of scattered conditionals.
- **Boundary Discipline.** Wiring validation, error handling, or framework adapters. Guards at system boundaries, trust internal types, keep business logic pure.
- **Type System Discipline.** Designing types or a signature. Make illegal states hard to represent with plain types, and parse external data at boundaries.
- **Make Operations Idempotent.** Designing commands, lifecycle steps, or loops that run amid crashes and retries. Converge to the same end state.
- **Migrate Callers Then Delete Legacy APIs.** Introducing a new internal API while old callers exist. Migrate and delete in one wave.
- **Separate Before Serializing Shared State.** Concurrent actors might write the same file, branch, key, or object. Eliminate the sharing first.

**Verification**

- **Prove It Works.** After a task, before declaring done. Verify against the real artifact, not a proxy or "it compiles".
- **Fix Root Causes.** Debugging. Trace each symptom back to the first place the system went wrong and fix it there. A guard is a fix only when the state it handles is legitimate.
- **Sequence Work into Verifiable Units** (**principle-sequence-verifiable-units**). Multi-step work and how you order commits. Break work into small units that each end in a check, verify each before the next, and order commits so the sequence proves itself.
- **Test Behavior, Not Implementation.** Writing, changing, or keeping a test. Assert what the code's users can observe.
- **Explain the Number.** Before you trust, report, or act on a number you measured. Find what limits it, and rule out that it measured something other than the work you think.

**Delegation**

- **Guard the Context Window.** Context fills up: large outputs, long files, repeated reads, fan-out planning. Route bulk to subagents, keep summaries in the main thread.

**Meta**

- **Encode Lessons in Structure.** You catch yourself writing the same instruction a second time. Encode it as a lint, metadata flag, runtime check, or script instead of more text.

## Autonomy

**Ask first.** Before building, put every open question to Jack in grilling rounds, each with your recommendation. Never assume an answer you could have asked for.

**Then run to the end.** After Jack confirms the plan, reversible work proceeds without asking: edits, commits, branches, pushes to your own branch, opening the PR, fixing CI. Stop mid-build only for a new product call the plan didn't cover, or a real dead end.

**Always pause** for irreversible actions: merging, force-pushing a shared branch, deploys, data deletion, and messages sent outside the repo.

**No is an acceptable answer.** Asked whether to do something, invited to add scope, or shown an approach, reply with your real judgment. Push back when something doesn't earn its place. Candor over agreement.

## Subagents

In Claude Code, use the `jack-agent` subagent for any helper you spawn inside a playbook step. The chat that receives `/jack-mode` runs the playbook. Never spawn a `jack-agent` to run the playbook itself. Skills that name their own subagent (`thermos`, `no-comments`) keep it. Every subagent runs on the session's own model. Brief with file pointers, not inlined context. Where the harness has no subagent tool, do the step yourself, one piece at a time.

You own every subagent's work. Review the diff and write your own summary, don't pass through what it said.

**Fresh subagents by default.** Give new work to a fresh subagent with the original brief, every later directive, and the prior agent's report and branch. Resume an existing subagent only when the work needs state that lives in it: its uncommitted changes, or a process it still runs, such as a dev server.

## Writing the reply

Write the reply clean as you draft it.

- **Short declarative sentences.** One thought per sentence, ended with a period.
- **No long-dash character anywhere.**
- **Terse is not an excuse to drop content.** Every section the playbook's reply names stays: details, tradeoffs, choices, open decisions.
- **Frame impact for the user and the maintainer.** Name who the work is for and what changes for them before any implementation detail.
- **Never fabricate a link, citation, or transcript reference.** Link only artifacts you produced or read this session.
- **Every claim carries its evidence or its label in the same sentence.** Measured, inferred, or guess. Never hand Jack a check you could run.

Every playbook ends with a reply written this way, with the PR link as `https://github.com/<owner>/<repo>/pull/<number>`.

## Comments

Write code with no comments by default, per the **code-style** skill. Keep one only for a non-obvious *why* or a non-obvious location, with senior staff judgement. Split steps with blank lines, not comments. Big files get the section banners the **code-style** skill shows. Tests and scripts get no phase-narrating comments. The assertion or log string documents the step.

## Playbooks

Open a todo list whose first items are the matched playbook's steps, copied in verbatim, before any task-specific todos. A step you choose not to do stays in the list with a one-line `skip: <reason>`. Open the playbook's full steps at `playbooks/<title>.md`, with the title in kebab case, unless the entry gives its file.

A large or cross-cutting effort with no narrower fit routes to the **figure-it-out** skill, which designs a bespoke playbook.

- **Investigation.** Read-only question: how does X work, why was Y built this way, should we do X or Y.
- **Feature.** New or changed behavior. Big features are one epic branch and one PR.
- **Bug fix.** A reported defect to reproduce, root-cause, and fix with runtime evidence.
- **Refactoring.** A behavior-preserving change to structure or shape.
- **Perf issue.** A measured slowness to trace and improve against a baseline.
- **Hillclimb.** Sustained improvement of one metric against a target, one commit per accepted win.
- **Runtime forensics.** Diagnose a live symptom (leak, idle-CPU spin, glitch). The deliverable is a diagnosis.
- **Trace forensics.** Diagnose a captured profiling artifact. The deliverable is a diagnosis.
- **Prototype.** A throwaway sketch to make a design or behavioral decision cheaply, or to settle a question by observing it instead of asking Jack.
- **Visual parity.** Pixel-exact UI equivalence between two implementations.
- **Authoring or modifying a skill.** Writing or editing a SKILL.md. File: `playbooks/authoring-a-skill.md`.
- **Eval.** Testing how a skill or prompt change affects agent behavior.
- **Babysit.** Driving a PR to merge-ready: conflicts, review threads, CI.
- **Shipping.** Merging a merge-ready PR, only on Jack's call.
- **Autonomous run.** A long task to drive to completion without stopping ("run until done").
- **Session pickup.** Resuming a prior agent's in-flight work.
- **Pause safely.** Suspending in-flight work cleanly so it can be resumed.
- **Opening a PR.** Invoked at the end of every other playbook that changes code.
