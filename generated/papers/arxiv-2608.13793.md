<!-- このファイルは scripts/generate.py が生成する。手で編集しない。 -->

# On the Brittleness of Maximum Likelihood Estimation for Gaussian Process Hyperparameter Optimization

- カード: [`arxiv-2608.13793`](../../papers/arxiv-2608.13793.yaml)
- 著者: Tyler R. Johnson, Kian Ben-Jacob, Christopher P. Muller, Ramin Bostanabad
- 年・掲載: 2026
- 原論文: [PDF](https://arxiv.org/pdf/2608.13793v1)(arXiv v1、カード作成時に読んだ版)
- タグ: gaussian-processes, in-context-learning, supervised, tabular-classification, tabular-foundation-model, tabular-regression
- 人手レビュー: 未

## 主張

出典のリンクは原論文PDFの該当ページを開く。リンクにカーソルを合わせると原文の引用が表示される。

- **c1** Implemented carefully, GPs trained via MLE remain highly competitive and can outperform foundation models such as TabPFN in prediction accuracy, UQ quality and inference cost.([Conclusion, p.19](https://arxiv.org/pdf/2608.13793v1#page=19 "When implemented carefully, GPs trained via MLE remain highly competitive and can outperform foundation models such as TabPFN in prediction accuracy, UQ quality, and inference cost."))
- **c2** To stress-test GPs, the GPs are trained with the default settings of GPyTorch and GP+.([Evaluation protocols, p.8](https://arxiv.org/pdf/2608.13793v1#page=8 "To stress-test GPs, we train them via the default settings of Gpytorch [55] and GP+ [56]."))
- **c3** The regression benchmarks are analytic test functions from a simulation-experiment library, with categorical inputs studied via the Buckling function.([Evaluation protocols, p.8](https://arxiv.org/pdf/2608.13793v1#page=8 "Nine benchmark regression problems are adopted from [57] (i.e. Ackley, Borehole, Dixon-Price, Griewank, Rosenbrock, Wing Weight, and Zakharov) and we study the effects of categorical inputs in the Buckling function obtained from [58]."))
- **c4** For the comparison with TabPFN, the GP training process and kernel were not fine-tuned; evaluating the models under their best settings is left open.([Conclusion, p.20](https://arxiv.org/pdf/2608.13793v1#page=20 "For a fair comparison, we refrained from fine-tuning the training process and kernel of the GPs when comparing them to TabPFN but it is interesting to evaluate these models under their best settings."))
- **c5** The studies were mostly limited to analytic benchmarks with Gaussian observation noise.([Conclusion, p.20](https://arxiv.org/pdf/2608.13793v1#page=20 "Our studies were mostly limited to analytic benchmarks with Gaussian observation noise."))
- **c6** GP+, one of the evaluated GP libraries, is described by the authors as their own package (conflict-of-interest relevant: the authors' library is compared against TabPFN).([Section 3.2, p.8](https://arxiv.org/pdf/2608.13793v1#page=8 "In our GP+ package, the hyperparameters corresponding to the kernel in Equation (11) are bounded"))

