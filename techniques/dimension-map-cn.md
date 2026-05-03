---
title: 技术主题卡片维度索引地图（14 张卡 × 8 维度）
type: technique
sources:
  - url: ./README.md
    fetched_at: 2026-05-02
    note: 仓库 README，本卡是其技术卡片维度的显式化
  - url: https://openreview.net/forum?id=oTeixD3oZO
    fetched_at: 2026-05-02
    note: C-SEO Bench (NeurIPS 2025)，作为仓库整体怀疑基调的源头
confidence: medium
verified: true
last_verified: 2026-05-02
platforms:
  - baidu
  - shenma
  - sogou
  - 360-search
  - bing-cn
  - weixin-sousou
  - weixin-mp
  - weixin-channels
  - doubao
  - deepseek
  - wenxin
  - qianwen
  - yuanbao
  - kimi
  - xiaohongshu
  - zhihu
  - bilibili
  - douyin
  - weibo
techniques:
  - llm-citation
  - eeat-cn
  - icp-and-subject
  - citation-attribution
  - structured-data
  - knowledge-graph
  - prompt-level-seo
  - on-platform-search
  - geo-experiment
maturity: in-validation
related:
  - ../README.md
  - ../STATUS.md
  - ../BACKLOG.md
  - ../glossary/terms.md
last_updated: 2026-05-02
---

# 技术主题卡片维度索引地图

> ⚠️ **状态：in-validation**（结构层面已稳定——14 张卡 × 8 维度图谱显式化；具体卡片的元假说仍在 concept）
>
> 这张卡是**元卡**——不引入新内容，只把仓库 14 张技术主题卡的维度结构和卡间关系显式化。
>
> 服务于 4 类读者：
>
> 1. **新读者**：先读这张卡，再选感兴趣的维度切入
> 2. **被服务商话术困扰的决策者**：第 V 节按话术反查到对应反驳卡片
> 3. **不同主体类型的实践者**：第 VI 节按主体类型反查到适用卡片
> 4. **未来卡片作者**：第 VIII 节扩展原则避免维度重复 / 漂移
>
> ⚠️ **怀疑锚点 1**：维度划分是**为了便于检索**，不是命题——同一张卡可能在多个维度被引用，本卡按"主维度"归类
>
> ⚠️ **怀疑锚点 2**：8 维度图谱**不声称完整**——第 VII 节列出当前空缺维度

## 一、8 维度图谱

```
                                ┌──────────────────────────────────┐
                                │   D8 反话术总论维度（汇流点）     │
                                │   geo-roi-framework-cn           │
                                └─────────────┬────────────────────┘
                                              ↑
        ┌─────────────────────────────────────┴─────────────────────────────────────┐
        ↓                                                                           ↓
┌──────────────────────────┐                                          ┌──────────────────────────┐
│  D1 内容供给侧（7 张）   │←─────────────────────────────────────────│  D7 主体决策维度（1 张） │
│  ─ 理论基础              │                                          │  overseas-cn-deployment  │
│    princeton-9-strategies│                                          └──────────────────────────┘
│    eeat-cn               │
│  ─ 内容信号              │←─── ┌──────────────────────────┐
│    llms-txt-cn-practice  │     │  D2 用户输入侧（1 张）   │
│    structured-data       │     │  prompt-level-seo-cn     │
│  ─ 主体合规              │     └──────────────────────────┘
│    account-grade-systems │
│    icp-and-subject       │←─── ┌──────────────────────────┐
│  ─ 知识载体              │     │  D3 内容形态维度（1 张） │
│    knowledge-graph       │     │  multimodal-cn           │
└──────────────────────────┘     └──────────────────────────┘
        ↑       ↑       ↑
        │       │       │
        │       │       └─── ┌──────────────────────────┐
        │       │            │  D4 LLM 输出维度（1 张） │
        │       │            │  citation-attribution    │
        │       │            └──────────────────────────┘
        │       │
        │       └────────── ┌──────────────────────────┐
        │                   │  D5 信源属性维度（1 张） │
        │                   │  private-vs-public-source│
        │                   └──────────────────────────┘
        │
        └────────────────── ┌──────────────────────────┐
                            │  D6 结构因果维度（1 张） │
                            │  platform-search-blockade│
                            └──────────────────────────┘
```

**维度间关系**：

- **D1 内容供给侧**是基础——其他维度都建立在内容供给的实操基础上
- **D6 结构因果维度**（封锁结构）解释了为什么 D5 信源属性 / D7 主体决策 / D1 主体合规要分别处理——封锁是中文场景独有的硬约束
- **D8 反话术总论维度**是汇流点——前 7 维度的元假说收敛到 D8 形成 ROI 决策框架
- **D2-D4** 是非内容供给侧的 3 个独立角度（用户输入 / 内容形态 / LLM 输出）

## 二、14 张卡按维度分组（带元假说强度概览）

### D1 内容供给侧（7 张）

| 卡片 | 主题 | 元假说数 | 最强反话术假说 |
|------|------|---------|---------------|
| [`princeton-9-strategies-cn`](./princeton-9-strategies-cn.md) | Princeton 9 策略中文场景适配 | 4 | B：生态内信源 > 生态外权威信源 |
| [`eeat-cn`](./eeat-cn.md) | 中文场景 E-E-A-T 类比信号 | 5 | B：中文 LLM 直接用自家生态作权威性代理（不复用底层搜索 E-E-A-T） |
| [`llms-txt-cn-practice`](./llms-txt-cn-practice.md) | llms.txt 中文采纳现状 | 4 | A：中文 LLM 全部不尊重 llms.txt |
| [`structured-data-cn-practice`](./structured-data-cn-practice.md) | Schema.org / JSON-LD 中文采纳 | 5 | B：schema 对中文 LLM 引用率边际效应接近 0 |
| [`account-grade-systems-cn`](./account-grade-systems-cn.md) | "号"主体绑定 + 账号等级体系 | 5 | D：L3 数字等级对外部 LLM 引用几乎无效 |
| [`icp-and-subject-cn`](./icp-and-subject-cn.md) | ICP 备案 + 行业资质 + 主体认证 | 5 | C：算法备案与内容站 GEO 是类别错误 |
| [`knowledge-graph-cn`](./knowledge-graph-cn.md) | 知识图谱与百科生态 | 5 | E：维基中文是 GEO 不可优化的硬基线 |

### D2 用户输入维度（1 张）

| 卡片 | 主题 | 元假说数 | 最强反话术假说 |
|------|------|---------|---------------|
| [`prompt-level-seo-cn`](./prompt-level-seo-cn.md) | Prompt-level SEO 中文适用性 | 5 | E：tokenizer 优化是伪需求 |

### D3 内容形态维度（1 张）

| 卡片 | 主题 | 元假说数 | 最强反话术假说 |
|------|------|---------|---------------|
| [`multimodal-cn`](./multimodal-cn.md) | 多模态信源（图 / 视频 / 音频 / PDF）采纳 | 5 | D：图里文字 > alt 标签（反直觉） |

### D4 LLM 输出维度（1 张）

| 卡片 | 主题 | 元假说数 | 最强反话术假说 |
|------|------|---------|---------------|
| [`citation-attribution-styles-cn`](./citation-attribution-styles-cn.md) | 中文 LLM 引用归因形态 | 5 | A：中文 LLM 引用源 CTR < 1% |

### D5 信源属性维度（1 张）

| 卡片 | 主题 | 元假说数 | 最强反话术假说 |
|------|------|---------|---------------|
| [`private-vs-public-source-cn`](./private-vs-public-source-cn.md) | 私域 vs 公域信源 5 档光谱 | 5 | B：公众号矩阵仅在元宝 / 微信搜一搜成立 |

### D6 结构因果维度（1 张）

| 卡片 | 主题 | 元假说数 | 最强反话术假说 |
|------|------|---------|---------------|
| [`platform-search-blockade-cn`](./platform-search-blockade-cn.md) | 中文平台间搜索 / 跳转 / 收录封锁 | 5 | C：互联互通政策对 LLM 引用率影响接近 0 |

### D7 主体决策维度（1 张）

| 卡片 | 主题 | 元假说数 | 最强反话术假说 |
|------|------|---------|---------------|
| [`overseas-cn-deployment`](./overseas-cn-deployment.md) | 出海品牌中文 GEO 部署路径 | 5 | D：70% 隐性成本在内容审查不在技术部署 |

### D8 反话术总论维度（1 张）

| 卡片 | 主题 | 元假说数 | 最强反话术假说 |
|------|------|---------|---------------|
| [`geo-roi-framework-cn`](./geo-roi-framework-cn.md) | GEO ROI 评估框架 | 5 | C：机会成本是最常被服务商隐藏项 |

**统计**：14 张卡 × 平均 4.86 条元假说 = **68 条元假说**，全部 concept 待实证。

## 三、卡片间引用关系图

主要"引用方 → 被引用方"关系（仅列高频）：

```
geo-roi-framework-cn  ────→  citation-attribution-styles-cn  (扩展两层模型)
                       ────→  account-grade-systems-cn        (合规层)
                       ────→  icp-and-subject-cn              (合规层)
                       ────→  overseas-cn-deployment          (主体差异 4.4)
                       ────→  prompt-level-seo-cn             (用户问法覆盖)
                       ────→  multimodal-cn                   (内容形态选择)
                       ────→  knowledge-graph-cn              (信源载体)

overseas-cn-deployment ────→  icp-and-subject-cn              (主体合规层)
                       ────→  platform-search-blockade-cn     (路径 E 解释)
                       ────→  private-vs-public-source-cn     (公开度档位)
                       ────→  account-grade-systems-cn        (账号矩阵)

platform-search-blockade ──→  private-vs-public-source-cn     (因果上游)
                       ────→  account-grade-systems-cn        (生态矩阵动因)

private-vs-public-source ──→  account-grade-systems-cn        (主体合规)
                       ────→  icp-and-subject-cn              (L1 公开前提)
                       ────→  llms-txt-cn-practice            (L1 部署前提)
                       ────→  multimodal-cn                   (L3 路径)

citation-attribution   ────→  multimodal-cn                   (卡片化形态)
                       ────→  prompt-level-seo-cn             (因果上下游)
                       ────→  knowledge-graph-cn              (双形态对照)
                       ────→  eeat-cn                         (信号价值积累)

multimodal-cn          ────→  structured-data-cn-practice     (schema 互补)
                       ────→  knowledge-graph-cn              (百科图文)

prompt-level-seo-cn    ────→  princeton-9-strategies-cn       (第 9 策略)
                       ────→  structured-data-cn-practice     (元假说同源)
                       ────→  knowledge-graph-cn              (用户问法覆盖载体)

knowledge-graph-cn     ────→  eeat-cn                         (生态权威性代理)
                       ────→  account-grade-systems-cn        (编辑门槛 = L3 等级)
                       ────→  structured-data-cn-practice     (跨变量失效同源)

structured-data-cn     ────→  llms-txt-cn-practice            (元数据维度互补)
                       ────→  eeat-cn                         (文心是唯一)

account-grade-systems  ────→  eeat-cn                         (元假说 E 展开)
                       ────→  princeton-9-strategies-cn       (Princeton B 强化)

icp-and-subject-cn     ────→  account-grade-systems-cn        (L1 层深挖)
                       ────→  eeat-cn                         (Trustworthiness 拆层)
```

**关键模式**：

- 大多数关系是**上游 → 下游**（基础卡 → 应用卡），少有循环引用
- **`geo-roi-framework-cn` 是最广引用方**（汇流点）
- **`eeat-cn` + `account-grade-systems-cn` + `icp-and-subject-cn` 是最广被引用方**（基础设施）
- D7 + D8 维度是"应用层"，引用 D1-D6 维度的"原理层"

## 四、强假说集（仓库的反话术武器库）

按"反驳力度"分级：

### 4.1 ⭐⭐⭐ 直接打脸高频服务商话术

| 假说 | 来自 | 打脸什么话术 |
|------|------|--------------|
| `llms-txt` 元假说 A：中文 LLM 全部不尊重 llms.txt | [`llms-txt-cn-practice`](./llms-txt-cn-practice.md) | "做 llms.txt 让 AI 优先抓取" |
| `eeat-cn` 元假说 B：中文 LLM 直接用自家生态作权威性代理 | [`eeat-cn`](./eeat-cn.md) | "提升 E-E-A-T 大幅提升 AI 引用率" |
| `structured-data` 元假说 B：schema 对中文 LLM 边际效应接近 0 | [`structured-data-cn-practice`](./structured-data-cn-practice.md) | "做 schema → AI 引用率翻倍" |
| `account-grade` 元假说 D：L3 数字等级对外部 LLM 引用几乎无效 | [`account-grade-systems-cn`](./account-grade-systems-cn.md) | "提升账号等级套餐" |
| `icp-and-subject` 元假说 C：算法备案与内容站 GEO 是类别错误 | [`icp-and-subject-cn`](./icp-and-subject-cn.md) | "做生成式 AI 备案提升引用率" |
| `prompt-level-seo` 元假说 E：tokenizer 优化是伪需求 | [`prompt-level-seo-cn`](./prompt-level-seo-cn.md) | "针对 X LLM tokenizer 优化" |
| `multimodal` 元假说 B：图片 alt 优化对 LLM 引用率边际效应接近 0 | [`multimodal-cn`](./multimodal-cn.md) | "做图片 alt 提升 AI 引用" |
| `citation-attribution` 元假说 A：中文 LLM 引用源 CTR < 1% | [`citation-attribution-styles-cn`](./citation-attribution-styles-cn.md) | "被 AI 引用 = AI 时代 SEO 流量" |
| `private-vs-public` 元假说 B：公众号矩阵仅在元宝 / 微信搜一搜成立 | [`private-vs-public-source-cn`](./private-vs-public-source-cn.md) | "公众号矩阵覆盖所有 AI" |
| `platform-search-blockade` 元假说 C：互联互通对 LLM 引用率影响接近 0 | [`platform-search-blockade-cn`](./platform-search-blockade-cn.md) | "互联互通后单点覆盖" |
| `overseas` 元假说 D：70% 隐性成本在内容审查不在技术部署 | [`overseas-cn-deployment`](./overseas-cn-deployment.md) | "建站 + 翻译 = 中文 GEO" |
| `geo-roi-framework` 元假说 C：机会成本是最常被隐藏项 | [`geo-roi-framework-cn`](./geo-roi-framework-cn.md) | "GEO 是 AI 时代必投" |

### 4.2 ⭐⭐ 反直觉的实操结论

| 假说 | 来自 | 含义 |
|------|------|------|
| `multimodal` 元假说 D：图里文字 > alt 标签 | [`multimodal-cn`](./multimodal-cn.md) | 中文场景反向优化 |
| `knowledge-graph` 元假说 E：维基中文是 GEO 不可优化的硬基线 | [`knowledge-graph-cn`](./knowledge-graph-cn.md) | 看得见够不着 |
| `geo-roi-framework` 元假说 A：中小新品牌中文 GEO ROI 结构性低于英文 | [`geo-roi-framework-cn`](./geo-roi-framework-cn.md) | 不是普世建议 |

## 五、按服务商话术索引（"X 话术对吗"反查表）

| 听到的话术 | 反查卡片 | 卡片判定 |
|------------|----------|----------|
| "做 schema 提升 AI 引用" | [`structured-data-cn-practice`](./structured-data-cn-practice.md) 第 7 节 | ❌ 大概率无效 |
| "做 llms.txt 让 AI 优先抓取" | [`llms-txt-cn-practice`](./llms-txt-cn-practice.md) | ❌ 中文 LLM 都不尊重 |
| "提升 E-E-A-T 信号" | [`eeat-cn`](./eeat-cn.md) 第 8 节 | ⚠️ 概念是术语借用 |
| "提升账号等级 N 档 = 引用率 +X%" | [`account-grade-systems-cn`](./account-grade-systems-cn.md) 第 8 节 | ❌ 因果链 4 段拆解 |
| "做生成式 AI 备案" | [`icp-and-subject-cn`](./icp-and-subject-cn.md) 第 7 节 | ❌ 类别错误 |
| "做百度百科保 AI 引用" | [`knowledge-graph-cn`](./knowledge-graph-cn.md) 第 7 节 | ⚠️ 仅文心成立 |
| "针对 X LLM tokenizer 优化" | [`prompt-level-seo-cn`](./prompt-level-seo-cn.md) 第 7 节 | ❌ 伪需求 |
| "做图片 alt / VideoObject schema" | [`multimodal-cn`](./multimodal-cn.md) 第 7 节 | ❌ 大概率无效 |
| "被 AI 引用 = AI 时代 SEO" | [`citation-attribution-styles-cn`](./citation-attribution-styles-cn.md) 第 6 节 | ❌ 量级错觉 |
| "公众号矩阵覆盖所有 AI" | [`private-vs-public-source-cn`](./private-vs-public-source-cn.md) 第 7 节 | ❌ 仅元宝成立 |
| "互联互通后单点覆盖" | [`platform-search-blockade-cn`](./platform-search-blockade-cn.md) 第 7 节 | ❌ 政策误读 |
| "建站 + 翻译 = 中文 GEO" | [`overseas-cn-deployment`](./overseas-cn-deployment.md) 第 7 节 | ❌ 主体 / 内容混淆 |
| "GEO 套餐 X 元 = AI 必引" | [`geo-roi-framework-cn`](./geo-roi-framework-cn.md) 第 9 节 | ❌ 单一 KPI 误导 |

## 六、按主体决策索引（"我是 X，应该看哪些卡"）

| 主体类型 | 推荐阅读顺序 | 核心结论提示 |
|---------|--------------|--------------|
| **中小新品牌**（无品牌识别度） | `geo-roi-framework-cn` 4.1 → `private-vs-public-source-cn` → `account-grade-systems-cn` | GEO 投入控制在 < 20% 营销预算；优先短视频 + 私域 |
| **中型品牌**（部分品牌识别度） | `geo-roi-framework-cn` 4.2 → `account-grade-systems-cn` → `prompt-level-seo-cn` → `multimodal-cn` | C+E 组合（代理备案 + 4-6 平台账号矩阵） |
| **大型品牌**（强品牌识别度） | `geo-roi-framework-cn` 4.3 → `icp-and-subject-cn` → 其余各卡 | GEO 视为"品牌强化的低成本辅助"，不是流量来源 |
| **出海品牌** | `overseas-cn-deployment` → `icp-and-subject-cn` → `geo-roi-framework-cn` 4.4 | 5 路径选择，70% 隐性成本在内容审查 |
| **YMYL 类持牌主体** | `eeat-cn` → `icp-and-subject-cn` → `geo-roi-framework-cn` 4.5 | 边际 GEO 投入 ROI 反而高（固定成本沉没） |
| **B2B / SaaS 类** | `prompt-level-seo-cn` → `private-vs-public-source-cn` → `geo-roi-framework-cn` 5 行业表 | 知乎 + B 站等技术社区为主战场；受访问限制 |
| **本地生活服务** | `geo-roi-framework-cn` 5 行业表 → `eeat-cn` | LBS 类 query + 美团 / 大众点评等平台依赖 |

## 七、当前空缺 / 未覆盖维度（自我批判）

仓库当前 14 张卡 × 8 维度**不声称完整**，已知空缺：

| 空缺维度 | 描述 | 为何空缺 |
|---------|------|----------|
| **LLM 内部机制侧** | 训练数据筛选 / RAG 实现 / query rewrite 内部规则 | 厂商均不公开——信息黑箱 |
| **时间维度** | 单张卡的纵向变化 / 平台 changelog 系列 | 已在 BACKLOG（[`platform-baidu-changelog`](../BACKLOG.md) 等待建） |
| **用户行为侧** | 实际中文用户怎么和 LLM 互动（query 长度 / 重复率 / 转化路径） | 行业开放数据空白 |
| **法律 vs 平台政策细化** | 反垄断 + 互联互通 + 平台规则的精细化对照 | 已在 BACKLOG（[`tech-cn-anti-monopoly-and-geo-roadmap`](../BACKLOG.md)） |
| **工具 / 服务商详细评测** | 国内 GEO 工具栈实测 | 仓库故意留白（[`BACKLOG.md`](../BACKLOG.md) 工具评测段已占位） |
| **中外对照实证** | 同主题中英文场景下的 GEO 量化对比 | 大多元假说待实证（[`geo-roi-framework-cn`](./geo-roi-framework-cn.md) 实验 1） |
| **企业内部知识库 → 公开化的决策框架** | B2B / 企业服务的 GEO 起步 | 已在 BACKLOG（`tech-cn-corporate-knowledge-geo`） |
| **垂类百科 / 知识库** | 萌娘百科 / MBA 智库 / 学术领域知识库 | 已在 BACKLOG（`tech-cn-vertical-wiki-and-domain-knowledge`） |

## 八、读卡建议路径

### 8.1 完全新读者（< 1 小时阅读时间）

1. [`README.md`](../README.md)（仓库整体定位）
2. 本卡（维度全景）
3. [`geo-roi-framework-cn`](./geo-roi-framework-cn.md) 第 1-4 节（投入 / 产出 / 错误 / 主体差异）
4. 按主体类型从第 VI 节挑 1-2 张深度卡

### 8.2 决策者（要不要做 GEO）

1. 本卡第 V + VI 节（按话术 + 按主体反查）
2. [`geo-roi-framework-cn`](./geo-roi-framework-cn.md) 全文
3. [`citation-attribution-styles-cn`](./citation-attribution-styles-cn.md) 第 2 节（信号价值 vs 回流价值）
4. 按行业从 ROI 卡 5 行业表跳转到对应深度卡

### 8.3 实践者（已决定做 GEO）

1. [`geo-roi-framework-cn`](./geo-roi-framework-cn.md) 第 6 节（投入优先级排序）
2. 按优先级 1-5 顺序，每项跳转到对应深度卡
3. 关注每张卡的"不做的事"段——避免低 ROI 微优化

### 8.4 研究者（关注实证缺口）

1. 本卡第 VII 节（空缺维度）
2. 各卡的"实验设计建议"段
3. [`STATUS.md`](../STATUS.md) 第三节（仓库三大卡住点）
4. [`experiments/`](../experiments/)（实验设计 + query 集 + 工具栈）

### 8.5 仓库贡献者（写新卡）

1. 本卡第 VIII 节（扩展原则）
2. [`CONTRIBUTING.md`](../CONTRIBUTING.md)（卡片格式约定）
3. [`templates/`](../templates/)（卡片模板）
4. 检查新卡是否落在已有 8 维度

## 九、未来扩展原则（避免维度漂移）

新卡片应通过以下检查：

| 检查项 | 描述 |
|--------|------|
| **维度归属** | 落在已有 8 维度之一？如不在，独立性 + 价值需要论证 |
| **避免重复** | 与已有 14 张卡的关系是"展开 / 衍生"还是"重复"？后者不应建卡 |
| **元假说密度** | 每张技术卡应包含 ≥ 4 条元假说，否则可能是"事实层卡片"应单列类型 |
| **怀疑锚点** | 顶部 ≥ 3 条怀疑锚点（含 C-SEO Bench 这一仓库通用锚点） |
| **服务商话术对照** | 第 7 节"与 GEO 服务商话术的对照"必须有，明确判定 |
| **不做的事** | 第 9 / 10 节明确禁区，避免功能蔓延 |
| **衍生 BACKLOG** | 末段必须有 3-5 条衍生待办，让卡片成为"源头"而非"终点" |

**不应建新卡的情况**：

- 已有卡的某段可以扩写，应该在原卡里更新而不是新建
- 主题与现有卡 ≥ 70% 重叠
- 主题是单平台细节（应放 [`platforms/<slug>/`](../platforms/) 而非 [`techniques/`](.)）
- 主题是单实验设计（应放 [`experiments/`](../experiments/) 而非 [`techniques/`](.)）

## 十、不做的事

- **不重复 14 张卡的具体内容**——本卡只做组织 / 索引 / 元数据
- **不在本卡引入新的元假说**——元假说全部在原卡内
- **不评判维度的优先级**——8 维度互相补充，无主次
- **不预先设计第 15 张卡**——按 BACKLOG 节奏自然推进

## 十一、变更记录

- 2026-05-02：初版。14 张卡 × 8 维度图谱显式化 + 卡间关系图 + 强假说集 + 服务商话术索引 + 主体决策索引 + 空缺维度 + 读卡建议路径 + 扩展原则。
