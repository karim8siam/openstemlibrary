# Unit 03 — Species interactions and community dynamics

> Analyze competition, consumption, mutualism, food webs and succession as demographic mechanisms.

## Learning goals

For species interactions and community dynamics, explain the processes described in this unit, identify suitable observational and experimental units, connect synthetic numerical cases to physical measurements, and distinguish competing mechanisms. In the context of analyze competition, consumption, mutualism, food webs and succession as demographic mechanisms., state how variation in sampling effort, habitat, time or model assumptions could change the result. Interpret quantities with units and identify the evidence required before applying results to a real management decision.

## Conceptual foundation

### Communities as networks of demographic consequences

Community ecology examines more than the number of species in one place. It asks how populations influence one another's survival, reproduction, behavior and access to resources. Shared resources can generate competition; predators alter prey mortality and movement; mutualistic partners exchange resources or services; ecosystem engineers change habitat structure for many other species. An interaction named from one experiment is not necessarily constant across time. A fungus can help a plant obtain limiting nutrients, yet the benefit may vanish or become costly when those nutrients are supplied externally. A predatory fish can strongly reduce a prey species in an open pond but have little effect where vegetation provides refuge.

To establish competition, researchers distinguish association from causation. Two plant species may rarely co-occur because one tolerates drought and the other prefers moist soils, without exerting much direct competitive pressure. A removal experiment can ask whether a focal species grows or reproduces better when its neighbor is absent, but removal itself can alter soil temperature, light exposure or disturbance. Appropriate controls and environmental measurements matter. The competitive-exclusion principle pertains to particular assumptions about stable environments and limiting factors; it should not be paraphrased as a universal impossibility of coexistence between species that appear similar.

Predation operates through consumption and through risk. A prey animal may avoid profitable feeding habitat in the presence of predators and suffer reduced growth even if few individuals are killed. A field study that records only carcasses will miss that pathway. In consumer-resource models, a functional response relates individual feeding to prey density, while a numerical response describes changes in consumer abundance. Both shape population trajectories. Classic two-species cycles are useful thought experiments but ignore alternative prey, immigration, seasonality and age structure. Their purpose in an introductory course is to identify mechanisms that can produce oscillation, not to guarantee a sinusoidal field pattern.

Indirect interactions make food webs harder to summarize. A predator may suppress a grazer and allow algae to increase; another predator may suppress that first predator; a nutrient pulse may increase algal growth even without any change in grazer pressure. Thus the observation that algae expanded after predator arrival cannot by itself establish a trophic cascade. Experiments that measure multiple levels, diet and resource availability offer better support. The phrase keystone species is most useful when a disproportionate ecological effect is demonstrated relative to the organism's abundance and ecological context. It is not a permanent rank assigned to a species in every location.

Community assembly also contains history. The first colonists to reach a disturbed patch may alter conditions for later arrivals; this can be tested by changing arrival order under comparable environments. Some sequences favor facilitation, where early species improve conditions for successors. Others show inhibition, where established species block later recruitment, or tolerance, where later species endure conditions independent of early occupants. Real succession need not approach a single stable endpoint, especially when disturbance, dispersal and climate continue changing. Permanent plots and experiments are stronger than interpreting separately aged sites as if every difference reflected elapsed time.

For every community pattern, ask three linked questions. What was actually observed: abundance, occupancy, cover, feeding, survival or reproduction? Which causal mechanism could produce it? What rival explanation predicts a different result when a variable is manipulated or measured independently? Those questions keep community ecology from becoming an inventory of relationships and support quantitative work on diversity and ecosystem functioning.

## Five focused topics with worked examples

### 3.1 Competition and resource partitioning

#### Ecological concept and mechanism

Individuals and species interact indirectly through shared resources and directly through interference. Coexistence depends on how competition within species compares with competition between species, plus spatial and temporal variation.

Resource depletion limits growth; aggressive exclusion changes access; different rooting depths, phenology or diet may lower overlap. Apparent niche separation can arise after historical sorting, not necessarily ongoing adaptive divergence.

#### Worked interpretive case

Two grass species overlap when nutrients are abundant but segregate across soil depths during drought. Removing one species could reveal competition concealed by environmental sorting.

#### Evidence and study design

Use a factorial removal experiment across moisture levels, measuring per-capita performance and starting densities. Replace disturbed biomass in controls if removal changes soil exposure.

Propose evidence that would distinguish competitive exclusion from different physiological tolerances in neighboring plant patches.

#### Critical limitations and transfer

Observed negative association is not sufficient evidence of competition: unmeasured environmental differences can create the same pattern. Experimental removals may also alter disturbance or herbivory.

Competition theory connects individual uptake traits to long-term coexistence only through explicit demographic consequences.

#### Worked quantitative example 3.1: Competition intensity proxy

**Synthetic data.** A paired experiment records a focal plant's mean biomass of 15 grams alone and 12 grams alongside a competitor under otherwise matched synthetic conditions.

**Derivation and solution.** Estimate fractional suppression relative to the without-competitor baseline. The explicit calculation `(15-12)/15` gives **0.2 fractional biomass suppression**. Identify how the input variables were defined before applying the same arithmetic to new measurements; the result is conditional on that definition.

**Ecological interpretation.** A twenty percent relative difference is consistent with competition but not a mechanistic measurement of resource depletion.

**When the computation would mislead.** Poor randomization, transplant damage or altered shade could generate differences without resource competition. For field applications, compare the precision of the input measurements with the apparent precision of the answer, then decide whether model structure or sampling error is likely to dominate uncertainty.

**Independent check and extension.** Add water or nutrients factorially and predict how a resource-mediated interaction should change. Recalculate with one altered input and describe the observation that would justify changing that parameter in a real ecological study. Distinguish recalculating an illustrative equation from experimentally validating the biological relationship.


### 3.2 Predation and consumer-resource feedbacks

#### Ecological concept and mechanism

Predators, herbivores and parasites affect prey abundance and behavior, while prey supply regulates consumer populations. Consumption can propagate through food webs as well as direct encounters.

Functional responses relate feeding rate to prey density; numerical responses concern predator reproduction or aggregation. Refuges and prey vigilance alter effective encounter rates and can stabilize or destabilize cycles.

#### Worked interpretive case

Small fish use shallow vegetation when larger piscivores are present. Their reduced feeding may reflect fear even without increased mortality, shifting effects to zooplankton.

#### Evidence and study design

Measure encounter rates, diet, prey survival and habitat use separately. Compare predator-access and predator-exclusion treatments with cage artifacts checked by partial cages.

Explain why a lower prey count after predator introduction cannot alone quantify consumption mortality.

#### Critical limitations and transfer

Lotka–Volterra cycles are conceptual benchmarks, not reliable predictions for every field system. Temperature and alternate prey may change predator behavior independently.

Food-web reasoning must include nonconsumptive behavior and time lags rather than a single arrow in a diagram.

#### Worked quantitative example 3.2: Saturating consumption rate

**Synthetic data.** A conceptual consumer encounters prey density N=80; encounter coefficient is a=0.05 and handling time h=0.2 in internally consistent units.

**Derivation and solution.** Evaluate a type-II functional response aN/(1+ahN). The explicit calculation `0.05*80/(1+0.05*0.2*80)` gives **2.22222 prey per consumer per model time**. Identify how the input variables were defined before applying the same arithmetic to new measurements; the result is conditional on that definition.

**Ecological interpretation.** The calculated rate is limited by handling time as prey becomes abundant.

**When the computation would mislead.** The model assumes one prey type, stable encounter conditions and a fixed consumer state. For field applications, compare the precision of the input measurements with the apparent precision of the answer, then decide whether model structure or sampling error is likely to dominate uncertainty.

**Independent check and extension.** Graph feeding rate over N=0–200 and contrast its shape to a linear response. Recalculate with one altered input and describe the observation that would justify changing that parameter in a real ecological study. Distinguish recalculating an illustrative equation from experimentally validating the biological relationship.


### 3.3 Mutualism, facilitation and conditional outcomes

#### Ecological concept and mechanism

Interactions can benefit both partners, but the net effect of a relationship depends on resource supply, partner identity and environmental stress. Positive effects should be measured against a relevant no-partner alternative.

Mycorrhizal fungi exchange nutrient access for plant carbon, pollinators trade visits for resources, and nurse plants can shelter seedlings while also competing for water. Costs and benefits change as conditions vary.

#### Worked interpretive case

A hypothetical legume gains biomass with rhizobial partners in nitrogen-poor soil but not after nitrogen addition. Symbiosis presence alone does not establish a net growth benefit.

#### Evidence and study design

Compare inoculated and uninoculated plants under low and high nitrogen using verified partner establishment. Track resource transfer or nutrient status instead of interpreting biomass as direct proof of exchange.

Specify a factorial design that can reveal whether mutualism strengthens during stress or instead collapses.

#### Critical limitations and transfer

A greenhouse response may not generalize to the field where competing microbes, grazing and abiotic stress interact. A partner may switch from beneficial to costly.

Recognizing conditional interactions avoids treating ecological relationships as fixed moral categories.

#### Worked quantitative example 3.3: Context-dependent mutualism gain

**Synthetic data.** A two-by-two trial yields partner and no-partner biomass means of 24 and 15 grams under low nitrogen and 19 and 16 grams under high nitrogen.

**Derivation and solution.** Subtract the two within-nutrient partner effects and then compare them as an interaction contrast. The explicit calculation `(24-15)-(19-16)` gives **6 grams of differential partner effect**. Identify how the input variables were defined before applying the same arithmetic to new measurements; the result is conditional on that definition.

**Ecological interpretation.** The interaction contrast of six grams indicates a stronger partner association under low nitrogen in this synthetic experiment.

**When the computation would mislead.** Biomass means need replicate-level variability, controls and confirmation that partners established. For field applications, compare the precision of the input measurements with the apparent precision of the answer, then decide whether model structure or sampling error is likely to dominate uncertainty.

**Independent check and extension.** Describe what would change if high nitrogen reduced partner establishment instead of reducing benefit from partnership. Recalculate with one altered input and describe the observation that would justify changing that parameter in a real ecological study. Distinguish recalculating an illustrative equation from experimentally validating the biological relationship.


### 3.4 Food webs, indirect effects and keystone roles

#### Ecological concept and mechanism

A food web is a network of feeding interactions whose consequences depend on interaction strengths, species abundance and alternative pathways. A species may have a disproportionate effect relative to its biomass.

A consumer can reduce prey, release competing prey or change producer abundance through trophic cascades. Omnivory, compensatory responses and spatial refuges can buffer expected cascades.

#### Worked interpretive case

Removal of a dominant grazer increases algae in some pools but not others because nutrient limitation and replacement grazers vary. The absence of a cascade is informative about network context.

#### Evidence and study design

Measure multiple trophic levels before and after manipulations with control sites. Identify energy pathways using diets or tracers where feasible and acknowledge isotopic mixing uncertainties.

Compare the expected consequence of removing a predator with that of removing the system's primary nutrient source.

#### Critical limitations and transfer

A dramatic response to removal does not prove a species is universally keystone. Food webs reconstructed solely from presence may exaggerate realized interactions.

Network diagrams become explanatory only when paired with rates or experimentally supported relationships.

#### Worked quantitative example 3.4: Grazer removal effect

**Synthetic data.** Mean producer cover is 80 percent of available substrate in grazer exclusions and 50 percent under grazer access.

**Derivation and solution.** Compute the relative difference using the exclusion mean as reference. The explicit calculation `(80-50)/80` gives **0.375 proportional cover reduction**. Identify how the input variables were defined before applying the same arithmetic to new measurements; the result is conditional on that definition.

**Ecological interpretation.** The 37.5 percent reduction is an illustrative grazer-access contrast, not a direct consumption rate.

**When the computation would mislead.** Cages may shade substrate, alter flow or exclude organisms other than target grazers. For field applications, compare the precision of the input measurements with the apparent precision of the answer, then decide whether model structure or sampling error is likely to dominate uncertainty.

**Independent check and extension.** Design a partial-cage control and explain how the percentage is sensitive to its reference denominator. Recalculate with one altered input and describe the observation that would justify changing that parameter in a real ecological study. Distinguish recalculating an illustrative equation from experimentally validating the biological relationship.


### 3.5 Community assembly, succession and disturbance

#### Ecological concept and mechanism

Communities reflect dispersal, environmental filtering, species interactions, historical contingency and disturbance. Succession may alter species composition, but there is no universal mandatory climax endpoint.

Colonists change light, soils or propagule arrival; disturbances open space and redistribute resources. Priority effects occur when early arrivals influence later colonists, sometimes producing alternative trajectories.

#### Worked interpretive case

Two abandoned fields with similar soils develop different early plant communities because one retained seed banks and the other received introduced pasture species.

#### Evidence and study design

Establish repeated permanent plots and document land-use history. Compare trait composition, recruitment and turnover; use manipulations of arrival order to test priority effects.

Construct rival predictions for facilitation, inhibition and tolerance during recovery after a storm.

#### Critical limitations and transfer

Chronosequences substitute space for time and can confound site age with management or soil differences. Disturbance magnitude and frequency must be defined.

Succession studies require a time series or well-justified replacement, not merely a photograph of older vegetation.

#### Worked quantitative example 3.5: Jaccard community overlap

**Synthetic data.** Two before-and-after species lists have five taxa in the first period, four in the second, and two shared taxa.

**Derivation and solution.** Jaccard similarity equals shared richness divided by union richness. The explicit calculation `2/(5+4-2)` gives **0.285714 shared fraction of pooled taxa**. Identify how the input variables were defined before applying the same arithmetic to new measurements; the result is conditional on that definition.

**Ecological interpretation.** About 0.286 similarity indicates notable turnover of incidence lists.

**When the computation would mislead.** Seasonal detectability and inconsistent taxonomy can create apparent turnover without genuine colonization or loss. For field applications, compare the precision of the input measurements with the apparent precision of the answer, then decide whether model structure or sampling error is likely to dominate uncertainty.

**Independent check and extension.** Give the corresponding dissimilarity and compare it to abundance-weighted change. Recalculate with one altered input and describe the observation that would justify changing that parameter in a real ecological study. Distinguish recalculating an illustrative equation from experimentally validating the biological relationship.


## Integrated computational and observation-design laboratory 3: Community assembly with paired exclusions

### Research aim and study system

Assign eight artificial pond mesocosms in matched blocks to grazer access or exclusion and record algae cover, grazer counts and light. This is an educational, entirely synthetic exercise for readers without laboratory equipment. Its case is **pond food-web manipulation**, represented by **matched mesocosms with submerged plants, algae, grazers and fish**. The key quantities to observe are **consumer access and producer cover**. The question is not simply whether two columns differ: it is whether the chosen evidence can **separate direct consumption from behavioral shifts and nutrient effects**. State the central alternative before generating any synthetic measurements. Otherwise changes in a plot can be explained after the fact without a meaningful test.

### Data dictionary and reproducibility requirements

Provide one row per actual study unit or visit, depending on the stage of measurement, and include explicit identifiers. Document **mesocosm as experimental unit**; also retain location class, date, survey duration, method version and a reason when data are missing. Define every unit, including degrees of temperature, area, individual counts or mass-per-time flux. Use distinct codes for zero, unobserved and not applicable. A table in which no organisms were seen despite valid sampling is not equivalent to a table in which a site was never visited. Save a read-only raw dataset and a second transformed dataset alongside a reproducible calculation log.

The book contains a synthetic example dataset for this unit under `datasets/lab-03.csv`. It illustrates a stable column structure rather than empirical evidence; its numerical values and site labels are invented. Review whether the input data are logically coherent before fitting any equation. A physically impossible concentration or a date outside the sampling window should trigger validation. Record any corrected values and preserve the originals so another reader can explain every change.

### Procedure

1. **Specify hypotheses.** Choose one explanatory process drawn from **competition and resource partitioning** and a serious competing explanation related to **mutualism, facilitation and conditional outcomes**. Describe the response variable and whether the process predicts an increase, decrease, threshold or no change. Include a null pattern that could plausibly arise through sampling variation.
2. **Establish comparability.** Match sites, periods, effort or experimental units appropriately. If the study uses simulated random assignment, preserve the random seed and show treatment balance. Do not treat several measurements from one habitat block as independent blocks. Explain how space, time and shared weather might introduce dependence even under a seemingly random scheme.
3. **Explore the data.** Construct a scatterplot or time series with labeled axes, raw points and explicit group names. Report sample size at the actual experimental or observational-unit level. Inspect non-detections and extreme values, but do not delete observations solely because they contradict the initial hypothesis.
4. **Calculate and compare.** Analyze treatment effects at the mesocosm level and compare behavioral and consumptive explanations. Check arithmetic using two methods—a spreadsheet and a manual calculation, for example. Explain what part of the comparison was identified by a definition and what part required a model assumption. A graph that looks smooth does not demonstrate the validity of a causal pathway.
5. **Stress-test the conclusion.** Change one defensible parameter or data-quality rule: detection probability, sampling area, rate assumption, autocorrelation or reference choice. Recompute the principal estimate. If a moderate alteration reverses the sign or action threshold, present both outcomes and recommend improved measurement before a high-cost decision.
6. **Interpret with an alternative.** Compare the leading mechanism with the explicitly named rival. Propose a new independent measurement that would discriminate them. Include uncertainty and an ethical or logistical limitation. If results are inconsistent, label the result unresolved instead of inventing an unobserved pathway to rescue a favorite hypothesis.

### Results discussion and expected reasoning

The exercise contains no prespecified discovery. Its purpose is to make plausible ecological stories answerable through measurements. Explain how **predation and consumer-resource feedbacks** may affect a predicted outcome while **food webs, indirect effects and keystone roles** can change the interpretation. Where the calculation involves probability, distinguish conditional probabilities from frequencies over repeated independent systems. Where a budget is calculated, distinguish flow rates from stocks and sum only compatible quantities. Where a management action is proposed, separate the number of actions implemented from the measured response of the ecosystem.

All species and treatments are hypothetical; physical organism use would require institutional approval. Report the synthetic status prominently. If a model produces an impossible value, do not silently truncate it unless the modeling rule explicitly requires a bound. Instead identify the biological restriction omitted by the simple equation. Some ecological systems can have alternative stable trajectories or long lag times, but neither should be claimed from the dataset without specific evidence.

### Deliverables, assessment and extension

Submit an annotated data dictionary, an analysis script or spreadsheet formula log, two labeled figures, one complete hand-worked numerical calculation and a one-page discussion with prediction, result, competing explanation and limitation. Include a paragraph on reproducibility and any constraints on safe field transfer. For extension, choose **community assembly, succession and disturbance** as a new potential driver and design a minimally more informative follow-up study. Explain the number and kind of genuinely independent replicates that would be needed for a small pilot, rather than declaring arbitrary sample sizes statistically adequate.


## Unit 3 synthesis and critical assessment

1. **Mechanism map.** Relate Competition and resource partitioning to Food webs, indirect effects and keystone roles. Mark the measured processes, their directions and the place where a biological outcome could be changed by an unobserved driver. Show two different indirect pathways from a predator to a producer.
2. **Rival explanation.** A report concludes that predation and consumer-resource feedbacks must be responsible for a mapped pattern. Identify an environmental or measurement-based alternative, an observation consistent with both, and an independent comparison that could distinguish them.
3. **Quantitative audit.** Reconstruct all five examples in this unit without looking at the displayed result. Check units and dimensions, identify the reference value, and vary an input by ten percent. Record the effect size and the meaning of a negative, zero or unexpected result where applicable.
4. **Evidence review.** Examine a hypothetical study with four sites, two of them treated and two untreated, where investigators repeated twenty subsamples at every site. Explain why there are four independent site-level units, then discuss what additional temporal and spatial controls would strengthen the inference. Adjust the explanation if treatment spills between adjacent sites.
5. **Transfer and limits.** Design a community experiment that can distinguish resource competition from abiotic habitat selection. Draft a concise comparison of how the model's assumptions change when moved from the constructed teaching scenario to a coastal, urban, agricultural or protected-area system. Explicitly indicate which ecological outcomes need long-term monitoring.
6. **Research communication.** Write a 500-word mini-review of two concepts from the unit, distinguishing established general mechanisms from synthetic calculations and uncertain real-world consequences. Cite at least one reliable open textbook or scientific reference, and state exactly which claim the reading supports. An external reference is not an endorsement of the OpenSTEM draft.

