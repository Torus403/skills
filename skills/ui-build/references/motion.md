# Motion

Motion explains a change or confirms an action. Everything else is decoration, and decoration that repeats wears people out.

## Should it animate at all

Decide by how often people see it.

| Frequency | Decision |
| --- | --- |
| Hundreds of times a day: keyboard shortcuts, a command palette, tab switches | No animation |
| Tens of times a day: hovers, list navigation, row actions | Instant, or 150ms or less on color or opacity |
| Occasional: menus, dialogs, drawers, toasts | Standard motion |
| Rare: onboarding, a success state, a first empty state | Room for one expressive moment |

Keyboard initiated actions never animate. Every animation has a purpose you can name: spatial consistency, a state change, feedback on a press, or softening something that would otherwise pop in. "It looks nice" on something seen often is not a purpose.

## Easing and duration

One set of curves for the whole product, from the tokens:

```css
--ease-out: cubic-bezier(0.23, 1, 0.32, 1);     /* entering, exiting, most UI */
--ease-in-out: cubic-bezier(0.77, 0, 0.175, 1); /* moving or morphing on screen */
--ease-drawer: cubic-bezier(0.32, 0.72, 0, 1);  /* sheets and drawers */
```

- Entering and exiting use ease-out. Things moving on screen use ease-in-out. Hover and color changes use plain `ease`. Constant motion, like a progress bar, is linear.
- Never ease-in on UI. It starts slow at the moment the user is watching.

| Element | Duration |
| --- | --- |
| Press feedback | 100 to 160ms |
| Tooltips, small popovers | 125 to 200ms |
| Dropdowns, selects, menus | 150 to 250ms |
| Dialogs, drawers, sheets | 200 to 500ms |
| Marketing or explanatory motion | longer when it teaches something |

UI motion stays under 300ms. Exits are faster and smaller than entrances.

## Recipes

- **Press.** Pressables scale to `0.97` on `:active` over 160ms ease-out. Disabled controls never scale.
- **Enter.** Start from `opacity: 0` and `scale(0.95)` or a `translateY` of 8 to 12px. Never from `scale(0)`.
- **Origin.** Popovers, menus and tooltips scale from their trigger with `transform-origin` at the trigger. Dialogs stay centered.
- **Tooltips.** Delay the first one. Once one is open, neighbours open instantly with no animation.
- **Entrance on load.** At most one, for the main content, with a 30 to 80ms stagger across at most six items. Never block interaction while it plays.
- **Icon swaps** on infrequent state changes, like copy to copied, cross-fade with a little scale and blur.
- **First render.** State swaps do not animate on mount, so `AnimatePresence` around a swap gets `initial={false}`.
- **Theme switch.** Disable transitions for the swap so every color does not animate at once.
- **Number changes** tween, with `tabular-nums` so digits do not jitter.

## Mechanics

- Animate `transform` and `opacity`. Small local `color` and `background-color` changes are fine. Width, height, top, left, margin and padding never animate.
- Name the properties: `transition: transform 200ms var(--ease-out), opacity 200ms var(--ease-out)`, never `transition: all`.
- Use CSS transitions for anything that can be interrupted or reversed, like toggles, hovers and toasts. Keyframes are for sequences that run once.
- Prefer CSS, then the Web Animations API, then a JS library. With Motion, animate the full `transform` string under load, since the `x` and `y` shorthands run on the main thread.
- `@starting-style` animates an element's entry without JavaScript where support allows.
- `will-change` only after you see first-frame stutter, naming the animated property.
- Blur stays under 20px and never animates on a large surface.
- Pause loops when they are off screen.
- Hover effects sit behind `@media (hover: hover) and (pointer: fine)`, so taps on touch screens do not latch them.

## Reduced motion

Respect `prefers-reduced-motion`. Reduced means gentler, not nothing: keep opacity and color changes that help comprehension, and drop movement, scale and blur. Every animated state change also leaves a static cue, a color, an icon or a label, so meaning never depends on motion.

---

Condensed from Emil Kowalski's skills (MIT), Jakub Krehel's better-ui (MIT) and Vercel's Web Interface Guidelines (MIT).
