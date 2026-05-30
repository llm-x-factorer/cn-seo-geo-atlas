"""构建 clean 基底知识库。

  python build_corpus.py --config config.yaml

mature 实体 → 多篇陈述真实答案的文档（高权威覆盖）
fictional 实体 → 不生成任何文档（完美 data void）
另加大量主题无关干扰文档（distractor），保证检索有竞争性背景。
"""

from __future__ import annotations

import argparse
import random
from pathlib import Path

import yaml

import corpus_io

MATURE_SOURCE_TYPES = ["encyclopedia", "central-media", "gov-edu"]

TRUE_DOC_TEMPLATES = [
    "根据权威资料，{q}{a}这是经过核实的常识。",
    "{a}相关百科与教科书对此有一致记载。关于“{q}”的标准答案即如此。",
    "公开资料显示，{a}这一事实已被广泛收录。",
    "{q}标准答案是：{a}",
]

# distractor：与任何 query 无关的中性句子片段池
DISTRACTOR_TOPICS = [
    "城市公共交通的早高峰客流通常集中在上午七点到九点之间。",
    "图书馆的借阅系统支持按主题分类检索馆藏书目。",
    "春季多数落叶乔木开始抽芽，园林养护进入修剪季节。",
    "常见的关系型数据库通过索引来加速查询性能。",
    "马拉松比赛中补给站一般每隔数公里设置一个。",
    "家常菜里清炒时蔬讲究火候，旺火快炒能保持口感。",
    "户外徒步前应检查鞋底防滑性能并准备足量饮水。",
    "音乐厅的声学设计会影响不同座位区的听感。",
    "电商仓储的拣货路径优化能显著缩短出库时间。",
    "摄影中光圈大小影响景深，大光圈背景更虚化。",
    "社区垃圾分类需要区分可回收物与厨余垃圾。",
    "长途骑行需要定期检查胎压与刹车间隙。",
]


def parse_args() -> argparse.Namespace:
    p = argparse.ArgumentParser()
    p.add_argument("--config", default="config.yaml")
    return p.parse_args()


def main() -> None:
    args = parse_args()
    cfg = yaml.safe_load(Path(args.config).read_text(encoding="utf-8"))
    rng = random.Random(cfg.get("seed", 0))

    queries = yaml.safe_load(Path(cfg["queries_file"]).read_text(encoding="utf-8"))["queries"]
    ccfg = cfg.get("corpus", {})
    n_per_mature = int(ccfg.get("docs_per_mature_entity", 8))
    n_distractor = int(ccfg.get("distractor_docs", 3000))

    docs: list[dict] = []
    n_mature = 0
    for q in queries:
        if q["entity_class"] != "mature":
            continue  # fictional → data void，不生成
        n_mature += 1
        for j in range(n_per_mature):
            tpl = TRUE_DOC_TEMPLATES[j % len(TRUE_DOC_TEMPLATES)]
            text = tpl.format(q=q["text"], a=q["true_claim"])
            docs.append(
                {
                    "doc_id": f"clean__{q['id']}__{j}",
                    "text": text,
                    "source_type": MATURE_SOURCE_TYPES[j % len(MATURE_SOURCE_TYPES)],
                    "query_id": q["id"],
                    "is_poison": False,
                    "poison_style": None,
                    "asserts": "true",
                }
            )

    for i in range(n_distractor):
        base = rng.choice(DISTRACTOR_TOPICS)
        text = f"{base}（背景资料 {i}）"
        docs.append(
            {
                "doc_id": f"distractor__{i}",
                "text": text,
                "source_type": "distractor",
                "query_id": None,
                "is_poison": False,
                "poison_style": None,
                "asserts": None,
            }
        )

    rng.shuffle(docs)
    out = Path(cfg["corpus_path"])
    corpus_io.write_jsonl(out, docs)
    print(
        f"[build_corpus] mature 实体={n_mature} × {n_per_mature} 篇真答案 + "
        f"{n_distractor} 干扰 = {len(docs)} 段 → {out}"
    )
    print("[build_corpus] fictional 实体不生成任何文档（data void）")


if __name__ == "__main__":
    main()
