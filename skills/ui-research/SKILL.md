---
name: ui-research
description: Study how the best real products solve a screen, flow or website section on Mobbin before designing it. Use before designing or redesigning any website, landing page, dashboard or app screen, or when asked for UI references or inspiration.
---

# UI research

Study how the best real products solve this screen before you design it. The design comes after the research, never before. Mobbin is a library of screens, flows and website sections from shipped apps and sites, searchable through its MCP tools (`search_screens`, `search_flows`, `search_sections`).

## If Mobbin is missing

Search your tools for Mobbin. If it is not connected, tell Jack the research step needs it and ask Jack to connect the Mobbin connector. Wait until it is connected or Jack says to go without it. Never skip the research silently.

## Search

1. **Name what you are designing.** One screen, flow or section at a time, with the kind of product, like `invoices list in a billing app`, `onboarding for a team analytics tool` or `pricing section for a developer tool`.
2. **Pick the tool.** `search_screens` for one screen of an app or dashboard. `search_flows` for a journey across screens, like sign up, checkout or an empty state into a first result. `search_sections` for parts of a website, like a hero, pricing, features or a footer.
3. **Search wide, then narrow.** Use `platform: "web"` for websites and dashboards. Start with the plain pattern, then add the product kind. Search a named app directly when Jack or the codebase points at one. Use `output_destination: "code"` and keep `task_intent` the same on every call.
4. **Look at the images.** Judge each result by what the screen shows, never by its metadata alone.

Done when you have studied 8 to 15 strong results from at least 5 different products, and every screen, flow and section the task adds is covered.

## Study

For each strong result, note what it does that you would keep:

- **Content.** What the screen shows first, what it leaves out, and how much fits above the fold.
- **Hierarchy.** The one thing the eye lands on, and how size, weight and color get it there.
- **Layout and density.** The grid, column widths, row heights and spacing rhythm.
- **Components.** Which controls it uses for each job, like a table versus a list, a tab versus a select.
- **States.** Empty, loading, error, long content, a first-time user.
- **Copy.** How it names things, and how short its labels are.

Then compare. Patterns that most of the best products share are the expected baseline, so users already know them. What the best one or two do differently is where the ideas are.

## Write the research brief

A short list Jack can read in a minute. It feeds the direction and the plan in the **ui-design** skill.

- **Patterns to follow**, each with two or three Mobbin links (`mobbin_url`) as evidence.
- **Ideas worth taking**, each with the one link it came from and what exactly to take.
- **Traps** you saw, like a dense table that breaks on mobile.

Take qualities, never a whole screen. The direction still comes from this product, so the result looks like this product and nobody else's.

Save picks to a Mobbin collection only when Jack asks for one.
