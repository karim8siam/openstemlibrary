# Unit 08 — Single-cell, metagenomic and integrative genomics

> **OpenSTEM Genomics · Book 16 · Editorial teaching draft.** All worked case data and investigations are synthetic. The interactive models describe simplified mathematical relations, not diagnoses or empirical genomic claims.

## Central scientific question

**How can genomes be analyzed across cells, communities and measurement layers?**

### Conceptual context and how the five lessons fit

Modern genomics increasingly combines heterogenous measurements: DNA and RNA from individual cells, community DNA from environmental specimens, spatially indexed molecular signals and cross-platform molecular layers. These datasets have different denominators and incomplete observation processes. Large cell counts cannot compensate for a lack of independent donors, and a high relative abundance of one microbial taxon does not imply more absolute organisms. This unit focuses on careful measurement definitions, mixture artifacts, spatial resolution, multi-omic integration and reproducible pipelines. Its goal is to prepare learners to critique a glamorous integrated visualization by asking mundane, essential questions about identity, independence, filtering, transformation and uncertainty.

### A running case to reason through

A multicenter tissue and environmental study reports a dramatic difference that vanishes when technical batches are modeled. The proposed explanation should remain a working hypothesis until both the measurement process and alternative biological accounts have been examined. Identify a plausible negative control, a sample identity verification and a condition in which the preferred model might fail. A final plot can be numerically precise while its biological conclusion is uncertain; your task is to make that uncertainty visible rather than treating it as a defect.

### Unit learning objectives

By the end of this unit, you should be able to reconstruct the data assumptions behind each of the five main topics, reproduce their toy calculations, distinguish technical and biological replication, identify a rival explanation for an apparent signal, and propose an independent measurement that would strengthen or challenge the inference. For each numerical answer, know the denominator, its unit and the simplifications required. Give yourself permission to conclude "not established" when appropriate.

### Study route

Read the five lessons in order. Each starts with an operational definition, moves through a fictional case and a worked calculation, then challenges the tempting inference. Compute the numbers by hand before using code. Finish with the unit capstone and the interactive model questions. Learning genomics requires deciding which questions an assay can answer at least as much as mastering the associated algorithm.

---

## Lesson 8.1 — Single-cell genomes, sparsity and doublets

### Mechanism and what can be inferred

Single-cell assays can capture genomic or transcriptomic differences across cells, but sparse counts, capture losses and doublets can distort inferred cell populations. A cell barcode is not guaranteed to represent one intact cell. Identify the physical material, the instrument observation and the computational summary separately. This prevents a dataset label from being mistaken for the underlying biological process. The central question is **How can genomes be analyzed across cells, communities and measurement layers?** Interpret that question in the limited context of the named species, specimens and assay; do not extrapolate from one sequence representation to all individuals.

### Measurement contract and analytical method

Identify cells with quality checks, classify multiplets, track specimen and batch effects, and avoid using thousands of cells from one donor as thousands of independent biological donors. Create a tiny independent benchmark that contains an ordinary case, an ambiguous boundary case and a deliberately malformed record. Check not only output numbers but also whether the tool detects invalid assumptions and refuses silent corrections. When comparing results, include the reference assembly or database release, observation level, quality thresholds, removed records and a denominator for each proportion. Missing genomic measurements are not synonymous with confidently absent biological events. Explain which parts of the pipeline are deterministic transformations and which rely on empirical model assumptions.

### Fictional case and competing explanation

In an invented developmental study, 6,000 droplets are retained but 300 have features consistent with two cells, altering lineage-frequency estimates. This is a hypothetical instructional case, not a reported finding. Begin with one biological hypothesis and one technical or sampling rival. Before choosing the most interesting interpretation, write down what each hypothesis predicts about a newly collected specimen or orthogonal assay. Different algorithms may agree because they reuse the same flawed reference or measurement, not because they supply independent experimental confirmation.

### Worked example with units

**Problem:** Three hundred suspected doublets among 6,000 retained barcodes give a 5% flagged fraction, not a measured universal doublet probability.

**Calculation:** `300/6000*100` = **5 %** for the invented inputs. Make a small companion table with the original fictional inputs, one alternative input value, the new result and a sentence describing whether the qualitative conclusion survives. Correct arithmetic validates a calculation, but it does not establish that the input data are representative or that the result has a causal meaning. Record whether the denominator counts bases, reads, allele copies, individuals, loci or experimental runs. Recompute with a modified hypothetical input to examine numerical sensitivity.

### Error modes and validation design

Cell filtering can preferentially remove a biologically interesting fragile population; small cell-type clusters may also result from doublets or ambient molecules. Explain how an earlier-stage error could propagate through several downstream analyses and create apparently consistent output. Correlation among derived reports should never substitute for documented source integrity. **Audit emphasis — Test the missingness.** Identify which observations were never sampled, lost in preparation, removed by filters or assigned ambiguous labels. A blank value and a confident absence are fundamentally different statements.

Vary filtering thresholds, verify marker consistency and design replicate-donor analysis before reporting stable cell-type differences. The proposed new evidence should help discriminate between mechanisms rather than merely producing another version of the same computational score. Explain the important negative control and a result that would weaken your preferred hypothesis. In a scientific report, keep measurements, computed statistics, model-based predictions and proposed biological explanations in separate statements.

### Transfer exercise

Connect **Single-cell genomes, sparsity and doublets** with **Metagenomic assembly and community composition**. Explain which source-data error would contaminate both topics and how a reference-aware provenance record would reveal it. Then answer: What was measured? How was the statistic calculated? What competing explanation remains? What independent experiment would be most efficient? Present the final inference as a conditional claim whose strength matches the available evidence.

---

## Lesson 8.2 — Metagenomic assembly and community composition

### Mechanism and what can be inferred

Metagenomics analyzes genomic fragments from biological communities; abundance estimates depend on extraction, reference databases, mapping ambiguity and organism genome length. Relative abundance is compositional. Identify the physical material, the instrument observation and the computational summary separately. This prevents a dataset label from being mistaken for the underlying biological process. The central question is **How can genomes be analyzed across cells, communities and measurement layers?** Interpret that question in the limited context of the named species, specimens and assay; do not extrapolate from one sequence representation to all individuals.

### Measurement contract and analytical method

Include negative controls, read-classification uncertainty and reference coverage; distinguish taxon presence, DNA abundance and viable cell counts rather than collapsing all three into one statement. For a transparent analysis, make two small tables: one describing source specimens and assays, and another describing computational transformations. The join keys should let another investigator trace a number back to its input without revealing restricted personal information. When comparing results, include the reference assembly or database release, observation level, quality thresholds, removed records and a denominator for each proportion. Missing genomic measurements are not synonymous with confidently absent biological events. Explain which parts of the pipeline are deterministic transformations and which rely on empirical model assumptions.

### Fictional case and competing explanation

A fictional river sediment comparison shows taxon A rising from 10% to 20% of assigned reads, even though total microbial DNA changes across sampling days. This is a hypothetical instructional case, not a reported finding. Begin with one biological hypothesis and one technical or sampling rival. Before choosing the most interesting interpretation, write down what each hypothesis predicts about a newly collected specimen or orthogonal assay. Different algorithms may agree because they reuse the same flawed reference or measurement, not because they supply independent experimental confirmation.

### Worked example with units

**Problem:** Taxon A with 2,000 of 10,000 assigned reads has 20% relative assigned-read abundance, not necessarily 20% of organisms.

**Calculation:** `2000/10_000*100` = **20 %** for the invented inputs. Keep the mathematical result separate from the scientific inference. Many arithmetic relations hold exactly under their definitions while the relationship between the calculated statistic and underlying biology remains conditional. Correct arithmetic validates a calculation, but it does not establish that the input data are representative or that the result has a causal meaning. Record whether the denominator counts bases, reads, allele copies, individuals, loci or experimental runs. Recompute with a modified hypothetical input to examine numerical sensitivity.

### Error modes and validation design

A doubled relative fraction does not prove doubled absolute biomass; contamination and compositional effects can create apparent shifts. Ask which alternative assay or independent group could challenge the finding. Repeating a computation under different colors or with another software package is not independent biological replication. **Audit emphasis — Inspect the mechanism.** Link the measured molecular signal to a plausible process and identify where the causal arrow is merely assumed. Correlated regulatory, evolutionary or clinical features can have shared upstream causes.

Check spike-in standards or independent quantitative measurements and reanalyze samples at broader taxonomic resolution. The proposed new evidence should help discriminate between mechanisms rather than merely producing another version of the same computational score. Explain the important negative control and a result that would weaken your preferred hypothesis. In a scientific report, keep measurements, computed statistics, model-based predictions and proposed biological explanations in separate statements.

### Transfer exercise

Connect **Metagenomic assembly and community composition** with **Spatial genomics and tissue architecture**. Explain which source-data error would contaminate both topics and how a reference-aware provenance record would reveal it. Then answer: What was measured? How was the statistic calculated? What competing explanation remains? What independent experiment would be most efficient? Present the final inference as a conditional claim whose strength matches the available evidence.

---

## Lesson 8.3 — Spatial genomics and tissue architecture

### Mechanism and what can be inferred

Spatial assays attach molecular observations to tissue coordinates; individual capture spots can contain mixtures of cells, and resolution varies by platform. RNA expression maps are not direct photographs of protein activity. Identify the physical material, the instrument observation and the computational summary separately. This prevents a dataset label from being mistaken for the underlying biological process. The central question is **How can genomes be analyzed across cells, communities and measurement layers?** Interpret that question in the limited context of the named species, specimens and assay; do not extrapolate from one sequence representation to all individuals.

### Measurement contract and analytical method

Register tissue geometry, spot size, segmentation accuracy and coordinate transforms, then assess batch effects and spatial autocorrelation before interpreting clusters. Preregister an analysis comparison in plain language: what signal is sought, which confounders are anticipated, how filtering will work, which readouts matter, and what observation would count against the favored interpretation. When comparing results, include the reference assembly or database release, observation level, quality thresholds, removed records and a denominator for each proportion. Missing genomic measurements are not synonymous with confidently absent biological events. Explain which parts of the pipeline are deterministic transformations and which rely on empirical model assumptions.

### Fictional case and competing explanation

In a fictional plant root cross-section, transporter RNA accumulates near one tissue boundary but sampled spots overlap two anatomically distinct layers. This is a hypothetical instructional case, not a reported finding. Begin with one biological hypothesis and one technical or sampling rival. Before choosing the most interesting interpretation, write down what each hypothesis predicts about a newly collected specimen or orthogonal assay. Different algorithms may agree because they reuse the same flawed reference or measurement, not because they supply independent experimental confirmation.

### Worked example with units

**Problem:** If 48 of 120 spots meet a predefined expression criterion, positive-spot fraction is 40%, not 40% of individual cells.

**Calculation:** `48/120*100` = **40 %** for the invented inputs. Make a small companion table with the original fictional inputs, one alternative input value, the new result and a sentence describing whether the qualitative conclusion survives. Correct arithmetic validates a calculation, but it does not establish that the input data are representative or that the result has a causal meaning. Record whether the denominator counts bases, reads, allele copies, individuals, loci or experimental runs. Recompute with a modified hypothetical input to examine numerical sensitivity.

### Error modes and validation design

Misregistered images and neighborhood dependence inflate apparent replication and can assign signals to the wrong tissue domain. If the measurement was duplicated at the technical level, name the correct independent sampling level before offering any significance claim. Replication improves confidence only to the extent that it samples the relevant biological variability. **Audit emphasis — Protect the inferential boundary.** Separate an algorithmic score from a measurement and from an actionable interpretation. Showing that a model is internally consistent is not the same as validating its claims in a new cohort.

Compare marker-based localization with independent imaging and assess sensitivity to spot boundaries and segmentation methods. The proposed new evidence should help discriminate between mechanisms rather than merely producing another version of the same computational score. Explain the important negative control and a result that would weaken your preferred hypothesis. In a scientific report, keep measurements, computed statistics, model-based predictions and proposed biological explanations in separate statements.

### Transfer exercise

Connect **Spatial genomics and tissue architecture** with **Multi-omic integration and causal inference**. Explain which source-data error would contaminate both topics and how a reference-aware provenance record would reveal it. Then answer: What was measured? How was the statistic calculated? What competing explanation remains? What independent experiment would be most efficient? Present the final inference as a conditional claim whose strength matches the available evidence.

---

## Lesson 8.4 — Multi-omic integration and causal inference

### Mechanism and what can be inferred

Joint models combine DNA, RNA, chromatin or protein observations, but cross-platform measurement scales and missingness make latent factors difficult to interpret biologically. Identify the physical material, the instrument observation and the computational summary separately. This prevents a dataset label from being mistaken for the underlying biological process. The central question is **How can genomes be analyzed across cells, communities and measurement layers?** Interpret that question in the limited context of the named species, specimens and assay; do not extrapolate from one sequence representation to all individuals.

### Measurement contract and analytical method

Align sample identifiers and independent-replicate structure before fitting a model. Reserve held-out donors or batches and compare integrated conclusions with results from each layer alone. Write a data dictionary before invoking a tool. It should specify permitted values, missing-data codes, identity keys, coordinate conventions, and a worked input-output example whose result can be checked without proprietary software. When comparing results, include the reference assembly or database release, observation level, quality thresholds, removed records and a denominator for each proportion. Missing genomic measurements are not synonymous with confidently absent biological events. Explain which parts of the pipeline are deterministic transformations and which rely on empirical model assumptions.

### Fictional case and competing explanation

An invented cell-state factor predicts treatment labels across three assays, yet all treated specimens were processed on the same day. This is a hypothetical instructional case, not a reported finding. Begin with one biological hypothesis and one technical or sampling rival. Before choosing the most interesting interpretation, write down what each hypothesis predicts about a newly collected specimen or orthogonal assay. Different algorithms may agree because they reuse the same flawed reference or measurement, not because they supply independent experimental confirmation.

### Worked example with units

**Problem:** If a model correctly classifies 72 of 90 held-out samples, observed accuracy is 80%; compare with the class baseline before celebrating.

**Calculation:** `72/90*100` = **80 %** for the invented inputs. Keep the mathematical result separate from the scientific inference. Many arithmetic relations hold exactly under their definitions while the relationship between the calculated statistic and underlying biology remains conditional. Correct arithmetic validates a calculation, but it does not establish that the input data are representative or that the result has a causal meaning. Record whether the denominator counts bases, reads, allele copies, individuals, loci or experimental runs. Recompute with a modified hypothetical input to examine numerical sensitivity.

### Error modes and validation design

A visually compelling shared embedding can encode processing batch or cell number rather than a mechanistic biological axis. Consider whether the strongest-looking pattern comes from a feature selected after inspecting the answer. Exploratory selection followed by an unadjusted confirmatory claim can overstate reproducibility. **Audit emphasis — Check the sensitivity.** Vary a defensible parameter—filter threshold, reference representation, cohort subset or matching rule—and report whether your conclusion changes. Sensitivity is information about model dependence, not a reason to hide uncertain results.

Cross-validate with batches deliberately held out and confirm predicted targets with perturbation or orthogonal biological measurements. The proposed new evidence should help discriminate between mechanisms rather than merely producing another version of the same computational score. Explain the important negative control and a result that would weaken your preferred hypothesis. In a scientific report, keep measurements, computed statistics, model-based predictions and proposed biological explanations in separate statements.

### Transfer exercise

Connect **Multi-omic integration and causal inference** with **Reproducible genomic workflows and communication**. Explain which source-data error would contaminate both topics and how a reference-aware provenance record would reveal it. Then answer: What was measured? How was the statistic calculated? What competing explanation remains? What independent experiment would be most efficient? Present the final inference as a conditional claim whose strength matches the available evidence.

---

## Lesson 8.5 — Reproducible genomic workflows and communication

### Mechanism and what can be inferred

A reproducible analysis identifies input versions, code, parameters, computing environment and decision rules. A workflow that runs twice without errors may still answer the wrong scientific question. Identify the physical material, the instrument observation and the computational summary separately. This prevents a dataset label from being mistaken for the underlying biological process. The central question is **How can genomes be analyzed across cells, communities and measurement layers?** Interpret that question in the limited context of the named species, specimens and assay; do not extrapolate from one sequence representation to all individuals.

### Measurement contract and analytical method

Create a machine-readable manifest for synthetic inputs, frozen references and checksums. Save intermediate quality metrics, unit tests and analysis decisions; separate exploration from confirmatory evaluation. Reconstruct the reasoning as an evidence ledger with separate columns for raw measurement, model choice, calculated value, alternative explanation and validation status. Avoid merging uncertain evidence into one unexplained confidence label. When comparing results, include the reference assembly or database release, observation level, quality thresholds, removed records and a denominator for each proportion. Missing genomic measurements are not synonymous with confidently absent biological events. Explain which parts of the pipeline are deterministic transformations and which rely on empirical model assumptions.

### Fictional case and competing explanation

A fictional laboratory migrates from one genome assembly to another; variant counts change even though no new specimens were collected. This is a hypothetical instructional case, not a reported finding. Begin with one biological hypothesis and one technical or sampling rival. Before choosing the most interesting interpretation, write down what each hypothesis predicts about a newly collected specimen or orthogonal assay. Different algorithms may agree because they reuse the same flawed reference or measurement, not because they supply independent experimental confirmation.

### Worked example with units

**Problem:** If 38 of 40 planned assertions pass, test pass rate is 95%; failures must be classified rather than hidden by the aggregate score.

**Calculation:** `38/40*100` = **95 %** for the invented inputs. Make a small companion table with the original fictional inputs, one alternative input value, the new result and a sentence describing whether the qualitative conclusion survives. Correct arithmetic validates a calculation, but it does not establish that the input data are representative or that the result has a causal meaning. Record whether the denominator counts bases, reads, allele copies, individuals, loci or experimental runs. Recompute with a modified hypothetical input to examine numerical sensitivity.

### Error modes and validation design

An unchanged chart is not proof of reproducibility when upstream database versions moved, and an exact rerun does not resolve confounding. Explain how an earlier-stage error could propagate through several downstream analyses and create apparently consistent output. Correlation among derived reports should never substitute for documented source integrity. **Audit emphasis — Design a contrast.** Specify at least one plausible nonbiological explanation and predict which extra measurement would expose it. Negative controls and orthogonal data are often more informative than adding another correlated software score.

Rerun in a fresh environment with frozen dependencies and independently validate biological interpretations using non-overlapping data when possible. The proposed new evidence should help discriminate between mechanisms rather than merely producing another version of the same computational score. Explain the important negative control and a result that would weaken your preferred hypothesis. In a scientific report, keep measurements, computed statistics, model-based predictions and proposed biological explanations in separate statements.

### Transfer exercise

Connect **Reproducible genomic workflows and communication** with **Multi-omic integration and causal inference**. Explain which source-data error would contaminate both topics and how a reference-aware provenance record would reveal it. Then answer: What was measured? How was the statistic calculated? What competing explanation remains? What independent experiment would be most efficient? Present the final inference as a conditional claim whose strength matches the available evidence.

---

## Unit 08 capstone — Cross-modal reproducibility challenge

### Situation and materials

A fictional environmental and tissue project has 4 donors, 8 preparations, 2 sequencing batches, 2,400 single-cell barcodes and a small metagenomic table. Assume all records are fabricated for the classroom. Start by listing the observational units: organism, donor, biological preparation, technical library, genomic site or algorithmic summary. This is a crucial step because denominator mistakes can produce a result that is mathematically correct but scientifically misleading. Fix the reference and analysis version for the exercise before comparing any numbers, and include unknowns explicitly.

### Procedure and minimum outputs

Trace the independent sampling unit through each assay and compute a doublet-flag fraction, a relative read abundance and held-out prediction accuracy. Separate cells, reads, spots, organisms and donors in all tables. Your calculations need not be complicated. They should be completely reproducible, with input values, a visible formula, arithmetic and units. Create one well-documented table for the observations, a second for transformations, and a third for which interpretations survive each quality check. Explain the transformations in words rather than copying a tool output without explanation. Before choosing a cutoff, describe the costs of false positive and false negative findings in this particular fictional study.

### Competing hypotheses and sensitivity experiment

Compare an integration model trained under random cell splits with one evaluated on held-out donors and batches. Consider which visually strong effects disappear and how to report them without a misleading causal claim. Your favored explanation should generate a prediction that would be less likely under a clearly named alternative. Design one sensitivity exercise that changes a single assumption—such as callable regions, phase, ancestry strata, normalization rule or depth threshold—and track its effect on the main statistic. If the preferred interpretation changes, report that dependence rather than selecting the setting with the most dramatic result. Explain which new specimen, assay or observation would provide the best independent discrimination.

### Deliverables, reflection and peer review

Submit a frozen manifest, lineage-aware validation design, release notes and three specific experiments that could corroborate the integrated hypothesis. In addition, prepare a reproducibility manifest with input identifiers, simulated-only status, calculations, method version and a short rationale for every excluded observation. Include a four-sentence abstract distinguishing what is measured, estimated, hypothesized and still unknown. Exchange reports with another learner, ask them to recalculate at least one statistic using only the supplied source data, and record one objection that improves the design. Do not describe any result as clinical, diagnostic or measured in the real world.

### Challenge questions for synthesis

1. Which dataset field would have the greatest impact if it were silently mislabeled? Identify a simple audit that could catch the mistake before modeling.
2. Does the unit's central conclusion rely on random sampling, correct genome representation, accurate molecular classification or independent replication? Rank those assumptions in importance for this case.
3. What result could falsify the leading explanation without proving every alternative? Discuss the distinction between rejection of one hypothesis and proof of another.
4. If your method produced a visually excellent plot from copied or confounded measurements, what independent check would you demand before publication?
5. Explain why the precise mathematical result alone does not certify the biological or social validity of the research conclusion.

---

## Two interactive teaching models

Change each slider, observe its graph and record which assumptions make the formula valid. These are hypothetical mathematical demonstrations, not empirical sequence analyses.

### Model 8.1: Barcode doublet-flag percentage

**Equation:** Flagged fraction = 100×x/2000. **Caveat:** Screening statistic not a true cell identity diagnosis. Change the independent parameter, then explain whether the output change is a simple mathematical consequence or requires a biological inference. A monotone visual trend is not automatically a causal biological law. Identify the units and what is held constant.

### Model 8.2: Compositional relative read fraction

**Equation:** Relative reads = x/10,000. **Caveat:** Not absolute biomass or organism count. Change the independent parameter, then explain whether the output change is a simple mathematical consequence or requires a biological inference. A monotone visual trend is not automatically a causal biological law. Identify the units and what is held constant.
