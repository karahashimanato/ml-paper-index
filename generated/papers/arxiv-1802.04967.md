<!-- このファイルは scripts/generate.py が生成する。手で編集しない。 -->

# DESlib: A Dynamic ensemble selection library in Python

- カード: [`arxiv-1802.04967`](../../papers/arxiv-1802.04967.yaml)
- 著者: Rafael M. O. Cruz, Luiz G. Hafemann, Robert Sabourin, George D. C. Cavalcanti
- 年・掲載: 2018
- 原論文: [PDF](https://arxiv.org/pdf/1802.04967v3)(arXiv v3、カード作成時に読んだ版)
- タグ: dynamic-ensemble-selection, model-selection, supervised
- 人手レビュー: 未

## 主張

出典のリンクは原論文PDFの該当ページを開く。リンクにカーソルを合わせると原文の引用が表示される。

- **c1** Rationale of dynamic selection: competence of each pool classifier is estimated per query and only the most competent classifier (or an ensemble of the most competent) predicts, on the premise that each base classifier is an expert in a different local region of the feature space.([Introduction, p.1](https://arxiv.org/pdf/1802.04967v3#page=1 "The rationale for such techniques is that not every classiﬁer in the pool is an expert in classifying all unknown samples; rather, each base classiﬁer is an expert in a different local region of the feature space."))
- **c2** Modular design following the authors' taxonomy (Cruz et al., 2018): a DS method is defined by how the region of competence is defined, the source of information used to estimate competence, and the selection approach; new methods often only need estimate_competence and select.([Project management, p.2](https://arxiv.org/pdf/1802.04967v3#page=2 "(1) the methodology used to deﬁne the local region, in which the competence level of the base classiﬁers are estimated (region of competence); (2) the source of information used to estimate the competence"))
- **c3** What is selected: DCS selects only the single base classifier with the highest competence; DES selects all base classifiers that reach a minimum competence level.([Implemented techniques, p.3](https://arxiv.org/pdf/1802.04967v3#page=3 "All base classiﬁers that attain a minimum competence level are selected to compose the ensemble of classiﬁers."))
- **c4** Baselines provided: static ensembles commonly used as baselines for DS methods, including Single Best, Static Selection, the Oracle and Stacked Generalization.([Implemented techniques, p.3](https://arxiv.org/pdf/1802.04967v3#page=3 "Static Ensembles: This module provides the implementation of static ensemble techniques that are usually used as a baseline for the comparison of DS methods: Single Best (SB), Static Selection (SS), Oracle and Stacked Generalization."))
- **c5** Usage defaults: from version 0.3 each method has default values and can train its pool inside fit when no trained pool is given; the documented example fits the DS method on a separate dynamic selection set (X_dsel).([Usage, p.4](https://arxiv.org/pdf/1802.04967v3#page=4 "As of version 0.3, each implemented method comes with a list of default values, not requiring a trained list of classiﬁers as input."))
- **c6** Scope / future work: dynamic selection for other contexts such as one-class classification and regression is listed as future work (the library covers classification).([Conclusion and future plans, p.4](https://arxiv.org/pdf/1802.04967v3#page=4 "Future work on this library includes the implementation of dynamic selection methods in different contexts, such as One-Class-Classiﬁcation (OCC) and regression."))

