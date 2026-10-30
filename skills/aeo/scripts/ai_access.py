#!/usr/bin/env python3
"""Check whether AI answer engines can reach and read a page.

Usage: python3 ai_access.py https://example.com/some/page

For every AI crawler and fetcher it reports what robots.txt decides for the
page, then fetches the page with that bot's user agent and reports the HTTP
status, how much visible text the raw HTML holds, and signs of a bot challenge.
It also checks /llms.txt. Standard library only.
"""

import re
import sys
import urllib.error
import urllib.request
from urllib.parse import urljoin, urlparse

BOTS = [
    # (robots.txt token, user agent sent, purpose)
    ("Googlebot", "Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)", "search: Google Search, AI Overviews, AI Mode"),
    ("Bingbot", "Mozilla/5.0 (compatible; bingbot/2.0; +http://www.bing.com/bingbot.htm)", "search: Bing, Copilot"),
    ("OAI-SearchBot", "Mozilla/5.0 AppleWebKit/537.36 (KHTML, like Gecko); compatible; OAI-SearchBot/1.4; +https://openai.com/searchbot", "search: ChatGPT search"),
    ("Claude-SearchBot", "Mozilla/5.0 AppleWebKit/537.36 (KHTML, like Gecko); compatible; Claude-SearchBot/1.0; +https://www.anthropic.com", "search: Claude"),
    ("PerplexityBot", "Mozilla/5.0 AppleWebKit/537.36 (KHTML, like Gecko); compatible; PerplexityBot/1.0; +https://perplexity.ai/perplexitybot", "search: Perplexity"),
    ("Applebot", "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.0 Safari/605.1.15 (Applebot/0.1; +http://www.apple.com/go/applebot)", "search: Siri, Spotlight, Safari"),
    ("meta-webindexer", "meta-webindexer/1.1 (+https://developers.facebook.com/docs/sharing/webmasters/crawler)", "search: Meta AI"),
    ("ChatGPT-User", "Mozilla/5.0 AppleWebKit/537.36 (KHTML, like Gecko); compatible; ChatGPT-User/1.0; +https://openai.com/bot", "user fetch: ChatGPT"),
    ("Claude-User", "Mozilla/5.0 AppleWebKit/537.36 (KHTML, like Gecko); compatible; Claude-User/1.0; +https://www.anthropic.com", "user fetch: Claude"),
    ("Perplexity-User", "Mozilla/5.0 AppleWebKit/537.36 (KHTML, like Gecko); compatible; Perplexity-User/1.0; +https://perplexity.ai/perplexity-user", "user fetch: Perplexity"),
    ("GPTBot", "Mozilla/5.0 AppleWebKit/537.36 (KHTML, like Gecko); compatible; GPTBot/1.4; +https://openai.com/gptbot", "training: OpenAI"),
    ("ClaudeBot", "Mozilla/5.0 AppleWebKit/537.36 (KHTML, like Gecko); compatible; ClaudeBot/1.0; +claudebot@anthropic.com", "training: Anthropic"),
    ("meta-externalagent", "meta-externalagent/1.1 (+https://developers.facebook.com/docs/sharing/webmasters/crawler)", "training: Meta"),
    ("CCBot", "CCBot/2.0 (https://commoncrawl.org/faq/)", "training: Common Crawl"),
    ("Google-Extended", None, "training and Gemini grounding (token only, never fetches)"),
    ("Applebot-Extended", None, "training: Apple (token only, never fetches)"),
]

BROWSER = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0 Safari/537.36"
CHALLENGE = re.compile(r"cf-challenge|challenge-platform|just a moment\.\.\.|captcha|attention required|access denied|verify you are human", re.I)


def fetch(url, agent):
    request = urllib.request.Request(url, headers={"User-Agent": agent, "Accept": "text/html,*/*"})
    try:
        with urllib.request.urlopen(request, timeout=20) as response:
            return response.status, response.read(2_000_000).decode("utf-8", "replace")
    except urllib.error.HTTPError as error:
        return error.code, error.read(200_000).decode("utf-8", "replace")
    except Exception as error:
        return None, str(error)


def visible_text_length(html):
    html = re.sub(r"(?is)<(script|style|noscript|template|svg)\b.*?</\1>", " ", html)
    text = re.sub(r"(?s)<[^>]+>", " ", html)
    return len(re.sub(r"\s+", " ", text).strip())


def parse_robots(text):
    """Group robots.txt rules by user agent, per RFC 9309."""
    groups = {}
    agents = []
    last_was_agent = False
    for raw in text.splitlines():
        line = raw.split("#", 1)[0].strip()
        if ":" not in line:
            continue
        key, value = (part.strip() for part in line.split(":", 1))
        key = key.lower()
        if key == "user-agent":
            if not last_was_agent:
                agents = []
            agents.append(value.lower())
            groups.setdefault(value.lower(), [])
            last_was_agent = True
        elif key in ("allow", "disallow"):
            for agent in agents:
                groups[agent].append((key == "allow", value))
            last_was_agent = False
        else:
            last_was_agent = False
    return groups


def rule_matches(pattern, path):
    if not pattern:
        return False
    regex = re.escape(pattern).replace(r"\*", ".*")
    if regex.endswith(r"\$"):
        regex = regex[:-2] + "$"
    return re.match(regex, path) is not None


def robots_decision(groups, token, path):
    """Return (allowed, which group decided). Longest match wins, allow wins ties."""
    group_name = token.lower() if token.lower() in groups else "*"
    rules = groups.get(group_name, [])
    best = None
    for allow, pattern in rules:
        if rule_matches(pattern, path):
            length = len(pattern)
            if best is None or length > best[0] or (length == best[0] and allow):
                best = (length, allow)
    allowed = True if best is None else best[1]
    return allowed, group_name if group_name in groups else "none"


def main():
    if len(sys.argv) != 2:
        print(__doc__)
        return 2
    url = sys.argv[1]
    parsed = urlparse(url)
    origin = f"{parsed.scheme}://{parsed.netloc}"
    path = (parsed.path or "/") + (f"?{parsed.query}" if parsed.query else "")

    robots_status, robots_text = fetch(urljoin(origin, "/robots.txt"), BROWSER)
    if robots_status == 200:
        groups = parse_robots(robots_text)
        print(f"robots.txt: 200, groups for {', '.join(sorted(groups)) or 'nobody'}")
    elif robots_status is not None and robots_status < 500:
        groups = {}
        print(f"robots.txt: {robots_status}, so every bot may crawl")
    else:
        groups = {}
        print(f"robots.txt: {robots_status or robots_text}. Crawlers treat an unreachable or 5xx robots.txt as disallow all, fix this first")

    browser_status, browser_html = fetch(url, BROWSER)
    if browser_status is None:
        print(f"could not fetch {url}: {browser_html}")
        return 1
    browser_text = visible_text_length(browser_html)
    print(f"browser: HTTP {browser_status}, {browser_text} characters of visible text in the raw HTML")
    if browser_text < 500:
        print("  warning: little text before JavaScript runs. Most AI fetchers do not run JavaScript, see the seo skill on rendering")
    print()

    print(f"{'bot':<20} {'robots.txt':<28} {'HTTP':<6} {'text':<8} purpose")
    for token, agent, purpose in BOTS:
        allowed, group = robots_decision(groups, token, path)
        verdict = f"{'allow' if allowed else 'DISALLOW'} ({group})"
        if agent is None:
            print(f"{token:<20} {verdict:<28} {'-':<6} {'-':<8} {purpose}")
            continue
        status, html = fetch(url, agent)
        text = visible_text_length(html)
        flag = " CHALLENGE PAGE" if CHALLENGE.search(html[:20000]) and text < browser_text * 0.5 else ""
        if status is not None and status != browser_status:
            flag += f" status differs from browser ({browser_status})"
        print(f"{token:<20} {verdict:<28} {str(status):<6} {text:<8} {purpose}{flag}")

    print()
    llms_status, llms_text = fetch(urljoin(origin, "/llms.txt"), BROWSER)
    if llms_status == 200 and llms_text.lstrip("﻿").startswith("# "):
        print("llms.txt: present and starts with an H1")
    elif llms_status == 200:
        print("llms.txt: 200 but does not start with '# ', so it is probably an HTML fallback page")
    else:
        print(f"llms.txt: {llms_status} (optional, see references/agent-readiness.md)")
    print()
    print("A 403 or challenge for one bot while the browser gets 200 means a CDN or WAF rule. Some providers")
    print("verify bots by IP, so a spoofed agent from this machine can be blocked even when the real bot is let in.")
    print("Confirm in the CDN's bot settings or server logs before changing anything.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
