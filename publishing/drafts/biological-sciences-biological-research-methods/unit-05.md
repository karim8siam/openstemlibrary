# Unit 05 — Statistics, estimation and honest inference

> **Educational editorial draft.** All scenarios and data are fictional. The sixteen adjustable models in the book are idealized teaching tools, not validated predictors.

## Unit orientation

Statistical methods quantify variation and patterns conditional on a study design and a model. They cannot manufacture independent replication, eliminate unmeasured confounding or repair poor measurement automatically. Exploratory plots are part of reasoning, but a test selected after many private attempts should not be reported as though chosen in advance. Estimate effects on interpretable scales with intervals and explain whether they are biologically important. Match outcome structure to models: continuous concentrations, binary germination, counts and repeated trajectories have different assumptions. Multiplicity matters when many genes, species or outcomes are searched.

### Learning objectives

- Identify the **estimand and uncertainty** for five different biological research decisions.

- Answer the design challenge: **Does the numerical model match the endpoint and dependency structure?**

- Identify an analysis failure addressed by **Which alternative assumptions move the effect most?**

- Produce a research artifact that makes the chain from observation to claim auditable.

## A method is an argument, not just a procedure

The topics in this unit share a concern with estimand and uncertainty. A sound method specifies what is being compared and explains why the measured response says something about the broader biological system. A result is interpretable only at the level supported by assignment, selection, calibration and analysis. The study may produce exact digital values while still leaving ecological or mechanistic uncertainty that cannot be converted into additional decimal places. In this unit, map decisions made before measurement separately from choices introduced while inspecting results. An acceptable alternative design may target a different estimand; that can be a strength when the alternatives are made visible.

### Practice before computation

Analysis workshop: start with raw observations and a design diagram; choose an estimand before a model. Plot replicate-level data, distinguish standard deviation from standard error, and compare the unadjusted contrast to a justified adjusted model. Examine residual patterns, leverage, missingness and clustering. Present a sensitivity table varying one important assumption at a time.

### The running scenario

Fictional investigation: A pot experiment measures growth repeatedly and a molecular assay measures selected markers. Designate growth as the primary outcome, use a unit-respecting model, and describe a multiplicity strategy for the exploratory marker scan. The numbers are invented teaching scenarios, not biological evidence.

### Responsibility and scope

Ethical boundary: p-values and model fit statistics must not be translated into guarantees that a mechanism exists or that an intervention should be implemented.

## Five lessons

## Lesson 5.1 — Descriptive summaries, distributions and uncertainty

**Inquiry to keep in view:** Does the numerical model match the endpoint and dependency structure? A lesson is successful when the learner can explain both the method and an observation that could undermine its proposed interpretation.

### Principle, construct and boundary

A mean describes location but can conceal skew, multimodality and important subgroups. Standard deviation describes observed spread; standard error describes uncertainty of an estimated mean under a model. Neither alone describes the biological importance of an effect.

### Study construction and operational decisions

For a fictional enzyme activity study, report independent-culture measurements using raw points, median and interquartile interval if skewed, and the mean with uncertainty when the estimand calls for it.

Convert that proposal into a miniature preregistered plan. Specify the sampling frame, independently informative unit, comparator, measurement schedule, planned primary endpoint and handling of observations that cannot be recorded. Identify which decisions must occur before anyone sees the response data. Where the proposed setting uses groups or clusters, identify the level at which a common cause or intervention can reach all observations. Where outcomes are longitudinal, state whether a difference between subjects or a change within subjects answers the question. Do not rely on the final number of data rows to settle the question of replication.

### Fictional example and worked calculation

**Method setting.** A range of fifteen units signals spread but says little about shape or reliability without raw observations.

**Invented inputs:** maxv = 22, minv = 7.  **Arithmetic expression:** `maxv-minv`.  **Computed result:** **15 assay units**.

### Diagnostic failure modes and design alternatives

Summaries based on pooled wells underestimate between-culture variation. Displaying a bar with standard error may hide outliers, denominator choices or batch structure critical to interpretation.

Use a structured critique rather than a general warning that bias may occur. First identify the exact step where the failure could enter: recruitment, allocation, collection, extraction, labelling, exclusion, modeling or interpretation. Next determine the direction in which a particular failure might move the estimate; an unknown direction is not the same as zero effect. Finally state which independent observation could distinguish the failure mechanism from the biological explanation. This process supports targeted controls and realistic uncertainty statements instead of presenting procedural completeness as proof of rigor.

**Alternative route.** Choose descriptive summaries according to variable scale and scientific objective rather than always using mean plus error bars.

### Interpretation, transparency and a reasoned conclusion

Label the level of replication and use plots of distributions before comparing groups; explain whether intervals represent data spread, estimation uncertainty or a model prediction.

**Transfer problem.** Apply the same distinction to animal movement distances with long right tails.

### Self-assessment (answers are provided for independent study)

1. **What does the arithmetic result establish?** It establishes `maxv-minv` for the explicitly invented numbers, giving 15 assay units; it does not, on its own, validate the underlying biological construct.

3. **How would you identify a stronger inference?** Propose one additional control, independent repeat, rival prediction or sensitivity test that separates the principal explanation from a plausible alternative.

## Lesson 5.2 — Effect sizes, confidence intervals and bootstrap methods

**Inquiry to keep in view:** Does the numerical model match the endpoint and dependency structure? A lesson is successful when the learner can explain both the method and an observation that could undermine its proposed interpretation.

### Principle, construct and boundary

Estimation focuses on how large an effect may be and how uncertain that estimate is. A confidence interval describes a procedure's long-run coverage under its assumptions, not a probability assigned to a fixed unknown parameter after data are observed. Bootstrap resampling must respect the independent sampling unit.

### Study construction and operational decisions

In a fictional two-group growth comparison, calculate an unstandardized difference in mean growth and resample whole pots rather than individual leaves to build a bootstrap uncertainty interval.

Convert that proposal into a miniature preregistered plan. Specify the sampling frame, independently informative unit, comparator, measurement schedule, planned primary endpoint and handling of observations that cannot be recorded. Identify which decisions must occur before anyone sees the response data. Where the proposed setting uses groups or clusters, identify the level at which a common cause or intervention can reach all observations. Where outcomes are longitudinal, state whether a difference between subjects or a change within subjects answers the question. Do not rely on the final number of data rows to settle the question of replication.

### Fictional example and worked calculation

**Method setting.** Use a standard error appropriate for independently sampled group means; the half-width is approximate and depends on assumptions.

**Invented inputs:** sd1 = 4, sd2 = 5, n1 = 25, n2 = 25.  **Arithmetic expression:** `1.96 * sqrt(sd1**2/n1 + sd2**2/n2)`.  **Computed result:** **2.51 95-percent normal-approximation half-width**.

### Diagnostic failure modes and design alternatives

A narrow interval can be precise about a biased quantity; a statistical significance threshold does not establish practical importance. Ordinary resampling fails for certain dependent, very small, or extreme-tail samples.

Use a structured critique rather than a general warning that bias may occur. First identify the exact step where the failure could enter: recruitment, allocation, collection, extraction, labelling, exclusion, modeling or interpretation. Next determine the direction in which a particular failure might move the estimate; an unknown direction is not the same as zero effect. Finally state which independent observation could distinguish the failure mechanism from the biological explanation. This process supports targeted controls and realistic uncertainty statements instead of presenting procedural completeness as proof of rigor.

**Alternative route.** Compare analytic intervals when assumptions are reasonable with percentile or studentized bootstrap intervals, inspecting sensitivity to skew and influential units.

### Interpretation, transparency and a reasoned conclusion

Give the estimate, units, interval, design limitations, and what values would change a biological decision instead of reporting a p-value alone.

**Transfer problem.** Carry the approach to paired before-and-after samples where each subject, not each row, must be resampled as a block.

### Self-assessment (answers are provided for independent study)

1. **What does the arithmetic result establish?** It establishes `1.96 * sqrt(sd1**2/n1 + sd2**2/n2)` for the explicitly invented numbers, giving 2.51 95-percent normal-approximation half-width; it does not, on its own, validate the underlying biological construct.

3. **How would you identify a stronger inference?** Propose one additional control, independent repeat, rival prediction or sensitivity test that separates the principal explanation from a plausible alternative.

## Lesson 5.3 — Regression and generalized linear models

**Inquiry to keep in view:** Does the numerical model match the endpoint and dependency structure? A lesson is successful when the learner can explain both the method and an observation that could undermine its proposed interpretation.

### Principle, construct and boundary

Regression relates an outcome to predictors conditional on a model; coefficient meaning depends on link function, scale, covariates and sampling design. Linear models suit some continuous endpoints; logistic or count models may suit binary outcomes or event counts. Model choice must be checked against biology and residual patterns.

### Study construction and operational decisions

Model fictional germination as a binary seed-level outcome with tray clustering and temperature as a predictor. Convert fitted log-odds to probabilities at biologically relevant temperatures instead of interpreting odds as probabilities.

Convert that proposal into a miniature preregistered plan. Specify the sampling frame, independently informative unit, comparator, measurement schedule, planned primary endpoint and handling of observations that cannot be recorded. Identify which decisions must occur before anyone sees the response data. Where the proposed setting uses groups or clusters, identify the level at which a common cause or intervention can reach all observations. Where outcomes are longitudinal, state whether a difference between subjects or a change within subjects answers the question. Do not rely on the final number of data rows to settle the question of replication.

### Fictional example and worked calculation

**Method setting.** A linear predictor of zero corresponds to probability one-half under a logistic link, not odds equal to one-half.

**Invented inputs:** eta = 0.  **Arithmetic expression:** `1/(1+exp(-eta))`.  **Computed result:** **0.5 probability**.

### Diagnostic failure modes and design alternatives

Complete separation, nonlinear dose-response, sparse counts and correlated responses can make naive maximum-likelihood estimates unstable or misleading. Including more predictors is not a substitute for sufficient independent information.

Use a structured critique rather than a general warning that bias may occur. First identify the exact step where the failure could enter: recruitment, allocation, collection, extraction, labelling, exclusion, modeling or interpretation. Next determine the direction in which a particular failure might move the estimate; an unknown direction is not the same as zero effect. Finally state which independent observation could distinguish the failure mechanism from the biological explanation. This process supports targeted controls and realistic uncertainty statements instead of presenting procedural completeness as proof of rigor.

**Alternative route.** Compare logistic and binomial models for germination fractions and assess whether overdispersion requires a different uncertainty structure.

### Interpretation, transparency and a reasoned conclusion

Report interpretable predicted outcomes, diagnostic checks, parameter uncertainty and the scope of extrapolation, not only a coefficient table.

**Transfer problem.** Translate to parasite egg counts where excess zeros and exposure time may matter.

### Self-assessment (answers are provided for independent study)

1. **What does the arithmetic result establish?** It establishes `1/(1+exp(-eta))` for the explicitly invented numbers, giving 0.5 probability; it does not, on its own, validate the underlying biological construct.

3. **How would you identify a stronger inference?** Propose one additional control, independent repeat, rival prediction or sensitivity test that separates the principal explanation from a plausible alternative.

## Lesson 5.4 — Repeated measures and hierarchical models

**Inquiry to keep in view:** Does the numerical model match the endpoint and dependency structure? A lesson is successful when the learner can explain both the method and an observation that could undermine its proposed interpretation.

### Principle, construct and boundary

Repeated measurements from one organism share a history and are typically correlated. Hierarchical models can represent variability among subjects, plots, batches or institutions while separating within-unit from between-unit patterns. The hierarchy must arise from the actual study, not convenience.

### Study construction and operational decisions

In an invented longitudinal growth experiment, collect four measurements from each of fifteen individual seedlings. Model a time trajectory with an individual-level random intercept and investigate whether a common slope is biologically plausible.

Convert that proposal into a miniature preregistered plan. Specify the sampling frame, independently informative unit, comparator, measurement schedule, planned primary endpoint and handling of observations that cannot be recorded. Identify which decisions must occur before anyone sees the response data. Where the proposed setting uses groups or clusters, identify the level at which a common cause or intervention can reach all observations. Where outcomes are longitudinal, state whether a difference between subjects or a change within subjects answers the question. Do not rely on the final number of data rows to settle the question of replication.

### Fictional example and worked calculation

**Method setting.** Four repeated measures with assumed intraclass correlation 0.3 have a simple equal-cluster design effect of 1.9 relative to independent rows.

**Invented inputs:** k = 4, icc = 0.3.  **Arithmetic expression:** `1+(k-1)*icc`.  **Computed result:** **1.9 multiplier**.

### Diagnostic failure modes and design alternatives

Treating sixty measurements as sixty independent plants exaggerates precision. With few high-level clusters, conventional asymptotic uncertainty formulas may be unreliable even if a mixed-model package converges.

Use a structured critique rather than a general warning that bias may occur. First identify the exact step where the failure could enter: recruitment, allocation, collection, extraction, labelling, exclusion, modeling or interpretation. Next determine the direction in which a particular failure might move the estimate; an unknown direction is not the same as zero effect. Finally state which independent observation could distinguish the failure mechanism from the biological explanation. This process supports targeted controls and realistic uncertainty statements instead of presenting procedural completeness as proof of rigor.

**Alternative route.** Compare subject-level slopes followed by analysis with a joint hierarchical model; the second uses more information but relies on a richer set of assumptions.

### Interpretation, transparency and a reasoned conclusion

Inspect within-subject residual correlation, unbalanced follow-up, between-subject heterogeneity and uncertainty on treatment-by-time terms.

**Transfer problem.** Extend the same framework to transects surveyed across seasons and years.

### Self-assessment (answers are provided for independent study)

1. **What does the arithmetic result establish?** It establishes `1+(k-1)*icc` for the explicitly invented numbers, giving 1.9 multiplier; it does not, on its own, validate the underlying biological construct.

3. **How would you identify a stronger inference?** Propose one additional control, independent repeat, rival prediction or sensitivity test that separates the principal explanation from a plausible alternative.

## Lesson 5.5 — Multiplicity, exploratory analyses and model selection

**Inquiry to keep in view:** Does the numerical model match the endpoint and dependency structure? A lesson is successful when the learner can explain both the method and an observation that could undermine its proposed interpretation.

### Principle, construct and boundary

Screening many genes, outcomes, contrasts or model specifications increases the chance that at least one apparently exciting result appears by chance. Control procedures address different error criteria, including family-wise error and expected false discovery proportion. Exploratory discovery can still be valuable when confirmed transparently.

### Study construction and operational decisions

In a fictional transcriptomic comparison, evaluate a prespecified gene-set endpoint and a secondary exploratory scan across several thousand features. Separate adjusted discovery statistics from confirmatory claims about one candidate.

Convert that proposal into a miniature preregistered plan. Specify the sampling frame, independently informative unit, comparator, measurement schedule, planned primary endpoint and handling of observations that cannot be recorded. Identify which decisions must occur before anyone sees the response data. Where the proposed setting uses groups or clusters, identify the level at which a common cause or intervention can reach all observations. Where outcomes are longitudinal, state whether a difference between subjects or a change within subjects answers the question. Do not rely on the final number of data rows to settle the question of replication.

### Fictional example and worked calculation

**Method setting.** For one hundred prespecified tests, a Bonferroni cutoff is 0.0005 for family-wise error at most 0.05 under standard validity assumptions.

**Invented inputs:** alpha = 0.05, tests = 100.  **Arithmetic expression:** `alpha / tests`.  **Computed result:** **0.0005 per-test alpha**.

### Diagnostic failure modes and design alternatives

Unreported model searching, repeated peeking and cherry-picked subgroups make nominal p-values untrustworthy. An adjusted list does not cure batch confounding or inadequate biological replication.

Use a structured critique rather than a general warning that bias may occur. First identify the exact step where the failure could enter: recruitment, allocation, collection, extraction, labelling, exclusion, modeling or interpretation. Next determine the direction in which a particular failure might move the estimate; an unknown direction is not the same as zero effect. Finally state which independent observation could distinguish the failure mechanism from the biological explanation. This process supports targeted controls and realistic uncertainty statements instead of presenting procedural completeness as proof of rigor.

**Alternative route.** Compare a small preregistered hypothesis family with broad discovery requiring error-rate control and independent validation in new samples.

### Interpretation, transparency and a reasoned conclusion

Publish all tested features, filter rules, normalization steps, effect estimates and the scope of each inferential claim.

**Transfer problem.** Repeat the logic for ecological studies testing many species responses from the same plots.

### Self-assessment (answers are provided for independent study)

1. **What does the arithmetic result establish?** It establishes `alpha / tests` for the explicitly invented numbers, giving 0.0005 per-test alpha; it does not, on its own, validate the underlying biological construct.

3. **How would you identify a stronger inference?** Propose one additional control, independent repeat, rival prediction or sensitivity test that separates the principal explanation from a plausible alternative.

## Unit 05 research studio — Synthetic integrated investigation

**Case premise.** Fictional investigation: A pot experiment measures growth repeatedly and a molecular assay measures selected markers. Designate growth as the primary outcome, use a unit-respecting model, and describe a multiplicity strategy for the exploratory marker scan. The numbers are invented teaching scenarios, not biological evidence.

### Stage A: write an analysis plan

Start with the exact main question, not a convenient available test. Write a population description, a sample eligibility rule, a biological unit, a comparator and the response scale. In the design table, separate outcome measurement from the biological construct it represents. Where an intervention exists, name the assignment mechanism and identify which participants, plots, specimens or batches share an exposure. Where the design is observational, supply a causal diagram or a carefully reasoned list of confounders and explain why each might influence both the exposure and endpoint.

The study should have at least one explicit falsification route. List an outcome or pattern that would make the leading explanation less plausible even if the average direction initially looked favorable. Also state why the same pattern might emerge from altered detection, handling, sample selection or instrument drift. This exercise prevents researchers from describing a merely possible mechanism as the only explanation for an observed contrast.

### Stage B: inspect fictional records

The accompanying unit CSV holds six invented observations with a baseline score, follow-up score, treatment label and batch identifier. No living organism was sampled to construct this file. Treat units as independent only for this classroom computation and record the assumption in your notes. Calculate changes for every row, group averages, difference in average change, the number of units contributing to each result and any imbalance across batches. Do not interpret the invented numbers as evidence of actual biological treatment response.

Before you summarize the numbers, intentionally remove one follow-up observation and write two analysis plans: a complete-case approach and a conservative sensitivity scenario. Why might missingness be related to the unobserved outcome? How would that possibility change the generality of your conclusion? For a second check, alter the assumed calibration of one instrument reading and repeat the contrast. The exercise reveals how numerical conclusions can depend on design and measurement assumptions rather than sample size alone.

### Stage C: defend the result

Write a two-hundred-word abstract for the synthetic example. It must use **estimand and uncertainty** to connect method to claim. Distinguish the calculation from the proposed mechanism, show the relevant uncertainty in prose, and name at least one alternative explanation. Attach an audit table with input file, analysis version, field definitions, excluded entries and a sentence describing how someone could independently rerun the exercise.

A reader who doubts the conclusion should not have to infer which values were changed after the fact. Retain your first analysis plan and place revisions beside it with dates and reasons. A corrected error is scientifically different from an undisclosed change that selects a pleasing outcome. If the stronger claim requires another experiment or validated technique, propose it explicitly instead of enlarging the present study’s conclusions.

### Stage D: ethical and practical review

Ethical boundary: p-values and model fit statistics must not be translated into guarantees that a mechanism exists or that an intervention should be implemented.

The studio is a dry-lab reasoning exercise. Any translation into work with participants, animals, sensitive ecological sites or biological materials demands separate supervision, local approvals and qualified protocol design. Identifying a feasible future observation is not authorization to conduct it. Preserve accurate fictional-data labels wherever the scenario is presented.

### Submission checklist

- Research question, population, independent unit, contrast and endpoint defined without hidden assumptions.

- Synthetic source CSV preserved without manual changes; any cleaning rules scripted and documented.

- Estimate calculated with units and appropriately cautious interpretation; alternatives and exclusions explained.

- A proposed independent check targets a specific failure mode rather than merely repeating the same measurement.

- Rights, safety, oversight, sensitive data and communication boundaries considered before translating the exercise.
