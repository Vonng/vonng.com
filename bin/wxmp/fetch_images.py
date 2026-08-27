#!/usr/bin/env python3
"""Download WeChat CDN images into Hugo page bundles and convert them to WebP."""
import argparse, hashlib, json, re, subprocess, sys, time, random
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path
from urllib.request import Request, urlopen
from urllib.error import HTTPError, URLError

UA = ("Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 "
      "(KHTML, like Gecko) Chrome/126.0 Safari/537.36")
CACHE = Path.home() / "www/blog/wxmp/output/image_cache"
DELAY_MIN = 3.0
DELAY_MAX = 5.0

MAGIC = [(b"\x89PNG\r\n\x1a\n", "png"), (b"GIF8", "gif"),
         (b"\xff\xd8\xff", "jpg"), (b"RIFF", "webp"), (b"BM", "bmp")]


def sniff(data: bytes) -> str:
    for sig, ext in MAGIC:
        if data.startswith(sig):
            return "webp" if ext == "webp" and data[8:12] == b"WEBP" else ext
    return ""


def fetch(url: str, tries: int = 3) -> bytes | None:
    key = hashlib.sha1(url.encode()).hexdigest()
    CACHE.mkdir(parents=True, exist_ok=True)
    hit = CACHE / key
    if hit.exists() and hit.stat().st_size > 0:
        return hit.read_bytes()
    for i in range(tries):
        try:
            req = Request(url, headers={"User-Agent": UA, "Referer": "https://mp.weixin.qq.com/"})
            with urlopen(req, timeout=30) as r:
                data = r.read()
            if data:
                hit.write_bytes(data)
                # Keep real CDN requests at a human pace. Cache hits perform no
                # network access and therefore do not need a delay.
                time.sleep(random.uniform(DELAY_MIN, DELAY_MAX))
                return data
        except (HTTPError, URLError, TimeoutError, OSError):
            if i == tries - 1:
                return None
            time.sleep(1.5 * (i + 1))
    return None


def to_webp(raw: bytes, dest: Path, ext: str) -> str | None:
    """Write raw bytes as WebP (or keep animated GIF). Returns final filename."""
    tmp = dest.with_suffix("." + ext + ".tmp")
    tmp.write_bytes(raw)
    try:
        if ext == "gif":
            out = dest.with_suffix(".gif")
            tmp.replace(out)
            return out.name
        out = dest.with_suffix(".webp")
        if ext == "webp":
            tmp.replace(out)
            return out.name
        r = subprocess.run(["cwebp", "-quiet", "-q", "82", "-metadata", "none", str(tmp), "-o", str(out)],
                           capture_output=True)
        if r.returncode != 0 or not out.exists():
            keep = dest.with_suffix("." + ("jpg" if ext == "jpg" else ext))
            tmp.replace(keep)
            return keep.name
        return out.name
    finally:
        if tmp.exists():
            tmp.unlink()


def og_image(html_path: str) -> str:
    p = Path(html_path) if html_path else None
    if not p or not p.exists():
        return ""
    head = p.read_text(encoding="utf-8", errors="ignore")[:900_000]
    for pat in (r'<meta[^>]+property=["\']og:image["\'][^>]+content=["\']([^"\']+)',
                r'<meta[^>]+content=["\']([^"\']+)["\'][^>]+property=["\']og:image["\']',
                r"msg_cdn_url\s*=\s*['\"]([^'\"]+)"):
        m = re.search(pat, head, re.I)
        if m:
            import html as H
            return H.unescape(m.group(1)).replace("http://", "https://", 1)
    return ""


def process(row, content_dir: Path, report: list):
    bundle = content_dir / row["section"] / row["slug"]
    bundle.mkdir(parents=True, exist_ok=True)
    meta_path = Path(row["source_markdown"]).with_name("metadata.json")
    meta = json.loads(meta_path.read_text(encoding="utf-8")) if meta_path.exists() else {}
    body = Path(row["source_markdown"]).read_text(encoding="utf-8", errors="ignore")

    urls = []
    for u in re.findall(r'!\[[^\]]*\]\((https?://[^\s)]+)', body):
        if u not in urls:
            urls.append(u)
    mapping, failed = {}, []
    for i, u in enumerate(urls, 1):
        raw = fetch(u)
        if not raw:
            failed.append(u); continue
        ext = sniff(raw)
        if not ext:
            failed.append(u); continue
        name = to_webp(raw, bundle / ("%02d" % i), ext)
        if name:
            mapping[u] = name
        else:
            failed.append(u)

    cover = "" if row.get("skip_featured") else (row.get("cover_url", "") or og_image(meta.get("source_html", "")))
    feat = ""
    if cover:
        raw = fetch(cover)
        if raw and sniff(raw):
            feat = to_webp(raw, bundle / "featured", sniff(raw))
    if not row.get("skip_featured") and not feat and mapping:
        first = bundle / mapping[urls[0]] if urls and urls[0] in mapping else None
        if first and first.exists():
            tgt = bundle / ("featured" + first.suffix)
            tgt.write_bytes(first.read_bytes())
            feat = tgt.name
    report.append({"slug": row["slug"], "section": row["section"], "title": row["wx_title"],
                   "images": len(mapping), "requested": len(urls),
                   "failed": failed, "featured": feat, "map": mapping})
    print("[%d] %s | images %d/%d | featured %s | failed %d" %
          (len(report), row["slug"], len(mapping), len(urls), feat or "-", len(failed)),
          flush=True)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--final", required=True)
    ap.add_argument("--content", required=True)
    ap.add_argument("--out", required=True)
    ap.add_argument("--workers", type=int, default=1)
    ap.add_argument("--delay-min", type=float, default=3.0)
    ap.add_argument("--delay-max", type=float, default=5.0)
    ap.add_argument("--limit", type=int, default=0)
    a = ap.parse_args()
    global DELAY_MIN, DELAY_MAX
    DELAY_MIN, DELAY_MAX = a.delay_min, a.delay_max
    if DELAY_MIN < 0 or DELAY_MAX < DELAY_MIN:
        raise SystemExit("invalid request delay range")
    rows = json.load(open(a.final))
    if a.limit:
        rows = rows[:a.limit]
    content = Path(a.content)
    report = []
    with ThreadPoolExecutor(max_workers=a.workers) as ex:
        list(ex.map(lambda r: process(r, content, report), rows))
    Path(a.out).write_text(json.dumps(report, ensure_ascii=False, indent=1), encoding="utf-8")
    tot = sum(r["images"] for r in report)
    req = sum(r["requested"] for r in report)
    nof = sum(1 for r in report if not r["featured"])
    print("articles %d | images %d/%d | missing featured %d" % (len(report), tot, req, nof))
    bad = [r for r in report if r["failed"]]
    print("articles with failed images: %d (%d urls)" % (len(bad), sum(len(r["failed"]) for r in bad)))


if __name__ == "__main__":
    sys.exit(main())
