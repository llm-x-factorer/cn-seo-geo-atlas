# cn-seo-geo-atlas — Claude Code 项目指引

> 这份文件给未来在本仓库工作的 Claude 会话使用。读完这一页 + [`STATUS.md`](./STATUS.md) + [`techniques/dimension-map-cn.md`](./techniques/dimension-map-cn.md) 就能立刻接着干。

## 项目定位

中文互联网 SEO + 生成式引擎优化（GEO）的**调研型 monorepo**，差异化是"英文 awesome list 完全空白的中文平台"——豆包 / DeepSeek / 文心 / 千问 / 元宝 / 小红书 / 知乎 / 微信 / B 站 / 抖音 / 百度。所有内容用中文写，技术术语保留英文（GEO / E-E-A-T / RAG）。

**反 GEO 服务商话术**是仓库基调。常驻怀疑锚点：[C-SEO Bench](https://openreview.net/forum?id=oTeixD3oZO)（NeurIPS 2025）发现严格控制下多数 GEO 方法基本无效。

## 本会话开始前必读

1. [`STATUS.md`](./STATUS.md) —— 当前进度 + 三大卡住点 + 下一步候选方向
2. [`techniques/dimension-map-cn.md`](./techniques/dimension-map-cn.md) —— 18 张技术卡 × D0 + D1-D8 + DS 三轴图谱、卡间关系、强假说集、按服务商话术 / 主体类型反查
3. [`audits/2026-05-04_meta-hypothesis-audit.md`](./audits/2026-05-04_meta-hypothesis-audit.md) —— 元假说审计：91 条假说基于 7 个反转事实判决 ✓ 28 / ◐ 17 / ✗ 9 / ? 32+5；4 个隐含前提中 2 证伪（"草莽期"+"创业 SaaS 为主"）+ 2 部分证伪。**仓库基调更新**：反**尾部 SEO 软文型话术**，不反国标参与方 / 上市公司 / 平台内部人创业等已有结构性背书的玩家
4. [`techniques/geo-industry-stratification-cn.md`](./techniques/geo-industry-stratification-cn.md) —— GEO 行业头部 / 腰部 / 尾部三层结构（承载审计核心结论"分层成熟期"），按客观谓词判分层，避免基于宣传物料 / 单样本主观判断
3. [`BACKLOG.md`](./BACKLOG.md) —— 待办池

## 关键约束（不要打破）

| 约束 | 详情 |
|------|------|
| **frontmatter 字段固定** | `type` / `sources`（含 `url` + `fetched_at`）/ `confidence` / `verified` / `last_verified` / `platforms` / `techniques` / `maturity` |
| **目录深度 ≤ 2** | `platforms/<slug>/<file>.md` 是上限，不再嵌套 |
| **平台不预先评判优劣** | 卡片只描述机制，不做"哪个最好" |
| **预注册阈值锁死** | `H1_DIFF_THRESHOLD_PP=20` / `H2=20` / `H3=30` / `WEAK=5` 一经写入实验设计就不能事后调整 |
| **selector 准确性标注** | 未真实验证写 `# TODO: pilot-verify`，验证后改 `# verified YYYY-MM-DD` |
| **不引入 package.json / CI / 静态站点** | 本轮不实现 |
| **新增 glossary slug 走 PR** | 不直接动 [`glossary/terms.md`](./glossary/terms.md) |
| **五大厂实验严格依赖第一个实验先跑通** | 不能并行启动 |

## 写作风格

### 技术主题卡的标准结构（参考 [`techniques/eeat-cn.md`](./techniques/eeat-cn.md) 或后续任意）

每张技术主题卡必须有：

1. **顶部 ≥ 3 条怀疑锚点**（含 C-SEO Bench 通用锚点）
2. **概念澄清 / 拆解**（区分常被混用的相关概念）
3. **横向对照表**（按平台 / 维度切片）
4. **≥ 4 条元假说**（含 ≥ 1 条强反话术假说）
5. **3 个实验设计建议**（含⭐⭐⭐ 最高优先级、⭐⭐ 中、不建议做的实验）
6. **与 GEO 服务商话术的对照**（明确 ✅ / ⚠️ / ❌ 判定）
7. **与本仓库其他卡片的关系**（引用 ≥ 2 张其他卡）
8. **不做的事**（明确禁区）
9. **待解决的未知 / 公开数据空白**
10. **衍生 BACKLOG 建议**（3-5 条）
11. **变更记录**

### 不应建新卡的情况（参考 [`dimension-map-cn.md`](./techniques/dimension-map-cn.md) 第 IX 节）

- 已有卡的某段可扩写——在原卡更新而不是新建
- 主题与现有卡 ≥ 70% 重叠
- 主题是单平台细节——应放 [`platforms/<slug>/`](./platforms/) 而非 [`techniques/`](./techniques/)
- 主题是单实验设计——应放 [`experiments/`](./experiments/) 而非 [`techniques/`](./techniques/)

## 用户偏好

- **中文回复**，简洁直接，不要寒暄不要总结性结尾
- 提建议时**给方案不要给套路**："我建议 A，因为 X；如果你接受 B 方向我也可以"
- 写代码时**不主动加注释 / docstring / 类型注解**到没改动的代码
- **不为不可能的场景加错误处理**
- 写新卡片时**严格对照 [`techniques/eeat-cn.md`](./techniques/eeat-cn.md) 或 [`techniques/dimension-map-cn.md`](./techniques/dimension-map-cn.md) 的结构**
- 每次完成卡片后**同步更新 [`STATUS.md`](./STATUS.md) 和 [`BACKLOG.md`](./BACKLOG.md)**——不要忘

## 仓库三大卡住点（按优先级，参考 [`STATUS.md`](./STATUS.md) 同段）

1. **第一个实验未跑过**：[`tools/exp-doubao-vs-deepseek-paired/`](./tools/exp-doubao-vs-deepseek-paired/) selector 标 `# TODO: pilot-verify`，等待人工 pilot
2. **五大厂实验未启动**：依赖第一个实验跑通；需 3 个新 adapter（wenxin / qianwen / yuanbao）
3. **大量元假说未实证**：18 张技术卡共 91 条元假说——2026-05-04 审计后 ✓ 28 / ◐ 17 / ✗ 9 / ? 32+5，但 ✓/◐/✗ 大多基于反转事实逻辑外推，pilot 实证仍是首要任务

距离"产出第一个一手研究结论"还差 selector pilot → pilot run → 主实验执行 → score + analyze → 回写。**前 3 步只能由用户做（账号 + 网络环境）**。

## 当前文件总数：81（持续增长中，每次新建卡片必须更新 [`STATUS.md`](./STATUS.md) 第 11 节文件总数）

## 看到这一行说明你已读完——现在去读 [`STATUS.md`](./STATUS.md) 和 [`techniques/dimension-map-cn.md`](./techniques/dimension-map-cn.md)。
