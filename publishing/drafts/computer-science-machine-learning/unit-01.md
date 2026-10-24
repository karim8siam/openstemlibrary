# Unit 1: Learning formulation

*Editorial draft; not approved for live publication.*

## Targets
### Targets

### A target is a measured construct, not simply a column
Supervised learning begins with a decision about what quantity a system is supposed to predict. A numerical target might be the number of kilowatt-hours a building consumes tomorrow; a categorical target might say whether an image contains a bicycle. Those labels are not automatically ground truth. A utility company may revise meter readings, a hospital may record diagnoses with imperfect coding, and an inspection dataset may record only defects that human inspectors noticed. The mathematical variable Y is the observed label; the underlying scientific quantity of interest is often a different latent variable. A reliable study documents how one is inferred from the other.

Define the prediction-time information boundary before training. If the task is to predict tomorrow's demand at 18:00 today, the features may include weather forecasts issued by 18:00 but not tomorrow's realized temperature. Similarly, predicting a loan's default at origination cannot legitimately use the number of overdue payments recorded after origination. Including such information is target leakage even if the column is statistically predictive. A high validation score obtained with impossible future information is not evidence of a deployable forecast.

Targets also determine loss and evaluation. For a real-valued demand forecast, squared error penalizes large misses quadratically while absolute error treats a five-unit miss as five times a one-unit miss. For an emergency alarm, the business may value missed dangerous events much more than harmless false alarms; an unweighted accuracy metric can conceal the tradeoff. When labels have uncertainty, keep the distinction between irreducible outcome variability and annotation disagreement: the same recorded event can legitimately receive different labels under competing definitions.

### Design notebook
Create a label specification with observation time, prediction time, measurement mechanism, missingness rules, class taxonomy, and acceptable delay. Check ten randomly selected examples by reconstructing the information available at prediction time. For a binary label, plot prevalence by calendar period and data source; a sudden jump may reveal a recording change rather than an epidemiological shift. Record two plausible alternative label definitions and which decisions each definition supports. The conclusion is a target contract that future data pipelines can test rather than an assumption buried in model code.

### Label disagreement and ground-truth adjudication
When several annotators disagree about a target, majority vote is not the only defensible resolution. One can retain the full distribution of annotator judgments, ask a specialist to adjudicate ambiguous cases, or redefine the target to a more observable event. Suppose five independent inspectors classify a photograph: three call it damaged and two call it normal. A binary majority label discards the 40% disagreement. A probabilistic label of 0.6 retains descriptive uncertainty about those five judgments, but it is not necessarily the true physical probability of damage because annotators may share biases. Compare agreement rates by lighting and device model to uncover systematic disagreement. If uncertain labels concentrate in one site, blindly removing them can damage fairness and future performance. Construct an uncertainty policy that routes unresolved examples to review. A genuine learning evaluation should state whether predictions are being compared against consensus judgments, adjudicated defect measurements, or verified later outcomes. These targets are not identical, and apparently contradictory models may simply optimize different definitions of success.

## Features
### Features

### Representations determine what a learner can see
Features are transformations of available observations into numerical or categorical inputs. A table with age, sensor temperature, and region cannot encode everything about the person or machine. The function phi(raw observation) is a modeling choice: a linear learner can only assign direct additive contributions to supplied features, whereas a nonlinear learner may discover some interactions. Feature engineering can expose domain structure but can also inject unsupported assumptions. For example, converting a time stamp into hour-of-day sine and cosine coordinates preserves cyclic proximity between 23:59 and 00:01, while treating the hour as an unscaled integer creates a false discontinuity.

A measurement must have units and provenance. If one temperature sensor reports Celsius and another reports Fahrenheit, naïve concatenation manufactures a distribution shift. If a categorical variable is expanded into one-hot vectors, the model must define what happens to categories appearing only after deployment. Scaling numeric variables often improves gradient-based optimization; fit the scaler on training data, then transform validation and test data with exactly those learned parameters. Fitting normalization on all data allows information from the held-out distribution to influence training decisions, even when no target is used.

Missing data is not one phenomenon. A broken sensor can be missing completely at random, readings may disappear at low battery charge, and expensive laboratory tests may be ordered only for severe cases. The latter mechanisms contain information and can bias complete-case analyses. Replacing all missing values with the mean erases the missingness mechanism. Compare complete-case, imputation-with-indicator, and domain-aware models while preserving the validation boundary. High-cardinality identifiers deserve scrutiny because they can memorize subjects rather than represent stable relationships.

### Representation lab
Take a small energy-use dataset with raw timestamp, appliance state, and room temperature. Build three feature sets: raw hour integer; cyclic time coordinates; and cyclic time plus lagged appliance load available at prediction time. Use the same chronological split, model family and hyperparameter budget for all three. Compare holdout error and residuals around midnight. Alter the evaluation period to a holiday week and observe whether apparently useful periodic features generalize. Document that better cross-validation performance of one representation does not prove it captures the physical mechanism.

### Feature lifecycle under revisions
Feature engineering must account for transformations being revised after training. Imagine a geographic service replacing region codes 01–20 with alphanumeric identifiers. An ordinal encoding stored only as an array position may silently map a new code to a previously used coefficient. A versioned vocabulary maps known categories by explicit names and reserves a tested policy for unseen ones. Similarly, a winsorization threshold estimated on historical values must be stored as a fitted parameter, not recomputed dynamically on each inference batch. Dynamic recomputation would make the same input produce different outputs depending on what other requests happened to arrive at the same time. In a reproducibility exercise, feed the same observation through separate batches with distinct companion records and verify invariant results. If the result changes, determine whether the model intentionally uses batch context or whether preprocessing is unexpectedly stateful. Feature engineering is successful only when its numeric outputs preserve the intended semantics across training, evaluation and serving.

## Risk Functions
### Risk Functions

### Empirical risk versus decision risk
A learner selects model parameters theta by minimizing a sample average loss: Rhat(theta)=(1/n) sum_i L(f_theta(x_i),y_i). The quantity estimated by this average depends on the sampling distribution. If a factory trains only on high-quality cameras but deploys to dim workshops, low empirical risk need not imply low deployment risk. The population objective is R(theta)=E_{(X,Y)~P}[L(f_theta(X),Y)], where the expectation involves the target operating environment. Generalization analysis asks how well the training estimate transfers to that expectation under stated assumptions.

Loss functions encode geometry and incentives. With squared loss, a single large residual contributes its square, making least squares sensitive to unusual observations. Absolute loss has a kink at zero and is more resistant to a few extreme outcomes. Binary log loss rewards calibrated probabilities when the model is correctly specified and the sample matches the target distribution; it can assign a very large penalty to a confidently wrong prediction. A zero-one loss directly counts misclassifications but is discontinuous, so many training methods use a smooth surrogate. Optimizing a surrogate and deploying a thresholded decision are distinct operations that must both be evaluated.

Consider two forecasts for actual values 2, 4, and 14. Model A predicts 3, 5, and 10; model B predicts 1, 3, and 12. Squared-error totals are 1+1+16=18 for A and 1+1+4=6 for B. Absolute-error totals are 1+1+4=6 for A and 1+1+2=4 for B. The ranking agrees in this case, but the relative weights on the last error differ. To see divergence, introduce one severe outlier and several modest misses and explicitly recompute both losses; do not assert that losses always rank models identically.

### Objective audit
State whether every observation receives equal weight, whether measurements are independent, and whether an intervention affects the observed labels. Evaluate at least three losses on the same predictions, with units for each metric. Simulate five percent gross label corruption and measure the change in optimum. A risk curve is not a certificate of causal validity; low prediction loss may coexist with harmful decisions if the action triggered by a prediction is specified incorrectly.

### Weighting observations without making up certainty
Some datasets overrepresent easy observations because they were collected more frequently. A weighted empirical risk Rhat_w=sum_i w_i L_i/sum_i w_i can target a different population when weights approximate a defensible sampling correction. However, weights can be unstable if a rare observation receives an enormous inverse-probability factor. Define effective sample size n_eff=(sum_i w_i)^2/sum_i w_i²; it is at most the raw sample count for nonnegative weights and becomes small when one weight dominates. Consider weights 1,1,1,7. Their sum is ten, sum of squares is 52 and effective size is 100/52≈1.92 even though four rows exist. A metric computed from this heavily weighted sample should not be interpreted as having four independent equally informative observations. Clip extreme weights only with a clear account of the resulting bias and sensitivity. Report the unweighted evaluation as well as the weighted target-specific result to reveal what changed.

## Train–Validation Design
### Train–Validation Design

### Validation is an experiment about future data
Separating training, validation and test data is not a clerical step. It establishes an information firewall around model selection. Training data update fitted parameters, validation data choose hyperparameters and development decisions, and a final untouched test set estimates performance after the procedure is fixed. Repeatedly checking the test set while changing preprocessing or architecture adapts the process to that test set; although the test samples never enter a gradient calculation, the estimated error becomes optimistic.

A random split assumes the exchangeability relevant to deployment. For patient records, random splitting by record may place visits from one patient in both training and test subsets, allowing the model to exploit stable identity cues. Use a patient-group split for evaluating generalization to unseen patients. For monthly demand forecasting, train on earlier months and assess later months; shuffling future observations into training can leak distribution information. Spatial applications may require separating entire sites. The evaluation design should mirror the exact generalization claim rather than use random sampling by default.

Cross-validation reduces sensitivity to one partition but does not solve dependence or selection bias. In K-fold cross-validation, train K times on K-1 folds and score on the remaining fold; aggregate per-fold errors and report variation. With strong temporal autocorrelation, ordinary K-fold can reuse nearly identical events on opposite sides of the boundary. Rolling-origin validation retains time order and may require a gap between training and validation to stop label windows from overlapping. Nested cross-validation is useful when hyperparameter tuning itself is extensive, but it increases computational cost.

### Split-design protocol
Write one sentence describing the future predictions the system will make, then choose the splitting key: individual, group, site, or time. Save immutable identifiers for each partition. Test the absence of duplicate entity keys across train and test wherever that is required by the stated goal. For each fold, fit imputation, scaling, vocabulary and feature selection on its training portion only. Report the number of independent groups, not just the number of rows. A large row count can disguise a tiny effective sample size when rows are clustered.

### Model-selection optimism and final reporting
Suppose twenty feature sets are evaluated on one validation sample. Even if their true risks are identical, the lowest observed validation loss tends to be optimistically biased because it was selected from noisy estimates. Increasing the number of tuning trials increases this selection effect. A nested evaluation design contains tuning inside training folds and measures the entire selection procedure on outer test folds. For a time series, the outer splits must also respect chronological ordering. When computation is limited, reserve one late period and perform all tuning on earlier data rather than repeatedly inspecting that period. Disclose how many candidate configurations were tried, including failed attempts; otherwise readers may underestimate experimentation. A final score should be accompanied by a precise claim: the frozen procedure attained a measured error on a specified population and interval. It is not proof of uniform performance across every future market, climate or hardware revision.

## Integrated technical investigations and review
# Integrated investigation for Learning formulation

### Temporal provenance: the difference between event time and knowledge time
In live systems there are often two distinct clocks. Event time records when a physical phenomenon occurred, while ingestion or knowledge time records when the prediction system could first access the corresponding fact. A sensor may measure a value at 09:00 but upload it at 10:00; a fraud investigation may label an event weeks later. When reconstructing a training example for a forecast made at 09:30, the system cannot use a reading that was not ingested until 10:00 even if the event time says 09:00. A correct as-of join therefore checks both the observation time and the time at which the record became accessible. Backfilled records must be versioned rather than silently overwriting the original feature snapshot.

Consider a transit delay prediction service issuing estimates every five minutes. Planned timetables are known days in advance; GPS locations arrive with seconds of delay; incident reports may be written after a dispatcher intervenes. A 'delay cause' column entered after an incident can be almost perfectly predictive of the final delay and yet completely useless to the real-time predictor. The analyst should construct a feature availability matrix with one row per source and columns for event time, publication delay, revision behavior, and missingness. To test leakage, sample historic predictions and replay ingestion logs, refusing any feature value whose recorded availability time exceeds the decision time. This is more reliable than trusting a single dataframe produced after the event.

### Choosing a metric by downstream action
Suppose an emergency repair truck has capacity for exactly 20 calls each day. A probability estimator can be used to rank candidate repair events, but a model selected on average log loss may not be best at identifying the top twenty highest-risk calls if its ranking is weak in that tail. Define precision-at-20 and total expected avoided damage for the actual dispatch decision, while also measuring global calibration so probabilities retain interpretation. A capacity-dependent decision metric may not be smooth enough to train directly; surrogate losses are acceptable but must be evaluated against the operational goal. When damage estimates are uncertain, sensitivity analysis over plausible utility values is more honest than claiming an exact expected savings figure.

For example, if 1,000 candidate machines produce 30 true failures and the model's top twenty include twelve failures, precision-at-20 is 12/20=.6 and recall-at-20 is 12/30=.4. If another model's top twenty include ten failures, its ranking is worse for this operational task, even if it has slightly better mean squared probability error over all 1,000 machines. The comparison depends on who can be inspected, on the definition of failure, and on whether the model affects which failures become observed. A model need not be 'best' in every metric to be useful; it must be evaluated against a declared service contract.

### Error decomposition and sampling uncertainty
Many benchmark reports show one number even though model training and test sampling are stochastic. A fair comparison separates uncertainty from the finite test sample, uncertainty from the particular training sample, and variability from random initialization or data ordering. Bootstrap intervals over test observations can approximate one component of uncertainty if the data are independent at the resampling unit. For clustered sensor readings, resample independent devices or episodes rather than every second separately. Otherwise thousands of strongly correlated rows can create a misleadingly narrow interval.

A planned experiment should specify how much improvement would matter before seeing the results. If the existing baseline MAE is 5.0 units and the new model obtains 4.98 on a small holdout, a difference of .02 may be overwhelmed by ordinary day-to-day variation. Evaluate paired errors on exactly the same observations, inspect the distribution of per-item differences, and report confidence intervals for the average difference. Model selection should not continuously expand its list of candidate features until one yields a tiny favorable test result. That procedure effectively performs many unreported comparisons.

### Unseen labels, humans, and feedback
Labels used to train a classifier may be outcomes of a prior human process rather than independent observations. A hospital's diagnosis label is shaped by who received testing; a bank's default label is visible only for customers who were granted loans; and a recommendation system's click label depends on which item the old recommender displayed. Training on the observed labels can reproduce historical selection decisions and cannot identify counterfactual outcomes without stronger assumptions. A robust dataset description distinguishes 'not labeled', 'confirmed negative', and 'unknown', even when a convenient binary coding scheme would collapse them.

In the transit example, if dispatchers send help only to predicted severe delays, the future observed delays will be influenced by the prediction system itself. A model retrained naively may learn that high predicted risk correlates with unexpectedly short realized delay because successful intervention reduced it. That is not straightforward evidence that the original prediction was wrong. For intervention-aware evaluation, log actions as well as predictions and outcomes, and consider randomized or causal designs where ethically and operationally feasible. The separation between predicting a world and changing a world is a foundational boundary for machine learning.

### Documentation and review checklist
A deployable learning problem can be summarized in a compact protocol: target specification with time of availability; input feature contracts; the population expected at inference; loss and decision utility; independent training, tuning and evaluation partitions; acceptable metrics by subgroup; baselines; uncertainty estimates; and a data-retention policy. Every statement should be testable. 'The model generalizes' is too vague; 'MAE under 5 kWh for newly observed buildings in the June–August holdout' is measurable and bounded. The report should also state obvious exclusions, such as unprecedented policy changes, newly installed meter types and geographic regions absent from evaluation. These exclusions stop a classroom predictor from being mistaken for a universal promise.

### Formal target-population specification
A model's scope is best stated as a relationship between a prediction rule and a defined deployment distribution. Write a sampling frame describing which buildings, patients, machines or time periods can enter the system, including exclusions. A test set drawn only from early adopters may not estimate risk for the broader population. Sampling weights can sometimes correct known differences, but not unobserved mechanisms or complete lack of coverage. Distinguish a task where the same entities are encountered repeatedly from one where every entity is new. These tasks require different splits and can have different difficulty even with the same target column and model architecture. A final report should list the data-observation mechanism, label latency, feature availability cutoff, evaluation unit and intended action. This formal specification makes disagreement between investigators easier to diagnose: one team may legitimately be predicting immediate laboratory measurements, while another is forecasting human decisions after intervention. Neither score should be transferred to the other's objective without retraining and reevaluation.

### Worked question: Time-safe feature selection
A forecast is issued at 18:00 on Monday for energy use on Tuesday. Candidate inputs are Monday 15:00 outdoor temperature; the Tuesday weather forecast published Monday 16:00; actual Tuesday outdoor temperature published Tuesday evening; and a historical meter reading corrected Wednesday. Identify legitimate and invalid inputs.

**Model the question**
The prediction-time information set contains only records that existed at 18:00 Monday. A variable can describe Tuesday if it is a forecast already issued by the cutoff; event time in the future does not by itself prove a leak. Data availability must use publication timestamps rather than nominal observation dates.

**Calculate or derive**
Monday observed temperature and the Monday-issued weather forecast are available. Tuesday realized temperature and Wednesday correction are unavailable. Even if a retrospective database associates each value with Tuesday, that convenient alignment does not make the observations usable at the time of prediction.

**Check assumptions and boundaries**
Replay the training feature-generation pipeline with an as-of cutoff and check each value against record creation time. Late corrections must not silently replace what the model would have seen. The validation period should also be later than the training period because tomorrow’s forecast is inherently prospective.

**Answer:** The first two fields may be used; the latter two leak unavailable future information.

### Worked question: Loss-function sensitivity
Two candidate demand models have residuals A=(1,1,5) and B=(2,2,2). Compute mean absolute error and mean squared error and explain whether model ranking depends on the loss.

**Model the question**
For MAE, average absolute residual magnitudes. For MSE, square each residual before averaging. Units matter: MAE has the same units as the target, while MSE is in squared target units.

**Calculate or derive**
MAE(A)=(1+1+5)/3=7/3≈2.333; MAE(B)=6/3=2. MSE(A)=(1+1+25)/3=9; MSE(B)=(4+4+4)/3=4. Here both objectives favor B, although MSE penalizes the last large error much more strongly.

**Check assumptions and boundaries**
To show that rankings can change, compare residuals C=(0,0,4) and D=(1.5,1.5,1.5). MAE(C)=4/3≈1.333 <1.5, whereas MSE(C)=16/3≈5.333 >2.25=MSE(D). Loss rankings therefore depend on error distribution and cost assumptions.

**Answer:** B outperforms A on both losses; the constructed C/D example demonstrates a possible ranking reversal.

### Worked question: Group versus row split
A dataset includes 80 patients, each contributing five imaging visits. A random row split has 300 training records and 100 test records. Is the test score an independent estimate for performance on unseen patients?

**Model the question**
There are 400 rows but only 80 unique patient entities. In the described row split, visits from the same patient may appear on both sides, so patient identity and stable physical characteristics can be shared.

**Calculate or derive**
A model can exploit patient-specific imaging style, hardware artifacts or medical history indirectly even if explicit identifiers are excluded. The 100 test rows therefore need not represent 100 independent patients. Group all visits from each patient in one partition, then calculate a metric on patients or properly clustered observations.

**Check assumptions and boundaries**
A grouped split also requires enough patient diversity and an intended deployment target. If deployment is repeated predictions for known patients, a chronological within-patient task might be legitimate, but its performance claim must be stated differently. Separate test design from feature choice.

**Answer:** No; the row split can leak patient-level information. Use patient-group splits to test unseen-patient generalization.
