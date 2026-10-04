<!-- このファイルは scripts/generate.py が生成する。手で編集しない。 -->

# NGBoost: Natural Gradient Boosting for Probabilistic Prediction

- カード: [`arxiv-1910.03225`](../../papers/arxiv-1910.03225.yaml)
- 著者: Tony Duan, Anand Avati, Daisy Yi Ding, Khanh K. Thai, Sanjay Basu, Andrew Y. Ng, Alejandro Schuler
- 年・掲載: 2019 ICML 2020
- 原論文: [PDF](https://arxiv.org/pdf/1910.03225v4)(arXiv v4、カード作成時に読んだ版)
- タグ: gradient-boosted-trees, supervised, tabular-regression, uncertainty-estimation
- 人手レビュー: 未

## 主張

出典のリンクは原論文PDFの該当ページを開く。リンクにカーソルを合わせると原文の引用が表示される。

- **c1** Motivation: in regression, GBMs output only a scalar; under squared-error loss this can be read as the mean of a Gaussian with constant variance, which the authors say has little use; predicted distributions need at least two parameters to convey both magnitude and uncertainty.([Introduction, p.2](https://arxiv.org/pdf/1910.03225v4#page=2 "However, such probabilistic interpretations have little use if the variance is assumed constant."))
- **c2** Design choice: the parameters of the conditional distribution are boosted jointly (one base learner per parameter per stage), and natural gradients are used because ordinary gradients are not invariant to reparameterization and the parameterization can drastically change training dynamics.([The Generalized Natural Gradient, p.3](https://arxiv.org/pdf/1910.03225v4#page=3 "Thus the choice of parameterization can drastically impact the training dynamics, even though the minima are unchanged."))
- **c3** Failure mode of ordinary gradients (Figure 4, toy data): examples that happen to lie close to the initial mean dominate learning, because their variances are adjusted much more aggressively than the wrong means of the other examples, giving simultaneous overfitting and underfitting; the natural gradient balances the updates.([Figure 4, p.6](https://arxiv.org/pdf/1910.03225v4#page=6 "With ordinary gradients, we observe that “lucky” examples that are accidentally close to the initial predicted mean dominate the learning."))
- **c4** Cost: one series of learners per distribution parameter (cost linear in the number of parameters p) and a p x p matrix inversion per observation; the authors state NGBoost scales like other boosting algorithms in N but with larger constants depending on p.([Analysis and Discussion, p.6](https://arxiv.org/pdf/1910.03225v4#page=6 "The relative increase in computational cost is thus linear in the number of distributional parameters (p)."))
- **c5** Evaluation protocol (UCI regression, following Hernández-Lobato and Adams 2015): 10% random test split; 20% of the remaining 90% held out to choose the number of boosting stages M by log-likelihood, then retraining on the full 90%; repeated 20 times (Protein 5 times, Year MSD once). NGBoost used a Normal distribution, depth-3 trees, log score, learning rate 0.01 (0.1 for Year MSD).([Experiments, p.7](https://arxiv.org/pdf/1910.03225v4#page=7 "This entire process is repeated 20 times for all datasets except Protein and Year MSD, for which it is repeated 5 times and 1 time respectively."))
- **c6** Baseline caveat: MC dropout, Deep Ensembles and Concrete Dropout results are taken from their original papers rather than re-run; GAMLSS and Distributional Forest (200 trees, default hyperparameters) and a GP were run by the authors.([Probabilistic regression, p.7](https://arxiv.org/pdf/1910.03225v4#page=7 "We use the results from Gal and Ghahramani (2016) as our benchmark."))
- **c7** Ablation: plain multiparameter boosting with ordinary gradients most often did worse than assuming homoscedasticity, likely due to poor training dynamics, and second-order (Newton) boosting did even worse; natural gradients correct this.([Conclusions, p.9](https://arxiv.org/pdf/1910.03225v4#page=9 "However, us- ing multiparameter boosting to relax the homoscedasticity assumption most often results in worse performance, likely due to poor training dynamics."))
- **c8** Point-estimation comparison with scikit-learn baselines: gradient boosting was tuned over learning rate, depth and iterations, random forest used 500 trees with other parameters at default; the authors note that NGBoost was optimized for NLL rather than RMSE and was less aggressively tuned than the comparators.([Conclusions, p.9](https://arxiv.org/pdf/1910.03225v4#page=9 "This is despite the fact that the NGBoost mod- els were (a) optimized for NLL, not to minimize RMSE and (b) less aggressively tuned."))

