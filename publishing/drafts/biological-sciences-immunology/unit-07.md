# Unit 07 — Infection, vaccines and population immunity

> **OpenSTEM Biological Sciences, Book 13: Immunology.** Undergraduate editorial draft; expert review pending. All numerical inputs and investigation records are hypothetical instructional examples. Models are not pathogen predictions, diagnostic tests, patient advice or clinical decision tools.

## Learning objectives and context

Immune responses interact with pathogen replication, transmission and evolution. Mechanistic protection for an individual and epidemiological outcomes for a population are different analytical levels. Vaccine design uses immunology but must be evaluated by empirical effectiveness and safety evidence.

The five topics in this unit approach a common problem from different levels of explanation. They concern **pathogen immune evasion; memory and boosting; antigenic variation; within-host versus population models; vaccine efficacy versus effectiveness**. By the end, explain the core mechanism for each topic, identify at least two plausible alternative explanations for a measured signal, reproduce the arithmetic in five cases, and describe what data would actually falsify a claim. Separate the event being *detected* from the downstream consequence inferred from that event. In immunology, an increase in a reporter, a cytokine, a cell percentage or antibody binding often looks persuasive but rarely establishes host protection by itself.

A useful immune-system model declares its spatial scale, the biological unit and the time horizon. A molecule can bind within seconds, a cell may alter transcription over hours, a clone expands across days, and tissue structure or population immunity changes across longer periods. Measured concentrations cannot be substituted for cell numbers, and cell numbers cannot replace measurements of functional killing, pathogen burden or tissue function. Check whether a figure uses proportions of all live cells, proportions within a selected gate, copies per milliliter, fluorescence units or an actual physical rate. The denominator is part of the scientific claim.

## Evidence and responsible interpretation

An immune response depends on anatomical compartment and previous exposure. Blood samples provide valuable, accessible information but can miss tissue-resident populations and localized mediator gradients. Bulk averages hide rare cell populations and interactions. Healthy versus diseased comparisons can confound cause and consequence, while an intervention that changes two pathways at once may not isolate either one. For quantitative work, preserve raw counts, clarify calibration, distinguish independent donors from repeated technical wells, and describe measurement error separately from biological variation.

All activities in this unit are computational, synthetic-data or abstract analysis exercises. Do not culture pathogens, perform human or animal exposure experiments, or attempt clinical assays on personal samples from these pages. Appropriate institutional biosafety and ethics review are prerequisites for any real laboratory research. These pages never prescribe immunization, diagnosis or treatment.


## Topic 7.1 — Pathogen strategies and immune evasion

### Biological mechanism

Microbes may change exposed antigens, hide within cells, interfere with host signaling or occupy anatomical locations that immune effectors access poorly. Different strategies limit recognition, recruitment or clearance. Host responses in turn impose selection pressures that can change pathogen populations.

### Why a plausible explanation can fail

A pathogen that avoids one antibody epitope may remain vulnerable to T-cell recognition or antibodies targeting other features. Escape can carry fitness costs, and a variant that grows faster in culture may not transmit better in a population.

To challenge this account, use the related concept **memory and boosting** to propose a different route to the same observation. Which intermediate biological step would make the two hypotheses diverge?

### Designing an informative measurement

Use a noninfectious computer model of two abstract variants with different recognition coefficients and replication parameters. Explore when each predominates, but avoid interpreting parameter choices as predictions of real pathogen evolution.

Define a control that separates assay background from biological mechanism. Sample before, during and after the expected response, and identify a second measurement that would corroborate the proposed pathway.

### Boundaries and counterexamples

Fitness depends on environment and intervention history. A single mutation cannot generally be labeled immune escape from sequence appearance alone; functional evidence is necessary.

Construct a counterexample where the measured signal changes without the proposed mechanism changing. Prioritize one alternative and choose an observation that would refute it.

### Quantitative worked case 7.1

**Problem.** A toy recognition coefficient falls from 0.8 to 0.3 after abstract antigen change. Find fractional reduction.

**Hypothetical inputs:** before = 0.8, after = 0.3. **Relation:** `(before-after)/before*100`. **Answer:** **62.5 %**. Recompute independently and identify the physical or assay denominator, including the time interval where applicable.

**Interpretation:** Reduced proxy recognition does not establish increased transmission. **Scope limit:** An escape variant could carry a growth penalty. These invented inputs offer no independent biological replicates or measured variance. Change an input by 20 percent, repeat the calculation and identify one mechanism that could break the simplified assumption.

### Applying and challenging the concept

Prepare a two-column evidence ledger on **pathogen immune evasion**: direct observations versus explanatory assumptions. Draw a causal network for **pathogen strategies and immune evasion** with one feedback edge. State how a null result could reflect either a false hypothesis or inadequate sampling.


## Topic 7.2 — Vaccines, adjuvants and immune priming

### Biological mechanism

Vaccines seek to provide protective immune learning without the risk profile of uncontrolled natural disease. Platforms deliver antigens or genetic instructions in different ways, while adjuvants in some formulations shape local sensing and antigen presentation. Dose, schedule, immune history and route affect the final response.

### Why a plausible explanation can fail

Safety and protective effectiveness are established through regulated empirical evidence, not from a diagram of memory-cell formation. High binding-antibody levels may be useful markers but are not always validated correlates of protection. Protection can involve many effector layers.

To challenge this account, use the related concept **antigenic variation** to propose a different route to the same observation. Which intermediate biological step would make the two hypotheses diverge?

### Designing an informative measurement

Given hypothetical immunogenicity data, compare median response and dispersion between two fictional formulations. State that immune marker response is not clinical efficacy and that a simulated chart cannot support vaccine policy or therapeutic claims.

Define a control that separates assay background from biological mechanism. Sample before, during and after the expected response, and identify a second measurement that would corroborate the proposed pathway.

### Boundaries and counterexamples

No vaccine is perfectly effective against every outcome or variant. Actual vaccine choices and schedules depend on current public-health recommendations and individual clinical factors.

Construct a counterexample where the measured signal changes without the proposed mechanism changing. Prioritize one alternative and choose an observation that would refute it.

### Quantitative worked case 7.2

**Problem.** Hypothetical antibody marker rises from 40 to 100 units in a controlled simulation. Find fold increase.

**Hypothetical inputs:** before = 40, after = 100. **Relation:** `after/before`. **Answer:** **2.5 fold**. Recompute independently and identify the physical or assay denominator, including the time interval where applicable.

**Interpretation:** Immunogenicity is not interchangeable with observed protection. **Scope limit:** Invented markers are not correlates of protection. These invented inputs offer no independent biological replicates or measured variance. Change an input by 20 percent, repeat the calculation and identify one mechanism that could break the simplified assumption.

### Applying and challenging the concept

Prepare a two-column evidence ledger on **memory and boosting**: direct observations versus explanatory assumptions. Draw a causal network for **vaccines, adjuvants and immune priming** with one feedback edge. State how a null result could reflect either a false hypothesis or inadequate sampling.


## Topic 7.3 — Primary, secondary and tissue-resident memory

### Biological mechanism

After first exposure, naive-cell expansion and differentiation create effector and memory populations. Some memory cells recirculate, while others reside in barrier tissues and can act rapidly at entry sites. Recall responses can therefore differ between blood and tissue, and between the same antigen delivered through different routes.

### Why a plausible explanation can fail

A high systemic antibody titer may not reflect local mucosal protection. Tissue-resident T cells can contribute despite being invisible in routine blood sampling. A secondary response is not invariably stronger in every measured compartment.

To challenge this account, use the related concept **within-host versus population models** to propose a different route to the same observation. Which intermediate biological step would make the two hypotheses diverge?

### Designing an informative measurement

Model two compartments with simple retention and movement rates, then compare blood and tissue proxies after a hypothetical antigen recall. Ask which samples would reveal rapid local activity, and why serial tissue measurements are difficult in practice.

Define a control that separates assay background from biological mechanism. Sample before, during and after the expected response, and identify a second measurement that would corroborate the proposed pathway.

### Boundaries and counterexamples

A two-compartment toy model does not measure actual protection; antigen specificity, pathogen replication and tissue injury require independent observations.

Construct a counterexample where the measured signal changes without the proposed mechanism changing. Prioritize one alternative and choose an observation that would refute it.

### Quantitative worked case 7.3

**Problem.** A simplified two-compartment response has 75 cells in tissue and 25 in blood. Compute tissue fraction.

**Hypothetical inputs:** tissue = 75, blood = 25. **Relation:** `tissue/(tissue+blood)*100`. **Answer:** **75 %**. Recompute independently and identify the physical or assay denominator, including the time interval where applicable.

**Interpretation:** Blood can underrepresent a tissue-enriched population. **Scope limit:** Numbers are fictional and total body compartments are omitted. These invented inputs offer no independent biological replicates or measured variance. Change an input by 20 percent, repeat the calculation and identify one mechanism that could break the simplified assumption.

### Applying and challenging the concept

Prepare a two-column evidence ledger on **antigenic variation**: direct observations versus explanatory assumptions. Draw a causal network for **primary, secondary and tissue-resident memory** with one feedback edge. State how a null result could reflect either a false hypothesis or inadequate sampling.


## Topic 7.4 — Transmission, herd effects and heterogeneity

### Biological mechanism

Transmission depends on contacts, infectiousness, susceptibility and duration of infectiousness. Immune protection can alter susceptibility or shedding, and distribution of immunity across contact networks matters. A crude homogeneous mixing model introduces useful concepts but omits age, setting, geography and temporal structure.

### Why a plausible explanation can fail

The simple threshold formula using a basic reproduction number assumes a particular idealized model and nearly uniform mixing. It cannot by itself establish a real-world vaccination target or policy. Variants, waning, coverage clustering and changed behavior modify population dynamics.

To challenge this account, use the related concept **vaccine efficacy versus effectiveness** to propose a different route to the same observation. Which intermediate biological step would make the two hypotheses diverge?

### Designing an informative measurement

Calculate a teaching threshold from a hypothetical R value, explicitly defining assumptions and interpreting it as a model quantity rather than a policy recommendation. Explore how uneven contact rates can produce outbreaks despite a favorable population average.

Define a control that separates assay background from biological mechanism. Sample before, during and after the expected response, and identify a second measurement that would corroborate the proposed pathway.

### Boundaries and counterexamples

Epidemiological parameters should be estimated with uncertainty from relevant data. Never quote toy thresholds as an official disease-control requirement.

Construct a counterexample where the measured signal changes without the proposed mechanism changing. Prioritize one alternative and choose an observation that would refute it.

### Quantitative worked case 7.4

**Problem.** For a theoretical homogeneous-mixing model with R0 = 2.5, find 1-1/R0 as a percentage.

**Hypothetical inputs:** r0 = 2.5. **Relation:** `(1-1/r0)*100`. **Answer:** **60 %**. Recompute independently and identify the physical or assay denominator, including the time interval where applicable.

**Interpretation:** This is a toy theoretical threshold under strong assumptions, not a vaccine policy target. **Scope limit:** Heterogeneity, pathogen evolution and immune dynamics invalidate direct policy extrapolation. These invented inputs offer no independent biological replicates or measured variance. Change an input by 20 percent, repeat the calculation and identify one mechanism that could break the simplified assumption.

### Applying and challenging the concept

Prepare a two-column evidence ledger on **within-host versus population models**: direct observations versus explanatory assumptions. Draw a causal network for **transmission, herd effects and heterogeneity** with one feedback edge. State how a null result could reflect either a false hypothesis or inadequate sampling.


## Topic 7.5 — Evaluating vaccine studies and correlates

### Biological mechanism

Randomized trials, surveillance and mechanistic studies answer different questions about vaccines. Efficacy compares outcomes under trial conditions, whereas effectiveness reflects performance in actual use and may vary with exposure history. Absolute risks, denominators, follow-up and outcome definitions are essential.

### Why a plausible explanation can fail

Relative risk reduction can sound impressive when baseline risk is small, and apparent vaccine associations can be confounded in observational datasets. Unmeasured prior immunity, exposure behavior and differential testing often matter. Safety outcomes require appropriate ascertainment and benefit-risk analysis.

To challenge this account, use the related concept **pathogen immune evasion** to propose a different route to the same observation. Which intermediate biological step would make the two hypotheses diverge?

### Designing an informative measurement

Analyze a fully synthetic two-by-two event table with distinct group denominators. Compute attack risks, risk ratio, absolute risk difference and relative reduction, and explain why one toy table cannot quantify vaccine safety or determine a national recommendation.

Define a control that separates assay background from biological mechanism. Sample before, during and after the expected response, and identify a second measurement that would corroborate the proposed pathway.

### Boundaries and counterexamples

The confidence of a conclusion depends on study design, measurement and uncertainty, not the number of decimal places in a single percentage.

Construct a counterexample where the measured signal changes without the proposed mechanism changing. Prioritize one alternative and choose an observation that would refute it.

### Quantitative worked case 7.5

**Problem.** In a synthetic trial-like table, group A has 12 outcomes among 600 people and B has 30 among 600. Compute relative risk reduction 1-riskA/riskB.

**Hypothetical inputs:** a = 12, na = 600, b = 30, nb = 600. **Relation:** `(1-(a/na)/(b/nb))*100`. **Answer:** **60 %**. Recompute independently and identify the physical or assay denominator, including the time interval where applicable.

**Interpretation:** The absolute risk difference is also relevant: 3 percentage points. **Scope limit:** Invented counts are not clinical trial or safety evidence. These invented inputs offer no independent biological replicates or measured variance. Change an input by 20 percent, repeat the calculation and identify one mechanism that could break the simplified assumption.

### Applying and challenging the concept

Prepare a two-column evidence ledger on **vaccine efficacy versus effectiveness**: direct observations versus explanatory assumptions. Draw a causal network for **evaluating vaccine studies and correlates** with one feedback edge. State how a null result could reflect either a false hypothesis or inadequate sampling.


## Integrated computational investigation — Immunological marker versus vaccine effectiveness

### Question and rival explanations

A simulated cohort shows high post-vaccination marker titers, yet outcome reduction is heterogeneous. Which level of inference has been crossed?

**Mechanistic hypothesis A:** Marker captures one protective mechanism incompletely.

**Mechanistic hypothesis B:** Exposure intensity and pre-existing immunity differ across subgroups.

The challenge is not to select the explanation that seems familiar. First articulate the different predictions each account makes under a condition that would actually distinguish them. A mechanism might predict an early localized signal, whereas an alternative predicts a later population effect; both can reproduce the same final bulk number. Construct a causal diagram with the stimulus, intermediate state, assay output and at least one unmeasured covariate. Mark which relations are observed and which require assumptions. The invented numbers below are practice material only: no patients, animals, pathogen samples or laboratory measurements generated them.

### Research design

Separate immunogenicity measurement from participant follow-up. For fictional surveillance records, compare absolute risks and ascertainment under predeclared strata, keeping randomization and adjustment concepts distinct.

**Principal confound:** People with different exposure and testing patterns can have different observed event rates even with identical biological susceptibility..

A study needs biological units that match the hypothesis. If all measurements come from one culture vessel, 50 images represent subsampling of that vessel, not 50 independent cultures. If hundreds of cells come from one donor, those cells cannot support donor-level generalization without a design that accounts for clustering. Predefine the primary comparison, effect direction, main covariates and quality exclusions. Calibrate instruments or report uncalibrated arbitrary units explicitly, and store the untouched data before plotting or normalization. Use safe computational methods for these classroom tasks; any real specimen acquisition requires proper authorization, ethics and biosafety oversight.

### Constructed series (not research data)

| Stage / sample index | Series A (invented) | Series B (invented) |
|---:|---:|---:|
| 0 | 4 | 3 |
| 1 | 8 | 7 |
| 2 | 14 | 10 |
| 3 | 18 | 11 |
| 4 | 19 | 12 |

Series A changes by **15** display units across the five stages; series B changes by **9**. Its endpoint ratio is **0.6316** if the chosen scales are comparable; if the assays do not share a scale, that arithmetic is only a display ratio and has no biological interpretation. Compute each sequence's initial-to-final proportional change separately. Plot the two curves, label axis units or 'arbitrary teaching index', and add no error bars: the dataset supplies no independent replicate variation. Do not invent significance levels, biological confidence intervals or citations to make synthetic observations appear empirical.

### Interpretation and identification

Marker increases do not establish clinically relevant effectiveness without credible outcomes and a defensible counterfactual comparison. The most important next step is to specify a discriminating measurement. A time course is better than a single endpoint when mechanisms have distinct delays, but unobserved confounding remains possible. A targeted perturbation can improve causal identification, provided it does not independently change the outcome through a second mechanism. Some data would make both hypotheses less plausible; identify such a result explicitly. The final answer should distinguish the direction of the constructed numbers, the mechanism proposed to explain them, and the missing evidence needed for a real biological conclusion.

### Structured analysis assignment

1. Write both hypotheses as falsifiable predictions for one named assay and an explicit time window.
2. State whether the sample unit is a donor, animal, organ, culture vessel or cell; explain why technical repetitions cannot silently increase biological sample size.
3. Quantify the endpoint and one interval rate, explaining any limitations due to missing time units.
4. Identify two alternative causes of the same observed trajectory, including the principal confound listed above.
5. Propose a safe, noninfectious follow-up or computational analysis and choose a criterion that would change your preferred explanation.
6. Produce a short reproducibility note giving data schema, graph labels, analysis pseudocode and a statement that all values are fictional.


## Systems synthesis and examination preparation

An immune network changes across compartments and timescales. This unit links **Pathogen strategies and immune evasion**, **Vaccines, adjuvants and immune priming**, **Primary, secondary and tissue-resident memory**, **Transmission, herd effects and heterogeneity** and **Evaluating vaccine studies and correlates**. Try placing these concepts in a table with columns for recognition, cellular actors, immediate output, delayed outcome, negative regulation and an assay limitation. Some rows will not fit neatly: the same mediator may promote clearance and also exacerbate injury. Treat that apparent contradiction as a clue about concentrations, timing and tissue specificity rather than a reason to ignore the mechanism.

To test integration, imagine two specimens showing the same final reporter value despite different early trajectories. In one, a small number of strongly responding cells drive the signal; in the other, a large number of weakly responding cells produce an equal bulk total. A single bulk assay cannot resolve those explanations. Which of this unit's five mechanisms could generate the two situations, and what independent measurement would discriminate them? For every proposed measurement, identify whether it estimates a concentration, frequency, absolute count, location, phenotype or function. Then articulate the assumption that makes the measurement relevant.

Transfer the explanation from a controlled cell system into an intact tissue. Tissue oxygen, access to antigen, migration routes and regulatory signals could all change the qualitative outcome even if receptor-level biochemistry remains the same. Do not silently treat a monotonic curve as an empirical law valid across species, tissues and developmental stages. If you use the interactive model, name one omitted interaction and describe how including it might shift the curve, introduce a delay, or reverse the predicted comparison. Sensitivity to an assumed parameter is useful for learning but cannot establish that the chosen parameter value matches biology.

### End-of-unit synthesis questions

- Use **pathogen strategies and immune evasion** and **evaluating vaccine studies and correlates** in one causal argument and identify where negative feedback could intervene.
- Present a competing hypothesis for a result initially attributed to **primary, secondary and tissue-resident memory**. What measurement, with units, would favor one explanation?
- Explain how an apparent change in immune-cell frequency might arise with no change in absolute abundance of that population.
- Recompute one quantitative case with different assumptions and report which assumption contributes most to uncertainty.
- Choose a claim that would be dangerous to generalize into patient advice and explain why the available educational model cannot justify it.

**Editorial reminder:** The described scenarios are concept exercises, not real laboratory results. All clinical statements require authoritative evidence and, where applicable, qualified professional interpretation.
