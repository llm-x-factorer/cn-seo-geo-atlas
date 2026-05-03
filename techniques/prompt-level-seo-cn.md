---
title: Prompt-level SEO 在中文场景的适用性（用户输入侧角度）
type: technique
sources:
  - url: https://arxiv.org/abs/2311.09735
    fetched_at: 2026-05-02
    note: Princeton GEO 原始论文（含 prompt 视角的部分讨论，但以内容侧策略为主）
  - url: https://huggingface.co/Qwen/Qwen2.5-7B/raw/main/tokenizer.json
    fetched_at: 2026-05-02
    note: Qwen 系列 tokenizer 公开（HuggingFace）——中文 token 化的事实参照
  - url: https://huggingface.co/deepseek-ai/DeepSeek-V3/raw/main/tokenizer.json
    fetched_at: 2026-05-02
    note: DeepSeek 系列 tokenizer 公开（HuggingFace）
  - url: https://openreview.net/forum?id=oTeixD3oZO
    fetched_at: 2026-05-02
    note: C-SEO Bench (NeurIPS 2025)，作为"prompt 关键词优化 → LLM 引用率"因果链待严格验证的怀疑锚点
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
  - prompt-level-seo
  - llm-citation
  - long-tail-keyword
maturity: concept
related:
  - ./eeat-cn.md
  - ./princeton-9-strategies-cn.md
  - ./knowledge-graph-cn.md
  - ./structured-data-cn-practice.md
  - ../experiments/query-set-v1.md
  - ../glossary/terms.md
last_updated: 2026-05-02
---

# Prompt-level SEO 在中文场景的适用性

> ⚠️ **状态：concept**（"prompt-level SEO"这个概念在英文圈本身也仅 2024-2025 才热起来，中文场景几乎完全空白）
>
> 本卡和前 7 张技术卡的取向不同：前面都是**内容供给侧**（怎么做内容、怎么挂资质、怎么进入百科）；本卡是**用户输入侧**——用户实际怎么向中文 LLM 发问，以及内容方能不能（以及怎么）针对这个做优化。
>
> 本卡做四件事：
>
> 1. 澄清"prompt-level SEO"概念——内容方**不能控制用户的 prompt**，所以"prompt-level SEO"不是字面的"优化用户的 prompt"，而是"预测用户可能用的多种 prompt 变体，让内容尽可能多地覆盖"
> 2. 横向对照中文 prompt 与英文 prompt 的结构差异（分词 / 长度 / 同义词 / 错别字 / 行业黑话）
> 3. 拆开"内容侧 SEO 思维"和"prompt engineering 思维"——这两者经常被服务商混淆为同一个东西
> 4. 反"prompt 关键词优化提升 AI 引用率"话术
>
> ⚠️ **怀疑锚点 1**：内容方**不能控制用户的 prompt**——能做的只是预测 prompt 多样性。"prompt-level SEO"这个名字本身就有误导嫌疑——它字面像"操控 prompt"，实际是"覆盖 prompt 变体"——后者其实是**长尾关键词思维的 LLM 时代版本**，不是新东西。
>
> ⚠️ **怀疑锚点 2**：中文 LLM 的 tokenizer 中**只有 Qwen / DeepSeek 公开**；豆包 / 文心 / 元宝 / Kimi 均不公开。**query rewrite 行为**（LLM 内部对用户 query 的改写 / 同义词扩展 / 召回 query 生成）**全部不公开**。这意味着"针对 LLM tokenizer 优化关键词"这种话术多数是**对不可观测系统做穴位按摩**。
>
> ⚠️ **怀疑锚点 3**：[C-SEO Bench](https://openreview.net/forum?id=oTeixD3oZO) 在英文场景对各类"内容侧关键词信号优化"的反向证据同样适用此处——"prompt 关键词覆盖优化"在中文 LLM 引用率上的边际效应**大概率显著小于服务商宣称值**。

## 一、概念澄清：什么是 prompt-level SEO，什么不是

### 1.1 字面 vs 实质

**字面**："在 prompt 层面优化"——听起来像内容方能直接干预用户输入。

**实质**：内容方**不能控制**用户怎么问；能做的只是：

- **预测**用户可能用的 prompt 变体（关键词 / 句式 / 同义词 / 拼写错误 / 行业黑话）
- **设计**内容让多种 prompt 变体都能命中

这是**长尾关键词挖掘**在 LLM 场景下的延续——不是新东西。

### 1.2 与 prompt engineering 的区别

| 维度 | Prompt engineering（用户侧） | Prompt-level SEO（内容侧） |
|------|------------------------------|----------------------------|
| 操作主体 | 终端用户（或开发者代用户） | 内容创作者 |
| 目的 | 让 LLM 输出更准确 / 更长 / 特定风格 | 让 LLM 在用户提问时引用自家内容 |
| 控制手段 | 写更精细的 prompt | 写多覆盖度的内容 |
| 反馈回路 | 即时（看输出） | 延迟（依赖 LLM 训练 / RAG 召回） |

**关键混淆点**：服务商话术常把这两者揉成一团，"做 prompt 工程让你被 AI 引用"——这是**类别错误**。

### 1.3 与传统 SEO 关键词工程的关系

| 维度 | 传统 SEO 关键词工程 | Prompt-level SEO |
|------|--------------------|--------------------|
| 信号载体 | 内容里的关键词频次 / 位置 / 密度 | 内容能否被多种 prompt 变体的语义召回 |
| 优化对象 | 词袋模型时代的检索算法 | 向量检索 / RAG 召回的语义匹配 |
| 是否仍有效 | 中文搜索引擎仍部分有效 | LLM RAG 中**关键词命中**的角色弱化，**语义覆盖**的角色上升 |

**关键观察**：传统关键词工程在 LLM 场景**没有完全失效**（RAG 通常是稀疏检索 + 密集检索混合），但**关键词堆砌的边际收益更接近 0**——LLM 答案不会因为某词出现 N 次而更引用某内容。

## 二、中文 prompt 与英文 prompt 的结构差异

### 2.1 分词 / token 化

| 维度 | 英文 | 中文 |
|------|------|------|
| 词边界 | 空格自然分词 | 无空格，需 tokenizer 切分 |
| 不同 LLM 的差异 | 较小（多数用 BPE） | **较大**——同一句中文在不同 LLM 上 token 数差异可达 20-40% |
| 内容方可控性 | 写作时即明确边界 | 写作时不可知（取决于具体 LLM tokenizer） |

**关键事实**：中文同一句在不同 tokenizer 下的切分差异比英文大很多——这意味着"针对某 LLM 的 tokenizer 优化关键词"在跨 LLM 时几乎不可移植。

### 2.2 长度密度

中文同等信息量约为英文的 **2/3 长度**（按字符数）但**token 数因 tokenizer 而异**。这导致：

- 中文 query 通常比英文 query 短
- 但中文 query 的**语义密度**（每单位信息量）更高
- 内容方需要在更短的语义单位里覆盖更多变体

### 2.3 同义词 / 俗称 / 行业黑话

| 类型 | 例子 | 影响 |
|------|------|------|
| 正名 vs 俗称 | "新型冠状病毒"vs"新冠"vs"那啥" | 同一概念多种表达，LLM 召回时能否合并取决于训练 |
| 网络谐音 | "鸡你太美"（蔡徐坤）/"芜湖起飞"（兴奋） | 跨域语义飘移，LLM 训练时机决定是否能识别 |
| 行业黑话 | "白嫖"（不付费使用）/"破防"（情绪触动）/"OOM"（out of memory） | 圈层内通用，圈外不解 |
| 错别字 / 形近字 | "百度"vs"百渡"（少见但存在） | 中文 LLM 通常能纠正，但拼音输入错误的情况未必 |
| 简繁混用 | "网络"vs"網路"vs"網絡" | 简繁映射在不同 LLM 上的处理一致性未公开 |

**关键观察**：中文 query 的多样性远高于英文——这反过来意味着"prompt 变体覆盖"的工程量更大，**但收益曲线递减**：覆盖 80% 主流变体可能只需要 20% 的工程量。

### 2.4 中文 query 的句式特征

中文 LLM query 与中文搜索 query 是否有显著差异？**几乎没有公开数据**支撑结论，但行业观察显示：

- LLM query 倾向**更长 / 更对话化**（"帮我讲讲 X 的历史"vs 搜索"X 历史"）
- LLM query 包含更多**约束条件**（"用 200 字解释 X，从 Y 角度"）
- LLM query **复合性更强**——一个 query 可能同时问多个相关问题

这一观察**未被严格实证**——是仓库需要补的中文实证之一。

## 三、各中文 LLM 的 tokenizer / query 处理：已知 vs 未公开

| LLM | tokenizer 公开度 | query rewrite / 同义词扩展行为 | 已知 / 推测 |
|-----|------------------|------------------------------|-------------|
| Qwen 系列 | **完全公开**（HuggingFace） | 千问 APP / 闭源版的 query 处理不公开 | 开源版可严格分析；闭源 APP 行为待观察 |
| DeepSeek 系列 | **完全公开**（HuggingFace） | chat.deepseek.com 的 query 处理不公开 | 开源 vs 服务侧可能有差异 |
| 豆包 | 不公开 | 行为观察显示存在自动 query 改写 | 字节系内部 tokenizer，外部不可知 |
| 文心 | 不公开 | 文心助手与百度搜索内嵌 AI 的 query 处理可能不同 | 详见 [`platforms/wenxin/citation-mechanism.md`](../platforms/wenxin/citation-mechanism.md) |
| 元宝 | 不公开 | 多模型路由可能导致同一 query 被不同模型不同处理 | 详见 [`platforms/yuanbao/citation-mechanism.md`](../platforms/yuanbao/citation-mechanism.md) |
| Kimi | 不公开 | 长上下文场景下的 query 处理特殊 | URL 抓取触发改变 query 形态 |

**关键观察**：开源（Qwen / DeepSeek）和闭源 APP 之间存在**信息不对称**——开源模型的 tokenizer 可严格分析，但用户实际使用的是 APP / Web 版（含未公开的检索增强 + query rewrite 层），所以**开源 tokenizer 的可分析性≠服务侧行为可分析**。

## 四、内容侧能做什么（操作建议）

不能做：

- **针对某 LLM tokenizer 调整关键词分布**——闭源 LLM 不公开 tokenizer，开源 vs APP 行为可能差异；优化跨 LLM 不可移植
- **塞各种 prompt 变体的关键词到内容里**——这是关键词堆砌的 LLM 版本，[`princeton-9-strategies-cn.md`](./princeton-9-strategies-cn.md) 第 9 策略已经反向证据明确

可以做：

- **写 FAQ 风格内容**——用户怎么问，内容里就有怎么答的语段（语义召回友好）
- **同主题多视角覆盖**——同一概念用 3-5 种说法（正名 + 俗称 + 行业表达）自然出现
- **别名 / 同义词出现在自然语境中**——不是堆叠，是语义铺设
- **使用清晰的子标题（H2 / H3）**——RAG 召回往往按段落，子标题帮助语义边界划分

**核心原则**：从"关键词堆砌"思维转向"用户问法覆盖"思维。这听起来玄学但有实操区别——前者数关键词频次，后者数 prompt 变体覆盖度。

## 五、待验证元假说

### 元假说 A：同一 query 在不同中文 LLM 上的引用信源池差异 > 30%

- 表述：用相同的中文 query 询问 5 大中文 LLM，引用源 URL 的 Jaccard 相似度 < 0.7（即重合 < 70%）
- **驱动力**：各 LLM 的 query rewrite + RAG 召回 + 训练数据均不同
- **如何验证**：[`exp-five-vendor-paired-queries`](../experiments/exp-five-vendor-paired-queries.md) 数据可直接析出"信源池 Jaccard"维度
- **含义**：服务商话术"做一次内容覆盖所有 LLM"基本不成立——内容必须按 LLM 分流

### 元假说 B：中文用户的 LLM query 长度显著大于搜索 query

- 表述：在同一用户 / 同一意图下，向中文 LLM 提交的 query 长度 > 向中文搜索引擎提交的 query 长度，差距均值 ≥ 50%（按字符数）
- **驱动力**：LLM 对长 / 复合 query 的兼容度更高，用户行为自然演化
- **如何验证**：被动观察——用户研究 / 公开 dataset 对照（如有）
- **风险**：缺乏开放 dataset，需平台合作或自有数据

### 元假说 C："prompt 关键词覆盖度"对中文 LLM 引用率的边际效应 < 5pp

- 表述：内容里关键词覆盖度（覆盖 prompt 变体词的密度）高 vs 低，引用率差异 < 5pp（仓库弱效应阈值）
- **含义**：服务商话术"prompt 关键词优化"在中文 LLM 上大概率无效
- **如何验证**：A/B 对照——同主题"关键词覆盖度高 vs 低"的引用率
- **关联**：[`structured-data-cn-practice.md`](./structured-data-cn-practice.md) 元假说 B（schema 边际效应接近 0）的姊妹假说

### 元假说 D：起效的是"用户问法覆盖"而非"prompt 关键词覆盖"

- 表述：内容用 N 种用户问法（FAQ + 多视角）覆盖同一概念时，引用率显著高于内容中关键词频次匹配但缺乏多问法的对照组
- **驱动力**：RAG 召回是语义匹配为主、关键词命中为辅
- **如何验证**：A/B 对照——"FAQ 多视角内容 vs 关键词高密度内容"
- **优先级**：⭐⭐⭐ 最高——这是 prompt-level SEO 的真正可操作命题

### 元假说 E：跨 LLM tokenizer 差异对内容方的引用率几乎无影响

- 表述：内容方在写作时**完全不需要考虑** tokenizer 差异——tokenizer 是 LLM 内部机制，外部不可控也不需可控
- **含义**：服务商话术"针对 X LLM tokenizer 优化"是**伪需求**
- **如何验证**：受控实验——同内容（不针对 tokenizer 设计）vs 同内容（针对 Qwen tokenizer 调整字段切分）的引用率
- **副作用**：本假说成立则一系列 tokenizer 优化服务话术可被直接判定无效

## 六、实验设计建议

### 实验 1：同 query 多 LLM 引用信源池差异（验证元假说 A）

- **目标**：量化中文 LLM 间的 query 处理差异
- **数据来源**：可从 [`exp-five-vendor-paired-queries`](../experiments/exp-five-vendor-paired-queries.md) 跑出来后的数据直接析出
- **优先级**：⭐⭐⭐ 高（无需新数据采集）

### 实验 2：FAQ 多视角内容 vs 关键词高密度内容引用率对照（验证元假说 D）

- **目标**：验证"用户问法覆盖"思维的实际收益
- **设计**：
  - 自变量：2 档（同主题 FAQ 多视角 vs 同主题关键词高密度）
  - 因变量：5 大中文 LLM 引用率
  - 控制：主题、长度、域名权重
- **样本**：每档 ≥ 20 篇 × 30 天观察
- **优先级**：⭐⭐⭐ 最高（这是 prompt-level SEO 真正可操作命题的检验）
- **复用**：[`exp-doubao-vs-deepseek-paired`](../experiments/exp-doubao-vs-deepseek-paired.md) 工具栈

### 实验 3：tokenizer 优化的"伪需求"反向证伪（验证元假说 E）

- **目标**：证伪"针对 tokenizer 优化"话术
- **设计**：A 组内容自然写作；B 组内容专门针对 Qwen tokenizer 优化字段切分；对照引用率
- **预期**：差异 < 5pp（弱效应）
- **优先级**：⭐⭐ 中

### 不建议做的实验

- **"中文 LLM query 长度分布的主动调研"**：需大量真实用户数据，仓库无能力完成；改为引用第三方研究（如有）
- **"针对每个 LLM tokenizer 单独优化"对照实验**：跨 LLM 不可移植，结论价值低
- **"prompt 关键词密度优化"实验**：与 Princeton 第 9 策略关键词堆砌反向证据冲突，结论已可预期

## 七、与 GEO 服务商话术的对照

国内常见话术：

- "做 prompt 工程让你被 AI 引用"
- "针对 X LLM 的 tokenizer 做关键词优化"
- "AI 时代关键词不过时，要做 prompt 关键词覆盖"
- "我们提供 prompt-level SEO 服务"

**本卡片判定**：

| 话术 | 判定 | 理由 |
|------|------|------|
| "做 prompt 工程让你被 AI 引用" | ❌ 类别错误 | Prompt engineering 是用户侧；内容方不可控 |
| "针对 X LLM tokenizer 优化" | ❌ 伪需求 | 元假说 E；跨 LLM 不可移植，闭源 LLM 不公开 |
| "AI 时代关键词不过时" | ⚠️ 半对 | 关键词没"完全失效"，但"堆砌的边际收益接近 0" |
| "Prompt 关键词覆盖" | ⚠️ 名字误导 | 实质是"用户问法覆盖"——FAQ + 多视角写作，不是关键词堆砌 |
| "FAQ 风格内容更易被 AI 引用" | ✅ 与元假说 D 部分一致 | 用户问法覆盖维度成立，但还需实证效应量级 |

**结论**：服务商话术里**与"用户问法覆盖"思维对齐**的部分相对靠谱；**与"关键词 / tokenizer 优化"对齐**的部分大概率是**伪需求 + 类别错误**。

## 八、与本仓库其他卡片的关系

- 与 [`princeton-9-strategies-cn.md`](./princeton-9-strategies-cn.md)：第 9 策略"关键词堆砌"是 prompt 层面"反向"证据（Princeton 实证关键词堆砌不仅无用，还可能反向）；本卡补全"那么什么是有效的 prompt 维度"问题
- 与 [`structured-data-cn-practice.md`](./structured-data-cn-practice.md)：本卡元假说 C 与该卡元假说 B（schema 边际效应接近 0）同源——都是"对 LLM 不可见的元数据 / 元结构优化无效"
- 与 [`knowledge-graph-cn.md`](./knowledge-graph-cn.md)：百科条目天然是"用户问法覆盖"的优秀载体（百科开头一段定义 + 别名 + 多角度展开）；本卡与百科卡片在"内容形态"维度互补
- 与 [`experiments/query-set-v1.md`](../experiments/query-set-v1.md) 第二节：query 类型分层是本卡 prompt 多样性的具体实现
- 与 [`exp-five-vendor-paired-queries`](../experiments/exp-five-vendor-paired-queries.md)：本卡元假说 A 可从该实验直接析出
- 与 [`glossary/terms.md`](../glossary/terms.md) `prompt-level-seo` slug：本卡是该 slug 的主卡片

## 九、不做的事

- **不做"prompt engineering 教程"**——本仓库不收录用户侧 prompt 写作技巧
- **不做"关键词工具链推荐"**——5118 / 词库 / Ahrefs 等关键词工具评测不在本卡范围
- **不复述各 LLM tokenizer 的具体词表细节**——读 HuggingFace 仓库更准
- **不预先断言中文 LLM 是否做 query rewrite**——5 家厂商都没公开
- **不为"关键词覆盖度"给量化目标**（如"覆盖 80% 长尾词"）——这是话术，无实证

## 十、待解决的未知 / 公开数据空白

1. 5 大中文 LLM 的 query rewrite 行为（**完全空白**——豆包 / 文心 / 元宝 / Kimi 都不公开）
2. 中文用户的 LLM query 与搜索 query 的实际差异（**完全空白**，无开放 dataset）
3. RAG 召回中"稀疏检索 vs 密集检索"的混合权重（厂商不公开）
4. 中文 LLM 对同义词 / 别名的合并能力（仅靠 ad hoc 测试）
5. FAQ 风格内容是否真的比单视角内容引用率高（实验 2 的核心）
6. 简繁中文在不同 LLM 上的处理一致性

## 十一、衍生 BACKLOG 建议

- `exp-cn-llm-query-rewrite-passive`：被动观察实验——通过对同一 query 询问多次看是否答案不同来推测 query rewrite 行为
- `exp-cn-faq-vs-keyword-density`：实验 2（FAQ 多视角 vs 关键词高密度）的独立条目
- `exp-cn-jaccard-of-cited-sources-cross-llm`：实验 1（信源池 Jaccard）的独立条目，可与 [`exp-five-vendor-paired-queries`](../experiments/exp-five-vendor-paired-queries.md) 数据复用
- 新增 `tech-cn-long-tail-keyword-vs-prompt-variants`：把传统长尾关键词挖掘和 prompt-level 变体覆盖的方法论对比
- 与 [`tech-multimodal-cn`](../BACKLOG.md)（待建）协调：多模态 prompt 是另一个未涉及维度

## 变更记录

- 2026-05-02：初版。澄清 prompt-level SEO 概念（实质是"用户问法覆盖"，不是"操控 prompt"）+ 中英 prompt 结构差异 + 各 LLM tokenizer 公开度对照 + 5 条元假说 + 3 个实验设计建议。confidence: low，maturity: concept，等待实验 2 数据回写。
