<!-- このファイルは scripts/generate.py が生成する。手で編集しない。 -->

# Stealing profits: Spread-based temporal hierarchy forecasting for day-ahead electricity markets

- カード: [`arxiv-2609.23223`](../../papers/arxiv-2609.23223.yaml)
- 著者: Arkadiusz Lipiecki, Nikolaos Kourentzes, Rafal Weron
- 年・掲載: 2026
- 原論文: [PDF](https://arxiv.org/pdf/2609.23223v1)(arXiv v1、カード作成時に読んだ版)
- タグ: deep-learning, in-context-learning, linear-models, supervised, tabular-foundation-model, time-series-forecasting
- 人手レビュー: 未

## 主張

出典のリンクは原論文PDFの該当ページを開く。リンクにカーソルを合わせると原文の引用が表示される。

- **c1** Jointly reconciling forecasts of hourly prices and all intraday price spreads improves performance across two European markets and three forecasting architectures.([Abstract, p.1](https://arxiv.org/pdf/2609.23223v1#page=1 "Here we show that a temporal hierarchy forecasting (THieF) framework that jointly reconciles forecasts of hourly electricity prices and all intraday price spreads consistently improves performance across two major European electricity markets and three different forecasting architectures."))
- **c2** The gains also hold for a pretrained TabPFN model.([Abstract, p.1](https://arxiv.org/pdf/2609.23223v1#page=1 "The gains persist even for a highly accurate pretrained TabPFN foundation model."))
- **c3** TabPFN-2 is used zero-shot, without tuning weights or hyperparameters, with a 3-year rolling window as the in-context support set.([Forecasting models, p.11](https://arxiv.org/pdf/2609.23223v1#page=11 "Forecasts are generated in the so-called zero-shot mode, i.e., without task-specific tuning of the model weights or hyperparameters."))
- **c4** Data come from two European day-ahead markets, German EPEX-DE and Spanish OMIE (public data spanning eight years).([Datasets, p.7](https://arxiv.org/pdf/2609.23223v1#page=7 "To ensure a sound assessment of the THieF approach, we consider two major European power markets: EPEX-DE (Germany) and OMIE (Spain)."))
- **c5** Statistical and economic rankings differ: TabPFN is the most accurate model, but NARX with Spread THieF gives the highest arbitrage profit.([Conclusions, p.21](https://arxiv.org/pdf/2609.23223v1#page=21 "although TabPFN is the most accurate model, NARX combined with Spread THieF yields the highest arbitrage profit in every market-efficiency combination"))
- **c6** Stated limitation: the battery arbitrage exercise is stylized (price-taking, one daily cycle, fixed round-trip cost).([Conclusions, p.21](https://arxiv.org/pdf/2609.23223v1#page=21 "The BESS exercise is deliberately stylized: we assume price-taking behavior, a single daily charge-discharge cycle, and a fixed round-trip cost."))

