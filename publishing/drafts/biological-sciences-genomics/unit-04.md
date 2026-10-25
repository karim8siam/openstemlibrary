# Unit 04 — Sequence variation and haplotype inference

> **OpenSTEM Genomics · Book 16 · Editorial teaching draft.** All worked case data and investigations are synthetic. The interactive models describe simplified mathematical relations, not diagnoses or empirical genomic claims.

## Central scientific question

**What genomic differences exist and how confidently can they be called?**

### Conceptual context and how the five lessons fit

Genomic variation is defined relative to a reference and encoded through conventions. An insertion in one representation may become a deletion under a different reference path; a biologically equivalent indel can also shift coordinates within a repeat. At the same time, variant calling must account for sequencing uncertainty, ploidy, contamination and technical artifacts. This unit examines small changes, copy-number variation, larger rearrangements, haplotype phase and the discipline of prioritization. Every stage answers a separate question: is the sequence signal real, how is the event represented, what genotype is supported, how might function be affected, and what action—if any—could the evidence justify? These questions should never be compressed into a single confidence score.

### A running case to reason through

A rare-variant study reports divergent calls depending on read alignment and repetitive-sequence handling. The proposed explanation should remain a working hypothesis until both the measurement process and alternative biological accounts have been examined. Identify a plausible negative control, a sample identity verification and a condition in which the preferred model might fail. A final plot can be numerically precise while its biological conclusion is uncertain; your task is to make that uncertainty visible rather than treating it as a defect.

### Unit learning objectives

By the end of this unit, you should be able to reconstruct the data assumptions behind each of the five main topics, reproduce their toy calculations, distinguish technical and biological replication, identify a rival explanation for an apparent signal, and propose an independent measurement that would strengthen or challenge the inference. For each numerical answer, know the denominator, its unit and the simplifications required. Give yourself permission to conclude "not established" when appropriate.

### Study route

Read the five lessons in order. Each starts with an operational definition, moves through a fictional case and a worked calculation, then challenges the tempting inference. Compute the numbers by hand before using code. Finish with the unit capstone and the interactive model questions. Learning genomics requires deciding which questions an assay can answer at least as much as mastering the associated algorithm.

---

## Lesson 4.1 — Single-nucleotide and small insertion/deletion variants

### Mechanism and what can be inferred

A variant call describes differences relative to a specified reference; depth, mapping quality, allelic balance and strand evidence affect reliability. The same event may have several equivalent representations in repetitive sequence. Identify the physical material, the instrument observation and the computational summary separately. This prevents a dataset label from being mistaken for the underlying biological process. The central question is **What genomic differences exist and how confidently can they be called?** Interpret that question in the limited context of the named species, specimens and assay; do not extrapolate from one sequence representation to all individuals.

### Measurement contract and analytical method

Retain reference allele, alternate allele, genomic assembly, normalized position and genotype likelihoods. Evaluate sample and site quality separately, and distinguish a call from a biologically functional interpretation. Preregister an analysis comparison in plain language: what signal is sought, which confounders are anticipated, how filtering will work, which readouts matter, and what observation would count against the favored interpretation. When comparing results, include the reference assembly or database release, observation level, quality thresholds, removed records and a denominator for each proportion. Missing genomic measurements are not synonymous with confidently absent biological events. Explain which parts of the pipeline are deterministic transformations and which rely on empirical model assumptions.

### Fictional case and competing explanation

At a fictional exon boundary, short-read alignment shifts an indel within a short repeat. Two tools emit different coordinates for effectively the same haplotype change. This is a hypothetical instructional case, not a reported finding. Begin with one biological hypothesis and one technical or sampling rival. Before choosing the most interesting interpretation, write down what each hypothesis predicts about a newly collected specimen or orthogonal assay. Different algorithms may agree because they reuse the same flawed reference or measurement, not because they supply independent experimental confirmation.

### Worked example with units

**Problem:** At a locus with 18 alternate and 42 reference reads, observed alternate fraction is 18/60 = 30%, not an exact germline genotype.

**Calculation:** `18/(18+42)*100` = **30 %** for the invented inputs. Make a small companion table with the original fictional inputs, one alternative input value, the new result and a sentence describing whether the qualitative conclusion survives. Correct arithmetic validates a calculation, but it does not establish that the input data are representative or that the result has a causal meaning. Record whether the denominator counts bases, reads, allele copies, individuals, loci or experimental runs. Recompute with a modified hypothetical input to examine numerical sensitivity.

### Error modes and validation design

Comparing raw coordinates without normalization produces false disagreement, while counting alternate reads without mapping checks overstates confidence. Explain how an earlier-stage error could propagate through several downstream analyses and create apparently consistent output. Correlation among derived reports should never substitute for documented source integrity. **Audit emphasis — Design a contrast.** Specify at least one plausible nonbiological explanation and predict which extra measurement would expose it. Negative controls and orthogonal data are often more informative than adding another correlated software score.

Normalize against the same reference, inspect read placement and evaluate orthogonal evidence for a subset of hard-to-call loci. The proposed new evidence should help discriminate between mechanisms rather than merely producing another version of the same computational score. Explain the important negative control and a result that would weaken your preferred hypothesis. In a scientific report, keep measurements, computed statistics, model-based predictions and proposed biological explanations in separate statements.

### Transfer exercise

Connect **Single-nucleotide and small insertion/deletion variants** with **Copy-number variation and dosage**. Explain which source-data error would contaminate both topics and how a reference-aware provenance record would reveal it. Then answer: What was measured? How was the statistic calculated? What competing explanation remains? What independent experiment would be most efficient? Present the final inference as a conditional claim whose strength matches the available evidence.

---

## Lesson 4.2 — Copy-number variation and dosage

### Mechanism and what can be inferred

Deletions, duplications and amplifications alter segment dosage; short-read depth reflects copy number and technical factors such as GC content and mappability. Biological ploidy and mosaic mixtures also change expected signals. Identify the physical material, the instrument observation and the computational summary separately. This prevents a dataset label from being mistaken for the underlying biological process. The central question is **What genomic differences exist and how confidently can they be called?** Interpret that question in the limited context of the named species, specimens and assay; do not extrapolate from one sequence representation to all individuals.

### Measurement contract and analytical method

Normalize depth by robust reference intervals and describe whether comparisons are against a diploid baseline, matched control or cohort expectation. Seek breakpoint or allele-fraction evidence where feasible. Write a data dictionary before invoking a tool. It should specify permitted values, missing-data codes, identity keys, coordinate conventions, and a worked input-output example whose result can be checked without proprietary software. When comparing results, include the reference assembly or database release, observation level, quality thresholds, removed records and a denominator for each proportion. Missing genomic measurements are not synonymous with confidently absent biological events. Explain which parts of the pipeline are deterministic transformations and which rely on empirical model assumptions.

### Fictional case and competing explanation

An imaginary tissue sample shows 1.4-times expected depth across a long chromosome segment; this could reflect mosaic gain or mapping to segmental duplications. This is a hypothetical instructional case, not a reported finding. Begin with one biological hypothesis and one technical or sampling rival. Before choosing the most interesting interpretation, write down what each hypothesis predicts about a newly collected specimen or orthogonal assay. Different algorithms may agree because they reuse the same flawed reference or measurement, not because they supply independent experimental confirmation.

### Worked example with units

**Problem:** Normalized relative depth of 150 counts versus a matched baseline of 100 is 1.5; copy number is not necessarily exactly three.

**Calculation:** `150/100` = **1.5 relative depth** for the invented inputs. Keep the mathematical result separate from the scientific inference. Many arithmetic relations hold exactly under their definitions while the relationship between the calculated statistic and underlying biology remains conditional. Correct arithmetic validates a calculation, but it does not establish that the input data are representative or that the result has a causal meaning. Record whether the denominator counts bases, reads, allele copies, individuals, loci or experimental runs. Recompute with a modified hypothetical input to examine numerical sensitivity.

### Error modes and validation design

Raw depth ratios can confuse global library-size shifts, hidden aneuploidy and repetitive mapping with local copy-number changes. Ask which alternative assay or independent group could challenge the finding. Repeating a computation under different colors or with another software package is not independent biological replication. **Audit emphasis — Begin with the denominator.** First write the total that would make a reported fraction equal to one: all molecules, all individuals, all reference positions or all interrogated loci. A percentage cannot be compared across studies if the denominators are inconsistent.

Check neighboring segments, allele balance and an independent technology before concluding a physical duplication. The proposed new evidence should help discriminate between mechanisms rather than merely producing another version of the same computational score. Explain the important negative control and a result that would weaken your preferred hypothesis. In a scientific report, keep measurements, computed statistics, model-based predictions and proposed biological explanations in separate statements.

### Transfer exercise

Connect **Copy-number variation and dosage** with **Structural variants and repeat-mediated changes**. Explain which source-data error would contaminate both topics and how a reference-aware provenance record would reveal it. Then answer: What was measured? How was the statistic calculated? What competing explanation remains? What independent experiment would be most efficient? Present the final inference as a conditional claim whose strength matches the available evidence.

---

## Lesson 4.3 — Structural variants and repeat-mediated changes

### Mechanism and what can be inferred

Inversions, large insertions, deletions, translocations and complex rearrangements can be inferred from read pairs, split reads, long-read alignments or assembly comparisons. Evidence strength depends on breakpoint uniqueness. Identify the physical material, the instrument observation and the computational summary separately. This prevents a dataset label from being mistaken for the underlying biological process. The central question is **What genomic differences exist and how confidently can they be called?** Interpret that question in the limited context of the named species, specimens and assay; do not extrapolate from one sequence representation to all individuals.

### Measurement contract and analytical method

Represent both breakpoints and orientation and preserve uncertainty intervals. Compare multiple callers with common event definitions, including whether complex or nested rearrangements are collapsed into one record. Reconstruct the reasoning as an evidence ledger with separate columns for raw measurement, model choice, calculated value, alternative explanation and validation status. Avoid merging uncertain evidence into one unexplained confidence label. When comparing results, include the reference assembly or database release, observation level, quality thresholds, removed records and a denominator for each proportion. Missing genomic measurements are not synonymous with confidently absent biological events. Explain which parts of the pipeline are deterministic transformations and which rely on empirical model assumptions.

### Fictional case and competing explanation

A synthetic chromosome inversion is suggested by split reads at two boundaries; the event lies inside duplicated segments that complicate confident breakpoint placement. This is a hypothetical instructional case, not a reported finding. Begin with one biological hypothesis and one technical or sampling rival. Before choosing the most interesting interpretation, write down what each hypothesis predicts about a newly collected specimen or orthogonal assay. Different algorithms may agree because they reuse the same flawed reference or measurement, not because they supply independent experimental confirmation.

### Worked example with units

**Problem:** If 24 of 30 high-confidence candidate junctions validate, observed validation proportion is 80%, conditional on the selected candidates.

**Calculation:** `24/30*100` = **80 %** for the invented inputs. Make a small companion table with the original fictional inputs, one alternative input value, the new result and a sentence describing whether the qualitative conclusion survives. Correct arithmetic validates a calculation, but it does not establish that the input data are representative or that the result has a causal meaning. Record whether the denominator counts bases, reads, allele copies, individuals, loci or experimental runs. Recompute with a modified hypothetical input to examine numerical sensitivity.

### Error modes and validation design

Two independent callers on one aligner are not two independent observations. Repeats can create mirrored breakpoint signals. If the measurement was duplicated at the technical level, name the correct independent sampling level before offering any significance claim. Replication improves confidence only to the extent that it samples the relevant biological variability. **Audit emphasis — Examine independence.** Ask whether repeated observations came from distinct biological sources or from technical processing of the same material. A thousand reads from one library can improve measurement precision without creating a thousand independent organisms.

Use molecules spanning junctions and a second mapping representation to distinguish one genuine inversion from alternative repeat-mediated placements. The proposed new evidence should help discriminate between mechanisms rather than merely producing another version of the same computational score. Explain the important negative control and a result that would weaken your preferred hypothesis. In a scientific report, keep measurements, computed statistics, model-based predictions and proposed biological explanations in separate statements.

### Transfer exercise

Connect **Structural variants and repeat-mediated changes** with **Haplotype blocks, linkage and allele phase**. Explain which source-data error would contaminate both topics and how a reference-aware provenance record would reveal it. Then answer: What was measured? How was the statistic calculated? What competing explanation remains? What independent experiment would be most efficient? Present the final inference as a conditional claim whose strength matches the available evidence.

---

## Lesson 4.4 — Haplotype blocks, linkage and allele phase

### Mechanism and what can be inferred

Alleles at nearby loci may be inherited together; haplotype blocks summarize correlated variation but change with recombination history and sampled populations. Phasing is an inference, not an observed property of unlinked short reads. Identify the physical material, the instrument observation and the computational summary separately. This prevents a dataset label from being mistaken for the underlying biological process. The central question is **What genomic differences exist and how confidently can they be called?** Interpret that question in the limited context of the named species, specimens and assay; do not extrapolate from one sequence representation to all individuals.

### Measurement contract and analytical method

Specify the phase-set definition, genetic map context, confidence metric and sample composition. Avoid labeling a haplotype common or rare without identifying the reference population and dataset. Create a tiny independent benchmark that contains an ordinary case, an ambiguous boundary case and a deliberately malformed record. Check not only output numbers but also whether the tool detects invalid assumptions and refuses silent corrections. When comparing results, include the reference assembly or database release, observation level, quality thresholds, removed records and a denominator for each proportion. Missing genomic measurements are not synonymous with confidently absent biological events. Explain which parts of the pipeline are deterministic transformations and which rely on empirical model assumptions.

### Fictional case and competing explanation

In a fictional family, two candidate variants appear on opposite parental haplotypes; treating them as cis would misrepresent possible functional consequences. This is a hypothetical instructional case, not a reported finding. Begin with one biological hypothesis and one technical or sampling rival. Before choosing the most interesting interpretation, write down what each hypothesis predicts about a newly collected specimen or orthogonal assay. Different algorithms may agree because they reuse the same flawed reference or measurement, not because they supply independent experimental confirmation.

### Worked example with units

**Problem:** Among 40 phased individuals, 12 carry a named haplotype: sample frequency is 0.30, but haplotype-copy frequency needs a different denominator.

**Calculation:** `12/40` = **0.3 fraction of sampled individuals** for the invented inputs. Keep the mathematical result separate from the scientific inference. Many arithmetic relations hold exactly under their definitions while the relationship between the calculated statistic and underlying biology remains conditional. Correct arithmetic validates a calculation, but it does not establish that the input data are representative or that the result has a causal meaning. Record whether the denominator counts bases, reads, allele copies, individuals, loci or experimental runs. Recompute with a modified hypothetical input to examine numerical sensitivity.

### Error modes and validation design

An LD coefficient cannot establish that two alleles sit on one individual chromosome in a particular person; population correlation and sample-specific phase differ. Consider whether the strongest-looking pattern comes from a feature selected after inspecting the answer. Exploratory selection followed by an unadjusted confirmatory claim can overstate reproducibility. **Audit emphasis — State the reference.** Describe what counts as a matching coordinate, allele or feature under the selected reference. Changing a reference can change apparent variants or gene boundaries while the original material remains unchanged.

Compare read-backed and pedigree-based phasing, record switches and cross-check whether allele transmission matches the inferred chromosome copies. The proposed new evidence should help discriminate between mechanisms rather than merely producing another version of the same computational score. Explain the important negative control and a result that would weaken your preferred hypothesis. In a scientific report, keep measurements, computed statistics, model-based predictions and proposed biological explanations in separate statements.

### Transfer exercise

Connect **Haplotype blocks, linkage and allele phase** with **Variant prioritization and validation**. Explain which source-data error would contaminate both topics and how a reference-aware provenance record would reveal it. Then answer: What was measured? How was the statistic calculated? What competing explanation remains? What independent experiment would be most efficient? Present the final inference as a conditional claim whose strength matches the available evidence.

---

## Lesson 4.5 — Variant prioritization and validation

### Mechanism and what can be inferred

Biological relevance is inferred by combining rarity, evolutionary conservation, predicted consequence, segregation and direct functional evidence. Prediction scores can rank hypotheses but do not convert uncertain changes into diagnoses. Identify the physical material, the instrument observation and the computational summary separately. This prevents a dataset label from being mistaken for the underlying biological process. The central question is **What genomic differences exist and how confidently can they be called?** Interpret that question in the limited context of the named species, specimens and assay; do not extrapolate from one sequence representation to all individuals.

### Measurement contract and analytical method

Predeclare filtering rules and investigate how ancestry, technical callability and transcript choice affect each ranking. Keep candidate status separate from evidence classification and actionability. For a transparent analysis, make two small tables: one describing source specimens and assays, and another describing computational transformations. The join keys should let another investigator trace a number back to its input without revealing restricted personal information. When comparing results, include the reference assembly or database release, observation level, quality thresholds, removed records and a denominator for each proportion. Missing genomic measurements are not synonymous with confidently absent biological events. Explain which parts of the pipeline are deterministic transformations and which rely on empirical model assumptions.

### Fictional case and competing explanation

A fictional candidate list shrinks from 800 variants to 20 after depth and consequence filters; a student incorrectly calls the first item pathogenic merely because it has the highest score. This is a hypothetical instructional case, not a reported finding. Begin with one biological hypothesis and one technical or sampling rival. Before choosing the most interesting interpretation, write down what each hypothesis predicts about a newly collected specimen or orthogonal assay. Different algorithms may agree because they reuse the same flawed reference or measurement, not because they supply independent experimental confirmation.

### Worked example with units

**Problem:** A filter retaining 20 of 800 initial records retains 2.5%; the 97.5% reduction is not proof of increased clinical truth.

**Calculation:** `20/800*100` = **2.5 %** for the invented inputs. Make a small companion table with the original fictional inputs, one alternative input value, the new result and a sentence describing whether the qualitative conclusion survives. Correct arithmetic validates a calculation, but it does not establish that the input data are representative or that the result has a causal meaning. Record whether the denominator counts bases, reads, allele copies, individuals, loci or experimental runs. Recompute with a modified hypothetical input to examine numerical sensitivity.

### Error modes and validation design

A rare variant is not automatically harmful; variant databases may underrepresent some populations and computational predictions can share training data. Explain how an earlier-stage error could propagate through several downstream analyses and create apparently consistent output. Correlation among derived reports should never substitute for documented source integrity. **Audit emphasis — Test the missingness.** Identify which observations were never sampled, lost in preparation, removed by filters or assigned ambiguous labels. A blank value and a confident absence are fundamentally different statements.

Blind-review several candidates, compare against independent functional data and quantify how rankings change under different defensible thresholds. The proposed new evidence should help discriminate between mechanisms rather than merely producing another version of the same computational score. Explain the important negative control and a result that would weaken your preferred hypothesis. In a scientific report, keep measurements, computed statistics, model-based predictions and proposed biological explanations in separate statements.

### Transfer exercise

Connect **Variant prioritization and validation** with **Haplotype blocks, linkage and allele phase**. Explain which source-data error would contaminate both topics and how a reference-aware provenance record would reveal it. Then answer: What was measured? How was the statistic calculated? What competing explanation remains? What independent experiment would be most efficient? Present the final inference as a conditional claim whose strength matches the available evidence.

---

## Unit 04 capstone — Variant interpretation under reference bias

### Situation and materials

A fictional family dataset contains four candidate small variants, one copy-number region and a phased two-site haplotype. Different aligners disagree at a repeat-associated site. Assume all records are fabricated for the classroom. Start by listing the observational units: organism, donor, biological preparation, technical library, genomic site or algorithmic summary. This is a crucial step because denominator mistakes can produce a result that is mathematically correct but scientifically misleading. Fix the reference and analysis version for the exercise before comparing any numbers, and include unknowns explicitly.

### Procedure and minimum outputs

Normalize alleles on a frozen reference, report callable depth and read quality, and distinguish candidate identification from functional and clinical interpretation. Produce a separate table for small variants, dosage and rearrangements. Your calculations need not be complicated. They should be completely reproducible, with input values, a visible formula, arithmetic and units. Create one well-documented table for the observations, a second for transformations, and a third for which interpretations survive each quality check. Explain the transformations in words rather than copying a tool output without explanation. Before choosing a cutoff, describe the costs of false positive and false negative findings in this particular fictional study.

### Competing hypotheses and sensitivity experiment

Re-run a thought experiment using another reference path and test how call concordance and evidence strength change. Preserve missing or ambiguous events rather than converting them to reference homozygotes. Your favored explanation should generate a prediction that would be less likely under a clearly named alternative. Design one sensitivity exercise that changes a single assumption—such as callable regions, phase, ancestry strata, normalization rule or depth threshold—and track its effect on the main statistic. If the preferred interpretation changes, report that dependence rather than selecting the setting with the most dramatic result. Explain which new specimen, assay or observation would provide the best independent discrimination.

### Deliverables, reflection and peer review

Submit a transparent evidence ledger and a list of observations needed for independent confirmation; do not issue clinical classifications. In addition, prepare a reproducibility manifest with input identifiers, simulated-only status, calculations, method version and a short rationale for every excluded observation. Include a four-sentence abstract distinguishing what is measured, estimated, hypothesized and still unknown. Exchange reports with another learner, ask them to recalculate at least one statistic using only the supplied source data, and record one objection that improves the design. Do not describe any result as clinical, diagnostic or measured in the real world.

### Challenge questions for synthesis

1. Which dataset field would have the greatest impact if it were silently mislabeled? Identify a simple audit that could catch the mistake before modeling.
2. Does the unit's central conclusion rely on random sampling, correct genome representation, accurate molecular classification or independent replication? Rank those assumptions in importance for this case.
3. What result could falsify the leading explanation without proving every alternative? Discuss the distinction between rejection of one hypothesis and proof of another.
4. If your method produced a visually excellent plot from copied or confounded measurements, what independent check would you demand before publication?
5. Explain why the precise mathematical result alone does not certify the biological or social validity of the research conclusion.

---

## Two interactive teaching models

Change each slider, observe its graph and record which assumptions make the formula valid. These are hypothetical mathematical demonstrations, not empirical sequence analyses.

### Model 4.1: Observed alternate-read fraction

**Equation:** VAF=alternate/total. **Caveat:** VAF does not equal clonal cell fraction. Change the independent parameter, then explain whether the output change is a simple mathematical consequence or requires a biological inference. A monotone visual trend is not automatically a causal biological law. Identify the units and what is held constant.

### Model 4.2: Copy count per diploid reference locus

**Equation:** Frequency=allele copies/200. **Caveat:** Assumes all calls complete and diploid. Change the independent parameter, then explain whether the output change is a simple mathematical consequence or requires a biological inference. A monotone visual trend is not automatically a causal biological law. Identify the units and what is held constant.
