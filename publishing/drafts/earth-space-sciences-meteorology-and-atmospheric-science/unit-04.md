# Unit 4 — Atmospheric motion and planetary circulation
## The central atmospheric investigation

**Question:** Why do winds curve, form jets and transport heat and moisture from regional to global scales?

**Case setting:** Upper-air soundings show strong jet-level winds while surface winds are light and variable. All locations and observations in the following investigation are synthetic. The purpose is to learn which inference would survive contact with independent measurements, rather than to produce a plausible-sounding story from an incomplete weather map.

Wind responds to pressure gradients, apparent Coriolis acceleration, turbulent friction and sometimes important curvature and acceleration terms. The relative strengths depend on length and time scale. Above a well-mixed boundary layer at middle latitudes, geostrophic balance is often a good diagnostic first approximation. Near the ground, friction causes flow across the isobars and modifies convergence. Near the equator the simple geostrophic approximation fails because the Coriolis parameter approaches zero.

Unequal solar heating produces meridional temperature gradients and large-scale overturning. The thermal-wind relationship says that horizontal temperature gradients imply changes in geostrophic wind with height, linking baroclinic zones to jets. Rossby waves and potential-vorticity dynamics can generate persistent high-amplitude ridges, troughs and atmospheric blocks, but one circulation map cannot identify a unique remote cause. Land–ocean thermal differences contribute to monsoons, while topography, latent heating and ocean coupling modulate onset and breaks.

### Working boundaries and research assumptions

The effective observational transect for this unit runs from **ground to jet stream**. Different forms of evidence support different kinds of inference: wind-vector field constrains one aspect, horizontal temperature gradient another, and scale estimate a third. These are not interchangeable. A flux through a boundary is different from a store inside a region; a spatial gradient is not a material change through time; a measured scalar does not determine a complete three-dimensional vector. Choose a control volume or moving parcel explicitly before writing the governing relationship. Record the averaging period and the geographical support used in comparisons.

Trace the balances appropriate to a small sea breeze, a thunderstorm and a synoptic cyclone rather than applying one formula to all three. Use directional wind components and map conventions; a wind blowing from the northwest is not the same vector as a wind pointing northwest.

### What success looks like

A strong unit report reconstructs a physical chain from forcing to response while maintaining the distinction between an observation, a calculation, a model hypothesis and a decision. Include a figure that cannot be understood without axis units, a written alternative explanation and a comparison with a second type of evidence. Test how pressure gradients, rotation, friction and thermal contrast affect wind at different scales.


## Lesson 4.1 — Pressure-gradient force and geostrophic balance

### The physical question

Away from friction and rapid curvature, horizontal pressure-gradient acceleration is approximately balanced by Coriolis acceleration. Geostrophic wind runs along constant-pressure or height contours, with sign and geometry depending on hemisphere. For the synthetic case, distinguish state, flux, tendency and any empirical relationship. When air moves past a fixed sensor, an observed change does not by itself establish a local transformation. Record the vertical level and sampling interval.


### From fundamental laws to an operational approximation

Begin by drawing **ground to jet stream** and labeling **forces and displacement scales**. State a relevant physical conservation law, and distinguish that law from its simplified diagnostic approximation. Check dimensions and direction conventions before calculating; atmospheric fields may be spatially varying even when one chart appears constant.


### What observations could distinguish mechanisms?

Estimate upper-level pressure or geopotential-height gradients and compare resulting geostrophic direction with radiosonde winds. Identify the observation time, position, calibration information and observational resolution. Contrast **wind-vector field**, **horizontal temperature gradient** and **scale estimate**. A strong experiment predicts one place, time or altitude where rival explanations differ. In particular, assess an unsupported assumption of local equilibrium; never use the same evidence both to tune a hypothesis and to claim its independent confirmation.


### Worked numerical case — Geostrophic wind magnitude

**Fictional data:** For a pressure gradient of 0.002 Pa/m, rho=1.2 kg/m³ and f=10−4 s−1.

**Calculation:** `0.002/(1.2*1e-4)`. The numerical result is **16.67 m/s**. Explicitly verify its units and interpretation; the number is a conditional result from invented inputs, not a documented observation. **Sensitivity:** perturb the dominant uncertain input by 10% and report what changes. Invalid very close to equator and where friction/curvature dominates. Explain which excluded process might invalidate the simplified estimate.


### Limits, confounding and counterfactual reasoning

Near the equator f approaches zero and a geostrophic approximation becomes singular; it must not be used for equatorial flow. Contrast an alternative mechanism and state an observation that could discriminate between them. A more complex fitted curve is not necessarily a better causal explanation. Record site elevation, weather regime and measurement support before transferring a conclusion to a new situation.


### Practical study investigation

Draw the force vectors for a Northern Hemisphere upper-level westward pressure gradient and compare with actual wind. Use `datasets/unit-04-synthetic.csv` for reproducible practice: plot the variable at native and aggregated sampling frequency; annotate potential instrument error and a rival hypothesis. Reserve some observations for an independent check. The synthetic values are not validated natural observations, and apparent agreement with an illustrative model is not forecast verification.


### Conceptual checks and problem set

1. Draw the physical process underlying **Pressure-gradient force and geostrophic balance**, then label the state variables, external forcing, fluxes and observational boundary. Which label is least well supported?
2. Reproduce the worked example with all unit conversions visible. Change one assumed value by 10%; report the new answer and interpret whether its sign or scale is plausible.
3. Explain how **near the equator f approaches zero and a geostrophic approximation becomes singular; it must not be used for equatorial flow.** Give one additional observable that would distinguish this issue from the core mechanism.
4. Translate the case into an observational protocol: station placement, sample frequency, calibration information, data exclusion rules and one independent validation source.
5. Explain why **draw the force vectors for a Northern Hemisphere upper-level westward pressure gradient and compare with actual wind.** might lead to a misleading conclusion if the sample were sparse or the relevant atmospheric state changed between observations.

**Answer expectations:** A competent response states the physical assumption, uses correctly dimensioned quantities, provides an interpretation in the context of the mechanism, reports an alternative explanation, and explicitly distinguishes fictional numerical inputs from observed meteorological evidence. Answers that assert a deterministic local forecast from these toy equations are not scientifically justified.


## Lesson 4.2 — Coriolis acceleration and Rossby number

### The physical question

The apparent Coriolis deflection is a consequence of Earth rotation in the rotating reference frame. Rossby number U/(fL) estimates inertial-to-Coriolis importance; local thunderstorms differ from synoptic depressions. For the synthetic case, distinguish state, flux, tendency and any empirical relationship. When air moves past a fixed sensor, an observed change does not by itself establish a local transformation. Record the vertical level and sampling interval.


### From fundamental laws to an operational approximation

Begin by drawing **ground to jet stream** and labeling **forces and displacement scales**. State a relevant physical conservation law, and distinguish that law from its simplified diagnostic approximation. Check dimensions and direction conventions before calculating; atmospheric fields may be spatially varying even when one chart appears constant.


### What observations could distinguish mechanisms?

Contrast wind curvature in a mesoscale sea breeze and a thousand-kilometer midlatitude cyclone, calculating characteristic Rossby numbers. Identify the observation time, position, calibration information and observational resolution. Contrast **wind-vector field**, **horizontal temperature gradient** and **scale estimate**. A strong experiment predicts one place, time or altitude where rival explanations differ. In particular, assess mixing between air masses; never use the same evidence both to tune a hypothesis and to claim its independent confirmation.


### Worked numerical case — Coriolis parameter

**Fictional data:** Find f=2Ω sin(phi) at latitude 45° with Ω=7.2921e−5 s−1.

**Calculation:** `2*7.2921e-5*math.sin(math.pi/4)`. The numerical result is **0.0001031 s⁻¹**. Explicitly verify its units and interpretation; the number is a conditional result from invented inputs, not a documented observation. **Sensitivity:** perturb the dominant uncertain input by 10% and report what changes. The sign changes across hemispheres and tends to zero at equator. Explain which excluded process might invalidate the simplified estimate.


### Limits, confounding and counterfactual reasoning

Coriolis force does not itself initiate motion, and everyday bathtub drains are not reliably controlled by Earth rotation. Contrast an alternative mechanism and state an observation that could discriminate between them. A more complex fitted curve is not necessarily a better causal explanation. Record site elevation, weather regime and measurement support before transferring a conclusion to a new situation.


### Practical study investigation

Use two length-scale assumptions to show why a local circulation may not be geostrophic. Use `datasets/unit-04-synthetic.csv` for reproducible practice: plot the variable at native and aggregated sampling frequency; annotate potential instrument error and a rival hypothesis. Reserve some observations for an independent check. The synthetic values are not validated natural observations, and apparent agreement with an illustrative model is not forecast verification.


### Conceptual checks and problem set

1. Draw the physical process underlying **Coriolis acceleration and Rossby number**, then label the state variables, external forcing, fluxes and observational boundary. Which label is least well supported?
2. Reproduce the worked example with all unit conversions visible. Change one assumed value by 10%; report the new answer and interpret whether its sign or scale is plausible.
3. Explain how **coriolis force does not itself initiate motion, and everyday bathtub drains are not reliably controlled by Earth rotation.** Give one additional observable that would distinguish this issue from the core mechanism.
4. Translate the case into an observational protocol: station placement, sample frequency, calibration information, data exclusion rules and one independent validation source.
5. Explain why **use two length-scale assumptions to show why a local circulation may not be geostrophic.** might lead to a misleading conclusion if the sample were sparse or the relevant atmospheric state changed between observations.

**Answer expectations:** A competent response states the physical assumption, uses correctly dimensioned quantities, provides an interpretation in the context of the mechanism, reports an alternative explanation, and explicitly distinguishes fictional numerical inputs from observed meteorological evidence. Answers that assert a deterministic local forecast from these toy equations are not scientifically justified.


## Lesson 4.3 — Thermal wind and vertical shear

### The physical question

The thermal-wind relation links vertical change of geostrophic wind to horizontal temperature gradient and hydrostatic balance. It does not describe a second wind; it diagnoses shear between pressure levels. For the synthetic case, distinguish state, flux, tendency and any empirical relationship. When air moves past a fixed sensor, an observed change does not by itself establish a local transformation. Record the vertical level and sampling interval.


### From fundamental laws to an operational approximation

Begin by drawing **ground to jet stream** and labeling **forces and displacement scales**. State a relevant physical conservation law, and distinguish that law from its simplified diagnostic approximation. Check dimensions and direction conventions before calculating; atmospheric fields may be spatially varying even when one chart appears constant.


### What observations could distinguish mechanisms?

Analyze 1000–500 hPa thickness and 850–300 hPa winds, locating baroclinic zones and strong jets. Identify the observation time, position, calibration information and observational resolution. Contrast **wind-vector field**, **horizontal temperature gradient** and **scale estimate**. A strong experiment predicts one place, time or altitude where rival explanations differ. In particular, assess a measurement artifact mistaken for a physical anomaly; never use the same evidence both to tune a hypothesis and to claim its independent confirmation.


### Worked numerical case — Idealized thermal wind shear

**Fictional data:** With Rd=287, f=1e−4, dT/dy=−0.001 K/m from 850 to 500 hPa: zonal shear =−Rd/f*dTdy*ln(p1/p2).

**Calculation:** `-287/1e-4*(-.001)*math.log(850/500)`. The numerical result is **1523 m/s**. Explicitly verify its units and interpretation; the number is a conditional result from invented inputs, not a documented observation. **Sensitivity:** perturb the dominant uncertain input by 10% and report what changes. Assumes geostrophy, hydrostatic balance and representative thermal gradient. Explain which excluded process might invalidate the simplified estimate.


### Limits, confounding and counterfactual reasoning

Thickness can reflect mean layer virtual temperature while wind profiles also contain ageostrophic accelerations and friction. Contrast an alternative mechanism and state an observation that could discriminate between them. A more complex fitted curve is not necessarily a better causal explanation. Record site elevation, weather regime and measurement support before transferring a conclusion to a new situation.


### Practical study investigation

Predict the direction of geostrophic shear across a north–south temperature gradient and confirm from a sounding. Use `datasets/unit-04-synthetic.csv` for reproducible practice: plot the variable at native and aggregated sampling frequency; annotate potential instrument error and a rival hypothesis. Reserve some observations for an independent check. The synthetic values are not validated natural observations, and apparent agreement with an illustrative model is not forecast verification.


### Conceptual checks and problem set

1. Draw the physical process underlying **Thermal wind and vertical shear**, then label the state variables, external forcing, fluxes and observational boundary. Which label is least well supported?
2. Reproduce the worked example with all unit conversions visible. Change one assumed value by 10%; report the new answer and interpret whether its sign or scale is plausible.
3. Explain how **thickness can reflect mean layer virtual temperature while wind profiles also contain ageostrophic accelerations and friction.** Give one additional observable that would distinguish this issue from the core mechanism.
4. Translate the case into an observational protocol: station placement, sample frequency, calibration information, data exclusion rules and one independent validation source.
5. Explain why **predict the direction of geostrophic shear across a north–south temperature gradient and confirm from a sounding.** might lead to a misleading conclusion if the sample were sparse or the relevant atmospheric state changed between observations.

**Answer expectations:** A competent response states the physical assumption, uses correctly dimensioned quantities, provides an interpretation in the context of the mechanism, reports an alternative explanation, and explicitly distinguishes fictional numerical inputs from observed meteorological evidence. Answers that assert a deterministic local forecast from these toy equations are not scientifically justified.


## Lesson 4.4 — Hadley circulation, trade winds and monsoons

### The physical question

Unequal solar heating and angular-momentum constraints shape tropical overturning, subtropical subsidence and trade winds. Seasonal migration of convection and land–sea thermal contrast influence monsoons alongside ocean feedbacks and regional topography. For the synthetic case, distinguish state, flux, tendency and any empirical relationship. When air moves past a fixed sensor, an observed change does not by itself establish a local transformation. Record the vertical level and sampling interval.


### From fundamental laws to an operational approximation

Begin by drawing **ground to jet stream** and labeling **forces and displacement scales**. State a relevant physical conservation law, and distinguish that law from its simplified diagnostic approximation. Check dimensions and direction conventions before calculating; atmospheric fields may be spatially varying even when one chart appears constant.


### What observations could distinguish mechanisms?

Compare seasonal upper-air winds, rainfall maxima and outgoing longwave radiation across a tropical ocean basin. Identify the observation time, position, calibration information and observational resolution. Contrast **wind-vector field**, **horizontal temperature gradient** and **scale estimate**. A strong experiment predicts one place, time or altitude where rival explanations differ. In particular, assess a poorly known top or lateral boundary; never use the same evidence both to tune a hypothesis and to claim its independent confirmation.


### Worked numerical case — Monsoon flow travel estimate

**Fictional data:** A representative low-level air parcel travels 1500 km at 12 m/s.

**Calculation:** `1500000/12/86400`. The numerical result is **1.447 days**. Explicitly verify its units and interpretation; the number is a conditional result from invented inputs, not a documented observation. **Sensitivity:** perturb the dominant uncertain input by 10% and report what changes. This is a kinematic estimate, not moisture residence time. Explain which excluded process might invalidate the simplified estimate.


### Limits, confounding and counterfactual reasoning

A monsoon is not simply a gigantic daily sea breeze; circulation involves remote and regional feedbacks across timescales. Contrast an alternative mechanism and state an observation that could discriminate between them. A more complex fitted curve is not necessarily a better causal explanation. Record site elevation, weather regime and measurement support before transferring a conclusion to a new situation.


### Practical study investigation

Diagram a cross-equatorial monsoon flow and specify observations that distinguish onset from a transient wet spell. Use `datasets/unit-04-synthetic.csv` for reproducible practice: plot the variable at native and aggregated sampling frequency; annotate potential instrument error and a rival hypothesis. Reserve some observations for an independent check. The synthetic values are not validated natural observations, and apparent agreement with an illustrative model is not forecast verification.


### Conceptual checks and problem set

1. Draw the physical process underlying **Hadley circulation, trade winds and monsoons**, then label the state variables, external forcing, fluxes and observational boundary. Which label is least well supported?
2. Reproduce the worked example with all unit conversions visible. Change one assumed value by 10%; report the new answer and interpret whether its sign or scale is plausible.
3. Explain how **a monsoon is not simply a gigantic daily sea breeze; circulation involves remote and regional feedbacks across timescales.** Give one additional observable that would distinguish this issue from the core mechanism.
4. Translate the case into an observational protocol: station placement, sample frequency, calibration information, data exclusion rules and one independent validation source.
5. Explain why **diagram a cross-equatorial monsoon flow and specify observations that distinguish onset from a transient wet spell.** might lead to a misleading conclusion if the sample were sparse or the relevant atmospheric state changed between observations.

**Answer expectations:** A competent response states the physical assumption, uses correctly dimensioned quantities, provides an interpretation in the context of the mechanism, reports an alternative explanation, and explicitly distinguishes fictional numerical inputs from observed meteorological evidence. Answers that assert a deterministic local forecast from these toy equations are not scientifically justified.


## Lesson 4.5 — Rossby waves, jet streams and blocking

### The physical question

Conservation of potential vorticity and latitudinal variation in planetary vorticity support large-scale Rossby waves. Jet streams follow sharp horizontal temperature contrasts and can develop meanders and persistent blocks. For the synthetic case, distinguish state, flux, tendency and any empirical relationship. When air moves past a fixed sensor, an observed change does not by itself establish a local transformation. Record the vertical level and sampling interval.


### From fundamental laws to an operational approximation

Begin by drawing **ground to jet stream** and labeling **forces and displacement scales**. State a relevant physical conservation law, and distinguish that law from its simplified diagnostic approximation. Check dimensions and direction conventions before calculating; atmospheric fields may be spatially varying even when one chart appears constant.


### What observations could distinguish mechanisms?

Track successive geopotential-height maps and jet isotachs to separate slow-moving ridge amplification from traveling short waves. Identify the observation time, position, calibration information and observational resolution. Contrast **wind-vector field**, **horizontal temperature gradient** and **scale estimate**. A strong experiment predicts one place, time or altitude where rival explanations differ. In particular, assess an unsupported assumption of local equilibrium; never use the same evidence both to tune a hypothesis and to claim its independent confirmation.


### Worked numerical case — Rossby number

**Fictional data:** U=10 m/s, length scale L=1000 km, f=1e−4 s−1; estimate Ro.

**Calculation:** `10/(1e-4*1e6)`. The numerical result is **0.1 dimensionless**. Explicitly verify its units and interpretation; the number is a conditional result from invented inputs, not a documented observation. **Sensitivity:** perturb the dominant uncertain input by 10% and report what changes. A single velocity and length scale obscures flow complexity. Explain which excluded process might invalidate the simplified estimate.


### Limits, confounding and counterfactual reasoning

A quasi-stationary ridge does not prove one unique remote forcing; ensemble circulation patterns and background flow matter. Contrast an alternative mechanism and state an observation that could discriminate between them. A more complex fitted curve is not necessarily a better causal explanation. Record site elevation, weather regime and measurement support before transferring a conclusion to a new situation.


### Practical study investigation

Quantify the translation of a 500 hPa trough and describe consequences for rain persistence downstream. Use `datasets/unit-04-synthetic.csv` for reproducible practice: plot the variable at native and aggregated sampling frequency; annotate potential instrument error and a rival hypothesis. Reserve some observations for an independent check. The synthetic values are not validated natural observations, and apparent agreement with an illustrative model is not forecast verification.


### Conceptual checks and problem set

1. Draw the physical process underlying **Rossby waves, jet streams and blocking**, then label the state variables, external forcing, fluxes and observational boundary. Which label is least well supported?
2. Reproduce the worked example with all unit conversions visible. Change one assumed value by 10%; report the new answer and interpret whether its sign or scale is plausible.
3. Explain how **a quasi-stationary ridge does not prove one unique remote forcing; ensemble circulation patterns and background flow matter.** Give one additional observable that would distinguish this issue from the core mechanism.
4. Translate the case into an observational protocol: station placement, sample frequency, calibration information, data exclusion rules and one independent validation source.
5. Explain why **quantify the translation of a 500 hPa trough and describe consequences for rain persistence downstream.** might lead to a misleading conclusion if the sample were sparse or the relevant atmospheric state changed between observations.

**Answer expectations:** A competent response states the physical assumption, uses correctly dimensioned quantities, provides an interpretation in the context of the mechanism, reports an alternative explanation, and explicitly distinguishes fictional numerical inputs from observed meteorological evidence. Answers that assert a deterministic local forecast from these toy equations are not scientifically justified.


## Unit 4 capstone — A reproducible atmospheric argument

Start from the research question **Why do winds curve, form jets and transport heat and moisture from regional to global scales?**. Create an evidence map that distinguishes the three sources **wind-vector field**, **horizontal temperature gradient** and **scale estimate**. The first source should establish the main physical state, the second should show whether the proposed forcing was present, and the third should offer a genuinely independent check. For the synthetic scenario, state a primary hypothesis and an alternative that differs in mechanism rather than merely in parameter size. Specify what both would predict at the same station but at different heights or times. In your technical report, use no unexplained uncertainty bars; distinguish calibration limits, observation support, model approximation, initialization errors, and uncertainty about the process itself.

**Data and reproducibility task:** Read the 30 synthetic records for this unit. Convert the ISO timestamps into a time axis, compute a descriptive mean and a robust range, and repeat the analysis after removing every fifth observation. If the trend changes materially, explain whether the underlying signal might be under-sampled. Prepare a plain-language summary of what the dataset can and cannot support. Supply enough detail that another student can reproduce every calculation without contacting the author. Test how pressure gradients, rotation, friction and thermal contrast affect wind at different scales.

**Critical discussion:** Suppose an institution must make a decision from the available analysis. Identify the evidence that is missing, the consequence of a false alarm versus a missed event, and the observation that would most efficiently reduce consequential uncertainty. Provide a direct recommendation only when the dataset and problem definition warrant one. Never treat synthetic meteorological examples as an operational alert or regulatory threshold.

## Key takeaways for Unit 4

- The subject is an atmospheric system, not just an isolated plotted correlation; a defensible explanation must respect fundamental balances.
- The measurement domain, spatial scale, averaging interval and uncertainty control what can be inferred.
- The worked formulas expose sensitivity and limiting assumptions, not an automatic prediction for an unobserved site.
- A scientifically meaningful alternative hypothesis requires an observation that could falsify it.
- Operational warnings require responsible meteorological services and independently validated evidence.
