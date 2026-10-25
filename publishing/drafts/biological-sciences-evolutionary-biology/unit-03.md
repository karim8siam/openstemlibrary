# Unit 03: Adaptation, plasticity and experimental evolution

> Analyzing context-dependent fitness, constraints, genetic response and experimental design.

## Learning outcomes

By the end of this unit, the reader should be able to investigate adaptation, plasticity and experimental evolution, interpret a relevant quantitative model, design a realistic test that controls for alternative explanations, and state the principal limits of the inference. An intellectually satisfactory answer can remain uncertain when the data do not discriminate among mechanisms.

## Integrative foundation

### Why 'best adapted' must include a question mark

No organism occupies an environment that remains fully constant across every location, developmental stage or generation. A phenotype that promotes survival against one predator may reduce reproductive success under another; a physiological adjustment that protects from heat may consume resources needed for reproduction. When comparing adaptation, specify the relevant fitness measure, the stage at which it is measured and the range of environments studied. Statements such as 'a longer beak is better' become scientific only after the relevant food sources, energetic costs and hereditary basis have been established.

The difference between plasticity and evolution is especially important in rapid environmental change. An individual can alter behavior or gene expression as temperature rises, but that observation alone is not inherited population change. A reaction norm shows how the same genotype's phenotype varies across environments. If different genotypes have different slopes, selection may favor plasticity itself, though costs and unreliable environmental cues can constrain the result. Repeated measurements of one genotype across environments answer a different question from a comparison of two genotypes in a single environment.

### Constraints and paths through genotype space

Fitness-landscape imagery can help students reason about local outcomes, provided the metaphor is not mistaken for a literal map of every possible genome. Nearby mutational states may differ in effect depending on genetic background. An allele beneficial in an ancestor can become harmful after additional changes; this is a form of epistasis. Some theoretical paths to higher fitness are inaccessible without an intermediate genotype that selection disfavors, yet drift, environmental fluctuations, recombination or different starting alleles may alter available pathways. Physical design constraints also matter. A body structure inherited from ancestors cannot be replaced instantaneously by an unrelated ideal architecture.

Trade-offs are not just stories about limited energy. To demonstrate a trade-off, measure the competing traits within a suitable design and rule out simple differences in overall resource access or age. If vigorous individuals both grow faster and reproduce more, a positive correlation does not disprove that each individual faces an allocation constraint. Conversely, a negative correlation might arise from a hidden ecological variable rather than direct resource competition. A manipulation that selectively increases investment in one function, followed by measurement of costs elsewhere, can provide stronger evidence when conducted ethically.

### Experimental evolution as an inference engine

Well-designed selection experiments are powerful because the researcher controls the environment and retains replicate populations and reference ancestors. Replication allows the investigator to ask whether similar phenotypic improvements recur while molecular routes differ. Archived ancestors can be revived for comparable assays in suitable supervised laboratory settings. In a classroom, computational lineages and simulated trait distributions can demonstrate principles without handling microorganisms. Whatever the system, a control population should experience the same bottlenecks and culture conditions except for the focal selection treatment.

Finally, quantitative genetic predictions such as R=h²S are conditional short-term approximations. The additive variance available to selection may decrease, genetic correlations can redirect responses, and the environment may change the phenotype without altering genotypes. A successful estimate reports what was selected, how heritability was obtained, and why the model's assumptions are plausible for the relevant generation. That precision is more useful than calling a trait 'genetically determined'.

## Focused studies and worked problems

### 3.1 Fitness landscapes and changing environments

#### Core idea and causal mechanism

Adaptation is a process of evolutionary change that increases relative performance under particular conditions, not a permanent certificate that a trait is best in all environments.

Genotype-by-environment interactions alter fitness rankings; epistasis means the effect of an allele depends on genetic background. Selection may track a moving optimum, and drift can occasionally cross fitness valleys in small populations.

#### Example in biological context

A coat coloration that improves concealment on dark rocks may expose animals on pale sand. Even within one habitat a trait favored during one season might be disadvantageous in another.

#### Evidence and a workable test

Create reaction norms by measuring genotype performance across temperatures or habitats; compare rank changes and confidence intervals rather than naming one genotype universally adapted.

**Investigation prompt.** Specify at least two environments in which the focal phenotype might experience different benefits or costs, and identify the measured endpoint that would make the comparison fair. A changed phenotype is not by itself an inherited change.

#### Where the inference could fail

Laboratory growth rates may not capture natural competition or reproduction. Fitness landscapes are conceptual or statistical models, and their peaks depend on which genotypes and environments are included.

Use a common-garden or reciprocal-environment design when feasible. Explain how an environmental induction, a genetic difference or their interaction could all generate a visible phenotypic pattern.

#### Apply and question

Draw a two-environment fitness table with a rank reversal and ask whether one best genotype exists. Compare the difference between plastic adjustment within a lifetime and inherited change between generations.

Forecasting evolution under warming conditions requires repeated environmental measurements and tracking of standing variation, not simple projection of today's winner.

Can selection favor a phenotype that remains below the environmental optimum? Discuss mutation supply, genetic correlations, lag and limited population size. Your answer should include a prediction that differs between hypotheses and state which assumptions would remain untested after the observation.

#### Quantitative case 3.1: Relative fitness in contrasting habitats

**Assumed data (synthetic).** Two genotypes have fitnesses 1.1 and 0.8 on dark substrate but 0.7 and 1.2 on pale substrate.

**Calculation.** Compute the favored genotype's advantage in the dark habitat as a ratio. Substituting the stipulated values into `1.1/0.8` gives **1.375 fitness ratio**. Confirm the result independently and retain consistent units.

**Interpretation.** The first type is favored in one environment, but the ranking reverses in the other; there is no universal winner.

**Model limitation.** Assumed fitness ratios ignore frequency-dependent predation and habitat switching.

**Try next.** If habitats are equally occupied, what extra assumptions are needed before averaging these fitness values? Show the derivation and distinguish the numerical result from any proposed biological cause.


### 3.2 Trade-offs and evolutionary constraints

#### Core idea and causal mechanism

A benefit in one dimension can impose a cost in another; constraints arise from development, history, pleiotropy, physical laws and limits on available genetic variants.

Increased seed provisioning can reduce the number of seeds made, while larger ornaments can improve mating success but elevate predation risk. Selection optimizes relative reproductive contribution subject to feasible combinations, not engineering perfection.

#### Example in biological context

A seabird's wing morphology participates in both underwater propulsion and aerial travel; improvement in one context may limit efficiency in the other. Historical modifications provide the starting architecture for later adaptation.

#### Evidence and a workable test

Measure at least two performance variables and reproduction across a range of trait values. Control for total resource acquisition so that an apparent trade-off is not simply variation in individual quality.



#### Where the inference could fail

A negative correlation does not by itself prove a resource trade-off; uncontrolled age or condition can reverse associations. Experimental manipulations help, but may create artificial costs.



#### Apply and question

Sketch a Pareto frontier of attainable outcomes and identify one phenotype that is dominated and one that is efficient but not universally preferred. Explicitly label the assumed environment.

Trade-off analysis is used in fisheries, agricultural breeding, evolutionary robotics and conservation management because selection on one trait can have unintended consequences.

If the best survivor produces few offspring, is it 'fittest'? Explain why survival is one component of reproductive fitness and why age-specific reproduction matters. Your answer should include a prediction that differs between hypotheses and state which assumptions would remain untested after the observation.

#### Quantitative case 3.2: Performance trade-off

**Assumed data (synthetic).** An individual makes 12 offspring at 0.55 expected survival each versus 8 offspring at 0.85 expected survival each.

**Calculation.** For the first option calculate expected surviving offspring from fecundity times survival. Substituting the stipulated values into `12*0.55` gives **6.6 offspring**. Confirm the result independently and retain consistent units.

**Interpretation.** Expected output is 6.6, compared with 6.8 for the second option; sheer offspring number is not the fitness criterion.

**Model limitation.** Later descendant reproduction and uncertainty may alter the ranking.

**Try next.** What if the first strategy reproduces two years sooner than the second? Show the derivation and distinguish the numerical result from any proposed biological cause.


### 3.3 Phenotypic plasticity and reaction norms

#### Core idea and causal mechanism

Phenotypic plasticity allows one genotype to produce different phenotypes under different environments. Plastic responses can be adaptive, neutral or maladaptive, and they need not involve inherited allele-frequency change.

Environmental signals alter gene expression and development; costs of sensing and switching, imperfect environmental cues and developmental irreversibility shape reaction norms. Plasticity can expose or hide genetic variation from selection.

#### Example in biological context

Aquatic organisms can develop alternative defenses in response to predator cues. Seasonal shifts in pigmentation or timing may similarly be environmentally induced without immediate genetic divergence.

#### Evidence and a workable test

Grow genetically comparable individuals across a factorial environmental design, record reaction norms, and ask whether lines differ in slope as well as intercept. Where feasible, rear a second generation in a shared environment.



#### Where the inference could fail

One-generation environmental inheritance and maternal effects can mimic some genetic differences. The word 'adaptation' should not be inferred just because a plastic response is visually impressive.



#### Apply and question

Draw two crossing reaction norms and identify genotype-by-environment interaction. Explain why selection on slope might differ from selection on trait value in a constant environment.

Crop breeding and climate-resilience studies benefit from reaction norms because field performance depends on both genetic stock and environmental variability.

When rapid climate change exceeds the range of prior cues, how could formerly useful plasticity become mismatched? Propose a measurable test. Your answer should include a prediction that differs between hypotheses and state which assumptions would remain untested after the observation.

#### Quantitative case 3.3: Reaction-norm slope

**Assumed data (synthetic).** Trait value is 15 at 20°C and 27 at 30°C for a particular genotype.

**Calculation.** Slope equals response change divided by environmental difference. Substituting the stipulated values into `(27-15)/(30-20)` gives **1.2 trait units per °C**. Confirm the result independently and retain consistent units.

**Interpretation.** The slope estimates plastic sensitivity over the sampled range, not necessarily a genetic evolutionary response.

**Model limitation.** Extrapolating linearly beyond the temperatures studied may be misleading.

**Try next.** How could a second genotype cross this reaction norm despite having a lower value at 20°C? Show the derivation and distinguish the numerical result from any proposed biological cause.


### 3.4 Experimental evolution and selection lines

#### Core idea and causal mechanism

Experimental evolution tracks heritable population changes under controlled, replicated conditions, permitting sharper causal tests than many historical comparisons.

Replicate lineages, pre-registered outcomes and archived ancestors allow researchers to compare genetic and phenotypic trajectories. Populations can discover different molecular routes to similar phenotypes, and some changes may reflect laboratory adaptation.

#### Example in biological context

Microbial cultures exposed to a new carbon source may improve growth over many transfers. A parallel unexposed control is needed to determine whether the change is specific to the treatment.

#### Evidence and a workable test

Plan an experiment with independent biological replicates, common-garden assays and whole-genome sampling at fixed generations. Use an unchanged ancestral strain to quantify improvement in comparable conditions.



#### Where the inference could fail

Contamination, cross-transfer among replicates, plate effects and accumulated benign mutations can distort inference. One winning lineage does not establish repeatability or generality.



#### Apply and question

Specify the unit of replication and a selection regime that can be reproduced. Compare a fitness assay performed during selection with one performed after several transfers in a shared environment.

Experimental evolution can test resistance costs and ecological trade-offs, but pathogen work requires trained laboratories and biosafety oversight; classroom simulations are safer for introductory settings.

If five lines show improved growth but carry different mutations, what conclusions are supported about repeatable phenotypes and repeated molecular mechanisms? Your answer should include a prediction that differs between hypotheses and state which assumptions would remain untested after the observation.

#### Quantitative case 3.4: Experimental fitness relative to ancestor

**Assumed data (synthetic).** A selected lineage grows 1.42-fold as fast in a standardized assay compared with an ancestral reference at 1.00.

**Calculation.** Compute percentage increase over ancestral value. Substituting the stipulated values into `100*(1.42-1)` gives **42 percent**. Confirm the result independently and retain consistent units.

**Interpretation.** A 42-percent difference in this assay is not automatically a 42-percent increase in natural reproductive fitness.

**Model limitation.** Assay transfer conditions and measurement uncertainty could change the result.

**Try next.** Which common-garden controls would be necessary to attribute the change to heritable evolutionary responses? Show the derivation and distinguish the numerical result from any proposed biological cause.


### 3.5 Quantitative traits and response to selection

#### Core idea and causal mechanism

Continuous traits often depend on many loci and environments. The breeder's equation R=h²S predicts a short-term response under restrictive assumptions about additive genetic variance and stable conditions.

Selection differential S is the difference between selected parents and the original population mean; narrow-sense heritability h² is the additive genetic fraction of phenotypic variance in a specified population and environment.

#### Example in biological context

A plant breeding program selects earlier-flowering parents. Their offspring may shift in mean flowering date, but the shift can differ across soil and temperature regimes.

#### Evidence and a workable test

Estimate parent-offspring response in a controlled breeding design, correct for environmental blocks and track genetic correlations with traits such as growth and reproduction.



#### Where the inference could fail

Heritability is not a fixed property of a trait or a percentage of a person's characteristic explained by genes; selection changes variance over time. The simple equation is not a long-term guarantee.



#### Apply and question

Compute R for several hypothetical heritability values while keeping selection differential constant. Explain why large S may still yield small R if additive genetic variation is limited.

Quantitative genetics informs crops, livestock and conservation interventions, but selection on correlated traits can undermine broad ecological performance.

What data would reveal that a breeding response plateau reflects genetic constraints rather than a ceiling in laboratory measurement? Your answer should include a prediction that differs between hypotheses and state which assumptions would remain untested after the observation.

#### Quantitative case 3.5: Breeder's equation response

**Assumed data (synthetic).** Hypothetical narrow-sense heritability is 0.35; selection differential S=8 millimeters.

**Calculation.** Use R=h²S for the predicted one-generation trait-mean change. Substituting the stipulated values into `0.35*8` gives **2.8 millimeters**. Confirm the result independently and retain consistent units.

**Interpretation.** Prediction 2.8 mm holds only under the approximate assumptions of this simple model.

**Model limitation.** Heritability and selection differential may shift each generation.

**Try next.** What correlated traits would you measure to check whether directional selection causes another fitness cost? Show the derivation and distinguish the numerical result from any proposed biological cause.


## Integrated investigation 3: Testing a plastic response against a genetic response

**Research aim.** Measure an invented temperature-associated trait across two genotypes and three environments, using a full factorial design. The investigation is designed for an introductory undergraduate seminar or computational laboratory; its specimens, dates, counts and measurements are hypothetical. Do not represent any result as a published empirical discovery.

### Materials, assumptions and ethical boundaries

Three temperature treatments, multiple independently generated individuals per genotype, randomized environmental chambers and repeated measurements with known instrument resolution. Use a spreadsheet or local script to create tables and plots, recording pseudorandom seeds if stochastic simulations are used. Collect no personal genetic data. Do not culture pathogens, collect protected wildlife, disturb habitats or undertake medical tests. Where the real-world analog requires permits, trained staff or ethical approval, use simulation or openly available teaching data instead.

### Step-by-step procedure

1. For **testing a plastic response against a genetic response**, define biological units, sampling frame, time coordinate and outcome variables. Write the competing hypotheses as distinct predictions: Measure an invented temperature-associated trait across two genotypes and three environments, using a full factorial design. A generic statement that 'evolution occurs' is not a testable outcome.
2. Assemble the synthetic input table and verify totals. For counts, check whether each observation represents an individual, gene copy, fossil occurrence or independent lineage. For traits, specify scale and units. Leave missing observations explicitly missing rather than silently substituting zero.
3. Produce a first visualization with individual values visible when practical. Include replicates, not only a pooled mean. Label assumptions, treatment groups and what uncertainty is shown; error bars without a stated definition are ambiguous.
4. Recalculate the outcome after changing one defensible assumption: sampling effort, effective size, migration, branch rate or measurement error, as appropriate. The change in conclusion is a sensitivity result, not a failure of the exercise.
5. Write a short report separating observation, model, interpretation and limitation. Include a figure caption, a reproducibility note and one proposed independent test.

### Expected reasoning, not prescribed results

Genotypes may show different reaction-norm slopes; offspring in a common environment are needed to test inherited differences after parental treatments. In this synthetic scenario, the warm chamber gives larger values for every group, but the between-genotype difference remains stable in one treatment and reverses in another. Resist presenting a single calculated value as the only outcome consistent with the mechanism. Explain what a failed prediction would require you to reconsider: an incorrect method, an unrealistic assumption or a genuinely unsupported biological hypothesis. Negative results are informative when sampling was capable of detecting the predicted difference.

### Troubleshooting the inference

Describe the ecological conditions that make the proposed advantage valuable and at least one setting in which the advantage might shrink or reverse. Adaptation claims should expose costs, opportunity constraints and measurement stages. Pseudoreplication is a major threat when multiple measurements from one biological unit are treated as independent organisms or populations. Similarly, sampling several fossils from one well-exposed outcrop may not represent equal coverage across geological intervals. Identify the true replication unit and justify the comparator. If simulations use the same seed or parameter configuration, discuss whether the apparently repeated outcome is truly independent.

### Submission and further questions

Submit a hypothesis table, methods summary, results figure with labeled axes, numerical worked example, explanation of assumptions and a 150-word limitations statement. How does a genotype-by-environment interaction alter the meaning of a single heritability estimate? For extension, describe one observation that would distinguish the leading hypothesis from a realistic competing mechanism, and state how much uncertainty would remain even if that observation agreed with the prediction.


## End-of-unit integrative assessment

1. Construct a concept map linking **Fitness landscapes and changing environments** and **Phenotypic plasticity and reaction norms**. Each connecting arrow must be labeled with a measurable or historically constrained mechanism, not a vague phrase such as 'related to'. Include at least one causal hypothesis and one statement of historical relationship.
2. Contrast **Trade-offs and evolutionary constraints** with **Quantitative traits and response to selection**. Describe a plausible observational pattern compatible with both, then design a new measurement that would make their predictions diverge. State your relevant biological unit and justify how many independent replicates you would need for a preliminary test.
3. Reproduce all five solved quantitative cases from this unit without viewing their answers. Change one parameter in each case, label units and explain whether the biological conclusion is sensitive to the change. A model calculation is not a field observation.
4. Evaluate a hypothetical paper claiming that **experimental evolution and selection lines** has been conclusively demonstrated from a small unreplicated dataset. Draft a respectful scientific response explaining the most serious limitation, a rival mechanism, and a feasible next step.
5. Prepare a 600-word mini-review integrating chronology or inheritance, mechanism and evidence for two topics of your choice. Define your terminology precisely, distinguish observed data from inferred history and cite a credible external scientific source. Close with a statement of what remains unknown.

**Self-check rubric for this unit.** When writing about **fitness landscapes and changing environments** or **experimental evolution and selection lines**, identify a defined population or lineage, give a defensible observation, show appropriate units or character coding and distinguish the leading hypothesis from a competitor. Evaluation rewards testable reasoning and candid limitations rather than memorization of a favored interpretation.

