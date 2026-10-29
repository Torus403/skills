---
name: python-best-practices
description: Python best practices. Use when reading or editing any .py file.
paths: ["**/*.py"]
disable-model-invocation: true
---

# Python best practices

The Python counterpart of the **typescript-best-practices** skill. Apply the **type-system-discipline** principle skill first. Follow the repo's own tooling and style before any rule here (the **principle-align-with-existing-practices** skill): its formatter and linter (usually `ruff`), its type checker (`pyright` or `mypy`), its package manager (`uv`, `poetry`, or `pip`), and its Python version.

| Rule | Summary |
|------|---------|
| Type everything | Annotate every function signature and public attribute. Run the repo's type checker in strict mode on the code you touch. Use modern syntax: `list[int]`, `X \| None`, `type` aliases. |
| Tagged unions | Model variants as frozen dataclasses with a `Literal` `kind` field, joined in a union. No bags of optional fields where only some combinations are valid. |
| Exhaustive `match` | `match` on the tag and end with `case _: assert_never(x)` so the type checker flags a new variant you didn't handle. |
| Branded primitives | Use `NewType` for ids and units so they can't be mixed up. Create them only in a validating parse function at the boundary. |
| Immutable by default | `@dataclass(frozen=True, slots=True)` for records. `tuple` and `frozenset` for collections that never change. Never use a mutable default argument. |
| `object` over `Any` | External data is `object` (or the schema library's input type) until parsed. `Any` turns the type checker off. |
| Schemas before guards | Parse external data with the repo's schema library (`pydantic`, `msgspec`, `attrs` with `cattrs`) and derive the type from the model. Don't hand-write field-by-field checks. |
| No unverified `cast` | `cast()` and `# type: ignore` hide bugs. Use them only after validation, with the error code named, such as `# type: ignore[attr-defined]`. |
| Boundary validation | Parse where data crosses in (HTTP, CLI, env, files, queues) into a named domain type. Trust types inside. See the **boundary-discipline** principle skill. |
| `Protocol` for seams | Describe a dependency with a `typing.Protocol` at the seam. Prefer it to an abstract base class you must inherit from. |
| Narrow exceptions | Catch the specific exception you can handle. No bare `except:` and no `except Exception: pass`. Re-raise with `raise ... from err` to keep the cause. |
| Resources in `with` | Files, locks, connections, and temp dirs open in a `with` block. Use `pathlib.Path`, not string paths. |
| Keyword arguments | Use keyword-only parameters (`*,`) for anything past the first one or two, so call sites read clearly. |
| Real tests | Use `pytest`. Don't mock what you can run: use `tmp_path`, a real SQLite or test database, and the real code. Mock only what you can't run locally. Parametrize instead of copying tests. |
| Structured logging | Use the `logging` module (or the repo's logger) with enough context to debug from an id. No `print` in shipped code. |

Examples: `references/patterns.md`.
