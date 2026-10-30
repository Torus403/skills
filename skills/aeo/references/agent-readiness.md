# Agent-readable sites

AI agents now visit sites for people: they read, compare and sometimes sign up or buy. They see a page through its raw HTML, a screenshot, or the accessibility tree. A site that works for them works for answer engines too.

Google Search ignores llms.txt and Markdown copies, so they neither help nor hurt there, and no other major engine documents using them. Coding agents and AI tools do fetch them, mostly for docs. Build the HTML right first.

## Must have

These are the checks agents fail on most, and the ones the AgentReady spec ([agentready.org](https://agentready.org), October 2026) marks as required:

- **Agents get through.** robots.txt and the CDN or firewall let search bots and user fetchers in. See [crawlers.md](crawlers.md).
- **The answer is in the initial HTML.** Most agents never run JavaScript. If the content appears only after hydration, they see nothing and answer from other people's pages.
- **Real status codes.** A missing page returns 404 or redirects. A single-page app that returns 200 for every path makes dead links look live.

## Should have

- **Semantic HTML and a clean accessibility tree**: `main`, `nav`, `article`, real `button` and `a` elements, one `h1`, labelled form fields, alt text. Agents lean on the same structure screen readers do.
- **Pricing, limits and contact details as text** on public pages. In Ora's 2026 agent study, answers about pricing were right 60% of the time when the agent could read the site's own pages and 37% when it could not.
- **Facts visible, not only in JSON-LD.** Many agents read the text and drop `<script>` blocks, so repeat every critical fact on the page.
- **Docs that answer**, linked from the home page, with fenced code blocks tagged with their language. Docs were the page agents read most.
- **Every discovery file linked** from pages agents already read (footer, `<link>` in the head). Agents found llms.txt and similar files through links far more often than by guessing the path.
- **High-intent actions that work without JavaScript-only flows**: sign up, book a demo, contact, with labelled fields and a confirmation the agent can read.

## llms.txt

A Markdown file at `/llms.txt` that tells a language model what the site is and where the important pages are. The spec is at [llmstxt.org](https://llmstxt.org). The format, in order:

1. An H1 with the site or project name. The only required part.
2. A blockquote with a one-paragraph summary.
3. Optional paragraphs or lists with more detail, but no headings.
4. H2 sections that each hold a list of links: `- [Name](url): optional note`.
5. An H2 named `Optional` for links an agent can skip when it is short on context.

```markdown
# Acme

> Acme is invoicing software for freelancers in the EU. Plans start at €9 a month.

Acme handles VAT for every EU country and exports to the main accounting tools.

## Product

- [Pricing](https://acme.example/pricing.md): plans, limits and billing rules
- [Features](https://acme.example/features.md)

## Docs

- [Quickstart](https://acme.example/docs/quickstart.md)
- [API reference](https://acme.example/docs/api.md)

## Optional

- [Changelog](https://acme.example/changelog.md)
```

Generate it from the same source as the sitemap so it never goes stale, and link it from the footer. A `llms-full.txt` with the full text of the key pages in one file is a common companion.

## Markdown copies

The llms.txt convention puts a Markdown version of a page at the same URL with `.md` added (`/pricing` becomes `/pricing.md`, a directory becomes `/index.html.md`). Advertise it with `<link rel="alternate" type="text/markdown" href="/pricing.md">` in the head or the same relation in an HTTP `Link` header. A server can instead answer `Accept: text/markdown` with Markdown at the same URL and send `Vary: Accept`. In Ora's controlled tests, Markdown did not change whether agents finished their task, so this comes after the HTML works.

## Acting, not just reading

For a product that agents should be able to use, not only read about:

- A public API with an OpenAPI description, self-serve API keys, and OAuth metadata under `/.well-known` for delegated access.
- An MCP server or a CLI, whichever fits how the product is used.
- WebMCP, an early draft that lets a page declare its forms as tools with input schemas. Treat it as experimental.
- A public `SKILL.md` for the product, linked from llms.txt, that tells an agent how to set it up or buy it: pricing as text and a prefilled checkout or signup link the server validates and re-prices. Keep it honest: recommend what fits the user's goal, and never push an upsell, which agent platforms treat as prompt injection.

## Checkers

Free tools score a site against these checks: `npx is-agentic <domain>` (Vercel and Ora), Frase's agent readiness checker, and `npx afdocs check <docs-url>` (Fern) for docs. They are vendor tools; the failed checks are the useful part. Run one before and after the work.
