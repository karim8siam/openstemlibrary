# Unit 2 — Energy balance and physical climate drivers
## The central climate-science investigation

**Question:** Which energy transfers and radiative processes determine equilibrium and transient climate responses?

**Case setting:** A hypothetical satellite and ocean-flux campaign detects a small persistent planetary energy imbalance. All locations and observations in the following investigation are synthetic. The purpose is to learn which inference would survive contact with independent measurements, rather than to produce a plausible-sounding story from an incomplete climate map.

Earth receives solar radiation and emits thermal infrared energy. Averaging over a rotating sphere changes the solar geometry; treating a planetary mean as a tropical noon flux creates a major budget error. Absorption and reflection redistribute solar energy; infrared opacity and temperature structure determine outgoing emission. These mechanisms support a global energy balance while leaving cloud distributions and regional transport complicated.

A radiative forcing is not the same as a feedback, and an instantaneous flux is not the same as accumulated heat content. Ocean temperature response is delayed because most heat capacity resides in water. The same change in net flux can be associated with different warming histories depending on how heat is exchanged with deeper layers. Any illustrative equilibrium calculation must state whether it neglects ocean uptake and nonlinear feedbacks.

### Working boundaries and research assumptions

The effective observational transect for this unit runs from **incoming solar flux to stored ocean heat**. Different forms of evidence support different kinds of inference: top-of-atmosphere satellite flux constrains one aspect, surface/ocean heat storage estimate another, and mechanistic radiative calculation a third. These are not interchangeable. A flux through a boundary differs from stored heat or carbon; a baseline-dependent anomaly is not an absolute state; a correlation alone cannot establish forcing attribution. Choose a geographic domain or explicit accounting boundary before writing the governing relationship. Record the averaging period and the geographical support used in comparisons.

In the unit project, test a one-box energy budget before adding an explicit ocean heat uptake term; compare the fit with independently generated temperature and ocean heat-content records. The result is a didactic scaling demonstration, not a projection.

### What success looks like

A strong unit report reconstructs a physical chain from forcing to response while maintaining the distinction between an observation, a calculation, a model hypothesis and a decision. Include a figure that cannot be understood without axis units, a written alternative explanation and a comparison with a second type of evidence. Close a budget with explicit uncertainty and distinguish forcing from feedback.


## Lesson 2.1 — Incoming sunlight, albedo and planetary budgets

### The physical question

Incoming top-of-atmosphere solar power is spread over a sphere, yielding an area mean near one-quarter of the solar constant. Reflection by clouds, aerosols and surfaces reduces absorbed solar flux. A planetary budget compares absorbed shortwave to emitted thermal radiation. Local and global energy budgets differ because horizontal transports redistribute energy. For the synthetic case, distinguish measured state, forcing, feedback, trend and any fitted relationship. An observed long-term change must be distinguished from sampling artifacts, internal variability and reference-period effects. Record the spatial scale, instrument history and averaging interval.


### From fundamental laws to an operational approximation

Begin by diagramming **incoming solar flux to stored ocean heat** and labeling **planetary radiative fluxes and ocean heat uptake**. Choose a defensible statistical estimator, physical balance or mass-budget relationship appropriate to this topic. Distinguish the underlying process from the approximations in a fitted model, observational indicator or toy equation. Check dimensions and direction conventions before calculating; climate fields may be spatially varying even when one chart appears constant.


### What observations could distinguish mechanisms?

Convert a solar constant to an idealized global mean, then compare reflected and absorbed energy under two fictional albedos. Identify the observation time, position, calibration information and observational resolution. Contrast **top-of-atmosphere satellite flux**, **surface/ocean heat storage estimate** and **mechanistic radiative calculation**. A strong analysis identifies at least one independent variable, region or time interval where competing explanations make different predictions. In particular, assess changing reference periods; never use the same evidence both to tune a hypothesis and to claim its independent confirmation.


### Worked numerical case — Global mean insolation

**Fictional data:** A reference incoming solar flux of 1360 W/m² averaged geometrically over Earth.

**Calculation:** `1360/4`. The numerical result is **340 W/m²**. Explicitly verify its units and interpretation; the number is a conditional result from invented inputs, not a documented observation. **Sensitivity:** perturb the dominant uncertain input by 10% and report what changes. The actual flux varies; this shows spherical geometry. Explain which excluded process might invalidate the simplified estimate.


### Limits, confounding and counterfactual reasoning

A fixed broadband albedo omits wavelength dependence and cloud adjustments. Contrast an alternative mechanism and state an observation that could discriminate between them. A more complex fitted curve is not necessarily a better causal explanation. Record station metadata, climate regime and measurement support before transferring a conclusion to a new situation.


### Practical study investigation

Draw a full top-of-atmosphere energy-flow diagram with flux signs and units. Use `datasets/unit-02-synthetic.csv` for reproducible practice: plot the yearly variable and a five-year average while stating what the smoothing removes; annotate potential instrument error and a rival hypothesis. Reserve some observations for an independent check. The synthetic values are not validated natural observations, and apparent agreement with an illustrative model is not climate-data verification.


### Conceptual checks and problem set

1. Draw the physical process underlying **Incoming sunlight, albedo and planetary budgets**, then label the state variables, external forcing, feedbacks and observational boundary. Which label is least well supported?
2. Reproduce the worked example with all unit conversions visible. Change one assumed value by 10%; report the new answer and interpret whether its sign or scale is plausible.
3. Explain how **a fixed broadband albedo omits wavelength dependence and cloud adjustments.** Give one additional observable that would distinguish this issue from the core mechanism.
4. Translate the case into an observational protocol: station placement, sample frequency, calibration information, data exclusion rules and one independent validation source.
5. Identify a failure mode for the proposed task: **Draw a full top-of-atmosphere energy-flow diagram with flux signs and units.** Explain how biased sampling, omitted uncertainty or changes in the measurement system could produce a misleading conclusion.

**Answer expectations:** A competent response states the physical assumption, uses correctly dimensioned quantities, provides an interpretation in the context of the mechanism, reports an alternative explanation, and explicitly distinguishes fictional numerical inputs from observed climatological evidence. Answers that assert an exact future climate outcome from these toy equations require independent validation.


## Lesson 2.2 — Infrared absorption, emission and greenhouse effect

### The physical question

Greenhouse gases absorb and emit infrared radiation in spectral bands, changing the height and temperature distribution of energy emission to space. The natural greenhouse effect is not a solid lid and does not require convection to stop. Surface warming changes outgoing emission and can restore balance. Band saturation arguments cannot ignore pressure broadening and vertical atmospheric structure. For the synthetic case, distinguish measured state, forcing, feedback, trend and any fitted relationship. An observed long-term change must be distinguished from sampling artifacts, internal variability and reference-period effects. Record the spatial scale, instrument history and averaging interval.


### From fundamental laws to an operational approximation

Begin by diagramming **incoming solar flux to stored ocean heat** and labeling **planetary radiative fluxes and ocean heat uptake**. Choose a defensible statistical estimator, physical balance or mass-budget relationship appropriate to this topic. Distinguish the underlying process from the approximations in a fitted model, observational indicator or toy equation. Check dimensions and direction conventions before calculating; climate fields may be spatially varying even when one chart appears constant.


### What observations could distinguish mechanisms?

Compare a thermal spectrum across absorbing and window bands rather than relying only on a total infrared number. Identify the observation time, position, calibration information and observational resolution. Contrast **top-of-atmosphere satellite flux**, **surface/ocean heat storage estimate** and **mechanistic radiative calculation**. A strong analysis identifies at least one independent variable, region or time interval where competing explanations make different predictions. In particular, assess time autocorrelation; never use the same evidence both to tune a hypothesis and to claim its independent confirmation.


### Worked numerical case — Stefan–Boltzmann emission

**Fictional data:** Ideal blackbody at 255 K, Stefan–Boltzmann constant 5.670374419×10⁻⁸.

**Calculation:** `5.670374419e-8*255**4`. The numerical result is **239.8 W/m²**. Explicitly verify its units and interpretation; the number is a conditional result from invented inputs, not a documented observation. **Sensitivity:** perturb the dominant uncertain input by 10% and report what changes. A blackbody is not a vertically resolved atmospheric spectrum. Explain which excluded process might invalidate the simplified estimate.


### Limits, confounding and counterfactual reasoning

A simple blackbody temperature cannot represent the full vertical radiative transfer problem. Contrast an alternative mechanism and state an observation that could discriminate between them. A more complex fitted curve is not necessarily a better causal explanation. Record station metadata, climate regime and measurement support before transferring a conclusion to a new situation.


### Practical study investigation

Write a two-layer energy-balance model and list the physical processes it excludes. Use `datasets/unit-02-synthetic.csv` for reproducible practice: plot the yearly variable and a five-year average while stating what the smoothing removes; annotate potential instrument error and a rival hypothesis. Reserve some observations for an independent check. The synthetic values are not validated natural observations, and apparent agreement with an illustrative model is not climate-data verification.


### Conceptual checks and problem set

1. Draw the physical process underlying **Infrared absorption, emission and greenhouse effect**, then label the state variables, external forcing, feedbacks and observational boundary. Which label is least well supported?
2. Reproduce the worked example with all unit conversions visible. Change one assumed value by 10%; report the new answer and interpret whether its sign or scale is plausible.
3. Explain how **a simple blackbody temperature cannot represent the full vertical radiative transfer problem.** Give one additional observable that would distinguish this issue from the core mechanism.
4. Translate the case into an observational protocol: station placement, sample frequency, calibration information, data exclusion rules and one independent validation source.
5. Identify a failure mode for the proposed task: **Write a two-layer energy-balance model and list the physical processes it excludes.** Explain how biased sampling, omitted uncertainty or changes in the measurement system could produce a misleading conclusion.

**Answer expectations:** A competent response states the physical assumption, uses correctly dimensioned quantities, provides an interpretation in the context of the mechanism, reports an alternative explanation, and explicitly distinguishes fictional numerical inputs from observed climatological evidence. Answers that assert an exact future climate outcome from these toy equations require independent validation.


## Lesson 2.3 — Radiative forcing and effective forcing

### The physical question

Radiative forcing is a perturbation to the energy budget defined under specified atmospheric adjustment conventions. Effective radiative forcing allows specified rapid adjustments, making forcing agents more comparable than instantaneous flux changes alone. Long-lived gases, aerosols, ozone, land-use and solar changes have different spatial patterns and lifetimes. Individual forcings are not directly interchangeable with observed temperature changes. For the synthetic case, distinguish measured state, forcing, feedback, trend and any fitted relationship. An observed long-term change must be distinguished from sampling artifacts, internal variability and reference-period effects. Record the spatial scale, instrument history and averaging interval.


### From fundamental laws to an operational approximation

Begin by diagramming **incoming solar flux to stored ocean heat** and labeling **planetary radiative fluxes and ocean heat uptake**. Choose a defensible statistical estimator, physical balance or mass-budget relationship appropriate to this topic. Distinguish the underlying process from the approximations in a fitted model, observational indicator or toy equation. Check dimensions and direction conventions before calculating; climate fields may be spatially varying even when one chart appears constant.


### What observations could distinguish mechanisms?

Classify a synthetic forcing dataset by agent, uncertainty range and spatial distribution; separate inventory inputs from diagnostic radiative flux. Identify the observation time, position, calibration information and observational resolution. Contrast **top-of-atmosphere satellite flux**, **surface/ocean heat storage estimate** and **mechanistic radiative calculation**. A strong analysis identifies at least one independent variable, region or time interval where competing explanations make different predictions. In particular, assess a shift in observational method; never use the same evidence both to tune a hypothesis and to claim its independent confirmation.


### Worked numerical case — Linear temperature response

**Fictional data:** A toy forcing of 2.5 W/m² is balanced by feedback parameter 1.25 W/m²/K.

**Calculation:** `2.5/1.25`. The numerical result is **2 K**. Explicitly verify its units and interpretation; the number is a conditional result from invented inputs, not a documented observation. **Sensitivity:** perturb the dominant uncertain input by 10% and report what changes. This is equilibrium in a linear toy model, not an observed future warming. Explain which excluded process might invalidate the simplified estimate.


### Limits, confounding and counterfactual reasoning

Adding poorly characterized agent estimates as exact numbers hides covariance and adjustment uncertainty. Contrast an alternative mechanism and state an observation that could discriminate between them. A more complex fitted curve is not necessarily a better causal explanation. Record station metadata, climate regime and measurement support before transferring a conclusion to a new situation.


### Practical study investigation

Estimate the temperature response in a toy linear model and compare it with a nonlinear budget. Use `datasets/unit-02-synthetic.csv` for reproducible practice: plot the yearly variable and a five-year average while stating what the smoothing removes; annotate potential instrument error and a rival hypothesis. Reserve some observations for an independent check. The synthetic values are not validated natural observations, and apparent agreement with an illustrative model is not climate-data verification.


### Conceptual checks and problem set

1. Draw the physical process underlying **Radiative forcing and effective forcing**, then label the state variables, external forcing, feedbacks and observational boundary. Which label is least well supported?
2. Reproduce the worked example with all unit conversions visible. Change one assumed value by 10%; report the new answer and interpret whether its sign or scale is plausible.
3. Explain how **adding poorly characterized agent estimates as exact numbers hides covariance and adjustment uncertainty.** Give one additional observable that would distinguish this issue from the core mechanism.
4. Translate the case into an observational protocol: station placement, sample frequency, calibration information, data exclusion rules and one independent validation source.
5. Identify a failure mode for the proposed task: **Estimate the temperature response in a toy linear model and compare it with a nonlinear budget.** Explain how biased sampling, omitted uncertainty or changes in the measurement system could produce a misleading conclusion.

**Answer expectations:** A competent response states the physical assumption, uses correctly dimensioned quantities, provides an interpretation in the context of the mechanism, reports an alternative explanation, and explicitly distinguishes fictional numerical inputs from observed climatological evidence. Answers that assert an exact future climate outcome from these toy equations require independent validation.


## Lesson 2.4 — Feedbacks, water vapor and clouds

### The physical question

A climate feedback changes net radiation in response to climate state. Water-vapor, lapse-rate, surface-albedo and cloud responses act through distinct processes and can differ by region or time scale. Positive feedback amplifies an initial perturbation but does not imply perpetual runaway. Cloud feedback is especially sensitive to representation of microphysics and circulation. For the synthetic case, distinguish measured state, forcing, feedback, trend and any fitted relationship. An observed long-term change must be distinguished from sampling artifacts, internal variability and reference-period effects. Record the spatial scale, instrument history and averaging interval.


### From fundamental laws to an operational approximation

Begin by diagramming **incoming solar flux to stored ocean heat** and labeling **planetary radiative fluxes and ocean heat uptake**. Choose a defensible statistical estimator, physical balance or mass-budget relationship appropriate to this topic. Distinguish the underlying process from the approximations in a fitted model, observational indicator or toy equation. Check dimensions and direction conventions before calculating; climate fields may be spatially varying even when one chart appears constant.


### What observations could distinguish mechanisms?

Compare feedback parameters diagnosed over short and long intervals, including an independent tropical-cloud constraint. Identify the observation time, position, calibration information and observational resolution. Contrast **top-of-atmosphere satellite flux**, **surface/ocean heat storage estimate** and **mechanistic radiative calculation**. A strong analysis identifies at least one independent variable, region or time interval where competing explanations make different predictions. In particular, assess uncertainty hidden by reporting a single estimate; never use the same evidence both to tune a hypothesis and to claim its independent confirmation.


### Worked numerical case — Cloud radiative compensation

**Fictional data:** Illustrative shortwave cloud effect −42 and longwave effect +31 W/m².

**Calculation:** `-42+31`. The numerical result is **-11 W/m²**. Explicitly verify its units and interpretation; the number is a conditional result from invented inputs, not a documented observation. **Sensitivity:** perturb the dominant uncertain input by 10% and report what changes. Cloud effects are geographically and temporally variable. Explain which excluded process might invalidate the simplified estimate.


### Limits, confounding and counterfactual reasoning

Cloud shortwave and longwave effects can oppose one another; a single percentage cloud-cover change is inadequate. Contrast an alternative mechanism and state an observation that could discriminate between them. A more complex fitted curve is not necessarily a better causal explanation. Record station metadata, climate regime and measurement support before transferring a conclusion to a new situation.


### Practical study investigation

Construct a signed feedback diagram and explicitly mark unknown links. Use `datasets/unit-02-synthetic.csv` for reproducible practice: plot the yearly variable and a five-year average while stating what the smoothing removes; annotate potential instrument error and a rival hypothesis. Reserve some observations for an independent check. The synthetic values are not validated natural observations, and apparent agreement with an illustrative model is not climate-data verification.


### Conceptual checks and problem set

1. Draw the physical process underlying **Feedbacks, water vapor and clouds**, then label the state variables, external forcing, feedbacks and observational boundary. Which label is least well supported?
2. Reproduce the worked example with all unit conversions visible. Change one assumed value by 10%; report the new answer and interpret whether its sign or scale is plausible.
3. Explain how **cloud shortwave and longwave effects can oppose one another; a single percentage cloud-cover change is inadequate.** Give one additional observable that would distinguish this issue from the core mechanism.
4. Translate the case into an observational protocol: station placement, sample frequency, calibration information, data exclusion rules and one independent validation source.
5. Identify a failure mode for the proposed task: **Construct a signed feedback diagram and explicitly mark unknown links.** Explain how biased sampling, omitted uncertainty or changes in the measurement system could produce a misleading conclusion.

**Answer expectations:** A competent response states the physical assumption, uses correctly dimensioned quantities, provides an interpretation in the context of the mechanism, reports an alternative explanation, and explicitly distinguishes fictional numerical inputs from observed climatological evidence. Answers that assert an exact future climate outcome from these toy equations require independent validation.


## Lesson 2.5 — Heat uptake, response times and imbalance

### The physical question

A transient planetary energy imbalance can warm the ocean, land, ice and atmosphere. Ocean heat uptake dominates heat storage because of water mass and heat capacity, but mixed-layer and deeper-ocean response times differ. A model with a single response time can illustrate transient warming yet miss interbasin transport. Equilibrium response and warming at one future date are different quantities. For the synthetic case, distinguish measured state, forcing, feedback, trend and any fitted relationship. An observed long-term change must be distinguished from sampling artifacts, internal variability and reference-period effects. Record the spatial scale, instrument history and averaging interval.


### From fundamental laws to an operational approximation

Begin by diagramming **incoming solar flux to stored ocean heat** and labeling **planetary radiative fluxes and ocean heat uptake**. Choose a defensible statistical estimator, physical balance or mass-budget relationship appropriate to this topic. Distinguish the underlying process from the approximations in a fitted model, observational indicator or toy equation. Check dimensions and direction conventions before calculating; climate fields may be spatially varying even when one chart appears constant.


### What observations could distinguish mechanisms?

Use synthetic ocean heat-content and top-of-atmosphere records to compare an energy-uptake estimate with a temperature-based inference. Identify the observation time, position, calibration information and observational resolution. Contrast **top-of-atmosphere satellite flux**, **surface/ocean heat storage estimate** and **mechanistic radiative calculation**. A strong analysis identifies at least one independent variable, region or time interval where competing explanations make different predictions. In particular, assess changing reference periods; never use the same evidence both to tune a hypothesis and to claim its independent confirmation.


### Worked numerical case — Energy accumulation

**Fictional data:** Fixed 0.8 W/m² across 5.1×10¹⁴ m² for one 365-day year.

**Calculation:** `0.8*5.1e14*365*86400`. The numerical result is **1.287e+22 joules**. Explicitly verify its units and interpretation; the number is a conditional result from invented inputs, not a documented observation. **Sensitivity:** perturb the dominant uncertain input by 10% and report what changes. A constant imbalance across time and space is an approximation. Explain which excluded process might invalidate the simplified estimate.


### Limits, confounding and counterfactual reasoning

Heat-storage measurements and top-of-atmosphere observations have different coverage, calibration histories and uncertainty structures. Contrast an alternative mechanism and state an observation that could discriminate between them. A more complex fitted curve is not necessarily a better causal explanation. Record station metadata, climate regime and measurement support before transferring a conclusion to a new situation.


### Practical study investigation

Compute energy accumulation from a fixed imbalance and explain why the assumption eventually breaks down. Use `datasets/unit-02-synthetic.csv` for reproducible practice: plot the yearly variable and a five-year average while stating what the smoothing removes; annotate potential instrument error and a rival hypothesis. Reserve some observations for an independent check. The synthetic values are not validated natural observations, and apparent agreement with an illustrative model is not climate-data verification.


### Conceptual checks and problem set

1. Draw the physical process underlying **Heat uptake, response times and imbalance**, then label the state variables, external forcing, feedbacks and observational boundary. Which label is least well supported?
2. Reproduce the worked example with all unit conversions visible. Change one assumed value by 10%; report the new answer and interpret whether its sign or scale is plausible.
3. Explain how **heat-storage measurements and top-of-atmosphere observations have different coverage, calibration histories and uncertainty structures.** Give one additional observable that would distinguish this issue from the core mechanism.
4. Translate the case into an observational protocol: station placement, sample frequency, calibration information, data exclusion rules and one independent validation source.
5. Identify a failure mode for the proposed task: **Compute energy accumulation from a fixed imbalance and explain why the assumption eventually breaks down.** Explain how biased sampling, omitted uncertainty or changes in the measurement system could produce a misleading conclusion.

**Answer expectations:** A competent response states the physical assumption, uses correctly dimensioned quantities, provides an interpretation in the context of the mechanism, reports an alternative explanation, and explicitly distinguishes fictional numerical inputs from observed climatological evidence. Answers that assert an exact future climate outcome from these toy equations require independent validation.


## Unit 2 capstone — A reproducible climate-science argument

Start from the research question **Which energy transfers and radiative processes determine equilibrium and transient climate responses?**. Create an evidence map that distinguishes the three sources **top-of-atmosphere satellite flux**, **surface/ocean heat storage estimate** and **mechanistic radiative calculation**. The first source should establish the main physical state, the second should show whether the proposed forcing was present, and the third should offer a genuinely independent check. For the synthetic scenario, state a primary hypothesis and an alternative that differs in mechanism rather than merely in parameter size. Specify what both would predict for the same geographic area under different observing or forcing conditions. In your technical report, use no unexplained uncertainty bars; distinguish calibration limits, observation support, model approximation, initialization errors, and uncertainty about the process itself.

**Data and reproducibility task:** Read the 30 synthetic records for this unit. Interpret the annual year column as a time axis, calculate a decadal mean and robust spread, and repeat the trend after withholding every fifth year. If the trend changes materially, explain whether the underlying signal might be under-sampled. Prepare a plain-language summary of what the dataset can and cannot support. Supply enough detail that another student can reproduce every calculation without contacting the author. Close a budget with explicit uncertainty and distinguish forcing from feedback.

**Critical discussion:** Suppose an institution must make a decision from the available analysis. Identify the evidence that is missing, the consequence of a false alarm versus a missed event, and the observation that would most efficiently reduce consequential uncertainty. Provide a direct recommendation only when the dataset and problem definition warrant one. Never treat synthetic climatological examples as an operational alert or regulatory threshold.

## Key takeaways for Unit 2

- The subject is an coupled climate system, not just an isolated plotted correlation; a defensible explanation must respect fundamental balances.
- The measurement domain, spatial scale, averaging interval and uncertainty control what can be inferred.
- The worked formulas expose sensitivity and limiting assumptions, not an automatic prediction for an unobserved site.
- A scientifically meaningful alternative hypothesis requires an observation that could falsify it.
- Operational warnings require responsible climatological services and independently validated evidence.
