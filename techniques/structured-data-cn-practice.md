---
title: 结构化数据（Schema.org / JSON-LD）在中文场景的采纳现状
type: technique
sources:
  - url: https://schema.org/
    fetched_at: 2026-05-02
    note: Schema.org 官方站，由 Google / Microsoft / Yahoo / Yandex 2011 年联合推出，开放词汇标准
  - url: https://developers.google.com/search/docs/appearance/structured-data
    fetched_at: 2026-05-02
    note: Google Search Central 结构化数据文档（西方对照基线，含支持的 schema 类型清单）
  - url: https://ziyuan.baidu.com/college/index
    fetched_at: 2026-05-02
    note: 百度搜索资源平台站长学院（百度对结构化数据的官方说明入口）
  - url: https://ziyuan.baidu.com/wiki
    fetched_at: 2026-05-02
    note: 百度站长 Wiki（含部分百度自有结构化数据 / 标签规范）
  - url: https://openreview.net/forum?id=oTeixD3oZO
    fetched_at: 2026-05-02
    note: C-SEO Bench (NeurIPS 2025)，作为"结构化数据 → LLM 引用率"因果链待严格验证的怀疑锚点
confidence: low
verified: false
last_verified: null
platforms:
  - baidu
  - shenma
  - sogou
  - 360-search
  - bing-cn
  - weixin-sousou
  - doubao
  - deepseek
  - wenxin
  - qianwen
  - yuanbao
  - kimi
techniques:
  - structured-data
  - llm-citation
  - featured-result
  - knowledge-graph
maturity: concept
related:
  - ./eeat-cn.md
  - ./llms-txt-cn-practice.md
  - ./princeton-9-strategies-cn.md
  - ../platforms/baidu/seo-signals-and-ai-overview.md
  - ../glossary/terms.md
last_updated: 2026-05-02
---

# 结构化数据（Schema.org / JSON-LD）在中文场景的采纳现状

> ⚠️ **状态：concept**（公开数据空白卡片——中文搜索引擎对 Schema.org 的支持文档有限，中文 LLM 是否解析 JSON-LD **完全无公开信息**）
>
> 这张卡和前 5 张技术主题卡的取向不同：前面几张讲的是"中文场景独有信号"（E-E-A-T 类比 / "号" / ICP / llms.txt / Princeton 9）；本卡讲的是**英文圈成熟的 Web 标准（Schema.org）在中文场景的实际采纳与脱节**。
>
> 本卡做三件事：
>
> 1. 把 Schema.org / JSON-LD / 微数据 / 百度自有结构化数据**理清四组关系**——它们不是同义词
> 2. 横向对照 4 大中文搜索引擎 + 6 大中文 LLM 对结构化数据的**已知 vs 未知**矩阵
> 3. 拆"做 schema 提升 AI 引用率"这种服务商话术——分清是西方场景外推还是中文场景实证
>
> ⚠️ **怀疑锚点 1**：Schema.org 在 **Google 场景**的效用主要体现在"特型卡 / Rich Results / Knowledge Panel"——这是**SERP 视觉位**层面的效果。它和"LLM 引用率"是**两个不同的因变量**——前者是搜索结果页元素，后者是生成答案中的命中。把 Google 场景下"做 schema → 拿 Rich Results"的经验直接外推到"做 schema → 中文 LLM 引用率提升"是**无支撑的跨变量、跨场景外推**。
>
> ⚠️ **怀疑锚点 2**：百度的"结构化数据支持"**远不如 Google 完整**——百度公开支持的 Schema 类型有限，且与百度自有的"结构化数据规范"（小卡 / 知道 / 百科主体）混用，二者关系**官方未给统一文档**。
>
> ⚠️ **怀疑锚点 3**：[C-SEO Bench](https://openreview.net/forum?id=oTeixD3oZO) 在英文场景对各类"内容信号优化"的反向证据同样适用此处——结构化数据在 LLM 输出层面的边际效应**大概率小于服务商话术宣称值**。

## 一、四组关系：Schema.org / JSON-LD / 微数据 / 百度自有结构化数据

### 1.1 Schema.org（词汇 / 本体）

- **是什么**：一组**开放共享的词汇表**（vocabulary / ontology），定义"Article""Product""Person""Recipe"等约 800 个类型 + 数千属性
- **谁维护**：Google / Microsoft / Yahoo / Yandex 2011 年联合推出，至今 schema.org 站点仍由这些主体共同维护
- **法律地位**：**不是 W3C 标准**，是事实标准——主流英文搜索引擎都采用
- **在中文场景**：**词汇本体被认可**（百度等也用 schema.org 词汇），但具体类型支持范围远窄

### 1.2 JSON-LD / 微数据 / RDFa（标记格式）

| 格式 | 性质 | 现状 |
|------|------|------|
| **JSON-LD** | `<script type="application/ld+json">` 注入 JSON 块 | Google 推荐；现代实践主流 |
| **Microdata** | HTML 标签内嵌 `itemscope itemtype` 属性 | 老式做法；维护成本高 |
| **RDFa** | XML 命名空间 + HTML 属性 | 学术 / 政府站常见，搜索引擎少用 |

**关键事实**：JSON-LD 是格式，schema.org 是词汇——两者正交。可以用 JSON-LD 写 schema.org 词汇（最常见），也可以用 Microdata / RDFa 写。

### 1.3 百度自有结构化数据规范

百度长期与开放标准平行维护**自家结构化数据规范**：

- **百度结构化数据小卡**：早期对垂类内容（新闻 / 资讯 / 招聘 / 视频 / 小说）有专项标记规范，部分类型与 schema.org 词汇不直接对应
- **MIP（移动网页加速器）**：曾对标 Google AMP，2020-2022 后逐渐淡出，本卡不展开
- **百家号 / 百度百科 / 百度知道的内部数据结构**：不是开放的"标记规范"，而是百度生态内部数据 schema——内容方通过提交而非标注接入

**与 schema.org 的关系**：

- 百度部分 schema.org 类型支持（Article / Product / Recipe 等）但**类型范围 + 属性深度都比 Google 浅**
- 百度自有规范在某些垂类（如招聘）反而更细，但**只在百度生态内通用**

### 1.4 与 llms.txt 的对照

| 维度 | 结构化数据（Schema.org / JSON-LD） | llms.txt |
|------|------------------------------|----------|
| 标记位置 | 页面内 `<script>` 或 HTML 属性 | 站点根目录 `/llms.txt` 单文件 |
| 受众 | 搜索引擎 + 部分 LLM | LLM（理论上） |
| 颗粒度 | 单页面 / 单实体 | 站点级摘要 |
| 标准化程度 | Schema.org 是事实标准（10+ 年） | 提议中（2024-09 起） |
| 中文场景采纳 | 部分（百度有限支持） | 几乎为空（详见 [`llms-txt-cn-practice.md`](./llms-txt-cn-practice.md)） |

详细差异在 [`llms-txt-cn-practice.md`](./llms-txt-cn-practice.md)，本卡不重复。

## 二、中文搜索引擎对结构化数据的支持矩阵

> ⚠️ **本表为公开文档 + 行业观察整合**——百度 / 神马公开文档相对有限，多数条目需以"已知 / 推测"标注。

| 平台 | Schema.org 词汇支持 | JSON-LD 解析 | 自有规范 | 触发特型卡的强度 |
|------|--------------------|--------------|----------|-----------------|
| **百度搜索** | 部分支持（Article / Product / Recipe 等核心类型） | 解析（不如 Google 完整） | 自有结构化数据小卡（垂类专项） | **中**——结构化数据对小卡触发有帮助但不必要 |
| **神马搜索** | 极有限文档 | 解析行为未公开 | 阿里电商生态内部 schema（淘宝 / 天猫 / 1688 商品库） | 弱（公开层面） |
| **360 搜索** | 文档稀少 | 解析行为未公开 | 自有"特型"机制，与 schema.org 关系不公开 | 弱 |
| **搜狗 / 微信搜一搜** | 微信生态以公众号原创 + 视频号实名为主 | 公众号文章页**不支持**自定义 `<script>` JSON-LD（编辑器层限制） | 微信生态内部 schema | **结构化数据通路在内容平台层级被阻断** |
| **必应中文** | 与全球必应一致，支持 Schema.org 主要类型 | 完整解析 | 无自有 | 与全球必应一致 |

**关键观察 1**：百度的"结构化数据支持"是**部分支持 + 自有规范并行**，与 Google 的"完整支持 schema.org"不是同一个层级。

**关键观察 2**：中文内容平台（微信 / 抖音 / 小红书 / B 站）**绝大多数不允许内容方在文章页注入自定义 `<script>` JSON-LD**——这意味着即使内容生产者想做 Schema 标记，**生产平台层面就被阻断了**。这是中文场景与英文独立站场景的核心结构差异。

**关键观察 3**：Schema.org 在中文场景的"做了未必有用"很大程度来自**生产平台不允许做** + **搜索引擎不完整支持**两端夹击。

## 三、中文 LLM 是否解析 JSON-LD：已知 vs 未知矩阵

> ⚠️ **本节几乎全部为推测**——5 大中文 LLM 厂商**均未公开**训练数据预处理 / RAG 召回时是否解析 JSON-LD。

| LLM | 训练数据预处理是否解析 JSON-LD | RAG 召回是否使用 schema 提升相关度 | 已知 / 推测 |
|-----|------------------------------|-----------------------------------|-------------|
| 豆包 | 未公开 | 未公开 | 字节系生态内（头条 / 抖音）有自家数据 schema，外站爬取大概率裸 HTML |
| DeepSeek | 未公开 | 不绑定单一搜索引擎 | 通用 RAG 大概率不专门解析 schema |
| 文心 | 未公开 | 未公开 | 共用百度索引时**有可能**继承百度对 schema 的部分理解 |
| 千问 | 未公开 | 未公开 | 电商类商品库有自家 schema；非电商类通用 |
| 元宝 | 未公开 | 未公开 | 微信生态内不允许内容方注入 schema，外站通用爬取 |
| Kimi | 未公开 | URL 抓取触发 | 长文本场景，对 schema 元数据感知最弱 |

**关键观察**：5 大中文 LLM 中**没有任何一家公开声明解析 JSON-LD**。这与英文场景下 GPT-4 / Gemini 也未公开同类信息一致——但 Google 的 RAG（AI Overviews / SGE）公认大量复用其搜索索引中的 schema 提取结果。中文 LLM 中可能复用搜索索引 schema 提取的**只有文心一种可能**。

## 四、Google → 中文场景外推的失效之处

服务商话术常引用"Google 场景下做 schema 拿 Rich Results 的成功案例"——但这种外推存在**至少 4 处失效**：

| 失效点 | 描述 |
|--------|------|
| **跨平台失效** | Google 完整支持 schema.org 数千属性；百度只部分支持；神马 / 360 / 搜狗 / 微信搜一搜公开支持极有限 |
| **跨变量失效** | Google 场景下"schema → Rich Results"是 SERP 视觉位；"schema → 中文 LLM 引用率"是生成答案命中——这是两个不同因变量 |
| **跨生产平台失效** | Google 场景的内容多来自独立站；中文场景的内容大量来自微信 / 抖音 / 小红书等内容平台，**这些平台禁止内容方注入 JSON-LD** |
| **跨监管失效** | YMYL 类内容 schema 标注不能替代行政资质（详见 [`icp-and-subject-cn.md`](./icp-and-subject-cn.md)）——医疗 schema 标得再精细，无医疗资质内容仍然不会被加权 |

**结论**：Google 场景下 schema 经验在中文场景的可移植性**结构性受限**。

## 五、待验证元假说

### 元假说 A：Schema.org 在中文搜索引擎下的边际效应远小于在 Google

- 表述：相同内容在百度部署完整 schema.org 标注后的特型卡触发率提升 < 在 Google 部署后的 Rich Results 提升
- **驱动力**：百度对 schema.org 类型范围 + 属性深度支持有限
- **如何验证**：跨场景 A/B——同主题内容分别在 google.com 和 baidu.com 索引下，对照"无 schema vs 完整 schema"的特型卡触发率变化

### 元假说 B：Schema.org 标注对中文 LLM 引用率的边际效应**接近 0**

- 表述：在内容站完整部署 JSON-LD schema.org 后，5 大中文 LLM 引用率与未部署时差异 < 5pp（弱效应阈值）
- **含义**：服务商话术"做 schema 提升 AI 引用率"在中文场景大概率无效
- **如何验证**：套用 [`exp-doubao-vs-deepseek-paired`](../experiments/exp-doubao-vs-deepseek-paired.md) 工具栈，A/B 部署对照
- **关联**：[`llms-txt-cn-practice.md`](./llms-txt-cn-practice.md) 元假说 A（中文 LLM 都不尊重 llms.txt）的姊妹假说

### 元假说 C：文心是唯一可能从 schema 标注中获益的中文 LLM

- 表述：在所有部署 schema.org 标注的中文站点中，**只有文心**的引用率有可观测提升；其他 4 家中文 LLM 几乎不受影响
- **驱动力**：文心共用百度索引 → 百度对 schema 的部分支持 → 文心继承
- **如何验证**：5 平台对照实验中析出文心子集
- **关联**：[`eeat-cn.md`](./eeat-cn.md) 元假说 B（文心是唯一复用底层搜索 E-E-A-T 信号的中文 LLM）的同一现象

### 元假说 D：百度自有结构化数据规范（垂类小卡）在百度场景的效应 > 通用 schema.org

- 表述：在百度生态内，部署百度自家垂类规范（招聘 / 资讯 / 视频小卡）的可见性效应 > 通用 schema.org
- **含义**：在中文场景做结构化数据的最佳策略**不是"做 schema.org 通用类型"**，而是"做对应垂类的百度自家规范"——这是基于平台分化的现实选择
- **副作用**：百度自家规范不通用——做完百度的，神马 / 360 还得另做（如有相应规范）

### 元假说 E：内容平台（微信 / 抖音 / 小红书）的"内部 schema"对应平台 LLM 引用是关键路径

- 表述：内容平台内部数据结构（微信公众号原创 + 视频号实名 + 抖音号原创等）对应**字节系 → 豆包 / 腾讯系 → 元宝**的引用率影响**远大于** schema.org JSON-LD
- **含义**：在中文场景关心 schema 的 GEO 视角应转向"在内容平台内部规范化做内容"而不是"在独立站打 JSON-LD"
- **关联**：[`account-grade-systems-cn.md`](./account-grade-systems-cn.md) 元假说 B（生态内传导）的 schema 侧重述

## 六、实验设计建议

### 实验 1：A/B 部署 schema.org 对中文 LLM 引用率的影响（核心实验）

- **目标**：验证元假说 B（schema 对中文 LLM 边际效应接近 0）+ 元假说 C（仅文心受益）
- **设计**：
  - 自变量：2 档（无 JSON-LD vs 完整 JSON-LD schema.org 标注）
  - 因变量：5 大中文 LLM 引用率
  - 控制：内容主题、长度、发布时间、域名权重
- **样本**：每档 ≥ 20 篇内容 × 30 天 = 1200 数据点
- **难点**：需要可控制的独立中文站点
- **优先级**：⭐⭐⭐ 最高
- **复用**：套用 [`exp-doubao-vs-deepseek-paired`](../experiments/exp-doubao-vs-deepseek-paired.md) 工具栈

### 实验 2：百度自有规范 vs 通用 schema.org 效应对照（验证元假说 D）

- **目标**：在百度场景下，自家规范是否真的优于通用 schema.org
- **设计**：3 档（无标注 vs 通用 schema.org vs 百度垂类规范），观察百度搜索特型卡触发率 + 文心引用率
- **优先级**：⭐⭐ 中（适合做百度场景的内容方参考）

### 实验 3：内容平台内部规范对生态 LLM 的影响（验证元假说 E）

- **目标**：在内容平台内做"原创认证 + 完整字段"vs"裸内容"对应平台 LLM 引用率
- **设计**：A 组发标准化字段完整的内容到（公众号原创 / 头条号原创 / 抖音号原创）；B 组发字段不完整的内容
- **优先级**：⭐⭐ 中

### 不建议做的实验

- **"加 FAQPage schema 是否提升 AI Overview"**：这是 Google 场景的命题，中文场景"AI Overview"不存在直接对应物（百度 AI 答案位机制不公开）
- **"做 BreadcrumbList schema 是否影响 LLM"**：Breadcrumb 主要影响 SERP 显示形态，与 LLM 引用率因果链最远
- **多 schema 类型同时变化的"完整结构化包"实验**：变量太多无法归因

## 七、与 GEO 服务商话术的对照

国内常见话术：

- "做完 schema.org 标注，AI 引用率翻倍"
- "JSON-LD 是 AI 时代 SEO 的硬通货"
- "FAQPage / HowTo schema 必拿 AI Overview 位"
- "结构化数据让 LLM '看懂'你的内容"

**本卡片判定**：

| 话术 | 判定 | 理由 |
|------|------|------|
| "schema → AI 引用率翻倍" | ❌ 无中文场景实证 | 元假说 B；服务商引用的 Google 场景案例不可外推 |
| "JSON-LD 是 AI 时代 SEO 硬通货" | ⚠️ 仅 Google 部分成立 | 中文搜索引擎支持有限；中文 LLM 解析未公开 |
| "FAQPage / HowTo 必拿 AI Overview 位" | ❌ 类别错误 | "AI Overview"是 Google 概念，中文等价物（百度 AI 答案位）机制不公开 |
| "schema 让 LLM 看懂内容" | ⚠️ 误用比喻 | LLM 不"看"标注，它读 token 序列；schema 只是元数据，未必进入 token 流 |
| "做百度结构化数据小卡" | ✅ 部分有效 | 元假说 D 支持，但仅在百度场景，且受垂类支持范围限制 |

**结论**：服务商话术里**与 Google 场景外推**的部分大概率失效；**与中文平台自家规范结合**的部分相对靠谱。

## 八、与本仓库其他卡片的关系

- 与 [`llms-txt-cn-practice.md`](./llms-txt-cn-practice.md)：互补——本卡是"页面内元数据"维度，llms.txt 是"站点级元数据"维度。两者的中文采纳现状高度相似（Google 场景成熟 vs 中文场景空白）
- 与 [`eeat-cn.md`](./eeat-cn.md) 元假说 B：文心是唯一可能从 schema 受益的中文 LLM——本卡元假说 C 与之同源
- 与 [`account-grade-systems-cn.md`](./account-grade-systems-cn.md) 元假说 B：本卡元假说 E 是其在 schema 视角的重述
- 与 [`icp-and-subject-cn.md`](./icp-and-subject-cn.md)：YMYL 类 schema 不能替代资质——这是 schema 在中文场景的硬限制
- 与 [`platforms/baidu/seo-signals-and-ai-overview.md`](../platforms/baidu/seo-signals-and-ai-overview.md) 第一节"结构化数据 / 主体优化"：本卡补全跨平台对照，百度卡片不重复展开
- 与 [`princeton-9-strategies-cn.md`](./princeton-9-strategies-cn.md)：Princeton 9 策略中**没有**专门的"结构化数据"策略——这本身是个值得记录的事实，说明 schema 在 LLM 引用率维度上的相对地位

## 九、不做的事

- **不做"如何写 JSON-LD"操作教程**——schema.org 官方文档 + Google Search Central 已经写得足够好
- **不复述 Schema.org 词汇细节**——读 schema.org/docs/full.html 更准
- **不预先断言中文 LLM 是否解析 schema**——5 家厂商都没公开
- **不为单个 schema 类型给"权重系数"**——平台不公开，服务商给的数字都是猜
- **不进入"JSON-LD vs Microdata 哪个更好"的格式之争**——和中文场景关系弱

## 十、待解决的未知 / 公开数据空白

1. 百度对 schema.org 类型 + 属性的**完整支持清单**（官方未给统一文档，行业整理也零散）
2. 神马 / 360 / 搜狗对 schema.org 的解析行为（**完全空白**）
3. 5 大中文 LLM 在训练数据预处理时**是否解析 JSON-LD**（**完全空白**）
4. 中文 LLM 的 RAG 召回是否对 schema 标注页做相关度提升（**完全空白**）
5. 内容平台（微信 / 抖音 / 小红书）内部 schema 对生态内 LLM 的传导路径具体强度
6. 百度自有垂类规范在 2026 年的实际维护状态（部分文档可能已过期）

## 十一、衍生 BACKLOG 建议

- `exp-cn-schema-vs-no-schema-llm`：实验 1（schema A/B 对中文 LLM 引用率影响）的独立条目
- `exp-cn-baidu-native-vs-schema-org`：实验 2（百度自有规范 vs 通用 schema.org）的独立条目
- 新增 `tech-cn-search-engine-schema-support-matrix`：跨搜索引擎 schema 支持类型清单（事实层卡片，定期更新）
- 与 `tech-knowledge-graph-cn`（[`BACKLOG.md`](../BACKLOG.md)）协调：百科 / 知识图谱与 schema 标注是知识表示的两条路径，可对照展开
- 平台 changelog 系列建立时（`platform-baidu-changelog` 等），同步追踪结构化数据规范的版本变更

## 变更记录

- 2026-05-02：初版。Schema.org / JSON-LD / 微数据 / 百度自有规范四组关系拆解 + 4 大搜索引擎 + 6 大 LLM 支持矩阵 + 5 条元假说 + 3 个实验设计建议 + Google 场景外推的 4 处失效。confidence: low，maturity: concept，等待实验 1 数据回写。
