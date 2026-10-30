# Crawl and index

Rung 1. Every page meant to rank must be fetchable, rendered on the server, indexable and canonical. Every page meant to stay out must say so in a way Google can read. Stack specifics are in [stack.md](stack.md).

## Rendering

Serve every public page as complete HTML from the server, by server rendering or prerendering.

- The main content, title, meta description, canonical, robots meta, Open Graph tags and JSON-LD are all in the initial HTML response.
- Google renders JavaScript later, in a queue, and only for pages that return 200. It may skip rendering a page whose raw HTML says `noindex`, so a `noindex` removed by JavaScript can still stick.
- Set the canonical in the HTML. If JavaScript changes it, Google may use either value.
- Many AI crawlers and link previews do not run JavaScript at all. To them, a client-rendered page is empty.
- Keep main content visible on load. Content that loads only after a click, a scroll or a tab change may never be seen.

Check: the audit's word count per page is close to what the rendered page shows. A page under 150 words in the server HTML is a finding unless it is meant to be short.

## Links Google can follow

- Google discovers pages only through `<a>` elements with an `href` holding a real URL. A `div` or `button` that navigates in `onClick` is invisible to it.
- Route with the History API. Never load different content on `#fragment` URLs.
- Give paginated lists real `<a href>` links to each page, and back infinite scroll or "load more" with paginated URLs. Each page of a list has its own self-referencing canonical. Google no longer uses `rel="next"` and `rel="prev"`.

## Status codes

| Situation | Response |
| --- | --- |
| A real page | 200 |
| Moved for good | 301 or 308, straight to the final URL |
| Moved for now | 302 or 307 |
| Never existed or deleted | 404, or 410 when gone for good, with a helpful page body |
| Down for maintenance | 503 with `Retry-After` |

- A missing page that returns 200 is a **soft 404**. Google treats it as low value and it wastes crawling. The audit requests a made-up URL to catch this.
- Repeated 5xx or 429 responses make Google slow its crawling.
- Use server redirects. Meta refresh and JavaScript redirects are a last resort.

## Redirects

- Every redirect takes one hop. Point an old URL at the final URL, never at another redirect.
- Update internal links, canonicals, hreflang and the sitemap to the final URL, so no internal link hits a redirect.
- Pick one form of every URL and redirect the rest to it: `https`, one of `www` or apex, one trailing slash policy, lowercase.
- When a URL changes, 301 the old one forever. Keep a redirect map in the repo for site moves.

## robots.txt

- Lives at the root of each host, returns 200 as `text/plain`, and names the sitemap with an absolute `Sitemap:` line.
- Controls crawling, not indexing. A URL blocked in robots.txt can still be indexed from links, without its content, and Google cannot see a `noindex` on a page it may not fetch. To keep a page out of the index, allow crawling and send `noindex`.
- Never block the CSS, JavaScript, images or API calls a public page needs to render.
- Disallow only what has no search value: admin, API, cart, checkout, internal search results, endless filter combinations.
- A robots.txt that answers with a 5xx can stop Google crawling the whole site.

```text
User-agent: *
Disallow: /admin/
Disallow: /api/
Disallow: /search

Sitemap: https://example.com/sitemap.xml
```

## noindex

- Send `<meta name="robots" content="noindex">` in the HTML, or `X-Robots-Tag: noindex` as a header for non-HTML files like PDFs.
- Remove every `noindex` from pages meant to rank. Check both the HTML and the headers, at every layer that can add one: framework config, a staging flag left on, a CDN rule.
- Keep `noindex` on pages meant to stay out: thank-you pages, internal search, account screens, staging and preview hosts.
- Never put a page in the sitemap that is `noindex`, redirected or non-canonical.

## Canonicals

- Every indexable page has one `<link rel="canonical">` in the `<head>`, with an absolute URL to itself.
- A duplicate points at the original. URL parameters for tracking, sorting or sessions point at the clean URL.
- The canonical URL returns 200, is indexable, and agrees with the sitemap, internal links, hreflang and redirects.
- A canonical is a hint. Google chooses a different one when the signals disagree, which Search Console reports as "Duplicate, Google chose different canonical than user".
- Never canonicalize page 2 of a list to page 1, every page to the homepage, or one language to another.

## Sitemaps

- Generate the sitemap from the routes and the content source, never by hand.
- List only absolute, canonical, indexable URLs that return 200.
- `lastmod` is the date the main content, structured data or links last changed. Google uses it only when it is consistently accurate, and ignores `priority` and `changefreq`.
- One file holds at most 50,000 URLs or 50 MB uncompressed. Split larger sites with a sitemap index, by content type.
- Reference it in robots.txt. Submitting it in Search Console is Jack's step, in [owner-tasks.md](owner-tasks.md).

## Hosts and duplicates

- One host serves the site. Every other host that answers with the same pages (`*.workers.dev`, `*.pages.dev`, the IP, an old domain) redirects to it or sends `noindex`.
- Preview and staging deployments send `noindex` or sit behind access control.
- HTTPS everywhere, with HTTP redirecting to HTTPS and no mixed content.

## Mobile

Google indexes the mobile version. The mobile page has the same content, title, headings, structured data and robots tags as desktop, and a `<meta name="viewport" content="width=device-width, initial-scale=1">`. Avoid interstitials that cover the main content on load.

## Languages and regions

Only when the site serves more than one language or region:

- One URL per language, in subdirectories like `/en/` and `/de/`. Never switch language by IP or `Accept-Language` on the same URL, since Googlebot crawls from the US without that header.
- `<html lang>` on every page, and every main word translated, not only the navigation.
- Hreflang on every variant listing every variant and itself, with valid codes like `en-GB` (never `en-UK`), each pointing at a canonical URL that returns 200. Add `x-default` for the fallback.
- Each language self-canonicalizes. A canonical across languages hides the variant.

## AI search and AI crawlers

Google's AI Overviews and AI Mode use the normal index. They need no special file, markup or schema: a page that is indexed and allowed a snippet is eligible. `nosnippet`, `data-nosnippet`, `max-snippet` and `noindex` limit what Google shows.

Other assistants run their own crawlers, each with a separate robots.txt token. Blocking a training crawler does not remove the site from that company's search:

| Token | Company | Purpose |
| --- | --- | --- |
| `Googlebot` | Google | Search, including AI Overviews |
| `Google-Extended` | Google | Gemini training and grounding. No effect on Search |
| `Bingbot` | Microsoft | Bing search, which also serves other engines and assistants |
| `OAI-SearchBot` | OpenAI | ChatGPT search results |
| `ChatGPT-User` | OpenAI | Fetches a page when a user asks |
| `GPTBot` | OpenAI | Training |
| `Claude-SearchBot` | Anthropic | Claude search results |
| `Claude-User` | Anthropic | Fetches a page when a user asks |
| `ClaudeBot` | Anthropic | Training |
| `PerplexityBot` | Perplexity | Perplexity search |
| `Applebot-Extended` | Apple | Opts out of Apple's AI training. Siri and Spotlight follow `Applebot` |

- Allow every search and user-fetch crawler by default. Whether to allow training crawlers is Jack's call.
- Cloudflare can prepend its own rules to robots.txt and block AI crawlers at the edge. Read the served `/robots.txt`, not the file in the repo.
- `llms.txt` is an optional proposal. No major search engine needs it, and Google says AI text files are unnecessary. Add one only when Jack asks.
- Vendors rename crawlers. Check the vendor's current crawler page before writing a rule for one.

## Checks

- [ ] The audit shows no `HIGH` on robots, sitemap, status, redirects, noindex or soft 404
- [ ] Every page meant to rank has its content in the server HTML
- [ ] Every navigation is an `<a href>` with a real URL
- [ ] Every redirect is one hop and permanent where the move is permanent
- [ ] One host, one protocol, one trailing slash policy
- [ ] Every page meant to stay out sends `noindex` and is not in the sitemap
- [ ] The served robots.txt allows `Googlebot`, `Bingbot` and the search crawlers Jack wants
