# Unit 04 — Data stewardship and reproducible computation

> **Educational editorial draft.** All scenarios and data are fictional. The sixteen adjustable models in the book are idealized teaching tools, not validated predictors.

## Unit orientation

A biological dataset is more than a numerical matrix. The observational unit, sampling context, variable meaning, measurement unit, transformation history and consent conditions determine what analysts can conclude. Stable identifiers prevent accidental many-to-many merges, metadata preserve interpretability, and scripted checks expose impossible values. Reproducible code means results can be regenerated from specified inputs and environments, whereas correct scientific interpretation still depends on valid assumptions. FAIR data are findable, accessible through appropriate controls, interoperable and reusable; 'accessible' does not necessarily mean unconditionally public. Protected data may need restricted access with public metadata.

### Learning objectives

- Identify the **records and executable lineage** for five different biological research decisions.

- Answer the design challenge: **Can another researcher trace an output to an unchanged input?**

- Identify an analysis failure addressed by **What is lost if missing observations or earlier file versions disappear?**

- Produce a research artifact that makes the chain from observation to claim auditable.

## A method is an argument, not just a procedure

The topics in this unit share a concern with records and executable lineage. A sound method specifies what is being compared and explains why the measured response says something about the broader biological system. A result is interpretable only at the level supported by assignment, selection, calibration and analysis. The study may produce exact digital values while still leaving ecological or mechanistic uncertainty that cannot be converted into additional decimal places. In this unit, map decisions made before measurement separately from choices introduced while inspecting results. An acceptable alternative design may target a different estimand; that can be a strength when the alternatives are made visible.

### Practice before computation

Computational workshop: create a data dictionary, frozen raw table and analysis-ready view for a simple pot growth experiment. Check unique pot keys, consistent sample time, allowed treatment labels and a checksum for each source file. Simulate two types of missingness and compare complete-case results to a plausible sensitivity scenario. Run scripts from a clean checkout, not a notebook containing hidden state.

### The running scenario

Fictional investigation: Reconstruct a small multi-table ecological dataset from eight invented site observations. Produce metadata, a cleaning log, an automated validation failure on duplicate IDs, and a report that separates measurements from inferred quantities.

### Responsibility and scope

Ethical boundary: cleaning operations must be reversible and transparent; sensitive coordinates, personal records or community-governed observations cannot be published merely for computational convenience.

## Five lessons

## Lesson 4.1 — Data dictionaries and tidy observation tables

**Inquiry to keep in view:** Can another researcher trace an output to an unchanged input? A lesson is successful when the learner can explain both the method and an observation that could undermine its proposed interpretation.

### Principle, construct and boundary

A data dictionary defines each variable's biological meaning, allowed values, units, missingness codes and collection context. A rectangular table is not automatically analyzable; rows must correspond to a defined observation unit and column names must not smuggle treatment information into values.

### Study construction and operational decisions

For fictional pot growth data, create separate tables for pot assignments, repeated observations and instrument calibration, joined by stable IDs. Use one row per pot-time observation while preserving the randomized pot as the treatment unit.

Convert that proposal into a miniature preregistered plan. Specify the sampling frame, independently informative unit, comparator, measurement schedule, planned primary endpoint and handling of observations that cannot be recorded. Identify which decisions must occur before anyone sees the response data. Where the proposed setting uses groups or clusters, identify the level at which a common cause or intervention can reach all observations. Where outcomes are longitudinal, state whether a difference between subjects or a change within subjects answers the question. Do not rely on the final number of data rows to settle the question of replication.

### Fictional example and worked calculation

**Method setting.** Four repeated identifiers among two hundred observations require investigation rather than automatic deletion.

**Invented inputs:** duplicates = 4, rows = 200.  **Arithmetic expression:** `duplicates / rows * 100`.  **Computed result:** **2 percent**.

### Diagnostic failure modes and design alternatives

Combining absent observations, zero growth and below-detection readings under a single '0' code destroys information. Mutable sample names and ambiguous date formats break joins silently.

Use a structured critique rather than a general warning that bias may occur. First identify the exact step where the failure could enter: recruitment, allocation, collection, extraction, labelling, exclusion, modeling or interpretation. Next determine the direction in which a particular failure might move the estimate; an unknown direction is not the same as zero effect. Finally state which independent observation could distinguish the failure mechanism from the biological explanation. This process supports targeted controls and realistic uncertainty statements instead of presenting procedural completeness as proof of rigor.

**Alternative route.** Compare a wide table useful for manual viewing with a long table useful for modeling repeated outcomes, documenting any reshaping decisions so no replicate disappears.

### Interpretation, transparency and a reasoned conclusion

Validate identifier uniqueness, legal units, time order, reference integrity and impossible values before estimating effects.

**Transfer problem.** Transfer this practice to sequencing metadata where lane, library, biological specimen and participant require distinct IDs.

### Self-assessment (answers are provided for independent study)

1. **What does the arithmetic result establish?** It establishes `duplicates / rows * 100` for the explicitly invented numbers, giving 2 percent; it does not, on its own, validate the underlying biological construct.

3. **How would you identify a stronger inference?** Propose one additional control, independent repeat, rival prediction or sensitivity test that separates the principal explanation from a plausible alternative.

## Lesson 4.2 — Provenance, metadata and FAIR data

**Inquiry to keep in view:** Can another researcher trace an output to an unchanged input? A lesson is successful when the learner can explain both the method and an observation that could undermine its proposed interpretation.

### Principle, construct and boundary

Provenance answers where data came from, how they were transformed and who is accountable for each transformation. FAIR refers to findable, accessible, interoperable and reusable data; it does not mean every dataset must be publicly disclosed without restriction. Machine-readable identifiers and controlled vocabularies support linkage across projects.

### Study construction and operational decisions

Build a manifest for a fictional stream ecology dataset including spatial resolution, sampling method, units, missingness, license, access category, instrument versions and a persistent identifier for the published release.

Convert that proposal into a miniature preregistered plan. Specify the sampling frame, independently informative unit, comparator, measurement schedule, planned primary endpoint and handling of observations that cannot be recorded. Identify which decisions must occur before anyone sees the response data. Where the proposed setting uses groups or clusters, identify the level at which a common cause or intervention can reach all observations. Where outcomes are longitudinal, state whether a difference between subjects or a change within subjects answers the question. Do not rely on the final number of data rows to settle the question of replication.

### Fictional example and worked calculation

**Method setting.** A provisional checklist finds eighteen of twenty-four required fields present; completeness does not certify that descriptions are correct.

**Invented inputs:** required_present = 18, required_total = 24.  **Arithmetic expression:** `required_present / required_total * 100`.  **Computed result:** **75 percent**.

### Diagnostic failure modes and design alternatives

A spreadsheet named 'final_revised_2' conveys little history, and a public download without consent may violate confidentiality. Even a well-documented file can be scientifically unusable if key sampling assumptions were never captured.

Use a structured critique rather than a general warning that bias may occur. First identify the exact step where the failure could enter: recruitment, allocation, collection, extraction, labelling, exclusion, modeling or interpretation. Next determine the direction in which a particular failure might move the estimate; an unknown direction is not the same as zero effect. Finally state which independent observation could distinguish the failure mechanism from the biological explanation. This process supports targeted controls and realistic uncertainty statements instead of presenting procedural completeness as proof of rigor.

**Alternative route.** Distinguish discoverable metadata from unrestricted raw data: sensitive location or individual information may remain access-controlled with publicly findable descriptions.

### Interpretation, transparency and a reasoned conclusion

Test whether an unfamiliar researcher can identify the observational unit, units of measure, caveats, rights to reuse and links to analytical code.

**Transfer problem.** Apply these questions to endangered-species location data, where full coordinate publication might create additional risk.

### Self-assessment (answers are provided for independent study)

1. **What does the arithmetic result establish?** It establishes `required_present / required_total * 100` for the explicitly invented numbers, giving 75 percent; it does not, on its own, validate the underlying biological construct.

3. **How would you identify a stronger inference?** Propose one additional control, independent repeat, rival prediction or sensitivity test that separates the principal explanation from a plausible alternative.

## Lesson 4.3 — Data cleaning, missingness and transformations

**Inquiry to keep in view:** Can another researcher trace an output to an unchanged input? A lesson is successful when the learner can explain both the method and an observation that could undermine its proposed interpretation.

### Principle, construct and boundary

Cleaning is part of the analysis, not a neutral prelude. Range checks, duplicates, outlier investigation, transformations and missing-data choices can all change the target estimand. Missing completely at random, missing at random conditional on observed variables, and not missing at random have different implications.

### Study construction and operational decisions

In a fictional metabolite dataset, preserve raw values, label instrument failure separately from true zeros, and produce a scripted table of missingness by batch and group before choosing any imputation procedure.

Convert that proposal into a miniature preregistered plan. Specify the sampling frame, independently informative unit, comparator, measurement schedule, planned primary endpoint and handling of observations that cannot be recorded. Identify which decisions must occur before anyone sees the response data. Where the proposed setting uses groups or clusters, identify the level at which a common cause or intervention can reach all observations. Where outcomes are longitudinal, state whether a difference between subjects or a change within subjects answers the question. Do not rely on the final number of data rows to settle the question of replication.

### Fictional example and worked calculation

**Method setting.** An eighty-four percent complete-case rate says nothing by itself about whether missingness is ignorable.

**Invented inputs:** complete = 84, total = 100.  **Arithmetic expression:** `complete/total*100`.  **Computed result:** **84 percent**.

### Diagnostic failure modes and design alternatives

Dropping all incomplete rows may distort representation if failure rates depend on treatment or concentration; deleting extreme biological observations without evidence of error destroys legitimate variation.

Use a structured critique rather than a general warning that bias may occur. First identify the exact step where the failure could enter: recruitment, allocation, collection, extraction, labelling, exclusion, modeling or interpretation. Next determine the direction in which a particular failure might move the estimate; an unknown direction is not the same as zero effect. Finally state which independent observation could distinguish the failure mechanism from the biological explanation. This process supports targeted controls and realistic uncertainty statements instead of presenting procedural completeness as proof of rigor.

**Alternative route.** Compare complete-case analysis, multiple imputation under explicit assumptions, and sensitivity scenarios for nonrandom missingness rather than claiming one algorithm always repairs the problem.

### Interpretation, transparency and a reasoned conclusion

Publish both a cleaning log and a side-by-side table of how each documented decision affects summary counts and effect estimates.

**Transfer problem.** Extend the audit to long-term surveys with gaps concentrated in storms or hard-to-reach field seasons.

### Self-assessment (answers are provided for independent study)

1. **What does the arithmetic result establish?** It establishes `complete/total*100` for the explicitly invented numbers, giving 84 percent; it does not, on its own, validate the underlying biological construct.

3. **How would you identify a stronger inference?** Propose one additional control, independent repeat, rival prediction or sensitivity test that separates the principal explanation from a plausible alternative.

## Lesson 4.4 — Version control, notebooks and dependency management

**Inquiry to keep in view:** Can another researcher trace an output to an unchanged input? A lesson is successful when the learner can explain both the method and an observation that could undermine its proposed interpretation.

### Principle, construct and boundary

A reproducible analysis records source code, input versions, environment and a sequence of transformations that can be rerun. Git versions text and code well; large raw datasets need appropriate storage and checksum strategies. Notebooks are useful teaching interfaces but hidden execution state can make their outputs misleading.

### Study construction and operational decisions

For a fictional greenhouse project, use a repository containing scripts, a locked package environment, tests for data validation, and an analysis entry point that creates figures and tables from a frozen data snapshot.

Convert that proposal into a miniature preregistered plan. Specify the sampling frame, independently informative unit, comparator, measurement schedule, planned primary endpoint and handling of observations that cannot be recorded. Identify which decisions must occur before anyone sees the response data. Where the proposed setting uses groups or clusters, identify the level at which a common cause or intervention can reach all observations. Where outcomes are longitudinal, state whether a difference between subjects or a change within subjects answers the question. Do not rely on the final number of data rows to settle the question of replication.

### Fictional example and worked calculation

**Method setting.** Three of fifty hashes differ across snapshots; investigate which files changed before declaring a reproducible run.

**Invented inputs:** matching = 47, tested = 50.  **Arithmetic expression:** `matching / tested * 100`.  **Computed result:** **94 percent**.

### Diagnostic failure modes and design alternatives

Manually editing a results spreadsheet after code execution creates an undocumented branch; a notebook that works only after running cells in an unusual order is not a reproducible workflow.

Use a structured critique rather than a general warning that bias may occur. First identify the exact step where the failure could enter: recruitment, allocation, collection, extraction, labelling, exclusion, modeling or interpretation. Next determine the direction in which a particular failure might move the estimate; an unknown direction is not the same as zero effect. Finally state which independent observation could distinguish the failure mechanism from the biological explanation. This process supports targeted controls and realistic uncertainty statements instead of presenting procedural completeness as proof of rigor.

**Alternative route.** Contrast container-based environments and lightweight dependency lockfiles: both reduce variability, but neither guarantees identical behavior across hardware or proves biological validity.

### Interpretation, transparency and a reasoned conclusion

Make a fresh-checkout test part of the release, record hashes of input files, and mark intentional deviations from historical analysis versions.

**Transfer problem.** Carry this workflow to collaborative image analysis where annotation files and model weights also require provenance.

### Self-assessment (answers are provided for independent study)

1. **What does the arithmetic result establish?** It establishes `matching / tested * 100` for the explicitly invented numbers, giving 94 percent; it does not, on its own, validate the underlying biological construct.

3. **How would you identify a stronger inference?** Propose one additional control, independent repeat, rival prediction or sensitivity test that separates the principal explanation from a plausible alternative.

## Lesson 4.5 — Validation, simulation and computational robustness

**Inquiry to keep in view:** Can another researcher trace an output to an unchanged input? A lesson is successful when the learner can explain both the method and an observation that could undermine its proposed interpretation.

### Principle, construct and boundary

Software tests establish that code behaves as specified; they do not by themselves establish that a scientific model is correct for reality. Unit tests, integration tests, synthetic-data checks and sensitivity analyses operate at different levels. Simulation is particularly useful for exposing estimator bias under known data-generating assumptions.

### Study construction and operational decisions

Build a small synthetic dataset with a known treatment effect, clusters and missingness. Confirm a model can recover its intended parameter under favorable conditions, then alter clustering and selection to identify failure boundaries.

Convert that proposal into a miniature preregistered plan. Specify the sampling frame, independently informative unit, comparator, measurement schedule, planned primary endpoint and handling of observations that cannot be recorded. Identify which decisions must occur before anyone sees the response data. Where the proposed setting uses groups or clusters, identify the level at which a common cause or intervention can reach all observations. Where outcomes are longitudinal, state whether a difference between subjects or a change within subjects answers the question. Do not rely on the final number of data rows to settle the question of replication.

### Fictional example and worked calculation

**Method setting.** A simulation with known truth allows direct bias calculation; the result depends on the assumed data-generating mechanism.

**Invented inputs:** estimated = 2.4, true_effect = 3.  **Arithmetic expression:** `estimated - true_effect`.  **Computed result:** **-0.6 effect units**.

### Diagnostic failure modes and design alternatives

A program returning the expected number for one input may contain compensating errors; using the same function to generate and verify results is a circular test.

Use a structured critique rather than a general warning that bias may occur. First identify the exact step where the failure could enter: recruitment, allocation, collection, extraction, labelling, exclusion, modeling or interpretation. Next determine the direction in which a particular failure might move the estimate; an unknown direction is not the same as zero effect. Finally state which independent observation could distinguish the failure mechanism from the biological explanation. This process supports targeted controls and realistic uncertainty statements instead of presenting procedural completeness as proof of rigor.

**Alternative route.** Compare mathematical checks with a second implementation, external benchmark datasets where permissible, and stress tests over plausible ranges of conditions.

### Interpretation, transparency and a reasoned conclusion

Record expected outcomes, tolerances, random seeds and failing cases; a robust pipeline should fail loudly when schema requirements are violated.

**Transfer problem.** Apply this approach to species-distribution models where predictive performance within a region may collapse under geographic transfer.

### Self-assessment (answers are provided for independent study)

1. **What does the arithmetic result establish?** It establishes `estimated - true_effect` for the explicitly invented numbers, giving -0.6 effect units; it does not, on its own, validate the underlying biological construct.

3. **How would you identify a stronger inference?** Propose one additional control, independent repeat, rival prediction or sensitivity test that separates the principal explanation from a plausible alternative.

## Unit 04 research studio — Synthetic integrated investigation

**Case premise.** Fictional investigation: Reconstruct a small multi-table ecological dataset from eight invented site observations. Produce metadata, a cleaning log, an automated validation failure on duplicate IDs, and a report that separates measurements from inferred quantities.

### Stage A: write an analysis plan

Start with the exact main question, not a convenient available test. Write a population description, a sample eligibility rule, a biological unit, a comparator and the response scale. In the design table, separate outcome measurement from the biological construct it represents. Where an intervention exists, name the assignment mechanism and identify which participants, plots, specimens or batches share an exposure. Where the design is observational, supply a causal diagram or a carefully reasoned list of confounders and explain why each might influence both the exposure and endpoint.

The study should have at least one explicit falsification route. List an outcome or pattern that would make the leading explanation less plausible even if the average direction initially looked favorable. Also state why the same pattern might emerge from altered detection, handling, sample selection or instrument drift. This exercise prevents researchers from describing a merely possible mechanism as the only explanation for an observed contrast.

### Stage B: inspect fictional records

The accompanying unit CSV holds six invented observations with a baseline score, follow-up score, treatment label and batch identifier. No living organism was sampled to construct this file. Treat units as independent only for this classroom computation and record the assumption in your notes. Calculate changes for every row, group averages, difference in average change, the number of units contributing to each result and any imbalance across batches. Do not interpret the invented numbers as evidence of actual biological treatment response.

Before you summarize the numbers, intentionally remove one follow-up observation and write two analysis plans: a complete-case approach and a conservative sensitivity scenario. Why might missingness be related to the unobserved outcome? How would that possibility change the generality of your conclusion? For a second check, alter the assumed calibration of one instrument reading and repeat the contrast. The exercise reveals how numerical conclusions can depend on design and measurement assumptions rather than sample size alone.

### Stage C: defend the result

Write a two-hundred-word abstract for the synthetic example. It must use **records and executable lineage** to connect method to claim. Distinguish the calculation from the proposed mechanism, show the relevant uncertainty in prose, and name at least one alternative explanation. Attach an audit table with input file, analysis version, field definitions, excluded entries and a sentence describing how someone could independently rerun the exercise.

A reader who doubts the conclusion should not have to infer which values were changed after the fact. Retain your first analysis plan and place revisions beside it with dates and reasons. A corrected error is scientifically different from an undisclosed change that selects a pleasing outcome. If the stronger claim requires another experiment or validated technique, propose it explicitly instead of enlarging the present study’s conclusions.

### Stage D: ethical and practical review

Ethical boundary: cleaning operations must be reversible and transparent; sensitive coordinates, personal records or community-governed observations cannot be published merely for computational convenience.

The studio is a dry-lab reasoning exercise. Any translation into work with participants, animals, sensitive ecological sites or biological materials demands separate supervision, local approvals and qualified protocol design. Identifying a feasible future observation is not authorization to conduct it. Preserve accurate fictional-data labels wherever the scenario is presented.

### Submission checklist

- Research question, population, independent unit, contrast and endpoint defined without hidden assumptions.

- Synthetic source CSV preserved without manual changes; any cleaning rules scripted and documented.

- Estimate calculated with units and appropriately cautious interpretation; alternatives and exclusions explained.

- A proposed independent check targets a specific failure mode rather than merely repeating the same measurement.

- Rights, safety, oversight, sensitive data and communication boundaries considered before translating the exercise.
