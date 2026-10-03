<!-- このファイルは scripts/generate.py が生成する。手で編集しない。 -->

# Unified Training of Universal Time Series Forecasting Transformers

- カード: [`arxiv-2402.02592`](../../papers/arxiv-2402.02592.yaml)
- 著者: Gerald Woo, Chenghao Liu, Akshat Kumar, Caiming Xiong, Silvio Savarese, Doyen Sahoo
- 年・掲載: 2024
- 原論文: [PDF](https://arxiv.org/pdf/2402.02592v2)(arXiv v2、カード作成時に読んだ版)
- タグ: deep-learning, self-supervised, time-series-forecasting, time-series-foundation-model
- 人手レビュー: 未

## 主張

出典のリンクは原論文PDFの該当ページを開く。リンクにカーソルを合わせると原文の引用が表示される。

- **c1** Method: Moirai modifies the time series Transformer to address cross-frequency learning, arbitrary numbers of variates and varying distributional properties.([Abstract, p.1](https://arxiv.org/pdf/2402.02592v2#page=1 "To address these challenges, we present novel enhancements to the conventional time series Transformer architecture, resulting in our proposed Masked EncOder-based UnIveRsAl TIme Series Forecasting Transformer (MOIRAI)."))
- **c2** Pretraining data: LOTSA, over 27B observations across nine domains; the authors report competitive or superior zero-shot performance versus full-shot models.([Abstract, p.1](https://arxiv.org/pdf/2402.02592v2#page=1 "Trained on our newly introduced Large-scale Open Time Series Archive (LOTSA) featuring over 27B observations across nine domains, MOIRAI achieves competitive or superior performance as a zero-shot forecaster when compared to full-shot models."))
- **c3** In-distribution evaluation: LOTSA includes the Monash archive as a data source; for a large portion of the Monash datasets only the train set is included, and the held-out test sets are used for in-distribution (not zero-shot) evaluation.([Experiments, p.6](https://arxiv.org/pdf/2402.02592v2#page=6 "For a large portion of these datasets, we only include the train set, holding out the test set which we now use for in-distribution evaluation."))
- **c4** Evaluation-practice remark: the authors say comparing zero-shot methods is made harder by not having a standard held-out test split, making it challenging to collate datasets that none of the models were trained on; in the same paragraph they state that the datasets used for their out-of-distribution evaluation were not included in LOTSA.([Out-of-distribution / Zero-shot Forecasting, p.6](https://arxiv.org/pdf/2402.02592v2#page=6 "Furthermore, the problem of comparing zero-shot methods is exacerbated by not having a standard held-out test split, making it challenging to collate a set of datasets which all the models have not been trained on."))
- **c5** Tuning protocol (probabilistic forecasting): full-shot baselines were hyperparameter-tuned per dataset on validation CRPS and averaged over five seeds; Moirai itself received inference-time tuning of context length and patch size on validation CRPS. Metrics: CRPS and MSIS with rolling evaluation.([Out-of-distribution / Zero-shot Forecasting, p.6](https://arxiv.org/pdf/2402.02592v2#page=6 "For each dataset and baseline, we perform hyperparameter tuning on a validation CRPS, and report results averaged over five training runs with different seeds."))
- **c6** Long sequence forecasting protocol: datasets with same-source data in pretraining were omitted (the appendix names the LSF Traffic dataset, omitted because LOTSA includes PeMS-sourced LargeST data); full-shot baseline results were copied from Liu et al. (2023b); Moirai was tuned on average validation MSE.([Out-of-distribution / Zero-shot Forecasting, p.7](https://arxiv.org/pdf/2402.02592v2#page=7 "We evaluate on a subset of the popular long sequence forecasting benchmark (Wu et al., 2021), omitting datasets which have datasets from the same source present in our pre-training data and cannot be considered zero-shot."))
- **c7** Limitations: little to no hyperparameter tuning due to resource constraints; the multi patch size mapping is somewhat heuristic; limited support for high-dimensional time series.([Limitations & Future Work, p.9](https://arxiv.org/pdf/2402.02592v2#page=9 "Due to resource constraints, little to no hyperparameter tuning was performed – efficient tuning techniques such as µP (Yang et al., 2022a) can be applied."))

