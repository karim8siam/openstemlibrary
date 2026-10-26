# Unit 6 — Water quality, solute movement and contamination

## Scientific problem for this unit

How do hydrologists trace the movement and transformation of dissolved constituents? The case-study setting is: **Calculate plausible solute transport, then challenge its assumptions.**. The central difficulty is that the same observed water level, hydrograph, concentration or land-surface change can arise from multiple physical causes. A course in hydrology becomes useful when students learn to infer processes cautiously rather than replacing a missing measurement with a convenient story. This unit integrates conservation laws, field observables and independent checks in a coherent investigation.

### Background and field context

A groundwater plume passing through heterogeneous sediments into a downstream river. The investigation asks students to define a measurement support, write the governing equation with correct units, and make a prediction before inspecting hypothetical data. Concentration may be high while total exported mass is low because water flux is low. To discuss exposure, specify the receptor; to discuss pollution load, multiply properly converted concentration by discharge. Students should keep a concise field ledger indicating which variables were measured, which were derived, and which were assigned because the problem did not provide enough data.

The unifying tools are dimensional reasoning, boundary diagrams and comparison of rival conceptual models. Concentration, loads, advection, dispersion, mixing, reactions and source attribution all become difficult when scales are mixed, when a sensor's datum is omitted, or when statistical fit is confused with causal evidence. Draw one section or plan view that labels land surface, relevant geological horizons, the stream or well network, and the water-transfer pathways under discussion. Give a sign convention to every flux. For quantities reported as volumes, identify the integration interval and contributing area. Explain why the chosen model domain includes or excludes neighboring exchanges.

### Reading and learning outcomes

Students should be able to calculate a conditional result, describe at least two competing processes, identify limitations of measurement, and write a short reproducible report. Alongside the five lessons, the unit includes a synthetic laboratory dataset and two illustrative slider-driven equations. These models are deliberately simple: use them to see parameter sensitivity, not to recommend operational changes. Any inference about actual water quality, flood hazard or well yield requires site data, qualified review and the relevant authorities.

## Lesson 6.1 — Concentration, flux and mass balance

### How the process works

Solute concentration is mass per water volume; chemical mass flux combines concentration and discharge. Mass balances must include units, changing storage, chemical reactions and unmeasured sources. Begin with a drawing of the physical stores and fluxes relevant to **concentration, flux and mass balance**, showing both the water-bearing materials and the chosen observation boundary. Explain which forces move the water, solute or energy; identify the reference datum if hydraulic head or elevation is involved. A catchment outlet, soil column, well screen and river reach measure different domains. Never describe the value at one instrument as a universal property without a scaling argument. Distinguish a conservation relationship, which must hold for a correctly bounded system, from a constitutive equation, whose coefficients require calibration and whose validity is conditional on site conditions.

### Evidence, ambiguity and falsifiable alternatives

Field blanks, duplicates, filtered and unfiltered samples, discharge records and timestamps constrain reported loads. For every proposed observation, record units, location, date, time step, instrument support and an independent quality check. Sketch what is measured directly and what must be inferred. Estimate an error or detection limit if the result will be compared across sites or dates. Changes that are smaller than the relevant error should not be described as robust physical trends.

A high concentration can accompany low total export during drought; interpreting concentration alone confuses exposure with mass flux. A scientifically serious explanation must accommodate rival mechanisms. Identify what the preferred mechanism would predict at another time, depth or location. Choose a second type of evidence—geological context, temperature, chemical tracers, parallel reference catchments or independently surveyed elevations—rather than only refitting the same data. An observation that both models predict equally well is not a discriminating test.

### Worked calculation — Instantaneous dissolved load

**Illustrative data:** Nitrate-N concentration 8 mg/L at flow 3 m³/s. **Equation or arithmetic:** `8*.001*3`. **Answer: 0.024 kg/s**. State why the inputs have compatible units, and explain which water store, flux, property, probability or statistic the output actually represents. For mixed units, write intermediate conversions explicitly. Distinguish the numerical answer from a claim about the real-world process: the answer follows from the invented inputs and the chosen equation, not from measurements of an actual catchment or aquifer.

**Sensitivity and limits:** A grab sample cannot establish the annual mean nitrogen load. If an input is changed by 20%, calculate the new output and describe whether the response is linear or nonlinear. Where appropriate, identify an excluded term or an assumption about spatial uniformity, stationarity, constant flow, conservative chemistry, or homogeneous porous media. This calculation cannot establish the excluded term is zero merely because it produces a tidy result.

### Field or data investigation

Compute an instantaneous load from concentration and flow and contrast wet- versus dry-season contributions. Put this in the unit investigation setting: A groundwater plume passing through heterogeneous sediments into a downstream river. Chemistry mass flux; Convert mg/L carefully when multiplying by m³/s. The monitoring sheet should retain raw values, calibration and a flag for missing or questionable samples. Before interpreting a change, ask whether an independent instrument would observe the same sign and magnitude. Observed concentration differences may reflect dilution, sorption, chemical reaction, groundwater mixing or laboratory inconsistency. A before-after increase at one well cannot single out a source by itself. Use a baseline scenario and an alternative scenario with an explicit change in just one assumption, so that the cause of the model's different output remains visible.

### Interpretation and practical constraints

Load estimated from one grab sample is not a measured annual load. Separate concentration from mass transport; Integrate sample-weighted loads across high flow and low flow. Break uncertainty into instrumental accuracy, insufficient temporal or spatial sampling, uncertain model coefficients and uncertainty about the governing mechanism itself. These sources can dominate in different circumstances. Report what could make a conclusion false, not merely a plus–minus range attached to a fitted number. An actual abstraction limit, well safety decision, contamination assessment or flood warning requires locally measured and professionally reviewed evidence.

### Problems and answer checks

1. **Calculation and units:** reproduce the example and then change one input by 20%. Retain units at every line and verify that the result is dimensionally meaningful.
2. **Scientific discrimination:** write two competing explanations for the described observations, and give the exact sampling location, instrument and predicted difference that could resolve them.
3. **Transferability:** explain which key assumption is most likely to break in a different soil, geology, season, flow regime or monitoring technology. Design a quick test.
4. **Evidence memo:** distinguish observations, computed quantities and interpretations in a five-sentence note. State a follow-up observation that could reverse the judgment.

**Answer guidance:** a sound answer includes the governing relationship, a physically appropriate measurement boundary, checks on units and uncertainty, and one genuinely differentiating field test. Numerical precision alone does not strengthen an unsupported hydrologic interpretation.

## Lesson 6.2 — Advection, dispersion and retardation

### How the process works

Groundwater transports solutes by bulk pore-water motion and hydrodynamic dispersion; sorption and transformation can delay or remove a species relative to conservative tracer behavior. Begin with a drawing of the physical stores and fluxes relevant to **advection, dispersion and retardation**, showing both the water-bearing materials and the chosen observation boundary. Explain which forces move the water, solute or energy; identify the reference datum if hydraulic head or elevation is involved. A catchment outlet, soil column, well screen and river reach measure different domains. Never describe the value at one instrument as a universal property without a scaling argument. Distinguish a conservation relationship, which must hold for a correctly bounded system, from a constitutive equation, whose coefficients require calibration and whose validity is conditional on site conditions.

### Evidence, ambiguity and falsifiable alternatives

Tracer breakthroughs, hydraulic gradients, sediment sorption tests and geochemical samples constrain mechanisms. For every proposed observation, record units, location, date, time step, instrument support and an independent quality check. Sketch what is measured directly and what must be inferred. Estimate an error or detection limit if the result will be compared across sites or dates. Changes that are smaller than the relevant error should not be described as robust physical trends.

Early tracer detection can arise from preferential fractures rather than unusually high representative matrix velocity. A scientifically serious explanation must accommodate rival mechanisms. Identify what the preferred mechanism would predict at another time, depth or location. Choose a second type of evidence—geological context, temperature, chemical tracers, parallel reference catchments or independently surveyed elevations—rather than only refitting the same data. An observation that both models predict equally well is not a discriminating test.

### Worked calculation — Advective travel time

**Illustrative data:** Distance 120 m and Darcy flux 0.012 m/day with effective porosity 0.25. **Equation or arithmetic:** `120/(.012/.25)`. **Answer: 2,500 days**. State why the inputs have compatible units, and explain which water store, flux, property, probability or statistic the output actually represents. For mixed units, write intermediate conversions explicitly. Distinguish the numerical answer from a claim about the real-world process: the answer follows from the invented inputs and the chosen equation, not from measurements of an actual catchment or aquifer.

**Sensitivity and limits:** Dispersion and preferential flow produce departures from one arrival time. If an input is changed by 20%, calculate the new output and describe whether the response is linear or nonlinear. Where appropriate, identify an excluded term or an assumption about spatial uniformity, stationarity, constant flow, conservative chemistry, or homogeneous porous media. This calculation cannot establish the excluded term is zero merely because it produces a tidy result.

### Field or data investigation

Compute ideal travel time from distance and pore velocity, then explore a hypothetical retardation factor. Put this in the unit investigation setting: A groundwater plume passing through heterogeneous sediments into a downstream river. Conservative tracer; Distinguish mean travel time from breakthrough tail. The monitoring sheet should retain raw values, calibration and a flag for missing or questionable samples. Before interpreting a change, ask whether an independent instrument would observe the same sign and magnitude. Observed concentration differences may reflect dilution, sorption, chemical reaction, groundwater mixing or laboratory inconsistency. A before-after increase at one well cannot single out a source by itself. Use a baseline scenario and an alternative scenario with an explicit change in just one assumption, so that the cause of the model's different output remains visible.

### Interpretation and practical constraints

Transport pathways and tails are highly sensitive to heterogeneity; the classroom calculation is not a safety-zone determination. Discuss sorption, dispersion and preferred pathways; Check sensitivity to effective porosity and velocity. Break uncertainty into instrumental accuracy, insufficient temporal or spatial sampling, uncertain model coefficients and uncertainty about the governing mechanism itself. These sources can dominate in different circumstances. Report what could make a conclusion false, not merely a plus–minus range attached to a fitted number. An actual abstraction limit, well safety decision, contamination assessment or flood warning requires locally measured and professionally reviewed evidence.

### Problems and answer checks

1. **Calculation and units:** reproduce the example and then change one input by 20%. Retain units at every line and verify that the result is dimensionally meaningful.
2. **Scientific discrimination:** write two competing explanations for the described observations, and give the exact sampling location, instrument and predicted difference that could resolve them.
3. **Transferability:** explain which key assumption is most likely to break in a different soil, geology, season, flow regime or monitoring technology. Design a quick test.
4. **Evidence memo:** distinguish observations, computed quantities and interpretations in a five-sentence note. State a follow-up observation that could reverse the judgment.

**Answer guidance:** a sound answer includes the governing relationship, a physically appropriate measurement boundary, checks on units and uncertainty, and one genuinely differentiating field test. Numerical precision alone does not strengthen an unsupported hydrologic interpretation.

## Lesson 6.3 — Major-ion chemistry and mixing

### How the process works

Weathering, evaporation, seawater mixing, mineral precipitation and exchange can modify dissolved-ion patterns during flow. Charge balance provides a quality screen, not proof of unique reaction history. Begin with a drawing of the physical stores and fluxes relevant to **major-ion chemistry and mixing**, showing both the water-bearing materials and the chosen observation boundary. Explain which forces move the water, solute or energy; identify the reference datum if hydraulic head or elevation is involved. A catchment outlet, soil column, well screen and river reach measure different domains. Never describe the value at one instrument as a universal property without a scaling argument. Distinguish a conservation relationship, which must hold for a correctly bounded system, from a constitutive equation, whose coefficients require calibration and whose validity is conditional on site conditions.

### Evidence, ambiguity and falsifiable alternatives

Conductivity, pH, temperature, measured major ions, alkalinity and well construction records support geochemical interpretation. For every proposed observation, record units, location, date, time step, instrument support and an independent quality check. Sketch what is measured directly and what must be inferred. Estimate an error or detection limit if the result will be compared across sites or dates. Changes that are smaller than the relevant error should not be described as robust physical trends.

Similar total dissolved solids may arise from distinct sources, and laboratory handling can change oxidation state. A scientifically serious explanation must accommodate rival mechanisms. Identify what the preferred mechanism would predict at another time, depth or location. Choose a second type of evidence—geological context, temperature, chemical tracers, parallel reference catchments or independently surveyed elevations—rather than only refitting the same data. An observation that both models predict equally well is not a discriminating test.

### Worked calculation — Conservative two-endmember mixing

**Illustrative data:** Sample chloride 65 mg/L, fresh endmember 15, salty endmember 215 mg/L. **Equation or arithmetic:** `(65-15)/(215-15)`. **Answer: 0.25 salty-water fraction**. State why the inputs have compatible units, and explain which water store, flux, property, probability or statistic the output actually represents. For mixed units, write intermediate conversions explicitly. Distinguish the numerical answer from a claim about the real-world process: the answer follows from the invented inputs and the chosen equation, not from measurements of an actual catchment or aquifer.

**Sensitivity and limits:** Changing or reacting chloride endmembers can make this inference invalid. If an input is changed by 20%, calculate the new output and describe whether the response is linear or nonlinear. Where appropriate, identify an excluded term or an assumption about spatial uniformity, stationarity, constant flow, conservative chemistry, or homogeneous porous media. This calculation cannot establish the excluded term is zero merely because it produces a tidy result.

### Field or data investigation

Calculate an illustrative mixture fraction from a conservative tracer and evaluate whether end-member stability is plausible. Put this in the unit investigation setting: A groundwater plume passing through heterogeneous sediments into a downstream river. Geochemical mixing; Use endmember values only when conservative and stable. The monitoring sheet should retain raw values, calibration and a flag for missing or questionable samples. Before interpreting a change, ask whether an independent instrument would observe the same sign and magnitude. Observed concentration differences may reflect dilution, sorption, chemical reaction, groundwater mixing or laboratory inconsistency. A before-after increase at one well cannot single out a source by itself. Use a baseline scenario and an alternative scenario with an explicit change in just one assumption, so that the cause of the model's different output remains visible.

### Interpretation and practical constraints

Ion composition requires laboratory quality control and speciation assessment, not only simple proportional mixing. Evaluate whether reactions could alter the chosen tracer; Calculate mixture bounds from uncertain endmember composition. Break uncertainty into instrumental accuracy, insufficient temporal or spatial sampling, uncertain model coefficients and uncertainty about the governing mechanism itself. These sources can dominate in different circumstances. Report what could make a conclusion false, not merely a plus–minus range attached to a fitted number. An actual abstraction limit, well safety decision, contamination assessment or flood warning requires locally measured and professionally reviewed evidence.

### Problems and answer checks

1. **Calculation and units:** reproduce the example and then change one input by 20%. Retain units at every line and verify that the result is dimensionally meaningful.
2. **Scientific discrimination:** write two competing explanations for the described observations, and give the exact sampling location, instrument and predicted difference that could resolve them.
3. **Transferability:** explain which key assumption is most likely to break in a different soil, geology, season, flow regime or monitoring technology. Design a quick test.
4. **Evidence memo:** distinguish observations, computed quantities and interpretations in a five-sentence note. State a follow-up observation that could reverse the judgment.

**Answer guidance:** a sound answer includes the governing relationship, a physically appropriate measurement boundary, checks on units and uncertainty, and one genuinely differentiating field test. Numerical precision alone does not strengthen an unsupported hydrologic interpretation.

## Lesson 6.4 — Nutrients, pathogens and exposure routes

### How the process works

Nitrogen and phosphorus move among dissolved, particulate and biological pools; pathogens have different transport and persistence controls. Recharge and preferential flow influence drinking-water vulnerability. Begin with a drawing of the physical stores and fluxes relevant to **nutrients, pathogens and exposure routes**, showing both the water-bearing materials and the chosen observation boundary. Explain which forces move the water, solute or energy; identify the reference datum if hydraulic head or elevation is involved. A catchment outlet, soil column, well screen and river reach measure different domains. Never describe the value at one instrument as a universal property without a scaling argument. Distinguish a conservation relationship, which must hold for a correctly bounded system, from a constitutive equation, whose coefficients require calibration and whose validity is conditional on site conditions.

### Evidence, ambiguity and falsifiable alternatives

Repeated upstream/downstream chemistry, land-use history, sanitation observations and appropriately designed laboratory analysis provide evidence. For every proposed observation, record units, location, date, time step, instrument support and an independent quality check. Sketch what is measured directly and what must be inferred. Estimate an error or detection limit if the result will be compared across sites or dates. Changes that are smaller than the relevant error should not be described as robust physical trends.

An apparent agricultural source can instead be failing sanitation infrastructure or a point discharge. A scientifically serious explanation must accommodate rival mechanisms. Identify what the preferred mechanism would predict at another time, depth or location. Choose a second type of evidence—geological context, temperature, chemical tracers, parallel reference catchments or independently surveyed elevations—rather than only refitting the same data. An observation that both models predict equally well is not a discriminating test.

### Worked calculation — Monthly nitrogen load

**Illustrative data:** Concentration=5 mg/L; steady flow=2 m³/s over a 30-day illustrative month. **Equation or arithmetic:** `5*.001*2*30*86400`. **Answer: 25,920 kg/month**. State why the inputs have compatible units, and explain which water store, flux, property, probability or statistic the output actually represents. For mixed units, write intermediate conversions explicitly. Distinguish the numerical answer from a claim about the real-world process: the answer follows from the invented inputs and the chosen equation, not from measurements of an actual catchment or aquifer.

**Sensitivity and limits:** Real concentration and flow covary; integration requires paired measurements. If an input is changed by 20%, calculate the new output and describe whether the response is linear or nonlinear. Where appropriate, identify an excluded term or an assumption about spatial uniformity, stationarity, constant flow, conservative chemistry, or homogeneous porous media. This calculation cannot establish the excluded term is zero merely because it produces a tidy result.

### Field or data investigation

Create an evidence matrix for competing nutrient sources and calculate a hypothetical monthly nitrate-N load without assuming causation. Put this in the unit investigation setting: A groundwater plume passing through heterogeneous sediments into a downstream river. Contaminant attribution; Separate upstream source possibilities with evidence. The monitoring sheet should retain raw values, calibration and a flag for missing or questionable samples. Before interpreting a change, ask whether an independent instrument would observe the same sign and magnitude. Observed concentration differences may reflect dilution, sorption, chemical reaction, groundwater mixing or laboratory inconsistency. A before-after increase at one well cannot single out a source by itself. Use a baseline scenario and an alternative scenario with an explicit change in just one assumption, so that the cause of the model's different output remains visible.

### Interpretation and practical constraints

Educational water-quality examples cannot determine potability; official standards and certified testing govern actual use. Recognize concentration is not a certified health evaluation; Trace nitrate-N load without claiming its causal origin. Break uncertainty into instrumental accuracy, insufficient temporal or spatial sampling, uncertain model coefficients and uncertainty about the governing mechanism itself. These sources can dominate in different circumstances. Report what could make a conclusion false, not merely a plus–minus range attached to a fitted number. An actual abstraction limit, well safety decision, contamination assessment or flood warning requires locally measured and professionally reviewed evidence.

### Problems and answer checks

1. **Calculation and units:** reproduce the example and then change one input by 20%. Retain units at every line and verify that the result is dimensionally meaningful.
2. **Scientific discrimination:** write two competing explanations for the described observations, and give the exact sampling location, instrument and predicted difference that could resolve them.
3. **Transferability:** explain which key assumption is most likely to break in a different soil, geology, season, flow regime or monitoring technology. Design a quick test.
4. **Evidence memo:** distinguish observations, computed quantities and interpretations in a five-sentence note. State a follow-up observation that could reverse the judgment.

**Answer guidance:** a sound answer includes the governing relationship, a physically appropriate measurement boundary, checks on units and uncertainty, and one genuinely differentiating field test. Numerical precision alone does not strengthen an unsupported hydrologic interpretation.

## Lesson 6.5 — Monitoring wells, statistics and QA/QC

### How the process works

Water-quality programs require spatially and temporally representative sampling, chain of custody, detection limits and careful treatment of censored data. More samples cannot repair systematic bias. Begin with a drawing of the physical stores and fluxes relevant to **monitoring wells, statistics and qa/qc**, showing both the water-bearing materials and the chosen observation boundary. Explain which forces move the water, solute or energy; identify the reference datum if hydraulic head or elevation is involved. A catchment outlet, soil column, well screen and river reach measure different domains. Never describe the value at one instrument as a universal property without a scaling argument. Distinguish a conservation relationship, which must hold for a correctly bounded system, from a constitutive equation, whose coefficients require calibration and whose validity is conditional on site conditions.

### Evidence, ambiguity and falsifiable alternatives

Blanks, laboratory duplicates, standards, field replicates and sampling protocols document comparability. For every proposed observation, record units, location, date, time step, instrument support and an independent quality check. Sketch what is measured directly and what must be inferred. Estimate an error or detection limit if the result will be compared across sites or dates. Changes that are smaller than the relevant error should not be described as robust physical trends.

A trend in measured concentrations can result from a laboratory-method change or well screening-depth change. A scientifically serious explanation must accommodate rival mechanisms. Identify what the preferred mechanism would predict at another time, depth or location. Choose a second type of evidence—geological context, temperature, chemical tracers, parallel reference catchments or independently surveyed elevations—rather than only refitting the same data. An observation that both models predict equally well is not a discriminating test.

### Worked calculation — Replicate coefficient of variation

**Illustrative data:** Duplicate nitrate measures 7.0 and 7.6 mg/L; sample SD uses n-1. **Equation or arithmetic:** `100*(.6/math.sqrt(2))/7.3`. **Answer: 5.8118 %**. State why the inputs have compatible units, and explain which water store, flux, property, probability or statistic the output actually represents. For mixed units, write intermediate conversions explicitly. Distinguish the numerical answer from a claim about the real-world process: the answer follows from the invented inputs and the chosen equation, not from measurements of an actual catchment or aquifer.

**Sensitivity and limits:** Two observations cannot characterize long-term analytical precision. If an input is changed by 20%, calculate the new output and describe whether the response is linear or nonlinear. Where appropriate, identify an excluded term or an assumption about spatial uniformity, stationarity, constant flow, conservative chemistry, or homogeneous porous media. This calculation cannot establish the excluded term is zero merely because it produces a tidy result.

### Field or data investigation

Test a trend after introducing an imaginary reporting-limit change; specify a quality-control rule before interpreting the result. Put this in the unit investigation setting: A groundwater plume passing through heterogeneous sediments into a downstream river. Analytical quality control; Separate laboratory and field measurement uncertainty. The monitoring sheet should retain raw values, calibration and a flag for missing or questionable samples. Before interpreting a change, ask whether an independent instrument would observe the same sign and magnitude. Observed concentration differences may reflect dilution, sorption, chemical reaction, groundwater mixing or laboratory inconsistency. A before-after increase at one well cannot single out a source by itself. Use a baseline scenario and an alternative scenario with an explicit change in just one assumption, so that the cause of the model's different output remains visible.

### Interpretation and practical constraints

Means calculated after replacing all non-detects with zero can be seriously biased. Handle detection limits transparently; Test a trend with a hypothetical method change date. Break uncertainty into instrumental accuracy, insufficient temporal or spatial sampling, uncertain model coefficients and uncertainty about the governing mechanism itself. These sources can dominate in different circumstances. Report what could make a conclusion false, not merely a plus–minus range attached to a fitted number. An actual abstraction limit, well safety decision, contamination assessment or flood warning requires locally measured and professionally reviewed evidence.

### Problems and answer checks

1. **Calculation and units:** reproduce the example and then change one input by 20%. Retain units at every line and verify that the result is dimensionally meaningful.
2. **Scientific discrimination:** write two competing explanations for the described observations, and give the exact sampling location, instrument and predicted difference that could resolve them.
3. **Transferability:** explain which key assumption is most likely to break in a different soil, geology, season, flow regime or monitoring technology. Design a quick test.
4. **Evidence memo:** distinguish observations, computed quantities and interpretations in a five-sentence note. State a follow-up observation that could reverse the judgment.

**Answer guidance:** a sound answer includes the governing relationship, a physically appropriate measurement boundary, checks on units and uncertainty, and one genuinely differentiating field test. Numerical precision alone does not strengthen an unsupported hydrologic interpretation.

## Integrated laboratory: Calculate plausible solute transport, then challenge its assumptions.

**Research task.** A groundwater plume passing through heterogeneous sediments into a downstream river Start from the attached `datasets/unit-06-synthetic.csv`. The records are deliberately fictional and provide no local environmental observations. The learner's deliverable is a short technical notebook, a table of measurements and conversions, a controlled comparison between two interpretations, and a one-page statement of residual uncertainty.

**Phase A — conceptual diagram.** Concentration may be high while total exported mass is low because water flux is low. To discuss exposure, specify the receptor; to discuss pollution load, multiply properly converted concentration by discharge. Each observation has a spatial footprint; annotate which terms would require a point sample, area-average estimate or volumetric balance. For groundwater, show screened intervals and vertical datum. For rivers, mark the measurement section and route. For water chemistry, identify concentration, flow and analyte units. A diagram that omits the boundary often hides the missing flux that later produces an apparently anomalous numerical result.

**Phase B — independent calculation.** Observed concentration differences may reflect dilution, sorption, chemical reaction, groundwater mixing or laboratory inconsistency. A before-after increase at one well cannot single out a source by itself. Use at least two independent calculation approaches where possible. Compare the result against a sanity bound: storage cannot be below a declared physically admissible minimum, chemical mixing fractions should lie between zero and one under the assumed ideal endmembers, and a probability cannot exceed unity. Round only after combining inputs; retain raw values and intermediate results in a reproducible notebook.

**Phase C — evaluate the alternative.** Transport time based on mean pore velocity misses early breakthrough and late tailing. Conservative tracers can map connected pathways but reactive species require additional geochemistry. Replace one assumption at a time. Include a small scenario table showing baseline, lower plausible input and upper plausible input, then a separate table for structural alternatives where equations themselves differ. Explain whether the compared outcomes cross a chosen decision threshold. If no real-world decision threshold has been justified, label the result descriptive only rather than declaring a policy winner.

**Phase D — submit a traceable report.** Include the following in one coherent narrative: (a) research question and ethical scope, (b) boundary and major water or solute pathways, (c) original invented records, (d) exact equation and dimensional checks, (e) rival mechanisms and discriminating observations, (f) sensitivity or uncertainty table, and (g) a short conclusion distinguishing the measurement from its interpretation. State why the data cannot justify a real-world site decision.

### Unit synthesis

Every lesson above contributes a different constraint to the integrated investigation. Cross-check a mass balance against a physically plausible flow path; cross-check a statistical summary against a documented measurement interval; and cross-check a model-derived conclusion against an independent observation wherever feasible. Report what evidence would overturn the preferred conclusion. The appropriate scientific endpoint is not a graph that looks convincing, but an interpretation that remains defensible when another researcher can inspect its data, assumptions and alternatives.
