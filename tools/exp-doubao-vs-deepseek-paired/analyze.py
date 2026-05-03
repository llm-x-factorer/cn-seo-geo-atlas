"""
分析脚本：读取 scored.csv，输出 Markdown 报告。

用法：
  python analyze.py --scored data/scored.csv --out data/results.md

报告内容：
  - 数据概览（采集数 / 失败数 / 缺引用数）
  - 平台 × 信源类别 交叉表（频次 + 百分比 + 95% CI）
  - 平台 × query 类型 × 信源类别 三维表
  - H1 / H2 验证结果
  - 卡方 / Fisher 检验
  - 引用源排名 Wilcoxon
  - 关键发现
"""

from __future__ import annotations

import argparse
import math
from pathlib import Path

import pandas as pd
from scipy import stats


# 与 experiment 设计同步的预注册阈值
H1_DIFF_THRESHOLD_PP = 20  # 强假设阈值
H1_WEAK_DIFF_PP = 5  # 弱效应阈值
H2_DIFF_THRESHOLD_PP = 20

CATEGORIES = [
    "bytedance-eco",
    "baidu-eco",
    "tencent-eco",
    "news-portal",
    "tech-community",
    "vertical-media",
    "central-media",
    "local-media",
    "gov-edu",
    "xiaohongshu",
    "wikipedia-zh",
    "other",
    "no_citation",
]


def parse_args() -> argparse.Namespace:
    p = argparse.ArgumentParser()
    p.add_argument("--scored", required=True)
    p.add_argument("--out", required=True)
    return p.parse_args()


def wilson_ci(k: int, n: int, z: float = 1.96) -> tuple[float, float]:
    """Wilson 95% 置信区间，比正态近似在小样本下更稳。"""
    if n == 0:
        return (0.0, 0.0)
    p = k / n
    denom = 1 + z**2 / n
    center = (p + z**2 / (2 * n)) / denom
    half = (z * math.sqrt(p * (1 - p) / n + z**2 / (4 * n**2))) / denom
    return (max(0.0, center - half), min(1.0, center + half))


def render_overview(df: pd.DataFrame) -> str:
    out = ["## 一、数据概览\n"]
    n_rows = len(df)
    n_sessions = df["session_id"].nunique()
    n_failed = df.loc[df["has_errors"] == True, "session_id"].nunique()
    n_no_citation = df.loc[df["source_category"] == "no_citation", "session_id"].nunique()
    out.append(f"- 总行数：{n_rows}")
    out.append(f"- 总会话数：{n_sessions}")
    out.append(f"- 失败会话数：{n_failed}（{n_failed / max(n_sessions,1):.1%}）")
    out.append(f"- 无引用会话数：{n_no_citation}（{n_no_citation / max(n_sessions,1):.1%}）")

    out.append("\n### 各平台 / query 类型采集分布\n")
    pivot = (
        df.drop_duplicates("session_id")
        .groupby(["platform", "query_type"])
        .size()
        .unstack(fill_value=0)
    )
    out.append(pivot.to_markdown())
    return "\n".join(out) + "\n"


def render_cross_table(df: pd.DataFrame) -> str:
    """平台 × 信源类别 交叉表（仅有引用的行）。"""
    out = ["\n## 二、平台 × 信源类别（含 95% CI）\n"]
    citation_df = df[df["source_category"] != "no_citation"]

    rows = []
    for platform in sorted(citation_df["platform"].dropna().unique()):
        sub = citation_df[citation_df["platform"] == platform]
        total = len(sub)
        for cat in CATEGORIES:
            if cat == "no_citation":
                continue
            k = (sub["source_category"] == cat).sum()
            pct = k / total if total > 0 else 0
            lo, hi = wilson_ci(k, total)
            rows.append(
                {
                    "platform": platform,
                    "category": cat,
                    "count": k,
                    "total": total,
                    "pct": f"{pct:.1%}",
                    "ci_95": f"[{lo:.1%}, {hi:.1%}]",
                }
            )
    table = pd.DataFrame(rows)
    out.append(table.to_markdown(index=False))
    return "\n".join(out) + "\n"


def render_h1(df: pd.DataFrame) -> str:
    """H1：豆包字节系内容引用比例 - DeepSeek 同类比例。"""
    out = ["\n## 三、H1 验证：豆包对字节系内容的偏好\n"]
    citation_df = df[df["source_category"] != "no_citation"]

    def pct_for(platform: str, category: str) -> tuple[int, int]:
        sub = citation_df[citation_df["platform"] == platform]
        total = len(sub)
        k = (sub["source_category"] == category).sum()
        return k, total

    db_k, db_n = pct_for("doubao", "bytedance-eco")
    ds_k, ds_n = pct_for("deepseek", "bytedance-eco")

    db_pct = db_k / db_n if db_n else 0
    ds_pct = ds_k / ds_n if ds_n else 0
    diff_pp = (db_pct - ds_pct) * 100

    db_lo, db_hi = wilson_ci(db_k, db_n)
    ds_lo, ds_hi = wilson_ci(ds_k, ds_n)

    out.append(f"- 豆包 bytedance-eco 引用比例：{db_pct:.1%} (95% CI [{db_lo:.1%}, {db_hi:.1%}], n={db_n})")
    out.append(f"- DeepSeek bytedance-eco 引用比例：{ds_pct:.1%} (95% CI [{ds_lo:.1%}, {ds_hi:.1%}], n={ds_n})")
    out.append(f"- 差值：{diff_pp:+.1f} 个百分点")

    if diff_pp >= H1_DIFF_THRESHOLD_PP:
        verdict = f"**H1 支持**（差值 ≥ {H1_DIFF_THRESHOLD_PP} pp）"
    elif diff_pp <= -H1_DIFF_THRESHOLD_PP:
        verdict = f"**H1 反向证伪**（差值 ≤ -{H1_DIFF_THRESHOLD_PP} pp）"
    elif abs(diff_pp) < H1_WEAK_DIFF_PP:
        verdict = f"**H1 不支持**（差值 < {H1_WEAK_DIFF_PP} pp）"
    else:
        verdict = f"**H1 弱效应**（差值在 {H1_WEAK_DIFF_PP}-{H1_DIFF_THRESHOLD_PP} pp 之间，不下结论）"
    out.append(f"- 判定：{verdict}")

    # Fisher / 卡方
    if min(db_n, ds_n) > 0:
        contingency = [
            [db_k, db_n - db_k],
            [ds_k, ds_n - ds_k],
        ]
        try:
            chi2, p_chi, _, _ = stats.chi2_contingency(contingency)
            out.append(f"- 卡方检验：χ²={chi2:.2f}, p={p_chi:.4g}")
        except Exception as e:
            out.append(f"- 卡方检验失败：{e!r}")

        try:
            _, p_fisher = stats.fisher_exact(contingency)
            out.append(f"- Fisher 精确检验：p={p_fisher:.4g}")
        except Exception:
            pass

    return "\n".join(out) + "\n"


def render_h2(df: pd.DataFrame) -> str:
    """H2：技术 query 下，DeepSeek tech-community 引用比例 - 豆包同类。"""
    out = ["\n## 四、H2 验证：DeepSeek 在技术 query 上的技术社区偏好\n"]
    citation_df = df[
        (df["source_category"] != "no_citation") & (df["query_type"] == "technical")
    ]

    def pct_for(platform: str, category: str) -> tuple[int, int]:
        sub = citation_df[citation_df["platform"] == platform]
        total = len(sub)
        k = (sub["source_category"] == category).sum()
        return k, total

    ds_k, ds_n = pct_for("deepseek", "tech-community")
    db_k, db_n = pct_for("doubao", "tech-community")

    ds_pct = ds_k / ds_n if ds_n else 0
    db_pct = db_k / db_n if db_n else 0
    diff_pp = (ds_pct - db_pct) * 100

    out.append(f"- DeepSeek 技术 query 下 tech-community 引用比例：{ds_pct:.1%} (n={ds_n})")
    out.append(f"- 豆包 技术 query 下 tech-community 引用比例：{db_pct:.1%} (n={db_n})")
    out.append(f"- 差值：{diff_pp:+.1f} 个百分点")

    if diff_pp >= H2_DIFF_THRESHOLD_PP:
        out.append(f"- 判定：**H2 支持**（差值 ≥ {H2_DIFF_THRESHOLD_PP} pp）")
    elif diff_pp <= -H2_DIFF_THRESHOLD_PP:
        out.append(f"- 判定：**H2 反向证伪**")
    elif abs(diff_pp) < H1_WEAK_DIFF_PP:
        out.append(f"- 判定：**H2 不支持**")
    else:
        out.append(f"- 判定：**H2 弱效应**（不下结论）")

    if min(ds_n, db_n) > 0:
        contingency = [[ds_k, ds_n - ds_k], [db_k, db_n - db_k]]
        try:
            chi2, p_chi, _, _ = stats.chi2_contingency(contingency)
            out.append(f"- 卡方：χ²={chi2:.2f}, p={p_chi:.4g}")
        except Exception:
            pass

    return "\n".join(out) + "\n"


def render_query_type_breakdown(df: pd.DataFrame) -> str:
    """平台 × query 类型 × 信源类别 三维（按比例展示）。"""
    out = ["\n## 五、平台 × query 类型 × 信源类别（百分比）\n"]
    citation_df = df[df["source_category"] != "no_citation"]
    grouped = (
        citation_df.groupby(["platform", "query_type", "source_category"])
        .size()
        .reset_index(name="count")
    )
    totals = (
        citation_df.groupby(["platform", "query_type"]).size().reset_index(name="total")
    )
    merged = grouped.merge(totals, on=["platform", "query_type"])
    merged["pct"] = merged["count"] / merged["total"]

    pivot = merged.pivot_table(
        index=["platform", "query_type"],
        columns="source_category",
        values="pct",
        fill_value=0,
    )
    pivot = pivot.applymap(lambda x: f"{x:.1%}")
    out.append(pivot.to_markdown())
    return "\n".join(out) + "\n"


def main():
    args = parse_args()
    df = pd.read_csv(args.scored)

    # 类型规整
    if "online_search_enabled" in df.columns:
        df["online_search_enabled"] = df["online_search_enabled"].astype(str)

    parts = [
        f"# {args.scored} 分析报告\n",
        f"_生成时间：{pd.Timestamp.now().isoformat(timespec='seconds')}_\n",
        render_overview(df),
        render_cross_table(df),
        render_h1(df),
        render_h2(df),
        render_query_type_breakdown(df),
    ]

    out_path = Path(args.out)
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text("\n".join(parts), encoding="utf-8")
    print(f"[done] report → {out_path}")


if __name__ == "__main__":
    main()
