<!-- このファイルは scripts/generate.py が生成する。手で編集しない。 -->

# PyOD: A Python Toolbox for Scalable Outlier Detection

- カード: [`arxiv-1901.01588`](../../papers/arxiv-1901.01588.yaml)
- 著者: Yue Zhao, Zain Nasrullah, Zheng Li
- 年・掲載: 2019 JMLR
- 原論文: [PDF](https://arxiv.org/pdf/1901.01588v2)(arXiv v2、カード作成時に読んだ版)
- タグ: anomaly-detection, classical-outlier-detectors, deep-learning, unsupervised
- 人手レビュー: 未

## 主張

出典のリンクは原論文PDFの該当ページを開く。リンクにカーソルを合わせると原文の引用が表示される。

- **c1** Motivation: Python lacked a dedicated outlier detection toolkit; existing implementations were single-algorithm tools (e.g. PyNomaly) or part of general frameworks such as scikit-learn that do not cater specifically to anomaly detection, while ELKI, RapidMiner (Java) and outliers (R) exist in other languages.([Introduction, p.1](https://arxiv.org/pdf/1901.01588v2#page=1 "However, Python, one of the most important languages in machine learning, still lacks a dedicated toolkit for outlier detection."))
- **c2** Coverage: more than 20 algorithms, from classical techniques such as local outlier factor to neural network architectures such as autoencoders and adversarial models, plus combination methods for merging detector results and outlier ensembles (version 0.7.0 summarized in Table 1).([Introduction, p.2](https://arxiv.org/pdf/1901.01588v2#page=2 "Firstly, it contains more than 20 algorithms which cover both classical techniques such as local outlier factor and recent neural network architectures such as autoencoders or adversarial models."))
- **c3** Unified API inspired by scikit-learn: every detector inherits from a base class with fit (train statistics), decision_function (raw outlier scores for unseen data), predict (binary labels) and predict_proba (probability by normalization or unification); fitted training scores and labels are available as attributes.([Section 3 (Library Design and Implementation), p.3](https://arxiv.org/pdf/1901.01588v2#page=3 "fit processes the train data and computes the necessary statistics"))
- **c4** Scalability: selected algorithms are JIT-compiled with numba and some support multi-core execution via joblib; the toolbox relies on numpy, scipy and scikit-learn, and neural networks additionally require Keras.([Section 3 (Library Design and Implementation), p.3](https://arxiv.org/pdf/1901.01588v2#page=3 "To enhance model scalability, select algorithms (Table 1) are optimized with JIT using numba."))
- **c5** Engineering practices: continuous integration on several Python versions and operating systems, PEP8 and CodeClimate checks, refactoring of complex code, and unit tests for 95% overall code coverage.([Section 2 (Project Focus), p.3](https://arxiv.org/pdf/1901.01588v2#page=3 "code blocks with high cognitive complexity are actively refactored and a standard set of unit tests exist to ensure 95% overall code coverage"))
- **c6** The helper data generator used in the example creates inliers from a Gaussian distribution and outliers from a uniform distribution (two-dimensional artificial data); the paper's only performance output is this demo, and it reports no benchmark comparison of the detectors.([Section 3 (Library Design and Implementation), p.4](https://arxiv.org/pdf/1901.01588v2#page=4 "which generates inliers from a Gaussian distribution and outliers from a uniform distribution"))
- **c7** Stated future work (current gaps): models for time series and geospatial data, computational efficiency through distributed computing, and engineering issues such as sparse matrices and memory limitations.([Section 4 (Conclusion and Future Plans), p.5](https://arxiv.org/pdf/1901.01588v2#page=5 "As avenues for future work, we plan to enhance the toolbox by implementing models that work well with time series and geospatial data, improving computational eﬃciency through distributed computing and addressing engineering challenges such as handling sparse matrices or memory limitations."))

