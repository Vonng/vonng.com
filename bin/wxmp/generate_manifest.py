#!/usr/bin/env python3
"""Generate a per-section audit manifest for the staged WeChat import."""

import argparse
import csv
import hashlib
import json
import re
import subprocess
from collections import Counter, defaultdict
from pathlib import Path

import yaml


SECTIONS = ("ai", "cloud", "db", "misc", "pg", "pigsty", "trip")
SECTION_NAMES = {
    "ai": "AI",
    "cloud": "云计算",
    "db": "数据库",
    "misc": "杂项",
    "pg": "PostgreSQL",
    "pigsty": "Pigsty",
    "trip": "旅行",
}


def git(*args: str, cwd: Path, check: bool = True) -> subprocess.CompletedProcess:
    return subprocess.run(
        ["git", *args], cwd=cwd, check=check, capture_output=True, text=False
    )


def front_matter(path: Path) -> dict:
    text = path.read_text(encoding="utf-8", errors="ignore")
    if not text.startswith("---\n") or "\n---\n" not in text:
        return {}
    raw = text[4:].split("\n---\n", 1)[0]
    return yaml.safe_load(raw) or {}


def base_blob(repo: Path, base: str, rel: str) -> bytes | None:
    result = git("show", f"{base}:{rel}", cwd=repo, check=False)
    return result.stdout if result.returncode == 0 else None


def author_names(repo: Path) -> dict[str, str]:
    result = {"vonng": "冯若航"}
    root = repo / "content/authors"
    for path in root.glob("*/_index.md"):
        result[path.parent.name] = str(front_matter(path).get("title") or path.parent.name)
    return result


def clean_cell(value: object) -> str:
    return str(value or "").replace("|", "\\|").replace("\n", " ").strip()


def tree_hashes(root: Path) -> dict[str, str]:
    return {
        path.relative_to(root).as_posix(): hashlib.sha256(path.read_bytes()).hexdigest()
        for path in sorted(root.rglob("*")) if path.is_file()
    }


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--repo", default=".")
    ap.add_argument("--base", default="main")
    ap.add_argument("--production-worktree", required=True)
    ap.add_argument("--ledger", required=True)
    ap.add_argument("--merge-report", required=True)
    ap.add_argument("--markdown", required=True)
    ap.add_argument("--csv", required=True)
    args = ap.parse_args()

    repo = Path(args.repo).resolve()
    production = Path(args.production_worktree).resolve()
    ledger = json.loads((repo / args.ledger).read_text())
    merge_report = json.loads((repo / args.merge_report).read_text())
    merge_by_path = {
        f"content/{row['target']}": row for row in merge_report["entries"]
    }
    names = author_names(repo)
    rows: list[dict] = []
    ledger_paths: set[str] = set()

    for item in ledger:
        rel = f"content/{item['section']}/{item['slug']}/index.md"
        path = repo / rel
        if not path.exists():
            raise SystemExit(f"ledger bundle missing: {rel}")
        if base_blob(repo, args.base, rel) is not None:
            raise SystemExit(f"ledger entry already exists on {args.base}: {rel}")
        ledger_paths.add(rel)
        authors = item.get("authors") or ["vonng"]
        author_text = "、".join(names.get(x, x) for x in authors)
        provenance = "原创" if authors == ["vonng"] else "原作者署名"
        rows.append(
            {
                "section": item["section"],
                "date": str(item.get("date") or ""),
                "action": f"新增 · {provenance}",
                "scope": "wxmp_import",
                "title": item["title"],
                "authors": author_text,
                "path": rel,
                "images": int(item.get("images") or 0),
                "featured": item.get("featured") or "",
                "source_url": item.get("wx_url") or "",
                "note": "独立页面包",
            }
        )

    for section in SECTIONS:
        for path in sorted((repo / "content" / section).glob("*/index.md")):
            rel = path.relative_to(repo).as_posix()
            if rel in ledger_paths:
                continue
            before = base_blob(repo, args.base, rel)
            if before is None:
                source_bundle = production / path.relative_to(repo).parent
                if not source_bundle.is_dir() or tree_hashes(source_bundle) != tree_hashes(path.parent):
                    raise SystemExit(f"unclassified or divergent new bundle outside WXMP ledger: {rel}")
                meta = front_matter(path)
                authors = meta.get("authors") or ["vonng"]
                if isinstance(authors, str):
                    authors = [authors]
                author_text = "、".join(names.get(x, x) for x in authors)
                text = path.read_text(encoding="utf-8", errors="ignore")
                refs = set(re.findall(r'!\[[^\]]*\]\(([^)\s]+)', text))
                local = [x for x in refs if not x.startswith(("http://", "https://", "data:", "/"))]
                feature = next((x.name for x in path.parent.glob("featured.*")), "")
                body_images = [x for x in local if x != feature]
                rows.append(
                    {
                        "section": section,
                        "date": str(meta.get("date") or "")[:10],
                        "action": "新增 · 生产叠加",
                        "scope": "production_overlay",
                        "title": meta.get("title") or path.parent.name,
                        "authors": author_text,
                        "path": rel,
                        "images": len(body_images),
                        "featured": feature,
                        "source_url": "",
                        "note": "保留生产 worktree 原有未跟踪页面包；不计入公众号 684 篇审计",
                    }
                )
                continue
            if before == path.read_bytes():
                continue
            meta = front_matter(path)
            authors = meta.get("authors") or ["vonng"]
            if isinstance(authors, str):
                authors = [authors]
            author_text = "、".join(names.get(x, x) for x in authors)
            if rel in merge_by_path:
                detail = merge_by_path[rel]
                action = "修改 · 正文合并"
                note = f"{detail['mode']}；新增 {detail['images']} 张本地正文图"
                images = int(detail["images"])
            elif rel == "content/pigsty/v4.2/index.md":
                action = "修改 · 版本追加"
                note = "追加 Pigsty v4.2.2 更新；3 张本地正文图"
                images = 3
            else:
                action = "修改 · 链接本地化"
                note = "公众号文章链接改为本地博客路由"
                images = 0
            rows.append(
                {
                    "section": section,
                    "date": str(meta.get("date") or "")[:10],
                    "action": action,
                    "scope": "wxmp_update",
                    "title": meta.get("title") or path.parent.name,
                    "authors": author_text,
                    "path": rel,
                    "images": images,
                    "featured": "",
                    "source_url": merge_by_path.get(rel, {}).get("wx_url", ""),
                    "note": note,
                }
            )

    rows.sort(key=lambda x: (SECTIONS.index(x["section"]), x["date"], x["title"]))
    counts = Counter((x["section"], x["scope"]) for x in rows)
    grouped: dict[str, list[dict]] = defaultdict(list)
    for row in rows:
        grouped[row["section"]].append(row)

    base_sha = git("rev-parse", "--short", args.base, cwd=repo).stdout.decode().strip()
    head_sha = git("rev-parse", "--short", "HEAD", cwd=repo).stdout.decode().strip()
    wxmp_new_count = sum(1 for x in rows if x["scope"] == "wxmp_import")
    overlay_count = sum(1 for x in rows if x["scope"] == "production_overlay")
    new_count = wxmp_new_count + overlay_count
    modified_count = sum(1 for x in rows if x["scope"] == "wxmp_update")
    lines = [
        "# 微信公众号文章导入变更清单",
        "",
        f"> 对比基线：`{args.base}` (`{base_sha}`)；测试分支：`{head_sha}` + 当前工作区。",
        "> 本表按文章页面包计数；同一页面包的中英文文件与图片资源不重复计数。",
        "",
        "## 汇总",
        "",
        f"- 公众号新增文章：**{wxmp_new_count}** 篇",
        f"- 保留生产 worktree 未跟踪文章：**{overlay_count}** 篇",
        f"- 相对 `main` 新增合计：**{new_count}** 篇",
        f"- 修改既有文章：**{modified_count}** 篇",
        f"- 合计涉及：**{len(rows)}** 篇",
        "",
        "| 专栏 | 公众号新增 | 生产叠加 | 修改 | 合计 |",
        "|---|---:|---:|---:|---:|",
    ]
    for section in SECTIONS:
        wxmp_new = counts[(section, "wxmp_import")]
        overlay = counts[(section, "production_overlay")]
        modified = counts[(section, "wxmp_update")]
        lines.append(f"| {SECTION_NAMES[section]} | {wxmp_new} | {overlay} | {modified} | {wxmp_new + overlay + modified} |")

    for section in SECTIONS:
        lines.extend(
            [
                "",
                f"## {SECTION_NAMES[section]}",
                "",
                "| 日期 | 变更 | 标题 | 作者 | 页面包 | 图片 | 说明 |",
                "|---|---|---|---|---|---:|---|",
            ]
        )
        for row in grouped[section]:
            link = f"[{clean_cell(row['path'])}](./{row['path']})"
            image_text = str(row["images"])
            if row["featured"]:
                image_text += "+封面"
            lines.append(
                "| {date} | {action} | {title} | {authors} | {path} | {images} | {note} |".format(
                    date=clean_cell(row["date"]),
                    action=clean_cell(row["action"]),
                    title=clean_cell(row["title"]),
                    authors=clean_cell(row["authors"]),
                    path=link,
                    images=clean_cell(image_text),
                    note=clean_cell(row["note"]),
                )
            )
    lines.extend(
        [
            "",
            "## 口径说明",
            "",
            "- “新增 · 原作者署名”表示转载文章使用原作者身份，不归到冯若航名下。",
            "- “正文合并”仅用于六篇用户确认应并入既有页面的文章；三篇用户指定内容已保留为独立页面包。",
            "- “链接本地化”只替换能够按标题确定目标的公众号文章链接，不改正文观点。",
            "- “生产叠加”是生产 worktree 原有但尚未提交的页面包，为测试真实合并结果而只读复制进测试副本；不计入公众号 684 篇核对。",
            "- 完整的逐篇收录、排除和转载复审依据见 `WXMP-EDITORIAL-REVIEW.md`。",
            "",
        ]
    )
    (repo / args.markdown).write_text("\n".join(lines), encoding="utf-8")

    fieldnames = [
        "section", "date", "action", "scope", "title", "authors", "path",
        "images", "featured", "source_url", "note",
    ]
    with (repo / args.csv).open("w", newline="", encoding="utf-8-sig") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames, lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)
    print(json.dumps({"wxmp_new": wxmp_new_count, "production_overlay": overlay_count,
                      "new": new_count, "modified": modified_count, "total": len(rows)}, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
