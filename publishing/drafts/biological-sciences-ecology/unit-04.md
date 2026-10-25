# Unit 04 — Ecosystem energetics and biogeochemistry

> Quantify photosynthetic energy capture and carbon, nitrogen, phosphorus and water transfers.

## Learning goals

For ecosystem energetics and biogeochemistry, explain the processes described in this unit, identify suitable observational and experimental units, connect synthetic numerical cases to physical measurements, and distinguish competing mechanisms. In the context of quantify photosynthetic energy capture and carbon, nitrogen, phosphorus and water transfers., state how variation in sampling effort, habitat, time or model assumptions could change the result. Interpret quantities with units and identify the evidence required before applying results to a real management decision.

## Conceptual foundation

### Ecosystems as linked energy and material budgets

An ecosystem is a system of organisms, physical surroundings and transfers across chosen boundaries. Energy flows from external sources into biochemical work and eventually disperses as heat, while atoms move among biotic and abiotic pools. The distinction is central: energy does not circulate endlessly as a conserved usable resource through food webs, but carbon, nitrogen and phosphorus can be transformed and recycled. A biomass snapshot does not reveal rates of production, consumption or decomposition. Small aquatic phytoplankton can support rapid production despite low standing biomass because cells turn over quickly. A mature forest can store large biomass while annual net stock change is relatively small.

Primary production must be expressed with units of area and time. Gross primary production represents photosynthetic carbon fixation in a stated accounting scheme. Net primary production subtracts producers' own respiration. Net ecosystem production considers broader respiratory losses, and full carbon accounting may need lateral dissolved or particulate export, fire, harvest and changes in soil reservoirs. Terminology and sign conventions differ among methods, so readers should define them explicitly. An atmosphere-to-ecosystem flux measured by a tower cannot automatically be equated with total long-term sequestration if harvested material or streams transport carbon out of the region.

Decomposition links living production to soil nutrients and atmospheric exchange. A standard litterbag exercise estimates disappearance of dry material, yet part of the disappearance may be physical fragmentation or leaching rather than complete mineralization. Mesh size can exclude larger detritivores, while a mesh bag may modify airflow and humidity. An exponential decay constant summarizes loss during a measured interval, not a single universal property of all leaf compounds. Decomposers react to moisture, oxygen and substrate chemistry; prolonged waterlogging can slow some aerobic pathways and change the forms of gases released. These processes matter for both crop soils and natural wetlands.

Carbon budgets illustrate why stock and flux must be reported separately. A soil can retain a large carbon stock from centuries of accumulation even when today's net flux is near zero. Conversely, a newly growing stand can have a high rate of uptake but relatively small standing carbon. Seasonal uptake may reverse during dry periods. To compare restoration treatments, an ecologist needs consistent depth intervals, bulk density for soil estimates, comparable time windows and uncertainties associated with spatial heterogeneity. This avoids crediting a site for sequestration that is really a redistribution of material or a short-term storage change.

Nitrogen cycling involves changes in chemical form. Biological fixation introduces newly available reactive nitrogen; mineralization returns organic nitrogen to inorganic forms; nitrification and denitrification proceed through microbial pathways conditioned by oxygen and carbon supplies. Phosphorus behaves differently, often interacting strongly with sediments and soil chemistry. Nutrient concentration alone does not establish limitation: a bioassay or nutrient-addition experiment must show a growth or functional response. Combined additions may reveal co-limitation or a shift in what becomes limiting after the first nutrient is supplied.

Catchments connect plot-scale processes to rivers and estuaries. An event with high discharge and moderate nutrient concentration can deliver more mass than a quiet period with a high concentration. Load calculations therefore multiply concentration by flow, after consistent conversion of liters, cubic meters, milligrams and kilograms. Continuous monitors and storm-triggered sampling can be more informative than a handful of convenient noon samples. A coherent ecosystem study draws its budget boundary, lists inputs and outputs, checks dimensional consistency and acknowledges missing pools before treating the remainder as ecological gain or loss.

## Five focused topics with worked examples

### 4.1 Primary production and energy budgets

#### Ecological concept and mechanism

Primary producers transform captured energy into organic chemical energy, while respiration and consumption influence what remains available for growth and food webs. Productivity is a rate; standing biomass is a stock.

Gross primary production includes photosynthetic carbon fixation; ecosystem respiration consumes organic carbon, and net ecosystem production reflects their balance under stated sign conventions. Light, nutrients and water regulate these fluxes.

#### Worked interpretive case

A productive wetland may have high plant biomass yet little annual carbon accumulation if decomposition and export offset growth. A low-biomass algal system can turn over rapidly.

#### Evidence and study design

Measure exchange rates over known area and time, estimate uncertainty and report whether belowground tissues and dissolved organic carbon are included.

Estimate GPP from net exchange and respiratory fluxes under one explicit convention and test sensitivity to nighttime measurements.

#### Critical limitations and transfer

Energy and mass units should not be mixed; day versus year comparisons require temporal integration. Photosynthetic uptake alone does not establish long-term carbon sequestration.

A full budget must close on a defined spatial boundary and accounting period.

#### Worked quantitative example 4.1: Net primary production

**Synthetic data.** Annual gross primary production is stipulated as 1400 grams carbon per square meter and annual producer autotrophic respiration is 800 in identical units.

**Derivation and solution.** NPP equals GPP minus autotrophic respiration. The explicit calculation `1400-800` gives **600 g C m^-2 yr^-1**. Identify how the input variables were defined before applying the same arithmetic to new measurements; the result is conditional on that definition.

**Ecological interpretation.** Six hundred grams carbon per square meter per year remain available for producer growth and associated pathways.

**When the computation would mislead.** This does not say how much persists in soil: grazing, decay, fire and export matter. For field applications, compare the precision of the input measurements with the apparent precision of the answer, then decide whether model structure or sampling error is likely to dominate uncertainty.

**Independent check and extension.** Calculate the change if respiration rises twenty percent while GPP stays fixed. Recalculate with one altered input and describe the observation that would justify changing that parameter in a real ecological study. Distinguish recalculating an illustrative equation from experimentally validating the biological relationship.


### 4.2 Decomposition, soil carbon and detrital webs

#### Ecological concept and mechanism

Dead organic matter is processed by microbes and detritivores, returning nutrients to availability and transferring carbon among pools. Decomposition depends on substrate quality, temperature, moisture and oxygen supply.

Labile compounds tend to disappear early while lignin-rich or physically protected carbon may persist. Microbial respiration releases carbon dioxide, and waterlogged anaerobic soils can favor different biochemical pathways.

#### Worked interpretive case

Leaves decomposing in a warm, moist forest lose mass faster than the same leaves in a dry open site, but leaching and fragmentation also contribute to measured loss.

#### Evidence and study design

Use standardized litterbags with mesh-size controls, weigh dry mass, analyze elemental composition and separate early leaching from later biological processing.

Compute the remaining fraction after a known decay constant and assess how a drought changes the estimated value.

#### Critical limitations and transfer

An exponential mass-loss constant averages changing processes and does not mean every carbon fraction decays identically. Mesh bags can exclude decomposers or alter airflow.

A soil carbon stock can rise because input increases, loss falls, or both; a mass-loss observation alone does not reveal the whole mechanism.

#### Worked quantitative example 4.2: Litter remaining after decay

**Synthetic data.** A teaching model starts with 100 grams of leaf dry matter and assumes an exponential loss constant of 0.20 per month over three months.

**Derivation and solution.** Compute remaining dry mass as M0 times exp(-kt), represented here by a precomputed survival factor exp(-0.6) approximately 0.548812. The explicit calculation `100*0.548812` gives **54.8812 grams dry mass**. Identify how the input variables were defined before applying the same arithmetic to new measurements; the result is conditional on that definition.

**Ecological interpretation.** About 54.9 grams remain under the single-pool exponential assumption.

**When the computation would mislead.** Leaching, fragmentation and variable compound chemistry mean real litter rarely follows one constant rate across every phase. For field applications, compare the precision of the input measurements with the apparent precision of the answer, then decide whether model structure or sampling error is likely to dominate uncertainty.

**Independent check and extension.** Compare mass loss under k=0.1 and explain whether an altered mesh design could change estimated k. Recalculate with one altered input and describe the observation that would justify changing that parameter in a real ecological study. Distinguish recalculating an illustrative equation from experimentally validating the biological relationship.


### 4.3 Carbon cycling and ecosystem respiration

#### Ecological concept and mechanism

Carbon moves through photosynthesis, respiration, dissolved transport, sediments, soils and the atmosphere. Evaluating a carbon sink requires accounting for both flux direction and all important pools.

Plants fix atmospheric carbon; consumers and microbes respire it; fire and land conversion can transfer stored carbon rapidly. Water can export carbon to downstream waters that later release it.

#### Worked interpretive case

A forest plot appears to accumulate trunk biomass for five years, but simultaneous soil carbon loss and harvested wood export alter its net carbon balance.

#### Evidence and study design

Construct an input-output budget for aboveground, belowground, soil and dissolved pools. Express all quantities in consistent carbon units and document stock changes over time.

Calculate a net budget when fixation, ecosystem respiration and stream export are given, stating the sign convention.

#### Critical limitations and transfer

Eddy covariance, chambers and inventories sample different processes and scales; none automatically captures imported or exported materials. A short monitoring interval can misclassify a fluctuating system.

Climate mitigation claims should distinguish measured sequestration from temporary storage and substitution assumptions.

#### Worked quantitative example 4.3: Net ecosystem carbon balance

**Synthetic data.** A hypothetical annual budget records carbon fixation of 1200, ecosystem respiratory losses of 900, and net stream export of 60 in matching grams C per square meter per year.

**Derivation and solution.** Under an explicitly positive-uptake convention, subtract both loss terms from fixation. The explicit calculation `1200-900-60` gives **240 g C m^-2 yr^-1**. Identify how the input variables were defined before applying the same arithmetic to new measurements; the result is conditional on that definition.

**Ecological interpretation.** The estimated positive retention is 240 under the stipulated complete accounting boundary.

**When the computation would mislead.** Lateral imports, harvest, erosion and fire may alter the real net ecosystem carbon balance. For field applications, compare the precision of the input measurements with the apparent precision of the answer, then decide whether model structure or sampling error is likely to dominate uncertainty.

**Independent check and extension.** Name one omitted flux that could reverse the sink classification. Recalculate with one altered input and describe the observation that would justify changing that parameter in a real ecological study. Distinguish recalculating an illustrative equation from experimentally validating the biological relationship.


### 4.4 Nitrogen transformations and nutrient limitation

#### Ecological concept and mechanism

Nitrogen fixation, mineralization, nitrification, assimilation and denitrification transform nitrogen among chemical forms with distinct mobility and biological availability. Nutrient limitation is defined by response, not mere low concentration.

Microbes mediate many redox-sensitive steps; oxygen, carbon supply, temperature and pH control rates. Adding nitrogen may increase plant growth in one ecosystem and increase leaching or harmful algal growth in another.

#### Worked interpretive case

A fertilized grassland has increased leaf nitrogen but no extra biomass after phosphorus becomes limiting. The limiting factor shifts with altered supply.

#### Evidence and study design

Compare single-nutrient and combined nutrient additions with replication. Track plant responses, soil pools and water losses rather than measuring concentration alone.

Interpret a factorial N×P addition table and identify evidence for co-limitation without overclaiming the physiological pathway.

#### Critical limitations and transfer

Concentration is a stock-related measurement, not a process rate. Isotopic tracers and incubations have distinct assumptions and potential artifacts.

Nutrient management requires matching form, dose, timing and hydrologic pathway to ecological objectives.

#### Worked quantitative example 4.4: Relative fertilizer response

**Synthetic data.** Plant production is 150 grams dry mass in a fertilized group versus 100 grams in the matched no-fertilizer group.

**Derivation and solution.** Compute relative response as treated minus control divided by the control mean. The explicit calculation `(150-100)/100` gives **0.5 fractional production change**. Identify how the input variables were defined before applying the same arithmetic to new measurements; the result is conditional on that definition.

**Ecological interpretation.** The fifty percent response is evidence of nutrient responsiveness in the hypothetical conditions.

**When the computation would mislead.** It does not identify the unique limiting nutrient if fertilizer added several elements or affected soil pH. For field applications, compare the precision of the input measurements with the apparent precision of the answer, then decide whether model structure or sampling error is likely to dominate uncertainty.

**Independent check and extension.** Propose a N×P experiment and contrast single-element effects to interaction effects. Recalculate with one altered input and describe the observation that would justify changing that parameter in a real ecological study. Distinguish recalculating an illustrative equation from experimentally validating the biological relationship.


### 4.5 Phosphorus, hydrology and material export

#### Ecological concept and mechanism

Phosphorus often moves with particles or dissolved compounds and is strongly shaped by soil chemistry and erosion; water flow determines when materials leave ecosystems. Hydrologic connections make local disturbances regional.

Rainfall intensity, vegetation cover and landscape slope affect runoff and sediment transport. Sorption and release can delay the effects of nutrient reductions after inputs are curtailed.

#### Worked interpretive case

A catchment reduces annual fertilizer application, yet downstream phosphorus remains high during heavy rains because legacy soil pools and bank sediments remain sources.

#### Evidence and study design

Use flow-weighted sampling across storms, map land cover and sediment sources, and distinguish dissolved from particulate concentrations. Compare load, the product of concentration and discharge, to concentration alone.

Calculate daily nutrient load from flow and concentration while checking liters, cubic meters and milligrams.

#### Critical limitations and transfer

A water sample collected during dry weather misses event-driven pulses; a single station cannot localize all upstream sources. Residence times produce delayed response.

Watershed decisions should compare upstream actions to measured downstream mass transport rather than selected concentration snapshots.

#### Worked quantitative example 4.5: Watershed nutrient load

**Synthetic data.** Water discharge is 0.2 cubic meters per second and dissolved phosphorus concentration is 0.3 milligrams per liter over one steady-state day.

**Derivation and solution.** Convert discharge to liters per second, multiply by concentration and 86,400 seconds, then convert milligrams to kilograms. The explicit calculation `0.2*1000*0.3*86400/1000000` gives **5.184 kilograms per day**. Identify how the input variables were defined before applying the same arithmetic to new measurements; the result is conditional on that definition.

**Ecological interpretation.** The resulting daily load is 5.184 kilograms phosphorus under constant flow and concentration.

**When the computation would mislead.** Storm-driven pulses can dominate annual load, and grab samples can miss them. For field applications, compare the precision of the input measurements with the apparent precision of the answer, then decide whether model structure or sampling error is likely to dominate uncertainty.

**Independent check and extension.** Recalculate at four times the discharge and half the concentration, then discuss storm sampling. Recalculate with one altered input and describe the observation that would justify changing that parameter in a real ecological study. Distinguish recalculating an illustrative equation from experimentally validating the biological relationship.


## Integrated computational and observation-design laboratory 4: Closing a simplified watershed budget

### Research aim and study system

Track weekly synthetic gross fixation, respiration, stream discharge and phosphorus concentration through a twelve-week period. This is an educational, entirely synthetic exercise for readers without laboratory equipment. Its case is **watershed energy and nutrient budget**, represented by **a small reservoir receiving sediment and nutrients from a managed catchment**. The key quantities to observe are **carbon flux, dissolved nutrient load and seasonal mixing**. The question is not simply whether two columns differ: it is whether the chosen evidence can **close mass budgets without confusing stocks, concentrations and rates**. State the central alternative before generating any synthetic measurements. Otherwise changes in a plot can be explained after the fact without a meaningful test.

### Data dictionary and reproducibility requirements

Provide one row per actual study unit or visit, depending on the stage of measurement, and include explicit identifiers. Document **catchment and annual integration period**; also retain location class, date, survey duration, method version and a reason when data are missing. Define every unit, including degrees of temperature, area, individual counts or mass-per-time flux. Use distinct codes for zero, unobserved and not applicable. A table in which no organisms were seen despite valid sampling is not equivalent to a table in which a site was never visited. Save a read-only raw dataset and a second transformed dataset alongside a reproducible calculation log.

The book contains a synthetic example dataset for this unit under `datasets/lab-04.csv`. It illustrates a stable column structure rather than empirical evidence; its numerical values and site labels are invented. Review whether the input data are logically coherent before fitting any equation. A physically impossible concentration or a date outside the sampling window should trigger validation. Record any corrected values and preserve the originals so another reader can explain every change.

### Procedure

1. **Specify hypotheses.** Choose one explanatory process drawn from **primary production and energy budgets** and a serious competing explanation related to **carbon cycling and ecosystem respiration**. Describe the response variable and whether the process predicts an increase, decrease, threshold or no change. Include a null pattern that could plausibly arise through sampling variation.
2. **Establish comparability.** Match sites, periods, effort or experimental units appropriately. If the study uses simulated random assignment, preserve the random seed and show treatment balance. Do not treat several measurements from one habitat block as independent blocks. Explain how space, time and shared weather might introduce dependence even under a seemingly random scheme.
3. **Explore the data.** Construct a scatterplot or time series with labeled axes, raw points and explicit group names. Report sample size at the actual experimental or observational-unit level. Inspect non-detections and extreme values, but do not delete observations solely because they contradict the initial hypothesis.
4. **Calculate and compare.** Convert every transfer to comparable area-time units and identify a hypothetical missing export needed to close the balance. Check arithmetic using two methods—a spreadsheet and a manual calculation, for example. Explain what part of the comparison was identified by a definition and what part required a model assumption. A graph that looks smooth does not demonstrate the validity of a causal pathway.
5. **Stress-test the conclusion.** Change one defensible parameter or data-quality rule: detection probability, sampling area, rate assumption, autocorrelation or reference choice. Recompute the principal estimate. If a moderate alteration reverses the sign or action threshold, present both outcomes and recommend improved measurement before a high-cost decision.
6. **Interpret with an alternative.** Compare the leading mechanism with the explicitly named rival. Propose a new independent measurement that would discriminate them. Include uncertainty and an ethical or logistical limitation. If results are inconsistent, label the result unresolved instead of inventing an unobserved pathway to rescue a favorite hypothesis.

### Results discussion and expected reasoning

The exercise contains no prespecified discovery. Its purpose is to make plausible ecological stories answerable through measurements. Explain how **decomposition, soil carbon and detrital webs** may affect a predicted outcome while **nitrogen transformations and nutrient limitation** can change the interpretation. Where the calculation involves probability, distinguish conditional probabilities from frequencies over repeated independent systems. Where a budget is calculated, distinguish flow rates from stocks and sum only compatible quantities. Where a management action is proposed, separate the number of actions implemented from the measured response of the ecosystem.

A model with a large residual should be reported as incomplete rather than corrected by inventing an unmeasured flux. Report the synthetic status prominently. If a model produces an impossible value, do not silently truncate it unless the modeling rule explicitly requires a bound. Instead identify the biological restriction omitted by the simple equation. Some ecological systems can have alternative stable trajectories or long lag times, but neither should be claimed from the dataset without specific evidence.

### Deliverables, assessment and extension

Submit an annotated data dictionary, an analysis script or spreadsheet formula log, two labeled figures, one complete hand-worked numerical calculation and a one-page discussion with prediction, result, competing explanation and limitation. Include a paragraph on reproducibility and any constraints on safe field transfer. For extension, choose **phosphorus, hydrology and material export** as a new potential driver and design a minimally more informative follow-up study. Explain the number and kind of genuinely independent replicates that would be needed for a small pilot, rather than declaring arbitrary sample sizes statistically adequate.


## Unit 4 synthesis and critical assessment

1. **Mechanism map.** Relate Primary production and energy budgets to Nitrogen transformations and nutrient limitation. Mark the measured processes, their directions and the place where a biological outcome could be changed by an unobserved driver. Close a carbon budget and state what would make the sink assignment reverse.
2. **Rival explanation.** A report concludes that decomposition, soil carbon and detrital webs must be responsible for a mapped pattern. Identify an environmental or measurement-based alternative, an observation consistent with both, and an independent comparison that could distinguish them.
3. **Quantitative audit.** Reconstruct all five examples in this unit without looking at the displayed result. Check units and dimensions, identify the reference value, and vary an input by ten percent. Record the effect size and the meaning of a negative, zero or unexpected result where applicable.
4. **Evidence review.** Examine a hypothetical study with four sites, two of them treated and two untreated, where investigators repeated twenty subsamples at every site. Explain why there are four independent site-level units, then discuss what additional temporal and spatial controls would strengthen the inference. Adjust the explanation if treatment spills between adjacent sites.
5. **Transfer and limits.** Contrast a nutrient concentration measurement with an annual nutrient load calculation. Draft a concise comparison of how the model's assumptions change when moved from the constructed teaching scenario to a coastal, urban, agricultural or protected-area system. Explicitly indicate which ecological outcomes need long-term monitoring.
6. **Research communication.** Write a 500-word mini-review of two concepts from the unit, distinguishing established general mechanisms from synthetic calculations and uncertain real-world consequences. Cite at least one reliable open textbook or scientific reference, and state exactly which claim the reading supports. An external reference is not an endorsement of the OpenSTEM draft.

