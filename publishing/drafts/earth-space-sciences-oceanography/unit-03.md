# Unit 3 — Circulation: momentum, rotation and transport

## Guiding question: Why do winds, pressure gradients and density fields produce distinct surface and deep circulations?

**Synthetic case study:** A drifter array is deployed across an eastern boundary upwelling zone while an altimeter maps a nearby eddy. The team must separate wind-driven motion from geostrophic flow and explain how uncertain reference velocities affect its transport estimate.

## Scientific foundations and the shape of the inquiry

The starting method in this unit is **momentum and transport**. Begin with a scale analysis: estimate Coriolis, pressure-gradient and frictional accelerations before assuming any one balance. Use signed vector components and draw axes with north and east clearly identified. A transport is a velocity integrated over a known cross-section, not simply a speed expressed in larger units.

**Comparative interpretation:** Use a synthetic current field with an energetic eddy superimposed on a weak regional mean. Show how different sampling dates can change the inferred transport direction, and use repeat observations to test whether the apparent reversal is enduring.

**Fieldwork and model validation:** A tracked object samples a Lagrangian trajectory, whereas a fixed current meter samples velocity at one location. Neither is a complete substitute for the other. Measurements of a front need spatial gradients; monitoring a tidal current needs sufficient temporal cadence to resolve periodic oscillations.

Oceanographic quantities generally depend on the choice of reference frame and on the boundaries of the study region. A point sensor records conditions in a small volume; a gridded map estimates a field across many cells; a process model predicts how that field should change under specified equations and boundary conditions. A student who moves directly from a point sensor to a regional mechanism is making an extrapolation that requires independent support. Keep a table recording the proposed mechanism, the predicted pattern, and the observation that would undermine it. This practice prevents a persuasive figure from becoming an unsupported explanation.

The lesson sequence moves from describing observations to relating them to mechanisms, building a tractable calculation, testing sensitivity and finally explaining what action could justifiably follow. No numerical constant in a simplified teaching exercise should be mistaken for a globally fitted parameter. The numerical questions in this unit are deliberately synthetic; their main purpose is to expose the dimensional structure of the reasoning.

## Lesson 3.1 — Momentum budgets and Coriolis acceleration

### 1. Physical question and core explanation

Horizontal ocean momentum balances pressure-gradient, Coriolis, wind stress, friction and acceleration terms. Rotation deflects moving water relative to Earth without doing work on the parcel. The f-plane approximation can explain a local phenomenon while failing over a wide latitude range.


### 2. What to measure, and how

Estimate the Coriolis parameter at two latitudes and discuss why near-equatorial dynamics deserve a different scaling. Draw free-body-style vectors for a northern-hemisphere current under an offshore pressure gradient.


### 3. Mechanism, model and dimensional reasoning

In a first approximation, represent **momentum budgets and coriolis acceleration** with an inventory, a forcing term and at least one route for exchange with surrounding water or the atmosphere. The model may be a proportionality, a conservative mixture, a flux balance, or a kinematic relation. Put units beside every variable before substituting measurements. A ratio of two volumes is dimensionless; a current is length per time; and a volume transport also includes cross-sectional area. If dimensions do not close, the numerical result cannot be correct even if a calculator produced it.


### 4. Fully worked quantitative case

**Problem — Coriolis parameter at 45°.** Calculate f=2Ω sinφ with Ω=7.2921159×10⁻⁵ s⁻¹ and φ=45°.

**Model and substitution:** `2*7.2921159e-5*math.sin(math.radians(45))`. Evaluate it using the units stated in the problem and the accompanying conversion factors. The result is **0.00010313 s⁻¹**. Every multiplier or divisor should have a physical interpretation: cross-sectional area converts velocity to transport; elapsed time converts a rate to a stock change; a density or heat-capacity factor connects a thermodynamic state change to an energy inventory. For angular or exponent-based relationships, specify whether the input is degrees, radians or a dimensionless ratio.

**Interpretation:** At the equator the conventional geostrophic division by f fails. The numerical answer belongs to a deliberately simplified scenario. Compare it against an order-of-magnitude estimate: could a change by a factor of ten in one driver plausibly change the reported quantity by that amount? Identify which omitted process would have the strongest effect if this toy calculation were used at sea. Explain why a precise printed number is not a measurement of exact physical truth.

### 5. Competing explanations, failure modes and observation quality

Saying that the Coriolis force makes water move right is incomplete without specifying velocity and hemisphere. An ideal geostrophic balance is invalid near the coast, in the equatorial band and where friction or acceleration is large.


### 6. Research procedure and reproducibility

Use the synthetic Unit 3 dataset to carry out a compact investigation. Begin by inspecting timestamps and units; then write one falsifiable prediction about **momentum budgets and coriolis acceleration**. Make a first plot of raw samples, mark missing or flagged records, and only afterward compute summary statistics. Repeat the summary after removing two extreme values and explain whether the conclusion changes. If the response is strongly depth-dependent, group observations by depth before averaging. A good lab submission includes the code or spreadsheet formulas, variable definitions, a figure with readable axes, and a one-paragraph argument that separates the observed pattern from its proposed cause.


### 7. Sensitivity, limits and transfer


**Short knowledge check:** State the direct observable for momentum budgets and coriolis acceleration, one mechanism compatible with it, one competing explanation, the units of the lesson’s calculation, and one measurement that would discriminate between the explanations. The response should contain at least one sentence explaining why the textbook’s simplified model is not by itself a site-specific forecast.

## Lesson 3.2 — Geostrophic flow and sea-surface slope

### 1. Physical question and core explanation

In the ocean interior, horizontal pressure gradients can balance the Coriolis force. Altimetry observes sea-surface height that is related to large-scale pressure gradients; absolute velocity still depends on reference fields and appropriate corrections. A few centimeters of slope can support appreciable current.


### 2. What to measure, and how

Use a sea-level difference across a known horizontal distance and a stated Coriolis parameter to estimate speed. State whether the height values are absolute dynamic topography or temporal anomalies.


### 3. Mechanism, model and dimensional reasoning

In a first approximation, represent **geostrophic flow and sea-surface slope** with an inventory, a forcing term and at least one route for exchange with surrounding water or the atmosphere. The model may be a proportionality, a conservative mixture, a flux balance, or a kinematic relation. Put units beside every variable before substituting measurements. A ratio of two volumes is dimensionless; a current is length per time; and a volume transport also includes cross-sectional area. If dimensions do not close, the numerical result cannot be correct even if a calculator produced it.


### 4. Fully worked quantitative case

**Problem — Geostrophic velocity magnitude.** Sea surface rises 0.2 m across 100 km at 40°N; estimate |u|=g|Δη/Δx|/|f|.

**Model and substitution:** `9.81*.2/(100000*(2*7.2921159e-5*math.sin(math.radians(40))))`. Evaluate it using the units stated in the problem and the accompanying conversion factors. The result is **0.20929 m/s**. Every multiplier or divisor should have a physical interpretation: cross-sectional area converts velocity to transport; elapsed time converts a rate to a stock change; a density or heat-capacity factor connects a thermodynamic state change to an energy inventory. For angular or exponent-based relationships, specify whether the input is degrees, radians or a dimensionless ratio.

**Interpretation:** Ignore wind, ageostrophic flow and reference-level corrections. The numerical answer belongs to a deliberately simplified scenario. Compare it against an order-of-magnitude estimate: could a change by a factor of ten in one driver plausibly change the reported quantity by that amount? Identify which omitted process would have the strongest effect if this toy calculation were used at sea. Explain why a precise printed number is not a measurement of exact physical truth.

### 5. Competing explanations, failure modes and observation quality

Geostrophic velocity computed from noisy differences can be unstable on small grids. Winds, tides, ageostrophic motion and unresolved coastline geometry must be separated before an altimetry map is converted to transport.


### 6. Research procedure and reproducibility

Use the synthetic Unit 3 dataset to carry out a compact investigation. Begin by inspecting timestamps and units; then write one falsifiable prediction about **geostrophic flow and sea-surface slope**. Make a first plot of raw samples, mark missing or flagged records, and only afterward compute summary statistics. Repeat the summary after removing two extreme values and explain whether the conclusion changes. If the response is strongly depth-dependent, group observations by depth before averaging. A good lab submission includes the code or spreadsheet formulas, variable definitions, a figure with readable axes, and a one-paragraph argument that separates the observed pattern from its proposed cause.


### 7. Sensitivity, limits and transfer


**Short knowledge check:** State the direct observable for geostrophic flow and sea-surface slope, one mechanism compatible with it, one competing explanation, the units of the lesson’s calculation, and one measurement that would discriminate between the explanations. The response should contain at least one sentence explaining why the textbook’s simplified model is not by itself a site-specific forecast.

## Lesson 3.3 — Ekman layers and upwelling

### 1. Physical question and core explanation

Wind stress drives a frictional surface boundary layer whose depth-integrated transport is approximately ninety degrees to the wind in an ideal steady rotating ocean. Alongshore winds can produce divergence or convergence at the coast and drive vertical motions. Real angles and layer depths depend on turbulence.


### 2. What to measure, and how

Combine a measured wind direction, hemisphere, coastline orientation and positive stress magnitude to predict the sign of coastal Ekman transport. Convert integrated transport into an illustrative vertical velocity using the width of the divergence zone.


### 3. Mechanism, model and dimensional reasoning

In a first approximation, represent **ekman layers and upwelling** with an inventory, a forcing term and at least one route for exchange with surrounding water or the atmosphere. The model may be a proportionality, a conservative mixture, a flux balance, or a kinematic relation. Put units beside every variable before substituting measurements. A ratio of two volumes is dimensionless; a current is length per time; and a volume transport also includes cross-sectional area. If dimensions do not close, the numerical result cannot be correct even if a calculator produced it.


### 4. Fully worked quantitative case

**Problem — Ekman transport per metre.** A surface stress magnitude of 0.1 N/m² at 45°N yields M=τ/(rho |f|), rho=1025.

**Model and substitution:** `.1/(1025*(2*7.2921159e-5*math.sin(math.radians(45))))`. Evaluate it using the units stated in the problem and the accompanying conversion factors. The result is **0.94604 m²/s**. Every multiplier or divisor should have a physical interpretation: cross-sectional area converts velocity to transport; elapsed time converts a rate to a stock change; a density or heat-capacity factor connects a thermodynamic state change to an energy inventory. For angular or exponent-based relationships, specify whether the input is degrees, radians or a dimensionless ratio.

**Interpretation:** This is depth-integrated volume transport per unit width. The numerical answer belongs to a deliberately simplified scenario. Compare it against an order-of-magnitude estimate: could a change by a factor of ten in one driver plausibly change the reported quantity by that amount? Identify which omitted process would have the strongest effect if this toy calculation were used at sea. Explain why a precise printed number is not a measurement of exact physical truth.

### 5. Competing explanations, failure modes and observation quality

The ideal Ekman spiral is not a universal observed pattern. Stratification, storms, vertical eddy viscosity and coastal geometry can reverse or mask short-term responses.


### 6. Research procedure and reproducibility

Use the synthetic Unit 3 dataset to carry out a compact investigation. Begin by inspecting timestamps and units; then write one falsifiable prediction about **ekman layers and upwelling**. Make a first plot of raw samples, mark missing or flagged records, and only afterward compute summary statistics. Repeat the summary after removing two extreme values and explain whether the conclusion changes. If the response is strongly depth-dependent, group observations by depth before averaging. A good lab submission includes the code or spreadsheet formulas, variable definitions, a figure with readable axes, and a one-paragraph argument that separates the observed pattern from its proposed cause.


### 7. Sensitivity, limits and transfer


**Short knowledge check:** State the direct observable for ekman layers and upwelling, one mechanism compatible with it, one competing explanation, the units of the lesson’s calculation, and one measurement that would discriminate between the explanations. The response should contain at least one sentence explaining why the textbook’s simplified model is not by itself a site-specific forecast.

## Lesson 3.4 — Gyres, western boundary currents and eddies

### 1. Physical question and core explanation

Basin winds and planetary vorticity produce subtropical and subpolar gyres. Conservation of potential vorticity helps explain western intensification; mesoscale eddies exchange heat, salt and momentum while complicating mean-flow maps. Mean circulation and eddy variability require different averaging scales.


### 2. What to measure, and how

Map synthetic drifter positions around a rotating eddy and infer rotation from sequential positions, not just a single sea-surface-height contour. Compare a seasonal mean velocity with individual drifter excursions.


### 3. Mechanism, model and dimensional reasoning

In a first approximation, represent **gyres, western boundary currents and eddies** with an inventory, a forcing term and at least one route for exchange with surrounding water or the atmosphere. The model may be a proportionality, a conservative mixture, a flux balance, or a kinematic relation. Put units beside every variable before substituting measurements. A ratio of two volumes is dimensionless; a current is length per time; and a volume transport also includes cross-sectional area. If dimensions do not close, the numerical result cannot be correct even if a calculator produced it.


### 4. Fully worked quantitative case

**Problem — Eddy orbital period.** A drifter orbits a feature of radius 30 km at speed 0.3 m/s. Estimate circumference travel time in days.

**Model and substitution:** `2*math.pi*30000/.3/86400`. Evaluate it using the units stated in the problem and the accompanying conversion factors. The result is **7.27221 days**. Every multiplier or divisor should have a physical interpretation: cross-sectional area converts velocity to transport; elapsed time converts a rate to a stock change; a density or heat-capacity factor connects a thermodynamic state change to an energy inventory. For angular or exponent-based relationships, specify whether the input is degrees, radians or a dimensionless ratio.

**Interpretation:** Not every eddy traps drifters on closed material paths. The numerical answer belongs to a deliberately simplified scenario. Compare it against an order-of-magnitude estimate: could a change by a factor of ten in one driver plausibly change the reported quantity by that amount? Identify which omitted process would have the strongest effect if this toy calculation were used at sea. Explain why a precise printed number is not a measurement of exact physical truth.

### 5. Competing explanations, failure modes and observation quality

A mesoscale eddy is not a rigid vortex, and altimetric contours do not always trace material boundaries. An inference about eddy heat transport also requires covariances rather than mean temperature and mean velocity alone.


### 6. Research procedure and reproducibility

Use the synthetic Unit 3 dataset to carry out a compact investigation. Begin by inspecting timestamps and units; then write one falsifiable prediction about **gyres, western boundary currents and eddies**. Make a first plot of raw samples, mark missing or flagged records, and only afterward compute summary statistics. Repeat the summary after removing two extreme values and explain whether the conclusion changes. If the response is strongly depth-dependent, group observations by depth before averaging. A good lab submission includes the code or spreadsheet formulas, variable definitions, a figure with readable axes, and a one-paragraph argument that separates the observed pattern from its proposed cause.


### 7. Sensitivity, limits and transfer


**Short knowledge check:** State the direct observable for gyres, western boundary currents and eddies, one mechanism compatible with it, one competing explanation, the units of the lesson’s calculation, and one measurement that would discriminate between the explanations. The response should contain at least one sentence explaining why the textbook’s simplified model is not by itself a site-specific forecast.

## Lesson 3.5 — Overturning circulation and deep water masses

### 1. Physical question and core explanation

Large-scale overturning combines dense-water formation, diapycnal mixing, winds and boundary pathways; it is not a literal single conveyor belt of uniform speed. Water-mass tracers constrain pathways and ventilation ages, while volume transports require coherent section integrals.


### 2. What to measure, and how

Construct a box diagram distinguishing surface heat and freshwater forcing from deep mixing and advective export. Compute a notional Sverdrup conversion, and show which sign corresponds to northward versus southward transport.


### 3. Mechanism, model and dimensional reasoning

In a first approximation, represent **overturning circulation and deep water masses** with an inventory, a forcing term and at least one route for exchange with surrounding water or the atmosphere. The model may be a proportionality, a conservative mixture, a flux balance, or a kinematic relation. Put units beside every variable before substituting measurements. A ratio of two volumes is dimensionless; a current is length per time; and a volume transport also includes cross-sectional area. If dimensions do not close, the numerical result cannot be correct even if a calculator produced it.


### 4. Fully worked quantitative case

**Problem — Sverdrup transport conversion.** Express a section transport of 25 million m³/s in Sverdrups.

**Model and substitution:** `25e6/1e6`. Evaluate it using the units stated in the problem and the accompanying conversion factors. The result is **25 Sv**. Every multiplier or divisor should have a physical interpretation: cross-sectional area converts velocity to transport; elapsed time converts a rate to a stock change; a density or heat-capacity factor connects a thermodynamic state change to an energy inventory. For angular or exponent-based relationships, specify whether the input is degrees, radians or a dimensionless ratio.

**Interpretation:** Sign and section orientation must be specified. The numerical answer belongs to a deliberately simplified scenario. Compare it against an order-of-magnitude estimate: could a change by a factor of ten in one driver plausibly change the reported quantity by that amount? Identify which omitted process would have the strongest effect if this toy calculation were used at sea. Explain why a precise printed number is not a measurement of exact physical truth.

### 5. Competing explanations, failure modes and observation quality

A regional freshening event does not by itself establish a permanent basin-scale circulation collapse. Sparse sections, strong eddies and changing reference levels require careful uncertainty estimates.


### 6. Research procedure and reproducibility

Use the synthetic Unit 3 dataset to carry out a compact investigation. Begin by inspecting timestamps and units; then write one falsifiable prediction about **overturning circulation and deep water masses**. Make a first plot of raw samples, mark missing or flagged records, and only afterward compute summary statistics. Repeat the summary after removing two extreme values and explain whether the conclusion changes. If the response is strongly depth-dependent, group observations by depth before averaging. A good lab submission includes the code or spreadsheet formulas, variable definitions, a figure with readable axes, and a one-paragraph argument that separates the observed pattern from its proposed cause.


### 7. Sensitivity, limits and transfer


**Short knowledge check:** State the direct observable for overturning circulation and deep water masses, one mechanism compatible with it, one competing explanation, the units of the lesson’s calculation, and one measurement that would discriminate between the explanations. The response should contain at least one sentence explaining why the textbook’s simplified model is not by itself a site-specific forecast.

## Integrated field investigation: joining the five lessons

**Research setting:** A drifter array is deployed across an eastern boundary upwelling zone while an altimeter maps a nearby eddy. The team must separate wind-driven motion from geostrophic flow and explain how uncertain reference velocities affect its transport estimate.

Begin by drawing an annotated cross-section of the hypothetical study domain. Mark the variables addressed in the five lessons: momentum budgets and coriolis acceleration, geostrophic flow and sea-surface slope, ekman layers and upwelling, gyres, western boundary currents and eddies, overturning circulation and deep water masses. State a hypothesis that predicts not only that two variables covary, but why a specified flux, force, mixing process or chemical transformation would connect them. If the hypothesized mechanism acts across a boundary, label that boundary with a direction arrow and correct units. If the hypothesis involves observational aliasing, describe which repeat sample would expose it.

Use the Unit 3 CSV as **fictional practice data**, not as empirical support. Calculate the mean, median, spread and a clearly chosen depth or time contrast. Fit a basic trend only after plotting raw values; a trend through a cyclic signal may depend on the starting and ending date. Draw uncertainty bars reflecting either an explicitly assumed sensor precision or the sample variability, and never call the two interchangeable. Rewrite one claim after noticing that an instrument was calibrated differently halfway through the experiment.

**Counterfactual:** Consider that the sampling route misses the location of maximum gradient. Estimate qualitatively whether a mean, a transport or an inventory would be biased upward or downward, and explain the sign. Then compare the consequences of doubling temporal cadence versus doubling spatial coverage. Select the cheaper improvement that tests the strongest competing explanation, even if it does not make the final map more visually attractive.

**Mini-report deliverables:** (1) a diagram with all coordinate and datum choices, (2) one calculation fully worked in SI units, (3) an independent check using a second observable, (4) a paragraph naming two uncertainties and whether they are random or systematic, and (5) a decision sentence that begins with the conditions under which the evidence is adequate. Good reasoning is judged by what could invalidate it, not by whether the synthetic plot looks smooth.

## Unit review and extension

Re-read the guiding question: Why do winds, pressure gradients and density fields produce distinct surface and deep circulations? Develop a two-column comparison between what the instruments directly measure and what the analyst hopes to infer. Explain at least three gaps between those columns. Reproduce the five solved exercises without looking at the results, and check the sensitivity of one result to a changed parameter. Demonstrate each unit model with the slider at its minimum, middle and maximum value. Finally, propose a new sampling site whose observation has the power to reject one interpretation, rather than simply providing more data of the same type.

A useful extension is to add a conservative tracer or reference measurement that responds to a different physical property. Observations become stronger when they have different failure mechanisms. A temperature record and an optical satellite product, for example, cannot replace a calibrated salinity profile, but together they may constrain a wider range of causal stories. Describe how the extension would change confidence and what inference remains beyond its reach.

### Interactive classroom model — Coriolis frequency

Change **latitude (degrees)** between -80 and 80 using the slider on the HTML reading page. The number displayed is in s⁻¹; first predict the direction of change from the equation, and then verify using the control. **Model limitation:** Spherical rigid Earth and local f-plane; no equatorial geostrophy.

A numerical graph is an invitation to test assumptions, not a replacement for a real observation. Try an extreme parameter setting, record whether it remains physically plausible, and name a missing mechanism. Explain how the simplified classroom response could be validated or invalidated with a real dataset.

### Interactive classroom model — Ideal sea-level-slope current

Change **sea-surface difference over 100 km (m)** between 0.01 and 1 using the slider on the HTML reading page. The number displayed is in m/s; first predict the direction of change from the equation, and then verify using the control. **Model limitation:** 40°N, steady geostrophic balance, ignores friction and atmospheric corrections.

A numerical graph is an invitation to test assumptions, not a replacement for a real observation. Try an extreme parameter setting, record whether it remains physically plausible, and name a missing mechanism. Explain how the simplified classroom response could be validated or invalidated with a real dataset.

