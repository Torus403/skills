# Python patterns

Code examples for each rule in `SKILL.md`. Python 3.12 or later. The underlying principles are language-agnostic. See the **type-system-discipline** and **boundary-discipline** principle skills.

## Tagged unions and exhaustive `match`

```python
from dataclasses import dataclass
from typing import Literal, assert_never

# Don't. A bool plus optionals lets contradictory states exist.
@dataclass
class DiffStateLoose:
    loading: bool
    diff: str | None = None
    error: str | None = None

# Do. Only valid states exist.
@dataclass(frozen=True, slots=True)
class Loading:
    kind: Literal["loading"] = "loading"

@dataclass(frozen=True, slots=True)
class Ready:
    diff: str
    kind: Literal["ready"] = "ready"

@dataclass(frozen=True, slots=True)
class Failed:
    error: str
    kind: Literal["failed"] = "failed"

type DiffState = Loading | Ready | Failed

def describe(state: DiffState) -> str:
    match state:
        case Loading():
            return "loading"
        case Ready(diff=diff):
            return f"{len(diff)} chars"
        case Failed(error=error):
            return f"failed: {error}"
        case _:
            assert_never(state)
```

## Branded primitives

```python
from typing import NewType
from uuid import UUID

AgentId = NewType("AgentId", str)

def parse_agent_id(raw: str) -> AgentId:
    UUID(raw)
    return AgentId(raw)

def focus_agent(agent_id: AgentId) -> None: ...
```

`focus_agent("abc")` fails the type check. Only `parse_agent_id` creates an `AgentId`.

## Schemas before guards

```python
from pydantic import BaseModel, ValidationError

class CreateUser(BaseModel):
    email: str
    name: str

def handle(body: bytes) -> CreateUser:
    try:
        return CreateUser.model_validate_json(body)
    except ValidationError as err:
        raise BadRequest(str(err)) from err
```

Use whichever schema library the repo already has. Add one only when it has none.

## `Protocol` for seams

```python
from typing import Protocol

class Clock(Protocol):
    def now(self) -> float: ...

def is_expired(deadline: float, clock: Clock) -> bool:
    return clock.now() > deadline
```

A test passes any object with a `now()` method. No inheritance, no mock library.

## Mutable defaults

```python
# Don't. The same list is shared by every call.
def add_tag(tag: str, tags: list[str] = []) -> list[str]:
    tags.append(tag)
    return tags

# Do.
def add_tag(tag: str, tags: tuple[str, ...] = ()) -> tuple[str, ...]:
    return (*tags, tag)
```

## Real tests

```python
import pytest

@pytest.mark.parametrize(("raw", "expected"), [("a,b", ["a", "b"]), ("", [])])
def test_split_tags(raw: str, expected: list[str]) -> None:
    assert split_tags(raw) == expected

def test_writes_report(tmp_path: Path) -> None:
    out = tmp_path / "report.json"
    write_report(out, rows=[{"id": 1}])
    assert json.loads(out.read_text()) == [{"id": 1}]
```
