# Unit 01 — Immune organization and the logic of host defense

> **OpenSTEM Biological Sciences, Book 13: Immunology.** Undergraduate editorial draft; expert review pending. All numerical inputs and investigation records are hypothetical instructional examples. Models are not pathogen predictions, diagnostic tests, patient advice or clinical decision tools.

## Learning objectives and context

Immunity is a distributed sensing and response system, not a single organ that detects everything equally. Physical barriers, fast pattern recognition, clonal specificity and memory solve different portions of the defense problem. A first-year reader must distinguish a mechanism that blocks entry from one that limits replication after entry, and both from regulation that prevents collateral damage.

The five topics in this unit approach a common problem from different levels of explanation. They concern **location and timing; innate–adaptive integration; self and nonself are not absolute rules; compartment-specific exposure; cost and protection**. By the end, explain the core mechanism for each topic, identify at least two plausible alternative explanations for a measured signal, reproduce the arithmetic in five cases, and describe what data would actually falsify a claim. Separate the event being *detected* from the downstream consequence inferred from that event. In immunology, an increase in a reporter, a cytokine, a cell percentage or antibody binding often looks persuasive but rarely establishes host protection by itself.

A useful immune-system model declares its spatial scale, the biological unit and the time horizon. A molecule can bind within seconds, a cell may alter transcription over hours, a clone expands across days, and tissue structure or population immunity changes across longer periods. Measured concentrations cannot be substituted for cell numbers, and cell numbers cannot replace measurements of functional killing, pathogen burden or tissue function. Check whether a figure uses proportions of all live cells, proportions within a selected gate, copies per milliliter, fluorescence units or an actual physical rate. The denominator is part of the scientific claim.

## Evidence and responsible interpretation

An immune response depends on anatomical compartment and previous exposure. Blood samples provide valuable, accessible information but can miss tissue-resident populations and localized mediator gradients. Bulk averages hide rare cell populations and interactions. Healthy versus diseased comparisons can confound cause and consequence, while an intervention that changes two pathways at once may not isolate either one. For quantitative work, preserve raw counts, clarify calibration, distinguish independent donors from repeated technical wells, and describe measurement error separately from biological variation.

All activities in this unit are computational, synthetic-data or abstract analysis exercises. Do not culture pathogens, perform human or animal exposure experiments, or attempt clinical assays on personal samples from these pages. Appropriate institutional biosafety and ethics review are prerequisites for any real laboratory research. These pages never prescribe immunization, diagnosis or treatment.


## Topic 1.1 — Barrier tissues and mucosal defense

### Biological mechanism

Skin and mucosal surfaces combine structural separation, epithelial turnover, antimicrobial chemistry, local antibodies and resident immune populations. Tight junctions change paracellular permeability while mucus and ciliary clearance move particles away from vulnerable surfaces. The gut must handle food molecules and enormous microbial communities without constantly producing destructive inflammation.

### Why a plausible explanation can fail

Barrier injury changes pathogen access but also changes inflammatory cues, tissue oxygen and local microbiota. An apparent infection susceptibility phenotype may therefore result from a wound, a signaling defect, or changed commensal competition. IgA is prominent in mucosal protection, yet antibody concentration alone cannot measure epithelial resilience.

To challenge this account, use the related concept **innate–adaptive integration** to propose a different route to the same observation. Which intermediate biological step would make the two hypotheses diverge?

### Designing an informative measurement

A noninfectious epithelial cell model can measure tracer permeability and junctional protein localization. Pair the permeability assay with viability and morphology; leakage after cell death does not prove regulated junction opening. A change in secreted antimicrobial peptides needs a separate expression or protein measurement.

Define a control that separates assay background from biological mechanism. Sample before, during and after the expected response, and identify a second measurement that would corroborate the proposed pathway.

### Boundaries and counterexamples

A surface that is impermeable to an experimental dye is not necessarily resistant to a living pathogen. The pathogen may use transcellular invasion, secreted enzymes or entry through a different tissue, and artificial culture surfaces lack real tissue architecture.

Construct a counterexample where the measured signal changes without the proposed mechanism changing. Prioritize one alternative and choose an observation that would refute it.

### Quantitative worked case 1.1

**Problem.** A mock epithelial tracer has baseline flux 2.4 arbitrary units/min and challenge flux 3.6. Find the relative increase.

**Hypothetical inputs:** baseline = 2.4, challenge = 3.6. **Relation:** `(challenge-baseline)/baseline*100`. **Answer:** **50 %**. Recompute independently and identify the physical or assay denominator, including the time interval where applicable.

**Interpretation:** The calculation quantifies permeability proxy change, not infection susceptibility. **Scope limit:** Tracer diffusion and biological pathogen entry need not follow the same path. These invented inputs offer no independent biological replicates or measured variance. Change an input by 20 percent, repeat the calculation and identify one mechanism that could break the simplified assumption.

### Applying and challenging the concept

Prepare a two-column evidence ledger on **location and timing**: direct observations versus explanatory assumptions. Draw a causal network for **barrier tissues and mucosal defense** with one feedback edge. State how a null result could reflect either a false hypothesis or inadequate sampling.


## Topic 1.2 — Hematopoiesis and immune-cell lineages

### Biological mechanism

Blood and many immune cells arise from hematopoietic stem and progenitor populations in bone marrow. Developmental paths generate granulocytes, monocytes, dendritic-cell subsets and lymphocyte lineages, with tissue residence and circulating recruitment varying substantially by population. Mature immune identity reflects both developmental history and signals encountered after entering a tissue.

### Why a plausible explanation can fail

A conventional lineage tree is useful but insufficient for describing activation states. Tissue macrophages can be maintained locally, and a cell expressing an activation marker may not have changed its developmental lineage. Cell abundance in blood is not a direct census of the entire immune system.

To challenge this account, use the related concept **self and nonself are not absolute rules** to propose a different route to the same observation. Which intermediate biological step would make the two hypotheses diverge?

### Designing an informative measurement

Compare flow-cytometry counts in blood and dissociated tissue under a defined mock challenge. Use panels with exclusion of dead cells and single-cell gating. Report marker definitions and absolute counts when possible, because percentages can change when a different population expands.

Define a control that separates assay background from biological mechanism. Sample before, during and after the expected response, and identify a second measurement that would corroborate the proposed pathway.

### Boundaries and counterexamples

Names such as myeloid and lymphoid are broad descriptions, not absolute boundaries for every dendritic or innate-like lymphocyte state. One surface marker rarely identifies a biologically homogeneous cell type.

Construct a counterexample where the measured signal changes without the proposed mechanism changing. Prioritize one alternative and choose an observation that would refute it.

### Quantitative worked case 1.2

**Problem.** A synthetic flow sample contains 3600 viable leukocytes among 15000 total counted events. Find the viable-leukocyte fraction.

**Hypothetical inputs:** viable = 3600, total = 15000. **Relation:** `viable/total*100`. **Answer:** **24 %**. Recompute independently and identify the physical or assay denominator, including the time interval where applicable.

**Interpretation:** The denominator controls interpretation; this is not a blood count. **Scope limit:** Gating decisions and sample preparation change event representation. These invented inputs offer no independent biological replicates or measured variance. Change an input by 20 percent, repeat the calculation and identify one mechanism that could break the simplified assumption.

### Applying and challenging the concept

Prepare a two-column evidence ledger on **innate–adaptive integration**: direct observations versus explanatory assumptions. Draw a causal network for **hematopoiesis and immune-cell lineages** with one feedback edge. State how a null result could reflect either a false hypothesis or inadequate sampling.


## Topic 1.3 — Lymphoid organs and cell trafficking

### Biological mechanism

Bone marrow and thymus support lymphocyte production or maturation; lymph nodes, spleen and mucosa-associated lymphoid structures promote surveillance and coordinated responses. Dendritic cells transport information from tissues while naive lymphocytes recirculate through secondary lymphoid regions. Chemokines, adhesion molecules and specialized vascular barriers affect where cells enter and remain.

### Why a plausible explanation can fail

The spleen filters blood-associated material, whereas a draining lymph node samples lymph from defined tissues. The same antigen can therefore produce different measured kinetics depending on route of encounter. Lymph-node enlargement reflects many possible events: increased entry, proliferation, vascular changes, or stromal remodeling.

To challenge this account, use the related concept **compartment-specific exposure** to propose a different route to the same observation. Which intermediate biological step would make the two hypotheses diverge?

### Designing an informative measurement

Use a hypothetical fluorescent cell-tracking dataset to estimate entry and exit rates from a node. Track cell proliferation separately so accumulated fluorescence is not automatically interpreted as immigration. Temporal sampling matters because retention and recruitment can look identical at one time point.

Define a control that separates assay background from biological mechanism. Sample before, during and after the expected response, and identify a second measurement that would corroborate the proposed pathway.

### Boundaries and counterexamples

A drawing of a lymph node as several homogeneous zones masks the architecture of follicles, T-cell regions, stromal guidance and vascular access. Do not infer anatomical pathways from a bulk sequencing sample.

Construct a counterexample where the measured signal changes without the proposed mechanism changing. Prioritize one alternative and choose an observation that would refute it.

### Quantitative worked case 1.3

**Problem.** In a mock node-tracking model, 120 cells enter each hour and 35 exit each hour. What is one-hour net accumulation with no proliferation?

**Hypothetical inputs:** entry = 120, exit = 35. **Relation:** `entry-exit`. **Answer:** **85 cells/hour**. Recompute independently and identify the physical or assay denominator, including the time interval where applicable.

**Interpretation:** Immigration and loss must both be measured to infer accumulation. **Scope limit:** Actual nodes include division, apoptosis and time-variable traffic. These invented inputs offer no independent biological replicates or measured variance. Change an input by 20 percent, repeat the calculation and identify one mechanism that could break the simplified assumption.

### Applying and challenging the concept

Prepare a two-column evidence ledger on **self and nonself are not absolute rules**: direct observations versus explanatory assumptions. Draw a causal network for **lymphoid organs and cell trafficking** with one feedback edge. State how a null result could reflect either a false hypothesis or inadequate sampling.


## Topic 1.4 — Innate and adaptive immunity compared

### Biological mechanism

Innate sensors recognize classes of microbial or injury-associated features and can act within minutes to hours; adaptive lymphocytes use diverse somatically rearranged receptors that undergo clonal selection and often require days for a primary response. Dendritic cells link the systems by presenting antigen and supplying context-dependent activation signals. Memory changes subsequent responses, though several innate populations can also display trained or altered states.

### Why a plausible explanation can fail

Innate does not mean nonspecific in every sense, nor does adaptive imply an automatic protective outcome. Pattern-recognition receptors have defined molecular recognition properties, while antibodies can cross-react. A rapid second response may reflect pre-existing antibodies, tissue-resident cells, or both.

To challenge this account, use the related concept **cost and protection** to propose a different route to the same observation. Which intermediate biological step would make the two hypotheses diverge?

### Designing an informative measurement

Plot separately a hypothetical interferon-associated transcript, antigen-specific cell number and antibody concentration over time. Do not compare raw heights across assays with different units. Annotate what signal identifies and which biological population produces it.

Define a control that separates assay background from biological mechanism. Sample before, during and after the expected response, and identify a second measurement that would corroborate the proposed pathway.

### Boundaries and counterexamples

Not all early defenses precede all adaptive events in a strict sequence. Existing memory cells and antibodies may operate immediately, and innate inflammation can persist long after antigen-specific cells expand.

Construct a counterexample where the measured signal changes without the proposed mechanism changing. Prioritize one alternative and choose an observation that would refute it.

### Quantitative worked case 1.4

**Problem.** Illustrative reporter signals are 2 units at time zero and 14 units after stimulation. Find fold change.

**Hypothetical inputs:** after = 14, before = 2. **Relation:** `after/before`. **Answer:** **7 fold**. Recompute independently and identify the physical or assay denominator, including the time interval where applicable.

**Interpretation:** Fold change expresses a relative contrast not a shared absolute molecular scale. **Scope limit:** Baseline background and saturation can substantially alter ratios. These invented inputs offer no independent biological replicates or measured variance. Change an input by 20 percent, repeat the calculation and identify one mechanism that could break the simplified assumption.

### Applying and challenging the concept

Prepare a two-column evidence ledger on **compartment-specific exposure**: direct observations versus explanatory assumptions. Draw a causal network for **innate and adaptive immunity compared** with one feedback edge. State how a null result could reflect either a false hypothesis or inadequate sampling.


## Topic 1.5 — Defense, immunopathology and homeostasis

### Biological mechanism

An effective response must reduce the probability or severity of harmful infection while limiting tissue damage. Cytokines recruit and instruct cells, but the same mediators can impair normal function when excessive, misplaced or persistent. Repair, resolution and regulatory circuits are active biological processes rather than passive disappearance of an antigen.

### Why a plausible explanation can fail

Higher inflammation is not automatically stronger protection. A treatment can lower pathogen burden yet damage the organ, or reduce inflammatory symptoms while permitting uncontrolled replication. Distinguish pathogen burden, immune activation, tissue injury and organism-level function as separate response variables.

To challenge this account, use the related concept **location and timing** to propose a different route to the same observation. Which intermediate biological step would make the two hypotheses diverge?

### Designing an informative measurement

In a hypothetical paired dataset, report a pathogen-related signal alongside a tissue-injury biomarker, and test whether the measures change in the same direction. Randomize sampling and avoid treating an inflammatory marker as a direct numerical measure of pathogen clearance.

Define a control that separates assay background from biological mechanism. Sample before, during and after the expected response, and identify a second measurement that would corroborate the proposed pathway.

### Boundaries and counterexamples

A patient-facing outcome cannot be predicted from a simplified marker model alone. Genetics, prior exposures, organ function and treatment timing alter relationships; this book does not provide diagnosis or therapy guidance.

Construct a counterexample where the measured signal changes without the proposed mechanism changing. Prioritize one alternative and choose an observation that would refute it.

### Quantitative worked case 1.5

**Problem.** An invented injury proxy rises from 8 to 12 while a microbial-proxy signal falls from 50 to 20. Calculate percentage change in injury proxy.

**Hypothetical inputs:** before = 8, after = 12. **Relation:** `(after-before)/before*100`. **Answer:** **50 %**. Recompute independently and identify the physical or assay denominator, including the time interval where applicable.

**Interpretation:** A higher injury readout can coincide with lower microbial readout. **Scope limit:** Neither toy readout constitutes evidence of a particular disease course. These invented inputs offer no independent biological replicates or measured variance. Change an input by 20 percent, repeat the calculation and identify one mechanism that could break the simplified assumption.

### Applying and challenging the concept

Prepare a two-column evidence ledger on **cost and protection**: direct observations versus explanatory assumptions. Draw a causal network for **defense, immunopathology and homeostasis** with one feedback edge. State how a null result could reflect either a false hypothesis or inadequate sampling.


## Integrated computational investigation — Separating barrier permeability from inflammatory state

### Question and rival explanations

An epithelium becomes more permeable after a noninfectious stress, and a cytokine reporter also rises. Which change caused the other, or might they share an upstream injury?

**Mechanistic hypothesis A:** Junction remodeling leads to secondary signaling.

**Mechanistic hypothesis B:** Signaling alters junctions without large-scale cell death.

The challenge is not to select the explanation that seems familiar. First articulate the different predictions each account makes under a condition that would actually distinguish them. A mechanism might predict an early localized signal, whereas an alternative predicts a later population effect; both can reproduce the same final bulk number. Construct a causal diagram with the stimulus, intermediate state, assay output and at least one unmeasured covariate. Mark which relations are observed and which require assumptions. The invented numbers below are practice material only: no patients, animals, pathogen samples or laboratory measurements generated them.

### Research design

Construct a factorial experiment with stress absent/present and receptor blocker absent/present in an ethically sourced, noninfectious teaching cell-line model. Measure tracer movement, viability, junction localization and reporter intensity at several times.

**Principal confound:** Changes in viable monolayer area mimic increased tracer movement even when tight-junction properties of surviving cells are unchanged..

A study needs biological units that match the hypothesis. If all measurements come from one culture vessel, 50 images represent subsampling of that vessel, not 50 independent cultures. If hundreds of cells come from one donor, those cells cannot support donor-level generalization without a design that accounts for clustering. Predefine the primary comparison, effect direction, main covariates and quality exclusions. Calibrate instruments or report uncalibrated arbitrary units explicitly, and store the untouched data before plotting or normalization. Use safe computational methods for these classroom tasks; any real specimen acquisition requires proper authorization, ethics and biosafety oversight.

### Constructed series (not research data)

| Stage / sample index | Series A (invented) | Series B (invented) |
|---:|---:|---:|
| 0 | 1 | 1 |
| 1 | 1.3 | 1.1 |
| 2 | 1.8 | 1.2 |
| 3 | 2 | 1.5 |
| 4 | 2.1 | 1.8 |

Series A changes by **1.1** display units across the five stages; series B changes by **0.8**. Its endpoint ratio is **0.8571** if the chosen scales are comparable; if the assays do not share a scale, that arithmetic is only a display ratio and has no biological interpretation. Compute each sequence's initial-to-final proportional change separately. Plot the two curves, label axis units or 'arbitrary teaching index', and add no error bars: the dataset supplies no independent replicate variation. Do not invent significance levels, biological confidence intervals or citations to make synthetic observations appear empirical.

### Interpretation and identification

Divergence in early trajectories could suggest timing differences but not alone establish direction. An additional perturbation specific to junction organization or the signaling receptor improves causal leverage. The most important next step is to specify a discriminating measurement. A time course is better than a single endpoint when mechanisms have distinct delays, but unobserved confounding remains possible. A targeted perturbation can improve causal identification, provided it does not independently change the outcome through a second mechanism. Some data would make both hypotheses less plausible; identify such a result explicitly. The final answer should distinguish the direction of the constructed numbers, the mechanism proposed to explain them, and the missing evidence needed for a real biological conclusion.

### Structured analysis assignment

1. Write both hypotheses as falsifiable predictions for one named assay and an explicit time window.
2. State whether the sample unit is a donor, animal, organ, culture vessel or cell; explain why technical repetitions cannot silently increase biological sample size.
3. Quantify the endpoint and one interval rate, explaining any limitations due to missing time units.
4. Identify two alternative causes of the same observed trajectory, including the principal confound listed above.
5. Propose a safe, noninfectious follow-up or computational analysis and choose a criterion that would change your preferred explanation.
6. Produce a short reproducibility note giving data schema, graph labels, analysis pseudocode and a statement that all values are fictional.


## Systems synthesis and examination preparation

An immune network changes across compartments and timescales. This unit links **Barrier tissues and mucosal defense**, **Hematopoiesis and immune-cell lineages**, **Lymphoid organs and cell trafficking**, **Innate and adaptive immunity compared** and **Defense, immunopathology and homeostasis**. Try placing these concepts in a table with columns for recognition, cellular actors, immediate output, delayed outcome, negative regulation and an assay limitation. Some rows will not fit neatly: the same mediator may promote clearance and also exacerbate injury. Treat that apparent contradiction as a clue about concentrations, timing and tissue specificity rather than a reason to ignore the mechanism.

To test integration, imagine two specimens showing the same final reporter value despite different early trajectories. In one, a small number of strongly responding cells drive the signal; in the other, a large number of weakly responding cells produce an equal bulk total. A single bulk assay cannot resolve those explanations. Which of this unit's five mechanisms could generate the two situations, and what independent measurement would discriminate them? For every proposed measurement, identify whether it estimates a concentration, frequency, absolute count, location, phenotype or function. Then articulate the assumption that makes the measurement relevant.

Transfer the explanation from a controlled cell system into an intact tissue. Tissue oxygen, access to antigen, migration routes and regulatory signals could all change the qualitative outcome even if receptor-level biochemistry remains the same. Do not silently treat a monotonic curve as an empirical law valid across species, tissues and developmental stages. If you use the interactive model, name one omitted interaction and describe how including it might shift the curve, introduce a delay, or reverse the predicted comparison. Sensitivity to an assumed parameter is useful for learning but cannot establish that the chosen parameter value matches biology.

### End-of-unit synthesis questions

- Use **barrier tissues and mucosal defense** and **defense, immunopathology and homeostasis** in one causal argument and identify where negative feedback could intervene.
- Present a competing hypothesis for a result initially attributed to **lymphoid organs and cell trafficking**. What measurement, with units, would favor one explanation?
- Explain how an apparent change in immune-cell frequency might arise with no change in absolute abundance of that population.
- Recompute one quantitative case with different assumptions and report which assumption contributes most to uncertainty.
- Choose a claim that would be dangerous to generalize into patient advice and explain why the available educational model cannot justify it.

**Editorial reminder:** The described scenarios are concept exercises, not real laboratory results. All clinical statements require authoritative evidence and, where applicable, qualified professional interpretation.
