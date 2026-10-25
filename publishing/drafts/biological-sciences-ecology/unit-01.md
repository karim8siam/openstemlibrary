# Unit 01 — Scope, environments and biomes

> Define ecological systems and compare environmental controls from microsite to biosphere.

## Learning goals

For scope, environments and biomes, explain the processes described in this unit, identify suitable observational and experimental units, connect synthetic numerical cases to physical measurements, and distinguish competing mechanisms. In the context of define ecological systems and compare environmental controls from microsite to biosphere., state how variation in sampling effort, habitat, time or model assumptions could change the result. Interpret quantities with units and identify the evidence required before applying results to a real management decision.

## Conceptual foundation

### Ecological inference begins by defining a system

A student walking beside a pond can easily list visible organisms, yet the scientific problem only begins with the choice of a question. “What lives here?” asks about inventory and detectability. “Why does a fish population decline during a heat wave?” asks about environmental causation and demography. “How much carbon does this wetland retain annually?” asks for an ecosystem mass balance. The same scene accommodates all three projects, but each requires different boundaries, units, instruments and timescales. A common mistake is to collect interesting measurements first and choose an explanation afterward. Strong ecological studies make predictions before the data are analyzed and document the assumptions that connect observations to inference.

Organismal responses to temperature, salinity, oxygen or water availability can be rapid. Population size, by contrast, depends on the cumulative balance of births, deaths, immigration and emigration. Community composition depends on these population processes across many interacting species. Ecosystem questions also involve abiotic reservoirs and transfers: water imports sediment, plants capture energy, microbes recycle nutrients and gaseous exchange connects local soil to the atmosphere. Scale is not just a measurement convenience. It determines which causal processes can even be represented. A one-square-meter quadrat may reveal seedling competition; it cannot establish regional dispersal without a separate sampling design.

Imagine two hypothetical marshes with identical average rainfall. One has short intense storms and compacted soil; the other has gentler rainfall and connected floodplain channels. Equal yearly rainfall does not imply equal infiltration, peak water depth or nutrient export. A useful conceptual model represents rainfall, interception, soil storage, evapotranspiration, runoff and water discharge as separate components. If the question concerns aquatic oxygen stress, the student may add temperature-dependent solubility, mixing and respiration. This is the ecological counterpart of a controlled physical system, but natural boundaries are often permeable. Defining a study area does not stop immigration, groundwater flow or atmospheric transport.

Observational sampling and manipulation answer different questions. A transect across salinity can map changes in vegetation, but salinity may covary with elevation, flooding and grazing. A greenhouse experiment can vary salinity independently and reveal physiological responses, but its conditions may omit symbionts, microbes and weather extremes. The combination is stronger than either approach alone. The field survey establishes the real spatial pattern; the experiment asks whether one candidate factor can cause the response under stipulated conditions. Time series and natural experiments can add evidence, although they still require care about confounding.

The unit therefore treats microhabitats, large biomes and freshwater or marine systems as connected expressions of physical constraints and living interactions. Expect “where?” and “how much?” to precede “why?”; distinguish the habitat in which organisms are found from the conditions under which they could persist. Record when observations were made. For example, a daytime dissolved-oxygen value may differ from predawn oxygen because photosynthesis and respiration vary over the day. Be prepared to explain why a non-detection is not a verified absence. These habits will remain essential in later studies of population trends, biodiversity and conservation.

## Five focused topics with worked examples

### 1.1 Ecological questions and nested scales

#### Ecological concept and mechanism

Ecology investigates the distribution, abundance, interactions and fluxes linking organisms to physical settings. An organism can respond to temperature in minutes while a population changes over generations and a watershed exports nutrients over seasons. Scale is therefore part of every ecological claim.

Define the spatial grain of a measurement and the extent of the system. Organismal physiology influences individual survival; births, deaths and movements change populations; interactions reorganize communities; production and decomposition move carbon through ecosystems.

#### Worked interpretive case

A pond may have fewer fish after a warm week because oxygen becomes limiting, because fish emigrate, or because sampling misses animals sheltering at depth. Each explanation changes what should be measured.

#### Evidence and study design

Measure water temperature, dissolved oxygen, detection effort and repeated fish counts along the same locations. Ask whether changes in observed counts coincide with environmental changes after controlling for visibility and sampling time.

Write three hypotheses for a decline in detected organisms. Name the unit of replication for each and an observation that would rule it out.

#### Critical limitations and transfer

Changing a map boundary changes estimated density, species richness and apparent habitat association. Ecological correlation cannot be transported automatically from a small plot to an entire region.

An ecological answer must tie a mechanism to a scale and a response variable; a sophisticated model with an undefined sampling unit remains uninterpretable.

#### Worked quantitative example 1.1: Sampling frame and density

**Synthetic data.** A hypothetical pond count records 72 fish across 2.4 hectares of defined suitable habitat; outside ponds and adjacent marsh are not sampled.

**Derivation and solution.** Density equals counted individuals divided by sampled area. The explicit calculation `72/2.4` gives **30 fish per hectare**. Identify how the input variables were defined before applying the same arithmetic to new measurements; the result is conditional on that definition.

**Ecological interpretation.** This is observed count density, not a detection-corrected abundance estimate. It supports comparison only if habitat definition and survey effort match.

**When the computation would mislead.** Fish hidden in vegetation or moving between zones break simple census assumptions; counting methods may need calibration. For field applications, compare the precision of the input measurements with the apparent precision of the answer, then decide whether model structure or sampling error is likely to dominate uncertainty.

**Independent check and extension.** Repeat with 3.6 hectares while holding the same count and explain why a changed denominator is not a biological decline. Recalculate with one altered input and describe the observation that would justify changing that parameter in a real ecological study. Distinguish recalculating an illustrative equation from experimentally validating the biological relationship.


### 1.2 Biotic and abiotic environmental gradients

#### Ecological concept and mechanism

Resource availability, salinity, water potential, light and temperature create environmental gradients, while neighbors alter the microclimate and access to resources. Species distributions reflect both physiological tolerance and biotic interactions.

Temperature modifies metabolic rates within limits, soil moisture influences stomatal conductance, and salinity alters osmoregulation. Competition or facilitation can shift the realized range away from physiological tolerance in isolation.

#### Worked interpretive case

A seedling survives near the edge of a dry grassland under shrub shade but dies in equally dry exposed microsites. Shade can reduce evaporative demand while the shrub also competes for water.

#### Evidence and study design

Compare matched shade and open microsites at similar soil moisture. Record actual leaf or soil temperatures instead of treating a categorical label as a direct physical measurement.

Draw a causal diagram separating radiation, water, neighbors and growth. Identify one contrast that could isolate facilitation from competitive effects.

#### Critical limitations and transfer

Survivorship of planted seedlings may not predict recruitment from seeds; rainfall history, herbivory and observer selection can confound an apparently simple gradient.

Environmental gradients are not necessarily linear; thresholds and temporal extremes may matter more than annual means.

#### Worked quantitative example 1.2: Thermal gradient magnitude

**Synthetic data.** Two paired microhabitats differ between 31.5 and 27.2 degrees Celsius during the same afternoon observation window.

**Derivation and solution.** Subtract the matched readings to estimate the thermal contrast. The explicit calculation `31.5-27.2` gives **4.3 degrees Celsius**. Identify how the input variables were defined before applying the same arithmetic to new measurements; the result is conditional on that definition.

**Ecological interpretation.** A 4.3-degree contrast may alter water loss or activity but does not quantify physiological performance by itself.

**When the computation would mislead.** One-time readings miss diurnal extremes and instrument placement could systematically affect the result. For field applications, compare the precision of the input measurements with the apparent precision of the answer, then decide whether model structure or sampling error is likely to dominate uncertainty.

**Independent check and extension.** Estimate the mean contrast using replicated hourly readings rather than selecting the warmest pair. Recalculate with one altered input and describe the observation that would justify changing that parameter in a real ecological study. Distinguish recalculating an illustrative equation from experimentally validating the biological relationship.


### 1.3 Ecological niches and limits of tolerance

#### Ecological concept and mechanism

The ecological niche describes the environmental conditions and resources under which a population can persist, not merely the physical place where organisms are found. A realized niche may be narrowed or shifted by interactions and dispersal limits.

Physiological performance curves combine with mortality, reproductive rates and colonization. A location can appear suitable at one season yet fail to support long-term reproduction when extreme events or missing partners intervene.

#### Worked interpretive case

Two hypothetical freshwater invertebrates tolerate overlapping oxygen concentrations in the laboratory, but only one is abundant where predatory fish occur. Predation changes occupancy without altering intrinsic oxygen tolerance.

#### Evidence and study design

Construct a performance-by-oxygen curve and compare field occupancy in sites with and without predators. Include replicate sites and estimates of detection probability.

Explain why presence does not prove a habitat is optimal and why non-detection is not proof of unsuitable conditions.

#### Critical limitations and transfer

A laboratory optimum cannot establish the fundamental niche across every relevant variable. Historical exclusion and inability to reach suitable habitat can mimic intolerance.

Niche models should distinguish mechanistic tolerance from observed association, especially when forecasting range shifts.

#### Worked quantitative example 1.3: Tolerance observations

**Synthetic data.** A synthetic assay scores survival in 14 of 20 evenly defined test intervals where environmental exposure falls within a tested range.

**Derivation and solution.** Compute the fraction of intervals in which survival was observed. The explicit calculation `14/20` gives **0.7 fraction of test intervals**. Identify how the input variables were defined before applying the same arithmetic to new measurements; the result is conditional on that definition.

**Ecological interpretation.** The observed proportion summarizes coverage of the selected experimental window, not geographic occupancy probability.

**When the computation would mislead.** Unequal interval durations and untested extremes would change the interpretation; survival is not equivalent to reproduction. For field applications, compare the precision of the input measurements with the apparent precision of the answer, then decide whether model structure or sampling error is likely to dominate uncertainty.

**Independent check and extension.** Explain why 14 of 20 does not establish that 70 percent of real-world environments support persistence. Recalculate with one altered input and describe the observation that would justify changing that parameter in a real ecological study. Distinguish recalculating an illustrative equation from experimentally validating the biological relationship.


### 1.4 Terrestrial biomes, soils and microhabitats

#### Ecological concept and mechanism

Broad climate patterns help organize forests, grasslands, deserts and tundra, yet local topography, disturbance, soils and land management generate large variation inside any named biome.

Heat and water budgets constrain plant productivity; parent material and soil development influence nutrients; fire and herbivory change vegetation structure. The same annual rainfall can yield different vegetation with different seasonality and soil retention.

#### Worked interpretive case

Two slopes in one regional biome may differ in vegetation because one faces stronger afternoon radiation and has shallower soil. A national biome map can overlook that local contrast.

#### Evidence and study design

Sample paired slopes for soil depth, moisture, plant cover and disturbance history; preserve site identifiers and avoid counting ten quadrats within one slope as ten independent landscapes.

Compare two hypothetical grasslands receiving equal annual rainfall but different wet-season timing. Predict a measurable functional difference.

#### Critical limitations and transfer

Biome labels are broad descriptions, not mechanisms or sharply bounded ecological states. Anthropogenic changes and climate anomalies create mixtures not represented by textbook maps.

Connecting macroclimate to microhabitats prevents ecological generalizations from erasing biodiversity at fine spatial grain.

#### Worked quantitative example 1.4: Rainfall to water depth

**Synthetic data.** Annual precipitation at an imaginary grassland station is 900 millimeters over one year. No conversion to net soil recharge is assumed.

**Derivation and solution.** Convert millimeters to meters by dividing by 1000. The explicit calculation `900/1000` gives **0.9 meters of precipitation**. Identify how the input variables were defined before applying the same arithmetic to new measurements; the result is conditional on that definition.

**Ecological interpretation.** The result is an input depth, not the depth stored in soil or used by plants.

**When the computation would mislead.** Runoff, interception, evaporation and infiltration partition the rainfall into unequal pathways. For field applications, compare the precision of the input measurements with the apparent precision of the answer, then decide whether model structure or sampling error is likely to dominate uncertainty.

**Independent check and extension.** Construct a water balance after hypothetical additions of evapotranspiration and runoff. Recalculate with one altered input and describe the observation that would justify changing that parameter in a real ecological study. Distinguish recalculating an illustrative equation from experimentally validating the biological relationship.


### 1.5 Freshwater, coastal and marine systems

#### Ecological concept and mechanism

Aquatic environments are structured by salinity, light penetration, mixing, flow, oxygen and nutrient delivery. Water depth is not equivalent to habitat quality, and connectivity links upstream practices to downstream ecological outcomes.

Stratification can isolate bottom waters from atmospheric oxygen; currents move plankton and larvae; sediments store or release nutrients under changing chemistry. Estuarine salinity varies with both rainfall and tides.

#### Worked interpretive case

In a hypothetical reservoir, surface chlorophyll increases while deep dissolved oxygen falls during prolonged stratification. Production near lighted surface waters can coexist with oxygen stress at depth.

#### Evidence and study design

Measure profiles of temperature, oxygen and conductivity over time; pair chlorophyll samples with light attenuation and mixing observations. Avoid extrapolating one midday profile to an entire season.

Design sampling for a tidal estuary in which the apparent salinity effect could be confounded by the phase of the tide.

#### Critical limitations and transfer

Turbid water may contain mineral particles rather than a phytoplankton bloom. Reservoir shape and water residence time can dominate responses to identical nutrient inputs.

Aquatic ecology depends on transport and storage: material introduced in one place may influence another place much later.

#### Worked quantitative example 1.5: Reservoir residence-time proxy

**Synthetic data.** A reservoir has a nominal volume of two million cubic meters and daily outflow of fifty thousand cubic meters under simplified steady conditions.

**Derivation and solution.** Residence time equals volume divided by daily outflow, assuming complete mixing and approximate steady state. The explicit calculation `2000000/50000` gives **40 days**. Identify how the input variables were defined before applying the same arithmetic to new measurements; the result is conditional on that definition.

**Ecological interpretation.** Forty days is a hydraulic turnover proxy and does not mean every water parcel exits after forty days.

**When the computation would mislead.** Stratification, dead zones, variable inflow and spatially structured flow broaden actual transit times. For field applications, compare the precision of the input measurements with the apparent precision of the answer, then decide whether model structure or sampling error is likely to dominate uncertainty.

**Independent check and extension.** Discuss how a tracer study could test whether the well-mixed estimate is suitable. Recalculate with one altered input and describe the observation that would justify changing that parameter in a real ecological study. Distinguish recalculating an illustrative equation from experimentally validating the biological relationship.


## Integrated computational and observation-design laboratory 1: How gradients can mimic causal explanations

### Research aim and study system

Record 12 invented sites across wetland edges, measure temperature, water depth, oxygen and vegetation cover, and group repeated readings by site. This is an educational, entirely synthetic exercise for readers without laboratory equipment. Its case is **pond-to-watershed gradient**, represented by **a shallow marsh, an upstream stream reach and a neighboring shrub-covered slope**. The key quantities to observe are **temperature, moisture and oxygen**. The question is not simply whether two columns differ: it is whether the chosen evidence can **separate spatial covariation from manipulations of one environmental driver**. State the central alternative before generating any synthetic measurements. Otherwise changes in a plot can be explained after the fact without a meaningful test.

### Data dictionary and reproducibility requirements

Provide one row per actual study unit or visit, depending on the stage of measurement, and include explicit identifiers. Document **site identity and time of day**; also retain location class, date, survey duration, method version and a reason when data are missing. Define every unit, including degrees of temperature, area, individual counts or mass-per-time flux. Use distinct codes for zero, unobserved and not applicable. A table in which no organisms were seen despite valid sampling is not equivalent to a table in which a site was never visited. Save a read-only raw dataset and a second transformed dataset alongside a reproducible calculation log.

The book contains a synthetic example dataset for this unit under `datasets/lab-01.csv`. It illustrates a stable column structure rather than empirical evidence; its numerical values and site labels are invented. Review whether the input data are logically coherent before fitting any equation. A physically impossible concentration or a date outside the sampling window should trigger validation. Record any corrected values and preserve the originals so another reader can explain every change.

### Procedure

1. **Specify hypotheses.** Choose one explanatory process drawn from **ecological questions and nested scales** and a serious competing explanation related to **ecological niches and limits of tolerance**. Describe the response variable and whether the process predicts an increase, decrease, threshold or no change. Include a null pattern that could plausibly arise through sampling variation.
2. **Establish comparability.** Match sites, periods, effort or experimental units appropriately. If the study uses simulated random assignment, preserve the random seed and show treatment balance. Do not treat several measurements from one habitat block as independent blocks. Explain how space, time and shared weather might introduce dependence even under a seemingly random scheme.
3. **Explore the data.** Construct a scatterplot or time series with labeled axes, raw points and explicit group names. Report sample size at the actual experimental or observational-unit level. Inspect non-detections and extreme values, but do not delete observations solely because they contradict the initial hypothesis.
4. **Calculate and compare.** Compare a gradient-only analysis to a matched-sites analysis while keeping the observation window explicit. Check arithmetic using two methods—a spreadsheet and a manual calculation, for example. Explain what part of the comparison was identified by a definition and what part required a model assumption. A graph that looks smooth does not demonstrate the validity of a causal pathway.
5. **Stress-test the conclusion.** Change one defensible parameter or data-quality rule: detection probability, sampling area, rate assumption, autocorrelation or reference choice. Recompute the principal estimate. If a moderate alteration reverses the sign or action threshold, present both outcomes and recommend improved measurement before a high-cost decision.
6. **Interpret with an alternative.** Compare the leading mechanism with the explicitly named rival. Propose a new independent measurement that would discriminate them. Include uncertainty and an ethical or logistical limitation. If results are inconsistent, label the result unresolved instead of inventing an unobserved pathway to rescue a favorite hypothesis.

### Results discussion and expected reasoning

The exercise contains no prespecified discovery. Its purpose is to make plausible ecological stories answerable through measurements. Explain how **biotic and abiotic environmental gradients** may affect a predicted outcome while **terrestrial biomes, soils and microhabitats** can change the interpretation. Where the calculation involves probability, distinguish conditional probabilities from frequencies over repeated independent systems. Where a budget is calculated, distinguish flow rates from stocks and sum only compatible quantities. Where a management action is proposed, separate the number of actions implemented from the measured response of the ecosystem.

Physical monitoring should be non-invasive, and no real field collection is represented by the numerical teaching rows. Report the synthetic status prominently. If a model produces an impossible value, do not silently truncate it unless the modeling rule explicitly requires a bound. Instead identify the biological restriction omitted by the simple equation. Some ecological systems can have alternative stable trajectories or long lag times, but neither should be claimed from the dataset without specific evidence.

### Deliverables, assessment and extension

Submit an annotated data dictionary, an analysis script or spreadsheet formula log, two labeled figures, one complete hand-worked numerical calculation and a one-page discussion with prediction, result, competing explanation and limitation. Include a paragraph on reproducibility and any constraints on safe field transfer. For extension, choose **freshwater, coastal and marine systems** as a new potential driver and design a minimally more informative follow-up study. Explain the number and kind of genuinely independent replicates that would be needed for a small pilot, rather than declaring arbitrary sample sizes statistically adequate.


## Unit 1 synthesis and critical assessment

1. **Mechanism map.** Relate Ecological questions and nested scales to Terrestrial biomes, soils and microhabitats. Mark the measured processes, their directions and the place where a biological outcome could be changed by an unobserved driver. Explain why site averages conceal microhabitats and temporal extremes.
2. **Rival explanation.** A report concludes that biotic and abiotic environmental gradients must be responsible for a mapped pattern. Identify an environmental or measurement-based alternative, an observation consistent with both, and an independent comparison that could distinguish them.
3. **Quantitative audit.** Reconstruct all five examples in this unit without looking at the displayed result. Check units and dimensions, identify the reference value, and vary an input by ten percent. Record the effect size and the meaning of a negative, zero or unexpected result where applicable.
4. **Evidence review.** Examine a hypothetical study with four sites, two of them treated and two untreated, where investigators repeated twenty subsamples at every site. Explain why there are four independent site-level units, then discuss what additional temporal and spatial controls would strengthen the inference. Adjust the explanation if treatment spills between adjacent sites.
5. **Transfer and limits.** Use a two-factor diagram to show why environmental tolerance and dispersal limitations produce different range predictions. Draft a concise comparison of how the model's assumptions change when moved from the constructed teaching scenario to a coastal, urban, agricultural or protected-area system. Explicitly indicate which ecological outcomes need long-term monitoring.
6. **Research communication.** Write a 500-word mini-review of two concepts from the unit, distinguishing established general mechanisms from synthetic calculations and uncertain real-world consequences. Cite at least one reliable open textbook or scientific reference, and state exactly which claim the reading supports. An external reference is not an endorsement of the OpenSTEM draft.

