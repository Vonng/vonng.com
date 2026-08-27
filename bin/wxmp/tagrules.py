"""Assign closed-vocabulary tags to a WeChat article from its title and body."""
import re

# vocabulary zh label -> tier
TIER = {
 "PostgreSQL":1,"Pigsty":1,"MySQL":1,"Redis":1,"MongoDB":1,"Oracle":1,"OLAP":1,
 "国产数据库":1,"AI":1,"Agent":1,"Claude":1,"Codex":1,"大模型":1,"云计算":1,"下云":1,
 "数据库":2,"RDS":2,"机器学习":2,"阿里云":2,"AWS":2,"Cloudflare":2,"故障复盘":2,"成本":2,
 "对象存储":2,"容器化":2,"Linux":2,"硬件":2,"PG管理":2,"PG开发":2,"PG生态":2,"PG内核":2,
 "扩展":2,"监控":2,"备份":2,"性能":2,"安全":2,"迁移":2,"GIS":2,"向量":2,"事务":2,
 "分布式系统":2,"架构":2,"软件工程":2,"数据主权":2,"本地优先":2,"软件仓库":2,"工具":2,"文档":2,
 "开源":3,"技术评论":3,"翻译":3,"职业":3,"哲学":3,"社会观察":3,"商业":3,"随笔":3,"旅行":3,
}

# tag -> regex over title+body. Order matters only for readability.
RULES = [
 ("PostgreSQL", r"PostgreSQL|PgSQL|(?<![A-Za-z])PG(?![A-Za-z])|Postgres"),
 ("Pigsty", r"Pigsty"),
 ("MySQL", r"MySQL"),
 ("Redis", r"Redis|Valkey"),
 ("MongoDB", r"MongoDB"),
 ("Oracle", r"Oracle|甲骨文"),
 ("OLAP", r"DuckDB|ClickHouse|Iceberg|OLAP|数据仓库|分析型"),
 ("国产数据库", r"国产数据库|信创|自主可控|PolarDB|IvorySQL|OceanBase|达梦|高斯|GaussDB|人大金仓"),
 ("AI", r"(?<![A-Za-z])AI(?![A-Za-z])|人工智能"),
 ("Agent", r"Agent|智能体|\bMCP\b|OpenClaw|Claude Code"),
 ("Claude", r"Claude|Anthropic|Fable"),
 ("Codex", r"Codex|OpenAI|ChatGPT|GPT-|gpt-oss"),
 ("大模型", r"大模型|\bLLM\b|DeepSeek|Qwen|通义|AGI|开放权重|模型权重"),
 ("云计算", r"云计算|公有云|云厂商|腾讯云|华为云|百度云|Azure|GCP|云服务"),
 ("下云", r"下云|上云|自建|本地部署|云退|离开云"),
 ("数据库", r"数据库"),
 ("RDS", r"(?<![A-Za-z])RDS(?![A-Za-z])|云数据库"),
 ("机器学习", r"机器学习|神经网络|深度学习|强化学习"),
 ("阿里云", r"阿里云|阿里巴巴|支付宝|淘宝|闲鱼"),
 ("AWS", r"(?<![A-Za-z])AWS(?![A-Za-z])|亚马逊|(?<![A-Za-z])EC2(?![A-Za-z])"),
 ("Cloudflare", r"Cloudflare|赛博菩萨"),
 ("故障复盘", r"故障|翻车|宕机|挂了|崩了|事故|中断|复盘|不可用|删库|泄露|泄漏"),
 ("成本", r"成本|费用|价格|降价|账单|省钱|收费|贵|便宜|烧钱|融资|收购|营收"),
 ("对象存储", r"对象存储|MinIO|(?<![A-Za-z])S3(?![A-Za-z])|存储桶"),
 ("容器化", r"容器|Docker|K8S|Kubernetes"),
 ("Linux", r"Linux|CentOS|Ubuntu|Debian|RHEL|发行版|内核"),
 ("硬件", r"硬件|CPU|GPU|显卡|内存条|服务器|笔记本|AMD|Intel|磁盘|NVMe"),
 ("PG管理", r"运维|管理|部署|配置|升级|巡检|参数|连接池|PgBouncer|备份恢复|高可用"),
 ("PG开发", r"(?<![A-Za-z])SQL(?![A-Za-z])|查询语句|索引|建表|存储过程|触发器|DDL|DML"),
 ("PG生态", r"PG ?生态|PostgreSQL ?社区|大会|峰会|论坛|贡献者|PGCon|PGConf|Meetup|年度调查|生态"),
 ("PG内核", r"内核|WAL|MVCC|存储引擎|执行器|优化器|脏页"),
 ("扩展", r"扩展|插件|Extension|pgvector|PostGIS|Citus|TimescaleDB"),
 ("监控", r"监控|Prometheus|Grafana|指标|告警|观测"),
 ("备份", r"备份|恢复|PITR|pgBackRest|归档"),
 ("性能", r"性能|优化|加速|吞吐|延迟|基准|Benchmark|跑分|快\d+倍|慢\d+倍"),
 ("安全", r"安全|漏洞|CVE|加密|认证|权限|攻击|合规|隐私|证书"),
 ("迁移", r"迁移|搬迁|切换|替换|下线"),
 ("GIS", r"PostGIS|地理|空间|经纬"),
 ("向量", r"向量|Embedding|pgvector|RAG"),
 ("事务", r"事务|隔离级别|一致性|ACID"),
 ("分布式系统", r"分布式|集群|副本|分片|共识|Raft"),
 ("架构", r"架构|设计|范式|技术栈|选型"),
 ("软件工程", r"软件工程|编程|代码|开发者|程序员|构建|打包|工程师"),
 ("数据主权", r"数据主权|主权|管辖|出海|合规|封禁|制裁"),
 ("本地优先", r"本地优先|Local.First|自托管|Self.Host"),
 ("软件仓库", r"仓库|镜像站|APT|YUM|RPM|源码包"),
 ("工具", r"工具|软件|客户端|命令行|编辑器|输入法"),
 ("文档", r"文档|手册|翻译版|教程|指南|书"),
 ("开源", r"开源|Open.Source|许可证|协议|GPL|Apache|AGPL|Star|GitHub"),
 ("技术评论", r"评论|观点|吐槽|驳《|批评|争论|辩论|闹剧|尬|忽悠|胡说|扯淡|谬论"),
 ("翻译", r"翻译|译文|编译自|原文作者|原文链接|译者"),
 ("职业", r"职业|招聘|坑位|薪资|年薪|求职|跳槽|DBA|工作"),
 ("哲学", r"哲学|本体论|道德经|儒|佛|禅|神学|经藏|吠檀多|诺斯替|拜火"),
 ("社会观察", r"社会|时代|舆论|热搜|大众|人们|国家|政策|监管"),
 ("商业", r"商业|公司|创业|市场|营收|融资|收购|估值|客户|销售|商业模式"),
 ("随笔", r"随笔|感想|回顾|总结|杂谈|小记|闲话|记事|流水账|碎碎念|这一年|近况"),
 ("旅行", r"旅行|游记|自驾|徒步|露营|风景|旅游|机场|飞回"),
]

SECTION_SEED = {
 "pg": "PostgreSQL", "pigsty": "Pigsty", "cloud": "云计算",
 "db": "数据库", "ai": "AI", "trip": "旅行", "misc": "",
}
COMPILED = [(t, re.compile(p, re.I)) for t, p in RULES]

# tier-1 brand tags need real presence, not a passing mention
BRAND = {"Pigsty","MySQL","Redis","MongoDB","Oracle","OLAP","Claude","Codex",
         "国产数据库","Agent","大模型","Cloudflare","AWS","阿里云","RDS","MinIO"}


def _score(rx, title, head, rest):
    return 6*len(rx.findall(title)) + 2*len(rx.findall(head)) + len(rx.findall(rest))


SERIES = [(re.compile(r'^Pigsty\s*v?\d'), ["Pigsty"])]


def assign(title: str, body: str, section: str, max_tags: int = 3) -> list[str]:
    for rx, tags in SERIES:
        if rx.match(title.strip()):
            return list(tags)
    head, rest = body[:600], body[600:6000]
    raw = {}
    for tag, rx in COMPILED:
        sc = _score(rx, title, head, rest)
        if sc:
            raw[tag] = sc
    seed = SECTION_SEED.get(section) or ""
    if seed:
        raw[seed] = raw.get(seed, 0) + 7

    if not raw:
        return ["随笔"]
    top = max(raw.values())
    # drop weak signals; brands need a title hit or several mentions
    keep = {}
    for tag, sc in raw.items():
        if tag == seed:
            keep[tag] = sc; continue
        if sc < max(2, 0.12 * top):
            continue
        if tag in BRAND and sc < 6 and tag != seed:
            continue
        keep[tag] = sc

    def best(tier, n):
        c = sorted((t for t in keep if TIER.get(t, 3) == tier),
                   key=lambda t: (-keep[t], t))
        return c[:n]

    out = []
    for t in best(1, 2):
        if t not in out: out.append(t)
    for t in best(2, 2):
        if len(out) >= max_tags: break
        if t not in out: out.append(t)
    for t in best(3, 1):
        if len(out) >= max_tags: break
        if t not in out: out.append(t)
    if len(out) < 2:
        for t in sorted(keep, key=lambda t: (-keep[t], t)):
            if t not in out:
                out.append(t)
            if len(out) >= 2: break
    return out[:max_tags]
