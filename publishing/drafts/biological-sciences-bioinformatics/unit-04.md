# Unit 04 — Computational phylogenetics and tree interpretation

> **OpenSTEM Bioinformatics · Book 15 · Editorial draft.** All instructional sequences, measurements, cases and figures in this unit are fictional. Scientific peer review and publication approval are pending.

## The question driving this unit

**Which parts of an evolutionary history can molecular comparisons identify?**

Phylogenetic analysis first proposes positional homology through alignment, then models substitutions and often reconstructs relationships among sequences. Each stage introduces uncertainty. A tree topology, branch length, rooting strategy and support measure answer different questions and should never be treated as interchangeable.

### Why this subject needs both biology and computation

Distance summaries discard some alignment information, while likelihood approaches evaluate site-pattern evidence under explicit substitution models. Neither approach guarantees a unique true history. Gene trees can disagree with species histories through duplication, incomplete lineage sorting, recombination or horizontal gene movement.

Computational methods are valuable because they allow a question to be formulated as an explicit transformation: which inputs enter the calculation, which parameters matter, what optimization or probability rule is applied, and which output should be checked against another observation. Biologists add knowledge of sampling, function and evolutionary history; statisticians add uncertainty analysis; software engineers add consistent handling of records and failure conditions. Effective bioinformatics takes all three perspectives seriously rather than treating a software report as its own justification.

### Running example and evidence hierarchy

Suppose two plant chloroplast loci group three species differently. The first impulse may be to average all sequences into a single supermatrix, but conflicting histories deserve inspection. Missing taxa, heterogeneous rates, misaligned regions and locus-specific history should be considered. Reporting uncertainty can be more scientifically useful than forcing one diagram.

For this example, use an evidence hierarchy rather than a binary correct/incorrect answer. At the lowest level sit identity and integrity checks. Next come observed measurement patterns and elementary comparisons. Next come model-based predictions whose uncertainty depends on assumptions. Finally come claims about biological mechanism or action, which normally require a stronger study design or independent evidence. Students should be able to identify the level actually supported and refuse an unsupported jump between levels.

### Course integration

A bootstrap percentage measures resampling stability for the specified procedure, not the probability that a historical claim is true. Similarly, substitutions per site are not years without an independent calibration. Trees are coordinate-free hypotheses: rotating branches does not change relationships, even though page layout may affect visual intuition.

The end-of-unit study uses a fictional dataset so students can audit the entire workflow without accessing private data or claiming to have made new biological discoveries. Record all transformations in a log, include the rejected observations and state explicitly how a different cutoff or model might change the narrative.

## Learning outcomes

By the end of this unit you should be able to: (1) define the five techniques in their proper inferential scope; (2) compute and audit the five numerical examples; (3) propose a minimal control or validation for an ambiguous result; (4) interpret each interactive model's assumptions; and (5) write a cautious, reproducible conclusion.

## Lesson 4.1 — Multiple sequence alignment

### Concept and biological meaning

Multiple alignment creates a site-wise hypothesis of positional homology across sequences; uncertain placement propagates into trees, motifs and ancestral reconstruction. 

### Method and reproducible data contract

Inspect gaps, low-complexity regions and unstable blocks; keep alignment parameters and avoid manual edits made only to produce a desired tree. Before running an analysis, write down the input type, reference release, allowed missing values, expected columns and numerical settings. Record the observation level—organism, specimen, sequencing run, read, transcript, protein or residue—because the number of table rows need not equal the number of independent biological replicates. Reproduce one calculation using a tiny invented example and write an automatic assertion for its expected output. This validates implementation, not the scientific truth of the starting assumptions.

### Case study: a plausible signal and a rival explanation

Ten homologous proteins share a stable catalytic core but disordered termini of variable length. The first task is to frame a biological hypothesis and a specific technical or sampling alternative. Describe what would be observed if the preferred explanation were true, then name an observation that might discriminate it from the rival. Consider label mix-ups, reference changes, missingness and biased sample recruitment before treating agreement among software tools as independent confirmation.



### Worked quantitative example

A 200-column alignment with 20 gap-rich columns has 90% retained columns after exclusion, but removing them can bias branch lengths. Treat these numbers as fictional teaching inputs. Reproduce the arithmetic in your notes, identify the denominator and decide whether the answer has physical units, is a dimensionless proportion or is a model score. Explain which input change would mechanically alter the answer. A numerical value calculated exactly from inaccurate or unrepresentative data is still a limited scientific result.

### Caveats, sensitivity and evidence strength

No alignment algorithm can recover historical homology with certainty from low-information regions; different methods may yield different columns. Treating visually aligned columns as unequivocally homologous ignores alternative histories, recombination and structural shifts. 

### Independent evaluation and advanced extension

Run two alignment settings on a toy set and identify conclusions robust to ambiguous columns rather than choosing the more attractive output. Use this extension as a miniature sensitivity study. Change one defensible setting at a time and record whether the inference remains stable. Where methods disagree, identify whether they use different definitions, references or sources of uncertainty. Avoid the practice of choosing whichever method produces the desired biological story.

**Reproducible decisions.** A reader should be able to regenerate the same derived table from the same inputs and explicit settings. Preserve a checksum and environment record, and keep a log of decisions that change which records enter the analysis. For **multiple sequence alignment**, supply an actual auditable record—not a generic pledge of reproducibility—that would expose a mistaken assumption in the fictional case.

### Questions for mastery

1. What is directly observed, what is computed, and what is inferred? Explain the transitions using this lesson’s situation.
2. Which negative control, alternative model or independent observation could test a rival explanation? State what result would weaken your preferred account.
3. Repeat the numerical example after changing one input and report units, denominator and interpretation. Explain why a correct recalculation does not establish biological validity.
4. Which detail would another scientist need to rerun the analysis from precisely the same inputs? Describe a realistic failure if it were missing.



---
## Lesson 4.2 — Pairwise evolutionary distances

### Concept and biological meaning

Evolutionary distance estimates substitutions per site after correcting observed differences for repeated changes; p-distance is simply observed fraction mismatched. 

### Method and reproducible data contract

Use a model matched to sequence type and range of divergence, and explain why uncertainty rises as observed differences saturate. Before running an analysis, write down the input type, reference release, allowed missing values, expected columns and numerical settings. Record the observation level—organism, specimen, sequencing run, read, transcript, protein or residue—because the number of table rows need not equal the number of independent biological replicates. Reproduce one calculation using a tiny invented example and write an automatic assertion for its expected output. This validates implementation, not the scientific truth of the starting assumptions.

### Case study: a plausible signal and a rival explanation

Two hypothetical DNA fragments differ at 10 of 100 confidently aligned positions. The first task is to frame a biological hypothesis and a specific technical or sampling alternative. Describe what would be observed if the preferred explanation were true, then name an observation that might discriminate it from the rival. Consider label mix-ups, reference changes, missingness and biased sample recruitment before treating agreement among software tools as independent confirmation.



### Worked quantitative example

With p=0.1, Jukes–Cantor distance is -(3/4) ln(1-4p/3) ≈ 0.10733 substitutions per site. Treat these numbers as fictional teaching inputs. Reproduce the arithmetic in your notes, identify the denominator and decide whether the answer has physical units, is a dimensionless proportion or is a model score. Explain which input change would mechanically alter the answer. A numerical value calculated exactly from inaccurate or unrepresentative data is still a limited scientific result.

### Caveats, sensitivity and evidence strength

Correction models make explicit assumptions about transition probabilities and base frequencies that may fail for biased genomes. A corrected substitution distance is not elapsed time unless rates have been calibrated using independent information. 

### Independent evaluation and advanced extension

Compute p-distance and JC distance at p=0.05 and p=0.5; discuss why the simpler approximation deteriorates. Use this extension as a miniature sensitivity study. Change one defensible setting at a time and record whether the inference remains stable. Where methods disagree, identify whether they use different definitions, references or sources of uncertainty. Avoid the practice of choosing whichever method produces the desired biological story.

**Operational definition.** Before computing, write an operational definition of the variable of interest, including its measurement unit, denominator, sampling level and admissible values. An operational definition is not bureaucracy; it is what makes two methods comparable and reveals when they answer different questions. For **pairwise evolutionary distances**, supply an actual auditable record—not a generic pledge of reproducibility—that would expose a mistaken assumption in the fictional case.

### Questions for mastery

1. What is directly observed, what is computed, and what is inferred? Explain the transitions using this lesson’s situation.
2. Which negative control, alternative model or independent observation could test a rival explanation? State what result would weaken your preferred account.
3. Repeat the numerical example after changing one input and report units, denominator and interpretation. Explain why a correct recalculation does not establish biological validity.
4. Which detail would another scientist need to rerun the analysis from precisely the same inputs? Describe a realistic failure if it were missing.



---
## Lesson 4.3 — Distance trees, UPGMA and neighbor joining

### Concept and biological meaning

Distance methods infer a topology from pairwise evolutionary dissimilarities; UPGMA assumes ultrametric distances, while neighbor joining does not require a strict clock. 

### Method and reproducible data contract

Validate matrix symmetry and nonnegative values; report whether rooting was imposed by clock assumptions or explicit outgroup evidence. Before running an analysis, write down the input type, reference release, allowed missing values, expected columns and numerical settings. Record the observation level—organism, specimen, sequencing run, read, transcript, protein or residue—because the number of table rows need not equal the number of independent biological replicates. Reproduce one calculation using a tiny invented example and write an automatic assertion for its expected output. This validates implementation, not the scientific truth of the starting assumptions.

### Case study: a plausible signal and a rival explanation

Four imagined species produce near-additive distances but one branch accumulated substitutions faster than the others. The first task is to frame a biological hypothesis and a specific technical or sampling alternative. Describe what would be observed if the preferred explanation were true, then name an observation that might discriminate it from the rival. Consider label mix-ups, reference changes, missingness and biased sample recruitment before treating agreement among software tools as independent confirmation.



### Worked quantitative example

For symmetric taxa with d(A,B)=0.2 and d(A,C)=0.8, A and B are closer in observed distance, but this does not itself establish the true root. Treat these numbers as fictional teaching inputs. Reproduce the arithmetic in your notes, identify the denominator and decide whether the answer has physical units, is a dimensionless proportion or is a model score. Explain which input change would mechanically alter the answer. A numerical value calculated exactly from inaccurate or unrepresentative data is still a limited scientific result.

### Caveats, sensitivity and evidence strength

UPGMA can cluster fast and slow lineages incorrectly under rate heterogeneity; neighbor joining remains a heuristic based on distances. A branch length displayed on a tree usually measures estimated substitutions per site, not necessarily years. 

### Independent evaluation and advanced extension

Compare an ultrametric synthetic matrix with a clock-violating matrix and describe which clustering rule changes. Use this extension as a miniature sensitivity study. Change one defensible setting at a time and record whether the inference remains stable. Where methods disagree, identify whether they use different definitions, references or sources of uncertainty. Avoid the practice of choosing whichever method produces the desired biological story.

**Independent confirmation.** Prefer independent forms of evidence to repeated analysis of the same imperfect input. A second algorithm may share the first algorithm’s reference bias or annotation assumption; an independently measured observation answers a more demanding question. For **distance trees, upgma and neighbor joining**, supply an actual auditable record—not a generic pledge of reproducibility—that would expose a mistaken assumption in the fictional case.

### Questions for mastery

1. What is directly observed, what is computed, and what is inferred? Explain the transitions using this lesson’s situation.
2. Which negative control, alternative model or independent observation could test a rival explanation? State what result would weaken your preferred account.
3. Repeat the numerical example after changing one input and report units, denominator and interpretation. Explain why a correct recalculation does not establish biological validity.
4. Which detail would another scientist need to rerun the analysis from precisely the same inputs? Describe a realistic failure if it were missing.



---
## Lesson 4.4 — Likelihood inference, bootstrap and model checking

### Concept and biological meaning

Maximum-likelihood phylogenetics evaluates how well tree and substitution-model parameters explain observed alignment patterns; resampling assesses stability under the chosen data procedure. 

### Method and reproducible data contract

Separate topology likelihood, branch-length optimization and bootstrap support; report model assumptions and inspect conflicting loci. Before running an analysis, write down the input type, reference release, allowed missing values, expected columns and numerical settings. Record the observation level—organism, specimen, sequencing run, read, transcript, protein or residue—because the number of table rows need not equal the number of independent biological replicates. Reproduce one calculation using a tiny invented example and write an automatic assertion for its expected output. This validates implementation, not the scientific truth of the starting assumptions.

### Case study: a plausible signal and a rival explanation

A gene tree strongly groups two taxa but another genomic locus produces a different grouping. The first task is to frame a biological hypothesis and a specific technical or sampling alternative. Describe what would be observed if the preferred explanation were true, then name an observation that might discriminate it from the rival. Consider label mix-ups, reference changes, missingness and biased sample recruitment before treating agreement among software tools as independent confirmation.



### Worked quantitative example

If a clade appears in 85 of 100 nonparametric bootstrap replicates, support is 85%; it is not automatically an 85% probability that the clade is true. Treat these numbers as fictional teaching inputs. Reproduce the arithmetic in your notes, identify the denominator and decide whether the answer has physical units, is a dimensionless proportion or is a model score. Explain which input change would mechanically alter the answer. A numerical value calculated exactly from inaccurate or unrepresentative data is still a limited scientific result.

### Caveats, sensitivity and evidence strength

Discordance can reflect gene duplication, incomplete lineage sorting, recombination, horizontal transfer or plain sampling noise. Resampling alignment columns does not repair wrong taxon labels or model misspecification. 

### Independent evaluation and advanced extension

Inspect support across loci and demonstrate a sensitivity analysis by excluding poorly aligned positions. Use this extension as a miniature sensitivity study. Change one defensible setting at a time and record whether the inference remains stable. Where methods disagree, identify whether they use different definitions, references or sources of uncertainty. Avoid the practice of choosing whichever method produces the desired biological story.

**Competing hypotheses.** Whenever one pattern appears to support a preferred biological story, deliberately develop a second explanation involving measurement, sampling or hidden structure. Specify what new observation would discriminate them and whether the proposed test is feasible. For **likelihood inference, bootstrap and model checking**, supply an actual auditable record—not a generic pledge of reproducibility—that would expose a mistaken assumption in the fictional case.

### Questions for mastery

1. What is directly observed, what is computed, and what is inferred? Explain the transitions using this lesson’s situation.
2. Which negative control, alternative model or independent observation could test a rival explanation? State what result would weaken your preferred account.
3. Repeat the numerical example after changing one input and report units, denominator and interpretation. Explain why a correct recalculation does not establish biological validity.
4. Which detail would another scientist need to rerun the analysis from precisely the same inputs? Describe a realistic failure if it were missing.



---
## Lesson 4.5 — Reading phylogenies without overclaiming

### Concept and biological meaning

A phylogenetic tree represents a hypothesis of shared ancestry and relative branching; rotations about internal nodes do not change topology. 

### Method and reproducible data contract

Distinguish unrooted relationships, outgroup rooting, support values and calibrated time; identify whether branch lengths have units of substitutions or time. Before running an analysis, write down the input type, reference release, allowed missing values, expected columns and numerical settings. Record the observation level—organism, specimen, sequencing run, read, transcript, protein or residue—because the number of table rows need not equal the number of independent biological replicates. Reproduce one calculation using a tiny invented example and write an automatic assertion for its expected output. This validates implementation, not the scientific truth of the starting assumptions.

### Case study: a plausible signal and a rival explanation

A published tree places a modern bacterium on a visually long terminal branch next to a fossil-calibrated clade. The first task is to frame a biological hypothesis and a specific technical or sampling alternative. Describe what would be observed if the preferred explanation were true, then name an observation that might discriminate it from the rival. Consider label mix-ups, reference changes, missingness and biased sample recruitment before treating agreement among software tools as independent confirmation.



### Worked quantitative example

In a three-taxon rooted tree with ((A,B),C), A and B share a more recent modeled ancestor than either shares with C. Treat these numbers as fictional teaching inputs. Reproduce the arithmetic in your notes, identify the denominator and decide whether the answer has physical units, is a dimensionless proportion or is a model score. Explain which input change would mechanically alter the answer. A numerical value calculated exactly from inaccurate or unrepresentative data is still a limited scientific result.

### Caveats, sensitivity and evidence strength

Tip position on a diagram is not a measure of evolutionary progress and living taxa do not descend from one another simply because their labels are adjacent. A strongly supported gene tree is not automatically a species tree, particularly when gene histories differ. 

### Independent evaluation and advanced extension

Draw two rotations of the same rooted tree, label the most recent common ancestors and compare statements invariant to drawing orientation. Use this extension as a miniature sensitivity study. Change one defensible setting at a time and record whether the inference remains stable. Where methods disagree, identify whether they use different definitions, references or sources of uncertainty. Avoid the practice of choosing whichever method produces the desired biological story.

**Failure and recovery.** A mature computational workflow reports failures explicitly: missing values, invalid identifiers, numerical instability, nonconvergent fits or violated assumptions. Silently deleting difficult observations can change the target population and make a polished result less credible. For **reading phylogenies without overclaiming**, supply an actual auditable record—not a generic pledge of reproducibility—that would expose a mistaken assumption in the fictional case.

### Questions for mastery

1. What is directly observed, what is computed, and what is inferred? Explain the transitions using this lesson’s situation.
2. Which negative control, alternative model or independent observation could test a rival explanation? State what result would weaken your preferred account.
3. Repeat the numerical example after changing one input and report units, denominator and interpretation. Explain why a correct recalculation does not establish biological validity.
4. Which detail would another scientist need to rerun the analysis from precisely the same inputs? Describe a realistic failure if it were missing.



---

## Integrated laboratory 4: an auditable evidence chain

**Setting.** Your undergraduate group receives fictional records about a small collection of biological material. The file descriptions are intentionally imperfect. The exercise focuses on **multiple sequence alignment, pairwise evolutionary distances, distance trees, upgma and neighbor joining, likelihood inference, bootstrap and model checking, reading phylogenies without overclaiming** as five aspects of one argument rather than five disconnected tool demonstrations. No live database submissions, human specimen data, laboratory samples or web API credentials are required.

**Question formation.** Begin with the question in the unit introduction. Rewrite it as a comparison of named observations, identify the unit of sampling and decide what counts as a missing or uninterpretable value. Include a skeptical alternative hypothesis. For example, an association between two measurements could reflect a common technical batch rather than a causal connection. A sensible plan makes that alternative visible before results are plotted.

**Table design.** Create a machine-readable table with fields `record_id`, `biological_unit_id`, `source_release`, `assay_or_algorithm`, `quality_note`, `value`, `unit` and `exclusion_reason`. State which fields can be blank, what the file encoding is, and how missingness is represented. Never represent a missing quantitative measurement as zero unless zero is a genuine recorded value. If two rows share the same biological unit, decide whether they are technical repeats or separate conditions before assigning inferential sample size.

**Computation plan.** Reproduce the numerical case from each of the five lessons by hand. Put the given values and final expressions into a transparent notebook or script. Build a validation assertion for each worked result, add one deliberately malformed record and document its rejection. Verify that each numerical result has a denominator, unit or declared scale. The exercise does not ask you to rerun sophisticated tools on real genomes; it asks for defensible reasoning about toy outputs.

**Sensitivity and counterexamples.** Perform two controlled changes. First vary a parameter that the method explicitly allows the analyst to choose, such as a gap cost, cutoff, filter or comparison baseline. Second introduce a metadata problem such as duplicate labels or a mismatched reference version. Predict the consequences before performing the changed calculation. A surprising result should trigger investigation rather than selective deletion.

**Scientific interpretation.** Prepare a figure caption with the method, invented input description, assumptions and excluded observations. Write a conclusion with one supported statement, one plausible rival explanation and one test that would improve confidence. The conclusion must not convert a sequence match into experimental function, a score into clinical truth, a correlation into causation or a diagram into exact evolutionary history.

**Peer review rubric.** A second student receives only the manifest, script, small input table, expected numeric outputs and explanatory notes. Award one point each for exact input identity, correct sampling unit, reproducible arithmetic, transparent uncertainty and appropriate claim boundaries. A score of five means the teaching exercise was reported clearly; it is not independent scientific validation of the underlying assumptions.

**Discussion prompt.** If a second software package reproduces the same output, what failure modes remain? Could both tools share a database annotation, an unrepresentative sample or an invalid conceptual assumption? Suggest one independent observation that would provide new evidence rather than only computational agreement.
