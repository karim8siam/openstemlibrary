# Unit 4 — Waves, tides, coasts and estuaries

## Guiding question: How does mechanical energy cross ocean boundaries and reshape shallow-water environments?

**Synthetic case study:** A coastal town needs to interpret an offshore buoy record and an estuary tide gauge before designing a monitoring program. Students separate wind waves, swell, tides, storm surge and river effects rather than assigning every high-water event the same cause.

## Scientific foundations and the shape of the inquiry

The starting method in this unit is **surface forcing and shallow-water processes**. Distinguish energy from mass transport and oscillation from drift. State whether the reported datum is relative to a chart datum, mean sea level, or a moving instrument platform. Decompose the observed water level conceptually into tide, meteorological residual and other terms before interpreting an extreme.

**Comparative interpretation:** Track a synthetic storm approach over a continental shelf. Offshore wave conditions, estuary phase and atmospheric pressure change together, but the peak at a sheltered harbor can occur at a different time from the maximum offshore wave height.

**Fieldwork and model validation:** Shallow-water dynamics change rapidly over distances shorter than typical offshore grids. Nearshore measurements should include bottom depth, instrument orientation and a consistent datum. Wave breaking and suspended sediments can interfere with optical and acoustic sensing at the very times hazards are highest.

Oceanographic quantities generally depend on the choice of reference frame and on the boundaries of the study region. A point sensor records conditions in a small volume; a gridded map estimates a field across many cells; a process model predicts how that field should change under specified equations and boundary conditions. A student who moves directly from a point sensor to a regional mechanism is making an extrapolation that requires independent support. Keep a table recording the proposed mechanism, the predicted pattern, and the observation that would undermine it. This practice prevents a persuasive figure from becoming an unsupported explanation.

The lesson sequence moves from describing observations to relating them to mechanisms, building a tractable calculation, testing sensitivity and finally explaining what action could justifiably follow. No numerical constant in a simplified teaching exercise should be mistaken for a globally fitted parameter. The numerical questions in this unit are deliberately synthetic; their main purpose is to expose the dimensional structure of the reasoning.

## Lesson 4.1 — Surface gravity waves and dispersion

### 1. Physical question and core explanation

Wind transfers energy to surface waves. For linear gravity waves, phase speed depends on wavelength and depth; deep-water waves are dispersive, whereas shallow-water long waves approach speed sqrt(gH). Individual water particles mostly oscillate while wave energy travels.


### 2. What to measure, and how

Evaluate long-wave c=sqrt(gH) for two depths, then compare travel times over an idealized flat shelf. Draw a wave train showing period, wavelength, phase speed and group speed as distinct quantities.


### 3. Mechanism, model and dimensional reasoning

In a first approximation, represent **surface gravity waves and dispersion** with an inventory, a forcing term and at least one route for exchange with surrounding water or the atmosphere. The model may be a proportionality, a conservative mixture, a flux balance, or a kinematic relation. Put units beside every variable before substituting measurements. A ratio of two volumes is dimensionless; a current is length per time; and a volume transport also includes cross-sectional area. If dimensions do not close, the numerical result cannot be correct even if a calculator produced it.


### 4. Fully worked quantitative case

**Problem — Shallow-water wave speed.** Compute sqrt(gH) for water 40 m deep.

**Model and substitution:** `math.sqrt(9.81*40)`. Evaluate it using the units stated in the problem and the accompanying conversion factors. The result is **19.80909 m/s**. Every multiplier or divisor should have a physical interpretation: cross-sectional area converts velocity to transport; elapsed time converts a rate to a stock change; a density or heat-capacity factor connects a thermodynamic state change to an energy inventory. For angular or exponent-based relationships, specify whether the input is degrees, radians or a dimensionless ratio.

**Interpretation:** Applies when wavelength is large relative to depth. The numerical answer belongs to a deliberately simplified scenario. Compare it against an order-of-magnitude estimate: could a change by a factor of ten in one driver plausibly change the reported quantity by that amount? Identify which omitted process would have the strongest effect if this toy calculation were used at sea. Explain why a precise printed number is not a measurement of exact physical truth.

### 5. Competing explanations, failure modes and observation quality

The shallow-water speed formula should not be applied to short swell in deep ocean without checking wavelength relative to depth. Wave breaking, nonlinear shoaling and currents modify the ideal prediction.


### 6. Research procedure and reproducibility

Use the synthetic Unit 4 dataset to carry out a compact investigation. Begin by inspecting timestamps and units; then write one falsifiable prediction about **surface gravity waves and dispersion**. Make a first plot of raw samples, mark missing or flagged records, and only afterward compute summary statistics. Repeat the summary after removing two extreme values and explain whether the conclusion changes. If the response is strongly depth-dependent, group observations by depth before averaging. A good lab submission includes the code or spreadsheet formulas, variable definitions, a figure with readable axes, and a one-paragraph argument that separates the observed pattern from its proposed cause.


### 7. Sensitivity, limits and transfer


**Short knowledge check:** State the direct observable for surface gravity waves and dispersion, one mechanism compatible with it, one competing explanation, the units of the lesson’s calculation, and one measurement that would discriminate between the explanations. The response should contain at least one sentence explaining why the textbook’s simplified model is not by itself a site-specific forecast.

## Lesson 4.2 — Wave energy, swell and coastal hazards

### 1. Physical question and core explanation

Significant wave height summarizes a wave spectrum; an occasional individual wave may exceed it. Wave energy scales approximately with the square of height, so modest height changes have disproportionate implications for loads and energy transport. Shoaling focuses energy as depth decreases.


### 2. What to measure, and how

Use an illustrative energy-per-area approximation rho*g*H_s^2/16 to compare two wave conditions. Discuss why an offshore wave buoy and a harbor wall can experience different heights.


### 3. Mechanism, model and dimensional reasoning

In a first approximation, represent **wave energy, swell and coastal hazards** with an inventory, a forcing term and at least one route for exchange with surrounding water or the atmosphere. The model may be a proportionality, a conservative mixture, a flux balance, or a kinematic relation. Put units beside every variable before substituting measurements. A ratio of two volumes is dimensionless; a current is length per time; and a volume transport also includes cross-sectional area. If dimensions do not close, the numerical result cannot be correct even if a calculator produced it.


### 4. Fully worked quantitative case

**Problem — Wave energy density proxy.** Take rho=1025, g=9.81, significant height=3 m: E≈rho g Hs²/16.

**Model and substitution:** `1025*9.81*3**2/16`. Evaluate it using the units stated in the problem and the accompanying conversion factors. The result is **5656.07812 J/m²**. Every multiplier or divisor should have a physical interpretation: cross-sectional area converts velocity to transport; elapsed time converts a rate to a stock change; a density or heat-capacity factor connects a thermodynamic state change to an energy inventory. For angular or exponent-based relationships, specify whether the input is degrees, radians or a dimensionless ratio.

**Interpretation:** Represents sea-state averaged linear wave energy per horizontal area. The numerical answer belongs to a deliberately simplified scenario. Compare it against an order-of-magnitude estimate: could a change by a factor of ten in one driver plausibly change the reported quantity by that amount? Identify which omitted process would have the strongest effect if this toy calculation were used at sea. Explain why a precise printed number is not a measurement of exact physical truth.

### 5. Competing explanations, failure modes and observation quality

A single monochromatic wave cannot reproduce irregular storm seas. Directional spreading, wave period, seabed refraction and coastal reflection can dominate local run-up.


### 6. Research procedure and reproducibility

Use the synthetic Unit 4 dataset to carry out a compact investigation. Begin by inspecting timestamps and units; then write one falsifiable prediction about **wave energy, swell and coastal hazards**. Make a first plot of raw samples, mark missing or flagged records, and only afterward compute summary statistics. Repeat the summary after removing two extreme values and explain whether the conclusion changes. If the response is strongly depth-dependent, group observations by depth before averaging. A good lab submission includes the code or spreadsheet formulas, variable definitions, a figure with readable axes, and a one-paragraph argument that separates the observed pattern from its proposed cause.


### 7. Sensitivity, limits and transfer


**Short knowledge check:** State the direct observable for wave energy, swell and coastal hazards, one mechanism compatible with it, one competing explanation, the units of the lesson’s calculation, and one measurement that would discriminate between the explanations. The response should contain at least one sentence explaining why the textbook’s simplified model is not by itself a site-specific forecast.

## Lesson 4.3 — Astronomical tides and harmonic analysis

### 1. Physical question and core explanation

Tides arise from gravitational forcing and rotating basin responses. Actual high-water timing depends on multiple constituents, resonance and coastline geometry. Tidal range varies within spring-neap cycles; chart datums are chosen for particular navigation and coastal applications.


### 2. What to measure, and how

Add two cosine tidal constituents with labeled amplitudes and periods to make an illustrative water-level series. Compare high-water heights with and without a non-tidal residual.


### 3. Mechanism, model and dimensional reasoning

In a first approximation, represent **astronomical tides and harmonic analysis** with an inventory, a forcing term and at least one route for exchange with surrounding water or the atmosphere. The model may be a proportionality, a conservative mixture, a flux balance, or a kinematic relation. Put units beside every variable before substituting measurements. A ratio of two volumes is dimensionless; a current is length per time; and a volume transport also includes cross-sectional area. If dimensions do not close, the numerical result cannot be correct even if a calculator produced it.


### 4. Fully worked quantitative case

**Problem — Tidal level superposition.** Add a 0.8 m cosine peak and 0.25 m cosine peak at coincident phase.

**Model and substitution:** `.8+.25`. Evaluate it using the units stated in the problem and the accompanying conversion factors. The result is **1.05 m**. Every multiplier or divisor should have a physical interpretation: cross-sectional area converts velocity to transport; elapsed time converts a rate to a stock change; a density or heat-capacity factor connects a thermodynamic state change to an energy inventory. For angular or exponent-based relationships, specify whether the input is degrees, radians or a dimensionless ratio.

**Interpretation:** This is a selected instant, not the full tide forecast. The numerical answer belongs to a deliberately simplified scenario. Compare it against an order-of-magnitude estimate: could a change by a factor of ten in one driver plausibly change the reported quantity by that amount? Identify which omitted process would have the strongest effect if this toy calculation were used at sea. Explain why a precise printed number is not a measurement of exact physical truth.

### 5. Competing explanations, failure modes and observation quality

The common two-bulge picture is a useful starting intuition but is not a global tidal prediction model. A tide-gauge anomaly may include barometric pressure, surge or sensor datum drift.


### 6. Research procedure and reproducibility

Use the synthetic Unit 4 dataset to carry out a compact investigation. Begin by inspecting timestamps and units; then write one falsifiable prediction about **astronomical tides and harmonic analysis**. Make a first plot of raw samples, mark missing or flagged records, and only afterward compute summary statistics. Repeat the summary after removing two extreme values and explain whether the conclusion changes. If the response is strongly depth-dependent, group observations by depth before averaging. A good lab submission includes the code or spreadsheet formulas, variable definitions, a figure with readable axes, and a one-paragraph argument that separates the observed pattern from its proposed cause.


### 7. Sensitivity, limits and transfer


**Short knowledge check:** State the direct observable for astronomical tides and harmonic analysis, one mechanism compatible with it, one competing explanation, the units of the lesson’s calculation, and one measurement that would discriminate between the explanations. The response should contain at least one sentence explaining why the textbook’s simplified model is not by itself a site-specific forecast.

## Lesson 4.4 — Nearshore currents, beaches and sediment exchange

### 1. Physical question and core explanation

Breaking waves create setup, longshore currents and nearshore circulation. Longshore sediment transport depends on wave angle, sediment availability and shoreline geometry. Rip currents move water seaward within circulation cells and are not simply undertows along the whole beach.


### 2. What to measure, and how

Use a simplified shoreline sediment-cell inventory with inflow, outflow and beach storage change. Track morphological response after a groyne without assuming sediment disappears from the system.


### 3. Mechanism, model and dimensional reasoning

In a first approximation, represent **nearshore currents, beaches and sediment exchange** with an inventory, a forcing term and at least one route for exchange with surrounding water or the atmosphere. The model may be a proportionality, a conservative mixture, a flux balance, or a kinematic relation. Put units beside every variable before substituting measurements. A ratio of two volumes is dimensionless; a current is length per time; and a volume transport also includes cross-sectional area. If dimensions do not close, the numerical result cannot be correct even if a calculator produced it.


### 4. Fully worked quantitative case

**Problem — Beach sediment cell balance.** Sediment arrives at 65,000 m³/year and leaves at 82,000 m³/year. Compute net storage change.

**Model and substitution:** `65000-82000`. Evaluate it using the units stated in the problem and the accompanying conversion factors. The result is **-17000 m³/year**. Every multiplier or divisor should have a physical interpretation: cross-sectional area converts velocity to transport; elapsed time converts a rate to a stock change; a density or heat-capacity factor connects a thermodynamic state change to an energy inventory. For angular or exponent-based relationships, specify whether the input is degrees, radians or a dimensionless ratio.

**Interpretation:** Offshore exchange and nourishment must be included in real budgets. The numerical answer belongs to a deliberately simplified scenario. Compare it against an order-of-magnitude estimate: could a change by a factor of ten in one driver plausibly change the reported quantity by that amount? Identify which omitted process would have the strongest effect if this toy calculation were used at sea. Explain why a precise printed number is not a measurement of exact physical truth.

### 5. Competing explanations, failure modes and observation quality

An engineering solution that retains sand on one beach may starve the down-drift coast. A short drone survey cannot distinguish seasonal erosion from long-term retreat without repeat surveys and datum consistency.


### 6. Research procedure and reproducibility

Use the synthetic Unit 4 dataset to carry out a compact investigation. Begin by inspecting timestamps and units; then write one falsifiable prediction about **nearshore currents, beaches and sediment exchange**. Make a first plot of raw samples, mark missing or flagged records, and only afterward compute summary statistics. Repeat the summary after removing two extreme values and explain whether the conclusion changes. If the response is strongly depth-dependent, group observations by depth before averaging. A good lab submission includes the code or spreadsheet formulas, variable definitions, a figure with readable axes, and a one-paragraph argument that separates the observed pattern from its proposed cause.


### 7. Sensitivity, limits and transfer


**Short knowledge check:** State the direct observable for nearshore currents, beaches and sediment exchange, one mechanism compatible with it, one competing explanation, the units of the lesson’s calculation, and one measurement that would discriminate between the explanations. The response should contain at least one sentence explaining why the textbook’s simplified model is not by itself a site-specific forecast.

## Lesson 4.5 — Estuaries, salt intrusion and river plume dynamics

### 1. Physical question and core explanation

Estuaries mix river freshwater and saline ocean water under tides, winds and variable discharge. Depending on forcing they may be well mixed, partially mixed or strongly stratified. Salt intrusion is a moving front, not a fixed administrative boundary.


### 2. What to measure, and how

Survey salinity along the estuary at two tidal stages and compare the section-mean versus near-bed salinity. Construct a simple salt conservation budget for an estuarine control volume.


### 3. Mechanism, model and dimensional reasoning

In a first approximation, represent **estuaries, salt intrusion and river plume dynamics** with an inventory, a forcing term and at least one route for exchange with surrounding water or the atmosphere. The model may be a proportionality, a conservative mixture, a flux balance, or a kinematic relation. Put units beside every variable before substituting measurements. A ratio of two volumes is dimensionless; a current is length per time; and a volume transport also includes cross-sectional area. If dimensions do not close, the numerical result cannot be correct even if a calculator produced it.


### 4. Fully worked quantitative case

**Problem — Estuarine endmember fraction.** A 20 g/kg sample mixes 0 and 35 g/kg endmembers. Find seawater mass fraction.

**Model and substitution:** `20/35`. Evaluate it using the units stated in the problem and the accompanying conversion factors. The result is **0.57143 fraction**. Every multiplier or divisor should have a physical interpretation: cross-sectional area converts velocity to transport; elapsed time converts a rate to a stock change; a density or heat-capacity factor connects a thermodynamic state change to an energy inventory. For angular or exponent-based relationships, specify whether the input is degrees, radians or a dimensionless ratio.

**Interpretation:** Assumes only two endmembers and conservative salt. The numerical answer belongs to a deliberately simplified scenario. Compare it against an order-of-magnitude estimate: could a change by a factor of ten in one driver plausibly change the reported quantity by that amount? Identify which omitted process would have the strongest effect if this toy calculation were used at sea. Explain why a precise printed number is not a measurement of exact physical truth.

### 5. Competing explanations, failure modes and observation quality

A one-dimensional average misses lateral channels and exchange flows. A short survey during unusual river discharge should not be treated as the annual salt-intrusion boundary.


### 6. Research procedure and reproducibility

Use the synthetic Unit 4 dataset to carry out a compact investigation. Begin by inspecting timestamps and units; then write one falsifiable prediction about **estuaries, salt intrusion and river plume dynamics**. Make a first plot of raw samples, mark missing or flagged records, and only afterward compute summary statistics. Repeat the summary after removing two extreme values and explain whether the conclusion changes. If the response is strongly depth-dependent, group observations by depth before averaging. A good lab submission includes the code or spreadsheet formulas, variable definitions, a figure with readable axes, and a one-paragraph argument that separates the observed pattern from its proposed cause.


### 7. Sensitivity, limits and transfer


**Short knowledge check:** State the direct observable for estuaries, salt intrusion and river plume dynamics, one mechanism compatible with it, one competing explanation, the units of the lesson’s calculation, and one measurement that would discriminate between the explanations. The response should contain at least one sentence explaining why the textbook’s simplified model is not by itself a site-specific forecast.

## Integrated field investigation: joining the five lessons

**Research setting:** A coastal town needs to interpret an offshore buoy record and an estuary tide gauge before designing a monitoring program. Students separate wind waves, swell, tides, storm surge and river effects rather than assigning every high-water event the same cause.

Begin by drawing an annotated cross-section of the hypothetical study domain. Mark the variables addressed in the five lessons: surface gravity waves and dispersion, wave energy, swell and coastal hazards, astronomical tides and harmonic analysis, nearshore currents, beaches and sediment exchange, estuaries, salt intrusion and river plume dynamics. State a hypothesis that predicts not only that two variables covary, but why a specified flux, force, mixing process or chemical transformation would connect them. If the hypothesized mechanism acts across a boundary, label that boundary with a direction arrow and correct units. If the hypothesis involves observational aliasing, describe which repeat sample would expose it.

Use the Unit 4 CSV as **fictional practice data**, not as empirical support. Calculate the mean, median, spread and a clearly chosen depth or time contrast. Fit a basic trend only after plotting raw values; a trend through a cyclic signal may depend on the starting and ending date. Draw uncertainty bars reflecting either an explicitly assumed sensor precision or the sample variability, and never call the two interchangeable. Rewrite one claim after noticing that an instrument was calibrated differently halfway through the experiment.

**Counterfactual:** Consider that the sampling route misses the location of maximum gradient. Estimate qualitatively whether a mean, a transport or an inventory would be biased upward or downward, and explain the sign. Then compare the consequences of doubling temporal cadence versus doubling spatial coverage. Select the cheaper improvement that tests the strongest competing explanation, even if it does not make the final map more visually attractive.

**Mini-report deliverables:** (1) a diagram with all coordinate and datum choices, (2) one calculation fully worked in SI units, (3) an independent check using a second observable, (4) a paragraph naming two uncertainties and whether they are random or systematic, and (5) a decision sentence that begins with the conditions under which the evidence is adequate. Good reasoning is judged by what could invalidate it, not by whether the synthetic plot looks smooth.

## Unit review and extension

Re-read the guiding question: How does mechanical energy cross ocean boundaries and reshape shallow-water environments? Develop a two-column comparison between what the instruments directly measure and what the analyst hopes to infer. Explain at least three gaps between those columns. Reproduce the five solved exercises without looking at the results, and check the sensitivity of one result to a changed parameter. Demonstrate each unit model with the slider at its minimum, middle and maximum value. Finally, propose a new sampling site whose observation has the power to reject one interpretation, rather than simply providing more data of the same type.

A useful extension is to add a conservative tracer or reference measurement that responds to a different physical property. Observations become stronger when they have different failure mechanisms. A temperature record and an optical satellite product, for example, cannot replace a calibrated salinity profile, but together they may constrain a wider range of causal stories. Describe how the extension would change confidence and what inference remains beyond its reach.

### Interactive classroom model — Long gravity-wave speed

Change **water depth (m)** between 5 and 6000 using the slider on the HTML reading page. The number displayed is in m/s; first predict the direction of change from the equation, and then verify using the control. **Model limitation:** Shallow-water wavelength assumption; not an arbitrary short wind wave.

A numerical graph is an invitation to test assumptions, not a replacement for a real observation. Try an extreme parameter setting, record whether it remains physically plausible, and name a missing mechanism. Explain how the simplified classroom response could be validated or invalidated with a real dataset.

### Interactive classroom model — Linear significant-wave energy per area

Change **significant wave height (m)** between 0.5 and 10 using the slider on the HTML reading page. The number displayed is in J/m²; first predict the direction of change from the equation, and then verify using the control. **Model limitation:** Linear irregular sea approximation; excludes breaking and directionality.

A numerical graph is an invitation to test assumptions, not a replacement for a real observation. Try an extreme parameter setting, record whether it remains physically plausible, and name a missing mechanism. Explain how the simplified classroom response could be validated or invalidated with a real dataset.

