<!-- このファイルは scripts/generate.py が生成する。手で編集しない。 -->

# AnoMamba: Aligning Reconstruction with Time Series Anomaly Detection via Selective Global Dependency Modeling

- カード: [`doi-10.24963_ijcai.2026_276`](../../papers/doi-10.24963_ijcai.2026_276.yaml)
- 著者: Junqi Chen, Xu Tan, Jie Chen, Susanto Rahardja
- 年・掲載: 2026 IJCAI 2026
- 原論文: [PDF](https://www.ijcai.org/proceedings/2026/0276.pdf)(IJCAI proceedings PDF、カード作成時に読んだ版)
- タグ: deep-learning, reconstruction-based-detectors, time-series-anomaly-detection, unsupervised
- 人手レビュー: 未

## 主張

出典のリンクは原論文PDFの該当ページを開く。リンクにカーソルを合わせると原文の引用が表示される。

- **c1** Minimizing reconstruction loss alone lets models reconstruct anomalies well by overfitting local patterns (misalignment between reconstruction and detection).([Abstract, p.1](https://www.ijcai.org/proceedings/2026/0276.pdf#page=1 "Consequently, anomalies that violate global de- pendencies can also be reconstructed well, leading to a misalignment between reconstruction and detection."))
- **c2** Citing Kim et al., it avoids point-adjustment metrics and uses affiliation F1 and VUS-ROC.([Implemented details, p.5](https://www.ijcai.org/proceedings/2026/0276.pdf#page=5 "As noted by [Kim et al., 2022], point-adjustment metrics can lead to misleading rankings"))
- **c3** All thresholds are selected by SPOT.([Implemented details, p.5](https://www.ijcai.org/proceedings/2026/0276.pdf#page=5 "All thresholds were selected by SPOT"))

