# Unit 7: Evaluation

*Editorial draft; not approved for live publication.*

## Calibration
### Calibration

### Calibration concerns the meaning of predicted probabilities
A probabilistic binary predictor is calibrated if, among examples assigned probability around p under an appropriate grouping or limiting definition, approximately fraction p have positive outcomes. Accuracy and ranking are separate properties: a model can correctly rank high-risk cases while systematically assigning probabilities that are too extreme. Reliability diagrams aggregate predictions into bins, but the chosen bins, sampling variability and class rarity affect their appearance. Calibration is distribution-dependent; a model calibrated on one population may become miscalibrated after prevalence or feature relationships change.

The Brier score is the mean of (p_i-y_i)² for binary labels. Log loss heavily penalizes confident wrong predictions, while Brier is bounded for p in [0,1]. Both are proper scoring rules when appropriately defined, yet finite-sample estimates are noisy. Post-hoc procedures such as Platt scaling or isotonic regression require a held-out calibration dataset not reused for the final evaluation. An isotonic fit can overfit with few examples because it is flexible.

Suppose predictions are .9, .6 and .2 for labels 1,0,0. Brier squared terms are .01,.36,.04; the score is .41/3≈.1367. Thresholded at .5, this model makes one mistake out of three, for accuracy 2/3. Different probability assignments can preserve the same classifications and accuracy while changing Brier score. This distinction matters in applications where action thresholds depend on accurate absolute risk.

### Reliability experiment
Group predictions into enough bins to reveal structure without leaving almost-empty groups. For each bin, display mean predicted probability, observed event fraction and uncertainty about the fraction. Compare overall calibration against clinically or operationally important subgroups. A low aggregate calibration error can hide group-specific overconfidence if errors cancel. Freeze the calibration transformation before testing and state the target population for any reliability claim.

### Reliability diagrams with sparse bins
A calibration plot dividing predictions into ten equal-width bins can produce nearly empty extreme bins when the model rarely predicts high probabilities. A plotted observed fraction of 100% from one positive example is not reliable evidence of perfect calibration. Display bin sample sizes and uncertainty intervals, and consider adaptive-count bins for a descriptive check. Calibration estimates depend on the evaluation population. When base rates change, an unchanged model may no longer be calibrated, even if score ranking persists. Compare proper scoring rules such as log loss and Brier score alongside the plot. A calibration-correction model must be fitted on a separate calibration set, then evaluated independently. Repeatedly trying smoothing and binning variants until the final plot appears flattering is a form of adaptive analysis, not a validation procedure.

## Leakage
### Leakage

### Leakage is an invalid information path, not a high correlation
Data leakage occurs when information unavailable at prediction time, or information from intended holdout samples, affects model fitting or selection. Classic examples include a patient outcome embedded in billing codes entered after diagnosis, duplicated product images across train and test, or computing feature selection using the whole dataset before cross-validation. Some of these leaks remain even when the target column is correctly removed. Proper evaluation therefore requires understanding feature generation and entity relationships, not simply calling a random train-test split utility.

Temporal leakage can arise from rolling statistics computed with a centered window. A seven-day moving average centered at time t includes days after t, so it cannot be used for a prediction made at t. Group leakage arises when one underlying item has many near-duplicate views and the split treats them as independent observations. Preprocessing leakage arises when global transformations reveal test distribution information to the training pipeline. These violations produce optimistic error estimates and may mask genuine modeling weaknesses.

Leakage diagnostics include checking all feature timestamps relative to the decision timestamp, hashing near-duplicate assets, splitting by subject or source, and comparing scores under progressively stricter partitions. An unexpectedly perfect score should trigger investigation before celebration. However, a strong score is not itself proof of leakage; some genuinely easy tasks are nearly deterministic. Conversely, poor scores do not establish a clean experiment.

### Split falsification
Create a synthetic dataset with ten people, five repeated rows per person, and a subject identifier correlated with the label. Random row splitting likely permits subject memorization; leave-one-person-out splitting blocks that shortcut. Compare a model using identity with one using only measurement features. Then introduce a post-outcome timestamp and verify a feature-store guard rejects it. Document the mechanism by which the contamination enters; merely observing a score drop does not uniquely identify the offending feature.

### Identity fingerprints and near-duplicate leakage
Removing explicit subject identifiers does not necessarily prevent memorization. An image may contain device borders, timestamps or background equipment unique to one source; numerical sequences may preserve characteristic noise signatures. Near-duplicate detection can use hashes for exact copies and perceptual similarity or embedding distances for modified copies. When creating a group split, identify the underlying entity rather than trusting the row key, which may be different for every visit. Compare model scores after blurring metadata regions or dropping stable device fingerprints; a large drop can reveal reliance on shortcuts but does not by itself identify the only leakage channel. A leakage investigation should preserve examples and timestamp evidence so another analyst can reproduce the finding. Statistical independence is a property of the collection and deployment goal, not something automatically supplied by a machine-learning library.

## Class Imbalance
### Class Imbalance

### Class imbalance changes the relevance of ordinary accuracy
When positive events are rare, a classifier that always predicts the majority class can have high accuracy while identifying no important events. For prevalence 1%, predicting all negative yields 99% accuracy and zero positive recall. Precision depends not only on sensitivity and specificity but also on base rate. With prevalence .01, sensitivity .9 and false-positive rate .05, precision is (.9×.01)/(.9×.01+.05×.99)=.009/.0585≈.1538. A classifier with apparently good sensitivity can therefore create mostly false alarms in low-prevalence settings.

Use confusion-matrix counts with a defined decision threshold: true positives, false positives, false negatives and true negatives. Recall is TP/(TP+FN), precision is TP/(TP+FP), and specificity is TN/(TN+FP). F1 summarizes precision and recall but ignores true negatives and does not encode asymmetric domain costs. Precision-recall curves are especially informative for rare positive classes, though comparisons across populations with different prevalence need care. ROC AUC is a ranking summary, not a complete workflow metric.

Class weighting, focal losses, oversampling and synthetic-example generation alter what the training algorithm emphasizes. They do not manufacture information about rare conditions. If duplicated minority examples appear on both sides of a split, evaluation becomes contaminated. Oversampling must happen only inside the training fold. Calibration can change when training class proportions differ from deployment proportions; always evaluate probability quality on a representative test distribution.

### Workload calculation
Suppose 10,000 events include 100 genuine positives. At 90% recall, the system finds 90 and misses 10. With a 5% false-positive rate among 9,900 negative events, it generates 495 false alerts. Precision is 90/(90+495)≈15.38%, meaning a reviewer must process 585 alerts to find 90 positives. If each alert costs five minutes, the alert workload is 2,925 minutes. A useful acceptance criterion states available reviewer capacity rather than only maximizing F1.

### Precision under changing prevalence
For binary classification, precision = sensitivity×prevalence / [sensitivity×prevalence + false-positive-rate×(1-prevalence)]. This formula makes base-rate dependence explicit. Take sensitivity .9 and false-positive rate .05. At prevalence .01, precision is roughly .154; at prevalence .1, it becomes .09/(.09+.045)=2/3. No classifier operating characteristic changed, yet precision increased dramatically because positive events became more common. A benchmark reporting precision without prevalence and decision threshold can therefore mislead stakeholders comparing locations or time periods. Calculate expected alerts per thousand observations for several prevalences and compare with reviewer capacity. If prevalence changes after deployment, examine whether probability calibration and threshold policy remain appropriate; blindly reusing a threshold may cause workload spikes or missed events.

## Uncertainty Estimation
### Uncertainty Estimation

### Uncertainty estimates need a definition of what varies
A model's predictive uncertainty may reflect observation noise, missing features, parameter estimation, model disagreement or changing environments. The terms aleatoric and epistemic are commonly used for irreducible conditional outcome variability and uncertainty from limited knowledge respectively, but the boundary depends on what information and model class are considered available. An ensemble disagreement measure is not a mathematically complete uncertainty distribution. A softmax maximum of .99 is not automatically 99% confidence that the answer is correct.

Prediction intervals target outcomes, whereas confidence intervals often target estimated parameters or mean responses. In linear regression, a prediction interval for a new observation is wider than a confidence interval for the conditional mean because it incorporates individual noise. Bootstrap intervals resample according to a declared sampling design; naïve resampling of dependent time-series rows may be invalid. Conformal prediction can obtain marginal coverage guarantees under exchangeability and a fixed calibration procedure, but those guarantees generally do not imply conditional coverage for every subgroup.

Suppose a method claims 90% marginal coverage and is evaluated on 200 exchangeable future cases. One can inspect the fraction of outcomes inside its intervals, but the empirical fraction need not equal exactly .90 because sampling variation remains. Assess average width, group-specific coverage and failure under changes of distribution. Very wide intervals can achieve coverage while being operationally useless; a sharp interval that frequently misses is also inadequate.

### Calibration-set discipline
Train the model without using the conformal calibration examples, choose nonconformity scores on the calibration set, and reserve independent evaluation observations for reporting coverage. In a temporal application, identify whether exchangeability is plausible; drift can invalidate a distribution-free coverage claim. Simulate a positive shift in target mean after calibration and record both empirical coverage and width. Distinguish observed degradation from the conditions under which the original guarantee was proved.

### Group coverage versus marginal interval coverage
A 90% marginally valid prediction interval can have 98% coverage for a common easy subgroup and 50% coverage for a rare difficult subgroup while still approaching 90% overall under suitable group proportions. To see the possibility, suppose 80% of cases are easy and have 98% coverage, while 20% are difficult and have 58% coverage. Aggregate coverage equals .8×.98+.2×.58=.9. Report disaggregated coverage with counts, especially for safety-critical groups. Increasing the interval width for everyone might restore difficult-group coverage but waste resources for easy cases. Group-conditional methods can require larger calibration samples and additional assumptions; tiny subgroup sizes make guarantees difficult. Explain precisely whether the interval covers a future individual outcome, a conditional mean or a model parameter.

## Integrated technical investigations and review
# Integrated investigation for Evaluation

### Interpreting scores under finite samples
An evaluation metric is an estimate built from a particular sample, not a property engraved in a model. If a test set contains only five positive events, one extra missed event changes recall by twenty percentage points. Confidence intervals based on a binomial approximation may become inaccurate in extreme small samples; exact or carefully designed resampling methods can give more honest uncertainty. In grouped data, uncertainty about generalization to new sites depends on the number of sites, not merely the count of repeated observations.

Comparing two models on paired test examples is usually more efficient than treating their evaluations as independent because their errors are correlated. Compute per-example score differences and summarize those differences with a method suited to the sampling design. If one model is tested on an easier period, the comparison is confounded. Repeatedly searching across dozens of thresholds on one tiny validation set induces optimism; use a separate final test or nested selection procedure.

### When calibration and discrimination disagree
A model that assigns 0.9 to every positive and 0.8 to every negative perfectly ranks positive cases above negatives in a clean dataset, yet may be badly calibrated because an 0.8 score incorrectly implies high positive event frequency among negatives. A monotone transformation of scores preserves ranking and AUC while changing absolute probabilities. Cost-sensitive decisions using a simple threshold derived from probability require calibration, so ranking excellence alone is not enough. Conversely, a constant predictor equal to overall prevalence can be calibrated in an aggregate sense but have no useful individual ranking power.

This difference creates multiple possible improvements. Temperature scaling may soften logits without changing ranking; collecting better features may improve separation; label definition changes can shift both. A useful evaluation displays AUC or another ranking measure alongside proper scoring rules and subgroup calibration. It also reports decision workload at actual thresholds, because a system can be good statistically while creating too many alerts for a small team.

### Selective labeling and verification bias
In a fraud system, human investigators examine transactions already flagged by an old model. Confirmed fraud labels are therefore more common in investigated transactions, and uninvestigated cases may never receive definitive outcomes. Treating uninvestigated transactions as clean creates verification bias. An ostensibly unbiased final test set drawn from the same selectively investigated stream may reproduce the bias. Random audits of ethically permissible samples or careful missing-outcome modeling may be needed to estimate true detection performance.

For a medical screen, only high-risk patients may receive definitive diagnostic tests, creating a similar problem. An observed sensitivity estimate among verified patients need not equal population sensitivity. Document the pathway by which an outcome becomes known and analyze whether missingness is plausibly independent conditional on observed variables. If it is not, avoid overly precise population claims.

### Data-adaptive interval estimates
A conformal prediction method often uses nonconformity scores computed on calibration examples, then selects a quantile designed for marginal coverage under exchangeability. The quantile index has finite-sample details, including a ceiling operation and possible infinite upper limit at small calibration sizes. Simplifying the procedure to an arbitrary empirical percentile can lose the guarantee. The method wraps a base predictor but does not require the base model to be perfectly specified; it does require the calibration exchangeability condition or an appropriate modified method.

Marginal coverage is an average statement over the target distribution. It can hide poor coverage on a rare subgroup. Report both pooled and subgroup coverage where sample sizes permit. For serial data, time dependence and regime shifts may break exchangeability, so conformal intervals can under-cover after a change. Weighted or adaptive variants have their own assumptions; none should be described as universally distribution-free under arbitrary shift.

### Monitoring relevance at a fixed resource budget
Suppose investigators can check 50 transactions per day. A test report should include precision-at-50, number of missed verified cases, expected cost under the business's declared utility model, and the stability of these measures across days. F1 may favor a threshold producing 500 alerts, but that setting cannot be used without additional staffing. A lower recall at a feasible threshold may be operationally necessary, and the tradeoff should be explicit. When probabilities are calibrated, risk-ranking policies can be compared with threshold policies subject to capacity constraints.

A deployment experiment should start in shadow mode, logging predictions without changing investigative allocation. Once the model acts, its decisions affect which cases become investigated and labeled. Future observational metrics are then entangled with the policy itself. Continued evaluation may require reserved audit samples or controlled policy experiments to preserve identifiability of the effect on downstream outcomes.

### Safe interpretation of fairness breakdowns
Group-specific metrics can reveal harms but also produce noisy estimates from tiny cohorts. Report numerator, denominator, confidence interval, sampling dates and label quality. Be wary of Simpson's paradox: aggregate rates may reverse when stratified by a relevant variable. A fair evaluation does not simply choose the metric that shows the smallest disparity; it identifies which mistakes matter to affected people and which changes are legally and ethically permissible. Automated fairness scores do not resolve normative tradeoffs or institutional accountability.

### Statistical significance versus practical usefulness
An improvement can be statistically detectable but operationally trivial. On a huge dataset, a reduction of mean error from 5.000 to 4.995 may achieve a narrow confidence interval while saving almost no resources; on a tiny dataset, a large apparent gain may be too uncertain to trust. Define a minimum meaningful improvement before tuning models. Use paired evaluation when candidates predict the same observations, and resample the correct independent units. If outcomes are clustered by patient or machine, rows are not independently informative. Report the full distribution of errors including high-cost tails, not only averages. Evaluation should explicitly distinguish score estimates, decision costs, calibration and uncertainty. Avoid declaring a model better merely because it wins one metric after many unreported experiments. A practical decision incorporates performance, inference costs, fairness, safety and the ability to monitor and correct errors after deployment.

### Worked question: Binary Brier score
Three probability forecasts are p=(.9,.6,.2) with observed labels y=(1,0,0). Compute binary Brier score and 0.5-threshold accuracy.

**Model the question**
Brier score is average squared difference between forecast probability and binary outcome. Thresholded predictions are 1,1,0 using threshold .5.

**Calculate or derive**
Squared errors are (.9-1)^2=.01, (.6-0)^2=.36 and (.2-0)^2=.04. Sum .41; divide by three to get about .136667. Predictions match first and third labels but not second, giving accuracy 2/3.

**Check assumptions and boundaries**
Another model could have identical thresholded predictions but different probabilities, changing Brier score while leaving accuracy fixed. Evaluate calibration on representative held-out data; three examples cannot establish reliable calibration.

**Answer:** Brier score≈0.136667; accuracy≈66.67%.

### Worked question: Precision under rare events
There are 10,000 cases, including 100 positives. A classifier detects 90 positives and has a 5% false-positive rate among the remaining 9,900 negatives. Calculate precision and review workload.

**Model the question**
True positives are 90; false negatives are 10. False positives are 0.05×9,900=495, under the stated rate.

**Calculate or derive**
Precision=90/(90+495)=90/585≈.153846, or 15.38%. The system produces 90+495=585 alerts. Even with recall 90%, most alerts are false because positive events are rare.

**Check assumptions and boundaries**
If reviewer capacity were only 100 alerts per day, this threshold would be operationally infeasible. The exact alert count is expected if the rates are population probabilities; observed finite-sample counts fluctuate.

**Answer:** Precision≈15.38%; approximately 585 alerts, of which 495 are false positives.

### Worked question: Prediction interval versus confidence interval
A regression model estimates mean outcome 10 with standard error for the estimated mean 1 and independent future outcome noise standard deviation 3. Under normal approximation, compare approximate 95% confidence and prediction interval half-widths.

**Model the question**
A confidence interval for the mean uses SE_mean=1. A prediction interval for a future individual outcome must combine uncertainty in the mean and the additional outcome noise, giving sqrt(1²+3²)=sqrt(10).

**Calculate or derive**
Approximate 95% mean half-width is 1.96×1=1.96. Prediction half-width is 1.96×sqrt(10)≈6.198. Intervals centered at 10 are roughly [8.04,11.96] for the conditional mean and [3.80,16.20] for an individual outcome.

**Check assumptions and boundaries**
These normal approximations assume the uncertainty components are correctly estimated and independent in the stated way. Small-sample regressions can require t-based critical values and leverage terms. Neither interval is automatically valid under distribution shift.

**Answer:** Mean interval half-width≈1.96; individual prediction interval half-width≈6.20.
