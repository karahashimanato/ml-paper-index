<!-- このファイルは scripts/generate.py が生成する。手で編集しない。 -->

# Model Assertions for Monitoring and Improving ML Models

- カード: [`arxiv-2003.01668`](../../papers/arxiv-2003.01668.yaml)
- 著者: Daniel Kang, Deepti Raghavan, Peter Bailis, Matei Zaharia
- 年・掲載: 2020
- 原論文: [PDF](https://arxiv.org/pdf/2003.01668v3)(arXiv v3、カード作成時に読んだ版)
- タグ: deep-learning, mlops, supervised
- 人手レビュー: 未

## 主張

出典のリンクは原論文PDFの該当ページを開く。リンクにカーソルを合わせると原文の引用が表示される。

- **c1** Abstraction: model assertions are arbitrary functions over a model's input and output that indicate when errors may be occurring (e.g., an object rapidly changing its class in a video); they return a Boolean or continuous severity score, 0 meaning abstention.([Abstract, p.1](https://arxiv.org/pdf/2003.01668v3#page=1 "Model assertions are arbitrary functions over a model’s input and output that indicate when errors may be occurring, e.g., a function that triggers if an object rapidly changes its class in a video."))
- **c2** Runtime use as stated by the authors: assertions can log unexpected behavior or automatically trigger corrective actions such as shutting down an autopilot. The evaluation measures assertion precision, high-confidence errors found, active learning and weak supervision; an experiment where an assertion triggers an automatic runtime corrective action was not found in the text.([Introduction, p.2](https://arxiv.org/pdf/2003.01668v3#page=2 "First, we show that model assertions can be used for runtime monitoring: they can be used to log unexpected behavior or automatically trigger corrective actions, e.g., shutting down an autopilot."))
- **c3** Settings: four workloads based on industrial and academic use cases: TV news (50 problematic hour-long segments with precomputed outputs; no retraining possible), video analytics (ResNet-34 SSD pretrained on MS-COCO on night-street video), autonomous vehicles (NuScenes; PointPillars LIDAR and SSD camera detectors) and AF classification from ECG (CINC17).([Experimental Setup, p.7](https://arxiv.org/pdf/2003.01668v3#page=7 "We evaluated OMG and model assertions on four diverse ML workloads based on real industrial and academic use-cases: analyzing TV news, video analytics, autonomous vehicles, and medical classiﬁcation."))
- **c4** Precision protocol: for each assertion, 50 randomly sampled data points that triggered it were checked manually for an incorrect model output. Only precision among flagged points is reported; a recall or miss-rate measurement for assertions was not found in the text.([Evaluation, p.8](https://arxiv.org/pdf/2003.01668v3#page=8 "To test this, we randomly sampled 50 data points that triggered each assertion and manually checked whether that data point had an incorrect output from the ML model."))
- **c5** High-confidence errors: for the video-analytics assertions, the 10 highest-confidence errors per assertion were placed in the confidence distribution of all boxes; the authors state uncertainty-based monitoring would not catch these errors.([Evaluation, p.8](https://arxiv.org/pdf/2003.01668v3#page=8 "Importantly, uncertainty-based methods of monitoring would not catch these errors."))
- **c6** Fallback inside BAL (active learning): BAL samples data flagged by assertions in proportion to the marginal reduction in assertions fired; when assertions cannot be reduced (e.g., noisy assertions; all reductions under 1% in Algorithm 2), it defaults to random or uncertainty sampling as the user specifies. The authors state BAL itself has no statistical guarantees and is verified empirically.([Active learning with BAL, p.6](https://arxiv.org/pdf/2003.01668v3#page=6 "In this case, BAL will default to random sampling or uncertainty sampling, as speciﬁed by the user."))
- **c7** Stated limitations: assertions have not been thoroughly evaluated in real-time systems and may add overhead where actuation has tight latency constraints (e.g., AVs), though they can be run over historical data; the authors also list API expressiveness for some temporal assertions and out-of-scope issues such as training-set bias.([Discussion, p.10](https://arxiv.org/pdf/2003.01668v3#page=10 "Second, we have not thoroughly evaluated model assertions’ performance in real-time systems."))

