# Unit 01: Reliability Engineering Fundamentals

**Course Code**: ERM 401 · **Level**: Advanced Undergraduate Engineering

## Unit Overview & Physical Foundations

This comprehensive university textbook unit covers the theoretical framework, physical modeling, mathematical governing equations, and engineering applications of **Reliability Engineering Fundamentals**.

# Unit 01 · Lesson 01 — Functions, requirements and the meaning of failure

**Learning goal.** Explain the core engineering statement, calculate a clearly bounded example, challenge at least one assumption and propose a measurable action. This material is an educational draft, not an authority for equipment acceptance.

## 1. Concept and technical meaning

A functional failure occurs when required performance is no longer met, not necessarily when a component has broken. The boundary of a refrigeration skid includes the compressor, protections, sensors, supply power and control handshakes; an energy trip is part of its functional story.

The useful starting question is **“What physical or service event am I modeling?”** Place the studied item within the unit's central objective: Define the operating function, failure boundary, exposure, mission and consequence before calculating a failure probability. A repaired item, a one-time mission, and a continuously operating fleet demand different metrics. Start from the asset boundary and the customer service that must be preserved. A numerical value only becomes an engineering claim when the mission duration, operating conditions, item state and decision boundary are specified. If the equipment is repaired between events, decide whether the model starts a new life or continues to represent accumulated degradation. When data are drawn from multiple installations, check whether load, age, ambient environment and maintenance practice are comparable.

### Define the denominator

Write down the reference population and the interval across which the observation has meaning. An event per machine-day differs from an event per operating hour if production schedules differ. A simulation that silently uses an assumed denominator produces a neat but potentially false comparison.

A professional worksheet for **functions, requirements and the meaning of failure** should preserve the original event definition and the raw denominator used in the calculation. Build a simple diagram that traces the studied input to a measured output. Label its arrows as measured relationships, physical assumptions or hypothetical causal mechanisms. This keeps the numerical calculation from silently becoming proof of a mechanism that has not been investigated.

## 2. Governing relation and derivation checks

**Primary relation:** `Define F=1 if delivered performance violates a specified limit during the mission; an indicator is not automatically a probability.`

The relation should first be read in words and translated into a dimensional statement. Identify which quantities are probabilities, time or cycle measures, rates, costs, loads, engineering scores or empirical indicators. If an input is a probability, its feasible interval is from zero to one; if it is an event intensity, it must be nonnegative and accompanied by a unit such as failures per operating hour. The output should be interpreted at the same stated boundary and over the same mission or reporting period as its inputs.

**Reasoning sequence.** (i) Define the asset and the function; (ii) write all inputs and their units; (iii) choose the simplest physically defensible model; (iv) perform the computation using an independent check; (v) compare the result with limiting cases; (vi) state uncertainty and model boundaries before recommending maintenance. For example, the limit of a no-failure event probability as an assumed event rate approaches zero should be consistent with ordinary experience. A result outside its physically possible range suggests either an arithmetic fault, incompatible units or a model used outside its assumptions.

**Worked engineering example.** A pump must deliver at least 90 cubic metres per hour. In a 12-hour observation, it spends 10 hours above the requirement and 2 hours below. Functional service fraction is 10/12=0.8333, but this is not a lifetime reliability estimate.

After evaluating the arithmetic, report what the result means and—equally important—what it does not mean. Distinguish a hypothetical prediction from a measured population statistic. If a numerical example uses a notional fleet or synthetic data, it must not appear in an operator's work package as a measured site result. For any policy comparison, repeat the calculation using at least two plausible ranges for its most uncertain input and report whether the choice changes.

### Distinguish data from decisions

A probability is an input to a decision rather than a decision by itself. Two alternatives with equal failure probability can lead to different responses when consequences, restoration time and regulatory obligations are different.

## 3. Where the model can fail

A temporary derating permitted in the operating specification is not a failure; exceeding a safety pressure limit is a failure even if flow is still available.

An important diagnostic practice is to seek evidence against the simplest explanation. A repair which temporarily restores output can disguise an uncorrected design, installation or operating error. If the apparent rate improves after a maintenance change, normalize against exposure and examine whether production load, weather, equipment population or reporting conventions changed in the same period. Correlation between a signal and a failure does not establish that intervening on the signal will prevent the failure.

The operational consequence of a bad assumption depends on the equipment. For an ordinary production asset it may mean excess inventory or a costly breakdown. For a safety-critical plant it can mean loss of containment, personnel exposure, service failure or violation of required inspection obligations. Use the teaching result only for understanding; site-specific decisions need competent hazard review, current standards, supplier instructions, physical verification and appropriate approval.

### Keep the operational objective in view

A metric is useful when it changes a decision that helps deliver service. Additional data collection should therefore answer a concrete question: whether to inspect, redesign, change stocking policy, add monitoring or accept an explicitly bounded residual risk.

## 4. Engineering investigation: from model to evidence

**Field prompt.** Write two failure definitions for an emergency pump: loss of flow on demand and dangerous leakage. List the separate consequences.

Connect this task to the unit study: A packaging line has nominal capacity 1,000 cartons per hour. A machine running at 600 cartons per hour may be functioning mechanically but has failed a customer-defined throughput requirement; a stopped spare machine may not have failed its standby function. An engineer therefore writes a measurable function statement rather than classifying every stoppage as equipment failure. The expected notebook output is concrete: Deliver a function register: system boundary, service requirement, duty cycle, outage classes, evidence source, and the decision owner. Include a sketch, a table of unknowns and an explicit statement of what observation would reverse the initial hypothesis. A useful investigation records the condition before repair, retains component photographs when safe, notes firmware and calibration versions where relevant, and documents any temporary bypass. Explain how the conclusion would be independently reproduced by another analyst.

**Proposed procedure.** First obtain permission and confirm the relevant safe isolation and operating boundaries; never open energized or pressurized equipment for a classroom exercise. Second use a published sampling interval or an explicit study protocol. Third capture raw data with units, timestamps and event codes before cleaning or filtering them. Fourth run a simple hand calculation and cross-check it with a separate implementation. Fifth evaluate sensitivity to one omitted mechanism, one measurement bias and one uncertain input. Sixth record the proposed action, owner, estimated restoration impact and a verification measure that will be checked after implementation.

A reliable result can be modest. It may show that two alternatives cannot yet be distinguished, that a missing event time prevents statistical estimation or that extra inspection has poor coverage. Reporting these limitations is preferable to manufacturing precision. For plant-level application, specify which person may authorize a shutdown, restart or alteration of protection logic; a textbook exercise never supplies that authorization.

## 5. Exercises and instructor checkpoints

1. **Definitions.** Define the physical or functional event involved in **functions, requirements and the meaning of failure**. Give its observable boundary and one alternative definition that would change the counted population.
2. **Quantification.** Use the relation `Define F=1 if delivered performance violates a specified limit during the mission; an indicator is not automatically a probability.` with a consistent assumed dataset of your own. Show all units and at least one limiting-case check.
3. **Sensitivity.** Change the most uncertain nonzero input by ±20% where physically meaningful. Compare the output and decide whether the maintenance choice is robust.
4. **Counterexample.** Explain precisely why the following limitation matters: A temporary derating permitted in the operating specification is not a failure; exceeding a safety pressure limit is a failure even if flow is still available.
5. **Application.** Write two failure definitions for an emergency pump: loss of flow on demand and dangerous leakage. List the separate consequences. Supply an evidence table with at least three observations and mark each entry as measured, supplied by a source, or synthetic.

**Self-check guidance.** A correct response identifies the function, model, assumptions, arithmetic, consequence and plausible falsification. The numeric exercise should be reproducible from the student's displayed inputs. The sensitivity response should not silently vary an independent parameter if two inputs are physically coupled. The field task should end with an evidence request or a testable action rather than a generic recommendation to “do maintenance.”

## 6. Connections to the wider curriculum

This topic interacts with earlier units through lifetime probability, state restoration, operating mechanisms and cost. When proposing a spare or a maintenance interval, ask how it changes both the frequency of failures and the length of lost service. When proposing a sensor, ask how often it produces a useful warning and how the organization responds. An effective recommendation uses the smallest set of credible assumptions needed for the stated decision and explains the circumstances under which its simplified formula would stop being useful.

**Source-reading exercise.** Compare the language of your model with the NIST reliability handbook or the NASA reliability-centered maintenance material listed in the references. Do not reproduce external texts; use the primary source to check the meaning of the statistical term or maintenance method, then describe the limitation in your own words.


---

# Unit 01 · Lesson 02 — Reliability, availability and maintainability

**Learning goal.** Explain the core engineering statement, calculate a clearly bounded example, challenge at least one assumption and propose a measurable action. This material is an educational draft, not an authority for equipment acceptance.

## 1. Concept and technical meaning

Reliability concerns survival without failure over a specified time or mission. Availability concerns being operational at an instant or fraction of time, including restorations. Maintainability describes the probability or effort of completing restoration under defined conditions. The same machine can have high reliability but poor availability if each rare failure requires months of repair.

The useful starting question is **“What physical or service event am I modeling?”** Place the studied item within the unit's central objective: Define the operating function, failure boundary, exposure, mission and consequence before calculating a failure probability. A repaired item, a one-time mission, and a continuously operating fleet demand different metrics. Start from the asset boundary and the customer service that must be preserved. A numerical value only becomes an engineering claim when the mission duration, operating conditions, item state and decision boundary are specified. If the equipment is repaired between events, decide whether the model starts a new life or continues to represent accumulated degradation. When data are drawn from multiple installations, check whether load, age, ambient environment and maintenance practice are comparable.

### Keep the physical mechanism visible

An apparent trend in a chart is evidence about recorded variables, not automatically the explanation of a component failure. Ask which loads, contamination pathways, temperatures, controls, maintenance practices or environmental stresses could produce the observed pattern.

A professional worksheet for **reliability, availability and maintainability** should preserve the original event definition and the raw denominator used in the calculation. Build a simple diagram that traces the studied input to a measured output. Label its arrows as measured relationships, physical assumptions or hypothetical causal mechanisms. This keeps the numerical calculation from silently becoming proof of a mechanism that has not been investigated.

## 2. Governing relation and derivation checks

**Primary relation:** `For a steady two-state idealized repair process, A=MTBF/(MTBF+MTTR).`

The relation should first be read in words and translated into a dimensional statement. Identify which quantities are probabilities, time or cycle measures, rates, costs, loads, engineering scores or empirical indicators. If an input is a probability, its feasible interval is from zero to one; if it is an event intensity, it must be nonnegative and accompanied by a unit such as failures per operating hour. The output should be interpreted at the same stated boundary and over the same mission or reporting period as its inputs.

**Reasoning sequence.** (i) Define the asset and the function; (ii) write all inputs and their units; (iii) choose the simplest physically defensible model; (iv) perform the computation using an independent check; (v) compare the result with limiting cases; (vi) state uncertainty and model boundaries before recommending maintenance. For example, the limit of a no-failure event probability as an assumed event rate approaches zero should be consistent with ordinary experience. A result outside its physically possible range suggests either an arithmetic fault, incompatible units or a model used outside its assumptions.

**Worked engineering example.** A repairable conveyor averages 500 running hours between functional failures and eight hours active repair. Ideal inherent availability is 500/508=0.9843, before logistics and waiting losses.

After evaluating the arithmetic, report what the result means and—equally important—what it does not mean. Distinguish a hypothetical prediction from a measured population statistic. If a numerical example uses a notional fleet or synthetic data, it must not appear in an operator's work package as a measured site result. For any policy comparison, repeat the calculation using at least two plausible ranges for its most uncertain input and report whether the choice changes.

### Audit model assumptions

Every model has a region in which its assumptions make sense. Before using an equation in a recommendation, check units, boundary, independence assumptions, the way failures are counted, and whether repair changes the modeled population.

## 3. Where the model can fail

MTBF is not a guaranteed life; using total calendar time rather than operating exposure biases comparisons when machines run different schedules.

An important diagnostic practice is to seek evidence against the simplest explanation. A repair which temporarily restores output can disguise an uncorrected design, installation or operating error. If the apparent rate improves after a maintenance change, normalize against exposure and examine whether production load, weather, equipment population or reporting conventions changed in the same period. Correlation between a signal and a failure does not establish that intervening on the signal will prevent the failure.

The operational consequence of a bad assumption depends on the equipment. For an ordinary production asset it may mean excess inventory or a costly breakdown. For a safety-critical plant it can mean loss of containment, personnel exposure, service failure or violation of required inspection obligations. Use the teaching result only for understanding; site-specific decisions need competent hazard review, current standards, supplier instructions, physical verification and appropriate approval.

### Make uncertainty actionable

The practical response to missing information is usually a low-cost measurement, a conservative bound or a controlled trial. Sensitivity analysis exposes which uncertain assumption is capable of reversing a recommendation.

## 4. Engineering investigation: from model to evidence

**Field prompt.** Compare an asset with MTBF 200 hours and MTTR 2 hours to one with MTBF 800 hours and MTTR 24 hours; explain why both metrics matter.

Connect this task to the unit study: Specify a pump train providing 100 m³/h at the required differential head for 8,000 hours per year; distinguish performance loss, protective trip, scheduled outage and leak. Interview the operator and safety representative about what is unsafe to restart. The expected notebook output is concrete: Deliver a function register: system boundary, service requirement, duty cycle, outage classes, evidence source, and the decision owner. Include a sketch, a table of unknowns and an explicit statement of what observation would reverse the initial hypothesis. A useful investigation records the condition before repair, retains component photographs when safe, notes firmware and calibration versions where relevant, and documents any temporary bypass. Explain how the conclusion would be independently reproduced by another analyst.

**Proposed procedure.** First obtain permission and confirm the relevant safe isolation and operating boundaries; never open energized or pressurized equipment for a classroom exercise. Second use a published sampling interval or an explicit study protocol. Third capture raw data with units, timestamps and event codes before cleaning or filtering them. Fourth run a simple hand calculation and cross-check it with a separate implementation. Fifth evaluate sensitivity to one omitted mechanism, one measurement bias and one uncertain input. Sixth record the proposed action, owner, estimated restoration impact and a verification measure that will be checked after implementation.

A reliable result can be modest. It may show that two alternatives cannot yet be distinguished, that a missing event time prevents statistical estimation or that extra inspection has poor coverage. Reporting these limitations is preferable to manufacturing precision. For plant-level application, specify which person may authorize a shutdown, restart or alteration of protection logic; a textbook exercise never supplies that authorization.

## 5. Exercises and instructor checkpoints

1. **Definitions.** Define the physical or functional event involved in **reliability, availability and maintainability**. Give its observable boundary and one alternative definition that would change the counted population.
2. **Quantification.** Use the relation `For a steady two-state idealized repair process, A=MTBF/(MTBF+MTTR).` with a consistent assumed dataset of your own. Show all units and at least one limiting-case check.
3. **Sensitivity.** Change the most uncertain nonzero input by ±20% where physically meaningful. Compare the output and decide whether the maintenance choice is robust.
4. **Counterexample.** Explain precisely why the following limitation matters: MTBF is not a guaranteed life; using total calendar time rather than operating exposure biases comparisons when machines run different schedules.
5. **Application.** Compare an asset with MTBF 200 hours and MTTR 2 hours to one with MTBF 800 hours and MTTR 24 hours; explain why both metrics matter. Supply an evidence table with at least three observations and mark each entry as measured, supplied by a source, or synthetic.

**Self-check guidance.** A correct response identifies the function, model, assumptions, arithmetic, consequence and plausible falsification. The numeric exercise should be reproducible from the student's displayed inputs. The sensitivity response should not silently vary an independent parameter if two inputs are physically coupled. The field task should end with an evidence request or a testable action rather than a generic recommendation to “do maintenance.”

## 6. Connections to the wider curriculum

This topic interacts with earlier units through lifetime probability, state restoration, operating mechanisms and cost. When proposing a spare or a maintenance interval, ask how it changes both the frequency of failures and the length of lost service. When proposing a sensor, ask how often it produces a useful warning and how the organization responds. An effective recommendation uses the smallest set of credible assumptions needed for the stated decision and explains the circumstances under which its simplified formula would stop being useful.

**Source-reading exercise.** Compare the language of your model with the NIST reliability handbook or the NASA reliability-centered maintenance material listed in the references. Do not reproduce external texts; use the primary source to check the meaning of the statistical term or maintenance method, then describe the limitation in your own words.


---

# Unit 01 · Lesson 03 — Mission time and exposure normalization

**Learning goal.** Explain the core engineering statement, calculate a clearly bounded example, challenge at least one assumption and propose a measurable action. This material is an educational draft, not an authority for equipment acceptance.

## 1. Concept and technical meaning

Exposure is the accumulation of time or cycles for which the relevant failure mechanism can act. Calendar time, engine hours, starts, thermal cycles, loaded revolutions and kilometers can support different inferences. Combining them into one unqualified time measure is dangerous when the duty mix varies.

The useful starting question is **“What physical or service event am I modeling?”** Place the studied item within the unit's central objective: Define the operating function, failure boundary, exposure, mission and consequence before calculating a failure probability. A repaired item, a one-time mission, and a continuously operating fleet demand different metrics. Start from the asset boundary and the customer service that must be preserved. A numerical value only becomes an engineering claim when the mission duration, operating conditions, item state and decision boundary are specified. If the equipment is repaired between events, decide whether the model starts a new life or continues to represent accumulated degradation. When data are drawn from multiple installations, check whether load, age, ambient environment and maintenance practice are comparable.

### Separate requirement from measurement

An engineer should be able to state the acceptance requirement before seeing the measurement. Otherwise thresholds tend to move after results are known. Preserve the original requirement, report any exception and obtain authorized approval for changes.

A professional worksheet for **mission time and exposure normalization** should preserve the original event definition and the raw denominator used in the calculation. Build a simple diagram that traces the studied input to a measured output. Label its arrows as measured relationships, physical assumptions or hypothetical causal mechanisms. This keeps the numerical calculation from silently becoming proof of a mechanism that has not been investigated.

## 2. Governing relation and derivation checks

**Primary relation:** `Event rate estimate λhat=N_fail/T_exposure under a constant-hazard, independent-event approximation.`

The relation should first be read in words and translated into a dimensional statement. Identify which quantities are probabilities, time or cycle measures, rates, costs, loads, engineering scores or empirical indicators. If an input is a probability, its feasible interval is from zero to one; if it is an event intensity, it must be nonnegative and accompanied by a unit such as failures per operating hour. The output should be interpreted at the same stated boundary and over the same mission or reporting period as its inputs.

**Reasoning sequence.** (i) Define the asset and the function; (ii) write all inputs and their units; (iii) choose the simplest physically defensible model; (iv) perform the computation using an independent check; (v) compare the result with limiting cases; (vi) state uncertainty and model boundaries before recommending maintenance. For example, the limit of a no-failure event probability as an assumed event rate approaches zero should be consistent with ordinary experience. A result outside its physically possible range suggests either an arithmetic fault, incompatible units or a model used outside its assumptions.

**Worked engineering example.** A pump fleet reports six failures over 60,000 operating hours: 1e-4 failures per operating hour. A second fleet with equal failures over 20,000 hours has three times the estimated event frequency, but uncertainty remains large.

After evaluating the arithmetic, report what the result means and—equally important—what it does not mean. Distinguish a hypothetical prediction from a measured population statistic. If a numerical example uses a notional fleet or synthetic data, it must not appear in an operator's work package as a measured site result. For any policy comparison, repeat the calculation using at least two plausible ranges for its most uncertain input and report whether the choice changes.

### Keep the operational objective in view

A metric is useful when it changes a decision that helps deliver service. Additional data collection should therefore answer a concrete question: whether to inspect, redesign, change stocking policy, add monitoring or accept an explicitly bounded residual risk.

## 3. Where the model can fail

One asset counted through repeated repairs contributes recurring events; a one-shot component contributes first failure. Do not mix these without an explicit process model.

An important diagnostic practice is to seek evidence against the simplest explanation. A repair which temporarily restores output can disguise an uncorrected design, installation or operating error. If the apparent rate improves after a maintenance change, normalize against exposure and examine whether production load, weather, equipment population or reporting conventions changed in the same period. Correlation between a signal and a failure does not establish that intervening on the signal will prevent the failure.

The operational consequence of a bad assumption depends on the equipment. For an ordinary production asset it may mean excess inventory or a costly breakdown. For a safety-critical plant it can mean loss of containment, personnel exposure, service failure or violation of required inspection obligations. Use the teaching result only for understanding; site-specific decisions need competent hazard review, current standards, supplier instructions, physical verification and appropriate approval.

### Plan a falsification test

A good explanation can be disproved. State an observation that would contradict the proposed failure mechanism, and arrange measurements so another engineer could reach an independent conclusion rather than merely agreeing with the initial diagnosis.

## 4. Engineering investigation: from model to evidence

**Field prompt.** Design a data form recording start, stop, load, cycles, failure category and return-to-service time.

Connect this task to the unit study: Specify a pump train providing 100 m³/h at the required differential head for 8,000 hours per year; distinguish performance loss, protective trip, scheduled outage and leak. Interview the operator and safety representative about what is unsafe to restart. The expected notebook output is concrete: Deliver a function register: system boundary, service requirement, duty cycle, outage classes, evidence source, and the decision owner. Include a sketch, a table of unknowns and an explicit statement of what observation would reverse the initial hypothesis. A useful investigation records the condition before repair, retains component photographs when safe, notes firmware and calibration versions where relevant, and documents any temporary bypass. Explain how the conclusion would be independently reproduced by another analyst.

**Proposed procedure.** First obtain permission and confirm the relevant safe isolation and operating boundaries; never open energized or pressurized equipment for a classroom exercise. Second use a published sampling interval or an explicit study protocol. Third capture raw data with units, timestamps and event codes before cleaning or filtering them. Fourth run a simple hand calculation and cross-check it with a separate implementation. Fifth evaluate sensitivity to one omitted mechanism, one measurement bias and one uncertain input. Sixth record the proposed action, owner, estimated restoration impact and a verification measure that will be checked after implementation.

A reliable result can be modest. It may show that two alternatives cannot yet be distinguished, that a missing event time prevents statistical estimation or that extra inspection has poor coverage. Reporting these limitations is preferable to manufacturing precision. For plant-level application, specify which person may authorize a shutdown, restart or alteration of protection logic; a textbook exercise never supplies that authorization.

## 5. Exercises and instructor checkpoints

1. **Definitions.** Define the physical or functional event involved in **mission time and exposure normalization**. Give its observable boundary and one alternative definition that would change the counted population.
2. **Quantification.** Use the relation `Event rate estimate λhat=N_fail/T_exposure under a constant-hazard, independent-event approximation.` with a consistent assumed dataset of your own. Show all units and at least one limiting-case check.
3. **Sensitivity.** Change the most uncertain nonzero input by ±20% where physically meaningful. Compare the output and decide whether the maintenance choice is robust.
4. **Counterexample.** Explain precisely why the following limitation matters: One asset counted through repeated repairs contributes recurring events; a one-shot component contributes first failure. Do not mix these without an explicit process model.
5. **Application.** Design a data form recording start, stop, load, cycles, failure category and return-to-service time. Supply an evidence table with at least three observations and mark each entry as measured, supplied by a source, or synthetic.

**Self-check guidance.** A correct response identifies the function, model, assumptions, arithmetic, consequence and plausible falsification. The numeric exercise should be reproducible from the student's displayed inputs. The sensitivity response should not silently vary an independent parameter if two inputs are physically coupled. The field task should end with an evidence request or a testable action rather than a generic recommendation to “do maintenance.”

## 6. Connections to the wider curriculum

This topic interacts with earlier units through lifetime probability, state restoration, operating mechanisms and cost. When proposing a spare or a maintenance interval, ask how it changes both the frequency of failures and the length of lost service. When proposing a sensor, ask how often it produces a useful warning and how the organization responds. An effective recommendation uses the smallest set of credible assumptions needed for the stated decision and explains the circumstances under which its simplified formula would stop being useful.

**Source-reading exercise.** Compare the language of your model with the NIST reliability handbook or the NASA reliability-centered maintenance material listed in the references. Do not reproduce external texts; use the primary source to check the meaning of the statistical term or maintenance method, then describe the limitation in your own words.


---

# Unit 01 · Lesson 04 — Failure modes, consequences and criticality

**Learning goal.** Explain the core engineering statement, calculate a clearly bounded example, challenge at least one assumption and propose a measurable action. This material is an educational draft, not an authority for equipment acceptance.

## 1. Concept and technical meaning

A failure mode describes the local manner in which required function is lost; a mechanism describes physical causal processes; consequence describes resulting harm or loss. A vibration alarm is an observation, not a root cause. Criticality must consider safety, environmental damage, service interruption and recovery capability, not just replacement price.

The useful starting question is **“What physical or service event am I modeling?”** Place the studied item within the unit's central objective: Define the operating function, failure boundary, exposure, mission and consequence before calculating a failure probability. A repaired item, a one-time mission, and a continuously operating fleet demand different metrics. Start from the asset boundary and the customer service that must be preserved. A numerical value only becomes an engineering claim when the mission duration, operating conditions, item state and decision boundary are specified. If the equipment is repaired between events, decide whether the model starts a new life or continues to represent accumulated degradation. When data are drawn from multiple installations, check whether load, age, ambient environment and maintenance practice are comparable.

### Distinguish data from decisions

A probability is an input to a decision rather than a decision by itself. Two alternatives with equal failure probability can lead to different responses when consequences, restoration time and regulatory obligations are different.

A professional worksheet for **failure modes, consequences and criticality** should preserve the original event definition and the raw denominator used in the calculation. Build a simple diagram that traces the studied input to a measured output. Label its arrows as measured relationships, physical assumptions or hypothetical causal mechanisms. This keeps the numerical calculation from silently becoming proof of a mechanism that has not been investigated.

## 2. Governing relation and derivation checks

**Primary relation:** `Expected direct loss in a simplified risk model = event probability × consequence cost; this is not a complete treatment of life safety.`

The relation should first be read in words and translated into a dimensional statement. Identify which quantities are probabilities, time or cycle measures, rates, costs, loads, engineering scores or empirical indicators. If an input is a probability, its feasible interval is from zero to one; if it is an event intensity, it must be nonnegative and accompanied by a unit such as failures per operating hour. The output should be interpreted at the same stated boundary and over the same mission or reporting period as its inputs.

**Reasoning sequence.** (i) Define the asset and the function; (ii) write all inputs and their units; (iii) choose the simplest physically defensible model; (iv) perform the computation using an independent check; (v) compare the result with limiting cases; (vi) state uncertainty and model boundaries before recommending maintenance. For example, the limit of a no-failure event probability as an assumed event rate approaches zero should be consistent with ordinary experience. A result outside its physically possible range suggests either an arithmetic fault, incompatible units or a model used outside its assumptions.

**Worked engineering example.** A cheap sensor can be critical if it silently disables overtemperature protection, while an expensive noncritical cosmetic component may have little operational risk.

After evaluating the arithmetic, report what the result means and—equally important—what it does not mean. Distinguish a hypothetical prediction from a measured population statistic. If a numerical example uses a notional fleet or synthetic data, it must not appear in an operator's work package as a measured site result. For any policy comparison, repeat the calculation using at least two plausible ranges for its most uncertain input and report whether the choice changes.

### Make uncertainty actionable

The practical response to missing information is usually a low-cost measurement, a conservative bound or a controlled trial. Sensitivity analysis exposes which uncertain assumption is capable of reversing a recommendation.

## 3. Where the model can fail

Multiplying arbitrary severity, occurrence and detectability rankings produces an ordinal screening score, not a calibrated probability or financial expectation.

An important diagnostic practice is to seek evidence against the simplest explanation. A repair which temporarily restores output can disguise an uncorrected design, installation or operating error. If the apparent rate improves after a maintenance change, normalize against exposure and examine whether production load, weather, equipment population or reporting conventions changed in the same period. Correlation between a signal and a failure does not establish that intervening on the signal will prevent the failure.

The operational consequence of a bad assumption depends on the equipment. For an ordinary production asset it may mean excess inventory or a costly breakdown. For a safety-critical plant it can mean loss of containment, personnel exposure, service failure or violation of required inspection obligations. Use the teaching result only for understanding; site-specific decisions need competent hazard review, current standards, supplier instructions, physical verification and appropriate approval.

### Define the denominator

Write down the reference population and the interval across which the observation has meaning. An event per machine-day differs from an event per operating hour if production schedules differ. A simulation that silently uses an assumed denominator produces a neat but potentially false comparison.

## 4. Engineering investigation: from model to evidence

**Field prompt.** Build a consequence matrix for a bearing seize, shaft leak, nuisance trip and protective-device failure.

Connect this task to the unit study: A packaging line has nominal capacity 1,000 cartons per hour. A machine running at 600 cartons per hour may be functioning mechanically but has failed a customer-defined throughput requirement; a stopped spare machine may not have failed its standby function. An engineer therefore writes a measurable function statement rather than classifying every stoppage as equipment failure. The expected notebook output is concrete: Deliver a function register: system boundary, service requirement, duty cycle, outage classes, evidence source, and the decision owner. Include a sketch, a table of unknowns and an explicit statement of what observation would reverse the initial hypothesis. A useful investigation records the condition before repair, retains component photographs when safe, notes firmware and calibration versions where relevant, and documents any temporary bypass. Explain how the conclusion would be independently reproduced by another analyst.

**Proposed procedure.** First obtain permission and confirm the relevant safe isolation and operating boundaries; never open energized or pressurized equipment for a classroom exercise. Second use a published sampling interval or an explicit study protocol. Third capture raw data with units, timestamps and event codes before cleaning or filtering them. Fourth run a simple hand calculation and cross-check it with a separate implementation. Fifth evaluate sensitivity to one omitted mechanism, one measurement bias and one uncertain input. Sixth record the proposed action, owner, estimated restoration impact and a verification measure that will be checked after implementation.

A reliable result can be modest. It may show that two alternatives cannot yet be distinguished, that a missing event time prevents statistical estimation or that extra inspection has poor coverage. Reporting these limitations is preferable to manufacturing precision. For plant-level application, specify which person may authorize a shutdown, restart or alteration of protection logic; a textbook exercise never supplies that authorization.

## 5. Exercises and instructor checkpoints

1. **Definitions.** Define the physical or functional event involved in **failure modes, consequences and criticality**. Give its observable boundary and one alternative definition that would change the counted population.
2. **Quantification.** Use the relation `Expected direct loss in a simplified risk model = event probability × consequence cost; this is not a complete treatment of life safety.` with a consistent assumed dataset of your own. Show all units and at least one limiting-case check.
3. **Sensitivity.** Change the most uncertain nonzero input by ±20% where physically meaningful. Compare the output and decide whether the maintenance choice is robust.
4. **Counterexample.** Explain precisely why the following limitation matters: Multiplying arbitrary severity, occurrence and detectability rankings produces an ordinal screening score, not a calibrated probability or financial expectation.
5. **Application.** Build a consequence matrix for a bearing seize, shaft leak, nuisance trip and protective-device failure. Supply an evidence table with at least three observations and mark each entry as measured, supplied by a source, or synthetic.

**Self-check guidance.** A correct response identifies the function, model, assumptions, arithmetic, consequence and plausible falsification. The numeric exercise should be reproducible from the student's displayed inputs. The sensitivity response should not silently vary an independent parameter if two inputs are physically coupled. The field task should end with an evidence request or a testable action rather than a generic recommendation to “do maintenance.”

## 6. Connections to the wider curriculum

This topic interacts with earlier units through lifetime probability, state restoration, operating mechanisms and cost. When proposing a spare or a maintenance interval, ask how it changes both the frequency of failures and the length of lost service. When proposing a sensor, ask how often it produces a useful warning and how the organization responds. An effective recommendation uses the smallest set of credible assumptions needed for the stated decision and explains the circumstances under which its simplified formula would stop being useful.

**Source-reading exercise.** Compare the language of your model with the NIST reliability handbook or the NASA reliability-centered maintenance material listed in the references. Do not reproduce external texts; use the primary source to check the meaning of the statistical term or maintenance method, then describe the limitation in your own words.


---

# Unit 01 · Lesson 05 — Reliability requirements and allocation

**Learning goal.** Explain the core engineering statement, calculate a clearly bounded example, challenge at least one assumption and propose a measurable action. This material is an educational draft, not an authority for equipment acceptance.

## 1. Concept and technical meaning

A valid reliability requirement defines item boundary, function, load profile, mission duration, confidence or evidence basis and permitted interventions. Allocating a system target to subsystems through algebra is only the beginning; feasibility, dependencies and uncertainty must be tested.

The useful starting question is **“What physical or service event am I modeling?”** Place the studied item within the unit's central objective: Define the operating function, failure boundary, exposure, mission and consequence before calculating a failure probability. A repaired item, a one-time mission, and a continuously operating fleet demand different metrics. Start from the asset boundary and the customer service that must be preserved. A numerical value only becomes an engineering claim when the mission duration, operating conditions, item state and decision boundary are specified. If the equipment is repaired between events, decide whether the model starts a new life or continues to represent accumulated degradation. When data are drawn from multiple installations, check whether load, age, ambient environment and maintenance practice are comparable.

### Audit model assumptions

Every model has a region in which its assumptions make sense. Before using an equation in a recommendation, check units, boundary, independence assumptions, the way failures are counted, and whether repair changes the modeled population.

A professional worksheet for **reliability requirements and allocation** should preserve the original event definition and the raw denominator used in the calculation. Build a simple diagram that traces the studied input to a measured output. Label its arrows as measured relationships, physical assumptions or hypothetical causal mechanisms. This keeps the numerical calculation from silently becoming proof of a mechanism that has not been investigated.

## 2. Governing relation and derivation checks

**Primary relation:** `For n equal independent series elements, target element reliability r=R_system^(1/n).`

The relation should first be read in words and translated into a dimensional statement. Identify which quantities are probabilities, time or cycle measures, rates, costs, loads, engineering scores or empirical indicators. If an input is a probability, its feasible interval is from zero to one; if it is an event intensity, it must be nonnegative and accompanied by a unit such as failures per operating hour. The output should be interpreted at the same stated boundary and over the same mission or reporting period as its inputs.

**Reasoning sequence.** (i) Define the asset and the function; (ii) write all inputs and their units; (iii) choose the simplest physically defensible model; (iv) perform the computation using an independent check; (v) compare the result with limiting cases; (vi) state uncertainty and model boundaries before recommending maintenance. For example, the limit of a no-failure event probability as an assumed event rate approaches zero should be consistent with ordinary experience. A result outside its physically possible range suggests either an arithmetic fault, incompatible units or a model used outside its assumptions.

**Worked engineering example.** A four-element independent series train with required R=0.90 for a mission implies r=0.90^(1/4)≈0.9740 per element when equal allocation is assumed.

After evaluating the arithmetic, report what the result means and—equally important—what it does not mean. Distinguish a hypothetical prediction from a measured population statistic. If a numerical example uses a notional fleet or synthetic data, it must not appear in an operator's work package as a measured site result. For any policy comparison, repeat the calculation using at least two plausible ranges for its most uncertain input and report whether the choice changes.

### Plan a falsification test

A good explanation can be disproved. State an observation that would contradict the proposed failure mechanism, and arrange measurements so another engineer could reach an independent conclusion rather than merely agreeing with the initial diagnosis.

## 3. Where the model can fail

Equal allocation does not match engineering reality when components have different maturities, thermal environments or replacement options; nor does algebra handle shared utilities.

An important diagnostic practice is to seek evidence against the simplest explanation. A repair which temporarily restores output can disguise an uncorrected design, installation or operating error. If the apparent rate improves after a maintenance change, normalize against exposure and examine whether production load, weather, equipment population or reporting conventions changed in the same period. Correlation between a signal and a failure does not establish that intervening on the signal will prevent the failure.

The operational consequence of a bad assumption depends on the equipment. For an ordinary production asset it may mean excess inventory or a costly breakdown. For a safety-critical plant it can mean loss of containment, personnel exposure, service failure or violation of required inspection obligations. Use the teaching result only for understanding; site-specific decisions need competent hazard review, current standards, supplier instructions, physical verification and appropriate approval.

### Keep the physical mechanism visible

An apparent trend in a chart is evidence about recorded variables, not automatically the explanation of a component failure. Ask which loads, contamination pathways, temperatures, controls, maintenance practices or environmental stresses could produce the observed pattern.

## 4. Engineering investigation: from model to evidence

**Field prompt.** Draft a traceable requirement for a standby hydraulic actuator and three measurable acceptance criteria.

Connect this task to the unit study: Specify a pump train providing 100 m³/h at the required differential head for 8,000 hours per year; distinguish performance loss, protective trip, scheduled outage and leak. Interview the operator and safety representative about what is unsafe to restart. The expected notebook output is concrete: Deliver a function register: system boundary, service requirement, duty cycle, outage classes, evidence source, and the decision owner. Include a sketch, a table of unknowns and an explicit statement of what observation would reverse the initial hypothesis. A useful investigation records the condition before repair, retains component photographs when safe, notes firmware and calibration versions where relevant, and documents any temporary bypass. Explain how the conclusion would be independently reproduced by another analyst.

**Proposed procedure.** First obtain permission and confirm the relevant safe isolation and operating boundaries; never open energized or pressurized equipment for a classroom exercise. Second use a published sampling interval or an explicit study protocol. Third capture raw data with units, timestamps and event codes before cleaning or filtering them. Fourth run a simple hand calculation and cross-check it with a separate implementation. Fifth evaluate sensitivity to one omitted mechanism, one measurement bias and one uncertain input. Sixth record the proposed action, owner, estimated restoration impact and a verification measure that will be checked after implementation.

A reliable result can be modest. It may show that two alternatives cannot yet be distinguished, that a missing event time prevents statistical estimation or that extra inspection has poor coverage. Reporting these limitations is preferable to manufacturing precision. For plant-level application, specify which person may authorize a shutdown, restart or alteration of protection logic; a textbook exercise never supplies that authorization.

## 5. Exercises and instructor checkpoints

1. **Definitions.** Define the physical or functional event involved in **reliability requirements and allocation**. Give its observable boundary and one alternative definition that would change the counted population.
2. **Quantification.** Use the relation `For n equal independent series elements, target element reliability r=R_system^(1/n).` with a consistent assumed dataset of your own. Show all units and at least one limiting-case check.
3. **Sensitivity.** Change the most uncertain nonzero input by ±20% where physically meaningful. Compare the output and decide whether the maintenance choice is robust.
4. **Counterexample.** Explain precisely why the following limitation matters: Equal allocation does not match engineering reality when components have different maturities, thermal environments or replacement options; nor does algebra handle shared utilities.
5. **Application.** Draft a traceable requirement for a standby hydraulic actuator and three measurable acceptance criteria. Supply an evidence table with at least three observations and mark each entry as measured, supplied by a source, or synthetic.

**Self-check guidance.** A correct response identifies the function, model, assumptions, arithmetic, consequence and plausible falsification. The numeric exercise should be reproducible from the student's displayed inputs. The sensitivity response should not silently vary an independent parameter if two inputs are physically coupled. The field task should end with an evidence request or a testable action rather than a generic recommendation to “do maintenance.”

## 6. Connections to the wider curriculum

This topic interacts with earlier units through lifetime probability, state restoration, operating mechanisms and cost. When proposing a spare or a maintenance interval, ask how it changes both the frequency of failures and the length of lost service. When proposing a sensor, ask how often it produces a useful warning and how the organization responds. An effective recommendation uses the smallest set of credible assumptions needed for the stated decision and explains the circumstances under which its simplified formula would stop being useful.

**Source-reading exercise.** Compare the language of your model with the NIST reliability handbook or the NASA reliability-centered maintenance material listed in the references. Do not reproduce external texts; use the primary source to check the meaning of the statistical term or maintenance method, then describe the limitation in your own words.


---

