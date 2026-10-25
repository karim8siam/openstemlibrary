# Unit 03 — Measurement, controls and biological observation

> **Educational editorial draft.** All scenarios and data are fictional. The sixteen adjustable models in the book are idealized teaching tools, not validated predictors.

## Unit orientation

Biological numbers emerge from observation processes. Devices respond to physical properties, sample collection selects a subset of a system, and data processing transforms signals into endpoints. Every step creates assumptions: an image segmentation threshold may determine cell counts, a positive control may confirm detection but not the absence of sample inhibition, and a sampling frame may omit difficult terrain. Calibration links signals to suitable references over bounded ranges, with uncertainty; it does not prove the measured quantity has biological meaning. Biological replication represents independent material; technical repeats measure analytical consistency. Controls should test specified failure modes rather than decorate methods sections.

### Learning objectives

- Identify the **signal-to-quantity conversion** for five different biological research decisions.

- Answer the design challenge: **What physical or observational process creates this measurement?**

- Identify an analysis failure addressed by **Could a change in sensitivity imitate the biological effect?**

- Produce a research artifact that makes the chain from observation to claim auditable.

## A method is an argument, not just a procedure

The topics in this unit share a concern with signal-to-quantity conversion. A sound method specifies what is being compared and explains why the measured response says something about the broader biological system. A result is interpretable only at the level supported by assignment, selection, calibration and analysis. The study may produce exact digital values while still leaving ecological or mechanistic uncertainty that cannot be converted into additional decimal places. In this unit, map decisions made before measurement separately from choices introduced while inspecting results. An acceptable alternative design may target a different estimand; that can be a strength when the alternatives are made visible.

### Practice before computation

Measurement workshop: draw a chain from living system to sample, specimen preparation, instrument signal, derived outcome and reported contrast. At each transition identify a plausible error, a corresponding control and an acceptance rule. Use a unit table to distinguish counts, concentrations, rates and normalized fold changes. Practice reporting limits of detection separately from truly absent quantities.

### The running scenario

Fictional investigation: Design an imaginary fluorescence assay of leaf extracts with blanks, a calibrator series, quality-control material and pot-level replication. Calculate concentrations only inside an assumed working range; label synthetic readings and document what a failed control would invalidate.

### Responsibility and scope

Ethical boundary: this course explains validation logic and uses invented values, not a lab-ready protocol for biological agents, human specimens or diagnostic decisions.

## Five lessons

## Lesson 3.1 — Sampling frames and field surveys

**Inquiry to keep in view:** What physical or observational process creates this measurement? A lesson is successful when the learner can explain both the method and an observation that could undermine its proposed interpretation.

### Principle, construct and boundary

A sampling frame is the practical collection of units that could enter a study; inference beyond it requires additional assumptions. Spatial design, seasonality, detection probability and access restrictions shape which organisms or habitats are observed. A large biased sample may be less informative than a smaller probability sample.

### Study construction and operational decisions

In a fictional wetland, define accessible survey plots with coordinates, draw a stratified random sample across habitat zones, and revisit plots on a planned schedule. Record effort, weather, observer, and reasons for missed visits.

Convert that proposal into a miniature preregistered plan. Specify the sampling frame, independently informative unit, comparator, measurement schedule, planned primary endpoint and handling of observations that cannot be recorded. Identify which decisions must occur before anyone sees the response data. Where the proposed setting uses groups or clusters, identify the level at which a common cause or intervention can reach all observations. Where outcomes are longitudinal, state whether a difference between subjects or a change within subjects answers the question. Do not rely on the final number of data rows to settle the question of replication.

### Fictional example and worked calculation

**Method setting.** A simple random sample of thirty plots from a frame of one hundred fifty gives each plot an inclusion probability of 0.20.

**Invented inputs:** n = 30, N = 150.  **Arithmetic expression:** `n / N`.  **Computed result:** **0.2 probability**.

### Diagnostic failure modes and design alternatives

Roadside-only plots can systematically omit remote habitat, and nondetection does not prove absence. Changing survey effort between seasons can imitate ecological change.

Use a structured critique rather than a general warning that bias may occur. First identify the exact step where the failure could enter: recruitment, allocation, collection, extraction, labelling, exclusion, modeling or interpretation. Next determine the direction in which a particular failure might move the estimate; an unknown direction is not the same as zero effect. Finally state which independent observation could distinguish the failure mechanism from the biological explanation. This process supports targeted controls and realistic uncertainty statements instead of presenting procedural completeness as proof of rigor.

**Alternative route.** For estimating total abundance, select methods with known inclusion probabilities; for mechanistic comparisons, purposeful environmental gradients may be useful but support narrower inference.

### Interpretation, transparency and a reasoned conclusion

Include a map of sampling coverage, response rates, detection assumptions and uncertainty attributable to observation as well as organism variability.

**Transfer problem.** Apply this critique to coastal samples where tide stage can make the frame itself dynamic.

### Self-assessment (answers are provided for independent study)

1. **What does the arithmetic result establish?** It establishes `n / N` for the explicitly invented numbers, giving 0.2 probability; it does not, on its own, validate the underlying biological construct.

3. **How would you identify a stronger inference?** Propose one additional control, independent repeat, rival prediction or sensitivity test that separates the principal explanation from a plausible alternative.

## Lesson 3.2 — Assay calibration and measurement error

**Inquiry to keep in view:** What physical or observational process creates this measurement? A lesson is successful when the learner can explain both the method and an observation that could undermine its proposed interpretation.

### Principle, construct and boundary

Calibration links instrument response to a known reference over a specified range, with blanks, controls and uncertainty. Precision describes consistency; accuracy concerns proximity to an appropriate reference. Biological samples introduce matrix effects that calibration standards may not reproduce.

### Study construction and operational decisions

Build a fictional optical assay with blank wells, multiple known-concentration standards, independent quality-control material, and duplicate unknowns. Fit an appropriate calibration relation only within its validated range and flag extrapolated samples.

Convert that proposal into a miniature preregistered plan. Specify the sampling frame, independently informative unit, comparator, measurement schedule, planned primary endpoint and handling of observations that cannot be recorded. Identify which decisions must occur before anyone sees the response data. Where the proposed setting uses groups or clusters, identify the level at which a common cause or intervention can reach all observations. Where outcomes are longitudinal, state whether a difference between subjects or a change within subjects answers the question. Do not rely on the final number of data rows to settle the question of replication.

### Fictional example and worked calculation

**Method setting.** A fictional linear calibration is used inside its stipulated validated range; the detector response is not an independent biological replicate.

**Invented inputs:** signal = 0.74, intercept = 0.1, slope = 0.08.  **Arithmetic expression:** `(signal - intercept)/slope`.  **Computed result:** **8 concentration units**.

### Diagnostic failure modes and design alternatives

A visually straight curve can conceal residual patterns, saturation, or drift; subtracting a blank cannot rescue a fundamentally nonlinear instrument region. Counting technical repeats as biological replication produces unjustified conclusions.

Use a structured critique rather than a general warning that bias may occur. First identify the exact step where the failure could enter: recruitment, allocation, collection, extraction, labelling, exclusion, modeling or interpretation. Next determine the direction in which a particular failure might move the estimate; an unknown direction is not the same as zero effect. Finally state which independent observation could distinguish the failure mechanism from the biological explanation. This process supports targeted controls and realistic uncertainty statements instead of presenting procedural completeness as proof of rigor.

**Alternative route.** Standard addition, matrix-matched calibration and dilution series address different interference mechanisms. Choose a control strategy justified by the sample matrix, not simply by convenience.

### Interpretation, transparency and a reasoned conclusion

Record lot numbers, detector settings, QC acceptance limits, raw instrument values, excluded observations and propagation of calibration uncertainty.

**Transfer problem.** Consider how changing reagent batch changes the meaning of between-day comparisons even with identical nominal concentrations.

### Self-assessment (answers are provided for independent study)

1. **What does the arithmetic result establish?** It establishes `(signal - intercept)/slope` for the explicitly invented numbers, giving 8 concentration units; it does not, on its own, validate the underlying biological construct.

3. **How would you identify a stronger inference?** Propose one additional control, independent repeat, rival prediction or sensitivity test that separates the principal explanation from a plausible alternative.

## Lesson 3.3 — Positive, negative and process controls

**Inquiry to keep in view:** What physical or observational process creates this measurement? A lesson is successful when the learner can explain both the method and an observation that could undermine its proposed interpretation.

### Principle, construct and boundary

A control is informative only relative to a stated failure mode. Negative controls test contamination or background; positive controls establish that a system can detect a target under validated conditions. Process controls monitor the collection, extraction, amplification or imaging pipeline.

### Study construction and operational decisions

In a fictional gene-expression assay, include no-template wells, extraction blanks, a stable reference material, and a monitored positive-control dilution. Define beforehand what pattern triggers a failed run or investigation.

Convert that proposal into a miniature preregistered plan. Specify the sampling frame, independently informative unit, comparator, measurement schedule, planned primary endpoint and handling of observations that cannot be recorded. Identify which decisions must occur before anyone sees the response data. Where the proposed setting uses groups or clusters, identify the level at which a common cause or intervention can reach all observations. Where outcomes are longitudinal, state whether a difference between subjects or a change within subjects answers the question. Do not rely on the final number of data rows to settle the question of replication.

### Fictional example and worked calculation

**Method setting.** A control measures ninety-five percent of its reference value; acceptability must depend on an independently justified performance criterion.

**Invented inputs:** observed = 95, target = 100.  **Arithmetic expression:** `observed / target * 100`.  **Computed result:** **95 percent recovery**.

### Diagnostic failure modes and design alternatives

A clean no-template control does not prove that extraction worked, while a positive control does not rule out sample-specific inhibition. Adding many unnamed controls is not equivalent to defining how each changes interpretation.

Use a structured critique rather than a general warning that bias may occur. First identify the exact step where the failure could enter: recruitment, allocation, collection, extraction, labelling, exclusion, modeling or interpretation. Next determine the direction in which a particular failure might move the estimate; an unknown direction is not the same as zero effect. Finally state which independent observation could distinguish the failure mechanism from the biological explanation. This process supports targeted controls and realistic uncertainty statements instead of presenting procedural completeness as proof of rigor.

**Alternative route.** Distinguish a biological comparator from a technical QC control: one estimates the research contrast; the other guards reliability of the measurement process.

### Interpretation, transparency and a reasoned conclusion

Present expected and observed control behavior next to the result, including failed batches and repeat rules, so readers can judge whether evidence was generated within accepted bounds.

**Transfer problem.** Adapt the structure to microscopy, where illumination flat fields and staining controls answer different questions.

### Self-assessment (answers are provided for independent study)

1. **What does the arithmetic result establish?** It establishes `observed / target * 100` for the explicitly invented numbers, giving 95 percent recovery; it does not, on its own, validate the underlying biological construct.

3. **How would you identify a stronger inference?** Propose one additional control, independent repeat, rival prediction or sensitivity test that separates the principal explanation from a plausible alternative.

## Lesson 3.4 — Imaging, segmentation and observer agreement

**Inquiry to keep in view:** What physical or observational process creates this measurement? A lesson is successful when the learner can explain both the method and an observation that could undermine its proposed interpretation.

### Principle, construct and boundary

An image becomes quantitative only after an explicit acquisition and analysis pipeline defines the biological object and endpoint. Spatial resolution, illumination, segmentation thresholds, operator choices and batch effects can dominate variation. Human labels may be useful but must be audited.

### Study construction and operational decisions

For hypothetical tissue images, fix acquisition settings, randomize slide order, mask groups, specify what qualifies as a cell, and compare automated segmentation counts with a blinded manually reviewed subset.

Convert that proposal into a miniature preregistered plan. Specify the sampling frame, independently informative unit, comparator, measurement schedule, planned primary endpoint and handling of observations that cannot be recorded. Identify which decisions must occur before anyone sees the response data. Where the proposed setting uses groups or clusters, identify the level at which a common cause or intervention can reach all observations. Where outcomes are longitudinal, state whether a difference between subjects or a change within subjects answers the question. Do not rely on the final number of data rows to settle the question of replication.

### Fictional example and worked calculation

**Method setting.** Among eighty software-marked objects, seventy-two match the invented reviewer standard; missed objects still need recall analysis.

**Invented inputs:** tp = 72, fp = 8.  **Arithmetic expression:** `tp/(tp+fp)`.  **Computed result:** **0.9 precision**.

### Diagnostic failure modes and design alternatives

Selecting the sharpest fields after looking at the treatment groups creates selection bias, while adjusting thresholds separately by condition can manufacture a signal. Agreement on training images does not demonstrate performance across instruments.

Use a structured critique rather than a general warning that bias may occur. First identify the exact step where the failure could enter: recruitment, allocation, collection, extraction, labelling, exclusion, modeling or interpretation. Next determine the direction in which a particular failure might move the estimate; an unknown direction is not the same as zero effect. Finally state which independent observation could distinguish the failure mechanism from the biological explanation. This process supports targeted controls and realistic uncertainty statements instead of presenting procedural completeness as proof of rigor.

**Alternative route.** Evaluate count agreement, error by object size, and sensitivity to threshold selection; when validation fails use a limited manually defined endpoint rather than claiming an autonomous image model is objective.

### Interpretation, transparency and a reasoned conclusion

Archive representative images, processing parameters, annotation rules and software versions with enough provenance to trace each derived number to pixels.

**Transfer problem.** Translate this workflow to wildlife camera traps where capture frequency and observer disagreement are additional sources of uncertainty.

### Self-assessment (answers are provided for independent study)

1. **What does the arithmetic result establish?** It establishes `tp/(tp+fp)` for the explicitly invented numbers, giving 0.9 precision; it does not, on its own, validate the underlying biological construct.

3. **How would you identify a stronger inference?** Propose one additional control, independent repeat, rival prediction or sensitivity test that separates the principal explanation from a plausible alternative.

## Lesson 3.5 — Molecular quantification and assay validity

**Inquiry to keep in view:** What physical or observational process creates this measurement? A lesson is successful when the learner can explain both the method and an observation that could undermine its proposed interpretation.

### Principle, construct and boundary

Relative molecular quantities often depend on normalization, reference assumptions, efficiency and scale. A value reported as a fold-change may be conditional on extraction quality or threshold choices, not simply the number of molecules in the original specimen.

### Study construction and operational decisions

In a fictional reverse-transcription quantitative PCR teaching dataset, compare target and reference cycle thresholds across balanced treatment groups and show the algebra behind a comparative threshold approach under stated efficiency assumptions.

Convert that proposal into a miniature preregistered plan. Specify the sampling frame, independently informative unit, comparator, measurement schedule, planned primary endpoint and handling of observations that cannot be recorded. Identify which decisions must occur before anyone sees the response data. Where the proposed setting uses groups or clusters, identify the level at which a common cause or intervention can reach all observations. Where outcomes are longitudinal, state whether a difference between subjects or a change within subjects answers the question. Do not rely on the final number of data rows to settle the question of replication.

### Fictional example and worked calculation

**Method setting.** A delta-delta Ct of minus two maps to a fourfold relative estimate only under stated assay-efficiency and reference stability assumptions.

**Invented inputs:** delta_delta_ct = -2.  **Arithmetic expression:** `2**(-delta_delta_ct)`.  **Computed result:** **4 relative fold**.

### Diagnostic failure modes and design alternatives

Unstable reference genes, inhibitors, variable efficiency and censoring near detection limits can distort apparent expression. A single arbitrarily chosen reference is not validated merely because its name is common in the literature.

Use a structured critique rather than a general warning that bias may occur. First identify the exact step where the failure could enter: recruitment, allocation, collection, extraction, labelling, exclusion, modeling or interpretation. Next determine the direction in which a particular failure might move the estimate; an unknown direction is not the same as zero effect. Finally state which independent observation could distinguish the failure mechanism from the biological explanation. This process supports targeted controls and realistic uncertainty statements instead of presenting procedural completeness as proof of rigor.

**Alternative route.** Compare absolute calibration using suitable standards with normalized relative analysis; the methods answer related but nonidentical questions and make different demands on uncertainty accounting.

### Interpretation, transparency and a reasoned conclusion

Report assay identifiers, technical repeat summaries, reference validation, exclusion handling and the units or relative scale of the endpoint.

**Transfer problem.** Contrast RNA sequencing where library normalization and compositional effects require a different statistical treatment.

### Self-assessment (answers are provided for independent study)

1. **What does the arithmetic result establish?** It establishes `2**(-delta_delta_ct)` for the explicitly invented numbers, giving 4 relative fold; it does not, on its own, validate the underlying biological construct.

3. **How would you identify a stronger inference?** Propose one additional control, independent repeat, rival prediction or sensitivity test that separates the principal explanation from a plausible alternative.

## Unit 03 research studio — Synthetic integrated investigation

**Case premise.** Fictional investigation: Design an imaginary fluorescence assay of leaf extracts with blanks, a calibrator series, quality-control material and pot-level replication. Calculate concentrations only inside an assumed working range; label synthetic readings and document what a failed control would invalidate.

### Stage A: write an analysis plan

Start with the exact main question, not a convenient available test. Write a population description, a sample eligibility rule, a biological unit, a comparator and the response scale. In the design table, separate outcome measurement from the biological construct it represents. Where an intervention exists, name the assignment mechanism and identify which participants, plots, specimens or batches share an exposure. Where the design is observational, supply a causal diagram or a carefully reasoned list of confounders and explain why each might influence both the exposure and endpoint.

The study should have at least one explicit falsification route. List an outcome or pattern that would make the leading explanation less plausible even if the average direction initially looked favorable. Also state why the same pattern might emerge from altered detection, handling, sample selection or instrument drift. This exercise prevents researchers from describing a merely possible mechanism as the only explanation for an observed contrast.

### Stage B: inspect fictional records

The accompanying unit CSV holds six invented observations with a baseline score, follow-up score, treatment label and batch identifier. No living organism was sampled to construct this file. Treat units as independent only for this classroom computation and record the assumption in your notes. Calculate changes for every row, group averages, difference in average change, the number of units contributing to each result and any imbalance across batches. Do not interpret the invented numbers as evidence of actual biological treatment response.

Before you summarize the numbers, intentionally remove one follow-up observation and write two analysis plans: a complete-case approach and a conservative sensitivity scenario. Why might missingness be related to the unobserved outcome? How would that possibility change the generality of your conclusion? For a second check, alter the assumed calibration of one instrument reading and repeat the contrast. The exercise reveals how numerical conclusions can depend on design and measurement assumptions rather than sample size alone.

### Stage C: defend the result

Write a two-hundred-word abstract for the synthetic example. It must use **signal-to-quantity conversion** to connect method to claim. Distinguish the calculation from the proposed mechanism, show the relevant uncertainty in prose, and name at least one alternative explanation. Attach an audit table with input file, analysis version, field definitions, excluded entries and a sentence describing how someone could independently rerun the exercise.

A reader who doubts the conclusion should not have to infer which values were changed after the fact. Retain your first analysis plan and place revisions beside it with dates and reasons. A corrected error is scientifically different from an undisclosed change that selects a pleasing outcome. If the stronger claim requires another experiment or validated technique, propose it explicitly instead of enlarging the present study’s conclusions.

### Stage D: ethical and practical review

Ethical boundary: this course explains validation logic and uses invented values, not a lab-ready protocol for biological agents, human specimens or diagnostic decisions.

The studio is a dry-lab reasoning exercise. Any translation into work with participants, animals, sensitive ecological sites or biological materials demands separate supervision, local approvals and qualified protocol design. Identifying a feasible future observation is not authorization to conduct it. Preserve accurate fictional-data labels wherever the scenario is presented.

### Submission checklist

- Research question, population, independent unit, contrast and endpoint defined without hidden assumptions.

- Synthetic source CSV preserved without manual changes; any cleaning rules scripted and documented.

- Estimate calculated with units and appropriately cautious interpretation; alternatives and exclusions explained.

- A proposed independent check targets a specific failure mode rather than merely repeating the same measurement.

- Rights, safety, oversight, sensitive data and communication boundaries considered before translating the exercise.
