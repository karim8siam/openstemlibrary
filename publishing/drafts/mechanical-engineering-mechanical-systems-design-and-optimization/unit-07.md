# Unit 07: Uncertainty, Robustness, Testing and Reliability

**Course Code**: MSO 407 · **Level**: Advanced Undergraduate Engineering

## Unit Overview & Physical Foundations

This comprehensive university textbook unit covers the theoretical framework, physical modeling, mathematical governing equations, and engineering applications of **Uncertainty, Robustness, Testing and Reliability**.

# U07-L01 — Statistics, tolerances and uncertainty budgets

**Unit 7: Uncertainty, Robustness, Testing and Reliability**  
**Purpose.** Evaluate one real design decision in the context of an integrated mechanical system. Students should be able to explain the physics, run a bounded calculation, test its assumptions and prepare a defensible design record.

## 1. Physical meaning and engineering relevance

Measurements have repeatability, calibration, drift, resolution and representativeness limitations. Propagate uncertainty through governing relations and separate aleatory variability from gaps in model knowledge.

A good engineering claim starts from the exact outcome being sought and a stated operational setting. In this lesson, explain what happens during commissioning, steady operation, abnormal operation and normal service. A variable that looks constant in a laboratory exercise may change dramatically when equipment ages or moves between sites. A drawing alone cannot show every thermal, mechanical and control dependency; record interfaces and operating sequences as well. Treat the word **system** as a boundary containing components, people, controls and environmental interactions, not simply a list of purchased items.

The governing decision is linked to the unit's wider question: Nominal performance is not robust performance. Uncertain loading, material properties, wear, manufacturing variation and model inadequacy produce distributions or bounded envelopes. Verification asks whether the calculation or implementation is correct; validation asks whether the model represents the intended reality. To make the relation operational, write every variable with units, the domain over which it is expected to be useful and the physical mechanism that might violate it. When using a supplied coefficient, say whether it came from a material test, a catalog, a standard, or a hypothetical classroom choice. Do not silently combine catalog ratings at different temperatures or duty cycles. If a concept depends on an uncertain input, use its plausible interval rather than only a best-looking estimate.

## 2. Governing relation and useful calculation

**Core relation or design rule:** `u_y² ≈ Σ (∂f/∂x_i)² u_i² for independent inputs`

**Worked case.** A force transducer uncertainty of 2% and lever-arm uncertainty of 1% combine to about 2.24% relative uncertainty for torque if independent and small. A systematic offset needs different treatment.

The first check is dimensional: if the symbols represent different physical dimensions, convert to a common SI basis before evaluating. The second check is one limiting case: set a load to zero, make the design very stiff, or let an efficiency approach unity—whichever is physically relevant—and ask if the predicted direction makes sense. The third check is to estimate the size of an ignored term. A compact hand calculation is valuable because it can expose a reversed ratio or a misplaced conversion factor that would otherwise pass through a spreadsheet unnoticed.

Convert the worked case into a design memo: state the known inputs, unknown output, assumptions, calculation, units and consequence of crossing the limit. Make two alternative estimates, one at a favorable operating point and one at a credible adverse point. Explain why the apparent improvement may not translate into a better total system. The correct comparison uses the same function, service life and boundary for each alternative rather than comparing one design at peak efficiency with another at average duty.

## 3. Scope, counterexample and failure conditions

Treating correlated sensors as independent can understate uncertainty. Extra decimal places from a spreadsheet are not evidence.

A calculation is only as good as its assumed configuration. Ask whether the actual mechanism is linear, whether geometry remains unchanged, whether a temperature-dependent property was treated as fixed, and whether contact, vibration or actuator saturation could introduce a discontinuity. If the model ignores an effect because it appears small, report the evidence supporting that decision. Quantification is not a substitute for identifying hazards: an attractive weighted objective cannot excuse an unverified guard, protection feature, pressure boundary or emergency stop.

A counterexample helps establish the scope. Imagine the original design moved from a controlled teaching bench to a dirty or wet industrial location. The incoming load spectrum, corrosion exposure, calibration frequency and repair resources may be different. Name at least one parameter from the equation that remains meaningful and one omitted mechanism that becomes important. Explain how the design review would change if that mechanism is plausible. Record any consequence whose acceptability must be judged by a competent safety professional rather than inferred from a classroom equation.

## 4. Practical investigation — What is controlled?

State the decision variable, its allowed range, and which physical observations it can change. A variable that cannot be adjusted by the engineer is a disturbance or measured parameter; confusing the two makes the optimization unrealistic.

**Studio assignment.** List every measurement needed for a shaft torque test and build a numerical uncertainty budget with covariance assumptions.

**Required confirmation.** Calibration certificates, uncertainty conventions and repeated readings on an independent instrument.

Build a reproducible notebook for this assignment. Include a sketch or diagram, table of known quantities with units, a physical basis for each relationship, and a separate list of facts that are merely assumed. Perform the calculation with independent arithmetic. If testing is proposed, explain where the sensors go and how their calibration and resolution affect the result. State what data would falsify the current design hypothesis; do not propose only measurements that could support it. Keep original data rather than overwriting it when outliers or transcription errors are discovered.

For this particular case, apply the following broader check: Present a traceable technical argument that allows another engineer to reconstruct the design choice. List rejected concepts, open issues, physical test evidence, planned maintenance and permitted operating limits. This guards against optimizing one metric while overlooking a coupled physical constraint. Report a design alternative in which the selected performance improves while some other important objective worsens. That alternative may still be appropriate, but the trade must be transparent and tied to stakeholder priorities. Before deciding, check whether the new configuration requires another supplier capability study, additional inspection or a revised safety analysis.

## 5. Exercises: calculation, design and criticism

1. **Definitions:** Explain **statistics, tolerances and uncertainty budgets** to a technician who knows the equipment but has not studied the model. State the measurable event, required operating condition and one assumption that cannot be read directly from the output.
2. **Hand calculation:** Reproduce the worked case and its governing rule `u_y² ≈ Σ (∂f/∂x_i)² u_i² for independent inputs` with all units and significant figures justified. Change one input by +10% and determine whether the direction of change is physically plausible.
3. **Boundary case:** Analyze the specific limitation: Treating correlated sensors as independent can understate uncertainty. Extra decimal places from a spreadsheet are not evidence. Explain which additional calculation, test or design constraint is required and why a single generic safety factor cannot solve the missing-physics problem.
4. **Alternative:** List every measurement needed for a shaft torque test and build a numerical uncertainty budget with covariance assumptions. Propose a second feasible mechanism or component, not merely a different numerical setting of the original choice. Evaluate manufacturing and maintenance implications.
5. **Evidence:** Calibration certificates, uncertainty conventions and repeated readings on an independent instrument. Prepare a small table of what would be measured, which instrument would be used, what uncertainty could dominate and whether the result would verify a requirement or validate intended use.

**Instructor checkpoint A.** An answer that repeats the formula without identifying the operational boundary is incomplete. The student's result must have consistent units and a clear physical sign. If the output is expressed as a ratio or probability, explain its numerical range and whether independence assumptions apply. If an optimization is involved, a design that violates a hard constraint is rejected even if its objective is lower.

**Instructor checkpoint B.** Students should distinguish a calculated output from physical evidence. Strong submissions show an independent check, a sensitivity comparison, a plausible counterexample and an actionable test plan. A poor submission uses extra decimal places, repeated simulations, or an appealing chart to imply accuracy that the inputs do not support. A recommendation is not complete without a limitation and a named action to reduce the largest consequential uncertainty.

## 6. Integration with other mechanical disciplines

The design decision in **statistics, tolerances and uncertainty budgets** is related to **physics-based modeling and digital engineering**. A useful model states assumptions, state variables, boundary conditions, conservation relations and applicable time scale. A model is not a digital twin merely because it has a dashboard. Its predictive usefulness rests on calibration, identification and comparison with measurements independent of fitting data. Think about what information must pass between those two engineering teams and whether the transfer occurs as a load case, geometric tolerance, material property, signal, cost scenario or acceptance test. An interface that lacks an owner may survive several design reviews without being checked. In a final integration meeting, require each assumption to have an identified source and a planned verification activity; record deviations explicitly.

**Engineering notebook output:** One independent arithmetic check, one alternative architecture, one requirement-to-evidence row, one uncertainty statement, and one open risk item to carry into the unit capstone.


---

# U07-L02 — Worst-case analysis and robust design

**Unit 7: Uncertainty, Robustness, Testing and Reliability**  
**Purpose.** Evaluate one real design decision in the context of an integrated mechanical system. Students should be able to explain the physics, run a bounded calculation, test its assumptions and prepare a defensible design record.

## 1. Physical meaning and engineering relevance

A design with the best nominal score may fail under minor variation. Robust design examines worst credible operating points or outcome distributions and seeks solutions that retain adequate margins without hidden violations.

A good engineering claim starts from the exact outcome being sought and a stated operational setting. In this lesson, explain what happens during commissioning, steady operation, abnormal operation and normal service. A variable that looks constant in a laboratory exercise may change dramatically when equipment ages or moves between sites. A drawing alone cannot show every thermal, mechanical and control dependency; record interfaces and operating sequences as well. Treat the word **system** as a boundary containing components, people, controls and environmental interactions, not simply a list of purchased items.

The governing decision is linked to the unit's wider question: Nominal performance is not robust performance. Uncertain loading, material properties, wear, manufacturing variation and model inadequacy produce distributions or bounded envelopes. Verification asks whether the calculation or implementation is correct; validation asks whether the model represents the intended reality. To make the relation operational, write every variable with units, the domain over which it is expected to be useful and the physical mechanism that might violate it. When using a supplied coefficient, say whether it came from a material test, a catalog, a standard, or a hypothetical classroom choice. Do not silently combine catalog ratings at different temperatures or duty cycles. If a concept depends on an uncertain input, use its plausible interval rather than only a best-looking estimate.

## 2. Governing relation and useful calculation

**Core relation or design rule:** `max_w g(x,w) ≤ 0 over stated uncertainty set W`

**Worked case.** A nominal clearance of 0.30 mm may vanish when production tolerance, temperature expansion and mounting deflection accumulate. Check compatible signed worst cases, not a random selection of large numbers.

The first check is dimensional: if the symbols represent different physical dimensions, convert to a common SI basis before evaluating. The second check is one limiting case: set a load to zero, make the design very stiff, or let an efficiency approach unity—whichever is physically relevant—and ask if the predicted direction makes sense. The third check is to estimate the size of an ignored term. A compact hand calculation is valuable because it can expose a reversed ratio or a misplaced conversion factor that would otherwise pass through a spreadsheet unnoticed.

Convert the worked case into a design memo: state the known inputs, unknown output, assumptions, calculation, units and consequence of crossing the limit. Make two alternative estimates, one at a favorable operating point and one at a credible adverse point. Explain why the apparent improvement may not translate into a better total system. The correct comparison uses the same function, service life and boundary for each alternative rather than comparing one design at peak efficiency with another at average duty.

## 3. Scope, counterexample and failure conditions

An arbitrarily large uncertainty box can produce an impractical design; an unjustifiably small box hides actual field risk.

A calculation is only as good as its assumed configuration. Ask whether the actual mechanism is linear, whether geometry remains unchanged, whether a temperature-dependent property was treated as fixed, and whether contact, vibration or actuator saturation could introduce a discontinuity. If the model ignores an effect because it appears small, report the evidence supporting that decision. Quantification is not a substitute for identifying hazards: an attractive weighted objective cannot excuse an unverified guard, protection feature, pressure boundary or emergency stop.

A counterexample helps establish the scope. Imagine the original design moved from a controlled teaching bench to a dirty or wet industrial location. The incoming load spectrum, corrosion exposure, calibration frequency and repair resources may be different. Name at least one parameter from the equation that remains meaningful and one omitted mechanism that becomes important. Explain how the design review would change if that mechanism is plausible. Record any consequence whose acceptability must be judged by a competent safety professional rather than inferred from a classroom equation.

## 4. Practical investigation — What is conserved?

Start by tracing mass, force, energy or information through the studied boundary. Write down any neglected source, loss or interface. When a numerical output appears to violate a conservation statement, inspect boundary definitions before changing the data.

**Studio assignment.** Define credible uncertainty intervals for a shaft seal, compute the tightest clearance and identify the dominant parameter.

**Required confirmation.** Validated tolerance sources, thermal observations and measurement of assembled clearance.

Build a reproducible notebook for this assignment. Include a sketch or diagram, table of known quantities with units, a physical basis for each relationship, and a separate list of facts that are merely assumed. Perform the calculation with independent arithmetic. If testing is proposed, explain where the sensors go and how their calibration and resolution affect the result. State what data would falsify the current design hypothesis; do not propose only measurements that could support it. Keep original data rather than overwriting it when outliers or transcription errors are discovered.

For this particular case, apply the following broader check: Form a trace from need through required function and quantified threshold to an instrumented acceptance result. Avoid a requirement stating only the preferred component; that describes a proposed solution rather than an outcome. This guards against optimizing one metric while overlooking a coupled physical constraint. Report a design alternative in which the selected performance improves while some other important objective worsens. That alternative may still be appropriate, but the trade must be transparent and tied to stakeholder priorities. Before deciding, check whether the new configuration requires another supplier capability study, additional inspection or a revised safety analysis.

## 5. Exercises: calculation, design and criticism

1. **Definitions:** Explain **worst-case analysis and robust design** to a technician who knows the equipment but has not studied the model. State the measurable event, required operating condition and one assumption that cannot be read directly from the output.
2. **Hand calculation:** Reproduce the worked case and its governing rule `max_w g(x,w) ≤ 0 over stated uncertainty set W` with all units and significant figures justified. Change one input by +10% and determine whether the direction of change is physically plausible.
3. **Boundary case:** Analyze the specific limitation: An arbitrarily large uncertainty box can produce an impractical design; an unjustifiably small box hides actual field risk. Explain which additional calculation, test or design constraint is required and why a single generic safety factor cannot solve the missing-physics problem.
4. **Alternative:** Define credible uncertainty intervals for a shaft seal, compute the tightest clearance and identify the dominant parameter. Propose a second feasible mechanism or component, not merely a different numerical setting of the original choice. Evaluate manufacturing and maintenance implications.
5. **Evidence:** Validated tolerance sources, thermal observations and measurement of assembled clearance. Prepare a small table of what would be measured, which instrument would be used, what uncertainty could dominate and whether the result would verify a requirement or validate intended use.

**Instructor checkpoint A.** An answer that repeats the formula without identifying the operational boundary is incomplete. The student's result must have consistent units and a clear physical sign. If the output is expressed as a ratio or probability, explain its numerical range and whether independence assumptions apply. If an optimization is involved, a design that violates a hard constraint is rejected even if its objective is lower.

**Instructor checkpoint B.** Students should distinguish a calculated output from physical evidence. Strong submissions show an independent check, a sensitivity comparison, a plausible counterexample and an actionable test plan. A poor submission uses extra decimal places, repeated simulations, or an appealing chart to imply accuracy that the inputs do not support. A recommendation is not complete without a limitation and a named action to reduce the largest consequential uncertainty.

## 6. Integration with other mechanical disciplines

The design decision in **worst-case analysis and robust design** is related to **optimization methods and design tradeoffs**. Design optimization asks which feasible decision vector gives the best defensible outcome. Feasibility conditions are not preferences. Multiobjective design typically produces a Pareto set rather than one uniquely correct answer, and ranking alternatives requires transparent priorities and sensitivity to uncertain weights. Think about what information must pass between those two engineering teams and whether the transfer occurs as a load case, geometric tolerance, material property, signal, cost scenario or acceptance test. An interface that lacks an owner may survive several design reviews without being checked. In a final integration meeting, require each assumption to have an identified source and a planned verification activity; record deviations explicitly.

**Engineering notebook output:** One independent arithmetic check, one alternative architecture, one requirement-to-evidence row, one uncertainty statement, and one open risk item to carry into the unit capstone.


---

# U07-L03 — Monte Carlo simulation and sampling

**Unit 7: Uncertainty, Robustness, Testing and Reliability**  
**Purpose.** Evaluate one real design decision in the context of an integrated mechanical system. Students should be able to explain the physics, run a bounded calculation, test its assumptions and prepare a defensible design record.

## 1. Physical meaning and engineering relevance

Sampling propagates assumed input distributions through a model to estimate plausible output variation. It does not cure uncertain distributions, omitted physics or wrong dependence assumptions. Use a fixed seed for reproducibility and convergence diagnostics for reported tails.

A good engineering claim starts from the exact outcome being sought and a stated operational setting. In this lesson, explain what happens during commissioning, steady operation, abnormal operation and normal service. A variable that looks constant in a laboratory exercise may change dramatically when equipment ages or moves between sites. A drawing alone cannot show every thermal, mechanical and control dependency; record interfaces and operating sequences as well. Treat the word **system** as a boundary containing components, people, controls and environmental interactions, not simply a list of purchased items.

The governing decision is linked to the unit's wider question: Nominal performance is not robust performance. Uncertain loading, material properties, wear, manufacturing variation and model inadequacy produce distributions or bounded envelopes. Verification asks whether the calculation or implementation is correct; validation asks whether the model represents the intended reality. To make the relation operational, write every variable with units, the domain over which it is expected to be useful and the physical mechanism that might violate it. When using a supplied coefficient, say whether it came from a material test, a catalog, a standard, or a hypothetical classroom choice. Do not silently combine catalog ratings at different temperatures or duty cycles. If a concept depends on an uncertain input, use its plausible interval rather than only a best-looking estimate.

## 2. Governing relation and useful calculation

**Core relation or design rule:** `Y_i = f(X_i), i = 1,…,N`

**Worked case.** Sample normally distributed dimensions to estimate a clearance distribution. If tolerance tails are truncated by production inspection, modeling unbounded normal values may exaggerate or distort the result.

The first check is dimensional: if the symbols represent different physical dimensions, convert to a common SI basis before evaluating. The second check is one limiting case: set a load to zero, make the design very stiff, or let an efficiency approach unity—whichever is physically relevant—and ask if the predicted direction makes sense. The third check is to estimate the size of an ignored term. A compact hand calculation is valuable because it can expose a reversed ratio or a misplaced conversion factor that would otherwise pass through a spreadsheet unnoticed.

Convert the worked case into a design memo: state the known inputs, unknown output, assumptions, calculation, units and consequence of crossing the limit. Make two alternative estimates, one at a favorable operating point and one at a credible adverse point. Explain why the apparent improvement may not translate into a better total system. The correct comparison uses the same function, service life and boundary for each alternative rather than comparing one design at peak efficiency with another at average duty.

## 3. Scope, counterexample and failure conditions

A million simulation draws cannot compensate for sparse material test data or a mislabeled failure threshold. Rare-event probabilities demand specialized estimation or evidence.

A calculation is only as good as its assumed configuration. Ask whether the actual mechanism is linear, whether geometry remains unchanged, whether a temperature-dependent property was treated as fixed, and whether contact, vibration or actuator saturation could introduce a discontinuity. If the model ignores an effect because it appears small, report the evidence supporting that decision. Quantification is not a substitute for identifying hazards: an attractive weighted objective cannot excuse an unverified guard, protection feature, pressure boundary or emergency stop.

A counterexample helps establish the scope. Imagine the original design moved from a controlled teaching bench to a dirty or wet industrial location. The incoming load spectrum, corrosion exposure, calibration frequency and repair resources may be different. Name at least one parameter from the equation that remains meaningful and one omitted mechanism that becomes important. Explain how the design review would change if that mechanism is plausible. Record any consequence whose acceptability must be judged by a competent safety professional rather than inferred from a classroom equation.

## 4. Practical investigation — Where are the limits?

Report physical operating limits, catalog limits and mandated safeguards separately. A design which fails an essential condition is not acceptable just because its average objective value is attractive.

**Studio assignment.** Construct a Monte Carlo clearance study with 1,000 and 10,000 draws; compare stability of mean and estimated low percentile.

**Required confirmation.** Reproducible seed, distribution rationale, dependence matrix and independent spot calculations.

Build a reproducible notebook for this assignment. Include a sketch or diagram, table of known quantities with units, a physical basis for each relationship, and a separate list of facts that are merely assumed. Perform the calculation with independent arithmetic. If testing is proposed, explain where the sensors go and how their calibration and resolution affect the result. State what data would falsify the current design hypothesis; do not propose only measurements that could support it. Keep original data rather than overwriting it when outliers or transcription errors are discovered.

For this particular case, apply the following broader check: Start with the system boundary and distinguish conservation equations from fitted correlations. Identify what inputs are measured, taken from vendor data or chosen for teaching. Do not claim that a model represents the plant until a separate measurement comparison has been made. This guards against optimizing one metric while overlooking a coupled physical constraint. Report a design alternative in which the selected performance improves while some other important objective worsens. That alternative may still be appropriate, but the trade must be transparent and tied to stakeholder priorities. Before deciding, check whether the new configuration requires another supplier capability study, additional inspection or a revised safety analysis.

## 5. Exercises: calculation, design and criticism

1. **Definitions:** Explain **monte carlo simulation and sampling** to a technician who knows the equipment but has not studied the model. State the measurable event, required operating condition and one assumption that cannot be read directly from the output.
2. **Hand calculation:** Reproduce the worked case and its governing rule `Y_i = f(X_i), i = 1,…,N` with all units and significant figures justified. Change one input by +10% and determine whether the direction of change is physically plausible.
3. **Boundary case:** Analyze the specific limitation: A million simulation draws cannot compensate for sparse material test data or a mislabeled failure threshold. Rare-event probabilities demand specialized estimation or evidence. Explain which additional calculation, test or design constraint is required and why a single generic safety factor cannot solve the missing-physics problem.
4. **Alternative:** Construct a Monte Carlo clearance study with 1,000 and 10,000 draws; compare stability of mean and estimated low percentile. Propose a second feasible mechanism or component, not merely a different numerical setting of the original choice. Evaluate manufacturing and maintenance implications.
5. **Evidence:** Reproducible seed, distribution rationale, dependence matrix and independent spot calculations. Prepare a small table of what would be measured, which instrument would be used, what uncertainty could dominate and whether the result would verify a requirement or validate intended use.

**Instructor checkpoint A.** An answer that repeats the formula without identifying the operational boundary is incomplete. The student's result must have consistent units and a clear physical sign. If the output is expressed as a ratio or probability, explain its numerical range and whether independence assumptions apply. If an optimization is involved, a design that violates a hard constraint is rejected even if its objective is lower.

**Instructor checkpoint B.** Students should distinguish a calculated output from physical evidence. Strong submissions show an independent check, a sensitivity comparison, a plausible counterexample and an actionable test plan. A poor submission uses extra decimal places, repeated simulations, or an appealing chart to imply accuracy that the inputs do not support. A recommendation is not complete without a limitation and a named action to reduce the largest consequential uncertainty.

## 6. Integration with other mechanical disciplines

The design decision in **monte carlo simulation and sampling** is related to **structural, thermal and fluid co-design**. Mechanical design is coupled: increasing stiffness can raise mass; reducing friction changes heat generation; additional insulation changes expansion and packaging. Sequential discipline-by-discipline optimization often shifts a problem to another subsystem. Co-design evaluates physical interfaces and operating envelopes. Think about what information must pass between those two engineering teams and whether the transfer occurs as a load case, geometric tolerance, material property, signal, cost scenario or acceptance test. An interface that lacks an owner may survive several design reviews without being checked. In a final integration meeting, require each assumption to have an identified source and a planned verification activity; record deviations explicitly.

**Engineering notebook output:** One independent arithmetic check, one alternative architecture, one requirement-to-evidence row, one uncertainty statement, and one open risk item to carry into the unit capstone.


---

# U07-L04 — Reliability allocation and evidence

**Unit 7: Uncertainty, Robustness, Testing and Reliability**  
**Purpose.** Evaluate one real design decision in the context of an integrated mechanical system. Students should be able to explain the physics, run a bounded calculation, test its assumptions and prepare a defensible design record.

## 1. Physical meaning and engineering relevance

System reliability is shaped by component architecture and dependencies. Allocate performance targets to subsystems while accounting for mission duration and evidence available. Do not assume component reliabilities are independent without justification.

A good engineering claim starts from the exact outcome being sought and a stated operational setting. In this lesson, explain what happens during commissioning, steady operation, abnormal operation and normal service. A variable that looks constant in a laboratory exercise may change dramatically when equipment ages or moves between sites. A drawing alone cannot show every thermal, mechanical and control dependency; record interfaces and operating sequences as well. Treat the word **system** as a boundary containing components, people, controls and environmental interactions, not simply a list of purchased items.

The governing decision is linked to the unit's wider question: Nominal performance is not robust performance. Uncertain loading, material properties, wear, manufacturing variation and model inadequacy produce distributions or bounded envelopes. Verification asks whether the calculation or implementation is correct; validation asks whether the model represents the intended reality. To make the relation operational, write every variable with units, the domain over which it is expected to be useful and the physical mechanism that might violate it. When using a supplied coefficient, say whether it came from a material test, a catalog, a standard, or a hypothetical classroom choice. Do not silently combine catalog ratings at different temperatures or duty cycles. If a concept depends on an uncertain input, use its plausible interval rather than only a best-looking estimate.

## 2. Governing relation and useful calculation

**Core relation or design rule:** `R_series = Π_i R_i`

**Worked case.** Three independent components with survival probabilities 0.98, 0.97 and 0.99 over the same mission yield system survival about 0.941. Common vibration or a shared power supply can make that estimate optimistic.

The first check is dimensional: if the symbols represent different physical dimensions, convert to a common SI basis before evaluating. The second check is one limiting case: set a load to zero, make the design very stiff, or let an efficiency approach unity—whichever is physically relevant—and ask if the predicted direction makes sense. The third check is to estimate the size of an ignored term. A compact hand calculation is valuable because it can expose a reversed ratio or a misplaced conversion factor that would otherwise pass through a spreadsheet unnoticed.

Convert the worked case into a design memo: state the known inputs, unknown output, assumptions, calculation, units and consequence of crossing the limit. Make two alternative estimates, one at a favorable operating point and one at a credible adverse point. Explain why the apparent improvement may not translate into a better total system. The correct comparison uses the same function, service life and boundary for each alternative rather than comparing one design at peak efficiency with another at average duty.

## 3. Scope, counterexample and failure conditions

Mixing reliability for different mission durations produces meaningless products. Product acceptance cannot rest on invented component survival rates.

A calculation is only as good as its assumed configuration. Ask whether the actual mechanism is linear, whether geometry remains unchanged, whether a temperature-dependent property was treated as fixed, and whether contact, vibration or actuator saturation could introduce a discontinuity. If the model ignores an effect because it appears small, report the evidence supporting that decision. Quantification is not a substitute for identifying hazards: an attractive weighted objective cannot excuse an unverified guard, protection feature, pressure boundary or emergency stop.

A counterexample helps establish the scope. Imagine the original design moved from a controlled teaching bench to a dirty or wet industrial location. The incoming load spectrum, corrosion exposure, calibration frequency and repair resources may be different. Name at least one parameter from the equation that remains meaningful and one omitted mechanism that becomes important. Explain how the design review would change if that mechanism is plausible. Record any consequence whose acceptability must be judged by a competent safety professional rather than inferred from a classroom equation.

## 4. Practical investigation — What is the evidence?

Maintain raw measurements, instrument calibration data, model input files and revision identifiers. An output graph without provenance cannot be independently reconstructed and should not serve as an engineering acceptance record.

**Studio assignment.** Make a mission-specific block diagram for a machine and identify common causes, repair states and functional dependencies.

**Required confirmation.** Test mission description, failure definition, component evidence and reviewed independence assumptions.

Build a reproducible notebook for this assignment. Include a sketch or diagram, table of known quantities with units, a physical basis for each relationship, and a separate list of facts that are merely assumed. Perform the calculation with independent arithmetic. If testing is proposed, explain where the sensors go and how their calibration and resolution affect the result. State what data would falsify the current design hypothesis; do not propose only measurements that could support it. Keep original data rather than overwriting it when outliers or transcription errors are discovered.

For this particular case, apply the following broader check: Write explicit hard constraints and evaluate them before comparing objective values. Use a common functional unit across alternatives. When uncertainty is large, quantify how a small adjustment in an estimated input alters the selected option. This guards against optimizing one metric while overlooking a coupled physical constraint. Report a design alternative in which the selected performance improves while some other important objective worsens. That alternative may still be appropriate, but the trade must be transparent and tied to stakeholder priorities. Before deciding, check whether the new configuration requires another supplier capability study, additional inspection or a revised safety analysis.

## 5. Exercises: calculation, design and criticism

1. **Definitions:** Explain **reliability allocation and evidence** to a technician who knows the equipment but has not studied the model. State the measurable event, required operating condition and one assumption that cannot be read directly from the output.
2. **Hand calculation:** Reproduce the worked case and its governing rule `R_series = Π_i R_i` with all units and significant figures justified. Change one input by +10% and determine whether the direction of change is physically plausible.
3. **Boundary case:** Analyze the specific limitation: Mixing reliability for different mission durations produces meaningless products. Product acceptance cannot rest on invented component survival rates. Explain which additional calculation, test or design constraint is required and why a single generic safety factor cannot solve the missing-physics problem.
4. **Alternative:** Make a mission-specific block diagram for a machine and identify common causes, repair states and functional dependencies. Propose a second feasible mechanism or component, not merely a different numerical setting of the original choice. Evaluate manufacturing and maintenance implications.
5. **Evidence:** Test mission description, failure definition, component evidence and reviewed independence assumptions. Prepare a small table of what would be measured, which instrument would be used, what uncertainty could dominate and whether the result would verify a requirement or validate intended use.

**Instructor checkpoint A.** An answer that repeats the formula without identifying the operational boundary is incomplete. The student's result must have consistent units and a clear physical sign. If the output is expressed as a ratio or probability, explain its numerical range and whether independence assumptions apply. If an optimization is involved, a design that violates a hard constraint is rejected even if its objective is lower.

**Instructor checkpoint B.** Students should distinguish a calculated output from physical evidence. Strong submissions show an independent check, a sensitivity comparison, a plausible counterexample and an actionable test plan. A poor submission uses extra decimal places, repeated simulations, or an appealing chart to imply accuracy that the inputs do not support. A recommendation is not complete without a limitation and a named action to reduce the largest consequential uncertainty.

## 6. Integration with other mechanical disciplines

The design decision in **reliability allocation and evidence** is related to **dynamics, control and mechatronic integration**. Moving mechanisms must satisfy kinematics, force and torque limits, transient control behavior and safety response. Sensor filtering introduces phase delay; actuator limits break linear assumptions. The selected mechanical transmission affects control bandwidth, heat and serviceability, so integration must be concurrent. Think about what information must pass between those two engineering teams and whether the transfer occurs as a load case, geometric tolerance, material property, signal, cost scenario or acceptance test. An interface that lacks an owner may survive several design reviews without being checked. In a final integration meeting, require each assumption to have an identified source and a planned verification activity; record deviations explicitly.

**Engineering notebook output:** One independent arithmetic check, one alternative architecture, one requirement-to-evidence row, one uncertainty statement, and one open risk item to carry into the unit capstone.


---

# U07-L05 — Verification, validation and test planning

**Unit 7: Uncertainty, Robustness, Testing and Reliability**  
**Purpose.** Evaluate one real design decision in the context of an integrated mechanical system. Students should be able to explain the physics, run a bounded calculation, test its assumptions and prepare a defensible design record.

## 1. Physical meaning and engineering relevance

A verification matrix links each requirement to evidence, analysis, inspection, demonstration or test. Validation asks whether the final system satisfies its intended use in realistic scenarios. Use risk to choose test depth and predefine acceptance criteria.

A good engineering claim starts from the exact outcome being sought and a stated operational setting. In this lesson, explain what happens during commissioning, steady operation, abnormal operation and normal service. A variable that looks constant in a laboratory exercise may change dramatically when equipment ages or moves between sites. A drawing alone cannot show every thermal, mechanical and control dependency; record interfaces and operating sequences as well. Treat the word **system** as a boundary containing components, people, controls and environmental interactions, not simply a list of purchased items.

The governing decision is linked to the unit's wider question: Nominal performance is not robust performance. Uncertain loading, material properties, wear, manufacturing variation and model inadequacy produce distributions or bounded envelopes. Verification asks whether the calculation or implementation is correct; validation asks whether the model represents the intended reality. To make the relation operational, write every variable with units, the domain over which it is expected to be useful and the physical mechanism that might violate it. When using a supplied coefficient, say whether it came from a material test, a catalog, a standard, or a hypothetical classroom choice. Do not silently combine catalog ratings at different temperatures or duty cycles. If a concept depends on an uncertain input, use its plausible interval rather than only a best-looking estimate.

## 2. Governing relation and useful calculation

**Core relation or design rule:** `Margin = (allowable − observed) / allowable`

**Worked case.** A prototype motor completes 200 repetitive moves without missing a step; that does not establish twenty years of gearbox life. The event exposure and environment do not match the broad claim.

The first check is dimensional: if the symbols represent different physical dimensions, convert to a common SI basis before evaluating. The second check is one limiting case: set a load to zero, make the design very stiff, or let an efficiency approach unity—whichever is physically relevant—and ask if the predicted direction makes sense. The third check is to estimate the size of an ignored term. A compact hand calculation is valuable because it can expose a reversed ratio or a misplaced conversion factor that would otherwise pass through a spreadsheet unnoticed.

Convert the worked case into a design memo: state the known inputs, unknown output, assumptions, calculation, units and consequence of crossing the limit. Make two alternative estimates, one at a favorable operating point and one at a credible adverse point. Explain why the apparent improvement may not translate into a better total system. The correct comparison uses the same function, service life and boundary for each alternative rather than comparing one design at peak efficiency with another at average duty.

## 3. Scope, counterexample and failure conditions

Post-hoc changing of pass thresholds invalidates conclusions. One successful device is not evidence about a production population without sampling assumptions.

A calculation is only as good as its assumed configuration. Ask whether the actual mechanism is linear, whether geometry remains unchanged, whether a temperature-dependent property was treated as fixed, and whether contact, vibration or actuator saturation could introduce a discontinuity. If the model ignores an effect because it appears small, report the evidence supporting that decision. Quantification is not a substitute for identifying hazards: an attractive weighted objective cannot excuse an unverified guard, protection feature, pressure boundary or emergency stop.

A counterexample helps establish the scope. Imagine the original design moved from a controlled teaching bench to a dirty or wet industrial location. The incoming load spectrum, corrosion exposure, calibration frequency and repair resources may be different. Name at least one parameter from the equation that remains meaningful and one omitted mechanism that becomes important. Explain how the design review would change if that mechanism is plausible. Record any consequence whose acceptability must be judged by a competent safety professional rather than inferred from a classroom equation.

## 4. Practical investigation — What could reverse the decision?

Identify the single uncertain parameter most likely to change the preferred alternative. Design a low-risk test that would measure it and record what evidence would justify changing the recommendation.

**Studio assignment.** Develop a 15-point acceptance test matrix for an indexing table, including electrical and mechanical fault states.

**Required confirmation.** Signed protocols, raw measurements, traceable deviations, retest logic and design change records.

Build a reproducible notebook for this assignment. Include a sketch or diagram, table of known quantities with units, a physical basis for each relationship, and a separate list of facts that are merely assumed. Perform the calculation with independent arithmetic. If testing is proposed, explain where the sensors go and how their calibration and resolution affect the result. State what data would falsify the current design hypothesis; do not propose only measurements that could support it. Keep original data rather than overwriting it when outliers or transcription errors are discovered.

For this particular case, apply the following broader check: Track interfaces where heat, stress, force, motion, pressure and dimensions interact. The correct limit often depends on the combined operating state rather than the maximum of one isolated variable. This guards against optimizing one metric while overlooking a coupled physical constraint. Report a design alternative in which the selected performance improves while some other important objective worsens. That alternative may still be appropriate, but the trade must be transparent and tied to stakeholder priorities. Before deciding, check whether the new configuration requires another supplier capability study, additional inspection or a revised safety analysis.

## 5. Exercises: calculation, design and criticism

1. **Definitions:** Explain **verification, validation and test planning** to a technician who knows the equipment but has not studied the model. State the measurable event, required operating condition and one assumption that cannot be read directly from the output.
2. **Hand calculation:** Reproduce the worked case and its governing rule `Margin = (allowable − observed) / allowable` with all units and significant figures justified. Change one input by +10% and determine whether the direction of change is physically plausible.
3. **Boundary case:** Analyze the specific limitation: Post-hoc changing of pass thresholds invalidates conclusions. One successful device is not evidence about a production population without sampling assumptions. Explain which additional calculation, test or design constraint is required and why a single generic safety factor cannot solve the missing-physics problem.
4. **Alternative:** Develop a 15-point acceptance test matrix for an indexing table, including electrical and mechanical fault states. Propose a second feasible mechanism or component, not merely a different numerical setting of the original choice. Evaluate manufacturing and maintenance implications.
5. **Evidence:** Signed protocols, raw measurements, traceable deviations, retest logic and design change records. Prepare a small table of what would be measured, which instrument would be used, what uncertainty could dominate and whether the result would verify a requirement or validate intended use.

**Instructor checkpoint A.** An answer that repeats the formula without identifying the operational boundary is incomplete. The student's result must have consistent units and a clear physical sign. If the output is expressed as a ratio or probability, explain its numerical range and whether independence assumptions apply. If an optimization is involved, a design that violates a hard constraint is rejected even if its objective is lower.

**Instructor checkpoint B.** Students should distinguish a calculated output from physical evidence. Strong submissions show an independent check, a sensitivity comparison, a plausible counterexample and an actionable test plan. A poor submission uses extra decimal places, repeated simulations, or an appealing chart to imply accuracy that the inputs do not support. A recommendation is not complete without a limitation and a named action to reduce the largest consequential uncertainty.

## 6. Integration with other mechanical disciplines

The design decision in **verification, validation and test planning** is related to **manufacturing, supply chain and sustainable design**. A design that cannot be made, inspected, acquired, repaired or recycled at the expected scale is incomplete. Manufacturing decisions control achievable tolerances, surface integrity, defect distributions, lead times and unit economics. Environmental comparisons must use a consistent functional unit and lifecycle boundary. Think about what information must pass between those two engineering teams and whether the transfer occurs as a load case, geometric tolerance, material property, signal, cost scenario or acceptance test. An interface that lacks an owner may survive several design reviews without being checked. In a final integration meeting, require each assumption to have an identified source and a planned verification activity; record deviations explicitly.

**Engineering notebook output:** One independent arithmetic check, one alternative architecture, one requirement-to-evidence row, one uncertainty statement, and one open risk item to carry into the unit capstone.


---

