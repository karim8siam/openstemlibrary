# Unit 02 — Sequencing design, measurement and quality

> **OpenSTEM Genomics · Book 16 · Editorial teaching draft.** All worked case data and investigations are synthetic. The interactive models describe simplified mathematical relations, not diagnoses or empirical genomic claims.

## Central scientific question

**How do laboratory choices determine which genomic events an analysis can detect?**

### Conceptual context and how the five lessons fit

Sequencing is a measurement process, not a neutral window onto DNA. How a sample is recruited, stored and extracted influences which molecules are available, while library preparation and instrument characteristics determine which molecules are read. A theoretical coverage equation offers only a rough starting point because sequencing data violate uniform sampling assumptions in multiple ways. This unit contrasts the strengths and limitations of short and long reads, introduces independent biological replication, and teaches quality measures that are meaningful only with denominators and detailed provenance. The central analytical goal is to distinguish inability to observe an event from genuine absence of the event. Attention to data protection is part of scientific design, especially when human genomes or community-sensitive collections are involved.

### A running case to reason through

Two research teams sequence the same fictional organism at nominally similar depth but one fails to observe a repeat-mediated event. The proposed explanation should remain a working hypothesis until both the measurement process and alternative biological accounts have been examined. Identify a plausible negative control, a sample identity verification and a condition in which the preferred model might fail. A final plot can be numerically precise while its biological conclusion is uncertain; your task is to make that uncertainty visible rather than treating it as a defect.

### Unit learning objectives

By the end of this unit, you should be able to reconstruct the data assumptions behind each of the five main topics, reproduce their toy calculations, distinguish technical and biological replication, identify a rival explanation for an apparent signal, and propose an independent measurement that would strengthen or challenge the inference. For each numerical answer, know the denominator, its unit and the simplifications required. Give yourself permission to conclude "not established" when appropriate.

### Study route

Read the five lessons in order. Each starts with an operational definition, moves through a fictional case and a worked calculation, then challenges the tempting inference. Compute the numbers by hand before using code. Finish with the unit capstone and the interactive model questions. Learning genomics requires deciding which questions an assay can answer at least as much as mastering the associated algorithm.

---

## Lesson 2.1 — Biological sampling and library construction

### Mechanism and what can be inferred

DNA extraction, fragmentation, enrichment, barcoding and amplification change which molecules enter the sequencer. Library preparation artifacts can mimic allelic imbalance even before alignment or statistical filtering begins. Identify the physical material, the instrument observation and the computational summary separately. This prevents a dataset label from being mistaken for the underlying biological process. The central question is **How do laboratory choices determine which genomic events an analysis can detect?** Interpret that question in the limited context of the named species, specimens and assay; do not extrapolate from one sequence representation to all individuals.

### Measurement contract and analytical method

Plan sampling units independently of technical replicates; register tissue, extraction batch, library index, storage, input mass and negative controls. Specify whether whole-genome, exome or targeted assays answer the biological question. Write a data dictionary before invoking a tool. It should specify permitted values, missing-data codes, identity keys, coordinate conventions, and a worked input-output example whose result can be checked without proprietary software. When comparing results, include the reference assembly or database release, observation level, quality thresholds, removed records and a denominator for each proportion. Missing genomic measurements are not synonymous with confidently absent biological events. Explain which parts of the pipeline are deterministic transformations and which rely on empirical model assumptions.

### Fictional case and competing explanation

An imaginary coastal plant survey samples ten individual plants but sequences two technical libraries for each. The biological sample size is ten, not twenty, because the libraries share DNA extraction and individual origin. This is a hypothetical instructional case, not a reported finding. Begin with one biological hypothesis and one technical or sampling rival. Before choosing the most interesting interpretation, write down what each hypothesis predicts about a newly collected specimen or orthogonal assay. Different algorithms may agree because they reuse the same flawed reference or measurement, not because they supply independent experimental confirmation.

### Worked example with units

**Problem:** Ten plants with two libraries each yield 20 libraries but biological n=10; the duplication factor is 2.

**Calculation:** `20/10` = **2 libraries per biological specimen** for the invented inputs. Keep the mathematical result separate from the scientific inference. Many arithmetic relations hold exactly under their definitions while the relationship between the calculated statistic and underlying biology remains conditional. Correct arithmetic validates a calculation, but it does not establish that the input data are representative or that the result has a causal meaning. Record whether the denominator counts bases, reads, allele copies, individuals, loci or experimental runs. Recompute with a modified hypothetical input to examine numerical sensitivity.

### Error modes and validation design

A sequencing lane or barcode is not a new biological specimen. Batch-confounded phenotype groups produce technical differences that can be mistaken for adaptation. Explain how an earlier-stage error could propagate through several downstream analyses and create apparently consistent output. Correlation among derived reports should never substitute for documented source integrity. **Audit emphasis — Protect the inferential boundary.** Separate an algorithmic score from a measurement and from an actionable interpretation. Showing that a model is internally consistent is not the same as validating its claims in a new cohort.

Randomize specimens across batches, include extraction controls and test whether signals reproduce across truly independent individual plants. The proposed new evidence should help discriminate between mechanisms rather than merely producing another version of the same computational score. Explain the important negative control and a result that would weaken your preferred hypothesis. In a scientific report, keep measurements, computed statistics, model-based predictions and proposed biological explanations in separate statements.

### Transfer exercise

Connect **Biological sampling and library construction** with **Short-read sequencing and base-call confidence**. Explain which source-data error would contaminate both topics and how a reference-aware provenance record would reveal it. Then answer: What was measured? How was the statistic calculated? What competing explanation remains? What independent experiment would be most efficient? Present the final inference as a conditional claim whose strength matches the available evidence.

---

## Lesson 2.2 — Short-read sequencing and base-call confidence

### Mechanism and what can be inferred

Short-read instruments generate large numbers of relatively small reads, allowing efficient coverage of many unique loci but reducing power to resolve repeats longer than a read or fragment. A Phred score describes modeled base-call error, not mapping correctness. Identify the physical material, the instrument observation and the computational summary separately. This prevents a dataset label from being mistaken for the underlying biological process. The central question is **How do laboratory choices determine which genomic events an analysis can detect?** Interpret that question in the limited context of the named species, specimens and assay; do not extrapolate from one sequence representation to all individuals.

### Measurement contract and analytical method

Record paired-end status, nominal read length, quality encoding, total bases, adapter fraction and per-cycle quality. Examine coverage distributions and unexpected sample mixtures rather than filtering solely on mean quality. Reconstruct the reasoning as an evidence ledger with separate columns for raw measurement, model choice, calculated value, alternative explanation and validation status. Avoid merging uncertain evidence into one unexplained confidence label. When comparing results, include the reference assembly or database release, observation level, quality thresholds, removed records and a denominator for each proportion. Missing genomic measurements are not synonymous with confidently absent biological events. Explain which parts of the pipeline are deterministic transformations and which rely on empirical model assumptions.

### Fictional case and competing explanation

Two fictional soybean libraries have similar median Q30 fractions, while one has highly uneven coverage caused by enrichment and amplification biases. This is a hypothetical instructional case, not a reported finding. Begin with one biological hypothesis and one technical or sampling rival. Before choosing the most interesting interpretation, write down what each hypothesis predicts about a newly collected specimen or orthogonal assay. Different algorithms may agree because they reuse the same flawed reference or measurement, not because they supply independent experimental confirmation.

### Worked example with units

**Problem:** At Q=30, modeled base error probability is 10^(−3)=0.001; an idealized sample of 10,000 comparable base calls predicts ten errors on average.

**Calculation:** `10**(-30/10)` = **0.001 estimated base-call error probability** for the invented inputs. Make a small companion table with the original fictional inputs, one alternative input value, the new result and a sentence describing whether the qualitative conclusion survives. Correct arithmetic validates a calculation, but it does not establish that the input data are representative or that the result has a causal meaning. Record whether the denominator counts bases, reads, allele copies, individuals, loci or experimental runs. Recompute with a modified hypothetical input to examine numerical sensitivity.

### Error modes and validation design

A high mean Phred score does not guarantee accurate structural-variant inference or show that inaccessible GC-rich intervals were measured. Ask which alternative assay or independent group could challenge the finding. Repeating a computation under different colors or with another software package is not independent biological replication. **Audit emphasis — Check the sensitivity.** Vary a defensible parameter—filter threshold, reference representation, cohort subset or matching rule—and report whether your conclusion changes. Sensitivity is information about model dependence, not a reason to hide uncertain results.

Inspect insert-size patterns and local coverage across difficult regions and confirm representative findings with an orthogonal measurement platform. The proposed new evidence should help discriminate between mechanisms rather than merely producing another version of the same computational score. Explain the important negative control and a result that would weaken your preferred hypothesis. In a scientific report, keep measurements, computed statistics, model-based predictions and proposed biological explanations in separate statements.

### Transfer exercise

Connect **Short-read sequencing and base-call confidence** with **Long-read and linked-molecule sequencing**. Explain which source-data error would contaminate both topics and how a reference-aware provenance record would reveal it. Then answer: What was measured? How was the statistic calculated? What competing explanation remains? What independent experiment would be most efficient? Present the final inference as a conditional claim whose strength matches the available evidence.

---

## Lesson 2.3 — Long-read and linked-molecule sequencing

### Mechanism and what can be inferred

Long reads span repeat boundaries and can support haplotype phasing, yet they have platform-dependent error profiles and may require polishing or consensus. Molecule length, accuracy and independence are different properties. Identify the physical material, the instrument observation and the computational summary separately. This prevents a dataset label from being mistaken for the underlying biological process. The central question is **How do laboratory choices determine which genomic events an analysis can detect?** Interpret that question in the limited context of the named species, specimens and assay; do not extrapolate from one sequence representation to all individuals.

### Measurement contract and analytical method

Summarize read-length N50, yield, estimated identity and molecule-level support; distinguish high-fidelity consensus reads from raw signal-derived reads. Record preparation methods that may favor intact long molecules. Create a tiny independent benchmark that contains an ordinary case, an ambiguous boundary case and a deliberately malformed record. Check not only output numbers but also whether the tool detects invalid assumptions and refuses silent corrections. When comparing results, include the reference assembly or database release, observation level, quality thresholds, removed records and a denominator for each proportion. Missing genomic measurements are not synonymous with confidently absent biological events. Explain which parts of the pipeline are deterministic transformations and which rely on empirical model assumptions.

### Fictional case and competing explanation

An imaginary fish assembly resolves a 12-kb tandem repeat using long molecules; a short-read-only assembly had split the region across contigs. This is a hypothetical instructional case, not a reported finding. Begin with one biological hypothesis and one technical or sampling rival. Before choosing the most interesting interpretation, write down what each hypothesis predicts about a newly collected specimen or orthogonal assay. Different algorithms may agree because they reuse the same flawed reference or measurement, not because they supply independent experimental confirmation.

### Worked example with units

**Problem:** If three reads span 15 kb, 18 kb and 27 kb, arithmetic mean span is 20 kb; this does not describe the whole read-length distribution.

**Calculation:** `(15+18+27)/3` = **20 kb** for the invented inputs. Keep the mathematical result separate from the scientific inference. Many arithmetic relations hold exactly under their definitions while the relationship between the calculated statistic and underlying biology remains conditional. Correct arithmetic validates a calculation, but it does not establish that the input data are representative or that the result has a causal meaning. Record whether the denominator counts bases, reads, allele copies, individuals, loci or experimental runs. Recompute with a modified hypothetical input to examine numerical sensitivity.

### Error modes and validation design

Treating every long alignment as independent support ignores chimeric molecules, correlated systematic errors and alignment to a wrong paralog. If the measurement was duplicated at the technical level, name the correct independent sampling level before offering any significance claim. Replication improves confidence only to the extent that it samples the relevant biological variability. **Audit emphasis — Design a contrast.** Specify at least one plausible nonbiological explanation and predict which extra measurement would expose it. Negative controls and orthogonal data are often more informative than adding another correlated software score.

Cross-validate candidate rearrangements with independent long molecules and paired-end or optical-map evidence wherever available. The proposed new evidence should help discriminate between mechanisms rather than merely producing another version of the same computational score. Explain the important negative control and a result that would weaken your preferred hypothesis. In a scientific report, keep measurements, computed statistics, model-based predictions and proposed biological explanations in separate statements.

### Transfer exercise

Connect **Long-read and linked-molecule sequencing** with **Coverage, callable sequence and contamination**. Explain which source-data error would contaminate both topics and how a reference-aware provenance record would reveal it. Then answer: What was measured? How was the statistic calculated? What competing explanation remains? What independent experiment would be most efficient? Present the final inference as a conditional claim whose strength matches the available evidence.

---

## Lesson 2.4 — Coverage, callable sequence and contamination

### Mechanism and what can be inferred

Mean depth equals aligned bases divided by reference length only under simplifying assumptions. Real genomes have low-complexity, GC-dependent and duplicated regions that remain poorly callable despite high mean depth. Identify the physical material, the instrument observation and the computational summary separately. This prevents a dataset label from being mistaken for the underlying biological process. The central question is **How do laboratory choices determine which genomic events an analysis can detect?** Interpret that question in the limited context of the named species, specimens and assay; do not extrapolate from one sequence representation to all individuals.

### Measurement contract and analytical method

Measure per-position depth, callable fraction, duplicate fraction, base/mapping quality and contamination statistics. State whether depth is mapped, unique, on-target or physically independent molecule depth. For a transparent analysis, make two small tables: one describing source specimens and assays, and another describing computational transformations. The join keys should let another investigator trace a number back to its input without revealing restricted personal information. When comparing results, include the reference assembly or database release, observation level, quality thresholds, removed records and a denominator for each proportion. Missing genomic measurements are not synonymous with confidently absent biological events. Explain which parts of the pipeline are deterministic transformations and which rely on empirical model assumptions.

### Fictional case and competing explanation

An invented 100-Mb haploid genome receives 3 Gb mapped sequence; mean depth is 30× while 8% of sites fail a minimum coverage threshold. This is a hypothetical instructional case, not a reported finding. Begin with one biological hypothesis and one technical or sampling rival. Before choosing the most interesting interpretation, write down what each hypothesis predicts about a newly collected specimen or orthogonal assay. Different algorithms may agree because they reuse the same flawed reference or measurement, not because they supply independent experimental confirmation.

### Worked example with units

**Problem:** Three billion mapped bases divided by 100 million reference bases equals 30× mean depth, not 30 independent evidence points for every locus.

**Calculation:** `3_000_000_000/100_000_000` = **30 ×** for the invented inputs. Make a small companion table with the original fictional inputs, one alternative input value, the new result and a sentence describing whether the qualitative conclusion survives. Correct arithmetic validates a calculation, but it does not establish that the input data are representative or that the result has a causal meaning. Record whether the denominator counts bases, reads, allele copies, individuals, loci or experimental runs. Recompute with a modified hypothetical input to examine numerical sensitivity.

### Error modes and validation design

A uniform-coverage calculation does not prove Poisson sampling; collapsed repeats can inflate apparent depth without increasing unique molecular coverage. Consider whether the strongest-looking pattern comes from a feature selected after inspecting the answer. Exploratory selection followed by an unadjusted confirmatory claim can overstate reproducibility. **Audit emphasis — Begin with the denominator.** First write the total that would make a reported fraction equal to one: all molecules, all individuals, all reference positions or all interrogated loci. A percentage cannot be compared across studies if the denominators are inconsistent.

Compare depth distributions with mappability masks and sample-specific GC curves; separately report high-confidence callable sequence under fixed criteria. The proposed new evidence should help discriminate between mechanisms rather than merely producing another version of the same computational score. Explain the important negative control and a result that would weaken your preferred hypothesis. In a scientific report, keep measurements, computed statistics, model-based predictions and proposed biological explanations in separate statements.

### Transfer exercise

Connect **Coverage, callable sequence and contamination** with **Genomic data quality and responsible stewardship**. Explain which source-data error would contaminate both topics and how a reference-aware provenance record would reveal it. Then answer: What was measured? How was the statistic calculated? What competing explanation remains? What independent experiment would be most efficient? Present the final inference as a conditional claim whose strength matches the available evidence.

---

## Lesson 2.5 — Genomic data quality and responsible stewardship

### Mechanism and what can be inferred

Genome data can reveal familial relationships and sensitive inferences even after obvious names have been removed. Meaningful reproducibility and privacy are compatible only when access policies and consent expectations are built into the data workflow. Identify the physical material, the instrument observation and the computational summary separately. This prevents a dataset label from being mistaken for the underlying biological process. The central question is **How do laboratory choices determine which genomic events an analysis can detect?** Interpret that question in the limited context of the named species, specimens and assay; do not extrapolate from one sequence representation to all individuals.

### Measurement contract and analytical method

Keep source material protected, verify checksums, use role-based access and record releases of reference files and analysis containers. Distinguish open synthetic teaching data from potentially identifiable actual human genome records. Preregister an analysis comparison in plain language: what signal is sought, which confounders are anticipated, how filtering will work, which readouts matter, and what observation would count against the favored interpretation. When comparing results, include the reference assembly or database release, observation level, quality thresholds, removed records and a denominator for each proportion. Missing genomic measurements are not synonymous with confidently absent biological events. Explain which parts of the pipeline are deterministic transformations and which rely on empirical model assumptions.

### Fictional case and competing explanation

A class project reuses four artificial DNA files from a public teaching repository; no subject consent is required for invented records, yet students still practice clear licensing and provenance documentation. This is a hypothetical instructional case, not a reported finding. Begin with one biological hypothesis and one technical or sampling rival. Before choosing the most interesting interpretation, write down what each hypothesis predicts about a newly collected specimen or orthogonal assay. Different algorithms may agree because they reuse the same flawed reference or measurement, not because they supply independent experimental confirmation.

### Worked example with units

**Problem:** If 9 of 12 planned input files pass SHA-256 verification, manifest completion is 75%, a workflow-quality measure rather than evidence of biological validity.

**Calculation:** `9/12*100` = **75 %** for the invented inputs. Keep the mathematical result separate from the scientific inference. Many arithmetic relations hold exactly under their definitions while the relationship between the calculated statistic and underlying biology remains conditional. Correct arithmetic validates a calculation, but it does not establish that the input data are representative or that the result has a causal meaning. Record whether the denominator counts bases, reads, allele copies, individuals, loci or experimental runs. Recompute with a modified hypothetical input to examine numerical sensitivity.

### Error modes and validation design

A dataset labeled de-identified may still permit re-identification in combination with external ancestry or family information; unrestricted publication is not a routine default. Explain how an earlier-stage error could propagate through several downstream analyses and create apparently consistent output. Correlation among derived reports should never substitute for documented source integrity. **Audit emphasis — Examine independence.** Ask whether repeated observations came from distinct biological sources or from technical processing of the same material. A thousand reads from one library can improve measurement precision without creating a thousand independent organisms.

Conduct a threat-model exercise and specify what information is necessary for reproducibility versus what needs controlled access and governance. The proposed new evidence should help discriminate between mechanisms rather than merely producing another version of the same computational score. Explain the important negative control and a result that would weaken your preferred hypothesis. In a scientific report, keep measurements, computed statistics, model-based predictions and proposed biological explanations in separate statements.

### Transfer exercise

Connect **Genomic data quality and responsible stewardship** with **Coverage, callable sequence and contamination**. Explain which source-data error would contaminate both topics and how a reference-aware provenance record would reveal it. Then answer: What was measured? How was the statistic calculated? What competing explanation remains? What independent experiment would be most efficient? Present the final inference as a conditional claim whose strength matches the available evidence.

---

## Unit 02 capstone — Sequencing assessment under uneven coverage

### Situation and materials

Design a fictional sequencing plan for 12 independently collected specimens. Each specimen has two technical libraries and three candidate platforms offer different read lengths and read accuracies. Assume all records are fabricated for the classroom. Start by listing the observational units: organism, donor, biological preparation, technical library, genomic site or algorithmic summary. This is a crucial step because denominator mistakes can produce a result that is mathematically correct but scientifically misleading. Fix the reference and analysis version for the exercise before comparing any numbers, and include unknowns explicitly.

### Procedure and minimum outputs

Make a table of biological versus technical sample counts, anticipated mean coverage, inaccessible intervals and expected evidence for different variant types. Calculate a toy base error probability but do not conflate it with variant false-positive rate. Your calculations need not be complicated. They should be completely reproducible, with input values, a visible formula, arithmetic and units. Create one well-documented table for the observations, a second for transformations, and a third for which interpretations survive each quality check. Explain the transformations in words rather than copying a tool output without explanation. Before choosing a cutoff, describe the costs of false positive and false negative findings in this particular fictional study.

### Competing hypotheses and sensitivity experiment

Create a case in which nominal 30× mean coverage hides an uncallable repeat. Explore how different QC filters remove or retain intervals and quantify the denominator of reported callability. Your favored explanation should generate a prediction that would be less likely under a clearly named alternative. Design one sensitivity exercise that changes a single assumption—such as callable regions, phase, ancestry strata, normalization rule or depth threshold—and track its effect on the main statistic. If the preferred interpretation changes, report that dependence rather than selecting the setting with the most dramatic result. Explain which new specimen, assay or observation would provide the best independent discrimination.

### Deliverables, reflection and peer review

Submit a pre-registered design, a quality dashboard specification, a contamination checklist and a privacy-preserving sharing statement. In addition, prepare a reproducibility manifest with input identifiers, simulated-only status, calculations, method version and a short rationale for every excluded observation. Include a four-sentence abstract distinguishing what is measured, estimated, hypothesized and still unknown. Exchange reports with another learner, ask them to recalculate at least one statistic using only the supplied source data, and record one objection that improves the design. Do not describe any result as clinical, diagnostic or measured in the real world.

### Challenge questions for synthesis

1. Which dataset field would have the greatest impact if it were silently mislabeled? Identify a simple audit that could catch the mistake before modeling.
2. Does the unit's central conclusion rely on random sampling, correct genome representation, accurate molecular classification or independent replication? Rank those assumptions in importance for this case.
3. What result could falsify the leading explanation without proving every alternative? Discuss the distinction between rejection of one hypothesis and proof of another.
4. If your method produced a visually excellent plot from copied or confounded measurements, what independent check would you demand before publication?
5. Explain why the precise mathematical result alone does not certify the biological or social validity of the research conclusion.

---

## Two interactive teaching models

Change each slider, observe its graph and record which assumptions make the formula valid. These are hypothetical mathematical demonstrations, not empirical sequence analyses.

### Model 2.1: Base-call error from a Phred score

**Equation:** P(error)=10^(−Q/10). **Caveat:** Does not include mapping error. Change the independent parameter, then explain whether the output change is a simple mathematical consequence or requires a biological inference. A monotone visual trend is not automatically a causal biological law. Identify the units and what is held constant.

### Model 2.2: Nominal average read depth

**Equation:** Depth = aligned bases / genome length. **Caveat:** Assume 100 Mb reference, uniformity not implied. Change the independent parameter, then explain whether the output change is a simple mathematical consequence or requires a biological inference. A monotone visual trend is not automatically a causal biological law. Identify the units and what is held constant.
