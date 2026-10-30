---
name: typescript-best-practices
description: TypeScript best practices. Use when reading or editing any .ts or .tsx file.
paths: ["**/*.ts", "**/*.tsx"]
---

# TypeScript best practices

Read the **code-style** skill first. These rules add the TypeScript type rules on top of it. They favor plain, widely known TypeScript over clever type machinery, even when that means a little more code. Follow the repo's own `tsconfig`, linter, and formatter before anything here.

| Rule | Summary |
|------|---------|
| Strict mode | Work with `strict` on. Fix the error, don't silence it. |
| `unknown` over `any` | External data is `unknown` until parsed. `any` turns the compiler off. |
| Parse at the boundary | Where data crosses in (HTTP, `JSON.parse`, env, files, IPC), parse it once into a named type with the repo's schema library (such as `zod`), and trust the type inside. See the **boundary-discipline** principle skill. |
| No `as` casts | An `as` is a claim the compiler can't check. Use one only right after validation. Never `as any`, and no `!` to dodge a possibly-undefined value. Handle the `undefined`. |
| Plain discriminated unions | Model "one of these states" as a union of object types with a `kind` string field, then `switch` on `kind`. No bags of optional fields where only some combinations are valid. |
| Exhaustive `switch` | End a `switch` over a union with a `default` that throws, so a new variant can't slip through silently. |
| Spell types out | Write the object type you mean. Avoid conditional types, mapped types with key remapping, template literal types, and deep generics in application code. A plain type that repeats a few fields beats one a reader has to evaluate. |
| Types over interfaces only when the repo does | Match the repo's choice between `type` and `interface`. Default to `type`. |
| Object parameters past three | Past three parameters, pass one object so call sites read clearly. |
| `null` and `undefined` | Pick the one the repo uses for "no value" and use it consistently. Check it with `=== null` or `=== undefined`, not truthiness, when `0` or `""` are valid. |
| `async` and `await` | Use `async`/`await`, not `.then()` chains. Always `await` or return a promise. Never leave one floating. |
| Real tests | Don't mock what you can run. Use the repo's test runner and real modules. Mock only what you can't run locally. |
| Structured logging | Use the repo's logger with enough context to debug from an id. No `console.log` in shipped code. |

Examples: `references/patterns.md`.
