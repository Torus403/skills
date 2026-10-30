# Speed

Rung 4. Core Web Vitals are part of Google's page experience signals. They help, but relevance and content usually outweigh them, so fix crawl, index and content problems first.

## Targets

Good at the 75th percentile of real visits, on mobile and desktop separately:

| Metric | Measures | Good | Poor |
| --- | --- | --- | --- |
| **LCP**, Largest Contentful Paint | When the main content shows | 2.5 s or less | Over 4 s |
| **INP**, Interaction to Next Paint | How fast the page responds to taps, clicks and keys | 200 ms or less | Over 500 ms |
| **CLS**, Cumulative Layout Shift | How much the layout jumps | 0.1 or less | Over 0.25 |

TTFB, the time to the first byte, is not a Core Web Vital, but over 0.8 s it makes a good LCP hard. "Every page loads in under 2 seconds" translates to LCP under 2 s at the 75th percentile on mobile, which beats the target.

## Measure before and after

- **Field data** decides pass or fail: PageSpeed Insights (CrUX) for the URL or the origin, and the Core Web Vitals report in Search Console. New sites with little traffic have no field data yet, so say so.
- **Lab data** diagnoses: Lighthouse, or a Chrome DevTools performance trace on a throttled mobile profile. One lab run is not a field pass.
- **Real user monitoring:** the `web-vitals` library sending to the site's analytics, or Cloudflare Web Analytics, which reports Core Web Vitals per page.
- From source code alone, name likely causes but never claim a metric fails or passes.
- After a fix, re-run the same lab test. Field numbers change only after weeks of new visits.

## LCP

Find the LCP element in the trace first. It is usually the hero image or the first large text block.

- **Fast server response.** Prerender or cache HTML at the edge. Avoid waterfalls of data requests before the first byte.
- **Discoverable early.** The LCP image is an `<img>` in the server HTML, not a CSS background or a client-fetched URL. Give it `fetchpriority="high"` and never `loading="lazy"`. Preload it only when a trace shows it is found late.
- **Small.** AVIF or WebP, sized to the slot with `srcset` and `sizes`.
- **No render blocking.** Keep critical CSS small, defer non-critical JavaScript, and keep third-party scripts out of the `<head>`.
- **Text renders at once.** Self-host fonts, preload only the one or two used above the fold, and use `font-display: swap` or `optional`.
- **Next pages.** Speculation rules can prerender likely next pages in Chromium. Start with `"eagerness": "moderate"`, exclude logout and checkout, and gate analytics on `document.prerendering`.

## CLS

- `width` and `height`, or a CSS `aspect-ratio`, on every image, video, iframe and embed.
- Reserve space for anything that arrives late: banners, consent bars, ads, async components. Prefer overlays to inserting content above what the reader sees.
- Match the fallback font's metrics with `size-adjust`, `ascent-override` and `descent-override`, derived from the real fonts.
- Animate with `transform` and `opacity`, never `top`, `height` or `width`. The **animation-performance** skill covers the rest.

## INP

Read the trace for the slow interaction and find which phase dominates:

| Phase | Cause | Fix |
| --- | --- | --- |
| Input delay | Long tasks already running | Less startup JavaScript, split long tasks, delay third parties |
| Processing | Heavy work in the event handler | Paint feedback first, then yield with `scheduler.yield()`, move heavy computation to a worker |
| Presentation | Large re-renders and layout | Smaller DOM, fewer components re-rendering, `content-visibility` for long offscreen sections |

For React, the **react-best-practices** skill covers re-renders, bundle size and waterfalls.

## Images

- Serve AVIF or WebP at the displayed size. Resizing a 4000px photo to its 800px slot saves more than changing its format.
- On Cloudflare, Image Transformations convert and resize on request: `/cdn-cgi/image/width=800,format=auto/images/hero.jpg`, where `format=auto` picks AVIF or WebP per browser. The zone needs transformations enabled.
- Compress at a quality that looks right at full size, around 60 to 80 for AVIF and WebP. Check by eye.

## Checks

- [ ] Field LCP, INP and CLS are good on mobile, or there is no field data yet and the lab run is good
- [ ] The LCP element is in the server HTML, prioritized and not lazy
- [ ] Every image, video and embed reserves its space
- [ ] No third-party script blocks rendering
- [ ] Fonts are self-hosted with a swap or optional display
