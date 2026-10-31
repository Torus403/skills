---
name: grilling
description: Grill the user relentlessly about a plan, decision, or idea. Use when the user wants to stress-test their thinking, or uses any 'grill' trigger phrases.
---

Interview the user relentlessly until you reach a shared understanding. Map this as a **design tree**: every decision branches into the decisions that hang off it.

Spend the user's attention on judgement calls only. The codebase already answers many decisions, and the user should not have to remember how it was done before.

## Sweep for precedent first

When there is a codebase, sweep it before round one. Dispatch a read-only sub-agent with a fresh context window to find the task's nearest relatives, not one example:

- Code that does the same kind of thing: sibling features, the same layer in another module, and the tests around them.
- How similar changes were made: `git log` on those files, and past commit and PR messages.
- The written rules: `AGENTS.md`, `CLAUDE.md`, lint config, ADRs, specs, and the Jack folder (`.jack/`).

It returns a **precedent map**: for each part of the task, the closest existing example with `file:line`, and every place the codebase does the same thing two ways. Sweep again whenever an answer opens a part of the tree the map does not cover.

## Sort every decision

Before each round, sort every frontier decision into one of four kinds. Only the last becomes a question.

| Kind | What it is | What you do |
| --- | --- | --- |
| **Fact** | How the code or environment behaves | Look it up and trace it (below). |
| **Precedent** | The precedent map answers it, with one consistent way | Follow it. List it under "Following the codebase" with its `file:line`. |
| **Your call** | No precedent, cheap to change later, and one answer is clearly best | Decide it. List it under "My calls" with a one-line reason. |
| **Judgement call** | Everything else | Ask it, with your recommendation. |

These are always judgement calls, whatever the precedent says:

- **Data models and database design.** Propose the full shape: every table or model, every column with its type, nullability, keys, and indexes, the relations, and why each one is needed. Show which existing model you copied it from. The user reviews and approves every model before you build.
- **Anything a user sees or reads.** Pages, views, components, emails, notifications, copy, and error messages. Propose and recommend, then wait for the user's approval.
- **Product behavior and scope.** What the feature does, its edge cases, and what is out.
- **Hard-to-undo steps.** Migrations that drop or rewrite data, public APIs, and anything shipped outside the repo. Ask, but recommend the migration or contract change when it gives the cleaner design. Never steer away from one only because it is a migration.
- **Conflicting precedent.** Where the codebase does it two ways, picking one is a convention decision.

When unsure whether something is your call, ask it.

## Ask in rounds

Work the tree in **rounds**. The **frontier** is every decision whose prerequisites are already settled: the questions you can ask _now_ without guessing at answers you haven't heard yet. Open each round with the "Following the codebase" and "My calls" items you settled since the last round, numbered so the user can say "flip 3" to turn one into a question. Then ask every judgement call on the frontier, each with your recommended answer. Wait for the user's answers before the next round.

A round with more than about five questions is a smell. Re-sort it before you send it: most of a big round is usually precedent or your own call.

Ask through the harness's question tool, so the questions show as native cards: `AskUserQuestion` in Claude Code, `request_user_input` in Codex. Give each question two or more options, the recommended one first with "(Recommended)" at the end of its label. The tools' limits and fallbacks are in the Asking questions section of `../jack-mode/references/harness.md`.

Where the tool is missing, or a question has no sensible options, ask in text. Number each question and format the round like so:

```
📐 **Following the codebase**
1. <decision>: <what you will do>, as in `<file:line>`

🧭 **My calls**
2. <decision>: <what you chose>, because <reason>

---

❓ **Q1** - **<question title>**: <question body, might be multiple paragraphs, including multiple choices>

➡️ <your recommended answer>

---

❓ **Q2** - **<question title>**: <question body, might be multiple paragraphs, including multiple choices>

➡️ <your recommended answer>
```

With the question tool, send the two lists as text just before the cards. In text, word each question so "yes" accepts your recommended answer.

Each round the user answers reshapes the tree: settled decisions push the frontier outward and unblock questions that depended on them. Recompute the frontier and ask the next round. A question whose answer depends on another question still open in this round belongs to a _later_ round, not this one.

Finding _facts_ is your job, never the user's. When a frontier question needs a fact from the environment (filesystem, tools, etc.), dispatch a sub-agent with a fresh context window to find it; don't ask the user for anything you could look up yourself. The facts you state are yours to check too. Before a question, an option, or a recommendation says how the code behaves, read the code that does it and trace it from where it is called, so you know it is wired up and not only defined. A downside you give for an option is a fact like any other. Don't block on exploration: a fact still being explored is an unsettled prerequisite, so only the questions that rest on it wait for the sub-agent to report; ask the rest of the frontier now. The _judgement calls_ are the user's: put each to them and wait.

For a design choice, put the simplest option first, per the **principle-fewest-moving-parts** skill: the one where every case works the same way. Recommend it unless the code shows it can't work.

The session is done when the frontier is empty: every branch of the design tree visited, nothing left silently assumed. Sum up the shared understanding as one plan, with every "Following the codebase" and "My calls" item in it, and do not act on it until the user confirms it. When the user answered a question with a convention that holds beyond this task ("we always do X here"), add a final plan item that proposes one line for the repo's `AGENTS.md`, so the next sweep finds it. Write it only once the user approves it in the plan. In plan mode, present it in the harness's plan form (`ExitPlanMode` in Claude Code, a `<proposed_plan>` block in Codex), so the user approves it in one click.
