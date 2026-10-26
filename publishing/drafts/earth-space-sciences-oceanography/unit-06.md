# Unit 6 — Marine chemistry and biogeochemical cycling

## Guiding question: What constraints determine the movement and chemical transformation of substances in seawater?

**Synthetic case study:** A shelf survey reveals elevated nutrients but declining oxygen near the seabed. The class must distinguish biological consumption, transport, mixing and measurement bias before drawing conclusions about ecosystem status.

## Scientific foundations and the shape of the inquiry

The starting method in this unit is **chemical inventories and cycling**. Choose molar, mass or volume units explicitly before applying ratios; ionic concentrations cannot be combined casually with mass mixing fractions. A budget must distinguish advection, biological reactions, air–sea exchange and sinking or sediment interactions. Inventory change is not equal to a reaction rate.

**Comparative interpretation:** A fictional coastal oxygen decline accompanies a nutrient pulse after rain. Evaluate three explanations—river input, local respiration and reduced ventilation—by proposing measurements whose expected signatures differ, rather than simply choosing the most intuitive narrative.

**Fieldwork and model validation:** Collection and storage conditions can alter the sample: dissolved gases may exchange with the atmosphere, microbes can transform nutrients and containers may add contaminants. Field blanks, certified reference materials and stated detection limits are as important as the equation applied after analysis.

Oceanographic quantities generally depend on the choice of reference frame and on the boundaries of the study region. A point sensor records conditions in a small volume; a gridded map estimates a field across many cells; a process model predicts how that field should change under specified equations and boundary conditions. A student who moves directly from a point sensor to a regional mechanism is making an extrapolation that requires independent support. Keep a table recording the proposed mechanism, the predicted pattern, and the observation that would undermine it. This practice prevents a persuasive figure from becoming an unsupported explanation.

The lesson sequence moves from describing observations to relating them to mechanisms, building a tractable calculation, testing sensitivity and finally explaining what action could justifiably follow. No numerical constant in a simplified teaching exercise should be mistaken for a globally fitted parameter. The numerical questions in this unit are deliberately synthetic; their main purpose is to expose the dimensional structure of the reasoning.

## Lesson 6.1 — Seawater major ions and residence time

### 1. Physical question and core explanation

Major seawater ions show relatively stable proportions over much of the open ocean, but coastal freshwater inputs and hydrothermal sources can modify composition. Residence time is a stock divided by a flux under equilibrium assumptions, not a literal timer on an individual atom.


### 2. What to measure, and how

Calculate an idealized reservoir turnover time and perform a conservative mixing estimate for two endmember water masses. Specify whether concentration is expressed per liter, kilogram or mole of solution.


### 3. Mechanism, model and dimensional reasoning

In a first approximation, represent **seawater major ions and residence time** with an inventory, a forcing term and at least one route for exchange with surrounding water or the atmosphere. The model may be a proportionality, a conservative mixture, a flux balance, or a kinematic relation. Put units beside every variable before substituting measurements. A ratio of two volumes is dimensionless; a current is length per time; and a volume transport also includes cross-sectional area. If dimensions do not close, the numerical result cannot be correct even if a calculator produced it.


### 4. Fully worked quantitative case

**Problem — One-box turnover time.** A tracer stock is 60 million tonnes with steady removal 4 million tonnes/year. Compute stock/flux.

**Model and substitution:** `60/4`. Evaluate it using the units stated in the problem and the accompanying conversion factors. The result is **15 years**. Every multiplier or divisor should have a physical interpretation: cross-sectional area converts velocity to transport; elapsed time converts a rate to a stock change; a density or heat-capacity factor connects a thermodynamic state change to an energy inventory. For angular or exponent-based relationships, specify whether the input is degrees, radians or a dimensionless ratio.

**Interpretation:** Residence-time proxy is meaningful only under chosen steady assumptions. The numerical answer belongs to a deliberately simplified scenario. Compare it against an order-of-magnitude estimate: could a change by a factor of ten in one driver plausibly change the reported quantity by that amount? Identify which omitted process would have the strongest effect if this toy calculation were used at sea. Explain why a precise printed number is not a measurement of exact physical truth.

### 5. Competing explanations, failure modes and observation quality

Residence time can be misleading in a spatially heterogeneous, non-steady reservoir. Chemical reactions, particle scavenging and localized inputs violate the simplest one-box budget.


### 6. Research procedure and reproducibility

Use the synthetic Unit 6 dataset to carry out a compact investigation. Begin by inspecting timestamps and units; then write one falsifiable prediction about **seawater major ions and residence time**. Make a first plot of raw samples, mark missing or flagged records, and only afterward compute summary statistics. Repeat the summary after removing two extreme values and explain whether the conclusion changes. If the response is strongly depth-dependent, group observations by depth before averaging. A good lab submission includes the code or spreadsheet formulas, variable definitions, a figure with readable axes, and a one-paragraph argument that separates the observed pattern from its proposed cause.


### 7. Sensitivity, limits and transfer


**Short knowledge check:** State the direct observable for seawater major ions and residence time, one mechanism compatible with it, one competing explanation, the units of the lesson’s calculation, and one measurement that would discriminate between the explanations. The response should contain at least one sentence explaining why the textbook’s simplified model is not by itself a site-specific forecast.

## Lesson 6.2 — Carbonate system and ocean acidification

### 1. Physical question and core explanation

Dissolved inorganic carbon is distributed among aqueous CO2, bicarbonate and carbonate ions according to pH, temperature, salinity and pressure. Air–sea CO2 exchange alters acid-base balance; lower pH does not mean the ocean becomes chemically acidic in the ordinary pH-less-than-seven sense.


### 2. What to measure, and how

Track a hypothetical pH shift and calculate hydrogen-ion activity ratio as 10 to the power of the pH difference. Distinguish pH measurement scales and laboratory equilibrium from dynamic ocean exchange.


### 3. Mechanism, model and dimensional reasoning

In a first approximation, represent **carbonate system and ocean acidification** with an inventory, a forcing term and at least one route for exchange with surrounding water or the atmosphere. The model may be a proportionality, a conservative mixture, a flux balance, or a kinematic relation. Put units beside every variable before substituting measurements. A ratio of two volumes is dimensionless; a current is length per time; and a volume transport also includes cross-sectional area. If dimensions do not close, the numerical result cannot be correct even if a calculator produced it.


### 4. Fully worked quantitative case

**Problem — Hydrogen-ion activity ratio.** Compare a change from pH 8.1 to 8.0 on same scale. Compute final/initial H+ activity.

**Model and substitution:** `10**(.1)`. Evaluate it using the units stated in the problem and the accompanying conversion factors. The result is **1.25893 ratio**. Every multiplier or divisor should have a physical interpretation: cross-sectional area converts velocity to transport; elapsed time converts a rate to a stock change; a density or heat-capacity factor connects a thermodynamic state change to an energy inventory. For angular or exponent-based relationships, specify whether the input is degrees, radians or a dimensionless ratio.

**Interpretation:** A pH difference cannot uniquely specify carbonate ion concentrations. The numerical answer belongs to a deliberately simplified scenario. Compare it against an order-of-magnitude estimate: could a change by a factor of ten in one driver plausibly change the reported quantity by that amount? Identify which omitted process would have the strongest effect if this toy calculation were used at sea. Explain why a precise printed number is not a measurement of exact physical truth.

### 5. Competing explanations, failure modes and observation quality

Carbonate calculations require equilibrium constants, total alkalinity and consistent units. A one-variable pH model cannot predict local organism calcification or saturation state precisely.


### 6. Research procedure and reproducibility

Use the synthetic Unit 6 dataset to carry out a compact investigation. Begin by inspecting timestamps and units; then write one falsifiable prediction about **carbonate system and ocean acidification**. Make a first plot of raw samples, mark missing or flagged records, and only afterward compute summary statistics. Repeat the summary after removing two extreme values and explain whether the conclusion changes. If the response is strongly depth-dependent, group observations by depth before averaging. A good lab submission includes the code or spreadsheet formulas, variable definitions, a figure with readable axes, and a one-paragraph argument that separates the observed pattern from its proposed cause.


### 7. Sensitivity, limits and transfer


**Short knowledge check:** State the direct observable for carbonate system and ocean acidification, one mechanism compatible with it, one competing explanation, the units of the lesson’s calculation, and one measurement that would discriminate between the explanations. The response should contain at least one sentence explaining why the textbook’s simplified model is not by itself a site-specific forecast.

## Lesson 6.3 — Nutrients, primary production and Redfield thinking

### 1. Physical question and core explanation

Nitrogen, phosphorus, silica and iron can constrain phytoplankton growth differently across regions and taxa. Redfield-type atomic ratios are useful reference concepts but not rigid cellular recipes. Upwelling replenishes surface nutrients while sinking particles redistribute biogenic matter.


### 2. What to measure, and how

Use a simplified N:P ratio to identify candidate limitation in a fictional bottle assay, then design a factorial addition experiment. Compare nutrient standing stocks with measured uptake to avoid confusing concentration with production.


### 3. Mechanism, model and dimensional reasoning

In a first approximation, represent **nutrients, primary production and redfield thinking** with an inventory, a forcing term and at least one route for exchange with surrounding water or the atmosphere. The model may be a proportionality, a conservative mixture, a flux balance, or a kinematic relation. Put units beside every variable before substituting measurements. A ratio of two volumes is dimensionless; a current is length per time; and a volume transport also includes cross-sectional area. If dimensions do not close, the numerical result cannot be correct even if a calculator produced it.


### 4. Fully worked quantitative case

**Problem — N:P molar ratio.** A sample contains 18 micromol/kg nitrate and 1.2 micromol/kg phosphate. Find molar N:P.

**Model and substitution:** `18/1.2`. Evaluate it using the units stated in the problem and the accompanying conversion factors. The result is **15 ratio**. Every multiplier or divisor should have a physical interpretation: cross-sectional area converts velocity to transport; elapsed time converts a rate to a stock change; a density or heat-capacity factor connects a thermodynamic state change to an energy inventory. For angular or exponent-based relationships, specify whether the input is degrees, radians or a dimensionless ratio.

**Interpretation:** Not a stand-alone diagnosis of growth limitation. The numerical answer belongs to a deliberately simplified scenario. Compare it against an order-of-magnitude estimate: could a change by a factor of ten in one driver plausibly change the reported quantity by that amount? Identify which omitted process would have the strongest effect if this toy calculation were used at sea. Explain why a precise printed number is not a measurement of exact physical truth.

### 5. Competing explanations, failure modes and observation quality

Low nitrate does not prove nitrogen limitation: rapid recycling can maintain low concentrations alongside high turnover. Co-limitation, light and grazing must be considered.


### 6. Research procedure and reproducibility

Use the synthetic Unit 6 dataset to carry out a compact investigation. Begin by inspecting timestamps and units; then write one falsifiable prediction about **nutrients, primary production and redfield thinking**. Make a first plot of raw samples, mark missing or flagged records, and only afterward compute summary statistics. Repeat the summary after removing two extreme values and explain whether the conclusion changes. If the response is strongly depth-dependent, group observations by depth before averaging. A good lab submission includes the code or spreadsheet formulas, variable definitions, a figure with readable axes, and a one-paragraph argument that separates the observed pattern from its proposed cause.


### 7. Sensitivity, limits and transfer


**Short knowledge check:** State the direct observable for nutrients, primary production and redfield thinking, one mechanism compatible with it, one competing explanation, the units of the lesson’s calculation, and one measurement that would discriminate between the explanations. The response should contain at least one sentence explaining why the textbook’s simplified model is not by itself a site-specific forecast.

## Lesson 6.4 — Dissolved oxygen, hypoxia and ventilation

### 1. Physical question and core explanation

Oxygen enters near the surface through gas exchange and photosynthesis and is consumed by respiration and organic matter oxidation. Solubility depends on temperature and salinity; bottom-water oxygen also depends on ventilation pathways and stratification. Oxygen-minimum zones are shaped by transport and biology.


### 2. What to measure, and how

Convert dissolved oxygen units consistently and sketch a depth profile showing a near-surface maximum and intermediate minimum. Set up oxygen stock change as supply minus consumption for a bounded box.


### 3. Mechanism, model and dimensional reasoning

In a first approximation, represent **dissolved oxygen, hypoxia and ventilation** with an inventory, a forcing term and at least one route for exchange with surrounding water or the atmosphere. The model may be a proportionality, a conservative mixture, a flux balance, or a kinematic relation. Put units beside every variable before substituting measurements. A ratio of two volumes is dimensionless; a current is length per time; and a volume transport also includes cross-sectional area. If dimensions do not close, the numerical result cannot be correct even if a calculator produced it.


### 4. Fully worked quantitative case

**Problem — Oxygen stock.** A 2e6 m³ box contains 0.008 kg/m³ dissolved oxygen (8 mg/L). Compute stock.

**Model and substitution:** `2e6*.008`. Evaluate it using the units stated in the problem and the accompanying conversion factors. The result is **16000 kg**. Every multiplier or divisor should have a physical interpretation: cross-sectional area converts velocity to transport; elapsed time converts a rate to a stock change; a density or heat-capacity factor connects a thermodynamic state change to an energy inventory. For angular or exponent-based relationships, specify whether the input is degrees, radians or a dimensionless ratio.

**Interpretation:** Uniform 8 mg/L concentration assumed across the entire box. The numerical answer belongs to a deliberately simplified scenario. Compare it against an order-of-magnitude estimate: could a change by a factor of ten in one driver plausibly change the reported quantity by that amount? Identify which omitted process would have the strongest effect if this toy calculation were used at sea. Explain why a precise printed number is not a measurement of exact physical truth.

### 5. Competing explanations, failure modes and observation quality

A single low oxygen reading may reflect calibration error, a real event or unrepresentative sampling. Nutrient concentration, oxygen and chlorophyll should not be assumed to move together everywhere.


### 6. Research procedure and reproducibility

Use the synthetic Unit 6 dataset to carry out a compact investigation. Begin by inspecting timestamps and units; then write one falsifiable prediction about **dissolved oxygen, hypoxia and ventilation**. Make a first plot of raw samples, mark missing or flagged records, and only afterward compute summary statistics. Repeat the summary after removing two extreme values and explain whether the conclusion changes. If the response is strongly depth-dependent, group observations by depth before averaging. A good lab submission includes the code or spreadsheet formulas, variable definitions, a figure with readable axes, and a one-paragraph argument that separates the observed pattern from its proposed cause.


### 7. Sensitivity, limits and transfer


**Short knowledge check:** State the direct observable for dissolved oxygen, hypoxia and ventilation, one mechanism compatible with it, one competing explanation, the units of the lesson’s calculation, and one measurement that would discriminate between the explanations. The response should contain at least one sentence explaining why the textbook’s simplified model is not by itself a site-specific forecast.

## Lesson 6.5 — Trace metals, pollutants and marine debris

### 1. Physical question and core explanation

Trace elements may be essential at small doses and harmful at larger exposures. Their bioavailability depends on chemical speciation, ligand binding and particles, while plastics vary by size, shape, material and weathering. Reliable pollution attribution requires identifying sources and transport.


### 2. What to measure, and how

Design a blank-corrected sampling chain for a dissolved-metal analysis; for debris, count particles with explicit mesh size and detection limits. Compare concentrations with fluxes through a waterway cross-section.


### 3. Mechanism, model and dimensional reasoning

In a first approximation, represent **trace metals, pollutants and marine debris** with an inventory, a forcing term and at least one route for exchange with surrounding water or the atmosphere. The model may be a proportionality, a conservative mixture, a flux balance, or a kinematic relation. Put units beside every variable before substituting measurements. A ratio of two volumes is dimensionless; a current is length per time; and a volume transport also includes cross-sectional area. If dimensions do not close, the numerical result cannot be correct even if a calculator produced it.


### 4. Fully worked quantitative case

**Problem — Pollutant load.** A waterway discharges 40 m³/s at 0.02 mg/L. Compute kg/day.

**Model and substitution:** `40*.02*1e-3*86400`. Evaluate it using the units stated in the problem and the accompanying conversion factors. The result is **69.12 kg/day**. Every multiplier or divisor should have a physical interpretation: cross-sectional area converts velocity to transport; elapsed time converts a rate to a stock change; a density or heat-capacity factor connects a thermodynamic state change to an energy inventory. For angular or exponent-based relationships, specify whether the input is degrees, radians or a dimensionless ratio.

**Interpretation:** 1 mg/L equals 1 g/m³; check unit conversion. The numerical answer belongs to a deliberately simplified scenario. Compare it against an order-of-magnitude estimate: could a change by a factor of ten in one driver plausibly change the reported quantity by that amount? Identify which omitted process would have the strongest effect if this toy calculation were used at sea. Explain why a precise printed number is not a measurement of exact physical truth.

### 5. Competing explanations, failure modes and observation quality

Sampling bottles and ship equipment can contaminate trace-metal samples. A debris count obtained with one mesh cannot be compared naively with a study using a much finer mesh.


### 6. Research procedure and reproducibility

Use the synthetic Unit 6 dataset to carry out a compact investigation. Begin by inspecting timestamps and units; then write one falsifiable prediction about **trace metals, pollutants and marine debris**. Make a first plot of raw samples, mark missing or flagged records, and only afterward compute summary statistics. Repeat the summary after removing two extreme values and explain whether the conclusion changes. If the response is strongly depth-dependent, group observations by depth before averaging. A good lab submission includes the code or spreadsheet formulas, variable definitions, a figure with readable axes, and a one-paragraph argument that separates the observed pattern from its proposed cause.


### 7. Sensitivity, limits and transfer


**Short knowledge check:** State the direct observable for trace metals, pollutants and marine debris, one mechanism compatible with it, one competing explanation, the units of the lesson’s calculation, and one measurement that would discriminate between the explanations. The response should contain at least one sentence explaining why the textbook’s simplified model is not by itself a site-specific forecast.

## Integrated field investigation: joining the five lessons

**Research setting:** A shelf survey reveals elevated nutrients but declining oxygen near the seabed. The class must distinguish biological consumption, transport, mixing and measurement bias before drawing conclusions about ecosystem status.

Begin by drawing an annotated cross-section of the hypothetical study domain. Mark the variables addressed in the five lessons: seawater major ions and residence time, carbonate system and ocean acidification, nutrients, primary production and redfield thinking, dissolved oxygen, hypoxia and ventilation, trace metals, pollutants and marine debris. State a hypothesis that predicts not only that two variables covary, but why a specified flux, force, mixing process or chemical transformation would connect them. If the hypothesized mechanism acts across a boundary, label that boundary with a direction arrow and correct units. If the hypothesis involves observational aliasing, describe which repeat sample would expose it.

Use the Unit 6 CSV as **fictional practice data**, not as empirical support. Calculate the mean, median, spread and a clearly chosen depth or time contrast. Fit a basic trend only after plotting raw values; a trend through a cyclic signal may depend on the starting and ending date. Draw uncertainty bars reflecting either an explicitly assumed sensor precision or the sample variability, and never call the two interchangeable. Rewrite one claim after noticing that an instrument was calibrated differently halfway through the experiment.

**Counterfactual:** Consider that the sampling route misses the location of maximum gradient. Estimate qualitatively whether a mean, a transport or an inventory would be biased upward or downward, and explain the sign. Then compare the consequences of doubling temporal cadence versus doubling spatial coverage. Select the cheaper improvement that tests the strongest competing explanation, even if it does not make the final map more visually attractive.

**Mini-report deliverables:** (1) a diagram with all coordinate and datum choices, (2) one calculation fully worked in SI units, (3) an independent check using a second observable, (4) a paragraph naming two uncertainties and whether they are random or systematic, and (5) a decision sentence that begins with the conditions under which the evidence is adequate. Good reasoning is judged by what could invalidate it, not by whether the synthetic plot looks smooth.

## Unit review and extension

Re-read the guiding question: What constraints determine the movement and chemical transformation of substances in seawater? Develop a two-column comparison between what the instruments directly measure and what the analyst hopes to infer. Explain at least three gaps between those columns. Reproduce the five solved exercises without looking at the results, and check the sensitivity of one result to a changed parameter. Demonstrate each unit model with the slider at its minimum, middle and maximum value. Finally, propose a new sampling site whose observation has the power to reject one interpretation, rather than simply providing more data of the same type.

A useful extension is to add a conservative tracer or reference measurement that responds to a different physical property. Observations become stronger when they have different failure mechanisms. A temperature record and an optical satellite product, for example, cannot replace a calibrated salinity profile, but together they may constrain a wider range of causal stories. Describe how the extension would change confidence and what inference remains beyond its reach.

### Interactive classroom model — Hydrogen-ion activity ratio to pH 8.1

Change **comparison ph** between 7.4 and 8.5 using the slider on the HTML reading page. The number displayed is in ratio; first predict the direction of change from the equation, and then verify using the control. **Model limitation:** Activity ratio in a consistent pH scale; not an estimate of carbonate saturation.

A numerical graph is an invitation to test assumptions, not a replacement for a real observation. Try an extreme parameter setting, record whether it remains physically plausible, and name a missing mechanism. Explain how the simplified classroom response could be validated or invalidated with a real dataset.

### Interactive classroom model — One-box residence-time proxy

Change **reservoir stock (million tonnes)** between 1 and 100 using the slider on the HTML reading page. The number displayed is in years; first predict the direction of change from the equation, and then verify using the control. **Model limitation:** Steady sink at 3 million tonnes/year; no recirculation or storage trend.

A numerical graph is an invitation to test assumptions, not a replacement for a real observation. Try an extreme parameter setting, record whether it remains physically plausible, and name a missing mechanism. Explain how the simplified classroom response could be validated or invalidated with a real dataset.

