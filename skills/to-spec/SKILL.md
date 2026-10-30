---
name: to-spec
description: "Turn the current conversation into a spec file in .jack/specs/, kept out of git: no interview, just synthesis of what you've already discussed. For new features, core logic, and architecture only."
disable-model-invocation: true
---

Adapted from Matt Pocock's `to-spec`. This skill takes the current conversation and your understanding of the codebase and writes a spec into the Jack folder, which git never tracks. Do NOT interview the user. Synthesize what you already know. The grilling already happened.

Specs are for big things only: a new feature, core logic, or an architecture change. If the work is small, say so and stop. The agreed plan in the conversation is enough.

## Process

1. Explore the repo to understand the current state of the codebase, if you haven't already. Use the project's glossary vocabulary throughout the spec, and respect any ADRs in the area you're touching. Read `.jack/domain.md` if it exists.

2. Sketch the seams at which you're going to test the feature. Prefer existing seams to new ones. Use the highest seam possible. If new seams are needed, propose them at the highest point you can. The fewer seams across the codebase, the better. The ideal number is one.

Check with the user that these seams match their expectations.

3. Write the spec with the template below to `.jack/specs/<feature>.md`, with `<feature>` in kebab case. That is the Jack folder, `.jack/`, which stays out of git (set it up per the Files you write in a repo section of `../jack-mode/references/harness.md`). Never commit the spec, never put it in the repo's own docs folder, and never link it from a PR. Tell Jack its path.

<spec-template>

# <Feature name>

## Problem Statement

The problem that the user is facing, from the user's perspective.

## Solution

The solution to the problem, from the user's perspective.

## User Stories

A numbered list of user stories that covers every aspect of the feature. Each one in the format:

1. As an <actor>, I want a <feature>, so that <benefit>

<user-story-example>
1. As a mobile bank customer, I want to see balance on my accounts, so that I can make better informed decisions about my spending
</user-story-example>

## Implementation Decisions

A list of implementation decisions that were made. This can include:

- The modules that will be built or modified
- The interfaces of those modules that will be modified
- Technical clarifications from the developer
- Architectural decisions (record lasting ones as an ADR too, via the **domain-modeling** skill)
- Schema changes
- API contracts
- Specific interactions

Do NOT include specific file paths or code snippets. They go stale quickly.

Exception: if a prototype produced a snippet that encodes a decision more precisely than prose can (state machine, reducer, schema, type shape), inline it within the relevant decision and note briefly that it came from a prototype. Trim it to the decision-rich parts.

## Testing Decisions

- What makes a good test here (only test external behavior, not implementation details)
- Which modules will be tested, at which seams
- Prior art for the tests (similar tests in the codebase)

## Out of Scope

What this spec deliberately leaves out.

## Further Notes

Any further notes about the feature.

</spec-template>
