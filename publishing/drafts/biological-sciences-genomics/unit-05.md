# Unit 05 — Regulatory and functional genomics

> **OpenSTEM Genomics · Book 16 · Editorial teaching draft.** All worked case data and investigations are synthetic. The interactive models describe simplified mathematical relations, not diagnoses or empirical genomic claims.

## Central scientific question

**Which genomic elements affect cell behavior, and under what context?**

### Conceptual context and how the five lessons fit

Genomic sequence helps construct regulatory mechanisms only when combined with cell-specific functional evidence. A DNA motif may be compatible with transcription-factor recognition, but whether binding occurs depends on cellular protein abundance, chromatin state and other interactions. Similarly, a physical contact enriched in a chromosome-conformation assay does not by itself prove enhancer action. This unit layers enhancer hypotheses, open chromatin, sequence motifs, three-dimensional structure and regulatory associations. The common lesson is that different assays measure related but nonidentical quantities; triangulating independent measurements strengthens explanations, while selectively picking a striking track can create false mechanistic certainty.

### A running case to reason through

A regulatory signal is stronger after stimulation, but the linked gene does not change expression in every cell type. The proposed explanation should remain a working hypothesis until both the measurement process and alternative biological accounts have been examined. Identify a plausible negative control, a sample identity verification and a condition in which the preferred model might fail. A final plot can be numerically precise while its biological conclusion is uncertain; your task is to make that uncertainty visible rather than treating it as a defect.

### Unit learning objectives

By the end of this unit, you should be able to reconstruct the data assumptions behind each of the five main topics, reproduce their toy calculations, distinguish technical and biological replication, identify a rival explanation for an apparent signal, and propose an independent measurement that would strengthen or challenge the inference. For each numerical answer, know the denominator, its unit and the simplifications required. Give yourself permission to conclude "not established" when appropriate.

### Study route

Read the five lessons in order. Each starts with an operational definition, moves through a fictional case and a worked calculation, then challenges the tempting inference. Compute the numbers by hand before using code. Finish with the unit capstone and the interactive model questions. Learning genomics requires deciding which questions an assay can answer at least as much as mastering the associated algorithm.

---

## Lesson 5.1 — Enhancers, promoters and cis regulation

### Mechanism and what can be inferred

Enhancers may regulate promoters over genomic distance through context-specific protein complexes and chromatin contacts. Sequence motif presence alone does not prove binding or regulatory effect. Identify the physical material, the instrument observation and the computational summary separately. This prevents a dataset label from being mistaken for the underlying biological process. The central question is **Which genomic elements affect cell behavior, and under what context?** Interpret that question in the limited context of the named species, specimens and assay; do not extrapolate from one sequence representation to all individuals.

### Measurement contract and analytical method

Integrate candidate enhancer sequence, accessibility, histone-mark patterns, target-gene expression and perturbation evidence while recording cell type and developmental stage. Reconstruct the reasoning as an evidence ledger with separate columns for raw measurement, model choice, calculated value, alternative explanation and validation status. Avoid merging uncertain evidence into one unexplained confidence label. When comparing results, include the reference assembly or database release, observation level, quality thresholds, removed records and a denominator for each proportion. Missing genomic measurements are not synonymous with confidently absent biological events. Explain which parts of the pipeline are deterministic transformations and which rely on empirical model assumptions.

### Fictional case and competing explanation

A fictional neuronal enhancer becomes accessible during differentiation, but a nearby housekeeping gene stays constant; proximity is not sufficient to assign the target. This is a hypothetical instructional case, not a reported finding. Begin with one biological hypothesis and one technical or sampling rival. Before choosing the most interesting interpretation, write down what each hypothesis predicts about a newly collected specimen or orthogonal assay. Different algorithms may agree because they reuse the same flawed reference or measurement, not because they supply independent experimental confirmation.

### Worked example with units

**Problem:** If 60 of 240 candidate intervals overlap a specified accessibility peak set, overlap proportion is 25%; this is not evidence that all sixty regulate transcription.

**Calculation:** `60/240*100` = **25 %** for the invented inputs. Check the unit, sign, scale and rounding of the calculated answer. Where a proportion is involved, state whether the result counts reads, alleles, individuals, transcripts, genomic sites or publications; those denominators are not interchangeable. Correct arithmetic validates a calculation, but it does not establish that the input data are representative or that the result has a causal meaning. Record whether the denominator counts bases, reads, allele copies, individuals, loci or experimental runs. Recompute with a modified hypothetical input to examine numerical sensitivity.

### Error modes and validation design

Assuming the nearest gene is the regulatory target can fail when contacts cross other genes or chromatin contexts change. If the measurement was duplicated at the technical level, name the correct independent sampling level before offering any significance claim. Replication improves confidence only to the extent that it samples the relevant biological variability. **Audit emphasis — Inspect the mechanism.** Link the measured molecular signal to a plausible process and identify where the causal arrow is merely assumed. Correlated regulatory, evolutionary or clinical features can have shared upstream causes.

Test several proposed targets using orthogonal evidence and compare expression or chromatin changes after a well-controlled regulatory perturbation. The proposed new evidence should help discriminate between mechanisms rather than merely producing another version of the same computational score. Explain the important negative control and a result that would weaken your preferred hypothesis. In a scientific report, keep measurements, computed statistics, model-based predictions and proposed biological explanations in separate statements.

### Transfer exercise

Connect **Enhancers, promoters and cis regulation** with **Chromatin accessibility and nucleosome positioning**. Explain which source-data error would contaminate both topics and how a reference-aware provenance record would reveal it. Then answer: What was measured? How was the statistic calculated? What competing explanation remains? What independent experiment would be most efficient? Present the final inference as a conditional claim whose strength matches the available evidence.

---

## Lesson 5.2 — Chromatin accessibility and nucleosome positioning

### Mechanism and what can be inferred

Nucleosome occupancy and chromatin accessibility change the probability that DNA-binding proteins interact with regulatory sequence. Accessibility assays also depend on enzyme bias, sequencing depth and cell composition. Identify the physical material, the instrument observation and the computational summary separately. This prevents a dataset label from being mistaken for the underlying biological process. The central question is **Which genomic elements affect cell behavior, and under what context?** Interpret that question in the limited context of the named species, specimens and assay; do not extrapolate from one sequence representation to all individuals.

### Measurement contract and analytical method

Normalize for library depth and compare replicates before calling differential accessibility. Inspect peak widths, mitochondrial-read fraction, transcription-start enrichment and experiment-specific quality measures. Create a tiny independent benchmark that contains an ordinary case, an ambiguous boundary case and a deliberately malformed record. Check not only output numbers but also whether the tool detects invalid assumptions and refuses silent corrections. When comparing results, include the reference assembly or database release, observation level, quality thresholds, removed records and a denominator for each proportion. Missing genomic measurements are not synonymous with confidently absent biological events. Explain which parts of the pipeline are deterministic transformations and which rely on empirical model assumptions.

### Fictional case and competing explanation

In invented cell samples, a stimulus produces twice the normalized signal at one enhancer while half the cells change state, raising a composition-confounding question. This is a hypothetical instructional case, not a reported finding. Begin with one biological hypothesis and one technical or sampling rival. Before choosing the most interesting interpretation, write down what each hypothesis predicts about a newly collected specimen or orthogonal assay. Different algorithms may agree because they reuse the same flawed reference or measurement, not because they supply independent experimental confirmation.

### Worked example with units

**Problem:** A peak with normalized 80 units after stimulus versus 40 before has a twofold ratio, or log2 fold change of 1, if measurement scales are comparable.

**Calculation:** `log2(80/40)` = **1 log2 fold** for the invented inputs. To test your interpretation, change one input within a plausible synthetic range and recompute the output. The goal is not to fit actual organisms but to understand how measurement assumptions propagate through the equation. Correct arithmetic validates a calculation, but it does not establish that the input data are representative or that the result has a causal meaning. Record whether the denominator counts bases, reads, allele copies, individuals, loci or experimental runs. Recompute with a modified hypothetical input to examine numerical sensitivity.

### Error modes and validation design

Bulk signal changes can result from altered proportions of cell types rather than a cell-intrinsic change at every cell. Consider whether the strongest-looking pattern comes from a feature selected after inspecting the answer. Exploratory selection followed by an unadjusted confirmatory claim can overstate reproducibility. **Audit emphasis — Protect the inferential boundary.** Separate an algorithmic score from a measurement and from an actionable interpretation. Showing that a model is internally consistent is not the same as validating its claims in a new cohort.

Compare matched purified cell populations or single-cell readouts and use spike-in or appropriate normalization when justified. The proposed new evidence should help discriminate between mechanisms rather than merely producing another version of the same computational score. Explain the important negative control and a result that would weaken your preferred hypothesis. In a scientific report, keep measurements, computed statistics, model-based predictions and proposed biological explanations in separate statements.

### Transfer exercise

Connect **Chromatin accessibility and nucleosome positioning** with **Transcription-factor binding and motif models**. Explain which source-data error would contaminate both topics and how a reference-aware provenance record would reveal it. Then answer: What was measured? How was the statistic calculated? What competing explanation remains? What independent experiment would be most efficient? Present the final inference as a conditional claim whose strength matches the available evidence.

---

## Lesson 5.3 — Transcription-factor binding and motif models

### Mechanism and what can be inferred

A transcription factor binds DNA according to affinity, concentration, chromatin accessibility and cofactors. Position-weight motifs summarize preferences but do not guarantee occupancy in a cell. Identify the physical material, the instrument observation and the computational summary separately. This prevents a dataset label from being mistaken for the underlying biological process. The central question is **Which genomic elements affect cell behavior, and under what context?** Interpret that question in the limited context of the named species, specimens and assay; do not extrapolate from one sequence representation to all individuals.

### Measurement contract and analytical method

Combine motif scanning with expression and direct binding evidence where available; correct for sequence-composition biases and search-space size when interpreting enrichment. For a transparent analysis, make two small tables: one describing source specimens and assays, and another describing computational transformations. The join keys should let another investigator trace a number back to its input without revealing restricted personal information. When comparing results, include the reference assembly or database release, observation level, quality thresholds, removed records and a denominator for each proportion. Missing genomic measurements are not synonymous with confidently absent biological events. Explain which parts of the pipeline are deterministic transformations and which rely on empirical model assumptions.

### Fictional case and competing explanation

An imaginary motif appears in 18% of accessible regions and 12% of matched control sequences, suggesting enrichment but not identifying which cell proteins actually bind it. This is a hypothetical instructional case, not a reported finding. Begin with one biological hypothesis and one technical or sampling rival. Before choosing the most interesting interpretation, write down what each hypothesis predicts about a newly collected specimen or orthogonal assay. Different algorithms may agree because they reuse the same flawed reference or measurement, not because they supply independent experimental confirmation.

### Worked example with units

**Problem:** Enrichment ratio 0.18/0.12 equals 1.5; the absolute difference is six percentage points, not a 50-percentage-point increase.

**Calculation:** `0.18/0.12` = **1.5 enrichment ratio** for the invented inputs. Check the unit, sign, scale and rounding of the calculated answer. Where a proportion is involved, state whether the result counts reads, alleles, individuals, transcripts, genomic sites or publications; those denominators are not interchangeable. Correct arithmetic validates a calculation, but it does not establish that the input data are representative or that the result has a causal meaning. Record whether the denominator counts bases, reads, allele copies, individuals, loci or experimental runs. Recompute with a modified hypothetical input to examine numerical sensitivity.

### Error modes and validation design

A statistically enriched short motif can occur by chance or be bound by multiple proteins from the same family. Explain how an earlier-stage error could propagate through several downstream analyses and create apparently consistent output. Correlation among derived reports should never substitute for documented source integrity. **Audit emphasis — Check the sensitivity.** Vary a defensible parameter—filter threshold, reference representation, cohort subset or matching rule—and report whether your conclusion changes. Sensitivity is information about model dependence, not a reason to hide uncertain results.

Repeat enrichment against GC-matched controls and examine an independent binding assay or perturbation for a candidate factor. The proposed new evidence should help discriminate between mechanisms rather than merely producing another version of the same computational score. Explain the important negative control and a result that would weaken your preferred hypothesis. In a scientific report, keep measurements, computed statistics, model-based predictions and proposed biological explanations in separate statements.

### Transfer exercise

Connect **Transcription-factor binding and motif models** with **Three-dimensional genome organization**. Explain which source-data error would contaminate both topics and how a reference-aware provenance record would reveal it. Then answer: What was measured? How was the statistic calculated? What competing explanation remains? What independent experiment would be most efficient? Present the final inference as a conditional claim whose strength matches the available evidence.

---

## Lesson 5.4 — Three-dimensional genome organization

### Mechanism and what can be inferred

Chromosome territories, loops and domains summarize spatial contact probabilities, not a fixed folding diagram identical in every cell. Contact-count matrices are shaped by distance decay and assay-specific biases. Identify the physical material, the instrument observation and the computational summary separately. This prevents a dataset label from being mistaken for the underlying biological process. The central question is **Which genomic elements affect cell behavior, and under what context?** Interpret that question in the limited context of the named species, specimens and assay; do not extrapolate from one sequence representation to all individuals.

### Measurement contract and analytical method

Balance contact maps appropriately, compare replicates and state resolution. Distinguish an enriched pairwise contact from causal regulation and avoid interpreting heat-map brightness without normalization. Preregister an analysis comparison in plain language: what signal is sought, which confounders are anticipated, how filtering will work, which readouts matter, and what observation would count against the favored interpretation. When comparing results, include the reference assembly or database release, observation level, quality thresholds, removed records and a denominator for each proportion. Missing genomic measurements are not synonymous with confidently absent biological events. Explain which parts of the pipeline are deterministic transformations and which rely on empirical model assumptions.

### Fictional case and competing explanation

A synthetic contact map appears to strengthen a domain boundary after differentiation, but the same samples differ substantially in cell-cycle composition. This is a hypothetical instructional case, not a reported finding. Begin with one biological hypothesis and one technical or sampling rival. Before choosing the most interesting interpretation, write down what each hypothesis predicts about a newly collected specimen or orthogonal assay. Different algorithms may agree because they reuse the same flawed reference or measurement, not because they supply independent experimental confirmation.

### Worked example with units

**Problem:** If an observed contact count is 90 and matched expectation is 30, observed/expected is 3, conditional on how expectation was estimated.

**Calculation:** `90/30` = **3 observed/expected** for the invented inputs. To test your interpretation, change one input within a plausible synthetic range and recompute the output. The goal is not to fit actual organisms but to understand how measurement assumptions propagate through the equation. Correct arithmetic validates a calculation, but it does not establish that the input data are representative or that the result has a causal meaning. Record whether the denominator counts bases, reads, allele copies, individuals, loci or experimental runs. Recompute with a modified hypothetical input to examine numerical sensitivity.

### Error modes and validation design

Resolution and depth limit whether a feature is detectable; visually sharp squares in smoothed maps may be artifacts. Ask which alternative assay or independent group could challenge the finding. Repeating a computation under different colors or with another software package is not independent biological replication. **Audit emphasis — Design a contrast.** Specify at least one plausible nonbiological explanation and predict which extra measurement would expose it. Negative controls and orthogonal data are often more informative than adding another correlated software score.

Repeat analysis at coarser bin sizes, test reproducibility and relate putative contacts to independent regulatory measurements. The proposed new evidence should help discriminate between mechanisms rather than merely producing another version of the same computational score. Explain the important negative control and a result that would weaken your preferred hypothesis. In a scientific report, keep measurements, computed statistics, model-based predictions and proposed biological explanations in separate statements.

### Transfer exercise

Connect **Three-dimensional genome organization** with **Expression QTLs and integrated regulatory evidence**. Explain which source-data error would contaminate both topics and how a reference-aware provenance record would reveal it. Then answer: What was measured? How was the statistic calculated? What competing explanation remains? What independent experiment would be most efficient? Present the final inference as a conditional claim whose strength matches the available evidence.

---

## Lesson 5.5 — Expression QTLs and integrated regulatory evidence

### Mechanism and what can be inferred

An expression quantitative trait locus is a statistical association between genetic variation and transcript abundance; linked markers, confounding and allelic heterogeneity complicate claims about causal variants. Identify the physical material, the instrument observation and the computational summary separately. This prevents a dataset label from being mistaken for the underlying biological process. The central question is **Which genomic elements affect cell behavior, and under what context?** Interpret that question in the limited context of the named species, specimens and assay; do not extrapolate from one sequence representation to all individuals.

### Measurement contract and analytical method

Model population structure and measured covariates, handle multiple tests and check tissue specificity. Compare eQTL, GWAS and colocalization claims under explicitly documented assumptions. Write a data dictionary before invoking a tool. It should specify permitted values, missing-data codes, identity keys, coordinate conventions, and a worked input-output example whose result can be checked without proprietary software. When comparing results, include the reference assembly or database release, observation level, quality thresholds, removed records and a denominator for each proportion. Missing genomic measurements are not synonymous with confidently absent biological events. Explain which parts of the pipeline are deterministic transformations and which rely on empirical model assumptions.

### Fictional case and competing explanation

A fictional cis-eQTL near a metabolic gene appears only in leaf tissue, while phenotype association is observed in the whole plant. This is a hypothetical instructional case, not a reported finding. Begin with one biological hypothesis and one technical or sampling rival. Before choosing the most interesting interpretation, write down what each hypothesis predicts about a newly collected specimen or orthogonal assay. Different algorithms may agree because they reuse the same flawed reference or measurement, not because they supply independent experimental confirmation.

### Worked example with units

**Problem:** In 100 tests with 8 nominal p-values below 0.05, nominal discovery fraction is 8%; this alone says nothing about the false discovery rate.

**Calculation:** `8/100*100` = **8 %** for the invented inputs. Check the unit, sign, scale and rounding of the calculated answer. Where a proportion is involved, state whether the result counts reads, alleles, individuals, transcripts, genomic sites or publications; those denominators are not interchangeable. Correct arithmetic validates a calculation, but it does not establish that the input data are representative or that the result has a causal meaning. Record whether the denominator counts bases, reads, allele copies, individuals, loci or experimental runs. Recompute with a modified hypothetical input to examine numerical sensitivity.

### Error modes and validation design

Two signals that overlap physically need not share a causal variant; colocalization itself depends on priors and regional variant coverage. If the measurement was duplicated at the technical level, name the correct independent sampling level before offering any significance claim. Replication improves confidence only to the extent that it samples the relevant biological variability. **Audit emphasis — Begin with the denominator.** First write the total that would make a reported fraction equal to one: all molecules, all individuals, all reference positions or all interrogated loci. A percentage cannot be compared across studies if the denominators are inconsistent.

Perform conditional analyses and check whether fine-mapping credible sets overlap with consistent direction across relevant tissues. The proposed new evidence should help discriminate between mechanisms rather than merely producing another version of the same computational score. Explain the important negative control and a result that would weaken your preferred hypothesis. In a scientific report, keep measurements, computed statistics, model-based predictions and proposed biological explanations in separate statements.

### Transfer exercise

Connect **Expression QTLs and integrated regulatory evidence** with **Three-dimensional genome organization**. Explain which source-data error would contaminate both topics and how a reference-aware provenance record would reveal it. Then answer: What was measured? How was the statistic calculated? What competing explanation remains? What independent experiment would be most efficient? Present the final inference as a conditional claim whose strength matches the available evidence.

---

## Unit 05 capstone — Connecting a regulatory element to a candidate target

### Situation and materials

A synthetic cell model shows increased accessibility at a distant enhancer-like region, a modest transcription change and an ambiguous chromatin contact to two genes. Assume all records are fabricated for the classroom. Start by listing the observational units: organism, donor, biological preparation, technical library, genomic site or algorithmic summary. This is a crucial step because denominator mistakes can produce a result that is mathematically correct but scientifically misleading. Fix the reference and analysis version for the exercise before comparing any numbers, and include unknowns explicitly.

### Procedure and minimum outputs

Construct a directed graph marking sequence, accessibility, protein occupancy, spatial proximity and expression as distinct measurements. Record which arrows are mechanistic hypotheses rather than directly observed links. Your calculations need not be complicated. They should be completely reproducible, with input values, a visible formula, arithmetic and units. Create one well-documented table for the observations, a second for transformations, and a third for which interpretations survive each quality check. Explain the transformations in words rather than copying a tool output without explanation. Before choosing a cutoff, describe the costs of false positive and false negative findings in this particular fictional study.

### Competing hypotheses and sensitivity experiment

Propose a perturbation and an orthogonal validation that would discriminate between the two candidate targets. Recompute a fold change and explain how changing cell-type composition could mimic it. Your favored explanation should generate a prediction that would be less likely under a clearly named alternative. Design one sensitivity exercise that changes a single assumption—such as callable regions, phase, ancestry strata, normalization rule or depth threshold—and track its effect on the main statistic. If the preferred interpretation changes, report that dependence rather than selecting the setting with the most dramatic result. Explain which new specimen, assay or observation would provide the best independent discrimination.

### Deliverables, reflection and peer review

Submit a preregistered hypothesis table, a bias checklist, and a cautious claim limited to the available evidence. In addition, prepare a reproducibility manifest with input identifiers, simulated-only status, calculations, method version and a short rationale for every excluded observation. Include a four-sentence abstract distinguishing what is measured, estimated, hypothesized and still unknown. Exchange reports with another learner, ask them to recalculate at least one statistic using only the supplied source data, and record one objection that improves the design. Do not describe any result as clinical, diagnostic or measured in the real world.

### Challenge questions for synthesis

1. Which dataset field would have the greatest impact if it were silently mislabeled? Identify a simple audit that could catch the mistake before modeling.
2. Does the unit's central conclusion rely on random sampling, correct genome representation, accurate molecular classification or independent replication? Rank those assumptions in importance for this case.
3. What result could falsify the leading explanation without proving every alternative? Discuss the distinction between rejection of one hypothesis and proof of another.
4. If your method produced a visually excellent plot from copied or confounded measurements, what independent check would you demand before publication?
5. Explain why the precise mathematical result alone does not certify the biological or social validity of the research conclusion.

---

## Two interactive teaching models

Change each slider, observe its graph and record which assumptions make the formula valid. These are hypothetical mathematical demonstrations, not empirical sequence analyses.

### Model 5.1: Regulatory signal log2 fold-change

**Equation:** log2FC=log2(after/40). **Caveat:** Scales must be comparable. Change the independent parameter, then explain whether the output change is a simple mathematical consequence or requires a biological inference. A monotone visual trend is not automatically a causal biological law. Identify the units and what is held constant.

### Model 5.2: Toy binding curve under mass action

**Equation:** θ=L/(Kd+L), Kd=25. **Caveat:** Not a TF binding inference from motif sequence. Change the independent parameter, then explain whether the output change is a simple mathematical consequence or requires a biological inference. A monotone visual trend is not automatically a causal biological law. Identify the units and what is held constant.
