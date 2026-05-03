"""
评分脚本：读取原始采集 JSON，应用 source_classifier 的归类规则，输出长格式 CSV。

用法：
  python score.py --data-dir data/raw --out data/scored.csv

输出 CSV 字段（每行一个引用源）：
  experiment_id, session_id, platform, query_id, query_type, repetition,
  timestamp_iso, online_search_enabled, model_id,
  source_rank, source_url, source_domain, source_category,
  total_citations_in_response, has_errors

如果一次采集没有任何引用源，仍会保留一条记录（source_rank=NA）以便统计 base rate。
"""

from __future__ import annotations

import argparse
import csv
import json
from pathlib import Path
from typing import Any

import tldextract

from source_classifier import classify, normalize_domain


CSV_FIELDS = [
    "experiment_id",
    "session_id",
    "platform",
    "query_id",
    "query_type",
    "repetition",
    "timestamp_iso",
    "online_search_enabled",
    "model_id",
    "source_rank",
    "source_url",
    "source_domain",
    "source_category",
    "total_citations_in_response",
    "has_errors",
]


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--data-dir", required=True, help="采集 raw 目录（含 platform/query_id 子树）")
    parser.add_argument("--out", required=True, help="输出 CSV 路径")
    return parser.parse_args()


def iter_raw_records(data_dir: Path):
    for json_path in sorted(data_dir.rglob("*.json")):
        try:
            yield json.loads(json_path.read_text(encoding="utf-8"))
        except Exception as e:
            print(f"[skip] {json_path}: {e!r}")


def record_to_rows(record: dict[str, Any]) -> list[dict[str, Any]]:
    base = {
        "experiment_id": record.get("experiment_id"),
        "session_id": record.get("session_id"),
        "platform": record.get("platform"),
        "query_id": record.get("query_id"),
        "query_type": record.get("query_type"),
        "repetition": record.get("repetition"),
        "timestamp_iso": record.get("timestamp_iso"),
        "online_search_enabled": record.get("online_search_enabled"),
        "model_id": record.get("model_id"),
        "has_errors": bool(record.get("errors")),
    }
    citations = record.get("citation_sources") or []
    base["total_citations_in_response"] = len(citations)

    if not citations:
        # 即使无引用，也保留一行以便统计 base rate
        return [
            {
                **base,
                "source_rank": "",
                "source_url": "",
                "source_domain": "",
                "source_category": "no_citation",
            }
        ]

    rows = []
    for c in citations:
        url = c.get("url") or ""
        rows.append(
            {
                **base,
                "source_rank": c.get("rank"),
                "source_url": url,
                "source_domain": normalize_domain(url),
                "source_category": classify(url),
            }
        )
    return rows


def main():
    args = parse_args()
    data_dir = Path(args.data_dir)
    out_path = Path(args.out)
    out_path.parent.mkdir(parents=True, exist_ok=True)

    n_records = 0
    n_rows = 0

    with out_path.open("w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=CSV_FIELDS)
        writer.writeheader()

        for record in iter_raw_records(data_dir):
            n_records += 1
            for row in record_to_rows(record):
                writer.writerow(row)
                n_rows += 1

    print(f"[done] {n_records} records → {n_rows} rows → {out_path}")


if __name__ == "__main__":
    main()
