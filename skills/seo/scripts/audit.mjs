const usage = "usage: node audit.mjs <site url> [--max=200] [--googlebot] [--json]";
const args = process.argv.slice(2);
const flag = (name) => args.find((arg) => arg.startsWith(`--${name}=`))?.split("=")[1];
const [start] = args.filter((arg) => !arg.startsWith("--"));
if (!start) {
  console.error(usage);
  process.exit(1);
}

const max = Number(flag("max") ?? 200);
const agent = args.includes("--googlebot")
  ? "Mozilla/5.0 (Linux; Android 6.0.1; Nexus 5X Build/MMB29P) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Mobile Safari/537.36 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)"
  : "Mozilla/5.0 (compatible; seo-audit/1.0)";
const origin = new URL(start).origin;
const findings = [];
const add = (severity, check, detail) => findings.push({ severity, check, detail });

async function get(url) {
  const hops = [];
  let current = url;
  for (let i = 0; i < 10; i++) {
    let res;
    try {
      res = await fetch(current, { redirect: "manual", headers: { "user-agent": agent } });
    } catch (error) {
      return { url, status: 0, hops, error: error.message };
    }
    const location = res.headers.get("location");
    if (res.status >= 300 && res.status < 400 && location) {
      hops.push({ from: current, status: res.status, to: new URL(location, current).href });
      current = new URL(location, current).href;
      continue;
    }
    const type = res.headers.get("content-type") ?? "";
    const body = /html|xml|text/.test(type) ? await res.text() : "";
    return { url, final: current, status: res.status, hops, headers: res.headers, type, body };
  }
  return { url, status: 0, hops, error: "more than 10 redirects" };
}

const attr = (tag, name) => tag.match(new RegExp(`\\s${name}\\s*=\\s*("([^"]*)"|'([^']*)'|([^\\s>]+))`, "i"))?.slice(2).find((v) => v !== undefined);
const tags = (html, name) => html.match(new RegExp(`<${name}\\b[^>]*>`, "gi")) ?? [];
const decode = (s) => s.replace(/&amp;/g, "&").replace(/&quot;/g, '"').replace(/&#39;|&#x27;/g, "'").replace(/&lt;/g, "<").replace(/&gt;/g, ">").replace(/\s+/g, " ").trim();

function parse(html, base) {
  const head = html.match(/<head\b[\s\S]*?<\/head>/i)?.[0] ?? html;
  const metas = tags(head, "meta");
  const meta = (key, value) => metas.find((m) => attr(m, key)?.toLowerCase() === value);
  const text = decode(html.replace(/<(script|style|noscript|template)\b[\s\S]*?<\/\1>/gi, " ").replace(/<[^>]+>/g, " "));
  const jsonld = [...html.matchAll(/<script[^>]+application\/ld\+json[^>]*>([\s\S]*?)<\/script>/gi)].map((m) => {
    try {
      const data = JSON.parse(m[1]);
      const nodes = [data, ...(data["@graph"] ?? [])].flat();
      return nodes.map((n) => n?.["@type"]).filter(Boolean).flat();
    } catch {
      return ["INVALID JSON"];
    }
  }).flat();
  const links = tags(html, "a").map((a) => attr(a, "href")).filter(Boolean).map((href) => {
    try {
      const u = new URL(decode(href), base);
      u.hash = "";
      return u.href;
    } catch {
      return null;
    }
  }).filter(Boolean);
  return {
    title: decode(head.match(/<title[^>]*>([\s\S]*?)<\/title>/i)?.[1] ?? ""),
    description: decode(attr(meta("name", "description") ?? "", "content") ?? ""),
    robots: (attr(meta("name", "robots") ?? "", "content") ?? "") + " " + (attr(meta("name", "googlebot") ?? "", "content") ?? ""),
    canonical: (() => { const l = tags(head, "link").find((t) => attr(t, "rel")?.toLowerCase() === "canonical"); return l ? new URL(attr(l, "href"), base).href : ""; })(),
    lang: attr(tags(html, "html")[0] ?? "", "lang") ?? "",
    viewport: Boolean(meta("name", "viewport")),
    ogImage: Boolean(meta("property", "og:image")),
    h1: tags(html, "h1").length,
    imgNoAlt: tags(html, "img").filter((i) => attr(i, "alt") === undefined).length,
    imgNoSize: tags(html, "img").filter((i) => !attr(i, "width") || !attr(i, "height")).length,
    words: text ? text.split(" ").length : 0,
    jsonld,
    links: [...new Set(links)],
  };
}

const first = await get(start);
if (!first.status) {
  console.error(`Could not fetch ${start}: ${first.error}`);
  process.exit(2);
}
const robots = await get(`${origin}/robots.txt`);
const sitemapUrls = new Set();
if (robots.status !== 200) add("HIGH", "robots.txt", `${origin}/robots.txt returned ${robots.status || robots.error}. Serve one that allows crawling and names the sitemap.`);
else {
  let agents = [];
  let inRules = false;
  for (const raw of robots.body.split("\n")) {
    const line = raw.split("#")[0].trim();
    const [key, ...rest] = line.split(":");
    const value = rest.join(":").trim();
    if (/^user-agent$/i.test(key)) {
      if (inRules) agents = [];
      inRules = false;
      agents.push(value);
    } else if (/^(allow|disallow)$/i.test(key)) {
      inRules = true;
      const forSearch = agents.some((a) => a === "*" || /^googlebot$/i.test(a));
      if (forSearch && /^disallow$/i.test(key) && value === "/") add("HIGH", "robots.txt", `The group for ${agents.join(", ")} has \`Disallow: /\`, which blocks the whole site.`);
    } else if (/^sitemap$/i.test(key)) sitemapUrls.add(value);
  }
  if (!sitemapUrls.size) add("MEDIUM", "robots.txt", "No `Sitemap:` line.");
}
if (!sitemapUrls.size) sitemapUrls.add(`${origin}/sitemap.xml`);

const inSitemap = new Set();
const queue = [...sitemapUrls];
for (let i = 0; i < queue.length && i < 50; i++) {
  const res = await get(queue[i]);
  if (res.status !== 200) {
    add("HIGH", "sitemap", `${queue[i]} returned ${res.status || res.error}.`);
    continue;
  }
  const locs = [...res.body.matchAll(/<loc>\s*([^<]+?)\s*<\/loc>/g)].map((m) => decode(m[1]));
  if (/<sitemapindex/i.test(res.body)) queue.push(...locs);
  else locs.forEach((loc) => inSitemap.add(loc));
  if (locs.some((loc) => !/^https?:\/\//.test(loc))) add("HIGH", "sitemap", `${queue[i]} has relative URLs. Use absolute URLs.`);
}

const pages = new Map();
const linkedFrom = new Map();
const crawl = [new URL(start).href, ...inSitemap];
for (let i = 0; i < crawl.length && pages.size < max; i++) {
  const url = crawl[i];
  if (pages.has(url) || new URL(url).origin !== origin) continue;
  const res = await get(url);
  const page = { ...res, ...(res.status === 200 && !res.hops.length && /html/.test(res.type) ? parse(res.body, res.final) : { links: [] }) };
  if (res.hops.length && res.final && !pages.has(res.final)) crawl.push(res.final);
  page.xRobots = res.headers?.get("x-robots-tag") ?? "";
  pages.set(url, page);
  for (const link of page.links) {
    if (new URL(link).origin !== origin) continue;
    if (!linkedFrom.has(link)) linkedFrom.set(link, new Set());
    linkedFrom.get(link).add(url);
    if (!pages.has(link)) crawl.push(link);
  }
}

const missing = await get(`${origin}/this-page-should-not-exist-${Date.now()}`);
if (missing.status === 200) add("HIGH", "soft 404", `A made-up URL returned 200. Missing pages must return 404 or 410.`);

const grouped = new Map();
const group = (severity, check, url, text) => {
  const key = `${severity}|${check}|${text}`;
  grouped.set(key, [...(grouped.get(key) ?? []), url]);
};
const byTitle = new Map();
const byDescription = new Map();
for (const [url, p] of pages) {
  const from = [...(linkedFrom.get(url) ?? [])].slice(0, 3).join(", ");
  if (p.status === 0) add("HIGH", "fetch", `${url}: ${p.error}`);
  else if (p.status >= 400) add("HIGH", "broken link", `${url} returned ${p.status}${from ? `, linked from ${from}` : ", listed in the sitemap"}.`);
  if (p.hops.length > 1) add("MEDIUM", "redirect chain", `${url} takes ${p.hops.length} hops: ${p.hops.map((h) => `${h.status} ${h.to}`).join(" -> ")}.`);
  if (p.hops.some((h) => h.status === 302 || h.status === 307)) add("LOW", "temporary redirect", `${url} uses ${p.hops.map((h) => h.status).join(", ")}. Use 301 or 308 for a permanent move.`);
  if (p.hops.length && linkedFrom.has(url)) add("LOW", "link to redirect", `${url} redirects, but ${from} links to it. Link to ${p.final}.`);
  if (inSitemap.has(url) && p.hops.length) add("HIGH", "sitemap", `${url} is in the sitemap but redirects to ${p.final}. List the final URL.`);
  if (p.status !== 200 || !("title" in p)) continue;
  const noindex = /noindex|none/i.test(p.robots) || /noindex|none/i.test(p.xRobots);
  if (noindex) add(inSitemap.has(url) ? "HIGH" : "MEDIUM", "noindex", `${url} is noindex${inSitemap.has(url) ? " but listed in the sitemap" : ""}. Confirm it is meant to stay out of search.`);
  if (!p.title) add("HIGH", "title", `${url} has no <title> in the server HTML.`);
  else byTitle.set(p.title, [...(byTitle.get(p.title) ?? []), url]);
  if (!p.description) group("MEDIUM", "description", url, "no meta description");
  else byDescription.set(p.description, [...(byDescription.get(p.description) ?? []), url]);
  if (!p.canonical) group("MEDIUM", "canonical", url, "no canonical link");
  else if (p.canonical !== p.final && !noindex) add("MEDIUM", "canonical", `${url} canonicalizes to ${p.canonical}. Fine for a duplicate, wrong for a page meant to rank.`);
  if (p.h1 !== 1) group("LOW", "h1", url, `${p.h1 ? "more than one" : "no"} <h1> in the server HTML`);
  if (p.words < 150) add("MEDIUM", "server render", `${url} has ${p.words} words in the server HTML. Check the content renders on the server, not only in the browser.`);
  if (!p.lang) group("LOW", "lang", url, "no <html lang>");
  if (!p.viewport) group("MEDIUM", "viewport", url, "no viewport meta");
  if (!p.ogImage) group("LOW", "open graph", url, "no og:image, so shared links show no preview");
  if (p.imgNoAlt) add("MEDIUM", "alt text", `${url} has ${p.imgNoAlt} <img> without an alt attribute.`);
  if (p.imgNoSize) group("LOW", "image size", url, "<img> without width and height, a layout shift risk");
  if (p.jsonld.includes("INVALID JSON")) add("HIGH", "structured data", `${url} has a JSON-LD block that does not parse.`);
  if (!inSitemap.has(url) && !noindex && inSitemap.size) group("LOW", "sitemap", url, "linked and indexable but missing from the sitemap");
  if (inSitemap.has(url) && !linkedFrom.has(url) && url !== new URL(start).href) add("MEDIUM", "orphan", `${url} is in the sitemap but no crawled page links to it.`);
}
for (const [key, urls] of grouped) {
  const [severity, check, text] = key.split("|");
  add(severity, check, `${text[0].toUpperCase()}${text.slice(1)} (${urls.length} ${urls.length === 1 ? "page" : "pages"}): ${urls.slice(0, 5).join(", ")}${urls.length > 5 ? ", ..." : ""}.`);
}
for (const [title, urls] of byTitle) if (urls.length > 1) add("MEDIUM", "duplicate title", `"${title}" on ${urls.length} pages: ${urls.slice(0, 5).join(", ")}.`);
for (const [, urls] of byDescription) if (urls.length > 1) add("LOW", "duplicate description", `Same meta description on ${urls.length} pages: ${urls.slice(0, 5).join(", ")}.`);

const order = { HIGH: 0, MEDIUM: 1, LOW: 2 };
findings.sort((a, b) => order[a.severity] - order[b.severity] || a.check.localeCompare(b.check));
const summary = { site: origin, crawled: pages.size, inSitemap: inSitemap.size, findings: findings.length };
if (args.includes("--json")) {
  const rows = [...pages].map(([url, p]) => ({ url, status: p.status, hops: p.hops.length, title: p.title, description: p.description, canonical: p.canonical, robots: `${p.robots ?? ""} ${p.xRobots}`.trim(), h1: p.h1, words: p.words, jsonld: p.jsonld }));
  console.log(JSON.stringify({ summary, findings, pages: rows }, null, 2));
} else {
  console.log(`# SEO audit of ${origin}\n\nCrawled ${pages.size} pages (limit ${max}), ${inSitemap.size} URLs in the sitemap, ${findings.length} findings. This reads the server HTML only, as a crawler first sees it.\n`);
  console.log("| Severity | Check | Detail |\n| --- | --- | --- |");
  for (const f of findings) console.log(`| ${f.severity} | ${f.check} | ${f.detail.replace(/\|/g, "\\|")} |`);
}
process.exit(findings.some((f) => f.severity === "HIGH") ? 1 : 0);
