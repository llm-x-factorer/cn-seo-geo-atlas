---
title: 豆包 vs DeepSeek 配对引用源分布实验（v1）
type: experiment
sources: []
confidence: high
verified: false
last_verified: null
platforms:
  - doubao
  - deepseek
techniques:
  - llm-citation
  - citation-attribution
  - geo-experiment
hypothesis: |
  豆包对字节系内容（头条 / 抖音百科 / 抖音视频转写）的引用比例显著高于 DeepSeek 对同类内容的引用比例，差异 ≥ 20 个百分点。同时 DeepSeek 在技术类 query 上对技术社区（CSDN / 知乎技术 / GitHub）的引用比例显著高于豆包，差异 ≥ 20 个百分点。
maturity: in-validation
run_date:
  start: TBD（pending account + tooling）
  end: TBD
sample_size: 32 query × 5 次重复 × 2 平台 = 320 次采集
controls:
  - 同 query 集
  - 同采集时段窗口
  - 同地理位置（中国大陆，IP 一致）
  - 同账号类型（新建匿名 / 未登录 Web 会话）
  - 同设备 / 浏览器（建议 Playwright + Chromium）
  - 联网搜索：双端均启用 + 双端均关闭，分别采样（共 4 组 = 2 平台 × 2 联网状态）
reproducibility: medium
query_set: query-set-v1
related:
  - ./methodology.md
  - ./query-set-v1.md
  - ../platforms/doubao/citation-mechanism.md
  - ../platforms/deepseek/citation-mechanism.md
  - ../techniques/princeton-9-strategies-cn.md
last_updated: 2026-05-01
---

# 豆包 vs DeepSeek 配对引用源分布实验（v1）

> ⚠️ **实验状态**：**设计完成、未执行**。本文档完成实验设计与协议；执行需要：豆包 / DeepSeek 账号、浏览器自动化能力、约 8-10 小时采集时间、约 4-6 小时人工评分时间。
>
> **价值定位**：仓库**第一个一手研究**——把"豆包偏好字节系、DeepSeek 偏好技术社区"的二手假说升级为有数据支撑的结论或证伪。

## 一、假设

### 主假设（H1）

> 豆包对**字节系内容**（今日头条文章、抖音百科 / 快懂百科、抖音视频转写）的引用比例**显著高于** DeepSeek 对同类内容的引用比例，差异 ≥ 20 个百分点。

### 副假设（H2）

> DeepSeek 在**技术类 query** 上对**技术社区**（CSDN、知乎技术答案、GitHub、Stack Overflow 中文）的引用比例**显著高于** 豆包，差异 ≥ 20 个百分点。

### 元假设回写

实验结果将回写到 [`techniques/princeton-9-strategies-cn.md`](../techniques/princeton-9-strategies-cn.md) 的：

- **元假说 B**（生态内信源 > 生态外权威信源）—— 第一个数据点
- **元假说 D**（query 类型对策略生效有强调节作用）—— 通过技术 query 的强差异验证

## 二、可证伪条件（pre-registration）

**为避免确认偏差，预先声明在以下情形下假设被证伪**：

- H1 证伪条件：豆包字节系内容引用比例与 DeepSeek 同类内容引用比例**差异 < 5 个百分点**，或方向相反
- H2 证伪条件：DeepSeek 在技术 query 上对技术社区引用比例与豆包**差异 < 5 个百分点**

**任何介于 5-20 个百分点之间的差异**——记为"弱效应"，不支持也不证伪强假设；后续需要更大样本量。

## 三、自变量、因变量、控制变量

### 自变量

- **平台**：豆包 vs DeepSeek（2 levels）
- **联网搜索状态**：开启 vs 关闭（2 levels，如 UI 提供该开关）
- **query 类型**：决策 / 知识 / 技术 / 资讯（4 levels）

设计：2 × 2 × 4 = 16 子组，每组 8 query × 5 重复 = 320 次总采集（如联网状态可控）；如不可控则降为 2 × 4 = 8 子组 × 8 query × 5 重复 = 320 次。

### 因变量（主指标）

- **信源类别分布**：每次回答中引用源被分类为以下类别之一的频次
  - `bytedance-eco`：今日头条、抖音百科、快懂百科、抖音视频、西瓜视频
  - `baidu-eco`：百家号、百度百科、百度知道、百度文库
  - `tencent-eco`：微信公众号、知乎专栏、视频号
  - `news-portal`：新浪、网易、搜狐、腾讯新闻、凤凰网（综合门户）
  - `tech-community`：CSDN、知乎技术答案、GitHub、Stack Overflow 中文、稀土掘金
  - `vertical-media`：36 氪、虎嗅、钛媒体、丁香园等垂直媒体
  - `central-media`：人民网、新华网、央视网、央广网、光明网（央媒）
  - `local-media`：地方党媒、地方新闻网
  - `gov-edu`：政府官网、高校 / 研究院网站
  - `xiaohongshu`：小红书笔记
  - `wikipedia-zh`：维基百科中文版
  - `other`：其他

### 因变量（次指标）

- **引用源排名**：在引用列表中的位置（如平台展示引用源列表）
- **每答案引用源数量**：平均每次回答中显示的引用源数
- **引用准确性**：抽样 10% 的回答，人工核对引用源内容是否被准确转述（0=错误 / 1=部分 / 2=准确）

### 控制变量

- 时间窗口：连续 3 天采集，每天采集时段固定（10:00-12:00 / 14:00-16:00 / 19:00-21:00 各一轮）
- 地理位置：中国大陆 IP，固定省份（实验数据中记录）
- 账号：新建匿名账号或未登录 Web 会话（避免历史污染）
- 设备 / 浏览器：Playwright + Chromium 控制，UA 一致
- 会话：每次 query **新会话 + 清空历史**

### 已知混杂变量（标注）

- **平台个性化推送**：即使新建账号，平台仍可能基于 IP / UA / 设备指纹做用户分组——降低但无法消除
- **平台 A/B 测试**：实验期间平台可能改变 UI / 模型——记录每次采集的平台版本号
- **联网检索的实时性**：同 query 不同时刻可能引用不同的"刚发布"内容——通过 3 天 × 3 时段采样平均掉
- **多模型路由（DeepSeek）**：R1 vs V 系列可能被自动路由——记录每次回答的模型标识（如 UI 显示）

## 四、Query 集

从 [`query-set-v1.md`](./query-set-v1.md) 中**选取 32 个 query**：

### 决策类（8 个）

`dec-01` `dec-02` `dec-03` `dec-05` `dec-06` `dec-08` `dec-09` `dec-10`

### 知识类（8 个）

`know-01` `know-02` `know-03` `know-05` `know-06` `know-07` `know-09` `know-10`

### 技术类（8 个，重点验证 H2）

`tech-01` `tech-02` `tech-03` `tech-05` `tech-06` `tech-07` `tech-08` `tech-09`

### 资讯类（8 个，对照基线）

`info-01` `info-03` `info-05` `info-06` `info-07` `info-08` `info-09` `info-10`

> **不包含**：YMYL（合规风险）、电商（千问独有，本实验外）、本地服务（与 LBS 实验绑定）、创意（弱 RAG）

## 五、数据采集协议

### 工具栈

- **浏览器自动化**：Playwright（Python 或 Node.js）+ Chromium
- **采集脚本**：[待编写]，参考 [BACKLOG `meta-experiment-tooling`](../BACKLOG.md)
- **数据存储**：JSON 格式，每次采集为一条记录

### 采集时段（3 天 × 3 时段）

| Day | 时段 1 | 时段 2 | 时段 3 |
|-----|--------|--------|--------|
| Day 1 | 10:00-12:00 | 14:00-16:00 | 19:00-21:00 |
| Day 2 | 同上 | 同上 | 同上 |
| Day 3 | 同上 | 同上 | 同上 |

每个 query 在 9 个时段中随机选 5 个（避免时段聚集）。

### 单次采集步骤

1. 启动新 Playwright 实例（fresh cookies / cache / localStorage）
2. 访问豆包 / DeepSeek Web 端
3. （如有）登录新建匿名账号
4. 配置联网搜索状态（开 / 关）
5. 输入 query，等待回答完成（≤ 60 秒）
6. 截图整个对话页面（PNG）
7. 提取：
   - 答案文本（原文 + 渲染后文本）
   - 引用源列表（URL + 标题，如 UI 展示）
   - 时间戳、平台版本号、模型标识（如 UI 显示）
8. 关闭浏览器实例

### 数据记录字段

```json
{
  "experiment_id": "exp-doubao-vs-deepseek-paired-v1",
  "platform": "doubao | deepseek",
  "query_id": "dec-01",
  "query_text": "...",
  "online_search_enabled": true | false,
  "model_id": "doubao-pro | deepseek-r1 | ...",
  "platform_version": "...",
  "session_id": "...",
  "timestamp": "2026-05-XX 14:30:00 +08:00",
  "geo_ip_province": "...",
  "raw_response_text": "...",
  "citation_sources": [
    {"rank": 1, "title": "...", "url": "..."},
    {"rank": 2, "title": "...", "url": "..."}
  ],
  "screenshot_path": "data/screenshots/...",
  "response_time_ms": 12345
}
```

## 六、评分 rubric（前定义）

### 信源类别归类规则（关键）

每个引用 URL 必须按以下规则归类：

| URL 模式 | 类别 |
|----------|------|
| `*.toutiao.com`, `*.bytedance.com`, `*.douyin.com`, `*.ixigua.com`, `baike.douyin.com` | `bytedance-eco` |
| `baijiahao.baidu.com`, `baike.baidu.com`, `zhidao.baidu.com`, `wenku.baidu.com`, `*.baidu.com` 知识类 | `baidu-eco` |
| `mp.weixin.qq.com`, `zhuanlan.zhihu.com`（专栏）, `channels.weixin.qq.com` | `tencent-eco` |
| `news.sina.com.cn`, `*.163.com`, `*.sohu.com`, `news.qq.com`, `*.ifeng.com` | `news-portal` |
| `*.csdn.net`, `www.zhihu.com/question`（问答）, `github.com`, `stackoverflow.com`, `juejin.cn` | `tech-community` |
| `36kr.com`, `huxiu.com`, `tmtpost.com`, `dxy.com` | `vertical-media` |
| `people.com.cn`, `xinhuanet.com`, `cctv.com`, `gmw.cn`, `cnr.cn` | `central-media` |
| 各省 / 市政府门户、地方报媒 | `local-media` |
| `*.gov.cn`, `*.edu.cn`, `*.cas.cn`, `*.cssn.cn` | `gov-edu` |
| `xiaohongshu.com`, `xhslink.com` | `xiaohongshu` |
| `zh.wikipedia.org` | `wikipedia-zh` |
| 其他 | `other` |

**边界规则**：

- 如果一个 URL 同时符合多个类别，按优先级：`gov-edu` > `central-media` > `local-media` > 生态系（`bytedance-eco` / `baidu-eco` / `tencent-eco`）> `vertical-media` > `news-portal` > `tech-community` > `xiaohongshu` > `wikipedia-zh` > `other`
- 知乎要细分：问答页（`/question/`）→ `tech-community`；专栏（`zhuanlan.zhihu.com`）→ `tencent-eco`
- 自动归类后，**抽样 10% 人工核查**——确保归类规则正确执行

### 主指标计算

对每个（平台 × query 类型）组合：

```
比例(类别 C) = 该组合下类别 C 出现的总频次 / 该组合下所有引用源总频次
```

H1 验证条件：

```
豆包.决策 + 豆包.知识 + 豆包.资讯 + 豆包.技术 → 平均字节系比例
减去
DeepSeek.决策 + DeepSeek.知识 + DeepSeek.资讯 + DeepSeek.技术 → 平均字节系比例
≥ 20 个百分点
```

H2 验证条件：

```
DeepSeek.技术 → 技术社区比例
减去
豆包.技术 → 技术社区比例
≥ 20 个百分点
```

### 统计检验

- **卡方检验**（chi-square test）：平台 × 信源类别交叉表，是否独立
- **Fisher 精确检验**：单元格期望频数 < 5 时使用
- **Bonferroni 修正**：多重比较时（4 个 query 类型 × 12 个信源类别 = 48 比较）
- **置信区间**：报告 95% CI，不只看 p 值

### 失败处理

- 单次采集失败（页面错误 / 平台风控）→ 跳过、记录、不替换
- 失败率 > 10% → 暂停实验、调查原因、修订协议
- 失败率 > 30% → **判定实验设计不可行**，进入小样本人工模式

## 七、反偏差检查

### 选择偏差

- query 集来源 [`query-set-v1.md`](./query-set-v1.md) 是**预先定义**的，不是看了平台行为后挑的
- query 类型分层覆盖（决策 / 知识 / 技术 / 资讯）
- 时段分散

### 确认偏差

- 假设 H1 / H2 **预先注册**在本文档中
- 设有**可证伪条件**
- 副作用：H1 H2 的"差异 ≥ 20 pp"是**为了避免"任何小差异都说成支持"** 设的硬阈值

### 测量偏差

- 信源归类规则**预先定义**
- 抽样 10% 人工核查归类
- 引用源排名直接读取 UI，不主观打分

### 报告偏差

- 失败 / 不显著 / 反向的结果**也必须写入 results 部分**
- 不使用"显著提升""大幅领先"未量化表述
- 报告样本量、置信区间、p 值

### GEO 服务商话术对照

实验结果对外展示时，**主动避免**以下话术：

- ❌ "豆包对字节系内容的引用率高达 X%"——容易被误用为"发头条就能上豆包"的销售证据
- ✅ "在我们的 query 集 + 协议下，豆包答案的引用源中字节系内容占 X%（95% CI: A-B%）；DeepSeek 同样条件下为 Y%"

## 八、可复现性

### 标注：medium

理由：

- 完整方法学公开 ✅
- query 集公开 ✅
- 信源归类规则公开 ✅
- 数据采集脚本待编写（写完后升级为 high）
- 需要：豆包 / DeepSeek 账号、IP 在中国大陆、Playwright 环境

### 复现指引

1. Clone 仓库
2. 准备豆包 / DeepSeek 测试账号（可用新建匿名）
3. 安装 Playwright + Python 环境
4. 运行 [待编写] 采集脚本
5. 运行 [待编写] 评分脚本
6. 比较你的结果与本实验结果

## 九、风险评估

| 风险 | 严重度 | 应对 |
|------|--------|------|
| 平台风控 / IP 封禁 | 高 | 单 IP 低频采集（间隔 ≥ 30 秒）+ UA 随机化 + 人工监控 |
| 平台界面变更 | 中 | 实验脚本需有失败重试 + 容错；变更时记录、不强行抓 |
| 引用源 URL 难以解析（短链 / 跳转） | 中 | 短链全部 follow redirect；解析后再分类 |
| 模型升级（实验期间） | 低 | 记录每次采集的模型版本，必要时分前后期分析 |
| 评分人主观偏差（10% 抽样核查） | 低 | 双人独立评分 + Cohen's Kappa；目标 κ > 0.8 |
| 业务影响 | 无 | 本实验不发布内容、不影响真实业务 |
| 法律合规 | 低 | 不涉及 YMYL 类 query；不抓取个人数据；遵守平台 robots（仅 Web 端、不破解 APP） |

## 十、预期产出

- **数据集**：320 条原始采集 + 320 张截图（数据存放路径见 frontmatter）
- **结果报告**：本文档的"Results"部分（待跑完后填写）
- **回写**：
  - [`platforms/doubao/citation-mechanism.md`](../platforms/doubao/citation-mechanism.md) **假说一** 升级为机制 / 证伪
  - [`platforms/deepseek/citation-mechanism.md`](../platforms/deepseek/citation-mechanism.md) **假说一**、**假说二（如涉及）** 升级
  - [`techniques/princeton-9-strategies-cn.md`](../techniques/princeton-9-strategies-cn.md) **元假说 B、D** 第一个数据点

## 十一、状态

- [x] 实验设计完成（2026-05-01）
- [ ] 采集工具编写
- [ ] Pilot run（5 个 query × 1 次 × 2 平台 = 10 次，验证脚本可用）
- [ ] 主实验执行
- [ ] 数据评分
- [ ] 结果分析与报告
- [ ] 回写到关联卡片
- [ ] 实验完成日期：TBD

## 十二、Results

> 待实验执行后填写。本节模板：
>
> - 实际采集次数（vs 计划 320）
> - 失败 / 缺失数据的原因与处理
> - 主指标交叉表（平台 × query 类型 × 信源类别）
> - H1 / H2 验证结果（支持 / 不支持 / 弱效应 / 反向）
> - 次指标分析（引用源排名、引用准确性等）
> - 意外发现（无论是否符合预期）
> - 局限性
> - 后续实验建议

## 变更记录

- 2026-05-01：初版实验设计
