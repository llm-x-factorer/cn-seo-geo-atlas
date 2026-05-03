# cn-seo-geo-atlas

> 中文互联网 SEO 与生成式引擎优化（GEO）的技术调研图谱。系统化追踪百度、小红书、豆包、Kimi 等平台的可见性优化机制，沉淀可复现的实验、可证伪的元假说、反 GEO 服务商话术的硬证据。

<!-- badges:start -->
<!-- 预留位：构建状态、条目数、最近更新、贡献者、Star。本轮不接入 CI，徽章后续补。 -->
<!-- badges:end -->

## 这是什么

一个**调研型 monorepo**——不是博客、不是工具集，而是把"中文搜索可见性"这件事的所有可观测面拆成可索引的卡片。每张卡片都带 frontmatter 元数据，便于后续脚本化、检索、做静态站点。

**当前状态（2026-05-02）**：

- 14 张跨平台**技术主题卡** + 1 张维度索引地图元卡，覆盖 **8 个独立维度**：内容供给侧 / 用户输入侧 / 内容形态侧 / LLM 输出侧 / 信源属性侧 / 结构因果侧 / 主体决策侧 / 反话术总论维度
- **68 条元假说**全部 `concept` 状态，等待数据回写
- 7 张平台卡片（豆包 / DeepSeek / 文心 / 千问 / 元宝 / 小红书 / 百度）
- 2 个预注册实验设计（豆包 vs DeepSeek 配对实验已就绪未跑；五大厂配对实验⭐⭐ 仓库终极实证目标）
- 第一个实验工具栈（11 个 Python/YAML 文件）就绪，selector 标 `# TODO: pilot-verify` 等待人工 pilot

读者画像：

- **决策者**（要不要做 GEO）：从 [`techniques/dimension-map-cn.md`](./techniques/dimension-map-cn.md) 第 V 节"按服务商话术反查表"切入
- **不同主体的实践者**：从 [`techniques/dimension-map-cn.md`](./techniques/dimension-map-cn.md) 第 VI 节"按主体决策索引"切入
- **完全新读者**：先读 [`techniques/dimension-map-cn.md`](./techniques/dimension-map-cn.md)，再选感兴趣的维度卡片
- **研究者**：关注每张卡的"实验设计建议"段 + [`STATUS.md`](./STATUS.md) 三大卡住点

30 秒判断要不要 star：如果你在意**百度之外的中文搜索面**（小红书站内搜索、微信搜一搜、抖音搜索），或者关心**生成式引擎引用机制**（豆包、Kimi、元宝、ChatGPT 中文 query），又**不愿被 GEO 服务商话术忽悠**，这里在长期积累一手卡片。

## 推荐入口：维度索引地图

> ⭐ **新读者强烈建议先读** [`techniques/dimension-map-cn.md`](./techniques/dimension-map-cn.md) ——它把 14 张技术卡的 8 维度图谱、卡间关系、强假说集、反话术索引一次性显式化。

| 入口 | 目的 |
|------|------|
| [`techniques/dimension-map-cn.md`](./techniques/dimension-map-cn.md) 第 V 节 | "听到 X 话术对吗"反查表（13 类常见话术 → 对应卡片 + 判定） |
| [`techniques/dimension-map-cn.md`](./techniques/dimension-map-cn.md) 第 VI 节 | "我是 X 主体类型"反查表（中小新品牌 / 中型 / 大型 / 出海 / YMYL / B2B / 本地生活） |
| [`techniques/dimension-map-cn.md`](./techniques/dimension-map-cn.md) 第 IV 节 | 强假说武器库（12 条 ⭐⭐⭐ 级别打脸高频话术的假说集合） |
| [`techniques/geo-roi-framework-cn.md`](./techniques/geo-roi-framework-cn.md) | GEO ROI 评估框架（投入 3 类 / 产出 3 类 / 计算 3 类常见错误 / 投入优先级排序） |
| [`STATUS.md`](./STATUS.md) | 跨会话快速恢复：已完成卡片 + 当前停在哪一步 + 下一步候选 |

## In-Scope

- **传统搜索**：百度、必应中文、神马、搜狗、360
- **内容平台站内搜索**：小红书、知乎、微信（搜一搜 / 公众号 / 视频号）、B 站、抖音、快手、微博
- **生成式引擎（GEO）**：豆包、Kimi、元宝、文心一言、通义千问、DeepSeek，以及 ChatGPT / Perplexity / Claude 在中文 query 下的行为
- **技术主题（已覆盖 8 维度）**：
  - **内容供给侧（7 张）**：Princeton 9 策略中文适配 / E-E-A-T 类比信号 / llms.txt 中文采纳 / Schema.org JSON-LD 中文采纳 / "号"主体绑定 + 账号等级 / ICP 备案 + 行业资质 / 知识图谱与百科生态
  - **用户输入侧（1 张）**：prompt-level SEO 中文场景适用性
  - **内容形态侧（1 张）**：多模态信源（图 / 视频 / 音频 / PDF）采纳
  - **LLM 输出侧（1 张）**：引用归因形态（行内 / 编号 / 卡片化）+ 信号价值 vs 回流价值两层模型
  - **信源属性侧（1 张）**：私域 vs 公域信源 5 档光谱
  - **结构因果侧（1 张）**：中文平台间搜索 / 跳转 / 收录封锁（C1-C5 五类 + 2008-2026 时间线）
  - **主体决策侧（1 张）**：境外品牌进入中文 GEO 的 5 种部署路径
  - **反话术总论维度（1 张）**：中文 GEO ROI 评估框架（按主体 / 行业差异化）
- **工具**：实验工具栈（playwright + pyyaml + scipy）、平台采集 adapter、信源分类器、统计分析
- **方法论**：可复现实验记录、预注册实验设计、反偏置 checklist、可信度评级

## Out-of-Scope

- 黑帽、刷量、刷排名、批量注册站群（不评测、不收录）
- "代写百度百科保 AI 引用"等灰产渠道 / 价格讨论
- 纯英文市场 SEO（除非作为对照）
- 广告投放（SEM / 信息流）的 ROI 优化
- 站点性能优化的通用知识（Core Web Vitals 这类有现成中文资料的不重复）
- "做 X 涨 N 倍"的服务商承诺类内容（本仓库立场是反向证伪）
- 任何会被简单等同为"AI SEO"的内容——本仓库**严格区分 SEO 与 GEO** 的优化对象、信号源和反馈回路

## 目录导航

| 路径 | 内容 |
|------|------|
| [`techniques/`](./techniques) | **核心**——14 张跨平台技术主题卡 + 1 张维度索引地图（[`dimension-map-cn.md`](./techniques/dimension-map-cn.md)） |
| [`platforms/`](./platforms) | 7 张按平台分的调研卡片（豆包、DeepSeek、文心、千问、元宝、小红书、百度） |
| [`experiments/`](./experiments) | 实验方法学 + query 集 v1 + 2 个预注册实验设计 |
| [`tools/`](./tools) | 实验工具栈（豆包 vs DeepSeek 配对实验：playwright + scipy 统计） |
| [`case-studies/`](./case-studies) | 实战案例复盘（占位，待填充） |
| [`resources/`](./resources) | 英文 awesome list 索引、论文清单 |
| [`glossary/`](./glossary) | 中英术语表（GEO 这种新词重点维护，新增 slug 走 PR） |
| [`templates/`](./templates) | 四类条目的 markdown 模板（带 frontmatter） |

## 仓库特色：怀疑锚点 + 元假说 + 反话术对照

每张技术主题卡都遵循**统一结构**（详见 [`techniques/dimension-map-cn.md`](./techniques/dimension-map-cn.md) 第 IX 节）：

1. **顶部 ≥ 3 条怀疑锚点**——含 [C-SEO Bench](https://openreview.net/forum?id=oTeixD3oZO)（NeurIPS 2025）这一仓库通用锚点
2. **≥ 4 条可证伪的元假说**——明确写出"如果 X 数据出现就证伪本假说"
3. **3 个实验设计建议**——⭐⭐⭐ 最高优先级、⭐⭐ 中、不建议做的实验
4. **与 GEO 服务商话术的对照表**——明确 ✅ / ⚠️ / ❌ 判定
5. **不做的事**——明确禁区，避免功能蔓延
6. **衍生 BACKLOG 建议**——让卡片成为"源头"而非"终点"

## 怎么贡献

详见 [`CONTRIBUTING.md`](./CONTRIBUTING.md)。每条条目至少要有：来源 URL、抓取日期、可信度评级、是否实测验证、关联平台、关联技术标签。

技术主题卡的写作约束（结构化反话术）见 [`CONTRIBUTING.md`](./CONTRIBUTING.md) 第三节。

issue 模板：
- [发现一个值得调研的源](./.github/ISSUE_TEMPLATE/new-source.md)
- [纠错](./.github/ISSUE_TEMPLATE/correction.md)
- [贡献一个 case](./.github/ISSUE_TEMPLATE/case-contribution.md)
- [调研 / 实验任务](./.github/ISSUE_TEMPLATE/research-task.md)

## 待办追踪

- 仓库尚未 push 到 GitHub 之前：所有待办进 [`BACKLOG.md`](./BACKLOG.md)（实验、平台调研、技术主题、工具评测、文档、元问题）
- push 之后：BACKLOG 批量转为 GitHub issue，本文件退役为 issue 列表的索引页
- **原则**：卡片正文不散落"待办"——卡片只承载知识，待办都汇集到 BACKLOG / issue 中

## 当前进度

跨会话快速恢复请读 [`STATUS.md`](./STATUS.md) —— 已完成的卡片、当前停在哪一步、下一步候选方向。

**仓库三大卡住点**（按优先级）：

1. **第一个实验未跑过**：[`tools/exp-doubao-vs-deepseek-paired/`](./tools/exp-doubao-vs-deepseek-paired/) 工具栈就绪，selector 标 `# TODO: pilot-verify`，等待人工 pilot
2. **五大厂实验未启动**：设计完成，依赖第一个实验跑通；需 3 个新 adapter（wenxin / qianwen / yuanbao）
3. **大量元假说未实证**：14 张技术卡共 68 条元假说全部 `concept`，需要数据回写

## 与已有英文资源的关系

英文 GEO/SEO 圈已经有相对成熟的开源资源（[amplifying-ai/awesome-generative-engine-optimization](https://github.com/amplifying-ai/awesome-generative-engine-optimization)、[luka2chat/awesome-geo](https://github.com/luka2chat/awesome-geo) 等），通用概念和工具栈不需要重复造轮子。**本仓库的差异化定位是中文场景**——豆包、千问、DeepSeek、文心、Kimi、元宝、小红书、知乎、微信、B 站、抖音这些平台在已有英文 awesome list 中**完全空白**。

具体怎么分工：

| 你的问题 | 去哪查 |
|----------|--------|
| 通用 GEO 概念 / 历史 / 定义 | 英文 awesome list（见 [`resources/awesome-lists.md`](./resources/awesome-lists.md)） |
| llms.txt / Schema / robots.txt 配置范例 | 英文 awesome list 的 Technical Docs 区 |
| ChatGPT / Perplexity / Gemini 的优化策略 | 英文 awesome list；本仓库只看中文 query 下的差异 |
| 学术论文起点 | [`resources/papers.md`](./resources/papers.md)（已挑选与中文场景相关的） |
| **国内 AI 平台、中文内容平台的 GEO/SEO** | **本仓库** |
| **反 GEO 服务商话术的硬证据** | **本仓库** + [C-SEO Bench](https://openreview.net/forum?id=oTeixD3oZO)（NeurIPS 2025） |

常驻怀疑锚点：NeurIPS 2025 的 C-SEO Bench 论文发现，在严格控制下**多数 GEO 方法基本无效**，传统 SEO 反而仍然有效。本仓库收录任何"做了 X 涨了 N 倍"类声明前，先用这条作交叉验证。

## 未来可能的方向（本轮不实现）

- 静态站点生成（基于 frontmatter 自动建索引、tag 页、平台聚合页）
- RAG 化：把所有卡片喂进向量库，做仓库内自然语言检索
- 自动化抓取流水线：定期扫描在线源，diff 出新增 / 失效条目
- 可见性看板：把 [`experiments/`](./experiments/) 里的可复现实验变成定期跑的监测任务

## 许可

调研内容遵循 CC BY 4.0，工具脚本如有则单独标注。
