# Unit 6: Learning foundations

*Editorial draft; not approved for live publication.*

## Supervised Learning
**Supervised Learning: conceptual explanation**

### Supervised learning: data, objective and leakage
In supervised learning, a model is fitted to labeled examples (x_i,y_i) so that predictions generalize to new observations. Classification predicts categories or class probabilities; regression predicts a numerical outcome. The usual empirical-risk objective minimizes (1/n)∑_i L(f_θ(x_i),y_i), optionally with a regularization term λR(θ). The choice of loss matters: squared error penalizes large residuals quadratically, cross-entropy evaluates probability assignments for classes, and absolute error is less sensitive than squared error to extreme residuals under common assumptions.

An empirical training loss can become very small while deployment error remains large. Overfitting occurs when the model captures incidental noise or dataset-specific features rather than stable relationships. A train–validation–test split separates fitting, model selection and final evaluation. If the test set is repeatedly used to choose models, it ceases to provide an unbiased final performance check. In time-series forecasting, random row shuffling may leak future information into training; use chronologically appropriate splits and prevent overlapping windows from sharing a future label.

Leakage can be subtle. A hospital admission predictor trained with a code assigned only after discharge may appear highly accurate while being useless at admission time. A student-performance model that includes the final grade in a transformed feature has effectively been given the answer. A causal feature-availability table should list when every input is available, whether it is influenced by the outcome and whether its measurement process will exist at inference. High feature importance cannot rescue a leaked feature.

For linear regression with predictions ŷ_i=w^T x_i+b and squared loss, the gradient with respect to w is proportional to ∑_i(ŷ_i-y_i)x_i. Gradient descent updates parameters opposite the gradient, but learning rate selection affects convergence. Scaling features may improve optimization conditioning. A logistic classifier uses a sigmoid to map a linear score into (0,1) and can be trained with cross-entropy; predicted probabilities still need calibration assessment. Do not assume a probability estimate is well calibrated simply because it falls between zero and one.

For a lab, train a small model on a synthetic relationship y=2x+1+ε with a seeded noise generator. Compare train and held-out error, vary dataset size, and inject a perfectly leaked feature built from y. Observe the sudden test improvement when leakage affects both splits, then remove the feature and conduct an honest temporal or group split. The main teaching result is not a flashy accuracy number but a reproducible demonstration of how evaluation design changes the claim that can be supported.

## Unsupervised Learning
**Unsupervised Learning: conceptual explanation**

### Unsupervised learning and the meaning of discovered structure
Unsupervised methods find patterns without externally supplied target labels. Clustering groups observations under a chosen similarity measure, dimensionality reduction represents data in fewer coordinates, and density estimation models how observations are distributed. These methods answer different questions. Clusters do not automatically correspond to natural kinds, customer segments or causal categories; they are mathematical partitions that depend on representation, scaling and algorithm settings.

K-means minimizes the within-cluster sum of squared Euclidean distances ∑_i ||x_i-μ_{c_i}||² for a fixed number of clusters k. Its iterative procedure alternates assigning each point to the nearest centroid and recomputing centroid means. Each iteration does not increase the objective when steps are performed exactly, but the algorithm may reach a local optimum sensitive to initialization. Standardizing features changes the geometry and can entirely change cluster membership. A customer dataset containing annual spending in thousands and visit count in units may be dominated by spending unless scaling or a meaningful distance metric is selected.

Principal component analysis chooses orthogonal directions maximizing projected variance under a specified centering and covariance convention. The first principal component of a two-dimensional dataset aligns with the largest eigenvector of the sample covariance matrix. High variance does not guarantee predictive relevance or semantic interpretability. If a rare fraud signal lies in a low-variance direction, PCA truncation can remove it. Similarly, a visualization showing two separated blobs in two dimensions may obscure overlap in the original high-dimensional space.

Density-based clustering can handle irregular cluster shapes and mark isolated points as noise. Yet density parameters interact with data scale and sampling density, potentially splitting a meaningful group or merging adjacent ones. Internal clustering scores favor particular geometric notions of quality; a high silhouette score does not by itself show that discovered groups are useful or fair for a downstream decision.

Design an experiment with two concentric rings and two compact Gaussian blobs. Compare k-means and a density-based clustering method using appropriate settings. Report the objective each algorithm actually optimizes, its sensitivity to scaling and random seeds, and whether noise points are assigned or excluded. Check stability under perturbation and explain that agreement with synthetic ground truth is possible only because the data-generation rule is known. Applied clustering requires domain review before labels such as 'high risk' are attached to people.

## Reinforcement Learning
**Reinforcement Learning: conceptual explanation**

### Reinforcement learning, returns and temporal credit assignment
In reinforcement learning, an agent collects experience by acting in an environment and receiving reward. A Markov decision process has states S, actions A, transition probabilities P(s'|s,a), reward information and a discount factor γ. A policy π(a|s) specifies action probabilities. The state-value function V^π(s) is the expected discounted return from s while following policy π; the action-value Q^π(s,a) includes the first chosen action. Learning differs from ordinary supervised prediction because actions influence which data become available and which future states are visited.

For a deterministic chain with two moves to the goal, reward 0 for the first move and 10 for the second, discount γ=0.9 gives initial return 0+0.9×10=9 under a common time-indexing convention. If an alternative action pays 8 immediately and terminates, the goal-seeking path remains preferable. With γ=0.7, the delayed reward becomes 7 and the immediate action wins. This is not an empirical law; it demonstrates how discounting changes the encoded objective. Reward specification and terminal-state treatment must be explicit.

Q-learning updates Q(s,a) toward r+γ max_{a'}Q(s',a') using a step size α. In the tabular finite setting, convergence results require technical conditions including adequate visitation and appropriate learning rates; practical deep Q-learning does not inherit unconditional guarantees. Exploration methods such as ε-greedy occasionally choose random actions to learn about uncertain alternatives. Pure exploitation can remain trapped in a suboptimal policy when an initially promising action dominates early observations.

Off-policy evaluation attempts to assess a policy using data collected under another policy. Naive averages may be badly biased if important actions were rarely taken. Importance-sampling approaches reweight trajectories by action-probability ratios, but high variance can make estimates unreliable. The behavior policy's support must cover evaluated actions; no amount of arithmetic recovers outcomes for never-observed actions without additional modeling assumptions.

In a lab, implement a tiny gridworld with a terminal reward and a step penalty. Compare value iteration on the known model to learned tabular Q-values under several seeds. Record visits per state-action pair, learning rates, exploration schedule and a moving average of return. Introduce a reward bug that grants a positive score for repeatedly moving in place. The resulting policy can maximize its configured reward while failing the intended goal, demonstrating the difference between optimization and alignment with the task.

## Generalization
**Generalization: conceptual explanation**

### Generalization, regularization and trustworthy evaluation
Generalization is performance on examples drawn from the intended deployment distribution, not on the training records already seen. Error estimates must reflect sampling units: if many observations come from the same patient, machine or school, splitting individual rows can leak shared information across train and test sets. Group-wise splits can reveal how a model performs on entirely unseen entities. A model that performs well within one institution may not transfer to another because equipment, demographics, data collection practices or operational policies differ.

Regularization deliberately restricts model flexibility. L2 regularization penalizes squared coefficient magnitudes and can reduce variance in ill-conditioned linear models; L1 can encourage sparse coefficients. Early stopping monitors validation performance and halts training before overfitting grows. Data augmentation can improve invariance when transformations preserve the correct label, but an invalid augmentation introduces mislabeled examples. Flipping a handwritten digit image horizontally can change its identity, so not every geometric transformation is label preserving.

Evaluation metrics must align with the intended decision. Accuracy is useful for balanced classification under symmetric costs, but with 1% positive prevalence a classifier predicting 'negative' always reaches 99% accuracy while finding none of the positives. Precision TP/(TP+FP) and recall TP/(TP+FN) answer different questions, and both require attention to the selected threshold. The F1 score is the harmonic mean of precision and recall when defined, but does not incorporate true negatives or explicit operating costs. Report confusion matrices and prevalence alongside summary metrics.

Confidence intervals express uncertainty from finite evaluation data under modeling and sampling assumptions. If 80 successes are observed in 100 approximately independent trials, the sample success rate is 0.8, but claiming exactly 80% performance in all future conditions would be unjustified. Wilson or bootstrap intervals can be more informative than a single point estimate. Bootstrap procedures must respect dependence; resampling individual transactions when transactions cluster by user can understate uncertainty.

A rigorous benchmark specifies preprocessing, split construction, baseline, hyperparameter search space, random seeds, hardware conditions when runtime matters and error analysis. Evaluate subgroups where appropriate, rare edge cases and deliberate distribution shifts. Report both central tendency and variability across seeds. Never improve a model by repeatedly tuning against a supposedly untouched test set and then present that same test score as independent evidence. The honest performance claim is limited to the evaluation design used.

## Integrated Case Study and Model Limitations
**Integrated investigation for Learning foundations.** The examples below illustrate the precise mathematical and operational constraints of the unit.

### Case study: demand forecasting for a student transport service
A university shuttle operator forecasts passenger demand at each stop to allocate buses. Inputs include past ridership, academic calendar, weather and event information known at prediction time. A common failure is training on randomized rows from the same day and then reporting performance on nearby rows that share hidden conditions. A proper evaluation uses forward-chaining time splits and tests the model on later periods. If the semester calendar changes, the covariate distribution may shift in ways not captured by historical data.

Begin with a simple seasonal baseline that predicts the demand from the corresponding hour and day in a previous week. Compare it to linear regression and a nonlinear model under mean absolute error and a capacity-oriented cost. A forecast of 50 passengers when 80 arrive may be more damaging than forecasting 80 when 50 arrive. A decision model can assign asymmetric penalties to undercapacity and overcapacity, rather than optimizing a symmetric error metric and hoping the operational objective follows.

Include special event days held entirely outside the training period. Assess whether forecast intervals cover actual counts at the intended nominal rate, not just whether their mean width looks reasonable. Under exceptional uncertainty the service may reserve an extra bus or allow a human dispatcher to override the recommendation. That override should be logged so analysts can distinguish model performance from the performance of the combined human–AI system.

For an interactive simulation, generate a small synthetic demand series with trend, weekday variation and seeded noise. Vary the training window, forecast horizon and noise level and display both point predictions and held-out errors. Clearly label that the simulator is not trained on genuine passenger data. Test for leakage by attempting to include the actual future count as a feature; the feature-availability validator should reject it even if it would reduce error.

The final report should identify the predictive task, explain the operational loss function, compare baseline and fitted models and evaluate deployment risks such as sudden timetable changes. Good AI education should show when a simple baseline is competitive, not force a sophisticated model to win merely to illustrate its complexity.

### Research exercise: estimate a generalization gap rather than just train longer
Suppose a classifier scores 98% accuracy on training data and 72% on an untouched test set. The 26 percentage-point gap signals that behavior on new cases is substantially worse than on fitted examples, but the gap alone does not identify the cause. It could reflect an overly flexible model, a distribution shift between splits, label errors or preprocessing inconsistencies. A careful investigation begins by checking data lineage, duplicate records, group membership and whether labels were computed the same way in both sets. Training longer may reduce training error further while leaving the test problem unchanged.

For a reproducible experiment, generate two-dimensional synthetic points from overlapping class distributions with known random seeds. Train linear logistic regression and a more flexible model, such as a small decision tree. Evaluate each on a held-out set generated from the same parameters, then on a shifted set with moved class means. Show accuracy, log loss and confusion matrices separately. A flexible model may fit the training set perfectly yet generalize poorly when examples are scarce. A simple model can be preferable if it is more stable and meets the actual task requirements.

### Analyze model selection itself
Suppose an experimenter tries 50 hyperparameter configurations and repeatedly chooses the best score on one fixed validation set. Even if all models have equal true performance, random sampling noise can make the best observed validation score optimistic. This is selection bias. A separate untouched test set provides an independent final comparison after selection, but only if it truly remains untouched. If the researcher adjusts the pipeline after seeing the test results, the test becomes part of model development. Nested cross-validation is one method for estimating performance after hyperparameter search when data are limited, though correct grouping and temporal constraints still matter.

A well-designed lab should include a deliberately leaked feature. For a student-grade predictor, generate a feature 'final-score-bucket' from the target after the exam. Train with it and observe strong evaluation results when the leaky feature appears in both training and test tables. Then remove the feature and rebuild the pipeline, documenting the exact time when legitimate predictors would be available. The strong first score is not a discovery; it is an invalid forecasting setup. Data leakage can be less obvious when records from the same person appear in both splits or when global normalization parameters are computed before splitting.

### Loss and decision costs
Classification probabilities should support operational decisions, but the training loss and decision loss may differ. A bank transaction model may be trained with cross-entropy but deployed with a threshold chosen to balance review effort against missed fraud. Suppose false-positive investigation costs 5 units and a missed positive costs 100. Under perfectly calibrated probabilities and no other constraints, acting on a positive event probability p is favored when the expected cost of not acting, 100p, exceeds the expected false-positive action cost 5(1-p). Solve 100p>5(1-p) to obtain p>5/105≈0.04762. That threshold differs markedly from 0.5 because costs are asymmetric. Its validity relies on the simplified assumption that review eliminates the miss cost without adding harms.

### Validate with uncertainty
For a binary success rate measured on n independent cases, a raw estimate p_hat=k/n does not reveal its sampling uncertainty. With n=20 and 18 successes, a 90% observed rate is consistent with a meaningful range of underlying success probabilities; confidence intervals and repeated samples help communicate this uncertainty. If examples cluster by institution or individual, independence fails and simple binomial intervals may be too narrow. A quality report should identify the evaluation unit, sample provenance and any resampling method used.

A complete assignment compares two models on the same examples, includes paired error cases, checks calibration and presents at least one failure investigation with corrected data handling. Record random seeds, software versions and every transformation. Model development is not successful merely because an optimization loop converges; it succeeds only when a defensible evaluation shows useful performance on the intended decision problem.

### Bounded training guarantees versus deployment evidence
A convergence theorem often assumes fixed data distributions, smooth or convex losses, suitable learning rates and sufficient exploration or independent samples. A plotted decreasing loss curve cannot establish that those assumptions hold. Conversely, a failure to reach zero training loss does not automatically imply poor generalization: regularization may deliberately prevent exact fitting. In a simple regression experiment, report the training objective, held-out error and residual distribution. Change the data generator so the slope after deployment differs from training and observe prediction bias. Distinguish a programming bug, estimation noise and a genuine regime shift. Each calls for a different remedy: code correction, more representative data or a monitored policy adaptation.

### Worked question: Classification recall
A model finds 36 true positive examples and misses 9 true positive examples. Calculate recall, then explain whether precision is determined.

**Model the question**
Recall is TP/(TP+FN). Substitute TP=36 and FN=9; the denominator is the number of actual positive cases.

**Calculate or derive**
Recall=36/(36+9)=36/45=0.8, or 80%. Precision requires false positives via TP/(TP+FP), which the question does not supply.

**Check assumptions and boundaries**
A false-positive count of 0 would yield perfect precision, while 36 false positives would yield 50% precision. The same recall can coexist with very different precision.

**Answer:** Recall is 80%; precision cannot be determined.

### Worked question: Gradient step for a linear model
For single training pair x=2,y=5, a model predicts yhat=w x with w=1 and uses loss L=(yhat-y)^2/2. What is the derivative dL/dw and a step with learning rate 0.1?

**Model the question**
Compute prediction yhat=1×2=2 and residual yhat-y=-3. The chain rule gives dL/dw=(yhat-y)x for the half-squared-error loss.

**Calculate or derive**
Gradient=(-3)×2=-6. A gradient descent update is w_new=w-η gradient=1-0.1×(-6)=1.6. The derivative follows from the chain rule: differentiating half the squared residual leaves one factor of the residual, and differentiating the predicted value w times x contributes the input x. Subtracting a negative gradient moves the coefficient upward.

**Check assumptions and boundaries**
Verify the loss decreases for this example: at w=1, L=4.5; at w=1.6, prediction is 3.2 and L=1.62. This check does not establish global convergence for arbitrary learning rates.

**Answer:** dL/dw=-6 and w_new=1.6.

### Worked question: Discounted return and policy preference
An agent chooses between receiving 8 reward immediately and terminating, or receiving zero now and 10 next step. For which discount factor γ is the delayed option preferred?

**Model the question**
Under the stated convention immediate reward has weight one and the next-step reward has weight γ. Returns are therefore G_immediate=8 and G_delayed=10γ.

**Calculate or derive**
The delayed option is preferred when 10γ>8, or γ>0.8. At γ=0.8 the two returns tie; below it the immediate option is preferred.

**Check assumptions and boundaries**
This is a numerical preference under a simplified reward model. A risk of future failure or additional step costs would shift the threshold.

**Answer:** Choose the delayed reward when γ>0.8; tie at γ=0.8.
