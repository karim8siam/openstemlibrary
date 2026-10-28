# Unit 06: Manufacturing, Supply Chain and Sustainable Design

**Course Code**: MSO 406 · **Level**: Advanced Undergraduate Engineering

## Unit Overview & Physical Foundations

This comprehensive university textbook unit covers the theoretical framework, physical modeling, mathematical governing equations, and engineering applications of **Manufacturing, Supply Chain and Sustainable Design**.

# U06-L01 — Process selection and design for manufacture

**Unit 6: Manufacturing, Supply Chain and Sustainable Design**  
**Purpose.** Evaluate one real design decision in the context of an integrated mechanical system. Students should be able to explain the physics, run a bounded calculation, test its assumptions and prepare a defensible design record.

## 1. Physical meaning and engineering relevance

Select manufacturing routes from geometry, volume, material, functional surfaces, tolerance, time and inspection capability. Process cost is not simply cycle time; fixtures, scrap, tooling and rework matter.

A good engineering claim starts from the exact outcome being sought and a stated operational setting. In this lesson, explain what happens during commissioning, steady operation, abnormal operation and normal service. A variable that looks constant in a laboratory exercise may change dramatically when equipment ages or moves between sites. A drawing alone cannot show every thermal, mechanical and control dependency; record interfaces and operating sequences as well. Treat the word **system** as a boundary containing components, people, controls and environmental interactions, not simply a list of purchased items.

The governing decision is linked to the unit's wider question: A design that cannot be made, inspected, acquired, repaired or recycled at the expected scale is incomplete. Manufacturing decisions control achievable tolerances, surface integrity, defect distributions, lead times and unit economics. Environmental comparisons must use a consistent functional unit and lifecycle boundary. To make the relation operational, write every variable with units, the domain over which it is expected to be useful and the physical mechanism that might violate it. When using a supplied coefficient, say whether it came from a material test, a catalog, a standard, or a hypothetical classroom choice. Do not silently combine catalog ratings at different temperatures or duty cycles. If a concept depends on an uncertain input, use its plausible interval rather than only a best-looking estimate.

## 2. Governing relation and useful calculation

**Core relation or design rule:** `Unit cost = variable cost + fixed cost / batch size`

**Worked case.** A process requiring 10,000 currency units in tooling and 15 per unit has different economics from a tool-free process costing 35 per unit. Their simplified break-even occurs at 500 parts, before yield and financing adjustments.

The first check is dimensional: if the symbols represent different physical dimensions, convert to a common SI basis before evaluating. The second check is one limiting case: set a load to zero, make the design very stiff, or let an efficiency approach unity—whichever is physically relevant—and ask if the predicted direction makes sense. The third check is to estimate the size of an ignored term. A compact hand calculation is valuable because it can expose a reversed ratio or a misplaced conversion factor that would otherwise pass through a spreadsheet unnoticed.

Convert the worked case into a design memo: state the known inputs, unknown output, assumptions, calculation, units and consequence of crossing the limit. Make two alternative estimates, one at a favorable operating point and one at a credible adverse point. Explain why the apparent improvement may not translate into a better total system. The correct comparison uses the same function, service life and boundary for each alternative rather than comparing one design at peak efficiency with another at average duty.

## 3. Scope, counterexample and failure conditions

A low quoted unit price may exclude inspection and rejected material. A part fabricated successfully once may not have reliable process capability.

A calculation is only as good as its assumed configuration. Ask whether the actual mechanism is linear, whether geometry remains unchanged, whether a temperature-dependent property was treated as fixed, and whether contact, vibration or actuator saturation could introduce a discontinuity. If the model ignores an effect because it appears small, report the evidence supporting that decision. Quantification is not a substitute for identifying hazards: an attractive weighted objective cannot excuse an unverified guard, protection feature, pressure boundary or emergency stop.

A counterexample helps establish the scope. Imagine the original design moved from a controlled teaching bench to a dirty or wet industrial location. The incoming load spectrum, corrosion exposure, calibration frequency and repair resources may be different. Name at least one parameter from the equation that remains meaningful and one omitted mechanism that becomes important. Explain how the design review would change if that mechanism is plausible. Record any consequence whose acceptability must be judged by a competent safety professional rather than inferred from a classroom equation.

## 4. Practical investigation — What is controlled?

State the decision variable, its allowed range, and which physical observations it can change. A variable that cannot be adjusted by the engineer is a disturbance or measured parameter; confusing the two makes the optimization unrealistic.

**Studio assignment.** Develop process routes for a complex bracket at batches of 10, 100 and 10,000 and show sensitivity to scrap rate.

**Required confirmation.** Supplier capability evidence, drawing review and pilot lot dimensional reports.

Build a reproducible notebook for this assignment. Include a sketch or diagram, table of known quantities with units, a physical basis for each relationship, and a separate list of facts that are merely assumed. Perform the calculation with independent arithmetic. If testing is proposed, explain where the sensors go and how their calibration and resolution affect the result. State what data would falsify the current design hypothesis; do not propose only measurements that could support it. Keep original data rather than overwriting it when outliers or transcription errors are discovered.

For this particular case, apply the following broader check: Represent measured scatter, uncertainty in model parameters and omitted mechanisms separately. Choose verification evidence that addresses the highest-consequence failure modes, not just the easiest measurements. This guards against optimizing one metric while overlooking a coupled physical constraint. Report a design alternative in which the selected performance improves while some other important objective worsens. That alternative may still be appropriate, but the trade must be transparent and tied to stakeholder priorities. Before deciding, check whether the new configuration requires another supplier capability study, additional inspection or a revised safety analysis.

## 5. Exercises: calculation, design and criticism

1. **Definitions:** Explain **process selection and design for manufacture** to a technician who knows the equipment but has not studied the model. State the measurable event, required operating condition and one assumption that cannot be read directly from the output.
2. **Hand calculation:** Reproduce the worked case and its governing rule `Unit cost = variable cost + fixed cost / batch size` with all units and significant figures justified. Change one input by +10% and determine whether the direction of change is physically plausible.
3. **Boundary case:** Analyze the specific limitation: A low quoted unit price may exclude inspection and rejected material. A part fabricated successfully once may not have reliable process capability. Explain which additional calculation, test or design constraint is required and why a single generic safety factor cannot solve the missing-physics problem.
4. **Alternative:** Develop process routes for a complex bracket at batches of 10, 100 and 10,000 and show sensitivity to scrap rate. Propose a second feasible mechanism or component, not merely a different numerical setting of the original choice. Evaluate manufacturing and maintenance implications.
5. **Evidence:** Supplier capability evidence, drawing review and pilot lot dimensional reports. Prepare a small table of what would be measured, which instrument would be used, what uncertainty could dominate and whether the result would verify a requirement or validate intended use.

**Instructor checkpoint A.** An answer that repeats the formula without identifying the operational boundary is incomplete. The student's result must have consistent units and a clear physical sign. If the output is expressed as a ratio or probability, explain its numerical range and whether independence assumptions apply. If an optimization is involved, a design that violates a hard constraint is rejected even if its objective is lower.

**Instructor checkpoint B.** Students should distinguish a calculated output from physical evidence. Strong submissions show an independent check, a sensitivity comparison, a plausible counterexample and an actionable test plan. A poor submission uses extra decimal places, repeated simulations, or an appealing chart to imply accuracy that the inputs do not support. A recommendation is not complete without a limitation and a named action to reduce the largest consequential uncertainty.

## 6. Integration with other mechanical disciplines

The design decision in **process selection and design for manufacture** is related to **engineering requirements and system architecture**. A mechanical system is an arrangement of components that jointly deliver a function within physical, financial and regulatory limits. Requirements must state observable performance, mission, environment, boundaries and evidence of acceptance. A specification without a test method cannot serve as a contract between customer, designer and verifier. Think about what information must pass between those two engineering teams and whether the transfer occurs as a load case, geometric tolerance, material property, signal, cost scenario or acceptance test. An interface that lacks an owner may survive several design reviews without being checked. In a final integration meeting, require each assumption to have an identified source and a planned verification activity; record deviations explicitly.

**Engineering notebook output:** One independent arithmetic check, one alternative architecture, one requirement-to-evidence row, one uncertainty statement, and one open risk item to carry into the unit capstone.


---

# U06-L02 — Geometric dimensioning and tolerance stackups

**Unit 6: Manufacturing, Supply Chain and Sustainable Design**  
**Purpose.** Evaluate one real design decision in the context of an integrated mechanical system. Students should be able to explain the physics, run a bounded calculation, test its assumptions and prepare a defensible design record.

## 1. Physical meaning and engineering relevance

A tolerance is a functional allocation, not an arbitrary machining precision. Worst-case and statistical stackups answer different questions. Datums must correspond to assembly function and how the part is measured.

A good engineering claim starts from the exact outcome being sought and a stated operational setting. In this lesson, explain what happens during commissioning, steady operation, abnormal operation and normal service. A variable that looks constant in a laboratory exercise may change dramatically when equipment ages or moves between sites. A drawing alone cannot show every thermal, mechanical and control dependency; record interfaces and operating sequences as well. Treat the word **system** as a boundary containing components, people, controls and environmental interactions, not simply a list of purchased items.

The governing decision is linked to the unit's wider question: A design that cannot be made, inspected, acquired, repaired or recycled at the expected scale is incomplete. Manufacturing decisions control achievable tolerances, surface integrity, defect distributions, lead times and unit economics. Environmental comparisons must use a consistent functional unit and lifecycle boundary. To make the relation operational, write every variable with units, the domain over which it is expected to be useful and the physical mechanism that might violate it. When using a supplied coefficient, say whether it came from a material test, a catalog, a standard, or a hypothetical classroom choice. Do not silently combine catalog ratings at different temperatures or duty cycles. If a concept depends on an uncertain input, use its plausible interval rather than only a best-looking estimate.

## 2. Governing relation and useful calculation

**Core relation or design rule:** `T_wc = Σ |t_i|`

**Worked case.** Four independent locating dimensions with ±0.10 mm worst-case deviations can produce ±0.40 mm total stack, but the actual assembly geometry and sign conventions determine the complete result.

The first check is dimensional: if the symbols represent different physical dimensions, convert to a common SI basis before evaluating. The second check is one limiting case: set a load to zero, make the design very stiff, or let an efficiency approach unity—whichever is physically relevant—and ask if the predicted direction makes sense. The third check is to estimate the size of an ignored term. A compact hand calculation is valuable because it can expose a reversed ratio or a misplaced conversion factor that would otherwise pass through a spreadsheet unnoticed.

Convert the worked case into a design memo: state the known inputs, unknown output, assumptions, calculation, units and consequence of crossing the limit. Make two alternative estimates, one at a favorable operating point and one at a credible adverse point. Explain why the apparent improvement may not translate into a better total system. The correct comparison uses the same function, service life and boundary for each alternative rather than comparing one design at peak efficiency with another at average duty.

## 3. Scope, counterexample and failure conditions

Applying root-sum-square blindly assumes suitable independence and distributions and may understate worst-case critical clearances.

A calculation is only as good as its assumed configuration. Ask whether the actual mechanism is linear, whether geometry remains unchanged, whether a temperature-dependent property was treated as fixed, and whether contact, vibration or actuator saturation could introduce a discontinuity. If the model ignores an effect because it appears small, report the evidence supporting that decision. Quantification is not a substitute for identifying hazards: an attractive weighted objective cannot excuse an unverified guard, protection feature, pressure boundary or emergency stop.

A counterexample helps establish the scope. Imagine the original design moved from a controlled teaching bench to a dirty or wet industrial location. The incoming load spectrum, corrosion exposure, calibration frequency and repair resources may be different. Name at least one parameter from the equation that remains meaningful and one omitted mechanism that becomes important. Explain how the design review would change if that mechanism is plausible. Record any consequence whose acceptability must be judged by a competent safety professional rather than inferred from a classroom equation.

## 4. Practical investigation — What is conserved?

Start by tracing mass, force, energy or information through the studied boundary. Write down any neglected source, loss or interface. When a numerical output appears to violate a conservation statement, inspect boundary definitions before changing the data.

**Studio assignment.** Draw a datum scheme for a bearing cap, allocate critical clearances and calculate the worst-case stack independently.

**Required confirmation.** Gage repeatability review, assembly trial and inspection agreement with the supplier.

Build a reproducible notebook for this assignment. Include a sketch or diagram, table of known quantities with units, a physical basis for each relationship, and a separate list of facts that are merely assumed. Perform the calculation with independent arithmetic. If testing is proposed, explain where the sensors go and how their calibration and resolution affect the result. State what data would falsify the current design hypothesis; do not propose only measurements that could support it. Keep original data rather than overwriting it when outliers or transcription errors are discovered.

For this particular case, apply the following broader check: Present a traceable technical argument that allows another engineer to reconstruct the design choice. List rejected concepts, open issues, physical test evidence, planned maintenance and permitted operating limits. This guards against optimizing one metric while overlooking a coupled physical constraint. Report a design alternative in which the selected performance improves while some other important objective worsens. That alternative may still be appropriate, but the trade must be transparent and tied to stakeholder priorities. Before deciding, check whether the new configuration requires another supplier capability study, additional inspection or a revised safety analysis.

## 5. Exercises: calculation, design and criticism

1. **Definitions:** Explain **geometric dimensioning and tolerance stackups** to a technician who knows the equipment but has not studied the model. State the measurable event, required operating condition and one assumption that cannot be read directly from the output.
2. **Hand calculation:** Reproduce the worked case and its governing rule `T_wc = Σ |t_i|` with all units and significant figures justified. Change one input by +10% and determine whether the direction of change is physically plausible.
3. **Boundary case:** Analyze the specific limitation: Applying root-sum-square blindly assumes suitable independence and distributions and may understate worst-case critical clearances. Explain which additional calculation, test or design constraint is required and why a single generic safety factor cannot solve the missing-physics problem.
4. **Alternative:** Draw a datum scheme for a bearing cap, allocate critical clearances and calculate the worst-case stack independently. Propose a second feasible mechanism or component, not merely a different numerical setting of the original choice. Evaluate manufacturing and maintenance implications.
5. **Evidence:** Gage repeatability review, assembly trial and inspection agreement with the supplier. Prepare a small table of what would be measured, which instrument would be used, what uncertainty could dominate and whether the result would verify a requirement or validate intended use.

**Instructor checkpoint A.** An answer that repeats the formula without identifying the operational boundary is incomplete. The student's result must have consistent units and a clear physical sign. If the output is expressed as a ratio or probability, explain its numerical range and whether independence assumptions apply. If an optimization is involved, a design that violates a hard constraint is rejected even if its objective is lower.

**Instructor checkpoint B.** Students should distinguish a calculated output from physical evidence. Strong submissions show an independent check, a sensitivity comparison, a plausible counterexample and an actionable test plan. A poor submission uses extra decimal places, repeated simulations, or an appealing chart to imply accuracy that the inputs do not support. A recommendation is not complete without a limitation and a named action to reduce the largest consequential uncertainty.

## 6. Integration with other mechanical disciplines

The design decision in **geometric dimensioning and tolerance stackups** is related to **physics-based modeling and digital engineering**. A useful model states assumptions, state variables, boundary conditions, conservation relations and applicable time scale. A model is not a digital twin merely because it has a dashboard. Its predictive usefulness rests on calibration, identification and comparison with measurements independent of fitting data. Think about what information must pass between those two engineering teams and whether the transfer occurs as a load case, geometric tolerance, material property, signal, cost scenario or acceptance test. An interface that lacks an owner may survive several design reviews without being checked. In a final integration meeting, require each assumption to have an identified source and a planned verification activity; record deviations explicitly.

**Engineering notebook output:** One independent arithmetic check, one alternative architecture, one requirement-to-evidence row, one uncertainty statement, and one open risk item to carry into the unit capstone.


---

# U06-L03 — Material selection and end-of-life

**Unit 6: Manufacturing, Supply Chain and Sustainable Design**  
**Purpose.** Evaluate one real design decision in the context of an integrated mechanical system. Students should be able to explain the physics, run a bounded calculation, test its assumptions and prepare a defensible design record.

## 1. Physical meaning and engineering relevance

Material choice involves mechanical and thermal properties, corrosion environment, embodied impacts, recycling infrastructure and supply risk. A lightweight alloy may reduce operating energy but require energy-intensive production.

A good engineering claim starts from the exact outcome being sought and a stated operational setting. In this lesson, explain what happens during commissioning, steady operation, abnormal operation and normal service. A variable that looks constant in a laboratory exercise may change dramatically when equipment ages or moves between sites. A drawing alone cannot show every thermal, mechanical and control dependency; record interfaces and operating sequences as well. Treat the word **system** as a boundary containing components, people, controls and environmental interactions, not simply a list of purchased items.

The governing decision is linked to the unit's wider question: A design that cannot be made, inspected, acquired, repaired or recycled at the expected scale is incomplete. Manufacturing decisions control achievable tolerances, surface integrity, defect distributions, lead times and unit economics. Environmental comparisons must use a consistent functional unit and lifecycle boundary. To make the relation operational, write every variable with units, the domain over which it is expected to be useful and the physical mechanism that might violate it. When using a supplied coefficient, say whether it came from a material test, a catalog, a standard, or a hypothetical classroom choice. Do not silently combine catalog ratings at different temperatures or duty cycles. If a concept depends on an uncertain input, use its plausible interval rather than only a best-looking estimate.

## 2. Governing relation and useful calculation

**Core relation or design rule:** `Lifecycle impact = production + use + maintenance + disposal`

**Worked case.** Compare a 3 kg aluminum panel with a 5 kg steel panel that provides the same function. The lighter panel is not automatically greener unless the use-phase savings, recycled content and lifetime assumptions justify it.

The first check is dimensional: if the symbols represent different physical dimensions, convert to a common SI basis before evaluating. The second check is one limiting case: set a load to zero, make the design very stiff, or let an efficiency approach unity—whichever is physically relevant—and ask if the predicted direction makes sense. The third check is to estimate the size of an ignored term. A compact hand calculation is valuable because it can expose a reversed ratio or a misplaced conversion factor that would otherwise pass through a spreadsheet unnoticed.

Convert the worked case into a design memo: state the known inputs, unknown output, assumptions, calculation, units and consequence of crossing the limit. Make two alternative estimates, one at a favorable operating point and one at a credible adverse point. Explain why the apparent improvement may not translate into a better total system. The correct comparison uses the same function, service life and boundary for each alternative rather than comparing one design at peak efficiency with another at average duty.

## 3. Scope, counterexample and failure conditions

Comparisons using different service lives or functional units are invalid. Generic emission factors may not reflect the supplier process or local electricity mix.

A calculation is only as good as its assumed configuration. Ask whether the actual mechanism is linear, whether geometry remains unchanged, whether a temperature-dependent property was treated as fixed, and whether contact, vibration or actuator saturation could introduce a discontinuity. If the model ignores an effect because it appears small, report the evidence supporting that decision. Quantification is not a substitute for identifying hazards: an attractive weighted objective cannot excuse an unverified guard, protection feature, pressure boundary or emergency stop.

A counterexample helps establish the scope. Imagine the original design moved from a controlled teaching bench to a dirty or wet industrial location. The incoming load spectrum, corrosion exposure, calibration frequency and repair resources may be different. Name at least one parameter from the equation that remains meaningful and one omitted mechanism that becomes important. Explain how the design review would change if that mechanism is plausible. Record any consequence whose acceptability must be judged by a competent safety professional rather than inferred from a classroom equation.

## 4. Practical investigation — Where are the limits?

Report physical operating limits, catalog limits and mandated safeguards separately. A design which fails an essential condition is not acceptable just because its average objective value is attractive.

**Studio assignment.** Prepare a material selection table that separates measured properties, source-reported impacts and speculative recycling assumptions.

**Required confirmation.** Material certificate, supplier provenance, service-life evidence and transparent system-boundary statement.

Build a reproducible notebook for this assignment. Include a sketch or diagram, table of known quantities with units, a physical basis for each relationship, and a separate list of facts that are merely assumed. Perform the calculation with independent arithmetic. If testing is proposed, explain where the sensors go and how their calibration and resolution affect the result. State what data would falsify the current design hypothesis; do not propose only measurements that could support it. Keep original data rather than overwriting it when outliers or transcription errors are discovered.

For this particular case, apply the following broader check: Form a trace from need through required function and quantified threshold to an instrumented acceptance result. Avoid a requirement stating only the preferred component; that describes a proposed solution rather than an outcome. This guards against optimizing one metric while overlooking a coupled physical constraint. Report a design alternative in which the selected performance improves while some other important objective worsens. That alternative may still be appropriate, but the trade must be transparent and tied to stakeholder priorities. Before deciding, check whether the new configuration requires another supplier capability study, additional inspection or a revised safety analysis.

## 5. Exercises: calculation, design and criticism

1. **Definitions:** Explain **material selection and end-of-life** to a technician who knows the equipment but has not studied the model. State the measurable event, required operating condition and one assumption that cannot be read directly from the output.
2. **Hand calculation:** Reproduce the worked case and its governing rule `Lifecycle impact = production + use + maintenance + disposal` with all units and significant figures justified. Change one input by +10% and determine whether the direction of change is physically plausible.
3. **Boundary case:** Analyze the specific limitation: Comparisons using different service lives or functional units are invalid. Generic emission factors may not reflect the supplier process or local electricity mix. Explain which additional calculation, test or design constraint is required and why a single generic safety factor cannot solve the missing-physics problem.
4. **Alternative:** Prepare a material selection table that separates measured properties, source-reported impacts and speculative recycling assumptions. Propose a second feasible mechanism or component, not merely a different numerical setting of the original choice. Evaluate manufacturing and maintenance implications.
5. **Evidence:** Material certificate, supplier provenance, service-life evidence and transparent system-boundary statement. Prepare a small table of what would be measured, which instrument would be used, what uncertainty could dominate and whether the result would verify a requirement or validate intended use.

**Instructor checkpoint A.** An answer that repeats the formula without identifying the operational boundary is incomplete. The student's result must have consistent units and a clear physical sign. If the output is expressed as a ratio or probability, explain its numerical range and whether independence assumptions apply. If an optimization is involved, a design that violates a hard constraint is rejected even if its objective is lower.

**Instructor checkpoint B.** Students should distinguish a calculated output from physical evidence. Strong submissions show an independent check, a sensitivity comparison, a plausible counterexample and an actionable test plan. A poor submission uses extra decimal places, repeated simulations, or an appealing chart to imply accuracy that the inputs do not support. A recommendation is not complete without a limitation and a named action to reduce the largest consequential uncertainty.

## 6. Integration with other mechanical disciplines

The design decision in **material selection and end-of-life** is related to **optimization methods and design tradeoffs**. Design optimization asks which feasible decision vector gives the best defensible outcome. Feasibility conditions are not preferences. Multiobjective design typically produces a Pareto set rather than one uniquely correct answer, and ranking alternatives requires transparent priorities and sensitivity to uncertain weights. Think about what information must pass between those two engineering teams and whether the transfer occurs as a load case, geometric tolerance, material property, signal, cost scenario or acceptance test. An interface that lacks an owner may survive several design reviews without being checked. In a final integration meeting, require each assumption to have an identified source and a planned verification activity; record deviations explicitly.

**Engineering notebook output:** One independent arithmetic check, one alternative architecture, one requirement-to-evidence row, one uncertainty statement, and one open risk item to carry into the unit capstone.


---

# U06-L04 — Assembly planning, maintainability and serviceability

**Unit 6: Manufacturing, Supply Chain and Sustainable Design**  
**Purpose.** Evaluate one real design decision in the context of an integrated mechanical system. Students should be able to explain the physics, run a bounded calculation, test its assumptions and prepare a defensible design record.

## 1. Physical meaning and engineering relevance

Design for assembly reduces unnecessary handling, alignment steps and inaccessible fasteners. Design for maintenance asks whether inspection, isolation and replacement can be done without unsafe improvisation or excessive downtime.

A good engineering claim starts from the exact outcome being sought and a stated operational setting. In this lesson, explain what happens during commissioning, steady operation, abnormal operation and normal service. A variable that looks constant in a laboratory exercise may change dramatically when equipment ages or moves between sites. A drawing alone cannot show every thermal, mechanical and control dependency; record interfaces and operating sequences as well. Treat the word **system** as a boundary containing components, people, controls and environmental interactions, not simply a list of purchased items.

The governing decision is linked to the unit's wider question: A design that cannot be made, inspected, acquired, repaired or recycled at the expected scale is incomplete. Manufacturing decisions control achievable tolerances, surface integrity, defect distributions, lead times and unit economics. Environmental comparisons must use a consistent functional unit and lifecycle boundary. To make the relation operational, write every variable with units, the domain over which it is expected to be useful and the physical mechanism that might violate it. When using a supplied coefficient, say whether it came from a material test, a catalog, a standard, or a hypothetical classroom choice. Do not silently combine catalog ratings at different temperatures or duty cycles. If a concept depends on an uncertain input, use its plausible interval rather than only a best-looking estimate.

## 2. Governing relation and useful calculation

**Core relation or design rule:** `Expected maintenance cost = frequency × event consequence`

**Worked case.** A sealed cartridge may cost more initially but allow a technician to replace an actuator in 30 minutes rather than four hours. The benefit depends on event frequency, stocking policy and whether field repair is permitted.

The first check is dimensional: if the symbols represent different physical dimensions, convert to a common SI basis before evaluating. The second check is one limiting case: set a load to zero, make the design very stiff, or let an efficiency approach unity—whichever is physically relevant—and ask if the predicted direction makes sense. The third check is to estimate the size of an ignored term. A compact hand calculation is valuable because it can expose a reversed ratio or a misplaced conversion factor that would otherwise pass through a spreadsheet unnoticed.

Convert the worked case into a design memo: state the known inputs, unknown output, assumptions, calculation, units and consequence of crossing the limit. Make two alternative estimates, one at a favorable operating point and one at a credible adverse point. Explain why the apparent improvement may not translate into a better total system. The correct comparison uses the same function, service life and boundary for each alternative rather than comparing one design at peak efficiency with another at average duty.

## 3. Scope, counterexample and failure conditions

Component modularity does not guarantee reliability: extra connectors and seals introduce possible failure interfaces.

A calculation is only as good as its assumed configuration. Ask whether the actual mechanism is linear, whether geometry remains unchanged, whether a temperature-dependent property was treated as fixed, and whether contact, vibration or actuator saturation could introduce a discontinuity. If the model ignores an effect because it appears small, report the evidence supporting that decision. Quantification is not a substitute for identifying hazards: an attractive weighted objective cannot excuse an unverified guard, protection feature, pressure boundary or emergency stop.

A counterexample helps establish the scope. Imagine the original design moved from a controlled teaching bench to a dirty or wet industrial location. The incoming load spectrum, corrosion exposure, calibration frequency and repair resources may be different. Name at least one parameter from the equation that remains meaningful and one omitted mechanism that becomes important. Explain how the design review would change if that mechanism is plausible. Record any consequence whose acceptability must be judged by a competent safety professional rather than inferred from a classroom equation.

## 4. Practical investigation — What is the evidence?

Maintain raw measurements, instrument calibration data, model input files and revision identifiers. An output graph without provenance cannot be independently reconstructed and should not serve as an engineering acceptance record.

**Studio assignment.** Create an assembly storyboard and a replacement operation plan, identifying tools, lift requirements, guards and verification after reassembly.

**Required confirmation.** Timed service rehearsal with representative tools, safe isolation and feedback from technicians.

Build a reproducible notebook for this assignment. Include a sketch or diagram, table of known quantities with units, a physical basis for each relationship, and a separate list of facts that are merely assumed. Perform the calculation with independent arithmetic. If testing is proposed, explain where the sensors go and how their calibration and resolution affect the result. State what data would falsify the current design hypothesis; do not propose only measurements that could support it. Keep original data rather than overwriting it when outliers or transcription errors are discovered.

For this particular case, apply the following broader check: Start with the system boundary and distinguish conservation equations from fitted correlations. Identify what inputs are measured, taken from vendor data or chosen for teaching. Do not claim that a model represents the plant until a separate measurement comparison has been made. This guards against optimizing one metric while overlooking a coupled physical constraint. Report a design alternative in which the selected performance improves while some other important objective worsens. That alternative may still be appropriate, but the trade must be transparent and tied to stakeholder priorities. Before deciding, check whether the new configuration requires another supplier capability study, additional inspection or a revised safety analysis.

## 5. Exercises: calculation, design and criticism

1. **Definitions:** Explain **assembly planning, maintainability and serviceability** to a technician who knows the equipment but has not studied the model. State the measurable event, required operating condition and one assumption that cannot be read directly from the output.
2. **Hand calculation:** Reproduce the worked case and its governing rule `Expected maintenance cost = frequency × event consequence` with all units and significant figures justified. Change one input by +10% and determine whether the direction of change is physically plausible.
3. **Boundary case:** Analyze the specific limitation: Component modularity does not guarantee reliability: extra connectors and seals introduce possible failure interfaces. Explain which additional calculation, test or design constraint is required and why a single generic safety factor cannot solve the missing-physics problem.
4. **Alternative:** Create an assembly storyboard and a replacement operation plan, identifying tools, lift requirements, guards and verification after reassembly. Propose a second feasible mechanism or component, not merely a different numerical setting of the original choice. Evaluate manufacturing and maintenance implications.
5. **Evidence:** Timed service rehearsal with representative tools, safe isolation and feedback from technicians. Prepare a small table of what would be measured, which instrument would be used, what uncertainty could dominate and whether the result would verify a requirement or validate intended use.

**Instructor checkpoint A.** An answer that repeats the formula without identifying the operational boundary is incomplete. The student's result must have consistent units and a clear physical sign. If the output is expressed as a ratio or probability, explain its numerical range and whether independence assumptions apply. If an optimization is involved, a design that violates a hard constraint is rejected even if its objective is lower.

**Instructor checkpoint B.** Students should distinguish a calculated output from physical evidence. Strong submissions show an independent check, a sensitivity comparison, a plausible counterexample and an actionable test plan. A poor submission uses extra decimal places, repeated simulations, or an appealing chart to imply accuracy that the inputs do not support. A recommendation is not complete without a limitation and a named action to reduce the largest consequential uncertainty.

## 6. Integration with other mechanical disciplines

The design decision in **assembly planning, maintainability and serviceability** is related to **structural, thermal and fluid co-design**. Mechanical design is coupled: increasing stiffness can raise mass; reducing friction changes heat generation; additional insulation changes expansion and packaging. Sequential discipline-by-discipline optimization often shifts a problem to another subsystem. Co-design evaluates physical interfaces and operating envelopes. Think about what information must pass between those two engineering teams and whether the transfer occurs as a load case, geometric tolerance, material property, signal, cost scenario or acceptance test. An interface that lacks an owner may survive several design reviews without being checked. In a final integration meeting, require each assumption to have an identified source and a planned verification activity; record deviations explicitly.

**Engineering notebook output:** One independent arithmetic check, one alternative architecture, one requirement-to-evidence row, one uncertainty statement, and one open risk item to carry into the unit capstone.


---

# U06-L05 — Lifecycle cost and responsible sourcing

**Unit 6: Manufacturing, Supply Chain and Sustainable Design**  
**Purpose.** Evaluate one real design decision in the context of an integrated mechanical system. Students should be able to explain the physics, run a bounded calculation, test its assumptions and prepare a defensible design record.

## 1. Physical meaning and engineering relevance

Up-front procurement price is only one term in total ownership cost. Energy, inspection, lost production, maintenance, replacement and disposal can dominate. Discount cash flows consistently without pricing away mandatory safety controls.

A good engineering claim starts from the exact outcome being sought and a stated operational setting. In this lesson, explain what happens during commissioning, steady operation, abnormal operation and normal service. A variable that looks constant in a laboratory exercise may change dramatically when equipment ages or moves between sites. A drawing alone cannot show every thermal, mechanical and control dependency; record interfaces and operating sequences as well. Treat the word **system** as a boundary containing components, people, controls and environmental interactions, not simply a list of purchased items.

The governing decision is linked to the unit's wider question: A design that cannot be made, inspected, acquired, repaired or recycled at the expected scale is incomplete. Manufacturing decisions control achievable tolerances, surface integrity, defect distributions, lead times and unit economics. Environmental comparisons must use a consistent functional unit and lifecycle boundary. To make the relation operational, write every variable with units, the domain over which it is expected to be useful and the physical mechanism that might violate it. When using a supplied coefficient, say whether it came from a material test, a catalog, a standard, or a hypothetical classroom choice. Do not silently combine catalog ratings at different temperatures or duty cycles. If a concept depends on an uncertain input, use its plausible interval rather than only a best-looking estimate.

## 2. Governing relation and useful calculation

**Core relation or design rule:** `LCC = CapEx + PV(Energy + Maintenance + Replacement − Salvage)`

**Worked case.** Two motors differ by 1,000 currency units in purchase price. The more efficient unit saves 300 per year for eight years. Discounting at 8% gives present savings around 1,724, so the higher cost may be justified before repairs and taxes.

The first check is dimensional: if the symbols represent different physical dimensions, convert to a common SI basis before evaluating. The second check is one limiting case: set a load to zero, make the design very stiff, or let an efficiency approach unity—whichever is physically relevant—and ask if the predicted direction makes sense. The third check is to estimate the size of an ignored term. A compact hand calculation is valuable because it can expose a reversed ratio or a misplaced conversion factor that would otherwise pass through a spreadsheet unnoticed.

Convert the worked case into a design memo: state the known inputs, unknown output, assumptions, calculation, units and consequence of crossing the limit. Make two alternative estimates, one at a favorable operating point and one at a credible adverse point. Explain why the apparent improvement may not translate into a better total system. The correct comparison uses the same function, service life and boundary for each alternative rather than comparing one design at peak efficiency with another at average duty.

## 3. Scope, counterexample and failure conditions

A deterministic NPV obscures uncertainty in energy cost, actual load fraction and equipment lifetime. Supplier promises are not field data.

A calculation is only as good as its assumed configuration. Ask whether the actual mechanism is linear, whether geometry remains unchanged, whether a temperature-dependent property was treated as fixed, and whether contact, vibration or actuator saturation could introduce a discontinuity. If the model ignores an effect because it appears small, report the evidence supporting that decision. Quantification is not a substitute for identifying hazards: an attractive weighted objective cannot excuse an unverified guard, protection feature, pressure boundary or emergency stop.

A counterexample helps establish the scope. Imagine the original design moved from a controlled teaching bench to a dirty or wet industrial location. The incoming load spectrum, corrosion exposure, calibration frequency and repair resources may be different. Name at least one parameter from the equation that remains meaningful and one omitted mechanism that becomes important. Explain how the design review would change if that mechanism is plausible. Record any consequence whose acceptability must be judged by a competent safety professional rather than inferred from a classroom equation.

## 4. Practical investigation — What could reverse the decision?

Identify the single uncertain parameter most likely to change the preferred alternative. Design a low-risk test that would measure it and record what evidence would justify changing the recommendation.

**Studio assignment.** Build two cost scenarios for a pump drive, including maintenance and sensitivity to operating hours.

**Required confirmation.** Procurement assumption register, energy meter plan and a documented currency/date basis.

Build a reproducible notebook for this assignment. Include a sketch or diagram, table of known quantities with units, a physical basis for each relationship, and a separate list of facts that are merely assumed. Perform the calculation with independent arithmetic. If testing is proposed, explain where the sensors go and how their calibration and resolution affect the result. State what data would falsify the current design hypothesis; do not propose only measurements that could support it. Keep original data rather than overwriting it when outliers or transcription errors are discovered.

For this particular case, apply the following broader check: Write explicit hard constraints and evaluate them before comparing objective values. Use a common functional unit across alternatives. When uncertainty is large, quantify how a small adjustment in an estimated input alters the selected option. This guards against optimizing one metric while overlooking a coupled physical constraint. Report a design alternative in which the selected performance improves while some other important objective worsens. That alternative may still be appropriate, but the trade must be transparent and tied to stakeholder priorities. Before deciding, check whether the new configuration requires another supplier capability study, additional inspection or a revised safety analysis.

## 5. Exercises: calculation, design and criticism

1. **Definitions:** Explain **lifecycle cost and responsible sourcing** to a technician who knows the equipment but has not studied the model. State the measurable event, required operating condition and one assumption that cannot be read directly from the output.
2. **Hand calculation:** Reproduce the worked case and its governing rule `LCC = CapEx + PV(Energy + Maintenance + Replacement − Salvage)` with all units and significant figures justified. Change one input by +10% and determine whether the direction of change is physically plausible.
3. **Boundary case:** Analyze the specific limitation: A deterministic NPV obscures uncertainty in energy cost, actual load fraction and equipment lifetime. Supplier promises are not field data. Explain which additional calculation, test or design constraint is required and why a single generic safety factor cannot solve the missing-physics problem.
4. **Alternative:** Build two cost scenarios for a pump drive, including maintenance and sensitivity to operating hours. Propose a second feasible mechanism or component, not merely a different numerical setting of the original choice. Evaluate manufacturing and maintenance implications.
5. **Evidence:** Procurement assumption register, energy meter plan and a documented currency/date basis. Prepare a small table of what would be measured, which instrument would be used, what uncertainty could dominate and whether the result would verify a requirement or validate intended use.

**Instructor checkpoint A.** An answer that repeats the formula without identifying the operational boundary is incomplete. The student's result must have consistent units and a clear physical sign. If the output is expressed as a ratio or probability, explain its numerical range and whether independence assumptions apply. If an optimization is involved, a design that violates a hard constraint is rejected even if its objective is lower.

**Instructor checkpoint B.** Students should distinguish a calculated output from physical evidence. Strong submissions show an independent check, a sensitivity comparison, a plausible counterexample and an actionable test plan. A poor submission uses extra decimal places, repeated simulations, or an appealing chart to imply accuracy that the inputs do not support. A recommendation is not complete without a limitation and a named action to reduce the largest consequential uncertainty.

## 6. Integration with other mechanical disciplines

The design decision in **lifecycle cost and responsible sourcing** is related to **dynamics, control and mechatronic integration**. Moving mechanisms must satisfy kinematics, force and torque limits, transient control behavior and safety response. Sensor filtering introduces phase delay; actuator limits break linear assumptions. The selected mechanical transmission affects control bandwidth, heat and serviceability, so integration must be concurrent. Think about what information must pass between those two engineering teams and whether the transfer occurs as a load case, geometric tolerance, material property, signal, cost scenario or acceptance test. An interface that lacks an owner may survive several design reviews without being checked. In a final integration meeting, require each assumption to have an identified source and a planned verification activity; record deviations explicitly.

**Engineering notebook output:** One independent arithmetic check, one alternative architecture, one requirement-to-evidence row, one uncertainty statement, and one open risk item to carry into the unit capstone.


---

