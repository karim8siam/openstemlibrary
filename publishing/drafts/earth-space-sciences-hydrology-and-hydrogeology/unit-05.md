# Unit 5 — Aquifer testing and groundwater–surface-water exchange

## Scientific problem for this unit

How can field tests distinguish aquifer properties from transient boundary effects? The case-study setting is: **Interpret a fictional well-test campaign alongside stream seepage.**. The central difficulty is that the same observed water level, hydrograph, concentration or land-surface change can arise from multiple physical causes. A course in hydrology becomes useful when students learn to infer processes cautiously rather than replacing a missing measurement with a convenient story. This unit integrates conservation laws, field observables and independent checks in a coherent investigation.

### Background and field context

A managed aquifer beside a river and a municipal abstraction well. The investigation asks students to define a measurement support, write the governing equation with correct units, and make a prediction before inspecting hypothetical data. Drawdown is a transient pressure response. A local well test may estimate a hydraulic property under simplifying boundaries, while a longer record integrates pumping schedules, seasonal recharge, stream capture and distant stresses. Students should keep a concise field ledger indicating which variables were measured, which were derived, and which were assigned because the problem did not provide enough data.

The unifying tools are dimensional reasoning, boundary diagrams and comparison of rival conceptual models. Wells, pumping, recovery, slug tests, springs, gaining and losing streams all become difficult when scales are mixed, when a sensor's datum is omitted, or when statistical fit is confused with causal evidence. Draw one section or plan view that labels land surface, relevant geological horizons, the stream or well network, and the water-transfer pathways under discussion. Give a sign convention to every flux. For quantities reported as volumes, identify the integration interval and contributing area. Explain why the chosen model domain includes or excludes neighboring exchanges.

### Reading and learning outcomes

Students should be able to calculate a conditional result, describe at least two competing processes, identify limitations of measurement, and write a short reproducible report. Alongside the five lessons, the unit includes a synthetic laboratory dataset and two illustrative slider-driven equations. These models are deliberately simple: use them to see parameter sensitivity, not to recommend operational changes. Any inference about actual water quality, flood hazard or well yield requires site data, qualified review and the relevant authorities.

## Lesson 5.1 — Wells, piezometers and measurement reference

### How the process works

A groundwater observation is the head within the interval hydraulically connected to a screened well. Construction, screen length, well development and datum quality affect the interpretation. Begin with a drawing of the physical stores and fluxes relevant to **wells, piezometers and measurement reference**, showing both the water-bearing materials and the chosen observation boundary. Explain which forces move the water, solute or energy; identify the reference datum if hydraulic head or elevation is involved. A catchment outlet, soil column, well screen and river reach measure different domains. Never describe the value at one instrument as a universal property without a scaling argument. Distinguish a conservation relationship, which must hold for a correctly bounded system, from a constitutive equation, whose coefficients require calibration and whose validity is conditional on site conditions.

### Evidence, ambiguity and falsifiable alternatives

Borehole records, screen coordinates, reference elevations, water-level tapes, logger offsets and purging notes are essential metadata. For every proposed observation, record units, location, date, time step, instrument support and an independent quality check. Sketch what is measured directly and what must be inferred. Estimate an error or detection limit if the result will be compared across sites or dates. Changes that are smaller than the relevant error should not be described as robust physical trends.

A transient water-level change can reflect sensor drift, an obstructed screen or atmospheric pressure rather than aquifer forcing. A scientifically serious explanation must accommodate rival mechanisms. Identify what the preferred mechanism would predict at another time, depth or location. Choose a second type of evidence—geological context, temperature, chemical tracers, parallel reference catchments or independently surveyed elevations—rather than only refitting the same data. An observation that both models predict equally well is not a discriminating test.

### Worked calculation — Elevation head from tape

**Illustrative data:** Well reference elevation=123.4 m, water depth below reference=7.2 m. **Equation or arithmetic:** `123.4-7.2`. **Answer: 116.2 m head**. State why the inputs have compatible units, and explain which water store, flux, property, probability or statistic the output actually represents. For mixed units, write intermediate conversions explicitly. Distinguish the numerical answer from a claim about the real-world process: the answer follows from the invented inputs and the chosen equation, not from measurements of an actual catchment or aquifer.

**Sensitivity and limits:** Inconsistent surveying datums may create fictitious head gradients. If an input is changed by 20%, calculate the new output and describe whether the response is linear or nonlinear. Where appropriate, identify an excluded term or an assumption about spatial uniformity, stationarity, constant flow, conservative chemistry, or homogeneous porous media. This calculation cannot establish the excluded term is zero merely because it produces a tidy result.

### Field or data investigation

Convert depth-to-water measurements to head relative to a surveyed elevation; repeat under a deliberate sensor-offset scenario. Put this in the unit investigation setting: A managed aquifer beside a river and a municipal abstraction well. Well data quality; Record depth relative to measuring point and official datum. The monitoring sheet should retain raw values, calibration and a flag for missing or questionable samples. Before interpreting a change, ask whether an independent instrument would observe the same sign and magnitude. A river losing water during low stage might reflect natural gradient reversal or nearby pumping. Simultaneous stream and groundwater levels offer stronger evidence than a single spot gauging. Use a baseline scenario and an alternative scenario with an explicit change in just one assumption, so that the cause of the model's different output remains visible.

### Interpretation and practical constraints

Poorly constructed wells can connect layers or cause contamination; only qualified professionals should install or alter them. Reject unlocated or undocumented screens in flow-direction inference; Test the effect of 0.25 m instrument offset. Break uncertainty into instrumental accuracy, insufficient temporal or spatial sampling, uncertain model coefficients and uncertainty about the governing mechanism itself. These sources can dominate in different circumstances. Report what could make a conclusion false, not merely a plus–minus range attached to a fitted number. An actual abstraction limit, well safety decision, contamination assessment or flood warning requires locally measured and professionally reviewed evidence.

### Problems and answer checks

1. **Calculation and units:** reproduce the example and then change one input by 20%. Retain units at every line and verify that the result is dimensionally meaningful.
2. **Scientific discrimination:** write two competing explanations for the described observations, and give the exact sampling location, instrument and predicted difference that could resolve them.
3. **Transferability:** explain which key assumption is most likely to break in a different soil, geology, season, flow regime or monitoring technology. Design a quick test.
4. **Evidence memo:** distinguish observations, computed quantities and interpretations in a five-sentence note. State a follow-up observation that could reverse the judgment.

**Answer guidance:** a sound answer includes the governing relationship, a physically appropriate measurement boundary, checks on units and uncertainty, and one genuinely differentiating field test. Numerical precision alone does not strengthen an unsupported hydrologic interpretation.

## Lesson 5.2 — Pumping tests and drawdown

### How the process works

Pump-induced drawdown depends on transmissivity, storativity, pumping history and aquifer boundaries. Analytical curves apply only when their simplifying conditions are reasonably met. Begin with a drawing of the physical stores and fluxes relevant to **pumping tests and drawdown**, showing both the water-bearing materials and the chosen observation boundary. Explain which forces move the water, solute or energy; identify the reference datum if hydraulic head or elevation is involved. A catchment outlet, soil column, well screen and river reach measure different domains. Never describe the value at one instrument as a universal property without a scaling argument. Distinguish a conservation relationship, which must hold for a correctly bounded system, from a constitutive equation, whose coefficients require calibration and whose validity is conditional on site conditions.

### Evidence, ambiguity and falsifiable alternatives

Controlled discharge, recovery, observation wells and monitoring of nearby pumping help separate aquifer signal from operations. For every proposed observation, record units, location, date, time step, instrument support and an independent quality check. Sketch what is measured directly and what must be inferred. Estimate an error or detection limit if the result will be compared across sites or dates. Changes that are smaller than the relevant error should not be described as robust physical trends.

Late-time flattening may indicate recharge boundary effects or a variable pumping rate; one drawdown curve does not uniquely identify either. A scientifically serious explanation must accommodate rival mechanisms. Identify what the preferred mechanism would predict at another time, depth or location. Choose a second type of evidence—geological context, temperature, chemical tracers, parallel reference catchments or independently surveyed elevations—rather than only refitting the same data. An observation that both models predict equally well is not a discriminating test.

### Worked calculation — Confined well drawdown approximation

**Illustrative data:** Q=400 m³/day, T=250 m²/day, t=10 day, radius=20 m, S=0.001. **Equation or arithmetic:** `2.3*400/(4*math.pi*250)*math.log10(2.25*250*10/(20**2*.001))`. **Answer: 1.2147 m**. State why the inputs have compatible units, and explain which water store, flux, property, probability or statistic the output actually represents. For mixed units, write intermediate conversions explicitly. Distinguish the numerical answer from a claim about the real-world process: the answer follows from the invented inputs and the chosen equation, not from measurements of an actual catchment or aquifer.

**Sensitivity and limits:** Cooper–Jacob late-time conditions and constant-rate confined setting are not verified. If an input is changed by 20%, calculate the new output and describe whether the response is linear or nonlinear. Where appropriate, identify an excluded term or an assumption about spatial uniformity, stationarity, constant flow, conservative chemistry, or homogeneous porous media. This calculation cannot establish the excluded term is zero merely because it produces a tidy result.

### Field or data investigation

Analyze a simplified confined-aquifer scenario with the Cooper-Jacob logarithmic approximation and its validity limits. Put this in the unit investigation setting: A managed aquifer beside a river and a municipal abstraction well. Well-test assumptions; Separate pumping rate variation from aquifer response. The monitoring sheet should retain raw values, calibration and a flag for missing or questionable samples. Before interpreting a change, ask whether an independent instrument would observe the same sign and magnitude. A river losing water during low stage might reflect natural gradient reversal or nearby pumping. Simultaneous stream and groundwater levels offer stronger evidence than a single spot gauging. Use a baseline scenario and an alternative scenario with an explicit change in just one assumption, so that the cause of the model's different output remains visible.

### Interpretation and practical constraints

A classroom calculation is not a site-specific pumping yield recommendation or safe abstraction limit. Check boundary and late-time assumptions; Show how uncertain transmissivity changes computed drawdown. Break uncertainty into instrumental accuracy, insufficient temporal or spatial sampling, uncertain model coefficients and uncertainty about the governing mechanism itself. These sources can dominate in different circumstances. Report what could make a conclusion false, not merely a plus–minus range attached to a fitted number. An actual abstraction limit, well safety decision, contamination assessment or flood warning requires locally measured and professionally reviewed evidence.

### Problems and answer checks

1. **Calculation and units:** reproduce the example and then change one input by 20%. Retain units at every line and verify that the result is dimensionally meaningful.
2. **Scientific discrimination:** write two competing explanations for the described observations, and give the exact sampling location, instrument and predicted difference that could resolve them.
3. **Transferability:** explain which key assumption is most likely to break in a different soil, geology, season, flow regime or monitoring technology. Design a quick test.
4. **Evidence memo:** distinguish observations, computed quantities and interpretations in a five-sentence note. State a follow-up observation that could reverse the judgment.

**Answer guidance:** a sound answer includes the governing relationship, a physically appropriate measurement boundary, checks on units and uncertainty, and one genuinely differentiating field test. Numerical precision alone does not strengthen an unsupported hydrologic interpretation.

## Lesson 5.3 — Slug tests and local conductivity

### How the process works

A slug test perturbs head rapidly within a well; recovery is influenced by near-well conductivity, screen geometry and skin effects. It samples a more local domain than extended pumping. Begin with a drawing of the physical stores and fluxes relevant to **slug tests and local conductivity**, showing both the water-bearing materials and the chosen observation boundary. Explain which forces move the water, solute or energy; identify the reference datum if hydraulic head or elevation is involved. A catchment outlet, soil column, well screen and river reach measure different domains. Never describe the value at one instrument as a universal property without a scaling argument. Distinguish a conservation relationship, which must hold for a correctly bounded system, from a constitutive equation, whose coefficients require calibration and whose validity is conditional on site conditions.

### Evidence, ambiguity and falsifiable alternatives

High-frequency pressure logger data, well dimensions and repeated positive/negative displacements support interpretation. For every proposed observation, record units, location, date, time step, instrument support and an independent quality check. Sketch what is measured directly and what must be inferred. Estimate an error or detection limit if the result will be compared across sites or dates. Changes that are smaller than the relevant error should not be described as robust physical trends.

Slow recovery can be caused by incomplete development or a low-permeability skin zone, not the broader aquifer. A scientifically serious explanation must accommodate rival mechanisms. Identify what the preferred mechanism would predict at another time, depth or location. Choose a second type of evidence—geological context, temperature, chemical tracers, parallel reference catchments or independently surveyed elevations—rather than only refitting the same data. An observation that both models predict equally well is not a discriminating test.

### Worked calculation — Slug-test recovery half-life

**Illustrative data:** Under a toy exponential recovery, normalized head falls from 1 to 0.25 in 6 minutes. **Equation or arithmetic:** `math.log(4)/6`. **Answer: 0.23105 min⁻¹ rate constant**. State why the inputs have compatible units, and explain which water store, flux, property, probability or statistic the output actually represents. For mixed units, write intermediate conversions explicitly. Distinguish the numerical answer from a claim about the real-world process: the answer follows from the invented inputs and the chosen equation, not from measurements of an actual catchment or aquifer.

**Sensitivity and limits:** A near-well skin may dominate recovery rather than regional conductivity. If an input is changed by 20%, calculate the new output and describe whether the response is linear or nonlinear. Where appropriate, identify an excluded term or an assumption about spatial uniformity, stationarity, constant flow, conservative chemistry, or homogeneous porous media. This calculation cannot establish the excluded term is zero merely because it produces a tidy result.

### Field or data investigation

Compare normalized recovery at two times under a simple exponential teaching curve and identify which test conditions violate that simplification. Put this in the unit investigation setting: A managed aquifer beside a river and a municipal abstraction well. Near-well tests; Consider skin, screen geometry and well development. The monitoring sheet should retain raw values, calibration and a flag for missing or questionable samples. Before interpreting a change, ask whether an independent instrument would observe the same sign and magnitude. A river losing water during low stage might reflect natural gradient reversal or nearby pumping. Simultaneous stream and groundwater levels offer stronger evidence than a single spot gauging. Use a baseline scenario and an alternative scenario with an explicit change in just one assumption, so that the cause of the model's different output remains visible.

### Interpretation and practical constraints

Do not infer basin-scale transmissivity from one local test without a representative design. Use repeated recovery curves and explicit logger frequency; Compare two exponential fits before physical interpretation. Break uncertainty into instrumental accuracy, insufficient temporal or spatial sampling, uncertain model coefficients and uncertainty about the governing mechanism itself. These sources can dominate in different circumstances. Report what could make a conclusion false, not merely a plus–minus range attached to a fitted number. An actual abstraction limit, well safety decision, contamination assessment or flood warning requires locally measured and professionally reviewed evidence.

### Problems and answer checks

1. **Calculation and units:** reproduce the example and then change one input by 20%. Retain units at every line and verify that the result is dimensionally meaningful.
2. **Scientific discrimination:** write two competing explanations for the described observations, and give the exact sampling location, instrument and predicted difference that could resolve them.
3. **Transferability:** explain which key assumption is most likely to break in a different soil, geology, season, flow regime or monitoring technology. Design a quick test.
4. **Evidence memo:** distinguish observations, computed quantities and interpretations in a five-sentence note. State a follow-up observation that could reverse the judgment.

**Answer guidance:** a sound answer includes the governing relationship, a physically appropriate measurement boundary, checks on units and uncertainty, and one genuinely differentiating field test. Numerical precision alone does not strengthen an unsupported hydrologic interpretation.

## Lesson 5.4 — Springs, rivers and aquifer exchange

### How the process works

Gaining reaches receive groundwater discharge; losing reaches recharge adjacent sediments or aquifers. Exchange can change sign by season, stage and pumping. Begin with a drawing of the physical stores and fluxes relevant to **springs, rivers and aquifer exchange**, showing both the water-bearing materials and the chosen observation boundary. Explain which forces move the water, solute or energy; identify the reference datum if hydraulic head or elevation is involved. A catchment outlet, soil column, well screen and river reach measure different domains. Never describe the value at one instrument as a universal property without a scaling argument. Distinguish a conservation relationship, which must hold for a correctly bounded system, from a constitutive equation, whose coefficients require calibration and whose validity is conditional on site conditions.

### Evidence, ambiguity and falsifiable alternatives

Paired stream gaugings, seepage meters, temperature fibers and piezometric gradients offer partially independent evidence. For every proposed observation, record units, location, date, time step, instrument support and an independent quality check. Sketch what is measured directly and what must be inferred. Estimate an error or detection limit if the result will be compared across sites or dates. Changes that are smaller than the relevant error should not be described as robust physical trends.

Apparent downstream loss may be caused by water diversion or gauging uncertainty rather than seepage. A scientifically serious explanation must accommodate rival mechanisms. Identify what the preferred mechanism would predict at another time, depth or location. Choose a second type of evidence—geological context, temperature, chemical tracers, parallel reference catchments or independently surveyed elevations—rather than only refitting the same data. An observation that both models predict equally well is not a discriminating test.

### Worked calculation — River seepage screening

**Illustrative data:** Upstream 5.2 m³/s, side inflows 0.4 m³/s, abstractions 0.1 m³/s, downstream 5.1 m³/s. **Equation or arithmetic:** `5.2+.4-.1-5.1`. **Answer: 0.4 m³/s loss**. State why the inputs have compatible units, and explain which water store, flux, property, probability or statistic the output actually represents. For mixed units, write intermediate conversions explicitly. Distinguish the numerical answer from a claim about the real-world process: the answer follows from the invented inputs and the chosen equation, not from measurements of an actual catchment or aquifer.

**Sensitivity and limits:** The residual also includes gauging error and ungauged exchanges. If an input is changed by 20%, calculate the new output and describe whether the response is linear or nonlinear. Where appropriate, identify an excluded term or an assumption about spatial uniformity, stationarity, constant flow, conservative chemistry, or homogeneous porous media. This calculation cannot establish the excluded term is zero merely because it produces a tidy result.

### Field or data investigation

Construct an upstream-downstream river water balance that includes tributaries and withdrawals before assigning exchange flux. Put this in the unit investigation setting: A managed aquifer beside a river and a municipal abstraction well. Surface-groundwater coupling; Include diversion and ungauged tributaries in stream balance. The monitoring sheet should retain raw values, calibration and a flag for missing or questionable samples. Before interpreting a change, ask whether an independent instrument would observe the same sign and magnitude. A river losing water during low stage might reflect natural gradient reversal or nearby pumping. Simultaneous stream and groundwater levels offer stronger evidence than a single spot gauging. Use a baseline scenario and an alternative scenario with an explicit change in just one assumption, so that the cause of the model's different output remains visible.

### Interpretation and practical constraints

A single seepage run cannot characterize seasonal stream-aquifer connectivity. Contrast hydraulic head and temperature evidence; Calculate gains and losses with gauging uncertainty. Break uncertainty into instrumental accuracy, insufficient temporal or spatial sampling, uncertain model coefficients and uncertainty about the governing mechanism itself. These sources can dominate in different circumstances. Report what could make a conclusion false, not merely a plus–minus range attached to a fitted number. An actual abstraction limit, well safety decision, contamination assessment or flood warning requires locally measured and professionally reviewed evidence.

### Problems and answer checks

1. **Calculation and units:** reproduce the example and then change one input by 20%. Retain units at every line and verify that the result is dimensionally meaningful.
2. **Scientific discrimination:** write two competing explanations for the described observations, and give the exact sampling location, instrument and predicted difference that could resolve them.
3. **Transferability:** explain which key assumption is most likely to break in a different soil, geology, season, flow regime or monitoring technology. Design a quick test.
4. **Evidence memo:** distinguish observations, computed quantities and interpretations in a five-sentence note. State a follow-up observation that could reverse the judgment.

**Answer guidance:** a sound answer includes the governing relationship, a physically appropriate measurement boundary, checks on units and uncertainty, and one genuinely differentiating field test. Numerical precision alone does not strengthen an unsupported hydrologic interpretation.

## Lesson 5.5 — Managed recharge and abstraction effects

### How the process works

Artificial recharge, pumping and land-use choices alter head gradients, transit times and connected streamflow. A pumping well may capture water formerly discharging to wetlands. Begin with a drawing of the physical stores and fluxes relevant to **managed recharge and abstraction effects**, showing both the water-bearing materials and the chosen observation boundary. Explain which forces move the water, solute or energy; identify the reference datum if hydraulic head or elevation is involved. A catchment outlet, soil column, well screen and river reach measure different domains. Never describe the value at one instrument as a universal property without a scaling argument. Distinguish a conservation relationship, which must hold for a correctly bounded system, from a constitutive equation, whose coefficients require calibration and whose validity is conditional on site conditions.

### Evidence, ambiguity and falsifiable alternatives

Multi-year heads, groundwater budgets, streamflow, ecological indicators and chemical tracers support evaluation. For every proposed observation, record units, location, date, time step, instrument support and an independent quality check. Sketch what is measured directly and what must be inferred. Estimate an error or detection limit if the result will be compared across sites or dates. Changes that are smaller than the relevant error should not be described as robust physical trends.

Rising groundwater head near a recharge basin may indicate perched water that never reaches the target confined aquifer. A scientifically serious explanation must accommodate rival mechanisms. Identify what the preferred mechanism would predict at another time, depth or location. Choose a second type of evidence—geological context, temperature, chemical tracers, parallel reference catchments or independently surveyed elevations—rather than only refitting the same data. An observation that both models predict equally well is not a discriminating test.

### Worked calculation — Recharge capture volume

**Illustrative data:** Managed infiltration rate 12 mm/day over 5 hectares for 20 days with 60% delivery efficiency. **Equation or arithmetic:** `0.012*50000*20*.6`. **Answer: 7,200 m³**. State why the inputs have compatible units, and explain which water store, flux, property, probability or statistic the output actually represents. For mixed units, write intermediate conversions explicitly. Distinguish the numerical answer from a claim about the real-world process: the answer follows from the invented inputs and the chosen equation, not from measurements of an actual catchment or aquifer.

**Sensitivity and limits:** Clogging, evaporation and chemistry may alter actual delivery efficiency. If an input is changed by 20%, calculate the new output and describe whether the response is linear or nonlinear. Where appropriate, identify an excluded term or an assumption about spatial uniformity, stationarity, constant flow, conservative chemistry, or homogeneous porous media. This calculation cannot establish the excluded term is zero merely because it produces a tidy result.

### Field or data investigation

Compare an assumed recharge inflow with delayed storage response and include operational losses. Put this in the unit investigation setting: A managed aquifer beside a river and a municipal abstraction well. Recharge management; Include actual delivered water, clogging and ecological capture. The monitoring sheet should retain raw values, calibration and a flag for missing or questionable samples. Before interpreting a change, ask whether an independent instrument would observe the same sign and magnitude. A river losing water during low stage might reflect natural gradient reversal or nearby pumping. Simultaneous stream and groundwater levels offer stronger evidence than a single spot gauging. Use a baseline scenario and an alternative scenario with an explicit change in just one assumption, so that the cause of the model's different output remains visible.

### Interpretation and practical constraints

Water rights, ecosystem protections and geochemical compatibility require local evidence beyond the teaching model. Compare short-term groundwater mounding against deep-aquifer response; Check an infiltration basin before recommending scale-up. Break uncertainty into instrumental accuracy, insufficient temporal or spatial sampling, uncertain model coefficients and uncertainty about the governing mechanism itself. These sources can dominate in different circumstances. Report what could make a conclusion false, not merely a plus–minus range attached to a fitted number. An actual abstraction limit, well safety decision, contamination assessment or flood warning requires locally measured and professionally reviewed evidence.

### Problems and answer checks

1. **Calculation and units:** reproduce the example and then change one input by 20%. Retain units at every line and verify that the result is dimensionally meaningful.
2. **Scientific discrimination:** write two competing explanations for the described observations, and give the exact sampling location, instrument and predicted difference that could resolve them.
3. **Transferability:** explain which key assumption is most likely to break in a different soil, geology, season, flow regime or monitoring technology. Design a quick test.
4. **Evidence memo:** distinguish observations, computed quantities and interpretations in a five-sentence note. State a follow-up observation that could reverse the judgment.

**Answer guidance:** a sound answer includes the governing relationship, a physically appropriate measurement boundary, checks on units and uncertainty, and one genuinely differentiating field test. Numerical precision alone does not strengthen an unsupported hydrologic interpretation.

## Integrated laboratory: Interpret a fictional well-test campaign alongside stream seepage.

**Research task.** A managed aquifer beside a river and a municipal abstraction well Start from the attached `datasets/unit-05-synthetic.csv`. The records are deliberately fictional and provide no local environmental observations. The learner's deliverable is a short technical notebook, a table of measurements and conversions, a controlled comparison between two interpretations, and a one-page statement of residual uncertainty.

**Phase A — conceptual diagram.** Drawdown is a transient pressure response. A local well test may estimate a hydraulic property under simplifying boundaries, while a longer record integrates pumping schedules, seasonal recharge, stream capture and distant stresses. Each observation has a spatial footprint; annotate which terms would require a point sample, area-average estimate or volumetric balance. For groundwater, show screened intervals and vertical datum. For rivers, mark the measurement section and route. For water chemistry, identify concentration, flow and analyte units. A diagram that omits the boundary often hides the missing flux that later produces an apparently anomalous numerical result.

**Phase B — independent calculation.** A river losing water during low stage might reflect natural gradient reversal or nearby pumping. Simultaneous stream and groundwater levels offer stronger evidence than a single spot gauging. Use at least two independent calculation approaches where possible. Compare the result against a sanity bound: storage cannot be below a declared physically admissible minimum, chemical mixing fractions should lie between zero and one under the assumed ideal endmembers, and a probability cannot exceed unity. Round only after combining inputs; retain raw values and intermediate results in a reproducible notebook.

**Phase C — evaluate the alternative.** A fitted pumping-curve coefficient has units and a domain of validity. Check assumed well radius, screen geometry, aquifer thickness and constant pumping rate before interpreting a transmissivity estimate. Replace one assumption at a time. Include a small scenario table showing baseline, lower plausible input and upper plausible input, then a separate table for structural alternatives where equations themselves differ. Explain whether the compared outcomes cross a chosen decision threshold. If no real-world decision threshold has been justified, label the result descriptive only rather than declaring a policy winner.

**Phase D — submit a traceable report.** Include the following in one coherent narrative: (a) research question and ethical scope, (b) boundary and major water or solute pathways, (c) original invented records, (d) exact equation and dimensional checks, (e) rival mechanisms and discriminating observations, (f) sensitivity or uncertainty table, and (g) a short conclusion distinguishing the measurement from its interpretation. State why the data cannot justify a real-world site decision.

### Unit synthesis

Every lesson above contributes a different constraint to the integrated investigation. Cross-check a mass balance against a physically plausible flow path; cross-check a statistical summary against a documented measurement interval; and cross-check a model-derived conclusion against an independent observation wherever feasible. Report what evidence would overturn the preferred conclusion. The appropriate scientific endpoint is not a graph that looks convincing, but an interpretation that remains defensible when another researcher can inspect its data, assumptions and alternatives.
