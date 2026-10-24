# Unit 2: Linear methods

*Editorial draft; not approved for live publication.*

## Linear Regression
### Linear Regression

### Linear regression as a projection problem
The linear model predicts yhat = beta_0 + sum_j beta_j x_j. With design matrix X and target vector y, minimizing squared residuals leads to the normal equations X^T X beta = X^T y. When X has full column rank, beta=(X^T X)^{-1}X^T y is a formal solution, but numerical software should not explicitly invert X^T X because it squares the condition number. QR factorization or singular-value decomposition is more stable, especially when predictors are correlated or scales vary greatly.

Geometrically, the fitted values X beta are the orthogonal projection of y onto the column space of X. The residual vector r=y-X beta is orthogonal to each column: X^T r=0, assuming an unconstrained least-squares solution. This is not a statement that errors in the population are independent of all predictors. It describes the algebra of the observed optimization problem. If the sample contains an intercept, residuals sum to zero; if no intercept is included, that property need not hold.

A coefficient represents a conditional association within the model and the data range, not automatically a causal effect. When two temperature sensors measure almost the same quantity, many coefficient combinations can generate similar predictions. Multicollinearity makes individual coefficients unstable while leaving some predictions reasonably accurate. Report confidence intervals or uncertainty when the inferential assumptions are justified, and avoid interpreting signs from arbitrarily standardized or encoded data without specifying the transformation.

### Numerical check
For two observations with x=0,2 and y=1,5, the exact line is yhat=1+2x; squared residuals are zero. Add a third point x=1,y=2 and calculate the least-squares optimum; the slope is 2 and the intercept becomes 2/3, yielding predictions 2/3, 8/3, and 14/3 at x=0,1,2. The sum of residuals is zero under the intercept model. A plotting simulation can vary slope and intercept, but it must distinguish the displayed finite sample from statements about unseen population relationships.

### Heteroskedastic errors and prediction intervals
Ordinary least squares can minimize squared error without errors having constant variance, but familiar textbook standard-error formulas may become invalid when conditional noise variance changes with predictors. If larger buildings have proportionally larger demand uncertainty, residuals may spread as floor area increases. Plot residual magnitude against fitted value and consider a heteroskedasticity-robust covariance estimator for coefficient inference where assumptions permit. Weighted least squares can be efficient when conditional variances are credibly known or estimated, but poor weights can worsen predictions. For prediction intervals, account for irreducible outcome variability and distinguish uncertainty in the estimated conditional mean. A bootstrap that resamples independent buildings may be defensible for new-building performance, while independently resampling daily rows from each building can ignore temporal dependence. Decide which uncertainty question matters before choosing the resampling unit. A line fitted accurately to a sample is not enough evidence for a narrow interval around future observations.

## Logistic Regression
### Logistic Regression

### Logistic regression models log-odds, not probabilities linearly
Binary logistic regression computes p(x)=1/(1+exp(-z)) with z=w^T x+b. The log-odds log[p/(1-p)] equals z, so a one-unit change in input x_j changes the log-odds by w_j holding other predictors fixed. Multiplying the odds by exp(w_j) is interpretable under a properly specified feature scale, but it does not translate into a constant probability increase because the sigmoid slope varies with the current score.

For an observed label y in {0,1}, the binary cross-entropy loss is -y log p-(1-y)log(1-p). Its derivative with respect to z is p-y, a useful cancellation that allows stable first-order optimization. Software generally uses a `logaddexp` or logits-based implementation rather than computing log(1-sigmoid(z)) naively when z is extreme. Overflow of exp and log(0) are implementation defects, not unavoidable properties of logistic regression.

A threshold such as 0.5 converts probabilities to classifications, but the best decision threshold depends on class prevalence, costs and calibration. A model with p=0.3 can rationally trigger a safety review if the cost of missing an event is sufficiently high. ROC curves describe performance over thresholds, while precision-recall behavior can shift strongly with prevalence. Training a logistic model on case-control sampled data may leave discrimination intact under some conditions while changing the intercept needed for probability calibration.

### Controlled example
At score z=0, p=0.5; at z=ln(3), p=0.75. If y=1, the loss falls from ln(2)≈0.693 to -ln(.75)≈0.288. If the true label is zero, the same change increases loss from ln(2) to -ln(.25)≈1.386. This asymmetry is exactly why the optimizer cannot improve loss by increasing scores for every observation. Plot loss against score separately for y=0 and y=1, then verify its gradient numerically using a small finite difference.

### Odds ratios and base-rate changes
The odds ratio exp(beta_j) summarizes the multiplicative change in conditional odds for one unit of x_j in logistic regression, holding other predictors fixed. This quantity depends on feature units and model specification; it is not the same as a risk ratio. For baseline probability .1, odds are 1/9. Doubling those odds gives 2/9, corresponding to probability 2/11≈.1818, not probability .2. At baseline probability .5, doubling odds yields probability 2/3. Thus a fixed odds multiplier creates a varying change in absolute risk. If the positive class becomes more common after deployment while conditional score distributions are otherwise stable, raw logistic probabilities can be miscalibrated even when ranking remains effective. Investigate prevalence and calibration separately. In a reporting exercise, convert three baseline risks to odds, apply a fixed multiplier, convert back, and display the differences. A coefficient should never be presented to nontechnical readers as a constant percentage-point change in probability without additional calculations.

## Regularization
### Regularization

### Regularization changes the objective, not merely the optimizer
Ridge regression minimizes ||y-Xbeta||²/(2n) + lambda||beta||²/2, commonly leaving the intercept unpenalized. Penalization discourages large coefficients and can stabilize predictions under collinearity. Lasso replaces squared coefficient magnitude with absolute magnitude, producing a nondifferentiable corner at zero and often sparse fitted coefficients. The word sparse is conditional: correlated predictors can lead to unstable selections, and a lasso coefficient of zero does not prove the variable lacks causal importance.

The effect of a penalty depends on feature scale. If x_j is measured in millimeters instead of meters, its coefficient changes by a factor of one thousand for the same prediction; applying a common coefficient penalty without standardization can create an artificial preference for some units. Fit standardization inside the training fold and keep the preprocessing attached to the model. Tune lambda by validation, recognizing that many nearby penalties can have practically indistinguishable performance.

From a Bayesian perspective, an L2 penalty corresponds to a Gaussian coefficient prior under a compatible likelihood and scaling convention, while an L1 penalty relates to a Laplace prior. This provides intuition about shrinkage, but it does not make a penalized point estimate equivalent to the complete posterior distribution. Report clearly whether uncertainty is from a sampling procedure, a posterior, or an empirical resampling method.

### Simple one-variable comparison
For one normalized feature with X^T X/n=1 and X^T y/n=3, unpenalized least squares gives beta=3. Under ridge penalty lambda=2 in the stated scaling, beta=3/(1+2)=1. Under an L1 penalty lambda=2, the soft-threshold solution is sign(3)max(|3|-2,0)=1. For lambda=4, lasso sets beta=0 whereas ridge returns beta=3/5. The two penalties are not interchangeable even when a particular case produces the same estimate.

### Penalization, missing variables, and interpretability
When two predictors are highly correlated, lasso may keep one and drop the other even though either could carry much the same predictive information. Under minor resampling, the selected variable can switch. A sparse coefficient table therefore describes one fitted representation, not a scientific proof about which variable caused the outcome. Stability selection repeats fitting across subsamples to assess how consistently variables enter a model; even stable selection remains associational without causal assumptions. Ridge can retain both predictors with shrunk coefficients, while elastic net combines L1 and L2 penalties. Compare selected-variable sets across several training subsets and calculate Jaccard overlap rather than relying only on a single chosen lambda. If the objective is interpretation, consider measurement reliability and causal study design, not simply sparsity. If the objective is prediction, emphasize holdout error and robustness under sensor changes. A penalty cannot repair a missing confounder or a target defined by a biased human decision process.

## Optimization
### Optimization

### Optimization, conditioning, and trustworthy stopping criteria
Gradient descent iteratively updates theta_{t+1}=theta_t-eta grad L(theta_t). On a convex differentiable objective with Lipschitz-continuous gradient, sufficiently small steps can decrease the objective, but neither convergence speed nor monotonic decrease is universal for arbitrarily large learning rates. The gradient is defined relative to parameterization and feature scaling. A shallow loss direction and a steep direction can make one global learning rate unsuitable; preconditioning and adaptive methods attempt to reduce this difficulty.

Batch gradient descent computes a full-data gradient each update. Stochastic gradient descent uses individual or minibatch examples, reducing computation per step but introducing sampling noise. An epoch is one pass over the chosen training observations, not a fixed number of parameter updates across datasets with different minibatch sizes. Shuffling example order may improve optimization but can conflict with sequence dependencies in an online or temporal process.

The learning rate interacts with weight decay, gradient clipping, momentum and normalization. Gradient clipping limits update magnitude or gradient norm and is useful for explosions, but can bias updates if applied too aggressively. Adaptive methods such as Adam normalize updates using estimated first and second moments; they do not eliminate the need to select a schedule or test generalization. A lower training loss is not always a better model: overfitting can lower training error while raising held-out risk.

### Reproducible optimization trial
Fit a linear predictor on x=2,y=5 with initial w=1 and loss (wx-y)²/2. The gradient is (2-5)×2=-6. With eta=.1, w moves to 1.6, and loss falls from 4.5 to 1.62. With eta=1, w jumps to 7 and loss becomes (14-5)²/2=40.5; repeated updates can diverge. Implement gradient checking against a central finite difference and vary learning rate on logarithmic axes. The experiment illustrates a local numerical property of a simple quadratic, not a universal recommendation for neural networks.

### Diagnosing divergence from step-size arithmetic
On the one-dimensional loss L(w)=(w-w_star)^2 with gradient 2(w-w_star), gradient descent obeys error recurrence e_{t+1}=(1-2eta)e_t. Its error magnitude contracts when |1-2eta|<1, equivalently 0<eta<1. At eta=.5 the method reaches the optimum in one step from any starting value for this exact quadratic. At eta=1 the error alternates sign without shrinking, and at eta>1 it diverges in magnitude. This simple recurrence explains why visual oscillations in a training graph may reflect a large step rather than a mysterious failure of deep learning. Multidimensional quadratics require considering Hessian eigenvalues, and nonlinear networks have changing curvature, so the numeric threshold is not transferable unchanged. Build a reference plot for eta=.1,.5,1,1.2 with a common initial error. Verify the recurrence against an independently coded loop. A numerical debug chart is useful only when the function being optimized and update convention are known.

## Integrated technical investigations and review
# Integrated investigation for Linear methods

### Conditioning and geometry of the least-squares landscape
Take a regression design with two nearly identical columns. The matrix X^T X contains large off-diagonal terms, and its smallest eigenvalue approaches zero as the columns become more collinear. Gradient descent updates can oscillate along a steep eigenvector while moving slowly along a flat one. On a quadratic loss, the spectral condition number of the Hessian describes this imbalance; preconditioning and feature scaling attempt to reduce it. A solver might produce accurate fitted responses but unstable coefficients because many nearby parameter vectors generate similar predictions.

Suppose x2=x1+epsilon with tiny independent measurement noise epsilon. A fitted model may assign +100 to x1 and -99.8 to x2, leaving a reasonable combined coefficient for observed paired values. When the relationship between sensors changes after one is recalibrated, predictions can become unreliable. Ridge shrinkage reduces the incentive for huge opposing coefficients, but may introduce bias. The right analysis compares prediction errors on a sensor-replacement holdout and coefficient sensitivity under perturbations, not simply the number of decimals printed by the optimizer.

### Bayesian interpretation is conditional on assumptions
Maximum likelihood chooses parameters that make observed labels comparatively plausible under a likelihood model. Adding a log-prior term creates a maximum a posteriori objective, but the resulting mode is just one summary of the posterior. For Gaussian observation noise and a Gaussian coefficient prior, ridge-like shrinkage emerges with scaling constants determined by the noise variance and prior variance. Changing the assumed noise distribution changes the connection: an L1 residual objective corresponds to Laplace-like errors, while a Gaussian residual model yields squared loss. One should not label a procedure 'Bayesian' merely because it uses a penalty inspired by a prior.

When actual uncertainty matters, posterior predictive intervals incorporate both residual variability and parameter uncertainty, provided the model and prior are credible. A ridge point prediction alone does not provide these intervals. Conversely, resampling-based uncertainty estimates can be useful without adopting a Bayesian probability interpretation. Students should write down their inferential target before choosing a method: best prediction, interpretable coefficient, probability interval or counterfactual effect.

### A full optimization debugging trace
Create a small design with X rows (1,0),(1,1),(1,2) and labels (1,3,5). The exact line y=1+2x has zero residual error. First verify its gradient numerically. Perturb the middle label from three to four, recompute the optimum analytically, and compare with QR least-squares output. Then standardize the non-intercept feature and observe the change in coefficient values and optimizer speed. The predictions expressed back in original units should agree when transformations and intercepts are handled consistently.

A common bug involves penalizing the intercept even though the intended objective says it is unpenalized. Test a constant target with every feature zero: the correct intercept should fit the target exactly for lambda>0 when only slopes are penalized, whereas a penalized intercept can be shrunk toward zero. Another bug comes from dividing data loss by n but forgetting that the penalty coefficient also has a convention, so lambda values cannot be compared across packages without checking definitions.

### Decision thresholds and score calibration
A logistic score and the intervention triggered by that score should be treated as separate artifacts. Suppose a warranty company must decide whether to send an inspector. Let the inspection cost be 20 units and the loss from missing a failure be 200 units. Under a simplified model where inspection perfectly prevents that failure and no other costs occur, inspection is favored when p×200 exceeds 20, or p>.1. A default threshold of .5 would ignore the organization's stated cost ratio. The threshold changes if inspections are imperfect, if a false alarm has social costs, or if labor availability is limited.

Threshold tuning on a validation period can overfit just like parameter tuning. Report a sensitivity curve showing how workload, precision, missed events and expected loss change across thresholds. If calibrated probabilities are required for the cost calculation, test calibration independently. A model can preserve an AUC while making poor expected-cost decisions because its absolute probabilities are biased. Recording only classification accuracy conceals this difference.

### Extrapolation and intervention caution
A linear predictor extrapolates its straight-line relation beyond the training range. This can be useful when domain physics genuinely supports linearity, but dangerous when mechanisms saturate. A house-price model may predict negative price at an extreme feature combination; logistic regression always produces values in [0,1], but that mathematical bound does not ensure good probabilities outside the observed feature domain. Add input-range monitors and report cases with high leverage or out-of-distribution feature combinations.

Coefficient interpretation is especially hazardous when actions are contemplated. A positive association between tutoring hours and examination score does not prove that increasing tutoring causes the same score increase: students who seek tutoring may differ in motivation or initial ability. Randomization or a credible causal identification strategy is needed for causal treatment claims. Linear prediction and causal linear models may share equations while making different assumptions. In a teaching project, challenge students to state which assumption bridges observation and intervention.

### Operational comparison
For a final linear-model laboratory, create a reproducible pipeline with a linear regression baseline, logistic classifier for thresholded outcomes, ridge and lasso variants, and a small nonlinear benchmark. Use consistent preprocessing rules and nested evaluation if extensive tuning occurs. Save coefficient stability across resamples, held-out errors, calibration, and model size. Plot learning curves as training sample size grows; a persistent train-validation gap suggests overfitting under the chosen split, while both errors being large suggests limited model class, weak features or irreducible target noise. These interpretations are hypotheses to test, not diagnoses guaranteed by curve shape.

### Units and parameterization as invariant checks
A well-implemented statistical pipeline should produce invariant physical predictions when only measurement units change, provided its transformations are updated consistently. If distance changes from meters to centimeters, the corresponding linear coefficient should change inversely so that fitted distances still produce identical outputs. Naively applying the old coefficient to the newly scaled data violates this invariance. Add a regression test with known example conversions. For logistic scores, the intercept and coefficient transform must preserve the linear predictor z for equivalent physical observations; the sigmoid then preserves probability exactly. The fitted penalty can complicate invariance if features are not standardized, which is one reason consistent scaling belongs inside model training. Explain to students that coefficient magnitude alone is not a scientifically comparable measure of variable importance across units. Model comparison should use output behavior, validation error, stability and uncertainty under declared parameterizations instead of ranking raw numerical coefficient sizes.

### Worked question: Least-squares line through two points
The points (0,1) and (2,5) must be fitted by yhat=b+w x with zero residual. Find b and w and verify both normal-equation residual conditions.

**Model the question**
At x=0 the prediction is b, so b must equal 1. At x=2 it must equal 5. Substituting gives 1+2w=5, hence w=2.

**Calculate or derive**
Predictions are 1 and 5; residuals are both zero. The intercept normal equation is sum residuals=0 and the slope equation is sum x_i residual_i=0, both satisfied. These properties also hold for a general unconstrained least-squares fit with full-rank design and an intercept.

**Check assumptions and boundaries**
Two points determine a line if their x values differ, but this gives no uncertainty estimate about future noisy points. A new measurement with x outside the training range is an extrapolation even though the formula remains defined.

**Answer:** b=1 and w=2, with zero training squared error.

### Worked question: Logistic probability and log loss
For a binary logistic model with score z=ln(3), calculate its positive-class probability and its binary cross-entropy for labels y=1 and y=0.

**Model the question**
The sigmoid transforms z into p=1/(1+exp(-z)). Since exp(-ln 3)=1/3, p=1/(4/3)=3/4.

**Calculate or derive**
When y=1, loss is -log(3/4)=log(4/3)≈0.28768. When y=0, loss is -log(1/4)=log 4≈1.38629. The two losses differ because the model confidently predicts the positive class.

**Check assumptions and boundaries**
Check normalization p+(1-p)=1 and note that z is an unbounded score, not a probability. Replacing log loss with classification error at threshold .5 would give zero-one loss 0 for y=1 and 1 for y=0, discarding the degree of confidence.

**Answer:** p=0.75; positive-label loss ≈0.2877 and negative-label loss ≈1.3863.

### Worked question: One-step gradient descent
For yhat=wx and L=(yhat-y)^2/2, take x=2,y=5,w=1. Compute the derivative and update w with eta=0.1; compare initial and final loss.

**Model the question**
Apply the chain rule: dL/dw=(wx-y)x. The prediction at the starting weight is 2 and residual is -3.

**Calculate or derive**
Gradient is (-3)×2=-6; new weight w=1-0.1×(-6)=1.6. Initial loss is (2-5)^2/2=4.5. New prediction is 3.2 and loss is (3.2-5)^2/2=1.62.

**Check assumptions and boundaries**
The loss decreases on this convex quadratic for the chosen step. A larger step can overshoot. The arithmetic does not verify general convergence with many correlated features or stochastic minibatches; it is a unit test for update implementation.

**Answer:** dL/dw=-6; updated w=1.6; loss decreases from 4.5 to 1.62.
