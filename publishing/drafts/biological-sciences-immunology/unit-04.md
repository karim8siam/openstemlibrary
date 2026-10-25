# Unit 04 — T lymphocytes and cell-mediated responses

> **OpenSTEM Biological Sciences, Book 13: Immunology.** Undergraduate editorial draft; expert review pending. All numerical inputs and investigation records are hypothetical instructional examples. Models are not pathogen predictions, diagnostic tests, patient advice or clinical decision tools.

## Learning objectives and context

T-cell immunity is a changing population process. Developmental selection establishes a usable, limited repertoire; antigen encounter drives differentiated functions, and surviving cells populate memory compartments. The same molecular label can be found on cells with different functional states.

The five topics in this unit approach a common problem from different levels of explanation. They concern **thymic selection; activation threshold; helper differentiation; cytotoxic mechanisms; memory and exhaustion**. By the end, explain the core mechanism for each topic, identify at least two plausible alternative explanations for a measured signal, reproduce the arithmetic in five cases, and describe what data would actually falsify a claim. Separate the event being *detected* from the downstream consequence inferred from that event. In immunology, an increase in a reporter, a cytokine, a cell percentage or antibody binding often looks persuasive but rarely establishes host protection by itself.

A useful immune-system model declares its spatial scale, the biological unit and the time horizon. A molecule can bind within seconds, a cell may alter transcription over hours, a clone expands across days, and tissue structure or population immunity changes across longer periods. Measured concentrations cannot be substituted for cell numbers, and cell numbers cannot replace measurements of functional killing, pathogen burden or tissue function. Check whether a figure uses proportions of all live cells, proportions within a selected gate, copies per milliliter, fluorescence units or an actual physical rate. The denominator is part of the scientific claim.

## Evidence and responsible interpretation

An immune response depends on anatomical compartment and previous exposure. Blood samples provide valuable, accessible information but can miss tissue-resident populations and localized mediator gradients. Bulk averages hide rare cell populations and interactions. Healthy versus diseased comparisons can confound cause and consequence, while an intervention that changes two pathways at once may not isolate either one. For quantitative work, preserve raw counts, clarify calibration, distinguish independent donors from repeated technical wells, and describe measurement error separately from biological variation.

All activities in this unit are computational, synthetic-data or abstract analysis exercises. Do not culture pathogens, perform human or animal exposure experiments, or attempt clinical assays on personal samples from these pages. Appropriate institutional biosafety and ethics review are prerequisites for any real laboratory research. These pages never prescribe immunization, diagnosis or treatment.


## Topic 4.1 — Thymic development and central selection

### Biological mechanism

T-cell precursors develop in the thymus through staged receptor rearrangement, survival decisions and lineage commitment. Positive selection favors cells capable of interacting appropriately with self MHC, while negative selection and regulatory-lineage pathways reduce some strongly self-reactive outcomes. The resulting repertoire is useful but not perfectly free of self-reactivity.

### Why a plausible explanation can fail

Selection is influenced by ligand abundance, presentation and signaling duration, not merely one intrinsic affinity number. Thymic architecture and age alter the process. Some potentially reactive cells survive and are restrained later by peripheral tolerance, so central selection is not the only layer of protection.

To challenge this account, use the related concept **activation threshold** to propose a different route to the same observation. Which intermediate biological step would make the two hypotheses diverge?

### Designing an informative measurement

In a conceptual model, vary an affinity-selection window and track what fraction of random receptor strengths survives. Compare repertoire size with a surrogate self-reactivity risk; emphasize that no such single-number rule predicts individual T-cell fate in vivo.

Define a control that separates assay background from biological mechanism. Sample before, during and after the expected response, and identify a second measurement that would corroborate the proposed pathway.

### Boundaries and counterexamples

A simplified threshold diagram is not an experimental substitute for mapping thymic epithelial cells, peptide repertoires or regulatory T-cell development.

Construct a counterexample where the measured signal changes without the proposed mechanism changing. Prioritize one alternative and choose an observation that would refute it.

### Quantitative worked case 4.1

**Problem.** In a simulated selection window 160 out of 1000 random precursors survive. Compute survival fraction.

**Hypothetical inputs:** survived = 160, initial = 1000. **Relation:** `survived/initial*100`. **Answer:** **16 %**. Recompute independently and identify the physical or assay denominator, including the time interval where applicable.

**Interpretation:** The fraction summarizes a toy selection rule only. **Scope limit:** Real thymic survival has multiple stages and cell-level variability. These invented inputs offer no independent biological replicates or measured variance. Change an input by 20 percent, repeat the calculation and identify one mechanism that could break the simplified assumption.

### Applying and challenging the concept

Prepare a two-column evidence ledger on **thymic selection**: direct observations versus explanatory assumptions. Draw a causal network for **thymic development and central selection** with one feedback edge. State how a null result could reflect either a false hypothesis or inadequate sampling.


## Topic 4.2 — Clonal expansion and activation kinetics

### Biological mechanism

When a naive T cell meets a suitable peptide–MHC complex and supporting signals, it can enter a program of metabolic remodeling, proliferation and differentiation. Descendants of one precursor share receptor specificity but may occupy distinct functional or memory states. Antigen persistence and cytokine environment alter expansion and contraction.

### Why a plausible explanation can fail

Cell counts at one time cannot distinguish increased division from improved survival or changed trafficking. Higher numbers of activated cells do not guarantee better pathogen control, particularly when target tissues are inaccessible or suppression dominates.

To challenge this account, use the related concept **helper differentiation** to propose a different route to the same observation. Which intermediate biological step would make the two hypotheses diverge?

### Designing an informative measurement

Use a constructed cell-count sequence to estimate population fold change and approximate doubling time over an explicitly exponential interval. Track division dye and apoptosis markers conceptually to separate replication from survival. Do not apply the same doubling rate indefinitely.

Define a control that separates assay background from biological mechanism. Sample before, during and after the expected response, and identify a second measurement that would corroborate the proposed pathway.

### Boundaries and counterexamples

Real clonal growth is limited by resources, regulatory circuits and antigen dynamics. An exponential curve can illustrate early expansion but becomes implausible when extrapolated across long periods.

Construct a counterexample where the measured signal changes without the proposed mechanism changing. Prioritize one alternative and choose an observation that would refute it.

### Quantitative worked case 4.2

**Problem.** A synthetic clone increases from 125 to 1000 cells during 18 hours of early exponential growth. Find approximate doubling time.

**Hypothetical inputs:** hours = 18, end = 1000, start = 125. **Relation:** `hours/(math.log(end/start,2))`. **Answer:** **6 h**. Recompute independently and identify the physical or assay denominator, including the time interval where applicable.

**Interpretation:** Three doublings over 18 hours yield six hours per doubling. **Scope limit:** A real T-cell clone will eventually cease exponential expansion. These invented inputs offer no independent biological replicates or measured variance. Change an input by 20 percent, repeat the calculation and identify one mechanism that could break the simplified assumption.

### Applying and challenging the concept

Prepare a two-column evidence ledger on **activation threshold**: direct observations versus explanatory assumptions. Draw a causal network for **clonal expansion and activation kinetics** with one feedback edge. State how a null result could reflect either a false hypothesis or inadequate sampling.


## Topic 4.3 — CD4 helper subsets and functional plasticity

### Biological mechanism

Activated CD4 lymphocytes can adopt helper programs associated with distinct cytokine patterns and tissue functions, including follicular help, inflammatory macrophage support and barrier-associated responses. Transcription-factor networks and local cytokines influence these fates, and individual cells can change phenotype over time.

### Why a plausible explanation can fail

The familiar labels Th1, Th2, Th17, Tfh and regulatory T cells are explanatory categories rather than perfectly exclusive boxes. A cytokine measured in supernatant may arise from several cell types. It is possible to observe a marker signature without demonstrating the corresponding effector function.

To challenge this account, use the related concept **cytotoxic mechanisms** to propose a different route to the same observation. Which intermediate biological step would make the two hypotheses diverge?

### Designing an informative measurement

Compare a hypothetical single-cell expression matrix before and after a defined activation context. Calculate proportions of selected signatures and then inspect cells that express overlapping markers. Use protein measurements or functional readouts as independent validation.

Define a control that separates assay background from biological mechanism. Sample before, during and after the expected response, and identify a second measurement that would corroborate the proposed pathway.

### Boundaries and counterexamples

Not every marker identifies a stable lineage, and the relative value of a helper response depends on the infection and tissue. Oversimplified claims that one subset is always protective are misleading.

Construct a counterexample where the measured signal changes without the proposed mechanism changing. Prioritize one alternative and choose an observation that would refute it.

### Quantitative worked case 4.3

**Problem.** In 240 synthetic CD4 cells, 36 express both markers A and B. Find overlapping-marker proportion.

**Hypothetical inputs:** overlap = 36, n = 240. **Relation:** `overlap/n*100`. **Answer:** **15 %**. Recompute independently and identify the physical or assay denominator, including the time interval where applicable.

**Interpretation:** Overlaps complicate mutually exclusive helper-subset classifications. **Scope limit:** Expression alone does not establish stable effector identity. These invented inputs offer no independent biological replicates or measured variance. Change an input by 20 percent, repeat the calculation and identify one mechanism that could break the simplified assumption.

### Applying and challenging the concept

Prepare a two-column evidence ledger on **helper differentiation**: direct observations versus explanatory assumptions. Draw a causal network for **cd4 helper subsets and functional plasticity** with one feedback edge. State how a null result could reflect either a false hypothesis or inadequate sampling.


## Topic 4.4 — CD8 cytotoxicity and target-cell recognition

### Biological mechanism

Activated CD8 T cells can recognize suitable peptide–MHC-I complexes on targets and deliver perforin/granzyme-associated lethal signals or use death-receptor pathways. Synapse formation localizes these effects, while serial interactions allow one effector to encounter multiple targets. Cytokine release contributes additional noncytolytic effects.

### Why a plausible explanation can fail

Target death can vary with MHC-I expression, antigen abundance, effector-to-target ratio and target resistance, not merely effector-cell number. Cell lysis and viral suppression are different endpoints; a cell can reduce replication without killing every infected target.

To challenge this account, use the related concept **memory and exhaustion** to propose a different route to the same observation. Which intermediate biological step would make the two hypotheses diverge?

### Designing an informative measurement

Analyze a synthetic time series of target survival at several effector-to-target ratios. Distinguish spontaneous target-cell death from effector-associated death and use a matched control condition. Show confidence intervals only if independent replicate variability is supplied.

Define a control that separates assay background from biological mechanism. Sample before, during and after the expected response, and identify a second measurement that would corroborate the proposed pathway.

### Boundaries and counterexamples

A culture assay does not fully model tissue trafficking, antigen escape or off-target injury. Increasing effector ratio in a dish is not a clinical dosing rule.

Construct a counterexample where the measured signal changes without the proposed mechanism changing. Prioritize one alternative and choose an observation that would refute it.

### Quantitative worked case 4.4

**Problem.** A mock cytotoxicity assay observes 32 dead target cells among 200 total at a fixed time. Find death proportion.

**Hypothetical inputs:** dead = 32, targets = 200. **Relation:** `dead/targets*100`. **Answer:** **16 %**. Recompute independently and identify the physical or assay denominator, including the time interval where applicable.

**Interpretation:** The result needs subtraction of background death for a specific effect. **Scope limit:** No tumor-treatment efficacy can be inferred from these numbers. These invented inputs offer no independent biological replicates or measured variance. Change an input by 20 percent, repeat the calculation and identify one mechanism that could break the simplified assumption.

### Applying and challenging the concept

Prepare a two-column evidence ledger on **cytotoxic mechanisms**: direct observations versus explanatory assumptions. Draw a causal network for **cd8 cytotoxicity and target-cell recognition** with one feedback edge. State how a null result could reflect either a false hypothesis or inadequate sampling.


## Topic 4.5 — Regulatory T cells, contraction and memory

### Biological mechanism

Regulatory populations help maintain tolerance through inhibitory signaling, cytokines and changes in access to growth factors or antigen-presenting cells. After a response peaks, many effectors contract while some survive as memory cells with differing migration and tissue-residency properties. Memory reflects both cell number and future response capacity.

### Why a plausible explanation can fail

A fall in blood T-cell frequency can reflect migration rather than disappearance. Similarly, high expression of an inhibitory receptor alone does not prove irreversible exhaustion; chronic antigen exposure changes multiple molecular programs, and functional context matters.

To challenge this account, use the related concept **thymic selection** to propose a different route to the same observation. Which intermediate biological step would make the two hypotheses diverge?

### Designing an informative measurement

Consider a hypothetical longitudinal repertoire where circulating clone abundance declines while a tissue compartment retains cells. Compute apparent half-life and test whether the conclusion changes when redistribution is modeled. Use distinct assays for phenotype and functional recall.

Define a control that separates assay background from biological mechanism. Sample before, during and after the expected response, and identify a second measurement that would corroborate the proposed pathway.

### Boundaries and counterexamples

Memory does not guarantee sterilizing protection against every variant or at every site. Tissue conditions and pathogen evolution limit extrapolation from one blood sample.

Construct a counterexample where the measured signal changes without the proposed mechanism changing. Prioritize one alternative and choose an observation that would refute it.

### Quantitative worked case 4.5

**Problem.** In a decline-phase cell series, a clone falls from 640 to 160 cells over 12 days. Compute apparent exponential half-life.

**Hypothetical inputs:** days = 12, start = 640, end = 160. **Relation:** `days/math.log(start/end,2)`. **Answer:** **6 days**. Recompute independently and identify the physical or assay denominator, including the time interval where applicable.

**Interpretation:** Decline in sampled compartment may reflect redistribution. **Scope limit:** Cell attrition and trafficking are confounded in blood-only measurements. These invented inputs offer no independent biological replicates or measured variance. Change an input by 20 percent, repeat the calculation and identify one mechanism that could break the simplified assumption.

### Applying and challenging the concept

Prepare a two-column evidence ledger on **memory and exhaustion**: direct observations versus explanatory assumptions. Draw a causal network for **regulatory t cells, contraction and memory** with one feedback edge. State how a null result could reflect either a false hypothesis or inadequate sampling.


## Integrated computational investigation — Clone growth or altered migration?

### Question and rival explanations

Antigen-specific T-cell counts rise in a node then fall in blood, but a tissue biopsy continues to show activity. How should a population balance be framed?

**Mechanistic hypothesis A:** Net proliferation followed by contraction is dominant.

**Mechanistic hypothesis B:** Redistribution across compartments explains much of the decline.

The challenge is not to select the explanation that seems familiar. First articulate the different predictions each account makes under a condition that would actually distinguish them. A mechanism might predict an early localized signal, whereas an alternative predicts a later population effect; both can reproduce the same final bulk number. Construct a causal diagram with the stimulus, intermediate state, assay output and at least one unmeasured covariate. Mark which relations are observed and which require assumptions. The invented numbers below are practice material only: no patients, animals, pathogen samples or laboratory measurements generated them.

### Research design

Construct population accounting for entry, division, death and exit in hypothetical compartments. Use absolute counts rather than percentages and inspect intervals rather than one endpoint.

**Principal confound:** Different recovery of cells from tissue versus blood can mimic migration, especially if fractions are normalized to changing totals..

A study needs biological units that match the hypothesis. If all measurements come from one culture vessel, 50 images represent subsampling of that vessel, not 50 independent cultures. If hundreds of cells come from one donor, those cells cannot support donor-level generalization without a design that accounts for clustering. Predefine the primary comparison, effect direction, main covariates and quality exclusions. Calibrate instruments or report uncalibrated arbitrary units explicitly, and store the untouched data before plotting or normalization. Use safe computational methods for these classroom tasks; any real specimen acquisition requires proper authorization, ethics and biosafety oversight.

### Constructed series (not research data)

| Stage / sample index | Series A (invented) | Series B (invented) |
|---:|---:|---:|
| 0 | 10 | 2 |
| 1 | 20 | 4 |
| 2 | 40 | 7 |
| 3 | 25 | 12 |
| 4 | 13 | 18 |

Series A changes by **3** display units across the five stages; series B changes by **16**. Its endpoint ratio is **1.385** if the chosen scales are comparable; if the assays do not share a scale, that arithmetic is only a display ratio and has no biological interpretation. Compute each sequence's initial-to-final proportional change separately. Plot the two curves, label axis units or 'arbitrary teaching index', and add no error bars: the dataset supplies no independent replicate variation. Do not invent significance levels, biological confidence intervals or citations to make synthetic observations appear empirical.

### Interpretation and identification

One group peaks then declines while the other accumulates. This qualitative pattern can be explained by multiple flux combinations. The most important next step is to specify a discriminating measurement. A time course is better than a single endpoint when mechanisms have distinct delays, but unobserved confounding remains possible. A targeted perturbation can improve causal identification, provided it does not independently change the outcome through a second mechanism. Some data would make both hypotheses less plausible; identify such a result explicitly. The final answer should distinguish the direction of the constructed numbers, the mechanism proposed to explain them, and the missing evidence needed for a real biological conclusion.

### Structured analysis assignment

1. Write both hypotheses as falsifiable predictions for one named assay and an explicit time window.
2. State whether the sample unit is a donor, animal, organ, culture vessel or cell; explain why technical repetitions cannot silently increase biological sample size.
3. Quantify the endpoint and one interval rate, explaining any limitations due to missing time units.
4. Identify two alternative causes of the same observed trajectory, including the principal confound listed above.
5. Propose a safe, noninfectious follow-up or computational analysis and choose a criterion that would change your preferred explanation.
6. Produce a short reproducibility note giving data schema, graph labels, analysis pseudocode and a statement that all values are fictional.


## Systems synthesis and examination preparation

An immune network changes across compartments and timescales. This unit links **Thymic development and central selection**, **Clonal expansion and activation kinetics**, **CD4 helper subsets and functional plasticity**, **CD8 cytotoxicity and target-cell recognition** and **Regulatory T cells, contraction and memory**. Try placing these concepts in a table with columns for recognition, cellular actors, immediate output, delayed outcome, negative regulation and an assay limitation. Some rows will not fit neatly: the same mediator may promote clearance and also exacerbate injury. Treat that apparent contradiction as a clue about concentrations, timing and tissue specificity rather than a reason to ignore the mechanism.

To test integration, imagine two specimens showing the same final reporter value despite different early trajectories. In one, a small number of strongly responding cells drive the signal; in the other, a large number of weakly responding cells produce an equal bulk total. A single bulk assay cannot resolve those explanations. Which of this unit's five mechanisms could generate the two situations, and what independent measurement would discriminate them? For every proposed measurement, identify whether it estimates a concentration, frequency, absolute count, location, phenotype or function. Then articulate the assumption that makes the measurement relevant.

Transfer the explanation from a controlled cell system into an intact tissue. Tissue oxygen, access to antigen, migration routes and regulatory signals could all change the qualitative outcome even if receptor-level biochemistry remains the same. Do not silently treat a monotonic curve as an empirical law valid across species, tissues and developmental stages. If you use the interactive model, name one omitted interaction and describe how including it might shift the curve, introduce a delay, or reverse the predicted comparison. Sensitivity to an assumed parameter is useful for learning but cannot establish that the chosen parameter value matches biology.

### End-of-unit synthesis questions

- Use **thymic development and central selection** and **regulatory t cells, contraction and memory** in one causal argument and identify where negative feedback could intervene.
- Present a competing hypothesis for a result initially attributed to **cd4 helper subsets and functional plasticity**. What measurement, with units, would favor one explanation?
- Explain how an apparent change in immune-cell frequency might arise with no change in absolute abundance of that population.
- Recompute one quantitative case with different assumptions and report which assumption contributes most to uncertainty.
- Choose a claim that would be dangerous to generalize into patient advice and explain why the available educational model cannot justify it.

**Editorial reminder:** The described scenarios are concept exercises, not real laboratory results. All clinical statements require authoritative evidence and, where applicable, qualified professional interpretation.
