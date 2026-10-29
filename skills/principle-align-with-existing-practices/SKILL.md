---
name: principle-align-with-existing-practices
description: "Apply before designing or writing anything in an existing codebase. Match how the codebase already solves this kind of problem before inventing a new way."
disable-model-invocation: true
---

# Align with Existing Practices

A codebase that does one thing two ways is harder to read than either way alone. Consistency beats local cleverness.

- **Find the closest example first.** Before designing, find where the codebase already does the most similar thing. Read it. Copy its shape: file layout, naming, error handling, data access, test style, and libraries.
- **Use what is already there.** Reach for the repo's existing utilities, components, and dependencies before adding a new one. A new dependency needs a reason the existing ones can't meet.
- **Follow the written rules.** Read `CLAUDE.md`, `AGENTS.md`, lint and format config, and any docs in `docs/`. They win over your defaults.
- **Invent only for real gaps.** When the codebase has no answer, pick the simplest one that fits its style, and say in the PR that it's a new pattern.
- **Disagree in the open.** If the existing practice is wrong, say so and propose the change as its own decision. Don't quietly do it differently in one place.
