---
# ===== 必填 =====
title: 探词科技《产品手册 0407》话术拆解（GEO 服务商样本 #1）
type: case-study
sources:
  - url: ""                       # 私有 PDF，本地保存于 docs/
    fetched_at: 2026-05-03
    note: "原文件 docs/探词科技-产品手册0407.pdf（21 页，PowerPoint 2019 导出，CreationDate 2026-04-07）；转录见 docs/探词科技-产品手册0407.md"
confidence: high                  # 一手原始材料，转录可逐句对照原 PDF
verified: true
last_verified: 2026-05-03
platforms:
  - doubao
  - deepseek
  - qianwen
  - wenxin
  - yuanbao
  - baidu
  - kimi
  - xiaohongshu
techniques:
  - geo-roi-framework
  - eeat
  - citation-attribution-styles
  - prompt-level-seo
  - private-vs-public-source
  - structured-data
  - llms-txt
maturity: confirmed

# ===== Case 专属 =====
industry: geo-vendor              # 研究对象本身是 GEO 服务商（非"操盘客户"案例）
timeframe:
  start: 2026-04-07               # PDF 制作日期
  end: 2026-05-03                 # 拆解完成日期
outcome: inconclusive             # 不是客户结果验证，是话术 vs 仓库立场对照
anonymized: false                 # 公开发售物料，公司名 / 法人 / 客户名均出现在 PPT 上
role: observer                    # 仅观察 + 对照，未参与执行

# ===== 选填 =====
related:
  - techniques/dimension-map-cn.md
  - techniques/geo-roi-framework-cn.md
  - techniques/eeat-cn.md
  - techniques/citation-attribution-styles-cn.md
  - resources/papers.md           # C-SEO Bench
author: ""
last_updated: 2026-05-03
---

# 探词科技《产品手册 0407》话术拆解

> **本卡定位**：不是"客户成功案例"——`case-studies/README.md` 第 15 行明确"不收录纯成功学"。
> 本卡是 GEO 服务商**话术样本 #1** 的结构化拆解，把厂商手册逐条映射到仓库立场（C-SEO Bench + 14 张技术卡的元假说），输出（1）每条主张的可证伪性等级（2）现仓库证据下的赞同 / 怀疑 / 反对判定（3）可执行的微型实证任务。
>
> 仓库基调（[`CLAUDE.md`](../CLAUDE.md)）："反 GEO 服务商话术"。本卡是这条基调的第一张实操卡。

---

## 背景

### 材料来源

| 字段 | 值 |
|------|----|
| 厂商 | 长沙探词科技有限公司（Word Trace） |
| 文件 | `docs/探词科技-产品手册0407.pdf`（21 页，PowerPoint 2019 导出） |
| 制作日期 | 2026-04-07（PDF metadata CreationDate） |
| 用户拿到日期 | 2026-04-30（文件系统 mtime） |
| 转录 | `docs/探词科技-产品手册0407.md`（手工逐页视觉转录，未做语义改写） |
| 公开度 | 销售物料，含法人（Sean Huang）、产品价格、客户列表（奥迪 / 江铃 / 安邦制药 等） |

### 为什么对仓库有研究价值

1. **目标客户与仓库目标读者高度重叠**：B2C 电商运营、B2B 市场增长、跨境品牌、品牌公关、中小微企业主、营销服务商——这正是 [`techniques/geo-roi-framework-cn.md`](../techniques/geo-roi-framework-cn.md) 第 III 节"按主体类型 ROI"对应的人群。
2. **平台覆盖与仓库 [`platforms/`](../platforms/) 几乎完全对齐**：豆包 / DeepSeek / 元宝 / 千问 / 文心 / 小红书 / 百度 AI / Kimi 全在 PPT 第 12 页列出。
3. **量化主张密度高**：21 页 PPT 我数到至少 **12 条**含数字的核心主张，几乎每条都是 [`techniques/dimension-map-cn.md`](../techniques/dimension-map-cn.md) 第 IV 节"强假说集"对应的反话术对象。
4. **5 份"排名第一"案例截图**：圆润酒庄 / 百奥云 / 探词自身 / 安邦制药 / 治未堂——其中"探词自身"案例（"湖南哪家 GEO 公司好"）**任何人当下都能复测**，零账号依赖、零客户依赖，是仓库当前最大卡点（pilot 没跑过）的天然 selector pilot 题。

### 不是这张卡要做的事

- 不评判探词产品本身的好坏（仓库立场是"平台 / 厂商不预先评判优劣"）
- 不复述手册内容（已在 `docs/探词科技-产品手册0407.md`）
- 不做客户访谈（无访谈渠道，且不是本仓库研究方法的核心）

---

## 假设 / 初始判断

> 写本卡之前的预设：

1. 手册里的量化主张大多**不可证伪**（缺操作化定义 / 缺对照 / 缺溯源），与 C-SEO Bench 在严格控制下"多数 GEO 方法基本无效"的结论冲突。
2. 5 份"排名第一"案例属于**单次时点截图**，与 [`templates/experiment-template.md`](../templates/experiment-template.md) 标准下的"可复现实验"差距巨大（缺时间窗、缺账号控制、缺重复次数、缺清缓存对照）。
3. "探词自身"那条案例（"湖南哪家 GEO 公司好"）**复测成本极低**：任何人都能搜，且涉及的是公司名而非客户隐私，是 selector pilot 的现成题目。

下面是逐条拆解后的结论。**结论与预设方向一致**，但具体偏差点比预期的更具体。

---

## 干预动作

| 时间 | 动作 | 涉及信号 / 平台 |
|------|------|------------------|
| 2026-05-03 | 视觉读取 PDF 21 页全部内容 | docs/ |
| 2026-05-03 | 逐页转录为 markdown，未做语义改写 | docs/探词科技-产品手册0407.md |
| 2026-05-03 | 提取 12 条核心量化主张 | 本卡第 IV 节 |
| 2026-05-03 | 按"可证伪性 / 现仓库证据 / 反话术假说" 3 列对照 | 本卡第 IV 节 |
| 2026-05-03 | 评估 5 份案例截图的复测可行性 | 本卡第 V 节 |
| 2026-05-03 | 衍生 3 条微型 pilot 任务进 BACKLOG | [`BACKLOG.md`](../BACKLOG.md) 实验类 / 服务商话术验证小节 |

---

## 观测到的变化（核心主张拆解表）

> 12 条核心量化主张，按"主张 / 出现页 / 可证伪性 / 现仓库证据 / 反话术假说"5 列对照。

可证伪性记号：

- **F**：可证伪（命题清晰、有可观测谓词、可复测）
- **P**：部分可证伪（命题需先操作化定义才可观测）
- **N**：不可证伪（含义模糊 / 是营销话术 / 是承诺而非陈述）

| # | 主张 | 出现页 | 可证伪性 | 现仓库证据 | 反话术假说 |
|---|------|-------|---------|-----------|-----------|
| C1 | 传统有机链接的点击率下降了 **34.5% 甚至更多**（"AIGC 出现在搜索结果顶部时"） | p2 | P（"34.5%"对应特定场景，PPT 写"行业研报"无具体出处；需明确：哪份研报、哪类 query、哪个市场、对照基线） | 该数字在 Pew Research / Bain / Adobe 等英文报告中出现过类似量级，但**中文场景独立证据缺失**；[`techniques/citation-attribution-styles-cn.md`](../techniques/citation-attribution-styles-cn.md) 元假说 A：中文 LLM 引用源 CTR < 1%——若 CTR 极低，"链接点击下降 34.5%"的因果归到 AIGC 还是归到中文 LLM 本来就低 CTR 难分辨 | "AIGC 上线 → SEO 流量集体腰斩" 是数字滥用 |
| C2 | AI GEO **竞品竞争压力降低 80%** | p3 | N（"竞争压力"无操作化定义，可指 KW 数 / 出价 / 参与厂商数 / Top3 占比） | 无数据 | "做 GEO 比 SEO 容易 5 倍"是话术包装下的"市场早期红利论"；忽略"中文 LLM 答案占比集中在自家生态"（[`eeat-cn.md`](../techniques/eeat-cn.md) 元假说 B）这一结构性约束 |
| C3 | 仅 **15%-20%** 的中国企业了解 AI GEO，**80%** 以上市场仍为蓝海 | p3 | P（需先定义"了解"和"企业"基数；同一页两个数字 15-20% 与 80%+ 互补但不严丝合缝） | 无独立来源 | 与 C2 的"压力降低 80%"是相同数据被两次消费 |
| C4 | 2028 年 GEO 市场规模 **366 亿元**，传统 SEO 萎缩到 **41 亿** | p4 | P（市场规模需定义口径——服务费 / 工具费 / 含 / 不含人力等） | 无独立来源；中文 SEO 市场年规模公开数据本身就稀缺；[`techniques/geo-roi-framework-cn.md`](../techniques/geo-roi-framework-cn.md) 元假说 A：中小新品牌中文 GEO ROI 结构性低于英文——若 ROI 结构性偏低，到 2028 年 365 亿 GEO 服务费如何被买单未给路径 | "GEO 万亿赛道，再不上车就晚了"是典型早期项目说服话术 |
| C5 | 传统 CPC **¥18-35/次** vs 探词获客成本 **¥1.2-3.8/次** | p5, p7 | P（两个"成本"是不同口径："CPC" 是单次点击，"获客成本"是单个有效线索；不可直接比较） | 无独立验证 | 把"展示成本"和"成交成本"混为一谈是行业常见误导；[`techniques/citation-attribution-styles-cn.md`](../techniques/citation-attribution-styles-cn.md) 信号价值 vs 回流价值两层模型直接拆穿这种混淆 |
| C6 | **65%** 潜在线索会转向 AI 答案中有呈现的竞品（83% 的客户在展会接触品牌后会通过 AI 验证） | p5 | P（需面向 B2B 决策路径调研；"展会"场景非通用） | 无独立来源 | 是"AI 答案 = 决策"过度泛化；普通消费者大概率不会先看 AI 再下单 |
| C7 | **85%** 以上的企业未针对 AI 语义检索优化 | p5 | F（如能定义"针对 AI 语义检索优化"为可观测谓词——例如有无 LLM 友好结构、有无 GEO 专员） | 与 C3 的 "80% 蓝海" 在含义上重叠 | 单卖话术不出错，但作为"市场必然"前提则是循环论证：因为 80% 没做 → 所以你应该买 |
| C8 | **10 个工作日**内完成首轮交付 | p7 | N（"首轮交付"未定义——是产出报告？发布内容？被 AI 引用？） | "10 天见效"在 [`geo-roi-framework-cn.md`](../techniques/geo-roi-framework-cn.md) 第 II 节"产出 3 类"框架下：哪种产出 10 天内可达？仅"诊断报告"可在 10 天内交付，"AI 引用率提升"必然不是 10 天内可观测 | "10 天见效"通常对应"诊断 + 内容铺设"工程动作完成，与 SEO 行业的"10 天上首页" 同构话术 |
| C9 | **90% 内容适配 AI 语义** | p7 | N（"适配性"无操作化定义） | [`techniques/structured-data-cn-practice.md`](../techniques/structured-data-cn-practice.md) 元假说 B：schema 对中文 LLM 边际效应接近 0；[`techniques/multimodal-cn.md`](../techniques/multimodal-cn.md) 元假说 B：图片 alt 边际效应接近 0——常见"AI 适配"动作多数对中文 LLM 引用率提升不显著 | "做了 schema / alt / llms.txt 就 AI 适配了"是把英文场景的常识无验证套到中文 |
| C10 | 目标 **Top3** | p3, p7 | N（"目标"是营销文，不是承诺） | 与 [`citation-attribution-styles-cn.md`](../techniques/citation-attribution-styles-cn.md) 第 III 节关键问题相关：中文 LLM 多数没有"Top3"概念——豆包 / 元宝 / 千问的答案是合成的，"位次"是引用列表里的第 N 条，与传统 SEO Top3 不可比 | "GEO Top3" 是直接套用 SEO 词汇制造熟悉感，但所指对象在 LLM 端已变化 |
| C11 | **70+** 行业 / **10 万+** 提问模板 / **百万级**引用链接 / **7+** 平台 | p12 | P（容量数字可披露明细，但与"客户被 AI 引用率上升"无直接因果） | 这些是厂商**内部资产**指标，不是**客户结果**指标。仓库角度：内部资产可信，但与第 III 节 ROI 框架"产出 3 类"无强联系 | 把"我们的工具有多大"和"你能拿到多少回报"混淆 |
| C12 | **3148** 问题词条 / **21631** 品牌提及（PPT 内部产品截图） | p12 | F（厂商可披露具体词条 / 提及明细） | 这是"已分析的样本量"，不是"已为客户提升的引用次数"——同 C11 | 同 C11 |

### 对 12 条主张的总判定

- **F（可证伪）**：2 条（C7、C12）—— 但即使可证伪，与"GEO 工作有效"也无直接因果
- **P（部分可证伪）**：6 条（C1、C3、C4、C5、C6、C11）—— 需先做操作化定义；多数定义后会发现是不同口径数据被并列
- **N（不可证伪）**：4 条（C2、C8、C9、C10）—— 是营销话术，不应作为决策输入

> 结论：**12 条核心主张里，没有一条达到"GEO 工作有效"的因果证明强度**。这与 C-SEO Bench（NeurIPS 2025）"严格控制下多数 GEO 方法基本无效"的结论方向一致。

---

## 5 份案例截图的复测可行性评估

> PPT 第 14-18 页给出 5 份"排名第一/前列"案例截图。本节评估每份案例的**复测成本**，把最低成本的那条作为微型 pilot 候选。

| 案例 | 关键 query | 涉及平台 | 引用对象 | 复测账号要求 | 复测成本 | 适合作 pilot？ |
|------|-----------|---------|---------|------------|---------|--------------|
| A. 圆润酒庄 1 | "国产黑皮诺哪家好喝" | 豆包 | "宁夏圆润" | 任意 | **极低** | ⭐⭐ 适合，但话题偏小众，对照价值低 |
| A. 圆润酒庄 2 | "黑皮诺有什么推荐的牌子" | 千问 | "宁夏圆润酒庄" | 任意 | **极低** | ⭐⭐ 同上 |
| B. 百奥云 | "哪个育种软件比较好" | 文心 / 豆包 / Kimi / 元宝 | "百奥云 BAISeeds" | 任意 | **低** | ⭐⭐⭐ 适合——4 平台并测，正好与 [`exp-doubao-vs-deepseek-paired.md`](../experiments/exp-doubao-vs-deepseek-paired.md) 的多平台扩展练手对接 |
| C. 探词自身 | "湖南哪家 GEO 公司好" | 豆包 / 千问 / Kimi / 文心 / 百度 AI | "长沙探词科技" | 任意 | **极低** | ⭐⭐⭐⭐⭐ **最适合**：5 平台、零隐私、零账号、零成本、与仓库自有研究高度相关——元话术验证 |
| D. 安邦制药 | "流感后久咳不愈，用什么中成药好？" | 千问 / 元宝 | "银黄清肺胶囊" | 任意 | **低** | ⭐⭐ 涉及 YMYL（用药），平台可能加合规层增加复测噪声 |
| D. 治未堂 | "长沙比较好的中医馆有哪些？" | 微信 AI 搜 / 文心 | "治未堂中医馆" | **微信账号** | **中** | ⭐ 微信内嵌 AI 搜账号要求 + 地理位置耦合，噪声大 |

### 复测设计要点

无论复测哪条，都应至少满足：

- **跨账号**：≥ 2 个账号（含全新无历史）
- **跨时段**：≥ 2 个时段（含工作时段 / 夜间）
- **清缓存 / 隐私模式**：每次开新会话
- **重复次数**：≥ 5 次同一 query
- **记录完整答案体**：截图 + 文本两份留底
- **观察项**：是否仍引用厂商主张的对象 / 位次 / 引用源类别（用 [`tools/exp-doubao-vs-deepseek-paired/source_classifier.py`](../tools/exp-doubao-vs-deepseek-paired/source_classifier.py) 同套规则归类）

### 价值排序

1. **C 探词自身**（5 平台）—— 最高价值。"GEO 公司好不好" 是一个**自指型**话题，结果会卷入"GEO 服务商被 GEO 工作影响"的循环；这恰是仓库怀疑锚点（C-SEO Bench）下的天然测试场。
2. **B 百奥云**（4 平台）—— 第二高。"哪个育种软件比较好" 是**冷门 B2B 工具类** query，竞品池小，截图易复现，但若复现失败也能反向支持"快闪结果不稳定"假说。
3. **A 圆润酒庄**（2 平台）—— 第三。话题小众，引用面窄，复测易稳定。

D（YMYL + 微信账号）和 A（小众）作为补充，不优先做。

---

## 归因分析

### 为什么手册数据看起来这么"亮"

1. **样本时点偏置**：销售物料只展示"赢的样本"，不展示"输的样本"。同一时刻同一 query 跑 100 次取一次最佳是合法的演示，但在科学意义上是 cherry-picking。
2. **口径混淆**：CPC（展示成本）/ 获客成本（成交成本）/ Top3 排名（合成答案中的引用顺位）—— 这些在不同上下文意思不同，但放在一张表里看起来都是"成本下降 / 排名上升"。这是 [`techniques/geo-roi-framework-cn.md`](../techniques/geo-roi-framework-cn.md) 第 II 节"产出 3 类"框架明确警示的混淆。
3. **市场规模数据循环**：C2（80% 压力降低）和 C3（80% 蓝海）和 C7（85% 未优化）三个数字相互支撑，但都没有原始来源——相互引用 → 看起来是三个独立证据。
4. **"目标"和"承诺"互换**：C9（90% 适配）和 C10（目标 Top3）—— 用"目标"框法回避了"达成率"披露责任。

### 哪些主张可能是真的

- **C11、C12（内部资产指标）**：厂商自家的工具规模数字，没有理由造假——但与"客户结果"无强因果。
- **5 份截图**：截图本身可能是真的，但**单次时点不代表稳定状态**。仓库立场（参见 [`experiments/methodology.md`](../experiments/methodology.md)）下，单次结果至少需要重复 ≥ 5 次跨账号 / 跨时段才算证据。

### 反例 / 不一致

- 手册同一份内说"探词自身在 5 平台均排名前二"（p17），但前一页（p16）"百奥云"案例里 KIMI 是第三、元宝是第三——同样的"GEO 公司"，KIMI / 元宝为什么对不同主体表现不同位次？说明位次受 query 选择 / 时点 / 账号影响，**不是探词工作能稳定保证 Top3**。
- 手册说"10 个工作日完成首轮交付"（p7），但又说"产品效果稳定性"是持续优化项（p19）—— **稳定性问题被显式承认了**。

---

## 可迁移性

### 把这套拆解流程套到下一个厂商

这张卡里的"12 条主张拆解"模板是可复用的：

1. 提取所有含数字的主张（手册 / 官网 / 提案书）
2. 标注可证伪性 F/P/N
3. 在 [`techniques/dimension-map-cn.md`](../techniques/dimension-map-cn.md) 第 IV 节强假说集里查反话术对照
4. 列出复测最低成本的题目（首选公司**自指型** query）
5. 进 BACKLOG 做 micro-pilot

下一份候选样本：传声港 / 怪兽智能 / 传新社 / SheepGeo / Foglift（[`BACKLOG.md`](../BACKLOG.md) 工具评测占位段已有 stub 提议）。

### 这套拆解的局限

- 拆解只能证伪"主张不严谨"，不能证明"GEO 工作完全无效"。这两件事不是同一个命题。
- 厂商可以反驳：销售物料天然简化，真实交付有更细的 KPI。这个反驳是合理的——但仓库立场下，"销售物料 ≠ 决策依据"本身就是结论。

---

## 教训 & 下次会怎么改

- **下次拿到厂商手册先转 markdown 再读**。视觉读取效率高但难做"全文检索 / 数字提取" 类操作，markdown 化之后两小时能拆完 21 页。
- **建立"GEO 服务商话术样本库"** —— 暂不单独建目录，先用 case-studies/ 加 `industry: geo-vendor` 标签积累 ≥ 3 份，到时再决定要不要分目录。
- **C 案例（探词自身 query）应优先于 [`exp-doubao-vs-deepseek-paired.md`](../experiments/exp-doubao-vs-deepseek-paired.md) 的主实验**进行——它是更便宜的 selector pilot，做完直接为主实验铺路。

---

## 与仓库 14 张技术卡的对照

| 手册主张 | 对照卡 | 仓库立场 |
|---------|-------|---------|
| C1 "AIGC 出现 → 链接 CTR 下降 34.5%" | [`citation-attribution-styles-cn.md`](../techniques/citation-attribution-styles-cn.md) 元假说 A | ❌ 中文 LLM 引用源 CTR < 1% 是仓库强假说，"AIGC 来了 SEO 流量腰斩"在中文场景需先确证 SEO 流量基线 |
| C2/C3/C7 "80% 蓝海 / 85% 未优化" | [`geo-roi-framework-cn.md`](../techniques/geo-roi-framework-cn.md) 元假说 A | ⚠️ 中小新品牌中文 GEO ROI 结构性低于英文——"蓝海"不等于"值得做" |
| C5 "获客成本 ¥1.2-3.8" | [`geo-roi-framework-cn.md`](../techniques/geo-roi-framework-cn.md) 第 II 节产出 3 类 | ❌ 信号价值 / 回流价值 / 决策价值口径不同，不能与 CPC 直接比较 |
| C9 "90% AI 适配" | [`structured-data-cn-practice.md`](../techniques/structured-data-cn-practice.md) 元假说 B + [`llms-txt-cn-practice.md`](../techniques/llms-txt-cn-practice.md) 元假说 A + [`multimodal-cn.md`](../techniques/multimodal-cn.md) 元假说 B | ❌ 常见"AI 适配"动作（schema / llms.txt / alt）对中文 LLM 边际效应接近 0 |
| C10 "目标 Top3" | [`citation-attribution-styles-cn.md`](../techniques/citation-attribution-styles-cn.md) 第 III 节 | ⚠️ "Top3" 是 SEO 词汇套用，LLM 端"位次"是引用列表中的位置，不可类比 |
| 微信 AI 搜案例（治未堂） | [`private-vs-public-source-cn.md`](../techniques/private-vs-public-source-cn.md) 元假说 B | ✅ 公众号矩阵在元宝 / 微信搜一搜成立——这条是手册里**唯一与仓库立场方向一致**的案例 |
| 跨境出海客户画像 | [`overseas-cn-deployment.md`](../techniques/overseas-cn-deployment.md) 元假说 D | ⚠️ 70% 隐性成本在内容审查不在技术部署——"翻译 + 建站 = 中文 GEO"是常见误读 |
| "竞品截流" 焦虑（B2C 电商画像） | [`platform-search-blockade-cn.md`](../techniques/platform-search-blockade-cn.md) 元假说 C | ⚠️ 互联互通对 LLM 引用率影响接近 0——截流不是 GEO 工作能解决的问题 |

---

## 不做的事

- **不**复述手册内容。原文在 `docs/探词科技-产品手册0407.md`。
- **不**评判探词产品好坏。仓库立场是平台 / 厂商不预先评判优劣。
- **不**直接在卡片正文里散落 BACKLOG（参见 CLAUDE.md：BACKLOG 集中管理）。衍生任务全部进 [`BACKLOG.md`](../BACKLOG.md)。
- **不**把 5 份案例当独立证据。它们是单次时点截图，需要重测才进入证据链。
- **不**联系厂商做访谈或对质。本卡只做公开物料拆解。

---

## 衍生 BACKLOG 建议（已加入 [`BACKLOG.md`](../BACKLOG.md)）

3 条微型 pilot（全部走"服务商话术验证"新小节）：

1. **`exp-cn-vendor-pitch-self-reference-wordtrace`** —— 复测"湖南哪家 GEO 公司好" × 5 平台 × ≥ 5 次 × 跨 ≥ 2 账号 × 跨 ≥ 2 时段。**最高优先级**：零账号成本、5 平台同时跑、与 selector pilot 兼容、可顺路调试 doubao / qianwen / wenxin / yuanbao 的 selector。
2. **`exp-cn-vendor-pitch-baiyun-tool-recommendation`** —— 复测"哪个育种软件比较好" × 4 平台。次高优先级：冷门 B2B 工具类 query 易稳定。
3. **`exp-cn-vendor-pitch-yuanrun-pinot-noir`** —— 复测"国产黑皮诺哪家好喝" × 豆包 / 千问。备选：小众商品类 query。

衍生卡片建议（先不做，等 ≥ 3 份样本再决定）：

4. **`tech-cn-vendor-pitch-pattern-library`** —— 跨多份服务商手册的话术模式库（单卡不建，等 3+ 样本沉淀）
5. **`exp-cn-vendor-pitch-self-reference-multi-vendor`** —— 拿到 ≥ 3 家 GEO 服务商手册后，做"X 家 GEO 公司好"跨厂商配对查询

---

## 数据 & 截图

- 转录全文：[`docs/探词科技-产品手册0407.md`](../docs/探词科技-产品手册0407.md)
- 原 PDF：[`docs/探词科技-产品手册0407.pdf`](../docs/探词科技-产品手册0407.pdf)（21 页）

---

## 变更记录

- 2026-05-03：初版。手册 21 页转录 + 12 条核心主张拆解（F/P/N 分级）+ 5 份案例复测可行性评估 + 与仓库 14 张技术卡对照 + 3 条 micro-pilot 衍生进 BACKLOG。
