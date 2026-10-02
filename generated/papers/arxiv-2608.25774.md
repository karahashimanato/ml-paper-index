<!-- このファイルは scripts/generate.py が生成する。手で編集しない。 -->

# EXAONE Tabular 1.0 : Technical Report

- カード: [`arxiv-2608.25774`](../../papers/arxiv-2608.25774.yaml)
- 著者: Moonjung Eo, Min-Kook Suh, Hye-Seung Cho, Jiwon Kim, Seoyoon Kim, Sangjun Nam, Soonyoung Lee
- 年・掲載: 2026
- 原論文: [PDF](https://arxiv.org/pdf/2608.25774v1)(arXiv v1、カード作成時に読んだ版)
- タグ: in-context-learning, tabular-attention, tabular-classification, tabular-foundation-model, tabular-regression
- 人手レビュー: 未

## 主張

出典のリンクは原論文PDFの該当ページを開く。リンクにカーソルを合わせると原文の引用が表示される。

- **c1** EXAONE Tabular interleaves feature-axis attention within each item with support-conditioned item-axis attention within each feature at every layer.([Abstract, p.1](https://arxiv.org/pdf/2608.25774v1#page=1 "EXAONE Tabular interleaves feature-axis attention within each item with support-conditioned item-axis attention within each feature at every Transformer layer"))
- **c2** On TabArena, the classification model ranks first overall, surpassing tuned ensembles and 4-hour AutoML pipelines, while regression reaches the performance regime of the much larger TabFM.([Abstract, p.1](https://arxiv.org/pdf/2608.25774v1#page=1 "On TabArena, its 20.81M-parameter classification model ranks first overall, surpassing tuned ensembles and 4-hour AutoML pipelines, while regression reaches the performance regime of the 1.64B-parameter TabFM at roughly 1/11 the inference cost."))
- **c3** TabArena baselines are taken from the official leaderboard, not re-run, so their preprocessing, hyperparameter optimization and ensembling follow the TabArena protocol.([Evaluation protocol, p.10](https://arxiv.org/pdf/2608.25774v1#page=10 "For TabArena, we use the results reported on the official leaderboard rather than re-running each comparison model."))
- **c4** On BCCO and TALENT the comparison is only against six tabular foundation models (no GBDT or neural baselines).([Evaluation protocol, p.10](https://arxiv.org/pdf/2608.25774v1#page=10 "For BCCO and TALENT, we conduct a controlled comparison against six tabular foundation models: TabSwift [31], TabDPT [23], TabPFN-3 [15], TabICLv2 [16], LimiX [19], and TabFM [18]."))
- **c5** On BCCO and TALENT the training/in-context support set is capped at 50,000 samples per fold.([Evaluation protocol, p.10](https://arxiv.org/pdf/2608.25774v1#page=10 "To control computational cost across datasets of different scales, the training or in-context support set was capped at 50,000 samples per fold for both classification and regression."))
- **c6** The model is developed by LG AI Research (company report on its own model).([Introduction, p.2](https://arxiv.org/pdf/2608.25774v1#page=2 "EXAONE Tabular is LG AI Research’s first tabular foundation model family"))

