# Unit 8 — Integrated hydrologic research and decision making

## Scientific problem for this unit

How do monitoring designs, models and communication support reproducible and equitable water decisions? The case-study setting is: **Design a complete observational research program with falsifiable outcomes.**. The central difficulty is that the same observed water level, hydrograph, concentration or land-surface change can arise from multiple physical causes. A course in hydrology becomes useful when students learn to infer processes cautiously rather than replacing a missing measurement with a convenient story. This unit integrates conservation laws, field observables and independent checks in a coherent investigation.

### Background and field context

An independent study team evaluating whether restoration improved river and groundwater outcomes. The investigation asks students to define a measurement support, write the governing equation with correct units, and make a prediction before inspecting hypothetical data. A reproducible study preserves raw files, time zones, site identifiers, processing scripts, versions, decisions and exclusion rules. Separate model training periods from independent validation periods before reporting forecast skill. Students should keep a concise field ledger indicating which variables were measured, which were derived, and which were assigned because the problem did not provide enough data.

The unifying tools are dimensional reasoning, boundary diagrams and comparison of rival conceptual models. Data quality, modeling, calibration, uncertainty, risk and stakeholder decisions all become difficult when scales are mixed, when a sensor's datum is omitted, or when statistical fit is confused with causal evidence. Draw one section or plan view that labels land surface, relevant geological horizons, the stream or well network, and the water-transfer pathways under discussion. Give a sign convention to every flux. For quantities reported as volumes, identify the integration interval and contributing area. Explain why the chosen model domain includes or excludes neighboring exchanges.

### Reading and learning outcomes

Students should be able to calculate a conditional result, describe at least two competing processes, identify limitations of measurement, and write a short reproducible report. Alongside the five lessons, the unit includes a synthetic laboratory dataset and two illustrative slider-driven equations. These models are deliberately simple: use them to see parameter sensitivity, not to recommend operational changes. Any inference about actual water quality, flood hazard or well yield requires site data, qualified review and the relevant authorities.

## Lesson 8.1 — Observation networks and sampling design

### How the process works

Monitoring design should begin with a decision question, required accuracy, spatial representativeness and expected timescale. Redundancy makes malfunction detectable but raises costs. Begin with a drawing of the physical stores and fluxes relevant to **observation networks and sampling design**, showing both the water-bearing materials and the chosen observation boundary. Explain which forces move the water, solute or energy; identify the reference datum if hydraulic head or elevation is involved. A catchment outlet, soil column, well screen and river reach measure different domains. Never describe the value at one instrument as a universal property without a scaling argument. Distinguish a conservation relationship, which must hold for a correctly bounded system, from a constitutive equation, whose coefficients require calibration and whose validity is conditional on site conditions.

### Evidence, ambiguity and falsifiable alternatives

Sensor cross-checks, field logs, maintenance records and independent samples help separate environmental change from measurement drift. For every proposed observation, record units, location, date, time step, instrument support and an independent quality check. Sketch what is measured directly and what must be inferred. Estimate an error or detection limit if the result will be compared across sites or dates. Changes that are smaller than the relevant error should not be described as robust physical trends.

Agreement among collocated sensors can reflect shared calibration error rather than independent confirmation. A scientifically serious explanation must accommodate rival mechanisms. Identify what the preferred mechanism would predict at another time, depth or location. Choose a second type of evidence—geological context, temperature, chemical tracers, parallel reference catchments or independently surveyed elevations—rather than only refitting the same data. An observation that both models predict equally well is not a discriminating test.

### Worked calculation — Network data completeness

**Illustrative data:** Hourly station logged 680 observations during a 30-day period with 720 expected. **Equation or arithmetic:** `100*680/720`. **Answer: 94.444 % complete**. State why the inputs have compatible units, and explain which water store, flux, property, probability or statistic the output actually represents. For mixed units, write intermediate conversions explicitly. Distinguish the numerical answer from a claim about the real-world process: the answer follows from the invented inputs and the chosen equation, not from measurements of an actual catchment or aquifer.

**Sensitivity and limits:** Missing hours clustered during storms are more consequential than random omissions. If an input is changed by 20%, calculate the new output and describe whether the response is linear or nonlinear. Where appropriate, identify an excluded term or an assumption about spatial uniformity, stationarity, constant flow, conservative chemistry, or homogeneous porous media. This calculation cannot establish the excluded term is zero merely because it produces a tidy result.

### Field or data investigation

Choose locations for three stream gauges and four wells given an invented basin map and justify each placement. Put this in the unit investigation setting: An independent study team evaluating whether restoration improved river and groundwater outcomes. Instrument planning; Design monitoring to falsify a claim rather than decorate a map. The monitoring sheet should retain raw values, calibration and a flag for missing or questionable samples. Before interpreting a change, ask whether an independent instrument would observe the same sign and magnitude. Excellent fit at one monitoring station might conceal unequal errors upstream or during peak flow. Compare multiple objectives, including flow volume, timing, groundwater head and data coverage. Use a baseline scenario and an alternative scenario with an explicit change in just one assumption, so that the cause of the model's different output remains visible.

### Interpretation and practical constraints

Convenience sampling can systematically miss inaccessible floodplains, deep aquifers and rare events. Budget for maintenance and independent calibration; Use missing-data scenarios to test a proposed network. Break uncertainty into instrumental accuracy, insufficient temporal or spatial sampling, uncertain model coefficients and uncertainty about the governing mechanism itself. These sources can dominate in different circumstances. Report what could make a conclusion false, not merely a plus–minus range attached to a fitted number. An actual abstraction limit, well safety decision, contamination assessment or flood warning requires locally measured and professionally reviewed evidence.

### Problems and answer checks

1. **Calculation and units:** reproduce the example and then change one input by 20%. Retain units at every line and verify that the result is dimensionally meaningful.
2. **Scientific discrimination:** write two competing explanations for the described observations, and give the exact sampling location, instrument and predicted difference that could resolve them.
3. **Transferability:** explain which key assumption is most likely to break in a different soil, geology, season, flow regime or monitoring technology. Design a quick test.
4. **Evidence memo:** distinguish observations, computed quantities and interpretations in a five-sentence note. State a follow-up observation that could reverse the judgment.

**Answer guidance:** a sound answer includes the governing relationship, a physically appropriate measurement boundary, checks on units and uncertainty, and one genuinely differentiating field test. Numerical precision alone does not strengthen an unsupported hydrologic interpretation.

## Lesson 8.2 — Hydrologic models and calibration

### How the process works

A model encodes conservation laws, constitutive relationships and approximated boundaries. Calibrated fit can conceal compensation among parameters; prediction is evaluated on independent data. Begin with a drawing of the physical stores and fluxes relevant to **hydrologic models and calibration**, showing both the water-bearing materials and the chosen observation boundary. Explain which forces move the water, solute or energy; identify the reference datum if hydraulic head or elevation is involved. A catchment outlet, soil column, well screen and river reach measure different domains. Never describe the value at one instrument as a universal property without a scaling argument. Distinguish a conservation relationship, which must hold for a correctly bounded system, from a constitutive equation, whose coefficients require calibration and whose validity is conditional on site conditions.

### Evidence, ambiguity and falsifiable alternatives

Rainfall-runoff records, aquifer heads, fluxes, event peaks and water quality provide multi-objective observations. For every proposed observation, record units, location, date, time step, instrument support and an independent quality check. Sketch what is measured directly and what must be inferred. Estimate an error or detection limit if the result will be compared across sites or dates. Changes that are smaller than the relevant error should not be described as robust physical trends.

A close hydrograph fit might come from an incorrect runoff parameter balanced against channel-routing error. A scientifically serious explanation must accommodate rival mechanisms. Identify what the preferred mechanism would predict at another time, depth or location. Choose a second type of evidence—geological context, temperature, chemical tracers, parallel reference catchments or independently surveyed elevations—rather than only refitting the same data. An observation that both models predict equally well is not a discriminating test.

### Worked calculation — Mean absolute model error

**Illustrative data:** Absolute daily errors are 3, 5, 2 and 6 m³/s. **Equation or arithmetic:** `(3+5+2+6)/4`. **Answer: 4 m³/s**. State why the inputs have compatible units, and explain which water store, flux, property, probability or statistic the output actually represents. For mixed units, write intermediate conversions explicitly. Distinguish the numerical answer from a claim about the real-world process: the answer follows from the invented inputs and the chosen equation, not from measurements of an actual catchment or aquifer.

**Sensitivity and limits:** MAE hides bias direction and relative importance of extreme flows. If an input is changed by 20%, calculate the new output and describe whether the response is linear or nonlinear. Where appropriate, identify an excluded term or an assumption about spatial uniformity, stationarity, constant flow, conservative chemistry, or homogeneous porous media. This calculation cannot establish the excluded term is zero merely because it produces a tidy result.

### Field or data investigation

Fit a simple reservoir model to training data and evaluate unseen high-flow events and residual structure. Put this in the unit investigation setting: An independent study team evaluating whether restoration improved river and groundwater outcomes. Model validation; Separate calibrated fit from independent forecasting performance. The monitoring sheet should retain raw values, calibration and a flag for missing or questionable samples. Before interpreting a change, ask whether an independent instrument would observe the same sign and magnitude. Excellent fit at one monitoring station might conceal unequal errors upstream or during peak flow. Compare multiple objectives, including flow volume, timing, groundwater head and data coverage. Use a baseline scenario and an alternative scenario with an explicit change in just one assumption, so that the cause of the model's different output remains visible.

### Interpretation and practical constraints

A fitted parameter need not correspond to a measurable physical property if the model structure is wrong. Examine multiple performance metrics and internal residual patterns; Challenge predictions with uncalibrated events. Break uncertainty into instrumental accuracy, insufficient temporal or spatial sampling, uncertain model coefficients and uncertainty about the governing mechanism itself. These sources can dominate in different circumstances. Report what could make a conclusion false, not merely a plus–minus range attached to a fitted number. An actual abstraction limit, well safety decision, contamination assessment or flood warning requires locally measured and professionally reviewed evidence.

### Problems and answer checks

1. **Calculation and units:** reproduce the example and then change one input by 20%. Retain units at every line and verify that the result is dimensionally meaningful.
2. **Scientific discrimination:** write two competing explanations for the described observations, and give the exact sampling location, instrument and predicted difference that could resolve them.
3. **Transferability:** explain which key assumption is most likely to break in a different soil, geology, season, flow regime or monitoring technology. Design a quick test.
4. **Evidence memo:** distinguish observations, computed quantities and interpretations in a five-sentence note. State a follow-up observation that could reverse the judgment.

**Answer guidance:** a sound answer includes the governing relationship, a physically appropriate measurement boundary, checks on units and uncertainty, and one genuinely differentiating field test. Numerical precision alone does not strengthen an unsupported hydrologic interpretation.

## Lesson 8.3 — Uncertainty, sensitivity and decision thresholds

### How the process works

Uncertainty includes measurement errors, unknown parameters, model structural inadequacy and plausible future forcing. Decision thresholds should be evaluated across credible scenarios. Begin with a drawing of the physical stores and fluxes relevant to **uncertainty, sensitivity and decision thresholds**, showing both the water-bearing materials and the chosen observation boundary. Explain which forces move the water, solute or energy; identify the reference datum if hydraulic head or elevation is involved. A catchment outlet, soil column, well screen and river reach measure different domains. Never describe the value at one instrument as a universal property without a scaling argument. Distinguish a conservation relationship, which must hold for a correctly bounded system, from a constitutive equation, whose coefficients require calibration and whose validity is conditional on site conditions.

### Evidence, ambiguity and falsifiable alternatives

Calibration records, alternative models, sensor precision, parameter bounds and scenario documentation allow transparent comparison. For every proposed observation, record units, location, date, time step, instrument support and an independent quality check. Sketch what is measured directly and what must be inferred. Estimate an error or detection limit if the result will be compared across sites or dates. Changes that are smaller than the relevant error should not be described as robust physical trends.

A narrow parameter confidence interval can coexist with a badly misspecified conceptual model. A scientifically serious explanation must accommodate rival mechanisms. Identify what the preferred mechanism would predict at another time, depth or location. Choose a second type of evidence—geological context, temperature, chemical tracers, parallel reference catchments or independently surveyed elevations—rather than only refitting the same data. An observation that both models predict equally well is not a discriminating test.

### Worked calculation — Recharge scenario uncertainty

**Illustrative data:** Assumed baseline recharge 150 mm/year, scenarios -30% and +20%. **Equation or arithmetic:** `(150*.70,150*1.20)`. **Answer: 105 and 180 mm/year interval**. State why the inputs have compatible units, and explain which water store, flux, property, probability or statistic the output actually represents. For mixed units, write intermediate conversions explicitly. Distinguish the numerical answer from a claim about the real-world process: the answer follows from the invented inputs and the chosen equation, not from measurements of an actual catchment or aquifer.

**Sensitivity and limits:** Scenario brackets are conditional choices, not validated probability bounds. If an input is changed by 20%, calculate the new output and describe whether the response is linear or nonlinear. Where appropriate, identify an excluded term or an assumption about spatial uniformity, stationarity, constant flow, conservative chemistry, or homogeneous porous media. This calculation cannot establish the excluded term is zero merely because it produces a tidy result.

### Field or data investigation

Run upper and lower rainfall/recharge scenarios and show when an ecological-flow criterion changes status. Put this in the unit investigation setting: An independent study team evaluating whether restoration improved river and groundwater outcomes. Decision under uncertainty; State policy threshold and uncertain model inputs. The monitoring sheet should retain raw values, calibration and a flag for missing or questionable samples. Before interpreting a change, ask whether an independent instrument would observe the same sign and magnitude. Excellent fit at one monitoring station might conceal unequal errors upstream or during peak flow. Compare multiple objectives, including flow volume, timing, groundwater head and data coverage. Use a baseline scenario and an alternative scenario with an explicit change in just one assumption, so that the cause of the model's different output remains visible.

### Interpretation and practical constraints

An uncertainty range is only as comprehensive as the neglected processes and alternatives you actually included. Check for structural alternatives missed by parameter intervals; Identify scenarios that change the management choice. Break uncertainty into instrumental accuracy, insufficient temporal or spatial sampling, uncertain model coefficients and uncertainty about the governing mechanism itself. These sources can dominate in different circumstances. Report what could make a conclusion false, not merely a plus–minus range attached to a fitted number. An actual abstraction limit, well safety decision, contamination assessment or flood warning requires locally measured and professionally reviewed evidence.

### Problems and answer checks

1. **Calculation and units:** reproduce the example and then change one input by 20%. Retain units at every line and verify that the result is dimensionally meaningful.
2. **Scientific discrimination:** write two competing explanations for the described observations, and give the exact sampling location, instrument and predicted difference that could resolve them.
3. **Transferability:** explain which key assumption is most likely to break in a different soil, geology, season, flow regime or monitoring technology. Design a quick test.
4. **Evidence memo:** distinguish observations, computed quantities and interpretations in a five-sentence note. State a follow-up observation that could reverse the judgment.

**Answer guidance:** a sound answer includes the governing relationship, a physically appropriate measurement boundary, checks on units and uncertainty, and one genuinely differentiating field test. Numerical precision alone does not strengthen an unsupported hydrologic interpretation.

## Lesson 8.4 — Adaptive management and intervention testing

### How the process works

Water management is an iterative decision process: specify an intervention, record a baseline, compare with a plausible counterfactual and adjust only after monitoring supports the change. Operational rules can be tested as policy scenarios but do not become empirical facts merely because a model predicts success. Begin with a drawing of the physical stores and fluxes relevant to **adaptive management and intervention testing**, showing both the water-bearing materials and the chosen observation boundary. Explain which forces move the water, solute or energy; identify the reference datum if hydraulic head or elevation is involved. A catchment outlet, soil column, well screen and river reach measure different domains. Never describe the value at one instrument as a universal property without a scaling argument. Distinguish a conservation relationship, which must hold for a correctly bounded system, from a constitutive equation, whose coefficients require calibration and whose validity is conditional on site conditions.

### Evidence, ambiguity and falsifiable alternatives

Reservoir releases, environmental flow indicators, groundwater heads, irrigator withdrawals and independent rain gauges document coupled outcomes. For every proposed observation, record units, location, date, time step, instrument support and an independent quality check. Sketch what is measured directly and what must be inferred. Estimate an error or detection limit if the result will be compared across sites or dates. Changes that are smaller than the relevant error should not be described as robust physical trends.

A post-intervention increase in low flows may be caused by a wetter year rather than the management rule; a downstream ecological gain may coincide with unexpected upstream harm. A scientifically serious explanation must accommodate rival mechanisms. Identify what the preferred mechanism would predict at another time, depth or location. Choose a second type of evidence—geological context, temperature, chemical tracers, parallel reference catchments or independently surveyed elevations—rather than only refitting the same data. An observation that both models predict equally well is not a discriminating test.

### Worked calculation — Adaptive policy threshold

**Illustrative data:** A release rule requires 12 m³/s in channel; modeled policy gives 14 m³/s. **Equation or arithmetic:** `14-12`. **Answer: 2 m³/s above threshold**. State why the inputs have compatible units, and explain which water store, flux, property, probability or statistic the output actually represents. For mixed units, write intermediate conversions explicitly. Distinguish the numerical answer from a claim about the real-world process: the answer follows from the invented inputs and the chosen equation, not from measurements of an actual catchment or aquifer.

**Sensitivity and limits:** Flow compliance alone does not prove ecological benefit, especially if timing is incorrect. If an input is changed by 20%, calculate the new output and describe whether the response is linear or nonlinear. Where appropriate, identify an excluded term or an assumption about spatial uniformity, stationarity, constant flow, conservative chemistry, or homogeneous porous media. This calculation cannot establish the excluded term is zero merely because it produces a tidy result.

### Field or data investigation

Create a before-after control-impact design for a synthetic river basin, identify confounders and set measurable thresholds for revising management. Put this in the unit investigation setting: An independent study team evaluating whether restoration improved river and groundwater outcomes. Adaptive intervention; Identify an actual observable counterfactual. The monitoring sheet should retain raw values, calibration and a flag for missing or questionable samples. Before interpreting a change, ask whether an independent instrument would observe the same sign and magnitude. Excellent fit at one monitoring station might conceal unequal errors upstream or during peak flow. Compare multiple objectives, including flow volume, timing, groundwater head and data coverage. Use a baseline scenario and an alternative scenario with an explicit change in just one assumption, so that the cause of the model's different output remains visible.

### Interpretation and practical constraints

A modelled optimum does not resolve water-rights conflicts or replace consultation with affected users. Design a before-after comparison with control catchments; Specify a measured threshold for changing operational policy. Break uncertainty into instrumental accuracy, insufficient temporal or spatial sampling, uncertain model coefficients and uncertainty about the governing mechanism itself. These sources can dominate in different circumstances. Report what could make a conclusion false, not merely a plus–minus range attached to a fitted number. An actual abstraction limit, well safety decision, contamination assessment or flood warning requires locally measured and professionally reviewed evidence.

### Problems and answer checks

1. **Calculation and units:** reproduce the example and then change one input by 20%. Retain units at every line and verify that the result is dimensionally meaningful.
2. **Scientific discrimination:** write two competing explanations for the described observations, and give the exact sampling location, instrument and predicted difference that could resolve them.
3. **Transferability:** explain which key assumption is most likely to break in a different soil, geology, season, flow regime or monitoring technology. Design a quick test.
4. **Evidence memo:** distinguish observations, computed quantities and interpretations in a five-sentence note. State a follow-up observation that could reverse the judgment.

**Answer guidance:** a sound answer includes the governing relationship, a physically appropriate measurement boundary, checks on units and uncertainty, and one genuinely differentiating field test. Numerical precision alone does not strengthen an unsupported hydrologic interpretation.

## Lesson 8.5 — Research ethics, reproducibility and public communication

### How the process works

Hydrologic decisions affect ecosystems, agricultural users, water utilities and communities that may have unequal access to data. Reproducibility requires traceable transformations, versions and uncertainty disclosure. Begin with a drawing of the physical stores and fluxes relevant to **research ethics, reproducibility and public communication**, showing both the water-bearing materials and the chosen observation boundary. Explain which forces move the water, solute or energy; identify the reference datum if hydraulic head or elevation is involved. A catchment outlet, soil column, well screen and river reach measure different domains. Never describe the value at one instrument as a universal property without a scaling argument. Distinguish a conservation relationship, which must hold for a correctly bounded system, from a constitutive equation, whose coefficients require calibration and whose validity is conditional on site conditions.

### Evidence, ambiguity and falsifiable alternatives

Open metadata, anonymized or permitted sampling locations, complete scripts and independent checks permit technical scrutiny. For every proposed observation, record units, location, date, time step, instrument support and an independent quality check. Sketch what is measured directly and what must be inferred. Estimate an error or detection limit if the result will be compared across sites or dates. Changes that are smaller than the relevant error should not be described as robust physical trends.

Data gaps near marginalized communities can make an apparently representative model inequitable even with excellent global fit. A scientifically serious explanation must accommodate rival mechanisms. Identify what the preferred mechanism would predict at another time, depth or location. Choose a second type of evidence—geological context, temperature, chemical tracers, parallel reference catchments or independently surveyed elevations—rather than only refitting the same data. An observation that both models predict equally well is not a discriminating test.

### Worked calculation — Water access comparison

**Illustrative data:** District A: 400 households with reliable access out of 500; B: 450 out of 750. **Equation or arithmetic:** `(100*400/500,100*450/750)`. **Answer: 80 and 60 % A and B**. State why the inputs have compatible units, and explain which water store, flux, property, probability or statistic the output actually represents. For mixed units, write intermediate conversions explicitly. Distinguish the numerical answer from a claim about the real-world process: the answer follows from the invented inputs and the chosen equation, not from measurements of an actual catchment or aquifer.

**Sensitivity and limits:** Coverage percentages do not by themselves quantify hours of service or quality. If an input is changed by 20%, calculate the new output and describe whether the response is linear or nonlinear. Where appropriate, identify an excluded term or an assumption about spatial uniformity, stationarity, constant flow, conservative chemistry, or homogeneous porous media. This calculation cannot establish the excluded term is zero merely because it produces a tidy result.

### Field or data investigation

Draft a preregistered monitoring protocol and a plain-language decision memo reporting evidence, assumptions and unresolved disagreement. Put this in the unit investigation setting: An independent study team evaluating whether restoration improved river and groundwater outcomes. Research transparency; Protect sensitive site locations while providing method provenance. The monitoring sheet should retain raw values, calibration and a flag for missing or questionable samples. Before interpreting a change, ask whether an independent instrument would observe the same sign and magnitude. Excellent fit at one monitoring station might conceal unequal errors upstream or during peak flow. Compare multiple objectives, including flow volume, timing, groundwater head and data coverage. Use a baseline scenario and an alternative scenario with an explicit change in just one assumption, so that the cause of the model's different output remains visible.

### Interpretation and practical constraints

Never publish private well addresses or make health, safety or rights decisions from an unvalidated classroom model. Include social and ecological limitations in quantitative conclusions; Write a communication plan for affected communities. Break uncertainty into instrumental accuracy, insufficient temporal or spatial sampling, uncertain model coefficients and uncertainty about the governing mechanism itself. These sources can dominate in different circumstances. Report what could make a conclusion false, not merely a plus–minus range attached to a fitted number. An actual abstraction limit, well safety decision, contamination assessment or flood warning requires locally measured and professionally reviewed evidence.

### Problems and answer checks

1. **Calculation and units:** reproduce the example and then change one input by 20%. Retain units at every line and verify that the result is dimensionally meaningful.
2. **Scientific discrimination:** write two competing explanations for the described observations, and give the exact sampling location, instrument and predicted difference that could resolve them.
3. **Transferability:** explain which key assumption is most likely to break in a different soil, geology, season, flow regime or monitoring technology. Design a quick test.
4. **Evidence memo:** distinguish observations, computed quantities and interpretations in a five-sentence note. State a follow-up observation that could reverse the judgment.

**Answer guidance:** a sound answer includes the governing relationship, a physically appropriate measurement boundary, checks on units and uncertainty, and one genuinely differentiating field test. Numerical precision alone does not strengthen an unsupported hydrologic interpretation.

## Integrated laboratory: Design a complete observational research program with falsifiable outcomes.

**Research task.** An independent study team evaluating whether restoration improved river and groundwater outcomes Start from the attached `datasets/unit-08-synthetic.csv`. The records are deliberately fictional and provide no local environmental observations. The learner's deliverable is a short technical notebook, a table of measurements and conversions, a controlled comparison between two interpretations, and a one-page statement of residual uncertainty.

**Phase A — conceptual diagram.** A reproducible study preserves raw files, time zones, site identifiers, processing scripts, versions, decisions and exclusion rules. Separate model training periods from independent validation periods before reporting forecast skill. Each observation has a spatial footprint; annotate which terms would require a point sample, area-average estimate or volumetric balance. For groundwater, show screened intervals and vertical datum. For rivers, mark the measurement section and route. For water chemistry, identify concentration, flow and analyte units. A diagram that omits the boundary often hides the missing flux that later produces an apparently anomalous numerical result.

**Phase B — independent calculation.** Excellent fit at one monitoring station might conceal unequal errors upstream or during peak flow. Compare multiple objectives, including flow volume, timing, groundwater head and data coverage. Use at least two independent calculation approaches where possible. Compare the result against a sanity bound: storage cannot be below a declared physically admissible minimum, chemical mixing fractions should lie between zero and one under the assumed ideal endmembers, and a probability cannot exceed unity. Round only after combining inputs; retain raw values and intermediate results in a reproducible notebook.

**Phase C — evaluate the alternative.** A counterfactual is what would likely have happened without the intervention; controls, paired basins or interrupted-series designs can help, but require explicit parallel-trend and confounding assumptions. Replace one assumption at a time. Include a small scenario table showing baseline, lower plausible input and upper plausible input, then a separate table for structural alternatives where equations themselves differ. Explain whether the compared outcomes cross a chosen decision threshold. If no real-world decision threshold has been justified, label the result descriptive only rather than declaring a policy winner.

**Phase D — submit a traceable report.** Include the following in one coherent narrative: (a) research question and ethical scope, (b) boundary and major water or solute pathways, (c) original invented records, (d) exact equation and dimensional checks, (e) rival mechanisms and discriminating observations, (f) sensitivity or uncertainty table, and (g) a short conclusion distinguishing the measurement from its interpretation. State why the data cannot justify a real-world site decision.

### Unit synthesis

Every lesson above contributes a different constraint to the integrated investigation. Cross-check a mass balance against a physically plausible flow path; cross-check a statistical summary against a documented measurement interval; and cross-check a model-derived conclusion against an independent observation wherever feasible. Report what evidence would overturn the preferred conclusion. The appropriate scientific endpoint is not a graph that looks convincing, but an interpretation that remains defensible when another researcher can inspect its data, assumptions and alternatives.
