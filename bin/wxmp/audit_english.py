#!/usr/bin/env python3
"""Report blog leaf bundles that intentionally or actionably lack English."""

import argparse
import csv
import json
import re
from collections import Counter, defaultdict
from pathlib import Path

import yaml


SECTIONS = ("ai", "cloud", "db", "misc", "pg", "pigsty", "trip")
SECTION_NAMES = {
    "ai": "AI", "cloud": "云计算", "db": "数据库", "misc": "杂项",
    "pg": "PostgreSQL", "pigsty": "Pigsty", "trip": "旅行",
}
INTENTIONAL = {
    "content/misc/fengzhenbiao": "仓库规范明确排除：冯振彪自传",
    "content/pg/pg-apt-loong64": "仓库规范明确排除：龙芯相关文章",
}
CATEGORY_NAMES = {
    "intentional": "规范明确不翻译",
    "translation_derived": "英文来源的翻译或改编，不回译",
    "review_external_provenance": "外部作者文章，需先核对原始语种",
    "actionable_original": "冯若航原创，后续应翻译",
    "ambiguous": "来源不清，需人工确认",
}


def front(path: Path) -> tuple[dict, str]:
    text = path.read_text(encoding="utf-8", errors="ignore")
    if not text.startswith("---\n") or "\n---\n" not in text:
        return {}, text
    raw, body = text[4:].split("\n---\n", 1)
    return yaml.safe_load(raw) or {}, body


def cell(value: object) -> str:
    return str(value or "").replace("|", "\\|").replace("\n", " ").strip()


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--repo", default=".")
    ap.add_argument("--ledger", required=True)
    ap.add_argument("--markdown", required=True)
    ap.add_argument("--csv", required=True)
    args = ap.parse_args()
    repo = Path(args.repo).resolve()
    ledger = json.loads((repo / args.ledger).read_text())
    ledger_by_bundle = {
        f"content/{x['section']}/{x['slug']}": x for x in ledger
    }
    rows = []

    for section in SECTIONS:
        for bundle in sorted((repo / "content" / section).iterdir()):
            zh = bundle / "index.md"
            if not bundle.is_dir() or not zh.exists() or (bundle / "index.en.md").exists():
                continue
            rel = bundle.relative_to(repo).as_posix()
            meta, body = front(zh)
            authors = meta.get("authors") or ([meta["author"]] if meta.get("author") else ["vonng"])
            if isinstance(authors, str):
                authors = [authors]
            tags = meta.get("tags") or []
            ledger_row = ledger_by_bundle.get(rel)

            if rel in INTENTIONAL:
                category = "intentional"
                evidence = INTENTIONAL[rel]
            elif ledger_row:
                if "翻译" in tags:
                    category = "translation_derived"
                    evidence = "导入元数据含“翻译”标签"
                elif authors != ["vonng"]:
                    category = "review_external_provenance"
                    evidence = "外部作者署名；需确认原始语种后再决定是否翻译"
                else:
                    category = "actionable_original"
                    evidence = "冯若航原创导入；尚无 index.en.md"
            else:
                explicit_translation = (
                    "翻译" in tags
                    or bool(meta.get("origin"))
                    or bool(re.search(r"译者|译评|英文原文|翻译自|【译】", body[:2500]))
                    or authors != ["vonng"]
                )
                if explicit_translation:
                    category = "translation_derived"
                    evidence = "正文、来源字段、作者或翻译标记表明源自英文内容"
                else:
                    category = "ambiguous"
                    evidence = "未发现足够的原创或翻译来源证据"

            rows.append({
                "category": category,
                "section": section,
                "date": str(meta.get("date") or "")[:10],
                "title": meta.get("title") or bundle.name,
                "authors": "、".join(str(x) for x in authors),
                "path": rel + "/index.md",
                "evidence": evidence,
            })

    rows.sort(key=lambda x: (list(CATEGORY_NAMES).index(x["category"]),
                             SECTIONS.index(x["section"]), x["date"], x["title"]))
    counts = Counter(x["category"] for x in rows)
    grouped = defaultdict(list)
    for row in rows:
        grouped[row["category"]].append(row)

    lines = [
        "# 英文版本缺口复扫",
        "",
        "> 本报告按仓库 `AGENTS.md` 的翻译政策分类；此次微信公众号导入未扩展为批量翻译任务。",
        "",
        "## 汇总",
        "",
        "| 分类 | 数量 | 当前处理 |",
        "|---|---:|---|",
    ]
    handling = {
        "intentional": "保持仅中文",
        "translation_derived": "保持仅中文，避免回译",
        "review_external_provenance": "先核对原始语种与授权",
        "actionable_original": "另开翻译任务，逐篇使用独立 SubAgent",
        "ambiguous": "请作者确认来源",
    }
    for category in CATEGORY_NAMES:
        lines.append(f"| {CATEGORY_NAMES[category]} | {counts[category]} | {handling[category]} |")
    lines.extend(["", f"合计缺少 `index.en.md`：**{len(rows)}** 篇。"])

    for category in CATEGORY_NAMES:
        if not grouped[category]:
            continue
        lines.extend([
            "", f"## {CATEGORY_NAMES[category]}", "",
            "| 日期 | 专栏 | 标题 | 作者 | 页面 | 依据 |",
            "|---|---|---|---|---|---|",
        ])
        for row in grouped[category]:
            link = f"[{cell(row['path'])}](./{row['path']})"
            lines.append(
                f"| {cell(row['date'])} | {SECTION_NAMES[row['section']]} | "
                f"{cell(row['title'])} | {cell(row['authors'])} | {link} | {cell(row['evidence'])} |"
            )
    lines.append("")
    (repo / args.markdown).write_text("\n".join(lines), encoding="utf-8")
    with (repo / args.csv).open("w", newline="", encoding="utf-8-sig") as handle:
        writer = csv.DictWriter(handle, fieldnames=[
            "category", "section", "date", "title", "authors", "path", "evidence"
        ], lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)
    print(json.dumps({"total": len(rows), "categories": counts}, ensure_ascii=False, default=dict))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
