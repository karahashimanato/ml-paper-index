<!-- このファイルは scripts/generate.py が生成する。手で編集しない。 -->

# Unsupervised Anomaly Detection via Variational Auto-Encoder for Seasonal KPIs in Web Applications

- カード: [`arxiv-1802.03903`](../../papers/arxiv-1802.03903.yaml)
- 著者: Haowen Xu, Wenxiao Chen, Nengwen Zhao, Zeyan Li, Jiahao Bu, Zhihan Li, Ying Liu, Youjian Zhao, Dan Pei, Yang Feng, Jie Chen, Zhaogang Wang, Honglin Qiao
- 年・掲載: 2018 WWW 2018
- 原論文: [PDF](https://arxiv.org/pdf/1802.03903v1)(arXiv v1、カード作成時に読んだ版)
- タグ: reconstruction-based-detectors, time-series-anomaly-detection, unsupervised, variational-autoencoders
- 人手レビュー: 未

## 主張

出典のリンクは原論文PDFの該当ページを開く。リンクにカーソルを合わせると原文の引用が表示される。

- **c1** Claimed contribution: the authors state that adopting VAEs (or generative models in general) for anomaly detection requires training on both normal and abnormal data, contrary to common intuition.([Introduction, p.1](https://arxiv.org/pdf/1802.03903v1#page=1 "For the first time in the literature, we discover that adopting VAE (or generative models in general) for anomaly detection requires training on both normal data and abnormal data, contrary to common intuition."))
- **c2** Training on contaminated data: the authors note that the earlier VAE-based detector of An & Cho [2] assumes training only on clean data, which is infeasible in their context, and that the VRNN-based work [36] does not discuss this problem.([Previous Work, p.2](https://arxiv.org/pdf/1802.03903v1#page=2 "Fifth, [2] assumes training only on clean data, which is infeasible in our context, while [36] does not discuss this problem."))
- **c3** M-ELBO: training windows are not filtered; missing points are filled with zeros and an indicator removes labelled anomalies and missing points from the reconstruction term, with the prior term scaled by the fraction of normal points; the objective still applies when there are no anomaly labels (the unsupervised case), in which unlabelled anomalies remain in the training windows.([Training, p.4](https://arxiv.org/pdf/1802.03903v1#page=4 "Note that Eqn (3) still holds when there is no labeled anomalies in the training data."))
- **c4** Anomaly score: following An & Cho [2], the score is the reconstruction probability E_q(z|x)[log p(x|z)], computed after MCMC imputation of known missing points and only for the last point of each window; the authors report that Monte Carlo estimation of p(x) by sampling on the prior does not work well enough in practice.([Detection, p.4](https://arxiv.org/pdf/1802.03903v1#page=4 "Since only the ordering rather than the exact values of anomaly scores are concerned in anomaly detection, we follow [2] and use the latter one."))
- **c5** Threshold: the paper does not propose a way to choose the detection threshold, calling it a difficult problem especially in the unsupervised scenario, and points to existing work (e.g. [21]) that might be applicable.([Future Work, p.11](https://arxiv.org/pdf/1802.03903v1#page=11 "We did not discuss how to choose the right threshold for detection."))
- **c6** Evaluation metric uses an oracle threshold: the headline metric is the best F-score over all thresholds on the test set, which the authors describe as the best possible performance given an optimal global threshold (AUC and alert delay are also reported).([Performance Metrics, p.5](https://arxiv.org/pdf/1802.03903v1#page=5 "The best F-score indicates the best possible performance of a model on a particular testing set, given an optimal global threshold."))
- **c7** Segment-level adjustment of the metric: if any point of a ground-truth anomaly segment is detected at a threshold, all points of that segment are counted as detected; points outside segments are treated as usual.([Performance Metrics, p.5](https://arxiv.org/pdf/1802.03903v1#page=5 "We instead use a simple strategy: if any point in an anomaly segment in the ground truth can be detected by a chosen threshold, we say this segment is detected correctly, and all points in this segment are treated as if they can be detected by this threshold."))
- **c8** Acknowledged failure mode: despite M-ELBO, missing-data injection and MCMC imputation, Donut may still fail to find a good posterior if a window contains too many anomalies; the authors argue that for long-lasting anomalies correct scores in the first few minutes suffice in their context.([Find Good Posteriors for Abnormal x, p.9](https://arxiv.org/pdf/1802.03903v1#page=9 "Despite these techniques, Donut may still fail to find a good posterior, if there are too many anomalies in x."))

