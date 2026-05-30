---
title: 投毒攻击在中文 GEO 的现实性威胁建模与防御导向研究草稿
type: audit
sources:
  - url: https://openreview.net/forum?id=oTeixD3oZO
    fetched_at: 2026-05-30
    note: C-SEO Bench (NeurIPS 2025) — 仓库通用怀疑锚点
  - url: https://www.usenix.org/conference/usenixsecurity25/presentation/zou-poisonedrag
    fetched_at: 2026-05-30
    note: PoisonedRAG (USENIX Sec 2025) — RAG 检索期投毒奠基性工作
  - url: https://www.stcn.com/article/detail/3677723.html
    fetched_at: 2026-05-30
    note: 央视 3·15（2026）AI 投毒实测 — 中文场景最硬一手证据
  - url: https://www.newsguardtech.com/special-reports/deepseek-ai-chatbot-china-russia-iran-disinformation/
    fetched_at: 2026-05-30
    note: NewsGuard DeepSeek 审计 — 中文 LLM 被波及的一手审计
confidence: low
verified: false
last_verified: 2026-05-30
platforms:
  - doubao
  - deepseek
  - wenxin
  - qianwen
  - yuanbao
  - baidu
techniques:
  - anti-geo-monitoring
  - knowledge-graph-cn
  - private-vs-public-source-cn
  - citation-attribution-styles-cn
maturity: concept
related:
  - ../techniques/anti-geo-monitoring-cn.md
  - ../techniques/dimension-map-cn.md
  - ../BACKLOG.md
last_updated: 2026-05-30
---

# 投毒攻击在中文 GEO 的现实性威胁建模与防御导向研究草稿（2026-05-30）

> **性质**：研究草稿，非正式技术卡。源自一次 6 路并行调研 + 1 路对抗性核验。落在 `audits/` 而非 `techniques/`——因为仓库正处"实证瓶颈"，[`2026-05-04 审计`](./2026-05-04_meta-hypothesis-audit.md) 已警告勿再"概念叠卡"。是否升级为 `techniques/poisoning-attack-surface-cn.md`（DS 维度子卡 #3），待 §7 衍生实验 E\* 产出第一手数据后再决定。
>
> **边界**：严格防御导向 / 威胁建模导向，**不含任何针对线上第三方商用系统的可操作攻击步骤**。与 [`CONTRIBUTING.md`](../CONTRIBUTING.md) "不收录黑帽，研究为什么有效 / 如何被识别可以、操作手册不行"红线一致。
>
> **可证伪性标注**：**F**（可证伪，有明确验证/证伪路径）/ **P**（部分可证伪，依赖未公开数据）/ **N**（暂不可证伪，机制合理但无独立大样本实证）。
>
> **证据强度三级**：confirmed（顶会确证 / 多机构交叉 / 厂商承认 / CVE 补丁）/ PoC（受控演示，未在生产发生）/ rumor（单方报告、利益相关、低粒度）。

## 校正说明（相对原始调研底稿的 8 处修正）

本草稿在写入前，已对原始调研底稿应用对抗性核验抓到的 8 处修正。**保留此清单作为认知演化痕迹**：

| # | 原始底稿的错误 | 核验结论 | 本草稿的处理 |
|---|---------------|---------|------------|
| 1 | CPA-RAG 的 arXiv ID 标 `2505.11548` | 错；`2505.11548` 实为另一篇 "One Shot Dominance / AuthChain"（EMNLP 2025） | 改为正确 ID **`2505.19864`** |
| 2 | 拿 POISONCRAFT（`2505.06579`，一篇*攻击*论文）当"证伪投毒"的怀疑论证据，挂"85%→30%""3-5% 语料"数字 | 张冠李戴；怀疑论框架更接近 CorruptRAG（`2504.03957`） | 怀疑论数字改引 CorruptRAG；POISONCRAFT 仅作"攻击侧 ASR-t≈31%@k=10/20"事实引用 |
| 3 | 称 C-SEO Bench "仅测 2 个英文模型" | 错；实跑 4 个（gpt-4o-mini / claude-3-5-haiku / o3 / o4-mini） | 改正模型数；外推到中文的论证支点从"模型覆盖窄"改为"全英文模型 + 英文 HTML 语料" |
| 4 | Harvard "主流查询 5% 命中、三分之二带警告" | "5%" 确证；"2/3 带警告"原文查无 | 删"2/3 带警告"，补 Harvard 真实发现（Gemini 2.5 Flash 13.5% 且仅其显著） |
| 5 | §0 "监管 + 平台风控**正在快速收窄**可写入口" | 偏满；清朗专项运动式 vs 制度化未定 | 降一档为"正在收窄（执行持久性待 2026 Q3-Q4 复核）" |
| 6 | §1.1 表 "Pravda 波及 DeepSeek" 整体标 confirmed，机制列"共享 Pravda 污染语料" | 复述 confirmed，但"因为共享语料"是推断因果 | 证据列拆为"复述 confirmed / 因果机制 推断" |
| 7 | 单边引 "Overcoming the Retrieval Barrier"（`2601.07072`）当"投毒难奏效"证据 | cherry-pick；该论文主贡献恰是*攻破*检索壁垒 | 平衡引用：承认其动机段证明"未优化文本检索不到"，但点明其提出新攻击破壁 |
| 8 | 一处误写 "3·11 / 3·15" | 应为 3·15（3 月 15 日晚会） | 统一为 3·15 |

---

## 0. 一句话判决（投毒在中文 GEO 到底有多现实）

**"投毒能稳定改变中文商用 LLM 输出"是被夸大的默认事实；真实结论是分层的——RAG 检索期投毒是唯一在中文生产环境有现场确证（2026 央视 3·15）的攻击面，但其生效高度依赖 data void（信息空白）这一苛刻前提，对已有权威覆盖的成熟实体预期大幅失效；监管 + 平台风控正在收窄"可写入口"（执行是运动式还是制度化，待 2026 Q3-Q4 复核）。** 〔判决标注：**P**——3·15 实测确证投毒"可发生"是 confirmed，但"对成熟实体也有效""能稳定操纵复杂决策"无独立大样本证据〕

三个层级：

1. **可发生（confirmed）**：3·15 现场实测从发 1 篇虚构软文到 7 家 AI 复述仅 2 小时；PoisonedRAG 在学术 benchmark 上 90%+ ASR；Pravda 网络多机构交叉证实污染了西方 LLM + 波及 DeepSeek 输出。这一层不存疑。
2. **效果上限存疑（C-SEO Bench 锚点）**：90%+ ASR 几乎全部来自玩具数据集 + 已知 query + 单 actor + 无防御；Harvard 实测主流查询投毒仅 5% 命中；3·15 的 Apollo-9 恰是零权威覆盖的虚构新品（极端 data void）。C-SEO Bench（NeurIPS 2025）证明严格控制 + 多 actor 竞争下多数 GEO 方法无效甚至负效。
3. **窗口收窄（中文独有强约束）**：2026-04-30 网信办"清朗·整治 AI 应用乱象"专项首次把"恶意 GEO 营销 / AI 数据投毒"列为整治对象，百家号 / 搜狐号 / 头条号矩阵被大批封禁降权（钛媒体）。但执行持久性未定，列为 §8 空白 #10。

**对仓库基调的校准**：C-SEO Bench 证伪的是"单篇内容改写式 GEO"——正对应该反的尾部 SEO 软文型话术；而 Pravda / 3·15 证实的"海量协同灌站 + 传统 SEO 抬源排名"是另一回事，恰是 C-SEO Bench 认定**可能有效**的那一类。**怀疑锚点应精确指向"发 10 篇软文就能改 AI 输出"的尾部话术，而非泛化否定一切协同污染。**

---

## 1. 案例（按证据强度 confirmed / PoC / rumor 分级）

### 1.1 confirmed —— 顶会确证 / 多机构交叉 / 厂商承认修复 / CVE 补丁

| 案例 | 机制一句话 | 关键数字 | 证据级别 | 来源 |
|------|-----------|---------|---------|------|
| **央视 3·15 AI 投毒实测**（2026） | 淘宝买"力擎"GEO 系统→给虚构"Apollo-9 手环"灌假软文→发 1 篇 2 小时后 7 家 AI 复述 | 2 小时时延（判决性：只能是联网检索）；39.9 元起 | confirmed（监管机构现场实测，全球罕见） | [证券时报](https://www.stcn.com/article/detail/3677723.html)、[36氪](https://36kr.com/p/3724411683895943) |
| **俄罗斯 Pravda 网络 LLM grooming** | ~150-300 伪新闻域名年发 360 万文 ×激进 SEO×多语种淹没爬虫 | NewsGuard 测 10 大 chatbot 平均 33% 复述；2025-05 复测降至 15-20% | confirmed（NewsGuard + ASP + DFRLab + Viginum 四方交叉） | [NewsGuard](https://www.newsguardtech.com/special-reports/moscow-based-global-news-network-infected-western-artificial-intelligence-russian-propaganda)、[DFRLab](https://www.atlanticcouncil.org/blogs/new-atlanticist/exposing-pravda-how-pro-kremlin-forces-are-poisoning-ai-models-and-rewriting-wikipedia) |
| **Pravda 波及 DeepSeek**（中文最硬一手） | DeepSeek 复述虚假叙事 + 自身官方叙事偏好叠加 | 35% 复述俄/伊虚假叙事、60% 框中国政府视角、fail rate 83% | **复述 confirmed / "因共享 Pravda 语料"机制为推断** | [NewsGuard DeepSeek 报告](https://www.newsguardtech.com/special-reports/deepseek-ai-chatbot-china-russia-iran-disinformation/) |
| **Google AI Overviews 翻车**（2024-05） | RAG 检索 Reddit 玩笑 / The Onion 讽刺当权威 | "披萨加胶水""每天吃石头" | confirmed（厂商承认并降权修复） | [TechCrunch](https://techcrunch.com/2024/05/30/google-changes-ai-overviews/) |
| **Gootloader SEO poisoning** | 入侵 WordPress 站群×"合同/协议/模板"法律词→投恶意软件 | UNC2565（Mandiant）/ Storm-0494（MSTIC），2020 至今，专打律所 | confirmed（多家威胁情报 IOC） | [Intel 471](https://www.intel471.com/blog/threat-hunting-case-study-tracking-down-gootloader) |
| **EchoLeak（CVE-2025-32711）** | M365 Copilot 零点击间接注入→邮件藏指令→外泄内部文件 | 首个生产 LLM 零点击数据外泄；CVSS 9.3；OWASP LLM01 | confirmed（CVE + 微软 2025-06 补丁） | [arXiv 2509.10540](https://arxiv.org/html/2509.10540v1) |
| **Bing/Sydney 系统提示词泄露**（2023-02） | "Ignore previous instructions"直接注入 | 泄出代号 Sydney + 完整 system prompt | confirmed（微软确认打补丁） | [Astra Security](https://www.getastra.com/blog/ai-security/prompt-injection-attacks) |
| **ZeroFox LLM-targeted SEO poisoning**（野外） | 伪造客服号 PDF 传 .edu/.gov→Gemini 当合法联系方式 | "数十份"跨多校/政府域 | confirmed in-the-wild（低粒度，无量化品牌数） | [ZeroFox](https://www.zerofox.com/blog/seo-poisoning-llms/) |

### 1.2 PoC —— 受控实验 / 演示，未在生产环境发生

| 案例 | 机制 | 边界（caveat） | 来源 |
|------|------|--------------|------|
| **Anthropic 250 文档投毒**（2025-10） | `<SUDO>` 触发词预训练后门，250 篇可靠植入，跨模型参数规模绝对数恒定 | **仅 DoS 乱码后门**；作者自注"不太可能对前沿模型构成重大风险"、能否扩展到改事实"尚不清楚" | [Anthropic](https://www.anthropic.com/research/small-samples-poison)、[arXiv 2510.07192](https://arxiv.org/pdf/2510.07192) |
| **Persistent Pre-training Poisoning**（ICLR 2025） | 测预训练投毒穿透 SFT+DPO 后是否存活 | 0.1% 即 4 类中 3 类（DoS/belief/context-extraction）穿透；jailbreak **不**存活——真正回答"穿透对齐" | [arXiv 2410.13722](https://arxiv.org/html/2410.13722v1) |
| **PoisonGPT**（2023） | ROME 编辑 GPT-J-6B 植"埃菲尔铁塔在罗马"，benchmark 仅差 0.1% | 纯演示，传 HuggingFace 获 40+ 下载 | [Barracuda](https://blog.barracuda.com/2025/09/11/poisongpt-weaponizing-ai-disinformation) |
| **CPA-RAG**（西电×蚂蚁，2025） | 黑盒多开源 LLM 生成自然对抗文本，top-k=5 ASR>90% | **arXiv 预印本未评审**；未明确所需文档数 / 是否专测中文 | [arXiv 2505.19864](https://arxiv.org/pdf/2505.19864) |
| **知危实验 / B站次日复刻** | 同文章发新浪/网易/知乎/搜狐→AI 推荐"知危" | 单次 PoC；3·15 后 AI 迅速"清醒"，但次日新虚构配方又骗到一次 | [虎嗅](https://www.huxiu.com/article/4843683.html) |
| **Common Crawl 中文污染审计** | DFRLab 审计出 Pravda / 中国政府关联 Glassbridge / RT 已进开放训练管线 | 证明"语料被动含毒"≠"可定向操纵某条事实" | [DFRLab](https://dfrlab.org/2026/04/08/pravda-in-the-pipeline/) |

### 1.3 rumor / 厂商情报级 —— 单方报告、低粒度、利益相关

| 案例 | 性质 | 为何降级 |
|------|------|---------|
| **agent-aware cloaking（ChatGPT Atlas）** | 按 user-agent 给 AI 投喂不同页面，伪简历 AI 评 88 vs 人类 26 | 多为安全厂商博客 + 预印本（arXiv 2509.00124），缺独立大规模复现 |
| **中文"被投毒监测"厂商案例** | "48h 内 200 山寨账号洗版致 Kimi 显示假货链接"（Tocanan）、各"2026 GEO 测评" | 营销物料，部分本身是反 GEO 厂商在做 GEO 式自我推荐 |
| **中文协同灌站改国产 LLM 输出** | 百度百科代编 / SEO 软文矩阵 / 营销号站群 | 机制合理但**无任何公开确证个案**——这是中文场景核心空白 |

**案例层的判决**〔**F**〕：把"案例存在"等同于"投毒普遍有效"是过度外推。所有高 ASR / 高复述率数字要么来自学术 benchmark（单 actor + 无防御），要么来自 data void 极端条件（虚构新品 / 冷门地缘叙事），要么是利益相关方自述。**中文场景唯一的硬一手证据是 3·15（确证可发生）+ DeepSeek 复述（掺杂官方叙事偏好混淆变量）**，两者都是"让 AI 复述错误事实"级别，非操纵复杂决策。

---

## 2. 技术上

### 2.1 学术技术分类总表（按攻击面 × 证据强度）

| 攻击面 | 代表工作 | 机制 | 所需投毒量 | 持久性 | 可检测性 | 证据 | 来源 |
|--------|---------|------|-----------|--------|---------|------|------|
| **训练期 / 预训练** | Anthropic 250 文档（2025） | `<SUDO>` 触发 DoS 后门 | 250 篇绝对数（占比随模型规模降到 ppm 级） | 仅预训练，未声称穿透后训练 | 极低 | confirmed（博客+arXiv，非顶会） | [arXiv 2510.07192](https://arxiv.org/pdf/2510.07192) |
| **训练期 / 持久性** | Persistent Pre-training（ICLR 2025） | 测穿透 SFT+DPO 后存活 | DoS 0.001% / context+belief 0.1% 存活；jailbreak 不存活 | **真正回答"穿透对齐"** | 低 | **confirmed（ICLR 2025，最硬）** | [arXiv 2410.13722](https://arxiv.org/html/2410.13722v1) |
| **训练期 / Web-scale** | Carlini split-view+frontrunning（S&P 2024） | 买过期域名替换内容 / 快照前注入 | ~$60 污染 0.01% LAION/COYO | frontrunning 因快照可在修正后存活 | 可防（哈希校验 / 延迟快照） | confirmed（S&P 2024，负责任披露） | [arXiv 2302.10149](https://arxiv.org/abs/2302.10149) |
| **训练期 / 百科** | Wikipedia frontrunning（同上） | 篡改维基→污染整训练集 0.27% | 高（快照已分发） | 中（vandalism 检测"单独不足"） | confirmed（可行性测算） | 同上 |
| **训练期 / 医疗** | Nature Medicine（2024） | The Pile 注入 0.001% 医疗假信息 | ~$5 | 需重训生效 | 中 | confirmed | [Nature Medicine](https://www.nature.com/articles/s41591-024-03445-1) |
| **检索期 / RAG 内容** | PoisonedRAG（USENIX Sec 2025） | 同时满足检索条件+生成条件 | 5 篇/问题（百万级库 ppm 级） | 留库即持续 | 中（困惑度 / KE / RobustRAG 部分识别） | **confirmed（奠基性）** | [USENIX](https://www.usenix.org/conference/usenixsecurity25/presentation/zou-poisonedrag) |
| **检索期 / 相关性** | Corpus poisoning（EMNLP 2023） | HotFlip 离散 token 扰动对抗段落 | ~50 篇误导 >94% 跨域 query | 留库 | 中（高困惑度可捕获） | confirmed | [ACL Anthology](https://aclanthology.org/2023.emnlp-main.849/) |
| **检索期 / SEO 提权** | GASLITE（ACM CCS 2025） | gradient-based 对抗段落，最强检索 SEO 投毒 | ≤0.0001% 语料 | 留库 | 中（比早期隐蔽） | confirmed | [CCS 2025](https://dl.acm.org/doi/10.1145/3719027.3765095) |
| **检索期 / 中文黑盒** | CPA-RAG（西电×蚂蚁 2025） | 多开源 LLM 生成自然对抗文本 | 未明确 | 留库 | 主打隐蔽（绕困惑度） | **PoC（未评审）** | [arXiv 2505.19864](https://arxiv.org/pdf/2505.19864) |
| **检索期 / 阻断** | Jamming/Blocker Docs（USENIX Sec 2025） | blocker 文档让模型拒答 | — | 留库 | 中 | confirmed | [USENIX](https://www.usenix.org/system/files/usenixsecurity25-shafran.pdf) |
| **检索期 / 实用攻击** | POISONCRAFT（2025） | 真实检索条件下的实用投毒 | — | 留库 | 中 | PoC（ASR-t≈31%@k=10/20） | [arXiv 2505.06579](https://arxiv.org/pdf/2505.06579) |
| **推理期 / 间接注入** | Greshake et al.（AISec 2023） | 指令藏进会被检索的内容 | 单内容即可 | 取决于内容存活 | 难（隐藏文字 / 同形字 / OCR） | **confirmed（Bing Chat 实演 + OWASP LLM01）** | [arXiv 2302.12173](https://arxiv.org/abs/2302.12173) |
| **推理期 / cloaking** | parallel-poisoned web（2025） | 按 user-agent 投喂 AI 不同页面 | 规则常驻 | 持续 | 中（对比 UA 抓取差异） | rumor/PoC 混合 | [arXiv 2509.00124](https://arxiv.org/pdf/2509.00124) |
| **知识库 / KGE** | Bhardwaj et al.（EMNLP 2021） | 增删三元组操纵 link prediction | 少量精选三元组 | 重训前持续 | 中（一致性检查） | confirmed | [arXiv 2111.06345](https://arxiv.org/pdf/2111.06345) |
| **知识库 / GraphRAG** | GRAGPOISON（2025） | 关系注入制造竞争性覆盖 | 单次可覆盖多查询 | 重索引前 | **抽取层自带过滤** | PoC | [arXiv 2501.14050](https://arxiv.org/html/2501.14050v2) |

**总表的三个反话术读法**：

1. **量纲不统一是横向比较的陷阱**〔**F**〕：训练投毒按"绝对文档数 / 占比"，检索投毒按"每问题文本数 / ppm"，注入按"单内容即可"，KG 按"三元组数"——直接比"哪个最容易"是错的。**对追求即时 ROI 的中文 GEO 黑产，唯一量纲匹配的是检索期**（小时级 + 零模型权限 + 成本最低）。
2. **持久性是两个概念、常被混用**〔**F**〕：训练投毒的持久性 = "穿透后训练对齐"（ICLR 2025 才真正证明，且 jailbreak 不存活）；检索投毒的持久性 = "毒文本留库即生效"——后者根本没碰模型权重。
3. **90%+ ASR 的真实检索衰减**〔**P**〕：CorruptRAG（[arXiv 2504.03957](https://arxiv.org/abs/2504.03957)）指出 PoisonedRAG 式攻击"毒文本数量压过正确文本"的假设在生产不现实；真实检索下 ASR 随查询语义距离增大、竞争文档增多而显著下降。POISONCRAFT（[arXiv 2505.06579](https://arxiv.org/pdf/2505.06579)）作为实用攻击在 k=10/20 时 ASR-t 也仅约 31%。〔注：原始调研把"85%→30%""生产需 3-5% 语料"挂到 POISONCRAFT 名下属张冠李戴，已删除具体数字，仅保留"真实检索下显著衰减"这一方向性结论；精确数字待 §7 E\* 自测。〕

### 2.2 三层注入机制 × 中文平台可行性矩阵

| 维度 | 层 1 预训练投毒 | 层 2 RAG 检索投毒 | 层 3 KG 抽取投毒 |
|------|----------------|------------------|-----------------|
| **时延** | 月 / 季级（等下次训练） | **小时级**（3·15 实测 2h） | 天 / 周级（重索引） |
| **注入点** | 进训练语料（攻击者控不了爬取/去重/对齐） | **开放公网网页（零模型权限）** | KG 三元组源 |
| **成本** | 高（需进语料 + 等重训） | **最低（39.9 元起）** | 中 |
| **可定向性** | **不可定向** | 可定向（看自己内容是否进引用） | 半定向 |
| **中文生产证据** | rumor（Common Crawl 含毒 confirmed，定向操纵无证据） | **confirmed（3·15）** | 无（仅英文 GraphRAG PoC） |
| **天然防御** | 对齐微调清洗大部分 | 多文档聚合 / 来源审查 | **抽取层 LLM 倾向保留可信关系、丢弃矛盾** |
| **对中文 GEO 黑产性价比** | 几乎无意义（无即时 ROI） | **唯一现实攻击面** | 最差 |
| **confidence** | P（理论可达不可定向） | **F→confirmed（可发生）** | N（中文无生产案例） |

**判决**〔**P**〕：**层 2 RAG 检索期是中文 GEO 投毒唯一现实攻击面**，三条理由——时延唯一匹配黑产即时 ROI；注入点是开放公网零模型权限；共享检索源使单篇污染影响多用户。但"现实"≠"万能"——层 2 生效的关键前提是 **data void 而非投毒本身奏效**。Apollo-9 之所以 2 小时生效，恰因它是零权威覆盖虚构新品。

### 2.3 六大中文平台攻击面映射表

| 平台 | 信源池构成 | 引用归因透明度 | **最可能成功入口** | **几乎无效入口** | confidence |
|------|-----------|--------------|-------------------|-----------------|-----------|
| **DeepSeek** | 几乎无自有生态，官方 App 用第三方搜索 API（博查 Bochaai）+公网 | **最高**（`[citation:X]` 角标 + "已搜索 X 网页"可点开） | 被博查/必应索引的公网高权重信源 | 模型底层权重（铺内容改不了） | high（citation 格式有官方佐证） |
| **豆包（字节）** | 字节自有生态优先（今日头条/抖音/西瓜）+ 公网补充 | 中 | **今日头条号 / 抖音（含字幕/OCR 封面/置顶评论）** | 不在字节生态且无结构化文字落地的纯外站 | medium（占比数字来自服务商物料） |
| **元宝（腾讯）** | 微信公众号（~36 亿篇半公域）+ 视频号 + 搜狗；多模型路由 | 低-中（多模型路由使可观测性差） | **微信公众号文章**（写入开放、抓取近垄断） | 其他平台 GEO 资产（百家号/抖音对元宝几乎无传导） | medium |
| **文心/百度 + 百度 AI 搜索** | 百度自有生态优先（百科自动挂词条+百家号+百度搜索） | 中（给标题/URL/域名/原文片段） | **百家号**（写入开放、被百度优先采纳） | **百度百科主词条**（编辑审核+权威加权，纯铺量难改写） | medium |
| **千问/通义（阿里）** | 绑定阿里电商履约生态；通用搜索由夸克承载 | 中（needReference 标注开关） | **夸克可索引公网 + 学术/文献类内容** | **电商交易链路结构化数据**（商品/价格由阿里闭环风控） | medium |
| **百度 AI 搜索（纯检索增强）** | 强制/按需/私有知识联合三种联网模式 | 中 | 公网信源（攻击面最大） | 百科主词条 | medium |

**映射表的关键区分**〔**P**〕：

- **"读取封闭"≠"写入封闭"**：元宝的微信公众号对外部爬虫半封闭（别家模型难污染你的私域）——但"注册公众号发文"这一写入动作完全开放。封闭性保护"被别人投毒"，不保护"被任何人写入"。
- **"被索引"≠"被引用"**：博查收录近百亿网页、百度百科常排靠前，但厂商 RAG 有去重 / 权威加权 / 交叉验证 / top-k 截断——进候选池≠进最终引用。这正是 C-SEO Bench 打的点。
- **跨平台 GEO 资产几乎不互通**：攻元宝写公众号、攻豆包写头条号、攻文心写百家号——与英文圈"优化一份内容打通多引擎"相反。这是中文"私域 vs 公域光谱更陡峭"的直接后果（对接 [`private-vs-public-source-cn`](../techniques/private-vs-public-source-cn.md) 元假说 B）。**反向锚点见 §9 缺口 #1：若 TabooRAG 式跨模型迁移攻击在中文成立，会动摇此判决。**
- **唯一 confirmed 级**：只有 DeepSeek 的 `[citation:X]` 格式 + 百度 AI 搜索信源关联 + needReference 有官方文档。所有"信源占比/权重"数字（豆包头条 60%+、元宝 36 亿篇）来自服务商营销物料，一律 medium。

---

## 3. 实践 / 全流程：把"复刻一个投毒案例"框成受控可复现实验

### 3.1 伦理与边界（前置硬约束）

> ⚠️ **本节定义的实验只在完全自掌控的沙盒 / 自建语料 / 自建 RAG 实例上做。明确禁止**：
> - 不向任何线上第三方商用系统（豆包/DeepSeek/文心/千问/元宝/Kimi/百度 AI 搜索）注入内容
> - 不发布会被真实用户检索到的误导内容
> - 不坑真实用户、不损害任何真实品牌
> - 全部参照 Carlini（S&P 2024）的负责任披露范式——只验证攻击路径可行性，不实际投毒
> - 凡涉及"线上平台"的部分只做**被动观测**（自己提问拿答案体），不做主动注入

这条边界与 [`CONTRIBUTING.md`](../CONTRIBUTING.md) "不收录黑帽……研究为什么有效 / 如何被识别可以，操作手册不行"红线完全一致——本实验测的是**防御侧的检测信号有效性**，不是攻击配方。

### 3.2 受控实验通用框架（6 步）

```
威胁模型定义 → 沙盒/自建语料/自建 RAG 实例搭建 → 单一注入向量 → 测量 → 预注册阈值判定 → 复盘
```

1. **威胁模型**：明确攻击者能力（能否写入语料？能否优化文本？是否知道目标 query？）——大多数学术高 ASR 假设"已知 query + 可写语料"，生产环境二者都不成立。
2. **沙盒搭建**：自建 retriever（如 bge-large-zh 中文 embedding）+ 自建知识库（公开中文语料子集，如 CMRC2018 / DuReader）+ 自建 RAG pipeline（可开关 KE / 来源白名单 / 困惑度过滤）。
3. **单一注入向量**：一次只测一个攻击面（如只测 RAG 检索期 + 自然文本投毒），避免混杂。
4. **测量**：ASR（目标 query 上模型复述指定答案率）+ 检索召回率（毒文本进 top-k 率）+ 误报率（防御误杀正常文本率）。
5. **预注册阈值**：实验前锁死判定阈值，不事后调整（对齐仓库 `H1_DIFF_THRESHOLD_PP` 锁死原则）。
6. **复盘**：区分"检索失败"（毒文本没进 top-k）vs"生成失败"（进了 top-k 但模型没复述）——这是 PoisonedRAG 两阶段机制的诊断核心。

### 3.3 最小可行实验设计 E\*（对齐 `experiments/` 卡风格）

- **实验 ID**：`exp-cn-rag-poisoning-datavoid-sandbox`
- **类型**：受控沙盒实验（自建 RAG，零线上注入）
- **成本**：¥0 现金 + 4-8 小时搭建 + GPU 推理（可用开源小模型 CPU 跑）
- **判决问题**：**data void 程度是否是中文 RAG 投毒成功的决定变量？**（而非投毒数量）

#### H 假设（预注册）

- **H1（data void 主效应）**：同等投毒量下，"零权威覆盖虚构实体"query 的 ASR 显著高于"高权威覆盖成熟实体"query。
  预注册阈值：`H1_ASR_DIFF_THRESHOLD_PP = 30`（虚构 vs 成熟 ASR 差 ≥ 30pp 判 H1 成立）
- **H2（防御衰减）**：开启 KE（检索文档数 5→20）+ 来源白名单后，ASR 显著下降。
  预注册阈值：`H2_DEFENSE_DROP_PP = 20`（防御后 ASR 下降 ≥ 20pp 判 H2 成立）
- **H3（自然文本隐蔽性）**：低困惑度自然对抗文本的困惑度过滤检出率显著低于高困惑度 GCG 式文本，但不能绕过多文档聚合。
  预注册阈值：`H3_PPL_EVASION_PP = 30`（自然文本检出率比 GCG 式低 ≥ 30pp 判隐蔽性成立）
- **WEAK 阈值**：所有差异 < 5pp 判为"无显著效应"。

#### 样本量

- query 集：40 条 × 2 类（20 虚构零覆盖实体 + 20 成熟高覆盖实体）
- 每 query × 投毒量 3 档（1 篇 / 5 篇 / 占库 3%）× 防御 2 态（开 / 关）× 重复 5 次
- = 40 × 3 × 2 × 5 = **1200 次采集**
- 知识库规模：≥ 10 万段中文语料（保证有竞争性干扰文档，避免玩具数据集偏差）

#### 判定逻辑

| 结果 | 解读 | 回写目标 |
|------|------|---------|
| H1 成立 + H2 成立 | 投毒有效性 = data void × 弱防御，验证"非万能"判决 | 强化本草稿 §0 判决 + [`geo-demand-side-fitness`](../techniques/geo-demand-side-fitness-cn.md) 长尾窄场景 |
| H1 不成立 | data void 不是决定变量，投毒更普遍——**需上调威胁评估** | 触发本草稿判决重审 |
| H3 成立 | 自然文本规避困惑度但栽在聚合——验证"绕困惑度≠绕聚合" | [`anti-geo-monitoring`](../techniques/anti-geo-monitoring-cn.md) N3 检测信号优先级 |

**为什么这是 E\* 而非更激进的设计**：它用自建沙盒完全规避伦理风险，单一注入向量保证可归因，预注册阈值防事后调整，且直接服务于仓库最缺的"生产级防御开启后 ASR 衰减多少"端到端量化空白（见 §8）。**不建议做的实验**：任何向线上商用系统主动注入的"复刻 3·15"——既违反 CONTRIBUTING 红线，又因平台风控/清朗专项实测窗口已收窄而不可复现。

---

## 4. 反话术 / 怀疑视角

### 4.1 投毒成功的前提条件清单（只有同时满足才可能成功）

**缺任何一条，成功率断崖式下降**〔此清单标 **F**——每条前提可在 E\* 沙盒中独立验证〕：

| # | 前提 | 缺失后果 | 证据 |
|---|------|---------|------|
| 1 | **目标处于 data void**（无权威源竞争） | Harvard：主流查询仅 5%（21/416）支持虚假信息；Gemini 2.5 Flash 最高 13.5% 且仅其统计显著 | [Harvard Misinfo Review](https://misinforeview.hks.harvard.edu/article/llms-grooming-or-data-voids-llm-powered-chatbot-references-to-kremlin-disinformation-reflect-information-gaps-not-manipulation/) |
| 2 | **毒文本能被召回进 top-k**（检索条件） | 自然查询下未优化文本"根本检索不到"（但 trigger+fragment 分解可破壁，见来源主结论） | [arXiv 2601.07072](https://arxiv.org/pdf/2601.07072) |
| 3 | **低困惑度 + 语义贴近 + 携带 payload 三者兼顾** | 三约束叠加，优化到极限成功率仍受限 | [EACL 2026 findings](https://aclanthology.org/2026.findings-eacl.108.pdf) |
| 4 | **目标平台无多文档聚合 / 来源白名单 / 交叉验证** | RobustRAG isolate-then-aggregate 提供 certifiable robustness | [arXiv 2405.15556](https://arxiv.org/pdf/2405.15556) |
| 5 | **单 actor（无竞争投毒方）** | C-SEO Bench：多 actor 竞争收益被抵消，呈"congested zero-sum" | [C-SEO Bench](https://openreview.net/forum?id=oTeixD3oZO) |
| 6 | **内容未被辟谣 / 未被监管打掉** | 3·15 后 AI 迅速"清醒"；清朗专项封矩阵号 | [人民网](http://politics.people.com.cn/n1/2026/0430/c461001-40712193.html) |
| 7 | **时间窗口期内**（高时效查询 + 语料稀疏） | 稳态知识查询有权威覆盖，投毒被覆盖 | 推断 N |

### 4.2 生产级防御如何逐层打掉投毒

第三方复现的 PoisonedRAG 单层防御 ASR（[aminrj.com](https://aminrj.com/posts/rag-document-poisoning/)）：无防御 95% → Ingestion Sanitization 95%（无效）→ Access Control 70% → Prompt Hardening 85% → Output Monitoring 60% → **Embedding Anomaly Detection 20%（单层最强）→ 五层叠加 10%**。结论：**单层不够，叠加显著压缩**。生产 defense-in-depth = 来源白名单/provenance + 摄入期清洗 + 检索期元数据过滤 + 重排（RRF）+ 检索后对抗内容分类器。

### 4.3 C-SEO Bench 的精确含义（不要误读为"中文投毒无效"）

C-SEO Bench（NeurIPS 2025）的 Conversational Search Engine 任务实跑 **4 个模型**（gpt-4o-mini / claude-3-5-haiku / o3 / o4-mini；仅 C-SEO 方法实现用 gpt-4o-mini）。54 格仅 3 格显著提升，Statistics 方法 19/24 拉低排名，product+Haiku 26/30 负面。**它证伪的是"内容编辑型 GEO"（改几个字/塞 prompt），不是"对抗性投毒"**。

把它外推到"中文投毒无效"是逻辑跳跃——**真正的缺口不是模型数少，而是它全部是英文模型 + 英文 HTML 语料**，需中文版 benchmark 才能直接支撑（见 §7 衍生 BACKLOG #5）。它的真正价值：**精确锚定该反的对象 = "单篇内容改写就能操纵 LLM"的尾部软文话术**，而非否定 Pravda 式协同灌站。

### 4.4 哪些是被夸大的（点名祛魅）

| 被夸大的主张 | 真相 | 标注 |
|------------|------|------|
| "Anthropic 250 篇毒倒任意 AI" | 仅 DoS 乱码后门，作者自注不太可能威胁前沿模型；不能改事实/绕护栏 | F |
| "PoisonedRAG 90% = 生产可投毒" | 玩具数据集 + 已知 query + 无防御上界；真实检索显著衰减（CorruptRAG/POISONCRAFT） | P |
| "Pravda 影响 33% = 投毒导致 33%" | NewsGuard 测的是复述频率，Harvard 复现主流查询仅 5%；归因跳跃 | P |
| "GEO 系统让 AI 推荐你" | 60-80% 成功率（从业者自述）+ 需连续投喂 + 客户竞对同时投放相互抵消 | P |
| "中文 LLM 已被大规模投毒" | 唯一硬证据是 DeepSeek 复述（掺官方叙事偏好混淆）；协同灌站改国产 LLM 无确证个案 | N |

---

## 5. 防御与检测

### 5.1 五大检测信号清单 + 可观测指标（每条带已知盲区）

| 信号 | 可观测指标 | 已知盲区 | 对接 N 类需求 |
|------|-----------|---------|--------------|
| **(1) 困惑度/流畅度异常** | chunk 级 PPL 离群 | confirmed 失效——GASLITE/CorruptRAG 流畅度保持攻击使简单过滤检出仅 31-34% | — |
| **(2) 来源可信度评分** | 第三方 truth score + C2PA 文本 manifest | 依赖权威库覆盖度 | N3 |
| **(3) 跨 LLM/跨平台答案一致性** | 同 query × 6 平台 Jaccard+编辑距离+NLI 分歧度 | **load-bearing 盲区：系统性投毒会一致输出同一错误，自一致性判其"高一致=非幻觉"** | N3/N2/N4 |
| **(4) 突发新源涌现** | 引用域名突变 + top-k 新源占比突增 + 历史快照残留 | data void 误判为 active poisoning | N2/N4 |
| **(5) 引用源溯源** | AI 答案事实回链原始独立数据源 | AI 答案动态合成无 URL 锚点 | N3 |

**最大误报源**〔**F**〕：**把 data void 误判为 active poisoning**。"AI 引用了坏源"≠"被投毒攻击成功"，可能只是冷门 query 无优质源可用。中文场景的 data void 误报率是产品化前必须量化的参数（§8 空白）。

**SelfCheckGPT 盲区是 load-bearing 反话术**〔**P**〕：它检测的是"不一致"而非"不正确"。若训练数据已系统性中毒，多次采样会一致输出同一错误，自一致性检测判其"非幻觉"——故**"跨 LLM 答案一致"不能反推"未被投毒"**，必须叠加跨平台分歧 + 外部权威源回链。

### 5.2 与 anti-geo-monitoring 的 N2/N3/N4 对接

本研究恰好补上 [`anti-geo-monitoring-cn.md`](../techniques/anti-geo-monitoring-cn.md) 缺失的**技术信号层**（原卡强在商业/需求框架，弱在可证伪检测细节）：

- **N2 竞品攻击监测** ← 信号(3)跨平台分歧 + (4)突发新源涌现 + 情感突变时序。中文 GEO 灰产已 confirmed 支持"反向抹黑竞品"（[证券时报](https://www.stcn.com/article/detail/3681991.html)），这是 N2 的一手锚点。
- **N3 AI 幻觉监测** ← 信号(2)可信度评分 + (3)一致性 + (5)溯源。**YMYL 主战场**（医疗疫苗有害论投毒 / 金融伪造投资关系）。
- **N4 AI 舆情扩散** ← 信号(3)+(4)+ 社媒负面声量与 AI 答案负面化时序相关。
- **核心挂钩结论**〔**N**〕：**监测有效性独立于攻击有效性**——投毒越是"难证伪/难防/平台沉默"，知情成本越高，第三方独立监测 + 合规留痕价值越大。这绕开进攻型 GEO 致命的"反事实不可验证"，与 anti-geo 元假说 A/F 完全一致。

### 5.3 YMYL 合规角度

中文已形成"监测刚需"政策栈（不依赖市场教育的合规驱动需求）：

- 网信办《AI 生成合成内容标识办法》（2025-09-01 施行）——显式 + 隐式标识，为"引用源溯源/provenance 检测"提供合规抓手 [CAC](https://www.cac.gov.cn/2025-09/04/c_1758702660093959.htm)
- 信通院《GEO 服务可信基本要求》评测（2026-03 启动）——把"关键词堆砌/语料轰炸/伪造权威信源"定性为污染；实测确证"特定论坛连续发布百余条虚假信息后主流大模型置信度从百分之十几快速飙升" [瞭望/新华](https://finance.sina.com.cn/jjxw/2025-05-30/doc-inezznzx0000000.shtml)
- 强制性国标（GB/T 45654-2025 等）：语料违法不良信息 >5% 不应使用 / 拒答率 ≥95% / 生成内容合格率 ≥90% / 来源审核+记录。叠加备案制（截至 2026-02 累计 796 款）

**中文 C 端投毒的前提比英文/企业 RAG 更苛刻**〔**P**〕：GEO 话术暗示"发软文→改中文大模型公开回答"，但这要穿透[国标语料审核 + 联网白名单 + 拒答层 + 检索重排]四道关，与"攻击者直接向企业自建 RAG 写文档"（EchoLeak/Copilot 案例的作用域，**有真实复现**）完全不同——后者有证据，前者公开证据链缺失。

---

## 6. 与本仓库的关系

### 6.1 是否升级为技术卡？——暂缓，先存草稿（本文件）

对照 [`dimension-map-cn.md`](../techniques/dimension-map-cn.md) 第 IX 节"不应建新卡"五条，本主题**结构上够格**（≥ 4 条元假说 / 与现有卡 < 70% 重叠 / 跨 6 平台跨 3 层 / 落 DS 维度）。但 [`2026-05-04 审计`](./2026-05-04_meta-hypothesis-audit.md) 已警告勿再"概念叠卡"，仓库当前瓶颈是实证而非结构。**决策：暂存草稿，待 E\*（§7 #1）产出第一手数据后再决定是否升为 `techniques/poisoning-attack-surface-cn.md`（maturity: concept / confidence: low）。**

### 6.2 与四张卡的引用对接

| 卡 | 对接关系 |
|----|---------|
| [`anti-geo-monitoring-cn`](../techniques/anti-geo-monitoring-cn.md) | 本草稿补其**技术信号层**（原卡缺）。N2/N3/N4 ← §5.1 五大检测信号；"监测独立于攻击"与其元假说 A/F 同源互证 |
| [`knowledge-graph-cn`](../techniques/knowledge-graph-cn.md) | 本草稿层 3 KG 抽取投毒 ← 其"训练/RAG/KG 三条传导路径"；其强假说 E"维基中文不可优化硬基线"= frontrunning 中文对应物 |
| [`private-vs-public-source-cn`](../techniques/private-vs-public-source-cn.md) | §2.3"跨平台 GEO 资产不互通"= 其元假说 B"公众号矩阵仅元宝成立"的攻击面版本；"读取封闭≠写入封闭"是其公开度光谱的攻防延伸 |
| [`citation-attribution-styles-cn`](../techniques/citation-attribution-styles-cn.md) | "投毒可观测性"分级（DeepSeek `[citation:X]` 最透明）直接用其引用归因 4 维分解；CTR<1% 限制了"投毒导流"实际价值 |

### 6.3 CONTRIBUTING.md "不给黑帽手册"红线的合规处理

本草稿**触及但不越线**：(1) 全文威胁建模 / 防御导向，只引用公开发表的受控研究 + 负责任披露；(2) cloaking / SEO poisoning 部分只描述机制与防御方向，不提供实施细节；(3) E\* 实验只在自建沙盒，测的是检测信号有效性；(4) 与 CONTRIBUTING "如何被识别可以，操作手册不行"完全对齐——重心在**如何被识别 / 如何防御**。

---

## 7. 衍生 BACKLOG 建议

1. ⭐⭐⭐ **`exp-cn-rag-poisoning-datavoid-sandbox`**（= §3.3 E\*）：自建 RAG 沙盒验证 data void 决定论 + 防御衰减曲线 + 自然文本隐蔽性。¥0 现金，补"生产级防御开启后 ASR 衰减多少"端到端量化空白。**与第一个实验 selector pilot 不冲突，可并行**。
2. ⭐⭐⭐ **`exp-cn-datavoid-vs-active-poisoning-detection`**：量化五大检测信号在中文语料上的误报率/漏报率基线，**重点测"data void 误判为 active poisoning"的中文误报率**——anti-geo 产品化前必须参数。
3. ⭐⭐ **`tech-cn-poisoning-takedown-timeline`**：3·15 后各平台 takedown / 防御响应时间序列纵向追踪——填"持久性"维度数据空白，同时复核清朗专项是运动式还是制度化。
4. ⭐⭐ **`tech-cn-cross-model-transfer-poisoning`**：正面交锋 TabooRAG 式"一份毒内容打通多中文引擎"——若成立则动摇 §2.3 核心判决（见 §9 缺口 #1）。
5. ⭐ **`tech-cn-cseo-bench-replication`**：C-SEO Bench 中文复现（测豆包/DeepSeek/文心，覆盖对抗性投毒，非仅内容编辑型）。
6. ⭐ **`tech-cn-content-farm-rag-hit-rate`**：中文内容农场被国产模型 RAG 检索命中的占比/重复率/模板化特征。

---

## 8. 公开数据空白 / 待解未知

| # | 空白 | 为何关键 |
|---|------|---------|
| 1 | 中文 C 端 LLM 被 RAG 投毒改正常品牌 query 输出的独立大样本复现 | 所有效果证据要么灰产自述要么厂商营销，无中立第三方受控数据 |
| 2 | "生产级防御开启后 ASR 衰减多少"端到端曲线 | PoisonedRAG 报无防御 ASR，RobustRAG 报防御鲁棒性，二者很少同实验对打 |
| 3 | data void 误判为 active poisoning 的中文误报率 | 检测产品化前必须量化，否则 N3 监测全是误报 |
| 4 | 六大平台联网模式默认开/关 + 检索源白名单 + 权威源加权工程配置 | 决定层 2 实际可达性，属各厂未公开内参 |
| 5 | 中文 data void"高频 vs 冷门 query"对照 | Harvard 结论基于英文 Pravda，中文是否同样"主流免疫长尾易中"未验证 |
| 6 | 3·15 后平台 takedown 时间序列 | "被打掉概率"与"持久性"只有定性描述无数据 |
| 7 | 国标审核栈真实执行强度 | 拒答率 ≥95% 是评估门槛≠线上真实拒答率 |
| 8 | 中文 retriever/embedding（bge-zh 等）对抗鲁棒性 | 所有检索投毒数字来自英文 retriever，迁移性未验证（见 §9 缺口 #7） |
| 9 | KG 三元组投毒 → 依赖该 KG 的 LLM 问答输出错误的端到端传导 | KGE 投毒只证明 link prediction 被操纵，完整链路缺测量 |
| 10 | 清朗专项实际执行效果与持久性 | 决定"投毒窗口收窄"是短期反弹还是长期结论，需 2026 Q3-Q4 复核 |

---

## 9. 对抗性核验留痕（steelman 缺口 + 核验裁决摘要）

> 本节是本草稿的**自我证伪记录**。原始调研经 1 路独立对抗性核验，13 条关键引用裁决为 supported 9 / partial 4（4 处已在"校正说明"修正）。以下 7 个 steelman 缺口是核验指出"底稿遗漏但对全流程分析重要"的角度，**列为后续优先补强方向**：

1. **跨模型迁移性攻击（最重要反向锚点）**：TabooRAG 等声称"一份毒内容跨 GPT-5.2 / DeepSeek-V3.2 / Qwen-3 高迁移"，与 §2.3"跨平台不互通"直接冲突。若迁移性在中文成立，会动摇核心判决——必须正面交锋（→ BACKLOG #4）。
2. **时间一致性/新鲜度攻击面**：高时效查询（突发事件/最新政策）语料稀疏期是 data void 的动态特例，"抢发首条权威内容"（frontrunning 的 RAG 检索版）在中文热点场景值得单独建模。
3. **多模态投毒载体**：豆包（视频字幕/封面 OCR/口播文案）、元宝视频号被一句带过。中文短视频生态的 ASR/OCR 提取链路是英文 awesome list 空白，也是中文差异化最强攻击面之一。
4. **防御侧"平台已部署什么"的被动观测探针**：平台 RAG 配置是黑箱，可设计用户侧被动探针（对照注入自建可索引源 + 跨平台引用差分）反推白名单/去重/权威加权——比纯沙盒 E\* 更能填平台黑箱（可作为"第一个实验"延伸）。
5. **法律责任/取证链**：YMYL 段引了"平台过错推定审核义务"，但未展开"被投毒受害品牌的取证-溯源-维权"全流程（历史快照固证、公证、不正当竞争诉讼）——是 anti-geo 监测"合规留痕"价值的落地闭环。
6. **攻击经济学/ROI 供给侧动态**：有成本数字但未建模"清朗封号后黑产迁移成本"与"多 actor 竞争自我稀释"的均衡。C-SEO Bench 的"congested zero-sum"若在中文黑产成立，意味投毒市场会自我塌缩——这比单次攻击成功率更能预测"窗口收窄"。
7. **中文 retriever/embedding 特异性**：所有检索投毒数字来自英文 retriever（Contriever/BEIR）。中文分词、bge-zh 对抗鲁棒性、困惑度过滤在中文的检出率是否与英文（约 30% 逃逸）相近——是"英文 PoC 能否迁移中文"判决的技术核心（→ §8 空白 #8）。

---

**变更记录**

- 2026-05-30：研究草稿初版。综合 6 路并行投毒攻击研究（对抗性 AI 安全技术分类 / 公开案例梳理 / 三层传导路径 × 平台可行性 / 六平台攻击面映射 / 红队怀疑者反证 / 防御检测内核）+ 1 路对抗性核验。写入前应用核验抓到的 8 处引用/事实修正（见"校正说明"）。核心判决：投毒在中文 GEO 是"已确证可发生但效果上限存疑"，层 2 RAG 检索期是唯一现实攻击面，生效依赖 data void，监管窗口收窄。存于 `audits/` 暂不升级技术卡，待 E\* 产出第一手数据再定。
