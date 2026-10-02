<!-- このファイルは scripts/generate.py が生成する。手で編集しない。 -->

# TAB: Unified Benchmarking of Time Series Anomaly Detection Methods

- カード: [`arxiv-2506.18046`](../../papers/arxiv-2506.18046.yaml)
- 著者: Xiangfei Qiu, Zhe Li, Wanghui Qiu, Shiyan Hu, Lekui Zhou, Xingjian Wu, Zhengyu Li, Chenjuan Guo, Aoying Zhou, Zhenli Sheng, Jilin Hu, Christian S. Jensen, Bin Yang
- 年・掲載: 2025 PVLDB 18(9)
- 原論文: [PDF](https://arxiv.org/pdf/2506.18046v2)(arXiv v2、カード作成時に読んだ版)
- タグ: classical-outlier-detectors, forecasting-based-detectors, reconstruction-based-detectors, tabular-foundation-model, time-series-anomaly-detection, unsupervised
- 人手レビュー: 未

## 主張

出典のリンクは原論文PDFの該当ページを開く。リンクにカーソルを合わせると原文の引用が表示される。

- **c1** TAB covers 29 public multivariate datasets and 1,635 univariate time series from different domains.([Abstract, p.1](https://arxiv.org/pdf/2506.18046v2#page=1 "TAB encompasses 29 public multivariate datasets and 1,635 univariate time series from different domains"))
- **c2** It covers non-learning, machine learning, deep learning, LLM-based and time-series pre-trained methods.([Abstract, p.1](https://arxiv.org/pdf/2506.18046v2#page=1 "TAB covers a variety of TSAD methods, including Non-learning, Machine learning, Deep learning, LLM-based, and Time-series pre-trained methods."))
- **c3** Among 100 surveyed studies, more than half use at most four multivariate datasets.([Introduction, p.2](https://arxiv.org/pdf/2506.18046v2#page=2 "more than half of the studies include at most four datasets, and only one study covers 17 datasets."))
- **c4** Inconsistent splitting: some methods take the validation set from the test set.([Introduction, p.2](https://arxiv.org/pdf/2506.18046v2#page=2 "Some methods use a validation set from the testing set"))
- **c5** Drop-last issue: discarding the last incomplete test batch makes comparisons unfair unless batch sizes match.([Introduction, p.2](https://arxiv.org/pdf/2506.18046v2#page=2 "discarding the last incomplete batch with fewer sample instances than the batch size is unfair"))
- **c6** With point adjustment, even random methods likely hit at least one point in long anomaly windows.([Introduction, p.2](https://arxiv.org/pdf/2506.18046v2#page=2 "even random methods have a good chance to predict at least one point in larger anomaly windows"))
- **c7** Threshold-independent metrics like AUC-ROC should not be recomputed after point adjustment.([Introduction, p.2](https://arxiv.org/pdf/2506.18046v2#page=2 "should not be recalculated after point adjustment."))
- **c8** Label-based metrics change considerably with the threshold.([Introduction, p.2](https://arxiv.org/pdf/2506.18046v2#page=2 "when the threshold changes, the performance can change considerably."))
- **c9** TAB computes metrics at all thresholds and reports the best.([Experimental settings, p.8](https://arxiv.org/pdf/2506.18046v2#page=8 "we conduct metric calculations at all thresholds and report the best results."))
- **c10** Each method is run with its original hyperparameters plus a search over several sets; the best result is reported.([Experimental settings, p.8](https://arxiv.org/pdf/2506.18046v2#page=8 "We then select the best results from these evaluations"))
- **c11** On univariate series, machine learning and non-learning methods had the best average V-PR and Aff-F1.([Section 5.2.1, p.10](https://arxiv.org/pdf/2506.18046v2#page=10 "Machine learning (ML) and non-learning (NL) methods exhibit the best average performance in terms of the V-PR and Aff-F metrics."))
- **c12** Classic methods should not be overlooked while pursuing novel ones.([Section 5.2.1, p.10](https://arxiv.org/pdf/2506.18046v2#page=10 "while pursuing novel methods, we should not overlook the classic methods."))
- **c13** On multivariate data some deep models (TsNet, CATCH) appear best in full-shot settings.([Multivariate results, p.10](https://arxiv.org/pdf/2506.18046v2#page=10 "Some deep learning models, such as TsNet and CATCH, appear to achieve the best performance in full-shot settings."))
- **c14** Strong non-learning/ML results on multivariate data suggest significant room for improving deep learning approaches.([Multivariate results, p.11](https://arxiv.org/pdf/2506.18046v2#page=11 "This suggests that there is still significant room for improvement in current deep learning approaches."))
- **c15** For multivariate data, pre-trained time-series models do much better with full-shot or few-shot than zero-shot.([Multivariate results, p.10](https://arxiv.org/pdf/2506.18046v2#page=10 "time series pre-trained models demonstrate significantly better performance compared to zero-shot learning approaches."))
- **c16** No single TSAD method is universally best for all time series and anomaly types.([Introduction, p.2](https://arxiv.org/pdf/2506.18046v2#page=2 "no single TSAD method is universally best for all time series and anomaly types."))
- **c17** Overlapping vs non-overlapping window post-processing usually does not change performance (with a few exceptions).([Performance comparison of post-processing methods, p.10](https://arxiv.org/pdf/2506.18046v2#page=10 "in most cases, the two post-processing methods do not affect the performance of the method"))
- **c18** In critical difference diagrams on univariate data, OCSVM, HOBS and DWT ranked best.([Statistical validation, p.11](https://arxiv.org/pdf/2506.18046v2#page=11 "with OCSVM, HOBS, and DWT achieving the excellent results."))

## 結果表

列ごとに比較条件が異なる。**同じ列の中だけ**比較できる。太字は列内の最良値。

#### auc-roc(大きいほど良い)

繰り返し: Not stated in the main text.

| method | `tab2025-calit2` | `tab2025-daphnet` | `tab2025-msl` | `tab2025-psm` | `tab2025-skab` | `tab2025-smap` |
|---|---|---|---|---|---|---|
| ATrans (overlap windows) | 0.483 | 0.469 | 0.494 | 0.496 | 0.495 | 0.504 |
| DC (overlap windows) | 0.499 | 0.486 | 0.502 | 0.499 | 0.532 | 0.499 |
| DLin (overlap windows) | 0.761 | 0.727 | 0.626 | 0.581 | 0.563 | 0.398 |
| NLin (overlap windows) | 0.694 | 0.715 | 0.594 | 0.586 | 0.558 | 0.434 |
| Patch (overlap windows) | 0.791 | 0.739 | **0.637** | 0.578 | 0.555 | 0.449 |
| TsNet (overlap windows) | 0.798 | **0.773** | 0.615 | 0.589 | 0.592 | 0.455 |
| ATrans (non-overlap windows) | 0.491 | 0.489 | 0.508 | 0.498 | 0.513 | 0.504 |
| DC (non-overlap windows) | 0.527 | 0.501 | 0.504 | 0.499 | 0.522 | **0.516** |
| DLin (non-overlap windows) | 0.752 | 0.728 | 0.624 | 0.58 | 0.593 | 0.397 |
| NLin (non-overlap windows) | 0.695 | 0.715 | 0.592 | 0.585 | 0.583 | 0.434 |
| Patch (non-overlap windows) | **0.808** | 0.741 | **0.637** | 0.586 | 0.597 | 0.448 |
| TsNet (non-overlap windows) | 0.771 | 0.754 | 0.613 | **0.592** | **0.62** | 0.453 |

出典: [Table 7, p.10](https://arxiv.org/pdf/2506.18046v2#page=10 "Overlap 0.483 0.499 0.761 0.694 0.791 0.798")

## 論文内の勝敗(結果から導出)

同じ比較条件での数値の大小だけを数えたもの。**統計的有意性は考慮していない**。

| A | B | A勝ち | 引き分け | B勝ち |
|---|---|---|---|---|
| ATrans (non-overlap windows) | ATrans (overlap windows) | 5 | 1 | 0 |
| ATrans (non-overlap windows) | DC (non-overlap windows) | 1 | 0 | 5 |
| ATrans (non-overlap windows) | DC (overlap windows) | 3 | 0 | 3 |
| ATrans (non-overlap windows) | DLin (non-overlap windows) | 1 | 0 | 5 |
| ATrans (non-overlap windows) | DLin (overlap windows) | 1 | 0 | 5 |
| ATrans (non-overlap windows) | NLin (non-overlap windows) | 1 | 0 | 5 |
| ATrans (non-overlap windows) | NLin (overlap windows) | 1 | 0 | 5 |
| ATrans (non-overlap windows) | Patch (non-overlap windows) | 1 | 0 | 5 |
| ATrans (non-overlap windows) | Patch (overlap windows) | 1 | 0 | 5 |
| ATrans (non-overlap windows) | TsNet (non-overlap windows) | 1 | 0 | 5 |
| ATrans (non-overlap windows) | TsNet (overlap windows) | 1 | 0 | 5 |
| ATrans (overlap windows) | DC (non-overlap windows) | 0 | 0 | 6 |
| ATrans (overlap windows) | DC (overlap windows) | 1 | 0 | 5 |
| ATrans (overlap windows) | DLin (non-overlap windows) | 1 | 0 | 5 |
| ATrans (overlap windows) | DLin (overlap windows) | 1 | 0 | 5 |
| ATrans (overlap windows) | NLin (non-overlap windows) | 1 | 0 | 5 |
| ATrans (overlap windows) | NLin (overlap windows) | 1 | 0 | 5 |
| ATrans (overlap windows) | Patch (non-overlap windows) | 1 | 0 | 5 |
| ATrans (overlap windows) | Patch (overlap windows) | 1 | 0 | 5 |
| ATrans (overlap windows) | TsNet (non-overlap windows) | 1 | 0 | 5 |
| ATrans (overlap windows) | TsNet (overlap windows) | 1 | 0 | 5 |
| DC (non-overlap windows) | DC (overlap windows) | 4 | 1 | 1 |
| DC (non-overlap windows) | DLin (non-overlap windows) | 1 | 0 | 5 |
| DC (non-overlap windows) | DLin (overlap windows) | 1 | 0 | 5 |
| DC (non-overlap windows) | NLin (non-overlap windows) | 1 | 0 | 5 |
| DC (non-overlap windows) | NLin (overlap windows) | 1 | 0 | 5 |
| DC (non-overlap windows) | Patch (non-overlap windows) | 1 | 0 | 5 |
| DC (non-overlap windows) | Patch (overlap windows) | 1 | 0 | 5 |
| DC (non-overlap windows) | TsNet (non-overlap windows) | 1 | 0 | 5 |
| DC (non-overlap windows) | TsNet (overlap windows) | 1 | 0 | 5 |
| DC (overlap windows) | DLin (non-overlap windows) | 1 | 0 | 5 |
| DC (overlap windows) | DLin (overlap windows) | 1 | 0 | 5 |
| DC (overlap windows) | NLin (non-overlap windows) | 1 | 0 | 5 |
| DC (overlap windows) | NLin (overlap windows) | 1 | 0 | 5 |
| DC (overlap windows) | Patch (non-overlap windows) | 1 | 0 | 5 |
| DC (overlap windows) | Patch (overlap windows) | 1 | 0 | 5 |
| DC (overlap windows) | TsNet (non-overlap windows) | 1 | 0 | 5 |
| DC (overlap windows) | TsNet (overlap windows) | 1 | 0 | 5 |
| DLin (non-overlap windows) | DLin (overlap windows) | 2 | 0 | 4 |
| DLin (non-overlap windows) | NLin (non-overlap windows) | 4 | 0 | 2 |
| DLin (non-overlap windows) | NLin (overlap windows) | 4 | 0 | 2 |
| DLin (non-overlap windows) | Patch (non-overlap windows) | 0 | 0 | 6 |
| DLin (non-overlap windows) | Patch (overlap windows) | 2 | 0 | 4 |
| DLin (non-overlap windows) | TsNet (non-overlap windows) | 1 | 0 | 5 |
| DLin (non-overlap windows) | TsNet (overlap windows) | 2 | 0 | 4 |
| DLin (overlap windows) | NLin (non-overlap windows) | 3 | 0 | 3 |
| DLin (overlap windows) | NLin (overlap windows) | 4 | 0 | 2 |
| DLin (overlap windows) | Patch (non-overlap windows) | 0 | 0 | 6 |
| DLin (overlap windows) | Patch (overlap windows) | 2 | 0 | 4 |
| DLin (overlap windows) | TsNet (non-overlap windows) | 1 | 0 | 5 |
| DLin (overlap windows) | TsNet (overlap windows) | 1 | 0 | 5 |
| NLin (non-overlap windows) | NLin (overlap windows) | 2 | 2 | 2 |
| NLin (non-overlap windows) | Patch (non-overlap windows) | 0 | 0 | 6 |
| NLin (non-overlap windows) | Patch (overlap windows) | 2 | 0 | 4 |
| NLin (non-overlap windows) | TsNet (non-overlap windows) | 0 | 0 | 6 |
| NLin (non-overlap windows) | TsNet (overlap windows) | 0 | 0 | 6 |
| NLin (overlap windows) | Patch (non-overlap windows) | 0 | 1 | 5 |
| NLin (overlap windows) | Patch (overlap windows) | 2 | 0 | 4 |
| NLin (overlap windows) | TsNet (non-overlap windows) | 0 | 0 | 6 |
| NLin (overlap windows) | TsNet (overlap windows) | 0 | 0 | 6 |
| Patch (non-overlap windows) | Patch (overlap windows) | 4 | 1 | 1 |
| Patch (non-overlap windows) | TsNet (non-overlap windows) | 2 | 0 | 4 |
| Patch (non-overlap windows) | TsNet (overlap windows) | 3 | 0 | 3 |
| Patch (overlap windows) | TsNet (non-overlap windows) | 2 | 0 | 4 |
| Patch (overlap windows) | TsNet (overlap windows) | 1 | 0 | 5 |
| TsNet (non-overlap windows) | TsNet (overlap windows) | 2 | 0 | 4 |

## 論文内の勝敗(本文の記述)

| 勝ち | 負け | 根拠 | 比較条件 | 出典 |
|---|---|---|---|---|
| Machine learning and non-learning methods | Deep learning, LLM-based and time-series pre-trained methods | Average V-PR (VUS-PR) and Aff-F1 over 1,635 univariate series (Table 6, box plots). | `tab2025-univariate` | [Section 5.2.1, p.10](https://arxiv.org/pdf/2506.18046v2#page=10 "Machine learning (ML) and non-learning (NL) methods exhibit the best average performance in terms of the V-PR and Aff-F metrics.") |

