---
name: principle-assume-the-call-fails
description: "Apply when code calls anything over a network or another process: an HTTP API, a database, a queue, a cache, a webhook. Give every call a timeout, retry only idempotent work with capped backoff and jitter, and bound every queue and fan-out."
disable-model-invocation: true
---

# Assume the Call Fails

Every call that leaves the process will, some day, hang, fail, time out after it succeeded, or arrive twice. Write the code for that day. This is the core of the Amazon Builders' Library and of Stripe's API.

**Why:** A call with no timeout holds a thread or a request forever. A retry with no cap or jitter turns a small outage into a stampede. A retried write without an idempotency key charges the customer twice.

**The rules:**

- **Every call has a timeout.** Set it from what the caller can afford to wait, not the library default, which is often infinite. Name it with its unit.
- **Retry only what is safe to repeat.** Reads, and writes that carry an idempotency key. Retry on timeouts, network errors, `429`, and `5xx`. Never on other `4xx`.
- **Cap retries and back off with jitter.** A few attempts at most, an exponential delay with random jitter, and a total time budget. Retry at one layer only, or the attempts multiply.
- **Idempotency keys on mutating requests.** An API that creates or charges accepts an `Idempotency-Key` header and returns the first result for a repeat. When you call such an API, send one, generated once per logical operation and reused across retries.
- **Webhooks and queue messages arrive more than once and out of order.** Record each event id you handled and skip a repeat. Check the current state before you act, per the **principle-make-operations-idempotent** skill.
- **No fallback path that only runs during an outage.** Code that runs rarely is broken when it is finally needed. Fail clearly, or make the fallback the normal path.
- **Bound queues and fan-out.** A queue has a maximum length and a plan for when it is full. Concurrent calls have a limit. Never start one request per item of an unbounded list.
- **Write the outcome where you can find it.** A call that timed out may have succeeded. Look the result up by its idempotency key or id before you assume it failed.

**The tests:**

1. What happens when this call hangs for a minute?
2. What happens when it succeeds but the response is lost, and we retry?
3. What happens when a thousand callers retry at once?
