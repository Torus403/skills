# Steps that need Jack

These need Jack's accounts, identity or relationships. Do everything around them first, then build a wizard with the **wizard** skill, one stage per item that applies, and list each item under **Needs Jack** in the report with what you prepared. Account screens change, so each stage names the goal and the menu, and Jack follows the current screen.

## Before launch

1. **AI crawler policy.** Decide which AI crawlers may fetch the site, with the table in [technical.md](technical.md). Prepare: what the served robots.txt allows now. Jack sets the policy in Cloudflare's AI crawler settings, and you write any robots.txt rules.
2. **Cloudflare dashboard settings** the repo cannot hold: Always Use HTTPS, the redirect rules, Bulk Redirects for `*.pages.dev`, Image Transformations, Crawler Hints and Web Analytics. Prepare: the exact rules, and a Terraform or API version if the project manages Cloudflare as code.
3. **Author details.** For each byline: name, photo, a short bio, credentials, and profile links. Prepare: the author page template with placeholders.
4. **Proof.** Real testimonials, reviews, customer logos, case studies and statistics, with permission to publish. Prepare: the slots, each marked as missing.

## At launch

5. **Google Search Console.** Add a Domain property for the domain. Verify it with the DNS TXT record Google shows, added in Cloudflare DNS, or through the Cloudflare option if Search Console offers one. Prepare: the domain and the Cloudflare zone.
6. **Submit the sitemap** in Search Console's Sitemaps report. Prepare: the sitemap URL, after checking it returns 200 and lists only indexable URLs.
7. **Request indexing** with URL Inspection for the homepage and up to ten key pages, once each. Requesting again does not speed anything up. Prepare: the URL list.
8. **Bing Webmaster Tools.** Import the site from Search Console and submit the sitemap. Prepare: the sitemap URL.
9. **Google Business Profile**, only for a business with a physical location or a service area. Name, address and phone match the site exactly. Prepare: those values as they appear on the site.

## After launch

10. **Check indexing** a week later in the Page indexing report, and share any "Crawled, currently not indexed", "Discovered, currently not indexed" or "Duplicate, Google chose different canonical" rows. Each maps to a fix in [technical.md](technical.md) or [content.md](content.md).
11. **Earn links.** Prepare: the list of linkable assets, directories, partners and communities from [content.md](content.md), with draft outreach. Jack sends it and keeps the relationships.
12. **Share Search Console data** monthly, for the striking-distance and click-through work in [content.md](content.md).
