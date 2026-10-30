# Breaking a screen with worst-case data

Demo data is chosen, usually without anyone noticing, to make the design look good: names that fit on one line, counts that never need a separator, every optional field filled in. Undo that choice one field at a time.

Every worst-case value is something a real user could produce, or the longest value the backend accepts. `aaaaaaaa` and 5,000 character names prove nothing. Long text is the obvious break. The ones that ship are the short name, the missing avatar, the count of exactly 1 ("1 members") and the empty list.

## 1. Map the fields

List every value the screen renders, with its source, its type, its limit and whether it is optional:

| Field | Source | Type | Limit | Optional |
| --- | --- | --- | --- | --- |
| `name` | `member.name` | string | 255 (`schema.ts:14`) | No |
| `email` | `member.email` | string | none found | No |
| `count` | `workspace.memberCount` | int | none | No |

Include the values people forget: counts in headers, relative timestamps, badge and status text, labels that come from data, tooltips, avatars, and the length of each list. Look up limits in the validation schema, database migrations, API types and `maxLength` attributes. No limit is itself a finding: write "unbounded".

Done when every rendered value is in the table with a source and a limit.

## 2. Build the fixtures

Pick values from [worst-case-catalog.md](worst-case-catalog.md). Build one worst-case fixture next to the existing demo data, shaped exactly like it, and spread the different failures across the first rows, since those are on screen. Add these as separate fixtures:

- **Empty.** Zero items and the no-results state.
- **One.** A single item, and every count at exactly 1.
- **Huge.** The realistic upper bound for list length, 1,000 rows or more for an unpaginated list.

The worst case enters through the same boundary as the demo data: the fixture, the mock, the props or the API stub. Never edit markup or CSS to produce a break. Put the switch behind a dev-only URL param like `?data=worst`, so a reload keeps it and it never ships.

## 3. Look for the failure signatures

View each fixture at the component's real container width, at 320px and at the widest layout, with browser zoom at 200%, and in dark mode and RTL when the product supports them.

| What you see | Cause | Fix |
| --- | --- | --- |
| Avatar or icon squished into an oval | Flex child shrinking | `flex-shrink: 0` on the fixed-size box |
| Text overflows its box | Flex or grid child with `min-width: auto` | `min-width: 0` on the text column, `minmax(0, 1fr)` in grid |
| Email or URL runs past the edge | No break opportunities | `overflow-wrap: anywhere` |
| Trailing action pushed off screen | Middle content took the space | `min-width: 0` on the middle, `flex-shrink: 0` on the action |
| Badge wraps onto two lines | Badge allowed to shrink | `white-space: nowrap; flex-shrink: 0` on the badge |
| Avatar adrift beside a three line name | `align-items: center` on rows of varying height | Top-align once text can wrap |
| Wrong initials, like `J` for "Jo" | `.split(' ')[0][0]` | Grapheme-aware initials with `Intl.Segmenter`, and a fallback icon |
| Orphaned dash where an optional field was | Placeholder for a missing field | Omit the line, or reserve its height on purpose |
| "1 members" | Hardcoded plural | `Intl.PluralRules` |
| `1284`, `NaN`, `undefined` | Raw number rendered | `Intl.NumberFormat` in the user's locale, and a null guard |
| Translated button label overflows | Fixed-width button | Width from content with a `min-width` |
| Diacritics clipped top or bottom | Tight `line-height` with `overflow: hidden` | Looser line height, or no clipping on text |
| Broken image icon | No error fallback | Fall back to initials, `object-fit: cover` |
| Truncated text with no way to read it | Ellipsis and nothing else | A `title` or tooltip, and the full value in a detail view |
| 1,000 rows stutter | Every row rendered | Virtualize or paginate |

For each long string, choose per field: **wrap** what users need in full to identify something, **truncate at the end** secondary metadata, **truncate in the middle** values that differ at the end, like file names, **clamp** previews in cards, and **never truncate** numbers, amounts or dates people compare.

Done when every catalog row that applies has been tried at every width and setting above, and every break has a cause and a fix.

---

Adapted from [break-ui](https://github.com/emilkowalski/skills/tree/main/skills/break-ui) by Emil Kowalski (MIT).
