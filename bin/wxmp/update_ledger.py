#!/usr/bin/env python3
"""Append a verified WXMP import batch to the tracked provenance ledger."""

import argparse
import json
from pathlib import Path


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--ledger", required=True)
    ap.add_argument("--final", required=True)
    ap.add_argument("--posts", required=True)
    args = ap.parse_args()
    ledger_path = Path(args.ledger)
    ledger = json.loads(ledger_path.read_text())
    final = json.loads(Path(args.final).read_text())
    posts = {x["slug"]: x for x in json.loads(Path(args.posts).read_text())}
    by_url = {str(x.get("wx_url") or ""): x for x in ledger}

    added = 0
    updated = 0
    for row in final:
        url = str(row["wx_url"])
        post = posts[row["slug"]]
        item = {
            "date": str(row["published_at"])[:10],
            "section": row["section"],
            "slug": row["slug"],
            "title": post["title"],
            "authors": row.get("authors") or ["vonng"],
            "tags": post["tags"],
            "wx_url": url,
            "images": post["images"],
            "featured": post["featured"],
        }
        if url in by_url:
            prior = by_url[url]
            prior.clear()
            prior.update(item)
            updated += 1
        else:
            ledger.append(item)
            by_url[url] = item
            added += 1

    ledger.sort(key=lambda x: (str(x.get("date") or ""), str(x.get("title") or "")))
    slugs = [str(x.get("slug") or "") for x in ledger]
    urls = [str(x.get("wx_url") or "") for x in ledger]
    if len(slugs) != len(set(slugs)) or len(urls) != len(set(urls)):
        raise SystemExit("ledger contains duplicate slug or URL")
    ledger_path.write_text(json.dumps(ledger, ensure_ascii=False, indent=1) + "\n")
    print(json.dumps({"added": added, "updated": updated, "total": len(ledger)}, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
