# Unit 3 — Atmosphere–ocean circulation and variability
## The central climate-science investigation

**Question:** How do circulation, ocean storage and coupled oscillations redistribute heat, freshwater and momentum?

**Case setting:** A synthetic tropical Pacific transect develops changing winds, SST anomalies and thermocline depth. All locations and observations in the following investigation are synthetic. The purpose is to learn which inference would survive contact with independent measurements, rather than to produce a plausible-sounding story from an incomplete climate map.

The coupled climate system contains atmospheric overturning, transient eddies, ocean currents, surface fluxes and ocean mixing. A local temperature anomaly need not equal new net heat gained by the globe; transport may redistribute existing energy. Mechanisms occur on vastly different time scales, from day-to-day wind bursts to multidecadal changes in subsurface storage. Understanding this distinction prevents a regional cool anomaly from being mistaken for evidence that planetary warming has ceased.

ENSO and monsoon systems illustrate why a climate index is not a deterministic local weather forecast. Index regions and baseline periods are conventions, and changing them can alter the timing of an episode. Composite events and teleconnections should be validated using years omitted from index construction. The strength of a remote teleconnection can vary with season, background state and geography.

### Working boundaries and research assumptions

The effective observational transect for this unit runs from **tropical Pacific variability to regional circulation**. Different forms of evidence support different kinds of inference: sea-surface-temperature records constrains one aspect, wind and subsurface ocean series another, and out-of-period teleconnection verification a third. These are not interchangeable. A flux through a boundary differs from stored heat or carbon; a baseline-dependent anomaly is not an absolute state; a correlation alone cannot establish forcing attribution. Choose a geographic domain or explicit accounting boundary before writing the governing relationship. Record the averaging period and the geographical support used in comparisons.

The capstone integrates synthetic sea-surface temperature anomalies, wind indicators and heat-storage information while examining two competing causal explanations. The report must separate diagnosed association from predictive skill.

### What success looks like

A strong unit report reconstructs a physical chain from forcing to response while maintaining the distinction between an observation, a calculation, a model hypothesis and a decision. Include a figure that cannot be understood without axis units, a written alternative explanation and a comparison with a second type of evidence. Compare an atmosphere-only account with a coupled ocean explanation.


## Lesson 3.1 — Hadley, Ferrel and polar circulation

### The physical question

Solar heating gradients and rotation shape large-scale meridional overturning and midlatitude eddy transport. Hadley-cell width and strength vary seasonally and with climate state, while the Ferrel circulation is an eddy-driven mean rather than a direct simple heat engine. Zonal averages conceal strong land–ocean differences. For the synthetic case, distinguish measured state, forcing, feedback, trend and any fitted relationship. An observed long-term change must be distinguished from sampling artifacts, internal variability and reference-period effects. Record the spatial scale, instrument history and averaging interval.


### From fundamental laws to an operational approximation

Begin by diagramming **tropical Pacific variability to regional circulation** and labeling **coupled transport and heat storage**. Choose a defensible statistical estimator, physical balance or mass-budget relationship appropriate to this topic. Distinguish the underlying process from the approximations in a fitted model, observational indicator or toy equation. Check dimensions and direction conventions before calculating; climate fields may be spatially varying even when one chart appears constant.


### What observations could distinguish mechanisms?

Contrast an annual-mean latitude–height streamfunction with monthly snapshots and surface wind observations. Identify the observation time, position, calibration information and observational resolution. Contrast **sea-surface-temperature records**, **wind and subsurface ocean series** and **out-of-period teleconnection verification**. A strong analysis identifies at least one independent variable, region or time interval where competing explanations make different predictions. In particular, assess heterogeneous geographic coverage; never use the same evidence both to tune a hypothesis and to claim its independent confirmation.


### Worked numerical case — Hadley cell latitudinal span

**Fictional data:** A model subtropical boundary shifts from 28° to 31° latitude.

**Calculation:** `31-28`. The numerical result is **3 degrees latitude**. Explicitly verify its units and interpretation; the number is a conditional result from invented inputs, not a documented observation. **Sensitivity:** perturb the dominant uncertain input by 10% and report what changes. A chosen boundary depends on diagnostic definition. Explain which excluded process might invalidate the simplified estimate.


### Limits, confounding and counterfactual reasoning

A cartoon of three idealized cells is not sufficient evidence of a local monsoon anomaly. Contrast an alternative mechanism and state an observation that could discriminate between them. A more complex fitted curve is not necessarily a better causal explanation. Record station metadata, climate regime and measurement support before transferring a conclusion to a new situation.


### Practical study investigation

Interpret circulation anomalies separately as zonal mean, regional pattern and transient eddy contribution. Use `datasets/unit-03-synthetic.csv` for reproducible practice: plot the yearly variable and a five-year average while stating what the smoothing removes; annotate potential instrument error and a rival hypothesis. Reserve some observations for an independent check. The synthetic values are not validated natural observations, and apparent agreement with an illustrative model is not climate-data verification.


### Conceptual checks and problem set

1. Draw the physical process underlying **Hadley, Ferrel and polar circulation**, then label the state variables, external forcing, feedbacks and observational boundary. Which label is least well supported?
2. Reproduce the worked example with all unit conversions visible. Change one assumed value by 10%; report the new answer and interpret whether its sign or scale is plausible.
3. Explain how **a cartoon of three idealized cells is not sufficient evidence of a local monsoon anomaly.** Give one additional observable that would distinguish this issue from the core mechanism.
4. Translate the case into an observational protocol: station placement, sample frequency, calibration information, data exclusion rules and one independent validation source.
5. Identify a failure mode for the proposed task: **Interpret circulation anomalies separately as zonal mean, regional pattern and transient eddy contribution.** Explain how biased sampling, omitted uncertainty or changes in the measurement system could produce a misleading conclusion.

**Answer expectations:** A competent response states the physical assumption, uses correctly dimensioned quantities, provides an interpretation in the context of the mechanism, reports an alternative explanation, and explicitly distinguishes fictional numerical inputs from observed climatological evidence. Answers that assert an exact future climate outcome from these toy equations require independent validation.


## Lesson 3.2 — Ocean mixed layers and heat transport

### The physical question

Wind-driven mixing, buoyancy fluxes and vertical stratification control mixed-layer depth. Ocean current systems and overturning transport redistribute heat on timescales far longer than synoptic weather. A shallow mixed layer warms rapidly for a given surface flux, while deeper entrainment spreads energy through a larger mass. For the synthetic case, distinguish measured state, forcing, feedback, trend and any fitted relationship. An observed long-term change must be distinguished from sampling artifacts, internal variability and reference-period effects. Record the spatial scale, instrument history and averaging interval.


### From fundamental laws to an operational approximation

Begin by diagramming **tropical Pacific variability to regional circulation** and labeling **coupled transport and heat storage**. Choose a defensible statistical estimator, physical balance or mass-budget relationship appropriate to this topic. Distinguish the underlying process from the approximations in a fitted model, observational indicator or toy equation. Check dimensions and direction conventions before calculating; climate fields may be spatially varying even when one chart appears constant.


### What observations could distinguish mechanisms?

Compute a mixed-layer warming tendency from a surface heat flux, depth and heat capacity. Identify the observation time, position, calibration information and observational resolution. Contrast **sea-surface-temperature records**, **wind and subsurface ocean series** and **out-of-period teleconnection verification**. A strong analysis identifies at least one independent variable, region or time interval where competing explanations make different predictions. In particular, assess a possible common forcing; never use the same evidence both to tune a hypothesis and to claim its independent confirmation.


### Worked numerical case — Mixed-layer ocean warming

**Fictional data:** A 40 m water layer receives 80 W/m² for 30 days; density 1025 kg/m³, cp 3990 J/kg/K.

**Calculation:** `80*30*86400/(1025*3990*40)`. The numerical result is **1.268 K**. Explicitly verify its units and interpretation; the number is a conditional result from invented inputs, not a documented observation. **Sensitivity:** perturb the dominant uncertain input by 10% and report what changes. Neglects losses and exchange with deeper water. Explain which excluded process might invalidate the simplified estimate.


### Limits, confounding and counterfactual reasoning

A fixed-depth slab neglects lateral transport, entrainment and exchange with the atmosphere. Contrast an alternative mechanism and state an observation that could discriminate between them. A more complex fitted curve is not necessarily a better causal explanation. Record station metadata, climate regime and measurement support before transferring a conclusion to a new situation.


### Practical study investigation

Identify the observational constraints needed to estimate full-depth ocean heat storage. Use `datasets/unit-03-synthetic.csv` for reproducible practice: plot the yearly variable and a five-year average while stating what the smoothing removes; annotate potential instrument error and a rival hypothesis. Reserve some observations for an independent check. The synthetic values are not validated natural observations, and apparent agreement with an illustrative model is not climate-data verification.


### Conceptual checks and problem set

1. Draw the physical process underlying **Ocean mixed layers and heat transport**, then label the state variables, external forcing, feedbacks and observational boundary. Which label is least well supported?
2. Reproduce the worked example with all unit conversions visible. Change one assumed value by 10%; report the new answer and interpret whether its sign or scale is plausible.
3. Explain how **a fixed-depth slab neglects lateral transport, entrainment and exchange with the atmosphere.** Give one additional observable that would distinguish this issue from the core mechanism.
4. Translate the case into an observational protocol: station placement, sample frequency, calibration information, data exclusion rules and one independent validation source.
5. Identify a failure mode for the proposed task: **Identify the observational constraints needed to estimate full-depth ocean heat storage.** Explain how biased sampling, omitted uncertainty or changes in the measurement system could produce a misleading conclusion.

**Answer expectations:** A competent response states the physical assumption, uses correctly dimensioned quantities, provides an interpretation in the context of the mechanism, reports an alternative explanation, and explicitly distinguishes fictional numerical inputs from observed climatological evidence. Answers that assert an exact future climate outcome from these toy equations require independent validation.


## Lesson 3.3 — El Niño–Southern Oscillation as coupled variability

### The physical question

ENSO involves coupled changes in equatorial Pacific winds, sea-surface temperature, convection and subsurface heat. Warm and cool phases alter conditional regional rainfall probabilities but do not prescribe weather at a particular site. Indices depend on region, baseline and averaging rule. ENSO phases can occur alongside a long-term warming trend. For the synthetic case, distinguish measured state, forcing, feedback, trend and any fitted relationship. An observed long-term change must be distinguished from sampling artifacts, internal variability and reference-period effects. Record the spatial scale, instrument history and averaging interval.


### From fundamental laws to an operational approximation

Begin by diagramming **tropical Pacific variability to regional circulation** and labeling **coupled transport and heat storage**. Choose a defensible statistical estimator, physical balance or mass-budget relationship appropriate to this topic. Distinguish the underlying process from the approximations in a fitted model, observational indicator or toy equation. Check dimensions and direction conventions before calculating; climate fields may be spatially varying even when one chart appears constant.


### What observations could distinguish mechanisms?

Compare an SST anomaly index with wind-stress and thermocline indicators over the same synthetic time series. Identify the observation time, position, calibration information and observational resolution. Contrast **sea-surface-temperature records**, **wind and subsurface ocean series** and **out-of-period teleconnection verification**. A strong analysis identifies at least one independent variable, region or time interval where competing explanations make different predictions. In particular, assess a distribution that is non-stationary; never use the same evidence both to tune a hypothesis and to claim its independent confirmation.


### Worked numerical case — ENSO anomaly difference

**Fictional data:** Fictional Niño-region SST 28.1°C compared with matching normal of 27.4°C.

**Calculation:** `28.1-27.4`. The numerical result is **0.7 °C anomaly**. Explicitly verify its units and interpretation; the number is a conditional result from invented inputs, not a documented observation. **Sensitivity:** perturb the dominant uncertain input by 10% and report what changes. One SST sample is not sufficient to classify an ENSO event. Explain which excluded process might invalidate the simplified estimate.


### Limits, confounding and counterfactual reasoning

Correlated remote rainfall does not prove local causality without circulation evidence and appropriate controls. Contrast an alternative mechanism and state an observation that could discriminate between them. A more complex fitted curve is not necessarily a better causal explanation. Record station metadata, climate regime and measurement support before transferring a conclusion to a new situation.


### Practical study investigation

Build a composite with withheld years and show its sensitivity to phase thresholds. Use `datasets/unit-03-synthetic.csv` for reproducible practice: plot the yearly variable and a five-year average while stating what the smoothing removes; annotate potential instrument error and a rival hypothesis. Reserve some observations for an independent check. The synthetic values are not validated natural observations, and apparent agreement with an illustrative model is not climate-data verification.


### Conceptual checks and problem set

1. Draw the physical process underlying **El Niño–Southern Oscillation as coupled variability**, then label the state variables, external forcing, feedbacks and observational boundary. Which label is least well supported?
2. Reproduce the worked example with all unit conversions visible. Change one assumed value by 10%; report the new answer and interpret whether its sign or scale is plausible.
3. Explain how **correlated remote rainfall does not prove local causality without circulation evidence and appropriate controls.** Give one additional observable that would distinguish this issue from the core mechanism.
4. Translate the case into an observational protocol: station placement, sample frequency, calibration information, data exclusion rules and one independent validation source.
5. Identify a failure mode for the proposed task: **Build a composite with withheld years and show its sensitivity to phase thresholds.** Explain how biased sampling, omitted uncertainty or changes in the measurement system could produce a misleading conclusion.

**Answer expectations:** A competent response states the physical assumption, uses correctly dimensioned quantities, provides an interpretation in the context of the mechanism, reports an alternative explanation, and explicitly distinguishes fictional numerical inputs from observed climatological evidence. Answers that assert an exact future climate outcome from these toy equations require independent validation.


## Lesson 3.4 — Atlantic variability and overturning circulation

### The physical question

The Atlantic meridional overturning circulation transports heat and freshwater through interacting wind, density and mixing processes. Different observing systems measure transports over different depths and times, and a single surface current is not the overturning circulation. Decadal variations can overlap with externally forced change. For the synthetic case, distinguish measured state, forcing, feedback, trend and any fitted relationship. An observed long-term change must be distinguished from sampling artifacts, internal variability and reference-period effects. Record the spatial scale, instrument history and averaging interval.


### From fundamental laws to an operational approximation

Begin by diagramming **tropical Pacific variability to regional circulation** and labeling **coupled transport and heat storage**. Choose a defensible statistical estimator, physical balance or mass-budget relationship appropriate to this topic. Distinguish the underlying process from the approximations in a fitted model, observational indicator or toy equation. Check dimensions and direction conventions before calculating; climate fields may be spatially varying even when one chart appears constant.


### What observations could distinguish mechanisms?

Compare a zonally integrated transport estimate against sparse hydrographic sections and moored time series. Identify the observation time, position, calibration information and observational resolution. Contrast **sea-surface-temperature records**, **wind and subsurface ocean series** and **out-of-period teleconnection verification**. A strong analysis identifies at least one independent variable, region or time interval where competing explanations make different predictions. In particular, assess an undocumented instrument relocation; never use the same evidence both to tune a hypothesis and to claim its independent confirmation.


### Worked numerical case — Atlantic heat transport proxy

**Fictional data:** A hypothetical transport anomaly of 0.17 PW above an illustrative baseline 0.95 PW.

**Calculation:** `0.95+0.17`. The numerical result is **1.12 petawatts**. Explicitly verify its units and interpretation; the number is a conditional result from invented inputs, not a documented observation. **Sensitivity:** perturb the dominant uncertain input by 10% and report what changes. Actual overturning transport requires section-integrated velocity and temperature. Explain which excluded process might invalidate the simplified estimate.


### Limits, confounding and counterfactual reasoning

Sea-surface temperature patterns are indirect AMOC indicators, not direct measurements of basin-wide overturning transport. Contrast an alternative mechanism and state an observation that could discriminate between them. A more complex fitted curve is not necessarily a better causal explanation. Record station metadata, climate regime and measurement support before transferring a conclusion to a new situation.


### Practical study investigation

List alternative explanations and observations needed before claiming a detected long-term trend. Use `datasets/unit-03-synthetic.csv` for reproducible practice: plot the yearly variable and a five-year average while stating what the smoothing removes; annotate potential instrument error and a rival hypothesis. Reserve some observations for an independent check. The synthetic values are not validated natural observations, and apparent agreement with an illustrative model is not climate-data verification.


### Conceptual checks and problem set

1. Draw the physical process underlying **Atlantic variability and overturning circulation**, then label the state variables, external forcing, feedbacks and observational boundary. Which label is least well supported?
2. Reproduce the worked example with all unit conversions visible. Change one assumed value by 10%; report the new answer and interpret whether its sign or scale is plausible.
3. Explain how **sea-surface temperature patterns are indirect AMOC indicators, not direct measurements of basin-wide overturning transport.** Give one additional observable that would distinguish this issue from the core mechanism.
4. Translate the case into an observational protocol: station placement, sample frequency, calibration information, data exclusion rules and one independent validation source.
5. Identify a failure mode for the proposed task: **List alternative explanations and observations needed before claiming a detected long-term trend.** Explain how biased sampling, omitted uncertainty or changes in the measurement system could produce a misleading conclusion.

**Answer expectations:** A competent response states the physical assumption, uses correctly dimensioned quantities, provides an interpretation in the context of the mechanism, reports an alternative explanation, and explicitly distinguishes fictional numerical inputs from observed climatological evidence. Answers that assert an exact future climate outcome from these toy equations require independent validation.


## Lesson 3.5 — Monsoons, teleconnections and regional climate

### The physical question

Monsoon rainfall emerges from land–ocean thermal contrasts, moisture transport, topography and shifting circulation, with influences from remote ocean anomalies. Seasonal averages can hide changes in onset, intraseasonal breaks and extreme daily rainfall. Remote teleconnections are variable and regime dependent. For the synthetic case, distinguish measured state, forcing, feedback, trend and any fitted relationship. An observed long-term change must be distinguished from sampling artifacts, internal variability and reference-period effects. Record the spatial scale, instrument history and averaging interval.


### From fundamental laws to an operational approximation

Begin by diagramming **tropical Pacific variability to regional circulation** and labeling **coupled transport and heat storage**. Choose a defensible statistical estimator, physical balance or mass-budget relationship appropriate to this topic. Distinguish the underlying process from the approximations in a fitted model, observational indicator or toy equation. Check dimensions and direction conventions before calculating; climate fields may be spatially varying even when one chart appears constant.


### What observations could distinguish mechanisms?

Compare fictional seasonal accumulation and daily wet-day distributions in two monsoon years with similar totals. Identify the observation time, position, calibration information and observational resolution. Contrast **sea-surface-temperature records**, **wind and subsurface ocean series** and **out-of-period teleconnection verification**. A strong analysis identifies at least one independent variable, region or time interval where competing explanations make different predictions. In particular, assess heterogeneous geographic coverage; never use the same evidence both to tune a hypothesis and to claim its independent confirmation.


### Worked numerical case — Monsoon seasonal anomaly

**Fictional data:** A station collected 710 mm in a synthetic season with 610 mm normal.

**Calculation:** `100*(710-610)/610`. The numerical result is **16.39 %**. Explicitly verify its units and interpretation; the number is a conditional result from invented inputs, not a documented observation. **Sensitivity:** perturb the dominant uncertain input by 10% and report what changes. A rainfall anomaly alone cannot isolate a remote circulation cause. Explain which excluded process might invalidate the simplified estimate.


### Limits, confounding and counterfactual reasoning

A single teleconnection index cannot reliably predict one district without local calibration and skill assessment. Contrast an alternative mechanism and state an observation that could discriminate between them. A more complex fitted curve is not necessarily a better causal explanation. Record station metadata, climate regime and measurement support before transferring a conclusion to a new situation.


### Practical study investigation

Design an evaluation with local rainfall stations and out-of-period verification. Use `datasets/unit-03-synthetic.csv` for reproducible practice: plot the yearly variable and a five-year average while stating what the smoothing removes; annotate potential instrument error and a rival hypothesis. Reserve some observations for an independent check. The synthetic values are not validated natural observations, and apparent agreement with an illustrative model is not climate-data verification.


### Conceptual checks and problem set

1. Draw the physical process underlying **Monsoons, teleconnections and regional climate**, then label the state variables, external forcing, feedbacks and observational boundary. Which label is least well supported?
2. Reproduce the worked example with all unit conversions visible. Change one assumed value by 10%; report the new answer and interpret whether its sign or scale is plausible.
3. Explain how **a single teleconnection index cannot reliably predict one district without local calibration and skill assessment.** Give one additional observable that would distinguish this issue from the core mechanism.
4. Translate the case into an observational protocol: station placement, sample frequency, calibration information, data exclusion rules and one independent validation source.
5. Identify a failure mode for the proposed task: **Design an evaluation with local rainfall stations and out-of-period verification.** Explain how biased sampling, omitted uncertainty or changes in the measurement system could produce a misleading conclusion.

**Answer expectations:** A competent response states the physical assumption, uses correctly dimensioned quantities, provides an interpretation in the context of the mechanism, reports an alternative explanation, and explicitly distinguishes fictional numerical inputs from observed climatological evidence. Answers that assert an exact future climate outcome from these toy equations require independent validation.


## Unit 3 capstone — A reproducible climate-science argument

Start from the research question **How do circulation, ocean storage and coupled oscillations redistribute heat, freshwater and momentum?**. Create an evidence map that distinguishes the three sources **sea-surface-temperature records**, **wind and subsurface ocean series** and **out-of-period teleconnection verification**. The first source should establish the main physical state, the second should show whether the proposed forcing was present, and the third should offer a genuinely independent check. For the synthetic scenario, state a primary hypothesis and an alternative that differs in mechanism rather than merely in parameter size. Specify what both would predict for the same geographic area under different observing or forcing conditions. In your technical report, use no unexplained uncertainty bars; distinguish calibration limits, observation support, model approximation, initialization errors, and uncertainty about the process itself.

**Data and reproducibility task:** Read the 30 synthetic records for this unit. Interpret the annual year column as a time axis, calculate a decadal mean and robust spread, and repeat the trend after withholding every fifth year. If the trend changes materially, explain whether the underlying signal might be under-sampled. Prepare a plain-language summary of what the dataset can and cannot support. Supply enough detail that another student can reproduce every calculation without contacting the author. Compare an atmosphere-only account with a coupled ocean explanation.

**Critical discussion:** Suppose an institution must make a decision from the available analysis. Identify the evidence that is missing, the consequence of a false alarm versus a missed event, and the observation that would most efficiently reduce consequential uncertainty. Provide a direct recommendation only when the dataset and problem definition warrant one. Never treat synthetic climatological examples as an operational alert or regulatory threshold.

## Key takeaways for Unit 3

- The subject is an coupled climate system, not just an isolated plotted correlation; a defensible explanation must respect fundamental balances.
- The measurement domain, spatial scale, averaging interval and uncertainty control what can be inferred.
- The worked formulas expose sensitivity and limiting assumptions, not an automatic prediction for an unobserved site.
- A scientifically meaningful alternative hypothesis requires an observation that could falsify it.
- Operational warnings require responsible climatological services and independently validated evidence.
