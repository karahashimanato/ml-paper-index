<!-- このファイルは scripts/generate.py が生成する。手で編集しない。 -->

# Lag-Llama: Towards Foundation Models for Probabilistic Time Series Forecasting

- カード: [`arxiv-2310.08278`](../../papers/arxiv-2310.08278.yaml)
- 著者: Kashif Rasul, Arjun Ashok, Andrew Robert Williams, Hena Ghonia, Rishika Bhagwatkar, Arian Khorasani, Mohammad Javad Darvishi Bayazi, George Adamopoulos, Roland Riachi, Nadhir Hassen, Marin Biloš, Sahil Garg, Anderson Schneider, Nicolas Chapados, Alexandre Drouin, Valentina Zantedeschi, Yuriy Nevmyvaka, Irina Rish
- 年・掲載: 2023
- 原論文: [PDF](https://arxiv.org/pdf/2310.08278v3)(arXiv v3、カード作成時に読んだ版)
- タグ: deep-learning, self-supervised, time-series-forecasting, time-series-foundation-model
- 人手レビュー: 未

## 主張

出典のリンクは原論文PDFの該当ページを開く。リンクにカーソルを合わせると原文の引用が表示される。

- **c1** Method: Lag-Llama is a general-purpose foundation model for univariate probabilistic forecasting built on a decoder-only transformer that uses lags as covariates.([Abstract, p.1](https://arxiv.org/pdf/2310.08278v3#page=1 "We present Lag-Llama, a general-purpose foundation model for univariate probabilistic time series forecasting based on a decoder-only transformer architecture that uses lags as covariates."))
- **c2** Pretraining data: the pretraining corpus comprises 7,965 univariate series (around 352 million data windows/tokens); it is the pretraining part of a collated collection of 27 datasets in six domains, from which held-out test datasets were also taken.([Datasets, p.5](https://arxiv.org/pdf/2310.08278v3#page=5 "Our pretraining corpus comprises a total of 7, 965 different univariate time series, each of different lengths, when put together, comprising a total of around 352 million data windows (tokens) for our model to train on."))
- **c3** Zero-shot definition: some datasets from each pretraining domain are held out as unseen test datasets, and datasets from entirely different domains are also set aside; 'domain' is only a grouping label.([Datasets, p.5](https://arxiv.org/pdf/2310.08278v3#page=5 "We leave out a few datasets from each domain for testing the few-shot generalization abilities of the pretrained model, whle using the remaining datasets for pretraining the founda-tion model."))
- **c4** Evaluation protocol: following Shchur et al. (2023), all reported results are on the last prediction window of each test split.([Appendix (Protocol Details), p.17](https://arxiv.org/pdf/2310.08278v3#page=17 "Following typical evaluation setups (Shchur et al., 2023), all results reported in the paper are on the last prediction window of the test splits defined in App. §A."))
- **c5** Baseline training: supervised baselines (via AutoGluon and others) were trained with the same setup as Lag-Llama fine-tuning; a dataset-specific hyperparameter search for baselines was not found in the text (Lag-Llama itself used a 100-configuration random search on pretraining validation loss).([Appendix (Protocol Details), p.17](https://arxiv.org/pdf/2310.08278v3#page=17 "We use the same setup as fine-tuning Lag-Llama, for all supervised baselines that we produce results for in the paper."))
- **c6** Main empirical claim: zero-shot Lag-Llama is comparable to baselines, and after fine-tuning it reaches the best average rank among the compared methods on the unseen datasets.([Zero-Shot & Finetuning Performance on New Data, p.7](https://arxiv.org/pdf/2310.08278v3#page=7 "In the zero-shot setting, Lag-Llama achieves comparable performance to all baselines, with an average rank of 6.714."))
- **c7** In-distribution caveat: on its pretraining datasets Lag-Llama is not the best model on each dataset, which the authors attribute to its training budget being split across all pretraining datasets.([Appendix (Results on the Pretraining Datasets), p.17](https://arxiv.org/pdf/2310.08278v3#page=17 "This is reflected in the results, as Lag-Llama is not the best performing model in each dataset."))
- **c8** Metrics: CRPS computed from 100 empirical samples, averaged over the prediction horizon and all series of a dataset; the average rank across datasets is also reported.([Inference and Model Evaluation, p.6](https://arxiv.org/pdf/2310.08278v3#page=6 "We use 100 empirical samples and report the CRPS averaged over the prediction horizon and across all the time series of a dataset."))

