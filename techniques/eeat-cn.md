---
title: 中文场景的 E-E-A-T 类比信号（跨平台横向对照）
type: technique
sources:
  - url: https://static.googleusercontent.com/media/guidelines.raterhub.com/zh-CN//searchqualityevaluatorguidelines.pdf
    fetched_at: 2026-05-02
    note: Google Search Quality Evaluator Guidelines 中文版，E-E-A-T 原始定义出处
  - url: https://developers.google.com/search/docs/fundamentals/creating-helpful-content
    fetched_at: 2026-05-02
    note: Google "Creating helpful, reliable, people-first content" 文档，含 E-E-A-T 应用指引
  - url: https://ziyuan.baidu.com/college/index
    fetched_at: 2026-05-02
    note: 百度搜索资源平台站长学院，含百度搜索算法规范、落地页规范等官方文档（百度对"权威性"信号的等价表述出处）
  - url: https://openreview.net/forum?id=oTeixD3oZO
    fetched_at: 2026-05-02
    note: C-SEO Bench (NeurIPS 2025)，"权威性策略"在严格控制下效应远低于宣称值的反向证据
confidence: medium
verified: false
last_verified: null
platforms:
  - baidu
  - shenma
  - sogou
  - weixin-sousou
  - doubao
  - deepseek
  - wenxin
  - qianwen
  - yuanbao
  - kimi
techniques:
  - eeat-cn
  - llm-citation
  - icp-and-subject
  - citation-attribution
maturity: concept
related:
  - ../techniques/princeton-9-strategies-cn.md
  - ../techniques/llms-txt-cn-practice.md
  - ../platforms/baidu/seo-signals-and-ai-overview.md
  - ../platforms/wenxin/citation-mechanism.md
  - ../platforms/doubao/citation-mechanism.md
  - ../platforms/deepseek/citation-mechanism.md
  - ../glossary/terms.md
last_updated: 2026-05-02
---

# 中文场景的 E-E-A-T 类比信号（跨平台横向对照）

> ⚠️ **状态：concept**（跨平台对照卡，部分维度有官方文档支撑，部分为待验证假说）
>
> 本卡片**不是 E-E-A-T 教程**，也不复述 Google 原始定义的细节。它做两件事：
>
> 1. **澄清两个常见误解**——"E-E-A-T 是 Google 排名信号" + "中文场景有原生 E-E-A-T 框架"
> 2. 跨平台横向对照——把 E-E-A-T 4 维度映射到中文 4 大搜索引擎 + 6 大生成式引擎，找出**真正能在中文场景操作的等价信号**与**中文场景独有但英文圈不存在的硬信号**
>
> ⚠️ **怀疑锚点 1**：Google 自己反复声明 **"E-E-A-T 不是直接排名信号"**——它是搜索质量评估员手册（SQE Guidelines）里给人类评估员看的概念框架，用来训练评估员、再反过来调整算法目标。E-E-A-T → 算法信号是**间接映射**，不是 1:1 的开关。
>
> ⚠️ **怀疑锚点 2**：百度 / 神马 / 360 / 搜狗**从未原生采用 "E-E-A-T" 框架**。它们各自有"搜索算法规范"等等价文档，但维度划分、术语、权重逻辑都不同。"中文 E-E-A-T"在英文圈和服务商口径里是**术语借用**——把 Google 的 4 维度套到中文场景做类比，不是中文搜索引擎自身的框架。
>
> ⚠️ **怀疑锚点 3**：[C-SEO Bench](https://openreview.net/forum?id=oTeixD3oZO) 在英文场景发现"提升权威性信号"在严格控制下边际效应远低于服务商宣称——中文场景大概率同样如此。本卡片不是"如何提升 E-E-A-T"操作手册。

## 一、E-E-A-T 是什么、不是什么

| 维度 | 含义 | 2022 年加入 |
|------|------|------------|
| **E**xperience | 内容创作者**亲历经验**（用过、去过、做过） | ✅ 2022-12 新加 |
| **E**xpertise | 专业知识 / 资质 | 既有 |
| **A**uthoritativeness | 权威性（行业认可、被引述） | 既有 |
| **T**rustworthiness | 可信度（核心维度，其他三项的"输出"） | 既有 |

**它不是什么**：

- ❌ 不是 Google 排名算法的直接输入信号
- ❌ 不是可以"打分"的指标（不存在 "E-E-A-T 分数"）
- ❌ 不是适用于所有 query 的统一标准——YMYL 类被显著加权，娱乐 / 创意类几乎无影响
- ❌ 不是可以通过"代发权威媒体""购买权威外链"快速提升的工具

**它实际是什么**：

- ✅ 一组给人类**搜索质量评估员**看的概念维度
- ✅ 评估员的判断聚合后**反向影响**算法目标设计
- ✅ 一个**结果导向**的视角——"这内容看起来权威 / 可信吗"，而不是技术信号清单

## 二、为什么"中文 E-E-A-T"是术语借用

中文搜索引擎和生成式引擎**从未公开采用** E-E-A-T 框架。各自的等价表述：

| 平台 | 类似表述 / 框架 | 公开文档来源 |
|------|----------------|--------------|
| 百度搜索 | "权威性 / 专业性 / 可信度"散见于《百度搜索算法规范》《百度落地页体验白皮书》《YMYL 类目的资质要求》等多份文档 | [百度搜索资源平台站长学院](https://ziyuan.baidu.com/college/index)（公开） |
| 神马搜索 | 资讯算法 / 站点资质审核（医疗 / 金融等行业准入） | 部分文档公开 |
| 360 搜索 | 内容生态规范 + 主体认证 | 文档分散，缺权威整合 |
| 搜狗搜索（被腾讯整合后） | 微信搜一搜复用微信公众号原创 / 认证体系；搜狗品牌弱化 | 微信公众号平台规则 |
| 微信搜一搜 | 公众号原创标识、认证主体、视频号实名 + 腾讯系账号体系 | 微信公众平台 |
| 字节系（豆包 / 抖音搜索） | 头条号 / 抖音号原创、蓝 V / 黄 V 认证 | 字节系账号规则 |
| 阿里系（千问 / 夸克） | 商家资质、品牌认证、阿里妈妈站点信用 | 阿里巴巴商家规则 |

**关键观察**：上述每家都有**等价但不同名**的"权威性 / 可信度"信号体系。"中文 E-E-A-T"作为**英文圈研究者的方便术语借用**可以使用，但要意识到这是**外部套用**，不是中文平台自身的框架。

## 三、Google E-E-A-T → 中文搜索引擎信号映射（速查表）

> **本表是横向汇总**。各平台的细节在对应 platform 卡片里，本卡片不重复。

| Google E-E-A-T 维度 | 百度对应 | 神马对应 | 微信搜一搜对应 |
|---------------------|---------|---------|----------------|
| Experience（亲历经验） | 弱信号；个人体验类内容偏向小红书 / 知乎，传统搜索弱 | 弱 | 公众号原创标记 + UGC（部分） |
| Expertise（专业知识） | 资质审核（百度健康 / 医典）+ 行业站权重 | 资质审核（医疗 / 金融准入） | 认证主体（行业 / 媒体 / 政府）|
| Authoritativeness（权威） | **强信号**：央媒 / 政府站 / 学术站 / 百度百科收录 + 百家号大 V | 央媒 / 官方机构 / 行业垂直媒体 | 微信原创 + 蓝 V 政府 / 媒体认证 |
| Trustworthiness（可信） | 主体认证 + ICP 备案 + 行业资质 + 历史合规 | 主体认证 + 备案 | 微信主体审核 + 投诉历史 |
| **中文独有补充：主体认证 / ICP 备案** | **硬门槛**（医疗 / 金融 / 教育不备案不能上） | 硬门槛 | 公众号实名主体 |
| **中文独有补充：账号等级 / 蓝 V** | 百家号 V 等级 / 百度知道答主等级 | 资讯号等级 | 公众号阅读量 / 历史合规 / 蓝 V |

**关键差异**（vs Google E-E-A-T）：

- 中文场景把 **Trustworthiness 拆成"算法可信"+"行政合规"两层**——后者通过 ICP 备案 / 主体认证 / 行业资质强制
- **Experience 在传统中文搜索引擎里弱信号**，但在小红书 / 知乎 / 抖音站内搜索是核心
- **"号"体系**（百家号 / 头条号 / 公众号 / 视频号）在中文场景的权重远高于 Google 对个人作者的处理

## 四、Google E-E-A-T → 中文生成式引擎信号映射（推测 + 已知）

> ⚠️ **本表多为推测**——除文心借用百度索引这条有公开支撑外，其他平台未公开"权威性"判定逻辑。引用本表请同时引怀疑锚点。

| 平台 | 训练数据"权威性"代理 | RAG / 实时检索"权威性"代理 | 已知 / 推测 |
|------|--------------------|---------------------------|-------------|
| 豆包 | 字节系生态（头条 / 抖音百科 / 抖音视频转写）+ 全网爬取 | 字节系搜索 + 全网联网 | "权威性" ≈ "字节系内"；详见 [`platforms/doubao/citation-mechanism.md`](../platforms/doubao/citation-mechanism.md) |
| DeepSeek | Common Crawl + 私有数据混合 | 不绑定单一搜索引擎，第三方接入差异大 | 无显著"权威性偏好"，更接近"通用 RAG"；详见 [`platforms/deepseek/citation-mechanism.md`](../platforms/deepseek/citation-mechanism.md) |
| 文心 | 百度索引 + 百度生态（百家号 / 百科 / 知道 / 文库）| 百度搜索 + 百度生态 | "权威性" ≈ "百度生态内"，**唯一与底层搜索 E-E-A-T 类信号高度耦合的中文 LLM**；详见 [`platforms/wenxin/citation-mechanism.md`](../platforms/wenxin/citation-mechanism.md) |
| 千问 | 阿里系（淘宝评论 / 阿里云 / 1688）+ 公开数据 | 夸克搜索 + 淘宝商品库 + 第三方 | "权威性" ≈ "电商资质 + 阿里系"，YMYL 类弱 |
| 元宝 | 微信公众号 36 亿文章 + 多模型路由 | 腾讯系搜索 + 微信生态 + 联网 | "权威性" ≈ "微信公众号原创 + 腾讯系" |
| Kimi | 长文本爬取 + URL 抓取 | 用户粘 URL 触发抓取 | "权威性"信号最弱，几乎完全依赖单次抓取的内容质量 |

**核心观察**：5 大中文 LLM 中，**只有文心明确复用了底层搜索引擎的"权威性"信号体系**（百度系）。其他 4 家**不复用底层搜索的 E-E-A-T 类信号**，而是直接用**自家生态作为权威性代理**——这与 Google 把 E-E-A-T 间接传导到 Gemini 的路径完全不同。

## 五、中文场景独有 / 与英文场景显著差异的信号

英文 E-E-A-T 框架里**不存在或不重要**，但中文场景**结构性影响**可见性的信号：

### 1. ICP 备案 + 主体认证

- **英文场景**：无对应（域名注册即可发布）
- **中文场景**：医疗 / 金融 / 教育 / 内容平台**无备案不能上线**——这是**前置硬门槛**，不是"加分项"
- **影响**：未备案的中文站点对中文搜索引擎几乎不可见；对中文 LLM 影响**未知但大概率显著**（训练数据爬取 + 联网检索都偏向已备案站点）

### 2. "号"主体绑定

- **英文场景**：内容平台个人账号是辅助，不是核心
- **中文场景**：**"号"是内容生产的基本单位**——百家号 / 头条号 / 公众号 / 视频号 / 知乎账号 / 小红书账号
- **影响**：每个生态系的"号"在自家平台搜索 / 推荐 / LLM 引用中享有结构性权重；跨生态发布的同质内容获得不同的可见性

### 3. 央媒 / 政府站结构性优先权

- **英文场景**：BBC / Reuters / .gov 等被信任，但属于"内容质量"维度
- **中文场景**：人民网 / 新华网 / 央视网 / `*.gov.cn` 在百度 / 神马等的特型卡占位、医疗类前置加权、政策类强制引用是**算法 + 监管混合作用**的结果，不只是"内容质量"
- **影响**：YMYL 类 query 上几乎所有中文搜索 + LLM 都加权央媒，但娱乐 / 决策类影响弱

### 4. YMYL 资质审核（医疗 / 金融硬门槛）

- **英文场景**：YMYL 是 SQE Guidelines 概念，影响通过算法间接传导
- **中文场景**：**直接行政准入**——医疗内容必须有医疗机构资质 + 医师资质审核（百度健康 / 微信健康 / 微博健康号）；金融内容受持牌机构限制
- **影响**：YMYL 类内容生产者**不能通过 SEO 技巧绕过资质门槛**；但持有资质的机构享有结构性优势

### 5. 平台账号等级体系

- **英文场景**：弱（Twitter Verified、LinkedIn Premium 等是社交身份，不是搜索 / 生成权重）
- **中文场景**：百家号 V 等级、头条号原创等级、知乎盐值、小红书等级、视频号原创——**直接影响内容分发权重**
- **影响**：在自家生态发布同质内容，账号等级差异导致可见性显著差异

## 六、待验证元假说

### 元假说 A：LLM 端的"权威性" = 训练数据 + 实时检索来源的"权威性"——而不是独立信号

- 表述：中文 LLM 不存在独立的"E-E-A-T 评估器"——它们的"权威性偏好"完全由训练数据分布 + RAG 检索源决定
- 含义：**优化"内容的 E-E-A-T 信号"无法直接影响 LLM 权威性输出**——除非该内容被纳入训练数据或被实时检索召回
- **如何证伪**：找到任一中文 LLM 在生成答案时对**未被检索到、也未在训练数据中**的"权威信号丰富"内容产生偏好

### 元假说 B：中文 LLM 不复用底层搜索引擎的 E-E-A-T 类信号——它们直接用"自家生态"作为权威性代理

- 表述：豆包 ≈ 字节系内权威；千问 ≈ 阿里系内权威；元宝 ≈ 腾讯系内权威；文心**例外**（复用百度搜索的权威性体系）；DeepSeek **退化**（无生态，权威性最弱）
- 含义：**"提升 E-E-A-T"在中文 LLM 上等价于"在多家自家生态发布"**——本质不是内容信号优化，而是渠道铺设
- **关联**：[`techniques/princeton-9-strategies-cn.md`](./princeton-9-strategies-cn.md) 元假说 B（生态内信源 > 生态外权威信源）的强化版
- **决定性证据**：[`experiments/exp-five-vendor-paired-queries.md`](../experiments/exp-five-vendor-paired-queries.md) H1 跑出来后

### 元假说 C：YMYL 是唯一例外——所有中文平台对央媒 / 政府站 / 资质机构的加权高度一致

- 表述：在 YMYL 类 query（医疗 / 金融 / 法律）上，5 大 LLM + 4 大搜索引擎对 `central-media` / `gov-edu` 类信源的引用率显著趋同（差异 < 10pp）
- **驱动力**：合规驱动，不是算法选择——监管要求所有平台在敏感领域优先引用权威源
- **含义**：YMYL 类是"中文 GEO 不需要按平台分流"的唯一例外
- **如何验证**：在 [`exp-five-vendor-paired-queries`](../experiments/exp-five-vendor-paired-queries.md) v2 中加入 YMYL query 子集

### 元假说 D：英文圈"建议提升 E-E-A-T"在中文场景大概率被替换为"在多家自家生态发布"

- 表述：在中文场景应用"提升 E-E-A-T"的英文圈建议，实际可观测的可见性提升路径是"在百家号 + 头条号 + 公众号 + 知乎 + 小红书等多家生态主体上做内容覆盖"
- **含义**：服务商话术"提升 E-E-A-T 信号"在中文场景的**翻译**应是"做生态铺设"——这是渠道工作，不是内容信号工作
- **副作用**：内容跨生态铺设需要主体多平台账号（百家号 + 头条号同时具备需要不同主体审核），是**中小品牌的结构性壁垒**

### 元假说 E：中文场景独有的"号"主体绑定是 E-E-A-T 框架未覆盖的核心信号

- 表述：在中文场景，**作者账号身份**（"号"）的权重 ≥ Google E-E-A-T 4 维度任意一项的权重
- **含义**：英文场景"高 E-E-A-T 内容 + 弱作者"可以通过站点 SEO 取得可见性；中文场景"高质量内容 + 无认证号"几乎不可见
- **如何验证**：受控发布同质内容到（认证号 vs 未认证号 vs 个人主页），观察可见性差异

## 七、实验设计建议

### 实验 1：央媒 vs 同生态 vs 第三方信源在 5 平台引用率对照（核心实验）

- **目标**：验证元假说 B（自家生态优先权威性）
- **设计**：
  - 自变量：信源类型（`central-media` / 平台自家生态 / 第三方权威媒体）
  - 因变量：在 5 平台引用率
  - 控制：query 内容、query 类型、时段
- **复用**：[`exp-five-vendor-paired-queries`](../experiments/exp-five-vendor-paired-queries.md) 数据可直接析出"central-media"维度对照
- **优先级**：⭐⭐⭐ 高

### 实验 2：YMYL 子集独立看央媒占比（验证元假说 C）

- **目标**：验证 YMYL 类是否真是"按平台分流"的例外
- **设计**：YMYL query 集（10 个，覆盖医疗 / 金融 / 法律）× 5 平台 × 5 重复 = 250 次采集
- **风险**：YMYL 类合规风险，需要严格遵循 [`experiments/methodology.md`](../experiments/methodology.md) 第 YMYL 段约束
- **优先级**：⭐⭐ 中

### 实验 3：主体认证 vs 无认证内容的引用率对照（验证元假说 E）

- **目标**：量化"号"主体绑定对中文场景可见性的实际效应
- **设计**：A/B 对照——同主题、同长度、同发布时间，A 组发认证号、B 组发未认证号 / 个人主页
- **难点**：需要真实账号资源（多平台 + 多主体），工程开销大
- **优先级**：⭐⭐ 中

### 不建议做的实验

- **逐条"验证 E-E-A-T 4 维度对中文 LLM 的影响"**：4 维度本身不是中文场景的原生维度，按 4 维度切片做实验是把英文框架硬套——不如按"信源类型 + 主体类型"切片
- **"提升 E-E-A-T 后跟踪可见性变化"**：E-E-A-T 不是直接信号，"提升 E-E-A-T"无明确操作定义，实验设计不严谨

## 八、与 GEO 服务商话术的对照

国内部分 SEO/GEO 服务商话术：

- "提升 E-E-A-T 信号是中文 SEO 的核心"
- "百度的 E-E-A-T 中文版是排名第一信号"
- "我们提供 E-E-A-T 优化服务，可大幅提升 AI 引用率"

**本卡片判定**：

| 话术 | 判定 | 理由 |
|------|------|------|
| "E-E-A-T 是排名信号" | ⚠️ 误导 | E-E-A-T 在 Google 都不是直接排名信号（间接传导）；中文搜索引擎更没有原生 E-E-A-T |
| "百度 E-E-A-T 中文版" | ⚠️ 术语借用 | 百度有"权威性 / 可信度"等价信号，但不叫 E-E-A-T，维度划分也不同 |
| "提升 E-E-A-T 大幅提升 AI 引用率" | ❌ 无中文场景实证 | 元假说 A 暗示中文 LLM 没有独立 E-E-A-T 评估器；元假说 D 暗示真正起效的是渠道铺设而不是信号优化 |
| "做央媒 / 政府站发稿" | ⚠️ 部分有效 | 仅 YMYL 类成立（元假说 C）；其他类目下被自家生态信号显著压制（元假说 B） |
| "做百家号 + 头条号 + 公众号矩阵" | ✅ 与元假说 D 一致 | 这是渠道工作，比"提升 E-E-A-T"的描述更准确 |

## 九、与本仓库其他卡片的关系

- 与 [`platforms/baidu/seo-signals-and-ai-overview.md`](../platforms/baidu/seo-signals-and-ai-overview.md) 第二节"E-E-A-T 中文版"：本卡片**不重复**百度细节，做横向对照；百度卡片是单平台深度，本卡是跨平台广度
- 与 [`platforms/wenxin/citation-mechanism.md`](../platforms/wenxin/citation-mechanism.md)：文心是"复用底层搜索 E-E-A-T"的唯一中文 LLM 例外
- 与 [`techniques/princeton-9-strategies-cn.md`](./princeton-9-strategies-cn.md)：Princeton 元假说 A（信源 > 风格）和元假说 B（生态内 > 生态外）→ 本卡片元假说 B 是其在 E-E-A-T 框架视角下的重述
- 与 [`techniques/llms-txt-cn-practice.md`](./llms-txt-cn-practice.md)：互补——llms.txt 是"爬虫指令"维度，E-E-A-T 是"内容信号"维度
- 与 [`experiments/exp-five-vendor-paired-queries.md`](../experiments/exp-five-vendor-paired-queries.md)：该实验数据可析出 `central-media` 占比对照，作为元假说 B/C 的核心数据点
- 与 [`glossary/terms.md`](../glossary/terms.md)：`eeat` 通用 slug；`eeat-cn` 中文语境专用

## 十、不做的事

- **不做"如何提升 E-E-A-T"操作手册**——本仓库不收录服务商话术
- **不复述 Google SQE Guidelines 细节**——读官方 PDF 更准
- **不预先断言中文 LLM 的具体偏好**——5 个元假说全部待实证
- **不针对单平台深度展开**——平台细节在 platform 卡片
- **不进入"E-E-A-T vs Helpful Content"等英文圈内部讨论**——和中文场景关系弱

## 十一、待解决的未知 / 公开数据空白

1. 5 大中文 LLM 在训练数据筛选时**是否使用过"权威性"打分**（OpenAI / Anthropic 已知有质量打分管道，中文厂商未公开）
2. 中文 LLM 的 RAG 实时检索时**是否对召回结果做"权威性 reranking"**（vs 仅用相关度 + 时效）
3. 元假说 C 的"YMYL 类全平台趋同"在数据上是否真的成立——还是各平台仍按自家生态分流，只是央媒占比都偏高
4. 主体认证 / 备案对中文 LLM 训练数据爬取的具体筛选规则
5. 跨生态发布的同质内容在不同账号等级上的可见性差异量级（实验 3 的核心问题）

## 十二、衍生 BACKLOG 建议

- 新增 `tech-cn-account-grade-systems`：中文场景"号"主体绑定和账号等级体系的横向对照卡（百家号 V / 头条号 / 公众号 / 知乎 / 小红书）
- 新增 `tech-icp-and-subject` 专题卡：ICP 备案 + 主体认证对中文搜索 + LLM 可见性的影响（已在 BACKLOG，可标记关联本卡片）
- 元假说 B/C 数据回写：[`exp-five-vendor-paired-queries`](../experiments/exp-five-vendor-paired-queries.md) 跑完后回写本卡片
- 实验 2 单立：`exp-cn-ymyl-cross-platform-citation`（YMYL 类跨平台引用对照）

## 变更记录

- 2026-05-02：初版。澄清 E-E-A-T 的两个常见误解 + 跨平台横向对照 + 5 条元假说 + 3 个实验设计建议。confidence: medium，maturity: concept，等待 exp-five-vendor-paired-queries 数据回写。
