# exp-cn-rag-poisoning-datavoid-sandbox 沙盒工具栈

> **状态**：脚手架完成、smoke test 路径就绪、未跑主实验。
>
> 本目录是 [`experiments/exp-cn-rag-poisoning-datavoid-sandbox.md`](../../experiments/exp-cn-rag-poisoning-datavoid-sandbox.md) 的工具实现，也是 [`audits/2026-05-30_poisoning-research.md`](../../audits/2026-05-30_poisoning-research.md) §3.3 E\* 的落地。

## ⚠️ 伦理边界（先读，不可破坏）

完整声明见 [`ETHICS.md`](./ETHICS.md)。一句话：

> **所有"投毒文档"只写入本地 `data/` 目录，绝不向任何线上第三方系统注入。本工具测的是"防御侧检测信号有没有用"，不是攻击配方。** `poison.py` 故意**不实现** gradient-based 对抗优化（GASLITE / HotFlip），只做 natural / noise 两个朴素风格。

## 判决问题

**data void（目标实体的权威信源覆盖度）是不是中文 RAG 投毒成功的决定变量？**（而非投毒数量）

## 文件结构

```
exp-cn-rag-poisoning-datavoid-sandbox/
├── README.md              # 本文件
├── ETHICS.md              # 伦理边界完整声明
├── requirements.txt       # 依赖（核心 + 可选 ML 后端）
├── config.example.yaml    # 配置模板（复制为 config.yaml）
├── queries.yaml           # 24 query（12 虚构 data void + 12 成熟高覆盖）
├── build_corpus.py        # 构建 clean 基底知识库（mature 有真答案 / fictional 零覆盖）
├── poison.py              # 沙盒投毒注入器（natural + noise 两风格，仅写本地）
├── retriever.py           # bge-zh / hash 检索 + 防御开关（KE / 白名单 / 困惑度过滤）
├── rag_runner.py          # 上下文组装 + 生成（backend: mock / openai / hf）
├── collect.py             # 遍历设计矩阵 → 落 session JSON
├── score.py               # ASR / 检索召回 / 困惑度检出 / FPR → 长格式 CSV
└── analyze.py             # 预注册阈值判定 H1/H2/H3 + Wilson CI + 卡方 → md 报告
```

## 运行环境

- **Python** ≥ 3.10
- **零依赖 smoke test**：只需 `pyyaml numpy pandas scipy`（hash retriever + 启发式困惑度 proxy + mock LLM，全本地、几十秒跑通）
- **真实主实验**：另需 `sentence-transformers`（bge-small-zh）+ 困惑度 LM（`transformers`）+ 一个 LLM backend（本地 `transformers` 小模型，或 OpenAI 兼容端点如 Ollama）

## 安装

```bash
cd tools/exp-cn-rag-poisoning-datavoid-sandbox
python -m venv .venv && source .venv/bin/activate

# 最小（够 smoke test）
pip install pyyaml numpy pandas scipy

# 全量（主实验）
pip install -r requirements.txt
```

## 运行流程

```bash
cp config.example.yaml config.yaml

# Step 0 — 构建 clean 基底知识库
python build_corpus.py --config config.yaml

# Step 1 — 生成本地投毒文档（natural + noise）
python poison.py --config config.yaml

# Step 2a — smoke test（零 ML 依赖，验证 pipeline 通畅）
python collect.py --config config.yaml --smoke

# Step 2b — 主采集（先在 config.yaml 把 retriever.backend=bge、llm.backend=openai/hf）
python collect.py --config config.yaml

# Step 3 — 评分
python score.py --config config.yaml --out data/scored.csv

# Step 4 — 分析（应用预注册阈值）
python analyze.py --scored data/scored.csv --out data/results.md
```

## mock vs 真实 backend（关键）

| backend | ASR 怎么来 | 是否证据 |
|---------|-----------|---------|
| `mock` | 确定性模拟：投毒进 top-k 且不被 clean 文档数量压过 → 判命中 | ❌ **仅验证 pipeline，绝非证据**。analyze.py 会在报告头打 "NOT EVIDENCE" 横幅 |
| `openai` | 真实 LLM（OpenAI 兼容端点，如本地 Ollama 跑 qwen2.5）生成后做关键短语匹配 | ✅ 真实结论 |
| `hf` | 本地 `transformers` 小模型生成 | ✅ 真实结论 |

> mock 之所以会"刚好"产出 H1（虚构 > 成熟）和 H2（防御降 ASR），是因为这两个效应被写进了模拟逻辑——**这正是它不能当证据的原因**。真实判决必须换真实 backend 重跑。

## 数据存放策略

- `data/corpus.jsonl` / `data/poison.jsonl` / `data/raw/*.json`：**不入库**（.gitignore）
- `data/scored.csv`：可选入库
- `data/results.md`：入库

## 已知限制

1. hash retriever / 困惑度 proxy 质量低于 bge-zh / 真实 LM PPL——只够 smoke test，主实验必须切真实后端
2. 投毒文档是朴素 natural / noise，不含 SOTA 对抗优化（故意）——故 ASR 是攻击能力下界，不是上界
3. mock backend 不是证据（见上）
4. 中文 retriever 对抗鲁棒性本身就是被测对象，不是已知量

## 变更记录

- 2026-05-30：初版脚手架（smoke test 就绪，主实验待真实 backend 执行）
