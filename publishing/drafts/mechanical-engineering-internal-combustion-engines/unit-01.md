# Unit 01: Engine Architecture, Geometry and Operating Measures

**Course Code**: ICE 201 · **Level**: Advanced Undergraduate Engineering

## Unit Overview & Physical Foundations

This comprehensive university textbook unit covers the theoretical framework, physical modeling, mathematical governing equations, and engineering applications of **Engine Architecture, Geometry and Operating Measures**.

# Internal Combustion Engines — U01-L01


## U01-L01 — Two-stroke and four-stroke operating sequences

**Learning target.** At the end of this lesson, a reader should interpret the governing relation, reproduce a worked estimate, identify the limiting assumption and plan an independent verification of the engineering claim.

### 1. Physical question and context

Begin with the question of what can legitimately be inferred about **two-stroke and four-stroke operating sequences** from a few laboratory numbers. Cycle completion and gas-exchange timing are not interchangeable with cylinder count. The distinction between a physical quantity and a convenient proxy matters because an engine is simultaneously a chemical reactor, a flow machine, a heat exchanger and an oscillating mechanism. A simple classroom calculation is useful when it makes this distinction precise. It becomes dangerous to reasoning when its hidden assumptions are forgotten.

### 2. Governing calculation and its domain

The working relation used here is `cycles_per_min = rpm/2 (four-stroke) or rpm (two-stroke).`. Define every variable before substitution, keep a single system of units, and check whether its result should increase or decrease when an input changes. Ask which assumptions make the expression possible: steady conditions, a perfect gas, constant properties, a lumped state, negligible pressure loss or an ideal mechanical linkage may be necessary. If an assumption does not hold in the intended application, identify the direction of the expected deviation when physics permits. When that direction is not clear, do not guess; schedule a measurement or use a higher-fidelity calculation.

**Assumed numerical case:** At 3000 rpm a four-stroke cylinder has 1500 nominal working cycles per minute, whereas a two-stroke has 3000.

**Calculation walkthrough:** At 3000 rpm, the crank completes 3000 revolutions each minute. A four-stroke cycle requires two revolutions, hence 3000/2 = 1500 cycles per minute per cylinder. A two-stroke cycle requires one, hence 3000 cycles per minute. That ratio is purely kinematic; scavenging, friction, thermal loading and exhaust composition have not been evaluated.

The stated values form a hypothetical teaching example and should be recalculated by hand. First write the governing relation, then translate the inputs to SI, then perform substitution before rounding the displayed output. Check the sign and order of magnitude against a physical limiting case. Finally, ask which measured input would dominate an uncertainty interval. A large discrepancy from an independently computed check is grounds to revise the work, not to adjust the accepted answer without explanation.

### 3. Interpret the result, including failures

**Critical interpretation:** Scavenging losses and unburned fuel can make cycle-frequency comparisons misleading. A misleading numerical result can arise even when the arithmetic is perfect: the problem may be a wrong system boundary, an inappropriate reference property, a time-averaged signal used for a crank-angle event, or an unrecorded controller response. State which of those failure mechanisms is most likely here. Think about the change that would be observed in cylinder pressure, exhaust temperature, manifold state, or brake output if the explanatory mechanism were genuinely active rather than merely correlated with an unrelated change.

**Conservation audit:** Start by marking the system boundary on a sketch. Separate fuel energy entering the cylinder from indicated work on the piston and brake work at the shaft. A computed improvement that violates energy conservation is a mistake, not a new engine phenomenon. Where an experimental result seems to contradict the calculation, investigate calibration, hidden storage, auxiliary loads and the interpretation of reference conditions before adding complexity to the model. Applied to **two-stroke and four-stroke operating sequences**, this discipline helps decide whether the model is a prediction with independent evidence or merely a restatement of its input measurements. Write the most restrictive assumption in the margin of the calculation, then revise the interpretation if that assumption fails under the case-study operating conditions.

### 4. Measurement, uncertainty and experimental integrity

**Measurement and evidence plan:** Use crank-encoder and in-cylinder-pressure traces to identify compression and expansion landmarks. Before any data are collected, define a consistent sample clock, an equipment configuration record and at least one repeated baseline run. Identify how the instrument is calibrated and what its resolution excludes. Put all conversions in the analysis code rather than transcribing rounded values manually. Where the quantity is derived from several measurements, propagate uncertainty through the formula or use an appropriate perturbation study. A graph should show its reference conditions and measurement units. Unsupported interpolation between sparse engine-map points is not experimental evidence.

**Time dependence:** Engines operate through rapid events and slowly changing component states simultaneously. A crank-angle snapshot can describe the valve position but not warm-up; an averaged steady flow can describe laboratory demand but hide combustion variability. State the time scale to which each measured quantity belongs before comparing it with a model prediction. A careful research report can hold two ideas at once: the simplified result is internally correct and it is insufficient for system approval. This is not a weakness of mathematical modeling; it is the reason engineering uses progressive verification against measurements.

### 5. Engineering decision and integration

**Design implication:** Choose cycle type using emissions, lubrication, efficiency and operating envelope together. This lesson addresses only one component of the unit's problem: A four-cylinder laboratory engine must meet a torque requirement without exceeding a piston-speed or durability limit. Changes that look beneficial locally can increase pumping loss, friction, catalyst warm-up time, thermal stress or control complexity elsewhere. Accordingly, the correct engineering decision requires a second comparison at an off-design state and a list of constraints that cannot be traded away. The next simulation or experiment should be chosen to resolve the most consequential unknown, not simply to make the improvement look larger.

A useful extension is to reverse the calculation: choose an output target, estimate the input it would require and then test whether the implied operating point satisfies the engine's load, temperature, fuel and emissions constraints. Reverse calculations frequently uncover impossible combinations that are obscured by forward examples. Record the result as a conditional design feasibility statement, not a claim of guaranteed machine performance.

### 6. Practice and assessment

1. **Conceptual:** Explain why the relation `cycles_per_min = rpm/2 (four-stroke) or rpm (two-stroke).` is meaningful for this lesson. Name two necessary assumptions and a physical regime in which one fails.
2. **Calculation:** Reproduce and verify the worked case: At 3000 rpm a four-stroke cylinder has 1500 nominal working cycles per minute, whereas a two-stroke has 3000. Show units at every intermediate stage and carry at least one input uncertainty through the output.
3. **Diagnostic:** A team reports a performance improvement after changing one input. Construct an alternative explanation using a measurement error, thermal shift or controller response. What single observation would discriminate between them?
4. **Design:** In the case “A four-cylinder laboratory engine must meet a torque requirement without exceeding a piston-speed or durability limit.”, propose one legitimate design change and one nonnegotiable constraint. Choose cycle type using emissions, lubrication, efficiency and operating envelope together.
5. **Research practice:** Give a file naming and metadata convention that would allow another student to reproduce the analysis, including configuration, units and calibration state.

**Worked-answer checking guide.** For question 2, the reference result is described in the assumed numerical case; a correct submission must also specify the formula, the explicit units and the idealizations. For question 3, credit is earned for a falsifiable alternative mechanism and a measurement that can separate it from the original claim. For question 4, a design that ignores the nonnegotiable constraint is rejected even if its calculated objective improves.

**Further investigation.** Repeat the reasoning at two additional operating points: lower speed and higher intake temperature, or cold start and warmed-up operation where relevant. Describe why the same input perturbation might have a different result under those conditions. Decide which hypothesis can be evaluated safely using the offline numerical model and which requires qualified laboratory equipment.



---

# Internal Combustion Engines — U01-L02


## U01-L02 — Bore, stroke, displacement and chamber volume

**Learning target.** At the end of this lesson, a reader should interpret the governing relation, reproduce a worked estimate, identify the limiting assumption and plan an independent verification of the engineering claim.

### 1. Physical question and context

Consider an engineer who is evaluating **bore, stroke, displacement and chamber volume** in the following setting: A four-cylinder laboratory engine must meet a torque requirement without exceeding a piston-speed or durability limit. The analytical priority is not to maximize the number of equations. It is to identify the correct conserved quantity, select a boundary and state the outcome that the instrument or simulation actually reports. Geometry maps a moving piston into a displaced volume, but not directly into combustion efficiency. Two measurements that share a unit may still refer to different control volumes, time windows or reference states.

### 2. Governing calculation and its domain

The smallest useful model is `V_d = (pi/4) * B^2 * S * n_c; all linear dimensions in meters.`. Write it first in symbols because symbols expose which quantities are inputs and which are derived. Conduct a dimensional check. For example, an energy rate must have dimensions of power, and a dimensionless efficiency must not quietly carry a pressure unit. Then inspect the limiting cases. A vanishing input, a zero flow or an impossible temperature ratio should trigger a validity warning rather than a numerically polished answer. The equation belongs to the assumptions stated with it, not to every engine.

**Assumed numerical case:** Four cylinders at bore 0.086 m and stroke 0.086 m displace approximately 2.0 L in total.

**Calculation walkthrough:** Convert the 86 mm dimensions to 0.086 m before cubing. One cylinder displaces (π/4)(0.086)²(0.086) = 0.0004996 m³. Multiplying by four cylinders yields 0.001998 m³, or 1.998 L. The bore and stroke are both rounded, so do not present the displacement as a precision metrology result.

The stated values form a hypothetical teaching example and should be recalculated by hand. First write the governing relation, then translate the inputs to SI, then perform substitution before rounding the displayed output. Check the sign and order of magnitude against a physical limiting case. Finally, ask which measured input would dominate an uncertainty interval. A large discrepancy from an independently computed check is grounds to revise the work, not to adjust the accepted answer without explanation.

### 3. Interpret the result, including failures

**Critical interpretation:** A catalog nominal displacement may be rounded and does not state the clearance volume. A misleading numerical result can arise even when the arithmetic is perfect: the problem may be a wrong system boundary, an inappropriate reference property, a time-averaged signal used for a crank-angle event, or an unrecorded controller response. State which of those failure mechanisms is most likely here. Think about the change that would be observed in cylinder pressure, exhaust temperature, manifold state, or brake output if the explanatory mechanism were genuinely active rather than merely correlated with an unrelated change.

**Scale and sensitivity:** Scaling a geometric or thermal parameter is not a free performance gain. With every scale change, ask which transport time, stress, temperature, pressure ratio or nondimensional group changes with it. If the underlying response is nonlinear, quote a local sensitivity around the stated operating point instead of applying a single proportional rule across an engine map. Applied to **bore, stroke, displacement and chamber volume**, this discipline helps decide whether the model is a prediction with independent evidence or merely a restatement of its input measurements. Write the most restrictive assumption in the margin of the calculation, then revise the interpretation if that assumption fails under the case-study operating conditions.

### 4. Measurement, uncertainty and experimental integrity

**Measurement and evidence plan:** Measure bore and stroke with calibrated gauges, then check the assembled volume independently. Before any data are collected, define a consistent sample clock, an equipment configuration record and at least one repeated baseline run. Identify how the instrument is calibrated and what its resolution excludes. Put all conversions in the analysis code rather than transcribing rounded values manually. Where the quantity is derived from several measurements, propagate uncertainty through the formula or use an appropriate perturbation study. A graph should show its reference conditions and measurement units. Unsupported interpolation between sparse engine-map points is not experimental evidence.

**Experimental identifiability:** A neat equation does not imply that each parameter can be determined from available measurements. Two unknown effects may create the same measured output, especially when only torque and speed are logged. Design an independent measurement that distinguishes the competing explanations; when this is impossible, report a bounded family of plausible parameter values rather than a falsely precise single answer. A careful research report can hold two ideas at once: the simplified result is internally correct and it is insufficient for system approval. This is not a weakness of mathematical modeling; it is the reason engineering uses progressive verification against measurements.

### 5. Engineering decision and integration

**Design implication:** Carry geometric measurement tolerances through the result rather than reporting fictitious precision. This lesson addresses only one component of the unit's problem: A four-cylinder laboratory engine must meet a torque requirement without exceeding a piston-speed or durability limit. Changes that look beneficial locally can increase pumping loss, friction, catalyst warm-up time, thermal stress or control complexity elsewhere. Accordingly, the correct engineering decision requires a second comparison at an off-design state and a list of constraints that cannot be traded away. The next simulation or experiment should be chosen to resolve the most consequential unknown, not simply to make the improvement look larger.

A useful extension is to reverse the calculation: choose an output target, estimate the input it would require and then test whether the implied operating point satisfies the engine's load, temperature, fuel and emissions constraints. Reverse calculations frequently uncover impossible combinations that are obscured by forward examples. Record the result as a conditional design feasibility statement, not a claim of guaranteed machine performance.

### 6. Practice and assessment

1. **Conceptual:** Explain why the relation `V_d = (pi/4) * B^2 * S * n_c; all linear dimensions in meters.` is meaningful for this lesson. Name two necessary assumptions and a physical regime in which one fails.
2. **Calculation:** Reproduce and verify the worked case: Four cylinders at bore 0.086 m and stroke 0.086 m displace approximately 2.0 L in total. Show units at every intermediate stage and carry at least one input uncertainty through the output.
3. **Diagnostic:** A team reports a performance improvement after changing one input. Construct an alternative explanation using a measurement error, thermal shift or controller response. What single observation would discriminate between them?
4. **Design:** In the case “A four-cylinder laboratory engine must meet a torque requirement without exceeding a piston-speed or durability limit.”, propose one legitimate design change and one nonnegotiable constraint. Carry geometric measurement tolerances through the result rather than reporting fictitious precision.
5. **Research practice:** Give a file naming and metadata convention that would allow another student to reproduce the analysis, including configuration, units and calibration state.

**Worked-answer checking guide.** For question 2, the reference result is described in the assumed numerical case; a correct submission must also specify the formula, the explicit units and the idealizations. For question 3, credit is earned for a falsifiable alternative mechanism and a measurement that can separate it from the original claim. For question 4, a design that ignores the nonnegotiable constraint is rejected even if its calculated objective improves.

**Further investigation.** Repeat the reasoning at two additional operating points: lower speed and higher intake temperature, or cold start and warmed-up operation where relevant. Describe why the same input perturbation might have a different result under those conditions. Decide which hypothesis can be evaluated safely using the offline numerical model and which requires qualified laboratory equipment.



---

# Internal Combustion Engines — U01-L03


## U01-L03 — Compression ratio and combustion chamber shape

**Learning target.** At the end of this lesson, a reader should interpret the governing relation, reproduce a worked estimate, identify the limiting assumption and plan an independent verification of the engineering claim.

### 1. Physical question and context

The central issue in **compression ratio and combustion chamber shape** is not memorizing a formula but knowing when its use is justified. The geometric compression ratio is defined by swept and clearance volumes, not by boost pressure. A model's apparent precision depends on measurement resolution, parameter provenance and the operating envelope. At the outset specify whether a statement refers to a single cylinder, all cylinders, indicated work, brake shaft work, intake flow or exhaust flow. Changing that definition silently can invalidate a numerical answer while leaving its arithmetic flawless.

### 2. Governing calculation and its domain

Use `r_c = (V_d+V_c)/V_c for a single cylinder.` as the initial closure relation. It is tempting to interpret the number as a design guarantee; instead define a reference operating point, perturb each independent input separately and observe the output response. Check whether apparently independent variables are actually correlated by conservation or control logic. Treat a high-sensitivity variable as a candidate for better measurement. If the result requires a parameter measured by the same output that is being predicted, the model is partly circular and its validation requires an independent observation.

**Assumed numerical case:** A 500 cm3 swept volume and 50 cm3 clearance volume give a compression ratio of 11.0.

**Calculation walkthrough:** The compression ratio numerator is swept volume plus clearance volume: 500 + 50 = 550 cm³. Divide by 50 cm³ and obtain 11.0. The units cancel, giving a dimensionless ratio. An 11:1 geometric ratio should not be substituted for the manifold pressure ratio or for the actual trapped compression after valve closing.

The stated values form a hypothetical teaching example and should be recalculated by hand. First write the governing relation, then translate the inputs to SI, then perform substitution before rounding the displayed output. Check the sign and order of magnitude against a physical limiting case. Finally, ask which measured input would dominate an uncertainty interval. A large discrepancy from an independently computed check is grounds to revise the work, not to adjust the accepted answer without explanation.

### 3. Interpret the result, including failures

**Critical interpretation:** Dynamic compression and effective trapped compression differ when valves close after bottom dead center. A misleading numerical result can arise even when the arithmetic is perfect: the problem may be a wrong system boundary, an inappropriate reference property, a time-averaged signal used for a crank-angle event, or an unrecorded controller response. State which of those failure mechanisms is most likely here. Think about the change that would be observed in cylinder pressure, exhaust temperature, manifold state, or brake output if the explanatory mechanism were genuinely active rather than merely correlated with an unrelated change.

**Time dependence:** Engines operate through rapid events and slowly changing component states simultaneously. A crank-angle snapshot can describe the valve position but not warm-up; an averaged steady flow can describe laboratory demand but hide combustion variability. State the time scale to which each measured quantity belongs before comparing it with a model prediction. Applied to **compression ratio and combustion chamber shape**, this discipline helps decide whether the model is a prediction with independent evidence or merely a restatement of its input measurements. Write the most restrictive assumption in the margin of the calculation, then revise the interpretation if that assumption fails under the case-study operating conditions.

### 4. Measurement, uncertainty and experimental integrity

**Measurement and evidence plan:** Measure clearance using an appropriate calibrated method and report its uncertainty. Before any data are collected, define a consistent sample clock, an equipment configuration record and at least one repeated baseline run. Identify how the instrument is calibrated and what its resolution excludes. Put all conversions in the analysis code rather than transcribing rounded values manually. Where the quantity is derived from several measurements, propagate uncertainty through the formula or use an appropriate perturbation study. A graph should show its reference conditions and measurement units. Unsupported interpolation between sparse engine-map points is not experimental evidence.

**Operating-envelope reasoning:** Any model can look successful at its calibration point. The meaningful question is whether its error stays acceptably small at cold start, hot idle, high load, low ambient pressure, and during rapid change. Define this intended envelope explicitly, keep data from some points for validation, and reject extrapolation outside known physical or measurement limits. A careful research report can hold two ideas at once: the simplified result is internally correct and it is insufficient for system approval. This is not a weakness of mathematical modeling; it is the reason engineering uses progressive verification against measurements.

### 5. Engineering decision and integration

**Design implication:** Compare geometrical compression only after accounting for combustion-chamber shape and knock limits. This lesson addresses only one component of the unit's problem: A four-cylinder laboratory engine must meet a torque requirement without exceeding a piston-speed or durability limit. Changes that look beneficial locally can increase pumping loss, friction, catalyst warm-up time, thermal stress or control complexity elsewhere. Accordingly, the correct engineering decision requires a second comparison at an off-design state and a list of constraints that cannot be traded away. The next simulation or experiment should be chosen to resolve the most consequential unknown, not simply to make the improvement look larger.

A useful extension is to reverse the calculation: choose an output target, estimate the input it would require and then test whether the implied operating point satisfies the engine's load, temperature, fuel and emissions constraints. Reverse calculations frequently uncover impossible combinations that are obscured by forward examples. Record the result as a conditional design feasibility statement, not a claim of guaranteed machine performance.

### 6. Practice and assessment

1. **Conceptual:** Explain why the relation `r_c = (V_d+V_c)/V_c for a single cylinder.` is meaningful for this lesson. Name two necessary assumptions and a physical regime in which one fails.
2. **Calculation:** Reproduce and verify the worked case: A 500 cm3 swept volume and 50 cm3 clearance volume give a compression ratio of 11.0. Show units at every intermediate stage and carry at least one input uncertainty through the output.
3. **Diagnostic:** A team reports a performance improvement after changing one input. Construct an alternative explanation using a measurement error, thermal shift or controller response. What single observation would discriminate between them?
4. **Design:** In the case “A four-cylinder laboratory engine must meet a torque requirement without exceeding a piston-speed or durability limit.”, propose one legitimate design change and one nonnegotiable constraint. Compare geometrical compression only after accounting for combustion-chamber shape and knock limits.
5. **Research practice:** Give a file naming and metadata convention that would allow another student to reproduce the analysis, including configuration, units and calibration state.

**Worked-answer checking guide.** For question 2, the reference result is described in the assumed numerical case; a correct submission must also specify the formula, the explicit units and the idealizations. For question 3, credit is earned for a falsifiable alternative mechanism and a measurement that can separate it from the original claim. For question 4, a design that ignores the nonnegotiable constraint is rejected even if its calculated objective improves.

**Further investigation.** Repeat the reasoning at two additional operating points: lower speed and higher intake temperature, or cold start and warmed-up operation where relevant. Describe why the same input perturbation might have a different result under those conditions. Decide which hypothesis can be evaluated safely using the offline numerical model and which requires qualified laboratory equipment.



---

# Internal Combustion Engines — U01-L04


## U01-L04 — Crankshaft kinematics and piston speed

**Learning target.** At the end of this lesson, a reader should interpret the governing relation, reproduce a worked estimate, identify the limiting assumption and plan an independent verification of the engineering claim.

### 1. Physical question and context

A defensible treatment of **crankshaft kinematics and piston speed** begins by separating observable behavior from explanatory mechanism. Crank geometry produces nonuniform instantaneous piston velocity even under constant crank rpm. In an internal combustion engine this distinction is especially important because the same output can be produced by changes in fueling, volumetric efficiency, combustion phase, wall heat transfer or mechanical loss. The lesson therefore treats a compact formula as a hypothesis to be tested, not as an exact engine description.

### 2. Governing calculation and its domain

The working relation used here is `U_mean = 2*S*N/60; N in revolutions per minute, S in meters.`. Define every variable before substitution, keep a single system of units, and check whether its result should increase or decrease when an input changes. Ask which assumptions make the expression possible: steady conditions, a perfect gas, constant properties, a lumped state, negligible pressure loss or an ideal mechanical linkage may be necessary. If an assumption does not hold in the intended application, identify the direction of the expected deviation when physics permits. When that direction is not clear, do not guess; schedule a measurement or use a higher-fidelity calculation.

**Assumed numerical case:** At 6000 rpm and stroke 0.09 m, mean piston speed is 18 m/s.

**Calculation walkthrough:** The piston traverses one stroke upward and one stroke downward per crank revolution. Its total path per revolution is therefore 2(0.09) = 0.18 m. At 6000 rpm, 0.18×6000/60 = 18 m/s mean piston speed. This does not claim that the instantaneous speed is constant over any crank revolution.

The stated values form a hypothetical teaching example and should be recalculated by hand. First write the governing relation, then translate the inputs to SI, then perform substitution before rounding the displayed output. Check the sign and order of magnitude against a physical limiting case. Finally, ask which measured input would dominate an uncertainty interval. A large discrepancy from an independently computed check is grounds to revise the work, not to adjust the accepted answer without explanation.

### 3. Interpret the result, including failures

**Critical interpretation:** Mean speed is not peak speed or ring sliding speed at every crank angle. A misleading numerical result can arise even when the arithmetic is perfect: the problem may be a wrong system boundary, an inappropriate reference property, a time-averaged signal used for a crank-angle event, or an unrecorded controller response. State which of those failure mechanisms is most likely here. Think about the change that would be observed in cylinder pressure, exhaust temperature, manifold state, or brake output if the explanatory mechanism were genuinely active rather than merely correlated with an unrelated change.

**Experimental identifiability:** A neat equation does not imply that each parameter can be determined from available measurements. Two unknown effects may create the same measured output, especially when only torque and speed are logged. Design an independent measurement that distinguishes the competing explanations; when this is impossible, report a bounded family of plausible parameter values rather than a falsely precise single answer. Applied to **crankshaft kinematics and piston speed**, this discipline helps decide whether the model is a prediction with independent evidence or merely a restatement of its input measurements. Write the most restrictive assumption in the margin of the calculation, then revise the interpretation if that assumption fails under the case-study operating conditions.

### 4. Measurement, uncertainty and experimental integrity

**Measurement and evidence plan:** Record crank speed and geometry; use a slider-crank model for instantaneous piston travel. Before any data are collected, define a consistent sample clock, an equipment configuration record and at least one repeated baseline run. Identify how the instrument is calibrated and what its resolution excludes. Put all conversions in the analysis code rather than transcribing rounded values manually. Where the quantity is derived from several measurements, propagate uncertainty through the formula or use an appropriate perturbation study. A graph should show its reference conditions and measurement units. Unsupported interpolation between sparse engine-map points is not experimental evidence.

**Conservation audit:** Start by marking the system boundary on a sketch. Separate fuel energy entering the cylinder from indicated work on the piston and brake work at the shaft. A computed improvement that violates energy conservation is a mistake, not a new engine phenomenon. Where an experimental result seems to contradict the calculation, investigate calibration, hidden storage, auxiliary loads and the interpretation of reference conditions before adding complexity to the model. A careful research report can hold two ideas at once: the simplified result is internally correct and it is insufficient for system approval. This is not a weakness of mathematical modeling; it is the reason engineering uses progressive verification against measurements.

### 5. Engineering decision and integration

**Design implication:** Do not certify bearing or ring loads from mean piston speed alone. This lesson addresses only one component of the unit's problem: A four-cylinder laboratory engine must meet a torque requirement without exceeding a piston-speed or durability limit. Changes that look beneficial locally can increase pumping loss, friction, catalyst warm-up time, thermal stress or control complexity elsewhere. Accordingly, the correct engineering decision requires a second comparison at an off-design state and a list of constraints that cannot be traded away. The next simulation or experiment should be chosen to resolve the most consequential unknown, not simply to make the improvement look larger.

A useful extension is to reverse the calculation: choose an output target, estimate the input it would require and then test whether the implied operating point satisfies the engine's load, temperature, fuel and emissions constraints. Reverse calculations frequently uncover impossible combinations that are obscured by forward examples. Record the result as a conditional design feasibility statement, not a claim of guaranteed machine performance.

### 6. Practice and assessment

1. **Conceptual:** Explain why the relation `U_mean = 2*S*N/60; N in revolutions per minute, S in meters.` is meaningful for this lesson. Name two necessary assumptions and a physical regime in which one fails.
2. **Calculation:** Reproduce and verify the worked case: At 6000 rpm and stroke 0.09 m, mean piston speed is 18 m/s. Show units at every intermediate stage and carry at least one input uncertainty through the output.
3. **Diagnostic:** A team reports a performance improvement after changing one input. Construct an alternative explanation using a measurement error, thermal shift or controller response. What single observation would discriminate between them?
4. **Design:** In the case “A four-cylinder laboratory engine must meet a torque requirement without exceeding a piston-speed or durability limit.”, propose one legitimate design change and one nonnegotiable constraint. Do not certify bearing or ring loads from mean piston speed alone.
5. **Research practice:** Give a file naming and metadata convention that would allow another student to reproduce the analysis, including configuration, units and calibration state.

**Worked-answer checking guide.** For question 2, the reference result is described in the assumed numerical case; a correct submission must also specify the formula, the explicit units and the idealizations. For question 3, credit is earned for a falsifiable alternative mechanism and a measurement that can separate it from the original claim. For question 4, a design that ignores the nonnegotiable constraint is rejected even if its calculated objective improves.

**Further investigation.** Repeat the reasoning at two additional operating points: lower speed and higher intake temperature, or cold start and warmed-up operation where relevant. Describe why the same input perturbation might have a different result under those conditions. Decide which hypothesis can be evaluated safely using the offline numerical model and which requires qualified laboratory equipment.



---

# Internal Combustion Engines — U01-L05


## U01-L05 — Torque, power and normalized engine maps

**Learning target.** At the end of this lesson, a reader should interpret the governing relation, reproduce a worked estimate, identify the limiting assumption and plan an independent verification of the engineering claim.

### 1. Physical question and context

Begin with the question of what can legitimately be inferred about **torque, power and normalized engine maps** from a few laboratory numbers. Brake torque is a moment; shaft power incorporates angular speed and is reduced by losses. The distinction between a physical quantity and a convenient proxy matters because an engine is simultaneously a chemical reactor, a flow machine, a heat exchanger and an oscillating mechanism. A simple classroom calculation is useful when it makes this distinction precise. It becomes dangerous to reasoning when its hidden assumptions are forgotten.

### 2. Governing calculation and its domain

The smallest useful model is `P_b = 2*pi*(N/60)*T; convert W to kW by dividing 1000.`. Write it first in symbols because symbols expose which quantities are inputs and which are derived. Conduct a dimensional check. For example, an energy rate must have dimensions of power, and a dimensionless efficiency must not quietly carry a pressure unit. Then inspect the limiting cases. A vanishing input, a zero flow or an impossible temperature ratio should trigger a validity warning rather than a numerically polished answer. The equation belongs to the assumptions stated with it, not to every engine.

**Assumed numerical case:** A shaft producing 200 N m at 3000 rpm delivers about 62.8 kW.

**Calculation walkthrough:** Convert 3000 rpm to 50 revolutions per second. The shaft angular velocity is 2π×50 = 314.159 rad/s. Multiply by measured torque 200 N·m to get 62,831.9 W or 62.83 kW. At a different speed, identical torque produces different shaft power; this is why a dynamometer map needs both axes.

The stated values form a hypothetical teaching example and should be recalculated by hand. First write the governing relation, then translate the inputs to SI, then perform substitution before rounding the displayed output. Check the sign and order of magnitude against a physical limiting case. Finally, ask which measured input would dominate an uncertainty interval. A large discrepancy from an independently computed check is grounds to revise the work, not to adjust the accepted answer without explanation.

### 3. Interpret the result, including failures

**Critical interpretation:** A single peak power figure omits fuel consumption, thermal limits and speed range. A misleading numerical result can arise even when the arithmetic is perfect: the problem may be a wrong system boundary, an inappropriate reference property, a time-averaged signal used for a crank-angle event, or an unrecorded controller response. State which of those failure mechanisms is most likely here. Think about the change that would be observed in cylinder pressure, exhaust temperature, manifold state, or brake output if the explanatory mechanism were genuinely active rather than merely correlated with an unrelated change.

**Operating-envelope reasoning:** Any model can look successful at its calibration point. The meaningful question is whether its error stays acceptably small at cold start, hot idle, high load, low ambient pressure, and during rapid change. Define this intended envelope explicitly, keep data from some points for validation, and reject extrapolation outside known physical or measurement limits. Applied to **torque, power and normalized engine maps**, this discipline helps decide whether the model is a prediction with independent evidence or merely a restatement of its input measurements. Write the most restrictive assumption in the margin of the calculation, then revise the interpretation if that assumption fails under the case-study operating conditions.

### 4. Measurement, uncertainty and experimental integrity

**Measurement and evidence plan:** Use a calibrated dynamometer to measure torque while independently logging speed. Before any data are collected, define a consistent sample clock, an equipment configuration record and at least one repeated baseline run. Identify how the instrument is calibrated and what its resolution excludes. Put all conversions in the analysis code rather than transcribing rounded values manually. Where the quantity is derived from several measurements, propagate uncertainty through the formula or use an appropriate perturbation study. A graph should show its reference conditions and measurement units. Unsupported interpolation between sparse engine-map points is not experimental evidence.

**Scale and sensitivity:** Scaling a geometric or thermal parameter is not a free performance gain. With every scale change, ask which transport time, stress, temperature, pressure ratio or nondimensional group changes with it. If the underlying response is nonlinear, quote a local sensitivity around the stated operating point instead of applying a single proportional rule across an engine map. A careful research report can hold two ideas at once: the simplified result is internally correct and it is insufficient for system approval. This is not a weakness of mathematical modeling; it is the reason engineering uses progressive verification against measurements.

### 5. Engineering decision and integration

**Design implication:** Publish operating-point maps and uncertainty rather than a single marketing headline. This lesson addresses only one component of the unit's problem: A four-cylinder laboratory engine must meet a torque requirement without exceeding a piston-speed or durability limit. Changes that look beneficial locally can increase pumping loss, friction, catalyst warm-up time, thermal stress or control complexity elsewhere. Accordingly, the correct engineering decision requires a second comparison at an off-design state and a list of constraints that cannot be traded away. The next simulation or experiment should be chosen to resolve the most consequential unknown, not simply to make the improvement look larger.

A useful extension is to reverse the calculation: choose an output target, estimate the input it would require and then test whether the implied operating point satisfies the engine's load, temperature, fuel and emissions constraints. Reverse calculations frequently uncover impossible combinations that are obscured by forward examples. Record the result as a conditional design feasibility statement, not a claim of guaranteed machine performance.

### 6. Practice and assessment

1. **Conceptual:** Explain why the relation `P_b = 2*pi*(N/60)*T; convert W to kW by dividing 1000.` is meaningful for this lesson. Name two necessary assumptions and a physical regime in which one fails.
2. **Calculation:** Reproduce and verify the worked case: A shaft producing 200 N m at 3000 rpm delivers about 62.8 kW. Show units at every intermediate stage and carry at least one input uncertainty through the output.
3. **Diagnostic:** A team reports a performance improvement after changing one input. Construct an alternative explanation using a measurement error, thermal shift or controller response. What single observation would discriminate between them?
4. **Design:** In the case “A four-cylinder laboratory engine must meet a torque requirement without exceeding a piston-speed or durability limit.”, propose one legitimate design change and one nonnegotiable constraint. Publish operating-point maps and uncertainty rather than a single marketing headline.
5. **Research practice:** Give a file naming and metadata convention that would allow another student to reproduce the analysis, including configuration, units and calibration state.

**Worked-answer checking guide.** For question 2, the reference result is described in the assumed numerical case; a correct submission must also specify the formula, the explicit units and the idealizations. For question 3, credit is earned for a falsifiable alternative mechanism and a measurement that can separate it from the original claim. For question 4, a design that ignores the nonnegotiable constraint is rejected even if its calculated objective improves.

**Further investigation.** Repeat the reasoning at two additional operating points: lower speed and higher intake temperature, or cold start and warmed-up operation where relevant. Describe why the same input perturbation might have a different result under those conditions. Decide which hypothesis can be evaluated safely using the offline numerical model and which requires qualified laboratory equipment.



---

