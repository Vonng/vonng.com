#!/usr/bin/env python3
"""Reclassify WXMP exclusions by editorial value and prepare imports."""

from __future__ import annotations

import argparse
import csv
import html
import json
import re
from collections import Counter
from datetime import datetime
from pathlib import Path
from typing import Any, Dict, List


EXCLUDE_REPRINT = {
    "奇绩创坛 2022 春季创业营路演日，全球 54 个项目，100%技术驱动": "创业项目路演目录，时效性与广告属性强",
    "天翼云API中的鸡鸡ID": "正文极短的低价值段子",
    "HOW 2026：国内2026年最高规格PostgreSQL 大会！": "大会报名与日程广告",
    "又一个开源pg备份工具pgBackRest倒下了": "仅 38 字与两张图片，缺少实质正文",
    "全球视角！PG 30 周年系列直播活动已开启！本周四第一期！": "直播活动广告",
    "PostgreSQL国际社区APT仓库支持龙芯CPU架构纪实": "同一事件已由 content/pg/pg-apt-loong64 完整覆盖",
}

INDEPENDENT = {
    "本号收到美团投诉：美团没有存储外卡CVV等敏感信息": ("cloud", "meituan-cvv-complaint", ["vonng"], ["云计算", "安全", "社会观察"]),
    "这次数据库真爆炸了，但摇人也没用了": ("db", "database-really-exploded", ["vonng"], ["数据库", "备份", "故障复盘"]),
    "Linus关于踢出毛子维护者的解释": ("misc", "linus-russia-maintainers", ["vonng"], ["Linux", "开源", "社会观察"]),
}

EXTRA_KEEP = {
    "有史以来最大的中国数据泄露：逾40亿条支付宝微信数据":
        ("cloud", "china-4b-data-leak", ["vonng"], ["云计算", "安全", "社会观察"]),
    "Oink: 用Markdown快速创建美观的现代网站":
        ("ai", "oink-intro", ["vonng"], ["Oink", "文档", "开源"]),
}

SLUGS = {
    "Paul Graham：这个时代更有效的财富创造路径 | 奇绩分享": "paul-graham-wealth-creation",
    "陆奇：怎么理解企业服务市场的数字化应用生态？": "luqi-enterprise-software",
    "你怎么还在招聘DBA?": "no-more-dba",
    "开源不是大杀器，免费才是": "open-source-vs-free",
    "MySQL：这个星球最成功的数据库": "mysql-most-successful-db",
    "云厂商眼中的客户：又穷又闲又缺爱": "cloud-customers-poor-bored-lonely",
    "互联网故障背后的草台班子们": "amateur-internet-outages",
    "没错，数据库确实应该放入 K8s 里！": "database-in-k8s-counterpoint",
    "卡在政企客户门口的阿里云": "aliyun-enterprise-market",
    "门内的国企如何看门外的云厂商": "state-owned-enterprise-cloud-view",
    "互联网技术大师速成班": "internet-tech-masterclass",
    "阿里云降价背后折射出的绝望": "aliyun-price-cut-despair",
    "迷失在阿里云的年轻人": "lost-youth-at-aliyun",
    "公有云厂商卖的云计算到底是什么玩意？": "what-public-cloud-sells",
    "牙膏云？您可别吹捧云厂商了": "toothpaste-cloud",
    "你用的公有云都没做过测试": "public-cloud-untested",
    "腾讯云/阿里云故障背后：投入不足": "cloud-outage-underinvestment",
    "为什么我们的云老是故障": "why-cloud-keeps-failing",
    "腾讯真的走通云原生之路了吗？": "tencent-cloud-native",
    "包年包月的云还能叫云原生吗？": "prepaid-cloud-native",
    "灿灿荐书：《收获，不止 SQL 优化》": "harvest-sql-tuning",
    "为什么这两年的舆论战，云厂商总是节节败退": "cloud-pr-war",
    "云计算：菜就是一种原罪": "cloud-incompetence",
    "资本拔苗助长的软件服务": "venture-capital-software",
    "数据库迁移工具箱，DBA老鸟的五金店": "database-migration-toolbox",
    "性学家，化学家，软件行业里的废话文学家": "nonsense-writers",
    "duckdb_fdw v1.0.0来了，第13届 PostgreSQL 中国技术大会见": "duckdb-fdw-1-0",
    "DBA不是数据库的用户，开发者才是！": "developers-are-db-users",
    "数据库的“萝卜快跑”时刻已到，DBA 请下车": "dba-get-off",
    "基础架构部不死，只是慢慢消逝": "infra-department-fading",
    "基础架构部，还有必要吗？": "need-infra-team",
    "如果 Oracle 都不能在 JAVA 上赚钱，基础软件不如不做": "oracle-java-software-business",
    "基础架构部需要先进技术吗？": "infra-needs-advanced-tech",
    "基础架构，路在何方？": "infra-road-ahead",
    "基础架构部，真的没有必要了么？": "infra-team-needed",
    "记一次阿里云 DCDN 加速仅 32 秒就欠了 1600 的问题处理（扯皮）。": "aliyun-dcdn-bill",
    "究竟是谁在卡脖子？": "who-chokes-us",
    "中国的开源运动再次到了十字路口": "china-open-source-crossroads",
    "中译版《PostgreSQL 14 Internals》上线": "pg14-internals-cn",
    "为什么云厂商销售只会打折？": "cloud-sales-discount",
    "如何通过远离 AWS 将年服务器费用从 100 万降至 20 万": "leave-aws-save-80-percent",
    "API 是云服务的灵魂": "api-soul-of-cloud",
    "SRE过气了吗": "sre-outdated",
    "互联网转向区级数据中心：一场静默的技术迁徙": "district-datacenters",
    "抄袭代码就是偷东西，抖音别狡辩了": "code-plagiarism-is-theft",
    "全民DeepSeek行为艺术观察": "deepseek-performance-art",
    "HTAP数据库，一场无人鼓掌的演出": "htap-no-applause",
    "特大新闻, Oracle强劲对手宣布开源！": "oracle-competitor-open-source",
    "云计算不能做成云算计之一：云行贿必须清理": "cloud-bribery",
    "影视飓风达芬奇千万级数据库演化及实践": "davinci-database",
    "PostgreSQL + 组播，有希望成为下一个被收购的 neon 吗？": "postgres-multicast",
    "硬编码密码泄漏，阿里云的软件工程也太差了": "aliyun-hardcoded-password",
    "再见MySQL，你好PG": "goodbye-mysql-hello-pg",
    "中国，AI 技术的企业级应用创业前景茫然": "china-ai-enterprise",
    "荣幸！小小的Get 笔记居然被腾讯举报了": "get-notes-tencent-report",
    "阿里的qwen code太草率了": "qwen-code-rushed",
    "Gojek 搬家记：腾讯云产品团队的缺位": "gojek-leaves-tencent-cloud",
    "聚焦六大功能：PostgreSQL 18 新特性深度解析": "pg18-six-features",
    "把运维干掉不是开玩笑，用AI试了试4小时搞定3天活": "ai-kills-ops",
    "云厂商需要有人管起来，CloudFlare又宕机了": "regulate-cloudflare",
    "Forward Deployed Engineer —— 硅谷版\"交付工程师\"": "fde-silicon-valley",
    "MySQL赢了2000s，PostgreSQL赢得2020s，谁将赢得AI时代？——数据库选型的三要素分析法": "db-choice-ai-era",
    "阿里云解决方案团队，雄起来!": "aliyun-solutions-team",
    "深入解析：元旦当天华为高斯数据库BUG，搞摊中国银行APP": "gaussdb-bank-of-china-outage",
    "学习PingCAP，打造你公司的AI原生软件开发团队": "pingcap-ai-team",
    "震惊！它改成阿帕奇开源协议了，不怕被云厂商“白嫖”吗？": "pigsty-apache-license",
    "你用AI生成的每一行UI代码，可能都是在给人类文明拖后腿": "ai-ui-civilization",
    "扯淡的一人公司OPC：团队AI转型才是正道": "opc-ai-transformation",
    "从 KV Cache 到 AI 内存系统：大模型推理架构的演进": "kv-cache-memory-system",
    "智能的骨架：关注、表征、学习、预测与协同": "skeleton-of-intelligence",
    "MinIO 发布10分安全漏洞": "minio-critical-vulnerability",
}

AUTHOR_SLUGS = {
    "陆奇": "lu-qi", "马工在瑞典": "ma-gong", "瑞典马工": "ma-gong", "马工": "ma-gong",
    "老头头": "laotoutou", "破产码农": "jiang-chengyao", "fanux": "fanux",
    "思维南人": "leo", "思维男人": "siwei-nanren", "会说话的波吉": "boji",
    "冷技术热思考": "cold-tech", "周新宇": "zhou-xinyu", "vage_lv": "vage", "VAGE": "vage",
    "王小瑞": "wang-xiaorui", "xiongcc": "xiongcc", "titi": "titi",
    "詹姆斯邦德007": "james-bond-007", "alitrack": "alitrack", "李令辉": "li-linghui",
    "程序员Aike": "aike", "诗语": "shiyu", "魏永明": "wei-yongming", "刘俊夏": "liu-junxia",
    "巫师小猪": "wizard-pig", "digoal": "digoal", "龚锐": "gong-rui", "快刀青衣": "kuaidao-qingyi",
    "马驰": "ma-chi", "IvorySQL": "ivorysql", "陈明": "chen-ming", "xieydd": "xieydd",
    "视觉即世界": "visual-is-world", "白小安": "bai-xiaoan",
}

TITLE_AUTHOR = {
    "Paul Graham：这个时代更有效的财富创造路径 | 奇绩分享": "paul-graham",
    "MySQL：这个星球最成功的数据库": "jiang-chengyao",
    "门内的国企如何看门外的云厂商": "leo",
}

TITLE_SECTION = {
    "数据库迁移工具箱，DBA老鸟的五金店": "db",
    "震惊！它改成阿帕奇开源协议了，不怕被云厂商“白嫖”吗？": "pigsty",
}

AUTHOR_PROFILES = {
    "paul-graham": ("Paul Graham", "Y Combinator 联合创始人，《黑客与画家》作者"),
    "lu-qi": ("陆奇", "奇绩创坛创始人，前微软全球执行副总裁"),
    "ma-gong": ("瑞典马工", "旅居瑞典的研发工程师，云计算与基础设施评论者"),
    "laotoutou": ("老头头", "软件与开源商业评论者"),
    "jiang-chengyao": ("姜承尧", "数据库从业者，公众号“破产码农”作者"),
    "fanux": ("fanux", "Sealos 创始人，云原生与 Kubernetes 工程师"),
    "leo": ("Leo（思维南人）", "企业 IT 与云计算评论者"),
    "siwei-nanren": ("思维男人", "基础设施与软件工程评论者"),
    "boji": ("会说话的波吉", "科技与软件行业评论者"),
    "cold-tech": ("冷技术热思考", "云计算与基础设施评论者"),
    "zhou-xinyu": ("周新宇", "云计算与基础设施作者"),
    "vage": ("VAGE", "基础设施与可靠性作者"),
    "wang-xiaorui": ("王小瑞", "云原生与基础设施作者"),
    "xiongcc": ("熊灿灿", "PostgreSQL 社区作者与技术译者"),
    "titi": ("titi", "云计算与基础设施评论者"),
    "james-bond-007": ("詹姆斯邦德007", "数据库迁移与运维作者"),
    "alitrack": ("alitrack", "PostgreSQL 与 DuckDB 社区作者"),
    "li-linghui": ("李令辉", "基础设施与数据库评论者"),
    "aike": ("程序员 Aike", "软件工程与基础设施作者"),
    "shiyu": ("诗语", "云计算用户与技术作者"),
    "wei-yongming": ("魏永明", "开源软件与产业观察者"),
    "liu-junxia": ("刘俊夏", "云计算成本与基础设施作者"),
    "wizard-pig": ("巫师小猪", "互联网基础设施作者"),
    "digoal": ("digoal", "PostgreSQL 专家与技术布道者"),
    "gong-rui": ("龚锐", "数据库与工程实践作者"),
    "kuaidao-qingyi": ("快刀青衣", "互联网产品与技术作者"),
    "ma-chi": ("马驰", "软件工程与 AI 编程作者"),
    "ivorysql": ("IvorySQL", "开源 Oracle 兼容 PostgreSQL 社区"),
    "chen-ming": ("陈明", "AI 与运维实践作者"),
    "xieydd": ("xieydd", "大模型推理系统作者"),
    "visual-is-world": ("视觉即世界", "人工智能与认知科学作者"),
    "bai-xiaoan": ("白小安", "对象存储与安全作者"),
}

USER_SOURCES = [
    {
        "wx_url": "https://mp.weixin.qq.com/s/5z3jUV8CrKPinUYzOnlC6g", "wx_title": "Oracle云大翻车：传6百万用户认证数据泄漏",
        "published_at": "2025-03-29T09:01:00+08:00", "section": "cloud", "provenance": "original",
        "conversion_status": "user_source", "source_markdown": "/Users/vonng/wechat/oracle-leak.md", "slug": "oracle-cloud-leak",
        "cover_url": "https://mmbiz.qpic.cn/mmbiz_jpg/Wkpr3rA9wF2eCVjyPy6814UCTibRoSyREZqCRUjW2VhlLh6ibBkVvQPM6v5pQQ4Rwtojoc9ZxTCIGkRHtDVKDWLw/0?wx_fmt=jpeg",
        "authors": ["vonng"], "tags": ["Oracle", "云计算", "安全"], "decision": "keep_user_source",
    },
    {
        "wx_url": "http://mp.weixin.qq.com/s?__biz=MzU5ODAyNTM5Ng==&tempkey=MTM2MF9GV3ZJc213V3pyVWdXSEtTdkJzOE1KVGFkajgtYUpwNDFqRnFMZktDUTlDYUFEYjc2WVJlcUpNZ0c1ZkE3MHdvT2pMdVZSUllOWXI0VUF0WlVDUXdFRXVlU3hlc3JwMmRlZUdqUmo5TjMxS0lSdjRnbVN2QWlSUGxUYm41OHRKbHY0LTRTVkJyRXVRSlBMNWpMR2M0NkVMd3MxNEQ4OHNPbnVYcGlnfn4%3D&chksm=fe4b3780c93cbe9615f8ecd7e2276e5e910ee56b1cfdb0c2cc08b121b636cdc0dd2be42d5ef0#rd",
        "wx_title": "撸一下官方疫情数据", "published_at": "2020-02-12T01:48:11+08:00", "section": "misc",
        "provenance": "original", "conversion_status": "user_source", "source_markdown": "/Users/vonng/wechat/covid-official-data.md",
        "slug": "covid-official-data", "cover_url": "https://mmbiz.qlogo.cn/mmbiz_jpg/Wkpr3rA9wF24Wicawyib36IwngXDn9ETwjDKicOJfZzLJ7ibsoluXPYSo7K1Or5ianLEckv5u6cUMra109fgX0MhTyQ/0?wx_fmt=jpeg",
        "authors": ["vonng"], "tags": ["数据分析", "社会观察"], "decision": "keep_user_source",
    },
]


def parse_args() -> argparse.Namespace:
    p = argparse.ArgumentParser()
    p.add_argument("--curation", required=True)
    p.add_argument("--markdown-manifest", required=True)
    p.add_argument("--ledger", required=True)
    p.add_argument("--content", required=True)
    p.add_argument("--out-final", required=True)
    p.add_argument("--out-json", required=True)
    p.add_argument("--out-md", required=True)
    p.add_argument("--out-csv", required=True)
    p.add_argument("--write-authors", action="store_true")
    return p.parse_args()


def og_author(path: str) -> str:
    p = Path(path) if path else None
    if not p or not p.exists():
        return ""
    head = p.read_text(encoding="utf-8", errors="ignore")[:800_000]
    pats = [
        r'<meta[^>]+property=["\']og:article:author["\'][^>]+content=["\']([^"\']+)',
        r'<meta[^>]+content=["\']([^"\']+)["\'][^>]+property=["\']og:article:author["\']',
    ]
    for pat in pats:
        m = re.search(pat, head, re.I)
        if m:
            return html.unescape(m.group(1)).strip()
    return ""


def main() -> int:
    a = parse_args()
    curation = json.loads(Path(a.curation).read_text())
    manifest = json.loads(Path(a.markdown_manifest).read_text())
    ledger = json.loads(Path(a.ledger).read_text())
    content = Path(a.content)
    md_map = {str(x.get("url") or ""): x for x in manifest.get("entries", [])}
    ledger_urls = {str(x.get("wx_url") or "") for x in ledger}
    ledger_slugs = {str(x.get("slug") or "") for x in ledger}
    ledger_by_url = {str(x.get("wx_url") or ""): x for x in ledger}
    ledger_by_slug = {str(x.get("slug") or ""): x for x in ledger}
    all_rows = {str(x.get("wx_title") or ""): x for x in curation.get("rows", [])}
    final: List[Dict[str, Any]] = []
    review: List[Dict[str, Any]] = []

    for row in curation.get("rows", []):
        title = str(row.get("wx_title") or "")
        if row.get("provenance") != "reprint":
            continue
        if title in EXCLUDE_REPRINT:
            review.append({**row, "new_decision": "exclude", "new_reason": EXCLUDE_REPRINT[title], "author": "", "slug": ""})
            continue
        slug = SLUGS.get(title)
        if not slug:
            raise SystemExit(f"missing semantic slug: {title}")
        source = md_map.get(str(row.get("wx_url") or "")) or {}
        author_name = og_author(str(source.get("source_html") or ""))
        author_slug = TITLE_AUTHOR.get(title) or AUTHOR_SLUGS.get(author_name)
        if not author_slug:
            raise SystemExit(f"missing author mapping: {title} ({author_name})")
        display = AUTHOR_PROFILES[author_slug][0]
        section = TITLE_SECTION.get(title, str(row.get("section") or ""))
        item = {
            **row,
            "section": section,
            "slug": slug,
            "authors": [author_slug],
            "source_markdown": str(source.get("markdown_file") or row.get("source_markdown") or ""),
            "conversion_status": str(row.get("conversion_status") or source.get("status") or "ok"),
            "decision": "keep_high_value_reprint",
            "author_display": display,
            "attribution": f"原作者：{display}",
            "translation_derived": title.startswith("Paul Graham："),
        }
        final.append(item)
        review.append({**row, "section": section, "new_decision": "keep_high_value_reprint", "new_reason": "正文完整且具有长期技术或行业价值", "author": display, "slug": slug})

    for title, (section, slug, authors, tags) in INDEPENDENT.items():
        row = all_rows.get(title)
        if not row:
            raise SystemExit(f"independent source missing: {title}")
        source = md_map.get(str(row.get("wx_url") or "")) or {}
        final.append({**row, "section": section, "slug": slug, "authors": authors, "tags": tags,
                      "source_markdown": str(source.get("markdown_file") or row.get("source_markdown") or ""),
                      "decision": "keep_independent"})
        review.append({**row, "new_decision": "keep_independent", "new_reason": "用户明确要求拆分为独立文章", "author": "冯若航", "slug": slug})

    for title, (section, slug, authors, tags) in EXTRA_KEEP.items():
        row = all_rows.get(title)
        if not row:
            raise SystemExit(f"extra keep source missing: {title}")
        source = md_map.get(str(row.get("wx_url") or "")) or {}
        source_markdown = str(row.get("source_markdown") or source.get("markdown_file") or "")
        final.append({**row, "section": section, "slug": slug, "authors": authors, "tags": tags,
                      "source_markdown": source_markdown, "decision": "keep_high_value_original"})
        review.append({**row, "new_decision": "keep_high_value_original", "new_reason": "正文完整且具有长期保存价值", "author": "冯若航", "slug": slug})

    for row in USER_SOURCES:
        final.append(dict(row))
        review.append({**row, "new_decision": "keep_user_source", "new_reason": "用户补充完整原稿", "author": "冯若航"})

    for row in curation.get("rows", []):
        if row.get("decision") != "exclude_media_only":
            continue
        if row.get("wx_title") == "盘古之殇：大模型研发历程的心酸与黑暗":
            if (content / "ai" / "pangu-model-story" / "index.md").exists():
                review.append({**row, "section": "ai", "new_decision": "imported_high_value_external",
                               "new_reason": "已从 GitHub 权威原文仓库恢复完整正文",
                               "author": "HW-whistleblower", "slug": "pangu-model-story"})
            else:
                review.append({**row, "new_decision": "needs_source_high_priority", "new_reason": "高价值外部分享；原知乎正文已删除且本地仅有摘要封面", "author": "待确认", "slug": "pangu-model-story"})
        else:
            review.append({**row, "new_decision": "exclude_media_or_promo", "new_reason": "纯视频、分享卡片、二维码、活动广告或仅图片内容", "author": "", "slug": ""})

    # Complete the ledger: keep every previous candidate visible in the review,
    # including items whose earlier decision remains unchanged.
    reviewed = {(str(x.get("wx_url") or ""), str(x.get("wx_title") or "")) for x in review}
    preserved_reason = {
        "exclude_covered": "同一正文已存在于本地博客",
        "exclude_superseded": "已有更完整的后续文章",
        "exclude_promo": "直播、活动、招聘、赠票或广告内容",
        "exclude_water": "信息量很低的即时短讯",
        "exclude_unmarked": "来源不明且正文过短或临时性强",
        "exclude_directory": "公众号导航已由博客栏目与标签替代",
        "exclude_external_profile": "第三方英文采访已在其他载体保留",
        "merge_into_local": "按既有决定更新对应版本/主题文章",
    }
    for row in curation.get("rows", []):
        key = (str(row.get("wx_url") or ""), str(row.get("wx_title") or ""))
        if key in reviewed:
            continue
        if str(row.get("wx_url") or "") in ledger_urls:
            decision, reason = "already_imported", "已存在于 wxmp-import 基线"
        elif row.get("wx_title") == "Pigsty 特性与快速上手":
            decision, reason = "exclude_covered", "内容已由 content/pigsty/v2.0 与现有 Pigsty 指南覆盖"
        else:
            decision = str(row.get("decision") or "preserve_previous_decision")
            reason = preserved_reason.get(decision, str(row.get("reason") or "保留此前人工审阅决定"))
        review.append({**row, "new_decision": decision, "new_reason": reason, "author": "", "slug": str(row.get("proposed_slug") or "")})

    slugs = [str(x["slug"]) for x in final]
    if len(slugs) != len(set(slugs)):
        raise SystemExit("duplicate final slug")
    intended = {str(x["slug"]): x for x in final}
    collisions = []
    for slug, row in intended.items():
        prior = ledger_by_slug.get(slug)
        if prior and str(prior.get("wx_url") or "") != str(row.get("wx_url") or ""):
            collisions.append(slug)
            continue
        existing = [content / sec / slug for sec in ("ai","cloud","db","misc","pg","pigsty","trip") if (content / sec / slug).exists()]
        if existing and not prior:
            collisions.append(slug)
        elif existing and (content / row["section"] / slug) not in existing:
            collisions.append(slug)
    collisions = sorted(collisions)
    if collisions:
        raise SystemExit(f"slug collisions: {collisions}")
    url_collisions = sorted(str(x["wx_url"]) for x in final
                            if str(x["wx_url"]) in ledger_urls
                            and str(ledger_by_url[str(x["wx_url"])].get("slug") or "") != str(x["slug"]))
    if url_collisions:
        raise SystemExit(f"URL already imported: {url_collisions}")
    for x in final:
        if not Path(str(x.get("source_markdown") or "")).exists():
            raise SystemExit(f"source missing: {x.get('wx_title')}")

    final.sort(key=lambda x: (str(x.get("published_at") or ""), str(x.get("wx_title") or "")))
    review.sort(key=lambda x: (str(x.get("published_at") or ""), str(x.get("wx_title") or "")))
    Path(a.out_final).write_text(json.dumps(final, ensure_ascii=False, indent=2) + "\n")
    payload = {"generated_at": datetime.now().astimezone().isoformat(timespec="seconds"),
               "counts": dict(Counter(x["new_decision"] for x in review)), "rows": review}
    Path(a.out_json).write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n")

    fields = ["new_decision","published_at","section","wx_title","provenance","source_text_length","image_count","author","slug","new_reason","wx_url"]
    with Path(a.out_csv).open("w", encoding="utf-8", newline="") as fp:
        w = csv.DictWriter(fp, fieldnames=fields, extrasaction="ignore", lineterminator="\n"); w.writeheader(); w.writerows(review)
    lines = ["# WXMP 转载与编辑性排除复审", "", f"> 生成时间：{payload['generated_at']}", "", "## 汇总", "",
             "| 决策 | 数量 |", "|---|---:|"]
    for k,v in sorted(payload["counts"].items()): lines.append(f"| `{k}` | {v} |")
    lines += ["", "## 逐篇决策", "", "| 日期 | 专栏 | 决策 | 标题 | 作者 | 理由 |", "|---|---|---|---|---|---|"]
    for x in review:
        esc=lambda v:str(v or "").replace("|","\\|").replace("\n"," ")
        lines.append(f"| {str(x.get('published_at') or '')[:10]} | `{esc(x.get('section'))}` | `{esc(x.get('new_decision'))}` | {esc(x.get('wx_title'))} | {esc(x.get('author'))} | {esc(x.get('new_reason'))} |")
    Path(a.out_md).write_text("\n".join(lines) + "\n")

    if a.write_authors:
        used = {s for x in final for s in x.get("authors", []) if s != "vonng"}
        for slug in sorted(used):
            if slug not in AUTHOR_PROFILES:
                raise SystemExit(f"profile missing: {slug}")
            target = content / "authors" / slug / "_index.md"
            if target.exists():
                continue
            name, desc = AUTHOR_PROFILES[slug]
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_text(f'---\ntitle: "{name}"\ndescription: "{desc}"\n---\n', encoding="utf-8")

    print(json.dumps({"imports":len(final),"review_counts":payload["counts"],"authors":len({s for x in final for s in x.get('authors',[]) if s!='vonng'})}, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
