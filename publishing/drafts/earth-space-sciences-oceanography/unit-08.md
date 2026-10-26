# Unit 8 — Oceanographic prediction, hazards and responsible decisions

## Guiding question: How can observations and models support defensible marine decisions without hiding uncertainty?

**Synthetic case study:** A coastal planning committee wants a single prediction for a complex shelf. The research team instead offers transparent scenarios, validation evidence and separate hazard indicators for surge, waves, tsunamis and ecosystem stress.

## Scientific foundations and the shape of the inquiry

The starting method in this unit is **predictive models and decision making**. Close mass and tracer budgets before interpreting sophisticated predictions. A calibrated model should be tested on held-out conditions and compared against persistence or climatology. Report decisions as conditional statements tied to an explicit value threshold, risk tolerance and evidence quality.

**Comparative interpretation:** A hypothetical coastal authority requests one exact number for next month’s flood risk. Construct a sensitivity table for tide phase, storm surge and relative sea-level uncertainty and explain why a forecast interval can be more operationally informative than an unjustified precise value.

**Fieldwork and model validation:** Model smoothness is not evidence of correctness. The first checks should be units, budgets, sign conventions, numerical convergence and basic observational comparisons. A decision tool becomes credible by naming failure conditions, not by displaying many decimal places.

Oceanographic quantities generally depend on the choice of reference frame and on the boundaries of the study region. A point sensor records conditions in a small volume; a gridded map estimates a field across many cells; a process model predicts how that field should change under specified equations and boundary conditions. A student who moves directly from a point sensor to a regional mechanism is making an extrapolation that requires independent support. Keep a table recording the proposed mechanism, the predicted pattern, and the observation that would undermine it. This practice prevents a persuasive figure from becoming an unsupported explanation.

The lesson sequence moves from describing observations to relating them to mechanisms, building a tractable calculation, testing sensitivity and finally explaining what action could justifiably follow. No numerical constant in a simplified teaching exercise should be mistaken for a globally fitted parameter. The numerical questions in this unit are deliberately synthetic; their main purpose is to expose the dimensional structure of the reasoning.

## Lesson 8.1 — Field campaign design and sensor calibration

### 1. Physical question and core explanation

A sampling campaign must connect its hypothesis to scales, instrument performance and a practical deployment plan. Station spacing follows the physical process; temporal cadence must resolve expected variability; calibration and intercomparison make records comparable across instruments.


### 2. What to measure, and how

Specify an observing network for a seasonal coastal upwelling event: sensors, sampling frequencies, reference casts, data backup and storm contingencies. Distinguish discovery-scale maps from high-frequency time series at a fixed mooring.


### 3. Mechanism, model and dimensional reasoning

In a first approximation, represent **field campaign design and sensor calibration** with an inventory, a forcing term and at least one route for exchange with surrounding water or the atmosphere. The model may be a proportionality, a conservative mixture, a flux balance, or a kinematic relation. Put units beside every variable before substituting measurements. A ratio of two volumes is dimensionless; a current is length per time; and a volume transport also includes cross-sectional area. If dimensions do not close, the numerical result cannot be correct even if a calculator produced it.


### 4. Fully worked quantitative case

**Problem — Campaign duty cycle.** A profiler makes one measurement every 15 min for 21 days. How many scheduled records?

**Model and substitution:** `21*24*60/15`. Evaluate it using the units stated in the problem and the accompanying conversion factors. The result is **2016 records**. Every multiplier or divisor should have a physical interpretation: cross-sectional area converts velocity to transport; elapsed time converts a rate to a stock change; a density or heat-capacity factor connects a thermodynamic state change to an energy inventory. For angular or exponent-based relationships, specify whether the input is degrees, radians or a dimensionless ratio.

**Interpretation:** Packet loss and quality flags reduce usable samples. The numerical answer belongs to a deliberately simplified scenario. Compare it against an order-of-magnitude estimate: could a change by a factor of ten in one driver plausibly change the reported quantity by that amount? Identify which omitted process would have the strongest effect if this toy calculation were used at sea. Explain why a precise printed number is not a measurement of exact physical truth.

### 5. Competing explanations, failure modes and observation quality

A precise instrument deployed at the wrong depth or season may be scientifically uninformative. Sensor drift and failed telemetry can masquerade as an environmental regime shift.


### 6. Research procedure and reproducibility

Use the synthetic Unit 8 dataset to carry out a compact investigation. Begin by inspecting timestamps and units; then write one falsifiable prediction about **field campaign design and sensor calibration**. Make a first plot of raw samples, mark missing or flagged records, and only afterward compute summary statistics. Repeat the summary after removing two extreme values and explain whether the conclusion changes. If the response is strongly depth-dependent, group observations by depth before averaging. A good lab submission includes the code or spreadsheet formulas, variable definitions, a figure with readable axes, and a one-paragraph argument that separates the observed pattern from its proposed cause.


### 7. Sensitivity, limits and transfer


**Short knowledge check:** State the direct observable for field campaign design and sensor calibration, one mechanism compatible with it, one competing explanation, the units of the lesson’s calculation, and one measurement that would discriminate between the explanations. The response should contain at least one sentence explaining why the textbook’s simplified model is not by itself a site-specific forecast.

## Lesson 8.2 — Conservation laws and numerical ocean models

### 1. Physical question and core explanation

Ocean models discretize momentum, mass, heat and salt conservation on computational grids. Choices of boundary conditions, turbulence closures and resolution govern which phenomena can be simulated. A stable numerical output is not evidence that model physics are correct.


### 2. What to measure, and how

Write a one-cell tracer update from advection and a source term with units checked. Run a time-step sensitivity study and compare mass before and after integration under closed boundaries.


### 3. Mechanism, model and dimensional reasoning

In a first approximation, represent **conservation laws and numerical ocean models** with an inventory, a forcing term and at least one route for exchange with surrounding water or the atmosphere. The model may be a proportionality, a conservative mixture, a flux balance, or a kinematic relation. Put units beside every variable before substituting measurements. A ratio of two volumes is dimensionless; a current is length per time; and a volume transport also includes cross-sectional area. If dimensions do not close, the numerical result cannot be correct even if a calculator produced it.


### 4. Fully worked quantitative case

**Problem — Tracer mass balance.** A closed cell initially stores 800 kg tracer. Source adds 12 kg/day for 5 days. Find stock.

**Model and substitution:** `800+12*5`. Evaluate it using the units stated in the problem and the accompanying conversion factors. The result is **860 kg**. Every multiplier or divisor should have a physical interpretation: cross-sectional area converts velocity to transport; elapsed time converts a rate to a stock change; a density or heat-capacity factor connects a thermodynamic state change to an energy inventory. For angular or exponent-based relationships, specify whether the input is degrees, radians or a dimensionless ratio.

**Interpretation:** No losses or boundary fluxes in the idealized box. The numerical answer belongs to a deliberately simplified scenario. Compare it against an order-of-magnitude estimate: could a change by a factor of ten in one driver plausibly change the reported quantity by that amount? Identify which omitted process would have the strongest effect if this toy calculation were used at sea. Explain why a precise printed number is not a measurement of exact physical truth.

### 5. Competing explanations, failure modes and observation quality

Numerical diffusion may produce smooth, convincing fields while erasing a real front. Conservation, stability and resolution convergence are separate tests, and calibration against observations cannot replace them.


### 6. Research procedure and reproducibility

Use the synthetic Unit 8 dataset to carry out a compact investigation. Begin by inspecting timestamps and units; then write one falsifiable prediction about **conservation laws and numerical ocean models**. Make a first plot of raw samples, mark missing or flagged records, and only afterward compute summary statistics. Repeat the summary after removing two extreme values and explain whether the conclusion changes. If the response is strongly depth-dependent, group observations by depth before averaging. A good lab submission includes the code or spreadsheet formulas, variable definitions, a figure with readable axes, and a one-paragraph argument that separates the observed pattern from its proposed cause.


### 7. Sensitivity, limits and transfer


**Short knowledge check:** State the direct observable for conservation laws and numerical ocean models, one mechanism compatible with it, one competing explanation, the units of the lesson’s calculation, and one measurement that would discriminate between the explanations. The response should contain at least one sentence explaining why the textbook’s simplified model is not by itself a site-specific forecast.

## Lesson 8.3 — Data assimilation, validation and forecast skill

### 1. Physical question and core explanation

Data assimilation combines a model prior with observations using assumptions about both error structures. Independent validation tests performance beyond the observations used for calibration. Good-looking hindcasts can be overfit, and a forecast needs probabilistic uncertainty.


### 2. What to measure, and how

Compute an illustrative weighted estimate from a prior and an observation with declared independent uncertainties. Evaluate persistence and climatology as baseline forecasts before claiming predictive skill.


### 3. Mechanism, model and dimensional reasoning

In a first approximation, represent **data assimilation, validation and forecast skill** with an inventory, a forcing term and at least one route for exchange with surrounding water or the atmosphere. The model may be a proportionality, a conservative mixture, a flux balance, or a kinematic relation. Put units beside every variable before substituting measurements. A ratio of two volumes is dimensionless; a current is length per time; and a volume transport also includes cross-sectional area. If dimensions do not close, the numerical result cannot be correct even if a calculator produced it.


### 4. Fully worked quantitative case

**Problem — Simple uncertainty weighting.** Prior 10 with SD2, observation 12 with SD1. Calculate inverse-variance mean.

**Model and substitution:** `(10/(2**2)+12/(1**2))/(1/(2**2)+1/(1**2))`. Evaluate it using the units stated in the problem and the accompanying conversion factors. The result is **11.6 units**. Every multiplier or divisor should have a physical interpretation: cross-sectional area converts velocity to transport; elapsed time converts a rate to a stock change; a density or heat-capacity factor connects a thermodynamic state change to an energy inventory. For angular or exponent-based relationships, specify whether the input is degrees, radians or a dimensionless ratio.

**Interpretation:** Independent errors required. The numerical answer belongs to a deliberately simplified scenario. Compare it against an order-of-magnitude estimate: could a change by a factor of ten in one driver plausibly change the reported quantity by that amount? Identify which omitted process would have the strongest effect if this toy calculation were used at sea. Explain why a precise printed number is not a measurement of exact physical truth.

### 5. Competing explanations, failure modes and observation quality

Treating correlated observations as independent makes uncertainty artificially small. A model evaluated at only a few calm-weather locations may fail during the high-impact storm events of practical interest.


### 6. Research procedure and reproducibility

Use the synthetic Unit 8 dataset to carry out a compact investigation. Begin by inspecting timestamps and units; then write one falsifiable prediction about **data assimilation, validation and forecast skill**. Make a first plot of raw samples, mark missing or flagged records, and only afterward compute summary statistics. Repeat the summary after removing two extreme values and explain whether the conclusion changes. If the response is strongly depth-dependent, group observations by depth before averaging. A good lab submission includes the code or spreadsheet formulas, variable definitions, a figure with readable axes, and a one-paragraph argument that separates the observed pattern from its proposed cause.


### 7. Sensitivity, limits and transfer


**Short knowledge check:** State the direct observable for data assimilation, validation and forecast skill, one mechanism compatible with it, one competing explanation, the units of the lesson’s calculation, and one measurement that would discriminate between the explanations. The response should contain at least one sentence explaining why the textbook’s simplified model is not by itself a site-specific forecast.

## Lesson 8.4 — Tsunamis, storm surge and compound coastal risk

### 1. Physical question and core explanation

A tsunami is a long gravity-wave response to rapid displacement and can travel across deep basins; storm surge results primarily from meteorological forcing. Compound flooding combines tide, waves, surge, river flow and land movement. These processes require different warning and modeling methods.


### 2. What to measure, and how

Estimate deep-ocean tsunami travel speed with c=sqrt(gH), then contrast the result with a shallow-shelf speed. Draw a compound water-level accounting diagram without assuming independent maxima occur simultaneously.


### 3. Mechanism, model and dimensional reasoning

In a first approximation, represent **tsunamis, storm surge and compound coastal risk** with an inventory, a forcing term and at least one route for exchange with surrounding water or the atmosphere. The model may be a proportionality, a conservative mixture, a flux balance, or a kinematic relation. Put units beside every variable before substituting measurements. A ratio of two volumes is dimensionless; a current is length per time; and a volume transport also includes cross-sectional area. If dimensions do not close, the numerical result cannot be correct even if a calculator produced it.


### 4. Fully worked quantitative case

**Problem — Tsunami ideal travel time.** An ideal long wave traverses 900 km at uniform depth 4000 m. Find hours.

**Model and substitution:** `900000/math.sqrt(9.81*4000)/3600`. Evaluate it using the units stated in the problem and the accompanying conversion factors. The result is **1.26205 hours**. Every multiplier or divisor should have a physical interpretation: cross-sectional area converts velocity to transport; elapsed time converts a rate to a stock change; a density or heat-capacity factor connects a thermodynamic state change to an energy inventory. For angular or exponent-based relationships, specify whether the input is degrees, radians or a dimensionless ratio.

**Interpretation:** Not a warning time for real coasts. The numerical answer belongs to a deliberately simplified scenario. Compare it against an order-of-magnitude estimate: could a change by a factor of ten in one driver plausibly change the reported quantity by that amount? Identify which omitted process would have the strongest effect if this toy calculation were used at sea. Explain why a precise printed number is not a measurement of exact physical truth.

### 5. Competing explanations, failure modes and observation quality

Small offshore tsunami wave heights may produce dangerous coastal currents and inundation. Simple travel-time calculations ignore variable bathymetry, refraction, resonance and source uncertainty; they are not evacuation guidance.


### 6. Research procedure and reproducibility

Use the synthetic Unit 8 dataset to carry out a compact investigation. Begin by inspecting timestamps and units; then write one falsifiable prediction about **tsunamis, storm surge and compound coastal risk**. Make a first plot of raw samples, mark missing or flagged records, and only afterward compute summary statistics. Repeat the summary after removing two extreme values and explain whether the conclusion changes. If the response is strongly depth-dependent, group observations by depth before averaging. A good lab submission includes the code or spreadsheet formulas, variable definitions, a figure with readable axes, and a one-paragraph argument that separates the observed pattern from its proposed cause.


### 7. Sensitivity, limits and transfer


**Short knowledge check:** State the direct observable for tsunamis, storm surge and compound coastal risk, one mechanism compatible with it, one competing explanation, the units of the lesson’s calculation, and one measurement that would discriminate between the explanations. The response should contain at least one sentence explaining why the textbook’s simplified model is not by itself a site-specific forecast.

## Lesson 8.5 — Synthesis: policy, uncertainty and reproducible science

### 1. Physical question and core explanation

A useful oceanographic result documents both a physical mechanism and what evidence could overturn it. Sustainable fisheries, marine protected areas, shipping safety and climate adaptation each require integrating physical, biological and socioeconomic observations. Data openness improves review but does not erase privacy or ecological sensitivity.


### 2. What to measure, and how

Produce a mini-assessment combining a hydrographic section, nearshore current estimate, chlorophyll proxy and stated decision threshold. Include raw data, code version, validation plots, alternative hypotheses and the exact conditions under which a recommendation fails.


### 3. Mechanism, model and dimensional reasoning

In a first approximation, represent **synthesis: policy, uncertainty and reproducible science** with an inventory, a forcing term and at least one route for exchange with surrounding water or the atmosphere. The model may be a proportionality, a conservative mixture, a flux balance, or a kinematic relation. Put units beside every variable before substituting measurements. A ratio of two volumes is dimensionless; a current is length per time; and a volume transport also includes cross-sectional area. If dimensions do not close, the numerical result cannot be correct even if a calculator produced it.


### 4. Fully worked quantitative case

**Problem — Integrated evidence index.** Three standardized component scores are 0.3, 0.6 and 0.9; give equal-weight mean.

**Model and substitution:** `(.3+.6+.9)/3`. Evaluate it using the units stated in the problem and the accompanying conversion factors. The result is **0.6 index**. Every multiplier or divisor should have a physical interpretation: cross-sectional area converts velocity to transport; elapsed time converts a rate to a stock change; a density or heat-capacity factor connects a thermodynamic state change to an energy inventory. For angular or exponent-based relationships, specify whether the input is degrees, radians or a dimensionless ratio.

**Interpretation:** A composite score embeds a normative weighting choice. The numerical answer belongs to a deliberately simplified scenario. Compare it against an order-of-magnitude estimate: could a change by a factor of ten in one driver plausibly change the reported quantity by that amount? Identify which omitted process would have the strongest effect if this toy calculation were used at sea. Explain why a precise printed number is not a measurement of exact physical truth.

### 5. Competing explanations, failure modes and observation quality

Optimizing one metric, such as mean annual sea level or average chlorophyll, may shift risk to unmeasured groups or extreme conditions. Good decisions separate what is measured, modeled, assumed and normatively chosen.


### 6. Research procedure and reproducibility

Use the synthetic Unit 8 dataset to carry out a compact investigation. Begin by inspecting timestamps and units; then write one falsifiable prediction about **synthesis: policy, uncertainty and reproducible science**. Make a first plot of raw samples, mark missing or flagged records, and only afterward compute summary statistics. Repeat the summary after removing two extreme values and explain whether the conclusion changes. If the response is strongly depth-dependent, group observations by depth before averaging. A good lab submission includes the code or spreadsheet formulas, variable definitions, a figure with readable axes, and a one-paragraph argument that separates the observed pattern from its proposed cause.


### 7. Sensitivity, limits and transfer


**Short knowledge check:** State the direct observable for synthesis: policy, uncertainty and reproducible science, one mechanism compatible with it, one competing explanation, the units of the lesson’s calculation, and one measurement that would discriminate between the explanations. The response should contain at least one sentence explaining why the textbook’s simplified model is not by itself a site-specific forecast.

## Integrated field investigation: joining the five lessons

**Research setting:** A coastal planning committee wants a single prediction for a complex shelf. The research team instead offers transparent scenarios, validation evidence and separate hazard indicators for surge, waves, tsunamis and ecosystem stress.

Begin by drawing an annotated cross-section of the hypothetical study domain. Mark the variables addressed in the five lessons: field campaign design and sensor calibration, conservation laws and numerical ocean models, data assimilation, validation and forecast skill, tsunamis, storm surge and compound coastal risk, synthesis: policy, uncertainty and reproducible science. State a hypothesis that predicts not only that two variables covary, but why a specified flux, force, mixing process or chemical transformation would connect them. If the hypothesized mechanism acts across a boundary, label that boundary with a direction arrow and correct units. If the hypothesis involves observational aliasing, describe which repeat sample would expose it.

Use the Unit 8 CSV as **fictional practice data**, not as empirical support. Calculate the mean, median, spread and a clearly chosen depth or time contrast. Fit a basic trend only after plotting raw values; a trend through a cyclic signal may depend on the starting and ending date. Draw uncertainty bars reflecting either an explicitly assumed sensor precision or the sample variability, and never call the two interchangeable. Rewrite one claim after noticing that an instrument was calibrated differently halfway through the experiment.

**Counterfactual:** Consider that the sampling route misses the location of maximum gradient. Estimate qualitatively whether a mean, a transport or an inventory would be biased upward or downward, and explain the sign. Then compare the consequences of doubling temporal cadence versus doubling spatial coverage. Select the cheaper improvement that tests the strongest competing explanation, even if it does not make the final map more visually attractive.

**Mini-report deliverables:** (1) a diagram with all coordinate and datum choices, (2) one calculation fully worked in SI units, (3) an independent check using a second observable, (4) a paragraph naming two uncertainties and whether they are random or systematic, and (5) a decision sentence that begins with the conditions under which the evidence is adequate. Good reasoning is judged by what could invalidate it, not by whether the synthetic plot looks smooth.

## Unit review and extension

Re-read the guiding question: How can observations and models support defensible marine decisions without hiding uncertainty? Develop a two-column comparison between what the instruments directly measure and what the analyst hopes to infer. Explain at least three gaps between those columns. Reproduce the five solved exercises without looking at the results, and check the sensitivity of one result to a changed parameter. Demonstrate each unit model with the slider at its minimum, middle and maximum value. Finally, propose a new sampling site whose observation has the power to reject one interpretation, rather than simply providing more data of the same type.

A useful extension is to add a conservative tracer or reference measurement that responds to a different physical property. Observations become stronger when they have different failure mechanisms. A temperature record and an optical satellite product, for example, cannot replace a calibrated salinity profile, but together they may constrain a wider range of causal stories. Describe how the extension would change confidence and what inference remains beyond its reach.

### Interactive classroom model — Scalar inverse-variance estimate

Change **observation error sd** between 0.2 and 5 using the slider on the HTML reading page. The number displayed is in units; first predict the direction of change from the equation, and then verify using the control. **Model limitation:** Prior 10±2 and observation 12±x, independent Gaussian errors.

A numerical graph is an invitation to test assumptions, not a replacement for a real observation. Try an extreme parameter setting, record whether it remains physically plausible, and name a missing mechanism. Explain how the simplified classroom response could be validated or invalidated with a real dataset.

### Interactive classroom model — Long-wave travel time for 900 km

Change **water depth (m)** between 20 and 6000 using the slider on the HTML reading page. The number displayed is in hours; first predict the direction of change from the equation, and then verify using the control. **Model limitation:** Uniform depth, ideal long wave, ignores complicated coastline and refraction.

A numerical graph is an invitation to test assumptions, not a replacement for a real observation. Try an extreme parameter setting, record whether it remains physically plausible, and name a missing mechanism. Explain how the simplified classroom response could be validated or invalidated with a real dataset.

