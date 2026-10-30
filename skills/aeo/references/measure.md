# Measuring AI visibility

AI answers are non-deterministic and most of their effect never shows up as a referral click. Measure in layers, report rates with sample sizes, and say whether a result is an observation, an association or a causal finding.

## Layers

| Layer | What it captures | Where it comes from |
| --- | --- | --- |
| Exposure | Retrieved, cited, mentioned, recommended, and the framing (see [presence.md](presence.md)) | Prompt tracking |
| Immediate | AI referral sessions and their landing pages | Analytics |
| Delayed | Branded search, direct visits, return visits | Search Console, analytics |
| Outcome | Signups, leads, revenue | CRM, billing |

Rising exposure does not prove rising revenue. Report each layer on its own.

## Built-in reports

- **Google Search Console**: the Search Generative AI performance report under Performance shows impressions and pages in AI Overviews, AI Mode and Discover, by country, device and date. No queries or clicks. AI clicks also count in the normal Web performance numbers.
- **Bing Webmaster Tools**: the AI Performance report shows citations in Copilot and Bing's AI answers, and the grounding queries behind them.
- **Server logs or CDN analytics**: hits from each bot in [crawlers.md](crawlers.md). Rising `OAI-SearchBot` or `Claude-SearchBot` crawls after a fix confirm access works. `ChatGPT-User`, `Claude-User` and `Perplexity-User` hits are real people's questions reaching the site.

## Referral traffic

Group AI referrers into one analytics channel, for example a GA4 custom channel group matching the source against:

```text
chatgpt\.com|chat\.openai\.com|perplexity\.ai|claude\.ai|gemini\.google\.com|copilot\.microsoft\.com|bing\.com/chat|meta\.ai|you\.com|phind\.com
```

ChatGPT adds `utm_source=chatgpt.com` to many links. AI Overview clicks arrive as ordinary Google organic traffic and cannot be split out in analytics. Expect this channel to undercount by a lot: in Profound's 2026 data, over 97% of visits that followed an AI recommendation carried no AI referrer, and fewer than half came within 24 hours. Watch branded search and direct visits over 7-day windows after a known change.

Add an AI option to any "How did you hear about us?" field, with a "What did you ask?" follow-up. Buyers hand over the real prompts to track.

## Prompt tracking

1. **Write down the decision** the numbers will drive, such as "are we on the shortlist for small EU agencies?"
2. **Collect prompts from real demand**: what buyers report asking, sales calls, support tickets, community threads, then search terms rewritten as someone would type them into a chat box. Weight by business value, since a citation for a glossary question rarely sells anything.
3. **Cover the intent families**: category discovery, problem research, comparisons and alternatives, "best for" a segment, trust and risk ("is X legit", "does X have SOC 2"), price and compatibility, setup and troubleshooting.
4. **Keep three cohorts**: a stable core that only changes through versioning, an exploratory set that rotates, and controls (the brand name, where the brand should always appear, and an unrelated category, where it never should). If the controls move, the engine or the tool changed.
5. **Run each prompt several times.** For a small set of 10 to 20 prompts, run each 3 to 5 times per engine and report the rate with its sample size, like "cited 3/5". For hundreds of prompts, once a day is enough.
6. **Score by topic, not by prompt.** Group prompts into buying topics and count appearances across runs for the brand and each competitor. Start on the topic where a competitor shows up most and the brand least.
7. **For a lost topic**, open the pages the engine cited, check whether an existing page should have won and why it did not, rule out access and indexing, then fix that page before writing a new one. Rerun the same portfolio once the change is crawled.
8. **Multi-turn**: for buying decisions, run an opening prompt and two or three realistic follow-ups in one session ("which of these work for a team of 5?", "what do users complain about?") and note the turn where the brand drops off the shortlist.

Version the portfolio, log every change with a date and reason, and only compare periods on the prompts they share.

Tools that automate this include Profound, Peec AI, Otterly, ZipTie, Ahrefs Brand Radar and Semrush. Check what each one samples before comparing their numbers. Buying one is Jack's call.

## Evaluation

Pick the strongest design the situation allows and name it in the report: a holdout of comparable untouched pages (strongest), a matched comparison, an interrupted time series around one change date, or a plain before and after on a stable cohort (weakest). List the confounders first: campaigns, launches, press, seasonality, price changes and engine updates.
