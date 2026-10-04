import sys

sys.path.insert(0, "scripts/cards")
from _spec_builder import build  # noqa: E402
from topic_tree_common import BASE_NOTE, CREATED  # noqa: E402

SPECS = [
    {"id": "arxiv-1504.07676",
     "title": "Explaining the Success of AdaBoost and Random Forests as Interpolating Classifiers",
     "authors": ["Abraham J. Wyner", "Matthew Olson", "Justin Bleich", "David Mease"],
     "year": 2015, "version": "arXiv v2",
     "links": {"arxiv": "https://arxiv.org/abs/1504.07676"},
     "tasks": ["tabular-classification"],
     "fam": ["random-forests", "tree-ensembles"], "par": ["supervised"],
     "proposes": ["An explanation of AdaBoost and random forests as self-averaging, interpolating classifiers that produce a 'spiked-smooth' decision surface",
                  "A decomposition of AdaBoost run for many iterations into a weighted sum of interpolating classifiers"],
     "claims": [
         ("Main conjecture: random forests are a self-averaging, interpolating algorithm producing what the authors call a 'spiked-smooth' classifier; they view AdaBoost in the same light and conjecture that both succeed because of this mechanism, supported by examples rather than proofs.",
          "Abstract",
          "We conjecture that both AdaBoost and random forests succeed because of this mechanism."),
         ("Proposed mechanism: interpolation gives a kind of robustness to noise, because a classifier that fits the data extremely locally lets a noise point affect the fit only in a small region; combined with averaging, the fit stabilizes where there is signal while the influence of noise points becomes more localized.",
          "Introduction",
          "It turns out that interpolation provides a kind of robustness to noise: if a classiﬁer ﬁts the data extremely locally, a “noise” point in one region will not aﬀect the ﬁt of the classiﬁer at a nearby location."),
         ("Practical recommendation drawn from this view, against the conventional advice to regularize boosting, stop early, or use low-complexity learners such as stumps: boosting should be used like random forests, with large trees and without regularization or early stopping.",
          "Abstract",
          "We conclude that boosting should be used like random forests: with large decision trees, without regularization or early stopping."),
         ("Why random forests count as interpolators here (classification): in implementations such as R randomForest the minimum node size is 1 for classification, so each tree interpolates its bootstrap sample; the authors argue the voted forest then fits the whole training set perfectly, at least with very high probability, because each point appears in most bootstrap samples as the number of trees grows.",
          "Section 3.1",
          "The ﬁnal random forest classiﬁer still ﬁts the entire training data set perfectly, at least with very high probability."),
         ("Self-smoothing of AdaBoost: in a 20-dimensional pure-noise simulation (n = 5000, P(y=1|x) = 0.8), 1000 iterations of AdaBoost are rewritten as a weighted average of 10 blocks of 100 iterations, each of which itself interpolates the training data; the authors argue the extra iterations act as averaging that further localizes errors near noise points rather than as overfitting.",
          "Section 4.1",
          "Boosting for 1000 iterations is thus a point-wise weighted average of 10 interpolating classiﬁers."),
         ("Against stumps: in a five-dimensional simulation with an additive Bayes rule and a high Bayes error, AdaBoost with stumps was outperformed by AdaBoost with large trees (up to 2^8 terminal nodes); the authors attribute this to stumps not interpolating locally enough and lacking self-smoothing. The numbers come from a single simulation run, which the authors say is qualitatively reproducible.",
          "Section 4.3",
          "These numerical values are based only on a single run of this simulation, but the qualitative ﬁnding is reproducible over repeated runs."),
         ("Evidence base on real data: because noise points cannot be identified in real data, the authors flip the labels of 100 randomly chosen training points (about 2%) of the phoneme data (n = 5404, p = 5; 70/30 train/test split) and study the fits of boosted trees and a random forest around them; a version of this analysis with 5% label noise was repeated on five UCI datasets over 50 random splits.",
          "Section 5.1",
          "As a substitute for noise points, we ﬂipped the signs of 100 randomly chosen points in our training data set (about 2% of the data) and analyzed the ﬁts of boosted trees and a random forest classiﬁer around these points."),
         ("Hedge on the decorrelation finding: sub-ensembles of AdaBoost had less correlated errors than those of a random forest, which were less correlated than those of bagged trees, in this example; the authors observed this in a few datasets and say they cannot state under what conditions it holds more generally.",
          "Section 4.2",
          "While we observed this phenomenon in a few data sets, we cannot state under what conditions it happens more generally."),
     ],
     "notes": ("Affiliations: Wharton School, University of Pennsylvania (Wyner, Olson, Bleich) and Apple Inc. (Mease). The PDF uses a journal-style template "
               "with an empty 'Editor:' field, but no venue is stated in the PDF or the arXiv metadata (comment: '40 pages, 11 figures, 2 algorithms'); no venue recorded. "
               "AdaBoost here uses rpart trees grown to a maximum depth of 8; random forests use 500 trees. The evidence is mostly two- to twenty-dimensional simulations "
               "with known Bayes rules plus label-flipping experiments on six real datasets; no theorem is proved. The paper cites the authors' own earlier work "
               "(Mease and Wyner, 2008; Wyner, 2003) as evidence against the statistical view of boosting. Results (Table 1, error rates) not recorded. "
               "AdaBoost is not tagged gradient-boosted-trees.")},

    {"id": "arxiv-1911.00190",
     "title": "Randomization as Regularization: A Degrees of Freedom Explanation for Random Forest Success",
     "authors": ["Lucas Mentch", "Siyu Zhou"],
     "year": 2019, "venue": "Journal of Machine Learning Research", "version": "arXiv v2",
     "links": {"arxiv": "https://arxiv.org/abs/1911.00190"},
     "tasks": ["tabular-regression"],
     "fam": ["random-forests", "tree-ensembles", "linear-models"], "par": ["supervised"],
     "proposes": ["A degrees-of-freedom explanation of random forest success: the mtry randomization acts as implicit regularization, most useful at low signal-to-noise ratio",
                  "Randomized forward selection (RandFS) and bagged forward selection (BaggFS) as linear-model analogues of random forests and bagging"],
     "claims": [
         ("Main thesis: the extra randomness injected into individual trees acts as implicit regularization, which the authors say makes random forests an ideal model in low signal-to-noise ratio (SNR) settings; from a model-complexity view, mtry plays a role similar to the shrinkage penalty in lasso and ridge regression.",
          "Abstract",
          "the additional randomness injected into individual trees serves as a form of implicit regularization, making random forests an ideal model in low signal-to-noise ratio (SNR) settings"),
         ("Critique of the interpolation explanation (Wyner et al. 2017) for regression: regression forests average rather than vote, and each bootstrap sample omits about 36.8% of observations on average, so a forest of fully grown trees is a weighted average of a training point's response and other responses and will not interpolate with exceedingly high probability.",
          "Section 2.3",
          "and hence with exceedingly high probability, the random forest will not interpolate."),
         ("Further critique: Wyner et al. seem to largely ignore the role of randomness, and their explanation would seem to apply equally well to bagging; the authors also take issue with the popular view that random forests simply 'are better' than bagging, calling it not a universal truth.",
          "Section 2.3",
          "The explanation the authors provide for random forest success would seem to apply equally well to bagging."),
         ("Degrees-of-freedom evidence: Monte Carlo estimates (500 trials, randomForest defaults except mtry and maxnodes, SNR 3.52, linear and MARSadd models) show that at every fixed maxnodes the estimated dof increases with mtry, so bagging (mtry = 1) always has more dof than the default regression forest (mtry = 0.33); the authors report nearly identical findings at SNR 0.09 (Appendix A).",
          "Section 3",
          "More importantly for our purposes, in each plot in Figure 3 we see that at every ﬁxed level of maxnodes, the dof increases with mtry."),
         ("Random forest vs bagging across SNR (simulations, 500 repetitions, test MSE on 1000 independent points): the advantage of random forests (mtry = 0.33) over bagging shrinks as SNR increases and bagging eventually wins at large SNR; the authors conclude that the view that random forests simply 'are better' than bagging seems largely unfounded and that the optimal mtry seems to depend on SNR. The same pattern is reported on 15 real regression datasets with noise injected into the response (Section 4.3).",
          "Section 4.1",
          "Given these results, the conventional wisdom that random forests simply “are better” than bagging seems largely unfounded; rather, the optimal value of mtry seems to be a function of the SNR."),
         ("Randomized forward selection: in linear-model settings taken from Hastie et al. (2017), with tuning parameters chosen on an independent validation set of size n, even untuned RandFS with mtry = 0.33 outperformed the lasso across all SNRs in the low and medium settings; in the high-dimensional settings the explicit regularizers (lasso, relaxed lasso) performed well.",
          "Section 5.2",
          "Even more remarkable is the performance of RandFS when mtry = 0.33 and is not tuned – in both the low and medium settings, even this default RandFS outperforms the lasso across all SNRs."),
         ("Theory (simplified model, not trees): for linear regression with n > p and an orthogonal design, averaging OLS fits on uniformly random subsets of m < p features converges, as the number of models grows, to the OLS estimate shrunk by m/p (stated as equivalent to ridge with penalty (p-m)/m); a related expectation result is given when observations are also subsampled. The authors say the same kind of effect is likely present in random forests, without proving it for trees.",
          "Section 5.3",
          "Under the data setup given above, assume that n > p and the design matrix X is orthogonal."),
         ("Practical guidance: the authors suggest mtry can be thought of as controlling the amount of shrinkage and is best tuned in practice, while noting that the default mtry = 0.33, though not always optimal, generally performs quite well and seems as good a starting point as any.",
          "Section 6",
          "Just as with explicit regularization procedures, the results above suggest that the mtry parameter in random forests can be thought of as controlling the amount of shrinkage and regularization and thus is best tuned in practice."),
         ("Proposed answer to why random forests work well on real data: in the authors' view many real datasets are simply quite noisy; citing Hastie et al. (2017), they note that SNRs as large as 5 or 6 are argued to be extremely rare on real data, which would explain why forests are often seen as superior to bagging.",
          "Section 6",
          "In our view, the clear answer is that in practice, many datasets simply are quite noisy."),
     ],
     "notes": ("Affiliation: Department of Statistics, University of Pittsburgh. Venue: the arXiv v2 PDF header reads 'Journal of Machine Learning Research 21 (2020) 1-36, "
               "Submitted 10/19; Revised 7/20; Published 8/20' (arXiv comment: 'To Appear in the Journal of Machine Learning Research (JMLR)'). Year kept as the arXiv "
               "submission year 2019. Real-data protocol (Section 4.3): 10 UCI regression datasets plus 5 high-dimensional datasets, rows with missing values removed, "
               "extra Gaussian noise added to the response at proportions alpha of var(y), 10-fold CV error of randomForest with default settings except mtry (0.33 vs 1), "
               "500 replications; results shown only as figures. Regression is the main focus; the authors note Breiman (2001) and Wyner et al. (2017) pertain to classification. "
               "Code: https://github.com/syzhou5/randomness-as-regularization. Results figures not recorded.")},

    {"id": "arxiv-2003.03629",
     "title": "Getting Better from Worse: Augmented Bagging and a Cautionary Tale of Variable Importance",
     "authors": ["Lucas Mentch", "Siyu Zhou"],
     "year": 2020, "version": "arXiv v2",
     "links": {"arxiv": "https://arxiv.org/abs/2003.03629"},
     "tasks": ["tabular-regression", "model-explanation"],
     "fam": ["random-forests", "tree-ensembles"], "par": ["supervised"],
     "proposes": ["Augmented bagging (AugBagg): bagging on a feature space augmented with extra noise features generated conditionally independent of the response",
                  "A caution that variable-importance tests based on drops in predictive accuracy can declare pure noise features significant"],
     "claims": [
         ("Main finding: adding extra randomly generated noise features and then running bagging (AugBagg) can lead to dramatic improvements in out-of-sample accuracy, sometimes outperforming even an optimally tuned random forest; consequently, variable importance based on improved accuracy may be deeply flawed.",
          "Abstract",
          "Surprisingly, we demonstrate that this simple act of including extra noise variables in the model can lead to dramatic improvements in out-of-sample predictive accuracy, sometimes outperforming even an optimally tuned traditional random forest."),
         ("Definition of the added features: the noise features N need only be conditionally independent of Y given X, so they may be correlated with the original features; the authors note that how they are generated can greatly affect performance.",
          "Section 2",
          "Importantly, we insist only that N be generated conditionally independent of Y given X."),
         ("When it helps: in the authors' simulations (linear model, n = 100, p = 5 signal features, 500 repetitions per point, random forests with each mtry as reference lines), gains appear most dramatic at low SNRs, while correlated noise features can keep improving performance at higher SNRs; with independent noise features performance deteriorates with the number of added features at moderate SNRs.",
          "Discussion",
          "Performance gains appear most dramatic at low SNRs, though the introduction of correlated noise features can continue to improve performance even at higher SNRs."),
         ("Real-data protocol: on 14 regression datasets (9 low- and 5 high-dimensional), the number of added features q is tuned over {p/2, p, 3p/2, 2p} and their correlation r over {0, 0.1, 0.4, 0.7, 0.9}, extra noise is injected into the response, and performance is relative test error versus bagging. No description of the data used to select q and r or of how the test error is estimated on these datasets was found in the text (searched for validation, cross-validation, out-of-bag, hold, test set).",
          "Section 3",
          "Since diﬀerent datasets have diﬀerent numbers of original features, q is tuned over p/2, p, 3p/2 and 2p."),
         ("Theoretical motivation (simplified model, OLS ensembles rather than trees): building on LeJeune et al. (2019), under their asymptotic assumptions (e.g., identity covariance, feature and row subsampling), a subsampled OLS ensemble built on a design augmented with independent noise features behaves like the ensemble on the original design with a smaller feature-subsampling rate, i.e., a more regularized estimator.",
          "Section 4",
          "eﬀect as constructing the ensemble on the original design with a smaller subsampling rate, thereby producing a more regularized estimator."),
         ("Variable importance: using the test of Williamson et al. (2020) with bagged ensembles of 500 trees, tests that drop the noise features under investigation rejected the null (declaring pure noise features important) far above the nominal 5% level: nearly 30% of the time at low SNRs with many tested features when the noise features are independent of the original features.",
          "Section 5",
          "the tests that drop the features under investigation reject nearly 30% of the time at low SNRs when a large number of features are being tested."),
         ("Caveat on those rejection rates: the authors caution that the particular rejection probabilities should not be read as guidelines; inflation depends on the data and on the power of the test (more powerful tests would reject even more often).",
          "Section 5",
          "These empirical results should in no way be seen as guidelines for how often or under what settings such tests will produce inﬂated rejection proportions."),
         ("Replacement-style tests (replacing features with random substitutes, as in Mentch and Hooker 2016 and Coleman et al. 2019) kept close to the nominal level when the substitutes had the same distribution as the tested features, but when correlated noise features were replaced by independent noise the test rejected with very high probability across all but the lowest SNRs.",
          "Section 5",
          "Here we again notice a troubling trend: the test has a very high probability of rejecting across all but the lowest SNRs and this probability appears to increase with q."),
         ("Interpretation and limitations: the authors do not conclude the tests are wrong, only that rejection means the features improve performance when included; they stress AugBagg should not replace random forests, as it increases computation and they cannot offer default values for q and r likely to work broadly.",
          "Discussion",
          "we stress that the procedure should not be seen as replacing or superseding more eﬃcient procedures like random forests."),
     ],
     "notes": ("Affiliation: Department of Statistics, University of Pittsburgh. No venue stated in the PDF or arXiv metadata; no venue recorded. "
               "Same authors as arxiv-1911.00190 (cited here as Mentch and Zhou, 2020), whose randomization-as-regularization view motivates AugBagg; the variable-importance "
               "tests discussed include Mentch and Hooker (2016), co-authored by the first author. In the real-data experiments bagging remained better on 2 of 14 datasets "
               "(AquaticTox, mtp2, the two with the most features), which the authors suggest may be because many original features are themselves noise. "
               "Section numbers 2-5 are confirmed by the roadmap in the Introduction; subsections are cited by section only. Results are shown as figures only; no numbers recorded.")},

    {"id": "arxiv-1804.03515",
     "title": "Hyperparameters and Tuning Strategies for Random Forest",
     "authors": ["Philipp Probst", "Marvin Wright", "Anne-Laure Boulesteix"],
     "year": 2018, "venue": "WIREs Data Mining and Knowledge Discovery", "version": "arXiv v2",
     "links": {"arxiv": "https://arxiv.org/abs/1804.03515"},
     "tasks": ["tabular-classification", "tabular-regression"],
     "fam": ["random-forests", "tree-ensembles"], "par": ["supervised"],
     "proposes": ["A literature review of random forest hyperparameters (mtry, sample size, replacement, node size, number of trees, splitting rule) and their effect on performance and variable importance",
                  "tuneRanger: an R package tuning mtry, sample size and node size with sequential model-based optimization evaluated on out-of-bag predictions"],
     "claims": [
         ("Starting point: the authors state it is well known that random forests mostly work reasonably well with software default hyperparameters, but that tuning can nevertheless improve performance.",
          "Abstract",
          "It is well known that in most cases RF works reasonably well with the default values of the hyperparameters speciﬁed in software packages."),
         ("Defaults (Table 1 and Section 2.1.1): mtry = sqrt(p) for classification and p/3 for regression in several packages; sample size n drawn with replacement; node size 1 for classification and 5 for regression. Lower mtry gives less correlated trees but weaker individual trees (a stability-accuracy trade-off).",
          "Section 2.1.1",
          "As default value in several software packages mtry is set to √p for classiﬁcation and p/3 for regression with p being the number of predictor variables."),
         ("The number of trees is not a tuning parameter in the classical sense but should be set sufficiently high; citing their own earlier work, more trees are always better for mean-quadratic-loss measures, while out-of-bag error-rate curves occasionally increase slightly with more trees.",
          "Section 2.1.4",
          "The number of trees in a forest is a parameter that is not tunable in the classical sense but should be set suﬃciently high (Díaz-Uriarte and De Andres, 2006; Oshiro et al., 2012; Probst and Boulesteix, 2017)."),
         ("Which hyperparameters matter, citing Probst et al. (2018, their own tunability study on 38 datasets): random forests are far less tunable than e.g. SVMs; tuning mtry gave the largest average AUC gain, then sample size, while node size had only a small effect and sampling without replacement a small positive effect.",
          "Tunability of random forest",
          "In their study, tuning the parameter mtry provides the biggest average improvement of the AUC (0.006), followed by the sample size (0.004), while the node size had only a small eﬀect (0.001)."),
         ("Evaluation strategy for tuning: the authors recommend out-of-bag predictions for most datasets because they are much faster than k-fold cross-validation, noting that OOB estimates can be biased in special situations (e.g., very small datasets with many predictors and balanced classes).",
          "Evaluation strategies and evaluation measures",
          "we recommend the out-of-bag approach for tuning as an appropriate procedure for most datasets."),
         ("Benchmark protocol: 39 binary-target OpenML100 datasets without missing values (26 small, 13 big by estimated tuning time); 5-fold CV repeated 10 times for small and once for big datasets; 2000 trees for every method; tuneRanger (with several target measures), mlrHyperopt, caret and tuneRF at default settings compared with untuned ranger; failed runs were assigned the worst result or imputed.",
          "Benchmark study",
          "For classiﬁcation we only use datasets that have a binary target and no missing values, which leads to a collection of 39 datasets."),
         ("Benchmark result: differences were small, although on average all tuning methods beat default ranger; the authors relate the small differences to random forests being less tunable. Tuning node size and sample size together with mtry gave on average a further improvement over tuning mtry alone.",
          "Results",
          "We see that the diﬀerences are small, although on average all algorithms perform better than the ranger default."),
         ("When defaults fail badly: on two datasets the default forest was far worse and tuning mtry was essential: monks-problems-2 (an interaction between two of six categorical predictors, where low mtry forces splits on the wrong variable) and madelon (20 informative and 480 non-informative predictors, where the default mtry is much too low).",
          "Results",
          "For these two datasets it is essential to tune mtry, which is done by all tuning algorithms."),
         ("Conclusion: mtry, sample size and node size control the randomness of the forest; mtry is the most influential, with its best value depending on the number of variables related to the outcome, while sample size and node size have a minor influence but are worth tuning in many cases. The authors also note the literature lacks systematic large-scale comparison studies of random forest hyperparameters.",
          "Conclusion and Discussion",
          "Out of these parameters, mtry is most inﬂuential both according to the literature and in our own experiments."),
     ],
     "notes": ("Affiliations not recorded. Venue from the arXiv journal_ref ('WIREs Data Mining Knowl Discov 2019'). Conflict of interest: tuneRanger, the method that "
               "performed best on average in the benchmark, is the authors' own package (Probst, 2018), and ranger is co-author Wright's package (Wright and Ziegler, 2017); "
               "the tunability evidence (Probst et al., 2018) and the number-of-trees results (Probst and Boulesteix, 2017) are the authors' own earlier work. The paper does not "
               "state these as conflicts, although its conclusion discusses that comparison studies in papers introducing new methods are often biased in their favour. "
               "tuneRanger defaults: SMBO (mlrMBO) with 30 initial random points and 70 iterations, tuning mtry, sample size and node size, sampling without replacement, "
               "OOB evaluation, Brier score (classification) or MSE (regression); final setting = average of the best 5% of iterations. Benchmark is classification only. "
               "Results tables (Tables 2-3) not recorded.")},
]

if __name__ == "__main__":
    build(SPECS, base_note=BASE_NOTE, **CREATED)
