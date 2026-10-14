#!/usr/bin/env python3
"""Live-check external links in source content and a freshly rendered Hugo site.

The checker extracts rendered Markdown links with markdown-it, limits global
and per-host concurrency, streams only response headers, retries transient
failures, and keeps restricted-but-existing responses separate from dead
links. HTTP 400/422, TLS failures, timeouts, rate limits and access restrictions are
not treated as confirmed dead links. WeChat can be excluded for an archive-aware
pass. The checker does not modify content.
"""

from __future__ import annotations

import argparse
import asyncio
import csv
import json
import time
from collections import Counter, defaultdict
from datetime import datetime
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlsplit

import httpx
from markdown_it import MarkdownIt


LIVE = set(range(200, 400))
RESTRICTED = {401, 403, 405, 451}
DEAD = {404, 410}
TRANSIENT = {408, 425, 429, 500, 502, 503, 504}


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--manifest", default="WXMP-IMPORT-MANIFEST.csv")
    parser.add_argument("--content-dir", help="scan all Markdown under a content directory")
    parser.add_argument("--public-dir", help="also extract links from rendered HTML, including automatic links")
    parser.add_argument("--include-images", action="store_true", help="also check remote image URLs")
    parser.add_argument("--proxy", help="explicit HTTP proxy for this audit, overriding proxy environment variables")
    parser.add_argument("--output", default="WXMP-EXTERNAL-LINKS.json")
    parser.add_argument("--concurrency", type=int, default=16)
    parser.add_argument("--per-host", type=int, default=2)
    parser.add_argument("--timeout", type=float, default=15.0)
    parser.add_argument("--retries", type=int, default=2)
    parser.add_argument("--skip-domain", action="append", default=[])
    parser.add_argument("--reuse", action="store_true", help="reuse prior results for unchanged URLs")
    parser.add_argument("--progress-output", help="save each completed result as JSON Lines")
    return parser.parse_args()


def extract_links(manifest: Path, content_dir: Path | None = None, public_dir: Path | None = None, include_images: bool = False) -> tuple[list[str], dict[str, list[str]]]:
    if content_dir:
        paths = sorted(content_dir.rglob("*.md"))
    else:
        with manifest.open(encoding="utf-8-sig") as stream:
            paths = [Path(row["path"]) for row in csv.DictReader(stream)]
    parser = MarkdownIt("commonmark")
    occurrences: dict[str, list[str]] = defaultdict(list)
    class HTMLLinks(HTMLParser):
        def __init__(self) -> None:
            super().__init__()
            self.links: list[str] = []

        def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
            if tag == "a":
                self.links.extend(value for key, value in attrs if key == "href" and value)
            elif include_images and tag == "img":
                self.links.extend(value for key, value in attrs if key == "src" and value)

    for path in paths:
        source = path.read_text(encoding="utf-8", errors="ignore")
        if source.startswith("---\n") and "\n---\n" in source:
            source = source.split("\n---\n", 1)[1]
        for token in parser.parse(source):
            if token.type == "html_block":
                html_links = HTMLLinks()
                html_links.feed(token.content)
                for href in html_links.links:
                    if href.startswith(("http://", "https://")):
                        occurrences[href].append(path.as_posix())
            if token.type != "inline" or not token.children:
                continue
            for child in token.children:
                if include_images and child.type == "image":
                    href = child.attrGet("src") or ""
                    if href.startswith(("http://", "https://")):
                        occurrences[href].append(path.as_posix())
                if child.type == "html_inline":
                    html_links = HTMLLinks()
                    html_links.feed(child.content)
                    for href in html_links.links:
                        if href.startswith(("http://", "https://")):
                            occurrences[href].append(path.as_posix())
                if child.type != "link_open":
                    continue
                href = child.attrGet("href") or ""
                if href.startswith(("http://", "https://")):
                    occurrences[href].append(path.as_posix())
    if public_dir:
        from bs4 import BeautifulSoup
        # Limit the rendered pass to pages represented by the content tree;
        # standalone static applications may embed unrelated link catalogs.
        rendered_pages: set[Path] = set()
        if content_dir:
            for source in paths:
                relative = source.relative_to(content_dir)
                name = relative.name
                language = "en" if name.endswith(".en.md") else ""
                stem = name.removesuffix(".en.md").removesuffix(".md")
                route = relative.parent if stem in {"index", "_index"} else relative.parent / stem
                rendered_pages.add(public_dir / language / route / "index.html")
        for page in sorted(public_dir.rglob("*.html")):
            if content_dir and page not in rendered_pages:
                continue
            document = BeautifulSoup(page.read_text(encoding="utf-8", errors="ignore"), "html.parser")
            body = document.select_one(".td-content")
            if not body:
                continue
            for sharing in body.select(".td-share, .td-page-actions"):
                sharing.decompose()
            html_links = HTMLLinks()
            html_links.feed(str(body))
            for href in html_links.links:
                if href.startswith(("http://", "https://")):
                    occurrences[href].append(page.as_posix())
    return sorted(occurrences), occurrences


async def check_one(
    url: str,
    client: httpx.AsyncClient,
    global_limit: asyncio.Semaphore,
    host_limit: asyncio.Semaphore,
    retries: int,
) -> dict[str, object]:
    started = time.monotonic()
    last_error = ""
    status = None
    final_url = url
    attempts = 0
    for attempt in range(retries + 1):
        attempts = attempt + 1
        try:
            # Acquire the per-host slot first so a large domain cannot occupy
            # every global slot while its tasks wait on the same host lock.
            async with host_limit, global_limit, asyncio.timeout(client.timeout.connect + client.timeout.read):
                async with client.stream(
                    "GET",
                    url,
                    headers={
                        "User-Agent": "Mozilla/5.0 (compatible; VonngLinkAudit/1.0)",
                        "Accept": "text/html,application/xhtml+xml,application/json;q=0.9,*/*;q=0.1",
                        "Range": "bytes=0-4095",
                    },
                    follow_redirects=True,
                ) as response:
                    status = response.status_code
                    final_url = str(response.url)
            if status in {400, 404, 410, 416, 422}:
                async with host_limit, global_limit, asyncio.timeout(client.timeout.connect + client.timeout.read):
                    async with client.stream(
                        "GET", url,
                        headers={"User-Agent": "Mozilla/5.0 (compatible; VonngLinkAudit/1.0)"},
                        follow_redirects=True,
                    ) as response:
                        status = response.status_code
                        final_url = str(response.url)
            if status not in TRANSIENT:
                break
            last_error = f"transient HTTP {status}"
        except (httpx.HTTPError, httpx.InvalidURL, ValueError, OSError) as exc:
            last_error = f"{type(exc).__name__}: {exc}"
        if attempt < retries:
            await asyncio.sleep(0.75 * (2**attempt))

    if status in LIVE:
        outcome = "live"
    elif status in RESTRICTED:
        outcome = "restricted"
    elif status in DEAD:
        outcome = "dead"
    elif status is not None:
        outcome = "uncertain"
    else:
        outcome = "error"
    return {
        "url": url,
        "outcome": outcome,
        "status": status,
        "final_url": final_url,
        "attempts": attempts,
        "elapsed_ms": round((time.monotonic() - started) * 1000),
        "error": last_error,
    }


async def run(args: argparse.Namespace) -> dict[str, object]:
    urls, occurrences = extract_links(
        Path(args.manifest), Path(args.content_dir) if args.content_dir else None,
        Path(args.public_dir) if args.public_dir else None,
        args.include_images,
    )
    skipped: list[str] = []
    selected: list[str] = []
    skip_domains = {domain.lower() for domain in args.skip_domain}
    for url in urls:
        host = urlsplit(url).netloc.lower().split(":", 1)[0]
        if host in skip_domains:
            skipped.append(url)
        else:
            selected.append(url)

    prior_results: dict[str, dict[str, object]] = {}
    if args.reuse and Path(args.output).exists():
        prior = json.loads(Path(args.output).read_text(encoding="utf-8"))
        prior_results = {item["url"]: item for item in prior.get("results", [])}
    reused = [prior_results[url] for url in selected if url in prior_results]
    selected = [url for url in selected if url not in prior_results]

    global_limit = asyncio.Semaphore(args.concurrency)
    host_limits: dict[str, asyncio.Semaphore] = defaultdict(
        lambda: asyncio.Semaphore(args.per_host)
    )
    timeout = httpx.Timeout(args.timeout, connect=args.timeout)
    limits = httpx.Limits(max_connections=None, max_keepalive_connections=args.concurrency)
    async with httpx.AsyncClient(
        timeout=timeout, limits=limits, verify=True,
        proxy=args.proxy, trust_env=not bool(args.proxy),
    ) as client:
        tasks = []
        for url in selected:
            host = urlsplit(url).netloc.lower().split(":", 1)[0]
            tasks.append(
                check_one(url, client, global_limit, host_limits[host], args.retries)
            )
        results = []
        progress = Path(args.progress_output).open("w", encoding="utf-8") if args.progress_output else None
        try:
            for completed, task in enumerate(asyncio.as_completed(tasks), start=1):
                result = await task
                results.append(result)
                if progress:
                    progress.write(json.dumps(result, ensure_ascii=False) + "\n")
                    progress.flush()
                if completed % 100 == 0 or completed == len(tasks):
                    print(f"checked {completed}/{len(tasks)}", flush=True)
        finally:
            if progress:
                progress.close()

    results.extend(reused)
    for result in results:
        result["files"] = sorted(set(occurrences[result["url"]]))
        result["occurrences"] = len(occurrences[result["url"]])
    counts = Counter(result["outcome"] for result in results)
    return {
        "checked_at": datetime.now().astimezone().isoformat(timespec="seconds"),
        "manifest": args.manifest,
        "unique_external_links": len(urls),
        "checked": len(results),
        "reused": len(reused),
        "skipped": len(skipped),
        "skip_domains": sorted(skip_domains),
        "counts": dict(sorted(counts.items())),
        "results": sorted(results, key=lambda item: (item["outcome"], item["url"])),
        "skipped_urls": skipped,
    }


def main() -> int:
    args = parse_args()
    report = asyncio.run(run(args))
    Path(args.output).write_text(
        json.dumps(report, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    print(json.dumps({key: report[key] for key in report if key != "results" and key != "skipped_urls"}, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
