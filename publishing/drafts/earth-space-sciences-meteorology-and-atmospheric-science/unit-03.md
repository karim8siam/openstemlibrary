# Unit 3 — Humidity, clouds and precipitation
## The central atmospheric investigation

**Question:** How does water vapor become droplets, ice, cloud layers and measurable precipitation?

**Case setting:** Two air masses have the same surface temperature yet only one produces heavy stratiform rain. All locations and observations in the following investigation are synthetic. The purpose is to learn which inference would survive contact with independent measurements, rather than to produce a plausible-sounding story from an incomplete weather map.

Water vapor carries latent energy and sets conditions for cloud condensation. Relative humidity is a thermodynamic ratio evaluated at a given temperature; it is not an independent measure of total atmospheric water. Dewpoint and mixing ratio complement relative humidity, and pressure matters when transforming between them. Air lifted toward saturation may form a cloud base, but an extended cloud deck is shaped by mixing, large-scale vertical motion and local radiative exchange.

Small cloud droplets rarely become heavy raindrops by condensation alone. Warm-cloud collision and coalescence, ice growth by vapor deposition, riming and aggregation provide growth pathways. Radar reflectivity responds strongly to particle size and also changes with phase, shape and melting. The bright band associated with melting snow can mimic an intense rainfall maximum, so a reliable rainfall estimate combines radar with gauges and microphysical information. Orographic forcing redistributes cloud and rain where flow crosses terrain, but strong upslope motion can coexist with a dry lower atmosphere if upstream water vapor is insufficient.

### Working boundaries and research assumptions

The effective observational transect for this unit runs from **unsaturated subcloud air through cloud top**. Different forms of evidence support different kinds of inference: temperature/dewpoint pair constrains one aspect, cloud-base estimate another, and precipitation observation a third. These are not interchangeable. A flux through a boundary is different from a store inside a region; a spatial gradient is not a material change through time; a measured scalar does not determine a complete three-dimensional vector. Choose a control volume or moving parcel explicitly before writing the governing relationship. Record the averaging period and the geographical support used in comparisons.

Use the unit dataset to distinguish water-vapor availability from the dynamical lifting mechanism. Ask whether a cloud observed from satellite is precipitating at the surface. No exercise should treat one aerosol measurement, one radar pixel or a one-hour rain record as proof of an entire precipitation mechanism.

### What success looks like

A strong unit report reconstructs a physical chain from forcing to response while maintaining the distinction between an observation, a calculation, a model hypothesis and a decision. Include a figure that cannot be understood without axis units, a written alternative explanation and a comparison with a second type of evidence. Use soundings, condensation nuclei, ascent and phase microphysics to explain the difference.


## Lesson 3.1 — Vapor pressure and relative humidity

### The physical question

Relative humidity is e/es(T) expressed as a percentage; because saturation vapor pressure rises strongly with temperature, relative humidity may fall during warming at constant moisture content. Dewpoint relates to vapor pressure and better indicates moisture amount. For the synthetic case, distinguish state, flux, tendency and any empirical relationship. When air moves past a fixed sensor, an observed change does not by itself establish a local transformation. Record the vertical level and sampling interval.


### From fundamental laws to an operational approximation

Begin by drawing **unsaturated subcloud air through cloud top** and labeling **moisture, condensate and mass flux**. State a relevant physical conservation law, and distinguish that law from its simplified diagnostic approximation. Check dimensions and direction conventions before calculating; atmospheric fields may be spatially varying even when one chart appears constant.


### What observations could distinguish mechanisms?

Contrast morning and afternoon air at the same station using temperature, dewpoint and RH; compute actual vapor pressure for each interval. Identify the observation time, position, calibration information and observational resolution. Contrast **temperature/dewpoint pair**, **cloud-base estimate** and **precipitation observation**. A strong experiment predicts one place, time or altitude where rival explanations differ. In particular, assess instrument response to an abrupt transition; never use the same evidence both to tune a hypothesis and to claim its independent confirmation.


### Worked numerical case — Relative humidity

**Fictional data:** Vapor pressure e=16 hPa and saturation es=20 hPa; find RH.

**Calculation:** `100*16/20`. The numerical result is **80 %**. Explicitly verify its units and interpretation; the number is a conditional result from invented inputs, not a documented observation. **Sensitivity:** perturb the dominant uncertain input by 10% and report what changes. Relative humidity is strongly temperature-sensitive. Explain which excluded process might invalidate the simplified estimate.


### Limits, confounding and counterfactual reasoning

Relative humidity alone does not measure the absolute mass of vapor, and sensors can be biased near saturation or icing conditions. Contrast an alternative mechanism and state an observation that could discriminate between them. A more complex fitted curve is not necessarily a better causal explanation. Record site elevation, weather regime and measurement support before transferring a conclusion to a new situation.


### Practical study investigation

Explain a falling RH with unchanged dewpoint, then identify an observation that would imply actual drying. Use `datasets/unit-03-synthetic.csv` for reproducible practice: plot the variable at native and aggregated sampling frequency; annotate potential instrument error and a rival hypothesis. Reserve some observations for an independent check. The synthetic values are not validated natural observations, and apparent agreement with an illustrative model is not forecast verification.


### Conceptual checks and problem set

1. Draw the physical process underlying **Vapor pressure and relative humidity**, then label the state variables, external forcing, fluxes and observational boundary. Which label is least well supported?
2. Reproduce the worked example with all unit conversions visible. Change one assumed value by 10%; report the new answer and interpret whether its sign or scale is plausible.
3. Explain how **relative humidity alone does not measure the absolute mass of vapor, and sensors can be biased near saturation or icing conditions.** Give one additional observable that would distinguish this issue from the core mechanism.
4. Translate the case into an observational protocol: station placement, sample frequency, calibration information, data exclusion rules and one independent validation source.
5. Explain why **explain a falling RH with unchanged dewpoint, then identify an observation that would imply actual drying.** might lead to a misleading conclusion if the sample were sparse or the relevant atmospheric state changed between observations.

**Answer expectations:** A competent response states the physical assumption, uses correctly dimensioned quantities, provides an interpretation in the context of the mechanism, reports an alternative explanation, and explicitly distinguishes fictional numerical inputs from observed meteorological evidence. Answers that assert a deterministic local forecast from these toy equations are not scientifically justified.


## Lesson 3.2 — Moist adiabatic ascent and cloud bases

### The physical question

Unsaturated rising parcels cool toward the lifting condensation level where saturation is approached. Further ascent releases latent heat, reducing the magnitude of the saturated lapse rate, which varies with pressure and temperature. For the synthetic case, distinguish state, flux, tendency and any empirical relationship. When air moves past a fixed sensor, an observed change does not by itself establish a local transformation. Record the vertical level and sampling interval.


### From fundamental laws to an operational approximation

Begin by drawing **unsaturated subcloud air through cloud top** and labeling **moisture, condensate and mass flux**. State a relevant physical conservation law, and distinguish that law from its simplified diagnostic approximation. Check dimensions and direction conventions before calculating; atmospheric fields may be spatially varying even when one chart appears constant.


### What observations could distinguish mechanisms?

Overlay parcel and environmental thermodynamic paths on a sounding and compare estimated cloud base with ceilometer reports. Identify the observation time, position, calibration information and observational resolution. Contrast **temperature/dewpoint pair**, **cloud-base estimate** and **precipitation observation**. A strong experiment predicts one place, time or altitude where rival explanations differ. In particular, assess spatial interpolation across sparse stations; never use the same evidence both to tune a hypothesis and to claim its independent confirmation.


### Worked numerical case — Approximate lifting condensation level

**Fictional data:** Air temperature 29°C and dewpoint 23°C; LCL approximately 125(T−Td) meters.

**Calculation:** `125*(29-23)`. The numerical result is **750 m AGL**. Explicitly verify its units and interpretation; the number is a conditional result from invented inputs, not a documented observation. **Sensitivity:** perturb the dominant uncertain input by 10% and report what changes. Approximation applies to idealized surface-parcel conditions. Explain which excluded process might invalidate the simplified estimate.


### Limits, confounding and counterfactual reasoning

The common 125 m per degree Celsius cloud-base approximation is not a forecast for layered clouds or terrain-forced fog. Contrast an alternative mechanism and state an observation that could discriminate between them. A more complex fitted curve is not necessarily a better causal explanation. Record site elevation, weather regime and measurement support before transferring a conclusion to a new situation.


### Practical study investigation

Estimate an idealized LCL and articulate how entrainment and mixing change the real cloud base. Use `datasets/unit-03-synthetic.csv` for reproducible practice: plot the variable at native and aggregated sampling frequency; annotate potential instrument error and a rival hypothesis. Reserve some observations for an independent check. The synthetic values are not validated natural observations, and apparent agreement with an illustrative model is not forecast verification.


### Conceptual checks and problem set

1. Draw the physical process underlying **Moist adiabatic ascent and cloud bases**, then label the state variables, external forcing, fluxes and observational boundary. Which label is least well supported?
2. Reproduce the worked example with all unit conversions visible. Change one assumed value by 10%; report the new answer and interpret whether its sign or scale is plausible.
3. Explain how **the common 125 m per degree Celsius cloud-base approximation is not a forecast for layered clouds or terrain-forced fog.** Give one additional observable that would distinguish this issue from the core mechanism.
4. Translate the case into an observational protocol: station placement, sample frequency, calibration information, data exclusion rules and one independent validation source.
5. Explain why **estimate an idealized LCL and articulate how entrainment and mixing change the real cloud base.** might lead to a misleading conclusion if the sample were sparse or the relevant atmospheric state changed between observations.

**Answer expectations:** A competent response states the physical assumption, uses correctly dimensioned quantities, provides an interpretation in the context of the mechanism, reports an alternative explanation, and explicitly distinguishes fictional numerical inputs from observed meteorological evidence. Answers that assert a deterministic local forecast from these toy equations are not scientifically justified.


## Lesson 3.3 — Cloud droplets, aerosols and activation

### The physical question

Cloud condensation nuclei provide surfaces enabling activation at achievable supersaturations. The size distribution of particles matters because condensation alone often grows droplets too slowly to create heavy rain. For the synthetic case, distinguish state, flux, tendency and any empirical relationship. When air moves past a fixed sensor, an observed change does not by itself establish a local transformation. Record the vertical level and sampling interval.


### From fundamental laws to an operational approximation

Begin by drawing **unsaturated subcloud air through cloud top** and labeling **moisture, condensate and mass flux**. State a relevant physical conservation law, and distinguish that law from its simplified diagnostic approximation. Check dimensions and direction conventions before calculating; atmospheric fields may be spatially varying even when one chart appears constant.


### What observations could distinguish mechanisms?

Compare cloud droplet concentration from an optical counter with aerosol spectra for clean and polluted maritime air. Identify the observation time, position, calibration information and observational resolution. Contrast **temperature/dewpoint pair**, **cloud-base estimate** and **precipitation observation**. A strong experiment predicts one place, time or altitude where rival explanations differ. In particular, assess weather regime change during averaging; never use the same evidence both to tune a hypothesis and to claim its independent confirmation.


### Worked numerical case — Aerosol activation percentage

**Fictional data:** Of 800 measured aerosol particles per cm³, 120 activate in illustrative chamber conditions.

**Calculation:** `100*120/800`. The numerical result is **15 % activated**. Explicitly verify its units and interpretation; the number is a conditional result from invented inputs, not a documented observation. **Sensitivity:** perturb the dominant uncertain input by 10% and report what changes. An activation fraction at one supersaturation is not a cloud-wide constant. Explain which excluded process might invalidate the simplified estimate.


### Limits, confounding and counterfactual reasoning

More aerosols can increase droplet number but rain responses depend on liquid-water path, turbulence and environmental state. Contrast an alternative mechanism and state an observation that could discriminate between them. A more complex fitted curve is not necessarily a better causal explanation. Record site elevation, weather regime and measurement support before transferring a conclusion to a new situation.


### Practical study investigation

Sketch a conditional causal graph that separates aerosol abundance from meteorological covariates. Use `datasets/unit-03-synthetic.csv` for reproducible practice: plot the variable at native and aggregated sampling frequency; annotate potential instrument error and a rival hypothesis. Reserve some observations for an independent check. The synthetic values are not validated natural observations, and apparent agreement with an illustrative model is not forecast verification.


### Conceptual checks and problem set

1. Draw the physical process underlying **Cloud droplets, aerosols and activation**, then label the state variables, external forcing, fluxes and observational boundary. Which label is least well supported?
2. Reproduce the worked example with all unit conversions visible. Change one assumed value by 10%; report the new answer and interpret whether its sign or scale is plausible.
3. Explain how **more aerosols can increase droplet number but rain responses depend on liquid-water path, turbulence and environmental state.** Give one additional observable that would distinguish this issue from the core mechanism.
4. Translate the case into an observational protocol: station placement, sample frequency, calibration information, data exclusion rules and one independent validation source.
5. Explain why **sketch a conditional causal graph that separates aerosol abundance from meteorological covariates.** might lead to a misleading conclusion if the sample were sparse or the relevant atmospheric state changed between observations.

**Answer expectations:** A competent response states the physical assumption, uses correctly dimensioned quantities, provides an interpretation in the context of the mechanism, reports an alternative explanation, and explicitly distinguishes fictional numerical inputs from observed meteorological evidence. Answers that assert a deterministic local forecast from these toy equations are not scientifically justified.


## Lesson 3.4 — Ice microphysics and precipitation growth

### The physical question

Mixed-phase clouds grow ice via vapor deposition, riming and aggregation, while warm rain develops through collision and coalescence. Snow crystals, graupel and hail represent distinct growth histories, not merely categories of temperature. For the synthetic case, distinguish state, flux, tendency and any empirical relationship. When air moves past a fixed sensor, an observed change does not by itself establish a local transformation. Record the vertical level and sampling interval.


### From fundamental laws to an operational approximation

Begin by drawing **unsaturated subcloud air through cloud top** and labeling **moisture, condensate and mass flux**. State a relevant physical conservation law, and distinguish that law from its simplified diagnostic approximation. Check dimensions and direction conventions before calculating; atmospheric fields may be spatially varying even when one chart appears constant.


### What observations could distinguish mechanisms?

Interpret dual-polarization radar signatures and surface hydrometeor reports in a winter storm with a melting layer. Identify the observation time, position, calibration information and observational resolution. Contrast **temperature/dewpoint pair**, **cloud-base estimate** and **precipitation observation**. A strong experiment predicts one place, time or altitude where rival explanations differ. In particular, assess changes in observation height; never use the same evidence both to tune a hypothesis and to claim its independent confirmation.


### Worked numerical case — Radar Z–R warm-rain estimate

**Fictional data:** Assume Z=200R^1.6 and measured Z=3200 mm⁶ m−3; estimate R.

**Calculation:** `(3200/200)**(1/1.6)`. The numerical result is **5.657 mm/h**. Explicitly verify its units and interpretation; the number is a conditional result from invented inputs, not a documented observation. **Sensitivity:** perturb the dominant uncertain input by 10% and report what changes. Relationship coefficients vary with drop-size distributions and precipitation type. Explain which excluded process might invalidate the simplified estimate.


### Limits, confounding and counterfactual reasoning

Radar reflectivity does not uniquely specify precipitation rate because particle shape, density and phase alter scattering. Contrast an alternative mechanism and state an observation that could discriminate between them. A more complex fitted curve is not necessarily a better causal explanation. Record site elevation, weather regime and measurement support before transferring a conclusion to a new situation.


### Practical study investigation

Compare the expected observational signatures of bright band, hail core and warm-rain shower. Use `datasets/unit-03-synthetic.csv` for reproducible practice: plot the variable at native and aggregated sampling frequency; annotate potential instrument error and a rival hypothesis. Reserve some observations for an independent check. The synthetic values are not validated natural observations, and apparent agreement with an illustrative model is not forecast verification.


### Conceptual checks and problem set

1. Draw the physical process underlying **Ice microphysics and precipitation growth**, then label the state variables, external forcing, fluxes and observational boundary. Which label is least well supported?
2. Reproduce the worked example with all unit conversions visible. Change one assumed value by 10%; report the new answer and interpret whether its sign or scale is plausible.
3. Explain how **radar reflectivity does not uniquely specify precipitation rate because particle shape, density and phase alter scattering.** Give one additional observable that would distinguish this issue from the core mechanism.
4. Translate the case into an observational protocol: station placement, sample frequency, calibration information, data exclusion rules and one independent validation source.
5. Explain why **compare the expected observational signatures of bright band, hail core and warm-rain shower.** might lead to a misleading conclusion if the sample were sparse or the relevant atmospheric state changed between observations.

**Answer expectations:** A competent response states the physical assumption, uses correctly dimensioned quantities, provides an interpretation in the context of the mechanism, reports an alternative explanation, and explicitly distinguishes fictional numerical inputs from observed meteorological evidence. Answers that assert a deterministic local forecast from these toy equations are not scientifically justified.


## Lesson 3.5 — Fog, orographic clouds and precipitation efficiency

### The physical question

Radiation fog forms from near-surface cooling while advection fog involves air transported across a colder surface. Orographic ascent, seeder–feeder interactions and rain-shadow effects depend on flow, stability and humidity. For the synthetic case, distinguish state, flux, tendency and any empirical relationship. When air moves past a fixed sensor, an observed change does not by itself establish a local transformation. Record the vertical level and sampling interval.


### From fundamental laws to an operational approximation

Begin by drawing **unsaturated subcloud air through cloud top** and labeling **moisture, condensate and mass flux**. State a relevant physical conservation law, and distinguish that law from its simplified diagnostic approximation. Check dimensions and direction conventions before calculating; atmospheric fields may be spatially varying even when one chart appears constant.


### What observations could distinguish mechanisms?

Measure upslope wind, dewpoint depression and low-cloud observations at valley, crest and lee sites during a crossing storm. Identify the observation time, position, calibration information and observational resolution. Contrast **temperature/dewpoint pair**, **cloud-base estimate** and **precipitation observation**. A strong experiment predicts one place, time or altitude where rival explanations differ. In particular, assess instrument response to an abrupt transition; never use the same evidence both to tune a hypothesis and to claim its independent confirmation.


### Worked numerical case — Orographic ascent time

**Fictional data:** A moist airstream traverses a 12 km upslope at a horizontal speed of 6 m/s.

**Calculation:** `12000/6/60`. The numerical result is **33.33 minutes**. Explicitly verify its units and interpretation; the number is a conditional result from invented inputs, not a documented observation. **Sensitivity:** perturb the dominant uncertain input by 10% and report what changes. Not equivalent to cloud residence time because winds and paths vary with height. Explain which excluded process might invalidate the simplified estimate.


### Limits, confounding and counterfactual reasoning

A wet windward slope is not sufficient proof of an orographic mechanism unless upstream moisture and synoptic timing are controlled. Contrast an alternative mechanism and state an observation that could discriminate between them. A more complex fitted curve is not necessarily a better causal explanation. Record site elevation, weather regime and measurement support before transferring a conclusion to a new situation.


### Practical study investigation

Construct an altitudinal transect and predict how lifting condensation changes in a drier air mass. Use `datasets/unit-03-synthetic.csv` for reproducible practice: plot the variable at native and aggregated sampling frequency; annotate potential instrument error and a rival hypothesis. Reserve some observations for an independent check. The synthetic values are not validated natural observations, and apparent agreement with an illustrative model is not forecast verification.


### Conceptual checks and problem set

1. Draw the physical process underlying **Fog, orographic clouds and precipitation efficiency**, then label the state variables, external forcing, fluxes and observational boundary. Which label is least well supported?
2. Reproduce the worked example with all unit conversions visible. Change one assumed value by 10%; report the new answer and interpret whether its sign or scale is plausible.
3. Explain how **a wet windward slope is not sufficient proof of an orographic mechanism unless upstream moisture and synoptic timing are controlled.** Give one additional observable that would distinguish this issue from the core mechanism.
4. Translate the case into an observational protocol: station placement, sample frequency, calibration information, data exclusion rules and one independent validation source.
5. Explain why **construct an altitudinal transect and predict how lifting condensation changes in a drier air mass.** might lead to a misleading conclusion if the sample were sparse or the relevant atmospheric state changed between observations.

**Answer expectations:** A competent response states the physical assumption, uses correctly dimensioned quantities, provides an interpretation in the context of the mechanism, reports an alternative explanation, and explicitly distinguishes fictional numerical inputs from observed meteorological evidence. Answers that assert a deterministic local forecast from these toy equations are not scientifically justified.


## Unit 3 capstone — A reproducible atmospheric argument

Start from the research question **How does water vapor become droplets, ice, cloud layers and measurable precipitation?**. Create an evidence map that distinguishes the three sources **temperature/dewpoint pair**, **cloud-base estimate** and **precipitation observation**. The first source should establish the main physical state, the second should show whether the proposed forcing was present, and the third should offer a genuinely independent check. For the synthetic scenario, state a primary hypothesis and an alternative that differs in mechanism rather than merely in parameter size. Specify what both would predict at the same station but at different heights or times. In your technical report, use no unexplained uncertainty bars; distinguish calibration limits, observation support, model approximation, initialization errors, and uncertainty about the process itself.

**Data and reproducibility task:** Read the 30 synthetic records for this unit. Convert the ISO timestamps into a time axis, compute a descriptive mean and a robust range, and repeat the analysis after removing every fifth observation. If the trend changes materially, explain whether the underlying signal might be under-sampled. Prepare a plain-language summary of what the dataset can and cannot support. Supply enough detail that another student can reproduce every calculation without contacting the author. Use soundings, condensation nuclei, ascent and phase microphysics to explain the difference.

**Critical discussion:** Suppose an institution must make a decision from the available analysis. Identify the evidence that is missing, the consequence of a false alarm versus a missed event, and the observation that would most efficiently reduce consequential uncertainty. Provide a direct recommendation only when the dataset and problem definition warrant one. Never treat synthetic meteorological examples as an operational alert or regulatory threshold.

## Key takeaways for Unit 3

- The subject is an atmospheric system, not just an isolated plotted correlation; a defensible explanation must respect fundamental balances.
- The measurement domain, spatial scale, averaging interval and uncertainty control what can be inferred.
- The worked formulas expose sensitivity and limiting assumptions, not an automatic prediction for an unobserved site.
- A scientifically meaningful alternative hypothesis requires an observation that could falsify it.
- Operational warnings require responsible meteorological services and independently validated evidence.
