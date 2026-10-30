# Dashboards and app screens

Rules for screens people work in every day: dashboards, analytics, admin, settings, lists and inboxes. A dashboard is read every day, so it earns calm through structure, not decoration.

## One question, one finding

- **The one question.** Write the question the screen answers first in one line, like "Did today's orders ship?" or "Which deploy broke?". The biggest block answers it, it comes first in reading order, and anything that answers no question is cut.
- **The one finding.** Name the fact in today's data that most needs attention, like "the 23:28 deploy doubled the error rate". Put it where it is read first, under the title or under the headline figure, next to the action it drives.
- **Blocks answer the next questions.** List each block as the answer to a follow-up question, one line each. This replaces the stock order of KPI row, big chart, two small charts, table.
- **The first screen holds the brief.** At 1440 by 900, every block the brief asks for shows its header and first rows or figure. Cap overview lists at 4 to 6 rows with "View all".
- **The main job is one click away.** Put its control where the answer shows: a primary button in the title row, an action on the row that needs it.
- **Evidence beside the answer.** A spike gets one line naming its cause rather than a second chart.

## Shell and canvas

- A sidebar of 240 to 280 on the page background, or one tone step from it, never a dark or saturated sidebar on a light screen. The active row is a neutral surface step.
- A top bar only when it carries something: search, a switcher or the object's name.
- Content is fluid, capped around 1440 to 1600, with one left edge and one right edge shared by every block.
- The title is a noun, like `Orders` or `October 2026`, at 18 to 32px. No greeting and no hero header.

## KPIs

- Prefer one container split by 1px dividers into equal columns over a card per KPI. Or put each headline number at the top of the block that explains it, which is often better.
- 3 or 4 per row. A label above, 12 to 14px, sentence case, grey. The value 24 to 30px at 400 to 500 in ink. Nothing at 48px or over.
- The figure that answers the screen's question is the largest on the screen, 30 to 36px, at least 1.3 times its siblings.
- Units are a smaller grey suffix. No icon in a colored circle, no sparkline, no tinted tile.
- **Deltas.** Optional, at most the label's size, with the window in words: `+12% vs last 30 days`. Color means good or bad, not up or down, since errors, latency and cost are better when they fall. A zero or undefined change is grey. A change from zero reads `+4 (new)`.

## Charts

| Question | Chart |
| --- | --- |
| Is it moving over time? | One line, an area only with a fill of 15% or less |
| How much per period? | Columns with square corners |
| Who ranks? | A sorted horizontal bar list |
| What share? | A thin ring or one 100% stacked bar, five parts at most |
| How far to a target? | A progress bar at the true ratio, both ends labelled |
| A few numbers | No chart. Show the numbers |

- One main chart, clearly the biggest thing on the screen, about two thirds of the content width and 200 to 360 tall. Anything else that shows data is smaller and different in kind, like a ranked list or a short table.
- One series per chart, three at most. Switch metrics with a control instead of overlaying lines.
- One hue per chart, on the thing that matters, like the current period. Everything else sits in neutral steps. One subject keeps one hue across the screen. Four hues at most on a screen.
- 3 to 5 faint horizontal gridlines, no y-axis line, round ticks with the top one above the maximum, zero as the baseline for bars and counts. Axis labels 11 to 12px grey, never rotated.
- Lines 2px in straight segments, no point markers. Bars square, or a 4px top radius on a square base.
- No legend for a single series. Otherwise a small dot and label in the card header, five at most.
- A spike or step that matters gets a 1px marker and a short label naming its cause. A forecast is dashed after today.
- An empty chart is drawn honestly: the zero line, missing bars for empty periods, one sentence.
- Charts are accessible: color-blind safe hues, and values available as text or in a table.

## Tables and lists

- Single line rows 40 to 48, two line rows 56 to 72, header 36 to 40.
- Headers 12px grey sentence case, no fill band, no zebra striping. Row rules 1px and 3 to 7% darker than the surface, or space alone.
- Numbers right-aligned in tabular figures, with their header right-aligned above them. Fixed decimals per metric: money 2, percentages 1 or 2, counts none. Thousands separators everywhere.
- The identity column gets the most width and is never the one cut off. Truncate to one line with an ellipsis and a way to read the full value.
- Only the identity and the key number take the primary ink. Everything else is grey.
- A missing value is a grey dash. A real zero is printed, like `$0`.
- Status pills are pale tints with dark text of the same hue, 20 to 24px tall, inside rows only.
- Capped rows and "View all" instead of pagination under a short list. Virtualize or paginate lists over about 50 rows.

## Density

Density is three settings moved together: row height, padding and type size.

- **Sparse**, about 6 to 25 data points: card padding 20 to 24, rows 56 to 72, body 14 to 16.
- **Medium**, 25 to 50: rows 44 to 56, padding 16 to 24.
- **Dense**, monitoring and research read for hours: a 13px body and 32 to 40px rows, framed with generous gutters.

Placed space reads as calm and leftover space reads as unfinished. A column empty in every row or a card stretched to its neighbour's height is leftover.

## States

- **Loading.** The final layout with each value replaced by a flat grey bar at its real size, labels and headers shown at once, no shimmer, and no layout shift when the data lands.
- **Empty.** A section keeps its frame and header and adds one sentence with the next action.
- **First run.** Keep the frame and title, and put the first action where the data will appear.
- **Error.** Inside the block that failed, never a full screen banner. One sentence saying what failed and when the data was last good, and a Retry button.
- **Stale.** A freshness stamp with a refresh control.
- **Counts follow the view.** Counts in tabs and headers are computed from the current filter and update on every switch.
- **State in the URL.** Filters, tabs, sort and pagination deep link, and Back restores them.

## Tells of generated dashboards

| Tell | Instead |
| --- | --- |
| A dark navy sidebar with a colored active pill and a left bar | The sidebar on the page background, a neutral active step |
| "Welcome back, Alex 👋" | A noun title |
| Four KPI cards, each with an icon in a tinted circle and a sparkline | One divided container, label over value |
| A green `+12.5%` pill on every KPI | A delta in words with its window, grey when flat |
| A gradient area chart with a smoothed line and a dot on every point | A 2px straight line, no fill or a light one, no markers |
| A rainbow palette, a hue per bar | One hue per chart, neutrals for the rest |
| A fat donut with labels on the slices | A thin ring with the legend as a small table |
| A zebra table under uppercase headers with a checkbox, avatar, chip and kebab on every row | Rules, alignment, one status mark, one action where needed |
| Saturated status chips with white text | Pale tints with dark text |
| The accent on every button, tab and link | The accent on data and at most one control |
| Placeholder people, round vanity totals, totals that do not add up | Believable data, totals summed from the rows |
| An illustration and "No data yet" in an empty chart | The zero line and one sentence |

A screen with every tell removed and nothing in its place is a tidy template. What fills the space is the product: its own data at its real size, the screen's one question answered by its biggest block, and one detail only this product has.

---

Condensed from the app screens reference in [taste-skill](https://github.com/Leonxlnx/taste-skill) by Leonxlnx (MIT) and from [unslop](https://github.com/heydamir/unslop) by Damir Sokolovsky ([@heydamir](https://x.com/heydamir)), CC BY 4.0.
