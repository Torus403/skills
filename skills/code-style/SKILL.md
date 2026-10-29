---
name: code-style
description: Jack's coding style for TypeScript and Python. Use before writing, editing, or reviewing any code, so it reads dead simple, plain, and consistent.
---

# Code style

Code should be dead simple to read. It mixes Ousterhout's deep modules with the readable parts of Uncle Bob's Clean Code, and it prefers plain, vanilla code over anything clever. When the repo already has a style, match it first (the **principle-align-with-existing-practices** skill). These rules fill the gaps.

Read the examples for the language you're writing before you write: [`examples/typescript.md`](examples/typescript.md) and [`examples/python.md`](examples/python.md). Copy their shape.

## Functions and modules

- **A function reads top to bottom as one story.** Let it be as long as the story needs. Don't chop it into tiny functions.
- **Inline single-use helpers.** A function called from one place stays inline in its caller, unless it hides real complexity behind a simple interface.
- **Extract only for a reason.** The code is reused, or it is a deep module: a small, simple interface over a lot of behavior that callers never need to see.
- **Deep over shallow.** A module earns its place by hiding decisions. A wrapper that only renames or passes through is deleted.
- **Plain functions and plain data.** Use classes only for real state with a lifecycle, or where the codebase already uses them.

## Layout

- **Let lines breathe.** Split each logical step inside a function with a blank line. The blank line is the marker. Don't add a comment to name the step.
- **Section banners for big files.** In a file long enough to have distinct parts, mark each part with a banner. Use the same banner format everywhere:

  ```ts
  // ------------------------------------------------------------
  // Parsing
  // ------------------------------------------------------------
  ```

  ```python
  # ------------------------------------------------------------
  # Parsing
  # ------------------------------------------------------------
  ```

  Small files get no banners.
- **Order a file for the reader.** Put the public entry point first and the details it uses below it, so the file reads downward.

## Names

- **One plain-English term per concept.** Pick one word for each idea and use it everywhere: in code, tests, logs, and docs. If the repo has a `GLOSSARY.md`, use its terms. Never use two words for one thing.
- **Prefer longer, descriptive names.** `unpaidInvoicesByCustomer` beats `invs`. A name should say what the thing holds or does without a comment.
- **No abbreviations** except ones every reader knows (`id`, `url`, `html`).

## Control flow

- **Guard clauses first.** Handle the edge cases and return early, so the main path is not nested.
- **Few parameters.** Three at most. Past that, pass one plain object.
- **No flag arguments.** A boolean that switches behavior means two functions, or the caller does the branch.
- **No hidden side effects.** A function does what its name says and nothing else. A function that returns a value doesn't also change state.
- **Simple over clever, even if it's longer.** A plain `for` loop beats a chain of `reduce` calls. An `if`/`else` beats a nested ternary. Use the language features most developers already know. Skip newer or clever ones (metaprogramming, decorators you write yourself, type gymnastics, walrus operators, nested comprehensions) even when they save lines.

## Comments

- **Senior staff judgement, very limited.** Most code gets no comments.
- **Write a comment only for** a non-obvious *why* the code can't show (a workaround forced by a library, a business rule with an outside source), or to point at a non-obvious location ("the retry limit lives in `config/network.ts`").
- **Never** narrate what the code does, label steps, leave commented-out code, or write a long justification. Fix the name or the structure instead.
- **Banners are the one decorative comment**, and only in big files.

## When a rule and the repo disagree

The repo wins. Follow its existing style, and say in the PR that you did.
