# Unit 8: Genetic investigation

## Unit overview

Genetic investigation combines careful experimental design with evidence management and ethical judgment. A credible conclusion requires genotype quality, independent verification, appropriate comparison groups, and an honest account of what a study cannot resolve. Family data and genomic datasets can be identifiable even after names are removed, so simulated classroom exercises cannot be treated as permission for real-world disclosure. This unit integrates crosses, pedigree likelihood, variant evidence and data governance into a repeatable research workflow.

## Learning goals

Explain mechanisms without conflating genotype, molecular state and observable phenotype; formulate explicit conditional probabilities; solve distinct numerical examples with appropriate denominators; evaluate experimental controls; challenge an alternative interpretation; and inspect the assumptions behind each interactive model.

## 8.1 Crosses and experimental design

### Mechanistic foundation: Crosses and experimental design

A genetic cross is informative only when parental genotypes, scoring rules, replication and transmission assumptions are explicit. Reciprocal crosses can reveal parent-of-origin or sex-linked patterns; testcrosses expose gametes; controlled backcrosses isolate particular segregating regions. Blind phenotype classification and prespecified exclusion criteria reduce bias. Viability selection, maternal effects and developmental stage can alter observed categories.

For **crosses and experimental design**, a model written without its inheritance assumptions is not a complete explanation.

### A quantitative example with a defined denominator

Under an Aa×aa cross with full penetrance and equal transmission, 200 offspring are expected to split 100 Aa and 100 aa.

Read the example in two passes. First solve the arithmetic as a hypothetical well-controlled classroom case. This separates a mathematical exercise from a causal scientific finding.

### From the process to an experiment

Randomize growth trays, genotype parents with a separate assay, collect enough independent crosses, and report missing observations before combining offspring into pooled classes. Specify an independent biological unit of replication. Those are different controls and answer different questions.

For **crosses and experimental design**, interpretation should follow the biology of the observation, not merely whether a significance threshold was crossed.

### Interpretations worth separating

A single large offspring count from one biological parent pair may not represent independent families or environments.

Compare the focal mechanism with **pedigree likelihoods**, using the dedicated topic section rather than assuming these labels describe the same process. The comparison is not evidence that one causes the other. It is a deliberate stress test for the student's categories. State explicitly when none of these strategies is feasible.

### Annotated investigation notebook

Start a new notebook entry titled *Crosses and experimental design: prior expectation, actual measurement, alternate mechanism*. Record the outcome before labeling it a confirmation or discrepancy.

For the next pass, consider the topic **genomics and variant interpretation**. Review its own mechanistic discussion before assuming a relationship. Ask whether it changes the apparent prediction for **crosses and experimental design**, changes only what is measured, or concerns a different scientific level entirely.

### A second, more demanding application

The memo must discuss **crosses and experimental design** using this design constraint: Randomize growth trays, genotype parents with a separate assay, collect enough independent crosses, and report missing observations before combining offspring into pooled classes. What would a null result say about assay power?

The main limitation for this subsection is not decorative fine print: A single large offspring count from one biological parent pair may not represent independent families or environments.

### Connection to the next course topic

A later unit investigates **probability in pedigrees**, whose underlying level of analysis should be inspected in that section.

## 8.2 Pedigree likelihoods

### Mechanistic foundation: Pedigree likelihoods

Pedigree analysis compares the probability of observed genotypes and phenotypes under alternate inheritance models. Incomplete penetrance, de novo variants, mosaicism and measurement error require likelihoods rather than deterministic labels. Conditional probabilities depend on ascertainment: families recruited because of an affected child are not random samples of all families. Molecular verification narrows possibilities but does not remove uncertainty in interpretation.

For **pedigree likelihoods**, a model written without its inheritance assumptions is not a complete explanation.

### A quantitative example with a defined denominator

With P(Aa)=0.1, sensitivity 0.95 and false-positive rate 0.02, the positive-test posterior is 0.095/(0.095+0.018)=0.841.

Read the example in two passes. First solve the arithmetic as a hypothetical well-controlled classroom case. This separates a mathematical exercise from a causal scientific finding.

### From the process to an experiment

Code a tiny pedigree enumerator for a specified autosomal locus, document allele priors and penetrance, and compare the result to manual state enumeration. Specify an independent biological unit of replication. Those are different controls and answer different questions.

For **pedigree likelihoods**, interpretation should follow the biology of the observation, not merely whether a significance threshold was crossed.

### Interpretations worth separating

A Bayesian posterior also depends on prior disease prevalence and test performance; a likelihood ratio alone is not an absolute risk.

Compare the focal mechanism with **genomics and variant interpretation**, using the dedicated topic section rather than assuming these labels describe the same process. The comparison is not evidence that one causes the other. It is a deliberate stress test for the student's categories. State explicitly when none of these strategies is feasible.

### Annotated investigation notebook

Start a new notebook entry titled *Pedigree likelihoods: prior expectation, actual measurement, alternate mechanism*. Record the outcome before labeling it a confirmation or discrepancy.

For the next pass, consider the topic **ethics, privacy and inference**. Review its own mechanistic discussion before assuming a relationship. Ask whether it changes the apparent prediction for **pedigree likelihoods**, changes only what is measured, or concerns a different scientific level entirely.

### A second, more demanding application

The memo must discuss **pedigree likelihoods** using this design constraint: Code a tiny pedigree enumerator for a specified autosomal locus, document allele priors and penetrance, and compare the result to manual state enumeration. What would a null result say about assay power?

The main limitation for this subsection is not decorative fine print: A Bayesian posterior also depends on prior disease prevalence and test performance; a likelihood ratio alone is not an absolute risk.

### Connection to the next course topic

A later unit investigates **linkage and assortment**, whose underlying level of analysis should be inspected in that section.

## 8.3 Genomics and variant interpretation

### Mechanistic foundation: Genomics and variant interpretation

Sequence variants require quality, context, segregation and functional evidence to interpret. A read-depth decrease can represent a deletion, coverage bias or mixture of cell states. Population databases inform allele frequency but must match ancestry and quality criteria. Pathogenicity labels are evidence classifications, not arithmetic outputs of one annotation predictor. Variants of uncertain significance should not be treated as confirmed causal drivers.

For **genomics and variant interpretation**, a model written without its inheritance assumptions is not a complete explanation.

### A quantitative example with a defined denominator

If 80 of 100 high-quality reads support a synthetic variant allele in a model tissue, observed variant allele fraction is 0.80, not necessarily germline copy number.

Read the example in two passes. First solve the arithmetic as a hypothetical well-controlled classroom case. This separates a mathematical exercise from a causal scientific finding.

### From the process to an experiment

Independently verify read mapping, call filters, sample identity and genotype quality; compare functional tests and segregation information with explicit alternate explanations. Specify an independent biological unit of replication. Those are different controls and answer different questions.

For **genomics and variant interpretation**, interpretation should follow the biology of the observation, not merely whether a significance threshold was crossed.

### Interpretations worth separating

Variant interpretation in medical contexts requires qualified professionals and updated practice guidance; teaching models do not provide clinical recommendations.

Compare the focal mechanism with **ethics, privacy and inference**, using the dedicated topic section rather than assuming these labels describe the same process. The comparison is not evidence that one causes the other. It is a deliberate stress test for the student's categories. State explicitly when none of these strategies is feasible.

### Annotated investigation notebook

Start a new notebook entry titled *Genomics and variant interpretation: prior expectation, actual measurement, alternate mechanism*. Record the outcome before labeling it a confirmation or discrepancy.

For the next pass, consider the topic **crosses and experimental design**. Review its own mechanistic discussion before assuming a relationship. Ask whether it changes the apparent prediction for **genomics and variant interpretation**, changes only what is measured, or concerns a different scientific level entirely.

### A second, more demanding application

The memo must discuss **genomics and variant interpretation** using this design constraint: Independently verify read mapping, call filters, sample identity and genotype quality; compare functional tests and segregation information with explicit alternate explanations. What would a null result say about assay power?

The main limitation for this subsection is not decorative fine print: Variant interpretation in medical contexts requires qualified professionals and updated practice guidance; teaching models do not provide clinical recommendations.

### Connection to the next course topic

A later unit investigates **sex-linked inheritance**, whose underlying level of analysis should be inspected in that section.

## 8.4 Ethics, privacy and inference

### Mechanistic foundation: Ethics, privacy and inference

Genetic information is probabilistic, potentially familial and sensitive. Consent must distinguish research sequencing from return of results, secondary reuse and sharing with collaborators. An ancestry-informative association can reflect population structure without supporting biological race categories. Decisions about disclosure should consider uncertainty, re-identification, family implications and unequal access to interpretation.

For **ethics, privacy and inference**, a model written without its inheritance assumptions is not a complete explanation.

### A quantitative example with a defined denominator

A 1% population frequency cannot be used as the individual probability of a condition without knowing genotype, penetrance and ascertainment.

Read the example in two passes. First solve the arithmetic as a hypothetical well-controlled classroom case. This separates a mathematical exercise from a causal scientific finding.

### From the process to an experiment

Prepare a mock data governance plan defining consent scope, anonymization limits, data retention, access logging, and a procedure for withdrawing future use where technically feasible. Specify an independent biological unit of replication. Those are different controls and answer different questions.

For **ethics, privacy and inference**, interpretation should follow the biology of the observation, not merely whether a significance threshold was crossed.

### Interpretations worth separating

A classroom genetic model cannot determine an individual’s identity, reproductive choices or medical diagnosis; avoid deterministic language.

Compare the focal mechanism with **crosses and experimental design**, using the dedicated topic section rather than assuming these labels describe the same process. The comparison is not evidence that one causes the other. It is a deliberate stress test for the student's categories. State explicitly when none of these strategies is feasible.

### Annotated investigation notebook

Start a new notebook entry titled *Ethics, privacy and inference: prior expectation, actual measurement, alternate mechanism*. Record the outcome before labeling it a confirmation or discrepancy.

For the next pass, consider the topic **pedigree likelihoods**. Review its own mechanistic discussion before assuming a relationship. Ask whether it changes the apparent prediction for **ethics, privacy and inference**, changes only what is measured, or concerns a different scientific level entirely.

### A second, more demanding application

The memo must discuss **ethics, privacy and inference** using this design constraint: Prepare a mock data governance plan defining consent scope, anonymization limits, data retention, access logging, and a procedure for withdrawing future use where technically feasible. What would a null result say about assay power?

The main limitation for this subsection is not decorative fine print: A classroom genetic model cannot determine an individual’s identity, reproductive choices or medical diagnosis; avoid deterministic language.

### Connection to the next course topic

A later unit investigates **mendelian segregation**, whose underlying level of analysis should be inspected in that section.

## Advanced studio: genetics research from design to responsible reporting

### What a cross can and cannot identify

An experimental cross starts with known parent identities, verified genotypes and a clearly defined offspring scoring rule. A reciprocal cross reverses which parental line contributes a particular allele or cytoplasmic background, potentially revealing parent-of-origin or cytoplasmic effects. A testcross mates a segregating individual with a genetically informative partner so that gamete haplotypes can be read from offspring. A backcross returns offspring to one parental genetic background and can be useful for introgression or linkage analysis. These designs answer different questions; choosing a familiar cross without confirming that it distinguishes rival explanations can consume many offspring without advancing knowledge.

Imagine a plant trait apparently transmitted at one half in an Aa × aa backcross. Before scoring offspring, determine whether genotype and phenotype can be measured independently. If the environment affects phenotype penetrance, a one-to-one phenotypic ratio might not directly show the genotype ratio. Repeat the cross with parental roles switched when biologically possible and control germination stage, tissue and scoring thresholds. Families are biological clusters; pooling all offspring across a few parental pairs without accounting for parental effects may underestimate uncertainty. The student should record the number of independent crosses and the number of offspring per cross separately.

### Pedigree likelihoods need ascertainment rules

A pedigree likelihood models the probability of the entire observed combination of genotypes and phenotypes under a proposed inheritance mechanism. Unknown genotypes are summed over rather than assigned by intuition. For an autosomal recessive condition, the presence of an affected individual changes posterior probabilities for relatives, but only after the known sampling rule and penetrance model have been specified. Families recruited because a particular child is affected are statistically different from families sampled at random. Ignoring that selection can produce biased prevalence or penetrance estimates.

Consider a toy carrier test with a prior probability of 0.1, sensitivity 0.95 and false-positive probability 0.02. A positive test occurs through carrier true positives with joint probability 0.095 or noncarrier false positives with probability 0.018. The posterior carrier probability conditional on a positive test is 0.095/(0.095+0.018), approximately 0.841. This is less than the assay's sensitivity because a posterior is a probability about genotype given a result, whereas sensitivity is a probability of a result given genotype. The prior population and assay validity matter; the numbers do not constitute guidance for a real person.

### Interpreting a variant requires multiple lines of evidence

Modern sequencing may return millions of differences relative to a reference genome. A useful interpretation begins with mapping quality, genotype likelihood, local sequence context and sample identity. Next evaluate population frequency, inheritance pattern, possible molecular effect and, where available, controlled functional evidence. A reported allele fraction of 0.8 in a tissue is a fraction of reads supporting a variant at a locus. It could reflect cell mixture, sequencing bias, copy-number change or a genuine allele imbalance; it should not be converted automatically into a germline genotype. Quality control is a scientific stage, not merely a computational housekeeping step.

For an uncertain variant, evidence can point in competing directions. A computational predictor may label an amino-acid substitution disruptive while family segregation is weak. A molecular assay may show altered transcript abundance but no measured phenotypic effect. The correct conclusion can be uncertainty. In medical contexts, interpretation systems and recommendations change as evidence develops, and qualified professionals must handle diagnostic decisions. Classroom worksheets may demonstrate the logic of evidence weighting but must not imply that a simplified formula overrides a validated clinical framework.

### Genetics data affect relatives and communities

A genome is not an isolated anonymous string. Alleles and long shared haplotypes can convey information about relatives, even when direct identifiers are stripped. Data governance therefore requires explicit scope for consent, honest discussion of secondary uses, controlled access, auditing and appropriate retention plans. A promise of absolute anonymity is generally stronger than can be justified for rich genomic data. Research proposals should identify who may access the information, for what purposes, under which ethical oversight and with what process for future changes. Consent for one analysis should not silently become consent for unrestricted commercialization.

Ancestry is statistically relevant to some genetic analyses because allele and haplotype frequencies vary with population history, but group differences cannot be interpreted as a ranking of human worth or capacity. Environmental inequalities and selection bias can correlate with genetic sampling patterns, creating false causal narratives if population structure is poorly modeled. Reports should identify uncertainty, avoid deterministic claims about identity or behavior, and protect participants from stigmatizing interpretations. Good methodology improves both scientific accuracy and ethical responsibility.

### A complete reproducible research packet

Close the book by preparing a mock research packet: a preregistered question, synthetic data dictionary, population definition, consent assumptions, laboratory or computational protocol, quality checks, primary model, negative controls, sensitivity analysis, uncertainty estimates, and a decision log for every excluded observation. Include executable code for the selected probability models and three examples where an identical-looking phenotype has different underlying genetic explanations. Place raw synthetic observations in one file and derived quantities in another so that analysts can trace every plotted number to its source. The packet should state what is known, what is inferred, what is unsupported and what additional data would change the conclusion. This is the foundation of trustworthy genetic investigation.

## Further conceptual check: uncertainty after consent and analysis

An ethical genetic study needs a plan for uncertainty discovered after data collection. A variant initially considered innocuous may later gain evidence of clinical relevance, while another initially suspected variant may turn out to be unrelated to the phenotype. Whether and how to recontact participants depends on consent, study purpose, governance and professional oversight. A research sequence database should not silently promise continuous clinical reinterpretation if no personnel or funding have been assigned to that task. Likewise, receiving one genetic result does not imply unrestricted permission to inspect or disclose relatives' probable genotypes.

For a student research packet, include a versioned interpretation field with the date and evidence class of each conclusion. Distinguish raw genotype observations from interpretations based on then-current scientific understanding. Keep an access log and note whether aggregate analyses can remain after a participant withdraws future participation, subject to the study's approved rules. If a dataset is shared in a classroom, synthetic variants and invented pedigrees avoid exposing personal information. The goal is to learn analytical discipline while acknowledging that real genetic findings carry responsibilities beyond a numerical answer.

## Integrated Genetics Laboratory 8: Genetic investigation

This laboratory is a written and computational design exercise. The first case involves **crosses and experimental design**: Under an Aa×aa cross with full penetrance and equal transmission, 200 offspring are expected to split 100 Aa and 100 aa. The second involves **pedigree likelihoods**: With P(Aa)=0.1, sensitivity 0.95 and false-positive rate 0.02, the positive-test posterior is 0.095/(0.095+0.018)=0.841. Treat both as mathematical thought experiments with supplied assumptions.

**Protocol design.** Begin by enumerating possible states without scoring phenotypes. Include one independent validation of the genotype or marker state. The rationale for the first experiment is Randomize growth trays, genotype parents with a separate assay, collect enough independent crosses, and report missing observations before combining offspring into pooled classes. A competing observation strategy involves Code a tiny pedigree enumerator for a specified autosomal locus, document allele priors and penetrance, and compare the result to manual state enumeration. These need not have the same denominator or uncertainty model.

Then compare the inference to **genomics and variant interpretation**. Its mechanism is: Sequence variants require quality, context, segregation and functional evidence to interpret.

It includes the caveat for **ethics, privacy and inference**: A classroom genetic model cannot determine an individual’s identity, reproductive choices or medical diagnosis; avoid deterministic language. For a population-frequency estimate include the time and sampling frame. For a family inference specify the selection rule for included pedigrees.

**Ethical and reproducibility note.** Use synthetic or appropriately consented data only. Share versioned simulation settings and code, not identifying family genomic records.

## Fully worked questions

All examples below are hypothetical and contain the necessary model assumptions. Solutions are provided to make reasoning inspectable rather than turning a genetics inference into a memorized ratio.

### Problem 1: Backcross expectation

A known Aa genotype is backcrossed to aa under fair segregation. What genotypes are expected among 200 offspring?

**Worked solution**

1. Aa produces A and a gametes with equal probability; aa produces only a.
2. Offspring are Aa with probability one half and aa with probability one half.
3. Expected counts are 100 Aa and 100 aa, while observed counts will vary. Viability differences could alter the observed distribution.

### Problem 2: Positive genetic test

A toy trait carrier prior is 0.1, sensitivity 0.95 and false-positive rate 0.02. Find P(carrier | positive).

**Worked solution**

1. Compute true-positive joint probability 0.1×0.95=0.095.
2. Compute false-positive joint probability 0.9×0.02=0.018.
3. Bayes posterior is 0.095/(0.095+0.018)=0.840708. This is a hypothetical teaching calculation, not a clinical result.

### Problem 3: Variant allele fraction

A synthetic sequencing dataset has 80 reads supporting a variant out of 100 high-quality reads. Find variant read fraction.

**Worked solution**

1. State denominator as all quality-filtered informative reads at the locus, not all genome reads.
2. Variant allele fraction is 80/100=0.80, or 80%.
3. Read fraction is not automatically a germline genotype or absolute copy number because coverage and cell mixture can distort it.

## Interactive genetics investigation

These interactive models are explicitly simplified quantitative thought experiments. Use the sliders to change one assumption at a time, inspect the curve or categorical display, check a limiting case, and reset to the baseline. A classroom model is not a clinical test or a measured population estimate.

### Model: ld

The ld model provides a numerical expectation or uncertainty-dependent outcome associated with Unit 8. Copy the default readout, alter the first parameter, and predict whether the result should rise, fall or be nonmonotonic. Change the second parameter and identify which part of the equation it modifies. Return to the starting settings and check that the original value is restored. State whether the plotted quantity represents a probability, an expectation, a standardized statistic, or a physical copy count.

Model interpretation should refer back to the underlying derivation and the experimental denominators in this chapter. Do not extrapolate beyond the allowed slider range, and do not describe a smooth curve as data from an observed population. If the model rejects an impossible parameter combination, explain the rejected biological assumption in words rather than simply resetting the input.

### Model: posterior

The posterior model provides a numerical expectation or uncertainty-dependent outcome associated with Unit 8. Copy the default readout, alter the first parameter, and predict whether the result should rise, fall or be nonmonotonic. Change the second parameter and identify which part of the equation it modifies. Return to the starting settings and check that the original value is restored. State whether the plotted quantity represents a probability, an expectation, a standardized statistic, or a physical copy count.

Model interpretation should refer back to the underlying derivation and the experimental denominators in this chapter. Do not extrapolate beyond the allowed slider range, and do not describe a smooth curve as data from an observed population. If the model rejects an impossible parameter combination, explain the rejected biological assumption in words rather than simply resetting the input.
