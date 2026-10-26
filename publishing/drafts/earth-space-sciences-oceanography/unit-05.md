# Unit 5 — Air–sea interaction and ocean climate

## Guiding question: How does the ocean store, redistribute and exchange climate-relevant energy?

**Synthetic case study:** A fictional subtropical observing station logs temperature profiles, satellite sea-surface height and surface flux estimates before and after a marine heatwave. Its investigators must establish whether changes reflect heating, advection, mixed-layer depth or sampling bias.

## Scientific foundations and the shape of the inquiry

The starting method in this unit is **heat budgets and climate interactions**. Express heat as a conserved inventory over a specified depth and area. A sea-surface trend is an indicator, not an integral through the entire ocean. Distinguish the direction of an air–sea flux from the net effect of all transport terms. Separate forced changes from internal variability using independent observations.

**Comparative interpretation:** Compare two synthetic years with the same annual-mean net flux but contrasting seasonal wind mixing. A deep winter mixed layer can distribute energy more broadly and alter the summer heatwave signature even when total surface energy input is similar.

**Fieldwork and model validation:** The ocean response to a heat flux depends on how much water is exposed to the forcing and where currents carry it. A change in temperature may occur despite a surface flux of the opposite sign if advection or entrainment dominates. Close a budget explicitly before describing an anomalous state as heat absorption.

Oceanographic quantities generally depend on the choice of reference frame and on the boundaries of the study region. A point sensor records conditions in a small volume; a gridded map estimates a field across many cells; a process model predicts how that field should change under specified equations and boundary conditions. A student who moves directly from a point sensor to a regional mechanism is making an extrapolation that requires independent support. Keep a table recording the proposed mechanism, the predicted pattern, and the observation that would undermine it. This practice prevents a persuasive figure from becoming an unsupported explanation.

The lesson sequence moves from describing observations to relating them to mechanisms, building a tractable calculation, testing sensitivity and finally explaining what action could justifiably follow. No numerical constant in a simplified teaching exercise should be mistaken for a globally fitted parameter. The numerical questions in this unit are deliberately synthetic; their main purpose is to expose the dimensional structure of the reasoning.

## Lesson 5.1 — Surface heat fluxes and bulk formulas

### 1. Physical question and core explanation

Net surface heat exchange combines solar radiation, longwave radiation, sensible heat and latent heat, with sign conventions stated. Evaporation transfers energy from the ocean into the atmosphere; warm ocean surfaces can fuel atmospheric convection. The same net flux warms a thin layer faster than a deep layer.


### 2. What to measure, and how

Calculate a temperature tendency from net flux, water density, heat capacity and mixed-layer thickness, then compare with a measured tendency. Assign the unexplained residual to unmeasured transport and mixing, not automatically to instrument failure.


### 3. Mechanism, model and dimensional reasoning

In a first approximation, represent **surface heat fluxes and bulk formulas** with an inventory, a forcing term and at least one route for exchange with surrounding water or the atmosphere. The model may be a proportionality, a conservative mixture, a flux balance, or a kinematic relation. Put units beside every variable before substituting measurements. A ratio of two volumes is dimensionless; a current is length per time; and a volume transport also includes cross-sectional area. If dimensions do not close, the numerical result cannot be correct even if a calculator produced it.


### 4. Fully worked quantitative case

**Problem — Mixed-layer heating per day.** For Q=85 W/m², rho=1025, cp=3990, H=40m find one-day temperature rise.

**Model and substitution:** `85*86400/(1025*3990*40)`. Evaluate it using the units stated in the problem and the accompanying conversion factors. The result is **0.04489 K/day**. Every multiplier or divisor should have a physical interpretation: cross-sectional area converts velocity to transport; elapsed time converts a rate to a stock change; a density or heat-capacity factor connects a thermodynamic state change to an energy inventory. For angular or exponent-based relationships, specify whether the input is degrees, radians or a dimensionless ratio.

**Interpretation:** No entrainment or advection in this classroom calculation. The numerical answer belongs to a deliberately simplified scenario. Compare it against an order-of-magnitude estimate: could a change by a factor of ten in one driver plausibly change the reported quantity by that amount? Identify which omitted process would have the strongest effect if this toy calculation were used at sea. Explain why a precise printed number is not a measurement of exact physical truth.

### 5. Competing explanations, failure modes and observation quality

Bulk flux coefficients and meteorological observations have uncertainty, especially during storms. Ignoring ocean advection and changing mixed-layer depth can make a heat-budget closure look better than warranted.


### 6. Research procedure and reproducibility

Use the synthetic Unit 5 dataset to carry out a compact investigation. Begin by inspecting timestamps and units; then write one falsifiable prediction about **surface heat fluxes and bulk formulas**. Make a first plot of raw samples, mark missing or flagged records, and only afterward compute summary statistics. Repeat the summary after removing two extreme values and explain whether the conclusion changes. If the response is strongly depth-dependent, group observations by depth before averaging. A good lab submission includes the code or spreadsheet formulas, variable definitions, a figure with readable axes, and a one-paragraph argument that separates the observed pattern from its proposed cause.


### 7. Sensitivity, limits and transfer


**Short knowledge check:** State the direct observable for surface heat fluxes and bulk formulas, one mechanism compatible with it, one competing explanation, the units of the lesson’s calculation, and one measurement that would discriminate between the explanations. The response should contain at least one sentence explaining why the textbook’s simplified model is not by itself a site-specific forecast.

## Lesson 5.2 — ENSO and tropical ocean coupling

### 1. Physical question and core explanation

The El Niño–Southern Oscillation arises from coupled tropical Pacific winds, thermocline adjustments and sea-surface-temperature anomalies. Equatorial waves redistribute thermocline depth. Regional climate effects depend on season and atmospheric teleconnections, not a deterministic single index.


### 2. What to measure, and how

Sketch how weakening trade winds can reduce equatorial upwelling and modify east-west thermal gradients. Compare a hypothetical eastern-Pacific SST index with wind anomalies while separating lagged association from proven causation.


### 3. Mechanism, model and dimensional reasoning

In a first approximation, represent **enso and tropical ocean coupling** with an inventory, a forcing term and at least one route for exchange with surrounding water or the atmosphere. The model may be a proportionality, a conservative mixture, a flux balance, or a kinematic relation. Put units beside every variable before substituting measurements. A ratio of two volumes is dimensionless; a current is length per time; and a volume transport also includes cross-sectional area. If dimensions do not close, the numerical result cannot be correct even if a calculator produced it.


### 4. Fully worked quantitative case

**Problem — Equatorial speed scale.** A signal covers 1,200 km in 20 days. Compute mean speed.

**Model and substitution:** `1200000/(20*86400)`. Evaluate it using the units stated in the problem and the accompanying conversion factors. The result is **0.69444 m/s**. Every multiplier or divisor should have a physical interpretation: cross-sectional area converts velocity to transport; elapsed time converts a rate to a stock change; a density or heat-capacity factor connects a thermodynamic state change to an energy inventory. For angular or exponent-based relationships, specify whether the input is degrees, radians or a dimensionless ratio.

**Interpretation:** A kinematic travel speed alone does not identify an equatorial-wave mode. The numerical answer belongs to a deliberately simplified scenario. Compare it against an order-of-magnitude estimate: could a change by a factor of ten in one driver plausibly change the reported quantity by that amount? Identify which omitted process would have the strongest effect if this toy calculation were used at sea. Explain why a precise printed number is not a measurement of exact physical truth.

### 5. Competing explanations, failure modes and observation quality

One warm equatorial month is not a complete ENSO event diagnosis. Spatial pattern, duration, thresholds, index definitions and background climate state determine classifications.


### 6. Research procedure and reproducibility

Use the synthetic Unit 5 dataset to carry out a compact investigation. Begin by inspecting timestamps and units; then write one falsifiable prediction about **enso and tropical ocean coupling**. Make a first plot of raw samples, mark missing or flagged records, and only afterward compute summary statistics. Repeat the summary after removing two extreme values and explain whether the conclusion changes. If the response is strongly depth-dependent, group observations by depth before averaging. A good lab submission includes the code or spreadsheet formulas, variable definitions, a figure with readable axes, and a one-paragraph argument that separates the observed pattern from its proposed cause.


### 7. Sensitivity, limits and transfer


**Short knowledge check:** State the direct observable for enso and tropical ocean coupling, one mechanism compatible with it, one competing explanation, the units of the lesson’s calculation, and one measurement that would discriminate between the explanations. The response should contain at least one sentence explaining why the textbook’s simplified model is not by itself a site-specific forecast.

## Lesson 5.3 — Sea level: steric change, mass and vertical land motion

### 1. Physical question and core explanation

Relative sea level at a tide gauge combines ocean height and local land motion. Satellite altimetry measures height relative to a reference system; steric expansion and ocean mass redistribution contribute to global changes. Coastal flood risk also depends on tides, storm surge and subsidence.


### 2. What to measure, and how

Convert a simplified ocean thermal expansion coefficient times temperature change and layer thickness into steric height. Contrast this estimate with a tide-gauge relative trend under an assumed subsidence rate.


### 3. Mechanism, model and dimensional reasoning

In a first approximation, represent **sea level: steric change, mass and vertical land motion** with an inventory, a forcing term and at least one route for exchange with surrounding water or the atmosphere. The model may be a proportionality, a conservative mixture, a flux balance, or a kinematic relation. Put units beside every variable before substituting measurements. A ratio of two volumes is dimensionless; a current is length per time; and a volume transport also includes cross-sectional area. If dimensions do not close, the numerical result cannot be correct even if a calculator produced it.


### 4. Fully worked quantitative case

**Problem — Steric sea-level proxy.** For α=2e−4 K−1, warming=1.5 K, layer=700 m calculate steric height.

**Model and substitution:** `2e-4*1.5*700`. Evaluate it using the units stated in the problem and the accompanying conversion factors. The result is **0.21 m**. Every multiplier or divisor should have a physical interpretation: cross-sectional area converts velocity to transport; elapsed time converts a rate to a stock change; a density or heat-capacity factor connects a thermodynamic state change to an energy inventory. For angular or exponent-based relationships, specify whether the input is degrees, radians or a dimensionless ratio.

**Interpretation:** Assumes constant expansion coefficient across the entire layer. The numerical answer belongs to a deliberately simplified scenario. Compare it against an order-of-magnitude estimate: could a change by a factor of ten in one driver plausibly change the reported quantity by that amount? Identify which omitted process would have the strongest effect if this toy calculation were used at sea. Explain why a precise printed number is not a measurement of exact physical truth.

### 5. Competing explanations, failure modes and observation quality

Steric expansion varies strongly with temperature, salinity and depth. A satellite global mean cannot substitute for local coastal risk assessment or for land-level monitoring.


### 6. Research procedure and reproducibility

Use the synthetic Unit 5 dataset to carry out a compact investigation. Begin by inspecting timestamps and units; then write one falsifiable prediction about **sea level: steric change, mass and vertical land motion**. Make a first plot of raw samples, mark missing or flagged records, and only afterward compute summary statistics. Repeat the summary after removing two extreme values and explain whether the conclusion changes. If the response is strongly depth-dependent, group observations by depth before averaging. A good lab submission includes the code or spreadsheet formulas, variable definitions, a figure with readable axes, and a one-paragraph argument that separates the observed pattern from its proposed cause.


### 7. Sensitivity, limits and transfer


**Short knowledge check:** State the direct observable for sea level: steric change, mass and vertical land motion, one mechanism compatible with it, one competing explanation, the units of the lesson’s calculation, and one measurement that would discriminate between the explanations. The response should contain at least one sentence explaining why the textbook’s simplified model is not by itself a site-specific forecast.

## Lesson 5.4 — Ocean heat content and marine heatwaves

### 1. Physical question and core explanation

Ocean heat content integrates temperature changes across volume and has different meaning from a surface-only temperature anomaly. Marine heatwaves are often defined relative to seasonal local percentiles and duration criteria. Their biological impact depends on depth, rate of change and ecological sensitivity.


### 2. What to measure, and how

Integrate a two-layer heat anomaly and compare the result with a one-layer proxy. Define a toy percentile threshold from a synthetic baseline and count consecutive exceedance days.


### 3. Mechanism, model and dimensional reasoning

In a first approximation, represent **ocean heat content and marine heatwaves** with an inventory, a forcing term and at least one route for exchange with surrounding water or the atmosphere. The model may be a proportionality, a conservative mixture, a flux balance, or a kinematic relation. Put units beside every variable before substituting measurements. A ratio of two volumes is dimensionless; a current is length per time; and a volume transport also includes cross-sectional area. If dimensions do not close, the numerical result cannot be correct even if a calculator produced it.


### 4. Fully worked quantitative case

**Problem — Two-layer heat anomaly.** Upper 20 m warms 2 K and next 80 m warms 0.25 K. Compute heat per m² with constant rho/cp.

**Model and substitution:** `1025*3990*(20*2+80*.25)`. Evaluate it using the units stated in the problem and the accompanying conversion factors. The result is **2.4538e+08 J/m²**. Every multiplier or divisor should have a physical interpretation: cross-sectional area converts velocity to transport; elapsed time converts a rate to a stock change; a density or heat-capacity factor connects a thermodynamic state change to an energy inventory. For angular or exponent-based relationships, specify whether the input is degrees, radians or a dimensionless ratio.

**Interpretation:** The calculation is a heat anomaly relative to a baseline. The numerical answer belongs to a deliberately simplified scenario. Compare it against an order-of-magnitude estimate: could a change by a factor of ten in one driver plausibly change the reported quantity by that amount? Identify which omitted process would have the strongest effect if this toy calculation were used at sea. Explain why a precise printed number is not a measurement of exact physical truth.

### 5. Competing explanations, failure modes and observation quality

A short warm anomaly does not by itself reveal the source of extra heat. Changes in currents, stratification, vertical mixing and instrument sampling all contribute.


### 6. Research procedure and reproducibility

Use the synthetic Unit 5 dataset to carry out a compact investigation. Begin by inspecting timestamps and units; then write one falsifiable prediction about **ocean heat content and marine heatwaves**. Make a first plot of raw samples, mark missing or flagged records, and only afterward compute summary statistics. Repeat the summary after removing two extreme values and explain whether the conclusion changes. If the response is strongly depth-dependent, group observations by depth before averaging. A good lab submission includes the code or spreadsheet formulas, variable definitions, a figure with readable axes, and a one-paragraph argument that separates the observed pattern from its proposed cause.


### 7. Sensitivity, limits and transfer


**Short knowledge check:** State the direct observable for ocean heat content and marine heatwaves, one mechanism compatible with it, one competing explanation, the units of the lesson’s calculation, and one measurement that would discriminate between the explanations. The response should contain at least one sentence explaining why the textbook’s simplified model is not by itself a site-specific forecast.

## Lesson 5.5 — Polar oceans, sea ice and freshwater forcing

### 1. Physical question and core explanation

Sea ice reflects solar radiation, insulates the ocean and modifies near-surface freshwater and salinity budgets. Freezing generally rejects salt into surrounding seawater; melting can cap deeper water with a fresher layer. Polar shelf processes contribute to dense-water production and ice-shelf interaction.


### 2. What to measure, and how

Write separate salt and heat budgets for an ice-covered upper-ocean box. Compare an idealized freshwater pulse with cooling-driven density change using a clearly marked approximate relationship.


### 3. Mechanism, model and dimensional reasoning

In a first approximation, represent **polar oceans, sea ice and freshwater forcing** with an inventory, a forcing term and at least one route for exchange with surrounding water or the atmosphere. The model may be a proportionality, a conservative mixture, a flux balance, or a kinematic relation. Put units beside every variable before substituting measurements. A ratio of two volumes is dimensionless; a current is length per time; and a volume transport also includes cross-sectional area. If dimensions do not close, the numerical result cannot be correct even if a calculator produced it.


### 4. Fully worked quantitative case

**Problem — Ice-free freshwater salinity budget.** A box with 1000 kg of 35 g/kg seawater receives 100 kg freshwater. Estimate mixed salinity.

**Model and substitution:** `35*1000/1100`. Evaluate it using the units stated in the problem and the accompanying conversion factors. The result is **31.81818 g/kg**. Every multiplier or divisor should have a physical interpretation: cross-sectional area converts velocity to transport; elapsed time converts a rate to a stock change; a density or heat-capacity factor connects a thermodynamic state change to an energy inventory. For angular or exponent-based relationships, specify whether the input is degrees, radians or a dimensionless ratio.

**Interpretation:** Assumes mass conservation of salt and complete instantaneous mixing. The numerical answer belongs to a deliberately simplified scenario. Compare it against an order-of-magnitude estimate: could a change by a factor of ten in one driver plausibly change the reported quantity by that amount? Identify which omitted process would have the strongest effect if this toy calculation were used at sea. Explain why a precise printed number is not a measurement of exact physical truth.

### 5. Competing explanations, failure modes and observation quality

Volume of ice, mass of meltwater and resulting sea-level change are not interchangeable quantities. The density of seawater and ice and whether the ice was floating matter to the water-level budget.


### 6. Research procedure and reproducibility

Use the synthetic Unit 5 dataset to carry out a compact investigation. Begin by inspecting timestamps and units; then write one falsifiable prediction about **polar oceans, sea ice and freshwater forcing**. Make a first plot of raw samples, mark missing or flagged records, and only afterward compute summary statistics. Repeat the summary after removing two extreme values and explain whether the conclusion changes. If the response is strongly depth-dependent, group observations by depth before averaging. A good lab submission includes the code or spreadsheet formulas, variable definitions, a figure with readable axes, and a one-paragraph argument that separates the observed pattern from its proposed cause.


### 7. Sensitivity, limits and transfer


**Short knowledge check:** State the direct observable for polar oceans, sea ice and freshwater forcing, one mechanism compatible with it, one competing explanation, the units of the lesson’s calculation, and one measurement that would discriminate between the explanations. The response should contain at least one sentence explaining why the textbook’s simplified model is not by itself a site-specific forecast.

## Integrated field investigation: joining the five lessons

**Research setting:** A fictional subtropical observing station logs temperature profiles, satellite sea-surface height and surface flux estimates before and after a marine heatwave. Its investigators must establish whether changes reflect heating, advection, mixed-layer depth or sampling bias.

Begin by drawing an annotated cross-section of the hypothetical study domain. Mark the variables addressed in the five lessons: surface heat fluxes and bulk formulas, enso and tropical ocean coupling, sea level: steric change, mass and vertical land motion, ocean heat content and marine heatwaves, polar oceans, sea ice and freshwater forcing. State a hypothesis that predicts not only that two variables covary, but why a specified flux, force, mixing process or chemical transformation would connect them. If the hypothesized mechanism acts across a boundary, label that boundary with a direction arrow and correct units. If the hypothesis involves observational aliasing, describe which repeat sample would expose it.

Use the Unit 5 CSV as **fictional practice data**, not as empirical support. Calculate the mean, median, spread and a clearly chosen depth or time contrast. Fit a basic trend only after plotting raw values; a trend through a cyclic signal may depend on the starting and ending date. Draw uncertainty bars reflecting either an explicitly assumed sensor precision or the sample variability, and never call the two interchangeable. Rewrite one claim after noticing that an instrument was calibrated differently halfway through the experiment.

**Counterfactual:** Consider that the sampling route misses the location of maximum gradient. Estimate qualitatively whether a mean, a transport or an inventory would be biased upward or downward, and explain the sign. Then compare the consequences of doubling temporal cadence versus doubling spatial coverage. Select the cheaper improvement that tests the strongest competing explanation, even if it does not make the final map more visually attractive.

**Mini-report deliverables:** (1) a diagram with all coordinate and datum choices, (2) one calculation fully worked in SI units, (3) an independent check using a second observable, (4) a paragraph naming two uncertainties and whether they are random or systematic, and (5) a decision sentence that begins with the conditions under which the evidence is adequate. Good reasoning is judged by what could invalidate it, not by whether the synthetic plot looks smooth.

## Unit review and extension

Re-read the guiding question: How does the ocean store, redistribute and exchange climate-relevant energy? Develop a two-column comparison between what the instruments directly measure and what the analyst hopes to infer. Explain at least three gaps between those columns. Reproduce the five solved exercises without looking at the results, and check the sensitivity of one result to a changed parameter. Demonstrate each unit model with the slider at its minimum, middle and maximum value. Finally, propose a new sampling site whose observation has the power to reject one interpretation, rather than simply providing more data of the same type.

A useful extension is to add a conservative tracer or reference measurement that responds to a different physical property. Observations become stronger when they have different failure mechanisms. A temperature record and an optical satellite product, for example, cannot replace a calibrated salinity profile, but together they may constrain a wider range of causal stories. Describe how the extension would change confidence and what inference remains beyond its reach.

### Interactive classroom model — Surface-flux-driven temperature tendency

Change **net flux (w/m²)** between -250 and 250 using the slider on the HTML reading page. The number displayed is in K/day; first predict the direction of change from the equation, and then verify using the control. **Model limitation:** Forty-meter mixed layer fixed; no vertical entrainment or advection.

A numerical graph is an invitation to test assumptions, not a replacement for a real observation. Try an extreme parameter setting, record whether it remains physically plausible, and name a missing mechanism. Explain how the simplified classroom response could be validated or invalidated with a real dataset.

### Interactive classroom model — Simplified thermal expansion contribution

Change **layer warming (k)** between 0 and 5 using the slider on the HTML reading page. The number displayed is in m; first predict the direction of change from the equation, and then verify using the control. **Model limitation:** Constant expansion coefficient and a 700 m layer; nonuniform real ocean.

A numerical graph is an invitation to test assumptions, not a replacement for a real observation. Try an extreme parameter setting, record whether it remains physically plausible, and name a missing mechanism. Explain how the simplified classroom response could be validated or invalidated with a real dataset.

