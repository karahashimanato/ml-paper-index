<!-- このファイルは scripts/generate.py が生成する。手で編集しない。 -->

# Optimal detection of general moment changes: Simultaneous mean and covariance change detection and beyond

- カード: [`arxiv-2609.36594`](../../papers/arxiv-2609.36594.yaml)
- 著者: Xiaokai Luo, Chenghao Xu, Haotian Xu, Carlos Misael Madrid Padilla, Daren Wang
- 年・掲載: 2026
- 原論文: [PDF](https://arxiv.org/pdf/2609.36594v1)(arXiv v1、カード作成時に読んだ版)
- タグ: change-point-detection, two-sample-tests, unsupervised
- 人手レビュー: 未

## 主張

出典のリンクは原論文PDFの該当ページを開く。リンクにカーソルを合わせると原文の引用が表示される。

- **c1** A tensor representation unifies moments of different orders, giving a method that detects changes in all moments up to a fixed order p.([Abstract, p.1](https://arxiv.org/pdf/2609.36594v1#page=1 "Our tensor representation unifies moments of different orders within a common linear algebraic framework, enabling a new method to detect changes in moments of all orders up to a prescribed fixed order p."))
- **c2** Theory: under regularity conditions the localization error rate matches a new minimax lower bound (temporal dependence and growing dimension allowed).([Abstract, p.1](https://arxiv.org/pdf/2609.36594v1#page=1 "Under suitable regularity conditions, the proposed procedure achieves a localization error rate that matches a newly developed minimax lower bound."))
- **c3** Competing methods (CPWZ, changeAUC, mean-change binary segmentation, MNSBS) use their default or paper-recommended tuning parameters and their own data-driven selection procedures.([Simulation and real data example (tuning parameter selection), p.12](https://arxiv.org/pdf/2609.36594v1#page=12 "For the competing methods, we use their default or paper-recommended tuning parameters and their associated data-driven selection procedures."))
- **c4** The proposed method's threshold tau and moment order p are chosen jointly from a grid by sample splitting: fit on odd-indexed observations and score the segmentation on even-indexed observations with an empirical kernel score (no ground-truth change points used).([Simulation and real data example (tuning parameter selection), p.12](https://arxiv.org/pdf/2609.36594v1#page=12 "To select the candidate pair in a data-driven manner, we evaluate these segments on the even-indexed observations using an empirical kernel score (Steinwart and Ziegel, 2021)."))
- **c5** Simulations: D = 100 dimensional AR(1) series, 100 repetitions per setting, with change points injected at fixed known locations; accuracy is the Hausdorff distance between true and estimated change sets plus the frequency of under/over-estimating the number of changes.([Simulation studies, p.13](https://arxiv.org/pdf/2609.36594v1#page=13 "We use D = 100 and 100 independent repetitions per setting."))
- **c6** Main empirical claim: in the simulations the method recovers the correct number of changes in every repetition and has the lowest mean Hausdorff distance.([Simulation studies, p.13](https://arxiv.org/pdf/2609.36594v1#page=13 "Table 1 shows that Tensor recovers the correct number of changes in all 100 repetitions of each setting, and its refined estimates attain the lowest mean Hausdorff distance."))

