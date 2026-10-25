# Unit 3: Gene mapping

## Unit overview

Genetic maps describe recombination behavior; physical maps describe DNA coordinates. Neither measurement is a direct substitute for causal gene identification. Linkage requires phase, suitable family or cross data, defined markers and careful treatment of errors. Association across a population introduces a different probability model, influenced by ancestry and demography. This unit uses explicit denominators to prevent percentages of recombinants, centimorgans, LOD evidence and allele associations from being mistakenly interpreted as the same quantity.

## Learning goals

Explain mechanisms without conflating genotype, molecular state and observable phenotype; formulate explicit conditional probabilities; solve distinct numerical examples with appropriate denominators; evaluate experimental controls; challenge an alternative interpretation; and inspect the assumptions behind each interactive model.

## 3.1 Recombination fraction

### Mechanistic foundation: Recombination fraction

The recombination fraction between two markers is the proportion of informative meioses yielding recombinant marker combinations. For a simple testcross with known phase, estimate r by recombinant_count/total_count. Values greater than one half are not meaningful for an ordinary two-locus recombination fraction because recombination status becomes effectively randomized at that limit. Confidence depends on sample size, marker reliability and transmission distortion.

For **recombination fraction**, a model written without its inheritance assumptions is not a complete explanation.

### A quantitative example with a defined denominator

With 92 recombinants among 800 informative meioses, r=0.115. For short intervals this approximates 11.5 cM.

Read the example in two passes. First solve the arithmetic as a hypothetical well-controlled classroom case. This separates a mathematical exercise from a causal scientific finding.

### From the process to an experiment

Create a four-column haplotype count table and have two blinded analysts assign parental versus recombinant status. Quantify uncertainty using binomial or likelihood methods. Specify an independent biological unit of replication. Those are different controls and answer different questions.

For **recombination fraction**, interpretation should follow the biology of the observation, not merely whether a significance threshold was crossed.

### Interpretations worth separating

A one-centimorgan distance is not one percent of the physical chromosome length; centimorgans measure recombination probability, not base pairs.

Compare the focal mechanism with **three-point linkage order**, using the dedicated topic section rather than assuming these labels describe the same process. The comparison is not evidence that one causes the other. It is a deliberate stress test for the student's categories. State explicitly when none of these strategies is feasible.

### Annotated investigation notebook

Start a new notebook entry titled *Recombination fraction: prior expectation, actual measurement, alternate mechanism*. Record the outcome before labeling it a confirmation or discrepancy.

For the next pass, consider the topic **marker association and ld**. Review its own mechanistic discussion before assuming a relationship. Ask whether it changes the apparent prediction for **recombination fraction**, changes only what is measured, or concerns a different scientific level entirely.

### A second, more demanding application

The memo must discuss **recombination fraction** using this design constraint: Create a four-column haplotype count table and have two blinded analysts assign parental versus recombinant status. Quantify uncertainty using binomial or likelihood methods. What would a null result say about assay power?

The main limitation for this subsection is not decorative fine print: A one-centimorgan distance is not one percent of the physical chromosome length; centimorgans measure recombination probability, not base pairs.

### Connection to the next course topic

A later unit investigates **gene complementation**, whose underlying level of analysis should be inspected in that section.

## 3.2 Three-point linkage order

### Mechanistic foundation: Three-point linkage order

Three-locus testcrosses use the least frequent double-crossover classes to help identify the middle gene. Compare the most common parental class with each rare double recombinant; the marker that switches state is the internal marker under the classical three-point model. Recombination values for the adjacent intervals can then be calculated including double-crossover classes. Gene order is an inference that requires scoring all eight genotype classes and checking for viability distortion.

For **three-point linkage order**, a model written without its inheritance assumptions is not a complete explanation.

### A quantitative example with a defined denominator

For adjacent interval counts of 64 and 36 recombinant meioses among 1000 offspring, respective estimates are 6.4 cM and 3.6 cM; the outer interval requires a double-crossover correction.

Read the example in two passes. First solve the arithmetic as a hypothetical well-controlled classroom case. This separates a mathematical exercise from a causal scientific finding.

### From the process to an experiment

Arrange an eight-class testcross dataset, confirm the phase of the parental heterozygote, designate two rare reciprocal classes, and recompute interval distances with double crossovers counted in each appropriate segment. Specify an independent biological unit of replication. Those are different controls and answer different questions.

For **three-point linkage order**, interpretation should follow the biology of the observation, not merely whether a significance threshold was crossed.

### Interpretations worth separating

If offspring viability differs systematically by genotype, frequency alone may misidentify the parental or double-recombinant classes.

Compare the focal mechanism with **marker association and ld**, using the dedicated topic section rather than assuming these labels describe the same process. The comparison is not evidence that one causes the other. It is a deliberate stress test for the student's categories. State explicitly when none of these strategies is feasible.

### Annotated investigation notebook

Start a new notebook entry titled *Three-point linkage order: prior expectation, actual measurement, alternate mechanism*. Record the outcome before labeling it a confirmation or discrepancy.

For the next pass, consider the topic **lod linkage evidence**. Review its own mechanistic discussion before assuming a relationship. Ask whether it changes the apparent prediction for **three-point linkage order**, changes only what is measured, or concerns a different scientific level entirely.

### A second, more demanding application

The memo must discuss **three-point linkage order** using this design constraint: Arrange an eight-class testcross dataset, confirm the phase of the parental heterozygote, designate two rare reciprocal classes, and recompute interval distances with double crossovers counted in each appropriate segment. What would a null result say about assay power?

The main limitation for this subsection is not decorative fine print: If offspring viability differs systematically by genotype, frequency alone may misidentify the parental or double-recombinant classes.

### Connection to the next course topic

A later unit investigates **gene regulation and alleles**, whose underlying level of analysis should be inspected in that section.

## 3.3 Marker association and LD

### Mechanistic foundation: Marker association and LD

Linkage disequilibrium measures nonrandom association of alleles across loci in a population. It is not the same as physical linkage in an individual meiosis. Haplotype frequencies reflect demography, recombination, selection, ancestry structure and sampling. The commonly used D measure compares observed haplotype frequency with the product of marginal allele frequencies; r-squared standardizes squared association and is relevant to tagging performance. Genotype association alone does not specify the causal variant.

For **marker association and ld**, a model written without its inheritance assumptions is not a complete explanation.

### A quantitative example with a defined denominator

If p(A)=0.4, p(B)=0.3, and p(AB)=0.18, then D=0.18−0.12=0.06.

Read the example in two passes. First solve the arithmetic as a hypothetical well-controlled classroom case. This separates a mathematical exercise from a causal scientific finding.

### From the process to an experiment

Phase haplotypes in synthetic reference panels, compare stratified population groups, and examine how a change in allele frequencies alters D and r-squared even with the same underlying physical distance. Specify an independent biological unit of replication. Those are different controls and answer different questions.

For **marker association and ld**, interpretation should follow the biology of the observation, not merely whether a significance threshold was crossed.

### Interpretations worth separating

A significant association marker may be a proxy for a nearby causal locus or for ancestry-related confounding.

Compare the focal mechanism with **lod linkage evidence**, using the dedicated topic section rather than assuming these labels describe the same process. The comparison is not evidence that one causes the other. It is a deliberate stress test for the student's categories. State explicitly when none of these strategies is feasible.

### Annotated investigation notebook

Start a new notebook entry titled *Marker association and LD: prior expectation, actual measurement, alternate mechanism*. Record the outcome before labeling it a confirmation or discrepancy.

For the next pass, consider the topic **recombination fraction**. Review its own mechanistic discussion before assuming a relationship. Ask whether it changes the apparent prediction for **marker association and ld**, changes only what is measured, or concerns a different scientific level entirely.

### A second, more demanding application

The memo must discuss **marker association and ld** using this design constraint: Phase haplotypes in synthetic reference panels, compare stratified population groups, and examine how a change in allele frequencies alters D and r-squared even with the same underlying physical distance. What would a null result say about assay power?

The main limitation for this subsection is not decorative fine print: A significant association marker may be a proxy for a nearby causal locus or for ancestry-related confounding.

### Connection to the next course topic

A later unit investigates **functional perturbation**, whose underlying level of analysis should be inspected in that section.

## 3.4 LOD linkage evidence

### Mechanistic foundation: LOD linkage evidence

A two-point LOD score compares the likelihood of pedigree genotypes under recombination fraction theta with that under theta=0.5. The logarithm is base ten, so LOD=3 represents a thousand-fold likelihood ratio for the specified evidence model, not a posterior probability of 99.9 percent. Genotyping errors, incomplete penetrance, pedigree misspecification and ascertainment affect the evidence. Multiple family scores can add if the families and modeled data are conditionally independent.

For **lod linkage evidence**, a model written without its inheritance assumptions is not a complete explanation.

### A quantitative example with a defined denominator

For 20 nonrecombinants and 2 recombinants, theta_hat=2/22; the LOD curve can be compared to its reference at theta=0.5.

Read the example in two passes. First solve the arithmetic as a hypothetical well-controlled classroom case. This separates a mathematical exercise from a causal scientific finding.

### From the process to an experiment

For an intentionally simple phase-known meiosis model, calculate LOD(theta) from recombinant and nonrecombinant counts; compare the shape to a direct grid search and verify maxima numerically. Specify an independent biological unit of replication. Those are different controls and answer different questions.

For **lod linkage evidence**, interpretation should follow the biology of the observation, not merely whether a significance threshold was crossed.

### Interpretations worth separating

A preferred theta is not a guaranteed disease-gene position; a full pedigree analysis needs family structure and penetrance likelihoods.

Compare the focal mechanism with **recombination fraction**, using the dedicated topic section rather than assuming these labels describe the same process. The comparison is not evidence that one causes the other. It is a deliberate stress test for the student's categories. State explicitly when none of these strategies is feasible.

### Annotated investigation notebook

Start a new notebook entry titled *LOD linkage evidence: prior expectation, actual measurement, alternate mechanism*. Record the outcome before labeling it a confirmation or discrepancy.

For the next pass, consider the topic **three-point linkage order**. Review its own mechanistic discussion before assuming a relationship. Ask whether it changes the apparent prediction for **lod linkage evidence**, changes only what is measured, or concerns a different scientific level entirely.

### A second, more demanding application

The memo must discuss **lod linkage evidence** using this design constraint: For an intentionally simple phase-known meiosis model, calculate LOD(theta) from recombinant and nonrecombinant counts; compare the shape to a direct grid search and verify maxima numerically. What would a null result say about assay power?

The main limitation for this subsection is not decorative fine print: A preferred theta is not a guaranteed disease-gene position; a full pedigree analysis needs family structure and penetrance likelihoods.

### Connection to the next course topic

A later unit investigates **mutation and sequence variation**, whose underlying level of analysis should be inspected in that section.

## Advanced studio: what genetic maps actually measure

### A recombination fraction is a gamete-level probability

Two loci on one chromosome can be joined on the same physical DNA molecule without staying joined in every offspring. Crossing over during meiosis can exchange material between homologous nonsister chromatids. In a phase-known double heterozygote AB/ab, gametes AB and ab are parental with respect to those loci; Ab and aB are recombinant. Under a symmetrical idealization and total recombinant fraction r, the four gamete probabilities are (1−r)/2, (1−r)/2, r/2 and r/2. A testcross with ab/ab reveals them directly in offspring genotypes if classification and viability are unbiased. This structure explains why recombinant counts are divided by all informative progeny and why the estimated fraction is bounded by one half.

A physical distance might be represented in base pairs or megabases. A genetic map distance uses a mathematical relationship to recombination; in short intervals, 1% recombinant offspring is approximated by one centimorgan. Long intervals are different because two crossing-over events between the same outside markers can restore a parental outer-marker pattern. As a result, long physical spans can show r approaching one half even when many crossovers occur. A mapping function introduces assumptions about the distribution of crossovers and interference. Under Haldane's no-interference Poisson approximation, map distance in morgans is −(1/2)ln(1−2r). At r=0.1, this corresponds to about 0.1116 morgans, or 11.16 cM, not exactly 10 cM. Near r=0.5, the transform diverges and inference becomes unstable.

### Three-point mapping resolves hidden events

Three linked marker loci can reveal double exchanges that a pair of outside markers misses. Imagine a phase-known parental chromosome with allele sequence A B C and the homolog with a b c. In a three-point testcross, the most numerous reciprocal classes are often the two parental combinations. The two rarest reciprocal classes are candidate double crossovers, but this classification is reliable only under assumptions about fitness and ascertainment. Compare each rare class with the parental types; the locus whose state alone appears switched relative to the relevant parental pattern is the middle marker in the classical analysis. The double crossover is then counted toward recombination in each of the two adjacent intervals. It is easy to omit it twice when reasoning only from external marker patterns.

In an illustrative dataset of one thousand offspring, suppose the A–B interval includes sixty-four recombinant classes and the B–C interval contains thirty-six, both after appropriate inclusion of double crossovers. The short-interval estimates are 6.4 cM and 3.6 cM. The sum is ten cM for the three-marker map segment. It would be wrong to claim that the physical DNA length is ten million base pairs; a megabase-to-centimorgan conversion depends on local recombination landscape, sex, organism and chromosome region. Small datasets also make uncertainty important: an estimate of one recombinant in one hundred informative meioses is particularly sensitive to a single classification error.

### A linkage LOD score is a likelihood ratio

Pedigree linkage calculations compare different recombination hypotheses rather than diagnosing a disease by arithmetic alone. For a highly simplified set of twenty-two phase-known independent informative meioses with twenty nonrecombinants and two recombinants, likelihood at theta is proportional to (1−theta)^20 theta². The unlinked hypothesis has theta=0.5. Hence LOD(theta)=20log10[(1−theta)/0.5]+2log10[theta/0.5]. At theta=0.1, this value is about 3.7075. A large score favors linkage under the specified model, but a likelihood ratio is not automatically a posterior disease probability; priors and potential model misspecification matter. A real extended pedigree is a dependence structure, not twenty-two randomly generated independent indicator variables unless a careful conditional argument makes that reduction valid.

Association mapping across unrelated individuals answers a different question. Linkage disequilibrium D compares observed haplotype probability P(AB) to p_A p_B. If p_A=0.4, p_B=0.3 and P(AB)=0.18, then D=0.06. The same D can have different standardized strength depending on allele frequencies, so r-squared or related measures can be more useful when describing marker tagging. Population admixture, selection, demographic events and assortative sampling can generate associations that do not indicate a nearby functional interaction. A marker may be statistically associated because it tags another locus; functional validation is still required.

### Comparing methods as a research decision

Choose testcross mapping when controlled crosses and interpretable gamete phases are available. Choose family linkage when relatives provide segregation information. Choose association mapping when a suitable population sample and robust confounder control exist. Choose physical mapping when the question concerns genomic coordinates, breakpoints or sequence architecture. These methods cannot be substituted solely because all produce a position-like output. The reporting checklist should state study unit, phase evidence, allele frequencies, genotyping error rate, sample exclusion rules, uncertainty interval, and the biological claim that the estimate actually supports. If a map interval is wide, the appropriate conclusion is a region of interest, not a uniquely identified causal gene.

## Further conceptual check: why mapping functions differ

The Haldane and Kosambi mapping functions are alternatives that convert observed two-marker recombination fraction into an inferred genetic distance under different assumptions about crossover interference. Haldane uses d=−0.5ln(1−2r) in morgans and treats crossovers as following a Poisson process without interference. Kosambi gives d=0.25ln[(1+2r)/(1−2r)], using a different interference model. For r=0.1, Haldane yields approximately 0.1116 morgans and Kosambi about 0.1014. Neither function is a universal law across all organisms and chromosome regions. A student should always name the chosen transform and report the underlying observed fraction.

A mapping workflow must also distinguish count uncertainty from mapping-function assumptions. Ten recombinant progeny among one hundred define a point estimate of r=0.1 with substantial binomial uncertainty; applying a logarithmic function does not remove that uncertainty. Near r=0.5 both transforms become unstable or divergent. Repeating the experiment with closer markers, more informative meioses or additional physical sequence evidence can improve interpretation, whereas quoting extra decimal places cannot. This is a practical example of how an algebraically exact formula may still yield a scientifically imprecise result.

## Integrated Genetics Laboratory 3: Gene mapping

This laboratory is a written and computational design exercise. The first case involves **recombination fraction**: With 92 recombinants among 800 informative meioses, r=0.115. For short intervals this approximates 11.5 cM. The second involves **three-point linkage order**: For adjacent interval counts of 64 and 36 recombinant meioses among 1000 offspring, respective estimates are 6.4 cM and 3.6 cM; the outer interval requires a double-crossover correction. Treat both as mathematical thought experiments with supplied assumptions.

**Protocol design.** Begin by enumerating possible states without scoring phenotypes. Include one independent validation of the genotype or marker state. The rationale for the first experiment is Create a four-column haplotype count table and have two blinded analysts assign parental versus recombinant status. Quantify uncertainty using binomial or likelihood methods. A competing observation strategy involves Arrange an eight-class testcross dataset, confirm the phase of the parental heterozygote, designate two rare reciprocal classes, and recompute interval distances with double crossovers counted in each appropriate segment. These need not have the same denominator or uncertainty model.

Then compare the inference to **marker association and ld**. Its mechanism is: Linkage disequilibrium measures nonrandom association of alleles across loci in a population. Haplotype frequencies reflect demography, recombination, selection, ancestry structure and sampling. Genotype association alone does not specify the causal variant.

It includes the caveat for **lod linkage evidence**: A preferred theta is not a guaranteed disease-gene position; a full pedigree analysis needs family structure and penetrance likelihoods. For a population-frequency estimate include the time and sampling frame. For a family inference specify the selection rule for included pedigrees.

**Ethical and reproducibility note.** Use synthetic or appropriately consented data only. Share versioned simulation settings and code, not identifying family genomic records.

## Fully worked questions

All examples below are hypothetical and contain the necessary model assumptions. Solutions are provided to make reasoning inspectable rather than turning a genetics inference into a memorized ratio.

### Problem 1: Pairwise recombination

Out of 800 informative offspring, 92 are recombinant for a locus pair. Find r and short-interval centimorgan distance.

**Worked solution**

1. Count r as 92 recombinant offspring divided by 800 informative total.
2. Thus r=0.115 and the short-interval approximation is 100r=11.5 cM.
3. This is not 11.5 megabases; physical distance requires sequence mapping and crossover-rate information.

### Problem 2: Linkage disequilibrium

Given P(A)=0.4, P(B)=0.3 and haplotype P(AB)=0.18, compute LD coefficient D.

**Worked solution**

1. The independence expectation for AB is P(A)P(B)=0.4×0.3=0.12.
2. D is the observed AB probability minus that independence baseline.
3. D=0.18−0.12=0.06. A different population’s allele frequencies can change D even for the same physical marker pair.

### Problem 3: Evidence against unlinked model

In 22 independent phase-known informative meioses, 20 are nonrecombinant and two recombinant. Evaluate a simplified LOD at theta=0.1.

**Worked solution**

1. The likelihood at theta is proportional to (1−theta)^20 theta^2, with the unlinked reference using 0.5 for both class probabilities.
2. Take base-ten logarithms of the ratio: LOD=20 log10(0.9/0.5)+2 log10(0.1/0.5).
3. Using log10(1.8)=0.25527 and log10(0.2)=−0.69897 gives LOD≈3.7075. The model omits pedigree complexities and errors.

## Interactive genetics investigation

These interactive models are explicitly simplified quantitative thought experiments. Use the sliders to change one assumption at a time, inspect the curve or categorical display, check a limiting case, and reset to the baseline. A classroom model is not a clinical test or a measured population estimate.

### Model: map

The map model provides a numerical expectation or uncertainty-dependent outcome associated with Unit 3. Copy the default readout, alter the first parameter, and predict whether the result should rise, fall or be nonmonotonic. Change the second parameter and identify which part of the equation it modifies. Return to the starting settings and check that the original value is restored. State whether the plotted quantity represents a probability, an expectation, a standardized statistic, or a physical copy count.

Model interpretation should refer back to the underlying derivation and the experimental denominators in this chapter. Do not extrapolate beyond the allowed slider range, and do not describe a smooth curve as data from an observed population. If the model rejects an impossible parameter combination, explain the rejected biological assumption in words rather than simply resetting the input.

### Model: lod

The lod model provides a numerical expectation or uncertainty-dependent outcome associated with Unit 3. Copy the default readout, alter the first parameter, and predict whether the result should rise, fall or be nonmonotonic. Change the second parameter and identify which part of the equation it modifies. Return to the starting settings and check that the original value is restored. State whether the plotted quantity represents a probability, an expectation, a standardized statistic, or a physical copy count.

Model interpretation should refer back to the underlying derivation and the experimental denominators in this chapter. Do not extrapolate beyond the allowed slider range, and do not describe a smooth curve as data from an observed population. If the model rejects an impossible parameter combination, explain the rejected biological assumption in words rather than simply resetting the input.
