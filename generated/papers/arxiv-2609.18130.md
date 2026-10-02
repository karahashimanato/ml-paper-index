<!-- このファイルは scripts/generate.py が生成する。手で編集しない。 -->

# Benchmarking Tabular Foundation Models as Surrogates in Expensive Evolutionary Optimization

- カード: [`arxiv-2609.18130`](../../papers/arxiv-2609.18130.yaml)
- 著者: Lu Han, Jin Wang, Yuchen Li, Haoran Gu, Shulei Liu, Ziyang Shi, Wenao Lu, Handing Wang
- 年・掲載: 2026
- 原論文: [PDF](https://arxiv.org/pdf/2609.18130v1)(arXiv v1、カード作成時に読んだ版)
- タグ: gaussian-processes, in-context-learning, tabular-foundation-model, tabular-regression
- 人手レビュー: 未

## 主張

出典のリンクは原論文PDFの該当ページを開く。リンクにカーソルを合わせると原文の引用が表示される。

- **c1** The paper studies, experimentally and theoretically, how effective TabPFN is as a surrogate in surrogate-assisted evolutionary algorithms.([Abstract, p.1](https://arxiv.org/pdf/2609.18130v1#page=1 "this work conducts a comprehensive study that combines extensive experiments with in-depth theoretical analysis to investigate the effectiveness of TabPFN"))
- **c2** TabPFN's effectiveness is highly problem dependent and it cannot universally replace conventional surrogates.([Abstract, p.1](https://arxiv.org/pdf/2609.18130v1#page=1 "Results show that the effectiveness of TabPFN is highly problem dependent, and it cannot replace conventional surrogates universally."))
- **c3** Predictive accuracy is compared between TabPFN v2, GP and RBFN on the CEC 2017 suite with RMSE and Kendall's tau, 25 independent runs per function; hyperparameter settings of GP/RBFN were not found in the text.([Prediction performance, p.4](https://arxiv.org/pdf/2609.18130v1#page=4 "We evaluate the prediction performance of three models, namely TabPFN, GP, and RBFN, on the CEC 2017 benchmark suite using RMSE and τ as evaluation metrics."))
- **c4** Training size is 10 times the dimension and test size 1000 for all three models.([Prediction performance, p.4](https://arxiv.org/pdf/2609.18130v1#page=4 "Across all test functions of different dimensions, we use a training sample size of Ntr = 10D and a test sample size of Nte = 1000 for the three models."))
- **c5** Limitation: although TabPFN needs no conventional hyperparameter optimization, its 'training' (context encoding) time can exceed RBFN's, which accumulates when surrogates are rebuilt often.([Limitations and Unsuitable Scenarios, p.12](https://arxiv.org/pdf/2609.18130v1#page=12 "Although TabPFN does not involve conventional hyper-parameter optimization, its training process still requires encoding and caching the training context to construct the predictive mapping."))
- **c6** Limitation: TabPFN extrapolates conservatively when candidates move away from the training data distribution.([Limitations and Unsuitable Scenarios, p.12](https://arxiv.org/pdf/2609.18130v1#page=12 "TabPFN exhibits relatively conservative extrapolation behavior when candidate solutions move away from the distribution of the training data."))

