# 贡献指南

这是一个调研仓库，**条目质量 > 条目数量**。一条 frontmatter 完整、来源清晰、标注了可信度的卡片，比十条道听途说的"经验"有用得多。

## 你能贡献什么

| 类型 | 用哪个模板 | 放哪里 |
|------|------------|--------|
| 一个技术点的拆解 | [`templates/technique-template.md`](./templates/technique-template.md) | `techniques/` 或 `platforms/<平台>/` |
| 一次实战的完整复盘 | [`templates/case-study-template.md`](./templates/case-study-template.md) | `case-studies/` |
| 一个可复现的实验 | [`templates/experiment-template.md`](./templates/experiment-template.md) | `experiments/` |
| 一个工具的评测 | [`templates/tool-review-template.md`](./templates/tool-review-template.md) | `tools/` |
| 一个值得追踪的源（人 / 账号 / 文档） | 直接 PR 到 `resources/` 或开 issue | `resources/` |
| 术语翻译或定义 | 直接 PR 到 `glossary/` | `glossary/` |

## 必填元数据

所有 markdown 条目顶部都要有 YAML frontmatter。**最小集**：

```yaml
---
title: 条目标题（中文）
type: technique | case-study | experiment | tool-review
sources:
  - url: https://example.com/原始来源
    fetched_at: 2026-05-01      # 抓取/访问日期，YYYY-MM-DD
confidence: low | medium | high  # 你对这条信息的把握程度
verified: false                  # 是否亲自实测验证过（true/false）
last_verified: 2026-05-01        # 最近一次验证日期；未验证就写 null
platforms:                       # 关联平台，参考 glossary
  - baidu
  - kimi
techniques:                      # 关联技术标签
  - structured-data
  - llm-citation
maturity: concept | in-validation | confirmed | deprecated
---
```

字段含义：

- **type**：用于脚本分类，必须是四个值之一。
- **sources**：至少一条。如果是你的原创实验，写自己的实验记录路径或日期。
- **confidence**：
  - `high` = 官方文档 / 多源交叉验证 / 自己跑过
  - `medium` = 单一可信源 / 间接证据
  - `low` = 道听途说 / 单一博文 / 推测
- **verified**：你**亲自跑过 / 复现过 / 观察过**才填 `true`。读了别人的复盘≠verified。
- **last_verified**：未验证则写 `null`，方便后续脚本筛选"待验证"队列。
- **platforms / techniques**：标签优先复用 [glossary/](./glossary) 里已有的，新增标签先在 PR 描述里说明。
- **maturity**：
  - `concept` = 想法、假设、未落地
  - `in-validation` = 正在测、有初步数据
  - `confirmed` = 多人多场景复现过
  - `deprecated` = 平台规则变了、不再适用

## 内容写作规范

- **中英混排**：正文中文为主，技术术语保留英文（如 SERP、E-E-A-T、Schema.org、prompt injection）。
- **每条声明都要可追溯**：要么有外链，要么有自己的实验数据，要么明确写"个人观察，未验证"。
- **不评判好坏**：客观描述机制和效果。"豆包对结构化内容的引用率高于纯叙述"是事实陈述，"豆包比 Kimi 强"不是。
- **不收录黑帽**：刷量、站群、寄生虫、克隆站点等不在收录范围。研究**为什么有效 / 如何被识别**可以，操作手册不行。
- **平台规则会变**：写完一段时间后，定期回来更新 `last_verified`。变了就标 `deprecated` 或开新条目。

## 技术主题卡（`techniques/`）的标准结构

跨平台技术主题卡是仓库的**核心叙事单元**。所有 `techniques/` 下的卡（除元卡）必须包含以下段落：

1. **顶部 ≥ 3 条怀疑锚点** —— 用 `> ⚠️` 引用块；至少 1 条引用 [C-SEO Bench](https://openreview.net/forum?id=oTeixD3oZO)（NeurIPS 2025）作为仓库通用锚点
2. **概念澄清 / 拆解** —— 区分常被混用的相关概念（这是反话术的第一步）
3. **横向对照表** —— 按平台 / 维度切片，禁止单平台深度展开（那是 `platforms/` 的职责）
4. **≥ 4 条可证伪的元假说** —— 每条明确写出"如何验证 / 如何证伪"，含 ≥ 1 条强反话术假说
5. **3 个实验设计建议** —— 标注⭐⭐⭐ 最高优先级、⭐⭐ 中、不建议做的实验
6. **与 GEO 服务商话术的对照表** —— 明确 ✅ / ⚠️ / ❌ 判定，理由必须基于本卡元假说
7. **与本仓库其他卡片的关系** —— 引用 ≥ 2 张其他卡，说明衔接 / 互补 / 同源关系
8. **不做的事** —— 明确禁区，避免功能蔓延
9. **待解决的未知 / 公开数据空白** —— 显式标注厂商不公开的部分
10. **衍生 BACKLOG 建议** —— 3-5 条，让卡片成为"源头"而非"终点"
11. **变更记录** —— 含 `YYYY-MM-DD：初版` 起步

写新技术主题卡时，**严格对照** [`techniques/eeat-cn.md`](./techniques/eeat-cn.md) 或 [`techniques/dimension-map-cn.md`](./techniques/dimension-map-cn.md) 的结构。

## 不应建新卡的情况

避免维度漂移和重复（参考 [`techniques/dimension-map-cn.md`](./techniques/dimension-map-cn.md) 第 IX 节）：

- 已有卡的某段可以扩写——在原卡里更新而不是新建
- 主题与现有卡 ≥ 70% 重叠
- 主题是单平台细节——应放 [`platforms/<slug>/`](./platforms/) 而非 [`techniques/`](./techniques/)
- 主题是单实验设计——应放 [`experiments/`](./experiments/) 而非 [`techniques/`](./techniques/)
- 主题不能产出 ≥ 4 条元假说（事实层卡片应另起类型，不混入技术主题卡）

## 写完一张卡后必须同步的文件

每完成一张技术主题卡，**同一 PR / 提交**必须同步：

- [`STATUS.md`](./STATUS.md) —— 加入"已完成"段、最近会话产出、元假说总数、文件总数、下一步候选
- [`BACKLOG.md`](./BACKLOG.md) —— 主条目标 [x] + 衍生子待办（3-5 条）
- 若新增 glossary slug —— **不直接动 [`glossary/terms.md`](./glossary/terms.md)**，加到 BACKLOG 走 PR 流程

## 文件命名

- 小写、用连字符：`baidu-mip-deprecation.md`、`kimi-citation-mechanism.md`
- 平台名用 [glossary/](./glossary) 里的 slug
- 同主题多版本用日期后缀：`baidu-eeat-2026-05.md`

## 提交流程

1. Fork → 新分支
2. 复制对应模板，填好 frontmatter 和正文
3. 自检 frontmatter（后续会有脚本，目前人工核对）
4. PR 标题：`add: <type> - <平台或主题>`，例如 `add: technique - 小红书站内搜索的笔记加权信号`
5. PR 描述里说明：信息来源、是否实测、和现有条目的关系（补充 / 修正 / 替代）

## 纠错

发现已有条目错了：

- 小修（错别字、链接失效）：直接 PR
- 实质性修正（结论反了、机制变了）：开 [纠错 issue](./.github/ISSUE_TEMPLATE/correction.md)，附证据，再 PR

## 不接受的贡献

- 没有来源的"行业秘密"
- AI 生成的、未经人工核实的内容（用 AI 辅助写作可以，但要自己验证再提交）
- 推广某个工具 / 课程 / 服务的软文
- 把 GEO 等同于"AI SEO"的内容（这是不同的优化对象）
