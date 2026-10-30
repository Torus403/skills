# Content that gets cited

AI engines quote passages, not pages. A page gets cited when one passage answers the question on its own, with a fact the engine can trust. Write for people first: Google says AI features need no special writing style, and the same structure that helps a skimming reader helps an engine lift the answer.

## Answer first

- Open each page and each section with the direct answer in one or two sentences, then the detail. A reader who stops after the first paragraph has the answer.
- Write headings the way people ask: "How long does setup take?", not "Implementation".
- Make each key passage self-contained. Name the subject instead of "it" or "this", so the passage still makes sense when quoted alone. Around 40 to 60 words is a good length for the core answer.
- One idea per paragraph. Lists for steps, tables for comparisons, prose for reasoning.
- Keep the page as long as the topic needs. Splitting a page into fragments for AI is a pattern Google warns against.

## Evidence

The GEO study (Aggarwal et al., [arXiv 2311.09735](https://arxiv.org/abs/2311.09735), KDD 2024) tested rewrites against a generative engine. Citing sources, adding quotations and adding statistics raised a page's visibility in answers by up to about 40%, and helped lower-ranked pages most. Keyword stuffing did not help. It is one benchmark on one engine, so read it as direction, not a forecast.

- **Specific numbers with a source and a date.** "Setup takes 4 to 8 weeks for a 50-person team (our 2026 customer survey, n=212)" beats "fast setup".
- **Named sources.** "According to [source]" with a link to the primary document, not a summary of it.
- **Quotations from named people** with their role.
- **Original data.** Research, benchmarks and first-hand experience that no other page has. Google calls the opposite "commodity content" and ranks it down.
- **A named author** with a real bio, and a visible "Updated" date that changes only when the content does.
- **Facts as text.** Prices, limits, ratings and customer names in the HTML, not only in an image, a widget or JSON-LD.

## Patterns

Use the pattern that matches how the question is asked.

**Definition** for "what is X":

```markdown
## What is [term]?

[Term] is [one-sentence definition]. [One or two sentences on what sets it apart]. [Why it matters or where it is used].
```

**Steps** for "how to X":

```markdown
## How to [goal]

[One sentence on what the process gets you.]

1. **[Step]**: [one or two sentences].
2. **[Step]**: [one or two sentences].
```

**Comparison table** for "X vs Y" and "alternatives to X". Be fair: name what the competitor does well, then where this product goes further. Engines discount one-sided comparisons.

```markdown
## [A] vs [B]

| | [A] | [B] |
| --- | --- | --- |
| [Criterion] | [Value] | [Value] |
| Best for | [Use case] | [Use case] |

**Bottom line**: [one or two sentences on who should pick which].
```

**FAQ** for the questions buyers actually ask (from support tickets, sales calls and "People also ask"). Answer in the first sentence, then two or three sentences of context.

**Pros and cons** for "is X worth it": a balanced list and a one-line verdict.

**Statistic or claim** for any fact worth quoting: claim, then source and number, then what it means.

## Query fan-out and fact families

Engines rewrite one question into several background searches and combine the results. Google calls this query fan-out and says not to build pages for each variant, which breaks its scaled content abuse policy. Plan around the stable facts underneath the searches instead.

1. Pick a question family that matters to the business, with its audience and buying stage.
2. List the background searches it is likely to trigger. Mark each one observed (from a tool or from the engine's visible search steps) or inferred.
3. Break them into fact families: category terms, sub-questions, comparison criteria, constraints like price, compatibility and location, and the evidence that settles each.
4. Give every fact family one owning page:

| Fact family | Observed or inferred | What the buyer needs | Best source today | Our owning page | Gap |
| --- | --- | --- | --- | --- | --- |
| Price for 10 seats | Observed | Monthly cost, annual discount | A 2025 review site | /pricing | Per-seat price not in text |
| SOC 2 status | Inferred | Report type and date | None | /security | Says "enterprise-grade", no report type |

5. Fix or merge an existing page before creating a new one. One strong page can own several fact families.

## By page type

- **Home and product pages**: what it is, who it is for, and what it costs in the first screen of text. Specific metrics over adjectives.
- **Pricing**: every plan, price, limit and billing rule as text on one public page. Hidden pricing makes an engine answer from someone else's stale page.
- **Docs and help**: numbered steps, fenced code blocks tagged with the language, prerequisites and expected results. Agents read docs more than any other page type.
- **Blog posts**: one question per post, answered in the opening, with original data and a named author.
- **Segment and industry pages**: one per segment the product really serves, each with real segment-specific detail. Pages that only swap the industry name are scaled content.
- **Local and shops**: keep Google Business Profile and Merchant Center feeds complete and current. Google's AI features answer local and product questions from them.

## Domain signals

- **Technical**: exact terms, version numbers and dates, links to official docs, code examples.
- **Health**: peer-reviewed sources, the reviewer's credentials, a "last reviewed" date.
- **Finance and legal**: the regulator or statute, the jurisdiction, and a clear note on when to ask a professional.
- **Business**: case studies with measured results and timeframes.
