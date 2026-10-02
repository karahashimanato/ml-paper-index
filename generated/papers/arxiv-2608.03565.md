<!-- このファイルは scripts/generate.py が生成する。手で編集しない。 -->

# Enhancing Tabular Learners with Context-Aware Semantic Embeddings

- カード: [`arxiv-2608.03565`](../../papers/arxiv-2608.03565.yaml)
- 著者: Günther Schindler, Maximilian Schambach, Johannes Höhne
- 年・掲載: 2026
- 原論文: [PDF](https://arxiv.org/pdf/2608.03565v1)(arXiv v1、カード作成時に読んだ版)
- タグ: large-language-models, supervised, tabular-classification, tabular-foundation-model, tabular-regression
- 人手レビュー: 未

## 主張

出典のリンクは原論文PDFの該当ページを開く。リンクにカーソルを合わせると原文の引用が表示される。

- **c1** CASE improves tabular learners on semantically rich datasets (CARTE, TextTab), particularly in low-data regimes.([Abstract, p.1](https://arxiv.org/pdf/2608.03565v1#page=1 "Our experiments across several benchmarks (CARTE, TextTab, and TabArena) demonstrate that CASE substantially improves the performance of tabular learners on semantically rich datasets, particularly in low-data regimes."))
- **c2** On the numerics-heavy TabArena benchmark there is a small trade-off: the raw learners (TabICLv2, AutoGluon) keep a lead.([Results, p.6](https://arxiv.org/pdf/2608.03565v1#page=6 "While showcasing significant improvements on semantically rich benchmarks, we observe a small performance trade-off on the numerics-heavy TabArena benchmark, where the raw statistical learners (TabICLv2 and AutoGluon) maintain a lead."))
- **c3** Evaluation uses CARTE, TextTab, and only the single-fold variant of TabArena.([Experimental setup, p.5](https://arxiv.org/pdf/2608.03565v1#page=5 "We evaluate our approach across three distinct benchmark suites: CARTE [18], TextTab [22], and the single-fold variant of TabArena [7]."))
- **c4** XGBoost, CatBoost and RealMLP (via pytabkit) are tuned with ensembled hyperparameter optimization across 5-fold inner cross-validation, using TabArena search spaces.([Appendix (Baseline details), p.13](https://arxiv.org/pdf/2608.03565v1#page=13 "We evaluate these models with ensembled hyperparameter optimization across 5-fold inner cross-validation (HPO-CV)."))
- **c5** The cited check for overlap between the T4 continued-pretraining corpus and evaluation data was done in related work [27] and covers the CARTE benchmark.([Appendix (Data contamination), p.16](https://arxiv.org/pdf/2608.03565v1#page=16 "Related work [27] conducted a systematic search for overlap between the T4 training set and the CARTE benchmark."))
- **c6** Co-author Maximilian Schambach is also an author of ConTextTab [27], one of the evaluated baselines (per the reference list).([References, p.11](https://arxiv.org/pdf/2608.03565v1#page=11 "Marco Spinaci, Marek Polewczyk, Maximilian Schambach, and Sam Thelin."))

