<!-- このファイルは scripts/generate.py が生成する。手で編集しない。 -->

# ScalarLens: Numerical Embeddings with Stable Coordinates and Contextual Responses for CTR Prediction

- カード: [`arxiv-2609.29182`](../../papers/arxiv-2609.29182.yaml)
- 著者: Heng Yao, Tianying Liu, Yulou Shu, Yong He, Chuan Yuan, Kaibin Qiu, Guowei Chen, Jiayu Zhao, Siyun Hou
- 年・掲載: 2026
- 原論文: [PDF](https://arxiv.org/pdf/2609.29182v1)(arXiv v1、カード作成時に読んだ版)
- タグ: deep-learning, supervised, tabular-classification
- 人手レビュー: 未

## 主張

出典のリンクは原論文PDFの該当ページを開く。リンクにカーソルを合わせると原文の引用が表示される。

- **c1** ScalarLens is a numerical-feature embedding for CTR models that keeps a stable coordinate for a value while adapting its interpretation to the sample's context.([Abstract, p.1](https://arxiv.org/pdf/2609.29182v1#page=1 "We introduce ScalaRLens, a numerical embedding that preserves what a value is while adapting how it should be interpreted."))
- **c2** In the primary evaluation (19 representations, three datasets, nine backbones, three seeds, original numerical scales), ScalarLens ranks first in most settings and second in the rest.([Abstract, p.1](https://arxiv.org/pdf/2609.29182v1#page=1 "In a 1,539-run primary evaluation covering 19 representations, three datasets, nine backbones, and three seeds, ScalaRLens ranks first in 25 of 27 settings on original numerical scales and second in the remaining two."))
- **c3** Datasets are AutoML-A/E from AutoML3 and Criteo, with Criteo's numerical fields kept without a log transform; backbones share one fixed training configuration with early stopping on validation AUC.([Experiments, p.4](https://arxiv.org/pdf/2609.29182v1#page=4 "AutoML-A/E come from AutoML3 [11]; Criteo preserves all 13 numerical fields without a shared logarithmic transformation."))
- **c4** No method gets dataset-specific hyperparameters, private preprocessing, or a different split.([Experiments, p.5](https://arxiv.org/pdf/2609.29182v1#page=5 "No method receives private preprocessing, a different split, or hyperparameters specific to a dataset."))
- **c5** Several baselines (DAE, DEER, NaryDis, DAES) are the authors' re-implementations from published descriptions, not official code.([Experiments, p.5](https://arxiv.org/pdf/2609.29182v1#page=5 "DAE, DEER, NaryDis, and DAES-Gate/Tran are implementations based on the published descriptions because no official module compatible with our code version was available"))
- **c6** Stated limitation: AutoML-A/E come from one family, all datasets informed development, and the 27 settings are correlated; random splits do not establish temporal or cross-family transfer.([Discussion and Limitations, p.8](https://arxiv.org/pdf/2609.29182v1#page=8 "AutoML-A/E share one family, all datasets informed development, and the 27 settings are correlated."))

