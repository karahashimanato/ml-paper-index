<!-- このファイルは scripts/generate.py が生成する。手で編集しない。 -->

# What You Observe Determines How You Identify Causal Effects: Evaluating Causal Models across Observational Views

- カード: [`arxiv-2609.36881`](../../papers/arxiv-2609.36881.yaml)
- 著者: Heejin Jung, Gyeongdeok Seo, Hoyoon Byun, Joseph Lee, Kyungwoo Song
- 年・掲載: 2026
- 原論文: [PDF](https://arxiv.org/pdf/2609.36881v1)(arXiv v1、カード作成時に読んだ版)
- タグ: causal-effect-estimation, in-context-learning, tabular-foundation-model
- 人手レビュー: 未

## 主張

出典のリンクは原論文PDFの該当ページを開く。リンクにカーソルを合わせると原文の引用が表示される。

- **c1** CausalIDView holds the SCM realization and target estimand fixed and varies only the observational view given to the estimator.([Abstract, p.1](https://arxiv.org/pdf/2609.36881v1#page=1 "a multi-view benchmark that holds the SCM realization and target estimand fixed while varying only the observational view available to the estimator."))
- **c2** Across matched views, no causal foundation model is consistently best and rankings vary substantially.([Abstract, p.1](https://arxiv.org/pdf/2609.36881v1#page=1 "Across these matched views, no CFM consistently performs best and model rankings vary substantially."))
- **c3** A modular approach pairing a predictive TFM with regime-specific identification procedures is competitive with CFMs and beats several of them.([Abstract, p.1](https://arxiv.org/pdf/2609.36881v1#page=1 "A modular approach that pairs a predictive tabular foundation model with regime-specific identification procedures is competitive with CFMs and outperforms several of them."))
- **c4** CFMs are evaluated with their released checkpoints without fine-tuning.([Appendix, p.26](https://arxiv.org/pdf/2609.36881v1#page=26 "We evaluate CausalPFN, Do-PFN, and CausalFM (Balazadeh Meresht et al., 2026; Ma et al., 2026; Robertson et al., 2026) using their released checkpoints without fine-tuning."))
- **c5** Predictive backbones in the modular estimators use fixed settings and package defaults with no hyperparameter optimization.([Appendix, p.27](https://arxiv.org/pdf/2609.36881v1#page=27 "All remaining parameters use the corresponding package defaults and we perform no hyperparameter optimization."))
- **c6** The comparisons concern the evaluated model-input configurations, not natively supported estimators in every regime.([Appendix, p.26](https://arxiv.org/pdf/2609.36881v1#page=26 "These comparisons concern the evaluated model–input configurations, not equally supported native estimators in every regime."))

