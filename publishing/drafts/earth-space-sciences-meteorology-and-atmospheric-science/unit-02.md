# Unit 2 — Radiation, surface exchange and the boundary layer
## The central atmospheric investigation

**Question:** How do energy fluxes between radiation, ground and turbulent air shape near-surface weather?

**Case setting:** A city–farmland transect shows contrasting temperatures and turbulence during clear and cloudy days. All locations and observations in the following investigation are synthetic. The purpose is to learn which inference would survive contact with independent measurements, rather than to produce a plausible-sounding story from an incomplete weather map.

Solar shortwave enters the Earth–atmosphere system with pronounced day–night and seasonal variation. Some is reflected by clouds, aerosols and the surface; the rest is absorbed by gases, clouds and ground. The ground emits longwave radiation and receives infrared radiation from the atmosphere. Net radiation is not itself equal to air heating: at the surface, energy also leaves through evaporation and sensible heat, enters or exits ground storage, or heats structures. These terms must refer to the same area and interval for an energy equation to close.

The Bowen ratio compares sensible to latent turbulent heat flux; a dry landscape and a wet irrigated field may both receive similar radiation but warm the air very differently. During a clear night, radiative cooling can produce a stable boundary layer where strong temperature inversions trap pollutants. Daytime buoyancy often deepens a mixed layer, but this depth also depends on synoptic subsidence and entrainment at its top. Surface roughness and obstacles change the vertical momentum transfer. A single rooftop thermometer is therefore a poor substitute for an exposure-controlled network.

### Working boundaries and research assumptions

The effective observational transect for this unit runs from **the top of the canopy to a reference height**. Different forms of evidence support different kinds of inference: radiometer record constrains one aspect, flux-footprint log another, and day–night turbulent profiles a third. These are not interchangeable. A flux through a boundary is different from a store inside a region; a spatial gradient is not a material change through time; a measured scalar does not determine a complete three-dimensional vector. Choose a control volume or moving parcel explicitly before writing the governing relationship. Record the averaging period and the geographical support used in comparisons.

The teaching transect should compare energy fluxes rather than making unsupported claims that tree planting reduces urban heat by one universal number. Record instrument placement, local material, cloud conditions, wind direction, fetch and time averaging. Distinguish changes in pedestrian radiant exposure from changes in standardized air temperature.

### What success looks like

A strong unit report reconstructs a physical chain from forcing to response while maintaining the distinction between an observation, a calculation, a model hypothesis and a decision. Include a figure that cannot be understood without axis units, a written alternative explanation and a comparison with a second type of evidence. Separate radiation, thermal inertia, anthropogenic heating, moisture and advection before assigning a cause.


## Lesson 2.1 — Shortwave radiation and albedo

### The physical question

Absorbed shortwave radiation depends on incoming solar flux, solar angle, cloud transmission and surface albedo. Fresh snow, water and vegetation behave differently, and a broadband albedo hides spectral and directional behavior. For the synthetic case, distinguish state, flux, tendency and any empirical relationship. When air moves past a fixed sensor, an observed change does not by itself establish a local transformation. Record the vertical level and sampling interval.


### From fundamental laws to an operational approximation

Begin by drawing **the top of the canopy to a reference height** and labeling **net energy and turbulent transport**. State a relevant physical conservation law, and distinguish that law from its simplified diagnostic approximation. Check dimensions and direction conventions before calculating; atmospheric fields may be spatially varying even when one chart appears constant.


### What observations could distinguish mechanisms?

Measure upward and downward pyranometer fluxes over asphalt and grass at matched solar times and cloud conditions. Identify the observation time, position, calibration information and observational resolution. Contrast **radiometer record**, **flux-footprint log** and **day–night turbulent profiles**. A strong experiment predicts one place, time or altitude where rival explanations differ. In particular, assess a poorly known top or lateral boundary; never use the same evidence both to tune a hypothesis and to claim its independent confirmation.


### Worked numerical case — Absorbed shortwave radiation

**Fictional data:** Downward solar flux 640 W/m² and albedo 0.25; find absorbed shortwave.

**Calculation:** `640*(1-.25)`. The numerical result is **480 W/m²**. Explicitly verify its units and interpretation; the number is a conditional result from invented inputs, not a documented observation. **Sensitivity:** perturb the dominant uncertain input by 10% and report what changes. Cloud transmission and albedo vary with time. Explain which excluded process might invalidate the simplified estimate.


### Limits, confounding and counterfactual reasoning

A one-time albedo estimate cannot isolate clouds, shading and changing sun angle; a wet surface may alter reflectance. Contrast an alternative mechanism and state an observation that could discriminate between them. A more complex fitted curve is not necessarily a better causal explanation. Record site elevation, weather regime and measurement support before transferring a conclusion to a new situation.


### Practical study investigation

Create an energy-flux diagram and estimate how reflective paving changes absorbed flux, not necessarily air temperature. Use `datasets/unit-02-synthetic.csv` for reproducible practice: plot the variable at native and aggregated sampling frequency; annotate potential instrument error and a rival hypothesis. Reserve some observations for an independent check. The synthetic values are not validated natural observations, and apparent agreement with an illustrative model is not forecast verification.


### Conceptual checks and problem set

1. Draw the physical process underlying **Shortwave radiation and albedo**, then label the state variables, external forcing, fluxes and observational boundary. Which label is least well supported?
2. Reproduce the worked example with all unit conversions visible. Change one assumed value by 10%; report the new answer and interpret whether its sign or scale is plausible.
3. Explain how **a one-time albedo estimate cannot isolate clouds, shading and changing sun angle; a wet surface may alter reflectance.** Give one additional observable that would distinguish this issue from the core mechanism.
4. Translate the case into an observational protocol: station placement, sample frequency, calibration information, data exclusion rules and one independent validation source.
5. Explain why **create an energy-flux diagram and estimate how reflective paving changes absorbed flux, not necessarily air temperature.** might lead to a misleading conclusion if the sample were sparse or the relevant atmospheric state changed between observations.

**Answer expectations:** A competent response states the physical assumption, uses correctly dimensioned quantities, provides an interpretation in the context of the mechanism, reports an alternative explanation, and explicitly distinguishes fictional numerical inputs from observed meteorological evidence. Answers that assert a deterministic local forecast from these toy equations are not scientifically justified.


## Lesson 2.2 — Longwave radiation and greenhouse gases

### The physical question

Terrestrial surfaces radiate approximately sigma T^4 times emissivity, but atmospheric absorption and emission redistribute infrared energy. Greenhouse gases influence effective emission to space and near-surface radiative fluxes through wavelength-dependent optical depth. For the synthetic case, distinguish state, flux, tendency and any empirical relationship. When air moves past a fixed sensor, an observed change does not by itself establish a local transformation. Record the vertical level and sampling interval.


### From fundamental laws to an operational approximation

Begin by drawing **the top of the canopy to a reference height** and labeling **net energy and turbulent transport**. State a relevant physical conservation law, and distinguish that law from its simplified diagnostic approximation. Check dimensions and direction conventions before calculating; atmospheric fields may be spatially varying even when one chart appears constant.


### What observations could distinguish mechanisms?

Compare thermal imagery and broadband longwave flux under clear and overcast conditions, recording surface and air temperatures. Identify the observation time, position, calibration information and observational resolution. Contrast **radiometer record**, **flux-footprint log** and **day–night turbulent profiles**. A strong experiment predicts one place, time or altitude where rival explanations differ. In particular, assess an unsupported assumption of local equilibrium; never use the same evidence both to tune a hypothesis and to claim its independent confirmation.


### Worked numerical case — Blackbody flux sensitivity

**Fictional data:** For emissivity 1, estimate emission from 290 K using sigma=5.670374419e−8 W m−2 K−4.

**Calculation:** `5.670374419e-8*290**4`. The numerical result is **401.1 W/m²**. Explicitly verify its units and interpretation; the number is a conditional result from invented inputs, not a documented observation. **Sensitivity:** perturb the dominant uncertain input by 10% and report what changes. Actual net longwave also depends on incoming atmospheric radiation. Explain which excluded process might invalidate the simplified estimate.


### Limits, confounding and counterfactual reasoning

A thermal camera infers brightness temperature using emissivity assumptions; brightness is not the same as measured air temperature. Contrast an alternative mechanism and state an observation that could discriminate between them. A more complex fitted curve is not necessarily a better causal explanation. Record site elevation, weather regime and measurement support before transferring a conclusion to a new situation.


### Practical study investigation

Write a two-layer radiative budget and identify parameters that change the sign of net flux. Use `datasets/unit-02-synthetic.csv` for reproducible practice: plot the variable at native and aggregated sampling frequency; annotate potential instrument error and a rival hypothesis. Reserve some observations for an independent check. The synthetic values are not validated natural observations, and apparent agreement with an illustrative model is not forecast verification.


### Conceptual checks and problem set

1. Draw the physical process underlying **Longwave radiation and greenhouse gases**, then label the state variables, external forcing, fluxes and observational boundary. Which label is least well supported?
2. Reproduce the worked example with all unit conversions visible. Change one assumed value by 10%; report the new answer and interpret whether its sign or scale is plausible.
3. Explain how **a thermal camera infers brightness temperature using emissivity assumptions; brightness is not the same as measured air temperature.** Give one additional observable that would distinguish this issue from the core mechanism.
4. Translate the case into an observational protocol: station placement, sample frequency, calibration information, data exclusion rules and one independent validation source.
5. Explain why **write a two-layer radiative budget and identify parameters that change the sign of net flux.** might lead to a misleading conclusion if the sample were sparse or the relevant atmospheric state changed between observations.

**Answer expectations:** A competent response states the physical assumption, uses correctly dimensioned quantities, provides an interpretation in the context of the mechanism, reports an alternative explanation, and explicitly distinguishes fictional numerical inputs from observed meteorological evidence. Answers that assert a deterministic local forecast from these toy equations are not scientifically justified.


## Lesson 2.3 — Surface energy balance and Bowen ratio

### The physical question

Net radiation is partitioned among latent heat, sensible heat, ground storage and sometimes anthropogenic or biological terms. The Bowen ratio H/LE summarizes turbulent partitioning, but measured closure can fail because of instrument and spatial mismatch. For the synthetic case, distinguish state, flux, tendency and any empirical relationship. When air moves past a fixed sensor, an observed change does not by itself establish a local transformation. Record the vertical level and sampling interval.


### From fundamental laws to an operational approximation

Begin by drawing **the top of the canopy to a reference height** and labeling **net energy and turbulent transport**. State a relevant physical conservation law, and distinguish that law from its simplified diagnostic approximation. Check dimensions and direction conventions before calculating; atmospheric fields may be spatially varying even when one chart appears constant.


### What observations could distinguish mechanisms?

Use eddy-covariance and soil heat flux observations to audit Rn minus H, LE and G over a uniform field. Identify the observation time, position, calibration information and observational resolution. Contrast **radiometer record**, **flux-footprint log** and **day–night turbulent profiles**. A strong experiment predicts one place, time or altitude where rival explanations differ. In particular, assess mixing between air masses; never use the same evidence both to tune a hypothesis and to claim its independent confirmation.


### Worked numerical case — Surface energy residual

**Fictional data:** Rn=440, H=150, LE=220, G=45 W/m²; calculate residual.

**Calculation:** `440-150-220-45`. The numerical result is **25 W/m²**. Explicitly verify its units and interpretation; the number is a conditional result from invented inputs, not a documented observation. **Sensitivity:** perturb the dominant uncertain input by 10% and report what changes. Do not automatically interpret an imbalance as one missing physical process. Explain which excluded process might invalidate the simplified estimate.


### Limits, confounding and counterfactual reasoning

Advected heat, heterogeneous fetch and instrument footprints produce residuals that cannot be assigned automatically to one flux. Contrast an alternative mechanism and state an observation that could discriminate between them. A more complex fitted curve is not necessarily a better causal explanation. Record site elevation, weather regime and measurement support before transferring a conclusion to a new situation.


### Practical study investigation

Compute a closure residual, propose two ways to reduce it, and explain their different evidential strength. Use `datasets/unit-02-synthetic.csv` for reproducible practice: plot the variable at native and aggregated sampling frequency; annotate potential instrument error and a rival hypothesis. Reserve some observations for an independent check. The synthetic values are not validated natural observations, and apparent agreement with an illustrative model is not forecast verification.


### Conceptual checks and problem set

1. Draw the physical process underlying **Surface energy balance and Bowen ratio**, then label the state variables, external forcing, fluxes and observational boundary. Which label is least well supported?
2. Reproduce the worked example with all unit conversions visible. Change one assumed value by 10%; report the new answer and interpret whether its sign or scale is plausible.
3. Explain how **advected heat, heterogeneous fetch and instrument footprints produce residuals that cannot be assigned automatically to one flux.** Give one additional observable that would distinguish this issue from the core mechanism.
4. Translate the case into an observational protocol: station placement, sample frequency, calibration information, data exclusion rules and one independent validation source.
5. Explain why **compute a closure residual, propose two ways to reduce it, and explain their different evidential strength.** might lead to a misleading conclusion if the sample were sparse or the relevant atmospheric state changed between observations.

**Answer expectations:** A competent response states the physical assumption, uses correctly dimensioned quantities, provides an interpretation in the context of the mechanism, reports an alternative explanation, and explicitly distinguishes fictional numerical inputs from observed meteorological evidence. Answers that assert a deterministic local forecast from these toy equations are not scientifically justified.


## Lesson 2.4 — Turbulent boundary layers and friction

### The physical question

Momentum transport in the atmospheric boundary layer involves turbulent eddies, mechanical shear and buoyant mixing. Friction velocity and Monin–Obukhov similarity are useful under restrictive near-stationary horizontally homogeneous conditions. For the synthetic case, distinguish state, flux, tendency and any empirical relationship. When air moves past a fixed sensor, an observed change does not by itself establish a local transformation. Record the vertical level and sampling interval.


### From fundamental laws to an operational approximation

Begin by drawing **the top of the canopy to a reference height** and labeling **net energy and turbulent transport**. State a relevant physical conservation law, and distinguish that law from its simplified diagnostic approximation. Check dimensions and direction conventions before calculating; atmospheric fields may be spatially varying even when one chart appears constant.


### What observations could distinguish mechanisms?

Compare wind profiles from a tower above open grassland and within a street canyon; note changing roughness. Identify the observation time, position, calibration information and observational resolution. Contrast **radiometer record**, **flux-footprint log** and **day–night turbulent profiles**. A strong experiment predicts one place, time or altitude where rival explanations differ. In particular, assess a measurement artifact mistaken for a physical anomaly; never use the same evidence both to tune a hypothesis and to claim its independent confirmation.


### Worked numerical case — Neutral logarithmic profile

**Fictional data:** u*=0.35 m/s, von Karman kappa=0.4; z=10 m and z0=0.1 m.

**Calculation:** `0.35/.4*math.log(10/.1)`. The numerical result is **4.03 m/s**. Explicitly verify its units and interpretation; the number is a conditional result from invented inputs, not a documented observation. **Sensitivity:** perturb the dominant uncertain input by 10% and report what changes. Neutral, horizontally homogeneous surface-layer assumptions are restrictive. Explain which excluded process might invalidate the simplified estimate.


### Limits, confounding and counterfactual reasoning

A logarithmic wind profile extrapolated over city roofs can fail because the local canopy creates displacement and complex wakes. Contrast an alternative mechanism and state an observation that could discriminate between them. A more complex fitted curve is not necessarily a better causal explanation. Record site elevation, weather regime and measurement support before transferring a conclusion to a new situation.


### Practical study investigation

Estimate a surface-layer wind gradient and identify where the log-law assumption breaks down. Use `datasets/unit-02-synthetic.csv` for reproducible practice: plot the variable at native and aggregated sampling frequency; annotate potential instrument error and a rival hypothesis. Reserve some observations for an independent check. The synthetic values are not validated natural observations, and apparent agreement with an illustrative model is not forecast verification.


### Conceptual checks and problem set

1. Draw the physical process underlying **Turbulent boundary layers and friction**, then label the state variables, external forcing, fluxes and observational boundary. Which label is least well supported?
2. Reproduce the worked example with all unit conversions visible. Change one assumed value by 10%; report the new answer and interpret whether its sign or scale is plausible.
3. Explain how **a logarithmic wind profile extrapolated over city roofs can fail because the local canopy creates displacement and complex wakes.** Give one additional observable that would distinguish this issue from the core mechanism.
4. Translate the case into an observational protocol: station placement, sample frequency, calibration information, data exclusion rules and one independent validation source.
5. Explain why **estimate a surface-layer wind gradient and identify where the log-law assumption breaks down.** might lead to a misleading conclusion if the sample were sparse or the relevant atmospheric state changed between observations.

**Answer expectations:** A competent response states the physical assumption, uses correctly dimensioned quantities, provides an interpretation in the context of the mechanism, reports an alternative explanation, and explicitly distinguishes fictional numerical inputs from observed meteorological evidence. Answers that assert a deterministic local forecast from these toy equations are not scientifically justified.


## Lesson 2.5 — Sea breezes, mountain winds and urban heat

### The physical question

Differential heating creates local pressure gradients and organized diurnal circulations, but larger synoptic winds can suppress or reverse them. Urban materials and geometry alter radiation, storage, evapotranspiration and nocturnal heat release. For the synthetic case, distinguish state, flux, tendency and any empirical relationship. When air moves past a fixed sensor, an observed change does not by itself establish a local transformation. Record the vertical level and sampling interval.


### From fundamental laws to an operational approximation

Begin by drawing **the top of the canopy to a reference height** and labeling **net energy and turbulent transport**. State a relevant physical conservation law, and distinguish that law from its simplified diagnostic approximation. Check dimensions and direction conventions before calculating; atmospheric fields may be spatially varying even when one chart appears constant.


### What observations could distinguish mechanisms?

Analyze hourly coastal wind direction, inland temperature and urban/rural stations during synoptically calm and windy days. Identify the observation time, position, calibration information and observational resolution. Contrast **radiometer record**, **flux-footprint log** and **day–night turbulent profiles**. A strong experiment predicts one place, time or altitude where rival explanations differ. In particular, assess a poorly known top or lateral boundary; never use the same evidence both to tune a hypothesis and to claim its independent confirmation.


### Worked numerical case — Coastal pressure contrast

**Fictional data:** A sea-breeze gradient has 0.6 hPa pressure difference across 30 km; find Pa/m.

**Calculation:** `(0.6*100)/30000`. The numerical result is **0.002 Pa/m**. Explicitly verify its units and interpretation; the number is a conditional result from invented inputs, not a documented observation. **Sensitivity:** perturb the dominant uncertain input by 10% and report what changes. Thermal circulation depends on vertical structure, not one pressure gradient. Explain which excluded process might invalidate the simplified estimate.


### Limits, confounding and counterfactual reasoning

An urban–rural temperature contrast is affected by instrument siting and land-use mismatch, not just the urban heat island. Contrast an alternative mechanism and state an observation that could discriminate between them. A more complex fitted curve is not necessarily a better causal explanation. Record site elevation, weather regime and measurement support before transferring a conclusion to a new situation.


### Practical study investigation

Test a sea-breeze onset hypothesis against pressure tendency, dewpoint change and independent wind observations. Use `datasets/unit-02-synthetic.csv` for reproducible practice: plot the variable at native and aggregated sampling frequency; annotate potential instrument error and a rival hypothesis. Reserve some observations for an independent check. The synthetic values are not validated natural observations, and apparent agreement with an illustrative model is not forecast verification.


### Conceptual checks and problem set

1. Draw the physical process underlying **Sea breezes, mountain winds and urban heat**, then label the state variables, external forcing, fluxes and observational boundary. Which label is least well supported?
2. Reproduce the worked example with all unit conversions visible. Change one assumed value by 10%; report the new answer and interpret whether its sign or scale is plausible.
3. Explain how **an urban–rural temperature contrast is affected by instrument siting and land-use mismatch, not just the urban heat island.** Give one additional observable that would distinguish this issue from the core mechanism.
4. Translate the case into an observational protocol: station placement, sample frequency, calibration information, data exclusion rules and one independent validation source.
5. Explain why **test a sea-breeze onset hypothesis against pressure tendency, dewpoint change and independent wind observations.** might lead to a misleading conclusion if the sample were sparse or the relevant atmospheric state changed between observations.

**Answer expectations:** A competent response states the physical assumption, uses correctly dimensioned quantities, provides an interpretation in the context of the mechanism, reports an alternative explanation, and explicitly distinguishes fictional numerical inputs from observed meteorological evidence. Answers that assert a deterministic local forecast from these toy equations are not scientifically justified.


## Unit 2 capstone — A reproducible atmospheric argument

Start from the research question **How do energy fluxes between radiation, ground and turbulent air shape near-surface weather?**. Create an evidence map that distinguishes the three sources **radiometer record**, **flux-footprint log** and **day–night turbulent profiles**. The first source should establish the main physical state, the second should show whether the proposed forcing was present, and the third should offer a genuinely independent check. For the synthetic scenario, state a primary hypothesis and an alternative that differs in mechanism rather than merely in parameter size. Specify what both would predict at the same station but at different heights or times. In your technical report, use no unexplained uncertainty bars; distinguish calibration limits, observation support, model approximation, initialization errors, and uncertainty about the process itself.

**Data and reproducibility task:** Read the 30 synthetic records for this unit. Convert the ISO timestamps into a time axis, compute a descriptive mean and a robust range, and repeat the analysis after removing every fifth observation. If the trend changes materially, explain whether the underlying signal might be under-sampled. Prepare a plain-language summary of what the dataset can and cannot support. Supply enough detail that another student can reproduce every calculation without contacting the author. Separate radiation, thermal inertia, anthropogenic heating, moisture and advection before assigning a cause.

**Critical discussion:** Suppose an institution must make a decision from the available analysis. Identify the evidence that is missing, the consequence of a false alarm versus a missed event, and the observation that would most efficiently reduce consequential uncertainty. Provide a direct recommendation only when the dataset and problem definition warrant one. Never treat synthetic meteorological examples as an operational alert or regulatory threshold.

## Key takeaways for Unit 2

- The subject is an atmospheric system, not just an isolated plotted correlation; a defensible explanation must respect fundamental balances.
- The measurement domain, spatial scale, averaging interval and uncertainty control what can be inferred.
- The worked formulas expose sensitivity and limiting assumptions, not an automatic prediction for an unobserved site.
- A scientifically meaningful alternative hypothesis requires an observation that could falsify it.
- Operational warnings require responsible meteorological services and independently validated evidence.
