<!-- このファイルは scripts/generate.py が生成する。手で編集しない。 -->

# Why do tree-based models still outperform deep learning on tabular data?

- カード: [`arxiv-2207.08815`](../../papers/arxiv-2207.08815.yaml)
- 著者: Léo Grinsztajn, Edouard Oyallon, Gaël Varoquaux
- 年・掲載: 2022
- 原論文: [PDF](https://arxiv.org/pdf/2207.08815v1)(arXiv v1、カード作成時に読んだ版)
- タグ: gradient-boosted-trees, random-forests, supervised, tabular-attention, tabular-classification, tabular-mlp, tabular-regression
- 人手レビュー: 未

## 主張

出典のリンクは原論文PDFの該当ページを開く。リンクにカーソルを合わせると原文の引用が表示される。

- **c1** Tree-based models remained state-of-the-art on medium-sized data (~10K training samples), even without counting their faster training.([Abstract, p.1](https://arxiv.org/pdf/2207.08815v1#page=1 "Results show that tree-based models remain state-of-the-art on medium-sized data"))
- **c2** Authors derive three challenges for tabular NNs: robustness to uninformative features, preserving data orientation, and learning irregular functions.([Abstract, p.1](https://arxiv.org/pdf/2207.08815v1#page=1 "be robust to uninformative features, 2. preserve the orientation of the data, and 3. be able to easily learn irregular functions."))
- **c3** Categorical variables are not the main weakness of NNs: most of the gap remains with numerical features only.([Section 4.2, p.6](https://arxiv.org/pdf/2207.08815v1#page=6 "Still, most of this gap subsists when learning on numerical features only."))
- **c4** Smoothing the training targets hurt tree-based models markedly but barely affected NNs, suggesting NNs are biased towards smooth solutions.([Section 5.2, p.6](https://arxiv.org/pdf/2207.08815v1#page=6 "For small lengthscales, smoothing the target function on the train set decreases markedly the accuracy of tree-based models, but barely impacts that of NNs."))
- **c5** MLP-like NNs (Resnet) were less robust to uninformative features: removing them narrowed the gap, adding them widened it.([Section 5.3, p.7](https://arxiv.org/pdf/2207.08815v1#page=7 "This shows that MLPs are less robust to uninformative features"))
- **c6** Under random rotation of the features, only Resnet was rotationally invariant (its accuracy was unaffected), unlike the other models.([Section 5.4, p.7](https://arxiv.org/pdf/2207.08815v1#page=7 "only Resnets are rotationally invariant"))
- **c7** Hyperparameters were tuned by random search of about 400 iterations per dataset.([Section 3.3, p.4](https://arxiv.org/pdf/2207.08815v1#page=4 "We run a random search of ≈400 iterations per dataset"))
- **c8** Training sets of bigger datasets were truncated to 10,000 samples (medium-sized regime).([Section 3.2, p.3](https://arxiv.org/pdf/2207.08815v1#page=3 "We truncate the training set to 10,000 samples for bigger datasets."))
- **c9** Multiclass targets were binarised to the two most frequent classes and balanced.([Section 3.2, p.3](https://arxiv.org/pdf/2207.08815v1#page=3 "For classification, the target is binarised if there are several classes, by taking the two most numerous classes, and we keep half of samples in each class."))
- **c10** Datasets where a default linear model scores within 5% of both a default Resnet and a default HistGradientBoosting were removed as too easy.([Section 3.1, p.3](https://arxiv.org/pdf/2207.08815v1#page=3 "Specifically, we remove a dataset if a default Logistic Regression (or Linear Regression for regression) reach a score whose relative difference"))
- **c11** All missing data were removed, so missing-value handling is out of scope.([Section 3.2, p.3](https://arxiv.org/pdf/2207.08815v1#page=3 "We remove all missing data from the datasets."))
- **c12** With a 50,000-sample training set (few eligible datasets), the gap between NNs and tree-based models seemed to shrink in most cases.([Appendix A.2, p.16](https://arxiv.org/pdf/2207.08815v1#page=16 "it seems that, in most cases, increasing the train set size reduces the gap between neural networks and tree-based models."))
- **c13** Per unit of random-search time (rather than iterations), tree-based models were always well above NNs (hardware differs, so not a rigorous speed comparison).([Appendix A.2, p.14](https://arxiv.org/pdf/2207.08815v1#page=14 "for the same amount of time spent on random search, tree-based models scores are always high above neural networks."))
- **c14** The benchmark consists of 45 datasets from varied domains.([Abstract, p.1](https://arxiv.org/pdf/2207.08815v1#page=1 "We define a standard set of 45 datasets from varied domains"))
- **c15** Scores for a given search budget are averaged over 15 shuffles of the random-search order (bootstrap-like estimate).([Section 3.3, p.4](https://arxiv.org/pdf/2207.08815v1#page=4 "We do this 15 times while shuffling the random search order at each time."))
- **c16** Embedding layers (even for numerical features) break rotation invariance; that different embeddings all help suggests breaking invariance is key to their gains.([Section 5.4, p.8](https://arxiv.org/pdf/2207.08815v1#page=8 "The fact that very different types of embeddings seem to improve performance suggests that the sheer presence of an embedding which breaks the invariance is a key part of these improvements."))
- **c17** Adequate regularization and careful optimization may let NNs learn irregular patterns (the findings do not contradict regularization papers).([Section 5.2, p.7](https://arxiv.org/pdf/2207.08815v1#page=7 "as adequate regularization and careful optimization may allow NNs to learn irregular patterns."))

## 論文内の勝敗(本文の記述)

| 勝ち | 負け | 根拠 | 比較条件 | 出典 |
|---|---|---|---|---|
| Tree-based models (RandomForest, GradientBoostingTrees, XGBoost) | Neural networks (MLP, Resnet, FT_Transformer, SAINT) | Normalized test score averaged over the benchmark's datasets, at every random-search budget (Figure 1). | `grinsztajn2022-medium-num-clf` | [Section 4.2, p.6](https://arxiv.org/pdf/2207.08815v1#page=6 "Tree-based models are superior for every random search budget, and the performance gap stays wide even after a large number of random search iterations.") |
| Tree-based models (RandomForest, GradientBoostingTrees, XGBoost) | Neural networks (MLP, Resnet, FT_Transformer, SAINT) | Normalized test score averaged over the benchmark's datasets, at every random-search budget (Figure 1). | `grinsztajn2022-medium-num-reg` | [Section 4.2, p.6](https://arxiv.org/pdf/2207.08815v1#page=6 "Tree-based models are superior for every random search budget, and the performance gap stays wide even after a large number of random search iterations.") |
| Tree-based models (RandomForest, GradientBoostingTrees, XGBoost) | Neural networks (MLP, Resnet, FT_Transformer, SAINT) | Normalized test score averaged over the benchmark's datasets, at every random-search budget (Figure 2). | `grinsztajn2022-medium-cat-clf` | [Section 4.2, p.6](https://arxiv.org/pdf/2207.08815v1#page=6 "Tree-based models are superior for every random search budget, and the performance gap stays wide even after a large number of random search iterations.") |
| Tree-based models (RandomForest, GradientBoostingTrees, XGBoost) | Neural networks (MLP, Resnet, FT_Transformer, SAINT) | Normalized test score averaged over the benchmark's datasets, at every random-search budget (Figure 2). | `grinsztajn2022-medium-cat-reg` | [Section 4.2, p.6](https://arxiv.org/pdf/2207.08815v1#page=6 "Tree-based models are superior for every random search budget, and the performance gap stays wide even after a large number of random search iterations.") |
| Neural networks (MLP, Resnet, FT_Transformer, SAINT) | Tree-based models (RandomForest, GradientBoostingTrees, XGBoost) | After randomly rotating the features of the numerical classification benchmark (Figure 6a); not the original benchmark condition. | – | [Section 5.4, p.7](https://arxiv.org/pdf/2207.08815v1#page=7 "More striking, random rotations reverse the performance order: NNs are now above tree-based models and Resnets above FT Transformers.") |
| Resnet | FT_Transformer | After randomly rotating the features of the numerical classification benchmark (Figure 6a); not the original benchmark condition. | – | [Section 5.4, p.7](https://arxiv.org/pdf/2207.08815v1#page=7 "More striking, random rotations reverse the performance order: NNs are now above tree-based models and Resnets above FT Transformers.") |

