# Unit 1 — Climate data, baselines and detection
## The central climate-science investigation

**Question:** How can a climate trend be distinguished from weather noise, instrument shifts and a changing reference period?

**Case setting:** A fictional network of seven observation sites compares temperature anomalies over several decades. All locations and observations in the following investigation are synthetic. The purpose is to learn which inference would survive contact with independent measurements, rather than to produce a plausible-sounding story from an incomplete climate map.

An observation network is an engineered sampling scheme rather than a transparent window on Earth. Measurement changes, missing seasons, unequal geographic coverage and arbitrary comparison periods can each alter a plotted anomaly. The introductory unit develops climate time series as data with physical provenance: exact coordinates, elevation, station instrument, measurement time, and the intended spatial support. A properly labeled anomaly can be reconstructed from stored absolute measurements and a baseline dataset; the reverse is not always possible without metadata.

The distinction between detection and attribution governs how evidence should be combined. Reject the argument that one anomalous year establishes a climate trajectory; equally reject using one cool week to overturn a multi-decade global result. Statistical uncertainty is not just a decorative interval: time dependence, spatial correlations and data selection affect coverage. Independent records such as ocean heat and satellite fluxes answer different questions.

### Working boundaries and research assumptions

The effective observational transect for this unit runs from **raw weather observations to area-weighted climate indicator**. Different forms of evidence support different kinds of inference: station quality-controlled time series constrains one aspect, independent neighboring climate observations another, and baseline sensitivity analysis a third. These are not interchangeable. A flux through a boundary differs from stored heat or carbon; a baseline-dependent anomaly is not an absolute state; a correlation alone cannot establish forcing attribution. Choose a geographic domain or explicit accounting boundary before writing the governing relationship. Record the averaging period and the geographical support used in comparisons.

The capstone assesses the fictional station network twice: first using a single uninterrupted raw series and then applying a documented break correction. Report the difference in trend along with model diagnostics, neighbor consistency and the scientific assumption behind each correction.

### What success looks like

A strong unit report reconstructs a physical chain from forcing to response while maintaining the distinction between an observation, a calculation, a model hypothesis and a decision. Include a figure that cannot be understood without axis units, a written alternative explanation and a comparison with a second type of evidence. Deliver a transparent station-quality report before offering a trend estimate.


## Lesson 1.1 — Climate versus weather and the choice of normal

### The physical question

Climate describes statistical distributions of weather across specified space and time. A multi-decade reference is needed to compare like conditions; using a different calendar season or station location can manufacture an apparent anomaly. The standard 30-year normals often used in operational climatology are practical reference conventions rather than immutable physical states. A distribution includes frequency and persistence of extremes, not only a monthly average. For the synthetic case, distinguish measured state, forcing, feedback, trend and any fitted relationship. An observed long-term change must be distinguished from sampling artifacts, internal variability and reference-period effects. Record the spatial scale, instrument history and averaging interval.


### From fundamental laws to an operational approximation

Begin by diagramming **raw weather observations to area-weighted climate indicator** and labeling **long-term distribution and observation provenance**. Choose a defensible statistical estimator, physical balance or mass-budget relationship appropriate to this topic. Distinguish the underlying process from the approximations in a fitted model, observational indicator or toy equation. Check dimensions and direction conventions before calculating; climate fields may be spatially varying even when one chart appears constant.


### What observations could distinguish mechanisms?

Compare two 30-year baselines and a recent five-year segment. Express anomalies relative to each baseline without changing the original thermometer values. Identify the observation time, position, calibration information and observational resolution. Contrast **station quality-controlled time series**, **independent neighboring climate observations** and **baseline sensitivity analysis**. A strong analysis identifies at least one independent variable, region or time interval where competing explanations make different predictions. In particular, assess an undocumented instrument relocation; never use the same evidence both to tune a hypothesis and to claim its independent confirmation.


### Worked numerical case — Temperature anomaly

**Fictional data:** A fictional site reports annual mean 18.6°C and matching climate normal 17.9°C.

**Calculation:** `18.6-17.9`. The numerical result is **0.7 °C anomaly**. Explicitly verify its units and interpretation; the number is a conditional result from invented inputs, not a documented observation. **Sensitivity:** perturb the dominant uncertain input by 10% and report what changes. This annual observation cannot prove a long-term trend. Explain which excluded process might invalidate the simplified estimate.


### Limits, confounding and counterfactual reasoning

Changing the reference period shifts the reported anomaly but need not change its time derivative or the physical warming itself. Contrast an alternative mechanism and state an observation that could discriminate between them. A more complex fitted curve is not necessarily a better causal explanation. Record station metadata, climate regime and measurement support before transferring a conclusion to a new situation.


### Practical study investigation

Write the baseline dates on each figure; prove algebraically how rebaselining changes an anomaly. Use `datasets/unit-01-synthetic.csv` for reproducible practice: plot the yearly variable and a five-year average while stating what the smoothing removes; annotate potential instrument error and a rival hypothesis. Reserve some observations for an independent check. The synthetic values are not validated natural observations, and apparent agreement with an illustrative model is not climate-data verification.


### Conceptual checks and problem set

1. Draw the physical process underlying **Climate versus weather and the choice of normal**, then label the state variables, external forcing, feedbacks and observational boundary. Which label is least well supported?
2. Reproduce the worked example with all unit conversions visible. Change one assumed value by 10%; report the new answer and interpret whether its sign or scale is plausible.
3. Explain how **changing the reference period shifts the reported anomaly but need not change its time derivative or the physical warming itself.** Give one additional observable that would distinguish this issue from the core mechanism.
4. Translate the case into an observational protocol: station placement, sample frequency, calibration information, data exclusion rules and one independent validation source.
5. Identify a failure mode for the proposed task: **Write the baseline dates on each figure; prove algebraically how rebaselining changes an anomaly.** Explain how biased sampling, omitted uncertainty or changes in the measurement system could produce a misleading conclusion.

**Answer expectations:** A competent response states the physical assumption, uses correctly dimensioned quantities, provides an interpretation in the context of the mechanism, reports an alternative explanation, and explicitly distinguishes fictional numerical inputs from observed climatological evidence. Answers that assert an exact future climate outcome from these toy equations require independent validation.


## Lesson 1.2 — Station siting, homogenization and metadata

### The physical question

Thermometer exposure, observing hour, vegetation and instrument replacement can create discontinuities unrelated to climate. Homogenization detects non-climatic breaks using station metadata and neighboring stations, but cannot turn a sparse network into a spatially complete truth. A reference station may itself contain a bias. Missing observations are not always random. For the synthetic case, distinguish measured state, forcing, feedback, trend and any fitted relationship. An observed long-term change must be distinguished from sampling artifacts, internal variability and reference-period effects. Record the spatial scale, instrument history and averaging interval.


### From fundamental laws to an operational approximation

Begin by diagramming **raw weather observations to area-weighted climate indicator** and labeling **long-term distribution and observation provenance**. Choose a defensible statistical estimator, physical balance or mass-budget relationship appropriate to this topic. Distinguish the underlying process from the approximations in a fitted model, observational indicator or toy equation. Check dimensions and direction conventions before calculating; climate fields may be spatially varying even when one chart appears constant.


### What observations could distinguish mechanisms?

Inspect paired neighbor differences before and after an imagined move from a roof to a ventilated field shelter. Use a blinded period to assess a correction. Identify the observation time, position, calibration information and observational resolution. Contrast **station quality-controlled time series**, **independent neighboring climate observations** and **baseline sensitivity analysis**. A strong analysis identifies at least one independent variable, region or time interval where competing explanations make different predictions. In particular, assess heterogeneous geographic coverage; never use the same evidence both to tune a hypothesis and to claim its independent confirmation.


### Worked numerical case — Thermometer break adjustment

**Fictional data:** A station series has a 0.42°C artificial warm offset after relocation; remove it from an observed 21.15°C.

**Calculation:** `21.15-0.42`. The numerical result is **20.73 °C corrected**. Explicitly verify its units and interpretation; the number is a conditional result from invented inputs, not a documented observation. **Sensitivity:** perturb the dominant uncertain input by 10% and report what changes. Document why the estimated shift is non-climatic. Explain which excluded process might invalidate the simplified estimate.


### Limits, confounding and counterfactual reasoning

An apparently abrupt jump may be regional weather if several independent neighbors show the same anomaly. Contrast an alternative mechanism and state an observation that could discriminate between them. A more complex fitted curve is not necessarily a better causal explanation. Record station metadata, climate regime and measurement support before transferring a conclusion to a new situation.


### Practical study investigation

Design an audit trail preserving raw measurements, adjustments and the reason for every exclusion. Use `datasets/unit-01-synthetic.csv` for reproducible practice: plot the yearly variable and a five-year average while stating what the smoothing removes; annotate potential instrument error and a rival hypothesis. Reserve some observations for an independent check. The synthetic values are not validated natural observations, and apparent agreement with an illustrative model is not climate-data verification.


### Conceptual checks and problem set

1. Draw the physical process underlying **Station siting, homogenization and metadata**, then label the state variables, external forcing, feedbacks and observational boundary. Which label is least well supported?
2. Reproduce the worked example with all unit conversions visible. Change one assumed value by 10%; report the new answer and interpret whether its sign or scale is plausible.
3. Explain how **an apparently abrupt jump may be regional weather if several independent neighbors show the same anomaly.** Give one additional observable that would distinguish this issue from the core mechanism.
4. Translate the case into an observational protocol: station placement, sample frequency, calibration information, data exclusion rules and one independent validation source.
5. Identify a failure mode for the proposed task: **Design an audit trail preserving raw measurements, adjustments and the reason for every exclusion.** Explain how biased sampling, omitted uncertainty or changes in the measurement system could produce a misleading conclusion.

**Answer expectations:** A competent response states the physical assumption, uses correctly dimensioned quantities, provides an interpretation in the context of the mechanism, reports an alternative explanation, and explicitly distinguishes fictional numerical inputs from observed climatological evidence. Answers that assert an exact future climate outcome from these toy equations require independent validation.


## Lesson 1.3 — Spatial sampling and area-weighted means

### The physical question

Global mean surface temperature combines unequal land and marine observations rather than simply averaging station readings. Equal-angle latitude-longitude cells cover different physical areas, so cosine-latitude weighting or equal-area grids matter. Spatial infilling, sea-surface sampling changes and data coverage contribute uncertainty. Global averages cannot describe local exposure. For the synthetic case, distinguish measured state, forcing, feedback, trend and any fitted relationship. An observed long-term change must be distinguished from sampling artifacts, internal variability and reference-period effects. Record the spatial scale, instrument history and averaging interval.


### From fundamental laws to an operational approximation

Begin by diagramming **raw weather observations to area-weighted climate indicator** and labeling **long-term distribution and observation provenance**. Choose a defensible statistical estimator, physical balance or mass-budget relationship appropriate to this topic. Distinguish the underlying process from the approximations in a fitted model, observational indicator or toy equation. Check dimensions and direction conventions before calculating; climate fields may be spatially varying even when one chart appears constant.


### What observations could distinguish mechanisms?

Compare a two-band area-weighted mean with an unweighted station mean, then introduce a missing high-latitude cell. Identify the observation time, position, calibration information and observational resolution. Contrast **station quality-controlled time series**, **independent neighboring climate observations** and **baseline sensitivity analysis**. A strong analysis identifies at least one independent variable, region or time interval where competing explanations make different predictions. In particular, assess a possible common forcing; never use the same evidence both to tune a hypothesis and to claim its independent confirmation.


### Worked numerical case — Latitude-weighted mean

**Fictional data:** Two equal-longitude grid cells at 0° and 60° have anomalies 1.2°C and 2.0°C.

**Calculation:** `(1.2+2*math.cos(math.pi/3))/(1+math.cos(math.pi/3))`. The numerical result is **1.467 °C**. Explicitly verify its units and interpretation; the number is a conditional result from invented inputs, not a documented observation. **Sensitivity:** perturb the dominant uncertain input by 10% and report what changes. This toy two-cell result is not a global estimate. Explain which excluded process might invalidate the simplified estimate.


### Limits, confounding and counterfactual reasoning

Weighting does not fix a sampling network whose sites systematically omit remote regions or seasons. Contrast an alternative mechanism and state an observation that could discriminate between them. A more complex fitted curve is not necessarily a better causal explanation. Record station metadata, climate regime and measurement support before transferring a conclusion to a new situation.


### Practical study investigation

Compute an aggregate three ways and explain the measurement operator each estimator implies. Use `datasets/unit-01-synthetic.csv` for reproducible practice: plot the yearly variable and a five-year average while stating what the smoothing removes; annotate potential instrument error and a rival hypothesis. Reserve some observations for an independent check. The synthetic values are not validated natural observations, and apparent agreement with an illustrative model is not climate-data verification.


### Conceptual checks and problem set

1. Draw the physical process underlying **Spatial sampling and area-weighted means**, then label the state variables, external forcing, feedbacks and observational boundary. Which label is least well supported?
2. Reproduce the worked example with all unit conversions visible. Change one assumed value by 10%; report the new answer and interpret whether its sign or scale is plausible.
3. Explain how **weighting does not fix a sampling network whose sites systematically omit remote regions or seasons.** Give one additional observable that would distinguish this issue from the core mechanism.
4. Translate the case into an observational protocol: station placement, sample frequency, calibration information, data exclusion rules and one independent validation source.
5. Identify a failure mode for the proposed task: **Compute an aggregate three ways and explain the measurement operator each estimator implies.** Explain how biased sampling, omitted uncertainty or changes in the measurement system could produce a misleading conclusion.

**Answer expectations:** A competent response states the physical assumption, uses correctly dimensioned quantities, provides an interpretation in the context of the mechanism, reports an alternative explanation, and explicitly distinguishes fictional numerical inputs from observed climatological evidence. Answers that assert an exact future climate outcome from these toy equations require independent validation.


## Lesson 1.4 — Trend fitting, autocorrelation and significance

### The physical question

A trend is an estimate conditional on the observation period, regression specification and error model. Year-to-year fluctuations often have serial correlation, so ordinary independent-error uncertainty intervals can be too narrow. Outliers may be informative extremes or recording faults. Statistical significance cannot substitute for effect size or physical attribution. For the synthetic case, distinguish measured state, forcing, feedback, trend and any fitted relationship. An observed long-term change must be distinguished from sampling artifacts, internal variability and reference-period effects. Record the spatial scale, instrument history and averaging interval.


### From fundamental laws to an operational approximation

Begin by diagramming **raw weather observations to area-weighted climate indicator** and labeling **long-term distribution and observation provenance**. Choose a defensible statistical estimator, physical balance or mass-budget relationship appropriate to this topic. Distinguish the underlying process from the approximations in a fitted model, observational indicator or toy equation. Check dimensions and direction conventions before calculating; climate fields may be spatially varying even when one chart appears constant.


### What observations could distinguish mechanisms?

Fit an ordinary least-squares slope, then repeat with an AR(1)-aware model and compare uncertainty ranges. Identify the observation time, position, calibration information and observational resolution. Contrast **station quality-controlled time series**, **independent neighboring climate observations** and **baseline sensitivity analysis**. A strong analysis identifies at least one independent variable, region or time interval where competing explanations make different predictions. In particular, assess a distribution that is non-stationary; never use the same evidence both to tune a hypothesis and to claim its independent confirmation.


### Worked numerical case — Change per decade

**Fictional data:** An illustrative fitted temperature change is 0.54°C over 30 years.

**Calculation:** `0.54/30*10`. The numerical result is **0.18 °C/decade**. Explicitly verify its units and interpretation; the number is a conditional result from invented inputs, not a documented observation. **Sensitivity:** perturb the dominant uncertain input by 10% and report what changes. A slope estimate requires statistical uncertainty and endpoints. Explain which excluded process might invalidate the simplified estimate.


### Limits, confounding and counterfactual reasoning

Selecting start years after seeing the plot creates an implicit multiple-comparison problem. Contrast an alternative mechanism and state an observation that could discriminate between them. A more complex fitted curve is not necessarily a better causal explanation. Record station metadata, climate regime and measurement support before transferring a conclusion to a new situation.


### Practical study investigation

Report slope in degrees Celsius per decade, confidence interval, time span and sensitivity to endpoints. Use `datasets/unit-01-synthetic.csv` for reproducible practice: plot the yearly variable and a five-year average while stating what the smoothing removes; annotate potential instrument error and a rival hypothesis. Reserve some observations for an independent check. The synthetic values are not validated natural observations, and apparent agreement with an illustrative model is not climate-data verification.


### Conceptual checks and problem set

1. Draw the physical process underlying **Trend fitting, autocorrelation and significance**, then label the state variables, external forcing, feedbacks and observational boundary. Which label is least well supported?
2. Reproduce the worked example with all unit conversions visible. Change one assumed value by 10%; report the new answer and interpret whether its sign or scale is plausible.
3. Explain how **selecting start years after seeing the plot creates an implicit multiple-comparison problem.** Give one additional observable that would distinguish this issue from the core mechanism.
4. Translate the case into an observational protocol: station placement, sample frequency, calibration information, data exclusion rules and one independent validation source.
5. Identify a failure mode for the proposed task: **Report slope in degrees Celsius per decade, confidence interval, time span and sensitivity to endpoints.** Explain how biased sampling, omitted uncertainty or changes in the measurement system could produce a misleading conclusion.

**Answer expectations:** A competent response states the physical assumption, uses correctly dimensioned quantities, provides an interpretation in the context of the mechanism, reports an alternative explanation, and explicitly distinguishes fictional numerical inputs from observed climatological evidence. Answers that assert an exact future climate outcome from these toy equations require independent validation.


## Lesson 1.5 — Detection, attribution and multiple lines of evidence

### The physical question

Detection establishes that an observed change is distinguishable from expected variability; attribution evaluates contributions from specified causes. Patterns across surface, ocean, stratosphere and seasonal cycles strengthen causal inference. Mechanistic model comparison, external forcings and independent observations must be combined. An increasing temperature by itself does not quantify an individual forcing. For the synthetic case, distinguish measured state, forcing, feedback, trend and any fitted relationship. An observed long-term change must be distinguished from sampling artifacts, internal variability and reference-period effects. Record the spatial scale, instrument history and averaging interval.


### From fundamental laws to an operational approximation

Begin by diagramming **raw weather observations to area-weighted climate indicator** and labeling **long-term distribution and observation provenance**. Choose a defensible statistical estimator, physical balance or mass-budget relationship appropriate to this topic. Distinguish the underlying process from the approximations in a fitted model, observational indicator or toy equation. Check dimensions and direction conventions before calculating; climate fields may be spatially varying even when one chart appears constant.


### What observations could distinguish mechanisms?

Contrast a natural-only forcing simulation with one including anthropogenic drivers using the same observation interval and calibration rules. Identify the observation time, position, calibration information and observational resolution. Contrast **station quality-controlled time series**, **independent neighboring climate observations** and **baseline sensitivity analysis**. A strong analysis identifies at least one independent variable, region or time interval where competing explanations make different predictions. In particular, assess an undocumented instrument relocation; never use the same evidence both to tune a hypothesis and to claim its independent confirmation.


### Worked numerical case — Residual difference between model fingerprints

**Fictional data:** A synthetic observation has anomaly 1.15°C; natural-only prediction is 0.25°C.

**Calculation:** `1.15-0.25`. The numerical result is **0.9 °C discrepancy**. Explicitly verify its units and interpretation; the number is a conditional result from invented inputs, not a documented observation. **Sensitivity:** perturb the dominant uncertain input by 10% and report what changes. Residual magnitude alone is not a full formal attribution study. Explain which excluded process might invalidate the simplified estimate.


### Limits, confounding and counterfactual reasoning

Shared model structural assumptions can make nominally independent runs less independent than they appear. Contrast an alternative mechanism and state an observation that could discriminate between them. A more complex fitted curve is not necessarily a better causal explanation. Record station metadata, climate regime and measurement support before transferring a conclusion to a new situation.


### Practical study investigation

Write a causal graph distinguishing emissions, radiative forcing, temperature, ocean heat and confounders. Use `datasets/unit-01-synthetic.csv` for reproducible practice: plot the yearly variable and a five-year average while stating what the smoothing removes; annotate potential instrument error and a rival hypothesis. Reserve some observations for an independent check. The synthetic values are not validated natural observations, and apparent agreement with an illustrative model is not climate-data verification.


### Conceptual checks and problem set

1. Draw the physical process underlying **Detection, attribution and multiple lines of evidence**, then label the state variables, external forcing, feedbacks and observational boundary. Which label is least well supported?
2. Reproduce the worked example with all unit conversions visible. Change one assumed value by 10%; report the new answer and interpret whether its sign or scale is plausible.
3. Explain how **shared model structural assumptions can make nominally independent runs less independent than they appear.** Give one additional observable that would distinguish this issue from the core mechanism.
4. Translate the case into an observational protocol: station placement, sample frequency, calibration information, data exclusion rules and one independent validation source.
5. Identify a failure mode for the proposed task: **Write a causal graph distinguishing emissions, radiative forcing, temperature, ocean heat and confounders.** Explain how biased sampling, omitted uncertainty or changes in the measurement system could produce a misleading conclusion.

**Answer expectations:** A competent response states the physical assumption, uses correctly dimensioned quantities, provides an interpretation in the context of the mechanism, reports an alternative explanation, and explicitly distinguishes fictional numerical inputs from observed climatological evidence. Answers that assert an exact future climate outcome from these toy equations require independent validation.


## Unit 1 capstone — A reproducible climate-science argument

Start from the research question **How can a climate trend be distinguished from weather noise, instrument shifts and a changing reference period?**. Create an evidence map that distinguishes the three sources **station quality-controlled time series**, **independent neighboring climate observations** and **baseline sensitivity analysis**. The first source should establish the main physical state, the second should show whether the proposed forcing was present, and the third should offer a genuinely independent check. For the synthetic scenario, state a primary hypothesis and an alternative that differs in mechanism rather than merely in parameter size. Specify what both would predict for the same geographic area under different observing or forcing conditions. In your technical report, use no unexplained uncertainty bars; distinguish calibration limits, observation support, model approximation, initialization errors, and uncertainty about the process itself.

**Data and reproducibility task:** Read the 30 synthetic records for this unit. Interpret the annual year column as a time axis, calculate a decadal mean and robust spread, and repeat the trend after withholding every fifth year. If the trend changes materially, explain whether the underlying signal might be under-sampled. Prepare a plain-language summary of what the dataset can and cannot support. Supply enough detail that another student can reproduce every calculation without contacting the author. Deliver a transparent station-quality report before offering a trend estimate.

**Critical discussion:** Suppose an institution must make a decision from the available analysis. Identify the evidence that is missing, the consequence of a false alarm versus a missed event, and the observation that would most efficiently reduce consequential uncertainty. Provide a direct recommendation only when the dataset and problem definition warrant one. Never treat synthetic climatological examples as an operational alert or regulatory threshold.

## Key takeaways for Unit 1

- The subject is an coupled climate system, not just an isolated plotted correlation; a defensible explanation must respect fundamental balances.
- The measurement domain, spatial scale, averaging interval and uncertainty control what can be inferred.
- The worked formulas expose sensitivity and limiting assumptions, not an automatic prediction for an unobserved site.
- A scientifically meaningful alternative hypothesis requires an observation that could falsify it.
- Operational warnings require responsible climatological services and independently validated evidence.
