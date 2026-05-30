"""检索器 + 防御层。

backend:
  bge  = BAAI/bge-small-zh-v1.5（sentence-transformers）
  hash = 无依赖 hashing embedding（smoke test）
  auto = 有 sentence-transformers 用 bge，否则 hash

防御（defense_state='on' 时）：
  1) KE：检索文档数 top_k_off → top_k_on
  2) 来源白名单：仅 whitelist_source_types 进上下文
  3) 困惑度过滤：候选文档异常分 z-score 超阈值则丢弃
"""

from __future__ import annotations

import numpy as np

import corpus_io


class Retriever:
    def __init__(self, cfg: dict):
        self.cfg = cfg
        rcfg = cfg.get("retriever", {})
        self.backend = rcfg.get("backend", "auto")
        self.bge_model_name = rcfg.get("bge_model", "BAAI/bge-small-zh-v1.5")
        self.dim = 256
        self._bge = None
        if self.backend == "auto":
            self.backend = "bge" if self._try_load_bge() else "hash"
        elif self.backend == "bge":
            if not self._try_load_bge():
                raise SystemExit("retriever.backend=bge 但 sentence-transformers 不可用")
        self._ppl = _PerplexityScorer(cfg)
        print(f"[retriever] backend={self.backend} ppl={self._ppl.backend}")

    def _try_load_bge(self) -> bool:
        try:
            from sentence_transformers import SentenceTransformer

            self._bge = SentenceTransformer(self.bge_model_name)
            return True
        except Exception:
            return False

    def embed(self, texts: list[str]) -> np.ndarray:
        if self.backend == "bge":
            return np.asarray(
                self._bge.encode(texts, normalize_embeddings=True, show_progress_bar=False),
                dtype=np.float32,
            )
        return corpus_io.hash_embed(texts, self.dim)

    def retrieve(
        self,
        query_text: str,
        docs: list[dict],
        doc_emb: np.ndarray,
        defense_state: str,
        query_id: str,
    ) -> dict:
        rcfg = self.cfg.get("retriever", {})
        dcfg = self.cfg.get("defense", {})
        on = defense_state == "on"
        top_k = rcfg.get("top_k_on", 20) if on else rcfg.get("top_k_off", 5)

        qv = self.embed([query_text])[0]
        order = corpus_io.cosine_topk(qv, doc_emb, top_k)
        cand_docs = [docs[i] for i in order]
        cand_scores = [float(doc_emb[i] @ qv) for i in order]

        wl_enabled = bool(dcfg.get("source_whitelist_enabled", True))
        wl_types = set(dcfg.get("whitelist_source_types", []))
        ppl_enabled = bool(dcfg.get("perplexity_filter_enabled", True))
        z_thr = float(dcfg.get("perplexity_zscore_drop", 2.0))

        # 困惑度异常分（仅防御开时计算，H3 只用防御开的样本）
        if on and ppl_enabled:
            anomalies = [self._ppl.anomaly(d["text"]) for d in cand_docs]
            zs = corpus_io.zscores(anomalies)
        else:
            zs = [0.0] * len(cand_docs)

        candidates = []
        context = []
        poison_diag = []
        for d, sc, z in zip(cand_docs, cand_scores, zs):
            f_wl = bool(on and wl_enabled and (d["source_type"] not in wl_types))
            f_ppl = bool(on and ppl_enabled and (z > z_thr))
            in_ctx = not (f_wl or f_ppl)
            candidates.append(
                {
                    "doc_id": d["doc_id"],
                    "score": sc,
                    "is_poison": d["is_poison"],
                    "poison_style": d["poison_style"],
                    "source_type": d["source_type"],
                    "asserts": d["asserts"],
                    "filtered_by_whitelist": f_wl,
                    "filtered_by_ppl": f_ppl,
                    "ppl_z": float(z),
                    "in_context": in_ctx,
                }
            )
            if in_ctx:
                context.append(d)
            if on and d["is_poison"]:
                poison_diag.append({"style": d["poison_style"], "filtered_by_ppl": f_ppl})

        poison_in_context = sum(1 for d in context if d["is_poison"])
        # 只数与本 query 相关的真答案文档（同 query_id）才算"竞争性 clean 信源"；
        # 别的实体的 true 文档即便串进 top-k 也不构成对本主张的反驳。
        clean_true_in_context = sum(
            1
            for d in context
            if (not d["is_poison"]) and d["asserts"] == "true" and d["query_id"] == query_id
        )
        return {
            "candidates": candidates,
            "context": context,
            "poison_in_context": poison_in_context,
            "clean_true_in_context": clean_true_in_context,
            "poison_diag": poison_diag,
        }


class _PerplexityScorer:
    """困惑度异常分。hf = 真实 LM PPL；heuristic = 流畅度 proxy。"""

    def __init__(self, cfg: dict):
        backend = cfg.get("defense", {}).get("perplexity_backend", "auto")
        self.model_name = cfg.get("defense", {}).get(
            "perplexity_hf_model", "uer/gpt2-chinese-cluecorpussmall"
        )
        self._tok = None
        self._lm = None
        if backend == "auto":
            backend = "hf" if self._try_load_hf() else "heuristic"
        elif backend == "hf":
            if not self._try_load_hf():
                raise SystemExit("perplexity_backend=hf 但 transformers/torch 不可用")
        self.backend = backend

    def _try_load_hf(self) -> bool:
        try:
            import torch  # noqa: F401
            from transformers import AutoModelForCausalLM, AutoTokenizer

            self._tok = AutoTokenizer.from_pretrained(self.model_name)
            self._lm = AutoModelForCausalLM.from_pretrained(self.model_name)
            self._lm.eval()
            return True
        except Exception:
            return False

    def anomaly(self, text: str) -> float:
        if self.backend == "hf":
            return self._hf_ppl(text)
        return corpus_io.fluency_anomaly_score(text)

    def _hf_ppl(self, text: str) -> float:
        import torch

        enc = self._tok(text, return_tensors="pt", truncation=True, max_length=256)
        with torch.no_grad():
            out = self._lm(**enc, labels=enc["input_ids"])
        return float(torch.exp(out.loss).item())
