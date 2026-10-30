# TanStack Start, Cloudflare and shadcn/ui

Where Jack's stack decides SEO. Read the framework skills the project installs first; this file covers only what touches crawling and indexing. Check the TanStack Start and Cloudflare docs for the current API before writing code, since both move fast.

## TanStack Start

**Rendering.** Routes render on the server by default. Search for `ssr: false`, `ssr: 'data-only'` and `defaultSsr: false`. On any public route, each one ships crawlers an empty page, so remove it. They belong only on app screens behind a login.

**Prerendering.** Static marketing pages can be prerendered at build time, and the plugin can write the sitemap from the crawl:

```ts
// vite.config.ts
tanstackStart({
  prerender: { enabled: true, crawlLinks: true },
  sitemap: { enabled: true, host: "https://acme.com" },
})
```

**Head tags.** The root shell renders `<HeadContent />` inside `<head>` and `<Scripts />` at the end of `<body>`. Each route sets its own tags in `head()`, from its loader data:

```tsx
export const Route = createFileRoute("/blog/$slug")({
  loader: async ({ params }) => {
    const post = await getPost({ data: params.slug });
    if (!post) throw notFound();
    return { post };
  },
  head: ({ loaderData }) => {
    const url = `${SITE_URL}/blog/${loaderData.post.slug}`;
    return {
      meta: [
        { title: `${loaderData.post.title} | Acme` },
        { name: "description", content: loaderData.post.excerpt },
        { property: "og:title", content: loaderData.post.title },
        { property: "og:image", content: loaderData.post.ogImage },
        { property: "og:url", content: url },
      ],
      links: [{ rel: "canonical", href: url }],
      scripts: [{ type: "application/ld+json", children: JSON.stringify(articleJsonLd(loaderData.post)) }],
    };
  },
  component: PostPage,
});
```

- Keep site-wide defaults (charset, viewport, the site's WebSite and Organization JSON-LD) in the root route's `head()`, and page values in each route. Check the rendered HTML has exactly one `<title>`, one description and one canonical.
- Build every canonical and `og:url` from one `SITE_URL` constant and the route's path, never from the request host, so preview hosts never become canonical.

**404s.** Throw `notFound()` from a loader when the record does not exist, and render a helpful `notFoundComponent`. Then check the status with `curl -sI <url>`. If a missing page answers 200, set the status with `setResponseStatus(404)` on the server.

**robots.txt and the sitemap.** A static file in `public/` works for a fixed site. For content from a database, use a server route that builds the file per request, cached at the edge:

```ts
// src/routes/sitemap[.]xml.ts
export const Route = createFileRoute("/sitemap.xml")({
  server: {
    handlers: {
      GET: async () => {
        const posts = await listPublishedPosts();
        const urls = [
          `<url><loc>${SITE_URL}/</loc></url>`,
          ...posts.map((p) => `<url><loc>${SITE_URL}/blog/${p.slug}</loc><lastmod>${p.updatedAt.toISOString()}</lastmod></url>`),
        ];
        return new Response(`<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">${urls.join("")}</urlset>`, {
          headers: { "content-type": "application/xml", "cache-control": "public, max-age=3600" },
        });
      },
    },
  },
});
```

`robots[.]txt.ts` follows the same shape, and can send `Disallow: /` with `noindex` headers on every host except production.

**Links.** `<Link to>` renders a real `<a href>`, so use it for every navigation. `navigate()` in an `onClick` is for after an action, like a form submit, never for a link.

## Cloudflare

- **One host.** Serve production on the custom domain. Set `workers_dev = false` and `preview_urls = false` in the Wrangler config once it is live, or make those hosts redirect or send `noindex`. Pages preview deployments already send `X-Robots-Tag: noindex`; the production `*.pages.dev` host does not, so redirect it with a Bulk Redirect.
- **One URL form.** Turn on Always Use HTTPS, and add one Redirect Rule for `www` to apex (or the reverse) and one for the trailing slash policy, each a single 301.
- **Bots.** Bot Fight Mode, the WAF and rate limits must not challenge verified bots like Googlebot and Bingbot. Check Security Events for challenges served to them after any rule change.
- **AI crawlers.** Cloudflare's AI crawler settings can prepend rules to robots.txt and block crawlers at the edge. `curl https://<domain>/robots.txt` shows what crawlers actually get. Which AI crawlers to allow is Jack's call, in [owner-tasks.md](owner-tasks.md).
- **Headers.** Transform Rules can add `X-Robots-Tag`. Check `curl -sI` on production for a stray `noindex`.
- **Caching.** Cache prerendered HTML at the edge, and static assets with `cache-control: public, max-age=31536000, immutable` and hashed file names. Fast TTFB is most of a good LCP.
- **Images.** Image Transformations resize and convert on request with `/cdn-cgi/image/width=800,format=auto/<path>`.
- **Measurement.** Cloudflare Web Analytics reports real-user Core Web Vitals per page.
- **Faster discovery on Bing.** Crawler Hints sends IndexNow pings to Bing and others when content changes. Turning it on is a dashboard step for Jack.

## shadcn/ui

- **Breadcrumb.** Render the trail with shadcn's `Breadcrumb`, using `<BreadcrumbLink asChild><Link to="...">` so each crumb is a real link, and `BreadcrumbPage` for the current page. Generate the BreadcrumbList JSON-LD from the same array.
- **Accordion and Tabs.** Radix unmounts closed `AccordionContent` and inactive `TabsContent`, so their text is missing from the server HTML. For content meant to rank, like an FAQ, render it open, use `forceMount` and hide it with CSS, or use a native `<details>` element.
- **Dialog, Sheet, Popover and HoverCard** render nothing until opened. Keep indexable content out of them.
- **NavigationMenu and DropdownMenu.** Use `asChild` with `<Link>` so menu items are real links, and keep the main navigation's links in the server HTML.
- **Headings.** shadcn components do not set heading levels for the page. `CardTitle` renders a `div`, so place the H1 and the heading order yourself.
