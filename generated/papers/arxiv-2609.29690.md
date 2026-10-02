<!-- このファイルは scripts/generate.py が生成する。手で編集しない。 -->

# Predicting Symptoms of Amotivation and Anhedonia among University Students with a Novel Oversampling Method

- カード: [`arxiv-2609.29690`](../../papers/arxiv-2609.29690.yaml)
- 著者: Dang Nguyen, Bao Duong, Arun Kumar, Dat Phan-Trong, Julian Berk, Taylor Braund, Kien Do, Debopriyo Bal, Wu Yi Zheng, Leonard Hoon, Jill Newby, Helen Christensen, Svetha Venkatesh, Alexis Whitton, Sunil Gupta
- 年・掲載: 2026
- 原論文: [PDF](https://arxiv.org/pdf/2609.29690v1)(arXiv v1、カード作成時に読んだ版)
- タグ: gradient-boosted-trees, imbalance-resampling, random-forests, supervised, tabular-classification
- 人手レビュー: 未

## 主張

出典のリンクは原論文PDFの該当ページを開く。リンクにカーソルを合わせると原文の引用が表示される。

- **c1** SMOTE-PRED generates nominal variables with a predictive model rather than by interpolation.([Abstract, p.1](https://arxiv.org/pdf/2609.29690v1#page=1 "Our approach leverages a predictive model to generate nominal variables, rather than interpolating them."))
- **c2** On a GPS location dataset from university students, the method is reported to be significantly better than existing oversampling approaches for predicting elevated amotivation and anhedonia symptoms.([Abstract, p.1](https://arxiv.org/pdf/2609.29690v1#page=1 "We validate our method on a large-scale GPS location dataset collected from university students and demonstrate that it is significantly better than existing oversampling approaches in predicting elevated symptoms of amotivation and anhedonia."))
- **c3** The oversampling baselines use default hyperparameters from their libraries.([Experimental setup, p.8](https://arxiv.org/pdf/2609.29690v1#page=8 "For the baselines, we use default hyper-parameters as suggested in the library/package."))
- **c4** The downstream classifiers (kNN, SVM, DT, RF, XGBoost) are tuned on the training set with ten-fold cross-validation.([Experimental setup, p.8](https://arxiv.org/pdf/2609.29690v1#page=8 "We tune their hyper-parameters (see Table 4) on the training set by using ten-fold cross-validation."))
- **c5** Experiments are repeated ten times with random 90/10 train/test splits and the average AUC is reported.([Experimental setup, p.8](https://arxiv.org/pdf/2609.29690v1#page=8 "In each time, we construct training and test sets by randomly splitting the dataset into 90% for training and 10% for testing."))
- **c6** kNN was chosen as the default classifier for the following experiments because it was the most effective classifier in the reported comparison.([Results and discussions, p.9](https://arxiv.org/pdf/2609.29690v1#page=9 "As kNN is the most effective classifier (it works well with not only our method SMOTE-PRED but also AdaSyn, SMOTE, and SMOTE-NC), we select it as the default classifier for our following experiments."))

