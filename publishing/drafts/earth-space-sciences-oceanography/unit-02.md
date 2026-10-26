# Unit 2 — Seawater properties and vertical structure

## Guiding question: How can salt, heat, compression and turbulence create layered fluid bodies?

**Synthetic case study:** An autonomous float crosses a warm surface lens after rain and then visits a colder, saltier water mass. Students must decide whether the apparent density gradient is physical and whether it inhibits vertical transport of nutrients and heat.

## Scientific foundations and the shape of the inquiry

The starting method in this unit is **thermodynamics and stratification**. Identify whether the quantity is a concentration, a specific property, or an extensive inventory. Density and salinity require explicit reference conventions. Use depth-positive-downward coordinates consistently, and do not interpret pressure-induced in-situ density changes as instability.

**Comparative interpretation:** Contrast a shallow fresh cap with a cold saline deep profile. Two water columns can have the same sea-surface temperature but very different integrated heat storage and buoyancy barriers, leading to different responses to an identical afternoon wind event.

**Fieldwork and model validation:** Sampling time is part of the physical coordinate: a ship section taken over several days can mix genuine horizontal gradients with changes caused by tides, fronts or storms. Examine reproducibility with repeat casts, and use temperature-salinity or density coordinates when depth coordinates alone are misleading.

Oceanographic quantities generally depend on the choice of reference frame and on the boundaries of the study region. A point sensor records conditions in a small volume; a gridded map estimates a field across many cells; a process model predicts how that field should change under specified equations and boundary conditions. A student who moves directly from a point sensor to a regional mechanism is making an extrapolation that requires independent support. Keep a table recording the proposed mechanism, the predicted pattern, and the observation that would undermine it. This practice prevents a persuasive figure from becoming an unsupported explanation.

The lesson sequence moves from describing observations to relating them to mechanisms, building a tractable calculation, testing sensitivity and finally explaining what action could justifiably follow. No numerical constant in a simplified teaching exercise should be mistaken for a globally fitted parameter. The numerical questions in this unit are deliberately synthetic; their main purpose is to expose the dimensional structure of the reasoning.

## Lesson 2.1 — Salinity and water-mass fingerprints

### 1. Physical question and core explanation

Salinity expresses dissolved salts relative to seawater mass or conductivity-based standards, not a universal fixed composition at every site. Freshwater input, evaporation, sea-ice formation and mixing alter salinity. Temperature-salinity diagrams help identify plausible endmembers, but different histories can produce similar points.


### 2. What to measure, and how

Use paired temperature and conductivity measurements to place each depth on a T–S plot. Compare candidate surface and deep endmembers, and calculate a linear mixture fraction only where conservation and consistent units are defensible.


### 3. Mechanism, model and dimensional reasoning

In a first approximation, represent **salinity and water-mass fingerprints** with an inventory, a forcing term and at least one route for exchange with surrounding water or the atmosphere. The model may be a proportionality, a conservative mixture, a flux balance, or a kinematic relation. Put units beside every variable before substituting measurements. A ratio of two volumes is dimensionless; a current is length per time; and a volume transport also includes cross-sectional area. If dimensions do not close, the numerical result cannot be correct even if a calculator produced it.


### 4. Fully worked quantitative case

**Problem — Conservative salinity mixture.** Mix 40% 30 g/kg water and 60% 35 g/kg water by mass. Compute salinity.

**Model and substitution:** `.4*30+.6*35`. Evaluate it using the units stated in the problem and the accompanying conversion factors. The result is **33 g/kg**. Every multiplier or divisor should have a physical interpretation: cross-sectional area converts velocity to transport; elapsed time converts a rate to a stock change; a density or heat-capacity factor connects a thermodynamic state change to an energy inventory. For angular or exponent-based relationships, specify whether the input is degrees, radians or a dimensionless ratio.

**Interpretation:** Use mass fraction, not volume, for this linear illustration. The numerical answer belongs to a deliberately simplified scenario. Compare it against an order-of-magnitude estimate: could a change by a factor of ten in one driver plausibly change the reported quantity by that amount? Identify which omitted process would have the strongest effect if this toy calculation were used at sea. Explain why a precise printed number is not a measurement of exact physical truth.

### 5. Competing explanations, failure modes and observation quality

Conductivity calibrations and practical-versus-absolute salinity conventions matter when comparing instruments. A straight mixing line cannot prove that only two source waters contributed.


### 6. Research procedure and reproducibility

Use the synthetic Unit 2 dataset to carry out a compact investigation. Begin by inspecting timestamps and units; then write one falsifiable prediction about **salinity and water-mass fingerprints**. Make a first plot of raw samples, mark missing or flagged records, and only afterward compute summary statistics. Repeat the summary after removing two extreme values and explain whether the conclusion changes. If the response is strongly depth-dependent, group observations by depth before averaging. A good lab submission includes the code or spreadsheet formulas, variable definitions, a figure with readable axes, and a one-paragraph argument that separates the observed pattern from its proposed cause.


### 7. Sensitivity, limits and transfer


**Short knowledge check:** State the direct observable for salinity and water-mass fingerprints, one mechanism compatible with it, one competing explanation, the units of the lesson’s calculation, and one measurement that would discriminate between the explanations. The response should contain at least one sentence explaining why the textbook’s simplified model is not by itself a site-specific forecast.

## Lesson 2.2 — Temperature, pressure and heat capacity

### 1. Physical question and core explanation

Temperature measured at depth is affected by pressure; potential or Conservative Temperature is useful for tracking water masses and heat budgets. The ocean stores large amounts of energy because seawater has high heat capacity and immense volume. Temperature trends must specify area and depth.


### 2. What to measure, and how

Integrate approximate rho*c_p*deltaT*layer-thickness over an idealized grid cell, then compare with surface heat-flux input. Make clear whether the result is heat per unit area or total heat.


### 3. Mechanism, model and dimensional reasoning

In a first approximation, represent **temperature, pressure and heat capacity** with an inventory, a forcing term and at least one route for exchange with surrounding water or the atmosphere. The model may be a proportionality, a conservative mixture, a flux balance, or a kinematic relation. Put units beside every variable before substituting measurements. A ratio of two volumes is dimensionless; a current is length per time; and a volume transport also includes cross-sectional area. If dimensions do not close, the numerical result cannot be correct even if a calculator produced it.


### 4. Fully worked quantitative case

**Problem — Simple heat content anomaly.** Calculate energy per m² for a 50 m layer warmed 1.2 K with rho=1025 kg/m³ and cp=3990 J/kg/K.

**Model and substitution:** `1025*3990*50*1.2`. Evaluate it using the units stated in the problem and the accompanying conversion factors. The result is **2.4538e+08 J/m²**. Every multiplier or divisor should have a physical interpretation: cross-sectional area converts velocity to transport; elapsed time converts a rate to a stock change; a density or heat-capacity factor connects a thermodynamic state change to an energy inventory. For angular or exponent-based relationships, specify whether the input is degrees, radians or a dimensionless ratio.

**Interpretation:** The slab approximation neglects density and cp variations. The numerical answer belongs to a deliberately simplified scenario. Compare it against an order-of-magnitude estimate: could a change by a factor of ten in one driver plausibly change the reported quantity by that amount? Identify which omitted process would have the strongest effect if this toy calculation were used at sea. Explain why a precise printed number is not a measurement of exact physical truth.

### 5. Competing explanations, failure modes and observation quality

Treating all layers as identical density, salinity and heat capacity is an approximation. The wrong pressure convention or an unrepresentative seasonal profile can dominate a small estimated heat-change signal.


### 6. Research procedure and reproducibility

Use the synthetic Unit 2 dataset to carry out a compact investigation. Begin by inspecting timestamps and units; then write one falsifiable prediction about **temperature, pressure and heat capacity**. Make a first plot of raw samples, mark missing or flagged records, and only afterward compute summary statistics. Repeat the summary after removing two extreme values and explain whether the conclusion changes. If the response is strongly depth-dependent, group observations by depth before averaging. A good lab submission includes the code or spreadsheet formulas, variable definitions, a figure with readable axes, and a one-paragraph argument that separates the observed pattern from its proposed cause.


### 7. Sensitivity, limits and transfer


**Short knowledge check:** State the direct observable for temperature, pressure and heat capacity, one mechanism compatible with it, one competing explanation, the units of the lesson’s calculation, and one measurement that would discriminate between the explanations. The response should contain at least one sentence explaining why the textbook’s simplified model is not by itself a site-specific forecast.

## Lesson 2.3 — Equation of state and density stratification

### 1. Physical question and core explanation

Seawater density depends on temperature, salinity and pressure; cooling and salinification usually increase surface density within common ocean ranges. Compressibility means the in-situ density increases with depth even without a dynamically unstable stratification. Potential density referenced to a specified pressure helps compare water parcels.


### 2. What to measure, and how

Inspect a profile for temperature and salinity compensation. Compute a local linear density anomaly as a transparent classroom approximation, then check the sign of stable stratification under an appropriate reference pressure.


### 3. Mechanism, model and dimensional reasoning

In a first approximation, represent **equation of state and density stratification** with an inventory, a forcing term and at least one route for exchange with surrounding water or the atmosphere. The model may be a proportionality, a conservative mixture, a flux balance, or a kinematic relation. Put units beside every variable before substituting measurements. A ratio of two volumes is dimensionless; a current is length per time; and a volume transport also includes cross-sectional area. If dimensions do not close, the numerical result cannot be correct even if a calculator produced it.


### 4. Fully worked quantitative case

**Problem — Linear surface density anomaly.** Use rho=1025−0.2ΔT+0.8ΔS kg/m³, with ΔT=3 K and ΔS=0.5 g/kg.

**Model and substitution:** `1025-.2*3+.8*.5`. Evaluate it using the units stated in the problem and the accompanying conversion factors. The result is **1024.8 kg/m³**. Every multiplier or divisor should have a physical interpretation: cross-sectional area converts velocity to transport; elapsed time converts a rate to a stock change; a density or heat-capacity factor connects a thermodynamic state change to an energy inventory. For angular or exponent-based relationships, specify whether the input is degrees, radians or a dimensionless ratio.

**Interpretation:** A teaching approximation, not TEOS-10 seawater thermodynamics. The numerical answer belongs to a deliberately simplified scenario. Compare it against an order-of-magnitude estimate: could a change by a factor of ten in one driver plausibly change the reported quantity by that amount? Identify which omitted process would have the strongest effect if this toy calculation were used at sea. Explain why a precise printed number is not a measurement of exact physical truth.

### 5. Competing explanations, failure modes and observation quality

A linear equation of state is not accurate for all temperatures, salinities and depths. Comparing in-situ density at different pressures can create a false inference about whether overturning will occur.


### 6. Research procedure and reproducibility

Use the synthetic Unit 2 dataset to carry out a compact investigation. Begin by inspecting timestamps and units; then write one falsifiable prediction about **equation of state and density stratification**. Make a first plot of raw samples, mark missing or flagged records, and only afterward compute summary statistics. Repeat the summary after removing two extreme values and explain whether the conclusion changes. If the response is strongly depth-dependent, group observations by depth before averaging. A good lab submission includes the code or spreadsheet formulas, variable definitions, a figure with readable axes, and a one-paragraph argument that separates the observed pattern from its proposed cause.


### 7. Sensitivity, limits and transfer


**Short knowledge check:** State the direct observable for equation of state and density stratification, one mechanism compatible with it, one competing explanation, the units of the lesson’s calculation, and one measurement that would discriminate between the explanations. The response should contain at least one sentence explaining why the textbook’s simplified model is not by itself a site-specific forecast.

## Lesson 2.4 — Pycnoclines, buoyancy frequency and mixing

### 1. Physical question and core explanation

A pycnocline is a zone of strong vertical density gradient that can resist vertical displacement. Buoyancy frequency links stable stratification to the restoring force on a displaced parcel. Wind stirring, convection and internal-wave breaking redistribute properties across a gradient.


### 2. What to measure, and how

Estimate N-squared from a reference-density gradient using centered differences, with z positive upward or depth positive downward declared explicitly. Check the sign convention using a known stable profile.


### 3. Mechanism, model and dimensional reasoning

In a first approximation, represent **pycnoclines, buoyancy frequency and mixing** with an inventory, a forcing term and at least one route for exchange with surrounding water or the atmosphere. The model may be a proportionality, a conservative mixture, a flux balance, or a kinematic relation. Put units beside every variable before substituting measurements. A ratio of two volumes is dimensionless; a current is length per time; and a volume transport also includes cross-sectional area. If dimensions do not close, the numerical result cannot be correct even if a calculator produced it.


### 4. Fully worked quantitative case

**Problem — Buoyancy frequency squared.** Use N²=(g/rho0)(Δrho/Δdepth) for density increase 0.8 kg/m³ over 40 m, rho0=1025.

**Model and substitution:** `9.81/1025*.8/40`. Evaluate it using the units stated in the problem and the accompanying conversion factors. The result is **0.00019141 s⁻²**. Every multiplier or divisor should have a physical interpretation: cross-sectional area converts velocity to transport; elapsed time converts a rate to a stock change; a density or heat-capacity factor connects a thermodynamic state change to an energy inventory. For angular or exponent-based relationships, specify whether the input is degrees, radians or a dimensionless ratio.

**Interpretation:** Depth is positive downward, hence the positive stable sign. The numerical answer belongs to a deliberately simplified scenario. Compare it against an order-of-magnitude estimate: could a change by a factor of ten in one driver plausibly change the reported quantity by that amount? Identify which omitted process would have the strongest effect if this toy calculation were used at sea. Explain why a precise printed number is not a measurement of exact physical truth.

### 5. Competing explanations, failure modes and observation quality

A five-meter averaging interval can miss a thin barrier layer. Negative N-squared from noisy sensors may be a calibration artifact rather than a real overturn, so resolution and error propagation are essential.


### 6. Research procedure and reproducibility

Use the synthetic Unit 2 dataset to carry out a compact investigation. Begin by inspecting timestamps and units; then write one falsifiable prediction about **pycnoclines, buoyancy frequency and mixing**. Make a first plot of raw samples, mark missing or flagged records, and only afterward compute summary statistics. Repeat the summary after removing two extreme values and explain whether the conclusion changes. If the response is strongly depth-dependent, group observations by depth before averaging. A good lab submission includes the code or spreadsheet formulas, variable definitions, a figure with readable axes, and a one-paragraph argument that separates the observed pattern from its proposed cause.


### 7. Sensitivity, limits and transfer


**Short knowledge check:** State the direct observable for pycnoclines, buoyancy frequency and mixing, one mechanism compatible with it, one competing explanation, the units of the lesson’s calculation, and one measurement that would discriminate between the explanations. The response should contain at least one sentence explaining why the textbook’s simplified model is not by itself a site-specific forecast.

## Lesson 2.5 — Mixed layers, freshwater lenses and convection

### 1. Physical question and core explanation

The ocean mixed layer emerges through surface forcing and turbulence, but its depth depends on the diagnostic threshold used. Rapid rainfall creates shallow low-salinity lenses; winter heat loss can deepen mixing. Entrainment at the layer base changes temperature even without direct surface heating.


### 2. What to measure, and how

Compute a mixed-layer heat budget and compare two depth thresholds on the same cast. Use an idealized freshwater pulse to trace salinity dilution in a fixed-volume box before including entrainment.


### 3. Mechanism, model and dimensional reasoning

In a first approximation, represent **mixed layers, freshwater lenses and convection** with an inventory, a forcing term and at least one route for exchange with surrounding water or the atmosphere. The model may be a proportionality, a conservative mixture, a flux balance, or a kinematic relation. Put units beside every variable before substituting measurements. A ratio of two volumes is dimensionless; a current is length per time; and a volume transport also includes cross-sectional area. If dimensions do not close, the numerical result cannot be correct even if a calculator produced it.


### 4. Fully worked quantitative case

**Problem — Heating fixed mixed layer.** 70 W/m² sustained 30 days warms a 40 m slab. Find ΔT with rho=1025 and cp=3990.

**Model and substitution:** `70*30*86400/(1025*3990*40)`. Evaluate it using the units stated in the problem and the accompanying conversion factors. The result is **1.10911 K**. Every multiplier or divisor should have a physical interpretation: cross-sectional area converts velocity to transport; elapsed time converts a rate to a stock change; a density or heat-capacity factor connects a thermodynamic state change to an energy inventory. For angular or exponent-based relationships, specify whether the input is degrees, radians or a dimensionless ratio.

**Interpretation:** Neglect entrainment and horizontal heat transport. The numerical answer belongs to a deliberately simplified scenario. Compare it against an order-of-magnitude estimate: could a change by a factor of ten in one driver plausibly change the reported quantity by that amount? Identify which omitted process would have the strongest effect if this toy calculation were used at sea. Explain why a precise printed number is not a measurement of exact physical truth.

### 5. Competing explanations, failure modes and observation quality

Assuming a constant layer thickness may be useful for a one-hour exercise but inappropriate for seasonal prediction. Horizontal advection, entrainment and short-lived rainfall can produce misleading surface trends.


### 6. Research procedure and reproducibility

Use the synthetic Unit 2 dataset to carry out a compact investigation. Begin by inspecting timestamps and units; then write one falsifiable prediction about **mixed layers, freshwater lenses and convection**. Make a first plot of raw samples, mark missing or flagged records, and only afterward compute summary statistics. Repeat the summary after removing two extreme values and explain whether the conclusion changes. If the response is strongly depth-dependent, group observations by depth before averaging. A good lab submission includes the code or spreadsheet formulas, variable definitions, a figure with readable axes, and a one-paragraph argument that separates the observed pattern from its proposed cause.


### 7. Sensitivity, limits and transfer


**Short knowledge check:** State the direct observable for mixed layers, freshwater lenses and convection, one mechanism compatible with it, one competing explanation, the units of the lesson’s calculation, and one measurement that would discriminate between the explanations. The response should contain at least one sentence explaining why the textbook’s simplified model is not by itself a site-specific forecast.

## Integrated field investigation: joining the five lessons

**Research setting:** An autonomous float crosses a warm surface lens after rain and then visits a colder, saltier water mass. Students must decide whether the apparent density gradient is physical and whether it inhibits vertical transport of nutrients and heat.

Begin by drawing an annotated cross-section of the hypothetical study domain. Mark the variables addressed in the five lessons: salinity and water-mass fingerprints, temperature, pressure and heat capacity, equation of state and density stratification, pycnoclines, buoyancy frequency and mixing, mixed layers, freshwater lenses and convection. State a hypothesis that predicts not only that two variables covary, but why a specified flux, force, mixing process or chemical transformation would connect them. If the hypothesized mechanism acts across a boundary, label that boundary with a direction arrow and correct units. If the hypothesis involves observational aliasing, describe which repeat sample would expose it.

Use the Unit 2 CSV as **fictional practice data**, not as empirical support. Calculate the mean, median, spread and a clearly chosen depth or time contrast. Fit a basic trend only after plotting raw values; a trend through a cyclic signal may depend on the starting and ending date. Draw uncertainty bars reflecting either an explicitly assumed sensor precision or the sample variability, and never call the two interchangeable. Rewrite one claim after noticing that an instrument was calibrated differently halfway through the experiment.

**Counterfactual:** Consider that the sampling route misses the location of maximum gradient. Estimate qualitatively whether a mean, a transport or an inventory would be biased upward or downward, and explain the sign. Then compare the consequences of doubling temporal cadence versus doubling spatial coverage. Select the cheaper improvement that tests the strongest competing explanation, even if it does not make the final map more visually attractive.

**Mini-report deliverables:** (1) a diagram with all coordinate and datum choices, (2) one calculation fully worked in SI units, (3) an independent check using a second observable, (4) a paragraph naming two uncertainties and whether they are random or systematic, and (5) a decision sentence that begins with the conditions under which the evidence is adequate. Good reasoning is judged by what could invalidate it, not by whether the synthetic plot looks smooth.

## Unit review and extension

Re-read the guiding question: How can salt, heat, compression and turbulence create layered fluid bodies? Develop a two-column comparison between what the instruments directly measure and what the analyst hopes to infer. Explain at least three gaps between those columns. Reproduce the five solved exercises without looking at the results, and check the sensitivity of one result to a changed parameter. Demonstrate each unit model with the slider at its minimum, middle and maximum value. Finally, propose a new sampling site whose observation has the power to reject one interpretation, rather than simply providing more data of the same type.

A useful extension is to add a conservative tracer or reference measurement that responds to a different physical property. Observations become stronger when they have different failure mechanisms. A temperature record and an optical satellite product, for example, cannot replace a calibrated salinity profile, but together they may constrain a wider range of causal stories. Describe how the extension would change confidence and what inference remains beyond its reach.

### Interactive classroom model — Two-endmember salinity mixing

Change **fraction of 35 g/kg endmember** between 0 and 1 using the slider on the HTML reading page. The number displayed is in g/kg; first predict the direction of change from the equation, and then verify using the control. **Model limitation:** Fixed conservative endmembers at 30 and 35 g/kg; no evaporation or reactions.

A numerical graph is an invitation to test assumptions, not a replacement for a real observation. Try an extreme parameter setting, record whether it remains physically plausible, and name a missing mechanism. Explain how the simplified classroom response could be validated or invalidated with a real dataset.

### Interactive classroom model — Temperature change after 30 days of heating

Change **mixed-layer depth (m)** between 5 and 150 using the slider on the HTML reading page. The number displayed is in °C; first predict the direction of change from the equation, and then verify using the control. **Model limitation:** Constant 70 W/m² net flux, no entrainment, loss or lateral advection.

A numerical graph is an invitation to test assumptions, not a replacement for a real observation. Try an extreme parameter setting, record whether it remains physically plausible, and name a missing mechanism. Explain how the simplified classroom response could be validated or invalidated with a real dataset.

