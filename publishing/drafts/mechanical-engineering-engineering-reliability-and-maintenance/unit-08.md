# Unit 08: Integrated Asset Reliability Cases and Decision Reporting

**Course Code**: ERM 408 · **Level**: Advanced Undergraduate Engineering

## Unit Overview & Physical Foundations

This comprehensive university textbook unit covers the theoretical framework, physical modeling, mathematical governing equations, and engineering applications of **Integrated Asset Reliability Cases and Decision Reporting**.

# Unit 08 · Lesson 01 — Centrifugal pump reliability case

**Learning goal.** Explain the core engineering statement, calculate a clearly bounded example, challenge at least one assumption and propose a measurable action. This material is an educational draft, not an authority for equipment acceptance.

## 1. Concept and technical meaning

Centrifugal pump loss of flow can arise from cavitation, suction blockage, wear-ring clearance, seal leakage, bearing damage, motor issues or instrumentation error. Diagnose from head-flow measurements, suction conditions and observed damage, not one vibration number. Reliability intervention can be as simple as correcting operating point.

The useful starting question is **“What physical or service event am I modeling?”** Place the studied item within the unit's central objective: The final engineering decision combines functional requirements, data uncertainty, dependency modeling, physical failure mechanisms, maintainability, safety and lifecycle costs. Good reports make alternative actions explicit and specify which evidence would change the preferred choice. A numerical value only becomes an engineering claim when the mission duration, operating conditions, item state and decision boundary are specified. If the equipment is repaired between events, decide whether the model starts a new life or continues to represent accumulated degradation. When data are drawn from multiple installations, check whether load, age, ambient environment and maintenance practice are comparable.

### Distinguish data from decisions

A probability is an input to a decision rather than a decision by itself. Two alternatives with equal failure probability can lead to different responses when consequences, restoration time and regulatory obligations are different.

A professional worksheet for **centrifugal pump reliability case** should preserve the original event definition and the raw denominator used in the calculation. Build a simple diagram that traces the studied input to a measured output. Label its arrows as measured relationships, physical assumptions or hypothetical causal mechanisms. This keeps the numerical calculation from silently becoming proof of a mechanism that has not been investigated.

## 2. Governing relation and derivation checks

**Primary relation:** `Hydraulic power P_h=ρgQH; shaft power P_s≈P_h/η for pump efficiency η, within defined system boundaries.`

The relation should first be read in words and translated into a dimensional statement. Identify which quantities are probabilities, time or cycle measures, rates, costs, loads, engineering scores or empirical indicators. If an input is a probability, its feasible interval is from zero to one; if it is an event intensity, it must be nonnegative and accompanied by a unit such as failures per operating hour. The output should be interpreted at the same stated boundary and over the same mission or reporting period as its inputs.

**Reasoning sequence.** (i) Define the asset and the function; (ii) write all inputs and their units; (iii) choose the simplest physically defensible model; (iv) perform the computation using an independent check; (v) compare the result with limiting cases; (vi) state uncertainty and model boundaries before recommending maintenance. For example, the limit of a no-failure event probability as an assumed event rate approaches zero should be consistent with ordinary experience. A result outside its physically possible range suggests either an arithmetic fault, incompatible units or a model used outside its assumptions.

**Worked engineering example.** For water at 1,000 kg/m³, Q=0.02 m³/s and H=30 m, hydraulic power≈5.886 kW; at efficiency 0.7, shaft demand≈8.409 kW. Loss of efficiency may raise motor thermal stress.

After evaluating the arithmetic, report what the result means and—equally important—what it does not mean. Distinguish a hypothetical prediction from a measured population statistic. If a numerical example uses a notional fleet or synthetic data, it must not appear in an operator's work package as a measured site result. For any policy comparison, repeat the calculation using at least two plausible ranges for its most uncertain input and report whether the choice changes.

### Make uncertainty actionable

The practical response to missing information is usually a low-cost measurement, a conservative bound or a controlled trial. Sensitivity analysis exposes which uncertain assumption is capable of reversing a recommendation.

## 3. Where the model can fail

A pump can remain mechanically intact but operate off-design because the system curve changed; replacing bearings cannot fix an undersized suction line.

An important diagnostic practice is to seek evidence against the simplest explanation. A repair which temporarily restores output can disguise an uncorrected design, installation or operating error. If the apparent rate improves after a maintenance change, normalize against exposure and examine whether production load, weather, equipment population or reporting conventions changed in the same period. Correlation between a signal and a failure does not establish that intervening on the signal will prevent the failure.

The operational consequence of a bad assumption depends on the equipment. For an ordinary production asset it may mean excess inventory or a costly breakdown. For a safety-critical plant it can mean loss of containment, personnel exposure, service failure or violation of required inspection obligations. Use the teaching result only for understanding; site-specific decisions need competent hazard review, current standards, supplier instructions, physical verification and appropriate approval.

### Define the denominator

Write down the reference population and the interval across which the observation has meaning. An event per machine-day differs from an event per operating hour if production schedules differ. A simulation that silently uses an assumed denominator produces a neat but potentially false comparison.

## 4. Engineering investigation: from model to evidence

**Field prompt.** Create a failure log linking flow, head, current, vibration and seal condition to maintenance recommendations.

Connect this task to the unit study: A food-processing refrigeration plant has chronic unplanned stops. A compressor overhaul, additional standby unit and improved lubrication monitoring may have different effects on frequency, duration and consequence. One option may improve availability while another mainly reduces catastrophic risk. The expected notebook output is concrete: Deliver a board-ready reliability improvement proposal, with assumptions, sensitivity, safety boundaries, monitoring and staged implementation. Include a sketch, a table of unknowns and an explicit statement of what observation would reverse the initial hypothesis. A useful investigation records the condition before repair, retains component photographs when safe, notes firmware and calibration versions where relevant, and documents any temporary bypass. Explain how the conclusion would be independently reproduced by another analyst.

**Proposed procedure.** First obtain permission and confirm the relevant safe isolation and operating boundaries; never open energized or pressurized equipment for a classroom exercise. Second use a published sampling interval or an explicit study protocol. Third capture raw data with units, timestamps and event codes before cleaning or filtering them. Fourth run a simple hand calculation and cross-check it with a separate implementation. Fifth evaluate sensitivity to one omitted mechanism, one measurement bias and one uncertain input. Sixth record the proposed action, owner, estimated restoration impact and a verification measure that will be checked after implementation.

A reliable result can be modest. It may show that two alternatives cannot yet be distinguished, that a missing event time prevents statistical estimation or that extra inspection has poor coverage. Reporting these limitations is preferable to manufacturing precision. For plant-level application, specify which person may authorize a shutdown, restart or alteration of protection logic; a textbook exercise never supplies that authorization.

## 5. Exercises and instructor checkpoints

1. **Definitions.** Define the physical or functional event involved in **centrifugal pump reliability case**. Give its observable boundary and one alternative definition that would change the counted population.
2. **Quantification.** Use the relation `Hydraulic power P_h=ρgQH; shaft power P_s≈P_h/η for pump efficiency η, within defined system boundaries.` with a consistent assumed dataset of your own. Show all units and at least one limiting-case check.
3. **Sensitivity.** Change the most uncertain nonzero input by ±20% where physically meaningful. Compare the output and decide whether the maintenance choice is robust.
4. **Counterexample.** Explain precisely why the following limitation matters: A pump can remain mechanically intact but operate off-design because the system curve changed; replacing bearings cannot fix an undersized suction line.
5. **Application.** Create a failure log linking flow, head, current, vibration and seal condition to maintenance recommendations. Supply an evidence table with at least three observations and mark each entry as measured, supplied by a source, or synthetic.

**Self-check guidance.** A correct response identifies the function, model, assumptions, arithmetic, consequence and plausible falsification. The numeric exercise should be reproducible from the student's displayed inputs. The sensitivity response should not silently vary an independent parameter if two inputs are physically coupled. The field task should end with an evidence request or a testable action rather than a generic recommendation to “do maintenance.”

## 6. Connections to the wider curriculum

This topic interacts with earlier units through lifetime probability, state restoration, operating mechanisms and cost. When proposing a spare or a maintenance interval, ask how it changes both the frequency of failures and the length of lost service. When proposing a sensor, ask how often it produces a useful warning and how the organization responds. An effective recommendation uses the smallest set of credible assumptions needed for the stated decision and explains the circumstances under which its simplified formula would stop being useful.

**Source-reading exercise.** Compare the language of your model with the NIST reliability handbook or the NASA reliability-centered maintenance material listed in the references. Do not reproduce external texts; use the primary source to check the meaning of the statistical term or maintenance method, then describe the limitation in your own words.


---

# Unit 08 · Lesson 02 — Bearings, gears and transmission case

**Learning goal.** Explain the core engineering statement, calculate a clearly bounded example, challenge at least one assumption and propose a measurable action. This material is an educational draft, not an authority for equipment acceptance.

## 1. Concept and technical meaning

Bearing and gear degradation are influenced by lubrication film, contamination, load alignment, surface fatigue and thermal conditions. Diagnostic patterns depend on geometry and speed. Successful maintenance means eliminating the damaging exposure, not simply replacing a damaged bearing.

The useful starting question is **“What physical or service event am I modeling?”** Place the studied item within the unit's central objective: The final engineering decision combines functional requirements, data uncertainty, dependency modeling, physical failure mechanisms, maintainability, safety and lifecycle costs. Good reports make alternative actions explicit and specify which evidence would change the preferred choice. A numerical value only becomes an engineering claim when the mission duration, operating conditions, item state and decision boundary are specified. If the equipment is repaired between events, decide whether the model starts a new life or continues to represent accumulated degradation. When data are drawn from multiple installations, check whether load, age, ambient environment and maintenance practice are comparable.

### Audit model assumptions

Every model has a region in which its assumptions make sense. Before using an equation in a recommendation, check units, boundary, independence assumptions, the way failures are counted, and whether repair changes the modeled population.

A professional worksheet for **bearings, gears and transmission case** should preserve the original event definition and the raw denominator used in the calculation. Build a simple diagram that traces the studied input to a measured output. Label its arrows as measured relationships, physical assumptions or hypothetical causal mechanisms. This keeps the numerical calculation from silently becoming proof of a mechanism that has not been investigated.

## 2. Governing relation and derivation checks

**Primary relation:** `Basic rating life for rolling bearings can be represented by L10=(C/P)^p in million revolutions under specified rating assumptions.`

The relation should first be read in words and translated into a dimensional statement. Identify which quantities are probabilities, time or cycle measures, rates, costs, loads, engineering scores or empirical indicators. If an input is a probability, its feasible interval is from zero to one; if it is an event intensity, it must be nonnegative and accompanied by a unit such as failures per operating hour. The output should be interpreted at the same stated boundary and over the same mission or reporting period as its inputs.

**Reasoning sequence.** (i) Define the asset and the function; (ii) write all inputs and their units; (iii) choose the simplest physically defensible model; (iv) perform the computation using an independent check; (v) compare the result with limiting cases; (vi) state uncertainty and model boundaries before recommending maintenance. For example, the limit of a no-failure event probability as an assumed event rate approaches zero should be consistent with ordinary experience. A result outside its physically possible range suggests either an arithmetic fault, incompatible units or a model used outside its assumptions.

**Worked engineering example.** For ball bearings p=3 and a load doubling, the ideal basic rating life ratio is (1/2)^3=1/8, other factors held fixed; real service life can differ substantially.

After evaluating the arithmetic, report what the result means and—equally important—what it does not mean. Distinguish a hypothetical prediction from a measured population statistic. If a numerical example uses a notional fleet or synthetic data, it must not appear in an operator's work package as a measured site result. For any policy comparison, repeat the calculation using at least two plausible ranges for its most uncertain input and report whether the choice changes.

### Plan a falsification test

A good explanation can be disproved. State an observation that would contradict the proposed failure mechanism, and arrange measurements so another engineer could reach an independent conclusion rather than merely agreeing with the initial diagnosis.

## 3. Where the model can fail

Do not apply rated bearing equations to heavily contaminated installations without appropriate life modifications and manufacturer guidance.

An important diagnostic practice is to seek evidence against the simplest explanation. A repair which temporarily restores output can disguise an uncorrected design, installation or operating error. If the apparent rate improves after a maintenance change, normalize against exposure and examine whether production load, weather, equipment population or reporting conventions changed in the same period. Correlation between a signal and a failure does not establish that intervening on the signal will prevent the failure.

The operational consequence of a bad assumption depends on the equipment. For an ordinary production asset it may mean excess inventory or a costly breakdown. For a safety-critical plant it can mean loss of containment, personnel exposure, service failure or violation of required inspection obligations. Use the teaching result only for understanding; site-specific decisions need competent hazard review, current standards, supplier instructions, physical verification and appropriate approval.

### Keep the physical mechanism visible

An apparent trend in a chart is evidence about recorded variables, not automatically the explanation of a component failure. Ask which loads, contamination pathways, temperatures, controls, maintenance practices or environmental stresses could produce the observed pattern.

## 4. Engineering investigation: from model to evidence

**Field prompt.** Investigate a gearbox bearing with spalling: inspect lubricant, alignment, load record, shaft fits and installation practice.

Connect this task to the unit study: Prepare an engineering business case for a mixed asset portfolio of pumps, bearings, compressors and HVAC equipment. Use synthetic data only and distinguish financial outcomes from risk-control obligations. The expected notebook output is concrete: Deliver a board-ready reliability improvement proposal, with assumptions, sensitivity, safety boundaries, monitoring and staged implementation. Include a sketch, a table of unknowns and an explicit statement of what observation would reverse the initial hypothesis. A useful investigation records the condition before repair, retains component photographs when safe, notes firmware and calibration versions where relevant, and documents any temporary bypass. Explain how the conclusion would be independently reproduced by another analyst.

**Proposed procedure.** First obtain permission and confirm the relevant safe isolation and operating boundaries; never open energized or pressurized equipment for a classroom exercise. Second use a published sampling interval or an explicit study protocol. Third capture raw data with units, timestamps and event codes before cleaning or filtering them. Fourth run a simple hand calculation and cross-check it with a separate implementation. Fifth evaluate sensitivity to one omitted mechanism, one measurement bias and one uncertain input. Sixth record the proposed action, owner, estimated restoration impact and a verification measure that will be checked after implementation.

A reliable result can be modest. It may show that two alternatives cannot yet be distinguished, that a missing event time prevents statistical estimation or that extra inspection has poor coverage. Reporting these limitations is preferable to manufacturing precision. For plant-level application, specify which person may authorize a shutdown, restart or alteration of protection logic; a textbook exercise never supplies that authorization.

## 5. Exercises and instructor checkpoints

1. **Definitions.** Define the physical or functional event involved in **bearings, gears and transmission case**. Give its observable boundary and one alternative definition that would change the counted population.
2. **Quantification.** Use the relation `Basic rating life for rolling bearings can be represented by L10=(C/P)^p in million revolutions under specified rating assumptions.` with a consistent assumed dataset of your own. Show all units and at least one limiting-case check.
3. **Sensitivity.** Change the most uncertain nonzero input by ±20% where physically meaningful. Compare the output and decide whether the maintenance choice is robust.
4. **Counterexample.** Explain precisely why the following limitation matters: Do not apply rated bearing equations to heavily contaminated installations without appropriate life modifications and manufacturer guidance.
5. **Application.** Investigate a gearbox bearing with spalling: inspect lubricant, alignment, load record, shaft fits and installation practice. Supply an evidence table with at least three observations and mark each entry as measured, supplied by a source, or synthetic.

**Self-check guidance.** A correct response identifies the function, model, assumptions, arithmetic, consequence and plausible falsification. The numeric exercise should be reproducible from the student's displayed inputs. The sensitivity response should not silently vary an independent parameter if two inputs are physically coupled. The field task should end with an evidence request or a testable action rather than a generic recommendation to “do maintenance.”

## 6. Connections to the wider curriculum

This topic interacts with earlier units through lifetime probability, state restoration, operating mechanisms and cost. When proposing a spare or a maintenance interval, ask how it changes both the frequency of failures and the length of lost service. When proposing a sensor, ask how often it produces a useful warning and how the organization responds. An effective recommendation uses the smallest set of credible assumptions needed for the stated decision and explains the circumstances under which its simplified formula would stop being useful.

**Source-reading exercise.** Compare the language of your model with the NIST reliability handbook or the NASA reliability-centered maintenance material listed in the references. Do not reproduce external texts; use the primary source to check the meaning of the statistical term or maintenance method, then describe the limitation in your own words.


---

# Unit 08 · Lesson 03 — Boilers and pressure equipment case

**Learning goal.** Explain the core engineering statement, calculate a clearly bounded example, challenge at least one assumption and propose a measurable action. This material is an educational draft, not an authority for equipment acceptance.

## 1. Concept and technical meaning

High-pressure thermal plant reliability must incorporate pressure integrity, water chemistry, feedwater systems, control interlocks, relief devices and human procedures. Scale and deposits degrade heat transfer; corrosion and fatigue can threaten containment. Classroom risk models cannot replace legal inspection programs.

The useful starting question is **“What physical or service event am I modeling?”** Place the studied item within the unit's central objective: The final engineering decision combines functional requirements, data uncertainty, dependency modeling, physical failure mechanisms, maintainability, safety and lifecycle costs. Good reports make alternative actions explicit and specify which evidence would change the preferred choice. A numerical value only becomes an engineering claim when the mission duration, operating conditions, item state and decision boundary are specified. If the equipment is repaired between events, decide whether the model starts a new life or continues to represent accumulated degradation. When data are drawn from multiple installations, check whether load, age, ambient environment and maintenance practice are comparable.

### Keep the operational objective in view

A metric is useful when it changes a decision that helps deliver service. Additional data collection should therefore answer a concrete question: whether to inspect, redesign, change stocking policy, add monitoring or accept an explicitly bounded residual risk.

A professional worksheet for **boilers and pressure equipment case** should preserve the original event definition and the raw denominator used in the calculation. Build a simple diagram that traces the studied input to a measured output. Label its arrows as measured relationships, physical assumptions or hypothetical causal mechanisms. This keeps the numerical calculation from silently becoming proof of a mechanism that has not been investigated.

## 2. Governing relation and derivation checks

**Primary relation:** `Thermal balance Qdot≈mdot(h_out-h_in) for a defined steady flow path, with sign and units consistent.`

The relation should first be read in words and translated into a dimensional statement. Identify which quantities are probabilities, time or cycle measures, rates, costs, loads, engineering scores or empirical indicators. If an input is a probability, its feasible interval is from zero to one; if it is an event intensity, it must be nonnegative and accompanied by a unit such as failures per operating hour. The output should be interpreted at the same stated boundary and over the same mission or reporting period as its inputs.

**Reasoning sequence.** (i) Define the asset and the function; (ii) write all inputs and their units; (iii) choose the simplest physically defensible model; (iv) perform the computation using an independent check; (v) compare the result with limiting cases; (vi) state uncertainty and model boundaries before recommending maintenance. For example, the limit of a no-failure event probability as an assumed event rate approaches zero should be consistent with ordinary experience. A result outside its physically possible range suggests either an arithmetic fault, incompatible units or a model used outside its assumptions.

**Worked engineering example.** A boiler feedwater enthalpy rise of 2,000 kJ/kg at 1.5 kg/s implies 3,000 kW transferred to the water under the simplified steady balance.

After evaluating the arithmetic, report what the result means and—equally important—what it does not mean. Distinguish a hypothetical prediction from a measured population statistic. If a numerical example uses a notional fleet or synthetic data, it must not appear in an operator's work package as a measured site result. For any policy comparison, repeat the calculation using at least two plausible ranges for its most uncertain input and report whether the choice changes.

### Define the denominator

Write down the reference population and the interval across which the observation has meaning. An event per machine-day differs from an event per operating hour if production schedules differ. A simulation that silently uses an assumed denominator produces a neat but potentially false comparison.

## 3. Where the model can fail

High output does not prove safe tube temperature or acceptable pressure integrity; water chemistry and local heat flux must still be assessed.

An important diagnostic practice is to seek evidence against the simplest explanation. A repair which temporarily restores output can disguise an uncorrected design, installation or operating error. If the apparent rate improves after a maintenance change, normalize against exposure and examine whether production load, weather, equipment population or reporting conventions changed in the same period. Correlation between a signal and a failure does not establish that intervening on the signal will prevent the failure.

The operational consequence of a bad assumption depends on the equipment. For an ordinary production asset it may mean excess inventory or a costly breakdown. For a safety-critical plant it can mean loss of containment, personnel exposure, service failure or violation of required inspection obligations. Use the teaching result only for understanding; site-specific decisions need competent hazard review, current standards, supplier instructions, physical verification and appropriate approval.

### Separate requirement from measurement

An engineer should be able to state the acceptance requirement before seeing the measurement. Otherwise thresholds tend to move after results are known. Preserve the original requirement, report any exception and obtain authorized approval for changes.

## 4. Engineering investigation: from model to evidence

**Field prompt.** Construct a boundary and maintenance review for water treatment, feed pumps, safety interlocks and integrity inspections.

Connect this task to the unit study: Prepare an engineering business case for a mixed asset portfolio of pumps, bearings, compressors and HVAC equipment. Use synthetic data only and distinguish financial outcomes from risk-control obligations. The expected notebook output is concrete: Deliver a board-ready reliability improvement proposal, with assumptions, sensitivity, safety boundaries, monitoring and staged implementation. Include a sketch, a table of unknowns and an explicit statement of what observation would reverse the initial hypothesis. A useful investigation records the condition before repair, retains component photographs when safe, notes firmware and calibration versions where relevant, and documents any temporary bypass. Explain how the conclusion would be independently reproduced by another analyst.

**Proposed procedure.** First obtain permission and confirm the relevant safe isolation and operating boundaries; never open energized or pressurized equipment for a classroom exercise. Second use a published sampling interval or an explicit study protocol. Third capture raw data with units, timestamps and event codes before cleaning or filtering them. Fourth run a simple hand calculation and cross-check it with a separate implementation. Fifth evaluate sensitivity to one omitted mechanism, one measurement bias and one uncertain input. Sixth record the proposed action, owner, estimated restoration impact and a verification measure that will be checked after implementation.

A reliable result can be modest. It may show that two alternatives cannot yet be distinguished, that a missing event time prevents statistical estimation or that extra inspection has poor coverage. Reporting these limitations is preferable to manufacturing precision. For plant-level application, specify which person may authorize a shutdown, restart or alteration of protection logic; a textbook exercise never supplies that authorization.

## 5. Exercises and instructor checkpoints

1. **Definitions.** Define the physical or functional event involved in **boilers and pressure equipment case**. Give its observable boundary and one alternative definition that would change the counted population.
2. **Quantification.** Use the relation `Thermal balance Qdot≈mdot(h_out-h_in) for a defined steady flow path, with sign and units consistent.` with a consistent assumed dataset of your own. Show all units and at least one limiting-case check.
3. **Sensitivity.** Change the most uncertain nonzero input by ±20% where physically meaningful. Compare the output and decide whether the maintenance choice is robust.
4. **Counterexample.** Explain precisely why the following limitation matters: High output does not prove safe tube temperature or acceptable pressure integrity; water chemistry and local heat flux must still be assessed.
5. **Application.** Construct a boundary and maintenance review for water treatment, feed pumps, safety interlocks and integrity inspections. Supply an evidence table with at least three observations and mark each entry as measured, supplied by a source, or synthetic.

**Self-check guidance.** A correct response identifies the function, model, assumptions, arithmetic, consequence and plausible falsification. The numeric exercise should be reproducible from the student's displayed inputs. The sensitivity response should not silently vary an independent parameter if two inputs are physically coupled. The field task should end with an evidence request or a testable action rather than a generic recommendation to “do maintenance.”

## 6. Connections to the wider curriculum

This topic interacts with earlier units through lifetime probability, state restoration, operating mechanisms and cost. When proposing a spare or a maintenance interval, ask how it changes both the frequency of failures and the length of lost service. When proposing a sensor, ask how often it produces a useful warning and how the organization responds. An effective recommendation uses the smallest set of credible assumptions needed for the stated decision and explains the circumstances under which its simplified formula would stop being useful.

**Source-reading exercise.** Compare the language of your model with the NIST reliability handbook or the NASA reliability-centered maintenance material listed in the references. Do not reproduce external texts; use the primary source to check the meaning of the statistical term or maintenance method, then describe the limitation in your own words.


---

# Unit 08 · Lesson 04 — Facilities, HVAC and fleet reliability case

**Learning goal.** Explain the core engineering statement, calculate a clearly bounded example, challenge at least one assumption and propose a measurable action. This material is an educational draft, not an authority for equipment acceptance.

## 1. Concept and technical meaning

Facility and fleet equipment operate across different duty cycles and service consequences. HVAC fault detection can focus on airflow, coil fouling, filters, condensate control and compressor cycling; fleets add route, driver and environment variability. Comparisons should normalize exposure and avoid reward systems that suppress honest reporting.

The useful starting question is **“What physical or service event am I modeling?”** Place the studied item within the unit's central objective: The final engineering decision combines functional requirements, data uncertainty, dependency modeling, physical failure mechanisms, maintainability, safety and lifecycle costs. Good reports make alternative actions explicit and specify which evidence would change the preferred choice. A numerical value only becomes an engineering claim when the mission duration, operating conditions, item state and decision boundary are specified. If the equipment is repaired between events, decide whether the model starts a new life or continues to represent accumulated degradation. When data are drawn from multiple installations, check whether load, age, ambient environment and maintenance practice are comparable.

### Make uncertainty actionable

The practical response to missing information is usually a low-cost measurement, a conservative bound or a controlled trial. Sensitivity analysis exposes which uncertain assumption is capable of reversing a recommendation.

A professional worksheet for **facilities, hvac and fleet reliability case** should preserve the original event definition and the raw denominator used in the calculation. Build a simple diagram that traces the studied input to a measured output. Label its arrows as measured relationships, physical assumptions or hypothetical causal mechanisms. This keeps the numerical calculation from silently becoming proof of a mechanism that has not been investigated.

## 2. Governing relation and derivation checks

**Primary relation:** `For a simple repairable portfolio, service availability=total demanded service time fulfilled/total demanded service time, with demand definition published.`

The relation should first be read in words and translated into a dimensional statement. Identify which quantities are probabilities, time or cycle measures, rates, costs, loads, engineering scores or empirical indicators. If an input is a probability, its feasible interval is from zero to one; if it is an event intensity, it must be nonnegative and accompanied by a unit such as failures per operating hour. The output should be interpreted at the same stated boundary and over the same mission or reporting period as its inputs.

**Reasoning sequence.** (i) Define the asset and the function; (ii) write all inputs and their units; (iii) choose the simplest physically defensible model; (iv) perform the computation using an independent check; (v) compare the result with limiting cases; (vi) state uncertainty and model boundaries before recommending maintenance. For example, the limit of a no-failure event probability as an assumed event rate approaches zero should be consistent with ordinary experience. A result outside its physically possible range suggests either an arithmetic fault, incompatible units or a model used outside its assumptions.

**Worked engineering example.** Two air handlers each have high mechanical uptime but fail to maintain indoor comfort during peak demand. A service-level metric captures this functional failure while a simple running-hours metric may not.

After evaluating the arithmetic, report what the result means and—equally important—what it does not mean. Distinguish a hypothetical prediction from a measured population statistic. If a numerical example uses a notional fleet or synthetic data, it must not appear in an operator's work package as a measured site result. For any policy comparison, repeat the calculation using at least two plausible ranges for its most uncertain input and report whether the choice changes.

### Keep the physical mechanism visible

An apparent trend in a chart is evidence about recorded variables, not automatically the explanation of a component failure. Ask which loads, contamination pathways, temperatures, controls, maintenance practices or environmental stresses could produce the observed pattern.

## 3. Where the model can fail

Seasonal loads and preventive shutdown windows complicate benchmarking; a failure count divided by calendar months can penalize the most-used asset.

An important diagnostic practice is to seek evidence against the simplest explanation. A repair which temporarily restores output can disguise an uncorrected design, installation or operating error. If the apparent rate improves after a maintenance change, normalize against exposure and examine whether production load, weather, equipment population or reporting conventions changed in the same period. Correlation between a signal and a failure does not establish that intervening on the signal will prevent the failure.

The operational consequence of a bad assumption depends on the equipment. For an ordinary production asset it may mean excess inventory or a costly breakdown. For a safety-critical plant it can mean loss of containment, personnel exposure, service failure or violation of required inspection obligations. Use the teaching result only for understanding; site-specific decisions need competent hazard review, current standards, supplier instructions, physical verification and appropriate approval.

### Distinguish data from decisions

A probability is an input to a decision rather than a decision by itself. Two alternatives with equal failure probability can lead to different responses when consequences, restoration time and regulatory obligations are different.

## 4. Engineering investigation: from model to evidence

**Field prompt.** Design a reliability dashboard for four assets with distinct demand calendars and a common transparent consequence scale.

Connect this task to the unit study: A food-processing refrigeration plant has chronic unplanned stops. A compressor overhaul, additional standby unit and improved lubrication monitoring may have different effects on frequency, duration and consequence. One option may improve availability while another mainly reduces catastrophic risk. The expected notebook output is concrete: Deliver a board-ready reliability improvement proposal, with assumptions, sensitivity, safety boundaries, monitoring and staged implementation. Include a sketch, a table of unknowns and an explicit statement of what observation would reverse the initial hypothesis. A useful investigation records the condition before repair, retains component photographs when safe, notes firmware and calibration versions where relevant, and documents any temporary bypass. Explain how the conclusion would be independently reproduced by another analyst.

**Proposed procedure.** First obtain permission and confirm the relevant safe isolation and operating boundaries; never open energized or pressurized equipment for a classroom exercise. Second use a published sampling interval or an explicit study protocol. Third capture raw data with units, timestamps and event codes before cleaning or filtering them. Fourth run a simple hand calculation and cross-check it with a separate implementation. Fifth evaluate sensitivity to one omitted mechanism, one measurement bias and one uncertain input. Sixth record the proposed action, owner, estimated restoration impact and a verification measure that will be checked after implementation.

A reliable result can be modest. It may show that two alternatives cannot yet be distinguished, that a missing event time prevents statistical estimation or that extra inspection has poor coverage. Reporting these limitations is preferable to manufacturing precision. For plant-level application, specify which person may authorize a shutdown, restart or alteration of protection logic; a textbook exercise never supplies that authorization.

## 5. Exercises and instructor checkpoints

1. **Definitions.** Define the physical or functional event involved in **facilities, hvac and fleet reliability case**. Give its observable boundary and one alternative definition that would change the counted population.
2. **Quantification.** Use the relation `For a simple repairable portfolio, service availability=total demanded service time fulfilled/total demanded service time, with demand definition published.` with a consistent assumed dataset of your own. Show all units and at least one limiting-case check.
3. **Sensitivity.** Change the most uncertain nonzero input by ±20% where physically meaningful. Compare the output and decide whether the maintenance choice is robust.
4. **Counterexample.** Explain precisely why the following limitation matters: Seasonal loads and preventive shutdown windows complicate benchmarking; a failure count divided by calendar months can penalize the most-used asset.
5. **Application.** Design a reliability dashboard for four assets with distinct demand calendars and a common transparent consequence scale. Supply an evidence table with at least three observations and mark each entry as measured, supplied by a source, or synthetic.

**Self-check guidance.** A correct response identifies the function, model, assumptions, arithmetic, consequence and plausible falsification. The numeric exercise should be reproducible from the student's displayed inputs. The sensitivity response should not silently vary an independent parameter if two inputs are physically coupled. The field task should end with an evidence request or a testable action rather than a generic recommendation to “do maintenance.”

## 6. Connections to the wider curriculum

This topic interacts with earlier units through lifetime probability, state restoration, operating mechanisms and cost. When proposing a spare or a maintenance interval, ask how it changes both the frequency of failures and the length of lost service. When proposing a sensor, ask how often it produces a useful warning and how the organization responds. An effective recommendation uses the smallest set of credible assumptions needed for the stated decision and explains the circumstances under which its simplified formula would stop being useful.

**Source-reading exercise.** Compare the language of your model with the NIST reliability handbook or the NASA reliability-centered maintenance material listed in the references. Do not reproduce external texts; use the primary source to check the meaning of the statistical term or maintenance method, then describe the limitation in your own words.


---

# Unit 08 · Lesson 05 — Integrated reliability engineering decision

**Learning goal.** Explain the core engineering statement, calculate a clearly bounded example, challenge at least one assumption and propose a measurable action. This material is an educational draft, not an authority for equipment acceptance.

## 1. Concept and technical meaning

A final proposal must start with what the customer needs, show what is known, identify the assumptions, compare technically feasible controls, and name what will be measured after implementation. Use multiple evidence types: field event history, failure analysis, simple probability models, economic scenarios and independent safety review.

The useful starting question is **“What physical or service event am I modeling?”** Place the studied item within the unit's central objective: The final engineering decision combines functional requirements, data uncertainty, dependency modeling, physical failure mechanisms, maintainability, safety and lifecycle costs. Good reports make alternative actions explicit and specify which evidence would change the preferred choice. A numerical value only becomes an engineering claim when the mission duration, operating conditions, item state and decision boundary are specified. If the equipment is repaired between events, decide whether the model starts a new life or continues to represent accumulated degradation. When data are drawn from multiple installations, check whether load, age, ambient environment and maintenance practice are comparable.

### Plan a falsification test

A good explanation can be disproved. State an observation that would contradict the proposed failure mechanism, and arrange measurements so another engineer could reach an independent conclusion rather than merely agreeing with the initial diagnosis.

A professional worksheet for **integrated reliability engineering decision** should preserve the original event definition and the raw denominator used in the calculation. Build a simple diagram that traces the studied input to a measured output. Label its arrows as measured relationships, physical assumptions or hypothetical causal mechanisms. This keeps the numerical calculation from silently becoming proof of a mechanism that has not been investigated.

## 2. Governing relation and derivation checks

**Primary relation:** `Decision logic: feasibility and safety constraints first; then compare cost, reliability improvement, maintainability, implementation risk and reversibility.`

The relation should first be read in words and translated into a dimensional statement. Identify which quantities are probabilities, time or cycle measures, rates, costs, loads, engineering scores or empirical indicators. If an input is a probability, its feasible interval is from zero to one; if it is an event intensity, it must be nonnegative and accompanied by a unit such as failures per operating hour. The output should be interpreted at the same stated boundary and over the same mission or reporting period as its inputs.

**Reasoning sequence.** (i) Define the asset and the function; (ii) write all inputs and their units; (iii) choose the simplest physically defensible model; (iv) perform the computation using an independent check; (v) compare the result with limiting cases; (vi) state uncertainty and model boundaries before recommending maintenance. For example, the limit of a no-failure event probability as an assumed event rate approaches zero should be consistent with ordinary experience. A result outside its physically possible range suggests either an arithmetic fault, incompatible units or a model used outside its assumptions.

**Worked engineering example.** A three-asset plant can choose between improving a pump seal design, storing a spare gearbox, and adding a vibration pilot. Data may support different priorities depending on outage consequence and probability of precursor detection.

After evaluating the arithmetic, report what the result means and—equally important—what it does not mean. Distinguish a hypothetical prediction from a measured population statistic. If a numerical example uses a notional fleet or synthetic data, it must not appear in an operator's work package as a measured site result. For any policy comparison, repeat the calculation using at least two plausible ranges for its most uncertain input and report whether the choice changes.

### Separate requirement from measurement

An engineer should be able to state the acceptance requirement before seeing the measurement. Otherwise thresholds tend to move after results are known. Preserve the original requirement, report any exception and obtain authorized approval for changes.

## 3. Where the model can fail

A spreadsheet output is not verification. Every estimate should link to a measurement, documented assumption, standard or explicit sensitivity range.

An important diagnostic practice is to seek evidence against the simplest explanation. A repair which temporarily restores output can disguise an uncorrected design, installation or operating error. If the apparent rate improves after a maintenance change, normalize against exposure and examine whether production load, weather, equipment population or reporting conventions changed in the same period. Correlation between a signal and a failure does not establish that intervening on the signal will prevent the failure.

The operational consequence of a bad assumption depends on the equipment. For an ordinary production asset it may mean excess inventory or a costly breakdown. For a safety-critical plant it can mean loss of containment, personnel exposure, service failure or violation of required inspection obligations. Use the teaching result only for understanding; site-specific decisions need competent hazard review, current standards, supplier instructions, physical verification and appropriate approval.

### Audit model assumptions

Every model has a region in which its assumptions make sense. Before using an equation in a recommendation, check units, boundary, independence assumptions, the way failures are counted, and whether repair changes the modeled population.

## 4. Engineering investigation: from model to evidence

**Field prompt.** Write a 2-page proposal with risk register, leading indicators, owner, deployment gate, stop condition and verification schedule.

Connect this task to the unit study: Prepare an engineering business case for a mixed asset portfolio of pumps, bearings, compressors and HVAC equipment. Use synthetic data only and distinguish financial outcomes from risk-control obligations. The expected notebook output is concrete: Deliver a board-ready reliability improvement proposal, with assumptions, sensitivity, safety boundaries, monitoring and staged implementation. Include a sketch, a table of unknowns and an explicit statement of what observation would reverse the initial hypothesis. A useful investigation records the condition before repair, retains component photographs when safe, notes firmware and calibration versions where relevant, and documents any temporary bypass. Explain how the conclusion would be independently reproduced by another analyst.

**Proposed procedure.** First obtain permission and confirm the relevant safe isolation and operating boundaries; never open energized or pressurized equipment for a classroom exercise. Second use a published sampling interval or an explicit study protocol. Third capture raw data with units, timestamps and event codes before cleaning or filtering them. Fourth run a simple hand calculation and cross-check it with a separate implementation. Fifth evaluate sensitivity to one omitted mechanism, one measurement bias and one uncertain input. Sixth record the proposed action, owner, estimated restoration impact and a verification measure that will be checked after implementation.

A reliable result can be modest. It may show that two alternatives cannot yet be distinguished, that a missing event time prevents statistical estimation or that extra inspection has poor coverage. Reporting these limitations is preferable to manufacturing precision. For plant-level application, specify which person may authorize a shutdown, restart or alteration of protection logic; a textbook exercise never supplies that authorization.

## 5. Exercises and instructor checkpoints

1. **Definitions.** Define the physical or functional event involved in **integrated reliability engineering decision**. Give its observable boundary and one alternative definition that would change the counted population.
2. **Quantification.** Use the relation `Decision logic: feasibility and safety constraints first; then compare cost, reliability improvement, maintainability, implementation risk and reversibility.` with a consistent assumed dataset of your own. Show all units and at least one limiting-case check.
3. **Sensitivity.** Change the most uncertain nonzero input by ±20% where physically meaningful. Compare the output and decide whether the maintenance choice is robust.
4. **Counterexample.** Explain precisely why the following limitation matters: A spreadsheet output is not verification. Every estimate should link to a measurement, documented assumption, standard or explicit sensitivity range.
5. **Application.** Write a 2-page proposal with risk register, leading indicators, owner, deployment gate, stop condition and verification schedule. Supply an evidence table with at least three observations and mark each entry as measured, supplied by a source, or synthetic.

**Self-check guidance.** A correct response identifies the function, model, assumptions, arithmetic, consequence and plausible falsification. The numeric exercise should be reproducible from the student's displayed inputs. The sensitivity response should not silently vary an independent parameter if two inputs are physically coupled. The field task should end with an evidence request or a testable action rather than a generic recommendation to “do maintenance.”

## 6. Connections to the wider curriculum

This topic interacts with earlier units through lifetime probability, state restoration, operating mechanisms and cost. When proposing a spare or a maintenance interval, ask how it changes both the frequency of failures and the length of lost service. When proposing a sensor, ask how often it produces a useful warning and how the organization responds. An effective recommendation uses the smallest set of credible assumptions needed for the stated decision and explains the circumstances under which its simplified formula would stop being useful.

**Source-reading exercise.** Compare the language of your model with the NIST reliability handbook or the NASA reliability-centered maintenance material listed in the references. Do not reproduce external texts; use the primary source to check the meaning of the statistical term or maintenance method, then describe the limitation in your own words.


---

