---
name: principle-fewest-moving-parts
description: "Apply when choosing a design or an implementation. Pick the least fancy, simplest, most robust option with the least logic that still scales."
disable-model-invocation: true
---

# Fewest Moving Parts

The best design is the plainest one that fully works. Every extra part is a place for a bug, a crash, or behavior nobody intended.

- **Least fancy wins.** Prefer boring, obvious code over clever code. A reader should see what it does at a glance.
- **Count the moving parts.** Services, queues, caches, state, flags, layers, and branches all count. Between two designs that meet the need, ship the one with fewer.
- **Least logic, no gaps.** Write the smallest amount of logic that covers every real case. Simple never means skipping an edge case, an error path, or a race.
- **Robust by construction.** Prefer designs where the bad state can't happen (types, constraints, idempotent steps) over code that checks for it.
- **Scales without rewrites.** Simple is not short-sighted. Choose the plain design that still holds at the next order of magnitude, and stop there.
- **Elegance is the result, not the goal.** If a design needs explaining, look for a simpler one first.
