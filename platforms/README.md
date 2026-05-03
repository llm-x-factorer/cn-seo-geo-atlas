# platforms/

按**平台**组织的调研卡片。每个平台一个子目录或一组卡片，记录该平台特有的可见性机制、信号、信号来源、官方文档、变更历史。

## 收录范围

### 传统搜索（SEO）

- `baidu/` —— 百度搜索
- `bing-cn/` —— 必应中文
- `shenma/` —— 神马搜索（UC / 移动端为主）
- `sogou/` —— 搜狗搜索

### 内容平台站内搜索（SEO 边界）

- `xiaohongshu/` —— 小红书站内搜索 + 推荐
- `zhihu/` —— 知乎搜索 + 推荐
- `weixin/` —— 微信搜一搜 / 公众号 / 视频号
- `bilibili/` —— B 站搜索 + 推荐
- `douyin/` —— 抖音搜索 + 推荐
- `kuaishou/` —— 快手搜索 + 推荐

### 生成式引擎（GEO）

- `doubao/` —— 字节豆包
- `kimi/` —— 月之暗面 Kimi
- `yuanbao/` —— 腾讯元宝
- `wenxin/` —— 百度文心一言
- `tongyi/` —— 阿里通义
- `deepseek/` —— DeepSeek
- `chatgpt-cn/` —— ChatGPT 在中文 query 下的行为
- `perplexity-cn/` —— Perplexity 在中文 query 下的行为
- `claude-cn/` —— Claude 在中文 query 下的行为

## 每个平台目录建议结构

```
<platform>/
├── overview.md           # 平台概况、可见性入口、官方文档索引
├── <topic>.md            # 该平台特定主题的卡片，用 technique-template
└── changelog.md          # 平台规则变更年表（可选）
```

> 本仓库目录**不超过两层**。所以平台子目录里只放 markdown，不再嵌套。

## 怎么开始

1. 找到目标平台的子目录（如果没有，先在 PR 里说明并新建）
2. 复制 [`../templates/technique-template.md`](../templates/technique-template.md)
3. 填好 frontmatter，特别是 `platforms` 字段对应这里的 slug

## SEO vs GEO 的边界

- **SEO 平台**：你优化的是**索引、排序、点击**——存在结果列表，用户在里面挑。
- **GEO 平台**：你优化的是**被引用、被合成、被归因**——结果是一段生成文本，引用源未必出现在用户视野里。
- **混合平台**（如知乎、微信）：既是 SEO 目标（站内搜索），也是 GEO 信号源（被生成式引擎抓取作为答案依据）。这类平台的卡片要明确说明在讨论哪种角色。
