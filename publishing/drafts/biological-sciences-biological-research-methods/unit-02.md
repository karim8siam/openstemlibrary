# Unit 02 — Experiments, samples and comparisons

> **Educational editorial draft.** All scenarios and data are fictional. The sixteen adjustable models in the book are idealized teaching tools, not validated predictors.

## Unit orientation

A scientific design specifies which units enter, which units receive interventions, when outcomes are measured and which contrast answers the question. The number of readings is not the same as the number of independent experimental units. A treatment assigned to tanks is replicated by independently treated tanks, even when numerous organisms live inside each. Blocking can account for background gradients, factorial design reveals conditional effects, and repeated measurement can improve precision when correlations are represented. Observational designs can be informative, yet their identification assumptions must be defended. Power calculations depend on expected variability and minimally important effects; an impressive sample number cannot rescue a biased allocation or invalid measurement.

### Learning objectives

- Identify the **unit and allocation process** for five different biological research decisions.

- Answer the design challenge: **At what level is the contrast independently generated?**

- Identify an analysis failure addressed by **Would counting sub-observations as replicates change the uncertainty without changing information?**

- Produce a research artifact that makes the chain from observation to claim auditable.

## A method is an argument, not just a procedure

The topics in this unit share a concern with unit and allocation process. A sound method specifies what is being compared and explains why the measured response says something about the broader biological system. A result is interpretable only at the level supported by assignment, selection, calibration and analysis. The study may produce exact digital values while still leaving ecological or mechanistic uncertainty that cannot be converted into additional decimal places. In this unit, map decisions made before measurement separately from choices introduced while inspecting results. An acceptable alternative design may target a different estimand; that can be a strength when the alternatives are made visible.

### Practice before computation

Design workshop: for each of three situations, diagram the nesting of treatment units, biological samples, technical repeats, and repeated visits. Specify whether randomization is possible, whether blinding can protect assessment, and which potential confounder blocks are intended to address. Recalculate apparent sample size when the average number of subsamples per cluster increases but independent cluster count remains fixed.

### The running scenario

Fictional investigation: Compare seedling growth in four greenhouse blocks under a crossed nutrient-by-temperature design. Explain why one chamber for each temperature confounds chamber with treatment. Create a random assignment ledger and predeclare interaction as the primary test, leaving exploratory contrasts explicitly secondary.

### Responsibility and scope

Ethical boundary: sample-size justification should make scientifically and ethically defensible use of resources; it must not be used to rationalize avoidable harm or concealed exploratory testing.

## Five lessons

## Lesson 2.1 — Experimental units and pseudoreplication

**Inquiry to keep in view:** At what level is the contrast independently generated? A lesson is successful when the learner can explain both the method and an observation that could undermine its proposed interpretation.

### Principle, construct and boundary

Independence is determined by how a treatment or environmental process reaches units, not by the number of rows in a spreadsheet. Subsamples from one culture dish, cage, field plot, or person generally do not substitute for independently assigned biological replicates. The hierarchy of experimental units must appear in the analysis.

### Study construction and operational decisions

An invented experiment treats six aquaria with a water chemistry regime, with five fish measured per aquarium. The independent treatment replication is six aquaria, not thirty fish, because all fish within an aquarium share the assigned exposure.

Convert that proposal into a miniature preregistered plan. Specify the sampling frame, independently informative unit, comparator, measurement schedule, planned primary endpoint and handling of observations that cannot be recorded. Identify which decisions must occur before anyone sees the response data. Where the proposed setting uses groups or clusters, identify the level at which a common cause or intervention can reach all observations. Where outcomes are longitudinal, state whether a difference between subjects or a change within subjects answers the question. Do not rely on the final number of data rows to settle the question of replication.

### Fictional example and worked calculation

**Method setting.** With five observations per aquarium and assumed intraclass correlation 0.2, independent-row information is overstated by a simple design effect of 1.8 under equal-size clustering.

**Invented inputs:** m = 5, rho = 0.2.  **Arithmetic expression:** `1 + (m - 1) * rho`.  **Computed result:** **1.8 design-effect multiplier**.

### Diagnostic failure modes and design alternatives

Ignoring clustering usually understates uncertainty and overstates apparent precision. Repeated measures and nested subsamples can improve measurement of an aquarium mean without increasing independent treatment replication.

Use a structured critique rather than a general warning that bias may occur. First identify the exact step where the failure could enter: recruitment, allocation, collection, extraction, labelling, exclusion, modeling or interpretation. Next determine the direction in which a particular failure might move the estimate; an unknown direction is not the same as zero effect. Finally state which independent observation could distinguish the failure mechanism from the biological explanation. This process supports targeted controls and realistic uncertainty statements instead of presenting procedural completeness as proof of rigor.

**Alternative route.** Either average appropriate fish-level measurements to tank summaries or use a justified hierarchical model that represents tank effects explicitly; never silently switch sample sizes.

### Interpretation, transparency and a reasoned conclusion

A transparent methods section distinguishes treatment units, biological replicates, technical repeats, temporal repeats, and the denominator used in each calculation.

**Transfer problem.** Reconsider the unit when the same design uses independent recirculating tanks versus tanks sharing a single reservoir.

### Self-assessment (answers are provided for independent study)

1. **What does the arithmetic result establish?** It establishes `1 + (m - 1) * rho` for the explicitly invented numbers, giving 1.8 design-effect multiplier; it does not, on its own, validate the underlying biological construct.

3. **How would you identify a stronger inference?** Propose one additional control, independent repeat, rival prediction or sensitivity test that separates the principal explanation from a plausible alternative.

## Lesson 2.2 — Randomization and allocation concealment

**Inquiry to keep in view:** At what level is the contrast independently generated? A lesson is successful when the learner can explain both the method and an observation that could undermine its proposed interpretation.

### Principle, construct and boundary

Random assignment helps break systematic links between treatment and preexisting differences when implementation preserves the intended process. Allocation concealment protects recruitment or selection before assignment; blinding protects measurement and decisions afterward. These safeguards answer distinct sources of bias.

### Study construction and operational decisions

In a fictional seedling study, generate the treatment schedule with a stored random seed and assign pot IDs before planting. Keep the allocation sequence inaccessible to the person selecting viable seedlings, and use masked image identifiers during leaf measurement.

Convert that proposal into a miniature preregistered plan. Specify the sampling frame, independently informative unit, comparator, measurement schedule, planned primary endpoint and handling of observations that cannot be recorded. Identify which decisions must occur before anyone sees the response data. Where the proposed setting uses groups or clusters, identify the level at which a common cause or intervention can reach all observations. Where outcomes are longitudinal, state whether a difference between subjects or a change within subjects answers the question. Do not rely on the final number of data rows to settle the question of replication.

### Fictional example and worked calculation

**Method setting.** A difference of two assigned pots is not evidence of assignment bias without considering the planned randomization scheme.

**Invented inputs:** n_a = 23, n_b = 21.  **Arithmetic expression:** `abs(n_a - n_b)`.  **Computed result:** **2 units**.

### Diagnostic failure modes and design alternatives

Alternating groups by bench position is predictable and can coincide with microclimate; excluding damaged seedlings only after seeing their groups defeats the intended protection.

Use a structured critique rather than a general warning that bias may occur. First identify the exact step where the failure could enter: recruitment, allocation, collection, extraction, labelling, exclusion, modeling or interpretation. Next determine the direction in which a particular failure might move the estimate; an unknown direction is not the same as zero effect. Finally state which independent observation could distinguish the failure mechanism from the biological explanation. This process supports targeted controls and realistic uncertainty statements instead of presenting procedural completeness as proof of rigor.

**Alternative route.** Simple randomization is adequate for many balanced settings, while blocked or stratified randomization can protect balance on a few strong baseline predictors in small experiments.

### Interpretation, transparency and a reasoned conclusion

Report the actual randomization mechanism, implementation failures, exclusions and any unblinded roles instead of writing the unsupported phrase 'samples were randomized.'

**Transfer problem.** Apply this distinction to an insect behavioral assay in which observers cannot be blinded to visible arena treatments but video scorers can be masked.

### Self-assessment (answers are provided for independent study)

1. **What does the arithmetic result establish?** It establishes `abs(n_a - n_b)` for the explicitly invented numbers, giving 2 units; it does not, on its own, validate the underlying biological construct.

3. **How would you identify a stronger inference?** Propose one additional control, independent repeat, rival prediction or sensitivity test that separates the principal explanation from a plausible alternative.

## Lesson 2.3 — Blocking and factorial experiments

**Inquiry to keep in view:** At what level is the contrast independently generated? A lesson is successful when the learner can explain both the method and an observation that could undermine its proposed interpretation.

### Principle, construct and boundary

Blocks group experimental units that share a nuisance condition; factorial designs estimate main effects and interactions among deliberate factors. A strong design uses variation to answer a planned biological question without confusing block identity with treatment. Interaction effects are differences in treatment effects across contexts.

### Study construction and operational decisions

Assign two temperature levels and two nutrient levels within each of four climate-control batches. Record the batch as a design variable and predefine whether the primary interest is the average nutrient effect or the temperature-by-nutrient interaction.

Convert that proposal into a miniature preregistered plan. Specify the sampling frame, independently informative unit, comparator, measurement schedule, planned primary endpoint and handling of observations that cannot be recorded. Identify which decisions must occur before anyone sees the response data. Where the proposed setting uses groups or clusters, identify the level at which a common cause or intervention can reach all observations. Where outcomes are longitudinal, state whether a difference between subjects or a change within subjects answers the question. Do not rely on the final number of data rows to settle the question of replication.

### Fictional example and worked calculation

**Method setting.** The synthetic difference-in-differences isolates an additive interaction on the observed response scale.

**Invented inputs:** a11 = 17, a10 = 11, a01 = 13, a00 = 10.  **Arithmetic expression:** `(a11-a10) - (a01-a00)`.  **Computed result:** **3 response units**.

### Diagnostic failure modes and design alternatives

One chamber per temperature cannot separate temperature from chamber effects no matter how many pots are inside. Factorial interactions also require sufficient replication; interpreting them after inspecting only four treatment means is unreliable.

Use a structured critique rather than a general warning that bias may occur. First identify the exact step where the failure could enter: recruitment, allocation, collection, extraction, labelling, exclusion, modeling or interpretation. Next determine the direction in which a particular failure might move the estimate; an unknown direction is not the same as zero effect. Finally state which independent observation could distinguish the failure mechanism from the biological explanation. This process supports targeted controls and realistic uncertainty statements instead of presenting procedural completeness as proof of rigor.

**Alternative route.** A blocked factorial design may cost more setup effort than one-factor-at-a-time work but is far more informative if the biological mechanism predicts conditional responses.

### Interpretation, transparency and a reasoned conclusion

Show four cell estimates, uncertainty, a clearly signed interaction contrast and the replication structure before mechanistic interpretation.

**Transfer problem.** Transfer the same design to substrate type and soil moisture when blocks are collected seed batches.

### Self-assessment (answers are provided for independent study)

1. **What does the arithmetic result establish?** It establishes `(a11-a10) - (a01-a00)` for the explicitly invented numbers, giving 3 response units; it does not, on its own, validate the underlying biological construct.

3. **How would you identify a stronger inference?** Propose one additional control, independent repeat, rival prediction or sensitivity test that separates the principal explanation from a plausible alternative.

## Lesson 2.4 — Observational designs and confounding

**Inquiry to keep in view:** At what level is the contrast independently generated? A lesson is successful when the learner can explain both the method and an observation that could undermine its proposed interpretation.

### Principle, construct and boundary

Cross-sectional, cohort, case-control, and repeated-observation designs select different populations and time structures. Their associations do not automatically identify interventions, especially when exposure is not assigned. Confounding is a causal problem arising when other factors influence both exposure and outcome.

### Study construction and operational decisions

Suppose a fictional study records pesticide exposure indicators and insect abundance across farms. Define the sampling frame, measure crop composition and surrounding habitat, and distinguish temporal ordering from a one-visit snapshot.

Convert that proposal into a miniature preregistered plan. Specify the sampling frame, independently informative unit, comparator, measurement schedule, planned primary endpoint and handling of observations that cannot be recorded. Identify which decisions must occur before anyone sees the response data. Where the proposed setting uses groups or clusters, identify the level at which a common cause or intervention can reach all observations. Where outcomes are longitudinal, state whether a difference between subjects or a change within subjects answers the question. Do not rely on the final number of data rows to settle the question of replication.

### Fictional example and worked calculation

**Method setting.** A fictional two-by-two association produces odds ratio three; selection and confounding remain unresolved.

**Invented inputs:** a = 18, b = 12, c = 10, d = 20.  **Arithmetic expression:** `(a*d)/(b*c)`.  **Computed result:** **3 odds ratio**.

### Diagnostic failure modes and design alternatives

Farms with higher pest pressure may use more pesticide; reverse causation and unmeasured management could create misleading associations. Adjusting an incomplete regression model does not turn the analysis into a randomized trial.

Use a structured critique rather than a general warning that bias may occur. First identify the exact step where the failure could enter: recruitment, allocation, collection, extraction, labelling, exclusion, modeling or interpretation. Next determine the direction in which a particular failure might move the estimate; an unknown direction is not the same as zero effect. Finally state which independent observation could distinguish the failure mechanism from the biological explanation. This process supports targeted controls and realistic uncertainty statements instead of presenting procedural completeness as proof of rigor.

**Alternative route.** Repeated within-farm measurements, negative controls, or a plausible natural experiment can strengthen inferences but demand explicit assumptions and sensitivity to violations.

### Interpretation, transparency and a reasoned conclusion

Report selection criteria, missing farms, measured confounders, effect estimates and the limits of identification rather than using 'impact' as a synonym for correlation.

**Transfer problem.** Consider how the question changes if monitoring starts before pesticide use rather than after damage is visible.

### Self-assessment (answers are provided for independent study)

1. **What does the arithmetic result establish?** It establishes `(a*d)/(b*c)` for the explicitly invented numbers, giving 3 odds ratio; it does not, on its own, validate the underlying biological construct.

3. **How would you identify a stronger inference?** Propose one additional control, independent repeat, rival prediction or sensitivity test that separates the principal explanation from a plausible alternative.

## Lesson 2.5 — Sample size, precision and statistical power

**Inquiry to keep in view:** At what level is the contrast independently generated? A lesson is successful when the learner can explain both the method and an observation that could undermine its proposed interpretation.

### Principle, construct and boundary

Sample-size planning begins with the estimand, variability, clustering, minimally relevant effect and tolerable error probabilities. Power is the probability of rejecting a specified null under an assumed effect; it is not the probability that the research hypothesis is true. Precision can be a more directly interpretable planning target.

### Study construction and operational decisions

For an invented two-group assay, specify a plausible standard deviation from pilot observations, a biologically meaningful mean difference, independent sample count per group, and a planned confidence-interval width. Check how the required count changes when the true variance is higher.

Convert that proposal into a miniature preregistered plan. Specify the sampling frame, independently informative unit, comparator, measurement schedule, planned primary endpoint and handling of observations that cannot be recorded. Identify which decisions must occur before anyone sees the response data. Where the proposed setting uses groups or clusters, identify the level at which a common cause or intervention can reach all observations. Where outcomes are longitudinal, state whether a difference between subjects or a change within subjects answers the question. Do not rely on the final number of data rows to settle the question of replication.

### Fictional example and worked calculation

**Method setting.** A normal approximation suggests rounding up to 36 independent observations per group for a specified effect, standard deviation and error criteria, excluding attrition and clustering.

**Invented inputs:** z_a = 1.96, z_b = 0.84, sd = 6, delta = 4.  **Arithmetic expression:** `2 * (z_a+z_b)**2 * sd**2 / delta**2`.  **Computed result:** **35.28 units per group before rounding**.

### Diagnostic failure modes and design alternatives

A pilot estimate of variability is uncertain; a formula assuming independent samples can be badly optimistic for clustered cultures. Planning by an arbitrarily chosen 'medium effect' may produce a study too small for biologically useful decisions.

Use a structured critique rather than a general warning that bias may occur. First identify the exact step where the failure could enter: recruitment, allocation, collection, extraction, labelling, exclusion, modeling or interpretation. Next determine the direction in which a particular failure might move the estimate; an unknown direction is not the same as zero effect. Finally state which independent observation could distinguish the failure mechanism from the biological explanation. This process supports targeted controls and realistic uncertainty statements instead of presenting procedural completeness as proof of rigor.

**Alternative route.** Compare superiority testing, equivalence margins and estimation-driven designs rather than treating every research aim as a conventional p-value test.

### Interpretation, transparency and a reasoned conclusion

Disclose assumptions, attrition allowance, allocation ratio and the design effect for clustering; use a sensitivity table instead of implying one sample number is universal.

**Transfer problem.** Recalculate under repeated observations where within-unit correlation changes the effective information.

### Self-assessment (answers are provided for independent study)

1. **What does the arithmetic result establish?** It establishes `2 * (z_a+z_b)**2 * sd**2 / delta**2` for the explicitly invented numbers, giving 35.28 units per group before rounding; it does not, on its own, validate the underlying biological construct.

3. **How would you identify a stronger inference?** Propose one additional control, independent repeat, rival prediction or sensitivity test that separates the principal explanation from a plausible alternative.

## Unit 02 research studio — Synthetic integrated investigation

**Case premise.** Fictional investigation: Compare seedling growth in four greenhouse blocks under a crossed nutrient-by-temperature design. Explain why one chamber for each temperature confounds chamber with treatment. Create a random assignment ledger and predeclare interaction as the primary test, leaving exploratory contrasts explicitly secondary.

### Stage A: write an analysis plan

Start with the exact main question, not a convenient available test. Write a population description, a sample eligibility rule, a biological unit, a comparator and the response scale. In the design table, separate outcome measurement from the biological construct it represents. Where an intervention exists, name the assignment mechanism and identify which participants, plots, specimens or batches share an exposure. Where the design is observational, supply a causal diagram or a carefully reasoned list of confounders and explain why each might influence both the exposure and endpoint.

The study should have at least one explicit falsification route. List an outcome or pattern that would make the leading explanation less plausible even if the average direction initially looked favorable. Also state why the same pattern might emerge from altered detection, handling, sample selection or instrument drift. This exercise prevents researchers from describing a merely possible mechanism as the only explanation for an observed contrast.

### Stage B: inspect fictional records

The accompanying unit CSV holds six invented observations with a baseline score, follow-up score, treatment label and batch identifier. No living organism was sampled to construct this file. Treat units as independent only for this classroom computation and record the assumption in your notes. Calculate changes for every row, group averages, difference in average change, the number of units contributing to each result and any imbalance across batches. Do not interpret the invented numbers as evidence of actual biological treatment response.

Before you summarize the numbers, intentionally remove one follow-up observation and write two analysis plans: a complete-case approach and a conservative sensitivity scenario. Why might missingness be related to the unobserved outcome? How would that possibility change the generality of your conclusion? For a second check, alter the assumed calibration of one instrument reading and repeat the contrast. The exercise reveals how numerical conclusions can depend on design and measurement assumptions rather than sample size alone.

### Stage C: defend the result

Write a two-hundred-word abstract for the synthetic example. It must use **unit and allocation process** to connect method to claim. Distinguish the calculation from the proposed mechanism, show the relevant uncertainty in prose, and name at least one alternative explanation. Attach an audit table with input file, analysis version, field definitions, excluded entries and a sentence describing how someone could independently rerun the exercise.

A reader who doubts the conclusion should not have to infer which values were changed after the fact. Retain your first analysis plan and place revisions beside it with dates and reasons. A corrected error is scientifically different from an undisclosed change that selects a pleasing outcome. If the stronger claim requires another experiment or validated technique, propose it explicitly instead of enlarging the present study’s conclusions.

### Stage D: ethical and practical review

Ethical boundary: sample-size justification should make scientifically and ethically defensible use of resources; it must not be used to rationalize avoidable harm or concealed exploratory testing.

The studio is a dry-lab reasoning exercise. Any translation into work with participants, animals, sensitive ecological sites or biological materials demands separate supervision, local approvals and qualified protocol design. Identifying a feasible future observation is not authorization to conduct it. Preserve accurate fictional-data labels wherever the scenario is presented.

### Submission checklist

- Research question, population, independent unit, contrast and endpoint defined without hidden assumptions.

- Synthetic source CSV preserved without manual changes; any cleaning rules scripted and documented.

- Estimate calculated with units and appropriately cautious interpretation; alternatives and exclusions explained.

- A proposed independent check targets a specific failure mode rather than merely repeating the same measurement.

- Rights, safety, oversight, sensitive data and communication boundaries considered before translating the exercise.
