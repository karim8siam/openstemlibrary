# Unit 02: Physics-Based Modeling and Digital Engineering

**Course Code**: MSO 402 · **Level**: Advanced Undergraduate Engineering

## Unit Overview & Physical Foundations

This comprehensive university textbook unit covers the theoretical framework, physical modeling, mathematical governing equations, and engineering applications of **Physics-Based Modeling and Digital Engineering**.

# U02-L01 — Conservation laws and model boundaries

**Unit 2: Physics-Based Modeling and Digital Engineering**  
**Purpose.** Evaluate one real design decision in the context of an integrated mechanical system. Students should be able to explain the physics, run a bounded calculation, test its assumptions and prepare a defensible design record.

## 1. Physical meaning and engineering relevance

Begin with control volume and conservation of mass, linear momentum and energy before selecting a convenient empirical correlation. Clearly define open and closed boundaries; an apparently missing term often represents an uncontrolled energy flow.

A good engineering claim starts from the exact outcome being sought and a stated operational setting. In this lesson, explain what happens during commissioning, steady operation, abnormal operation and normal service. A variable that looks constant in a laboratory exercise may change dramatically when equipment ages or moves between sites. A drawing alone cannot show every thermal, mechanical and control dependency; record interfaces and operating sequences as well. Treat the word **system** as a boundary containing components, people, controls and environmental interactions, not simply a list of purchased items.

The governing decision is linked to the unit's wider question: A useful model states assumptions, state variables, boundary conditions, conservation relations and applicable time scale. A model is not a digital twin merely because it has a dashboard. Its predictive usefulness rests on calibration, identification and comparison with measurements independent of fitting data. To make the relation operational, write every variable with units, the domain over which it is expected to be useful and the physical mechanism that might violate it. When using a supplied coefficient, say whether it came from a material test, a catalog, a standard, or a hypothetical classroom choice. Do not silently combine catalog ratings at different temperatures or duty cycles. If a concept depends on an uncertain input, use its plausible interval rather than only a best-looking estimate.

## 2. Governing relation and useful calculation

**Core relation or design rule:** `dE/dt = Qin − Qout + Win − Wout`

**Worked case.** For a 2 kW electrical heater delivering 1.5 kW to a fluid at steady state, at least 0.5 kW is not reaching the fluid. That difference may be heat loss or a mismatch in instrumentation boundaries.

The first check is dimensional: if the symbols represent different physical dimensions, convert to a common SI basis before evaluating. The second check is one limiting case: set a load to zero, make the design very stiff, or let an efficiency approach unity—whichever is physically relevant—and ask if the predicted direction makes sense. The third check is to estimate the size of an ignored term. A compact hand calculation is valuable because it can expose a reversed ratio or a misplaced conversion factor that would otherwise pass through a spreadsheet unnoticed.

Convert the worked case into a design memo: state the known inputs, unknown output, assumptions, calculation, units and consequence of crossing the limit. Make two alternative estimates, one at a favorable operating point and one at a credible adverse point. Explain why the apparent improvement may not translate into a better total system. The correct comparison uses the same function, service life and boundary for each alternative rather than comparing one design at peak efficiency with another at average duty.

## 3. Scope, counterexample and failure conditions

Confusing heat with stored energy or neglecting shaft work causes inconsistent budgets. A steady state equation cannot predict warm-up duration.

A calculation is only as good as its assumed configuration. Ask whether the actual mechanism is linear, whether geometry remains unchanged, whether a temperature-dependent property was treated as fixed, and whether contact, vibration or actuator saturation could introduce a discontinuity. If the model ignores an effect because it appears small, report the evidence supporting that decision. Quantification is not a substitute for identifying hazards: an attractive weighted objective cannot excuse an unverified guard, protection feature, pressure boundary or emergency stop.

A counterexample helps establish the scope. Imagine the original design moved from a controlled teaching bench to a dirty or wet industrial location. The incoming load spectrum, corrosion exposure, calibration frequency and repair resources may be different. Name at least one parameter from the equation that remains meaningful and one omitted mechanism that becomes important. Explain how the design review would change if that mechanism is plausible. Record any consequence whose acceptability must be judged by a competent safety professional rather than inferred from a classroom equation.

## 4. Practical investigation — What is controlled?

State the decision variable, its allowed range, and which physical observations it can change. A variable that cannot be adjusted by the engineer is a disturbance or measured parameter; confusing the two makes the optimization unrealistic.

**Studio assignment.** Create a diagram with measurable power, enthalpy and thermal leakage terms, and check that all flows use consistent sign conventions.

**Required confirmation.** Energy-balance residual across several load points with separately measured input and output.

Build a reproducible notebook for this assignment. Include a sketch or diagram, table of known quantities with units, a physical basis for each relationship, and a separate list of facts that are merely assumed. Perform the calculation with independent arithmetic. If testing is proposed, explain where the sensors go and how their calibration and resolution affect the result. State what data would falsify the current design hypothesis; do not propose only measurements that could support it. Keep original data rather than overwriting it when outliers or transcription errors are discovered.

For this particular case, apply the following broader check: Write explicit hard constraints and evaluate them before comparing objective values. Use a common functional unit across alternatives. When uncertainty is large, quantify how a small adjustment in an estimated input alters the selected option. This guards against optimizing one metric while overlooking a coupled physical constraint. Report a design alternative in which the selected performance improves while some other important objective worsens. That alternative may still be appropriate, but the trade must be transparent and tied to stakeholder priorities. Before deciding, check whether the new configuration requires another supplier capability study, additional inspection or a revised safety analysis.

## 5. Exercises: calculation, design and criticism

1. **Definitions:** Explain **conservation laws and model boundaries** to a technician who knows the equipment but has not studied the model. State the measurable event, required operating condition and one assumption that cannot be read directly from the output.
2. **Hand calculation:** Reproduce the worked case and its governing rule `dE/dt = Qin − Qout + Win − Wout` with all units and significant figures justified. Change one input by +10% and determine whether the direction of change is physically plausible.
3. **Boundary case:** Analyze the specific limitation: Confusing heat with stored energy or neglecting shaft work causes inconsistent budgets. A steady state equation cannot predict warm-up duration. Explain which additional calculation, test or design constraint is required and why a single generic safety factor cannot solve the missing-physics problem.
4. **Alternative:** Create a diagram with measurable power, enthalpy and thermal leakage terms, and check that all flows use consistent sign conventions. Propose a second feasible mechanism or component, not merely a different numerical setting of the original choice. Evaluate manufacturing and maintenance implications.
5. **Evidence:** Energy-balance residual across several load points with separately measured input and output. Prepare a small table of what would be measured, which instrument would be used, what uncertainty could dominate and whether the result would verify a requirement or validate intended use.

**Instructor checkpoint A.** An answer that repeats the formula without identifying the operational boundary is incomplete. The student's result must have consistent units and a clear physical sign. If the output is expressed as a ratio or probability, explain its numerical range and whether independence assumptions apply. If an optimization is involved, a design that violates a hard constraint is rejected even if its objective is lower.

**Instructor checkpoint B.** Students should distinguish a calculated output from physical evidence. Strong submissions show an independent check, a sensitivity comparison, a plausible counterexample and an actionable test plan. A poor submission uses extra decimal places, repeated simulations, or an appealing chart to imply accuracy that the inputs do not support. A recommendation is not complete without a limitation and a named action to reduce the largest consequential uncertainty.

## 6. Integration with other mechanical disciplines

The design decision in **conservation laws and model boundaries** is related to **dynamics, control and mechatronic integration**. Moving mechanisms must satisfy kinematics, force and torque limits, transient control behavior and safety response. Sensor filtering introduces phase delay; actuator limits break linear assumptions. The selected mechanical transmission affects control bandwidth, heat and serviceability, so integration must be concurrent. Think about what information must pass between those two engineering teams and whether the transfer occurs as a load case, geometric tolerance, material property, signal, cost scenario or acceptance test. An interface that lacks an owner may survive several design reviews without being checked. In a final integration meeting, require each assumption to have an identified source and a planned verification activity; record deviations explicitly.

**Engineering notebook output:** One independent arithmetic check, one alternative architecture, one requirement-to-evidence row, one uncertainty statement, and one open risk item to carry into the unit capstone.


---

# U02-L02 — Dimensional analysis and similarity

**Unit 2: Physics-Based Modeling and Digital Engineering**  
**Purpose.** Evaluate one real design decision in the context of an integrated mechanical system. Students should be able to explain the physics, run a bounded calculation, test its assumptions and prepare a defensible design record.

## 1. Physical meaning and engineering relevance

Dimensionless groups make results comparable across scale and reveal which variables a proposed law omitted. Similarity is limited when geometry, roughness, compressibility or relevant regimes differ between prototype and product.

A good engineering claim starts from the exact outcome being sought and a stated operational setting. In this lesson, explain what happens during commissioning, steady operation, abnormal operation and normal service. A variable that looks constant in a laboratory exercise may change dramatically when equipment ages or moves between sites. A drawing alone cannot show every thermal, mechanical and control dependency; record interfaces and operating sequences as well. Treat the word **system** as a boundary containing components, people, controls and environmental interactions, not simply a list of purchased items.

The governing decision is linked to the unit's wider question: A useful model states assumptions, state variables, boundary conditions, conservation relations and applicable time scale. A model is not a digital twin merely because it has a dashboard. Its predictive usefulness rests on calibration, identification and comparison with measurements independent of fitting data. To make the relation operational, write every variable with units, the domain over which it is expected to be useful and the physical mechanism that might violate it. When using a supplied coefficient, say whether it came from a material test, a catalog, a standard, or a hypothetical classroom choice. Do not silently combine catalog ratings at different temperatures or duty cycles. If a concept depends on an uncertain input, use its plausible interval rather than only a best-looking estimate.

## 2. Governing relation and useful calculation

**Core relation or design rule:** `Re = ρVD/μ`

**Worked case.** Water flowing at 1 m/s in a 20 mm tube has Reynolds number about 20,000 if kinematic viscosity is 10^-6 m²/s. The same velocity and diameter with much more viscous oil can behave very differently.

The first check is dimensional: if the symbols represent different physical dimensions, convert to a common SI basis before evaluating. The second check is one limiting case: set a load to zero, make the design very stiff, or let an efficiency approach unity—whichever is physically relevant—and ask if the predicted direction makes sense. The third check is to estimate the size of an ignored term. A compact hand calculation is valuable because it can expose a reversed ratio or a misplaced conversion factor that would otherwise pass through a spreadsheet unnoticed.

Convert the worked case into a design memo: state the known inputs, unknown output, assumptions, calculation, units and consequence of crossing the limit. Make two alternative estimates, one at a favorable operating point and one at a credible adverse point. Explain why the apparent improvement may not translate into a better total system. The correct comparison uses the same function, service life and boundary for each alternative rather than comparing one design at peak efficiency with another at average duty.

## 3. Scope, counterexample and failure conditions

A model turbine scaled in size and speed may match Reynolds number but fail to match Mach or cavitation number. Similar shape alone is not dynamic similarity.

A calculation is only as good as its assumed configuration. Ask whether the actual mechanism is linear, whether geometry remains unchanged, whether a temperature-dependent property was treated as fixed, and whether contact, vibration or actuator saturation could introduce a discontinuity. If the model ignores an effect because it appears small, report the evidence supporting that decision. Quantification is not a substitute for identifying hazards: an attractive weighted objective cannot excuse an unverified guard, protection feature, pressure boundary or emergency stop.

A counterexample helps establish the scope. Imagine the original design moved from a controlled teaching bench to a dirty or wet industrial location. The incoming load spectrum, corrosion exposure, calibration frequency and repair resources may be different. Name at least one parameter from the equation that remains meaningful and one omitted mechanism that becomes important. Explain how the design review would change if that mechanism is plausible. Record any consequence whose acceptability must be judged by a competent safety professional rather than inferred from a classroom equation.

## 4. Practical investigation — What is conserved?

Start by tracing mass, force, energy or information through the studied boundary. Write down any neglected source, loss or interface. When a numerical output appears to violate a conservation statement, inspect boundary definitions before changing the data.

**Studio assignment.** Identify three relevant dimensionless groups for a ducted fan test and explain which ones the laboratory setup cannot simultaneously match.

**Required confirmation.** Dimensional audit and regime comparison with a clearly labeled extrapolation boundary.

Build a reproducible notebook for this assignment. Include a sketch or diagram, table of known quantities with units, a physical basis for each relationship, and a separate list of facts that are merely assumed. Perform the calculation with independent arithmetic. If testing is proposed, explain where the sensors go and how their calibration and resolution affect the result. State what data would falsify the current design hypothesis; do not propose only measurements that could support it. Keep original data rather than overwriting it when outliers or transcription errors are discovered.

For this particular case, apply the following broader check: Track interfaces where heat, stress, force, motion, pressure and dimensions interact. The correct limit often depends on the combined operating state rather than the maximum of one isolated variable. This guards against optimizing one metric while overlooking a coupled physical constraint. Report a design alternative in which the selected performance improves while some other important objective worsens. That alternative may still be appropriate, but the trade must be transparent and tied to stakeholder priorities. Before deciding, check whether the new configuration requires another supplier capability study, additional inspection or a revised safety analysis.

## 5. Exercises: calculation, design and criticism

1. **Definitions:** Explain **dimensional analysis and similarity** to a technician who knows the equipment but has not studied the model. State the measurable event, required operating condition and one assumption that cannot be read directly from the output.
2. **Hand calculation:** Reproduce the worked case and its governing rule `Re = ρVD/μ` with all units and significant figures justified. Change one input by +10% and determine whether the direction of change is physically plausible.
3. **Boundary case:** Analyze the specific limitation: A model turbine scaled in size and speed may match Reynolds number but fail to match Mach or cavitation number. Similar shape alone is not dynamic similarity. Explain which additional calculation, test or design constraint is required and why a single generic safety factor cannot solve the missing-physics problem.
4. **Alternative:** Identify three relevant dimensionless groups for a ducted fan test and explain which ones the laboratory setup cannot simultaneously match. Propose a second feasible mechanism or component, not merely a different numerical setting of the original choice. Evaluate manufacturing and maintenance implications.
5. **Evidence:** Dimensional audit and regime comparison with a clearly labeled extrapolation boundary. Prepare a small table of what would be measured, which instrument would be used, what uncertainty could dominate and whether the result would verify a requirement or validate intended use.

**Instructor checkpoint A.** An answer that repeats the formula without identifying the operational boundary is incomplete. The student's result must have consistent units and a clear physical sign. If the output is expressed as a ratio or probability, explain its numerical range and whether independence assumptions apply. If an optimization is involved, a design that violates a hard constraint is rejected even if its objective is lower.

**Instructor checkpoint B.** Students should distinguish a calculated output from physical evidence. Strong submissions show an independent check, a sensitivity comparison, a plausible counterexample and an actionable test plan. A poor submission uses extra decimal places, repeated simulations, or an appealing chart to imply accuracy that the inputs do not support. A recommendation is not complete without a limitation and a named action to reduce the largest consequential uncertainty.

## 6. Integration with other mechanical disciplines

The design decision in **dimensional analysis and similarity** is related to **manufacturing, supply chain and sustainable design**. A design that cannot be made, inspected, acquired, repaired or recycled at the expected scale is incomplete. Manufacturing decisions control achievable tolerances, surface integrity, defect distributions, lead times and unit economics. Environmental comparisons must use a consistent functional unit and lifecycle boundary. Think about what information must pass between those two engineering teams and whether the transfer occurs as a load case, geometric tolerance, material property, signal, cost scenario or acceptance test. An interface that lacks an owner may survive several design reviews without being checked. In a final integration meeting, require each assumption to have an identified source and a planned verification activity; record deviations explicitly.

**Engineering notebook output:** One independent arithmetic check, one alternative architecture, one requirement-to-evidence row, one uncertainty statement, and one open risk item to carry into the unit capstone.


---

# U02-L03 — Reduced-order and surrogate modeling

**Unit 2: Physics-Based Modeling and Digital Engineering**  
**Purpose.** Evaluate one real design decision in the context of an integrated mechanical system. Students should be able to explain the physics, run a bounded calculation, test its assumptions and prepare a defensible design record.

## 1. Physical meaning and engineering relevance

A reduced model retains the dominant dynamics or responses while discarding details that do not change the decision. Parameter fitting should use separate training and validation subsets, and surrogate errors should be reported in physically meaningful units.

A good engineering claim starts from the exact outcome being sought and a stated operational setting. In this lesson, explain what happens during commissioning, steady operation, abnormal operation and normal service. A variable that looks constant in a laboratory exercise may change dramatically when equipment ages or moves between sites. A drawing alone cannot show every thermal, mechanical and control dependency; record interfaces and operating sequences as well. Treat the word **system** as a boundary containing components, people, controls and environmental interactions, not simply a list of purchased items.

The governing decision is linked to the unit's wider question: A useful model states assumptions, state variables, boundary conditions, conservation relations and applicable time scale. A model is not a digital twin merely because it has a dashboard. Its predictive usefulness rests on calibration, identification and comparison with measurements independent of fitting data. To make the relation operational, write every variable with units, the domain over which it is expected to be useful and the physical mechanism that might violate it. When using a supplied coefficient, say whether it came from a material test, a catalog, a standard, or a hypothetical classroom choice. Do not silently combine catalog ratings at different temperatures or duty cycles. If a concept depends on an uncertain input, use its plausible interval rather than only a best-looking estimate.

## 2. Governing relation and useful calculation

**Core relation or design rule:** `y ≈ a0 + a1x + a2x²`

**Worked case.** A quadratic pump-efficiency surrogate fitted to five operating points may work locally but can predict efficiency above unity outside its fitted range. Clip-free physical validation is more important than a visually smooth curve.

The first check is dimensional: if the symbols represent different physical dimensions, convert to a common SI basis before evaluating. The second check is one limiting case: set a load to zero, make the design very stiff, or let an efficiency approach unity—whichever is physically relevant—and ask if the predicted direction makes sense. The third check is to estimate the size of an ignored term. A compact hand calculation is valuable because it can expose a reversed ratio or a misplaced conversion factor that would otherwise pass through a spreadsheet unnoticed.

Convert the worked case into a design memo: state the known inputs, unknown output, assumptions, calculation, units and consequence of crossing the limit. Make two alternative estimates, one at a favorable operating point and one at a credible adverse point. Explain why the apparent improvement may not translate into a better total system. The correct comparison uses the same function, service life and boundary for each alternative rather than comparing one design at peak efficiency with another at average duty.

## 3. Scope, counterexample and failure conditions

High fit accuracy is not evidence of causality or correct behavior under extrapolation. Optimization can exploit surrogate defects unless bounds and error checks are enforced.

A calculation is only as good as its assumed configuration. Ask whether the actual mechanism is linear, whether geometry remains unchanged, whether a temperature-dependent property was treated as fixed, and whether contact, vibration or actuator saturation could introduce a discontinuity. If the model ignores an effect because it appears small, report the evidence supporting that decision. Quantification is not a substitute for identifying hazards: an attractive weighted objective cannot excuse an unverified guard, protection feature, pressure boundary or emergency stop.

A counterexample helps establish the scope. Imagine the original design moved from a controlled teaching bench to a dirty or wet industrial location. The incoming load spectrum, corrosion exposure, calibration frequency and repair resources may be different. Name at least one parameter from the equation that remains meaningful and one omitted mechanism that becomes important. Explain how the design review would change if that mechanism is plausible. Record any consequence whose acceptability must be judged by a competent safety professional rather than inferred from a classroom equation.

## 4. Practical investigation — Where are the limits?

Report physical operating limits, catalog limits and mandated safeguards separately. A design which fails an essential condition is not acceptable just because its average objective value is attractive.

**Studio assignment.** Fit a curve to synthetic measurements, reserve one point for testing and compare prediction uncertainty to the design margin.

**Required confirmation.** Residual plot, holdout error, fitted interval, parameter units and physical plausibility test.

Build a reproducible notebook for this assignment. Include a sketch or diagram, table of known quantities with units, a physical basis for each relationship, and a separate list of facts that are merely assumed. Perform the calculation with independent arithmetic. If testing is proposed, explain where the sensors go and how their calibration and resolution affect the result. State what data would falsify the current design hypothesis; do not propose only measurements that could support it. Keep original data rather than overwriting it when outliers or transcription errors are discovered.

For this particular case, apply the following broader check: Evaluate dynamic response using an identified inertia, stiffness, damping and actuator torque-speed curve. Verify sensing and sampling delays, saturations, and the behavior of the machine after power interruption. This guards against optimizing one metric while overlooking a coupled physical constraint. Report a design alternative in which the selected performance improves while some other important objective worsens. That alternative may still be appropriate, but the trade must be transparent and tied to stakeholder priorities. Before deciding, check whether the new configuration requires another supplier capability study, additional inspection or a revised safety analysis.

## 5. Exercises: calculation, design and criticism

1. **Definitions:** Explain **reduced-order and surrogate modeling** to a technician who knows the equipment but has not studied the model. State the measurable event, required operating condition and one assumption that cannot be read directly from the output.
2. **Hand calculation:** Reproduce the worked case and its governing rule `y ≈ a0 + a1x + a2x²` with all units and significant figures justified. Change one input by +10% and determine whether the direction of change is physically plausible.
3. **Boundary case:** Analyze the specific limitation: High fit accuracy is not evidence of causality or correct behavior under extrapolation. Optimization can exploit surrogate defects unless bounds and error checks are enforced. Explain which additional calculation, test or design constraint is required and why a single generic safety factor cannot solve the missing-physics problem.
4. **Alternative:** Fit a curve to synthetic measurements, reserve one point for testing and compare prediction uncertainty to the design margin. Propose a second feasible mechanism or component, not merely a different numerical setting of the original choice. Evaluate manufacturing and maintenance implications.
5. **Evidence:** Residual plot, holdout error, fitted interval, parameter units and physical plausibility test. Prepare a small table of what would be measured, which instrument would be used, what uncertainty could dominate and whether the result would verify a requirement or validate intended use.

**Instructor checkpoint A.** An answer that repeats the formula without identifying the operational boundary is incomplete. The student's result must have consistent units and a clear physical sign. If the output is expressed as a ratio or probability, explain its numerical range and whether independence assumptions apply. If an optimization is involved, a design that violates a hard constraint is rejected even if its objective is lower.

**Instructor checkpoint B.** Students should distinguish a calculated output from physical evidence. Strong submissions show an independent check, a sensitivity comparison, a plausible counterexample and an actionable test plan. A poor submission uses extra decimal places, repeated simulations, or an appealing chart to imply accuracy that the inputs do not support. A recommendation is not complete without a limitation and a named action to reduce the largest consequential uncertainty.

## 6. Integration with other mechanical disciplines

The design decision in **reduced-order and surrogate modeling** is related to **uncertainty, robustness, testing and reliability**. Nominal performance is not robust performance. Uncertain loading, material properties, wear, manufacturing variation and model inadequacy produce distributions or bounded envelopes. Verification asks whether the calculation or implementation is correct; validation asks whether the model represents the intended reality. Think about what information must pass between those two engineering teams and whether the transfer occurs as a load case, geometric tolerance, material property, signal, cost scenario or acceptance test. An interface that lacks an owner may survive several design reviews without being checked. In a final integration meeting, require each assumption to have an identified source and a planned verification activity; record deviations explicitly.

**Engineering notebook output:** One independent arithmetic check, one alternative architecture, one requirement-to-evidence row, one uncertainty statement, and one open risk item to carry into the unit capstone.


---

# U02-L04 — Digital model configuration and provenance

**Unit 2: Physics-Based Modeling and Digital Engineering**  
**Purpose.** Evaluate one real design decision in the context of an integrated mechanical system. Students should be able to explain the physics, run a bounded calculation, test its assumptions and prepare a defensible design record.

## 1. Physical meaning and engineering relevance

Treat computational analyses as controlled engineering records. Log geometry revision, assumptions, solver version, material card, mesh density, load-case name and reviewer. Automation makes it easier to reproduce errors at scale if provenance is missing.

A good engineering claim starts from the exact outcome being sought and a stated operational setting. In this lesson, explain what happens during commissioning, steady operation, abnormal operation and normal service. A variable that looks constant in a laboratory exercise may change dramatically when equipment ages or moves between sites. A drawing alone cannot show every thermal, mechanical and control dependency; record interfaces and operating sequences as well. Treat the word **system** as a boundary containing components, people, controls and environmental interactions, not simply a list of purchased items.

The governing decision is linked to the unit's wider question: A useful model states assumptions, state variables, boundary conditions, conservation relations and applicable time scale. A model is not a digital twin merely because it has a dashboard. Its predictive usefulness rests on calibration, identification and comparison with measurements independent of fitting data. To make the relation operational, write every variable with units, the domain over which it is expected to be useful and the physical mechanism that might violate it. When using a supplied coefficient, say whether it came from a material test, a catalog, a standard, or a hypothetical classroom choice. Do not silently combine catalog ratings at different temperatures or duty cycles. If a concept depends on an uncertain input, use its plausible interval rather than only a best-looking estimate.

## 2. Governing relation and useful calculation

**Core relation or design rule:** `Result = f(inputs, assumptions, model revision)`

**Worked case.** Two finite-element analyses both report 80 MPa but use different contacts, boundary supports and material temperatures. Without a model fingerprint these results cannot be legitimately compared.

The first check is dimensional: if the symbols represent different physical dimensions, convert to a common SI basis before evaluating. The second check is one limiting case: set a load to zero, make the design very stiff, or let an efficiency approach unity—whichever is physically relevant—and ask if the predicted direction makes sense. The third check is to estimate the size of an ignored term. A compact hand calculation is valuable because it can expose a reversed ratio or a misplaced conversion factor that would otherwise pass through a spreadsheet unnoticed.

Convert the worked case into a design memo: state the known inputs, unknown output, assumptions, calculation, units and consequence of crossing the limit. Make two alternative estimates, one at a favorable operating point and one at a credible adverse point. Explain why the apparent improvement may not translate into a better total system. The correct comparison uses the same function, service life and boundary for each alternative rather than comparing one design at peak efficiency with another at average duty.

## 3. Scope, counterexample and failure conditions

A screenshot of a color plot is not sufficient evidence of convergence, correct boundary conditions or correct sign conventions.

A calculation is only as good as its assumed configuration. Ask whether the actual mechanism is linear, whether geometry remains unchanged, whether a temperature-dependent property was treated as fixed, and whether contact, vibration or actuator saturation could introduce a discontinuity. If the model ignores an effect because it appears small, report the evidence supporting that decision. Quantification is not a substitute for identifying hazards: an attractive weighted objective cannot excuse an unverified guard, protection feature, pressure boundary or emergency stop.

A counterexample helps establish the scope. Imagine the original design moved from a controlled teaching bench to a dirty or wet industrial location. The incoming load spectrum, corrosion exposure, calibration frequency and repair resources may be different. Name at least one parameter from the equation that remains meaningful and one omitted mechanism that becomes important. Explain how the design review would change if that mechanism is plausible. Record any consequence whose acceptability must be judged by a competent safety professional rather than inferred from a classroom equation.

## 4. Practical investigation — What is the evidence?

Maintain raw measurements, instrument calibration data, model input files and revision identifiers. An output graph without provenance cannot be independently reconstructed and should not serve as an engineering acceptance record.

**Studio assignment.** Publish one example run with a plain-text manifest, all inputs, a reproducible solver command and a record of changed assumptions.

**Required confirmation.** Independent re-run producing compatible outputs and a signed deviation log.

Build a reproducible notebook for this assignment. Include a sketch or diagram, table of known quantities with units, a physical basis for each relationship, and a separate list of facts that are merely assumed. Perform the calculation with independent arithmetic. If testing is proposed, explain where the sensors go and how their calibration and resolution affect the result. State what data would falsify the current design hypothesis; do not propose only measurements that could support it. Keep original data rather than overwriting it when outliers or transcription errors are discovered.

For this particular case, apply the following broader check: Consider the entire manufacturing route and the support work needed during the product life. Use consistent measurements for process yield, geometry, inspection and service time. This guards against optimizing one metric while overlooking a coupled physical constraint. Report a design alternative in which the selected performance improves while some other important objective worsens. That alternative may still be appropriate, but the trade must be transparent and tied to stakeholder priorities. Before deciding, check whether the new configuration requires another supplier capability study, additional inspection or a revised safety analysis.

## 5. Exercises: calculation, design and criticism

1. **Definitions:** Explain **digital model configuration and provenance** to a technician who knows the equipment but has not studied the model. State the measurable event, required operating condition and one assumption that cannot be read directly from the output.
2. **Hand calculation:** Reproduce the worked case and its governing rule `Result = f(inputs, assumptions, model revision)` with all units and significant figures justified. Change one input by +10% and determine whether the direction of change is physically plausible.
3. **Boundary case:** Analyze the specific limitation: A screenshot of a color plot is not sufficient evidence of convergence, correct boundary conditions or correct sign conventions. Explain which additional calculation, test or design constraint is required and why a single generic safety factor cannot solve the missing-physics problem.
4. **Alternative:** Publish one example run with a plain-text manifest, all inputs, a reproducible solver command and a record of changed assumptions. Propose a second feasible mechanism or component, not merely a different numerical setting of the original choice. Evaluate manufacturing and maintenance implications.
5. **Evidence:** Independent re-run producing compatible outputs and a signed deviation log. Prepare a small table of what would be measured, which instrument would be used, what uncertainty could dominate and whether the result would verify a requirement or validate intended use.

**Instructor checkpoint A.** An answer that repeats the formula without identifying the operational boundary is incomplete. The student's result must have consistent units and a clear physical sign. If the output is expressed as a ratio or probability, explain its numerical range and whether independence assumptions apply. If an optimization is involved, a design that violates a hard constraint is rejected even if its objective is lower.

**Instructor checkpoint B.** Students should distinguish a calculated output from physical evidence. Strong submissions show an independent check, a sensitivity comparison, a plausible counterexample and an actionable test plan. A poor submission uses extra decimal places, repeated simulations, or an appealing chart to imply accuracy that the inputs do not support. A recommendation is not complete without a limitation and a named action to reduce the largest consequential uncertainty.

## 6. Integration with other mechanical disciplines

The design decision in **digital model configuration and provenance** is related to **integrated capstone and engineering decision-making**. System design culminates in traceable evidence and an honest decision under constraints. A useful engineering dossier ties stakeholder needs to functional architecture, engineering analysis, cost, verification, failure controls, manufacturing and eventual disposition. Unresolved risk is an outcome to report, not a number to conceal. Think about what information must pass between those two engineering teams and whether the transfer occurs as a load case, geometric tolerance, material property, signal, cost scenario or acceptance test. An interface that lacks an owner may survive several design reviews without being checked. In a final integration meeting, require each assumption to have an identified source and a planned verification activity; record deviations explicitly.

**Engineering notebook output:** One independent arithmetic check, one alternative architecture, one requirement-to-evidence row, one uncertainty statement, and one open risk item to carry into the unit capstone.


---

# U02-L05 — Model calibration and validation

**Unit 2: Physics-Based Modeling and Digital Engineering**  
**Purpose.** Evaluate one real design decision in the context of an integrated mechanical system. Students should be able to explain the physics, run a bounded calculation, test its assumptions and prepare a defensible design record.

## 1. Physical meaning and engineering relevance

Calibration adjusts uncertain model parameters from data; validation compares predictions with evidence not used for calibration. A physical model with a calibrated friction coefficient may still omit nonlinear wear or a change in lubrication regime.

A good engineering claim starts from the exact outcome being sought and a stated operational setting. In this lesson, explain what happens during commissioning, steady operation, abnormal operation and normal service. A variable that looks constant in a laboratory exercise may change dramatically when equipment ages or moves between sites. A drawing alone cannot show every thermal, mechanical and control dependency; record interfaces and operating sequences as well. Treat the word **system** as a boundary containing components, people, controls and environmental interactions, not simply a list of purchased items.

The governing decision is linked to the unit's wider question: A useful model states assumptions, state variables, boundary conditions, conservation relations and applicable time scale. A model is not a digital twin merely because it has a dashboard. Its predictive usefulness rests on calibration, identification and comparison with measurements independent of fitting data. To make the relation operational, write every variable with units, the domain over which it is expected to be useful and the physical mechanism that might violate it. When using a supplied coefficient, say whether it came from a material test, a catalog, a standard, or a hypothetical classroom choice. Do not silently combine catalog ratings at different temperatures or duty cycles. If a concept depends on an uncertain input, use its plausible interval rather than only a best-looking estimate.

## 2. Governing relation and useful calculation

**Core relation or design rule:** `Residual_i = measured_i − predicted_i`

**Worked case.** Calibrate a thermal resistance using one heat-flow experiment, then predict another at a different ambient temperature. A 2 °C bias that is small at low temperature may become critical near an insulation limit.

The first check is dimensional: if the symbols represent different physical dimensions, convert to a common SI basis before evaluating. The second check is one limiting case: set a load to zero, make the design very stiff, or let an efficiency approach unity—whichever is physically relevant—and ask if the predicted direction makes sense. The third check is to estimate the size of an ignored term. A compact hand calculation is valuable because it can expose a reversed ratio or a misplaced conversion factor that would otherwise pass through a spreadsheet unnoticed.

Convert the worked case into a design memo: state the known inputs, unknown output, assumptions, calculation, units and consequence of crossing the limit. Make two alternative estimates, one at a favorable operating point and one at a credible adverse point. Explain why the apparent improvement may not translate into a better total system. The correct comparison uses the same function, service life and boundary for each alternative rather than comparing one design at peak efficiency with another at average duty.

## 3. Scope, counterexample and failure conditions

Using the same observations to fit and validate a model overstates reliability. Sensor drift and unmodeled dynamics may masquerade as parameter errors.

A calculation is only as good as its assumed configuration. Ask whether the actual mechanism is linear, whether geometry remains unchanged, whether a temperature-dependent property was treated as fixed, and whether contact, vibration or actuator saturation could introduce a discontinuity. If the model ignores an effect because it appears small, report the evidence supporting that decision. Quantification is not a substitute for identifying hazards: an attractive weighted objective cannot excuse an unverified guard, protection feature, pressure boundary or emergency stop.

A counterexample helps establish the scope. Imagine the original design moved from a controlled teaching bench to a dirty or wet industrial location. The incoming load spectrum, corrosion exposure, calibration frequency and repair resources may be different. Name at least one parameter from the equation that remains meaningful and one omitted mechanism that becomes important. Explain how the design review would change if that mechanism is plausible. Record any consequence whose acceptability must be judged by a competent safety professional rather than inferred from a classroom equation.

## 4. Practical investigation — What could reverse the decision?

Identify the single uncertain parameter most likely to change the preferred alternative. Design a low-risk test that would measure it and record what evidence would justify changing the recommendation.

**Studio assignment.** Define a calibration data partition, measurement uncertainty and numerical acceptance rule before calculating errors.

**Required confirmation.** Independent holdout measurement with uncertainty interval and a record of model discrepancy.

Build a reproducible notebook for this assignment. Include a sketch or diagram, table of known quantities with units, a physical basis for each relationship, and a separate list of facts that are merely assumed. Perform the calculation with independent arithmetic. If testing is proposed, explain where the sensors go and how their calibration and resolution affect the result. State what data would falsify the current design hypothesis; do not propose only measurements that could support it. Keep original data rather than overwriting it when outliers or transcription errors are discovered.

For this particular case, apply the following broader check: Represent measured scatter, uncertainty in model parameters and omitted mechanisms separately. Choose verification evidence that addresses the highest-consequence failure modes, not just the easiest measurements. This guards against optimizing one metric while overlooking a coupled physical constraint. Report a design alternative in which the selected performance improves while some other important objective worsens. That alternative may still be appropriate, but the trade must be transparent and tied to stakeholder priorities. Before deciding, check whether the new configuration requires another supplier capability study, additional inspection or a revised safety analysis.

## 5. Exercises: calculation, design and criticism

1. **Definitions:** Explain **model calibration and validation** to a technician who knows the equipment but has not studied the model. State the measurable event, required operating condition and one assumption that cannot be read directly from the output.
2. **Hand calculation:** Reproduce the worked case and its governing rule `Residual_i = measured_i − predicted_i` with all units and significant figures justified. Change one input by +10% and determine whether the direction of change is physically plausible.
3. **Boundary case:** Analyze the specific limitation: Using the same observations to fit and validate a model overstates reliability. Sensor drift and unmodeled dynamics may masquerade as parameter errors. Explain which additional calculation, test or design constraint is required and why a single generic safety factor cannot solve the missing-physics problem.
4. **Alternative:** Define a calibration data partition, measurement uncertainty and numerical acceptance rule before calculating errors. Propose a second feasible mechanism or component, not merely a different numerical setting of the original choice. Evaluate manufacturing and maintenance implications.
5. **Evidence:** Independent holdout measurement with uncertainty interval and a record of model discrepancy. Prepare a small table of what would be measured, which instrument would be used, what uncertainty could dominate and whether the result would verify a requirement or validate intended use.

**Instructor checkpoint A.** An answer that repeats the formula without identifying the operational boundary is incomplete. The student's result must have consistent units and a clear physical sign. If the output is expressed as a ratio or probability, explain its numerical range and whether independence assumptions apply. If an optimization is involved, a design that violates a hard constraint is rejected even if its objective is lower.

**Instructor checkpoint B.** Students should distinguish a calculated output from physical evidence. Strong submissions show an independent check, a sensitivity comparison, a plausible counterexample and an actionable test plan. A poor submission uses extra decimal places, repeated simulations, or an appealing chart to imply accuracy that the inputs do not support. A recommendation is not complete without a limitation and a named action to reduce the largest consequential uncertainty.

## 6. Integration with other mechanical disciplines

The design decision in **model calibration and validation** is related to **engineering requirements and system architecture**. A mechanical system is an arrangement of components that jointly deliver a function within physical, financial and regulatory limits. Requirements must state observable performance, mission, environment, boundaries and evidence of acceptance. A specification without a test method cannot serve as a contract between customer, designer and verifier. Think about what information must pass between those two engineering teams and whether the transfer occurs as a load case, geometric tolerance, material property, signal, cost scenario or acceptance test. An interface that lacks an owner may survive several design reviews without being checked. In a final integration meeting, require each assumption to have an identified source and a planned verification activity; record deviations explicitly.

**Engineering notebook output:** One independent arithmetic check, one alternative architecture, one requirement-to-evidence row, one uncertainty statement, and one open risk item to carry into the unit capstone.


---

