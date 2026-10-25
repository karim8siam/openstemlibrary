# Unit 01 — Biological data, formats and responsible provenance

> **OpenSTEM Bioinformatics · Book 15 · Editorial draft.** All instructional sequences, measurements, cases and figures in this unit are fictional. Scientific peer review and publication approval are pending.

## The question driving this unit

**What does a bioinformatics file mean, and how do we know which biological observation it describes?**

Raw strings become data only when sample origin, measurement procedure and intended units are specified. A nucleotide sequence without reference orientation cannot support a genomic comparison; a quality character without encoding is not a probability; and an accession without version can point to a different record on a later date.

### Why this subject needs both biology and computation

A practical analyst should be able to audit five layers: material source, biological specimen, laboratory assay, digital representation and transformed research output. These layers may have one-to-many relationships: several runs can measure one specimen; one file can contain thousands of molecules; a consensus sequence can combine multiple reads. Failure to distinguish these levels leads directly to pseudoreplication.

Computational methods are valuable because they allow a question to be formulated as an explicit transformation: which inputs enter the calculation, which parameters matter, what optimization or probability rule is applied, and which output should be checked against another observation. Biologists add knowledge of sampling, function and evolutionary history; statisticians add uncertainty analysis; software engineers add consistent handling of records and failure conditions. Effective bioinformatics takes all three perspectives seriously rather than treating a software report as its own justification.

### Running example and evidence hierarchy

Consider a field collection of leaves from six plants. Each leaf receives a stable sample identifier, a collection date and a storage condition. Two sequencing lanes run for each extraction. The appropriate biological sample count is six, even though twelve technical outputs exist. The manifest maps each run back to the originating organism. A quality graph reports per-read uncertainty; it does not tell us whether the plant was correctly identified.

For this example, use an evidence hierarchy rather than a binary correct/incorrect answer. At the lowest level sit identity and integrity checks. Next come observed measurement patterns and elementary comparisons. Next come model-based predictions whose uncertainty depends on assumptions. Finally come claims about biological mechanism or action, which normally require a stronger study design or independent evidence. Students should be able to identify the level actually supported and refuse an unsupported jump between levels.

### Course integration

The five lessons form an evidence chain: validate sequence representation; interpret base-call uncertainty; freeze record identity; join metadata at the right sampling level; and preserve provenance with appropriate access controls. A decision to drop one poor-quality sample changes the population of observations. An identifier change can instead change which biological feature the sequence is claimed to represent. Both decisions belong in the audit trail.

The end-of-unit study uses a fictional dataset so students can audit the entire workflow without accessing private data or claiming to have made new biological discoveries. Record all transformations in a log, include the rejected observations and state explicitly how a different cutoff or model might change the narrative.

## Learning outcomes

By the end of this unit you should be able to: (1) define the five techniques in their proper inferential scope; (2) compute and audit the five numerical examples; (3) propose a minimal control or validation for an ambiguous result; (4) interpret each interactive model's assumptions; and (5) write a cautious, reproducible conclusion.

## Lesson 1.1 — FASTA sequences and reference records

### Concept and biological meaning

FASTA records separate a header beginning with > from one or more lines of sequence; the alphabet and the assembly context determine whether a string is meaningful DNA, RNA, or protein data. 

### Method and reproducible data contract

A parser should concatenate sequence lines, reject empty identifiers, preserve accession/version fields and record any noncanonical characters rather than silently changing them. Before running an analysis, write down the input type, reference release, allowed missing values, expected columns and numerical settings. Record the observation level—organism, specimen, sequencing run, read, transcript, protein or residue—because the number of table rows need not equal the number of independent biological replicates. Reproduce one calculation using a tiny invented example and write an automatic assertion for its expected output. This validates implementation, not the scientific truth of the starting assumptions.

### Case study: a plausible signal and a rival explanation

A comparative study receives mitochondrial fragments from four species but two headers abbreviate the same specimen name. The first task is to frame a biological hypothesis and a specific technical or sampling alternative. Describe what would be observed if the preferred explanation were true, then name an observation that might discriminate it from the rival. Consider label mix-ups, reference changes, missingness and biased sample recruitment before treating agreement among software tools as independent confirmation.



### Worked quantitative example

For lengths 450, 500 and 550 nucleotides, mean length equals 500 and range equals 100; report whether ambiguous N characters contributed to length. Treat these numbers as fictional teaching inputs. Reproduce the arithmetic in your notes, identify the denominator and decide whether the answer has physical units, is a dimensionless proportion or is a model score. Explain which input change would mechanically alter the answer. A numerical value calculated exactly from inaccurate or unrepresentative data is still a limited scientific result.

### Caveats, sensitivity and evidence strength

Sequence similarity cannot establish sample identity when header labels have been copied, aliases merged, or strand orientation lost. The common error is to assume the FASTA header proves origin; headers are annotations that can be wrong, unlike sequence characters that themselves are also subject to error. 

### Independent evaluation and advanced extension

Generate a validation manifest with stable record IDs, observed alphabet, length, count of ambiguity symbols, and the provenance of the reference release. Use this extension as a miniature sensitivity study. Change one defensible setting at a time and record whether the inference remains stable. Where methods disagree, identify whether they use different definitions, references or sources of uncertainty. Avoid the practice of choosing whichever method produces the desired biological story.

**Operational definition.** Before computing, write an operational definition of the variable of interest, including its measurement unit, denominator, sampling level and admissible values. An operational definition is not bureaucracy; it is what makes two methods comparable and reveals when they answer different questions. For **fasta sequences and reference records**, supply an actual auditable record—not a generic pledge of reproducibility—that would expose a mistaken assumption in the fictional case.

### Questions for mastery

1. What is directly observed, what is computed, and what is inferred? Explain the transitions using this lesson’s situation.
2. Which negative control, alternative model or independent observation could test a rival explanation? State what result would weaken your preferred account.
3. Repeat the numerical example after changing one input and report units, denominator and interpretation. Explain why a correct recalculation does not establish biological validity.
4. Which detail would another scientist need to rerun the analysis from precisely the same inputs? Describe a realistic failure if it were missing.



---
## Lesson 1.2 — FASTQ and quality scores

### Concept and biological meaning

FASTQ records connect each read to a quality string; Phred quality Q is defined as -10 log10 of the estimated probability of a base call error, not of a biological mutation. 

### Method and reproducible data contract

Each record contains four logical lines with matching sequence and quality lengths; offsets and encoding conventions should be established from metadata before processing. Before running an analysis, write down the input type, reference release, allowed missing values, expected columns and numerical settings. Record the observation level—organism, specimen, sequencing run, read, transcript, protein or residue—because the number of table rows need not equal the number of independent biological replicates. Reproduce one calculation using a tiny invented example and write an automatic assertion for its expected output. This validates implementation, not the scientific truth of the starting assumptions.

### Case study: a plausible signal and a rival explanation

A student compares the terminal ten bases of two libraries and observes declining quality in one but not the other. The first task is to frame a biological hypothesis and a specific technical or sampling alternative. Describe what would be observed if the preferred explanation were true, then name an observation that might discriminate it from the rival. Consider label mix-ups, reference changes, missingness and biased sample recruitment before treating agreement among software tools as independent confirmation.



### Worked quantitative example

For Q=20, estimated error probability is 0.01; for Q=30, it is 0.001, a tenfold rather than ten-percentage-point difference. Treat these numbers as fictional teaching inputs. Reproduce the arithmetic in your notes, identify the denominator and decide whether the answer has physical units, is a dimensionless proportion or is a model score. Explain which input change would mechanically alter the answer. A numerical value calculated exactly from inaccurate or unrepresentative data is still a limited scientific result.

### Caveats, sensitivity and evidence strength

High Phred scores are calibrated estimates, not guarantees, and systematic errors or mapping ambiguities remain invisible to a per-base score. Mistaking a quality histogram for a coverage histogram hides the fact that independent samples can have identical quality yet radically different representativeness. 

### Independent evaluation and advanced extension

Report per-cycle quality, ambiguity fraction, read length and fraction filtered with thresholds specified before comparing biological conditions. Use this extension as a miniature sensitivity study. Change one defensible setting at a time and record whether the inference remains stable. Where methods disagree, identify whether they use different definitions, references or sources of uncertainty. Avoid the practice of choosing whichever method produces the desired biological story.

**Independent confirmation.** Prefer independent forms of evidence to repeated analysis of the same imperfect input. A second algorithm may share the first algorithm’s reference bias or annotation assumption; an independently measured observation answers a more demanding question. For **fastq and quality scores**, supply an actual auditable record—not a generic pledge of reproducibility—that would expose a mistaken assumption in the fictional case.

### Questions for mastery

1. What is directly observed, what is computed, and what is inferred? Explain the transitions using this lesson’s situation.
2. Which negative control, alternative model or independent observation could test a rival explanation? State what result would weaken your preferred account.
3. Repeat the numerical example after changing one input and report units, denominator and interpretation. Explain why a correct recalculation does not establish biological validity.
4. Which detail would another scientist need to rerun the analysis from precisely the same inputs? Describe a realistic failure if it were missing.



---
## Lesson 1.3 — Database identifiers and versions

### Concept and biological meaning

An accession names a record while a version suffix or database release identifies a particular state of that record; identity across resources often requires explicit mappings. 

### Method and reproducible data contract

Keep the accession, version, organism, reference assembly, transcript accession and retrieval date as distinct fields rather than flattening them into a human-readable gene symbol. Before running an analysis, write down the input type, reference release, allowed missing values, expected columns and numerical settings. Record the observation level—organism, specimen, sequencing run, read, transcript, protein or residue—because the number of table rows need not equal the number of independent biological replicates. Reproduce one calculation using a tiny invented example and write an automatic assertion for its expected output. This validates implementation, not the scientific truth of the starting assumptions.

### Case study: a plausible signal and a rival explanation

An investigator quotes a variant at one coordinate from an older assembly and attempts to compare it with a newer reference. The first task is to frame a biological hypothesis and a specific technical or sampling alternative. Describe what would be observed if the preferred explanation were true, then name an observation that might discriminate it from the rival. Consider label mix-ups, reference changes, missingness and biased sample recruitment before treating agreement among software tools as independent confirmation.



### Worked quantitative example

If 12 of 200 accessions change version, the proportion updated is 12/200 = 6%; the remaining 94% is not evidence that annotations never changed. Treat these numbers as fictional teaching inputs. Reproduce the arithmetic in your notes, identify the denominator and decide whether the answer has physical units, is a dimensionless proportion or is a model score. Explain which input change would mechanically alter the answer. A numerical value calculated exactly from inaccurate or unrepresentative data is still a limited scientific result.

### Caveats, sensitivity and evidence strength

Coordinate-only matching can produce the wrong locus after an assembly update even if the chromosome number is unchanged. A gene name is neither a universal primary key nor an immutable identifier; paralogs, retired symbols and organism ambiguity complicate joins. 

### Independent evaluation and advanced extension

Resolve each external identifier using an audited mapping table and preserve unmapped records rather than silently dropping inconvenient cases. Use this extension as a miniature sensitivity study. Change one defensible setting at a time and record whether the inference remains stable. Where methods disagree, identify whether they use different definitions, references or sources of uncertainty. Avoid the practice of choosing whichever method produces the desired biological story.

**Competing hypotheses.** Whenever one pattern appears to support a preferred biological story, deliberately develop a second explanation involving measurement, sampling or hidden structure. Specify what new observation would discriminate them and whether the proposed test is feasible. For **database identifiers and versions**, supply an actual auditable record—not a generic pledge of reproducibility—that would expose a mistaken assumption in the fictional case.

### Questions for mastery

1. What is directly observed, what is computed, and what is inferred? Explain the transitions using this lesson’s situation.
2. Which negative control, alternative model or independent observation could test a rival explanation? State what result would weaken your preferred account.
3. Repeat the numerical example after changing one input and report units, denominator and interpretation. Explain why a correct recalculation does not establish biological validity.
4. Which detail would another scientist need to rerun the analysis from precisely the same inputs? Describe a realistic failure if it were missing.



---
## Lesson 1.4 — Metadata schemas and joining tables

### Concept and biological meaning

Biological tables form relationships among specimens, assay runs, subjects, treatments, batches and derived files; a key encodes a level of observation. 

### Method and reproducible data contract

Define one row per independent biological unit in the sample sheet and maintain separate sequencing-run identifiers so technical lanes do not masquerade as replicate individuals. Before running an analysis, write down the input type, reference release, allowed missing values, expected columns and numerical settings. Record the observation level—organism, specimen, sequencing run, read, transcript, protein or residue—because the number of table rows need not equal the number of independent biological replicates. Reproduce one calculation using a tiny invented example and write an automatic assertion for its expected output. This validates implementation, not the scientific truth of the starting assumptions.

### Case study: a plausible signal and a rival explanation

A cohort has four organisms, each measured twice on one sequencing instrument across two lanes. The first task is to frame a biological hypothesis and a specific technical or sampling alternative. Describe what would be observed if the preferred explanation were true, then name an observation that might discriminate it from the rival. Consider label mix-ups, reference changes, missingness and biased sample recruitment before treating agreement among software tools as independent confirmation.



### Worked quantitative example

Four organisms each sequenced in two lanes yield eight run entries but only four biological experimental units for between-organism inference. Treat these numbers as fictional teaching inputs. Reproduce the arithmetic in your notes, identify the denominator and decide whether the answer has physical units, is a dimensionless proportion or is a model score. Explain which input change would mechanically alter the answer. A numerical value calculated exactly from inaccurate or unrepresentative data is still a limited scientific result.

### Caveats, sensitivity and evidence strength

Treating eight lanes as eight biological replicates underestimates variability and exaggerates inferential precision. An apparently successful inner join can discard all samples whose identifiers carry a space or a leading zero. 

### Independent evaluation and advanced extension

Build a diagram of primary and foreign keys, require uniqueness, and compare row counts before and after every join. Use this extension as a miniature sensitivity study. Change one defensible setting at a time and record whether the inference remains stable. Where methods disagree, identify whether they use different definitions, references or sources of uncertainty. Avoid the practice of choosing whichever method produces the desired biological story.

**Failure and recovery.** A mature computational workflow reports failures explicitly: missing values, invalid identifiers, numerical instability, nonconvergent fits or violated assumptions. Silently deleting difficult observations can change the target population and make a polished result less credible. For **metadata schemas and joining tables**, supply an actual auditable record—not a generic pledge of reproducibility—that would expose a mistaken assumption in the fictional case.

### Questions for mastery

1. What is directly observed, what is computed, and what is inferred? Explain the transitions using this lesson’s situation.
2. Which negative control, alternative model or independent observation could test a rival explanation? State what result would weaken your preferred account.
3. Repeat the numerical example after changing one input and report units, denominator and interpretation. Explain why a correct recalculation does not establish biological validity.
4. Which detail would another scientist need to rerun the analysis from precisely the same inputs? Describe a realistic failure if it were missing.



---
## Lesson 1.5 — Data provenance, FAIR principles and licenses

### Concept and biological meaning

A reproducible result requires a traceable sequence from source accession and license to transformation, environment, intermediate outputs and final interpretation. 

### Method and reproducible data contract

Record acquisition URL, retrieval timestamp, checksum, release, software versions, parameters and restrictions on redistribution; distinguish findable metadata from openly reusable data. Before running an analysis, write down the input type, reference release, allowed missing values, expected columns and numerical settings. Record the observation level—organism, specimen, sequencing run, read, transcript, protein or residue—because the number of table rows need not equal the number of independent biological replicates. Reproduce one calculation using a tiny invented example and write an automatic assertion for its expected output. This validates implementation, not the scientific truth of the starting assumptions.

### Case study: a plausible signal and a rival explanation

A teaching notebook uses a publicly viewable human dataset whose consent does not permit public reposting of individual-level records. The first task is to frame a biological hypothesis and a specific technical or sampling alternative. Describe what would be observed if the preferred explanation were true, then name an observation that might discriminate it from the rival. Consider label mix-ups, reference changes, missingness and biased sample recruitment before treating agreement among software tools as independent confirmation.



### Worked quantitative example

A SHA-256 manifest allows an exact byte-level equality check; it does not certify the biological accuracy of those bytes. Treat these numbers as fictional teaching inputs. Reproduce the arithmetic in your notes, identify the denominator and decide whether the answer has physical units, is a dimensionless proportion or is a model score. Explain which input change would mechanically alter the answer. A numerical value calculated exactly from inaccurate or unrepresentative data is still a limited scientific result.

### Caveats, sensitivity and evidence strength

FAIR does not mean unrestricted public access: privacy, security and community governance can justify controlled access while permitting discovery. The misconception is that a script alone is sufficient reproducibility; without raw-data identity and environment documentation the same script may answer a different question. 

### Independent evaluation and advanced extension

Publish a synthetic demonstration dataset with a license note and an auditable README while keeping restricted original records outside the repository. Use this extension as a miniature sensitivity study. Change one defensible setting at a time and record whether the inference remains stable. Where methods disagree, identify whether they use different definitions, references or sources of uncertainty. Avoid the practice of choosing whichever method produces the desired biological story.

**Transfer of conclusions.** A numerical relationship estimated on a small classroom dataset can demonstrate a procedure without transferring to another organism or technology. External validity is an empirical question; record domain, reference, experimental setting and foreseeable distribution shift. For **data provenance, fair principles and licenses**, supply an actual auditable record—not a generic pledge of reproducibility—that would expose a mistaken assumption in the fictional case.

### Questions for mastery

1. What is directly observed, what is computed, and what is inferred? Explain the transitions using this lesson’s situation.
2. Which negative control, alternative model or independent observation could test a rival explanation? State what result would weaken your preferred account.
3. Repeat the numerical example after changing one input and report units, denominator and interpretation. Explain why a correct recalculation does not establish biological validity.
4. Which detail would another scientist need to rerun the analysis from precisely the same inputs? Describe a realistic failure if it were missing.



---

## Integrated laboratory 1: an auditable evidence chain

**Setting.** Your undergraduate group receives fictional records about a small collection of biological material. The file descriptions are intentionally imperfect. The exercise focuses on **fasta sequences and reference records, fastq and quality scores, database identifiers and versions, metadata schemas and joining tables, data provenance, fair principles and licenses** as five aspects of one argument rather than five disconnected tool demonstrations. No live database submissions, human specimen data, laboratory samples or web API credentials are required.

**Question formation.** Begin with the question in the unit introduction. Rewrite it as a comparison of named observations, identify the unit of sampling and decide what counts as a missing or uninterpretable value. Include a skeptical alternative hypothesis. For example, an association between two measurements could reflect a common technical batch rather than a causal connection. A sensible plan makes that alternative visible before results are plotted.

**Table design.** Create a machine-readable table with fields `record_id`, `biological_unit_id`, `source_release`, `assay_or_algorithm`, `quality_note`, `value`, `unit` and `exclusion_reason`. State which fields can be blank, what the file encoding is, and how missingness is represented. Never represent a missing quantitative measurement as zero unless zero is a genuine recorded value. If two rows share the same biological unit, decide whether they are technical repeats or separate conditions before assigning inferential sample size.

**Computation plan.** Reproduce the numerical case from each of the five lessons by hand. Put the given values and final expressions into a transparent notebook or script. Build a validation assertion for each worked result, add one deliberately malformed record and document its rejection. Verify that each numerical result has a denominator, unit or declared scale. The exercise does not ask you to rerun sophisticated tools on real genomes; it asks for defensible reasoning about toy outputs.

**Sensitivity and counterexamples.** Perform two controlled changes. First vary a parameter that the method explicitly allows the analyst to choose, such as a gap cost, cutoff, filter or comparison baseline. Second introduce a metadata problem such as duplicate labels or a mismatched reference version. Predict the consequences before performing the changed calculation. A surprising result should trigger investigation rather than selective deletion.

**Scientific interpretation.** Prepare a figure caption with the method, invented input description, assumptions and excluded observations. Write a conclusion with one supported statement, one plausible rival explanation and one test that would improve confidence. The conclusion must not convert a sequence match into experimental function, a score into clinical truth, a correlation into causation or a diagram into exact evolutionary history.

**Peer review rubric.** A second student receives only the manifest, script, small input table, expected numeric outputs and explanatory notes. Award one point each for exact input identity, correct sampling unit, reproducible arithmetic, transparent uncertainty and appropriate claim boundaries. A score of five means the teaching exercise was reported clearly; it is not independent scientific validation of the underlying assumptions.

**Discussion prompt.** If a second software package reproduces the same output, what failure modes remain? Could both tools share a database annotation, an unrepresentative sample or an invalid conceptual assumption? Suggest one independent observation that would provide new evidence rather than only computational agreement.
