# Unit 06 — Structural bioinformatics and molecular interpretation

> **OpenSTEM Bioinformatics · Book 15 · Editorial draft.** All instructional sequences, measurements, cases and figures in this unit are fictional. Scientific peer review and publication approval are pending.

## The question driving this unit

**How can three-dimensional models inform mechanisms without overstating their certainty?**

Coordinate files express geometric hypotheses supported by measurements, computations or both. The existence of a neat three-dimensional rendering does not imply that every residue was resolved, every conformational state was observed or every interface is biologically active.

### Why this subject needs both biology and computation

Structure analysis must preserve the selected chains and residues, confidence indicators and geometric definitions. A contact map depends on distance cutoff and atom choice; RMSD depends on superposition and atom selection. Predictions of a complex or binding pose require independent validation, particularly for flexible or disordered regions.

Computational methods are valuable because they allow a question to be formulated as an explicit transformation: which inputs enter the calculation, which parameters matter, what optimization or probability rule is applied, and which output should be checked against another observation. Biologists add knowledge of sampling, function and evolutionary history; statisticians add uncertainty analysis; software engineers add consistent handling of records and failure conditions. Effective bioinformatics takes all three perspectives seriously rather than treating a software report as its own justification.

### Running example and evidence hierarchy

A hypothetical plant enzyme has a tightly aligned catalytic domain and a poorly modeled regulatory segment. An overall rendering suggests a conserved fold, but claims about ligand accessibility depend on the uncertain segment. Reporting local coverage and confidence helps a reader separate a stable core from a speculative extension.

For this example, use an evidence hierarchy rather than a binary correct/incorrect answer. At the lowest level sit identity and integrity checks. Next come observed measurement patterns and elementary comparisons. Next come model-based predictions whose uncertainty depends on assumptions. Finally come claims about biological mechanism or action, which normally require a stronger study design or independent evidence. Students should be able to identify the level actually supported and refuse an unsupported jump between levels.

### Course integration

Think of structural computation as evidence integration. Sequence conservation may locate a plausible active region, an experimental map may delimit a fold, and a contact analysis may suggest steric constraints. Functional activity, binding affinity and in vivo relevance remain separate properties that require distinct evidence.

The end-of-unit study uses a fictional dataset so students can audit the entire workflow without accessing private data or claiming to have made new biological discoveries. Record all transformations in a log, include the rejected observations and state explicitly how a different cutoff or model might change the narrative.

## Learning outcomes

By the end of this unit you should be able to: (1) define the five techniques in their proper inferential scope; (2) compute and audit the five numerical examples; (3) propose a minimal control or validation for an ambiguous result; (4) interpret each interactive model's assumptions; and (5) write a cautious, reproducible conclusion.

## Lesson 6.1 — Protein structure records and confidence

### Concept and biological meaning

Macromolecular coordinates describe particular structural observations or predictions; experimental models and predictions carry different uncertainty representations. 

### Method and reproducible data contract

Inspect chains, ligands, unresolved residues, resolution or confidence metadata, biological assembly and residue numbering before analysis. Before running an analysis, write down the input type, reference release, allowed missing values, expected columns and numerical settings. Record the observation level—organism, specimen, sequencing run, read, transcript, protein or residue—because the number of table rows need not equal the number of independent biological replicates. Reproduce one calculation using a tiny invented example and write an automatic assertion for its expected output. This validates implementation, not the scientific truth of the starting assumptions.

### Case study: a plausible signal and a rival explanation

A structure file contains only one domain of a large membrane protein and omits flexible loops. The first task is to frame a biological hypothesis and a specific technical or sampling alternative. Describe what would be observed if the preferred explanation were true, then name an observation that might discriminate it from the rival. Consider label mix-ups, reference changes, missingness and biased sample recruitment before treating agreement among software tools as independent confirmation.



### Worked quantitative example

A model containing 180 resolved residues from a 220-residue sequence has coordinate coverage 180/220 ≈ 81.8%. Treat these numbers as fictional teaching inputs. Reproduce the arithmetic in your notes, identify the denominator and decide whether the answer has physical units, is a dimensionless proportion or is a model score. Explain which input change would mechanically alter the answer. A numerical value calculated exactly from inaccurate or unrepresentative data is still a limited scientific result.

### Caveats, sensitivity and evidence strength

Absence of coordinates is not evidence that residues do not exist, and high per-residue model confidence does not guarantee a complex is physically realized. Comparing two structures by residue number fails when construct tags, insertions or missing loops change numbering. 

### Independent evaluation and advanced extension

Create a coverage map and explicitly report which claims concern observed coordinates and which concern unmodeled regions. Use this extension as a miniature sensitivity study. Change one defensible setting at a time and record whether the inference remains stable. Where methods disagree, identify whether they use different definitions, references or sources of uncertainty. Avoid the practice of choosing whichever method produces the desired biological story.

**Independent confirmation.** Prefer independent forms of evidence to repeated analysis of the same imperfect input. A second algorithm may share the first algorithm’s reference bias or annotation assumption; an independently measured observation answers a more demanding question. For **protein structure records and confidence**, supply an actual auditable record—not a generic pledge of reproducibility—that would expose a mistaken assumption in the fictional case.

### Questions for mastery

1. What is directly observed, what is computed, and what is inferred? Explain the transitions using this lesson’s situation.
2. Which negative control, alternative model or independent observation could test a rival explanation? State what result would weaken your preferred account.
3. Repeat the numerical example after changing one input and report units, denominator and interpretation. Explain why a correct recalculation does not establish biological validity.
4. Which detail would another scientist need to rerun the analysis from precisely the same inputs? Describe a realistic failure if it were missing.



---
## Lesson 6.2 — Secondary structure and contacts

### Concept and biological meaning

Protein secondary structure summarizes local backbone geometry; residue contacts summarize spatial proximity under a chosen representation and cutoff. 

### Method and reproducible data contract

Define whether distance means C-alpha, heavy-atom minimum or side-chain centroid, and ensure that contacts near the sequence diagonal are interpreted appropriately. Before running an analysis, write down the input type, reference release, allowed missing values, expected columns and numerical settings. Record the observation level—organism, specimen, sequencing run, read, transcript, protein or residue—because the number of table rows need not equal the number of independent biological replicates. Reproduce one calculation using a tiny invented example and write an automatic assertion for its expected output. This validates implementation, not the scientific truth of the starting assumptions.

### Case study: a plausible signal and a rival explanation

A predicted helical bundle appears compact under an eight-angstrom C-alpha contact threshold. The first task is to frame a biological hypothesis and a specific technical or sampling alternative. Describe what would be observed if the preferred explanation were true, then name an observation that might discriminate it from the rival. Consider label mix-ups, reference changes, missingness and biased sample recruitment before treating agreement among software tools as independent confirmation.



### Worked quantitative example

A list of ten candidate residue pairs with six distances below eight angstrom gives a contact fraction of 60% under the declared rule. Treat these numbers as fictional teaching inputs. Reproduce the arithmetic in your notes, identify the denominator and decide whether the answer has physical units, is a dimensionless proportion or is a model score. Explain which input change would mechanically alter the answer. A numerical value calculated exactly from inaccurate or unrepresentative data is still a limited scientific result.

### Caveats, sensitivity and evidence strength

Changing the cutoff changes contact count, and contacts alone do not establish chemical bonding or folding stability. A contact map is a geometric summary and cannot by itself prove enzymatic activity or binding specificity. 

### Independent evaluation and advanced extension

Recompute a toy contact matrix at two cutoffs, masking immediate sequence neighbors, and compare long-range contact patterns. Use this extension as a miniature sensitivity study. Change one defensible setting at a time and record whether the inference remains stable. Where methods disagree, identify whether they use different definitions, references or sources of uncertainty. Avoid the practice of choosing whichever method produces the desired biological story.

**Competing hypotheses.** Whenever one pattern appears to support a preferred biological story, deliberately develop a second explanation involving measurement, sampling or hidden structure. Specify what new observation would discriminate them and whether the proposed test is feasible. For **secondary structure and contacts**, supply an actual auditable record—not a generic pledge of reproducibility—that would expose a mistaken assumption in the fictional case.

### Questions for mastery

1. What is directly observed, what is computed, and what is inferred? Explain the transitions using this lesson’s situation.
2. Which negative control, alternative model or independent observation could test a rival explanation? State what result would weaken your preferred account.
3. Repeat the numerical example after changing one input and report units, denominator and interpretation. Explain why a correct recalculation does not establish biological validity.
4. Which detail would another scientist need to rerun the analysis from precisely the same inputs? Describe a realistic failure if it were missing.



---
## Lesson 6.3 — Structural alignment and RMSD

### Concept and biological meaning

Structural alignment seeks corresponding residues and an optimal rigid-body superposition, commonly summarized by root-mean-square deviation for a selected atom set. 

### Method and reproducible data contract

Declare selection, chain pairing, flexible regions, superposition algorithm and whether RMSD is reported before or after optimal fitting. Before running an analysis, write down the input type, reference release, allowed missing values, expected columns and numerical settings. Record the observation level—organism, specimen, sequencing run, read, transcript, protein or residue—because the number of table rows need not equal the number of independent biological replicates. Reproduce one calculation using a tiny invented example and write an automatic assertion for its expected output. This validates implementation, not the scientific truth of the starting assumptions.

### Case study: a plausible signal and a rival explanation

Two proteins share a rigid core but one has a mobile loop controlling access to a pocket. The first task is to frame a biological hypothesis and a specific technical or sampling alternative. Describe what would be observed if the preferred explanation were true, then name an observation that might discriminate it from the rival. Consider label mix-ups, reference changes, missingness and biased sample recruitment before treating agreement among software tools as independent confirmation.



### Worked quantitative example

For fitted paired-atom squared deviations 1, 4 and 9 Å², RMSD is sqrt((1+4+9)/3) ≈ 2.16 Å. Treat these numbers as fictional teaching inputs. Reproduce the arithmetic in your notes, identify the denominator and decide whether the answer has physical units, is a dimensionless proportion or is a model score. Explain which input change would mechanically alter the answer. A numerical value calculated exactly from inaccurate or unrepresentative data is still a limited scientific result.

### Caveats, sensitivity and evidence strength

A low core RMSD can coexist with an important difference at an active site; global and local metrics answer different questions. Comparing RMSDs with different residue selections gives a misleading ranking even if the numerical values are precise. 

### Independent evaluation and advanced extension

Report the number of superposed atoms, sequence identity, coverage and both global and core-only geometric summaries. Use this extension as a miniature sensitivity study. Change one defensible setting at a time and record whether the inference remains stable. Where methods disagree, identify whether they use different definitions, references or sources of uncertainty. Avoid the practice of choosing whichever method produces the desired biological story.

**Failure and recovery.** A mature computational workflow reports failures explicitly: missing values, invalid identifiers, numerical instability, nonconvergent fits or violated assumptions. Silently deleting difficult observations can change the target population and make a polished result less credible. For **structural alignment and rmsd**, supply an actual auditable record—not a generic pledge of reproducibility—that would expose a mistaken assumption in the fictional case.

### Questions for mastery

1. What is directly observed, what is computed, and what is inferred? Explain the transitions using this lesson’s situation.
2. Which negative control, alternative model or independent observation could test a rival explanation? State what result would weaken your preferred account.
3. Repeat the numerical example after changing one input and report units, denominator and interpretation. Explain why a correct recalculation does not establish biological validity.
4. Which detail would another scientist need to rerun the analysis from precisely the same inputs? Describe a realistic failure if it were missing.



---
## Lesson 6.4 — Molecular interfaces and docking claims

### Concept and biological meaning

Interaction prediction ranks proposed relative arrangements using simplified energetic and geometric approximations; experimental binding evidence is a separate question. 

### Method and reproducible data contract

Inspect steric clashes, solvent exposure, interface residues, conformational ensembles and benchmark quality rather than treating the top ranked pose as measured truth. Before running an analysis, write down the input type, reference release, allowed missing values, expected columns and numerical settings. Record the observation level—organism, specimen, sequencing run, read, transcript, protein or residue—because the number of table rows need not equal the number of independent biological replicates. Reproduce one calculation using a tiny invented example and write an automatic assertion for its expected output. This validates implementation, not the scientific truth of the starting assumptions.

### Case study: a plausible signal and a rival explanation

Two docking programs predict different partner orientations for a protein with a flexible loop. The first task is to frame a biological hypothesis and a specific technical or sampling alternative. Describe what would be observed if the preferred explanation were true, then name an observation that might discriminate it from the rival. Consider label mix-ups, reference changes, missingness and biased sample recruitment before treating agreement among software tools as independent confirmation.



### Worked quantitative example

If a prediction contains 24 interface contacts and 6 clash flags, the raw clash-to-contact ratio is 6/24 = 0.25; interpretation depends on definitions. Treat these numbers as fictional teaching inputs. Reproduce the arithmetic in your notes, identify the denominator and decide whether the answer has physical units, is a dimensionless proportion or is a model score. Explain which input change would mechanically alter the answer. A numerical value calculated exactly from inaccurate or unrepresentative data is still a limited scientific result.

### Caveats, sensitivity and evidence strength

A score optimized for ranking candidates is not automatically a binding free energy or affinity measurement. High geometric overlap may reflect shared folds and not direct biological interaction between two particular proteins. 

### Independent evaluation and advanced extension

Create a short evidence hierarchy separating docking hypotheses, orthogonal assays and validated functional perturbations. Use this extension as a miniature sensitivity study. Change one defensible setting at a time and record whether the inference remains stable. Where methods disagree, identify whether they use different definitions, references or sources of uncertainty. Avoid the practice of choosing whichever method produces the desired biological story.

**Transfer of conclusions.** A numerical relationship estimated on a small classroom dataset can demonstrate a procedure without transferring to another organism or technology. External validity is an empirical question; record domain, reference, experimental setting and foreseeable distribution shift. For **molecular interfaces and docking claims**, supply an actual auditable record—not a generic pledge of reproducibility—that would expose a mistaken assumption in the fictional case.

### Questions for mastery

1. What is directly observed, what is computed, and what is inferred? Explain the transitions using this lesson’s situation.
2. Which negative control, alternative model or independent observation could test a rival explanation? State what result would weaken your preferred account.
3. Repeat the numerical example after changing one input and report units, denominator and interpretation. Explain why a correct recalculation does not establish biological validity.
4. Which detail would another scientist need to rerun the analysis from precisely the same inputs? Describe a realistic failure if it were missing.



---
## Lesson 6.5 — Comparative modeling and structural uncertainty

### Concept and biological meaning

Homology or comparative modeling builds a structural hypothesis using template evidence and sequence alignment; prediction quality varies across domains and conformations. 

### Method and reproducible data contract

Propagate template coverage, insertion boundaries and alignment uncertainty into confidence statements; compare multiple plausible states for dynamic systems. Before running an analysis, write down the input type, reference release, allowed missing values, expected columns and numerical settings. Record the observation level—organism, specimen, sequencing run, read, transcript, protein or residue—because the number of table rows need not equal the number of independent biological replicates. Reproduce one calculation using a tiny invented example and write an automatic assertion for its expected output. This validates implementation, not the scientific truth of the starting assumptions.

### Case study: a plausible signal and a rival explanation

A target protein has a 75% identical catalytic core but a novel 100-residue appendage. The first task is to frame a biological hypothesis and a specific technical or sampling alternative. Describe what would be observed if the preferred explanation were true, then name an observation that might discriminate it from the rival. Consider label mix-ups, reference changes, missingness and biased sample recruitment before treating agreement among software tools as independent confirmation.



### Worked quantitative example

A 400-residue target with a 260-residue aligned template has 65% template coverage, independently of local sequence identity. Treat these numbers as fictional teaching inputs. Reproduce the arithmetic in your notes, identify the denominator and decide whether the answer has physical units, is a dimensionless proportion or is a model score. Explain which input change would mechanically alter the answer. A numerical value calculated exactly from inaccurate or unrepresentative data is still a limited scientific result.

### Caveats, sensitivity and evidence strength

Excellent accuracy for a conserved domain says little about an untemplated appendage or an oligomeric arrangement. A single structural snapshot cannot represent all binding-induced motions or conditional conformational states. 

### Independent evaluation and advanced extension

Write an interpretation that names modeled regions, unmodeled uncertainty and a feasible independent validation route. Use this extension as a miniature sensitivity study. Change one defensible setting at a time and record whether the inference remains stable. Where methods disagree, identify whether they use different definitions, references or sources of uncertainty. Avoid the practice of choosing whichever method produces the desired biological story.

**Biological unit.** Count the unit actually sampled rather than the number of rows generated by instruments or algorithms. Repeated reads, peptides, contigs or scans may improve measurement of one specimen without increasing independence for population-level inference. For **comparative modeling and structural uncertainty**, supply an actual auditable record—not a generic pledge of reproducibility—that would expose a mistaken assumption in the fictional case.

### Questions for mastery

1. What is directly observed, what is computed, and what is inferred? Explain the transitions using this lesson’s situation.
2. Which negative control, alternative model or independent observation could test a rival explanation? State what result would weaken your preferred account.
3. Repeat the numerical example after changing one input and report units, denominator and interpretation. Explain why a correct recalculation does not establish biological validity.
4. Which detail would another scientist need to rerun the analysis from precisely the same inputs? Describe a realistic failure if it were missing.



---

## Integrated laboratory 6: an auditable evidence chain

**Setting.** Your undergraduate group receives fictional records about a small collection of biological material. The file descriptions are intentionally imperfect. The exercise focuses on **protein structure records and confidence, secondary structure and contacts, structural alignment and rmsd, molecular interfaces and docking claims, comparative modeling and structural uncertainty** as five aspects of one argument rather than five disconnected tool demonstrations. No live database submissions, human specimen data, laboratory samples or web API credentials are required.

**Question formation.** Begin with the question in the unit introduction. Rewrite it as a comparison of named observations, identify the unit of sampling and decide what counts as a missing or uninterpretable value. Include a skeptical alternative hypothesis. For example, an association between two measurements could reflect a common technical batch rather than a causal connection. A sensible plan makes that alternative visible before results are plotted.

**Table design.** Create a machine-readable table with fields `record_id`, `biological_unit_id`, `source_release`, `assay_or_algorithm`, `quality_note`, `value`, `unit` and `exclusion_reason`. State which fields can be blank, what the file encoding is, and how missingness is represented. Never represent a missing quantitative measurement as zero unless zero is a genuine recorded value. If two rows share the same biological unit, decide whether they are technical repeats or separate conditions before assigning inferential sample size.

**Computation plan.** Reproduce the numerical case from each of the five lessons by hand. Put the given values and final expressions into a transparent notebook or script. Build a validation assertion for each worked result, add one deliberately malformed record and document its rejection. Verify that each numerical result has a denominator, unit or declared scale. The exercise does not ask you to rerun sophisticated tools on real genomes; it asks for defensible reasoning about toy outputs.

**Sensitivity and counterexamples.** Perform two controlled changes. First vary a parameter that the method explicitly allows the analyst to choose, such as a gap cost, cutoff, filter or comparison baseline. Second introduce a metadata problem such as duplicate labels or a mismatched reference version. Predict the consequences before performing the changed calculation. A surprising result should trigger investigation rather than selective deletion.

**Scientific interpretation.** Prepare a figure caption with the method, invented input description, assumptions and excluded observations. Write a conclusion with one supported statement, one plausible rival explanation and one test that would improve confidence. The conclusion must not convert a sequence match into experimental function, a score into clinical truth, a correlation into causation or a diagram into exact evolutionary history.

**Peer review rubric.** A second student receives only the manifest, script, small input table, expected numeric outputs and explanatory notes. Award one point each for exact input identity, correct sampling unit, reproducible arithmetic, transparent uncertainty and appropriate claim boundaries. A score of five means the teaching exercise was reported clearly; it is not independent scientific validation of the underlying assumptions.

**Discussion prompt.** If a second software package reproduces the same output, what failure modes remain? Could both tools share a database annotation, an unrepresentative sample or an invalid conceptual assumption? Suggest one independent observation that would provide new evidence rather than only computational agreement.
