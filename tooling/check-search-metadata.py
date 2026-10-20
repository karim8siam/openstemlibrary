"""Check sitemap targets and search metadata without changing textbook content."""
from collections import Counter
from datetime import date
from html.parser import HTMLParser
from pathlib import Path
import json
import sys
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parents[1]
BASE = "https://openstemlibrary.com/"


class Metadata(HTMLParser):
    def __init__(self):
        super().__init__()
        self.canonicals = []
        self.robots = []
        self.title = ""
        self.schemas = []
        self.in_title = False
        self.in_schema = False

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if tag == "link" and "canonical" in attrs.get("rel", "").split():
            self.canonicals.append(attrs.get("href"))
        if tag == "meta" and attrs.get("name", "").lower() in ("robots", "googlebot"):
            self.robots.extend(attrs.get("content", "").lower().replace(",", " ").split())
        if tag == "title":
            self.in_title = True
        if tag == "script" and attrs.get("type") == "application/ld+json":
            self.in_schema = True
            self.schemas.append("")

    def handle_endtag(self, tag):
        if tag == "title":
            self.in_title = False
        if tag == "script":
            self.in_schema = False

    def handle_data(self, data):
        if self.in_title:
            self.title += data
        if self.in_schema:
            self.schemas[-1] += data


def check():
    failures = []
    tree = ET.parse(ROOT / "sitemap.xml")
    entries = tree.getroot().findall("{*}url")
    urls = [entry.findtext("{*}loc", "") for entry in entries]
    for url, count in Counter(urls).items():
        if count != 1:
            failures.append(f"Duplicate sitemap URL: {url}")
    titles = {}
    for entry, url in zip(entries, urls):
        route = url.removeprefix(BASE)
        if not url.startswith(BASE) or any(c in route for c in "?#") or route.endswith(".html"):
            failures.append(f"Noncanonical sitemap URL: {url}")
            continue
        if route.startswith(("publishing/", "tooling/")) or route == "404":
            failures.append(f"Internal/error page in sitemap: {url}")
        relative = route + ".html" if route else "index.html"
        file = ROOT / relative
        if not file.is_file() and (ROOT / "dist" / relative).is_file():
            file = ROOT / "dist" / relative
        if not file.resolve().is_relative_to(ROOT) or not file.is_file():
            failures.append(f"Missing sitemap target: {url}")
            continue
        metadata = Metadata()
        metadata.feed(file.read_text())
        if metadata.canonicals != [url]:
            failures.append(f"Canonical mismatch: {url}")
        if any(value in metadata.robots for value in ("noindex", "none")):
            failures.append(f"Nonindexable sitemap target: {url}")
        title = metadata.title.strip()
        if not title or title in titles:
            failures.append(f"Missing/duplicate title: {url}")
        titles[title] = url
        for schema in metadata.schemas:
            try:
                json.loads(schema)
            except ValueError:
                failures.append(f"Invalid structured data JSON: {url}")
        lastmod = entry.findtext("{*}lastmod")
        if lastmod:
            try:
                if date.fromisoformat(lastmod) > date.today():
                    failures.append(f"Future sitemap lastmod: {url}")
            except ValueError:
                failures.append(f"Invalid sitemap lastmod: {url}")
    if not (ROOT / "404.html").is_file():
        failures.append("Missing top-level 404.html: Cloudflare will serve the homepage for unknown URLs")
    print(json.dumps({"sitemap_urls": len(urls), "failures": failures}, indent=2))
    return bool(failures)


if __name__ == "__main__":
    sys.exit(check())
