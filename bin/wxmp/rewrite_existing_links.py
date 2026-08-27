#!/usr/bin/env python3
"""Rewrite exact-title WeChat article links to imported local routes."""

import argparse
import json
import re
from pathlib import Path


def norm_title(value: str) -> str:
    value = re.sub(r"[*_`]", "", value).strip()
    return re.sub(r"\s+", "", value).lower()


LINK = re.compile(r'\[([^\]]+)\]\((https?://(?:mp\.weixin\.qq\.com|weixin\.qq\.com)/[^)\s]+?)(?:\s+"[^"]*")?\)')


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--final", required=True)
    ap.add_argument("--content", required=True)
    args = ap.parse_args()
    content = Path(args.content)
    rows = json.loads(Path(args.final).read_text())
    routes = {norm_title(r["wx_title"]): f'/{r["section"]}/{r["slug"]}/' for r in rows}
    changed_files = []
    replacements = 0

    for path in content.rglob("index*.md"):
        text = path.read_text(encoding="utf-8", errors="ignore")
        rel = path.relative_to(content)
        current = "/" + rel.parent.as_posix().strip("/") + "/"

        def replace(match: re.Match[str]) -> str:
            nonlocal replacements
            route = routes.get(norm_title(match.group(1)))
            if not route or route == current:
                return match.group(0)
            replacements += 1
            return f'[{match.group(1)}]({route})'

        updated = LINK.sub(replace, text)
        if updated != text:
            path.write_text(updated, encoding="utf-8")
            changed_files.append(path.relative_to(content).as_posix())

    print(json.dumps({"files": len(changed_files), "replacements": replacements,
                      "changed": changed_files}, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
