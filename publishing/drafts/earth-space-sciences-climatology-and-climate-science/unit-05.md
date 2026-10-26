# Unit 5 — Paleoclimate and evidence of past change
## The central climate-science investigation

**Question:** What can proxies reveal about past climates, chronology and natural forcing?

**Case setting:** A hypothetical lake-sediment core, tree-ring chronology and ice-core record overlap imperfectly. All locations and observations in the following investigation are synthetic. The purpose is to learn which inference would survive contact with independent measurements, rather than to produce a plausible-sounding story from an incomplete climate map.

Past climates are reconstructed by linking archives to environmental mechanisms. Tree rings may favor moisture or temperature depending on limiting conditions; ice isotopes involve moisture sources and condensation processes; marine microfossils are affected by ecology and preservation. None is an automatic thermometer. Calibration and cross-validation should use independent overlap, while dating uncertainty must be propagated into any analysis of abrupt transitions.

Multiple archives can corroborate a climate episode without necessarily sharing the same temporal resolution. A smoothed sediment signal might not resolve a short event captured by an annually dated tree-ring series. Comparing reconstructed changes requires common baseline units, calibration assumptions and age models. The history of forcing from orbital geometry, volcanism and greenhouse gases must be matched against chronology rather than inserted after the conclusion.

### Working boundaries and research assumptions

The effective observational transect for this unit runs from **physical proxy archive to dated climate reconstruction**. Different forms of evidence support different kinds of inference: primary proxy measurement constrains one aspect, dated chronological markers another, and independent proxy reconstruction a third. These are not interchangeable. A flux through a boundary differs from stored heat or carbon; a baseline-dependent anomaly is not an absolute state; a correlation alone cannot establish forcing attribution. Choose a geographic domain or explicit accounting boundary before writing the governing relationship. Record the averaging period and the geographical support used in comparisons.

The capstone makes a composite reconstruction from three invented archives, reports distinct uncertainties for proxy response and calendar age, and uses an independent record as a falsification check.

### What success looks like

A strong unit report reconstructs a physical chain from forcing to response while maintaining the distinction between an observation, a calculation, a model hypothesis and a decision. Include a figure that cannot be understood without axis units, a written alternative explanation and a comparison with a second type of evidence. Produce a proxy interpretation with age uncertainty and independent calibration.


## Lesson 5.1 — Proxy formation and calibration

### The physical question

A climate proxy responds to temperature, moisture or environmental conditions through a biological, chemical or physical process. Proxy response may vary across seasons and can be affected by non-climatic changes. Calibration against measured climate helps interpret a proxy, but short overlap periods can misrepresent past relationships. For the synthetic case, distinguish measured state, forcing, feedback, trend and any fitted relationship. An observed long-term change must be distinguished from sampling artifacts, internal variability and reference-period effects. Record the spatial scale, instrument history and averaging interval.


### From fundamental laws to an operational approximation

Begin by diagramming **physical proxy archive to dated climate reconstruction** and labeling **proxy measurement and chronology**. Choose a defensible statistical estimator, physical balance or mass-budget relationship appropriate to this topic. Distinguish the underlying process from the approximations in a fitted model, observational indicator or toy equation. Check dimensions and direction conventions before calculating; climate fields may be spatially varying even when one chart appears constant.


### What observations could distinguish mechanisms?

Compare a fictional tree-ring width series with seasonal precipitation and temperature across a calibration and validation window. Identify the observation time, position, calibration information and observational resolution. Contrast **primary proxy measurement**, **dated chronological markers** and **independent proxy reconstruction**. A strong analysis identifies at least one independent variable, region or time interval where competing explanations make different predictions. In particular, assess a possible common forcing; never use the same evidence both to tune a hypothesis and to claim its independent confirmation.


### Worked numerical case — Proxy calibration prediction

**Fictional data:** Toy proxy relation T(°C)=10+0.08×ring index; index is 70.

**Calculation:** `10+0.08*70`. The numerical result is **15.6 °C**. Explicitly verify its units and interpretation; the number is a conditional result from invented inputs, not a documented observation. **Sensitivity:** perturb the dominant uncertain input by 10% and report what changes. A true proxy transfer function requires validated calibration. Explain which excluded process might invalidate the simplified estimate.


### Limits, confounding and counterfactual reasoning

Strong calibration correlation may arise from shared trends or autocorrelation rather than stable mechanistic sensitivity. Contrast an alternative mechanism and state an observation that could discriminate between them. A more complex fitted curve is not necessarily a better causal explanation. Record station metadata, climate regime and measurement support before transferring a conclusion to a new situation.


### Practical study investigation

Write a proxy transfer function and test it on withheld years. Use `datasets/unit-05-synthetic.csv` for reproducible practice: plot the yearly variable and a five-year average while stating what the smoothing removes; annotate potential instrument error and a rival hypothesis. Reserve some observations for an independent check. The synthetic values are not validated natural observations, and apparent agreement with an illustrative model is not climate-data verification.


### Conceptual checks and problem set

1. Draw the physical process underlying **Proxy formation and calibration**, then label the state variables, external forcing, feedbacks and observational boundary. Which label is least well supported?
2. Reproduce the worked example with all unit conversions visible. Change one assumed value by 10%; report the new answer and interpret whether its sign or scale is plausible.
3. Explain how **strong calibration correlation may arise from shared trends or autocorrelation rather than stable mechanistic sensitivity.** Give one additional observable that would distinguish this issue from the core mechanism.
4. Translate the case into an observational protocol: station placement, sample frequency, calibration information, data exclusion rules and one independent validation source.
5. Identify a failure mode for the proposed task: **Write a proxy transfer function and test it on withheld years.** Explain how biased sampling, omitted uncertainty or changes in the measurement system could produce a misleading conclusion.

**Answer expectations:** A competent response states the physical assumption, uses correctly dimensioned quantities, provides an interpretation in the context of the mechanism, reports an alternative explanation, and explicitly distinguishes fictional numerical inputs from observed climatological evidence. Answers that assert an exact future climate outcome from these toy equations require independent validation.


## Lesson 5.2 — Chronologies and age-model uncertainty

### The physical question

Tree rings may supply annual dating in suitable material; sediments and ice often need depth-to-age models from layer counts or dated markers. Uncertainty can accumulate between tie points and may vary strongly with depth. Records with uncertain ages should not be aligned by maximizing correlation alone. For the synthetic case, distinguish measured state, forcing, feedback, trend and any fitted relationship. An observed long-term change must be distinguished from sampling artifacts, internal variability and reference-period effects. Record the spatial scale, instrument history and averaging interval.


### From fundamental laws to an operational approximation

Begin by diagramming **physical proxy archive to dated climate reconstruction** and labeling **proxy measurement and chronology**. Choose a defensible statistical estimator, physical balance or mass-budget relationship appropriate to this topic. Distinguish the underlying process from the approximations in a fitted model, observational indicator or toy equation. Check dimensions and direction conventions before calculating; climate fields may be spatially varying even when one chart appears constant.


### What observations could distinguish mechanisms?

Use two fictional dated marker horizons to interpolate sediment age and propagate age uncertainty. Identify the observation time, position, calibration information and observational resolution. Contrast **primary proxy measurement**, **dated chronological markers** and **independent proxy reconstruction**. A strong analysis identifies at least one independent variable, region or time interval where competing explanations make different predictions. In particular, assess a distribution that is non-stationary; never use the same evidence both to tune a hypothesis and to claim its independent confirmation.


### Worked numerical case — Linear sediment age model

**Fictional data:** At 1 m depth the age is 2000 y BP; at 3 m it is 6000 y BP. Estimate age at 2 m.

**Calculation:** `2000+(6000-2000)*(2-1)/(3-1)`. The numerical result is **4000 years BP**. Explicitly verify its units and interpretation; the number is a conditional result from invented inputs, not a documented observation. **Sensitivity:** perturb the dominant uncertain input by 10% and report what changes. Requires interpolation assumption and separate age uncertainty. Explain which excluded process might invalidate the simplified estimate.


### Limits, confounding and counterfactual reasoning

Assuming constant deposition between markers can fail during erosion, disturbance or changing sedimentation. Contrast an alternative mechanism and state an observation that could discriminate between them. A more complex fitted curve is not necessarily a better causal explanation. Record station metadata, climate regime and measurement support before transferring a conclusion to a new situation.


### Practical study investigation

Show how an event correlation changes when proxy ages vary within plausible bounds. Use `datasets/unit-05-synthetic.csv` for reproducible practice: plot the yearly variable and a five-year average while stating what the smoothing removes; annotate potential instrument error and a rival hypothesis. Reserve some observations for an independent check. The synthetic values are not validated natural observations, and apparent agreement with an illustrative model is not climate-data verification.


### Conceptual checks and problem set

1. Draw the physical process underlying **Chronologies and age-model uncertainty**, then label the state variables, external forcing, feedbacks and observational boundary. Which label is least well supported?
2. Reproduce the worked example with all unit conversions visible. Change one assumed value by 10%; report the new answer and interpret whether its sign or scale is plausible.
3. Explain how **assuming constant deposition between markers can fail during erosion, disturbance or changing sedimentation.** Give one additional observable that would distinguish this issue from the core mechanism.
4. Translate the case into an observational protocol: station placement, sample frequency, calibration information, data exclusion rules and one independent validation source.
5. Identify a failure mode for the proposed task: **Show how an event correlation changes when proxy ages vary within plausible bounds.** Explain how biased sampling, omitted uncertainty or changes in the measurement system could produce a misleading conclusion.

**Answer expectations:** A competent response states the physical assumption, uses correctly dimensioned quantities, provides an interpretation in the context of the mechanism, reports an alternative explanation, and explicitly distinguishes fictional numerical inputs from observed climatological evidence. Answers that assert an exact future climate outcome from these toy equations require independent validation.


## Lesson 5.3 — Ice cores, isotopes and atmospheric composition

### The physical question

Stable-isotope ratios in snow and ice reflect fractionation during evaporation, transport and condensation. The isotope–temperature relationship is context dependent and can be influenced by moisture source and seasonality. Trapped air samples contain a record of past atmospheric gas composition with an age offset relative to the surrounding ice. For the synthetic case, distinguish measured state, forcing, feedback, trend and any fitted relationship. An observed long-term change must be distinguished from sampling artifacts, internal variability and reference-period effects. Record the spatial scale, instrument history and averaging interval.


### From fundamental laws to an operational approximation

Begin by diagramming **physical proxy archive to dated climate reconstruction** and labeling **proxy measurement and chronology**. Choose a defensible statistical estimator, physical balance or mass-budget relationship appropriate to this topic. Distinguish the underlying process from the approximations in a fitted model, observational indicator or toy equation. Check dimensions and direction conventions before calculating; climate fields may be spatially varying even when one chart appears constant.


### What observations could distinguish mechanisms?

Contrast an invented isotope profile, dust event and gas record, tracking the separate ice-age and gas-age scales. Identify the observation time, position, calibration information and observational resolution. Contrast **primary proxy measurement**, **dated chronological markers** and **independent proxy reconstruction**. A strong analysis identifies at least one independent variable, region or time interval where competing explanations make different predictions. In particular, assess an undocumented instrument relocation; never use the same evidence both to tune a hypothesis and to claim its independent confirmation.


### Worked numerical case — Isotope offset

**Fictional data:** Illustrative sample δ18O −34.8‰ and reference −36.3‰.

**Calculation:** `-34.8-(-36.3)`. The numerical result is **1.5 per mille**. Explicitly verify its units and interpretation; the number is a conditional result from invented inputs, not a documented observation. **Sensitivity:** perturb the dominant uncertain input by 10% and report what changes. Isotope difference is not automatically a temperature difference. Explain which excluded process might invalidate the simplified estimate.


### Limits, confounding and counterfactual reasoning

A fixed isotope-to-temperature conversion imported from a different ice sheet is not generally defensible. Contrast an alternative mechanism and state an observation that could discriminate between them. A more complex fitted curve is not necessarily a better causal explanation. Record station metadata, climate regime and measurement support before transferring a conclusion to a new situation.


### Practical study investigation

Develop a multi-proxy reconstruction with explicit physical assumptions. Use `datasets/unit-05-synthetic.csv` for reproducible practice: plot the yearly variable and a five-year average while stating what the smoothing removes; annotate potential instrument error and a rival hypothesis. Reserve some observations for an independent check. The synthetic values are not validated natural observations, and apparent agreement with an illustrative model is not climate-data verification.


### Conceptual checks and problem set

1. Draw the physical process underlying **Ice cores, isotopes and atmospheric composition**, then label the state variables, external forcing, feedbacks and observational boundary. Which label is least well supported?
2. Reproduce the worked example with all unit conversions visible. Change one assumed value by 10%; report the new answer and interpret whether its sign or scale is plausible.
3. Explain how **a fixed isotope-to-temperature conversion imported from a different ice sheet is not generally defensible.** Give one additional observable that would distinguish this issue from the core mechanism.
4. Translate the case into an observational protocol: station placement, sample frequency, calibration information, data exclusion rules and one independent validation source.
5. Identify a failure mode for the proposed task: **Develop a multi-proxy reconstruction with explicit physical assumptions.** Explain how biased sampling, omitted uncertainty or changes in the measurement system could produce a misleading conclusion.

**Answer expectations:** A competent response states the physical assumption, uses correctly dimensioned quantities, provides an interpretation in the context of the mechanism, reports an alternative explanation, and explicitly distinguishes fictional numerical inputs from observed climatological evidence. Answers that assert an exact future climate outcome from these toy equations require independent validation.


## Lesson 5.4 — Marine and lake sediment archives

### The physical question

Foraminiferal assemblages, oxygen isotopes and sediment composition can infer past ocean conditions, but preservation, mixing and changes in season of production complicate interpretation. Lake sediments also respond to catchment disturbance and hydrology. Sediment archive resolution is not constant through time. For the synthetic case, distinguish measured state, forcing, feedback, trend and any fitted relationship. An observed long-term change must be distinguished from sampling artifacts, internal variability and reference-period effects. Record the spatial scale, instrument history and averaging interval.


### From fundamental laws to an operational approximation

Begin by diagramming **physical proxy archive to dated climate reconstruction** and labeling **proxy measurement and chronology**. Choose a defensible statistical estimator, physical balance or mass-budget relationship appropriate to this topic. Distinguish the underlying process from the approximations in a fitted model, observational indicator or toy equation. Check dimensions and direction conventions before calculating; climate fields may be spatially varying even when one chart appears constant.


### What observations could distinguish mechanisms?

Compare fictional microfossil and isotope signals with sediment grain size over several depths. Identify the observation time, position, calibration information and observational resolution. Contrast **primary proxy measurement**, **dated chronological markers** and **independent proxy reconstruction**. A strong analysis identifies at least one independent variable, region or time interval where competing explanations make different predictions. In particular, assess heterogeneous geographic coverage; never use the same evidence both to tune a hypothesis and to claim its independent confirmation.


### Worked numerical case — Sediment accumulation

**Fictional data:** An undisturbed 60 cm section deposited over 3000 years.

**Calculation:** `60/3000`. The numerical result is **0.02 cm/year**. Explicitly verify its units and interpretation; the number is a conditional result from invented inputs, not a documented observation. **Sensitivity:** perturb the dominant uncertain input by 10% and report what changes. Real sediment accumulation varies and cores may be disturbed. Explain which excluded process might invalidate the simplified estimate.


### Limits, confounding and counterfactual reasoning

Bioturbation can smear short events; the apparent absence of a rapid pulse may be an archive-resolution limit. Contrast an alternative mechanism and state an observation that could discriminate between them. A more complex fitted curve is not necessarily a better causal explanation. Record station metadata, climate regime and measurement support before transferring a conclusion to a new situation.


### Practical study investigation

Quantify how smoothing a sharp step changes inferred rate of change. Use `datasets/unit-05-synthetic.csv` for reproducible practice: plot the yearly variable and a five-year average while stating what the smoothing removes; annotate potential instrument error and a rival hypothesis. Reserve some observations for an independent check. The synthetic values are not validated natural observations, and apparent agreement with an illustrative model is not climate-data verification.


### Conceptual checks and problem set

1. Draw the physical process underlying **Marine and lake sediment archives**, then label the state variables, external forcing, feedbacks and observational boundary. Which label is least well supported?
2. Reproduce the worked example with all unit conversions visible. Change one assumed value by 10%; report the new answer and interpret whether its sign or scale is plausible.
3. Explain how **bioturbation can smear short events; the apparent absence of a rapid pulse may be an archive-resolution limit.** Give one additional observable that would distinguish this issue from the core mechanism.
4. Translate the case into an observational protocol: station placement, sample frequency, calibration information, data exclusion rules and one independent validation source.
5. Identify a failure mode for the proposed task: **Quantify how smoothing a sharp step changes inferred rate of change.** Explain how biased sampling, omitted uncertainty or changes in the measurement system could produce a misleading conclusion.

**Answer expectations:** A competent response states the physical assumption, uses correctly dimensioned quantities, provides an interpretation in the context of the mechanism, reports an alternative explanation, and explicitly distinguishes fictional numerical inputs from observed climatological evidence. Answers that assert an exact future climate outcome from these toy equations require independent validation.


## Lesson 5.5 — Natural forcing and climate transitions

### The physical question

Orbital cycles shift the seasonal and latitudinal distribution of insolation, while volcanic aerosols and solar variability also perturb energy balance. Feedbacks from ice sheets and greenhouse gases can amplify or redistribute slow forcings. Abrupt events may involve thresholds and ocean circulation changes. For the synthetic case, distinguish measured state, forcing, feedback, trend and any fitted relationship. An observed long-term change must be distinguished from sampling artifacts, internal variability and reference-period effects. Record the spatial scale, instrument history and averaging interval.


### From fundamental laws to an operational approximation

Begin by diagramming **physical proxy archive to dated climate reconstruction** and labeling **proxy measurement and chronology**. Choose a defensible statistical estimator, physical balance or mass-budget relationship appropriate to this topic. Distinguish the underlying process from the approximations in a fitted model, observational indicator or toy equation. Check dimensions and direction conventions before calculating; climate fields may be spatially varying even when one chart appears constant.


### What observations could distinguish mechanisms?

Compare phase relationships between orbital forcing, ice extent and greenhouse gas proxies rather than assuming simultaneous peaks. Identify the observation time, position, calibration information and observational resolution. Contrast **primary proxy measurement**, **dated chronological markers** and **independent proxy reconstruction**. A strong analysis identifies at least one independent variable, region or time interval where competing explanations make different predictions. In particular, assess a possible common forcing; never use the same evidence both to tune a hypothesis and to claim its independent confirmation.


### Worked numerical case — Orbital-timescale separation

**Fictional data:** A 23,000-year orbital cycle compared with a 100-year observation span.

**Calculation:** `23000/100`. The numerical result is **230 times longer**. Explicitly verify its units and interpretation; the number is a conditional result from invented inputs, not a documented observation. **Sensitivity:** perturb the dominant uncertain input by 10% and report what changes. This ratio is not a measure of physical forcing strength. Explain which excluded process might invalidate the simplified estimate.


### Limits, confounding and counterfactual reasoning

A causal explanation needs timescale and chronology consistency; correlation alone is insufficient. Contrast an alternative mechanism and state an observation that could discriminate between them. A more complex fitted curve is not necessarily a better causal explanation. Record station metadata, climate regime and measurement support before transferring a conclusion to a new situation.


### Practical study investigation

Write a chronology with alternative causal orderings and test which observations could distinguish them. Use `datasets/unit-05-synthetic.csv` for reproducible practice: plot the yearly variable and a five-year average while stating what the smoothing removes; annotate potential instrument error and a rival hypothesis. Reserve some observations for an independent check. The synthetic values are not validated natural observations, and apparent agreement with an illustrative model is not climate-data verification.


### Conceptual checks and problem set

1. Draw the physical process underlying **Natural forcing and climate transitions**, then label the state variables, external forcing, feedbacks and observational boundary. Which label is least well supported?
2. Reproduce the worked example with all unit conversions visible. Change one assumed value by 10%; report the new answer and interpret whether its sign or scale is plausible.
3. Explain how **a causal explanation needs timescale and chronology consistency; correlation alone is insufficient.** Give one additional observable that would distinguish this issue from the core mechanism.
4. Translate the case into an observational protocol: station placement, sample frequency, calibration information, data exclusion rules and one independent validation source.
5. Identify a failure mode for the proposed task: **Write a chronology with alternative causal orderings and test which observations could distinguish them.** Explain how biased sampling, omitted uncertainty or changes in the measurement system could produce a misleading conclusion.

**Answer expectations:** A competent response states the physical assumption, uses correctly dimensioned quantities, provides an interpretation in the context of the mechanism, reports an alternative explanation, and explicitly distinguishes fictional numerical inputs from observed climatological evidence. Answers that assert an exact future climate outcome from these toy equations require independent validation.


## Unit 5 capstone — A reproducible climate-science argument

Start from the research question **What can proxies reveal about past climates, chronology and natural forcing?**. Create an evidence map that distinguishes the three sources **primary proxy measurement**, **dated chronological markers** and **independent proxy reconstruction**. The first source should establish the main physical state, the second should show whether the proposed forcing was present, and the third should offer a genuinely independent check. For the synthetic scenario, state a primary hypothesis and an alternative that differs in mechanism rather than merely in parameter size. Specify what both would predict for the same geographic area under different observing or forcing conditions. In your technical report, use no unexplained uncertainty bars; distinguish calibration limits, observation support, model approximation, initialization errors, and uncertainty about the process itself.

**Data and reproducibility task:** Read the 30 synthetic records for this unit. Interpret the annual year column as a time axis, calculate a decadal mean and robust spread, and repeat the trend after withholding every fifth year. If the trend changes materially, explain whether the underlying signal might be under-sampled. Prepare a plain-language summary of what the dataset can and cannot support. Supply enough detail that another student can reproduce every calculation without contacting the author. Produce a proxy interpretation with age uncertainty and independent calibration.

**Critical discussion:** Suppose an institution must make a decision from the available analysis. Identify the evidence that is missing, the consequence of a false alarm versus a missed event, and the observation that would most efficiently reduce consequential uncertainty. Provide a direct recommendation only when the dataset and problem definition warrant one. Never treat synthetic climatological examples as an operational alert or regulatory threshold.

## Key takeaways for Unit 5

- The subject is an coupled climate system, not just an isolated plotted correlation; a defensible explanation must respect fundamental balances.
- The measurement domain, spatial scale, averaging interval and uncertainty control what can be inferred.
- The worked formulas expose sensitivity and limiting assumptions, not an automatic prediction for an unobserved site.
- A scientifically meaningful alternative hypothesis requires an observation that could falsify it.
- Operational warnings require responsible climatological services and independently validated evidence.
