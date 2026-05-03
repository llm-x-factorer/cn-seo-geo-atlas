---
title: 术语索引
type: glossary
last_updated: 2026-05-01
verified: true
confidence: high
---

# 术语索引

本文件是仓库内**唯一**的术语标准。所有卡片 frontmatter 的 `platforms` / `techniques` / `industry` 字段，slug 必须从这里取。新增 slug 走 PR。

## 核心概念

### SEO — Search Engine Optimization

**搜索引擎优化**。优化对象是**索引、排序、点击**：内容被搜索引擎收录 → 在结果页排序靠前 → 被用户点击。

- 反馈回路明确：可观测排名、可观测点击率
- 经典信号源：链接、内容相关性、用户行为（停留 / 跳出）、技术指标（速度、移动适配、结构化数据）
- 中文 SEO 的特殊性：百度的"主体认证"、ICP 备案、号主体绑定、特型卡占位

### GEO — Generative Engine Optimization

**生成式引擎优化**。优化对象是**被引用、被合成、被归因**：内容被 LLM 抓取并纳入训练 / 检索增强（RAG）→ 在用户与生成式引擎对话时被引用为答案依据。

- 反馈回路弱：没有"排名"，只有"被提及频率"和"引用上下文是否准确"
- 信号源未充分公开：依赖各生成式引擎的训练数据来源、检索增强的信源选择、过滤规则
- 与 SEO 的关键差异：
  - SEO 用户在结果列表里挑；GEO 用户接收一段合成文本，引用源**未必出现在视野里**
  - SEO 信号收敛（搜索引擎自己说的算）；GEO 信号发散（不同模型 / 不同 RAG 实现 / 不同时间点结果完全不同）
  - SEO 的"作弊"是堆链接堆关键词；GEO 的"作弊"是制造看起来权威的内容污染

> ⚠️ **GEO ≠ "AI SEO"**。把 GEO 简化成"AI 时代的 SEO"会错过它的本质：GEO 优化的是**信息被采纳为知识**，不是被检索到。

**Slug**：`geo`

### AEO — Answer Engine Optimization

**答案引擎优化**。最初指针对 Google "Featured Snippet" / "People Also Ask" 等**零点击答案位**的优化，目标是占据 SERP 内的答案盒。后来语义被泛化，常和 GEO 混用。

- 严格用法：仍在搜索结果页范畴内，只是结果是"答案"而非"链接"
- 泛化用法：包括 AI Overviews（Google）、必应 Copilot 答案、生成式引擎答案
- 本仓库立场：**严格用法**保留 AEO；指生成式引擎时用 GEO

**Slug**：`aeo`

### LLMO / AISO

**LLM Optimization** / **AI Search Optimization**。社群中和 GEO 大致同义的别名。本仓库统一用 GEO，不在卡片 slug 里使用 `llmo` / `aiso`。

### SERP — Search Engine Results Page

**搜索引擎结果页**。一次搜索查询后展示的整个页面，包括：

- 自然结果（organic results）
- 广告位（百度的"商业推广"、Google 的 Ads）
- 特型卡 / 答案盒（见下）
- 相关搜索、People Also Ask
- 知识面板 / 知识卡

**Slug**：`serp`

### 特型卡 / 特型结果

百度等搜索引擎在结果页中**非标准列表**形式的展示位的统称。包括：

- 答案卡（直接给一句话答案）
- 聚合卡（多源聚合，类似 Featured Snippet）
- 视频 / 图片 / 商品横滑卡
- 知识图谱卡（百度知道、百度百科主体）
- 站内子链 / Sitelinks

中文场景下"特型"是一个伞形术语，不同行业、不同平台所指可能略有差异。在卡片里使用时建议加修饰，例如"百度问答特型"、"小红书话题聚合卡"。

**Slug**：`featured-result`（避免和英文 Featured Snippet 完全等价）

### 站内搜索

**Internal site search / on-platform search**。内容平台（小红书、知乎、微信、B 站、抖音、淘宝、京东……）内部的搜索功能。

- 与 SEO 的关系：站内搜索的优化方法和传统 SEO 不同，但很多原理（关键词命中、内容质量、用户互动信号）可类比
- 与 GEO 的关系：很多内容平台的内容会**作为信源**被生成式引擎抓取，所以站内排名高的内容更可能被 GEO 系统纳入

**Slug**：`on-platform-search`

### 引用归因 — Citation Attribution

生成式引擎在答案中**标注信息来源**的机制。具体形式：

- 行内引用（"根据 X 网站..."）
- 上标编号 + 末尾引用列表（Perplexity、ChatGPT Search、豆包深度搜索）
- 卡片化引用（豆包、元宝在答案下方展示来源链接缩略图）
- 仅文字描述，无可点击链接

引用归因是 GEO 最关键的可观测面：能不能被引用 + 引用是否准确 + 用户能否回流。

**Slug**：`citation-attribution`

### 可见性 — Visibility

被检索 / 被引用 / 被展示的总称。是 SEO 和 GEO 共同的**最终目标的抽象层**。

- SEO 视角下的可见性：搜索结果中出现 + 排名 + 占位（特型卡 / 答案位）
- GEO 视角下的可见性：被生成式引擎引用 / 在生成答案中被提及 / 引用是否带链接
- 实操中需要进一步具体化为可测量的指标，"提升可见性"作为目标过于模糊

**Slug**：`visibility`

## 内容质量框架

### E-E-A-T

Experience, Expertise, Authoritativeness, Trustworthiness。Google 在 2022 年 12 月对原 E-A-T（Expertise, Authoritativeness, Trustworthiness）的扩充，加入了 Experience（亲历经验）维度。

来源：Google Search Quality Evaluator Guidelines。

中文常见译法：经验、专业、权威、可信。

中文搜索引擎（百度、神马）有类似但不完全等同的信号体系，本仓库的 `eeat-cn` 标签专指**中文搜索语境下的 E-E-A-T 类比信号**，不直接套用 Google 定义。

**Slug**：`eeat`（通用）/ `eeat-cn`（中文语境）

### YMYL — Your Money or Your Life

Google 提出的内容分类，指**对用户健康、财务、安全有重大影响**的内容（医疗、法律、金融、新闻等）。这类内容的 E-E-A-T 标准被 Google 显著提高。

中文搜索引擎在医疗、金融领域有更严格的资质审核（"百度医典"、"百度健康"等专项），可视为 YMYL 的本地化实现。

**Slug**：`ymyl`

## 平台 slug 规范

平台 slug 全小写、英文 / 拼音、连字符分隔。下表是已确认的 slug：

### 传统搜索

| Slug | 名称 |
|------|------|
| `baidu` | 百度搜索 |
| `bing-cn` | 必应中文 |
| `shenma` | 神马搜索 |
| `sogou` | 搜狗搜索 |
| `360-search` | 360 搜索 |

### 内容平台站内搜索

| Slug | 名称 |
|------|------|
| `xiaohongshu` | 小红书 |
| `zhihu` | 知乎 |
| `weixin` | 微信（搜一搜 / 公众号 / 视频号统称） |
| `weixin-sousou` | 微信搜一搜（搜索功能特指） |
| `weixin-mp` | 微信公众号 |
| `weixin-channels` | 微信视频号 |
| `bilibili` | B 站 |
| `douyin` | 抖音 |
| `kuaishou` | 快手 |
| `weibo` | 微博 |

### 生成式引擎

| Slug | 名称 |
|------|------|
| `doubao` | 豆包（字节） |
| `qianwen` | 通义千问 / 千问 APP（阿里） |
| `deepseek` | DeepSeek |
| `yuanbao` | 腾讯元宝 |
| `wenxin` | 文心一言（百度） |
| `kimi` | Kimi（月之暗面） |
| `chatgpt-cn` | ChatGPT 在中文 query 下的行为 |
| `perplexity-cn` | Perplexity 在中文 query 下的行为 |
| `claude-cn` | Claude 在中文 query 下的行为 |
| `gemini-cn` | Gemini 在中文 query 下的行为 |

> 注：通义 APP 在 2026 年品牌已统一为"千问"，slug 用 `qianwen`。

## 技术标签 slug 规范

技术标签全小写、英文、连字符。已确认的 slug：

| Slug | 含义 |
|------|------|
| `structured-data` | 结构化数据（Schema.org、JSON-LD、微数据） |
| `eeat-cn` | 中文语境的 E-E-A-T 类比信号 |
| `llm-citation` | LLM 引用机制 |
| `citation-attribution` | 引用归因机制 |
| `prompt-level-seo` | Prompt 层面的可见性优化 |
| `long-tail-keyword` | 长尾关键词挖掘 |
| `knowledge-graph` | 知识图谱与百科收录 |
| `on-platform-search` | 站内搜索机制 |
| `icp-and-subject` | ICP 备案 / 主体认证 |
| `featured-result` | 特型 / 特型卡相关 |
| `visibility-monitoring` | 可见性监测方法 |
| `geo-experiment` | GEO 实验设计 |

## 行业 slug 规范

| Slug | 含义 |
|------|------|
| `saas` | SaaS / 软件服务 |
| `ecommerce` | 电商 |
| `cross-border-ecommerce` | 跨境电商（出海） |
| `local-services` | 本地生活服务 |
| `cosmetics` | 美妆个护 |
| `b2b-services` | B2B 服务 |
| `education` | 教培 |
| `healthcare` | 医疗健康（YMYL） |
| `finance` | 金融（YMYL） |
| `consumer-electronics` | 消费电子 |

## 维护规则

- 新增 slug 走 PR，PR 描述里说明新增理由
- 已使用的 slug 不轻易重命名（会让历史卡片失效）
- 同义词在术语条目里写入 `aliases`，不创建多个 slug
- 每次重大 GEO/SEO 行业事件（新平台爆发、平台关停）后更新本表
