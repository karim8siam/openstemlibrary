# Unit 7 — Biological oceanography and ecosystems

## Guiding question: How do photons, nutrients, mixing and trophic interactions generate ocean ecosystems?

**Synthetic case study:** A temperate shelf experiences a spring bloom after stratification develops. Observers measure fluorescence, nutrients and grazing but disagree on whether increasing color means higher daily production, higher standing stock or a different plankton community.

## Scientific foundations and the shape of the inquiry

The starting method in this unit is **biological measurement and trophic budgets**. Separate population size, pigment concentration, primary productivity, grazing losses and export. These are related but nonidentical variables. When comparing remote sensing with ship measurements, write down the spatial footprint, time mismatch and optical uncertainty.

**Comparative interpretation:** A new satellite composite shows brighter ocean color during a stratified week. Test whether the change could be caused by higher chlorophyll per cell or suspended particles, and describe which bottle samples or particle measurements would distinguish these possibilities.

**Fieldwork and model validation:** Biological communities respond to life histories and interactions, not only an instantaneous environmental value. A single chlorophyll image cannot resolve taxonomic composition, and a one-time bloom survey cannot give growth rate without flux or repeated abundance measurements.

Oceanographic quantities generally depend on the choice of reference frame and on the boundaries of the study region. A point sensor records conditions in a small volume; a gridded map estimates a field across many cells; a process model predicts how that field should change under specified equations and boundary conditions. A student who moves directly from a point sensor to a regional mechanism is making an extrapolation that requires independent support. Keep a table recording the proposed mechanism, the predicted pattern, and the observation that would undermine it. This practice prevents a persuasive figure from becoming an unsupported explanation.

The lesson sequence moves from describing observations to relating them to mechanisms, building a tractable calculation, testing sensitivity and finally explaining what action could justifiably follow. No numerical constant in a simplified teaching exercise should be mistaken for a globally fitted parameter. The numerical questions in this unit are deliberately synthetic; their main purpose is to expose the dimensional structure of the reasoning.

## Lesson 7.1 — Light attenuation and the euphotic zone

### 1. Physical question and core explanation

Sunlight decays with depth according to absorption and scattering that depend on wavelength, particles and dissolved matter. The euphotic-zone depth is a useful operational threshold rather than a sharp biological boundary. Photoinhibition and light acclimation complicate simple production curves.


### 2. What to measure, and how

Calculate idealized irradiance I(z)=I0 exp(-kz) and derive the depth of a chosen percentage. Compare two attenuation coefficients from fictional clear and turbid water columns.


### 3. Mechanism, model and dimensional reasoning

In a first approximation, represent **light attenuation and the euphotic zone** with an inventory, a forcing term and at least one route for exchange with surrounding water or the atmosphere. The model may be a proportionality, a conservative mixture, a flux balance, or a kinematic relation. Put units beside every variable before substituting measurements. A ratio of two volumes is dimensionless; a current is length per time; and a volume transport also includes cross-sectional area. If dimensions do not close, the numerical result cannot be correct even if a calculator produced it.


### 4. Fully worked quantitative case

**Problem — Euphotic fraction at depth.** At k=0.12 m−1 and depth 20 m, find percent of incident light.

**Model and substitution:** `100*math.exp(-.12*20)`. Evaluate it using the units stated in the problem and the accompanying conversion factors. The result is **9.0718 %**. Every multiplier or divisor should have a physical interpretation: cross-sectional area converts velocity to transport; elapsed time converts a rate to a stock change; a density or heat-capacity factor connects a thermodynamic state change to an energy inventory. For angular or exponent-based relationships, specify whether the input is degrees, radians or a dimensionless ratio.

**Interpretation:** A one-parameter exponential model simplifies optical complexity. The numerical answer belongs to a deliberately simplified scenario. Compare it against an order-of-magnitude estimate: could a change by a factor of ten in one driver plausibly change the reported quantity by that amount? Identify which omitted process would have the strongest effect if this toy calculation were used at sea. Explain why a precise printed number is not a measurement of exact physical truth.

### 5. Competing explanations, failure modes and observation quality

Using a single attenuation coefficient across colors and seasons oversimplifies marine optics. Cloud cover, sun angle and mixing depth alter a cell’s actual light history.


### 6. Research procedure and reproducibility

Use the synthetic Unit 7 dataset to carry out a compact investigation. Begin by inspecting timestamps and units; then write one falsifiable prediction about **light attenuation and the euphotic zone**. Make a first plot of raw samples, mark missing or flagged records, and only afterward compute summary statistics. Repeat the summary after removing two extreme values and explain whether the conclusion changes. If the response is strongly depth-dependent, group observations by depth before averaging. A good lab submission includes the code or spreadsheet formulas, variable definitions, a figure with readable axes, and a one-paragraph argument that separates the observed pattern from its proposed cause.


### 7. Sensitivity, limits and transfer


**Short knowledge check:** State the direct observable for light attenuation and the euphotic zone, one mechanism compatible with it, one competing explanation, the units of the lesson’s calculation, and one measurement that would discriminate between the explanations. The response should contain at least one sentence explaining why the textbook’s simplified model is not by itself a site-specific forecast.

## Lesson 7.2 — Phytoplankton growth, grazing and bloom dynamics

### 1. Physical question and core explanation

Population abundance changes with photosynthetic growth, losses, grazing, sinking and mixing. A chlorophyll concentration can rise because cells contain more pigment, not solely because cell number or carbon fixation rose. Bloom termination may result from nutrient exhaustion, grazers or vertical transport.


### 2. What to measure, and how

Construct a discrete stock budget with growth and grazing rates, and calculate one-day biomass change under fixed coefficients. Plot why doubling a rate does not always double the final standing stock when losses depend on abundance.


### 3. Mechanism, model and dimensional reasoning

In a first approximation, represent **phytoplankton growth, grazing and bloom dynamics** with an inventory, a forcing term and at least one route for exchange with surrounding water or the atmosphere. The model may be a proportionality, a conservative mixture, a flux balance, or a kinematic relation. Put units beside every variable before substituting measurements. A ratio of two volumes is dimensionless; a current is length per time; and a volume transport also includes cross-sectional area. If dimensions do not close, the numerical result cannot be correct even if a calculator produced it.


### 4. Fully worked quantitative case

**Problem — Net biomass change.** 100 units biomass grows 0.3 day−1 and loses 0.12 day−1 under Euler one-day update.

**Model and substitution:** `100*(1+.3-.12)`. Evaluate it using the units stated in the problem and the accompanying conversion factors. The result is **118 units**. Every multiplier or divisor should have a physical interpretation: cross-sectional area converts velocity to transport; elapsed time converts a rate to a stock change; a density or heat-capacity factor connects a thermodynamic state change to an energy inventory. For angular or exponent-based relationships, specify whether the input is degrees, radians or a dimensionless ratio.

**Interpretation:** Discrete approximation; rates are held fixed over one day. The numerical answer belongs to a deliberately simplified scenario. Compare it against an order-of-magnitude estimate: could a change by a factor of ten in one driver plausibly change the reported quantity by that amount? Identify which omitted process would have the strongest effect if this toy calculation were used at sea. Explain why a precise printed number is not a measurement of exact physical truth.

### 5. Competing explanations, failure modes and observation quality

Chlorophyll from fluorescence and pigments may differ across taxa and stress conditions. A net accumulation estimate does not independently measure gross primary production.


### 6. Research procedure and reproducibility

Use the synthetic Unit 7 dataset to carry out a compact investigation. Begin by inspecting timestamps and units; then write one falsifiable prediction about **phytoplankton growth, grazing and bloom dynamics**. Make a first plot of raw samples, mark missing or flagged records, and only afterward compute summary statistics. Repeat the summary after removing two extreme values and explain whether the conclusion changes. If the response is strongly depth-dependent, group observations by depth before averaging. A good lab submission includes the code or spreadsheet formulas, variable definitions, a figure with readable axes, and a one-paragraph argument that separates the observed pattern from its proposed cause.


### 7. Sensitivity, limits and transfer


**Short knowledge check:** State the direct observable for phytoplankton growth, grazing and bloom dynamics, one mechanism compatible with it, one competing explanation, the units of the lesson’s calculation, and one measurement that would discriminate between the explanations. The response should contain at least one sentence explaining why the textbook’s simplified model is not by itself a site-specific forecast.

## Lesson 7.3 — Marine food webs and the biological carbon pump

### 1. Physical question and core explanation

Food-web energy transfer is inefficient and organism-specific; particle export from surface waters transports carbon to depth. Some sinking matter is remineralized before reaching the seabed, and dissolved pathways complicate a simplistic sinking-only picture. Efficiency depends on particle size and environmental conditions.


### 2. What to measure, and how

Use an illustrative export fraction and remineralization attenuation law to compute deep export from surface production. Separate gross production, net production and export as distinct terms in a carbon budget.


### 3. Mechanism, model and dimensional reasoning

In a first approximation, represent **marine food webs and the biological carbon pump** with an inventory, a forcing term and at least one route for exchange with surrounding water or the atmosphere. The model may be a proportionality, a conservative mixture, a flux balance, or a kinematic relation. Put units beside every variable before substituting measurements. A ratio of two volumes is dimensionless; a current is length per time; and a volume transport also includes cross-sectional area. If dimensions do not close, the numerical result cannot be correct even if a calculator produced it.


### 4. Fully worked quantitative case

**Problem — Export reduction with depth.** Use F(z)=F100(z/100)^−0.8; if F100=80, calculate F1000.

**Model and substitution:** `80*(1000/100)**(-.8)`. Evaluate it using the units stated in the problem and the accompanying conversion factors. The result is **12.67915 units**. Every multiplier or divisor should have a physical interpretation: cross-sectional area converts velocity to transport; elapsed time converts a rate to a stock change; a density or heat-capacity factor connects a thermodynamic state change to an energy inventory. For angular or exponent-based relationships, specify whether the input is degrees, radians or a dimensionless ratio.

**Interpretation:** An illustrative Martin-curve scaling, not a universal law. The numerical answer belongs to a deliberately simplified scenario. Compare it against an order-of-magnitude estimate: could a change by a factor of ten in one driver plausibly change the reported quantity by that amount? Identify which omitted process would have the strongest effect if this toy calculation were used at sea. Explain why a precise printed number is not a measurement of exact physical truth.

### 5. Competing explanations, failure modes and observation quality

A fixed ecological transfer percentage applied to all species is not a global predictive law. Export estimated from sediment traps may be biased by hydrodynamics or incomplete particle capture.


### 6. Research procedure and reproducibility

Use the synthetic Unit 7 dataset to carry out a compact investigation. Begin by inspecting timestamps and units; then write one falsifiable prediction about **marine food webs and the biological carbon pump**. Make a first plot of raw samples, mark missing or flagged records, and only afterward compute summary statistics. Repeat the summary after removing two extreme values and explain whether the conclusion changes. If the response is strongly depth-dependent, group observations by depth before averaging. A good lab submission includes the code or spreadsheet formulas, variable definitions, a figure with readable axes, and a one-paragraph argument that separates the observed pattern from its proposed cause.


### 7. Sensitivity, limits and transfer


**Short knowledge check:** State the direct observable for marine food webs and the biological carbon pump, one mechanism compatible with it, one competing explanation, the units of the lesson’s calculation, and one measurement that would discriminate between the explanations. The response should contain at least one sentence explaining why the textbook’s simplified model is not by itself a site-specific forecast.

## Lesson 7.4 — Remote sensing of ocean color and ecosystem change

### 1. Physical question and core explanation

Satellite ocean color retrieves spectral radiance transformed through atmospheric correction and bio-optical algorithms. It can reveal spatial patterns in surface chlorophyll proxies, colored dissolved organic material or suspended particles, but not directly identify all species or deep populations.


### 2. What to measure, and how

Cross-validate a synthetic satellite chlorophyll estimate with near-surface bottle samples at matching times. Report regression bias, root-mean-square difference and sampling mismatch rather than relying only on correlation.


### 3. Mechanism, model and dimensional reasoning

In a first approximation, represent **remote sensing of ocean color and ecosystem change** with an inventory, a forcing term and at least one route for exchange with surrounding water or the atmosphere. The model may be a proportionality, a conservative mixture, a flux balance, or a kinematic relation. Put units beside every variable before substituting measurements. A ratio of two volumes is dimensionless; a current is length per time; and a volume transport also includes cross-sectional area. If dimensions do not close, the numerical result cannot be correct even if a calculator produced it.


### 4. Fully worked quantitative case

**Problem — Ocean color prediction bias.** Three synthetic residuals (satellite minus ship) are +0.2, −0.1, +0.3 mg/m³. Find mean bias.

**Model and substitution:** `(.2-.1+.3)/3`. Evaluate it using the units stated in the problem and the accompanying conversion factors. The result is **0.13333 mg/m³**. Every multiplier or divisor should have a physical interpretation: cross-sectional area converts velocity to transport; elapsed time converts a rate to a stock change; a density or heat-capacity factor connects a thermodynamic state change to an energy inventory. For angular or exponent-based relationships, specify whether the input is degrees, radians or a dimensionless ratio.

**Interpretation:** Small samples cannot characterize global algorithm quality. The numerical answer belongs to a deliberately simplified scenario. Compare it against an order-of-magnitude estimate: could a change by a factor of ten in one driver plausibly change the reported quantity by that amount? Identify which omitted process would have the strongest effect if this toy calculation were used at sea. Explain why a precise printed number is not a measurement of exact physical truth.

### 5. Competing explanations, failure modes and observation quality

Cloud cover creates nonrandom gaps, and turbid coastal waters challenge open-ocean algorithms. A surface optical observation should not be presented as a complete ocean productivity estimate.


### 6. Research procedure and reproducibility

Use the synthetic Unit 7 dataset to carry out a compact investigation. Begin by inspecting timestamps and units; then write one falsifiable prediction about **remote sensing of ocean color and ecosystem change**. Make a first plot of raw samples, mark missing or flagged records, and only afterward compute summary statistics. Repeat the summary after removing two extreme values and explain whether the conclusion changes. If the response is strongly depth-dependent, group observations by depth before averaging. A good lab submission includes the code or spreadsheet formulas, variable definitions, a figure with readable axes, and a one-paragraph argument that separates the observed pattern from its proposed cause.


### 7. Sensitivity, limits and transfer


**Short knowledge check:** State the direct observable for remote sensing of ocean color and ecosystem change, one mechanism compatible with it, one competing explanation, the units of the lesson’s calculation, and one measurement that would discriminate between the explanations. The response should contain at least one sentence explaining why the textbook’s simplified model is not by itself a site-specific forecast.

## Lesson 7.5 — Deep-sea ecology, hypoxia and harmful blooms

### 1. Physical question and core explanation

Seafloor ecosystems rely on sinking organic particles, lateral transport and in some settings chemosynthesis. Harmful algal blooms involve particular species and toxins rather than merely high phytoplankton abundance. Low oxygen and high nutrients can interact through physical retention and biological demand.


### 2. What to measure, and how

Compare an idealized deep-sea carbon supply with benthic oxygen consumption. For a bloom alert, combine microscopy or molecular identification with toxin measurements and circulation forecasts rather than chlorophyll alone.


### 3. Mechanism, model and dimensional reasoning

In a first approximation, represent **deep-sea ecology, hypoxia and harmful blooms** with an inventory, a forcing term and at least one route for exchange with surrounding water or the atmosphere. The model may be a proportionality, a conservative mixture, a flux balance, or a kinematic relation. Put units beside every variable before substituting measurements. A ratio of two volumes is dimensionless; a current is length per time; and a volume transport also includes cross-sectional area. If dimensions do not close, the numerical result cannot be correct even if a calculator produced it.


### 4. Fully worked quantitative case

**Problem — Benthic carbon supply.** Sinking flux is 25 units/m²/year and 30% is retained locally. Find retained input.

**Model and substitution:** `25*.3`. Evaluate it using the units stated in the problem and the accompanying conversion factors. The result is **7.5 units/m²/year**. Every multiplier or divisor should have a physical interpretation: cross-sectional area converts velocity to transport; elapsed time converts a rate to a stock change; a density or heat-capacity factor connects a thermodynamic state change to an energy inventory. For angular or exponent-based relationships, specify whether the input is degrees, radians or a dimensionless ratio.

**Interpretation:** Residence, grazing and lateral flux are simplified. The numerical answer belongs to a deliberately simplified scenario. Compare it against an order-of-magnitude estimate: could a change by a factor of ten in one driver plausibly change the reported quantity by that amount? Identify which omitted process would have the strongest effect if this toy calculation were used at sea. Explain why a precise printed number is not a measurement of exact physical truth.

### 5. Competing explanations, failure modes and observation quality

Deep-water observations are spatially sparse, and the presence of algae does not prove toxin production. Sampling during daylight and calm conditions may miss the most dangerous or biologically informative events.


### 6. Research procedure and reproducibility

Use the synthetic Unit 7 dataset to carry out a compact investigation. Begin by inspecting timestamps and units; then write one falsifiable prediction about **deep-sea ecology, hypoxia and harmful blooms**. Make a first plot of raw samples, mark missing or flagged records, and only afterward compute summary statistics. Repeat the summary after removing two extreme values and explain whether the conclusion changes. If the response is strongly depth-dependent, group observations by depth before averaging. A good lab submission includes the code or spreadsheet formulas, variable definitions, a figure with readable axes, and a one-paragraph argument that separates the observed pattern from its proposed cause.


### 7. Sensitivity, limits and transfer


**Short knowledge check:** State the direct observable for deep-sea ecology, hypoxia and harmful blooms, one mechanism compatible with it, one competing explanation, the units of the lesson’s calculation, and one measurement that would discriminate between the explanations. The response should contain at least one sentence explaining why the textbook’s simplified model is not by itself a site-specific forecast.

## Integrated field investigation: joining the five lessons

**Research setting:** A temperate shelf experiences a spring bloom after stratification develops. Observers measure fluorescence, nutrients and grazing but disagree on whether increasing color means higher daily production, higher standing stock or a different plankton community.

Begin by drawing an annotated cross-section of the hypothetical study domain. Mark the variables addressed in the five lessons: light attenuation and the euphotic zone, phytoplankton growth, grazing and bloom dynamics, marine food webs and the biological carbon pump, remote sensing of ocean color and ecosystem change, deep-sea ecology, hypoxia and harmful blooms. State a hypothesis that predicts not only that two variables covary, but why a specified flux, force, mixing process or chemical transformation would connect them. If the hypothesized mechanism acts across a boundary, label that boundary with a direction arrow and correct units. If the hypothesis involves observational aliasing, describe which repeat sample would expose it.

Use the Unit 7 CSV as **fictional practice data**, not as empirical support. Calculate the mean, median, spread and a clearly chosen depth or time contrast. Fit a basic trend only after plotting raw values; a trend through a cyclic signal may depend on the starting and ending date. Draw uncertainty bars reflecting either an explicitly assumed sensor precision or the sample variability, and never call the two interchangeable. Rewrite one claim after noticing that an instrument was calibrated differently halfway through the experiment.

**Counterfactual:** Consider that the sampling route misses the location of maximum gradient. Estimate qualitatively whether a mean, a transport or an inventory would be biased upward or downward, and explain the sign. Then compare the consequences of doubling temporal cadence versus doubling spatial coverage. Select the cheaper improvement that tests the strongest competing explanation, even if it does not make the final map more visually attractive.

**Mini-report deliverables:** (1) a diagram with all coordinate and datum choices, (2) one calculation fully worked in SI units, (3) an independent check using a second observable, (4) a paragraph naming two uncertainties and whether they are random or systematic, and (5) a decision sentence that begins with the conditions under which the evidence is adequate. Good reasoning is judged by what could invalidate it, not by whether the synthetic plot looks smooth.

## Unit review and extension

Re-read the guiding question: How do photons, nutrients, mixing and trophic interactions generate ocean ecosystems? Develop a two-column comparison between what the instruments directly measure and what the analyst hopes to infer. Explain at least three gaps between those columns. Reproduce the five solved exercises without looking at the results, and check the sensitivity of one result to a changed parameter. Demonstrate each unit model with the slider at its minimum, middle and maximum value. Finally, propose a new sampling site whose observation has the power to reject one interpretation, rather than simply providing more data of the same type.

A useful extension is to add a conservative tracer or reference measurement that responds to a different physical property. Observations become stronger when they have different failure mechanisms. A temperature record and an optical satellite product, for example, cannot replace a calibrated salinity profile, but together they may constrain a wider range of causal stories. Describe how the extension would change confidence and what inference remains beyond its reach.

### Interactive classroom model — Photosynthetically available light at 20 m

Change **attenuation coefficient (m⁻¹)** between 0.02 and 0.5 using the slider on the HTML reading page. The number displayed is in % surface; first predict the direction of change from the equation, and then verify using the control. **Model limitation:** Single exponential coefficient; spectrum and angular light field omitted.

A numerical graph is an invitation to test assumptions, not a replacement for a real observation. Try an extreme parameter setting, record whether it remains physically plausible, and name a missing mechanism. Explain how the simplified classroom response could be validated or invalidated with a real dataset.

### Interactive classroom model — Particle export reaching depth

Change **remineralization exponent** between 0.2 and 1.5 using the slider on the HTML reading page. The number displayed is in %; first predict the direction of change from the equation, and then verify using the control. **Model limitation:** Martin-type power-law toy model between 100 and 1000 m; region dependent.

A numerical graph is an invitation to test assumptions, not a replacement for a real observation. Try an extreme parameter setting, record whether it remains physically plausible, and name a missing mechanism. Explain how the simplified classroom response could be validated or invalidated with a real dataset.

