---
title: グラフニューラルネットワーク — メッセージパッシングの基本、表現力の上限、深さの問題、異質なグラフ、評価の落とし穴
kind: method
tags: [graph-neural-networks]
depends_on: [arxiv-1609.02907, arxiv-1706.02216, arxiv-1710.10903, arxiv-1902.07153, arxiv-1810.00826, arxiv-1704.01212, arxiv-1801.07606, arxiv-1905.10947, arxiv-2006.05205, arxiv-1811.05868, arxiv-1912.09893, arxiv-2006.11468, arxiv-2302.11640, arxiv-2005.00687, arxiv-2003.00982, arxiv-2206.08164]
written_at: 2026-10-10
written_by: claude-opus-5-5 via Claude Code
---

# グラフニューラルネットワーク — メッセージパッシングの基本、表現力の上限、深さの問題、異質なグラフ、評価の落とし穴

<!-- generated:stale -->
> ⚠ この記事の執筆後(2026-10-10)に、関連カードが 24 件追加されています(未反映): `arxiv-1611.02401`, `arxiv-1704.01665`, `arxiv-1803.08475`, `arxiv-1810.10659`, `arxiv-1905.13211`, `arxiv-1906.01629`, `arxiv-1910.10593`, `arxiv-2004.01608`, `arxiv-2006.07054`, `arxiv-2012.10658`, `arxiv-2012.13349`, `arxiv-2102.11756`, `arxiv-2107.10201`, `arxiv-2201.10494`, `arxiv-2203.15544`, `arxiv-2205.15659`, `arxiv-2206.13211`, `arxiv-2608.11431`, `arxiv-2609.05955`, `arxiv-2609.12712`, `arxiv-2609.26855`, `arxiv-2609.35703`, `arxiv-2609.36302`, `arxiv-2609.37057`
<!-- /generated:stale -->

## この記事の読み方

**グラフニューラルネットワーク**(GNN)は、ノード(頂点)とエッジ(辺)からなるグラフを入力とするニューラルネットワークである。各ノードが隣のノードから情報を集めて自分の表現を更新する、という操作を繰り返す。
タスクは主に、ノードごとの分類(論文の引用ネットワークで各論文の分野を当てる、など)と、グラフ全体の分類・回帰(分子の性質を当てる、など)に分かれる。

この記事は16本の新しいカードから、次の5点を整理する。

1. 基本の層:GCN、メッセージパッシングの枠組み、GraphSAGE、GAT、SGC
2. 表現力の上限:WL 検定との関係
3. 深くするとうまくいかない理由:過平滑化と過圧縮
4. 隣どうしのラベルが違うグラフ(異質性)
5. 評価の落とし穴とベンチマーク

性能の数値は書かない。各論文のページの結果表を参照のこと(カードは結果表を記録せず、主張だけを記録している)。
組合せ最適化やアルゴリズムの学習に GNN を使う研究は、[アルゴリズムと機械学習](../topics/algorithms-and-ml.md) の記事で扱った。

## 1. 基本の層

### GCN

Kipf と Welling の GCN は、次の層の規則を使う [arxiv-1609.02907#c1](https://arxiv.org/pdf/1609.02907v4#page=2 "We consider a multi-layer Graph Convolutional Network (GCN) with the following layer-wise propagation rule:")。

$$
H^{(l+1)} = \sigma\!\left( \tilde{D}^{-1/2} \tilde{A} \tilde{D}^{-1/2} H^{(l)} W^{(l)} \right), \qquad \tilde{A} = A + I
$$

$A$ はグラフの隣接行列で、$I$ を足して各ノードに自分自身へのループを加える。$\tilde{D}$ は $\tilde{A}$ の次数(各ノードのつながりの数)を並べた対角行列で、両側から $\tilde{D}^{-1/2}$ を掛けて正規化する。つまり「自分と隣のノードの特徴を、次数で重み付けして平均し、重み $W$ を掛ける」操作である。

この形は、グラフのスペクトル(ラプラシアンの固有値)の上で定義した畳み込みを近似して導かれた [arxiv-1609.02907#c2](https://arxiv.org/pdf/1609.02907v4#page=2 "Note that this expression is now K-localized since it is a Kth-order polynomial in the Laplacian, i.e. it depends only on nodes that are at maximum K steps away from the central node (Kth-order neighborhood).")。近似を1次で打ち切り、パラメータを1つにまとめ [arxiv-1609.02907#c3](https://arxiv.org/pdf/1609.02907v4#page=3 "In this linear formulation of a GCN we further approximate λmax ≈2, as we can expect that neural network parameters will adapt to this change in scale during training.")、さらに数値の不安定さを避けるために自分自身へのループを入れて正規化し直した(再正規化の工夫)[arxiv-1609.02907#c4](https://arxiv.org/pdf/1609.02907v4#page=3 "Repeated application of this operator can therefore lead to numerical instabilities and exploding/vanishing gradients when used in a deep neural network model.")。

論文は、全データを一度に使う学習のためメモリがデータの大きさに比例すること、エッジの特徴を自然には扱えず無向グラフに限られること、自分と隣を同じ重みで扱う前提があることを、限界として挙げている [arxiv-1609.02907#c8](https://arxiv.org/pdf/1609.02907v4#page=8 "Through the approximations introduced in Section 2, we implicitly assume locality (dependence on the Kth-order neighborhood for a GCN with K layers) and equal importance of self-connections vs. edges to neighboring nodes.")。

### メッセージパッシングの枠組み

Gilmer らは、多くの GNN を**メッセージパッシング**という共通の枠組みで書き直した [arxiv-1704.01212#c1](https://arxiv.org/pdf/1704.01212v2#page=3 "R operates on the set of node states and must be invariant to permutations of the node states in order for the MPNN to be invariant to graph isomorphism.")。

1. 各ノードが、隣のノードから**メッセージ**を受け取って足し合わせる(メッセージ関数)。
2. 受け取ったメッセージと自分の状態から、状態を**更新**する(更新関数)。
3. これを $T$ 回繰り返した後、全ノードの状態からグラフ全体の表現を**読み出す**(読み出し関数)。読み出しはノードの並べ方によらない必要がある。

彼らは少なくとも8つの既存モデルをこの形で表し、GCN もその1つとして書いている [arxiv-1704.01212#c2](https://arxiv.org/pdf/1704.01212v2#page=2 "There are at least eight notable examples of models from the literature that we can describe using our Message Passing Neural Networks (MPNN) framework.")。

### GraphSAGE:学習時に見ていないノードへの一般化

従来のノードの埋め込み手法の多くは、すべてのノードが学習時にそろっている必要があり(**トランスダクティブ**)、新しいノードには使えなかった。GraphSAGE は、近傍から特徴を集める**関数**を学習することで、学習時に見ていないノードにも使えるようにした(**インダクティブ**)[arxiv-1706.02216#c1](https://arxiv.org/pdf/1706.02216v4#page=1 "However, most existing approaches require that all nodes in the graph are present during training of the embeddings; these previous approaches are inherently transductive and do not naturally generalize to unseen nodes.")。

- 各段で、隣のノードの表現を1つにまとめ(集約)、自分の表現とつなげて全結合層に通す [arxiv-1706.02216#c2](https://arxiv.org/pdf/1706.02216v4#page=4 "The intuition behind Algorithm 1 is that at each iteration, or search depth, nodes aggregate information from their local neighbors, and as this process iterates, nodes incrementally gain more and more information from further reaches of the graph.")。
- 隣を全部使う代わりに、決まった数だけランダムに選ぶ。これで1バッチの計算量が一定になる [arxiv-1706.02216#c4](https://arxiv.org/pdf/1706.02216v4#page=5 "Without this sampling the memory and expected runtime of a single batch is unpredictable and in the worst case O(/V/).")。
- 集約には平均、最大値プーリングなどを使う。平均の集約は GCN の規則とほぼ同じになる [arxiv-1706.02216#c5](https://arxiv.org/pdf/1706.02216v4#page=5 "The mean aggregator is nearly equivalent to the convolutional propagation rule used in the transductive GCN framework [17].") [arxiv-1706.02216#c6](https://arxiv.org/pdf/1706.02216v4#page=6 "The ﬁnal aggregator we examine is both symmetric and trainable.")。

### GAT:隣ごとに重みを変える

GAT は、隣のノードごとに**注意の重み**を計算して、重み付きで集める。注意は隣とのペアから計算し、隣接するノードだけに限って正規化する [arxiv-1710.10903#c1](https://arxiv.org/pdf/1710.10903v3#page=3 "We inject the graph structure into the mechanism by performing masked attention—we only compute eij for nodes j ∈Ni, where Ni is some neighborhood of node i in the graph.")。複数の注意を並べる多頭注意も使う [arxiv-1710.10903#c2](https://arxiv.org/pdf/1710.10903v3#page=4 "To stabilize the learning process of self-attention, we have found extending our mechanism to employ multi-head attention to be beneﬁcial, similarly to Vaswani et al. (2017).")。
注意はすべてのエッジで共有されるので、グラフ全体を前もって知る必要がなく、学習時に見ていないグラフにも使える [arxiv-1710.10903#c4](https://arxiv.org/pdf/1710.10903v3#page=5 "The attention mechanism is applied in a shared manner to all edges in the graph, and therefore it does not depend on upfront access to the global graph structure or (features of) all of its nodes (a limitation of many prior techniques).")。GraphSAGE が隣を一部だけ選ぶのに対し、GAT は隣を全部使う代わりに計算量が変わりうる [arxiv-1710.10903#c5](https://arxiv.org/pdf/1710.10903v3#page=5 "Our technique does not suffer from either of these issues—it works with the entirety of the neighborhood (at the expense of a variable computational footprint, which is still on-par with methods like the GCN), and does not assume any ordering within it.")。

### SGC:非線形をなくしても働くか

Wu らは、GCN の層の間の非線形関数は重要ではなく、効果のほとんどは隣との平均(局所的な平均化)から来る、という仮説を立てた。非線形をすべて取り除くと、モデルは「正規化した隣接行列を $K$ 回掛けて特徴をなめらかにし、ロジスティック回帰で分類する」だけになる [arxiv-1902.07153#c1](https://arxiv.org/pdf/1902.07153v2#page=3 "We hypothesize that the nonlinearity between GCN layers is not critical - but that the majority of the beneﬁt arises from the local averaging.") [arxiv-1902.07153#c2](https://arxiv.org/pdf/1902.07153v2#page=3 "SGC consists of a ﬁxed (i.e., parameter-free) feature extraction/smoothing component")。
スペクトルの見方では、自分自身へのループを加えると、この操作は**低域通過フィルタ**(なめらかな成分だけを通す)として働く [arxiv-1902.07153#c4](https://arxiv.org/pdf/1902.07153v2#page=5 "the largest eigenvalue shrinks from 2 to approximately 1.5 and then eliminates the effect of negative coefﬁcients")。
著者らは、GCN の表現力は主に繰り返しの伝播から来ている可能性が高いと結論し、SGC をまず試すべき単純なベースラインとして勧めている [arxiv-1902.07153#c9](https://arxiv.org/pdf/1902.07153v2#page=8 "It is likely that the expressive power of GCNs originates primarily from the repeated graph propagation (which SGC preserves) rather than the nonlinear feature extraction (which it doesn’t.)")。一方、グラフ分類では、より表現力の高いモデルに大きく及ばなかった [arxiv-1902.07153#c7](https://arxiv.org/pdf/1902.07153v2#page=8 "We replace the GCN in DCGCN (Zhang et al., 2018b) with an SGC and get 71.0% and 76.2% on NCI1 and COLLAB datasets (Yanardag & Vishwanathan, 2015) respectively, which is on par with an GCN counterpart, but far behind GIN.")。

## 2. 表現力の上限:WL 検定

**WL 検定**(Weisfeiler-Lehman 検定)は、2つのグラフが同じ形(同型)かどうかを見分ける古典的な手続きで、各ノードのラベルを、隣のラベルの集まりから繰り返し更新する。GraphSAGE の論文も、自分のアルゴリズムが WL 検定の一種と見なせることを指摘している [arxiv-1706.02216#c3](https://arxiv.org/pdf/1706.02216v4#page=4 "GraphSAGE is a continuous approximation to the WL test, where we replace the hash function with trainable neural network aggregators.")。

Xu らは、隣から集めて更新する GNN は、グラフを見分ける力において**WL 検定を超えない**ことを示した [arxiv-1810.00826#c1](https://arxiv.org/pdf/1810.00826v3#page=4 "Hence, any aggregation-based GNN is at most as powerful as the WL test in distinguishing different graphs.")。逆に、集約・更新・読み出しが**単射**(違う入力を違う出力に写す)なら WL 検定と同じ力を持つ [arxiv-1810.00826#c2](https://arxiv.org/pdf/1810.00826v3#page=4 "if the neighbor aggregation and graph-level readout functions are injective, then the resulting GNN is as powerful as the WL test.")。

- 隣の集まりは、同じ値が何度も出てくる**多重集合**である。和による集約は多重集合を見分けられるが、平均や最大値は見分けられない [arxiv-1810.00826#c4](https://arxiv.org/pdf/1810.00826v3#page=5 "Our next lemma states that sum aggregators can represent injective, in fact, universal functions over multisets.") [arxiv-1810.00826#c7](https://arxiv.org/pdf/1810.00826v3#page=7 "Mean and max-pooling aggregators are still well-deﬁned multiset functions because they are permutation invariant.")。
- この考えから、和で集めて多層パーセプトロンで更新する **GIN** を提案した [arxiv-1810.00826#c4](https://arxiv.org/pdf/1810.00826v3#page=5 "Our next lemma states that sum aggregators can represent injective, in fact, universal functions over multisets.")。
- 平均は多重集合の「割合」を、最大値は「どんな値があるか」だけを捉える。著者らは、ノードの特徴が豊かで重複が少ないノード分類では、平均の集約でも十分働くことの説明になるかもしれない、と述べている [arxiv-1810.00826#c8](https://arxiv.org/pdf/1810.00826v3#page=7 "Moreover, when node features are diverse and rarely repeat, the mean aggregator is as powerful as the sum aggregator.")。
- 解析は、ノードの特徴が可算集合から来ることを前提にしている。連続値の特徴は今後の課題とされている [arxiv-1810.00826#c3](https://arxiv.org/pdf/1810.00826v3#page=4 "Uncountable sets, where node features are continuous, need some further considerations.")。

## 3. 深くするとうまくいかない理由

GCN の論文の付録でも、層を深くすると残差接続なしでは学習が難しくなると報告されている [arxiv-1609.02907#c9](https://arxiv.org/pdf/1609.02907v4#page=14 "We observe that for models deeper than 7 layers, training without the use of residual connections can become difﬁcult, as the effective context size for each node increases by the size of its Kth-order neighborhood (for a model with K layers) with each additional layer.")。その理由として、2つの現象が論じられてきた。

### 過平滑化

Li らは、GCN のグラフ畳み込みは**ラプラシアン平滑化**(各ノードの値を隣との平均に近づける操作)の一種だと示した [arxiv-1801.07606#c2](https://arxiv.org/pdf/1801.07606v1#page=4 "We thus call the graph convolution a special form of Laplacian smoothing – symmetric Laplacian smoothing.")。平滑化によって、同じクラスタのノードの特徴が似てくるので、分類しやすくなる [arxiv-1801.07606#c3](https://arxiv.org/pdf/1801.07606v1#page=3 "Surprisingly, even a one-layer GCN outperformed a one-layer FCN by a very large margin.")。
しかし平滑化を何度も繰り返すと、異なるクラスタの特徴まで混ざってしまう(**過平滑化**)[arxiv-1801.07606#c4](https://arxiv.org/pdf/1801.07606v1#page=4 "On the other hand, repeatedly applying Laplacian smoothing may mix the features of vertices from different clusters and make them indistinguishable.")。論文の定理1は、二部グラフの成分がないなどの仮定のもとで、繰り返した平滑化が連結成分ごとに一定のベクトルに収束することを示す [arxiv-1801.07606#c5](https://arxiv.org/pdf/1801.07606v1#page=5 "Based on the above theorem, over-smoothing will make the features indistinguishable and hurt the classiﬁcation accuracy.")。
ただし、著者ら自身の実験では、層を増やしたときの精度の低下は、過平滑化よりも過学習による「可能性が高い」と述べている [arxiv-1801.07606#c9](https://arxiv.org/pdf/1801.07606v1#page=7 "When the number of convolutional layers grows, the classiﬁcation accuracy decreases drastically, which is probably due to overﬁtting.")。

Oono と Suzuki は、これを一般化し、一定の条件のもとで GCN の表現は層を重ねると指数的に情報を失い、連結成分と次数の情報しか残らない部分空間に近づくことを示した [arxiv-1905.10947#c2](https://arxiv.org/pdf/1905.10947v5#page=4 "We use the non-negativity of em to prove this claim.") [arxiv-1905.10947#c3](https://arxiv.org/pdf/1905.10947v5#page=5 "In this sense, M only has information about connected components and node degrees and we can interpret this theorem as the exponential information loss of GCNs in terms of the layer size.")。
ただし、著者らは、現実のグラフは疎なことが多いので、この定理が当てはまる GCN は限られていると認めている [arxiv-1905.10947#c6](https://arxiv.org/pdf/1905.10947v5#page=8 "However, real-world graphs are not often dense, which means that Theorem 2 is applicable to very limited GCNs.")。

### 過圧縮

Alon と Yahav は、遠いノードの情報が必要な問題では、別の現象が問題になると指摘した。問題に必要な距離(半径)が $r$ なら、少なくとも $r$ 層が必要だが、$r$ 歩以内のノードの数は指数的に増える。その情報を固定長のベクトルに押し込むので、情報が失われる(**過圧縮**)[arxiv-2006.05205#c1](https://arxiv.org/pdf/2006.05205v4#page=3 "When a prediction problem relies on long-range interaction between nodes, the GNN must have as many layers K as the estimated range of these interactions, or otherwise, these distant nodes would not be able to interact.")。
彼らは、長距離の問題で性能が落ちるのは、過平滑化より過圧縮によるという仮説を立てている [arxiv-2006.05205#c8](https://arxiv.org/pdf/2006.05205v4#page=9 "We hypothesize that in long-range problems, the explanation for the degraded performance is over-squashing rather than over-smoothing.")。合成したタスクでは、すべての隣を集めてから自分と組み合わせるモデルは、注意で選ぶモデルより早く失敗した [arxiv-2006.05205#c3](https://arxiv.org/pdf/2006.05205v4#page=5 "GCN and GIN managed to perfectly ﬁt r=3 at most, while GGNN and GAT also reached 100% accuracy at r=4.")。

Gilmer らも、すべてのノードにつながる仮想のノードを加えると、長距離の相互作用を捉えるのに役立つと報告している [arxiv-1704.01212#c5](https://arxiv.org/pdf/1704.01212v2#page=8 "Moreover, our results also reveal the importance of allowing long range interactions between nodes in the graph with either the master node or the set2set output.")。

長距離の依存を評価するために作られた **LRGB** は、既存のベンチマークの多くは局所的な構造で解けてしまうと指摘している [arxiv-2206.08164#c1](https://arxiv.org/pdf/2206.08164v4#page=2 "Consequently, such GNNs fail at capturing long-range dependencies as a significant amount of distant information may get lost due to the squashing.") [arxiv-2206.08164#c2](https://arxiv.org/pdf/2206.08164v4#page=2 "However, it is often the case that these models are evaluated on datasets where the corresponding tasks primarily rely on local structural information rather than the distant information propagation between nodes.")。LRGB の実験では、単純なメッセージパッシングの GNN は多くのデータセットで振るわず、全ノードをつなぐ Transformer が上位に入った [arxiv-2206.08164#c7](https://arxiv.org/pdf/2206.08164v4#page=9 "This is consistent with the empirical findings in [2] where GCN and GIN suffer from over-squashing to a greater extent than GAT, an attention based MP-GNN [60].") [arxiv-2206.08164#c8](https://arxiv.org/pdf/2206.08164v4#page=10 "First, the use of positional encoding alone contributes to little or no gain in performance on the proposed datasets.")。ただし、最新版の論文は、元のベースラインを見直した後続研究(Tönshoff ら)を参照するよう注記している [arxiv-2206.08164#c9](https://arxiv.org/pdf/2206.08164v4#page=8 "For a reassessment of the original baselines on all the datasets as well as extensions of PCQM-Contact’s metric, we refer to the paper [58] by Tönshoff et al., 2023.")。

## 4. 隣どうしのラベルが違うグラフ(異質性)

GCN などは、「つながったノードは同じクラスになりやすい」(**同質性**)を暗に前提にしている。Zhu らは、同じクラスどうしをつなぐエッジの割合を**エッジ同質性** $h$ と定義した [arxiv-2006.11468#c1](https://arxiv.org/pdf/2006.11468v2#page=2 "is the fraction of edges in a graph which connect nodes that have the same class label (i.e., intra-class edges).")。

- 同質性の低い合成グラフでは、調べた既存の GNN はどれも、グラフを使わない MLP に勝てなかった [arxiv-2006.11468#c2](https://arxiv.org/pdf/2006.11468v2#page=3 "Especially, GCN [17] and GAT [36] show up to 42% worse performance than MLP, highlighting that methods that work well under high homophily (h = 0.7) may not be appropriate for networks with low/medium homophily.")。
- 直接の隣が異質でも、2歩先の隣は同質になりやすいことを、仮定付きで示している [arxiv-2006.11468#c4](https://arxiv.org/pdf/2006.11468v2#page=4 "In the case of heterophily, we have seen empirically that although the immediate neighborhoods may be heterophily-dominant, the higher-order neighborhoods may be homophily-dominant and thus provide more relevant context.")。
- この分析から、自分の表現と隣の表現を分けて扱う、2歩先の隣も集める、途中の層の表現を組み合わせる、という設計を提案した(H2GCN)[arxiv-2006.11468#c6](https://arxiv.org/pdf/2006.11468v2#page=6 "We found that removing the usual nonlinear transformations per round, as in SGC [37], works better (App. D.2), in which case we only need to include the ego-embedding in the ﬁnal representation.")。

その後、Platonov らは、異質性の評価に使われてきた標準のデータセットそのものに問題があると指摘した。

- squirrel と chameleon には、同じ目標値と同じ近傍を持つ重複したノードが多く、学習データとテストデータの間で情報が漏れている [arxiv-2302.11640#c2](https://arxiv.org/pdf/2302.11640v2#page=4 "Since duplicates from the same group appear in the train, validation, and test parts of the datasets, they create a train-test data leakage:")。重複を除くと多くのモデルの性能が下がり、順位も大きく入れ替わった [arxiv-2302.11640#c4](https://arxiv.org/pdf/2302.11640v2#page=5 "Such a substantial shake-up raises concerns about the validity of conclusions made in previous works that rely on analyzing the performance of different models on these datasets.")。
- 他の3つのデータセットはとても小さく、クラスの偏りも強いので、結果が不安定になりうる [arxiv-2302.11640#c5](https://arxiv.org/pdf/2302.11640v2#page=5 "We ﬁrst note that these datasets are very small (183-251 nodes and 295-499 edges), which can lead to unstable and statistically insigniﬁcant results.")。
- 新しいデータセットでは、異質性向けの専用モデルより、標準的な GNN がほとんどの場合よかった [arxiv-2302.11640#c8](https://arxiv.org/pdf/2302.11640v2#page=9 "Among 15 of the top-3 performances on our 5 datasets, 13 belong to standard GNNs.")。自分と隣の表現を分けることは効果があった [arxiv-2302.11640#c9](https://arxiv.org/pdf/2302.11640v2#page=9 "GAT-sep and GT-sep typically outperform their versions without embedding separation, which shows that this trick proposed in Zhu et al. (2020) is indeed helpful for learning under heterophily.")。
- なお、ベースラインは層の数だけを調整し、専用モデルはより多くのハイパーパラメータを調整している [arxiv-2302.11640#c7](https://arxiv.org/pdf/2302.11640v2#page=14 "Further, we found that they make our baseline models quite robust to the selection of hyperparameter values, so the only hyperparameter that we tune for them is the number of graph neighborhood aggregation layers.")。

## 5. 評価の落とし穴とベンチマーク

### 固定の分割と、そろわない学習手順

Shchur らは、多くのモデルが Cora などの同じ固定の分割だけで評価されていること、新しいモデルがベースラインと違う手順で学習されていることを批判した [arxiv-1811.05868#c1](https://arxiv.org/pdf/1811.05868v2#page=1 "Such experimental setup favors the model that overﬁts the most and defeats the main purpose of using a train/validation/test split — ﬁnding the model with the best generalization properties [Friedman et al., 2001].")。

- 同じ学習手順と同じハイパーパラメータ探索で、多数のランダムな分割と初期化で比べると [arxiv-1811.05868#c3](https://arxiv.org/pdf/1811.05868v2#page=3 "In all cases, we use 20 labeled nodes per class as the training set, 30 nodes per class as the validation set, and the rest as the test set.")、GNN はグラフを使わないベースラインには勝つが、GNN の間に明確な勝者はいなかった [arxiv-1811.05868#c5](https://arxiv.org/pdf/1811.05868v2#page=3 "Among the GNN approaches, there is no clear winner that dominates across all the datasets.")。平均すると最も単純な GCN が最もよかった [arxiv-1811.05868#c6](https://arxiv.org/pdf/1811.05868v2#page=4 "We observe that GCN is able to achieve the best performance across all models.")。
- 固定の分割と別のランダムな分割では、モデルの順位が入れ替わった。著者らは、1つの分割の結果はもろく、誤解を招くと結論している [arxiv-1811.05868#c7](https://arxiv.org/pdf/1811.05868v2#page=4 "This shows how fragile and misleading results obtained on a single split can be.")。

Li らも、GCN の評価で使われる検証用のラベルが学習用より多く、半教師あり学習の前提に合わないと指摘している [arxiv-1801.07606#c7](https://arxiv.org/pdf/1801.07606v1#page=5 "Furthermore, it makes the comparison of GCNs with other methods unfair as other methods such as label propagation may not need the validation data at all.")。

### モデル選択と性能評価を分ける

Errica らは、グラフ分類の比較で、ハイパーパラメータを選ぶ**モデル選択**と、選んだモデルの性能を測る**リスク評価**を分けることが重要だと強調した [arxiv-1912.09893#c1](https://arxiv.org/pdf/1912.09893v3#page=3 "This way, test data is never used for model selection.") [arxiv-1912.09893#c2](https://arxiv.org/pdf/1912.09893v3#page=3 "Consequently, model selection results are generally over-optimistic; this issue is thoroughly documented in Cawley & Talbot (2010).")。

- 見直した論文の中には、テストデータでなく交差検証の検証データの精度を報告しているものがあった。GIN の論文もその1つである [arxiv-1912.09893#c3](https://arxiv.org/pdf/1912.09893v3#page=4 "In other words, reported results refer to model selection and not to model evaluation.") [arxiv-1810.00826#c9](https://arxiv.org/pdf/1810.00826v3#page=9 "We report the average and standard deviation of validation accuracies across the 10 folds within the cross-validation.")。
- グラフの構造を使わないベースラインを置くと、いくつかのデータセットでは、どの GNN もそのベースラインを上回らなかった [arxiv-1912.09893#c7](https://arxiv.org/pdf/1912.09893v3#page=7 "Importantly, we discover that on D&D, PROTEINS and ENZYMES none of the GNNs are able to improve over the baseline.")。著者らは、ベースラインに近い性能なら、そのタスクに構造が要らないか、GNN が構造をうまく使えていないかのどちらかだと述べている [arxiv-1912.09893#c6](https://arxiv.org/pdf/1912.09893v3#page=5 "As a matter of fact, if GNN performances are close to the ones of a structure-agnostic baseline, one can draw two possible conclusions: the task does not need topological information to be effectively solved, or the GNN is not exploiting graph structure adequately.")。

### ベンチマーク

- **OGB** は、既存のデータセットが小さすぎ、統一された評価の手順もないと批判した [arxiv-2005.00687#c1](https://arxiv.org/pdf/2005.00687v7#page=2 "Most of the frequently-used graph datasets are extremely small compared to graphs found in real applications (with more than 1 million nodes or 100 thousand graphs)") [arxiv-2005.00687#c2](https://arxiv.org/pdf/2005.00687v7#page=3 "Furthermore, there is no uniﬁed and commonly-followed experimental protocol.")。小さい部類でもノードが10万を超える規模にし [arxiv-2005.00687#c4](https://arxiv.org/pdf/2005.00687v7#page=3 "Even the “small” OGB graphs have more than 100 thousand nodes or more than 1 million edges, but are small enough to ﬁt into the memory of a single GPU, making them suitable for testing computationally intensive algorithms.")、時間や分子の骨格に基づく現実的な分割を用意した [arxiv-2005.00687#c5](https://arxiv.org/pdf/2005.00687v7#page=11 "Speciﬁcally, we propose to train on papers published until 2017, validate on those published in 2018, and test on those published since 2019.")。同じ割合でもランダムな分割のほうが一貫して易しかった [arxiv-2005.00687#c7](https://arxiv.org/pdf/2005.00687v7#page=22 "We ﬁnd the random split to be much easier than scaffold split.")。
- **Benchmarking GNNs** は、パラメータ数の予算(主に100k)をそろえて比べる枠組みである [arxiv-2003.00982#c2](https://arxiv.org/pdf/2003.00982v5#page=3 "In the absence of such design choice, it is comparatively diﬃcult to conclude whether a better performing model’s gain arises from its architectural design or extra learning capacity brought by additional model parameters.")。理論上は WL 検定より強いモデルが、メッセージパッシングの GCN を上回らなかった [arxiv-2003.00982#c6](https://arxiv.org/pdf/2003.00982v5#page=29 "These new models are limited in terms of space/time complexities, with O(n2)/O(n3) respectively, not allowing them to scale to larger datasets.")。小さな TU データセットでは、標準偏差が大きく、すべてのモデルが統計的に同程度で、シードを変えると順位が変わった [arxiv-2003.00982#c9](https://arxiv.org/pdf/2003.00982v5#page=38 "We observe all NNs have similar statistical test performance as the standard deviation is quite large.")。

Gilmer らの論文にも、比較相手の数値が別の分割で得られたものだという注意がある [arxiv-1704.01212#c8](https://arxiv.org/pdf/1704.01212v2#page=8 "The model was trained on a different train/test split with 100k training samples vs 110k used in our experiments.")。

### 利益相反

ベンチマークの論文の著者が、自分たちのモデルやライブラリも評価していることがある。OGB の著者には GIN の著者が含まれ、Benchmarking GNNs と LRGB の著者は自分たちの提案した部品を評価している(各カードの notes 参照)。

## 設計への示唆(本記事の整理)

- **まず単純なベースラインと比べる。** グラフを使わない MLP や構造を使わないベースライン [arxiv-1912.09893#c6](https://arxiv.org/pdf/1912.09893v3#page=5 "As a matter of fact, if GNN performances are close to the ones of a structure-agnostic baseline, one can draw two possible conclusions: the task does not need topological information to be effectively solved, or the GNN is not exploiting graph structure adequately.")、SGC のような単純なモデル [arxiv-1902.07153#c9](https://arxiv.org/pdf/1902.07153v2#page=8 "It is likely that the expressive power of GCNs originates primarily from the repeated graph propagation (which SGC preserves) rather than the nonlinear feature extraction (which it doesn’t.)") に勝っているかを確かめる。
- **複数の分割で評価する。** 1つの固定の分割の結果は順位が入れ替わりうる [arxiv-1811.05868#c7](https://arxiv.org/pdf/1811.05868v2#page=4 "This shows how fragile and misleading results obtained on a single split can be.")。可能なら、時間や構造に基づく現実的な分割を使う [arxiv-2005.00687#c5](https://arxiv.org/pdf/2005.00687v7#page=11 "Speciﬁcally, we propose to train on papers published until 2017, validate on those published in 2018, and test on those published since 2019.")。
- **モデル選択と性能評価を分ける。** 検証データの精度を報告していないかを確認する [arxiv-1912.09893#c2](https://arxiv.org/pdf/1912.09893v3#page=3 "Consequently, model selection results are generally over-optimistic; this issue is thoroughly documented in Cawley & Talbot (2010).")。
- **グラフの同質性を確認する。** 同質性が低いグラフでは、自分と隣の表現を分ける設計が効くことがある [arxiv-2006.11468#c6](https://arxiv.org/pdf/2006.11468v2#page=6 "We found that removing the usual nonlinear transformations per round, as in SGC [37], works better (App. D.2), in which case we only need to include the ego-embedding in the ﬁnal representation.") [arxiv-2302.11640#c9](https://arxiv.org/pdf/2302.11640v2#page=9 "GAT-sep and GT-sep typically outperform their versions without embedding separation, which shows that this trick proposed in Zhu et al. (2020) is indeed helpful for learning under heterophily.")。異質性のデータセットには重複の問題がある [arxiv-2302.11640#c2](https://arxiv.org/pdf/2302.11640v2#page=4 "Since duplicates from the same group appear in the train, validation, and test parts of the datasets, they create a train-test data leakage:")。
- **深くする前に、問題に必要な距離を考える。** 遠くの情報が必要な問題では過圧縮が起きうる [arxiv-2006.05205#c1](https://arxiv.org/pdf/2006.05205v4#page=3 "When a prediction problem relies on long-range interaction between nodes, the GNN must have as many layers K as the estimated range of these interactions, or otherwise, these distant nodes would not be able to interact.")。

## わかっていないこと

- 過平滑化の理論は、密なグラフなどの条件のもとでしか示されておらず、疎な現実のグラフでの振る舞いは十分にわかっていない [arxiv-1905.10947#c6](https://arxiv.org/pdf/1905.10947v5#page=8 "However, real-world graphs are not often dense, which means that Theorem 2 is applicable to very limited GCNs.")。
- 層を増やしたときの劣化が、過平滑化、過圧縮、過学習、学習の難しさのどれによるかは、論文によって見方が違う [arxiv-1801.07606#c9](https://arxiv.org/pdf/1801.07606v1#page=7 "When the number of convolutional layers grows, the classiﬁcation accuracy decreases drastically, which is probably due to overﬁtting.") [arxiv-2006.05205#c8](https://arxiv.org/pdf/2006.05205v4#page=9 "We hypothesize that in long-range problems, the explanation for the degraded performance is over-squashing rather than over-smoothing.")。
- WL 検定との関係は可算のノード特徴を前提にしており、連続値の特徴の場合は残された課題である [arxiv-1810.00826#c3](https://arxiv.org/pdf/1810.00826v3#page=4 "Uncountable sets, where node features are continuous, need some further considerations.")。
- 長距離のベンチマークでのモデルの優劣は、ベースラインの見直しによって変わりうる [arxiv-2206.08164#c9](https://arxiv.org/pdf/2206.08164v4#page=8 "For a reassessment of the original baselines on all the datasets as well as extensions of PCQM-Contact’s metric, we refer to the paper [58] by Tönshoff et al., 2023.")。

## 参照カード

- [arxiv-1609.02907](../../papers/arxiv-1609.02907.yaml) Kipf & Welling, "Semi-Supervised Classification with Graph Convolutional Networks"
- [arxiv-1704.01212](../../papers/arxiv-1704.01212.yaml) Gilmer et al., "Neural Message Passing for Quantum Chemistry"
- [arxiv-1706.02216](../../papers/arxiv-1706.02216.yaml) Hamilton, Ying & Leskovec, "Inductive Representation Learning on Large Graphs"
- [arxiv-1710.10903](../../papers/arxiv-1710.10903.yaml) Veličković et al., "Graph Attention Networks"
- [arxiv-1902.07153](../../papers/arxiv-1902.07153.yaml) Wu et al., "Simplifying Graph Convolutional Networks"
- [arxiv-1810.00826](../../papers/arxiv-1810.00826.yaml) Xu et al., "How Powerful are Graph Neural Networks?"
- [arxiv-1801.07606](../../papers/arxiv-1801.07606.yaml) Li, Han & Wu, "Deeper Insights into Graph Convolutional Networks for Semi-Supervised Learning"
- [arxiv-1905.10947](../../papers/arxiv-1905.10947.yaml) Oono & Suzuki, "Graph Neural Networks Exponentially Lose Expressive Power for Node Classification"
- [arxiv-2006.05205](../../papers/arxiv-2006.05205.yaml) Alon & Yahav, "On the Bottleneck of Graph Neural Networks and its Practical Implications"
- [arxiv-2206.08164](../../papers/arxiv-2206.08164.yaml) Dwivedi et al., "Long Range Graph Benchmark"
- [arxiv-2006.11468](../../papers/arxiv-2006.11468.yaml) Zhu et al., "Beyond Homophily in Graph Neural Networks"
- [arxiv-2302.11640](../../papers/arxiv-2302.11640.yaml) Platonov et al., "A critical look at the evaluation of GNNs under heterophily"
- [arxiv-1811.05868](../../papers/arxiv-1811.05868.yaml) Shchur et al., "Pitfalls of Graph Neural Network Evaluation"
- [arxiv-1912.09893](../../papers/arxiv-1912.09893.yaml) Errica et al., "A Fair Comparison of Graph Neural Networks for Graph Classification"
- [arxiv-2005.00687](../../papers/arxiv-2005.00687.yaml) Hu et al., "Open Graph Benchmark"
- [arxiv-2003.00982](../../papers/arxiv-2003.00982.yaml) Dwivedi et al., "Benchmarking Graph Neural Networks"
