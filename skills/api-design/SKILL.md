---
name: api-design
description: Design an HTTP, RPC, or webhook API that callers can rely on for years, following Stripe's conventions. Use when adding or changing an endpoint, a request or response shape, an error format, pagination, a webhook, or an API version.
---

# API design

An API is a promise. Once someone calls it, every field, status, and error code is part of the contract (Hyrum's law). Stripe's API is the model here because its shapes have stayed consistent for over a decade.

Match the repo's existing API conventions first (the **principle-align-with-existing-practices** skill). Where the repo has none, use these. Every new or changed shape is a judgement call for Jack in grilling (the **grilling** skill).

## Resources and names

- **Nouns for resources, plural paths.** `GET /invoices`, `POST /invoices`, `GET /invoices/:id`. A verb only for an action that isn't create, read, update, or delete: `POST /invoices/:id/finalize`.
- **One name per concept**, the glossary's term, in requests, responses, and docs alike.
- **Field names in `snake_case`** (or the repo's choice, applied everywhere).
- **Ids are opaque strings with a type prefix.** `inv_8fK2...`, `cus_...`. A prefixed id is self-describing in logs and can't be passed as the wrong kind by mistake. Never expose sequential database ids.
- **Every object says what it is.** An `object` (or `type`) field: `"object": "invoice"`.

## Values

- **Timestamps** in UTC: ISO 8601 strings or integer Unix seconds, one choice for the whole API.
- **Money** as an integer in minor units plus a currency: `"amount": 1999, "currency": "usd"`.
- **Enums** as lowercase strings, and callers must tolerate new values.
- **No `null` and missing-field ambiguity.** Pick one meaning for each, and document it.

## Requests

- **Validate at the boundary** and reject unknown fields on writes (the **principle-boundary-discipline** skill).
- **Mutating requests accept an `Idempotency-Key` header.** Store the key with the first result and return that result for any repeat (the **principle-assume-the-call-fails** skill).
- **Partial updates** with `PATCH`, or `POST` to the resource, sending only changed fields.

## Responses and errors

- **List endpoints use cursor pagination.** `?limit=` with a documented maximum, and `starting_after` or a `next_cursor` in the response with `has_more`. Never offset pagination on data that changes.
- **One error shape everywhere:**

  ```json
  {
    "error": {
      "type": "invalid_request_error",
      "code": "amount_too_small",
      "param": "amount",
      "message": "Amount must be at least 50 cents."
    }
  }
  ```

  `type` is a broad class the caller branches on, `code` a stable machine string, `param` the offending field, `message` a sentence safe to show a person. Never a stack trace.
- **Status codes mean what HTTP says.** `400` invalid input, `401` not signed in, `403` not allowed, `404` not found (also for another tenant's object, so its existence doesn't leak), `409` conflict, `422` only if the repo already uses it, `429` rate limited, `5xx` our fault.

## Webhooks

- **Sign every delivery** (an HMAC of the timestamp and body with a per-endpoint secret) and document how to verify it.
- **Retry with backoff** for days, and expect receivers to see duplicates. Send an event id and type: `{ "id": "evt_...", "type": "invoice.paid", "created": ..., "data": { ... } }`.
- **Thin events are safer.** Send the id and let the receiver fetch the current object, so out-of-order deliveries can't apply stale data.

## Change and versioning

- **Additive changes only** on a published API: new optional fields, new endpoints, new enum values. Removing or renaming a field, tightening validation, or changing a meaning is a breaking change.
- **Pre-launch**, break freely and migrate every caller in the same PR (the Standing rules in `../jack-mode/SKILL.md`).
- **Launched**, a breaking change needs a new version. Use one dated version per account or request header (`Api-Version: 2026-11-01`), with the old behavior kept working behind it. Never break a caller silently.

## Before you call it done

The PR's `## Blast Radius` names every new or changed field, status, error code, and event, and says whether each is additive or breaking.
