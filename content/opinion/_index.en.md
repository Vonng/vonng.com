---
title: Opinions
linkTitle: Opinions
description: "The author's personal views, core theses, and structured FAQ index."
type: docs
icon: fa-solid fa-lightbulb
sidebar_root_for: self
sidebar_root_link_self: true
sidebar_enabled: true
sidebar_expanded: true
toc_style: fixed
page_width: normal
featured_image: none
no_list: true
comments: false
backlinks: false
cascade:
  type: docs
  sidebar_enabled: true
  sidebar_expanded: true
  toc_style: fixed
  page_width: normal
  featured_image: none
  section_index: cards
  section_index_columns: 2
  comments: false
---

While blog columns flow chronologically as standalone essays, **Opinions** organizes Ruohang Feng's core arguments into a structured **Question → Thesis Summary → Supporting Evidence** reference tree.

Every entry states a concrete engineering, economic, or philosophical question upfront, answers it directly with first-hand numbers and reasoning, and links to the underlying essays that supply empirical bills, benchmarks, source audits, or postmortems.

> **Language Note**: The Opinion tree is currently maintained in Chinese (`zh-cn`), distilling 319 essays across the [AI Explorer](/en/ai/) (110), [Database](/en/db/) (109), and [Cloud Mudslide](/en/cloud/) (100) columns into 449 question-driven entries with exact section-level anchors. Links below jump directly to the corresponding Chinese topic pages.

## AI & Agents Opinion Tree {#ai-themes}

- [AI Overview (AI 板块总览)](/opinion/ai/) — Master index across compute economics, AI-native software engineering, DB × AI architecture, model cognition, organizational shifts, macroeconomics, and alignment philosophy.
- [Compute Economics (算力经济学)](/opinion/ai/compute/) — Subscription arbitrage ledgers, tier pricing laws, anti-Goodhart token KPIs, payment risk controls, and sovereign local inference.
- [AI Software Engineering (AI 软件工程)](/opinion/ai/swe/) — Spec-Driven Development (SDD), spending 80% of tokens on verification harnesses, multi-model personality pairing, and dual-surface docs.
- [Databases & AI (数据库与AI)](/opinion/ai/db/) — Memory as the complement of environment, the 50-year filesystem vs. database tug-of-war, the twilight of standalone RAG/vector DBs, and why PostgreSQL won.
- [Model Meditations (模型沉思录)](/opinion/ai/model/) — The missing 60-billion-neuron cerebellum, the 70% tacit-knowledge ceiling, Transformer vs. Diffusion hemispheres, world models, and Free Energy.
- [Enterprise AI Transformation (企业AI转型)](/opinion/ai/org/) — Why legacy AI rollouts stall on steam-era drive shafts, SaaS unbundling, open-source karma and punishability, OPC valuation, and talent survival.
- [AI Macroeconomics (AI 宏观经济)](/opinion/ai/macro/) — The 5-tier global adoption funnel, post-attention compute sinks, a 45% bubble-clearing thesis, cognitive deflation ("the horse trap"), and 2036 scarcities.
- [AI Philosophy (AI 哲学思考)](/opinion/ai/philosophy/) — *Cyber Dharma* across seven traditions, the Lethal Trifecta of cloud secretaries, niche-isolated privacy, academic citation laundering, and digital tombstones.
  {.cards}

## Database Industry Opinion Tree {#db-themes}

- [Database Overview (数据库板块总览)](/opinion/db/) — Master index across engine selection, architectural minimalism, domestic database reality, open-source object storage, and production operations (145 questions).
- [Selection & Engine Wars (选型与路线之争)](/opinion/db/selection/) — The database hierarchy of needs, why MySQL faded and PostgreSQL won, MongoDB & standalone vector DB postmortems, and AI state stores.
- [Architectural Minimalism (架构祛魅与极简主义)](/opinion/db/architecture/) — Distributed OLTP & microservice mirages, Small Data & DuckDB, Catalog & Palantir "Ontology" hype, modern hardware, and core concurrency primitives.
- [Domestic Databases & Sovereignty (国产数据库与自主可控)](/opinion/db/domestic/) — Anatomy of the domestic DB lemon market, shell-fork archaeology, compliance strategies, and genuine open-source software sovereignty.
- [Open Source & Object Storage (开源变局与对象存储)](/opinion/db/oss-storage/) — How MinIO died and Silo revived it, commercial open-source rug-pulls, software supply-chain trust, and self-built tooling.
- [Production Ops, Containers & DBAs (生产运维、容器化与DBA)](/opinion/db/ops-career/) — Why stateful production databases stay out of Docker/K8s, Etcd postmortems, 5 TB drop-database lessons, and the future of DBAs.
  {.cards}

## Cloud & Cloud-Exit Opinion Tree {#cloud-themes}

- [Cloud Overview (云计算板块总览)](/opinion/cloud/) — Master index across cloud tax economics, hyperscaler postmortems, RDS critique & industrialized self-hosting, and data sovereignty (114 questions).
- [FinOps & Cloud-Exit Economics (云税解剖与下云经济学)](/opinion/cloud/finops/) — Deconstructing compute/EBS/S3 markups, why FinOps ends in cloud exit, DHH & Ahrefs ledgers, and hardware dividends.
- [Cloud Outages & Postmortems (云上草台班子与故障启示录)](/opinion/cloud/outages/) — Why cloud SLAs are placebos, global IAM/DNS cascade failures, postmortem culture gaps, and war-era disaster recovery.
- [RDS Critique & Self-Hosting (云数据库祛魅与工业化自建)](/opinion/cloud/rds-dba/) — How managed RDS castrates PostgreSQL's extension soul, why DBAs remain irreplaceable, and IDC 2.0 + Cloudflare.
- [Data Sovereignty & Cloud Security (数据主权、云安全与平台阴影)](/opinion/cloud/sovereignty/) — The Data Sovereignty Manifesto, SaaS kill switches, AI-era cloud security sieves, and hyperscaler open-source strip-mining.
  {.cards}
