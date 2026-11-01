---
name: production-readiness
description: "Make a service ready for real users to depend on: structured logs with request ids, the four golden signals, health checks, alerts on symptoms, staged rollout and rollback, and a short runbook. Use before a first launch, when adding a new service or background worker, or when a repo's stage moves to launched."
---

# Production readiness

AWS runs an operational readiness review and Google a production readiness review before anything takes real traffic. This is the solo-sized version: the questions that decide whether you find out about a problem from a dashboard or from a user.

Use the repo's existing logger, metrics, error tracker, and hosting platform (the **principle-align-with-existing-practices** skill). Add a new tool only with Jack's approval. Walk the checklist, fix what's missing on the task's branch, and list anything only Jack can do (an account, a dashboard, a paid plan) as owner tasks, with the **wizard** skill when the steps are fiddly.

## Logs

- **Structured, one event per line**, as JSON or the logger's structured form, with a level.
- **A request id on every line.** Accept an incoming one or generate it at the edge, pass it to every downstream call and job, and return it in a response header so a user report can be traced.
- **Log the decision, not the noise.** Errors with their cause and the ids involved. One line per request at the edge. No logs inside tight loops.
- **Never log secrets or personal data** beyond an id (the **secure-by-default** skill).

## Metrics and errors

- **The four golden signals** for each service: latency (as percentiles, not an average), traffic, errors, and saturation (queue depth, connection pool, memory).
- **Unhandled errors reach an error tracker** (Sentry or the platform's own), tagged with release and request id.
- **Background jobs report** success, failure, duration, and queue age.

## Health and limits

- **A health check** that proves the service can do its job: it reaches the database, not only that the process is up. Keep it cheap and unauthenticated, and leak nothing.
- **Timeouts, retries, and bounded queues** on every outside call (the **principle-assume-the-call-fails** skill).
- **Graceful shutdown.** Stop taking work, finish what's in flight within a deadline, then exit.
- **Configuration parsed at startup.** A missing variable stops the deploy, not the first request that needs it.

## Alerts

- **Alert on what users feel**: error rate, latency, a job queue that keeps growing, a health check failing. Not on CPU or a single error.
- **Each alert names its runbook entry.** An alert you'd ignore is deleted.
- **Start with very few.** One or two that always mean "look now" beat twenty that train you to ignore them.

## Change

- **Deploys are boring and reversible.** One command or a merge deploys, and one command rolls back to the last good release.
- **Database migrations follow expand, migrate, contract** once the repo is launched (the Standing rules in `../jack-mode/SKILL.md`). Back up before a destructive one, and test the restore at least once.
- **Risky behavior ships behind a flag** the repo already has, off by default, so turning it off is a config change, not a deploy.

## Runbook

A short `docs/runbook.md`, committed, with one entry per alert and per common failure: how to tell it's happening, where to look (log query, dashboard), and the first safe action (roll back, turn off the flag, scale up, replay the queue). Add the docs path to the repo's Agent setup section (the **setup-repo** skill).

## Done

Report each checklist area as covered, fixed in this branch, or an owner task for Jack, with the evidence: the log line, the metric, the health check response, the rollback command run once.
