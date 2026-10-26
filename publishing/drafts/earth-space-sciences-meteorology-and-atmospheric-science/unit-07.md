# Unit 7 — Observations, remote sensing and numerical forecasting
## The central atmospheric investigation

**Question:** How are atmospheric states observed, assimilated into models and evaluated as forecasts?

**Case setting:** A regional forecast desk must merge radar, surface stations, satellites and numerical ensemble output. All locations and observations in the following investigation are synthetic. The purpose is to learn which inference would survive contact with independent measurements, rather than to produce a plausible-sounding story from an incomplete weather map.

Every atmospheric observing system applies a measurement operator: a rain gauge measures accumulation in a small collecting area; radar samples backscatter within a volume; a satellite senses emitted or reflected electromagnetic radiation; an aircraft or radiosonde follows a moving trajectory. Their outputs differ even when none is faulty, because they represent different places, levels and physical quantities. Temporal averaging and observation latency can reverse the apparent order of rapidly developing events.

A numerical weather prediction model evolves approximate governing equations from estimated starting conditions, often using parameterizations for unresolved clouds and turbulence. Data assimilation combines incomplete measurements with a short-range forecast, conditioned on uncertainty assumptions. Ensembles sample several sources of possible futures but frequently share structural biases. Verification must compare like with like: location, lead time, variable, and event definition, alongside an honest baseline such as climatology or persistence.

### Working boundaries and research assumptions

The effective observational transect for this unit runs from **raw measurement through retrieval to forecast**. Different forms of evidence support different kinds of inference: raw station log constrains one aspect, independent verification archive another, and observation metadata a third. These are not interchangeable. A flux through a boundary is different from a store inside a region; a spatial gradient is not a material change through time; a measured scalar does not determine a complete three-dimensional vector. Choose a control volume or moving parcel explicitly before writing the governing relationship. Record the averaging period and the geographical support used in comparisons.

A calibrated 70% rain forecast should correspond to approximately seven events in ten comparable forecasts, not rain across 70% of the city. Score probabilistic and deterministic predictions separately. Explain why high-resolution pictures and a precisely written number are not themselves proof of forecast skill.

### What success looks like

A strong unit report reconstructs a physical chain from forcing to response while maintaining the distinction between an observation, a calculation, a model hypothesis and a decision. Include a figure that cannot be understood without axis units, a written alternative explanation and a comparison with a second type of evidence. Quantify representativeness, latency, instrument biases and out-of-sample forecast verification.


## Lesson 7.1 — Surface networks and quality control

### The physical question

Automated stations sample point conditions while ships, buoys and aircraft extend coverage. Quality control detects physical inconsistencies, sensor drift and time-stamp errors before observations enter analysis or forecasts. For the synthetic case, distinguish state, flux, tendency and any empirical relationship. When air moves past a fixed sensor, an observed change does not by itself establish a local transformation. Record the vertical level and sampling interval.


### From fundamental laws to an operational approximation

Begin by drawing **raw measurement through retrieval to forecast** and labeling **observation support, sensor response and model resolution**. State a relevant physical conservation law, and distinguish that law from its simplified diagnostic approximation. Check dimensions and direction conventions before calculating; atmospheric fields may be spatially varying even when one chart appears constant.


### What observations could distinguish mechanisms?

Compare nearby station pressure and temperature series after converting them to compatible time zones and height datums. Identify the observation time, position, calibration information and observational resolution. Contrast **raw station log**, **independent verification archive** and **observation metadata**. A strong experiment predicts one place, time or altitude where rival explanations differ. In particular, assess weather regime change during averaging; never use the same evidence both to tune a hypothesis and to claim its independent confirmation.


### Worked numerical case — Station completeness

**Fictional data:** An hourly station reports 698 valid values of 720 expected; calculate completeness.

**Calculation:** `100*698/720`. The numerical result is **96.94 %**. Explicitly verify its units and interpretation; the number is a conditional result from invented inputs, not a documented observation. **Sensitivity:** perturb the dominant uncertain input by 10% and report what changes. Missing observations concentrated during storms are especially consequential. Explain which excluded process might invalidate the simplified estimate.


### Limits, confounding and counterfactual reasoning

Two nearby stations can differ from true microclimates, so automatic outlier removal can erase a real mesoscale signal. Contrast an alternative mechanism and state an observation that could discriminate between them. A more complex fitted curve is not necessarily a better causal explanation. Record site elevation, weather regime and measurement support before transferring a conclusion to a new situation.


### Practical study investigation

Create an automated check that flags impossible values but retains original data for review. Use `datasets/unit-07-synthetic.csv` for reproducible practice: plot the variable at native and aggregated sampling frequency; annotate potential instrument error and a rival hypothesis. Reserve some observations for an independent check. The synthetic values are not validated natural observations, and apparent agreement with an illustrative model is not forecast verification.


### Conceptual checks and problem set

1. Draw the physical process underlying **Surface networks and quality control**, then label the state variables, external forcing, fluxes and observational boundary. Which label is least well supported?
2. Reproduce the worked example with all unit conversions visible. Change one assumed value by 10%; report the new answer and interpret whether its sign or scale is plausible.
3. Explain how **two nearby stations can differ from true microclimates, so automatic outlier removal can erase a real mesoscale signal.** Give one additional observable that would distinguish this issue from the core mechanism.
4. Translate the case into an observational protocol: station placement, sample frequency, calibration information, data exclusion rules and one independent validation source.
5. Explain why **create an automated check that flags impossible values but retains original data for review.** might lead to a misleading conclusion if the sample were sparse or the relevant atmospheric state changed between observations.

**Answer expectations:** A competent response states the physical assumption, uses correctly dimensioned quantities, provides an interpretation in the context of the mechanism, reports an alternative explanation, and explicitly distinguishes fictional numerical inputs from observed meteorological evidence. Answers that assert a deterministic local forecast from these toy equations are not scientifically justified.


## Lesson 7.2 — Weather radar and Doppler principles

### The physical question

Radar measures electromagnetic backscatter, from which reflectivity and radial velocity are derived. Doppler velocity measures only motion toward or away from the instrument; dual-polarization variables help distinguish hydrometeor types. For the synthetic case, distinguish state, flux, tendency and any empirical relationship. When air moves past a fixed sensor, an observed change does not by itself establish a local transformation. Record the vertical level and sampling interval.


### From fundamental laws to an operational approximation

Begin by drawing **raw measurement through retrieval to forecast** and labeling **observation support, sensor response and model resolution**. State a relevant physical conservation law, and distinguish that law from its simplified diagnostic approximation. Check dimensions and direction conventions before calculating; atmospheric fields may be spatially varying even when one chart appears constant.


### What observations could distinguish mechanisms?

Analyze elevation scans with known beam heights, gauge comparisons and clutter masks during organized rain. Identify the observation time, position, calibration information and observational resolution. Contrast **raw station log**, **independent verification archive** and **observation metadata**. A strong experiment predicts one place, time or altitude where rival explanations differ. In particular, assess changes in observation height; never use the same evidence both to tune a hypothesis and to claim its independent confirmation.


### Worked numerical case — Radar two-way propagation

**Fictional data:** Electromagnetic pulse travels to a target at 75 km and back at c=3e8 m/s.

**Calculation:** `2*75000/3e8*1e6`. The numerical result is **500 microseconds**. Explicitly verify its units and interpretation; the number is a conditional result from invented inputs, not a documented observation. **Sensitivity:** perturb the dominant uncertain input by 10% and report what changes. Range errors from refraction and beam broadening need separate analysis. Explain which excluded process might invalidate the simplified estimate.


### Limits, confounding and counterfactual reasoning

A radar cannot resolve the full three-dimensional wind vector from one radial measurement without additional assumptions or scans. Contrast an alternative mechanism and state an observation that could discriminate between them. A more complex fitted curve is not necessarily a better causal explanation. Record site elevation, weather regime and measurement support before transferring a conclusion to a new situation.


### Practical study investigation

Compute round-trip signal travel time and show how beam geometry limits low-level coverage far from the site. Use `datasets/unit-07-synthetic.csv` for reproducible practice: plot the variable at native and aggregated sampling frequency; annotate potential instrument error and a rival hypothesis. Reserve some observations for an independent check. The synthetic values are not validated natural observations, and apparent agreement with an illustrative model is not forecast verification.


### Conceptual checks and problem set

1. Draw the physical process underlying **Weather radar and Doppler principles**, then label the state variables, external forcing, fluxes and observational boundary. Which label is least well supported?
2. Reproduce the worked example with all unit conversions visible. Change one assumed value by 10%; report the new answer and interpret whether its sign or scale is plausible.
3. Explain how **a radar cannot resolve the full three-dimensional wind vector from one radial measurement without additional assumptions or scans.** Give one additional observable that would distinguish this issue from the core mechanism.
4. Translate the case into an observational protocol: station placement, sample frequency, calibration information, data exclusion rules and one independent validation source.
5. Explain why **compute round-trip signal travel time and show how beam geometry limits low-level coverage far from the site.** might lead to a misleading conclusion if the sample were sparse or the relevant atmospheric state changed between observations.

**Answer expectations:** A competent response states the physical assumption, uses correctly dimensioned quantities, provides an interpretation in the context of the mechanism, reports an alternative explanation, and explicitly distinguishes fictional numerical inputs from observed meteorological evidence. Answers that assert a deterministic local forecast from these toy equations are not scientifically justified.


## Lesson 7.3 — Meteorological satellites and retrieval uncertainty

### The physical question

Visible, infrared and microwave channels provide different information about cloud tops, water vapor and atmospheric profiles. Retrieval algorithms infer geophysical quantities through radiative-transfer models and prior assumptions. For the synthetic case, distinguish state, flux, tendency and any empirical relationship. When air moves past a fixed sensor, an observed change does not by itself establish a local transformation. Record the vertical level and sampling interval.


### From fundamental laws to an operational approximation

Begin by drawing **raw measurement through retrieval to forecast** and labeling **observation support, sensor response and model resolution**. State a relevant physical conservation law, and distinguish that law from its simplified diagnostic approximation. Check dimensions and direction conventions before calculating; atmospheric fields may be spatially varying even when one chart appears constant.


### What observations could distinguish mechanisms?

Compare visible and infrared satellite loops against ground cloud observations and radiosonde humidity profiles. Identify the observation time, position, calibration information and observational resolution. Contrast **raw station log**, **independent verification archive** and **observation metadata**. A strong experiment predicts one place, time or altitude where rival explanations differ. In particular, assess instrument response to an abrupt transition; never use the same evidence both to tune a hypothesis and to claim its independent confirmation.


### Worked numerical case — Satellite sampling density

**Fictional data:** A sensor observes a region every 15 minutes; number of nominal scans in 24 h?

**Calculation:** `24*60/15`. The numerical result is **96 scans**. Explicitly verify its units and interpretation; the number is a conditional result from invented inputs, not a documented observation. **Sensitivity:** perturb the dominant uncertain input by 10% and report what changes. Temporal sampling can miss rapidly evolving convective structures. Explain which excluded process might invalidate the simplified estimate.


### Limits, confounding and counterfactual reasoning

Cold infrared brightness temperature does not necessarily imply surface precipitation; cirrus can be optically thin yet very cold. Contrast an alternative mechanism and state an observation that could discriminate between them. A more complex fitted curve is not necessarily a better causal explanation. Record site elevation, weather regime and measurement support before transferring a conclusion to a new situation.


### Practical study investigation

Develop an observation table distinguishing direct radiance measurements from retrieved estimates. Use `datasets/unit-07-synthetic.csv` for reproducible practice: plot the variable at native and aggregated sampling frequency; annotate potential instrument error and a rival hypothesis. Reserve some observations for an independent check. The synthetic values are not validated natural observations, and apparent agreement with an illustrative model is not forecast verification.


### Conceptual checks and problem set

1. Draw the physical process underlying **Meteorological satellites and retrieval uncertainty**, then label the state variables, external forcing, fluxes and observational boundary. Which label is least well supported?
2. Reproduce the worked example with all unit conversions visible. Change one assumed value by 10%; report the new answer and interpret whether its sign or scale is plausible.
3. Explain how **cold infrared brightness temperature does not necessarily imply surface precipitation; cirrus can be optically thin yet very cold.** Give one additional observable that would distinguish this issue from the core mechanism.
4. Translate the case into an observational protocol: station placement, sample frequency, calibration information, data exclusion rules and one independent validation source.
5. Explain why **develop an observation table distinguishing direct radiance measurements from retrieved estimates.** might lead to a misleading conclusion if the sample were sparse or the relevant atmospheric state changed between observations.

**Answer expectations:** A competent response states the physical assumption, uses correctly dimensioned quantities, provides an interpretation in the context of the mechanism, reports an alternative explanation, and explicitly distinguishes fictional numerical inputs from observed meteorological evidence. Answers that assert a deterministic local forecast from these toy equations are not scientifically justified.


## Lesson 7.4 — Numerical weather prediction and data assimilation

### The physical question

Prediction systems discretize fluid motion, thermodynamics and water processes using boundary and initial conditions. Data assimilation combines prior forecasts with observations using assumed uncertainty structures; unresolved processes require parameterization. For the synthetic case, distinguish state, flux, tendency and any empirical relationship. When air moves past a fixed sensor, an observed change does not by itself establish a local transformation. Record the vertical level and sampling interval.


### From fundamental laws to an operational approximation

Begin by drawing **raw measurement through retrieval to forecast** and labeling **observation support, sensor response and model resolution**. State a relevant physical conservation law, and distinguish that law from its simplified diagnostic approximation. Check dimensions and direction conventions before calculating; atmospheric fields may be spatially varying even when one chart appears constant.


### What observations could distinguish mechanisms?

Compare a model analysis with independent withheld stations, then diagnose changes following assimilation of a new sounding. Identify the observation time, position, calibration information and observational resolution. Contrast **raw station log**, **independent verification archive** and **observation metadata**. A strong experiment predicts one place, time or altitude where rival explanations differ. In particular, assess spatial interpolation across sparse stations; never use the same evidence both to tune a hypothesis and to claim its independent confirmation.


### Worked numerical case — Model timestep count

**Fictional data:** Forecast integrates 36 h with timestep 30 s; number of steps?

**Calculation:** `36*3600/30`. The numerical result is **4320 timesteps**. Explicitly verify its units and interpretation; the number is a conditional result from invented inputs, not a documented observation. **Sensitivity:** perturb the dominant uncertain input by 10% and report what changes. A fine timestep does not imply sufficiently fine spatial resolution. Explain which excluded process might invalidate the simplified estimate.


### Limits, confounding and counterfactual reasoning

A model can fit assimilated stations well but forecast poorly; initial analysis fit is not the same as future skill. Contrast an alternative mechanism and state an observation that could discriminate between them. A more complex fitted curve is not necessarily a better causal explanation. Record site elevation, weather regime and measurement support before transferring a conclusion to a new situation.


### Practical study investigation

Explain spin-up, truncation error and representativeness error using a heavy-rainfall case. Use `datasets/unit-07-synthetic.csv` for reproducible practice: plot the variable at native and aggregated sampling frequency; annotate potential instrument error and a rival hypothesis. Reserve some observations for an independent check. The synthetic values are not validated natural observations, and apparent agreement with an illustrative model is not forecast verification.


### Conceptual checks and problem set

1. Draw the physical process underlying **Numerical weather prediction and data assimilation**, then label the state variables, external forcing, fluxes and observational boundary. Which label is least well supported?
2. Reproduce the worked example with all unit conversions visible. Change one assumed value by 10%; report the new answer and interpret whether its sign or scale is plausible.
3. Explain how **a model can fit assimilated stations well but forecast poorly; initial analysis fit is not the same as future skill.** Give one additional observable that would distinguish this issue from the core mechanism.
4. Translate the case into an observational protocol: station placement, sample frequency, calibration information, data exclusion rules and one independent validation source.
5. Explain why **explain spin-up, truncation error and representativeness error using a heavy-rainfall case.** might lead to a misleading conclusion if the sample were sparse or the relevant atmospheric state changed between observations.

**Answer expectations:** A competent response states the physical assumption, uses correctly dimensioned quantities, provides an interpretation in the context of the mechanism, reports an alternative explanation, and explicitly distinguishes fictional numerical inputs from observed meteorological evidence. Answers that assert a deterministic local forecast from these toy equations are not scientifically justified.


## Lesson 7.5 — Ensembles, forecast verification and calibration

### The physical question

Forecast ensembles represent sampled sources of uncertainty, although all members can share model biases. Reliability, sharpness, Brier score and benchmark comparisons are distinct aspects of forecast quality. For the synthetic case, distinguish state, flux, tendency and any empirical relationship. When air moves past a fixed sensor, an observed change does not by itself establish a local transformation. Record the vertical level and sampling interval.


### From fundamental laws to an operational approximation

Begin by drawing **raw measurement through retrieval to forecast** and labeling **observation support, sensor response and model resolution**. State a relevant physical conservation law, and distinguish that law from its simplified diagnostic approximation. Check dimensions and direction conventions before calculating; atmospheric fields may be spatially varying even when one chart appears constant.


### What observations could distinguish mechanisms?

Calculate probability bins from a fictional archive and verify event frequencies, then assess changes after recalibration. Identify the observation time, position, calibration information and observational resolution. Contrast **raw station log**, **independent verification archive** and **observation metadata**. A strong experiment predicts one place, time or altitude where rival explanations differ. In particular, assess weather regime change during averaging; never use the same evidence both to tune a hypothesis and to claim its independent confirmation.


### Worked numerical case — Brier score

**Fictional data:** Forecast event probabilities [0.2,0.7,0.8] and outcomes [0,1,0].

**Calculation:** `((.2-0)**2+(.7-1)**2+(.8-0)**2)/3`. The numerical result is **0.2567 dimensionless**. Explicitly verify its units and interpretation; the number is a conditional result from invented inputs, not a documented observation. **Sensitivity:** perturb the dominant uncertain input by 10% and report what changes. Judge against a comparable reference forecast and many cases. Explain which excluded process might invalidate the simplified estimate.


### Limits, confounding and counterfactual reasoning

A high apparent hit rate may simply reflect a common non-event; rare-event warnings need event-sensitive metrics. Contrast an alternative mechanism and state an observation that could discriminate between them. A more complex fitted curve is not necessarily a better causal explanation. Record site elevation, weather regime and measurement support before transferring a conclusion to a new situation.


### Practical study investigation

Create a reliability diagram concept and identify the cost–loss tradeoff of different alert thresholds. Use `datasets/unit-07-synthetic.csv` for reproducible practice: plot the variable at native and aggregated sampling frequency; annotate potential instrument error and a rival hypothesis. Reserve some observations for an independent check. The synthetic values are not validated natural observations, and apparent agreement with an illustrative model is not forecast verification.


### Conceptual checks and problem set

1. Draw the physical process underlying **Ensembles, forecast verification and calibration**, then label the state variables, external forcing, fluxes and observational boundary. Which label is least well supported?
2. Reproduce the worked example with all unit conversions visible. Change one assumed value by 10%; report the new answer and interpret whether its sign or scale is plausible.
3. Explain how **a high apparent hit rate may simply reflect a common non-event; rare-event warnings need event-sensitive metrics.** Give one additional observable that would distinguish this issue from the core mechanism.
4. Translate the case into an observational protocol: station placement, sample frequency, calibration information, data exclusion rules and one independent validation source.
5. Explain why **create a reliability diagram concept and identify the cost–loss tradeoff of different alert thresholds.** might lead to a misleading conclusion if the sample were sparse or the relevant atmospheric state changed between observations.

**Answer expectations:** A competent response states the physical assumption, uses correctly dimensioned quantities, provides an interpretation in the context of the mechanism, reports an alternative explanation, and explicitly distinguishes fictional numerical inputs from observed meteorological evidence. Answers that assert a deterministic local forecast from these toy equations are not scientifically justified.


## Unit 7 capstone — A reproducible atmospheric argument

Start from the research question **How are atmospheric states observed, assimilated into models and evaluated as forecasts?**. Create an evidence map that distinguishes the three sources **raw station log**, **independent verification archive** and **observation metadata**. The first source should establish the main physical state, the second should show whether the proposed forcing was present, and the third should offer a genuinely independent check. For the synthetic scenario, state a primary hypothesis and an alternative that differs in mechanism rather than merely in parameter size. Specify what both would predict at the same station but at different heights or times. In your technical report, use no unexplained uncertainty bars; distinguish calibration limits, observation support, model approximation, initialization errors, and uncertainty about the process itself.

**Data and reproducibility task:** Read the 30 synthetic records for this unit. Convert the ISO timestamps into a time axis, compute a descriptive mean and a robust range, and repeat the analysis after removing every fifth observation. If the trend changes materially, explain whether the underlying signal might be under-sampled. Prepare a plain-language summary of what the dataset can and cannot support. Supply enough detail that another student can reproduce every calculation without contacting the author. Quantify representativeness, latency, instrument biases and out-of-sample forecast verification.

**Critical discussion:** Suppose an institution must make a decision from the available analysis. Identify the evidence that is missing, the consequence of a false alarm versus a missed event, and the observation that would most efficiently reduce consequential uncertainty. Provide a direct recommendation only when the dataset and problem definition warrant one. Never treat synthetic meteorological examples as an operational alert or regulatory threshold.

## Key takeaways for Unit 7

- The subject is an atmospheric system, not just an isolated plotted correlation; a defensible explanation must respect fundamental balances.
- The measurement domain, spatial scale, averaging interval and uncertainty control what can be inferred.
- The worked formulas expose sensitivity and limiting assumptions, not an automatic prediction for an unobserved site.
- A scientifically meaningful alternative hypothesis requires an observation that could falsify it.
- Operational warnings require responsible meteorological services and independently validated evidence.
