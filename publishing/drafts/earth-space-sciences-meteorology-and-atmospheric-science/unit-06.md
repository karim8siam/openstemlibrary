# Unit 6 — Convection, severe weather and tropical systems
## The central atmospheric investigation

**Question:** Which ingredients create organized deep convection, tropical cyclones and rainfall extremes?

**Case setting:** A humid coastal district faces both afternoon thunderstorms and an approaching tropical disturbance. All locations and observations in the following investigation are synthetic. The purpose is to learn which inference would survive contact with independent measurements, rather than to produce a plausible-sounding story from an incomplete weather map.

Cumulonimbus clouds result when moist parcels are lifted enough to reach favorable buoyancy, with adequate moisture and a depth of support for vertical development. CAPE is a parcel integral and does not directly measure observed updraft speed. CIN can delay initiation; lift and surface heating may reduce the barrier, and entrainment may weaken the updraft. Shear helps determine whether precipitation falls into the updraft or whether new cells propagate along a boundary.

Storm hazards are not interchangeable. Lightning poses risk before the heaviest rain arrives; wet microbursts can produce violent outflow without classic tornado-like radar patterns; hail depends on microphysical growth and convective residence time. Tropical cyclones use organized surface heat and moisture fluxes under a rotating circulation, but sea-surface temperature alone is insufficient to predict intensification. Moisture convergence and storm training produce precipitation extremes that lead to flooding only in the context of catchment storage, land use and exposure.

### Working boundaries and research assumptions

The effective observational transect for this unit runs from **the inflow sector into the storm updraft**. Different forms of evidence support different kinds of inference: storm sounding constrains one aspect, radar loop another, and surface gust/rain record a third. These are not interchangeable. A flux through a boundary is different from a store inside a region; a spatial gradient is not a material change through time; a measured scalar does not determine a complete three-dimensional vector. Choose a control volume or moving parcel explicitly before writing the governing relationship. Record the averaging period and the geographical support used in comparisons.

Illustrative calculations in this unit cannot be used as operational severe-weather warnings. Use current alerts from the responsible meteorological service for actual risk decisions. A scientifically responsible capstone separates observed rainfall, forecast intensity, local flood susceptibility and the social response to a warning.

### What success looks like

A strong unit report reconstructs a physical chain from forcing to response while maintaining the distinction between an observation, a calculation, a model hypothesis and a decision. Include a figure that cannot be understood without axis units, a written alternative explanation and a comparison with a second type of evidence. Distinguish environmental ingredients from prediction of specific damaging impacts.


## Lesson 6.1 — Convective instability and CAPE/CIN

### The physical question

CAPE integrates positive parcel buoyancy over the free-convection layer; convective inhibition measures a barrier to triggering. Moisture, lifting, wind shear and entrainment determine whether potential energy supports organized storms. For the synthetic case, distinguish state, flux, tendency and any empirical relationship. When air moves past a fixed sensor, an observed change does not by itself establish a local transformation. Record the vertical level and sampling interval.


### From fundamental laws to an operational approximation

Begin by drawing **the inflow sector into the storm updraft** and labeling **storm-relative wind and moist static energy**. State a relevant physical conservation law, and distinguish that law from its simplified diagnostic approximation. Check dimensions and direction conventions before calculating; atmospheric fields may be spatially varying even when one chart appears constant.


### What observations could distinguish mechanisms?

Compare morning and afternoon soundings and observed cell initiation near a boundary in the same environment. Identify the observation time, position, calibration information and observational resolution. Contrast **storm sounding**, **radar loop** and **surface gust/rain record**. A strong experiment predicts one place, time or altitude where rival explanations differ. In particular, assess mixing between air masses; never use the same evidence both to tune a hypothesis and to claim its independent confirmation.


### Worked numerical case — CAPE upper-bound updraft speed

**Fictional data:** Under ideal no-loss assumptions, CAPE=1500 J/kg; find sqrt(2 CAPE).

**Calculation:** `math.sqrt(2*1500)`. The numerical result is **54.77 m/s**. Explicitly verify its units and interpretation; the number is a conditional result from invented inputs, not a documented observation. **Sensitivity:** perturb the dominant uncertain input by 10% and report what changes. Not a guaranteed measured vertical velocity. Explain which excluded process might invalidate the simplified estimate.


### Limits, confounding and counterfactual reasoning

Large CAPE alone neither guarantees thunderstorms nor indicates a specified severity; vertical shear and storm initiation matter. Contrast an alternative mechanism and state an observation that could discriminate between them. A more complex fitted curve is not necessarily a better causal explanation. Record site elevation, weather regime and measurement support before transferring a conclusion to a new situation.


### Practical study investigation

Calculate an ideal upper-bound parcel speed and explain why actual updrafts are smaller. Use `datasets/unit-06-synthetic.csv` for reproducible practice: plot the variable at native and aggregated sampling frequency; annotate potential instrument error and a rival hypothesis. Reserve some observations for an independent check. The synthetic values are not validated natural observations, and apparent agreement with an illustrative model is not forecast verification.


### Conceptual checks and problem set

1. Draw the physical process underlying **Convective instability and CAPE/CIN**, then label the state variables, external forcing, fluxes and observational boundary. Which label is least well supported?
2. Reproduce the worked example with all unit conversions visible. Change one assumed value by 10%; report the new answer and interpret whether its sign or scale is plausible.
3. Explain how **large CAPE alone neither guarantees thunderstorms nor indicates a specified severity; vertical shear and storm initiation matter.** Give one additional observable that would distinguish this issue from the core mechanism.
4. Translate the case into an observational protocol: station placement, sample frequency, calibration information, data exclusion rules and one independent validation source.
5. Explain why **calculate an ideal upper-bound parcel speed and explain why actual updrafts are smaller.** might lead to a misleading conclusion if the sample were sparse or the relevant atmospheric state changed between observations.

**Answer expectations:** A competent response states the physical assumption, uses correctly dimensioned quantities, provides an interpretation in the context of the mechanism, reports an alternative explanation, and explicitly distinguishes fictional numerical inputs from observed meteorological evidence. Answers that assert a deterministic local forecast from these toy equations are not scientifically justified.


## Lesson 6.2 — Thunderstorm organization and shear

### The physical question

Vertical wind shear can tilt and separate updrafts from downdrafts, prolonging convection. Ordinary pulse storms, multicells, squall lines and supercells differ in storm-relative flow and rotation structures. For the synthetic case, distinguish state, flux, tendency and any empirical relationship. When air moves past a fixed sensor, an observed change does not by itself establish a local transformation. Record the vertical level and sampling interval.


### From fundamental laws to an operational approximation

Begin by drawing **the inflow sector into the storm updraft** and labeling **storm-relative wind and moist static energy**. State a relevant physical conservation law, and distinguish that law from its simplified diagnostic approximation. Check dimensions and direction conventions before calculating; atmospheric fields may be spatially varying even when one chart appears constant.


### What observations could distinguish mechanisms?

Use Doppler radial-velocity patterns and successive radar scans to compare a short-lived pulse cell with a persistent line. Identify the observation time, position, calibration information and observational resolution. Contrast **storm sounding**, **radar loop** and **surface gust/rain record**. A strong experiment predicts one place, time or altitude where rival explanations differ. In particular, assess a measurement artifact mistaken for a physical anomaly; never use the same evidence both to tune a hypothesis and to claim its independent confirmation.


### Worked numerical case — Bulk wind shear

**Fictional data:** Wind speed difference across a chosen layer is 22 m/s over 6 km; average magnitude gradient.

**Calculation:** `22/6`. The numerical result is **3.667 (m/s)/km**. Explicitly verify its units and interpretation; the number is a conditional result from invented inputs, not a documented observation. **Sensitivity:** perturb the dominant uncertain input by 10% and report what changes. Vector subtraction is required for real directional shear. Explain which excluded process might invalidate the simplified estimate.


### Limits, confounding and counterfactual reasoning

A radar-indicated velocity couplet requires scrutiny for aliasing, range effects and whether rotation is sustained. Contrast an alternative mechanism and state an observation that could discriminate between them. A more complex fitted curve is not necessarily a better causal explanation. Record site elevation, weather regime and measurement support before transferring a conclusion to a new situation.


### Practical study investigation

Sketch updraft–downdraft separation for weak and strong deep-layer shear cases. Use `datasets/unit-06-synthetic.csv` for reproducible practice: plot the variable at native and aggregated sampling frequency; annotate potential instrument error and a rival hypothesis. Reserve some observations for an independent check. The synthetic values are not validated natural observations, and apparent agreement with an illustrative model is not forecast verification.


### Conceptual checks and problem set

1. Draw the physical process underlying **Thunderstorm organization and shear**, then label the state variables, external forcing, fluxes and observational boundary. Which label is least well supported?
2. Reproduce the worked example with all unit conversions visible. Change one assumed value by 10%; report the new answer and interpret whether its sign or scale is plausible.
3. Explain how **a radar-indicated velocity couplet requires scrutiny for aliasing, range effects and whether rotation is sustained.** Give one additional observable that would distinguish this issue from the core mechanism.
4. Translate the case into an observational protocol: station placement, sample frequency, calibration information, data exclusion rules and one independent validation source.
5. Explain why **sketch updraft–downdraft separation for weak and strong deep-layer shear cases.** might lead to a misleading conclusion if the sample were sparse or the relevant atmospheric state changed between observations.

**Answer expectations:** A competent response states the physical assumption, uses correctly dimensioned quantities, provides an interpretation in the context of the mechanism, reports an alternative explanation, and explicitly distinguishes fictional numerical inputs from observed meteorological evidence. Answers that assert a deterministic local forecast from these toy equations are not scientifically justified.


## Lesson 6.3 — Microbursts, hail and lightning

### The physical question

Evaporative cooling and precipitation loading can accelerate downdrafts; hailstones grow through mixed-phase interactions in strong updrafts. Electrification occurs through collisions of particles in mixed-phase regions and produces hazardous lightning. For the synthetic case, distinguish state, flux, tendency and any empirical relationship. When air moves past a fixed sensor, an observed change does not by itself establish a local transformation. Record the vertical level and sampling interval.


### From fundamental laws to an operational approximation

Begin by drawing **the inflow sector into the storm updraft** and labeling **storm-relative wind and moist static energy**. State a relevant physical conservation law, and distinguish that law from its simplified diagnostic approximation. Check dimensions and direction conventions before calculating; atmospheric fields may be spatially varying even when one chart appears constant.


### What observations could distinguish mechanisms?

Examine surface gust spikes, sharp temperature drops and dual-polarization hydrometeor classifications during a convective event. Identify the observation time, position, calibration information and observational resolution. Contrast **storm sounding**, **radar loop** and **surface gust/rain record**. A strong experiment predicts one place, time or altitude where rival explanations differ. In particular, assess a poorly known top or lateral boundary; never use the same evidence both to tune a hypothesis and to claim its independent confirmation.


### Worked numerical case — Downburst outflow travel

**Fictional data:** Cold-pool leading edge travels 9 km in 12 minutes; mean speed?

**Calculation:** `9000/(12*60)`. The numerical result is **12.5 m/s**. Explicitly verify its units and interpretation; the number is a conditional result from invented inputs, not a documented observation. **Sensitivity:** perturb the dominant uncertain input by 10% and report what changes. Damage and gust magnitude cannot be inferred from translation alone. Explain which excluded process might invalidate the simplified estimate.


### Limits, confounding and counterfactual reasoning

Surface gust reports are sparse; a damaging gust cannot be inferred from rain intensity alone. Contrast an alternative mechanism and state an observation that could discriminate between them. A more complex fitted curve is not necessarily a better causal explanation. Record site elevation, weather regime and measurement support before transferring a conclusion to a new situation.


### Practical study investigation

Specify independent signatures of a downburst and explain why lightning risk extends beyond visible heavy rain. Use `datasets/unit-06-synthetic.csv` for reproducible practice: plot the variable at native and aggregated sampling frequency; annotate potential instrument error and a rival hypothesis. Reserve some observations for an independent check. The synthetic values are not validated natural observations, and apparent agreement with an illustrative model is not forecast verification.


### Conceptual checks and problem set

1. Draw the physical process underlying **Microbursts, hail and lightning**, then label the state variables, external forcing, fluxes and observational boundary. Which label is least well supported?
2. Reproduce the worked example with all unit conversions visible. Change one assumed value by 10%; report the new answer and interpret whether its sign or scale is plausible.
3. Explain how **surface gust reports are sparse; a damaging gust cannot be inferred from rain intensity alone.** Give one additional observable that would distinguish this issue from the core mechanism.
4. Translate the case into an observational protocol: station placement, sample frequency, calibration information, data exclusion rules and one independent validation source.
5. Explain why **specify independent signatures of a downburst and explain why lightning risk extends beyond visible heavy rain.** might lead to a misleading conclusion if the sample were sparse or the relevant atmospheric state changed between observations.

**Answer expectations:** A competent response states the physical assumption, uses correctly dimensioned quantities, provides an interpretation in the context of the mechanism, reports an alternative explanation, and explicitly distinguishes fictional numerical inputs from observed meteorological evidence. Answers that assert a deterministic local forecast from these toy equations are not scientifically justified.


## Lesson 6.4 — Tropical cyclone thermodynamics and dynamics

### The physical question

Tropical cyclones require sustained deep convection, organized rotation, surface energy fluxes and favorable environmental conditions. Warm ocean water is helpful but insufficient without moisture, weak disruptive shear and a preexisting disturbance. For the synthetic case, distinguish state, flux, tendency and any empirical relationship. When air moves past a fixed sensor, an observed change does not by itself establish a local transformation. Record the vertical level and sampling interval.


### From fundamental laws to an operational approximation

Begin by drawing **the inflow sector into the storm updraft** and labeling **storm-relative wind and moist static energy**. State a relevant physical conservation law, and distinguish that law from its simplified diagnostic approximation. Check dimensions and direction conventions before calculating; atmospheric fields may be spatially varying even when one chart appears constant.


### What observations could distinguish mechanisms?

Compare ocean heat content, satellite cloud symmetry, upper-level outflow and surface pressure during observed intensification. Identify the observation time, position, calibration information and observational resolution. Contrast **storm sounding**, **radar loop** and **surface gust/rain record**. A strong experiment predicts one place, time or altitude where rival explanations differ. In particular, assess an unsupported assumption of local equilibrium; never use the same evidence both to tune a hypothesis and to claim its independent confirmation.


### Worked numerical case — Tropical pressure deficit

**Fictional data:** Environmental sea-level pressure 1010 hPa and storm center 955 hPa; difference?

**Calculation:** `1010-955`. The numerical result is **55 hPa**. Explicitly verify its units and interpretation; the number is a conditional result from invented inputs, not a documented observation. **Sensitivity:** perturb the dominant uncertain input by 10% and report what changes. Pressure deficit alone is not a complete intensity or surge forecast. Explain which excluded process might invalidate the simplified estimate.


### Limits, confounding and counterfactual reasoning

Sea-surface temperature alone cannot determine intensity, and storm-surge risk depends on coastal geometry and bathymetry. Contrast an alternative mechanism and state an observation that could discriminate between them. A more complex fitted curve is not necessarily a better causal explanation. Record site elevation, weather regime and measurement support before transferring a conclusion to a new situation.


### Practical study investigation

Use a set of scenarios to explain how dry-air entrainment or shear can disrupt otherwise favorable oceanic conditions. Use `datasets/unit-06-synthetic.csv` for reproducible practice: plot the variable at native and aggregated sampling frequency; annotate potential instrument error and a rival hypothesis. Reserve some observations for an independent check. The synthetic values are not validated natural observations, and apparent agreement with an illustrative model is not forecast verification.


### Conceptual checks and problem set

1. Draw the physical process underlying **Tropical cyclone thermodynamics and dynamics**, then label the state variables, external forcing, fluxes and observational boundary. Which label is least well supported?
2. Reproduce the worked example with all unit conversions visible. Change one assumed value by 10%; report the new answer and interpret whether its sign or scale is plausible.
3. Explain how **sea-surface temperature alone cannot determine intensity, and storm-surge risk depends on coastal geometry and bathymetry.** Give one additional observable that would distinguish this issue from the core mechanism.
4. Translate the case into an observational protocol: station placement, sample frequency, calibration information, data exclusion rules and one independent validation source.
5. Explain why **use a set of scenarios to explain how dry-air entrainment or shear can disrupt otherwise favorable oceanic conditions.** might lead to a misleading conclusion if the sample were sparse or the relevant atmospheric state changed between observations.

**Answer expectations:** A competent response states the physical assumption, uses correctly dimensioned quantities, provides an interpretation in the context of the mechanism, reports an alternative explanation, and explicitly distinguishes fictional numerical inputs from observed meteorological evidence. Answers that assert a deterministic local forecast from these toy equations are not scientifically justified.


## Lesson 6.5 — Monsoon rainfall and flood-producing extremes

### The physical question

Intense rainfall can result from moisture convergence, repeated convection and slow storm motion. Terrain and soil saturation convert meteorological precipitation into different hydrological impacts across catchments. For the synthetic case, distinguish state, flux, tendency and any empirical relationship. When air moves past a fixed sensor, an observed change does not by itself establish a local transformation. Record the vertical level and sampling interval.


### From fundamental laws to an operational approximation

Begin by drawing **the inflow sector into the storm updraft** and labeling **storm-relative wind and moist static energy**. State a relevant physical conservation law, and distinguish that law from its simplified diagnostic approximation. Check dimensions and direction conventions before calculating; atmospheric fields may be spatially varying even when one chart appears constant.


### What observations could distinguish mechanisms?

Construct a rain-gauge/radar accumulation map, align with river hydrographs, and separate extreme rain location from flood exposure. Identify the observation time, position, calibration information and observational resolution. Contrast **storm sounding**, **radar loop** and **surface gust/rain record**. A strong experiment predicts one place, time or altitude where rival explanations differ. In particular, assess mixing between air masses; never use the same evidence both to tune a hypothesis and to claim its independent confirmation.


### Worked numerical case — Accumulated intense rain

**Fictional data:** Assume a constant 48 mm/h rain rate sustained for 2.5 h.

**Calculation:** `48*2.5`. The numerical result is **120 mm**. Explicitly verify its units and interpretation; the number is a conditional result from invented inputs, not a documented observation. **Sensitivity:** perturb the dominant uncertain input by 10% and report what changes. Intense storms rarely hold constant rate over a broad region. Explain which excluded process might invalidate the simplified estimate.


### Limits, confounding and counterfactual reasoning

Radar bright band, attenuation and gauge undercatch can distort intensity estimates, especially across mountains. Contrast an alternative mechanism and state an observation that could discriminate between them. A more complex fitted curve is not necessarily a better causal explanation. Record site elevation, weather regime and measurement support before transferring a conclusion to a new situation.


### Practical study investigation

Communicate a scenario range for accumulation without asserting a deterministic village-scale flood forecast. Use `datasets/unit-06-synthetic.csv` for reproducible practice: plot the variable at native and aggregated sampling frequency; annotate potential instrument error and a rival hypothesis. Reserve some observations for an independent check. The synthetic values are not validated natural observations, and apparent agreement with an illustrative model is not forecast verification.


### Conceptual checks and problem set

1. Draw the physical process underlying **Monsoon rainfall and flood-producing extremes**, then label the state variables, external forcing, fluxes and observational boundary. Which label is least well supported?
2. Reproduce the worked example with all unit conversions visible. Change one assumed value by 10%; report the new answer and interpret whether its sign or scale is plausible.
3. Explain how **radar bright band, attenuation and gauge undercatch can distort intensity estimates, especially across mountains.** Give one additional observable that would distinguish this issue from the core mechanism.
4. Translate the case into an observational protocol: station placement, sample frequency, calibration information, data exclusion rules and one independent validation source.
5. Explain why **communicate a scenario range for accumulation without asserting a deterministic village-scale flood forecast.** might lead to a misleading conclusion if the sample were sparse or the relevant atmospheric state changed between observations.

**Answer expectations:** A competent response states the physical assumption, uses correctly dimensioned quantities, provides an interpretation in the context of the mechanism, reports an alternative explanation, and explicitly distinguishes fictional numerical inputs from observed meteorological evidence. Answers that assert a deterministic local forecast from these toy equations are not scientifically justified.


## Unit 6 capstone — A reproducible atmospheric argument

Start from the research question **Which ingredients create organized deep convection, tropical cyclones and rainfall extremes?**. Create an evidence map that distinguishes the three sources **storm sounding**, **radar loop** and **surface gust/rain record**. The first source should establish the main physical state, the second should show whether the proposed forcing was present, and the third should offer a genuinely independent check. For the synthetic scenario, state a primary hypothesis and an alternative that differs in mechanism rather than merely in parameter size. Specify what both would predict at the same station but at different heights or times. In your technical report, use no unexplained uncertainty bars; distinguish calibration limits, observation support, model approximation, initialization errors, and uncertainty about the process itself.

**Data and reproducibility task:** Read the 30 synthetic records for this unit. Convert the ISO timestamps into a time axis, compute a descriptive mean and a robust range, and repeat the analysis after removing every fifth observation. If the trend changes materially, explain whether the underlying signal might be under-sampled. Prepare a plain-language summary of what the dataset can and cannot support. Supply enough detail that another student can reproduce every calculation without contacting the author. Distinguish environmental ingredients from prediction of specific damaging impacts.

**Critical discussion:** Suppose an institution must make a decision from the available analysis. Identify the evidence that is missing, the consequence of a false alarm versus a missed event, and the observation that would most efficiently reduce consequential uncertainty. Provide a direct recommendation only when the dataset and problem definition warrant one. Never treat synthetic meteorological examples as an operational alert or regulatory threshold.

## Key takeaways for Unit 6

- The subject is an atmospheric system, not just an isolated plotted correlation; a defensible explanation must respect fundamental balances.
- The measurement domain, spatial scale, averaging interval and uncertainty control what can be inferred.
- The worked formulas expose sensitivity and limiting assumptions, not an automatic prediction for an unobserved site.
- A scientifically meaningful alternative hypothesis requires an observation that could falsify it.
- Operational warnings require responsible meteorological services and independently validated evidence.
