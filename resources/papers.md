# 学术论文索引

按"对中文场景的可借鉴度"和"反 GEO 营销话术的硬度"挑选，不追求全。本文是**带注释的研究底稿**（每篇含作者 / 年份 / 核心结论 / 中文场景借鉴度判断）。

> **与姊妹库的分工（避免两边各改各的漂移）**：面向公众的论文速览表见 [awesome-geo-cn 学术论文区](https://github.com/LLM-X-Factorer/awesome-geo-cn#学术论文)（持续收录、表格速查、对外用）；本文只收"值得逐篇精读 + 反话术有用"的精选并加注释——两边重叠的奠基论文，**注释深度以本文为准，全量覆盖以 awesome-geo-cn 为准**。完整英文列表见 [DavidHuji/Awesome-GEO](https://github.com/DavidHuji/Awesome-GEO) 和 [amplifying-ai 的 papers-and-studies](https://github.com/amplifying-ai/awesome-generative-engine-optimization/tree/main/papers-and-studies)。

---

## 一、奠基论文

### GEO: Generative Engine Optimization
- **作者 / 单位**：Pranjal Aggarwal et al., Princeton / Georgia Tech / Allen Institute for AI
- **链接**：https://arxiv.org/abs/2311.09735（[ACM 版](https://dl.acm.org/doi/10.1145/3637528.3671900)）
- **年份**：2023-11（持续更新到 KDD 2024）
- **核心结论**：
  - 提出 GEO 这一术语并系统化
  - 测试 9 个核心优化策略（cite sources、quotation addition、statistics addition、authoritative tone、easy-to-understand、fluency optimization、unique words、technical terms、keyword stuffing）
  - 在某些设置下声称 40% 可见性提升
- **本仓库的用法**：
  - 作为 `techniques/` 卡片的**起点假说**——这 9 条在中文平台（豆包 / 千问 / DeepSeek）上是否仍然成立？
  - **不当作事实**——见下面的 C-SEO Bench
- **可信度评级**：medium。论文方法学严谨，但 benchmark 是英文场景；样本量与统计显著性的细节需读完整 PDF 复核

---

## 二、反向证据 / 怀疑锚点（重要！）

### C-SEO Bench: Does Conversational SEO Work?
- **链接**：https://openreview.net/forum?id=oTeixD3oZO
- **会议 / 年份**：NeurIPS 2025
- **核心结论**：
  - 在严格控制（多任务、多领域、多竞争密度）下，**多数 GEO 方法基本无效**
  - 传统 SEO 方法在很多场景下仍然有效
  - 当多个竞争方都使用 GEO 时，效果互相抵消
- **本仓库的用法**：
  - **常驻怀疑锚点**——任何"做了 X 就涨了 N 倍"的 GEO 服务商话术，都先用这篇论文 cross-check
  - 可在 `glossary/terms.md` 或 GEO 卡片里直接引用作为反证据
- **可信度评级**：high。NeurIPS 同行评审 + 大规模 benchmark + 对抗性场景

---

## 三、自动化 / Agent 方向

### AutoGEO: What Generative Search Engines Like and How to Optimize Web Content Cooperatively
- **链接**：https://openreview.net/forum?id=K8EinVWtUB（[GitHub 实现](https://github.com/cxcscmu/AutoGEO)）
- **会议 / 年份**：ICLR 2026
- **核心结论**：
  - 自动学习生成式引擎对内容的偏好
  - 用 GRPO（Group Relative Policy Optimization）训练 rewriting 策略
  - 提出"协作式"内容优化框架
- **本仓库的用法**：
  - 如果未来要做"针对豆包 / 千问的内容自动优化器"，这是技术起点
  - 论文的偏好学习方法学可借鉴到中文模型上做对照实验

### MAGEO: From Experience to Skill: Multi-Agent Generative Engine Optimization via Reusable Strategy Learning
- **链接**：https://github.com/Wu-beining/MAGEO
- **会议 / 年份**：ACL 2026
- **核心结论**：
  - Multi-agent 协作学习 GEO 策略
  - 把"经验"沉淀为"可复用的技能"

---

## 四、领域特化基准

### E-GEO: A Testbed for Generative Engine Optimization in E-Commerce
- **链接**：https://arxiv.org/abs/2511.20867
- **核心结论**：
  - 7000+ 电商 query benchmark
  - 评测 15 种 rewriting heuristics
  - 第一个电商场景的 GEO 基准
- **本仓库的用法**：
  - 中文电商场景（淘宝 / 京东 / 拼多多被 AI 引用、品牌方在豆包 / 千问上的电商可见性）的对照基线
  - 方法学可参考但不能直接复用——中文 query 分布、平台、用户意图都不同

---

## 五、AI 搜索 / 引用机制基础研究

### When Search Meets LLMs: Interactions and Performance
- **链接**：https://arxiv.org/abs/2407.00128
- **类型**：综述
- **本仓库的用法**：理解 RAG、检索增强、Search4LLM / LLM4Search 架构的入门

### Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks
- **链接**：https://arxiv.org/abs/2005.11401
- **作者**：Lewis et al., Meta AI
- **本仓库的用法**：RAG 原始论文。理解 GEO 为什么"内容结构化、可被检索"是有效信号的根本

### Is ChatGPT Good at Search?
- **链接**：https://arxiv.org/abs/2304.09542
- **本仓库的用法**：对话式 AI 搜索质量的早期评估

---

## 六、知识冲突 / 引用准确性

### ConflictBank: A Benchmark for Evaluating the Influence of Knowledge Conflicts in LLM
- **链接**：https://arxiv.org/abs/2408.12076
- **核心**：7.4M claim-evidence 对，研究 LLM 在外部内容与训练数据冲突时如何抉择
- **本仓库的用法**：理解为什么 GEO 的"权威信源"信号有时会被 LLM 自身知识覆盖

### ConflictingQA
- **链接**：https://arxiv.org/abs/2402.11782
- **核心**：LLM 在选择信息时，**偏好"相关性"而非"学术语调"**
- **本仓库的用法**：反驳"学术语调能提升被引用率"这类话术

---

## 七、对抗性 / 安全研究

### GASLITE: SEO Attacks on Dense Retrieval
- **链接**：https://arxiv.org/abs/2412.20953
- **核心**：0.0001% 语料污染就能劫持 top-10 检索结果
- **本仓库的用法**：黑帽 GEO 的可行性证据，提醒**不要把"自然有效"和"被攻击劫持"混为一谈**

### Adversarial SEO for LLMs
- **链接**：https://arxiv.org/abs/2406.18382
- **核心**：隐藏文本能让 AI 答案中的品牌提及提升 2.5×
- **本仓库的用法**：识别黑帽手段；反 GEO 服务商话术（"提升提及率 N 倍"是否来自这种手段？）

### Ranking Manipulation for Conversational Search
- **链接**：https://arxiv.org/abs/2406.03589
- **核心**：通过 prompt injection 操纵对话式搜索排名

### Persistent Pre-Training Poisoning of LLMs
- **链接**：https://arxiv.org/abs/2410.13722
- **核心**：长期预训练污染攻击

### Dynamics of Adversarial Attacks on LLM-Based Search
- **链接**：https://arxiv.org/pdf/2501.00745
- **核心**：black-hat 与 white-hat GEO 的博弈论建模

---

## 八、产业 / 数据分析

### Generative Engine Optimization: How to Dominate AI Search
- **链接**：https://arxiv.org/abs/2509.08919
- **年份**：2025
- **核心结论**：AI 搜索引擎**系统性偏向 earned media（第三方报道、行业媒体）而非 brand-owned content（品牌自有内容）**
- **本仓库的用法**：
  - 解释为什么 GEO 服务商常推"发央媒、发行业媒体"——背后有论文证据
  - 但这不等于"发了就有效"——还要看 C-SEO Bench 的反向证据

---

## 选论文时的过滤条件

加入本列表的论文必须满足至少一项：

- 提供**反 GEO 营销话术**的硬证据（如 C-SEO Bench）
- 提供**机制层面**的解释（如 ConflictingQA、GASLITE）
- 提供**可复现的 benchmark 或数据集**（如 E-GEO）
- 提供**可借鉴到中文场景**的方法学（如 AutoGEO、Princeton GEO）

不加入：

- 纯 marketing-driven 的"行业研究报告"——放到 [`awesome-lists.md`](./awesome-lists.md) 的"行业报告"区
- 仅列举案例无可复现实验的论文
- 重复结论且方法学不更优的后续工作

---

## 维护

- 新论文走 PR，PR 描述里说明它属于上面 1-8 哪个类别
- 论文链接 + 一句话核心 + 本仓库的用法（不超过 3 句）
- 论文被后续工作推翻时，标注 `superseded by`，但**保留原条目**作为研究脉络的一部分
