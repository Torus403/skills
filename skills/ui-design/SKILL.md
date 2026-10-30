---
name: ui-design
description: Design websites, landing pages, dashboards and app screens that look made for the product, not AI-generated. Use whenever you build, redesign or polish any UI a user sees, or a screen shows AI tells like purple gradients, glows, gradient text, emoji labels or uneven spacing.
license: CC-BY-4.0 AND Apache-2.0, see NOTICE.md
---

# UI design

The front door for every piece of UI work. It owns the direction and the proposal to Jack, and routes research, building and verification to their own skills. Sources and licenses are in [NOTICE.md](NOTICE.md).

Vibecoded UI fails in the same predictable ways. Every surface glows, every label has an emoji, spacing is whatever the model typed that day, and the copy shouts. Good UI makes every size, color, word and image deliberate, and keeps the product's features, content and order of sections.

A screen that is clean but could belong to any product is the next template. Every run ends with a screen that only this product could have.

The difference between slop and craft is where the richness goes. Slop spreads color and effects over the chrome, the backgrounds, buttons, borders and labels. Craft keeps the chrome quiet and puts the richness into one or two moments of content that people remember, like a rendered object, a beautiful chart or an image from the product's world.

## What good looks like

- **One bright element.** Each screen has one polished thing that carries the color and the craft, a rendered object, a painted scene or a rich chart. Everything around it is quiet, so it reads instantly.
- **Quiet chrome.** Navigation, buttons and text use the tinted neutrals and one accent. Nothing glows, nothing competes with the bright element.
- **A clear idea.** You can say in one sentence what the visual shows and why it belongs to this product.
- **Real product, real material.** Previews look like the real app with plausible data, and objects look like real things with weight, light and shadow.
- **Consistent.** The same thing looks and behaves the same everywhere, built from one set of tokens and one set of components.
- **Solid underneath.** Every screen meets the sizing standards, works by keyboard, holds up with worst-case data and reads at every width.

## Mode

Name the mode of the surface first, from what the visitor's success looks like on it.

- **Operate.** The visitor completes a task: an app screen, a dashboard, settings, an editor, admin. Scanability, consistency and the patterns users already know outrank expression. The brand lives in precise details, and the screen answers one question first.
- **Persuade.** The visitor decides and acts: a landing page, marketing, pricing. The design is the product. Earn attention with one strong idea from the product's world.
- **Read.** The visitor understands something: docs, articles, a changelog. Structure for comprehension, then make the reading worth staying for.

Choose the mode from the surface, not the product. A dashboard tool's landing page is Persuade.

## Run it

1. **Read the context.** Find the files that render the screen, the project's tokens or theme, its components, and two or three sibling screens. If a screen exists, render it and take a screenshot with the **control-ui** skill, so you judge what people see and not only the code.
   - Only a link to a live site, no code? Save the page with `node <skill folder>/scripts/snapshot.mjs <url> <Jack folder>/ui-design/original.html` and work on a copy. The Jack folder is set up per the Files you write in a repo section of [`../jack-mode/references/harness.md`](../jack-mode/references/harness.md). Add `--dark` or `--light` to match the theme the user sees. It also saves `original.live.png`, a screenshot of the live page, so render the saved copy and compare the two before you start.
   - Only a screenshot? Rebuild the screen as one static HTML file first, matching it closely, and treat that as the original.
   - A Figma file or design image to build as drawn? Skip to step 7. The design is the approved direction.
2. **Research.** Run the **ui-research** skill for every new screen, flow or section, and for every redesign. Done when its research brief is written.
3. **Audit an existing screen.** Go through [references/signs.md](references/signs.md) and list every sign you find, one line each with where it lives. A new screen has no audit.
4. **Decide how much to change.** Read the audit honestly before planning anything.
   - **Heavy slop**, many signs across color, type, icons and copy. Run the full process.
   - **Light slop**, a screen that is mostly designed with a few signs left. Polish mode. Fix only what the audit found, keep the palette, type, layout and visual, and skip research. Bigger ideas go into the report as suggestions, not changes.
   - **No slop.** Say so plainly and suggest two or three small refinements at most, with exact values. Apply them only if Jack agrees, and stop there.
5. **Plan.** Write the [Direction](#direction), then a compact plan:
   - **Color.** The base palette as 4 to 6 named hex values, from the ramps in [`../ui-build/references/tokens.md`](../ui-build/references/tokens.md) or the brand.
   - **Type.** The families and their roles.
   - **Layout.** One sentence per section or block saying what it shows and why, in reading order, with an ASCII wireframe of the first screen. For an Operate screen, open with the screen's one question and its one finding, per [`../ui-build/references/dashboards.md`](../ui-build/references/dashboards.md).
   - **Moments and signature.** Where the richness goes.
   Then review the plan against the Defaults section of [references/signs.md](references/signs.md). If a part would come out the same for any similar product, revise it and say what changed and why.
6. **Propose and wait.** Anything a user sees is Jack's call. Show Jack the research brief, the audit, the direction and the plan. Ask through the question tool per [`../jack-mode/references/harness.md`](../jack-mode/references/harness.md), one recommendation per question. When the layout itself is an open choice, sketch two or three variants with the **prototype** skill and show the screenshots. Build nothing until Jack approves. Jack telling you to just do it counts as approval.
7. **Build.** Run the **ui-build** skill with the approved plan.
8. **Verify.** Run the **ui-verify** skill on the result. Fix what it finds and run it again until its verdict is Approve.
9. **Report** the direction, what changed per pass, the Mobbin links that shaped it, the verification evidence, and any image prompt you wrote.

## Direction

Write five short lines. Derive them from what the product does, who it is for and what the research showed. Never from what is trending.

- **Product.** What it does and for whom, in one plain sentence.
- **Character.** Two or three concrete words, like `calm, exact, a little warm` or `fast, technical, playful`. Words like clean, modern, sleek, minimal and premium are not allowed, because they describe every template.
- **World.** The place or material the product naturally belongs to. A note app lives near paper and ink, a monitoring tool near instruments and night shifts, a travel app near maps and window light. This world sets the tint of the neutrals, the accent and the visual.
- **Moments.** One or two places where the screen gets rich color, material and detail, chosen from what the product shows. A rendered card or device inside the preview, a chart whose colors each mean a series, an object from the world placed next to the content.
- **Signature.** One small detail only this product would have, used consistently. A live status dot for a monitoring tool, keycaps for a developer tool, a route line for a delivery app. One detail, not five.

The examples only show the shape of an answer. Derive yours from the product in front of you.

If the product already has a real brand, like a logo file, a color or a typeface that is not slop, keep it and build the direction around it. A violet to blue gradient, sparkles and glow are slop even when they sit in the logo, unless Jack says they are the brand. A new screen in an existing product takes the product's direction as it is.

## Hard guardrails

- Keep the product's name and a real logo. When the logo itself is slop, like an emoji or a sparkle in a gradient tile, redraw it flat: the wordmark alone, or a simple glyph in one solid color.
- Keep what the product is: its features, content and the order of sections, unless Jack asks for more. Placeholder content that means nothing may be replaced with content that does.
- Leave the space that removed decoration frees up quiet, instead of filling it with a new trend like glass, grain, noise, neon or bento grids.
- Use only real features, claims and data. Ask Jack about any claim you cannot check.
- Let the direction decide the palette tint, type and visual for each product, not habit.

Which visual styles tend to work is in [references/visuals.md](references/visuals.md), finished examples are in [references/refs.md](references/refs.md), and code treatments like drawing an image in glyphs are in [references/effects.md](references/effects.md).
