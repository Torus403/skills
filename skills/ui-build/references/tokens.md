# Tokens

Starting values for each pass. When the project already has a good system, keep its values and only fix how they are used. These are starting points, not a house style, so let the direction move them.

## Sizing standards

These hold whatever the direction says. They come from WCAG 2.2, Apple's Human Interface Guidelines and Material Design, so a screen that meets them works for every user on every device.

| What | Standard |
| --- | --- |
| Touch targets | At least 44 by 44 CSS px on touch screens. Pad the hit area when the visible control is smaller. Never below 24 by 24 anywhere (WCAG 2.5.8) |
| Control heights | 32 compact, 36 default, 40 to 44 large or touch. Buttons, inputs and selects that sit in one row share one height |
| Body text | 16px on landing pages and anything read on a phone. 14 to 15 is fine in a dense desktop app. Inputs stay at 16 or more on mobile so iOS does not zoom on focus |
| Smallest text | 12px, and 11px only inside a dense preview on mobile |
| Line length | 45 to 75 characters for paragraphs, about `max-width: 65ch` |
| Contrast | 4.5 to 1 for text, 3 to 1 for text from 24px (or 19px bold), icons, input borders and focus rings |
| Focus ring | Visible on every interactive element, at least 2px, offset from the control, from `:focus-visible` |
| Icons | 16, 18, 20 or 24, one stroke for the whole set |
| Breakpoints | The project's own. Without any, 640, 768, 1024, 1280 and 1536. Check every screen at 375, 768, 1280 and 1440 wide |
| Units | Font sizes in `rem` so they follow the browser setting. Spacing in the project's units |

## Spacing scale

4, 8, 12, 16, 20, 24, 32, 40, 48, 64, 80, 96, 128

- Inside a control: 4 to 12
- Between related items, like rows in a list: 2 to 8
- Between groups, like a label and its list or two cards: 12 to 24
- Between sections: 32 to 64, landing sections 80 to 128
- Row heights: 32 compact, 36 default, 40 to 44 touch
- Hero: 96 to 128 from the navigation to the headline on desktop, 48 to 64 on mobile

## App layout

- Sidebar 240 to 280 wide, content fluid with page padding 24 to 32, capped around 1440 to 1600.
- Top bar or page header 56 to 64 tall.
- Navigation rows 32 to 36, gap 2 to 4, section labels 24 above and 8 below.
- Stat cards in a row share one height, usually 3 or 4 compact cards per row on desktop, numbers only.
- The main chart spans at least two thirds of the content width and is 280 to 360 tall. A second data block next to it is a list or table, narrower, not another chart.

## Neutral ramps

For apps and dashboards use graphite, or a ramp just as grey, for every surface. For landing pages pick the ramp whose tint matches the world in the direction. Warm suits paper, wood, food, craft and anything human. Ink suits night, sky, water and anything technical. You can tint your own ramp the same way, keeping saturation very low, so a surface never reads as a color on its own.

### Dark

| Role | Graphite | Warm | Ink |
| --- | --- | --- | --- |
| Deepest surface, like a sidebar | #0f0f10 | #12110f | #07080d |
| Page background | #141415 | #161513 | #0b0d14 |
| Card | #19191b | #1c1a18 | #11141c |
| Raised, like an active row or input | #232325 | #262421 | #1a1e28 |
| Hairline | primary text at 8% | primary text at 8% | primary text at 8% |
| Primary text | #ededed | #efe9de | #eef0f5 |
| Secondary text | #a1a1a6 | #aaa398 | #a3a9b8 |
| Muted text and icons | #85858b | #8a847a | #7a8296 |

### Light

| Role | Graphite | Warm | Ink |
| --- | --- | --- | --- |
| Page background | #fafafa | #f7f4ee | #f5f7fa |
| Card | #ffffff | #fdfbf7 | #ffffff |
| Raised, like an active row or input | #f4f4f5 | #efe9df | #eceff4 |
| Hairline | primary text at 8% | primary text at 8% | primary text at 8% |
| Primary text | #171717 | #1f1b16 | #111827 |
| Secondary text | #525252 | #5e554a | #4b5565 |
| Muted text and icons | #737373 | #7b7266 | #6b7487 |

Muted text is for meta and captions only and stays near 4.5 to 1 on its surface. Body text uses primary or secondary.

Semantic colors, toned to sit inside any ramp: positive #4cc38a on dark and #16a34a on light, negative #e5484d on dark and #dc2626 on light.

## Accent

- Keep a real brand color. A violet to blue or any other hue to hue glow gradient is slop, not a brand color, unless the user says otherwise.
- Without a brand color, take it from the world. Warm worlds suit amber, coral or ember orange. Cool worlds suit cobalt, teal or a clear sky blue. Natural worlds suit moss or sage. Avoid the purple to blue family unless the brand really is purple.
- Text on the accent reaches 4.5 to 1 contrast. Darken the accent or use dark text when it does not.
- The accent covers a few percent of the screen, like the primary action, the selection and one key figure.

## Buttons

- Hero buttons 44 to 48 tall, navigation buttons 32 to 36, padding 16 to 20 on the sides.
- Primary on dark: an off white from the ramp with dark text, or the accent. Primary on light: the primary text color as a fill with white text, or the accent.
- Secondary: the raised surface with a hairline, primary text.
- A soft top highlight like `inset 0 1px 0 rgba(255,255,255,0.12)` on dark buttons gives depth without a glow.

## Type families

Pick by the character in the direction. All of these are free, and a partner can come from any row.

| Character | Interface family | Optional partner |
| --- | --- | --- |
| Precise, technical, calm | Geist, Inter, IBM Plex Sans | Geist Mono, IBM Plex Mono, JetBrains Mono for figures and meta |
| Warm, friendly, human | Instrument Sans, DM Sans, Figtree | Instrument Serif or Newsreader for the hero headline only |
| Editorial, literary, crafted | Inter or Instrument Sans for the interface | Newsreader, Instrument Serif or Fraunces for headlines |
| Playful, bold | Space Grotesk, Bricolage Grotesque | a mono for small labels |

A display serif belongs to large headlines only, never to labels or buttons.

## Type scale

| Use | Size | Line height | Weight |
| --- | --- | --- | --- |
| Small labels, meta, counts | 12 | 16 | 400, mono welcome |
| Secondary text, captions | 13 to 14 | 20 | 400 |
| Body, nav items | 14 to 15 | 20 to 22 | 400 to 500 |
| Logo wordmark | 16 to 18 | 1 | 500 to 600 |
| Hero subhead | 18 to 20 | 28 to 30 | 400, secondary color, at most 36rem wide |
| Card figures | 28 to 32 | 1 | 500, tabular |
| Page title | 28 to 36 | 1.15 | 400 to 500 |
| Hero headline | 56 to 72 desktop, 36 to 44 mobile | 1.02 to 1.08 | 400 to 500 |

Letter spacing is 0 for anything under 16px, slightly positive like 0.01em is fine for small muted text. Display text from 40px can go to -0.02em, and from 56px to -0.03em.

## Radius

| Element | Radius |
| --- | --- |
| Keycap, tag, small button | 4 to 6 |
| Row, input, button | 8 to 10 |
| Card | 12 to 16 |
| Panel or window | 14 to 20 |

Nested radius: inner = outer − padding, never below 4. A 16px card with 8px padding holds items with an 8px radius.

## Icons

lucide, 16 or 18px, stroke 1.5, color of the muted or secondary text role, 8 to 10px gap to the label.

## Depth

- Dark: surface steps plus a hairline. An active row can carry `inset 0 1px 0 rgba(255,255,255,0.12)` as a top highlight.
- Light: `0 1px 2px rgba(0,0,0,0.05)` for small things, `0 8px 24px rgba(0,0,0,0.06)` for floating ones.

## Motion

Define the curves and durations once, as tokens. The values come from the **emil-design-eng** skill, which says when to use each:

```css
--ease-out: cubic-bezier(0.23, 1, 0.32, 1);
--ease-in-out: cubic-bezier(0.77, 0, 0.175, 1);
--ease-drawer: cubic-bezier(0.32, 0.72, 0, 1);
--duration-press: 160ms;
--duration-menu: 200ms;
--duration-sheet: 300ms;
```

## Layers

One z-index scale, named by role, never an arbitrary `z-*`: base, sticky header, dropdown, overlay, dialog, toast.

---

Adapted from [unslop](https://github.com/heydamir/unslop) by Damir Sokolovsky ([@heydamir](https://x.com/heydamir)), CC BY 4.0. Keep this credit in copies and adaptations.
