# Unit 1 — The hydrologic system and its measurements

## Scientific problem for this unit

What can a catchment water balance genuinely tell us about movement, storage and uncertainty? The case-study setting is: **Establish a defensible water ledger for a synthetic upland basin.**. The central difficulty is that the same observed water level, hydrograph, concentration or land-surface change can arise from multiple physical causes. A course in hydrology becomes useful when students learn to infer processes cautiously rather than replacing a missing measurement with a convenient story. This unit integrates conservation laws, field observables and independent checks in a coherent investigation.

### Background and field context

An upland watershed with poorly constrained groundwater export. The investigation asks students to define a measurement support, write the governing equation with correct units, and make a prediction before inspecting hypothetical data. Before examining models, redraw the control volume three times: one for the soil profile, one for the surface stream network and one enclosing all groundwater discharge. Three boundaries demand different flux accounting, so a balance that closes in one may leave unresolved transfers in another. Students should keep a concise field ledger indicating which variables were measured, which were derived, and which were assigned because the problem did not provide enough data.

The unifying tools are dimensional reasoning, boundary diagrams and comparison of rival conceptual models. Catchment delineation, seasonality, conservation of mass, rainfall instrumentation and observational scale all become difficult when scales are mixed, when a sensor's datum is omitted, or when statistical fit is confused with causal evidence. Draw one section or plan view that labels land surface, relevant geological horizons, the stream or well network, and the water-transfer pathways under discussion. Give a sign convention to every flux. For quantities reported as volumes, identify the integration interval and contributing area. Explain why the chosen model domain includes or excludes neighboring exchanges.

### Reading and learning outcomes

Students should be able to calculate a conditional result, describe at least two competing processes, identify limitations of measurement, and write a short reproducible report. Alongside the five lessons, the unit includes a synthetic laboratory dataset and two illustrative slider-driven equations. These models are deliberately simple: use them to see parameter sensitivity, not to recommend operational changes. Any inference about actual water quality, flood hazard or well yield requires site data, qualified review and the relevant authorities.

## Lesson 1.1 — Hydrologic compartments and water fluxes

### How the process works

Precipitation, evapotranspiration, stream export, groundwater transfer and changes in soil, snow, surface and aquifer storage share one conservation equation. A flux has dimensions of volume per time or depth per time after area normalization; a stock has units of volume or equivalent depth. Begin with a drawing of the physical stores and fluxes relevant to **hydrologic compartments and water fluxes**, showing both the water-bearing materials and the chosen observation boundary. Explain which forces move the water, solute or energy; identify the reference datum if hydraulic head or elevation is involved. A catchment outlet, soil column, well screen and river reach measure different domains. Never describe the value at one instrument as a universal property without a scaling argument. Distinguish a conservation relationship, which must hold for a correctly bounded system, from a constitutive equation, whose coefficients require calibration and whose validity is conditional on site conditions.

### Evidence, ambiguity and falsifiable alternatives

Rain gauges, discharge records, soil sensors, snow surveys and groundwater heads sample different volumes and intervals. Closing a basin boundary does not imply groundwater respects the topographic divide. For every proposed observation, record units, location, date, time step, instrument support and an independent quality check. Sketch what is measured directly and what must be inferred. Estimate an error or detection limit if the result will be compared across sites or dates. Changes that are smaller than the relevant error should not be described as robust physical trends.

A rising stream hydrograph might contain displaced pre-event water rather than freshly fallen rain. Water origins and flow pathways require chemical tracers or isotopic evidence, not discharge alone. A scientifically serious explanation must accommodate rival mechanisms. Identify what the preferred mechanism would predict at another time, depth or location. Choose a second type of evidence—geological context, temperature, chemical tracers, parallel reference catchments or independently surveyed elevations—rather than only refitting the same data. An observation that both models predict equally well is not a discriminating test.

### Worked calculation — Catchment annual water balance

**Illustrative data:** P=1,100 mm, ET=550 mm and river yield=420 mm. **Equation or arithmetic:** `1100 - 550 - 420`. **Answer: 130 mm residual**. State why the inputs have compatible units, and explain which water store, flux, property, probability or statistic the output actually represents. For mixed units, write intermediate conversions explicitly. Distinguish the numerical answer from a claim about the real-world process: the answer follows from the invented inputs and the chosen equation, not from measurements of an actual catchment or aquifer.

**Sensitivity and limits:** If subsurface export of 60 mm was omitted, inferred storage change would be 70 mm, not 130 mm. If an input is changed by 20%, calculate the new output and describe whether the response is linear or nonlinear. Where appropriate, identify an excluded term or an assumption about spatial uniformity, stationarity, constant flow, conservative chemistry, or homogeneous porous media. This calculation cannot establish the excluded term is zero merely because it produces a tidy result.

### Field or data investigation

Draw a basin control volume and label each flux as incoming, outgoing or internal. Vary the groundwater leakage term and calculate the residual storage change before explaining the observed hydrograph. Put this in the unit investigation setting: An upland watershed with poorly constrained groundwater export. Conservation audit; Use a ledger with measured versus inferred fluxes. The monitoring sheet should retain raw values, calibration and a flag for missing or questionable samples. Before interpreting a change, ask whether an independent instrument would observe the same sign and magnitude. A monthly gauge shows a late runoff peak despite a short intense burst. Alternative A invokes catchment retention and channel routing; alternative B invokes rainfall falling later in a distant tributary. Discharge alone cannot choose between them. Use a baseline scenario and an alternative scenario with an explicit change in just one assumption, so that the cause of the model's different output remains visible.

### Interpretation and practical constraints

A small residual is not proof that fluxes are correct if compensating measurement errors occur. Check the difference between rainfall and discharge observation footprints; Stress-test the boundary under unmeasured groundwater transfers. Break uncertainty into instrumental accuracy, insufficient temporal or spatial sampling, uncertain model coefficients and uncertainty about the governing mechanism itself. These sources can dominate in different circumstances. Report what could make a conclusion false, not merely a plus–minus range attached to a fitted number. An actual abstraction limit, well safety decision, contamination assessment or flood warning requires locally measured and professionally reviewed evidence.

### Problems and answer checks

1. **Calculation and units:** reproduce the example and then change one input by 20%. Retain units at every line and verify that the result is dimensionally meaningful.
2. **Scientific discrimination:** write two competing explanations for the described observations, and give the exact sampling location, instrument and predicted difference that could resolve them.
3. **Transferability:** explain which key assumption is most likely to break in a different soil, geology, season, flow regime or monitoring technology. Design a quick test.
4. **Evidence memo:** distinguish observations, computed quantities and interpretations in a five-sentence note. State a follow-up observation that could reverse the judgment.

**Answer guidance:** a sound answer includes the governing relationship, a physically appropriate measurement boundary, checks on units and uncertainty, and one genuinely differentiating field test. Numerical precision alone does not strengthen an unsupported hydrologic interpretation.

## Lesson 1.2 — Catchment boundaries and scale

### How the process works

Digital elevation models route surface flow along terrain; watershed masks change with resolution, road culverts, sink filling and engineered drainage. Nested subcatchments can respond very differently to the same rainfall pulse. Begin with a drawing of the physical stores and fluxes relevant to **catchment boundaries and scale**, showing both the water-bearing materials and the chosen observation boundary. Explain which forces move the water, solute or energy; identify the reference datum if hydraulic head or elevation is involved. A catchment outlet, soil column, well screen and river reach measure different domains. Never describe the value at one instrument as a universal property without a scaling argument. Distinguish a conservation relationship, which must hold for a correctly bounded system, from a constitutive equation, whose coefficients require calibration and whose validity is conditional on site conditions.

### Evidence, ambiguity and falsifiable alternatives

Surveyed channels, culvert maps, DEM conditioning and field observations identify physically connected flow paths. A network traced only from raster cells is a model output. For every proposed observation, record units, location, date, time step, instrument support and an independent quality check. Sketch what is measured directly and what must be inferred. Estimate an error or detection limit if the result will be compared across sites or dates. Changes that are smaller than the relevant error should not be described as robust physical trends.

Subsurface conduits in karst and buried urban pipes can move water across surface drainage divides. Mistaking a filled depression for a channel can create phantom contributing area. A scientifically serious explanation must accommodate rival mechanisms. Identify what the preferred mechanism would predict at another time, depth or location. Choose a second type of evidence—geological context, temperature, chemical tracers, parallel reference catchments or independently surveyed elevations—rather than only refitting the same data. An observation that both models predict equally well is not a discriminating test.

### Worked calculation — Raster catchment area

**Illustrative data:** 340 mapped cells, 20 m by 20 m. **Equation or arithmetic:** `340*20*20/1e6`. **Answer: 0.136 km²**. State why the inputs have compatible units, and explain which water store, flux, property, probability or statistic the output actually represents. For mixed units, write intermediate conversions explicitly. Distinguish the numerical answer from a claim about the real-world process: the answer follows from the invented inputs and the chosen equation, not from measurements of an actual catchment or aquifer.

**Sensitivity and limits:** Doubling the grid dimension at unchanged cell count quadruples the derived area. If an input is changed by 20%, calculate the new output and describe whether the response is linear or nonlinear. Where appropriate, identify an excluded term or an assumption about spatial uniformity, stationarity, constant flow, conservative chemistry, or homogeneous porous media. This calculation cannot establish the excluded term is zero merely because it produces a tidy result.

### Field or data investigation

Compare delineations from two raster resolutions against a surveyed culvert and describe how differences affect depth-to-volume conversion. Put this in the unit investigation setting: An upland watershed with poorly constrained groundwater export. Spatial delineation; Compare spatial and temporal supports of measurements. The monitoring sheet should retain raw values, calibration and a flag for missing or questionable samples. Before interpreting a change, ask whether an independent instrument would observe the same sign and magnitude. A monthly gauge shows a late runoff peak despite a short intense burst. Alternative A invokes catchment retention and channel routing; alternative B invokes rainfall falling later in a distant tributary. Discharge alone cannot choose between them. Use a baseline scenario and an alternative scenario with an explicit change in just one assumption, so that the cause of the model's different output remains visible.

### Interpretation and practical constraints

Map area is not the same as storm-effective contributing area; assume neither is constant without data. Map which measurements represent surface rather than underground drainage; Recalculate a derived depth after changing the catchment area. Break uncertainty into instrumental accuracy, insufficient temporal or spatial sampling, uncertain model coefficients and uncertainty about the governing mechanism itself. These sources can dominate in different circumstances. Report what could make a conclusion false, not merely a plus–minus range attached to a fitted number. An actual abstraction limit, well safety decision, contamination assessment or flood warning requires locally measured and professionally reviewed evidence.

### Problems and answer checks

1. **Calculation and units:** reproduce the example and then change one input by 20%. Retain units at every line and verify that the result is dimensionally meaningful.
2. **Scientific discrimination:** write two competing explanations for the described observations, and give the exact sampling location, instrument and predicted difference that could resolve them.
3. **Transferability:** explain which key assumption is most likely to break in a different soil, geology, season, flow regime or monitoring technology. Design a quick test.
4. **Evidence memo:** distinguish observations, computed quantities and interpretations in a five-sentence note. State a follow-up observation that could reverse the judgment.

**Answer guidance:** a sound answer includes the governing relationship, a physically appropriate measurement boundary, checks on units and uncertainty, and one genuinely differentiating field test. Numerical precision alone does not strengthen an unsupported hydrologic interpretation.

## Lesson 1.3 — Precipitation measurement and bias

### How the process works

Rainfall depth is a catchment input, but point gauges record specific locations and may miss convective gradients. Wind undercatch, wetting losses and gauge malfunction can bias snowfall and rain differently. Begin with a drawing of the physical stores and fluxes relevant to **precipitation measurement and bias**, showing both the water-bearing materials and the chosen observation boundary. Explain which forces move the water, solute or energy; identify the reference datum if hydraulic head or elevation is involved. A catchment outlet, soil column, well screen and river reach measure different domains. Never describe the value at one instrument as a universal property without a scaling argument. Distinguish a conservation relationship, which must hold for a correctly bounded system, from a constitutive equation, whose coefficients require calibration and whose validity is conditional on site conditions.

### Evidence, ambiguity and falsifiable alternatives

Tipping-bucket accumulation, manual standard gauges, radar estimates, gauge metadata and quality flags can be combined through cautious adjustment. For every proposed observation, record units, location, date, time step, instrument support and an independent quality check. Sketch what is measured directly and what must be inferred. Estimate an error or detection limit if the result will be compared across sites or dates. Changes that are smaller than the relevant error should not be described as robust physical trends.

An apparent rainfall trend can be caused by station relocation, instrument replacement, or changing observation hour rather than climate. A scientifically serious explanation must accommodate rival mechanisms. Identify what the preferred mechanism would predict at another time, depth or location. Choose a second type of evidence—geological context, temperature, chemical tracers, parallel reference catchments or independently surveyed elevations—rather than only refitting the same data. An observation that both models predict equally well is not a discriminating test.

### Worked calculation — Area-weighted basin rainfall

**Illustrative data:** Two zones: 30% receives 80 mm and 70% receives 50 mm. **Equation or arithmetic:** `0.3*80+0.7*50`. **Answer: 59 mm**. State why the inputs have compatible units, and explain which water store, flux, property, probability or statistic the output actually represents. For mixed units, write intermediate conversions explicitly. Distinguish the numerical answer from a claim about the real-world process: the answer follows from the invented inputs and the chosen equation, not from measurements of an actual catchment or aquifer.

**Sensitivity and limits:** Uncertain zone boundaries or convective rainfall gradients directly affect the mean. If an input is changed by 20%, calculate the new output and describe whether the response is linear or nonlinear. Where appropriate, identify an excluded term or an assumption about spatial uniformity, stationarity, constant flow, conservative chemistry, or homogeneous porous media. This calculation cannot establish the excluded term is zero merely because it produces a tidy result.

### Field or data investigation

Compute a weighted basin-average depth from two gauges, and compare it with the arithmetic mean while documenting weights and coverage. Put this in the unit investigation setting: An upland watershed with poorly constrained groundwater export. Observation bias; Write down raw calibration and maintenance metadata. The monitoring sheet should retain raw values, calibration and a flag for missing or questionable samples. Before interpreting a change, ask whether an independent instrument would observe the same sign and magnitude. A monthly gauge shows a late runoff peak despite a short intense burst. Alternative A invokes catchment retention and channel routing; alternative B invokes rainfall falling later in a distant tributary. Discharge alone cannot choose between them. Use a baseline scenario and an alternative scenario with an explicit change in just one assumption, so that the cause of the model's different output remains visible.

### Interpretation and practical constraints

Radar has reflectivity-conversion and beam limitations; remote rainfall fields are not independent truth. Separate physical signal from changes in instruments or methods; Propagate observation error instead of assuming perfect station measurements. Break uncertainty into instrumental accuracy, insufficient temporal or spatial sampling, uncertain model coefficients and uncertainty about the governing mechanism itself. These sources can dominate in different circumstances. Report what could make a conclusion false, not merely a plus–minus range attached to a fitted number. An actual abstraction limit, well safety decision, contamination assessment or flood warning requires locally measured and professionally reviewed evidence.

### Problems and answer checks

1. **Calculation and units:** reproduce the example and then change one input by 20%. Retain units at every line and verify that the result is dimensionally meaningful.
2. **Scientific discrimination:** write two competing explanations for the described observations, and give the exact sampling location, instrument and predicted difference that could resolve them.
3. **Transferability:** explain which key assumption is most likely to break in a different soil, geology, season, flow regime or monitoring technology. Design a quick test.
4. **Evidence memo:** distinguish observations, computed quantities and interpretations in a five-sentence note. State a follow-up observation that could reverse the judgment.

**Answer guidance:** a sound answer includes the governing relationship, a physically appropriate measurement boundary, checks on units and uncertainty, and one genuinely differentiating field test. Numerical precision alone does not strengthen an unsupported hydrologic interpretation.

## Lesson 1.4 — Water balance and residual storage

### How the process works

A hydrologic budget equates precipitation plus inflow with evapotranspiration, outflow and storage change. The interval controls what storage changes may cancel; annual equilibrium is an assumption, not a law. Begin with a drawing of the physical stores and fluxes relevant to **water balance and residual storage**, showing both the water-bearing materials and the chosen observation boundary. Explain which forces move the water, solute or energy; identify the reference datum if hydraulic head or elevation is involved. A catchment outlet, soil column, well screen and river reach measure different domains. Never describe the value at one instrument as a universal property without a scaling argument. Distinguish a conservation relationship, which must hold for a correctly bounded system, from a constitutive equation, whose coefficients require calibration and whose validity is conditional on site conditions.

### Evidence, ambiguity and falsifiable alternatives

Paired precipitation and discharge totals, evaporation estimates, ground-water data and storage observations constrain only some terms. For every proposed observation, record units, location, date, time step, instrument support and an independent quality check. Sketch what is measured directly and what must be inferred. Estimate an error or detection limit if the result will be compared across sites or dates. Changes that are smaller than the relevant error should not be described as robust physical trends.

Unmeasured imports through pipes or interbasin aquifers can masquerade as a negative storage change. A scientifically serious explanation must accommodate rival mechanisms. Identify what the preferred mechanism would predict at another time, depth or location. Choose a second type of evidence—geological context, temperature, chemical tracers, parallel reference catchments or independently surveyed elevations—rather than only refitting the same data. An observation that both models predict equally well is not a discriminating test.

### Worked calculation — Storage residual with inputs

**Illustrative data:** Basin receives 140 mm rainfall and 12 mm imported water; ET=60 mm, outflow=75 mm. **Equation or arithmetic:** `140+12-60-75`. **Answer: 17 mm**. State why the inputs have compatible units, and explain which water store, flux, property, probability or statistic the output actually represents. For mixed units, write intermediate conversions explicitly. Distinguish the numerical answer from a claim about the real-world process: the answer follows from the invented inputs and the chosen equation, not from measurements of an actual catchment or aquifer.

**Sensitivity and limits:** Misclassifying the import as local rain would obscure infrastructure dependence. If an input is changed by 20%, calculate the new output and describe whether the response is linear or nonlinear. Where appropriate, identify an excluded term or an assumption about spatial uniformity, stationarity, constant flow, conservative chemistry, or homogeneous porous media. This calculation cannot establish the excluded term is zero merely because it produces a tidy result.

### Field or data investigation

Build monthly and annual balances from the same fictional records and diagnose why aggregation conceals seasonally important deficits. Put this in the unit investigation setting: An upland watershed with poorly constrained groundwater export. Conceptual model; Annotate every state and exchange in a systems diagram. The monitoring sheet should retain raw values, calibration and a flag for missing or questionable samples. Before interpreting a change, ask whether an independent instrument would observe the same sign and magnitude. A monthly gauge shows a late runoff peak despite a short intense burst. Alternative A invokes catchment retention and channel routing; alternative B invokes rainfall falling later in a distant tributary. Discharge alone cannot choose between them. Use a baseline scenario and an alternative scenario with an explicit change in just one assumption, so that the cause of the model's different output remains visible.

### Interpretation and practical constraints

Residuals combine real storage, measurement errors and omitted fluxes; do not rename a residual recharge without evidence. Distinguish a controlling assumption from an observed causal mechanism; Use counterfactual scenarios with and without the assumed transfer. Break uncertainty into instrumental accuracy, insufficient temporal or spatial sampling, uncertain model coefficients and uncertainty about the governing mechanism itself. These sources can dominate in different circumstances. Report what could make a conclusion false, not merely a plus–minus range attached to a fitted number. An actual abstraction limit, well safety decision, contamination assessment or flood warning requires locally measured and professionally reviewed evidence.

### Problems and answer checks

1. **Calculation and units:** reproduce the example and then change one input by 20%. Retain units at every line and verify that the result is dimensionally meaningful.
2. **Scientific discrimination:** write two competing explanations for the described observations, and give the exact sampling location, instrument and predicted difference that could resolve them.
3. **Transferability:** explain which key assumption is most likely to break in a different soil, geology, season, flow regime or monitoring technology. Design a quick test.
4. **Evidence memo:** distinguish observations, computed quantities and interpretations in a five-sentence note. State a follow-up observation that could reverse the judgment.

**Answer guidance:** a sound answer includes the governing relationship, a physically appropriate measurement boundary, checks on units and uncertainty, and one genuinely differentiating field test. Numerical precision alone does not strengthen an unsupported hydrologic interpretation.

## Lesson 1.5 — Hydrologic time and observation design

### How the process works

Storm response is sampled over minutes to days whereas groundwater recession, land-use change and climate shifts may unfold over years. Time steps, rating-curve errors and sensor drift affect the signal scientists infer. Begin with a drawing of the physical stores and fluxes relevant to **hydrologic time and observation design**, showing both the water-bearing materials and the chosen observation boundary. Explain which forces move the water, solute or energy; identify the reference datum if hydraulic head or elevation is involved. A catchment outlet, soil column, well screen and river reach measure different domains. Never describe the value at one instrument as a universal property without a scaling argument. Distinguish a conservation relationship, which must hold for a correctly bounded system, from a constitutive equation, whose coefficients require calibration and whose validity is conditional on site conditions.

### Evidence, ambiguity and falsifiable alternatives

Time-stamped flow and rain observations, documented clock synchronization, sensor maintenance and recorded missing intervals support inference. For every proposed observation, record units, location, date, time step, instrument support and an independent quality check. Sketch what is measured directly and what must be inferred. Estimate an error or detection limit if the result will be compared across sites or dates. Changes that are smaller than the relevant error should not be described as robust physical trends.

A peak shift between stations may be inaccurate time synchronization or a genuine routing difference. A scientifically serious explanation must accommodate rival mechanisms. Identify what the preferred mechanism would predict at another time, depth or location. Choose a second type of evidence—geological context, temperature, chemical tracers, parallel reference catchments or independently surveyed elevations—rather than only refitting the same data. An observation that both models predict equally well is not a discriminating test.

### Worked calculation — Hydrograph time resolution

**Illustrative data:** Rainfall peak 09:30 and downstream flow peak 13:45. **Equation or arithmetic:** `(13*60+45-(9*60+30))/60`. **Answer: 4.25 hours**. State why the inputs have compatible units, and explain which water store, flux, property, probability or statistic the output actually represents. For mixed units, write intermediate conversions explicitly. Distinguish the numerical answer from a claim about the real-world process: the answer follows from the invented inputs and the chosen equation, not from measurements of an actual catchment or aquifer.

**Sensitivity and limits:** Time synchronization errors of 30 minutes can materially change this estimate. If an input is changed by 20%, calculate the new output and describe whether the response is linear or nonlinear. Where appropriate, identify an excluded term or an assumption about spatial uniformity, stationarity, constant flow, conservative chemistry, or homogeneous porous media. This calculation cannot establish the excluded term is zero merely because it produces a tidy result.

### Field or data investigation

Align clocks and compare peak time at three stations; report resolution and timing error before inferring travel speed. Put this in the unit investigation setting: An upland watershed with poorly constrained groundwater export. Time and scale; Resample a record at two temporal resolutions. The monitoring sheet should retain raw values, calibration and a flag for missing or questionable samples. Before interpreting a change, ask whether an independent instrument would observe the same sign and magnitude. A monthly gauge shows a late runoff peak despite a short intense burst. Alternative A invokes catchment retention and channel routing; alternative B invokes rainfall falling later in a distant tributary. Discharge alone cannot choose between them. Use a baseline scenario and an alternative scenario with an explicit change in just one assumption, so that the cause of the model's different output remains visible.

### Interpretation and practical constraints

Sampling faster cannot repair systematic instrument bias or missing spatial coverage. Explain whether a lag is a measured response or an inferred residence time; Revisit a conclusion after excluding a sensor-failure interval. Break uncertainty into instrumental accuracy, insufficient temporal or spatial sampling, uncertain model coefficients and uncertainty about the governing mechanism itself. These sources can dominate in different circumstances. Report what could make a conclusion false, not merely a plus–minus range attached to a fitted number. An actual abstraction limit, well safety decision, contamination assessment or flood warning requires locally measured and professionally reviewed evidence.

### Problems and answer checks

1. **Calculation and units:** reproduce the example and then change one input by 20%. Retain units at every line and verify that the result is dimensionally meaningful.
2. **Scientific discrimination:** write two competing explanations for the described observations, and give the exact sampling location, instrument and predicted difference that could resolve them.
3. **Transferability:** explain which key assumption is most likely to break in a different soil, geology, season, flow regime or monitoring technology. Design a quick test.
4. **Evidence memo:** distinguish observations, computed quantities and interpretations in a five-sentence note. State a follow-up observation that could reverse the judgment.

**Answer guidance:** a sound answer includes the governing relationship, a physically appropriate measurement boundary, checks on units and uncertainty, and one genuinely differentiating field test. Numerical precision alone does not strengthen an unsupported hydrologic interpretation.

## Integrated laboratory: Establish a defensible water ledger for a synthetic upland basin.

**Research task.** An upland watershed with poorly constrained groundwater export Start from the attached `datasets/unit-01-synthetic.csv`. The records are deliberately fictional and provide no local environmental observations. The learner's deliverable is a short technical notebook, a table of measurements and conversions, a controlled comparison between two interpretations, and a one-page statement of residual uncertainty.

**Phase A — conceptual diagram.** Before examining models, redraw the control volume three times: one for the soil profile, one for the surface stream network and one enclosing all groundwater discharge. Three boundaries demand different flux accounting, so a balance that closes in one may leave unresolved transfers in another. Each observation has a spatial footprint; annotate which terms would require a point sample, area-average estimate or volumetric balance. For groundwater, show screened intervals and vertical datum. For rivers, mark the measurement section and route. For water chemistry, identify concentration, flow and analyte units. A diagram that omits the boundary often hides the missing flux that later produces an apparently anomalous numerical result.

**Phase B — independent calculation.** A monthly gauge shows a late runoff peak despite a short intense burst. Alternative A invokes catchment retention and channel routing; alternative B invokes rainfall falling later in a distant tributary. Discharge alone cannot choose between them. Use at least two independent calculation approaches where possible. Compare the result against a sanity bound: storage cannot be below a declared physically admissible minimum, chemical mixing fractions should lie between zero and one under the assumed ideal endmembers, and a probability cannot exceed unity. Round only after combining inputs; retain raw values and intermediate results in a reproducible notebook.

**Phase C — evaluate the alternative.** Rain and discharge have different measurement supports: rainfall is typically sampled in depth and discharge in volume per time. Multiply rainfall depth in metres by contributing area in square metres before comparing event runoff volume. Replace one assumption at a time. Include a small scenario table showing baseline, lower plausible input and upper plausible input, then a separate table for structural alternatives where equations themselves differ. Explain whether the compared outcomes cross a chosen decision threshold. If no real-world decision threshold has been justified, label the result descriptive only rather than declaring a policy winner.

**Phase D — submit a traceable report.** Include the following in one coherent narrative: (a) research question and ethical scope, (b) boundary and major water or solute pathways, (c) original invented records, (d) exact equation and dimensional checks, (e) rival mechanisms and discriminating observations, (f) sensitivity or uncertainty table, and (g) a short conclusion distinguishing the measurement from its interpretation. State why the data cannot justify a real-world site decision.

### Unit synthesis

Every lesson above contributes a different constraint to the integrated investigation. Cross-check a mass balance against a physically plausible flow path; cross-check a statistical summary against a documented measurement interval; and cross-check a model-derived conclusion against an independent observation wherever feasible. Report what evidence would overturn the preferred conclusion. The appropriate scientific endpoint is not a graph that looks convincing, but an interpretation that remains defensible when another researcher can inspect its data, assumptions and alternatives.
