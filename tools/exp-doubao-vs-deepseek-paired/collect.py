"""
主采集脚本。

用法：
  # pilot run（建议首次执行 / selector 变更后跑）
  python collect.py --pilot --queries 2 --platforms doubao,deepseek

  # 主采集
  python collect.py

  # 限定平台 / 时段
  python collect.py --platforms doubao --time-window day1-am
"""

from __future__ import annotations

import argparse
import asyncio
import json
import random
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

import yaml
from playwright.async_api import async_playwright

import doubao_adapter
import deepseek_adapter


PLATFORM_ADAPTERS = {
    "doubao": doubao_adapter,
    "deepseek": deepseek_adapter,
}


def load_yaml(path: Path) -> dict[str, Any]:
    return yaml.safe_load(path.read_text(encoding="utf-8"))


def now_iso() -> str:
    return datetime.now(timezone.utc).astimezone().isoformat(timespec="seconds")


def make_session_id(experiment_id: str, platform: str, query_id: str, rep: int) -> str:
    ts = datetime.now().strftime("%Y%m%d-%H%M%S")
    return f"{experiment_id}__{platform}__{query_id}__rep{rep}__{ts}"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--config", default="config.yaml")
    parser.add_argument("--queries-file", default="queries.yaml")
    parser.add_argument(
        "--platforms",
        default="doubao,deepseek",
        help="逗号分隔的平台列表",
    )
    parser.add_argument("--pilot", action="store_true", help="pilot 模式（少量采集 + headless=false）")
    parser.add_argument(
        "--queries",
        type=int,
        default=None,
        help="只跑前 N 个 query（pilot 时使用）",
    )
    parser.add_argument(
        "--repetitions",
        type=int,
        default=None,
        help="覆盖配置中的 repetitions",
    )
    parser.add_argument("--time-window", default=None, help="时段标签，仅记录用，不影响实际行为")
    return parser.parse_args()


async def run_one(
    p,
    platform: str,
    query: dict[str, Any],
    rep: int,
    config: dict[str, Any],
    out_dir: Path,
    args: argparse.Namespace,
) -> dict[str, Any]:
    """跑一次采集，返回数据 dict（含错误时也返回）。"""
    adapter = PLATFORM_ADAPTERS[platform]
    session_id = make_session_id(
        config["experiment_id"], platform, query["id"], rep
    )

    # 数据存放路径
    record_dir = out_dir / "raw" / platform / query["id"]
    record_dir.mkdir(parents=True, exist_ok=True)
    json_path = record_dir / f"rep{rep}__{session_id}.json"
    screenshot_path = (
        out_dir / config.get("screenshots_subdir", "screenshots") / platform / query["id"]
    )
    screenshot_path.mkdir(parents=True, exist_ok=True)
    screenshot_file = screenshot_path / f"rep{rep}__{session_id}.png"

    # fresh 浏览器 context
    headless = args.pilot is False and config.get("headless", True)
    if args.pilot:
        headless = False

    browser = await p.chromium.launch(headless=headless)
    context = await browser.new_context(
        viewport=config.get("viewport", {"width": 1440, "height": 900}),
        locale=config.get("locale", "zh-CN"),
        timezone_id=config.get("timezone", "Asia/Shanghai"),
    )
    page = await context.new_page()

    online_search = bool(config.get("online_search", {}).get(platform, True))

    record: dict[str, Any] = {
        "experiment_id": config["experiment_id"],
        "session_id": session_id,
        "platform": platform,
        "query_id": query["id"],
        "query_type": query["type"],
        "query_text": query["text"],
        "repetition": rep,
        "online_search_enabled": online_search,
        "geo_ip_province": config.get("geo_ip_province", ""),
        "network_note": config.get("network_note", ""),
        "time_window_label": args.time_window or "",
        "timestamp_iso": now_iso(),
    }

    try:
        adapter_result = await adapter.collect(
            page,
            query["text"],
            {**config, "screenshot_path": str(screenshot_file)},
            online_search=online_search,
        )
        record.update(adapter_result)
    except Exception as e:
        record["errors"] = [f"runner_error: {e!r}"]
    finally:
        await context.close()
        await browser.close()

    # 落盘
    json_path.write_text(
        json.dumps(record, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )

    return record


async def main():
    args = parse_args()
    config = load_yaml(Path(args.config))
    queries_doc = load_yaml(Path(args.queries_file))
    queries: list[dict[str, Any]] = queries_doc["queries"]

    if args.queries is not None:
        queries = queries[: args.queries]

    repetitions = args.repetitions or config.get("repetitions", 5)
    if args.pilot:
        repetitions = 1

    platforms = [p.strip() for p in args.platforms.split(",") if p.strip()]
    out_dir = Path(config["data_dir"])
    out_dir.mkdir(parents=True, exist_ok=True)

    cooldown = config.get("cooldown_seconds", 30)
    fail_log_path = Path(
        config.get("fail_log_path") or (out_dir / "failures.jsonl")
    )
    fail_log_path.parent.mkdir(parents=True, exist_ok=True)

    consecutive_failures = 0
    max_consec = config.get("max_consecutive_failures", 5)

    total = len(platforms) * len(queries) * repetitions
    done = 0

    print(
        f"[collect] experiment={config['experiment_id']} "
        f"platforms={platforms} queries={len(queries)} reps={repetitions} "
        f"total={total} pilot={args.pilot}"
    )

    async with async_playwright() as p:
        for platform in platforms:
            if platform not in PLATFORM_ADAPTERS:
                print(f"[skip] unknown platform: {platform}")
                continue
            for query in queries:
                for rep in range(repetitions):
                    done += 1
                    print(
                        f"[{done}/{total}] {platform} {query['id']} rep={rep} ..."
                    )
                    record = await run_one(
                        p, platform, query, rep, config, out_dir, args
                    )

                    failed = bool(record.get("errors"))
                    if failed:
                        consecutive_failures += 1
                        with fail_log_path.open("a", encoding="utf-8") as f:
                            f.write(
                                json.dumps(record, ensure_ascii=False) + "\n"
                            )
                        print(f"  ✗ failed: {record['errors']}")
                    else:
                        consecutive_failures = 0
                        print(f"  ✓ ok ({record.get('response_time_ms')}ms)")

                    if consecutive_failures >= max_consec:
                        print(
                            f"[abort] {consecutive_failures} consecutive failures, "
                            f"check {fail_log_path} and platform UI"
                        )
                        return

                    # 抖动 cooldown 避免规律性请求
                    jitter = random.uniform(0.7, 1.3)
                    await asyncio.sleep(cooldown * jitter)

    print(f"[done] collected {done} sessions to {out_dir}")


if __name__ == "__main__":
    asyncio.run(main())
