# Unit 02: Population processes and evolutionary forces

> Separating allele-frequency calculations from causal claims about selection, drift, mutation and gene flow.

## Learning outcomes

By the end of this unit, the reader should be able to investigate population processes and evolutionary forces, interpret a relevant quantitative model, design a realistic test that controls for alternative explanations, and state the principal limits of the inference. An intellectually satisfactory answer can remain uncertain when the data do not discriminate among mechanisms.

## Integrative foundation

### The frequency is a fraction; the process is a hypothesis

Allele-frequency bookkeeping begins with choosing a population, time interval and locus. In a diploid sample with equal reliable genotyping, an AA individual contributes two A copies, an Aa individual contributes one, and an aa individual contributes none. Allele frequency is therefore a ratio of counted copies; a frequency by itself cannot reveal whether mutation, drift, selection or migration produced a change. Likewise, an allele may remain constant over several sampling periods despite continuing selection if opposing processes balance one another. The correct scientific task is not to announce a cause from a plot but to compare process-specific predictions.

The Hardy–Weinberg model is a reference for one locus under assumptions about mating and other processes, not a promise that organisms naturally obey the assumptions. A mismatch can result from genotype error, substructure, selection, assortative mating or finite sampling. In particular, pooling differently distributed populations often creates a deficit of heterozygotes relative to a pooled random-mating baseline. This is known as the Wahlund effect and illustrates why choosing a sampling boundary is part of the biological analysis, not a clerical decision. The same issue arises when adults sampled from several distant streams are combined and treated as one breeding population.

### Why replicates change inference

Deterministic selection models predict an expected frequency trajectory from stipulated fitness values, while stochastic models predict a distribution of trajectories. Replicating a drift simulation many times shows that neutral allele frequencies can rise, fall or be lost from any particular population while the mean trajectory remains approximately stationary under the idealized assumptions. The variance among populations is the informative statistic. In a small effective population, repeated sampling consumes more of the available variation than in a large one. Effective population size is a model-derived measure of genetic drift or inbreeding intensity; it often differs markedly from the number of individuals counted in the landscape.

Similarly, a mutation rate describes the production of new variants under specified molecular or reproductive conditions. A variant can appear many times yet remain rare if it is harmful or repeatedly lost by chance. Conversely, a variant initially rare can increase dramatically when selection changes. A resistant colony count is therefore not automatically a mutation-rate measurement. A fluctuation experiment uses variation among independently cultured replicate populations to help distinguish mutations present before exposure from adaptation induced directly by exposure.

### Designing a transparent population-genetic comparison

Start with genotype counts from two sampling times and calculate the corresponding allele frequencies. Record sample size and missing calls. Fit a null model of sampling variability, then compare the predictions under a migration pulse, one-generation selection and neutral drift. Each process should have an explicitly chosen parameter and a distinct observation it predicts. For instance, strong movement evidence without offspring assignment does not demonstrate genetic migration. A genetic frequency shift correlated with a changed habitat does not prove that habitat caused selection. If repeated loci share the same sudden shift, demographic processes may offer a parsimonious explanation; if a particular genomic region deviates strongly, locus-specific processes deserve consideration, but linked inheritance must still be assessed.

This unit's goal is the disciplined separation of calculation from causal explanation. Arithmetic can be exact under a model that is biologically inappropriate. Good reports give both the calculated result and the conditions under which it would be meaningful.

## Focused studies and worked problems

### 2.1 Allele frequencies and Hardy–Weinberg reasoning

#### Core idea and causal mechanism

Allele frequency is the fraction of gene copies of a specified type among sampled copies, not a claim about the fitness of its carriers. Hardy–Weinberg proportions are a useful null expectation for idealized randomly mating diploids.

With two alleles A and a, p+q=1; random union of gametes yields p² AA, 2pq Aa and q² aa genotype proportions. Departures in observed counts can result from selection, population structure, genotyping errors and other causes.

#### Example in biological context

In a synthetic classroom population with p=0.7 and q=0.3, expected heterozygosity under the ideal model is 0.42. Real samples can deviate by chance even without a systematic evolutionary force.

#### Evidence and a workable test

Compute p from genotype counts rather than phenotype labels when dominance obscures heterozygotes; compare observed and expected proportions using sample size and measurement error, not mere visual discrepancy.

**Investigation prompt.** Recalculate the same allele-frequency statistic with one alternative sampling boundary and show how its denominator changes. Model selection and chance sampling separately; a plausible-looking trajectory should not be treated as proof of either.

#### Where the inference could fail

Hardy–Weinberg balance at one locus does not prove a population is free from evolution, and disequilibrium does not identify a unique cause. Selection can occur with subtle frequency changes that are hard to detect.

Quantify how a small effective size widens possible outcomes. Report expectations over repeated replicates rather than a single striking simulation path, and explain why uncertainty need not indicate scientific ignorance.

#### Apply and question

Use a table of AA, Aa and aa genotypes to estimate p, expected heterozygosity and the direction of a change across two samples. Specify how unequal sampling alters confidence.

Population-genetic bookkeeping underlies conservation monitoring, forensic population analysis and experimental selection studies, but ethically sensitive human inferences demand extra care.

What happens if a pooled sample combines two genetically differentiated populations? Predict whether the pooled heterozygote fraction may be depressed relative to a single random-mating reference. Your answer should include a prediction that differs between hypotheses and state which assumptions would remain untested after the observation.

#### Quantitative case 2.1: Hardy–Weinberg heterozygotes

**Assumed data (synthetic).** In a hypothetical two-allele diploid population, p=0.65 and q=0.35.

**Calculation.** Expected heterozygote fraction under random gamete union is 2pq. Substituting the stipulated values into `2*0.65*0.35` gives **0.455 fraction**. Confirm the result independently and retain consistent units.

**Interpretation.** The expectation is 0.455, not the measured heterozygote proportion in any particular real population.

**Model limitation.** Population subdivision or consanguinity can depress observed heterozygosity.

**Try next.** Compute expected AA and aa fractions and verify that all three sum to one. Show the derivation and distinguish the numerical result from any proposed biological cause.


### 2.2 Mutation as the source of new variants

#### Core idea and causal mechanism

Mutation creates new alleles through sequence changes, insertions, deletions, rearrangements and other genome alterations; most mutations do not arise because an organism needs a particular advantageous state.

Replication errors and DNA damage/repair processes shape mutation spectra. A new variant may be neutral, deleterious or occasionally beneficial in a defined environment; its fate after origin depends on inheritance, selection and stochastic loss.

#### Example in biological context

A bacterial mutation may change a drug target and reduce drug binding, while also imposing a growth cost without medication. Fitness effects are contextual and may change when compensatory mutations occur.

#### Evidence and a workable test

Measure mutation rates with suitable fluctuation experiments or sequence parent-offspring lineages, carefully separating mutation *appearance* from the rise of an existing variant under selection.



#### Where the inference could fail

Sequencing errors, contamination and gene transfer can masquerade as new mutations. A mutation's frequency among surviving colonies is not the underlying per-division mutation rate.



#### Apply and question

State how you would use independent replicate cultures to distinguish selection of pre-existing mutants from directed response. Interpret what a highly variable distribution of resistant colony counts implies.

Recognizing mutation-selection separation shapes antibiotic stewardship and evolutionary forecasting. Mutation-rate estimation also matters for genetic disease research but population estimates are not diagnoses.

Could the same mutation be beneficial in one environment and harmful in another? Build a two-environment payoff table and explain why the answer does not require purposeful mutation. Your answer should include a prediction that differs between hypotheses and state which assumptions would remain untested after the observation.

#### Quantitative case 2.2: Expected number of new mutants

**Assumed data (synthetic).** A teaching culture undergoes 2.5 million cell divisions with an assumed per-division mutation rate of 0.000004 for a specified event.

**Calculation.** Multiply divisions by the assumed rate for the expected number of mutation occurrences. Substituting the stipulated values into `2500000*0.000004` gives **10 events**. Confirm the result independently and retain consistent units.

**Interpretation.** Expectation 10 does not imply exactly ten distinct colonies or that each mutant survives.

**Model limitation.** Mutation events can recur in descendants or remain undetected; mutation rate differs among genomic changes.

**Try next.** Why might fluctuation-test counts vary much more than a Poisson-like count from independent events? Show the derivation and distinguish the numerical result from any proposed biological cause.


### 2.3 Natural selection and relative fitness

#### Core idea and causal mechanism

Natural selection requires heritable variation linked to differences in reproductive success. Absolute offspring counts can change with ecology, while *relative* fitness determines changes in variant representation in a simple selection model.

In a haploid two-type approximation, after selection p' = p wA / (p wA + (1-p) wa). Frequency dependence, age structure, dominance and changing environments require more complex treatments.

#### Example in biological context

A synthetic insect population has color morphs with different predation risks on distinct substrates; when the substrate changes, the favored morph may reverse without any alteration in the rules of heredity.

#### Evidence and a workable test

Estimate reproductive output of genotyped individuals over a comparable life cycle, account for survival versus fecundity components, and conduct replicate treatments to guard against confounded microhabitats.



#### Where the inference could fail

A positive association between a trait and offspring count may reflect body size or habitat quality rather than causal selection on the trait itself. Fitness is environment- and time-dependent.



#### Apply and question

Calculate a one-generation frequency prediction, then list observations that would make it incorrect even when its arithmetic is exact. Compare the result with a randomly drifting population.

Applied breeding can change trait distributions rapidly, but correlated traits and loss of diversity make narrowly optimizing one target potentially costly.

Under what conditions does a locally advantageous allele fail to fix? Consider recurrent migration, heterozygote advantage, changing ecological selection and stochastic loss. Your answer should include a prediction that differs between hypotheses and state which assumptions would remain untested after the observation.

#### Quantitative case 2.3: One-generation haploid selection

**Assumed data (synthetic).** A haploid type starts at p=0.30, with wA=1.20 and wa=1.00.

**Calculation.** Apply p'=p wA / (p wA+(1-p)wa). Substituting the stipulated values into `0.30*1.20/(0.30*1.20+0.70*1.00)` gives **0.339623 frequency**. Confirm the result independently and retain consistent units.

**Interpretation.** Frequency rises because the first type has greater stipulated reproductive contribution; no mutation is needed for the response.

**Model limitation.** This deterministic model excludes genetic drift and changing density.

**Try next.** Repeat with wA=0.9 and explain the direction of change. Show the derivation and distinguish the numerical result from any proposed biological cause.


### 2.4 Genetic drift and effective population size

#### Core idea and causal mechanism

Genetic drift is change caused by sampling across reproduction; in finite populations it can fix or remove alleles without conferring superior adaptation. Its strength is governed by effective rather than simply census population size.

Under a Wright–Fisher diploid approximation, allele-count sampling has variance p(1-p)/(2Ne) per generation in frequency units. Unequal breeding success, skewed sex ratios and historical bottlenecks can reduce Ne relative to counts of bodies.

#### Example in biological context

A small island population can lose a rare neutral allele in a few generations even if habitat conditions remain constant. A larger population may retain more diversity while still experiencing some stochastic change.

#### Evidence and a workable test

Use many replicate numerical simulations from the same starting p and Ne, plot distribution of final frequencies and compare variance with the simple one-generation expectation.



#### Where the inference could fail

A single observed trajectory cannot reliably distinguish drift from weak selection. Temporal genetic sampling can be biased by related individuals or laboratory batches.



#### Apply and question

Change Ne without changing the starting allele frequency in a simulation. Explain why mean change across replicates approaches zero in the neutral model while variance grows as Ne shrinks.

Conservation planning should preserve breeding connectivity and monitor diversity, rather than treating a single census number as a complete measure of evolutionary resilience.

How can a population of thousands have a surprisingly small effective size? Construct examples involving highly uneven reproductive success or strong fluctuations in population size. Your answer should include a prediction that differs between hypotheses and state which assumptions would remain untested after the observation.

#### Quantitative case 2.4: Sampling variance under drift

**Assumed data (synthetic).** For a neutral allele at p=0.4, assumed effective diploid size Ne=50.

**Calculation.** Wright–Fisher one-generation frequency variance is p(1-p)/(2Ne). Substituting the stipulated values into `0.4*0.6/(2*50)` gives **0.0024 frequency-squared**. Confirm the result independently and retain consistent units.

**Interpretation.** This is the variance across replicate populations, not an expected signed change in one population.

**Model limitation.** Nonrandom reproduction and overlapping generations invalidate a literal Wright–Fisher interpretation.

**Try next.** What happens to the variance if Ne doubles while p stays fixed? Show the derivation and distinguish the numerical result from any proposed biological cause.


### 2.5 Gene flow and population structure

#### Core idea and causal mechanism

Migration of individuals or gametes can carry alleles among populations, affecting both diversity within populations and differentiation between them. 'Migration' in a genetic model means successful contribution to the breeding pool.

For a simple recipient population, p_new=(1-m)p_local + m p_source when fraction m of gene copies derives from migrants. Selection after migration can counteract introduced alleles, producing clines or stable differences.

#### Example in biological context

Windborne pollen can connect separated plant stands even when adult trees cannot move. Conversely a newly built road may sharply reduce dispersal of terrestrial animals without completely stopping it.

#### Evidence and a workable test

Genotype several spatial samples across time and compare allele-frequency patterns with independent movement evidence such as tracking or parentage assignment. Test asymmetry because gene flow may be strongly directional.



#### Where the inference could fail

Genetic similarity can result from recent common ancestry rather than present-day gene flow. A small number of successful breeders may matter more than frequent nonbreeding visitors.



#### Apply and question

Predict recipient frequency after a pulse of migration; then explain how a selective disadvantage in the recipient habitat would alter the next generation. Specify whether m measures individuals or alleles.

Habitat corridors can aid genetic rescue, but translocations must consider pathogens, ecological fit and potential disruption of locally adapted variants.

If two populations become more genetically similar, can you conclude that migration increased? Give at least two alternative mechanisms and one additional dataset. Your answer should include a prediction that differs between hypotheses and state which assumptions would remain untested after the observation.

#### Quantitative case 2.5: Migrating gene copies

**Assumed data (synthetic).** Recipient population p=0.20; source p=0.80; fraction of new recipient gene copies m=0.10.

**Calculation.** Calculate a one-pulse mixture as (1-m)p_local+mp_source. Substituting the stipulated values into `0.9*0.2+0.1*0.8` gives **0.26 frequency**. Confirm the result independently and retain consistent units.

**Interpretation.** The immediate expected recipient frequency is 0.26 before later viability selection.

**Model limitation.** Successful gene flow must be measured among breeders, not passersby.

**Try next.** How would asymmetric migration change donor and recipient trajectories? Show the derivation and distinguish the numerical result from any proposed biological cause.


## Integrated investigation 2: Replicate drift versus directional selection

**Research aim.** Distinguish a distribution of allele-frequency trajectories generated by drift from a consistent directional shift expected under a simple selection model. The investigation is designed for an introductory undergraduate seminar or computational laboratory; its specimens, dates, counts and measurements are hypothetical. Do not represent any result as a published empirical discovery.

### Materials, assumptions and ethical boundaries

At least 100 independent simulated populations at Ne=30 and another 100 at Ne=300, both starting p=0.4, plus parallel deterministic selection scenarios. Use a spreadsheet or local script to create tables and plots, recording pseudorandom seeds if stochastic simulations are used. Collect no personal genetic data. Do not culture pathogens, collect protected wildlife, disturb habitats or undertake medical tests. Where the real-world analog requires permits, trained staff or ethical approval, use simulation or openly available teaching data instead.

### Step-by-step procedure

1. For **replicate drift versus directional selection**, define biological units, sampling frame, time coordinate and outcome variables. Write the competing hypotheses as distinct predictions: Distinguish a distribution of allele-frequency trajectories generated by drift from a consistent directional shift expected under a simple selection model. A generic statement that 'evolution occurs' is not a testable outcome.
2. Assemble the synthetic input table and verify totals. For counts, check whether each observation represents an individual, gene copy, fossil occurrence or independent lineage. For traits, specify scale and units. Leave missing observations explicitly missing rather than silently substituting zero.
3. Produce a first visualization with individual values visible when practical. Include replicates, not only a pooled mean. Label assumptions, treatment groups and what uncertainty is shown; error bars without a stated definition are ambiguous.
4. Recalculate the outcome after changing one defensible assumption: sampling effort, effective size, migration, branch rate or measurement error, as appropriate. The change in conclusion is a sensitivity result, not a failure of the exercise.
5. Write a short report separating observation, model, interpretation and limitation. Include a figure caption, a reproducibility note and one proposed independent test.

### Expected reasoning, not prescribed results

Under neutral Wright–Fisher sampling, expected mean signed change across many runs is approximately zero while among-run variance is greater at smaller Ne. In this synthetic scenario, some individual neutral runs will look directional or even lose an allele; selection runs also vary when sampling is added. Resist presenting a single calculated value as the only outcome consistent with the mechanism. Explain what a failed prediction would require you to reconsider: an incorrect method, an unrealistic assumption or a genuinely unsupported biological hypothesis. Negative results are informative when sampling was capable of detecting the predicted difference.

### Troubleshooting the inference

Before assigning a causal mechanism, check whether the data come from comparable cohorts, whether drift is credible for the effective size and whether migration or laboratory batch effects could reproduce the observation. Pseudoreplication is a major threat when multiple measurements from one biological unit are treated as independent organisms or populations. Similarly, sampling several fossils from one well-exposed outcrop may not represent equal coverage across geological intervals. Identify the true replication unit and justify the comparator. If simulations use the same seed or parameter configuration, discuss whether the apparently repeated outcome is truly independent.

### Submission and further questions

Submit a hypothesis table, methods summary, results figure with labeled axes, numerical worked example, explanation of assumptions and a 150-word limitations statement. Which summaries require replicate trajectories rather than one observed line? For extension, describe one observation that would distinguish the leading hypothesis from a realistic competing mechanism, and state how much uncertainty would remain even if that observation agreed with the prediction.


## End-of-unit integrative assessment

1. Construct a concept map linking **Allele frequencies and Hardy–Weinberg reasoning** and **Natural selection and relative fitness**. Each connecting arrow must be labeled with a measurable or historically constrained mechanism, not a vague phrase such as 'related to'. Include at least one causal hypothesis and one statement of historical relationship.
2. Contrast **Mutation as the source of new variants** with **Gene flow and population structure**. Describe a plausible observational pattern compatible with both, then design a new measurement that would make their predictions diverge. State your relevant biological unit and justify how many independent replicates you would need for a preliminary test.
3. Reproduce all five solved quantitative cases from this unit without viewing their answers. Change one parameter in each case, label units and explain whether the biological conclusion is sensitive to the change. A model calculation is not a field observation.
4. Evaluate a hypothetical paper claiming that **genetic drift and effective population size** has been conclusively demonstrated from a small unreplicated dataset. Draft a respectful scientific response explaining the most serious limitation, a rival mechanism, and a feasible next step.
5. Prepare a 600-word mini-review integrating chronology or inheritance, mechanism and evidence for two topics of your choice. Define your terminology precisely, distinguish observed data from inferred history and cite a credible external scientific source. Close with a statement of what remains unknown.

**Self-check rubric for this unit.** When writing about **allele frequencies and hardy–weinberg reasoning** or **genetic drift and effective population size**, identify a defined population or lineage, give a defensible observation, show appropriate units or character coding and distinguish the leading hypothesis from a competitor. Evaluation rewards testable reasoning and candid limitations rather than memorization of a favored interpretation.

