---
name: 调研 / 实验任务
about: 跟踪一个具体的调研任务、实验、平台 stub 创建、技术主题写作、工具评测
title: "[task] "
labels: ["task", "triage"]
---

## 任务类型

（选一个）

- [ ] 实验（experiment）
- [ ] 平台调研（platform）
- [ ] 技术主题（technique）
- [ ] 工具评测（tool-review）
- [ ] 资源 / 文档（docs）
- [ ] 元问题 / 方法学（meta）

## 关联

- **来源**：从哪里来的？引用 [`BACKLOG.md`](../../BACKLOG.md) 的条目 ID（如 `exp-doubao-citation-source-distribution`），或链接到提出这个任务的 PR / 卡片
- **关联条目**：哪些已有卡片需要在任务完成后回写？列出仓库内相对路径
- **关联平台 / 技术 slug**：（参考 [`glossary/terms.md`](../../glossary/terms.md)）

## 任务描述

一段话说清要做什么。**不要展开成调研内容**——那应该写到对应的卡片里。本 issue 只是任务跟踪。

## 验收条件

清晰列出"做完"的标准。例：

- [ ] 跑了 N 类 query × M 次重复，原始数据落库
- [ ] 在 `experiments/<name>.md` 输出实验记录，frontmatter 完整
- [ ] 在 `platforms/<plat>/citation-mechanism.md` 对应假说处回写 `Confirmed / Refuted`
- [ ] 在 `BACKLOG.md` 标 `[x]` 完成

## 工作量估计

- [ ] 小（< 半天）
- [ ] 中（半天 ~ 2 天）
- [ ] 大（> 2 天，应考虑拆分）

## 优先级

- [ ] high（阻塞后续工作 / 高边际价值）
- [ ] medium（计划内但不紧迫）
- [ ] low（机会主义型）

## 依赖

- **被这个 task 阻塞的**：（其他 issue / 卡片）
- **阻塞这个 task 的**：（其他 issue / 卡片 / 外部条件，例：账号、梯子、抓取工具）

## 备注

- 已知风险、不确定性、需要决定的事
- 数据来源、需要访问的平台、是否需要梯子 / 账号
