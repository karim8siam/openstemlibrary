# Unit 1 — Ocean basins, exploration and evidence

## Guiding question: How does oceanography establish a reliable picture of a domain that cannot be inspected everywhere?

**Synthetic case study:** A fictional survey team maps a continental margin before selecting sites for a long-term observing program. The ship has limited station time, variable acoustic conditions and an imperfect archived chart. The research objective is to distinguish bathymetric form from water-column variability and instrument artifacts.

## Scientific foundations and the shape of the inquiry

The starting method in this unit is **bathymetry and sampling**. Convert between map units and physical lengths before classifying seafloor features; inspect raw sounding locations rather than relying exclusively on gridded contours. Separate positional uncertainty from depth uncertainty. An uncertainty of tens of meters can change whether a narrow canyon has truly been observed.

**Comparative interpretation:** Stratify the fictional study region into shelf, slope and abyssal stations, then compare the effect of adding one targeted transect with the effect of uniformly adding stations. The former may reveal an overlooked canyon, whereas the latter offers more even geographic coverage.

**Fieldwork and model validation:** A map cell represents a spatial average and a processing history, not direct observation at every point. Keep both the sounding-density layer and the gridded surface. If a feature survives reasonable changes in interpolation, confidence improves; if its existence depends on a single smoothing parameter, lower the interpretation grade.

Oceanographic quantities generally depend on the choice of reference frame and on the boundaries of the study region. A point sensor records conditions in a small volume; a gridded map estimates a field across many cells; a process model predicts how that field should change under specified equations and boundary conditions. A student who moves directly from a point sensor to a regional mechanism is making an extrapolation that requires independent support. Keep a table recording the proposed mechanism, the predicted pattern, and the observation that would undermine it. This practice prevents a persuasive figure from becoming an unsupported explanation.

The lesson sequence moves from describing observations to relating them to mechanisms, building a tractable calculation, testing sensitivity and finally explaining what action could justifiably follow. No numerical constant in a simplified teaching exercise should be mistaken for a globally fitted parameter. The numerical questions in this unit are deliberately synthetic; their main purpose is to expose the dimensional structure of the reasoning.

## Lesson 1.1 — Ocean basins and plate-tectonic setting

### 1. Physical question and core explanation

Ocean basins are shaped by oceanic crust production at spreading ridges, recycling at subduction zones, and sediment loading along margins. A transect from shelf to abyssal plain crosses environments with different geological ages, heat fluxes, and sediment supplies. Relief is not a direct measurement of water properties.


### 2. What to measure, and how

Compare a regional multibeam grid with a tectonic map, and mark where sparse sounding coverage or interpolation might mislead an inexperienced mapper. Measure the slope distribution separately for shelf, slope and plain instead of averaging them indiscriminately.


### 3. Mechanism, model and dimensional reasoning

In a first approximation, represent **ocean basins and plate-tectonic setting** with an inventory, a forcing term and at least one route for exchange with surrounding water or the atmosphere. The model may be a proportionality, a conservative mixture, a flux balance, or a kinematic relation. Put units beside every variable before substituting measurements. A ratio of two volumes is dimensionless; a current is length per time; and a volume transport also includes cross-sectional area. If dimensions do not close, the numerical result cannot be correct even if a calculator produced it.


### 4. Fully worked quantitative case

**Problem — Shelf-to-basin depth contrast.** A shelf station has depth 180 m and an abyssal station 4,680 m. Compute their depth contrast.

**Model and substitution:** `4680-180`. Evaluate it using the units stated in the problem and the accompanying conversion factors. The result is **4500 m**. Every multiplier or divisor should have a physical interpretation: cross-sectional area converts velocity to transport; elapsed time converts a rate to a stock change; a density or heat-capacity factor connects a thermodynamic state change to an energy inventory. For angular or exponent-based relationships, specify whether the input is degrees, radians or a dimensionless ratio.

**Interpretation:** Record both stations under the same vertical datum. The numerical answer belongs to a deliberately simplified scenario. Compare it against an order-of-magnitude estimate: could a change by a factor of ten in one driver plausibly change the reported quantity by that amount? Identify which omitted process would have the strongest effect if this toy calculation were used at sea. Explain why a precise printed number is not a measurement of exact physical truth.

### 5. Competing explanations, failure modes and observation quality

Seafloor relief can resemble a crustal fault even when erosion, landslide deposition or acoustic gaps produced the lineament. An abrupt depth change should not become a tectonic interpretation until location accuracy and alternative explanations have been checked.


### 6. Research procedure and reproducibility

Use the synthetic Unit 1 dataset to carry out a compact investigation. Begin by inspecting timestamps and units; then write one falsifiable prediction about **ocean basins and plate-tectonic setting**. Make a first plot of raw samples, mark missing or flagged records, and only afterward compute summary statistics. Repeat the summary after removing two extreme values and explain whether the conclusion changes. If the response is strongly depth-dependent, group observations by depth before averaging. A good lab submission includes the code or spreadsheet formulas, variable definitions, a figure with readable axes, and a one-paragraph argument that separates the observed pattern from its proposed cause.


### 7. Sensitivity, limits and transfer


**Short knowledge check:** State the direct observable for ocean basins and plate-tectonic setting, one mechanism compatible with it, one competing explanation, the units of the lesson’s calculation, and one measurement that would discriminate between the explanations. The response should contain at least one sentence explaining why the textbook’s simplified model is not by itself a site-specific forecast.

## Lesson 1.2 — Continental shelves, slopes and abyssal plains

### 1. Physical question and core explanation

Shelf width reflects tectonic setting, sea-level history and sediment supply, while slope morphology often records canyons and mass wasting. Abyssal plains are not always flat: buried relief, fracture zones and sediment drifts create subtle spatial patterns. The landward reference for a depth section matters.


### 2. What to measure, and how

Establish a shore-normal transect using a common vertical datum and calculate slope from horizontal separation rather than map distance along a winding track. Relate adjacent sediment samples to the mapped morphological units.


### 3. Mechanism, model and dimensional reasoning

In a first approximation, represent **continental shelves, slopes and abyssal plains** with an inventory, a forcing term and at least one route for exchange with surrounding water or the atmosphere. The model may be a proportionality, a conservative mixture, a flux balance, or a kinematic relation. Put units beside every variable before substituting measurements. A ratio of two volumes is dimensionless; a current is length per time; and a volume transport also includes cross-sectional area. If dimensions do not close, the numerical result cannot be correct even if a calculator produced it.


### 4. Fully worked quantitative case

**Problem — Echo sounding depth.** A vertically directed pulse returns after 4.2 s at an assumed sound speed 1480 m/s. Estimate water depth.

**Model and substitution:** `1480*4.2/2`. Evaluate it using the units stated in the problem and the accompanying conversion factors. The result is **3108 m**. Every multiplier or divisor should have a physical interpretation: cross-sectional area converts velocity to transport; elapsed time converts a rate to a stock change; a density or heat-capacity factor connects a thermodynamic state change to an energy inventory. For angular or exponent-based relationships, specify whether the input is degrees, radians or a dimensionless ratio.

**Interpretation:** This is a two-way time with uniform assumed sound speed. The numerical answer belongs to a deliberately simplified scenario. Compare it against an order-of-magnitude estimate: could a change by a factor of ten in one driver plausibly change the reported quantity by that amount? Identify which omitted process would have the strongest effect if this toy calculation were used at sea. Explain why a precise printed number is not a measurement of exact physical truth.

### 5. Competing explanations, failure modes and observation quality

Comparisons across charts can be wrong if one survey uses a tidal datum and another uses mean sea level. Gridded surfaces also smooth small canyons; slope estimated over a large cell cannot resolve a narrow failure scarp.


### 6. Research procedure and reproducibility

Use the synthetic Unit 1 dataset to carry out a compact investigation. Begin by inspecting timestamps and units; then write one falsifiable prediction about **continental shelves, slopes and abyssal plains**. Make a first plot of raw samples, mark missing or flagged records, and only afterward compute summary statistics. Repeat the summary after removing two extreme values and explain whether the conclusion changes. If the response is strongly depth-dependent, group observations by depth before averaging. A good lab submission includes the code or spreadsheet formulas, variable definitions, a figure with readable axes, and a one-paragraph argument that separates the observed pattern from its proposed cause.


### 7. Sensitivity, limits and transfer


**Short knowledge check:** State the direct observable for continental shelves, slopes and abyssal plains, one mechanism compatible with it, one competing explanation, the units of the lesson’s calculation, and one measurement that would discriminate between the explanations. The response should contain at least one sentence explaining why the textbook’s simplified model is not by itself a site-specific forecast.

## Lesson 1.3 — Echo sounding, acoustics and seafloor uncertainty

### 1. Physical question and core explanation

A sonar estimates distance from two-way travel time and sound speed; the latter varies with temperature, salinity and pressure. Multibeam systems map wide swaths, but refraction and ship attitude can distort the outer beams. The travel-time equation is simple, the calibration problem is not.


### 2. What to measure, and how

Pair acoustic profiles with conductivity-temperature-depth casts, positioning information and motion sensors. Plot overlapping survey swaths to reveal offsets, and retain the raw returns for later reprocessing as sound-speed estimates improve.


### 3. Mechanism, model and dimensional reasoning

In a first approximation, represent **echo sounding, acoustics and seafloor uncertainty** with an inventory, a forcing term and at least one route for exchange with surrounding water or the atmosphere. The model may be a proportionality, a conservative mixture, a flux balance, or a kinematic relation. Put units beside every variable before substituting measurements. A ratio of two volumes is dimensionless; a current is length per time; and a volume transport also includes cross-sectional area. If dimensions do not close, the numerical result cannot be correct even if a calculator produced it.


### 4. Fully worked quantitative case

**Problem — Survey swath area.** A sonar swath covers 3.5 km width along a 64 km survey line. Find nominal area.

**Model and substitution:** `3.5*64`. Evaluate it using the units stated in the problem and the accompanying conversion factors. The result is **224 km²**. Every multiplier or divisor should have a physical interpretation: cross-sectional area converts velocity to transport; elapsed time converts a rate to a stock change; a density or heat-capacity factor connects a thermodynamic state change to an energy inventory. For angular or exponent-based relationships, specify whether the input is degrees, radians or a dimensionless ratio.

**Interpretation:** Overlap, turns and invalid beams reduce useful coverage. The numerical answer belongs to a deliberately simplified scenario. Compare it against an order-of-magnitude estimate: could a change by a factor of ten in one driver plausibly change the reported quantity by that amount? Identify which omitted process would have the strongest effect if this toy calculation were used at sea. Explain why a precise printed number is not a measurement of exact physical truth.

### 5. Competing explanations, failure modes and observation quality

An assumed uniform sound speed may bias every reported depth. Reverberation, bubble clouds, fish schools and sidelobes can yield apparent seabed echoes that are physically unrelated to the bottom.


### 6. Research procedure and reproducibility

Use the synthetic Unit 1 dataset to carry out a compact investigation. Begin by inspecting timestamps and units; then write one falsifiable prediction about **echo sounding, acoustics and seafloor uncertainty**. Make a first plot of raw samples, mark missing or flagged records, and only afterward compute summary statistics. Repeat the summary after removing two extreme values and explain whether the conclusion changes. If the response is strongly depth-dependent, group observations by depth before averaging. A good lab submission includes the code or spreadsheet formulas, variable definitions, a figure with readable axes, and a one-paragraph argument that separates the observed pattern from its proposed cause.


### 7. Sensitivity, limits and transfer


**Short knowledge check:** State the direct observable for echo sounding, acoustics and seafloor uncertainty, one mechanism compatible with it, one competing explanation, the units of the lesson’s calculation, and one measurement that would discriminate between the explanations. The response should contain at least one sentence explaining why the textbook’s simplified model is not by itself a site-specific forecast.

## Lesson 1.4 — Satellites, floats, gliders and ship sections

### 1. Physical question and core explanation

Ship stations provide rich vertical profiles at sparse locations; satellites provide broad, repeated surface observations; floats and gliders trade speed and payload for autonomous sampling. An adequate observing system merges rather than conflates these complementary viewpoints.


### 2. What to measure, and how

Design overlapping observation windows: CTD profiles for subsurface context, sea-surface temperature for upper-boundary variability, altimetry for sea-surface-height anomalies and floats for seasonal evolution. Note the orbit repeat cycle and missing coastal pixels.


### 3. Mechanism, model and dimensional reasoning

In a first approximation, represent **satellites, floats, gliders and ship sections** with an inventory, a forcing term and at least one route for exchange with surrounding water or the atmosphere. The model may be a proportionality, a conservative mixture, a flux balance, or a kinematic relation. Put units beside every variable before substituting measurements. A ratio of two volumes is dimensionless; a current is length per time; and a volume transport also includes cross-sectional area. If dimensions do not close, the numerical result cannot be correct even if a calculator produced it.


### 4. Fully worked quantitative case

**Problem — Argo float sampling fraction.** If 85 successful profiles came from 100 scheduled cycles, calculate completion percent.

**Model and substitution:** `85/100*100`. Evaluate it using the units stated in the problem and the accompanying conversion factors. The result is **85 %**. Every multiplier or divisor should have a physical interpretation: cross-sectional area converts velocity to transport; elapsed time converts a rate to a stock change; a density or heat-capacity factor connects a thermodynamic state change to an energy inventory. For angular or exponent-based relationships, specify whether the input is degrees, radians or a dimensionless ratio.

**Interpretation:** Scientific coverage also depends on where failures occurred. The numerical answer belongs to a deliberately simplified scenario. Compare it against an order-of-magnitude estimate: could a change by a factor of ten in one driver plausibly change the reported quantity by that amount? Identify which omitted process would have the strongest effect if this toy calculation were used at sea. Explain why a precise printed number is not a measurement of exact physical truth.

### 5. Competing explanations, failure modes and observation quality

Ocean color is not a direct species census, and satellite temperature is not the full water-column heat content. Clouds, retrieval algorithms, float drift and biased ship routes affect apparent geographic patterns.


### 6. Research procedure and reproducibility

Use the synthetic Unit 1 dataset to carry out a compact investigation. Begin by inspecting timestamps and units; then write one falsifiable prediction about **satellites, floats, gliders and ship sections**. Make a first plot of raw samples, mark missing or flagged records, and only afterward compute summary statistics. Repeat the summary after removing two extreme values and explain whether the conclusion changes. If the response is strongly depth-dependent, group observations by depth before averaging. A good lab submission includes the code or spreadsheet formulas, variable definitions, a figure with readable axes, and a one-paragraph argument that separates the observed pattern from its proposed cause.


### 7. Sensitivity, limits and transfer


**Short knowledge check:** State the direct observable for satellites, floats, gliders and ship sections, one mechanism compatible with it, one competing explanation, the units of the lesson’s calculation, and one measurement that would discriminate between the explanations. The response should contain at least one sentence explaining why the textbook’s simplified model is not by itself a site-specific forecast.

## Lesson 1.5 — Sampling, coordinates and data provenance

### 1. Physical question and core explanation

A datum, a time zone, a coordinate reference and an instrument calibration are scientific variables. Sampling plans also carry a selection mechanism: convenient stations may overrepresent calm weather and shallow accessible water. Provenance makes a dataset independently reusable.


### 2. What to measure, and how

Create a metadata ledger recording position, time in UTC, nominal and corrected depth, sensor identifier, calibration files, flags and processing steps. Randomize some station choices within geographic strata to test sensitivity to convenience sampling.


### 3. Mechanism, model and dimensional reasoning

In a first approximation, represent **sampling, coordinates and data provenance** with an inventory, a forcing term and at least one route for exchange with surrounding water or the atmosphere. The model may be a proportionality, a conservative mixture, a flux balance, or a kinematic relation. Put units beside every variable before substituting measurements. A ratio of two volumes is dimensionless; a current is length per time; and a volume transport also includes cross-sectional area. If dimensions do not close, the numerical result cannot be correct even if a calculator produced it.


### 4. Fully worked quantitative case

**Problem — Latitude scale conversion.** At an approximate 111 km per degree of latitude, convert 0.08° to distance.

**Model and substitution:** `111*.08`. Evaluate it using the units stated in the problem and the accompanying conversion factors. The result is **8.88 km**. Every multiplier or divisor should have a physical interpretation: cross-sectional area converts velocity to transport; elapsed time converts a rate to a stock change; a density or heat-capacity factor connects a thermodynamic state change to an energy inventory. For angular or exponent-based relationships, specify whether the input is degrees, radians or a dimensionless ratio.

**Interpretation:** Longitude requires latitude-dependent scaling. The numerical answer belongs to a deliberately simplified scenario. Compare it against an order-of-magnitude estimate: could a change by a factor of ten in one driver plausibly change the reported quantity by that amount? Identify which omitted process would have the strongest effect if this toy calculation were used at sea. Explain why a precise printed number is not a measurement of exact physical truth.

### 5. Competing explanations, failure modes and observation quality

False precision is common in exported spreadsheets. A tenth of a degree of latitude is not a meter-scale location, and a sensor record with a missing depth offset cannot be interpreted as an absolute vertical profile.


### 6. Research procedure and reproducibility

Use the synthetic Unit 1 dataset to carry out a compact investigation. Begin by inspecting timestamps and units; then write one falsifiable prediction about **sampling, coordinates and data provenance**. Make a first plot of raw samples, mark missing or flagged records, and only afterward compute summary statistics. Repeat the summary after removing two extreme values and explain whether the conclusion changes. If the response is strongly depth-dependent, group observations by depth before averaging. A good lab submission includes the code or spreadsheet formulas, variable definitions, a figure with readable axes, and a one-paragraph argument that separates the observed pattern from its proposed cause.


### 7. Sensitivity, limits and transfer


**Short knowledge check:** State the direct observable for sampling, coordinates and data provenance, one mechanism compatible with it, one competing explanation, the units of the lesson’s calculation, and one measurement that would discriminate between the explanations. The response should contain at least one sentence explaining why the textbook’s simplified model is not by itself a site-specific forecast.

## Integrated field investigation: joining the five lessons

**Research setting:** A fictional survey team maps a continental margin before selecting sites for a long-term observing program. The ship has limited station time, variable acoustic conditions and an imperfect archived chart. The research objective is to distinguish bathymetric form from water-column variability and instrument artifacts.

Begin by drawing an annotated cross-section of the hypothetical study domain. Mark the variables addressed in the five lessons: ocean basins and plate-tectonic setting, continental shelves, slopes and abyssal plains, echo sounding, acoustics and seafloor uncertainty, satellites, floats, gliders and ship sections, sampling, coordinates and data provenance. State a hypothesis that predicts not only that two variables covary, but why a specified flux, force, mixing process or chemical transformation would connect them. If the hypothesized mechanism acts across a boundary, label that boundary with a direction arrow and correct units. If the hypothesis involves observational aliasing, describe which repeat sample would expose it.

Use the Unit 1 CSV as **fictional practice data**, not as empirical support. Calculate the mean, median, spread and a clearly chosen depth or time contrast. Fit a basic trend only after plotting raw values; a trend through a cyclic signal may depend on the starting and ending date. Draw uncertainty bars reflecting either an explicitly assumed sensor precision or the sample variability, and never call the two interchangeable. Rewrite one claim after noticing that an instrument was calibrated differently halfway through the experiment.

**Counterfactual:** Consider that the sampling route misses the location of maximum gradient. Estimate qualitatively whether a mean, a transport or an inventory would be biased upward or downward, and explain the sign. Then compare the consequences of doubling temporal cadence versus doubling spatial coverage. Select the cheaper improvement that tests the strongest competing explanation, even if it does not make the final map more visually attractive.

**Mini-report deliverables:** (1) a diagram with all coordinate and datum choices, (2) one calculation fully worked in SI units, (3) an independent check using a second observable, (4) a paragraph naming two uncertainties and whether they are random or systematic, and (5) a decision sentence that begins with the conditions under which the evidence is adequate. Good reasoning is judged by what could invalidate it, not by whether the synthetic plot looks smooth.

## Unit review and extension

Re-read the guiding question: How does oceanography establish a reliable picture of a domain that cannot be inspected everywhere? Develop a two-column comparison between what the instruments directly measure and what the analyst hopes to infer. Explain at least three gaps between those columns. Reproduce the five solved exercises without looking at the results, and check the sensitivity of one result to a changed parameter. Demonstrate each unit model with the slider at its minimum, middle and maximum value. Finally, propose a new sampling site whose observation has the power to reject one interpretation, rather than simply providing more data of the same type.

A useful extension is to add a conservative tracer or reference measurement that responds to a different physical property. Observations become stronger when they have different failure mechanisms. A temperature record and an optical satellite product, for example, cannot replace a calibrated salinity profile, but together they may constrain a wider range of causal stories. Describe how the extension would change confidence and what inference remains beyond its reach.

### Interactive classroom model — Sounding depth from echo return

Change **round-trip echo travel time (s)** between 0.5 and 8 using the slider on the HTML reading page. The number displayed is in m; first predict the direction of change from the equation, and then verify using the control. **Model limitation:** Constant sound speed 1480 m/s; real sound speed varies with temperature, pressure and salinity.

A numerical graph is an invitation to test assumptions, not a replacement for a real observation. Try an extreme parameter setting, record whether it remains physically plausible, and name a missing mechanism. Explain how the simplified classroom response could be validated or invalidated with a real dataset.

### Interactive classroom model — Local seafloor slope

Change **depth change across 1 km (m)** between 0 and 400 using the slider on the HTML reading page. The number displayed is in degrees; first predict the direction of change from the equation, and then verify using the control. **Model limitation:** Ideal straight transect; slope depends on grid scale and the distance reference.

A numerical graph is an invitation to test assumptions, not a replacement for a real observation. Try an extreme parameter setting, record whether it remains physically plausible, and name a missing mechanism. Explain how the simplified classroom response could be validated or invalidated with a real dataset.

