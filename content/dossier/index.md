---
title: "冯若航 — PostgreSQL 社区贡献者档案"
summary: "PostgreSQL 认可贡献者（Recognized Contributor）提名档案：冯若航在相关开源代码、扩展打包分发、官方文档翻译、开放教育与社区布道五个维度的持续贡献记录。"
description: "冯若航（Ruohang Feng / Vonng）的 PostgreSQL 社区贡献者提名档案中文版，与 2026 年 5 月英文版 Dossier 对齐。"
date: 2026-05-01
layout: dossier
reading_time: false
notoc: true
comments: false
tags: []
---

<article class="dossier" aria-labelledby="dossier-title">
  <section class="dossier-sheet dossier-sheet-primary" aria-label="贡献者档案 第 1 页">
    <div class="dossier-topline">
      <span>2026 年 5 月 · <a href="/en/dossier/">English Dossier →</a></span>
      <span>冯若航 (Ruohang Feng) — PostgreSQL Contributor Dossier</span>
    </div>

    <header class="dossier-hero">
      <div>
        <h1 id="dossier-title">冯若航 · Ruohang Feng</h1>
        <p>PostgreSQL 认可贡献者提名档案（Nomination Dossier）</p>
      </div>
      <aside aria-label="呈交对象">
        <span>Prepared for</span>
        <strong>Contributors Committee</strong>
        <a href="mailto:contributors@postgresql.org">contributors@postgresql.org</a>
        <time datetime="2026-05">May 2026</time>
      </aside>
    </header>

    <dl class="dossier-meta">
      <div class="dossier-meta-name">
        <dt>姓名 / Name</dt>
        <dd>冯若航 / Ruohang Feng / Vonng</dd>
      </div>
      <div class="dossier-meta-identity">
        <dt>主要身份 / Identity</dt>
        <dd><a href="https://github.com/pgsty/pigsty">Pigsty</a> 作者与创始人</dd>
      </div>
      <div class="dossier-meta-based">
        <dt>常驻地 / Based in</dt>
        <dd>中国上海 · 新加坡</dd>
      </div>
      <div class="dossier-meta-active">
        <dt>深耕年限 / Active since</dt>
        <dd>2015 年至今 — 11 年独立贡献</dd>
      </div>
      <div class="dossier-meta-links">
        <dt>链接 / Links</dt>
        <dd>
          <a href="https://github.com/Vonng">GitHub</a>
          <a href="https://vonng.com">个人网站</a>
          <a href="https://www.linkedin.com/in/vonng">LinkedIn</a>
          <a href="https://x.com/RonVonng">Twitter</a>
          <a href="mailto:rh@vonng.com">电子邮箱</a>
        </dd>
      </div>
    </dl>

    <p class="dossier-lede">
      围绕 <a href="https://www.postgresql.org/about/policies/contributors/">PostgreSQL 认可贡献者政策（Recognized Contributors Policy）</a> 所列举的五大方向——<em>紧密相关的外部开源代码、软件包构建与分发、官方文档翻译、开放技术教育与社区布道</em>——自 2015 年起持续开展独立贡献，重点聚焦于跨 Linux 发行版的 PostgreSQL 扩展供应链建设、官方技术资料的中文无障碍普及，以及中文社区内少有的厂商中立技术发声。
    </p>

    <section class="dossier-section" aria-labelledby="code">
      <h2 id="code"><span>I. Code</span><em>紧密相关的开源项目</em></h2>

      <div class="dossier-entry">
        <h3>Pigsty — 开箱即用的开源 PostgreSQL RDS 发行版</h3>
        <p><a href="https://github.com/pgsty/pigsty">Pigsty</a>（5,100+ GitHub Stars，当前版本 v4.3.0）是一套开箱即用的开源 PostgreSQL 数据库发行版，深度集成了高可用（Patroni）、时间点恢复（pgBackRest）、连接池（PgBouncer）、可观测性栈（pg_exporter + Grafana）以及下文所述的扩展插件生态。它可直接部署于 16 种主流 Linux 发行版的裸金属或虚拟机之上，在开源 Postgres 发行版中拥有广泛的社区采用度。其文档站点 <a href="https://pigsty.cc/">pigsty.cc</a> / <a href="https://pigsty.io/">pigsty.io</a> 目前每月服务约 <strong>10,000 名开发者</strong>，软件源月均提供约 <strong>100 万次软件包下载</strong>。</p>
      </div>

      <div class="dossier-entry">
        <h3>pg_exporter — 声明式 PostgreSQL Prometheus 监控采集器</h3>
        <p><a href="https://github.com/pgsty/pg_exporter">pg_exporter</a> 是使用 Go 语言编写的 PostgreSQL 监控指标导出器，通过声明式 YAML 配置暴露 600+ 项数据库核心指标，支持动态查询编排、跨版本自动适配（PG 10–18）与按集群细粒度定制。它既是 Pigsty 可观测性体系的核心引擎，也被大量未部署 Pigsty 的生产环境 DBA 独立采用。</p>
      </div>
    </section>

    <section class="dossier-section" aria-labelledby="packaging">
      <h2 id="packaging"><span>II. Packaging</span><em>软件包构建与分发</em></h2>

      <div class="dossier-stats" aria-label="扩展打包核心指标">
        <div><strong>1,617</strong><span>扩展目录收录总数</span></div>
        <div><strong>511</strong><span>PGDG 兼容二进制扩展</span></div>
        <div><strong>16</strong><span>支持 Linux 发行版</span></div>
        <div><strong>14</strong><span>兼容 PG 内核分支</span></div>
        <div><strong>100k+</strong><span>仓库二进制包总量</span></div>
      </div>

      <p>两项相辅相成的软件源工程，均与上游官方 PGDG YUM / APT 仓库保持 100% 兼容与互操作：</p>

      <div class="dossier-entry">
        <h3>PGEXT.CLOUD — 全球 PostgreSQL 扩展二进制仓库与目录</h3>
        <p><a href="https://pgext.cloud/">PGEXT.CLOUD</a> 整理收录了广义 Postgres 生态中 <strong>1,617 款扩展插件</strong>的标准化元数据；在与官方 PGDG 仓库配合使用时，为横跨 16 种 Linux 发行版（EL 8/9/10、Debian 11/12/13、Ubuntu 22.04/24.04/26.04 及其衍生版）与 5 个 PostgreSQL 大版本（14–18）提供 <strong>511 款 PostgreSQL 扩展</strong>的即装即用 RPM 与 DEB 二进制包。该工程与 Devrim Gündüz 及 Christoph Berg 维护的上游 PGDG 仓库完全兼容，重点填补上游构建矩阵之外的长尾扩展空白，并将 EL 系与 Debian 系的包名、版本与依赖统一到同一套元数据模型之下。目前仓库托管超过 10 万个二进制包，通过全球 CDN 开放分发。</p>
      </div>

      <div class="dossier-entry">
        <h3>中国大陆地区官方 PGDG 镜像源</h3>
        <p>长期独立运维<a href="https://pigsty.cc/docs/repo/pgdg/#mirror"><strong>面向中国大陆地区的官方 PGDG YUM 与 APT 完整镜像源</strong></a>，切实解决了长期困扰国内用户的跨境网络阻断与安装失败问题。镜像严格跟踪上游同步，完整保留官方 PGDG 目录结构与签名校验体系。</p>
      </div>

      <div class="dossier-entry">
        <h3>PIG — PostgreSQL 扩展与软件包管理器 CLI</h3>
        <p><a href="https://pigsty.io/docs/pig">PIG</a> 是一款独立的 Go 命令行工具，兼具 PostgreSQL 扩展包管理器与通用 Postgres 软件源管理器的双重角色。它能够自动识别当前运行的操作系统与内核版本、解析扩展依赖关系，并从 PGEXT.CLOUD 或上游 PGDG 仓库拉取匹配的二进制包。PIG v1.0 正式发布消息已获 <a href="https://www.postgresql.org/about/news/pig-v10-released-with-pgextcloud-444-pg-extensions-on-14-linux-3214/">postgresql.org 官方新闻</a>收录报道。</p>
      </div>
    </section>

    <section class="dossier-section" aria-labelledby="translation">
      <h2 id="translation"><span>III. Translation</span><em>官方文档与生态汉化</em></h2>
      <p>独立构建并持续维护的简体中文文档翻译工程，覆盖 PostgreSQL 官方手册及核心高可用生态组件：</p>
      <ul>
        <li><strong>PostgreSQL 14–18 官方手册完整中文版</strong> — 发布于 <a href="https://pg.center/docs/">pg.center/docs/</a>，随上游大版本演进持续同步更新，而非停留在单一历史版本。</li>
        <li><strong>核心生态组件文档翻译</strong> — 完成 <em>PgBouncer</em>、<em>Patroni</em> 与 <em>pgBackRest</em> 全套官方文档的中文译介。</li>
        <li><strong>500+ 扩展插件文档汉化</strong> — 为 PGEXT.CLOUD 目录中约 <strong>500 款 PostgreSQL 扩展</strong>提供中文说明与使用文档，大幅降低了中文开发者发现、评估与采纳 PG 扩展的门槛。</li>
      </ul>
      <blockquote>这是一条独立发起、面向当前活跃上游版本持续演进的全新中文文档轨道。</blockquote>
    </section>

    <footer class="dossier-page-footer">
      <span>冯若航 (Ruohang Feng) — Contributor Dossier</span>
      <span>Page 1 / 2</span>
    </footer>
  </section>

  <section class="dossier-sheet" aria-label="贡献者档案 第 2 页">
    <div class="dossier-topline">
      <span>2026 年 5 月 · <a href="/en/dossier/">English Dossier →</a></span>
      <span>冯若航 (Ruohang Feng) — PostgreSQL Contributor Dossier</span>
    </div>

    <header class="dossier-continuation">
      <div>
        <h2>冯若航 · Ruohang Feng</h2>
        <p>提名档案（续页）</p>
      </div>
      <a href="mailto:contributors@postgresql.org">contributors@postgresql.org</a>
    </header>

    <section class="dossier-section" aria-labelledby="education">
      <h2 id="education"><span>IV. Open Education</span><em>技术专栏、经典译著与参考门户</em></h2>

      <div class="dossier-entry">
        <h3>pg.center — PostgreSQL 知识图谱与中文文档门户</h3>
        <p><a href="https://pg.center/docs/">pg.center</a> 将 PostgreSQL 14–18 中英双语官方手册、系统目录、GUC 参数矩阵以及 500+ 扩展文档串联为统一的参考界面，是目前面向中文 DBA 与开发者持续跟进上游最新版本的首要官方资料入口。同时配套维护经典技术译著《<a href="https://pgint.vonng.com">PostgreSQL 内幕探索</a>》与《<a href="https://ddia.vonng.com">设计数据密集型应用（DDIA）</a>》中文版。</p>
      </div>

      <div class="dossier-entry">
        <h3>持续十年的中文 PostgreSQL 深度写作（2016 至今）</h3>
        <p>自 2016 年起通过个人技术博客（<a href="https://vonng.com">vonng.com</a>）与微信公众号《老冯云数》不间断撰写 PostgreSQL 深度文章。公众号拥有约 <strong>60,000 名订阅者</strong>，全网跨平台总读者约 <strong>100,000 人</strong>，是中文技术社区在数据库与基础架构领域最具影响力的独立技术作者（KOL）之一。写作内容全面覆盖 Postgres 生态演进、扩展插件、应用开发、生产运维、架构选型、下云实践与内核原理。</p>
      </div>

      <div class="dossier-entry">
        <h3>《PostgreSQL 正在吞噬数据库世界》（2024）</h3>
        <p>发表于 <a href="https://vonng.com/en/pg/pg-eat-db-world/">vonng.com</a>（中文原版：<a href="https://vonng.com/pg/pg-eat-db-world/">《PostgreSQL 正在吞噬数据库世界》</a>）的深度评论长文，英文版曾<a href="https://news.ycombinator.com/item?id=39711863">登顶 Hacker News 首页榜首</a>，并在全球 Postgres 社区关于“可扩展性吞噬专用数据库”的讨论中被广泛引用。</p>
      </div>
    </section>

    <section class="dossier-section" aria-labelledby="community">
      <h2 id="community"><span>V. Community &amp; Advocacy</span><em>社区参与与独立布道</em></h2>
      <ul>
        <li>曾任<strong>中国开源软件推进联盟 PostgreSQL 分会（中文社区）技术委员会委员</strong>。</li>
        <li>连续多年作为演讲嘉宾与参会者活跃于 <strong>PGConf.Dev</strong> 与 <strong>PGConf.Asia</strong> 等国际顶级社区会议。</li>
        <li>以<strong>独立开发者（One-Person Company）</strong>身份开展开源工作——既非云厂商雇员，亦不依附于任何大型商业机构——在由大厂与官方机构主导的中文数据库舆论场中，提供罕见且坚定的厂商中立（Vendor-Neutral）社区视角。</li>
      </ul>

      <div class="dossier-entry">
        <h3>近年国际与社区大会参与记录</h3>
        <div class="dossier-table-wrap">
          <table class="dossier-events">
            <thead>
              <tr>
                <th>会议名称</th>
                <th>角色</th>
                <th>演讲议题</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td data-label="会议名称">PGConf.Dev 2026</td>
                <td data-label="角色">主题演讲</td>
                <td data-label="演讲议题"><a href="/work/extensions-for-everyone/">Extensions for Everyone</a></td>
              </tr>
              <tr>
                <td data-label="会议名称">HOW / PGConf.Asia 2026</td>
                <td data-label="角色">主题演讲</td>
                <td data-label="演讲议题">DBA Agent and Runtime</td>
              </tr>
              <tr>
                <td data-label="会议名称">HOW / PGConf.Asia 2025</td>
                <td data-label="角色">主题演讲</td>
                <td data-label="演讲议题">Let your elephant run</td>
              </tr>
              <tr>
                <td data-label="会议名称">PGEXT.Day 2025</td>
                <td data-label="角色">主题演讲</td>
                <td data-label="演讲议题">The Missing Package Manager and Extension Repo for PostgreSQL Ecosystem</td>
              </tr>
              <tr>
                <td data-label="会议名称">PGConf.Dev 2025</td>
                <td data-label="角色">闪电演讲</td>
                <td data-label="演讲议题">Extension Delivery: Make your PGEXT accessible to users</td>
              </tr>
              <tr>
                <td data-label="会议名称">PGConf.Dev 2024</td>
                <td data-label="角色">参会交流</td>
                <td data-label="演讲议题">-</td>
              </tr>
            </tbody>
          </table>
        </div>
      </div>
    </section>

    <section class="dossier-section dossier-assessment" aria-labelledby="assessment">
      <h2 id="assessment"><span>Honest Assessment</span><em>坦诚说明与边界界定</em></h2>
      <p>本档案所申请的社区认可类别为 <strong>Significant Contributor（重要贡献者）</strong>，依据是十余年来在扩展打包分发、外围生态代码、官方文档翻译与社区开放教育上的持续投入。为清晰界定边界，特此明确本档案<strong>不涉及</strong>以下范畴：</p>
      <ul>
        <li><strong>并非内核开发者或 Core Committer。</strong> 作者从未声称自己拥有 PostgreSQL 核心开发者（Core Developer）或代码提交者（Committer）身份。</li>
        <li><strong>无上游内核主干补丁提交记录。</strong> 作者未向 Postgres 核心代码库提交过合并补丁，在 <code>pgsql-hackers</code> 邮件列表上的参与亦属偶发而非持续——这一点在公开邮件列表归档中一目了然。</li>
      </ul>
    </section>

    <section class="dossier-section dossier-verification" aria-labelledby="verification">
      <h2 id="verification"><span>Verification</span><em>核验链接</em></h2>
      <ul>
        <li><strong>代码与软件源：</strong> <a href="https://github.com/pgsty/pigsty">github.com/pgsty/pigsty</a> · <a href="https://github.com/pgsty/pg_exporter">github.com/pgsty/pg_exporter</a> · <a href="https://pgext.cloud/">pgext.cloud</a> · <a href="https://pigsty.io/docs/pig">pigsty.io/docs/pig</a></li>
        <li><strong>翻译与写作：</strong> <a href="https://pg.center/docs/">pg.center/docs/</a> · <a href="https://vonng.com">vonng.com</a>（中英双语博客） · 微信公众号“老冯云数” · <a href="https://www.postgresql.org/about/newsarchive/">postgresql.org 官方新闻归档</a></li>
      </ul>
    </section>

    <footer class="dossier-page-footer">
      <span>冯若航 · Ruohang Feng — <a href="mailto:rh@vonng.com">rh@vonng.com</a> — <a href="https://vonng.com/">https://vonng.com</a></span>
      <span>Page 2 / 2</span>
    </footer>
  </section>
</article>
