---
name: python-best-practices
description: Python best practices. Use when reading or editing any .py file.
paths: ["**/*.py"]
---

# Python best practices

Read the **code-style** skill first. These rules add the Python rules on top of it. They favor plain, widely known Python over newer or clever features, even when that means a little more code. Follow the repo's own tooling first: its formatter and linter (usually `ruff`), its type checker, its package manager, and its Python version.

| Rule | Summary |
|------|---------|
| Type hints | Annotate function signatures and dataclass fields. Use the plain forms: `list[str]`, `dict[str, int]`, `str \| None`. |
| Dataclasses for records | Use `@dataclass` for plain data. Add `frozen=True` when the record should never change. Classes with methods only for real state, per the **code-style** skill. |
| Parse at the boundary | Where data crosses in (HTTP, CLI, env, files, queues), parse it once into a dataclass or the repo's schema model (such as `pydantic`), and trust it inside. See the **boundary-discipline** principle skill. |
| Plain branching | Use `if`/`elif` and `isinstance`, not `match` statements. End a branch over known cases with a `raise` for the case nobody handled. |
| Plain loops | Use a `for` loop when a comprehension would nest, filter twice, or need a walrus (`:=`). A single, flat comprehension is fine. |
| No clever features | No metaprogramming, no decorators you write yourself, no `__getattr__` tricks, no dynamic `setattr`. Plain code a newcomer can follow. |
| No `Any` | Avoid `typing.Any`. Use a real type, or `object` for data you haven't parsed yet. |
| No mutable defaults | Never `def f(items=[])`. Use `None` and create the list inside, or an immutable default such as `()`. |
| Narrow exceptions | Catch the specific exception you can handle. No bare `except:` and no `except Exception: pass`. Re-raise with `raise ... from error` to keep the cause. |
| Resources in `with` | Files, locks, and connections open in a `with` block. Use `pathlib.Path` for paths. |
| Keyword arguments | Past three parameters, make the rest keyword-only (`*,`) so call sites read clearly. |
| Real tests | Use `pytest`. Don't mock what you can run: use `tmp_path`, a real test database, and the real code. Mock only what you can't run locally. |
| Logging | Use the `logging` module (or the repo's logger) with enough context to debug from an id. No `print` in shipped code. |

Examples: `references/patterns.md`.
