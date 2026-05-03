---
title: DeepSeek 平台概况
type: technique
sources:
  - url: https://news.qq.com/rain/a/20260421A04I2F00
    fetched_at: 2026-05-01
    note: QuestMobile 2026Q1 报告月活与人均使用次数
  - url: https://www.donews.com/news/detail/1/6521095.html
    fetched_at: 2026-05-01
    note: QuestMobile 2026Q1 报告（DoNews 转载）
  - url: https://www.instagram.com/p/DXmK8-MmsSO/
    fetched_at: 2026-05-01
    note: 2026-03-30 DeepSeek 7 小时服务中断报道（用户规模反向佐证）
  - url: https://blog.csdn.net/yunFAA667/article/details/159512346
    fetched_at: 2026-05-01
    note: 第三方 GEO 分析（CSDN），DeepSeek 引用源偏好；服务商口径，需独立验证
confidence: medium
verified: false
last_verified: null
platforms:
  - deepseek
techniques:
  - llm-citation
  - citation-attribution
maturity: in-validation
aliases:
  - DeepSeek
  - 深度求索
related:
  - ./citation-mechanism.md
  - ../doubao/overview.md
  - ../../techniques/princeton-9-strategies-cn.md
  - ../../glossary/terms.md
last_updated: 2026-05-01
---

# DeepSeek 平台概况

> ⚠️ **状态说明**：基于 QuestMobile 一手数据 + 第三方 GEO 服务商二手分析整理，**未实测**。

## 基本信息

| 字段 | 值 |
|------|----|
| 产品方 | 杭州深度求索人工智能基础技术研究有限公司（DeepSeek） |
| 底层模型 | DeepSeek-V 系列 / DeepSeek-R 系列（推理） |
| 关键时间点 | 2025-01 R1 模型开源、2026-03 V4 发布 |
| 主要入口 | iOS / Android APP、Web（chat.deepseek.com）、API（platform.deepseek.com）、众多第三方 APP / 工具集成 |
| 模型授权 | **开源**（MIT License，主要权重） |
| 商业化路径 | API 计费 + 企业部署 + 第三方应用集成 |

## 规模与用户画像（2026Q1，QuestMobile）

| 指标 | 数值 | 来源 |
|------|------|------|
| 月活（MAU） | **1.27 亿** | QuestMobile，截至 2026-03 |
| 月人均使用次数 | **41.7 次/月** | QuestMobile，2026Q1（**仅次于豆包的 54.8**） |
| 平均活跃率（DAU/MAU） | 21% | QuestMobile，2026Q1 |
| 行业排名 | **第三**（豆包 → 千问 → DeepSeek） | QuestMobile，2026Q1 |

**用户粘性**：人均次数 41.7 vs 千问 19.8——**比月活第二的千问高一倍**，说明 DeepSeek 用户是"重度使用者"，与"被春节红包拉新的浅度用户"画像不同。

**关键事件**：

- **2025-01-20**：R1 模型开源，全球轰动；中文 AI 应用增长曲线被它显著抬高
- **春节红包大战（2026-01）**：豆包、千问、元宝靠红包拉新，DeepSeek 几乎没参与，但用户增长仍持续
- **2026-03-30**：服务中断 7 小时（路透 / Instagram 报道），数百万用户受影响——印证用户基数规模
- **2026-03**：V4 发布

## 战略定位（与豆包对照）

| 维度 | 豆包 | DeepSeek |
|------|------|----------|
| **公司类型** | 大厂（字节，内容 / 流量帝国） | 创业公司（量化基金背景，无 To C 历史） |
| **模型授权** | 闭源 | **开源**（核心差异） |
| **内容生态** | 头条 / 抖音 / 抖音百科 / 西瓜（自有闭环） | **无自有内容生态** |
| **用户结构** | 银发 + 下沉，娱乐 / 决策为主 | 偏技术 / 知识型，使用粘性高 |
| **拉新方式** | 红包 + 字节系投放 | 模型能力出圈（R1 开源震动） |
| **第三方 API 集成** | 火山引擎，相对封闭 | 大量第三方 APP 接入（元宝接入、问小白、纳米AI、众多 IDE 集成） |
| **场景定位** | 生活 / 娱乐 / 消费决策 | 研究 / 编程 / 推理 / 写作 |

> **结构性最大差异**：DeepSeek **没有自己的内容平台**，所以它的"信源偏好"必然来自外部公开内容生态——这恰好是研究"非生态绑定的纯模型偏好"的最佳样本。

## 入口与可见性结构

### 用户主要触达 DeepSeek 的方式

1. **官方 APP / Web**（chat.deepseek.com）
2. **DeepSeek API** —— 大量第三方应用通过 API 接入：
   - 腾讯元宝（部分场景接入 R1）
   - 问小白、纳米AI 搜索、知乎直答
   - 各类 IDE（Cursor、Cline、各类 coding agent）
3. **本地部署 / 开源** —— 由于权重开源，企业 / 个人可自部署

### 关键观察：APP 用户 vs API 调用方的分离

DeepSeek 的"模型行为"会通过两条非常不同的路径触达用户：

- **路径 A**：用户在 chat.deepseek.com 或 DeepSeek APP 直接对话（QuestMobile 的 1.27 亿就是这部分）
- **路径 B**：用户在第三方应用里使用，背后是 DeepSeek API（QuestMobile 不计入）

这两条路径下：

- **联网搜索 / 引用机制不同**——官方 APP 有自己的检索增强配置；第三方应用各自接 RAG，引用源结构完全由集成方决定
- **可见性研究的边界**：研究"DeepSeek 自己引用什么"应锁定路径 A；研究"通过 DeepSeek 模型的应用引用什么"则需要逐个研究集成方

这与豆包的 **APP/API 信源差异**是同类问题，但 DeepSeek 因开源 + 第三方集成度极高，问题更复杂（详见 [`citation-mechanism.md`](./citation-mechanism.md)）。

## 官方资源索引

| 资源 | 链接 | 用途 |
|------|------|------|
| DeepSeek 官网 | https://www.deepseek.com | 产品入口 |
| DeepSeek Chat | https://chat.deepseek.com | Web 端对话 |
| API 平台 | https://platform.deepseek.com | 开发者文档、计费 |
| GitHub 主页 | https://github.com/deepseek-ai | 开源模型权重、技术报告 |

> 待补：DeepSeek 是否有公开的"信源筛选 / 联网搜索"政策——目前**未见专项文档**，与字节豆包同样是黑箱。

## 在仓库内的位置

DeepSeek 是仓库**第二个深度调研的 GEO 平台**，理由：

1. 月活第三，但人均使用次数极高（41.7 次/月，国内仅次于豆包），用户密度大
2. **结构性对照豆包的最佳样本**：
   - 豆包 = 大厂 + 自有生态 + 闭源 → 测"生态偏好"信号
   - DeepSeek = 创业公司 + 无生态 + 开源 → 测"纯模型偏好"信号
3. 开源 + 第三方集成生态成熟，对"GEO 监测应该锁定哪个层级"是关键问题

## 未解问题（待实测验证）

不在本卡片下结论，仅列出：

1. **DeepSeek 官方 APP 是否使用联网搜索 + RAG，还是更多依赖训练时的内部知识？**
   - 与 ChatGPT / 豆包不同，DeepSeek 早期宣传偏向"模型推理能力"而非"实时检索"
   - 2026 年的最新行为待确认
2. **官方 APP 的引用源结构**
   - 第三方分析声称偏好 CSDN、搜狐号、网易号、百科站点（详见 [`citation-mechanism.md`](./citation-mechanism.md)）
   - 未独立验证
3. **不同接入方（元宝接 R1、问小白、知乎直答）的 RAG 配置差异**
   - 这决定了"GEO 优化能否跨接入方迁移"
4. **开源权重被自部署后的引用机制**
   - 自部署没有联网搜索能力时，引用完全来自训练数据——这是 GEO 的"长期记忆"层
   - 联网检索增强后则与官方在线服务类似

## 计划中的实验

候选实验（待排期）：

- `deepseek-citation-source-distribution`：在 DeepSeek 官方 APP 跑 N 类 query × M 次重复
- `deepseek-vs-doubao-paired-queries`：**配对实验**——同 query 同时刻在豆包和 DeepSeek 双端跑，对比信源结构差异
- `deepseek-via-third-party-divergence`：同 query 在官方 APP 和 3 个接入方（元宝 / 问小白 / 纳米 AI）跑，量化集成方的影响
- `deepseek-csdn-bias-test`：验证 GEO 服务商声称的"DeepSeek 偏好 CSDN"——用对照内容（同主题 CSDN vs 知乎 vs 微信公众号）

## 与豆包卡片的实验配对

豆包和 DeepSeek 形成天然的**对照实验对**：

- 豆包卡片有的实验，DeepSeek 应该跑配对版
- 这样能区分"中文 LLM 通用行为"vs"豆包字节生态加成"
- 一旦实验数据出来，可在 [`techniques/princeton-9-strategies-cn.md`](../../techniques/princeton-9-strategies-cn.md) 的元假说 B（生态内信源 > 生态外权威信源）下回写结论

## 变更记录

- 2026-05-01：初版，基于二手报道整理，标 `verified: false`
