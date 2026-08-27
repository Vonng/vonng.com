#!/usr/bin/env python3
"""Turn curated WeChat exports into OINK page bundles."""
import argparse, json, re, sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
import clean as C
import tagrules

# translated pieces -> existing author-taxonomy slugs
AUTHORS = {
    "Andy Pavlo: 2024年度数据库回顾": ["andy-pavlo", "vonng"],
    "DHH下云：S3晚搬一天，就多花四万": ["dhh"],
}
# pieces that are translations/renderings of someone else's work
TRANSLATED = set(AUTHORS) | {
    "YC教父Paul Graham：写作者与非写作者",
    "软件3.0时代，AI带来的范式转移",
    "关于AI与人类的坦诚对话",
    "Wiz: DeepSeek数据库暴露",
}

TITLE_FIX = {
    "PostgreSQL 号外小版本发布：17.2, 16.6, 15.10, 14.15, 13.18, and 12.22":
        "PostgreSQL 号外小版本发布：17.2, 16.6, 15.10, 14.15, 13.18, 12.22",
    "阿里云：从上到下烂到根了【去除原文版】": "阿里云：从上到下烂到根了",
}


def norm_title(s: str) -> str:
    s = re.sub(r'[*_`]', '', s).strip()
    s = re.sub(r'\s+', '', s)
    return s.lower()


def build_link_map(rows, content: Path):
    """anchor-text -> local route, from existing posts and the new imports."""
    m = {}
    for p in content.rglob('index.md'):
        t = p.read_text(encoding='utf-8', errors='ignore')
        fm = re.search(r'(?ms)\A---\n(.*?)\n---', t)
        if not fm:
            continue
        ti = re.search(r'(?m)^title:\s*["\']?(.*?)["\']?\s*$', fm.group(1))
        if not ti:
            continue
        rel = p.relative_to(content).parent
        m.setdefault(norm_title(ti.group(1)), '/%s/' % rel.as_posix())
    for r in rows:
        m[norm_title(r['wx_title'])] = '/%s/%s/' % (r['section'], r['slug'])
    return m


def rewrite_links(body: str, linkmap: dict, self_route: str) -> tuple[str, int]:
    n = 0
    def sub(mo):
        nonlocal n
        text, url = mo.group(1), mo.group(2)
        if 'mp.weixin.qq.com' not in url:
            return mo.group(0)
        route = linkmap.get(norm_title(text))
        if route and route != self_route:
            n += 1
            return '[%s](%s)' % (text, route)
        return mo.group(0)
    return re.sub(r'\[([^\]]+)\]\((https?://[^)\s]+?)(?:\s+"[^"]*")?\)', sub, body), n


def rewrite_images(body: str, imap: dict) -> str:
    def sub(mo):
        alt, url = mo.group(1), mo.group(2)
        local = imap.get(url)
        if not local:
            return mo.group(0)
        return '![%s](%s)' % (alt or '', local)
    body = re.sub(r'!\[([^\]]*)\]\((https?://[^)\s]+?)(?:\s+"[^"]*")?\)', sub, body)
    # drop images we could not fetch
    body = re.sub(r'!\[[^\]]*\]\(https?://[^)\s]+\)\s*\n?', '', body)
    return body


def make_summary(digest: str, body: str, limit: int = 90) -> str:
    s = (digest or '').strip()
    s = re.sub(r'^\s*(摘要|导读|编者按)\s*[:：]?\s*', '', s)
    if not s:
        for para in body.split('\n\n'):
            p = re.sub(r'!\[[^\]]*\]\([^)]*\)', '', para)
            p = re.sub(r'\[([^\]]*)\]\([^)]*\)', r'\1', p)
            p = re.sub(r'[#>*`_\\]', '', p).strip()
            if len(p) >= 25 and not p.startswith('|'):
                s = p
                break
    s = re.sub(r'\s+', ' ', s).strip()
    if len(s) > limit:
        cut = s[:limit]
        for ch in '。！？；.!?':
            i = cut.rfind(ch)
            if i > limit * 0.5:
                return cut[:i + 1]
        s = cut.rstrip('，,、 ') + '…'
    return s


def yq(v: str) -> str:
    return '"%s"' % v.replace('\\', '\\\\').replace('"', '\\"')


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--final', required=True)
    ap.add_argument('--images', required=True)
    ap.add_argument('--content', required=True)
    ap.add_argument('--audit', required=True)
    ap.add_argument('--report', required=True)
    a = ap.parse_args()

    rows = json.load(open(a.final))
    imgs = {r['slug']: r for r in json.load(open(a.images))}
    digests = {p['wx_url']: (p.get('wx_digest') or '')
               for p in json.load(open(a.audit))['posts']}
    content = Path(a.content)
    linkmap = build_link_map(rows, content)

    report, links_total = [], 0
    for r in rows:
        src = Path(r['source_markdown']).read_text(encoding='utf-8', errors='ignore')
        fm = re.search(r'(?ms)\A---\n.*?\n---', src)
        body = src[fm.end():] if fm else src
        # User-supplied recovery files may be plain Markdown rather than an
        # exported bundle. Remove a leading duplicate title and date.
        body = re.sub(r'(?m)\A\s*#{1,2}\s*' + re.escape(r['wx_title']) + r'\s*\n+', '', body, count=1)
        body = re.sub(r'(?m)\A\s*\d{4}-\d{2}-\d{2}\s*\n+', '', body, count=1)
        body = C.clean(body)

        rec = imgs.get(r['slug'], {})
        body = rewrite_images(body, rec.get('map', {}))
        route = '/%s/%s/' % (r['section'], r['slug'])
        body, nl = rewrite_links(body, linkmap, route)
        links_total += nl
        body = C.normalize_article(body)

        title = TITLE_FIX.get(r['wx_title'], r['wx_title']).strip()
        authors = r.get('authors') or AUTHORS.get(r['wx_title'], ['vonng'])
        tags = r.get('tags') or tagrules.assign(title, body, r['section'])
        if (r['wx_title'] in TRANSLATED or r.get('translation_derived')) and '翻译' not in tags:
            tags = tags[:3] + ['翻译']
        summary = r.get('summary') or make_summary(digests.get(r['wx_url'], ''), body)

        if r.get('attribution'):
            body = '> %s · [微信公众号转载页](%s)\n\n%s' % (
                r['attribution'], r['wx_url'], body.lstrip())

        front = ['---', 'title: %s' % yq(title), 'date: %s' % r['published_at'][:10],
                 'authors: [%s]' % ', '.join(authors), 'summary: >', '  %s' % summary,
                 'tags: [%s]' % ', '.join(tags), '---', '']
        out = content / r['section'] / r['slug'] / 'index.md'
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text('\n'.join(front) + '\n' + body, encoding='utf-8')
        report.append({'slug': r['slug'], 'section': r['section'], 'title': title,
                       'tags': tags, 'summary': summary, 'links_rewritten': nl,
                       'images': rec.get('images', 0), 'featured': rec.get('featured', '')})

    Path(a.report).write_text(json.dumps(report, ensure_ascii=False, indent=1), encoding='utf-8')
    print('wrote %d posts | %d wechat links rewritten to local routes' % (len(report), links_total))


if __name__ == '__main__':
    sys.exit(main())
