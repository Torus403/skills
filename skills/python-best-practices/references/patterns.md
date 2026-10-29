# Python patterns

Examples for the rules in `../SKILL.md`. Style examples (inlining, names, layout, comments, plain branching, plain loops) live in the **code-style** skill. Python 3.10 or later.

## Dataclasses for records

```python
from dataclasses import dataclass


@dataclass(frozen=True)
class Invoice:
    invoice_id: str
    customer_id: str
    total_in_cents: int
    paid: bool
```

## Parse at the boundary

```python
from pydantic import BaseModel, ValidationError


class CreateUserRequest(BaseModel):
    email: str
    display_name: str


def parse_create_user_request(body: bytes) -> CreateUserRequest:
    try:
        return CreateUserRequest.model_validate_json(body)
    except ValidationError as error:
        raise BadRequestError(str(error)) from error
```

Use the schema library the repo already has. Without one, parse into a dataclass by hand at the boundary and raise on anything missing.

## One state at a time

```python
# Avoid. Optional fields allow states that can't happen, such as uploading with an error.
@dataclass
class UploadStatus:
    uploading: bool
    file_url: str | None = None
    error_message: str | None = None
```

```python
# Write. One small dataclass per state, and plain `isinstance` checks.
@dataclass(frozen=True)
class Uploading:
    pass


@dataclass(frozen=True)
class Uploaded:
    file_url: str


@dataclass(frozen=True)
class UploadFailed:
    error_message: str


def describe_upload(upload_status: Uploading | Uploaded | UploadFailed) -> str:
    if isinstance(upload_status, Uploading):
        return "Uploading"

    if isinstance(upload_status, Uploaded):
        return f"Uploaded to {upload_status.file_url}"

    if isinstance(upload_status, UploadFailed):
        return f"Upload failed: {upload_status.error_message}"

    raise ValueError(f"Unknown upload status: {upload_status!r}")
```

## No mutable defaults

```python
# Avoid. Every call shares the same list.
def add_tag(tag: str, tags: list[str] = []) -> list[str]:
    tags.append(tag)
    return tags
```

```python
# Write.
def add_tag(tag: str, tags: list[str] | None = None) -> list[str]:
    if tags is None:
        tags = []

    return [*tags, tag]
```

## Real tests

```python
import json
from pathlib import Path

import pytest


@pytest.mark.parametrize(("raw_tags", "expected_tags"), [("a,b", ["a", "b"]), ("", [])])
def test_split_tags(raw_tags: str, expected_tags: list[str]) -> None:
    assert split_tags(raw_tags) == expected_tags


def test_write_report_saves_rows_as_json(tmp_path: Path) -> None:
    report_path = tmp_path / "report.json"

    write_report(report_path, rows=[{"invoice_id": "inv_1"}])

    assert json.loads(report_path.read_text()) == [{"invoice_id": "inv_1"}]
```
