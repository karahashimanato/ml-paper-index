<!-- このファイルは scripts/generate.py が生成する。手で編集しない。 -->

# SwitchPFN: Shared Switching Dynamics for Frozen In-Context Time Series Classification

- カード: [`arxiv-2609.29814`](../../papers/arxiv-2609.29814.yaml)
- 著者: Zhenyi Zhu, Jacqueline Pang, Peilin Shen, Tianyi Song, Tingwei Zhang, Keyi Hu, Kangjun Yin, Shiwei Pu, Yingbo Zhou, Chen Shao
- 年・掲載: 2026
- 原論文: [PDF](https://arxiv.org/pdf/2609.29814v1)(arXiv v1、カード作成時に読んだ版)
- タグ: in-context-learning, supervised, tabular-foundation-model, time-series-classification
- 人手レビュー: 未

## 主張

出典のリンクは原論文PDFの該当ページを開く。リンクにカーソルを合わせると原文の引用が表示される。

- **c1** SwitchPFN learns a shared projection and regime codebook from the training sequences so that local dynamics features are comparable across samples, and feeds the resulting table to a frozen TabPFN.([Abstract, p.1](https://arxiv.org/pdf/2609.29814v1#page=1 "We propose SwitchPFN, which learns a shared projection and regime codebook from the training sequences, making local dynamic operators and transition features directly comparable across samples."))
- **c2** On the evaluated benchmarks, SwitchPFN has the highest mean accuracy among the evaluated methods.([Abstract, p.1](https://arxiv.org/pdf/2609.29814v1#page=1 "Across the evaluated benchmarks, SwitchPFN achieves the highest mean accuracy among the evaluated methods, improving over the strongest baseline by 4.47% relatively."))
- **c3** Evaluation uses eight UEA multivariate time-series classification tasks with the official train/test splits.([Experimental setup, p.3](https://arxiv.org/pdf/2609.29814v1#page=3 "We evaluate eight University of East Anglia (UEA) tasks [33] covering five signal domains"))
- **c4** Several baselines (DTW, XGBoost, LSTM, Informer, DLinear) use historical three-run summaries, whereas the other methods use five repeats; baseline hyperparameter tuning is not described (not found in the text).([Experimental setup, p.3](https://arxiv.org/pdf/2609.29814v1#page=3 "DTW, XGBoost, LSTM, Informer, and DLinear use historical three-run summaries; other methods use five repeats."))
- **c5** SwitchPFN's own settings are frozen after a selection that uses only the training data.([Experimental setup, p.3](https://arxiv.org/pdf/2609.29814v1#page=3 "Settings are frozen after training-only selection."))
- **c6** The authors declare no conflicts of interest.([Acknowledgments, p.4](https://arxiv.org/pdf/2609.29814v1#page=4 "The authors declare no conflicts of interest."))

