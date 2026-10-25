# Unit 5: Quantitative genetics

## Unit overview

Quantitative genetics shifts from discrete genotype categories to distributions of measured traits. Variance components and heritability depend on the study population, environment and scale; these are estimates with uncertainty, not immutable facts about individuals. Selection-response equations are powerful but conditional. This unit connects a trait’s distribution with the experimental and statistical design needed to infer inherited change, while avoiding the common error of treating high heritability as proof that environmental intervention cannot matter.

## Learning goals

Explain mechanisms without conflating genotype, molecular state and observable phenotype; formulate explicit conditional probabilities; solve distinct numerical examples with appropriate denominators; evaluate experimental controls; challenge an alternative interpretation; and inspect the assumptions behind each interactive model.

## 5.1 Continuous traits

### Mechanistic foundation: Continuous traits

Height, yield, stress tolerance and many behavioral phenotypes vary continuously because multiple genetic and environmental processes contribute. A distribution of observed trait values is not itself proof that infinitely many loci are involved: measurement noise, developmental state and finite loci with complex interactions can produce similar shapes. A quantitative study specifies the population, trait scale, environment, developmental stage and sampling design before attributing observed variance to genotype.

For **continuous traits**, a model written without its inheritance assumptions is not a complete explanation.

### A quantitative example with a defined denominator

For trait values 10, 12, 14 and 16, the population mean is 13 and population variance is 5 in squared trait units.

Read the example in two passes. First solve the arithmetic as a hypothetical well-controlled classroom case. This separates a mathematical exercise from a causal scientific finding.

### From the process to an experiment

Record a quantitative plant trait across replicated environments with randomized blocks, repeated calibration measurements and known relatedness. Inspect residual distributions before fitting a genetic model. Specify an independent biological unit of replication. Those are different controls and answer different questions.

For **continuous traits**, interpretation should follow the biology of the observation, not merely whether a significance threshold was crossed.

### Interpretations worth separating

An observed bell-shaped histogram does not establish a purely additive polygenic mechanism.

Compare the focal mechanism with **variance and heritability**, using the dedicated topic section rather than assuming these labels describe the same process. The comparison is not evidence that one causes the other. It is a deliberate stress test for the student's categories. State explicitly when none of these strategies is feasible.

### Annotated investigation notebook

Start a new notebook entry titled *Continuous traits: prior expectation, actual measurement, alternate mechanism*. Record the outcome before labeling it a confirmation or discrepancy.

For the next pass, consider the topic **selection response**. Review its own mechanistic discussion before assuming a relationship. Ask whether it changes the apparent prediction for **continuous traits**, changes only what is measured, or concerns a different scientific level entirely.

### A second, more demanding application

The memo must discuss **continuous traits** using this design constraint: Record a quantitative plant trait across replicated environments with randomized blocks, repeated calibration measurements and known relatedness. Inspect residual distributions before fitting a genetic model. What would a null result say about assay power?

The main limitation for this subsection is not decorative fine print: An observed bell-shaped histogram does not establish a purely additive polygenic mechanism.

### Connection to the next course topic

A later unit investigates **hardy–weinberg model**, whose underlying level of analysis should be inspected in that section.

## 5.2 Variance and heritability

### Mechanistic foundation: Variance and heritability

Phenotypic variance is often partitioned schematically into genetic and environmental components, with covariance terms if independence assumptions fail. Broad-sense heritability is VG/VP in a defined study; narrow-sense heritability uses additive genetic variance VA/VP. Neither is a property of a gene or an immutable trait percentage, and neither tells what proportion of an individual phenotype is genetically caused. Changing environment, allele frequencies or population composition changes the ratio.

For **variance and heritability**, a model written without its inheritance assumptions is not a complete explanation.

### A quantitative example with a defined denominator

If VA=12 and VP=30 in matched units, narrow-sense h²=0.4 within the specified population and model.

Read the example in two passes. First solve the arithmetic as a hypothetical well-controlled classroom case. This separates a mathematical exercise from a causal scientific finding.

### From the process to an experiment

Fit a pedigree or replicated genotype model in one defined population, quantify uncertainty in each variance component, and repeat across environments before comparing estimates. Specify an independent biological unit of replication. Those are different controls and answer different questions.

For **variance and heritability**, interpretation should follow the biology of the observation, not merely whether a significance threshold was crossed.

### Interpretations worth separating

A high heritability does not imply resistance to environmental intervention or genetic determinism.

Compare the focal mechanism with **selection response**, using the dedicated topic section rather than assuming these labels describe the same process. The comparison is not evidence that one causes the other. It is a deliberate stress test for the student's categories. State explicitly when none of these strategies is feasible.

### Annotated investigation notebook

Start a new notebook entry titled *Variance and heritability: prior expectation, actual measurement, alternate mechanism*. Record the outcome before labeling it a confirmation or discrepancy.

For the next pass, consider the topic **genotype–environment structure**. Review its own mechanistic discussion before assuming a relationship. Ask whether it changes the apparent prediction for **variance and heritability**, changes only what is measured, or concerns a different scientific level entirely.

### A second, more demanding application

The memo must discuss **variance and heritability** using this design constraint: Fit a pedigree or replicated genotype model in one defined population, quantify uncertainty in each variance component, and repeat across environments before comparing estimates. What would a null result say about assay power?

The main limitation for this subsection is not decorative fine print: A high heritability does not imply resistance to environmental intervention or genetic determinism.

### Connection to the next course topic

A later unit investigates **genetic drift**, whose underlying level of analysis should be inspected in that section.

## 5.3 Selection response

### Mechanistic foundation: Selection response

The breeder equation R=h²S is a first-order prediction for response to directional selection in an additive, sufficiently stable context. S is the difference between selected parents and the population mean; R is the expected mean shift in offspring relative to the original mean. Linkage, changing genetic variance, inbreeding and environment dependence can violate the simple prediction. For multiple cycles, a constant h² assumption is often unjustified.

For **selection response**, a model written without its inheritance assumptions is not a complete explanation.

### A quantitative example with a defined denominator

With h²=0.35 and selection differential 6 g, predicted offspring shift is 2.1 g in the idealized single-generation model.

Read the example in two passes. First solve the arithmetic as a hypothetical well-controlled classroom case. This separates a mathematical exercise from a causal scientific finding.

### From the process to an experiment

Choose parents according to a preregistered trait cutoff, compare offspring with an unselected control line, and distinguish shared rearing environment from inherited change. Specify an independent biological unit of replication. Those are different controls and answer different questions.

For **selection response**, interpretation should follow the biology of the observation, not merely whether a significance threshold was crossed.

### Interpretations worth separating

A one-generation breeder prediction is not a statement about indefinite response or individual improvement.

Compare the focal mechanism with **genotype–environment structure**, using the dedicated topic section rather than assuming these labels describe the same process. The comparison is not evidence that one causes the other. It is a deliberate stress test for the student's categories. State explicitly when none of these strategies is feasible.

### Annotated investigation notebook

Start a new notebook entry titled *Selection response: prior expectation, actual measurement, alternate mechanism*. Record the outcome before labeling it a confirmation or discrepancy.

For the next pass, consider the topic **continuous traits**. Review its own mechanistic discussion before assuming a relationship. Ask whether it changes the apparent prediction for **selection response**, changes only what is measured, or concerns a different scientific level entirely.

### A second, more demanding application

The memo must discuss **selection response** using this design constraint: Choose parents according to a preregistered trait cutoff, compare offspring with an unselected control line, and distinguish shared rearing environment from inherited change. What would a null result say about assay power?

The main limitation for this subsection is not decorative fine print: A one-generation breeder prediction is not a statement about indefinite response or individual improvement.

### Connection to the next course topic

A later unit investigates **migration and selection**, whose underlying level of analysis should be inspected in that section.

## 5.4 Genotype–environment structure

### Mechanistic foundation: Genotype–environment structure

Reaction norms describe how trait values for particular genotypes depend on an environmental gradient. Parallel norms suggest genetic differences stable across environments on the measured scale; crossing norms show rank-order changes and genotype-by-environment interaction. A simple additive ANOVA can estimate components, but unbalanced designs, heteroscedasticity and correlated environments affect interpretation. A trait measurement also depends on when and how it is measured.

For **genotype–environment structure**, a model written without its inheritance assumptions is not a complete explanation.

### A quantitative example with a defined denominator

If genotype A increases from 12 to 18 and genotype B from 15 to 16, environment effects are +6 and +1, so a contrast difference is 5 trait units.

Read the example in two passes. First solve the arithmetic as a hypothetical well-controlled classroom case. This separates a mathematical exercise from a causal scientific finding.

### From the process to an experiment

Plant three genotypes in low and high resource conditions with randomized replicates, plot separate mean reaction norms and inspect whether rankings reverse. Specify an independent biological unit of replication. Those are different controls and answer different questions.

For **genotype–environment structure**, interpretation should follow the biology of the observation, not merely whether a significance threshold was crossed.

### Interpretations worth separating

A statistically detected interaction is scale-dependent and does not alone identify a molecular mechanism.

Compare the focal mechanism with **continuous traits**, using the dedicated topic section rather than assuming these labels describe the same process. The comparison is not evidence that one causes the other. It is a deliberate stress test for the student's categories. State explicitly when none of these strategies is feasible.

### Annotated investigation notebook

Start a new notebook entry titled *Genotype–environment structure: prior expectation, actual measurement, alternate mechanism*. Record the outcome before labeling it a confirmation or discrepancy.

For the next pass, consider the topic **variance and heritability**. Review its own mechanistic discussion before assuming a relationship. Ask whether it changes the apparent prediction for **genotype–environment structure**, changes only what is measured, or concerns a different scientific level entirely.

### A second, more demanding application

The memo must discuss **genotype–environment structure** using this design constraint: Plant three genotypes in low and high resource conditions with randomized replicates, plot separate mean reaction norms and inspect whether rankings reverse. What would a null result say about assay power?

The main limitation for this subsection is not decorative fine print: A statistically detected interaction is scale-dependent and does not alone identify a molecular mechanism.

### Connection to the next course topic

A later unit investigates **allele frequencies**, whose underlying level of analysis should be inspected in that section.

## Advanced studio: estimating inherited variation without genetic determinism

### From a measured distribution to a model

A measured trait such as seed mass is not the same kind of object as a categorical genotype. Its numerical value depends on trait definition, instrument calibration, developmental stage, water content, rearing environment and genetic background. A histogram tells us how observations are distributed, not which causal factors created that distribution. Consider four seed masses 10, 12, 14 and 16 milligrams. Their population mean is 13 milligrams and the population variance is five squared milligrams. If these values are treated as a sample for inference rather than an entire finite population, the ordinary unbiased sample-variance estimator divides the sum of squared deviations by three instead of four. The arithmetic denominator follows the inferential question, not the number's visual appearance.

In quantitative genetics, phenotypic variance is represented through contributions that depend on the statistical model. A schematic VP=VG+VE is appropriate only under assumptions that eliminate or explicitly account for genetic–environment covariance and residual interaction components. Genetic variation itself may be separated into additive, dominance and epistatic components according to the population's allele frequencies and a chosen parameterization. These statistical components do not map one-to-one to unique molecular pathways. A variance model fitted in a greenhouse at one temperature can have a different decomposition in a field environment or in a population with different allele frequencies.

### What heritability actually describes

Narrow-sense heritability h²=VA/VP compares additive genetic variance to phenotypic variance within a specified population and environment. If VA=12 and VP=30, the estimate is 0.4. This does not mean that forty percent of a particular person's height, seed weight or behavior is caused by DNA, with the rest caused by environment. Individuals do not come equipped with a personal variance decomposition. Variance is a property of a set of observations and a model. A uniform environment may reduce environmental variance and increase heritability even when genetic mechanisms are unchanged; environmental inequality can alter phenotypic variation and change the ratio in the opposite direction.

Imagine two breeding populations with identical sets of alleles but different nutrient availability. In one population, nutritional exposure varies greatly between trays. In the other, nutrient exposure is tightly controlled and standardized. The underlying DNA differences need not change for the estimated h² values to differ. Likewise, selective breeding alters allele frequencies and relatedness, which can change additive variance from one generation to the next. The correct scientific statement reports population, time, environmental conditions, trait metric, estimation method and uncertainty. Omitting those qualifiers creates an illusion that heritability is a fixed property of a trait everywhere.

### Selection response and its assumptions

The breeder equation R=h²S separates selection differential S from realized response R. Suppose selected parents have a mean six grams above the base population and h² is 0.35. The first-order predicted next-generation shift is 2.1 grams, assuming an approximately additive architecture and sufficiently comparable environmental conditions. It is not a guarantee of any particular offspring outcome. The selected parent mean can also contain an environmental advantage that offspring will not inherit, while relatedness and linkage can cause variation in realized transmission. A controlled selection experiment therefore uses replicate lines, unselected controls and ideally common-environment offspring assays.

The equation also loses reliability if one extrapolates it indefinitely. Continued selection can deplete favorable additive variation, increase inbreeding, expose correlated trade-offs or change genotype–environment relationships. A model of response across ten generations needs a recursion that updates genetic variance, selection intensity and perhaps effective population size. Applying the same h² and S ten times without sensitivity analysis masks the very processes that make breeding biologically interesting. Predictive models should be compared with observed outcomes and revised when their assumptions fail.

### Reaction norms expose environmental structure

Plot the expected phenotype of each genotype across an ordered environmental gradient. If lines are parallel on the chosen trait scale, additive genetic differences persist with similar magnitude across those environments. If they cross, genotype rankings depend on environment. For example, genotype A has trait means 12 and 18 in low and high resources; genotype B has means 15 and 16. In low resources B is higher, while in high resources A is higher. The first genotype responds by six units and the second by one; the interaction difference on an additive scale is five units. The analysis needs replication and uncertainty before drawing conclusions about robustness. It also depends on the chosen mathematical scale; transformations can change whether an interaction appears additive.

A well-designed greenhouse study uses randomized placement, periodic tray rotation, batch control and blinded scoring. Multiple individuals per genotype should be spread across experimental units rather than placed together in one container that confounds genotype with environment. If a dataset contains only one representative genotype per family, family background and genotype effects may be inseparable. The final report needs an honest account of relatedness, model assumptions and uncertainty. Quantitative genetics provides tools for thinking about inherited differences; it never authorizes ranking individuals deterministically or treating social outcomes as inevitable products of genetics.

## Further conceptual check: between-family versus within-family comparisons

Family resemblance can arise through shared genes, shared environments and the relationships between them. A correlation between a parental trait and an offspring trait is not automatically an estimate of additive heritability. If high-yield families also receive systematically different growing conditions, environment is confounded with pedigree. Replicated breeding designs and mixed-effects models attempt to separate those components, but their estimates remain dependent on the available relatedness structure and model assumptions.

Consider two parental families grown on separate shelves with different light intensities. Even if each family produces many seedlings, family and shelf effects cannot be distinguished without moving genotypes across environments. A better design splits offspring from each family across randomized shelves and blocks, then records shared tray effects. In a statistical model, a family random effect may absorb several sources of similarity, not just additive inherited variance. The appropriate label for a model component depends on its design and covariance assumptions. Reporting standard errors alone does not repair an unidentifiable experimental design.

## Integrated Genetics Laboratory 5: Quantitative genetics

This laboratory is a written and computational design exercise. The first case involves **continuous traits**: For trait values 10, 12, 14 and 16, the population mean is 13 and population variance is 5 in squared trait units. The second involves **variance and heritability**: If VA=12 and VP=30 in matched units, narrow-sense h²=0.4 within the specified population and model. Treat both as mathematical thought experiments with supplied assumptions.

**Protocol design.** Begin by enumerating possible states without scoring phenotypes. Include one independent validation of the genotype or marker state. The rationale for the first experiment is Record a quantitative plant trait across replicated environments with randomized blocks, repeated calibration measurements and known relatedness. Inspect residual distributions before fitting a genetic model. A competing observation strategy involves Fit a pedigree or replicated genotype model in one defined population, quantify uncertainty in each variance component, and repeat across environments before comparing estimates. These need not have the same denominator or uncertainty model.

Then compare the inference to **selection response**. Its mechanism is: The breeder equation R=h²S is a first-order prediction for response to directional selection in an additive, sufficiently stable context. For multiple cycles, a constant h² assumption is often unjustified.

It includes the caveat for **genotype–environment structure**: A statistically detected interaction is scale-dependent and does not alone identify a molecular mechanism. For a population-frequency estimate include the time and sampling frame. For a family inference specify the selection rule for included pedigrees.

**Ethical and reproducibility note.** Use synthetic or appropriately consented data only. Share versioned simulation settings and code, not identifying family genomic records.

## Fully worked questions

All examples below are hypothetical and contain the necessary model assumptions. Solutions are provided to make reasoning inspectable rather than turning a genetics inference into a memorized ratio.

### Problem 1: Trait variance

Four illustrative trait measurements are 10, 12, 14 and 16 units. Compute their population mean and variance.

**Worked solution**

1. The mean is (10+12+14+16)/4=13.
2. Squared deviations from 13 are 9,1,1,9, which sum to 20.
3. The population variance is 20/4=5 squared units. A sample variance estimator would use denominator 3 instead.

### Problem 2: Additive heritability

A population model estimates additive genetic variance 12 and phenotypic variance 30 in matched units. Compute narrow-sense heritability.

**Worked solution**

1. Define h² as the ratio of additive genetic variance VA to total phenotypic variance VP in a specified population.
2. Substitute VA=12 and VP=30: h²=12/30=0.4.
3. This 40% is a variance ratio; it is not the fraction of an individual’s trait caused by genes.

### Problem 3: Selection response

A breeding population has h²=0.35 and selection differential S=6 grams. Compute first-generation expected response.

**Worked solution**

1. The first-order breeder equation is R=h²S under a stable additive response model.
2. Multiply 0.35 by 6 grams to obtain R=2.1 grams.
3. Changing genetic variance, rearing environment and selection intensity can make observed response differ from this expectation.

## Interactive genetics investigation

These interactive models are explicitly simplified quantitative thought experiments. Use the sliders to change one assumption at a time, inspect the curve or categorical display, check a limiting case, and reset to the baseline. A classroom model is not a clinical test or a measured population estimate.

### Model: h2

The h2 model provides a numerical expectation or uncertainty-dependent outcome associated with Unit 5. Copy the default readout, alter the first parameter, and predict whether the result should rise, fall or be nonmonotonic. Change the second parameter and identify which part of the equation it modifies. Return to the starting settings and check that the original value is restored. State whether the plotted quantity represents a probability, an expectation, a standardized statistic, or a physical copy count.

Model interpretation should refer back to the underlying derivation and the experimental denominators in this chapter. Do not extrapolate beyond the allowed slider range, and do not describe a smooth curve as data from an observed population. If the model rejects an impossible parameter combination, explain the rejected biological assumption in words rather than simply resetting the input.

### Model: breeder

The breeder model provides a numerical expectation or uncertainty-dependent outcome associated with Unit 5. Copy the default readout, alter the first parameter, and predict whether the result should rise, fall or be nonmonotonic. Change the second parameter and identify which part of the equation it modifies. Return to the starting settings and check that the original value is restored. State whether the plotted quantity represents a probability, an expectation, a standardized statistic, or a physical copy count.

Model interpretation should refer back to the underlying derivation and the experimental denominators in this chapter. Do not extrapolate beyond the allowed slider range, and do not describe a smooth curve as data from an observed population. If the model rejects an impossible parameter combination, explain the rejected biological assumption in words rather than simply resetting the input.
