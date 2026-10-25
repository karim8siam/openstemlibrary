# Unit 02 — Sequence comparison and statistical search

> **OpenSTEM Bioinformatics · Book 15 · Editorial draft.** All instructional sequences, measurements, cases and figures in this unit are fictional. Scientific peer review and publication approval are pending.

## The question driving this unit

**When do two molecular strings provide credible evidence of shared evolutionary origin or function?**

An alignment is an explicit model of which positions correspond. Without its scoring scheme, an identity fraction is incomplete because gap placement and boundaries can change. Local search highlights conserved subsequences; global alignment assesses comparable full regions. Search statistics judge surprise under a background model, not experimental functional equivalence.

### Why this subject needs both biology and computation

Molecular strings are not ordinary character strings because residues have different substitution tendencies, codons impose structure, and biological insertion-deletion events often affect contiguous segments. The mathematical objective is therefore a carefully chosen proxy for an evolutionary story, not a direct recording of ancient events.

Computational methods are valuable because they allow a question to be formulated as an explicit transformation: which inputs enter the calculation, which parameters matter, what optimization or probability rule is applied, and which output should be checked against another observation. Biologists add knowledge of sampling, function and evolutionary history; statisticians add uncertainty analysis; software engineers add consistent handling of records and failure conditions. Effective bioinformatics takes all three perspectives seriously rather than treating a software report as its own justification.

### Running example and evidence hierarchy

In an imagined protein survey, a 60-residue kinase-like region aligns almost exactly between two otherwise dissimilar 800-residue proteins. The local score may be compelling, while a conclusion that the entire proteins have the same role is not. Coverage, domain order, sequence composition, localization and independent evidence must be examined together.

For this example, use an evidence hierarchy rather than a binary correct/incorrect answer. At the lowest level sit identity and integrity checks. Next come observed measurement patterns and elementary comparisons. Next come model-based predictions whose uncertainty depends on assumptions. Finally come claims about biological mechanism or action, which normally require a stronger study design or independent evidence. Students should be able to identify the level actually supported and refuse an unsupported jump between levels.

### Course integration

Learn to distinguish descriptive similarity, optimized alignment scores, database-search E-values and biological homology. A high-scoring match can be due to repetitive residues; a weak global match can coexist with strong shared domains. Record database size and algorithm versions because significance can shift when the reference collection changes.

The end-of-unit study uses a fictional dataset so students can audit the entire workflow without accessing private data or claiming to have made new biological discoveries. Record all transformations in a log, include the rejected observations and state explicitly how a different cutoff or model might change the narrative.

## Learning outcomes

By the end of this unit you should be able to: (1) define the five techniques in their proper inferential scope; (2) compute and audit the five numerical examples; (3) propose a minimal control or validation for an ambiguous result; (4) interpret each interactive model's assumptions; and (5) write a cautious, reproducible conclusion.

## Lesson 2.1 — Edit distance and similarity definitions

### Concept and biological meaning

Edit distance counts a minimum series of substitutions, insertions and deletions; biological similarity generally uses weighted scores rather than an unqualified identity percentage. 

### Method and reproducible data contract

Specify gap penalties and whether terminal gaps count; align sequences in an explicit orientation, and never infer homology from a trivial short exact match. Before running an analysis, write down the input type, reference release, allowed missing values, expected columns and numerical settings. Record the observation level—organism, specimen, sequencing run, read, transcript, protein or residue—because the number of table rows need not equal the number of independent biological replicates. Reproduce one calculation using a tiny invented example and write an automatic assertion for its expected output. This validates implementation, not the scientific truth of the starting assumptions.

### Case study: a plausible signal and a rival explanation

Two imagined genes share 92% identity over 20 aligned positions but only 20 positions were aligned out of a 1,000-base gene. The first task is to frame a biological hypothesis and a specific technical or sampling alternative. Describe what would be observed if the preferred explanation were true, then name an observation that might discriminate it from the rival. Consider label mix-ups, reference changes, missingness and biased sample recruitment before treating agreement among software tools as independent confirmation.



### Worked quantitative example

Three substitutions and one deletion under unit costs give edit distance four; with a gap-open cost three, the optimal scoring alignment may differ. Treat these numbers as fictional teaching inputs. Reproduce the arithmetic in your notes, identify the denominator and decide whether the answer has physical units, is a dimensionless proportion or is a model score. Explain which input change would mechanically alter the answer. A numerical value calculated exactly from inaccurate or unrepresentative data is still a limited scientific result.

### Caveats, sensitivity and evidence strength

Local identity of 92% over a tiny aligned segment is not 92% identity over whole genes and may reflect a low-complexity region. Percent identity is a descriptive property of an alignment; the biological relationship depends on coverage, composition, scoring and database context. 

### Independent evaluation and advanced extension

Compare the same toy pair under edit distance and a score with a gap-open penalty, documenting when preferred alignments change. Use this extension as a miniature sensitivity study. Change one defensible setting at a time and record whether the inference remains stable. Where methods disagree, identify whether they use different definitions, references or sources of uncertainty. Avoid the practice of choosing whichever method produces the desired biological story.

**Biological unit.** Count the unit actually sampled rather than the number of rows generated by instruments or algorithms. Repeated reads, peptides, contigs or scans may improve measurement of one specimen without increasing independence for population-level inference. For **edit distance and similarity definitions**, supply an actual auditable record—not a generic pledge of reproducibility—that would expose a mistaken assumption in the fictional case.

### Questions for mastery

1. What is directly observed, what is computed, and what is inferred? Explain the transitions using this lesson’s situation.
2. Which negative control, alternative model or independent observation could test a rival explanation? State what result would weaken your preferred account.
3. Repeat the numerical example after changing one input and report units, denominator and interpretation. Explain why a correct recalculation does not establish biological validity.
4. Which detail would another scientist need to rerun the analysis from precisely the same inputs? Describe a realistic failure if it were missing.



---
## Lesson 2.2 — Global alignment and Needleman–Wunsch

### Concept and biological meaning

Global dynamic programming computes the best end-to-end alignment under an additive scoring rule; the recurrence considers diagonal match, insertion and deletion transitions. 

### Method and reproducible data contract

Initialize matrix boundaries consistently with the stated gap costs; retain a traceback path instead of assuming the final score identifies one unique alignment. Before running an analysis, write down the input type, reference release, allowed missing values, expected columns and numerical settings. Record the observation level—organism, specimen, sequencing run, read, transcript, protein or residue—because the number of table rows need not equal the number of independent biological replicates. Reproduce one calculation using a tiny invented example and write an automatic assertion for its expected output. This validates implementation, not the scientific truth of the starting assumptions.

### Case study: a plausible signal and a rival explanation

Two homologous coding regions are roughly the same length, but a short internal deletion occurred in one lineage. The first task is to frame a biological hypothesis and a specific technical or sampling alternative. Describe what would be observed if the preferred explanation were true, then name an observation that might discriminate it from the rival. Consider label mix-ups, reference changes, missingness and biased sample recruitment before treating agreement among software tools as independent confirmation.



### Worked quantitative example

Using match +2, mismatch -1 and linear gap -2, an exact match of five bases scores 10 before any terminal-gap policy applies. Treat these numbers as fictional teaching inputs. Reproduce the arithmetic in your notes, identify the denominator and decide whether the answer has physical units, is a dimensionless proportion or is a model score. Explain which input change would mechanically alter the answer. A numerical value calculated exactly from inaccurate or unrepresentative data is still a limited scientific result.

### Caveats, sensitivity and evidence strength

End-to-end alignment is helpful for comparable regions; it can be misleading for sequences with unrelated flanking segments. A visually plausible alignment is not proof it maximizes the announced scoring scheme, especially when several optima tie. 

### Independent evaluation and advanced extension

Fill a four-by-four scoring matrix by hand, mark ties, and reconstruct all equal-score tracebacks for a short pair. Use this extension as a miniature sensitivity study. Change one defensible setting at a time and record whether the inference remains stable. Where methods disagree, identify whether they use different definitions, references or sources of uncertainty. Avoid the practice of choosing whichever method produces the desired biological story.

**Model adequacy.** Mathematical formulas compress real biological processes. Before interpreting a parameter, check limiting cases, dimensional consistency and residual patterns. Simple models can sharpen reasoning precisely because their omissions are transparent. For **global alignment and needleman–wunsch**, supply an actual auditable record—not a generic pledge of reproducibility—that would expose a mistaken assumption in the fictional case.

### Questions for mastery

1. What is directly observed, what is computed, and what is inferred? Explain the transitions using this lesson’s situation.
2. Which negative control, alternative model or independent observation could test a rival explanation? State what result would weaken your preferred account.
3. Repeat the numerical example after changing one input and report units, denominator and interpretation. Explain why a correct recalculation does not establish biological validity.
4. Which detail would another scientist need to rerun the analysis from precisely the same inputs? Describe a realistic failure if it were missing.



---
## Lesson 2.3 — Local alignment and Smith–Waterman

### Concept and biological meaning

Local alignment permits an optimal similar subsequence by flooring dynamic-programming cells at zero; traceback starts at the highest score and stops at zero. 

### Method and reproducible data contract

Use local search to find shared domains inside longer proteins, and report start and end coordinates in both original sequences. Before running an analysis, write down the input type, reference release, allowed missing values, expected columns and numerical settings. Record the observation level—organism, specimen, sequencing run, read, transcript, protein or residue—because the number of table rows need not equal the number of independent biological replicates. Reproduce one calculation using a tiny invented example and write an automatic assertion for its expected output. This validates implementation, not the scientific truth of the starting assumptions.

### Case study: a plausible signal and a rival explanation

A signaling protein has a conserved catalytic domain but gained a long regulatory tail in one lineage. The first task is to frame a biological hypothesis and a specific technical or sampling alternative. Describe what would be observed if the preferred explanation were true, then name an observation that might discriminate it from the rival. Consider label mix-ups, reference changes, missingness and biased sample recruitment before treating agreement among software tools as independent confirmation.



### Worked quantitative example

With match +2, mismatch -1 and gap -2, four exact aligned positions contribute score eight in the absence of extending penalties. Treat these numbers as fictional teaching inputs. Reproduce the arithmetic in your notes, identify the denominator and decide whether the answer has physical units, is a dimensionless proportion or is a model score. Explain which input change would mechanically alter the answer. A numerical value calculated exactly from inaccurate or unrepresentative data is still a limited scientific result.

### Caveats, sensitivity and evidence strength

Local alignment may conceal domain rearrangements or cause a shared low-complexity segment to dominate results unless composition is examined. Local maximum score alone provides no reliable genome-wide false-hit probability; significance depends on lengths and search space. 

### Independent evaluation and advanced extension

Compare local and global alignments for a domain-only match and explain why they answer different biological questions. Use this extension as a miniature sensitivity study. Change one defensible setting at a time and record whether the inference remains stable. Where methods disagree, identify whether they use different definitions, references or sources of uncertainty. Avoid the practice of choosing whichever method produces the desired biological story.

**Reproducible decisions.** A reader should be able to regenerate the same derived table from the same inputs and explicit settings. Preserve a checksum and environment record, and keep a log of decisions that change which records enter the analysis. For **local alignment and smith–waterman**, supply an actual auditable record—not a generic pledge of reproducibility—that would expose a mistaken assumption in the fictional case.

### Questions for mastery

1. What is directly observed, what is computed, and what is inferred? Explain the transitions using this lesson’s situation.
2. Which negative control, alternative model or independent observation could test a rival explanation? State what result would weaken your preferred account.
3. Repeat the numerical example after changing one input and report units, denominator and interpretation. Explain why a correct recalculation does not establish biological validity.
4. Which detail would another scientist need to rerun the analysis from precisely the same inputs? Describe a realistic failure if it were missing.



---
## Lesson 2.4 — Substitution matrices and gap penalties

### Concept and biological meaning

A substitution matrix assigns relative support to amino-acid replacements based on an empirical evolutionary model or curated alignments, while affine gaps distinguish opening a gap from extending it. 

### Method and reproducible data contract

Choose matrix and gap costs appropriate to expected divergence; document that a score is not a probability without calibration. Before running an analysis, write down the input type, reference release, allowed missing values, expected columns and numerical settings. Record the observation level—organism, specimen, sequencing run, read, transcript, protein or residue—because the number of table rows need not equal the number of independent biological replicates. Reproduce one calculation using a tiny invented example and write an automatic assertion for its expected output. This validates implementation, not the scientific truth of the starting assumptions.

### Case study: a plausible signal and a rival explanation

Two proteins preserve conservative replacements within a binding pocket while other sites drift substantially. The first task is to frame a biological hypothesis and a specific technical or sampling alternative. Describe what would be observed if the preferred explanation were true, then name an observation that might discriminate it from the rival. Consider label mix-ups, reference changes, missingness and biased sample recruitment before treating agreement among software tools as independent confirmation.



### Worked quantitative example

An affine gap of length three with open=5 and extend=1 costs 5+2×1=7 under the convention that opening includes the first residue. Treat these numbers as fictional teaching inputs. Reproduce the arithmetic in your notes, identify the denominator and decide whether the answer has physical units, is a dimensionless proportion or is a model score. Explain which input change would mechanically alter the answer. A numerical value calculated exactly from inaccurate or unrepresentative data is still a limited scientific result.

### Caveats, sensitivity and evidence strength

A larger raw score may result merely from length; normalized scores, domain architecture and independent annotations aid comparison. There are multiple gap-cost conventions; confusing open plus length times extension with open plus (length-1) times extension yields different reported numbers. 

### Independent evaluation and advanced extension

Perform a sensitivity analysis across two matrices and two gap regimes; note which conclusions remain stable. Use this extension as a miniature sensitivity study. Change one defensible setting at a time and record whether the inference remains stable. Where methods disagree, identify whether they use different definitions, references or sources of uncertainty. Avoid the practice of choosing whichever method produces the desired biological story.

**Operational definition.** Before computing, write an operational definition of the variable of interest, including its measurement unit, denominator, sampling level and admissible values. An operational definition is not bureaucracy; it is what makes two methods comparable and reveals when they answer different questions. For **substitution matrices and gap penalties**, supply an actual auditable record—not a generic pledge of reproducibility—that would expose a mistaken assumption in the fictional case.

### Questions for mastery

1. What is directly observed, what is computed, and what is inferred? Explain the transitions using this lesson’s situation.
2. Which negative control, alternative model or independent observation could test a rival explanation? State what result would weaken your preferred account.
3. Repeat the numerical example after changing one input and report units, denominator and interpretation. Explain why a correct recalculation does not establish biological validity.
4. Which detail would another scientist need to rerun the analysis from precisely the same inputs? Describe a realistic failure if it were missing.



---
## Lesson 2.5 — Search significance: BLAST, E-values and coverage

### Concept and biological meaning

A database search reports local matches; under its background model, the E-value approximates the expected number of matches with at least a given score in the searched space. 

### Method and reproducible data contract

Inspect query coverage, subject coverage, alignment length, score composition and database size alongside E-value; apply low-complexity masking where justified. Before running an analysis, write down the input type, reference release, allowed missing values, expected columns and numerical settings. Record the observation level—organism, specimen, sequencing run, read, transcript, protein or residue—because the number of table rows need not equal the number of independent biological replicates. Reproduce one calculation using a tiny invented example and write an automatic assertion for its expected output. This validates implementation, not the scientific truth of the starting assumptions.

### Case study: a plausible signal and a rival explanation

A protein domain returns a highly significant hit to a multidomain enzyme, but the rest of the protein has a different architecture. The first task is to frame a biological hypothesis and a specific technical or sampling alternative. Describe what would be observed if the preferred explanation were true, then name an observation that might discriminate it from the rival. Consider label mix-ups, reference changes, missingness and biased sample recruitment before treating agreement among software tools as independent confirmation.



### Worked quantitative example

If a search setting doubles effective database size while the score stays fixed, E approximately doubles under simple assumptions. Treat these numbers as fictional teaching inputs. Reproduce the arithmetic in your notes, identify the denominator and decide whether the answer has physical units, is a dimensionless proportion or is a model score. Explain which input change would mechanically alter the answer. A numerical value calculated exactly from inaccurate or unrepresentative data is still a limited scientific result.

### Caveats, sensitivity and evidence strength

A low E-value supports nonrandom similarity under the model, not identical function or experimentally demonstrated homology for every subregion. A tiny E-value can arise from one long conserved domain while the overall proteins are functionally distinct. 

### Independent evaluation and advanced extension

Record search algorithm, matrix, reference database release, query length, masking and domain coverage before annotating function. Use this extension as a miniature sensitivity study. Change one defensible setting at a time and record whether the inference remains stable. Where methods disagree, identify whether they use different definitions, references or sources of uncertainty. Avoid the practice of choosing whichever method produces the desired biological story.

**Independent confirmation.** Prefer independent forms of evidence to repeated analysis of the same imperfect input. A second algorithm may share the first algorithm’s reference bias or annotation assumption; an independently measured observation answers a more demanding question. For **search significance: blast, e-values and coverage**, supply an actual auditable record—not a generic pledge of reproducibility—that would expose a mistaken assumption in the fictional case.

### Questions for mastery

1. What is directly observed, what is computed, and what is inferred? Explain the transitions using this lesson’s situation.
2. Which negative control, alternative model or independent observation could test a rival explanation? State what result would weaken your preferred account.
3. Repeat the numerical example after changing one input and report units, denominator and interpretation. Explain why a correct recalculation does not establish biological validity.
4. Which detail would another scientist need to rerun the analysis from precisely the same inputs? Describe a realistic failure if it were missing.



---

## Integrated laboratory 2: an auditable evidence chain

**Setting.** Your undergraduate group receives fictional records about a small collection of biological material. The file descriptions are intentionally imperfect. The exercise focuses on **edit distance and similarity definitions, global alignment and needleman–wunsch, local alignment and smith–waterman, substitution matrices and gap penalties, search significance: blast, e-values and coverage** as five aspects of one argument rather than five disconnected tool demonstrations. No live database submissions, human specimen data, laboratory samples or web API credentials are required.

**Question formation.** Begin with the question in the unit introduction. Rewrite it as a comparison of named observations, identify the unit of sampling and decide what counts as a missing or uninterpretable value. Include a skeptical alternative hypothesis. For example, an association between two measurements could reflect a common technical batch rather than a causal connection. A sensible plan makes that alternative visible before results are plotted.

**Table design.** Create a machine-readable table with fields `record_id`, `biological_unit_id`, `source_release`, `assay_or_algorithm`, `quality_note`, `value`, `unit` and `exclusion_reason`. State which fields can be blank, what the file encoding is, and how missingness is represented. Never represent a missing quantitative measurement as zero unless zero is a genuine recorded value. If two rows share the same biological unit, decide whether they are technical repeats or separate conditions before assigning inferential sample size.

**Computation plan.** Reproduce the numerical case from each of the five lessons by hand. Put the given values and final expressions into a transparent notebook or script. Build a validation assertion for each worked result, add one deliberately malformed record and document its rejection. Verify that each numerical result has a denominator, unit or declared scale. The exercise does not ask you to rerun sophisticated tools on real genomes; it asks for defensible reasoning about toy outputs.

**Sensitivity and counterexamples.** Perform two controlled changes. First vary a parameter that the method explicitly allows the analyst to choose, such as a gap cost, cutoff, filter or comparison baseline. Second introduce a metadata problem such as duplicate labels or a mismatched reference version. Predict the consequences before performing the changed calculation. A surprising result should trigger investigation rather than selective deletion.

**Scientific interpretation.** Prepare a figure caption with the method, invented input description, assumptions and excluded observations. Write a conclusion with one supported statement, one plausible rival explanation and one test that would improve confidence. The conclusion must not convert a sequence match into experimental function, a score into clinical truth, a correlation into causation or a diagram into exact evolutionary history.

**Peer review rubric.** A second student receives only the manifest, script, small input table, expected numeric outputs and explanatory notes. Award one point each for exact input identity, correct sampling unit, reproducible arithmetic, transparent uncertainty and appropriate claim boundaries. A score of five means the teaching exercise was reported clearly; it is not independent scientific validation of the underlying assumptions.

**Discussion prompt.** If a second software package reproduces the same output, what failure modes remain? Could both tools share a database annotation, an unrepresentative sample or an invalid conceptual assumption? Suggest one independent observation that would provide new evidence rather than only computational agreement.
