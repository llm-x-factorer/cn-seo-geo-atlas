# tools/

工具评测与脚本。覆盖范围：

| 类别 | 说明 |
|------|------|
| `crawler` | 爬虫 / 抓取（针对 SERP、内容平台、生成式引擎响应） |
| `rank-monitor` | 排名监控（百度、必应、神马，以及内容平台站内关键词排名） |
| `serp-analysis` | SERP 结构分析（特型卡、知识图谱、站内入口、AI 摘要位） |
| `geo-visibility` | 生成式引擎可见性测试（同一 query 在多模型上的引用情况） |
| `content-gen` | 内容生产辅助（结构化生成、批量改写、本地化） |
| `keyword` | 关键词与意图工具（百度指数、5118、热搜趋势） |
| `monitoring` | 站点 / 账号健康监控（备案、收录、索引量） |
| `other` | 其他 |

## 收录原则

- **可访问性优先**：开源 / SaaS / 国内可访问 都收，但分别标注。
- **实测过才写"recommended"**：仅看官网截图不算实测。
- **价格信息标注日期**：定价会变。
- **披露利益关系**：作者 / 投资人 / 长期付费用户都要在卡片里写明。

## 脚本

如果你贡献的是一段脚本而不是评测，可以放在 `tools/<脚本名>/`，附带：

- `README.md`（用法、依赖、注意事项）
- 源码
- 一个最小可运行示例

> 当前阶段不引入语言 / 包管理约定。脚本作者自己写清楚怎么跑就行。

### 已收录脚本

| 路径 | 用途 |
|------|------|
| [`exp-doubao-vs-deepseek-paired/`](./exp-doubao-vs-deepseek-paired) | [`experiments/exp-doubao-vs-deepseek-paired.md`](../experiments/exp-doubao-vs-deepseek-paired.md) 的采集 / 评分 / 分析脚本（Playwright + Python，selector 待 pilot 验证） |

## 模板

复制 [`../templates/tool-review-template.md`](../templates/tool-review-template.md)。
