#!/usr/bin/env python3
"""
Fetch and parse software documentation pages into clean markdown.

Modes:
  page    - Fetch a single page, extract main content as markdown
  links   - Fetch a page and list all internal navigation/doc links
  sitemap - Crawl from a root page up to N levels deep, building a sitemap

Usage:
  fetch_docs.py page <url> [--output FILE]
  fetch_docs.py links <url> [--filter PATTERN]
  fetch_docs.py sitemap <url> [--depth N] [--filter PATTERN] [--output FILE]

Dependencies (auto-installed if missing): beautifulsoup4, html2text, requests
"""

import argparse
import json
import re
import subprocess
import sys
from pathlib import Path
from urllib.parse import urljoin, urlparse, urldefrag

def ensure_deps():
    """Install missing dependencies."""
    required = {"bs4": "beautifulsoup4", "html2text": "html2text", "requests": "requests"}
    missing = []
    for mod, pkg in required.items():
        try:
            __import__(mod)
        except ImportError:
            missing.append(pkg)
    if missing:
        print(f"Installing: {', '.join(missing)}", file=sys.stderr)
        subprocess.check_call([sys.executable, "-m", "pip", "install", "-q"] + missing)

ensure_deps()

import requests
from bs4 import BeautifulSoup, Comment
import html2text


# Elements that are almost never main content
REMOVE_SELECTORS = [
    "nav", "header", "footer", ".sidebar", ".nav-sidebar", "#sidebar",
    ".toctree-wrapper", ".sphinxsidebar", ".related", ".topbar", ".navbar",
    ".breadcrumb", ".breadcrumbs", ".page-nav", ".pagination",
    ".header-bar", ".footer-bar", "#navbar", "#header", "#footer",
    ".cookie-banner", ".banner", ".announcement", ".admonition.warning",
    "script", "style", "noscript", ".headerlink",
    # Doxygen-specific
    "#nav-tree", "#side-nav", ".navpath", "#nav-path",
    # Sphinx-specific
    ".sphinxsidebarwrapper", "#searchbox", ".search-button",
    # RTD-specific
    ".rst-versions", ".wy-side-nav-search", ".wy-nav-side",
    # Common doc site patterns
    ".edit-on-github", ".view-source", ".copy-button",
]

# Content selectors to try, in priority order
CONTENT_SELECTORS = [
    "article", "main", "[role='main']",
    ".document", ".body", ".content", "#content",
    ".main-content", ".page-content", ".doc-content",
    ".section", "#main-content", ".markdown-body",
    # Doxygen
    ".contents", "#doc-content",
    # Sphinx
    ".body[role='main']", "div.body",
    # NVIDIA docs
    ".page__content", ".article-content",
]

HEADERS = {
    "User-Agent": "Mozilla/5.0 (compatible; DocFetcher/1.0)"
}


def fetch_page(url: str) -> str:
    """Fetch raw HTML from URL."""
    resp = requests.get(url, headers=HEADERS, timeout=30)
    resp.raise_for_status()
    return resp.text


def find_main_content(soup: BeautifulSoup) -> BeautifulSoup:
    """Extract the main content area from a doc page."""
    # Remove noisy elements first
    for sel in REMOVE_SELECTORS:
        for el in soup.select(sel):
            el.decompose()
    # Remove HTML comments
    for comment in soup.find_all(string=lambda s: isinstance(s, Comment)):
        comment.extract()

    # Try content selectors in order
    for sel in CONTENT_SELECTORS:
        content = soup.select_one(sel)
        if content and len(content.get_text(strip=True)) > 100:
            return content

    # Fallback to body
    body = soup.find("body")
    return body if body else soup


def html_to_markdown(html_content: str, base_url: str) -> str:
    """Convert HTML to clean markdown."""
    h = html2text.HTML2Text()
    h.body_width = 0  # no wrapping
    h.ignore_images = False
    h.ignore_links = False
    h.protect_links = True
    h.baseurl = base_url
    h.ignore_emphasis = False
    h.skip_internal_links = False
    md = h.handle(str(html_content))
    # Clean up excessive blank lines
    md = re.sub(r'\n{4,}', '\n\n\n', md)
    return md.strip()


def extract_links(soup: BeautifulSoup, base_url: str, filter_pattern: str = None) -> list[dict]:
    """Extract all documentation links from a page."""
    parsed_base = urlparse(base_url)
    base_domain = parsed_base.netloc
    links = []
    seen = set()

    for a in soup.find_all("a", href=True):
        href = a["href"]
        # Skip anchors-only, javascript, mailto
        if href.startswith(("#", "javascript:", "mailto:")):
            continue

        full_url = urljoin(base_url, href)
        full_url, _ = urldefrag(full_url)  # remove fragment

        # Only keep same-domain links
        parsed = urlparse(full_url)
        if parsed.netloc != base_domain:
            continue

        # Skip non-doc resources
        path = parsed.path.lower()
        if any(path.endswith(ext) for ext in ['.png', '.jpg', '.gif', '.svg', '.css', '.js', '.zip', '.tar', '.gz', '.whl']):
            continue

        if full_url in seen:
            continue
        seen.add(full_url)

        text = a.get_text(strip=True)
        if not text:
            continue

        if filter_pattern and not re.search(filter_pattern, full_url, re.IGNORECASE):
            continue

        links.append({"text": text, "url": full_url})

    return links


def fetch_doc_page(url: str) -> dict:
    """Fetch a doc page and return structured result."""
    html = fetch_page(url)
    soup = BeautifulSoup(html, "html.parser")

    # Extract title
    title_el = soup.find("title")
    title = title_el.get_text(strip=True) if title_el else ""

    # Get main content
    content = find_main_content(soup)
    markdown = html_to_markdown(content, url)

    return {"title": title, "url": url, "content": markdown}


def fetch_doc_links(url: str, filter_pattern: str = None) -> list[dict]:
    """Fetch a doc page and return all doc links."""
    html = fetch_page(url)
    soup = BeautifulSoup(html, "html.parser")
    return extract_links(soup, url, filter_pattern)


def build_sitemap(url: str, max_depth: int = 2, filter_pattern: str = None) -> list[dict]:
    """Crawl from root URL building a sitemap of doc pages."""
    parsed_base = urlparse(url)
    base_path = parsed_base.path.rsplit("/", 1)[0] if "/" in parsed_base.path else ""

    visited = set()
    sitemap = []
    queue = [(url, 0)]

    while queue:
        current_url, depth = queue.pop(0)
        if current_url in visited:
            continue
        visited.add(current_url)

        try:
            html = fetch_page(current_url)
        except Exception as e:
            print(f"  Skip {current_url}: {e}", file=sys.stderr)
            continue

        soup = BeautifulSoup(html, "html.parser")
        title_el = soup.find("title")
        title = title_el.get_text(strip=True) if title_el else current_url

        sitemap.append({"title": title, "url": current_url, "depth": depth})
        print(f"  [{depth}] {title}", file=sys.stderr)

        if depth < max_depth:
            links = extract_links(soup, current_url, filter_pattern)
            for link in links:
                link_url = link["url"]
                # Only follow links under the same base path
                link_parsed = urlparse(link_url)
                if link_parsed.path.startswith(base_path) and link_url not in visited:
                    queue.append((link_url, depth + 1))

    return sitemap


def main():
    parser = argparse.ArgumentParser(description="Fetch software documentation pages")
    subparsers = parser.add_subparsers(dest="mode", required=True)

    # page mode
    p_page = subparsers.add_parser("page", help="Fetch a single page as markdown")
    p_page.add_argument("url")
    p_page.add_argument("--output", "-o", help="Write output to file instead of stdout")

    # links mode
    p_links = subparsers.add_parser("links", help="List doc links on a page")
    p_links.add_argument("url")
    p_links.add_argument("--filter", "-f", help="Regex to filter link URLs")

    # sitemap mode
    p_sitemap = subparsers.add_parser("sitemap", help="Crawl and build a sitemap")
    p_sitemap.add_argument("url")
    p_sitemap.add_argument("--depth", "-d", type=int, default=1, help="Max crawl depth (default: 1)")
    p_sitemap.add_argument("--filter", "-f", help="Regex to filter link URLs")
    p_sitemap.add_argument("--output", "-o", help="Write output to file")

    args = parser.parse_args()

    if args.mode == "page":
        result = fetch_doc_page(args.url)
        output = f"# {result['title']}\n\nSource: {result['url']}\n\n---\n\n{result['content']}"
        if args.output:
            Path(args.output).parent.mkdir(parents=True, exist_ok=True)
            Path(args.output).write_text(output)
            print(f"Written to {args.output}", file=sys.stderr)
        else:
            print(output)

    elif args.mode == "links":
        links = fetch_doc_links(args.url, args.filter)
        for link in links:
            print(f"- [{link['text']}]({link['url']})")

    elif args.mode == "sitemap":
        sitemap = build_sitemap(args.url, args.depth, args.filter)
        output = json.dumps(sitemap, indent=2)
        if args.output:
            Path(args.output).parent.mkdir(parents=True, exist_ok=True)
            Path(args.output).write_text(output)
            print(f"Sitemap ({len(sitemap)} pages) written to {args.output}", file=sys.stderr)
        else:
            # Print as readable list
            for entry in sitemap:
                indent = "  " * entry["depth"]
                print(f"{indent}- [{entry['title']}]({entry['url']})")


if __name__ == "__main__":
    main()
