# Content and trust

Rung 5. Google's ranking systems aim to reward content made to help people, written by someone who knows the subject. Every technical fix below this rung only lets Google see the page. This rung is why it would pick the page.

## One page, one intent

- Each page answers one search intent and targets one primary query, with its close variants.
- Search the query and read the top results before writing. Match the kind of page they are (a tool, a list, a guide, a product page). A guide never outranks tools on a query where every result is a tool.
- Answer the query in the first two sentences, then go deeper. That opening is also the passage AI answers tend to quote.
- Cover the sub-questions the top results and the "People also ask" box show. Add the missing section rather than rewriting the page.
- Two pages chasing the same query compete. Pick one, merge the useful parts of the other into it, and 301 the loser. This is **cannibalization**.

## Worth reading

Google's self-assessment, condensed. Each "no" is a finding:

- Does the page offer original information, research, analysis or first-hand experience, beyond what the other results already say?
- Is the topic covered completely enough that a reader leaves without searching again?
- Would someone bookmark it, share it or recommend it?
- Is it free of easily checked factual errors?
- Is it made for the site's existing audience, rather than to attract search traffic?

Warning signs: a page made mainly to rank, summaries of other pages with nothing added, many pages on topics the site has no expertise in, and mass-produced pages with little care for each.

## Slop

- Rewrite copy that reads as machine-made with the patterns in [`unslop`](../../unslop/SKILL.md): filler phrases, words like "delve" and "crucial", forced groups of three, long dashes, empty summaries.
- Concrete beats generic. A number, a name, a screenshot, a worked example or a first-hand detail is what generated text lacks.
- AI may help write. Generating many pages with little oversight to manipulate rankings is **scaled content abuse**, a spam policy. A set of generated pages (one per city, per tool, per keyword) ships only when each page carries data or value unique to it.

## Who, how and why

- **Who.** Put a byline wherever readers expect one, linked to an author page with a real name, photo, bio, credentials and profile links, and `ProfilePage` markup from [structured-data.md](structured-data.md). Google warns against deceptive authorship: invented names, generated headshots or false credentials. Jack supplies every author detail.
- **How.** Say how the content was made when readers would wonder: tested by hand, based on what data, written with AI help and checked by whom.
- **Why.** The page exists to help its reader.

## Trust

- An About page that says who runs the site, and a Contact page with a real way to reach them.
- Privacy policy and terms. For a business, the same name, address and phone everywhere they appear.
- Reviews, testimonials, customer logos and case studies are real and attributable, from Jack. Never write one.
- `dateModified` and "updated" labels change only when the content does.

## Spam policies

Each can cost a page or the whole site its rankings:

- **Cloaking:** showing crawlers different content from people.
- **Doorway pages:** many near-identical pages that funnel to one place.
- **Hidden text or links,** and **keyword stuffing.**
- **Link schemes:** buying, selling or trading links that pass ranking credit, and mass guest posts or comments with keyword anchors.
- **Scaled content abuse,** above.
- **Site reputation abuse:** hosting third-party pages to ride the site's rankings.
- **Expired domain abuse:** buying an old domain to rank unrelated content.
- **Sneaky redirects:** sending searchers somewhere other than what crawlers saw.
- **Fake reviews** and markup for content that is not on the page.

## Links from other sites

Links from relevant, trusted sites remain a strong signal, and they come from relationships, so earning them is Jack's work. You can prepare it:

- Make linkable assets: a free tool, original data, a template, a clear guide others cite.
- List the places where a link would be natural: the niche's directories and "awesome" lists, integration partners' pages, launch sites, communities where Jack already takes part, podcasts and newsletters in the field.
- Draft outreach for Jack to send. Never buy links, auto-post comments or submit to link farms.

[owner-tasks.md](owner-tasks.md) holds the steps.

## After launch

Once Search Console has a few weeks of data, Jack can share it:

- **Striking distance:** queries where a page averages position 8 to 20. Find what the top three results have that the page lacks, add it, and add internal links to the page.
- **Weak click-through:** a page in the top five with a click-through rate well below its neighbours needs a better title and description, and nothing else, so the change is measurable.
- Change one page at a time, note the baseline, and wait three to four weeks before judging.

## Checks

- [ ] Each page targets one intent, with no two pages on the same query
- [ ] The answer is in the opening of the page
- [ ] The copy passes the unslop patterns
- [ ] Every byline names a real person with an author page, supplied by Jack
- [ ] About, Contact, Privacy and Terms pages exist
- [ ] No content, review or link that breaks a spam policy
