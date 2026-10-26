# Unit 4 — Cryosphere, land, biosphere and carbon cycling
## The central climate-science investigation

**Question:** How do ice, soil, vegetation and the carbon cycle modify climate and respond to it?

**Case setting:** An invented watershed experiences snow retreat, soil drying and forest disturbance. All locations and observations in the following investigation are synthetic. The purpose is to learn which inference would survive contact with independent measurements, rather than to produce a plausible-sounding story from an incomplete climate map.

The cryosphere and biosphere are neither passive recipients of atmospheric change nor simple independent forcings. Snow and ice change surface reflectivity; thawed soils alter drainage and carbon processing; vegetation changes surface roughness, evapotranspiration and ecosystem storage. Mass conservation matters: a glacier losing thickness differs from a globally uniform meltwater contribution, and a short-term forest uptake flux does not guarantee long-term storage.

Time lags often separate forcing, local response and observations. A satellite maps reflectance or surface height, whereas ground sensors supply local depth, moisture or flux. Each observation captures a different support. A coherent explanation for a changing mountain watershed must reconcile seasonality, elevation, topography and disturbances such as fire rather than relying on one temperature trace.

### Working boundaries and research assumptions

The effective observational transect for this unit runs from **snow, vegetation and ocean surface feedbacks**. Different forms of evidence support different kinds of inference: satellite ice/vegetation field constrains one aspect, ground mass or carbon measurements another, and independent regional water balance a third. These are not interchangeable. A flux through a boundary differs from stored heat or carbon; a baseline-dependent anomaly is not an absolute state; a correlation alone cannot establish forcing attribution. Choose a geographic domain or explicit accounting boundary before writing the governing relationship. Record the averaging period and the geographical support used in comparisons.

Use a synthetic mountain basin with ice, snow and vegetation changes to construct separate water, energy and carbon budgets; identify at least one possible sign change in a feedback.

### What success looks like

A strong unit report reconstructs a physical chain from forcing to response while maintaining the distinction between an observation, a calculation, a model hypothesis and a decision. Include a figure that cannot be understood without axis units, a written alternative explanation and a comparison with a second type of evidence. Account for spatial coverage and lagged feedbacks before claiming a causal sequence.


## Lesson 4.1 — Snow cover, albedo and mountain hydrology

### The physical question

Snow reflects more sunlight than many snow-free surfaces, providing an albedo feedback when cover changes. Snowfall, compaction, melt, sublimation and runoff depend on energy and mass balance. Elevation and aspect create spatial contrasts unresolved by coarse models. Snowpack timing often matters more than annual snow amount for water supplies. For the synthetic case, distinguish measured state, forcing, feedback, trend and any fitted relationship. An observed long-term change must be distinguished from sampling artifacts, internal variability and reference-period effects. Record the spatial scale, instrument history and averaging interval.


### From fundamental laws to an operational approximation

Begin by diagramming **snow, vegetation and ocean surface feedbacks** and labeling **surface water, carbon and energy transfers**. Choose a defensible statistical estimator, physical balance or mass-budget relationship appropriate to this topic. Distinguish the underlying process from the approximations in a fitted model, observational indicator or toy equation. Check dimensions and direction conventions before calculating; climate fields may be spatially varying even when one chart appears constant.


### What observations could distinguish mechanisms?

Use paired snow-depth and radiation measurements to separate accumulation from energy-driven melt. Identify the observation time, position, calibration information and observational resolution. Contrast **satellite ice/vegetation field**, **ground mass or carbon measurements** and **independent regional water balance**. A strong analysis identifies at least one independent variable, region or time interval where competing explanations make different predictions. In particular, assess time autocorrelation; never use the same evidence both to tune a hypothesis and to claim its independent confirmation.


### Worked numerical case — Snow-albedo absorbed flux

**Fictional data:** Incident shortwave 450 W/m² on snow albedo 0.78.

**Calculation:** `450*(1-.78)`. The numerical result is **99 W/m²**. Explicitly verify its units and interpretation; the number is a conditional result from invented inputs, not a documented observation. **Sensitivity:** perturb the dominant uncertain input by 10% and report what changes. Albedo depends on snow age, angle and spectral response. Explain which excluded process might invalidate the simplified estimate.


### Limits, confounding and counterfactual reasoning

A temperature threshold alone misses rain-on-snow, solar flux and wind redistribution. Contrast an alternative mechanism and state an observation that could discriminate between them. A more complex fitted curve is not necessarily a better causal explanation. Record station metadata, climate regime and measurement support before transferring a conclusion to a new situation.


### Practical study investigation

Trace a spring snowmelt water-budget with storage and timing explicitly separated. Use `datasets/unit-04-synthetic.csv` for reproducible practice: plot the yearly variable and a five-year average while stating what the smoothing removes; annotate potential instrument error and a rival hypothesis. Reserve some observations for an independent check. The synthetic values are not validated natural observations, and apparent agreement with an illustrative model is not climate-data verification.


### Conceptual checks and problem set

1. Draw the physical process underlying **Snow cover, albedo and mountain hydrology**, then label the state variables, external forcing, feedbacks and observational boundary. Which label is least well supported?
2. Reproduce the worked example with all unit conversions visible. Change one assumed value by 10%; report the new answer and interpret whether its sign or scale is plausible.
3. Explain how **a temperature threshold alone misses rain-on-snow, solar flux and wind redistribution.** Give one additional observable that would distinguish this issue from the core mechanism.
4. Translate the case into an observational protocol: station placement, sample frequency, calibration information, data exclusion rules and one independent validation source.
5. Identify a failure mode for the proposed task: **Trace a spring snowmelt water-budget with storage and timing explicitly separated.** Explain how biased sampling, omitted uncertainty or changes in the measurement system could produce a misleading conclusion.

**Answer expectations:** A competent response states the physical assumption, uses correctly dimensioned quantities, provides an interpretation in the context of the mechanism, reports an alternative explanation, and explicitly distinguishes fictional numerical inputs from observed climatological evidence. Answers that assert an exact future climate outcome from these toy equations require independent validation.


## Lesson 4.2 — Glacier mass balance and sea level

### The physical question

Glacier mass balance measures accumulation minus ablation, and delayed ice flow may obscure surface climate response. Mass loss from grounded land ice contributes to ocean mass; floating ice has a different direct displacement relationship. Sea level also responds to ocean thermal expansion and regional circulation and gravity effects. For the synthetic case, distinguish measured state, forcing, feedback, trend and any fitted relationship. An observed long-term change must be distinguished from sampling artifacts, internal variability and reference-period effects. Record the spatial scale, instrument history and averaging interval.


### From fundamental laws to an operational approximation

Begin by diagramming **snow, vegetation and ocean surface feedbacks** and labeling **surface water, carbon and energy transfers**. Choose a defensible statistical estimator, physical balance or mass-budget relationship appropriate to this topic. Distinguish the underlying process from the approximations in a fitted model, observational indicator or toy equation. Check dimensions and direction conventions before calculating; climate fields may be spatially varying even when one chart appears constant.


### What observations could distinguish mechanisms?

Compare geodetic elevation-change evidence with seasonal stake records and an ocean-altimetry estimate. Identify the observation time, position, calibration information and observational resolution. Contrast **satellite ice/vegetation field**, **ground mass or carbon measurements** and **independent regional water balance**. A strong analysis identifies at least one independent variable, region or time interval where competing explanations make different predictions. In particular, assess a shift in observational method; never use the same evidence both to tune a hypothesis and to claim its independent confirmation.


### Worked numerical case — Land-ice mass equivalent

**Fictional data:** An imaginary glacier loses 12 km³ of ice of mean density 900 kg/m³.

**Calculation:** `12e9*900/1e12`. The numerical result is **10.8 gigatonnes**. Explicitly verify its units and interpretation; the number is a conditional result from invented inputs, not a documented observation. **Sensitivity:** perturb the dominant uncertain input by 10% and report what changes. Volume-to-mass conversion assumes representative density. Explain which excluded process might invalidate the simplified estimate.


### Limits, confounding and counterfactual reasoning

Volume change must be converted using density assumptions, and regional sea level is not globally uniform. Contrast an alternative mechanism and state an observation that could discriminate between them. A more complex fitted curve is not necessarily a better causal explanation. Record station metadata, climate regime and measurement support before transferring a conclusion to a new situation.


### Practical study investigation

Prepare a coastal planning note that states which ice terms enter global mean sea-level accounting. Use `datasets/unit-04-synthetic.csv` for reproducible practice: plot the yearly variable and a five-year average while stating what the smoothing removes; annotate potential instrument error and a rival hypothesis. Reserve some observations for an independent check. The synthetic values are not validated natural observations, and apparent agreement with an illustrative model is not climate-data verification.


### Conceptual checks and problem set

1. Draw the physical process underlying **Glacier mass balance and sea level**, then label the state variables, external forcing, feedbacks and observational boundary. Which label is least well supported?
2. Reproduce the worked example with all unit conversions visible. Change one assumed value by 10%; report the new answer and interpret whether its sign or scale is plausible.
3. Explain how **volume change must be converted using density assumptions, and regional sea level is not globally uniform.** Give one additional observable that would distinguish this issue from the core mechanism.
4. Translate the case into an observational protocol: station placement, sample frequency, calibration information, data exclusion rules and one independent validation source.
5. Identify a failure mode for the proposed task: **Prepare a coastal planning note that states which ice terms enter global mean sea-level accounting.** Explain how biased sampling, omitted uncertainty or changes in the measurement system could produce a misleading conclusion.

**Answer expectations:** A competent response states the physical assumption, uses correctly dimensioned quantities, provides an interpretation in the context of the mechanism, reports an alternative explanation, and explicitly distinguishes fictional numerical inputs from observed climatological evidence. Answers that assert an exact future climate outcome from these toy equations require independent validation.


## Lesson 4.3 — Permafrost, soil carbon and hydrology

### The physical question

Permafrost thaw changes water movement, ground stability and microbial carbon processing. Some sites become wetter and favor methane generation; others dry and release more carbon dioxide. Carbon stocks, release rates and future warming response are different variables. For the synthetic case, distinguish measured state, forcing, feedback, trend and any fitted relationship. An observed long-term change must be distinguished from sampling artifacts, internal variability and reference-period effects. Record the spatial scale, instrument history and averaging interval.


### From fundamental laws to an operational approximation

Begin by diagramming **snow, vegetation and ocean surface feedbacks** and labeling **surface water, carbon and energy transfers**. Choose a defensible statistical estimator, physical balance or mass-budget relationship appropriate to this topic. Distinguish the underlying process from the approximations in a fitted model, observational indicator or toy equation. Check dimensions and direction conventions before calculating; climate fields may be spatially varying even when one chart appears constant.


### What observations could distinguish mechanisms?

Measure a fictional active-layer depth and soil moisture gradient across a thawing transect. Identify the observation time, position, calibration information and observational resolution. Contrast **satellite ice/vegetation field**, **ground mass or carbon measurements** and **independent regional water balance**. A strong analysis identifies at least one independent variable, region or time interval where competing explanations make different predictions. In particular, assess uncertainty hidden by reporting a single estimate; never use the same evidence both to tune a hypothesis and to claim its independent confirmation.


### Worked numerical case — Active-layer deepening

**Fictional data:** Frozen-ground seasonal thaw depth rises from 0.64 m to 0.89 m.

**Calculation:** `0.89-0.64`. The numerical result is **0.25 m**. Explicitly verify its units and interpretation; the number is a conditional result from invented inputs, not a documented observation. **Sensitivity:** perturb the dominant uncertain input by 10% and report what changes. One site cannot establish regional thaw trends. Explain which excluded process might invalidate the simplified estimate.


### Limits, confounding and counterfactual reasoning

A short chamber flux record cannot establish the multi-decade landscape carbon budget. Contrast an alternative mechanism and state an observation that could discriminate between them. A more complex fitted curve is not necessarily a better causal explanation. Record station metadata, climate regime and measurement support before transferring a conclusion to a new situation.


### Practical study investigation

Design a study that combines soil cores, chambers, vegetation surveys and hydrology. Use `datasets/unit-04-synthetic.csv` for reproducible practice: plot the yearly variable and a five-year average while stating what the smoothing removes; annotate potential instrument error and a rival hypothesis. Reserve some observations for an independent check. The synthetic values are not validated natural observations, and apparent agreement with an illustrative model is not climate-data verification.


### Conceptual checks and problem set

1. Draw the physical process underlying **Permafrost, soil carbon and hydrology**, then label the state variables, external forcing, feedbacks and observational boundary. Which label is least well supported?
2. Reproduce the worked example with all unit conversions visible. Change one assumed value by 10%; report the new answer and interpret whether its sign or scale is plausible.
3. Explain how **a short chamber flux record cannot establish the multi-decade landscape carbon budget.** Give one additional observable that would distinguish this issue from the core mechanism.
4. Translate the case into an observational protocol: station placement, sample frequency, calibration information, data exclusion rules and one independent validation source.
5. Identify a failure mode for the proposed task: **Design a study that combines soil cores, chambers, vegetation surveys and hydrology.** Explain how biased sampling, omitted uncertainty or changes in the measurement system could produce a misleading conclusion.

**Answer expectations:** A competent response states the physical assumption, uses correctly dimensioned quantities, provides an interpretation in the context of the mechanism, reports an alternative explanation, and explicitly distinguishes fictional numerical inputs from observed climatological evidence. Answers that assert an exact future climate outcome from these toy equations require independent validation.


## Lesson 4.4 — Terrestrial ecosystems and surface exchange

### The physical question

Vegetation modifies evapotranspiration, aerodynamic roughness, surface albedo and carbon uptake. Deforestation can warm or cool regional surfaces depending on latitude, season, cloud and moisture response. Gross primary productivity is not identical to long-term net carbon storage. For the synthetic case, distinguish measured state, forcing, feedback, trend and any fitted relationship. An observed long-term change must be distinguished from sampling artifacts, internal variability and reference-period effects. Record the spatial scale, instrument history and averaging interval.


### From fundamental laws to an operational approximation

Begin by diagramming **snow, vegetation and ocean surface feedbacks** and labeling **surface water, carbon and energy transfers**. Choose a defensible statistical estimator, physical balance or mass-budget relationship appropriate to this topic. Distinguish the underlying process from the approximations in a fitted model, observational indicator or toy equation. Check dimensions and direction conventions before calculating; climate fields may be spatially varying even when one chart appears constant.


### What observations could distinguish mechanisms?

Compare eddy-covariance, leaf-area and satellite records following a hypothetical forest disturbance. Identify the observation time, position, calibration information and observational resolution. Contrast **satellite ice/vegetation field**, **ground mass or carbon measurements** and **independent regional water balance**. A strong analysis identifies at least one independent variable, region or time interval where competing explanations make different predictions. In particular, assess changing reference periods; never use the same evidence both to tune a hypothesis and to claim its independent confirmation.


### Worked numerical case — Forest net carbon balance

**Fictional data:** Fictional ecosystem GPP 1250 and total respiration 1010 g C/m²/yr.

**Calculation:** `1250-1010`. The numerical result is **240 g C/m²/yr**. Explicitly verify its units and interpretation; the number is a conditional result from invented inputs, not a documented observation. **Sensitivity:** perturb the dominant uncertain input by 10% and report what changes. Disturbance losses, exports and full ecosystem boundary matter. Explain which excluded process might invalidate the simplified estimate.


### Limits, confounding and counterfactual reasoning

A greener satellite pixel may reflect rainfall variability rather than persistent ecosystem carbon uptake. Contrast an alternative mechanism and state an observation that could discriminate between them. A more complex fitted curve is not necessarily a better causal explanation. Record station metadata, climate regime and measurement support before transferring a conclusion to a new situation.


### Practical study investigation

Compute a simplified net ecosystem carbon balance and evaluate storage permanence. Use `datasets/unit-04-synthetic.csv` for reproducible practice: plot the yearly variable and a five-year average while stating what the smoothing removes; annotate potential instrument error and a rival hypothesis. Reserve some observations for an independent check. The synthetic values are not validated natural observations, and apparent agreement with an illustrative model is not climate-data verification.


### Conceptual checks and problem set

1. Draw the physical process underlying **Terrestrial ecosystems and surface exchange**, then label the state variables, external forcing, feedbacks and observational boundary. Which label is least well supported?
2. Reproduce the worked example with all unit conversions visible. Change one assumed value by 10%; report the new answer and interpret whether its sign or scale is plausible.
3. Explain how **a greener satellite pixel may reflect rainfall variability rather than persistent ecosystem carbon uptake.** Give one additional observable that would distinguish this issue from the core mechanism.
4. Translate the case into an observational protocol: station placement, sample frequency, calibration information, data exclusion rules and one independent validation source.
5. Identify a failure mode for the proposed task: **Compute a simplified net ecosystem carbon balance and evaluate storage permanence.** Explain how biased sampling, omitted uncertainty or changes in the measurement system could produce a misleading conclusion.

**Answer expectations:** A competent response states the physical assumption, uses correctly dimensioned quantities, provides an interpretation in the context of the mechanism, reports an alternative explanation, and explicitly distinguishes fictional numerical inputs from observed climatological evidence. Answers that assert an exact future climate outcome from these toy equations require independent validation.


## Lesson 4.5 — Carbon reservoirs, fluxes and residence times

### The physical question

Atmosphere, land, ocean and geologic reservoirs exchange carbon through multiple pathways. A residence time for an individual molecule is not the adjustment time of an added fossil-carbon pulse, because removal processes and reservoirs are coupled. Conservation requires clear sign conventions and external source terms. For the synthetic case, distinguish measured state, forcing, feedback, trend and any fitted relationship. An observed long-term change must be distinguished from sampling artifacts, internal variability and reference-period effects. Record the spatial scale, instrument history and averaging interval.


### From fundamental laws to an operational approximation

Begin by diagramming **snow, vegetation and ocean surface feedbacks** and labeling **surface water, carbon and energy transfers**. Choose a defensible statistical estimator, physical balance or mass-budget relationship appropriate to this topic. Distinguish the underlying process from the approximations in a fitted model, observational indicator or toy equation. Check dimensions and direction conventions before calculating; climate fields may be spatially varying even when one chart appears constant.


### What observations could distinguish mechanisms?

Track a toy three-box carbon inventory and a separately labeled fossil emission input over multiple steps. Identify the observation time, position, calibration information and observational resolution. Contrast **satellite ice/vegetation field**, **ground mass or carbon measurements** and **independent regional water balance**. A strong analysis identifies at least one independent variable, region or time interval where competing explanations make different predictions. In particular, assess time autocorrelation; never use the same evidence both to tune a hypothesis and to claim its independent confirmation.


### Worked numerical case — Mass-balance carbon ledger

**Fictional data:** Atmospheric source 10 Gt C/yr; sink terms 3 and 2 Gt C/yr in a toy model.

**Calculation:** `10-3-2`. The numerical result is **5 Gt C/yr**. Explicitly verify its units and interpretation; the number is a conditional result from invented inputs, not a documented observation. **Sensitivity:** perturb the dominant uncertain input by 10% and report what changes. Sinks are not universally fixed fractions of emissions. Explain which excluded process might invalidate the simplified estimate.


### Limits, confounding and counterfactual reasoning

A single fixed percentage removal rate is not a reliable long-horizon model of cumulative emissions. Contrast an alternative mechanism and state an observation that could discriminate between them. A more complex fitted curve is not necessarily a better causal explanation. Record station metadata, climate regime and measurement support before transferring a conclusion to a new situation.


### Practical study investigation

Write a mass-conserving model with units in gigatonnes of carbon and identify unmodeled feedbacks. Use `datasets/unit-04-synthetic.csv` for reproducible practice: plot the yearly variable and a five-year average while stating what the smoothing removes; annotate potential instrument error and a rival hypothesis. Reserve some observations for an independent check. The synthetic values are not validated natural observations, and apparent agreement with an illustrative model is not climate-data verification.


### Conceptual checks and problem set

1. Draw the physical process underlying **Carbon reservoirs, fluxes and residence times**, then label the state variables, external forcing, feedbacks and observational boundary. Which label is least well supported?
2. Reproduce the worked example with all unit conversions visible. Change one assumed value by 10%; report the new answer and interpret whether its sign or scale is plausible.
3. Explain how **a single fixed percentage removal rate is not a reliable long-horizon model of cumulative emissions.** Give one additional observable that would distinguish this issue from the core mechanism.
4. Translate the case into an observational protocol: station placement, sample frequency, calibration information, data exclusion rules and one independent validation source.
5. Identify a failure mode for the proposed task: **Write a mass-conserving model with units in gigatonnes of carbon and identify unmodeled feedbacks.** Explain how biased sampling, omitted uncertainty or changes in the measurement system could produce a misleading conclusion.

**Answer expectations:** A competent response states the physical assumption, uses correctly dimensioned quantities, provides an interpretation in the context of the mechanism, reports an alternative explanation, and explicitly distinguishes fictional numerical inputs from observed climatological evidence. Answers that assert an exact future climate outcome from these toy equations require independent validation.


## Unit 4 capstone — A reproducible climate-science argument

Start from the research question **How do ice, soil, vegetation and the carbon cycle modify climate and respond to it?**. Create an evidence map that distinguishes the three sources **satellite ice/vegetation field**, **ground mass or carbon measurements** and **independent regional water balance**. The first source should establish the main physical state, the second should show whether the proposed forcing was present, and the third should offer a genuinely independent check. For the synthetic scenario, state a primary hypothesis and an alternative that differs in mechanism rather than merely in parameter size. Specify what both would predict for the same geographic area under different observing or forcing conditions. In your technical report, use no unexplained uncertainty bars; distinguish calibration limits, observation support, model approximation, initialization errors, and uncertainty about the process itself.

**Data and reproducibility task:** Read the 30 synthetic records for this unit. Interpret the annual year column as a time axis, calculate a decadal mean and robust spread, and repeat the trend after withholding every fifth year. If the trend changes materially, explain whether the underlying signal might be under-sampled. Prepare a plain-language summary of what the dataset can and cannot support. Supply enough detail that another student can reproduce every calculation without contacting the author. Account for spatial coverage and lagged feedbacks before claiming a causal sequence.

**Critical discussion:** Suppose an institution must make a decision from the available analysis. Identify the evidence that is missing, the consequence of a false alarm versus a missed event, and the observation that would most efficiently reduce consequential uncertainty. Provide a direct recommendation only when the dataset and problem definition warrant one. Never treat synthetic climatological examples as an operational alert or regulatory threshold.

## Key takeaways for Unit 4

- The subject is an coupled climate system, not just an isolated plotted correlation; a defensible explanation must respect fundamental balances.
- The measurement domain, spatial scale, averaging interval and uncertainty control what can be inferred.
- The worked formulas expose sensitivity and limiting assumptions, not an automatic prediction for an unobserved site.
- A scientifically meaningful alternative hypothesis requires an observation that could falsify it.
- Operational warnings require responsible climatological services and independently validated evidence.
