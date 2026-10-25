# Unit 01 — Research questions, evidence and scientific judgment

> **Educational editorial draft.** All scenarios and data are fictional. The sixteen adjustable models in the book are idealized teaching tools, not validated predictors.

## Unit orientation

Biology moves between descriptions, mechanisms and interventions. A question about what exists requires a different study from a question about what would happen under an action. The distinction affects what counts as a comparison, how a population is defined, and what uncertainty means. An explanatory claim that light changes plant growth needs an intervention or another reason that compared groups are causally comparable; an inventory question may need probability sampling rather than manipulation. The research literature is useful only insofar as methods answer compatible questions. A graph, hypothesis or protocol is an explicit commitment about how observed numbers bear on a claim. The commitments are revisable, but revision after looking at outcomes must remain visible.

### Learning objectives

- Identify the **question and evidentiary target** for five different biological research decisions.

- Answer the design challenge: **Why is this question answerable with the observations proposed?**

- Identify an analysis failure addressed by **Which conclusion would require a stronger causal or sampling assumption?**

- Produce a research artifact that makes the chain from observation to claim auditable.

## A method is an argument, not just a procedure

The topics in this unit share a concern with question and evidentiary target. A sound method specifies what is being compared and explains why the measured response says something about the broader biological system. A result is interpretable only at the level supported by assignment, selection, calibration and analysis. The study may produce exact digital values while still leaving ecological or mechanistic uncertainty that cannot be converted into additional decimal places. In this unit, map decisions made before measurement separately from choices introduced while inspecting results. An acceptable alternative design may target a different estimand; that can be a strength when the alternatives are made visible.

### Practice before computation

Conceptual workshop: rewrite five vague questions as estimands with units, populations, interventions or exposures, comparators and timeframes. Draw a causal diagram for one question and identify a possible hidden cause. Distinguish an outcome that would weaken a hypothesis from a result that merely fails to show statistical significance. Practice keeping a dated research log so changes are traced rather than erased.

### The running scenario

Fictional investigation: A university teaching greenhouse wants to know whether a new lighting schedule changes fourteen-day seedling growth. Define the pot-level difference in average leaf-area change, include a randomized schedule, and nominate a competing temperature mechanism. The fictional data are only for method practice; no organism-based inference is claimed.

### Responsibility and scope

Ethical boundary: hypotheses and literature must not be shaped into certainty by selectively omitting contrary studies. Report which claims come from prior work and which are only assumptions of the teaching exercise.

## Five lessons

## Lesson 1.1 — Formulating a researchable biological question

**Inquiry to keep in view:** Why is this question answerable with the observations proposed? A lesson is successful when the learner can explain both the method and an observation that could undermine its proposed interpretation.

### Principle, construct and boundary

A useful biological question specifies organisms or systems, a contrast, a measurable response, and a time or spatial scale. A broad question such as whether habitat influences growth becomes answerable only after the substrate, growth criterion, developmental stage, and comparator are declared. The question also implies what population an answer would describe.

### Study construction and operational decisions

In a fictional greenhouse, compare relative leaf area growth in seedlings under two light schedules. Define the experimental unit as a pot receiving an assigned lighting program, not every leaf photographed. Measure standardized digital leaf area at baseline and day fourteen and register a primary difference in change.

Convert that proposal into a miniature preregistered plan. Specify the sampling frame, independently informative unit, comparator, measurement schedule, planned primary endpoint and handling of observations that cannot be recorded. Identify which decisions must occur before anyone sees the response data. Where the proposed setting uses groups or clusters, identify the level at which a common cause or intervention can reach all observations. Where outcomes are longitudinal, state whether a difference between subjects or a change within subjects answers the question. Do not rely on the final number of data rows to settle the question of replication.

### Fictional example and worked calculation

**Method setting.** For independent pot-level mean changes, the synthetic difference is 18 minus 14; this describes magnitude, not certainty about an intervention.

**Invented inputs:** mean_t = 18, mean_c = 14.  **Arithmetic expression:** `mean_t - mean_c`.  **Computed result:** **4 square centimetres**.

### Diagnostic failure modes and design alternatives

Light and temperature can covary across shelves; treating twenty leaves per pot as twenty independent replicates would disguise pseudoreplication. Choose several independently assigned pots per schedule and rotate their positions when rotation does not violate the treatment.

Use a structured critique rather than a general warning that bias may occur. First identify the exact step where the failure could enter: recruitment, allocation, collection, extraction, labelling, exclusion, modeling or interpretation. Next determine the direction in which a particular failure might move the estimate; an unknown direction is not the same as zero effect. Finally state which independent observation could distinguish the failure mechanism from the biological explanation. This process supports targeted controls and realistic uncertainty statements instead of presenting procedural completeness as proof of rigor.

**Alternative route.** A descriptive question about the mean leaf area in a greenhouse needs a representative sample; a causal question about the effect of lighting needs a deliberate intervention or carefully defended identification strategy.

### Interpretation, transparency and a reasoned conclusion

A valid claim will identify the quantity estimated, its uncertainty, the circumstances sampled, and the rival explanations not ruled out.

**Transfer problem.** Transfer the design to seed germination, where the unit might instead be a tray and the endpoint time to emergence rather than final size.

### Self-assessment (answers are provided for independent study)

1. **What does the arithmetic result establish?** It establishes `mean_t - mean_c` for the explicitly invented numbers, giving 4 square centimetres; it does not, on its own, validate the underlying biological construct.

3. **How would you identify a stronger inference?** Propose one additional control, independent repeat, rival prediction or sensitivity test that separates the principal explanation from a plausible alternative.

## Lesson 1.2 — Finding and appraising scientific literature

**Inquiry to keep in view:** Why is this question answerable with the observations proposed? A lesson is successful when the learner can explain both the method and an observation that could undermine its proposed interpretation.

### Principle, construct and boundary

A literature review is an auditable search and appraisal process, not a list of articles remembered by the investigator. Database choice, search terms, year restrictions, study design eligibility, and reasons for exclusion should follow the question. Citation counts and journal prestige are weak substitutes for directly reading sampling and analysis methods.

### Study construction and operational decisions

For a fictional study of pollinator visitation, construct concept groups for landscape fragmentation, flower visitation, and observational sampling. Search at least two relevant scholarly indexes, record dates and exact query strings, and screen titles and abstracts using a prespecified scope.

Convert that proposal into a miniature preregistered plan. Specify the sampling frame, independently informative unit, comparator, measurement schedule, planned primary endpoint and handling of observations that cannot be recorded. Identify which decisions must occur before anyone sees the response data. Where the proposed setting uses groups or clusters, identify the level at which a common cause or intervention can reach all observations. Where outcomes are longitudinal, state whether a difference between subjects or a change within subjects answers the question. Do not rely on the final number of data rows to settle the question of replication.

### Fictional example and worked calculation

**Method setting.** A fictional review screened 160 records and included 24; eligibility yield is not itself a measure of evidence quality.

**Invented inputs:** included = 24, screened = 160.  **Arithmetic expression:** `included / screened * 100`.  **Computed result:** **15 percent**.

### Diagnostic failure modes and design alternatives

Positive studies may be easier to locate, indexing vocabularies differ, and identical datasets may appear in several reports. A review must distinguish biological comparability from keyword similarity and detect overlapping samples.

Use a structured critique rather than a general warning that bias may occur. First identify the exact step where the failure could enter: recruitment, allocation, collection, extraction, labelling, exclusion, modeling or interpretation. Next determine the direction in which a particular failure might move the estimate; an unknown direction is not the same as zero effect. Finally state which independent observation could distinguish the failure mechanism from the biological explanation. This process supports targeted controls and realistic uncertainty statements instead of presenting procedural completeness as proof of rigor.

**Alternative route.** A scoping map describes how methods have been used; a systematic review asks a narrower question and requires more stringent reproducible search and synthesis procedures.

### Interpretation, transparency and a reasoned conclusion

The defensible output is an evidence table with sample frame, methods, effect definition, uncertainty, quality limits, and a transparent rationale for inclusion.

**Transfer problem.** Apply the same review protocol to host microbiome surveys while noting that sequencing platform changes complicate comparisons.

### Self-assessment (answers are provided for independent study)

1. **What does the arithmetic result establish?** It establishes `included / screened * 100` for the explicitly invented numbers, giving 15 percent; it does not, on its own, validate the underlying biological construct.

3. **How would you identify a stronger inference?** Propose one additional control, independent repeat, rival prediction or sensitivity test that separates the principal explanation from a plausible alternative.

## Lesson 1.3 — Hypotheses, predictions and alternative explanations

**Inquiry to keep in view:** Why is this question answerable with the observations proposed? A lesson is successful when the learner can explain both the method and an observation that could undermine its proposed interpretation.

### Principle, construct and boundary

A hypothesis proposes an explanation; a prediction states what should be observed under specified assumptions if that explanation holds. Several explanations often predict the same outcome, so effective tests seek observations that discriminate among mechanisms. Distinguish preregistered primary questions from exploratory patterns identified after looking at data.

### Study construction and operational decisions

In invented pond samples, hypothesize that nutrient addition increases algae through resource limitation and predict an increase in chlorophyll signal compared with matched controls. Also predict how the effect changes under shaded conditions, because light limitation offers a mechanistic rival.

Convert that proposal into a miniature preregistered plan. Specify the sampling frame, independently informative unit, comparator, measurement schedule, planned primary endpoint and handling of observations that cannot be recorded. Identify which decisions must occur before anyone sees the response data. Where the proposed setting uses groups or clusters, identify the level at which a common cause or intervention can reach all observations. Where outcomes are longitudinal, state whether a difference between subjects or a change within subjects answers the question. Do not rely on the final number of data rows to settle the question of replication.

### Fictional example and worked calculation

**Method setting.** A positive planned treatment-control difference fits one prediction but cannot identify a unique biochemical mechanism.

**Invented inputs:** treated = 26, control = 20.  **Arithmetic expression:** `treated - control`.  **Computed result:** **6 chlorophyll units**.

### Diagnostic failure modes and design alternatives

Chlorophyll fluorescence may change with physiological state without a proportional change in cell number. A single significant contrast does not select a unique mechanism; competing predictions and independent measurement matter.

Use a structured critique rather than a general warning that bias may occur. First identify the exact step where the failure could enter: recruitment, allocation, collection, extraction, labelling, exclusion, modeling or interpretation. Next determine the direction in which a particular failure might move the estimate; an unknown direction is not the same as zero effect. Finally state which independent observation could distinguish the failure mechanism from the biological explanation. This process supports targeted controls and realistic uncertainty statements instead of presenting procedural completeness as proof of rigor.

**Alternative route.** Compare a falsification-focused design using deliberately contrasting conditions with an estimation-focused design targeting the plausible magnitude of change across a realistic range.

### Interpretation, transparency and a reasoned conclusion

Interpret an outcome by specifying what the competing explanations expected before observation and how well each prediction fit, not by presenting an unexpected result as inevitable.

**Transfer problem.** Translate this logic to antibiotic resistance where growth, survival, and tolerance require different endpoints.

### Self-assessment (answers are provided for independent study)

1. **What does the arithmetic result establish?** It establishes `treated - control` for the explicitly invented numbers, giving 6 chlorophyll units; it does not, on its own, validate the underlying biological construct.

3. **How would you identify a stronger inference?** Propose one additional control, independent repeat, rival prediction or sensitivity test that separates the principal explanation from a plausible alternative.

## Lesson 1.4 — Causal diagrams and assumptions

**Inquiry to keep in view:** Why is this question answerable with the observations proposed? A lesson is successful when the learner can explain both the method and an observation that could undermine its proposed interpretation.

### Principle, construct and boundary

Directed acyclic graphs encode proposed relationships among variables and can reveal confounding, selection, and conditioning mistakes. A diagram is a statement of assumptions rather than a machine that proves causation. The timing and meaning of each arrow should be explicit.

### Study construction and operational decisions

Model a fictional association between stream temperature and invertebrate abundance. Upstream land cover affects both temperature and sediment, and sediment affects abundance; map those pathways before choosing covariates.

Convert that proposal into a miniature preregistered plan. Specify the sampling frame, independently informative unit, comparator, measurement schedule, planned primary endpoint and handling of observations that cannot be recorded. Identify which decisions must occur before anyone sees the response data. Where the proposed setting uses groups or clusters, identify the level at which a common cause or intervention can reach all observations. Where outcomes are longitudinal, state whether a difference between subjects or a change within subjects answers the question. Do not rely on the final number of data rows to settle the question of replication.

### Fictional example and worked calculation

**Method setting.** This numerical gap illustrates how an assumed adjusted model differs from a crude association; it does not establish which model is causally correct.

**Invented inputs:** crude = 7, adjusted = 3.  **Arithmetic expression:** `crude - adjusted`.  **Computed result:** **4 count units**.

### Diagnostic failure modes and design alternatives

Adjusting for a mediator can remove part of the effect being studied, while conditioning on a collider can create a spurious association. A statistical package will still return precise coefficients for a mistaken adjustment set.

Use a structured critique rather than a general warning that bias may occur. First identify the exact step where the failure could enter: recruitment, allocation, collection, extraction, labelling, exclusion, modeling or interpretation. Next determine the direction in which a particular failure might move the estimate; an unknown direction is not the same as zero effect. Finally state which independent observation could distinguish the failure mechanism from the biological explanation. This process supports targeted controls and realistic uncertainty statements instead of presenting procedural completeness as proof of rigor.

**Alternative route.** A controlled manipulation of temperature targets a different question from an observational contrast across catchments; neither design automatically transports to unstudied habitats.

### Interpretation, transparency and a reasoned conclusion

Record the proposed graph, identify unmeasured drivers, and present sensitivity analyses showing which conclusions depend on particular pathways.

**Transfer problem.** Extend the graph to disease ecology where sampling intensity responds to both perceived risk and observed cases.

### Self-assessment (answers are provided for independent study)

1. **What does the arithmetic result establish?** It establishes `crude - adjusted` for the explicitly invented numbers, giving 4 count units; it does not, on its own, validate the underlying biological construct.

3. **How would you identify a stronger inference?** Propose one additional control, independent repeat, rival prediction or sensitivity test that separates the principal explanation from a plausible alternative.

## Lesson 1.5 — Protocols, preregistration and research integrity

**Inquiry to keep in view:** Why is this question answerable with the observations proposed? A lesson is successful when the learner can explain both the method and an observation that could undermine its proposed interpretation.

### Principle, construct and boundary

A protocol records the research objective, inclusion criteria, primary outcome, analysis choices, quality controls, decision rules, and revision history before results can influence them. Preregistration does not eliminate exploratory research; it makes the distinction between planned and newly discovered analyses visible.

### Study construction and operational decisions

For a fictional enzyme activity comparison, specify reagent-lot records, blank correction, plate randomization, excluded wells, and one primary effect before collecting measurements. Preserve dated amendments when an instrument is repaired or a biologically justified exclusion is added.

Convert that proposal into a miniature preregistered plan. Specify the sampling frame, independently informative unit, comparator, measurement schedule, planned primary endpoint and handling of observations that cannot be recorded. Identify which decisions must occur before anyone sees the response data. Where the proposed setting uses groups or clusters, identify the level at which a common cause or intervention can reach all observations. Where outcomes are longitudinal, state whether a difference between subjects or a change within subjects answers the question. Do not rely on the final number of data rows to settle the question of replication.

### Fictional example and worked calculation

**Method setting.** Record three deviations among sixty scheduled measurements; the timing and causes matter more than a percentage alone.

**Invented inputs:** deviations = 3, attempts = 60.  **Arithmetic expression:** `deviations / attempts * 100`.  **Computed result:** **5 percent**.

### Diagnostic failure modes and design alternatives

Selective outcome reporting, undisclosed repeated testing, changed endpoints, image manipulation, and data fabrication threaten reliability in different ways. The remedy is an auditable record and independent verification, not a promise of personal objectivity.

Use a structured critique rather than a general warning that bias may occur. First identify the exact step where the failure could enter: recruitment, allocation, collection, extraction, labelling, exclusion, modeling or interpretation. Next determine the direction in which a particular failure might move the estimate; an unknown direction is not the same as zero effect. Finally state which independent observation could distinguish the failure mechanism from the biological explanation. This process supports targeted controls and realistic uncertainty statements instead of presenting procedural completeness as proof of rigor.

**Alternative route.** A registered confirmatory assay can coexist with clearly labeled pilot experiments and discovery analyses as long as reported conclusions correspond to their evidence strength.

### Interpretation, transparency and a reasoned conclusion

A credible report separates design deviations from analytic discretion, links raw records to figures, and makes unsuccessful attempts visible when they bear on interpretation.

**Transfer problem.** Transfer this reasoning to ecological field protocols where weather can force deviations and revisions must be timestamped.

### Self-assessment (answers are provided for independent study)

1. **What does the arithmetic result establish?** It establishes `deviations / attempts * 100` for the explicitly invented numbers, giving 5 percent; it does not, on its own, validate the underlying biological construct.

3. **How would you identify a stronger inference?** Propose one additional control, independent repeat, rival prediction or sensitivity test that separates the principal explanation from a plausible alternative.

## Unit 01 research studio — Synthetic integrated investigation

**Case premise.** Fictional investigation: A university teaching greenhouse wants to know whether a new lighting schedule changes fourteen-day seedling growth. Define the pot-level difference in average leaf-area change, include a randomized schedule, and nominate a competing temperature mechanism. The fictional data are only for method practice; no organism-based inference is claimed.

### Stage A: write an analysis plan

Start with the exact main question, not a convenient available test. Write a population description, a sample eligibility rule, a biological unit, a comparator and the response scale. In the design table, separate outcome measurement from the biological construct it represents. Where an intervention exists, name the assignment mechanism and identify which participants, plots, specimens or batches share an exposure. Where the design is observational, supply a causal diagram or a carefully reasoned list of confounders and explain why each might influence both the exposure and endpoint.

The study should have at least one explicit falsification route. List an outcome or pattern that would make the leading explanation less plausible even if the average direction initially looked favorable. Also state why the same pattern might emerge from altered detection, handling, sample selection or instrument drift. This exercise prevents researchers from describing a merely possible mechanism as the only explanation for an observed contrast.

### Stage B: inspect fictional records

The accompanying unit CSV holds six invented observations with a baseline score, follow-up score, treatment label and batch identifier. No living organism was sampled to construct this file. Treat units as independent only for this classroom computation and record the assumption in your notes. Calculate changes for every row, group averages, difference in average change, the number of units contributing to each result and any imbalance across batches. Do not interpret the invented numbers as evidence of actual biological treatment response.

Before you summarize the numbers, intentionally remove one follow-up observation and write two analysis plans: a complete-case approach and a conservative sensitivity scenario. Why might missingness be related to the unobserved outcome? How would that possibility change the generality of your conclusion? For a second check, alter the assumed calibration of one instrument reading and repeat the contrast. The exercise reveals how numerical conclusions can depend on design and measurement assumptions rather than sample size alone.

### Stage C: defend the result

Write a two-hundred-word abstract for the synthetic example. It must use **question and evidentiary target** to connect method to claim. Distinguish the calculation from the proposed mechanism, show the relevant uncertainty in prose, and name at least one alternative explanation. Attach an audit table with input file, analysis version, field definitions, excluded entries and a sentence describing how someone could independently rerun the exercise.

A reader who doubts the conclusion should not have to infer which values were changed after the fact. Retain your first analysis plan and place revisions beside it with dates and reasons. A corrected error is scientifically different from an undisclosed change that selects a pleasing outcome. If the stronger claim requires another experiment or validated technique, propose it explicitly instead of enlarging the present study’s conclusions.

### Stage D: ethical and practical review

Ethical boundary: hypotheses and literature must not be shaped into certainty by selectively omitting contrary studies. Report which claims come from prior work and which are only assumptions of the teaching exercise.

The studio is a dry-lab reasoning exercise. Any translation into work with participants, animals, sensitive ecological sites or biological materials demands separate supervision, local approvals and qualified protocol design. Identifying a feasible future observation is not authorization to conduct it. Preserve accurate fictional-data labels wherever the scenario is presented.

### Submission checklist

- Research question, population, independent unit, contrast and endpoint defined without hidden assumptions.

- Synthetic source CSV preserved without manual changes; any cleaning rules scripted and documented.

- Estimate calculated with units and appropriately cautious interpretation; alternatives and exclusions explained.

- A proposed independent check targets a specific failure mode rather than merely repeating the same measurement.

- Rights, safety, oversight, sensitive data and communication boundaries considered before translating the exercise.
