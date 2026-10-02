<!-- このファイルは scripts/generate.py が生成する。手で編集しない。 -->

# TabM: Advancing Tabular Deep Learning with Parameter-Efficient Ensembling

- カード: [`arxiv-2410.24210`](../../papers/arxiv-2410.24210.yaml)
- 著者: Yury Gorishniy, Akim Kotelnikov, Artem Babenko
- 年・掲載: 2025 ICLR 2025
- 原論文: [PDF](https://arxiv.org/pdf/2410.24210v3)(arXiv v3、カード作成時に読んだ版)
- タグ: gradient-boosted-trees, supervised, tabular-attention, tabular-classification, tabular-mlp, tabular-regression
- 人手レビュー: 未

## 主張

出典のリンクは原論文PDFの該当ページを開く。リンクにカーソルを合わせると原文の引用が表示される。

- **c1** TabM showed the best performance among tabular deep learning models.([Abstract, p.1](https://arxiv.org/pdf/2410.24210v3#page=1 "In particular, we find that TabM demonstrates the best performance among tabular DL models."))
- **c2** MLP-based models, including TabM, are stronger and more practical than attention- and retrieval-based architectures.([Abstract, p.1](https://arxiv.org/pdf/2410.24210v3#page=1 "Generally, we show that MLPs, including TabM, form a line of stronger and more practical models compared to attention- and retrieval-based architectures."))
- **c3** TabM's multiple predictions are weak individually but powerful collectively.([Abstract, p.1](https://arxiv.org/pdf/2410.24210v3#page=1 "We observe that the multiple predictions of TabM are weak individually, but powerful collectively."))
- **c4** A plain MLP with BatchEnsemble already outperforms attention-based models such as FT-Transformer.([Section 1, p.2](https://arxiv.org/pdf/2410.24210v3#page=2 "MLP coupled with BatchEnsemble (Wen et al., 2020) — a long-existing method — right away outperforms popular attention-based models, such as FT-Transformer"))
- **c5** TabM competes with GBDT and outperforms prior tabular DL models while being more efficient.([Section 1, p.2](https://arxiv.org/pdf/2410.24210v3#page=2 "TabM easily competes with GBDT and outperforms prior tabular DL models"))
- **c6** The benchmark has 46 public datasets from prior work (incl. Grinsztajn et al., TabR, TabReD).([Section 3.1, p.3](https://arxiv.org/pdf/2410.24210v3#page=3 "Our benchmark consists of 46 publicly available datasets used in prior work"))
- **c7** Datasets with domain-aware (e.g. time-based) splits exhibit distribution shift and are challenging for some methods.([Section 3.1, p.3](https://arxiv.org/pdf/2410.24210v3#page=3 "Such datasets were shown to be challenging for some methods because they naturally exhibit a certain degree of distribution shift between training and test parts"))
- **c8** Protocol: tune on validation, retrain the tuned model under multiple seeds, report the test metric averaged over seeds.([Section 3.1, p.3](https://arxiv.org/pdf/2410.24210v3#page=3 "a given model undergoes hyperparameter tuning on the validation set, then the tuned model is trained from scratch under multiple random seeds, and the test metric averaged over the random seeds becomes the final score of the model on the dataset."))
- **c9** The ensemble size k is fixed at 32 and not tuned.([Section 3.3, p.6](https://arxiv.org/pdf/2410.24210v3#page=6 "We heuristically set k = 32 and do not tune this value."))
- **c10** Weight sharing among the implicit MLPs acts as an effective regularizer on tabular tasks.([Section 3.3, p.5](https://arxiv.org/pdf/2410.24210v3#page=5 "Thus, constraining the ensemble with weight sharing turns out to be a highly effective regularization on tabular tasks."))
- **c11** The two key reasons for TabM's performance are simultaneous training of the implicit MLPs and weight sharing.([Section 1, p.2](https://arxiv.org/pdf/2410.24210v3#page=2 "the two key reasons for TabM's high performance are the collective training of the underlying implicit MLPs and the weight sharing."))
- **c12** Many DL methods are no better, or worse, than a plain MLP on a non-negligible number of datasets.([Section 4.2, p.7](https://arxiv.org/pdf/2410.24210v3#page=7 "many DL methods turn out to be no better or even worse than MLP on a non-negligible number of datasets"))
- **c13** Simple MLPs are the fastest DL models and TabM is the runner-up; attention- and retrieval-based models are much slower.([Section 4.3, p.8](https://arxiv.org/pdf/2410.24210v3#page=8 "Simple MLPs are the fastest DL models, with TabM being the runner-up."))
- **c14** On large datasets, attention- and retrieval-based models need extremely long training or are inapplicable without extra effort.([Section 4.3, p.8](https://arxiv.org/pdf/2410.24210v3#page=8 "As expected, attention- and retrieval-based models struggle, yielding extremely long training times, or being simply inapplicable without additional effort."))
- **c15** Even the best individual submodel of TabM is no better than a simple MLP.([Section 5.1, p.9](https://arxiv.org/pdf/2410.24210v3#page=9 "individually, even the best submodel of TabM is no better than a simple MLP."))
- **c16** TabM's strength comes from the collective prediction of weak but diverse submodels.([Section 5.1, p.9](https://arxiv.org/pdf/2410.24210v3#page=9 "TabM draws its power from the collective prediction of weak, but diverse submodels."))
- **c17** Too large k can be detrimental.([Section 5.3, p.10](https://arxiv.org/pdf/2410.24210v3#page=10 "too high values of k can be detrimental."))
- **c18** MLP with piecewise-linear embeddings (MLP†) is a decent practical option between a plain MLP and TabM.([Section 4.2, p.7](https://arxiv.org/pdf/2410.24210v3#page=7 "MLP† seems to be a decent practical option between the plain MLP and TabM"))
- **c19** Variants with AMP and torch.compile (marked ∗) showcase efficiency and should not be directly compared to other DL models.([Section 4.3, p.8](https://arxiv.org/pdf/2410.24210v3#page=8 "they should not be directly compared to other DL models."))
- **c20** Metrics: RMSE for regression; accuracy or ROC-AUC for classification depending on the dataset source.([Section 3.1, p.3](https://arxiv.org/pdf/2410.24210v3#page=3 "We use RMSE (the root mean square error) for regression tasks, and accuracy or ROC-AUC for classification tasks depending on the dataset source."))
- **c21** Tabular MLPs have potential, but overfitting and optimization issues must be handled to reveal it.([Related work, p.2](https://arxiv.org/pdf/2410.24210v3#page=2 "one has to deal with overfitting and optimization issues to reveal that potential."))

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

出典: [Table 2, p.8](https://arxiv.org/pdf/2410.24210v3#page=8 "Maps Routing 6.5M 986 0.1601 0.1592 0.1583 0.1582 0.1594 OOM")

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
| TabM | Other tabular DL models (MLP, FT-T, SAINT, T2G, Excel, TabR, ModernNCA and embedding variants) | Mean performance rank over the 46 datasets (Figure 3); GBDTs are also in the figure but the statement is about DL models. | `gorishniy2025-46-datasets` | [Section 4.2, p.7](https://arxiv.org/pdf/2410.24210v3#page=7 "The performance ranks render TabM as the top-tier DL model.") |
| TabM-packed (MLP + Packed-Ensemble) | MLPxk (deep ensemble of independently trained MLPs) | Figure 2, tuned models on 46 datasets. | `gorishniy2025-46-datasets` | [Section 3.3, p.5](https://arxiv.org/pdf/2410.24210v3#page=5 "TabMpacked delivers significantly better performance compared to MLP×k.") |
| TabM-naive (MLP + BatchEnsemble) | TabM-packed | Figure 2, tuned models on 46 datasets. | `gorishniy2025-46-datasets` | [Section 3.3, p.5](https://arxiv.org/pdf/2410.24210v3#page=5 "Interestingly, Figure 2 reports higher performance of TabMnaive compared to TabMpacked.") |
| MLPxk (deep ensemble) | FT-Transformer | Figure 2, tuned models on 46 datasets. | `gorishniy2025-46-datasets` | [Section 3.3, p.4](https://arxiv.org/pdf/2410.24210v3#page=4 "Notably, the results are already better and more stable than those of FT-Transformer") |

