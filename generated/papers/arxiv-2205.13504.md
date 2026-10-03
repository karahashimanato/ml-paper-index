<!-- このファイルは scripts/generate.py が生成する。手で編集しない。 -->

# Are Transformers Effective for Time Series Forecasting?

- カード: [`arxiv-2205.13504`](../../papers/arxiv-2205.13504.yaml)
- 著者: Ailing Zeng, Muxi Chen, Lei Zhang, Qiang Xu
- 年・掲載: 2022
- 原論文: [PDF](https://arxiv.org/pdf/2205.13504v3)(arXiv v3、カード作成時に読んだ版)
- タグ: deep-learning, linear-models, supervised, time-series-forecasting
- 人手レビュー: 未

## 主張

出典のリンクは原論文PDFの該当ページを開く。リンクにカーソルを合わせると原文の引用が表示される。

- **c1** Proposes LTSF-Linear, a set of one-layer linear models (Linear, DLinear with trend/remainder decomposition, NLinear with last-value subtraction) as a comparison baseline for long-term forecasting.([Abstract, p.1](https://arxiv.org/pdf/2205.13504v3#page=1 "To validate our claim, we introduce a set of embarrass-ingly simple one-layer linear models named LTSF-Linear for comparison."))
- **c2** Main claim: on nine real-life datasets, LTSF-Linear outperforms existing Transformer-based LTSF models in all cases, often by a large margin.([Abstract, p.1](https://arxiv.org/pdf/2205.13504v3#page=1 "Experimental results on nine real-life datasets show that LTSF-Linear surprisingly outperforms existing sophisticated Transformer-based LTSF models in all cases, and often by a large margin."))
- **c3** Hedged conclusion: the temporal modeling capabilities of Transformers for time series are exaggerated, at least for the existing LTSF benchmarks.([Introduction, p.2](https://arxiv.org/pdf/2205.13504v3#page=2 "With the above, we conclude that the temporal modeling capabilities of Transformers for time series are exaggerated, at least for the existing LTSF benchmarks."))
- **c4** Baseline protocol: Appendix B.2 states that Transformer baselines (Autoformer, Informer, vanilla Transformer from the Autoformer code; FEDformer and Pyraformer from their repositories) were trained with their default hyperparameters; in the main Table 2, however, only methods marked * (Linear, NLinear, DLinear, Pyraformer, Repeat) were run by the authors and the other results (FEDformer, Autoformer, Informer, LogTrans) are copied from the FEDformer paper.([Appendix: Implementation Details, p.9](https://arxiv.org/pdf/2205.13504v3#page=9 "We also adopt their default hyper-parameters to train the models."))
- **c5** Look-back asymmetry: by default the paper reports look-back L=336 for LTSF-Linear and L=96 for Transformers, motivated by linear models underfitting on short inputs and Transformers overfitting on long ones.([Appendix: Implementation Details, p.9](https://arxiv.org/pdf/2205.13504v3#page=9 "To compare the best performance of existing LTSF-Transformers with LTSF-Linear, we re-port L=336 for LTSF-Linear and L=96 for Transformers by default."))
- **c6** Look-back study: similar to previous studies' observations, existing Transformer-based models' performance deteriorates or stays stable as the look-back window grows, whereas LTSF-Linear improves.([Experiments: More Analyses on LTSF-Transformers, p.5](https://arxiv.org/pdf/2205.13504v3#page=5 "Similar to the observations from previous studies [27, 30], existing Transformer-based models’ performance deteriorates or stays stable when the look-back window size increases."))
- **c7** Stated limitation: LTSF-Linear has limited model capacity and is meant only as a simple, competitive baseline; e.g. a one-layer linear network struggles with dynamics caused by change points.([Conclusion: Future work, p.8](https://arxiv.org/pdf/2205.13504v3#page=8 "LTSF-Linear has a limited model ca-pacity, and it merely serves a simple yet competitive base-line with strong interpretability for future research."))

