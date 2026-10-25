# Unit 03 — Gene prediction, annotation and genomic comparison

> **OpenSTEM Bioinformatics · Book 15 · Editorial draft.** All instructional sequences, measurements, cases and figures in this unit are fictional. Scientific peer review and publication approval are pending.

## The question driving this unit

**How do computational systems turn observed bases into testable claims about genes, alleles and evolutionary relationships?**

Predictive annotation transforms coordinates and sequences into hypotheses about functional elements. The inference is layered: sequence evidence suggests a coding region, structural features propose a gene model, reference comparison proposes an activity and a transcript-specific mapping suggests a variant consequence. Each layer can be uncertain independently.

### Why this subject needs both biology and computation

An ORF need not be a true gene, and a gene can contain multiple transcripts. Annotation pipelines must not collapse these differences simply to obtain a clean spreadsheet. In particular, variant coordinates depend on the declared genome assembly and interval convention. A one-base indexing mistake at a splice boundary can change a predicted consequence.

Computational methods are valuable because they allow a question to be formulated as an explicit transformation: which inputs enter the calculation, which parameters matter, what optimization or probability rule is applied, and which output should be checked against another observation. Biologists add knowledge of sampling, function and evolutionary history; statisticians add uncertainty analysis; software engineers add consistent handling of records and failure conditions. Effective bioinformatics takes all three perspectives seriously rather than treating a software report as its own justification.

### Running example and evidence hierarchy

Imagine a genome assembly whose final contig ends inside a long coding sequence. The ORF caller reports a truncated gene; the annotator copies an enzyme label from a single best protein match; a later pipeline calls a sample-specific SNP damaging. Without assembly completeness, transcript choice and independent function evidence, the apparent chain of certainty is unjustified.

For this example, use an evidence hierarchy rather than a binary correct/incorrect answer. At the lowest level sit identity and integrity checks. Next come observed measurement patterns and elementary comparisons. Next come model-based predictions whose uncertainty depends on assumptions. Finally come claims about biological mechanism or action, which normally require a stronger study design or independent evidence. Students should be able to identify the level actually supported and refuse an unsupported jump between levels.

### Course integration

Make an evidence table rather than a single categorical label. For each gene preserve prediction score, protein-domain evidence, transcript accession, orthology assumptions and supporting study. For variants, record REF and ALT, normalization, assembly, genotype uncertainty and all relevant transcript consequences before discussing biological impact.

The end-of-unit study uses a fictional dataset so students can audit the entire workflow without accessing private data or claiming to have made new biological discoveries. Record all transformations in a log, include the rejected observations and state explicitly how a different cutoff or model might change the narrative.

## Learning outcomes

By the end of this unit you should be able to: (1) define the five techniques in their proper inferential scope; (2) compute and audit the five numerical examples; (3) propose a minimal control or validation for an ambiguous result; (4) interpret each interactive model's assumptions; and (5) write a cautious, reproducible conclusion.

## Lesson 3.1 — Open reading frames and coding potential

### Concept and biological meaning

An open reading frame is a stretch of codons without an in-frame stop; computational prediction is conditional on genetic code, strandedness and biological context. 

### Method and reproducible data contract

Inspect all relevant reading frames and distinguish start sites, complete CDS features, untranslated regions and short ORFs that occur by chance. Before running an analysis, write down the input type, reference release, allowed missing values, expected columns and numerical settings. Record the observation level—organism, specimen, sequencing run, read, transcript, protein or residue—because the number of table rows need not equal the number of independent biological replicates. Reproduce one calculation using a tiny invented example and write an automatic assertion for its expected output. This validates implementation, not the scientific truth of the starting assumptions.

### Case study: a plausible signal and a rival explanation

A draft bacterial contig contains a long ORF crossing the artificial end of a fragmented assembly. The first task is to frame a biological hypothesis and a specific technical or sampling alternative. Describe what would be observed if the preferred explanation were true, then name an observation that might discriminate it from the rival. Consider label mix-ups, reference changes, missingness and biased sample recruitment before treating agreement among software tools as independent confirmation.



### Worked quantitative example

A 303-nucleotide coding region excluding the terminal stop corresponds to 101 amino acids if length is divisible by three. Treat these numbers as fictional teaching inputs. Reproduce the arithmetic in your notes, identify the denominator and decide whether the answer has physical units, is a dimensionless proportion or is a model score. Explain which input change would mechanically alter the answer. A numerical value calculated exactly from inaccurate or unrepresentative data is still a limited scientific result.

### Caveats, sensitivity and evidence strength

A long ORF alone does not prove expression, correct frame or full-length gene boundaries; noncanonical initiation and overlapping features occur. Naively dividing every nucleotide span by three ignores introns, frameshifts, annotated stop codons and coordinate conventions. 

### Independent evaluation and advanced extension

Compare ORF calls with read evidence, conserved protein domains and translated reference similarity, recording disagreements. Use this extension as a miniature sensitivity study. Change one defensible setting at a time and record whether the inference remains stable. Where methods disagree, identify whether they use different definitions, references or sources of uncertainty. Avoid the practice of choosing whichever method produces the desired biological story.

**Competing hypotheses.** Whenever one pattern appears to support a preferred biological story, deliberately develop a second explanation involving measurement, sampling or hidden structure. Specify what new observation would discriminate them and whether the proposed test is feasible. For **open reading frames and coding potential**, supply an actual auditable record—not a generic pledge of reproducibility—that would expose a mistaken assumption in the fictional case.

### Questions for mastery

1. What is directly observed, what is computed, and what is inferred? Explain the transitions using this lesson’s situation.
2. Which negative control, alternative model or independent observation could test a rival explanation? State what result would weaken your preferred account.
3. Repeat the numerical example after changing one input and report units, denominator and interpretation. Explain why a correct recalculation does not establish biological validity.
4. Which detail would another scientist need to rerun the analysis from precisely the same inputs? Describe a realistic failure if it were missing.



---
## Lesson 3.2 — Gene models and transcript isoforms

### Concept and biological meaning

A gene model comprises genomic intervals and relationships among exons, introns, UTRs and transcripts; a gene can have more than one biologically relevant isoform. 

### Method and reproducible data contract

Use a declared annotation release and coordinate convention; distinguish exon identity, transcript ID and protein-coding status when merging counts. Before running an analysis, write down the input type, reference release, allowed missing values, expected columns and numerical settings. Record the observation level—organism, specimen, sequencing run, read, transcript, protein or residue—because the number of table rows need not equal the number of independent biological replicates. Reproduce one calculation using a tiny invented example and write an automatic assertion for its expected output. This validates implementation, not the scientific truth of the starting assumptions.

### Case study: a plausible signal and a rival explanation

A variant falls inside an exon of transcript A but in an intron of transcript B from the same gene. The first task is to frame a biological hypothesis and a specific technical or sampling alternative. Describe what would be observed if the preferred explanation were true, then name an observation that might discriminate it from the rival. Consider label mix-ups, reference changes, missingness and biased sample recruitment before treating agreement among software tools as independent confirmation.



### Worked quantitative example

For exons of 120, 90 and 150 coding nucleotides with non-overlapping splice structure, CDS length is 360 nucleotides and translates to 120 amino acids absent a counted stop. Treat these numbers as fictional teaching inputs. Reproduce the arithmetic in your notes, identify the denominator and decide whether the answer has physical units, is a dimensionless proportion or is a model score. Explain which input change would mechanically alter the answer. A numerical value calculated exactly from inaccurate or unrepresentative data is still a limited scientific result.

### Caveats, sensitivity and evidence strength

There is no uniquely correct consequence without naming the affected transcript and expression context. Treating all transcripts as interchangeable obscures tissue specificity and makes differential transcript usage impossible to interpret. 

### Independent evaluation and advanced extension

Draw a splice graph and compute exon inclusion for two hypothetical isoforms rather than collapsing the graph to one gene symbol. Use this extension as a miniature sensitivity study. Change one defensible setting at a time and record whether the inference remains stable. Where methods disagree, identify whether they use different definitions, references or sources of uncertainty. Avoid the practice of choosing whichever method produces the desired biological story.

**Failure and recovery.** A mature computational workflow reports failures explicitly: missing values, invalid identifiers, numerical instability, nonconvergent fits or violated assumptions. Silently deleting difficult observations can change the target population and make a polished result less credible. For **gene models and transcript isoforms**, supply an actual auditable record—not a generic pledge of reproducibility—that would expose a mistaken assumption in the fictional case.

### Questions for mastery

1. What is directly observed, what is computed, and what is inferred? Explain the transitions using this lesson’s situation.
2. Which negative control, alternative model or independent observation could test a rival explanation? State what result would weaken your preferred account.
3. Repeat the numerical example after changing one input and report units, denominator and interpretation. Explain why a correct recalculation does not establish biological validity.
4. Which detail would another scientist need to rerun the analysis from precisely the same inputs? Describe a realistic failure if it were missing.



---
## Lesson 3.3 — Functional annotation and evidence codes

### Concept and biological meaning

Functional annotation links sequence features to biological processes or activities, with evidence ranging from direct experiment to computational similarity. 

### Method and reproducible data contract

Separate direct observation, curated inference, electronic prediction and unreviewed text; use controlled vocabularies such as Gene Ontology only with evidence qualifiers. Before running an analysis, write down the input type, reference release, allowed missing values, expected columns and numerical settings. Record the observation level—organism, specimen, sequencing run, read, transcript, protein or residue—because the number of table rows need not equal the number of independent biological replicates. Reproduce one calculation using a tiny invented example and write an automatic assertion for its expected output. This validates implementation, not the scientific truth of the starting assumptions.

### Case study: a plausible signal and a rival explanation

A newly assembled plant gene has a domain resembling an enzyme family but lacks biochemical characterization. The first task is to frame a biological hypothesis and a specific technical or sampling alternative. Describe what would be observed if the preferred explanation were true, then name an observation that might discriminate it from the rival. Consider label mix-ups, reference changes, missingness and biased sample recruitment before treating agreement among software tools as independent confirmation.



### Worked quantitative example

If 18 of 30 proposed annotations have direct experimental evidence, 60% are directly supported and 40% still require qualification. Treat these numbers as fictional teaching inputs. Reproduce the arithmetic in your notes, identify the denominator and decide whether the answer has physical units, is a dimensionless proportion or is a model score. Explain which input change would mechanically alter the answer. A numerical value calculated exactly from inaccurate or unrepresentative data is still a limited scientific result.

### Caveats, sensitivity and evidence strength

Domain matches suggest possible activity yet cannot resolve substrate specificity or subcellular context on their own. A familiar gene name imported from a distant homolog is not an experiment and can propagate mistaken function through downstream databases. 

### Independent evaluation and advanced extension

Create an annotation table with evidence type, source, date, predicted role and a confidence rationale including contrary data. Use this extension as a miniature sensitivity study. Change one defensible setting at a time and record whether the inference remains stable. Where methods disagree, identify whether they use different definitions, references or sources of uncertainty. Avoid the practice of choosing whichever method produces the desired biological story.

**Transfer of conclusions.** A numerical relationship estimated on a small classroom dataset can demonstrate a procedure without transferring to another organism or technology. External validity is an empirical question; record domain, reference, experimental setting and foreseeable distribution shift. For **functional annotation and evidence codes**, supply an actual auditable record—not a generic pledge of reproducibility—that would expose a mistaken assumption in the fictional case.

### Questions for mastery

1. What is directly observed, what is computed, and what is inferred? Explain the transitions using this lesson’s situation.
2. Which negative control, alternative model or independent observation could test a rival explanation? State what result would weaken your preferred account.
3. Repeat the numerical example after changing one input and report units, denominator and interpretation. Explain why a correct recalculation does not establish biological validity.
4. Which detail would another scientist need to rerun the analysis from precisely the same inputs? Describe a realistic failure if it were missing.



---
## Lesson 3.4 — Variant annotation and coordinate systems

### Concept and biological meaning

Variant annotation maps observed changes to genome and transcript coordinates to predict molecular consequence; VCF coordinates and alleles require normalization. 

### Method and reproducible data contract

Preserve reference build and REF/ALT alleles; left-normalize small indels when appropriate and avoid conflating consequence prediction with pathogenic classification. Before running an analysis, write down the input type, reference release, allowed missing values, expected columns and numerical settings. Record the observation level—organism, specimen, sequencing run, read, transcript, protein or residue—because the number of table rows need not equal the number of independent biological replicates. Reproduce one calculation using a tiny invented example and write an automatic assertion for its expected output. This validates implementation, not the scientific truth of the starting assumptions.

### Case study: a plausible signal and a rival explanation

An insertion near a splice boundary affects several transcript models differently. The first task is to frame a biological hypothesis and a specific technical or sampling alternative. Describe what would be observed if the preferred explanation were true, then name an observation that might discriminate it from the rival. Consider label mix-ups, reference changes, missingness and biased sample recruitment before treating agreement among software tools as independent confirmation.



### Worked quantitative example

A site with alternate allele count 12 among 200 called chromosomes has observed sample allele frequency 0.06, assuming correct diploid counting. Treat these numbers as fictional teaching inputs. Reproduce the arithmetic in your notes, identify the denominator and decide whether the answer has physical units, is a dimensionless proportion or is a model score. Explain which input change would mechanically alter the answer. A numerical value calculated exactly from inaccurate or unrepresentative data is still a limited scientific result.

### Caveats, sensitivity and evidence strength

Predicted missense or splice-region status alone neither establishes disease causation nor predicts phenotype without additional data. One-based VCF POS is easily confused with zero-based half-open BED coordinates, causing off-by-one errors at interval joins. 

### Independent evaluation and advanced extension

Test a toy conversion between VCF and BED, verify the reference base, and label every reported consequence by transcript. Use this extension as a miniature sensitivity study. Change one defensible setting at a time and record whether the inference remains stable. Where methods disagree, identify whether they use different definitions, references or sources of uncertainty. Avoid the practice of choosing whichever method produces the desired biological story.

**Biological unit.** Count the unit actually sampled rather than the number of rows generated by instruments or algorithms. Repeated reads, peptides, contigs or scans may improve measurement of one specimen without increasing independence for population-level inference. For **variant annotation and coordinate systems**, supply an actual auditable record—not a generic pledge of reproducibility—that would expose a mistaken assumption in the fictional case.

### Questions for mastery

1. What is directly observed, what is computed, and what is inferred? Explain the transitions using this lesson’s situation.
2. Which negative control, alternative model or independent observation could test a rival explanation? State what result would weaken your preferred account.
3. Repeat the numerical example after changing one input and report units, denominator and interpretation. Explain why a correct recalculation does not establish biological validity.
4. Which detail would another scientist need to rerun the analysis from precisely the same inputs? Describe a realistic failure if it were missing.



---
## Lesson 3.5 — Comparative genomics and orthology

### Concept and biological meaning

Orthologs descend from a speciation event; paralogs result from duplication, so high sequence similarity alone is insufficient to separate relationships. 

### Method and reproducible data contract

Combine gene trees, conserved genomic neighborhoods and reciprocal similarity checks; account for incomplete assemblies and gene loss. Before running an analysis, write down the input type, reference release, allowed missing values, expected columns and numerical settings. Record the observation level—organism, specimen, sequencing run, read, transcript, protein or residue—because the number of table rows need not equal the number of independent biological replicates. Reproduce one calculation using a tiny invented example and write an automatic assertion for its expected output. This validates implementation, not the scientific truth of the starting assumptions.

### Case study: a plausible signal and a rival explanation

A two-copy enzyme family expanded independently in two vertebrate lineages. The first task is to frame a biological hypothesis and a specific technical or sampling alternative. Describe what would be observed if the preferred explanation were true, then name an observation that might discriminate it from the rival. Consider label mix-ups, reference changes, missingness and biased sample recruitment before treating agreement among software tools as independent confirmation.



### Worked quantitative example

If a family contains three genes in species A and two in species B, five observed copies do not imply five independent orthology pairs. Treat these numbers as fictional teaching inputs. Reproduce the arithmetic in your notes, identify the denominator and decide whether the answer has physical units, is a dimensionless proportion or is a model score. Explain which input change would mechanically alter the answer. A numerical value calculated exactly from inaccurate or unrepresentative data is still a limited scientific result.

### Caveats, sensitivity and evidence strength

A reciprocal-best-hit method may choose an arbitrary copy and miss genuine orthology when lineage-specific duplications occurred. Synteny conservation can break through rearrangement; absence in an annotation is not proof of evolutionary deletion. 

### Independent evaluation and advanced extension

Construct a small gene-family tree with a marked duplication and ask which pairs are orthologous across the species split. Use this extension as a miniature sensitivity study. Change one defensible setting at a time and record whether the inference remains stable. Where methods disagree, identify whether they use different definitions, references or sources of uncertainty. Avoid the practice of choosing whichever method produces the desired biological story.

**Model adequacy.** Mathematical formulas compress real biological processes. Before interpreting a parameter, check limiting cases, dimensional consistency and residual patterns. Simple models can sharpen reasoning precisely because their omissions are transparent. For **comparative genomics and orthology**, supply an actual auditable record—not a generic pledge of reproducibility—that would expose a mistaken assumption in the fictional case.

### Questions for mastery

1. What is directly observed, what is computed, and what is inferred? Explain the transitions using this lesson’s situation.
2. Which negative control, alternative model or independent observation could test a rival explanation? State what result would weaken your preferred account.
3. Repeat the numerical example after changing one input and report units, denominator and interpretation. Explain why a correct recalculation does not establish biological validity.
4. Which detail would another scientist need to rerun the analysis from precisely the same inputs? Describe a realistic failure if it were missing.



---

## Integrated laboratory 3: an auditable evidence chain

**Setting.** Your undergraduate group receives fictional records about a small collection of biological material. The file descriptions are intentionally imperfect. The exercise focuses on **open reading frames and coding potential, gene models and transcript isoforms, functional annotation and evidence codes, variant annotation and coordinate systems, comparative genomics and orthology** as five aspects of one argument rather than five disconnected tool demonstrations. No live database submissions, human specimen data, laboratory samples or web API credentials are required.

**Question formation.** Begin with the question in the unit introduction. Rewrite it as a comparison of named observations, identify the unit of sampling and decide what counts as a missing or uninterpretable value. Include a skeptical alternative hypothesis. For example, an association between two measurements could reflect a common technical batch rather than a causal connection. A sensible plan makes that alternative visible before results are plotted.

**Table design.** Create a machine-readable table with fields `record_id`, `biological_unit_id`, `source_release`, `assay_or_algorithm`, `quality_note`, `value`, `unit` and `exclusion_reason`. State which fields can be blank, what the file encoding is, and how missingness is represented. Never represent a missing quantitative measurement as zero unless zero is a genuine recorded value. If two rows share the same biological unit, decide whether they are technical repeats or separate conditions before assigning inferential sample size.

**Computation plan.** Reproduce the numerical case from each of the five lessons by hand. Put the given values and final expressions into a transparent notebook or script. Build a validation assertion for each worked result, add one deliberately malformed record and document its rejection. Verify that each numerical result has a denominator, unit or declared scale. The exercise does not ask you to rerun sophisticated tools on real genomes; it asks for defensible reasoning about toy outputs.

**Sensitivity and counterexamples.** Perform two controlled changes. First vary a parameter that the method explicitly allows the analyst to choose, such as a gap cost, cutoff, filter or comparison baseline. Second introduce a metadata problem such as duplicate labels or a mismatched reference version. Predict the consequences before performing the changed calculation. A surprising result should trigger investigation rather than selective deletion.

**Scientific interpretation.** Prepare a figure caption with the method, invented input description, assumptions and excluded observations. Write a conclusion with one supported statement, one plausible rival explanation and one test that would improve confidence. The conclusion must not convert a sequence match into experimental function, a score into clinical truth, a correlation into causation or a diagram into exact evolutionary history.

**Peer review rubric.** A second student receives only the manifest, script, small input table, expected numeric outputs and explanatory notes. Award one point each for exact input identity, correct sampling unit, reproducible arithmetic, transparent uncertainty and appropriate claim boundaries. A score of five means the teaching exercise was reported clearly; it is not independent scientific validation of the underlying assumptions.

**Discussion prompt.** If a second software package reproduces the same output, what failure modes remain? Could both tools share a database annotation, an unrepresentative sample or an invalid conceptual assumption? Suggest one independent observation that would provide new evidence rather than only computational agreement.
