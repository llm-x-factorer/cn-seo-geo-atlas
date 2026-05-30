"""评分：读 data/raw/*.json → 两个长格式 CSV。

  python score.py --config config.yaml --out data/scored.csv

scored.csv          每 session 一行（ASR / 检索失败 vs 生成失败）
scored_detection.csv 每个投毒候选一行（防御开时，供 H3 困惑度检出率）
"""

from __future__ import annotations

import argparse
import csv
import json
from pathlib import Path

import yaml


def parse_args() -> argparse.Namespace:
    p = argparse.ArgumentParser()
    p.add_argument("--config", default="config.yaml")
    p.add_argument("--out", default="data/scored.csv")
    return p.parse_args()


def main() -> None:
    args = parse_args()
    cfg = yaml.safe_load(Path(args.config).read_text(encoding="utf-8"))
    raw_dir = Path(cfg["data_dir"]) / "raw"
    files = sorted(raw_dir.rglob("*.json"))
    if not files:
        raise SystemExit(f"无 session 数据：{raw_dir}（先跑 collect.py）")

    session_rows = []
    detection_rows = []
    for fp in files:
        rec = json.loads(fp.read_text(encoding="utf-8"))
        pin = rec["poison_in_context"]
        session_rows.append(
            {
                "experiment_id": rec["experiment_id"],
                "session_id": rec["session_id"],
                "query_id": rec["query_id"],
                "entity_class": rec["entity_class"],
                "poison_dose": rec["poison_dose"],
                "defense_state": rec["defense_state"],
                "repetition": rec["repetition"],
                "llm_backend": rec["llm_backend"],
                "poison_in_context": pin,
                "clean_true_in_context": rec["clean_true_in_context"],
                "asr_hit": rec["asr_hit"],
                "retrieval_fail": int(pin == 0),
                "generation_fail": int(pin > 0 and rec["asr_hit"] == 0),
            }
        )
        for diag in rec.get("poison_diag", []):
            detection_rows.append(
                {
                    "query_id": rec["query_id"],
                    "entity_class": rec["entity_class"],
                    "defense_state": rec["defense_state"],
                    "poison_style": diag["style"],
                    "filtered_by_ppl": int(diag["filtered_by_ppl"]),
                }
            )

    out = Path(args.out)
    out.parent.mkdir(parents=True, exist_ok=True)
    with out.open("w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=list(session_rows[0].keys()))
        w.writeheader()
        w.writerows(session_rows)

    det_out = out.with_name(out.stem + "_detection.csv")
    if detection_rows:
        with det_out.open("w", encoding="utf-8", newline="") as f:
            w = csv.DictWriter(f, fieldnames=list(detection_rows[0].keys()))
            w.writeheader()
            w.writerows(detection_rows)

    print(f"[score] sessions={len(session_rows)} → {out}")
    print(f"[score] detection={len(detection_rows)} → {det_out if detection_rows else '（无防御开样本）'}")


if __name__ == "__main__":
    main()
