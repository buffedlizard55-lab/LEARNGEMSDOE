#!/usr/bin/env python3
"""Build the client-side search index for the GitHub Pages site.

Reads the markdown mirrors in `research/` and the page metadata in `docs/`, then writes
`docs/assets/search-index.js`. Idempotent: re-running regenerates the same file from the
current sources. Nothing here fetches, downloads or produces prediction data.

Usage:
    python3 scripts/build_search_index.py            # write the index
    python3 scripts/build_search_index.py --check    # report drift, exit 1 if out of date
"""

from __future__ import annotations

import json
import re
import sys
from html.parser import HTMLParser
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
RESEARCH = ROOT / "research"
DOCS = ROOT / "docs"
OUT = DOCS / "assets" / "search-index.js"

# Markdown mirror -> (published page, human domain label, entry-id prefix)
DOMAINS = {
    "catalogue-gaps.md": ("research/catalogue-gaps.html", "Catalogue gaps", "CG"),
    "potential-field.md": ("research/potential-field.html", "Potential field", "PF"),
    "geomorphology.md": ("research/geomorphology.html", "Geomorphology", "GM"),
    "seismotectonics.md": ("research/seismotectonics.html", "Seismotectonics", "ST"),
    "prior-art.md": ("research/prior-art.html", "Prior art", "PA"),
    "governance.md": ("research/governance.html", "Governance", "GV"),
}

# Numbered-entry mirrors where the id has no domain prefix (H1, H2, …).
ENTRY_DOCUMENTS = {
    "hypotheses.md": ("hypotheses.html", "Hypotheses"),
}

# Other markdown mirrors indexed section by section.
DOCUMENTS = {
    "feature-stack.md": ("feature-stack.html", "Feature stack"),
    "data-placement.md": ("pipeline.html", "Pipeline"),
}

# Entry heading pattern: "## CG-9 · Title", "## H11 — Title", "## GM-7 · Title (…)"
ENTRY_RE = re.compile(r"^##\s+(([A-Z]{1,2})-?(\d+))\s*[·—-]\s*(.+?)\s*$")
HEADING_RE = re.compile(r"^(#{2,3})\s+(.+?)\s*$")


def slugify(prefix: str, number: str) -> str:
    return f"{prefix.lower()}{number}"


def strip_markdown(text: str) -> str:
    """Flatten markdown to searchable plain text without losing the words."""
    text = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", text)  # [label](url) -> label
    text = re.sub(r"<https?://[^>]+>", "", text)  # bare autolinks
    text = re.sub(r"<span[^>]*>|</span>", "", text)  # stray html spans in md mirrors
    text = re.sub(r"`{1,3}([^`]*)`{1,3}", r"\1", text)  # code
    text = text.replace("**", "").replace("*", "")
    text = re.sub(r"\s+", " ", text)
    return text.strip()


def parse_markdown_entries(path: Path, page: str, domain: str, prefix: str) -> list[dict]:
    items: list[dict] = []
    lines = path.read_text(encoding="utf-8").splitlines()
    current: dict | None = None
    for line in lines:
        match = ENTRY_RE.match(line)
        if match:
            if current:
                items.append(current)
            current = {
                "id": match.group(1),
                "anchor": slugify(match.group(2), match.group(3)),
                "title": strip_markdown(match.group(4)),
                "domain": domain,
                "url": page,
                "body": [],
            }
            continue
        if HEADING_RE.match(line):
            if current:
                items.append(current)
                current = None
            continue
        if current is not None:
            current["body"].append(line)
    if current:
        items.append(current)

    out = []
    for item in items:
        body = strip_markdown(" ".join(item["body"]))
        out.append(
            {
                "id": item["id"],
                "title": f"{item['id']} · {item['title']}",
                "domain": domain,
                "url": f"{item['url']}#{item['anchor']}",
                "text": f"{item['title']} {body}"[:4000],
            }
        )
    return out


def parse_markdown_sections(path: Path, page: str, domain: str) -> list[dict]:
    """Whole-document index for mirrors that are not numbered entry lists."""
    text = path.read_text(encoding="utf-8")
    items: list[dict] = []
    current_title = domain
    current_body: list[str] = []
    for line in text.splitlines():
        heading = HEADING_RE.match(line)
        if heading:
            if current_body:
                items.append((current_title, " ".join(current_body)))
            current_title = strip_markdown(heading.group(2))
            current_body = []
            continue
        current_body.append(line)
    if current_body:
        items.append((current_title, " ".join(current_body)))
    return [
        {
            "id": "",
            "title": f"{domain} — {title}",
            "domain": domain,
            "url": page,
            "text": f"{title} {strip_markdown(body)}"[:4000],
        }
        for title, body in items
        if strip_markdown(body)
    ]


class MetaParser(HTMLParser):
    """Pull <title> and <meta name="description"> out of a page."""

    def __init__(self) -> None:
        super().__init__()
        self.title = ""
        self.description = ""
        self._in_title = False

    def handle_starttag(self, tag, attrs):
        if tag == "title":
            self._in_title = True
        elif tag == "meta":
            attrs = dict(attrs)
            if attrs.get("name") == "description":
                self.description = attrs.get("content", "")

    def handle_endtag(self, tag):
        if tag == "title":
            self._in_title = False

    def handle_data(self, data):
        if self._in_title:
            self.title += data


def parse_pages() -> list[dict]:
    items = []
    for page in sorted(DOCS.rglob("*.html")):
        rel = page.relative_to(DOCS).as_posix()
        if rel.startswith("assets/"):
            continue
        parser = MetaParser()
        parser.feed(page.read_text(encoding="utf-8"))
        title = re.sub(r"\s+", " ", parser.title).strip()
        if not title:
            continue
        items.append(
            {
                "id": "",
                "title": title,
                "domain": "Page",
                "url": rel,
                "text": f"{title} {parser.description}".strip(),
            }
        )
    return items


def build() -> list[dict]:
    items: list[dict] = []
    for name, (page, domain, prefix) in DOMAINS.items():
        path = RESEARCH / name
        if path.exists():
            items.extend(parse_markdown_entries(path, page, domain, prefix))
    for name, (page, domain) in ENTRY_DOCUMENTS.items():
        path = RESEARCH / name
        if path.exists():
            items.extend(parse_markdown_entries(path, page, domain, ""))
    for name, (page, domain) in DOCUMENTS.items():
        path = RESEARCH / name
        if path.exists():
            items.extend(parse_markdown_sections(path, page, domain))
    items.extend(parse_pages())
    # Stable order: entries first (by id), then pages.
    items.sort(key=lambda item: (item["domain"] == "Page", item["domain"], item["id"], item["title"]))
    return items


def main() -> int:
    items = build()
    payload = "/* Generated by scripts/build_search_index.py — do not edit by hand. */\n"
    payload += "window.GEMSDOE_INDEX = " + json.dumps(items, ensure_ascii=False, indent=0, sort_keys=False) + ";\n"

    if "--check" in sys.argv:
        current = OUT.read_text(encoding="utf-8") if OUT.exists() else ""
        if current != payload:
            print(f"search index is out of date: {len(items)} items would be written to {OUT}")
            return 1
        print(f"search index up to date: {len(items)} items")
        return 0

    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(payload, encoding="utf-8")
    print(f"wrote {OUT.relative_to(ROOT)} — {len(items)} searchable items")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
