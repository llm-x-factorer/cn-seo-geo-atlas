# BACKLOG

> **状态**：仓库已 push 到 GitHub（[LLM-X-Factorer/cn-seo-geo-atlas](https://github.com/LLM-X-Factorer/cn-seo-geo-atlas)，2026-05-03）。**转 issue 工作进行中**——按"高优先级 + 高复用价值"分批转，本文件继续作为待办池，已转 issue 的条目末尾追加 issue 编号引用，退役计划在所有 high 优先级条目转完后启动。
>
> **维护原则**：新待办先进这里。完成后留 `[x]` 一段时间（一周左右）再清。永远不在卡片正文里散落"待办"——卡片只承载知识，待办都汇集到这里。

转 issue 时统一用 `gh issue create` + 模板 [`.github/ISSUE_TEMPLATE/research-task.md`](./.github/ISSUE_TEMPLATE/research-task.md)。

## 已转 GitHub issue（首批 10 条，2026-05-03）

| # | 标题 | 来源 BACKLOG 条目 |
|---|------|-------------------|
| [#1](https://github.com/LLM-X-Factorer/cn-seo-geo-atlas/issues/1) | selector pilot 验证（豆包 + DeepSeek 实际 UI） | `exp-doubao-vs-deepseek-paired-queries` 子 1 |
| [#2](https://github.com/LLM-X-Factorer/cn-seo-geo-atlas/issues/2) | Pilot run（10 次采集端到端验证） | `exp-doubao-vs-deepseek-paired-queries` 子 2 |
| [#3](https://github.com/LLM-X-Factorer/cn-seo-geo-atlas/issues/3) | 主实验执行（320 次采集 × 3 天） | `exp-doubao-vs-deepseek-paired-queries` 子 3 |
| [#4](https://github.com/LLM-X-Factorer/cn-seo-geo-atlas/issues/4) | 数据评分 + 统计分析 | `exp-doubao-vs-deepseek-paired-queries` 子 4 |
| [#5](https://github.com/LLM-X-Factorer/cn-seo-geo-atlas/issues/5) | 回写结果到豆包 / DeepSeek / Princeton 9 卡片 | `exp-doubao-vs-deepseek-paired-queries` 子 5 |
| [#6](https://github.com/LLM-X-Factorer/cn-seo-geo-atlas/issues/6) | 五大厂 adapter 扩展（wenxin / qianwen / yuanbao） | `tools-five-vendor-adapters` |
| [#7](https://github.com/LLM-X-Factorer/cn-seo-geo-atlas/issues/7) | source_classifier.py 三套标签扩展 | 合并 `tools-source-classifier-backfill-alibaba` + `-tier-tag` + `-platform-tag` |
| [#8](https://github.com/LLM-X-Factorer/cn-seo-geo-atlas/issues/8) | ⭐⭐⭐ 中文 LLM 引用源 CTR 测量 | `exp-cn-llm-citation-source-ctr` |
| [#9](https://github.com/LLM-X-Factorer/cn-seo-geo-atlas/issues/9) | 跨 LLM 信源池 Jaccard 量化（多卡复用） | 合并 `exp-cn-jaccard-of-cited-sources-cross-llm` + `exp-cn-cross-llm-source-jaccard` |
| [#10](https://github.com/LLM-X-Factorer/cn-seo-geo-atlas/issues/10) | ⭐⭐⭐ 等预算 GEO vs 短视频 ROI 对照 | `exp-cn-equal-budget-channel-comparison` |

---

## 🧪 实验类（priority: high）

### 豆包

- [ ] **`exp-doubao-citation-source-distribution`** —— 在豆包 APP 端跑 N 类 query × M 次重复，统计引用源分布。验证"今日头条 60%+"等服务商口径。来源：[`platforms/doubao/overview.md`](./platforms/doubao/overview.md)、[`citation-mechanism.md`](./platforms/doubao/citation-mechanism.md) 假说一。
- [ ] **`exp-doubao-app-vs-api-divergence`** —— 同 query 同时刻在豆包 APP 和 火山引擎 API 双端跑，对比信源结构。验证假说二。
- [ ] **`exp-doubao-recency-window`** —— 受控发布同主题内容到不同字节系平台，测时效窗口。验证假说三。
- [ ] **`exp-doubao-bytedance-ecosystem-bias`** —— 对比同主题内容在字节系 vs 非字节系平台发布后被引用率。验证元假说 B。

### DeepSeek

- [ ] **`exp-deepseek-citation-source-distribution`** —— 在 chat.deepseek.com 跑 query 集，统计引用源分布。验证"CSDN / 搜狐号 / 网易号 / 百科"假说。
- [ ] **`exp-deepseek-csdn-bias-test`** —— 用对照内容（同主题 CSDN vs 知乎 vs 微信公众号）测 DeepSeek 偏好。
- [ ] **`exp-deepseek-via-third-party-divergence`** —— 同 query 在官方 + 元宝 R1 模式 + 问小白 + 纳米 AI 跑，量化集成方影响（B 类研究边界）。
- [ ] **`exp-deepseek-r1-vs-v-citation-difference`** —— R1 推理模式 vs V 系列通用模式的引用行为差异。

### 配对实验（豆包 × DeepSeek，最高价值）

- [x] **`exp-doubao-vs-deepseek-paired-queries`** —— 实验设计完成于 2026-05-01：[`exp-doubao-vs-deepseek-paired.md`](./experiments/exp-doubao-vs-deepseek-paired.md)
  - [x] 采集脚本骨架完成于 2026-05-01：[`tools/exp-doubao-vs-deepseek-paired/`](./tools/exp-doubao-vs-deepseek-paired/)
  - [ ] **selector pilot 验证**（豆包 / DeepSeek 实际 UI 跑 1-2 个 query 验证 selector，调整失败的）
  - [ ] Pilot run（10 次采集，端到端验证脚本可用）
  - [ ] 主实验执行（320 次采集 × 3 天）
  - [ ] 数据评分 + 统计分析（脚本就绪，跑就行）
  - [ ] 回写结果到豆包 / DeepSeek / Princeton 9 策略卡片

### Princeton 9 策略对照

- [ ] **`exp-princeton-1-cite-sources-cn`** —— 中文场景下"引用央媒 vs 引用同生态"对豆包 / DeepSeek 引用率的影响。
- [ ] **`exp-princeton-3-statistics-addition-cn`** —— "加数据"在豆包 / 千问 / DeepSeek 的差异。
- [ ] **`exp-princeton-meta-A-source-vs-style`** —— 信源信号 vs 文风信号的相对效应（元假说 A）。
- [ ] **`exp-princeton-meta-C-multi-actor`** —— 多竞争方下的策略衰减（元假说 C），中文复现 C-SEO Bench。
- [ ] **`exp-princeton-9-keyword-stuffing-cn`** —— 关键词堆砌在中文 LLM 是否依然反向（低优先级，预期与英文一致）。

### 服务商话术验证 micro-pilot（最低成本 + 与 selector pilot 兼容）

> 来源：[`case-studies/wordtrace-vendor-pitch-decon-2026-05.md`](./case-studies/wordtrace-vendor-pitch-decon-2026-05.md)。这三条都是**任意账号即可复测的现成 query**，零客户依赖、零隐私风险，可顺路完成 doubao / qianwen / wenxin / yuanbao / kimi 五个平台的 selector pilot。完成后回写到上述 case-study 卡的"复测结果"段。
>
> 复测最低标准：≥ 2 账号 × ≥ 2 时段 × ≥ 5 次 / 平台 × 隐私模式 + 截图 + 文本双留底，按 [`tools/exp-doubao-vs-deepseek-paired/source_classifier.py`](./tools/exp-doubao-vs-deepseek-paired/source_classifier.py) 同套规则归类。

- [ ] **`exp-cn-vendor-pitch-self-reference-wordtrace`** —— ⭐⭐⭐ 复测"湖南哪家 GEO 公司好"× 豆包 / 千问 / Kimi / 文心 / 百度 AI（手册 p17 自指型案例）。**最高优先级**：5 平台同时跑，与 selector pilot 高度兼容；自指型 query 受 GEO 工作影响最强，是 C-SEO Bench 立场下天然测试场。验证厂商主张"长沙探词科技稳居 5 平台前二"是否在跨账号 / 跨时段下成立。
- [ ] **`exp-cn-vendor-pitch-baiyun-tool-recommendation`** —— ⭐⭐ 复测"哪个育种软件比较好"× 文心 / 豆包 / Kimi / 元宝（手册 p16 案例）。冷门 B2B 工具类 query 竞品池小，结果易稳定，是"普通客户案例"复现性的代表样本。
- [ ] **`exp-cn-vendor-pitch-yuanrun-pinot-noir`** —— ⭐ 复测"国产黑皮诺哪家好喝" / "黑皮诺有什么推荐的牌子" × 豆包 / 千问（手册 p14-15 案例）。小众商品类 query 易复现，作为补充样本。

### 需求侧实证（priority: high，资金依赖）

> 来源：[`techniques/geo-demand-side-fitness-cn.md`](./techniques/geo-demand-side-fitness-cn.md) 第 IV 节实验设计建议。这两条都是仓库需求侧元假说 A、B、E 的直接证伪 / 支持任务。需要资金（调研公司或自建样本），不是当前会话内能立刻跑的微型 pilot。

- [ ] **`exp-cn-llm-decision-path-survey`** —— ⭐⭐⭐ E1 中文消费者真实决策路径分品类调研：≥ 500 名 18-55 岁城市网民 × ≥ 12 类消费场景，量化"先 LLM / 后 LLM / 不用 LLM"占比。预算 ¥3-30 万。直接证伪 / 支持元假说 A、E。
- [ ] **`exp-cn-b2b-selection-llm-penetration`** —— ⭐⭐ E2 B2B 选型场景 LLM 渗透率独立测量：≥ 100 名 B2B 决策者 × 近 3 个月 ≥ 1 次选型经历跟踪。预算 ¥3-8 万。给 [`geo-roi-framework-cn.md`](./techniques/geo-roi-framework-cn.md) B2B SaaS 类目提供 ROI 输入参数。

---

## 🌐 平台调研类（priority: medium）

### 生成式引擎

- [x] **`platform-qianwen`** —— 千问 ✅ 完成于 2026-05-01：[`overview.md`](./platforms/qianwen/overview.md)、[`citation-mechanism.md`](./platforms/qianwen/citation-mechanism.md)
  - [ ] **`platform-qianwen-changelog`** —— 千问平台规则变更年表
  - [ ] **`platform-qianwen-commerce-geo`** —— 千问"AI 下单"路径下的电商 SKU 优化机制专题
  - [ ] **`exp-qianwen-citation-source-distribution`** —— 千问 APP 引用源分布
  - [ ] **`exp-qianwen-commerce-geo`** —— 电商类 query 在千问上的"AI 下单"路径
  - [ ] **`exp-qianwen-app-vs-quark-vs-taobao-divergence`** —— 阿里多入口同模型差异
  - [ ] **`exp-qwen-open-vs-qianwen-closed`** —— Qwen 开源版 vs 千问 APP 闭源版引用机制
- [x] **`platform-yuanbao`** —— 腾讯元宝 ✅ 完成于 2026-05-01：[`overview.md`](./platforms/yuanbao/overview.md)、[`citation-mechanism.md`](./platforms/yuanbao/citation-mechanism.md)
  - [ ] **`platform-yuanbao-changelog`** —— 元宝平台规则变更年表
  - [ ] **`platform-yuanbao-wechat-ecosystem-geo`** —— 微信生态 GEO 专题（公众号 + 视频号 + 文档）
  - [ ] **`exp-yuanbao-citation-source-distribution`** —— 元宝 APP 引用源分布
  - [ ] **`exp-yuanbao-multi-model-routing`** —— 元宝多模型路由策略观察
  - [ ] **`exp-yuanbao-wechat-mp-bias`** —— 微信公众号 vs 其他信源的相对权重
  - [ ] **`exp-yuanbao-app-vs-wechat-embedded`** —— 元宝 APP vs 微信内嵌 AI 搜的引用对比

#### 跨平台终极实验

- [x] **`exp-five-vendor-paired-queries`** ⭐⭐ —— **五大厂配对实验**实验设计完成于 2026-05-02：[`exp-five-vendor-paired-queries.md`](./experiments/exp-five-vendor-paired-queries.md)（H1 生态偏好普遍性 + H2 DeepSeek 技术 + H3 千问电商；预注册阈值 20pp/20pp/30pp + 120 比较 Bonferroni 修正；800 次采集计划；状态 concept，依赖第一个实验先跑通）
  - [ ] **`tools-five-vendor-adapters`** —— 在 [`tools/exp-doubao-vs-deepseek-paired/`](./tools/exp-doubao-vs-deepseek-paired/) 基础上新增 3 个 adapter（wenxin / qianwen / yuanbao）+ 扩展 source_classifier 加入 `alibaba-eco` 归类
  - [ ] **`tools-source-classifier-backfill-alibaba`** —— 第一个实验跑完后，用扩展后的 source_classifier 重跑分类，把原 `other` 中实际属于 `alibaba-eco` 的样本回填，确保两个实验的数据可横向对比
  - [ ] **`exp-five-vendor-selector-pilot`** —— 5 平台 selector pilot 验证（2 个继承自第一个实验，3 个新增）
  - [ ] **`exp-five-vendor-pilot-run`** —— 10 query × 1 次 × 5 平台 = 50 次端到端 pilot
  - [ ] **`exp-five-vendor-main-run`** —— 主实验执行（800 次采集 × 3 天）
  - [ ] **`exp-five-vendor-analyze-and-writeback`** —— 数据评分 + 统计分析 + 回写到 5 平台 + Princeton 元假说 + README
- [x] **`tech-private-vs-public-source-cn`** —— 中文私域 vs 公域信源光谱 ✅ 完成于 2026-05-02：[`techniques/private-vs-public-source-cn.md`](./techniques/private-vs-public-source-cn.md)（5 档公开度 L1-L5 + 各信源平台横向对照 + 训练 / RAG / 用户转述三条传导路径 + 5 条元假说 + 3 个实验设计；强假说 B：公众号矩阵仅在元宝 / 微信搜一搜成立；强假说 D：L4-L5 全私域是 0 信号基线）
  - [ ] **`exp-cn-source-disclosure-tier-distribution`** —— 按档位归类信源后引用率分布（验证元假说 A，可从五大厂实验数据析出）
  - [ ] **`exp-cn-mp-matrix-cross-llm`** —— 公众号矩阵跨 LLM 对照实验（验证元假说 B，⭐⭐⭐ 直接打脸服务商话术）
  - [ ] **`exp-cn-xhs-l3-passive-observation`** —— 小红书 L3 注册可见信源传导路径观察实验（验证元假说 C）
  - [x] **`tech-cn-platform-search-blockade`** —— 中文平台间相互封锁搜索的历史与现状 ✅ 完成于 2026-05-02：[`techniques/platform-search-blockade-cn.md`](./techniques/platform-search-blockade-cn.md)（封锁拆为 C1-C5 五类 + 2008-2026 关键节点时间线 + 当前状态矩阵 + 信源池子池切割 + 5 条元假说 + 3 个实验设计；强假说 A：中文 LLM 信源池 Jaccard < 50%；强假说 C：互联互通对 LLM 引用率影响接近 0）
    - [ ] **`exp-cn-cross-llm-source-jaccard`** —— 跨 LLM 信源池 Jaccard 量化（验证元假说 A，可从五大厂数据析出）
    - [ ] **`exp-cn-platform-domain-distribution`** —— 按平台域名分类的引用占比对照（验证元假说 B：通用 LLM 偏向 L1 残余 Web）
    - [ ] **`tools-source-classifier-platform-tag`** —— [`tools/exp-doubao-vs-deepseek-paired/source_classifier.py`](./tools/exp-doubao-vs-deepseek-paired/source_classifier.py) 扩展加入平台来源 + 封锁状态标签
    - [ ] **`tech-cn-anti-monopoly-and-geo-roadmap`** —— 反垄断 / 互联互通政策对 GEO 影响的时间线卡（持续更新）
  - [ ] **`tech-cn-corporate-knowledge-geo`** —— 企业内部知识库 GEO 专题（公开度调整 + 选择性开放）
  - [ ] **`tools-source-classifier-tier-tag`** —— [`tools/exp-doubao-vs-deepseek-paired/source_classifier.py`](./tools/exp-doubao-vs-deepseek-paired/source_classifier.py) 扩展加入 L1-L5 档位标签
- [ ] **`platform-kimi`** —— Kimi（月之暗面）overview。早期长文本爆款，2025 后期份额被压；用户偏研究 / 学术。
- [x] **`platform-wenxin`** —— 文心一言 / 文心助手 ✅ 完成于 2026-05-01：[`overview.md`](./platforms/wenxin/overview.md)、[`citation-mechanism.md`](./platforms/wenxin/citation-mechanism.md)
  - [ ] **`platform-wenxin-changelog`** —— 文心 5.0 上线、AI 答案位演进等关键事件年表
  - [ ] **`exp-wenxin-citation-source-distribution`** —— 文心助手 APP 的引用源分布
  - [ ] **`exp-wenxin-vs-baidu-search-ai-divergence`** —— 文心助手 vs 百度搜索 AI 答案位的引用对比（同公司同模型不同入口）
  - [ ] **`exp-wenxin-baijia-bias-test`** —— 百家号 vs 同质量第三方内容在文心中的相对权重
  - [ ] **`exp-wenxin-ymyl-weighting`** —— YMYL 类 query 在文心 vs 豆包 / DeepSeek 上的引用源结构
  - [ ] **`exp-wenxin-vs-doubao-vs-deepseek-paired`** ⭐ —— **三平台配对实验**，仓库第二个高价值实证目标，验证"中文 GEO 是否需要按平台分流"
  - [ ] **`exp-wenxin-5-vs-4`** —— 文心 5.0 上线前后引用行为对照（如能跨过升级窗口）
- [ ] **`platform-chatgpt-cn`** —— ChatGPT 在中文 query 下的行为研究。
- [ ] **`platform-perplexity-cn`** —— Perplexity 在中文 query 下的行为研究。
- [ ] **`platform-claude-cn`** —— Claude 在中文 query 下的行为研究。
- [ ] **`platform-gemini-cn`** —— Gemini 在中文 query 下的行为研究。

### 内容平台站内搜索

- [x] **`platform-xiaohongshu`** —— 小红书站内搜索 + 推荐 ✅ 完成于 2026-05-01：[`overview.md`](./platforms/xiaohongshu/overview.md)、[`on-platform-search.md`](./platforms/xiaohongshu/on-platform-search.md)
  - [ ] **`xhs-as-llm-source`** —— 子卡片：小红书作为外部 LLM 信源（路径：被豆包 / 千问 / Kimi 抓取的现状）
  - [ ] **`xhs-changelog`** —— 平台规则变更年表，重点跟踪 2025 末算法部门整合的后续影响
  - [ ] **`exp-xhs-search-ranking-factors-v2026`** —— 受控笔记 A/B 测试，量化 2026 算法各信号权重
  - [ ] **`exp-xhs-search-vs-recommend-traffic`** —— 同笔记跟踪 30 天，搜索流量 vs 推荐流量贡献分布
  - [ ] **`exp-xhs-as-llm-source-coverage`** —— 在豆包 / 千问 / Kimi 跑 N 个 query，统计小红书笔记被引用比例
  - [ ] **`exp-xhs-diandian-vs-doubao`** —— "点点" vs 豆包跑同 query，对比引用结构（小红书自有 GEO 入口 vs 字节系生态）
- [ ] **`platform-zhihu`** —— 知乎搜索 + 知乎直答 + 推荐
- [ ] **`platform-weixin-sousou`** —— 微信搜一搜
- [ ] **`platform-weixin-mp`** —— 微信公众号生态
- [ ] **`platform-bilibili`** —— B 站搜索 + 推荐
- [ ] **`platform-douyin`** —— 抖音搜索 + 推荐
- [ ] **`platform-kuaishou`** —— 快手搜索 + 推荐
- [ ] **`platform-weibo`** —— 微博搜索

### 传统搜索

- [x] **`platform-baidu`** —— 百度搜索 ✅ 完成于 2026-05-01：[`overview.md`](./platforms/baidu/overview.md)、[`seo-signals-and-ai-overview.md`](./platforms/baidu/seo-signals-and-ai-overview.md)
  - [ ] **`platform-baidu-ecosystem`** —— 子卡片：百度生态详解（百家号 / 百度百科 / 百度知道 / 百度文库 / 百度健康）
  - [ ] **`platform-baidu-changelog`** —— 平台规则变更年表（含算法规范的历史与"AI 答案位"演进）
  - [ ] **`exp-baidu-ai-overview-coverage`** —— 跑 N 类 query，统计百度搜索 AI 答案位的出现率
  - [ ] **`exp-baidu-baijia-vs-third-party`** —— 百家号 vs 第三方权威媒体在百度搜索 / 文心引用中的相对权重
  - [ ] **`exp-baidu-vs-wenxin-citation-divergence`** —— 同 query 在百度搜索内嵌 AI 和文心助手中的引用源差异
  - [ ] **`exp-baidu-tezing-ka-trigger-2026`** —— 特型卡触发的 query 类型映射（2026 版）
  - [ ] **`exp-baidu-ai-vs-organic-ctr-cn`** —— 百度 AI 答案位对自然 CTR 的实际影响（中文场景对照中欧白皮书引用的 Google 数据）
- [ ] **`platform-bing-cn`** —— 必应中文
- [ ] **`platform-shenma`** —— 神马搜索
- [ ] **`platform-sogou`** —— 搜狗搜索

---

## 🛠 跨平台技术主题（priority: medium）

- [x] **`tech-structured-data-cn-practice`** —— 结构化数据中文实践 ✅ 完成于 2026-05-02：[`techniques/structured-data-cn-practice.md`](./techniques/structured-data-cn-practice.md)（Schema.org / JSON-LD / 微数据 / 百度自有规范 4 组关系 + 4 搜索引擎 × 6 LLM 支持矩阵 + Google 场景外推的 4 处失效 + 5 条元假说 + 3 个实验设计；强假说 B：schema 对中文 LLM 引用率边际效应接近 0）
  - [ ] **`exp-cn-schema-vs-no-schema-llm`** —— schema A/B 对中文 LLM 引用率影响实验（验证元假说 B）
  - [ ] **`exp-cn-baidu-native-vs-schema-org`** —— 百度自有规范 vs 通用 schema.org 效应对照（验证元假说 D）
  - [ ] **`tech-cn-search-engine-schema-support-matrix`** —— 跨搜索引擎 schema 支持类型清单（事实层卡片，定期更新）
- [x] **`tech-eeat-cn`** —— 中文 E-E-A-T 类比信号 ✅ 完成于 2026-05-02：[`techniques/eeat-cn.md`](./techniques/eeat-cn.md)（澄清两个误解 + 5 平台搜索引擎 + 6 平台 LLM 横向对照 + 5 条元假说 + 3 个实验设计建议）
  - [x] **`tech-cn-account-grade-systems`** —— 中文"号"主体绑定 + 账号等级体系横向对照卡 ✅ 完成于 2026-05-02：[`techniques/account-grade-systems-cn.md`](./techniques/account-grade-systems-cn.md)（10+ 平台 L1/L2/L3 三层结构 + 5 条元假说 + 3 个实验设计建议；强假说 D：L3 数字等级对外部 LLM 引用几乎无效）
    - [ ] **`glossary-add-account-grade-system`** —— glossary 新增 slug `account-grade-system`（走 PR）
    - [ ] **`exp-cn-account-grade-jump`** —— 等级跃升前后引用率对照实验（验证元假说 D：L3 数字等级对 LLM 引用无效）
    - [ ] **`exp-cn-cross-eco-matrix`** —— 跨生态号矩阵 vs 单号深耕对照实验（验证元假说 E：跨生态铺设是中文 GEO 真正硬信号）
  - [ ] **`exp-cn-ymyl-cross-platform-citation`** —— YMYL 类跨平台引用对照实验（验证元假说 C：YMYL 类全平台趋同）
  - [ ] **`exp-cn-account-cert-impact`** —— 认证号 vs 未认证号同质内容引用率对照实验（验证元假说 E）
- [x] **`tech-llms-txt-cn-practice`** —— llms.txt 在中文场景的采纳现状 ✅ 完成于 2026-05-02：[`techniques/llms-txt-cn-practice.md`](./techniques/llms-txt-cn-practice.md)
  - [ ] **`tech-cn-llm-crawler-ua-registry`** —— 中文 LLM 爬虫 UA / IP 段登记卡片（作为 llms.txt 卡片的事实补充）
  - [ ] **`glossary-add-crawler-directive`** —— glossary 新增 slug `crawler-directive`（涵盖 robots.txt / llms.txt / ai.txt / sitemap.xml）
  - [ ] **`exp-llms-txt-access-log-observation`** —— 实验 1：在受控中文站点部署 llms.txt 后做 30-60 天抓取日志被动观察
  - [ ] **`exp-llms-txt-ab-citation-impact`** —— 实验 2：A/B 对照测部署 llms.txt 是否提升中文 LLM 引用率（套用 exp-doubao-vs-deepseek-paired 工具栈）
  - [ ] **`exp-llms-txt-fingerprint-injection`** —— 实验 3：独特词指纹植入实验
- [x] **`tech-knowledge-graph-cn`** —— 知识图谱与百科收录 ✅ 完成于 2026-05-02：[`techniques/knowledge-graph-cn.md`](./techniques/knowledge-graph-cn.md)（区分知识图谱与百科 + 6+ 大百科生态横向对照 + 训练 / RAG / KG 抽取三条传导路径 + 5 条元假说 + 3 个实验设计；强假说 E：维基中文"看得见够不着"，是 GEO 不可优化的硬基线）
  - [ ] **`exp-cn-baike-cross-llm-citation`** —— 4 大百科 × 5 大 LLM 引用率对照实验（验证元假说 B + C）
  - [ ] **`exp-cn-wiki-zh-fingerprint-passive`** —— 维基中文被动观察实验（验证元假说 A）
  - [ ] **`exp-cn-baike-serp-vs-llm-divergence`** —— 百度百科 SERP 特型卡 vs LLM 引用率双因变量观察（验证元假说 D）
  - [ ] **`tech-cn-vertical-wiki-and-domain-knowledge`** —— 垂类百科（萌娘 / MBA 智库 / 学术领域知识库等）横向对照
- [x] **`tech-prompt-level-seo`** —— prompt-level SEO 中文场景适用性 ✅ 完成于 2026-05-02：[`techniques/prompt-level-seo-cn.md`](./techniques/prompt-level-seo-cn.md)（澄清"prompt-level SEO 实质是用户问法覆盖" + 中英 prompt 结构差异 + 各 LLM tokenizer 公开度对照 + 5 条元假说 + 3 个实验设计；强假说 E：tokenizer 优化是伪需求）
  - [ ] **`exp-cn-faq-vs-keyword-density`** —— FAQ 多视角 vs 关键词高密度内容引用率对照（验证元假说 D，⭐⭐⭐ 最高）
  - [ ] **`exp-cn-jaccard-of-cited-sources-cross-llm`** —— 跨 LLM 信源池 Jaccard 对照（验证元假说 A，可从五大厂实验数据析出）
  - [ ] **`exp-cn-llm-query-rewrite-passive`** —— 被动观察 LLM query rewrite 行为（同 query 多次询问看答案差异）
  - [ ] **`tech-cn-long-tail-keyword-vs-prompt-variants`** —— 传统长尾关键词挖掘 vs prompt-level 变体覆盖方法论对比
- [x] **`tech-icp-and-subject`** —— 备案 / 主体认证对中文搜索 / LLM 可见性的影响 ✅ 完成于 2026-05-02：[`techniques/icp-and-subject-cn.md`](./techniques/icp-and-subject-cn.md)（拆 ICP / 行业资质 / 平台主体认证三套体系 + 因果链 5 段拆解 + 5 条元假说 + 3 个实验设计建议；强假说 C：算法备案与内容站 GEO 是类别错误）
  - [ ] **`exp-cn-icp-vs-overseas`** —— 境内备案 vs 境外服务器 vs 境外 + canonical 对照实验（验证元假说 A + D）
  - [ ] **`exp-cn-ymyl-license-impact`** —— YMYL 资质效应实验（可与 [`exp-cn-ymyl-cross-platform-citation`](#) 合并设计）
  - [x] **`tech-overseas-cn-deployment`** —— 境外品牌进中文 GEO 的部署路径 ✅ 完成于 2026-05-02：[`techniques/overseas-cn-deployment.md`](./techniques/overseas-cn-deployment.md)（5 种部署路径 A-E 横向对照 + 主体侧 / 内容侧两个独立维度 + 行业差异矩阵 + 5 条元假说 + 3 个实验设计；强假说 A：完全境外路径可见性低于代理备案路径一个量级；强假说 D：70% 隐性成本在内容审查不在技术部署）
    - [ ] **`exp-cn-overseas-path-a-vs-c-comparison`** —— 路径 A 完全境外 vs 路径 C 代理备案同品牌引用率对照（验证元假说 A）
    - [ ] **`exp-cn-overseas-medium-brand-roi-case-study`** —— 中型出海品牌 C+E 组合 vs D 单独 ROI 案例研究（验证元假说 B）
    - [ ] **`exp-cn-content-review-cost-quantification`** —— 出海品牌内容审查 + 合规适配成本量化（验证元假说 D）
    - [ ] **`tech-cn-cross-border-payment-and-conversion`** —— 跨境品牌支付通道 + 转化漏斗在中文 GEO 中的特殊性
    - [ ] **`tech-cn-foreign-licensed-isp-and-ymyl`** —— YMYL 类外资牌照获取的现状卡
- [x] **`tech-multimodal-cn`** —— 多模态信源在中文 LLM 中的采纳 ✅ 完成于 2026-05-02：[`techniques/multimodal-cn.md`](./techniques/multimodal-cn.md)（拆 4 类多模态信源 + 输入能力 vs 召回能力两套维度 + 6 大 LLM 对照 + 5 条元假说 + 3 个实验设计；强假说 D：图里文字 > alt 标签是中文场景反直觉的实操结论；强假说 C：视频字幕是中文场景被 LLM 召回最多的多模态信号）
  - [ ] **`glossary-add-multimodal`** —— glossary 新增 slug `multimodal`（走 PR）
  - [ ] **`exp-cn-image-alt-vs-no-alt`** —— 图片 alt A/B 对照实验（验证元假说 B：alt 边际效应接近 0）
  - [ ] **`exp-cn-content-format-comparison`** —— 同主题图文 vs 视频 vs 纯文本在生态内 vs 通用 LLM 引用率对照（验证元假说 A + C + E）
  - [ ] **`exp-cn-text-in-image-vs-out`** —— 图里文字 vs 图外文字对照实验（验证反直觉元假说 D）
  - [ ] **`tech-cn-asr-quality-divergence`** —— 中文 ASR 在不同视频平台的质量对照（事实层卡片）
- [x] **`tech-citation-attribution-styles`** —— 引用归因机制对比 ✅ 完成于 2026-05-02：[`techniques/citation-attribution-styles-cn.md`](./techniques/citation-attribution-styles-cn.md)（4 维分解 + 6 大中文 LLM × 英文基线横向表 + 信号价值 vs 回流价值两层模型 + 5 条元假说 + 3 个实验设计；强假说 A：中文 LLM 引用源 CTR < 1%；强假说 E：被引用对无品牌内容方是零价值事件）
  - [ ] **`exp-cn-llm-citation-source-ctr`** —— 中文 LLM 引用源 CTR 测量实验（验证元假说 A，**仓库商业价值最高实证**）
  - [ ] **`exp-cn-content-form-vs-citation-style`** —— 内容形态触发引用形态对照实验（验证元假说 B）
  - [ ] **`exp-cn-yuanbao-mp-soft-funnel`** —— 元宝公众号"软回流"路径观察实验（验证元假说 C）
  - [x] **`tech-cn-geo-roi-framework`** —— 中文 GEO ROI 评估框架 ✅ 完成于 2026-05-02：[`techniques/geo-roi-framework-cn.md`](./techniques/geo-roi-framework-cn.md)（投入 3 类 / 产出 3 类拆解 + ROI 计算 3 类常见错误 + 按主体类型差异化 ROI（中小 / 中型 / 大型 / 出海 / YMYL）+ 按行业差异化 ROI + 投入优先级排序含"不建议"清单 + 5 条元假说 + 3 个实验设计；强假说 C：机会成本是最常被服务商隐藏的项；强假说 A：中小新品牌中文 GEO ROI 结构性低于英文场景）
    - [ ] **`exp-cn-cross-language-roi-comparison`** —— 跨语言（中文 vs 英文）GEO ROI 对照（验证元假说 A）
    - [ ] **`exp-cn-account-ban-asset-discount`** —— 账号封禁的资产折现率量化（验证元假说 B）
    - [ ] **`exp-cn-equal-budget-channel-comparison`** —— 等预算 GEO vs 短视频带货对照（验证元假说 C，⭐⭐⭐ 仓库 GEO ROI 决定性实证）
    - [ ] **`tech-cn-channel-mix-strategy`** —— 把 GEO 放在完整营销 mix（短视频 / 直播 / 私域 / 信息流 / 线下）中的位置评估
- [x] **`tech-dimension-map-cn`** —— 技术主题卡片维度索引地图 ✅ 完成于 2026-05-02：[`techniques/dimension-map-cn.md`](./techniques/dimension-map-cn.md)（元卡，14 张技术卡 × 8 维度图谱显式化 + 卡间关系图 + 强假说集 + 服务商话术索引 + 主体决策索引 + 空缺维度 + 4 类读者阅读路径 + 新卡扩展原则）
- [x] **`tech-cn-geo-demand-side-fitness`** —— GEO 需求侧场景适配地图 ✅ 完成于 2026-05-03：[`techniques/geo-demand-side-fitness-cn.md`](./techniques/geo-demand-side-fitness-cn.md)（**仓库第一张需求侧卡 / D0 前置维度**，三层拆解 + 4 类窄场景识别 + 5 条元假说 + 2 个实验设计 + 与服务商客户画像话术对照）

### 接续需求侧卡的衍生（priority: medium-high）

> 来源：[`techniques/geo-demand-side-fitness-cn.md`](./techniques/geo-demand-side-fitness-cn.md) 第 IX 节衍生 BACKLOG 建议 + [`docs/meeting-2026-05-03-geo-demand-and-business-model.md`](./docs/meeting-2026-05-03-geo-demand-and-business-model.md) 第 8 节行动项。

- [x] **`tech-cn-geo-business-model-taxonomy`** —— GEO 商业模式七层分类卡 ✅ 完成于 2026-05-03：[`techniques/geo-business-model-taxonomy-cn.md`](./techniques/geo-business-model-taxonomy-cn.md)（**仓库第一张供给侧卡 / DS 维度**，七层 × 6 维度 + 投入产出结构 + 平台原生功能取代风险三个独立切片 + 6 条元假说 + 2 个实验设计 + 衍生 BACKLOG 8 条）
- [ ] **`tech-cn-geo-source-pool-density`** —— 信源池占有率密度卡（探词们的真实护城河，仓库当前结构空白）。讨论"在多少家被收录的站上铺多少量才能影响 LLM"的密度问题。是 [`private-vs-public-source-cn.md`](./techniques/private-vs-public-source-cn.md) 的供给量级补充。
- [ ] **`tech-cn-llm-vs-traditional-search-decision-funnel`** —— LLM 与小红书 / 淘宝 / 抖音 / 美团 / 朋友推荐的决策漏斗位置对比卡。无需新数据，可基于现有公开报告 + 仓库元假说衍生。
- [ ] **`tech-cn-ymyl-llm-trust-temporal`** —— YMYL 场景 LLM 信任度纵向跟踪卡（健康 / 法律 / 财务用户警惕度可能波动，需要周期数据）。
- [ ] **`tech-cn-geo-target-segment-by-industry`** —— 按行业的 GEO 目标客户分层卡（与需求侧卡 2.3 节衔接，为各 GEO 商业模式提供"哪个行业的什么角色是真买家"的清单）。
- [x] **`update-dimension-map-three-axis`** —— 把 [`dimension-map-cn.md`](./techniques/dimension-map-cn.md) 的 8 维度结构升级为 **D0（需求侧前置）+ D1-D8（信号侧）+ DS（供给侧 / 商业模式侧）** 的三轴结构。✅ 完成于 2026-05-03：dimension-map 376 → 487 行，元假说总数 68 → 79，强假说集 4.1 新增 5 条 ⭐⭐⭐，话术索引新增 ≥ 8 条，主体路径全部加 D0 前置 + 新增 GEO 服务商路径。
- [ ] **`tech-cn-7w-media-channel-classification`** —— 把"7 万+ 媒体发布渠道"按"百度收录站 / 公众号 / 知乎 / 小红书 / B 站 / 自建网站"分类，作为 [`private-vs-public-source-cn.md`](./techniques/private-vs-public-source-cn.md) 的具体落地补充。来源：探词手册 p13。
- [ ] **`exp-cn-source-flooding-ab-vs-citation-rate`** —— A/B 实验：同 query 同时间段，监测铺量前 vs 铺量后 4 周引用差异。**采购一次 RaaS 服务**作为实验输入。资金依赖（≥ ¥1 万）+ 流程合规依赖。

### 接续供给侧卡的衍生（priority: medium-high）

> 来源：[`techniques/geo-business-model-taxonomy-cn.md`](./techniques/geo-business-model-taxonomy-cn.md) 第 IX 节衍生 BACKLOG 建议。

- [ ] **`exp-cn-llm-platform-ad-slot-monitor`** —— ⭐⭐⭐ 6 大平台广告位上线监控（豆包 / 元宝 / 千问 / 文心 / Kimi / 小红书问一问）。**🔄 2026-05-04 升级**为 [`exp-cn-llm-platform-4-monetization-form-monitor`](./BACKLOG.md)（见下条）——单押"广告位"形态被审计证伪，监测应扩为 4 形态。原项保留作认知演化痕迹。
- [ ] **`exp-cn-llm-platform-4-monetization-form-monitor`** —— ⭐⭐⭐ 6 大平台 **4 形态平台变现监控**（订阅制 / 电商佣金 / 自建品牌方监测后台 / API 收费）。验证供给侧元假说 A 升级版。每形态分别监测信号：（1）订阅版用户数披露 + 答案质量分层；（2）答案体中商品卡频率 + 平台抽佣率；（3）官方"商家品牌可见度查询"模块；（4）API 公开定价 + 企业调用量披露。可与 [`tools/exp-doubao-vs-deepseek-paired/`](./tools/exp-doubao-vs-deepseek-paired/) 监测系统集成扩展。低成本（自建爬虫 + 公开物料追踪）。
- [ ] **`exp-cn-geo-vendor-revenue-structure`** —— ⭐⭐ 5 家 GEO 公司收入构成反推（看融资 PR / 招聘 JD / 案例文章 / 媒体访谈）。验证元假说 B：多数所谓 SaaS 实际主收入仍是 RaaS。人力 ≈ 8-15 小时（全公开信息）。
- [x] **`tech-cn-anti-geo-monitoring`** —— ⭐⭐⭐ 反 GEO 监测专题卡 ✅ 完成于 2026-05-03：[`techniques/anti-geo-monitoring-cn.md`](./techniques/anti-geo-monitoring-cn.md)（**DS 元假说 C 具体展开 / DS 维度首张子卡**，386 行，4 类需求拆解 + 客户决策人/预算/心理对照 + 与传统舆情监测技术差异 + 各 LLM 平台监测难度 + 7 条元假说 + 3 个实验设计 + 衍生 BACKLOG 7 条）

### 接续 2026-05-04 元假说审计的衍生（priority: medium-high）

> 来源：[`audits/2026-05-04_meta-hypothesis-audit.md`](./audits/2026-05-04_meta-hypothesis-audit.md) 第四节"新发现的研究空白"。

- [x] **`tech-cn-mofusoft-tgeo-reverse-engineering`** —— ⭐⭐⭐ 迈富时（02556.HK）港股年报反工程 **第一阶段（2026-05-04）✅**：[`case-studies/mofusoft-tier1-reverse-engineering-2026-05.md`](./case-studies/mofusoft-tier1-reverse-engineering-2026-05.md)（约 2 小时人力，6 个 A 级信源，281 行）。**关键修正**：审计 brief "T-GEO™ 五层认知架构 / 21 万企业客户 / 千亿参数 / 7 年 IDC 第一" 多项数据需修正——实际是"AI-Agentforce 智能体中台 + 四层架构 / 2.7 万企业客户 / 参数量未公开 / 6 年 AI SaaS 第一"。修正不影响 Tier 1 整体判断。剩余第二阶段（6-13 小时）见下条。
- [ ] **`tech-cn-mofusoft-tgeo-reverse-engineering-phase2`** —— ⭐⭐ E1 第二阶段（剩余 6-13 小时人力 / ¥0 现金）：完整年报正文阅读 + 关联方交易公告 + 投资者关系活动记录 + Q1-Q3 季报对照 + 与销售物料的术语口径对照。建议下一阶段在仓库实地 pilot 实验后启动。
- [ ] **`tech-cn-mofusoft-anti-geo-monitoring-product-watch`** —— 监测迈富时是否上线反 GEO 监测产品（连接 [`anti-geo-monitoring-cn.md`](./techniques/anti-geo-monitoring-cn.md)）。
- [ ] **`exp-cn-mofusoft-acquisition-tracker`** —— 跟踪迈富时 2025-2026 并购公告（验证 [`geo-industry-stratification-cn.md`](./techniques/geo-industry-stratification-cn.md) 元假说 C "尾部玩家被并购"）。计划 2025 内完成 ≥ 2 宗。
- [ ] **`tech-cn-tier1-vendor-jargon-reconciliation`** —— 头部公司销售物料 vs 财报披露的术语对照（"21 万 vs 2.7 万" / "千亿参数 vs 未公开" / "T-GEO 五层 vs AI-Agentforce 四层" 等偏差源头分析）。是仓库识别"反尾部 SEO 软文型话术 vs 头部销售物料"差异的方法学卡。
- [ ] **`tech-cn-percent-national-standard-path`** —— ⭐⭐ 百分点科技参与 40 项国标的具体路径调研。识别百分点参与的 GEO 相关国标（信通院《GEO 服务可信基本要求》是否包括）+ CMMI 5 / ISO20000 在 GEO 服务可信认证中的位置 + 党校案例库具体内容。验证 DS 元假说 D（标准协议层最高 ROI 位置）的具体推动方。
- [ ] **`tech-cn-zhitui-customer-portrait-deep-dive`** —— ⭐⭐ 智推时代客户画像深挖（三七互娱 / 作业帮 / 小鹏 / 理想 + 入选艾瑞 2026 GEO 行业研究报告 + 进天津商业大学新工科课程）。验证 D0 元假说 C 修订方向——头部 / 腰部 GEO 公司宽客户画像是大客户密度的反映而非销售勉强匹配。
- [ ] **`tech-cn-geo-industry-cr5-tracker`** —— 行业 CR5 集中度纵向跟踪（艾瑞 2026 Q1 已达 62.3%）。预期 2-3 年内并购窗口打开——头部上市公司（迈富时 / 蓝色光标系 / 三七互娱系）可能横向并购腰部创业 GEO 公司。
- [ ] **`tech-cn-platform-insider-startup-pattern`** —— "平台内部人 + 上市投资"创业模式专题（PureblueAI 清蓝 = 前豆包市场负责人 + 蓝色光标领投是新现象）。仓库假说未覆盖此类组合。

### 接续反 GEO 监测卡的衍生（priority: medium-high）

> 来源：[`techniques/anti-geo-monitoring-cn.md`](./techniques/anti-geo-monitoring-cn.md) 第 IX 节衍生 BACKLOG 建议。

- [ ] **`exp-cn-anti-geo-buyer-interview`** —— ⭐⭐⭐ E1 上市公司公关 / 法务 / 舆情监测总监访谈（≥ 10 家），半结构化覆盖：当前 AI 监测视野 / 已发生的 AI 幻觉/舆情扩散事件 / 预算分配 / 决策路径 / 付费意愿。验证元假说 A、B。预算 ¥0.5-3 万。
- [ ] **`exp-cn-llm-hallucination-rate-ymyl-vs-non`** —— ⭐⭐ E2 YMYL（医疗/法律/金融）vs 非 YMYL 类 LLM 幻觉率对照（6 平台 × 100 query × 3 次重复 + 人工标注）。验证元假说 D 监管驱动假设。可与 [`tools/exp-doubao-vs-deepseek-paired/`](./tools/exp-doubao-vs-deepseek-paired/) 数据采集流程复用。
- [ ] **`exp-cn-cross-llm-answer-consistency`** —— ⭐⭐ E3 跨 LLM 答案一致性指数测量（50 query × 6 平台 × 5 次 × Jaccard / 编辑距离 / NLI 三种指数）。验证元假说 E 跨 LLM 监测技术壁垒。
- [ ] **`tech-cn-llm-platform-brand-console-watch`** —— LLM 平台是否上线"品牌方监测后台"监控（元假说 G）。可与 [`exp-cn-llm-platform-ad-slot-monitor`](./BACKLOG.md) 监测系统集成。
- [ ] **`tech-cn-ai-hallucination-compliance-mapping`** —— AI 幻觉合规要求映射（《生成式人工智能服务管理办法》后续配套细则跟踪）；YMYL 行业被罚案例收集。
- [ ] **`tech-cn-anti-geo-vendor-landscape`** —— 已有"伪反 GEO 监测" 厂商盘点（探词 + 蜂鸟 / 海纳 / 鹰眼 / 慧科 等传统舆情厂商对照）。
- [ ] **`tech-cn-geo-vs-anti-geo-comparison`** —— 进攻型 vs 防御型 GEO 系统对比卡（DS 子卡积累 ≥ 3 张后启动）。
- [ ] **`tech-cn-geo-training-certification-landscape`** —— 培训认证赛道现有玩家盘点 + 入场门槛分析（元假说 E 合法暴利）。SEO 行业类比 + 1-3 年市场扩张预期。
- [ ] **`tech-cn-llms-txt-chinese-promoter-watch`** —— 中文 llms.txt / AI provenance 推动方监测（元假说 D 长期最高 ROI 位置）。当前空白本身可能就是机会。
- [ ] **`tech-cn-vertical-vs-generic-geo-survival-tracker`** —— 垂直陪跑 vs 通用 GEO 公司存活率纵向跟踪（元假说 F）。需 3-5 年观察。
- [ ] **`tech-cn-vendor-pitch-pattern-library`** —— 多份 GEO 服务商话术对比库（基于 case-studies 积累 ≥ 3 份后启动；当前仅探词 1 份）。

---

## 🔧 工具评测占位（priority: low）

国内 GEO 服务商 / 监测工具，先建 stub 卡片（标 `verified: false`），等实测后填充：

- [ ] **`tool-chuanshenggang-geo`** —— 传声港 GEO（多个 GEO 服务商榜单中常见）
- [ ] **`tool-chuanxinshe`** —— 传新社
- [ ] **`tool-guaishou-geo`** —— 怪兽智能 GEO
- [ ] **`tool-sheepgeo`** —— SheepGeo（国内 GEO 监测工具）
- [ ] **`tool-foglift`** —— Foglift（含 MCP server）
- [ ] **`tool-otterly-cn-test`** —— Otterly.AI 在国内平台支持度评测
- [ ] **`tool-profound-cn-test`** —— Profound 在国内平台支持度评测
- [ ] **`tool-geo-aeo-tracker`** —— danishashko/geo-aeo-tracker 自部署评测
- [ ] **`tool-auriti-geo-optimizer`** —— Auriti-Labs/geo-optimizer-skill 评测
- [ ] **`tool-onvoyage-skills`** —— onvoyage-ai/gtm-engineer-skills 评测

---

## 📚 资源 / 文档完善（priority: low）

- [ ] **`docs-doubao-changelog`** —— 创建 [`platforms/doubao/changelog.md`](./platforms/doubao/changelog.md)，追踪豆包平台规则 / 功能变更
- [ ] **`docs-deepseek-changelog`** —— DeepSeek changelog
- [ ] **`docs-resources-people`** —— [`resources/people.md`](./resources/people.md) 创建，追踪值得关注的中文 GEO/SEO 从业者
- [ ] **`docs-resources-official-docs`** —— [`resources/official-docs.md`](./resources/official-docs.md) 创建，整合各平台官方文档链接索引
- [ ] **`docs-resources-courses`** —— [`resources/courses.md`](./resources/courses.md) 国内付费 GEO 课程评测（披露利益关系）
- [ ] **`docs-glossary-update-cycle`** —— glossary 维护节奏（每季度回看）

---

## 🔬 元问题 / 方法学（priority: medium）

- [ ] **`meta-experiment-tooling`** —— 选定实验执行的工具栈：手动 / Playwright / 抓包脚本 / 第三方监测工具的取舍
- [ ] **`meta-data-storage`** —— 实验原始数据存放策略（gist / 仓库内 / 外部 S3 + 校验和）
- [ ] **`meta-confidence-calibration`** —— 跨条目的 `confidence` 评级标准是否需要统一定义、量化
- [ ] **`meta-platform-changelog-pipeline`** —— 各平台 changelog 的采集机制（人工 vs 自动）

---

## 转 issue 时的 label 建议

| BACKLOG 分类 | 建议 GitHub label |
|--------------|--------------------|
| 实验 | `experiment`, 关联平台 label（`platform:doubao` 等） |
| 平台调研 | `platform`, 关联 slug |
| 技术主题 | `technique`, 关联标签 slug |
| 工具评测 | `tool-review` |
| 资源 / 文档 | `docs` |
| 元问题 | `meta` |

优先级：`priority:high` / `priority:medium` / `priority:low`。
