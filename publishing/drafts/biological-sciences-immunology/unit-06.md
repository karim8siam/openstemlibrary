# Unit 06 — Tolerance, hypersensitivity and immune dysfunction

> **OpenSTEM Biological Sciences, Book 13: Immunology.** Undergraduate editorial draft; expert review pending. All numerical inputs and investigation records are hypothetical instructional examples. Models are not pathogen predictions, diagnostic tests, patient advice or clinical decision tools.

## Learning objectives and context

Immune regulation explains why recognition can remain silent, why harmless exposures can provoke pathology and why compromised defenses create characteristic vulnerabilities. Clinical syndromes are multifactorial; this is a conceptual undergraduate course, not a diagnostic manual.

The five topics in this unit approach a common problem from different levels of explanation. They concern **central versus peripheral tolerance; hypersensitivity mechanisms; autoimmune etiology; immunodeficiency; context-sensitive interpretation**. By the end, explain the core mechanism for each topic, identify at least two plausible alternative explanations for a measured signal, reproduce the arithmetic in five cases, and describe what data would actually falsify a claim. Separate the event being *detected* from the downstream consequence inferred from that event. In immunology, an increase in a reporter, a cytokine, a cell percentage or antibody binding often looks persuasive but rarely establishes host protection by itself.

A useful immune-system model declares its spatial scale, the biological unit and the time horizon. A molecule can bind within seconds, a cell may alter transcription over hours, a clone expands across days, and tissue structure or population immunity changes across longer periods. Measured concentrations cannot be substituted for cell numbers, and cell numbers cannot replace measurements of functional killing, pathogen burden or tissue function. Check whether a figure uses proportions of all live cells, proportions within a selected gate, copies per milliliter, fluorescence units or an actual physical rate. The denominator is part of the scientific claim.

## Evidence and responsible interpretation

An immune response depends on anatomical compartment and previous exposure. Blood samples provide valuable, accessible information but can miss tissue-resident populations and localized mediator gradients. Bulk averages hide rare cell populations and interactions. Healthy versus diseased comparisons can confound cause and consequence, while an intervention that changes two pathways at once may not isolate either one. For quantitative work, preserve raw counts, clarify calibration, distinguish independent donors from repeated technical wells, and describe measurement error separately from biological variation.

All activities in this unit are computational, synthetic-data or abstract analysis exercises. Do not culture pathogens, perform human or animal exposure experiments, or attempt clinical assays on personal samples from these pages. Appropriate institutional biosafety and ethics review are prerequisites for any real laboratory research. These pages never prescribe immunization, diagnosis or treatment.


## Topic 6.1 — Central and peripheral tolerance

### Biological mechanism

Negative selection during lymphocyte development reduces some self-reactive populations; peripheral controls further constrain cells that escaped deletion. Mechanisms include anergy, regulatory cells, activation-dependent death and restrictions on costimulation or antigen location. These controls permit ongoing repair and coexistence with many self structures.

### Why a plausible explanation can fail

Tolerance is antigen- and context-dependent, not a claim that every self-recognizing clone is eliminated. Environmental inflammation, tissue injury and altered antigen presentation can change how a previously restrained clone behaves. Self-reactivity in a laboratory assay is not equivalent to destructive autoimmune disease.

To challenge this account, use the related concept **hypersensitivity mechanisms** to propose a different route to the same observation. Which intermediate biological step would make the two hypotheses diverge?

### Designing an informative measurement

Construct a four-condition table crossing receptor binding and costimulation, then compare predicted activation for otherwise identical clones. Explain what an independent regulatory-population measurement would add. Account for survival and migration rather than measuring only proliferation.

Define a control that separates assay background from biological mechanism. Sample before, during and after the expected response, and identify a second measurement that would corroborate the proposed pathway.

### Boundaries and counterexamples

No one tolerance assay proves whole-organism immune safety. Tissue-restricted antigens, microbiota, sex, age and inherited variation complicate extrapolation.

Construct a counterexample where the measured signal changes without the proposed mechanism changing. Prioritize one alternative and choose an observation that would refute it.

### Quantitative worked case 6.1

**Problem.** A toy assay detects 18 responding cells out of 300 with a costimulation signal and 3 out of 300 without. Find difference in percentage points.

**Hypothetical inputs:** with_signal = 18, without_signal = 3, n = 300. **Relation:** `(with_signal/n-without_signal/n)*100`. **Answer:** **5 percentage points**. Recompute independently and identify the physical or assay denominator, including the time interval where applicable.

**Interpretation:** Peripheral signals alter the response in this idealized comparison. **Scope limit:** The model cannot predict clinical autoimmunity. These invented inputs offer no independent biological replicates or measured variance. Change an input by 20 percent, repeat the calculation and identify one mechanism that could break the simplified assumption.

### Applying and challenging the concept

Prepare a two-column evidence ledger on **central versus peripheral tolerance**: direct observations versus explanatory assumptions. Draw a causal network for **central and peripheral tolerance** with one feedback edge. State how a null result could reflect either a false hypothesis or inadequate sampling.


## Topic 6.2 — Immediate hypersensitivity and mast cells

### Biological mechanism

In some allergic responses, antigen crosslinks IgE already bound to Fc receptors on mast cells or basophils, promoting release of stored mediators and synthesis of other inflammatory compounds. Vascular, smooth-muscle and epithelial responses influence symptoms. Sensitization and subsequent triggering are distinct biological events.

### Why a plausible explanation can fail

Mast-cell mediator release is context-dependent and not every reaction resembling allergy is IgE mediated. Dose, route, cofactors and tissue distribution matter. A detectable IgE binding signal does not necessarily predict the severity of a future reaction.

To challenge this account, use the related concept **autoimmune etiology** to propose a different route to the same observation. Which intermediate biological step would make the two hypotheses diverge?

### Designing an informative measurement

Analyze an invented dose-response curve for mediator release with baseline and saturation. Ask how a receptor-blocking control would help attribute the mechanism. Use no real allergen exposure or provocative testing; classroom work should remain computational.

Define a control that separates assay background from biological mechanism. Sample before, during and after the expected response, and identify a second measurement that would corroborate the proposed pathway.

### Boundaries and counterexamples

Severe allergic reactions are medical emergencies and cannot be assessed by a classroom model. Do not infer clinical risk, treatment or challenge dosing from hypothetical curves.

Construct a counterexample where the measured signal changes without the proposed mechanism changing. Prioritize one alternative and choose an observation that would refute it.

### Quantitative worked case 6.2

**Problem.** A harmless hypothetical mediator assay changes from 5 to 25 arbitrary units after stimulation. Find fold change.

**Hypothetical inputs:** stimulated = 25, baseline = 5. **Relation:** `stimulated/baseline`. **Answer:** **5 fold**. Recompute independently and identify the physical or assay denominator, including the time interval where applicable.

**Interpretation:** A ratio does not indicate whether the response is safe or pathogenic. **Scope limit:** No actual allergen or challenge protocol is provided. These invented inputs offer no independent biological replicates or measured variance. Change an input by 20 percent, repeat the calculation and identify one mechanism that could break the simplified assumption.

### Applying and challenging the concept

Prepare a two-column evidence ledger on **hypersensitivity mechanisms**: direct observations versus explanatory assumptions. Draw a causal network for **immediate hypersensitivity and mast cells** with one feedback edge. State how a null result could reflect either a false hypothesis or inadequate sampling.


## Topic 6.3 — Immune-complex and T-cell-mediated hypersensitivity

### Biological mechanism

Immune complexes can deposit in tissues and engage complement or Fc-dependent inflammatory mechanisms, while certain delayed hypersensitivity reactions recruit antigen-specific T cells and activated innate effectors. The classical hypersensitivity scheme is a useful organizing framework but real diseases often involve overlapping processes.

### Why a plausible explanation can fail

Similar tissue inflammation can result from distinct immune pathways. Timing alone cannot fully identify a mechanism, and circulating complex concentrations do not directly map to deposition in particular organs. Histology, antigen localization and complementary assays are needed for mechanistic attribution.

To challenge this account, use the related concept **immunodeficiency** to propose a different route to the same observation. Which intermediate biological step would make the two hypotheses diverge?

### Designing an informative measurement

Compare a hypothetical early mediator profile with a later cellular infiltrate profile. Decide what assays could distinguish complex-associated complement activation from local T-cell recruitment, recognizing that both may be present.

Define a control that separates assay background from biological mechanism. Sample before, during and after the expected response, and identify a second measurement that would corroborate the proposed pathway.

### Boundaries and counterexamples

Labels such as type III and type IV simplify complex pathophysiology. They should not be converted into self-diagnosis from a symptom or a single blood-test value.

Construct a counterexample where the measured signal changes without the proposed mechanism changing. Prioritize one alternative and choose an observation that would refute it.

### Quantitative worked case 6.3

**Problem.** Invented complement-fragment signal is 15 at early time and 39 at later time. Find absolute increase.

**Hypothetical inputs:** early = 15, late = 39. **Relation:** `late-early`. **Answer:** **24 signal units**. Recompute independently and identify the physical or assay denominator, including the time interval where applicable.

**Interpretation:** Temporal measurements help identify sequence, not cause. **Scope limit:** Signal units may have nonlinear instrument behavior. These invented inputs offer no independent biological replicates or measured variance. Change an input by 20 percent, repeat the calculation and identify one mechanism that could break the simplified assumption.

### Applying and challenging the concept

Prepare a two-column evidence ledger on **autoimmune etiology**: direct observations versus explanatory assumptions. Draw a causal network for **immune-complex and t-cell-mediated hypersensitivity** with one feedback edge. State how a null result could reflect either a false hypothesis or inadequate sampling.


## Topic 6.4 — Autoimmunity and loss of regulation

### Biological mechanism

Autoimmune disease emerges when immune responses contribute to injury against self tissues, often through combinations of genetic susceptibility, stochastic receptor repertoires, environmental exposures and inflammatory context. Antibodies and T cells may be involved in different proportions depending on syndrome. Organ-specific and systemic disease require distinct explanatory models.

### Why a plausible explanation can fail

Detection of an autoantibody may support a clinical investigation but does not always establish active disease. A susceptible genotype changes probability, not destiny. Destructive pathology may also reflect downstream tissue responses rather than direct receptor binding alone.

To challenge this account, use the related concept **context-sensitive interpretation** to propose a different route to the same observation. Which intermediate biological step would make the two hypotheses diverge?

### Designing an informative measurement

In an entirely synthetic dataset, model disease probability in two genetic-background categories crossed with a second factor. Compare relative and absolute risk and explain the assumptions of observational associations. Explicitly avoid presenting invented values as epidemiology.

Define a control that separates assay background from biological mechanism. Sample before, during and after the expected response, and identify a second measurement that would corroborate the proposed pathway.

### Boundaries and counterexamples

A correlation between exposure and immune marker is not proof that the exposure triggered a specific disease. Diagnosis requires qualified clinical evaluation and validated methods.

Construct a counterexample where the measured signal changes without the proposed mechanism changing. Prioritize one alternative and choose an observation that would refute it.

### Quantitative worked case 6.4

**Problem.** Synthetic relative risks are 0.08 versus 0.04 across two exposure categories. Find risk ratio.

**Hypothetical inputs:** risk_a = 0.08, risk_b = 0.04. **Relation:** `risk_a/risk_b`. **Answer:** **2 risk ratio**. Recompute independently and identify the physical or assay denominator, including the time interval where applicable.

**Interpretation:** A relative association is not evidence of causality. **Scope limit:** The numbers are not disease incidence data. These invented inputs offer no independent biological replicates or measured variance. Change an input by 20 percent, repeat the calculation and identify one mechanism that could break the simplified assumption.

### Applying and challenging the concept

Prepare a two-column evidence ledger on **immunodeficiency**: direct observations versus explanatory assumptions. Draw a causal network for **autoimmunity and loss of regulation** with one feedback edge. State how a null result could reflect either a false hypothesis or inadequate sampling.


## Topic 6.5 — Primary and acquired immunodeficiency

### Biological mechanism

Reduced immune function can arise through inherited variants affecting cell development, signaling, complement or antimicrobial effectors, or through acquired causes such as medications, infection or nutritional impairment. Patterns of susceptibility vary because immune pathways control different threats. Functional assays and clinical history often matter more than one cell count.

### Why a plausible explanation can fail

Low circulating lymphocyte number is not equivalent to a uniform absence of immunity, and a normal count does not rule out signaling dysfunction. Suppression of inflammation may improve symptoms while also increasing infection risk; context determines the clinical balance.

To challenge this account, use the related concept **central versus peripheral tolerance** to propose a different route to the same observation. Which intermediate biological step would make the two hypotheses diverge?

### Designing an informative measurement

Use a fictitious decision tree comparing quantitative counts and functional response proxies under several mechanistic hypotheses. Identify what extra test could discriminate a cellular absence from impaired activation without proposing actual diagnostic thresholds.

Define a control that separates assay background from biological mechanism. Sample before, during and after the expected response, and identify a second measurement that would corroborate the proposed pathway.

### Boundaries and counterexamples

This text does not provide patient-specific testing, clinical classification or treatment. Immunodeficiency evaluation and vaccination decisions require specialist guidance.

Construct a counterexample where the measured signal changes without the proposed mechanism changing. Prioritize one alternative and choose an observation that would refute it.

### Quantitative worked case 6.5

**Problem.** In a fictional assay 80 out of 400 cells show an expected functional response. Calculate percentage.

**Hypothetical inputs:** functional = 80, total = 400. **Relation:** `functional/total*100`. **Answer:** **20 %**. Recompute independently and identify the physical or assay denominator, including the time interval where applicable.

**Interpretation:** This quantifies a declared assay endpoint, not immune competence. **Scope limit:** No diagnostic threshold follows from invented data. These invented inputs offer no independent biological replicates or measured variance. Change an input by 20 percent, repeat the calculation and identify one mechanism that could break the simplified assumption.

### Applying and challenging the concept

Prepare a two-column evidence ledger on **context-sensitive interpretation**: direct observations versus explanatory assumptions. Draw a causal network for **primary and acquired immunodeficiency** with one feedback edge. State how a null result could reflect either a false hypothesis or inadequate sampling.


## Integrated computational investigation — Tolerance marker or disease mechanism?

### Question and rival explanations

A self-reactive assay signal is measurable in a hypothetical cohort but most individuals have no tissue injury marker. What does the signal establish?

**Mechanistic hypothesis A:** Peripheral regulatory circuits prevent injury.

**Mechanistic hypothesis B:** The assay detects binding that does not access tissue or recruit effectors.

The challenge is not to select the explanation that seems familiar. First articulate the different predictions each account makes under a condition that would actually distinguish them. A mechanism might predict an early localized signal, whereas an alternative predicts a later population effect; both can reproduce the same final bulk number. Construct a causal diagram with the stimulus, intermediate state, assay output and at least one unmeasured covariate. Mark which relations are observed and which require assumptions. The invented numbers below are practice material only: no patients, animals, pathogen samples or laboratory measurements generated them.

### Research design

Construct a cross-sectional synthetic matrix with binding intensity, regulatory-cell marker and tissue-injury proxy. Use donor-level analysis and predeclare outcome definitions.

**Principal confound:** Marker measurement can be affected by age, batch and selection of subjects, making naive associations misleading..

A study needs biological units that match the hypothesis. If all measurements come from one culture vessel, 50 images represent subsampling of that vessel, not 50 independent cultures. If hundreds of cells come from one donor, those cells cannot support donor-level generalization without a design that accounts for clustering. Predefine the primary comparison, effect direction, main covariates and quality exclusions. Calibrate instruments or report uncalibrated arbitrary units explicitly, and store the untouched data before plotting or normalization. Use safe computational methods for these classroom tasks; any real specimen acquisition requires proper authorization, ethics and biosafety oversight.

### Constructed series (not research data)

| Stage / sample index | Series A (invented) | Series B (invented) |
|---:|---:|---:|
| 0 | 1 | 1 |
| 1 | 3 | 1.2 |
| 2 | 5 | 1.3 |
| 3 | 7 | 1.4 |
| 4 | 9 | 1.5 |

Series A changes by **8** display units across the five stages; series B changes by **0.5**. Its endpoint ratio is **0.1667** if the chosen scales are comparable; if the assays do not share a scale, that arithmetic is only a display ratio and has no biological interpretation. Compute each sequence's initial-to-final proportional change separately. Plot the two curves, label axis units or 'arbitrary teaching index', and add no error bars: the dataset supplies no independent replicate variation. Do not invent significance levels, biological confidence intervals or citations to make synthetic observations appear empirical.

### Interpretation and identification

A rising binding proxy with nearly stable injury proxy is consistent with multiple explanatory mechanisms, not evidence that either hypothesis is proven. The most important next step is to specify a discriminating measurement. A time course is better than a single endpoint when mechanisms have distinct delays, but unobserved confounding remains possible. A targeted perturbation can improve causal identification, provided it does not independently change the outcome through a second mechanism. Some data would make both hypotheses less plausible; identify such a result explicitly. The final answer should distinguish the direction of the constructed numbers, the mechanism proposed to explain them, and the missing evidence needed for a real biological conclusion.

### Structured analysis assignment

1. Write both hypotheses as falsifiable predictions for one named assay and an explicit time window.
2. State whether the sample unit is a donor, animal, organ, culture vessel or cell; explain why technical repetitions cannot silently increase biological sample size.
3. Quantify the endpoint and one interval rate, explaining any limitations due to missing time units.
4. Identify two alternative causes of the same observed trajectory, including the principal confound listed above.
5. Propose a safe, noninfectious follow-up or computational analysis and choose a criterion that would change your preferred explanation.
6. Produce a short reproducibility note giving data schema, graph labels, analysis pseudocode and a statement that all values are fictional.


## Systems synthesis and examination preparation

An immune network changes across compartments and timescales. This unit links **Central and peripheral tolerance**, **Immediate hypersensitivity and mast cells**, **Immune-complex and T-cell-mediated hypersensitivity**, **Autoimmunity and loss of regulation** and **Primary and acquired immunodeficiency**. Try placing these concepts in a table with columns for recognition, cellular actors, immediate output, delayed outcome, negative regulation and an assay limitation. Some rows will not fit neatly: the same mediator may promote clearance and also exacerbate injury. Treat that apparent contradiction as a clue about concentrations, timing and tissue specificity rather than a reason to ignore the mechanism.

To test integration, imagine two specimens showing the same final reporter value despite different early trajectories. In one, a small number of strongly responding cells drive the signal; in the other, a large number of weakly responding cells produce an equal bulk total. A single bulk assay cannot resolve those explanations. Which of this unit's five mechanisms could generate the two situations, and what independent measurement would discriminate them? For every proposed measurement, identify whether it estimates a concentration, frequency, absolute count, location, phenotype or function. Then articulate the assumption that makes the measurement relevant.

Transfer the explanation from a controlled cell system into an intact tissue. Tissue oxygen, access to antigen, migration routes and regulatory signals could all change the qualitative outcome even if receptor-level biochemistry remains the same. Do not silently treat a monotonic curve as an empirical law valid across species, tissues and developmental stages. If you use the interactive model, name one omitted interaction and describe how including it might shift the curve, introduce a delay, or reverse the predicted comparison. Sensitivity to an assumed parameter is useful for learning but cannot establish that the chosen parameter value matches biology.

### End-of-unit synthesis questions

- Use **central and peripheral tolerance** and **primary and acquired immunodeficiency** in one causal argument and identify where negative feedback could intervene.
- Present a competing hypothesis for a result initially attributed to **immune-complex and t-cell-mediated hypersensitivity**. What measurement, with units, would favor one explanation?
- Explain how an apparent change in immune-cell frequency might arise with no change in absolute abundance of that population.
- Recompute one quantitative case with different assumptions and report which assumption contributes most to uncertainty.
- Choose a claim that would be dangerous to generalize into patient advice and explain why the available educational model cannot justify it.

**Editorial reminder:** The described scenarios are concept exercises, not real laboratory results. All clinical statements require authoritative evidence and, where applicable, qualified professional interpretation.
