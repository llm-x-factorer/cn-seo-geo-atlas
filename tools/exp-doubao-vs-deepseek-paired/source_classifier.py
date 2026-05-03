"""
信源 URL → 类别 归类规则。

规则与 experiments/exp-doubao-vs-deepseek-paired.md §六 评分 rubric 严格一致。
修改归类规则时务必同步更新该实验设计文档。
"""

from __future__ import annotations

import re
from urllib.parse import urlparse

import tldextract

# 类别优先级（从高到低）
# 当一个 URL 同时符合多个类别时，按此顺序判定
CATEGORY_PRIORITY = [
    "gov-edu",
    "central-media",
    "local-media",
    "bytedance-eco",
    "baidu-eco",
    "tencent-eco",
    "vertical-media",
    "news-portal",
    "tech-community",
    "xiaohongshu",
    "wikipedia-zh",
    "other",
]


# 各类别的判定规则
# 每条规则：(类别, 域名集合 | 正则) — 域名匹配优先于正则
RULES: list[tuple[str, set[str] | re.Pattern]] = [
    (
        "gov-edu",
        re.compile(r"\.(gov|edu)\.cn$|^cas\.cn$|^cssn\.cn$|^cae\.cn$"),
    ),
    (
        "central-media",
        {
            "people.com.cn",
            "xinhuanet.com",
            "cctv.com",
            "cntv.cn",
            "gmw.cn",
            "cnr.cn",
            "china.com.cn",
            "chinanews.com.cn",
            "chinanews.com",
            "cri.cn",
            "youth.cn",
            "ce.cn",
            "stdaily.com",
        },
    ),
    (
        "local-media",
        re.compile(
            r"^(thepaper\.cn|jfdaily\.com|yzdsb\.com\.cn|dahebao\.cn|"
            r"hebnews\.cn|sxrb\.com|nfnews\.com|nbd\.com\.cn|cnhubei\.com|"
            r"hnr\.cn|qlwb\.com\.cn|sznews\.com|hangzhou\.com\.cn|"
            r"thepaper\.cn|qianlong\.com|eastday\.com|dzwww\.com|"
            r"bjd\.com\.cn|wenweipo\.com|takungpao\.com)$"
        ),
    ),
    (
        "bytedance-eco",
        {
            "toutiao.com",
            "bytedance.com",
            "douyin.com",
            "ixigua.com",
            "snssdk.com",
            "feishu.cn",
            "lark.com",
        },
    ),
    (
        "bytedance-eco",  # 抖音 / 快懂百科子域单独捕获
        re.compile(
            r"^baike\.douyin\.com$|^baike\.so\.com$|^baike\.toutiao\.com$"
        ),
    ),
    (
        "baidu-eco",
        re.compile(
            r"^baijiahao\.baidu\.com$|^baike\.baidu\.com$|"
            r"^zhidao\.baidu\.com$|^wenku\.baidu\.com$|"
            r"^jingyan\.baidu\.com$|^xueshu\.baidu\.com$|"
            r"^mbd\.baidu\.com$|^haokan\.baidu\.com$|"
            r"^iknow\.baidu\.com$|^muzhi\.baidu\.com$|^aiqicha\.baidu\.com$"
        ),
    ),
    (
        "tencent-eco",
        re.compile(
            r"^mp\.weixin\.qq\.com$|"
            r"^channels\.weixin\.qq\.com$|"
            r"^zhuanlan\.zhihu\.com$|"
            r"^docs\.qq\.com$"
        ),
    ),
    (
        "vertical-media",
        {
            "36kr.com",
            "huxiu.com",
            "tmtpost.com",
            "iyiou.com",
            "geekpark.net",
            "leiphone.com",
            "pingwest.com",
            "ifanr.com",
            "dxy.com",
            "dxy.cn",
            "haodf.com",
            "yixinli.com",
            "jiemian.com",
            "yicai.com",
            "caixin.com",
            "cls.cn",
            "stcn.com",
            "21jingji.com",
            "autohome.com.cn",
            "bitauto.com",
            "pcauto.com.cn",
            "to8to.com",
            "fang.com",
        },
    ),
    (
        "news-portal",
        {
            "sina.com.cn",
            "sina.cn",
            "163.com",
            "sohu.com",
            "qq.com",  # 注意：news.qq.com 走门户，但 mp.weixin.qq.com 已先归 tencent-eco
            "ifeng.com",
            "huanqiu.com",
            "global.com",
        },
    ),
    (
        "tech-community",
        re.compile(
            r"^(www\.)?csdn\.net$|"
            r"^(.*\.)?juejin\.cn$|"
            r"^github\.com$|"
            r"^stackoverflow\.com$|"
            r"^oschina\.net$|"
            r"^segmentfault\.com$|"
            r"^cnblogs\.com$|"
            r"^v2ex\.com$"
        ),
    ),
    (
        "xiaohongshu",
        re.compile(r"^(www\.)?xiaohongshu\.com$|^xhslink\.com$"),
    ),
    (
        "wikipedia-zh",
        re.compile(r"^zh\.wikipedia\.org$|^wikipedia\.org$"),
    ),
]


def normalize_domain(url: str) -> str:
    """从 URL 提取规范化域名（含子域），小写。"""
    if not url:
        return ""
    parsed = urlparse(url if "://" in url else f"http://{url}")
    return parsed.netloc.lower()


def registered_domain(url: str) -> str:
    """从 URL 提取注册域名（不含子域）。例：news.sina.com.cn → sina.com.cn"""
    ext = tldextract.extract(url)
    if not ext.domain:
        return ""
    return ".".join(part for part in [ext.domain, ext.suffix] if part)


def classify(url: str) -> str:
    """
    按 CATEGORY_PRIORITY 顺序匹配 RULES，返回第一个命中的类别。
    没有命中返回 'other'。
    """
    if not url:
        return "other"

    domain = normalize_domain(url)
    reg_domain = registered_domain(url)

    # 知乎特殊处理：问答页 → tech-community；专栏 → tencent-eco
    if reg_domain == "zhihu.com":
        if "/question/" in url or "/answer/" in url:
            return "tech-community"
        if domain.startswith("zhuanlan.") or "/p/" in url:
            return "tencent-eco"
        return "tech-community"  # 兜底归技术社区

    # 按优先级遍历规则
    matched = []
    for category, rule in RULES:
        if isinstance(rule, set):
            if reg_domain in rule or domain in rule:
                matched.append(category)
        elif isinstance(rule, re.Pattern):
            if rule.search(domain):
                matched.append(category)

    if not matched:
        return "other"

    # 返回最高优先级的类别
    for category in CATEGORY_PRIORITY:
        if category in matched:
            return category

    return "other"


def classify_batch(urls: list[str]) -> list[tuple[str, str]]:
    """批量归类，返回 [(url, category), ...]"""
    return [(url, classify(url)) for url in urls]


if __name__ == "__main__":
    test_cases = [
        ("https://www.toutiao.com/article/123", "bytedance-eco"),
        ("https://baijiahao.baidu.com/s?id=123", "baidu-eco"),
        ("https://baike.baidu.com/item/X", "baidu-eco"),
        ("https://mp.weixin.qq.com/s/abc", "tencent-eco"),
        ("https://www.zhihu.com/question/123/answer/456", "tech-community"),
        ("https://zhuanlan.zhihu.com/p/123", "tencent-eco"),
        ("https://blog.csdn.net/u/p/123", "tech-community"),
        ("https://news.sina.com.cn/c/123.html", "news-portal"),
        ("https://news.qq.com/x/y", "news-portal"),
        ("https://www.people.com.cn/n1/2026/0501/c123.html", "central-media"),
        ("https://36kr.com/p/123", "vertical-media"),
        ("https://www.xiaohongshu.com/discovery/item/123", "xiaohongshu"),
        ("https://zh.wikipedia.org/wiki/X", "wikipedia-zh"),
        ("https://www.tsinghua.edu.cn/info/123", "gov-edu"),
        ("https://www.beijing.gov.cn/zhengce", "gov-edu"),
        ("https://github.com/owner/repo", "tech-community"),
        ("https://random-blog.example.com/post", "other"),
    ]

    print("Self-test:")
    failures = 0
    for url, expected in test_cases:
        actual = classify(url)
        status = "✓" if actual == expected else "✗"
        if actual != expected:
            failures += 1
        print(f"  {status} {url:60} → {actual} (expected {expected})")

    print(f"\n{len(test_cases) - failures}/{len(test_cases)} passed")
    if failures > 0:
        raise SystemExit(1)
