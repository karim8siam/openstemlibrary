# Unit 06 — Population, comparative and evolutionary genomics

> **OpenSTEM Genomics · Book 16 · Editorial teaching draft.** All worked case data and investigations are synthetic. The interactive models describe simplified mathematical relations, not diagnoses or empirical genomic claims.

## Central scientific question

**Which genomic patterns reflect ancestry, demography, selection or technical confounding?**

### Conceptual context and how the five lessons fit

Genomes record evolutionary processes, but interpretation is conditional on sample composition and demographic history. Allele frequencies and linked markers change through drift, migration, recombination and selection. Related individuals and geographic stratification can generate associations even without a causal locus effect. Comparative analyses add the difficulty of separating orthologs, paralogs, lineage-specific losses and incomplete assemblies. This unit develops coherent reasoning from genotype counts through LD and GWAS to conserved gene order and selection signals. An evolutionary story should make discriminating predictions and compare plausible demographic or technical alternatives, rather than attributing every extreme statistic to natural selection.

### A running case to reason through

A local plant population exhibits a steep allele-frequency gradient that might reflect geography, selection or sample collection. The proposed explanation should remain a working hypothesis until both the measurement process and alternative biological accounts have been examined. Identify a plausible negative control, a sample identity verification and a condition in which the preferred model might fail. A final plot can be numerically precise while its biological conclusion is uncertain; your task is to make that uncertainty visible rather than treating it as a defect.

### Unit learning objectives

By the end of this unit, you should be able to reconstruct the data assumptions behind each of the five main topics, reproduce their toy calculations, distinguish technical and biological replication, identify a rival explanation for an apparent signal, and propose an independent measurement that would strengthen or challenge the inference. For each numerical answer, know the denominator, its unit and the simplifications required. Give yourself permission to conclude "not established" when appropriate.

### Study route

Read the five lessons in order. Each starts with an operational definition, moves through a fictional case and a worked calculation, then challenges the tempting inference. Compute the numbers by hand before using code. Finish with the unit capstone and the interactive model questions. Learning genomics requires deciding which questions an assay can answer at least as much as mastering the associated algorithm.

---

## Lesson 6.1 — Allele frequencies and Hardy–Weinberg checks

### Mechanism and what can be inferred

Allele-frequency estimates depend on sampling and genotype calling. Hardy–Weinberg proportions provide a model benchmark for randomly mating diploid populations under simplifying assumptions, not a universal law for all loci. Identify the physical material, the instrument observation and the computational summary separately. This prevents a dataset label from being mistaken for the underlying biological process. The central question is **Which genomic patterns reflect ancestry, demography, selection or technical confounding?** Interpret that question in the limited context of the named species, specimens and assay; do not extrapolate from one sequence representation to all individuals.

### Measurement contract and analytical method

Count allele copies in callable diploid individuals, account for missing genotypes and compare observed versus expected genotype proportions under a clearly defined population model. For a transparent analysis, make two small tables: one describing source specimens and assays, and another describing computational transformations. The join keys should let another investigator trace a number back to its input without revealing restricted personal information. When comparing results, include the reference assembly or database release, observation level, quality thresholds, removed records and a denominator for each proportion. Missing genomic measurements are not synonymous with confidently absent biological events. Explain which parts of the pipeline are deterministic transformations and which rely on empirical model assumptions.

### Fictional case and competing explanation

A fictional wildflower cohort includes 20 AA, 50 Aa and 30 aa plants, yielding allele A count 90 among 200 copies; subpopulation pooling may explain deviations. This is a hypothetical instructional case, not a reported finding. Begin with one biological hypothesis and one technical or sampling rival. Before choosing the most interesting interpretation, write down what each hypothesis predicts about a newly collected specimen or orthogonal assay. Different algorithms may agree because they reuse the same flawed reference or measurement, not because they supply independent experimental confirmation.

### Worked example with units

**Problem:** For 20 AA, 50 Aa and 30 aa, A frequency is (2×20+50)/(2×100)=0.45.

**Calculation:** `(2*20+50)/(2*100)` = **0.45 A allele frequency** for the invented inputs. Keep the mathematical result separate from the scientific inference. Many arithmetic relations hold exactly under their definitions while the relationship between the calculated statistic and underlying biology remains conditional. Correct arithmetic validates a calculation, but it does not establish that the input data are representative or that the result has a causal meaning. Record whether the denominator counts bases, reads, allele copies, individuals, loci or experimental runs. Recompute with a modified hypothetical input to examine numerical sensitivity.

### Error modes and validation design

Sequencing errors, selection, nonrandom mating and population substructure can all affect observed proportions; deviation does not uniquely identify one cause. Explain how an earlier-stage error could propagate through several downstream analyses and create apparently consistent output. Correlation among derived reports should never substitute for documented source integrity. **Audit emphasis — Examine independence.** Ask whether repeated observations came from distinct biological sources or from technical processing of the same material. A thousand reads from one library can improve measurement precision without creating a thousand independent organisms.

Analyze subpopulations separately, test genotype-quality sensitivity and check whether inferred frequencies are stable across sampling locations. The proposed new evidence should help discriminate between mechanisms rather than merely producing another version of the same computational score. Explain the important negative control and a result that would weaken your preferred hypothesis. In a scientific report, keep measurements, computed statistics, model-based predictions and proposed biological explanations in separate statements.

### Transfer exercise

Connect **Allele frequencies and Hardy–Weinberg checks** with **Linkage disequilibrium and recombination maps**. Explain which source-data error would contaminate both topics and how a reference-aware provenance record would reveal it. Then answer: What was measured? How was the statistic calculated? What competing explanation remains? What independent experiment would be most efficient? Present the final inference as a conditional claim whose strength matches the available evidence.

---

## Lesson 6.2 — Linkage disequilibrium and recombination maps

### Mechanism and what can be inferred

Linkage disequilibrium summarizes nonrandom association among alleles; its decay depends on recombination, population history, drift and selection. Distance in bases is not interchangeable with distance in centimorgans. Identify the physical material, the instrument observation and the computational summary separately. This prevents a dataset label from being mistaken for the underlying biological process. The central question is **Which genomic patterns reflect ancestry, demography, selection or technical confounding?** Interpret that question in the limited context of the named species, specimens and assay; do not extrapolate from one sequence representation to all individuals.

### Measurement contract and analytical method

Estimate LD only for clearly defined populations with adequate sample size and phased or probabilistically treated genotypes. Report allele frequencies and a precise statistic such as r². Preregister an analysis comparison in plain language: what signal is sought, which confounders are anticipated, how filtering will work, which readouts matter, and what observation would count against the favored interpretation. When comparing results, include the reference assembly or database release, observation level, quality thresholds, removed records and a denominator for each proportion. Missing genomic measurements are not synonymous with confidently absent biological events. Explain which parts of the pipeline are deterministic transformations and which rely on empirical model assumptions.

### Fictional case and competing explanation

In an invented field experiment, a marker pair 10 kb apart shows stronger LD in one population than another despite comparable physical distance. This is a hypothetical instructional case, not a reported finding. Begin with one biological hypothesis and one technical or sampling rival. Before choosing the most interesting interpretation, write down what each hypothesis predicts about a newly collected specimen or orthogonal assay. Different algorithms may agree because they reuse the same flawed reference or measurement, not because they supply independent experimental confirmation.

### Worked example with units

**Problem:** For recombination fraction θ=0.08, genetic distance is approximately 8 cM in the small-distance approximation, not 8 million bases.

**Calculation:** `0.08*100` = **8 approximate cM** for the invented inputs. Make a small companion table with the original fictional inputs, one alternative input value, the new result and a sentence describing whether the qualitative conclusion survives. Correct arithmetic validates a calculation, but it does not establish that the input data are representative or that the result has a causal meaning. Record whether the denominator counts bases, reads, allele copies, individuals, loci or experimental runs. Recompute with a modified hypothetical input to examine numerical sensitivity.

### Error modes and validation design

A high r² can occur from shared ancestry rather than direct molecular interaction, and allele-frequency imbalance changes statistical bounds. Ask which alternative assay or independent group could challenge the finding. Repeating a computation under different colors or with another software package is not independent biological replication. **Audit emphasis — State the reference.** Describe what counts as a matching coordinate, allele or feature under the selected reference. Changing a reference can change apparent variants or gene boundaries while the original material remains unchanged.

Recompute LD after ancestry stratification and use genetic-map estimates to evaluate long-range association patterns. The proposed new evidence should help discriminate between mechanisms rather than merely producing another version of the same computational score. Explain the important negative control and a result that would weaken your preferred hypothesis. In a scientific report, keep measurements, computed statistics, model-based predictions and proposed biological explanations in separate statements.

### Transfer exercise

Connect **Linkage disequilibrium and recombination maps** with **Genome-wide association designs and confounding**. Explain which source-data error would contaminate both topics and how a reference-aware provenance record would reveal it. Then answer: What was measured? How was the statistic calculated? What competing explanation remains? What independent experiment would be most efficient? Present the final inference as a conditional claim whose strength matches the available evidence.

---

## Lesson 6.3 — Genome-wide association designs and confounding

### Mechanism and what can be inferred

GWAS tests marker–trait associations across genomes; ancestry, relatedness, environmental factors and selection into the study can generate confounded signals. An association locus may tag rather than cause a trait difference. Identify the physical material, the instrument observation and the computational summary separately. This prevents a dataset label from being mistaken for the underlying biological process. The central question is **Which genomic patterns reflect ancestry, demography, selection or technical confounding?** Interpret that question in the limited context of the named species, specimens and assay; do not extrapolate from one sequence representation to all individuals.

### Measurement contract and analytical method

Prespecify phenotype definitions, covariates, quality thresholds and correction for multiple testing. Use suitable kinship-aware models and independent replication populations when possible. Write a data dictionary before invoking a tool. It should specify permitted values, missing-data codes, identity keys, coordinate conventions, and a worked input-output example whose result can be checked without proprietary software. When comparing results, include the reference assembly or database release, observation level, quality thresholds, removed records and a denominator for each proportion. Missing genomic measurements are not synonymous with confidently absent biological events. Explain which parts of the pipeline are deterministic transformations and which rely on empirical model assumptions.

### Fictional case and competing explanation

A fictional crop GWAS finds a striking association with drought survival that vanishes after adjusting for growing-site geography. This is a hypothetical instructional case, not a reported finding. Begin with one biological hypothesis and one technical or sampling rival. Before choosing the most interesting interpretation, write down what each hypothesis predicts about a newly collected specimen or orthogonal assay. Different algorithms may agree because they reuse the same flawed reference or measurement, not because they supply independent experimental confirmation.

### Worked example with units

**Problem:** Bonferroni threshold for 10,000 tests at family-wise alpha 0.05 equals 5×10^(−6), a deliberately conservative bound.

**Calculation:** `0.05/10_000` = **5e-06 Bonferroni threshold** for the invented inputs. Keep the mathematical result separate from the scientific inference. Many arithmetic relations hold exactly under their definitions while the relationship between the calculated statistic and underlying biology remains conditional. Correct arithmetic validates a calculation, but it does not establish that the input data are representative or that the result has a causal meaning. Record whether the denominator counts bases, reads, allele copies, individuals, loci or experimental runs. Recompute with a modified hypothetical input to examine numerical sensitivity.

### Error modes and validation design

The smallest p-value need not identify the causal gene, and using the discovery cohort to pick features and then claim validation gives circular evidence. If the measurement was duplicated at the technical level, name the correct independent sampling level before offering any significance claim. Replication improves confidence only to the extent that it samples the relevant biological variability. **Audit emphasis — Test the missingness.** Identify which observations were never sampled, lost in preparation, removed by filters or assigned ambiguous labels. A blank value and a confident absence are fundamentally different statements.

Compare nested models with and without measured environmental covariates, perform calibration checks and confirm lead signals in independent plots or cohorts. The proposed new evidence should help discriminate between mechanisms rather than merely producing another version of the same computational score. Explain the important negative control and a result that would weaken your preferred hypothesis. In a scientific report, keep measurements, computed statistics, model-based predictions and proposed biological explanations in separate statements.

### Transfer exercise

Connect **Genome-wide association designs and confounding** with **Comparative genomics, synteny and duplication**. Explain which source-data error would contaminate both topics and how a reference-aware provenance record would reveal it. Then answer: What was measured? How was the statistic calculated? What competing explanation remains? What independent experiment would be most efficient? Present the final inference as a conditional claim whose strength matches the available evidence.

---

## Lesson 6.4 — Comparative genomics, synteny and duplication

### Mechanism and what can be inferred

Shared gene order across lineages can indicate conserved chromosome blocks; duplication, rearrangement and lineage-specific losses complicate one-to-one ortholog assignment. Paralogy and orthology are evolutionary relationships. Identify the physical material, the instrument observation and the computational summary separately. This prevents a dataset label from being mistaken for the underlying biological process. The central question is **Which genomic patterns reflect ancestry, demography, selection or technical confounding?** Interpret that question in the limited context of the named species, specimens and assay; do not extrapolate from one sequence representation to all individuals.

### Measurement contract and analytical method

Compare annotation versions and gene-family phylogenies before reporting conserved blocks. Evaluate whether assembly gaps or poor gene predictions could imitate gene loss. Reconstruct the reasoning as an evidence ledger with separate columns for raw measurement, model choice, calculated value, alternative explanation and validation status. Avoid merging uncertain evidence into one unexplained confidence label. When comparing results, include the reference assembly or database release, observation level, quality thresholds, removed records and a denominator for each proportion. Missing genomic measurements are not synonymous with confidently absent biological events. Explain which parts of the pipeline are deterministic transformations and which rely on empirical model assumptions.

### Fictional case and competing explanation

A fictional genome comparison finds a cluster of four related transport genes in one species but two copies in another; copy counts alone cannot reveal the timing of duplication. This is a hypothetical instructional case, not a reported finding. Begin with one biological hypothesis and one technical or sampling rival. Before choosing the most interesting interpretation, write down what each hypothesis predicts about a newly collected specimen or orthogonal assay. Different algorithms may agree because they reuse the same flawed reference or measurement, not because they supply independent experimental confirmation.

### Worked example with units

**Problem:** If 72 of 90 sampled anchor-gene pairs preserve local order, observed synteny retention is 80%, under the stated matching rule.

**Calculation:** `72/90*100` = **80 %** for the invented inputs. Make a small companion table with the original fictional inputs, one alternative input value, the new result and a sentence describing whether the qualitative conclusion survives. Correct arithmetic validates a calculation, but it does not establish that the input data are representative or that the result has a causal meaning. Record whether the denominator counts bases, reads, allele copies, individuals, loci or experimental runs. Recompute with a modified hypothetical input to examine numerical sensitivity.

### Error modes and validation design

High sequence identity does not establish orthology if a recent duplication created close paralogs within a lineage. Consider whether the strongest-looking pattern comes from a feature selected after inspecting the answer. Exploratory selection followed by an unadjusted confirmatory claim can overstate reproducibility. **Audit emphasis — Inspect the mechanism.** Link the measured molecular signal to a plausible process and identify where the causal arrow is merely assumed. Correlated regulatory, evolutionary or clinical features can have shared upstream causes.

Build a rooted gene-family hypothesis, inspect neighboring conserved genes and test whether broader species sampling changes duplication placement. The proposed new evidence should help discriminate between mechanisms rather than merely producing another version of the same computational score. Explain the important negative control and a result that would weaken your preferred hypothesis. In a scientific report, keep measurements, computed statistics, model-based predictions and proposed biological explanations in separate statements.

### Transfer exercise

Connect **Comparative genomics, synteny and duplication** with **Selection scans and demographic alternatives**. Explain which source-data error would contaminate both topics and how a reference-aware provenance record would reveal it. Then answer: What was measured? How was the statistic calculated? What competing explanation remains? What independent experiment would be most efficient? Present the final inference as a conditional claim whose strength matches the available evidence.

---

## Lesson 6.5 — Selection scans and demographic alternatives

### Mechanism and what can be inferred

Allele-frequency spectra, extended haplotypes and divergence patterns may signal natural selection, but bottlenecks, admixture and variable recombination can imitate several signatures. Identify the physical material, the instrument observation and the computational summary separately. This prevents a dataset label from being mistaken for the underlying biological process. The central question is **Which genomic patterns reflect ancestry, demography, selection or technical confounding?** Interpret that question in the limited context of the named species, specimens and assay; do not extrapolate from one sequence representation to all individuals.

### Measurement contract and analytical method

Simulate neutral demographic nulls with explicit assumptions and compare results across genomic windows that differ in recombination and callability. Create a tiny independent benchmark that contains an ordinary case, an ambiguous boundary case and a deliberately malformed record. Check not only output numbers but also whether the tool detects invalid assumptions and refuses silent corrections. When comparing results, include the reference assembly or database release, observation level, quality thresholds, removed records and a denominator for each proportion. Missing genomic measurements are not synonymous with confidently absent biological events. Explain which parts of the pipeline are deterministic transformations and which rely on empirical model assumptions.

### Fictional case and competing explanation

A fictional island bird population shows a low-diversity region near a plumage locus; the population recently experienced a founder event. This is a hypothetical instructional case, not a reported finding. Begin with one biological hypothesis and one technical or sampling rival. Before choosing the most interesting interpretation, write down what each hypothesis predicts about a newly collected specimen or orthogonal assay. Different algorithms may agree because they reuse the same flawed reference or measurement, not because they supply independent experimental confirmation.

### Worked example with units

**Problem:** An observed heterozygosity estimate of 0.12 versus 0.20 in a matched background is 40% lower relative to 0.20; it does not establish selection.

**Calculation:** `(0.20-0.12)/0.20*100` = **40 % lower** for the invented inputs. Keep the mathematical result separate from the scientific inference. Many arithmetic relations hold exactly under their definitions while the relationship between the calculated statistic and underlying biology remains conditional. Correct arithmetic validates a calculation, but it does not establish that the input data are representative or that the result has a causal meaning. Record whether the denominator counts bases, reads, allele copies, individuals, loci or experimental runs. Recompute with a modified hypothetical input to examine numerical sensitivity.

### Error modes and validation design

Describing a region as positively selected from one statistic alone risks conflating historical demography with locus-specific adaptation. Explain how an earlier-stage error could propagate through several downstream analyses and create apparently consistent output. Correlation among derived reports should never substitute for documented source integrity. **Audit emphasis — Protect the inferential boundary.** Separate an algorithmic score from a measurement and from an actionable interpretation. Showing that a model is internally consistent is not the same as validating its claims in a new cohort.

Compare multiple independent summaries, matched genomic backgrounds and environmental associations, and state which alternatives remain unresolved. The proposed new evidence should help discriminate between mechanisms rather than merely producing another version of the same computational score. Explain the important negative control and a result that would weaken your preferred hypothesis. In a scientific report, keep measurements, computed statistics, model-based predictions and proposed biological explanations in separate statements.

### Transfer exercise

Connect **Selection scans and demographic alternatives** with **Comparative genomics, synteny and duplication**. Explain which source-data error would contaminate both topics and how a reference-aware provenance record would reveal it. Then answer: What was measured? How was the statistic calculated? What competing explanation remains? What independent experiment would be most efficient? Present the final inference as a conditional claim whose strength matches the available evidence.

---

## Unit 06 capstone — Differentiating selection from population structure

### Situation and materials

A fictional species is sampled at three geographically separated sites, with marker genotype counts, a drought phenotype and simulated ancestral relationships. Assume all records are fabricated for the classroom. Start by listing the observational units: organism, donor, biological preparation, technical library, genomic site or algorithmic summary. This is a crucial step because denominator mistakes can produce a result that is mathematically correct but scientifically misleading. Fix the reference and analysis version for the exercise before comparing any numbers, and include unknowns explicitly.

### Procedure and minimum outputs

Calculate a selected allele frequency and a simple heterozygosity expectation, then evaluate how pooling sites changes equilibrium diagnostics. Distinguish population LD from physically linked causation. Your calculations need not be complicated. They should be completely reproducible, with input values, a visible formula, arithmetic and units. Create one well-documented table for the observations, a second for transformations, and a third for which interpretations survive each quality check. Explain the transformations in words rather than copying a tool output without explanation. Before choosing a cutoff, describe the costs of false positive and false negative findings in this particular fictional study.

### Competing hypotheses and sensitivity experiment

Design a comparison of a naive GWAS with a structure-aware model, and explain whether extreme haplotypes could also arise from recent founder events. Your favored explanation should generate a prediction that would be less likely under a clearly named alternative. Design one sensitivity exercise that changes a single assumption—such as callable regions, phase, ancestry strata, normalization rule or depth threshold—and track its effect on the main statistic. If the preferred interpretation changes, report that dependence rather than selecting the setting with the most dramatic result. Explain which new specimen, assay or observation would provide the best independent discrimination.

### Deliverables, reflection and peer review

Submit an alternative-hypotheses matrix, sensitivity table and independent replication design. In addition, prepare a reproducibility manifest with input identifiers, simulated-only status, calculations, method version and a short rationale for every excluded observation. Include a four-sentence abstract distinguishing what is measured, estimated, hypothesized and still unknown. Exchange reports with another learner, ask them to recalculate at least one statistic using only the supplied source data, and record one objection that improves the design. Do not describe any result as clinical, diagnostic or measured in the real world.

### Challenge questions for synthesis

1. Which dataset field would have the greatest impact if it were silently mislabeled? Identify a simple audit that could catch the mistake before modeling.
2. Does the unit's central conclusion rely on random sampling, correct genome representation, accurate molecular classification or independent replication? Rank those assumptions in importance for this case.
3. What result could falsify the leading explanation without proving every alternative? Discuss the distinction between rejection of one hypothesis and proof of another.
4. If your method produced a visually excellent plot from copied or confounded measurements, what independent check would you demand before publication?
5. Explain why the precise mathematical result alone does not certify the biological or social validity of the research conclusion.

---

## Two interactive teaching models

Change each slider, observe its graph and record which assumptions make the formula valid. These are hypothetical mathematical demonstrations, not empirical sequence analyses.

### Model 6.1: Expected heterozygote fraction under HWE

**Equation:** H=2p(1−p). **Caveat:** Idealized randomly mating diploid benchmark. Change the independent parameter, then explain whether the output change is a simple mathematical consequence or requires a biological inference. A monotone visual trend is not automatically a causal biological law. Identify the units and what is held constant.

### Model 6.2: Family-wise significance threshold

**Equation:** α/m with α=.05; m=1000x. **Caveat:** Conservative threshold under simple correction. Change the independent parameter, then explain whether the output change is a simple mathematical consequence or requires a biological inference. A monotone visual trend is not automatically a causal biological law. Identify the units and what is held constant.
