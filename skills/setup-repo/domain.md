# Domain Docs

How the engineering skills should consume this repo's domain documentation when exploring the codebase. Jack's docs live in `.jack/`, which git never tracks. The repo's own tracked docs, if any, belong to its team: read them too, and never write to them.

## Before exploring, read these

- **`.jack/GLOSSARY.md`**, or
- **`.jack/GLOSSARY-MAP.md`** if it exists: it points at one `GLOSSARY.md` per context under `.jack/contexts/`. Read each one relevant to the topic.
- **`.jack/adr/`**: read ADRs that touch the area you're about to work in. In multi-context repos, also check `.jack/contexts/<context>/adr/` for context-scoped decisions.
- The repo's tracked `GLOSSARY.md`, `GLOSSARY-MAP.md`, and `docs/adr/`, if they exist.

If any of these files don't exist, **proceed silently**. Don't flag their absence; don't suggest creating them upfront. The `/domain-modeling` skill (reached via `/grill-with-docs` and `/improve-codebase-architecture`) creates them lazily when terms or decisions actually get resolved.

## File structure

Single-context repo (most repos):

```
.jack/
├── GLOSSARY.md
└── adr/
    ├── 0001-event-sourced-orders.md
    └── 0002-postgres-for-write-model.md
```

Multi-context repo (presence of `.jack/GLOSSARY-MAP.md`):

```
.jack/
├── GLOSSARY-MAP.md
├── adr/                               ← system-wide decisions
└── contexts/
    ├── ordering/
    │   ├── GLOSSARY.md
    │   └── adr/                       ← context-specific decisions
    └── billing/
        ├── GLOSSARY.md
        └── adr/
```

## Use the glossary's vocabulary

When your output names a domain concept (in an issue title, a refactor proposal, a hypothesis, a test name), use the term as the glossary defines it. Don't drift to synonyms the glossary explicitly avoids.

If the concept you need isn't in the glossary yet, that's a signal: either you're inventing language the project doesn't use (reconsider) or there's a real gap (note it for `/domain-modeling`).

## Flag ADR conflicts

If your output contradicts an existing ADR, surface it explicitly rather than silently overriding:

> _Contradicts ADR-0007 (event-sourced orders), but worth reopening because…_
