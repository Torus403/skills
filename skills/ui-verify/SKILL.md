---
name: ui-verify
description: Verify a website, dashboard or app screen on the rendered page, against the approved design, worst-case data, accessibility, the interface guidelines and the sibling screens. Use after building or changing any UI, before calling it done, and when asked to review UI or a UI diff.
license: MIT AND CC-BY-4.0, see NOTICE.md
---

# UI verify

Checks the UI the way users meet it: rendered, at every width, with real and worst-case data, by mouse and keyboard. A claim you did not look at is not verified. Sources and licenses are in [NOTICE.md](NOTICE.md).

Verification reads and reports. It edits nothing, except the dev-only worst-case fixtures, unless you are fixing your own build or Jack asks for fixes.

## 1. Resolve the scope

- **Your own build.** The screens and components the **ui-build** skill just produced, with the approved plan or design to compare against.
- **A change to review**, like a branch, a pull request or uncommitted work. Review the surfaces the changed files render in, not only the files: expand one hop to their direct consumers, and a second hop for tokens, theme values and shared components. Give every finding a status: `Introduced` (the change created it), `Regression` (the change weakened something that worked, so read the removed lines too) or `Pre-existing`. Report at most three `Pre-existing` findings.
- **A screen or flow** with no change. Cover all of it, including its empty, loading, error and narrow states.

State the scope you resolved in the report.

## 2. Look at it

Render with the **control-ui** skill:

- At 320, 375, 768, 1280 and 1440 wide, and at 2560 for anything with a max width. At 200% browser zoom.
- In every theme the product has, and in RTL when it supports it.
- Every state: hover, focus, pressed, disabled, loading, empty, error, and the first-time user.
- By keyboard alone: tab through every control, open and close every menu and dialog, and check focus moves, traps and returns.
- With `prefers-reduced-motion: reduce` emulated.

Compare each render with the approved plan or the design file, element by element. "Gap is 12px, design is 16px" is a finding. "Feels a bit tight" is not.

## 3. Break it

Follow [references/break.md](references/break.md). Done when every rendered value has been tried with worst-case, empty, one and huge data.

## 4. Check the rules

Walk the code and the renders against each source, and cite `path/to/file:line` for every finding:

- Every rule in [`../ui-build/references/web-interface-guidelines.md`](../ui-build/references/web-interface-guidelines.md).
- The sizing standards in [`../ui-build/references/tokens.md`](../ui-build/references/tokens.md). Measure contrast, target sizes and line lengths on the render.
- The signs and the Defaults in [`../ui-design/references/signs.md`](../ui-design/references/signs.md).
- The tells in [`../ui-build/references/dashboards.md`](../ui-build/references/dashboards.md) for an Operate screen.

## 5. Check consistency

- **Tokens.** Search the diff for hex codes, raw `px` values, Tailwind arbitrary values like `w-[13px]`, arbitrary `z-*`, and durations or easings outside the tokens. Each is a finding unless it exactly centers something.
- **Components.** Find any hand-built control that duplicates one the project has, and any new component that should extend an existing one.
- **Siblings.** Open two sibling screens beside the new one at the same width. Page header, padding, section spacing, table rows, form layout, the place of the primary action and the wording of shared labels match, or the difference is deliberate and named.
- **Behavior.** The same states behave the same way as on the siblings.

## 6. Report

Rank by user impact:

- `HIGH` blocks a task, misleads, hides content or controls, or risks data loss.
- `MEDIUM` harms comprehension, efficiency or consistency.
- `LOW` is isolated polish.

These are `HIGH` on sight, however minor the surface:

- An interactive control with no accessible name, or no visible focus.
- Something reachable by pointer but not by keyboard.
- Motion that ignores `prefers-reduced-motion`, or a state change carried by motion alone.
- Content or a control clipped, overlapped or unreachable at 320px or 200% zoom.
- Text that fails its contrast ratio.
- Meaning carried by color alone.
- A destructive action with no confirmation or undo.
- Truncated content with no way to read the full value.
- An error that names no way to recover.

One root cause is one finding, with every location in the same row. For each fix, prefer the cheapest that works: delete, use the platform, reuse what the project has, correct the value, and only then add something new.

| Severity | Location | Before | After | Why |
| --- | --- | --- | --- | --- |
| HIGH | `src/Dialog.tsx:42` | Icon-only close button with no name | `aria-label="Close"` | Screen readers announce an unnamed button |

Add a `Status` column for a change review. Mark every check you could not run as `Not verified`, never as passed. End with **Block** while any `HIGH` remains, or **Approve**. Never approve what you did not inspect.

## Checklist

- [ ] Rendered at every width, theme, zoom and state above, and every comparison has a screenshot behind it
- [ ] Worst-case, empty, one and huge data tried on every rendered value
- [ ] Every control works by keyboard with visible focus, and every icon-only control has a name
- [ ] Touch targets, control heights, text sizes, line length and contrast meet the sizing standards
- [ ] No signs or Defaults left from the signs list, unless the direction asks for one by name
- [ ] Every value comes from a token, and no raw values in the diff
- [ ] Solid surfaces, one accent, line icons from one set, no emoji in the interface
- [ ] Numbers in one format with tabular figures, right-aligned in tables
- [ ] Hover, focus, pressed, disabled, loading, empty and error states exist
- [ ] No decorative motion, and reduced motion respected
- [ ] Matches the sibling screens, or each difference is named
- [ ] Template check: swap the product name for another product's. If the screen still fits, the direction needs pushing in the copy, the visual or the signature detail
