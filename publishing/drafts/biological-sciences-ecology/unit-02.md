# Unit 02 — Population ecology and demography

> Translate survival, reproduction, detectability and movement into population trajectories.

## Learning goals

For population ecology and demography, explain the processes described in this unit, identify suitable observational and experimental units, connect synthetic numerical cases to physical measurements, and distinguish competing mechanisms. In the context of translate survival, reproduction, detectability and movement into population trajectories., state how variation in sampling effort, habitat, time or model assumptions could change the result. Interpret quantities with units and identify the evidence required before applying results to a real management decision.

## Conceptual foundation

### Individuals, populations and the arithmetic of change

Population ecology connects individual vital rates to the number of organisms in a defined place. A basic bookkeeping identity is N at time t+1 equals N at time t plus births and immigrants minus deaths and emigrants. It sounds trivial, but it prevents common errors: an observed population decline does not prove high mortality, and a new sighting does not prove local reproduction. Animals may redistribute within a landscape because water, food or disturbance has changed. A quadrat count may increase when vegetation is removed simply because individuals become easier to observe. Detection and demographic processes require different measurements.

Density is only meaningful with an explicit area. Dividing all observed birds by the area of an administrative reserve can produce a very different value than dividing territorial breeders by the area of suitable nesting habitat. Neither denominator is universally correct. The reserve-wide metric can inform a regional budget, while habitat-area density may illuminate local crowding. Choice of metric should follow the biological mechanism and the decision, and researchers should retain both the raw numerator and the boundaries used.

Life tables resolve the timing of survival and reproduction. A cohort that produces offspring early may expand more rapidly than one with the same total expected reproduction delayed until later ages. The net reproductive rate R0 combines survival to age x with fecundity at x, but it is not automatically equal to the finite annual growth factor lambda. Real organisms may have discrete stage transitions, overlapping generations and dormancy. In plants, a seed bank can buffer bad seasons; in vertebrates, delayed maturity can slow the demographic effect of habitat improvement. Stage-based matrix models become useful when age is not the best indicator of transitions.

Exponential growth is a conditional mathematical description: it assumes a constant proportional rate over the interval modeled. Logistic growth introduces density feedback by reducing per-capita growth as the population approaches a specified K. Neither equation promises that nature follows a smooth trajectory. A drought can lower resource supply quickly; a recruitment pulse can produce transient overshoot; predation or disease can create delayed feedback; demographic chance matters for very small populations. Fit residuals, parameter uncertainty and plausible ecological mechanisms must accompany curves shown in a report.

Spatial subdivision further complicates population persistence. A patch can be empty despite high-quality habitat if colonizers cannot reach it. A small population may survive through immigration from a nearby source. Conversely, apparently occupied patches may depend on continual arrival because local reproduction falls below replacement. Metapopulation language helps describe turnover, but reliable inference requires monitoring multiple seasons and estimating detection. Simple occupancy models can illustrate expected colonization-extinction relationships, although they must not erase habitat quality or dispersal behavior.

Finally, low density is not always beneficial. At low abundance, organisms may have difficulty finding mates, recruiting cooperative partners or defending habitats. Positive density dependence in such mechanisms creates an Allee effect, particularly important in some restoration or harvest questions. A management rule that removes a constant number of adults may become dangerous as abundance falls, even if it was inconsequential at high density. Explicitly compare fixed quota, proportional harvest and temporary closure scenarios. State whether a predicted threshold is observed, fitted or merely hypothetical before drawing ecological management conclusions.

## Five focused topics with worked examples

### 2.1 Population boundaries, density and detectability

#### Ecological concept and mechanism

A population estimate requires a spatial boundary, a time window and a rule for which individuals belong. Abundance and density are not equivalent, and observed encounters differ from true numbers when detection is imperfect.

Movement changes counts without births or deaths; patchy habitat changes density per total area versus suitable area; visibility and animal behavior change encounter probabilities. Ecologists must model or measure these separately.

#### Worked interpretive case

Bird observations increase along a wetland trail after vegetation removal, even when breeding territories are unchanged. The increase could reflect easier sighting rather than genuine population growth.

#### Evidence and study design

Run repeated standardized surveys across visibility gradients, estimate detection or distance effects, and state whether the target is total abundance, breeding individuals or density in usable habitat.

Calculate both whole-reserve and suitable-habitat density for one count; explain which question each answers.

#### Critical limitations and transfer

A count divided by arbitrary administrative area may have little biological meaning. Repeated visits improve inference only when closure and detectability assumptions are defensible.

Population monitoring can be misleading when sampling efficiency changes with the management intervention being evaluated.

#### Worked quantitative example 2.1: Detection-corrected point estimate

**Synthetic data.** Repeated observers detect a mean of 48 individuals in one standardized area and an independent calibration estimates per-individual detection probability of 0.60.

**Derivation and solution.** Divide the observed count by estimated detection probability for a simplified corrected count. The explicit calculation `48/0.6` gives **80 estimated individuals**. Identify how the input variables were defined before applying the same arithmetic to new measurements; the result is conditional on that definition.

**Ecological interpretation.** Correction suggests 80 individuals under equal independent detection probabilities.

**When the computation would mislead.** Heterogeneous detection, dependent encounters and uncertain p can produce substantial bias. For field applications, compare the precision of the input measurements with the apparent precision of the answer, then decide whether model structure or sampling error is likely to dominate uncertainty.

**Independent check and extension.** Recalculate with p=0.40 and explain why detection uncertainty must be propagated. Recalculate with one altered input and describe the observation that would justify changing that parameter in a real ecological study. Distinguish recalculating an illustrative equation from experimentally validating the biological relationship.


### 2.2 Life tables and demographic schedules

#### Ecological concept and mechanism

Life tables distinguish survival to each age from reproduction at each age. Population growth depends on when individuals reproduce as well as how many offspring are produced over a lifetime.

Age-specific survivorship l_x and fecundity m_x combine into net reproductive rate R0 = sum l_x m_x. Generation time and the intrinsic growth rate also reflect the distribution of reproduction across ages.

#### Worked interpretive case

Two hypothetical insect populations produce the same expected daughters per newborn female, but one reproduces mainly in the first month and the other mainly in the third. Their near-term rates can differ.

#### Evidence and study design

Construct a cohort from known starting individuals and follow marked life stages. Separate mortality, missing individuals and emigration, and estimate the uncertainty of rare adult classes.

Build a three-age life table and ask whether R0 above one guarantees growth under an abrupt habitat disturbance.

#### Critical limitations and transfer

One snapshot of an age structure is not the same as a followed cohort. Density dependence and changing conditions can invalidate a constant vital-rate projection.

Demographic models are powerful precisely when their chosen stages and transitions match an organism's biology.

#### Worked quantitative example 2.2: Net reproductive rate

**Synthetic data.** An invented cohort has survival to reproductive ages of 0.50 and 0.30 with respective daughter production of 1.8 and 2.4 per surviving female.

**Derivation and solution.** Sum survival times age-specific fecundity across the two reproductive age classes. The explicit calculation `0.5*1.8+0.3*2.4` gives **1.62 expected daughters per newborn female**. Identify how the input variables were defined before applying the same arithmetic to new measurements; the result is conditional on that definition.

**Ecological interpretation.** R0 above one suggests replacement exceeds unity under fixed cohort conditions; the speed of growth remains undetermined.

**When the computation would mislead.** If female dispersal or juvenile survival changes, the local population may still decline. For field applications, compare the precision of the input measurements with the apparent precision of the answer, then decide whether model structure or sampling error is likely to dominate uncertainty.

**Independent check and extension.** Contrast equal R0 schedules with reproduction occurring earlier or later in life. Recalculate with one altered input and describe the observation that would justify changing that parameter in a real ecological study. Distinguish recalculating an illustrative equation from experimentally validating the biological relationship.


### 2.3 Exponential, logistic and stochastic growth

#### Ecological concept and mechanism

Exponential growth describes proportional increase without density feedback. The logistic model represents declining per-capita growth as abundance approaches a parameter K, but real populations fluctuate and K is not necessarily fixed.

Births, deaths and immigration can create rapid increases; resource depletion or interference changes per-capita vital rates. Environmental variability introduces correlated shocks while demographic stochasticity matters especially in small populations.

#### Worked interpretive case

A laboratory culture grows almost exponentially early, slows as nutrients are exhausted, and then declines after waste accumulation. Fitting one logistic curve across all phases can hide changing mechanisms.

#### Evidence and study design

Plot changes per individual against density and examine residuals. Compare exponential and logistic fits over a stated interval, and record whether density was independently measured.

Use a discretized growth model to test the consequences of doubling r while K stays fixed and then changing K through habitat restoration.

#### Critical limitations and transfer

K depends on habitat and assumptions; the classic model cannot represent all time lags, age structure, seasonal forcing or Allee effects. An excellent curve fit is not causal proof.

Population growth projections should include alternative scenarios rather than a single endpoint with unexplained certainty.

#### Worked quantitative example 2.3: Logistic instantaneous increase

**Synthetic data.** A model population has N=200, intrinsic growth parameter r=0.3 per year, and stipulated carrying capacity K=1000.

**Derivation and solution.** Apply the logistic growth term rN(1-N/K) at the specified instant. The explicit calculation `0.3*200*(1-200/1000)` gives **48 individuals per year**. Identify how the input variables were defined before applying the same arithmetic to new measurements; the result is conditional on that definition.

**Ecological interpretation.** The theoretical rate is 48 new individuals per year at that density under the model assumptions.

**When the computation would mislead.** This is not an integer realized birth count, and K and r may change seasonally. For field applications, compare the precision of the input measurements with the apparent precision of the answer, then decide whether model structure or sampling error is likely to dominate uncertainty.

**Independent check and extension.** Repeat at N=900 and compare per-capita versus total expected growth. Recalculate with one altered input and describe the observation that would justify changing that parameter in a real ecological study. Distinguish recalculating an illustrative equation from experimentally validating the biological relationship.


### 2.4 Metapopulations and connectivity

#### Ecological concept and mechanism

Many species occupy patch networks where local extinctions and recolonizations jointly determine regional persistence. Suitable patches may remain empty when dispersal is rare, and occupied patches can act as sources or sinks.

Colonization probability often changes with neighboring occupied patches, distance and matrix resistance; extinction risk may rise as patch area or habitat quality falls. Migration can rescue small local populations.

#### Worked interpretive case

A butterfly occurs on small meadow patches near a core reserve but is missing from equally sized distant patches. Connectivity is plausible, yet patch management differences must also be examined.

#### Evidence and study design

Repeatedly survey patches, estimate detection, and compare colonization and extinction between seasons. Record patch area, quality and connectivity from biologically relevant movement distances.

Sketch a three-patch network and identify which link might increase recolonization most if restoration resources are limited.

#### Critical limitations and transfer

A simple patch-occupancy model assumes patches can be compared and their detection is known. The landscape matrix can help or hinder movement depending on species.

Spatial population theory helps distinguish preserving large habitat blocks from creating functional corridors.

#### Worked quantitative example 2.4: Occupied patch proportion

**Synthetic data.** Eighteen out of thirty hypothetical habitat patches were recorded occupied after a full season of standardized surveys.

**Derivation and solution.** Divide occupied patches by the total sampled patch frame. The explicit calculation `18/30` gives **0.6 observed occupancy fraction**. Identify how the input variables were defined before applying the same arithmetic to new measurements; the result is conditional on that definition.

**Ecological interpretation.** Observed occupancy equals 0.6 only under near-complete detection and a representative sampling frame.

**When the computation would mislead.** Missing the species in an occupied patch biases the naïve fraction downward; variable patch sizes matter for abundance. For field applications, compare the precision of the input measurements with the apparent precision of the answer, then decide whether model structure or sampling error is likely to dominate uncertainty.

**Independent check and extension.** Propose repeated surveys that separate occupancy from detectability. Recalculate with one altered input and describe the observation that would justify changing that parameter in a real ecological study. Distinguish recalculating an illustrative equation from experimentally validating the biological relationship.


### 2.5 Density dependence, Allee effects and exploitation

#### Ecological concept and mechanism

Density can reduce individual growth through crowding and competition, but low density may also depress reproduction when mates or cooperative partners become scarce. Harvest changes age structure and may alter future recruitment.

Negative density dependence tends to stabilize growth, whereas positive density dependence at low densities creates an Allee threshold. Removing a fixed number versus a fixed fraction has different effects near low abundance.

#### Worked interpretive case

A hypothetical broadcast-spawning marine invertebrate shows fewer successful fertilizations per adult at sparse densities even though food is plentiful. Its recovery may require local aggregation rather than only reducing harvest.

#### Evidence and study design

Relate per-capita recruitment to adult density across replicated sites while controlling for substrate, currents and temperature. Do not infer an Allee effect solely from declining abundance.

Contrast a fixed harvest of twenty animals with ten percent harvest when a population drops from five hundred to one hundred.

#### Critical limitations and transfer

Fishing and habitat degradation often change together, and fitted density effects can absorb an unmeasured time trend. Mechanisms must be tested, not just named.

Management thresholds are sensitive to the shape of the density response and uncertainty in estimating it.

#### Worked quantitative example 2.5: Proportional harvest

**Synthetic data.** A model harvest rule removes ten percent of a population estimated at one hundred adults before breeding.

**Derivation and solution.** Multiply current abundance by the fixed proportional removal fraction. The explicit calculation `0.10*100` gives **10 adults removed**. Identify how the input variables were defined before applying the same arithmetic to new measurements; the result is conditional on that definition.

**Ecological interpretation.** The proportional rule yields ten removals at this abundance, contrasted with a fixed take of twenty.

**When the computation would mislead.** Model predictions omit compensatory survival, measurement error and effects of removing particular age classes. For field applications, compare the precision of the input measurements with the apparent precision of the answer, then decide whether model structure or sampling error is likely to dominate uncertainty.

**Independent check and extension.** Calculate removal at a population of fifty and discuss whether the rule remains safe. Recalculate with one altered input and describe the observation that would justify changing that parameter in a real ecological study. Distinguish recalculating an illustrative equation from experimentally validating the biological relationship.


## Integrated computational and observation-design laboratory 2: Repeated surveys of a patch network

### Research aim and study system

Generate detections on four visits to each of 30 synthetic patches at two habitat qualities, with detection changing between windy and calm nights. This is an educational, entirely synthetic exercise for readers without laboratory equipment. Its case is **wetland breeding bird demography**, represented by **a wetland of thirty monitored nesting territories linked to nearby reedbeds**. The key quantities to observe are **adult survival, juvenile recruitment and movement**. The question is not simply whether two columns differ: it is whether the chosen evidence can **distinguish local failure to breed from departure to another site**. State the central alternative before generating any synthetic measurements. Otherwise changes in a plot can be explained after the fact without a meaningful test.

### Data dictionary and reproducibility requirements

Provide one row per actual study unit or visit, depending on the stage of measurement, and include explicit identifiers. Document **individual identity and detection**; also retain location class, date, survey duration, method version and a reason when data are missing. Define every unit, including degrees of temperature, area, individual counts or mass-per-time flux. Use distinct codes for zero, unobserved and not applicable. A table in which no organisms were seen despite valid sampling is not equivalent to a table in which a site was never visited. Save a read-only raw dataset and a second transformed dataset alongside a reproducible calculation log.

The book contains a synthetic example dataset for this unit under `datasets/lab-02.csv`. It illustrates a stable column structure rather than empirical evidence; its numerical values and site labels are invented. Review whether the input data are logically coherent before fitting any equation. A physically impossible concentration or a date outside the sampling window should trigger validation. Record any corrected values and preserve the originals so another reader can explain every change.

### Procedure

1. **Specify hypotheses.** Choose one explanatory process drawn from **population boundaries, density and detectability** and a serious competing explanation related to **exponential, logistic and stochastic growth**. Describe the response variable and whether the process predicts an increase, decrease, threshold or no change. Include a null pattern that could plausibly arise through sampling variation.
2. **Establish comparability.** Match sites, periods, effort or experimental units appropriately. If the study uses simulated random assignment, preserve the random seed and show treatment balance. Do not treat several measurements from one habitat block as independent blocks. Explain how space, time and shared weather might introduce dependence even under a seemingly random scheme.
3. **Explore the data.** Construct a scatterplot or time series with labeled axes, raw points and explicit group names. Report sample size at the actual experimental or observational-unit level. Inspect non-detections and extreme values, but do not delete observations solely because they contradict the initial hypothesis.
4. **Calculate and compare.** Estimate naïve occupancy then a detection-adjusted hypothetical quantity; examine how a closure violation changes the conclusion. Check arithmetic using two methods—a spreadsheet and a manual calculation, for example. Explain what part of the comparison was identified by a definition and what part required a model assumption. A graph that looks smooth does not demonstrate the validity of a causal pathway.
5. **Stress-test the conclusion.** Change one defensible parameter or data-quality rule: detection probability, sampling area, rate assumption, autocorrelation or reference choice. Recompute the principal estimate. If a moderate alteration reverses the sign or action threshold, present both outcomes and recommend improved measurement before a high-cost decision.
6. **Interpret with an alternative.** Compare the leading mechanism with the explicitly named rival. Propose a new independent measurement that would discriminate them. Include uncertainty and an ethical or logistical limitation. If results are inconsistent, label the result unresolved instead of inventing an unobserved pathway to rescue a favorite hypothesis.

### Results discussion and expected reasoning

The exercise contains no prespecified discovery. Its purpose is to make plausible ecological stories answerable through measurements. Explain how **life tables and demographic schedules** may affect a predicted outcome while **metapopulations and connectivity** can change the interpretation. Where the calculation involves probability, distinguish conditional probabilities from frequencies over repeated independent systems. Where a budget is calculated, distinguish flow rates from stocks and sum only compatible quantities. Where a management action is proposed, separate the number of actions implemented from the measured response of the ecosystem.

Do not equate failed detection with extinction or infer rescue effects from one short survey. Report the synthetic status prominently. If a model produces an impossible value, do not silently truncate it unless the modeling rule explicitly requires a bound. Instead identify the biological restriction omitted by the simple equation. Some ecological systems can have alternative stable trajectories or long lag times, but neither should be claimed from the dataset without specific evidence.

### Deliverables, assessment and extension

Submit an annotated data dictionary, an analysis script or spreadsheet formula log, two labeled figures, one complete hand-worked numerical calculation and a one-page discussion with prediction, result, competing explanation and limitation. Include a paragraph on reproducibility and any constraints on safe field transfer. For extension, choose **density dependence, allee effects and exploitation** as a new potential driver and design a minimally more informative follow-up study. Explain the number and kind of genuinely independent replicates that would be needed for a small pilot, rather than declaring arbitrary sample sizes statistically adequate.


## Unit 2 synthesis and critical assessment

1. **Mechanism map.** Relate Population boundaries, density and detectability to Metapopulations and connectivity. Mark the measured processes, their directions and the place where a biological outcome could be changed by an unobserved driver. Reconstruct a population change by separating vital rates and movement.
2. **Rival explanation.** A report concludes that life tables and demographic schedules must be responsible for a mapped pattern. Identify an environmental or measurement-based alternative, an observation consistent with both, and an independent comparison that could distinguish them.
3. **Quantitative audit.** Reconstruct all five examples in this unit without looking at the displayed result. Check units and dimensions, identify the reference value, and vary an input by ten percent. Record the effect size and the meaning of a negative, zero or unexpected result where applicable.
4. **Evidence review.** Examine a hypothetical study with four sites, two of them treated and two untreated, where investigators repeated twenty subsamples at every site. Explain why there are four independent site-level units, then discuss what additional temporal and spatial controls would strengthen the inference. Adjust the explanation if treatment spills between adjacent sites.
5. **Transfer and limits.** Discuss when proportional versus constant harvest creates different near-term risks. Draft a concise comparison of how the model's assumptions change when moved from the constructed teaching scenario to a coastal, urban, agricultural or protected-area system. Explicitly indicate which ecological outcomes need long-term monitoring.
6. **Research communication.** Write a 500-word mini-review of two concepts from the unit, distinguishing established general mechanisms from synthetic calculations and uncertain real-world consequences. Cite at least one reliable open textbook or scientific reference, and state exactly which claim the reading supports. An external reference is not an endorsement of the OpenSTEM draft.

