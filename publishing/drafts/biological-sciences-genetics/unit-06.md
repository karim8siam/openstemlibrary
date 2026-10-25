# Unit 6: Population genetics

## Unit overview

Population genetics follows alleles through generations while keeping gene copies, individuals and sampling frames distinct. Hardy–Weinberg equilibrium provides a useful null model under specified assumptions. Drift, selection and migration offer alternative mechanisms of change; an observed trajectory rarely identifies one cause uniquely. Numerical models demonstrate expected values and sampling variance while emphasizing that a real natural population can violate several idealizations simultaneously.

## Learning goals

Explain mechanisms without conflating genotype, molecular state and observable phenotype; formulate explicit conditional probabilities; solve distinct numerical examples with appropriate denominators; evaluate experimental controls; challenge an alternative interpretation; and inspect the assumptions behind each interactive model.

## 6.1 Allele frequencies

### Mechanistic foundation: Allele frequencies

For a diploid biallelic locus, allele frequency is counted from chromosomes: p=(2nAA+nAa)/(2N) and q=1−p. A frequency is defined for a particular population, locus, time and sampling scheme. Heterozygosity, genotype frequencies and allele frequencies are related but not interchangeable. Frequency estimation can be distorted by genotyping error, nonrandom sampling and copy-number variation.

For **allele frequencies**, a model written without its inheritance assumptions is not a complete explanation.

### A quantitative example with a defined denominator

From 35 AA, 50 Aa and 15 aa genotypes, p=(70+50)/200=0.60 and q=0.40.

Read the example in two passes. First solve the arithmetic as a hypothetical well-controlled classroom case. This separates a mathematical exercise from a causal scientific finding.

### From the process to an experiment

Count genotype calls from a representative sample, apply call-rate quality controls and derive confidence bounds that reflect both binomial sampling and population structure. Specify an independent biological unit of replication. Those are different controls and answer different questions.

For **allele frequencies**, interpretation should follow the biology of the observation, not merely whether a significance threshold was crossed.

### Interpretations worth separating

Computing an allele frequency from a clinically ascertained set does not automatically estimate frequency in the general population.

Compare the focal mechanism with **hardy–weinberg model**, using the dedicated topic section rather than assuming these labels describe the same process. The comparison is not evidence that one causes the other. It is a deliberate stress test for the student's categories. State explicitly when none of these strategies is feasible.

### Annotated investigation notebook

Start a new notebook entry titled *Allele frequencies: prior expectation, actual measurement, alternate mechanism*. Record the outcome before labeling it a confirmation or discrepancy.

For the next pass, consider the topic **genetic drift**. Review its own mechanistic discussion before assuming a relationship. Ask whether it changes the apparent prediction for **allele frequencies**, changes only what is measured, or concerns a different scientific level entirely.

### A second, more demanding application

The memo must discuss **allele frequencies** using this design constraint: Count genotype calls from a representative sample, apply call-rate quality controls and derive confidence bounds that reflect both binomial sampling and population structure. What would a null result say about assay power?

The main limitation for this subsection is not decorative fine print: Computing an allele frequency from a clinically ascertained set does not automatically estimate frequency in the general population.

### Connection to the next course topic

A later unit investigates **penetrance and expressivity**, whose underlying level of analysis should be inspected in that section.

## 6.2 Hardy–Weinberg model

### Mechanistic foundation: Hardy–Weinberg model

In an idealized randomly mating diploid population with suitable assumptions, one generation of random union of gametes gives genotype proportions p², 2pq and q². These form an equilibrium reference, not a claim that natural populations meet every assumption. Observed deviations can reflect inbreeding, selection, population structure, errors or nonrandom mating; no single departure uniquely identifies a cause. Allele frequency remains unchanged under random mating alone.

For **hardy–weinberg model**, a model written without its inheritance assumptions is not a complete explanation.

### A quantitative example with a defined denominator

For p=0.6 and q=0.4, expected AA=0.36, Aa=0.48 and aa=0.16.

Read the example in two passes. First solve the arithmetic as a hypothetical well-controlled classroom case. This separates a mathematical exercise from a causal scientific finding.

### From the process to an experiment

Precompute expected genotype counts from a sample-specific p, examine whether expected counts are adequate for the selected test, and evaluate a stratified analysis before interpreting a pooled deviation. Specify an independent biological unit of replication. Those are different controls and answer different questions.

For **hardy–weinberg model**, interpretation should follow the biology of the observation, not merely whether a significance threshold was crossed.

### Interpretations worth separating

A failure to reject an equilibrium test does not prove absence of selection or error; low statistical power may mask deviations.

Compare the focal mechanism with **genetic drift**, using the dedicated topic section rather than assuming these labels describe the same process. The comparison is not evidence that one causes the other. It is a deliberate stress test for the student's categories. State explicitly when none of these strategies is feasible.

### Annotated investigation notebook

Start a new notebook entry titled *Hardy–Weinberg model: prior expectation, actual measurement, alternate mechanism*. Record the outcome before labeling it a confirmation or discrepancy.

For the next pass, consider the topic **migration and selection**. Review its own mechanistic discussion before assuming a relationship. Ask whether it changes the apparent prediction for **hardy–weinberg model**, changes only what is measured, or concerns a different scientific level entirely.

### A second, more demanding application

The memo must discuss **hardy–weinberg model** using this design constraint: Precompute expected genotype counts from a sample-specific p, examine whether expected counts are adequate for the selected test, and evaluate a stratified analysis before interpreting a pooled deviation. What would a null result say about assay power?

The main limitation for this subsection is not decorative fine print: A failure to reject an equilibrium test does not prove absence of selection or error; low statistical power may mask deviations.

### Connection to the next course topic

A later unit investigates **polygenic traits and prediction**, whose underlying level of analysis should be inspected in that section.

## 6.3 Genetic drift

### Mechanistic foundation: Genetic drift

Drift is random change in allele frequencies caused by finite sampling of gametes and offspring. In an idealized Wright–Fisher diploid population, the next generation draws 2Ne allele copies binomially from the current p. The conditional expectation stays p, while variance of the next-generation frequency is p(1−p)/(2Ne). Small effective size causes stronger fluctuations, faster loss of variation and higher chance of eventual fixation or loss. Effective size may differ substantially from census size.

For **genetic drift**, a model written without its inheritance assumptions is not a complete explanation.

### A quantitative example with a defined denominator

For p=0.5 and Ne=100, one-generation variance in p is 0.25/200=0.00125, and standard deviation is about 0.0354.

Read the example in two passes. First solve the arithmetic as a hypothetical well-controlled classroom case. This separates a mathematical exercise from a causal scientific finding.

### From the process to an experiment

Simulate many replicate populations at different effective sizes with independent random seeds and plot trajectories plus quantile bands; compare empirical variance at one generation with the binomial prediction. Specify an independent biological unit of replication. Those are different controls and answer different questions.

For **genetic drift**, interpretation should follow the biology of the observation, not merely whether a significance threshold was crossed.

### Interpretations worth separating

A single drifting trajectory that rises is not evidence of positive selection; replicate distributions and external fitness evidence matter.

Compare the focal mechanism with **migration and selection**, using the dedicated topic section rather than assuming these labels describe the same process. The comparison is not evidence that one causes the other. It is a deliberate stress test for the student's categories. State explicitly when none of these strategies is feasible.

### Annotated investigation notebook

Start a new notebook entry titled *Genetic drift: prior expectation, actual measurement, alternate mechanism*. Record the outcome before labeling it a confirmation or discrepancy.

For the next pass, consider the topic **allele frequencies**. Review its own mechanistic discussion before assuming a relationship. Ask whether it changes the apparent prediction for **genetic drift**, changes only what is measured, or concerns a different scientific level entirely.

### A second, more demanding application

The memo must discuss **genetic drift** using this design constraint: Simulate many replicate populations at different effective sizes with independent random seeds and plot trajectories plus quantile bands; compare empirical variance at one generation with the binomial prediction. What would a null result say about assay power?

The main limitation for this subsection is not decorative fine print: A single drifting trajectory that rises is not evidence of positive selection; replicate distributions and external fitness evidence matter.

### Connection to the next course topic

A later unit investigates **gene–environment interaction**, whose underlying level of analysis should be inspected in that section.

## 6.4 Migration and selection

### Mechanistic foundation: Migration and selection

Gene flow transports alleles between populations and can oppose drift or local adaptation. In a simple mixing model, destination frequency after migration is (1−m)p_local+mp_source. Selection changes relative contributions of genotypes to the next generation, often modeled with weighted genotype fitnesses. Both processes can operate simultaneously, while the order of migration, selection and reproduction changes the resulting recursion.

For **migration and selection**, a model written without its inheritance assumptions is not a complete explanation.

### A quantitative example with a defined denominator

At p_local=0.2, p_source=0.8 and m=0.1, the postmixing p is 0.26.

Read the example in two passes. First solve the arithmetic as a hypothetical well-controlled classroom case. This separates a mathematical exercise from a causal scientific finding.

### From the process to an experiment

Use time-series allele-frequency data from matched sampling sites, model migration separately from local fitness and test sensitivity to unsampled source populations. Specify an independent biological unit of replication. Those are different controls and answer different questions.

For **migration and selection**, interpretation should follow the biology of the observation, not merely whether a significance threshold was crossed.

### Interpretations worth separating

A temporal allele-frequency change does not by itself identify migration or selection; genetic drift and ascertainment can mimic it.

Compare the focal mechanism with **allele frequencies**, using the dedicated topic section rather than assuming these labels describe the same process. The comparison is not evidence that one causes the other. It is a deliberate stress test for the student's categories. State explicitly when none of these strategies is feasible.

### Annotated investigation notebook

Start a new notebook entry titled *Migration and selection: prior expectation, actual measurement, alternate mechanism*. Record the outcome before labeling it a confirmation or discrepancy.

For the next pass, consider the topic **hardy–weinberg model**. Review its own mechanistic discussion before assuming a relationship. Ask whether it changes the apparent prediction for **migration and selection**, changes only what is measured, or concerns a different scientific level entirely.

### A second, more demanding application

The memo must discuss **migration and selection** using this design constraint: Use time-series allele-frequency data from matched sampling sites, model migration separately from local fitness and test sensitivity to unsampled source populations. What would a null result say about assay power?

The main limitation for this subsection is not decorative fine print: A temporal allele-frequency change does not by itself identify migration or selection; genetic drift and ascertainment can mimic it.

### Connection to the next course topic

A later unit investigates **epistasis and interaction**, whose underlying level of analysis should be inspected in that section.

## Advanced studio: connecting equilibrium, drift and migration

### Counting gene copies before inferring processes

For an autosomal diploid locus in N individuals, there are normally 2N allele copies. If thirty-five individuals are AA, fifty are Aa and fifteen are aa, the sample size is one hundred and there are two hundred allele copies. The count of A alleles is seventy from AA individuals plus fifty from heterozygotes, giving p=120/200=0.6. This frequency cannot be determined by counting only individuals with the dominant phenotype unless the genotype–phenotype model supplies enough additional information. If missing genotypes or copy-number changes occur, the denominator requires adjustment and the missingness mechanism may matter.

Hardy–Weinberg proportions follow from a simple probabilistic operation: gametes with A frequency p and a frequency q=1−p combine at random. Multiplying gamete probabilities produces AA at p², Aa at pq+qp=2pq, and aa at q². For p=0.6, the values are 0.36, 0.48 and 0.16. An illustrative population of two hundred individuals would have expected counts 72, 96 and 32. These counts are not an observed census, and estimating p from the same small sample creates dependencies in some statistical tests. One cannot infer perfect random mating merely because the observed table looks close to expectation; multiple mechanisms may balance or sampling variation may hide departures.

### Drift as a generational sampling operation

In a diploid Wright–Fisher idealization, the next generation has 2Ne copies sampled from a binomial distribution with success probability p. Its expected allele frequency remains p, but the realized value is random. Conditional variance is p(1−p)/(2Ne). At p=0.5 and Ne=100 the variance is 0.00125 and standard deviation approximately 0.03536 after one modeled generation. A simulated increase from 0.5 to 0.56 in one replicate cannot by itself demonstrate selection, even though 0.56 may feel like directional progress. Compare many independent replicate populations with the same starting p to the expected drift distribution.

Repeated drift can push alleles toward loss or fixation. These absorbing boundaries change long-run distributions, so a normal approximation valid over a short interval may be poor near p=0 or p=1. Variance accumulates and surviving polymorphic trajectories become a selected subset. Moreover, effective population size is a summary of reproductive variance and demographic history, not simply the number of bodies counted in a survey. A colony of one thousand organisms with extreme inequality in reproductive contributions can have a far smaller effective population size than one thousand. Simulation controls should therefore label Ne as effective size, not census population.

### Migration and selection are distinguishable mechanisms

A simple migration step mixes a local allele frequency pL and a source frequency pS with migration fraction m: p_new=(1−m)pL+mpS. For pL=0.2, pS=0.8 and m=0.1, the result is 0.26. This deterministic calculation says what an ideal mixing event would do; it does not establish that observed change of 0.06 was actually caused by migration. Sampling drift or differential survival could change frequency similarly. Geographic population labels may also conceal substructure, changing the interpretation of pooled estimates.

Selection is instead represented through differences in expected reproductive contribution. For genotype fitness weights wAA, wAa and waa, start from preselection genotype frequencies, multiply each class by its weight, sum to obtain mean fitness and normalize. The resulting genotype contributions then determine the allele frequency after selection. Such a model is sensitive to dominance, mating pattern and life-cycle ordering. Applying migration before selection can produce a different single-generation recursion from applying selection before migration. A responsible simulation declares that order rather than presenting an unqualified trajectory.

### A multiprocess inference exercise

Imagine two neighboring populations sampled at three times with allele-frequency estimates 0.20, 0.26 and 0.29 in one location. The source population is believed to remain near 0.8. Several plausible models fit an increase: migration at changing rates, positive selection at the focal locus, drift in a small effective population, or genotyping error correlated with the sampling year. A defensible investigation would collect neutral reference markers, effective-size estimates and ecological information about movement while checking whether sampling sites and sequencing procedures changed over time. Replicate loci can help distinguish genome-wide demographic effects from highly locus-specific deviations, but none of those comparisons removes every confounder.

The conclusion should distinguish deterministic model expectations from stochastic realizations, report confidence intervals, and describe alternative mechanisms. An equilibrium deviation, a shift in allele frequency, or a high differentiation estimate is an observation to explain, not a mechanistic diagnosis by itself. Population genetics teaches how to connect gene-copy arithmetic to evolutionary hypotheses without mistaking a tidy formula for evidence that only one force acted.

## Further conceptual check: inbreeding and population mixture

Hardy–Weinberg proportions describe the consequence of random mating under specified assumptions, not the only possible organization of genotypes at a given allele frequency. An inbreeding coefficient F is often used in a simple model to write expected heterozygote frequency as 2pq(1−F), with corresponding increases in homozygote fractions. This is a parameterization of genotype correlation relative to an equilibrium baseline and should not be confused with the probability that two specific people are relatives. Changing population mixture can also produce a heterozygote deficit: separately random-mating groups with different allele frequencies may have fewer pooled heterozygotes than predicted from the pooled average. This is a form of the Wahlund effect.

For a toy mixture, take equal numbers from populations with allele-A frequencies 0.2 and 0.8. Each group has equilibrium heterozygosity 2×0.2×0.8=0.32; the pooled allele frequency is 0.5, whose equilibrium expectation would be 0.5. The observed pooled heterozygosity expected from within-group mating remains 0.32, giving a deficit without requiring inbreeding within either group. A genetics analysis should first investigate population sampling and stratification before assigning one mechanism to such a departure.

## Integrated Genetics Laboratory 6: Population genetics

This laboratory is a written and computational design exercise. The first case involves **allele frequencies**: From 35 AA, 50 Aa and 15 aa genotypes, p=(70+50)/200=0.60 and q=0.40. The second involves **hardy–weinberg model**: For p=0.6 and q=0.4, expected AA=0.36, Aa=0.48 and aa=0.16. Treat both as mathematical thought experiments with supplied assumptions.

**Protocol design.** Begin by enumerating possible states without scoring phenotypes. Include one independent validation of the genotype or marker state. The rationale for the first experiment is Count genotype calls from a representative sample, apply call-rate quality controls and derive confidence bounds that reflect both binomial sampling and population structure. A competing observation strategy involves Precompute expected genotype counts from a sample-specific p, examine whether expected counts are adequate for the selected test, and evaluate a stratified analysis before interpreting a pooled deviation. These need not have the same denominator or uncertainty model.

Then compare the inference to **genetic drift**. Its mechanism is: Drift is random change in allele frequencies caused by finite sampling of gametes and offspring. Effective size may differ substantially from census size.

It includes the caveat for **migration and selection**: A temporal allele-frequency change does not by itself identify migration or selection; genetic drift and ascertainment can mimic it. For a population-frequency estimate include the time and sampling frame. For a family inference specify the selection rule for included pedigrees.

**Ethical and reproducibility note.** Use synthetic or appropriately consented data only. Share versioned simulation settings and code, not identifying family genomic records.

## Fully worked questions

All examples below are hypothetical and contain the necessary model assumptions. Solutions are provided to make reasoning inspectable rather than turning a genetics inference into a memorized ratio.

### Problem 1: Allele copy counting

A sample has 35 AA, 50 Aa and 15 aa diploid individuals. Calculate allele-A frequency.

**Worked solution**

1. There are 100 individuals and therefore 200 allele copies at an ordinary autosomal diploid locus.
2. Count A copies: 2×35+50=120.
3. Frequency p=120/200=0.60 and q=0.40. Calling only AA organisms would omit A carried by heterozygotes.

### Problem 2: Equilibrium expectation

For p=0.6 in a randomly mating idealized model and N=200 diploid individuals, find expected genotype counts.

**Worked solution**

1. Set q=1−p=0.4. Idealized genotype frequencies are p²=0.36, 2pq=0.48 and q²=0.16.
2. Multiply each by 200 to get 72 AA, 96 Aa and 32 aa expected individuals.
3. These are theoretical expectations and need not match the genotypes in the sample used to estimate p.

### Problem 3: One-generation drift

In a Wright–Fisher model with p=0.5 and effective population size Ne=100, compute one-generation allele-frequency variance.

**Worked solution**

1. For a diploid idealized population, Var(p_next|p)=p(1−p)/(2Ne).
2. The numerator is 0.25 and denominator 200, so variance=0.00125.
3. The square root is approximately 0.03536. This dispersion arises from sampling rather than a directional fitness effect.

## Interactive genetics investigation

These interactive models are explicitly simplified quantitative thought experiments. Use the sliders to change one assumption at a time, inspect the curve or categorical display, check a limiting case, and reset to the baseline. A classroom model is not a clinical test or a measured population estimate.

### Model: hardy

The hardy model provides a numerical expectation or uncertainty-dependent outcome associated with Unit 6. Copy the default readout, alter the first parameter, and predict whether the result should rise, fall or be nonmonotonic. Change the second parameter and identify which part of the equation it modifies. Return to the starting settings and check that the original value is restored. State whether the plotted quantity represents a probability, an expectation, a standardized statistic, or a physical copy count.

Model interpretation should refer back to the underlying derivation and the experimental denominators in this chapter. Do not extrapolate beyond the allowed slider range, and do not describe a smooth curve as data from an observed population. If the model rejects an impossible parameter combination, explain the rejected biological assumption in words rather than simply resetting the input.

### Model: migration

The migration model provides a numerical expectation or uncertainty-dependent outcome associated with Unit 6. Copy the default readout, alter the first parameter, and predict whether the result should rise, fall or be nonmonotonic. Change the second parameter and identify which part of the equation it modifies. Return to the starting settings and check that the original value is restored. State whether the plotted quantity represents a probability, an expectation, a standardized statistic, or a physical copy count.

Model interpretation should refer back to the underlying derivation and the experimental denominators in this chapter. Do not extrapolate beyond the allowed slider range, and do not describe a smooth curve as data from an observed population. If the model rejects an impossible parameter combination, explain the rejected biological assumption in words rather than simply resetting the input.
