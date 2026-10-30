# Structured data

Rung 3. JSON-LD that tells search engines what the page is, in schema.org terms. It can earn a rich result, but Google decides whether to show one, so markup is never a ranking promise.

## Rules

- JSON-LD in a `<script type="application/ld+json">`, in the server HTML.
- Describe only what the page visibly shows. Marking up content a reader cannot see, or a claim the page does not make, breaks Google's policy and can earn a manual action.
- Use the most specific type that fits: `BlogPosting` over `Article`, `SoftwareApplication` over `Product` for an app.
- Absolute URLs, and stable `@id` values like `https://acme.com/#organization` so pages can reference one entity.
- One `@graph` per page is easier to keep consistent than several scripts.
- Build the markup from the same data that renders the page, so the two cannot drift.

## What Google still shows

Google's search gallery lists the features it supports. Before adding a type for a rich result, check it is still there. As of October 2026:

- **Shown:** Article, Breadcrumb, Product, Review snippet, Organization, Local business, Event, Video, Recipe, Job posting, Course list, Discussion forum, Q&A, Profile page, Software app, Dataset, Vacation rental, Subscription and paywalled content, and a few more.
- **Retired:** FAQ rich results stopped showing in May 2026. HowTo rich results ended in 2023. FAQPage markup earns no Google rich result. Keep a visible FAQ section when readers need one, and its markup only if it is accurate, since other consumers may still read it.
- **Self-serving reviews** of a business on its own site do not get review stars.

## Site-wide, on the homepage

```json
{
  "@context": "https://schema.org",
  "@graph": [
    {
      "@type": "WebSite",
      "@id": "https://acme.com/#website",
      "url": "https://acme.com/",
      "name": "Acme",
      "alternateName": "Acme Invoicing",
      "publisher": { "@id": "https://acme.com/#organization" }
    },
    {
      "@type": "Organization",
      "@id": "https://acme.com/#organization",
      "name": "Acme",
      "url": "https://acme.com/",
      "logo": "https://acme.com/logo-512.png",
      "sameAs": ["https://github.com/acme", "https://www.linkedin.com/company/acme"]
    }
  ]
}
```

`WebSite` with `name` sets the site name Google shows above results. `sameAs` lists the organization's real profiles, which Jack supplies.

## Articles and posts

```json
{
  "@context": "https://schema.org",
  "@type": "BlogPosting",
  "headline": "How to Price a Freelance Project",
  "description": "Three pricing models, with the maths for each.",
  "image": ["https://acme.com/blog/pricing/cover-1200x630.png"],
  "datePublished": "2026-10-01T09:00:00Z",
  "dateModified": "2026-10-20T14:30:00Z",
  "author": {
    "@type": "Person",
    "name": "Jane Doe",
    "url": "https://acme.com/authors/jane-doe"
  },
  "publisher": { "@id": "https://acme.com/#organization" }
}
```

- `author` is a real person, with `name` holding only the name and `url` pointing at their author page.
- `dateModified` changes only when the content does.

## Author pages

The author page shows the person's name, photo, bio and links, and carries `ProfilePage` markup:

```json
{
  "@context": "https://schema.org",
  "@type": "ProfilePage",
  "mainEntity": {
    "@type": "Person",
    "name": "Jane Doe",
    "url": "https://acme.com/authors/jane-doe",
    "image": "https://acme.com/authors/jane-doe.jpg",
    "jobTitle": "Founder",
    "description": "Jane has run a freelance design studio since 2014.",
    "sameAs": ["https://www.linkedin.com/in/janedoe"]
  }
}
```

## Breadcrumbs

Mirror the visible breadcrumb trail. Omit `item` on the last entry, the current page.

```json
{
  "@context": "https://schema.org",
  "@type": "BreadcrumbList",
  "itemListElement": [
    { "@type": "ListItem", "position": 1, "name": "Templates", "item": "https://acme.com/templates" },
    { "@type": "ListItem", "position": 2, "name": "Invoice template" }
  ]
}
```

## Other common types

| Page | Type | Must match on the page |
| --- | --- | --- |
| Product for sale | `Product` with `Offer` | Price, currency, availability |
| Product reviews | `Review`, `AggregateRating` | Real reviews from real customers, shown on the page |
| App or SaaS product | `SoftwareApplication` | Name, category, operating system, price |
| Physical business | `LocalBusiness` subtype | Name, address and phone, the same everywhere they appear |
| Event | `Event` | Date, place or online status |
| Video | `VideoObject` | Thumbnail, upload date, the video on the page |
| Job opening | `JobPosting` | Title, date, location, the full description |

Check the required and recommended properties on the type's Google documentation page before shipping it.

## Checks

- [ ] Every JSON-LD block parses (the audit flags those that do not)
- [ ] The markup is in the server HTML, not added only by client JavaScript
- [ ] Every value matches what the page shows
- [ ] The Rich Results Test passes for each template, run on the live URL or the pasted HTML
- [ ] No review, rating, author or statistic in the markup that Jack did not supply
