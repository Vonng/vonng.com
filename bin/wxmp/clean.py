"""Clean a WeChat-exported markdown body into blog-ready Markdown."""
import re

WX_LINK = re.compile(r'https?://mp\.weixin\.qq\.com/')

CTA = [
    re.compile(r'^\**点一个关注'), re.compile(r'^\**数据库老司机点一个关注'),
    re.compile(r'^\[数据库老司机\]\([^)]*\)\s*点一个关注'),
    re.compile(r'^\**对\s*PostgreSQL.{0,20}感兴趣的朋友'),
    re.compile(r'^\**欢迎加入\s*PGSQL'), re.compile(r'^搜索\s*\**pigsty-cc'),
    re.compile(r'^微信搜\s*pigsty-cc'), re.compile(r'^非法加冯公众号二维码'),
    re.compile(r'^欢迎关注本号'), re.compile(r'^\**精彩不迷路'),
    re.compile(r'^\**扫码加群'), re.compile(r'^\**加微信\s*\S*\s*入群'),
    re.compile(r'^\**长按.{0,10}二维码'), re.compile(r'^\**关注公众号'),
]
# Headings that open a trailing "further reading" block
TAIL_HEAD = re.compile(r'^#{1,6}\s*(参考阅读|推荐阅读|往期精选|相关阅读|扩展阅读|历史文章|近期文章)\s*$')
SEP = re.compile(r'^\s*(\*\\?\*|-{3,}|\*{3,}|_{3,})\s*$')


def _is_linky(line: str) -> bool:
    """True if the line is (almost) nothing but article links.

    Tolerates the shapes WeChat 'further reading' blocks use: a leading
    ``2023-03-08`` date, and a short trailing byline after the link.
    """
    s = line.strip()
    if not s or not re.search(r'\]\((?:https?://mp\.weixin\.qq\.com|/)', s):
        return False
    residue = re.sub(r'\[[^\]]*\]\([^)]*\)', '', s)
    residue = re.sub(r'\d{4}[-/.]\d{1,2}[-/.]\d{1,2}', '', residue)
    residue = re.sub(r'[\s\\*>·、，,。|-]+', '', residue)
    return len(residue) <= 6

CONNECTOR_HEAD = re.compile(r'^#{1,6}\s*.{0,24}(参考阅读|推荐阅读|往期精选|相关阅读|扩展阅读|历史文章|近期文章|专栏|合集|系列|精选)\s*$')
SHORT_LABEL = re.compile(r'^\**[^\s\[\]()]{1,20}\**$')


def _is_connector(line: str) -> bool:
    s = line.strip()
    if not s or SEP.match(s):
        return True
    if CONNECTOR_HEAD.match(s) or TAIL_HEAD.match(s):
        return True
    if any(p.match(s) for p in CTA):
        return True
    if s.startswith('#') and len(s) <= 30:
        return True
    return bool(SHORT_LABEL.match(s)) and len(s) <= 22


def strip_tail(md: str) -> str:
    lines = md.split('\n')
    n = len(lines)
    best = None
    for i in range(n):
        region = [x for x in lines[i:] if x.strip()]
        if not region:
            continue
        linky = sum(_is_linky(x) for x in region)
        conn = sum(_is_connector(x) for x in region if not _is_linky(x))
        other = len(region) - linky - conn
        if linky >= 3 and other == 0:
            best = i
            break
    if best is not None:
        lines = lines[:best]
    return '\n'.join(lines).rstrip()


def strip_cta(md: str) -> str:
    out = []
    for ln in md.split('\n'):
        s = ln.strip()
        if any(p.match(s) for p in CTA):
            continue
        out.append(ln)
    return '\n'.join(out)


def collapse_blanks(md: str) -> str:
    md = re.sub(r'\n{3,}', '\n\n', md)
    md = re.sub(r'(?m)^\s*\*\\\*\s*$\n?', '', md)
    return md.strip() + '\n'


# Pandoc escapes literal brackets/parens as \[ \] \( \); Hugo's passthrough
# then reads those as LaTeX math delimiters and KaTeX chokes on CJK inside.
MATHY = re.compile(r'\\([\[\]()])')


def unescape_brackets(md: str) -> str:
    return MATHY.sub(r'\1', md)


def normalize_article(md: str) -> str:
    """Normalize structures that are valid in WeChat but awkward in a leaf page."""
    # The Hugo page title is the only H1; preserve source hierarchy beneath it.
    md = re.sub(r'(?m)^(#{1,5})(\s+)', lambda m: '#' + m.group(1) + m.group(2), md)
    # Pandoc sometimes preserves both a textual bullet and Markdown marker.
    md = re.sub(r'(?m)^-\s*•\s*', '- ', md)
    # Separate a bare URL immediately followed by an image.
    md = re.sub(r'(https?://[^\s!]+)(?=!\[)', r'\1\n\n', md)
    # WeChat often emits an inline image immediately followed by prose.
    md = re.sub(r'(!\[[^\]]*\]\([^)]+\))(?=\S)', r'\1\n\n', md)
    # Remove whitespace accidentally captured inside strong emphasis.
    md = re.sub(r'\*\*([^*\n]*?)\s+\*\*', r'**\1**', md)
    return collapse_blanks(md)


def clean(md: str) -> str:
    return collapse_blanks(unescape_brackets(strip_cta(strip_tail(md))))
