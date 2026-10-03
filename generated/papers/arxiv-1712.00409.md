<!-- このファイルは scripts/generate.py が生成する。手で編集しない。 -->

# Deep Learning Scaling is Predictable, Empirically

- カード: [`arxiv-1712.00409`](../../papers/arxiv-1712.00409.yaml)
- 著者: Joel Hestness, Sharan Narang, Newsha Ardalani, Gregory Diamos, Heewoo Jun, Hassan Kianinejad, Md. Mostofa Ali Patwary, Yang Yang, Yanqi Zhou
- 年・掲載: 2017
- 原論文: [PDF](https://arxiv.org/pdf/1712.00409v1)(arXiv v1、カード作成時に読んだ版)
- タグ: deep-learning, image-classification, language-modeling, scaling-laws, supervised
- 人手レビュー: 未

## 主張

出典のリンクは原論文PDFの該当ページを開く。リンクにカーソルを合わせると原文の引用が表示される。

- **c1** Contribution: the paper presents a large-scale empirical characterization of how generalization error and model size grow as training sets grow, tested on machine translation, language modeling, image processing and speech recognition.([Abstract, p.1](https://arxiv.org/pdf/1712.00409v1#page=1 "This paper presents a large scale empirical characterization of generalization error and model size growth as training sets grow."))
- **c2** Main empirical claim: in real applications the authors find the learning-curve exponent usually settles in a range that is shallower than the exponents predicted by prior theory and is unexplained by that theory.([Introduction, p.2](https://arxiv.org/pdf/1712.00409v1#page=2 "Unfortunately, in real applications, we ﬁnd empirically that βg usually settles between −0.07 and −0.35, exponents that are unexplained by prior theoretical work."))
- **c3** Architecture vs exponent: model improvements only shift the error and do not appear to affect the power-law exponent (hedged as 'do not appear').([Abstract, p.1](https://arxiv.org/pdf/1712.00409v1#page=1 "Further, model improvements only shift the error but do not appear to affect the power-law exponent."))
- **c4** Experimental range (protocol): each training set is randomly shuffled and split into shards spanning 2-3 orders of magnitude in steps of roughly 2x, all scored on a single validation set disjoint from every shard.([Measuring model accuracy and size scaling with training data size, p.4](https://arxiv.org/pdf/1712.00409v1#page=4 "We then subdivide T into shard sizes that span 2-3 orders of magnitude in steps of roughly 2×"))
- **c5** Model size vs data: the best-fit model size grows sublinearly with training set size (equivalently, the data set grows faster than linearly with best-fit model size).([Abstract, p.1](https://arxiv.org/pdf/1712.00409v1#page=1 "We also show that model size scales sublinearly with data size."))
- **c6** Caveat: as training set sizes grow, optimization becomes harder and models run out of capacity, so the empirical error tends away from the power-law trend; the authors say a more exhaustive hyperparameter search would be needed to get closer to the trend.([Neural machine translation, p.6](https://arxiv.org/pdf/1712.00409v1#page=6 "We also note that as training set sizes grow, optimization becomes more difﬁcult and models run out of capacity, so the empirical error tends away from the power-law trend."))
- **c7** Limitation: the authors report running into compute limitations (most frequently GPU memory) for the largest data sets of each application domain.([Operational implications, p.12](https://arxiv.org/pdf/1712.00409v1#page=12 "After reviewing the tests performed for this work, we ﬁnd that we have run into compute limitations for the largest data sets of each application domain."))

