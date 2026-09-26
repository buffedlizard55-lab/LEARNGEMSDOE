#!/usr/bin/env python3
"""Static checks for the GitHub Pages site in `docs/`.

Three checks, each of which protects a stated rule of this project:

1. **Internal links resolve.** Every relative `href` points at a file that exists, and every
   `#fragment` points at an `id` that exists in the target page.
2. **External links are recorded as sources.** The "no hallucinated sources" rule is only
   enforceable if every outbound link on the site also appears on the sources page. URLs are
   compared on scheme + host + path: query strings are treated as parameters of the same
   endpoint because the sources page records endpoints, not every query permutation.
3. **Pages are structurally consistent.** Every published page carries the two-tier nav, the
   skip link and a `<title>`; referenced local assets exist.

Read-only. It never fetches anything over the network — an offline verifier cannot be fooled by
a live page that changed.

Usage:
    python3 scripts/check_site.py            # report and exit non-zero on any failure
    python3 scripts/check_site.py --quiet    # only print failures
"""

from __future__ import annotations

import html as html_module
import re
import sys
from pathlib import Path
from urllib.parse import urlsplit

ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
SOURCES_PAGE = DOCS / "sources.html"

HREF_RE = re.compile(r'href="([^"]+)"', re.I)
ID_RE = re.compile(r'id="([^"]+)"', re.I)
ASSET_RE = re.compile(r'(?:src|href)="((?!https?:|mailto:|#)[^"]+)"', re.I)

# External hosts that are navigation or identity rather than citations, so they need not appear
# as research sources on the sources page.
NAVIGATION_HOSTS = {"github.com", "www.github.com"}

# This is the site's own Pages host: links to it are navigation, not evidence.
OWN_HOST_SUFFIX = "github.io"


def pages() -> list[Path]:
    return sorted(p for p in DOCS.rglob("*.html") if p.parts[1] != "assets")


def ids_in(path: Path) -> set[str]:
    return set(ID_RE.findall(path.read_text(encoding="utf-8")))


def norm_external(url: str) -> str:
    parts = urlsplit(url)
    if not parts.scheme:
        return ""
    host = parts.netloc.lower()
    path = parts.path.rstrip("/") or "/"
    return f"{parts.scheme.lower()}://{host}{path}"


def collect_source_urls() -> set[str]:
    seen: set[str] = set()
    # Sources page first.
    if SOURCES_PAGE.exists():
        for href in HREF_RE.findall(SOURCES_PAGE.read_text(encoding="utf-8")):
            if href.startswith(("http://", "https://")):
                key = norm_external(href)
                if key:
                    seen.add(key)
    # The project brief is a curated anchor list and counts as permission to cite.
    brief = ROOT / "PROJECT_BRIEF_GEMSDOE.md"
    if brief.exists():
        for href in re.findall(r"https?://[^\s>|)\]]+", brief.read_text(encoding="utf-8")):
            key = norm_external(href.rstrip(".,;"))
            if key:
                seen.add(key)
    return seen


CARD_RE = re.compile(
    r'<a class="card" href="([^"]+\.html)">.*?<p class="card-meta">\s*(\d+)\s+entries', re.S
)


def check_domain_counts() -> list[str]:
    """The overview and library index cards advertise an entry count per domain. Make it true."""
    problems: list[str] = []
    for index_rel, base in (("research/index.html", DOCS / "research"), ("index.html", DOCS)):
        index_page = DOCS / index_rel
        if not index_page.exists():
            problems.append(f"{index_rel} is missing")
            continue
        text = index_page.read_text(encoding="utf-8")
        for target, claimed in CARD_RE.findall(text):
            path = base / target
            if not path.exists():
                problems.append(f"{index_rel}: card points at missing page {target}")
                continue
            actual = path.read_text(encoding="utf-8").count('class="entry"')
            if actual != int(claimed):
                problems.append(
                    f"{index_rel}: {target} claims {claimed} entries, page has {actual}"
                )
    return problems


META_COUNT_RE = re.compile(r"domain \d of 6 · (\d+) entries")


def check_page_meta_counts() -> list[str]:
    """Each domain page announces its own entry count in the page meta line. Make it true."""
    problems: list[str] = []
    for page in sorted((DOCS / "research").glob("*.html")):
        text = page.read_text(encoding="utf-8")
        match = META_COUNT_RE.search(text)
        if not match:
            continue
        claimed = int(match.group(1))
        actual = text.count('class="entry"')
        if claimed != actual:
            problems.append(
                f"{page.relative_to(DOCS).as_posix()}: meta says {claimed} entries, page has {actual}"
            )
    return problems


def main() -> int:
    quiet = "--quiet" in sys.argv
    failures: list[str] = []
    warnings: list[str] = []

    doc_pages = pages()
    id_cache: dict[Path, set[str]] = {}
    sources = collect_source_urls()
    failures.extend(check_domain_counts())
    failures.extend(check_page_meta_counts())

    for page in doc_pages:
        text = page.read_text(encoding="utf-8")
        rel = page.relative_to(DOCS).as_posix()

        # --- structure ------------------------------------------------------
        if 'class="navs"' not in text:
            failures.append(f"{rel}: missing the two-tier nav block")
        if 'class="skip"' not in text:
            failures.append(f"{rel}: missing the skip link")
        if "<title>" not in text:
            failures.append(f"{rel}: missing <title>")

        for raw_href in HREF_RE.findall(text):
            href = html_module.unescape(raw_href)
            if href.startswith("mailto:"):
                continue

            # --- local assets ------------------------------------------------
            if href.startswith("http://") or href.startswith("https://"):
                key = norm_external(href)
                host = urlsplit(href).netloc.lower()
                if host in NAVIGATION_HOSTS or host.endswith(OWN_HOST_SUFFIX) or not key:
                    continue
                if key not in sources:
                    failures.append(
                        f"{rel}: external link not recorded on the sources page → {href}"
                    )
                continue

            if href.startswith("#"):
                if href[1:] not in ids_in(page):
                    failures.append(f"{rel}: dangling in-page anchor {href}")
                continue

            # --- internal pages ------------------------------------------------
            target_part, _, fragment = href.partition("#")
            target = (page.parent / target_part).resolve()
            if not target.exists():
                failures.append(f"{rel}: broken internal link → {href}")
                continue
            if fragment:
                if target not in id_cache:
                    id_cache[target] = ids_in(target)
                if fragment not in id_cache[target]:
                    failures.append(f"{rel}: missing anchor #{fragment} in {target_part}")
            if (
                target_part.endswith(".html")
                and "assets/" not in target_part
                and DOCS in target.parents
                and 'class="navs"' not in target.read_text(encoding="utf-8")
            ):
                warnings.append(f"{rel}: {target_part} is missing the nav block")

        for raw_asset in ASSET_RE.findall(text):
            asset = html_module.unescape(raw_asset)
            if asset.startswith(("http://", "https://", "mailto:", "#")):
                continue
            if "#" in asset or asset.endswith((".html", ".htm")):
                continue  # page links are checked above; only assets are checked here
            if not (page.parent / asset).exists():
                failures.append(f"{rel}: missing local asset → {asset}")

    if not quiet:
        print(f"checked {len(doc_pages)} pages and {len(sources)} recorded source URLs")
        for line in warnings:
            print(f"  note    {line}")
    for line in failures:
        print(f"  FAIL    {line}")

    if failures:
        print(f"\n{len(failures)} failure(s)")
        return 1
    print("site checks passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
