# Unit 07 — Statistics, machine learning and scientific uncertainty

> **OpenSTEM Bioinformatics · Book 15 · Editorial draft.** All instructional sequences, measurements, cases and figures in this unit are fictional. Scientific peer review and publication approval are pending.

## The question driving this unit

**What would have to be true for a computational pattern to generalize to new biological data?**

A model can fit observations while being fundamentally unhelpful. Low p-values may multiply by the thousands; unsupervised clusters may reflect batch; classifiers may exploit repeated measurements from the same organism; and confident probabilities may be badly calibrated. Each failure has a different remedy.

### Why this subject needs both biology and computation

The inferential contract begins with defining a target, splitting data at the correct biological level and specifying the uncertainty of interest. Exploratory visualizations reveal patterns, but confirmation requires held-out observations or carefully controlled follow-up designs. Any preprocessing tuned with test data leaks information into assessment.

Computational methods are valuable because they allow a question to be formulated as an explicit transformation: which inputs enter the calculation, which parameters matter, what optimization or probability rule is applied, and which output should be checked against another observation. Biologists add knowledge of sampling, function and evolutionary history; statisticians add uncertainty analysis; software engineers add consistent handling of records and failure conditions. Effective bioinformatics takes all three perspectives seriously rather than treating a software report as its own justification.

### Running example and evidence hierarchy

Imagine classifying plant stress status from thousands of transcripts measured across two farms. Randomly splitting technical repeats creates deceptively high performance because the same source appears in both subsets. Holding out entire plants, field plots or farms provides a more realistic assessment of deployment into new settings.

For this example, use an evidence hierarchy rather than a binary correct/incorrect answer. At the lowest level sit identity and integrity checks. Next come observed measurement patterns and elementary comparisons. Next come model-based predictions whose uncertainty depends on assumptions. Finally come claims about biological mechanism or action, which normally require a stronger study design or independent evidence. Students should be able to identify the level actually supported and refuse an unsupported jump between levels.

### Course integration

Evidence must also survive subgroup inspection, changed preprocessing and calibration. A model whose top features are preparation-day proxies can appear mechanistically interesting. Separate prediction from explanation and causal intervention; use scientific constraints to decide whether a variable is worth studying further.

The end-of-unit study uses a fictional dataset so students can audit the entire workflow without accessing private data or claiming to have made new biological discoveries. Record all transformations in a log, include the rejected observations and state explicitly how a different cutoff or model might change the narrative.

## Learning outcomes

By the end of this unit you should be able to: (1) define the five techniques in their proper inferential scope; (2) compute and audit the five numerical examples; (3) propose a minimal control or validation for an ambiguous result; (4) interpret each interactive model's assumptions; and (5) write a cautious, reproducible conclusion.

## Lesson 7.1 — Null hypotheses and false discovery rates

### Concept and biological meaning

Testing thousands of features creates multiplicity; procedures such as Benjamini–Hochberg aim to control expected false-discovery proportion among discoveries under their assumptions. 

### Method and reproducible data contract

Prespecify the hypothesis family, filtering rule and dependence assumptions; distinguish adjusted p-values from probabilities that individual results are false. Before running an analysis, write down the input type, reference release, allowed missing values, expected columns and numerical settings. Record the observation level—organism, specimen, sequencing run, read, transcript, protein or residue—because the number of table rows need not equal the number of independent biological replicates. Reproduce one calculation using a tiny invented example and write an automatic assertion for its expected output. This validates implementation, not the scientific truth of the starting assumptions.

### Case study: a plausible signal and a rival explanation

An exploratory study tests 5,000 transcripts and reports all unadjusted p-values below 0.05. The first task is to frame a biological hypothesis and a specific technical or sampling alternative. Describe what would be observed if the preferred explanation were true, then name an observation that might discriminate it from the rival. Consider label mix-ups, reference changes, missingness and biased sample recruitment before treating agreement among software tools as independent confirmation.



### Worked quantitative example

For ordered p-values 0.001, 0.02, 0.03 with m=3, BH raw ranks yield 0.003, 0.03 and 0.03 before monotonicity adjustment. Treat these numbers as fictional teaching inputs. Reproduce the arithmetic in your notes, identify the denominator and decide whether the answer has physical units, is a dimensionless proportion or is a model score. Explain which input change would mechanically alter the answer. A numerical value calculated exactly from inaccurate or unrepresentative data is still a limited scientific result.

### Caveats, sensitivity and evidence strength

Under 5,000 independent true nulls, about 250 p-values below 0.05 are expected on average, not 250 confirmed biological changes. A false discovery rate of 5% is not a guarantee that each reported gene has exactly 5% probability of being false. 

### Independent evaluation and advanced extension

Compare unadjusted and BH-adjusted findings and explain how prefiltering based on results could invalidate simple error claims. Use this extension as a miniature sensitivity study. Change one defensible setting at a time and record whether the inference remains stable. Where methods disagree, identify whether they use different definitions, references or sources of uncertainty. Avoid the practice of choosing whichever method produces the desired biological story.

**Model adequacy.** Mathematical formulas compress real biological processes. Before interpreting a parameter, check limiting cases, dimensional consistency and residual patterns. Simple models can sharpen reasoning precisely because their omissions are transparent. For **null hypotheses and false discovery rates**, supply an actual auditable record—not a generic pledge of reproducibility—that would expose a mistaken assumption in the fictional case.

### Questions for mastery

1. What is directly observed, what is computed, and what is inferred? Explain the transitions using this lesson’s situation.
2. Which negative control, alternative model or independent observation could test a rival explanation? State what result would weaken your preferred account.
3. Repeat the numerical example after changing one input and report units, denominator and interpretation. Explain why a correct recalculation does not establish biological validity.
4. Which detail would another scientist need to rerun the analysis from precisely the same inputs? Describe a realistic failure if it were missing.



---
## Lesson 7.2 — Principal component analysis and latent structure

### Concept and biological meaning

PCA finds orthogonal directions of maximum variance in scaled numeric data; the axes summarize covariance and do not know treatment labels. 

### Method and reproducible data contract

Center and, where justified, scale features; assess depth and batch effects, loadings, explained variance and sensitivity to highly abundant variables. Before running an analysis, write down the input type, reference release, allowed missing values, expected columns and numerical settings. Record the observation level—organism, specimen, sequencing run, read, transcript, protein or residue—because the number of table rows need not equal the number of independent biological replicates. Reproduce one calculation using a tiny invented example and write an automatic assertion for its expected output. This validates implementation, not the scientific truth of the starting assumptions.

### Case study: a plausible signal and a rival explanation

RNA-seq samples separate perfectly by preparation date rather than experimental condition on the first principal component. The first task is to frame a biological hypothesis and a specific technical or sampling alternative. Describe what would be observed if the preferred explanation were true, then name an observation that might discriminate it from the rival. Consider label mix-ups, reference changes, missingness and biased sample recruitment before treating agreement among software tools as independent confirmation.



### Worked quantitative example

If eigenvalues are 6, 3 and 1, the first two PCs explain (6+3)/10 = 90% of represented variance. Treat these numbers as fictional teaching inputs. Reproduce the arithmetic in your notes, identify the denominator and decide whether the answer has physical units, is a dimensionless proportion or is a model score. Explain which input change would mechanically alter the answer. A numerical value calculated exactly from inaccurate or unrepresentative data is still a limited scientific result.

### Caveats, sensitivity and evidence strength

A cluster in two dimensions is not evidence of a biological subtype without replication and alternative explanations. PCA on mixed units without scaling can be dominated by high-variance features unrelated to biological relevance. 

### Independent evaluation and advanced extension

Annotate a synthetic scores plot with batch and condition, then compare the interpretation before and after a principled transform. Use this extension as a miniature sensitivity study. Change one defensible setting at a time and record whether the inference remains stable. Where methods disagree, identify whether they use different definitions, references or sources of uncertainty. Avoid the practice of choosing whichever method produces the desired biological story.

**Reproducible decisions.** A reader should be able to regenerate the same derived table from the same inputs and explicit settings. Preserve a checksum and environment record, and keep a log of decisions that change which records enter the analysis. For **principal component analysis and latent structure**, supply an actual auditable record—not a generic pledge of reproducibility—that would expose a mistaken assumption in the fictional case.

### Questions for mastery

1. What is directly observed, what is computed, and what is inferred? Explain the transitions using this lesson’s situation.
2. Which negative control, alternative model or independent observation could test a rival explanation? State what result would weaken your preferred account.
3. Repeat the numerical example after changing one input and report units, denominator and interpretation. Explain why a correct recalculation does not establish biological validity.
4. Which detail would another scientist need to rerun the analysis from precisely the same inputs? Describe a realistic failure if it were missing.



---
## Lesson 7.3 — Clustering, stability and batch effects

### Concept and biological meaning

Clustering groups observations by an explicit distance and algorithm; the output reflects representation choices rather than discovering immutable natural categories. 

### Method and reproducible data contract

Choose distance metric, normalization, missing-data policy and number of clusters with reference to the biological objective; assess stability across perturbations. Before running an analysis, write down the input type, reference release, allowed missing values, expected columns and numerical settings. Record the observation level—organism, specimen, sequencing run, read, transcript, protein or residue—because the number of table rows need not equal the number of independent biological replicates. Reproduce one calculation using a tiny invented example and write an automatic assertion for its expected output. This validates implementation, not the scientific truth of the starting assumptions.

### Case study: a plausible signal and a rival explanation

A heatmap divides specimens into three groups when Euclidean distance is used but two groups under correlation distance. The first task is to frame a biological hypothesis and a specific technical or sampling alternative. Describe what would be observed if the preferred explanation were true, then name an observation that might discriminate it from the rival. Consider label mix-ups, reference changes, missingness and biased sample recruitment before treating agreement among software tools as independent confirmation.



### Worked quantitative example

Two samples with vectors (1,2) and (2,4) have Euclidean distance sqrt(5), but Pearson correlation one. Treat these numbers as fictional teaching inputs. Reproduce the arithmetic in your notes, identify the denominator and decide whether the answer has physical units, is a dimensionless proportion or is a model score. Explain which input change would mechanically alter the answer. A numerical value calculated exactly from inaccurate or unrepresentative data is still a limited scientific result.

### Caveats, sensitivity and evidence strength

Selection of clusters after looking at outcome labels invites circular validation, and dendrogram branch lengths are method-specific. High correlation need not imply low Euclidean distance; absolute abundance and pattern similarity are distinct questions. 

### Independent evaluation and advanced extension

Bootstrap feature subsets, record co-clustering rates and test whether batch labels explain major splits. Use this extension as a miniature sensitivity study. Change one defensible setting at a time and record whether the inference remains stable. Where methods disagree, identify whether they use different definitions, references or sources of uncertainty. Avoid the practice of choosing whichever method produces the desired biological story.

**Operational definition.** Before computing, write an operational definition of the variable of interest, including its measurement unit, denominator, sampling level and admissible values. An operational definition is not bureaucracy; it is what makes two methods comparable and reveals when they answer different questions. For **clustering, stability and batch effects**, supply an actual auditable record—not a generic pledge of reproducibility—that would expose a mistaken assumption in the fictional case.

### Questions for mastery

1. What is directly observed, what is computed, and what is inferred? Explain the transitions using this lesson’s situation.
2. Which negative control, alternative model or independent observation could test a rival explanation? State what result would weaken your preferred account.
3. Repeat the numerical example after changing one input and report units, denominator and interpretation. Explain why a correct recalculation does not establish biological validity.
4. Which detail would another scientist need to rerun the analysis from precisely the same inputs? Describe a realistic failure if it were missing.



---
## Lesson 7.4 — Classification and cross-validation

### Concept and biological meaning

A supervised predictor estimates labels from features, and its usefulness depends on generalization to genuinely new biological units. 

### Method and reproducible data contract

Keep all data from the same individual or site in the same fold, nest hyperparameter tuning inside training folds and reserve an untouched test set when possible. Before running an analysis, write down the input type, reference release, allowed missing values, expected columns and numerical settings. Record the observation level—organism, specimen, sequencing run, read, transcript, protein or residue—because the number of table rows need not equal the number of independent biological replicates. Reproduce one calculation using a tiny invented example and write an automatic assertion for its expected output. This validates implementation, not the scientific truth of the starting assumptions.

### Case study: a plausible signal and a rival explanation

A classifier for animal species uses multiple images from the same individual and accidentally places some images in training and test folds. The first task is to frame a biological hypothesis and a specific technical or sampling alternative. Describe what would be observed if the preferred explanation were true, then name an observation that might discriminate it from the rival. Consider label mix-ups, reference changes, missingness and biased sample recruitment before treating agreement among software tools as independent confirmation.



### Worked quantitative example

For a test set with 18 true positives, 2 false negatives and 5 false positives, recall is 18/20=0.9 and precision is 18/23≈0.783. Treat these numbers as fictional teaching inputs. Reproduce the arithmetic in your notes, identify the denominator and decide whether the answer has physical units, is a dimensionless proportion or is a model score. Explain which input change would mechanically alter the answer. A numerical value calculated exactly from inaccurate or unrepresentative data is still a limited scientific result.

### Caveats, sensitivity and evidence strength

Leakage can produce near-perfect test accuracy while failing on new individuals, instruments or study sites. Accuracy alone obscures class imbalance; a majority-class model can look impressive without identifying rare positives. 

### Independent evaluation and advanced extension

Design group-aware splits and report confusion matrices, confidence intervals and performance across cohorts. Use this extension as a miniature sensitivity study. Change one defensible setting at a time and record whether the inference remains stable. Where methods disagree, identify whether they use different definitions, references or sources of uncertainty. Avoid the practice of choosing whichever method produces the desired biological story.

**Independent confirmation.** Prefer independent forms of evidence to repeated analysis of the same imperfect input. A second algorithm may share the first algorithm’s reference bias or annotation assumption; an independently measured observation answers a more demanding question. For **classification and cross-validation**, supply an actual auditable record—not a generic pledge of reproducibility—that would expose a mistaken assumption in the fictional case.

### Questions for mastery

1. What is directly observed, what is computed, and what is inferred? Explain the transitions using this lesson’s situation.
2. Which negative control, alternative model or independent observation could test a rival explanation? State what result would weaken your preferred account.
3. Repeat the numerical example after changing one input and report units, denominator and interpretation. Explain why a correct recalculation does not establish biological validity.
4. Which detail would another scientist need to rerun the analysis from precisely the same inputs? Describe a realistic failure if it were missing.



---
## Lesson 7.5 — Calibration, uncertainty and causal boundaries

### Concept and biological meaning

Predictive scores need calibration to make probability statements; uncertainty includes sampling variation, dataset shift and model misspecification. 

### Method and reproducible data contract

Use reliability diagrams and external validation where possible; carefully distinguish associated features from interventions that change outcomes. Before running an analysis, write down the input type, reference release, allowed missing values, expected columns and numerical settings. Record the observation level—organism, specimen, sequencing run, read, transcript, protein or residue—because the number of table rows need not equal the number of independent biological replicates. Reproduce one calculation using a tiny invented example and write an automatic assertion for its expected output. This validates implementation, not the scientific truth of the starting assumptions.

### Case study: a plausible signal and a rival explanation

A laboratory risk model outputs 0.9 on nearly every case but only 0.6 of those cases have the outcome. The first task is to frame a biological hypothesis and a specific technical or sampling alternative. Describe what would be observed if the preferred explanation were true, then name an observation that might discriminate it from the rival. Consider label mix-ups, reference changes, missingness and biased sample recruitment before treating agreement among software tools as independent confirmation.



### Worked quantitative example

Among 50 cases assigned predicted probability 0.8, observing 30 outcomes gives empirical rate 0.6 and calibration gap -0.2. Treat these numbers as fictional teaching inputs. Reproduce the arithmetic in your notes, identify the denominator and decide whether the answer has physical units, is a dimensionless proportion or is a model score. Explain which input change would mechanically alter the answer. A numerical value calculated exactly from inaccurate or unrepresentative data is still a limited scientific result.

### Caveats, sensitivity and evidence strength

Strong discrimination can coexist with poor probability calibration, and calibration in one population may degrade elsewhere. A feature's predictive importance is not proof that changing it would change the phenotype. 

### Independent evaluation and advanced extension

Report discrimination, calibration, subgroup uncertainty and actionable limits; avoid automated clinical decisions from classroom models. Use this extension as a miniature sensitivity study. Change one defensible setting at a time and record whether the inference remains stable. Where methods disagree, identify whether they use different definitions, references or sources of uncertainty. Avoid the practice of choosing whichever method produces the desired biological story.

**Competing hypotheses.** Whenever one pattern appears to support a preferred biological story, deliberately develop a second explanation involving measurement, sampling or hidden structure. Specify what new observation would discriminate them and whether the proposed test is feasible. For **calibration, uncertainty and causal boundaries**, supply an actual auditable record—not a generic pledge of reproducibility—that would expose a mistaken assumption in the fictional case.

### Questions for mastery

1. What is directly observed, what is computed, and what is inferred? Explain the transitions using this lesson’s situation.
2. Which negative control, alternative model or independent observation could test a rival explanation? State what result would weaken your preferred account.
3. Repeat the numerical example after changing one input and report units, denominator and interpretation. Explain why a correct recalculation does not establish biological validity.
4. Which detail would another scientist need to rerun the analysis from precisely the same inputs? Describe a realistic failure if it were missing.



---

## Integrated laboratory 7: an auditable evidence chain

**Setting.** Your undergraduate group receives fictional records about a small collection of biological material. The file descriptions are intentionally imperfect. The exercise focuses on **null hypotheses and false discovery rates, principal component analysis and latent structure, clustering, stability and batch effects, classification and cross-validation, calibration, uncertainty and causal boundaries** as five aspects of one argument rather than five disconnected tool demonstrations. No live database submissions, human specimen data, laboratory samples or web API credentials are required.

**Question formation.** Begin with the question in the unit introduction. Rewrite it as a comparison of named observations, identify the unit of sampling and decide what counts as a missing or uninterpretable value. Include a skeptical alternative hypothesis. For example, an association between two measurements could reflect a common technical batch rather than a causal connection. A sensible plan makes that alternative visible before results are plotted.

**Table design.** Create a machine-readable table with fields `record_id`, `biological_unit_id`, `source_release`, `assay_or_algorithm`, `quality_note`, `value`, `unit` and `exclusion_reason`. State which fields can be blank, what the file encoding is, and how missingness is represented. Never represent a missing quantitative measurement as zero unless zero is a genuine recorded value. If two rows share the same biological unit, decide whether they are technical repeats or separate conditions before assigning inferential sample size.

**Computation plan.** Reproduce the numerical case from each of the five lessons by hand. Put the given values and final expressions into a transparent notebook or script. Build a validation assertion for each worked result, add one deliberately malformed record and document its rejection. Verify that each numerical result has a denominator, unit or declared scale. The exercise does not ask you to rerun sophisticated tools on real genomes; it asks for defensible reasoning about toy outputs.

**Sensitivity and counterexamples.** Perform two controlled changes. First vary a parameter that the method explicitly allows the analyst to choose, such as a gap cost, cutoff, filter or comparison baseline. Second introduce a metadata problem such as duplicate labels or a mismatched reference version. Predict the consequences before performing the changed calculation. A surprising result should trigger investigation rather than selective deletion.

**Scientific interpretation.** Prepare a figure caption with the method, invented input description, assumptions and excluded observations. Write a conclusion with one supported statement, one plausible rival explanation and one test that would improve confidence. The conclusion must not convert a sequence match into experimental function, a score into clinical truth, a correlation into causation or a diagram into exact evolutionary history.

**Peer review rubric.** A second student receives only the manifest, script, small input table, expected numeric outputs and explanatory notes. Award one point each for exact input identity, correct sampling unit, reproducible arithmetic, transparent uncertainty and appropriate claim boundaries. A score of five means the teaching exercise was reported clearly; it is not independent scientific validation of the underlying assumptions.

**Discussion prompt.** If a second software package reproduces the same output, what failure modes remain? Could both tools share a database annotation, an unrepresentative sample or an invalid conceptual assumption? Suggest one independent observation that would provide new evidence rather than only computational agreement.
