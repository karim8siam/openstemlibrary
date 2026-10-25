# Unit 03 — Antigen recognition, processing and presentation

> **OpenSTEM Biological Sciences, Book 13: Immunology.** Undergraduate editorial draft; expert review pending. All numerical inputs and investigation records are hypothetical instructional examples. Models are not pathogen predictions, diagnostic tests, patient advice or clinical decision tools.

## Learning objectives and context

Adaptive specificity depends on what a receptor binds, how ligands are processed and where cells encounter them. B-cell receptors can recognize native molecular structures, while most conventional T-cell receptors recognize peptide–MHC complexes. Selection and context turn binding into an organized response.

The five topics in this unit approach a common problem from different levels of explanation. They concern **binding versus signaling; peptide processing routes; MHC polymorphism; costimulation and tolerance; receptor diversity**. By the end, explain the core mechanism for each topic, identify at least two plausible alternative explanations for a measured signal, reproduce the arithmetic in five cases, and describe what data would actually falsify a claim. Separate the event being *detected* from the downstream consequence inferred from that event. In immunology, an increase in a reporter, a cytokine, a cell percentage or antibody binding often looks persuasive but rarely establishes host protection by itself.

A useful immune-system model declares its spatial scale, the biological unit and the time horizon. A molecule can bind within seconds, a cell may alter transcription over hours, a clone expands across days, and tissue structure or population immunity changes across longer periods. Measured concentrations cannot be substituted for cell numbers, and cell numbers cannot replace measurements of functional killing, pathogen burden or tissue function. Check whether a figure uses proportions of all live cells, proportions within a selected gate, copies per milliliter, fluorescence units or an actual physical rate. The denominator is part of the scientific claim.

## Evidence and responsible interpretation

An immune response depends on anatomical compartment and previous exposure. Blood samples provide valuable, accessible information but can miss tissue-resident populations and localized mediator gradients. Bulk averages hide rare cell populations and interactions. Healthy versus diseased comparisons can confound cause and consequence, while an intervention that changes two pathways at once may not isolate either one. For quantitative work, preserve raw counts, clarify calibration, distinguish independent donors from repeated technical wells, and describe measurement error separately from biological variation.

All activities in this unit are computational, synthetic-data or abstract analysis exercises. Do not culture pathogens, perform human or animal exposure experiments, or attempt clinical assays on personal samples from these pages. Appropriate institutional biosafety and ethics review are prerequisites for any real laboratory research. These pages never prescribe immunization, diagnosis or treatment.


## Topic 3.1 — Antigen, epitope and molecular specificity

### Biological mechanism

An antigen can contain multiple epitopes recognized by different receptors. Antibody epitopes may be linear or conformational and often depend on accessible folded surfaces; conventional T-cell epitopes involve processed peptides displayed with MHC. Binding strength, receptor density and epitope accessibility together influence whether engagement becomes measurable.

### Why a plausible explanation can fail

Affinity describes an interaction under defined conditions, while avidity reflects combined interactions in multivalent contexts. A strong biochemical interaction does not necessarily produce efficient neutralization. A receptor can cross-react with chemically related ligands, and mutation can change presentation without altering protein abundance.

To challenge this account, use the related concept **peptide processing routes** to propose a different route to the same observation. Which intermediate biological step would make the two hypotheses diverge?

### Designing an informative measurement

Compare binding curves for a native folded protein and a denatured preparation using a hypothetical fluorescent antibody. Include matched concentration and nonspecific binding controls. Fit a binding model only within the assumptions of equilibrium, single-site behavior and a stable ligand concentration.

Define a control that separates assay background from biological mechanism. Sample before, during and after the expected response, and identify a second measurement that would corroborate the proposed pathway.

### Boundaries and counterexamples

An apparent dissociation constant from a cell surface assay may incorporate rebinding, multivalency and transport limitation. Do not equate it with an intrinsic solution-phase molecular constant.

Construct a counterexample where the measured signal changes without the proposed mechanism changing. Prioritize one alternative and choose an observation that would refute it.

### Quantitative worked case 3.1

**Problem.** A receptor occupancy proxy is 0.25 at low ligand and 0.75 at high ligand. Find difference in percentage points.

**Hypothetical inputs:** high = 0.75, low = 0.25. **Relation:** `(high-low)*100`. **Answer:** **50 percentage points**. Recompute independently and identify the physical or assay denominator, including the time interval where applicable.

**Interpretation:** Absolute difference between proportions differs from relative fold change. **Scope limit:** Binding does not imply effective downstream signaling. These invented inputs offer no independent biological replicates or measured variance. Change an input by 20 percent, repeat the calculation and identify one mechanism that could break the simplified assumption.

### Applying and challenging the concept

Prepare a two-column evidence ledger on **binding versus signaling**: direct observations versus explanatory assumptions. Draw a causal network for **antigen, epitope and molecular specificity** with one feedback edge. State how a null result could reflect either a false hypothesis or inadequate sampling.


## Topic 3.2 — Antigen uptake and MHC class II presentation

### Biological mechanism

Professional antigen-presenting cells can internalize extracellular proteins into endosomal compartments, where proteolysis generates peptides. MHC class II molecules assemble with chaperone assistance and load suitable peptides for presentation mainly to CD4 T cells. The peptide repertoire depends on processing conditions and MHC molecular properties.

### Why a plausible explanation can fail

More antigen uptake does not guarantee stronger T-cell activation; overdigestion can remove epitopes, and inadequate costimulatory signals can change response quality. B cells efficiently internalize material recognized by their antigen receptor, allowing focused presentation of linked peptides to helper cells.

To challenge this account, use the related concept **MHC polymorphism** to propose a different route to the same observation. Which intermediate biological step would make the two hypotheses diverge?

### Designing an informative measurement

In a hypothetical comparison of antigen doses, record an MHC-II–peptide proxy and a separate CD4-cell activation readout. A change in T-cell activation that exceeds changes in peptide display points toward additional signaling differences, not necessarily better antigen processing.

Define a control that separates assay background from biological mechanism. Sample before, during and after the expected response, and identify a second measurement that would corroborate the proposed pathway.

### Boundaries and counterexamples

Most MHC-II presentation involves exogenous material but exceptions exist; this classification is not an absolute rule for every intracellular antigen. General fluorescence from antigen uptake is not a direct measurement of peptide–MHC occupancy.

Construct a counterexample where the measured signal changes without the proposed mechanism changing. Prioritize one alternative and choose an observation that would refute it.

### Quantitative worked case 3.2

**Problem.** In hypothetical endosomal processing, 14 peptide complexes are counted per 70 tracked cells. Compute mean complexes/cell.

**Hypothetical inputs:** complexes = 14, cells = 70. **Relation:** `complexes/cells`. **Answer:** **0.2 complexes/cell**. Recompute independently and identify the physical or assay denominator, including the time interval where applicable.

**Interpretation:** A mean conceals cell-to-cell differences and detection limits. **Scope limit:** Not a real MHC occupancy estimate. These invented inputs offer no independent biological replicates or measured variance. Change an input by 20 percent, repeat the calculation and identify one mechanism that could break the simplified assumption.

### Applying and challenging the concept

Prepare a two-column evidence ledger on **peptide processing routes**: direct observations versus explanatory assumptions. Draw a causal network for **antigen uptake and mhc class ii presentation** with one feedback edge. State how a null result could reflect either a false hypothesis or inadequate sampling.


## Topic 3.3 — Proteasomal processing and MHC class I

### Biological mechanism

Intracellular proteins are degraded into peptide fragments, some of which enter the endoplasmic reticulum through transport machinery to associate with MHC class I molecules. MHC-I presentation lets CD8 T cells survey peptides reflecting intracellular protein content. Processing, peptide availability and quality-control steps all influence which complexes reach the surface.

### Why a plausible explanation can fail

A protein can be abundant yet poorly represented in the MHC-I peptide repertoire. The presented fragment may be short-lived, and changes in protein turnover can affect antigen presentation independently of transcription. Some specialized dendritic cells also cross-present extracellular material on MHC-I.

To challenge this account, use the related concept **costimulation and tolerance** to propose a different route to the same observation. Which intermediate biological step would make the two hypotheses diverge?

### Designing an informative measurement

Imagine measuring protein abundance, peptide–MHC display and CD8 reporter activation in parallel after a harmless inducible protein pulse. If protein increases while display does not, consider processing and trafficking as well as receptor recognition.

Define a control that separates assay background from biological mechanism. Sample before, during and after the expected response, and identify a second measurement that would corroborate the proposed pathway.

### Boundaries and counterexamples

Bulk MHC-I staining reports total surface expression, not the number of complexes containing one named peptide. Peptide recognition is MHC restricted, so an assay using incompatible MHC alleles is not an interpretable negative test.

Construct a counterexample where the measured signal changes without the proposed mechanism changing. Prioritize one alternative and choose an observation that would refute it.

### Quantitative worked case 3.3

**Problem.** A mock peptide-display assay counts 90 positive cells out of 600. Find the positive percentage.

**Hypothetical inputs:** positive = 90, total = 600. **Relation:** `positive/total*100`. **Answer:** **15 %**. Recompute independently and identify the physical or assay denominator, including the time interval where applicable.

**Interpretation:** MHC peptide display varies across cells and alleles. **Scope limit:** A reporter threshold may miss weak but functionally important complexes. These invented inputs offer no independent biological replicates or measured variance. Change an input by 20 percent, repeat the calculation and identify one mechanism that could break the simplified assumption.

### Applying and challenging the concept

Prepare a two-column evidence ledger on **MHC polymorphism**: direct observations versus explanatory assumptions. Draw a causal network for **proteasomal processing and mhc class i** with one feedback edge. State how a null result could reflect either a false hypothesis or inadequate sampling.


## Topic 3.4 — Costimulation, inhibitory signals and context

### Biological mechanism

Naive T-cell activation typically integrates T-cell receptor signaling with costimulatory molecules and cytokine context supplied by antigen-presenting cells. CD28-family and other pathways affect survival, proliferation and differentiation; inhibitory receptors can reduce or reshape activation. The balance varies with cell state and prior activation history.

### Why a plausible explanation can fail

An antigen-specific T cell may receive a strong receptor signal yet fail to develop a sustained effector response if appropriate supporting signals are absent. Conversely, inflammation can alter costimulation without changing antigen quantity. Negative regulation is a protective feature and not always an obstacle to be overridden.

To challenge this account, use the related concept **receptor diversity** to propose a different route to the same observation. Which intermediate biological step would make the two hypotheses diverge?

### Designing an informative measurement

Compare a hypothetical factorial design crossing antigen strength and costimulatory intensity. Interpret whether the factors interact on a defined outcome scale. A change in division number alone does not identify cytokine secretion, functional killing or durable memory.

Define a control that separates assay background from biological mechanism. Sample before, during and after the expected response, and identify a second measurement that would corroborate the proposed pathway.

### Boundaries and counterexamples

No single receptor is a universal on/off switch across tissues and disease states. Clinical checkpoint modulation is complex, has significant risks and is outside this educational model.

Construct a counterexample where the measured signal changes without the proposed mechanism changing. Prioritize one alternative and choose an observation that would refute it.

### Quantitative worked case 3.4

**Problem.** A factorial toy assay gives 6 units without costimulation and 18 with costimulation. Find fold effect at fixed antigen.

**Hypothetical inputs:** with_co = 18, without_co = 6. **Relation:** `with_co/without_co`. **Answer:** **3 fold**. Recompute independently and identify the physical or assay denominator, including the time interval where applicable.

**Interpretation:** Holding antigen fixed helps attribute changes to the second factor. **Scope limit:** Cell survival or composition could still drive the result. These invented inputs offer no independent biological replicates or measured variance. Change an input by 20 percent, repeat the calculation and identify one mechanism that could break the simplified assumption.

### Applying and challenging the concept

Prepare a two-column evidence ledger on **costimulation and tolerance**: direct observations versus explanatory assumptions. Draw a causal network for **costimulation, inhibitory signals and context** with one feedback edge. State how a null result could reflect either a false hypothesis or inadequate sampling.


## Topic 3.5 — Receptor gene rearrangement and clonal repertoires

### Biological mechanism

Developing B and T lymphocytes generate diverse antigen receptors by rearranging V, D and J gene segments where appropriate, with additional diversity at junctions and from chain pairing. Quality-control processes shape which receptors survive development. In B cells, subsequent germinal-center processes can further diversify antibodies through somatic hypermutation.

### Why a plausible explanation can fail

A theoretical number of possible receptors is not the same as the number physically present in one person. Cells are lost, selected, expanded and unevenly distributed across tissues. Sequencing an expanded clone does not prove that its antigen has been identified.

To challenge this account, use the related concept **binding versus signaling** to propose a different route to the same observation. Which intermediate biological step would make the two hypotheses diverge?

### Designing an informative measurement

Use a toy repertoire of many unique identifiers and sample it repeatedly to demonstrate that rare clones may be missed. Compare Simpson diversity with simple richness and examine how unequal clone frequencies affect both. State whether reads reflect molecules or corrected cell counts.

Define a control that separates assay background from biological mechanism. Sample before, during and after the expected response, and identify a second measurement that would corroborate the proposed pathway.

### Boundaries and counterexamples

Raw sequence diversity depends on sampling depth, amplification bias and receptor assembly decisions. It should never be used alone to declare immune competence or to diagnose disease.

Construct a counterexample where the measured signal changes without the proposed mechanism changing. Prioritize one alternative and choose an observation that would refute it.

### Quantitative worked case 3.5

**Problem.** A toy repertoire has clone probabilities 0.5, 0.3, 0.2. Compute Simpson diversity 1 minus sum of squared probabilities.

**Hypothetical inputs:** p1 = 0.5, p2 = 0.3, p3 = 0.2. **Relation:** `1-(p1*p1+p2*p2+p3*p3)`. **Answer:** **0.62 index**. Recompute independently and identify the physical or assay denominator, including the time interval where applicable.

**Interpretation:** An even repertoire has a greater diversity index for a fixed number of clones. **Scope limit:** This estimate ignores unobserved rare clones. These invented inputs offer no independent biological replicates or measured variance. Change an input by 20 percent, repeat the calculation and identify one mechanism that could break the simplified assumption.

### Applying and challenging the concept

Prepare a two-column evidence ledger on **receptor diversity**: direct observations versus explanatory assumptions. Draw a causal network for **receptor gene rearrangement and clonal repertoires** with one feedback edge. State how a null result could reflect either a false hypothesis or inadequate sampling.


## Integrated computational investigation — Presentation intensity versus T-cell activation

### Question and rival explanations

Two samples display comparable bulk MHC yet recruit different numbers of antigen-specific T cells. What must be distinguished?

**Mechanistic hypothesis A:** The specific displayed peptide fraction differs.

**Mechanistic hypothesis B:** Costimulatory context rather than peptide display differs.

The challenge is not to select the explanation that seems familiar. First articulate the different predictions each account makes under a condition that would actually distinguish them. A mechanism might predict an early localized signal, whereas an alternative predicts a later population effect; both can reproduce the same final bulk number. Construct a causal diagram with the stimulus, intermediate state, assay output and at least one unmeasured covariate. Mark which relations are observed and which require assumptions. The invented numbers below are practice material only: no patients, animals, pathogen samples or laboratory measurements generated them.

### Research design

Use an abstract factorial dataset of peptide–MHC occupancy proxy and costimulation, then calculate predicted responding fractions; a peptide-specific reporter is distinguished from total MHC surface stain.

**Principal confound:** Variability in T-cell receptor repertoire and baseline viability can create differences without changing antigen presentation..

A study needs biological units that match the hypothesis. If all measurements come from one culture vessel, 50 images represent subsampling of that vessel, not 50 independent cultures. If hundreds of cells come from one donor, those cells cannot support donor-level generalization without a design that accounts for clustering. Predefine the primary comparison, effect direction, main covariates and quality exclusions. Calibrate instruments or report uncalibrated arbitrary units explicitly, and store the untouched data before plotting or normalization. Use safe computational methods for these classroom tasks; any real specimen acquisition requires proper authorization, ethics and biosafety oversight.

### Constructed series (not research data)

| Stage / sample index | Series A (invented) | Series B (invented) |
|---:|---:|---:|
| 0 | 2 | 2 |
| 1 | 4 | 2.5 |
| 2 | 7 | 3 |
| 3 | 8 | 5 |
| 4 | 9 | 7 |

Series A changes by **7** display units across the five stages; series B changes by **5**. Its endpoint ratio is **0.7778** if the chosen scales are comparable; if the assays do not share a scale, that arithmetic is only a display ratio and has no biological interpretation. Compute each sequence's initial-to-final proportional change separately. Plot the two curves, label axis units or 'arbitrary teaching index', and add no error bars: the dataset supplies no independent replicate variation. Do not invent significance levels, biological confidence intervals or citations to make synthetic observations appear empirical.

### Interpretation and identification

The first series saturates earlier than the second; without a shared and defined assay calibration their heights cannot be compared as T-cell counts. The most important next step is to specify a discriminating measurement. A time course is better than a single endpoint when mechanisms have distinct delays, but unobserved confounding remains possible. A targeted perturbation can improve causal identification, provided it does not independently change the outcome through a second mechanism. Some data would make both hypotheses less plausible; identify such a result explicitly. The final answer should distinguish the direction of the constructed numbers, the mechanism proposed to explain them, and the missing evidence needed for a real biological conclusion.

### Structured analysis assignment

1. Write both hypotheses as falsifiable predictions for one named assay and an explicit time window.
2. State whether the sample unit is a donor, animal, organ, culture vessel or cell; explain why technical repetitions cannot silently increase biological sample size.
3. Quantify the endpoint and one interval rate, explaining any limitations due to missing time units.
4. Identify two alternative causes of the same observed trajectory, including the principal confound listed above.
5. Propose a safe, noninfectious follow-up or computational analysis and choose a criterion that would change your preferred explanation.
6. Produce a short reproducibility note giving data schema, graph labels, analysis pseudocode and a statement that all values are fictional.


## Systems synthesis and examination preparation

An immune network changes across compartments and timescales. This unit links **Antigen, epitope and molecular specificity**, **Antigen uptake and MHC class II presentation**, **Proteasomal processing and MHC class I**, **Costimulation, inhibitory signals and context** and **Receptor gene rearrangement and clonal repertoires**. Try placing these concepts in a table with columns for recognition, cellular actors, immediate output, delayed outcome, negative regulation and an assay limitation. Some rows will not fit neatly: the same mediator may promote clearance and also exacerbate injury. Treat that apparent contradiction as a clue about concentrations, timing and tissue specificity rather than a reason to ignore the mechanism.

To test integration, imagine two specimens showing the same final reporter value despite different early trajectories. In one, a small number of strongly responding cells drive the signal; in the other, a large number of weakly responding cells produce an equal bulk total. A single bulk assay cannot resolve those explanations. Which of this unit's five mechanisms could generate the two situations, and what independent measurement would discriminate them? For every proposed measurement, identify whether it estimates a concentration, frequency, absolute count, location, phenotype or function. Then articulate the assumption that makes the measurement relevant.

Transfer the explanation from a controlled cell system into an intact tissue. Tissue oxygen, access to antigen, migration routes and regulatory signals could all change the qualitative outcome even if receptor-level biochemistry remains the same. Do not silently treat a monotonic curve as an empirical law valid across species, tissues and developmental stages. If you use the interactive model, name one omitted interaction and describe how including it might shift the curve, introduce a delay, or reverse the predicted comparison. Sensitivity to an assumed parameter is useful for learning but cannot establish that the chosen parameter value matches biology.

### End-of-unit synthesis questions

- Use **antigen, epitope and molecular specificity** and **receptor gene rearrangement and clonal repertoires** in one causal argument and identify where negative feedback could intervene.
- Present a competing hypothesis for a result initially attributed to **proteasomal processing and mhc class i**. What measurement, with units, would favor one explanation?
- Explain how an apparent change in immune-cell frequency might arise with no change in absolute abundance of that population.
- Recompute one quantitative case with different assumptions and report which assumption contributes most to uncertainty.
- Choose a claim that would be dangerous to generalize into patient advice and explain why the available educational model cannot justify it.

**Editorial reminder:** The described scenarios are concept exercises, not real laboratory results. All clinical statements require authoritative evidence and, where applicable, qualified professional interpretation.
