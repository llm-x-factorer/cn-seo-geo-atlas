# exp-doubao-vs-deepseek-paired 采集 / 评分 / 分析脚本

> **状态**：**框架完成、selector 待 pilot 验证**。
>
> 本目录是 [`experiments/exp-doubao-vs-deepseek-paired.md`](../../experiments/exp-doubao-vs-deepseek-paired.md) 的工具实现。框架代码完整，但豆包 / DeepSeek 的 Web 端 selector **必须先跑 pilot 验证 / 调整** 才能用于主实验。

## 文件结构

```
exp-doubao-vs-deepseek-paired/
├── README.md                  # 本文件
├── requirements.txt           # Python 依赖
├── config.example.yaml        # 配置模板（复制为 config.yaml）
├── queries.yaml               # 32 个实验 query（从 query-set-v1 抽取）
├── source_classifier.py       # URL → 信源类别 归类规则（纯函数）
├── doubao_adapter.py          # 豆包 Web 端页面适配器
├── deepseek_adapter.py        # DeepSeek Web 端页面适配器
├── collect.py                 # 主采集脚本
├── score.py                   # 评分脚本（应用归类规则）
└── analyze.py                 # 统计分析脚本（交叉表 + 卡方）
```

## 运行环境

- **Python**：≥ 3.10（建议 3.11）
- **OS**：macOS / Linux（Windows 未测试）
- **网络**：中国大陆 IP（实验设计要求）；如需访问豆包 / DeepSeek 的 Web 端，按当地合规要求配置网络

## 安装

```bash
cd tools/exp-doubao-vs-deepseek-paired

python -m venv .venv
source .venv/bin/activate

pip install -r requirements.txt
playwright install chromium
```

## 配置

```bash
cp config.example.yaml config.yaml
# 编辑 config.yaml，根据实际情况修改
```

关键配置项：

| 字段 | 说明 |
|------|------|
| `experiment_id` | 实验唯一标识，对应 [`experiments/`](../../experiments/) 中的实验设计文档 |
| `data_dir` | 原始采集数据存放目录（**绝不入库**，加入 .gitignore） |
| `repetitions` | 每个 query 重复采集次数（实验设计要求 5） |
| `cooldown_seconds` | 单次采集之间的 sleep（避免被风控） |
| `timeout_seconds` | 单次回答等待超时 |
| `headless` | pilot 时建议 `false` 以便人工监督 selector 是否生效 |
| `online_search.<platform>` | 是否开启平台联网搜索（豆包 / DeepSeek 都有此开关） |

## 运行流程

### Step 1 — Pilot run（必做）

主实验前**必须**先跑 pilot，验证 selector 在当前平台 UI 下能正确工作：

```bash
python collect.py --pilot --queries 2 --platforms doubao,deepseek
```

`--pilot` 模式只跑 2 个 query × 1 次 × 2 平台 = 4 次采集（headless=false，人工监督）。

**人工核查清单**（pilot 完成后逐项确认）：

- [ ] 浏览器是否成功访问平台 Web 端？
- [ ] query 是否被正确输入？
- [ ] 答案是否被等到完整生成？
- [ ] 引用源是否被完整提取？
- [ ] 截图是否完整？
- [ ] 数据 JSON 是否字段完整？

如果任何一项失败：**修改对应 adapter 的 selector**（`doubao_adapter.py` / `deepseek_adapter.py`），重跑 pilot，直到全部通过。

### Step 2 — 主采集（pilot 通过后）

```bash
python collect.py --queries-file queries.yaml --platforms doubao,deepseek
```

预期：320 次采集，分散在 3 天 × 3 时段。**强烈建议分批跑**：

```bash
# Day 1
python collect.py --time-window day1-am   # 预定义时段
python collect.py --time-window day1-pm
python collect.py --time-window day1-eve

# Day 2 / 3 同上
```

### Step 3 — 评分（应用归类规则）

```bash
python score.py --data-dir data/raw --out data/scored.csv
```

输出 CSV，每行一个引用源，字段：

```
experiment_id, platform, query_id, query_type, repetition, timestamp,
source_rank, source_url, source_domain, source_category
```

### Step 4 — 统计分析

```bash
python analyze.py --scored data/scored.csv --out data/results.md
```

输出 Markdown 报告：

- 平台 × 信源类别 交叉表（含百分比 + 95% CI）
- 卡方 / Fisher 精确检验 p 值
- H1 / H2 验证结果（支持 / 不支持 / 弱效应）
- 引用源排名 Wilcoxon
- 关键发现 highlight

## 数据存放策略

按 [`experiments/methodology.md`](../../experiments/methodology.md) §六：

- `data/raw/`：原始 JSON + 截图，**不入库**（在 .gitignore）
- `data/scored.csv`：归类后数据，**可选入库**（脱敏后）
- `data/results.md`：分析结果报告，**入库**

## 已知限制

1. **selector 易变**：豆包 / DeepSeek 的 Web UI 持续迭代——adapter 中的 selector 可能在数周内失效。每次重跑前先做 pilot
2. **APP 行为不等于 Web**：本脚本只测 Web 端。APP 行为（特别是豆包）需要其他工具（Appium / 真机）
3. **无法绕过风控**：高频请求会触发风控，必须遵守 `cooldown_seconds`
4. **多模型路由（DeepSeek）**：脚本会记录回答中的 model identifier（如 UI 显示），但**无法控制路由**
5. **联网搜索状态不一定可控**：部分平台 UI 没有显式开关——以平台默认行为为准，记录在数据中
6. **截图可能不完整**：长答案 / 多引用源时整页截图可能切割——脚本使用 full page screenshot，但仍可能受平台懒加载影响

## 风险

| 风险 | 应对 |
|------|------|
| 账号 / IP 被风控 | 单 IP 低频（≥ 30s 间隔）+ UA 随机化 + 单 session 单次采集 |
| 平台 UI 变更 | pilot 即时验证；selector 改动通过 PR 留痕 |
| 数据泄露（截图含个人信息） | 使用新建匿名账号 / 未登录会话；截图前清空浏览器存储 |
| 平台条款合规 | **仅 Web 端 + 遵守 robots.txt + 不破解 / 反编译 / 大规模爬取**——本脚本是科研级单 IP 慢速采集 |

## 修改 selector 的位置

豆包：[`doubao_adapter.py`](./doubao_adapter.py) 顶部的 `SELECTORS` 字典
DeepSeek：[`deepseek_adapter.py`](./deepseek_adapter.py) 顶部的 `SELECTORS` 字典

每个 selector 都有 `# TODO: pilot-verify` 注释，pilot 通过后改为 `# verified YYYY-MM-DD`。

## 贡献

- selector 失效时**直接修复 + PR**（不要新建 adapter 文件）
- 新平台支持（千问 / 文心 / 元宝）→ 新建 `<platform>_adapter.py`，在 collect.py 中注册
- 评分规则更新（新信源类别 / 新 URL 模式）→ 改 `source_classifier.py`，在 [`experiments/methodology.md`](../../experiments/methodology.md) 同步更新

## 变更记录

- 2026-05-01：初版骨架（selector 待 pilot 验证）
