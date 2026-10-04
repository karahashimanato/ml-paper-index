<!-- このファイルは scripts/generate.py が生成する。手で編集しない。 -->

# Minimal Variance Sampling in Stochastic Gradient Boosting

- カード: [`arxiv-1910.13204`](../../papers/arxiv-1910.13204.yaml)
- 著者: Bulat Ibragimov, Gleb Gusev
- 年・掲載: 2019
- 原論文: [PDF](https://arxiv.org/pdf/1910.13204v1)(arXiv v1、カード作成時に読んだ版)
- タグ: gradient-boosted-trees, supervised, tabular-classification
- 人手レビュー: 未

## 主張

出典のリンクは原論文PDFの該当ページを開く。リンクにカーソルを合わせると原文の引用が表示される。

- **c1** Problem formulation: randomization in stochastic gradient boosting is cast as optimizing sampling probabilities to maximize the estimation accuracy of split scores used to train the trees.([Abstract, p.1](https://arxiv.org/pdf/1910.13204v1#page=1 "In this paper, we formulate the problem of randomization in SGB in terms of optimization of sampling probabilities to maximize the estimation accuracy of split scoring used to train decision trees."))
- **c2** Assumptions of the derivation: the squared deviation between sampled and full-data split scores is minimized assuming previous splits of the tree are fixed and the same for subsampled and full data; an upper bound is minimized and the unknown leaf values are replaced by a universal constant (the parameter lambda), giving a nearly optimal closed-form solution.([Problem setting, p.5](https://arxiv.org/pdf/1910.13204v1#page=5 "under the assumption that previous splits of the tree are ﬁxed and the same for subsampled and full data."))
- **c3** Setting lambda to 0 recovers Importance Sampling, which the authors say is of limited use in GBDT because the number of instances in each node must still be estimated accurately and it is numerically unstable for near-zero gradients; the lambda term acts as a regularizer against enormous weights. (The next paragraph states that lambda to infinity gives SGB.)([Theoretical analysis, p.6](https://arxiv.org/pdf/1910.13204v1#page=6 "It is easy to derive that setting λ to 0 implies the procedure of Importance Sampling."))
- **c4** Cost of sampling: a sort-and-binary-search threshold search is O(N log N), versus O(N) for SGB and GOSS; the authors propose a quickselect-like algorithm with O(N) complexity.([Algorithm, p.7](https://arxiv.org/pdf/1910.13204v1#page=7 "To compare with, SGB and GOSS algorithms have O(N) complexity for sampling."))
- **c5** CatBoost benchmark setup: MVS (80% sampling ratio) implemented in CatBoost and compared with default CatBoost without sampling on 153 public and proprietary binary classification datasets (up to 45 million instances), counting ROC-AUC wins.([Experiments, p.7](https://arxiv.org/pdf/1910.13204v1#page=7 "We implemented MVS in CatBoost and performed benchmark comparison of MVS with sampling ratio 80% and default CatBoost with no sampling on 153 publicly available and proprietary binary classiﬁcation datasets of different sizes up to 45 millions instances."))
- **c6** Result stated in the text for the CatBoost benchmark: 97 wins for MVS versus 55 for the default setting and +0.12% mean ROC-AUC.([Experiments, p.7](https://arxiv.org/pdf/1910.13204v1#page=7 "The results show signiﬁcant improvement over the existing default: 97 wins of MVS versus 55 wins of default setting and +0.12% mean ROC-AUC improvement."))
- **c7** LightGBM comparison protocol (MVS vs GOSS vs SGB, all implemented in LightGBM): baselines use the tuned parameters and train-test splits from the CatBoost benchmark repository [5] with sampling ratio 1; only the sampling parameters of each method are tuned by 5-fold cross-validation on the training subset; evaluation on the 20% test subset with 1 - ROC-AUC, averaged over 10 seeds; seven public datasets.([Experiments, p.8](https://arxiv.org/pdf/1910.13204v1#page=8 "We used the tuned parameters and train-test splitting for each dataset from [5] as baselines, presetting the sampling ratio to 1."))
- **c8** Tuning cost: GOSS and MVS each have one hyperparameter beyond the sample rate, so tuning them may potentially take more time than SGB; MVS Adaptive is introduced to remove the lambda hyperparameter.([Experiments, p.9](https://arxiv.org/pdf/1910.13204v1#page=9 "So tuning GOSS and MVS may potentially take more time than SGB."))

