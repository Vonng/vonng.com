#!/usr/bin/env python3
"""Apply reviewed WeChat revisions to existing page bundles with local assets."""

import argparse
import hashlib
import json
import re
import shutil
import sys
from datetime import datetime
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
import clean as C


def split_front(text: str):
    if not text.startswith("---\n") or "\n---\n" not in text:
        raise ValueError("front matter missing")
    front, body = text[4:].split("\n---\n", 1)
    return front, body.lstrip()


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--rules", required=True)
    ap.add_argument("--images", required=True)
    ap.add_argument("--content", required=True)
    ap.add_argument("--temp-section", default="wxmp-merge-tmp")
    ap.add_argument("--backup", required=True)
    ap.add_argument("--report", required=True)
    args = ap.parse_args()
    rules = json.loads(Path(args.rules).read_text())
    images = {x["slug"]: x for x in json.loads(Path(args.images).read_text())}
    content = Path(args.content)
    backup_root = Path(args.backup)
    report = []

    for rule in rules:
        target = content / rule["local_rel"]
        backup = backup_root / rule["local_rel"]
        backup.parent.mkdir(parents=True, exist_ok=True)
        if not backup.exists():
            shutil.copy2(target, backup)
        base = backup.read_text(encoding="utf-8", errors="ignore")
        front, base_body = split_front(base)
        source = Path(rule["source_markdown"]).read_text(encoding="utf-8", errors="ignore")
        _, source_body = split_front(source)
        source_body = C.normalize_article(C.clean(source_body))
        image_row = images[rule["slug"]]
        if image_row.get("failed"):
            raise SystemExit(f"failed images for {rule['wx_title']}: {image_row['failed']}")
        mapping = {}
        temp = content / args.temp_section / rule["slug"]
        target_dir = target.parent
        for url, filename in image_row.get("map", {}).items():
            outname = f"wxmp-{rule['slug']}-{filename}"
            shutil.copy2(temp / filename, target_dir / outname)
            mapping[url] = outname

        def image_sub(m):
            alt, url = m.group(1), m.group(2)
            return f"![{alt}]({mapping[url]})" if url in mapping else ""
        source_body = re.sub(r'!\[([^\]]*)\]\((https?://[^)\s]+?)(?:\s+"[^"]*")?\)', image_sub, source_body)
        source_body = C.collapse_blanks(source_body)
        note = f"> [微信公众号原文]({rule['wx_url']})\n\n"
        if rule["mode"] == "replace":
            merged_body = note + source_body
        else:
            match = re.search(rule["tail"], base_body, re.M)
            if not match:
                raise SystemExit(f"local tail not found: {rule['wx_title']}")
            merged_body = note + source_body.rstrip() + "\n\n---\n\n" + base_body[match.start():].strip() + "\n"
        merged = "---\n" + front.rstrip() + "\n---\n\n" + merged_body
        target.write_text(merged, encoding="utf-8")
        report.append({
            "wx_title": rule["wx_title"], "wx_url": rule["wx_url"],
            "target": rule["local_rel"], "mode": rule["mode"],
            "images": len(mapping), "before_sha256": hashlib.sha256(base.encode()).hexdigest(),
            "after_sha256": hashlib.sha256(merged.encode()).hexdigest(),
        })

    payload = {"generated_at": datetime.now().astimezone().isoformat(timespec="seconds"),
               "entry_count": len(report), "entries": report}
    Path(args.report).write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n")
    print(json.dumps(payload, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
