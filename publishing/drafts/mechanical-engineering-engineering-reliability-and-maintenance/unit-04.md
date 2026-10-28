# Unit 04: Failure Mechanisms and Root-Cause Methods

**Course Code**: ERM 404 · **Level**: Advanced Undergraduate Engineering

## Unit Overview & Physical Foundations

This comprehensive university textbook unit covers the theoretical framework, physical modeling, mathematical governing equations, and engineering applications of **Failure Mechanisms and Root-Cause Methods**.

# Unit 04 · Lesson 01 — FMEA and disciplined risk screening

**Learning goal.** Explain the core engineering statement, calculate a clearly bounded example, challenge at least one assumption and propose a measurable action. This material is an educational draft, not an authority for equipment acceptance.

## 1. Concept and technical meaning

Failure Modes and Effects Analysis identifies item functions, potential modes, effects, causes, preventive controls, detection controls and actions. It is iterative and evidence-based; assessment scales must be defined locally. An RPN can prioritize discussion but never overrides unacceptable severity or statutory duties.

The useful starting question is **“What physical or service event am I modeling?”** Place the studied item within the unit's central objective: A useful failure analysis distinguishes observed symptom, functional failure, failure mode, physical mechanism and systemic cause. FMEA is a structured screening technique, not a guarantee of safety; rankings depend on scales and judgement. Root-cause methods must be anchored in retained evidence and causal tests. A numerical value only becomes an engineering claim when the mission duration, operating conditions, item state and decision boundary are specified. If the equipment is repaired between events, decide whether the model starts a new life or continues to represent accumulated degradation. When data are drawn from multiple installations, check whether load, age, ambient environment and maintenance practice are comparable.

### Plan a falsification test

A good explanation can be disproved. State an observation that would contradict the proposed failure mechanism, and arrange measurements so another engineer could reach an independent conclusion rather than merely agreeing with the initial diagnosis.

A professional worksheet for **fmea and disciplined risk screening** should preserve the original event definition and the raw denominator used in the calculation. Build a simple diagram that traces the studied input to a measured output. Label its arrows as measured relationships, physical assumptions or hypothetical causal mechanisms. This keeps the numerical calculation from silently becoming proof of a mechanism that has not been investigated.

## 2. Governing relation and derivation checks

**Primary relation:** `Common screening index RPN=S×O×D uses ordinal ranks; do not interpret RPN/1000 as a failure probability.`

The relation should first be read in words and translated into a dimensional statement. Identify which quantities are probabilities, time or cycle measures, rates, costs, loads, engineering scores or empirical indicators. If an input is a probability, its feasible interval is from zero to one; if it is an event intensity, it must be nonnegative and accompanied by a unit such as failures per operating hour. The output should be interpreted at the same stated boundary and over the same mission or reporting period as its inputs.

**Reasoning sequence.** (i) Define the asset and the function; (ii) write all inputs and their units; (iii) choose the simplest physically defensible model; (iv) perform the computation using an independent check; (v) compare the result with limiting cases; (vi) state uncertainty and model boundaries before recommending maintenance. For example, the limit of a no-failure event probability as an assumed event rate approaches zero should be consistent with ordinary experience. A result outside its physically possible range suggests either an arithmetic fault, incompatible units or a model used outside its assumptions.

**Worked engineering example.** A miscalibrated temperature sensor may score modest occurrence but very high severity if it can defeat thermal protection. A cracked bracket can be visible yet have serious falling-object consequences.

After evaluating the arithmetic, report what the result means and—equally important—what it does not mean. Distinguish a hypothetical prediction from a measured population statistic. If a numerical example uses a notional fleet or synthetic data, it must not appear in an operator's work package as a measured site result. For any policy comparison, repeat the calculation using at least two plausible ranges for its most uncertain input and report whether the choice changes.

### Separate requirement from measurement

An engineer should be able to state the acceptance requirement before seeing the measurement. Otherwise thresholds tend to move after results are known. Preserve the original requirement, report any exception and obtain authorized approval for changes.

## 3. Where the model can fail

Changing a detection score after adding an alarm does not prove risk reduction if false negatives, sensor power loss and operator response are untested.

An important diagnostic practice is to seek evidence against the simplest explanation. A repair which temporarily restores output can disguise an uncorrected design, installation or operating error. If the apparent rate improves after a maintenance change, normalize against exposure and examine whether production load, weather, equipment population or reporting conventions changed in the same period. Correlation between a signal and a failure does not establish that intervening on the signal will prevent the failure.

The operational consequence of a bad assumption depends on the equipment. For an ordinary production asset it may mean excess inventory or a costly breakdown. For a safety-critical plant it can mean loss of containment, personnel exposure, service failure or violation of required inspection obligations. Use the teaching result only for understanding; site-specific decisions need competent hazard review, current standards, supplier instructions, physical verification and appropriate approval.

### Audit model assumptions

Every model has a region in which its assumptions make sense. Before using an equation in a recommendation, check units, boundary, independence assumptions, the way failures are counted, and whether repair changes the modeled population.

## 4. Engineering investigation: from model to evidence

**Field prompt.** Write one complete FMEA row for a pump dry-running event with evidence for each proposed control.

Connect this task to the unit study: A gearbox trips on high vibration. Replacing the bearing may restore function without explaining whether inadequate lubrication, assembly preload, shaft misalignment or a faulty sensor caused the event. A durable corrective action must target the tested mechanism and verify it later. The expected notebook output is concrete: Deliver a FMEA and an incident report containing verified observations, competing hypotheses, causal testing and effectiveness criteria. Include a sketch, a table of unknowns and an explicit statement of what observation would reverse the initial hypothesis. A useful investigation records the condition before repair, retains component photographs when safe, notes firmware and calibration versions where relevant, and documents any temporary bypass. Explain how the conclusion would be independently reproduced by another analyst.

**Proposed procedure.** First obtain permission and confirm the relevant safe isolation and operating boundaries; never open energized or pressurized equipment for a classroom exercise. Second use a published sampling interval or an explicit study protocol. Third capture raw data with units, timestamps and event codes before cleaning or filtering them. Fourth run a simple hand calculation and cross-check it with a separate implementation. Fifth evaluate sensitivity to one omitted mechanism, one measurement bias and one uncertain input. Sixth record the proposed action, owner, estimated restoration impact and a verification measure that will be checked after implementation.

A reliable result can be modest. It may show that two alternatives cannot yet be distinguished, that a missing event time prevents statistical estimation or that extra inspection has poor coverage. Reporting these limitations is preferable to manufacturing precision. For plant-level application, specify which person may authorize a shutdown, restart or alteration of protection logic; a textbook exercise never supplies that authorization.

## 5. Exercises and instructor checkpoints

1. **Definitions.** Define the physical or functional event involved in **fmea and disciplined risk screening**. Give its observable boundary and one alternative definition that would change the counted population.
2. **Quantification.** Use the relation `Common screening index RPN=S×O×D uses ordinal ranks; do not interpret RPN/1000 as a failure probability.` with a consistent assumed dataset of your own. Show all units and at least one limiting-case check.
3. **Sensitivity.** Change the most uncertain nonzero input by ±20% where physically meaningful. Compare the output and decide whether the maintenance choice is robust.
4. **Counterexample.** Explain precisely why the following limitation matters: Changing a detection score after adding an alarm does not prove risk reduction if false negatives, sensor power loss and operator response are untested.
5. **Application.** Write one complete FMEA row for a pump dry-running event with evidence for each proposed control. Supply an evidence table with at least three observations and mark each entry as measured, supplied by a source, or synthetic.

**Self-check guidance.** A correct response identifies the function, model, assumptions, arithmetic, consequence and plausible falsification. The numeric exercise should be reproducible from the student's displayed inputs. The sensitivity response should not silently vary an independent parameter if two inputs are physically coupled. The field task should end with an evidence request or a testable action rather than a generic recommendation to “do maintenance.”

## 6. Connections to the wider curriculum

This topic interacts with earlier units through lifetime probability, state restoration, operating mechanisms and cost. When proposing a spare or a maintenance interval, ask how it changes both the frequency of failures and the length of lost service. When proposing a sensor, ask how often it produces a useful warning and how the organization responds. An effective recommendation uses the smallest set of credible assumptions needed for the stated decision and explains the circumstances under which its simplified formula would stop being useful.

**Source-reading exercise.** Compare the language of your model with the NIST reliability handbook or the NASA reliability-centered maintenance material listed in the references. Do not reproduce external texts; use the primary source to check the meaning of the statistical term or maintenance method, then describe the limitation in your own words.


---

# Unit 04 · Lesson 02 — Reliability-centered maintenance decisions

**Learning goal.** Explain the core engineering statement, calculate a clearly bounded example, challenge at least one assumption and propose a measurable action. This material is an educational draft, not an authority for equipment acceptance.

## 1. Concept and technical meaning

RCM begins with functions and consequences, then evaluates failure modes and technically feasible tasks. It does not mean “maintain every asset more often.” Inspection interval should be related to degradation behavior and the time available between detectable potential failure and functional failure.

The useful starting question is **“What physical or service event am I modeling?”** Place the studied item within the unit's central objective: A useful failure analysis distinguishes observed symptom, functional failure, failure mode, physical mechanism and systemic cause. FMEA is a structured screening technique, not a guarantee of safety; rankings depend on scales and judgement. Root-cause methods must be anchored in retained evidence and causal tests. A numerical value only becomes an engineering claim when the mission duration, operating conditions, item state and decision boundary are specified. If the equipment is repaired between events, decide whether the model starts a new life or continues to represent accumulated degradation. When data are drawn from multiple installations, check whether load, age, ambient environment and maintenance practice are comparable.

### Define the denominator

Write down the reference population and the interval across which the observation has meaning. An event per machine-day differs from an event per operating hour if production schedules differ. A simulation that silently uses an assumed denominator produces a neat but potentially false comparison.

A professional worksheet for **reliability-centered maintenance decisions** should preserve the original event definition and the raw denominator used in the calculation. Build a simple diagram that traces the studied input to a measured output. Label its arrows as measured relationships, physical assumptions or hypothetical causal mechanisms. This keeps the numerical calculation from silently becoming proof of a mechanism that has not been investigated.

## 2. Governing relation and derivation checks

**Primary relation:** `If P-F interval has a conservative estimate of 12 days, a proposed 30-day inspection cannot reliably find the warning in that window.`

The relation should first be read in words and translated into a dimensional statement. Identify which quantities are probabilities, time or cycle measures, rates, costs, loads, engineering scores or empirical indicators. If an input is a probability, its feasible interval is from zero to one; if it is an event intensity, it must be nonnegative and accompanied by a unit such as failures per operating hour. The output should be interpreted at the same stated boundary and over the same mission or reporting period as its inputs.

**Reasoning sequence.** (i) Define the asset and the function; (ii) write all inputs and their units; (iii) choose the simplest physically defensible model; (iv) perform the computation using an independent check; (v) compare the result with limiting cases; (vi) state uncertainty and model boundaries before recommending maintenance. For example, the limit of a no-failure event probability as an assumed event rate approaches zero should be consistent with ordinary experience. A result outside its physically possible range suggests either an arithmetic fault, incompatible units or a model used outside its assumptions.

**Worked engineering example.** An oil-contamination trend may give weeks of warning for a gearbox; an electronic switch can fail randomly without a measurable P-F precursor. Different policies are justified.

After evaluating the arithmetic, report what the result means and—equally important—what it does not mean. Distinguish a hypothetical prediction from a measured population statistic. If a numerical example uses a notional fleet or synthetic data, it must not appear in an operator's work package as a measured site result. For any policy comparison, repeat the calculation using at least two plausible ranges for its most uncertain input and report whether the choice changes.

### Distinguish data from decisions

A probability is an input to a decision rather than a decision by itself. Two alternatives with equal failure probability can lead to different responses when consequences, restoration time and regulatory obligations are different.

## 3. Where the model can fail

A theoretically effective task may be impractical due to unsafe access, inability to isolate equipment, or inadequate measurement repeatability.

An important diagnostic practice is to seek evidence against the simplest explanation. A repair which temporarily restores output can disguise an uncorrected design, installation or operating error. If the apparent rate improves after a maintenance change, normalize against exposure and examine whether production load, weather, equipment population or reporting conventions changed in the same period. Correlation between a signal and a failure does not establish that intervening on the signal will prevent the failure.

The operational consequence of a bad assumption depends on the equipment. For an ordinary production asset it may mean excess inventory or a costly breakdown. For a safety-critical plant it can mean loss of containment, personnel exposure, service failure or violation of required inspection obligations. Use the teaching result only for understanding; site-specific decisions need competent hazard review, current standards, supplier instructions, physical verification and appropriate approval.

### Keep the operational objective in view

A metric is useful when it changes a decision that helps deliver service. Additional data collection should therefore answer a concrete question: whether to inspect, redesign, change stocking policy, add monitoring or accept an explicitly bounded residual risk.

## 4. Engineering investigation: from model to evidence

**Field prompt.** Choose between condition monitoring, scheduled replacement, failure finding, redesign and run-to-failure for four specified failure modes.

Connect this task to the unit study: Analyze a repeated centrifugal-pump seal leak. Build a chronology, preserve damaged parts, classify conditions, and use an evidence-versus-hypothesis table. The expected notebook output is concrete: Deliver a FMEA and an incident report containing verified observations, competing hypotheses, causal testing and effectiveness criteria. Include a sketch, a table of unknowns and an explicit statement of what observation would reverse the initial hypothesis. A useful investigation records the condition before repair, retains component photographs when safe, notes firmware and calibration versions where relevant, and documents any temporary bypass. Explain how the conclusion would be independently reproduced by another analyst.

**Proposed procedure.** First obtain permission and confirm the relevant safe isolation and operating boundaries; never open energized or pressurized equipment for a classroom exercise. Second use a published sampling interval or an explicit study protocol. Third capture raw data with units, timestamps and event codes before cleaning or filtering them. Fourth run a simple hand calculation and cross-check it with a separate implementation. Fifth evaluate sensitivity to one omitted mechanism, one measurement bias and one uncertain input. Sixth record the proposed action, owner, estimated restoration impact and a verification measure that will be checked after implementation.

A reliable result can be modest. It may show that two alternatives cannot yet be distinguished, that a missing event time prevents statistical estimation or that extra inspection has poor coverage. Reporting these limitations is preferable to manufacturing precision. For plant-level application, specify which person may authorize a shutdown, restart or alteration of protection logic; a textbook exercise never supplies that authorization.

## 5. Exercises and instructor checkpoints

1. **Definitions.** Define the physical or functional event involved in **reliability-centered maintenance decisions**. Give its observable boundary and one alternative definition that would change the counted population.
2. **Quantification.** Use the relation `If P-F interval has a conservative estimate of 12 days, a proposed 30-day inspection cannot reliably find the warning in that window.` with a consistent assumed dataset of your own. Show all units and at least one limiting-case check.
3. **Sensitivity.** Change the most uncertain nonzero input by ±20% where physically meaningful. Compare the output and decide whether the maintenance choice is robust.
4. **Counterexample.** Explain precisely why the following limitation matters: A theoretically effective task may be impractical due to unsafe access, inability to isolate equipment, or inadequate measurement repeatability.
5. **Application.** Choose between condition monitoring, scheduled replacement, failure finding, redesign and run-to-failure for four specified failure modes. Supply an evidence table with at least three observations and mark each entry as measured, supplied by a source, or synthetic.

**Self-check guidance.** A correct response identifies the function, model, assumptions, arithmetic, consequence and plausible falsification. The numeric exercise should be reproducible from the student's displayed inputs. The sensitivity response should not silently vary an independent parameter if two inputs are physically coupled. The field task should end with an evidence request or a testable action rather than a generic recommendation to “do maintenance.”

## 6. Connections to the wider curriculum

This topic interacts with earlier units through lifetime probability, state restoration, operating mechanisms and cost. When proposing a spare or a maintenance interval, ask how it changes both the frequency of failures and the length of lost service. When proposing a sensor, ask how often it produces a useful warning and how the organization responds. An effective recommendation uses the smallest set of credible assumptions needed for the stated decision and explains the circumstances under which its simplified formula would stop being useful.

**Source-reading exercise.** Compare the language of your model with the NIST reliability handbook or the NASA reliability-centered maintenance material listed in the references. Do not reproduce external texts; use the primary source to check the meaning of the statistical term or maintenance method, then describe the limitation in your own words.


---

# Unit 04 · Lesson 03 — FRACAS and effective corrective actions

**Learning goal.** Explain the core engineering statement, calculate a clearly bounded example, challenge at least one assumption and propose a measurable action. This material is an educational draft, not an authority for equipment acceptance.

## 1. Concept and technical meaning

Failure Reporting, Analysis and Corrective Action Systems track events from initial report through containment, analysis, action, verification and recurrence monitoring. A work order closed after part replacement is not proof that the defect mechanism is resolved. Traceability is essential when the same failure repeats.

The useful starting question is **“What physical or service event am I modeling?”** Place the studied item within the unit's central objective: A useful failure analysis distinguishes observed symptom, functional failure, failure mode, physical mechanism and systemic cause. FMEA is a structured screening technique, not a guarantee of safety; rankings depend on scales and judgement. Root-cause methods must be anchored in retained evidence and causal tests. A numerical value only becomes an engineering claim when the mission duration, operating conditions, item state and decision boundary are specified. If the equipment is repaired between events, decide whether the model starts a new life or continues to represent accumulated degradation. When data are drawn from multiple installations, check whether load, age, ambient environment and maintenance practice are comparable.

### Keep the physical mechanism visible

An apparent trend in a chart is evidence about recorded variables, not automatically the explanation of a component failure. Ask which loads, contamination pathways, temperatures, controls, maintenance practices or environmental stresses could produce the observed pattern.

A professional worksheet for **fracas and effective corrective actions** should preserve the original event definition and the raw denominator used in the calculation. Build a simple diagram that traces the studied input to a measured output. Label its arrows as measured relationships, physical assumptions or hypothetical causal mechanisms. This keeps the numerical calculation from silently becoming proof of a mechanism that has not been investigated.

## 2. Governing relation and derivation checks

**Primary relation:** `Recurrence proportion after a corrective-action date = repeated qualifying events / exposure in the defined follow-up window; comparisons require comparable exposure.`

The relation should first be read in words and translated into a dimensional statement. Identify which quantities are probabilities, time or cycle measures, rates, costs, loads, engineering scores or empirical indicators. If an input is a probability, its feasible interval is from zero to one; if it is an event intensity, it must be nonnegative and accompanied by a unit such as failures per operating hour. The output should be interpreted at the same stated boundary and over the same mission or reporting period as its inputs.

**Reasoning sequence.** (i) Define the asset and the function; (ii) write all inputs and their units; (iii) choose the simplest physically defensible model; (iv) perform the computation using an independent check; (v) compare the result with limiting cases; (vi) state uncertainty and model boundaries before recommending maintenance. For example, the limit of a no-failure event probability as an assumed event rate approaches zero should be consistent with ordinary experience. A result outside its physically possible range suggests either an arithmetic fault, incompatible units or a model used outside its assumptions.

**Worked engineering example.** Three motor failures occur after a cooling fan redesign. Investigators should compare load, ambient temperature, ventilation blockage and repair history before judging whether the redesign worked.

After evaluating the arithmetic, report what the result means and—equally important—what it does not mean. Distinguish a hypothetical prediction from a measured population statistic. If a numerical example uses a notional fleet or synthetic data, it must not appear in an operator's work package as a measured site result. For any policy comparison, repeat the calculation using at least two plausible ranges for its most uncertain input and report whether the choice changes.

### Audit model assumptions

Every model has a region in which its assumptions make sense. Before using an equation in a recommendation, check units, boundary, independence assumptions, the way failures are counted, and whether repair changes the modeled population.

## 3. Where the model can fail

A reduction in failure count after an upgrade may simply reflect a shorter operating period or production slowdown; normalize by exposure.

An important diagnostic practice is to seek evidence against the simplest explanation. A repair which temporarily restores output can disguise an uncorrected design, installation or operating error. If the apparent rate improves after a maintenance change, normalize against exposure and examine whether production load, weather, equipment population or reporting conventions changed in the same period. Correlation between a signal and a failure does not establish that intervening on the signal will prevent the failure.

The operational consequence of a bad assumption depends on the equipment. For an ordinary production asset it may mean excess inventory or a costly breakdown. For a safety-critical plant it can mean loss of containment, personnel exposure, service failure or violation of required inspection obligations. Use the teaching result only for understanding; site-specific decisions need competent hazard review, current standards, supplier instructions, physical verification and appropriate approval.

### Make uncertainty actionable

The practical response to missing information is usually a low-cost measurement, a conservative bound or a controlled trial. Sensitivity analysis exposes which uncertain assumption is capable of reversing a recommendation.

## 4. Engineering investigation: from model to evidence

**Field prompt.** Draft a FRACAS ticket with traceable evidence links and a test that could falsify the proposed root cause.

Connect this task to the unit study: Analyze a repeated centrifugal-pump seal leak. Build a chronology, preserve damaged parts, classify conditions, and use an evidence-versus-hypothesis table. The expected notebook output is concrete: Deliver a FMEA and an incident report containing verified observations, competing hypotheses, causal testing and effectiveness criteria. Include a sketch, a table of unknowns and an explicit statement of what observation would reverse the initial hypothesis. A useful investigation records the condition before repair, retains component photographs when safe, notes firmware and calibration versions where relevant, and documents any temporary bypass. Explain how the conclusion would be independently reproduced by another analyst.

**Proposed procedure.** First obtain permission and confirm the relevant safe isolation and operating boundaries; never open energized or pressurized equipment for a classroom exercise. Second use a published sampling interval or an explicit study protocol. Third capture raw data with units, timestamps and event codes before cleaning or filtering them. Fourth run a simple hand calculation and cross-check it with a separate implementation. Fifth evaluate sensitivity to one omitted mechanism, one measurement bias and one uncertain input. Sixth record the proposed action, owner, estimated restoration impact and a verification measure that will be checked after implementation.

A reliable result can be modest. It may show that two alternatives cannot yet be distinguished, that a missing event time prevents statistical estimation or that extra inspection has poor coverage. Reporting these limitations is preferable to manufacturing precision. For plant-level application, specify which person may authorize a shutdown, restart or alteration of protection logic; a textbook exercise never supplies that authorization.

## 5. Exercises and instructor checkpoints

1. **Definitions.** Define the physical or functional event involved in **fracas and effective corrective actions**. Give its observable boundary and one alternative definition that would change the counted population.
2. **Quantification.** Use the relation `Recurrence proportion after a corrective-action date = repeated qualifying events / exposure in the defined follow-up window; comparisons require comparable exposure.` with a consistent assumed dataset of your own. Show all units and at least one limiting-case check.
3. **Sensitivity.** Change the most uncertain nonzero input by ±20% where physically meaningful. Compare the output and decide whether the maintenance choice is robust.
4. **Counterexample.** Explain precisely why the following limitation matters: A reduction in failure count after an upgrade may simply reflect a shorter operating period or production slowdown; normalize by exposure.
5. **Application.** Draft a FRACAS ticket with traceable evidence links and a test that could falsify the proposed root cause. Supply an evidence table with at least three observations and mark each entry as measured, supplied by a source, or synthetic.

**Self-check guidance.** A correct response identifies the function, model, assumptions, arithmetic, consequence and plausible falsification. The numeric exercise should be reproducible from the student's displayed inputs. The sensitivity response should not silently vary an independent parameter if two inputs are physically coupled. The field task should end with an evidence request or a testable action rather than a generic recommendation to “do maintenance.”

## 6. Connections to the wider curriculum

This topic interacts with earlier units through lifetime probability, state restoration, operating mechanisms and cost. When proposing a spare or a maintenance interval, ask how it changes both the frequency of failures and the length of lost service. When proposing a sensor, ask how often it produces a useful warning and how the organization responds. An effective recommendation uses the smallest set of credible assumptions needed for the stated decision and explains the circumstances under which its simplified formula would stop being useful.

**Source-reading exercise.** Compare the language of your model with the NIST reliability handbook or the NASA reliability-centered maintenance material listed in the references. Do not reproduce external texts; use the primary source to check the meaning of the statistical term or maintenance method, then describe the limitation in your own words.


---

# Unit 04 · Lesson 04 — Physics of failure: fatigue, wear and corrosion

**Learning goal.** Explain the core engineering statement, calculate a clearly bounded example, challenge at least one assumption and propose a measurable action. This material is an educational draft, not an authority for equipment acceptance.

## 1. Concept and technical meaning

Physical degradation often accumulates through crack growth, surface contact, chemical attack or thermal cycling. Statistical fitting can describe failure times but the physics identifies which design or maintenance changes act on causal pathways. Distinguish fatigue initiation, propagation, fracture and post-failure artifacts.

The useful starting question is **“What physical or service event am I modeling?”** Place the studied item within the unit's central objective: A useful failure analysis distinguishes observed symptom, functional failure, failure mode, physical mechanism and systemic cause. FMEA is a structured screening technique, not a guarantee of safety; rankings depend on scales and judgement. Root-cause methods must be anchored in retained evidence and causal tests. A numerical value only becomes an engineering claim when the mission duration, operating conditions, item state and decision boundary are specified. If the equipment is repaired between events, decide whether the model starts a new life or continues to represent accumulated degradation. When data are drawn from multiple installations, check whether load, age, ambient environment and maintenance practice are comparable.

### Separate requirement from measurement

An engineer should be able to state the acceptance requirement before seeing the measurement. Otherwise thresholds tend to move after results are known. Preserve the original requirement, report any exception and obtain authorized approval for changes.

A professional worksheet for **physics of failure: fatigue, wear and corrosion** should preserve the original event definition and the raw denominator used in the calculation. Build a simple diagram that traces the studied input to a measured output. Label its arrows as measured relationships, physical assumptions or hypothetical causal mechanisms. This keeps the numerical calculation from silently becoming proof of a mechanism that has not been investigated.

## 2. Governing relation and derivation checks

**Primary relation:** `For high-cycle fatigue an illustrative Basquin relation may take σ_a=C N^b with b<0 within its applicable material regime.`

The relation should first be read in words and translated into a dimensional statement. Identify which quantities are probabilities, time or cycle measures, rates, costs, loads, engineering scores or empirical indicators. If an input is a probability, its feasible interval is from zero to one; if it is an event intensity, it must be nonnegative and accompanied by a unit such as failures per operating hour. The output should be interpreted at the same stated boundary and over the same mission or reporting period as its inputs.

**Reasoning sequence.** (i) Define the asset and the function; (ii) write all inputs and their units; (iii) choose the simplest physically defensible model; (iv) perform the computation using an independent check; (v) compare the result with limiting cases; (vi) state uncertainty and model boundaries before recommending maintenance. For example, the limit of a no-failure event probability as an assumed event rate approaches zero should be consistent with ordinary experience. A result outside its physically possible range suggests either an arithmetic fault, incompatible units or a model used outside its assumptions.

**Worked engineering example.** A shaft suffering reversed bending near a keyway may fail after many cycles although static stress remains below yield. Inspections must consider crack accessibility and detectable size.

After evaluating the arithmetic, report what the result means and—equally important—what it does not mean. Distinguish a hypothetical prediction from a measured population statistic. If a numerical example uses a notional fleet or synthetic data, it must not appear in an operator's work package as a measured site result. For any policy comparison, repeat the calculation using at least two plausible ranges for its most uncertain input and report whether the choice changes.

### Keep the operational objective in view

A metric is useful when it changes a decision that helps deliver service. Additional data collection should therefore answer a concrete question: whether to inspect, redesign, change stocking policy, add monitoring or accept an explicitly bounded residual risk.

## 3. Where the model can fail

An S–N fit from laboratory specimens should not be used without correction for surface condition, size, temperature, mean stress and scatter.

An important diagnostic practice is to seek evidence against the simplest explanation. A repair which temporarily restores output can disguise an uncorrected design, installation or operating error. If the apparent rate improves after a maintenance change, normalize against exposure and examine whether production load, weather, equipment population or reporting conventions changed in the same period. Correlation between a signal and a failure does not establish that intervening on the signal will prevent the failure.

The operational consequence of a bad assumption depends on the equipment. For an ordinary production asset it may mean excess inventory or a costly breakdown. For a safety-critical plant it can mean loss of containment, personnel exposure, service failure or violation of required inspection obligations. Use the teaching result only for understanding; site-specific decisions need competent hazard review, current standards, supplier instructions, physical verification and appropriate approval.

### Plan a falsification test

A good explanation can be disproved. State an observation that would contradict the proposed failure mechanism, and arrange measurements so another engineer could reach an independent conclusion rather than merely agreeing with the initial diagnosis.

## 4. Engineering investigation: from model to evidence

**Field prompt.** Create an evidence plan to separate corrosion fatigue from overload and lubrication-related wear.

Connect this task to the unit study: A gearbox trips on high vibration. Replacing the bearing may restore function without explaining whether inadequate lubrication, assembly preload, shaft misalignment or a faulty sensor caused the event. A durable corrective action must target the tested mechanism and verify it later. The expected notebook output is concrete: Deliver a FMEA and an incident report containing verified observations, competing hypotheses, causal testing and effectiveness criteria. Include a sketch, a table of unknowns and an explicit statement of what observation would reverse the initial hypothesis. A useful investigation records the condition before repair, retains component photographs when safe, notes firmware and calibration versions where relevant, and documents any temporary bypass. Explain how the conclusion would be independently reproduced by another analyst.

**Proposed procedure.** First obtain permission and confirm the relevant safe isolation and operating boundaries; never open energized or pressurized equipment for a classroom exercise. Second use a published sampling interval or an explicit study protocol. Third capture raw data with units, timestamps and event codes before cleaning or filtering them. Fourth run a simple hand calculation and cross-check it with a separate implementation. Fifth evaluate sensitivity to one omitted mechanism, one measurement bias and one uncertain input. Sixth record the proposed action, owner, estimated restoration impact and a verification measure that will be checked after implementation.

A reliable result can be modest. It may show that two alternatives cannot yet be distinguished, that a missing event time prevents statistical estimation or that extra inspection has poor coverage. Reporting these limitations is preferable to manufacturing precision. For plant-level application, specify which person may authorize a shutdown, restart or alteration of protection logic; a textbook exercise never supplies that authorization.

## 5. Exercises and instructor checkpoints

1. **Definitions.** Define the physical or functional event involved in **physics of failure: fatigue, wear and corrosion**. Give its observable boundary and one alternative definition that would change the counted population.
2. **Quantification.** Use the relation `For high-cycle fatigue an illustrative Basquin relation may take σ_a=C N^b with b<0 within its applicable material regime.` with a consistent assumed dataset of your own. Show all units and at least one limiting-case check.
3. **Sensitivity.** Change the most uncertain nonzero input by ±20% where physically meaningful. Compare the output and decide whether the maintenance choice is robust.
4. **Counterexample.** Explain precisely why the following limitation matters: An S–N fit from laboratory specimens should not be used without correction for surface condition, size, temperature, mean stress and scatter.
5. **Application.** Create an evidence plan to separate corrosion fatigue from overload and lubrication-related wear. Supply an evidence table with at least three observations and mark each entry as measured, supplied by a source, or synthetic.

**Self-check guidance.** A correct response identifies the function, model, assumptions, arithmetic, consequence and plausible falsification. The numeric exercise should be reproducible from the student's displayed inputs. The sensitivity response should not silently vary an independent parameter if two inputs are physically coupled. The field task should end with an evidence request or a testable action rather than a generic recommendation to “do maintenance.”

## 6. Connections to the wider curriculum

This topic interacts with earlier units through lifetime probability, state restoration, operating mechanisms and cost. When proposing a spare or a maintenance interval, ask how it changes both the frequency of failures and the length of lost service. When proposing a sensor, ask how often it produces a useful warning and how the organization responds. An effective recommendation uses the smallest set of credible assumptions needed for the stated decision and explains the circumstances under which its simplified formula would stop being useful.

**Source-reading exercise.** Compare the language of your model with the NIST reliability handbook or the NASA reliability-centered maintenance material listed in the references. Do not reproduce external texts; use the primary source to check the meaning of the statistical term or maintenance method, then describe the limitation in your own words.


---

# Unit 04 · Lesson 05 — Human factors and diagnostic errors

**Learning goal.** Explain the core engineering statement, calculate a clearly bounded example, challenge at least one assumption and propose a measurable action. This material is an educational draft, not an authority for equipment acceptance.

## 1. Concept and technical meaning

Reliability is influenced by design, installation, operation, maintenance and organizational practices. Poor labeling, inaccessible fittings and ambiguous alarms create error-likely conditions. Investigations should address system design rather than stopping at “operator error.”

The useful starting question is **“What physical or service event am I modeling?”** Place the studied item within the unit's central objective: A useful failure analysis distinguishes observed symptom, functional failure, failure mode, physical mechanism and systemic cause. FMEA is a structured screening technique, not a guarantee of safety; rankings depend on scales and judgement. Root-cause methods must be anchored in retained evidence and causal tests. A numerical value only becomes an engineering claim when the mission duration, operating conditions, item state and decision boundary are specified. If the equipment is repaired between events, decide whether the model starts a new life or continues to represent accumulated degradation. When data are drawn from multiple installations, check whether load, age, ambient environment and maintenance practice are comparable.

### Distinguish data from decisions

A probability is an input to a decision rather than a decision by itself. Two alternatives with equal failure probability can lead to different responses when consequences, restoration time and regulatory obligations are different.

A professional worksheet for **human factors and diagnostic errors** should preserve the original event definition and the raw denominator used in the calculation. Build a simple diagram that traces the studied input to a measured output. Label its arrows as measured relationships, physical assumptions or hypothetical causal mechanisms. This keeps the numerical calculation from silently becoming proof of a mechanism that has not been investigated.

## 2. Governing relation and derivation checks

**Primary relation:** `A diagnostic test has false-positive and false-negative rates; predictive value also depends on prevalence.`

The relation should first be read in words and translated into a dimensional statement. Identify which quantities are probabilities, time or cycle measures, rates, costs, loads, engineering scores or empirical indicators. If an input is a probability, its feasible interval is from zero to one; if it is an event intensity, it must be nonnegative and accompanied by a unit such as failures per operating hour. The output should be interpreted at the same stated boundary and over the same mission or reporting period as its inputs.

**Reasoning sequence.** (i) Define the asset and the function; (ii) write all inputs and their units; (iii) choose the simplest physically defensible model; (iv) perform the computation using an independent check; (v) compare the result with limiting cases; (vi) state uncertainty and model boundaries before recommending maintenance. For example, the limit of a no-failure event probability as an assumed event rate approaches zero should be consistent with ordinary experience. A result outside its physically possible range suggests either an arithmetic fault, incompatible units or a model used outside its assumptions.

**Worked engineering example.** When a rare failure has prevalence 1%, even a test with 95% sensitivity and 95% specificity gives many false alarms relative to true detections: PPV≈16.1%.

After evaluating the arithmetic, report what the result means and—equally important—what it does not mean. Distinguish a hypothetical prediction from a measured population statistic. If a numerical example uses a notional fleet or synthetic data, it must not appear in an operator's work package as a measured site result. For any policy comparison, repeat the calculation using at least two plausible ranges for its most uncertain input and report whether the choice changes.

### Make uncertainty actionable

The practical response to missing information is usually a low-cost measurement, a conservative bound or a controlled trial. Sensitivity analysis exposes which uncertain assumption is capable of reversing a recommendation.

## 3. Where the model can fail

An alarm may be technically accurate but ineffective if the control-room interface buries it among frequent nuisance alarms.

An important diagnostic practice is to seek evidence against the simplest explanation. A repair which temporarily restores output can disguise an uncorrected design, installation or operating error. If the apparent rate improves after a maintenance change, normalize against exposure and examine whether production load, weather, equipment population or reporting conventions changed in the same period. Correlation between a signal and a failure does not establish that intervening on the signal will prevent the failure.

The operational consequence of a bad assumption depends on the equipment. For an ordinary production asset it may mean excess inventory or a costly breakdown. For a safety-critical plant it can mean loss of containment, personnel exposure, service failure or violation of required inspection obligations. Use the teaching result only for understanding; site-specific decisions need competent hazard review, current standards, supplier instructions, physical verification and appropriate approval.

### Define the denominator

Write down the reference population and the interval across which the observation has meaning. An event per machine-day differs from an event per operating hour if production schedules differ. A simulation that silently uses an assumed denominator produces a neat but potentially false comparison.

## 4. Engineering investigation: from model to evidence

**Field prompt.** Map a repair procedure and identify steps vulnerable to incorrect part, polarity, torque or isolation state.

Connect this task to the unit study: Analyze a repeated centrifugal-pump seal leak. Build a chronology, preserve damaged parts, classify conditions, and use an evidence-versus-hypothesis table. The expected notebook output is concrete: Deliver a FMEA and an incident report containing verified observations, competing hypotheses, causal testing and effectiveness criteria. Include a sketch, a table of unknowns and an explicit statement of what observation would reverse the initial hypothesis. A useful investigation records the condition before repair, retains component photographs when safe, notes firmware and calibration versions where relevant, and documents any temporary bypass. Explain how the conclusion would be independently reproduced by another analyst.

**Proposed procedure.** First obtain permission and confirm the relevant safe isolation and operating boundaries; never open energized or pressurized equipment for a classroom exercise. Second use a published sampling interval or an explicit study protocol. Third capture raw data with units, timestamps and event codes before cleaning or filtering them. Fourth run a simple hand calculation and cross-check it with a separate implementation. Fifth evaluate sensitivity to one omitted mechanism, one measurement bias and one uncertain input. Sixth record the proposed action, owner, estimated restoration impact and a verification measure that will be checked after implementation.

A reliable result can be modest. It may show that two alternatives cannot yet be distinguished, that a missing event time prevents statistical estimation or that extra inspection has poor coverage. Reporting these limitations is preferable to manufacturing precision. For plant-level application, specify which person may authorize a shutdown, restart or alteration of protection logic; a textbook exercise never supplies that authorization.

## 5. Exercises and instructor checkpoints

1. **Definitions.** Define the physical or functional event involved in **human factors and diagnostic errors**. Give its observable boundary and one alternative definition that would change the counted population.
2. **Quantification.** Use the relation `A diagnostic test has false-positive and false-negative rates; predictive value also depends on prevalence.` with a consistent assumed dataset of your own. Show all units and at least one limiting-case check.
3. **Sensitivity.** Change the most uncertain nonzero input by ±20% where physically meaningful. Compare the output and decide whether the maintenance choice is robust.
4. **Counterexample.** Explain precisely why the following limitation matters: An alarm may be technically accurate but ineffective if the control-room interface buries it among frequent nuisance alarms.
5. **Application.** Map a repair procedure and identify steps vulnerable to incorrect part, polarity, torque or isolation state. Supply an evidence table with at least three observations and mark each entry as measured, supplied by a source, or synthetic.

**Self-check guidance.** A correct response identifies the function, model, assumptions, arithmetic, consequence and plausible falsification. The numeric exercise should be reproducible from the student's displayed inputs. The sensitivity response should not silently vary an independent parameter if two inputs are physically coupled. The field task should end with an evidence request or a testable action rather than a generic recommendation to “do maintenance.”

## 6. Connections to the wider curriculum

This topic interacts with earlier units through lifetime probability, state restoration, operating mechanisms and cost. When proposing a spare or a maintenance interval, ask how it changes both the frequency of failures and the length of lost service. When proposing a sensor, ask how often it produces a useful warning and how the organization responds. An effective recommendation uses the smallest set of credible assumptions needed for the stated decision and explains the circumstances under which its simplified formula would stop being useful.

**Source-reading exercise.** Compare the language of your model with the NIST reliability handbook or the NASA reliability-centered maintenance material listed in the references. Do not reproduce external texts; use the primary source to check the meaning of the statistical term or maintenance method, then describe the limitation in your own words.


---

