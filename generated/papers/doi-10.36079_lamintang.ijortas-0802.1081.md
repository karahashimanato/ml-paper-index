<!-- このファイルは scripts/generate.py が生成する。手で編集しない。 -->

# Interpretable Machine Learning Framework for Personalized Health Insurance Risk Prediction

- カード: [`doi-10.36079_lamintang.ijortas-0802.1081`](../../papers/doi-10.36079_lamintang.ijortas-0802.1081.yaml)
- 著者: Mohammed M. Al-Mhadawi, Qahtan Yas
- 年・掲載: 2026 International Journal of Recent Technology and Applied Science (IJORTAS)
- 原論文: [PDF](https://lamintang.org/journal/index.php/ijortas/article/download/1081/674)(Publisher PDF via OpenAlex (publishedVersion)、カード作成時に読んだ版)
- タグ: feature-attribution, gradient-boosted-trees, linear-models, random-forests, supervised, tabular-mlp, tabular-regression
- 人手レビュー: 未

## 主張

出典のリンクは原論文PDFの該当ページを開く。リンクにカーソルを合わせると原文の引用が表示される。

- **c1** Six predictive models (five tree ensembles and an MLP control) are benchmarked on one real-world insurance dataset of 1,338 records.([Abstract, p.1](https://lamintang.org/journal/index.php/ijortas/article/download/1081/674#page=1 "We benchmarked six predictive architectures (five tree ensembles and a multi-layer perceptron control) on a real-world dataset (n=1,338)."))
- **c2** Gradient Boosting performed best in their experiments.([Abstract, p.1](https://lamintang.org/journal/index.php/ijortas/article/download/1081/674#page=1 "Experimental results demonstrate that Gradient Boosting achieved superior performance"))
- **c3** Evaluation uses five folds with an 80/20 train-test partition per fold, with preprocessing fit on each training partition.([Methodology, p.5](https://lamintang.org/journal/index.php/ijortas/article/download/1081/674#page=5 "The dataset is partitioned using an 80/20 train-test strategy across five folds, resulting in 1,070 training samples and 268 testing samples per fold."))
- **c4** All models use the fixed 'optimized' configurations listed in a hyperparameter table with a fixed random seed; how these configurations were selected was not found in the text.([Finding and Discussion, p.9](https://lamintang.org/journal/index.php/ijortas/article/download/1081/674#page=9 "All experiments were conducted using the optimized hyperparameter configurations presented in Table 3, with random_state = 42 applied consistently across all models to ensure experimental reproducibility."))
- **c5** The MLP was a plain baseline control without tabular-specific adaptations such as TabNet, which the authors take as further support for tree ensembles.([Finding and Discussion, p.9](https://lamintang.org/journal/index.php/ijortas/article/download/1081/674#page=9 "Since such adaptations were not incorporated into this baseline control, the results further emphasize the suitability of tree-based ensemble approaches for modeling nonlinear insurance risk patterns."))
- **c6** The single static U.S.-centric dataset limits generalizability across regulatory, demographic and economic contexts.([Conclusion, p.11](https://lamintang.org/journal/index.php/ijortas/article/download/1081/674#page=11 "dataset, which restricts the generalizability of the findings across different regulatory, demographic, and economic contexts."))

