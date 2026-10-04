<!-- このファイルは scripts/generate.py が生成する。手で編集しない。 -->

# Uncertainty in Gradient Boosting via Ensembles

- カード: [`arxiv-2006.10562`](../../papers/arxiv-2006.10562.yaml)
- 著者: Andrey Malinin, Liudmila Prokhorenkova, Aleksei Ustimenko
- 年・掲載: 2020 ICLR 2021
- 原論文: [PDF](https://arxiv.org/pdf/2006.10562v4)(arXiv v4、カード作成時に読んだ版)
- タグ: gradient-boosted-trees, supervised, tabular-classification, tabular-regression, uncertainty-estimation
- 人手レビュー: 未

## 主張

出典のリンクは原論文PDFの該当ページを開く。リンクにカーソルを合わせると原文の引用が表示される。

- **c1** Gap identified: NGBoost-style GBDT models that predict a mean and variance capture only data (aleatoric) uncertainty, not knowledge (epistemic) uncertainty about inputs far from or sparsely covered by the training data.([Introduction, p.2](https://arxiv.org/pdf/2006.10562v4#page=2 "However, such models only capture data uncertainty (Gal, 2016; Malinin, 2019), also known as aleatoric uncertainty, which arises due to inherent class overlap or noise in the data."))
- **c2** Ensemble generation: SGB ensembles (independent stochastic gradient boosting models with different seeds) have no guarantee of approximating the true posterior; SGLB (Stochastic Gradient Langevin Boosting, by two of the authors) is used because its models are asymptotically sampled from the true posterior.([Generating ensembles of GDBT models, p.4](https://arxiv.org/pdf/2006.10562v4#page=4 "Unfortunately, there are no guarantees on how well the distribution q(θ) estimates the true posterior p(θ/D)."))
- **c3** Virtual ensembles trade quality for cost: members are truncated sub-models of one GBDT and are strongly correlated; on synthetic data the authors conclude that vSGLB knowledge-uncertainty estimates are very cheap but inferior to ensembles of independent models.([Analysis on synthetic data, p.7](https://arxiv.org/pdf/2006.10562v4#page=7 "This shows that while vSGLB yields very cheap estimates of knowledge uncertainty by exploiting the ‘ensemble of trees’ structure of GBDT models, the quality of these estimates is inferior to ensembles of independent models."))
- **c4** Failure mode on continuous features: traces of class boundaries remain in knowledge-uncertainty maps, possibly because split values vary across ensemble members near class borders (decision-boundary 'jitter'); outside the training domain, trees extend the boundary behaviour outward.([Analysis on synthetic data, p.6](https://arxiv.org/pdf/2006.10562v4#page=6 "However, we still can see traces of the class boundaries in Figure 3(c)."))
- **c5** On real datasets, ensembles do not outperform single models for error detection (PRR); the authors believe this is because GBDT models are already ensembles and because knowledge uncertainty contributes little to total uncertainty.([Detection of errors and anomalous inputs, p.8](https://arxiv.org/pdf/2006.10562v4#page=8 "However, ensembles do not outperform single models."))
- **c6** Knowledge-uncertainty measures give better out-of-domain detection (AUC-ROC) than total uncertainty; the OOD data are synthetic, sampled from another dataset (Year MSD, or CT slices for KDD datasets and Year MSD) because real OOD examples were hard to obtain.([Detection of errors and anomalous inputs, p.8](https://arxiv.org/pdf/2006.10562v4#page=8 "However, obtaining ‘real’ OOD examples for the datasets considered in this work is challenging, so we instead create synthetic OOD data as follows."))
- **c7** Evaluation protocol: all GBDT models are built with CatBoost; ensembles have 10 models of 1000 trees; hyperparameters were tuned by grid search over learning rate {0.001, 0.01, 0.1} and depth {3, 4, 5, 6}, with subsample fixed to 0.5 for SGB and 1 for SGLB; UCI regression uses standard splits, classification a 65/15/20 split.([Appendix A.2, p.13](https://arxiv.org/pdf/2006.10562v4#page=13 "For all approaches, we use grid search to tune learning-rate in {0.001, 0.01, 0.1}, tree depth in {3, 4, 5, 6}."))
- **c8** Conflict of interest: the methods were implemented within the open-source CatBoost library, which is the library used for all GBDT models in the experiments (and the paper cites Prokhorenkova et al., 2018 for CatBoost).([Introduction, p.2](https://arxiv.org/pdf/2006.10562v4#page=2 "Our methods have been implemented within the open-source CatBoost library."))

