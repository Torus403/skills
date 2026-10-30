# Page signals

Rung 2. Each page says what it is in its title, description, headings, URL, links and images, and says it differently from every other page.

## Title

The strongest on-page signal you control, and the first thing a searcher reads.

- Unique on every page, describing that page's topic.
- Search the target query first. Match the format the ranking results share (guide, tool, list, comparison, product page) and use the words searchers expect.
- Structure: `[primary query] + [the reason to click] + [brand, when it helps]`. The query goes first and the brand last.
- About 50 to 60 characters, as a lint, not a rule. Google truncates by pixel width, so keep the important words in the first 50.
- Agrees with the H1, the URL and the description. They need not match word for word.
- Use "free", a year or a number only when the page delivers it.

| Page type | Pattern |
| --- | --- |
| Product or feature | `[Category] for [Audience] \| [Brand]` |
| Pricing | `[Brand] Pricing: Plans and Costs` |
| Comparison | `[A] vs [B]: [the deciding difference]` |
| How-to | `How to [Task]` |
| Definition | `What Is [Term]? [Short payoff]` |
| Guide | `[Topic]: A Guide for [Audience]` |
| Tool or template | `Free [Thing] [Calculator or Template]` |
| Home | `[What the product does] \| [Brand]` |

Google rewrites titles that are generic ("Home"), stuffed with keywords or boilerplate, much longer than the display, or out of line with the H1. A rewritten title in Search Console is a signal to fix that one.

## Meta description

- Unique on every page. A summary of the page that gives a reason to click.
- About 150 to 160 characters, as a lint.
- Not a ranking factor. Google often picks page text instead, so the page's opening paragraph matters as much.

## Headings

- One visible H1 per page that names the topic. Google does not penalize several H1s, but one H1 keeps the page clear to readers, screen readers and crawlers.
- H2 and H3 in order, without skipped levels, each describing its section.
- Headings carry structure, never styling. Style text with classes.

## URL

- Lowercase, words joined by hyphens, short and readable: `/guides/invoice-template`, not `/p?id=812`.
- Stable. Changing a URL needs a 301 forever, so change the title instead of the slug to chase a year.
- No session IDs or tracking parameters in internal links.

## Internal links

The cheapest lever and the most neglected.

- Every indexable page is linked from at least one other crawlable page. A page reachable only through the sitemap is an **orphan**.
- Important pages are linked from the navigation, the homepage or hub pages, and sit within about three clicks of the homepage.
- Anchor text describes the target: "invoice template for freelancers", not "click here" or "read more".
- Link new pages from three or more related existing pages when they ship.
- Breadcrumbs on every page below the top level, as real links, with BreadcrumbList markup from [structured-data.md](structured-data.md).
- Every internal link points at the final URL, never at a redirect or a 404.
- Mark paid links `rel="sponsored"` and user-submitted links `rel="ugc"`.

## Images

- Content images are `<img>` elements with a `src`, not CSS backgrounds, so Google can index them.
- Alt text describes what the image shows, in context, in a short sentence. Decorative images get `alt=""`. Never stuff keywords.
- Descriptive file names: `blue-standing-desk.avif`, not `IMG_2041.jpg`.
- `width` and `height` on every `<img>`, plus `srcset` and `sizes` for responsive images.
- AVIF or WebP at the size they display. The right dimensions save more bytes than the format does.
- `loading="lazy"` below the fold only. The LCP image loads eagerly with `fetchpriority="high"`.
- Place images near the text they illustrate.

## Head basics

```html
<html lang="en">
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Invoice Template for Freelancers | Acme</title>
<meta name="description" content="A free invoice template that totals tax and due dates for you. Download as Google Sheets or Excel.">
<link rel="canonical" href="https://acme.com/templates/invoice">
<meta property="og:title" content="Invoice Template for Freelancers">
<meta property="og:description" content="A free invoice template that totals tax and due dates for you.">
<meta property="og:image" content="https://acme.com/og/invoice.png">
<meta property="og:url" content="https://acme.com/templates/invoice">
<meta property="og:type" content="website">
<meta name="twitter:card" content="summary_large_image">
```

- Open Graph and Twitter tags control link previews in chats and social posts. They do not affect ranking, but a shared link with no image gets fewer clicks. Images are 1200 by 630.
- **Favicon.** Google shows it beside results. Square, larger than 48 by 48 pixels, at a stable crawlable URL, linked with `<link rel="icon">` on the homepage.
- **Site name.** Google takes the name shown above results from WebSite markup on the homepage, in [structured-data.md](structured-data.md).

## Checks

- [ ] No duplicate titles or descriptions in the audit
- [ ] Every title leads with what the page is about
- [ ] One H1 per page, headings in order
- [ ] No orphans, no internal link to a redirect or a 404
- [ ] Every meaningful image has alt text, every image has width and height
- [ ] Every page has Open Graph tags with an image
