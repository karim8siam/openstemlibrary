# Unit 6 — Climate models, scenarios and uncertainty
## The central climate-science investigation

**Question:** How can climate models be evaluated and used responsibly to explore plausible futures?

**Case setting:** A teaching ensemble spans simple energy-balance models, regional gridded simulations and emission scenarios. All locations and observations in the following investigation are synthetic. The purpose is to learn which inference would survive contact with independent measurements, rather than to produce a plausible-sounding story from an incomplete climate map.

A climate model solves approximate conservation and transport equations on finite grids, using parameterizations for unresolved processes. Because the Earth system is coupled, biases in one component can influence other variables and regions. Verification therefore examines budgets, variability, historical response, extremes and observations not already used for tuning. Reproducing a global mean through compensating errors is not successful process validation.

Future scenario uncertainty differs from internal climate variability or structural model uncertainty. Model ensembles often share code, assumptions or parameterization choices, so the individual runs are not independent random samples from an objective probability distribution. A high-resolution regional product inherits assumptions from its global drivers and its bias correction. Responsible use retains the conditional nature of the emission pathway.

### Working boundaries and research assumptions

The effective observational transect for this unit runs from **scenario assumptions to regional model output**. Different forms of evidence support different kinds of inference: physical model diagnostics constrains one aspect, held-out instrumental record another, and scenario-conditional ensemble comparison a third. These are not interchangeable. A flux through a boundary differs from stored heat or carbon; a baseline-dependent anomaly is not an absolute state; a correlation alone cannot establish forcing attribution. Choose a geographic domain or explicit accounting boundary before writing the governing relationship. Record the averaging period and the geographical support used in comparisons.

The capstone evaluates a small synthetic ensemble against withheld historical values, ranks results on more than one diagnostic, and shows how different scenarios and model parameters produce distinct futures.

### What success looks like

A strong unit report reconstructs a physical chain from forcing to response while maintaining the distinction between an observation, a calculation, a model hypothesis and a decision. Include a figure that cannot be understood without axis units, a written alternative explanation and a comparison with a second type of evidence. Explain structural uncertainty, internal variability and scenario dependence separately.


## Lesson 6.1 — From equations to coupled Earth-system models

### The physical question

Climate models approximate fluid dynamics, thermodynamics, radiation and biogeochemical processes on finite grids. Parameterizations represent unresolved processes and may be tuned using selected observations. Model conservation budgets and numerics must be audited separately from visible pattern resemblance. Increasing spatial resolution does not remove model structural error. For the synthetic case, distinguish measured state, forcing, feedback, trend and any fitted relationship. An observed long-term change must be distinguished from sampling artifacts, internal variability and reference-period effects. Record the spatial scale, instrument history and averaging interval.


### From fundamental laws to an operational approximation

Begin by diagramming **scenario assumptions to regional model output** and labeling **model forcings, parameters and initial conditions**. Choose a defensible statistical estimator, physical balance or mass-budget relationship appropriate to this topic. Distinguish the underlying process from the approximations in a fitted model, observational indicator or toy equation. Check dimensions and direction conventions before calculating; climate fields may be spatially varying even when one chart appears constant.


### What observations could distinguish mechanisms?

Compare model global energy closure, regional rainfall pattern and out-of-sample seasonal variability against different observations. Identify the observation time, position, calibration information and observational resolution. Contrast **physical model diagnostics**, **held-out instrumental record** and **scenario-conditional ensemble comparison**. A strong analysis identifies at least one independent variable, region or time interval where competing explanations make different predictions. In particular, assess a shift in observational method; never use the same evidence both to tune a hypothesis and to claim its independent confirmation.


### Worked numerical case — Energy budget model drift

**Fictional data:** Toy climate simulation absorbs 241.3 W/m² and emits 240.6 W/m².

**Calculation:** `241.3-240.6`. The numerical result is **0.7 W/m²**. Explicitly verify its units and interpretation; the number is a conditional result from invented inputs, not a documented observation. **Sensitivity:** perturb the dominant uncertain input by 10% and report what changes. Residual can reflect an evolving state or numerical imbalance. Explain which excluded process might invalidate the simplified estimate.


### Limits, confounding and counterfactual reasoning

A model can reproduce a historical average for compensating wrong reasons; tuning data must not serve as independent verification. Contrast an alternative mechanism and state an observation that could discriminate between them. A more complex fitted curve is not necessarily a better causal explanation. Record station metadata, climate regime and measurement support before transferring a conclusion to a new situation.


### Practical study investigation

Draw a model component diagram with exchange fluxes and failure points. Use `datasets/unit-06-synthetic.csv` for reproducible practice: plot the yearly variable and a five-year average while stating what the smoothing removes; annotate potential instrument error and a rival hypothesis. Reserve some observations for an independent check. The synthetic values are not validated natural observations, and apparent agreement with an illustrative model is not climate-data verification.


### Conceptual checks and problem set

1. Draw the physical process underlying **From equations to coupled Earth-system models**, then label the state variables, external forcing, feedbacks and observational boundary. Which label is least well supported?
2. Reproduce the worked example with all unit conversions visible. Change one assumed value by 10%; report the new answer and interpret whether its sign or scale is plausible.
3. Explain how **a model can reproduce a historical average for compensating wrong reasons; tuning data must not serve as independent verification.** Give one additional observable that would distinguish this issue from the core mechanism.
4. Translate the case into an observational protocol: station placement, sample frequency, calibration information, data exclusion rules and one independent validation source.
5. Identify a failure mode for the proposed task: **Draw a model component diagram with exchange fluxes and failure points.** Explain how biased sampling, omitted uncertainty or changes in the measurement system could produce a misleading conclusion.

**Answer expectations:** A competent response states the physical assumption, uses correctly dimensioned quantities, provides an interpretation in the context of the mechanism, reports an alternative explanation, and explicitly distinguishes fictional numerical inputs from observed climatological evidence. Answers that assert an exact future climate outcome from these toy equations require independent validation.


## Lesson 6.2 — Scenario pathways versus predictions

### The physical question

An emissions pathway describes assumptions about future activity, technology and policy; model climate outcomes are conditional on these pathways. A scenario is not a probability forecast unless probabilities are explicitly justified. Physical climate uncertainty, socioeconomic uncertainty and natural variability should not be merged into one vague range. For the synthetic case, distinguish measured state, forcing, feedback, trend and any fitted relationship. An observed long-term change must be distinguished from sampling artifacts, internal variability and reference-period effects. Record the spatial scale, instrument history and averaging interval.


### From fundamental laws to an operational approximation

Begin by diagramming **scenario assumptions to regional model output** and labeling **model forcings, parameters and initial conditions**. Choose a defensible statistical estimator, physical balance or mass-budget relationship appropriate to this topic. Distinguish the underlying process from the approximations in a fitted model, observational indicator or toy equation. Check dimensions and direction conventions before calculating; climate fields may be spatially varying even when one chart appears constant.


### What observations could distinguish mechanisms?

Compare hypothetical emission pathways with fixed model sensitivity, then vary climate parameters independently. Identify the observation time, position, calibration information and observational resolution. Contrast **physical model diagnostics**, **held-out instrumental record** and **scenario-conditional ensemble comparison**. A strong analysis identifies at least one independent variable, region or time interval where competing explanations make different predictions. In particular, assess uncertainty hidden by reporting a single estimate; never use the same evidence both to tune a hypothesis and to claim its independent confirmation.


### Worked numerical case — Scenario emissions gap

**Fictional data:** Fictional 2050 pathways emit 20 and 12 Gt CO₂/year.

**Calculation:** `20-12`. The numerical result is **8 Gt CO₂/year**. Explicitly verify its units and interpretation; the number is a conditional result from invented inputs, not a documented observation. **Sensitivity:** perturb the dominant uncertain input by 10% and report what changes. Neither path is assigned a real-world probability. Explain which excluded process might invalidate the simplified estimate.


### Limits, confounding and counterfactual reasoning

A single scenario trace should not be described as what definitely will happen in a particular year. Contrast an alternative mechanism and state an observation that could discriminate between them. A more complex fitted curve is not necessarily a better causal explanation. Record station metadata, climate regime and measurement support before transferring a conclusion to a new situation.


### Practical study investigation

Write three conditional statements that retain both scenario and physical-model qualifications. Use `datasets/unit-06-synthetic.csv` for reproducible practice: plot the yearly variable and a five-year average while stating what the smoothing removes; annotate potential instrument error and a rival hypothesis. Reserve some observations for an independent check. The synthetic values are not validated natural observations, and apparent agreement with an illustrative model is not climate-data verification.


### Conceptual checks and problem set

1. Draw the physical process underlying **Scenario pathways versus predictions**, then label the state variables, external forcing, feedbacks and observational boundary. Which label is least well supported?
2. Reproduce the worked example with all unit conversions visible. Change one assumed value by 10%; report the new answer and interpret whether its sign or scale is plausible.
3. Explain how **a single scenario trace should not be described as what definitely will happen in a particular year.** Give one additional observable that would distinguish this issue from the core mechanism.
4. Translate the case into an observational protocol: station placement, sample frequency, calibration information, data exclusion rules and one independent validation source.
5. Identify a failure mode for the proposed task: **Write three conditional statements that retain both scenario and physical-model qualifications.** Explain how biased sampling, omitted uncertainty or changes in the measurement system could produce a misleading conclusion.

**Answer expectations:** A competent response states the physical assumption, uses correctly dimensioned quantities, provides an interpretation in the context of the mechanism, reports an alternative explanation, and explicitly distinguishes fictional numerical inputs from observed climatological evidence. Answers that assert an exact future climate outcome from these toy equations require independent validation.


## Lesson 6.3 — Climate sensitivity and transient response

### The physical question

Equilibrium climate sensitivity concerns eventual global warming following a sustained CO₂ doubling after ocean adjustment; transient climate response concerns warming in a defined gradually increasing CO₂ experiment. Feedbacks and ocean heat uptake make these quantities distinct. A one-box energy-balance model is instructive but cannot reproduce all spatial and temporal processes. For the synthetic case, distinguish measured state, forcing, feedback, trend and any fitted relationship. An observed long-term change must be distinguished from sampling artifacts, internal variability and reference-period effects. Record the spatial scale, instrument history and averaging interval.


### From fundamental laws to an operational approximation

Begin by diagramming **scenario assumptions to regional model output** and labeling **model forcings, parameters and initial conditions**. Choose a defensible statistical estimator, physical balance or mass-budget relationship appropriate to this topic. Distinguish the underlying process from the approximations in a fitted model, observational indicator or toy equation. Check dimensions and direction conventions before calculating; climate fields may be spatially varying even when one chart appears constant.


### What observations could distinguish mechanisms?

Simulate a constant forcing in a one-box model, then add an ocean uptake term and compare equilibration rates. Identify the observation time, position, calibration information and observational resolution. Contrast **physical model diagnostics**, **held-out instrumental record** and **scenario-conditional ensemble comparison**. A strong analysis identifies at least one independent variable, region or time interval where competing explanations make different predictions. In particular, assess changing reference periods; never use the same evidence both to tune a hypothesis and to claim its independent confirmation.


### Worked numerical case — Toy equilibrium sensitivity

**Fictional data:** Forcing 3.7 W/m², restoring parameter 1.1 W/m²/K.

**Calculation:** `3.7/1.1`. The numerical result is **3.364 K**. Explicitly verify its units and interpretation; the number is a conditional result from invented inputs, not a documented observation. **Sensitivity:** perturb the dominant uncertain input by 10% and report what changes. Not a direct IPCC estimate; simple equilibrium response only. Explain which excluded process might invalidate the simplified estimate.


### Limits, confounding and counterfactual reasoning

Dividing observed warming by assumed forcing without accounting for internal variability and heat uptake misestimates sensitivity. Contrast an alternative mechanism and state an observation that could discriminate between them. A more complex fitted curve is not necessarily a better causal explanation. Record station metadata, climate regime and measurement support before transferring a conclusion to a new situation.


### Practical study investigation

Explain the parameter identifiability problem using two models with similar short-term fits. Use `datasets/unit-06-synthetic.csv` for reproducible practice: plot the yearly variable and a five-year average while stating what the smoothing removes; annotate potential instrument error and a rival hypothesis. Reserve some observations for an independent check. The synthetic values are not validated natural observations, and apparent agreement with an illustrative model is not climate-data verification.


### Conceptual checks and problem set

1. Draw the physical process underlying **Climate sensitivity and transient response**, then label the state variables, external forcing, feedbacks and observational boundary. Which label is least well supported?
2. Reproduce the worked example with all unit conversions visible. Change one assumed value by 10%; report the new answer and interpret whether its sign or scale is plausible.
3. Explain how **dividing observed warming by assumed forcing without accounting for internal variability and heat uptake misestimates sensitivity.** Give one additional observable that would distinguish this issue from the core mechanism.
4. Translate the case into an observational protocol: station placement, sample frequency, calibration information, data exclusion rules and one independent validation source.
5. Identify a failure mode for the proposed task: **Explain the parameter identifiability problem using two models with similar short-term fits.** Explain how biased sampling, omitted uncertainty or changes in the measurement system could produce a misleading conclusion.

**Answer expectations:** A competent response states the physical assumption, uses correctly dimensioned quantities, provides an interpretation in the context of the mechanism, reports an alternative explanation, and explicitly distinguishes fictional numerical inputs from observed climatological evidence. Answers that assert an exact future climate outcome from these toy equations require independent validation.


## Lesson 6.4 — Ensembles, bias correction and downscaling

### The physical question

Multi-model ensembles sample some structural choices but do not constitute uniformly independent random draws from all possible climate futures. Dynamical downscaling adds regional process representation, while statistical downscaling assumes empirically stable relationships. Bias correction can improve marginal distributions without fixing temporal dependence or physical causality. For the synthetic case, distinguish measured state, forcing, feedback, trend and any fitted relationship. An observed long-term change must be distinguished from sampling artifacts, internal variability and reference-period effects. Record the spatial scale, instrument history and averaging interval.


### From fundamental laws to an operational approximation

Begin by diagramming **scenario assumptions to regional model output** and labeling **model forcings, parameters and initial conditions**. Choose a defensible statistical estimator, physical balance or mass-budget relationship appropriate to this topic. Distinguish the underlying process from the approximations in a fitted model, observational indicator or toy equation. Check dimensions and direction conventions before calculating; climate fields may be spatially varying even when one chart appears constant.


### What observations could distinguish mechanisms?

Compare ensemble median, full range and station-scale validation of downscaled daily precipitation. Identify the observation time, position, calibration information and observational resolution. Contrast **physical model diagnostics**, **held-out instrumental record** and **scenario-conditional ensemble comparison**. A strong analysis identifies at least one independent variable, region or time interval where competing explanations make different predictions. In particular, assess time autocorrelation; never use the same evidence both to tune a hypothesis and to claim its independent confirmation.


### Worked numerical case — Ensemble median

**Fictional data:** Three model projections are 2.0, 2.4 and 3.5°C for an illustrative scenario.

**Calculation:** `2.4`. The numerical result is **2.4 °C**. Explicitly verify its units and interpretation; the number is a conditional result from invented inputs, not a documented observation. **Sensitivity:** perturb the dominant uncertain input by 10% and report what changes. Model runs are not necessarily independent or equally plausible. Explain which excluded process might invalidate the simplified estimate.


### Limits, confounding and counterfactual reasoning

An artificially narrow spread after bias correction should not be mistaken for reduced physical uncertainty. Contrast an alternative mechanism and state an observation that could discriminate between them. A more complex fitted curve is not necessarily a better causal explanation. Record station metadata, climate regime and measurement support before transferring a conclusion to a new situation.


### Practical study investigation

Audit a regional projection for calibration overlap, independence and support of validation records. Use `datasets/unit-06-synthetic.csv` for reproducible practice: plot the yearly variable and a five-year average while stating what the smoothing removes; annotate potential instrument error and a rival hypothesis. Reserve some observations for an independent check. The synthetic values are not validated natural observations, and apparent agreement with an illustrative model is not climate-data verification.


### Conceptual checks and problem set

1. Draw the physical process underlying **Ensembles, bias correction and downscaling**, then label the state variables, external forcing, feedbacks and observational boundary. Which label is least well supported?
2. Reproduce the worked example with all unit conversions visible. Change one assumed value by 10%; report the new answer and interpret whether its sign or scale is plausible.
3. Explain how **an artificially narrow spread after bias correction should not be mistaken for reduced physical uncertainty.** Give one additional observable that would distinguish this issue from the core mechanism.
4. Translate the case into an observational protocol: station placement, sample frequency, calibration information, data exclusion rules and one independent validation source.
5. Identify a failure mode for the proposed task: **Audit a regional projection for calibration overlap, independence and support of validation records.** Explain how biased sampling, omitted uncertainty or changes in the measurement system could produce a misleading conclusion.

**Answer expectations:** A competent response states the physical assumption, uses correctly dimensioned quantities, provides an interpretation in the context of the mechanism, reports an alternative explanation, and explicitly distinguishes fictional numerical inputs from observed climatological evidence. Answers that assert an exact future climate outcome from these toy equations require independent validation.


## Lesson 6.5 — Model validation, emergent constraints and uncertainty

### The physical question

Useful evaluation targets include conservation, variability, extremes, observations outside tuning samples, and simulated responses to known perturbations. An emergent constraint links observable variability or climate-state relationships to a harder-to-measure future response, and needs a defensible mechanism. Overfitting a limited ensemble can create spurious predictive confidence. For the synthetic case, distinguish measured state, forcing, feedback, trend and any fitted relationship. An observed long-term change must be distinguished from sampling artifacts, internal variability and reference-period effects. Record the spatial scale, instrument history and averaging interval.


### From fundamental laws to an operational approximation

Begin by diagramming **scenario assumptions to regional model output** and labeling **model forcings, parameters and initial conditions**. Choose a defensible statistical estimator, physical balance or mass-budget relationship appropriate to this topic. Distinguish the underlying process from the approximations in a fitted model, observational indicator or toy equation. Check dimensions and direction conventions before calculating; climate fields may be spatially varying even when one chart appears constant.


### What observations could distinguish mechanisms?

Fit a proposed observational constraint on a subset of teaching models, then test prediction on held-out members. Identify the observation time, position, calibration information and observational resolution. Contrast **physical model diagnostics**, **held-out instrumental record** and **scenario-conditional ensemble comparison**. A strong analysis identifies at least one independent variable, region or time interval where competing explanations make different predictions. In particular, assess a shift in observational method; never use the same evidence both to tune a hypothesis and to claim its independent confirmation.


### Worked numerical case — Bias correction offset

**Fictional data:** Fictional model mean 19.7°C, reference mean 18.4°C.

**Calculation:** `19.7-18.4`. The numerical result is **1.3 °C bias**. Explicitly verify its units and interpretation; the number is a conditional result from invented inputs, not a documented observation. **Sensitivity:** perturb the dominant uncertain input by 10% and report what changes. Subtracting mean bias does not repair variance or extremes. Explain which excluded process might invalidate the simplified estimate.


### Limits, confounding and counterfactual reasoning

Small multi-model samples and shared ancestry can exaggerate correlation precision. Contrast an alternative mechanism and state an observation that could discriminate between them. A more complex fitted curve is not necessarily a better causal explanation. Record station metadata, climate regime and measurement support before transferring a conclusion to a new situation.


### Practical study investigation

Produce a transparent uncertainty taxonomy with structural, observational, internal and scenario terms. Use `datasets/unit-06-synthetic.csv` for reproducible practice: plot the yearly variable and a five-year average while stating what the smoothing removes; annotate potential instrument error and a rival hypothesis. Reserve some observations for an independent check. The synthetic values are not validated natural observations, and apparent agreement with an illustrative model is not climate-data verification.


### Conceptual checks and problem set

1. Draw the physical process underlying **Model validation, emergent constraints and uncertainty**, then label the state variables, external forcing, feedbacks and observational boundary. Which label is least well supported?
2. Reproduce the worked example with all unit conversions visible. Change one assumed value by 10%; report the new answer and interpret whether its sign or scale is plausible.
3. Explain how **small multi-model samples and shared ancestry can exaggerate correlation precision.** Give one additional observable that would distinguish this issue from the core mechanism.
4. Translate the case into an observational protocol: station placement, sample frequency, calibration information, data exclusion rules and one independent validation source.
5. Identify a failure mode for the proposed task: **Produce a transparent uncertainty taxonomy with structural, observational, internal and scenario terms.** Explain how biased sampling, omitted uncertainty or changes in the measurement system could produce a misleading conclusion.

**Answer expectations:** A competent response states the physical assumption, uses correctly dimensioned quantities, provides an interpretation in the context of the mechanism, reports an alternative explanation, and explicitly distinguishes fictional numerical inputs from observed climatological evidence. Answers that assert an exact future climate outcome from these toy equations require independent validation.


## Unit 6 capstone — A reproducible climate-science argument

Start from the research question **How can climate models be evaluated and used responsibly to explore plausible futures?**. Create an evidence map that distinguishes the three sources **physical model diagnostics**, **held-out instrumental record** and **scenario-conditional ensemble comparison**. The first source should establish the main physical state, the second should show whether the proposed forcing was present, and the third should offer a genuinely independent check. For the synthetic scenario, state a primary hypothesis and an alternative that differs in mechanism rather than merely in parameter size. Specify what both would predict for the same geographic area under different observing or forcing conditions. In your technical report, use no unexplained uncertainty bars; distinguish calibration limits, observation support, model approximation, initialization errors, and uncertainty about the process itself.

**Data and reproducibility task:** Read the 30 synthetic records for this unit. Interpret the annual year column as a time axis, calculate a decadal mean and robust spread, and repeat the trend after withholding every fifth year. If the trend changes materially, explain whether the underlying signal might be under-sampled. Prepare a plain-language summary of what the dataset can and cannot support. Supply enough detail that another student can reproduce every calculation without contacting the author. Explain structural uncertainty, internal variability and scenario dependence separately.

**Critical discussion:** Suppose an institution must make a decision from the available analysis. Identify the evidence that is missing, the consequence of a false alarm versus a missed event, and the observation that would most efficiently reduce consequential uncertainty. Provide a direct recommendation only when the dataset and problem definition warrant one. Never treat synthetic climatological examples as an operational alert or regulatory threshold.

## Key takeaways for Unit 6

- The subject is an coupled climate system, not just an isolated plotted correlation; a defensible explanation must respect fundamental balances.
- The measurement domain, spatial scale, averaging interval and uncertainty control what can be inferred.
- The worked formulas expose sensitivity and limiting assumptions, not an automatic prediction for an unobserved site.
- A scientifically meaningful alternative hypothesis requires an observation that could falsify it.
- Operational warnings require responsible climatological services and independently validated evidence.
