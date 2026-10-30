# Notice

This skill adapts work by others. Each source keeps its license, and the changes are listed below the table.

| Source | Author | License | Used in |
| --- | --- | --- | --- |
| [web-quality-skills](https://github.com/addyosmani/web-quality-skills) | Addy Osmani | [MIT](licenses/MIT.txt) | `references/performance.md`, from core-web-vitals; the audit order in `SKILL.md`, and `references/structured-data.md`, from seo |
| [marketingskills](https://github.com/coreyhaines31/marketingskills) | Corey Haines | [MIT](licenses/MIT.txt) | The title patterns in `references/on-page.md`, the new page checklist in `SKILL.md`, and the intent, cannibalization and after-launch sections of `references/content.md`, from seo-audit |
| [claude-seo](https://github.com/AgriciDaniel/claude-seo) | agricidaniel | [MIT](licenses/MIT.txt) | The rendering and pagination rules in `references/technical.md`, from seo-technical |
| [TanStack Start docs](https://tanstack.com/start/latest/docs/framework/react/guide/seo) | Tanner Linsley and contributors | [MIT](licenses/MIT.txt) | The code in `references/stack.md` |
| [Google Search Central](https://developers.google.com/search/docs) | Google | [CC BY 4.0](licenses/CC-BY-4.0.txt) | Facts throughout, checked against the docs in October 2026: rendering, status codes, robots.txt, canonicals, sitemaps, the search gallery, AI features, helpful content and spam policies |
| [web.dev](https://web.dev/articles/vitals) | Google | [CC BY 4.0](licenses/CC-BY-4.0.txt) | The Core Web Vitals thresholds in `references/performance.md` |
| [Cloudflare docs](https://developers.cloudflare.com/) | Cloudflare | [CC BY 4.0](licenses/CC-BY-4.0.txt) | Managed robots.txt and preview deployment behavior in `references/stack.md` |

Changes from the sources: condensed and reworded into one ladder, checked against Google's current documentation (FAQ rich results are marked retired, and one H1 is a convention, not a ranking rule), rewritten for TanStack Start, Cloudflare and shadcn/ui, and extended with `scripts/audit.mjs` and the steps only Jack can take.
