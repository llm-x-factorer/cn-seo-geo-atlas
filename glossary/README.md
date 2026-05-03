# glossary/

中英术语表。中文互联网 SEO/GEO 圈有大量术语在不同社群里用法不一致，这里做收敛。

## 维护方式

- 单一索引文件 [`terms.md`](./terms.md)（首次贡献时创建）
- 每个术语一段，包含：英文 / 中文常见译法 / 一句话定义 / 易混词区分 / 在本仓库使用的标准 slug
- 新术语来 PR，争议术语开 issue 讨论

## 必须收录的高优先术语（占位，待补）

- **GEO** (Generative Engine Optimization)：针对生成式引擎的优化。**不等于** "AI SEO"——
  - SEO 优化的是被检索、被排序、被点击
  - GEO 优化的是被引用、被合成、被归因
  - 信号源、反馈回路、可观测性都不同
- **AEO** (Answer Engine Optimization)：针对答案引擎的优化，常和 GEO 混用，但严格说更偏向"零点击答案位"
- **LLMO** / **AISO**：业内不同社群的别名，本仓库统一用 GEO
- **E-E-A-T**：Experience, Expertise, Authoritativeness, Trustworthiness（中文常译"经验、专业、权威、可信"）
- **SERP** (Search Engine Results Page)：搜索结果页
- **特型 / 特型卡**：百度对结构化结果位的内部叫法（Featured Snippet 类似物）
- **站内搜索**：内容平台内部的搜索功能（小红书、知乎、B站、抖音、微信搜一搜……）
- **可见性**（visibility）：被检索 / 被引用 / 被展示的总称
- **引用归因** (citation attribution)：生成式引擎在答案中标注信息来源的机制

## Slug 规范

平台 slug、技术标签 slug 在 frontmatter 中使用，需要稳定。每次新增 slug 都要更新这个表。

| 类别 | slug 命名规则 |
|------|---------------|
| 平台 | 全小写、英文 / 拼音、连字符。例：`baidu`、`xiaohongshu`、`weixin`、`kimi`、`chatgpt-cn` |
| 技术标签 | 全小写、英文、连字符。例：`structured-data`、`llm-citation`、`prompt-level-seo` |
| 行业 | 全小写、英文。例：`saas`、`ecommerce`、`local-services` |
