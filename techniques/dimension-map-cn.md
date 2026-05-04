---
title: 技术主题卡片维度索引地图（16 张卡 × D0 + D1-D8 + DS 三轴）
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
last_verified: 2026-05-03
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
  - geo-demand-side-fitness
  - geo-business-model-taxonomy
maturity: in-validation
related:
  - ../README.md
  - ../STATUS.md
  - ../BACKLOG.md
  - ../glossary/terms.md
  - ./geo-demand-side-fitness-cn.md
  - ./geo-business-model-taxonomy-cn.md
  - ../case-studies/wordtrace-vendor-pitch-decon-2026-05.md
  - ../docs/meeting-2026-05-03-geo-demand-and-business-model.md
last_updated: 2026-05-03
---

# 技术主题卡片维度索引地图

> ⚠️ **状态：in-validation**（结构层面已稳定——16 张卡 × **D0 + D1-D8 + DS 三轴**结构显式化；具体卡片的元假说仍在 concept）
>
> 这张卡是**元卡**——不引入新内容，只把仓库 16 张技术主题卡的维度结构和卡间关系显式化。
>
> 服务于 4 类读者：
>
> 1. **新读者**：先读这张卡，再选感兴趣的轴 / 维度切入
> 2. **被服务商话术困扰的决策者**：第 V 节按话术反查到对应反驳卡片
> 3. **不同主体类型的实践者**：第 VI 节按主体类型反查到适用卡片
> 4. **未来卡片作者**：第 IX 节扩展原则避免维度重复 / 漂移
>
> ⚠️ **怀疑锚点 1**：维度划分是**为了便于检索**，不是命题——同一张卡可能在多个维度被引用，本卡按"主维度"归类
>
> ⚠️ **怀疑锚点 2**：三轴结构（D0 / D1-D8 / DS）**不声称完整**——第 VII 节列出当前空缺
>
> ⚠️ **怀疑锚点 3（2026-05-03 升级）**：原 8 维度（D1-D8）全部为**信号侧**视角，假设"用户在用 LLM 做决策"且"GEO 业务模式存在"。三轴结构补全两个被假设掉的前提：**D0 需求侧前置**（用户是否真在 LLM 上做该类决策）+ **DS 供给侧**（GEO 业务在什么模式下存在）。三轴一起才是完整的研究地图

## 一、三轴维度图谱

```
┌─────────────────────────────────────────────────────────────────────┐
│  D0 需求侧前置维度（1 张）                                          │
│  geo-demand-side-fitness-cn                                         │
│  → 用户层 / 场景层 / 决策路径位置层 / 4 类窄场景                    │
│  ⚠️ 前置于所有 D1-D8——需求不在，信号优化无意义                      │
└──────────────────────────────────┬──────────────────────────────────┘
                                   ↓
┌─────────────────────────────────────────────────────────────────────┐
│                D1-D8 信号侧 8 维度（14 张卡）                       │
│                                                                     │
│                  ┌───────────────────────────────────────────────┐  │
│                  │   D8 反话术总论维度（汇流点）                  │  │
│                  │   geo-roi-framework-cn                        │  │
│                  └─────────────┬─────────────────────────────────┘  │
│                                ↑                                    │
│        ┌───────────────────────┴────────────────────────┐           │
│        ↓                                                ↓           │
│  ┌─────────────────────┐                  ┌─────────────────────┐   │
│  │ D1 内容供给侧 (7张) │←─────────────────│ D7 主体决策维度(1张)│   │
│  │ princeton-9         │                  │ overseas-cn-deploy  │   │
│  │ eeat-cn             │                  └─────────────────────┘   │
│  │ llms-txt            │                                            │
│  │ structured-data     │←── ┌─────────────────────┐                 │
│  │ account-grade       │    │ D2 用户输入侧 (1张) │                 │
│  │ icp-and-subject     │    │ prompt-level-seo    │                 │
│  │ knowledge-graph     │    └─────────────────────┘                 │
│  └─────────────────────┘                                            │
│        ↑       ↑       ↑                                            │
│        │       │       └── ┌─────────────────────┐                  │
│        │       │           │ D3 内容形态 (1张)   │                  │
│        │       │           │ multimodal-cn       │                  │
│        │       │           └─────────────────────┘                  │
│        │       │                                                    │
│        │       └─────────── ┌─────────────────────┐                 │
│        │                    │ D4 LLM 输出 (1张)   │                 │
│        │                    │ citation-attribution│                 │
│        │                    └─────────────────────┘                 │
│        │                                                            │
│        └────────────────── ┌─────────────────────┐                  │
│                            │ D5 信源属性 (1张)   │                  │
│                            │ private-vs-public   │                  │
│                            └─────────────────────┘                  │
│                            ┌─────────────────────┐                  │
│                            │ D6 结构因果 (1张)   │                  │
│                            │ platform-blockade   │                  │
│                            └─────────────────────┘                  │
└──────────────────────────────────┬──────────────────────────────────┘
                                   ↓
┌─────────────────────────────────────────────────────────────────────┐
│  DS 供给侧维度（1 张）                                              │
│  geo-business-model-taxonomy-cn                                     │
│  → 八层商业模式 × 平台原生功能取代风险（2026-05-04 加 h 层横向扩展） │
│  ⚠️ 后置于 D1-D8——业务模式建立在信号有效性 + 客户付费意愿之上        │
└─────────────────────────────────────────────────────────────────────┘
```

**三轴间的因果关系**：

- **D0 是前置约束**：需求场景决定 D1-D8 的实施目标（4 类窄场景外的信号优化是空跑）
- **D1-D8 是信号机制**：14 张卡讨论"什么信号 → LLM 引用率"的因果
- **DS 是后置变现**：业务模式建立在 D1-D8 的有效性 + D0 的需求规模上

**三轴一起回答的总问题**：在中文 LLM 生态下，**有谁在用 LLM 做决策**（D0），**什么信号能影响其决策结果**（D1-D8），**什么商业模式能在这条价值链上稳定存在**（DS）？

**信号侧 D1-D8 内部关系**（保留原 8 维度内部结构）：

- D1 内容供给侧是基础——其他维度都建立在内容供给的实操基础上
- D6 结构因果维度（封锁结构）解释了为什么 D5 信源属性 / D7 主体决策 / D1 主体合规要分别处理——封锁是中文场景独有的硬约束
- D8 反话术总论维度是汇流点——前 7 维度的元假说收敛到 D8 形成 ROI 决策框架
- D2-D4 是非内容供给侧的 3 个独立角度（用户输入 / 内容形态 / LLM 输出）

## 二、16 张卡按三轴分组（带元假说强度概览）

### D0 需求侧前置维度（1 张）

| 卡片 | 主题 | 元假说数 | 最强反话术假说 |
|------|------|---------|---------------|
| [`geo-demand-side-fitness-cn`](./geo-demand-side-fitness-cn.md) | GEO 需求侧场景适配地图 | 5 | C：⭐⭐⭐ 服务商客户画像越宽 → 销售在勉强匹配市场 |

### D1 内容供给侧（7 张）

| 卡片 | 主题 | 元假说数 | 最强反话术假说 |
|------|------|---------|---------------|
| [`princeton-9-strategies-cn`](./princeton-9-strategies-cn.md) | Princeton 9 策略中文场景适配 | 4 | B：生态内信源 > 生态外权威信源 |
| [`eeat-cn`](./eeat-cn.md) | 中文场景 E-E-A-T 类比信号 | 5 | B：中文 LLM 直接用自家生态作权威性代理 |
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

### DS 供给侧维度（1 主卡 + 1 子卡）

| 卡片 | 主题 | 元假说数 | 最强反话术假说 |
|------|------|---------|---------------|
| [`geo-business-model-taxonomy-cn`](./geo-business-model-taxonomy-cn.md) | GEO 商业模式八层分类（主卡，2026-05-04 七层 → 八层） | 6 | A：⭐⭐⭐ LLM 平台一旦自建广告位，c/d 层中介模式整体被腰斩 🔄 已降级 |
| [`anti-geo-monitoring-cn`](./anti-geo-monitoring-cn.md) | 反 GEO 监测：防御侧赛道（DS 元假说 C 具体展开 / 子卡） | 7 | A：⭐⭐⭐ 反 GEO 监测真实需求规模与进攻型 GEO 相当甚至更大 |

**统计（2026-05-03 二次更新后）**：

| 轴 | 卡片数 | 元假说数 |
|---|--------|--------|
| D0 需求侧 | 1 | 5 |
| D1-D8 信号侧 | 14 | 68 |
| DS 供给侧 | 1 主 + 1 子 = 2 | 6 + 7 = 13 |
| **合计** | **17** | **86** |

平均 5.06 条元假说 / 卡。**全部 86 条仍为 concept 待实证**。

## 三、卡片间引用关系图

新增（D0 / DS 与 D1-D8 的关系）：

```
geo-demand-side-fitness-cn ────→  citation-attribution-styles-cn  (CTR<1% 印证 LLM 不是流量入口)
                          ────→  geo-roi-framework-cn             (互补：需求 vs 决策)
                          ────→  overseas-cn-deployment           (跨语言场景 = 4 窄场景之一)
                          ────→  prompt-level-seo-cn              (限定适用范围)

geo-business-model-taxonomy-cn ─→  geo-demand-side-fitness-cn      (前置依赖：需求决定模式)
                          ────→  geo-roi-framework-cn             (互补：供给 vs 决策)
                          ────→  platform-search-blockade-cn      (平台原生功能取代风险预判)
                          ────→  citation-attribution-styles-cn   (CTR<1% 限制流量分成型变现)
                          ────→  private-vs-public-source-cn      (c 层模式细分边界)
                          ────→  overseas-cn-deployment           (跨语言陪跑细分)
```

D1-D8 内部引用关系（保留原结构）：

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

- 三轴间是**前置 → 信号 → 后置**链：D0 → D1-D8 → DS
- D1-D8 内部大多数关系是**上游 → 下游**（基础卡 → 应用卡），少有循环引用
- **`geo-roi-framework-cn`** 是 D1-D8 内最广引用方（汇流点）
- **`geo-demand-side-fitness-cn`** 和 **`geo-business-model-taxonomy-cn`** 都引用 `geo-roi-framework-cn` 作为决策侧锚点
- D0、D7（出海）、D8（ROI）、DS 是"应用层"，引用 D1-D6 维度的"原理层"

## 四、强假说集（仓库的反话术武器库）

按"反驳力度"分级。**2026-05-03 升级后纳入 D0 + DS 新假说**：

### 4.1 ⭐⭐⭐ 直接打脸高频服务商话术

> 🔄 **2026-05-04 审计降级标注**（[`audits/2026-05-04_meta-hypothesis-audit.md`](../audits/2026-05-04_meta-hypothesis-audit.md)）：以下假说中 **DS-主-A（c/d 层被广告位腰斩）已被审计判 ✗**——平台变现路径 F7 不是凤巢式竞价，是订阅+电商佣金混合，原假说"广告位"作为单一最大风险被证伪（方向对形态错）。**D0 元假说 C（画像越宽=销售勉强匹配）已被审计判 ✗**——逻辑只在尾部草莽期玩家成立，对头部 / 腰部不成立（迈富时 21 万企业客户 + 世界 500 强 80+；智推时代客户跨 4 行业但都是大客户）。本表保留原文，正式重写在 P1 修订集中执行时一起做。

| 假说 | 来自 | 打脸什么话术 |
|------|------|--------------|
| **D0** `demand-side` 元假说 C：服务商客户画像越宽，越说明销售在勉强匹配市场 🔄 已降级 | [`geo-demand-side-fitness-cn`](./geo-demand-side-fitness-cn.md) | "GEO 适用所有行业 / 所有企业必投" |
| **D0** `demand-side` 元假说 E："用 LLM" vs "通过 LLM 做决策"是数量级不同的两个市场 | [`geo-demand-side-fitness-cn`](./geo-demand-side-fitness-cn.md) | "10 亿 AI 用户 = 10 亿 GEO 可寻址市场" |
| **D0** `demand-side` 元假说 A：中文消费决策路径中 LLM 是补充节点而非主节点 | [`geo-demand-side-fitness-cn`](./geo-demand-side-fitness-cn.md) | "AI 时代用户先问 AI 再下单" |
| **DS** `business-model` 元假说 A：LLM 平台一旦自建广告位，c/d 层中介模式整体被腰斩 🔄 已降级 | [`geo-business-model-taxonomy-cn`](./geo-business-model-taxonomy-cn.md) | "GEO 是 AI 时代长期赛道"（方向对形态错——实际是订阅+电商佣金 4 形态） |
| **DS** `business-model` 元假说 C：反 GEO 监测是被严重低估的对称赛道 | [`geo-business-model-taxonomy-cn`](./geo-business-model-taxonomy-cn.md) | "GEO 服务商之间竞争"（忽视防御侧） |
| **DS-子** `anti-geo` 元假说 A：反 GEO 监测真实需求规模与进攻型 GEO 相当甚至更大 | [`anti-geo-monitoring-cn`](./anti-geo-monitoring-cn.md) | "客户都是营销部门买单"（防御型客户是公关 + 法务） |
| **DS-子** `anti-geo` 元假说 C：反 GEO 监测的技术门槛比进攻型低（不需要 c/d 层） | [`anti-geo-monitoring-cn`](./anti-geo-monitoring-cn.md) | "GEO 全栈服务"（多数厂商所谓"全栈"是为了报价高） |
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
| **DS** `business-model` 元假说 D：标准 / 协议层是中文 GEO 长期最高 ROI 的位置 | [`geo-business-model-taxonomy-cn`](./geo-business-model-taxonomy-cn.md) | 第一推动者拿规则定价权 |
| **DS** `business-model` 元假说 F：垂直陪跑（B2B SaaS / YMYL）是平台风险下最稳的位置 | [`geo-business-model-taxonomy-cn`](./geo-business-model-taxonomy-cn.md) | 行业 know-how 比平台规则稳 |
| `multimodal` 元假说 D：图里文字 > alt 标签 | [`multimodal-cn`](./multimodal-cn.md) | 中文场景反向优化 |
| `knowledge-graph` 元假说 E：维基中文是 GEO 不可优化的硬基线 | [`knowledge-graph-cn`](./knowledge-graph-cn.md) | 看得见够不着 |
| `geo-roi-framework` 元假说 A：中小新品牌中文 GEO ROI 结构性低于英文 | [`geo-roi-framework-cn`](./geo-roi-framework-cn.md) | 不是普世建议 |

## 五、按服务商话术索引（"X 话术对吗"反查表）

| 听到的话术 | 反查卡片 | 卡片判定 |
|------------|----------|----------|
| **"GEO 适用所有行业 / 必修课"** | [`geo-demand-side-fitness-cn`](./geo-demand-side-fitness-cn.md) 元假说 C | ❌ 仅 4 类窄场景真有效 |
| **"10 亿 AI 用户 = GEO 大市场"** | [`geo-demand-side-fitness-cn`](./geo-demand-side-fitness-cn.md) 元假说 E | ❌ L1 ≠ L2 ≠ L3，数量级混淆 |
| **"AI 时代用户先问 AI 再下单"** | [`geo-demand-side-fitness-cn`](./geo-demand-side-fitness-cn.md) 元假说 A | ❌ 中文消费 LLM 是补充节点 |
| **"B2C 电商 / 跨境出海 / 本地服务做 GEO"** | [`geo-demand-side-fitness-cn`](./geo-demand-side-fitness-cn.md) 第 2.2 节 | ❌ 用户路径不在 LLM |
| **"GEO 是 AI 时代长期赛道"** | [`geo-business-model-taxonomy-cn`](./geo-business-model-taxonomy-cn.md) 元假说 A | ❌ 中介模式生命周期由平台决策定 |
| **"我们做的是 SaaS 模式扩张性强"** | [`geo-business-model-taxonomy-cn`](./geo-business-model-taxonomy-cn.md) 元假说 B | ⚠️ 多数所谓 SaaS 实际主收入仍是 RaaS |
| **"OEM / 源码模式护城河深"** | [`geo-business-model-taxonomy-cn`](./geo-business-model-taxonomy-cn.md) 第 2 节 e 层 | ❌ 同行二开稀释（千博系统剧本） |
| **"独家覆盖 N+ 平台"** | [`geo-business-model-taxonomy-cn`](./geo-business-model-taxonomy-cn.md) + [`platform-search-blockade-cn`](./platform-search-blockade-cn.md) | ❌ 平台改 UI 全部返工，覆盖广 = 技术债指数级 |
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
| **"效果按 query 计费"** | [`geo-business-model-taxonomy-cn`](./geo-business-model-taxonomy-cn.md) 第 5 节 | ✅ 是聪明的产品化（值得肯定） |

## 六、按主体决策索引（"我是 X，应该看哪些卡"）

> **2026-05-03 升级**：所有路径加 D0 [`geo-demand-side-fitness-cn`](./geo-demand-side-fitness-cn.md) 作为前置阅读，避免在需求场景错配的前提下做信号侧讨论。

| 主体类型 | 推荐阅读顺序 | 核心结论提示 |
|---------|--------------|--------------|
| **中小新品牌**（无品牌识别度） | **D0** → `geo-roi-framework-cn` 4.1 → `private-vs-public-source-cn` → `account-grade-systems-cn` | 先确认是否在 4 类窄场景；GEO 投入控制在 < 20% 营销预算；优先短视频 + 私域 |
| **中型品牌**（部分品牌识别度） | **D0** → `geo-roi-framework-cn` 4.2 → `account-grade-systems-cn` → `prompt-level-seo-cn` → `multimodal-cn` | C+E 组合（代理备案 + 4-6 平台账号矩阵） |
| **大型品牌**（强品牌识别度） | **D0** → `geo-roi-framework-cn` 4.3 → `icp-and-subject-cn` → 其余各卡 | GEO 视为"品牌强化的低成本辅助"，不是流量来源 |
| **出海品牌** | **D0** → `overseas-cn-deployment` → `icp-and-subject-cn` → `geo-roi-framework-cn` 4.4 | 5 路径选择，70% 隐性成本在内容审查 |
| **YMYL 类持牌主体** | **D0** → `eeat-cn` → `icp-and-subject-cn` → `geo-roi-framework-cn` 4.5 | 边际 GEO 投入 ROI 反而高（固定成本沉没） |
| **B2B / SaaS 类** | **D0** → `prompt-level-seo-cn` → `private-vs-public-source-cn` → `geo-roi-framework-cn` 5 行业表 | 知乎 + B 站等技术社区为主战场；受访问限制 |
| **本地生活服务** | **D0**（直接判定不做 GEO） | 用户路径在美团 / 大众点评 / 高德 / 微信 |
| **GEO 服务商 / 创业者** | **DS** → **D0** → `geo-roi-framework-cn` → 反看四象限模式 / 客户价值表 | 模式合理性 ≠ 客户价值；垂直 + 反向 / 防御 + 标准协议是空白 ⭐⭐⭐ |

## 七、当前空缺 / 未覆盖维度（自我批判）

仓库当前 16 张卡 × 三轴**不声称完整**，已知空缺。**2026-05-03 更新**：原 8 维度的 2 项空缺被新卡填补，新增供给侧 / 需求侧细化空缺。

| 空缺维度 | 描述 | 当前状态 |
|---------|------|----------|
| ~~需求侧（用户是否真用 LLM 做决策）~~ | ~~原 8 维度全部假设需求存在~~ | ✅ **已被 [`geo-demand-side-fitness-cn`](./geo-demand-side-fitness-cn.md) 填补**（2026-05-03） |
| ~~供给侧（GEO 业务在什么模式下存在）~~ | ~~原 8 维度全部假设业务模式存在~~ | ✅ **已被 [`geo-business-model-taxonomy-cn`](./geo-business-model-taxonomy-cn.md) 填补**（2026-05-03） |
| **LLM 内部机制侧** | 训练数据筛选 / RAG 实现 / query rewrite 内部规则 | 厂商均不公开——信息黑箱 |
| **时间维度** | 单张卡的纵向变化 / 平台 changelog 系列 | 已在 BACKLOG（[`platform-baidu-changelog`](../BACKLOG.md) 等待建） |
| **用户行为侧（细粒度）** | 实际中文用户怎么和 LLM 互动（query 长度 / 重复率 / 转化路径） | D0 卡给出宏观矩阵，细粒度行为待第三方调研（[`exp-cn-llm-decision-path-survey`](../BACKLOG.md)） |
| **法律 vs 平台政策细化** | 反垄断 + 互联互通 + 平台规则的精细化对照 | 已在 BACKLOG（`tech-cn-anti-monopoly-and-geo-roadmap`） |
| **工具 / 服务商详细评测** | 国内 GEO 工具栈实测 | 仓库故意留白（[`BACKLOG.md`](../BACKLOG.md) 工具评测段已占位） |
| **中外对照实证** | 同主题中英文场景下的 GEO 量化对比 | 大多元假说待实证 |
| **企业内部知识库 → 公开化的决策框架** | B2B / 企业服务的 GEO 起步 | 已在 BACKLOG（`tech-cn-corporate-knowledge-geo`） |
| **垂类百科 / 知识库** | 萌娘百科 / MBA 智库 / 学术领域知识库 | 已在 BACKLOG（`tech-cn-vertical-wiki-and-domain-knowledge`） |
| ~~DS 子空缺：反 GEO 监测专题~~ | ~~元假说 C 的具体展开~~ | ✅ **已被 [`anti-geo-monitoring-cn`](./anti-geo-monitoring-cn.md) 填补**（2026-05-03） |
| **DS 子空缺：信源池占有率密度** | 探词们的真实护城河，仓库结构空白 | 已在 BACKLOG（`tech-cn-geo-source-pool-density`） |
| **DS 子空缺：标准协议推动方监测** | 元假说 D 的纵向跟踪 | 已在 BACKLOG（`tech-cn-llms-txt-chinese-promoter-watch`） |

## 八、读卡建议路径

### 8.1 完全新读者（< 1 小时阅读时间）

1. [`README.md`](../README.md)（仓库整体定位）
2. 本卡（维度全景 + 三轴）
3. [`geo-demand-side-fitness-cn`](./geo-demand-side-fitness-cn.md) 第 II 节（4 类窄场景）—— **判断自己是否在有效场景内**
4. [`geo-roi-framework-cn`](./geo-roi-framework-cn.md) 第 1-4 节（投入 / 产出 / 错误 / 主体差异）
5. 按主体类型从第 VI 节挑 1-2 张深度卡

### 8.2 决策者（要不要做 GEO）

1. **先读 D0** [`geo-demand-side-fitness-cn`](./geo-demand-side-fitness-cn.md)——确认需求场景是否在 4 类窄区
2. 本卡第 V + VI 节（按话术 + 按主体反查）
3. [`geo-roi-framework-cn`](./geo-roi-framework-cn.md) 全文
4. [`citation-attribution-styles-cn`](./citation-attribution-styles-cn.md) 第 2 节（信号价值 vs 回流价值）
5. 按行业从 ROI 卡 5 行业表跳转到对应深度卡

### 8.3 实践者（已决定做 GEO）

1. **先读 D0**——确认场景前提没错
2. [`geo-roi-framework-cn`](./geo-roi-framework-cn.md) 第 6 节（投入优先级排序）
3. 按优先级 1-5 顺序，每项跳转到对应深度卡
4. 关注每张卡的"不做的事"段——避免低 ROI 微优化

### 8.4 研究者（关注实证缺口）

1. 本卡第 VII 节（空缺维度）
2. 各卡的"实验设计建议"段
3. [`STATUS.md`](../STATUS.md) 第三节（仓库三大卡住点）
4. [`experiments/`](../experiments/)（实验设计 + query 集 + 工具栈）

### 8.5 GEO 服务商 / 创业者（评估自身定位）

> **2026-05-03 新增路径**：基于 DS 维度卡。

1. [`geo-business-model-taxonomy-cn`](./geo-business-model-taxonomy-cn.md) 第 II 节八层 × 6 维度全表
2. [`geo-demand-side-fitness-cn`](./geo-demand-side-fitness-cn.md)——判断目标客户是否在真买家区
3. 自检：本公司在八层中位置 / 平台原生功能取代风险 / 客户价值 vs 模式合理性四象限
4. [`case-studies/wordtrace-vendor-pitch-decon-2026-05.md`](../case-studies/wordtrace-vendor-pitch-decon-2026-05.md)——对照样本 #1（探词科技）

### 8.6 仓库贡献者（写新卡）

1. 本卡第 IX 节（扩展原则）
2. [`CONTRIBUTING.md`](../CONTRIBUTING.md)（卡片格式约定）
3. [`templates/`](../templates/)（卡片模板）
4. 检查新卡是否落在已有三轴（D0 / D1-D8 / DS）

## 九、未来扩展原则（避免维度漂移）

新卡片应通过以下检查：

| 检查项 | 描述 |
|--------|------|
| **轴归属** | 落在 D0 / D1-D8 / DS 三轴之一？如不在，独立性 + 价值需要论证（可能是新轴） |
| **维度归属** | 在轴内落在已有维度？如开新维度，需说明与其他维度的正交性 |
| **避免重复** | 与已有 16 张卡的关系是"展开 / 衍生"还是"重复"？后者不应建卡 |
| **元假说密度** | 每张技术卡应包含 ≥ 4 条元假说，否则可能是"事实层卡片"应单列类型 |
| **怀疑锚点** | 顶部 ≥ 3 条怀疑锚点（含 C-SEO Bench 这一仓库通用锚点） |
| **服务商话术对照** | "与 GEO 服务商话术的对照"段必须有，明确判定 |
| **不做的事** | 明确禁区，避免功能蔓延 |
| **衍生 BACKLOG** | 末段必须有 3-5 条衍生待办，让卡片成为"源头"而非"终点" |

**不应建新卡的情况**：

- 已有卡的某段可以扩写，应该在原卡里更新而不是新建
- 主题与现有卡 ≥ 70% 重叠
- 主题是单平台细节（应放 [`platforms/<slug>/`](../platforms/) 而非 [`techniques/`](.)）
- 主题是单实验设计（应放 [`experiments/`](../experiments/) 而非 [`techniques/`](.)）
- 主题是单服务商话术拆解（应放 [`case-studies/`](../case-studies/) 而非 [`techniques/`](.)）

## 十、不做的事

- **不重复 16 张卡的具体内容**——本卡只做组织 / 索引 / 元数据
- **不在本卡引入新的元假说**——元假说全部在原卡内
- **不评判轴 / 维度的优先级**——三轴互相补充，无主次（但因果上 D0 前置 / DS 后置）
- **不预先设计第 17 张卡**——按 BACKLOG 节奏自然推进
- **不重复 case-studies / docs 内容**——本卡是技术维度索引，case-studies 是话术拆解，docs 是会议 / 转录

## 十一、变更记录

- 2026-05-02：初版。14 张卡 × 8 维度图谱显式化 + 卡间关系图 + 强假说集 + 服务商话术索引 + 主体决策索引 + 空缺维度 + 读卡建议路径 + 扩展原则。
- **2026-05-03：三轴升级**。16 张卡 × **D0（需求侧）+ D1-D8（信号侧）+ DS（供给侧）** 三轴结构。新增 D0 [`geo-demand-side-fitness-cn`](./geo-demand-side-fitness-cn.md) + DS [`geo-business-model-taxonomy-cn`](./geo-business-model-taxonomy-cn.md) 两张卡，元假说总数 68 → 79。强假说集 4.1 新增 5 条 ⭐⭐⭐ 反话术（D0 三条 + DS 两条），4.2 新增 2 条 ⭐⭐ 反直觉结论。第 V 节话术索引新增 ≥ 8 条（含正向认可 1 条）。第 VI 节主体决策路径全部加 D0 前置 + 新增"GEO 服务商 / 创业者"路径。第 VII 节空缺维度标记 2 项已填补 + 新增 3 项 DS 子空缺。第 VIII 节新增 8.5 GEO 服务商读卡路径。第 IX 节扩展原则升级为"三轴归属"检查 + 新增 case-studies 类型禁区。
- **2026-05-03（二次更新）**：DS 维度新增子卡 [`anti-geo-monitoring-cn`](./anti-geo-monitoring-cn.md)。DS 维度从"1 张主卡"升级为"1 主卡 + 1 子卡"，卡片总数 16 → **17**，元假说总数 79 → **86**（+7）。强假说集 4.1 新增 2 条 ⭐⭐⭐ 反话术（来自 anti-geo 元假说 A、C）。第 VII 节"DS 子空缺：反 GEO 监测专题"标记 ✅ 已填补。
- **2026-05-04**：审计修订标注。基于 [`audits/2026-05-04_meta-hypothesis-audit.md`](../audits/2026-05-04_meta-hypothesis-audit.md) + 7 反转事实（迈富时 02556.HK / PureblueAI / 智推时代 / 百分点 / 央企招标 / 行业自律 / 平台变现非凤巢式），86 条元假说判决 ✓28 / ◐17 / ✗9 / ?32。强假说集 4.1 标注 2 条 🔄 已降级（D0-C 与 DS-主-A）。识别出 4 个隐含前提中 2 证伪（"草莽期"+"创业 SaaS 为主"）+ 1 部分证伪（"广告位是最大单一风险"）+ 1 部分证伪（"客户付费弱仅窄场景"）。被强化的 4 个判断（反 GEO 监测 / 标准协议层 / YMYL 监管驱动 / ROI 框架）是审计后剩下最坚固的部分。
- **2026-05-04（DS 升级）**：[`geo-business-model-taxonomy-cn`](./geo-business-model-taxonomy-cn.md) 七层 → 八层升级，新增 h 层"横向扩展"（上市营销云加 GEO 模块 + 数据 / 政务公司加 GEO 模块 + 平台内部人创业 + 上市投资）。h 层不独立成新元假说——判断分散落入元假说 B / F 修订段。本元卡同步更新 II 节卡表 + 引用关系图 + 8.5 节 GEO 服务商读卡路径。
