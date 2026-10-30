---
name: aeo
description: Get a website found, cited and recommended by AI answer engines (ChatGPT, Google AI Overviews and AI Mode, Claude, Perplexity, Copilot, Gemini). Use whenever you build or audit a public website, landing page, blog or docs, and whenever the work touches AEO, GEO, AI search visibility, AI crawlers, robots.txt for AI bots, llms.txt or AI citations.
license: MIT, see NOTICE.md
---

# AEO

Answer engine optimization: getting a site retrieved, cited and recommended when people ask ChatGPT, Google, Claude, Perplexity or Copilot instead of clicking through search results. Sources and licenses are in [NOTICE.md](NOTICE.md).

AEO sits on top of SEO. Google says its AI features use the same index and ranking systems as Search, and the other engines search their own or Bing's index, so a page that is not crawlable and indexed is never cited. The **seo** skill owns crawling, rendering, indexing, sitemaps, canonicals, speed and structured data. This skill adds what is specific to AI engines: their bots, answer-shaped content, evidence, entity and consensus signals, agent-readable files, and measuring citations.

## Every public page

Apply these whenever you build or change a public page, with no audit needed:

- The **seo** skill's essentials hold: server-rendered HTML, indexable, one `h1`, a unique title and description.
- The page answers its main question in the first two sentences, in plain text in the initial HTML.
- Headings read like the questions people ask. Each key passage makes sense when quoted on its own.
- Claims carry specific numbers, named sources and dates. Prices, limits and contact details are text, not images or widgets.
- An author and an "Updated" date on articles and docs.
- robots.txt allows search bots and user fetchers through the `*` group, per [references/crawlers.md](references/crawlers.md).

## Audit or improve a site

1. **SEO first.** Run the **seo** skill on the site, or read its latest report in the Jack folder. Done when indexing and rendering problems are fixed or listed, because nothing below works on a page engines cannot index.
2. **Access.** Run `python3 <skill folder>/scripts/ai_access.py <url>` on the home page and one page of each type (product, pricing, docs, article). Fix robots.txt and firewall rules per [references/crawlers.md](references/crawlers.md). Ask Jack whether each site allows training bots, with allowing as the recommendation for a site that wants to be known. Done when every search bot and user fetcher is allowed and gets the same status and text as a browser, and the training bots match Jack's answer.
3. **Baseline.** Write 10 to 20 prompts buyers would really ask, across the intent families in [references/measure.md](references/measure.md). Run each 3 to 5 times in ChatGPT, Perplexity and Google, and in any other engine that matters, and record for each: cited or not, mentioned or not, recommended or not, who was cited instead, and which page. Without browser access to those engines, write the prompt list and hand the runs to Jack. Done when every prompt has a result or is on Jack's list.
4. **Content.** For each page that should own an answer, apply [references/content.md](references/content.md): answer first, self-contained passages, evidence, facts as text, one owning page per fact family. Fix existing pages before writing new ones. List each rewrite with the before and after, and apply it once Jack approves, since visible copy is Jack's call. Done when every prompt from step 3 maps to a page that answers it in its first passage, or to a page in the plan.
5. **Entity and presence.** Check the `Organization` data and every third-party profile per [references/presence.md](references/presence.md), and classify the sources the engines cited in step 3. Done when the brand is described the same way everywhere and the off-site gaps are listed with the pages to target.
6. **Agent-readable.** Apply the must-haves in [references/agent-readiness.md](references/agent-readiness.md) and put pricing on a public page as text. Add llms.txt for docs and developer products, where coding agents read it, and elsewhere only when Jack asks, since no major engine documents using it. Done when the must-haves pass.
7. **Engine extras.** Go through [references/platforms.md](references/platforms.md) for the engines that matter to this audience. Done when each one's setup is done or on Jack's list.
8. **Report** to the Jack folder (per the Files you write in a repo section of [`../jack-mode/references/harness.md`](../jack-mode/references/harness.md)) as `aeo/report.md`: the baseline table, what changed, what is left, the measurement plan from [references/measure.md](references/measure.md), and a **Needs Jack** list from the section below.

When an engine states something wrong about the brand, follow the accuracy steps in [references/presence.md](references/presence.md).

## Things only Jack can do

Accounts, dashboards and outreach need Jack's logins and judgement. Search Console, Bing Webmaster Tools, Cloudflare and Business Profile setup already live in the **seo** skill's [owner tasks](../seo/references/owner-tasks.md). Add the AI-specific items that apply, prepare everything around them, and walk Jack through them with the **wizard** skill:

- **Training bots.** Allow or block them for each site. Prepare: what the served robots.txt and Cloudflare's AI Crawl Control allow now, and the rules for each answer.
- **Google's AI features setting.** Confirm the per-site setting in Search Console that excludes the site from AI Overviews and AI Mode is off.
- **AI reports.** Open the Search Generative AI report in Search Console and the AI Performance report in Bing Webmaster Tools, and share them monthly.
- **IndexNow.** Turn it on where the host or a dashboard setting controls it. Prepare: the key file and the submit call if the repo can do it.
- **Profiles.** Claim and complete G2, Capterra, LinkedIn, Crunchbase, app store and partner listings with the same description. Prepare: the canonical name, one-line description, category and segment.
- **Earned presence.** Ask customers for reviews, pitch press and analysts, and take part in communities under a real name. Prepare: the target list from step 5 and draft outreach.
- **Prompt runs and tools.** Run the baseline prompts when no agent can reach the engines, and decide whether to pay for a tracking tool. Prepare: the prompt sheet.

Never invent what only Jack can supply: a review, a quote, a statistic, a customer name. Leave a visible placeholder and list it.

## Guardrails

Google lists these as useless or harmful, and the other engines discount them too:

- One version of each page, written for people. No hidden or separate copy for AI.
- Pages at the length the topic needs, not chopped into fragments.
- One owning page per topic, never a page per query variant, which is scaled content abuse.
- Real evidence and real mentions only: no invented statistics, fake reviews, paid or astroturfed mentions, or self-written Wikipedia entries.
- Structured data that matches the visible text, used as context, not as a promised citation boost.
- Claims about engines checked against the vendor's own page, with dates. Third-party "ranking factors" and vendor statistics are hypotheses until the baseline confirms them.
