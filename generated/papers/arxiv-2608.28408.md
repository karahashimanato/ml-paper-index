<!-- このファイルは scripts/generate.py が生成する。手で編集しない。 -->

# SymboLLM-FE: LLM-Accelerated Symbolic Regression for Automated Feature Engineering on Tabular Data

- カード: [`arxiv-2608.28408`](../../papers/arxiv-2608.28408.yaml)
- 著者: Zi-Jian Cheng, Zi-Yi Jia, Zhi Zhou, Yu-Feng Li, Lan-Zhe Guo
- 年・掲載: 2026
- 原論文: [PDF](https://arxiv.org/pdf/2608.28408v1)(arXiv v1、カード作成時に読んだ版)
- タグ: automl-systems, large-language-models, supervised, tabular-classification, tabular-regression
- 人手レビュー: 未

## 主張

出典のリンクは原論文PDFの該当ページを開く。リンクにカーソルを合わせると原文の引用が表示される。

- **c1** Formulas correlated with the target are extracted by symbolic regression and then refined by an LLM for interpretability.([Abstract, p.1](https://arxiv.org/pdf/2608.28408v1#page=1 "We extract math- ematically expressive formulas strongly corre- lated with the target via symbolic regression, which can enhance model performance, then refine them by LLMs with rich prior knowl- edge to ensure interpretability."))
- **c2** On six real-world datasets and four Kaggle competitions, SymboLLM-FE outperforms existing AutoFE methods.([Abstract, p.1](https://arxiv.org/pdf/2608.28408v1#page=1 "Empirical re- sults on six real-world datasets and four Kaggle competitions demonstrate that SymboLLM-FE outperforms existing AutoFE."))
- **c3** Evaluation protocol: a fold-wise protocol within cross-validation is used.([Method, p.4](https://arxiv.org/pdf/2608.28408v1#page=4 "SymboLLM-FE strictly adheres to a fold-wise training protocol within a cross- validation framework."))
- **c4** The validation set is used only for hyperparameter tuning, to prevent leakage into the test evaluation.([Method, p.5](https://arxiv.org/pdf/2608.28408v1#page=5 "To strictly prevent data leakage, the validation set is employed exclusively for hyperparameter tuning."))
- **c5** Downstream models (CatBoost, XGBoost, MLP, TabPFN) have hyperparameter grids reported in the appendix.([Experimental setup, p.6](https://arxiv.org/pdf/2608.28408v1#page=6 "Appendix C.2 shows these baselines’ information and full hyperparameter grids."))
- **c6** Limitation: the sliding-window subset construction over importance-sorted features may miss synergies among non-adjacent variables.([Limitations, p.9](https://arxiv.org/pdf/2608.28408v1#page=9 "Second, the subset construction strategy, which sorts features in descending order of importance and employs a continuous sliding window, may fail to capture synergistic effects among non-adjacent variables."))

