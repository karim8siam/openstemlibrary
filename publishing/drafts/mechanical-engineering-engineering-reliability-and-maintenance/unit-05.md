# Unit 05: Maintenance Strategy and Condition Monitoring

**Course Code**: ERM 405 · **Level**: Advanced Undergraduate Engineering

## Unit Overview & Physical Foundations

This comprehensive university textbook unit covers the theoretical framework, physical modeling, mathematical governing equations, and engineering applications of **Maintenance Strategy and Condition Monitoring**.

# Unit 05 · Lesson 01 — Preventive replacement intervals

**Learning goal.** Explain the core engineering statement, calculate a clearly bounded example, challenge at least one assumption and propose a measurable action. This material is an educational draft, not an authority for equipment acceptance.

## 1. Concept and technical meaning

Age-based replacement can reduce risk for wear-out mechanisms but increases scheduled work and may introduce infant mortality or assembly errors. Optimum interval depends on the entire lifetime distribution, replacement costs and consequences, not only the mean life. A repairable system with minimal repair may need a different model.

The useful starting question is **“What physical or service event am I modeling?”** Place the studied item within the unit's central objective: Preventive replacement, inspection, condition-based intervention, and run-to-failure are economic and risk decisions, not moral labels. Age replacement only makes sense when the failure-time behavior and replacement consequence justify it. Sensor trends become decisions only with baseline, alarm thresholds, false-alarm handling and response plans. A numerical value only becomes an engineering claim when the mission duration, operating conditions, item state and decision boundary are specified. If the equipment is repaired between events, decide whether the model starts a new life or continues to represent accumulated degradation. When data are drawn from multiple installations, check whether load, age, ambient environment and maintenance practice are comparable.

### Audit model assumptions

Every model has a region in which its assumptions make sense. Before using an equation in a recommendation, check units, boundary, independence assumptions, the way failures are counted, and whether repair changes the modeled population.

A professional worksheet for **preventive replacement intervals** should preserve the original event definition and the raw denominator used in the calculation. Build a simple diagram that traces the studied input to a measured output. Label its arrows as measured relationships, physical assumptions or hypothetical causal mechanisms. This keeps the numerical calculation from silently becoming proof of a mechanism that has not been investigated.

## 2. Governing relation and derivation checks

**Primary relation:** `Simplified cost rate for planned replacement at age τ: [C_p R(τ)+C_f(1-R(τ))]/∫_0^τ R(t)dt, assuming renewal at planned or first failure.`

The relation should first be read in words and translated into a dimensional statement. Identify which quantities are probabilities, time or cycle measures, rates, costs, loads, engineering scores or empirical indicators. If an input is a probability, its feasible interval is from zero to one; if it is an event intensity, it must be nonnegative and accompanied by a unit such as failures per operating hour. The output should be interpreted at the same stated boundary and over the same mission or reporting period as its inputs.

**Reasoning sequence.** (i) Define the asset and the function; (ii) write all inputs and their units; (iii) choose the simplest physically defensible model; (iv) perform the computation using an independent check; (v) compare the result with limiting cases; (vi) state uncertainty and model boundaries before recommending maintenance. For example, the limit of a no-failure event probability as an assumed event rate approaches zero should be consistent with ordinary experience. A result outside its physically possible range suggests either an arithmetic fault, incompatible units or a model used outside its assumptions.

**Worked engineering example.** If planned replacement costs 100 units and failure replacement costs 1,000, the tradeoff depends on Weibull shape; constant hazard alone provides little rationale for age replacement.

After evaluating the arithmetic, report what the result means and—equally important—what it does not mean. Distinguish a hypothetical prediction from a measured population statistic. If a numerical example uses a notional fleet or synthetic data, it must not appear in an operator's work package as a measured site result. For any policy comparison, repeat the calculation using at least two plausible ranges for its most uncertain input and report whether the choice changes.

### Plan a falsification test

A good explanation can be disproved. State an observation that would contradict the proposed failure mechanism, and arrange measurements so another engineer could reach an independent conclusion rather than merely agreeing with the initial diagnosis.

## 3. Where the model can fail

The stated expression assumes the replacement restores an as-new condition, includes the chosen failure cost and measures operating exposure; prove these assumptions before optimization.

An important diagnostic practice is to seek evidence against the simplest explanation. A repair which temporarily restores output can disguise an uncorrected design, installation or operating error. If the apparent rate improves after a maintenance change, normalize against exposure and examine whether production load, weather, equipment population or reporting conventions changed in the same period. Correlation between a signal and a failure does not establish that intervening on the signal will prevent the failure.

The operational consequence of a bad assumption depends on the equipment. For an ordinary production asset it may mean excess inventory or a costly breakdown. For a safety-critical plant it can mean loss of containment, personnel exposure, service failure or violation of required inspection obligations. Use the teaching result only for understanding; site-specific decisions need competent hazard review, current standards, supplier instructions, physical verification and appropriate approval.

### Keep the physical mechanism visible

An apparent trend in a chart is evidence about recorded variables, not automatically the explanation of a component failure. Ask which loads, contamination pathways, temperatures, controls, maintenance practices or environmental stresses could produce the observed pattern.

## 4. Engineering investigation: from model to evidence

**Field prompt.** Plot hypothetical cost rate over candidate intervals and identify which uncertainties alter the optimum.

Connect this task to the unit study: Changing all rolling bearings every 1,000 hours can consume healthy life while failing to catch contamination damage. By contrast, a seal on a hazardous fluid service may justify conservative inspection and verified containment independent of its average failure probability. The expected notebook output is concrete: Deliver a maintenance task list with triggering evidence, work method, permitted operating condition, isolation needs, interval rationale and post-work test. Include a sketch, a table of unknowns and an explicit statement of what observation would reverse the initial hypothesis. A useful investigation records the condition before repair, retains component photographs when safe, notes firmware and calibration versions where relevant, and documents any temporary bypass. Explain how the conclusion would be independently reproduced by another analyst.

**Proposed procedure.** First obtain permission and confirm the relevant safe isolation and operating boundaries; never open energized or pressurized equipment for a classroom exercise. Second use a published sampling interval or an explicit study protocol. Third capture raw data with units, timestamps and event codes before cleaning or filtering them. Fourth run a simple hand calculation and cross-check it with a separate implementation. Fifth evaluate sensitivity to one omitted mechanism, one measurement bias and one uncertain input. Sixth record the proposed action, owner, estimated restoration impact and a verification measure that will be checked after implementation.

A reliable result can be modest. It may show that two alternatives cannot yet be distinguished, that a missing event time prevents statistical estimation or that extra inspection has poor coverage. Reporting these limitations is preferable to manufacturing precision. For plant-level application, specify which person may authorize a shutdown, restart or alteration of protection logic; a textbook exercise never supplies that authorization.

## 5. Exercises and instructor checkpoints

1. **Definitions.** Define the physical or functional event involved in **preventive replacement intervals**. Give its observable boundary and one alternative definition that would change the counted population.
2. **Quantification.** Use the relation `Simplified cost rate for planned replacement at age τ: [C_p R(τ)+C_f(1-R(τ))]/∫_0^τ R(t)dt, assuming renewal at planned or first failure.` with a consistent assumed dataset of your own. Show all units and at least one limiting-case check.
3. **Sensitivity.** Change the most uncertain nonzero input by ±20% where physically meaningful. Compare the output and decide whether the maintenance choice is robust.
4. **Counterexample.** Explain precisely why the following limitation matters: The stated expression assumes the replacement restores an as-new condition, includes the chosen failure cost and measures operating exposure; prove these assumptions before optimization.
5. **Application.** Plot hypothetical cost rate over candidate intervals and identify which uncertainties alter the optimum. Supply an evidence table with at least three observations and mark each entry as measured, supplied by a source, or synthetic.

**Self-check guidance.** A correct response identifies the function, model, assumptions, arithmetic, consequence and plausible falsification. The numeric exercise should be reproducible from the student's displayed inputs. The sensitivity response should not silently vary an independent parameter if two inputs are physically coupled. The field task should end with an evidence request or a testable action rather than a generic recommendation to “do maintenance.”

## 6. Connections to the wider curriculum

This topic interacts with earlier units through lifetime probability, state restoration, operating mechanisms and cost. When proposing a spare or a maintenance interval, ask how it changes both the frequency of failures and the length of lost service. When proposing a sensor, ask how often it produces a useful warning and how the organization responds. An effective recommendation uses the smallest set of credible assumptions needed for the stated decision and explains the circumstances under which its simplified formula would stop being useful.

**Source-reading exercise.** Compare the language of your model with the NIST reliability handbook or the NASA reliability-centered maintenance material listed in the references. Do not reproduce external texts; use the primary source to check the meaning of the statistical term or maintenance method, then describe the limitation in your own words.


---

# Unit 05 · Lesson 02 — Corrective maintenance and restoration time

**Learning goal.** Explain the core engineering statement, calculate a clearly bounded example, challenge at least one assumption and propose a measurable action. This material is an educational draft, not an authority for equipment acceptance.

## 1. Concept and technical meaning

Corrective maintenance includes fault detection, diagnosis, isolation, repair, verification and return-to-service. Active wrench time, technical repair time, logistics delay and administrative hold should be reported separately. MTTR itself may refer to different clocks, so a report must define it.

The useful starting question is **“What physical or service event am I modeling?”** Place the studied item within the unit's central objective: Preventive replacement, inspection, condition-based intervention, and run-to-failure are economic and risk decisions, not moral labels. Age replacement only makes sense when the failure-time behavior and replacement consequence justify it. Sensor trends become decisions only with baseline, alarm thresholds, false-alarm handling and response plans. A numerical value only becomes an engineering claim when the mission duration, operating conditions, item state and decision boundary are specified. If the equipment is repaired between events, decide whether the model starts a new life or continues to represent accumulated degradation. When data are drawn from multiple installations, check whether load, age, ambient environment and maintenance practice are comparable.

### Keep the operational objective in view

A metric is useful when it changes a decision that helps deliver service. Additional data collection should therefore answer a concrete question: whether to inspect, redesign, change stocking policy, add monitoring or accept an explicitly bounded residual risk.

A professional worksheet for **corrective maintenance and restoration time** should preserve the original event definition and the raw denominator used in the calculation. Build a simple diagram that traces the studied input to a measured output. Label its arrows as measured relationships, physical assumptions or hypothetical causal mechanisms. This keeps the numerical calculation from silently becoming proof of a mechanism that has not been investigated.

## 2. Governing relation and derivation checks

**Primary relation:** `Mean downtime per event=total counted outage duration/number of counted restoration events.`

The relation should first be read in words and translated into a dimensional statement. Identify which quantities are probabilities, time or cycle measures, rates, costs, loads, engineering scores or empirical indicators. If an input is a probability, its feasible interval is from zero to one; if it is an event intensity, it must be nonnegative and accompanied by a unit such as failures per operating hour. The output should be interpreted at the same stated boundary and over the same mission or reporting period as its inputs.

**Reasoning sequence.** (i) Define the asset and the function; (ii) write all inputs and their units; (iii) choose the simplest physically defensible model; (iv) perform the computation using an independent check; (v) compare the result with limiting cases; (vi) state uncertainty and model boundaries before recommending maintenance. For example, the limit of a no-failure event probability as an assumed event rate approaches zero should be consistent with ordinary experience. A result outside its physically possible range suggests either an arithmetic fault, incompatible units or a model used outside its assumptions.

**Worked engineering example.** A failed motor takes 4 hours to replace but 42 hours to receive. If the outage clock includes logistics, the service restoration duration is 46 hours, not 4.

After evaluating the arithmetic, report what the result means and—equally important—what it does not mean. Distinguish a hypothetical prediction from a measured population statistic. If a numerical example uses a notional fleet or synthetic data, it must not appear in an operator's work package as a measured site result. For any policy comparison, repeat the calculation using at least two plausible ranges for its most uncertain input and report whether the choice changes.

### Define the denominator

Write down the reference population and the interval across which the observation has meaning. An event per machine-day differs from an event per operating hour if production schedules differ. A simulation that silently uses an assumed denominator produces a neat but potentially false comparison.

## 3. Where the model can fail

Restoration can be incomplete if a bypass is left in place or functional testing is skipped; define an acceptable return-to-service criterion.

An important diagnostic practice is to seek evidence against the simplest explanation. A repair which temporarily restores output can disguise an uncorrected design, installation or operating error. If the apparent rate improves after a maintenance change, normalize against exposure and examine whether production load, weather, equipment population or reporting conventions changed in the same period. Correlation between a signal and a failure does not establish that intervening on the signal will prevent the failure.

The operational consequence of a bad assumption depends on the equipment. For an ordinary production asset it may mean excess inventory or a costly breakdown. For a safety-critical plant it can mean loss of containment, personnel exposure, service failure or violation of required inspection obligations. Use the teaching result only for understanding; site-specific decisions need competent hazard review, current standards, supplier instructions, physical verification and appropriate approval.

### Separate requirement from measurement

An engineer should be able to state the acceptance requirement before seeing the measurement. Otherwise thresholds tend to move after results are known. Preserve the original requirement, report any exception and obtain authorized approval for changes.

## 4. Engineering investigation: from model to evidence

**Field prompt.** Create a downtime event timeline separating recognition, lockout, procurement, installation, test and handover.

Connect this task to the unit study: Design maintenance for a ventilator fan, standby generator, transfer pump and low-cost office fan. Separate safety-critical requirements from cost-only optimization. The expected notebook output is concrete: Deliver a maintenance task list with triggering evidence, work method, permitted operating condition, isolation needs, interval rationale and post-work test. Include a sketch, a table of unknowns and an explicit statement of what observation would reverse the initial hypothesis. A useful investigation records the condition before repair, retains component photographs when safe, notes firmware and calibration versions where relevant, and documents any temporary bypass. Explain how the conclusion would be independently reproduced by another analyst.

**Proposed procedure.** First obtain permission and confirm the relevant safe isolation and operating boundaries; never open energized or pressurized equipment for a classroom exercise. Second use a published sampling interval or an explicit study protocol. Third capture raw data with units, timestamps and event codes before cleaning or filtering them. Fourth run a simple hand calculation and cross-check it with a separate implementation. Fifth evaluate sensitivity to one omitted mechanism, one measurement bias and one uncertain input. Sixth record the proposed action, owner, estimated restoration impact and a verification measure that will be checked after implementation.

A reliable result can be modest. It may show that two alternatives cannot yet be distinguished, that a missing event time prevents statistical estimation or that extra inspection has poor coverage. Reporting these limitations is preferable to manufacturing precision. For plant-level application, specify which person may authorize a shutdown, restart or alteration of protection logic; a textbook exercise never supplies that authorization.

## 5. Exercises and instructor checkpoints

1. **Definitions.** Define the physical or functional event involved in **corrective maintenance and restoration time**. Give its observable boundary and one alternative definition that would change the counted population.
2. **Quantification.** Use the relation `Mean downtime per event=total counted outage duration/number of counted restoration events.` with a consistent assumed dataset of your own. Show all units and at least one limiting-case check.
3. **Sensitivity.** Change the most uncertain nonzero input by ±20% where physically meaningful. Compare the output and decide whether the maintenance choice is robust.
4. **Counterexample.** Explain precisely why the following limitation matters: Restoration can be incomplete if a bypass is left in place or functional testing is skipped; define an acceptable return-to-service criterion.
5. **Application.** Create a downtime event timeline separating recognition, lockout, procurement, installation, test and handover. Supply an evidence table with at least three observations and mark each entry as measured, supplied by a source, or synthetic.

**Self-check guidance.** A correct response identifies the function, model, assumptions, arithmetic, consequence and plausible falsification. The numeric exercise should be reproducible from the student's displayed inputs. The sensitivity response should not silently vary an independent parameter if two inputs are physically coupled. The field task should end with an evidence request or a testable action rather than a generic recommendation to “do maintenance.”

## 6. Connections to the wider curriculum

This topic interacts with earlier units through lifetime probability, state restoration, operating mechanisms and cost. When proposing a spare or a maintenance interval, ask how it changes both the frequency of failures and the length of lost service. When proposing a sensor, ask how often it produces a useful warning and how the organization responds. An effective recommendation uses the smallest set of credible assumptions needed for the stated decision and explains the circumstances under which its simplified formula would stop being useful.

**Source-reading exercise.** Compare the language of your model with the NIST reliability handbook or the NASA reliability-centered maintenance material listed in the references. Do not reproduce external texts; use the primary source to check the meaning of the statistical term or maintenance method, then describe the limitation in your own words.


---

# Unit 05 · Lesson 03 — Vibration diagnostics and spectrum analysis

**Learning goal.** Explain the core engineering statement, calculate a clearly bounded example, challenge at least one assumption and propose a measurable action. This material is an educational draft, not an authority for equipment acceptance.

## 1. Concept and technical meaning

Rotating equipment vibration can reveal imbalance, misalignment, looseness, resonance and bearing defects, but the same symptom has multiple causes. Overall RMS is a severity descriptor over a bandwidth; it cannot uniquely diagnose a fault. Sampling, sensor mounting, operating speed and load must be controlled.

The useful starting question is **“What physical or service event am I modeling?”** Place the studied item within the unit's central objective: Preventive replacement, inspection, condition-based intervention, and run-to-failure are economic and risk decisions, not moral labels. Age replacement only makes sense when the failure-time behavior and replacement consequence justify it. Sensor trends become decisions only with baseline, alarm thresholds, false-alarm handling and response plans. A numerical value only becomes an engineering claim when the mission duration, operating conditions, item state and decision boundary are specified. If the equipment is repaired between events, decide whether the model starts a new life or continues to represent accumulated degradation. When data are drawn from multiple installations, check whether load, age, ambient environment and maintenance practice are comparable.

### Make uncertainty actionable

The practical response to missing information is usually a low-cost measurement, a conservative bound or a controlled trial. Sensitivity analysis exposes which uncertain assumption is capable of reversing a recommendation.

A professional worksheet for **vibration diagnostics and spectrum analysis** should preserve the original event definition and the raw denominator used in the calculation. Build a simple diagram that traces the studied input to a measured output. Label its arrows as measured relationships, physical assumptions or hypothetical causal mechanisms. This keeps the numerical calculation from silently becoming proof of a mechanism that has not been investigated.

## 2. Governing relation and derivation checks

**Primary relation:** `For discrete centered samples x_i, RMS=sqrt((1/n)Σ x_i²); units depend on whether x is displacement, velocity or acceleration.`

The relation should first be read in words and translated into a dimensional statement. Identify which quantities are probabilities, time or cycle measures, rates, costs, loads, engineering scores or empirical indicators. If an input is a probability, its feasible interval is from zero to one; if it is an event intensity, it must be nonnegative and accompanied by a unit such as failures per operating hour. The output should be interpreted at the same stated boundary and over the same mission or reporting period as its inputs.

**Reasoning sequence.** (i) Define the asset and the function; (ii) write all inputs and their units; (iii) choose the simplest physically defensible model; (iv) perform the computation using an independent check; (v) compare the result with limiting cases; (vi) state uncertainty and model boundaries before recommending maintenance. For example, the limit of a no-failure event probability as an assumed event rate approaches zero should be consistent with ordinary experience. A result outside its physically possible range suggests either an arithmetic fault, incompatible units or a model used outside its assumptions.

**Worked engineering example.** Four velocity samples 1, -1, 2, -2 mm/s have RMS=sqrt(2.5)=1.581 mm/s. This number alone does not identify the machine condition.

After evaluating the arithmetic, report what the result means and—equally important—what it does not mean. Distinguish a hypothetical prediction from a measured population statistic. If a numerical example uses a notional fleet or synthetic data, it must not appear in an operator's work package as a measured site result. For any policy comparison, repeat the calculation using at least two plausible ranges for its most uncertain input and report whether the choice changes.

### Keep the physical mechanism visible

An apparent trend in a chart is evidence about recorded variables, not automatically the explanation of a component failure. Ask which loads, contamination pathways, temperatures, controls, maintenance practices or environmental stresses could produce the observed pattern.

## 3. Where the model can fail

FFT peak positions can be distorted by aliasing, nonstationarity, resolution or a sensor mounting resonance; compare to tachometer and load records.

An important diagnostic practice is to seek evidence against the simplest explanation. A repair which temporarily restores output can disguise an uncorrected design, installation or operating error. If the apparent rate improves after a maintenance change, normalize against exposure and examine whether production load, weather, equipment population or reporting conventions changed in the same period. Correlation between a signal and a failure does not establish that intervening on the signal will prevent the failure.

The operational consequence of a bad assumption depends on the equipment. For an ordinary production asset it may mean excess inventory or a costly breakdown. For a safety-critical plant it can mean loss of containment, personnel exposure, service failure or violation of required inspection obligations. Use the teaching result only for understanding; site-specific decisions need competent hazard review, current standards, supplier instructions, physical verification and appropriate approval.

### Distinguish data from decisions

A probability is an input to a decision rather than a decision by itself. Two alternatives with equal failure probability can lead to different responses when consequences, restoration time and regulatory obligations are different.

## 4. Engineering investigation: from model to evidence

**Field prompt.** Design a baseline test for a fan, specifying sensor axes, speed, load, window, sampling and alarm process.

Connect this task to the unit study: Design maintenance for a ventilator fan, standby generator, transfer pump and low-cost office fan. Separate safety-critical requirements from cost-only optimization. The expected notebook output is concrete: Deliver a maintenance task list with triggering evidence, work method, permitted operating condition, isolation needs, interval rationale and post-work test. Include a sketch, a table of unknowns and an explicit statement of what observation would reverse the initial hypothesis. A useful investigation records the condition before repair, retains component photographs when safe, notes firmware and calibration versions where relevant, and documents any temporary bypass. Explain how the conclusion would be independently reproduced by another analyst.

**Proposed procedure.** First obtain permission and confirm the relevant safe isolation and operating boundaries; never open energized or pressurized equipment for a classroom exercise. Second use a published sampling interval or an explicit study protocol. Third capture raw data with units, timestamps and event codes before cleaning or filtering them. Fourth run a simple hand calculation and cross-check it with a separate implementation. Fifth evaluate sensitivity to one omitted mechanism, one measurement bias and one uncertain input. Sixth record the proposed action, owner, estimated restoration impact and a verification measure that will be checked after implementation.

A reliable result can be modest. It may show that two alternatives cannot yet be distinguished, that a missing event time prevents statistical estimation or that extra inspection has poor coverage. Reporting these limitations is preferable to manufacturing precision. For plant-level application, specify which person may authorize a shutdown, restart or alteration of protection logic; a textbook exercise never supplies that authorization.

## 5. Exercises and instructor checkpoints

1. **Definitions.** Define the physical or functional event involved in **vibration diagnostics and spectrum analysis**. Give its observable boundary and one alternative definition that would change the counted population.
2. **Quantification.** Use the relation `For discrete centered samples x_i, RMS=sqrt((1/n)Σ x_i²); units depend on whether x is displacement, velocity or acceleration.` with a consistent assumed dataset of your own. Show all units and at least one limiting-case check.
3. **Sensitivity.** Change the most uncertain nonzero input by ±20% where physically meaningful. Compare the output and decide whether the maintenance choice is robust.
4. **Counterexample.** Explain precisely why the following limitation matters: FFT peak positions can be distorted by aliasing, nonstationarity, resolution or a sensor mounting resonance; compare to tachometer and load records.
5. **Application.** Design a baseline test for a fan, specifying sensor axes, speed, load, window, sampling and alarm process. Supply an evidence table with at least three observations and mark each entry as measured, supplied by a source, or synthetic.

**Self-check guidance.** A correct response identifies the function, model, assumptions, arithmetic, consequence and plausible falsification. The numeric exercise should be reproducible from the student's displayed inputs. The sensitivity response should not silently vary an independent parameter if two inputs are physically coupled. The field task should end with an evidence request or a testable action rather than a generic recommendation to “do maintenance.”

## 6. Connections to the wider curriculum

This topic interacts with earlier units through lifetime probability, state restoration, operating mechanisms and cost. When proposing a spare or a maintenance interval, ask how it changes both the frequency of failures and the length of lost service. When proposing a sensor, ask how often it produces a useful warning and how the organization responds. An effective recommendation uses the smallest set of credible assumptions needed for the stated decision and explains the circumstances under which its simplified formula would stop being useful.

**Source-reading exercise.** Compare the language of your model with the NIST reliability handbook or the NASA reliability-centered maintenance material listed in the references. Do not reproduce external texts; use the primary source to check the meaning of the statistical term or maintenance method, then describe the limitation in your own words.


---

# Unit 05 · Lesson 04 — Oil, thermography and ultrasonic monitoring

**Learning goal.** Explain the core engineering statement, calculate a clearly bounded example, challenge at least one assumption and propose a measurable action. This material is an educational draft, not an authority for equipment acceptance.

## 1. Concept and technical meaning

Lubricant analysis can reveal wear metals, viscosity change, water contamination and particle content; thermography can identify thermal asymmetry; ultrasound can detect certain leaks and friction signatures. Each method requires correct sampling and baseline interpretation. Combining independent observations improves diagnosis.

The useful starting question is **“What physical or service event am I modeling?”** Place the studied item within the unit's central objective: Preventive replacement, inspection, condition-based intervention, and run-to-failure are economic and risk decisions, not moral labels. Age replacement only makes sense when the failure-time behavior and replacement consequence justify it. Sensor trends become decisions only with baseline, alarm thresholds, false-alarm handling and response plans. A numerical value only becomes an engineering claim when the mission duration, operating conditions, item state and decision boundary are specified. If the equipment is repaired between events, decide whether the model starts a new life or continues to represent accumulated degradation. When data are drawn from multiple installations, check whether load, age, ambient environment and maintenance practice are comparable.

### Plan a falsification test

A good explanation can be disproved. State an observation that would contradict the proposed failure mechanism, and arrange measurements so another engineer could reach an independent conclusion rather than merely agreeing with the initial diagnosis.

A professional worksheet for **oil, thermography and ultrasonic monitoring** should preserve the original event definition and the raw denominator used in the calculation. Build a simple diagram that traces the studied input to a measured output. Label its arrows as measured relationships, physical assumptions or hypothetical causal mechanisms. This keeps the numerical calculation from silently becoming proof of a mechanism that has not been investigated.

## 2. Governing relation and derivation checks

**Primary relation:** `Temperature rise ΔT=T_location-T_reference is meaningful only when emissivity, load, ambient and viewing conditions are comparable.`

The relation should first be read in words and translated into a dimensional statement. Identify which quantities are probabilities, time or cycle measures, rates, costs, loads, engineering scores or empirical indicators. If an input is a probability, its feasible interval is from zero to one; if it is an event intensity, it must be nonnegative and accompanied by a unit such as failures per operating hour. The output should be interpreted at the same stated boundary and over the same mission or reporting period as its inputs.

**Reasoning sequence.** (i) Define the asset and the function; (ii) write all inputs and their units; (iii) choose the simplest physically defensible model; (iv) perform the computation using an independent check; (v) compare the result with limiting cases; (vi) state uncertainty and model boundaries before recommending maintenance. For example, the limit of a no-failure event probability as an assumed event rate approaches zero should be consistent with ordinary experience. A result outside its physically possible range suggests either an arithmetic fault, incompatible units or a model used outside its assumptions.

**Worked engineering example.** A bearing housing is 15 °C warmer than an adjacent identical housing. Compare actual loads, insulation and sensor settings before declaring imminent bearing failure.

After evaluating the arithmetic, report what the result means and—equally important—what it does not mean. Distinguish a hypothetical prediction from a measured population statistic. If a numerical example uses a notional fleet or synthetic data, it must not appear in an operator's work package as a measured site result. For any policy comparison, repeat the calculation using at least two plausible ranges for its most uncertain input and report whether the choice changes.

### Separate requirement from measurement

An engineer should be able to state the acceptance requirement before seeing the measurement. Otherwise thresholds tend to move after results are known. Preserve the original requirement, report any exception and obtain authorized approval for changes.

## 3. Where the model can fail

An infrared camera reports apparent radiance, not direct internal material temperature. Inaccessible or reflective surfaces create misleading readings.

An important diagnostic practice is to seek evidence against the simplest explanation. A repair which temporarily restores output can disguise an uncorrected design, installation or operating error. If the apparent rate improves after a maintenance change, normalize against exposure and examine whether production load, weather, equipment population or reporting conventions changed in the same period. Correlation between a signal and a failure does not establish that intervening on the signal will prevent the failure.

The operational consequence of a bad assumption depends on the equipment. For an ordinary production asset it may mean excess inventory or a costly breakdown. For a safety-critical plant it can mean loss of containment, personnel exposure, service failure or violation of required inspection obligations. Use the teaching result only for understanding; site-specific decisions need competent hazard review, current standards, supplier instructions, physical verification and appropriate approval.

### Audit model assumptions

Every model has a region in which its assumptions make sense. Before using an equation in a recommendation, check units, boundary, independence assumptions, the way failures are counted, and whether repair changes the modeled population.

## 4. Engineering investigation: from model to evidence

**Field prompt.** Plan an oil sample location and trend chart, with contamination limits justified by actual machine and lubricant requirements.

Connect this task to the unit study: Changing all rolling bearings every 1,000 hours can consume healthy life while failing to catch contamination damage. By contrast, a seal on a hazardous fluid service may justify conservative inspection and verified containment independent of its average failure probability. The expected notebook output is concrete: Deliver a maintenance task list with triggering evidence, work method, permitted operating condition, isolation needs, interval rationale and post-work test. Include a sketch, a table of unknowns and an explicit statement of what observation would reverse the initial hypothesis. A useful investigation records the condition before repair, retains component photographs when safe, notes firmware and calibration versions where relevant, and documents any temporary bypass. Explain how the conclusion would be independently reproduced by another analyst.

**Proposed procedure.** First obtain permission and confirm the relevant safe isolation and operating boundaries; never open energized or pressurized equipment for a classroom exercise. Second use a published sampling interval or an explicit study protocol. Third capture raw data with units, timestamps and event codes before cleaning or filtering them. Fourth run a simple hand calculation and cross-check it with a separate implementation. Fifth evaluate sensitivity to one omitted mechanism, one measurement bias and one uncertain input. Sixth record the proposed action, owner, estimated restoration impact and a verification measure that will be checked after implementation.

A reliable result can be modest. It may show that two alternatives cannot yet be distinguished, that a missing event time prevents statistical estimation or that extra inspection has poor coverage. Reporting these limitations is preferable to manufacturing precision. For plant-level application, specify which person may authorize a shutdown, restart or alteration of protection logic; a textbook exercise never supplies that authorization.

## 5. Exercises and instructor checkpoints

1. **Definitions.** Define the physical or functional event involved in **oil, thermography and ultrasonic monitoring**. Give its observable boundary and one alternative definition that would change the counted population.
2. **Quantification.** Use the relation `Temperature rise ΔT=T_location-T_reference is meaningful only when emissivity, load, ambient and viewing conditions are comparable.` with a consistent assumed dataset of your own. Show all units and at least one limiting-case check.
3. **Sensitivity.** Change the most uncertain nonzero input by ±20% where physically meaningful. Compare the output and decide whether the maintenance choice is robust.
4. **Counterexample.** Explain precisely why the following limitation matters: An infrared camera reports apparent radiance, not direct internal material temperature. Inaccessible or reflective surfaces create misleading readings.
5. **Application.** Plan an oil sample location and trend chart, with contamination limits justified by actual machine and lubricant requirements. Supply an evidence table with at least three observations and mark each entry as measured, supplied by a source, or synthetic.

**Self-check guidance.** A correct response identifies the function, model, assumptions, arithmetic, consequence and plausible falsification. The numeric exercise should be reproducible from the student's displayed inputs. The sensitivity response should not silently vary an independent parameter if two inputs are physically coupled. The field task should end with an evidence request or a testable action rather than a generic recommendation to “do maintenance.”

## 6. Connections to the wider curriculum

This topic interacts with earlier units through lifetime probability, state restoration, operating mechanisms and cost. When proposing a spare or a maintenance interval, ask how it changes both the frequency of failures and the length of lost service. When proposing a sensor, ask how often it produces a useful warning and how the organization responds. An effective recommendation uses the smallest set of credible assumptions needed for the stated decision and explains the circumstances under which its simplified formula would stop being useful.

**Source-reading exercise.** Compare the language of your model with the NIST reliability handbook or the NASA reliability-centered maintenance material listed in the references. Do not reproduce external texts; use the primary source to check the meaning of the statistical term or maintenance method, then describe the limitation in your own words.


---

# Unit 05 · Lesson 05 — Condition thresholds and prognostics

**Learning goal.** Explain the core engineering statement, calculate a clearly bounded example, challenge at least one assumption and propose a measurable action. This material is an educational draft, not an authority for equipment acceptance.

## 1. Concept and technical meaning

A predictive maintenance system uses measurable features, baselines, thresholds, forecast uncertainty and explicit actions. A classification score is not remaining useful life. Confidence deteriorates during operating shifts, replacements, changes in sensor positions and new failure mechanisms.

The useful starting question is **“What physical or service event am I modeling?”** Place the studied item within the unit's central objective: Preventive replacement, inspection, condition-based intervention, and run-to-failure are economic and risk decisions, not moral labels. Age replacement only makes sense when the failure-time behavior and replacement consequence justify it. Sensor trends become decisions only with baseline, alarm thresholds, false-alarm handling and response plans. A numerical value only becomes an engineering claim when the mission duration, operating conditions, item state and decision boundary are specified. If the equipment is repaired between events, decide whether the model starts a new life or continues to represent accumulated degradation. When data are drawn from multiple installations, check whether load, age, ambient environment and maintenance practice are comparable.

### Define the denominator

Write down the reference population and the interval across which the observation has meaning. An event per machine-day differs from an event per operating hour if production schedules differ. A simulation that silently uses an assumed denominator produces a neat but potentially false comparison.

A professional worksheet for **condition thresholds and prognostics** should preserve the original event definition and the raw denominator used in the calculation. Build a simple diagram that traces the studied input to a measured output. Label its arrows as measured relationships, physical assumptions or hypothetical causal mechanisms. This keeps the numerical calculation from silently becoming proof of a mechanism that has not been investigated.

## 2. Governing relation and derivation checks

**Primary relation:** `A linear degradation extrapolation t_remaining=(limit-current)/slope is illustrative and valid only while the trend assumptions remain plausible.`

The relation should first be read in words and translated into a dimensional statement. Identify which quantities are probabilities, time or cycle measures, rates, costs, loads, engineering scores or empirical indicators. If an input is a probability, its feasible interval is from zero to one; if it is an event intensity, it must be nonnegative and accompanied by a unit such as failures per operating hour. The output should be interpreted at the same stated boundary and over the same mission or reporting period as its inputs.

**Reasoning sequence.** (i) Define the asset and the function; (ii) write all inputs and their units; (iii) choose the simplest physically defensible model; (iv) perform the computation using an independent check; (v) compare the result with limiting cases; (vi) state uncertainty and model boundaries before recommending maintenance. For example, the limit of a no-failure event probability as an assumed event rate approaches zero should be consistent with ordinary experience. A result outside its physically possible range suggests either an arithmetic fault, incompatible units or a model used outside its assumptions.

**Worked engineering example.** A normalized vibration indicator rises from 2 to 5 in 100 hours and alarm limit is 8. A linear slope 0.03 units/hour predicts 100 hours to threshold, ignoring uncertainty and regime change.

After evaluating the arithmetic, report what the result means and—equally important—what it does not mean. Distinguish a hypothetical prediction from a measured population statistic. If a numerical example uses a notional fleet or synthetic data, it must not appear in an operator's work package as a measured site result. For any policy comparison, repeat the calculation using at least two plausible ranges for its most uncertain input and report whether the choice changes.

### Distinguish data from decisions

A probability is an input to a decision rather than a decision by itself. Two alternatives with equal failure probability can lead to different responses when consequences, restoration time and regulatory obligations are different.

## 3. Where the model can fail

Triggering replacement on every noisy excursion creates false positives and unnecessary downtime; hysteresis or sustained exceedance may help but must not hide dangerous events.

An important diagnostic practice is to seek evidence against the simplest explanation. A repair which temporarily restores output can disguise an uncorrected design, installation or operating error. If the apparent rate improves after a maintenance change, normalize against exposure and examine whether production load, weather, equipment population or reporting conventions changed in the same period. Correlation between a signal and a failure does not establish that intervening on the signal will prevent the failure.

The operational consequence of a bad assumption depends on the equipment. For an ordinary production asset it may mean excess inventory or a costly breakdown. For a safety-critical plant it can mean loss of containment, personnel exposure, service failure or violation of required inspection obligations. Use the teaching result only for understanding; site-specific decisions need competent hazard review, current standards, supplier instructions, physical verification and appropriate approval.

### Keep the operational objective in view

A metric is useful when it changes a decision that helps deliver service. Additional data collection should therefore answer a concrete question: whether to inspect, redesign, change stocking policy, add monitoring or accept an explicitly bounded residual risk.

## 4. Engineering investigation: from model to evidence

**Field prompt.** Define alert, intervention, validation and model-retraining rules for a compressor condition-monitoring pilot.

Connect this task to the unit study: Design maintenance for a ventilator fan, standby generator, transfer pump and low-cost office fan. Separate safety-critical requirements from cost-only optimization. The expected notebook output is concrete: Deliver a maintenance task list with triggering evidence, work method, permitted operating condition, isolation needs, interval rationale and post-work test. Include a sketch, a table of unknowns and an explicit statement of what observation would reverse the initial hypothesis. A useful investigation records the condition before repair, retains component photographs when safe, notes firmware and calibration versions where relevant, and documents any temporary bypass. Explain how the conclusion would be independently reproduced by another analyst.

**Proposed procedure.** First obtain permission and confirm the relevant safe isolation and operating boundaries; never open energized or pressurized equipment for a classroom exercise. Second use a published sampling interval or an explicit study protocol. Third capture raw data with units, timestamps and event codes before cleaning or filtering them. Fourth run a simple hand calculation and cross-check it with a separate implementation. Fifth evaluate sensitivity to one omitted mechanism, one measurement bias and one uncertain input. Sixth record the proposed action, owner, estimated restoration impact and a verification measure that will be checked after implementation.

A reliable result can be modest. It may show that two alternatives cannot yet be distinguished, that a missing event time prevents statistical estimation or that extra inspection has poor coverage. Reporting these limitations is preferable to manufacturing precision. For plant-level application, specify which person may authorize a shutdown, restart or alteration of protection logic; a textbook exercise never supplies that authorization.

## 5. Exercises and instructor checkpoints

1. **Definitions.** Define the physical or functional event involved in **condition thresholds and prognostics**. Give its observable boundary and one alternative definition that would change the counted population.
2. **Quantification.** Use the relation `A linear degradation extrapolation t_remaining=(limit-current)/slope is illustrative and valid only while the trend assumptions remain plausible.` with a consistent assumed dataset of your own. Show all units and at least one limiting-case check.
3. **Sensitivity.** Change the most uncertain nonzero input by ±20% where physically meaningful. Compare the output and decide whether the maintenance choice is robust.
4. **Counterexample.** Explain precisely why the following limitation matters: Triggering replacement on every noisy excursion creates false positives and unnecessary downtime; hysteresis or sustained exceedance may help but must not hide dangerous events.
5. **Application.** Define alert, intervention, validation and model-retraining rules for a compressor condition-monitoring pilot. Supply an evidence table with at least three observations and mark each entry as measured, supplied by a source, or synthetic.

**Self-check guidance.** A correct response identifies the function, model, assumptions, arithmetic, consequence and plausible falsification. The numeric exercise should be reproducible from the student's displayed inputs. The sensitivity response should not silently vary an independent parameter if two inputs are physically coupled. The field task should end with an evidence request or a testable action rather than a generic recommendation to “do maintenance.”

## 6. Connections to the wider curriculum

This topic interacts with earlier units through lifetime probability, state restoration, operating mechanisms and cost. When proposing a spare or a maintenance interval, ask how it changes both the frequency of failures and the length of lost service. When proposing a sensor, ask how often it produces a useful warning and how the organization responds. An effective recommendation uses the smallest set of credible assumptions needed for the stated decision and explains the circumstances under which its simplified formula would stop being useful.

**Source-reading exercise.** Compare the language of your model with the NIST reliability handbook or the NASA reliability-centered maintenance material listed in the references. Do not reproduce external texts; use the primary source to check the meaning of the statistical term or maintenance method, then describe the limitation in your own words.


---

