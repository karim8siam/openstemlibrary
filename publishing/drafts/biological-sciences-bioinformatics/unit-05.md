# Unit 05 — Transcriptomics, proteomics and integrated omics

> **OpenSTEM Bioinformatics · Book 15 · Editorial draft.** All instructional sequences, measurements, cases and figures in this unit are fictional. Scientific peer review and publication approval are pending.

## The question driving this unit

**How do high-dimensional molecular assays support fair comparisons among conditions?**

Omics datasets combine measurement intensity, technical processing, biology and sampling. A complete workflow starts with experimental design, not with a heatmap. Counts reflect both molecule abundance and sampling depth; peptide intensities reflect multiple layers of ionization and identification; metabolite features may lack definitive structural identities.

### Why this subject needs both biology and computation

Normalization corrects specified measurement effects, but it cannot resolve a treatment perfectly confounded with batch. Likewise, statistical significance should depend on between-sample variability and multiplicity, not just a striking fold-change. Exploratory dimensionality reduction cannot rescue poorly collected data.

Computational methods are valuable because they allow a question to be formulated as an explicit transformation: which inputs enter the calculation, which parameters matter, what optimization or probability rule is applied, and which output should be checked against another observation. Biologists add knowledge of sampling, function and evolutionary history; statisticians add uncertainty analysis; software engineers add consistent handling of records and failure conditions. Effective bioinformatics takes all three perspectives seriously rather than treating a software report as its own justification.

### Running example and evidence hierarchy

Imagine leaves collected before and after controlled shade treatments, with sample identities balanced across preparation days. First report assay quality and independent biological units. Then use a count model for gene expression and explicit missingness policies for proteomics. Integrating layers can prioritize an explanation but does not automatically establish causal molecular pathways.

For this example, use an evidence hierarchy rather than a binary correct/incorrect answer. At the lowest level sit identity and integrity checks. Next come observed measurement patterns and elementary comparisons. Next come model-based predictions whose uncertainty depends on assumptions. Finally come claims about biological mechanism or action, which normally require a stronger study design or independent evidence. Students should be able to identify the level actually supported and refuse an unsupported jump between levels.

### Course integration

Good evidence states the observational unit, laboratory limitations and the scope of interpretation. A path diagram that joins transcript, protein and metabolite signals may serve as a hypothesis map. It is not proof that changing one component alters another. Design future experiments to test the most consequential causal link.

The end-of-unit study uses a fictional dataset so students can audit the entire workflow without accessing private data or claiming to have made new biological discoveries. Record all transformations in a log, include the rejected observations and state explicitly how a different cutoff or model might change the narrative.

## Learning outcomes

By the end of this unit you should be able to: (1) define the five techniques in their proper inferential scope; (2) compute and audit the five numerical examples; (3) propose a minimal control or validation for an ambiguous result; (4) interpret each interactive model's assumptions; and (5) write a cautious, reproducible conclusion.

## Lesson 5.1 — RNA-seq experimental design

### Concept and biological meaning

RNA-seq assays transcript abundance indirectly through sequenced molecules, so conclusions depend on biological replicates, sampling design and technical batch structure. 

### Method and reproducible data contract

Randomize batches, track RNA integrity, library preparation, organism, tissue, sex or other relevant confounders, and choose units of biological replication before sequencing. Before running an analysis, write down the input type, reference release, allowed missing values, expected columns and numerical settings. Record the observation level—organism, specimen, sequencing run, read, transcript, protein or residue—because the number of table rows need not equal the number of independent biological replicates. Reproduce one calculation using a tiny invented example and write an automatic assertion for its expected output. This validates implementation, not the scientific truth of the starting assumptions.

### Case study: a plausible signal and a rival explanation

A plant stress experiment processed all control libraries on Monday and all treated libraries on Friday. The first task is to frame a biological hypothesis and a specific technical or sampling alternative. Describe what would be observed if the preferred explanation were true, then name an observation that might discriminate it from the rival. Consider label mix-ups, reference changes, missingness and biased sample recruitment before treating agreement among software tools as independent confirmation.



### Worked quantitative example

Three samples per group give six independent biological units if sampled from six plants; repeated lanes do not change biological n. Treat these numbers as fictional teaching inputs. Reproduce the arithmetic in your notes, identify the denominator and decide whether the answer has physical units, is a dimensionless proportion or is a model score. Explain which input change would mechanically alter the answer. A numerical value calculated exactly from inaccurate or unrepresentative data is still a limited scientific result.

### Caveats, sensitivity and evidence strength

If batch is perfectly confounded with treatment, modeling cannot distinguish the two causes without new data. More reads per existing library improve measurement depth but do not substitute for replication across organisms. 

### Independent evaluation and advanced extension

Propose a balanced library assignment in which both treatments appear across each preparation batch, with blinded QC. Use this extension as a miniature sensitivity study. Change one defensible setting at a time and record whether the inference remains stable. Where methods disagree, identify whether they use different definitions, references or sources of uncertainty. Avoid the practice of choosing whichever method produces the desired biological story.

**Transfer of conclusions.** A numerical relationship estimated on a small classroom dataset can demonstrate a procedure without transferring to another organism or technology. External validity is an empirical question; record domain, reference, experimental setting and foreseeable distribution shift. For **rna-seq experimental design**, supply an actual auditable record—not a generic pledge of reproducibility—that would expose a mistaken assumption in the fictional case.

### Questions for mastery

1. What is directly observed, what is computed, and what is inferred? Explain the transitions using this lesson’s situation.
2. Which negative control, alternative model or independent observation could test a rival explanation? State what result would weaken your preferred account.
3. Repeat the numerical example after changing one input and report units, denominator and interpretation. Explain why a correct recalculation does not establish biological validity.
4. Which detail would another scientist need to rerun the analysis from precisely the same inputs? Describe a realistic failure if it were missing.



---
## Lesson 5.2 — Count matrices and normalization

### Concept and biological meaning

Gene-level RNA-seq count matrices hold integer fragment or read counts by gene and sample; library-size effects and composition biases require modeled normalization. 

### Method and reproducible data contract

Use raw counts with count-based models such as DESeq2 and let the method estimate size factors; normalized counts are generally for exploration and display. Before running an analysis, write down the input type, reference release, allowed missing values, expected columns and numerical settings. Record the observation level—organism, specimen, sequencing run, read, transcript, protein or residue—because the number of table rows need not equal the number of independent biological replicates. Reproduce one calculation using a tiny invented example and write an automatic assertion for its expected output. This validates implementation, not the scientific truth of the starting assumptions.

### Case study: a plausible signal and a rival explanation

One sample has twice as many total fragments yet comparable transcript composition. The first task is to frame a biological hypothesis and a specific technical or sampling alternative. Describe what would be observed if the preferred explanation were true, then name an observation that might discriminate it from the rival. Consider label mix-ups, reference changes, missingness and biased sample recruitment before treating agreement among software tools as independent confirmation.



### Worked quantitative example

A gene with 40 reads in a 2-million-read library has 20 counts per million; in a 4-million-read library 80 reads also yield 20 CPM. Treat these numbers as fictional teaching inputs. Reproduce the arithmetic in your notes, identify the denominator and decide whether the answer has physical units, is a dimensionless proportion or is a model score. Explain which input change would mechanically alter the answer. A numerical value calculated exactly from inaccurate or unrepresentative data is still a limited scientific result.

### Caveats, sensitivity and evidence strength

Doubling library depth can approximately double raw gene counts without changing the underlying relative abundance. Counts per million correct only total library size, not transcript length, composition shifts or design confounding. 

### Independent evaluation and advanced extension

Contrast total-count scaling with median-of-ratios intuition using several genes, and identify a global compositional shift. Use this extension as a miniature sensitivity study. Change one defensible setting at a time and record whether the inference remains stable. Where methods disagree, identify whether they use different definitions, references or sources of uncertainty. Avoid the practice of choosing whichever method produces the desired biological story.

**Biological unit.** Count the unit actually sampled rather than the number of rows generated by instruments or algorithms. Repeated reads, peptides, contigs or scans may improve measurement of one specimen without increasing independence for population-level inference. For **count matrices and normalization**, supply an actual auditable record—not a generic pledge of reproducibility—that would expose a mistaken assumption in the fictional case.

### Questions for mastery

1. What is directly observed, what is computed, and what is inferred? Explain the transitions using this lesson’s situation.
2. Which negative control, alternative model or independent observation could test a rival explanation? State what result would weaken your preferred account.
3. Repeat the numerical example after changing one input and report units, denominator and interpretation. Explain why a correct recalculation does not establish biological validity.
4. Which detail would another scientist need to rerun the analysis from precisely the same inputs? Describe a realistic failure if it were missing.



---
## Lesson 5.3 — Differential expression and dispersion

### Concept and biological meaning

Differential expression compares evidence for condition-associated changes against variability between biological samples, often with a negative-binomial count model. 

### Method and reproducible data contract

Specify design formula, reference contrast, minimum effect of interest, dispersion estimation and multiple-testing correction before inspecting ranked genes. Before running an analysis, write down the input type, reference release, allowed missing values, expected columns and numerical settings. Record the observation level—organism, specimen, sequencing run, read, transcript, protein or residue—because the number of table rows need not equal the number of independent biological replicates. Reproduce one calculation using a tiny invented example and write an automatic assertion for its expected output. This validates implementation, not the scientific truth of the starting assumptions.

### Case study: a plausible signal and a rival explanation

A rare transcript has an apparent eightfold change driven by one count in the untreated group. The first task is to frame a biological hypothesis and a specific technical or sampling alternative. Describe what would be observed if the preferred explanation were true, then name an observation that might discriminate it from the rival. Consider label mix-ups, reference changes, missingness and biased sample recruitment before treating agreement among software tools as independent confirmation.



### Worked quantitative example

Counts 10 versus 40 yield raw fold change four and log2 fold change two, but significance cannot be inferred without replicate variability. Treat these numbers as fictional teaching inputs. Reproduce the arithmetic in your notes, identify the denominator and decide whether the answer has physical units, is a dimensionless proportion or is a model score. Explain which input change would mechanically alter the answer. A numerical value calculated exactly from inaccurate or unrepresentative data is still a limited scientific result.

### Caveats, sensitivity and evidence strength

Huge fold changes near zero can be unstable; effect-size shrinkage and dispersion-aware testing address different uncertainties. A small p-value does not measure the size or biological importance of a change and cannot correct a confounded design. 

### Independent evaluation and advanced extension

Plot effect size versus precision for a synthetic comparison and explain why the same fold change has different confidence in two genes. Use this extension as a miniature sensitivity study. Change one defensible setting at a time and record whether the inference remains stable. Where methods disagree, identify whether they use different definitions, references or sources of uncertainty. Avoid the practice of choosing whichever method produces the desired biological story.

**Model adequacy.** Mathematical formulas compress real biological processes. Before interpreting a parameter, check limiting cases, dimensional consistency and residual patterns. Simple models can sharpen reasoning precisely because their omissions are transparent. For **differential expression and dispersion**, supply an actual auditable record—not a generic pledge of reproducibility—that would expose a mistaken assumption in the fictional case.

### Questions for mastery

1. What is directly observed, what is computed, and what is inferred? Explain the transitions using this lesson’s situation.
2. Which negative control, alternative model or independent observation could test a rival explanation? State what result would weaken your preferred account.
3. Repeat the numerical example after changing one input and report units, denominator and interpretation. Explain why a correct recalculation does not establish biological validity.
4. Which detail would another scientist need to rerun the analysis from precisely the same inputs? Describe a realistic failure if it were missing.



---
## Lesson 5.4 — Proteomics features and missingness

### Concept and biological meaning

Mass spectrometry quantifies peptide evidence that is mapped to proteins; protein inference and ionization efficiency complicate abundance comparisons. 

### Method and reproducible data contract

Track peptide uniqueness, charge states, identification confidence, batch drift and the mechanism that causes features to be missing. Before running an analysis, write down the input type, reference release, allowed missing values, expected columns and numerical settings. Record the observation level—organism, specimen, sequencing run, read, transcript, protein or residue—because the number of table rows need not equal the number of independent biological replicates. Reproduce one calculation using a tiny invented example and write an automatic assertion for its expected output. This validates implementation, not the scientific truth of the starting assumptions.

### Case study: a plausible signal and a rival explanation

Two protein isoforms share most peptides and a single discriminating peptide is absent in one run. The first task is to frame a biological hypothesis and a specific technical or sampling alternative. Describe what would be observed if the preferred explanation were true, then name an observation that might discriminate it from the rival. Consider label mix-ups, reference changes, missingness and biased sample recruitment before treating agreement among software tools as independent confirmation.



### Worked quantitative example

If 45 of 60 expected peptide measurements are detected, completeness is 75%, but detection fraction is not an effect size. Treat these numbers as fictional teaching inputs. Reproduce the arithmetic in your notes, identify the denominator and decide whether the answer has physical units, is a dimensionless proportion or is a model score. Explain which input change would mechanically alter the answer. A numerical value calculated exactly from inaccurate or unrepresentative data is still a limited scientific result.

### Caveats, sensitivity and evidence strength

Missing values can arise below detection limits or stochastic acquisition; blindly imputing a constant creates artificial group differences. One peptide may map to several homologous proteins, so adding its intensity to every mapped protein overcounts evidence. 

### Independent evaluation and advanced extension

Separate peptide-level identification evidence from protein-level quantitative summaries and document the inference policy. Use this extension as a miniature sensitivity study. Change one defensible setting at a time and record whether the inference remains stable. Where methods disagree, identify whether they use different definitions, references or sources of uncertainty. Avoid the practice of choosing whichever method produces the desired biological story.

**Reproducible decisions.** A reader should be able to regenerate the same derived table from the same inputs and explicit settings. Preserve a checksum and environment record, and keep a log of decisions that change which records enter the analysis. For **proteomics features and missingness**, supply an actual auditable record—not a generic pledge of reproducibility—that would expose a mistaken assumption in the fictional case.

### Questions for mastery

1. What is directly observed, what is computed, and what is inferred? Explain the transitions using this lesson’s situation.
2. Which negative control, alternative model or independent observation could test a rival explanation? State what result would weaken your preferred account.
3. Repeat the numerical example after changing one input and report units, denominator and interpretation. Explain why a correct recalculation does not establish biological validity.
4. Which detail would another scientist need to rerun the analysis from precisely the same inputs? Describe a realistic failure if it were missing.



---
## Lesson 5.5 — Metabolomics and multi-omics integration

### Concept and biological meaning

Metabolomics measures molecular features influenced by extraction, chromatography, ionization and identification ambiguity; multi-omics integration combines different data-generating processes. 

### Method and reproducible data contract

Use sample-matched identifiers, scale-aware normalization and explicit feature identification levels; cross-study harmonization needs documented units. Before running an analysis, write down the input type, reference release, allowed missing values, expected columns and numerical settings. Record the observation level—organism, specimen, sequencing run, read, transcript, protein or residue—because the number of table rows need not equal the number of independent biological replicates. Reproduce one calculation using a tiny invented example and write an automatic assertion for its expected output. This validates implementation, not the scientific truth of the starting assumptions.

### Case study: a plausible signal and a rival explanation

A stress response appears in RNA profiles but a candidate metabolite changes only after a time delay. The first task is to frame a biological hypothesis and a specific technical or sampling alternative. Describe what would be observed if the preferred explanation were true, then name an observation that might discriminate it from the rival. Consider label mix-ups, reference changes, missingness and biased sample recruitment before treating agreement among software tools as independent confirmation.



### Worked quantitative example

For paired samples with values (2,4) and (3,6), both ratios equal 1.5, but no biological pathway claim follows from two observations. Treat these numbers as fictional teaching inputs. Reproduce the arithmetic in your notes, identify the denominator and decide whether the answer has physical units, is a dimensionless proportion or is a model score. Explain which input change would mechanically alter the answer. A numerical value calculated exactly from inaccurate or unrepresentative data is still a limited scientific result.

### Caveats, sensitivity and evidence strength

Correlations across molecular layers do not determine direction or causal mediation; pathway databases encode incomplete knowledge. A mass-to-charge feature with an approximate name is not necessarily a confirmed molecular structure. 

### Independent evaluation and advanced extension

Sketch causal hypotheses and a sample-matched table, then distinguish joint prediction from mechanistic verification. Use this extension as a miniature sensitivity study. Change one defensible setting at a time and record whether the inference remains stable. Where methods disagree, identify whether they use different definitions, references or sources of uncertainty. Avoid the practice of choosing whichever method produces the desired biological story.

**Operational definition.** Before computing, write an operational definition of the variable of interest, including its measurement unit, denominator, sampling level and admissible values. An operational definition is not bureaucracy; it is what makes two methods comparable and reveals when they answer different questions. For **metabolomics and multi-omics integration**, supply an actual auditable record—not a generic pledge of reproducibility—that would expose a mistaken assumption in the fictional case.

### Questions for mastery

1. What is directly observed, what is computed, and what is inferred? Explain the transitions using this lesson’s situation.
2. Which negative control, alternative model or independent observation could test a rival explanation? State what result would weaken your preferred account.
3. Repeat the numerical example after changing one input and report units, denominator and interpretation. Explain why a correct recalculation does not establish biological validity.
4. Which detail would another scientist need to rerun the analysis from precisely the same inputs? Describe a realistic failure if it were missing.



---

## Integrated laboratory 5: an auditable evidence chain

**Setting.** Your undergraduate group receives fictional records about a small collection of biological material. The file descriptions are intentionally imperfect. The exercise focuses on **rna-seq experimental design, count matrices and normalization, differential expression and dispersion, proteomics features and missingness, metabolomics and multi-omics integration** as five aspects of one argument rather than five disconnected tool demonstrations. No live database submissions, human specimen data, laboratory samples or web API credentials are required.

**Question formation.** Begin with the question in the unit introduction. Rewrite it as a comparison of named observations, identify the unit of sampling and decide what counts as a missing or uninterpretable value. Include a skeptical alternative hypothesis. For example, an association between two measurements could reflect a common technical batch rather than a causal connection. A sensible plan makes that alternative visible before results are plotted.

**Table design.** Create a machine-readable table with fields `record_id`, `biological_unit_id`, `source_release`, `assay_or_algorithm`, `quality_note`, `value`, `unit` and `exclusion_reason`. State which fields can be blank, what the file encoding is, and how missingness is represented. Never represent a missing quantitative measurement as zero unless zero is a genuine recorded value. If two rows share the same biological unit, decide whether they are technical repeats or separate conditions before assigning inferential sample size.

**Computation plan.** Reproduce the numerical case from each of the five lessons by hand. Put the given values and final expressions into a transparent notebook or script. Build a validation assertion for each worked result, add one deliberately malformed record and document its rejection. Verify that each numerical result has a denominator, unit or declared scale. The exercise does not ask you to rerun sophisticated tools on real genomes; it asks for defensible reasoning about toy outputs.

**Sensitivity and counterexamples.** Perform two controlled changes. First vary a parameter that the method explicitly allows the analyst to choose, such as a gap cost, cutoff, filter or comparison baseline. Second introduce a metadata problem such as duplicate labels or a mismatched reference version. Predict the consequences before performing the changed calculation. A surprising result should trigger investigation rather than selective deletion.

**Scientific interpretation.** Prepare a figure caption with the method, invented input description, assumptions and excluded observations. Write a conclusion with one supported statement, one plausible rival explanation and one test that would improve confidence. The conclusion must not convert a sequence match into experimental function, a score into clinical truth, a correlation into causation or a diagram into exact evolutionary history.

**Peer review rubric.** A second student receives only the manifest, script, small input table, expected numeric outputs and explanatory notes. Award one point each for exact input identity, correct sampling unit, reproducible arithmetic, transparent uncertainty and appropriate claim boundaries. A score of five means the teaching exercise was reported clearly; it is not independent scientific validation of the underlying assumptions.

**Discussion prompt.** If a second software package reproduces the same output, what failure modes remain? Could both tools share a database annotation, an unrepresentative sample or an invalid conceptual assumption? Suggest one independent observation that would provide new evidence rather than only computational agreement.
