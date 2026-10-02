<!-- このファイルは scripts/generate.py が生成する。手で編集しない。 -->

# Evaluation of hybrid models based on image segmentation and inference for pig weight estimation

- カード: [`doi-10.3389_frai.2026.1876396`](../../papers/doi-10.3389_frai.2026.1876396.yaml)
- 著者: Miguel Angel Valles-Coral, Kelvin Lleins Rojas-Córdova, Lloy Pinedo, Richard Injante, Pierre Vidaurre-Rojas, Jorge Saavedra-Ramírez, Fernando Ruiz-Saavedra, Williams Ramirez
- 年・掲載: 2026 Frontiers in Artificial Intelligence
- 原論文: [PDF](https://www.frontiersin.org/journals/artificial-intelligence/articles/10.3389/frai.2026.1876396/pdf)(Publisher PDF via OpenAlex (publishedVersion)、カード作成時に読んだ版)
- タグ: deep-learning, gradient-boosted-trees, kernel-methods, supervised, tabular-regression
- 人手レビュー: 未

## 主張

出典のリンクは原論文PDFの該当ページを開く。リンクにカーソルを合わせると原文の引用が表示される。

- **c1** The paper proposes a non-invasive computer-vision approach to estimate pig weight under real farm conditions.([Abstract, p.1](https://www.frontiersin.org/journals/artificial-intelligence/articles/10.3389/frai.2026.1876396/pdf#page=1 "This study proposes a non-invasive computer vision–based approach to estimate pig weight under real farm conditions in San Martín, Peru."))
- **c2** Frozen-CNN image embeddings are fed to SVR, XGBoost and CatBoost, evaluated with repeated stratified cross-validation and an independent test set.([Abstract, p.1](https://www.frontiersin.org/journals/artificial-intelligence/articles/10.3389/frai.2026.1876396/pdf#page=1 "The resulting embeddings were used as input for supervised regression models (SVR, XGBoost, and CatBoost), evaluated using repeated stratified cross-validation and an independent test set, with MAE, RMSE, and R² as performance metrics."))
- **c3** Hyperparameters are tuned on a separate tuning subset of the development data, distinct from the cross-validation pool and the held-out test set.([Materials and methods, p.6](https://www.frontiersin.org/journals/artificial-intelligence/articles/10.3389/frai.2026.1876396/pdf#page=6 "subset represented 15% of TrainDev and was used for hyperparameter optimization, while CVPool comprised the remaining data."))
- **c4** Models are compared with a Friedman test followed by Wilcoxon post hoc tests with Holm correction.([Abstract, p.1](https://www.frontiersin.org/journals/artificial-intelligence/articles/10.3389/frai.2026.1876396/pdf#page=1 "Statistical comparisons were conducted using the Friedman test followed by Wilcoxon post hoc analysis with Holm correction."))
- **c5** SVR gave the best results, with statistically significant differences from the other models.([Abstract, p.1](https://www.frontiersin.org/journals/artificial-intelligence/articles/10.3389/frai.2026.1876396/pdf#page=1 "showing statistically significant differences compared to the other models."))
- **c6** The authors note a tendency to underestimate weight in higher weight ranges, which they take to indicate a limitation of two-dimensional images in representing the animal's full volume.([Discussion, p.10](https://www.frontiersin.org/journals/artificial-intelligence/articles/10.3389/frai.2026.1876396/pdf#page=10 "However, the observed tendency toward underestimation in higher weight ranges indicates a limitation of two-dimensional images in representing the full volumetric characteristics of the animal, as also reported in previous studies (Liu et al., 2023; Paudel et al., 2023)."))

