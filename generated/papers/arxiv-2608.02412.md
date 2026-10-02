<!-- このファイルは scripts/generate.py が生成する。手で編集しない。 -->

# Why Large Language Models Fail at Tabular Prediction

- カード: [`arxiv-2608.02412`](../../papers/arxiv-2608.02412.yaml)
- 著者: Marta Garnelo, Wojciech M. Czarnecki
- 年・掲載: 2026
- 原論文: [PDF](https://arxiv.org/pdf/2608.02412v1)(arXiv v1、カード作成時に読んだ版)
- タグ: in-context-learning, large-language-models, tabular-classification
- 人手レビュー: 未

## 主張

出典のリンクは原論文PDFの該当ページを開く。リンクにカーソルを合わせると原文の引用が表示される。

- **c1** Under random linear projections, the LLM is the only one of nine methods whose accuracy decreases as dimensionality grows, while every classical baseline stays flat or improves.([Abstract, p.1](https://arxiv.org/pdf/2608.02412v1#page=1 "Dimensionality, in contrast, is decisive: sweeping random linear projections of thirty-one benchmark datasets, the LLM is the only method among nine whose accuracy decreases as dimensionality grows, while every classical baseline stays flat or improves."))
- **c2** The experiments use claude-opus-4-6, with an initial generalisation experiment using Qwen.([What do we mean by LLM, p.3](https://arxiv.org/pdf/2608.02412v1#page=3 "Concretely, our experiments use claude-opus-4-6 [2], a frontier model at the time of writing (Section C.3), alongside an initial generalizing experiment using Qwen to begin moving our claims from a single model to LLMs more broadly."))
- **c3** Splits are 5-fold stratified cross-validation repeated over 5 seeds.([Datasets and experimental setup, p.4](https://arxiv.org/pdf/2608.02412v1#page=4 "Splits are 5-fold stratified cross-validation repeated over 5 seeds, giving 25 splits per dataset and 475 queries in total."))
- **c4** The main classical baselines use fixed scikit-learn configurations; e.g. gradient boosting uses 100 estimators and otherwise sklearn defaults. No tuning of the main baselines was found in the text.([Appendix, p.25](https://arxiv.org/pdf/2608.02412v1#page=25 "GradientBoostingClassifier with n_estimators=100 and random_state=0; sklearn defaults otherwise"))
- **c5** The authors suggest that a memorisation probe should be standard practice in any LLM-for-tabular evaluation.([Data hygiene, p.5](https://arxiv.org/pdf/2608.02412v1#page=5 "More broadly, we suggest that a probe of this kind should be standard practice in any LLM-for-tabular evaluation."))
- **c6** The evaluation is restricted to toy-scale tabular datasets, a restriction partly forced by the cost and context limits of the LLM.([Limitations, p.14](https://arxiv.org/pdf/2608.02412v1#page=14 "A limitation of our evaluation is that it is restricted to toy-scale tabular datasets; however, this restriction is itself partly forced by the cost and context limits of the method being studied."))

