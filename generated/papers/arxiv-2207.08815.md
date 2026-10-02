<!-- このファイルは scripts/generate.py が生成する。手で編集しない。 -->

# Why do tree-based models still outperform deep learning on tabular data?

- カード: [`arxiv-2207.08815`](../../papers/arxiv-2207.08815.yaml)
- 著者: Léo Grinsztajn, Edouard Oyallon, Gaël Varoquaux
- 年・掲載: 2022
- タグ: gradient-boosted-trees, random-forests, supervised, tabular-attention, tabular-classification, tabular-mlp, tabular-regression
- 人手レビュー: 未

## 主張

- **c1** Tree-based models remained state-of-the-art on medium-sized data (~10K training samples), even without counting their faster training.(Abstract)
- **c2** Authors derive three challenges for tabular NNs: robustness to uninformative features, preserving data orientation, and learning irregular functions.(Abstract)
- **c3** Categorical variables are not the main weakness of NNs: most of the gap remains with numerical features only.(Section 4.2)
- **c4** Smoothing the training targets hurt tree-based models markedly but barely affected NNs, suggesting NNs are biased towards smooth solutions.(Section 5.2)
- **c5** MLP-like NNs (Resnet) were less robust to uninformative features: removing them narrowed the gap, adding them widened it.(Section 5.3)
- **c6** Under random rotation of the features, only Resnet was rotationally invariant (its accuracy was unaffected), unlike the other models.(Section 5.4)
- **c7** Hyperparameters were tuned by random search of about 400 iterations per dataset.(Section 3.3)
- **c8** Training sets of bigger datasets were truncated to 10,000 samples (medium-sized regime).(Section 3.2)
- **c9** Multiclass targets were binarised to the two most frequent classes and balanced.(Section 3.2)
- **c10** Datasets where a default linear model scores within 5% of both a default Resnet and a default HistGradientBoosting were removed as too easy.(Section 3.1)
- **c11** All missing data were removed, so missing-value handling is out of scope.(Section 3.2)
- **c12** With a 50,000-sample training set (few eligible datasets), the gap between NNs and tree-based models seemed to shrink in most cases.(Appendix A.2)
- **c13** Per unit of random-search time (rather than iterations), tree-based models were always well above NNs (hardware differs, so not a rigorous speed comparison).(Appendix A.2)
- **c14** The benchmark consists of 45 datasets from varied domains.(Abstract)
- **c15** Scores for a given search budget are averaged over 15 shuffles of the random-search order (bootstrap-like estimate).(Section 3.3)

## 論文内の勝敗(本文の記述)

| 勝ち | 負け | 根拠 | 比較条件 | 出典 |
|---|---|---|---|---|
| Tree-based models (RandomForest, GradientBoostingTrees, XGBoost) | Neural networks (MLP, Resnet, FT_Transformer, SAINT) | Normalized test score averaged over the benchmark's datasets, at every random-search budget (Figure 1). | `grinsztajn2022-medium-num-clf` | Section 4.2 |
| Tree-based models (RandomForest, GradientBoostingTrees, XGBoost) | Neural networks (MLP, Resnet, FT_Transformer, SAINT) | Normalized test score averaged over the benchmark's datasets, at every random-search budget (Figure 1). | `grinsztajn2022-medium-num-reg` | Section 4.2 |
| Tree-based models (RandomForest, GradientBoostingTrees, XGBoost) | Neural networks (MLP, Resnet, FT_Transformer, SAINT) | Normalized test score averaged over the benchmark's datasets, at every random-search budget (Figure 2). | `grinsztajn2022-medium-cat-clf` | Section 4.2 |
| Tree-based models (RandomForest, GradientBoostingTrees, XGBoost) | Neural networks (MLP, Resnet, FT_Transformer, SAINT) | Normalized test score averaged over the benchmark's datasets, at every random-search budget (Figure 2). | `grinsztajn2022-medium-cat-reg` | Section 4.2 |
| Neural networks (MLP, Resnet, FT_Transformer, SAINT) | Tree-based models (RandomForest, GradientBoostingTrees, XGBoost) | After randomly rotating the features of the numerical classification benchmark (Figure 6a); not the original benchmark condition. | – | Section 5.4 |
| Resnet | FT_Transformer | After randomly rotating the features of the numerical classification benchmark (Figure 6a); not the original benchmark condition. | – | Section 5.4 |

