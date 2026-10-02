<!-- このファイルは scripts/generate.py が生成する。手で編集しない。 -->

# Adaptive Multi-Task Learning for Urban Air Quality Assessment

- カード: [`doi-10.65542_djei.v2i3.83`](../../papers/doi-10.65542_djei.v2i3.83.yaml)
- 著者: Iman Youssif Ibrahim, Dindar M. Ahmed
- 年・掲載: 2026 Dasinya Journal for Engineering and Informatics
- 原論文: [PDF](https://dasinya.dpu.edu.krd/index.php/pub/article/download/83/38)(Publisher PDF via OpenAlex (publishedVersion)、カード作成時に読んだ版)
- タグ: supervised, tabular-classification, tabular-mlp, tabular-regression
- 人手レビュー: 未

## 主張

出典のリンクは原論文PDFの該当ページを開く。リンクにカーソルを合わせると原文の引用が表示される。

- **c1** TMTL-AQI jointly performs AQI category classification, PM2.5/PM10 regression and auxiliary AQI value regression from structured data with a shared backbone.([Abstract, p.1](https://dasinya.dpu.edu.krd/index.php/pub/article/download/83/38#page=1 "The model simultaneously performs three tasks: Air Quality Index category classification, PM2.5 and PM10 particulate matter regression, and auxiliary AQI value prediction."))
- **c2** Data and split: the TRAQID dataset (26,678 samples, 2022-2024) with a single stratified 80:20 train/test split.([Dataset Description, p.4](https://dasinya.dpu.edu.krd/index.php/pub/article/download/83/38#page=4 "The dataset comprises 26,678 samples collected between 2022 and 2024 and was divided into training and testing sets using a stratified 80:20 ratio to preserve the class distribution."))
- **c3** The evaluated models are a single-task model, a multi-task model and the proposed TMTL-AQI; no tree-based or other tabular baselines were run (the AQC-Net comparison uses results reported for AQC-Net).([Results, p.8](https://dasinya.dpu.edu.krd/index.php/pub/article/download/83/38#page=8 "Three models were evaluated: a single-task model, a multi-task model, and the proposed (TMTL-AQI) model."))
- **c4** Hyperparameters were set empirically through preliminary validation.([Proposed Approach, p.7](https://dasinya.dpu.edu.krd/index.php/pub/article/download/83/38#page=7 "The selected hyperparameters were determined empirically through preliminary validation to achieve stable convergence and consistent validation performance."))
- **c5** The comparison with AQC-Net uses results reported for AQC-Net, not a re-run under the same conditions.([Discussion, p.10](https://dasinya.dpu.edu.krd/index.php/pub/article/download/83/38#page=10 "Table 5 provides an additional comparison with the state-of-the-art results reported on the AQC-Net dataset."))
- **c6** Limitation: no ablation study was conducted for the temporal encoding and the auxiliary AQI head; this and evaluation across multiple random seeds are left to future work.([Discussion, p.10](https://dasinya.dpu.edu.krd/index.php/pub/article/download/83/38#page=10 "A limitation of this study is that no ablation study was conducted to evaluate the individual contribution of the temporal encoding and the auxiliary AQI regression head."))

