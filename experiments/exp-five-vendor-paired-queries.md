---
title: 五大厂配对引用源分布实验（v1，仓库终极实证目标）
type: experiment
sources: []
confidence: high
verified: false
last_verified: null
platforms:
  - doubao
  - deepseek
  - wenxin
  - qianwen
  - yuanbao
techniques:
  - llm-citation
  - citation-attribution
  - geo-experiment
hypothesis: |
  在中文 GEO 场景下，每家主流生成式引擎对**自家生态信源**的引用比例显著高于其他四家对同一生态的引用比例（差异 ≥ 20 个百分点）。即：豆包→字节系，文心→百度系，元宝→腾讯系，千问→阿里系，DeepSeek→技术社区。该假说一旦在严格控制下成立，即为"中文 GEO 必须按平台分流策略"的核心实证支撑。
maturity: concept
run_date:
  start: TBD（依赖五端账号 + 工具栈扩展 + 第一个实验跑通）
  end: TBD
sample_size: 32 query × 5 重复 × 5 平台 = 800 次采集
controls:
  - 同 query 集（query-set-v1 子集）
  - 同采集时段窗口（连续 3 天 × 3 时段）
  - 同地理位置（中国大陆，固定省份）
  - 同账号类型（新建匿名 / 未登录 Web 会话）
  - 同设备 / 浏览器（Playwright + Chromium）
  - 联网搜索：所有平台**启用联网**（避免 5 平台 × 2 联网状态 × 32 query × 5 重复 = 1600 的爆炸样本量；联网状态作为单独 v2 实验拆出去）
reproducibility: medium
query_set: query-set-v1
related:
  - ./methodology.md
  - ./query-set-v1.md
  - ./exp-doubao-vs-deepseek-paired.md
  - ../platforms/doubao/citation-mechanism.md
  - ../platforms/deepseek/citation-mechanism.md
  - ../platforms/wenxin/citation-mechanism.md
  - ../platforms/qianwen/citation-mechanism.md
  - ../platforms/yuanbao/citation-mechanism.md
  - ../techniques/princeton-9-strategies-cn.md
last_updated: 2026-05-02
---

# 五大厂配对引用源分布实验（v1，仓库终极实证目标）

> ⚠️ **实验状态**：**设计完成、工具未写、未执行**。本文档完成实验设计与协议；执行前置依赖：
>
> 1. 五端账号（豆包 / DeepSeek / 文心 / 千问 / 元宝 Web 端）
> 2. 工具栈扩展（在 [`tools/exp-doubao-vs-deepseek-paired/`](../tools/exp-doubao-vs-deepseek-paired/) 基础上新增 3 个 adapter）
> 3. **第一个实验（exp-doubao-vs-deepseek-paired）已跑通**——验证方法学和工具栈在 2 平台上可行后再放大到 5 平台
>
> **价值定位**：仓库的**终极实证目标**。第一个实验（双平台）回答"豆包和 DeepSeek 是否在引用源结构上有差异"；本实验回答**更核心的问题**——"中文 GEO 的'按平台分流'主张是否在五大厂上普遍成立"。如果 H1 成立，仓库的核心论点（"中文 GEO 不存在统一最佳实践"）首次得到一手数据支撑；如果 H1 被证伪，仓库要重新组织叙事。

## 一、假设

### 主假设（H1）—— "生态偏好普遍性" 假设

> 每家中文主流生成式引擎对**自家生态信源**的引用比例**显著高于**其他四家对同一生态的引用比例，每个配对差异 **≥ 20 个百分点**。

具体五条配对：

| 平台 | 自家生态信源 | 配对方 | 预期方向 |
|------|------------|--------|---------|
| 豆包 | `bytedance-eco`（头条 / 抖音百科 / 抖音视频转写 / 西瓜 / 快懂） | 其他 4 平台 | 豆包 ≥ 其他平台 + 20pp |
| 文心 | `baidu-eco`（百家号 / 百度百科 / 百度知道 / 百度文库 / 百度健康） | 其他 4 平台 | 文心 ≥ 其他平台 + 20pp |
| 元宝 | `tencent-eco`（微信公众号 / 视频号 / 知乎专栏） | 其他 4 平台 | 元宝 ≥ 其他平台 + 20pp |
| 千问 | `alibaba-eco`（淘宝 / 天猫 / 阿里云 / 闲鱼 / 夸克 / 阿里妈妈站） | 其他 4 平台 | 千问 ≥ 其他平台 + 20pp |
| DeepSeek | **无自家内容生态**——以"技术社区"作为代理（CSDN / GitHub / Stack Overflow 中文 / 知乎技术问答 / 稀土掘金） | 其他 4 平台（仅技术 query 类型上） | DeepSeek ≥ 其他平台 + 20pp |

H1 整体成立条件：**5 条配对中至少 4 条独立成立**，且没有任何一条出现"反向显著"（自家平台引用率比其他平台**低 20pp 以上**）。

### 副假设（H2）—— DeepSeek 技术社区强偏好

> 在**技术类 query**（`tech-XX`）上，DeepSeek 对技术社区（`tech-community`）的引用比例显著高于豆包 / 文心 / 千问 / 元宝四平台中**任意一家**，差异 ≥ 20 个百分点。

H2 是 H1 中"DeepSeek 配对"在技术 query 子集上的强化版本——技术 query 是 DeepSeek 的强项域，差异预期最显著。

### 副假设（H3）—— 千问电商场景强偏好

> 在**电商类 query**（`comm-XX`）上，千问对 `alibaba-eco` 的引用比例显著高于其他四平台对同一生态的引用比例，差异 ≥ 30 个百分点。

H3 阈值（30pp）比 H1（20pp）更严——电商 query 是千问的强主张域，预期差异更显著。如果连这都不成立，"千问的电商强项"假说要被严重削弱。

### 元假设回写

实验结果将回写到：

- [`techniques/princeton-9-strategies-cn.md`](../techniques/princeton-9-strategies-cn.md) **元假说 B**（生态内信源 > 生态外权威信源）—— **决定性数据点**
- [`techniques/princeton-9-strategies-cn.md`](../techniques/princeton-9-strategies-cn.md) **元假说 D**（query 类型对策略生效有强调节作用）—— H2/H3 验证
- 各 [`platforms/<slug>/citation-mechanism.md`](../platforms/) 假说一全部升级 / 证伪
- 仓库 [`README.md`](../README.md) 中"中文 GEO 不存在统一最佳实践"主张获得首个一手实证支撑

## 二、可证伪条件（pre-registration）

为避免确认偏差，预先声明以下情形为**证伪 / 弱效应**：

### H1 整体证伪条件

- **强证伪**：5 条配对中 ≥ 3 条出现"差异 < 5pp"或"反向"——证伪"按平台分流"普遍主张
- **弱证伪**：5 条配对中恰好 2 条出现"差异 < 5pp"——H1 部分成立，仓库主张需要修订为"按平台分流仅在 X 平台成立"
- **支持**：5 条配对中 ≥ 4 条出现"差异 ≥ 20pp"，且无反向

### H2 证伪条件

- DeepSeek 对技术社区引用比例 与 其他四平台中**最高的一家**对技术社区引用比例 **差异 < 5pp**

### H3 证伪条件

- 千问对 `alibaba-eco` 引用比例 与 其他四平台中**最高的一家** **差异 < 5pp**

**任何介于 5-20pp（H1/H2）或 5-30pp（H3）之间的差异**——记为"弱效应"，不支持也不证伪强假设；后续需要更大样本量。

> ⚠️ **预注册阈值（一旦写定不能事后改）**：`H1_DIFF_THRESHOLD_PP = 20`、`H2_DIFF_THRESHOLD_PP = 20`、`H3_DIFF_THRESHOLD_PP = 30`、`WEAK_DIFF_PP = 5`。这些值已在第一个实验（exp-doubao-vs-deepseek-paired）的 `analyze.py` 中编码，本实验复用相同的 H1/H2 阈值。H3 是新增阈值，工具栈扩展时编码。

## 三、自变量、因变量、控制变量

### 自变量

- **平台**：豆包 / DeepSeek / 文心 / 千问 / 元宝（5 levels）
- **query 类型**：决策 / 知识 / 技术 / 资讯 / 电商（5 levels）

设计：5 × 5 = **25 子组**，每组 ≈ 6-7 query × 5 重复 ≈ 32-35 次采集。

> **不在自变量中的维度**：联网搜索状态。理由：本实验全部启用联网搜索；"联网开 / 关对引用源结构的影响"作为 v2 实验拆出去，避免样本量爆炸（2× 维度即从 800 → 1600）。

### 因变量（主指标）

- **信源类别分布**：每次回答中引用源被分类为以下类别之一的频次

| 类别 slug | 含义 | 关联平台预期 |
|----------|------|-------------|
| `bytedance-eco` | 头条 / 抖音百科 / 抖音视频 / 西瓜 / 快懂 | 豆包 ↑ |
| `baidu-eco` | 百家号 / 百度百科 / 百度知道 / 百度文库 / 百度健康 | 文心 ↑ |
| `tencent-eco` | 微信公众号 / 视频号 / 知乎专栏 / 腾讯新闻 | 元宝 ↑ |
| `alibaba-eco` | 淘宝 / 天猫 / 阿里云 / 闲鱼 / 夸克 / 阿里妈妈站 | 千问 ↑ |
| `news-portal` | 新浪 / 网易 / 搜狐 / 凤凰网（综合门户，非生态系） | 中性基线 |
| `tech-community` | CSDN / 知乎技术问答 / GitHub / Stack Overflow 中文 / 稀土掘金 | DeepSeek ↑ |
| `vertical-media` | 36 氪 / 虎嗅 / 钛媒体 / 丁香园 / 站长之家 | 中性 |
| `central-media` | 人民网 / 新华网 / 央视网 / 央广网 / 光明网 | YMYL 类预期 ↑ |
| `local-media` | 地方党媒 / 地方新闻网 | 本地类预期 ↑ |
| `gov-edu` | `*.gov.cn` / `*.edu.cn` / `*.cas.cn` / `*.cssn.cn` | YMYL 类预期 ↑ |
| `xiaohongshu` | 小红书笔记 | 美妆 / 决策类预期 ↑ |
| `wikipedia-zh` | 维基百科中文 | 知识类预期 ↑ |
| `other` | 其他 | — |

> **vs 第一个实验的差异**：新增 `alibaba-eco`（v1 未独立分类，散在 `other`）。归类规则需要在工具栈中扩展，详见后文"评分 rubric"。

### 因变量（次指标）

- **引用源排名**：在引用列表中的位置（如平台展示引用源列表）
- **每答案引用源数量**：平均每次回答中显示的引用源数（**已知差异大**：豆包 / 元宝 多源卡片化、DeepSeek 行内编号、文心 5.0 全模态卡片）
- **引用准确性**：抽样 5%（800 × 5% = 40 条）人工核对引用源内容是否被准确转述（0 = 错误 / 1 = 部分 / 2 = 准确）

### 控制变量

- 时间窗口：连续 3 天 × 3 时段（10:00-12:00 / 14:00-16:00 / 19:00-21:00）
- 地理位置：中国大陆 IP，固定省份（实验数据中记录）
- 账号：每平台**新建匿名账号或未登录 Web 会话**（5 平台分别独立账号，不复用、不交叉登录）
- 设备 / 浏览器：Playwright + Chromium，UA 一致
- 会话：每次 query **新会话 + 清空历史**

### 已知混杂变量（标注）

- **平台个性化推送**：5 平台对账号 / IP 的策略不同——元宝因为微信生态可能更敏感
- **平台 A/B 测试**：实验期间任一平台都可能改 UI / 模型——记录每次采集的平台版本号 + 模型标识
- **联网检索的实时性**：3 天 × 3 时段采样平均掉
- **多模型路由**（元宝 / DeepSeek 特有）：元宝多模型路由、DeepSeek R1/V 切换——记录每次回答的模型标识
- **千问"AI 下单"路径触发**：电商 query 可能触发千问的下单路径，UI 与普通回答不同——**单独标记**这类回答（不剔除，但分析时单独看）
- **文心 5.0 全模态**：可能引用图片 / 视频信源——本实验只统计文本类引用源

## 四、Query 集

从 [`query-set-v1.md`](./query-set-v1.md) 中**选取 32 个 query**：

### 决策类（8 个）

`dec-01` `dec-02` `dec-03` `dec-05` `dec-06` `dec-08` `dec-09` `dec-10`

### 知识类（8 个）

`know-01` `know-02` `know-03` `know-05` `know-06` `know-07` `know-09` `know-10`

### 技术类（6 个，重点验证 H2）

`tech-01` `tech-02` `tech-03` `tech-05` `tech-07` `tech-09`

### 资讯类（4 个，对照基线）

`info-03` `info-06` `info-08` `info-09`

### 电商类（6 个，重点验证 H3）

`comm-01` `comm-03` `comm-04` `comm-05` `comm-06` `comm-10`

> **不包含**：
> - YMYL 类（合规风险，单独走 [`exp-five-vendor-ymyl`](../BACKLOG.md) 计划）
> - 本地服务类（与 LBS 实验绑定，需要固定地理位置严控）
> - 创意 / 闲聊类（弱 RAG 或无 RAG，引用源数据稀疏）
> - **AI 下单**强触发 query（`comm-07` / `comm-08` / `comm-09`）：千问会进入交易闭环 UI，与普通问答路径差异过大，单独走 [`exp-qianwen-commerce-geo`](../BACKLOG.md)

## 五、数据采集协议

### 工具栈

- **浏览器自动化**：Playwright（Python）+ Chromium
- **采集脚本**：复用 [`tools/exp-doubao-vs-deepseek-paired/collect.py`](../tools/exp-doubao-vs-deepseek-paired/) 框架；**新增三个 adapter**：
  - `wenxin_adapter.py`（标 `# TODO: pilot-verify`，待真实 UI 验证）
  - `qianwen_adapter.py`（标 `# TODO: pilot-verify`）
  - `yuanbao_adapter.py`（标 `# TODO: pilot-verify`）
- **source_classifier.py 扩展**：新增 `alibaba-eco` 归类规则（淘宝 / 天猫 / 阿里云 / 闲鱼 / 夸克 / 1688 / 阿里妈妈系列子域）
- **数据存储**：JSON 格式，每次采集为一条记录

> **强约束**：5 个 adapter 全部完成 selector pilot 验证后才能跑主实验。**第一个实验的 selector 验证经验直接复用**——豆包 / DeepSeek 已验证的部分不重做。

### 采集时段（3 天 × 3 时段）

| Day | 时段 1 | 时段 2 | 时段 3 |
|-----|--------|--------|--------|
| Day 1 | 10:00-12:00 | 14:00-16:00 | 19:00-21:00 |
| Day 2 | 同上 | 同上 | 同上 |
| Day 3 | 同上 | 同上 | 同上 |

每个 query 在 9 个时段中随机选 5 个（避免时段聚集）。

### 单次采集步骤

每平台的步骤复用第一个实验，5 平台并行 / 串行的取舍：

- **建议串行**（按平台一台台跑）：避免 IP 风控同时触发 5 平台
- **平台间间隔**：≥ 60 秒（高于第一个实验的 30 秒，因 5 平台间相互不干扰但需要预留浏览器启动 / 关闭时间）

### 数据记录字段（在第一个实验基础上扩展）

```json
{
  "experiment_id": "exp-five-vendor-paired-v1",
  "platform": "doubao | deepseek | wenxin | qianwen | yuanbao",
  "query_id": "dec-01",
  "query_text": "...",
  "query_type": "decisional | knowledge | technical | informational | commerce",
  "online_search_enabled": true,
  "model_id": "doubao-pro | deepseek-r1 | wenxin-5.0 | qwen-max | yuanbao-deepseek-r1 | ...",
  "platform_version": "...",
  "session_id": "...",
  "timestamp": "2026-XX-XX 14:30:00 +08:00",
  "geo_ip_province": "...",
  "raw_response_text": "...",
  "citation_sources": [
    {"rank": 1, "title": "...", "url": "..."},
    {"rank": 2, "title": "...", "url": "..."}
  ],
  "screenshot_path": "data/screenshots/...",
  "response_time_ms": 12345,
  "qianwen_commerce_path_triggered": false,
  "yuanbao_routed_to_model": "deepseek-r1 | hunyuan | ..."
}
```

## 六、评分 rubric（前定义）

### 信源类别归类规则（在第一个实验基础上扩展）

新增 `alibaba-eco` 归类：

| URL 模式 | 类别 |
|----------|------|
| `*.taobao.com`, `*.tmall.com`, `*.aliyun.com`, `*.alimama.com`, `*.1688.com`, `*.xianyu.com`, `*.quark.cn`, `developer.aliyun.com`, `help.aliyun.com` | `alibaba-eco` |

其他 11 类归类规则**完全复用**第一个实验，详见 [`exp-doubao-vs-deepseek-paired.md`](./exp-doubao-vs-deepseek-paired.md) 第六节。

**边界规则更新**（按优先级排序）：

```
gov-edu > central-media > local-media >
{bytedance-eco / baidu-eco / tencent-eco / alibaba-eco}（生态系优先级相同，URL 各占其域）>
vertical-media > news-portal > tech-community > xiaohongshu > wikipedia-zh > other
```

知乎细分仍然适用：`/question/` → `tech-community`；`zhuanlan.zhihu.com` → `tencent-eco`。

### 主指标计算

对每个（平台 × query 类型）组合，计算每类信源的占比：

```
比例(类别 C, 平台 P, query 类型 T) = (P × T 下类别 C 出现的总频次) / (P × T 下所有引用源总频次)
```

**H1 验证条件（按平台展开）**：

```
H1.豆包：
  豆包.全 query → bytedance-eco 占比
  减去
  max(DeepSeek / 文心 / 千问 / 元宝).全 query → bytedance-eco 占比
  ≥ 20pp

H1.文心：同上，把 bytedance-eco 换成 baidu-eco
H1.元宝：同上，换成 tencent-eco
H1.千问：同上，换成 alibaba-eco
H1.DeepSeek：限定在技术 query 子集上，换成 tech-community
```

**H2 验证条件**：

```
DeepSeek.技术 query → tech-community 占比
减去
max(豆包 / 文心 / 千问 / 元宝).技术 query → tech-community 占比
≥ 20pp
```

**H3 验证条件**：

```
千问.电商 query → alibaba-eco 占比
减去
max(豆包 / DeepSeek / 文心 / 元宝).电商 query → alibaba-eco 占比
≥ 30pp
```

### 统计检验

- **卡方检验**：5 平台 × 13 信源类别交叉表（13 = 12 类 + other），检验"平台 vs 信源类别独立"是否被拒绝
- **Fisher 精确检验**：单元格期望频数 < 5 时使用
- **Bonferroni 修正**：多重比较修正——5 平台两两比较 = **C(5,2) = 10 对**，每对 12 类信源 = 120 比较；α = 0.05 / 120 ≈ **0.0004**
- **置信区间**：报告 Wilson 95% CI，不只看 p 值
- **效应量**：Cramér's V（描述平台 × 信源关联强度）

### 失败处理

- 单次采集失败（页面错误 / 平台风控）→ 跳过、记录、不替换
- 单平台失败率 > 10% → 暂停该平台采集、调查、修订协议
- 单平台失败率 > 30% → **判定该平台 v1 实验设计不可行**，进入小样本人工模式或剔除该平台（同时降级 H1 为 4 平台版本）

## 七、反偏差检查

### 选择偏差

- query 集来源 [`query-set-v1.md`](./query-set-v1.md) 是**预先定义**的，不是看了平台行为后挑的
- 32 个 query 中决策 8 + 知识 8 + 技术 6 + 资讯 4 + 电商 6——五类覆盖且权重合理
- 故意**不挑 YMYL / 本地 / 创意**——这些有更明显的"内置预期信源"或"无信源"，与本实验主旨（生态偏好）正交

### 确认偏差

- 假设 H1 / H2 / H3 **预先注册**在本文档中
- H1 设计为**整体阈值 + 5 配对独立成立 + 无反向**——降低"挑显著的报告"空间
- 副作用：H1 阈值"差异 ≥ 20pp"是为了避免"任何小差异都说成支持"设的硬阈值

### 测量偏差

- 信源归类规则**预先定义**（第一个实验已沉淀，本实验仅扩展 `alibaba-eco`）
- 抽样 5% 人工核查归类（800 × 5% = 40 条）
- 引用源排名直接读取 UI，不主观打分
- 5 平台引用展示形态**差异大**（卡片 / 行内 / 编号），归一化时记录原始展示形态作为元数据

### 报告偏差

- 失败 / 不显著 / 反向的结果**也必须写入 results 部分**
- 不使用"豆包对头条引用率高达 X%"等服务商话术——见下条
- 报告样本量、置信区间、效应量

### GEO 服务商话术对照

实验结果对外展示时，**主动避免**：

- ❌ "豆包对头条引用率 X%，所以发头条就能上豆包"
- ❌ "千问 AI 下单路径覆盖率 Y%，电商商家必投千问"
- ✅ "在 query-set-v1 子集 + 本实验协议下，豆包答案的引用源中 bytedance-eco 类占 X%（95% CI: A-B%；DeepSeek / 文心 / 千问 / 元宝 同样条件下分别为...%）"
- ✅ 与 [C-SEO Bench](https://openreview.net/forum?id=oTeixD3oZO) 的"多数 GEO 方法在严格控制下无效"做对照陈述

## 八、可复现性

### 标注：medium

理由：

- 完整方法学公开 ✅
- query 集公开 ✅
- 信源归类规则公开 ✅
- 数据采集脚本：第一个实验工具栈已写、本实验**3 个新增 adapter 待写**（写完后升级为 high）
- 需要：5 平台账号、IP 在中国大陆、Playwright 环境、约 25-30 小时采集时间、约 8-10 小时人工评分时间

### 复现指引

1. Clone 仓库
2. 准备 5 端测试账号（可用新建匿名）
3. 按 [`tools/exp-doubao-vs-deepseek-paired/`](../tools/exp-doubao-vs-deepseek-paired/) 工具栈基础上扩展 3 个 adapter（wenxin / qianwen / yuanbao）
4. 安装 Playwright + Python 环境
5. 运行扩展后的采集脚本
6. 运行扩展后的评分 / 分析脚本
7. 比较你的结果与本实验结果

## 九、风险评估

| 风险 | 严重度 | 应对 |
|------|--------|------|
| 5 平台风控 / IP 封禁同时触发 | **高** | **串行采集**（不并发）+ 平台间间隔 ≥ 60 秒 + 单 IP 低频（每平台每分钟 ≤ 1 query）+ UA 随机化 + 人工监控 |
| 平台界面变更（5 平台之一） | 高 | 实验脚本需有失败重试 + 容错；**单平台变更只暂停该平台**，其余平台继续采集；变更时记录原 selector 失效日期、新 selector 生效日期 |
| 引用源 URL 难以解析（短链 / 跳转） | 中 | 短链全部 follow redirect；解析后再分类 |
| 模型升级（实验期间，特别是文心 5.0 持续更新） | 中 | 记录每次采集的模型版本，必要时分前后期分析；如某平台升级跨度过大，**该平台数据分前后两批，独立分析** |
| 元宝多模型路由不可控 | 中 | 记录每次的实际路由模型；分析时按"模型组"再切片 |
| 千问 AI 下单路径触发 | 低 | 在数据中标记 `qianwen_commerce_path_triggered`，分析时单独看；触发样本不剔除 |
| 评分人主观偏差（5% 抽样核查） | 低 | 双人独立评分 + Cohen's Kappa；目标 κ > 0.8 |
| 业务影响 | 无 | 本实验不发布内容、不影响真实业务 |
| 法律合规 | 低 | 不涉及 YMYL 类 query；不抓取个人数据；遵守平台 robots（仅 Web 端、不破解 APP） |

## 十、预期产出

- **数据集**：800 条原始采集 + 800 张截图（数据存放路径见 frontmatter）
- **结果报告**：本文档"Results"部分（待跑完后填写）
- **回写**：
  - [`platforms/doubao/citation-mechanism.md`](../platforms/doubao/citation-mechanism.md) 假说一**确认 / 证伪**
  - [`platforms/deepseek/citation-mechanism.md`](../platforms/deepseek/citation-mechanism.md) 假说一 / 二**确认 / 证伪**
  - [`platforms/wenxin/citation-mechanism.md`](../platforms/wenxin/citation-mechanism.md) 假说一**确认 / 证伪**
  - [`platforms/qianwen/citation-mechanism.md`](../platforms/qianwen/citation-mechanism.md) 假说一**确认 / 证伪**
  - [`platforms/yuanbao/citation-mechanism.md`](../platforms/yuanbao/citation-mechanism.md) 假说一**确认 / 证伪**
  - [`techniques/princeton-9-strategies-cn.md`](../techniques/princeton-9-strategies-cn.md) 元假说 B / D **决定性数据点**
  - [`README.md`](../README.md) "中文 GEO 不存在统一最佳实践"主张：首个一手实证支撑 / 修订 / 撤回

## 十一、状态

- [x] 实验设计完成（2026-05-02）
- [ ] 工具栈扩展（wenxin / qianwen / yuanbao 3 个 adapter）
- [ ] 5 平台 selector pilot 验证（2 个已在 exp-doubao-vs-deepseek-paired 中待验证，3 个新增）
- [ ] Pilot run（10 个 query × 1 次 × 5 平台 = 50 次，验证脚本可用）
- [ ] 主实验执行（800 次采集 × 3 天）
- [ ] 数据评分
- [ ] 结果分析与报告
- [ ] 回写到 5 个平台 + Princeton 元假说 + 仓库 README
- [ ] 实验完成日期：TBD

## 十二、与第一个实验的关系

| 维度 | exp-doubao-vs-deepseek-paired (v1) | exp-five-vendor-paired-queries (v1) |
|------|----------------------------------|-----------------------------------|
| 平台数 | 2 | 5 |
| 样本量 | 320 | 800 |
| 主假设 | 双平台单维度差异 | 五平台"生态偏好普遍性" |
| 信源分类 | 12 类（不含 alibaba-eco 独立） | 13 类（新增 alibaba-eco） |
| 阈值 | H1=20pp, H2=20pp | H1=20pp, H2=20pp, **H3=30pp** |
| 多重比较修正 | 48 比较的 Bonferroni | **120 比较**的 Bonferroni |
| 联网状态 | 双轨（开 / 关） | **单轨（仅开启）**——v2 拆 |
| 工具栈 | 已写（pending pilot） | **3 个 adapter 待新增** |
| 状态 | in-validation | **concept** |
| 价值定位 | 仓库第一个一手研究 | **仓库终极实证目标** |

**严格依赖**：本实验 **不能在第一个实验完成前启动**。理由：

1. 第一个实验验证方法学和工具栈在 2 平台上的可行性——5 平台只是放大
2. 如果第一个实验暴露重大方法学缺陷（如归类规则歧义、selector 不稳定）需要先修
3. 5 平台并行采集的工程开销大，先在小样本上确认 ROI

## 十三、Results

> 待实验执行后填写。本节模板：
>
> - 实际采集次数（vs 计划 800）
> - 每平台失败率
> - 主指标交叉表（5 平台 × 5 query 类型 × 13 信源类别 = 325 单元格 + 边际汇总）
> - H1 五条配对各自的验证结果（支持 / 不支持 / 弱效应 / 反向）
> - H1 整体判定（强支持 / 弱支持 / 弱证伪 / 强证伪）
> - H2 / H3 验证结果
> - Cramér's V 效应量
> - 意外发现（无论是否符合预期）
> - 局限性（特别是平台个性化与本实验外控制能力的边界）
> - 后续实验建议（如 H1 部分成立，建议在哪些平台上做更细颗粒度的子实验）

## 变更记录

- 2026-05-02：初版实验设计。在 exp-doubao-vs-deepseek-paired 基础上扩展到 5 平台，新增 H3（千问电商）、`alibaba-eco` 信源类别、120 比较 Bonferroni 修正。状态 concept，等待第一个实验跑通后启动。
