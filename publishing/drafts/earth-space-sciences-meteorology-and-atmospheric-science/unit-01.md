# Unit 1 — Atmospheric structure and thermodynamic foundations
## The central atmospheric investigation

**Question:** How do air composition, pressure, temperature and stability govern an atmospheric column?

**Case setting:** An instrumented research balloon rises from a coastal station through the boundary layer to the lower stratosphere. All locations and observations in the following investigation are synthetic. The purpose is to learn which inference would survive contact with independent measurements, rather than to produce a plausible-sounding story from an incomplete weather map.

An atmosphere is a compressible fluid in a gravitational field. Its properties depend on pressure, absolute temperature, composition, and the vertical exchange of heat and momentum. The ideal gas relationship is powerful precisely because it ties three measurable variables together; it is not a substitute for checking whether the same air mass is being observed. In a drifting balloon ascent a value recorded at 3 km occurs at a later time and another horizontal location than the surface sample. A vertical profile is therefore best understood as a spatial–temporal transect rather than a frozen column.

Hydrostatic balance makes the layer mass above a level responsible for the pressure at that level. If an air column is warmer at fixed pressure endpoints, it is generally thicker than a colder column of the same composition. This principle links the early lessons on pressure to the later thermal-wind interpretation of jet streams. Potential temperature is especially useful because a dry parcel moved adiabatically between pressure levels changes ordinary temperature without changing its potential temperature. A stable atmosphere resists a small vertical displacement; an unstable one may accelerate displacement if environmental stratification supports buoyancy. Real clouds require moist thermodynamics, latent heat, and entrainment, so the dry conceptual picture is a starting condition.

### Working boundaries and research assumptions

The effective observational transect for this unit runs from **surface to lower stratosphere**. Different forms of evidence support different kinds of inference: pressure–height curve constrains one aspect, thermodynamic sounding another, and virtual-temperature profile a third. These are not interchangeable. A flux through a boundary is different from a store inside a region; a spatial gradient is not a material change through time; a measured scalar does not determine a complete three-dimensional vector. Choose a control volume or moving parcel explicitly before writing the governing relationship. Record the averaging period and the geographical support used in comparisons.

Do not assume a measured pressure fall always implies a cyclone: a pressure tendency may reflect local oscillations, changing station elevation, or instrument errors. In the capstone sounding, identify which layers are observed, which variables are converted, and which stability claims depend on neglecting water vapor. Provide plots with units and an honest treatment of sensor uncertainty.

### What success looks like

A strong unit report reconstructs a physical chain from forcing to response while maintaining the distinction between an observation, a calculation, a model hypothesis and a decision. Include a figure that cannot be understood without axis units, a written alternative explanation and a comparison with a second type of evidence. Compare a hydrostatic column and a moving column; estimate how a measurement at one level constrains layers not directly sampled.


## Lesson 1.1 — Atmospheric composition and vertical layers

### The physical question

Nitrogen and oxygen dominate dry-air volume, but water vapor varies and affects density, radiation and phase transitions. Tropospheric temperatures generally decrease with altitude while stratospheric ozone absorption helps produce a temperature inversion. The tropopause changes height across latitude and season. For the synthetic case, distinguish state, flux, tendency and any empirical relationship. When air moves past a fixed sensor, an observed change does not by itself establish a local transformation. Record the vertical level and sampling interval.


### From fundamental laws to an operational approximation

Begin by drawing **surface to lower stratosphere** and labeling **pressure and thermal state**. State a relevant physical conservation law, and distinguish that law from its simplified diagnostic approximation. Check dimensions and direction conventions before calculating; atmospheric fields may be spatially varying even when one chart appears constant.


### What observations could distinguish mechanisms?

Compare a radiosonde temperature profile with ozone and humidity traces; locate a thermodynamic tropopause from lapse-rate criteria rather than an arbitrary fixed altitude. Identify the observation time, position, calibration information and observational resolution. Contrast **pressure–height curve**, **thermodynamic sounding** and **virtual-temperature profile**. A strong experiment predicts one place, time or altitude where rival explanations differ. In particular, assess changes in observation height; never use the same evidence both to tune a hypothesis and to claim its independent confirmation.


### Worked numerical case — Dry-air density

**Fictional data:** At p=100000 Pa and T=290 K, estimate dry-air density with Rd=287 J/(kg K).

**Calculation:** `100000/(287*290)`. The numerical result is **1.201 kg/m³**. Explicitly verify its units and interpretation; the number is a conditional result from invented inputs, not a documented observation. **Sensitivity:** perturb the dominant uncertain input by 10% and report what changes. Use virtual temperature when moisture is material. Explain which excluded process might invalidate the simplified estimate.


### Limits, confounding and counterfactual reasoning

Balloon temperature sensors can lag changes during a rapid ascent; a local inversion must not be mislabeled as the climatological tropopause. Contrast an alternative mechanism and state an observation that could discriminate between them. A more complex fitted curve is not necessarily a better causal explanation. Record site elevation, weather regime and measurement support before transferring a conclusion to a new situation.


### Practical study investigation

Draw a height–pressure–temperature section and explain which layers would be lost in a coarse model grid. Use `datasets/unit-01-synthetic.csv` for reproducible practice: plot the variable at native and aggregated sampling frequency; annotate potential instrument error and a rival hypothesis. Reserve some observations for an independent check. The synthetic values are not validated natural observations, and apparent agreement with an illustrative model is not forecast verification.


### Conceptual checks and problem set

1. Draw the physical process underlying **Atmospheric composition and vertical layers**, then label the state variables, external forcing, fluxes and observational boundary. Which label is least well supported?
2. Reproduce the worked example with all unit conversions visible. Change one assumed value by 10%; report the new answer and interpret whether its sign or scale is plausible.
3. Explain how **balloon temperature sensors can lag changes during a rapid ascent; a local inversion must not be mislabeled as the climatological tropopause.** Give one additional observable that would distinguish this issue from the core mechanism.
4. Translate the case into an observational protocol: station placement, sample frequency, calibration information, data exclusion rules and one independent validation source.
5. Explain why **draw a height–pressure–temperature section and explain which layers would be lost in a coarse model grid.** might lead to a misleading conclusion if the sample were sparse or the relevant atmospheric state changed between observations.

**Answer expectations:** A competent response states the physical assumption, uses correctly dimensioned quantities, provides an interpretation in the context of the mechanism, reports an alternative explanation, and explicitly distinguishes fictional numerical inputs from observed meteorological evidence. Answers that assert a deterministic local forecast from these toy equations are not scientifically justified.


## Lesson 1.2 — Pressure, density and ideal gas mixtures

### The physical question

An atmospheric parcel satisfies p=rho Rd Tv approximately when moisture is represented by virtual temperature. Hydrostatic balance dp/dz=-rho g relates pressure to the weight of overlying air, not a direct measure of one local wind speed. For the synthetic case, distinguish state, flux, tendency and any empirical relationship. When air moves past a fixed sensor, an observed change does not by itself establish a local transformation. Record the vertical level and sampling interval.


### From fundamental laws to an operational approximation

Begin by drawing **surface to lower stratosphere** and labeling **pressure and thermal state**. State a relevant physical conservation law, and distinguish that law from its simplified diagnostic approximation. Check dimensions and direction conventions before calculating; atmospheric fields may be spatially varying even when one chart appears constant.


### What observations could distinguish mechanisms?

Use paired barometers on a hill and at sea level; estimate pressure difference while recording temperatures and instrument elevation. Identify the observation time, position, calibration information and observational resolution. Contrast **pressure–height curve**, **thermodynamic sounding** and **virtual-temperature profile**. A strong experiment predicts one place, time or altitude where rival explanations differ. In particular, assess instrument response to an abrupt transition; never use the same evidence both to tune a hypothesis and to claim its independent confirmation.


### Worked numerical case — Hypsometric thickness

**Fictional data:** Mean Tv=275 K; find layer thickness from 1000 to 850 hPa, Rd=287, g=9.81.

**Calculation:** `287*275/9.81*math.log(1000/850)`. The numerical result is **1308 m**. Explicitly verify its units and interpretation; the number is a conditional result from invented inputs, not a documented observation. **Sensitivity:** perturb the dominant uncertain input by 10% and report what changes. Layer-mean virtual temperature is an assumption, not a surface reading. Explain which excluded process might invalidate the simplified estimate.


### Limits, confounding and counterfactual reasoning

A sea-level-adjusted pressure is derived from an assumed layer temperature and cannot be compared uncritically with raw station pressure. Contrast an alternative mechanism and state an observation that could discriminate between them. A more complex fitted curve is not necessarily a better causal explanation. Record site elevation, weather regime and measurement support before transferring a conclusion to a new situation.


### Practical study investigation

Reconstruct density two ways and state how humidity enters the virtual-temperature correction. Use `datasets/unit-01-synthetic.csv` for reproducible practice: plot the variable at native and aggregated sampling frequency; annotate potential instrument error and a rival hypothesis. Reserve some observations for an independent check. The synthetic values are not validated natural observations, and apparent agreement with an illustrative model is not forecast verification.


### Conceptual checks and problem set

1. Draw the physical process underlying **Pressure, density and ideal gas mixtures**, then label the state variables, external forcing, fluxes and observational boundary. Which label is least well supported?
2. Reproduce the worked example with all unit conversions visible. Change one assumed value by 10%; report the new answer and interpret whether its sign or scale is plausible.
3. Explain how **a sea-level-adjusted pressure is derived from an assumed layer temperature and cannot be compared uncritically with raw station pressure.** Give one additional observable that would distinguish this issue from the core mechanism.
4. Translate the case into an observational protocol: station placement, sample frequency, calibration information, data exclusion rules and one independent validation source.
5. Explain why **reconstruct density two ways and state how humidity enters the virtual-temperature correction.** might lead to a misleading conclusion if the sample were sparse or the relevant atmospheric state changed between observations.

**Answer expectations:** A competent response states the physical assumption, uses correctly dimensioned quantities, provides an interpretation in the context of the mechanism, reports an alternative explanation, and explicitly distinguishes fictional numerical inputs from observed meteorological evidence. Answers that assert a deterministic local forecast from these toy equations are not scientifically justified.


## Lesson 1.3 — Adiabatic processes and potential temperature

### The physical question

A rising unsaturated air parcel expands and cools near the dry adiabatic rate, while an ideal descent warms from compression. Potential temperature theta=T(1000 hPa/p)^(Rd/cp) expresses temperature relative to a reference pressure for an adiabatic transformation. For the synthetic case, distinguish state, flux, tendency and any empirical relationship. When air moves past a fixed sensor, an observed change does not by itself establish a local transformation. Record the vertical level and sampling interval.


### From fundamental laws to an operational approximation

Begin by drawing **surface to lower stratosphere** and labeling **pressure and thermal state**. State a relevant physical conservation law, and distinguish that law from its simplified diagnostic approximation. Check dimensions and direction conventions before calculating; atmospheric fields may be spatially varying even when one chart appears constant.


### What observations could distinguish mechanisms?

Plot observed T and computed theta against pressure for morning and afternoon profiles, identifying stable layers and mixed layers. Identify the observation time, position, calibration information and observational resolution. Contrast **pressure–height curve**, **thermodynamic sounding** and **virtual-temperature profile**. A strong experiment predicts one place, time or altitude where rival explanations differ. In particular, assess spatial interpolation across sparse stations; never use the same evidence both to tune a hypothesis and to claim its independent confirmation.


### Worked numerical case — Potential temperature

**Fictional data:** Parcel T=280 K at p=850 hPa; compute theta with kappa=0.286.

**Calculation:** `280*(1000/850)**0.286`. The numerical result is **293.3 K**. Explicitly verify its units and interpretation; the number is a conditional result from invented inputs, not a documented observation. **Sensitivity:** perturb the dominant uncertain input by 10% and report what changes. Dry reversible assumptions fail for condensation and strong mixing. Explain which excluded process might invalidate the simplified estimate.


### Limits, confounding and counterfactual reasoning

Strong entrainment, cloud formation, radiative heating and irreversible mixing violate a perfectly reversible dry-adiabatic parcel assumption. Contrast an alternative mechanism and state an observation that could discriminate between them. A more complex fitted curve is not necessarily a better causal explanation. Record site elevation, weather regime and measurement support before transferring a conclusion to a new situation.


### Practical study investigation

Trace two parcels from different pressure levels onto a theta–height diagram and compare vertical stability. Use `datasets/unit-01-synthetic.csv` for reproducible practice: plot the variable at native and aggregated sampling frequency; annotate potential instrument error and a rival hypothesis. Reserve some observations for an independent check. The synthetic values are not validated natural observations, and apparent agreement with an illustrative model is not forecast verification.


### Conceptual checks and problem set

1. Draw the physical process underlying **Adiabatic processes and potential temperature**, then label the state variables, external forcing, fluxes and observational boundary. Which label is least well supported?
2. Reproduce the worked example with all unit conversions visible. Change one assumed value by 10%; report the new answer and interpret whether its sign or scale is plausible.
3. Explain how **strong entrainment, cloud formation, radiative heating and irreversible mixing violate a perfectly reversible dry-adiabatic parcel assumption.** Give one additional observable that would distinguish this issue from the core mechanism.
4. Translate the case into an observational protocol: station placement, sample frequency, calibration information, data exclusion rules and one independent validation source.
5. Explain why **trace two parcels from different pressure levels onto a theta–height diagram and compare vertical stability.** might lead to a misleading conclusion if the sample were sparse or the relevant atmospheric state changed between observations.

**Answer expectations:** A competent response states the physical assumption, uses correctly dimensioned quantities, provides an interpretation in the context of the mechanism, reports an alternative explanation, and explicitly distinguishes fictional numerical inputs from observed meteorological evidence. Answers that assert a deterministic local forecast from these toy equations are not scientifically justified.


## Lesson 1.4 — Static stability, buoyancy and inversions

### The physical question

Buoyancy arises from density contrasts: warmer or moister air can be lighter than its environment at the same pressure. Potential-temperature gradients offer a dry-stability indicator, while moist parcels need saturated thermodynamics and entrainment. For the synthetic case, distinguish state, flux, tendency and any empirical relationship. When air moves past a fixed sensor, an observed change does not by itself establish a local transformation. Record the vertical level and sampling interval.


### From fundamental laws to an operational approximation

Begin by drawing **surface to lower stratosphere** and labeling **pressure and thermal state**. State a relevant physical conservation law, and distinguish that law from its simplified diagnostic approximation. Check dimensions and direction conventions before calculating; atmospheric fields may be spatially varying even when one chart appears constant.


### What observations could distinguish mechanisms?

Compare a nocturnal inversion with afternoon mixed-layer profiles and use balloon or mast temperatures at multiple heights. Identify the observation time, position, calibration information and observational resolution. Contrast **pressure–height curve**, **thermodynamic sounding** and **virtual-temperature profile**. A strong experiment predicts one place, time or altitude where rival explanations differ. In particular, assess weather regime change during averaging; never use the same evidence both to tune a hypothesis and to claim its independent confirmation.


### Worked numerical case — Brunt–Väisälä estimate

**Fictional data:** In a dry stable layer theta increases 3 K over 300 m; theta=300 K, g=9.81.

**Calculation:** `math.sqrt(9.81/300*(3/300))`. The numerical result is **0.01808 s⁻¹**. Explicitly verify its units and interpretation; the number is a conditional result from invented inputs, not a documented observation. **Sensitivity:** perturb the dominant uncertain input by 10% and report what changes. Meaningful only for small-amplitude displacements in a suitable stratification. Explain which excluded process might invalidate the simplified estimate.


### Limits, confounding and counterfactual reasoning

A positive surface temperature is not proof of instability; surface-based CAPE may be absent beneath a strong cap. Contrast an alternative mechanism and state an observation that could discriminate between them. A more complex fitted curve is not necessarily a better causal explanation. Record site elevation, weather regime and measurement support before transferring a conclusion to a new situation.


### Practical study investigation

Use temperature perturbations to predict parcel acceleration with a clearly marked reference environment. Use `datasets/unit-01-synthetic.csv` for reproducible practice: plot the variable at native and aggregated sampling frequency; annotate potential instrument error and a rival hypothesis. Reserve some observations for an independent check. The synthetic values are not validated natural observations, and apparent agreement with an illustrative model is not forecast verification.


### Conceptual checks and problem set

1. Draw the physical process underlying **Static stability, buoyancy and inversions**, then label the state variables, external forcing, fluxes and observational boundary. Which label is least well supported?
2. Reproduce the worked example with all unit conversions visible. Change one assumed value by 10%; report the new answer and interpret whether its sign or scale is plausible.
3. Explain how **a positive surface temperature is not proof of instability; surface-based CAPE may be absent beneath a strong cap.** Give one additional observable that would distinguish this issue from the core mechanism.
4. Translate the case into an observational protocol: station placement, sample frequency, calibration information, data exclusion rules and one independent validation source.
5. Explain why **use temperature perturbations to predict parcel acceleration with a clearly marked reference environment.** might lead to a misleading conclusion if the sample were sparse or the relevant atmospheric state changed between observations.

**Answer expectations:** A competent response states the physical assumption, uses correctly dimensioned quantities, provides an interpretation in the context of the mechanism, reports an alternative explanation, and explicitly distinguishes fictional numerical inputs from observed meteorological evidence. Answers that assert a deterministic local forecast from these toy equations are not scientifically justified.


## Lesson 1.5 — Atmospheric instruments and sounding uncertainty

### The physical question

Thermometers, barometers, anemometers and humidity sensors observe quantities with exposure, response-time and calibration effects. Radiosondes record pressure, temperature, humidity and winds along a drifting path, not a stationary straight column. For the synthetic case, distinguish state, flux, tendency and any empirical relationship. When air moves past a fixed sensor, an observed change does not by itself establish a local transformation. Record the vertical level and sampling interval.


### From fundamental laws to an operational approximation

Begin by drawing **surface to lower stratosphere** and labeling **pressure and thermal state**. State a relevant physical conservation law, and distinguish that law from its simplified diagnostic approximation. Check dimensions and direction conventions before calculating; atmospheric fields may be spatially varying even when one chart appears constant.


### What observations could distinguish mechanisms?

Cross-check a radiosonde with a rooftop station and a second balloon at a different hour, including station metadata and sensor time response. Identify the observation time, position, calibration information and observational resolution. Contrast **pressure–height curve**, **thermodynamic sounding** and **virtual-temperature profile**. A strong experiment predicts one place, time or altitude where rival explanations differ. In particular, assess changes in observation height; never use the same evidence both to tune a hypothesis and to claim its independent confirmation.


### Worked numerical case — Pressure conversion

**Fictional data:** Convert an observed station pressure of 996 hPa to Pa.

**Calculation:** `996*100`. The numerical result is **99600 Pa**. Explicitly verify its units and interpretation; the number is a conditional result from invented inputs, not a documented observation. **Sensitivity:** perturb the dominant uncertain input by 10% and report what changes. Do not call a simple unit conversion a sea-level pressure adjustment. Explain which excluded process might invalidate the simplified estimate.


### Limits, confounding and counterfactual reasoning

Solar heating, radiation shielding, high-altitude dry bias and drift create profile differences that do not necessarily reflect an atmospheric transition. Contrast an alternative mechanism and state an observation that could discriminate between them. A more complex fitted curve is not necessarily a better causal explanation. Record site elevation, weather regime and measurement support before transferring a conclusion to a new situation.


### Practical study investigation

Design a station log and flag samples potentially contaminated by nearby buildings or solar exposure. Use `datasets/unit-01-synthetic.csv` for reproducible practice: plot the variable at native and aggregated sampling frequency; annotate potential instrument error and a rival hypothesis. Reserve some observations for an independent check. The synthetic values are not validated natural observations, and apparent agreement with an illustrative model is not forecast verification.


### Conceptual checks and problem set

1. Draw the physical process underlying **Atmospheric instruments and sounding uncertainty**, then label the state variables, external forcing, fluxes and observational boundary. Which label is least well supported?
2. Reproduce the worked example with all unit conversions visible. Change one assumed value by 10%; report the new answer and interpret whether its sign or scale is plausible.
3. Explain how **solar heating, radiation shielding, high-altitude dry bias and drift create profile differences that do not necessarily reflect an atmospheric transition.** Give one additional observable that would distinguish this issue from the core mechanism.
4. Translate the case into an observational protocol: station placement, sample frequency, calibration information, data exclusion rules and one independent validation source.
5. Explain why **design a station log and flag samples potentially contaminated by nearby buildings or solar exposure.** might lead to a misleading conclusion if the sample were sparse or the relevant atmospheric state changed between observations.

**Answer expectations:** A competent response states the physical assumption, uses correctly dimensioned quantities, provides an interpretation in the context of the mechanism, reports an alternative explanation, and explicitly distinguishes fictional numerical inputs from observed meteorological evidence. Answers that assert a deterministic local forecast from these toy equations are not scientifically justified.


## Unit 1 capstone — A reproducible atmospheric argument

Start from the research question **How do air composition, pressure, temperature and stability govern an atmospheric column?**. Create an evidence map that distinguishes the three sources **pressure–height curve**, **thermodynamic sounding** and **virtual-temperature profile**. The first source should establish the main physical state, the second should show whether the proposed forcing was present, and the third should offer a genuinely independent check. For the synthetic scenario, state a primary hypothesis and an alternative that differs in mechanism rather than merely in parameter size. Specify what both would predict at the same station but at different heights or times. In your technical report, use no unexplained uncertainty bars; distinguish calibration limits, observation support, model approximation, initialization errors, and uncertainty about the process itself.

**Data and reproducibility task:** Read the 30 synthetic records for this unit. Convert the ISO timestamps into a time axis, compute a descriptive mean and a robust range, and repeat the analysis after removing every fifth observation. If the trend changes materially, explain whether the underlying signal might be under-sampled. Prepare a plain-language summary of what the dataset can and cannot support. Supply enough detail that another student can reproduce every calculation without contacting the author. Compare a hydrostatic column and a moving column; estimate how a measurement at one level constrains layers not directly sampled.

**Critical discussion:** Suppose an institution must make a decision from the available analysis. Identify the evidence that is missing, the consequence of a false alarm versus a missed event, and the observation that would most efficiently reduce consequential uncertainty. Provide a direct recommendation only when the dataset and problem definition warrant one. Never treat synthetic meteorological examples as an operational alert or regulatory threshold.

## Key takeaways for Unit 1

- The subject is an atmospheric system, not just an isolated plotted correlation; a defensible explanation must respect fundamental balances.
- The measurement domain, spatial scale, averaging interval and uncertainty control what can be inferred.
- The worked formulas expose sensitivity and limiting assumptions, not an automatic prediction for an unobserved site.
- A scientifically meaningful alternative hypothesis requires an observation that could falsify it.
- Operational warnings require responsible meteorological services and independently validated evidence.
