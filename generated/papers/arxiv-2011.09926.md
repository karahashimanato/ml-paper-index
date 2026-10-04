<!-- このファイルは scripts/generate.py が生成する。手で編集しない。 -->

# Challenges in Deploying Machine Learning: a Survey of Case Studies

- カード: [`arxiv-2011.09926`](../../papers/arxiv-2011.09926.yaml)
- 著者: Andrei Paleyes, Raoul-Gabriel Urma, Neil D. Lawrence
- 年・掲載: 2020
- 原論文: [PDF](https://arxiv.org/pdf/2011.09926v3)(arXiv v3、カード作成時に読んだ版)
- タグ: automl-systems, mlops
- 人手レビュー: 未

## 主張

出典のリンクは原論文PDFの該当ページを開く。リンクにカーソルを合わせると原文の引用が表示される。

- **c1** Main claim: by mapping the challenges found in reports to the steps of the deployment workflow, the authors show that practitioners face issues at each stage of deployment.([Abstract, p.1](https://arxiv.org/pdf/2011.09926v3#page=1 "By mapping found challenges to the steps of the machine learning deployment workﬂow we show that practitioners face issues at each stage of the deployment process."))
- **c2** Evidence base: case study papers (single deployment project), review papers of a field/industry, and lessons-learned papers, mostly limited to the last five years with a few exceptions; the authors state they conducted no interviews themselves.([Introduction, p.2](https://arxiv.org/pdf/2011.09926v3#page=2 "We have not conducted any interviews ourselves as part of this study."))
- **c3** Monitoring (citing Sculley et al.): the ML community is said to be early in understanding which data and model metrics to monitor and how to trigger alarms when they deviate; monitoring evolving input data, prediction bias and overall performance is called an open problem.([Monitoring, p.13](https://arxiv.org/pdf/2011.09926v3#page=13 "Monitoring of evolving input data, prediction bias and overall performance of ML models is an open problem."))
- **c4** Outlier detection (citing Klaise et al.): outlier detection is presented as a key instrument to flag predictions that cannot be used in production; deploying the detector is itself a challenge because labeled outlier data are scarce, making training semi-supervised or unsupervised.([Monitoring, p.13](https://arxiv.org/pdf/2011.09926v3#page=13 "Klaise et al. [72] point out the importance of outlier detection as a key instrument to ﬂag model predictions that cannot be used in a production setting."))
- **c5** Case study cited (Ackermann et al., early intervention system for two US police departments): data integrity checks, anomaly detection and performance metrics had to be built from scratch; the survey takes this as a sign that out-of-the-box tooling of end-to-end platforms often does not fit problem specifics.([Monitoring, p.13](https://arxiv.org/pdf/2011.09926v3#page=13 "However, the authors explain that they had to build all these checks from scratch in order to maintain good model performance."))
- **c6** Updating: besides when to retrain (concept drift, linked to monitoring) and how to deliver the model artifact (continuous delivery), the survey notes (citing Bansal et al. and Srivastava et al.) that updates may harm users or downstream systems through behavior changes, e.g. backward-incompatible updates.([Updating, p.14](https://arxiv.org/pdf/2011.09926v3#page=14 "While updating is necessary for keeping a model up to date with recent ﬂuctuations in the data, it may also inﬂict damage on users or downstream systems because of the changes in the model’s behavior, even without causing obvious software errors."))
- **c7** Stated limitation: the set of reviewed challenges is far from complete; identifying further (especially non-technical) challenges, possibly via interviews with industry representatives, is left as further work.([Further Work, p.21](https://arxiv.org/pdf/2011.09926v3#page=21 "Even though the set of challenges we reviewed covers every stage of the ML deployment workﬂow, it is far from complete."))

