# Unit 07 — Synthesis, review and reliable communication

> **Educational editorial draft.** All scenarios and data are fictional. The sixteen adjustable models in the book are idealized teaching tools, not validated predictors.

## Unit orientation

The end of analysis is not the end of method. Conclusions need a traceable chain from study design and observations to assumptions, estimates and claims. Replication collects independent evidence; computational reproduction regenerates results from shared artifacts; sensitivity analysis explores assumption dependence. Systematic reviews must identify overlap between datasets and differences in estimands before pooling. Reporting guidelines improve completeness but cannot retroactively fix confounding or selection bias. Peer review is structured scrutiny, not an infallible seal of correctness, and scientific records must allow correction.

### Learning objectives

- Identify the **evidence to defensible claims** for five different biological research decisions.

- Answer the design challenge: **What independent scrutiny would expose a hidden assumption?**

- Identify an analysis failure addressed by **How should the claim be narrowed if that assumption remains untested?**

- Produce a research artifact that makes the chain from observation to claim auditable.

## A method is an argument, not just a procedure

The topics in this unit share a concern with evidence to defensible claims. A sound method specifies what is being compared and explains why the measured response says something about the broader biological system. A result is interpretable only at the level supported by assignment, selection, calibration and analysis. The study may produce exact digital values while still leaving ecological or mechanistic uncertainty that cannot be converted into additional decimal places. In this unit, map decisions made before measurement separately from choices introduced while inspecting results. An acceptable alternative design may target a different estimand; that can be a strength when the alternatives are made visible.

### Practice before computation

Writing workshop: construct an evidence-to-claim table and tag each claim as descriptive, associational, causal or predictive. Reproduce a plotted result from an analysis script, propose an independent replication, and prepare a short sensitivity annex. Choose a reporting checklist that matches study type. Critique an abstract that confuses nonsignificance with absence of an effect.

### The running scenario

Fictional investigation: Synthesize several invented ecological intervention studies whose outcomes and sample designs differ. Explain why a pooled number may be unreasonable and create a narrative synthesis with transparent exclusion reasons and uncertainty.

### Responsibility and scope

Ethical boundary: accurately describe uncertainty and disclose conflicts, corrections, protocol changes and unavailable data rather than treating transparency as optional decoration.

## Five lessons

## Lesson 7.1 — Bias, validity and sensitivity analysis

**Inquiry to keep in view:** What independent scrutiny would expose a hidden assumption? A lesson is successful when the learner can explain both the method and an observation that could undermine its proposed interpretation.

### Principle, construct and boundary

Internal validity concerns whether the study's inference follows from its design; external validity concerns applicability beyond sampled conditions. Construct validity asks whether a measurement corresponds to the concept of interest. A sensitivity analysis deliberately varies assumptions to find where a conclusion changes.

### Study construction and operational decisions

In an invented intervention on pond algae, vary assumptions about unmeasured temperature differences, missing samples and endpoint calibration, then compare whether the treatment effect remains decision-relevant.

Convert that proposal into a miniature preregistered plan. Specify the sampling frame, independently informative unit, comparator, measurement schedule, planned primary endpoint and handling of observations that cannot be recorded. Identify which decisions must occur before anyone sees the response data. Where the proposed setting uses groups or clusters, identify the level at which a common cause or intervention can reach all observations. Where outcomes are longitudinal, state whether a difference between subjects or a change within subjects answers the question. Do not rely on the final number of data rows to settle the question of replication.

### Fictional example and worked calculation

**Method setting.** An assumed bias adjustment changes the result by 2.1 units; whether the correction is plausible must be argued independently.

**Invented inputs:** baseline = 5.2, corrected = 3.1.  **Arithmetic expression:** `baseline - corrected`.  **Computed result:** **2.1 effect units**.

### Diagnostic failure modes and design alternatives

Stable results across several similar regression specifications do not remove shared measurement bias. A robust coefficient is still about the wrong quantity if the instrument reports fluorescence but the conclusion claims cell division.

Use a structured critique rather than a general warning that bias may occur. First identify the exact step where the failure could enter: recruitment, allocation, collection, extraction, labelling, exclusion, modeling or interpretation. Next determine the direction in which a particular failure might move the estimate; an unknown direction is not the same as zero effect. Finally state which independent observation could distinguish the failure mechanism from the biological explanation. This process supports targeted controls and realistic uncertainty statements instead of presenting procedural completeness as proof of rigor.

**Alternative route.** Contrast negative controls, quantitative bias analysis, alternative outcome definitions and independent replication; each targets a different possible failure.

### Interpretation, transparency and a reasoned conclusion

Report which assumptions are empirically checked, which remain hypothetical, and how large a bias would have to be to reverse the conclusion.

**Transfer problem.** Transfer this method to genomic association studies, where ancestry-related structure is a potential rival explanation.

### Self-assessment (answers are provided for independent study)

1. **What does the arithmetic result establish?** It establishes `baseline - corrected` for the explicitly invented numbers, giving 2.1 effect units; it does not, on its own, validate the underlying biological construct.

3. **How would you identify a stronger inference?** Propose one additional control, independent repeat, rival prediction or sensitivity test that separates the principal explanation from a plausible alternative.

## Lesson 7.2 — Replication, reproducibility and robustness

**Inquiry to keep in view:** What independent scrutiny would expose a hidden assumption? A lesson is successful when the learner can explain both the method and an observation that could undermine its proposed interpretation.

### Principle, construct and boundary

Computational reproducibility means others can regenerate results from specified code and data; experimental replication collects independent new evidence. Robustness assesses whether conclusions survive reasonable methodological choices. These are related but separate properties of knowledge.

### Study construction and operational decisions

Reanalyze a fictional soil assay dataset using a frozen script, then plan a new independent experiment in a different batch of soil with the same prespecified primary outcome. Record what changed and why.

Convert that proposal into a miniature preregistered plan. Specify the sampling frame, independently informative unit, comparator, measurement schedule, planned primary endpoint and handling of observations that cannot be recorded. Identify which decisions must occur before anyone sees the response data. Where the proposed setting uses groups or clusters, identify the level at which a common cause or intervention can reach all observations. Where outcomes are longitudinal, state whether a difference between subjects or a change within subjects answers the question. Do not rely on the final number of data rows to settle the question of replication.

### Fictional example and worked calculation

**Method setting.** The size of a difference across studies has to be interpreted with uncertainty, context and predeclared compatibility criteria.

**Invented inputs:** replication = 1.8, original = 2.5.  **Arithmetic expression:** `abs(replication - original)`.  **Computed result:** **0.7 effect units**.

### Diagnostic failure modes and design alternatives

Recreating a graph from the original data does not validate the sampling process, and a failed replication may arise from meaningful contextual differences rather than fraud.

Use a structured critique rather than a general warning that bias may occur. First identify the exact step where the failure could enter: recruitment, allocation, collection, extraction, labelling, exclusion, modeling or interpretation. Next determine the direction in which a particular failure might move the estimate; an unknown direction is not the same as zero effect. Finally state which independent observation could distinguish the failure mechanism from the biological explanation. This process supports targeted controls and realistic uncertainty statements instead of presenting procedural completeness as proof of rigor.

**Alternative route.** Compare direct replication of a defined contrast with conceptual replication using another measurement to test the same explanation.

### Interpretation, transparency and a reasoned conclusion

Share the conditions required to reproduce the analysis and the protocol deviations that matter for experimental comparison; avoid treating disagreement as automatically decisive.

**Transfer problem.** Extend the concept to collaborative projects using independent laboratories and differing reagent lots.

### Self-assessment (answers are provided for independent study)

1. **What does the arithmetic result establish?** It establishes `abs(replication - original)` for the explicitly invented numbers, giving 0.7 effect units; it does not, on its own, validate the underlying biological construct.

3. **How would you identify a stronger inference?** Propose one additional control, independent repeat, rival prediction or sensitivity test that separates the principal explanation from a plausible alternative.

## Lesson 7.3 — Evidence synthesis and meta-analysis

**Inquiry to keep in view:** What independent scrutiny would expose a hidden assumption? A lesson is successful when the learner can explain both the method and an observation that could undermine its proposed interpretation.

### Principle, construct and boundary

Synthesis asks whether studies estimate compatible quantities under comparable populations and interventions. Pooling does not erase measurement bias, selective reporting or heterogeneity. An effect average can be misleading when mechanisms vary by ecosystem or organism.

### Study construction and operational decisions

In a fictional synthesis of fertilizer studies, extract effect measures with direction harmonized, standard errors, setting, allocation unit and risk-of-bias assessments before computing a pooled estimate.

Convert that proposal into a miniature preregistered plan. Specify the sampling frame, independently informative unit, comparator, measurement schedule, planned primary endpoint and handling of observations that cannot be recorded. Identify which decisions must occur before anyone sees the response data. Where the proposed setting uses groups or clusters, identify the level at which a common cause or intervention can reach all observations. Where outcomes are longitudinal, state whether a difference between subjects or a change within subjects answers the question. Do not rely on the final number of data rows to settle the question of replication.

### Fictional example and worked calculation

**Method setting.** The lower-variance estimate receives more weight under an illustrative fixed-effect model; methodological comparability is assumed, not proved.

**Invented inputs:** e1 = 1.5, e2 = 2.5, v1 = 1, v2 = 4.  **Arithmetic expression:** `(e1/v1+e2/v2)/(1/v1+1/v2)`.  **Computed result:** **1.7 effect units**.

### Diagnostic failure modes and design alternatives

Multiple publications of the same trial produce double counting; heterogeneity cannot be diagnosed solely by a convenient threshold. Funnel asymmetry can arise for several reasons besides publication bias.

Use a structured critique rather than a general warning that bias may occur. First identify the exact step where the failure could enter: recruitment, allocation, collection, extraction, labelling, exclusion, modeling or interpretation. Next determine the direction in which a particular failure might move the estimate; an unknown direction is not the same as zero effect. Finally state which independent observation could distinguish the failure mechanism from the biological explanation. This process supports targeted controls and realistic uncertainty statements instead of presenting procedural completeness as proof of rigor.

**Alternative route.** Compare fixed-effect synthesis when one common effect is a plausible target with random-effects modeling that acknowledges a distribution of effects; neither rescues fundamentally incomparable studies.

### Interpretation, transparency and a reasoned conclusion

Show individual-study estimates, model assumptions, interval estimates, sensitivity to small studies and reasons not to pool some evidence.

**Transfer problem.** Apply the same logic to animal model studies with different strains, stages and endpoints.

### Self-assessment (answers are provided for independent study)

1. **What does the arithmetic result establish?** It establishes `(e1/v1+e2/v2)/(1/v1+1/v2)` for the explicitly invented numbers, giving 1.7 effect units; it does not, on its own, validate the underlying biological construct.

3. **How would you identify a stronger inference?** Propose one additional control, independent repeat, rival prediction or sensitivity test that separates the principal explanation from a plausible alternative.

## Lesson 7.4 — Reporting guidelines and transparent manuscripts

**Inquiry to keep in view:** What independent scrutiny would expose a hidden assumption? A lesson is successful when the learner can explain both the method and an observation that could undermine its proposed interpretation.

### Principle, construct and boundary

A methods paper should let readers reconstruct the sampling, experimental unit, exclusions, instruments, analysis, and limitations. Reporting checklists such as CONSORT, STROBE, PRISMA, ARRIVE and related discipline-specific standards support completeness but do not guarantee good design. The guideline must match study type.

### Study construction and operational decisions

Draft a mock report of a randomized plant experiment with clear outcomes, allocation procedures, sample flow, uncertainty, all planned analyses and protocol deviations. Compare the draft with an appropriate reporting checklist rather than choosing one by reputation.

Convert that proposal into a miniature preregistered plan. Specify the sampling frame, independently informative unit, comparator, measurement schedule, planned primary endpoint and handling of observations that cannot be recorded. Identify which decisions must occur before anyone sees the response data. Where the proposed setting uses groups or clusters, identify the level at which a common cause or intervention can reach all observations. Where outcomes are longitudinal, state whether a difference between subjects or a change within subjects answers the question. Do not rely on the final number of data rows to settle the question of replication.

### Fictional example and worked calculation

**Method setting.** Eight of ten registered outcomes appear in the manuscript; investigate the two omitted endpoints before accepting reporting completeness.

**Invented inputs:** reported = 8, planned = 10.  **Arithmetic expression:** `reported/planned * 100`.  **Computed result:** **80 percent**.

### Diagnostic failure modes and design alternatives

Checklist completion can become ritual if authors obscure biased allocation, misdescribe biological replication, or omit non-significant outcomes. Style and statistical significance cannot substitute for traceable evidence.

Use a structured critique rather than a general warning that bias may occur. First identify the exact step where the failure could enter: recruitment, allocation, collection, extraction, labelling, exclusion, modeling or interpretation. Next determine the direction in which a particular failure might move the estimate; an unknown direction is not the same as zero effect. Finally state which independent observation could distinguish the failure mechanism from the biological explanation. This process supports targeted controls and realistic uncertainty statements instead of presenting procedural completeness as proof of rigor.

**Alternative route.** Distinguish prospective design registration from retrospective reporting: the latter documents what happened, while the former records intentions before outcomes were known.

### Interpretation, transparency and a reasoned conclusion

Publish data availability, code availability, funding, conflicts, ethical approvals where applicable, and precise limits to the claims being made.

**Transfer problem.** Extend to observational studies where STROBE-style transparency about confounders and missingness is essential.

### Self-assessment (answers are provided for independent study)

1. **What does the arithmetic result establish?** It establishes `reported/planned * 100` for the explicitly invented numbers, giving 80 percent; it does not, on its own, validate the underlying biological construct.

3. **How would you identify a stronger inference?** Propose one additional control, independent repeat, rival prediction or sensitivity test that separates the principal explanation from a plausible alternative.

## Lesson 7.5 — Peer review, corrections and responsible claims

**Inquiry to keep in view:** What independent scrutiny would expose a hidden assumption? A lesson is successful when the learner can explain both the method and an observation that could undermine its proposed interpretation.

### Principle, construct and boundary

Peer review evaluates evidence but is not a certificate of truth; reviewers may have limited access to raw data or specialist methods. Editorial accountability includes corrections, versioning, responsiveness to critique and proportionate claims. Scientific communication should reflect uncertainty without making all findings sound equally weak.

### Study construction and operational decisions

For a fictional article on habitat restoration, prepare an evidence-to-claim matrix linking every headline conclusion to figures, analysis scripts, units and plausible alternative explanations. Invite a skeptical methodological review before submission.

Convert that proposal into a miniature preregistered plan. Specify the sampling frame, independently informative unit, comparator, measurement schedule, planned primary endpoint and handling of observations that cannot be recorded. Identify which decisions must occur before anyone sees the response data. Where the proposed setting uses groups or clusters, identify the level at which a common cause or intervention can reach all observations. Where outcomes are longitudinal, state whether a difference between subjects or a change within subjects answers the question. Do not rely on the final number of data rows to settle the question of replication.

### Fictional example and worked calculation

**Method setting.** Nine of twelve detected problems were resolved; remaining errors require a transparent correction plan.

**Invented inputs:** corrected = 9, identified = 12.  **Arithmetic expression:** `corrected/identified * 100`.  **Computed result:** **75 percent**.

### Diagnostic failure modes and design alternatives

Overstating mechanism from association, presenting significance as certainty, and burying failed quality controls create avoidable epistemic harm. Withholding reproducibility material without explanation makes error correction harder.

Use a structured critique rather than a general warning that bias may occur. First identify the exact step where the failure could enter: recruitment, allocation, collection, extraction, labelling, exclusion, modeling or interpretation. Next determine the direction in which a particular failure might move the estimate; an unknown direction is not the same as zero effect. Finally state which independent observation could distinguish the failure mechanism from the biological explanation. This process supports targeted controls and realistic uncertainty statements instead of presenting procedural completeness as proof of rigor.

**Alternative route.** A preprint may accelerate discussion, a reviewed article adds structured scrutiny, and a registered report shifts important design assessment ahead of observing results; none removes the need for later correction.

### Interpretation, transparency and a reasoned conclusion

Preserve review responses and dated versions, distinguish honest error from misconduct allegations, and correct discovered mistakes proportionately.

**Transfer problem.** Apply the matrix to outreach material for policy makers, where concise writing must preserve the boundaries of evidence.

### Self-assessment (answers are provided for independent study)

1. **What does the arithmetic result establish?** It establishes `corrected/identified * 100` for the explicitly invented numbers, giving 75 percent; it does not, on its own, validate the underlying biological construct.

3. **How would you identify a stronger inference?** Propose one additional control, independent repeat, rival prediction or sensitivity test that separates the principal explanation from a plausible alternative.

## Unit 07 research studio — Synthetic integrated investigation

**Case premise.** Fictional investigation: Synthesize several invented ecological intervention studies whose outcomes and sample designs differ. Explain why a pooled number may be unreasonable and create a narrative synthesis with transparent exclusion reasons and uncertainty.

### Stage A: write an analysis plan

Start with the exact main question, not a convenient available test. Write a population description, a sample eligibility rule, a biological unit, a comparator and the response scale. In the design table, separate outcome measurement from the biological construct it represents. Where an intervention exists, name the assignment mechanism and identify which participants, plots, specimens or batches share an exposure. Where the design is observational, supply a causal diagram or a carefully reasoned list of confounders and explain why each might influence both the exposure and endpoint.

The study should have at least one explicit falsification route. List an outcome or pattern that would make the leading explanation less plausible even if the average direction initially looked favorable. Also state why the same pattern might emerge from altered detection, handling, sample selection or instrument drift. This exercise prevents researchers from describing a merely possible mechanism as the only explanation for an observed contrast.

### Stage B: inspect fictional records

The accompanying unit CSV holds six invented observations with a baseline score, follow-up score, treatment label and batch identifier. No living organism was sampled to construct this file. Treat units as independent only for this classroom computation and record the assumption in your notes. Calculate changes for every row, group averages, difference in average change, the number of units contributing to each result and any imbalance across batches. Do not interpret the invented numbers as evidence of actual biological treatment response.

Before you summarize the numbers, intentionally remove one follow-up observation and write two analysis plans: a complete-case approach and a conservative sensitivity scenario. Why might missingness be related to the unobserved outcome? How would that possibility change the generality of your conclusion? For a second check, alter the assumed calibration of one instrument reading and repeat the contrast. The exercise reveals how numerical conclusions can depend on design and measurement assumptions rather than sample size alone.

### Stage C: defend the result

Write a two-hundred-word abstract for the synthetic example. It must use **evidence to defensible claims** to connect method to claim. Distinguish the calculation from the proposed mechanism, show the relevant uncertainty in prose, and name at least one alternative explanation. Attach an audit table with input file, analysis version, field definitions, excluded entries and a sentence describing how someone could independently rerun the exercise.

A reader who doubts the conclusion should not have to infer which values were changed after the fact. Retain your first analysis plan and place revisions beside it with dates and reasons. A corrected error is scientifically different from an undisclosed change that selects a pleasing outcome. If the stronger claim requires another experiment or validated technique, propose it explicitly instead of enlarging the present study’s conclusions.

### Stage D: ethical and practical review

Ethical boundary: accurately describe uncertainty and disclose conflicts, corrections, protocol changes and unavailable data rather than treating transparency as optional decoration.

The studio is a dry-lab reasoning exercise. Any translation into work with participants, animals, sensitive ecological sites or biological materials demands separate supervision, local approvals and qualified protocol design. Identifying a feasible future observation is not authorization to conduct it. Preserve accurate fictional-data labels wherever the scenario is presented.

### Submission checklist

- Research question, population, independent unit, contrast and endpoint defined without hidden assumptions.

- Synthetic source CSV preserved without manual changes; any cleaning rules scripted and documented.

- Estimate calculated with units and appropriately cautious interpretation; alternatives and exclusions explained.

- A proposed independent check targets a specific failure mode rather than merely repeating the same measurement.

- Rights, safety, oversight, sensitive data and communication boundaries considered before translating the exercise.
