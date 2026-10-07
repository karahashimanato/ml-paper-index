<!-- このファイルは scripts/generate.py が生成する。手で編集しない。 -->

# Active multi-fidelity Bayesian online changepoint detection

- カード: [`arxiv-2103.14224`](../../papers/arxiv-2103.14224.yaml)
- 著者: Gregory W. Gundersen, Diana Cai, Chuteng Zhou, Barbara E. Engelhardt, Ryan P. Adams
- 年・掲載: 2021 UAI 2021
- 原論文: [PDF](https://arxiv.org/pdf/2103.14224v2)(arXiv v2、カード作成時に読んだ版)
- タグ: bayesian-changepoint-models, online-change-point-detection, streaming
- 人手レビュー: 未

## 主張

出典のリンクは原論文PDFの該当ページを開く。リンクにカーソルを合わせると原文の引用が表示される。

- **c1** BOCD model used: changepoints arrive as a discrete-time Bernoulli process with constant hazard 1/β (geometric partition lengths with mean β); data within a partition are i.i.d. with partition-specific parameters drawn afresh from a prior at a changepoint.([Bayesian Online Changepoint Detection, p.2](https://arxiv.org/pdf/2103.14224v2#page=2 "We model the arrival of changepoints as a discrete time Bernoulli process with hazard rate 1/β"))
- **c2** Motivation: BOCD can be viewed as a model-based exponentially weighted moving average whose weights are estimated from data; when posterior confidence about changepoints is high there is no need for expensive high-fidelity observations.([Introduction, p.2](https://arxiv.org/pdf/2103.14224v2#page=2 "as a model-based version of an exponentially-weighted moving average, estimating the weights from data rather than selecting them a priori."))
- **c3** Multi-fidelity posterior: each observation's likelihood is raised to its fidelity ζ in [0, 1], which down-weights its sufficient statistics; the paper only considers exponential-family models because this often allows efficient online updates (non-conjugate cases would need approximations).([Multi-Fidelity Posterior Predictive, p.4](https://arxiv.org/pdf/2103.14224v2#page=4 "In this paper, we only consider models in the exponential family, since this restriction often allows for efﬁcient online updates."))
- **c4** Decision rule: choose the fidelity maximizing a weighted information rate w(ζ) U(ζ) / λ(ζ), where U is the expected reduction in run-length entropy and λ a known scalar cost; the weights can be tuned on held-out data to achieve a desired budget.([Section 3.4, p.5](https://arxiv.org/pdf/2103.14224v2#page=5 "Note that the weights can be tuned on held-out data to achieve a desired expected budget."))
- **c5** An alternative rule (pick low fidelity when the information gains differ by less than a margin) resulted empirically in frequent switching, because the two gains were often close; the information rate was more stable.([Section 3.4, p.6](https://arxiv.org/pdf/2103.14224v2#page=6 "However, empirically, this resulted in frequent switching between ﬁdelities since the two information gains were often quite close in value."))
- **c6** Cost of deciding: computing the information gain sums over the run-length posterior, so its cost grows linearly with time (32t + 1 flops for the beta-Bernoulli model); with Fearnhead and Liu's resampling the cost is fixed, e.g. 0.32 million flops with 10,000 particles, compared with 82 million flops for the smallest reported MobileNet.([Practical Considerations, p.6](https://arxiv.org/pdf/2103.14224v2#page=6 "The cost grows linearly with time because computing information gain requires summing over the run length posterior"))
- **c7** Evaluation metrics are relative, not to ground truth: MSE of the predictive mean and L1 distance of the run-length posterior are computed against BOCD using only high-fidelity data; baselines are low-fidelity-only BOCD and random fidelity switching with roughly the same high-fidelity fraction.([Experiments, p.6](https://arxiv.org/pdf/2103.14224v2#page=6 "In other words, we compare the evaluated model to the best it could have done in practice."))
- **c8** CamVid protocol: pretrained MobileNetV3 large/small segmentation models give a binary 'fence' signal fitted with the multi-fidelity Bernoulli model; costs are set from flops and the low fidelity from the IoU difference; the decision-rule weights were tuned on cross-validation data to approximately 50% low-fidelity usage, and the random baseline flips a fair coin.([Section 4.2, p.7](https://arxiv.org/pdf/2103.14224v2#page=7 "The multi-ﬁdelity model’s decision rule weights were tuned to approximate total computational cost of 50% low-ﬁdelity data using cross-validation data, and the randomized approach ﬂips a fair coin to choose the data ﬁdelity."))
- **c9** Negative result on MIMII (synthetic changepoint sequences built by sampling normal/anomalous audio clips, 500 datasets per machine): MF-BOCD is not significantly better than random switching on machine 4, which the authors hypothesize is due to the poor low-fidelity model (AUC < 0.5); they note a randomized approach can sometimes do well.([MIMII Audio Data, p.8](https://arxiv.org/pdf/2103.14224v2#page=8 "An interesting negative result is that MF-BOCD does not do signiﬁcantly better than random on machine 4."))

