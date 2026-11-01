---
name: secure-by-default
description: Build security in while writing code, not only at review. Use whenever code touches auth, sessions, permissions, money, user data, file uploads, outbound requests, secrets, raw SQL, or shell commands.
---

# Secure by default

Stripe and the OWASP Application Security Verification Standard treat security as a property of how code is written, not a pass at the end. The **thermos** review still runs before the PR. This skill is what you do while building so it finds nothing.

Follow the repo's existing auth, permission, and secrets code first (the **principle-align-with-existing-practices** skill). These rules fill the gaps.

## Threat model in two questions

For any feature in the trigger list, answer these in the grilling round, with your recommendation:

1. **Who can call this, and what may each caller see or change?** Name every role, including anonymous and another tenant's user.
2. **What is the worst a hostile caller could do with it?** Read another user's data, spend someone's money, run code, flood it, or leak a secret.

Each answer becomes a check in the code. If an answer is "nothing stops them", that is a design gap, not a follow-up.

## Access

- **Deny by default.** Every route, action, and job needs an explicit auth check. A new endpoint with no check is a bug, even if the UI hides it.
- **Check ownership on every read and write.** Scope each query by the caller's user or tenant id (`where id = $1 and account_id = $2`), never by the id from the request alone. A missing scope is the most common breach in web apps (insecure direct object reference).
- **Authorize on the server.** Hidden buttons and client checks are UX, not security.
- **Least privilege.** Each service, key, token, and database role gets only what it needs. Use restricted API keys where the provider offers them.

## Input and output

- **Parse at the boundary.** The **principle-boundary-discipline** skill. Reject what you don't expect: lengths, sizes, enums, and formats all have limits.
- **No string-built queries, commands, or paths.** Use parameterised queries or the ORM. Pass arguments to subprocesses as an array, never through a shell. Resolve a user-supplied path and confirm it stays inside the allowed folder.
- **Encode output for where it goes.** Let the framework escape HTML. Never put user input in `dangerouslySetInnerHTML`, `eval`, a template string that becomes code, or a redirect URL without an allowlist.
- **Uploads.** Check size and type on the server, store outside the web root or in object storage under a generated name, and never trust the client's filename or content type.
- **Outbound requests to a user-supplied URL.** Allowlist hosts, block private and metadata addresses (`127.0.0.0/8`, `10.0.0.0/8`, `169.254.169.254`, and the like), and set a timeout (server-side request forgery).

## Secrets

- **Only from the environment or a secret store.** Never in code, tests, fixtures, logs, error messages, URLs, or the client bundle. A secret in git history is leaked: rotate it.
- **Parse them at startup.** Fail fast when one is missing, per the **principle-boundary-discipline** skill.
- **Compare secrets and tokens in constant time** (`crypto.timingSafeEqual`, `hmac.compare_digest`).

## Sessions, passwords, and tokens

- **Use the framework's or provider's auth.** Never roll your own password hashing, session format, or crypto. When you must hash a password, use argon2id or bcrypt.
- **Cookies** are `HttpOnly`, `Secure`, and `SameSite=Lax` or stricter. State-changing requests are protected against cross-site request forgery by the framework's mechanism.
- **Verify webhook signatures** before you read the body, and reject old timestamps to stop replays.
- **Rate limit** login, signup, password reset, and anything that sends email or costs money.

## Data and logs

- **Collect and keep only what the feature needs.**
- **Never log** secrets, tokens, passwords, full card numbers, or personal data beyond an id. Log the id and look the rest up.
- **Errors shown to users** carry a code and a safe message, never a stack trace or a query (the **code-style** skill).

## Dependencies

- **Add one only when it earns its place.** "A little copying is better than a little dependency." Prefer the platform and libraries the repo already has.
- **Commit the lockfile** and run the repo's audit (`npm audit`, `pnpm audit`, `pip-audit`) in its check command (the **setup-repo** skill).

## Before you call it done

For each trigger the diff touches, name the check that covers it in the PR's `## Blast Radius`: the auth check, the ownership scope, the signature check, the rate limit. A trigger with no check is a finding to fix, not to list.
