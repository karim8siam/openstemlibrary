# Unit 07 — Human genomics, medicine and responsible interpretation

> **OpenSTEM Genomics · Book 16 · Editorial teaching draft.** All worked case data and investigations are synthetic. The interactive models describe simplified mathematical relations, not diagnoses or empirical genomic claims.

## Central scientific question

**When can genomic evidence responsibly inform a consequential decision?**

### Conceptual context and how the five lessons fit

Human genomic information can carry substantial personal and familial consequences. Variants can be observed and measured accurately without their clinical significance being known. Professional interpretation requires evidence standards, context, consent and validation; no educational worked example should be used to diagnose an individual or select medication. This unit separates inheritance models, variant classification, tumor heterogeneity, pharmacogenomics and ethical stewardship. Learners should be able to explain not just why a finding appears interesting, but what could make it misleading, whose interests are implicated and which evidence is required before a consequential decision. Uncertainty is a result worth reporting, not a problem to hide.

### A running case to reason through

An educational family-sequencing case shows a candidate allele but the inferred risk changes markedly with ascertainment and prior probability. The proposed explanation should remain a working hypothesis until both the measurement process and alternative biological accounts have been examined. Identify a plausible negative control, a sample identity verification and a condition in which the preferred model might fail. A final plot can be numerically precise while its biological conclusion is uncertain; your task is to make that uncertainty visible rather than treating it as a defect.

### Unit learning objectives

By the end of this unit, you should be able to reconstruct the data assumptions behind each of the five main topics, reproduce their toy calculations, distinguish technical and biological replication, identify a rival explanation for an apparent signal, and propose an independent measurement that would strengthen or challenge the inference. For each numerical answer, know the denominator, its unit and the simplifications required. Give yourself permission to conclude "not established" when appropriate.

### Study route

Read the five lessons in order. Each starts with an operational definition, moves through a fictional case and a worked calculation, then challenges the tempting inference. Compute the numbers by hand before using code. Finish with the unit capstone and the interactive model questions. Learning genomics requires deciding which questions an assay can answer at least as much as mastering the associated algorithm.

---

## Lesson 7.1 — Inheritance, penetrance and genomic evidence

### Mechanism and what can be inferred

Alleles may be inherited in dominant, recessive, sex-linked or complex patterns; penetrance is probability of a specified phenotype among carriers in a defined context. Family history is affected by ascertainment and age. Identify the physical material, the instrument observation and the computational summary separately. This prevents a dataset label from being mistaken for the underlying biological process. The central question is **When can genomic evidence responsibly inform a consequential decision?** Interpret that question in the limited context of the named species, specimens and assay; do not extrapolate from one sequence representation to all individuals.

### Measurement contract and analytical method

Construct an explicit pedigree model including phenotype definitions, affected/unaffected ages and missing relatives. Keep segregation support separate from variant classification and use established professional frameworks for clinical claims. Write a data dictionary before invoking a tool. It should specify permitted values, missing-data codes, identity keys, coordinate conventions, and a worked input-output example whose result can be checked without proprietary software. When comparing results, include the reference assembly or database release, observation level, quality thresholds, removed records and a denominator for each proportion. Missing genomic measurements are not synonymous with confidently absent biological events. Explain which parts of the pipeline are deterministic transformations and which rely on empirical model assumptions.

### Fictional case and competing explanation

A fictional four-generation family has a candidate allele found in most affected individuals but also in an unaffected young adult. This is a hypothetical instructional case, not a reported finding. Begin with one biological hypothesis and one technical or sampling rival. Before choosing the most interesting interpretation, write down what each hypothesis predicts about a newly collected specimen or orthogonal assay. Different algorithms may agree because they reuse the same flawed reference or measurement, not because they supply independent experimental confirmation.

### Worked example with units

**Problem:** If 8 of 10 sampled adult carriers exhibit a defined trait, observed penetrance estimate is 0.8 in this selected sample, not a universal estimate.

**Calculation:** `8/10` = **0.8 selected-sample fraction** for the invented inputs. To test your interpretation, change one input within a plausible synthetic range and recompute the output. The goal is not to fit actual organisms but to understand how measurement assumptions propagate through the equation. Correct arithmetic validates a calculation, but it does not establish that the input data are representative or that the result has a causal meaning. Record whether the denominator counts bases, reads, allele copies, individuals, loci or experimental runs. Recompute with a modified hypothetical input to examine numerical sensitivity.

### Error modes and validation design

An unaffected carrier does not refute incomplete penetrance; neither does affected status prove that one variant is the cause. If the measurement was duplicated at the technical level, name the correct independent sampling level before offering any significance claim. Replication improves confidence only to the extent that it samples the relevant biological variability. **Audit emphasis — Check the sensitivity.** Vary a defensible parameter—filter threshold, reference representation, cohort subset or matching rule—and report whether your conclusion changes. Sensitivity is information about model dependence, not a reason to hide uncertain results.

Compare age-dependent phenotype frequencies, assess non-carriers and seek independent functional and population evidence under appropriate consent. The proposed new evidence should help discriminate between mechanisms rather than merely producing another version of the same computational score. Explain the important negative control and a result that would weaken your preferred hypothesis. In a scientific report, keep measurements, computed statistics, model-based predictions and proposed biological explanations in separate statements.

### Transfer exercise

Connect **Inheritance, penetrance and genomic evidence** with **Variant classification and clinical uncertainty**. Explain which source-data error would contaminate both topics and how a reference-aware provenance record would reveal it. Then answer: What was measured? How was the statistic calculated? What competing explanation remains? What independent experiment would be most efficient? Present the final inference as a conditional claim whose strength matches the available evidence.

---

## Lesson 7.2 — Variant classification and clinical uncertainty

### Mechanism and what can be inferred

Evidence categories for sequence variation can involve population frequency, functional measurements, segregation and prior documented cases. VUS means uncertainty and should not be treated as established pathogenicity. Identify the physical material, the instrument observation and the computational summary separately. This prevents a dataset label from being mistaken for the underlying biological process. The central question is **When can genomic evidence responsibly inform a consequential decision?** Interpret that question in the limited context of the named species, specimens and assay; do not extrapolate from one sequence representation to all individuals.

### Measurement contract and analytical method

Document transcript, reference assembly, allele representation, evidence sources and date. Apply current validated criteria only under professional review, distinguishing research hypothesis from clinical diagnosis. Reconstruct the reasoning as an evidence ledger with separate columns for raw measurement, model choice, calculated value, alternative explanation and validation status. Avoid merging uncertain evidence into one unexplained confidence label. When comparing results, include the reference assembly or database release, observation level, quality thresholds, removed records and a denominator for each proportion. Missing genomic measurements are not synonymous with confidently absent biological events. Explain which parts of the pipeline are deterministic transformations and which rely on empirical model assumptions.

### Fictional case and competing explanation

A hypothetical variant is absent in a small ancestry-skewed database but has no reliable functional data, making causal interpretation unjustified. This is a hypothetical instructional case, not a reported finding. Begin with one biological hypothesis and one technical or sampling rival. Before choosing the most interesting interpretation, write down what each hypothesis predicts about a newly collected specimen or orthogonal assay. Different algorithms may agree because they reuse the same flawed reference or measurement, not because they supply independent experimental confirmation.

### Worked example with units

**Problem:** A variant present in 3 of 2,000 sampled allele copies has observed frequency 0.0015; sampling error and ascertainment still matter.

**Calculation:** `3/2_000` = **0.0015 observed allele frequency** for the invented inputs. Check the unit, sign, scale and rounding of the calculated answer. Where a proportion is involved, state whether the result counts reads, alleles, individuals, transcripts, genomic sites or publications; those denominators are not interchangeable. Correct arithmetic validates a calculation, but it does not establish that the input data are representative or that the result has a causal meaning. Record whether the denominator counts bases, reads, allele copies, individuals, loci or experimental runs. Recompute with a modified hypothetical input to examine numerical sensitivity.

### Error modes and validation design

Absence from a database is not automatically rarity worldwide; false precision in disease-risk prediction can generate real harm. Consider whether the strongest-looking pattern comes from a feature selected after inspecting the answer. Exploratory selection followed by an unadjusted confirmatory claim can overstate reproducibility. **Audit emphasis — Design a contrast.** Specify at least one plausible nonbiological explanation and predict which extra measurement would expose it. Negative controls and orthogonal data are often more informative than adding another correlated software score.

Ask which additional independent observations would change classification and whether the laboratory evidence is validated for the intended setting. The proposed new evidence should help discriminate between mechanisms rather than merely producing another version of the same computational score. Explain the important negative control and a result that would weaken your preferred hypothesis. In a scientific report, keep measurements, computed statistics, model-based predictions and proposed biological explanations in separate statements.

### Transfer exercise

Connect **Variant classification and clinical uncertainty** with **Cancer genomics and cellular heterogeneity**. Explain which source-data error would contaminate both topics and how a reference-aware provenance record would reveal it. Then answer: What was measured? How was the statistic calculated? What competing explanation remains? What independent experiment would be most efficient? Present the final inference as a conditional claim whose strength matches the available evidence.

---

## Lesson 7.3 — Cancer genomics and cellular heterogeneity

### Mechanism and what can be inferred

Tumors may contain distinct subclones with somatic sequence and copy-number differences. Tumor purity, normal-cell admixture and local dosage affect variant allele fractions independently of mutation timing. Identify the physical material, the instrument observation and the computational summary separately. This prevents a dataset label from being mistaken for the underlying biological process. The central question is **When can genomic evidence responsibly inform a consequential decision?** Interpret that question in the limited context of the named species, specimens and assay; do not extrapolate from one sequence representation to all individuals.

### Measurement contract and analytical method

Distinguish matched germline and tumor measurements, local copy number, sequencing artifacts, and subclone models. Treat phylogenetic reconstruction as assumption-dependent when only bulk data are available. Create a tiny independent benchmark that contains an ordinary case, an ambiguous boundary case and a deliberately malformed record. Check not only output numbers but also whether the tool detects invalid assumptions and refuses silent corrections. When comparing results, include the reference assembly or database release, observation level, quality thresholds, removed records and a denominator for each proportion. Missing genomic measurements are not synonymous with confidently absent biological events. Explain which parts of the pipeline are deterministic transformations and which rely on empirical model assumptions.

### Fictional case and competing explanation

A fictional tumor biopsy has a variant at 15% observed allele fraction; multiple purity and copy-number scenarios could generate the same number. This is a hypothetical instructional case, not a reported finding. Begin with one biological hypothesis and one technical or sampling rival. Before choosing the most interesting interpretation, write down what each hypothesis predicts about a newly collected specimen or orthogonal assay. Different algorithms may agree because they reuse the same flawed reference or measurement, not because they supply independent experimental confirmation.

### Worked example with units

**Problem:** With 45 alternate-supporting reads among 300 high-quality reads, variant allele fraction is 0.15; it is not the cancer-cell fraction.

**Calculation:** `45/300` = **0.15 variant allele fraction** for the invented inputs. To test your interpretation, change one input within a plausible synthetic range and recompute the output. The goal is not to fit actual organisms but to understand how measurement assumptions propagate through the equation. Correct arithmetic validates a calculation, but it does not establish that the input data are representative or that the result has a causal meaning. Record whether the denominator counts bases, reads, allele copies, individuals, loci or experimental runs. Recompute with a modified hypothetical input to examine numerical sensitivity.

### Error modes and validation design

Equating 15% alternate reads with 15% malignant cells ignores allele dosage, contamination, sampling noise and clonal structure. Explain how an earlier-stage error could propagate through several downstream analyses and create apparently consistent output. Correlation among derived reports should never substitute for documented source integrity. **Audit emphasis — Begin with the denominator.** First write the total that would make a reported fraction equal to one: all molecules, all individuals, all reference positions or all interrogated loci. A percentage cannot be compared across studies if the denominators are inconsistent.

Compare neighboring copy-number regions and independent samples, and show several plausible cellular mixture models rather than selecting a unique story. The proposed new evidence should help discriminate between mechanisms rather than merely producing another version of the same computational score. Explain the important negative control and a result that would weaken your preferred hypothesis. In a scientific report, keep measurements, computed statistics, model-based predictions and proposed biological explanations in separate statements.

### Transfer exercise

Connect **Cancer genomics and cellular heterogeneity** with **Pharmacogenomics and context-sensitive evidence**. Explain which source-data error would contaminate both topics and how a reference-aware provenance record would reveal it. Then answer: What was measured? How was the statistic calculated? What competing explanation remains? What independent experiment would be most efficient? Present the final inference as a conditional claim whose strength matches the available evidence.

---

## Lesson 7.4 — Pharmacogenomics and context-sensitive evidence

### Mechanism and what can be inferred

Some inherited variants affect pharmacokinetic enzymes or drug targets, but phenotype prediction also depends on medication, environment, ancestry, co-therapies and assay interpretation. Identify the physical material, the instrument observation and the computational summary separately. This prevents a dataset label from being mistaken for the underlying biological process. The central question is **When can genomic evidence responsibly inform a consequential decision?** Interpret that question in the limited context of the named species, specimens and assay; do not extrapolate from one sequence representation to all individuals.

### Measurement contract and analytical method

Keep the stated gene–drug relationship, variant-to-haplotype assignment, activity assumptions and evidence-based guideline edition explicit. Never infer a dose or medication change from an educational calculator. For a transparent analysis, make two small tables: one describing source specimens and assays, and another describing computational transformations. The join keys should let another investigator trace a number back to its input without revealing restricted personal information. When comparing results, include the reference assembly or database release, observation level, quality thresholds, removed records and a denominator for each proportion. Missing genomic measurements are not synonymous with confidently absent biological events. Explain which parts of the pipeline are deterministic transformations and which rely on empirical model assumptions.

### Fictional case and competing explanation

An invented case has two variants in a drug-metabolism gene, but their phase is unknown; an automated diplotype label may be unreliable. This is a hypothetical instructional case, not a reported finding. Begin with one biological hypothesis and one technical or sampling rival. Before choosing the most interesting interpretation, write down what each hypothesis predicts about a newly collected specimen or orthogonal assay. Different algorithms may agree because they reuse the same flawed reference or measurement, not because they supply independent experimental confirmation.

### Worked example with units

**Problem:** Of 40 hypothetical calls, 32 have an unambiguous star-allele match under a chosen table: mapping completeness is 80%, not clinical sensitivity.

**Calculation:** `32/40*100` = **80 %** for the invented inputs. Check the unit, sign, scale and rounding of the calculated answer. Where a proportion is involved, state whether the result counts reads, alleles, individuals, transcripts, genomic sites or publications; those denominators are not interchangeable. Correct arithmetic validates a calculation, but it does not establish that the input data are representative or that the result has a causal meaning. Record whether the denominator counts bases, reads, allele copies, individuals, loci or experimental runs. Recompute with a modified hypothetical input to examine numerical sensitivity.

### Error modes and validation design

A sequence-to-response relationship validated in one context does not confer the same predictive accuracy for all drugs or populations. Ask which alternative assay or independent group could challenge the finding. Repeating a computation under different colors or with another software package is not independent biological replication. **Audit emphasis — Examine independence.** Ask whether repeated observations came from distinct biological sources or from technical processing of the same material. A thousand reads from one library can improve measurement precision without creating a thousand independent organisms.

Compare inferred phase under different data sources and consult peer-reviewed professional guidelines; seek appropriate pharmacological validation where needed. The proposed new evidence should help discriminate between mechanisms rather than merely producing another version of the same computational score. Explain the important negative control and a result that would weaken your preferred hypothesis. In a scientific report, keep measurements, computed statistics, model-based predictions and proposed biological explanations in separate statements.

### Transfer exercise

Connect **Pharmacogenomics and context-sensitive evidence** with **Consent, genomic privacy and benefit sharing**. Explain which source-data error would contaminate both topics and how a reference-aware provenance record would reveal it. Then answer: What was measured? How was the statistic calculated? What competing explanation remains? What independent experiment would be most efficient? Present the final inference as a conditional claim whose strength matches the available evidence.

---

## Lesson 7.5 — Consent, genomic privacy and benefit sharing

### Mechanism and what can be inferred

Genomic information is familial and persistent: sharing one person’s data can reveal statistical information about relatives. Ethical governance must consider consent scope, retention, access, community representation and benefit sharing. Identify the physical material, the instrument observation and the computational summary separately. This prevents a dataset label from being mistaken for the underlying biological process. The central question is **When can genomic evidence responsibly inform a consequential decision?** Interpret that question in the limited context of the named species, specimens and assay; do not extrapolate from one sequence representation to all individuals.

### Measurement contract and analytical method

Use purpose-limited data access, minimize identifiers and describe re-contact, secondary findings, withdrawal limits and applicable institutional oversight. Teach on synthetic datasets without attempting participant identification. Preregister an analysis comparison in plain language: what signal is sought, which confounders are anticipated, how filtering will work, which readouts matter, and what observation would count against the favored interpretation. When comparing results, include the reference assembly or database release, observation level, quality thresholds, removed records and a denominator for each proportion. Missing genomic measurements are not synonymous with confidently absent biological events. Explain which parts of the pipeline are deterministic transformations and which rely on empirical model assumptions.

### Fictional case and competing explanation

A fictional research partnership considers releasing identifiable genetic ancestry maps; stakeholder consultation changes the public release plan to controlled access and aggregated summaries. This is a hypothetical instructional case, not a reported finding. Begin with one biological hypothesis and one technical or sampling rival. Before choosing the most interesting interpretation, write down what each hypothesis predicts about a newly collected specimen or orthogonal assay. Different algorithms may agree because they reuse the same flawed reference or measurement, not because they supply independent experimental confirmation.

### Worked example with units

**Problem:** If 18 of 24 participants select a particular optional sharing scope, observed proportion is 75%; these consent preferences cannot be extrapolated to unconsulted communities.

**Calculation:** `18/24*100` = **75 %** for the invented inputs. To test your interpretation, change one input within a plausible synthetic range and recompute the output. The goal is not to fit actual organisms but to understand how measurement assumptions propagate through the equation. Correct arithmetic validates a calculation, but it does not establish that the input data are representative or that the result has a causal meaning. Record whether the denominator counts bases, reads, allele copies, individuals, loci or experimental runs. Recompute with a modified hypothetical input to examine numerical sensitivity.

### Error modes and validation design

Removing names from full genomes does not guarantee anonymity; communities can experience harm even when individual identifiers are not published. If the measurement was duplicated at the technical level, name the correct independent sampling level before offering any significance claim. Replication improves confidence only to the extent that it samples the relevant biological variability. **Audit emphasis — State the reference.** Describe what counts as a matching coordinate, allele or feature under the selected reference. Changing a reference can change apparent variants or gene boundaries while the original material remains unchanged.

Write a release risk assessment involving families and source communities, and evaluate reproducibility routes that do not require making sensitive data unrestricted. The proposed new evidence should help discriminate between mechanisms rather than merely producing another version of the same computational score. Explain the important negative control and a result that would weaken your preferred hypothesis. In a scientific report, keep measurements, computed statistics, model-based predictions and proposed biological explanations in separate statements.

### Transfer exercise

Connect **Consent, genomic privacy and benefit sharing** with **Pharmacogenomics and context-sensitive evidence**. Explain which source-data error would contaminate both topics and how a reference-aware provenance record would reveal it. Then answer: What was measured? How was the statistic calculated? What competing explanation remains? What independent experiment would be most efficient? Present the final inference as a conditional claim whose strength matches the available evidence.

---

## Unit 07 capstone — Responsible genomic evidence conference

### Situation and materials

Review a wholly invented pedigree, an uncertain sequence variant, a cancer-like mixture signal and a list of consent restrictions. No identifiable personal or clinical data are used. Assume all records are fabricated for the classroom. Start by listing the observational units: organism, donor, biological preparation, technical library, genomic site or algorithmic summary. This is a crucial step because denominator mistakes can produce a result that is mathematically correct but scientifically misleading. Fix the reference and analysis version for the exercise before comparing any numbers, and include unknowns explicitly.

### Procedure and minimum outputs

Assign each statement to measurement, computational inference, uncertain biological interpretation or professional clinical decision. Compute sample-specific frequency and variant-read fractions with their actual denominators. Your calculations need not be complicated. They should be completely reproducible, with input values, a visible formula, arithmetic and units. Create one well-documented table for the observations, a second for transformations, and a third for which interpretations survive each quality check. Explain the transformations in words rather than copying a tool output without explanation. Before choosing a cutoff, describe the costs of false positive and false negative findings in this particular fictional study.

### Competing hypotheses and sensitivity experiment

Discuss how database ancestry imbalance, age-related penetrance, tumor purity and phase ambiguity affect conclusions. Write a participant-facing explanation that avoids both alarm and false reassurance. Your favored explanation should generate a prediction that would be less likely under a clearly named alternative. Design one sensitivity exercise that changes a single assumption—such as callable regions, phase, ancestry strata, normalization rule or depth threshold—and track its effect on the main statistic. If the preferred interpretation changes, report that dependence rather than selecting the setting with the most dramatic result. Explain which new specimen, assay or observation would provide the best independent discrimination.

### Deliverables, reflection and peer review

Submit an evidence-classification worksheet and a privacy-preserving analysis plan, with no diagnostic or treatment advice. In addition, prepare a reproducibility manifest with input identifiers, simulated-only status, calculations, method version and a short rationale for every excluded observation. Include a four-sentence abstract distinguishing what is measured, estimated, hypothesized and still unknown. Exchange reports with another learner, ask them to recalculate at least one statistic using only the supplied source data, and record one objection that improves the design. Do not describe any result as clinical, diagnostic or measured in the real world.

### Challenge questions for synthesis

1. Which dataset field would have the greatest impact if it were silently mislabeled? Identify a simple audit that could catch the mistake before modeling.
2. Does the unit's central conclusion rely on random sampling, correct genome representation, accurate molecular classification or independent replication? Rank those assumptions in importance for this case.
3. What result could falsify the leading explanation without proving every alternative? Discuss the distinction between rejection of one hypothesis and proof of another.
4. If your method produced a visually excellent plot from copied or confounded measurements, what independent check would you demand before publication?
5. Explain why the precise mathematical result alone does not certify the biological or social validity of the research conclusion.

---

## Two interactive teaching models

Change each slider, observe its graph and record which assumptions make the formula valid. These are hypothetical mathematical demonstrations, not empirical sequence analyses.

### Model 7.1: Toy Bayes positive predictive value

**Equation:** PPV=Se p/[Se p+(1−Sp)(1−p)]. **Caveat:** Sensitivity=.90 and specificity=.95 assumed; not clinical. Change the independent parameter, then explain whether the output change is a simple mathematical consequence or requires a biological inference. A monotone visual trend is not automatically a causal biological law. Identify the units and what is held constant.

### Model 7.2: Observed sample penetrance

**Equation:** Observed proportion=affected/20. **Caveat:** Selected sample, not population risk. Change the independent parameter, then explain whether the output change is a simple mathematical consequence or requires a biological inference. A monotone visual trend is not automatically a causal biological law. Identify the units and what is held constant.
