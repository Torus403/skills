---
name: principle-type-system-discipline
description: "Apply when designing types, reviewing a function signature, or writing code in any statically-typed language. Make illegal states hard to represent with plain types, parse external data at boundaries, handle every variant, derive from authoritative schemas."
disable-model-invocation: true
---

# Type System Discipline

Let the types reject impossible states and unhandled variants, using plain, widely known type features. Jack prefers simple over clever: never reach for type gymnastics or newer features when a plain type does the job. Prefer defining errors and special cases out of existence over proliferating handlers. For syntax, see the **typescript-best-practices** and **python-best-practices** skills.

- **One state at a time.** Model "one of these states" as a plain union of small records, each carrying only its own data, instead of one record with optional fields that allow impossible combinations.
- **Handle every variant.** Branch over every known case and end with an error for the case nobody handled.
- **Name what a primitive means.** When two arguments share a primitive type but mean different things, give them long, distinct names (`customerId`, `invoiceId`) and pass them in one object. Don't build branded types for it.
- **External data is untyped until parsed.** RPC payloads, JSON, IPC messages, CLI args, config files, environment variables, database rows. Have a parse function at every boundary that turns unstructured input into the typed model. The **boundary-discipline** principle skill says where to put validation.
- **Derive types from authoritative schemas.** When a protocol buffer, OpenAPI spec, GraphQL schema, database migration, design-token file, or another file owns a shape, derive from it instead of hand-rolling a parallel type. See the **encode-lessons-in-structure** principle skill.
