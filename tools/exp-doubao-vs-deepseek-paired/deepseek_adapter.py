"""
DeepSeek Web 端（chat.deepseek.com）适配器。

⚠️ selector 待 pilot 验证。详见 doubao_adapter.py 的相同说明。

DeepSeek 特殊性：
- 同一 query 可能被路由到不同模型（V 系列 / R 系列）
- UI 上有"深度思考"切换 + "联网搜索"切换
- 引用源的展示形态与豆包不同（通常是答案末尾的引用列表）
"""

from __future__ import annotations

import asyncio
import time
from typing import Any

from playwright.async_api import Page, TimeoutError as PlaywrightTimeoutError


SELECTORS = {
    "input_textarea": "textarea[placeholder*='发送消息']",  # TODO: pilot-verify
    "send_button": "button[type='submit']",  # TODO: pilot-verify
    "answer_container": "[class*='message']:last-of-type",  # TODO: pilot-verify
    "generating_indicator": "[class*='generating'], button[disabled]",  # TODO: pilot-verify
    "citation_list": "[class*='reference'], [class*='source'], [class*='citation']",  # TODO: pilot-verify
    "citation_link": "a[href]",  # TODO: pilot-verify
    "online_search_toggle": "button[aria-label*='联网搜索']",  # TODO: pilot-verify
    "deep_thinking_toggle": "button[aria-label*='深度思考']",  # TODO: pilot-verify
    "model_indicator": "[class*='model-name'], [class*='model-tag']",  # TODO: pilot-verify
}


URL = "https://chat.deepseek.com"
PLATFORM_NAME = "deepseek"


async def collect(
    page: Page,
    query: str,
    config: dict[str, Any],
    *,
    online_search: bool = True,
) -> dict[str, Any]:
    timeout_s = config.get("timeout_seconds", 60)
    errors: list[str] = []

    result: dict[str, Any] = {
        "platform": PLATFORM_NAME,
        "platform_url": URL,
        "query_text": query,
        "online_search_enabled": online_search,
        "model_id": None,
        "platform_version": None,
        "raw_response_text": None,
        "raw_response_html": None,
        "citation_sources": [],
        "screenshot_path": None,
        "response_time_ms": None,
        "errors": errors,
    }

    started_at = time.time()

    try:
        await page.goto(URL, wait_until="domcontentloaded", timeout=30_000)

        await page.wait_for_selector(
            SELECTORS["input_textarea"], state="visible", timeout=15_000
        )

        if not online_search:
            errors.append(
                "online_search=False but adapter does not yet implement toggle off"
            )

        await page.fill(SELECTORS["input_textarea"], query)
        await page.click(SELECTORS["send_button"])

        # 等待答案生成
        deadline = time.time() + timeout_s
        last_text = ""
        stable_iters = 0
        while time.time() < deadline:
            await asyncio.sleep(1)
            try:
                indicator = await page.query_selector(SELECTORS["generating_indicator"])
                if indicator is None:
                    cur_text = await _get_answer_text(page)
                    if cur_text == last_text and cur_text:
                        stable_iters += 1
                        if stable_iters >= 3:
                            break
                    else:
                        stable_iters = 0
                    last_text = cur_text
            except Exception as e:
                errors.append(f"polling error: {e!r}")

        # 抽取模型标识（如 UI 显示）
        try:
            model_el = await page.query_selector(SELECTORS["model_indicator"])
            if model_el:
                result["model_id"] = (await model_el.inner_text()).strip()
        except Exception:
            pass

        result["raw_response_text"] = await _get_answer_text(page)
        result["raw_response_html"] = await _get_answer_html(page)
        result["citation_sources"] = await _extract_citations(page)

        if config.get("screenshot_path"):
            await page.screenshot(path=config["screenshot_path"], full_page=True)
            result["screenshot_path"] = config["screenshot_path"]

    except PlaywrightTimeoutError as e:
        errors.append(f"timeout: {e!r}")
    except Exception as e:
        errors.append(f"unexpected: {e!r}")

    result["response_time_ms"] = int((time.time() - started_at) * 1000)
    return result


async def _get_answer_text(page: Page) -> str:
    el = await page.query_selector(SELECTORS["answer_container"])
    if el is None:
        return ""
    return (await el.inner_text()).strip()


async def _get_answer_html(page: Page) -> str:
    el = await page.query_selector(SELECTORS["answer_container"])
    if el is None:
        return ""
    return await el.inner_html()


async def _extract_citations(page: Page) -> list[dict[str, Any]]:
    citations: list[dict[str, Any]] = []
    list_el = await page.query_selector(SELECTORS["citation_list"])
    if list_el is None:
        return citations

    links = await list_el.query_selector_all(SELECTORS["citation_link"])
    for rank, link in enumerate(links, start=1):
        href = await link.get_attribute("href")
        title = (await link.inner_text()).strip()
        if href:
            citations.append({"rank": rank, "title": title or None, "url": href})
    return citations
