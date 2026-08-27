#!/usr/bin/env python3
"""Append a generated WXMP page body as a versioned update to an existing page."""

import argparse
import re
from pathlib import Path


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--source-page", required=True)
    ap.add_argument("--target-page", required=True)
    ap.add_argument("--source-url", required=True)
    ap.add_argument("--heading", required=True)
    ap.add_argument("--image-prefix", required=True)
    args = ap.parse_args()
    source = Path(args.source_page).read_text(encoding="utf-8")
    target_path = Path(args.target_page)
    target = target_path.read_text(encoding="utf-8")
    marker = f'<!-- wxmp-update:{args.source_url} -->'
    if marker in target:
        print("already appended")
        return 0
    parts = source.split("\n---\n", 1)
    if len(parts) != 2:
        raise SystemExit("source page front matter missing")
    body = parts[1].lstrip()
    body = re.sub(r'\]\((\d{2}\.webp)\)', lambda m: f']({args.image_prefix}{m.group(1)})', body)
    # The update heading becomes H2, so source headings descend one level.
    body = re.sub(r'(?m)^(#{2,5})(\s+)', lambda m: '#' + m.group(1) + m.group(2), body)
    appended = (target.rstrip() + f'\n\n---\n\n{marker}\n## {args.heading}\n\n'
                f'> [微信公众号原文]({args.source_url})\n\n' + body.rstrip() + '\n')
    target_path.write_text(appended, encoding="utf-8")
    print("appended")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
