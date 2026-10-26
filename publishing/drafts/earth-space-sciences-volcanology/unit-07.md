# Unit 7: Monitoring, Data, and Eruption Forecasting

## Central question

**What can observatories infer—and what remains uncertain—from volcanic unrest?**

**Synthetic scenario.** A fictional observatory receives earthquake counts, GNSS positions, gas estimates and satellite thermal observations with missing data and changing instrument baselines. This is an imagined classroom landscape; no measured eruption or real safety recommendation is implied.

## Concepts and study approach

The unit brings together **seismicity, deformation, volcanic gases, remote sensing and probabilistic interpretation**. Physical processes can be reconstructed from deposits, rock composition, geodetic observations or measured signals, but different materials survive and different instruments observe different parts of the system. The same observable feature may arise from distinct combinations of source conditions and later changes. The aim is to identify the evidence most capable of separating interpretations, not merely to attach a name to the most striking landform. The included case measurements and graphs were designed solely for teaching.

**Problem framing.** A fictional observatory receives earthquake counts, GNSS positions, gas estimates and satellite thermal observations with missing data and changing instrument baselines. Imagine that students must present a short technical brief. Before making a numerical model, determine the time span, which observations are independent, and which boundaries are directly mapped rather than estimated. Data may have unequal completeness and calibration. Distinguish an interpretation based on direct field material from one inferred from numerical fitting or a remote sensor. Where the evidence allows more than one answer, explain what added observation would be valuable.

### Lesson 7.1: Volcano seismology

**Learning objective.** Explain the physical reasoning behind volcano seismology, design a suitable observation, evaluate a counterexample, and distinguish classroom arithmetic from an empirical volcanic conclusion.

**Scientific foundation.** Volcano-tectonic earthquakes, long-period signals and tremor can reflect different physical processes but classifications require waveforms, locations and context. The issue is not resolved by knowing a label alone: observations may be indirect, sampled at different scales or altered after the event. A defensible explanation specifies the process, its boundary conditions and a plausible competing mechanism.

**Evidence and method.** Compare synthetic earthquake-rate time series with station geometry and a noise record; distinguish detections from catalog completeness. Define the instrument or mapping method, the measured physical quantity, the sampling interval and the possible biases. State what could be directly checked by another observer, without requiring them to accept your interpretation first.

**Common interpretive trap.** An earthquake swarm is not a deterministic countdown to eruption, and signal names do not uniquely determine magma motion. The corresponding methodological safeguard is to compare observations that should differ between explanations. A failure to collect discriminating data is a limitation, not proof that the working mechanism is right.

#### Mechanisms and competing explanations

A causal model should connect source conditions, transport, transformation and the observable product. The central mechanism is: Volcano-tectonic earthquakes, long-period signals and tremor can reflect different physical processes but classifications require waveforms, locations and context. This description predicts particular textures or signals, yet alternate processes might also produce parts of the same pattern. Use **An earthquake swarm is not a deterministic countdown to eruption, and signal names do not uniquely determine magma motion.** as a test of an attractive but inadequate story. Set out two hypotheses with predictions that diverge at a practical sampling location. Retain the less dramatic hypothesis in the record until some observation actually rules it out; familiarity is not a substitute for comparison.

#### Designing an investigation in practice

An actionable class exercise is: Estimate changes in a toy event count while checking exposure time and detection thresholds. Describe two observations that support the preferred inference and one that would substantially weaken it. Provide a sketch or table with a data dictionary and include both an expected result and a plausible unexpected result. Distinguish data gathered at the same site from independently sampled sites. Even if the teaching exercise is entirely desk-based, include metadata on coordinate systems, measurement precision, instrument or image source, and whether values are synthetic.

#### Competing hypothesis protocol

Begin with three columns: observable feature, explanation A, explanation B. For each column decide whether an observation is expected, merely compatible or contradictory. The exercise should not put a weight of one on every observation: multiple measurements from the same camera, sample or process can be correlated. Where the evidence is ambiguous, propose a new measurement rather than manufacturing a definitive choice. Apply it specifically to **volcano seismology** using the supplied scenario. An effective report should make the observer’s original question visible and keep all artificial data marked as invented.

#### Checked numerical exercise

**Worked case 7.1: Mogi point-source uplift directly above a source offset.** Input = 1.6 million m³; the specified relation is `(0.75*(x*1e6)/Math.PI)*3000/Math.pow(2000*2000+3000*3000,1.5)` with `x` equal to that input. Substitution yields **0.0244477 vertical displacement (m)**. Assumptions and interpretation: Assumes homogeneous elastic half-space, point source, nu=0.25, r=2 km, depth=3 km. Recompute from the given numbers and state why additional digits would not increase physical reliability.

#### Research task and assessment

**Investigation.** Estimate changes in a toy event count while checking exposure time and detection thresholds. Before starting, list the available evidence, feasible controls and at least one alternative explanation. Your product should include a labeled diagram, a small table, a calculation when appropriate, and a short uncertainty paragraph.

**Interpretation check.** Identify the most consequential uncertainty in your conclusion.

### Lesson 7.2: GNSS, tilt and deformation

**Learning objective.** Explain the physical reasoning behind gnss, tilt and deformation, design a suitable observation, evaluate a counterexample, and distinguish classroom arithmetic from an empirical volcanic conclusion.

**Scientific foundation.** Ground movement can reflect pressure changes, dike intrusion, hydrothermal circulation, loading or tectonic motion; models translate displacement into possible subsurface causes. The issue is not resolved by knowing a label alone: observations may be indirect, sampled at different scales or altered after the event. A defensible explanation specifies the process, its boundary conditions and a plausible competing mechanism.

**Evidence and method.** Explore a simplified Mogi-type point-source deformation example and assess how source depth and sensor distance affect results. Define the instrument or mapping method, the measured physical quantity, the sampling interval and the possible biases. State what could be directly checked by another observer, without requiring them to accept your interpretation first.

**Common interpretive trap.** A mathematically good single-source fit can still be non-unique and should be checked against independent data. The corresponding methodological safeguard is to compare observations that should differ between explanations. A failure to collect discriminating data is a limitation, not proof that the working mechanism is right.

#### Measurements and evidence quality in practice

Implement the following discipline-specific measurement plan: Explore a simplified Mogi-type point-source deformation example and assess how source depth and sensor distance affect results. Make sampling and calibration explicit. If an instrument observes several correlated points, avoid reporting them as fully independent replications. Carry the raw data and a record of exclusions into the final analysis. If a signal is close to the detection limit, show an interval or a qualified statement rather than an extra decimal place. Ask whether the same observational conclusion would emerge if the most uncertain record were removed or processed using another defensible method.

#### Interpretation, uncertainty, and safe limits

When presenting a result, separate the observation, the calculation and the implication in three sentences. An output that matches a conceptual model does not necessarily predict a real eruptive event. In this topic, **A mathematically good single-source fit can still be non-unique and should be checked against independent data.** remains an important constraint even when the exercise appears numerically neat. Volcanic hazards affect communities and field researchers; classroom values must never become evacuation zones, thresholds, aircraft routing or claims of safety. The scientific report should end by naming what would have to be independently observed before any consequential application.

#### Mapping protocol

Provide a legend for directly mapped material, interpolated boundaries, inaccessible terrain, and the uncertain direction of transport. Label profiles with a consistent distance scale. When converting between a map and cross-section, note that topographic exaggeration alters the visual impression of slope and thickness. Any real-world hazard map would need expert validation not attempted here. Apply it specifically to **gnss, tilt and deformation** using the supplied scenario. An effective report should make the observer’s original question visible and keep all artificial data marked as invented.

#### Checked numerical exercise

**Worked case 7.2: Convert sulfur dioxide mass flux into daily tons.** Input = 2.9 kg/s; the specified relation is `86.4*x` with `x` equal to that input. Substitution yields **250.56 tons per day**. Assumptions and interpretation: Continuous constant flux assumed; measurement uncertainty and meteorology absent. Recompute from the given numbers and state why additional digits would not increase physical reliability.

#### Research task and assessment

**Investigation.** State what new observations would distinguish broad inflation from localized fault movement. Before starting, list the available evidence, feasible controls and at least one alternative explanation. Your product should include a labeled diagram, a small table, a calculation when appropriate, and a short uncertainty paragraph.

**Interpretation check.** Identify the most consequential uncertainty in your conclusion.

### Lesson 7.3: Gas flux and magma chemistry

**Learning objective.** Explain the physical reasoning behind gas flux and magma chemistry, design a suitable observation, evaluate a counterexample, and distinguish classroom arithmetic from an empirical volcanic conclusion.

**Scientific foundation.** Gas ratios and fluxes sometimes illuminate magma supply and degassing pathways when measurement methods, wind conditions and hydrothermal scrubbing are considered. The issue is not resolved by knowing a label alone: observations may be indirect, sampled at different scales or altered after the event. A defensible explanation specifies the process, its boundary conditions and a plausible competing mechanism.

**Evidence and method.** Examine a hypothetical sulfur dioxide flux sequence with calibration blanks and missing weather observations. Define the instrument or mapping method, the measured physical quantity, the sampling interval and the possible biases. State what could be directly checked by another observer, without requiring them to accept your interpretation first.

**Common interpretive trap.** A decline in measured gas could indicate reduced emissions or blocked pathways; it is not automatically reassuring. The corresponding methodological safeguard is to compare observations that should differ between explanations. A failure to collect discriminating data is a limitation, not proof that the working mechanism is right.

#### Establishing what is observed

Treat the starting point as an observation rather than a conclusion. For **Gas flux and magma chemistry**, describe the feature recorded in a map, sample, time series or laboratory log. A photograph should include scale and orientation, and a quantitative record should state units and detection limits. The next step is to ask whether **Examine a hypothetical sulfur dioxide flux sequence with calibration blanks and missing weather observations.** is directly measured or reconstructed. Where reconstruction is involved, name the underlying assumption instead of hiding it within a figure caption. A later researcher must be able to reverse that assumption without recreating the entire field campaign.

#### Physical scale and boundary conditions

Physical interpretation changes with scale. A hand specimen, a ten-metre outcrop, a volcanic edifice and a satellite pixel do not offer interchangeable constraints on **gas flux and magma chemistry**. State the spatial support of each observation and the time averaging implicit in the selected method. Compare the variables held fixed in the worked exercise with the quantities that vary naturally. If your calculation assumes a homogeneous material or a steady flow, explain which observations could reveal heterogeneity, a discontinuity, or a shift in regime.

#### Time-series protocol

State acquisition times, the local-to-UTC conversion, instrument uptime, rate of sampling and any changes to detection limits. Calculate the effect of one missing observation on a simple mean, then compare this change with any claimed physical trend. Multiple channels may indicate the same phenomenon and should not automatically be interpreted as independent evidence. Apply it specifically to **gas flux and magma chemistry** using the supplied scenario. An effective report should make the observer’s original question visible and keep all artificial data marked as invented.

#### Checked numerical exercise

**Worked case 7.3: Mogi point-source uplift directly above a source offset.** Input = 4.2 million m³; the specified relation is `(0.75*(x*1e6)/Math.PI)*3000/Math.pow(2000*2000+3000*3000,1.5)` with `x` equal to that input. Substitution yields **0.0641752 vertical displacement (m)**. Assumptions and interpretation: Assumes homogeneous elastic half-space, point source, nu=0.25, r=2 km, depth=3 km. Recompute from the given numbers and state why additional digits would not increase physical reliability.

#### Research task and assessment

**Investigation.** Define a reproducible uncertainty budget for plume transects rather than a single 'gas alarm' value. Before starting, list the available evidence, feasible controls and at least one alternative explanation. Your product should include a labeled diagram, a small table, a calculation when appropriate, and a short uncertainty paragraph.

**Interpretation check.** Identify the most consequential uncertainty in your conclusion.

### Lesson 7.4: Satellite and thermal surveillance

**Learning objective.** Explain the physical reasoning behind satellite and thermal surveillance, design a suitable observation, evaluate a counterexample, and distinguish classroom arithmetic from an empirical volcanic conclusion.

**Scientific foundation.** Optical, infrared and radar sensors can show thermal anomalies, surface deformation, ash clouds and plume gases at complementary spatial and temporal scales. The issue is not resolved by knowing a label alone: observations may be indirect, sampled at different scales or altered after the event. A defensible explanation specifies the process, its boundary conditions and a plausible competing mechanism.

**Evidence and method.** Compare daytime optical cloud cover with nighttime infrared detections and InSAR coherence limitations. Define the instrument or mapping method, the measured physical quantity, the sampling interval and the possible biases. State what could be directly checked by another observer, without requiring them to accept your interpretation first.

**Common interpretive trap.** An apparent hotspot may involve sun-heated rock or wildfire; atmospheric and geometric artifacts can mimic a volcanic change. The corresponding methodological safeguard is to compare observations that should differ between explanations. A failure to collect discriminating data is a limitation, not proof that the working mechanism is right.

#### Mechanisms and competing explanations

A causal model should connect source conditions, transport, transformation and the observable product. The central mechanism is: Optical, infrared and radar sensors can show thermal anomalies, surface deformation, ash clouds and plume gases at complementary spatial and temporal scales. This description predicts particular textures or signals, yet alternate processes might also produce parts of the same pattern. Use **An apparent hotspot may involve sun-heated rock or wildfire; atmospheric and geometric artifacts can mimic a volcanic change.** as a test of an attractive but inadequate story. Set out two hypotheses with predictions that diverge at a practical sampling location. Retain the less dramatic hypothesis in the record until some observation actually rules it out; familiarity is not a substitute for comparison.

#### Contradictions worth testing

A scientific explanation is strengthened when it survives serious attempts at falsification. Here, a specific danger is: An apparent hotspot may involve sun-heated rock or wildfire; atmospheric and geometric artifacts can mimic a volcanic change. Write the interpretation that a skeptical colleague would advance from the same field notebook. Then identify what the two explanations predict differently in rock fabric, chemistry, geophysical time series or deposit distribution. Record the proposed test before examining the answer so it cannot be adjusted after the fact. Where more than one hypothesis survives, report that ambiguity instead of choosing the version that tells the most coherent story.

#### Rock and material protocol

Describe texture and components before giving the sample a genetic name. Keep field identification separate from laboratory classification. Distinguish fresh juvenile material, older lithic fragments and secondary alteration where relevant. A classification statement should say what observations are decisive and what additional analysis would be needed to settle ambiguity. Apply it specifically to **satellite and thermal surveillance** using the supplied scenario. An effective report should make the observer’s original question visible and keep all artificial data marked as invented.

#### Checked numerical exercise

**Worked case 7.4: Convert sulfur dioxide mass flux into daily tons.** Input = 5.5 kg/s; the specified relation is `86.4*x` with `x` equal to that input. Substitution yields **475.2 tons per day**. Assumptions and interpretation: Continuous constant flux assumed; measurement uncertainty and meteorology absent. Recompute from the given numbers and state why additional digits would not increase physical reliability.

#### Research task and assessment

**Investigation.** Build a multi-sensor observation table and list which features cannot be resolved from orbit. Before starting, list the available evidence, feasible controls and at least one alternative explanation. Your product should include a labeled diagram, a small table, a calculation when appropriate, and a short uncertainty paragraph.

**Interpretation check.** Identify the most consequential uncertainty in your conclusion.

### Lesson 7.5: Probabilistic forecasts and observatory communication

**Learning objective.** Explain the physical reasoning behind probabilistic forecasts and observatory communication, design a suitable observation, evaluate a counterexample, and distinguish classroom arithmetic from an empirical volcanic conclusion.

**Scientific foundation.** Forecasts combine prior knowledge, monitored evidence, possible eruption pathways and evolving uncertainties; responsible notices communicate states rather than impossible certainty. The issue is not resolved by knowing a label alone: observations may be indirect, sampled at different scales or altered after the event. A defensible explanation specifies the process, its boundary conditions and a plausible competing mechanism.

**Evidence and method.** Compare a fictional event tree with a stated time horizon, definitions and stakeholder consequences, keeping it separate from official alert levels. Define the instrument or mapping method, the measured physical quantity, the sampling interval and the possible biases. State what could be directly checked by another observer, without requiring them to accept your interpretation first.

**Common interpretive trap.** A model's numeric probability is not a substitute for expert interpretation, and national color-code systems are not universal. The corresponding methodological safeguard is to compare observations that should differ between explanations. A failure to collect discriminating data is a limitation, not proof that the working mechanism is right.

#### Measurements and evidence quality in practice

Implement the following discipline-specific measurement plan: Compare a fictional event tree with a stated time horizon, definitions and stakeholder consequences, keeping it separate from official alert levels. Make sampling and calibration explicit. If an instrument observes several correlated points, avoid reporting them as fully independent replications. Carry the raw data and a record of exclusions into the final analysis. If a signal is close to the detection limit, show an interval or a qualified statement rather than an extra decimal place. Ask whether the same observational conclusion would emerge if the most uncertain record were removed or processed using another defensible method.

#### Worked quantitative reasoning in practice

The numerical exercise uses fictional inputs and one declared equation, so it can be recalculated without external data. First determine the measured quantity, units, reference level and temporal averaging interval. Change the model input by a modest fraction and check whether the response is linear, nonlinear or bounded. Be careful not to infer that a good calculator result validates the underlying physics. For **probabilistic forecasts and observatory communication**, numbers support an explanation only when the chosen equation applies to the process, not merely because the units can be made to cancel.

#### Model validation protocol

Write assumptions beside the model, not in a remote appendix. Confirm dimensional consistency and limiting behavior; then evaluate at the smallest, intermediate and largest plausible classroom inputs. Validate arithmetic against an independent calculation. The model remains provisional if there are no external observations that test the mechanism. Apply it specifically to **probabilistic forecasts and observatory communication** using the supplied scenario. An effective report should make the observer’s original question visible and keep all artificial data marked as invented.

#### Checked numerical exercise

**Worked case 7.5: Mogi point-source uplift directly above a source offset.** Input = 6.8 million m³; the specified relation is `(0.75*(x*1e6)/Math.PI)*3000/Math.pow(2000*2000+3000*3000,1.5)` with `x` equal to that input. Substitution yields **0.103903 vertical displacement (m)**. Assumptions and interpretation: Assumes homogeneous elastic half-space, point source, nu=0.25, r=2 km, depth=3 km. Recompute from the given numbers and state why additional digits would not increase physical reliability.

#### Research task and assessment

**Investigation.** Compose a sample advisory that clearly states evidence, uncertainty, timestamp and where to find official updates. Before starting, list the available evidence, feasible controls and at least one alternative explanation. Your product should include a labeled diagram, a small table, a calculation when appropriate, and a short uncertainty paragraph.

**Interpretation check.** Identify the most consequential uncertainty in your conclusion.

## Integrated research studio: Unit 7

**Scenario.** A fictional observatory receives earthquake counts, GNSS positions, gas estimates and satellite thermal observations with missing data and changing instrument baselines. Assemble an evidence ledger with a row for each observation, its provenance, its measured units, and an explicit distinction between original observation and interpreted process. Add a third column for alternative hypotheses. Decide which items could be affected by the same source of error or sampling gap before computing averages, rates or correlations. A synthetic observation should be documented as such both in the file name and in any figure legend, because a decontextualized number can appear real after it is copied into another report.

**Research sequence.** First define a narrowly stated question. Second draw the relevant physical geometry or time axis. Third identify process variables that could be measured independently. Fourth check dimensional consistency of a simple model. Fifth create two alternative explanations and an observation capable of distinguishing them. Sixth record an uncertainty or sensitivity check. Seventh communicate the conclusion in a short paragraph aimed at technically informed readers and in another paragraph suited to nonspecialists, preserving the uncertainty in both.

**Practical assessment.** Use the explicitly synthetic CSV file for this unit to construct a two-panel visualization: one panel shows the fictional input series, and the other shows the result of a transparently specified numerical transformation. Add labeled axes and units; do not connect samples with a line if the observation units are unrelated. Explain whether outliers represent legitimate processes, data errors or unknowns. Describe how results change if the least complete rows are excluded, and archive the transformation steps.

**Scope and responsibility.** The educational concepts here do not generate official volcano warnings, physical access permissions or operational models of lava inundation, ash dispersal or lahar travel. Where a problem resembles an applied hazard calculation, the student must state why it lacks sufficient measurements for public-safety use. Official observatories and civil authorities are responsible for operational interpretations and decisions. For reproducible research, preserve the original dataset, all transformations, software environment information and the model assumptions.

## Simulation review

This unit's two browser models are **Mogi point-source uplift directly above a source offset** and **Convert sulfur dioxide mass flux into daily tons**. Change each slider near its low, middle and high settings. Observe whether the numerical result rises, falls, saturates or changes rapidly. Explain which assumption produces that shape. The plotted curve is a property of its stated function, not an observation of a volcanic system.

