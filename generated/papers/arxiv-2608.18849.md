<!-- このファイルは scripts/generate.py が生成する。手で編集しない。 -->

# GEAR: Generative Expansion and Real Anchoring for Two-Stage Distillation of Tabular Foundation Models

- カード: [`arxiv-2608.18849`](../../papers/arxiv-2608.18849.yaml)
- 著者: Qi Qin, Jiajie Zhu, Dali Chen, Yuzhao Zhang, Jia-Xing Han, Peng Zhang, Ying Yan, Yifan Sun, Yu Su
- 年・掲載: 2026
- 原論文: [PDF](https://arxiv.org/pdf/2608.18849v2)(arXiv v2、カード作成時に読んだ版)
- タグ: gradient-boosted-trees, in-context-learning, knowledge-distillation, model-compression, supervised, tabular-classification, tabular-foundation-model, tabular-mlp
- 人手レビュー: 未

## 主張

出典のリンクは原論文PDFの該当ページを開く。リンクにカーソルを合わせると原文の引用が表示される。

- **c1** GEAR distills TFMs into lightweight MLP or tree-based predictors deployable on commodity CPUs.([Abstract, p.1](https://arxiv.org/pdf/2608.18849v2#page=1 "We propose GEAR (Generative Expansion and Real Anchoring), a modular two-stage framework that distills TFMs into lightweight MLP or tree-based predictors that can be deployed on commodity CPUs."))
- **c2** Stage 2 uses out-of-fold teacher predictions on real rows to avoid self-labeling leakage.([Abstract, p.1](https://arxiv.org/pdf/2608.18849v2#page=1 "Stage 2 re-anchors the student to the target distribution using real labels and out-of-fold teacher predictions, which avoids self-labeling leakage."))
- **c3** On binary tasks the gains transfer to LightGBM and XGBoost students, and all three student families outperform CatBoost in mean AUC.([Abstract, p.1](https://arxiv.org/pdf/2608.18849v2#page=1 "On binary tasks, the gains also transfer to LightGBM and XGBoost, and all three student families outperform CatBoost, the strongest non-TFM baseline, in mean AUC."))
- **c4** Evaluation is on TALENT and TabArena with ROC-AUC (binary) and macro one-vs-rest AUC (multiclass), averaged over five random runs.([Experimental setup, p.4](https://arxiv.org/pdf/2608.18849v2#page=4 "For all settings, we use ROC-AUC for binary classification and macro one-vs-rest AUC for multiclass classification; reported values are averaged over five random runs."))
- **c5** Detailed optimization settings and implementation are deferred to the supplementary material; how the supervised baselines (CatBoost, RealMLP, TabM) were tuned, and dataset counts or size limits, were not found in the main text.([Experimental setup, p.5](https://arxiv.org/pdf/2608.18849v2#page=5 "Detailed optimization settings and implementation are provided in the supplementary material."))
- **c6** The work covers classification and single-teacher distillation only.([Conclusion, p.7](https://arxiv.org/pdf/2608.18849v2#page=7 "Although this work focuses on classification and single-teacher distillation, GEAR could be extended to regression and multi-teacher distillation."))

