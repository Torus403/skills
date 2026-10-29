### Feature

**You own the design. Align, grill, build, verify.** Delegate implementation where it helps. Stay in the lead.

1. Align with the codebase (the **principle-align-with-existing-practices** skill). Run `how` over the affected subsystem and find the closest existing feature to copy the shape of.
2. Grill Jack with the **grilling** skill until the design tree is empty: behavior, edge cases, data shape, UX, scope, what is out. Settle factual forks with the Prototype playbook instead of asking. For a new feature, core logic, or an architecture change, write the spec with **to-spec** (`docs/specs/<feature>.md`), and record architecture decisions and new terms with **domain-modeling**.
3. Shape it. Name the data shape and its organizing structure per **principle-model-the-domain**. If the design crosses a function boundary, run `architect`. Pick the design with the fewest moving parts (**principle-fewest-moving-parts**). Show Jack the shape as the last grilling round, and wait for Jack to confirm the shared understanding before building.
4. Write the throughput checkpoint as four todo items. A dimension that genuinely does not apply keeps its item with `n/a: <reason>`:
   - **Blocking first steps.** Gates run before fan-out.
   - **Independent workstreams.** Disjoint files, services, or layers parallelize. Shared writes serialize.
   - **Shared mutable state.** Default to splitting the target (the **separate-before-serializing-shared-state** principle skill). Serialize only for real invariants.
   - **Smallest safe decomposition.** If one worker is best, name why.
5. Create the branch `feat/<short-desc>` and build. Delegate code-writing to a `jack-agent` with a specific scope (file paths, the named data shape, the existing example to match, and success criteria). When the implementation admits several valid shapes, delegate through the **arena** skill instead. Comments per **Comments**. Run `deslop` before each commit. Commit as you go with Conventional Commits.
6. For an epic, build it in phases on the same branch. Each phase ends in a verifiable state with its own commits (the **sequence-verifiable-units** principle skill). Do not split it into stacked PRs.
7. Verify on the matching surface with `control-ui` or `control-cli`, against the spec when one exists. "Inconclusive" or wrong-surface is not a pass. Flag it.
8. Run **Opening a PR**.

**Reply:** what you built, what you chose and why, the throughput checkpoint, how you verified it, and anything left open. Tables for design alternatives.
