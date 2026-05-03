---
title: llms.txt 在中文场景的采纳现状
type: technique
sources:
  - url: https://llmstxt.org/
    fetched_at: 2026-05-02
    note: llms.txt 提议官方站，Jeremy Howard / Answer.AI 维护
  - url: https://www.answer.ai/posts/2024-09-03-llmstxt.html
    fetched_at: 2026-05-02
    note: 提议原始博文（2024-09-03），含与 robots.txt / sitemap.xml 的差异说明
  - url: https://platform.openai.com/docs/bots
    fetched_at: 2026-05-02
    note: OpenAI 官方爬虫文档（GPTBot / OAI-SearchBot / ChatGPT-User 三类分离）作为西方对照
  - url: https://darkvisitors.com/
    fetched_at: 2026-05-02
    note: 第三方 LLM 爬虫 UA 跟踪站，含中文厂商记录的对照参考（待实抓验证）
  - url: https://openreview.net/forum?id=oTeixD3oZO
    fetched_at: 2026-05-02
    note: C-SEO Bench (NeurIPS 2025)，作为"即使被抓取，引用率因果链仍待严格验证"的怀疑锚点
confidence: low
verified: false
last_verified: null
platforms:
  - doubao
  - deepseek
  - wenxin
  - qianwen
  - yuanbao
  - kimi
techniques:
  - llm-citation
  - geo-experiment
  - structured-data
maturity: concept
related:
  - ../techniques/princeton-9-strategies-cn.md
  - ../platforms/doubao/citation-mechanism.md
  - ../platforms/deepseek/citation-mechanism.md
  - ../resources/papers.md
last_updated: 2026-05-02
---

# llms.txt 在中文场景的采纳现状

> ⚠️ **状态：concept**（公开数据空白卡片）
>
> llms.txt 是 2024-09 由 Jeremy Howard / Answer.AI 提出的非标准提议，目标是给 LLM 提供一份"网站精华内容索引"。**它至今不是 W3C / IETF 标准**，主流 LLM 厂商既未明确背书也未明确拒绝。
>
> 本卡片不重复英文圈关于 llms.txt 提议本身的讨论（[llmstxt.org](https://llmstxt.org/) 和 Answer.AI 原始博文已经讲清楚），而是聚焦一个**英文资料几乎完全空白**的子问题：
>
> **中文主流 LLM 厂商（豆包 / DeepSeek / 文心 / 千问 / 元宝 / Kimi）的爬虫 UA 是否公开？是否抓取 `/llms.txt`？是否在生成答案时优待部署了 llms.txt 的中文站点？**
>
> ⚠️ **怀疑锚点**：截至 2026-05，没有任何一家中文 LLM 厂商**公开声明**支持 llms.txt。即便部署，因果链"部署 → 被抓 → 被采纳进训练 / RAG → 在生成答案中被引用"中的每一环在中文场景都未被实证。结合 [C-SEO Bench](https://openreview.net/forum?id=oTeixD3oZO) 的发现（多数 GEO 方法在严格控制下基本无效），llms.txt 在中文场景大概率是"低成本部署可做，但不要预期可见性提升"。

## llms.txt 是什么（速览）

| 维度 | llms.txt | robots.txt | sitemap.xml |
|------|----------|-----------|--------------|
| 受众 | LLM（训练 / RAG） | 爬虫（搜索引擎为主） | 搜索引擎 |
| 目的 | 告诉 LLM "**该读什么**" | 告诉爬虫"**能不能爬**" | 告诉搜索引擎"**有哪些 URL**" |
| 内容形态 | Markdown，含精选页面摘要 + 链接 | 简单指令（Allow / Disallow） | 结构化 URL 列表（XML） |
| 标准状态 | 非标准提议（2024-09） | RFC 9309（2022 正式 RFC） | sitemaps.org（2008 起事实标准） |
| 覆盖率 | 极低（早期采纳者多为英文技术站） | 几乎全网 | 主流 SEO 站点 |

两个版本：

- `/llms.txt`：精简索引，约几 KB，给上下文窗口受限的 LLM 用
- `/llms-full.txt`：完整内容拼接，可能数 MB，给上下文窗口大的 LLM 用

提议本身不强制实现，**没有任何"协议警察"**——LLM 厂商是否读取完全自愿。

## 西方 LLM 厂商对爬虫的公开做法（参照系）

注意：**公开爬虫 UA ≠ 支持 llms.txt**。下表只说明"是否能在 robots.txt 里识别该厂商爬虫"，这是 llms.txt 讨论的前置条件——如果连爬虫 UA 都不公开，站长根本无法定向控制其抓取行为。

| 厂商 | 训练爬虫 UA | 实时检索爬虫 UA | 用户触发抓取 UA | 是否官方声明 llms.txt |
|------|------------|----------------|----------------|----------------------|
| OpenAI | `GPTBot` | `OAI-SearchBot` | `ChatGPT-User` | 未声明 |
| Anthropic | `ClaudeBot` / `anthropic-ai` | `Claude-SearchBot`（社群观察） | `Claude-User` | 未声明 |
| Google | `Google-Extended`（训练标记） | Googlebot | — | 未声明 |
| Perplexity | `PerplexityBot` | `Perplexity-User` | — | 社群报告 Perplexity 会读 llms.txt（待严格验证） |
| Common Crawl | `CCBot` | — | — | 不适用 |

**关键观察**：西方主流厂商在 2024-2025 趋势是**爬虫 UA 三类分离**（训练 / 实时检索 / 用户主动触发），方便站长分级控制。

## 中文 LLM 厂商：已知 vs 未知（核心研究空白）

| 厂商 | 训练爬虫 UA 是否公开 | 实时检索爬虫 UA | 是否有公开 llms.txt 立场 | 已知的可观测信号 |
|------|---------------------|----------------|------------------------|----------------|
| 豆包（字节） | 未明确公开 | `Bytespider` 是字节系搜索爬虫历史 UA，但**是否用于豆包训练 / RAG 未公开** | 未声明 | 站长社区有"Bytespider 抓取激进 / 不严格遵守 robots.txt"的报告（待集中归档） |
| DeepSeek | **未公开** | 未公开（DeepSeek 官方未发布爬虫文档） | 未声明 | 训练数据来源仅在论文中提到 Common Crawl + 私有数据混合 |
| 文心（百度） | 未明确分离 | `Baiduspider`（搜索）；用于文心训练的 UA 是否同源未公开 | 未声明 | 百度站长平台对 Baiduspider 有控制接口，但不区分"搜索 vs LLM 训练用途" |
| 千问（阿里） | **未公开** | 未公开 | 未声明 | Qwen 开源版训练数据混合公开数据集；千问 APP 的实时检索路径未披露爬虫信息 |
| 元宝（腾讯） | **未公开** | 未公开（元宝接入腾讯多搜索源 + 微信公众号 36 亿文章库，但抓取 UA 未独立暴露） | 未声明 | 微信生态内的内容是站内库，**不经过外部爬虫**——llms.txt 对微信公众号无适用性 |
| Kimi（月之暗面） | **未公开** | 未公开（Kimi 长文本能力依赖站点抓取，但 UA 未文档化） | 未声明 | Kimi 的 URL 提交功能（用户粘 URL → Kimi 抓取）触发的 UA 待社区抓包确认 |

**强假说（待证伪）**：截至 2026-05，**中文主流 LLM 厂商无一支持 llms.txt**——既无公开声明，也无独立的 LLM 训练爬虫 UA 文档化。

**关键空白**：

1. 中文站长端**没有像 Google Search Console 那样的"LLM 训练抓取报告"工具**
2. 各厂商的训练数据是否包含中文 Common Crawl 切片，间接影响是否"读到了"部署 llms.txt 的中文站
3. RAG 实时检索路径（豆包深度搜索 / 元宝联网 / 千问 AI 搜索）调用的是自家爬虫还是第三方搜索 API（如必应国际 / 神马），未公开

## 中文站点部署 llms.txt 的现状

**截至 2026-05 的观察（待系统普查）**：

- 中文部署 llms.txt 的站点极少，已知样本主要在**面向开发者的英文 / 中英双语技术站**（SaaS、AI 工具、开源文档）
- 纯中文内容站（资讯门户、电商、内容平台）几乎无人部署
- 部分企业官网部署了 `/llms.txt` 但内容是英文版站点结构索引，与中文内容不同步

**部署模式（推测）**：

- 模式 A：精简版索引，列首页 + 主要产品 / 文档 URL + 一句话描述
- 模式 B：完整版（`/llms-full.txt`），把核心文档全文拼接
- 模式 C：双语并存（`/llms.txt` + `/llms-zh.txt`，后者为中文索引，**非提议规范**，是站点自定义扩展）

> 待验证：模式 C 的"自定义扩展"在 LLM 端是否被识别？大概率不被识别——LLM 厂商没有任何理由探测非标准路径。

## 待验证元假说

### 元假说 A：中文 LLM 全部不尊重 llms.txt（强假说，最可能成立）

- 表述：豆包 / DeepSeek / 文心 / 千问 / 元宝 / Kimi 在生成答案时，部署了 llms.txt 的站点 vs 未部署的同质量站点，被引用率**无显著差异**（| diff | < 5pp）
- 含义：如果成立，中文 GEO 文献中"建议部署 llms.txt"的说法是噪音
- **如何证伪**：找到任一中文 LLM 在引用同质量内容时显著优待部署了 llms.txt 的源（≥10pp 差异，且统计显著）

### 元假说 B：抓取行为 vs 引用行为分离

- 表述：即使中文 LLM 厂商的爬虫**抓取**了 `/llms.txt`，也不代表内容**进入**训练 / RAG 通路或在生成答案时被优待
- 含义：站长端能在日志里看到"`/llms.txt` 被某 UA 访问"，但这只是抓取层证据，不是引用层证据
- **实操推论**：抓取日志分析（实验 1）只能给出"是否被读"，不能给出"是否被采纳"——后者只能靠引用率对照实验

### 元假说 C：robots.txt 仍然优先于 llms.txt

- 表述：当 robots.txt 与 llms.txt 冲突时（例如 robots.txt Disallow 了 `/docs/` 但 llms.txt 索引了 `/docs/intro`），LLM 厂商遵守 robots.txt
- 含义：llms.txt 不是"绕过 robots.txt 的快车道"
- **如何证伪**：构造冲突路径，观察是否被某厂商抓取
- **风险**：故意触发"绕过 robots.txt"实验需要站长侧授权，不要在他人站点做

### 元假说 D：间接采纳路径——通过英文 Common Crawl 切片

- 表述：中文站点部署的 llms.txt 即使中文 LLM 不读，也可能通过 **Common Crawl → 英文 LLM 训练 → 英文 LLM 输出 → 中文 LLM 训练数据混入英文 LLM 输出** 的链路间接产生影响
- 含义：影响极弱、不可控、不可观测
- **实操推论**：作为优化策略**不可依赖**，但作为"全球内容生态"参与的一种姿态有意义

## 实验设计建议（按优先级）

### 实验 1：抓取日志被动观察（最低成本，先做）

- **目标**：观察哪些 UA 实际访问 `/llms.txt`
- **设计**：在自己控制的中文站点（≥3 个，覆盖不同行业）部署 `/llms.txt` 和 `/llms-full.txt`，连续记录 30-60 天访问日志
- **采集字段**：UA、IP（粗粒度归属）、Referer、访问频次、是否同时访问 `robots.txt`
- **判定**：
  - 中文 LLM 厂商已知 IP 段（豆包 / DeepSeek 等）若出现 → 抓取存在
  - 仅 GPTBot / ClaudeBot / CCBot 出现 → 西方厂商抓取，中文厂商未触达
- **限制**：抓取 ≠ 采纳进训练 / RAG（见元假说 B）
- **优先级**：⭐⭐⭐ 高（成本几乎为 0）

### 实验 2：受控部署 A/B 对照（核心实验）

- **目标**：测部署 llms.txt 是否提升中文 LLM 引用率
- **设计**：两组同质量、同主题、同发布时间的中文页面，A 组部署 `/llms.txt` 索引该页面，B 组不部署。在豆包 / DeepSeek / 文心 / 千问 / 元宝 / Kimi 上各跑 30+ query，统计被引用率
- **预期**：基于元假说 A，预期 | A - B | < 5pp
- **复用**：直接套用 [`exp-doubao-vs-deepseek-paired`](../experiments/exp-doubao-vs-deepseek-paired.md) 的工具栈，只是把"平台"作为分组、"是否部署"作为自变量
- **样本规模**：参考 [methodology.md](../experiments/methodology.md) 最小样本规则
- **优先级**：⭐⭐ 中（成本中等，需要站点资源）

### 实验 3：独特词指纹植入

- **目标**：检测 llms.txt 内容是否进入了 LLM 上下文
- **设计**：在 `/llms.txt` 中植入若干**生造的、互联网零搜索结果**的"指纹词"（如 `qkz-blueonion-2026`），然后在各中文 LLM 上构造引导 prompt，看模型是否能复现指纹词
- **判定**：
  - 模型复现指纹词 → llms.txt 进入了模型上下文（训练或 RAG）
  - 不复现 → 没有证据进入（不能反证未进入，可能仅未在该 prompt 下被检索到）
- **优先级**：⭐ 低（创意实验，假阴性率高，但能给"是否被读取"提供阳性证据）

### 不建议做的实验

- **故意违反 robots.txt 看 llms.txt 是否被绕过**：法律 / 道德灰色地带，不在调研范畴
- **大规模站点部署后等"自然观察"**：观察期长、噪音大、无对照，无法形成研究结论

## 与 SEO/GEO 服务商话术的对照

国内部分 GEO 服务商建议"部署 llms.txt 是基础动作"。本卡片的判定：

- **"部署本身成本很低"**：✅ 基本属实，几行 Markdown 而已
- **"部署后可见性显著提升"**：⚠️ **无中文场景实证**，违反 C-SEO Bench 的整体发现趋势
- **"中文 LLM 都支持 llms.txt"**：❌ **目前无任何中文 LLM 厂商公开声明支持**

参考 [`techniques/princeton-9-strategies-cn.md`](./princeton-9-strategies-cn.md) 元假说 C：当所有竞争方都部署相同 GEO 信号时，单一信号的边际效应趋近于 0。

## 与本仓库其他卡片的关系

- 与 [`techniques/princeton-9-strategies-cn.md`](./princeton-9-strategies-cn.md) 元假说 A（信源信号 > 表达层信号）：llms.txt 不是"信源"也不是"表达"，是一种**新型抓取指令**——这条卡片填的是该分类之外的盲区
- 与 [`platforms/doubao/citation-mechanism.md`](../platforms/doubao/citation-mechanism.md)、[`platforms/deepseek/citation-mechanism.md`](../platforms/deepseek/citation-mechanism.md) 假说一：豆包 / DeepSeek 的"内部生态优先"假说一旦成立，llms.txt 这种"外部公平协议"在它们身上效应必然更弱
- 与 [`resources/papers.md`](../resources/papers.md) 中的 C-SEO Bench：作为"GEO 提议无效化"的整体怀疑锚点

## 不做的事

- **不复述 llms.txt 提议的英文细节**：去 [llmstxt.org](https://llmstxt.org/) 看原文
- **不为某个 GEO 服务商背书或踩**：本卡片只描述机制和未知，不是消费决策
- **不预先断言"llms.txt 中文场景必然无效"**：元假说 A 是强假说，但要等实证数据
- **不在卡片正文里堆操作步骤**：实操步骤（如何写 llms.txt）属于服务商 / 提议官网的领域，不是调研仓库的职责

## 待解决的未知 / 公开数据空白

1. 各中文 LLM 厂商的训练爬虫 UA 是否存在但未公开（黑盒爬虫）
2. 各厂商的实时检索路径（联网搜索）调用的是自家爬虫还是第三方 API
3. 中文 Common Crawl 在各厂商训练数据中的权重（影响元假说 D 强度）
4. 中文站点部署 llms.txt 的真实样本量（需要爬一份 Tranco / Cloudflare Radar 中文 Top 1k 普查）
5. 微信公众号、知乎、小红书等**封闭内容平台**对 llms.txt 的态度——大概率"完全不适用"，因为这些平台的内容不在自有域名下

## 建议的后续动作（落到 BACKLOG）

- 新增 `tech-cn-llm-crawler-ua-registry`：建立中文 LLM 爬虫 UA / IP 段登记卡片，作为本卡片的事实补充
- 新增 glossary slug `crawler-directive`（涵盖 robots.txt / llms.txt / ai.txt / sitemap.xml 一类爬虫指令）
- 实验 1（抓取日志观察）作为低成本先行实验，转 issue
- 实验 2（A/B 对照）需要站点资源，纳入"高价值实验池"

## 变更记录

- 2026-05-02：初版。6 家中文 LLM 厂商的"已知 vs 未知"矩阵 + 4 条元假说 + 3 个实验设计建议。confidence: low，maturity: concept。等待实验数据回写。
