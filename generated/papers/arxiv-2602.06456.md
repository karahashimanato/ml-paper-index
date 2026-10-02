<!-- このファイルは scripts/generate.py が生成する。手で編集しない。 -->

# The Window Dilemma: Why Concept Drift Detection is Ill-Posed

- カード: [`arxiv-2602.06456`](../../papers/arxiv-2602.06456.yaml)
- 著者: Brandon Gower-Winter, Misja Groen, Georg Krempl
- 年・掲載: 2026
- 原論文: [PDF](https://arxiv.org/pdf/2602.06456v1)(arXiv v1、カード作成時に読んだ版)
- タグ: concept-drift-detection, error-rate-drift-detectors, random-forests, streaming, window-based-drift-detectors
- 人手レビュー: 未

## 主張

出典のリンクは原論文PDFの該当ページを開く。リンクにカーソルを合わせると原文の引用が表示される。

- **c1** Traditional batch learning often performed better than drift-aware stream learners.([Abstract, p.1](https://arxiv.org/pdf/2602.06456v1#page=1 "is that traditional batch learning techniques often perform better than their drift-aware counterparts"))
- **c2** The Window Dilemma: perceived drift is a product of how instances are windowed, not necessarily of the data-generating process.([Abstract, p.1](https://arxiv.org/pdf/2602.06456v1#page=1 "perceived drift is a product of windowing and not necessarily the underlying data generating process."))
- **c3** Drift detection is ill-posed mainly because drift events can rarely be verified in practice.([Abstract, p.1](https://arxiv.org/pdf/2602.06456v1#page=1 "drift detection is ill-posed, primarily because verification of drift events are implausible in practice."))
- **c4** Better performance of a classifier with a drift detector does not prove that drift was detected (affirming the consequent).([Section 4, p.4](https://arxiv.org/pdf/2602.06456v1#page=4 "Performance improvement is neither necessary nor sufficient evidence of successful drift detection"))
- **c5** Detectors that alarm more frequently tend to perform better (up to a point), likely because they retrain more often on recent data.([Section 4, p.4](https://arxiv.org/pdf/2602.06456v1#page=4 "concept drift detectors that detect more frequently, tend to perform better (up to a point)."))
- **c6** The type of classifier often matters more than drift-awareness.([Introduction, p.1](https://arxiv.org/pdf/2602.06456v1#page=1 "indicates that the type of classifier is often more important than drift-awareness."))
- **c7** Among drift detectors, D3 with a Hoeffding Tree discriminator was best for both base models (consistent with Lukats et al.).([Section 5, p.7](https://arxiv.org/pdf/2602.06456v1#page=7 "Of the drift detectors, D3-HT performed the best for both the NB and HT base models."))
- **c8** The drift-unaware Aggregated Mondrian Forest was competitive with the drift-aware Adaptive Random Forest.([Section 5, p.7](https://arxiv.org/pdf/2602.06456v1#page=7 "the drift-unaware Aggregated Mondrian Forest (AMF) performed competitively with the drift-aware Adaptive Random Forest (ARF)."))
- **c9** Keeping past data and periodically retraining on growing training sets is often effective.([Section 5, p.7](https://arxiv.org/pdf/2602.06456v1#page=7 "our results suggest that keeping past data is often useful and periodically retraining a model on increasingly large training sets is often an effective strategy."))
- **c10** Under the same update regime as batch random forests, drift-aware stream learners are often inferior to simple batch learning with a suitable classifier.([Section 5, p.7](https://arxiv.org/pdf/2602.06456v1#page=7 "drift-aware stream learners are often inferior to simple batch learning procedures provided an appropriate classifier is chosen."))
- **c11** The authors do not claim drift detection is pointless, but that its current purpose is misplaced.([Conclusion, p.8](https://arxiv.org/pdf/2602.06456v1#page=8 "Our findings do not mean that drift detection is pointless, rather that its current purpose is misplaced."))
- **c12** No per-stream tuning: default parameters of each library/implementation are used.([Appendix A, p.8](https://arxiv.org/pdf/2602.06456v1#page=8 "We do not perform explicit parameter tuning for model on each data stream and instead use the default values"))
- **c13** Evaluation uses 11 binary and multiclass real-world streams (no purely synthetic data).([Section 5, p.5](https://arxiv.org/pdf/2602.06456v1#page=5 "we evaluate each model across 11 binary and multiclass data streams"))
- **c14** The Last Class baseline wins on Forest Covertype by exploiting autocorrelation.([Section 5 footnote, p.7](https://arxiv.org/pdf/2602.06456v1#page=7 "The Last Class classifier performed best on ForestCoverType because it abuses the known autocorrelation in the data stream."))
- **c15** Accuracy can be misleading for drifting streams (Cohen's kappa is reported in the appendix).([Section 5, p.5](https://arxiv.org/pdf/2602.06456v1#page=5 "We acknowledge that accuracy is a potentially misleading metric in Drift Research"))
- **c16** Reset intervals of the periodic-reset models use domain knowledge for some datasets (e.g. one month, one season).([Appendix, p.8](https://arxiv.org/pdf/2602.06456v1#page=8 "For resetting, some datasets possess domain knowledge that we could exploit."))

## 結果表

列ごとに比較条件が異なる。**同じ列の中だけ**比較できる。太字は列内の最良値。

#### mean-prequential-accuracy(大きいほど良い)

繰り返し: Mean prequential accuracy over the stream with fixed seeds (Section 5).

| method | `gowerwinter2026-el` | `gowerwinter2026-fc` | `gowerwinter2026-ia` | `gowerwinter2026-ii` | `gowerwinter2026-ks` | `gowerwinter2026-lx` | `gowerwinter2026-mr` | `gowerwinter2026-nw` | `gowerwinter2026-oz` | `gowerwinter2026-rt` | `gowerwinter2026-yg` |
|---|---|---|---|---|---|---|---|---|---|---|---|
| LC | 84.8 | **91.4** | 25 | 15.9 | 6.7 | 48 | 49.8 | 68.1 | 90.2 | 0 | 48.7 |
| MC | 57.4 | 56.6 | 17.7 | 11 | 6.8 | 52.3 | 54.1 | 69.8 | 92.3 | 10 | 52 |
| NB | 76.3 | 56.6 | 53.6 | 46.5 | 69.9 | 55.6 | 63.8 | 69.6 | 73.8 | 18.8 | 54.3 |
| DDM-NB | 82.4 | 79.3 | 61.2 | 52.5 | 70.5 | 55.6 | 64 | 71.1 | 89.9 | 25 | 54.3 |
| ADWIN-NB | 82.3 | 71.4 | 63.2 | 52.6 | 69.9 | 55.6 | 64.2 | 70.7 | 85.7 | 30.3 | 55.1 |
| R-NB | 86.3 | 81.5 | 54.2 | 39.2 | 72.8 | 56.3 | 65.9 | 73.2 | 91.9 | 34.9 | 54.6 |
| D3-LR-NB | 82.3 | 70 | 58.6 | 44.4 | 75.6 | 55.6 | 66.9 | 72.7 | 89.6 | 34.6 | 54.6 |
| D3-HT-NB | 86.6 | 76.2 | 63.7 | 52.4 | 75.6 | 61.2 | 65 | 73 | 88.8 | 37.9 | 55.9 |
| IBDD-NB | 86.7 | 82 | 59.8 | 46.4 | 72.5 | 56.6 | 66.1 | 71 | 88.1 | 23.6 | 56.8 |
| HT | 80.2 | 79.7 | 54.9 | 48.1 | 70 | 90.2 | 63.6 | 72.6 | 92.3 | 27.3 | 54.6 |
| DDM-HT | 86.1 | 85.3 | 60.5 | 52.5 | 70.6 | 90.2 | 63.7 | 71.4 | 92.1 | 41.5 | 54.6 |
| ADWIN-HT | 83.9 | 79 | 61.3 | 52.8 | 70 | 85 | 63.8 | 70.6 | 92.2 | 44.5 | 54.8 |
| R-HT | 86 | 87.3 | 40 | 33.3 | 69.7 | 64 | 63 | 72.6 | **92.8** | 53.9 | 52.5 |
| D3-LR-HT | 84.3 | 80.4 | 46.7 | 41 | 77.5 | 90.2 | 65.3 | 71.8 | 92.4 | 51 | 53.2 |
| D3-HT-HT | 86.4 | 85.7 | 59.4 | 51.8 | 74.9 | 87.5 | 64.5 | 72.2 | 92.4 | 55.8 | 55.4 |
| IBDD-HT | 86.1 | 87 | 50.7 | 44 | 71.8 | 85.5 | 65.2 | 70.5 | 92 | 36.1 | 55.8 |
| HAT | 84.6 | 79.7 | 57.7 | 49.4 | 70.5 | 91.9 | 63.7 | 73.8 | 92.3 | 29.3 | 55.1 |
| AMF | 85 | 90.5 | 67.2 | 57.5 | **88.7** | **95.4** | 73.7 | 76.4 | 92 | **82.8** | 75.5 |
| ARF | **88.3** | 89.4 | **71.4** | **58.7** | 87.4 | 94.8 | 76.5 | 78.1 | 92.3 | 72.8 | 68.8 |
| S-RF | 62.6 | 67.3 | 55.8 | 19.3 | 51.9 | 91 | 69.7 | 72.8 | 92.3 | 14.2 | 60 |
| R-RF | 81.9 | 78.1 | 69.8 | 58.4 | 81.7 | 93.9 | 73.9 | 72.1 | 91.6 | 80.3 | 62.9 |
| I-RF | 78.2 | 78.7 | 63.2 | 55 | 82.3 | 94.3 | **78.9** | **79.1** | 92.6 | 81.3 | **79** |
| AMF (batch update regime) | 76.9 | 75.6 | 63.3 | 55.7 | 78.8 | 91.6 | 73.1 | 76.5 | 92 | 74.7 | 75.2 |
| ARF (batch update regime) | 81.1 | 69.7 | 66.7 | 56.8 | 77 | 93.7 | 74.1 | 77.2 | 92.2 | 63.3 | 67.8 |

出典: [Table 1, p.6](https://arxiv.org/pdf/2602.06456v1#page=6 "LC 84,8 91,4 25,0 15,9 6,7 48,0 49,8 68,1 90,2 0,0 48,7 22") / [Table 2, p.6](https://arxiv.org/pdf/2602.06456v1#page=6 "AMF 76,9 75,6 63,3 55,7 78,8 91,6 73,1 76,5 92,0 74,7 75,2")

#### median-rank(小さいほど良い)

繰り返し: Mean prequential accuracy over the stream with fixed seeds (Section 5).

| method | `gowerwinter2026-11-streams` |
|---|---|
| LC | 22 |
| MC | 21 |
| NB | 17 |
| DDM-NB | 14 |
| ADWIN-NB | 16 |
| R-NB | 12 |
| D3-LR-NB | 15 |
| D3-HT-NB | 9 |
| IBDD-NB | 10 |
| HT | 13 |
| DDM-HT | 9 |
| ADWIN-HT | 12 |
| R-HT | 13 |
| D3-LR-HT | 10 |
| D3-HT-HT | 9 |
| IBDD-HT | 11 |
| HAT | 11 |
| AMF | 3 |
| ARF | **2** |
| S-RF | 14 |
| R-RF | 4 |
| I-RF | 3 |

出典: [Table 1, p.6](https://arxiv.org/pdf/2602.06456v1#page=6 "LC 84,8 91,4 25,0 15,9 6,7 48,0 49,8 68,1 90,2 0,0 48,7 22")

## 論文内の勝敗(結果から導出)

同じ比較条件での数値の大小だけを数えたもの。**統計的有意性は考慮していない**。

| A | B | A勝ち | 引き分け | B勝ち |
|---|---|---|---|---|
| ADWIN-HT | ADWIN-NB | 8 | 0 | 4 |
| ADWIN-HT | AMF | 1 | 0 | 11 |
| ADWIN-HT | AMF (batch update regime) | 3 | 0 | 8 |
| ADWIN-HT | ARF | 0 | 0 | 12 |
| ADWIN-HT | ARF (batch update regime) | 2 | 1 | 8 |
| ADWIN-HT | D3-HT-HT | 2 | 0 | 10 |
| ADWIN-HT | D3-HT-NB | 5 | 0 | 7 |
| ADWIN-HT | D3-LR-HT | 3 | 0 | 9 |
| ADWIN-HT | D3-LR-NB | 9 | 0 | 3 |
| ADWIN-HT | DDM-HT | 6 | 0 | 6 |
| ADWIN-HT | DDM-NB | 8 | 0 | 4 |
| ADWIN-HT | HAT | 4 | 0 | 8 |
| ADWIN-HT | HT | 7 | 1 | 4 |
| ADWIN-HT | I-RF | 2 | 0 | 10 |
| ADWIN-HT | IBDD-HT | 5 | 0 | 7 |
| ADWIN-HT | IBDD-NB | 5 | 0 | 7 |
| ADWIN-HT | LC | 10 | 0 | 2 |
| ADWIN-HT | MC | 11 | 0 | 1 |
| ADWIN-HT | NB | 11 | 1 | 0 |
| ADWIN-HT | R-HT | 7 | 0 | 5 |
| ADWIN-HT | R-NB | 6 | 1 | 5 |
| ADWIN-HT | R-RF | 3 | 0 | 9 |
| ADWIN-HT | S-RF | 7 | 0 | 5 |
| ADWIN-NB | AMF | 0 | 0 | 12 |
| ADWIN-NB | AMF (batch update regime) | 1 | 0 | 10 |
| ADWIN-NB | ARF | 0 | 0 | 12 |
| ADWIN-NB | ARF (batch update regime) | 2 | 0 | 9 |
| ADWIN-NB | D3-HT-HT | 2 | 0 | 10 |
| ADWIN-NB | D3-HT-NB | 1 | 0 | 11 |
| ADWIN-NB | D3-LR-HT | 3 | 0 | 9 |
| ADWIN-NB | D3-LR-NB | 4 | 2 | 6 |
| ADWIN-NB | DDM-HT | 4 | 0 | 8 |
| ADWIN-NB | DDM-NB | 5 | 1 | 6 |
| ADWIN-NB | HAT | 4 | 1 | 7 |
| ADWIN-NB | HT | 6 | 0 | 6 |
| ADWIN-NB | I-RF | 1 | 1 | 10 |
| ADWIN-NB | IBDD-HT | 3 | 0 | 9 |
| ADWIN-NB | IBDD-NB | 3 | 0 | 9 |
| ADWIN-NB | LC | 9 | 0 | 3 |
| ADWIN-NB | MC | 11 | 0 | 1 |
| ADWIN-NB | NB | 10 | 2 | 0 |
| ADWIN-NB | R-HT | 5 | 0 | 7 |
| ADWIN-NB | R-NB | 3 | 0 | 9 |
| ADWIN-NB | R-RF | 1 | 0 | 11 |
| ADWIN-NB | S-RF | 6 | 0 | 6 |
| AMF | AMF (batch update regime) | 9 | 1 | 1 |
| AMF | ARF | 5 | 0 | 7 |
| AMF | ARF (batch update regime) | 8 | 0 | 3 |
| AMF | D3-HT-HT | 10 | 0 | 2 |
| AMF | D3-HT-NB | 11 | 0 | 1 |
| AMF | D3-LR-HT | 11 | 0 | 1 |
| AMF | D3-LR-NB | 12 | 0 | 0 |
| AMF | DDM-HT | 10 | 0 | 2 |
| AMF | DDM-NB | 12 | 0 | 0 |
| AMF | HAT | 11 | 0 | 1 |
| AMF | HT | 11 | 0 | 1 |
| AMF | I-RF | 7 | 1 | 4 |
| AMF | IBDD-HT | 10 | 1 | 1 |
| AMF | IBDD-NB | 11 | 0 | 1 |
| AMF | LC | 11 | 0 | 1 |
| AMF | MC | 11 | 0 | 1 |
| AMF | NB | 12 | 0 | 0 |
| AMF | R-HT | 10 | 0 | 2 |
| AMF | R-NB | 11 | 0 | 1 |
| AMF | R-RF | 9 | 0 | 3 |
| AMF | S-RF | 11 | 0 | 1 |
| AMF (batch update regime) | ARF | 2 | 0 | 9 |
| AMF (batch update regime) | ARF (batch update regime) | 4 | 0 | 7 |
| AMF (batch update regime) | D3-HT-HT | 8 | 0 | 3 |
| AMF (batch update regime) | D3-HT-NB | 8 | 0 | 3 |
| AMF (batch update regime) | D3-LR-HT | 8 | 0 | 3 |
| AMF (batch update regime) | D3-LR-NB | 10 | 0 | 1 |
| AMF (batch update regime) | DDM-HT | 8 | 0 | 3 |
| AMF (batch update regime) | DDM-NB | 9 | 0 | 2 |
| AMF (batch update regime) | HAT | 7 | 0 | 4 |
| AMF (batch update regime) | HT | 8 | 0 | 3 |
| AMF (batch update regime) | I-RF | 2 | 0 | 9 |
| AMF (batch update regime) | IBDD-HT | 8 | 1 | 2 |
| AMF (batch update regime) | IBDD-NB | 9 | 0 | 2 |
| AMF (batch update regime) | LC | 9 | 0 | 2 |
| AMF (batch update regime) | MC | 10 | 0 | 1 |
| AMF (batch update regime) | NB | 11 | 0 | 0 |
| AMF (batch update regime) | R-HT | 8 | 0 | 3 |
| AMF (batch update regime) | R-NB | 9 | 0 | 2 |
| AMF (batch update regime) | R-RF | 3 | 0 | 8 |
| AMF (batch update regime) | S-RF | 10 | 0 | 1 |
| ARF | ARF (batch update regime) | 11 | 0 | 0 |
| ARF | D3-HT-HT | 11 | 0 | 1 |
| ARF | D3-HT-NB | 12 | 0 | 0 |
| ARF | D3-LR-HT | 11 | 0 | 1 |
| ARF | D3-LR-NB | 12 | 0 | 0 |
| ARF | DDM-HT | 12 | 0 | 0 |
| ARF | DDM-NB | 12 | 0 | 0 |
| ARF | HAT | 11 | 1 | 0 |
| ARF | HT | 11 | 1 | 0 |
| ARF | I-RF | 7 | 0 | 5 |
| ARF | IBDD-HT | 12 | 0 | 0 |
| ARF | IBDD-NB | 12 | 0 | 0 |
| ARF | LC | 11 | 0 | 1 |
| ARF | MC | 11 | 1 | 0 |
| ARF | NB | 12 | 0 | 0 |
| ARF | R-HT | 11 | 0 | 1 |
| ARF | R-NB | 12 | 0 | 0 |
| ARF | R-RF | 11 | 0 | 1 |
| ARF | S-RF | 11 | 1 | 0 |
| ARF (batch update regime) | D3-HT-HT | 8 | 0 | 3 |
| ARF (batch update regime) | D3-HT-NB | 9 | 0 | 2 |
| ARF (batch update regime) | D3-LR-HT | 7 | 0 | 4 |
| ARF (batch update regime) | D3-LR-NB | 9 | 0 | 2 |
| ARF (batch update regime) | DDM-HT | 9 | 0 | 2 |
| ARF (batch update regime) | DDM-NB | 9 | 0 | 2 |
| ARF (batch update regime) | HAT | 8 | 0 | 3 |
| ARF (batch update regime) | HT | 9 | 0 | 2 |
| ARF (batch update regime) | I-RF | 3 | 0 | 8 |
| ARF (batch update regime) | IBDD-HT | 9 | 0 | 2 |
| ARF (batch update regime) | IBDD-NB | 9 | 0 | 2 |
| ARF (batch update regime) | LC | 9 | 0 | 2 |
| ARF (batch update regime) | MC | 10 | 0 | 1 |
| ARF (batch update regime) | NB | 11 | 0 | 0 |
| ARF (batch update regime) | R-HT | 8 | 0 | 3 |
| ARF (batch update regime) | R-NB | 9 | 0 | 2 |
| ARF (batch update regime) | R-RF | 4 | 0 | 7 |
| ARF (batch update regime) | S-RF | 10 | 0 | 1 |
| D3-HT-HT | D3-HT-NB | 4 | 1 | 7 |
| D3-HT-HT | D3-LR-HT | 8 | 1 | 3 |
| D3-HT-HT | D3-LR-NB | 9 | 0 | 3 |
| D3-HT-HT | DDM-HT | 8 | 1 | 3 |
| D3-HT-HT | DDM-NB | 10 | 0 | 2 |
| D3-HT-HT | HAT | 10 | 0 | 2 |
| D3-HT-HT | HT | 10 | 0 | 2 |
| D3-HT-HT | I-RF | 2 | 0 | 10 |
| D3-HT-HT | IBDD-HT | 9 | 0 | 3 |
| D3-HT-HT | IBDD-NB | 8 | 0 | 4 |
| D3-HT-HT | LC | 11 | 0 | 1 |
| D3-HT-HT | MC | 12 | 0 | 0 |
| D3-HT-HT | NB | 12 | 0 | 0 |
| D3-HT-HT | R-HT | 9 | 0 | 3 |
| D3-HT-HT | R-NB | 10 | 0 | 2 |
| D3-HT-HT | R-RF | 4 | 0 | 8 |
| D3-HT-HT | S-RF | 8 | 0 | 4 |
| D3-HT-NB | D3-LR-HT | 6 | 0 | 6 |
| D3-HT-NB | D3-LR-NB | 9 | 1 | 2 |
| D3-HT-NB | DDM-HT | 6 | 1 | 5 |
| D3-HT-NB | DDM-NB | 9 | 0 | 3 |
| D3-HT-NB | HAT | 8 | 0 | 4 |
| D3-HT-NB | HT | 9 | 0 | 3 |
| D3-HT-NB | I-RF | 2 | 0 | 10 |
| D3-HT-NB | IBDD-HT | 8 | 0 | 4 |
| D3-HT-NB | IBDD-NB | 8 | 0 | 4 |
| D3-HT-NB | LC | 10 | 0 | 2 |
| D3-HT-NB | MC | 11 | 0 | 1 |
| D3-HT-NB | NB | 12 | 0 | 0 |
| D3-HT-NB | R-HT | 8 | 0 | 4 |
| D3-HT-NB | R-NB | 8 | 0 | 4 |
| D3-HT-NB | R-RF | 2 | 0 | 10 |
| D3-HT-NB | S-RF | 8 | 0 | 4 |
| D3-LR-HT | D3-LR-NB | 7 | 0 | 5 |
| D3-LR-HT | DDM-HT | 5 | 1 | 6 |
| D3-LR-HT | DDM-NB | 9 | 0 | 3 |
| D3-LR-HT | HAT | 6 | 0 | 6 |
| D3-LR-HT | HT | 7 | 1 | 4 |
| D3-LR-HT | I-RF | 2 | 0 | 10 |
| D3-LR-HT | IBDD-HT | 7 | 0 | 5 |
| D3-LR-HT | IBDD-NB | 5 | 1 | 6 |
| D3-LR-HT | LC | 10 | 0 | 2 |
| D3-LR-HT | MC | 12 | 0 | 0 |
| D3-LR-HT | NB | 9 | 0 | 3 |
| D3-LR-HT | R-HT | 7 | 0 | 5 |
| D3-LR-HT | R-NB | 6 | 0 | 6 |
| D3-LR-HT | R-RF | 3 | 0 | 9 |
| D3-LR-HT | S-RF | 7 | 0 | 5 |
| D3-LR-NB | DDM-HT | 3 | 1 | 8 |
| D3-LR-NB | DDM-NB | 5 | 1 | 6 |
| D3-LR-NB | HAT | 4 | 0 | 8 |
| D3-LR-NB | HT | 6 | 1 | 5 |
| D3-LR-NB | I-RF | 1 | 0 | 11 |
| D3-LR-NB | IBDD-HT | 5 | 0 | 7 |
| D3-LR-NB | IBDD-NB | 5 | 0 | 7 |
| D3-LR-NB | LC | 9 | 0 | 3 |
| D3-LR-NB | MC | 11 | 0 | 1 |
| D3-LR-NB | NB | 10 | 1 | 1 |
| D3-LR-NB | R-HT | 6 | 0 | 6 |
| D3-LR-NB | R-NB | 4 | 1 | 7 |
| D3-LR-NB | R-RF | 2 | 0 | 10 |
| D3-LR-NB | S-RF | 6 | 0 | 6 |
| DDM-HT | DDM-NB | 9 | 1 | 2 |
| DDM-HT | HAT | 7 | 1 | 4 |
| DDM-HT | HT | 8 | 2 | 2 |
| DDM-HT | I-RF | 2 | 0 | 10 |
| DDM-HT | IBDD-HT | 7 | 1 | 4 |
| DDM-HT | IBDD-NB | 8 | 0 | 4 |
| DDM-HT | LC | 11 | 0 | 1 |
| DDM-HT | MC | 11 | 0 | 1 |
| DDM-HT | NB | 11 | 0 | 1 |
| DDM-HT | R-HT | 8 | 0 | 4 |
| DDM-HT | R-NB | 7 | 1 | 4 |
| DDM-HT | R-RF | 3 | 0 | 9 |
| DDM-HT | S-RF | 7 | 0 | 5 |
| DDM-NB | HAT | 3 | 1 | 8 |
| DDM-NB | HT | 5 | 0 | 7 |
| DDM-NB | I-RF | 2 | 0 | 10 |
| DDM-NB | IBDD-HT | 3 | 0 | 9 |
| DDM-NB | IBDD-NB | 5 | 0 | 7 |
| DDM-NB | LC | 9 | 0 | 3 |
| DDM-NB | MC | 11 | 0 | 1 |
| DDM-NB | NB | 10 | 2 | 0 |
| DDM-NB | R-HT | 5 | 0 | 7 |
| DDM-NB | R-NB | 2 | 0 | 10 |
| DDM-NB | R-RF | 2 | 0 | 10 |
| DDM-NB | S-RF | 6 | 1 | 5 |
| HAT | HT | 10 | 2 | 0 |
| HAT | I-RF | 2 | 0 | 10 |
| HAT | IBDD-HT | 5 | 1 | 6 |
| HAT | IBDD-NB | 5 | 0 | 7 |
| HAT | LC | 10 | 0 | 2 |
| HAT | MC | 11 | 1 | 0 |
| HAT | NB | 11 | 0 | 1 |
| HAT | R-HT | 8 | 0 | 4 |
| HAT | R-NB | 7 | 0 | 5 |
| HAT | R-RF | 4 | 0 | 8 |
| HAT | S-RF | 9 | 1 | 2 |
| HT | I-RF | 2 | 0 | 10 |
| HT | IBDD-HT | 5 | 0 | 7 |
| HT | IBDD-NB | 5 | 0 | 7 |
| HT | LC | 10 | 0 | 2 |
| HT | MC | 11 | 1 | 0 |
| HT | NB | 11 | 0 | 1 |
| HT | R-HT | 6 | 2 | 4 |
| HT | R-NB | 4 | 1 | 7 |
| HT | R-RF | 3 | 0 | 9 |
| HT | S-RF | 6 | 1 | 5 |
| I-RF | IBDD-HT | 10 | 0 | 2 |
| I-RF | IBDD-NB | 10 | 0 | 2 |
| I-RF | LC | 10 | 0 | 2 |
| I-RF | MC | 12 | 0 | 0 |
| I-RF | NB | 12 | 0 | 0 |
| I-RF | R-HT | 9 | 0 | 3 |
| I-RF | R-NB | 10 | 0 | 2 |
| I-RF | R-RF | 9 | 0 | 3 |
| I-RF | S-RF | 12 | 0 | 0 |
| IBDD-HT | IBDD-NB | 4 | 0 | 8 |
| IBDD-HT | LC | 11 | 0 | 1 |
| IBDD-HT | MC | 11 | 0 | 1 |
| IBDD-HT | NB | 10 | 0 | 2 |
| IBDD-HT | R-HT | 8 | 0 | 4 |
| IBDD-HT | R-NB | 7 | 0 | 5 |
| IBDD-HT | R-RF | 3 | 0 | 9 |
| IBDD-HT | S-RF | 6 | 0 | 6 |
| IBDD-NB | LC | 10 | 0 | 2 |
| IBDD-NB | MC | 11 | 0 | 1 |
| IBDD-NB | NB | 11 | 0 | 1 |
| IBDD-NB | R-HT | 7 | 0 | 5 |
| IBDD-NB | R-NB | 8 | 0 | 4 |
| IBDD-NB | R-RF | 2 | 0 | 10 |
| IBDD-NB | S-RF | 7 | 0 | 5 |
| LC | MC | 4 | 0 | 8 |
| LC | NB | 3 | 0 | 9 |
| LC | R-HT | 1 | 0 | 11 |
| LC | R-NB | 1 | 0 | 11 |
| LC | R-RF | 2 | 0 | 10 |
| LC | S-RF | 2 | 0 | 10 |
| MC | NB | 2 | 1 | 9 |
| MC | R-HT | 0 | 0 | 12 |
| MC | R-NB | 1 | 0 | 11 |
| MC | R-RF | 1 | 0 | 11 |
| MC | S-RF | 0 | 1 | 11 |
| NB | R-HT | 5 | 0 | 7 |
| NB | R-NB | 1 | 0 | 11 |
| NB | R-RF | 0 | 0 | 12 |
| NB | S-RF | 4 | 0 | 8 |
| R-HT | R-NB | 4 | 0 | 8 |
| R-HT | R-RF | 4 | 0 | 8 |
| R-HT | S-RF | 7 | 0 | 5 |
| R-NB | R-RF | 4 | 0 | 8 |
| R-NB | S-RF | 7 | 0 | 5 |
| R-RF | S-RF | 10 | 0 | 2 |

## 論文内の勝敗(本文の記述)

| 勝ち | 負け | 根拠 | 比較条件 | 出典 |
|---|---|---|---|---|
| AMF, ARF, R-RF, I-RF (forest-based learners) | Naive Bayes and Hoeffding Tree variants with or without drift detectors | Median rank over the 11 streams (Table 1); 'Adaptive Forest (tree-ensemble) techniques outperformed the single learner NB and HT variants'. | `gowerwinter2026-11-streams` | [Section 5, p.7](https://arxiv.org/pdf/2602.06456v1#page=7 "Adaptive Forest (tree-ensemble) techniques outperformed the single learner NB and HT variants.") |

