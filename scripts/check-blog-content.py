#!/usr/bin/env python3
"""Check every blog language version without modifying it.

Requires PyYAML and markdown-it-py; rendered checks also use BeautifulSoup.
Run with --public-dir after a Hugo build to check visible markup and assets.
"""

from __future__ import annotations

import argparse
import json
import re
from collections import Counter
from pathlib import Path
from urllib.parse import unquote, urljoin, urlsplit

import yaml
from markdown_it import MarkdownIt


SECTIONS = ("ai", "cloud", "db", "misc", "pg", "pigsty", "trip")


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--content-dir", type=Path, default=Path("content"))
    ap.add_argument("--public-dir", type=Path)
    ap.add_argument("--report", type=Path)
    args = ap.parse_args()
    parser = MarkdownIt("commonmark", {"html": True}).enable("table")
    findings: list[dict] = []
    pages = sorted(p for s in SECTIONS for p in (args.content_dir / s).glob("*/index*.md"))
    counts: Counter = Counter()

    def fail(path: Path, line: int, kind: str, detail: str) -> None:
        findings.append({"path": str(path), "line": line, "kind": kind, "detail": detail})

    for path in pages:
        text = path.read_text(encoding="utf-8")
        front = re.match(r"\A---\n(.*?)\n---(?:\n|$)", text, re.S)
        if not front:
            fail(path, 1, "front_matter", "Missing YAML front matter")
            continue
        try:
            meta = yaml.safe_load(front[1])
        except yaml.YAMLError as exc:
            fail(path, 1, "front_matter", str(exc))
            continue
        for key in ("title", "date", "tags"):
            if not meta.get(key):
                fail(path, 1, "front_matter", f"Missing {key}")
        if not meta.get("authors"):
            counts["without_explicit_authors"] += 1
        body = text[front.end():]
        offset = text[:front.end()].count("\n")
        lines = body.splitlines()
        tokens = parser.parse(body)
        protected: set[int] = set()
        for i, token in enumerate(tokens[:-1]):
            if token.type == "list_item_open" and tokens[i + 1].type == "list_item_close" and token.map:
                fail(path, token.map[0] + offset + 1, "empty_list_item", "List item has no content")
        previous_heading = 1
        for token in tokens:
            line = (token.map[0] if token.map else 0) + offset + 1
            if token.type in {"fence", "code_block"} and token.map:
                protected.update(range(*token.map))
                counts["code_blocks"] += 1
                if token.type == "fence":
                    start, end = token.map
                    marker = re.search(r"(`{3,}|~{3,})", lines[start])[1]
                    closing = r"\s*" + re.escape(marker[0]) + "{" + str(len(marker)) + r",}\s*"
                    if end == len(lines) and not re.fullmatch(closing, lines[-1]):
                        fail(path, line, "code_fence", "Unclosed code fence")
                    if not token.info.strip():
                        fail(path, line, "code_fence", "Code fence has no language")
            if token.type == "heading_open" and token.level == 0:
                level = int(token.tag[1:])
                if level == 1 or level > previous_heading + 1:
                    fail(path, line, "heading_level", f"H{previous_heading} to H{level}")
                previous_heading = level
            if token.type == "hr" and token.level == 0:
                counts["horizontal_rules"] += 1
                start, end = token.map
                before = start - 1
                while before >= 0 and not lines[before].strip():
                    before -= 1
                after = end
                while after < len(lines) and not lines[after].strip():
                    after += 1
                neighbors = [lines[before] if before >= 0 else "", lines[after] if after < len(lines) else ""]
                if before < 0 or after == len(lines) or any(re.match(r"^#{1,6}\s", x) for x in neighbors):
                    fail(path, line, "redundant_rule", "Horizontal rule at an article edge or next to a heading")
            for child in token.children or []:
                if child.type == "image":
                    counts["images"] += 1
                    if not child.content.strip():
                        fail(path, line, "image_alt", "Image has no alternative text")
                if child.type in {"image", "link_open"}:
                    target = child.attrGet("src" if child.type == "image" else "href") or ""
                    parsed = urlsplit(target)
                    if parsed.scheme in {"http", "https"} and not parsed.netloc:
                        fail(path, line, "invalid_url", target)
        prose = "\n".join(x for i, x in enumerate(lines) if i not in protected)
        definitions = set(re.findall(r"^\s*\[\^([^]]+)\]:", prose, re.M))
        references = set(re.findall(r"(?<!\\)\[\^([^]]+)\]", prose))
        for reference in sorted(references - definitions):
            fail(path, 1, "footnote", f"Undefined footnote {reference}")
        for i, source in enumerate(lines):
            if i in protected:
                continue
            if re.fullmatch(r"\s*#{1,6}\s*", source):
                fail(path, i + offset + 1, "empty_heading", source)
            if re.match(r"^\s*\d+\.(?:\*\*|\[|[\u4e00-\u9fffA-Za-z])", source):
                fail(path, i + offset + 1, "list_marker", "Ordered list marker needs a space")
            if "xXXXXX" in source:
                fail(path, i + offset + 1, "placeholder", source)
            if re.search(r"[\x00-\x08\x0b\x0c\x0e-\x1f\x7f]", source):
                fail(path, i + offset + 1, "control_character", "Imported control character in prose")
            if "[???]" in source:
                fail(path, i + offset + 1, "placeholder", "Unfinished link label")
        if args.public_dir:
            from bs4 import BeautifulSoup

            relative = path.relative_to(args.content_dir)
            prefix = "en/" if path.name == "index.en.md" else ""
            route = "/" + prefix + relative.parent.as_posix() + "/"
            page = args.public_dir / route.lstrip("/") / "index.html"
            if not page.is_file():
                counts["unpublished_pages"] += 1
                continue
            counts["rendered_pages"] += 1
            document = BeautifulSoup(page.read_text(), "html.parser")
            content = document.select_one(".td-content")
            if not content:
                fail(path, 1, "rendered_content", "Rendered article body is missing")
                continue
            for image in content.select("img[src]"):
                if not image.get("alt", "").strip() and not image.find_parent(class_="td-byline__author") and image.get("role") != "presentation" and image.get("aria-hidden") != "true":
                    fail(path, 1, "image_alt", "Rendered image has no alternative text: " + image["src"])
                parsed = urlsplit(image["src"])
                if not parsed.scheme and not parsed.netloc:
                    target = args.public_dir / unquote(urlsplit(urljoin(route, image["src"])).path).lstrip("/")
                    if not target.is_file():
                        fail(path, 1, "image_file", image["src"])
            for element in content.select("pre, code, script, style, .katex, .td-share"):
                element.decompose()
            for literal in content.find_all(string=re.compile(r"(?<!\*)\*\*(?!\*)|\]\((?:/|https?://)")):
                fail(path, 1, "visible_markup", str(literal).strip()[:180])

    report = {"article_files": len(pages), "counts": dict(counts), "issues": findings}
    if args.report:
        args.report.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n")
    for finding in findings:
        print(f"{finding['path']}:{finding['line']}: {finding['kind']}: {finding['detail']}")
    print(f"Checked {len(pages)} article files; {len(findings)} issues")
    return bool(findings)


if __name__ == "__main__":
    raise SystemExit(main())
