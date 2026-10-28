# Unit 07: Emissions, Aftertreatment and Experimental Measurement

**Course Code**: ICE 207 · **Level**: Advanced Undergraduate Engineering

## Unit Overview & Physical Foundations

This comprehensive university textbook unit covers the theoretical framework, physical modeling, mathematical governing equations, and engineering applications of **Emissions, Aftertreatment and Experimental Measurement**.

# Internal Combustion Engines — U07-L01


## U07-L01 — Formation mechanisms for NOx, CO, HC and particulate

**Learning target.** At the end of this lesson, a reader should interpret the governing relation, reproduce a worked estimate, identify the limiting assumption and plan an independent verification of the engineering claim.

### 1. Physical question and context

The central issue in **formation mechanisms for nox, co, hc and particulate** is not memorizing a formula but knowing when its use is justified. Temperature, oxygen availability, mixing and wall effects alter pollutants by different mechanisms. A model's apparent precision depends on measurement resolution, parameter provenance and the operating envelope. At the outset specify whether a statement refers to a single cylinder, all cylinders, indicated work, brake shaft work, intake flow or exhaust flow. Changing that definition silently can invalidate a numerical answer while leaving its arithmetic flawless.

### 2. Governing calculation and its domain

The working relation used here is `Normalize mass emissions by useful work: g/kWh = grams emitted / brake work in kWh.`. Define every variable before substitution, keep a single system of units, and check whether its result should increase or decrease when an input changes. Ask which assumptions make the expression possible: steady conditions, a perfect gas, constant properties, a lumped state, negligible pressure loss or an ideal mechanical linkage may be necessary. If an assumption does not hold in the intended application, identify the direction of the expected deviation when physics permits. When that direction is not clear, do not guess; schedule a measurement or use a higher-fidelity calculation.

**Assumed numerical case:** An illustrative run emitting 20 g of a constituent while delivering 50 kWh yields 0.4 g/kWh.

**Calculation walkthrough:** If measured pollutant mass is 20 g over a test yielding 50 kWh of brake work, the normalized intensity is 20/50 = 0.40 g/kWh. A reading of 100 ppm cannot be directly substituted for 20 g because mass flow and species molecular mass are needed. Ensure the mass and work cover exactly the same time interval.

The stated values form a hypothetical teaching example and should be recalculated by hand. First write the governing relation, then translate the inputs to SI, then perform substitution before rounding the displayed output. Check the sign and order of magnitude against a physical limiting case. Finally, ask which measured input would dominate an uncertainty interval. A large discrepancy from an independently computed check is grounds to revise the work, not to adjust the accepted answer without explanation.

### 3. Interpret the result, including failures

**Critical interpretation:** Concentration in ppm cannot be compared as mass rate without exhaust-flow information. A misleading numerical result can arise even when the arithmetic is perfect: the problem may be a wrong system boundary, an inappropriate reference property, a time-averaged signal used for a crank-angle event, or an unrecorded controller response. State which of those failure mechanisms is most likely here. Think about the change that would be observed in cylinder pressure, exhaust temperature, manifold state, or brake output if the explanatory mechanism were genuinely active rather than merely correlated with an unrelated change.

**Conservation audit:** Start by marking the system boundary on a sketch. Separate fuel energy entering the cylinder from indicated work on the piston and brake work at the shaft. A computed improvement that violates energy conservation is a mistake, not a new engine phenomenon. Where an experimental result seems to contradict the calculation, investigate calibration, hidden storage, auxiliary loads and the interpretation of reference conditions before adding complexity to the model. Applied to **formation mechanisms for nox, co, hc and particulate**, this discipline helps decide whether the model is a prediction with independent evidence or merely a restatement of its input measurements. Write the most restrictive assumption in the margin of the calculation, then revise the interpretation if that assumption fails under the case-study operating conditions.

### 4. Measurement, uncertainty and experimental integrity

**Measurement and evidence plan:** Calibrate analyzers, account for sampling delay and check whether data are wet or dry. Before any data are collected, define a consistent sample clock, an equipment configuration record and at least one repeated baseline run. Identify how the instrument is calibrated and what its resolution excludes. Put all conversions in the analysis code rather than transcribing rounded values manually. Where the quantity is derived from several measurements, propagate uncertainty through the formula or use an appropriate perturbation study. A graph should show its reference conditions and measurement units. Unsupported interpolation between sparse engine-map points is not experimental evidence.

**Time dependence:** Engines operate through rapid events and slowly changing component states simultaneously. A crank-angle snapshot can describe the valve position but not warm-up; an averaged steady flow can describe laboratory demand but hide combustion variability. State the time scale to which each measured quantity belongs before comparing it with a model prediction. A careful research report can hold two ideas at once: the simplified result is internally correct and it is insufficient for system approval. This is not a weakness of mathematical modeling; it is the reason engineering uses progressive verification against measurements.

### 5. Engineering decision and integration

**Design implication:** Compare separate pollutant and fuel-economy objectives rather than a single vague clean label. This lesson addresses only one component of the unit's problem: A test group compares two calibrations across warmed-up steady states and a representative transient cycle. Changes that look beneficial locally can increase pumping loss, friction, catalyst warm-up time, thermal stress or control complexity elsewhere. Accordingly, the correct engineering decision requires a second comparison at an off-design state and a list of constraints that cannot be traded away. The next simulation or experiment should be chosen to resolve the most consequential unknown, not simply to make the improvement look larger.

A useful extension is to reverse the calculation: choose an output target, estimate the input it would require and then test whether the implied operating point satisfies the engine's load, temperature, fuel and emissions constraints. Reverse calculations frequently uncover impossible combinations that are obscured by forward examples. Record the result as a conditional design feasibility statement, not a claim of guaranteed machine performance.

### 6. Practice and assessment

1. **Conceptual:** Explain why the relation `Normalize mass emissions by useful work: g/kWh = grams emitted / brake work in kWh.` is meaningful for this lesson. Name two necessary assumptions and a physical regime in which one fails.
2. **Calculation:** Reproduce and verify the worked case: An illustrative run emitting 20 g of a constituent while delivering 50 kWh yields 0.4 g/kWh. Show units at every intermediate stage and carry at least one input uncertainty through the output.
3. **Diagnostic:** A team reports a performance improvement after changing one input. Construct an alternative explanation using a measurement error, thermal shift or controller response. What single observation would discriminate between them?
4. **Design:** In the case “A test group compares two calibrations across warmed-up steady states and a representative transient cycle.”, propose one legitimate design change and one nonnegotiable constraint. Compare separate pollutant and fuel-economy objectives rather than a single vague clean label.
5. **Research practice:** Give a file naming and metadata convention that would allow another student to reproduce the analysis, including configuration, units and calibration state.

**Worked-answer checking guide.** For question 2, the reference result is described in the assumed numerical case; a correct submission must also specify the formula, the explicit units and the idealizations. For question 3, credit is earned for a falsifiable alternative mechanism and a measurement that can separate it from the original claim. For question 4, a design that ignores the nonnegotiable constraint is rejected even if its calculated objective improves.

**Further investigation.** Repeat the reasoning at two additional operating points: lower speed and higher intake temperature, or cold start and warmed-up operation where relevant. Describe why the same input perturbation might have a different result under those conditions. Decide which hypothesis can be evaluated safely using the offline numerical model and which requires qualified laboratory equipment.



---

# Internal Combustion Engines — U07-L02


## U07-L02 — Three-way catalysts and stoichiometric windows

**Learning target.** At the end of this lesson, a reader should interpret the governing relation, reproduce a worked estimate, identify the limiting assumption and plan an independent verification of the engineering claim.

### 1. Physical question and context

A defensible treatment of **three-way catalysts and stoichiometric windows** begins by separating observable behavior from explanatory mechanism. A three-way catalyst converts targeted pollutants best when oxygen storage and exhaust composition are compatible. In an internal combustion engine this distinction is especially important because the same output can be produced by changes in fueling, volumetric efficiency, combustion phase, wall heat transfer or mechanical loss. The lesson therefore treats a compact formula as a hypothesis to be tested, not as an exact engine description.

### 2. Governing calculation and its domain

The smallest useful model is `Conversion efficiency eta=1-(mass_out/mass_in) for comparable mass measurements.`. Write it first in symbols because symbols expose which quantities are inputs and which are derived. Conduct a dimensional check. For example, an energy rate must have dimensions of power, and a dimensionless efficiency must not quietly carry a pressure unit. Then inspect the limiting cases. A vanishing input, a zero flow or an impossible temperature ratio should trigger a validity warning rather than a numerically polished answer. The equation belongs to the assumptions stated with it, not to every engine.

**Assumed numerical case:** An upstream 1.0 g/min CO signal and downstream 0.15 g/min imply 85% conversion.

**Calculation walkthrough:** Using a matching upstream mass rate 1.0 g/min and downstream 0.15 g/min, conversion = (1−0.15/1.0)×100 = 85%. This is a single idealized operating point. To interpret a real catalyst, report temperature, aging, oxygen state, flow and transient context together with the input/output analyte measurements.

The stated values form a hypothetical teaching example and should be recalculated by hand. First write the governing relation, then translate the inputs to SI, then perform substitution before rounding the displayed output. Check the sign and order of magnitude against a physical limiting case. Finally, ask which measured input would dominate an uncertainty interval. A large discrepancy from an independently computed check is grounds to revise the work, not to adjust the accepted answer without explanation.

### 3. Interpret the result, including failures

**Critical interpretation:** Warm-up, aging, transient lambda and flow rate change apparent conversion. A misleading numerical result can arise even when the arithmetic is perfect: the problem may be a wrong system boundary, an inappropriate reference property, a time-averaged signal used for a crank-angle event, or an unrecorded controller response. State which of those failure mechanisms is most likely here. Think about the change that would be observed in cylinder pressure, exhaust temperature, manifold state, or brake output if the explanatory mechanism were genuinely active rather than merely correlated with an unrelated change.

**Scale and sensitivity:** Scaling a geometric or thermal parameter is not a free performance gain. With every scale change, ask which transport time, stress, temperature, pressure ratio or nondimensional group changes with it. If the underlying response is nonlinear, quote a local sensitivity around the stated operating point instead of applying a single proportional rule across an engine map. Applied to **three-way catalysts and stoichiometric windows**, this discipline helps decide whether the model is a prediction with independent evidence or merely a restatement of its input measurements. Write the most restrictive assumption in the margin of the calculation, then revise the interpretation if that assumption fails under the case-study operating conditions.

### 4. Measurement, uncertainty and experimental integrity

**Measurement and evidence plan:** Pair upstream/downstream measurements with temperature and mass-flow logging. Before any data are collected, define a consistent sample clock, an equipment configuration record and at least one repeated baseline run. Identify how the instrument is calibrated and what its resolution excludes. Put all conversions in the analysis code rather than transcribing rounded values manually. Where the quantity is derived from several measurements, propagate uncertainty through the formula or use an appropriate perturbation study. A graph should show its reference conditions and measurement units. Unsupported interpolation between sparse engine-map points is not experimental evidence.

**Experimental identifiability:** A neat equation does not imply that each parameter can be determined from available measurements. Two unknown effects may create the same measured output, especially when only torque and speed are logged. Design an independent measurement that distinguishes the competing explanations; when this is impossible, report a bounded family of plausible parameter values rather than a falsely precise single answer. A careful research report can hold two ideas at once: the simplified result is internally correct and it is insufficient for system approval. This is not a weakness of mathematical modeling; it is the reason engineering uses progressive verification against measurements.

### 5. Engineering decision and integration

**Design implication:** Do not transfer a hot steady conversion value to cold-start conditions. This lesson addresses only one component of the unit's problem: A test group compares two calibrations across warmed-up steady states and a representative transient cycle. Changes that look beneficial locally can increase pumping loss, friction, catalyst warm-up time, thermal stress or control complexity elsewhere. Accordingly, the correct engineering decision requires a second comparison at an off-design state and a list of constraints that cannot be traded away. The next simulation or experiment should be chosen to resolve the most consequential unknown, not simply to make the improvement look larger.

A useful extension is to reverse the calculation: choose an output target, estimate the input it would require and then test whether the implied operating point satisfies the engine's load, temperature, fuel and emissions constraints. Reverse calculations frequently uncover impossible combinations that are obscured by forward examples. Record the result as a conditional design feasibility statement, not a claim of guaranteed machine performance.

### 6. Practice and assessment

1. **Conceptual:** Explain why the relation `Conversion efficiency eta=1-(mass_out/mass_in) for comparable mass measurements.` is meaningful for this lesson. Name two necessary assumptions and a physical regime in which one fails.
2. **Calculation:** Reproduce and verify the worked case: An upstream 1.0 g/min CO signal and downstream 0.15 g/min imply 85% conversion. Show units at every intermediate stage and carry at least one input uncertainty through the output.
3. **Diagnostic:** A team reports a performance improvement after changing one input. Construct an alternative explanation using a measurement error, thermal shift or controller response. What single observation would discriminate between them?
4. **Design:** In the case “A test group compares two calibrations across warmed-up steady states and a representative transient cycle.”, propose one legitimate design change and one nonnegotiable constraint. Do not transfer a hot steady conversion value to cold-start conditions.
5. **Research practice:** Give a file naming and metadata convention that would allow another student to reproduce the analysis, including configuration, units and calibration state.

**Worked-answer checking guide.** For question 2, the reference result is described in the assumed numerical case; a correct submission must also specify the formula, the explicit units and the idealizations. For question 3, credit is earned for a falsifiable alternative mechanism and a measurement that can separate it from the original claim. For question 4, a design that ignores the nonnegotiable constraint is rejected even if its calculated objective improves.

**Further investigation.** Repeat the reasoning at two additional operating points: lower speed and higher intake temperature, or cold start and warmed-up operation where relevant. Describe why the same input perturbation might have a different result under those conditions. Decide which hypothesis can be evaluated safely using the offline numerical model and which requires qualified laboratory equipment.



---

# Internal Combustion Engines — U07-L03


## U07-L03 — Diesel oxidation catalysts, particulate filters and SCR

**Learning target.** At the end of this lesson, a reader should interpret the governing relation, reproduce a worked estimate, identify the limiting assumption and plan an independent verification of the engineering claim.

### 1. Physical question and context

Begin with the question of what can legitimately be inferred about **diesel oxidation catalysts, particulate filters and scr** from a few laboratory numbers. Compression-ignition aftertreatment uses distinct devices with distinct temperature and maintenance demands. The distinction between a physical quantity and a convenient proxy matters because an engine is simultaneously a chemical reactor, a flow machine, a heat exchanger and an oscillating mechanism. A simple classroom calculation is useful when it makes this distinction precise. It becomes dangerous to reasoning when its hidden assumptions are forgotten.

### 2. Governing calculation and its domain

Use `A mass capture estimate is eta_c=(m_in-m_out)/m_in.` as the initial closure relation. It is tempting to interpret the number as a design guarantee; instead define a reference operating point, perturb each independent input separately and observe the output response. Check whether apparently independent variables are actually correlated by conservation or control logic. Treat a high-sensitivity variable as a candidate for better measurement. If the result requires a parameter measured by the same output that is being predicted, the model is partly circular and its validation requires an independent observation.

**Assumed numerical case:** If particulate entering a filter is 2.0 g/h and leaving is 0.1 g/h, apparent capture is 95%.

**Calculation walkthrough:** For 2.0 g/h particulate entering and 0.1 g/h leaving, capture fraction is (2.0−0.1)/2.0 = 0.95, or 95%. The value is not necessarily sustained during regeneration or different particle-size distributions. Check differential pressure and filter loading before comparing filter architectures.

The stated values form a hypothetical teaching example and should be recalculated by hand. First write the governing relation, then translate the inputs to SI, then perform substitution before rounding the displayed output. Check the sign and order of magnitude against a physical limiting case. Finally, ask which measured input would dominate an uncertainty interval. A large discrepancy from an independently computed check is grounds to revise the work, not to adjust the accepted answer without explanation.

### 3. Interpret the result, including failures

**Critical interpretation:** Ash, backpressure, active regeneration and reductant supply create system tradeoffs. A misleading numerical result can arise even when the arithmetic is perfect: the problem may be a wrong system boundary, an inappropriate reference property, a time-averaged signal used for a crank-angle event, or an unrecorded controller response. State which of those failure mechanisms is most likely here. Think about the change that would be observed in cylinder pressure, exhaust temperature, manifold state, or brake output if the explanatory mechanism were genuinely active rather than merely correlated with an unrelated change.

**Time dependence:** Engines operate through rapid events and slowly changing component states simultaneously. A crank-angle snapshot can describe the valve position but not warm-up; an averaged steady flow can describe laboratory demand but hide combustion variability. State the time scale to which each measured quantity belongs before comparing it with a model prediction. Applied to **diesel oxidation catalysts, particulate filters and scr**, this discipline helps decide whether the model is a prediction with independent evidence or merely a restatement of its input measurements. Write the most restrictive assumption in the margin of the calculation, then revise the interpretation if that assumption fails under the case-study operating conditions.

### 4. Measurement, uncertainty and experimental integrity

**Measurement and evidence plan:** Measure backpressure, catalyst inlet temperature, differential pressure and downstream species. Before any data are collected, define a consistent sample clock, an equipment configuration record and at least one repeated baseline run. Identify how the instrument is calibrated and what its resolution excludes. Put all conversions in the analysis code rather than transcribing rounded values manually. Where the quantity is derived from several measurements, propagate uncertainty through the formula or use an appropriate perturbation study. A graph should show its reference conditions and measurement units. Unsupported interpolation between sparse engine-map points is not experimental evidence.

**Operating-envelope reasoning:** Any model can look successful at its calibration point. The meaningful question is whether its error stays acceptably small at cold start, hot idle, high load, low ambient pressure, and during rapid change. Define this intended envelope explicitly, keep data from some points for validation, and reject extrapolation outside known physical or measurement limits. A careful research report can hold two ideas at once: the simplified result is internally correct and it is insufficient for system approval. This is not a weakness of mathematical modeling; it is the reason engineering uses progressive verification against measurements.

### 5. Engineering decision and integration

**Design implication:** Separate filter efficiency from whole-vehicle compliance and regeneration duty. This lesson addresses only one component of the unit's problem: A test group compares two calibrations across warmed-up steady states and a representative transient cycle. Changes that look beneficial locally can increase pumping loss, friction, catalyst warm-up time, thermal stress or control complexity elsewhere. Accordingly, the correct engineering decision requires a second comparison at an off-design state and a list of constraints that cannot be traded away. The next simulation or experiment should be chosen to resolve the most consequential unknown, not simply to make the improvement look larger.

A useful extension is to reverse the calculation: choose an output target, estimate the input it would require and then test whether the implied operating point satisfies the engine's load, temperature, fuel and emissions constraints. Reverse calculations frequently uncover impossible combinations that are obscured by forward examples. Record the result as a conditional design feasibility statement, not a claim of guaranteed machine performance.

### 6. Practice and assessment

1. **Conceptual:** Explain why the relation `A mass capture estimate is eta_c=(m_in-m_out)/m_in.` is meaningful for this lesson. Name two necessary assumptions and a physical regime in which one fails.
2. **Calculation:** Reproduce and verify the worked case: If particulate entering a filter is 2.0 g/h and leaving is 0.1 g/h, apparent capture is 95%. Show units at every intermediate stage and carry at least one input uncertainty through the output.
3. **Diagnostic:** A team reports a performance improvement after changing one input. Construct an alternative explanation using a measurement error, thermal shift or controller response. What single observation would discriminate between them?
4. **Design:** In the case “A test group compares two calibrations across warmed-up steady states and a representative transient cycle.”, propose one legitimate design change and one nonnegotiable constraint. Separate filter efficiency from whole-vehicle compliance and regeneration duty.
5. **Research practice:** Give a file naming and metadata convention that would allow another student to reproduce the analysis, including configuration, units and calibration state.

**Worked-answer checking guide.** For question 2, the reference result is described in the assumed numerical case; a correct submission must also specify the formula, the explicit units and the idealizations. For question 3, credit is earned for a falsifiable alternative mechanism and a measurement that can separate it from the original claim. For question 4, a design that ignores the nonnegotiable constraint is rejected even if its calculated objective improves.

**Further investigation.** Repeat the reasoning at two additional operating points: lower speed and higher intake temperature, or cold start and warmed-up operation where relevant. Describe why the same input perturbation might have a different result under those conditions. Decide which hypothesis can be evaluated safely using the offline numerical model and which requires qualified laboratory equipment.



---

# Internal Combustion Engines — U07-L04


## U07-L04 — Engine dynamometer and measurement uncertainty

**Learning target.** At the end of this lesson, a reader should interpret the governing relation, reproduce a worked estimate, identify the limiting assumption and plan an independent verification of the engineering claim.

### 1. Physical question and context

Consider an engineer who is evaluating **engine dynamometer and measurement uncertainty** in the following setting: A test group compares two calibrations across warmed-up steady states and a representative transient cycle. The analytical priority is not to maximize the number of equations. It is to identify the correct conserved quantity, select a boundary and state the outcome that the instrument or simulation actually reports. Measured efficiency is only as reliable as torque, speed, fuel flow and the stability of the operating point. Two measurements that share a unit may still refer to different control volumes, time windows or reference states.

### 2. Governing calculation and its domain

The working relation used here is `P=2*pi*N*T/60; propagate uncertainty from torque and speed rather than assuming exact data.`. Define every variable before substitution, keep a single system of units, and check whether its result should increase or decrease when an input changes. Ask which assumptions make the expression possible: steady conditions, a perfect gas, constant properties, a lumped state, negligible pressure loss or an ideal mechanical linkage may be necessary. If an assumption does not hold in the intended application, identify the direction of the expected deviation when physics permits. When that direction is not clear, do not guess; schedule a measurement or use a higher-fidelity calculation.

**Assumed numerical case:** At 150 N m and 2500 rpm, brake power is approximately 39.3 kW.

**Calculation walkthrough:** Convert 2500 rpm to 41.667 revolutions per second, multiply by 2π to obtain 261.799 rad/s, then multiply by 150 N·m for 39,269.9 W or 39.27 kW. A torque error of 1% contributes approximately 1% relative power error when speed uncertainty is negligible. That uncertainty can decide whether a small efficiency difference is persuasive.

The stated values form a hypothetical teaching example and should be recalculated by hand. First write the governing relation, then translate the inputs to SI, then perform substitution before rounding the displayed output. Check the sign and order of magnitude against a physical limiting case. Finally, ask which measured input would dominate an uncertainty interval. A large discrepancy from an independently computed check is grounds to revise the work, not to adjust the accepted answer without explanation.

### 3. Interpret the result, including failures

**Critical interpretation:** Uncorrected ambient conditions and sensor offsets can exceed a claimed small improvement. A misleading numerical result can arise even when the arithmetic is perfect: the problem may be a wrong system boundary, an inappropriate reference property, a time-averaged signal used for a crank-angle event, or an unrecorded controller response. State which of those failure mechanisms is most likely here. Think about the change that would be observed in cylinder pressure, exhaust temperature, manifold state, or brake output if the explanatory mechanism were genuinely active rather than merely correlated with an unrelated change.

**Experimental identifiability:** A neat equation does not imply that each parameter can be determined from available measurements. Two unknown effects may create the same measured output, especially when only torque and speed are logged. Design an independent measurement that distinguishes the competing explanations; when this is impossible, report a bounded family of plausible parameter values rather than a falsely precise single answer. Applied to **engine dynamometer and measurement uncertainty**, this discipline helps decide whether the model is a prediction with independent evidence or merely a restatement of its input measurements. Write the most restrictive assumption in the margin of the calculation, then revise the interpretation if that assumption fails under the case-study operating conditions.

### 4. Measurement, uncertainty and experimental integrity

**Measurement and evidence plan:** Perform zero checks, traceable calibration and repeat runs with full uncertainty budgets. Before any data are collected, define a consistent sample clock, an equipment configuration record and at least one repeated baseline run. Identify how the instrument is calibrated and what its resolution excludes. Put all conversions in the analysis code rather than transcribing rounded values manually. Where the quantity is derived from several measurements, propagate uncertainty through the formula or use an appropriate perturbation study. A graph should show its reference conditions and measurement units. Unsupported interpolation between sparse engine-map points is not experimental evidence.

**Conservation audit:** Start by marking the system boundary on a sketch. Separate fuel energy entering the cylinder from indicated work on the piston and brake work at the shaft. A computed improvement that violates energy conservation is a mistake, not a new engine phenomenon. Where an experimental result seems to contradict the calculation, investigate calibration, hidden storage, auxiliary loads and the interpretation of reference conditions before adding complexity to the model. A careful research report can hold two ideas at once: the simplified result is internally correct and it is insufficient for system approval. This is not a weakness of mathematical modeling; it is the reason engineering uses progressive verification against measurements.

### 5. Engineering decision and integration

**Design implication:** Require improvement exceeding combined uncertainty before calling a design winner. This lesson addresses only one component of the unit's problem: A test group compares two calibrations across warmed-up steady states and a representative transient cycle. Changes that look beneficial locally can increase pumping loss, friction, catalyst warm-up time, thermal stress or control complexity elsewhere. Accordingly, the correct engineering decision requires a second comparison at an off-design state and a list of constraints that cannot be traded away. The next simulation or experiment should be chosen to resolve the most consequential unknown, not simply to make the improvement look larger.

A useful extension is to reverse the calculation: choose an output target, estimate the input it would require and then test whether the implied operating point satisfies the engine's load, temperature, fuel and emissions constraints. Reverse calculations frequently uncover impossible combinations that are obscured by forward examples. Record the result as a conditional design feasibility statement, not a claim of guaranteed machine performance.

### 6. Practice and assessment

1. **Conceptual:** Explain why the relation `P=2*pi*N*T/60; propagate uncertainty from torque and speed rather than assuming exact data.` is meaningful for this lesson. Name two necessary assumptions and a physical regime in which one fails.
2. **Calculation:** Reproduce and verify the worked case: At 150 N m and 2500 rpm, brake power is approximately 39.3 kW. Show units at every intermediate stage and carry at least one input uncertainty through the output.
3. **Diagnostic:** A team reports a performance improvement after changing one input. Construct an alternative explanation using a measurement error, thermal shift or controller response. What single observation would discriminate between them?
4. **Design:** In the case “A test group compares two calibrations across warmed-up steady states and a representative transient cycle.”, propose one legitimate design change and one nonnegotiable constraint. Require improvement exceeding combined uncertainty before calling a design winner.
5. **Research practice:** Give a file naming and metadata convention that would allow another student to reproduce the analysis, including configuration, units and calibration state.

**Worked-answer checking guide.** For question 2, the reference result is described in the assumed numerical case; a correct submission must also specify the formula, the explicit units and the idealizations. For question 3, credit is earned for a falsifiable alternative mechanism and a measurement that can separate it from the original claim. For question 4, a design that ignores the nonnegotiable constraint is rejected even if its calculated objective improves.

**Further investigation.** Repeat the reasoning at two additional operating points: lower speed and higher intake temperature, or cold start and warmed-up operation where relevant. Describe why the same input perturbation might have a different result under those conditions. Decide which hypothesis can be evaluated safely using the offline numerical model and which requires qualified laboratory equipment.



---

# Internal Combustion Engines — U07-L05


## U07-L05 — Transient emissions and reproducible test design

**Learning target.** At the end of this lesson, a reader should interpret the governing relation, reproduce a worked estimate, identify the limiting assumption and plan an independent verification of the engineering claim.

### 1. Physical question and context

The central issue in **transient emissions and reproducible test design** is not memorizing a formula but knowing when its use is justified. Transient cycles expose cold-start, thermal storage and control dynamics that steady maps miss. A model's apparent precision depends on measurement resolution, parameter provenance and the operating envelope. At the outset specify whether a statement refers to a single cylinder, all cylinders, indicated work, brake shaft work, intake flow or exhaust flow. Changing that definition silently can invalidate a numerical answer while leaving its arithmetic flawless.

### 2. Governing calculation and its domain

The smallest useful model is `Distance-normalized emissions = integrated pollutant mass / distance for a vehicle cycle.`. Write it first in symbols because symbols expose which quantities are inputs and which are derived. Conduct a dimensional check. For example, an energy rate must have dimensions of power, and a dimensionless efficiency must not quietly carry a pressure unit. Then inspect the limiting cases. A vanishing input, a zero flow or an impossible temperature ratio should trigger a validity warning rather than a numerically polished answer. The equation belongs to the assumptions stated with it, not to every engine.

**Assumed numerical case:** A 1.5 g integrated pollutant mass over a 12 km cycle is 0.125 g/km.

**Calculation walkthrough:** An integrated emission mass of 1.5 g over 12 km gives 1.5/12 = 0.125 g/km. To compare test cycles, preserve the same distance and phase definitions, include cold-start behavior if relevant, and align pollutant analyzers to exhaust transport time. A difference in distance normalization must not be confused with an emissions reduction.

The stated values form a hypothetical teaching example and should be recalculated by hand. First write the governing relation, then translate the inputs to SI, then perform substitution before rounding the displayed output. Check the sign and order of magnitude against a physical limiting case. Finally, ask which measured input would dominate an uncertainty interval. A large discrepancy from an independently computed check is grounds to revise the work, not to adjust the accepted answer without explanation.

### 3. Interpret the result, including failures

**Critical interpretation:** Road load, ambient, driver trace and instrumentation all influence repeatability. A misleading numerical result can arise even when the arithmetic is perfect: the problem may be a wrong system boundary, an inappropriate reference property, a time-averaged signal used for a crank-angle event, or an unrecorded controller response. State which of those failure mechanisms is most likely here. Think about the change that would be observed in cylinder pressure, exhaust temperature, manifold state, or brake output if the explanatory mechanism were genuinely active rather than merely correlated with an unrelated change.

**Operating-envelope reasoning:** Any model can look successful at its calibration point. The meaningful question is whether its error stays acceptably small at cold start, hot idle, high load, low ambient pressure, and during rapid change. Define this intended envelope explicitly, keep data from some points for validation, and reject extrapolation outside known physical or measurement limits. Applied to **transient emissions and reproducible test design**, this discipline helps decide whether the model is a prediction with independent evidence or merely a restatement of its input measurements. Write the most restrictive assumption in the margin of the calculation, then revise the interpretation if that assumption fails under the case-study operating conditions.

### 4. Measurement, uncertainty and experimental integrity

**Measurement and evidence plan:** Time-align all signals, state test boundaries and compare replicated representative cycles. Before any data are collected, define a consistent sample clock, an equipment configuration record and at least one repeated baseline run. Identify how the instrument is calibrated and what its resolution excludes. Put all conversions in the analysis code rather than transcribing rounded values manually. Where the quantity is derived from several measurements, propagate uncertainty through the formula or use an appropriate perturbation study. A graph should show its reference conditions and measurement units. Unsupported interpolation between sparse engine-map points is not experimental evidence.

**Scale and sensitivity:** Scaling a geometric or thermal parameter is not a free performance gain. With every scale change, ask which transport time, stress, temperature, pressure ratio or nondimensional group changes with it. If the underlying response is nonlinear, quote a local sensitivity around the stated operating point instead of applying a single proportional rule across an engine map. A careful research report can hold two ideas at once: the simplified result is internally correct and it is insufficient for system approval. This is not a weakness of mathematical modeling; it is the reason engineering uses progressive verification against measurements.

### 5. Engineering decision and integration

**Design implication:** Do not equate an academic drive cycle with jurisdictional regulatory certification. This lesson addresses only one component of the unit's problem: A test group compares two calibrations across warmed-up steady states and a representative transient cycle. Changes that look beneficial locally can increase pumping loss, friction, catalyst warm-up time, thermal stress or control complexity elsewhere. Accordingly, the correct engineering decision requires a second comparison at an off-design state and a list of constraints that cannot be traded away. The next simulation or experiment should be chosen to resolve the most consequential unknown, not simply to make the improvement look larger.

A useful extension is to reverse the calculation: choose an output target, estimate the input it would require and then test whether the implied operating point satisfies the engine's load, temperature, fuel and emissions constraints. Reverse calculations frequently uncover impossible combinations that are obscured by forward examples. Record the result as a conditional design feasibility statement, not a claim of guaranteed machine performance.

### 6. Practice and assessment

1. **Conceptual:** Explain why the relation `Distance-normalized emissions = integrated pollutant mass / distance for a vehicle cycle.` is meaningful for this lesson. Name two necessary assumptions and a physical regime in which one fails.
2. **Calculation:** Reproduce and verify the worked case: A 1.5 g integrated pollutant mass over a 12 km cycle is 0.125 g/km. Show units at every intermediate stage and carry at least one input uncertainty through the output.
3. **Diagnostic:** A team reports a performance improvement after changing one input. Construct an alternative explanation using a measurement error, thermal shift or controller response. What single observation would discriminate between them?
4. **Design:** In the case “A test group compares two calibrations across warmed-up steady states and a representative transient cycle.”, propose one legitimate design change and one nonnegotiable constraint. Do not equate an academic drive cycle with jurisdictional regulatory certification.
5. **Research practice:** Give a file naming and metadata convention that would allow another student to reproduce the analysis, including configuration, units and calibration state.

**Worked-answer checking guide.** For question 2, the reference result is described in the assumed numerical case; a correct submission must also specify the formula, the explicit units and the idealizations. For question 3, credit is earned for a falsifiable alternative mechanism and a measurement that can separate it from the original claim. For question 4, a design that ignores the nonnegotiable constraint is rejected even if its calculated objective improves.

**Further investigation.** Repeat the reasoning at two additional operating points: lower speed and higher intake temperature, or cold start and warmed-up operation where relevant. Describe why the same input perturbation might have a different result under those conditions. Decide which hypothesis can be evaluated safely using the offline numerical model and which requires qualified laboratory equipment.



---

