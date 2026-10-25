# Unit 04: Speciation and hybridization

> From divided breeding populations to complex boundaries, gene exchange and new lineages.

## Learning outcomes

By the end of this unit, the reader should be able to investigate speciation and hybridization, interpret a relevant quantitative model, design a realistic test that controls for alternative explanations, and state the principal limits of the inference. An intellectually satisfactory answer can remain uncertain when the data do not discriminate among mechanisms.

## Integrative foundation

### Species boundaries are data-rich problems

A species can be treated as an independently evolving lineage, but the observations used to recognize that lineage differ dramatically among bacteria, flowering plants, sexually reproducing animals and fossil forms. A biological-species assessment based on reproductive isolation is informative where actual mating and offspring performance can be studied, yet it does not transfer directly to asexual organisms. A diagnosable genomic cluster can assist delimitation, but stable clusters depend on how extensively populations and environments have been sampled. Taxonomy summarizes evidence at a time; it should allow evidence-driven correction rather than presenting every label as an eternal natural boundary.

Divergence is likewise not a single-step event. Two populations may become ecologically different, then alter mate preferences, then diverge across more of their genomes. Alternatively, a geographic barrier may reduce migration and chance drift may initiate some differences long before any strong reproductive barriers exist. A model may therefore track several variables: gene flow, ecological performance, mating probability, hybrid fitness and temporal stability. A sharp shift in one variable does not imply that all other boundaries are complete.

### Layers of isolation

When studying potential reproductive isolation, specify the sequential opportunities for genetic exchange. Individuals must first meet, then attempt mating or pollen transfer, then achieve fertilization, then produce descendants capable of further reproduction. An investigator measuring only hybrid sterility skips the barriers that operate earlier in nature. Conversely, an investigator counting few hybrids may misdiagnose a biological incompatibility if parental lineages simply occupy different seasons or habitats. Conditional-probability diagrams make the problem clearer: success at a late stage must be multiplied by the probability of reaching that stage.

Not all reproductive barriers evolve because selection favors isolation directly. Geographic separation can allow differences to accumulate as by-products; later contact can reveal incompatibilities. Ecological adaptation can decrease migrant performance, even before a strongly assortative mate preference evolves. Reinforcement is a particular hypothesis in which selection against hybridization can favor stronger prezygotic isolation in contact regions. To test it, researchers must distinguish the effects of reinforcement from ecological sorting and differences in opportunities to mate.

### Hybridization as a process, not a verdict

Hybridization can weaken boundaries, maintain a narrow contact zone, allow useful alleles to move between lineages or contribute to hybrid speciation under particular conditions. The genome is not always represented by one clean tree. Interspecific gene flow generates reticulate histories, especially for some plant, fish and microbial groups. However, a few conflicting gene trees do not prove hybridization, because ancestral alleles can persist and sort differently across descendant lineages. Synteny, chromosome behavior, genomic tract lengths and spatial sampling may discriminate explanations.

A careful species account therefore states what organism and data motivated the chosen species concept, which populations were sampled, whether gene flow was quantified and what evidence limits the confidence of delimitation. The goal is not to force every borderline case into two named boxes but to make predictions about independently evolving populations that can be revisited.

## Focused studies and worked problems

### 4.1 Biological and phylogenetic species concepts

#### Core idea and causal mechanism

Species delimitation depends on the evidence and organisms being studied. Reproductive isolation works well for many sexual taxa, while lineage-based, ecological and diagnosable-character concepts handle other cases.

Persistent separation of breeding pools can allow independent evolutionary trajectories, but asexual reproduction, fossil taxa and hybridization complicate simple definitions. Genealogical patterns often differ among loci shortly after divergence.

#### Example in biological context

Some flowering plants exchange pollen across named species while retaining strong habitat differences. Bacteria may show ecological lineages despite horizontal gene transfer, requiring an explicitly different operational strategy.

#### Evidence and a workable test

Collect genomic, ecological, reproductive and geographic data, and examine whether conclusions are stable under different sampling decisions and species criteria.

**Investigation prompt.** Identify contact, mating, fertilization, hybrid survival and later fertility as distinct conditional stages. Estimate which stage contributes most to the reduction in gene exchange, using a consistent denominator.

#### Where the inference could fail

A universal barcode threshold does not define species, and labels can change with richer evidence. Cryptic species may differ without visible morphology, while within-species variation can be substantial.

Compare one geographic account of divergence with an ecological account and explain which datasets could discriminate them. Speciation is an evolving process rather than a timestamp observed directly.

#### Apply and question

Construct two delimitation hypotheses for populations with low genetic distance but strong mating barriers. Give an observation that would weaken each hypothesis.

Conservation law and biodiversity inventories often require names, but uncertain taxonomy should be documented rather than disguised as a precise count.

Could two well-defined species exchange genes? Explain why occasional introgression does not automatically collapse all biological boundaries. Your answer should include a prediction that differs between hypotheses and state which assumptions would remain untested after the observation.

#### Quantitative case 4.1: Genetic differentiation

**Assumed data (synthetic).** Allele frequency at a chosen marker is 0.15 in region A and 0.61 in region B.

**Calculation.** Calculate the absolute allele-frequency difference. Substituting the stipulated values into `abs(0.61-0.15)` gives **0.46 frequency difference**. Confirm the result independently and retain consistent units.

**Interpretation.** The descriptive gap does not itself specify how many species exist or whether there is current reproductive isolation.

**Model limitation.** Markers with unusual selection can overstate genome-wide divergence.

**Try next.** Would many independent loci and mate-choice data change the interpretation? Show the derivation and distinguish the numerical result from any proposed biological cause.


### 4.2 Allopatric divergence and geographic barriers

#### Core idea and causal mechanism

Allopatric speciation begins with geographic separation that reduces gene flow, permitting drift, selection and mutation to drive divergence in different places.

Barrier formation can occur by mountain uplift, river rearrangement, sea-level change or habitat fragmentation. The timing of reduced connectivity, not simply the present-day map, matters for proposed historical explanations.

#### Example in biological context

Separated populations of freshwater fish may experience different prey, temperatures and predators after a river drainage shifts. Their genetic divergence can persist even if partial contact returns.

#### Evidence and a workable test

Compare genomic divergence with geological reconstructions, sample contact zones and estimate migration under appropriate demographic models. Alternative outcomes include convergence or renewed gene flow.



#### Where the inference could fail

Sequence divergence alone is not evidence that a geographic barrier caused it; distance isolation and different effective population sizes also shape genetic patterns.



#### Apply and question

Draw a timeline with barrier emergence, expected reduction in gene flow, local adaptations and possible secondary contact. Identify which elements are directly observed.

Infrastructure barriers may create evolutionary isolation today, making corridor design a population-genetic issue as well as a demographic one.

If populations become different while still connected by migrants, what evidence would show that geography was not the only cause? Your answer should include a prediction that differs between hypotheses and state which assumptions would remain untested after the observation.

#### Quantitative case 4.2: Time since a barrier

**Assumed data (synthetic).** A geological scenario places barrier formation at 2.8 million years before present and contact at 0.7 million years before present.

**Calculation.** Subtract the date of renewed contact from the date of initial isolation. Substituting the stipulated values into `2.8-0.7` gives **2.1 million years**. Confirm the result independently and retain consistent units.

**Interpretation.** A putative 2.1-million-year separation offers a timeline to test, not proof that isolation was complete throughout it.

**Model limitation.** Geological dates and molecular divergence estimates have different uncertainties.

**Try next.** What observations would distinguish persistent dispersal across the barrier from a clean allopatric split? Show the derivation and distinguish the numerical result from any proposed biological cause.


### 4.3 Ecological speciation and assortative mating

#### Core idea and causal mechanism

Divergent ecological selection can contribute to reproductive isolation when adaptation to different niches reduces mating between groups or offspring fitness in alternative habitats.

Habitat choice, mating signals linked to ecological traits and immigrant inviability may couple selection to reduced gene exchange. The relative contribution of ecological and sexual mechanisms must be tested.

#### Example in biological context

In a hypothetical lake, fish specialized to shallow vegetation may encounter mates and spawn separately from deep-water feeders. The ecological split could predate genetic mate preferences or follow them.

#### Evidence and a workable test

Measure habitat use, reciprocal performance, mate choice under shared conditions, and gene flow across ecological transitions. Manipulate available habitat when ethically feasible without disrupting wild populations.



#### Where the inference could fail

Different diets in sympatry do not by themselves prove speciation; plasticity or seasonal competition can generate similar observations. A hybrid zone may persist despite partial isolation.



#### Apply and question

Propose an experiment that decouples habitat preference from mate recognition. State predictions under a sensory-choice model and an environmental-performance model.

Understanding ecological speciation informs adaptive radiation and explains why habitat homogenization might collapse previously divergent lineages.

Can reproductive isolation strengthen after secondary contact? Explain reinforcement and why its evidence requires excluding ecological sorting alone. Your answer should include a prediction that differs between hypotheses and state which assumptions would remain untested after the observation.

#### Quantitative case 4.3: Habitat-assortative mating

**Assumed data (synthetic).** Of 240 mating events observed, 192 occurred among individuals using the same habitat type.

**Calculation.** Divide within-habitat matings by the total sampled events. Substituting the stipulated values into `100*192/240` gives **80 percent**. Confirm the result independently and retain consistent units.

**Interpretation.** Eighty percent within-habitat pairing does not by itself prove an inherited preference; encounters may be strongly habitat-structured.

**Model limitation.** Unequal group numbers can produce high within-group mating by chance.

**Try next.** Compute a chance expectation under equal group sizes and compare it with observations. Show the derivation and distinguish the numerical result from any proposed biological cause.


### 4.4 Prezygotic and postzygotic reproductive barriers

#### Core idea and causal mechanism

Reproductive isolation can arise before fertilization, through behavior or gamete incompatibility, or after fertilization through reduced hybrid survival or fertility.

Temporal and spatial separation reduce encounters; mechanical and gametic incompatibilities reduce fertilization. Hybrid dysfunction can arise from negative interactions among divergent gene products, chromosome differences or ecological maladaptation.

#### Example in biological context

Flowering plants that bloom in different seasons may rarely hybridize even when ranges overlap. In other cases hybrid seeds form but germinate poorly in the parental habitats.

#### Evidence and a workable test

Measure each barrier sequentially: encounter probability, mating probability, fertilization, offspring viability, and fertility. Report total isolation without double-counting overlapping barriers.



#### Where the inference could fail

A low hybrid count may reflect rare encounters rather than intrinsic incompatibility. Controlled crosses can isolate one mechanism but may not represent behavior or ecology in nature.



#### Apply and question

Build a staged probability tree for reproduction across populations and explain why multiplying conditional success probabilities avoids adding incompatible percentages.

Barrier diagnosis helps understand crop introgression and conservation of distinct breeding populations without equating all hybrids with ecological harm.

What happens if hybrids thrive in an intermediate habitat while remaining rare in either parental habitat? Distinguish intrinsic from environment-dependent isolation. Your answer should include a prediction that differs between hypotheses and state which assumptions would remain untested after the observation.

#### Quantitative case 4.4: Layered reproductive barriers

**Assumed data (synthetic).** Cross-population encounters occur in 0.60 of potential pairs and gametic compatibility is 0.35 conditional on encounter.

**Calculation.** Multiply stage-specific success probabilities. Substituting the stipulated values into `0.60*0.35` gives **0.21 combined probability**. Confirm the result independently and retain consistent units.

**Interpretation.** An expected 0.21 reaches fertilization in this simplified staged model; later hybrid survival can reduce effective exchange further.

**Model limitation.** Conditional probabilities must be measured on appropriate denominators and stages.

**Try next.** What is the correct new product if postzygotic survival is 0.5? Show the derivation and distinguish the numerical result from any proposed biological cause.


### 4.5 Hybridization, introgression and polyploidy

#### Core idea and causal mechanism

Hybridization is not simply failure of speciation; it can transfer alleles between lineages, create stable hybrid zones and occasionally contribute to new species formation.

Repeated backcrossing can introgress a genomic region across a species boundary. In plants, whole-genome duplication can sometimes restore fertility after hybridization and produce a rapid reproductive barrier.

#### Example in biological context

Adaptive introgression may introduce a beneficial variant into a population while most genomic regions remain differentiated. Some polyploid plant lineages differ reproductively from diploid relatives through chromosome pairing constraints.

#### Evidence and a workable test

Combine genome-wide ancestry analyses with ecological performance assays and chromosome counts where appropriate. Compare candidate introgressed regions against background demographic structure.



#### Where the inference could fail

An unusual genealogical tree might reflect incomplete lineage sorting rather than introgression. Mixed-ancestry genomes are not proof that hybrids are fitter or represent a newly formed species.



#### Apply and question

Sketch crosses among two diploid lineages and a potential polyploid lineage, then state why fertility predictions depend on chromosome pairing and not merely the number of parents.

Hybridization matters for threatened species management, crop breeding and pathogen evolution, but translocations should not proceed from a simplistic 'more mixing is always good' assumption.

How could introgression and incomplete lineage sorting generate similar gene trees, and what patterns across many linked loci might help distinguish them? Your answer should include a prediction that differs between hypotheses and state which assumptions would remain untested after the observation.

#### Quantitative case 4.5: Introgressed ancestry fraction

**Assumed data (synthetic).** A toy population genome summary assigns 17 percent of ancestry to an introgressing lineage.

**Calculation.** Calculate the percentage of non-introgressed ancestry. Substituting the stipulated values into `100-17` gives **83 percent**. Confirm the result independently and retain consistent units.

**Interpretation.** The 83-percent remainder is merely a classification under a particular ancestry model, not a taxonomic purity claim.

**Model limitation.** Model choice, reference populations and recombination affect ancestry fractions.

**Try next.** Why can a specific advantageous allele introgress even when mean genome-wide ancestry remains low? Show the derivation and distinguish the numerical result from any proposed biological cause.


## Integrated investigation 4: Diagnosing reproductive isolation in a contact zone

**Research aim.** Disentangle poor encounter rates from fertilization incompatibility and hybrid offspring failure across hypothetical populations. The investigation is designed for an introductory undergraduate seminar or computational laboratory; its specimens, dates, counts and measurements are hypothetical. Do not represent any result as a published empirical discovery.

### Materials, assumptions and ethical boundaries

Data on 200 possible cross-population encounters, mating attempts, fertilizations, offspring survival and adult fertility with conditional denominators. Use a spreadsheet or local script to create tables and plots, recording pseudorandom seeds if stochastic simulations are used. Collect no personal genetic data. Do not culture pathogens, collect protected wildlife, disturb habitats or undertake medical tests. Where the real-world analog requires permits, trained staff or ethical approval, use simulation or openly available teaching data instead.

### Step-by-step procedure

1. For **diagnosing reproductive isolation in a contact zone**, define biological units, sampling frame, time coordinate and outcome variables. Write the competing hypotheses as distinct predictions: Disentangle poor encounter rates from fertilization incompatibility and hybrid offspring failure across hypothetical populations. A generic statement that 'evolution occurs' is not a testable outcome.
2. Assemble the synthetic input table and verify totals. For counts, check whether each observation represents an individual, gene copy, fossil occurrence or independent lineage. For traits, specify scale and units. Leave missing observations explicitly missing rather than silently substituting zero.
3. Produce a first visualization with individual values visible when practical. Include replicates, not only a pooled mean. Label assumptions, treatment groups and what uncertainty is shown; error bars without a stated definition are ambiguous.
4. Recalculate the outcome after changing one defensible assumption: sampling effort, effective size, migration, branch rate or measurement error, as appropriate. The change in conclusion is a sensitivity result, not a failure of the exercise.
5. Write a short report separating observation, model, interpretation and limitation. Include a figure caption, a reproducibility note and one proposed independent test.

### Expected reasoning, not prescribed results

A product of conditional success probabilities represents the total success path only when stages are correctly ordered and definitions aligned. In this synthetic scenario, a high failure rate after mating can be overshadowed by even stronger pre-mating habitat separation. Resist presenting a single calculated value as the only outcome consistent with the mechanism. Explain what a failed prediction would require you to reconsider: an incorrect method, an unrealistic assumption or a genuinely unsupported biological hypothesis. Negative results are informative when sampling was capable of detecting the predicted difference.

### Troubleshooting the inference

A report should specify the population concept, the geographic extent and the sample dates. Show how uncertain migration or hybrid viability changes the conclusion instead of hiding borderline observations. Pseudoreplication is a major threat when multiple measurements from one biological unit are treated as independent organisms or populations. Similarly, sampling several fossils from one well-exposed outcrop may not represent equal coverage across geological intervals. Identify the true replication unit and justify the comparator. If simulations use the same seed or parameter configuration, discuss whether the apparently repeated outcome is truly independent.

### Submission and further questions

Submit a hypothesis table, methods summary, results figure with labeled axes, numerical worked example, explanation of assumptions and a 150-word limitations statement. Which barrier is most important in nature, and which is easiest to measure in captivity? For extension, describe one observation that would distinguish the leading hypothesis from a realistic competing mechanism, and state how much uncertainty would remain even if that observation agreed with the prediction.


## End-of-unit integrative assessment

1. Construct a concept map linking **Biological and phylogenetic species concepts** and **Ecological speciation and assortative mating**. Each connecting arrow must be labeled with a measurable or historically constrained mechanism, not a vague phrase such as 'related to'. Include at least one causal hypothesis and one statement of historical relationship.
2. Contrast **Allopatric divergence and geographic barriers** with **Hybridization, introgression and polyploidy**. Describe a plausible observational pattern compatible with both, then design a new measurement that would make their predictions diverge. State your relevant biological unit and justify how many independent replicates you would need for a preliminary test.
3. Reproduce all five solved quantitative cases from this unit without viewing their answers. Change one parameter in each case, label units and explain whether the biological conclusion is sensitive to the change. A model calculation is not a field observation.
4. Evaluate a hypothetical paper claiming that **prezygotic and postzygotic reproductive barriers** has been conclusively demonstrated from a small unreplicated dataset. Draft a respectful scientific response explaining the most serious limitation, a rival mechanism, and a feasible next step.
5. Prepare a 600-word mini-review integrating chronology or inheritance, mechanism and evidence for two topics of your choice. Define your terminology precisely, distinguish observed data from inferred history and cite a credible external scientific source. Close with a statement of what remains unknown.

**Self-check rubric for this unit.** When writing about **biological and phylogenetic species concepts** or **prezygotic and postzygotic reproductive barriers**, identify a defined population or lineage, give a defensible observation, show appropriate units or character coding and distinguish the leading hypothesis from a competitor. Evaluation rewards testable reasoning and candid limitations rather than memorization of a favored interpretation.

