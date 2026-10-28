# Unit 08: Integrated Capstone and Engineering Decision-Making

**Course Code**: MSO 408 · **Level**: Advanced Undergraduate Engineering

## Unit Overview & Physical Foundations

This comprehensive university textbook unit covers the theoretical framework, physical modeling, mathematical governing equations, and engineering applications of **Integrated Capstone and Engineering Decision-Making**.

# U08-L01 — Capstone problem definition and system boundary

**Unit 8: Integrated Capstone and Engineering Decision-Making**  
**Purpose.** Evaluate one real design decision in the context of an integrated mechanical system. Students should be able to explain the physics, run a bounded calculation, test its assumptions and prepare a defensible design record.

## 1. Physical meaning and engineering relevance

A capstone must frame a solvable problem with a defined customer, site, mission, hazards and resource ceiling. Design claims need a consistent functional boundary so energy accounting, reliability and economics are not manipulated by exclusions.

A good engineering claim starts from the exact outcome being sought and a stated operational setting. In this lesson, explain what happens during commissioning, steady operation, abnormal operation and normal service. A variable that looks constant in a laboratory exercise may change dramatically when equipment ages or moves between sites. A drawing alone cannot show every thermal, mechanical and control dependency; record interfaces and operating sequences as well. Treat the word **system** as a boundary containing components, people, controls and environmental interactions, not simply a list of purchased items.

The governing decision is linked to the unit's wider question: System design culminates in traceable evidence and an honest decision under constraints. A useful engineering dossier ties stakeholder needs to functional architecture, engineering analysis, cost, verification, failure controls, manufacturing and eventual disposition. Unresolved risk is an outcome to report, not a number to conceal. To make the relation operational, write every variable with units, the domain over which it is expected to be useful and the physical mechanism that might violate it. When using a supplied coefficient, say whether it came from a material test, a catalog, a standard, or a hypothetical classroom choice. Do not silently combine catalog ratings at different temperatures or duty cycles. If a concept depends on an uncertain input, use its plausible interval rather than only a best-looking estimate.

## 2. Governing relation and useful calculation

**Core relation or design rule:** `Net useful output = gross output − parasitic consumption`

**Worked case.** An energy-recovery demonstrator generating 100 W while consuming 150 W in the pump is not producing net electricity, even if its generator shows a useful voltage. The learning value may be real; the energy claim is false.

The first check is dimensional: if the symbols represent different physical dimensions, convert to a common SI basis before evaluating. The second check is one limiting case: set a load to zero, make the design very stiff, or let an efficiency approach unity—whichever is physically relevant—and ask if the predicted direction makes sense. The third check is to estimate the size of an ignored term. A compact hand calculation is valuable because it can expose a reversed ratio or a misplaced conversion factor that would otherwise pass through a spreadsheet unnoticed.

Convert the worked case into a design memo: state the known inputs, unknown output, assumptions, calculation, units and consequence of crossing the limit. Make two alternative estimates, one at a favorable operating point and one at a credible adverse point. Explain why the apparent improvement may not translate into a better total system. The correct comparison uses the same function, service life and boundary for each alternative rather than comparing one design at peak efficiency with another at average duty.

## 3. Scope, counterexample and failure conditions

Ignoring inverter losses, startup transients or external energy inputs can create apparent perpetual-motion performance. Conservation must remain non-negotiable.

A calculation is only as good as its assumed configuration. Ask whether the actual mechanism is linear, whether geometry remains unchanged, whether a temperature-dependent property was treated as fixed, and whether contact, vibration or actuator saturation could introduce a discontinuity. If the model ignores an effect because it appears small, report the evidence supporting that decision. Quantification is not a substitute for identifying hazards: an attractive weighted objective cannot excuse an unverified guard, protection feature, pressure boundary or emergency stop.

A counterexample helps establish the scope. Imagine the original design moved from a controlled teaching bench to a dirty or wet industrial location. The incoming load spectrum, corrosion exposure, calibration frequency and repair resources may be different. Name at least one parameter from the equation that remains meaningful and one omitted mechanism that becomes important. Explain how the design review would change if that mechanism is plausible. Record any consequence whose acceptability must be judged by a competent safety professional rather than inferred from a classroom equation.

## 4. Practical investigation — What is controlled?

State the decision variable, its allowed range, and which physical observations it can change. A variable that cannot be adjusted by the engineer is a disturbance or measured parameter; confusing the two makes the optimization unrealistic.

**Studio assignment.** Write a one-page problem charter listing measurable outcomes, no-go conditions and required review authorities.

**Required confirmation.** Boundary diagram, energy input metering and approved capstone scope.

Build a reproducible notebook for this assignment. Include a sketch or diagram, table of known quantities with units, a physical basis for each relationship, and a separate list of facts that are merely assumed. Perform the calculation with independent arithmetic. If testing is proposed, explain where the sensors go and how their calibration and resolution affect the result. State what data would falsify the current design hypothesis; do not propose only measurements that could support it. Keep original data rather than overwriting it when outliers or transcription errors are discovered.

For this particular case, apply the following broader check: Form a trace from need through required function and quantified threshold to an instrumented acceptance result. Avoid a requirement stating only the preferred component; that describes a proposed solution rather than an outcome. This guards against optimizing one metric while overlooking a coupled physical constraint. Report a design alternative in which the selected performance improves while some other important objective worsens. That alternative may still be appropriate, but the trade must be transparent and tied to stakeholder priorities. Before deciding, check whether the new configuration requires another supplier capability study, additional inspection or a revised safety analysis.

## 5. Exercises: calculation, design and criticism

1. **Definitions:** Explain **capstone problem definition and system boundary** to a technician who knows the equipment but has not studied the model. State the measurable event, required operating condition and one assumption that cannot be read directly from the output.
2. **Hand calculation:** Reproduce the worked case and its governing rule `Net useful output = gross output − parasitic consumption` with all units and significant figures justified. Change one input by +10% and determine whether the direction of change is physically plausible.
3. **Boundary case:** Analyze the specific limitation: Ignoring inverter losses, startup transients or external energy inputs can create apparent perpetual-motion performance. Conservation must remain non-negotiable. Explain which additional calculation, test or design constraint is required and why a single generic safety factor cannot solve the missing-physics problem.
4. **Alternative:** Write a one-page problem charter listing measurable outcomes, no-go conditions and required review authorities. Propose a second feasible mechanism or component, not merely a different numerical setting of the original choice. Evaluate manufacturing and maintenance implications.
5. **Evidence:** Boundary diagram, energy input metering and approved capstone scope. Prepare a small table of what would be measured, which instrument would be used, what uncertainty could dominate and whether the result would verify a requirement or validate intended use.

**Instructor checkpoint A.** An answer that repeats the formula without identifying the operational boundary is incomplete. The student's result must have consistent units and a clear physical sign. If the output is expressed as a ratio or probability, explain its numerical range and whether independence assumptions apply. If an optimization is involved, a design that violates a hard constraint is rejected even if its objective is lower.

**Instructor checkpoint B.** Students should distinguish a calculated output from physical evidence. Strong submissions show an independent check, a sensitivity comparison, a plausible counterexample and an actionable test plan. A poor submission uses extra decimal places, repeated simulations, or an appealing chart to imply accuracy that the inputs do not support. A recommendation is not complete without a limitation and a named action to reduce the largest consequential uncertainty.

## 6. Integration with other mechanical disciplines

The design decision in **capstone problem definition and system boundary** is related to **optimization methods and design tradeoffs**. Design optimization asks which feasible decision vector gives the best defensible outcome. Feasibility conditions are not preferences. Multiobjective design typically produces a Pareto set rather than one uniquely correct answer, and ranking alternatives requires transparent priorities and sensitivity to uncertain weights. Think about what information must pass between those two engineering teams and whether the transfer occurs as a load case, geometric tolerance, material property, signal, cost scenario or acceptance test. An interface that lacks an owner may survive several design reviews without being checked. In a final integration meeting, require each assumption to have an identified source and a planned verification activity; record deviations explicitly.

**Engineering notebook output:** One independent arithmetic check, one alternative architecture, one requirement-to-evidence row, one uncertainty statement, and one open risk item to carry into the unit capstone.


---

# U08-L02 — Architecture trade study and baseline selection

**Unit 8: Integrated Capstone and Engineering Decision-Making**  
**Purpose.** Evaluate one real design decision in the context of an integrated mechanical system. Students should be able to explain the physics, run a bounded calculation, test its assumptions and prepare a defensible design record.

## 1. Physical meaning and engineering relevance

A capstone architecture must compare at least two credible concepts on the same test mission. Interfaces, component sourcing, maintenance and expected data quality can outweigh a small predicted efficiency gain.

A good engineering claim starts from the exact outcome being sought and a stated operational setting. In this lesson, explain what happens during commissioning, steady operation, abnormal operation and normal service. A variable that looks constant in a laboratory exercise may change dramatically when equipment ages or moves between sites. A drawing alone cannot show every thermal, mechanical and control dependency; record interfaces and operating sequences as well. Treat the word **system** as a boundary containing components, people, controls and environmental interactions, not simply a list of purchased items.

The governing decision is linked to the unit's wider question: System design culminates in traceable evidence and an honest decision under constraints. A useful engineering dossier ties stakeholder needs to functional architecture, engineering analysis, cost, verification, failure controls, manufacturing and eventual disposition. Unresolved risk is an outcome to report, not a number to conceal. To make the relation operational, write every variable with units, the domain over which it is expected to be useful and the physical mechanism that might violate it. When using a supplied coefficient, say whether it came from a material test, a catalog, a standard, or a hypothetical classroom choice. Do not silently combine catalog ratings at different temperatures or duty cycles. If a concept depends on an uncertain input, use its plausible interval rather than only a best-looking estimate.

## 2. Governing relation and useful calculation

**Core relation or design rule:** `Score is secondary to hard-constraint feasibility`

**Worked case.** Compare direct coupling, belt drive and geared coupling for a generator demonstrator. Consider rotational speed envelope, slip, guarding, bearing load and instruments needed to measure losses.

The first check is dimensional: if the symbols represent different physical dimensions, convert to a common SI basis before evaluating. The second check is one limiting case: set a load to zero, make the design very stiff, or let an efficiency approach unity—whichever is physically relevant—and ask if the predicted direction makes sense. The third check is to estimate the size of an ignored term. A compact hand calculation is valuable because it can expose a reversed ratio or a misplaced conversion factor that would otherwise pass through a spreadsheet unnoticed.

Convert the worked case into a design memo: state the known inputs, unknown output, assumptions, calculation, units and consequence of crossing the limit. Make two alternative estimates, one at a favorable operating point and one at a credible adverse point. Explain why the apparent improvement may not translate into a better total system. The correct comparison uses the same function, service life and boundary for each alternative rather than comparing one design at peak efficiency with another at average duty.

## 3. Scope, counterexample and failure conditions

A weighted score disguises uncertainty if all input numbers are fabricated. Present ranges and explain which test will separate close alternatives.

A calculation is only as good as its assumed configuration. Ask whether the actual mechanism is linear, whether geometry remains unchanged, whether a temperature-dependent property was treated as fixed, and whether contact, vibration or actuator saturation could introduce a discontinuity. If the model ignores an effect because it appears small, report the evidence supporting that decision. Quantification is not a substitute for identifying hazards: an attractive weighted objective cannot excuse an unverified guard, protection feature, pressure boundary or emergency stop.

A counterexample helps establish the scope. Imagine the original design moved from a controlled teaching bench to a dirty or wet industrial location. The incoming load spectrum, corrosion exposure, calibration frequency and repair resources may be different. Name at least one parameter from the equation that remains meaningful and one omitted mechanism that becomes important. Explain how the design review would change if that mechanism is plausible. Record any consequence whose acceptability must be judged by a competent safety professional rather than inferred from a classroom equation.

## 4. Practical investigation — What is conserved?

Start by tracing mass, force, energy or information through the studied boundary. Write down any neglected source, loss or interface. When a numerical output appears to violate a conservation statement, inspect boundary definitions before changing the data.

**Studio assignment.** Create a supplier-aware concept comparison with a documented rejection rationale and verification action for the selected design.

**Required confirmation.** Alternatives report with dated quotes, interface assumptions and traceable review comments.

Build a reproducible notebook for this assignment. Include a sketch or diagram, table of known quantities with units, a physical basis for each relationship, and a separate list of facts that are merely assumed. Perform the calculation with independent arithmetic. If testing is proposed, explain where the sensors go and how their calibration and resolution affect the result. State what data would falsify the current design hypothesis; do not propose only measurements that could support it. Keep original data rather than overwriting it when outliers or transcription errors are discovered.

For this particular case, apply the following broader check: Start with the system boundary and distinguish conservation equations from fitted correlations. Identify what inputs are measured, taken from vendor data or chosen for teaching. Do not claim that a model represents the plant until a separate measurement comparison has been made. This guards against optimizing one metric while overlooking a coupled physical constraint. Report a design alternative in which the selected performance improves while some other important objective worsens. That alternative may still be appropriate, but the trade must be transparent and tied to stakeholder priorities. Before deciding, check whether the new configuration requires another supplier capability study, additional inspection or a revised safety analysis.

## 5. Exercises: calculation, design and criticism

1. **Definitions:** Explain **architecture trade study and baseline selection** to a technician who knows the equipment but has not studied the model. State the measurable event, required operating condition and one assumption that cannot be read directly from the output.
2. **Hand calculation:** Reproduce the worked case and its governing rule `Score is secondary to hard-constraint feasibility` with all units and significant figures justified. Change one input by +10% and determine whether the direction of change is physically plausible.
3. **Boundary case:** Analyze the specific limitation: A weighted score disguises uncertainty if all input numbers are fabricated. Present ranges and explain which test will separate close alternatives. Explain which additional calculation, test or design constraint is required and why a single generic safety factor cannot solve the missing-physics problem.
4. **Alternative:** Create a supplier-aware concept comparison with a documented rejection rationale and verification action for the selected design. Propose a second feasible mechanism or component, not merely a different numerical setting of the original choice. Evaluate manufacturing and maintenance implications.
5. **Evidence:** Alternatives report with dated quotes, interface assumptions and traceable review comments. Prepare a small table of what would be measured, which instrument would be used, what uncertainty could dominate and whether the result would verify a requirement or validate intended use.

**Instructor checkpoint A.** An answer that repeats the formula without identifying the operational boundary is incomplete. The student's result must have consistent units and a clear physical sign. If the output is expressed as a ratio or probability, explain its numerical range and whether independence assumptions apply. If an optimization is involved, a design that violates a hard constraint is rejected even if its objective is lower.

**Instructor checkpoint B.** Students should distinguish a calculated output from physical evidence. Strong submissions show an independent check, a sensitivity comparison, a plausible counterexample and an actionable test plan. A poor submission uses extra decimal places, repeated simulations, or an appealing chart to imply accuracy that the inputs do not support. A recommendation is not complete without a limitation and a named action to reduce the largest consequential uncertainty.

## 6. Integration with other mechanical disciplines

The design decision in **architecture trade study and baseline selection** is related to **structural, thermal and fluid co-design**. Mechanical design is coupled: increasing stiffness can raise mass; reducing friction changes heat generation; additional insulation changes expansion and packaging. Sequential discipline-by-discipline optimization often shifts a problem to another subsystem. Co-design evaluates physical interfaces and operating envelopes. Think about what information must pass between those two engineering teams and whether the transfer occurs as a load case, geometric tolerance, material property, signal, cost scenario or acceptance test. An interface that lacks an owner may survive several design reviews without being checked. In a final integration meeting, require each assumption to have an identified source and a planned verification activity; record deviations explicitly.

**Engineering notebook output:** One independent arithmetic check, one alternative architecture, one requirement-to-evidence row, one uncertainty statement, and one open risk item to carry into the unit capstone.


---

# U08-L03 — Integrated simulation and budget reconciliation

**Unit 8: Integrated Capstone and Engineering Decision-Making**  
**Purpose.** Evaluate one real design decision in the context of an integrated mechanical system. Students should be able to explain the physics, run a bounded calculation, test its assumptions and prepare a defensible design record.

## 1. Physical meaning and engineering relevance

Close mechanical, thermal, fluid and electrical budgets over a common time base. Use independent first-principles estimates before coupling detailed models; agreement between two implementations of the same flawed assumption does not validate physics.

A good engineering claim starts from the exact outcome being sought and a stated operational setting. In this lesson, explain what happens during commissioning, steady operation, abnormal operation and normal service. A variable that looks constant in a laboratory exercise may change dramatically when equipment ages or moves between sites. A drawing alone cannot show every thermal, mechanical and control dependency; record interfaces and operating sequences as well. Treat the word **system** as a boundary containing components, people, controls and environmental interactions, not simply a list of purchased items.

The governing decision is linked to the unit's wider question: System design culminates in traceable evidence and an honest decision under constraints. A useful engineering dossier ties stakeholder needs to functional architecture, engineering analysis, cost, verification, failure controls, manufacturing and eventual disposition. Unresolved risk is an outcome to report, not a number to conceal. To make the relation operational, write every variable with units, the domain over which it is expected to be useful and the physical mechanism that might violate it. When using a supplied coefficient, say whether it came from a material test, a catalog, a standard, or a hypothetical classroom choice. Do not silently combine catalog ratings at different temperatures or duty cycles. If a concept depends on an uncertain input, use its plausible interval rather than only a best-looking estimate.

## 2. Governing relation and useful calculation

**Core relation or design rule:** `P_electrical = η_generator η_mechanical P_shaft`

**Worked case.** A generator expected to receive 300 W shaft input at 90% efficiency would yield about 270 W electrical under that condition, before downstream conversion. If the driving pump uses 500 W, net import remains positive.

The first check is dimensional: if the symbols represent different physical dimensions, convert to a common SI basis before evaluating. The second check is one limiting case: set a load to zero, make the design very stiff, or let an efficiency approach unity—whichever is physically relevant—and ask if the predicted direction makes sense. The third check is to estimate the size of an ignored term. A compact hand calculation is valuable because it can expose a reversed ratio or a misplaced conversion factor that would otherwise pass through a spreadsheet unnoticed.

Convert the worked case into a design memo: state the known inputs, unknown output, assumptions, calculation, units and consequence of crossing the limit. Make two alternative estimates, one at a favorable operating point and one at a credible adverse point. Explain why the apparent improvement may not translate into a better total system. The correct comparison uses the same function, service life and boundary for each alternative rather than comparing one design at peak efficiency with another at average duty.

## 3. Scope, counterexample and failure conditions

Summing peak loads that never coincide may oversize equipment; ignoring startup peaks may undersize protection. A steady balance cannot reveal dynamic stability.

A calculation is only as good as its assumed configuration. Ask whether the actual mechanism is linear, whether geometry remains unchanged, whether a temperature-dependent property was treated as fixed, and whether contact, vibration or actuator saturation could introduce a discontinuity. If the model ignores an effect because it appears small, report the evidence supporting that decision. Quantification is not a substitute for identifying hazards: an attractive weighted objective cannot excuse an unverified guard, protection feature, pressure boundary or emergency stop.

A counterexample helps establish the scope. Imagine the original design moved from a controlled teaching bench to a dirty or wet industrial location. The incoming load spectrum, corrosion exposure, calibration frequency and repair resources may be different. Name at least one parameter from the equation that remains meaningful and one omitted mechanism that becomes important. Explain how the design review would change if that mechanism is plausible. Record any consequence whose acceptability must be judged by a competent safety professional rather than inferred from a classroom equation.

## 4. Practical investigation — Where are the limits?

Report physical operating limits, catalog limits and mandated safeguards separately. A design which fails an essential condition is not acceptable just because its average objective value is attractive.

**Studio assignment.** Construct an energy ledger for startup and steady operation, with uncertainty ranges and sensor locations.

**Required confirmation.** Independent meter readings, parameter sweep and auditable model comparison.

Build a reproducible notebook for this assignment. Include a sketch or diagram, table of known quantities with units, a physical basis for each relationship, and a separate list of facts that are merely assumed. Perform the calculation with independent arithmetic. If testing is proposed, explain where the sensors go and how their calibration and resolution affect the result. State what data would falsify the current design hypothesis; do not propose only measurements that could support it. Keep original data rather than overwriting it when outliers or transcription errors are discovered.

For this particular case, apply the following broader check: Write explicit hard constraints and evaluate them before comparing objective values. Use a common functional unit across alternatives. When uncertainty is large, quantify how a small adjustment in an estimated input alters the selected option. This guards against optimizing one metric while overlooking a coupled physical constraint. Report a design alternative in which the selected performance improves while some other important objective worsens. That alternative may still be appropriate, but the trade must be transparent and tied to stakeholder priorities. Before deciding, check whether the new configuration requires another supplier capability study, additional inspection or a revised safety analysis.

## 5. Exercises: calculation, design and criticism

1. **Definitions:** Explain **integrated simulation and budget reconciliation** to a technician who knows the equipment but has not studied the model. State the measurable event, required operating condition and one assumption that cannot be read directly from the output.
2. **Hand calculation:** Reproduce the worked case and its governing rule `P_electrical = η_generator η_mechanical P_shaft` with all units and significant figures justified. Change one input by +10% and determine whether the direction of change is physically plausible.
3. **Boundary case:** Analyze the specific limitation: Summing peak loads that never coincide may oversize equipment; ignoring startup peaks may undersize protection. A steady balance cannot reveal dynamic stability. Explain which additional calculation, test or design constraint is required and why a single generic safety factor cannot solve the missing-physics problem.
4. **Alternative:** Construct an energy ledger for startup and steady operation, with uncertainty ranges and sensor locations. Propose a second feasible mechanism or component, not merely a different numerical setting of the original choice. Evaluate manufacturing and maintenance implications.
5. **Evidence:** Independent meter readings, parameter sweep and auditable model comparison. Prepare a small table of what would be measured, which instrument would be used, what uncertainty could dominate and whether the result would verify a requirement or validate intended use.

**Instructor checkpoint A.** An answer that repeats the formula without identifying the operational boundary is incomplete. The student's result must have consistent units and a clear physical sign. If the output is expressed as a ratio or probability, explain its numerical range and whether independence assumptions apply. If an optimization is involved, a design that violates a hard constraint is rejected even if its objective is lower.

**Instructor checkpoint B.** Students should distinguish a calculated output from physical evidence. Strong submissions show an independent check, a sensitivity comparison, a plausible counterexample and an actionable test plan. A poor submission uses extra decimal places, repeated simulations, or an appealing chart to imply accuracy that the inputs do not support. A recommendation is not complete without a limitation and a named action to reduce the largest consequential uncertainty.

## 6. Integration with other mechanical disciplines

The design decision in **integrated simulation and budget reconciliation** is related to **dynamics, control and mechatronic integration**. Moving mechanisms must satisfy kinematics, force and torque limits, transient control behavior and safety response. Sensor filtering introduces phase delay; actuator limits break linear assumptions. The selected mechanical transmission affects control bandwidth, heat and serviceability, so integration must be concurrent. Think about what information must pass between those two engineering teams and whether the transfer occurs as a load case, geometric tolerance, material property, signal, cost scenario or acceptance test. An interface that lacks an owner may survive several design reviews without being checked. In a final integration meeting, require each assumption to have an identified source and a planned verification activity; record deviations explicitly.

**Engineering notebook output:** One independent arithmetic check, one alternative architecture, one requirement-to-evidence row, one uncertainty statement, and one open risk item to carry into the unit capstone.


---

# U08-L04 — Failure review and safe test execution

**Unit 8: Integrated Capstone and Engineering Decision-Making**  
**Purpose.** Evaluate one real design decision in the context of an integrated mechanical system. Students should be able to explain the physics, run a bounded calculation, test its assumptions and prepare a defensible design record.

## 1. Physical meaning and engineering relevance

Final testing should start with hazard analysis and controlled procedures. Store energy, pinch points, sharp fragments, hot surfaces and electrical faults require engineering safeguards. Do not perform high-energy or unguarded destructive tests in educational contexts.

A good engineering claim starts from the exact outcome being sought and a stated operational setting. In this lesson, explain what happens during commissioning, steady operation, abnormal operation and normal service. A variable that looks constant in a laboratory exercise may change dramatically when equipment ages or moves between sites. A drawing alone cannot show every thermal, mechanical and control dependency; record interfaces and operating sequences as well. Treat the word **system** as a boundary containing components, people, controls and environmental interactions, not simply a list of purchased items.

The governing decision is linked to the unit's wider question: System design culminates in traceable evidence and an honest decision under constraints. A useful engineering dossier ties stakeholder needs to functional architecture, engineering analysis, cost, verification, failure controls, manufacturing and eventual disposition. Unresolved risk is an outcome to report, not a number to conceal. To make the relation operational, write every variable with units, the domain over which it is expected to be useful and the physical mechanism that might violate it. When using a supplied coefficient, say whether it came from a material test, a catalog, a standard, or a hypothetical classroom choice. Do not silently combine catalog ratings at different temperatures or duty cycles. If a concept depends on an uncertain input, use its plausible interval rather than only a best-looking estimate.

## 2. Governing relation and useful calculation

**Core relation or design rule:** `Residual risk depends on credible events and verified barriers`

**Worked case.** A flywheel can store significant rotational energy even after the motor supply is disconnected. Isolation must address coast-down and stored energy, not just the electrical switch state.

The first check is dimensional: if the symbols represent different physical dimensions, convert to a common SI basis before evaluating. The second check is one limiting case: set a load to zero, make the design very stiff, or let an efficiency approach unity—whichever is physically relevant—and ask if the predicted direction makes sense. The third check is to estimate the size of an ignored term. A compact hand calculation is valuable because it can expose a reversed ratio or a misplaced conversion factor that would otherwise pass through a spreadsheet unnoticed.

Convert the worked case into a design memo: state the known inputs, unknown output, assumptions, calculation, units and consequence of crossing the limit. Make two alternative estimates, one at a favorable operating point and one at a credible adverse point. Explain why the apparent improvement may not translate into a better total system. The correct comparison uses the same function, service life and boundary for each alternative rather than comparing one design at peak efficiency with another at average duty.

## 3. Scope, counterexample and failure conditions

A safe operating procedure copied from a different machine may omit project-specific over-speed and containment hazards.

A calculation is only as good as its assumed configuration. Ask whether the actual mechanism is linear, whether geometry remains unchanged, whether a temperature-dependent property was treated as fixed, and whether contact, vibration or actuator saturation could introduce a discontinuity. If the model ignores an effect because it appears small, report the evidence supporting that decision. Quantification is not a substitute for identifying hazards: an attractive weighted objective cannot excuse an unverified guard, protection feature, pressure boundary or emergency stop.

A counterexample helps establish the scope. Imagine the original design moved from a controlled teaching bench to a dirty or wet industrial location. The incoming load spectrum, corrosion exposure, calibration frequency and repair resources may be different. Name at least one parameter from the equation that remains meaningful and one omitted mechanism that becomes important. Explain how the design review would change if that mechanism is plausible. Record any consequence whose acceptability must be judged by a competent safety professional rather than inferred from a classroom equation.

## 4. Practical investigation — What is the evidence?

Maintain raw measurements, instrument calibration data, model input files and revision identifiers. An output graph without provenance cannot be independently reconstructed and should not serve as an engineering acceptance record.

**Studio assignment.** Draft a hazard log and test readiness review with no-go criteria, emergency response, instrumentation checks and authority to stop testing.

**Required confirmation.** Competent-person safety review, signed checklist and traceable incident/near-miss reporting.

Build a reproducible notebook for this assignment. Include a sketch or diagram, table of known quantities with units, a physical basis for each relationship, and a separate list of facts that are merely assumed. Perform the calculation with independent arithmetic. If testing is proposed, explain where the sensors go and how their calibration and resolution affect the result. State what data would falsify the current design hypothesis; do not propose only measurements that could support it. Keep original data rather than overwriting it when outliers or transcription errors are discovered.

For this particular case, apply the following broader check: Track interfaces where heat, stress, force, motion, pressure and dimensions interact. The correct limit often depends on the combined operating state rather than the maximum of one isolated variable. This guards against optimizing one metric while overlooking a coupled physical constraint. Report a design alternative in which the selected performance improves while some other important objective worsens. That alternative may still be appropriate, but the trade must be transparent and tied to stakeholder priorities. Before deciding, check whether the new configuration requires another supplier capability study, additional inspection or a revised safety analysis.

## 5. Exercises: calculation, design and criticism

1. **Definitions:** Explain **failure review and safe test execution** to a technician who knows the equipment but has not studied the model. State the measurable event, required operating condition and one assumption that cannot be read directly from the output.
2. **Hand calculation:** Reproduce the worked case and its governing rule `Residual risk depends on credible events and verified barriers` with all units and significant figures justified. Change one input by +10% and determine whether the direction of change is physically plausible.
3. **Boundary case:** Analyze the specific limitation: A safe operating procedure copied from a different machine may omit project-specific over-speed and containment hazards. Explain which additional calculation, test or design constraint is required and why a single generic safety factor cannot solve the missing-physics problem.
4. **Alternative:** Draft a hazard log and test readiness review with no-go criteria, emergency response, instrumentation checks and authority to stop testing. Propose a second feasible mechanism or component, not merely a different numerical setting of the original choice. Evaluate manufacturing and maintenance implications.
5. **Evidence:** Competent-person safety review, signed checklist and traceable incident/near-miss reporting. Prepare a small table of what would be measured, which instrument would be used, what uncertainty could dominate and whether the result would verify a requirement or validate intended use.

**Instructor checkpoint A.** An answer that repeats the formula without identifying the operational boundary is incomplete. The student's result must have consistent units and a clear physical sign. If the output is expressed as a ratio or probability, explain its numerical range and whether independence assumptions apply. If an optimization is involved, a design that violates a hard constraint is rejected even if its objective is lower.

**Instructor checkpoint B.** Students should distinguish a calculated output from physical evidence. Strong submissions show an independent check, a sensitivity comparison, a plausible counterexample and an actionable test plan. A poor submission uses extra decimal places, repeated simulations, or an appealing chart to imply accuracy that the inputs do not support. A recommendation is not complete without a limitation and a named action to reduce the largest consequential uncertainty.

## 6. Integration with other mechanical disciplines

The design decision in **failure review and safe test execution** is related to **manufacturing, supply chain and sustainable design**. A design that cannot be made, inspected, acquired, repaired or recycled at the expected scale is incomplete. Manufacturing decisions control achievable tolerances, surface integrity, defect distributions, lead times and unit economics. Environmental comparisons must use a consistent functional unit and lifecycle boundary. Think about what information must pass between those two engineering teams and whether the transfer occurs as a load case, geometric tolerance, material property, signal, cost scenario or acceptance test. An interface that lacks an owner may survive several design reviews without being checked. In a final integration meeting, require each assumption to have an identified source and a planned verification activity; record deviations explicitly.

**Engineering notebook output:** One independent arithmetic check, one alternative architecture, one requirement-to-evidence row, one uncertainty statement, and one open risk item to carry into the unit capstone.


---

# U08-L05 — Design review, evidence package and handover

**Unit 8: Integrated Capstone and Engineering Decision-Making**  
**Purpose.** Evaluate one real design decision in the context of an integrated mechanical system. Students should be able to explain the physics, run a bounded calculation, test its assumptions and prepare a defensible design record.

## 1. Physical meaning and engineering relevance

A complete engineering outcome is a documented argument: what was required, what was built, what was measured, what remains uncertain and what may be done next. The handover must distinguish approved uses from excluded or untested conditions.

A good engineering claim starts from the exact outcome being sought and a stated operational setting. In this lesson, explain what happens during commissioning, steady operation, abnormal operation and normal service. A variable that looks constant in a laboratory exercise may change dramatically when equipment ages or moves between sites. A drawing alone cannot show every thermal, mechanical and control dependency; record interfaces and operating sequences as well. Treat the word **system** as a boundary containing components, people, controls and environmental interactions, not simply a list of purchased items.

The governing decision is linked to the unit's wider question: System design culminates in traceable evidence and an honest decision under constraints. A useful engineering dossier ties stakeholder needs to functional architecture, engineering analysis, cost, verification, failure controls, manufacturing and eventual disposition. Unresolved risk is an outcome to report, not a number to conceal. To make the relation operational, write every variable with units, the domain over which it is expected to be useful and the physical mechanism that might violate it. When using a supplied coefficient, say whether it came from a material test, a catalog, a standard, or a hypothetical classroom choice. Do not silently combine catalog ratings at different temperatures or duty cycles. If a concept depends on an uncertain input, use its plausible interval rather than only a best-looking estimate.

## 2. Governing relation and useful calculation

**Core relation or design rule:** `Claim → evidence → uncertainty → disposition`

**Worked case.** A design review can accept a teaching demonstration while explicitly rejecting industrial commissioning. The same analysis may be educationally useful yet insufficient for a safety-critical production decision.

The first check is dimensional: if the symbols represent different physical dimensions, convert to a common SI basis before evaluating. The second check is one limiting case: set a load to zero, make the design very stiff, or let an efficiency approach unity—whichever is physically relevant—and ask if the predicted direction makes sense. The third check is to estimate the size of an ignored term. A compact hand calculation is valuable because it can expose a reversed ratio or a misplaced conversion factor that would otherwise pass through a spreadsheet unnoticed.

Convert the worked case into a design memo: state the known inputs, unknown output, assumptions, calculation, units and consequence of crossing the limit. Make two alternative estimates, one at a favorable operating point and one at a credible adverse point. Explain why the apparent improvement may not translate into a better total system. The correct comparison uses the same function, service life and boundary for each alternative rather than comparing one design at peak efficiency with another at average duty.

## 3. Scope, counterexample and failure conditions

An unexplained “passed” badge on a dashboard conceals test scope and operator assumptions. Reviewers need raw data and deviations, not just polished slides.

A calculation is only as good as its assumed configuration. Ask whether the actual mechanism is linear, whether geometry remains unchanged, whether a temperature-dependent property was treated as fixed, and whether contact, vibration or actuator saturation could introduce a discontinuity. If the model ignores an effect because it appears small, report the evidence supporting that decision. Quantification is not a substitute for identifying hazards: an attractive weighted objective cannot excuse an unverified guard, protection feature, pressure boundary or emergency stop.

A counterexample helps establish the scope. Imagine the original design moved from a controlled teaching bench to a dirty or wet industrial location. The incoming load spectrum, corrosion exposure, calibration frequency and repair resources may be different. Name at least one parameter from the equation that remains meaningful and one omitted mechanism that becomes important. Explain how the design review would change if that mechanism is plausible. Record any consequence whose acceptability must be judged by a competent safety professional rather than inferred from a classroom equation.

## 4. Practical investigation — What could reverse the decision?

Identify the single uncertain parameter most likely to change the preferred alternative. Design a low-risk test that would measure it and record what evidence would justify changing the recommendation.

**Studio assignment.** Assemble a 20-page final dossier with drawings, bill of materials, test results, model limitations, lifecycle plan and unresolved issue log.

**Required confirmation.** Independent reviewer sign-off, reproducibility package, retained raw data and a documented permitted-use boundary.

Build a reproducible notebook for this assignment. Include a sketch or diagram, table of known quantities with units, a physical basis for each relationship, and a separate list of facts that are merely assumed. Perform the calculation with independent arithmetic. If testing is proposed, explain where the sensors go and how their calibration and resolution affect the result. State what data would falsify the current design hypothesis; do not propose only measurements that could support it. Keep original data rather than overwriting it when outliers or transcription errors are discovered.

For this particular case, apply the following broader check: Evaluate dynamic response using an identified inertia, stiffness, damping and actuator torque-speed curve. Verify sensing and sampling delays, saturations, and the behavior of the machine after power interruption. This guards against optimizing one metric while overlooking a coupled physical constraint. Report a design alternative in which the selected performance improves while some other important objective worsens. That alternative may still be appropriate, but the trade must be transparent and tied to stakeholder priorities. Before deciding, check whether the new configuration requires another supplier capability study, additional inspection or a revised safety analysis.

## 5. Exercises: calculation, design and criticism

1. **Definitions:** Explain **design review, evidence package and handover** to a technician who knows the equipment but has not studied the model. State the measurable event, required operating condition and one assumption that cannot be read directly from the output.
2. **Hand calculation:** Reproduce the worked case and its governing rule `Claim → evidence → uncertainty → disposition` with all units and significant figures justified. Change one input by +10% and determine whether the direction of change is physically plausible.
3. **Boundary case:** Analyze the specific limitation: An unexplained “passed” badge on a dashboard conceals test scope and operator assumptions. Reviewers need raw data and deviations, not just polished slides. Explain which additional calculation, test or design constraint is required and why a single generic safety factor cannot solve the missing-physics problem.
4. **Alternative:** Assemble a 20-page final dossier with drawings, bill of materials, test results, model limitations, lifecycle plan and unresolved issue log. Propose a second feasible mechanism or component, not merely a different numerical setting of the original choice. Evaluate manufacturing and maintenance implications.
5. **Evidence:** Independent reviewer sign-off, reproducibility package, retained raw data and a documented permitted-use boundary. Prepare a small table of what would be measured, which instrument would be used, what uncertainty could dominate and whether the result would verify a requirement or validate intended use.

**Instructor checkpoint A.** An answer that repeats the formula without identifying the operational boundary is incomplete. The student's result must have consistent units and a clear physical sign. If the output is expressed as a ratio or probability, explain its numerical range and whether independence assumptions apply. If an optimization is involved, a design that violates a hard constraint is rejected even if its objective is lower.

**Instructor checkpoint B.** Students should distinguish a calculated output from physical evidence. Strong submissions show an independent check, a sensitivity comparison, a plausible counterexample and an actionable test plan. A poor submission uses extra decimal places, repeated simulations, or an appealing chart to imply accuracy that the inputs do not support. A recommendation is not complete without a limitation and a named action to reduce the largest consequential uncertainty.

## 6. Integration with other mechanical disciplines

The design decision in **design review, evidence package and handover** is related to **uncertainty, robustness, testing and reliability**. Nominal performance is not robust performance. Uncertain loading, material properties, wear, manufacturing variation and model inadequacy produce distributions or bounded envelopes. Verification asks whether the calculation or implementation is correct; validation asks whether the model represents the intended reality. Think about what information must pass between those two engineering teams and whether the transfer occurs as a load case, geometric tolerance, material property, signal, cost scenario or acceptance test. An interface that lacks an owner may survive several design reviews without being checked. In a final integration meeting, require each assumption to have an identified source and a planned verification activity; record deviations explicitly.

**Engineering notebook output:** One independent arithmetic check, one alternative architecture, one requirement-to-evidence row, one uncertainty statement, and one open risk item to carry into the unit capstone.


---

