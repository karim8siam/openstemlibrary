# Unit 03 — Genome assembly and functional annotation

> **OpenSTEM Genomics · Book 16 · Editorial teaching draft.** All worked case data and investigations are synthetic. The interactive models describe simplified mathematical relations, not diagnoses or empirical genomic claims.

## Central scientific question

**How are fragmented measurements converted into genomic maps and features?**

### Conceptual context and how the five lessons fit

Genome assembly is a hypothesis about sequence order constrained by fragments, graphs and other measurements. Graph branches may reflect repeats, heterozygosity, true rearrangements or error; a tool's decision to choose one branch does not eliminate those alternatives. Assembly evaluation has therefore become multidimensional: continuity, base accuracy, completeness, contamination, haplotype representation and biological plausibility should be considered separately. Annotation adds a new inferential layer by locating putative genes and regulatory features. In this unit, learners move from assembly algorithms to contig summaries, phasing, gene-model evidence and functional descriptions. Whenever an algorithm emits an apparently definitive label, inspect which measurements warrant that label and what independent evidence might overturn it.

### A running case to reason through

A proposed high-quality assembly has impressive contig sizes but contains collapsed paralogs and a swapped sample. The proposed explanation should remain a working hypothesis until both the measurement process and alternative biological accounts have been examined. Identify a plausible negative control, a sample identity verification and a condition in which the preferred model might fail. A final plot can be numerically precise while its biological conclusion is uncertain; your task is to make that uncertainty visible rather than treating it as a defect.

### Unit learning objectives

By the end of this unit, you should be able to reconstruct the data assumptions behind each of the five main topics, reproduce their toy calculations, distinguish technical and biological replication, identify a rival explanation for an apparent signal, and propose an independent measurement that would strengthen or challenge the inference. For each numerical answer, know the denominator, its unit and the simplifications required. Give yourself permission to conclude "not established" when appropriate.

### Study route

Read the five lessons in order. Each starts with an operational definition, moves through a fictional case and a worked calculation, then challenges the tempting inference. Compute the numbers by hand before using code. Finish with the unit capstone and the interactive model questions. Learning genomics requires deciding which questions an assay can answer at least as much as mastering the associated algorithm.

---

## Lesson 3.1 — Assembly graphs, k-mers and ambiguity

### Mechanism and what can be inferred

A de Bruijn graph connects overlapping k-mers, whereas overlap-based approaches connect longer observed reads; repeats generate cycles or branches, and sequencing errors generate low-support paths. Identify the physical material, the instrument observation and the computational summary separately. This prevents a dataset label from being mistaken for the underlying biological process. The central question is **How are fragmented measurements converted into genomic maps and features?** Interpret that question in the limited context of the named species, specimens and assay; do not extrapolate from one sequence representation to all individuals.

### Measurement contract and analytical method

Choose k-mer or overlap parameters based on read lengths and expected heterozygosity. Inspect graph bubbles, coverage balance, alternative haplotype paths and disconnected components before assigning a unique traversal. Create a tiny independent benchmark that contains an ordinary case, an ambiguous boundary case and a deliberately malformed record. Check not only output numbers but also whether the tool detects invalid assumptions and refuses silent corrections. When comparing results, include the reference assembly or database release, observation level, quality thresholds, removed records and a denominator for each proportion. Missing genomic measurements are not synonymous with confidently absent biological events. Explain which parts of the pipeline are deterministic transformations and which rely on empirical model assumptions.

### Fictional case and competing explanation

An imaginary bacterial assembly has a repeated gene family whose length exceeds short-read fragments; its graph has a branch that cannot be disambiguated without other evidence. This is a hypothetical instructional case, not a reported finding. Begin with one biological hypothesis and one technical or sampling rival. Before choosing the most interesting interpretation, write down what each hypothesis predicts about a newly collected specimen or orthogonal assay. Different algorithms may agree because they reuse the same flawed reference or measurement, not because they supply independent experimental confirmation.

### Worked example with units

**Problem:** A linear 100-base sequence contains 70 overlapping 31-mers, counting positions not necessarily 70 unique k-mer strings.

**Calculation:** `100-31+1` = **70 31-mer positions** for the invented inputs. To test your interpretation, change one input within a plausible synthetic range and recompute the output. The goal is not to fit actual organisms but to understand how measurement assumptions propagate through the equation. Correct arithmetic validates a calculation, but it does not establish that the input data are representative or that the result has a causal meaning. Record whether the denominator counts bases, reads, allele copies, individuals, loci or experimental runs. Recompute with a modified hypothetical input to examine numerical sensitivity.

### Error modes and validation design

A graph traversal is not necessarily a biological chromosome; combining paths merely to maximize continuity may invent a nonexistent sequence. If the measurement was duplicated at the technical level, name the correct independent sampling level before offering any significance claim. Replication improves confidence only to the extent that it samples the relevant biological variability. **Audit emphasis — State the reference.** Describe what counts as a matching coordinate, allele or feature under the selected reference. Changing a reference can change apparent variants or gene boundaries while the original material remains unchanged.

Simulate unique and duplicated 31-mers; compare a graph with and without error filtering, then validate traversal using long molecules. The proposed new evidence should help discriminate between mechanisms rather than merely producing another version of the same computational score. Explain the important negative control and a result that would weaken your preferred hypothesis. In a scientific report, keep measurements, computed statistics, model-based predictions and proposed biological explanations in separate statements.

### Transfer exercise

Connect **Assembly graphs, k-mers and ambiguity** with **Contig metrics, N50 and completeness**. Explain which source-data error would contaminate both topics and how a reference-aware provenance record would reveal it. Then answer: What was measured? How was the statistic calculated? What competing explanation remains? What independent experiment would be most efficient? Present the final inference as a conditional claim whose strength matches the available evidence.

---

## Lesson 3.2 — Contig metrics, N50 and completeness

### Mechanism and what can be inferred

N50 describes the length at which contigs of at least that size account for half the assembled bases. It quantifies size distribution, not accuracy, gene completeness or structural plausibility. Identify the physical material, the instrument observation and the computational summary separately. This prevents a dataset label from being mistaken for the underlying biological process. The central question is **How are fragmented measurements converted into genomic maps and features?** Interpret that question in the limited context of the named species, specimens and assay; do not extrapolate from one sequence representation to all individuals.

### Measurement contract and analytical method

Compute contig lengths, total span, gap fraction, support for intercontig joins and assembly-vs-reference discrepancies. For gene completeness use independently curated ortholog sets where appropriate and report lineage choice. For a transparent analysis, make two small tables: one describing source specimens and assays, and another describing computational transformations. The join keys should let another investigator trace a number back to its input without revealing restricted personal information. When comparing results, include the reference assembly or database release, observation level, quality thresholds, removed records and a denominator for each proportion. Missing genomic measurements are not synonymous with confidently absent biological events. Explain which parts of the pipeline are deterministic transformations and which rely on empirical model assumptions.

### Fictional case and competing explanation

A fictional 4-Mb assembly has contigs of 2 Mb, 1 Mb and two 0.5-Mb pieces, but the largest contig contains a misassembly. This is a hypothetical instructional case, not a reported finding. Begin with one biological hypothesis and one technical or sampling rival. Before choosing the most interesting interpretation, write down what each hypothesis predicts about a newly collected specimen or orthogonal assay. Different algorithms may agree because they reuse the same flawed reference or measurement, not because they supply independent experimental confirmation.

### Worked example with units

**Problem:** For contigs 2, 1, 0.5 and 0.5 Mb (4 Mb total), N50 equals 2 Mb because the largest contig alone reaches half of assembly span.

**Calculation:** `2` = **2 Mb** for the invented inputs. Check the unit, sign, scale and rounding of the calculated answer. Where a proportion is involved, state whether the result counts reads, alleles, individuals, transcripts, genomic sites or publications; those denominators are not interchangeable. Correct arithmetic validates a calculation, but it does not establish that the input data are representative or that the result has a causal meaning. Record whether the denominator counts bases, reads, allele copies, individuals, loci or experimental runs. Recompute with a modified hypothetical input to examine numerical sensitivity.

### Error modes and validation design

Selecting the largest N50 can reward erroneous joins; missing small chromosomes and collapsed repeats may go undetected by this statistic. Consider whether the strongest-looking pattern comes from a feature selected after inspecting the answer. Exploratory selection followed by an unadjusted confirmatory claim can overstate reproducibility. **Audit emphasis — Test the missingness.** Identify which observations were never sampled, lost in preparation, removed by filters or assigned ambiguous labels. A blank value and a confident absence are fundamentally different statements.

Combine multiple independent QC dimensions: completeness, contamination, k-mer consistency, read-to-assembly concordance and long-range structure. The proposed new evidence should help discriminate between mechanisms rather than merely producing another version of the same computational score. Explain the important negative control and a result that would weaken your preferred hypothesis. In a scientific report, keep measurements, computed statistics, model-based predictions and proposed biological explanations in separate statements.

### Transfer exercise

Connect **Contig metrics, N50 and completeness** with **Phasing, scaffolding and diploid assemblies**. Explain which source-data error would contaminate both topics and how a reference-aware provenance record would reveal it. Then answer: What was measured? How was the statistic calculated? What competing explanation remains? What independent experiment would be most efficient? Present the final inference as a conditional claim whose strength matches the available evidence.

---

## Lesson 3.3 — Phasing, scaffolding and diploid assemblies

### Mechanism and what can be inferred

Phasing assigns alleles to chromosome copies; scaffolding orders and orients contigs using long-range evidence. A diploid primary assembly may collapse or separate haplotypes depending on strategy. Identify the physical material, the instrument observation and the computational summary separately. This prevents a dataset label from being mistaken for the underlying biological process. The central question is **How are fragmented measurements converted into genomic maps and features?** Interpret that question in the limited context of the named species, specimens and assay; do not extrapolate from one sequence representation to all individuals.

### Measurement contract and analytical method

Document which scaffold represents which haplotype, switch-error rate where measurable, long-range link quality and treatment of homozygous runs. Treat sequence gaps and uncertain orientation as explicit unknowns. Preregister an analysis comparison in plain language: what signal is sought, which confounders are anticipated, how filtering will work, which readouts matter, and what observation would count against the favored interpretation. When comparing results, include the reference assembly or database release, observation level, quality thresholds, removed records and a denominator for each proportion. Missing genomic measurements are not synonymous with confidently absent biological events. Explain which parts of the pipeline are deterministic transformations and which rely on empirical model assumptions.

### Fictional case and competing explanation

Two fictional siblings share many alleles; a researcher mistakenly stitches alternative parental haplotypes into the same scaffold. This is a hypothetical instructional case, not a reported finding. Begin with one biological hypothesis and one technical or sampling rival. Before choosing the most interesting interpretation, write down what each hypothesis predicts about a newly collected specimen or orthogonal assay. Different algorithms may agree because they reuse the same flawed reference or measurement, not because they supply independent experimental confirmation.

### Worked example with units

**Problem:** If 7 switches occur across 350 assessed adjacent heterozygous-marker intervals, empirical switch-error fraction is 2%.

**Calculation:** `7/350*100` = **2 %** for the invented inputs. To test your interpretation, change one input within a plausible synthetic range and recompute the output. The goal is not to fit actual organisms but to understand how measurement assumptions propagate through the equation. Correct arithmetic validates a calculation, but it does not establish that the input data are representative or that the result has a causal meaning. Record whether the denominator counts bases, reads, allele copies, individuals, loci or experimental runs. Recompute with a modified hypothetical input to examine numerical sensitivity.

### Error modes and validation design

An attractive chromosome-length sequence can contain phase switches, so continuity alone cannot prove correct inheritance patterns. Explain how an earlier-stage error could propagate through several downstream analyses and create apparently consistent output. Correlation among derived reports should never substitute for documented source integrity. **Audit emphasis — Inspect the mechanism.** Link the measured molecular signal to a plausible process and identify where the causal arrow is merely assumed. Correlated regulatory, evolutionary or clinical features can have shared upstream causes.

Check read-linked allele co-occurrence and pedigree-consistent transmission across heterozygous markers; compare results under stricter phasing criteria. The proposed new evidence should help discriminate between mechanisms rather than merely producing another version of the same computational score. Explain the important negative control and a result that would weaken your preferred hypothesis. In a scientific report, keep measurements, computed statistics, model-based predictions and proposed biological explanations in separate statements.

### Transfer exercise

Connect **Phasing, scaffolding and diploid assemblies** with **Gene prediction and evidence-supported annotation**. Explain which source-data error would contaminate both topics and how a reference-aware provenance record would reveal it. Then answer: What was measured? How was the statistic calculated? What competing explanation remains? What independent experiment would be most efficient? Present the final inference as a conditional claim whose strength matches the available evidence.

---

## Lesson 3.4 — Gene prediction and evidence-supported annotation

### Mechanism and what can be inferred

Gene callers combine sequence features, conserved protein similarity and expression evidence to propose coding loci. A transcript may be real without being protein coding; gene boundaries differ among isoforms. Identify the physical material, the instrument observation and the computational summary separately. This prevents a dataset label from being mistaken for the underlying biological process. The central question is **How are fragmented measurements converted into genomic maps and features?** Interpret that question in the limited context of the named species, specimens and assay; do not extrapolate from one sequence representation to all individuals.

### Measurement contract and analytical method

Retain feature provenance, transcript structures, evidence codes and annotation version. Compare ab initio predictions to aligned RNA and curated ortholog sequences while documenting unsupported candidates. Write a data dictionary before invoking a tool. It should specify permitted values, missing-data codes, identity keys, coordinate conventions, and a worked input-output example whose result can be checked without proprietary software. When comparing results, include the reference assembly or database release, observation level, quality thresholds, removed records and a denominator for each proportion. Missing genomic measurements are not synonymous with confidently absent biological events. Explain which parts of the pipeline are deterministic transformations and which rely on empirical model assumptions.

### Fictional case and competing explanation

A fictional insect genome yields 18,000 automated predictions but only 13,500 candidates have at least one independent evidence class. This is a hypothetical instructional case, not a reported finding. Begin with one biological hypothesis and one technical or sampling rival. Before choosing the most interesting interpretation, write down what each hypothesis predicts about a newly collected specimen or orthogonal assay. Different algorithms may agree because they reuse the same flawed reference or measurement, not because they supply independent experimental confirmation.

### Worked example with units

**Problem:** Of 18,000 predictions, 13,500 with independent evidence are 75%; this does not imply the other 25% are false.

**Calculation:** `13_500/18_000*100` = **75 %** for the invented inputs. Check the unit, sign, scale and rounding of the calculated answer. Where a proportion is involved, state whether the result counts reads, alleles, individuals, transcripts, genomic sites or publications; those denominators are not interchangeable. Correct arithmetic validates a calculation, but it does not establish that the input data are representative or that the result has a causal meaning. Record whether the denominator counts bases, reads, allele copies, individuals, loci or experimental runs. Recompute with a modified hypothetical input to examine numerical sensitivity.

### Error modes and validation design

Automated gene counts are sensitive to fragmentation, transposable element misannotation and paralog collapse; they cannot be read as confirmed gene inventories. Ask which alternative assay or independent group could challenge the finding. Repeating a computation under different colors or with another software package is not independent biological replication. **Audit emphasis — Protect the inferential boundary.** Separate an algorithmic score from a measurement and from an actionable interpretation. Showing that a model is internally consistent is not the same as validating its claims in a new cohort.

Audit random gene models visually and compare strand, intron support, untranslated regions and protein domains with an external curated set. The proposed new evidence should help discriminate between mechanisms rather than merely producing another version of the same computational score. Explain the important negative control and a result that would weaken your preferred hypothesis. In a scientific report, keep measurements, computed statistics, model-based predictions and proposed biological explanations in separate statements.

### Transfer exercise

Connect **Gene prediction and evidence-supported annotation** with **Functional annotation and ontology evidence**. Explain which source-data error would contaminate both topics and how a reference-aware provenance record would reveal it. Then answer: What was measured? How was the statistic calculated? What competing explanation remains? What independent experiment would be most efficient? Present the final inference as a conditional claim whose strength matches the available evidence.

---

## Lesson 3.5 — Functional annotation and ontology evidence

### Mechanism and what can be inferred

A protein-family match, predicted domain and pathway label are different strengths of functional evidence. Orthology can support hypotheses but cannot guarantee conserved substrate specificity or tissue function. Identify the physical material, the instrument observation and the computational summary separately. This prevents a dataset label from being mistaken for the underlying biological process. The central question is **How are fragmented measurements converted into genomic maps and features?** Interpret that question in the limited context of the named species, specimens and assay; do not extrapolate from one sequence representation to all individuals.

### Measurement contract and analytical method

Separate molecular function, biological process and cellular location labels, and include annotation method and evidence code. Avoid transferring a narrow curated property through distant paralogs. Reconstruct the reasoning as an evidence ledger with separate columns for raw measurement, model choice, calculated value, alternative explanation and validation status. Avoid merging uncertain evidence into one unexplained confidence label. When comparing results, include the reference assembly or database release, observation level, quality thresholds, removed records and a denominator for each proportion. Missing genomic measurements are not synonymous with confidently absent biological events. Explain which parts of the pipeline are deterministic transformations and which rely on empirical model assumptions.

### Fictional case and competing explanation

A fictional archaeal enzyme resembles a known kinase at the sequence level, but its cellular substrate and physiological pathway remain experimentally untested. This is a hypothetical instructional case, not a reported finding. Begin with one biological hypothesis and one technical or sampling rival. Before choosing the most interesting interpretation, write down what each hypothesis predicts about a newly collected specimen or orthogonal assay. Different algorithms may agree because they reuse the same flawed reference or measurement, not because they supply independent experimental confirmation.

### Worked example with units

**Problem:** A curated 200-protein benchmark labels 170 correctly; observed benchmark accuracy is 85%, not a genome-wide universal accuracy guarantee.

**Calculation:** `170/200*100` = **85 %** for the invented inputs. To test your interpretation, change one input within a plausible synthetic range and recompute the output. The goal is not to fit actual organisms but to understand how measurement assumptions propagate through the equation. Correct arithmetic validates a calculation, but it does not establish that the input data are representative or that the result has a causal meaning. Record whether the denominator counts bases, reads, allele copies, individuals, loci or experimental runs. Recompute with a modified hypothetical input to examine numerical sensitivity.

### Error modes and validation design

Annotation pipelines can amplify one incorrect database label across many genes; mutually agreeing outputs may rely on the same underlying mistaken reference. If the measurement was duplicated at the technical level, name the correct independent sampling level before offering any significance claim. Replication improves confidence only to the extent that it samples the relevant biological variability. **Audit emphasis — Check the sensitivity.** Vary a defensible parameter—filter threshold, reference representation, cohort subset or matching rule—and report whether your conclusion changes. Sensitivity is information about model dependence, not a reason to hide uncertain results.

Prioritize testable biochemical or expression predictions and look for independently characterized homologs with compatible domains and cellular localization. The proposed new evidence should help discriminate between mechanisms rather than merely producing another version of the same computational score. Explain the important negative control and a result that would weaken your preferred hypothesis. In a scientific report, keep measurements, computed statistics, model-based predictions and proposed biological explanations in separate statements.

### Transfer exercise

Connect **Functional annotation and ontology evidence** with **Gene prediction and evidence-supported annotation**. Explain which source-data error would contaminate both topics and how a reference-aware provenance record would reveal it. Then answer: What was measured? How was the statistic calculated? What competing explanation remains? What independent experiment would be most efficient? Present the final inference as a conditional claim whose strength matches the available evidence.

---

## Unit 03 capstone — Assembly reconciliation without a ground truth chromosome

### Situation and materials

You are given fictional assembly proposals A and B. A has much higher N50, while B shows better independent molecule concordance; both differ at an apparent duplication boundary. Assume all records are fabricated for the classroom. Start by listing the observational units: organism, donor, biological preparation, technical library, genomic site or algorithmic summary. This is a crucial step because denominator mistakes can produce a result that is mathematically correct but scientifically misleading. Fix the reference and analysis version for the exercise before comparing any numbers, and include unknowns explicitly.

### Procedure and minimum outputs

Construct an evidence matrix for continuity, accuracy, completeness, contamination, phase and annotation. Use a tiny list of contig sizes to recompute N50 and reject the unsupported claim that it is an accuracy metric. Your calculations need not be complicated. They should be completely reproducible, with input values, a visible formula, arithmetic and units. Create one well-documented table for the observations, a second for transformations, and a third for which interpretations survive each quality check. Explain the transformations in words rather than copying a tool output without explanation. Before choosing a cutoff, describe the costs of false positive and false negative findings in this particular fictional study.

### Competing hypotheses and sensitivity experiment

Inspect alternative paths through a repeat graph, state what read types could resolve the ambiguity and determine whether a gene count discrepancy may reflect model fragmentation. Your favored explanation should generate a prediction that would be less likely under a clearly named alternative. Design one sensitivity exercise that changes a single assumption—such as callable regions, phase, ancestry strata, normalization rule or depth threshold—and track its effect on the main statistic. If the preferred interpretation changes, report that dependence rather than selecting the setting with the most dramatic result. Explain which new specimen, assay or observation would provide the best independent discrimination.

### Deliverables, reflection and peer review

Submit a publication-style assembly limitations paragraph and a prioritized validation plan, not a single unqualified best-assembly label. In addition, prepare a reproducibility manifest with input identifiers, simulated-only status, calculations, method version and a short rationale for every excluded observation. Include a four-sentence abstract distinguishing what is measured, estimated, hypothesized and still unknown. Exchange reports with another learner, ask them to recalculate at least one statistic using only the supplied source data, and record one objection that improves the design. Do not describe any result as clinical, diagnostic or measured in the real world.

### Challenge questions for synthesis

1. Which dataset field would have the greatest impact if it were silently mislabeled? Identify a simple audit that could catch the mistake before modeling.
2. Does the unit's central conclusion rely on random sampling, correct genome representation, accurate molecular classification or independent replication? Rank those assumptions in importance for this case.
3. What result could falsify the leading explanation without proving every alternative? Discuss the distinction between rejection of one hypothesis and proof of another.
4. If your method produced a visually excellent plot from copied or confounded measurements, what independent check would you demand before publication?
5. Explain why the precise mathematical result alone does not certify the biological or social validity of the research conclusion.

---

## Two interactive teaching models

Change each slider, observe its graph and record which assumptions make the formula valid. These are hypothetical mathematical demonstrations, not empirical sequence analyses.

### Model 3.1: Count of k-mer starting positions

**Equation:** Positions = 200−k+1. **Caveat:** Positions, not necessarily unique strings. Change the independent parameter, then explain whether the output change is a simple mathematical consequence or requires a biological inference. A monotone visual trend is not automatically a causal biological law. Identify the units and what is held constant.

### Model 3.2: Two-contig balance and length N50

**Equation:** N50 of [x,10−x] is x if x≥5. **Caveat:** N50 is not a correctness metric. Change the independent parameter, then explain whether the output change is a simple mathematical consequence or requires a biological inference. A monotone visual trend is not automatically a causal biological law. Identify the units and what is held constant.
