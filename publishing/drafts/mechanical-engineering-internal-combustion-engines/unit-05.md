# Unit 05: Fuel Systems, Engine Controls and Transients

**Course Code**: ICE 205 · **Level**: Advanced Undergraduate Engineering

## Unit Overview & Physical Foundations

This comprehensive university textbook unit covers the theoretical framework, physical modeling, mathematical governing equations, and engineering applications of **Fuel Systems, Engine Controls and Transients**.

# Internal Combustion Engines — U05-L01


## U05-L01 — Port injection and direct injection tradeoffs

**Learning target.** At the end of this lesson, a reader should interpret the governing relation, reproduce a worked estimate, identify the limiting assumption and plan an independent verification of the engineering claim.

### 1. Physical question and context

Begin with the question of what can legitimately be inferred about **port injection and direct injection tradeoffs** from a few laboratory numbers. Injection location changes mixture preparation, wall wetting, evaporation time and particulate formation pathways. The distinction between a physical quantity and a convenient proxy matters because an engine is simultaneously a chemical reactor, a flow machine, a heat exchanger and an oscillating mechanism. A simple classroom calculation is useful when it makes this distinction precise. It becomes dangerous to reasoning when its hidden assumptions are forgotten.

### 2. Governing calculation and its domain

Use `Fuel required per cycle = trapped_air_mass / commanded_AFR on a consistent mass basis.` as the initial closure relation. It is tempting to interpret the number as a design guarantee; instead define a reference operating point, perturb each independent input separately and observe the output response. Check whether apparently independent variables are actually correlated by conservation or control logic. Treat a high-sensitivity variable as a candidate for better measurement. If the result requires a parameter measured by the same output that is being predicted, the model is partly circular and its validation requires an independent observation.

**Assumed numerical case:** With 0.0005 kg air per cycle and AFR=14.7, fuel target is about 34 mg per cycle.

**Calculation walkthrough:** At 0.0005 kg trapped air per induction event and commanded mass AFR 14.7, divide 0.0005/14.7 = 3.401×10⁻⁵ kg fuel. This equals 34.0 mg. For injection duration, additional injector flow calibration and dead-time compensation are required; the mass calculation by itself does not give a pulse width.

The stated values form a hypothetical teaching example and should be recalculated by hand. First write the governing relation, then translate the inputs to SI, then perform substitution before rounding the displayed output. Check the sign and order of magnitude against a physical limiting case. Finally, ask which measured input would dominate an uncertainty interval. A large discrepancy from an independently computed check is grounds to revise the work, not to adjust the accepted answer without explanation.

### 3. Interpret the result, including failures

**Critical interpretation:** Commanded pulse width does not equal delivered mass at all injector pressures or voltages. A misleading numerical result can arise even when the arithmetic is perfect: the problem may be a wrong system boundary, an inappropriate reference property, a time-averaged signal used for a crank-angle event, or an unrecorded controller response. State which of those failure mechanisms is most likely here. Think about the change that would be observed in cylinder pressure, exhaust temperature, manifold state, or brake output if the explanatory mechanism were genuinely active rather than merely correlated with an unrelated change.

**Conservation audit:** Start by marking the system boundary on a sketch. Separate fuel energy entering the cylinder from indicated work on the piston and brake work at the shaft. A computed improvement that violates energy conservation is a mistake, not a new engine phenomenon. Where an experimental result seems to contradict the calculation, investigate calibration, hidden storage, auxiliary loads and the interpretation of reference conditions before adding complexity to the model. Applied to **port injection and direct injection tradeoffs**, this discipline helps decide whether the model is a prediction with independent evidence or merely a restatement of its input measurements. Write the most restrictive assumption in the margin of the calculation, then revise the interpretation if that assumption fails under the case-study operating conditions.

### 4. Measurement, uncertainty and experimental integrity

**Measurement and evidence plan:** Measure injectors on a bench and reconcile accumulated fuel consumption. Before any data are collected, define a consistent sample clock, an equipment configuration record and at least one repeated baseline run. Identify how the instrument is calibrated and what its resolution excludes. Put all conversions in the analysis code rather than transcribing rounded values manually. Where the quantity is derived from several measurements, propagate uncertainty through the formula or use an appropriate perturbation study. A graph should show its reference conditions and measurement units. Unsupported interpolation between sparse engine-map points is not experimental evidence.

**Time dependence:** Engines operate through rapid events and slowly changing component states simultaneously. A crank-angle snapshot can describe the valve position but not warm-up; an averaged steady flow can describe laboratory demand but hide combustion variability. State the time scale to which each measured quantity belongs before comparing it with a model prediction. A careful research report can hold two ideas at once: the simplified result is internally correct and it is insufficient for system approval. This is not a weakness of mathematical modeling; it is the reason engineering uses progressive verification against measurements.

### 5. Engineering decision and integration

**Design implication:** Specify spray, wall impingement and deposit risks before committing to an architecture. This lesson addresses only one component of the unit's problem: An engine controller must deliver changing torque with stable combustion and bounded exhaust temperatures. Changes that look beneficial locally can increase pumping loss, friction, catalyst warm-up time, thermal stress or control complexity elsewhere. Accordingly, the correct engineering decision requires a second comparison at an off-design state and a list of constraints that cannot be traded away. The next simulation or experiment should be chosen to resolve the most consequential unknown, not simply to make the improvement look larger.

A useful extension is to reverse the calculation: choose an output target, estimate the input it would require and then test whether the implied operating point satisfies the engine's load, temperature, fuel and emissions constraints. Reverse calculations frequently uncover impossible combinations that are obscured by forward examples. Record the result as a conditional design feasibility statement, not a claim of guaranteed machine performance.

### 6. Practice and assessment

1. **Conceptual:** Explain why the relation `Fuel required per cycle = trapped_air_mass / commanded_AFR on a consistent mass basis.` is meaningful for this lesson. Name two necessary assumptions and a physical regime in which one fails.
2. **Calculation:** Reproduce and verify the worked case: With 0.0005 kg air per cycle and AFR=14.7, fuel target is about 34 mg per cycle. Show units at every intermediate stage and carry at least one input uncertainty through the output.
3. **Diagnostic:** A team reports a performance improvement after changing one input. Construct an alternative explanation using a measurement error, thermal shift or controller response. What single observation would discriminate between them?
4. **Design:** In the case “An engine controller must deliver changing torque with stable combustion and bounded exhaust temperatures.”, propose one legitimate design change and one nonnegotiable constraint. Specify spray, wall impingement and deposit risks before committing to an architecture.
5. **Research practice:** Give a file naming and metadata convention that would allow another student to reproduce the analysis, including configuration, units and calibration state.

**Worked-answer checking guide.** For question 2, the reference result is described in the assumed numerical case; a correct submission must also specify the formula, the explicit units and the idealizations. For question 3, credit is earned for a falsifiable alternative mechanism and a measurement that can separate it from the original claim. For question 4, a design that ignores the nonnegotiable constraint is rejected even if its calculated objective improves.

**Further investigation.** Repeat the reasoning at two additional operating points: lower speed and higher intake temperature, or cold start and warmed-up operation where relevant. Describe why the same input perturbation might have a different result under those conditions. Decide which hypothesis can be evaluated safely using the offline numerical model and which requires qualified laboratory equipment.



---

# Internal Combustion Engines — U05-L02


## U05-L02 — Compression-ignition injection and mixing

**Learning target.** At the end of this lesson, a reader should interpret the governing relation, reproduce a worked estimate, identify the limiting assumption and plan an independent verification of the engineering claim.

### 1. Physical question and context

Consider an engineer who is evaluating **compression-ignition injection and mixing** in the following setting: An engine controller must deliver changing torque with stable combustion and bounded exhaust temperatures. The analytical priority is not to maximize the number of equations. It is to identify the correct conserved quantity, select a boundary and state the outcome that the instrument or simulation actually reports. Diesel-type combustion couples spray breakup, evaporation, entrainment and ignition rather than a premixed flame alone. Two measurements that share a unit may still refer to different control volumes, time windows or reference states.

### 2. Governing calculation and its domain

The working relation used here is `Injection quantity can be estimated from calibrated mass-flow rate integrated over the event.`. Define every variable before substitution, keep a single system of units, and check whether its result should increase or decrease when an input changes. Ask which assumptions make the expression possible: steady conditions, a perfect gas, constant properties, a lumped state, negligible pressure loss or an ideal mechanical linkage may be necessary. If an assumption does not hold in the intended application, identify the direction of the expected deviation when physics permits. When that direction is not clear, do not guess; schedule a measurement or use a higher-fidelity calculation.

**Assumed numerical case:** A hypothetical 10 mg/ms steady injection rate over 3 ms gives 30 mg, ignoring opening and closing transients.

**Calculation walkthrough:** At a hypothetical injector rate of 10 mg/ms, a rectangular 3 ms pulse would inject 30 mg. Real opening and closing transitions reduce the useful effective interval, and rail pressure changes flow. Instead of treating the rectangle as a ground-truth injection event, integrate a measured injector flow trace when practical.

The stated values form a hypothetical teaching example and should be recalculated by hand. First write the governing relation, then translate the inputs to SI, then perform substitution before rounding the displayed output. Check the sign and order of magnitude against a physical limiting case. Finally, ask which measured input would dominate an uncertainty interval. A large discrepancy from an independently computed check is grounds to revise the work, not to adjust the accepted answer without explanation.

### 3. Interpret the result, including failures

**Critical interpretation:** Multiple pulses and rail-pressure dynamics make square-pulse approximations unreliable. A misleading numerical result can arise even when the arithmetic is perfect: the problem may be a wrong system boundary, an inappropriate reference property, a time-averaged signal used for a crank-angle event, or an unrecorded controller response. State which of those failure mechanisms is most likely here. Think about the change that would be observed in cylinder pressure, exhaust temperature, manifold state, or brake output if the explanatory mechanism were genuinely active rather than merely correlated with an unrelated change.

**Scale and sensitivity:** Scaling a geometric or thermal parameter is not a free performance gain. With every scale change, ask which transport time, stress, temperature, pressure ratio or nondimensional group changes with it. If the underlying response is nonlinear, quote a local sensitivity around the stated operating point instead of applying a single proportional rule across an engine map. Applied to **compression-ignition injection and mixing**, this discipline helps decide whether the model is a prediction with independent evidence or merely a restatement of its input measurements. Write the most restrictive assumption in the margin of the calculation, then revise the interpretation if that assumption fails under the case-study operating conditions.

### 4. Measurement, uncertainty and experimental integrity

**Measurement and evidence plan:** Capture injector current, rail pressure and fuel balance while checking cylinder pressure. Before any data are collected, define a consistent sample clock, an equipment configuration record and at least one repeated baseline run. Identify how the instrument is calibrated and what its resolution excludes. Put all conversions in the analysis code rather than transcribing rounded values manually. Where the quantity is derived from several measurements, propagate uncertainty through the formula or use an appropriate perturbation study. A graph should show its reference conditions and measurement units. Unsupported interpolation between sparse engine-map points is not experimental evidence.

**Experimental identifiability:** A neat equation does not imply that each parameter can be determined from available measurements. Two unknown effects may create the same measured output, especially when only torque and speed are logged. Design an independent measurement that distinguishes the competing explanations; when this is impossible, report a bounded family of plausible parameter values rather than a falsely precise single answer. A careful research report can hold two ideas at once: the simplified result is internally correct and it is insufficient for system approval. This is not a weakness of mathematical modeling; it is the reason engineering uses progressive verification against measurements.

### 5. Engineering decision and integration

**Design implication:** Evaluate noise, soot and NOx tradeoffs across load rather than only peak torque. This lesson addresses only one component of the unit's problem: An engine controller must deliver changing torque with stable combustion and bounded exhaust temperatures. Changes that look beneficial locally can increase pumping loss, friction, catalyst warm-up time, thermal stress or control complexity elsewhere. Accordingly, the correct engineering decision requires a second comparison at an off-design state and a list of constraints that cannot be traded away. The next simulation or experiment should be chosen to resolve the most consequential unknown, not simply to make the improvement look larger.

A useful extension is to reverse the calculation: choose an output target, estimate the input it would require and then test whether the implied operating point satisfies the engine's load, temperature, fuel and emissions constraints. Reverse calculations frequently uncover impossible combinations that are obscured by forward examples. Record the result as a conditional design feasibility statement, not a claim of guaranteed machine performance.

### 6. Practice and assessment

1. **Conceptual:** Explain why the relation `Injection quantity can be estimated from calibrated mass-flow rate integrated over the event.` is meaningful for this lesson. Name two necessary assumptions and a physical regime in which one fails.
2. **Calculation:** Reproduce and verify the worked case: A hypothetical 10 mg/ms steady injection rate over 3 ms gives 30 mg, ignoring opening and closing transients. Show units at every intermediate stage and carry at least one input uncertainty through the output.
3. **Diagnostic:** A team reports a performance improvement after changing one input. Construct an alternative explanation using a measurement error, thermal shift or controller response. What single observation would discriminate between them?
4. **Design:** In the case “An engine controller must deliver changing torque with stable combustion and bounded exhaust temperatures.”, propose one legitimate design change and one nonnegotiable constraint. Evaluate noise, soot and NOx tradeoffs across load rather than only peak torque.
5. **Research practice:** Give a file naming and metadata convention that would allow another student to reproduce the analysis, including configuration, units and calibration state.

**Worked-answer checking guide.** For question 2, the reference result is described in the assumed numerical case; a correct submission must also specify the formula, the explicit units and the idealizations. For question 3, credit is earned for a falsifiable alternative mechanism and a measurement that can separate it from the original claim. For question 4, a design that ignores the nonnegotiable constraint is rejected even if its calculated objective improves.

**Further investigation.** Repeat the reasoning at two additional operating points: lower speed and higher intake temperature, or cold start and warmed-up operation where relevant. Describe why the same input perturbation might have a different result under those conditions. Decide which hypothesis can be evaluated safely using the offline numerical model and which requires qualified laboratory equipment.



---

# Internal Combustion Engines — U05-L03


## U05-L03 — Electronic throttle and torque request coordination

**Learning target.** At the end of this lesson, a reader should interpret the governing relation, reproduce a worked estimate, identify the limiting assumption and plan an independent verification of the engineering claim.

### 1. Physical question and context

The central issue in **electronic throttle and torque request coordination** is not memorizing a formula but knowing when its use is justified. Driver or supervisor demand should be translated into bounded torque rather than a direct open-loop actuator position. A model's apparent precision depends on measurement resolution, parameter provenance and the operating envelope. At the outset specify whether a statement refers to a single cylinder, all cylinders, indicated work, brake shaft work, intake flow or exhaust flow. Changing that definition silently can invalidate a numerical answer while leaving its arithmetic flawless.

### 2. Governing calculation and its domain

The smallest useful model is `Torque error e = T_requested - T_estimated, with limits supplied by subsystem constraints.`. Write it first in symbols because symbols expose which quantities are inputs and which are derived. Conduct a dimensional check. For example, an energy rate must have dimensions of power, and a dimensionless efficiency must not quietly carry a pressure unit. Then inspect the limiting cases. A vanishing input, a zero flow or an impossible temperature ratio should trigger a validity warning rather than a numerically polished answer. The equation belongs to the assumptions stated with it, not to every engine.

**Assumed numerical case:** If request is 220 N m and permitted limit is 180 N m, the delivered target must be bounded at 180 N m.

**Calculation walkthrough:** If estimated requested torque is 220 N·m and the calibrated thermal protection limit is 180 N·m, use min(220,180)=180 N·m as the bounded target. This arithmetic does not establish that the physical engine can deliver 180 N·m safely; other constraints may reduce the target further. The prioritization must be explicitly recorded in the controller design.

The stated values form a hypothetical teaching example and should be recalculated by hand. First write the governing relation, then translate the inputs to SI, then perform substitution before rounding the displayed output. Check the sign and order of magnitude against a physical limiting case. Finally, ask which measured input would dominate an uncertainty interval. A large discrepancy from an independently computed check is grounds to revise the work, not to adjust the accepted answer without explanation.

### 3. Interpret the result, including failures

**Critical interpretation:** Estimated torque may drift with fuel properties, ambient conditions and air-path dynamics. A misleading numerical result can arise even when the arithmetic is perfect: the problem may be a wrong system boundary, an inappropriate reference property, a time-averaged signal used for a crank-angle event, or an unrecorded controller response. State which of those failure mechanisms is most likely here. Think about the change that would be observed in cylinder pressure, exhaust temperature, manifold state, or brake output if the explanatory mechanism were genuinely active rather than merely correlated with an unrelated change.

**Time dependence:** Engines operate through rapid events and slowly changing component states simultaneously. A crank-angle snapshot can describe the valve position but not warm-up; an averaged steady flow can describe laboratory demand but hide combustion variability. State the time scale to which each measured quantity belongs before comparing it with a model prediction. Applied to **electronic throttle and torque request coordination**, this discipline helps decide whether the model is a prediction with independent evidence or merely a restatement of its input measurements. Write the most restrictive assumption in the margin of the calculation, then revise the interpretation if that assumption fails under the case-study operating conditions.

### 4. Measurement, uncertainty and experimental integrity

**Measurement and evidence plan:** Compare torque request, estimated torque and dynamometer measurement during ramp tests. Before any data are collected, define a consistent sample clock, an equipment configuration record and at least one repeated baseline run. Identify how the instrument is calibrated and what its resolution excludes. Put all conversions in the analysis code rather than transcribing rounded values manually. Where the quantity is derived from several measurements, propagate uncertainty through the formula or use an appropriate perturbation study. A graph should show its reference conditions and measurement units. Unsupported interpolation between sparse engine-map points is not experimental evidence.

**Operating-envelope reasoning:** Any model can look successful at its calibration point. The meaningful question is whether its error stays acceptably small at cold start, hot idle, high load, low ambient pressure, and during rapid change. Define this intended envelope explicitly, keep data from some points for validation, and reject extrapolation outside known physical or measurement limits. A careful research report can hold two ideas at once: the simplified result is internally correct and it is insufficient for system approval. This is not a weakness of mathematical modeling; it is the reason engineering uses progressive verification against measurements.

### 5. Engineering decision and integration

**Design implication:** Use explicit priority among driver demand, thermal protection, emissions and stability limits. This lesson addresses only one component of the unit's problem: An engine controller must deliver changing torque with stable combustion and bounded exhaust temperatures. Changes that look beneficial locally can increase pumping loss, friction, catalyst warm-up time, thermal stress or control complexity elsewhere. Accordingly, the correct engineering decision requires a second comparison at an off-design state and a list of constraints that cannot be traded away. The next simulation or experiment should be chosen to resolve the most consequential unknown, not simply to make the improvement look larger.

A useful extension is to reverse the calculation: choose an output target, estimate the input it would require and then test whether the implied operating point satisfies the engine's load, temperature, fuel and emissions constraints. Reverse calculations frequently uncover impossible combinations that are obscured by forward examples. Record the result as a conditional design feasibility statement, not a claim of guaranteed machine performance.

### 6. Practice and assessment

1. **Conceptual:** Explain why the relation `Torque error e = T_requested - T_estimated, with limits supplied by subsystem constraints.` is meaningful for this lesson. Name two necessary assumptions and a physical regime in which one fails.
2. **Calculation:** Reproduce and verify the worked case: If request is 220 N m and permitted limit is 180 N m, the delivered target must be bounded at 180 N m. Show units at every intermediate stage and carry at least one input uncertainty through the output.
3. **Diagnostic:** A team reports a performance improvement after changing one input. Construct an alternative explanation using a measurement error, thermal shift or controller response. What single observation would discriminate between them?
4. **Design:** In the case “An engine controller must deliver changing torque with stable combustion and bounded exhaust temperatures.”, propose one legitimate design change and one nonnegotiable constraint. Use explicit priority among driver demand, thermal protection, emissions and stability limits.
5. **Research practice:** Give a file naming and metadata convention that would allow another student to reproduce the analysis, including configuration, units and calibration state.

**Worked-answer checking guide.** For question 2, the reference result is described in the assumed numerical case; a correct submission must also specify the formula, the explicit units and the idealizations. For question 3, credit is earned for a falsifiable alternative mechanism and a measurement that can separate it from the original claim. For question 4, a design that ignores the nonnegotiable constraint is rejected even if its calculated objective improves.

**Further investigation.** Repeat the reasoning at two additional operating points: lower speed and higher intake temperature, or cold start and warmed-up operation where relevant. Describe why the same input perturbation might have a different result under those conditions. Decide which hypothesis can be evaluated safely using the offline numerical model and which requires qualified laboratory equipment.



---

# Internal Combustion Engines — U05-L04


## U05-L04 — Oxygen sensing and closed-loop mixture control

**Learning target.** At the end of this lesson, a reader should interpret the governing relation, reproduce a worked estimate, identify the limiting assumption and plan an independent verification of the engineering claim.

### 1. Physical question and context

A defensible treatment of **oxygen sensing and closed-loop mixture control** begins by separating observable behavior from explanatory mechanism. The sensed exhaust mixture represents transport delay, catalyst state and sensor dynamics, not instantaneous cylinder chemistry. In an internal combustion engine this distinction is especially important because the same output can be produced by changes in fueling, volumetric efficiency, combustion phase, wall heat transfer or mechanical loss. The lesson therefore treats a compact formula as a hypothesis to be tested, not as an exact engine description.

### 2. Governing calculation and its domain

Use `Simple integral controller u[k+1]=u[k]+K_i*(lambda_target-lambda_measured).` as the initial closure relation. It is tempting to interpret the number as a design guarantee; instead define a reference operating point, perturb each independent input separately and observe the output response. Check whether apparently independent variables are actually correlated by conservation or control logic. Treat a high-sensitivity variable as a candidate for better measurement. If the result requires a parameter measured by the same output that is being predicted, the model is partly circular and its validation requires an independent observation.

**Assumed numerical case:** If measured lambda is 1.03 while target is 1.00, the calibration must correct in the physically appropriate direction.

**Calculation walkthrough:** At λ_measured=1.03, the exhaust indication is slightly leaner than λ_target=1.00, assuming the sensor and reference are valid. Correcting toward stoichiometry normally requires increasing delivered fuel relative to air. A feedback sign that instead reduces fuel will push λ farther above one and can amplify a control problem.

The stated values form a hypothetical teaching example and should be recalculated by hand. First write the governing relation, then translate the inputs to SI, then perform substitution before rounding the displayed output. Check the sign and order of magnitude against a physical limiting case. Finally, ask which measured input would dominate an uncertainty interval. A large discrepancy from an independently computed check is grounds to revise the work, not to adjust the accepted answer without explanation.

### 3. Interpret the result, including failures

**Critical interpretation:** Incorrect feedback sign or long delay can produce sustained oscillation. A misleading numerical result can arise even when the arithmetic is perfect: the problem may be a wrong system boundary, an inappropriate reference property, a time-averaged signal used for a crank-angle event, or an unrecorded controller response. State which of those failure mechanisms is most likely here. Think about the change that would be observed in cylinder pressure, exhaust temperature, manifold state, or brake output if the explanatory mechanism were genuinely active rather than merely correlated with an unrelated change.

**Experimental identifiability:** A neat equation does not imply that each parameter can be determined from available measurements. Two unknown effects may create the same measured output, especially when only torque and speed are logged. Design an independent measurement that distinguishes the competing explanations; when this is impossible, report a bounded family of plausible parameter values rather than a falsely precise single answer. Applied to **oxygen sensing and closed-loop mixture control**, this discipline helps decide whether the model is a prediction with independent evidence or merely a restatement of its input measurements. Write the most restrictive assumption in the margin of the calculation, then revise the interpretation if that assumption fails under the case-study operating conditions.

### 4. Measurement, uncertainty and experimental integrity

**Measurement and evidence plan:** Inject bounded sensor offsets in a nonhardware model and verify direction and saturation. Before any data are collected, define a consistent sample clock, an equipment configuration record and at least one repeated baseline run. Identify how the instrument is calibrated and what its resolution excludes. Put all conversions in the analysis code rather than transcribing rounded values manually. Where the quantity is derived from several measurements, propagate uncertainty through the formula or use an appropriate perturbation study. A graph should show its reference conditions and measurement units. Unsupported interpolation between sparse engine-map points is not experimental evidence.

**Conservation audit:** Start by marking the system boundary on a sketch. Separate fuel energy entering the cylinder from indicated work on the piston and brake work at the shaft. A computed improvement that violates energy conservation is a mistake, not a new engine phenomenon. Where an experimental result seems to contradict the calculation, investigate calibration, hidden storage, auxiliary loads and the interpretation of reference conditions before adding complexity to the model. A careful research report can hold two ideas at once: the simplified result is internally correct and it is insufficient for system approval. This is not a weakness of mathematical modeling; it is the reason engineering uses progressive verification against measurements.

### 5. Engineering decision and integration

**Design implication:** Demand sensor plausibility checks before enabling high-authority adaptive corrections. This lesson addresses only one component of the unit's problem: An engine controller must deliver changing torque with stable combustion and bounded exhaust temperatures. Changes that look beneficial locally can increase pumping loss, friction, catalyst warm-up time, thermal stress or control complexity elsewhere. Accordingly, the correct engineering decision requires a second comparison at an off-design state and a list of constraints that cannot be traded away. The next simulation or experiment should be chosen to resolve the most consequential unknown, not simply to make the improvement look larger.

A useful extension is to reverse the calculation: choose an output target, estimate the input it would require and then test whether the implied operating point satisfies the engine's load, temperature, fuel and emissions constraints. Reverse calculations frequently uncover impossible combinations that are obscured by forward examples. Record the result as a conditional design feasibility statement, not a claim of guaranteed machine performance.

### 6. Practice and assessment

1. **Conceptual:** Explain why the relation `Simple integral controller u[k+1]=u[k]+K_i*(lambda_target-lambda_measured).` is meaningful for this lesson. Name two necessary assumptions and a physical regime in which one fails.
2. **Calculation:** Reproduce and verify the worked case: If measured lambda is 1.03 while target is 1.00, the calibration must correct in the physically appropriate direction. Show units at every intermediate stage and carry at least one input uncertainty through the output.
3. **Diagnostic:** A team reports a performance improvement after changing one input. Construct an alternative explanation using a measurement error, thermal shift or controller response. What single observation would discriminate between them?
4. **Design:** In the case “An engine controller must deliver changing torque with stable combustion and bounded exhaust temperatures.”, propose one legitimate design change and one nonnegotiable constraint. Demand sensor plausibility checks before enabling high-authority adaptive corrections.
5. **Research practice:** Give a file naming and metadata convention that would allow another student to reproduce the analysis, including configuration, units and calibration state.

**Worked-answer checking guide.** For question 2, the reference result is described in the assumed numerical case; a correct submission must also specify the formula, the explicit units and the idealizations. For question 3, credit is earned for a falsifiable alternative mechanism and a measurement that can separate it from the original claim. For question 4, a design that ignores the nonnegotiable constraint is rejected even if its calculated objective improves.

**Further investigation.** Repeat the reasoning at two additional operating points: lower speed and higher intake temperature, or cold start and warmed-up operation where relevant. Describe why the same input perturbation might have a different result under those conditions. Decide which hypothesis can be evaluated safely using the offline numerical model and which requires qualified laboratory equipment.



---

# Internal Combustion Engines — U05-L05


## U05-L05 — Transient fueling, calibration and fault handling

**Learning target.** At the end of this lesson, a reader should interpret the governing relation, reproduce a worked estimate, identify the limiting assumption and plan an independent verification of the engineering claim.

### 1. Physical question and context

Begin with the question of what can legitimately be inferred about **transient fueling, calibration and fault handling** from a few laboratory numbers. Rapid air-path changes can outrun fuel film and manifold-state estimates. The distinction between a physical quantity and a convenient proxy matters because an engine is simultaneously a chemical reactor, a flow machine, a heat exchanger and an oscillating mechanism. A simple classroom calculation is useful when it makes this distinction precise. It becomes dangerous to reasoning when its hidden assumptions are forgotten.

### 2. Governing calculation and its domain

The working relation used here is `A first-order transient model is x_dot=(u-x)/tau; this is a simplification, not a full fuel-film law.`. Define every variable before substitution, keep a single system of units, and check whether its result should increase or decrease when an input changes. Ask which assumptions make the expression possible: steady conditions, a perfect gas, constant properties, a lumped state, negligible pressure loss or an ideal mechanical linkage may be necessary. If an assumption does not hold in the intended application, identify the direction of the expected deviation when physics permits. When that direction is not clear, do not guess; schedule a measurement or use a higher-fidelity calculation.

**Assumed numerical case:** For tau=0.2 s a 0.1 s change reaches about 39% of its step under the linear model.

**Calculation walkthrough:** For a first-order model at t=0.1 s and τ=0.2 s, fraction completed is 1−exp(−0.5)=0.3935, or 39.35%. At t=0.2 s, fraction becomes 63.21%. These numbers characterize only the chosen mathematical time constant; an actual transient fueling strategy includes additional delays and nonlinear states.

The stated values form a hypothetical teaching example and should be recalculated by hand. First write the governing relation, then translate the inputs to SI, then perform substitution before rounding the displayed output. Check the sign and order of magnitude against a physical limiting case. Finally, ask which measured input would dominate an uncertainty interval. A large discrepancy from an independently computed check is grounds to revise the work, not to adjust the accepted answer without explanation.

### 3. Interpret the result, including failures

**Critical interpretation:** Steady air–fuel maps cannot represent cold-wall wetting and cylinder-to-cylinder variability. A misleading numerical result can arise even when the arithmetic is perfect: the problem may be a wrong system boundary, an inappropriate reference property, a time-averaged signal used for a crank-angle event, or an unrecorded controller response. State which of those failure mechanisms is most likely here. Think about the change that would be observed in cylinder pressure, exhaust temperature, manifold state, or brake output if the explanatory mechanism were genuinely active rather than merely correlated with an unrelated change.

**Operating-envelope reasoning:** Any model can look successful at its calibration point. The meaningful question is whether its error stays acceptably small at cold start, hot idle, high load, low ambient pressure, and during rapid change. Define this intended envelope explicitly, keep data from some points for validation, and reject extrapolation outside known physical or measurement limits. Applied to **transient fueling, calibration and fault handling**, this discipline helps decide whether the model is a prediction with independent evidence or merely a restatement of its input measurements. Write the most restrictive assumption in the margin of the calculation, then revise the interpretation if that assumption fails under the case-study operating conditions.

### 4. Measurement, uncertainty and experimental integrity

**Measurement and evidence plan:** Run logged steps with temperature, air mass and lambda sensors while limiting load. Before any data are collected, define a consistent sample clock, an equipment configuration record and at least one repeated baseline run. Identify how the instrument is calibrated and what its resolution excludes. Put all conversions in the analysis code rather than transcribing rounded values manually. Where the quantity is derived from several measurements, propagate uncertainty through the formula or use an appropriate perturbation study. A graph should show its reference conditions and measurement units. Unsupported interpolation between sparse engine-map points is not experimental evidence.

**Scale and sensitivity:** Scaling a geometric or thermal parameter is not a free performance gain. With every scale change, ask which transport time, stress, temperature, pressure ratio or nondimensional group changes with it. If the underlying response is nonlinear, quote a local sensitivity around the stated operating point instead of applying a single proportional rule across an engine map. A careful research report can hold two ideas at once: the simplified result is internally correct and it is insufficient for system approval. This is not a weakness of mathematical modeling; it is the reason engineering uses progressive verification against measurements.

### 5. Engineering decision and integration

**Design implication:** Define a safe degradation mode for implausible sensors rather than relying on a single reading. This lesson addresses only one component of the unit's problem: An engine controller must deliver changing torque with stable combustion and bounded exhaust temperatures. Changes that look beneficial locally can increase pumping loss, friction, catalyst warm-up time, thermal stress or control complexity elsewhere. Accordingly, the correct engineering decision requires a second comparison at an off-design state and a list of constraints that cannot be traded away. The next simulation or experiment should be chosen to resolve the most consequential unknown, not simply to make the improvement look larger.

A useful extension is to reverse the calculation: choose an output target, estimate the input it would require and then test whether the implied operating point satisfies the engine's load, temperature, fuel and emissions constraints. Reverse calculations frequently uncover impossible combinations that are obscured by forward examples. Record the result as a conditional design feasibility statement, not a claim of guaranteed machine performance.

### 6. Practice and assessment

1. **Conceptual:** Explain why the relation `A first-order transient model is x_dot=(u-x)/tau; this is a simplification, not a full fuel-film law.` is meaningful for this lesson. Name two necessary assumptions and a physical regime in which one fails.
2. **Calculation:** Reproduce and verify the worked case: For tau=0.2 s a 0.1 s change reaches about 39% of its step under the linear model. Show units at every intermediate stage and carry at least one input uncertainty through the output.
3. **Diagnostic:** A team reports a performance improvement after changing one input. Construct an alternative explanation using a measurement error, thermal shift or controller response. What single observation would discriminate between them?
4. **Design:** In the case “An engine controller must deliver changing torque with stable combustion and bounded exhaust temperatures.”, propose one legitimate design change and one nonnegotiable constraint. Define a safe degradation mode for implausible sensors rather than relying on a single reading.
5. **Research practice:** Give a file naming and metadata convention that would allow another student to reproduce the analysis, including configuration, units and calibration state.

**Worked-answer checking guide.** For question 2, the reference result is described in the assumed numerical case; a correct submission must also specify the formula, the explicit units and the idealizations. For question 3, credit is earned for a falsifiable alternative mechanism and a measurement that can separate it from the original claim. For question 4, a design that ignores the nonnegotiable constraint is rejected even if its calculated objective improves.

**Further investigation.** Repeat the reasoning at two additional operating points: lower speed and higher intake temperature, or cold start and warmed-up operation where relevant. Describe why the same input perturbation might have a different result under those conditions. Decide which hypothesis can be evaluated safely using the offline numerical model and which requires qualified laboratory equipment.



---

