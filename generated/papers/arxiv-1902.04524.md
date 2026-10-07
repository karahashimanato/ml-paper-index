<!-- このファイルは scripts/generate.py が生成する。手で編集しない。 -->

# Bayesian Online Prediction of Change Points

- カード: [`arxiv-1902.04524`](../../papers/arxiv-1902.04524.yaml)
- 著者: Diego Agudelo-España, Sebastian Gomez-Gonzalez, Stefan Bauer, Bernhard Schölkopf, Jan Peters
- 年・掲載: 2019 UAI 2020
- 原論文: [PDF](https://arxiv.org/pdf/1902.04524v2)(arXiv v2、カード作成時に読んだ版)
- タグ: bayesian-changepoint-models, online-change-point-detection, streaming
- 人手レビュー: 未

## 主張

出典のリンクは原論文PDFの該当ページを開く。リンクにカーソルを合わせると原文の引用が表示される。

- **c1** Residual time: the posterior over the residual time (steps until the end of the current segment) is obtained by summing p(l_t | r_t) p(r_t | data) over run lengths, where p(l_t | r_t) depends only on the hazard function and can be precomputed; this assumes the observation model is independent of the residual time and the segment duration.([Residual Time Prediction for BOCPD, p.4](https://arxiv.org/pdf/1902.04524v2#page=4 "Note the assumption of independence of the observation model with respect to the residual time and the segment duration."))
- **c2** With a constant hazard the residual-time posterior equals c(1-c)^l regardless of the observations, which the authors say suggests that online prediction of changepoints is more meaningful for non-constant hazards.([Residual Time Prediction for BOCPD, p.4](https://arxiv.org/pdf/1902.04524v2#page=4 "This suggests that online prediction of CPs is more meaningful for non-constant hazard settings."))
- **c3** The hazard implicitly induces a distribution over segment durations; a constant hazard induces a geometric duration distribution (as in a standard HMM).([Section 2.2, p.2](https://arxiv.org/pdf/1902.04524v2#page=2 "induces a geometric distribution over the segment duration"))
- **c4** An HSMM with a single hidden state is an equivalent generative model to BOCPD; differences are the parameterization (total segment duration vs run length through the hazard) and inference (HSMMs mostly batch forward-backward/Viterbi, BOCPD filtering with incomplete segments).([HSMMs vs BOCPD, p.3](https://arxiv.org/pdf/1902.04524v2#page=3 "Note that an HSMM (Section 2.1) with a single hidden state K = 1 leads to an equivalent generative model for BOCPD."))
- **c5** Hyperparameters (transition matrix, duration matrix, observation-model parameters, initial state distribution) are learned by maximum likelihood from labelled sequences with marked change points, since domain knowledge is usually limited; an unsupervised EM variant is described as possible.([Section 4.4, p.5](https://arxiv.org/pdf/1902.04524v2#page=5 "We adopt a data-driven approach by using labeled observation sequences where the change point locations have been marked."))
- **c6** Cost: per-step complexity O(K^2 + D^3 K) for arbitrary underlying predictive models and O(K^2 + D^2 K) with exponential-family (sufficient-statistic) models, where K is the number of hidden states and D the maximum duration; the same O(K^2 + D^2 K) holds for duration-agnostic models, and whether exact residual-time inference can be done more efficiently is left open.([Section 4.5, p.5](https://arxiv.org/pdf/1902.04524v2#page=5 "We leave as an open question whether it is possible to achieve a more efﬁcient update to exactly infer the residual time"))
- **c7** Synthetic experiment caveat: the run-length inference has almost no uncertainty, which the authors attribute to using the actual generative models to process the synthetic observations.([Section 5.1, p.6](https://arxiv.org/pdf/1902.04524v2#page=6 "This high conﬁdence occurs as a consequence of using the actual generative models to process the synthetic observations."))
- **c8** Mice sleep staging protocol: 3 mice (2 EEG + 1 EMG channels, 24h, 4-second epochs); one mouse is the test subject and the other two with labels are used for supervised MLE; K = 3, D = 1500, with a duration-agnostic Gaussian model on frequency-band features for computational reasons. Compared with FASTER (an offline method), the authors report NREM F1 of 0.45 for FASTER versus 0.84 for their method and note that their method ran online while FASTER handled the easier offline case. How FASTER was configured was not found in the text (searched for FASTER, tune, default).([Section 5.2, p.8](https://arxiv.org/pdf/1902.04524v2#page=8 "Note that our algorithm performed online inference while FASTER considered the signiﬁcantly easier ofﬂine case."))
- **c9** Run-length inference is much more confident than residual-time inference, which the authors attribute mostly to residual time being inherently predictive whereas the run length concerns an event that has already happened.([Section 5.2, p.8](https://arxiv.org/pdf/1902.04524v2#page=8 "This is mostly due to the fact that the residual time prediction is inherently a predictive task, whereas the run length estimation accounts for an event that has already happened and from which there must be more evidence about."))

