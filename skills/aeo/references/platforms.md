# Engine by engine

Every engine needs the same three things: the page is in the index it searches, its bots can fetch the page, and a passage answers the question. Past that, each one leans differently.

Weigh evidence in this order: the vendor's own documentation, then controlled experiments, then large observational datasets (mostly from vendors selling tracking tools), then practitioner reports. Follow the documentation for eligibility and crawler controls, and treat the rest as hypotheses to test with the measurement in [measure.md](measure.md). Every number here is a dated snapshot.

## Google AI Overviews and AI Mode

Documented ([AI features](https://developers.google.com/search/docs/appearance/ai-features), [optimizing for generative AI](https://developers.google.com/search/docs/fundamentals/ai-optimization-guide), July 2026):

- A page is eligible when it is indexed and can show with a snippet. There are no extra technical requirements, files, markup or schema.
- Google's own words: optimizing for generative AI search "is optimizing for the search experience, and thus still SEO." So the **seo** skill is the whole technical job here.
- What helps: non-commodity content with first-hand experience, clear headings and paragraphs, good images and video, semantic HTML, crawlable JavaScript, good page experience, little duplicate content, and complete Merchant Center and Business Profile data.
- Controls: `nosnippet`, `data-nosnippet`, `max-snippet` and `noindex` limit what shows. Search Console has a per-site setting that opts the site out of AI features entirely; check it is off.
- Measure with the Search Generative AI performance report in Search Console: impressions and pages in AI Overviews, AI Mode and Discover, with no query or click data.

## ChatGPT

Documented: ChatGPT search uses `OAI-SearchBot`. Allow it, and a site opted out shows only as a bare link. OpenAI does not document its search backend. Practitioners widely report Bing results feeding it, so Bing indexing (below) is a cheap hedge.

Observed (vendor research, 2025 to 2026): referring domains correlated most strongly with citation in SE Ranking's study of 129,000 domains, recently updated pages were cited more, and pages whose substance matched ChatGPT's own answer were cited most. ChatGPT's 2026 retrieval updates moved citations away from listicles and comparison roundups toward official first-party pages, and nearly removed Reddit as a source. Expect more shifts.

## Microsoft Copilot and Bing

Copilot answers from Bing's index.

- Verify the site in Bing Webmaster Tools and submit the sitemap. Many sites only ever set up Google.
- Use IndexNow to push new and changed URLs to Bing and other engines within minutes. Many hosts and CMS plugins support it.
- Bing Webmaster Tools has an AI Performance report: how often pages are cited in Copilot and Bing's AI answers, and the grounding queries Bing ran to find them. Grounding queries are the engine's rewrite of the user's question, which shows what to answer.

## Perplexity

Documented: `PerplexityBot` builds the index and is not used for training. Allow it.

Observed: Perplexity always shows its sources, favors fresh and well-structured pages, and is a fast way to see whether a passage is quotable. Practitioners report public PDFs and FAQ-structured pages doing well there.

## Claude

Documented: `Claude-SearchBot` indexes for search and `Claude-User` fetches for users. Allow both.

Anthropic does not document which search provider Claude's web search uses. Practitioner reports point at Brave Search, so check the site shows up at search.brave.com and submit missing pages at search.brave.com/submit-url. Claude cites sparingly and favors precise, well-sourced facts.

## Gemini

Gemini apps ground on Google Search and the Knowledge Graph. `Google-Extended` controls Gemini training and grounding use, not Search. A correct Knowledge Graph entry (driven by consistent `Organization` data, a Wikipedia or Wikidata entry where notable, and matching profiles) helps it describe the brand right.

## Meta AI

Allow `meta-webindexer`, which Meta says lets Meta AI cite and link the site. Meta does not document how it picks sources, so test with real prompts and log the date.

## Apple

Allow `Applebot` for Siri, Spotlight and Safari suggestions. `Applebot-Extended` only controls training.

## Where to start

1. Google, because AI Overviews reach the most people and it is the same work as SEO.
2. ChatGPT, through `OAI-SearchBot`, Bing indexing, fresh first-party pages and earned links.
3. Perplexity and Copilot, which mostly follow from the first two plus Bing Webmaster Tools.
4. Claude, Gemini apps, Meta AI and Apple, through bot access and the shared fundamentals, unless the audience lives there.
