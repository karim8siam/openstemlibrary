# Unit 1: Inheritance

## Unit overview

Inheritance is a process of conditional transmission, not a lookup table assigning fixed outcomes to all parents. The same observed family can be compatible with several causal explanations. Start with a single locus and physically follow homologs into gametes before computing zygote probabilities. Next distinguish genotypes from phenotypes, and update family probabilities only after identifying the evidence on which a calculation is conditioned. The models here deliberately expose the assumptions hidden behind familiar ratios. No exercise uses an identifiable human family or a clinical diagnosis.

## Learning goals

Explain mechanisms without conflating genotype, molecular state and observable phenotype; formulate explicit conditional probabilities; solve distinct numerical examples with appropriate denominators; evaluate experimental controls; challenge an alternative interpretation; and inspect the assumptions behind each interactive model.

## 1.1 Mendelian segregation

### Mechanistic foundation: Mendelian segregation

A heterozygous diploid parent carries two distinct alleles at one autosomal locus, but an ordinary gamete receives only one homolog. An Aa by Aa cross produces AA, Aa, and aa zygotes in the familiar one-to-two-to-one ratio when meiotic transmission and fertilization are unbiased. A dominant phenotype can therefore conceal two genotypes. Trait categories must be defined before the cross, since continuous morphology, environmental effects, and variable penetrance can make an apparent binary score unreliable.

The teaching goal is to follow a specific causal chain rather than simply assign a name to a pattern. Identify the material that is inherited, which division or biochemical process can alter it, the observable output and the comparison group. For **mendelian segregation**, a model written without its inheritance assumptions is not a complete explanation. Test whether a proposed result would still follow if the sample included individuals with different genetic backgrounds, developmental stages or measurement environments. The distinction is important because two experiments with the same mean outcome can arrive there through different mixtures of genotypes and measurement errors.

### A quantitative example with a defined denominator

In a synthetic 160-seed cross the expectation is 40 AA, 80 Aa and 40 aa. Ask whether an observed 37:83:40 is evidence for changed segregation or routine sampling noise. Before substituting numbers into an equation, label every numerator and denominator in words. If an observation is a frequency, specify whether it counts gametes, allele copies, independent families, sequenced reads or individuals. If the numerator is an estimated quantity rather than a direct count, state the assumptions used to calculate it. Then ask whether the comparison involves a probability conditional on known parental genotypes or an estimate sampled from a population. Confusing those two statements produces incorrect uncertainty and incorrect predictions for later generations.

Read the example in two passes. First solve the arithmetic as a hypothetical well-controlled classroom case. Next change one biological assumption and predict which term of the calculation breaks. Altering penetrance affects a phenotype likelihood, whereas altering allele transmission changes a gamete probability; changing a sample ascertainment rule affects the meaning of an observed frequency even if the molecular mechanism is unchanged. Whenever a simple numerical relationship succeeds, write down the smallest set of assumptions under which that success is informative. This separates a mathematical exercise from a causal scientific finding.

### From the process to an experiment

Cross two verified heterozygotes, score genotypes independently of phenotype, and compare observed genotype proportions with the Mendelian null using a multinomial analysis. Record seed viability as well as germinated offspring; differential mortality can distort counts. Specify an independent biological unit of replication. Ten DNA reads from one individual are not ten independent offspring; ten cells from one dish may share treatment history; ten offspring from one parent pair are not independent parental families. A legitimate experiment records the level at which treatment or inheritance varies and avoids overstating the effective sample size. Plan at least one control directed at assay reliability and another directed at the biological explanation. Those are different controls and answer different questions.

One practical workflow starts by defining a genotype or chromosome state with a separately verified method. Record the prospective phenotype classification or molecular measurement rule before examining the main outcome. Then collect a balanced comparison where possible, quantify missing observations, and keep an audit trail of excluded records. An analysis table should report raw counts alongside normalized frequencies, because normalized plots can conceal tiny denominators or selective omission. For **mendelian segregation**, interpretation should follow the biology of the observation, not merely whether a significance threshold was crossed.

### Interpretations worth separating

A ratio predicted for surviving offspring is not guaranteed if any genotype changes survival or if phenotype scoring is imperfect. Consider at least three classes of alternative explanation: inherited architecture, environmental or developmental conditions, and technical measurement. A difference between genotyped groups might arise from genuine functional differences, background linkage with another causal locus, or batch effects correlated with sample labels. The appropriate test depends on whether the claim is about transmission, molecular function, association or evolutionary change. An orthogonal measurement is most convincing when it fails in a different way from the original assay.

Compare the focal mechanism with **probability in pedigrees**, using the dedicated topic section rather than assuming these labels describe the same process. The comparison is not evidence that one causes the other. It is a deliberate stress test for the student's categories. If the second process predicts the same endpoint, design an additional measurement that breaks the tie. For a family-based inference, ask what a reciprocal cross would reveal; for a population sample, ask whether ancestry stratification changes the estimate; for a laboratory intervention, ask whether rescue or a second perturbation supports specificity. State explicitly when none of these strategies is feasible.

### Annotated investigation notebook

Start a new notebook entry titled *Mendelian segregation: prior expectation, actual measurement, alternate mechanism*. Put the starting assumption in the first line and a falsifiable prediction in the second. Record the outcome before labeling it a confirmation or discrepancy. A predicted ratio is not a confidence interval, and an observed point estimate is not an exact biological law. The entry should keep observations and interpretation in different columns, with measurement units, uncertainty, and any known exclusions visible. A reader who was absent from the experiment should be able to reconstruct what was measured.

For the next pass, consider the topic **linkage and assortment**. Review its own mechanistic discussion before assuming a relationship. Ask whether it changes the apparent prediction for **mendelian segregation**, changes only what is measured, or concerns a different scientific level entirely. If the two mechanisms are logically independent, it is appropriate to state that fact rather than invent a connection. Develop a negative control that would remain unchanged under the focal hypothesis, and then identify a positive control whose successful outcome demonstrates that the measurement procedure was capable of detecting the expected change.

### A second, more demanding application

Write a research memo for a hypothetical dataset that records an apparent deviation from the simple expectation. The memo must discuss **mendelian segregation** using this design constraint: Cross two verified heterozygotes, score genotypes independently of phenotype, and compare observed genotype proportions with the Mendelian null using a multinomial analysis. It should not invent numerical results or imply an experiment has been performed. Instead produce a table of possible result patterns, and for each pattern write the strongest warranted inference. What would a null result say about assay power? What if an orthogonal assay agrees while a closely related measurement does not? Could a change in developmental timing alter the measured endpoint without changing the inherited allele?

The final check is to distinguish what belongs to model structure from what belongs to biological evidence. A model can be internally consistent and still be inapplicable because the sample is selected, the trait definition changes, or a key rate varies between individuals. The main limitation for this subsection is not decorative fine print: A ratio predicted for surviving offspring is not guaranteed if any genotype changes survival or if phenotype scoring is imperfect. List the predicted direction of bias, if it can be reasoned out, and mark it unknown otherwise. Unjustified certainty is a larger scientific error than a correctly qualified result.

### Connection to the next course topic

A later unit investigates **aneuploidy and nondisjunction**, whose underlying level of analysis should be inspected in that section. The relationship to the present topic is an invitation to examine the *level of explanation*. An inherited state and the population frequency of that state occupy different levels, as do allele dosage and protein abundance. A measurement can serve as evidence in two chapters while answering different questions. Write a sentence explaining what new kind of experiment would be needed before transferring an inference from one level to another. Finish with a diagram of causal arrows, unknown links and measured outcomes, and distinguish arrows justified by design from arrows merely suggested by correlation.

## 1.2 Probability in pedigrees

### Mechanistic foundation: Probability in pedigrees

A pedigree is a graph of biological relationships annotated by observed traits; it is not proof that one locus determines the trait. Condition each probability on the information actually observed. An unaffected person with an affected sibling has a two-thirds carrier probability for a fully penetrant autosomal recessive disorder when both parents are known carriers, because AA and Aa are the only unaffected genotypes after excluding aa. Population allele frequencies and test results may update that estimate by Bayes reasoning.

For **probability in pedigrees**, a model written without its inheritance assumptions is not a complete explanation.

### A quantitative example with a defined denominator

An unaffected sibling of an aa individual, born to two Aa parents, has P(Aa | unaffected)=2/3, not 1/2. Show the conditioning explicitly.

Read the example in two passes. First solve the arithmetic as a hypothetical well-controlled classroom case. This separates a mathematical exercise from a causal scientific finding.

### From the process to an experiment

Draw a three-generation synthetic pedigree with uncertain genotypes, write a likelihood for each inheritance model, and update with a molecular test whose sensitivity and specificity are stated. Specify an independent biological unit of replication. Those are different controls and answer different questions.

For **probability in pedigrees**, interpretation should follow the biology of the observation, not merely whether a significance threshold was crossed.

### Interpretations worth separating

Pedigree symbols do not encode penetrance, adoption, misattributed parentage, mosaicism or phenocopies automatically.

Compare the focal mechanism with **linkage and assortment**, using the dedicated topic section rather than assuming these labels describe the same process. The comparison is not evidence that one causes the other. It is a deliberate stress test for the student's categories. State explicitly when none of these strategies is feasible.

### Annotated investigation notebook

Start a new notebook entry titled *Probability in pedigrees: prior expectation, actual measurement, alternate mechanism*. Record the outcome before labeling it a confirmation or discrepancy.

For the next pass, consider the topic **sex-linked inheritance**. Review its own mechanistic discussion before assuming a relationship. Ask whether it changes the apparent prediction for **probability in pedigrees**, changes only what is measured, or concerns a different scientific level entirely.

### A second, more demanding application

The memo must discuss **probability in pedigrees** using this design constraint: Draw a three-generation synthetic pedigree with uncertain genotypes, write a likelihood for each inheritance model, and update with a molecular test whose sensitivity and specificity are stated. What would a null result say about assay power?

The main limitation for this subsection is not decorative fine print: Pedigree symbols do not encode penetrance, adoption, misattributed parentage, mosaicism or phenocopies automatically.

### Connection to the next course topic

A later unit investigates **copy number and dosage**, whose underlying level of analysis should be inspected in that section.

## 1.3 Linkage and assortment

### Mechanistic foundation: Linkage and assortment

Genes on different chromosomes are typically independently assorted during meiosis; loci on the same chromosome may be correlated because they travel on the same physical DNA molecules. A testcross can expose gamete haplotypes without masking by dominance. For a double heterozygote AB/ab crossed with ab/ab, parental AB and ab classes dominate when recombination is less than one half. Two recombinant classes, Ab and aB, share the total recombinant fraction in a symmetrical model.

For **linkage and assortment**, a model written without its inheritance assumptions is not a complete explanation.

### A quantitative example with a defined denominator

For 400 informative progeny and 64 recombinants, r=64/400=0.16, or approximately 16 centimorgans for a short map interval.

Read the example in two passes. First solve the arithmetic as a hypothetical well-controlled classroom case. This separates a mathematical exercise from a causal scientific finding.

### From the process to an experiment

Score a blinded four-category testcross table, designate parental classes using phase information, and estimate recombination fraction with a confidence interval. Specify an independent biological unit of replication. Those are different controls and answer different questions.

For **linkage and assortment**, interpretation should follow the biology of the observation, not merely whether a significance threshold was crossed.

### Interpretations worth separating

A recombination fraction of one half does not prove that loci are on different chromosomes; widely separated loci on one chromosome may appear unlinked.

Compare the focal mechanism with **sex-linked inheritance**, using the dedicated topic section rather than assuming these labels describe the same process. The comparison is not evidence that one causes the other. It is a deliberate stress test for the student's categories. State explicitly when none of these strategies is feasible.

### Annotated investigation notebook

Start a new notebook entry titled *Linkage and assortment: prior expectation, actual measurement, alternate mechanism*. Record the outcome before labeling it a confirmation or discrepancy.

For the next pass, consider the topic **mendelian segregation**. Review its own mechanistic discussion before assuming a relationship. Ask whether it changes the apparent prediction for **linkage and assortment**, changes only what is measured, or concerns a different scientific level entirely.

### A second, more demanding application

The memo must discuss **linkage and assortment** using this design constraint: Score a blinded four-category testcross table, designate parental classes using phase information, and estimate recombination fraction with a confidence interval. What would a null result say about assay power?

The main limitation for this subsection is not decorative fine print: A recombination fraction of one half does not prove that loci are on different chromosomes; widely separated loci on one chromosome may appear unlinked.

### Connection to the next course topic

A later unit investigates **structural chromosome changes**, whose underlying level of analysis should be inspected in that section.

## 1.4 Sex-linked inheritance

### Mechanistic foundation: Sex-linked inheritance

X-linked variants have different transmission patterns depending on karyotype and which parent transmits the chromosome. In the common XY model, an XY parent passes an X chromosome to X-bearing offspring, not Y-bearing offspring; however sex development and chromosome complements are biologically diverse. An X-linked recessive allele can be expressed when only one functional copy is present. Carrier status, new variants and skewed X inactivation complicate textbook patterns.

For **sex-linked inheritance**, a model written without its inheritance assumptions is not a complete explanation.

### A quantitative example with a defined denominator

For an X-linked carrier mother XAXa and father XAY, a chromosomally XY child has a one-half probability of receiving Xa under fair segregation.

Read the example in two passes. First solve the arithmetic as a hypothetical well-controlled classroom case. This separates a mathematical exercise from a causal scientific finding.

### From the process to an experiment

Compare reciprocal crosses, assign explicit parental genotypes and chromosomal gametes, then score offspring by genotype rather than using appearance to infer sex chromosome content. Specify an independent biological unit of replication. Those are different controls and answer different questions.

For **sex-linked inheritance**, interpretation should follow the biology of the observation, not merely whether a significance threshold was crossed.

### Interpretations worth separating

Do not infer sex identity, phenotype, or an individual diagnosis directly from an abstract XX/XY classroom cross.

Compare the focal mechanism with **mendelian segregation**, using the dedicated topic section rather than assuming these labels describe the same process. The comparison is not evidence that one causes the other. It is a deliberate stress test for the student's categories. State explicitly when none of these strategies is feasible.

### Annotated investigation notebook

Start a new notebook entry titled *Sex-linked inheritance: prior expectation, actual measurement, alternate mechanism*. Record the outcome before labeling it a confirmation or discrepancy.

For the next pass, consider the topic **probability in pedigrees**. Review its own mechanistic discussion before assuming a relationship. Ask whether it changes the apparent prediction for **sex-linked inheritance**, changes only what is measured, or concerns a different scientific level entirely.

### A second, more demanding application

The memo must discuss **sex-linked inheritance** using this design constraint: Compare reciprocal crosses, assign explicit parental genotypes and chromosomal gametes, then score offspring by genotype rather than using appearance to infer sex chromosome content. What would a null result say about assay power?

The main limitation for this subsection is not decorative fine print: Do not infer sex identity, phenotype, or an individual diagnosis directly from an abstract XX/XY classroom cross.

### Connection to the next course topic

A later unit investigates **karyotypes and ploidy**, whose underlying level of analysis should be inspected in that section.

## Advanced studio: inheritance as a probability tree

### Starting with gametes instead of appearance

Consider a diploid flowering plant with a locus controlling an easily scored pigment. The experimenter has independently genotyped the parents as Aa and Aa. During ordinary reductional meiosis the homolog bearing A and the homolog bearing a enter different products. Write the maternal gamete probabilities as a vector (0.5,0.5), with the first component assigned to A; write the paternal vector the same way. Their outer product is a two-by-two matrix with four cells of probability 0.25. The diagonal entries represent AA and aa, while the off-diagonal entries represent the two parental origins of the same unordered genotype Aa. It is important that the matrix encodes ordered gamete origins even though a routine genotype report may combine them. If a researcher discovers a parent-of-origin effect, that once-irrelevant ordering can suddenly become biologically important.

Suppose a dominant pigment phenotype occurs in both AA and Aa. The phenotype fraction is three quarters only if the dominance classification is complete and the three expressing genotype–environment combinations have equivalent viability through observation. The word dominant describes the heterozygote relative to two homozygotes in a defined assay. It does not mean the allele is common, favorable, evolutionarily stronger, or uniformly expressed. To detect departures from fair segregation, genotype the offspring and estimate transmission probabilities before comparing colors. An observed 3:1 color ratio may persist even when the genotype ratio departs modestly from 1:2:1 because genotype-to-phenotype mapping has collapsed categories. That loss of information matters for inference.

### What does a pedigree probability mean?

A family is chosen for investigation after a child displays an uncommon recessive phenotype. The two biological parents are molecularly established carriers. In this family, the next child's probability of genotype aa is one quarter under the simple model. This prediction is made before the next child's genotype or phenotype is known. Now imagine examining an older unaffected sibling. It is mathematically wrong to treat the genotype alternatives as equally likely simply because AA and Aa are both compatible with being unaffected. Their prior probabilities are 1/4 and 1/2, and dividing by the sum 3/4 produces P(Aa | unaffected)=2/3. If the older sibling obtains a negative assay with imperfect sensitivity, the new probability requires an explicit measurement-likelihood term. A negative assay cannot be represented by deleting all carriers unless it is genuinely perfect.

One can illustrate this distinction using odds. Before testing, carrier-to-noncarrier odds among unaffected siblings are 2 to 1. Suppose a hypothetical screening assay is positive in 90% of carriers and falsely positive in 5% of noncarriers. For a positive result, the carrier-to-noncarrier likelihood ratio is 0.90/0.05=18, and posterior odds are 36 to 1. Convert odds back to a posterior probability 36/37, approximately 97.3%. This figure is an artificial arithmetic example, not a recommended clinical screening interpretation. The lesson is that family information and assay information enter at distinct stages. Real genetic counseling uses validated tests, clinically appropriate penetrance models and professional assessment.

### Phase, sex chromosomes and family ascertainment

When two loci are on the same chromosome, a double heterozygote can have AB/ab or Ab/aB phase. Both phase configurations contain A/a and B/b at the genotype level, yet they make different parental gamete pairs. A testcross with ab/ab exposes these gametes because the testcross parent contributes the same ab combination to every offspring. Four observed classes can then be partitioned into parental and recombinant types using the independently known phase. If one simply labels the two largest classes parental without checking survival, distorted fitness among offspring could make the label incorrect. Phase may instead be inferred with grandparental genotypes, physical haplotypes or molecular phasing algorithms.

For an X-linked recessive classroom pedigree, annotate parental chromosome complements and transmitted gametes rather than relying on unqualified statements about sons and daughters. A child receiving one variant X chromosome may express the associated phenotype in some chromosome contexts but not others. Skewed X inactivation, mosaicism and sex-chromosome variation demonstrate why the basic diagram is only one genetic framework. Human sex identity is not determined by a classroom Punnett square, and no individual should be categorized medically from a cartoon genotype. The purpose of the cross is transmission logic, not social classification.

### A falsifiable synthesis

Design a short report with four panels. Panel one displays independently verified parental genotypes. Panel two displays the gamete probability matrix. Panel three compares expected versus observed offspring genotype counts with sampling uncertainty. Panel four plots the observed pigment phenotype conditioned on offspring genotype. If panel three departs from expected counts but panel four does not, investigate viability, assay error and penetrance rather than immediately rewriting Mendel's law. If the genotype ratios match expectations but phenotype frequencies shift between growing conditions, examine gene–environment dependence and measurement thresholds. The same data, organized by causal stage, can distinguish questions that a single pooled trait ratio cannot.

## Further conceptual check: independence versus unrelatedness

Independent assortment and genetic independence should be distinguished from lack of biological interaction. Genes at two unlinked loci can contribute to the same enzyme pathway, even though their alleles assort independently in an ordinary meiosis. Conversely, closely linked markers may travel together in pedigrees yet affect completely unrelated biological processes. Crossing design addresses transmission correlation, while perturbation experiments address function. A student who finds a nonrandom association between genotypes at two locations should therefore consider linkage, population structure and biological selection before claiming one gene regulates the other.

For a double heterozygote AaBb at unlinked loci under simple fair segregation, there are four gamete types, AB, Ab, aB and ab, each with probability one quarter. If phase matters because the loci are linked, replace this equiprobable model with separate parental and recombinant class probabilities. A recombination fraction of 0.1 under AB/ab phase yields parental gametes at 0.45 each and recombinants at 0.05 each. Those numbers describe gamete formation before viability selection. To design a useful test, record genotypes rather than collapse all offspring into a dominant phenotype; otherwise distinct haplotype classes may become unidentifiable.

## Integrated Genetics Laboratory 1: Inheritance

**Objective.** Evaluate an inherited or population-level prediction by explicitly checking which observations distinguish explanations. This laboratory is a written and computational design exercise. No living organisms or personal genomic data are required, and no empirical result is invented. The first case involves **mendelian segregation**: In a synthetic 160-seed cross the expectation is 40 AA, 80 Aa and 40 aa. The second involves **probability in pedigrees**: An unaffected sibling of an aa individual, born to two Aa parents, has P(Aa | unaffected)=2/3, not 1/2. Show the conditioning explicitly. Treat both as mathematical thought experiments with supplied assumptions.

**Protocol design.** Begin by enumerating possible states without scoring phenotypes. Decide whether each record is a meiosis, an offspring, an allele copy, a family, a sequencing observation or a continuous trait measurement. Include one independent validation of the genotype or marker state. The rationale for the first experiment is Cross two verified heterozygotes, score genotypes independently of phenotype, and compare observed genotype proportions with the Mendelian null using a multinomial analysis. A competing observation strategy involves Draw a three-generation synthetic pedigree with uncertain genotypes, write a likelihood for each inheritance model, and update with a molecular test whose sensitivity and specificity are stated. These need not have the same denominator or uncertainty model. Write the proposed sample-size calculation for both; if relevant parameter values are not supplied, leave them symbolic instead of guessing.

**Analysis.** For each case, construct a row for the null expectation, observed quantity, uncertainty and a biological alternative. Then compare the inference to **linkage and assortment**. Its mechanism is: Genes on different chromosomes are typically independently assorted during meiosis; loci on the same chromosome may be correlated because they travel on the same physical DNA molecules. A testcross can expose gamete haplotypes without masking by dominance. A pattern that looks like support for one model may also follow from a change in sampling, viability, phase or phenotype definition. Write a sensitivity analysis in which the assumed marker error rate rises from zero to a small nonzero value. Do not assume the error causes only random noise; it can systematically attenuate an association or generate false discrepancies when error differs by group.

**Interpretation and report.** The final report is organized by claim, observed evidence, alternative explanation, and a proposed discriminating experiment. It includes the caveat for **sex-linked inheritance**: Do not infer sex identity, phenotype, or an individual diagnosis directly from an abstract XX/XY classroom cross. Record which uncertainty arises from sampling and which arises from the underlying biological model. For a population-frequency estimate include the time and sampling frame. For a family inference specify the selection rule for included pedigrees. For a molecular result distinguish sequence verification, expression, biochemical effect and organismal phenotype. Conclude with a concise statement containing a plausible range of outcomes, rather than an unsupported deterministic prediction.

**Ethical and reproducibility note.** Use synthetic or appropriately consented data only. Share versioned simulation settings and code, not identifying family genomic records. Keep failed or ambiguous outcomes in the analysis, report exclusions before interpretation, and distinguish computational expectations from empirical measurements. A credible analysis is reproducible when another student can reconstruct its inputs, equations, definitions, and decisions without contacting the original investigator. A formally accurate numeric answer is only one component of that standard.

## Fully worked questions

All examples below are hypothetical and contain the necessary model assumptions. Solutions are provided to make reasoning inspectable rather than turning a genetics inference into a memorized ratio.

### Problem 1: Two heterozygotes

In an Aa × Aa autosomal cross with fair segregation, calculate P(AA), P(Aa), P(aa), then expected genotype counts for 160 offspring.

**Worked solution**

1. Each parent produces A and a gametes with probability one half; combine them as four equiprobable products AA, Aa, aA and aa.
2. The two heterozygote products have the same unphased genotype, so P(AA)=1/4, P(Aa)=2/4 and P(aa)=1/4.
3. Multiply each fraction by 160 to obtain 40, 80 and 40. These are expected counts; observations vary because offspring are random draws.

### Problem 2: Carrier given unaffected

Two known Aa parents have an unaffected child under a fully penetrant autosomal recessive model. What is the probability that this child is a carrier?

**Worked solution**

1. Before observing health, the three genotype probabilities are AA=1/4, Aa=1/2 and aa=1/4.
2. Unaffected status excludes aa under the stipulated full-penetrance model. Its total probability is 3/4.
3. The conditional carrier probability is (1/2)/(3/4)=2/3. The value differs if penetrance, classification or parental genotypes differ.

### Problem 3: Testcross linkage

A phase-known AB/ab by ab/ab testcross yields 336 parental and 64 recombinant offspring. Estimate the pairwise recombination fraction.

**Worked solution**

1. Count all informative offspring: 336+64=400.
2. Recombination fraction r is recombinant offspring divided by all informative offspring: 64/400=0.16.
3. Express as 16% recombinants or approximately 16 cM for a short interval. Without a mapping function, do not assume the physical distance is 16% of a chromosome.

## Interactive genetics investigation

These interactive models are explicitly simplified quantitative thought experiments. Use the sliders to change one assumption at a time, inspect the curve or categorical display, check a limiting case, and reset to the baseline. A classroom model is not a clinical test or a measured population estimate.

### Model: mendel

The mendel model provides a numerical expectation or uncertainty-dependent outcome associated with Unit 1. Copy the default readout, alter the first parameter, and predict whether the result should rise, fall or be nonmonotonic. Change the second parameter and identify which part of the equation it modifies. Return to the starting settings and check that the original value is restored. State whether the plotted quantity represents a probability, an expectation, a standardized statistic, or a physical copy count.

Model interpretation should refer back to the underlying derivation and the experimental denominators in this chapter. Do not extrapolate beyond the allowed slider range, and do not describe a smooth curve as data from an observed population. If the model rejects an impossible parameter combination, explain the rejected biological assumption in words rather than simply resetting the input.

### Model: carrier

The carrier model provides a numerical expectation or uncertainty-dependent outcome associated with Unit 1. Copy the default readout, alter the first parameter, and predict whether the result should rise, fall or be nonmonotonic. Change the second parameter and identify which part of the equation it modifies. Return to the starting settings and check that the original value is restored. State whether the plotted quantity represents a probability, an expectation, a standardized statistic, or a physical copy count.

Model interpretation should refer back to the underlying derivation and the experimental denominators in this chapter. Do not extrapolate beyond the allowed slider range, and do not describe a smooth curve as data from an observed population. If the model rejects an impossible parameter combination, explain the rejected biological assumption in words rather than simply resetting the input.
