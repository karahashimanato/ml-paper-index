<!-- このファイルは scripts/generate.py が生成する。手で編集しない。 -->

# Generating Sentences from a Continuous Space

- カード: [`arxiv-1511.06349`](../../papers/arxiv-1511.06349.yaml)
- 著者: Samuel R. Bowman, Luke Vilnis, Oriol Vinyals, Andrew M. Dai, Rafal Jozefowicz, Samy Bengio
- 年・掲載: 2015 CoNLL 2016
- 原論文: [PDF](https://arxiv.org/pdf/1511.06349v4)(arXiv v4、カード作成時に読んだ版)
- タグ: generative-modeling, language-modeling, representation-learning, unsupervised, variational-autoencoders
- 人手レビュー: 未

## 主張

出典のリンクは原論文PDFの該当ページを開く。リンクにカーソルを合わせると原文の引用が表示される。

- **c1** Motivating observation: decoding points on a path between two sentence encodings of a conventional (sequence) autoencoder gives intermediate sentences that are generally ungrammatical (Table 1), which the authors take to suggest that standard autoencoders do not learn a smooth, interpretable sentence feature space.([Background, p.2](https://arxiv.org/pdf/1511.06349v4#page=2 "Standard autoencoders are not eﬀective at extracting for global semantic features."))
- **c2** Optimization failure (posterior collapse): straightforward implementations fail to encode information in the latent variable; except in vanishingly rare cases, most training runs with most hyperparameters set the approximate posterior equal to the prior, bringing the KL term to zero, and the model then behaves as an RNN language model.([Optimization challenges, p.3](https://arxiv.org/pdf/1511.06349v4#page=3 "Straightforward implementations of our vae fail to learn this behavior"))
- **c3** Proposed mechanism: the LSTM decoder is sensitive to small variations in the hidden state, so the model first learns to ignore the latent code; afterwards the decoder ignores the encoder and little gradient passes between them, an undesirable stable equilibrium with the KL term at zero.([Optimization challenges, p.3](https://arxiv.org/pdf/1511.06349v4#page=3 "Once this has happened, the decoder ignores the encoder and little to no gradient signal passes between the two, yielding an undesirable stable equilibrium with the kl cost term at zero."))
- **c4** KL cost annealing: the weight on the KL term starts at zero and is gradually increased to 1, so the true lower bound is not optimized early in training; the authors describe it as annealing from a vanilla autoencoder to a VAE, with the rate tuned as a hyperparameter.([KL cost annealing, p.4](https://arxiv.org/pdf/1511.06349v4#page=4 "This can be thought of as annealing from a vanilla autoencoder to a vae."))
- **c5** Word dropout: replacing a fraction of the conditioned-on previous words with an unknown-word token weakens the decoder and forces it to rely on the latent variable; standard dropout on decoder input embeddings did not help the model use the latent variable.([Word dropout and historyless decoding, p.4](https://arxiv.org/pdf/1511.06349v4#page=4 "This forces the model to rely on the latent variable"))
- **c6** Without both word dropout and KL annealing, training in the standard setting reliably gives models equivalent to the baseline RNN language model with zero KL divergence.([Results: Language modeling, p.4](https://arxiv.org/pdf/1511.06349v4#page=4 "Training a vae in the standard setting without both word dropout and cost annealing reliably results in models with equivalent performance to the baseline rnnlm, and zero kl divergence."))
- **c7** Evaluation caveats on Penn Treebank language modelling: the VAE hyperparameter search was restricted to models encoding a non-trivial amount in the latent variable, and the VAE is reported with a variational lower bound while the RNNLM is reported with its exact likelihood, which the authors note puts the VAE at a potential disadvantage. In the standard setting the VAE performs slightly worse than the RNNLM.([Results: Language modeling, p.4](https://arxiv.org/pdf/1511.06349v4#page=4 "This discrepancy puts the vae at a potential disadvantage."))
- **c8** Even with these techniques the authors could not train models in which the KL term dominates the reconstruction term, which they take to suggest that it is substantially easier to model the data with local statistics, so the encoder only encodes what those statistics cannot describe.([Results: Language modeling, p.5](https://arxiv.org/pdf/1511.06349v4#page=5 "This suggests that it is still substantially easier to learn to factor the data distribution using simple local statistics"))

