<!-- このファイルは scripts/generate.py が生成する。手で編集しない。 -->

# LSTM-based Encoder-Decoder for Multi-sensor Anomaly Detection

- カード: [`arxiv-1607.00148`](../../papers/arxiv-1607.00148.yaml)
- 著者: Pankaj Malhotra, Anusha Ramakrishnan, Gaurangi Anand, Lovekesh Vig, Puneet Agarwal, Gautam Shroff
- 年・掲載: 2016 ICML 2016 Anomaly Detection Workshop
- 原論文: [PDF](https://arxiv.org/pdf/1607.00148v2)(arXiv v2、カード作成時に読んだ版)
- タグ: autoencoders, reconstruction-based-detectors, time-series-anomaly-detection, unsupervised
- 人手レビュー: 未

## 主張

出典のリンクは原論文PDFの該当ページを開く。リンクにカーソルを合わせると原文の引用が表示される。

- **c1** Training data assumption: EncDec-AD is trained on normal sequences only, which the authors present as useful when anomalous data is unavailable or sparse (e.g. machines serviced before anomalies appear).([Introduction, p.2](https://arxiv.org/pdf/1607.00148v2#page=2 "EncDec-AD uses only the normal sequences for training."))
- **c2** Detection premise (hedged): since the encoder-decoder has only seen normal instances, it may not reconstruct an anomalous sequence well, which would give higher reconstruction errors than for normal sequences.([Introduction, p.2](https://arxiv.org/pdf/1607.00148v2#page=2 "When given an anomalous sequence, it may not be able to reconstruct it well, and hence would lead to higher reconstruction errors compared to the reconstruction errors for the normal sequences."))
- **c3** Anomaly score: normal data is split into sN (training), vN1 (early stopping), vN2 and tN, and anomalous data into vA and tA; a Normal distribution is fitted by maximum likelihood to the point-wise absolute reconstruction-error vectors on vN1, and the anomaly score of a point is (e - mu)^T Sigma^-1 (e - mu).([Section 2.2, p.2](https://arxiv.org/pdf/1607.00148v2#page=2 "are used to estimate the parameters µ and Σ of a Normal distribution N(µ, Σ)"))
- **c4** Threshold selection uses labeled anomalies: when enough anomalous sequences are available, the threshold tau is learnt to maximize an F-beta score (beta < 1, anomalous = positive class); tau and the number of LSTM units c are chosen on the validation sets vN2 (normal) and vA (anomalous).([Section 2.2, p.3](https://arxiv.org/pdf/1607.00148v2#page=3 "The parameters τ and c are chosen with maximum Fβ score on the validation sequences in vN2 and vA."))
- **c5** Window-level labels: a window containing an anomalous pattern is labelled anomalous as a whole, which the authors find helpful when the exact position of an anomaly is unknown; for the engine data the only information is a repair date, and the last runs before repair are assumed anomalous and the first runs after repair normal.([Section 2.2, p.3](https://arxiv.org/pdf/1607.00148v2#page=3 "is helpful in many real-world applications where the exact position of anomaly is not known."))
- **c6** ECG exception: with only one anomaly in the ECG series, vN2 and vA are not created; c is chosen by minimum reconstruction error on vN1, and the threshold is set from normal data only as the mean plus one standard deviation of the anomaly scores on vN1.([Section 3.1, p.4](https://arxiv.org/pdf/1607.00148v2#page=4 "We choose τ = µa + σa, where µa and σa are the mean and standard deviation of the anomaly scores of the points from vN1."))
- **c7** Data provenance: power demand, space shuttle valve and ECG are taken from Keogh et al. (2005); the engine data (Engine-P, Engine-NP; 12 sensors reduced to the first principal component) is proprietary, from a real-life project.([Section 3, p.3](https://arxiv.org/pdf/1607.00148v2#page=3 "whereas the engine dataset is a proprietary one encountered in a real-life project."))
- **c8** Comparison with the authors' own prediction-based LSTM-AD (Malhotra et al., 2015, which shares authors with this paper): LSTM-AD gives better results on the predictable datasets (Space Shuttle, Power, Engine-P; F0.1 of 0.84, 0.90, 0.89 as stated in the text), while EncDec-AD gives better results on the unpredictable Engine-NP.([Section 3.2, p.4](https://arxiv.org/pdf/1607.00148v2#page=4 "On the other hand, EncDec-AD gives better results for Engine-NP where the sequences are not predictable."))
- **c9** The authors conclude (hedged) that because EncDec-AD detects anomalies even in unpredictable time series, it may be more robust than models that rely on predictability.([Discussion, p.4](https://arxiv.org/pdf/1607.00148v2#page=4 "and hence may be more robust compared to such models."))

