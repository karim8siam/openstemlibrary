# Unit 3: Nonlinear methods

*Editorial draft; not approved for live publication.*

## Kernels
### Kernels

### Kernels express similarity through inner products
A kernel function k(x,z) computes an inner product in an implicit feature representation when it is positive semidefinite: k(x,z)=<phi(x),phi(z)>. Instead of explicitly constructing all transformed coordinates, a kernel method can operate on a Gram matrix K_ij=k(x_i,x_j). A Gaussian radial-basis kernel exp(-gamma||x-z||²) treats nearby observations as similar and rapidly reduces similarity with distance; its gamma parameter controls the effective spatial scale. This does not guarantee that Euclidean distance in the original features corresponds to meaningful domain similarity.

Kernel ridge regression solves a regularized squared-error problem using alpha=(K+n lambda I)^{-1}y under one common scaling convention, then predicts f(x)=sum_i alpha_i k(x_i,x). The solution depends on the training examples rather than a fixed small coefficient vector. Training requires constructing and storing an n-by-n Gram matrix, with quadratic memory in the basic implementation, and generic direct solving can cost cubic time. Approximate features and inducing-point approaches trade exactness for scalable computation. Report the approximation rather than silently presenting it as the original algorithm.

Kernel selection embodies assumptions about smoothness. An RBF kernel implies a smooth notion of local variation, whereas a linear kernel reduces to ordinary inner products. Standardize input dimensions and document periodic or categorical structure before choosing a similarity metric. A single excessively scaled feature can dominate squared distance and effectively hide all others. The kernel trick is powerful because it changes the function class, not because it can recover information absent from the observed features.

### Demonstration
Take points x=0,1,2 and Gaussian gamma=1. The similarity between 0 and 1 is exp(-1)≈0.368 while between 0 and 2 it is exp(-4)≈0.0183. Increasing gamma makes both off-diagonal similarities smaller. Plot the 3×3 Gram matrix over gamma values and check its eigenvalues for numerical nonnegativity within rounding tolerance. Then perturb one feature's units by a factor of 100 and repeat. Explain why feature scaling changes neighborhoods even though the mathematical kernel definition is unchanged.

### Kernel conditioning and regularization stress test
A Gaussian kernel Gram matrix becomes nearly the identity when gamma is so large that distinct training samples have negligible similarity. When gamma is extremely small, most entries approach one, making the matrix almost rank one for distinct but nearby observations. Both extremes can create undesirable predictive behavior; the regularization parameter also affects numerical conditioning. On points 0,1,2, compute K for gamma values .001,1 and 100, and inspect the eigenvalue range. Compare predictions and effective degrees of freedom under a fixed ridge penalty. A good kernel setting is not determined solely by how visually smooth its similarity plot appears. If a model processes millions of examples, storing the full Gram matrix may be infeasible; Nyström approximation or random Fourier features approximate useful parts of the kernel behavior with different errors. Record approximation size, memory and validation loss. Calling a kernel model 'nonlinear' does not exempt it from data scale, leakage or calibration requirements.

## Nearest Neighbors
### Nearest Neighbors

### Nearest neighbors transfer a local label assumption
K-nearest-neighbor prediction identifies K training observations considered closest to a query under a specified distance. For regression it may average their targets; for classification it may take a majority vote or distance-weighted class proportion. The method is described as nonparametric because it does not fit a fixed-dimensional global function in the simplest version. Nevertheless, it has hyperparameters, implicit inductive assumptions and computational costs. A useful prediction requires the neighborhood to contain examples from a locally comparable conditional distribution.

Small K yields high flexibility and sensitivity to label noise. Large K smooths local variation and can wash out minority subpopulations. Ties need explicit handling, especially for even K in binary classification. Many distance metrics become less discriminative in high dimensions: unrelated coordinates contribute to distance, sparse vectors behave differently under cosine similarity, and missingness treatment may dominate the ranking. Feature selection, dimensionality reduction or learned metrics can matter more than switching K from five to seven.

Naïve prediction scans n points of dimension d, costing O(nd) arithmetic per query. Spatial trees can accelerate certain low-dimensional metrics but often deteriorate at high dimensions; approximate nearest-neighbor indexes use recall-versus-latency tradeoffs. A trained index can also become stale if the reference population changes. In a recommendation system, retrieving a near neighbor in embedding space does not by itself establish that recommending its associated item is safe or relevant.

### Small calculation
Training observations have scalar features 1,4,7 and labels 2,8,11. For query x=5, distances are 4,1,2. With K=1 regression predicts 8. With K=2 it averages the labels of points 4 and 7, predicting 9.5. A distance-weighted rule with weights 1/d predicts (8/1+11/2)/(1+1/2)=9. For a held-out observation at x=5 with true y=10, squared errors are 4,0.25 and 1. Those values illustrate one query, not generalization superiority.

### KNN distances and missing-information geometry
Consider two machines with temperature, pressure and vibration features. Machine A has temperature close to the query but pressure far away; machine B shows the opposite. The nearest neighbor depends on relative feature scales and chosen metric. An unscaled Euclidean distance implicitly assumes one unit of each recorded feature is equally meaningful after squaring. A Mahalanobis metric uses an inverse covariance matrix to account for correlations, but its estimate can be unstable when dimension approaches sample size. Missing values introduce a further problem: computing distance only over shared observed coordinates can favor pairs with few measurements unless normalization is careful. Test predictions under deliberate deletion of one feature and compare a missingness-aware policy with mean imputation. In a retriever, report neighbor IDs, distances and exact metric version for a sample of queries. This debugging evidence can uncover mislabeled feature columns that average accuracy obscures.

## Decision Trees
### Decision Trees

### Decision trees partition a feature space with rules
A classification tree recursively splits the observations, often choosing the feature threshold that maximizes reduction in Gini impurity or entropy. For class proportions p_c in a node, Gini impurity is 1-sum_c p_c². If all observations have one class, impurity is zero; if two classes are evenly mixed, it is 0.5. A candidate split is compared by its child sample-weighted impurity. The greedily best immediate split does not necessarily minimize the error of the fully grown tree, because future splitting possibilities matter.

Trees can capture interactions without explicitly specifying polynomial terms. They also extrapolate poorly in regression: leaves usually predict constants derived from observed training targets, so predictions outside the training feature range may remain stuck at the nearest learned leaf value. A deep tree with one observation per leaf memorizes peculiarities of training data. Constraints on depth, leaf population and split gain create regularization. Pruning can replace a complex branch with a simpler leaf if complexity cost outweighs error reduction.

Categorical encoding changes the splits a learner can express; treating category IDs as ordered numbers can create meaningless thresholds. Missing-value routing must be defined during training and preserved during inference. Feature importance based on impurity reductions can favor features with many possible split points, and correlated predictors may share credit unpredictably. Permutation importance depends on evaluation distribution and can itself mislead when features are strongly dependent.

### Split trace
Suppose a parent node contains six positive and four negative examples. Its Gini impurity is 1-(.6²+.4²)=.48. A split sends four positives and one negative left, and two positives and three negatives right. Child impurities are .32 and .48, each weighted .5, giving .40. The impurity reduction is .08. A competing split with children pure would improve more if it obeyed the minimum leaf size. Verify these counts manually and test the split with different leaf-size constraints. This exercise separates scoring arithmetic from the search procedure that proposes candidate thresholds.

### Tree pruning as a bias-complexity tradeoff
A fully grown classification tree can isolate extremely small groups and assign perfect training labels to them. Those leaves may represent genuine rare structure or annotation noise. Cost-complexity pruning minimizes a combination of prediction error and a penalty on number of terminal nodes, tracing a sequence of progressively smaller trees. Select the complexity parameter on validation data; do not simply choose the training-perfect tree. Evaluate rare but high-cost classes separately because overall pruning may remove leaves that detect them. A split based on a small handful of cases should also be tested for stability across resamples. In a worked audit, fit depth 1 through 10 on a fixed dataset, plot train and grouped-validation errors, and inspect which samples switch decisions when depth changes. That change matters to downstream users, not just the line on a performance graph. Interpretable tree rules can still be brittle at thresholds and under feature drift.

## Ensembles
### Ensembles

### Ensembles combine diverse errors, not magic votes
Bagging resamples training observations to fit multiple base learners and aggregates predictions. In a random forest, candidate features are often subsampled at splits so that trees do not all exploit the same dominant predictor. Averaging can reduce variance when errors are not perfectly correlated. If every tree makes the same systematic mistake under a shifted data distribution, adding trees will not repair the bias. Out-of-bag observations support convenient internal diagnostics, but their reuse in extensive model selection can still create optimistic reporting.

Boosting instead builds learners sequentially to improve a specified objective, frequently by fitting new models to residual-like gradients. In gradient boosting, each iteration adds a weighted weak learner that descends the loss functional. Learning rate, tree depth, regularization and number of rounds interact; early stopping on a genuinely held-out validation subset is common. A sophisticated ensemble can overfit categorical artifacts and interactions as effectively as it discovers useful patterns. Calibration may need a separate assessment even when ranking metrics are strong.

Ensemble gains should be compared with added training time, memory, inference latency and interpretability requirements. A small business monitoring thousands of devices every second may benefit more from a well-calibrated logistic baseline than a heavily tuned ensemble with a tiny offline accuracy advantage. Evaluate the incremental value against deployment constraints, not against an intentionally weak strawman.

### Error-correlation experiment
Two unbiased regression models have error variances 4 and 9 and covariance 2. Their equal-weight average has variance (4+9+2×2)/4=4.25. If covariance were zero, variance would be 13/4=3.25. If the errors were maximally aligned, the improvement could shrink. Generate correlated Gaussian errors in a seeded toy experiment and compare empirical ensemble variance with the theoretical formula. Explain that averaging biased estimators adds the squared ensemble bias to mean squared error; the variance calculation alone is not the full risk.

### Boosting loss choice and early stopping
Gradient boosting fits a new learner to a pseudo-residual direction derived from the chosen loss. For squared error, the negative gradient is proportional to y-f(x); for logistic loss it relates to y-p(x) on an appropriate score scale. Thus 'fit residuals' is a shorthand that must specify the objective. Shrinkage multiplies each added learner by a learning rate, often allowing more rounds with smaller changes. Early stopping selects the number of rounds using validation rather than training fit. Compare trajectories with the same total tree-computation budget and different learning rates to avoid misleading speed claims. For imbalanced classification, weighting or loss changes can alter the calibration of output scores. After training, evaluate both ranking quality and probability reliability on an untouched holdout. A 500-tree model with slightly lower average log loss may still be inferior operationally if its latency breaches the service deadline.

## Integrated technical investigations and review
# Integrated investigation for Nonlinear methods

### Neighborhood assumptions and changes of representation
A nearest-neighbor method and an RBF kernel both express locality, but they do so differently. A KNN predictor uses a fixed number of nearby training labels, while kernel regression or a kernel machine can weight many training points according to similarity. When observations are unevenly distributed, KNN adjusts its effective physical radius to include K points; a fixed-bandwidth kernel uses a similar radius regardless of local sample density. Sparse regions therefore receive substantially different levels of smoothing. Neither choice resolves the problem of unmeasured confounding variables or inconsistent labels.

In document classification, Euclidean distance on raw count vectors often treats document length as a principal determinant of similarity. TF–IDF normalization and cosine similarity can focus on proportional term usage, though short documents remain noisy. In image analysis, pixel Euclidean distance can be large for two photographs of the same object under lighting or translation. Domain-aligned learned embeddings can help, but their quality requires independent evaluation. A method is only as meaningful as the representation over which its geometry is defined.

### Ensemble uncertainty and correlated failures
Random forests generate diverse predictors through bootstrapping and feature randomness. Their predicted variance across trees can reflect instability of fitted trees but is not automatically a valid interval for the true outcome. Trees share training data, can learn the same shortcuts and may be highly correlated. To compare ensembles, compute each base model's test residuals e_j and the covariance of those residuals. For an equal average of M models, ensemble error variance involves all pairwise covariances, not merely the individual variances divided by M.

For two models with variances 4 and 9 and covariance 2, the average has variance (4+9+2×2)/4=4.25. The best individual variance is 4, so the unweighted average is worse than that model despite reducing variance relative to the second. Weight selection can improve or harm the result depending on the covariance matrix and bias. If the two models fail in the same extreme weather conditions, ensemble agreement may create misplaced confidence exactly where uncertainty is important.

### Validation under extrapolation
Create training data x uniformly sampled between -2 and 2 with targets y=sin(x)+small noise. Evaluate first on random test samples in the same interval, then on x between 2 and 4. KNN usually returns labels near the boundary in the extrapolation regime; a tree similarly predicts within known leaf outcomes; linear regression extends its fitted slope; an RBF kernel's behavior depends on its regularization and intercept treatment. No algorithm can learn the true sine curve outside the observed interval without appropriate assumptions. The goal is not to declare a winner but to inspect the inductive bias exposed by the shift.

Quantify predictive error both near and far from the training support. Report test coordinate range in every figure. A single pooled metric over a mixed test set can conceal catastrophic failures in the extrapolation subset. If an industrial control system must extrapolate, prefer a physical model or a controlled experiment that samples relevant new operating conditions rather than a purely empirical claim based on interior observations.

### Tree leaf counts and categorical traps
A tree learner evaluating all split points of a numerical feature can appear attractive because each split is easy to interpret. Yet repeated greedy choices produce complex global interactions: one variable can matter only inside a branch defined by another variable. An impurity-based feature-importance ranking may favor continuous identifiers with many thresholds over low-cardinality but causal variables. Permutation importance on a test distribution can also become misleading if correlated variables can substitute for one another. A careful analysis uses domain plausibility, ablation and conditional diagnostics rather than a single plotted importance bar.

For categories such as device manufacturer, ordinal encoding 'A=0,B=1,C=2' invents an ordering. A split at 1.5 groups A and B together for an arbitrary reason. One-hot or appropriate categorical splits remove this exact ordering artifact, but high-cardinality encodings raise memory and leakage risks. Target encoding must be computed within training folds, using out-of-fold strategies where appropriate, because a category's own label must not be directly incorporated into its explanatory value.

### Controlled engineering comparison
Benchmark a small regularized tree, forest and gradient-boosted model against a distance-based learner, using the same feature store snapshot and held-out entities. Measure not just discrimination but calibration, p95 latency, memory footprint and failures on unseen categories. For class imbalances, track false negatives under a fixed false-positive budget rather than optimizing average classification accuracy. Tune with a declared resource budget. Record a diagnostic case for every major failure regime and an exact recipe for reproducing the result from the saved dataset snapshot.

### Separate interpolation from extrapolation in evaluation
Nonlinear models often perform well where nearby training observations are plentiful and poorly where the evaluation distribution leaves the training support. Rather than publishing one overall average, tag each test observation by a defensible measure of distance from training support. Use feature-space distance only with a representation whose metric has a documented interpretation; embedding distances can inherit learned shortcuts. Report accuracy separately for interpolation-like and extrapolation-like cases. In a manufacturing example, a model trained on spindle speeds from 1,000 to 3,000 revolutions per minute should not claim proven reliability at 5,000 based on random holdout scores inside the earlier range. A controlled laboratory that deliberately evaluates at 3,500 and 4,000 can measure some extrapolation failure, but it still cannot prove safety under every untested condition. Combine mechanistic knowledge, domain constraints and data collection targeted at the actual operating envelope.

### Worked question: Gaussian kernel scale
With Gaussian kernel k(x,z)=exp(-gamma(x-z)^2), evaluate similarities k(0,1) and k(0,2) when gamma=1, and explain the effect of increasing gamma.

**Model the question**
Squared distances are 1 and 4. Multiply by gamma, negate and exponentiate. A Gaussian kernel returns one for identical inputs and lies in (0,1] for the stated real inputs.

**Calculate or derive**
k(0,1)=exp(-1)≈0.367879 and k(0,2)=exp(-4)≈0.018316. With gamma=2 they become exp(-2)≈0.135335 and exp(-8)≈0.000335. Thus the same absolute distances are treated as less similar with larger gamma.

**Check assumptions and boundaries**
This arithmetic assumes a one-dimensional Euclidean feature with meaningful units. Multiplying every coordinate by ten has the same effect on squared distances as multiplying gamma by 100. Feature scaling and kernel width must therefore be chosen together.

**Answer:** At gamma=1, similarities are approximately 0.3679 and 0.0183; increasing gamma shrinks similarities of distinct points.

### Worked question: K-nearest-neighbor regression
Training pairs are (1,2),(4,8),(7,11). Predict y for input x=5 using K=1 and K=2 unweighted nearest-neighbor regression.

**Model the question**
Compute absolute distances to x=5: from x=1 distance four, x=4 distance one, x=7 distance two. Sort by these distances without peeking at the associated targets.

**Calculate or derive**
K=1 chooses x=4 with label 8, so prediction is 8. K=2 chooses x=4 and 7 with labels 8 and 11, so mean prediction is (8+11)/2=9.5.

**Check assumptions and boundaries**
If equal-distance ties existed, the algorithm would need a deterministic tie rule. Different feature scaling could alter the neighbor ordering in more than one dimension; the current one-dimensional result is a property of the specified metric and sample only.

**Answer:** K=1 predicts 8; K=2 predicts 9.5.

### Worked question: Gini improvement
A binary-classification tree node contains six positives and four negatives. One proposed split produces children (4 positives,1 negative) and (2 positives,3 negatives). Calculate parent Gini, weighted child Gini and improvement.

**Model the question**
Gini for a node with positive proportion p is 1-p^2-(1-p)^2. Parent p=6/10=.6; each child contains five observations and has equal weight .5.

**Calculate or derive**
Parent Gini=1-.36-.16=.48. Left Gini=1-(4/5)^2-(1/5)^2=.32. Right Gini=1-(2/5)^2-(3/5)^2=.48. Weighted child impurity=.5(.32)+.5(.48)=.40. Improvement=.48-.40=.08.

**Check assumptions and boundaries**
An improvement of .08 does not certify global optimality: a competing split can score better, and deeper splits interact with earlier choices. Check leaf-size constraints before accepting a split. Small sample counts can also make scores unstable.

**Answer:** Parent Gini=.48, weighted child=.40, reduction=.08.
