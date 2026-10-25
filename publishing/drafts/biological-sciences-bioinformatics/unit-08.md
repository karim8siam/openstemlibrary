# Unit 08 — Scripting, workflows and reproducible biological inference

> **OpenSTEM Bioinformatics · Book 15 · Editorial draft.** All instructional sequences, measurements, cases and figures in this unit are fictional. Scientific peer review and publication approval are pending.

## The question driving this unit

**Can another investigator re-create the result from an auditable computational record?**

Reproducibility is a property of an entire analysis specification: raw-data identity, software environment, reference databases, parameters, transformations, tests and final interpretation. A script that runs on one computer is only one part of that contract.

### Why this subject needs both biology and computation

Well-designed workflows declare dependencies and refuse to continue when inputs fail validation. A rule graph ensures that downstream analyses change when a reference or parameter changes. Tests prevent silent file corruption, resource plans guard against practical constraints, and access controls protect sensitive biological observations.

Computational methods are valuable because they allow a question to be formulated as an explicit transformation: which inputs enter the calculation, which parameters matter, what optimization or probability rule is applied, and which output should be checked against another observation. Biologists add knowledge of sampling, function and evolutionary history; statisticians add uncertainty analysis; software engineers add consistent handling of records and failure conditions. Effective bioinformatics takes all three perspectives seriously rather than treating a software report as its own justification.

### Running example and evidence hierarchy

A fictional ecology consortium processes sequence records from three research groups. Each group uses different identifiers and an imperfectly documented reference version. The correct first step is to reconcile provenance and define admissible records, not to run a fashionable statistical pipeline. The final scientific summary should include exclusions and uncertainty.

For this example, use an evidence hierarchy rather than a binary correct/incorrect answer. At the lowest level sit identity and integrity checks. Next come observed measurement patterns and elementary comparisons. Next come model-based predictions whose uncertainty depends on assumptions. Finally come claims about biological mechanism or action, which normally require a stronger study design or independent evidence. Students should be able to identify the level actually supported and refuse an unsupported jump between levels.

### Course integration

Use synthetically generated learning data in this book. For genuine human, animal or sensitive ecological records, appropriate consent, permits, access control, community interests and institutional governance matter. Reproducibility does not entitle everyone to the raw dataset; derived outputs and controlled access may be better solutions.

The end-of-unit study uses a fictional dataset so students can audit the entire workflow without accessing private data or claiming to have made new biological discoveries. Record all transformations in a log, include the rejected observations and state explicitly how a different cutoff or model might change the narrative.

## Learning outcomes

By the end of this unit you should be able to: (1) define the five techniques in their proper inferential scope; (2) compute and audit the five numerical examples; (3) propose a minimal control or validation for an ambiguous result; (4) interpret each interactive model's assumptions; and (5) write a cautious, reproducible conclusion.

## Lesson 8.1 — Command line and scripting practice

### Concept and biological meaning

A command-line workflow turns operations into versionable code with explicit inputs, outputs and failure conditions, reducing unrecorded manual changes. 

### Method and reproducible data contract

Quote file paths, handle nonzero exit statuses, validate schemas and use clear project directories with read-only originals. Before running an analysis, write down the input type, reference release, allowed missing values, expected columns and numerical settings. Record the observation level—organism, specimen, sequencing run, read, transcript, protein or residue—because the number of table rows need not equal the number of independent biological replicates. Reproduce one calculation using a tiny invented example and write an automatic assertion for its expected output. This validates implementation, not the scientific truth of the starting assumptions.

### Case study: a plausible signal and a rival explanation

A pipeline processes 20 FASTA files but two have whitespace in filenames and one is compressed unexpectedly. The first task is to frame a biological hypothesis and a specific technical or sampling alternative. Describe what would be observed if the preferred explanation were true, then name an observation that might discriminate it from the rival. Consider label mix-ups, reference changes, missingness and biased sample recruitment before treating agreement among software tools as independent confirmation.



### Worked quantitative example

If 18 of 20 validated files pass preflight, success fraction is 90%; downstream steps should not silently process the two rejects. Treat these numbers as fictional teaching inputs. Reproduce the arithmetic in your notes, identify the denominator and decide whether the answer has physical units, is a dimensionless proportion or is a model score. Explain which input change would mechanically alter the answer. A numerical value calculated exactly from inaccurate or unrepresentative data is still a limited scientific result.

### Caveats, sensitivity and evidence strength

A command that exits successfully may still produce biologically empty output if input validation is skipped. Copy-pasting commands into a shell history is not an auditable execution record unless the input and environment are preserved. 

### Independent evaluation and advanced extension

Write a short Python parser with input validation and an automated test using only synthetic short sequences. Use this extension as a miniature sensitivity study. Change one defensible setting at a time and record whether the inference remains stable. Where methods disagree, identify whether they use different definitions, references or sources of uncertainty. Avoid the practice of choosing whichever method produces the desired biological story.

**Failure and recovery.** A mature computational workflow reports failures explicitly: missing values, invalid identifiers, numerical instability, nonconvergent fits or violated assumptions. Silently deleting difficult observations can change the target population and make a polished result less credible. For **command line and scripting practice**, supply an actual auditable record—not a generic pledge of reproducibility—that would expose a mistaken assumption in the fictional case.

### Questions for mastery

1. What is directly observed, what is computed, and what is inferred? Explain the transitions using this lesson’s situation.
2. Which negative control, alternative model or independent observation could test a rival explanation? State what result would weaken your preferred account.
3. Repeat the numerical example after changing one input and report units, denominator and interpretation. Explain why a correct recalculation does not establish biological validity.
4. Which detail would another scientist need to rerun the analysis from precisely the same inputs? Describe a realistic failure if it were missing.



---
## Lesson 8.2 — Directed acyclic graphs and workflow engines

### Concept and biological meaning

A scientific pipeline can be described as a dependency graph where each transformation has declared inputs, outputs and parameters. 

### Method and reproducible data contract

Use reproducible rule definitions, fail-fast behavior, staged checkpoints and resource requirements; do not silently reuse stale intermediates. Before running an analysis, write down the input type, reference release, allowed missing values, expected columns and numerical settings. Record the observation level—organism, specimen, sequencing run, read, transcript, protein or residue—because the number of table rows need not equal the number of independent biological replicates. Reproduce one calculation using a tiny invented example and write an automatic assertion for its expected output. This validates implementation, not the scientific truth of the starting assumptions.

### Case study: a plausible signal and a rival explanation

A multi-step experiment performs QC, mapping, counting, modeling and plotting for four samples. The first task is to frame a biological hypothesis and a specific technical or sampling alternative. Describe what would be observed if the preferred explanation were true, then name an observation that might discriminate it from the rival. Consider label mix-ups, reference changes, missingness and biased sample recruitment before treating agreement among software tools as independent confirmation.



### Worked quantitative example

With serial tasks of 2, 4 and 3 minutes, critical path is 9 minutes; parallel sample-level processing may reduce wall time, not total compute. Treat these numbers as fictional teaching inputs. Reproduce the arithmetic in your notes, identify the denominator and decide whether the answer has physical units, is a dimensionless proportion or is a model score. Explain which input change would mechanically alter the answer. A numerical value calculated exactly from inaccurate or unrepresentative data is still a limited scientific result.

### Caveats, sensitivity and evidence strength

If a reference or parameter changes, downstream artifacts must be recomputed as dictated by dependencies rather than reused by filename. An uninterrupted sequence of commands is not equivalent to an auditable workflow with input checksums and dependency tracking. 

### Independent evaluation and advanced extension

Draw a DAG with three sample branches and one aggregate analysis, naming reproducible artifacts and failure states. Use this extension as a miniature sensitivity study. Change one defensible setting at a time and record whether the inference remains stable. Where methods disagree, identify whether they use different definitions, references or sources of uncertainty. Avoid the practice of choosing whichever method produces the desired biological story.

**Transfer of conclusions.** A numerical relationship estimated on a small classroom dataset can demonstrate a procedure without transferring to another organism or technology. External validity is an empirical question; record domain, reference, experimental setting and foreseeable distribution shift. For **directed acyclic graphs and workflow engines**, supply an actual auditable record—not a generic pledge of reproducibility—that would expose a mistaken assumption in the fictional case.

### Questions for mastery

1. What is directly observed, what is computed, and what is inferred? Explain the transitions using this lesson’s situation.
2. Which negative control, alternative model or independent observation could test a rival explanation? State what result would weaken your preferred account.
3. Repeat the numerical example after changing one input and report units, denominator and interpretation. Explain why a correct recalculation does not establish biological validity.
4. Which detail would another scientist need to rerun the analysis from precisely the same inputs? Describe a realistic failure if it were missing.



---
## Lesson 8.3 — Containers, environments and computational scaling

### Concept and biological meaning

Computational reproducibility requires constrained software versions, reference data identity and platform-aware execution, not only a script copied between machines. 

### Method and reproducible data contract

Pin package versions, document architecture, record container image digest and separate CPU, memory, disk and network constraints. Before running an analysis, write down the input type, reference release, allowed missing values, expected columns and numerical settings. Record the observation level—organism, specimen, sequencing run, read, transcript, protein or residue—because the number of table rows need not equal the number of independent biological replicates. Reproduce one calculation using a tiny invented example and write an automatic assertion for its expected output. This validates implementation, not the scientific truth of the starting assumptions.

### Case study: a plausible signal and a rival explanation

A program produces a new annotation after a database update even though its command line and Python code stayed unchanged. The first task is to frame a biological hypothesis and a specific technical or sampling alternative. Describe what would be observed if the preferred explanation were true, then name an observation that might discriminate it from the rival. Consider label mix-ups, reference changes, missingness and biased sample recruitment before treating agreement among software tools as independent confirmation.



### Worked quantitative example

A job using 3 GB per worker cannot safely allocate four such workers within an 8 GB memory limit without accounting for overhead. Treat these numbers as fictional teaching inputs. Reproduce the arithmetic in your notes, identify the denominator and decide whether the answer has physical units, is a dimensionless proportion or is a model score. Explain which input change would mechanically alter the answer. A numerical value calculated exactly from inaccurate or unrepresentative data is still a limited scientific result.

### Caveats, sensitivity and evidence strength

Containerizing tools does not freeze external web services or database records; hidden dependencies still matter. Adding threads can increase memory use or I/O contention so speedup is not guaranteed to follow the number of cores. 

### Independent evaluation and advanced extension

Provide a resource budget and explain when chunking, caching or cloud storage is warranted without overstating cost savings. Use this extension as a miniature sensitivity study. Change one defensible setting at a time and record whether the inference remains stable. Where methods disagree, identify whether they use different definitions, references or sources of uncertainty. Avoid the practice of choosing whichever method produces the desired biological story.

**Biological unit.** Count the unit actually sampled rather than the number of rows generated by instruments or algorithms. Repeated reads, peptides, contigs or scans may improve measurement of one specimen without increasing independence for population-level inference. For **containers, environments and computational scaling**, supply an actual auditable record—not a generic pledge of reproducibility—that would expose a mistaken assumption in the fictional case.

### Questions for mastery

1. What is directly observed, what is computed, and what is inferred? Explain the transitions using this lesson’s situation.
2. Which negative control, alternative model or independent observation could test a rival explanation? State what result would weaken your preferred account.
3. Repeat the numerical example after changing one input and report units, denominator and interpretation. Explain why a correct recalculation does not establish biological validity.
4. Which detail would another scientist need to rerun the analysis from precisely the same inputs? Describe a realistic failure if it were missing.



---
## Lesson 8.4 — Integrity, access control and responsible genomics

### Concept and biological meaning

Responsible computation protects participant autonomy, sample privacy, consent constraints and data integrity alongside reproducibility and open learning. 

### Method and reproducible data contract

Pseudonymization, minimum necessary access, retention policy and authorized storage matter because DNA sequences can be indirectly identifying. Before running an analysis, write down the input type, reference release, allowed missing values, expected columns and numerical settings. Record the observation level—organism, specimen, sequencing run, read, transcript, protein or residue—because the number of table rows need not equal the number of independent biological replicates. Reproduce one calculation using a tiny invented example and write an automatic assertion for its expected output. This validates implementation, not the scientific truth of the starting assumptions.

### Case study: a plausible signal and a rival explanation

A student wants to publish a small human cohort dataset with removed names but detailed variant and demographic columns. The first task is to frame a biological hypothesis and a specific technical or sampling alternative. Describe what would be observed if the preferred explanation were true, then name an observation that might discriminate it from the rival. Consider label mix-ups, reference changes, missingness and biased sample recruitment before treating agreement among software tools as independent confirmation.



### Worked quantitative example

If 3 of 50 input files have checksum mismatches, integrity failure rate is 6%; every mismatch needs investigation before analysis. Treat these numbers as fictional teaching inputs. Reproduce the arithmetic in your notes, identify the denominator and decide whether the answer has physical units, is a dimensionless proportion or is a model score. Explain which input change would mechanically alter the answer. A numerical value calculated exactly from inaccurate or unrepresentative data is still a limited scientific result.

### Caveats, sensitivity and evidence strength

Removing direct identifiers does not make genomic records anonymous, and repository visibility does not imply appropriate consent. A checksum proves byte equality across two copies, not ethical permission to distribute or scientific correctness. 

### Independent evaluation and advanced extension

Use wholly fictional sequences in public teaching exercises and document how a restricted-data analysis would be audited without exposing samples. Use this extension as a miniature sensitivity study. Change one defensible setting at a time and record whether the inference remains stable. Where methods disagree, identify whether they use different definitions, references or sources of uncertainty. Avoid the practice of choosing whichever method produces the desired biological story.

**Model adequacy.** Mathematical formulas compress real biological processes. Before interpreting a parameter, check limiting cases, dimensional consistency and residual patterns. Simple models can sharpen reasoning precisely because their omissions are transparent. For **integrity, access control and responsible genomics**, supply an actual auditable record—not a generic pledge of reproducibility—that would expose a mistaken assumption in the fictional case.

### Questions for mastery

1. What is directly observed, what is computed, and what is inferred? Explain the transitions using this lesson’s situation.
2. Which negative control, alternative model or independent observation could test a rival explanation? State what result would weaken your preferred account.
3. Repeat the numerical example after changing one input and report units, denominator and interpretation. Explain why a correct recalculation does not establish biological validity.
4. Which detail would another scientist need to rerun the analysis from precisely the same inputs? Describe a realistic failure if it were missing.



---
## Lesson 8.5 — Capstone: evidence-to-interpretation pipeline

### Concept and biological meaning

A complete bioinformatics argument links a question, sampling strategy, identified data, quality control, computational transformations, uncertainty and a restrained conclusion. 

### Method and reproducible data contract

Define the estimand and comparison, register reference releases and methods, collect QC artifacts, interpret competing explanations and retain a failure log. Before running an analysis, write down the input type, reference release, allowed missing values, expected columns and numerical settings. Record the observation level—organism, specimen, sequencing run, read, transcript, protein or residue—because the number of table rows need not equal the number of independent biological replicates. Reproduce one calculation using a tiny invented example and write an automatic assertion for its expected output. This validates implementation, not the scientific truth of the starting assumptions.

### Case study: a plausible signal and a rival explanation

A fictional field ecology study asks whether a stress gradient is associated with expression differences in a nonmodel plant. The first task is to frame a biological hypothesis and a specific technical or sampling alternative. Describe what would be observed if the preferred explanation were true, then name an observation that might discriminate it from the rival. Consider label mix-ups, reference changes, missingness and biased sample recruitment before treating agreement among software tools as independent confirmation.



### Worked quantitative example

In a synthetic class exercise, 12 planned samples and 2 exclusions leave 10 analyzable units; the 16.7% exclusion rate must be reported. Treat these numbers as fictional teaching inputs. Reproduce the arithmetic in your notes, identify the denominator and decide whether the answer has physical units, is a dimensionless proportion or is a model score. Explain which input change would mechanically alter the answer. A numerical value calculated exactly from inaccurate or unrepresentative data is still a limited scientific result.

### Caveats, sensitivity and evidence strength

An associated sequence signature might reflect species composition, tissue condition, batch or environmental covariates instead of causal adaptation. A visually compelling plot is not a self-validating conclusion, particularly when alternative processing settings change the result. 

### Independent evaluation and advanced extension

Produce a complete reproducibility package with synthetic inputs, declared methods, numeric answer checks, limitations and a proposed confirmatory study. Use this extension as a miniature sensitivity study. Change one defensible setting at a time and record whether the inference remains stable. Where methods disagree, identify whether they use different definitions, references or sources of uncertainty. Avoid the practice of choosing whichever method produces the desired biological story.

**Reproducible decisions.** A reader should be able to regenerate the same derived table from the same inputs and explicit settings. Preserve a checksum and environment record, and keep a log of decisions that change which records enter the analysis. For **capstone: evidence-to-interpretation pipeline**, supply an actual auditable record—not a generic pledge of reproducibility—that would expose a mistaken assumption in the fictional case.

### Questions for mastery

1. What is directly observed, what is computed, and what is inferred? Explain the transitions using this lesson’s situation.
2. Which negative control, alternative model or independent observation could test a rival explanation? State what result would weaken your preferred account.
3. Repeat the numerical example after changing one input and report units, denominator and interpretation. Explain why a correct recalculation does not establish biological validity.
4. Which detail would another scientist need to rerun the analysis from precisely the same inputs? Describe a realistic failure if it were missing.



---

## Integrated laboratory 8: an auditable evidence chain

**Setting.** Your undergraduate group receives fictional records about a small collection of biological material. The file descriptions are intentionally imperfect. The exercise focuses on **command line and scripting practice, directed acyclic graphs and workflow engines, containers, environments and computational scaling, integrity, access control and responsible genomics, capstone: evidence-to-interpretation pipeline** as five aspects of one argument rather than five disconnected tool demonstrations. No live database submissions, human specimen data, laboratory samples or web API credentials are required.

**Question formation.** Begin with the question in the unit introduction. Rewrite it as a comparison of named observations, identify the unit of sampling and decide what counts as a missing or uninterpretable value. Include a skeptical alternative hypothesis. For example, an association between two measurements could reflect a common technical batch rather than a causal connection. A sensible plan makes that alternative visible before results are plotted.

**Table design.** Create a machine-readable table with fields `record_id`, `biological_unit_id`, `source_release`, `assay_or_algorithm`, `quality_note`, `value`, `unit` and `exclusion_reason`. State which fields can be blank, what the file encoding is, and how missingness is represented. Never represent a missing quantitative measurement as zero unless zero is a genuine recorded value. If two rows share the same biological unit, decide whether they are technical repeats or separate conditions before assigning inferential sample size.

**Computation plan.** Reproduce the numerical case from each of the five lessons by hand. Put the given values and final expressions into a transparent notebook or script. Build a validation assertion for each worked result, add one deliberately malformed record and document its rejection. Verify that each numerical result has a denominator, unit or declared scale. The exercise does not ask you to rerun sophisticated tools on real genomes; it asks for defensible reasoning about toy outputs.

**Sensitivity and counterexamples.** Perform two controlled changes. First vary a parameter that the method explicitly allows the analyst to choose, such as a gap cost, cutoff, filter or comparison baseline. Second introduce a metadata problem such as duplicate labels or a mismatched reference version. Predict the consequences before performing the changed calculation. A surprising result should trigger investigation rather than selective deletion.

**Scientific interpretation.** Prepare a figure caption with the method, invented input description, assumptions and excluded observations. Write a conclusion with one supported statement, one plausible rival explanation and one test that would improve confidence. The conclusion must not convert a sequence match into experimental function, a score into clinical truth, a correlation into causation or a diagram into exact evolutionary history.

**Peer review rubric.** A second student receives only the manifest, script, small input table, expected numeric outputs and explanatory notes. Award one point each for exact input identity, correct sampling unit, reproducible arithmetic, transparent uncertainty and appropriate claim boundaries. A score of five means the teaching exercise was reported clearly; it is not independent scientific validation of the underlying assumptions.

**Discussion prompt.** If a second software package reproduces the same output, what failure modes remain? Could both tools share a database annotation, an unrepresentative sample or an invalid conceptual assumption? Suggest one independent observation that would provide new evidence rather than only computational agreement.
