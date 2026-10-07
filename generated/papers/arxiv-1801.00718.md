<!-- このファイルは scripts/generate.py が生成する。手で編集しない。 -->

# Selective review of offline change point detection methods

- カード: [`arxiv-1801.00718`](../../papers/arxiv-1801.00718.yaml)
- 著者: Charles Truong, Laurent Oudre, Nicolas Vayatis
- 年・掲載: 2018 Signal Processing
- 原論文: [PDF](https://arxiv.org/pdf/1801.00718v3)(arXiv v3、カード作成時に読んだ版)
- タグ: change-point-detection, kernel-methods, linear-models, unsupervised
- 人手レビュー: 未

## 主張

出典のリンクは原論文PDFの該当ページを開く。リンクにカーソルを合わせると原文の引用が表示される。

- **c1** Framework: offline detection is cast as minimizing a sum of segment costs, with a known number of changes (P1) or with a complexity penalty (P2). Methods are characterized by a cost function (a measure of homogeneity that encodes the type of change detectable), a search method (exact or approximate, trading complexity and accuracy), and a constraint; too small a penalty detects many changes, even noise, while too much penalization detects only the most significant changes or none.([Section 2.3, p.6](https://arxiv.org/pdf/1801.00718v3#page=6 "Precisely, detection methods are expressed as the combination of the following three elements."))
- **c2** Scope limitation: Bayesian approaches are not covered by the review's framework, although the authors note they provide state-of-the-art results in several domains such as speech and sound processing.([Section 2.4, p.6](https://arxiv.org/pdf/1801.00718v3#page=6 "In particular, Bayesian approaches are not considered in the remainder of this article, even though they provide state-of-the-art results in several domains, such as speech and sound processing."))
- **c3** Where Bayesian methods are pointed to: the HMM is named as the most well-known Bayesian algorithm, later extended with Dirichlet processes or product partition models; readers are referred to other reviews for Bayesian approaches. Apart from this paragraph and the BIC/mBIC penalties, no further discussion of Bayesian change point methods was found in the text (searched for Bayes, posterior, prior).([Section 2.4, p.7](https://arxiv.org/pdf/1801.00718v3#page=7 "The interested reader can ﬁnd reviews of Bayesian approaches in [4] and [6]."))
- **c4** Theoretical evaluation: asymptotic consistency is defined on change point fractions (t/T), since the distances between true and estimated change point indexes in general do not converge to 0 even for simple models.([Section 3.1, p.9](https://arxiv.org/pdf/1801.00718v3#page=9 "As a result, consistency results in the literature only deal with change point fractions."))
- **c5** Empirical metrics reviewed: AnnotationError (difference in the number of changes), Hausdorff (worst temporal error), RandIndex, and F1-score with a user-defined margin M; precision and recall are well defined only if M is smaller than the minimum spacing between true change points, and over-segmentation drives precision toward zero and recall toward one.([Section 3.2.4, p.11](https://arxiv.org/pdf/1801.00718v3#page=11 "A breakpoint is considered detected up to a user-deﬁned margin of error M > 0; true positives Tp are true change points for which there is an estimated one at less than M samples, i.e."))
- **c6** Search costs (assuming O(1) cost evaluation): Opt (dynamic programming for a known K) is of order O(KT^2); Pelt solves the linearly penalized problem exactly with pruning and is of order O(T) under the assumption that regime lengths are randomly drawn from a uniform distribution; binary segmentation (greedy) is of order O(T log T).([Section 5.1.2, p.33](https://arxiv.org/pdf/1801.00718v3#page=33 "This results in a considerable speed-up: under the assumption that regime lengths are randomly drawn from a uniform distribution, the complexity of Pelt is of the order O(T)."))
- **c7** Penalty calibration: the linear (l0) penalty generalizes BIC and AIC; its smoothing parameter can be set by model-selection criteria that assume a model on the data, by heuristics such as cross-validation or the slope heuristics when no model is assumed, or by supervised procedures that minimize an approximation of the segmentation error on an annotated set of signals.([Section 6.1, p.41](https://arxiv.org/pdf/1801.00718v3#page=41 "In [138, 139], supervised algorithms are proposed: the chosen β is the one that minimizes an approximation of the segmentation error on an annotated set of signals."))
- **c8** The authors describe their own library ruptures (which implements most reviewed procedures) as the most comprehensive change point detection library.([Section 9 (Conclusion), p.49](https://arxiv.org/pdf/1801.00718v3#page=49 "Most detection procedures described above are available within the Python language from the package ruptures [37], which is the most comprehensive change point detection library."))

