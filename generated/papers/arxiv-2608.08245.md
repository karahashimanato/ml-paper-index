<!-- このファイルは scripts/generate.py が生成する。手で編集しない。 -->

# Privacy-Preserving Data Drift Detection and Recovery for Large-Scale LLM Applications via Proxy Representations

- カード: [`arxiv-2608.08245`](../../papers/arxiv-2608.08245.yaml)
- 著者: Michael Levit, Josh Ledgard, Haoyu Dong, Vishwas Suryanarayanan, Eyal Kolman, Sharon Tan, Qiang Gan, Vishal Chowdhary
- 年・掲載: 2026
- 原論文: [PDF](https://arxiv.org/pdf/2608.08245v1)(arXiv v1、カード作成時に読んだ版)
- タグ: dataset-shift-detection, dimensionality-reduction-for-shift, large-language-models, unsupervised
- 人手レビュー: 未

## 主張

出典のリンクは原論文PDFの該当ページを開く。リンクにカーソルを合わせると原文の引用が表示される。

- **c1** ProxyDrift identifies and measures drift between production traffic and offline evaluation sets, and builds/refreshes those sets, without access to raw user data.([Abstract, p.1](https://arxiv.org/pdf/2608.08245v1#page=1 "We present PROXYDRIFT, a framework that (i) identifies and measures drift between production traffic and offline evaluation sets, and (ii) constructs and refreshes those evaluation sets accordingly; all without access to raw user data."))
- **c2** Per-dimension drift is measured with the Jensen-Shannon distance on categorical proxy distributions, chosen because it reacts strongly to support mismatches; it is then chance-calibrated against a permutation baseline.([Drift Measurement, p.3](https://arxiv.org/pdf/2608.08245v1#page=3 "Among several candidate distance metrics (Total Variation, Wasserstein, Euclidean, ...), we selected Jensen–Shannon distance (JSD) as the default for categorical distributions because it reacts strongly to support mismatches."))
- **c3** Decision bands are fixed, not learned: the alignment range is split into equal thirds (bad / average / good); dimension importance weights are set by domain experts.([Drift Measurement, p.4](https://arxiv.org/pdf/2608.08245v1#page=4 "we use equal thirds (bad < 1/3, average ≥1/3, good ≥2/3) uniformly throughout the paper."))
- **c4** Drift evaluation setup: one week of production traffic is the reference, against which two synthetic samplers and the legacy hand-curated test set are scored; there are no labeled drift events.([Evaluation (end-to-end drift alignment), p.7](https://arxiv.org/pdf/2608.08245v1#page=7 "Reference distributions were computed from a week of production traffic (2026-04-02 to 2026-04-08)."))
- **c5** The legacy hand-curated offline test set is poorly aligned with production on most dimensions; the paper adds that quality scores were lower on a distribution-aligned synthetic set and says this suggests score inflation in conventional offline evaluation.([Evaluation (end-to-end drift alignment), p.8](https://arxiv.org/pdf/2608.08245v1#page=8 "By contrast, the legacy hand-curated test set fails on most dimensions, with individual per-dimension alignment scores typically below 0.40 and the overall alignment score in the bad range."))
- **c6** The system is deployed in a large commercial productivity suite (all authors are at Microsoft Corporation).([Introduction, p.2](https://arxiv.org/pdf/2608.08245v1#page=2 "PROXYDRIFT has been deployed in a major cloud-based productivity suite serving hundreds of millions of users, where it monitors multiple application scenarios continuously and generates synthetic evaluation data on a weekly cadence."))

