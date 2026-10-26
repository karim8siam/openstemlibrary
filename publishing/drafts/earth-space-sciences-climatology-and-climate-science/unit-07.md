# Unit 7 — Extremes, attribution and compound hazards
## The central climate-science investigation

**Question:** How are changes in heat, precipitation, drought and coastal risks measured and attributed?

**Case setting:** A fictional river basin experiences simultaneous heat stress, crop failure and heavy precipitation. All locations and observations in the following investigation are synthetic. The purpose is to learn which inference would survive contact with independent measurements, rather than to produce a plausible-sounding story from an incomplete climate map.

A climate extreme is defined relative to a variable, time scale, location, threshold and often a historical reference period. Mean warming can change the frequency of high-temperature thresholds; rainfall and drought also depend on circulation, land surface and hydrological storage. Even a well-supported general physical mechanism does not establish an exact future flood level or the cause of one damaging event.

Attribution is an explicit counterfactual comparison: probabilities in a climate with observed forcing versus an otherwise defined climate without that forcing. Large ensembles and independent observations help, but limited rare-event samples create substantial uncertainty. Compound hazards depend on statistical dependence and physical interactions. Exposure and vulnerability shape damages, which are not determined by meteorology alone.

### Working boundaries and research assumptions

The effective observational transect for this unit runs from **statistical extremes to actual exposure and consequences**. Different forms of evidence support different kinds of inference: observed event definition constrains one aspect, counterfactual modeled distribution another, and independent exposure and hazard record a third. These are not interchangeable. A flux through a boundary differs from stored heat or carbon; a baseline-dependent anomaly is not an absolute state; a correlation alone cannot establish forcing attribution. Choose a geographic domain or explicit accounting boundary before writing the governing relationship. Record the averaging period and the geographical support used in comparisons.

The final project estimates a toy risk ratio and a joint-event frequency from synthetic counts, then writes a transparent limitation statement and a plan for collecting real evidence.

### What success looks like

A strong unit report reconstructs a physical chain from forcing to response while maintaining the distinction between an observation, a calculation, a model hypothesis and a decision. Include a figure that cannot be understood without axis units, a written alternative explanation and a comparison with a second type of evidence. Give a conditional risk assessment without pretending that a synthetic event was observed.


## Lesson 7.1 — Changes in heat extremes and thresholds

### The physical question

Heat hazards depend on temperature, humidity, duration, nighttime recovery and human vulnerability. Distribution shifts can change exceedance frequency even when variability stays constant, but changes in spread or persistence matter too. Urban heat islands affect local exposure and should not be conflated with global climate trend measures. For the synthetic case, distinguish measured state, forcing, feedback, trend and any fitted relationship. An observed long-term change must be distinguished from sampling artifacts, internal variability and reference-period effects. Record the spatial scale, instrument history and averaging interval.


### From fundamental laws to an operational approximation

Begin by diagramming **statistical extremes to actual exposure and consequences** and labeling **hazard distribution and exposed assets**. Choose a defensible statistical estimator, physical balance or mass-budget relationship appropriate to this topic. Distinguish the underlying process from the approximations in a fitted model, observational indicator or toy equation. Check dimensions and direction conventions before calculating; climate fields may be spatially varying even when one chart appears constant.


### What observations could distinguish mechanisms?

Calculate exceedance probabilities before and after shifting a hypothetical normal temperature distribution. Identify the observation time, position, calibration information and observational resolution. Contrast **observed event definition**, **counterfactual modeled distribution** and **independent exposure and hazard record**. A strong analysis identifies at least one independent variable, region or time interval where competing explanations make different predictions. In particular, assess a distribution that is non-stationary; never use the same evidence both to tune a hypothesis and to claim its independent confirmation.


### Worked numerical case — Temperature exceedance change

**Fictional data:** Synthetic hot-day counts increase from 8 to 22 in a 100-day window.

**Calculation:** `22-8`. The numerical result is **14 additional days**. Explicitly verify its units and interpretation; the number is a conditional result from invented inputs, not a documented observation. **Sensitivity:** perturb the dominant uncertain input by 10% and report what changes. Compare equivalent periods and measurement support. Explain which excluded process might invalidate the simplified estimate.


### Limits, confounding and counterfactual reasoning

A threshold defined for one climate period can be inappropriate for another risk decision or local acclimatization context. Contrast an alternative mechanism and state an observation that could discriminate between them. A more complex fitted curve is not necessarily a better causal explanation. Record station metadata, climate regime and measurement support before transferring a conclusion to a new situation.


### Practical study investigation

Compare days above a threshold, warm nights and three-day spell frequency with identical baseline dates. Use `datasets/unit-07-synthetic.csv` for reproducible practice: plot the yearly variable and a five-year average while stating what the smoothing removes; annotate potential instrument error and a rival hypothesis. Reserve some observations for an independent check. The synthetic values are not validated natural observations, and apparent agreement with an illustrative model is not climate-data verification.


### Conceptual checks and problem set

1. Draw the physical process underlying **Changes in heat extremes and thresholds**, then label the state variables, external forcing, feedbacks and observational boundary. Which label is least well supported?
2. Reproduce the worked example with all unit conversions visible. Change one assumed value by 10%; report the new answer and interpret whether its sign or scale is plausible.
3. Explain how **a threshold defined for one climate period can be inappropriate for another risk decision or local acclimatization context.** Give one additional observable that would distinguish this issue from the core mechanism.
4. Translate the case into an observational protocol: station placement, sample frequency, calibration information, data exclusion rules and one independent validation source.
5. Identify a failure mode for the proposed task: **Compare days above a threshold, warm nights and three-day spell frequency with identical baseline dates.** Explain how biased sampling, omitted uncertainty or changes in the measurement system could produce a misleading conclusion.

**Answer expectations:** A competent response states the physical assumption, uses correctly dimensioned quantities, provides an interpretation in the context of the mechanism, reports an alternative explanation, and explicitly distinguishes fictional numerical inputs from observed climatological evidence. Answers that assert an exact future climate outcome from these toy equations require independent validation.


## Lesson 7.2 — Heavy rainfall and hydrologic translation

### The physical question

Warmer air can hold more water vapor at saturation under many conditions, but changes in precipitation extremes also depend on circulation, moisture convergence and storm organization. Flooding requires a hydrologic pathway through catchments, soils, reservoirs, tides and drainage. Rain intensity and flood depth must not be treated as the same hazard measure. For the synthetic case, distinguish measured state, forcing, feedback, trend and any fitted relationship. An observed long-term change must be distinguished from sampling artifacts, internal variability and reference-period effects. Record the spatial scale, instrument history and averaging interval.


### From fundamental laws to an operational approximation

Begin by diagramming **statistical extremes to actual exposure and consequences** and labeling **hazard distribution and exposed assets**. Choose a defensible statistical estimator, physical balance or mass-budget relationship appropriate to this topic. Distinguish the underlying process from the approximations in a fitted model, observational indicator or toy equation. Check dimensions and direction conventions before calculating; climate fields may be spatially varying even when one chart appears constant.


### What observations could distinguish mechanisms?

Compare fictional subdaily rainfall extremes with streamflow peaks while recording catchment antecedent wetness. Identify the observation time, position, calibration information and observational resolution. Contrast **observed event definition**, **counterfactual modeled distribution** and **independent exposure and hazard record**. A strong analysis identifies at least one independent variable, region or time interval where competing explanations make different predictions. In particular, assess an undocumented instrument relocation; never use the same evidence both to tune a hypothesis and to claim its independent confirmation.


### Worked numerical case — Extreme rainfall total

**Fictional data:** A fictional rainfall episode averages 34 mm/h for 3 hours.

**Calculation:** `34*3`. The numerical result is **102 mm**. Explicitly verify its units and interpretation; the number is a conditional result from invented inputs, not a documented observation. **Sensitivity:** perturb the dominant uncertain input by 10% and report what changes. A uniform rainfall rate is a simplification. Explain which excluded process might invalidate the simplified estimate.


### Limits, confounding and counterfactual reasoning

A physical thermodynamic scaling cannot directly predict local flood loss without exposure and runoff modeling. Contrast an alternative mechanism and state an observation that could discriminate between them. A more complex fitted curve is not necessarily a better causal explanation. Record station metadata, climate regime and measurement support before transferring a conclusion to a new situation.


### Practical study investigation

Develop a causal chain from moisture source to precipitation to streamflow to damage. Use `datasets/unit-07-synthetic.csv` for reproducible practice: plot the yearly variable and a five-year average while stating what the smoothing removes; annotate potential instrument error and a rival hypothesis. Reserve some observations for an independent check. The synthetic values are not validated natural observations, and apparent agreement with an illustrative model is not climate-data verification.


### Conceptual checks and problem set

1. Draw the physical process underlying **Heavy rainfall and hydrologic translation**, then label the state variables, external forcing, feedbacks and observational boundary. Which label is least well supported?
2. Reproduce the worked example with all unit conversions visible. Change one assumed value by 10%; report the new answer and interpret whether its sign or scale is plausible.
3. Explain how **a physical thermodynamic scaling cannot directly predict local flood loss without exposure and runoff modeling.** Give one additional observable that would distinguish this issue from the core mechanism.
4. Translate the case into an observational protocol: station placement, sample frequency, calibration information, data exclusion rules and one independent validation source.
5. Identify a failure mode for the proposed task: **Develop a causal chain from moisture source to precipitation to streamflow to damage.** Explain how biased sampling, omitted uncertainty or changes in the measurement system could produce a misleading conclusion.

**Answer expectations:** A competent response states the physical assumption, uses correctly dimensioned quantities, provides an interpretation in the context of the mechanism, reports an alternative explanation, and explicitly distinguishes fictional numerical inputs from observed climatological evidence. Answers that assert an exact future climate outcome from these toy equations require independent validation.


## Lesson 7.3 — Drought and aridity metrics

### The physical question

Meteorological drought describes deficits relative to typical precipitation; agricultural and hydrological drought involve soil moisture and water availability. Higher atmospheric evaporative demand can worsen some droughts without a corresponding reduction in annual precipitation. Indices have varying averaging windows and statistical reference periods. For the synthetic case, distinguish measured state, forcing, feedback, trend and any fitted relationship. An observed long-term change must be distinguished from sampling artifacts, internal variability and reference-period effects. Record the spatial scale, instrument history and averaging interval.


### From fundamental laws to an operational approximation

Begin by diagramming **statistical extremes to actual exposure and consequences** and labeling **hazard distribution and exposed assets**. Choose a defensible statistical estimator, physical balance or mass-budget relationship appropriate to this topic. Distinguish the underlying process from the approximations in a fitted model, observational indicator or toy equation. Check dimensions and direction conventions before calculating; climate fields may be spatially varying even when one chart appears constant.


### What observations could distinguish mechanisms?

Compare precipitation anomalies, modeled soil moisture and reservoir storage for the same fictional dry season. Identify the observation time, position, calibration information and observational resolution. Contrast **observed event definition**, **counterfactual modeled distribution** and **independent exposure and hazard record**. A strong analysis identifies at least one independent variable, region or time interval where competing explanations make different predictions. In particular, assess heterogeneous geographic coverage; never use the same evidence both to tune a hypothesis and to claim its independent confirmation.


### Worked numerical case — Drought soil moisture deficit

**Fictional data:** Root-zone storage fell from 115 to 83 mm.

**Calculation:** `115-83`. The numerical result is **32 mm storage deficit**. Explicitly verify its units and interpretation; the number is a conditional result from invented inputs, not a documented observation. **Sensitivity:** perturb the dominant uncertain input by 10% and report what changes. Not the same as seasonal rainfall shortage. Explain which excluded process might invalidate the simplified estimate.


### Limits, confounding and counterfactual reasoning

A short dry spell can be severe for crops yet not qualify as multiyear hydrological drought. Contrast an alternative mechanism and state an observation that could discriminate between them. A more complex fitted curve is not necessarily a better causal explanation. Record station metadata, climate regime and measurement support before transferring a conclusion to a new situation.


### Practical study investigation

Construct a table of stakeholder-relevant metrics and explicit thresholds. Use `datasets/unit-07-synthetic.csv` for reproducible practice: plot the yearly variable and a five-year average while stating what the smoothing removes; annotate potential instrument error and a rival hypothesis. Reserve some observations for an independent check. The synthetic values are not validated natural observations, and apparent agreement with an illustrative model is not climate-data verification.


### Conceptual checks and problem set

1. Draw the physical process underlying **Drought and aridity metrics**, then label the state variables, external forcing, feedbacks and observational boundary. Which label is least well supported?
2. Reproduce the worked example with all unit conversions visible. Change one assumed value by 10%; report the new answer and interpret whether its sign or scale is plausible.
3. Explain how **a short dry spell can be severe for crops yet not qualify as multiyear hydrological drought.** Give one additional observable that would distinguish this issue from the core mechanism.
4. Translate the case into an observational protocol: station placement, sample frequency, calibration information, data exclusion rules and one independent validation source.
5. Identify a failure mode for the proposed task: **Construct a table of stakeholder-relevant metrics and explicit thresholds.** Explain how biased sampling, omitted uncertainty or changes in the measurement system could produce a misleading conclusion.

**Answer expectations:** A competent response states the physical assumption, uses correctly dimensioned quantities, provides an interpretation in the context of the mechanism, reports an alternative explanation, and explicitly distinguishes fictional numerical inputs from observed climatological evidence. Answers that assert an exact future climate outcome from these toy equations require independent validation.


## Lesson 7.4 — Event attribution and counterfactual worlds

### The physical question

Event attribution compares the likelihood or intensity of a defined event in actual and counterfactual climate conditions using observations and models. The event definition, duration, spatial footprint and preselected threshold materially affect results. A risk ratio requires reasonable estimates of two event probabilities. For the synthetic case, distinguish measured state, forcing, feedback, trend and any fitted relationship. An observed long-term change must be distinguished from sampling artifacts, internal variability and reference-period effects. Record the spatial scale, instrument history and averaging interval.


### From fundamental laws to an operational approximation

Begin by diagramming **statistical extremes to actual exposure and consequences** and labeling **hazard distribution and exposed assets**. Choose a defensible statistical estimator, physical balance or mass-budget relationship appropriate to this topic. Distinguish the underlying process from the approximations in a fitted model, observational indicator or toy equation. Check dimensions and direction conventions before calculating; climate fields may be spatially varying even when one chart appears constant.


### What observations could distinguish mechanisms?

Estimate probabilities in two fictional ensembles under the same event definition and quantify sampling uncertainty. Identify the observation time, position, calibration information and observational resolution. Contrast **observed event definition**, **counterfactual modeled distribution** and **independent exposure and hazard record**. A strong analysis identifies at least one independent variable, region or time interval where competing explanations make different predictions. In particular, assess a possible common forcing; never use the same evidence both to tune a hypothesis and to claim its independent confirmation.


### Worked numerical case — Attribution risk ratio

**Fictional data:** Toy event probabilities are 0.10 in a factual world and 0.04 in counterfactual.

**Calculation:** `0.10/0.04`. The numerical result is **2.5 risk ratio**. Explicitly verify its units and interpretation; the number is a conditional result from invented inputs, not a documented observation. **Sensitivity:** perturb the dominant uncertain input by 10% and report what changes. Sampling uncertainty and event definition must be supplied. Explain which excluded process might invalidate the simplified estimate.


### Limits, confounding and counterfactual reasoning

Rare-event probabilities near zero are especially unstable; an infinite estimated risk ratio is not automatically a physical infinity. Contrast an alternative mechanism and state an observation that could discriminate between them. A more complex fitted curve is not necessarily a better causal explanation. Record station metadata, climate regime and measurement support before transferring a conclusion to a new situation.


### Practical study investigation

State three assumptions that must hold before drawing a causal attribution conclusion. Use `datasets/unit-07-synthetic.csv` for reproducible practice: plot the yearly variable and a five-year average while stating what the smoothing removes; annotate potential instrument error and a rival hypothesis. Reserve some observations for an independent check. The synthetic values are not validated natural observations, and apparent agreement with an illustrative model is not climate-data verification.


### Conceptual checks and problem set

1. Draw the physical process underlying **Event attribution and counterfactual worlds**, then label the state variables, external forcing, feedbacks and observational boundary. Which label is least well supported?
2. Reproduce the worked example with all unit conversions visible. Change one assumed value by 10%; report the new answer and interpret whether its sign or scale is plausible.
3. Explain how **rare-event probabilities near zero are especially unstable; an infinite estimated risk ratio is not automatically a physical infinity.** Give one additional observable that would distinguish this issue from the core mechanism.
4. Translate the case into an observational protocol: station placement, sample frequency, calibration information, data exclusion rules and one independent validation source.
5. Identify a failure mode for the proposed task: **State three assumptions that must hold before drawing a causal attribution conclusion.** Explain how biased sampling, omitted uncertainty or changes in the measurement system could produce a misleading conclusion.

**Answer expectations:** A competent response states the physical assumption, uses correctly dimensioned quantities, provides an interpretation in the context of the mechanism, reports an alternative explanation, and explicitly distinguishes fictional numerical inputs from observed climatological evidence. Answers that assert an exact future climate outcome from these toy equations require independent validation.


## Lesson 7.5 — Compound events, cascading risks and exposure

### The physical question

Co-occurring or sequential hazards can interact: drought followed by heat, storm surge with heavy rainfall, or heat stress with power failure. Dependence between hazards matters; multiplying separate probabilities is invalid without an independence assumption. Losses also reflect the social and physical systems exposed. For the synthetic case, distinguish measured state, forcing, feedback, trend and any fitted relationship. An observed long-term change must be distinguished from sampling artifacts, internal variability and reference-period effects. Record the spatial scale, instrument history and averaging interval.


### From fundamental laws to an operational approximation

Begin by diagramming **statistical extremes to actual exposure and consequences** and labeling **hazard distribution and exposed assets**. Choose a defensible statistical estimator, physical balance or mass-budget relationship appropriate to this topic. Distinguish the underlying process from the approximations in a fitted model, observational indicator or toy equation. Check dimensions and direction conventions before calculating; climate fields may be spatially varying even when one chart appears constant.


### What observations could distinguish mechanisms?

Compute a joint-event frequency from a synthetic contingency table and compare it with an independence estimate. Identify the observation time, position, calibration information and observational resolution. Contrast **observed event definition**, **counterfactual modeled distribution** and **independent exposure and hazard record**. A strong analysis identifies at least one independent variable, region or time interval where competing explanations make different predictions. In particular, assess a distribution that is non-stationary; never use the same evidence both to tune a hypothesis and to claim its independent confirmation.


### Worked numerical case — Compound-event dependence

**Fictional data:** In 120 synthetic seasons, both heat and drought occurred together in 18.

**Calculation:** `100*18/120`. The numerical result is **15 %**. Explicitly verify its units and interpretation; the number is a conditional result from invented inputs, not a documented observation. **Sensitivity:** perturb the dominant uncertain input by 10% and report what changes. A short joint frequency is not a stable rare-event probability. Explain which excluded process might invalidate the simplified estimate.


### Limits, confounding and counterfactual reasoning

Correlation over a short record does not establish the dependence structure of very rare combinations. Contrast an alternative mechanism and state an observation that could discriminate between them. A more complex fitted curve is not necessarily a better causal explanation. Record station metadata, climate regime and measurement support before transferring a conclusion to a new situation.


### Practical study investigation

Map a cascading impact pathway and identify one intervention at each stage. Use `datasets/unit-07-synthetic.csv` for reproducible practice: plot the yearly variable and a five-year average while stating what the smoothing removes; annotate potential instrument error and a rival hypothesis. Reserve some observations for an independent check. The synthetic values are not validated natural observations, and apparent agreement with an illustrative model is not climate-data verification.


### Conceptual checks and problem set

1. Draw the physical process underlying **Compound events, cascading risks and exposure**, then label the state variables, external forcing, feedbacks and observational boundary. Which label is least well supported?
2. Reproduce the worked example with all unit conversions visible. Change one assumed value by 10%; report the new answer and interpret whether its sign or scale is plausible.
3. Explain how **correlation over a short record does not establish the dependence structure of very rare combinations.** Give one additional observable that would distinguish this issue from the core mechanism.
4. Translate the case into an observational protocol: station placement, sample frequency, calibration information, data exclusion rules and one independent validation source.
5. Identify a failure mode for the proposed task: **Map a cascading impact pathway and identify one intervention at each stage.** Explain how biased sampling, omitted uncertainty or changes in the measurement system could produce a misleading conclusion.

**Answer expectations:** A competent response states the physical assumption, uses correctly dimensioned quantities, provides an interpretation in the context of the mechanism, reports an alternative explanation, and explicitly distinguishes fictional numerical inputs from observed climatological evidence. Answers that assert an exact future climate outcome from these toy equations require independent validation.


## Unit 7 capstone — A reproducible climate-science argument

Start from the research question **How are changes in heat, precipitation, drought and coastal risks measured and attributed?**. Create an evidence map that distinguishes the three sources **observed event definition**, **counterfactual modeled distribution** and **independent exposure and hazard record**. The first source should establish the main physical state, the second should show whether the proposed forcing was present, and the third should offer a genuinely independent check. For the synthetic scenario, state a primary hypothesis and an alternative that differs in mechanism rather than merely in parameter size. Specify what both would predict for the same geographic area under different observing or forcing conditions. In your technical report, use no unexplained uncertainty bars; distinguish calibration limits, observation support, model approximation, initialization errors, and uncertainty about the process itself.

**Data and reproducibility task:** Read the 30 synthetic records for this unit. Interpret the annual year column as a time axis, calculate a decadal mean and robust spread, and repeat the trend after withholding every fifth year. If the trend changes materially, explain whether the underlying signal might be under-sampled. Prepare a plain-language summary of what the dataset can and cannot support. Supply enough detail that another student can reproduce every calculation without contacting the author. Give a conditional risk assessment without pretending that a synthetic event was observed.

**Critical discussion:** Suppose an institution must make a decision from the available analysis. Identify the evidence that is missing, the consequence of a false alarm versus a missed event, and the observation that would most efficiently reduce consequential uncertainty. Provide a direct recommendation only when the dataset and problem definition warrant one. Never treat synthetic climatological examples as an operational alert or regulatory threshold.

## Key takeaways for Unit 7

- The subject is an coupled climate system, not just an isolated plotted correlation; a defensible explanation must respect fundamental balances.
- The measurement domain, spatial scale, averaging interval and uncertainty control what can be inferred.
- The worked formulas expose sensitivity and limiting assumptions, not an automatic prediction for an unobserved site.
- A scientifically meaningful alternative hypothesis requires an observation that could falsify it.
- Operational warnings require responsible climatological services and independently validated evidence.
