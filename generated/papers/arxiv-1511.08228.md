<!-- このファイルは scripts/generate.py が生成する。手で編集しない。 -->

# Neural GPUs Learn Algorithms

- カード: [`arxiv-1511.08228`](../../papers/arxiv-1511.08228.yaml)
- 著者: Łukasz Kaiser, Ilya Sutskever
- 年・掲載: 2015
- 原論文: [PDF](https://arxiv.org/pdf/1511.08228v3)(arXiv v3、カード作成時に読んだ版)
- タグ: algorithm-learning, deep-learning, supervised
- 人手レビュー: 未

## 主張

出典のリンクは原論文PDFの該当ページを開く。リンクにカーソルを合わせると原文の引用が表示される。

- **c1** Contribution: the paper proposes the Neural GPU, built on a convolutional gated recurrent unit, presented as computationally universal like the Neural Turing Machine but highly parallel, which the authors say makes it easier to train and efficient to run.([Abstract, p.1](https://arxiv.org/pdf/1511.08228v3#page=1 "We present a neural network architecture to address this problem: the Neural GPU."))
- **c2** Main empirical claim (length generalization): trained on binary numbers of up to 20 bits, the Neural GPU shows no errors at test time even on much longer numbers (tasks include long binary addition and multiplication).([Abstract, p.1](https://arxiv.org/pdf/1511.08228v3#page=1 "We train the Neural GPU on numbers with up-to 20 bits and observe no errors whatsoever while testing it, even on much longer numbers."))
- **c3** Test input sizes: for binary multiplication, trained on numbers of up to 20 bits, the authors report no error on any inputs they tested, with tests on numbers up to 2000 bits long; they also say technical limits of their implementation prevented testing much above 2000 bits (Results paragraph).([Introduction, p.2](https://arxiv.org/pdf/1511.08228v3#page=2 "Trained on up-to 20-bit numbers, we see no single error on any inputs we tested, and we tested on numbers up-to 2000 bits long."))
- **c4** Success metric: Table 1 reports the fraction of test cases in which every bit of the model's output is correct (whole-sequence exact match), not per-bit accuracy.([Experiments (Table 1 caption), p.5](https://arxiv.org/pdf/1511.08228v3#page=5 "The table shows the fraction of test cases for which every single bit of the model’s output is correct."))
- **c5** Relation to sorting: one of the simpler tasks is sorting a bit sequence; the authors note that with only two symbols this is a counting task (count the 0s). For the simpler tasks of Section 3.2 the authors state that, after training on sequences of length up to 41, they found no error on any length tested (up to 4001); for duplication, however, the same section states training on inputs of up to 20 bits and testing on inputs of up to 2000 bits.([Other algorithmic tasks, p.6](https://arxiv.org/pdf/1511.08228v3#page=6 "Since there are only 2 symbols to sort, this is a counting tasks – the network must count how many 0s are in the input and produce the output accordingly, as in the example below."))
- **c6** Baseline protocol: the stack-RNN baseline was not trained with the authors' training regime but with its released source code (n_max = 41); to match the authors' procedure it was run 729 times with different seeds and the best result is reported. The LSTM+attention baseline (about 200k parameters vs about 30k for the Neural GPU) was trained with the same techniques as the Neural GPU, including curriculum training and gradient noise.([Addition and multiplication (Models), p.5](https://arxiv.org/pdf/1511.08228v3#page=5 "To match our training procedure, we ran it 729 times (cf. Section 3.3) with different random seeds and we report the best obtained result."))
- **c7** Failure modes: often only a few of the 729 grid-search models generalize to very long unseen instances (usually many generalize to 40 or even 200 bits, but only a few work without error for 2000-bit numbers); dropout and gradient noise improve reliability, and the authors suggest another technique might help more.([Discussion, p.7](https://arxiv.org/pdf/1511.08228v3#page=7 "Another problem is that often only a few models in a 729 grid search generalize to very long unseen instances."))

