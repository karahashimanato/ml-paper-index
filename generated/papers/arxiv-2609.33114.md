<!-- このファイルは scripts/generate.py が生成する。手で編集しない。 -->

# Can Tabular Foundation Models Amortize Statistical Inference?

- カード: [`arxiv-2609.33114`](../../papers/arxiv-2609.33114.yaml)
- 著者: Kai Ye, Shijin Gong, Hongyi Zhou, Valentina Zangirolami, Chengchun Shi
- 年・掲載: 2026
- 原論文: [PDF](https://arxiv.org/pdf/2609.33114v1)(arXiv v1、カード作成時に読んだ版)
- タグ: in-context-learning, tabular-foundation-model, tabular-regression
- 人手レビュー: 未

## 主張

出典のリンクは原論文PDFの該当ページを開く。リンクにカーソルを合わせると原文の引用が表示される。

- **c1** TabCon is an amortized inference system on a tabular foundation model producing confidence intervals for new datasets in one forward pass, using a sparse MoE and RL-based post-training.([Abstract, p.1](https://arxiv.org/pdf/2609.33114v1#page=1 "The key methodological ingredients of TabCon are a sparse mixture-of-experts architecture and reinforcement-learning-based post-training that calibrate the resulting confidence intervals to a desired coverage level."))
- **c2** Across benchmark datasets TabCon attains near-nominal coverage with short intervals and runs 50 times faster than a 50-sample bootstrap.([Abstract, p.1](https://arxiv.org/pdf/2609.33114v1#page=1 "Across a wide range of benchmark datasets, TabCon attains near-nominal coverage while producing short confidence intervals."))
- **c3** Evaluation uses 64 synthetic DGPs (32 seen in training, 32 unseen) in standard and stress-test settings, plus a semi-synthetic benchmark using real covariates from 13 OpenML-CC18 datasets with synthetic responses.([Experiments, p.8](https://arxiv.org/pdf/2609.33114v1#page=8 "Finally, we construct a semi-synthetic benchmark based on real feature matrices from 13 OpenML-CC18 datasets (Bischl et al., 2021)."))
- **c4** Baselines are Linear and RFF Wald-type intervals and three TabPFN-v3-based approaches (bootstrap with 50 samples, predictive-distribution PI, and approximate martingale posterior).([Experiments, p.8](https://arxiv.org/pdf/2609.33114v1#page=8 "We compare TabCon against five methods for CI construction, including two based on normal approximations and three built on TabPFN that represent different approaches to uncertainty quantification with existing tabular foundation models."))
- **c5** Prediction intervals from existing TFMs are 13%-148% wider than TabCon's CIs in the experiments.([Introduction, p.2](https://arxiv.org/pdf/2609.33114v1#page=2 "In our experiments, the latter are 13%–148% wider than the CIs produced by TabCon."))
- **c6** Open question: whether other inference tasks such as hypothesis testing can be amortized in a unified foundation model.([Discussion, p.11](https://arxiv.org/pdf/2609.33114v1#page=11 "It remains an open question whether these tasks can similarly be amortized within a unified foundation model."))

