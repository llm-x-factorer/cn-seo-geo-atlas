# techniques/

**跨平台**的技术主题。一个技术点如果只在单个平台有效，写到 `platforms/<平台>/` 下；如果横跨多个平台，写在这里，再用 frontmatter 的 `platforms` 字段做关联。

## 主题分组建议

### 内容信号

- 结构化数据（Schema.org 中文实践、JSON-LD、微数据、标注覆盖）
- E-E-A-T 中文版（百度的"权威性 / 专业性"信号，与 Google 的异同）
- 标题、首段、TL;DR 的可引用性结构
- 多模态信号（图片 alt、视频转录、字幕）

### 站点 / 账号信号

- 备案、ICP、域名年龄对中文搜索的影响
- 账号实名、企业号、蓝 V / 黄 V 认证
- 主体绑定与跨平台一致性

### 链接 / 引用 / 提及

- 中文外链生态（行业目录、问答站、行业站）
- LLM 引用机制（哪些源被高频引用、引用归因怎么标）
- 知识图谱与百科收录（百度百科、维基中文、垂直百科）

### 检索 & 提示词

- prompt-level SEO（"在豆包里搜什么会出现你"）
- 长尾词挖掘（百度指数、5118、AI 工具的中文词覆盖差异）
- query 意图分类在中文场景下的偏移

### 反馈回路 & 监测

- 排名监控的可观测性边界
- 生成式引擎可见性测试方法学
- A/B 在 SEO/GEO 场景下的局限

> 以上是**起点目录**，不是封闭分类。新主题直接加。

## 写法

- 每个技术点一个 markdown，复制 [`../templates/technique-template.md`](../templates/technique-template.md)
- 文件名用平铺命名：`structured-data-cn-practice.md`、`llm-citation-attribution.md`
- frontmatter 的 `platforms` 字段列出**实证关联过**的平台，没验证过别填
