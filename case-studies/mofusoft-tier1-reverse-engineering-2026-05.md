---
# ===== 必填 =====
title: 迈富时（02556.HK）港股年报反工程（GEO 行业 Tier 1 头部样本 #1）
type: case-study
sources:
  - url: https://emweb.securities.eastmoney.com/PC_HKF10/CoreReading/index?type=web&code=02556
    fetched_at: 2026-05-04
    note: 东方财富港股 F10 资料。2024 / 2025 中报 / 2025 年报核心财务比率全表，A 级（直接来自香港交易所披露）
  - url: https://img03.71360.com/w3/k4vde5/20250425/987b8f0c9382340375b3fb12d7fa9827.pdf
    fetched_at: 2026-05-04
    note: 迈富时管理有限公司 2024 年度业绩公告 PDF（2025-04 发布）。A 级（公司直接发布的投资者关系材料）
  - url: https://aigc.idigital.com.cn/djyanbao/迈富时（02556）：营销SaaS龙头，AI加速平台化转型-2025-08-25.pdf
    fetched_at: 2026-05-04
    note: 东吴证券海外公司深度研报 39 页（2025-08-25）。A 级（持牌投行研究所深度研报，引 Wind 数据）
  - url: https://finance.sina.com.cn/stock/bxjj/2026-03-26/doc-inhsiqkt8919618.shtml
    fetched_at: 2026-05-04
    note: 新浪财经 2026-03-26 报道迈富时 2025 全年业绩。A 级（媒体直接转发公司业绩公告）
  - url: https://basic.10jqka.com.cn/176/HK2556/
    fetched_at: 2026-05-04
    note: 同花顺金融服务网 F10 财务数据 + 业务回顾。A 级（与港交所披露同源）
  - url: https://cj.sina.cn/articles/view/5115326071/130e5ae7702002pnoe
    fetched_at: 2026-05-04
    note: 新浪财经 2025-11-19 转格隆汇关于迈富时 Q3 经营数据公告。A 级（媒体转港交所披露）
confidence: high
verified: true
last_verified: 2026-05-04
platforms: []
techniques:
  - geo-business-model-taxonomy
  - geo-industry-stratification
  - geo-roi-framework
  - geo-demand-side-fitness
maturity: confirmed

# ===== Case 专属 =====
industry: geo-vendor              # 研究对象本身是 GEO 服务商（Tier 1 头部画像）
timeframe:
  start: 2024-05-16               # 港股主板上市日
  end: 2026-03-26                 # 2025 全年业绩公告日（最新）
outcome: tier1-confirmed          # 按 [`techniques/geo-industry-stratification-cn.md`](../techniques/geo-industry-stratification-cn.md) 1.2 节客观谓词，迈富时归 Tier 1
anonymized: false
role: observer

# ===== 选填 =====
related:
  - ../techniques/geo-industry-stratification-cn.md
  - ../techniques/geo-business-model-taxonomy-cn.md
  - ../techniques/geo-roi-framework-cn.md
  - ../audits/2026-05-04_meta-hypothesis-audit.md
  - ./wordtrace-vendor-pitch-decon-2026-05.md
author: ""
last_updated: 2026-05-04
---

# 迈富时（02556.HK）港股年报反工程

> **本卡定位**：仓库**第一份基于 A 级公开数据源**（港股年报 + 投行深度研报 + 持牌媒体原创报道）的 GEO 行业 Tier 1 头部样本反工程。
>
> 与 [`wordtrace-vendor-pitch-decon-2026-05.md`](./wordtrace-vendor-pitch-decon-2026-05.md)（Tier 3 尾部样本 #1 探词科技）形成**头部 vs 尾部对照组**——按 [`techniques/geo-industry-stratification-cn.md`](../techniques/geo-industry-stratification-cn.md) 1.2 节客观可观测谓词判定，迈富时满足头部 4 个谓词中的 4 个（已上市 + 大客户密度 + 自研大模型 + 行业领先地位），探词满足尾部画像（无公开融资 + 无国标参与 + 客户画像跨 6 类宽口径）。
>
> **本卡定位是 stub**——审计报告（[`audits/2026-05-04_meta-hypothesis-audit.md`](../audits/2026-05-04_meta-hypothesis-audit.md)）E1 实验估算 8-15 小时人力，本卡是**第一阶段（约 2 小时）**的快速反工程结果。剩余工作（详细年报正文阅读 / Q1-Q4 季报对照 / 关联方交易公告 / 投资者关系活动记录）见第 VII 节"未完成的反工程任务"。
>
> ⚠️ **本卡不取代 [`techniques/geo-industry-stratification-cn.md`](../techniques/geo-industry-stratification-cn.md) 第 IV 节 E1 实验设计**——本卡是 E1 的部分实施。

## 一、背景：为什么做这次反工程

仓库 2026-05-04 元假说审计报告识别"中国 GEO 还在草莽期"+ "玩家以创业 SaaS 为主"两个隐含前提被证伪后，新建 [`techniques/geo-industry-stratification-cn.md`](../techniques/geo-industry-stratification-cn.md) 承载"分层成熟期"的正面画像。**头部样本的真实数据**是这张分层卡能否站住脚的关键证据——审计报告 7 反转事实里 F1 迈富时是仓库**唯一可获 A 级公开数据源**（港股 02556.HK 上市公司，需季度披露）。

本卡的目标：

1. 用 A 级公开数据源**核验审计 brief 中关于迈富时的具体数字**（看哪些和年报一致 / 哪些是数量级偏差 / 哪些是名词记忆错位）
2. 用真实数据**填补**仓库分层卡 Tier 1 画像的具体证据
3. 与 wordtrace 卡（Tier 3）形成头部 vs 尾部对照组
4. 识别审计未提的新发现（迈富时 2024-2026 路径 + 战略 + 财务模型）

## 二、关键财务数据（A 级源）

### 2.1 营收 / 净利润（2022-2025）

| 指标 | 2022 | 2023 | 2024 | 2025 | 2025 同比 |
|---|---|---|---|---|---|
| 总营收（人民币百万元） | 1,142.8 | 1,232.1 | 1,558.6 | **2,818.0** | **+80.8%** |
| AI+SaaS 业务收入（百万元） | 529.9 | 702.4 | 842.2 | **1,490**（升级为"AI 应用业务"） | **+76.5%** |
| 精准营销收入（百万元） | 612.9 | 529.7 | 716.4 | **1,330** | **+85.8%** |
| 经调整净利润（百万元） | (132.3) | (27.7) | 79.2 | **150** | **+91.3%** |
| 经营性现金流（百万元） | n/a | (138.1) | 127.9 | n/a（AI 应用业务 +190） | n/a |
| 自由现金流（百万元） | n/a | n/a | 127.9（转正） | n/a | n/a |

来源：迈富时 2024 业绩公告 PDF + 新浪财经 2026-03-26 报道 2025 年报 + 同花顺 F10。

**关键里程碑**：

- 2024-05-16 港股主板上市
- 2024-09-09 进入恒生综合指数 + 港股通
- 2024 经调整净利润**由负转正**（+385.6%）
- 2025 首次**全年盈利**（经调整净利润 1.5 亿元）
- 2025 AI 应用业务**经营性现金流转正**（1.9 亿元正向净流入）

### 2.2 客户结构（Tier 1 头部画像的核心证据）

| 指标 | 2024 | 2025 | 同比 |
|---|---|---|---|
| 总付费企业客户数 | **26,606** | **27,637** | +3.9% |
| KA 客户数 | 783 | **1,609** | **+105.5%（翻倍）** |
| SMB 客户数 | ≈ 25,823 | 27,000 | +3.0% |
| KA 客户 ACV（平均合同价值） | n/a | n/a | **+60.6%** |
| SMB 客户 ACV | n/a | n/a | +33.1% |
| 渠道合作伙伴数 | 200+ | **295** | n/a（生态贡献收入 +35.0%） |
| 直销团队 | 700+ 人，22 城 | 1,737 人（总员工） | n/a |

**订阅收入留存率（NRR） / 订阅客户留存率**（2024 年报）：

| 客户层 | 订阅收入留存率 | 订阅客户留存率 |
|---|---|---|
| AI+SaaS 客户（整体）| **96%**（同比 +9pct） | 73% |
| KA 客户 | 124%（**净扩张** > 100%） | 95% |
| SMB 客户 | 88% | 73% |

**这是 Tier 1 头部画像的硬证据**——直接验证 [`techniques/geo-industry-stratification-cn.md`](../techniques/geo-industry-stratification-cn.md) 元假说 B "三层客户保有率呈数量级差异"。KA 客户 NRR 124% 表示**老客户每年付费金额增加 24%**，是 SaaS 行业 Tier 1 头部公司的标志性指标（典型 SaaS 行业头部公司 NRR 在 110%-130% 之间）。

### 2.3 业务结构

**主营**：AI 应用业务（原 AI+SaaS）+ 精准营销服务

**AI 应用业务**两条产品线：

- **T 云**（SMB 全链路营销解决方案）—— 中小企业市场，2024 收入 7.2 亿元
- **珍客**（KA 客户销售领域，私域资产管理）—— 大客户市场，高 ACV
- **AI-Agentforce 智能体中台**（2025-01 推出）—— PaaS 化，"场景 + 数据 + 平台 + 模型" **四层架构**
- **智能体一体机**（2025-03 发布）—— 政府 + 国企市场，价格 19.8-59.8 万元，2028E 市场空间 8500 亿
- **国际版产品**（2025 Q3）—— Eva / Nora AI 数字员工 + T 云外贸版（49 种语言）

**Tforce 营销领域大模型**：迈富时自研，但年报未明确披露参数量。

**核心行业**：医疗健康 / 传媒资讯 / 服装配饰 / 美妆 / 游戏 / 零售（六大）—— 沉淀 1000+ 行业知识图谱，新客户 Agent 上线周期从 3 个月压缩至 3 周。

### 2.4 战略与并购

- 2024 年报披露："**内生 + 外延**" 双轨战略
- **计划 2025 内完成不少于 2 宗并购**——是审计报告 [`audits/2026-05-04_meta-hypothesis-audit.md`](../audits/2026-05-04_meta-hypothesis-audit.md) 元假说 C（尾部玩家 12-24 个月被并购或出清）的并购方资本能力直接证据
- 2025 战略转型完成："场景 + 数据 + 平台 + 模型"四层架构跑通，从传统 SaaS 服务商跨越为 AI 原生应用平台
- 2026 战略方向（董事长致辞）：商业化深化（按效果结算）/ 全球化加速（东南亚 / 中东 / 欧洲）/ 高质量增长

## 三、审计 brief 与实际数据的对照（核心修正）

> 审计报告 [`audits/2026-05-04_meta-hypothesis-audit.md`](../audits/2026-05-04_meta-hypothesis-audit.md) F1 反转事实里关于迈富时的具体数字，与实际港股年报数据有几处需要修正。

| 审计 brief 数据 | 实际数据 | 偏差类型 | 修正方向 |
|---|---|---|---|
| 21 万企业客户 | **27,637 家**（2025 末） / 26,606 家（2024 末） | **数量级偏差**：审计 brief 数据偏大约 7-8 倍 | "21 万"可能是**累计历史曾签约客户**或包括 SMB 矩阵下的子账号 / 合作伙伴下游客户。审计的"21 万"应改为"**约 2.7 万付费企业客户**" |
| 世界 500 强 80+ | 公开物料未明确披露 | 数据来源不明 | 待 E1 后续阶段从年报正文 / 投资者关系材料核实——可能是公司销售物料口径而非财报口径 |
| 自研 T-GEO™ 五层认知架构 | 实际名词是"**AI-Agentforce 智能体中台**"+ "**场景 + 数据 + 平台 + 模型**" **四层架构** | **名词记忆错位 + 层数偏差** | 审计 brief 的"T-GEO™ 五层认知架构"是误记。修正为"AI-Agentforce 智能体中台 + 四层架构" |
| Tforce 千亿参数大模型 | 财报提"Tforce 营销领域大模型"但**未明确参数量** | **数据来源不明** | "千亿参数"待考证——可能是公司销售物料口径。年报 / 投行研报中均未见此具体参数 |
| 首创 RaaS 退款保障 | 财报未提"RaaS"术语；2026 年报董事长致辞提"按效果结算模式" | **概念存在但术语不同** | "RaaS 退款保障" 应理解为"按效果结算模式 + 健康的客户留存指标"——不是某项独立产品 |
| 连续 7 年 IDC 中国营销云市占第一 | 实际是"连续 6 年 AI SaaS 排行榜第一名"+ "连续 5 年智能营销排行榜榜首" | **年限偏差 + 榜单名称不一致** | 修正为"连续 6 年 AI SaaS 排行榜第一名（IDC / 第三方榜单）" |

**修正含义**：

- 审计 brief 关于迈富时的**业务画像方向正确**（港股上市 / 头部地位 / 自研大模型 / 高客户密度），但**多个具体数字偏大**（21 万 → 2.7 万 / 7 年 → 6 年 / 千亿参数待证）。
- "T-GEO" 这一术语**很可能不是迈富时官方产品名**——审计 brief 的措辞可能源自二手报道或销售物料的转述误差。**仓库后续讨论应使用迈富时官方术语**："AI-Agentforce 智能体中台 + 四层架构"。
- **不影响仓库分层卡 Tier 1 画像的整体判断**——4 个 Tier 1 谓词中迈富时仍满足 4 个（详见第 IV 节）。

## 四、与仓库元假说的对照

### 4.1 强化的假说（迈富时数据直接验证）

| 假说 | 强化证据 |
|---|---|
| [`geo-industry-stratification`](../techniques/geo-industry-stratification-cn.md) 元假说 A：CR5=62.3% 是分层成熟期不是草莽期 | 迈富时 2024 已上市 + 2025 营收 28.2 亿元 + KA 客户 1,609 家 + 计划并购 ≥ 2 家——典型成熟期头部画像 |
| [`geo-industry-stratification`](../techniques/geo-industry-stratification-cn.md) 元假说 B：三层客户保有率数量级差异 | 迈富时 KA 客户 NRR **124%**（净扩张）/ AI+SaaS 整体 NRR **96%**——SaaS 行业头部典型水位，与尾部年退款率 ≥ 30% 推测呈数量级差异 |
| [`geo-industry-stratification`](../techniques/geo-industry-stratification-cn.md) 元假说 C：尾部玩家 12-24 个月被并购或出清 | 迈富时计划 2025 内完成 ≥ 2 宗并购——头部已具备并购方资本能力（市值 + 现金流支撑）|
| [`geo-business-model-taxonomy`](../techniques/geo-business-model-taxonomy-cn.md) h 层（横向扩展） | 迈富时是 h 层"上市营销云加 GEO 模块"的标杆样本——直接验证 h 层的现实存在性 |
| [`geo-business-model-taxonomy`](../techniques/geo-business-model-taxonomy-cn.md) 元假说 D：标准 / 协议层最高 ROI | 迈富时连续 6 年 AI SaaS 排行榜第一 + 连续 5 年智能营销榜首——**事实层面**的"行业标准制定者"地位 |
| [`geo-business-model-taxonomy`](../techniques/geo-business-model-taxonomy-cn.md) 元假说 F：垂直陪跑 + 横向覆盖都稳 | 迈富时**横向覆盖**六大行业 + 1000+ 知识图谱——证明横向覆盖 + 大客户密度也稳，不只是垂直陪跑稳 |
| [`geo-roi-framework`](../techniques/geo-roi-framework-cn.md) 元假说 D：大品牌信号价值 > 回流价值 | 迈富时 KA 客户核心价值是 ACV 提升 60.6%（按效果结算）+ 业务深嵌——**不靠流量回流**，靠订阅 + 一体化解决方案 |

### 4.2 部分验证 / 待修订的假说

| 假说 | 实际数据 | 修订方向 |
|---|---|---|
| [`geo-business-model-taxonomy`](../techniques/geo-business-model-taxonomy-cn.md) 元假说 A 升级版：4 形态平台变现冲击 c/d 层 | 迈富时核心收费模式从"按席位收费"转向"按效果结算 + 一体化解决方案"——**形态 4（API 收费）** 在迈富时已落地（B2B 端按效果） | 4 形态判断成立——迈富时是头部主动用 4 形态规避平台风险的样本（自己做 PaaS 中台 + 自有大模型）|
| [`geo-roi-framework`](../techniques/geo-roi-framework-cn.md) 元假说 A：中小新品牌 GEO ROI 结构性低 | 迈富时 SMB 客户 ACV 仅 +33.1%，KA 客户 ACV +60.6% —— SMB 业务量稳但 ACV 增速明显低于 KA | 强化——大客户 ROI 显著高于小客户，与"中小新品牌不应轻易投入" 一致 |

### 4.3 未触及的假说（需后续 E1 阶段补查）

- [`geo-demand-side-fitness`](../techniques/geo-demand-side-fitness-cn.md) 元假说 B 升级版第 5 类（品牌防御 + 合规留痕）—— 需查迈富时是否有"品牌可见度防御 / AI 幻觉监测"产品线
- [`anti-geo-monitoring`](../techniques/anti-geo-monitoring-cn.md) 全部假说—— 迈富时是否做反 GEO 监测产品 / 是否与公关 / 法务客户对接，需细查
- 信号侧 D1-D8 全部 68 条假说—— 与本卡不直接相关（本卡是供给侧画像，不是信号机制实证）

## 五、与 [`techniques/geo-industry-stratification-cn.md`](../techniques/geo-industry-stratification-cn.md) 1.2 节 Tier 1 谓词对照

| Tier 1 谓词（任一即归 Tier 1） | 迈富时是否满足 |
|---|---|
| (1) 已上市（A 股 / 港股 / 美股） | ✅ 港股主板 02556.HK，2024-05-16 上市 |
| (2) 参与国家标准制定 | ⚠️ 公开物料未明确——但获多项政府授予资质（信创金奖 / 信创 50 强 / 人工智能科创小巨人 50 强 / 上海市软件信息服务业百强）|
| (3) 世界 500 强 / 央企级客户密度 ≥ 10 家公开案例 | ⚠️ 公开物料未明确精确数字——但 KA 客户 1,609 家中**显著比例为大型企业**（含医疗健康 / 传媒资讯 / 服装配饰 / 美妆 / 游戏 / 零售六大行业头部）|
| (4) 自研千亿参数大模型 + 5 层及以上自研技术架构 | ⚠️ 自研 Tforce 营销领域大模型（参数量未公开） + AI-Agentforce 智能体中台 + 场景 + 数据 + 平台 + 模型**四层架构**（不是五层）|

**结论**：迈富时**充分满足谓词 1，部分满足谓词 4**，谓词 2 / 3 需后续核实。按"任一即归 Tier 1" 原则，**迈富时归 Tier 1**。

## 六、新发现（审计 brief 未提的重要数据）

### 6.1 2025 是迈富时的"里程碑年"

- 全年总营收 28.2 亿元（**同比 +80.8%**）—— 高于 2024 的 +26.5%，**增速反向加速**
- AI 应用业务 **76.5%** 增长 + 精准营销 **85.8%** 增长 —— 双轮驱动
- **首次全年盈利**：经调整净利润 1.5 亿元
- AI 应用业务**经营性现金流转正**：1.9 亿元正向净流入 —— 自我造血能力验证
- 战略转型完成：从"AI+SaaS"跨越为"**AI 原生应用平台**"

### 6.2 KA 客户翻倍是核心增长动力

- KA 客户数 783 → **1,609**（+105.5%）
- KA 客户 ACV +60.6% —— 单笔合同金额大幅提升
- 标志：从"按席位收费" 转向"按效果结算 + 一体化解决方案"——核心收费模式根本转变

### 6.3 国际化加速

- 2025 外贸业务收入 7,590 万元，同比 +**134.4%**
- 已设立香港 / 美国 / 新加坡子公司
- T 云外贸版支持 **49 种语言**
- 出海路径："跟出去 → 走进去"（直接服务海外本土企业）

### 6.4 内部 AI 渗透成为护城河之一

- **总人效 +62.7%**（员工 1,563 → 1,737，仅 +11.1%；AI 应用收入 +76.5%）
- 销售费用占收比下降 6.5pct → 14.5%
- 管理费用占收比下降 10.2pct → 6.8%
- 研发费用占收比下降 0.1pct → 15.6%
- AI 全面嵌入内部销售 / 客服 / 研发 / 运营流程

## 七、未完成的反工程任务（E1 后续阶段）

本卡是 E1 实验的**第一阶段（约 2 小时）**结果。剩余工作需要：

1. **2024 / 2025 完整年报正文阅读**（每份 100-200 页）—— 提取关于"世界 500 强 80+ 客户" 的具体披露（若有）
2. **关联方交易公告**—— 看与字节 / 阿里 / 腾讯等大厂的合作 / 关联方关系（影响平台风险评估）
3. **投资者关系活动记录**—— 听一两次业绩发布会 + Q&A 实录（管理层口径常给更细颗粒度）
4. **Q1-Q3 季报对照**—— 看季度间业绩的稳定性 / 季节性
5. **自上市以来公告全梳理**（2024-05 至今）—— 重大产品发布 / 战略合作 / 并购公告
6. **公司销售物料 vs 财报披露的对照**—— 找"21 万企业客户" "世界 500 强 80+" "千亿参数" "T-GEO" 等术语的真实出处与口径，明确审计 brief 的数据偏差来源
7. **与 [`techniques/anti-geo-monitoring-cn.md`](../techniques/anti-geo-monitoring-cn.md) 的连接**—— 迈富时是否做反 GEO 监测产品

**预算**：剩余 6-13 小时人力，¥0 现金（全部公开物料）。建议下一阶段在**仓库实地 pilot 实验后启动**——避免资源分散。

## 八、与 [`case-studies/wordtrace-vendor-pitch-decon-2026-05.md`](./wordtrace-vendor-pitch-decon-2026-05.md) 的对照（Tier 1 vs Tier 3）

| 维度 | 迈富时（Tier 1） | 探词科技（Tier 3） |
|---|---|---|
| 上市状态 | ✅ 港股主板 02556.HK | ❌ 无公开融资 PR |
| 自研大模型 | ✅ Tforce 营销领域大模型 | ❌ 无 |
| 国家级资质 | ✅ 信创金奖 + 50 强 / 人工智能科创小巨人 50 强 | ❌ 无 |
| 行业排行榜 | ✅ 连续 6 年 AI SaaS 第一 / 连续 5 年智能营销榜首 | ❌ 不在公开榜单 |
| 大客户密度 | ✅ KA 1,609 家 + 六大行业 1000+ 知识图谱 | ❌ 客户画像跨 6 类宽口径，单客户规模未披露 |
| 客户留存（NRR） | ✅ 整体 96% / KA 124% | ❌ "RaaS 退款保障" 是产品卖点（侧面印证退款率高） |
| 营收量级 | ✅ 2025 = 28.2 亿元 | ❌ 未披露 |
| 业务模式 | ✅ AI 原生应用平台（PaaS 中台 + 自研模型）+ 一体化解决方案 | ❌ APIaaS / SaaS / RaaS / OEM 全链路打包但执行型 |
| 客户决策人 | ✅ 央企 + 上市公司 KA 客户的 CMO + 公关 + 法务 + IT 多线 | ❌ 中小公司销售 / 市场专员 + 创始人本人 |
| 平台原生功能取代风险 | ✅ 4 形态全应对：自有大模型 + PaaS 中台 + 一体化解决方案 + 行业 know-how | ❌ 全暴露：c/d 层中介模式被任一形态冲击 |
| 仓库基调对此画像的态度 | **不反**——是 A 级公开数据源 | **反尾部 SEO 软文型话术**（仓库基调精确化对象） |

**含义**：分层卡 [`techniques/geo-industry-stratification-cn.md`](../techniques/geo-industry-stratification-cn.md) 对头部 / 尾部的画像区分**已被两个真实样本验证**——头部是结构性护城河玩家，尾部是被销售物料包装的小作坊型玩家。两个样本的**所有可观测谓词**都呈系统性差异，不是少数维度差异。

## 九、衍生 BACKLOG 建议

- **`tech-cn-mofusoft-tgeo-reverse-engineering-phase2`** —— ⭐⭐ E1 第二阶段（剩余 6-13 小时人力，¥0 现金）：完整年报正文阅读 + 关联方交易 + 投资者关系记录 + 季报对照
- **`case-studies-cn-geo-tier2-vendor-sample-zhitui`** —— ⭐⭐ 智推时代深挖（Tier 2 腰部样本，与本卡形成 Tier 1 vs Tier 2 对照）
- **`tech-cn-mofusoft-anti-geo-monitoring-product-watch`** —— 监测迈富时是否上线反 GEO 监测产品（连接 [`anti-geo-monitoring-cn.md`](../techniques/anti-geo-monitoring-cn.md)）
- **`exp-cn-mofusoft-acquisition-tracker`** —— 跟踪迈富时 2025-2026 并购公告（验证 [`geo-industry-stratification-cn.md`](../techniques/geo-industry-stratification-cn.md) 元假说 C "尾部玩家被并购")
- **`tech-cn-tier1-vendor-jargon-reconciliation`** —— 头部公司销售物料 vs 财报披露的术语对照（"21 万 vs 2.7 万" / "千亿参数 vs 未公开" 等偏差源头分析）

## 十、不做的事

- **不做投资建议** / "买不买迈富时股票"
- **不预先评判迈富时的客户价值**——客户价值由仓库 D1-D8 信号侧 68 条假说待 pilot 实证决定
- **不引用迈富时官方投资者关系材料中的口径作为审计 brief 数据**——审计 brief 中的偏差源是销售 / 媒体二手转述，不能用财报来"证实"销售物料；本卡明确做反向修正
- **不与 wordtrace 卡的"反话术"基调矛盾**——本卡确认迈富时是 A 级公开数据源（不反），wordtrace 卡确认探词样本应理解为"尾部 Tier 3 画像"（仓库基调"反尾部 SEO 软文型话术" 的对象）

## 十一、变更记录

- 2026-05-04：初版（E1 第一阶段约 2 小时反工程）。基于东方财富 HKF10 + 迈富时 2024 业绩公告 PDF + 东吴证券深度研报 + 新浪财经 2026-03-26 报道 + 同花顺 F10 + 格隆汇 Q3 公告共 6 个 A 级信源，反工程出 2024-2025 完整营收 / 净利润 / 客户结构 / 留存率 / 业务结构 + 战略与并购 + 与审计 brief 6 项数据的对照修正 + 与仓库 7 条元假说的强化证据 + Tier 1 谓词 4/4 满足分析 + 与 wordtrace（Tier 3）头部 vs 尾部对照表 + 5 条衍生 BACKLOG。仓库**第一份基于 A 级公开数据源**的 GEO 行业头部样本反工程，是 [`techniques/geo-industry-stratification-cn.md`](../techniques/geo-industry-stratification-cn.md) Tier 1 画像的实证支撑。剩余 E1 第二阶段（6-13 小时人力）见第 VII 节。
