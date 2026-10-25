# Unit 07 — Global change, restoration and conservation

> Evaluate disturbance, climate responses, fragmentation, restoration and prioritization.

## Learning goals

For global change, restoration and conservation, explain the processes described in this unit, identify suitable observational and experimental units, connect synthetic numerical cases to physical measurements, and distinguish competing mechanisms. In the context of evaluate disturbance, climate responses, fragmentation, restoration and prioritization., state how variation in sampling effort, habitat, time or model assumptions could change the result. Interpret quantities with units and identify the evidence required before applying results to a real management decision.

## Conceptual foundation

### Change, resilience and ecological futures

Ecosystems change under ordinary variation and large disturbances. A disturbance is not defined solely by visible destruction: a drought can reduce growth without removing vegetation, and a fire can create habitat structure necessary for certain organisms while damaging others. Frequency, severity, duration and timing are separate components of a disturbance regime. A habitat that usually experiences periodic flooding may deteriorate when flooding is prevented, even if human observers see the absence of floods as stability. Ecologists therefore describe the historical variability of a system before setting a recovery benchmark.

Resilience has several operational meanings. A population may recover its abundance after a pulse disturbance while losing genetic variation; a marsh may recover plant cover while its sediment chemistry remains altered; a forest may regain carbon storage but change species composition. A statement that an ecosystem has recovered is incomplete without the response variable, baseline, reference trajectory and observation period. If the reference site itself shifts with climate, the target must be revisited. Claims about irreversible regime shifts require stronger evidence than a single abrupt time-series change, because unmeasured drivers or slow recovery can produce similar patterns.

Climate changes challenge equilibrium expectations. Mean warming can modify metabolism and reproductive timing, but heat waves, unusual droughts and altered seasonality may drive the largest effects. Phenological mismatch is a hypothesis linking timing of interacting species to realized reproduction or survival; an earlier flowering date alone does not establish a demographic loss. Species-distribution models trained on current climate correlations can fail under novel climate combinations, changing competitors or inaccessible migration routes. Microhabitats sometimes buffer regional warming, yet exposure may rise with land conversion and heat accumulation. Field measurements across microclimates can test whether local refuges are ecologically meaningful.

Habitat fragmentation changes more than area. Core habitat depends on patch geometry and depth of edge influence, while roads and transformed land may inhibit or facilitate movement depending on the species. To isolate fragmentation effects, researchers attempt to distinguish subdivision from overall habitat loss and from changes in quality. A small fragment in a well-connected landscape can behave differently from a similarly sized isolated fragment. Connectivity cannot be assessed with a single human map distance when organisms experience roads, currents, shade or canopy differently.

Restoration turns theory into testable intervention. A floodplain reconnection project may restore seasonal water movement quickly, while seed banks, food webs and native recruitment respond over years. A replanting effort can report high first-year seedling survival without establishing a self-sustaining ecosystem. Good projects specify separate indicators for structure, function, species composition and community benefits; they budget for maintenance and monitoring; and they define when an underperforming intervention should be revised. Reference conditions are guides, not timeless mandates that ignore shifting climate or social realities.

Conservation prioritization involves irreversible opportunity costs. Protecting large sites may help common habitat and regional connectivity, whereas small irreplaceable sites may sustain endemic species. A decision model can clarify objectives, costs, uncertainties and trade-offs, but it cannot determine ethical priorities without input from affected communities and legitimate governance. Uncertainty is a reason to compare scenarios and monitor outcomes, not to pretend every alternative is equally good. The practical aim is to make explicit why a proposed action was chosen, how its outcomes will be measured and what evidence would lead to change.

## Five focused topics with worked examples

### 7.1 Disturbance regimes, resilience and thresholds

#### Ecological concept and mechanism

Ecosystems experience fires, floods, storms, droughts and human disturbance that vary in frequency, size and severity. Recovery means different things for biomass, species composition and functional processes.

Repeated perturbations may change feedbacks such as vegetation cover, soil retention and recruitment. Some systems recover along the former trajectory; others shift to a different state if thresholds are crossed.

#### Worked interpretive case

A coastal marsh regains plant cover after flooding but retains altered soil salinity and invertebrate communities for years. Calling it fully recovered depends on the variable chosen.

#### Evidence and study design

Measure several functions over time against comparable reference sites and baseline variability. Examine pulse versus press disturbances and report recovery horizons.

Define resilience operationally for a restoration project and identify a measurable early warning that must be validated.

#### Critical limitations and transfer

A before-and-after comparison without controls cannot distinguish disturbance effects from regional climate anomalies. Observed abrupt change does not automatically prove alternative stable states.

Disturbance management is a question of coupled ecological processes, not maintaining one fixed visual appearance.

#### Worked quantitative example 7.1: Relative restoration recovery

**Synthetic data.** A disturbed ecological function scored 30 units, a reference scores 90, and the monitored restored site now scores 70 on the same validated scale.

**Derivation and solution.** Express recovered distance as improvement from baseline divided by the full reference gap. The explicit calculation `(70-30)/(90-30)` gives **0.666667 fraction of reference gap closed**. Identify how the input variables were defined before applying the same arithmetic to new measurements; the result is conditional on that definition.

**Ecological interpretation.** About two-thirds of the initial gap has closed under this chosen indicator.

**When the computation would mislead.** The metric may conceal decline in another indicator such as native composition or water quality. For field applications, compare the precision of the input measurements with the apparent precision of the answer, then decide whether model structure or sampling error is likely to dominate uncertainty.

**Independent check and extension.** State what happens if the reference site also changes during the restoration period. Recalculate with one altered input and describe the observation that would justify changing that parameter in a real ecological study. Distinguish recalculating an illustrative equation from experimentally validating the biological relationship.


### 7.2 Climate responses and range shifts

#### Ecological concept and mechanism

Warming, altered precipitation and extreme events modify performance, phenology and species distributions. Ecological responses can lag climate exposure because dispersal, interactions and microhabitats mediate change.

Heat and drought affect metabolism and water balance, while seasonal timing changes resource synchronization. Range limits can reflect both mortality at extremes and historical colonization barriers.

#### Worked interpretive case

A pollinator emerges earlier in warmer springs, but flowering shifts less, creating an apparent timing mismatch. Effects on reproduction depend on actual overlap and alternative pollinators.

#### Evidence and study design

Use long-term paired phenology and temperature records, compare sites across climate gradients and record observation effort. Distinguish mean warming from changed extreme-event frequency.

Predict two mechanisms for a species remaining in a warming region despite projected loss of climatic suitability.

#### Critical limitations and transfer

Correlative species-distribution models assume relationships that may not hold during novel climates. Range change is not a direct measurement of adaptation.

Climate forecasts for ecosystems should communicate dispersal assumptions and uncertainties in biotic interactions.

#### Worked quantitative example 7.2: Accumulated growing-degree estimate

**Synthetic data.** Mean daily temperature is modeled at 22 degrees Celsius for thirty days and the chosen species-specific base is 10 degrees.

**Derivation and solution.** Accumulate positive daily temperature above base with a constant illustrative mean. The explicit calculation `(22-10)*30` gives **360 degree-days**. Identify how the input variables were defined before applying the same arithmetic to new measurements; the result is conditional on that definition.

**Ecological interpretation.** The synthetic sum is 360 degree-days and may index phenological development under a basic threshold model.

**When the computation would mislead.** Actual daily maxima, minima, extreme heat and moisture conditions affect development beyond this simplification. For field applications, compare the precision of the input measurements with the apparent precision of the answer, then decide whether model structure or sampling error is likely to dominate uncertainty.

**Independent check and extension.** Contrast a constant average with thirty highly variable daily temperatures. Recalculate with one altered input and describe the observation that would justify changing that parameter in a real ecological study. Distinguish recalculating an illustrative equation from experimentally validating the biological relationship.


### 7.3 Landscape fragmentation and edge effects

#### Ecological concept and mechanism

Habitat fragmentation changes patch sizes, isolation and the ratio of edge to interior conditions. A fragment's nominal area may overstate habitat available to interior specialists.

Edges alter light, wind, temperature, predators and human access. Roads can impede movement for some organisms while serving as dispersal corridors for others. Connectivity is therefore species-dependent.

#### Worked interpretive case

A forest patch supports edge-tolerant birds but loses an understory specialist after surrounding clearing increases edge exposure.

#### Evidence and study design

Map edge distance, patch shape, matrix and local habitat quality; compare demographic rates rather than species sightings alone. Consider matched continuous-forest sites.

Calculate approximate core area after excluding an edge buffer from a rectangular patch, showing how shape affects the answer.

#### Critical limitations and transfer

Fragmentation per se can be difficult to separate from total habitat loss; smaller patches may also be degraded for unrelated reasons.

Landscape recommendations need species-specific movement and interior-habitat evidence, not corridor construction as an automatic default.

#### Worked quantitative example 7.3: Edge-buffer core area

**Synthetic data.** A rectangular habitat fragment measures 1000 by 500 meters and the ecological interior is operationally defined as more than 100 meters from every edge.

**Derivation and solution.** Subtract two edge widths from each dimension and multiply the remaining lengths. The explicit calculation `(1000-2*100)*(500-2*100)` gives **240000 square meters of core habitat**. Identify how the input variables were defined before applying the same arithmetic to new measurements; the result is conditional on that definition.

**Ecological interpretation.** The core rectangle is 240000 square meters, or 24 hectares, under the stated buffer.

**When the computation would mislead.** Organisms experience different edge-depth effects, and irregular shapes may contain much less interior habitat. For field applications, compare the precision of the input measurements with the apparent precision of the answer, then decide whether model structure or sampling error is likely to dominate uncertainty.

**Independent check and extension.** Compare with a long thin fragment of the same total area. Recalculate with one altered input and describe the observation that would justify changing that parameter in a real ecological study. Distinguish recalculating an illustrative equation from experimentally validating the biological relationship.


### 7.4 Restoration ecology and reference conditions

#### Ecological concept and mechanism

Restoration aims to recover defined ecological attributes or processes, yet no single historical snapshot is automatically attainable or desirable under continuing change.

Removing a pressure can permit natural regeneration; planting, hydrologic reconnection or soil remediation may be needed when key processes or propagule sources are absent. Social governance determines which outcomes are legitimate.

#### Worked interpretive case

A drained floodplain regains seasonal water after a levee is altered, but aquatic invertebrates recolonize slowly because upstream sources are fragmented.

#### Evidence and study design

Set multiple measurable objectives—hydrology, native recruitment, water quality, connectivity—and compare restored sites with reference and untreated controls across years.

Develop a five-year monitoring plan with leading indicators and a predefined rule for adjusting interventions.

#### Critical limitations and transfer

Success judged only by planted seedling survival can miss functional failure. Restored habitat should not be represented as ecologically equivalent immediately after planting.

Effective restoration evaluates ecological outcomes and trade-offs rather than counting planted trees or completed construction alone.

#### Worked quantitative example 7.4: Restored seedling survival

**Synthetic data.** Three hundred fifty native seedlings were planted in monitored plots and 280 were alive at the prespecified first-year survey.

**Derivation and solution.** Divide live planted individuals by the known initial planting cohort. The explicit calculation `280/350` gives **0.8 first-year survival fraction**. Identify how the input variables were defined before applying the same arithmetic to new measurements; the result is conditional on that definition.

**Ecological interpretation.** The monitored first-year survival is 0.80 for this cohort under complete reidentification.

**When the computation would mislead.** Survival at one year does not establish recruitment, reproduction or ecosystem recovery. For field applications, compare the precision of the input measurements with the apparent precision of the answer, then decide whether model structure or sampling error is likely to dominate uncertainty.

**Independent check and extension.** Estimate uncertainty and propose how to track self-sustaining recruitment in later years. Recalculate with one altered input and describe the observation that would justify changing that parameter in a real ecological study. Distinguish recalculating an illustrative equation from experimentally validating the biological relationship.


### 7.5 Conservation prioritization and decision analysis

#### Ecological concept and mechanism

Conservation decisions allocate limited resources under uncertain extinction risk, ecosystem values, implementation feasibility and equity constraints. The priority depends on the explicit objective and whose interests are included.

Optimizing for species richness alone may neglect irreplaceable endemic communities; connectivity may improve dispersal but be costly or ineffective without habitat quality. Risk reduction and cost-effectiveness should be estimated transparently.

#### Worked interpretive case

A hypothetical reserve proposal protects a large common habitat, while a smaller site contains an endemic species and provides flood protection for nearby settlements.

#### Evidence and study design

Define alternative objectives, opportunity costs, monitoring costs and risk scenarios. Use structured decision analysis with stakeholder participation rather than treating one score as natural truth.

Compare two conservation projects using expected benefit per dollar while explaining missing social and ecological dimensions.

#### Critical limitations and transfer

Values cannot always be compressed into a single index. Biological uncertainty, tenure rights and long-term funding can overturn an apparently cheap ranking.

A decision is defensible when assumptions and trade-offs are explicit, not when it produces a uniquely precise number.

#### Worked quantitative example 7.5: Cost per protected area

**Synthetic data.** A hypothetical intervention costs 60000 monetary units for a verified protected area of 120 hectares, with all implementation costs assumed included.

**Derivation and solution.** Divide intervention expenditure by hectares protected. The explicit calculation `60000/120` gives **500 money units per hectare**. Identify how the input variables were defined before applying the same arithmetic to new measurements; the result is conditional on that definition.

**Ecological interpretation.** Five hundred per hectare is a simple implementation cost ratio, not a measured ecological benefit.

**When the computation would mislead.** Long-term management expenses, land tenure and effectiveness can reverse comparisons between projects. For field applications, compare the precision of the input measurements with the apparent precision of the answer, then decide whether model structure or sampling error is likely to dominate uncertainty.

**Independent check and extension.** Explain how expected persistence benefit per hectare could change the preferred site. Recalculate with one altered input and describe the observation that would justify changing that parameter in a real ecological study. Distinguish recalculating an illustrative equation from experimentally validating the biological relationship.


## Integrated computational and observation-design laboratory 7: Recovery after a change in hydrology

### Research aim and study system

Generate five monitoring years for a restored wetland, a reference area and a matched no-intervention area with rainfall anomalies. This is an educational, entirely synthetic exercise for readers without laboratory equipment. Its case is **floodplain recovery trajectory**, represented by **a restored floodplain, a similar untreated floodplain and a reference wetland**. The key quantities to observe are **hydrology, recruitment, native cover and nutrient export**. The question is not simply whether two columns differ: it is whether the chosen evidence can **evaluate ecological function rather than counting interventions completed**. State the central alternative before generating any synthetic measurements. Otherwise changes in a plot can be explained after the fact without a meaningful test.

### Data dictionary and reproducibility requirements

Provide one row per actual study unit or visit, depending on the stage of measurement, and include explicit identifiers. Document **time since intervention and reference-site drift**; also retain location class, date, survey duration, method version and a reason when data are missing. Define every unit, including degrees of temperature, area, individual counts or mass-per-time flux. Use distinct codes for zero, unobserved and not applicable. A table in which no organisms were seen despite valid sampling is not equivalent to a table in which a site was never visited. Save a read-only raw dataset and a second transformed dataset alongside a reproducible calculation log.

The book contains a synthetic example dataset for this unit under `datasets/lab-07.csv`. It illustrates a stable column structure rather than empirical evidence; its numerical values and site labels are invented. Review whether the input data are logically coherent before fitting any equation. A physically impossible concentration or a date outside the sampling window should trigger validation. Record any corrected values and preserve the originals so another reader can explain every change.

### Procedure

1. **Specify hypotheses.** Choose one explanatory process drawn from **disturbance regimes, resilience and thresholds** and a serious competing explanation related to **landscape fragmentation and edge effects**. Describe the response variable and whether the process predicts an increase, decrease, threshold or no change. Include a null pattern that could plausibly arise through sampling variation.
2. **Establish comparability.** Match sites, periods, effort or experimental units appropriately. If the study uses simulated random assignment, preserve the random seed and show treatment balance. Do not treat several measurements from one habitat block as independent blocks. Explain how space, time and shared weather might introduce dependence even under a seemingly random scheme.
3. **Explore the data.** Construct a scatterplot or time series with labeled axes, raw points and explicit group names. Report sample size at the actual experimental or observational-unit level. Inspect non-detections and extreme values, but do not delete observations solely because they contradict the initial hypothesis.
4. **Calculate and compare.** Fit and plot response trajectories for vegetation and nutrient load, testing whether recovery definitions disagree. Check arithmetic using two methods—a spreadsheet and a manual calculation, for example. Explain what part of the comparison was identified by a definition and what part required a model assumption. A graph that looks smooth does not demonstrate the validity of a causal pathway.
5. **Stress-test the conclusion.** Change one defensible parameter or data-quality rule: detection probability, sampling area, rate assumption, autocorrelation or reference choice. Recompute the principal estimate. If a moderate alteration reverses the sign or action threshold, present both outcomes and recommend improved measurement before a high-cost decision.
6. **Interpret with an alternative.** Compare the leading mechanism with the explicitly named rival. Propose a new independent measurement that would discriminate them. Include uncertainty and an ethical or logistical limitation. If results are inconsistent, label the result unresolved instead of inventing an unobserved pathway to rescue a favorite hypothesis.

### Results discussion and expected reasoning

The exercise contains no prespecified discovery. Its purpose is to make plausible ecological stories answerable through measurements. Explain how **climate responses and range shifts** may affect a predicted outcome while **restoration ecology and reference conditions** can change the interpretation. Where the calculation involves probability, distinguish conditional probabilities from frequencies over repeated independent systems. Where a budget is calculated, distinguish flow rates from stocks and sum only compatible quantities. Where a management action is proposed, separate the number of actions implemented from the measured response of the ecosystem.

Do not declare full recovery from a single vegetation indicator or an unreplicated before-after contrast. Report the synthetic status prominently. If a model produces an impossible value, do not silently truncate it unless the modeling rule explicitly requires a bound. Instead identify the biological restriction omitted by the simple equation. Some ecological systems can have alternative stable trajectories or long lag times, but neither should be claimed from the dataset without specific evidence.

### Deliverables, assessment and extension

Submit an annotated data dictionary, an analysis script or spreadsheet formula log, two labeled figures, one complete hand-worked numerical calculation and a one-page discussion with prediction, result, competing explanation and limitation. Include a paragraph on reproducibility and any constraints on safe field transfer. For extension, choose **conservation prioritization and decision analysis** as a new potential driver and design a minimally more informative follow-up study. Explain the number and kind of genuinely independent replicates that would be needed for a small pilot, rather than declaring arbitrary sample sizes statistically adequate.


## Unit 7 synthesis and critical assessment

1. **Mechanism map.** Relate Disturbance regimes, resilience and thresholds to Restoration ecology and reference conditions. Mark the measured processes, their directions and the place where a biological outcome could be changed by an unobserved driver. Define resilience using two response indicators with different trajectories.
2. **Rival explanation.** A report concludes that climate responses and range shifts must be responsible for a mapped pattern. Identify an environmental or measurement-based alternative, an observation consistent with both, and an independent comparison that could distinguish them.
3. **Quantitative audit.** Reconstruct all five examples in this unit without looking at the displayed result. Check units and dimensions, identify the reference value, and vary an input by ten percent. Record the effect size and the meaning of a negative, zero or unexpected result where applicable.
4. **Evidence review.** Examine a hypothetical study with four sites, two of them treated and two untreated, where investigators repeated twenty subsamples at every site. Explain why there are four independent site-level units, then discuss what additional temporal and spatial controls would strengthen the inference. Adjust the explanation if treatment spills between adjacent sites.
5. **Transfer and limits.** Compare restoration options when habitat area and landscape connectivity differ. Draft a concise comparison of how the model's assumptions change when moved from the constructed teaching scenario to a coastal, urban, agricultural or protected-area system. Explicitly indicate which ecological outcomes need long-term monitoring.
6. **Research communication.** Write a 500-word mini-review of two concepts from the unit, distinguishing established general mechanisms from synthetic calculations and uncertain real-world consequences. Cite at least one reliable open textbook or scientific reference, and state exactly which claim the reading supports. An external reference is not an endorsement of the OpenSTEM draft.

