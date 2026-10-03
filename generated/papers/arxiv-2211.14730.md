<!-- このファイルは scripts/generate.py が生成する。手で編集しない。 -->

# A Time Series is Worth 64 Words: Long-term Forecasting with Transformers

- カード: [`arxiv-2211.14730`](../../papers/arxiv-2211.14730.yaml)
- 著者: Yuqi Nie, Nam H. Nguyen, Phanwadee Sinthong, Jayant Kalagnanam
- 年・掲載: 2022
- 原論文: [PDF](https://arxiv.org/pdf/2211.14730v2)(arXiv v2、カード作成時に読んだ版)
- タグ: deep-learning, self-supervised, supervised, time-series-forecasting
- 人手レビュー: 未

## 主張

出典のリンクは原論文PDFの該当ページを開く。リンクにカーソルを合わせると原文の引用が表示される。

- **c1** Method: PatchTST segments each series into subseries-level patches used as Transformer input tokens, and processes channels independently with shared embedding and Transformer weights across all series.([Abstract, p.1](https://arxiv.org/pdf/2211.14730v2#page=1 "It is based on two key components: (i) segmentation of time series into subseries-level patches which are served as input tokens to Transformer; (ii) channel-independence"))
- **c2** Main claim: PatchTST significantly improves long-term forecasting accuracy compared with SOTA Transformer-based models.([Abstract, p.1](https://arxiv.org/pdf/2211.14730v2#page=1 "Our channel-independent patch time series Transformer (PatchTST) can improve the long-term forecasting accuracy signiﬁcantly when compared with that of SOTA Transformer-based models."))
- **c3** Baseline protocol: baseline results are collected from Zeng et al. (2022) (default look-back 96 for Transformers, 336 for DLinear; Appendix A.1.2 gives 36 and 104 for ILI); additionally FEDformer, Autoformer and Informer are re-run for six look-back windows and the best result per task is kept to avoid under-estimating them. Whether this best-of-six selection used validation or test data was not found in the text.([Experiments: Baselines and Experimental Settings, p.6](https://arxiv.org/pdf/2211.14730v2#page=6 "But in order to avoid under-estimating the baselines, we also run FEDformer, Autoformer and Informer for six different look-back window L ∈{24, 48, 96, 192, 336, 720}, and always choose the best results to create strong baselines."))
- **c4** Versus DLinear (the linear baseline that challenged Transformers), PatchTST outperforms it in general, especially on the large datasets (Weather, Traffic, Electricity) and ILI.([Experiments: Results, p.6](https://arxiv.org/pdf/2211.14730v2#page=6 "Compared with the DLinear model, PatchTST can still outperform it in general, especially on large datasets (Weather, Trafﬁc, Electricity) and ILI dataset."))
- **c5** Self-supervised pretraining (masked patches, 40% masking): on large datasets, pretraining clearly improves over supervised training from scratch.([Representation learning: Comparison with Supervised Methods, p.7](https://arxiv.org/pdf/2211.14730v2#page=7 "As shown in the table, on large datasets our pre-training procedure contributes a clear improvement compared to supervised training from scratch."))
- **c6** Transfer learning (pretrain on Electricity, fine-tune on other datasets): fine-tuning MSE is slightly worse than pretraining on the same dataset, and in some cases worse than supervised training.([Representation learning: Transfer Learning, p.7](https://arxiv.org/pdf/2211.14730v2#page=7 "The ﬁne-tuning performance is also worse than supervised training in some cases."))
- **c7** Affiliations: one author is from Princeton University and three are from IBM Research.([Title page, p.1](https://arxiv.org/pdf/2211.14730v2#page=1 "1Princeton University 2IBM Research"))

