# Unit 01 — Genome architecture and reference representations

> **OpenSTEM Genomics · Book 16 · Editorial teaching draft.** All worked case data and investigations are synthetic. The interactive models describe simplified mathematical relations, not diagnoses or empirical genomic claims.

## Central scientific question

**What is being counted when investigators say that an organism has a genome?**

### Conceptual context and how the five lessons fit

A genome is not equivalent to a FASTA file, a haploid length estimate, a reference chromosome or a list of gene symbols. Each of these is a representation created by making assumptions about a specimen and a measurement process. In eukaryotes, DNA is arranged among multiple nuclear chromosomes and can also reside in mitochondria or chloroplasts. In microbes, plasmids and genome rearrangements challenge the idea of one immutable canonical sequence. The first responsibility of a genomic scientist is to state exactly what biological object is being represented. In this unit, the five lessons progress from genome content through chromosome structure and transcript architecture to repeated sequence and reference choices. Think of assembly quality and annotation quality as distinct axes. A genome can be nearly complete yet incorrectly annotated, and a high-quality gene model can exist in a reference missing much of a population's structural diversity.

### A running case to reason through

A comparative project mixes diploid plants, microbial isolates and tumor subclones; a single genome size or gene count is not a meaningful universal quality score. The proposed explanation should remain a working hypothesis until both the measurement process and alternative biological accounts have been examined. Identify a plausible negative control, a sample identity verification and a condition in which the preferred model might fail. A final plot can be numerically precise while its biological conclusion is uncertain; your task is to make that uncertainty visible rather than treating it as a defect.

### Unit learning objectives

By the end of this unit, you should be able to reconstruct the data assumptions behind each of the five main topics, reproduce their toy calculations, distinguish technical and biological replication, identify a rival explanation for an apparent signal, and propose an independent measurement that would strengthen or challenge the inference. For each numerical answer, know the denominator, its unit and the simplifications required. Give yourself permission to conclude "not established" when appropriate.

### Study route

Read the five lessons in order. Each starts with an operational definition, moves through a fictional case and a worked calculation, then challenges the tempting inference. Compute the numbers by hand before using code. Finish with the unit capstone and the interactive model questions. Learning genomics requires deciding which questions an assay can answer at least as much as mastering the associated algorithm.

---

## Lesson 1.1 — Genome composition, ploidy and C-value

### Mechanism and what can be inferred

A haploid complement is one chromosome set; genome size depends on ploidy, organellar compartments, repeated DNA and what physical state is quantified. Gene number does not increase proportionally with DNA mass, the classical C-value paradox. Identify the physical material, the instrument observation and the computational summary separately. This prevents a dataset label from being mistaken for the underlying biological process. The central question is **What is being counted when investigators say that an organism has a genome?** Interpret that question in the limited context of the named species, specimens and assay; do not extrapolate from one sequence representation to all individuals.

### Measurement contract and analytical method

Report whether a value is a haploid nuclear estimate, diploid nuclear content or total DNA including organelles. Document species, life stage, cell cycle, tissue, method and uncertainty before dividing DNA content by a base-pair conversion factor. For a transparent analysis, make two small tables: one describing source specimens and assays, and another describing computational transformations. The join keys should let another investigator trace a number back to its input without revealing restricted personal information. When comparing results, include the reference assembly or database release, observation level, quality thresholds, removed records and a denominator for each proportion. Missing genomic measurements are not synonymous with confidently absent biological events. Explain which parts of the pipeline are deterministic transformations and which rely on empirical model assumptions.

### Fictional case and competing explanation

Fictional algae species A and B have similar annotated protein-coding gene numbers, yet B carries threefold more nuclear DNA. Inspect long intergenic and repeat-rich regions before declaring that one organism has more biological complexity. This is a hypothetical instructional case, not a reported finding. Begin with one biological hypothesis and one technical or sampling rival. Before choosing the most interesting interpretation, write down what each hypothesis predicts about a newly collected specimen or orthogonal assay. Different algorithms may agree because they reuse the same flawed reference or measurement, not because they supply independent experimental confirmation.

### Worked example with units

**Problem:** Compute a haploid estimate as diploid nuclear DNA of 1.6 pg divided by two; report 0.8 pg, not an asserted gene count.

**Calculation:** `1.6/2` = **0.8 pg** for the invented inputs. Check the unit, sign, scale and rounding of the calculated answer. Where a proportion is involved, state whether the result counts reads, alleles, individuals, transcripts, genomic sites or publications; those denominators are not interchangeable. Correct arithmetic validates a calculation, but it does not establish that the input data are representative or that the result has a causal meaning. Record whether the denominator counts bases, reads, allele copies, individuals, loci or experimental runs. Recompute with a modified hypothetical input to examine numerical sensitivity.

### Error modes and validation design

Treating flow-cytometric fluorescence as base pairs without standards or treating polyploid read depth as diploid depth creates misleading genome-size comparisons. If the measurement was duplicated at the technical level, name the correct independent sampling level before offering any significance claim. Replication improves confidence only to the extent that it samples the relevant biological variability. **Audit emphasis — Begin with the denominator.** First write the total that would make a reported fraction equal to one: all molecules, all individuals, all reference positions or all interrogated loci. A percentage cannot be compared across studies if the denominators are inconsistent.

Compare a calibrated nuclear DNA assay with a k-mer genome-size estimate using replicate preparations and a ploidy-aware model; large disagreement motivates sample-identity and repeat-content checks. The proposed new evidence should help discriminate between mechanisms rather than merely producing another version of the same computational score. Explain the important negative control and a result that would weaken your preferred hypothesis. In a scientific report, keep measurements, computed statistics, model-based predictions and proposed biological explanations in separate statements.

### Transfer exercise

Connect **Genome composition, ploidy and C-value** with **Chromosome architecture and centromeres**. Explain which source-data error would contaminate both topics and how a reference-aware provenance record would reveal it. Then answer: What was measured? How was the statistic calculated? What competing explanation remains? What independent experiment would be most efficient? Present the final inference as a conditional claim whose strength matches the available evidence.

---

## Lesson 1.2 — Chromosome architecture and centromeres

### Mechanism and what can be inferred

Chromosomes package DNA with chromatin; centromere specification is strongly influenced by specialized chromatin, while telomeres protect natural chromosome termini. Centromeric repeats and segmental duplications create difficult mapping regions. Identify the physical material, the instrument observation and the computational summary separately. This prevents a dataset label from being mistaken for the underlying biological process. The central question is **What is being counted when investigators say that an organism has a genome?** Interpret that question in the limited context of the named species, specimens and assay; do not extrapolate from one sequence representation to all individuals.

### Measurement contract and analytical method

Inspect chromosome-level evidence from cytogenetics, long DNA molecules and assembly paths. Separate chromosome number, topological placement, strand orientation and completeness of telomere-associated sequence as different assessments. Preregister an analysis comparison in plain language: what signal is sought, which confounders are anticipated, how filtering will work, which readouts matter, and what observation would count against the favored interpretation. When comparing results, include the reference assembly or database release, observation level, quality thresholds, removed records and a denominator for each proportion. Missing genomic measurements are not synonymous with confidently absent biological events. Explain which parts of the pipeline are deterministic transformations and which rely on empirical model assumptions.

### Fictional case and competing explanation

A fictional grass assembly has 14 labeled chromosomes but several suspicious joins near highly similar repeats. Supporting contact maps alone are insufficient if the mapping itself is ambiguous around rearrangements. This is a hypothetical instructional case, not a reported finding. Begin with one biological hypothesis and one technical or sampling rival. Before choosing the most interesting interpretation, write down what each hypothesis predicts about a newly collected specimen or orthogonal assay. Different algorithms may agree because they reuse the same flawed reference or measurement, not because they supply independent experimental confirmation.

### Worked example with units

**Problem:** For 14 chromosomes, a diploid somatic count of 28 is expected under ordinary diploidy; acknowledge exceptions such as aneuploid cells.

**Calculation:** `28/2` = **14 haploid chromosomes** for the invented inputs. To test your interpretation, change one input within a plausible synthetic range and recompute the output. The goal is not to fit actual organisms but to understand how measurement assumptions propagate through the equation. Correct arithmetic validates a calculation, but it does not establish that the input data are representative or that the result has a causal meaning. Record whether the denominator counts bases, reads, allele copies, individuals, loci or experimental runs. Recompute with a modified hypothetical input to examine numerical sensitivity.

### Error modes and validation design

A long scaffold can be misjoined; scaffold N50 cannot certify centromere localization or the physical orientation of repeated blocks. Consider whether the strongest-looking pattern comes from a feature selected after inspecting the answer. Exploratory selection followed by an unadjusted confirmatory claim can overstate reproducibility. **Audit emphasis — Examine independence.** Ask whether repeated observations came from distinct biological sources or from technical processing of the same material. A thousand reads from one library can improve measurement precision without creating a thousand independent organisms.

Compare independent linkage evidence, long-range maps and read support across boundaries, while preserving ambiguous unresolved repeat segments in the release notes. The proposed new evidence should help discriminate between mechanisms rather than merely producing another version of the same computational score. Explain the important negative control and a result that would weaken your preferred hypothesis. In a scientific report, keep measurements, computed statistics, model-based predictions and proposed biological explanations in separate statements.

### Transfer exercise

Connect **Chromosome architecture and centromeres** with **Gene structures, isoforms and noncoding DNA**. Explain which source-data error would contaminate both topics and how a reference-aware provenance record would reveal it. Then answer: What was measured? How was the statistic calculated? What competing explanation remains? What independent experiment would be most efficient? Present the final inference as a conditional claim whose strength matches the available evidence.

---

## Lesson 1.3 — Gene structures, isoforms and noncoding DNA

### Mechanism and what can be inferred

A genomic locus can produce different transcripts via alternative initiation, splicing and termination; promoter and enhancer function is context-dependent. Gene annotations depend on evidence and conventions, not on raw DNA alone. Identify the physical material, the instrument observation and the computational summary separately. This prevents a dataset label from being mistaken for the underlying biological process. The central question is **What is being counted when investigators say that an organism has a genome?** Interpret that question in the limited context of the named species, specimens and assay; do not extrapolate from one sequence representation to all individuals.

### Measurement contract and analytical method

Track assembly accession, genomic coordinate, strand, transcript ID and annotation release. Match exon chains and coding boundaries at transcript level rather than collapsing all RNA products to one simplified gene name. Write a data dictionary before invoking a tool. It should specify permitted values, missing-data codes, identity keys, coordinate conventions, and a worked input-output example whose result can be checked without proprietary software. When comparing results, include the reference assembly or database release, observation level, quality thresholds, removed records and a denominator for each proportion. Missing genomic measurements are not synonymous with confidently absent biological events. Explain which parts of the pipeline are deterministic transformations and which rely on empirical model assumptions.

### Fictional case and competing explanation

In an invented vertebrate specimen, a gene has three observed transcript isoforms but only one demonstrated protein product. Transcript counts must not be treated as independent genes or as confirmed protein isoforms. This is a hypothetical instructional case, not a reported finding. Begin with one biological hypothesis and one technical or sampling rival. Before choosing the most interesting interpretation, write down what each hypothesis predicts about a newly collected specimen or orthogonal assay. Different algorithms may agree because they reuse the same flawed reference or measurement, not because they supply independent experimental confirmation.

### Worked example with units

**Problem:** If one 2.4-kb transcript contains 1.5 kb coding sequence, the coding proportion is 62.5%, not 62.5% of the entire genome.

**Calculation:** `1.5/2.4*100` = **62.5 %** for the invented inputs. Check the unit, sign, scale and rounding of the calculated answer. Where a proportion is involved, state whether the result counts reads, alleles, individuals, transcripts, genomic sites or publications; those denominators are not interchangeable. Correct arithmetic validates a calculation, but it does not establish that the input data are representative or that the result has a causal meaning. Record whether the denominator counts bases, reads, allele copies, individuals, loci or experimental runs. Recompute with a modified hypothetical input to examine numerical sensitivity.

### Error modes and validation design

Assuming every predicted open reading frame is a functional gene or interpreting noncoding DNA as universally inactive confuses classification with measurement. Explain how an earlier-stage error could propagate through several downstream analyses and create apparently consistent output. Correlation among derived reports should never substitute for documented source integrity. **Audit emphasis — State the reference.** Describe what counts as a matching coordinate, allele or feature under the selected reference. Changing a reference can change apparent variants or gene boundaries while the original material remains unchanged.

Compare RNA evidence from different tissues with curated splice junctions; test whether observed isoforms are robust to library preparation and mapping ambiguity. The proposed new evidence should help discriminate between mechanisms rather than merely producing another version of the same computational score. Explain the important negative control and a result that would weaken your preferred hypothesis. In a scientific report, keep measurements, computed statistics, model-based predictions and proposed biological explanations in separate statements.

### Transfer exercise

Connect **Gene structures, isoforms and noncoding DNA** with **Repetitive elements and genome plasticity**. Explain which source-data error would contaminate both topics and how a reference-aware provenance record would reveal it. Then answer: What was measured? How was the statistic calculated? What competing explanation remains? What independent experiment would be most efficient? Present the final inference as a conditional claim whose strength matches the available evidence.

---

## Lesson 1.4 — Repetitive elements and genome plasticity

### Mechanism and what can be inferred

Tandem repeats, transposable elements, simple repeats and segmental duplications account for major fractions of many eukaryotic genomes. Different repeat classes arise through distinct mechanisms and have different consequences for assembly and regulation. Identify the physical material, the instrument observation and the computational summary separately. This prevents a dataset label from being mistaken for the underlying biological process. The central question is **What is being counted when investigators say that an organism has a genome?** Interpret that question in the limited context of the named species, specimens and assay; do not extrapolate from one sequence representation to all individuals.

### Measurement contract and analytical method

Specify repeat families, reference database, overlap rules and the proportion of ambiguous bases. Analyze both masked and unmasked sequence; estimate copy number while checking whether reads collapse among similar copies. Reconstruct the reasoning as an evidence ledger with separate columns for raw measurement, model choice, calculated value, alternative explanation and validation status. Avoid merging uncertain evidence into one unexplained confidence label. When comparing results, include the reference assembly or database release, observation level, quality thresholds, removed records and a denominator for each proportion. Missing genomic measurements are not synonymous with confidently absent biological events. Explain which parts of the pipeline are deterministic transformations and which rely on empirical model assumptions.

### Fictional case and competing explanation

A fictional moss genome contains 43% annotated repeat-masked sequence, much of which is made up of several old element families rather than active transposition. This is a hypothetical instructional case, not a reported finding. Begin with one biological hypothesis and one technical or sampling rival. Before choosing the most interesting interpretation, write down what each hypothesis predicts about a newly collected specimen or orthogonal assay. Different algorithms may agree because they reuse the same flawed reference or measurement, not because they supply independent experimental confirmation.

### Worked example with units

**Problem:** For 120 Mb assembled sequence with 45 Mb masked as repeats, masked fraction is 37.5%; the fraction is not a measure of recent transposition.

**Calculation:** `45/120*100` = **37.5 %** for the invented inputs. To test your interpretation, change one input within a plausible synthetic range and recompute the output. The goal is not to fit actual organisms but to understand how measurement assumptions propagate through the equation. Correct arithmetic validates a calculation, but it does not establish that the input data are representative or that the result has a causal meaning. Record whether the denominator counts bases, reads, allele copies, individuals, loci or experimental runs. Recompute with a modified hypothetical input to examine numerical sensitivity.

### Error modes and validation design

Repeat annotation is incomplete and database-dependent. Calling every repeat a harmful mutation, or assigning an element to a family from a single short motif, overstates evidence. Ask which alternative assay or independent group could challenge the finding. Repeating a computation under different colors or with another software package is not independent biological replication. **Audit emphasis — Test the missingness.** Identify which observations were never sampled, lost in preparation, removed by filters or assigned ambiguous labels. A blank value and a confident absence are fundamentally different statements.

Compare family-consensus alignments with de novo repeat discovery and inspect insertion-site support in independent libraries. The proposed new evidence should help discriminate between mechanisms rather than merely producing another version of the same computational score. Explain the important negative control and a result that would weaken your preferred hypothesis. In a scientific report, keep measurements, computed statistics, model-based predictions and proposed biological explanations in separate statements.

### Transfer exercise

Connect **Repetitive elements and genome plasticity** with **Reference assemblies and pangenome graphs**. Explain which source-data error would contaminate both topics and how a reference-aware provenance record would reveal it. Then answer: What was measured? How was the statistic calculated? What competing explanation remains? What independent experiment would be most efficient? Present the final inference as a conditional claim whose strength matches the available evidence.

---

## Lesson 1.5 — Reference assemblies and pangenome graphs

### Mechanism and what can be inferred

A linear reference is one representation of genome sequence, not the genotype of every member of a species. Graph pangenomes allow alternate sequence paths and can represent complex variation that cannot be expressed by a simple linear coordinate alone. Identify the physical material, the instrument observation and the computational summary separately. This prevents a dataset label from being mistaken for the underlying biological process. The central question is **What is being counted when investigators say that an organism has a genome?** Interpret that question in the limited context of the named species, specimens and assay; do not extrapolate from one sequence representation to all individuals.

### Measurement contract and analytical method

Use stable assembly identifiers, graph or linear representation version, mapping path, coordinates and normalization convention. Test reference-bias sensitivity with alternate haplotypes and preserve the transformation log when converting coordinates. Create a tiny independent benchmark that contains an ordinary case, an ambiguous boundary case and a deliberately malformed record. Check not only output numbers but also whether the tool detects invalid assumptions and refuses silent corrections. When comparing results, include the reference assembly or database release, observation level, quality thresholds, removed records and a denominator for each proportion. Missing genomic measurements are not synonymous with confidently absent biological events. Explain which parts of the pipeline are deterministic transformations and which rely on empirical model assumptions.

### Fictional case and competing explanation

Two fictional wheat accessions differ by a sizable insertion absent from the baseline line; linear reference mapping creates uneven read support near its breakpoint. This is a hypothetical instructional case, not a reported finding. Begin with one biological hypothesis and one technical or sampling rival. Before choosing the most interesting interpretation, write down what each hypothesis predicts about a newly collected specimen or orthogonal assay. Different algorithms may agree because they reuse the same flawed reference or measurement, not because they supply independent experimental confirmation.

### Worked example with units

**Problem:** Of 250 loci, 225 calls agree between mappings: concordance is 90%, conditional on loci measured by both pipelines.

**Calculation:** `225/250*100` = **90 %** for the invented inputs. Check the unit, sign, scale and rounding of the calculated answer. Where a proportion is involved, state whether the result counts reads, alleles, individuals, transcripts, genomic sites or publications; those denominators are not interchangeable. Correct arithmetic validates a calculation, but it does not establish that the input data are representative or that the result has a causal meaning. Record whether the denominator counts bases, reads, allele copies, individuals, loci or experimental runs. Recompute with a modified hypothetical input to examine numerical sensitivity.

### Error modes and validation design

A graph reference can also bias analysis if sampling is uneven and path choices are underdocumented; a graph does not make incomplete variation catalogs magically comprehensive. If the measurement was duplicated at the technical level, name the correct independent sampling level before offering any significance claim. Replication improves confidence only to the extent that it samples the relevant biological variability. **Audit emphasis — Inspect the mechanism.** Link the measured molecular signal to a plausible process and identify where the causal arrow is merely assumed. Correlated regulatory, evolutionary or clinical features can have shared upstream causes.

Contrast calls against two independently built references; measure call concordance separately for repeats and unique regions rather than taking one global percentage. The proposed new evidence should help discriminate between mechanisms rather than merely producing another version of the same computational score. Explain the important negative control and a result that would weaken your preferred hypothesis. In a scientific report, keep measurements, computed statistics, model-based predictions and proposed biological explanations in separate statements.

### Transfer exercise

Connect **Reference assemblies and pangenome graphs** with **Repetitive elements and genome plasticity**. Explain which source-data error would contaminate both topics and how a reference-aware provenance record would reveal it. Then answer: What was measured? How was the statistic calculated? What competing explanation remains? What independent experiment would be most efficient? Present the final inference as a conditional claim whose strength matches the available evidence.

---

## Unit 01 capstone — Reference audit of a fictional flowering plant

### Situation and materials

Build a mini-reference dossier for a hypothetical diploid plant with variable repeat burden. Your input consists of a nuclear size estimate, chromosome count, four simulated contigs, two transcript isoforms and a graph path differing by one insertion. Assume all records are fabricated for the classroom. Start by listing the observational units: organism, donor, biological preparation, technical library, genomic site or algorithmic summary. This is a crucial step because denominator mistakes can produce a result that is mathematically correct but scientifically misleading. Fix the reference and analysis version for the exercise before comparing any numbers, and include unknowns explicitly.

### Procedure and minimum outputs

Draw the hierarchy from specimen to chromosome to contig to gene and transcript. Annotate every number with organism, ploidy, assembly accession and physical unit. Check that a gene and its isoforms are not double counted. Your calculations need not be complicated. They should be completely reproducible, with input values, a visible formula, arithmetic and units. Create one well-documented table for the observations, a second for transformations, and a third for which interpretations survive each quality check. Explain the transformations in words rather than copying a tool output without explanation. Before choosing a cutoff, describe the costs of false positive and false negative findings in this particular fictional study.

### Competing hypotheses and sensitivity experiment

Change the assumed repeat percentage and ask which gene-count inference, if any, legitimately changes. Record what cannot be inferred from DNA mass, and compare the value of long-range evidence versus sequence alignment alone. Your favored explanation should generate a prediction that would be less likely under a clearly named alternative. Design one sensitivity exercise that changes a single assumption—such as callable regions, phase, ancestry strata, normalization rule or depth threshold—and track its effect on the main statistic. If the preferred interpretation changes, report that dependence rather than selecting the setting with the most dramatic result. Explain which new specimen, assay or observation would provide the best independent discrimination.

### Deliverables, reflection and peer review

Submit a one-page manifest, a reference-aware coordinate example and two competing explanations for an apparent structural difference. In addition, prepare a reproducibility manifest with input identifiers, simulated-only status, calculations, method version and a short rationale for every excluded observation. Include a four-sentence abstract distinguishing what is measured, estimated, hypothesized and still unknown. Exchange reports with another learner, ask them to recalculate at least one statistic using only the supplied source data, and record one objection that improves the design. Do not describe any result as clinical, diagnostic or measured in the real world.

### Challenge questions for synthesis

1. Which dataset field would have the greatest impact if it were silently mislabeled? Identify a simple audit that could catch the mistake before modeling.
2. Does the unit's central conclusion rely on random sampling, correct genome representation, accurate molecular classification or independent replication? Rank those assumptions in importance for this case.
3. What result could falsify the leading explanation without proving every alternative? Discuss the distinction between rejection of one hypothesis and proof of another.
4. If your method produced a visually excellent plot from copied or confounded measurements, what independent check would you demand before publication?
5. Explain why the precise mathematical result alone does not certify the biological or social validity of the research conclusion.

---

## Two interactive teaching models

Change each slider, observe its graph and record which assumptions make the formula valid. These are hypothetical mathematical demonstrations, not empirical sequence analyses.

### Model 1.1: Fraction annotated as repeat sequence

**Equation:** Repeat fraction = flagged bases / total. **Caveat:** Toy percentage only. Change the independent parameter, then explain whether the output change is a simple mathematical consequence or requires a biological inference. A monotone visual trend is not automatically a causal biological law. Identify the units and what is held constant.

### Model 1.2: Haploid size from diploid DNA content

**Equation:** Haploid mass = diploid mass / 2. **Caveat:** Only ordinary diploid-nuclear assumption. Change the independent parameter, then explain whether the output change is a simple mathematical consequence or requires a biological inference. A monotone visual trend is not automatically a causal biological law. Identify the units and what is held constant.
