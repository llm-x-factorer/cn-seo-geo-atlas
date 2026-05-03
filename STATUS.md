# 项目当前进度

> 最后更新：2026-05-03（含 2026-05-02 完整产出 + 2026-05-03 文档同步与首次 git 初始化）
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

**仓库三大卡住点**（按优先级）：

1. **第一个实验未跑过**：[`tools/exp-doubao-vs-deepseek-paired/`](./tools/exp-doubao-vs-deepseek-paired/) 工具栈就绪，selector 标 `# TODO: pilot-verify`，等待人工 pilot
2. **五大厂实验未启动**：设计完成，依赖第一个实验跑通后才能启动；需要 3 个新 adapter（wenxin / qianwen / yuanbao）
3. **大量元假说未实证**：14 张技术主题卡共 68 条元假说全部 `concept`，需要数据回写

距离"产出第一个一手研究结论"还差：

1. **selector pilot 验证**（30-60 分钟）—— 需要真实账号 + 浏览器
2. **pilot run**（10 次采集）—— 端到端验证脚本
3. **主实验执行**（320 次采集 × 3 天）
4. **score + analyze**（30 分钟）
5. **回写结果**到 [`platforms/doubao/citation-mechanism.md`](./platforms/doubao/citation-mechanism.md) 假说一、[`platforms/deepseek/citation-mechanism.md`](./platforms/deepseek/citation-mechanism.md) 假说一/二、[`techniques/princeton-9-strategies-cn.md`](./techniques/princeton-9-strategies-cn.md) 元假说 B/D

> 上述 1-3 步只能由用户做（账号 + 网络环境）。Claude 可以协助 selector 调试、数据分析、回写。

## 下一步候选方向（按优先级）

1. **A. 跑第一个实验 pilot**（最高 ROI 仍然不变）—— 用户人工 + Claude 协助调 selector，产出第一份真实数据
2. **B. 平台 changelog 系列起手** —— 写 [`docs-doubao-changelog`](./BACKLOG.md) 建立 changelog 卡片模式，作为后续各平台 changelog 范本（豆包 / DeepSeek / 文心 / 千问 / 元宝 / 百度 / 小红书）
3. **C. 继续铺技术主题** —— [`tech-cn-channel-mix-strategy`](./BACKLOG.md)（接 GEO ROI 框架的 mix 视角）/ [`tech-cn-corporate-knowledge-geo`](./BACKLOG.md)（企业内部知识库 GEO 专题）/ [`tech-cn-anti-monopoly-and-geo-roadmap`](./BACKLOG.md)（接 platform-search-blockade 衍生）/ [`tech-cn-llm-crawler-ua-registry`](./BACKLOG.md)（接 llms.txt 卡衍生）
4. **D. 工具评测占位** —— 国内 GEO 服务商（传声港 / 怪兽智能 / 传新社 / SheepGeo / Foglift）建 stub 卡片
5. **E. push 到 GitHub + BACKLOG → issue 转换** —— 仓库迁移到协作模式
6. **F. 设计第三个实验** —— 例如 [`exp-cn-ymyl-cross-platform-citation`](./BACKLOG.md)（验证 E-E-A-T 卡片元假说 C：YMYL 类全平台趋同）

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

66 个（含 11 个 Python/YAML 工具文件 + 1 个 .gitignore + 1 个项目级 [`CLAUDE.md`](./CLAUDE.md)）

```
$ find . -type f \( -name "*.md" -o -name "*.py" -o -name "*.yaml" -o -name "*.txt" \) | grep -v __pycache__ | wc -l
66
```
