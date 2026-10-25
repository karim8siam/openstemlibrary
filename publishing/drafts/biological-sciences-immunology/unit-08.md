# Unit 08 — Transplantation, tumors and experimental immunology

> **OpenSTEM Biological Sciences, Book 13: Immunology.** Undergraduate editorial draft; expert review pending. All numerical inputs and investigation records are hypothetical instructional examples. Models are not pathogen predictions, diagnostic tests, patient advice or clinical decision tools.

## Learning objectives and context

Clinical and experimental applications reveal the strengths and limits of immune specificity. Recognition of graft or tumor-associated features intersects with suppression, tissue access, immune escape and unintended injury. Ethical interpretation and rigorous experimental design are central.

The five topics in this unit approach a common problem from different levels of explanation. They concern **allorecognition; tumor surveillance; therapeutic trade-offs; assay validity; reproducible data analysis**. By the end, explain the core mechanism for each topic, identify at least two plausible alternative explanations for a measured signal, reproduce the arithmetic in five cases, and describe what data would actually falsify a claim. Separate the event being *detected* from the downstream consequence inferred from that event. In immunology, an increase in a reporter, a cytokine, a cell percentage or antibody binding often looks persuasive but rarely establishes host protection by itself.

A useful immune-system model declares its spatial scale, the biological unit and the time horizon. A molecule can bind within seconds, a cell may alter transcription over hours, a clone expands across days, and tissue structure or population immunity changes across longer periods. Measured concentrations cannot be substituted for cell numbers, and cell numbers cannot replace measurements of functional killing, pathogen burden or tissue function. Check whether a figure uses proportions of all live cells, proportions within a selected gate, copies per milliliter, fluorescence units or an actual physical rate. The denominator is part of the scientific claim.

## Evidence and responsible interpretation

An immune response depends on anatomical compartment and previous exposure. Blood samples provide valuable, accessible information but can miss tissue-resident populations and localized mediator gradients. Bulk averages hide rare cell populations and interactions. Healthy versus diseased comparisons can confound cause and consequence, while an intervention that changes two pathways at once may not isolate either one. For quantitative work, preserve raw counts, clarify calibration, distinguish independent donors from repeated technical wells, and describe measurement error separately from biological variation.

All activities in this unit are computational, synthetic-data or abstract analysis exercises. Do not culture pathogens, perform human or animal exposure experiments, or attempt clinical assays on personal samples from these pages. Appropriate institutional biosafety and ethics review are prerequisites for any real laboratory research. These pages never prescribe immunization, diagnosis or treatment.


## Topic 8.1 — Allorecognition and transplant responses

### Biological mechanism

Transplanted cells may display MHC molecules or other features recognized by host immunity. T cells can respond through direct or indirect routes of alloantigen presentation, while antibodies and innate effectors can contribute to graft injury. Regulation and treatment can reduce rejection risks at the cost of altered protective responses.

### Why a plausible explanation can fail

An in vitro T-cell activation result does not predict long-term graft function by itself. Tissue-specific injury, immunosuppressive exposure and recipient history shape outcomes. Donor-recipient matching reduces some risks but does not erase all immune differences.

To challenge this account, use the related concept **tumor surveillance** to propose a different route to the same observation. Which intermediate biological step would make the two hypotheses diverge?

### Designing an informative measurement

Use a fictional two-signal model to compare a T-cell activation proxy for matched and mismatched presentation assumptions. Identify why a tissue-function measurement and longitudinal monitoring are still needed to interpret graft outcomes.

Define a control that separates assay background from biological mechanism. Sample before, during and after the expected response, and identify a second measurement that would corroborate the proposed pathway.

### Boundaries and counterexamples

Transplantation involves clinical decisions about immunosuppression and infection risk. No parameter in this educational example should guide organ matching or medication choices.

Construct a counterexample where the measured signal changes without the proposed mechanism changing. Prioritize one alternative and choose an observation that would refute it.

### Quantitative worked case 8.1

**Problem.** A toy alloactivation reporter rises from 5 to 17 arbitrary units. Compute increment.

**Hypothetical inputs:** matched = 5, mismatched = 17. **Relation:** `mismatched-matched`. **Answer:** **12 signal units**. Recompute independently and identify the physical or assay denominator, including the time interval where applicable.

**Interpretation:** Reactivity readouts do not predict graft outcomes by themselves. **Scope limit:** No medical matching or treatment criteria can be inferred. These invented inputs offer no independent biological replicates or measured variance. Change an input by 20 percent, repeat the calculation and identify one mechanism that could break the simplified assumption.

### Applying and challenging the concept

Prepare a two-column evidence ledger on **allorecognition**: direct observations versus explanatory assumptions. Draw a causal network for **allorecognition and transplant responses** with one feedback edge. State how a null result could reflect either a false hypothesis or inadequate sampling.


## Topic 8.2 — Tumor immunosurveillance and antigen escape

### Biological mechanism

Immune cells can recognize tumor-associated antigens or altered stress signals, and tumors can evolve mechanisms that restrict antigen presentation, immune entry or effector activity. The tumor microenvironment includes stromal cells, metabolites and inhibitory signals that alter local responses. Tumor diversity changes the set of targets over time.

### Why a plausible explanation can fail

Presence of tumor-infiltrating lymphocytes does not guarantee effective killing; some populations are suppressed or spatially excluded. A tumor can lose a target antigen while continuing to grow. Observed immune activation may also reflect tissue injury or inflammation unrelated to control.

To challenge this account, use the related concept **therapeutic trade-offs** to propose a different route to the same observation. Which intermediate biological step would make the two hypotheses diverge?

### Designing an informative measurement

Analyze an invented spatial grid representing immune-cell positions and target-cell regions. Compare total cell count with average distance to target and define a contact probability proxy. Explain what microscopy or functional evidence would be needed for a causal conclusion.

Define a control that separates assay background from biological mechanism. Sample before, during and after the expected response, and identify a second measurement that would corroborate the proposed pathway.

### Boundaries and counterexamples

Antigen expression and histological immune density alone cannot predict response to a cancer therapy. The models here are conceptual and are not clinical prognostic tools.

Construct a counterexample where the measured signal changes without the proposed mechanism changing. Prioritize one alternative and choose an observation that would refute it.

### Quantitative worked case 8.2

**Problem.** A mock tumor grid has 42 contacts within 210 possible local immune-target pairs. Compute contact fraction.

**Hypothetical inputs:** contacts = 42, pairs = 210. **Relation:** `contacts/pairs*100`. **Answer:** **20 %**. Recompute independently and identify the physical or assay denominator, including the time interval where applicable.

**Interpretation:** Spatial opportunity is not the same as successful killing. **Scope limit:** Toy spatial geometry excludes dynamic migration. These invented inputs offer no independent biological replicates or measured variance. Change an input by 20 percent, repeat the calculation and identify one mechanism that could break the simplified assumption.

### Applying and challenging the concept

Prepare a two-column evidence ledger on **tumor surveillance**: direct observations versus explanatory assumptions. Draw a causal network for **tumor immunosurveillance and antigen escape** with one feedback edge. State how a null result could reflect either a false hypothesis or inadequate sampling.


## Topic 8.3 — Cancer immunotherapy mechanisms and adverse effects

### Biological mechanism

Several cancer-immunotherapy approaches aim to strengthen recognition or effector functions, or change suppressive signaling. Checkpoint-related therapies and engineered cellular treatments illustrate how targeting can generate useful responses and substantial immune-mediated adverse effects. Benefit depends on disease setting, target selection and patient factors.

### Why a plausible explanation can fail

Increasing activation does not always improve the therapeutic index. A treatment can amplify self-directed inflammation, and tumor antigen heterogeneity can permit escape. A model that only plots tumor-cell loss misses systemic toxicity, quality of life and delayed complications.

To challenge this account, use the related concept **assay validity** to propose a different route to the same observation. Which intermediate biological step would make the two hypotheses diverge?

### Designing an informative measurement

Create a nonclinical multiobjective toy table with benefit proxy and adverse-event proxy for abstract treatment intensities. Identify Pareto trade-offs rather than choosing the numerically largest immune activation. The toy values cannot predict clinical outcomes.

Define a control that separates assay background from biological mechanism. Sample before, during and after the expected response, and identify a second measurement that would corroborate the proposed pathway.

### Boundaries and counterexamples

Treatment eligibility, dose and safety monitoring are specialist clinical matters. This chapter intentionally provides no dosing, procedure or individual treatment recommendation.

Construct a counterexample where the measured signal changes without the proposed mechanism changing. Prioritize one alternative and choose an observation that would refute it.

### Quantitative worked case 8.3

**Problem.** One fictional treatment-intensity point scores benefit 65 and toxicity proxy 35. Find difference on their arbitrary common 0–100 display scale.

**Hypothetical inputs:** benefit = 65, toxicity = 35. **Relation:** `benefit-toxicity`. **Answer:** **30 display points**. Recompute independently and identify the physical or assay denominator, including the time interval where applicable.

**Interpretation:** A numerical difference can help compare toy points, but is not a clinical utility function. **Scope limit:** Real benefit and harm often cannot be placed on a common scale without normative choices. These invented inputs offer no independent biological replicates or measured variance. Change an input by 20 percent, repeat the calculation and identify one mechanism that could break the simplified assumption.

### Applying and challenging the concept

Prepare a two-column evidence ledger on **therapeutic trade-offs**: direct observations versus explanatory assumptions. Draw a causal network for **cancer immunotherapy mechanisms and adverse effects** with one feedback edge. State how a null result could reflect either a false hypothesis or inadequate sampling.


## Topic 8.4 — Flow cytometry, ELISA and functional assays

### Biological mechanism

Flow cytometry measures per-particle optical signals and can characterize defined cell populations after careful gating; ELISA-like assays estimate molecular binding or concentration using calibrated detection curves. Functional assays measure outcomes such as proliferation, signaling or target-cell death. Each method introduces different measurement errors and biological interpretations.

### Why a plausible explanation can fail

A flow marker fraction is conditioned on its parent gate. Changing which events are excluded can produce a large apparent biological difference. An ELISA signal can saturate or be affected by matrix background; without a standard curve it need not map linearly to concentration.

To challenge this account, use the related concept **reproducible data analysis** to propose a different route to the same observation. Which intermediate biological step would make the two hypotheses diverge?

### Designing an informative measurement

Practice on invented fluorescence intensities, a gating table and a calibrated serial dilution. Distinguish true biological replicates from technical wells, use blanks and standards, and preserve raw instrument units before normalization. Record exclusion criteria prior to seeing the final plots.

Define a control that separates assay background from biological mechanism. Sample before, during and after the expected response, and identify a second measurement that would corroborate the proposed pathway.

### Boundaries and counterexamples

A positive binding assay does not establish immune protection, and an attractive gating figure does not establish that the selected population is pure or functionally homogeneous.

Construct a counterexample where the measured signal changes without the proposed mechanism changing. Prioritize one alternative and choose an observation that would refute it.

### Quantitative worked case 8.4

**Problem.** A toy flow gate retains 6200 singlets from 8000 acquired events. Calculate singlet proportion.

**Hypothetical inputs:** singlets = 6200, all_events = 8000. **Relation:** `singlets/all_events*100`. **Answer:** **77.5 %**. Recompute independently and identify the physical or assay denominator, including the time interval where applicable.

**Interpretation:** Gating defines a conditional denominator. **Scope limit:** The cell type composition of excluded events also matters. These invented inputs offer no independent biological replicates or measured variance. Change an input by 20 percent, repeat the calculation and identify one mechanism that could break the simplified assumption.

### Applying and challenging the concept

Prepare a two-column evidence ledger on **assay validity**: direct observations versus explanatory assumptions. Draw a causal network for **flow cytometry, elisa and functional assays** with one feedback edge. State how a null result could reflect either a false hypothesis or inadequate sampling.


## Topic 8.5 — Single-cell data, causal inference and reproducibility

### Biological mechanism

Single-cell sequencing, multiplex imaging and repertoire profiling can reveal heterogeneity concealed by bulk measurements. However, batch effects, low molecule capture, doublets, cell-state shifts and compositional differences complicate conclusions. Mechanistic inference needs perturbation or convergent evidence, not clustering alone.

### Why a plausible explanation can fail

Cells from one donor are not independent biological replicates of a donor-level treatment. A statistically significant difference among thousands of cells can disappear when donor-level variation is modeled. Unsupervised clusters depend on analysis choices and need biological validation.

To challenge this account, use the related concept **allorecognition** to propose a different route to the same observation. Which intermediate biological step would make the two hypotheses diverge?

### Designing an informative measurement

Use a fully synthetic expression matrix from four donors to compare naive cell-level and donor-aggregated group means. Preserve analysis code, thresholds and seed values and report missingness. Then design a feasible nonhazardous validation such as a reporter assay or imaging readout.

Define a control that separates assay background from biological mechanism. Sample before, during and after the expected response, and identify a second measurement that would corroborate the proposed pathway.

### Boundaries and counterexamples

No clustering algorithm discovers immutable cell types by itself. Publication-quality claims demand provenance, uncertainty assessment, ethical handling of human data and independent scrutiny.

Construct a counterexample where the measured signal changes without the proposed mechanism changing. Prioritize one alternative and choose an observation that would refute it.

### Quantitative worked case 8.5

**Problem.** A synthetic single-cell dataset has 4000 cells from four donors. Calculate mean sampled cells per donor assuming equal representation.

**Hypothetical inputs:** cells = 4000, donors = 4. **Relation:** `cells/donors`. **Answer:** **1000 cells/donor**. Recompute independently and identify the physical or assay denominator, including the time interval where applicable.

**Interpretation:** Four donors, not 4000 cells, set the independent donor-level sample size. **Scope limit:** Equal representation is an explicit invented simplification. These invented inputs offer no independent biological replicates or measured variance. Change an input by 20 percent, repeat the calculation and identify one mechanism that could break the simplified assumption.

### Applying and challenging the concept

Prepare a two-column evidence ledger on **reproducible data analysis**: direct observations versus explanatory assumptions. Draw a causal network for **single-cell data, causal inference and reproducibility** with one feedback edge. State how a null result could reflect either a false hypothesis or inadequate sampling.


## Integrated computational investigation — Immune infiltration versus function in a tissue

### Question and rival explanations

A simulated tissue contains many immune cells but target burden remains high; do cell density and function answer the same question?

**Mechanistic hypothesis A:** Effector cells lack productive contact with targets.

**Mechanistic hypothesis B:** Contact occurs but inhibitory context reduces function.

The challenge is not to select the explanation that seems familiar. First articulate the different predictions each account makes under a condition that would actually distinguish them. A mechanism might predict an early localized signal, whereas an alternative predicts a later population effect; both can reproduce the same final bulk number. Construct a causal diagram with the stimulus, intermediate state, assay output and at least one unmeasured covariate. Mark which relations are observed and which require assumptions. The invented numbers below are practice material only: no patients, animals, pathogen samples or laboratory measurements generated them.

### Research design

Use a hypothetical spatial image grid and construct distance-to-target statistics, contact frequencies and separate functional activation indicators. Compare donors at donor-level rather than treating pixels as replicates.

**Principal confound:** A larger tissue region or different sampling depth can inflate cell density and apparent tumor size together..

A study needs biological units that match the hypothesis. If all measurements come from one culture vessel, 50 images represent subsampling of that vessel, not 50 independent cultures. If hundreds of cells come from one donor, those cells cannot support donor-level generalization without a design that accounts for clustering. Predefine the primary comparison, effect direction, main covariates and quality exclusions. Calibrate instruments or report uncalibrated arbitrary units explicitly, and store the untouched data before plotting or normalization. Use safe computational methods for these classroom tasks; any real specimen acquisition requires proper authorization, ethics and biosafety oversight.

### Constructed series (not research data)

| Stage / sample index | Series A (invented) | Series B (invented) |
|---:|---:|---:|
| 0 | 2 | 1 |
| 1 | 4 | 2 |
| 2 | 7 | 3.5 |
| 3 | 9 | 4.5 |
| 4 | 10 | 5 |

Series A changes by **8** display units across the five stages; series B changes by **4**. Its endpoint ratio is **0.5** if the chosen scales are comparable; if the assays do not share a scale, that arithmetic is only a display ratio and has no biological interpretation. Compute each sequence's initial-to-final proportional change separately. Plot the two curves, label axis units or 'arbitrary teaching index', and add no error bars: the dataset supplies no independent replicate variation. Do not invent significance levels, biological confidence intervals or citations to make synthetic observations appear empirical.

### Interpretation and identification

The higher count series may reflect cells that are unable to reach relevant targets; localized function is a separate observation. The most important next step is to specify a discriminating measurement. A time course is better than a single endpoint when mechanisms have distinct delays, but unobserved confounding remains possible. A targeted perturbation can improve causal identification, provided it does not independently change the outcome through a second mechanism. Some data would make both hypotheses less plausible; identify such a result explicitly. The final answer should distinguish the direction of the constructed numbers, the mechanism proposed to explain them, and the missing evidence needed for a real biological conclusion.

### Structured analysis assignment

1. Write both hypotheses as falsifiable predictions for one named assay and an explicit time window.
2. State whether the sample unit is a donor, animal, organ, culture vessel or cell; explain why technical repetitions cannot silently increase biological sample size.
3. Quantify the endpoint and one interval rate, explaining any limitations due to missing time units.
4. Identify two alternative causes of the same observed trajectory, including the principal confound listed above.
5. Propose a safe, noninfectious follow-up or computational analysis and choose a criterion that would change your preferred explanation.
6. Produce a short reproducibility note giving data schema, graph labels, analysis pseudocode and a statement that all values are fictional.


## Systems synthesis and examination preparation

An immune network changes across compartments and timescales. This unit links **Allorecognition and transplant responses**, **Tumor immunosurveillance and antigen escape**, **Cancer immunotherapy mechanisms and adverse effects**, **Flow cytometry, ELISA and functional assays** and **Single-cell data, causal inference and reproducibility**. Try placing these concepts in a table with columns for recognition, cellular actors, immediate output, delayed outcome, negative regulation and an assay limitation. Some rows will not fit neatly: the same mediator may promote clearance and also exacerbate injury. Treat that apparent contradiction as a clue about concentrations, timing and tissue specificity rather than a reason to ignore the mechanism.

To test integration, imagine two specimens showing the same final reporter value despite different early trajectories. In one, a small number of strongly responding cells drive the signal; in the other, a large number of weakly responding cells produce an equal bulk total. A single bulk assay cannot resolve those explanations. Which of this unit's five mechanisms could generate the two situations, and what independent measurement would discriminate them? For every proposed measurement, identify whether it estimates a concentration, frequency, absolute count, location, phenotype or function. Then articulate the assumption that makes the measurement relevant.

Transfer the explanation from a controlled cell system into an intact tissue. Tissue oxygen, access to antigen, migration routes and regulatory signals could all change the qualitative outcome even if receptor-level biochemistry remains the same. Do not silently treat a monotonic curve as an empirical law valid across species, tissues and developmental stages. If you use the interactive model, name one omitted interaction and describe how including it might shift the curve, introduce a delay, or reverse the predicted comparison. Sensitivity to an assumed parameter is useful for learning but cannot establish that the chosen parameter value matches biology.

### End-of-unit synthesis questions

- Use **allorecognition and transplant responses** and **single-cell data, causal inference and reproducibility** in one causal argument and identify where negative feedback could intervene.
- Present a competing hypothesis for a result initially attributed to **cancer immunotherapy mechanisms and adverse effects**. What measurement, with units, would favor one explanation?
- Explain how an apparent change in immune-cell frequency might arise with no change in absolute abundance of that population.
- Recompute one quantitative case with different assumptions and report which assumption contributes most to uncertainty.
- Choose a claim that would be dangerous to generalize into patient advice and explain why the available educational model cannot justify it.

**Editorial reminder:** The described scenarios are concept exercises, not real laboratory results. All clinical statements require authoritative evidence and, where applicable, qualified professional interpretation.
