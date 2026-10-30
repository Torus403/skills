# The nine passes

Finish a pass across the whole screen before starting the next. When nearly every line changes, plan the passes in order and then write the screen in one go, as long as every pass is applied. Spacing comes first because everything else reads differently once the rhythm is right. Copy comes before type and layout because the length of the headline decides its size and where it sits. Visuals and motion come last because they should fit a screen that already works without them.

Exact values for every pass are in [tokens.md](tokens.md).

## 1. Spacing

- Everything sits on a 4px grid. Margins, paddings, gaps and fixed heights are multiples of 4, so 28 or 104 are fine even though they are not in the token list. A 2px step is fine for nudges inside small controls, and an odd value that exactly centers something stays.
- Same thing, same size. All rows in a list share one height and one gap, all cards in a row share one padding.
- Space shows grouping. Space inside a group is smaller than space between groups, and a heading sits closer to what it labels than to the section above it.
- Things line up. Icons sit in one column, labels start on one line, numbers align right in one column. Nothing is nudged off the line with a stray translate or odd margin.
- Padding follows density. Compact panels and sidebars around 16, cards 20 to 24, page edges 24 to 32.
- Navigation is the densest part of an app. Rows are 32 to 36 tall with 2 to 4 between them, icons in one column, labels on one line. A section label sits 24 below the section above and 8 above its own items. Measure the sidebar after the pass, it is where spacing breaks most often.
- Controls meet the sizing standards: touch targets, control heights and one height for controls in a row.
- Replace one-off values that break the rhythm, like `mt-[13px]` or `py-[11px]`, with steps from the scale.

## 2. Color

- Build from one neutral ramp, tinted toward the world from the direction. Background, raised surfaces, borders and text all come from that ramp.
- In apps and dashboards the backgrounds, surfaces, borders and text stay neutral, the graphite ramp or something just as grey. People look at them for hours and the content has to carry the color. The world shows in the accent, the charts and the moments, not in the surfaces. Landing pages can tint their surfaces further toward the world.
- Three text roles, primary, secondary and muted.
- In the chrome, one accent, used rarely. It marks the primary action, the selection or the one number that matters.
- The moments from the direction are the exception. Inside them color can be rich, as long as it stays inside the world and each color means something.
- A real brand color becomes the accent and leaves the surfaces. Without one, take the accent from the world.
- Text on the accent, and the accent used as text, reach 4.5 to 1 contrast. Darken it or put dark text on it when they do not.
- On dark themes the primary button can be an off white from the ramp with dark text, and the accent can live in a smaller place like the selection or a key figure.
- Semantic colors only carry meaning, like green for a good change and red for an error, toned down to sit inside the palette. Meaning never rides on color alone, so pair it with a sign, an icon or a word.
- Surfaces are solid colors from the ramp. Hue gradients, gradient text, colored glows and colored shadows, radial washes, blobs behind content and neon borders all go.
- Borders are quiet hairlines, the text color of the ramp at 6 to 10% opacity. A surface takes a border or a shadow, not both.
- On dark themes depth comes from surface steps and hairlines. On light themes shadows are neutral, soft and small.
- A gradient is allowed only as a small tone shift inside one neutral, like an active row going from #2b2b2b to #1f1f1f.

## 3. Icons

- Every emoji used as an icon or decoration becomes a line icon from one set. Use the set the project already has, otherwise lucide.
- One size and one stroke everywhere, 16 or 18px with a 1.5 stroke, in `currentColor`.
- Icons take the color of their text role, usually secondary or muted, and take hover, selected and disabled states from that color.
- The icon box has the same width in every row and the gap to the label is fixed, 8 or 10, so labels align.
- Icon-only buttons have an `aria-label`.
- Drop icons that add nothing, like one in every card title or before every section label. Categories that need color get a small status dot.

## 4. Copy

- Headlines say what the product does for whom, in plain words, using the facts already on the page.
- Name things the way users think of them, not how the system is built. A user manages notifications, not webhook config.
- A button says exactly what happens, and the action keeps its name through the flow: `Publish` produces `Published`.
- Interface text states things plainly, with no exclamation marks.
- The title names the context, like the page name or the period, for example `October 2026`, instead of a greeting like `Welcome back, Damir! 👋`.
- Short labels. `Search`, not `Search anything...`.
- A change says what it compares to, like `+12% vs last month`.
- Headlines, labels, buttons and captions end without a period. Only paragraphs keep their periods.
- An error names what went wrong and how to fix it. An empty state names the next action.
- Say what the thing does instead of hype words like supercharge, seamless, unlock or magic.
- Claims that cannot be checked, like `Loved by 10,000+ teams`, stay only if Jack confirms they are real.
- Mock data looks real, with plausible numbers and names, and totals that add up from the rows.
- Use `…` for loading states and for actions that open a follow up, like `Rename…`.

## 5. Type

- Choose type for the character in the direction, from the families in the tokens. Keep the project's font when it is part of a real brand. One family for the interface, plus at most one partner, a mono for figures and meta or a display face for large headlines.
- A few sizes from the type scale and two weights, 400 and 500, with 600 at most for rare emphasis. Headings stay solid colored.
- Hierarchy comes from size and color, not from weight.
- Sentence case everywhere, including labels and table headers.
- Small text keeps zero or slightly positive letter spacing. Tight tracking is only for large display text.
- `text-wrap: balance` on headings and `text-wrap: pretty` on paragraphs.
- Numbers use `tabular-nums` and one format across the screen, from `Intl.NumberFormat` in the user's locale.
- Emphasis comes from color or weight, not italic.

## 6. Layout

- Keep the sections and their order. Inside a section, alignment and proportions may change when that makes the screen clearer.
- Apps and dashboards keep real app proportions. The shell fills the viewport, a sidebar of 240 to 280 and fluid content capped around 1440 to 1600 wide. Never shrink an app into a narrow centered column. The rules for the canvas, KPIs, charts, tables and states are in [dashboards.md](dashboards.md).
- The strongest landing hero is a scene. One generated image fills the hero from edge to edge, its subject sits on one side, and the headline sits on the calm empty part of the same image, with the product view rising from the bottom edge.
- Without a scene, use an asymmetric split, text on one side and the visual given at least half the width, or text over a large product view below it. Everything stacked and centered is kept only for a short hero with no visual.
- Long headlines align left. Centered text works for one or two short lines.
- One primary action and at most one secondary action next to it.
- Navigation stays quiet. Logo, the existing links, one button. Log in is a quiet text link. On small screens the links collapse into one menu button.
- Compose the first screen as a whole, with no dead empty band.
- On small screens everything stacks in reading order. A dense preview gets simpler on mobile instead of being zoomed down.
- Layout changes at the project's breakpoints and nowhere else. Use flex and grid, `h-dvh` over `h-screen`, and `env(safe-area-inset-*)` for fixed elements.

## 7. Details

- Nested radius. An inner radius equals the outer radius minus the padding between them, never less than 4. Controls 8 to 10, cards 12 to 16, panels 14 to 20. Not everything is a pill.
- Counts and meta become quiet text instead of glowing pills. Keyboard shortcuts become small keycaps.
- Charts follow [dashboards.md](dashboards.md): one main chart, one accent per chart, the chart type picked for the data.
- Stat cards are a label, a big figure and a change with what it compares to. No sparklines, icons or mini bars added to fill them.
- Vary the sizes. Equal cards side by side with the same content read as a template.
- The active state is a small surface step with a hairline highlight.
- Hover, focus, pressed, disabled, loading, empty and error states exist and stay inside the palette, with a visible focus ring from `:focus-visible`.
- Theme the parts browsers draw: text selection, scrollbars, focus rings and `color-scheme` on `<html>` for dark themes.
- The logo is the product name in the main family, plus a simple flat mark if there is one.
- The signature detail from the direction appears where it belongs and nowhere else.

## 8. Visuals

- Decorative filler goes. Glossy blobs, orbs, nebulas, floating cubes, glowing grids and robots say nothing about the product.
- A landing hero gets a visual that shows something true. Dashboards and app screens almost never need generated images. Their moments come from the product itself, like a chart drawn with care or real content.
- Without an image tool, show the product. Build a preview in code of what the page already promises, with the project's components and plausible data.
- How to pick the subject, the prompt recipe and how to place an image are in [`../../ui-design/references/visuals.md`](../../ui-design/references/visuals.md). Read it before this pass whenever the screen needs a visual.
- Images get explicit dimensions, WebP or AVIF at twice the display size, a real `alt`, and high priority only above the fold.

## 9. Motion

Follow [motion.md](motion.md). Most screens need far less motion than you think: a press, a menu, and at most one entrance.

---

Passes 1 to 8 adapted from [unslop](https://github.com/heydamir/unslop) by Damir Sokolovsky ([@heydamir](https://x.com/heydamir)), CC BY 4.0, with copy rules from Anthropic's frontend-design skill (Apache 2.0) and Vercel's Web Interface Guidelines (MIT). Keep this credit in copies and adaptations.
