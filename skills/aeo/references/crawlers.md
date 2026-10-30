# AI crawlers and access

Each AI vendor runs separate bots for search, for fetches a user asks for, and for model training. They are separate controls, so decide each one on purpose. Blocking a training bot does not remove a site from that vendor's answers, and blocking a search bot does.

Facts below come from each vendor's own page, checked October 2026. Names and behavior change, so re-check the linked page before telling Jack a bot does something.

## The bots

| Token | Vendor | Kind | What it does | Honors robots.txt |
| --- | --- | --- | --- | --- |
| `Googlebot` | Google | Search | Crawls for Google Search. AI Overviews and AI Mode use the same index, so Googlebot rules are the only crawl control for them. | Yes |
| `Google-Extended` | Google | Training | A robots.txt token only, never a separate crawler. Controls use of content Google already crawled for Gemini training and grounding. No effect on Search inclusion or ranking. | Yes |
| `Bingbot` | Microsoft | Search | Crawls for Bing, which Copilot answers from. | Yes |
| `OAI-SearchBot` | OpenAI | Search | Surfaces sites in ChatGPT search. Opted out sites are not shown in ChatGPT search answers, only as plain navigational links. Changes take about 24 hours. | Yes |
| `ChatGPT-User` | OpenAI | User fetch | Visits a page when a ChatGPT user or Custom GPT asks. Not used to decide what appears in search. | May not apply |
| `GPTBot` | OpenAI | Training | Crawls content that may train OpenAI's foundation models. Independent of `OAI-SearchBot`. | Yes |
| `Claude-SearchBot` | Anthropic | Search | Indexes content to improve Claude's search answers. Blocking it can reduce visibility in Claude's answers. | Yes |
| `Claude-User` | Anthropic | User fetch | Fetches a page when a Claude user asks. Blocking it stops Claude retrieving the page for users. | Yes |
| `ClaudeBot` | Anthropic | Training | Collects content that may train Anthropic's models. Supports `Crawl-delay`. | Yes |
| `PerplexityBot` | Perplexity | Search | Builds Perplexity's search index. Not used for model training. A disallowed page may still show as a headline and short summary. | Yes |
| `Perplexity-User` | Perplexity | User fetch | Visits a page to answer a user's question. | Generally ignores it |
| `Applebot` | Apple | Search | Crawls for Siri, Spotlight and Safari search. | Yes |
| `Applebot-Extended` | Apple | Training | A token only. Controls use of Applebot's crawl for Apple's foundation models. | Yes |
| `meta-webindexer` | Meta | Search | Crawls so Meta AI can cite and link the site. | Yes |
| `meta-externalfetcher` | Meta | User fetch | Fetches a link a user asked about. | May bypass |
| `meta-externalagent` | Meta | Training | Crawls to train models and index content for products. | Yes |
| `facebookexternalhit` | Meta | Link preview | Builds the title and image when a link is shared. Keep it allowed. | Mostly |
| `CCBot` | Common Crawl | Training | Builds the open Common Crawl corpus that many model trainers use. | Yes |

Vendor pages: [OpenAI](https://developers.openai.com/docs/gptbot), [Anthropic](https://support.claude.com/en/articles/8896518), [Google AI features](https://developers.google.com/search/docs/appearance/ai-features), [Google crawlers](https://developers.google.com/crawling/docs/crawlers-fetchers/google-common-crawlers), [Perplexity](https://docs.perplexity.ai/docs/resources/perplexity-crawlers), [Apple](https://support.apple.com/en-us/119829), [Meta](https://developers.facebook.com/docs/sharing/webmasters/web-crawlers). OpenAI and Perplexity publish IP lists (`openai.com/searchbot.json`, `openai.com/gptbot.json`, `openai.com/chatgpt-user.json`, `perplexity.ai/perplexitybot.json`, `perplexity.ai/perplexity-user.json`) for allowlisting in a firewall.

## The robots.txt policy

Start from one wildcard group that allows everything, and add named groups only for a deliberate exception such as a training opt-out. An allowlist of named crawlers silently shuts out every search API and new engine that runs its own crawler.

A named group replaces the `*` group for that bot completely. A bot with its own group ignores every `*` rule, so copy any `Disallow` it still needs, like `/admin`, into its group.

The default for a site that wants to be found and cited, with training left on:

```text
User-agent: *
Allow: /
Disallow: /admin/

Sitemap: https://example.com/sitemap.xml
```

The same site with training opted out. Search and user fetches still fall through to `*`:

```text
User-agent: *
Allow: /
Disallow: /admin/

User-agent: GPTBot
User-agent: ClaudeBot
User-agent: Google-Extended
User-agent: Applebot-Extended
User-agent: meta-externalagent
User-agent: CCBot
Disallow: /

Sitemap: https://example.com/sitemap.xml
```

Training on or off is Jack's call for each site. Being in training data is how a model knows a brand without searching, so opting out trades future brand recall for control of the content. Ask once per site, recommend allowing training for a product or marketing site that wants to be known, and record the answer in the robots.txt itself.

## The second gate: CDN and firewall

robots.txt is a request. A CDN or web application firewall answers before it, and a 403 or challenge page blocks a bot however open the file is.

- **Cloudflare** blocks AI crawlers by default on many newer zones, can prepend its own rules to the served robots.txt, and has an AI Crawl Control page that allows or blocks each bot. Read the robots.txt that is actually served, not the one in the repo, and check the dashboard. This is a dashboard setting Jack changes by hand.
- **Vercel, Netlify, AWS WAF, Akamai and bot-protection services** have similar bot rules. Let verified bots through by the vendor's published IP ranges or the provider's verified-bot list, never by user agent alone, since anyone can send any user agent.
- A throttled bot needs a `429` with `Retry-After`, never a challenge page.
- A robots.txt that times out or returns 5xx makes crawlers treat the whole site as disallowed.

`python3 <skill folder>/scripts/ai_access.py <url>` reads the served robots.txt the way RFC 9309 does (longest match wins, allow wins ties, a named group replaces `*`), then fetches the page with every bot's user agent and flags status codes and challenge pages that differ from a browser's. A block it reports may be an IP check that the real bot would pass, so confirm in the CDN settings or server logs before changing anything.

## Content the bot sees

Most AI fetchers do not run JavaScript. The answer has to be in the HTML the server sends. The **seo** skill owns rendering; the script's visible-text count is a quick check that the page is not an empty shell.
