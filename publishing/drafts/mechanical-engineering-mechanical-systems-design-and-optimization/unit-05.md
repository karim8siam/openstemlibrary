# Unit 05: Dynamics, Control and Mechatronic Integration

**Course Code**: MSO 405 · **Level**: Advanced Undergraduate Engineering

## Unit Overview & Physical Foundations

This comprehensive university textbook unit covers the theoretical framework, physical modeling, mathematical governing equations, and engineering applications of **Dynamics, Control and Mechatronic Integration**.

# U05-L01 — Inertia and motion profile selection

**Unit 5: Dynamics, Control and Mechatronic Integration**  
**Purpose.** Evaluate one real design decision in the context of an integrated mechanical system. Students should be able to explain the physics, run a bounded calculation, test its assumptions and prepare a defensible design record.

## 1. Physical meaning and engineering relevance

Acceleration profiles trade cycle time against peak torque, vibration, heat and wear. Trapezoidal velocity profiles assume sharp jerk transitions; smoother S-curves reduce excitation but may require extra travel time.

A good engineering claim starts from the exact outcome being sought and a stated operational setting. In this lesson, explain what happens during commissioning, steady operation, abnormal operation and normal service. A variable that looks constant in a laboratory exercise may change dramatically when equipment ages or moves between sites. A drawing alone cannot show every thermal, mechanical and control dependency; record interfaces and operating sequences as well. Treat the word **system** as a boundary containing components, people, controls and environmental interactions, not simply a list of purchased items.

The governing decision is linked to the unit's wider question: Moving mechanisms must satisfy kinematics, force and torque limits, transient control behavior and safety response. Sensor filtering introduces phase delay; actuator limits break linear assumptions. The selected mechanical transmission affects control bandwidth, heat and serviceability, so integration must be concurrent. To make the relation operational, write every variable with units, the domain over which it is expected to be useful and the physical mechanism that might violate it. When using a supplied coefficient, say whether it came from a material test, a catalog, a standard, or a hypothetical classroom choice. Do not silently combine catalog ratings at different temperatures or duty cycles. If a concept depends on an uncertain input, use its plausible interval rather than only a best-looking estimate.

## 2. Governing relation and useful calculation

**Core relation or design rule:** `τ = Jα + τ_load`

**Worked case.** An indexing table with total inertia 0.12 kg·m² accelerating at 10 rad/s² needs at least 1.2 N·m inertial torque before friction and external load. Reflected gearbox inertia can add substantially.

The first check is dimensional: if the symbols represent different physical dimensions, convert to a common SI basis before evaluating. The second check is one limiting case: set a load to zero, make the design very stiff, or let an efficiency approach unity—whichever is physically relevant—and ask if the predicted direction makes sense. The third check is to estimate the size of an ignored term. A compact hand calculation is valuable because it can expose a reversed ratio or a misplaced conversion factor that would otherwise pass through a spreadsheet unnoticed.

Convert the worked case into a design memo: state the known inputs, unknown output, assumptions, calculation, units and consequence of crossing the limit. Make two alternative estimates, one at a favorable operating point and one at a credible adverse point. Explain why the apparent improvement may not translate into a better total system. The correct comparison uses the same function, service life and boundary for each alternative rather than comparing one design at peak efficiency with another at average duty.

## 3. Scope, counterexample and failure conditions

Motor torque curves depend on speed, supply voltage, cooling and duty. Continuous torque must not be inferred from a short-duration peak rating.

A calculation is only as good as its assumed configuration. Ask whether the actual mechanism is linear, whether geometry remains unchanged, whether a temperature-dependent property was treated as fixed, and whether contact, vibration or actuator saturation could introduce a discontinuity. If the model ignores an effect because it appears small, report the evidence supporting that decision. Quantification is not a substitute for identifying hazards: an attractive weighted objective cannot excuse an unverified guard, protection feature, pressure boundary or emergency stop.

A counterexample helps establish the scope. Imagine the original design moved from a controlled teaching bench to a dirty or wet industrial location. The incoming load spectrum, corrosion exposure, calibration frequency and repair resources may be different. Name at least one parameter from the equation that remains meaningful and one omitted mechanism that becomes important. Explain how the design review would change if that mechanism is plausible. Record any consequence whose acceptability must be judged by a competent safety professional rather than inferred from a classroom equation.

## 4. Practical investigation — What is controlled?

State the decision variable, its allowed range, and which physical observations it can change. A variable that cannot be adjusted by the engineer is a disturbance or measured parameter; confusing the two makes the optimization unrealistic.

**Studio assignment.** Compare two motion profiles with identical travel and time, then calculate likely vibration and peak electrical demand trends.

**Required confirmation.** Recorded speed and torque traces across heavy and light payloads.

Build a reproducible notebook for this assignment. Include a sketch or diagram, table of known quantities with units, a physical basis for each relationship, and a separate list of facts that are merely assumed. Perform the calculation with independent arithmetic. If testing is proposed, explain where the sensors go and how their calibration and resolution affect the result. State what data would falsify the current design hypothesis; do not propose only measurements that could support it. Keep original data rather than overwriting it when outliers or transcription errors are discovered.

For this particular case, apply the following broader check: Consider the entire manufacturing route and the support work needed during the product life. Use consistent measurements for process yield, geometry, inspection and service time. This guards against optimizing one metric while overlooking a coupled physical constraint. Report a design alternative in which the selected performance improves while some other important objective worsens. That alternative may still be appropriate, but the trade must be transparent and tied to stakeholder priorities. Before deciding, check whether the new configuration requires another supplier capability study, additional inspection or a revised safety analysis.

## 5. Exercises: calculation, design and criticism

1. **Definitions:** Explain **inertia and motion profile selection** to a technician who knows the equipment but has not studied the model. State the measurable event, required operating condition and one assumption that cannot be read directly from the output.
2. **Hand calculation:** Reproduce the worked case and its governing rule `τ = Jα + τ_load` with all units and significant figures justified. Change one input by +10% and determine whether the direction of change is physically plausible.
3. **Boundary case:** Analyze the specific limitation: Motor torque curves depend on speed, supply voltage, cooling and duty. Continuous torque must not be inferred from a short-duration peak rating. Explain which additional calculation, test or design constraint is required and why a single generic safety factor cannot solve the missing-physics problem.
4. **Alternative:** Compare two motion profiles with identical travel and time, then calculate likely vibration and peak electrical demand trends. Propose a second feasible mechanism or component, not merely a different numerical setting of the original choice. Evaluate manufacturing and maintenance implications.
5. **Evidence:** Recorded speed and torque traces across heavy and light payloads. Prepare a small table of what would be measured, which instrument would be used, what uncertainty could dominate and whether the result would verify a requirement or validate intended use.

**Instructor checkpoint A.** An answer that repeats the formula without identifying the operational boundary is incomplete. The student's result must have consistent units and a clear physical sign. If the output is expressed as a ratio or probability, explain its numerical range and whether independence assumptions apply. If an optimization is involved, a design that violates a hard constraint is rejected even if its objective is lower.

**Instructor checkpoint B.** Students should distinguish a calculated output from physical evidence. Strong submissions show an independent check, a sensitivity comparison, a plausible counterexample and an actionable test plan. A poor submission uses extra decimal places, repeated simulations, or an appealing chart to imply accuracy that the inputs do not support. A recommendation is not complete without a limitation and a named action to reduce the largest consequential uncertainty.

## 6. Integration with other mechanical disciplines

The design decision in **inertia and motion profile selection** is related to **integrated capstone and engineering decision-making**. System design culminates in traceable evidence and an honest decision under constraints. A useful engineering dossier ties stakeholder needs to functional architecture, engineering analysis, cost, verification, failure controls, manufacturing and eventual disposition. Unresolved risk is an outcome to report, not a number to conceal. Think about what information must pass between those two engineering teams and whether the transfer occurs as a load case, geometric tolerance, material property, signal, cost scenario or acceptance test. An interface that lacks an owner may survive several design reviews without being checked. In a final integration meeting, require each assumption to have an identified source and a planned verification activity; record deviations explicitly.

**Engineering notebook output:** One independent arithmetic check, one alternative architecture, one requirement-to-evidence row, one uncertainty statement, and one open risk item to carry into the unit capstone.


---

# U05-L02 — Transmission choice and backlash

**Unit 5: Dynamics, Control and Mechatronic Integration**  
**Purpose.** Evaluate one real design decision in the context of an integrated mechanical system. Students should be able to explain the physics, run a bounded calculation, test its assumptions and prepare a defensible design record.

## 1. Physical meaning and engineering relevance

Gear trains, belts, screw drives and direct-drive actuators produce different reflected inertia, efficiency, compliance and maintenance needs. Position resolution at the encoder is not identical to positional accuracy at the load.

A good engineering claim starts from the exact outcome being sought and a stated operational setting. In this lesson, explain what happens during commissioning, steady operation, abnormal operation and normal service. A variable that looks constant in a laboratory exercise may change dramatically when equipment ages or moves between sites. A drawing alone cannot show every thermal, mechanical and control dependency; record interfaces and operating sequences as well. Treat the word **system** as a boundary containing components, people, controls and environmental interactions, not simply a list of purchased items.

The governing decision is linked to the unit's wider question: Moving mechanisms must satisfy kinematics, force and torque limits, transient control behavior and safety response. Sensor filtering introduces phase delay; actuator limits break linear assumptions. The selected mechanical transmission affects control bandwidth, heat and serviceability, so integration must be concurrent. To make the relation operational, write every variable with units, the domain over which it is expected to be useful and the physical mechanism that might violate it. When using a supplied coefficient, say whether it came from a material test, a catalog, a standard, or a hypothetical classroom choice. Do not silently combine catalog ratings at different temperatures or duty cycles. If a concept depends on an uncertain input, use its plausible interval rather than only a best-looking estimate.

## 2. Governing relation and useful calculation

**Core relation or design rule:** `J_reflected = J_load / N² for ideal speed reduction N`

**Worked case.** A gearbox ratio of 5 reduces ideal reflected load inertia by 25 when referred to the motor, but adds gear inertia and introduces finite stiffness. A step command may excite output-side resonances.

The first check is dimensional: if the symbols represent different physical dimensions, convert to a common SI basis before evaluating. The second check is one limiting case: set a load to zero, make the design very stiff, or let an efficiency approach unity—whichever is physically relevant—and ask if the predicted direction makes sense. The third check is to estimate the size of an ignored term. A compact hand calculation is valuable because it can expose a reversed ratio or a misplaced conversion factor that would otherwise pass through a spreadsheet unnoticed.

Convert the worked case into a design memo: state the known inputs, unknown output, assumptions, calculation, units and consequence of crossing the limit. Make two alternative estimates, one at a favorable operating point and one at a credible adverse point. Explain why the apparent improvement may not translate into a better total system. The correct comparison uses the same function, service life and boundary for each alternative rather than comparing one design at peak efficiency with another at average duty.

## 3. Scope, counterexample and failure conditions

Ignoring backlash during direction reversal can cause deadband and limit cycles. Tightening control gains cannot eliminate a mechanical clearance.

A calculation is only as good as its assumed configuration. Ask whether the actual mechanism is linear, whether geometry remains unchanged, whether a temperature-dependent property was treated as fixed, and whether contact, vibration or actuator saturation could introduce a discontinuity. If the model ignores an effect because it appears small, report the evidence supporting that decision. Quantification is not a substitute for identifying hazards: an attractive weighted objective cannot excuse an unverified guard, protection feature, pressure boundary or emergency stop.

A counterexample helps establish the scope. Imagine the original design moved from a controlled teaching bench to a dirty or wet industrial location. The incoming load spectrum, corrosion exposure, calibration frequency and repair resources may be different. Name at least one parameter from the equation that remains meaningful and one omitted mechanism that becomes important. Explain how the design review would change if that mechanism is plausible. Record any consequence whose acceptability must be judged by a competent safety professional rather than inferred from a classroom equation.

## 4. Practical investigation — What is conserved?

Start by tracing mass, force, energy or information through the studied boundary. Write down any neglected source, loss or interface. When a numerical output appears to violate a conservation statement, inspect boundary definitions before changing the data.

**Studio assignment.** Compare a belt, geared and direct-drive table using measured reversal error, peak torque, service interval and floor area.

**Required confirmation.** Reversal hysteresis plot and a torque-speed duty-cycle check.

Build a reproducible notebook for this assignment. Include a sketch or diagram, table of known quantities with units, a physical basis for each relationship, and a separate list of facts that are merely assumed. Perform the calculation with independent arithmetic. If testing is proposed, explain where the sensors go and how their calibration and resolution affect the result. State what data would falsify the current design hypothesis; do not propose only measurements that could support it. Keep original data rather than overwriting it when outliers or transcription errors are discovered.

For this particular case, apply the following broader check: Represent measured scatter, uncertainty in model parameters and omitted mechanisms separately. Choose verification evidence that addresses the highest-consequence failure modes, not just the easiest measurements. This guards against optimizing one metric while overlooking a coupled physical constraint. Report a design alternative in which the selected performance improves while some other important objective worsens. That alternative may still be appropriate, but the trade must be transparent and tied to stakeholder priorities. Before deciding, check whether the new configuration requires another supplier capability study, additional inspection or a revised safety analysis.

## 5. Exercises: calculation, design and criticism

1. **Definitions:** Explain **transmission choice and backlash** to a technician who knows the equipment but has not studied the model. State the measurable event, required operating condition and one assumption that cannot be read directly from the output.
2. **Hand calculation:** Reproduce the worked case and its governing rule `J_reflected = J_load / N² for ideal speed reduction N` with all units and significant figures justified. Change one input by +10% and determine whether the direction of change is physically plausible.
3. **Boundary case:** Analyze the specific limitation: Ignoring backlash during direction reversal can cause deadband and limit cycles. Tightening control gains cannot eliminate a mechanical clearance. Explain which additional calculation, test or design constraint is required and why a single generic safety factor cannot solve the missing-physics problem.
4. **Alternative:** Compare a belt, geared and direct-drive table using measured reversal error, peak torque, service interval and floor area. Propose a second feasible mechanism or component, not merely a different numerical setting of the original choice. Evaluate manufacturing and maintenance implications.
5. **Evidence:** Reversal hysteresis plot and a torque-speed duty-cycle check. Prepare a small table of what would be measured, which instrument would be used, what uncertainty could dominate and whether the result would verify a requirement or validate intended use.

**Instructor checkpoint A.** An answer that repeats the formula without identifying the operational boundary is incomplete. The student's result must have consistent units and a clear physical sign. If the output is expressed as a ratio or probability, explain its numerical range and whether independence assumptions apply. If an optimization is involved, a design that violates a hard constraint is rejected even if its objective is lower.

**Instructor checkpoint B.** Students should distinguish a calculated output from physical evidence. Strong submissions show an independent check, a sensitivity comparison, a plausible counterexample and an actionable test plan. A poor submission uses extra decimal places, repeated simulations, or an appealing chart to imply accuracy that the inputs do not support. A recommendation is not complete without a limitation and a named action to reduce the largest consequential uncertainty.

## 6. Integration with other mechanical disciplines

The design decision in **transmission choice and backlash** is related to **engineering requirements and system architecture**. A mechanical system is an arrangement of components that jointly deliver a function within physical, financial and regulatory limits. Requirements must state observable performance, mission, environment, boundaries and evidence of acceptance. A specification without a test method cannot serve as a contract between customer, designer and verifier. Think about what information must pass between those two engineering teams and whether the transfer occurs as a load case, geometric tolerance, material property, signal, cost scenario or acceptance test. An interface that lacks an owner may survive several design reviews without being checked. In a final integration meeting, require each assumption to have an identified source and a planned verification activity; record deviations explicitly.

**Engineering notebook output:** One independent arithmetic check, one alternative architecture, one requirement-to-evidence row, one uncertainty statement, and one open risk item to carry into the unit capstone.


---

# U05-L03 — Frequency response and resonance separation

**Unit 5: Dynamics, Control and Mechatronic Integration**  
**Purpose.** Evaluate one real design decision in the context of an integrated mechanical system. Students should be able to explain the physics, run a bounded calculation, test its assumptions and prepare a defensible design record.

## 1. Physical meaning and engineering relevance

Excitation from motors, gears or process loads can amplify a lightly damped structure near a natural frequency. Modal testing is required when mass distribution, boundary compliance or damping is uncertain.

A good engineering claim starts from the exact outcome being sought and a stated operational setting. In this lesson, explain what happens during commissioning, steady operation, abnormal operation and normal service. A variable that looks constant in a laboratory exercise may change dramatically when equipment ages or moves between sites. A drawing alone cannot show every thermal, mechanical and control dependency; record interfaces and operating sequences as well. Treat the word **system** as a boundary containing components, people, controls and environmental interactions, not simply a list of purchased items.

The governing decision is linked to the unit's wider question: Moving mechanisms must satisfy kinematics, force and torque limits, transient control behavior and safety response. Sensor filtering introduces phase delay; actuator limits break linear assumptions. The selected mechanical transmission affects control bandwidth, heat and serviceability, so integration must be concurrent. To make the relation operational, write every variable with units, the domain over which it is expected to be useful and the physical mechanism that might violate it. When using a supplied coefficient, say whether it came from a material test, a catalog, a standard, or a hypothetical classroom choice. Do not silently combine catalog ratings at different temperatures or duty cycles. If a concept depends on an uncertain input, use its plausible interval rather than only a best-looking estimate.

## 2. Governing relation and useful calculation

**Core relation or design rule:** `f_n = (1/2π)√(k/m)`

**Worked case.** A 10 kg single-degree-of-freedom stage with 40,000 N/m equivalent stiffness has natural frequency about 10.1 Hz. Repeated 10 Hz forcing is therefore concerning even when static stresses look small.

The first check is dimensional: if the symbols represent different physical dimensions, convert to a common SI basis before evaluating. The second check is one limiting case: set a load to zero, make the design very stiff, or let an efficiency approach unity—whichever is physically relevant—and ask if the predicted direction makes sense. The third check is to estimate the size of an ignored term. A compact hand calculation is valuable because it can expose a reversed ratio or a misplaced conversion factor that would otherwise pass through a spreadsheet unnoticed.

Convert the worked case into a design memo: state the known inputs, unknown output, assumptions, calculation, units and consequence of crossing the limit. Make two alternative estimates, one at a favorable operating point and one at a credible adverse point. Explain why the apparent improvement may not translate into a better total system. The correct comparison uses the same function, service life and boundary for each alternative rather than comparing one design at peak efficiency with another at average duty.

## 3. Scope, counterexample and failure conditions

An undamped single-mode model cannot predict a flexible machine across a broad frequency range. Mounting bolts can change boundary stiffness.

A calculation is only as good as its assumed configuration. Ask whether the actual mechanism is linear, whether geometry remains unchanged, whether a temperature-dependent property was treated as fixed, and whether contact, vibration or actuator saturation could introduce a discontinuity. If the model ignores an effect because it appears small, report the evidence supporting that decision. Quantification is not a substitute for identifying hazards: an attractive weighted objective cannot excuse an unverified guard, protection feature, pressure boundary or emergency stop.

A counterexample helps establish the scope. Imagine the original design moved from a controlled teaching bench to a dirty or wet industrial location. The incoming load spectrum, corrosion exposure, calibration frequency and repair resources may be different. Name at least one parameter from the equation that remains meaningful and one omitted mechanism that becomes important. Explain how the design review would change if that mechanism is plausible. Record any consequence whose acceptability must be judged by a competent safety professional rather than inferred from a classroom equation.

## 4. Practical investigation — Where are the limits?

Report physical operating limits, catalog limits and mandated safeguards separately. A design which fails an essential condition is not acceptable just because its average objective value is attractive.

**Studio assignment.** Estimate the first mode and create a controlled tap-test plan; compare isolated and assembled configurations.

**Required confirmation.** Measured frequency-response peak, coherence and documented boundary conditions.

Build a reproducible notebook for this assignment. Include a sketch or diagram, table of known quantities with units, a physical basis for each relationship, and a separate list of facts that are merely assumed. Perform the calculation with independent arithmetic. If testing is proposed, explain where the sensors go and how their calibration and resolution affect the result. State what data would falsify the current design hypothesis; do not propose only measurements that could support it. Keep original data rather than overwriting it when outliers or transcription errors are discovered.

For this particular case, apply the following broader check: Present a traceable technical argument that allows another engineer to reconstruct the design choice. List rejected concepts, open issues, physical test evidence, planned maintenance and permitted operating limits. This guards against optimizing one metric while overlooking a coupled physical constraint. Report a design alternative in which the selected performance improves while some other important objective worsens. That alternative may still be appropriate, but the trade must be transparent and tied to stakeholder priorities. Before deciding, check whether the new configuration requires another supplier capability study, additional inspection or a revised safety analysis.

## 5. Exercises: calculation, design and criticism

1. **Definitions:** Explain **frequency response and resonance separation** to a technician who knows the equipment but has not studied the model. State the measurable event, required operating condition and one assumption that cannot be read directly from the output.
2. **Hand calculation:** Reproduce the worked case and its governing rule `f_n = (1/2π)√(k/m)` with all units and significant figures justified. Change one input by +10% and determine whether the direction of change is physically plausible.
3. **Boundary case:** Analyze the specific limitation: An undamped single-mode model cannot predict a flexible machine across a broad frequency range. Mounting bolts can change boundary stiffness. Explain which additional calculation, test or design constraint is required and why a single generic safety factor cannot solve the missing-physics problem.
4. **Alternative:** Estimate the first mode and create a controlled tap-test plan; compare isolated and assembled configurations. Propose a second feasible mechanism or component, not merely a different numerical setting of the original choice. Evaluate manufacturing and maintenance implications.
5. **Evidence:** Measured frequency-response peak, coherence and documented boundary conditions. Prepare a small table of what would be measured, which instrument would be used, what uncertainty could dominate and whether the result would verify a requirement or validate intended use.

**Instructor checkpoint A.** An answer that repeats the formula without identifying the operational boundary is incomplete. The student's result must have consistent units and a clear physical sign. If the output is expressed as a ratio or probability, explain its numerical range and whether independence assumptions apply. If an optimization is involved, a design that violates a hard constraint is rejected even if its objective is lower.

**Instructor checkpoint B.** Students should distinguish a calculated output from physical evidence. Strong submissions show an independent check, a sensitivity comparison, a plausible counterexample and an actionable test plan. A poor submission uses extra decimal places, repeated simulations, or an appealing chart to imply accuracy that the inputs do not support. A recommendation is not complete without a limitation and a named action to reduce the largest consequential uncertainty.

## 6. Integration with other mechanical disciplines

The design decision in **frequency response and resonance separation** is related to **physics-based modeling and digital engineering**. A useful model states assumptions, state variables, boundary conditions, conservation relations and applicable time scale. A model is not a digital twin merely because it has a dashboard. Its predictive usefulness rests on calibration, identification and comparison with measurements independent of fitting data. Think about what information must pass between those two engineering teams and whether the transfer occurs as a load case, geometric tolerance, material property, signal, cost scenario or acceptance test. An interface that lacks an owner may survive several design reviews without being checked. In a final integration meeting, require each assumption to have an identified source and a planned verification activity; record deviations explicitly.

**Engineering notebook output:** One independent arithmetic check, one alternative architecture, one requirement-to-evidence row, one uncertainty statement, and one open risk item to carry into the unit capstone.


---

# U05-L04 — Feedback, sampling and actuator saturation

**Unit 5: Dynamics, Control and Mechatronic Integration**  
**Purpose.** Evaluate one real design decision in the context of an integrated mechanical system. Students should be able to explain the physics, run a bounded calculation, test its assumptions and prepare a defensible design record.

## 1. Physical meaning and engineering relevance

A digital loop is affected by sample time, delay, sensor noise, quantization and actuator limits. A stable continuous controller may become unstable after discretization or saturation. Analyze the closed-loop system over real operating conditions.

A good engineering claim starts from the exact outcome being sought and a stated operational setting. In this lesson, explain what happens during commissioning, steady operation, abnormal operation and normal service. A variable that looks constant in a laboratory exercise may change dramatically when equipment ages or moves between sites. A drawing alone cannot show every thermal, mechanical and control dependency; record interfaces and operating sequences as well. Treat the word **system** as a boundary containing components, people, controls and environmental interactions, not simply a list of purchased items.

The governing decision is linked to the unit's wider question: Moving mechanisms must satisfy kinematics, force and torque limits, transient control behavior and safety response. Sensor filtering introduces phase delay; actuator limits break linear assumptions. The selected mechanical transmission affects control bandwidth, heat and serviceability, so integration must be concurrent. To make the relation operational, write every variable with units, the domain over which it is expected to be useful and the physical mechanism that might violate it. When using a supplied coefficient, say whether it came from a material test, a catalog, a standard, or a hypothetical classroom choice. Do not silently combine catalog ratings at different temperatures or duty cycles. If a concept depends on an uncertain input, use its plausible interval rather than only a best-looking estimate.

## 2. Governing relation and useful calculation

**Core relation or design rule:** `u = Kp e + Ki∫e dt + Kd de/dt`

**Worked case.** A position actuator commanded beyond a mechanical stop accumulates integral error unless the controller limits or unwinds it. After the command is released, the stored action can cause overshoot.

The first check is dimensional: if the symbols represent different physical dimensions, convert to a common SI basis before evaluating. The second check is one limiting case: set a load to zero, make the design very stiff, or let an efficiency approach unity—whichever is physically relevant—and ask if the predicted direction makes sense. The third check is to estimate the size of an ignored term. A compact hand calculation is valuable because it can expose a reversed ratio or a misplaced conversion factor that would otherwise pass through a spreadsheet unnoticed.

Convert the worked case into a design memo: state the known inputs, unknown output, assumptions, calculation, units and consequence of crossing the limit. Make two alternative estimates, one at a favorable operating point and one at a credible adverse point. Explain why the apparent improvement may not translate into a better total system. The correct comparison uses the same function, service life and boundary for each alternative rather than comparing one design at peak efficiency with another at average duty.

## 3. Scope, counterexample and failure conditions

Tuning on an unloaded demonstration does not verify behavior with a heavier payload, temperature drift or emergency-stop transition.

A calculation is only as good as its assumed configuration. Ask whether the actual mechanism is linear, whether geometry remains unchanged, whether a temperature-dependent property was treated as fixed, and whether contact, vibration or actuator saturation could introduce a discontinuity. If the model ignores an effect because it appears small, report the evidence supporting that decision. Quantification is not a substitute for identifying hazards: an attractive weighted objective cannot excuse an unverified guard, protection feature, pressure boundary or emergency stop.

A counterexample helps establish the scope. Imagine the original design moved from a controlled teaching bench to a dirty or wet industrial location. The incoming load spectrum, corrosion exposure, calibration frequency and repair resources may be different. Name at least one parameter from the equation that remains meaningful and one omitted mechanism that becomes important. Explain how the design review would change if that mechanism is plausible. Record any consequence whose acceptability must be judged by a competent safety professional rather than inferred from a classroom equation.

## 4. Practical investigation — What is the evidence?

Maintain raw measurements, instrument calibration data, model input files and revision identifiers. An output graph without provenance cannot be independently reconstructed and should not serve as an engineering acceptance record.

**Studio assignment.** Write a control-state machine for an indexing stage with startup, homing, run, fault and safe shutdown.

**Required confirmation.** Step responses at load corners, limit-switch tests, measured delay and safe-state proof.

Build a reproducible notebook for this assignment. Include a sketch or diagram, table of known quantities with units, a physical basis for each relationship, and a separate list of facts that are merely assumed. Perform the calculation with independent arithmetic. If testing is proposed, explain where the sensors go and how their calibration and resolution affect the result. State what data would falsify the current design hypothesis; do not propose only measurements that could support it. Keep original data rather than overwriting it when outliers or transcription errors are discovered.

For this particular case, apply the following broader check: Form a trace from need through required function and quantified threshold to an instrumented acceptance result. Avoid a requirement stating only the preferred component; that describes a proposed solution rather than an outcome. This guards against optimizing one metric while overlooking a coupled physical constraint. Report a design alternative in which the selected performance improves while some other important objective worsens. That alternative may still be appropriate, but the trade must be transparent and tied to stakeholder priorities. Before deciding, check whether the new configuration requires another supplier capability study, additional inspection or a revised safety analysis.

## 5. Exercises: calculation, design and criticism

1. **Definitions:** Explain **feedback, sampling and actuator saturation** to a technician who knows the equipment but has not studied the model. State the measurable event, required operating condition and one assumption that cannot be read directly from the output.
2. **Hand calculation:** Reproduce the worked case and its governing rule `u = Kp e + Ki∫e dt + Kd de/dt` with all units and significant figures justified. Change one input by +10% and determine whether the direction of change is physically plausible.
3. **Boundary case:** Analyze the specific limitation: Tuning on an unloaded demonstration does not verify behavior with a heavier payload, temperature drift or emergency-stop transition. Explain which additional calculation, test or design constraint is required and why a single generic safety factor cannot solve the missing-physics problem.
4. **Alternative:** Write a control-state machine for an indexing stage with startup, homing, run, fault and safe shutdown. Propose a second feasible mechanism or component, not merely a different numerical setting of the original choice. Evaluate manufacturing and maintenance implications.
5. **Evidence:** Step responses at load corners, limit-switch tests, measured delay and safe-state proof. Prepare a small table of what would be measured, which instrument would be used, what uncertainty could dominate and whether the result would verify a requirement or validate intended use.

**Instructor checkpoint A.** An answer that repeats the formula without identifying the operational boundary is incomplete. The student's result must have consistent units and a clear physical sign. If the output is expressed as a ratio or probability, explain its numerical range and whether independence assumptions apply. If an optimization is involved, a design that violates a hard constraint is rejected even if its objective is lower.

**Instructor checkpoint B.** Students should distinguish a calculated output from physical evidence. Strong submissions show an independent check, a sensitivity comparison, a plausible counterexample and an actionable test plan. A poor submission uses extra decimal places, repeated simulations, or an appealing chart to imply accuracy that the inputs do not support. A recommendation is not complete without a limitation and a named action to reduce the largest consequential uncertainty.

## 6. Integration with other mechanical disciplines

The design decision in **feedback, sampling and actuator saturation** is related to **optimization methods and design tradeoffs**. Design optimization asks which feasible decision vector gives the best defensible outcome. Feasibility conditions are not preferences. Multiobjective design typically produces a Pareto set rather than one uniquely correct answer, and ranking alternatives requires transparent priorities and sensitivity to uncertain weights. Think about what information must pass between those two engineering teams and whether the transfer occurs as a load case, geometric tolerance, material property, signal, cost scenario or acceptance test. An interface that lacks an owner may survive several design reviews without being checked. In a final integration meeting, require each assumption to have an identified source and a planned verification activity; record deviations explicitly.

**Engineering notebook output:** One independent arithmetic check, one alternative architecture, one requirement-to-evidence row, one uncertainty statement, and one open risk item to carry into the unit capstone.


---

# U05-L05 — System integration and safety control

**Unit 5: Dynamics, Control and Mechatronic Integration**  
**Purpose.** Evaluate one real design decision in the context of an integrated mechanical system. Students should be able to explain the physics, run a bounded calculation, test its assumptions and prepare a defensible design record.

## 1. Physical meaning and engineering relevance

Integration tests must exercise failure and degraded states, not only nominal automatic operation. Mechanical guarding, electrical isolation and software interlocks have different reliability characteristics and should not be treated as interchangeable.

A good engineering claim starts from the exact outcome being sought and a stated operational setting. In this lesson, explain what happens during commissioning, steady operation, abnormal operation and normal service. A variable that looks constant in a laboratory exercise may change dramatically when equipment ages or moves between sites. A drawing alone cannot show every thermal, mechanical and control dependency; record interfaces and operating sequences as well. Treat the word **system** as a boundary containing components, people, controls and environmental interactions, not simply a list of purchased items.

The governing decision is linked to the unit's wider question: Moving mechanisms must satisfy kinematics, force and torque limits, transient control behavior and safety response. Sensor filtering introduces phase delay; actuator limits break linear assumptions. The selected mechanical transmission affects control bandwidth, heat and serviceability, so integration must be concurrent. To make the relation operational, write every variable with units, the domain over which it is expected to be useful and the physical mechanism that might violate it. When using a supplied coefficient, say whether it came from a material test, a catalog, a standard, or a hypothetical classroom choice. Do not silently combine catalog ratings at different temperatures or duty cycles. If a concept depends on an uncertain input, use its plausible interval rather than only a best-looking estimate.

## 2. Governing relation and useful calculation

**Core relation or design rule:** `Risk reduction = independent barriers + evidence`

**Worked case.** Suppose an automatic table achieves 10,000 cycles without a motion error but its guard interlock was never tested. The functional performance data do not establish safety integrity.

The first check is dimensional: if the symbols represent different physical dimensions, convert to a common SI basis before evaluating. The second check is one limiting case: set a load to zero, make the design very stiff, or let an efficiency approach unity—whichever is physically relevant—and ask if the predicted direction makes sense. The third check is to estimate the size of an ignored term. A compact hand calculation is valuable because it can expose a reversed ratio or a misplaced conversion factor that would otherwise pass through a spreadsheet unnoticed.

Convert the worked case into a design memo: state the known inputs, unknown output, assumptions, calculation, units and consequence of crossing the limit. Make two alternative estimates, one at a favorable operating point and one at a credible adverse point. Explain why the apparent improvement may not translate into a better total system. The correct comparison uses the same function, service life and boundary for each alternative rather than comparing one design at peak efficiency with another at average duty.

## 3. Scope, counterexample and failure conditions

A software warning is not a substitute for required physical barriers. Safety architecture and applicable standards require a qualified assessment outside this educational exercise.

A calculation is only as good as its assumed configuration. Ask whether the actual mechanism is linear, whether geometry remains unchanged, whether a temperature-dependent property was treated as fixed, and whether contact, vibration or actuator saturation could introduce a discontinuity. If the model ignores an effect because it appears small, report the evidence supporting that decision. Quantification is not a substitute for identifying hazards: an attractive weighted objective cannot excuse an unverified guard, protection feature, pressure boundary or emergency stop.

A counterexample helps establish the scope. Imagine the original design moved from a controlled teaching bench to a dirty or wet industrial location. The incoming load spectrum, corrosion exposure, calibration frequency and repair resources may be different. Name at least one parameter from the equation that remains meaningful and one omitted mechanism that becomes important. Explain how the design review would change if that mechanism is plausible. Record any consequence whose acceptability must be judged by a competent safety professional rather than inferred from a classroom equation.

## 4. Practical investigation — What could reverse the decision?

Identify the single uncertain parameter most likely to change the preferred alternative. Design a low-risk test that would measure it and record what evidence would justify changing the recommendation.

**Studio assignment.** List five single-fault scenarios, define required safe responses and propose a documented functional test plan that does not deliberately create hazards.

**Required confirmation.** Approved safety requirements, test logs, version-controlled fault response and competent-person signoff.

Build a reproducible notebook for this assignment. Include a sketch or diagram, table of known quantities with units, a physical basis for each relationship, and a separate list of facts that are merely assumed. Perform the calculation with independent arithmetic. If testing is proposed, explain where the sensors go and how their calibration and resolution affect the result. State what data would falsify the current design hypothesis; do not propose only measurements that could support it. Keep original data rather than overwriting it when outliers or transcription errors are discovered.

For this particular case, apply the following broader check: Start with the system boundary and distinguish conservation equations from fitted correlations. Identify what inputs are measured, taken from vendor data or chosen for teaching. Do not claim that a model represents the plant until a separate measurement comparison has been made. This guards against optimizing one metric while overlooking a coupled physical constraint. Report a design alternative in which the selected performance improves while some other important objective worsens. That alternative may still be appropriate, but the trade must be transparent and tied to stakeholder priorities. Before deciding, check whether the new configuration requires another supplier capability study, additional inspection or a revised safety analysis.

## 5. Exercises: calculation, design and criticism

1. **Definitions:** Explain **system integration and safety control** to a technician who knows the equipment but has not studied the model. State the measurable event, required operating condition and one assumption that cannot be read directly from the output.
2. **Hand calculation:** Reproduce the worked case and its governing rule `Risk reduction = independent barriers + evidence` with all units and significant figures justified. Change one input by +10% and determine whether the direction of change is physically plausible.
3. **Boundary case:** Analyze the specific limitation: A software warning is not a substitute for required physical barriers. Safety architecture and applicable standards require a qualified assessment outside this educational exercise. Explain which additional calculation, test or design constraint is required and why a single generic safety factor cannot solve the missing-physics problem.
4. **Alternative:** List five single-fault scenarios, define required safe responses and propose a documented functional test plan that does not deliberately create hazards. Propose a second feasible mechanism or component, not merely a different numerical setting of the original choice. Evaluate manufacturing and maintenance implications.
5. **Evidence:** Approved safety requirements, test logs, version-controlled fault response and competent-person signoff. Prepare a small table of what would be measured, which instrument would be used, what uncertainty could dominate and whether the result would verify a requirement or validate intended use.

**Instructor checkpoint A.** An answer that repeats the formula without identifying the operational boundary is incomplete. The student's result must have consistent units and a clear physical sign. If the output is expressed as a ratio or probability, explain its numerical range and whether independence assumptions apply. If an optimization is involved, a design that violates a hard constraint is rejected even if its objective is lower.

**Instructor checkpoint B.** Students should distinguish a calculated output from physical evidence. Strong submissions show an independent check, a sensitivity comparison, a plausible counterexample and an actionable test plan. A poor submission uses extra decimal places, repeated simulations, or an appealing chart to imply accuracy that the inputs do not support. A recommendation is not complete without a limitation and a named action to reduce the largest consequential uncertainty.

## 6. Integration with other mechanical disciplines

The design decision in **system integration and safety control** is related to **structural, thermal and fluid co-design**. Mechanical design is coupled: increasing stiffness can raise mass; reducing friction changes heat generation; additional insulation changes expansion and packaging. Sequential discipline-by-discipline optimization often shifts a problem to another subsystem. Co-design evaluates physical interfaces and operating envelopes. Think about what information must pass between those two engineering teams and whether the transfer occurs as a load case, geometric tolerance, material property, signal, cost scenario or acceptance test. An interface that lacks an owner may survive several design reviews without being checked. In a final integration meeting, require each assumption to have an identified source and a planned verification activity; record deviations explicitly.

**Engineering notebook output:** One independent arithmetic check, one alternative architecture, one requirement-to-evidence row, one uncertainty statement, and one open risk item to carry into the unit capstone.


---

