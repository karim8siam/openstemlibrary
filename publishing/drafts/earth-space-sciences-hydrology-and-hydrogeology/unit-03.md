# Unit 3 — Rivers, hydrographs and floods

## Scientific problem for this unit

How can flow measurements explain catchment response without confusing event probabilities with predictions? The case-study setting is: **Use paired hydrographs to test a change in runoff connectivity.**. The central difficulty is that the same observed water level, hydrograph, concentration or land-surface change can arise from multiple physical causes. A course in hydrology becomes useful when students learn to infer processes cautiously rather than replacing a missing measurement with a convenient story. This unit integrates conservation laws, field observables and independent checks in a coherent investigation.

### Background and field context

A river basin with two gauges and an ungauged tributary. The investigation asks students to define a measurement support, write the governing equation with correct units, and make a prediction before inspecting hypothetical data. Streamflow is a rate, not a static store. Integrating the area under a hydrograph yields event volume only after choosing the baseline, recording time intervals and converting seconds correctly. Changing the baseline can change estimates of direct runoff substantially. Students should keep a concise field ledger indicating which variables were measured, which were derived, and which were assigned because the problem did not provide enough data.

The unifying tools are dimensional reasoning, boundary diagrams and comparison of rival conceptual models. Stage-discharge conversion, response time, baseflow, flood frequency, hydrograph separation all become difficult when scales are mixed, when a sensor's datum is omitted, or when statistical fit is confused with causal evidence. Draw one section or plan view that labels land surface, relevant geological horizons, the stream or well network, and the water-transfer pathways under discussion. Give a sign convention to every flux. For quantities reported as volumes, identify the integration interval and contributing area. Explain why the chosen model domain includes or excludes neighboring exchanges.

### Reading and learning outcomes

Students should be able to calculate a conditional result, describe at least two competing processes, identify limitations of measurement, and write a short reproducible report. Alongside the five lessons, the unit includes a synthetic laboratory dataset and two illustrative slider-driven equations. These models are deliberately simple: use them to see parameter sensitivity, not to recommend operational changes. Any inference about actual water quality, flood hazard or well yield requires site data, qualified review and the relevant authorities.

## Lesson 3.1 — Channel discharge and velocity measurement

### How the process works

Discharge integrates velocity across the wet cross-section; using width times central velocity ignores vertical and lateral heterogeneity. Turbulence and stage influence instrument reliability. Begin with a drawing of the physical stores and fluxes relevant to **channel discharge and velocity measurement**, showing both the water-bearing materials and the chosen observation boundary. Explain which forces move the water, solute or energy; identify the reference datum if hydraulic head or elevation is involved. A catchment outlet, soil column, well screen and river reach measure different domains. Never describe the value at one instrument as a universal property without a scaling argument. Distinguish a conservation relationship, which must hold for a correctly bounded system, from a constitutive equation, whose coefficients require calibration and whose validity is conditional on site conditions.

### Evidence, ambiguity and falsifiable alternatives

Velocity-area transects, acoustic Doppler measurements, current meters and repeated section surveys provide direct discharge evidence. For every proposed observation, record units, location, date, time step, instrument support and an independent quality check. Sketch what is measured directly and what must be inferred. Estimate an error or detection limit if the result will be compared across sites or dates. Changes that are smaller than the relevant error should not be described as robust physical trends.

A gauge reading that rises without a true discharge rise can occur with backwater, debris jams or tidal influence. A scientifically serious explanation must accommodate rival mechanisms. Identify what the preferred mechanism would predict at another time, depth or location. Choose a second type of evidence—geological context, temperature, chemical tracers, parallel reference catchments or independently surveyed elevations—rather than only refitting the same data. An observation that both models predict equally well is not a discriminating test.

### Worked calculation — Channel discharge by subsections

**Illustrative data:** Three subsection areas 4, 6 and 5 m² with mean velocities 0.5, 0.9 and 0.7 m/s. **Equation or arithmetic:** `4*.5+6*.9+5*.7`. **Answer: 10.9 m³/s**. State why the inputs have compatible units, and explain which water store, flux, property, probability or statistic the output actually represents. For mixed units, write intermediate conversions explicitly. Distinguish the numerical answer from a claim about the real-world process: the answer follows from the invented inputs and the chosen equation, not from measurements of an actual catchment or aquifer.

**Sensitivity and limits:** Unmeasured near-bank low velocities can bias a coarse three-cell partition. If an input is changed by 20%, calculate the new output and describe whether the response is linear or nonlinear. Where appropriate, identify an excluded term or an assumption about spatial uniformity, stationarity, constant flow, conservative chemistry, or homogeneous porous media. This calculation cannot establish the excluded term is zero merely because it produces a tidy result.

### Field or data investigation

Compare a single-rectangle estimate to a subsection velocity-area sum and quantify their difference. Put this in the unit investigation setting: A river basin with two gauges and an ungauged tributary. Field gauging; Subdivide flow cross sections rather than extrapolate midstream speed. The monitoring sheet should retain raw values, calibration and a flag for missing or questionable samples. Before interpreting a change, ask whether an independent instrument would observe the same sign and magnitude. Routing can delay and flatten a peak; downstream local rain may amplify a peak even where routing would otherwise attenuate it. Measure storm location and tributary arrival before interpreting the sign of peak-time differences. Use a baseline scenario and an alternative scenario with an explicit change in just one assumption, so that the cause of the model's different output remains visible.

### Interpretation and practical constraints

A convenient approximation cannot be presented as a certified measurement for infrastructure decisions. Check backwater or tidal interference with stage-discharge relations; Vary velocity weighting in each measured subsection. Break uncertainty into instrumental accuracy, insufficient temporal or spatial sampling, uncertain model coefficients and uncertainty about the governing mechanism itself. These sources can dominate in different circumstances. Report what could make a conclusion false, not merely a plus–minus range attached to a fitted number. An actual abstraction limit, well safety decision, contamination assessment or flood warning requires locally measured and professionally reviewed evidence.

### Problems and answer checks

1. **Calculation and units:** reproduce the example and then change one input by 20%. Retain units at every line and verify that the result is dimensionally meaningful.
2. **Scientific discrimination:** write two competing explanations for the described observations, and give the exact sampling location, instrument and predicted difference that could resolve them.
3. **Transferability:** explain which key assumption is most likely to break in a different soil, geology, season, flow regime or monitoring technology. Design a quick test.
4. **Evidence memo:** distinguish observations, computed quantities and interpretations in a five-sentence note. State a follow-up observation that could reverse the judgment.

**Answer guidance:** a sound answer includes the governing relationship, a physically appropriate measurement boundary, checks on units and uncertainty, and one genuinely differentiating field test. Numerical precision alone does not strengthen an unsupported hydrologic interpretation.

## Lesson 3.2 — Hydrograph timing and routing

### How the process works

Hydrographs describe flow variation at a point; catchment storage, river routing and network connections change the timing and shape of response. Travel time is not uniquely revealed by peak separation. Begin with a drawing of the physical stores and fluxes relevant to **hydrograph timing and routing**, showing both the water-bearing materials and the chosen observation boundary. Explain which forces move the water, solute or energy; identify the reference datum if hydraulic head or elevation is involved. A catchment outlet, soil column, well screen and river reach measure different domains. Never describe the value at one instrument as a universal property without a scaling argument. Distinguish a conservation relationship, which must hold for a correctly bounded system, from a constitutive equation, whose coefficients require calibration and whose validity is conditional on site conditions.

### Evidence, ambiguity and falsifiable alternatives

Synced gauges, rainfall fields, tracers and river geometry help separate translation from attenuation and lateral contributions. For every proposed observation, record units, location, date, time step, instrument support and an independent quality check. Sketch what is measured directly and what must be inferred. Estimate an error or detection limit if the result will be compared across sites or dates. Changes that are smaller than the relevant error should not be described as robust physical trends.

A downstream peak may precede an upstream peak when downstream tributary rainfall arrives first. A scientifically serious explanation must accommodate rival mechanisms. Identify what the preferred mechanism would predict at another time, depth or location. Choose a second type of evidence—geological context, temperature, chemical tracers, parallel reference catchments or independently surveyed elevations—rather than only refitting the same data. An observation that both models predict equally well is not a discriminating test.

### Worked calculation — Hydrograph event runoff volume

**Illustrative data:** Ideal triangular event excess hydrograph: base 12 hours and maximum 10 m³/s. **Equation or arithmetic:** `0.5*(12*3600)*10`. **Answer: 2.16e+05 m³**. State why the inputs have compatible units, and explain which water store, flux, property, probability or statistic the output actually represents. For mixed units, write intermediate conversions explicitly. Distinguish the numerical answer from a claim about the real-world process: the answer follows from the invented inputs and the chosen equation, not from measurements of an actual catchment or aquifer.

**Sensitivity and limits:** A real routed hydrograph is unlikely to form a perfect symmetric triangle. If an input is changed by 20%, calculate the new output and describe whether the response is linear or nonlinear. Where appropriate, identify an excluded term or an assumption about spatial uniformity, stationarity, constant flow, conservative chemistry, or homogeneous porous media. This calculation cannot establish the excluded term is zero merely because it produces a tidy result.

### Field or data investigation

Estimate the time lag and outline two rainfall configurations that yield the same observed lag. Put this in the unit investigation setting: A river basin with two gauges and an ungauged tributary. Hydrograph interpretation; Separate translation and storage attenuation. The monitoring sheet should retain raw values, calibration and a flag for missing or questionable samples. Before interpreting a change, ask whether an independent instrument would observe the same sign and magnitude. Routing can delay and flatten a peak; downstream local rain may amplify a peak even where routing would otherwise attenuate it. Measure storm location and tributary arrival before interpreting the sign of peak-time differences. Use a baseline scenario and an alternative scenario with an explicit change in just one assumption, so that the cause of the model's different output remains visible.

### Interpretation and practical constraints

Hydrograph lag is not the velocity of an individual water parcel. Avoid interpreting peak lag as parcel velocity; Test an ungauged tributary explanation against rainfall radar. Break uncertainty into instrumental accuracy, insufficient temporal or spatial sampling, uncertain model coefficients and uncertainty about the governing mechanism itself. These sources can dominate in different circumstances. Report what could make a conclusion false, not merely a plus–minus range attached to a fitted number. An actual abstraction limit, well safety decision, contamination assessment or flood warning requires locally measured and professionally reviewed evidence.

### Problems and answer checks

1. **Calculation and units:** reproduce the example and then change one input by 20%. Retain units at every line and verify that the result is dimensionally meaningful.
2. **Scientific discrimination:** write two competing explanations for the described observations, and give the exact sampling location, instrument and predicted difference that could resolve them.
3. **Transferability:** explain which key assumption is most likely to break in a different soil, geology, season, flow regime or monitoring technology. Design a quick test.
4. **Evidence memo:** distinguish observations, computed quantities and interpretations in a five-sentence note. State a follow-up observation that could reverse the judgment.

**Answer guidance:** a sound answer includes the governing relationship, a physically appropriate measurement boundary, checks on units and uncertainty, and one genuinely differentiating field test. Numerical precision alone does not strengthen an unsupported hydrologic interpretation.

## Lesson 3.3 — Baseflow and recession

### How the process works

During rain-free periods streams may be sustained by groundwater, bank storage, wetlands, snowmelt or releases. A recession curve can summarize drainage but need not represent one reservoir. Begin with a drawing of the physical stores and fluxes relevant to **baseflow and recession**, showing both the water-bearing materials and the chosen observation boundary. Explain which forces move the water, solute or energy; identify the reference datum if hydraulic head or elevation is involved. A catchment outlet, soil column, well screen and river reach measure different domains. Never describe the value at one instrument as a universal property without a scaling argument. Distinguish a conservation relationship, which must hold for a correctly bounded system, from a constitutive equation, whose coefficients require calibration and whose validity is conditional on site conditions.

### Evidence, ambiguity and falsifiable alternatives

Long flow records, groundwater hydrographs, temperature, electrical conductivity and isotopes constrain source components. For every proposed observation, record units, location, date, time step, instrument support and an independent quality check. Sketch what is measured directly and what must be inferred. Estimate an error or detection limit if the result will be compared across sites or dates. Changes that are smaller than the relevant error should not be described as robust physical trends.

Dam operation may create an exponential-looking recession entirely unrelated to aquifer drainage. A scientifically serious explanation must accommodate rival mechanisms. Identify what the preferred mechanism would predict at another time, depth or location. Choose a second type of evidence—geological context, temperature, chemical tracers, parallel reference catchments or independently surveyed elevations—rather than only refitting the same data. An observation that both models predict equally well is not a discriminating test.

### Worked calculation — Recession constant

**Illustrative data:** Flow falls from 8 to 4 m³/s in four rainless days under Q(t)=Q0 exp(-kt). **Equation or arithmetic:** `math.log(8/4)/4`. **Answer: 0.17329 per day**. State why the inputs have compatible units, and explain which water store, flux, property, probability or statistic the output actually represents. For mixed units, write intermediate conversions explicitly. Distinguish the numerical answer from a claim about the real-world process: the answer follows from the invented inputs and the chosen equation, not from measurements of an actual catchment or aquifer.

**Sensitivity and limits:** Stream regulations and evapotranspiration change apparent recession rates. If an input is changed by 20%, calculate the new output and describe whether the response is linear or nonlinear. Where appropriate, identify an excluded term or an assumption about spatial uniformity, stationarity, constant flow, conservative chemistry, or homogeneous porous media. This calculation cannot establish the excluded term is zero merely because it produces a tidy result.

### Field or data investigation

Fit a first-order recession coefficient to idealized daily discharge and compare it to a two-reservoir response. Put this in the unit investigation setting: A river basin with two gauges and an ungauged tributary. Recession interpretation; Test whether one exponential store is sufficient. The monitoring sheet should retain raw values, calibration and a flag for missing or questionable samples. Before interpreting a change, ask whether an independent instrument would observe the same sign and magnitude. Routing can delay and flatten a peak; downstream local rain may amplify a peak even where routing would otherwise attenuate it. Measure storm location and tributary arrival before interpreting the sign of peak-time differences. Use a baseline scenario and an alternative scenario with an explicit change in just one assumption, so that the cause of the model's different output remains visible.

### Interpretation and practical constraints

Baseflow separation filters are analytical conventions; their components are not automatically measured groundwater fractions. Recognize reservoir releases and evapotranspiration as confounders; Fit curves independently across three rain-free intervals. Break uncertainty into instrumental accuracy, insufficient temporal or spatial sampling, uncertain model coefficients and uncertainty about the governing mechanism itself. These sources can dominate in different circumstances. Report what could make a conclusion false, not merely a plus–minus range attached to a fitted number. An actual abstraction limit, well safety decision, contamination assessment or flood warning requires locally measured and professionally reviewed evidence.

### Problems and answer checks

1. **Calculation and units:** reproduce the example and then change one input by 20%. Retain units at every line and verify that the result is dimensionally meaningful.
2. **Scientific discrimination:** write two competing explanations for the described observations, and give the exact sampling location, instrument and predicted difference that could resolve them.
3. **Transferability:** explain which key assumption is most likely to break in a different soil, geology, season, flow regime or monitoring technology. Design a quick test.
4. **Evidence memo:** distinguish observations, computed quantities and interpretations in a five-sentence note. State a follow-up observation that could reverse the judgment.

**Answer guidance:** a sound answer includes the governing relationship, a physically appropriate measurement boundary, checks on units and uncertainty, and one genuinely differentiating field test. Numerical precision alone does not strengthen an unsupported hydrologic interpretation.

## Lesson 3.4 — Flood frequency and nonstationarity

### How the process works

Annual maxima support estimated exceedance probabilities only under assumptions about data quality, representativeness and probability structure. Land use and climate variability may change those conditions. Begin with a drawing of the physical stores and fluxes relevant to **flood frequency and nonstationarity**, showing both the water-bearing materials and the chosen observation boundary. Explain which forces move the water, solute or energy; identify the reference datum if hydraulic head or elevation is involved. A catchment outlet, soil column, well screen and river reach measure different domains. Never describe the value at one instrument as a universal property without a scaling argument. Distinguish a conservation relationship, which must hold for a correctly bounded system, from a constitutive equation, whose coefficients require calibration and whose validity is conditional on site conditions.

### Evidence, ambiguity and falsifiable alternatives

Gauge history, rating-curve metadata, flood marks and paleoflood evidence inform uncertain tails of flood distributions. For every proposed observation, record units, location, date, time step, instrument support and an independent quality check. Sketch what is measured directly and what must be inferred. Estimate an error or detection limit if the result will be compared across sites or dates. Changes that are smaller than the relevant error should not be described as robust physical trends.

A record-breaking flood does not prove a precise new recurrence interval, and a 1% annual chance is not a once-per-century calendar. A scientifically serious explanation must accommodate rival mechanisms. Identify what the preferred mechanism would predict at another time, depth or location. Choose a second type of evidence—geological context, temperature, chemical tracers, parallel reference catchments or independently surveyed elevations—rather than only refitting the same data. An observation that both models predict equally well is not a discriminating test.

### Worked calculation — Exceedance within multiple years

**Illustrative data:** Assume independent stationary annual exceedance probability p=0.01 over 30 years. **Equation or arithmetic:** `100*(1-.99**30)`. **Answer: 26.03 % chance**. State why the inputs have compatible units, and explain which water store, flux, property, probability or statistic the output actually represents. For mixed units, write intermediate conversions explicitly. Distinguish the numerical answer from a claim about the real-world process: the answer follows from the invented inputs and the chosen equation, not from measurements of an actual catchment or aquifer.

**Sensitivity and limits:** A changing climate or serial dependence invalidates this simple sequence probability. If an input is changed by 20%, calculate the new output and describe whether the response is linear or nonlinear. Where appropriate, identify an excluded term or an assumption about spatial uniformity, stationarity, constant flow, conservative chemistry, or homogeneous porous media. This calculation cannot establish the excluded term is zero merely because it produces a tidy result.

### Field or data investigation

Compute the probability of at least one exceedance in a specified number of independent years; discuss dependence and changing probabilities. Put this in the unit investigation setting: A river basin with two gauges and an ungauged tributary. Probabilistic reasoning; Write annual exceedance probability in ordinary language. The monitoring sheet should retain raw values, calibration and a flag for missing or questionable samples. Before interpreting a change, ask whether an independent instrument would observe the same sign and magnitude. Routing can delay and flatten a peak; downstream local rain may amplify a peak even where routing would otherwise attenuate it. Measure storm location and tributary arrival before interpreting the sign of peak-time differences. Use a baseline scenario and an alternative scenario with an explicit change in just one assumption, so that the cause of the model's different output remains visible.

### Interpretation and practical constraints

A fitted return period is not a deterministic forecast or a substitute for approved hazard mapping. Distinguish independence assumptions and stationary probabilities; Calculate event probability for different assumed risk horizons. Break uncertainty into instrumental accuracy, insufficient temporal or spatial sampling, uncertain model coefficients and uncertainty about the governing mechanism itself. These sources can dominate in different circumstances. Report what could make a conclusion false, not merely a plus–minus range attached to a fitted number. An actual abstraction limit, well safety decision, contamination assessment or flood warning requires locally measured and professionally reviewed evidence.

### Problems and answer checks

1. **Calculation and units:** reproduce the example and then change one input by 20%. Retain units at every line and verify that the result is dimensionally meaningful.
2. **Scientific discrimination:** write two competing explanations for the described observations, and give the exact sampling location, instrument and predicted difference that could resolve them.
3. **Transferability:** explain which key assumption is most likely to break in a different soil, geology, season, flow regime or monitoring technology. Design a quick test.
4. **Evidence memo:** distinguish observations, computed quantities and interpretations in a five-sentence note. State a follow-up observation that could reverse the judgment.

**Answer guidance:** a sound answer includes the governing relationship, a physically appropriate measurement boundary, checks on units and uncertainty, and one genuinely differentiating field test. Numerical precision alone does not strengthen an unsupported hydrologic interpretation.

## Lesson 3.5 — Rivers, sediment and hydraulic controls

### How the process works

Flow depth, energy slope and bed roughness influence channel conveyance and sediment motion. Sediment transport depends on thresholds, supply and bed composition, not discharge alone. Begin with a drawing of the physical stores and fluxes relevant to **rivers, sediment and hydraulic controls**, showing both the water-bearing materials and the chosen observation boundary. Explain which forces move the water, solute or energy; identify the reference datum if hydraulic head or elevation is involved. A catchment outlet, soil column, well screen and river reach measure different domains. Never describe the value at one instrument as a universal property without a scaling argument. Distinguish a conservation relationship, which must hold for a correctly bounded system, from a constitutive equation, whose coefficients require calibration and whose validity is conditional on site conditions.

### Evidence, ambiguity and falsifiable alternatives

Cross sections, bed particle surveys, suspended sampling and water-level gradients constrain hydraulic interpretations. For every proposed observation, record units, location, date, time step, instrument support and an independent quality check. Sketch what is measured directly and what must be inferred. Estimate an error or detection limit if the result will be compared across sites or dates. Changes that are smaller than the relevant error should not be described as robust physical trends.

Bed aggradation may result from a tributary sediment pulse despite nearly unchanged basin runoff. A scientifically serious explanation must accommodate rival mechanisms. Identify what the preferred mechanism would predict at another time, depth or location. Choose a second type of evidence—geological context, temperature, chemical tracers, parallel reference catchments or independently surveyed elevations—rather than only refitting the same data. An observation that both models predict equally well is not a discriminating test.

### Worked calculation — Manning ideal discharge

**Illustrative data:** Rectangular section 3 m wide, 1 m deep, n=0.035 and slope=0.002. **Equation or arithmetic:** `(1/.035)*3*(3/5)**(2/3)*math.sqrt(.002)`. **Answer: 2.7269 m³/s**. State why the inputs have compatible units, and explain which water store, flux, property, probability or statistic the output actually represents. For mixed units, write intermediate conversions explicitly. Distinguish the numerical answer from a claim about the real-world process: the answer follows from the invented inputs and the chosen equation, not from measurements of an actual catchment or aquifer.

**Sensitivity and limits:** Natural channels may not have a rectangular shape or one defensible roughness value. If an input is changed by 20%, calculate the new output and describe whether the response is linear or nonlinear. Where appropriate, identify an excluded term or an assumption about spatial uniformity, stationarity, constant flow, conservative chemistry, or homogeneous porous media. This calculation cannot establish the excluded term is zero merely because it produces a tidy result.

### Field or data investigation

Apply Manning's equation with disclosed n and geometry to an ideal channel; test sensitivity to roughness. Put this in the unit investigation setting: A river basin with two gauges and an ungauged tributary. Hydraulic channel screening; Check geometry, slope and roughness assumptions. The monitoring sheet should retain raw values, calibration and a flag for missing or questionable samples. Before interpreting a change, ask whether an independent instrument would observe the same sign and magnitude. Routing can delay and flatten a peak; downstream local rain may amplify a peak even where routing would otherwise attenuate it. Measure storm location and tributary arrival before interpreting the sign of peak-time differences. Use a baseline scenario and an alternative scenario with an explicit change in just one assumption, so that the cause of the model's different output remains visible.

### Interpretation and practical constraints

Manning coefficients and ideal geometry are not transferable to unmeasured floodplain reaches. Separate water motion from sediment threshold conditions; Compute a plausible discharge band rather than one precise number. Break uncertainty into instrumental accuracy, insufficient temporal or spatial sampling, uncertain model coefficients and uncertainty about the governing mechanism itself. These sources can dominate in different circumstances. Report what could make a conclusion false, not merely a plus–minus range attached to a fitted number. An actual abstraction limit, well safety decision, contamination assessment or flood warning requires locally measured and professionally reviewed evidence.

### Problems and answer checks

1. **Calculation and units:** reproduce the example and then change one input by 20%. Retain units at every line and verify that the result is dimensionally meaningful.
2. **Scientific discrimination:** write two competing explanations for the described observations, and give the exact sampling location, instrument and predicted difference that could resolve them.
3. **Transferability:** explain which key assumption is most likely to break in a different soil, geology, season, flow regime or monitoring technology. Design a quick test.
4. **Evidence memo:** distinguish observations, computed quantities and interpretations in a five-sentence note. State a follow-up observation that could reverse the judgment.

**Answer guidance:** a sound answer includes the governing relationship, a physically appropriate measurement boundary, checks on units and uncertainty, and one genuinely differentiating field test. Numerical precision alone does not strengthen an unsupported hydrologic interpretation.

## Integrated laboratory: Use paired hydrographs to test a change in runoff connectivity.

**Research task.** A river basin with two gauges and an ungauged tributary Start from the attached `datasets/unit-03-synthetic.csv`. The records are deliberately fictional and provide no local environmental observations. The learner's deliverable is a short technical notebook, a table of measurements and conversions, a controlled comparison between two interpretations, and a one-page statement of residual uncertainty.

**Phase A — conceptual diagram.** Streamflow is a rate, not a static store. Integrating the area under a hydrograph yields event volume only after choosing the baseline, recording time intervals and converting seconds correctly. Changing the baseline can change estimates of direct runoff substantially. Each observation has a spatial footprint; annotate which terms would require a point sample, area-average estimate or volumetric balance. For groundwater, show screened intervals and vertical datum. For rivers, mark the measurement section and route. For water chemistry, identify concentration, flow and analyte units. A diagram that omits the boundary often hides the missing flux that later produces an apparently anomalous numerical result.

**Phase B — independent calculation.** Routing can delay and flatten a peak; downstream local rain may amplify a peak even where routing would otherwise attenuate it. Measure storm location and tributary arrival before interpreting the sign of peak-time differences. Use at least two independent calculation approaches where possible. Compare the result against a sanity bound: storage cannot be below a declared physically admissible minimum, chemical mixing fractions should lie between zero and one under the assumed ideal endmembers, and a probability cannot exceed unity. Round only after combining inputs; retain raw values and intermediate results in a reproducible notebook.

**Phase C — evaluate the alternative.** Hydraulic geometry and flood probabilities are different kinds of models. Cross-section flow laws require channel roughness and water surface slope; flood frequency requires defensible assumptions about observations and probability stationarity. Replace one assumption at a time. Include a small scenario table showing baseline, lower plausible input and upper plausible input, then a separate table for structural alternatives where equations themselves differ. Explain whether the compared outcomes cross a chosen decision threshold. If no real-world decision threshold has been justified, label the result descriptive only rather than declaring a policy winner.

**Phase D — submit a traceable report.** Include the following in one coherent narrative: (a) research question and ethical scope, (b) boundary and major water or solute pathways, (c) original invented records, (d) exact equation and dimensional checks, (e) rival mechanisms and discriminating observations, (f) sensitivity or uncertainty table, and (g) a short conclusion distinguishing the measurement from its interpretation. State why the data cannot justify a real-world site decision.

### Unit synthesis

Every lesson above contributes a different constraint to the integrated investigation. Cross-check a mass balance against a physically plausible flow path; cross-check a statistical summary against a documented measurement interval; and cross-check a model-derived conclusion against an independent observation wherever feasible. Report what evidence would overturn the preferred conclusion. The appropriate scientific endpoint is not a graph that looks convincing, but an interpretation that remains defensible when another researcher can inspect its data, assumptions and alternatives.
