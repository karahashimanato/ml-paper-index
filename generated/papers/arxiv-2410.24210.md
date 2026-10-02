<!-- このファイルは scripts/generate.py が生成する。手で編集しない。 -->

# TabM: Advancing Tabular Deep Learning with Parameter-Efficient Ensembling

- カード: [`arxiv-2410.24210`](../../papers/arxiv-2410.24210.yaml)
- 著者: Yury Gorishniy, Akim Kotelnikov, Artem Babenko
- 年・掲載: 2025 ICLR 2025
- タグ: gradient-boosted-trees, supervised, tabular-attention, tabular-classification, tabular-mlp, tabular-regression
- 人手レビュー: 未

## 主張

- **c1** TabM showed the best performance among tabular deep learning models.(Abstract)
- **c2** MLP-based models, including TabM, are stronger and more practical than attention- and retrieval-based architectures.(Abstract)
- **c3** TabM's multiple predictions are weak individually but powerful collectively.(Abstract)
- **c4** A plain MLP with BatchEnsemble already outperforms attention-based models such as FT-Transformer.(Section 1)
- **c5** TabM competes with GBDT and outperforms prior tabular DL models while being more efficient.(Section 1)
- **c6** The benchmark has 46 public datasets from prior work (incl. Grinsztajn et al., TabR, TabReD).(Section 3.1)
- **c7** Datasets with domain-aware (e.g. time-based) splits exhibit distribution shift and are challenging for some methods.(Section 3.1)
- **c8** Protocol: tune on validation, retrain the tuned model under multiple seeds, report the test metric averaged over seeds.(Section 3.1)
- **c9** The ensemble size k is fixed at 32 and not tuned.(Section 3.3)
- **c10** Weight sharing among the implicit MLPs acts as an effective regularizer on tabular tasks.(Section 3.3)
- **c11** The two key reasons for TabM's performance are simultaneous training of the implicit MLPs and weight sharing.(Section 1)
- **c12** Many DL methods are no better, or worse, than a plain MLP on a non-negligible number of datasets.(Section 4.2)
- **c13** Simple MLPs are the fastest DL models and TabM is the runner-up; attention- and retrieval-based models are much slower.(Section 4.3)
- **c14** On large datasets, attention- and retrieval-based models need extremely long training or are inapplicable without extra effort.(Section 4.3)
- **c15** Even the best individual submodel of TabM is no better than a simple MLP.(Section 5.1)
- **c16** TabM's strength comes from the collective prediction of weak but diverse submodels.(Section 5.1)
- **c17** Too large k can be detrimental.(Section 5.3)
- **c18** MLP with piecewise-linear embeddings (MLP†) is a decent practical option between a plain MLP and TabM.(Section 4.2)
- **c19** Variants with AMP and torch.compile (marked ∗) showcase efficiency and should not be directly compared to other DL models.(Section 4.3)
- **c20** Metrics: RMSE for regression; accuracy or ROC-AUC for classification depending on the dataset source.(Section 3.1)

## 結果表

列ごとに比較条件が異なる。**同じ列の中だけ**比較できる。太字は列内の最良値。

#### rmse(小さいほど良い)

繰り返し: Tuned model retrained under multiple random seeds; test metric averaged over seeds (Section 3.1).

| method | `gorishniy2025-maps-routing` | `gorishniy2025-weather` |
|---|---|---|
| XGBoost | 0.1601 | 1.4234 |
| MLP | 0.1592 | 1.4842 |
| TabM-mini† (shared batches, AMP + torch.compile) | 0.1583 | **1.409** |
| TabM-mini† | **0.1582** | 1.4112 |
| FT-Transformer | 0.1594 | 1.4409 |

## 論文内の勝敗(結果から導出)

同じ比較条件での数値の大小だけを数えたもの。**統計的有意性は考慮していない**。

| A | B | A勝ち | 引き分け | B勝ち |
|---|---|---|---|---|
| FT-Transformer | MLP | 1 | 0 | 1 |
| FT-Transformer | TabM-mini† | 0 | 0 | 2 |
| FT-Transformer | TabM-mini† (shared batches, AMP + torch.compile) | 0 | 0 | 2 |
| FT-Transformer | XGBoost | 1 | 0 | 1 |
| MLP | TabM-mini† | 0 | 0 | 2 |
| MLP | TabM-mini† (shared batches, AMP + torch.compile) | 0 | 0 | 2 |
| MLP | XGBoost | 1 | 0 | 1 |
| TabM-mini† | TabM-mini† (shared batches, AMP + torch.compile) | 1 | 0 | 1 |
| TabM-mini† | XGBoost | 2 | 0 | 0 |
| TabM-mini† (shared batches, AMP + torch.compile) | XGBoost | 2 | 0 | 0 |

## 論文内の勝敗(本文の記述)

| 勝ち | 負け | 根拠 | 比較条件 | 出典 |
|---|---|---|---|---|
| TabM | Other tabular DL models (MLP, FT-T, SAINT, T2G, Excel, TabR, ModernNCA and embedding variants) | Mean performance rank over the 46 datasets (Figure 3); GBDTs are also in the figure but the statement is about DL models. | `gorishniy2025-46-datasets` | Section 4.2 |
| TabM-packed (MLP + Packed-Ensemble) | MLPxk (deep ensemble of independently trained MLPs) | Figure 2, tuned models on 46 datasets. | `gorishniy2025-46-datasets` | Section 3.3 |
| TabM-naive (MLP + BatchEnsemble) | TabM-packed | Figure 2, tuned models on 46 datasets. | `gorishniy2025-46-datasets` | Section 3.3 |
| MLPxk (deep ensemble) | FT-Transformer | Figure 2, tuned models on 46 datasets. | `gorishniy2025-46-datasets` | Section 3.3 |

