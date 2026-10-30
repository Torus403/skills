---
name: ui-build
description: Build UI to an approved design with the project's tokens and components, exact sizing standards and consistency. Use when writing or changing the code of any website, dashboard, component or app screen, including building from a Figma file or a design image.
license: CC-BY-4.0 AND MIT AND Apache-2.0, see NOTICE.md
---

# UI build

Turns an approved design into code that matches it, built from what the project already has. The design comes from the **ui-design** skill or from a design file Jack gives you. Sources and licenses are in [NOTICE.md](NOTICE.md).

The approved design decides. A change it does not show is a deviation, and a deviation is Jack's call.

## 1. Hold the design

- **From the ui-design skill.** The approved direction and plan, with the research brief.
- **From Figma.** Search your tools for `figma` before saying it is unavailable. A server that lists only an authenticate tool is signed out, so ask Jack to sign in. Read every frame in scope with its exact values.
- **From an image.** Sizes are ratios to the capture, so state the scale you assumed and treat every value as an estimate. Ask for the Figma link when one exists.

Done when you hold, for every screen or frame in scope, its layout and its values for spacing, size, radius, color, type and the components used.

## 2. Map the design onto the project

Read the project's tokens, theme and component library before writing anything. Then map every value:

| In the design | In code |
| --- | --- |
| A value that equals a token | That token |
| A value with no token | The nearest token, listed in the report as rounded |
| A component | The project's component of that kind, with the variant the design shows |
| A component the project lacks | Plain markup, listed as a deviation, and ask whether a shared component should exist |
| A one-off group | Plain markup in place, not a new component |

Stop and ask Jack when rounding would visibly change the design: more than 2px on spacing or size, or a color landing on a different step.

When the project has no tokens, or they miss a role, define them once as shadcn/ui theme variables in the global CSS (`--background`, `--foreground`, `--primary`, `--muted`, `--border`, `--ring`, `--radius` and the rest), plus spacing, type and motion tokens, from [references/tokens.md](references/tokens.md). From here on every value comes from a token.

## 3. Build

Read these before the first line of code, and apply them to every line:

- [references/web-interface-guidelines.md](references/web-interface-guidelines.md). Every MUST and NEVER is a requirement.
- The sizing standards in [references/tokens.md](references/tokens.md).
- [references/dashboards.md](references/dashboards.md) for an Operate screen: dashboards, admin, settings, lists.
- The **animate** skill for anything that moves, with the rules in the **emil-design-eng** skill. The **animation-performance** skill when an animation drops frames.
- The **mobile-native** skill for anything used on a phone.
- The **seo** skill's new page checklist for any public page: server-rendered content, a unique title and description, a canonical, one H1 and real links.

Then build:

- **New or redesigned screens** go through the nine passes in [references/passes.md](references/passes.md), in order.
- **A Figma file or image** is built as drawn: the frames, the breakpoints the frames define and the states the file draws. A state the file does not draw keeps the component's default and goes in the report as missing.

Build only what the design shows. Leave everything around it as it was: no neighbouring copy edits, no icon swaps, no cleanups on the way. A diff wider than the design is the most common way this goes wrong.

Components are shadcn/ui. Use the project's shadcn components, and add a missing one with `npx shadcn@latest add <component>` instead of building it by hand or bringing in another component library. Compose and restyle them through the theme tokens and their variants. Never rebuild keyboard or focus behavior by hand. Use the **pick-ui-library** skill only for what shadcn/ui does not cover, like number animation or virtualization. Where its list names a component library, shadcn/ui wins.

Where the backend for part of the design does not exist yet, build that part fed by props and list it as unwired.

## 4. Keep it consistent

Do this while you build, not after.

- **One token set.** Every color, size, radius, shadow, duration, z-index and breakpoint comes from a token. No hex codes, raw `px` values or Tailwind arbitrary values like `w-[13px]` in the diff, except an odd value that exactly centers something.
- **One component per job.** Reuse the project's button, input, table, card, dialog and empty state. Extend an existing component before making a second one, and add a new shared pattern to the shared components, not inline in one screen.
- **Same as the siblings.** Page headers, page padding, section spacing, table rows, forms, the position of primary actions and the wording of shared labels match the sibling screens.
- **Same behavior.** Hover, focus, press, loading, empty and error states work the way they do on the sibling screens.

## 5. Hand over

Render the result once at desktop width with the **control-ui** skill to catch anything obviously broken, then run the **ui-verify** skill.

For a build from a design file, report each element against the design:

| Element | Design | Built | Status |
| --- | --- | --- | --- |
| Card padding | 20px | `p-5` | Matches |
| Title size | 15px | `text-sm`, 14px | Rounded to token |
| Badge | Filled pill | Text label | Deviates, asked: no badge component exists |

Then list, one line each, and omit an empty list: **Unwired** parts, **Missing states** the design did not draw, and **Conflicts** where the design breaks a guideline, built as designed and flagged for Jack.
