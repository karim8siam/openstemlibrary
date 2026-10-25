# Unit 05 — B lymphocytes, antibodies and humoral memory

> **OpenSTEM Biological Sciences, Book 13: Immunology.** Undergraduate editorial draft; expert review pending. All numerical inputs and investigation records are hypothetical instructional examples. Models are not pathogen predictions, diagnostic tests, patient advice or clinical decision tools.

## Learning objectives and context

Humoral immunity couples molecular recognition to antibody-secreting cells, antigen transport and durable immune memory. The useful unit of explanation changes between an antibody molecule, a clone and the whole-body distribution of antibodies. Affinity and concentration should never be collapsed into one number.

The five topics in this unit approach a common problem from different levels of explanation. They concern **B-cell activation; germinal-center selection; antibody classes; effector functions; memory cell dynamics**. By the end, explain the core mechanism for each topic, identify at least two plausible alternative explanations for a measured signal, reproduce the arithmetic in five cases, and describe what data would actually falsify a claim. Separate the event being *detected* from the downstream consequence inferred from that event. In immunology, an increase in a reporter, a cytokine, a cell percentage or antibody binding often looks persuasive but rarely establishes host protection by itself.

A useful immune-system model declares its spatial scale, the biological unit and the time horizon. A molecule can bind within seconds, a cell may alter transcription over hours, a clone expands across days, and tissue structure or population immunity changes across longer periods. Measured concentrations cannot be substituted for cell numbers, and cell numbers cannot replace measurements of functional killing, pathogen burden or tissue function. Check whether a figure uses proportions of all live cells, proportions within a selected gate, copies per milliliter, fluorescence units or an actual physical rate. The denominator is part of the scientific claim.

## Evidence and responsible interpretation

An immune response depends on anatomical compartment and previous exposure. Blood samples provide valuable, accessible information but can miss tissue-resident populations and localized mediator gradients. Bulk averages hide rare cell populations and interactions. Healthy versus diseased comparisons can confound cause and consequence, while an intervention that changes two pathways at once may not isolate either one. For quantitative work, preserve raw counts, clarify calibration, distinguish independent donors from repeated technical wells, and describe measurement error separately from biological variation.

All activities in this unit are computational, synthetic-data or abstract analysis exercises. Do not culture pathogens, perform human or animal exposure experiments, or attempt clinical assays on personal samples from these pages. Appropriate institutional biosafety and ethics review are prerequisites for any real laboratory research. These pages never prescribe immunization, diagnosis or treatment.


## Topic 5.1 — B-cell receptor signaling and helper cooperation

### Biological mechanism

B cells recognize native molecular structures through membrane immunoglobulin and signal through associated proteins. Antigen internalization supports peptide–MHC-II display, allowing antigen-specific CD4 helper cells to provide signals important for many antibody responses. Some antigens produce substantial T-independent activity, but response quality and durability differ.

### Why a plausible explanation can fail

Crosslinking, antigen geometry, innate receptor signals and help can all change the threshold for B-cell activation. Recognition alone is not equivalent to secretion of protective antibody. Mature B cells encounter antigens in a physical microenvironment where complement deposition and follicular access matter.

To challenge this account, use the related concept **germinal-center selection** to propose a different route to the same observation. Which intermediate biological step would make the two hypotheses diverge?

### Designing an informative measurement

Use a toy response surface that varies receptor occupancy and help intensity. Compare how many cells enter division under a monotonic saturating assumption. Critique the omission of anergy, competing clones and antigen clearance rather than treating the curve as a universal dose rule.

Define a control that separates assay background from biological mechanism. Sample before, during and after the expected response, and identify a second measurement that would corroborate the proposed pathway.

### Boundaries and counterexamples

Helper dependence varies by antigen and organism. It is false to say that every antibody response absolutely requires direct T-cell help or that stronger binding automatically means stronger immunological memory.

Construct a counterexample where the measured signal changes without the proposed mechanism changing. Prioritize one alternative and choose an observation that would refute it.

### Quantitative worked case 5.1

**Problem.** In a mock activation sample 120 of 500 B cells entered division. Compute the dividing fraction.

**Hypothetical inputs:** dividing = 120, total = 500. **Relation:** `dividing/total*100`. **Answer:** **24 %**. Recompute independently and identify the physical or assay denominator, including the time interval where applicable.

**Interpretation:** Receptor binding and cell division are distinct events. **Scope limit:** No antibody function was measured. These invented inputs offer no independent biological replicates or measured variance. Change an input by 20 percent, repeat the calculation and identify one mechanism that could break the simplified assumption.

### Applying and challenging the concept

Prepare a two-column evidence ledger on **B-cell activation**: direct observations versus explanatory assumptions. Draw a causal network for **b-cell receptor signaling and helper cooperation** with one feedback edge. State how a null result could reflect either a false hypothesis or inadequate sampling.


## Topic 5.2 — Germinal centers and affinity maturation

### Biological mechanism

Germinal centers coordinate B-cell proliferation, somatic hypermutation and selection based on antigen capture and T-follicular helper interactions. Repeated cycles can shift the surviving pool toward antibodies with improved functional affinity, while other lineages produce plasma cells or memory cells. Competition shapes which variants persist.

### Why a plausible explanation can fail

Affinity maturation is selection among variants, not directed mutation toward a desired epitope. A rise in mean apparent affinity can occur because low-affinity clones disappear without every surviving lineage improving. Selection also depends on available antigen and competing specificities.

To challenge this account, use the related concept **antibody classes** to propose a different route to the same observation. Which intermediate biological step would make the two hypotheses diverge?

### Designing an informative measurement

Analyze a synthetic clone-frequency table before and after a selection round. Calculate weighted mean affinity proxy and distinguish changes in within-clone binding from changes in abundance. Sampling error could alter both estimates in a small sample.

Define a control that separates assay background from biological mechanism. Sample before, during and after the expected response, and identify a second measurement that would corroborate the proposed pathway.

### Boundaries and counterexamples

The toy fitness landscape omits T-cell help, anatomical cycling and stochastic mutation. No deterministic formula predicts an exact antibody sequence for a given infection.

Construct a counterexample where the measured signal changes without the proposed mechanism changing. Prioritize one alternative and choose an observation that would refute it.

### Quantitative worked case 5.2

**Problem.** Two toy antibody clones have binding proxies 3 and 9 and frequencies 0.4 and 0.6. Compute weighted mean proxy.

**Hypothetical inputs:** a = 3, b = 9, wa = 0.4, wb = 0.6. **Relation:** `a*wa+b*wb`. **Answer:** **6.6 arbitrary binding units**. Recompute independently and identify the physical or assay denominator, including the time interval where applicable.

**Interpretation:** Frequency weighting can shift the population average without changes in individual clone properties. **Scope limit:** These are invented binding proxies, not affinity constants. These invented inputs offer no independent biological replicates or measured variance. Change an input by 20 percent, repeat the calculation and identify one mechanism that could break the simplified assumption.

### Applying and challenging the concept

Prepare a two-column evidence ledger on **germinal-center selection**: direct observations versus explanatory assumptions. Draw a causal network for **germinal centers and affinity maturation** with one feedback edge. State how a null result could reflect either a false hypothesis or inadequate sampling.


## Topic 5.3 — Antibody isotypes, structure and distribution

### Biological mechanism

Antibodies comprise variable antigen-binding regions and constant regions that govern interaction with effector systems. IgM, IgG, IgA, IgE and IgD differ in common locations and functional associations, with substantial subclass and species variation. Class switching changes constant-region usage while generally preserving the selected antigen-binding rearrangement.

### Why a plausible explanation can fail

Blood concentration does not fully represent mucosal or tissue antibody distribution. IgA frequently operates at surfaces, IgG is prominent in many systemic settings, and IgE participates in type-2 defense and allergy. Antibody action depends on physical state, glycosylation, valency and available receptors.

To challenge this account, use the related concept **effector functions** to propose a different route to the same observation. Which intermediate biological step would make the two hypotheses diverge?

### Designing an informative measurement

Given a hypothetical serum and secretion table, compute an isotype fraction and compare the information provided by absolute concentration. Discuss how total protein recovery or dilution might create a false shift in apparent class distribution.

Define a control that separates assay background from biological mechanism. Sample before, during and after the expected response, and identify a second measurement that would corroborate the proposed pathway.

### Boundaries and counterexamples

An isotype is not a one-word synonym for a disease category. IgE can be relevant to protection in some settings, but its detection does not by itself diagnose allergy.

Construct a counterexample where the measured signal changes without the proposed mechanism changing. Prioritize one alternative and choose an observation that would refute it.

### Quantitative worked case 5.3

**Problem.** A hypothetical specimen contains 120 arbitrary IgA units and 380 IgG units. Find IgA fraction among these two quantities.

**Hypothetical inputs:** iga = 120, igg = 380. **Relation:** `iga/(iga+igg)*100`. **Answer:** **24 %**. Recompute independently and identify the physical or assay denominator, including the time interval where applicable.

**Interpretation:** Isotype proportions depend on where and how samples are collected. **Scope limit:** No absolute immunoglobulin concentration or health judgment follows. These invented inputs offer no independent biological replicates or measured variance. Change an input by 20 percent, repeat the calculation and identify one mechanism that could break the simplified assumption.

### Applying and challenging the concept

Prepare a two-column evidence ledger on **antibody classes**: direct observations versus explanatory assumptions. Draw a causal network for **antibody isotypes, structure and distribution** with one feedback edge. State how a null result could reflect either a false hypothesis or inadequate sampling.


## Topic 5.4 — Neutralization, opsonization and Fc receptors

### Biological mechanism

An antibody may prevent a ligand from contacting its receptor, promote uptake through Fc receptors, initiate complement in suitable contexts, or connect targets to immune effector cells. Different mechanisms require different molecular positions and cellular partners. Neutralization often depends strongly on epitope and binding geometry.

### Why a plausible explanation can fail

A high binding titer does not guarantee high neutralizing activity. Fc-associated functions can vary with isotype and receptor context. The same antibody may perform differently in an in vitro binding assay and a tissue where the relevant effector cell is scarce.

To challenge this account, use the related concept **memory cell dynamics** to propose a different route to the same observation. Which intermediate biological step would make the two hypotheses diverge?

### Designing an informative measurement

Consider invented binding and functional assay curves for two antibody preparations. Calculate the concentration needed for a specified effect in each model, then challenge the assumption that curves with equal maximum binding must have equal functional potency.

Define a control that separates assay background from biological mechanism. Sample before, during and after the expected response, and identify a second measurement that would corroborate the proposed pathway.

### Boundaries and counterexamples

There is no single numerical protective antibody threshold transferable across pathogens, vaccines or assays. Functional laboratory assays have assay-specific normalization and limitations.

Construct a counterexample where the measured signal changes without the proposed mechanism changing. Prioritize one alternative and choose an observation that would refute it.

### Quantitative worked case 5.4

**Problem.** A toy neutralization curve requires 4 arbitrary units for 50% effect, another requires 10. Compute second-to-first ratio.

**Hypothetical inputs:** second = 10, first = 4. **Relation:** `second/first`. **Answer:** **2.5 ratio**. Recompute independently and identify the physical or assay denominator, including the time interval where applicable.

**Interpretation:** Different functional curves can arise despite similar binding profiles. **Scope limit:** The assay is invented and has no clinical potency meaning. These invented inputs offer no independent biological replicates or measured variance. Change an input by 20 percent, repeat the calculation and identify one mechanism that could break the simplified assumption.

### Applying and challenging the concept

Prepare a two-column evidence ledger on **effector functions**: direct observations versus explanatory assumptions. Draw a causal network for **neutralization, opsonization and fc receptors** with one feedback edge. State how a null result could reflect either a false hypothesis or inadequate sampling.


## Topic 5.5 — Long-lived plasma cells, recall and vaccine responses

### Biological mechanism

Some differentiated plasma cells maintain antibody secretion for extended periods, while memory B cells can expand or diversify after re-exposure. A recall response may be faster or of higher effective affinity, but observed kinetics reflect baseline antibody, sampling time and prior exposure history. Helper-cell memory is also important.

### Why a plausible explanation can fail

An early antibody rise after boosting need not be caused only by brand-new clonal expansion; pre-existing antibodies and plasma cells contribute to the measured starting level. A falling serum titer does not prove complete loss of cellular memory.

To challenge this account, use the related concept **B-cell activation** to propose a different route to the same observation. Which intermediate biological step would make the two hypotheses diverge?

### Designing an informative measurement

Use paired hypothetical primary and recall curves to estimate time to a defined threshold, peak area and decline slope. Compare baseline-subtracted changes rather than simply placing curves on the same axis. Do not infer protection from an illustrative titer alone.

Define a control that separates assay background from biological mechanism. Sample before, during and after the expected response, and identify a second measurement that would corroborate the proposed pathway.

### Boundaries and counterexamples

Vaccine protection is antigen- and disease-specific and may involve T-cell as well as antibody effects. Immunization schedules and clinical decisions must follow appropriate public-health guidance, not this toy simulation.

Construct a counterexample where the measured signal changes without the proposed mechanism changing. Prioritize one alternative and choose an observation that would refute it.

### Quantitative worked case 5.5

**Problem.** A synthetic recall curve reaches a threshold after 4 days, while primary curve needs 11. Find time saved.

**Hypothetical inputs:** primary = 11, recall = 4. **Relation:** `primary-recall`. **Answer:** **7 days**. Recompute independently and identify the physical or assay denominator, including the time interval where applicable.

**Interpretation:** This timing comparison does not report protection probability. **Scope limit:** Curve durations are pedagogic, not observations. These invented inputs offer no independent biological replicates or measured variance. Change an input by 20 percent, repeat the calculation and identify one mechanism that could break the simplified assumption.

### Applying and challenging the concept

Prepare a two-column evidence ledger on **memory cell dynamics**: direct observations versus explanatory assumptions. Draw a causal network for **long-lived plasma cells, recall and vaccine responses** with one feedback edge. State how a null result could reflect either a false hypothesis or inadequate sampling.


## Integrated computational investigation — Binding abundance versus functional antibodies

### Question and rival explanations

Two antibody samples show similar binding signal but differing neutralization proxy. Is quantity or molecular function the key difference?

**Mechanistic hypothesis A:** The epitope geometry changes functional blockade.

**Mechanistic hypothesis B:** Antibody effective concentration or avidity differs across assays.

The challenge is not to select the explanation that seems familiar. First articulate the different predictions each account makes under a condition that would actually distinguish them. A mechanism might predict an early localized signal, whereas an alternative predicts a later population effect; both can reproduce the same final bulk number. Construct a causal diagram with the stimulus, intermediate state, assay output and at least one unmeasured covariate. Mark which relations are observed and which require assumptions. The invented numbers below are practice material only: no patients, animals, pathogen samples or laboratory measurements generated them.

### Research design

Compare synthetic normalized binding curves with functional inhibition curves at matched concentration. Include nonspecific binding control and annotate detection saturation separately from biological saturation.

**Principal confound:** Different assay dilution ranges or batch calibration can produce an apparent potency difference without underlying molecular change..

A study needs biological units that match the hypothesis. If all measurements come from one culture vessel, 50 images represent subsampling of that vessel, not 50 independent cultures. If hundreds of cells come from one donor, those cells cannot support donor-level generalization without a design that accounts for clustering. Predefine the primary comparison, effect direction, main covariates and quality exclusions. Calibrate instruments or report uncalibrated arbitrary units explicitly, and store the untouched data before plotting or normalization. Use safe computational methods for these classroom tasks; any real specimen acquisition requires proper authorization, ethics and biosafety oversight.

### Constructed series (not research data)

| Stage / sample index | Series A (invented) | Series B (invented) |
|---:|---:|---:|
| 0 | 5 | 4 |
| 1 | 25 | 17 |
| 2 | 52 | 35 |
| 3 | 78 | 61 |
| 4 | 90 | 79 |

Series A changes by **85** display units across the five stages; series B changes by **75**. Its endpoint ratio is **0.8778** if the chosen scales are comparable; if the assays do not share a scale, that arithmetic is only a display ratio and has no biological interpretation. Compute each sequence's initial-to-final proportional change separately. Plot the two curves, label axis units or 'arbitrary teaching index', and add no error bars: the dataset supplies no independent replicate variation. Do not invent significance levels, biological confidence intervals or citations to make synthetic observations appear empirical.

### Interpretation and identification

Both series rise but functional ranking cannot be established without specifying which output each measures and the uncertainty around the curve. The most important next step is to specify a discriminating measurement. A time course is better than a single endpoint when mechanisms have distinct delays, but unobserved confounding remains possible. A targeted perturbation can improve causal identification, provided it does not independently change the outcome through a second mechanism. Some data would make both hypotheses less plausible; identify such a result explicitly. The final answer should distinguish the direction of the constructed numbers, the mechanism proposed to explain them, and the missing evidence needed for a real biological conclusion.

### Structured analysis assignment

1. Write both hypotheses as falsifiable predictions for one named assay and an explicit time window.
2. State whether the sample unit is a donor, animal, organ, culture vessel or cell; explain why technical repetitions cannot silently increase biological sample size.
3. Quantify the endpoint and one interval rate, explaining any limitations due to missing time units.
4. Identify two alternative causes of the same observed trajectory, including the principal confound listed above.
5. Propose a safe, noninfectious follow-up or computational analysis and choose a criterion that would change your preferred explanation.
6. Produce a short reproducibility note giving data schema, graph labels, analysis pseudocode and a statement that all values are fictional.


## Systems synthesis and examination preparation

An immune network changes across compartments and timescales. This unit links **B-cell receptor signaling and helper cooperation**, **Germinal centers and affinity maturation**, **Antibody isotypes, structure and distribution**, **Neutralization, opsonization and Fc receptors** and **Long-lived plasma cells, recall and vaccine responses**. Try placing these concepts in a table with columns for recognition, cellular actors, immediate output, delayed outcome, negative regulation and an assay limitation. Some rows will not fit neatly: the same mediator may promote clearance and also exacerbate injury. Treat that apparent contradiction as a clue about concentrations, timing and tissue specificity rather than a reason to ignore the mechanism.

To test integration, imagine two specimens showing the same final reporter value despite different early trajectories. In one, a small number of strongly responding cells drive the signal; in the other, a large number of weakly responding cells produce an equal bulk total. A single bulk assay cannot resolve those explanations. Which of this unit's five mechanisms could generate the two situations, and what independent measurement would discriminate them? For every proposed measurement, identify whether it estimates a concentration, frequency, absolute count, location, phenotype or function. Then articulate the assumption that makes the measurement relevant.

Transfer the explanation from a controlled cell system into an intact tissue. Tissue oxygen, access to antigen, migration routes and regulatory signals could all change the qualitative outcome even if receptor-level biochemistry remains the same. Do not silently treat a monotonic curve as an empirical law valid across species, tissues and developmental stages. If you use the interactive model, name one omitted interaction and describe how including it might shift the curve, introduce a delay, or reverse the predicted comparison. Sensitivity to an assumed parameter is useful for learning but cannot establish that the chosen parameter value matches biology.

### End-of-unit synthesis questions

- Use **b-cell receptor signaling and helper cooperation** and **long-lived plasma cells, recall and vaccine responses** in one causal argument and identify where negative feedback could intervene.
- Present a competing hypothesis for a result initially attributed to **antibody isotypes, structure and distribution**. What measurement, with units, would favor one explanation?
- Explain how an apparent change in immune-cell frequency might arise with no change in absolute abundance of that population.
- Recompute one quantitative case with different assumptions and report which assumption contributes most to uncertainty.
- Choose a claim that would be dangerous to generalize into patient advice and explain why the available educational model cannot justify it.

**Editorial reminder:** The described scenarios are concept exercises, not real laboratory results. All clinical statements require authoritative evidence and, where applicable, qualified professional interpretation.
