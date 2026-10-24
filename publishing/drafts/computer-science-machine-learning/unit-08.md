# Unit 8: Learning systems

*Editorial draft; not approved for live publication.*

## Data Pipelines
### Data Pipelines

### Data pipelines are part of the model's mathematical definition
A deployed learner consists of much more than a serialized matrix of weights. It depends on feature definitions, transformations, model code, category vocabularies, units, timezone rules, missingness defaults, and the availability of prediction-time data. A training pipeline may use a dataframe with columns in a fixed order while a serving pipeline receives a JSON object whose fields are reordered or missing. If code silently treats column positions as semantic identities, predictions can be catastrophically wrong without an exception.

A reproducible pipeline records raw data lineage, schema version, feature transformations, fit-time statistics, data-splitting rules, model parameters and validation evidence. Tests should reject impossible values and unknown feature schema versions. For a model expecting height in centimeters, a measurement in meters should not be quietly accepted as an unusually small person. Do not rely on machine-learning frameworks to discover semantic unit errors; add explicit domain checks.

Online and batch inference have different latency and consistency constraints. A nightly demand forecast may tolerate several hours of data processing, while a safety alarm requires a bounded end-to-end delay. A feature store can reduce training-serving mismatch, but only if event time, ingestion time and backfills are modeled correctly. Late-arriving records must not leak retrospective corrections into as-of-time features when replaying historical predictions.

### Serialization test
Export a preprocessing-plus-model artifact with an explicit input schema and a known test vector. Run inference before serialization, after local reload, and in a separate serving process; compare outputs within a fixed tolerance. Change feature order and confirm name-based mapping produces identical results. Remove a mandatory feature and verify the system rejects the request or invokes a documented fallback. Repeat with nonfinite numeric values and previously unseen categorical levels. These tests are part of empirical model correctness.

### As-of feature joins and delayed arrivals
Suppose a data warehouse stores measurements with event timestamp e and ingestion timestamp a. For a prediction made at time t, a valid historical feature must respect the intended event window and generally satisfy a≤t. Filtering only by e≤t can leak measurements backfilled after the prediction occurred. Build a small example table where one sensor reading has e=t-10 minutes but a=t+30 minutes, and prove that an as-of join using ingestion availability excludes it. Late data may still be useful for training labels or offline analysis, but it cannot be treated as a real-time input. Test timezone conversion, daylight-saving transitions in relevant regions, and duplicate updates with consistent ordering. Store exactly which feature version the service used for each production prediction so downstream error analysis is reproducible.

## Fairness
### Fairness

### Fairness metrics express distinct normative objectives
A model may produce different error rates across groups because of historical disparities, measurement noise, selection bias or differences in underlying populations. Demographic parity compares overall positive-decision rates, equal opportunity compares true-positive rates conditional on actual positives, and equalized odds compares both true-positive and false-positive rates. Calibration asks whether predicted risks match observed event frequencies. These are mathematically different constraints and can conflict when base rates differ, so satisfying one does not mean the system is universally fair.

For group A, suppose 30 of 40 actual positives are correctly flagged; true-positive rate is .75. For group B, 15 of 20 actual positives are correctly flagged; its true-positive rate is also .75. Equal opportunity holds on this sample even if the groups have very different false-positive rates or overall acceptance rates. Report counts and interval uncertainty: 15 successes in 20 trials provide less precise rate evidence than 300 in 400. Small denominator instability should not be obscured by percentages alone.

Fairness analysis requires a domain-specific theory of harm. A false rejection of a credit application and a false negative in a disease screen have different consequences and legal contexts. Protected attributes may require special handling, consent and data governance. Simply removing a sensitive column does not eliminate correlations through location, school or other proxies. Conversely, measuring disparities may require ethically and legally justified collection of group information.

### Structured audit
Identify who experiences benefits or harms from decisions, not merely from prediction error. For each group with adequate sample size, report prevalence, calibration, false-positive rate, true-positive rate and decision frequency. Evaluate whether a group metric changes over time. Specify whether interventions are evaluated on the same data or a separately randomized trial. A fairness dashboard can identify potential problems, but policy decisions require contextual judgment, legal review and affected-user participation.

### Fairness thresholds as policy choices
A risk score can be thresholded at one value for everyone or at group-specific values. These choices change selection rates, error rates and potentially legal consequences. There is no purely mathematical formula that determines the correct normative objective independently of application and jurisdiction. In a worked example, two groups have equal true-positive rates but different false-positive rates; equal opportunity holds while equalized odds does not. Altering thresholds can reduce one disparity while increasing another or changing resource allocation. Before selecting an intervention, identify affected populations, error costs, data quality and the decision-maker's authority. Keep technical evaluation separate from unsupported legal conclusions. If the model influences access to housing, jobs or credit, a domain-specific legal and ethical review is necessary in addition to an algorithmic audit.

## Distribution Shifts
### Distribution Shifts

### Distribution shift changes the question to which a model responds
Covariate shift refers to changes in P(X) while a relevant conditional P(Y|X) remains stable; label shift changes class priors P(Y) under a suitable stable class-conditional feature model; concept shift changes the relationship between features and targets. These labels simplify complex realities, and multiple changes can occur simultaneously. Detecting a shifted histogram does not reveal which causal mechanism produced it, nor whether predictive accuracy has changed.

A deployment may encounter new sensor hardware, changed regulations, seasonal behavior or strategic responses to model decisions. An input-distribution monitor might compare means, quantiles or multivariate distances; a performance monitor requires delayed ground-truth labels. If labels arrive months later, proxy metrics can provide partial early warnings but cannot certify accuracy. Statistical significance depends heavily on sample size; a tiny harmless shift can be statistically detectable in enormous streams, while a dangerous subgroup shift may be missed with sparse data.

Under genuine covariate shift and sufficient support overlap, importance weighting by P_target(X)/P_train(X) can reweight source examples, but large weights generate variance and support violations defeat the correction. Under label shift, class-prior correction can help if P(X|Y) is stable. These are conditional remedies rather than universal drift fixes. If concept shift changes P(Y|X), collecting new labeled data may be unavoidable.

### Shift experiment
Train a classifier on sensor values centered near zero. Evaluate on a synthetic population shifted by +1 input unit while keeping label generation fixed; compare accuracy and calibration. Then change the label-generation threshold while keeping feature marginals fixed. An input-only monitor may detect the first but miss the second even though predictive behavior changes. Plot performance against degree of shift, retain fixed random seeds, and state exactly how labels were simulated. The lab illustrates why monitoring feature drift is not equivalent to monitoring model quality.

### Support overlap in dataset-shift correction
Importance weighting under covariate shift uses P_target(X)/P_train(X). If the target population includes feature regions never observed in training, the ratio cannot be estimated from source outcomes there. No amount of sample reweighting creates missing labels or correct extrapolation. Diagnose overlap using feature ranges, neighbor distances and domain-classification models, remembering that high-dimensional support is hard to measure reliably. Even with overlap, large weights increase variance. Report effective sample size and sensitivity to clipping. If P(Y|X) changes, the covariate-shift assumption fails and weighted source risk need not equal target risk. A valid shift analysis explicitly distinguishes changes in observable features, prevalence and conditional label relation instead of treating every change as a generic 'drift score'.

## Model Monitoring
### Model Monitoring

### Monitoring measures performance and operational safety over time
After launch, a model should be treated as a changing sociotechnical system rather than a frozen research benchmark. Track input schema failures, missing-feature rates, prediction distributions, service errors, latency, data age and operating cost. Once reliable labels arrive, monitor appropriate quality metrics by time and subgroup. Distinguish a code release that changed feature processing from a population shift that changed customers. Both can alter model outputs, but they require different responses.

Design alerts using baseline variability and action cost. An alert every time a mean fluctuates creates fatigue; a threshold insensitive to subtle but severe degradation provides false security. Combining fixed guardrails with statistically informed change detection can help. For rare failures, track confidence intervals or sequential testing assumptions; repeated daily significance tests without a multiple-testing strategy can create many false alarms. A model rollback should include the associated preprocessing and feature definition versions, not only the weight file.

Retraining is not automatically an improvement. New labels might have changed definition, newly collected data may overrepresent dissatisfied users, and feedback loops may amplify the model's previous choices. A champion-challenger evaluation can compare a candidate against the deployed baseline on representative, independently labeled observations. Shadow deployments collect predictions without changing actions and allow latency testing, but may not reveal the intervention effects that would occur after the challenger controls decisions.

### Operational playbook
Specify which team owns each monitored metric, what constitutes a critical anomaly, and how to disable predictions safely. Inject corrupted sensor fields into staging and verify schema alarms trigger. Test a delayed label feed and confirm that dashboards display data freshness rather than silently reporting yesterday's accuracy as current. Record latency percentiles, not just the mean, and budget for tail behavior during load spikes. Demonstrate one rollback using a reproducible stored artifact and exact feature transformation version.

### Shadow deployment and feedback loops
A shadow model processes live inputs and logs predictions without controlling actions. This can test data contracts, serving latency and stability against current conditions. However, it cannot directly measure how users or equipment would respond if the shadow model's recommendations were followed. When a model enters control, outcomes become affected by its choices and the evaluation problem changes. A lending score that changes approvals also changes which defaults are observed, creating selection feedback. Record decisions, policy propensities where appropriate, interventions and later outcomes so retrospective analysis does not confuse observation with causal influence. A shadow model should have explicit data minimization and retention rules; capturing more production information is not automatically justified by research interest.

## Integrated technical investigations and review
# Integrated investigation for Learning systems

### Data lineage as a reproducible graph
A machine-learning result is reproducible only if a reviewer can reconstruct the training inputs, target labels, feature transforms and exact evaluation partitions. Record raw source identifiers and cryptographic checksums, transformation code versions, configuration parameters, fitted scaler statistics, vocabulary maps and model artifact hashes. A dataset can change without a code commit: an upstream provider may correct old entries or modify category encodings. Immutable snapshots or documented as-of data queries prevent silent drift in repeated experiments.

In large organizations, lineage is a directed graph from raw feeds through cleaning, aggregation and feature construction to final predictions. Each node should have an owner, schema contract, update cadence and allowed failure behavior. When an outlier appears, lineage helps determine whether it arose in a sensor, a timezone conversion, a new join key or the model. Without it, teams may retrain repeatedly to repair what is actually a data-engineering defect.

### Monitoring in the absence of immediate labels
Ground truth for long-horizon tasks may arrive months after the forecast. During that delay, schema validity, missingness, feature drift, score distributions and model agreement provide provisional health indicators. They cannot establish current accuracy without labels. An operations dashboard should display the date through which outcomes have been verified, and distinguish unobserved outcomes from genuine negatives. Backfilled labels may revise historical metrics; dashboards should record when such revisions occurred.

A shift in prediction distributions might be expected after a genuine seasonal change. Investigate rather than trigger automatic retraining on every alarm. Conversely, prediction distribution stability is not evidence of quality if the conditional relationship P(Y|X) has changed. For a revenue forecast, customers could spend less at every feature value while input variables remain distributed exactly as before; feature drift monitors could miss that concept shift entirely.

### Testing deployment symmetry
Offline evaluation typically calls a model with clean arrays prepared by data scientists. Production traffic includes malformed requests, unknown categories, absent values, duplicates, slow feature APIs and race conditions. Build contract tests that send known examples through both training and serving transformations. Compare the transformed feature vectors element by element before comparing final predictions. Test that serialized categories preserve their exact mapping and that feature order cannot silently change when JSON fields arrive in a different order.

Adversarial input tests should include negative quantities where forbidden, NaNs, infinities, timestamps in different zones, future dates and strings where numbers are expected. Some inputs should be rejected, others mapped to explicitly documented fallback values. A fallback prediction should carry a warning flag to downstream systems. Silent coercion may make a service appear reliable while systematically producing nonsense.

### Monitoring risk after interventions
When a model prioritizes pipelines for inspection, repaired high-risk pipes may fail less often. New training data thus reflect actions caused by prior scores. An apparent reduction in risk among previously high-risk items might demonstrate successful intervention rather than a faulty original model. Conversely, repeated surveillance of certain neighborhoods can yield more detected incidents there even if underlying physical risk is unchanged. Track intervention assignments, observation opportunities and reporting practices before interpreting disparities.

Causal inference is distinct from predictive accuracy. A model predicting where failures will be found under the current inspection policy need not identify where increasing inspection would prevent the most harm. The latter is a counterfactual treatment-effect question. Organizations should not silently use a predictive ranking as an allocation policy without assessing how allocation changes outcomes and who bears the costs.

### Cost of drift versus cost of retraining
Retraining uses compute, annotation, specialist review and deployment effort. Its value depends on expected degradation avoided and the risk of introducing regressions. A champion-challenger study compares an updated model to the current model on a representative period, controlling for changes in input processing. If the challenger improves one segment but damages another, a global average may conceal the tradeoff. Shadow execution can reveal serving performance while leaving actual decisions unchanged.

Rollback readiness requires storing the full serving bundle, including model weights, preprocessing, threshold configuration, schema version and dependencies. Rolling back weights alone while retaining a new scaler can produce unexpected output. Conduct rollback drills on an isolated staging environment. Measure time to detect, diagnose and recover, because deployment reliability is an operational property rather than a score in an offline machine-learning benchmark.

### Governance, permissions, and data minimization
Datasets may contain personal information even when explicit names are removed; combinations of timestamps, location and behavior can reidentify individuals. Minimize collection, restrict access, limit retention and audit outputs for unintended memorization. The appropriate legal basis and privacy duties depend on jurisdiction and application, so a textbook should not claim that a generic pseudonymization script satisfies all regulations. Record model-card limitations, data provenance and responsible ownership of alerts. A high-quality system earns trust through verifiable constraints and incident handling, not through a marketing label such as 'unbiased AI'.

An integrated acceptance test can combine data lineage, schema contracts, drift injection, subgroup evaluation, shadow serving and rollback. Each test should have a clear oracle and an expected failure. For example, a unit-conversion change should either be rejected by a schema guard or trigger an explicit blocked prediction, not silently change the model's risk estimate. Packaging these checks with versioned artifacts makes later review possible.

### When a model must stop making automatic decisions
A production machine-learning service needs an explicit abstention or fallback policy. Unknown schema versions, missing mandatory features, predictions outside validated score ranges, extreme measurement values and persistent monitoring alarms may justify blocking an automated action. The fallback should be tested for operational feasibility: an instruction to ask a human is insufficient if hundreds of requests arrive every second and only one reviewer is available. Estimate fallback workload under realistic failure frequencies and prioritize severe cases using approved rules. Log why each prediction was accepted, rejected or escalated, together with the model and data versions used. A rollback mechanism should restore preprocessing and threshold configurations as well as model parameters. The service's reliability depends as much on these behaviors as on the average accuracy measured before launch. A trustworthy textbook teaches failure containment alongside model construction.

### An independent serving acceptance trial
Before approving an updated machine-learning service, capture a set of reference requests representing ordinary observations, boundary values, missing optional features, unknown categories and deliberately invalid units. For each request, record the expected schema response and the expected model output or safe rejection. Run the reference suite against the exact serving bundle that would be deployed, including preprocessing code and decision thresholds. In a separate statistical validation, compare candidate and incumbent models on the same frozen holdout examples with a predeclared metric and acceptable uncertainty. A numerical serving test and a prediction-quality test answer different questions, so both must pass independently. If the new system improves average accuracy but causes unacceptable latency on a mobile device, changes scores under field reordering, or fails to reject invalid sensor units, it is not operationally ready. Keep the prior version available for rollback, rehearse the rollback procedure, and record a human owner for production alerts. The final approval record should state what has actually been tested, where evidence remains incomplete, and which environments are not covered. This prevents the existence of a ZIP file or a green unit-test badge from being mistaken for proof that a deployed learning system will behave safely.

### Worked question: Training-serving units
A model trained on temperature in Celsius uses standardized value z=(T-20)/5. A serving client sends 68 Fahrenheit but the service mistakenly treats it as Celsius. Compare incorrect and correct z values.

**Model the question**
Correct unit conversion is Celsius=(Fahrenheit-32)×5/9. Fahrenheit 68 equals Celsius 20, which is the training mean.

**Calculate or derive**
Incorrect pipeline computes (68-20)/5=9.6 standardized units. Correct conversion computes (20-20)/5=0. The enormous discrepancy is a semantic data bug that a learned model may treat as an extreme outlier.

**Check assumptions and boundaries**
A distribution monitor might notice a spike, but rejection before prediction is safer. Store feature units in the schema and test known conversion pairs. A 9.6-sigma-looking input does not prove a rare environmental event when software changed its measurement units.

**Answer:** Incorrect z=9.6; correct z=0.

### Worked question: True-positive-rate parity
Group A has 40 actual positive cases and the model detects 30. Group B has 20 actual positive cases and detects 15. Determine whether observed equal opportunity holds and whether equalized odds follows.

**Model the question**
Equal opportunity compares the true-positive rates for groups. Compute TP/(TP+FN) using actual positive denominators.

**Calculate or derive**
For A, TPR=30/40=.75. For B, TPR=15/20=.75. The observed TPRs match, so the sample satisfies equal opportunity in this specific numerical sense.

**Check assumptions and boundaries**
Equalized odds additionally requires equal false-positive rates. No false-positive counts or negative denominators were provided, so equalized odds cannot be assessed. Sampling uncertainty is substantial for twenty positive cases; identical point estimates do not certify population equality.

**Answer:** Sample equal-opportunity TPR parity holds at 75%; equalized odds is undetermined.

### Worked question: Covariate shift weight
For a discretized feature region x=A, the training probability is P_train(A)=0.2 while target probability is P_target(A)=0.5. Calculate the covariate-shift importance weight and explain its validity conditions.

**Model the question**
A basic importance weight for feature realization x is w(x)=P_target(x)/P_train(x), provided source support includes all target-important regions and conditional label behavior is stable.

**Calculate or derive**
For x=A, w(A)=.5/.2=2.5. Observations from A receive 2.5 times ordinary weight in a weighted risk estimate. Another region must balance probabilities, so not all weights are necessarily above one.

**Check assumptions and boundaries**
If the relationship P(Y|X) changes, correcting feature frequencies alone will not fix predictions. Weights estimated from finite samples have uncertainty, and extreme ratios reduce effective sample size. Report estimated support and variance rather than treating the factor as universal.

**Answer:** Importance weight for A is 2.5 under the covariate-shift assumptions.


### Extended evaluation laboratory: a model that learns a university semester rather than a general pattern

A predictive model estimates whether students will complete an introductory programming unit within a semester. The available table includes course identifier, assignment dates, support-session attendance and final completion. A naive random split can leak information when several rows describe the same student across assessments, or when features are measured after the outcome date. The correct split depends on the intended decision. If the tool forecasts progress at week three, all feature values must be available by week three for every training and test observation. A column recording final examination attendance violates that condition even if it raises reported validation accuracy. Construct a feature-availability table with a timestamp for every variable and use an explicit cutoff to rule out future information.

Repeated students also violate naive independence. If the same learner appears in training and validation, the model may memorize stable personal patterns rather than generalize to unseen people. A grouped split should place all records belonging to a learner in only one split when deployment targets new learners. If deployment targets returning students in a later semester, a chronological split may be more faithful, but historical data for that student can legitimately be known at prediction time. Write the intended population and inference timestamp before choosing grouped or temporal splitting. There is no universally correct split independent of the decision the system will support.

Build two baselines. The trivial baseline predicts the majority class and reports its class-specific errors; a simple logistic model uses approved pre-week-three features. A complex nonlinear model is justified only if it improves a meaningful evaluation measure on untouched data and does not introduce disproportionate operational cost. When completion is rare in some courses, report precision, recall and class-specific performance instead of relying only on accuracy. A predicted probability of 0.7 is not a measured probability of success unless calibration is supported under the evaluation distribution. Evaluate confidence intervals and sensitivity to changes in cohort composition.

Selection bias can further distort conclusions. Attendance at optional support sessions may correlate with motivation, schedule constraints and underlying difficulties. A predictive association does not establish that forcing every student to attend will causally increase completion. The model can support a decision about whom to invite to voluntary support, but its correlations should not be marketed as causal effects. To estimate interventions, a randomized or carefully justified quasi-experimental study is needed, with appropriate consent and privacy protections. Treat each feature as a data-governance responsibility: minimize personal data, restrict access, and explain how predictions are used.

After deployment, monitor changes to feature definitions, missing-value proportions, calibration and performance across cohorts. A sudden shift in assignment deadlines or curriculum can invalidate the old training distribution. Monitor labels only when they become available; do not compare immediate predictions to outcomes not yet observed. Set review triggers using observed degradation and operational impact rather than automatic retraining on every minor fluctuation. Version model artifacts, preprocessing code, training data lineage and evaluation criteria together so a prior decision can be reconstructed. Keep an override path for educators and learners, and audit whether assistance is allocated fairly. The experiment is complete only when the learner outcome, evaluation boundary and limitations are defined as carefully as the optimization algorithm. 

### Extension: checking whether a confidence threshold serves students

Suppose an adviser sends an optional tutoring invitation when predicted completion probability falls below 0.4. A threshold is not merely a statistical parameter; it determines which students receive an intervention, how many tutor hours are needed, and how often students are inconvenienced. Evaluate the workload at multiple thresholds on a held-out cohort, reporting counts of invitations, missed struggling students, and unnecessary invitations. Compare the intervention capacity against demand. If tutoring places are limited, ranking students solely by predicted risk can systematically deprioritize groups with poorer historical data coverage; analyze calibration and access separately for relevant cohorts without treating protected or sensitive attributes as permissible decision features by default. An invitation should not be treated as a punitive label. Run an evaluation of the actual support policy, because predicting need accurately is different from demonstrating that a targeted intervention improves learning. If outcomes cannot be measured independently, record uncertainty rather than assuming a beneficial effect. A policy should permit opt-out and correction of inaccurate records, and a human adviser should understand what evidence led to an invitation.

