<!-- このファイルは scripts/generate.py が生成する。手で編集しない。 -->

# Chronos-2: From Univariate to Universal Forecasting

- カード: [`arxiv-2510.15821`](../../papers/arxiv-2510.15821.yaml)
- 著者: Abdul Fatir Ansari, Oleksandr Shchur, Jaris Küken, Andreas Auer, Boran Han, Pedro Mercado, Syama Sundar Rangapuram, Huibin Shen, Lorenzo Stella, Xiyuan Zhang, Mononito Goswami, Shubham Kapoor, Danielle C. Maddix, Pablo Guerron, Tony Hu, Junming Yin, Nick Erickson, Prateek Mutalik Desai, Hao Wang, Huzefa Rangwala, George Karypis, Yuyang Wang, Michael Bohlke-Schneider
- 年・掲載: 2025
- 原論文: [PDF](https://arxiv.org/pdf/2510.15821v1)(arXiv v1、カード作成時に読んだ版)
- タグ: deep-learning, in-context-learning, self-supervised, time-series-forecasting, time-series-foundation-model
- 人手レビュー: 未

## 主張

出典のリンクは原論文PDFの該当ページを開く。リンクにカーソルを合わせると原文の引用が表示される。

- **c1** Method: Chronos-2 uses a group attention mechanism that enables in-context learning by sharing information across the series in a group (related series, variates of a multivariate series, or targets and covariates).([Abstract, p.1](https://arxiv.org/pdf/2510.15821v1#page=1 "Chronos-2 employs a group attention mechanism that facilitates in-context learning (ICL) through efficient information sharing across multiple time series within a group"))
- **c2** Leakage on GIFT-Eval: the pretraining corpus was checked not to overlap with GIFT-Eval test portions, but it does partially overlap with the training portions of some GIFT-Eval datasets; for strictly zero-shot results the authors point to a synthetic-data-only variant.([Results (GIFT-Eval), p.10](https://arxiv.org/pdf/2510.15821v1#page=10 "Nonetheless, the corpus does include partial overlap with the training portions of some GIFT-Eval datasets."))
- **c3** Zero-shot status on fev-bench: according to the authors, none of the fev-bench datasets or tasks were seen by Chronos-2 during training.([Results (fev-bench), p.9](https://arxiv.org/pdf/2510.15821v1#page=9 "None of these datasets or tasks were seen by Chronos-2 during training."))
- **c4** Evaluation practice: on fev-bench, both the baseline results and the imputation strategy for handling data leakage in certain tasks were taken from Shchur et al. (2025).([Results (fev-bench, Table 3 caption), p.8](https://arxiv.org/pdf/2510.15821v1#page=8 "Baseline results and the imputation strategy for handling data leakage in certain tasks are both taken from Shchur et al. (2025)."))
- **c5** Baseline scope: only pretrained models and statistical baselines (AutoARIMA, AutoETS, AutoTheta and their ensemble) are compared; task-specific deep learning models are excluded, citing prior studies (GIFT-Eval, Chronos) that found pretrained models comparable or better on average.([Experiments, p.8](https://arxiv.org/pdf/2510.15821v1#page=8 "We compare Chronos-2 only with the aforementioned models and exclude task-specific deep learning models from our evaluation"))
- **c6** Mixed finding: on the multivariate subset of fev-bench, ICL gave only modest gains over univariate inference, which the authors read as suggesting the benefits of explicit multivariate modeling can be limited; the largest ICL gains were on tasks with covariates.([Improvements with In-context Learning, p.11](https://arxiv.org/pdf/2510.15821v1#page=11 "This suggests that while these tasks involve multiple variates with potentially shared dynamics, the benefits of explicit multivariate modeling can be limited."))
- **c7** Affiliation: the title page lists Amazon Web Services / Amazon (some authors also list universities; two contributed as AWS interns), and the footnote states that the report describes work performed at Amazon. The compared models include Chronos-Bolt, described in the paper as the latest publicly released version of Chronos.([Title page (footnote), p.1](https://arxiv.org/pdf/2510.15821v1#page=1 "Hao Wang and Pablo Guerron hold concurrent appointments at Amazon and their corresponding universities, and this report describes work performed at Amazon."))
- **c8** Zero-shot status on Chronos Benchmark II: according to the authors, none of its datasets were included in the training corpus of Chronos-2.([Results (Chronos Benchmark II), p.10](https://arxiv.org/pdf/2510.15821v1#page=10 "None of these datasets were included in the training corpus of Chronos-2."))

