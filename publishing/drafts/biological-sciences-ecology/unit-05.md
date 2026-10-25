# Unit 05 — Biodiversity and biogeography

> Compare richness, turnover, functional traits, species-area patterns and invasions.

## Learning goals

For biodiversity and biogeography, explain the processes described in this unit, identify suitable observational and experimental units, connect synthetic numerical cases to physical measurements, and distinguish competing mechanisms. In the context of compare richness, turnover, functional traits, species-area patterns and invasions., state how variation in sampling effort, habitat, time or model assumptions could change the result. Interpret quantities with units and identify the evidence required before applying results to a real management decision.

## Conceptual foundation

### Biodiversity is not one statistic

Biodiversity refers to variation across genes, species, traits, ecological roles and landscapes. Species richness is the simplest count but answers only one question. A community with one very abundant species and five extremely rare species has the same richness as another with six similarly abundant species; their dominance patterns and susceptibility to losing uncommon species differ. Evenness and abundance-sensitive indices offer complementary descriptions. Shannon entropy responds to proportional abundances, while Gini-Simpson diversity has a direct interpretation in terms of the chance that two independent draws belong to different species under its assumptions. Neither index measures ecosystem health by itself.

Sampling affects all diversity measures. Rare organisms can remain undetected when effort is low or identification requires particular seasons. Comparing a morning transect in one habitat with three full-day surveys in another will usually confound real ecological differences with effort. Rarefaction and sample-coverage concepts help place unequal samples on a more defensible basis, but they rely on their own assumptions and cannot manufacture observations of unsampled habitats. A rich dataset retains detection methods and taxonomic decisions, not merely the final index.

Beta diversity addresses how composition varies among sites. Suppose two wetlands each support ten identified taxa, but they share only two: richness alone conceals large compositional turnover. Another pair might share all ten species while differing in dominance. Incidence and abundance measures answer different questions. Turnover can be related to dispersal barriers, habitat filtering, disturbances or stochastic histories, but the numerical dissimilarity does not establish which process caused it. Studies should compare a hypothesis about movement limitation with one about environmental differences using independent evidence.

Functional biodiversity attempts to connect organisms' traits to processes such as resource uptake, decomposition or pollination. Leaf economics, rooting depth, body size and feeding guilds may be ecologically informative, yet many traits are plastic or vary within species. An abundance-weighted community mean can change because a dominant species expands even when every species retains its average trait. A functional diversity index can rise without producing more biomass if light, water or nutrients are the limiting constraints. Mechanistic hypotheses are needed to move from a trait table to a process explanation.

Biogeography introduces scale and history. Species-area relationships summarize the tendency to detect more taxa across larger areas, but the exponent depends on whether areas are nested samples, independent fragments or islands with differing colonization opportunities. Habitat heterogeneity, isolation and effort all matter. It is not justified to multiply a fitted species-area relation far beyond the observed range and claim a precise number of extinctions or conservation gains. The pattern remains valuable when used comparatively and when model scope is made explicit.

Range expansion and biological invasion are additional ecological problems where categories can outrun evidence. A species present outside its historical native range is not automatically proven ecologically harmful at every site. A convincing impact assessment measures changes in recipient communities or processes with plausible controls, not simply the invader's increasing occupancy. Propagule pressure, disturbance, climatic suitability and enemy communities are candidates for explaining spread. Management should consider proportionality, ecological side effects and the legal protection of people and non-target species. Good biodiversity science defines the metric, sampling frame, process hypothesis and management aim independently.

## Five focused topics with worked examples

### 5.1 Species richness, evenness and diversity metrics

#### Ecological concept and mechanism

Richness counts species while evenness describes how abundances are distributed; different diversity indices emphasize common or rare species differently. Sampling effort must be comparable before interpreting change.

Shannon entropy weights proportional abundances logarithmically, while Simpson-type metrics emphasize dominance. Rarefaction and coverage estimation address incomplete observation rather than biological absence.

#### Worked interpretive case

A restored meadow contains the same number of detected plant species as a heavily grazed meadow, but one is dominated by a single grass whereas the other has more balanced cover.

#### Evidence and study design

Use equal survey effort or sample-coverage methods, identify organisms consistently, and examine how conclusions vary between richness and effective numbers of species.

Compute Simpson diversity for a three-species example and explain why it cannot measure ecological function by itself.

#### Critical limitations and transfer

Indices derived from relative cover are not interchangeable with organism counts. Unequal detectability of flowering and nonflowering plants can bias seasonal comparisons.

Biodiversity arguments should specify whether the goal concerns richness, community composition, functional traits or persistence.

#### Worked quantitative example 5.1: Simpson diversity

**Synthetic data.** A synthetic three-species community has relative abundances 0.6, 0.3 and 0.1, which sum to one.

**Derivation and solution.** Use Gini-Simpson diversity: 1 minus the sum of squared relative abundances. The explicit calculation `1-(0.6**2+0.3**2+0.1**2)` gives **0.54 Gini-Simpson index**. Identify how the input variables were defined before applying the same arithmetic to new measurements; the result is conditional on that definition.

**Ecological interpretation.** The result 0.54 quantifies the chance two independent draws belong to different species under this model.

**When the computation would mislead.** Sampling without replacement slightly changes small-community interpretations, and richness alone cannot be inferred. For field applications, compare the precision of the input measurements with the apparent precision of the answer, then decide whether model structure or sampling error is likely to dominate uncertainty.

**Independent check and extension.** Find the index for three equal abundances and explain the direction of change. Recalculate with one altered input and describe the observation that would justify changing that parameter in a real ecological study. Distinguish recalculating an illustrative equation from experimentally validating the biological relationship.


### 5.2 Beta diversity and community turnover

#### Ecological concept and mechanism

Beta diversity concerns differences in species composition among sampling locations or times. Similar turnover scores may arise from species replacement or nested subsets of richer communities.

Dispersal barriers, environmental heterogeneity and historical processes shape turnover. Incidence measures emphasize occurrence while abundance-weighted measures change with dominance.

#### Worked interpretive case

Two wetlands contain equal richness but no species in common, while two others share most species but differ greatly in abundance. A single richness statistic cannot distinguish them.

#### Evidence and study design

Calculate Jaccard dissimilarity from matched incidence lists, then repeat with a suitable abundance metric. Check survey timing and taxonomic resolution.

Compare beta diversity before and after habitat homogenization and propose a null expectation based on regional species frequencies.

#### Critical limitations and transfer

Nestedness and turnover partitioning methods depend on metric choice; mathematical components should not automatically be assigned unique ecological causes.

Conservation planning often values complementarity between sites rather than selecting sites solely by their individual richness.

#### Worked quantitative example 5.2: Between-site dissimilarity

**Synthetic data.** One wetland has five taxa, another four, and only two occur in both species lists.

**Derivation and solution.** Jaccard dissimilarity equals 1 minus intersection divided by the union. The explicit calculation `1-2/(5+4-2)` gives **0.714286 Jaccard dissimilarity**. Identify how the input variables were defined before applying the same arithmetic to new measurements; the result is conditional on that definition.

**Ecological interpretation.** Approximately 0.714 reflects dissimilar occurrence lists across the two sites.

**When the computation would mislead.** Low survey effort or seasonal absence can inflate dissimilarity despite similar underlying communities. For field applications, compare the precision of the input measurements with the apparent precision of the answer, then decide whether model structure or sampling error is likely to dominate uncertainty.

**Independent check and extension.** Compare incidence-based dissimilarity to a Bray-Curtis calculation if abundances are available. Recalculate with one altered input and describe the observation that would justify changing that parameter in a real ecological study. Distinguish recalculating an illustrative equation from experimentally validating the biological relationship.


### 5.3 Functional traits and ecosystem processes

#### Ecological concept and mechanism

Traits such as seed mass, leaf chemistry, body size or feeding mode can connect organisms to resource use and ecosystem functioning. Functional diversity can change while species counts appear stable.

Complementarity may increase resource capture across niches, but a dominant species with a strongly expressed trait can determine a measured process. Correlated traits reflect both adaptation and shared ancestry.

#### Worked interpretive case

A grassland replacement of deep-rooted perennial plants with shallow-rooted annuals may alter water uptake even when richness is unchanged.

#### Evidence and study design

Measure a defined process such as soil infiltration or peak-season productivity, sample traits at comparable life stages and analyze abundance-weighted trait distributions.

Identify an intervention or natural experiment that can separate diversity effects from fertilization or rainfall differences.

#### Critical limitations and transfer

A trait correlated with ecosystem output is not automatically causal. Environment drives both species sorting and ecosystem rates, generating confounding.

Functional ecology needs a mechanistic pathway between measured traits and measured processes, not an assumption that more diversity always improves every function.

#### Worked quantitative example 5.3: Abundance-weighted trait mean

**Synthetic data.** A community has two hypothetical plant functional groups with leaf lengths 10 and 20 centimeters, weighted by relative cover 0.2 and 0.8.

**Derivation and solution.** Compute the weighted mean trait across the two groups. The explicit calculation `0.2*10+0.8*20` gives **18 centimeters**. Identify how the input variables were defined before applying the same arithmetic to new measurements; the result is conditional on that definition.

**Ecological interpretation.** The community-weighted leaf length is 18 centimeters, dominated by the common group.

**When the computation would mislead.** Cover is not interchangeable with individual frequency or biomass; the weighting choice affects interpretation. For field applications, compare the precision of the input measurements with the apparent precision of the answer, then decide whether model structure or sampling error is likely to dominate uncertainty.

**Independent check and extension.** Replace relative cover with individual numbers and state when the two methods might disagree. Recalculate with one altered input and describe the observation that would justify changing that parameter in a real ecological study. Distinguish recalculating an illustrative equation from experimentally validating the biological relationship.


### 5.4 Biogeography and species-area relationships

#### Ecological concept and mechanism

Larger sampled areas often contain more species, but the species-area pattern depends on habitat heterogeneity, isolation, geographic scale and sampling completeness. Islands also expose colonization-extinction dynamics.

Adding area may increase individual numbers and habitat types; increasing isolation can reduce arrival; past disturbances and regional species pools modify the local assemblage.

#### Worked interpretive case

A cluster of small habitat fragments contains more habitat types than one uniform patch of the same area, challenging an area-only prediction.

#### Evidence and study design

Plot richness against area using consistent surveys, compare habitat diversity and isolation, and fit a model with an explicit scope. Distinguish a nested sampling curve from independent-island comparisons.

Estimate predicted richness at doubled area under S=cA^z while emphasizing the assumed scale and habitat context.

#### Critical limitations and transfer

Extrapolation from a handful of sites to entire continents is fragile; the exponent of a power-law fit is not a universal ecological constant.

Reserve design combines area with complementarity, edge effects, connectivity and real species requirements.

#### Worked quantitative example 5.4: Species-area extrapolation

**Synthetic data.** A constructed species-area model estimates 15 taxa at unit reference area and specifies exponent z=0.25; area then doubles.

**Derivation and solution.** Calculate predicted richness multiplier as area ratio raised to z. The explicit calculation `15*2**0.25` gives **17.8381 predicted taxa**. Identify how the input variables were defined before applying the same arithmetic to new measurements; the result is conditional on that definition.

**Ecological interpretation.** Roughly 17.84 is a continuous model expectation, not a directly observed integer species count.

**When the computation would mislead.** Predictions assume comparable habitat and a stable species pool; extrapolation beyond measured range is uncertain. For field applications, compare the precision of the input measurements with the apparent precision of the answer, then decide whether model structure or sampling error is likely to dominate uncertainty.

**Independent check and extension.** Compare predictions when z=0.15 and z=0.4 and explain why patch quality still matters. Recalculate with one altered input and describe the observation that would justify changing that parameter in a real ecological study. Distinguish recalculating an illustrative equation from experimentally validating the biological relationship.


### 5.5 Invasion ecology and range expansion

#### Ecological concept and mechanism

A nonnative species may establish, spread and affect ecosystems, but introduction alone does not prove harm. Ecological impacts vary with propagule pressure, disturbance, enemy communities and recipient ecosystem properties.

High propagule supply increases opportunities for establishment; disturbance can open resources; biotic interactions regulate spread. An invader's effect can include competition, predation, habitat modification or pathogen transmission.

#### Worked interpretive case

An ornamental plant appears along roadsides but remains scarce inside intact forests; road maintenance and dispersal may explain the boundary better than broad climate suitability.

#### Evidence and study design

Map abundance over repeated seasons along gradients of disturbance and distance from introduction points. Where possible compare matched invaded and uninvaded plots while considering prior conditions.

Frame a decision between early detection, containment and long-term management using impact evidence and feasibility.

#### Critical limitations and transfer

Before-after effects can be confounded if invaded places were already degraded. Eradication actions have costs, off-target effects and legal constraints.

Responsible invasion assessments distinguish range expansion, ecological effect and the justification for specific control methods.

#### Worked quantitative example 5.5: Short-term range expansion

**Synthetic data.** The number of invented occupied cells on a monitoring grid increases from 20 to 26 between matched surveys.

**Derivation and solution.** Relative change equals later minus earlier divided by the earlier count. The explicit calculation `(26-20)/20` gives **0.3 fractional expansion**. Identify how the input variables were defined before applying the same arithmetic to new measurements; the result is conditional on that definition.

**Ecological interpretation.** A thirty percent increase in occupied cells may represent spread, greater detection or changed grid effort.

**When the computation would mislead.** Occupied area does not quantify ecological harm, and reclassification of boundary cells can create spurious change. For field applications, compare the precision of the input measurements with the apparent precision of the answer, then decide whether model structure or sampling error is likely to dominate uncertainty.

**Independent check and extension.** Design independent ecological impact measurements rather than inferring effect from expansion rate. Recalculate with one altered input and describe the observation that would justify changing that parameter in a real ecological study. Distinguish recalculating an illustrative equation from experimentally validating the biological relationship.


## Integrated computational and observation-design laboratory 5: Turnover and trait change with stable richness

### Research aim and study system

Create four six-species samples in which dominance changes and one species is replaced while total richness stays constant. This is an educational, entirely synthetic exercise for readers without laboratory equipment. Its case is **paired habitat biodiversity assessment**, represented by **two hypothetical grasslands and two adjacent wetlands under different management**. The key quantities to observe are **species incidence, relative cover and trait composition**. The question is not simply whether two columns differ: it is whether the chosen evidence can **distinguish richness changes from turnover or abundance redistribution**. State the central alternative before generating any synthetic measurements. Otherwise changes in a plot can be explained after the fact without a meaningful test.

### Data dictionary and reproducibility requirements

Provide one row per actual study unit or visit, depending on the stage of measurement, and include explicit identifiers. Document **sampling effort and taxonomic identification**; also retain location class, date, survey duration, method version and a reason when data are missing. Define every unit, including degrees of temperature, area, individual counts or mass-per-time flux. Use distinct codes for zero, unobserved and not applicable. A table in which no organisms were seen despite valid sampling is not equivalent to a table in which a site was never visited. Save a read-only raw dataset and a second transformed dataset alongside a reproducible calculation log.

The book contains a synthetic example dataset for this unit under `datasets/lab-05.csv`. It illustrates a stable column structure rather than empirical evidence; its numerical values and site labels are invented. Review whether the input data are logically coherent before fitting any equation. A physically impossible concentration or a date outside the sampling window should trigger validation. Record any corrected values and preserve the originals so another reader can explain every change.

### Procedure

1. **Specify hypotheses.** Choose one explanatory process drawn from **species richness, evenness and diversity metrics** and a serious competing explanation related to **functional traits and ecosystem processes**. Describe the response variable and whether the process predicts an increase, decrease, threshold or no change. Include a null pattern that could plausibly arise through sampling variation.
2. **Establish comparability.** Match sites, periods, effort or experimental units appropriately. If the study uses simulated random assignment, preserve the random seed and show treatment balance. Do not treat several measurements from one habitat block as independent blocks. Explain how space, time and shared weather might introduce dependence even under a seemingly random scheme.
3. **Explore the data.** Construct a scatterplot or time series with labeled axes, raw points and explicit group names. Report sample size at the actual experimental or observational-unit level. Inspect non-detections and extreme values, but do not delete observations solely because they contradict the initial hypothesis.
4. **Calculate and compare.** Calculate richness, Gini-Simpson index, Jaccard dissimilarity and a weighted functional trait mean. Check arithmetic using two methods—a spreadsheet and a manual calculation, for example. Explain what part of the comparison was identified by a definition and what part required a model assumption. A graph that looks smooth does not demonstrate the validity of a causal pathway.
5. **Stress-test the conclusion.** Change one defensible parameter or data-quality rule: detection probability, sampling area, rate assumption, autocorrelation or reference choice. Recompute the principal estimate. If a moderate alteration reverses the sign or action threshold, present both outcomes and recommend improved measurement before a high-cost decision.
6. **Interpret with an alternative.** Compare the leading mechanism with the explicitly named rival. Propose a new independent measurement that would discriminate them. Include uncertainty and an ethical or logistical limitation. If results are inconsistent, label the result unresolved instead of inventing an unobserved pathway to rescue a favorite hypothesis.

### Results discussion and expected reasoning

The exercise contains no prespecified discovery. Its purpose is to make plausible ecological stories answerable through measurements. Explain how **beta diversity and community turnover** may affect a predicted outcome while **biogeography and species-area relationships** can change the interpretation. Where the calculation involves probability, distinguish conditional probabilities from frequencies over repeated independent systems. Where a budget is calculated, distinguish flow rates from stocks and sum only compatible quantities. Where a management action is proposed, separate the number of actions implemented from the measured response of the ecosystem.

Species lists must reflect consistent identification and comparable effort; treat invented occurrences as teaching data. Report the synthetic status prominently. If a model produces an impossible value, do not silently truncate it unless the modeling rule explicitly requires a bound. Instead identify the biological restriction omitted by the simple equation. Some ecological systems can have alternative stable trajectories or long lag times, but neither should be claimed from the dataset without specific evidence.

### Deliverables, assessment and extension

Submit an annotated data dictionary, an analysis script or spreadsheet formula log, two labeled figures, one complete hand-worked numerical calculation and a one-page discussion with prediction, result, competing explanation and limitation. Include a paragraph on reproducibility and any constraints on safe field transfer. For extension, choose **invasion ecology and range expansion** as a new potential driver and design a minimally more informative follow-up study. Explain the number and kind of genuinely independent replicates that would be needed for a small pilot, rather than declaring arbitrary sample sizes statistically adequate.


## Unit 5 synthesis and critical assessment

1. **Mechanism map.** Relate Species richness, evenness and diversity metrics to Biogeography and species-area relationships. Mark the measured processes, their directions and the place where a biological outcome could be changed by an unobserved driver. Compare richness, evenness and between-site turnover using one synthetic community.
2. **Rival explanation.** A report concludes that beta diversity and community turnover must be responsible for a mapped pattern. Identify an environmental or measurement-based alternative, an observation consistent with both, and an independent comparison that could distinguish them.
3. **Quantitative audit.** Reconstruct all five examples in this unit without looking at the displayed result. Check units and dimensions, identify the reference value, and vary an input by ten percent. Record the effect size and the meaning of a negative, zero or unexpected result where applicable.
4. **Evidence review.** Examine a hypothetical study with four sites, two of them treated and two untreated, where investigators repeated twenty subsamples at every site. Explain why there are four independent site-level units, then discuss what additional temporal and spatial controls would strengthen the inference. Adjust the explanation if treatment spills between adjacent sites.
5. **Transfer and limits.** Explain why a range-expanding species is not automatically demonstrated to be damaging. Draft a concise comparison of how the model's assumptions change when moved from the constructed teaching scenario to a coastal, urban, agricultural or protected-area system. Explicitly indicate which ecological outcomes need long-term monitoring.
6. **Research communication.** Write a 500-word mini-review of two concepts from the unit, distinguishing established general mechanisms from synthetic calculations and uncertain real-world consequences. Cite at least one reliable open textbook or scientific reference, and state exactly which claim the reading supports. An external reference is not an endorsement of the OpenSTEM draft.

