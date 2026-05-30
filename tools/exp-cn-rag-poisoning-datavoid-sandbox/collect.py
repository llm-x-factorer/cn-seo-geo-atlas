"""主采集：遍历设计矩阵（query × 投毒量 × 防御态 × 重复），每 session 落 JSON。

  # smoke test（零 ML 依赖，验证 pipeline）
  python collect.py --config config.yaml --smoke

  # 主采集（先在 config.yaml 切 retriever.backend=bge、llm.backend=openai/hf）
  python collect.py --config config.yaml

每 session 在每 query 内同时注入 natural + noise 两风格投毒（各 dose 篇），
检索一次，记录 ASR + 每风格投毒文档是否被困惑度过滤（供 H3）。
"""

from __future__ import annotations

import argparse
import json
from collections import defaultdict
from datetime import datetime, timezone
from pathlib import Path

import numpy as np
import yaml

import corpus_io
import rag_runner
from retriever import Retriever


def now_iso() -> str:
    return datetime.now(timezone.utc).astimezone().isoformat(timespec="seconds")


def parse_args() -> argparse.Namespace:
    p = argparse.ArgumentParser()
    p.add_argument("--config", default="config.yaml")
    p.add_argument("--smoke", action="store_true", help="零依赖快速验证：hash 检索 + mock LLM + 启发式困惑度 + 少量样本")
    return p.parse_args()


def resolve_dose_n(dose, corpus_size: int) -> int:
    if isinstance(dose, int):
        return dose
    return max(1, round(float(dose) * corpus_size))


def main() -> None:
    args = parse_args()
    cfg = yaml.safe_load(Path(args.config).read_text(encoding="utf-8"))
    queries = yaml.safe_load(Path(cfg["queries_file"]).read_text(encoding="utf-8"))["queries"]

    if args.smoke:
        cfg.setdefault("retriever", {})["backend"] = "hash"
        cfg.setdefault("defense", {})["perplexity_backend"] = "heuristic"
        cfg.setdefault("llm", {})["backend"] = "mock"
        cfg["repetitions"] = 1
        cfg["poison_doses"] = [1, 5]
        fic = [q for q in queries if q["entity_class"] == "fictional"][:2]
        mat = [q for q in queries if q["entity_class"] == "mature"][:2]
        queries = fic + mat
        print("[collect] SMOKE 模式：hash + mock + heuristic，2 虚构 + 2 成熟 × dose[1,5] × def[off,on] × 1")

    clean = corpus_io.load_jsonl(Path(cfg["corpus_path"]))
    poison = corpus_io.load_jsonl(Path(cfg["poison_path"]))
    if not clean:
        raise SystemExit("clean corpus 为空，先跑 build_corpus.py")
    if not poison:
        raise SystemExit("poison 为空，先跑 poison.py")

    retr = Retriever(cfg)

    # 预计算 embedding（clean 一次 + poison 全池一次）
    print(f"[collect] embedding clean={len(clean)} poison={len(poison)} ...")
    clean_emb = retr.embed([d["text"] for d in clean])
    poison_emb = retr.embed([d["text"] for d in poison])
    poison_by_qs: dict[tuple, list[int]] = defaultdict(list)
    for i, d in enumerate(poison):
        poison_by_qs[(d["query_id"], d["poison_style"])].append(i)

    doses = cfg.get("poison_doses", [1, 5, 0.03])
    defenses = cfg.get("defense_states", ["off", "on"])
    reps = int(cfg.get("repetitions", 5))
    styles = cfg.get("poison_styles", ["natural", "noise"])
    out_dir = Path(cfg["data_dir"]) / "raw"
    exp = cfg["experiment_id"]

    total = len(queries) * len(doses) * len(defenses) * reps
    done = 0
    for q in queries:
        for dose in doses:
            dose_n = resolve_dose_n(dose, len(clean))
            sel = []
            for style in styles:
                sel += poison_by_qs.get((q["id"], style), [])[:dose_n]
            work_docs = clean + [poison[i] for i in sel]
            work_emb = np.vstack([clean_emb, poison_emb[sel]]) if sel else clean_emb

            for defense in defenses:
                for rep in range(reps):
                    done += 1
                    r = retr.retrieve(q["text"], work_docs, work_emb, defense, q["id"])
                    answer, hit = rag_runner.generate(q, r["context"], cfg)
                    sid = f"{exp}__{q['id']}__dose{dose}__def{defense}__rep{rep}"
                    rec = {
                        "experiment_id": exp,
                        "session_id": sid,
                        "query_id": q["id"],
                        "entity_class": q["entity_class"],
                        "poison_dose": dose,
                        "poison_dose_n": dose_n,
                        "defense_state": defense,
                        "repetition": rep,
                        "llm_backend": cfg["llm"]["backend"],
                        "retriever_backend": retr.backend,
                        "ppl_backend": retr._ppl.backend,
                        "poison_in_context": r["poison_in_context"],
                        "clean_true_in_context": r["clean_true_in_context"],
                        "asr_hit": hit,
                        "answer_text": answer,
                        "poison_diag": r["poison_diag"],
                        "timestamp_iso": now_iso(),
                    }
                    rec_dir = out_dir / q["id"]
                    rec_dir.mkdir(parents=True, exist_ok=True)
                    (rec_dir / f"{sid}.json").write_text(
                        json.dumps(rec, ensure_ascii=False, indent=2), encoding="utf-8"
                    )
                    if done % 20 == 0 or done == total:
                        print(f"[{done}/{total}] {q['id']} dose={dose} def={defense} hit={hit}")

    print(f"[done] {done} sessions → {out_dir}")
    if cfg["llm"]["backend"] == "mock":
        print("[warn] llm.backend=mock —— 结果仅验证 pipeline，不是证据。换 openai/hf 跑主实验。")


if __name__ == "__main__":
    main()
