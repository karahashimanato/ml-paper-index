<!-- このファイルは scripts/generate.py が生成する。手で編集しない。 -->

# Learning and Predicting Patent Technology Reuse Trajectories from Emergence-Time Signals

- カード: [`arxiv-2610.00806`](../../papers/arxiv-2610.00806.yaml)
- 著者: Ayham Yousef, Qiang Ye, Qiang Cheng
- 年・掲載: 2026
- 原論文: [PDF](https://arxiv.org/pdf/2610.00806v1)(arXiv v1、カード作成時に読んだ版)
- タグ: deep-learning, gradient-boosted-trees, random-forests, supervised, tabular-attention, tabular-classification, tabular-mlp, unsupervised
- 人手レビュー: 未

## 主張

出典のリンクは原論文PDFの該当ページを開く。リンクにカーソルを合わせると原文の引用が表示される。

- **c1** Seven emergence-time features recover the GRU-based reuse labels well, but the calendar year of emergence alone is almost as predictive.([Abstract, p.1](https://arxiv.org/pdf/2610.00806v1#page=1 "Seven emergence-time features, observable in a technology’s first year, recover these labels at a one-vs-rest macro ROC-AUC of 0.914, but the calendar year of emergence alone reaches 0.874."))
- **c2** Seven classifiers are compared: GBDT, ExtraTrees, TabNet, FT-Transformer, TabM, TabKAN and TabMixer; GBDT is the primary baseline.([Supervised Classification, p.10](https://arxiv.org/pdf/2610.00806v1#page=10 "We evaluate two tree ensembles, Gradient Boosting Decision Trees (GBDT) and Extremely Randomized Trees (ExtraTrees), and five deep tabular models"))
- **c3** Classifiers use fixed settings listed per model (e.g. scikit-learn tree ensembles with the settings shown); no hyperparameter search procedure was found in the text.([Appendix (Classifier Hyperparameters), p.35](https://arxiv.org/pdf/2610.00806v1#page=35 "The tree ensembles use the scikit-learn implementations with the settings shown."))
- **c4** Label construction is fit on the full corpus; a stratified 60/40 train/test split (with a 90/10 train/validation split for early stopping) is applied afterwards to the classification stage only.([Methodology, p.12](https://arxiv.org/pdf/2610.00806v1#page=12 "The train/test split is applied afterwards, to the classification stage only: we use a stratified 60/40 train/test split, with a further 90/10 train/validation split within the training set for early stopping."))
- **c5** The sample-efficiency differences are mainly a GBDT effect rather than deep-versus-tree, and the sweep compares models that all already solve the (easy) emergence-profile task.([Discussion, p.27](https://arxiv.org/pdf/2610.00806v1#page=27 "What the sweep shows is that GBDT degrades faster than ExtraTrees, TabM, and FT-Transformer at very low data, and that the effect is confined to the smallest fractions."))
- **c6** Limitation: evaluation is single-domain (USPTO 2002-2022), untested on other patent offices.([Limitations, p.27](https://arxiv.org/pdf/2610.00806v1#page=27 "First, the evaluation is single-domain: it uses USPTO patents from 2002–2022, and we have not tested whether the findings transfer to other patent offices such as the EPO or JPO."))

