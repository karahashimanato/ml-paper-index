<!-- このファイルは scripts/generate.py が生成する。手で編集しない。 -->

# Scaling Vision Transformers

- カード: [`arxiv-2106.04560`](../../papers/arxiv-2106.04560.yaml)
- 著者: Xiaohua Zhai, Alexander Kolesnikov, Neil Houlsby, Lucas Beyer
- 年・掲載: 2021
- 原論文: [PDF](https://arxiv.org/pdf/2106.04560v2)(arXiv v2、カード作成時に読んだ版)
- タグ: deep-learning, image-classification, scaling-laws, supervised
- 人手レビュー: 未

## 主張

出典のリンクは原論文PDFの該当ページを開く。リンクにカーソルを合わせると原文の引用が表示される。

- **c1** Experimental range: models from five million to two billion parameters, datasets from one million to three billion training images, and compute from below one to beyond 10,000 TPUv3 core-days; the frontier is characterized on two datasets (the paper names public ImageNet-21k and proprietary JFT-3B elsewhere).([Introduction, p.1](https://arxiv.org/pdf/2106.04560v2#page=1 "In particular, we experiment with models ranging from ﬁve million to two billion parameters, datasets ranging from one million to three billion training images and com-pute budgets ranging from below one TPUv3 core-day to beyond 10 000 core-days."))
- **c2** Cost measurement: since all models were trained on TPUv3, total compute is measured in TPUv3 core-days (not FLOPs).([Core Results, p.2](https://arxiv.org/pdf/2106.04560v2#page=2 "All models are trained on TPUv3, thus total compute is measured in TPUv3 core-days."))
- **c3** Main claim: with enough training data, the ViT performance-compute frontier roughly follows a saturating power law.([Conclusion, p.8](https://arxiv.org/pdf/2106.04560v2#page=8 "We demonstrate that the performance-compute frontier for ViT models with enough training data roughly follows a (saturating) power law."))
- **c4** Compute allocation: for ViT within the studied range, staying on the frontier requires scaling compute and model size together; not increasing model size when extra compute is available is suboptimal.([Conclusion, p.8](https://arxiv.org/pdf/2106.04560v2#page=8 "Crucially, in order to stay on this frontier one has to simultaneously scale compute and model size; that is, not increasing a model’s size when extra com-pute becomes available is suboptimal."))
- **c5** Sample efficiency: bigger models reach the same error with fewer seen images, and the authors suggest that with sufficient data, training a larger model for fewer steps is preferable, mirroring results in language modeling and machine translation.([Big models are more sample efficient, p.3](https://arxiv.org/pdf/2106.04560v2#page=3 "Our results suggest that with sufﬁcient data, training a larger model for fewer steps is preferable."))
- **c6** Data limitation: the scaling-law study uses the proprietary JFT-3B dataset; to make the insights more reliable, the authors verify that the scaling laws also apply on public ImageNet-21k.([Discussion (Limitations), p.8](https://arxiv.org/pdf/2106.04560v2#page=8 "This work uses the proprietary JFT-3B dataset for the scaling laws study."))
- **c7** Scope caveat: the conclusions may not generalize beyond the studied scale or beyond the ViT model family.([Conclusion, p.8](https://arxiv.org/pdf/2106.04560v2#page=8 "Note, that our conclusions may not necessarily generalize beyond the scale we have studied and they may not generalize beyond the ViT family of models."))

