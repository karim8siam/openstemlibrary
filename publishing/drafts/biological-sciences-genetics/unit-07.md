# Unit 7: Complex inheritance

## Unit overview

Complex inheritance often arises because multiple causal links intervene between DNA and a measured trait. Epistasis, penetrance, polygenic scores and genotype–environment interaction are related concepts, but they are not synonyms. In particular, statistical interaction need not prove molecular contact; incomplete penetrance does not rewrite allele segregation; and a polygenic prediction is not a deterministic diagnosis. The examples force students to state a phenotype definition, model scale, population and uncertainty before interpreting effects.

## Learning goals

Explain mechanisms without conflating genotype, molecular state and observable phenotype; formulate explicit conditional probabilities; solve distinct numerical examples with appropriate denominators; evaluate experimental controls; challenge an alternative interpretation; and inspect the assumptions behind each interactive model.

## 7.1 Epistasis and interaction

### Mechanistic foundation: Epistasis and interaction

Epistasis means the phenotypic effect of one locus depends on genetic state at another locus. In a simple recessive epistasis cross, a blocked biochemical step can mask variation at a later step, producing a 9:3:4 F2 phenotype ratio under specific assumptions. Statistical interaction in a regression is not automatically the same as a molecular interaction, and its magnitude changes with trait scale. Biological pathway reasoning helps distinguish the two.

For **epistasis and interaction**, a model written without its inheritance assumptions is not a complete explanation.

### A quantitative example with a defined denominator

For 160 F2 progeny under an ideal 9:3:4 ratio, expected class counts are 90, 30 and 40.

Read the example in two passes. First solve the arithmetic as a hypothetical well-controlled classroom case. This separates a mathematical exercise from a causal scientific finding.

### From the process to an experiment

Genotype both loci, measure molecular intermediates and phenotype, and compare full two-locus models with additive predictions across controlled environments. Specify an independent biological unit of replication. Those are different controls and answer different questions.

For **epistasis and interaction**, interpretation should follow the biology of the observation, not merely whether a significance threshold was crossed.

### Interpretations worth separating

A nonadditive phenotype does not prove direct binding between the two gene products.

Compare the focal mechanism with **penetrance and expressivity**, using the dedicated topic section rather than assuming these labels describe the same process. The comparison is not evidence that one causes the other. It is a deliberate stress test for the student's categories. State explicitly when none of these strategies is feasible.

### Annotated investigation notebook

Start a new notebook entry titled *Epistasis and interaction: prior expectation, actual measurement, alternate mechanism*. Record the outcome before labeling it a confirmation or discrepancy.

For the next pass, consider the topic **polygenic traits and prediction**. Review its own mechanistic discussion before assuming a relationship. Ask whether it changes the apparent prediction for **epistasis and interaction**, changes only what is measured, or concerns a different scientific level entirely.

### A second, more demanding application

The memo must discuss **epistasis and interaction** using this design constraint: Genotype both loci, measure molecular intermediates and phenotype, and compare full two-locus models with additive predictions across controlled environments. What would a null result say about assay power?

The main limitation for this subsection is not decorative fine print: A nonadditive phenotype does not prove direct binding between the two gene products.

### Connection to the next course topic

A later unit investigates **pedigree likelihoods**, whose underlying level of analysis should be inspected in that section.

## 7.2 Penetrance and expressivity

### Mechanistic foundation: Penetrance and expressivity

Penetrance is the proportion of people or organisms with a defined genotype who display a specified phenotype under defined conditions; expressivity describes variation in phenotype severity among those expressing it. Age, environment, modifiers, assay threshold and incomplete clinical ascertainment all influence measured rates. A genotype with reduced penetrance can appear to skip generations in pedigrees without changing Mendelian allele transmission.

For **penetrance and expressivity**, a model written without its inheritance assumptions is not a complete explanation.

### A quantitative example with a defined denominator

Under an illustrative penetrance of 0.7, the chance of an unaffected carrier at the stated observation time is 0.3.

Read the example in two passes. First solve the arithmetic as a hypothetical well-controlled classroom case. This separates a mathematical exercise from a causal scientific finding.

### From the process to an experiment

Follow genotype-confirmed individuals longitudinally, apply a prespecified phenotype definition and compare age-specific estimates rather than pooling unequal follow-up periods. Specify an independent biological unit of replication. Those are different controls and answer different questions.

For **penetrance and expressivity**, interpretation should follow the biology of the observation, not merely whether a significance threshold was crossed.

### Interpretations worth separating

Penetrance cannot be interpreted as a universal constant for a variant independent of the phenotype definition and studied population.

Compare the focal mechanism with **polygenic traits and prediction**, using the dedicated topic section rather than assuming these labels describe the same process. The comparison is not evidence that one causes the other. It is a deliberate stress test for the student's categories. State explicitly when none of these strategies is feasible.

### Annotated investigation notebook

Start a new notebook entry titled *Penetrance and expressivity: prior expectation, actual measurement, alternate mechanism*. Record the outcome before labeling it a confirmation or discrepancy.

For the next pass, consider the topic **gene–environment interaction**. Review its own mechanistic discussion before assuming a relationship. Ask whether it changes the apparent prediction for **penetrance and expressivity**, changes only what is measured, or concerns a different scientific level entirely.

### A second, more demanding application

The memo must discuss **penetrance and expressivity** using this design constraint: Follow genotype-confirmed individuals longitudinally, apply a prespecified phenotype definition and compare age-specific estimates rather than pooling unequal follow-up periods. What would a null result say about assay power?

The main limitation for this subsection is not decorative fine print: Penetrance cannot be interpreted as a universal constant for a variant independent of the phenotype definition and studied population.

### Connection to the next course topic

A later unit investigates **genomics and variant interpretation**, whose underlying level of analysis should be inspected in that section.

## 7.3 Polygenic traits and prediction

### Mechanistic foundation: Polygenic traits and prediction

Many measured traits aggregate small associations across loci, often with effects estimated in one study population and trait definition. A polygenic score can summarize statistical association but does not determine an individual outcome. Predictive calibration may shift with ancestry, age, environment and measurement. Correlation among linked variants and selection of discovery samples can inflate naive transfer of effect estimates.

For **polygenic traits and prediction**, a model written without its inheritance assumptions is not a complete explanation.

### A quantitative example with a defined denominator

For allelic dosages 0,1,2 weighted by 0.2,−0.1,0.4 respectively, an additive toy score is 0×0.2+1×(−0.1)+2×0.4=0.7 units.

Read the example in two passes. First solve the arithmetic as a hypothetical well-controlled classroom case. This separates a mathematical exercise from a causal scientific finding.

### From the process to an experiment

Split discovery, tuning and validation datasets at the individual and family level, evaluate calibration and predictive error separately for subgroups, and report outcomes with uncertainty. Specify an independent biological unit of replication. Those are different controls and answer different questions.

For **polygenic traits and prediction**, interpretation should follow the biology of the observation, not merely whether a significance threshold was crossed.

### Interpretations worth separating

Strong sample-level predictive performance does not imply a modifiable molecular cause for every marker included in a score.

Compare the focal mechanism with **gene–environment interaction**, using the dedicated topic section rather than assuming these labels describe the same process. The comparison is not evidence that one causes the other. It is a deliberate stress test for the student's categories. State explicitly when none of these strategies is feasible.

### Annotated investigation notebook

Start a new notebook entry titled *Polygenic traits and prediction: prior expectation, actual measurement, alternate mechanism*. Record the outcome before labeling it a confirmation or discrepancy.

For the next pass, consider the topic **epistasis and interaction**. Review its own mechanistic discussion before assuming a relationship. Ask whether it changes the apparent prediction for **polygenic traits and prediction**, changes only what is measured, or concerns a different scientific level entirely.

### A second, more demanding application

The memo must discuss **polygenic traits and prediction** using this design constraint: Split discovery, tuning and validation datasets at the individual and family level, evaluate calibration and predictive error separately for subgroups, and report outcomes with uncertainty. What would a null result say about assay power?

The main limitation for this subsection is not decorative fine print: Strong sample-level predictive performance does not imply a modifiable molecular cause for every marker included in a score.

### Connection to the next course topic

A later unit investigates **ethics, privacy and inference**, whose underlying level of analysis should be inspected in that section.

## 7.4 Gene–environment interaction

### Mechanistic foundation: Gene–environment interaction

A gene–environment interaction occurs when the effect of a genotype depends on environmental conditions or the effect of an exposure depends on genotype, on a specified effect scale. Interaction may arise from changed pathway activity, differential exposure, confounding or selection into the sample. Randomization of environment can be powerful in experiments, but is not feasible or ethical for every human exposure. Estimation must separate a true interaction from a nonlinear baseline relation.

For **gene–environment interaction**, a model written without its inheritance assumptions is not a complete explanation.

### A quantitative example with a defined denominator

With genotype A response 4→7 and genotype B response 5→12, the difference in environment effects is (12−5)−(7−4)=4.

Read the example in two passes. First solve the arithmetic as a hypothetical well-controlled classroom case. This separates a mathematical exercise from a causal scientific finding.

### From the process to an experiment

Design a factorial experiment with genotype classes and two benign environmental conditions, preregister a difference-of-differences contrast and check the confidence interval. Specify an independent biological unit of replication. Those are different controls and answer different questions.

For **gene–environment interaction**, interpretation should follow the biology of the observation, not merely whether a significance threshold was crossed.

### Interpretations worth separating

An interaction on an additive scale may disappear on a multiplicative scale, so the scale must be reported.

Compare the focal mechanism with **epistasis and interaction**, using the dedicated topic section rather than assuming these labels describe the same process. The comparison is not evidence that one causes the other. It is a deliberate stress test for the student's categories. State explicitly when none of these strategies is feasible.

### Annotated investigation notebook

Start a new notebook entry titled *Gene–environment interaction: prior expectation, actual measurement, alternate mechanism*. Record the outcome before labeling it a confirmation or discrepancy.

For the next pass, consider the topic **penetrance and expressivity**. Review its own mechanistic discussion before assuming a relationship. Ask whether it changes the apparent prediction for **gene–environment interaction**, changes only what is measured, or concerns a different scientific level entirely.

### A second, more demanding application

The memo must discuss **gene–environment interaction** using this design constraint: Design a factorial experiment with genotype classes and two benign environmental conditions, preregister a difference-of-differences contrast and check the confidence interval. What would a null result say about assay power?

The main limitation for this subsection is not decorative fine print: An interaction on an additive scale may disappear on a multiplicative scale, so the scale must be reported.

### Connection to the next course topic

A later unit investigates **crosses and experimental design**, whose underlying level of analysis should be inspected in that section.

## Advanced studio: separating complexity from vagueness

### Two genes can interact without proteins touching

Consider a pathway in which one gene product makes a precursor pigment and another converts that precursor to a visible form. If the first process is completely blocked by a recessive genotype, variation at the downstream locus may have no visible effect. With independent assortment and specific fully penetrant classifications, a classical F2 cross can exhibit a 9:3:4 phenotypic ratio. Nine sixteenths of offspring express the jointly functional class, three sixteenths have one pathway outcome, and four sixteenths share the phenotype caused by an upstream block. For one hundred sixty offspring, the expected values are ninety, thirty and forty. Those are phenotype-class probabilities under an explicit model, not universal ratios produced by every pair of genes.

Now consider a regression model of a quantitative trait containing genotype indicators G1 and G2 together with an interaction product G1×G2. A nonzero estimated interaction coefficient means that the combined statistical effect differs from the specified additive baseline on the chosen scale. That observation does not require that two proteins bind each other; the result could reflect a multi-step pathway, environment dependence or phenotype transformation. Conversely, physical protein interaction need not produce a large statistical interaction in a specific population. Distinguishing these definitions prevents a mechanistic overclaim based on a coefficient alone.

### Penetrance modifies observation, not meiosis

A variant may be inherited according to simple Mendelian rules but display a phenotype only in some carriers under a defined observation criterion. If penetrance is 70% by a particular age, then thirty percent of genetically confirmed carriers are not observed with that phenotype by that age under the stipulated study model. The underlying allele does not cease to exist in those carriers. Observing an apparently unaffected parent with an affected child can be consistent with reduced penetrance, but also with a new mutation, variable expressivity, alternative inherited mechanisms or classification error. To evaluate the possibilities one must use genotype data, age-dependent phenotype definitions and family ascertainment rather than treating a skipped pedigree symbol as proof.

Expressivity describes the variation in severity or form of a phenotype among expressing carriers. Penetrance and expressivity are therefore different summaries. If an assay uses a stricter diagnostic threshold, some mildly expressing carriers can be reclassified as unaffected, changing the measured penetrance. Longitudinal observation may further alter classification as the phenotype develops. A prevalence percentage from one clinical cohort should not be transferred casually to a different population or age group. Data collection and the biological model are inseparable.

### Polygenic prediction is calibrated to a population

A polygenic score may add weighted allele dosages from many marker loci to predict variation in an outcome. For a deliberately simple example, if dosages are 0, 1 and 2 with weights 0.2, −0.1 and 0.4, their additive score equals 0.7 arbitrary units. The score is not a physical amount of a molecule and cannot be converted into an individual's destiny. Its predictive value depends on the training population, associations among markers, environmental distribution and phenotype definition. Overlap between relatives in training and testing data can exaggerate apparent performance, as can selecting the best model after repeatedly examining a nominal holdout set.

A credible evaluation separates the discovery cohort, development decisions and final validation cohort, checks calibration rather than only ranking ability, and reports performance by relevant sample groups. If a model's predictions are systematically too high for one group and too low for another, its apparent average accuracy hides inequitable errors. Genetic ancestry correlations do not justify treating social or racial categories as biological essences. The investigator should discuss dataset representation, migration and population structure, and the difference between association and causation.

### Explicitly model the environment

A factorial genotype–environment experiment estimates whether the genotype contrast changes between environmental treatments. Suppose genotype A has means 4 and 7 in low and high resources, while genotype B has means 5 and 12. The effect of changing environment is three units for A and seven units for B; the difference of these effects is four units. This difference-of-differences contrast is an interaction on an additive trait scale. It requires replication and uncertainty to assess against noise, and a log or ratio-scale model may yield a different interaction statement. No scale-free interaction coefficient exists for all biological questions.

An informative experiment randomizes treatment, balances developmental stages, includes replicate individuals and records whether genotypes differ in survival before measurement. Otherwise, apparent response differences may arise because only unusually robust individuals remain in one condition. Molecular measurements of pathway activity can help suggest a mechanism for the interaction, but correlations across a handful of samples cannot replace targeted perturbation. The goal is to say exactly which genetic effect is modified by which environment and to identify the conditions under which the claim can be tested or falsified.

## Further conceptual check: thresholds and nonlinear observation

A continuously varying underlying liability can produce a seemingly categorical phenotype when a fixed threshold is used. Environmental exposures, several genes, developmental noise and measurement uncertainty can jointly shift liability. Moving the threshold changes the measured prevalence even if the continuous distribution itself is unchanged. In such a model, a genotype can alter the mean liability without guaranteeing that every carrier crosses the diagnostic or experimental cutoff. This is one route to apparent incomplete penetrance, although the liability-threshold model is not appropriate for every trait.

To examine interpretation, suppose an assay calls a plant stressed when fluorescence falls below an arbitrarily selected value. Plants close to that threshold can switch categories under small measurement perturbations. A genotype associated with a modest shift in average fluorescence may show a large apparent change in the binary stressed fraction if many individuals sit near the cutoff. Report continuous measurements where scientifically meaningful, justify thresholds before analysis and test conclusions across plausible alternative thresholds. A categorical effect should not be treated as a universal property of the genotype when it is partly created by the operational phenotype definition.

## Integrated Genetics Laboratory 7: Complex inheritance

This laboratory is a written and computational design exercise. The first case involves **epistasis and interaction**: For 160 F2 progeny under an ideal 9:3:4 ratio, expected class counts are 90, 30 and 40. The second involves **penetrance and expressivity**: Under an illustrative penetrance of 0.7, the chance of an unaffected carrier at the stated observation time is 0.3. Treat both as mathematical thought experiments with supplied assumptions.

**Protocol design.** Begin by enumerating possible states without scoring phenotypes. Include one independent validation of the genotype or marker state. The rationale for the first experiment is Genotype both loci, measure molecular intermediates and phenotype, and compare full two-locus models with additive predictions across controlled environments. A competing observation strategy involves Follow genotype-confirmed individuals longitudinally, apply a prespecified phenotype definition and compare age-specific estimates rather than pooling unequal follow-up periods. These need not have the same denominator or uncertainty model.

Then compare the inference to **polygenic traits and prediction**. Its mechanism is: Many measured traits aggregate small associations across loci, often with effects estimated in one study population and trait definition. Predictive calibration may shift with ancestry, age, environment and measurement.

It includes the caveat for **gene–environment interaction**: An interaction on an additive scale may disappear on a multiplicative scale, so the scale must be reported. For a population-frequency estimate include the time and sampling frame. For a family inference specify the selection rule for included pedigrees.

**Ethical and reproducibility note.** Use synthetic or appropriately consented data only. Share versioned simulation settings and code, not identifying family genomic records.

## Fully worked questions

All examples below are hypothetical and contain the necessary model assumptions. Solutions are provided to make reasoning inspectable rather than turning a genetics inference into a memorized ratio.

### Problem 1: Epistatic phenotypic classes

A model F2 cross follows a 9:3:4 recessive epistasis ratio. For 160 offspring, find expected class numbers.

**Worked solution**

1. Convert the ratio parts into probabilities 9/16, 3/16 and 4/16.
2. Multiply each by 160 to obtain 90, 30 and 40 expected offspring.
3. The ratio requires independent segregation and the specific pathway-phenotype assumptions of recessive epistasis.

### Problem 2: Penetrance complement

A defined variant has penetrance 0.70 by a particular observation age in a hypothetical carrier group. What fraction are phenotypically unaffected?

**Worked solution**

1. Penetrance is the conditional probability of the specified phenotype among carriers under the stipulated observation conditions.
2. The complementary probability of not expressing that phenotype is 1−0.70=0.30.
3. The estimate changes with phenotype definition, age, environmental context and ascertainment.

### Problem 3: Difference of differences

Genotype A has mean 4 in environment 1 and 7 in environment 2; genotype B has means 5 and 12. Find the difference in environmental effects.

**Worked solution**

1. Environmental change in genotype A is 7−4=3 trait units.
2. Environmental change in genotype B is 12−5=7 trait units.
3. The additive-scale interaction contrast is 7−3=4 units. A formal estimate would also require uncertainty and replication.

## Interactive genetics investigation

These interactive models are explicitly simplified quantitative thought experiments. Use the sliders to change one assumption at a time, inspect the curve or categorical display, check a limiting case, and reset to the baseline. A classroom model is not a clinical test or a measured population estimate.

### Model: penetrance

The penetrance model provides a numerical expectation or uncertainty-dependent outcome associated with Unit 7. Copy the default readout, alter the first parameter, and predict whether the result should rise, fall or be nonmonotonic. Change the second parameter and identify which part of the equation it modifies. Return to the starting settings and check that the original value is restored. State whether the plotted quantity represents a probability, an expectation, a standardized statistic, or a physical copy count.

Model interpretation should refer back to the underlying derivation and the experimental denominators in this chapter. Do not extrapolate beyond the allowed slider range, and do not describe a smooth curve as data from an observed population. If the model rejects an impossible parameter combination, explain the rejected biological assumption in words rather than simply resetting the input.

### Model: epistasis

The epistasis model provides a numerical expectation or uncertainty-dependent outcome associated with Unit 7. Copy the default readout, alter the first parameter, and predict whether the result should rise, fall or be nonmonotonic. Change the second parameter and identify which part of the equation it modifies. Return to the starting settings and check that the original value is restored. State whether the plotted quantity represents a probability, an expectation, a standardized statistic, or a physical copy count.

Model interpretation should refer back to the underlying derivation and the experimental denominators in this chapter. Do not extrapolate beyond the allowed slider range, and do not describe a smooth curve as data from an observed population. If the model rejects an impossible parameter combination, explain the rejected biological assumption in words rather than simply resetting the input.
