# Unit 06: Maintenance Data, Spares and Economic Optimization

**Course Code**: ERM 406 · **Level**: Advanced Undergraduate Engineering

## Unit Overview & Physical Foundations

This comprehensive university textbook unit covers the theoretical framework, physical modeling, mathematical governing equations, and engineering applications of **Maintenance Data, Spares and Economic Optimization**.

# Unit 06 · Lesson 01 — CMMS records, data governance and KPIs

**Learning goal.** Explain the core engineering statement, calculate a clearly bounded example, challenge at least one assumption and propose a measurable action. This material is an educational draft, not an authority for equipment acceptance.

## 1. Concept and technical meaning

A computerized maintenance management system becomes analytically useful only when hierarchy, location, operating time, failure codes, work types and cost definitions are consistent. Text fields alone are hard to compare; rigid codes alone can erase crucial nuance. Balance both, and retain the audit trail of changed records.

The useful starting question is **“What physical or service event am I modeling?”** Place the studied item within the unit's central objective: Maintenance information systems fail when people use inconsistent failure codes, do not record exposure, and cannot reconcile repair labor with calendar downtime. Spare provisioning must reflect demand uncertainty, lead time, criticality and obsolescence; a single inventory formula cannot substitute for risk judgement. A numerical value only becomes an engineering claim when the mission duration, operating conditions, item state and decision boundary are specified. If the equipment is repaired between events, decide whether the model starts a new life or continues to represent accumulated degradation. When data are drawn from multiple installations, check whether load, age, ambient environment and maintenance practice are comparable.

### Keep the physical mechanism visible

An apparent trend in a chart is evidence about recorded variables, not automatically the explanation of a component failure. Ask which loads, contamination pathways, temperatures, controls, maintenance practices or environmental stresses could produce the observed pattern.

A professional worksheet for **cmms records, data governance and kpis** should preserve the original event definition and the raw denominator used in the calculation. Build a simple diagram that traces the studied input to a measured output. Label its arrows as measured relationships, physical assumptions or hypothetical causal mechanisms. This keeps the numerical calculation from silently becoming proof of a mechanism that has not been investigated.

## 2. Governing relation and derivation checks

**Primary relation:** `Failure rate per 1,000 operating hours=1000×N_failures/operating_hours for a chosen event definition.`

The relation should first be read in words and translated into a dimensional statement. Identify which quantities are probabilities, time or cycle measures, rates, costs, loads, engineering scores or empirical indicators. If an input is a probability, its feasible interval is from zero to one; if it is an event intensity, it must be nonnegative and accompanied by a unit such as failures per operating hour. The output should be interpreted at the same stated boundary and over the same mission or reporting period as its inputs.

**Reasoning sequence.** (i) Define the asset and the function; (ii) write all inputs and their units; (iii) choose the simplest physically defensible model; (iv) perform the computation using an independent check; (v) compare the result with limiting cases; (vi) state uncertainty and model boundaries before recommending maintenance. For example, the limit of a no-failure event probability as an assumed event rate approaches zero should be consistent with ordinary experience. A result outside its physically possible range suggests either an arithmetic fault, incompatible units or a model used outside its assumptions.

**Worked engineering example.** A facility records eight unscheduled functional failures over 16,000 runtime hours, or 0.5 per 1,000 runtime hours. If one site excludes protective trips, direct comparison becomes invalid.

After evaluating the arithmetic, report what the result means and—equally important—what it does not mean. Distinguish a hypothetical prediction from a measured population statistic. If a numerical example uses a notional fleet or synthetic data, it must not appear in an operator's work package as a measured site result. For any policy comparison, repeat the calculation using at least two plausible ranges for its most uncertain input and report whether the choice changes.

### Audit model assumptions

Every model has a region in which its assumptions make sense. Before using an equation in a recommendation, check units, boundary, independence assumptions, the way failures are counted, and whether repair changes the modeled population.

## 3. Where the model can fail

Backfilling unknown failure reasons as “bearing fault” because the bearing was replaced creates confirmation bias and artificially high cause frequency.

An important diagnostic practice is to seek evidence against the simplest explanation. A repair which temporarily restores output can disguise an uncorrected design, installation or operating error. If the apparent rate improves after a maintenance change, normalize against exposure and examine whether production load, weather, equipment population or reporting conventions changed in the same period. Correlation between a signal and a failure does not establish that intervening on the signal will prevent the failure.

The operational consequence of a bad assumption depends on the equipment. For an ordinary production asset it may mean excess inventory or a costly breakdown. For a safety-critical plant it can mean loss of containment, personnel exposure, service failure or violation of required inspection obligations. Use the teaching result only for understanding; site-specific decisions need competent hazard review, current standards, supplier instructions, physical verification and appropriate approval.

### Make uncertainty actionable

The practical response to missing information is usually a low-cost measurement, a conservative bound or a controlled trial. Sensitivity analysis exposes which uncertain assumption is capable of reversing a recommendation.

## 4. Engineering investigation: from model to evidence

**Field prompt.** Design an asset hierarchy, required work-order fields and a monthly data-quality audit.

Connect this task to the unit study: A replacement motor has a three-week purchasing lead time. The practical outage duration may be days even when hands-on repair takes four hours. This difference determines both stock policy and the choice of reported maintainability metric. The expected notebook output is concrete: Deliver a master data standard, spare-parts risk register, cost scenario table, and set of leading and lagging KPIs. Include a sketch, a table of unknowns and an explicit statement of what observation would reverse the initial hypothesis. A useful investigation records the condition before repair, retains component photographs when safe, notes firmware and calibration versions where relevant, and documents any temporary bypass. Explain how the conclusion would be independently reproduced by another analyst.

**Proposed procedure.** First obtain permission and confirm the relevant safe isolation and operating boundaries; never open energized or pressurized equipment for a classroom exercise. Second use a published sampling interval or an explicit study protocol. Third capture raw data with units, timestamps and event codes before cleaning or filtering them. Fourth run a simple hand calculation and cross-check it with a separate implementation. Fifth evaluate sensitivity to one omitted mechanism, one measurement bias and one uncertain input. Sixth record the proposed action, owner, estimated restoration impact and a verification measure that will be checked after implementation.

A reliable result can be modest. It may show that two alternatives cannot yet be distinguished, that a missing event time prevents statistical estimation or that extra inspection has poor coverage. Reporting these limitations is preferable to manufacturing precision. For plant-level application, specify which person may authorize a shutdown, restart or alteration of protection logic; a textbook exercise never supplies that authorization.

## 5. Exercises and instructor checkpoints

1. **Definitions.** Define the physical or functional event involved in **cmms records, data governance and kpis**. Give its observable boundary and one alternative definition that would change the counted population.
2. **Quantification.** Use the relation `Failure rate per 1,000 operating hours=1000×N_failures/operating_hours for a chosen event definition.` with a consistent assumed dataset of your own. Show all units and at least one limiting-case check.
3. **Sensitivity.** Change the most uncertain nonzero input by ±20% where physically meaningful. Compare the output and decide whether the maintenance choice is robust.
4. **Counterexample.** Explain precisely why the following limitation matters: Backfilling unknown failure reasons as “bearing fault” because the bearing was replaced creates confirmation bias and artificially high cause frequency.
5. **Application.** Design an asset hierarchy, required work-order fields and a monthly data-quality audit. Supply an evidence table with at least three observations and mark each entry as measured, supplied by a source, or synthetic.

**Self-check guidance.** A correct response identifies the function, model, assumptions, arithmetic, consequence and plausible falsification. The numeric exercise should be reproducible from the student's displayed inputs. The sensitivity response should not silently vary an independent parameter if two inputs are physically coupled. The field task should end with an evidence request or a testable action rather than a generic recommendation to “do maintenance.”

## 6. Connections to the wider curriculum

This topic interacts with earlier units through lifetime probability, state restoration, operating mechanisms and cost. When proposing a spare or a maintenance interval, ask how it changes both the frequency of failures and the length of lost service. When proposing a sensor, ask how often it produces a useful warning and how the organization responds. An effective recommendation uses the smallest set of credible assumptions needed for the stated decision and explains the circumstances under which its simplified formula would stop being useful.

**Source-reading exercise.** Compare the language of your model with the NIST reliability handbook or the NASA reliability-centered maintenance material listed in the references. Do not reproduce external texts; use the primary source to check the meaning of the statistical term or maintenance method, then describe the limitation in your own words.


---

# Unit 06 · Lesson 02 — Spare part inventory and critical lead times

**Learning goal.** Explain the core engineering statement, calculate a clearly bounded example, challenge at least one assumption and propose a measurable action. This material is an educational draft, not an authority for equipment acceptance.

## 1. Concept and technical meaning

Spares bridge uncertain failure demand and replenishment lead time. The appropriate inventory depends on criticality, interchangeability, repair capability, purchasing risk and obsolescence. Expected demand alone underestimates exposure to an infrequent but long outage if the tail is important.

The useful starting question is **“What physical or service event am I modeling?”** Place the studied item within the unit's central objective: Maintenance information systems fail when people use inconsistent failure codes, do not record exposure, and cannot reconcile repair labor with calendar downtime. Spare provisioning must reflect demand uncertainty, lead time, criticality and obsolescence; a single inventory formula cannot substitute for risk judgement. A numerical value only becomes an engineering claim when the mission duration, operating conditions, item state and decision boundary are specified. If the equipment is repaired between events, decide whether the model starts a new life or continues to represent accumulated degradation. When data are drawn from multiple installations, check whether load, age, ambient environment and maintenance practice are comparable.

### Separate requirement from measurement

An engineer should be able to state the acceptance requirement before seeing the measurement. Otherwise thresholds tend to move after results are known. Preserve the original requirement, report any exception and obtain authorized approval for changes.

A professional worksheet for **spare part inventory and critical lead times** should preserve the original event definition and the raw denominator used in the calculation. Build a simple diagram that traces the studied input to a measured output. Label its arrows as measured relationships, physical assumptions or hypothetical causal mechanisms. This keeps the numerical calculation from silently becoming proof of a mechanism that has not been investigated.

## 2. Governing relation and derivation checks

**Primary relation:** `For Poisson demand with mean m during lead time, P(N<=k)=exp(-m)Σ_(j=0)^k m^j/j!.`

The relation should first be read in words and translated into a dimensional statement. Identify which quantities are probabilities, time or cycle measures, rates, costs, loads, engineering scores or empirical indicators. If an input is a probability, its feasible interval is from zero to one; if it is an event intensity, it must be nonnegative and accompanied by a unit such as failures per operating hour. The output should be interpreted at the same stated boundary and over the same mission or reporting period as its inputs.

**Reasoning sequence.** (i) Define the asset and the function; (ii) write all inputs and their units; (iii) choose the simplest physically defensible model; (iv) perform the computation using an independent check; (v) compare the result with limiting cases; (vi) state uncertainty and model boundaries before recommending maintenance. For example, the limit of a no-failure event probability as an assumed event rate approaches zero should be consistent with ordinary experience. A result outside its physically possible range suggests either an arithmetic fault, incompatible units or a model used outside its assumptions.

**Worked engineering example.** If expected demand during lead time is m=0.5, having one spare covers at most one demand with probability exp(-0.5)(1+0.5)=0.9098, leaving roughly 9% probability of two or more demands.

After evaluating the arithmetic, report what the result means and—equally important—what it does not mean. Distinguish a hypothetical prediction from a measured population statistic. If a numerical example uses a notional fleet or synthetic data, it must not appear in an operator's work package as a measured site result. For any policy comparison, repeat the calculation using at least two plausible ranges for its most uncertain input and report whether the choice changes.

### Keep the operational objective in view

A metric is useful when it changes a decision that helps deliver service. Additional data collection should therefore answer a concrete question: whether to inspect, redesign, change stocking policy, add monitoring or accept an explicitly bounded residual risk.

## 3. Where the model can fail

Demand events may cluster due to a bad production batch or harsh season; the Poisson model underestimates risk when failures are correlated.

An important diagnostic practice is to seek evidence against the simplest explanation. A repair which temporarily restores output can disguise an uncorrected design, installation or operating error. If the apparent rate improves after a maintenance change, normalize against exposure and examine whether production load, weather, equipment population or reporting conventions changed in the same period. Correlation between a signal and a failure does not establish that intervening on the signal will prevent the failure.

The operational consequence of a bad assumption depends on the equipment. For an ordinary production asset it may mean excess inventory or a costly breakdown. For a safety-critical plant it can mean loss of containment, personnel exposure, service failure or violation of required inspection obligations. Use the teaching result only for understanding; site-specific decisions need competent hazard review, current standards, supplier instructions, physical verification and appropriate approval.

### Plan a falsification test

A good explanation can be disproved. State an observation that would contradict the proposed failure mechanism, and arrange measurements so another engineer could reach an independent conclusion rather than merely agreeing with the initial diagnosis.

## 4. Engineering investigation: from model to evidence

**Field prompt.** Compare one spare, two spares and no local spares under purchase lead-time uncertainty and include storage risks.

Connect this task to the unit study: Compare stocking one critical drive at a remote water station with purchasing on demand. Use hypothetical failure frequency, lead time and holding cost, and vary the consequence of lost water supply. The expected notebook output is concrete: Deliver a master data standard, spare-parts risk register, cost scenario table, and set of leading and lagging KPIs. Include a sketch, a table of unknowns and an explicit statement of what observation would reverse the initial hypothesis. A useful investigation records the condition before repair, retains component photographs when safe, notes firmware and calibration versions where relevant, and documents any temporary bypass. Explain how the conclusion would be independently reproduced by another analyst.

**Proposed procedure.** First obtain permission and confirm the relevant safe isolation and operating boundaries; never open energized or pressurized equipment for a classroom exercise. Second use a published sampling interval or an explicit study protocol. Third capture raw data with units, timestamps and event codes before cleaning or filtering them. Fourth run a simple hand calculation and cross-check it with a separate implementation. Fifth evaluate sensitivity to one omitted mechanism, one measurement bias and one uncertain input. Sixth record the proposed action, owner, estimated restoration impact and a verification measure that will be checked after implementation.

A reliable result can be modest. It may show that two alternatives cannot yet be distinguished, that a missing event time prevents statistical estimation or that extra inspection has poor coverage. Reporting these limitations is preferable to manufacturing precision. For plant-level application, specify which person may authorize a shutdown, restart or alteration of protection logic; a textbook exercise never supplies that authorization.

## 5. Exercises and instructor checkpoints

1. **Definitions.** Define the physical or functional event involved in **spare part inventory and critical lead times**. Give its observable boundary and one alternative definition that would change the counted population.
2. **Quantification.** Use the relation `For Poisson demand with mean m during lead time, P(N<=k)=exp(-m)Σ_(j=0)^k m^j/j!.` with a consistent assumed dataset of your own. Show all units and at least one limiting-case check.
3. **Sensitivity.** Change the most uncertain nonzero input by ±20% where physically meaningful. Compare the output and decide whether the maintenance choice is robust.
4. **Counterexample.** Explain precisely why the following limitation matters: Demand events may cluster due to a bad production batch or harsh season; the Poisson model underestimates risk when failures are correlated.
5. **Application.** Compare one spare, two spares and no local spares under purchase lead-time uncertainty and include storage risks. Supply an evidence table with at least three observations and mark each entry as measured, supplied by a source, or synthetic.

**Self-check guidance.** A correct response identifies the function, model, assumptions, arithmetic, consequence and plausible falsification. The numeric exercise should be reproducible from the student's displayed inputs. The sensitivity response should not silently vary an independent parameter if two inputs are physically coupled. The field task should end with an evidence request or a testable action rather than a generic recommendation to “do maintenance.”

## 6. Connections to the wider curriculum

This topic interacts with earlier units through lifetime probability, state restoration, operating mechanisms and cost. When proposing a spare or a maintenance interval, ask how it changes both the frequency of failures and the length of lost service. When proposing a sensor, ask how often it produces a useful warning and how the organization responds. An effective recommendation uses the smallest set of credible assumptions needed for the stated decision and explains the circumstances under which its simplified formula would stop being useful.

**Source-reading exercise.** Compare the language of your model with the NIST reliability handbook or the NASA reliability-centered maintenance material listed in the references. Do not reproduce external texts; use the primary source to check the meaning of the statistical term or maintenance method, then describe the limitation in your own words.


---

# Unit 06 · Lesson 03 — Replacement versus repair decisions

**Learning goal.** Explain the core engineering statement, calculate a clearly bounded example, challenge at least one assumption and propose a measurable action. This material is an educational draft, not an authority for equipment acceptance.

## 1. Concept and technical meaning

Repair can restore function cheaply but leave aging mechanisms in place. Full replacement may reset life yet create commissioning and installation risk. Economic selection needs labor, downtime, spares, warranty, energy, disposal, safety and the opportunity cost of capital. A refurbishment claim requires post-repair acceptance evidence.

The useful starting question is **“What physical or service event am I modeling?”** Place the studied item within the unit's central objective: Maintenance information systems fail when people use inconsistent failure codes, do not record exposure, and cannot reconcile repair labor with calendar downtime. Spare provisioning must reflect demand uncertainty, lead time, criticality and obsolescence; a single inventory formula cannot substitute for risk judgement. A numerical value only becomes an engineering claim when the mission duration, operating conditions, item state and decision boundary are specified. If the equipment is repaired between events, decide whether the model starts a new life or continues to represent accumulated degradation. When data are drawn from multiple installations, check whether load, age, ambient environment and maintenance practice are comparable.

### Distinguish data from decisions

A probability is an input to a decision rather than a decision by itself. Two alternatives with equal failure probability can lead to different responses when consequences, restoration time and regulatory obligations are different.

A professional worksheet for **replacement versus repair decisions** should preserve the original event definition and the raw denominator used in the calculation. Build a simple diagram that traces the studied input to a measured output. Label its arrows as measured relationships, physical assumptions or hypothetical causal mechanisms. This keeps the numerical calculation from silently becoming proof of a mechanism that has not been investigated.

## 2. Governing relation and derivation checks

**Primary relation:** `Equivalent annualized cost can compare life-cycle alternatives with equal service objectives and a consistent discount rate.`

The relation should first be read in words and translated into a dimensional statement. Identify which quantities are probabilities, time or cycle measures, rates, costs, loads, engineering scores or empirical indicators. If an input is a probability, its feasible interval is from zero to one; if it is an event intensity, it must be nonnegative and accompanied by a unit such as failures per operating hour. The output should be interpreted at the same stated boundary and over the same mission or reporting period as its inputs.

**Reasoning sequence.** (i) Define the asset and the function; (ii) write all inputs and their units; (iii) choose the simplest physically defensible model; (iv) perform the computation using an independent check; (v) compare the result with limiting cases; (vi) state uncertainty and model boundaries before recommending maintenance. For example, the limit of a no-failure event probability as an assumed event rate approaches zero should be consistent with ordinary experience. A result outside its physically possible range suggests either an arithmetic fault, incompatible units or a model used outside its assumptions.

**Worked engineering example.** A repaired pump costs 2,000 today and is expected to incur 900 annual service cost; a replacement costs 8,000 and 300 annually. The least cost depends strongly on horizon, residual value and unplanned failure consequences.

After evaluating the arithmetic, report what the result means and—equally important—what it does not mean. Distinguish a hypothetical prediction from a measured population statistic. If a numerical example uses a notional fleet or synthetic data, it must not appear in an operator's work package as a measured site result. For any policy comparison, repeat the calculation using at least two plausible ranges for its most uncertain input and report whether the choice changes.

### Make uncertainty actionable

The practical response to missing information is usually a low-cost measurement, a conservative bound or a controlled trial. Sensitivity analysis exposes which uncertain assumption is capable of reversing a recommendation.

## 3. Where the model can fail

Choosing the cheapest expected cost is not adequate if one option violates safety, environmental or regulatory constraints.

An important diagnostic practice is to seek evidence against the simplest explanation. A repair which temporarily restores output can disguise an uncorrected design, installation or operating error. If the apparent rate improves after a maintenance change, normalize against exposure and examine whether production load, weather, equipment population or reporting conventions changed in the same period. Correlation between a signal and a failure does not establish that intervening on the signal will prevent the failure.

The operational consequence of a bad assumption depends on the equipment. For an ordinary production asset it may mean excess inventory or a costly breakdown. For a safety-critical plant it can mean loss of containment, personnel exposure, service failure or violation of required inspection obligations. Use the teaching result only for understanding; site-specific decisions need competent hazard review, current standards, supplier instructions, physical verification and appropriate approval.

### Define the denominator

Write down the reference population and the interval across which the observation has meaning. An event per machine-day differs from an event per operating hour if production schedules differ. A simulation that silently uses an assumed denominator produces a neat but potentially false comparison.

## 4. Engineering investigation: from model to evidence

**Field prompt.** Create a decision matrix for repair, overhaul and replacement with explicit no-go conditions and uncertainty ranges.

Connect this task to the unit study: Compare stocking one critical drive at a remote water station with purchasing on demand. Use hypothetical failure frequency, lead time and holding cost, and vary the consequence of lost water supply. The expected notebook output is concrete: Deliver a master data standard, spare-parts risk register, cost scenario table, and set of leading and lagging KPIs. Include a sketch, a table of unknowns and an explicit statement of what observation would reverse the initial hypothesis. A useful investigation records the condition before repair, retains component photographs when safe, notes firmware and calibration versions where relevant, and documents any temporary bypass. Explain how the conclusion would be independently reproduced by another analyst.

**Proposed procedure.** First obtain permission and confirm the relevant safe isolation and operating boundaries; never open energized or pressurized equipment for a classroom exercise. Second use a published sampling interval or an explicit study protocol. Third capture raw data with units, timestamps and event codes before cleaning or filtering them. Fourth run a simple hand calculation and cross-check it with a separate implementation. Fifth evaluate sensitivity to one omitted mechanism, one measurement bias and one uncertain input. Sixth record the proposed action, owner, estimated restoration impact and a verification measure that will be checked after implementation.

A reliable result can be modest. It may show that two alternatives cannot yet be distinguished, that a missing event time prevents statistical estimation or that extra inspection has poor coverage. Reporting these limitations is preferable to manufacturing precision. For plant-level application, specify which person may authorize a shutdown, restart or alteration of protection logic; a textbook exercise never supplies that authorization.

## 5. Exercises and instructor checkpoints

1. **Definitions.** Define the physical or functional event involved in **replacement versus repair decisions**. Give its observable boundary and one alternative definition that would change the counted population.
2. **Quantification.** Use the relation `Equivalent annualized cost can compare life-cycle alternatives with equal service objectives and a consistent discount rate.` with a consistent assumed dataset of your own. Show all units and at least one limiting-case check.
3. **Sensitivity.** Change the most uncertain nonzero input by ±20% where physically meaningful. Compare the output and decide whether the maintenance choice is robust.
4. **Counterexample.** Explain precisely why the following limitation matters: Choosing the cheapest expected cost is not adequate if one option violates safety, environmental or regulatory constraints.
5. **Application.** Create a decision matrix for repair, overhaul and replacement with explicit no-go conditions and uncertainty ranges. Supply an evidence table with at least three observations and mark each entry as measured, supplied by a source, or synthetic.

**Self-check guidance.** A correct response identifies the function, model, assumptions, arithmetic, consequence and plausible falsification. The numeric exercise should be reproducible from the student's displayed inputs. The sensitivity response should not silently vary an independent parameter if two inputs are physically coupled. The field task should end with an evidence request or a testable action rather than a generic recommendation to “do maintenance.”

## 6. Connections to the wider curriculum

This topic interacts with earlier units through lifetime probability, state restoration, operating mechanisms and cost. When proposing a spare or a maintenance interval, ask how it changes both the frequency of failures and the length of lost service. When proposing a sensor, ask how often it produces a useful warning and how the organization responds. An effective recommendation uses the smallest set of credible assumptions needed for the stated decision and explains the circumstances under which its simplified formula would stop being useful.

**Source-reading exercise.** Compare the language of your model with the NIST reliability handbook or the NASA reliability-centered maintenance material listed in the references. Do not reproduce external texts; use the primary source to check the meaning of the statistical term or maintenance method, then describe the limitation in your own words.


---

# Unit 06 · Lesson 04 — Uncertainty and Monte Carlo scenarios

**Learning goal.** Explain the core engineering statement, calculate a clearly bounded example, challenge at least one assumption and propose a measurable action. This material is an educational draft, not an authority for equipment acceptance.

## 1. Concept and technical meaning

Monte Carlo simulation propagates stated input distributions through a model; it does not validate the model structure or guarantee representative inputs. Separate parameter uncertainty, natural variability, measurement error and uncertainty about failure mechanisms. Report percentiles, assumptions and risk drivers, not only a mean.

The useful starting question is **“What physical or service event am I modeling?”** Place the studied item within the unit's central objective: Maintenance information systems fail when people use inconsistent failure codes, do not record exposure, and cannot reconcile repair labor with calendar downtime. Spare provisioning must reflect demand uncertainty, lead time, criticality and obsolescence; a single inventory formula cannot substitute for risk judgement. A numerical value only becomes an engineering claim when the mission duration, operating conditions, item state and decision boundary are specified. If the equipment is repaired between events, decide whether the model starts a new life or continues to represent accumulated degradation. When data are drawn from multiple installations, check whether load, age, ambient environment and maintenance practice are comparable.

### Audit model assumptions

Every model has a region in which its assumptions make sense. Before using an equation in a recommendation, check units, boundary, independence assumptions, the way failures are counted, and whether repair changes the modeled population.

A professional worksheet for **uncertainty and monte carlo scenarios** should preserve the original event definition and the raw denominator used in the calculation. Build a simple diagram that traces the studied input to a measured output. Label its arrows as measured relationships, physical assumptions or hypothetical causal mechanisms. This keeps the numerical calculation from silently becoming proof of a mechanism that has not been investigated.

## 2. Governing relation and derivation checks

**Primary relation:** `A simple annual cost sample C=N_f C_f+N_pm C_pm+fixed cost; the event process for N_f must match exposure assumptions.`

The relation should first be read in words and translated into a dimensional statement. Identify which quantities are probabilities, time or cycle measures, rates, costs, loads, engineering scores or empirical indicators. If an input is a probability, its feasible interval is from zero to one; if it is an event intensity, it must be nonnegative and accompanied by a unit such as failures per operating hour. The output should be interpreted at the same stated boundary and over the same mission or reporting period as its inputs.

**Reasoning sequence.** (i) Define the asset and the function; (ii) write all inputs and their units; (iii) choose the simplest physically defensible model; (iv) perform the computation using an independent check; (v) compare the result with limiting cases; (vi) state uncertainty and model boundaries before recommending maintenance. For example, the limit of a no-failure event probability as an assumed event rate approaches zero should be consistent with ordinary experience. A result outside its physically possible range suggests either an arithmetic fault, incompatible units or a model used outside its assumptions.

**Worked engineering example.** Sampling annual failures from a Poisson distribution with mean 3 and multiplying by failure consequence demonstrates cost variability. If failures share one common utility, independent Poisson counts can be misleading.

After evaluating the arithmetic, report what the result means and—equally important—what it does not mean. Distinguish a hypothetical prediction from a measured population statistic. If a numerical example uses a notional fleet or synthetic data, it must not appear in an operator's work package as a measured site result. For any policy comparison, repeat the calculation using at least two plausible ranges for its most uncertain input and report whether the choice changes.

### Plan a falsification test

A good explanation can be disproved. State an observation that would contradict the proposed failure mechanism, and arrange measurements so another engineer could reach an independent conclusion rather than merely agreeing with the initial diagnosis.

## 3. Where the model can fail

Fitting broad uncertainty intervals because data are missing should be accompanied by a data-collection plan, not merely a more sophisticated simulator.

An important diagnostic practice is to seek evidence against the simplest explanation. A repair which temporarily restores output can disguise an uncorrected design, installation or operating error. If the apparent rate improves after a maintenance change, normalize against exposure and examine whether production load, weather, equipment population or reporting conventions changed in the same period. Correlation between a signal and a failure does not establish that intervening on the signal will prevent the failure.

The operational consequence of a bad assumption depends on the equipment. For an ordinary production asset it may mean excess inventory or a costly breakdown. For a safety-critical plant it can mean loss of containment, personnel exposure, service failure or violation of required inspection obligations. Use the teaching result only for understanding; site-specific decisions need competent hazard review, current standards, supplier instructions, physical verification and appropriate approval.

### Keep the physical mechanism visible

An apparent trend in a chart is evidence about recorded variables, not automatically the explanation of a component failure. Ask which loads, contamination pathways, temperatures, controls, maintenance practices or environmental stresses could produce the observed pattern.

## 4. Engineering investigation: from model to evidence

**Field prompt.** Set up a 1,000-trial model and sensitivity plot for alternative preventive-maintenance schedules.

Connect this task to the unit study: A replacement motor has a three-week purchasing lead time. The practical outage duration may be days even when hands-on repair takes four hours. This difference determines both stock policy and the choice of reported maintainability metric. The expected notebook output is concrete: Deliver a master data standard, spare-parts risk register, cost scenario table, and set of leading and lagging KPIs. Include a sketch, a table of unknowns and an explicit statement of what observation would reverse the initial hypothesis. A useful investigation records the condition before repair, retains component photographs when safe, notes firmware and calibration versions where relevant, and documents any temporary bypass. Explain how the conclusion would be independently reproduced by another analyst.

**Proposed procedure.** First obtain permission and confirm the relevant safe isolation and operating boundaries; never open energized or pressurized equipment for a classroom exercise. Second use a published sampling interval or an explicit study protocol. Third capture raw data with units, timestamps and event codes before cleaning or filtering them. Fourth run a simple hand calculation and cross-check it with a separate implementation. Fifth evaluate sensitivity to one omitted mechanism, one measurement bias and one uncertain input. Sixth record the proposed action, owner, estimated restoration impact and a verification measure that will be checked after implementation.

A reliable result can be modest. It may show that two alternatives cannot yet be distinguished, that a missing event time prevents statistical estimation or that extra inspection has poor coverage. Reporting these limitations is preferable to manufacturing precision. For plant-level application, specify which person may authorize a shutdown, restart or alteration of protection logic; a textbook exercise never supplies that authorization.

## 5. Exercises and instructor checkpoints

1. **Definitions.** Define the physical or functional event involved in **uncertainty and monte carlo scenarios**. Give its observable boundary and one alternative definition that would change the counted population.
2. **Quantification.** Use the relation `A simple annual cost sample C=N_f C_f+N_pm C_pm+fixed cost; the event process for N_f must match exposure assumptions.` with a consistent assumed dataset of your own. Show all units and at least one limiting-case check.
3. **Sensitivity.** Change the most uncertain nonzero input by ±20% where physically meaningful. Compare the output and decide whether the maintenance choice is robust.
4. **Counterexample.** Explain precisely why the following limitation matters: Fitting broad uncertainty intervals because data are missing should be accompanied by a data-collection plan, not merely a more sophisticated simulator.
5. **Application.** Set up a 1,000-trial model and sensitivity plot for alternative preventive-maintenance schedules. Supply an evidence table with at least three observations and mark each entry as measured, supplied by a source, or synthetic.

**Self-check guidance.** A correct response identifies the function, model, assumptions, arithmetic, consequence and plausible falsification. The numeric exercise should be reproducible from the student's displayed inputs. The sensitivity response should not silently vary an independent parameter if two inputs are physically coupled. The field task should end with an evidence request or a testable action rather than a generic recommendation to “do maintenance.”

## 6. Connections to the wider curriculum

This topic interacts with earlier units through lifetime probability, state restoration, operating mechanisms and cost. When proposing a spare or a maintenance interval, ask how it changes both the frequency of failures and the length of lost service. When proposing a sensor, ask how often it produces a useful warning and how the organization responds. An effective recommendation uses the smallest set of credible assumptions needed for the stated decision and explains the circumstances under which its simplified formula would stop being useful.

**Source-reading exercise.** Compare the language of your model with the NIST reliability handbook or the NASA reliability-centered maintenance material listed in the references. Do not reproduce external texts; use the primary source to check the meaning of the statistical term or maintenance method, then describe the limitation in your own words.


---

# Unit 06 · Lesson 05 — OEE, production losses and bottleneck performance

**Learning goal.** Explain the core engineering statement, calculate a clearly bounded example, challenge at least one assumption and propose a measurable action. This material is an educational draft, not an authority for equipment acceptance.

## 1. Concept and technical meaning

Overall Equipment Effectiveness multiplies availability, performance and quality ratios under a defined scheduled production-time convention. It is a production accounting framework, not a direct measure of inherent reliability. Improving OEE on a non-bottleneck asset may not increase total plant throughput.

The useful starting question is **“What physical or service event am I modeling?”** Place the studied item within the unit's central objective: Maintenance information systems fail when people use inconsistent failure codes, do not record exposure, and cannot reconcile repair labor with calendar downtime. Spare provisioning must reflect demand uncertainty, lead time, criticality and obsolescence; a single inventory formula cannot substitute for risk judgement. A numerical value only becomes an engineering claim when the mission duration, operating conditions, item state and decision boundary are specified. If the equipment is repaired between events, decide whether the model starts a new life or continues to represent accumulated degradation. When data are drawn from multiple installations, check whether load, age, ambient environment and maintenance practice are comparable.

### Keep the operational objective in view

A metric is useful when it changes a decision that helps deliver service. Additional data collection should therefore answer a concrete question: whether to inspect, redesign, change stocking policy, add monitoring or accept an explicitly bounded residual risk.

A professional worksheet for **oee, production losses and bottleneck performance** should preserve the original event definition and the raw denominator used in the calculation. Build a simple diagram that traces the studied input to a measured output. Label its arrows as measured relationships, physical assumptions or hypothetical causal mechanisms. This keeps the numerical calculation from silently becoming proof of a mechanism that has not been investigated.

## 2. Governing relation and derivation checks

**Primary relation:** `OEE=A×P×Q.`

The relation should first be read in words and translated into a dimensional statement. Identify which quantities are probabilities, time or cycle measures, rates, costs, loads, engineering scores or empirical indicators. If an input is a probability, its feasible interval is from zero to one; if it is an event intensity, it must be nonnegative and accompanied by a unit such as failures per operating hour. The output should be interpreted at the same stated boundary and over the same mission or reporting period as its inputs.

**Reasoning sequence.** (i) Define the asset and the function; (ii) write all inputs and their units; (iii) choose the simplest physically defensible model; (iv) perform the computation using an independent check; (v) compare the result with limiting cases; (vi) state uncertainty and model boundaries before recommending maintenance. For example, the limit of a no-failure event probability as an assumed event rate approaches zero should be consistent with ordinary experience. A result outside its physically possible range suggests either an arithmetic fault, incompatible units or a model used outside its assumptions.

**Worked engineering example.** A production cell with availability 0.90, performance 0.95 and first-pass quality 0.98 has OEE≈0.8379. A maintenance intervention improves the availability term only if it reduces the counted losses.

After evaluating the arithmetic, report what the result means and—equally important—what it does not mean. Distinguish a hypothetical prediction from a measured population statistic. If a numerical example uses a notional fleet or synthetic data, it must not appear in an operator's work package as a measured site result. For any policy comparison, repeat the calculation using at least two plausible ranges for its most uncertain input and report whether the choice changes.

### Define the denominator

Write down the reference population and the interval across which the observation has meaning. An event per machine-day differs from an event per operating hour if production schedules differ. A simulation that silently uses an assumed denominator produces a neat but potentially false comparison.

## 3. Where the model can fail

Counting planned shutdowns differently between departments invalidates cross-site benchmarking; quality loss may be caused by upstream process variation, not machinery.

An important diagnostic practice is to seek evidence against the simplest explanation. A repair which temporarily restores output can disguise an uncorrected design, installation or operating error. If the apparent rate improves after a maintenance change, normalize against exposure and examine whether production load, weather, equipment population or reporting conventions changed in the same period. Correlation between a signal and a failure does not establish that intervening on the signal will prevent the failure.

The operational consequence of a bad assumption depends on the equipment. For an ordinary production asset it may mean excess inventory or a costly breakdown. For a safety-critical plant it can mean loss of containment, personnel exposure, service failure or violation of required inspection obligations. Use the teaching result only for understanding; site-specific decisions need competent hazard review, current standards, supplier instructions, physical verification and appropriate approval.

### Separate requirement from measurement

An engineer should be able to state the acceptance requirement before seeing the measurement. Otherwise thresholds tend to move after results are known. Preserve the original requirement, report any exception and obtain authorized approval for changes.

## 4. Engineering investigation: from model to evidence

**Field prompt.** Break down one shift into planned time, breakdowns, microstops, speed losses and rejected units.

Connect this task to the unit study: Compare stocking one critical drive at a remote water station with purchasing on demand. Use hypothetical failure frequency, lead time and holding cost, and vary the consequence of lost water supply. The expected notebook output is concrete: Deliver a master data standard, spare-parts risk register, cost scenario table, and set of leading and lagging KPIs. Include a sketch, a table of unknowns and an explicit statement of what observation would reverse the initial hypothesis. A useful investigation records the condition before repair, retains component photographs when safe, notes firmware and calibration versions where relevant, and documents any temporary bypass. Explain how the conclusion would be independently reproduced by another analyst.

**Proposed procedure.** First obtain permission and confirm the relevant safe isolation and operating boundaries; never open energized or pressurized equipment for a classroom exercise. Second use a published sampling interval or an explicit study protocol. Third capture raw data with units, timestamps and event codes before cleaning or filtering them. Fourth run a simple hand calculation and cross-check it with a separate implementation. Fifth evaluate sensitivity to one omitted mechanism, one measurement bias and one uncertain input. Sixth record the proposed action, owner, estimated restoration impact and a verification measure that will be checked after implementation.

A reliable result can be modest. It may show that two alternatives cannot yet be distinguished, that a missing event time prevents statistical estimation or that extra inspection has poor coverage. Reporting these limitations is preferable to manufacturing precision. For plant-level application, specify which person may authorize a shutdown, restart or alteration of protection logic; a textbook exercise never supplies that authorization.

## 5. Exercises and instructor checkpoints

1. **Definitions.** Define the physical or functional event involved in **oee, production losses and bottleneck performance**. Give its observable boundary and one alternative definition that would change the counted population.
2. **Quantification.** Use the relation `OEE=A×P×Q.` with a consistent assumed dataset of your own. Show all units and at least one limiting-case check.
3. **Sensitivity.** Change the most uncertain nonzero input by ±20% where physically meaningful. Compare the output and decide whether the maintenance choice is robust.
4. **Counterexample.** Explain precisely why the following limitation matters: Counting planned shutdowns differently between departments invalidates cross-site benchmarking; quality loss may be caused by upstream process variation, not machinery.
5. **Application.** Break down one shift into planned time, breakdowns, microstops, speed losses and rejected units. Supply an evidence table with at least three observations and mark each entry as measured, supplied by a source, or synthetic.

**Self-check guidance.** A correct response identifies the function, model, assumptions, arithmetic, consequence and plausible falsification. The numeric exercise should be reproducible from the student's displayed inputs. The sensitivity response should not silently vary an independent parameter if two inputs are physically coupled. The field task should end with an evidence request or a testable action rather than a generic recommendation to “do maintenance.”

## 6. Connections to the wider curriculum

This topic interacts with earlier units through lifetime probability, state restoration, operating mechanisms and cost. When proposing a spare or a maintenance interval, ask how it changes both the frequency of failures and the length of lost service. When proposing a sensor, ask how often it produces a useful warning and how the organization responds. An effective recommendation uses the smallest set of credible assumptions needed for the stated decision and explains the circumstances under which its simplified formula would stop being useful.

**Source-reading exercise.** Compare the language of your model with the NIST reliability handbook or the NASA reliability-centered maintenance material listed in the references. Do not reproduce external texts; use the primary source to check the meaning of the statistical term or maintenance method, then describe the limitation in your own words.


---

