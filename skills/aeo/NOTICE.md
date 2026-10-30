# Notice

This skill adapts work by others. Each source keeps its license, and the changes are listed below the table.

| Source | Author | License | Used in |
| --- | --- | --- | --- |
| [ai-seo](https://github.com/coreyhaines31/marketingskills/tree/main/skills/ai-seo) in marketingskills, commit `820ad2c` | Corey Haines | [MIT](licenses/MIT.txt) | `SKILL.md` and every file in `references/` |

The ai-seo skill credits further sources that its text carries into this one: Profound's MIT-licensed ai-retrieval-fanout-mapper, ai-search-attribution-planner, ai-prompt-portfolio-builder, ai-answer-accuracy-auditor and ai-citation-mix-strategist skills and their 2026 studies (the fact-family matrix in `references/content.md`, the layers and prompt tracking in `references/measure.md`, the accuracy steps and citation classes in `references/presence.md`), Lily Ray's 2026 study of B2B listicles (`references/presence.md`), and Ora's agent research and the AgentReady spec (`references/agent-readiness.md`).

Facts, not text, come from these primary sources, checked October 2026:

- Crawler names, purposes and robots.txt behavior: [OpenAI](https://developers.openai.com/docs/gptbot), [Anthropic](https://support.claude.com/en/articles/8896518), [Google](https://developers.google.com/crawling/docs/crawlers-fetchers/google-common-crawlers), [Perplexity](https://docs.perplexity.ai/docs/resources/perplexity-crawlers), [Apple](https://support.apple.com/en-us/119829) and [Meta](https://developers.facebook.com/docs/sharing/webmasters/web-crawlers).
- Google's guidance on AI features: [AI features and your website](https://developers.google.com/search/docs/appearance/ai-features) and [Optimizing for generative AI features](https://developers.google.com/search/docs/fundamentals/ai-optimization-guide).
- The llms.txt format: [llmstxt.org](https://llmstxt.org).
- The GEO study: Aggarwal et al., [GEO: Generative Engine Optimization](https://arxiv.org/abs/2311.09735), KDD 2024.
- robots.txt matching in `scripts/ai_access.py`: [RFC 9309](https://www.rfc-editor.org/rfc/rfc9309).

Changes from the sources: rewritten as a numbered audit with completion criteria and a short checklist for every public page, split from SEO so the **seo** skill owns crawling, indexing and markup, and reworded throughout. Crawler facts were checked against each vendor's page and the bot table extended with Apple, Meta and Common Crawl. Claims that conflict with Google's July 2026 guidance were corrected: Search Console now has a generative AI performance report and a per-site AI features setting, and Google ignores llms.txt. The per-method uplift table attributed to the GEO study was replaced with the paper's own headline result. LinkedIn, YouTube, multilingual, commerce, Open Knowledge Format and agent-default material was left out. `scripts/ai_access.py` is new.
