# 项目当前进度

> 最后更新：2026-05-03（含 2026-05-02 完整产出 + 2026-05-03 文档同步、首次 git 初始化、服务商话术拆解卡 #1、**仓库第一张需求侧卡 + 会议纪要**）
> 此文件用于跨会话快速恢复上下文。读完这一页 + [`BACKLOG.md`](./BACKLOG.md) + [`techniques/dimension-map-cn.md`](./techniques/dimension-map-cn.md) 就能接着干。

## 已完成（截至 2026-05-02）

### 1. 仓库骨架 ✅
- [`README.md`](./README.md) / [`CONTRIBUTING.md`](./CONTRIBUTING.md) / [`BACKLOG.md`](./BACKLOG.md)
- 4 个 markdown 模板（[`templates/`](./templates/)）
- 4 个 issue 模板（[`.github/ISSUE_TEMPLATE/`](./.github/ISSUE_TEMPLATE/)）
- [`glossary/terms.md`](./glossary/terms.md) 术语表 + slug 规范

### 2. 平台卡片 ✅（5 个生成式引擎 + 1 内容平台 + 1 传统搜索 = 7 平台）

| 平台 | 卡片 | 关键观点 |
|------|------|----------|
| 豆包（字节） | [`platforms/doubao/`](./platforms/doubao/) | 字节生态优先（头条 60%+ 假说） |
| DeepSeek | [`platforms/deepseek/`](./platforms/deepseek/) | 开源 + 第三方接入 + 三类研究边界 A/B/C |
| 文心（百度） | [`platforms/wenxin/`](./platforms/wenxin/) | 百度生态最深 + 5 入口边界 A-E |
| 千问（阿里） | [`platforms/qianwen/`](./platforms/qianwen/) | 电商绑定 + AI 下单 + Qwen 开源/闭源双轨 |
| 元宝（腾讯） | [`platforms/yuanbao/`](./platforms/yuanbao/) | 微信公众号 36 亿文章 + 多模型路由 + 7 入口 |
| 小红书 | [`platforms/xiaohongshu/`](./platforms/xiaohongshu/) | SEO/GEO 双重角色 |
| 百度 | [`platforms/baidu/`](./platforms/baidu/) | 唯一有官方算法文档的平台 |

### 3. 理论基础 ✅
- [`techniques/princeton-9-strategies-cn.md`](./techniques/princeton-9-strategies-cn.md) — Princeton 9 策略 + 4 个中文场景元假说（A-D，B 最重要）
- [`techniques/llms-txt-cn-practice.md`](./techniques/llms-txt-cn-practice.md) — llms.txt 中文采纳现状（6 家中文 LLM 的"已知 vs 未知"矩阵 + 4 条元假说 + 3 个实验设计；强假说 A：中文 LLM 全部不尊重 llms.txt）
- [`techniques/eeat-cn.md`](./techniques/eeat-cn.md) — 中文 E-E-A-T 类比信号跨平台横向对照（澄清两个误解：E-E-A-T 不是排名信号、中文场景是术语借用；5 平台搜索 + 6 平台 LLM 映射 + 5 条元假说；强假说 B：中文 LLM 不复用底层搜索的 E-E-A-T，直接用自家生态作为权威性代理）
- [`techniques/account-grade-systems-cn.md`](./techniques/account-grade-systems-cn.md) — 中文"号"主体绑定 + 账号等级体系横向对照（10+ 平台 L1/L2/L3 三层结构 + 5 条元假说 + 3 个实验设计；强假说 D：L3 数字等级对外部 LLM 引用几乎无效，是 [`eeat-cn.md`](./techniques/eeat-cn.md) 元假说 E 的展开）
- [`techniques/icp-and-subject-cn.md`](./techniques/icp-and-subject-cn.md) — ICP 备案 + 行业资质 + 平台主体认证三套体系横向对照（拆开三层 + 因果链 5 段拆解 + 5 条元假说 + 3 个实验设计；是 [`account-grade-systems-cn.md`](./techniques/account-grade-systems-cn.md) L1 主体合规层的深挖）
- [`techniques/structured-data-cn-practice.md`](./techniques/structured-data-cn-practice.md) — Schema.org / JSON-LD 在中文场景的采纳现状（4 组关系拆解 + 4 搜索引擎 × 6 LLM 支持矩阵 + Google 场景外推的 4 处失效 + 5 条元假说 + 3 个实验设计；强假说 B：schema 对中文 LLM 引用率边际效应接近 0）
- [`techniques/knowledge-graph-cn.md`](./techniques/knowledge-graph-cn.md) — 中文知识图谱与百科生态横向对照（区分 KG 与百科 + 6+ 大百科生态 + 训练 / RAG / KG 抽取三条传导路径 + 5 条元假说 + 3 个实验设计；强假说 E：维基中文"看得见够不着"，是 GEO 不可优化的硬基线）
- [`techniques/prompt-level-seo-cn.md`](./techniques/prompt-level-seo-cn.md) — Prompt-level SEO 中文场景适用性（**用户输入侧**角度，与前 7 张内容供给侧对照 + 中英 prompt 结构差异 + 各 LLM tokenizer 公开度对照 + 5 条元假说 + 3 个实验设计；强假说 E：tokenizer 优化是伪需求）
- [`techniques/multimodal-cn.md`](./techniques/multimodal-cn.md) — 多模态信源（图片 / 视频 / 音频 / PDF）在中文 LLM 中的采纳（**内容形态维度**，补全前 8 张文本中心默认 + 输入能力 vs 召回能力两套维度区分 + 6 大 LLM 对照 + 5 条元假说 + 3 个实验设计；强假说 D：图里文字 > alt 标签是中文场景反直觉的实操结论）
- [`techniques/citation-attribution-styles-cn.md`](./techniques/citation-attribution-styles-cn.md) — 中文 LLM 引用归因形态横向对照（**LLM 输出维度**，4 维分解 + 6 大中文 LLM × 英文对照基线 + 信号价值 vs 回流价值两层模型 + 5 条元假说 + 3 个实验设计；强假说 A：中文 LLM 引用源 CTR < 1%——直接挑战"被 AI 引用 = AI 流量"话术）
- [`techniques/private-vs-public-source-cn.md`](./techniques/private-vs-public-source-cn.md) — 中文私域 vs 公域信源光谱（**信源属性维度**，5 档公开度 L1-L5 + 各信源平台横向对照 + 三条传导路径 + 5 条元假说 + 3 个实验设计；强假说 B：公众号矩阵仅在元宝 / 微信搜一搜成立——直接打脸"公众号矩阵覆盖所有 AI"话术）
- [`techniques/platform-search-blockade-cn.md`](./techniques/platform-search-blockade-cn.md) — 中文平台间搜索 / 跳转 / 收录的相互封锁（**结构因果维度**，封锁 C1-C5 五类拆解 + 2008-2026 时间线 + 当前状态矩阵 + 信源池子池切割对中文 LLM 的结构后果 + 5 条元假说 + 3 个实验设计；强假说 C：互联互通政策对 LLM 引用率影响接近 0——指明"互联互通后单点覆盖"是政策误读）
- [`techniques/overseas-cn-deployment.md`](./techniques/overseas-cn-deployment.md) — 境外品牌进入中文 GEO 的部署路径（**主体决策维度**，5 种路径 A-E 横向对照 + 主体侧 / 内容侧两个独立维度 + 行业差异矩阵 + 5 条元假说 + 3 个实验设计；强假说 D：70% 隐性成本在内容审查不在技术部署——直接打脸"建站 + 翻译 = 中文 GEO"话术）
- [`techniques/geo-roi-framework-cn.md`](./techniques/geo-roi-framework-cn.md) — 中文 GEO ROI 评估框架（**反话术总论**，前 13 张技术卡元假说收敛 + 投入 3 类 / 产出 3 类拆解 + 按主体类型 / 行业差异化 ROI + 投入优先级排序含"不建议"清单 + 5 条元假说 + 3 个实验设计；强假说 C：机会成本是最常被隐藏项——指明"做 GEO"不是普世建议而是特定主体 + 特定行业的选择）
- [`techniques/dimension-map-cn.md`](./techniques/dimension-map-cn.md) — **技术主题卡片维度索引地图（元卡）**，把 14 张卡 × 8 维度显式化 + 卡间关系图 + 强假说集 + 服务商话术索引 + 主体决策索引 + 空缺维度 + 4 类读者的阅读路径 + 新卡扩展原则；in-validation 状态——结构稳定但元假说待实证

### 7.5 服务商话术拆解（新增 2026-05-03）✅

- [`docs/探词科技-产品手册0407.md`](./docs/探词科技-产品手册0407.md) —— 厂商 PDF 21 页 markdown 转录（视觉读取 + 人工逐页转录，未做语义改写）
- [`case-studies/wordtrace-vendor-pitch-decon-2026-05.md`](./case-studies/wordtrace-vendor-pitch-decon-2026-05.md) —— **GEO 服务商话术样本 #1** 拆解卡：12 条核心量化主张 × F/P/N 可证伪性分级 + 与仓库 14 张技术卡反话术对照 + 5 份"案例截图"复测可行性评估 + 3 条 micro-pilot 衍生进 BACKLOG。是仓库"反 GEO 服务商话术"基调的第一张实操卡。
- 衍生 BACKLOG 新小节"服务商话术验证 micro-pilot"3 条：[`exp-cn-vendor-pitch-self-reference-wordtrace`](./BACKLOG.md)（⭐⭐⭐ 与 selector pilot 兼容） / [`exp-cn-vendor-pitch-baiyun-tool-recommendation`](./BACKLOG.md) / [`exp-cn-vendor-pitch-yuanrun-pinot-noir`](./BACKLOG.md)

### 7.6 需求侧 + 供给侧两张新维度卡 + 讨论纪要（新增 2026-05-03）✅

- [`docs/meeting-2026-05-03-geo-demand-and-business-model.md`](./docs/meeting-2026-05-03-geo-demand-and-business-model.md) —— 会议纪要：探词业务技术反向工程 + 商业模式反推 + GEO 需求侧拆解 + 七层商业模式扫描 + 探词合理性 / 缺陷 / 结构性风险 + 7 个值得探索方向。
- [`techniques/geo-demand-side-fitness-cn.md`](./techniques/geo-demand-side-fitness-cn.md) —— **仓库第一张需求侧卡**（D0 需求侧前置维度，前置于 dimension-map-cn 现有 8 维度）：用户层 / 场景层 / 决策路径位置层三层拆解 + 用户类型 × 问题类型矩阵识别 GEO 真有效的 4 类窄场景 + 5 条元假说（含 ⭐⭐⭐ 强反话术 C "服务商客户画像越宽越说明销售在勉强匹配市场"）+ 2 个实验设计（E1 ⭐⭐⭐ 决策路径调研 / E2 ⭐⭐ B2B 选型 LLM 渗透率，均资金依赖）+ 衍生 BACKLOG 7 条。
- [`techniques/geo-business-model-taxonomy-cn.md`](./techniques/geo-business-model-taxonomy-cn.md) —— **仓库第一张供给侧卡**（DS 供给侧维度）：七层商业模式分类（数据 / 工具 / 内容 / 服务 / 平台 / 防御 / 标准）× 6 维度 + 投入产出结构 + 平台原生功能取代风险三个独立切片 + 6 条元假说（含 ⭐⭐⭐ 强反话术 A "LLM 平台一旦自建广告位 c/d 层中介模式整体被腰斩" 和 ⭐⭐⭐ C "反 GEO 监测是被严重低估的对称赛道"）+ 2 个实验设计（E1 ⭐⭐⭐ 平台广告位监控 / E2 ⭐⭐ 收入构成反推）+ 与服务商自我定位话术对照 + 衍生 BACKLOG 8 条。
- 仓库结构演进：14+1 → **16+1** 张技术卡（14 信号侧 + 1 元卡 + **新增 1 张需求侧前置卡 D0 + 1 张供给侧卡 DS**）。两卡 + [`geo-roi-framework-cn.md`](./techniques/geo-roi-framework-cn.md) 形成 **"需求 + 信号 + 模式 + ROI"** 四轴完整研究地图。
- [`techniques/dimension-map-cn.md`](./techniques/dimension-map-cn.md) **三轴升级**（376 → 487 行）：8 维度结构升级为 **D0（需求侧）+ D1-D8（信号侧）+ DS（供给侧）** 三轴，元假说总数 68 → **79**，强假说集 4.1 新增 5 条 ⭐⭐⭐ 反话术（D0 三条 + DS 两条），话术索引新增 ≥ 8 条，主体决策路径全部加 D0 前置 + 新增"GEO 服务商 / 创业者" 路径，空缺维度标记 2 项已填补 + 新增 3 项 DS 子空缺。

### 7.7 DS 维度首张子展开卡（新增 2026-05-03）✅

- [`techniques/anti-geo-monitoring-cn.md`](./techniques/anti-geo-monitoring-cn.md) —— **DS 元假说 C 的具体展开卡**：4 类反 GEO 监测需求拆解（N1 品牌可见度 / N2 竞品攻击 / N3 AI 幻觉 / N4 AI 舆情扩散）+ 客户决策人 / 预算来源 / 购买心理与进攻型对照 + 与传统舆情监测的技术差异 + 各 LLM 平台监测难度对照 + 7 条元假说（含 ⭐⭐⭐ 强反话术 A "需求规模与进攻型相当甚至更大"、⭐⭐⭐ C "技术门槛低于进攻型"）+ 3 个实验设计（E1 ⭐⭐⭐ 客户访谈 / E2 ⭐⭐ YMYL 幻觉率 / E3 ⭐⭐ 一致性指数）。
- 仓库结构演进：16+1 → **17+1** 张技术卡。dimension-map DS 维度从 1 张主卡 → 1 主卡 + 1 子卡。元假说总数 79 → **86**。

### 7.8 对外博客系列首发（新增 2026-05-03）✅

仓库新增 [`blog/`](./blog/) 目录，6 篇系列博客对外输出研究成果。要求：直白、不用隐喻、避免行业黑话。

- [`blog/README.md`](./blog/README.md) —— 系列索引 + 收录原则 + 阅读建议（按读者类型分路径）
- [`blog/01-拆服务商手册.md`](./blog/01-拆服务商手册.md) —— 拆一份 GEO 服务商产品手册（F/P/N 可证伪性框架）
- [`blog/02-谁用LLM找答案.md`](./blog/02-谁用LLM找答案.md) —— 什么人、什么场景，真的用 LLM 找答案（GEO 真实可寻址市场拆解）
- [`blog/03-七种生意模式.md`](./blog/03-七种生意模式.md) —— GEO 公司怎么赚钱（七种生意模式 + 客户价值 vs 模式合理性独立判断）
- [`blog/04-平台广告位风险.md`](./blog/04-平台广告位风险.md) —— GEO 行业最大的单一风险：LLM 平台自己卖广告位（c/d 层中介模式生命周期）
- [`blog/05-反GEO监测.md`](./blog/05-反GEO监测.md) —— 被严重低估的另一个生意：反 GEO 监测（公关 / 法务侧的空白赛道 + YMYL 监管驱动）
- [`blog/06-要不要做GEO.md`](./blog/06-要不要做GEO.md) —— 你公司要不要做 GEO（四关决策清单 + 不做 GEO 的明确名单）

合计 1059 行，约 14000 字。每篇末尾"延伸阅读"链接回仓库技术卡 / 案例 / docs。**仓库从研究资产首次跨入"对外可读内容输出"阶段**。

### 7.9 元假说审计（新增 2026-05-04）✅

- [`audits/2026-05-04_meta-hypothesis-audit.md`](./audits/2026-05-04_meta-hypothesis-audit.md) —— **仓库第一份反向审计报告**：基于 7 个反转事实（迈富时 02556.HK 港股上市 / PureblueAI 蓝色光标投资 / 智推时代 A 股投资 / 百分点参与 40 项国标 / 央企 137 万级招标 / 信通院起草标准 + CR5=62.3% / 平台变现非凤巢式）对 86 条元假说做系统性反向审计。判决分布 ✓ 28 / ◐ 17 / ✗ 9 / ? 32（30.2% 严格性合格）。识别 4 个隐含前提中 2 证伪（"草莽期"+"创业 SaaS 为主"）+ 1 部分证伪（"广告位最大单一风险"形态错——实际 4 形态：订阅 / 电商佣金 / 监测后台 / API）+ 1 部分证伪（"客户付费弱仅窄场景"——遗漏防御侧）。
- 已落地修订标注：[`techniques/geo-business-model-taxonomy-cn.md`](./techniques/geo-business-model-taxonomy-cn.md)（A ✗ / B ◐ / F ◐ / C/D 强化 ✓✓ / E ✓）+ [`techniques/geo-demand-side-fitness-cn.md`](./techniques/geo-demand-side-fitness-cn.md)（B ◐ / C ✗ / D ◐）+ [`techniques/dimension-map-cn.md`](./techniques/dimension-map-cn.md) 4.1 强假说集标注 2 条 🔄 已降级 + [`case-studies/wordtrace-vendor-pitch-decon-2026-05.md`](./case-studies/wordtrace-vendor-pitch-decon-2026-05.md) 顶部加 7 条反转事实补丁。**所有原文保留作认知演化痕迹**——P1 必改 8 项的正式重写在后续集中执行。
- **审计核心结论**：底座没崩，盖子歪了。D1-D8 信号侧 68 条假说在反转事实射程外，整体世界观成立；D0 + DS 18 条假说严重低估行业成熟度，被强化的 4 个判断（反 GEO 监测 / 标准协议层 / YMYL 监管驱动 / ROI 框架）是审计后剩下最坚固的部分。
- **DS 升级（2026-05-04 当天补完）**：[`techniques/geo-business-model-taxonomy-cn.md`](./techniques/geo-business-model-taxonomy-cn.md) 七层 → 八层结构升级——新增 h 层"横向扩展"（上市营销云加 GEO 模块 + 数据 / 政务公司加 GEO 模块 + 平台内部人创业 + 上市投资），承载迈富时 02556.HK / 百分点 / 蓝色光标系等画像。第 II 节标题 + 2.1 / 2.2 / 2.3 三表加 h 行 + 后续段落同步。h 层不独立成新元假说——分散落入 B / F 修订段。dimension-map 第 II 节 / III 节 / 8.5 节同步更新。
- **D0 升级（2026-05-04 当天补完）**：[`techniques/geo-demand-side-fitness-cn.md`](./techniques/geo-demand-side-fitness-cn.md) 元假说 B 从"4 类窄场景"升级为"5 类窄场景，分两条决策路径"。**这是 D0 卡的核心结构升级——把 GEO 需求模型从单维度"用户决策路径"扩为双维度"用户路径 + 品牌方采购动机"**。II 节 2.2 表加"品牌防御类需求" 5 行补表 + 结论段升级 + 2.3 表加"品牌防御维度的行业差异" 5 行补表 + 元假说 B 段加正式升级版扩展 + V 节话术对照新增 4 条。dimension-map 第 II 节 D0 行同步更新。
- **DS 元假说 A 升级（2026-05-04 当天补完）**：[`techniques/geo-business-model-taxonomy-cn.md`](./techniques/geo-business-model-taxonomy-cn.md) 元假说 A 从"广告位单一风险"升级为"4 形态平台变现冲击"——订阅制（消费侧绕过）/ 电商佣金（供给侧绕过）/ 自建品牌方监测后台 / API 收费（B2B 端绕过）。每形态独立给出机制 / 对 c/d 层冲击 / 当前已有信号 / 可证伪性 + 4 形态叠加效应表 + c/d 层剩余价值（非电商可路由场景 + 跨平台监测 + 垂直陪跑）+ 强反话术从 2 条扩为 6 条。BACKLOG 中 [`exp-cn-llm-platform-ad-slot-monitor`](./BACKLOG.md) 标 🔄 升级，新增 [`exp-cn-llm-platform-4-monetization-form-monitor`](./BACKLOG.md) 替代项。**这是 DS 卡的核心结构升级——把平台风险模型从单形态扩为 4 形态**。

### 7.10 DS 维度第 2 张子卡：GEO 行业分层（新增 2026-05-04）✅

- [`techniques/geo-industry-stratification-cn.md`](./techniques/geo-industry-stratification-cn.md) —— **DS 维度第 2 张子卡 / 仓库第 18 张技术卡**。承载审计报告（[`audits/2026-05-04_meta-hypothesis-audit.md`](./audits/2026-05-04_meta-hypothesis-audit.md)）核心结论"**分层成熟期**"——审计识别原前提"草莽期"被证伪后必须有正面卡片承载新画像。322 行，11 段标准结构。
- 核心内容：客观可观测谓词（上市 / 国标 / 大客户密度 / 千亿模型 / 上市公司投资 / 行业研究入选 / 高校课程纳入）拆三层 + 三层 × 6 维度对照（代表玩家 / 客户画像 / 决策人 / 客户价值 / 模式合理性 / 平台风险）+ CR5=62.3% 含义解读（成熟行业典型水位） + 5 条元假说（A 强反话术 ⭐⭐⭐ "CR5=62.3% 已是分层成熟期" / B 强假说"三层客户保有率数量级差异" / C 强假说"尾部 12-24 个月被并购或出清" / D "反话术基调精确化为反尾部 SEO 软文型话术" / E "分层判定可观测谓词成为仓库硬基线"）+ 3 个实验设计（E1 ⭐⭐⭐ 迈富时港股年报反工程，¥0 成本，仓库唯一 A 级公开数据源 / E2 ⭐⭐ 腰部纵向跟踪 / E3 ⭐ 尾部存活率跟踪）+ 7 条话术分层重判 + 衍生 BACKLOG 8 条。
- 仓库结构演进：17 张 → **18 张技术卡**，元假说总数 86 → **91**（+5）。dimension-map 第 II 节 DS 行 + 强假说集 4.1 + 变更记录同步更新。
- **这是审计后仓库结构的最重要补全**——把"分层成熟期"从修订标注转为正面卡片，形成与 [`anti-geo-monitoring-cn.md`](./techniques/anti-geo-monitoring-cn.md) 并列的 DS 维度第 2 张子卡。

### 7.11 E1 实验第一阶段：迈富时港股年报反工程（新增 2026-05-04）✅

- [`case-studies/mofusoft-tier1-reverse-engineering-2026-05.md`](./case-studies/mofusoft-tier1-reverse-engineering-2026-05.md) —— **仓库第一份基于 A 级公开数据源**的 GEO 行业 Tier 1 头部样本反工程（迈富时 02556.HK）。约 2 小时人力 / ¥0 现金（公开物料）。281 行。
- 6 个 A 级信源：东方财富 HKF10 + 迈富时 2024 业绩公告 PDF + 东吴证券海外公司深度研报 39 页 + 新浪财经 2026-03-26 转 2025 年报 + 同花顺 F10 + 格隆汇 Q3 公告。
- **核心数据**：2024 营收 15.6 亿（+26.5%）/ 2025 营收 28.2 亿（+80.8%）/ AI 应用业务 14.9 亿（+76.5%）/ 经调整净利润 1.5 亿（+91.3% 首次全年盈利）/ KA 客户翻倍 1,609 家（+105.5%）/ KA 客户 ACV +60.6% / 整体 NRR 96% / KA NRR 124%（净扩张）/ 总员工 1,737 人 / 计划 2025 内并购 ≥ 2 宗。
- **审计 brief 6 项数据的对照修正**：（1）21 万企业客户 → 实际 27,637 家（数量级偏差）；（2）世界 500 强 80+ 公开物料未明确（待 E1 第二阶段查）；（3）T-GEO™ 五层认知架构 → 实际是"AI-Agentforce 智能体中台" + "场景+数据+平台+模型" **四层架构**（名词记忆错位 + 层数偏差）；（4）Tforce 千亿参数大模型 → 财报未公开参数量；（5）首创 RaaS 退款保障 → 财报未提"RaaS"术语，实际是"按效果结算模式 + 健康留存"；（6）连续 7 年 IDC 中国营销云市占第一 → 实际"连续 6 年 AI SaaS 排行榜第一名"+"连续 5 年智能营销榜首"。**修正不影响 Tier 1 整体判断**——4 个 Tier 1 谓词中迈富时仍满足 4 个。
- **强化的仓库假说**（7 条）：[`geo-industry-stratification`](./techniques/geo-industry-stratification-cn.md) A/B/C 全部强化；[`geo-business-model-taxonomy`](./techniques/geo-business-model-taxonomy-cn.md) D/F + h 层强化；[`geo-roi-framework`](./techniques/geo-roi-framework-cn.md) D 强化。
- **与 wordtrace 卡（Tier 3）形成头部 vs 尾部对照组**——12 个维度对照表显示两个样本所有可观测谓词都呈系统性差异，验证分层卡画像区分。
- 仓库结构：**18 张技术卡 / 91 条元假说 / 2 张 case-study 卡（Tier 1 + Tier 3 完整对照组）**。剩余 E1 第二阶段约 6-13 小时人力（年报正文阅读 + 关联方交易 + 投资者关系记录 + 季报对照）。

### 7.14 会话总结 + 文档同步 + 记忆更新（新增 2026-05-04）✅

- [`audits/2026-05-04-session-summary.md`](./audits/2026-05-04-session-summary.md) —— **本次会话的跨会话恢复点**。涵盖 11 个 commit 时间线 / 4 个隐含前提的判决 / 三层完整对照组 / 4 形态 T0 基线 / 6 项审计 brief 数据修正 / 下一会话接续路径。
- 项目文档同步：[`STATUS.md`](./STATUS.md) 三大卡住点 + 下一步候选方向更新到 2026-05-04 状态 + [`README.md`](./README.md) / [`CLAUDE.md`](./CLAUDE.md) 文件总数 + 必读清单同步。
- 记忆系统升级（`/Users/liu/.claude/projects/-Users-liu-Projects-cn-seo-geo-atlas/memory/`）：
  - 升级 [`project_dimension_atlas_saturation.md`](memory) 从"14+1 卡饱和"到"18 卡 + 实证瓶颈阶段"
  - 新增 [`feedback_audit_baseline_refined.md`](memory)：仓库基调精确化为分层判定（反尾部 / 接受腰部 A 级 / 不反头部）
  - 新增 [`project_audit_2026_05_04_complete.md`](memory)：审计闭环 + 跨会话恢复入口
  - 更新 [`MEMORY.md`](memory) 索引
- **本次会话总结**：从审计触发到结构重建到实证启动的完整闭环——11 个 commit / 18 张技术卡 / 91 元假说 / 三层对照组 / 4 形态 T0。**这是仓库从"概念叠卡"阶段进入"实证瓶颈"阶段的拐点**。

### 7.13 4 形态平台变现监测系统启动（新增 2026-05-04）✅

- [`experiments/exp-cn-llm-platform-4-monetization-form-monitor.md`](./experiments/exp-cn-llm-platform-4-monetization-form-monitor.md) —— **DS 元假说 A 升级版"4 形态平台变现冲击"的实证基础设施**。273 行。建立 6 平台 × 4 形态 = 24 监测点的协议 + T0 基线 + 季度全面 / 月度告警 / 一次性事件三级响应机制。
- **T0 基线（2026-05-04）核心发现**：
  - 形态 1（订阅制 / 消费侧绕过）：**3/6 已上线**——豆包付费版 / 文心一言 49.9-59.9 元/月 / Kimi 探索版按 query 计费
  - 形态 2（电商佣金 / 供给侧绕过）：**至少 2/6 已链接**——豆包→抖音商店 / 千问→淘宝；ChatGPT Atlas→Shopify 海外对照
  - 形态 3（自建品牌方监测后台）：**0/6 上线**——是 4 形态中唯一在中文场景未发生的形态，**最高优先级监测点**。Google Search Console 类比预计 12-24 个月内中文 LLM 平台开始上线
  - 形态 4（API 收费 / B2B 端绕过）：**4-5/6 已商业化**——豆包 API 定价已公开（doubao-seed-2.0-pro 3.2/16 元每百万 tokens 输入/输出）。豆包是仓库唯一可获 A 级 API 定价数据
- **触发机制**：任一形态新平台上线 → 立即引发仓库 DS 元假说 A 升级版重审 + [`techniques/anti-geo-monitoring-cn.md`](./techniques/anti-geo-monitoring-cn.md) 元假说 G 升级（形态 3 直接对应）。
- 衍生 BACKLOG 6 条：4 形态演化纵向卡 / 订阅 ARR 追踪 / 电商抽佣率追踪 / 品牌方监测后台监控 / API 调用量追踪 / c/d 层收入影响实测。
- **预算**：自建监测 ¥0 / 4-6 小时初始搭建 / 1-2 小时月度维护。第一份季度报告窗口 2026-08。

### 7.12 Tier 2 腰部样本卡：智推时代（新增 2026-05-04）✅

- [`case-studies/zhitui-tier2-2026-05.md`](./case-studies/zhitui-tier2-2026-05.md) —— **仓库 Tier 2 腰部样本 #1 反工程**。约 2 小时人力 / ¥0 现金。278 行。
- 7 个信源：**4 A 级**（亿邦动力公司融资 PR + 同花顺转载 + 网易订阅投融湾团队报道含具体客户名单 + 东方财富转 21 世纪经济报道 2025 大湾区文化产业投资大会路演现场报道）+ **3 B 级**（智推时代官网 + 新浪财经 2026-03-13 合作媒体 + IT之家 2026 测评——典型 SEO 软文型物料）。
- **核心数据**：公司 2025-05 注册成立 / 创始人陈缪喆（连续创业者，上一项目 2019 被三七互娱并购）/ 2025-10-29 千万级种子轮（三七互娱 002555 领投 + 趣睡科技 301336 跟投）/ 2025-11-28 路演披露天使轮在进行 / 自研 GENO 系统 4 大模块 / 25+ AI 平台覆盖（豆包+DeepSeek+元宝占客户 95%）/ 9+ 公开客户（招行 / 广汽 / 广发证券 / 珀莱雅 / 豌豆思维 / 三七互娱 / 作业帮 / 小鹏 / 理想）/ 2026-02-11 入选艾瑞《2026 GEO 行业研究报告》/ 2025-09 进天津商业大学新工科课程。
- **关键发现 #1：F7 反转事实的直接出处**——创始人陈缪喆 2025-11-28 原话："国内只有 GEO，平台没开放商业化"+"豆包链接抖音商店"+"ChatGPT Atlas 跳蓝链 → Shopify"——是审计报告 F7 + DS 元假说 A 升级版"4 形态平台变现冲击"的直接源头。
- **关键发现 #2：Tier 2 画像 = A 级 + B 级二元混合**：A 级层（上市公司投资 + 艾瑞报告 + 高校课程 + 9+ 公开大客户案例 + 创始人持牌媒体采访）+ B 级层（精确小数点客户案例 / 行业覆盖数 31/39/30+ 版本不一致 / 时间口径"2025-05 注册"vs"2023 年最早实践"混用 / "国内最早" 不可证伪表述）。**仓库基调精确化**：在 Tier 2 画像下，"反 GEO 服务商话术"应理解为"**反 B 级 SEO 软文层，不反 A 级结构性背书层**"。
- **完整三层对照组**：12 维度对照表显示 Tier 1（迈富时） / Tier 2（智推时代） / Tier 3（探词）**所有可观测谓词呈系统性梯度差异**——证明分层卡 1.2 节客观谓词集有内在一致性。
- 仓库结构：**18 张技术卡 / 91 条元假说 / 3 张 case-study 卡（完整三层对照组）**。
- 衍生 BACKLOG 5 条：智推时代后续融资 / 并购跟踪 / Tier 2 公司"二元混合"方法学 / 客户独立核实 / GENO 系统开源验证 / Tier 2 不可证伪声称清单。

### 7. 项目级文档 ✅
- [`README.md`](./README.md) — 已更新到 2026-05-02 现状（14+1 张技术卡 / 8 维度 / 68 元假说 + dimension-map 入口指引 + 仓库特色"怀疑锚点 + 元假说 + 反话术对照"段）
- [`CLAUDE.md`](./CLAUDE.md) — **项目级 Claude Code 指引**（新建 2026-05-02）：项目定位 + 关键约束 + 写作风格 + 技术主题卡标准结构 + 不应建新卡的情况 + 用户偏好 + 三大卡住点速查
- [`CONTRIBUTING.md`](./CONTRIBUTING.md) — 已扩充技术主题卡的标准结构段（11 段强制约束）+ 不应建新卡的情况 + 写完一张卡后必须同步的文件清单

### 4. 资源索引 ✅
- [`resources/awesome-lists.md`](./resources/awesome-lists.md) — amplifying-ai / luka2chat / DavidHuji 等英文 awesome 清单
- [`resources/papers.md`](./resources/papers.md) — Princeton GEO / C-SEO Bench / AutoGEO / MAGEO / E-GEO 等论文

### 5. 实验方法学 ✅
- [`experiments/methodology.md`](./experiments/methodology.md) — 3 种实验类型 + 最小样本 + 反偏置 checklist + 中文场景特殊挑战
- [`experiments/query-set-v1.md`](./experiments/query-set-v1.md) — 80 query × 8 类（informational/decisional/factual/YMYL/technical/commercial/local/creative）
- [`experiments/exp-doubao-vs-deepseek-paired.md`](./experiments/exp-doubao-vs-deepseek-paired.md) — 第一个预注册实验设计（H1/H2 假设 + ≥20pp 阈值 + 320 次采集计划）
- [`experiments/exp-five-vendor-paired-queries.md`](./experiments/exp-five-vendor-paired-queries.md) — ⭐⭐ **仓库终极实证目标**实验设计（H1 生态偏好普遍性 + H2 DeepSeek 技术 + H3 千问电商；20/20/30pp 阈值 + 120 比较 Bonferroni；800 次采集；concept，依赖第一个实验先跑通）

### 6. 第一个实验工具栈 ✅（脚本就绪，未真实执行）

[`tools/exp-doubao-vs-deepseek-paired/`](./tools/exp-doubao-vs-deepseek-paired/)：

| 文件 | 职责 |
|------|------|
| `README.md` | 安装、运行、pilot、selector 修改位置 |
| `requirements.txt` | playwright / pyyaml / beautifulsoup4 / pandas / scipy / tldextract |
| `config.example.yaml` | 配置模板（含时段窗口、联网状态、失败处理） |
| `queries.yaml` | 32 个实验 query |
| `source_classifier.py` | URL → 信源类别归类规则 + 17 case 自测 |
| `doubao_adapter.py` | 豆包 Web 端适配器（**selector 标 `# TODO: pilot-verify`**） |
| `deepseek_adapter.py` | DeepSeek Web 端适配器（**selector 标 `# TODO: pilot-verify`**） |
| `collect.py` | 主采集（pilot 模式 / 时段标签 / 连续失败暂停 / JSON 落盘） |
| `score.py` | 评分（应用归类规则，输出长格式 CSV） |
| `analyze.py` | 统计（Wilson 95% CI / 卡方 / Fisher / H1+H2 自动判定） |

**预注册阈值已编码进 `analyze.py`**：`H1_DIFF_THRESHOLD_PP = 20` / `H1_WEAK_DIFF_PP = 5`，避免事后调整。

### 8. 投毒攻击研究草稿 + E\* 沙盒实验工具栈（新增 2026-05-30）✅

- [`audits/2026-05-30_poisoning-research.md`](./audits/2026-05-30_poisoning-research.md) —— **投毒攻击在中文 GEO 的威胁建模研究草稿**（防御导向）。源自 6 路并行调研 + 1 路对抗性核验。8 段正文 + F/P/N 标注 + "校正说明"（落盘前修正核验抓到的 8 处引用/事实错误：CPA-RAG / POISONCRAFT 的 arXiv ID 张冠李戴、C-SEO Bench 模型数、Harvard 数字等）+ §9 对抗性核验留痕（13 条引用裁决 supported 9 / partial 4 + 7 个 steelman 缺口）。核心判决：**投毒在中文 GEO 是"已确证可发生（3·15）但效果上限存疑"，层 2 RAG 检索期是唯一现实攻击面，生效依赖 data void，监管窗口收窄**。暂存草稿不升技术卡（审计已警告勿"概念叠卡"），待 E\* 产出第一手数据再定。
- [`experiments/exp-cn-rag-poisoning-datavoid-sandbox.md`](./experiments/exp-cn-rag-poisoning-datavoid-sandbox.md) —— **E\* 实验设计**：判决问题"data void 是不是中文 RAG 投毒成功的决定变量"。预注册 H1（虚构 vs 成熟 ASR 差 ≥30pp）/ H2（防御后降 ≥20pp）/ H3（自然文本绕困惑度 ≥30pp），阈值锁死在 analyze.py。伦理边界：**只在自建沙盒，零线上注入**。
- [`tools/exp-cn-rag-poisoning-datavoid-sandbox/`](./tools/exp-cn-rag-poisoning-datavoid-sandbox/) —— **13 文件可跑工具栈**：corpus_io / build_corpus / poison（沙盒投毒器，故意不实现 GASLITE/HotFlip）/ retriever（bge-zh 或 hash + KE/白名单/困惑度过滤三防御）/ rag_runner（mock/openai/hf）/ collect / score / analyze + README + ETHICS + config.example + queries（12 虚构 + 12 成熟）。
- **smoke test 已端到端验证通过**（python3.13）：build→poison→collect→score→analyze 全链路跑通，产出含 NOT-EVIDENCE 横幅的 results.md（H1 虚构 75% vs 成熟 0% 支持 / 两阶段诊断检索失败 vs 生成失败）。**smoke 逮到并修掉 3 个真 bug**：YAML 把 `off/on` 解析成布尔、`np.bool_` JSON 序列化崩、`clean_true` 跨 query 串源。
- **意义**：这是**仓库第一个不依赖用户账号、纯本地可跑的实验**——只需配本地 embedding（bge-zh）+ 本地/API LLM 即可产出第一手投毒有效性数据，**与卡了很久的"豆包 vs DeepSeek selector pilot"不冲突、可并行**。
- 仓库结构：18 张技术卡 / 91 元假说 / 3 case-study / **+1 audit 草稿 + 1 实验设计 + 1 工具栈（smoke 验证）**。

## 当前进行中 / 即将开始

**2026-05-03 文档同步**：项目级 [`CLAUDE.md`](./CLAUDE.md) 新建 + [`README.md`](./README.md) 改写到 14+1 卡现状 + [`CONTRIBUTING.md`](./CONTRIBUTING.md) 加技术主题卡的 11 段标准结构和"不应建新卡"约束 + auto memory 系统建立 3 条 feedback / project memory + 仓库首次 git init + commit。

**最近一次会话（2026-05-02）产出**：14 张跨平台技术主题卡片 + 1 张维度索引地图元卡 + 1 个⭐⭐终极实证目标实验设计文档。

- [`techniques/llms-txt-cn-practice.md`](./techniques/llms-txt-cn-practice.md) —— llms.txt 中文采纳现状
- [`experiments/exp-five-vendor-paired-queries.md`](./experiments/exp-five-vendor-paired-queries.md) —— 五大厂配对实验设计（concept，依赖第一个实验先跑通）
- [`techniques/eeat-cn.md`](./techniques/eeat-cn.md) —— 中文 E-E-A-T 跨平台横向对照
- [`techniques/account-grade-systems-cn.md`](./techniques/account-grade-systems-cn.md) —— "号"主体绑定 + 账号等级体系横向对照（接 E-E-A-T 元假说 E 衍生）
- [`techniques/icp-and-subject-cn.md`](./techniques/icp-and-subject-cn.md) —— ICP 备案 + 行业资质 + 平台主体认证三套体系（接 account-grade L1 层深挖）
- [`techniques/structured-data-cn-practice.md`](./techniques/structured-data-cn-practice.md) —— Schema.org / JSON-LD 在中文场景的采纳现状（与"中文场景独有信号"系列形成对照，转向"通用 Web 标准的中文采纳"角度）
- [`techniques/knowledge-graph-cn.md`](./techniques/knowledge-graph-cn.md) —— 知识图谱与百科生态横向对照（接 schema-data 元假说，转向"信源载体"维度）
- [`techniques/prompt-level-seo-cn.md`](./techniques/prompt-level-seo-cn.md) —— Prompt-level SEO 中文场景适用性（**首张用户输入侧**视角，与前 7 张内容供给侧形成 V 字结构）
- [`techniques/multimodal-cn.md`](./techniques/multimodal-cn.md) —— 多模态信源在中文 LLM 中的采纳（**内容形态维度**补全文本中心盲区，输入能力 vs 召回能力两套维度区分）
- [`techniques/citation-attribution-styles-cn.md`](./techniques/citation-attribution-styles-cn.md) —— 中文 LLM 引用归因形态横向对照（**LLM 输出维度**，信号价值 vs 回流价值两层模型直接挑战"被 AI 引用 = AI 流量"话术）
- [`techniques/private-vs-public-source-cn.md`](./techniques/private-vs-public-source-cn.md) —— 中文私域 vs 公域信源光谱（**信源属性维度**，5 档公开度 L1-L5 直接打脸"公众号矩阵覆盖所有 AI"话术）
- [`techniques/platform-search-blockade-cn.md`](./techniques/platform-search-blockade-cn.md) —— 中文平台间搜索 / 跳转 / 收录的相互封锁（**结构因果维度**，2008-2026 时间线 + C1-C5 封锁拆解 + 信源池子池切割对中文 LLM 的结构后果）
- [`techniques/overseas-cn-deployment.md`](./techniques/overseas-cn-deployment.md) —— 境外品牌进入中文 GEO 的部署路径（**主体决策维度**，5 种路径 A-E 横向对照，把前 12 张技术维度落到出海品牌的具体决策上）
- [`techniques/geo-roi-framework-cn.md`](./techniques/geo-roi-framework-cn.md) —— 中文 GEO ROI 评估框架（**反话术总论维度**，前 13 张技术卡的元假说收敛为 ROI 决策框架）
- [`techniques/dimension-map-cn.md`](./techniques/dimension-map-cn.md) —— 技术主题卡片维度索引地图（**元卡**，14 卡 × 8 维度显式化 + 卡间关系图 + 强假说集 + 4 类索引）

**仓库三大卡住点（2026-05-04 更新）**：

1. **第一个实验未跑过**：[`tools/exp-doubao-vs-deepseek-paired/`](./tools/exp-doubao-vs-deepseek-paired/) 工具栈就绪，selector 标 `# TODO: pilot-verify`，等待人工 pilot——**仓库当前唯一硬瓶颈**
2. **服务商话术验证 micro-pilot 未跑过**：[`exp-cn-vendor-pitch-self-reference-wordtrace`](./BACKLOG.md) 与 selector pilot 高度兼容（5 平台共用），适合作为 #1 的入门题。仍需用户人工 + 账号
3. **大量元假说未实证**：18 张技术主题卡共 91 条元假说——审计后判决 ✓28 / ◐17 / ✗9 / ?32，但 ✓/◐/✗ 大多基于反转事实 + Tier 1/2/3 case-study 数据的逻辑外推，未经过 pilot 实证

**审计后仓库结构**（2026-05-04 完成）：

- ✅ 元假说审计闭环（[`audits/2026-05-04_meta-hypothesis-audit.md`](./audits/2026-05-04_meta-hypothesis-audit.md)）
- ✅ DS 七层 → 八层（h 层"横向扩展"）
- ✅ D0 元假说 B 4 类 → 5 类窄场景（加品牌防御维度）
- ✅ DS 元假说 A 单形态 → 4 形态（订阅 / 电商佣金 / 监测后台 / API）
- ✅ 三层完整对照组（[`mofusoft Tier 1`](./case-studies/mofusoft-tier1-reverse-engineering-2026-05.md) + [`zhitui Tier 2`](./case-studies/zhitui-tier2-2026-05.md) + [`wordtrace Tier 3`](./case-studies/wordtrace-vendor-pitch-decon-2026-05.md)）
- ✅ 仓库基调精确化："反**尾部** SEO 软文型话术"，**不反** A 级结构性背书层
- ✅ 4 形态平台变现监测系统启动 + T0 基线（[`exp-cn-llm-platform-4-monetization-form-monitor`](./experiments/exp-cn-llm-platform-4-monetization-form-monitor.md)）

距离"产出第一个一手研究结论"还差：

1. **selector pilot 验证**（30-60 分钟）—— 需要真实账号 + 浏览器
2. **pilot run**（10 次采集）—— 端到端验证脚本
3. **主实验执行**（320 次采集 × 3 天）
4. **score + analyze**（30 分钟）
5. **回写结果**到 [`platforms/doubao/citation-mechanism.md`](./platforms/doubao/citation-mechanism.md) 假说一、[`platforms/deepseek/citation-mechanism.md`](./platforms/deepseek/citation-mechanism.md) 假说一/二、[`techniques/princeton-9-strategies-cn.md`](./techniques/princeton-9-strategies-cn.md) 元假说 B/D

> 上述 1-3 步只能由用户做（账号 + 网络环境）。Claude 可以协助 selector 调试、数据分析、回写。

## 下一步候选方向（按优先级，2026-05-04 更新）

仓库已从"概念叠卡"阶段进入"实证瓶颈"阶段——审计后认知重建已完成，**主要瓶颈是用户人工 pilot**。

### 用户人工依赖项（瓶颈，最高优先级）

1. **⭐⭐⭐ A0. 服务商话术验证 micro-pilot** —— [`exp-cn-vendor-pitch-self-reference-wordtrace`](./BACKLOG.md)："湖南哪家 GEO 公司好" × 5 平台 × ≥ 2 账号 × ≥ 2 时段 × ≥ 5 次。零账号成本、与 5 平台 selector pilot 高度兼容；做完直接为 A 项主实验铺路；同时回写探词案例卡的"复测结果"段
2. **⭐⭐⭐ A. 第一个实验 pilot** —— 仓库**最高优先级实证目标**；用户人工 + Claude 协助调 selector，产出第一份真实数据；selector 验证后端到端 pilot run（10 次）+ 主实验 320 次采集

### Claude 可独立推进项

3. **⭐⭐ E1 第二阶段：迈富时年报反工程深挖**（剩余 6-13 小时）—— 完整年报正文阅读 + 关联方交易 + 投资者关系记录 + 季报对照 + 销售物料 vs 财报披露的术语口径对照
4. **⭐⭐ B. 平台 changelog 系列起手** —— [`docs-doubao-changelog`](./BACKLOG.md) 建立 changelog 卡片模式，作为后续各平台 changelog 范本
5. **⭐⭐ Tier 2 第二样本：PureblueAI 清蓝**（前豆包平台市场负责人 + 蓝色光标系投资）—— 与智推时代形成 Tier 2 内部对照
6. **⭐ D. 工具评测占位** —— 国内 GEO 服务商（传声港 / 怪兽智能 / 传新社 / SheepGeo / Foglift）建 stub 卡片，按客观可观测谓词分层归类
7. **⭐ 平台 4 形态变现监测：第一份季度报告** —— 窗口 2026-08

### 大型基础设施项

8. **E. push 到 GitHub + BACKLOG → issue 转换** —— 仓库迁移到协作模式
9. **F. 设计第三个实验** —— 例如 [`exp-cn-ymyl-cross-platform-citation`](./BACKLOG.md)（验证 E-E-A-T 卡片元假说 C：YMYL 类全平台趋同）

## 关键约束 / 不要破坏的设计决定

- **frontmatter 字段固定**：`type` / `sources` / `confidence` / `verified` / `platforms` / `techniques` / `maturity`，见 [`CONTRIBUTING.md`](./CONTRIBUTING.md) 和模板
- **目录深度 ≤ 2**（`platforms/<slug>/<file>.md`）
- **平台不预先评判优劣**——卡片只描述机制，不做"哪个最好"
- **预注册阈值不能事后改**——任何统计判定（如 `H1_DIFF_THRESHOLD_PP`）一经写入实验设计就锁定
- **GEO 服务商话术一律对照 [C-SEO Bench](https://openreview.net/forum?id=oTeixD3oZO)（NeurIPS 2025）作交叉验证**——多数 GEO 方法在严格控制下基本无效
- **中文为主，技术术语保留英文**（GEO / E-E-A-T / RAG 等不强译）
- **不引入 package.json / CI / 静态站点生成**（README 末尾"未来可能的方向"明确这些不在当前轮次）
- **selector 准确性标注**：未真实验证的写 `# TODO: pilot-verify`，验证后改 `# verified YYYY-MM-DD`——禁止假交付

## 文件总数

101 个（含工具文件 + 1 个 .gitignore + 1 个项目级 [`CLAUDE.md`](./CLAUDE.md)；2026-05-03 累计 +13：服务商话术拆解 #1 + 厂商 PDF 转录 + 需求侧首张技术卡 + 会议纪要 + 供给侧首张技术卡 + DS 子展开卡反 GEO 监测 + 博客系列首发 6 篇 + 索引 README；**2026-05-04 +6**：元假说审计报告 + GEO 行业分层卡 + 迈富时港股年报反工程案例卡 + 智推时代 Tier 2 腰部样本卡 + 4 形态平台变现监测实验 + 会话总结；**2026-05-30 +14**：投毒攻击研究草稿 [`audits/2026-05-30_poisoning-research.md`](./audits/2026-05-30_poisoning-research.md) + E\* 实验设计 [`experiments/exp-cn-rag-poisoning-datavoid-sandbox.md`](./experiments/exp-cn-rag-poisoning-datavoid-sandbox.md) + 13 文件沙盒工具栈 [`tools/exp-cn-rag-poisoning-datavoid-sandbox/`](./tools/exp-cn-rag-poisoning-datavoid-sandbox/)，smoke test 已端到端验证；**2026-06-14 +1**：GEO 市场全景卡 [`techniques/geo-industry-market-landscape-cn.md`](./techniques/geo-industry-market-landscape-cn.md)——从 my-cognition 实地调研笔记迁入并脱敏，DS 子卡 #3 / 分层卡横向全景姊妹卡，仓库 18 → **19** 张技术卡、元假说 91 → **95**）

```
$ find . -type f \( -name "*.md" -o -name "*.py" -o -name "*.yaml" -o -name "*.txt" \) | grep -v __pycache__ | grep -v '/\.claude/' | wc -l
101
```
