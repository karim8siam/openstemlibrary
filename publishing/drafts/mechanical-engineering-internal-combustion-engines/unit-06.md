# Unit 06: Heat Transfer, Friction, Lubrication and Engine Durability

**Course Code**: ICE 206 · **Level**: Advanced Undergraduate Engineering

## Unit Overview & Physical Foundations

This comprehensive university textbook unit covers the theoretical framework, physical modeling, mathematical governing equations, and engineering applications of **Heat Transfer, Friction, Lubrication and Engine Durability**.

# Internal Combustion Engines — U06-L01


## U06-L01 — Combustion heat transfer and coolant rejection

**Learning target.** At the end of this lesson, a reader should interpret the governing relation, reproduce a worked estimate, identify the limiting assumption and plan an independent verification of the engineering claim.

### 1. Physical question and context

Consider an engineer who is evaluating **combustion heat transfer and coolant rejection** in the following setting: A long-duration duty cycle causes elevated coolant temperature and increasing friction at fixed torque. The analytical priority is not to maximize the number of equations. It is to identify the correct conserved quantity, select a boundary and state the outcome that the instrument or simulation actually reports. Combustion chemical energy splits among shaft work, coolant, exhaust, radiation and other losses. Two measurements that share a unit may still refer to different control volumes, time windows or reference states.

### 2. Governing calculation and its domain

The smallest useful model is `Steady coolant heat rate Q_dot = m_dot_c * cp_c * (T_out-T_in).`. Write it first in symbols because symbols expose which quantities are inputs and which are derived. Conduct a dimensional check. For example, an energy rate must have dimensions of power, and a dimensionless efficiency must not quietly carry a pressure unit. Then inspect the limiting cases. A vanishing input, a zero flow or an impossible temperature ratio should trigger a validity warning rather than a numerically polished answer. The equation belongs to the assumptions stated with it, not to every engine.

**Assumed numerical case:** At 0.5 kg/s water, cp=4.18 kJ/kg K and DeltaT=8 K, coolant heat is 16.7 kW.

**Calculation walkthrough:** For a 0.5 kg/s coolant flow, specific heat 4.18 kJ/(kg·K), and measured 8 K rise, Q_dot = 0.5×4.18×8 = 16.72 kW. If flow is not measured accurately or temperature probes are separated from the control volume, the energy-balance figure can shift. The result is a coolant heat rate, not useful shaft work.

The stated values form a hypothetical teaching example and should be recalculated by hand. First write the governing relation, then translate the inputs to SI, then perform substitution before rounding the displayed output. Check the sign and order of magnitude against a physical limiting case. Finally, ask which measured input would dominate an uncertainty interval. A large discrepancy from an independently computed check is grounds to revise the work, not to adjust the accepted answer without explanation.

### 3. Interpret the result, including failures

**Critical interpretation:** This estimate excludes transient storage and errors from temperature probe placement. A misleading numerical result can arise even when the arithmetic is perfect: the problem may be a wrong system boundary, an inappropriate reference property, a time-averaged signal used for a crank-angle event, or an unrecorded controller response. State which of those failure mechanisms is most likely here. Think about the change that would be observed in cylinder pressure, exhaust temperature, manifold state, or brake output if the explanatory mechanism were genuinely active rather than merely correlated with an unrelated change.

**Conservation audit:** Start by marking the system boundary on a sketch. Separate fuel energy entering the cylinder from indicated work on the piston and brake work at the shaft. A computed improvement that violates energy conservation is a mistake, not a new engine phenomenon. Where an experimental result seems to contradict the calculation, investigate calibration, hidden storage, auxiliary loads and the interpretation of reference conditions before adding complexity to the model. Applied to **combustion heat transfer and coolant rejection**, this discipline helps decide whether the model is a prediction with independent evidence or merely a restatement of its input measurements. Write the most restrictive assumption in the margin of the calculation, then revise the interpretation if that assumption fails under the case-study operating conditions.

### 4. Measurement, uncertainty and experimental integrity

**Measurement and evidence plan:** Measure coolant flow and paired temperatures under stable load with uncertainty estimates. Before any data are collected, define a consistent sample clock, an equipment configuration record and at least one repeated baseline run. Identify how the instrument is calibrated and what its resolution excludes. Put all conversions in the analysis code rather than transcribing rounded values manually. Where the quantity is derived from several measurements, propagate uncertainty through the formula or use an appropriate perturbation study. A graph should show its reference conditions and measurement units. Unsupported interpolation between sparse engine-map points is not experimental evidence.

**Time dependence:** Engines operate through rapid events and slowly changing component states simultaneously. A crank-angle snapshot can describe the valve position but not warm-up; an averaged steady flow can describe laboratory demand but hide combustion variability. State the time scale to which each measured quantity belongs before comparing it with a model prediction. A careful research report can hold two ideas at once: the simplified result is internally correct and it is insufficient for system approval. This is not a weakness of mathematical modeling; it is the reason engineering uses progressive verification against measurements.

### 5. Engineering decision and integration

**Design implication:** Optimize wall temperatures and durability, not simply the smallest coolant heat figure. This lesson addresses only one component of the unit's problem: A long-duration duty cycle causes elevated coolant temperature and increasing friction at fixed torque. Changes that look beneficial locally can increase pumping loss, friction, catalyst warm-up time, thermal stress or control complexity elsewhere. Accordingly, the correct engineering decision requires a second comparison at an off-design state and a list of constraints that cannot be traded away. The next simulation or experiment should be chosen to resolve the most consequential unknown, not simply to make the improvement look larger.

A useful extension is to reverse the calculation: choose an output target, estimate the input it would require and then test whether the implied operating point satisfies the engine's load, temperature, fuel and emissions constraints. Reverse calculations frequently uncover impossible combinations that are obscured by forward examples. Record the result as a conditional design feasibility statement, not a claim of guaranteed machine performance.

### 6. Practice and assessment

1. **Conceptual:** Explain why the relation `Steady coolant heat rate Q_dot = m_dot_c * cp_c * (T_out-T_in).` is meaningful for this lesson. Name two necessary assumptions and a physical regime in which one fails.
2. **Calculation:** Reproduce and verify the worked case: At 0.5 kg/s water, cp=4.18 kJ/kg K and DeltaT=8 K, coolant heat is 16.7 kW. Show units at every intermediate stage and carry at least one input uncertainty through the output.
3. **Diagnostic:** A team reports a performance improvement after changing one input. Construct an alternative explanation using a measurement error, thermal shift or controller response. What single observation would discriminate between them?
4. **Design:** In the case “A long-duration duty cycle causes elevated coolant temperature and increasing friction at fixed torque.”, propose one legitimate design change and one nonnegotiable constraint. Optimize wall temperatures and durability, not simply the smallest coolant heat figure.
5. **Research practice:** Give a file naming and metadata convention that would allow another student to reproduce the analysis, including configuration, units and calibration state.

**Worked-answer checking guide.** For question 2, the reference result is described in the assumed numerical case; a correct submission must also specify the formula, the explicit units and the idealizations. For question 3, credit is earned for a falsifiable alternative mechanism and a measurement that can separate it from the original claim. For question 4, a design that ignores the nonnegotiable constraint is rejected even if its calculated objective improves.

**Further investigation.** Repeat the reasoning at two additional operating points: lower speed and higher intake temperature, or cold start and warmed-up operation where relevant. Describe why the same input perturbation might have a different result under those conditions. Decide which hypothesis can be evaluated safely using the offline numerical model and which requires qualified laboratory equipment.



---

# Internal Combustion Engines — U06-L02


## U06-L02 — Lubrication regimes and oil film behavior

**Learning target.** At the end of this lesson, a reader should interpret the governing relation, reproduce a worked estimate, identify the limiting assumption and plan an independent verification of the engineering claim.

### 1. Physical question and context

The central issue in **lubrication regimes and oil film behavior** is not memorizing a formula but knowing when its use is justified. Hydrodynamic, mixed and boundary lubrication differ in how surfaces carry load and generate friction. A model's apparent precision depends on measurement resolution, parameter provenance and the operating envelope. At the outset specify whether a statement refers to a single cylinder, all cylinders, indicated work, brake shaft work, intake flow or exhaust flow. Changing that definition silently can invalidate a numerical answer while leaving its arithmetic flawless.

### 2. Governing calculation and its domain

Use `A simplified film parameter lambda_f = minimum film thickness / composite surface roughness.` as the initial closure relation. It is tempting to interpret the number as a design guarantee; instead define a reference operating point, perturb each independent input separately and observe the output response. Check whether apparently independent variables are actually correlated by conservation or control logic. Treat a high-sensitivity variable as a candidate for better measurement. If the result requires a parameter measured by the same output that is being predicted, the model is partly circular and its validation requires an independent observation.

**Assumed numerical case:** A 1.5 micrometre film over 0.5 micrometre composite roughness gives a nominal film parameter 3.

**Calculation walkthrough:** The illustrative film parameter is film thickness divided by composite roughness. Here λ_f = 1.5 μm/0.5 μm = 3. Both dimensions use the same micrometre unit, so the ratio is dimensionless. The number indicates a nominal regime, not a guarantee that every microscopic asperity stays separated under transient load.

The stated values form a hypothetical teaching example and should be recalculated by hand. First write the governing relation, then translate the inputs to SI, then perform substitution before rounding the displayed output. Check the sign and order of magnitude against a physical limiting case. Finally, ask which measured input would dominate an uncertainty interval. A large discrepancy from an independently computed check is grounds to revise the work, not to adjust the accepted answer without explanation.

### 3. Interpret the result, including failures

**Critical interpretation:** Average pressure does not guarantee local film survival at the contact or thermal hotspot. A misleading numerical result can arise even when the arithmetic is perfect: the problem may be a wrong system boundary, an inappropriate reference property, a time-averaged signal used for a crank-angle event, or an unrecorded controller response. State which of those failure mechanisms is most likely here. Think about the change that would be observed in cylinder pressure, exhaust temperature, manifold state, or brake output if the explanatory mechanism were genuinely active rather than merely correlated with an unrelated change.

**Scale and sensitivity:** Scaling a geometric or thermal parameter is not a free performance gain. With every scale change, ask which transport time, stress, temperature, pressure ratio or nondimensional group changes with it. If the underlying response is nonlinear, quote a local sensitivity around the stated operating point instead of applying a single proportional rule across an engine map. Applied to **lubrication regimes and oil film behavior**, this discipline helps decide whether the model is a prediction with independent evidence or merely a restatement of its input measurements. Write the most restrictive assumption in the margin of the calculation, then revise the interpretation if that assumption fails under the case-study operating conditions.

### 4. Measurement, uncertainty and experimental integrity

**Measurement and evidence plan:** Correlate oil temperature, pressure, particle wear trends and friction indicators. Before any data are collected, define a consistent sample clock, an equipment configuration record and at least one repeated baseline run. Identify how the instrument is calibrated and what its resolution excludes. Put all conversions in the analysis code rather than transcribing rounded values manually. Where the quantity is derived from several measurements, propagate uncertainty through the formula or use an appropriate perturbation study. A graph should show its reference conditions and measurement units. Unsupported interpolation between sparse engine-map points is not experimental evidence.

**Experimental identifiability:** A neat equation does not imply that each parameter can be determined from available measurements. Two unknown effects may create the same measured output, especially when only torque and speed are logged. Design an independent measurement that distinguishes the competing explanations; when this is impossible, report a bounded family of plausible parameter values rather than a falsely precise single answer. A careful research report can hold two ideas at once: the simplified result is internally correct and it is insufficient for system approval. This is not a weakness of mathematical modeling; it is the reason engineering uses progressive verification against measurements.

### 5. Engineering decision and integration

**Design implication:** Use manufacturer-specified oil requirements and appropriate durability testing. This lesson addresses only one component of the unit's problem: A long-duration duty cycle causes elevated coolant temperature and increasing friction at fixed torque. Changes that look beneficial locally can increase pumping loss, friction, catalyst warm-up time, thermal stress or control complexity elsewhere. Accordingly, the correct engineering decision requires a second comparison at an off-design state and a list of constraints that cannot be traded away. The next simulation or experiment should be chosen to resolve the most consequential unknown, not simply to make the improvement look larger.

A useful extension is to reverse the calculation: choose an output target, estimate the input it would require and then test whether the implied operating point satisfies the engine's load, temperature, fuel and emissions constraints. Reverse calculations frequently uncover impossible combinations that are obscured by forward examples. Record the result as a conditional design feasibility statement, not a claim of guaranteed machine performance.

### 6. Practice and assessment

1. **Conceptual:** Explain why the relation `A simplified film parameter lambda_f = minimum film thickness / composite surface roughness.` is meaningful for this lesson. Name two necessary assumptions and a physical regime in which one fails.
2. **Calculation:** Reproduce and verify the worked case: A 1.5 micrometre film over 0.5 micrometre composite roughness gives a nominal film parameter 3. Show units at every intermediate stage and carry at least one input uncertainty through the output.
3. **Diagnostic:** A team reports a performance improvement after changing one input. Construct an alternative explanation using a measurement error, thermal shift or controller response. What single observation would discriminate between them?
4. **Design:** In the case “A long-duration duty cycle causes elevated coolant temperature and increasing friction at fixed torque.”, propose one legitimate design change and one nonnegotiable constraint. Use manufacturer-specified oil requirements and appropriate durability testing.
5. **Research practice:** Give a file naming and metadata convention that would allow another student to reproduce the analysis, including configuration, units and calibration state.

**Worked-answer checking guide.** For question 2, the reference result is described in the assumed numerical case; a correct submission must also specify the formula, the explicit units and the idealizations. For question 3, credit is earned for a falsifiable alternative mechanism and a measurement that can separate it from the original claim. For question 4, a design that ignores the nonnegotiable constraint is rejected even if its calculated objective improves.

**Further investigation.** Repeat the reasoning at two additional operating points: lower speed and higher intake temperature, or cold start and warmed-up operation where relevant. Describe why the same input perturbation might have a different result under those conditions. Decide which hypothesis can be evaluated safely using the offline numerical model and which requires qualified laboratory equipment.



---

# Internal Combustion Engines — U06-L03


## U06-L03 — Mechanical friction and friction mean effective pressure

**Learning target.** At the end of this lesson, a reader should interpret the governing relation, reproduce a worked estimate, identify the limiting assumption and plan an independent verification of the engineering claim.

### 1. Physical question and context

A defensible treatment of **mechanical friction and friction mean effective pressure** begins by separating observable behavior from explanatory mechanism. Moving components consume indicated work before it reaches the brake shaft. In an internal combustion engine this distinction is especially important because the same output can be produced by changes in fueling, volumetric efficiency, combustion phase, wall heat transfer or mechanical loss. The lesson therefore treats a compact formula as a hypothesis to be tested, not as an exact engine description.

### 2. Governing calculation and its domain

The working relation used here is `FMEP = IMEP - BMEP with a consistent four-stroke-cycle definition.`. Define every variable before substitution, keep a single system of units, and check whether its result should increase or decrease when an input changes. Ask which assumptions make the expression possible: steady conditions, a perfect gas, constant properties, a lumped state, negligible pressure loss or an ideal mechanical linkage may be necessary. If an assumption does not hold in the intended application, identify the direction of the expected deviation when physics permits. When that direction is not clear, do not guess; schedule a measurement or use a higher-fidelity calculation.

**Assumed numerical case:** If IMEP=12 bar and BMEP=9.5 bar, FMEP is 2.5 bar.

**Calculation walkthrough:** With IMEP=12 bar and BMEP=9.5 bar on matching cycles and displacement, the estimated friction mean effective pressure is 2.5 bar. If the pressure analysis and shaft test refer to different load conditions, subtracting them would be meaningless. Also specify whether accessory loads are included in the brake measurement.

The stated values form a hypothetical teaching example and should be recalculated by hand. First write the governing relation, then translate the inputs to SI, then perform substitution before rounding the displayed output. Check the sign and order of magnitude against a physical limiting case. Finally, ask which measured input would dominate an uncertainty interval. A large discrepancy from an independently computed check is grounds to revise the work, not to adjust the accepted answer without explanation.

### 3. Interpret the result, including failures

**Critical interpretation:** Apparent FMEP also absorbs model error in indicated pressure analysis and accessory definitions. A misleading numerical result can arise even when the arithmetic is perfect: the problem may be a wrong system boundary, an inappropriate reference property, a time-averaged signal used for a crank-angle event, or an unrecorded controller response. State which of those failure mechanisms is most likely here. Think about the change that would be observed in cylinder pressure, exhaust temperature, manifold state, or brake output if the explanatory mechanism were genuinely active rather than merely correlated with an unrelated change.

**Time dependence:** Engines operate through rapid events and slowly changing component states simultaneously. A crank-angle snapshot can describe the valve position but not warm-up; an averaged steady flow can describe laboratory demand but hide combustion variability. State the time scale to which each measured quantity belongs before comparing it with a model prediction. Applied to **mechanical friction and friction mean effective pressure**, this discipline helps decide whether the model is a prediction with independent evidence or merely a restatement of its input measurements. Write the most restrictive assumption in the margin of the calculation, then revise the interpretation if that assumption fails under the case-study operating conditions.

### 4. Measurement, uncertainty and experimental integrity

**Measurement and evidence plan:** Perform instrumented indicated/brake comparisons at controlled temperature and speed. Before any data are collected, define a consistent sample clock, an equipment configuration record and at least one repeated baseline run. Identify how the instrument is calibrated and what its resolution excludes. Put all conversions in the analysis code rather than transcribing rounded values manually. Where the quantity is derived from several measurements, propagate uncertainty through the formula or use an appropriate perturbation study. A graph should show its reference conditions and measurement units. Unsupported interpolation between sparse engine-map points is not experimental evidence.

**Operating-envelope reasoning:** Any model can look successful at its calibration point. The meaningful question is whether its error stays acceptably small at cold start, hot idle, high load, low ambient pressure, and during rapid change. Define this intended envelope explicitly, keep data from some points for validation, and reject extrapolation outside known physical or measurement limits. A careful research report can hold two ideas at once: the simplified result is internally correct and it is insufficient for system approval. This is not a weakness of mathematical modeling; it is the reason engineering uses progressive verification against measurements.

### 5. Engineering decision and integration

**Design implication:** Compare friction maps instead of extrapolating one warm operating point. This lesson addresses only one component of the unit's problem: A long-duration duty cycle causes elevated coolant temperature and increasing friction at fixed torque. Changes that look beneficial locally can increase pumping loss, friction, catalyst warm-up time, thermal stress or control complexity elsewhere. Accordingly, the correct engineering decision requires a second comparison at an off-design state and a list of constraints that cannot be traded away. The next simulation or experiment should be chosen to resolve the most consequential unknown, not simply to make the improvement look larger.

A useful extension is to reverse the calculation: choose an output target, estimate the input it would require and then test whether the implied operating point satisfies the engine's load, temperature, fuel and emissions constraints. Reverse calculations frequently uncover impossible combinations that are obscured by forward examples. Record the result as a conditional design feasibility statement, not a claim of guaranteed machine performance.

### 6. Practice and assessment

1. **Conceptual:** Explain why the relation `FMEP = IMEP - BMEP with a consistent four-stroke-cycle definition.` is meaningful for this lesson. Name two necessary assumptions and a physical regime in which one fails.
2. **Calculation:** Reproduce and verify the worked case: If IMEP=12 bar and BMEP=9.5 bar, FMEP is 2.5 bar. Show units at every intermediate stage and carry at least one input uncertainty through the output.
3. **Diagnostic:** A team reports a performance improvement after changing one input. Construct an alternative explanation using a measurement error, thermal shift or controller response. What single observation would discriminate between them?
4. **Design:** In the case “A long-duration duty cycle causes elevated coolant temperature and increasing friction at fixed torque.”, propose one legitimate design change and one nonnegotiable constraint. Compare friction maps instead of extrapolating one warm operating point.
5. **Research practice:** Give a file naming and metadata convention that would allow another student to reproduce the analysis, including configuration, units and calibration state.

**Worked-answer checking guide.** For question 2, the reference result is described in the assumed numerical case; a correct submission must also specify the formula, the explicit units and the idealizations. For question 3, credit is earned for a falsifiable alternative mechanism and a measurement that can separate it from the original claim. For question 4, a design that ignores the nonnegotiable constraint is rejected even if its calculated objective improves.

**Further investigation.** Repeat the reasoning at two additional operating points: lower speed and higher intake temperature, or cold start and warmed-up operation where relevant. Describe why the same input perturbation might have a different result under those conditions. Decide which hypothesis can be evaluated safely using the offline numerical model and which requires qualified laboratory equipment.



---

# Internal Combustion Engines — U06-L04


## U06-L04 — Cooling, oil and exhaust thermal systems

**Learning target.** At the end of this lesson, a reader should interpret the governing relation, reproduce a worked estimate, identify the limiting assumption and plan an independent verification of the engineering claim.

### 1. Physical question and context

Begin with the question of what can legitimately be inferred about **cooling, oil and exhaust thermal systems** from a few laboratory numbers. Thermal circuits interact: thermostat behavior, oil viscosity and exhaust catalyst temperature constrain calibrations. The distinction between a physical quantity and a convenient proxy matters because an engine is simultaneously a chemical reactor, a flow machine, a heat exchanger and an oscillating mechanism. A simple classroom calculation is useful when it makes this distinction precise. It becomes dangerous to reasoning when its hidden assumptions are forgotten.

### 2. Governing calculation and its domain

The smallest useful model is `For a lumped thermal mass C_th*dT/dt=Q_in-Q_out.`. Write it first in symbols because symbols expose which quantities are inputs and which are derived. Conduct a dimensional check. For example, an energy rate must have dimensions of power, and a dimensionless efficiency must not quietly carry a pressure unit. Then inspect the limiting cases. A vanishing input, a zero flow or an impossible temperature ratio should trigger a validity warning rather than a numerically polished answer. The equation belongs to the assumptions stated with it, not to every engine.

**Assumed numerical case:** With C_th=20 kJ/K and net heating of 2 kW, the initial ideal rate is 0.1 K/s.

**Calculation walkthrough:** In the simplified lumped model, C_th=20 kJ/K and net heat rate 2 kJ/s give dT/dt = 2/20 = 0.10 K/s initially. This is not an indefinite linear climb: the rejected heat usually increases with temperature, and thermostats or fans switch states. Plotting an initial slope is not a full warm-up model.

The stated values form a hypothetical teaching example and should be recalculated by hand. First write the governing relation, then translate the inputs to SI, then perform substitution before rounding the displayed output. Check the sign and order of magnitude against a physical limiting case. Finally, ask which measured input would dominate an uncertainty interval. A large discrepancy from an independently computed check is grounds to revise the work, not to adjust the accepted answer without explanation.

### 3. Interpret the result, including failures

**Critical interpretation:** Real thermal networks include spatial gradients, delays and nonlinear control. A misleading numerical result can arise even when the arithmetic is perfect: the problem may be a wrong system boundary, an inappropriate reference property, a time-averaged signal used for a crank-angle event, or an unrecorded controller response. State which of those failure mechanisms is most likely here. Think about the change that would be observed in cylinder pressure, exhaust temperature, manifold state, or brake output if the explanatory mechanism were genuinely active rather than merely correlated with an unrelated change.

**Experimental identifiability:** A neat equation does not imply that each parameter can be determined from available measurements. Two unknown effects may create the same measured output, especially when only torque and speed are logged. Design an independent measurement that distinguishes the competing explanations; when this is impossible, report a bounded family of plausible parameter values rather than a falsely precise single answer. Applied to **cooling, oil and exhaust thermal systems**, this discipline helps decide whether the model is a prediction with independent evidence or merely a restatement of its input measurements. Write the most restrictive assumption in the margin of the calculation, then revise the interpretation if that assumption fails under the case-study operating conditions.

### 4. Measurement, uncertainty and experimental integrity

**Measurement and evidence plan:** Log multiple temperatures across a controlled load step and fit response times. Before any data are collected, define a consistent sample clock, an equipment configuration record and at least one repeated baseline run. Identify how the instrument is calibrated and what its resolution excludes. Put all conversions in the analysis code rather than transcribing rounded values manually. Where the quantity is derived from several measurements, propagate uncertainty through the formula or use an appropriate perturbation study. A graph should show its reference conditions and measurement units. Unsupported interpolation between sparse engine-map points is not experimental evidence.

**Conservation audit:** Start by marking the system boundary on a sketch. Separate fuel energy entering the cylinder from indicated work on the piston and brake work at the shaft. A computed improvement that violates energy conservation is a mistake, not a new engine phenomenon. Where an experimental result seems to contradict the calculation, investigate calibration, hidden storage, auxiliary loads and the interpretation of reference conditions before adding complexity to the model. A careful research report can hold two ideas at once: the simplified result is internally correct and it is insufficient for system approval. This is not a weakness of mathematical modeling; it is the reason engineering uses progressive verification against measurements.

### 5. Engineering decision and integration

**Design implication:** A thermal protection strategy must handle warm-up and sustained operation separately. This lesson addresses only one component of the unit's problem: A long-duration duty cycle causes elevated coolant temperature and increasing friction at fixed torque. Changes that look beneficial locally can increase pumping loss, friction, catalyst warm-up time, thermal stress or control complexity elsewhere. Accordingly, the correct engineering decision requires a second comparison at an off-design state and a list of constraints that cannot be traded away. The next simulation or experiment should be chosen to resolve the most consequential unknown, not simply to make the improvement look larger.

A useful extension is to reverse the calculation: choose an output target, estimate the input it would require and then test whether the implied operating point satisfies the engine's load, temperature, fuel and emissions constraints. Reverse calculations frequently uncover impossible combinations that are obscured by forward examples. Record the result as a conditional design feasibility statement, not a claim of guaranteed machine performance.

### 6. Practice and assessment

1. **Conceptual:** Explain why the relation `For a lumped thermal mass C_th*dT/dt=Q_in-Q_out.` is meaningful for this lesson. Name two necessary assumptions and a physical regime in which one fails.
2. **Calculation:** Reproduce and verify the worked case: With C_th=20 kJ/K and net heating of 2 kW, the initial ideal rate is 0.1 K/s. Show units at every intermediate stage and carry at least one input uncertainty through the output.
3. **Diagnostic:** A team reports a performance improvement after changing one input. Construct an alternative explanation using a measurement error, thermal shift or controller response. What single observation would discriminate between them?
4. **Design:** In the case “A long-duration duty cycle causes elevated coolant temperature and increasing friction at fixed torque.”, propose one legitimate design change and one nonnegotiable constraint. A thermal protection strategy must handle warm-up and sustained operation separately.
5. **Research practice:** Give a file naming and metadata convention that would allow another student to reproduce the analysis, including configuration, units and calibration state.

**Worked-answer checking guide.** For question 2, the reference result is described in the assumed numerical case; a correct submission must also specify the formula, the explicit units and the idealizations. For question 3, credit is earned for a falsifiable alternative mechanism and a measurement that can separate it from the original claim. For question 4, a design that ignores the nonnegotiable constraint is rejected even if its calculated objective improves.

**Further investigation.** Repeat the reasoning at two additional operating points: lower speed and higher intake temperature, or cold start and warmed-up operation where relevant. Describe why the same input perturbation might have a different result under those conditions. Decide which hypothesis can be evaluated safely using the offline numerical model and which requires qualified laboratory equipment.



---

# Internal Combustion Engines — U06-L05


## U06-L05 — Fatigue, wear, diagnostics and reliability growth

**Learning target.** At the end of this lesson, a reader should interpret the governing relation, reproduce a worked estimate, identify the limiting assumption and plan an independent verification of the engineering claim.

### 1. Physical question and context

Consider an engineer who is evaluating **fatigue, wear, diagnostics and reliability growth** in the following setting: A long-duration duty cycle causes elevated coolant temperature and increasing friction at fixed torque. The analytical priority is not to maximize the number of equations. It is to identify the correct conserved quantity, select a boundary and state the outcome that the instrument or simulation actually reports. Thermal cycling, contact stresses, deposits and vibration lead to multiple interacting degradation mechanisms. Two measurements that share a unit may still refer to different control volumes, time windows or reference states.

### 2. Governing calculation and its domain

Use `A simple Miner sum D = sum(n_i/N_i) is an empirical screening tool for fatigue.` as the initial closure relation. It is tempting to interpret the number as a design guarantee; instead define a reference operating point, perturb each independent input separately and observe the output response. Check whether apparently independent variables are actually correlated by conservation or control logic. Treat a high-sensitivity variable as a candidate for better measurement. If the result requires a parameter measured by the same output that is being predicted, the model is partly circular and its validation requires an independent observation.

**Assumed numerical case:** A block with 10000 cycles at a nominal endurance of 100000 gives damage fraction 0.1.

**Calculation walkthrough:** For a load block with 10,000 cycles applied and a nominal constant-amplitude life of 100,000 cycles, the linear damage fraction is 0.10. Ten identical such blocks would sum to one within the model. Sequence effects, lubricating film changes and corrosion can invalidate this simple addition, so it is a screening estimate rather than a certified life prediction.

The stated values form a hypothetical teaching example and should be recalculated by hand. First write the governing relation, then translate the inputs to SI, then perform substitution before rounding the displayed output. Check the sign and order of magnitude against a physical limiting case. Finally, ask which measured input would dominate an uncertainty interval. A large discrepancy from an independently computed check is grounds to revise the work, not to adjust the accepted answer without explanation.

### 3. Interpret the result, including failures

**Critical interpretation:** Linear damage accumulation does not capture corrosion, overload order or lubrication collapse. A misleading numerical result can arise even when the arithmetic is perfect: the problem may be a wrong system boundary, an inappropriate reference property, a time-averaged signal used for a crank-angle event, or an unrecorded controller response. State which of those failure mechanisms is most likely here. Think about the change that would be observed in cylinder pressure, exhaust temperature, manifold state, or brake output if the explanatory mechanism were genuinely active rather than merely correlated with an unrelated change.

**Operating-envelope reasoning:** Any model can look successful at its calibration point. The meaningful question is whether its error stays acceptably small at cold start, hot idle, high load, low ambient pressure, and during rapid change. Define this intended envelope explicitly, keep data from some points for validation, and reject extrapolation outside known physical or measurement limits. Applied to **fatigue, wear, diagnostics and reliability growth**, this discipline helps decide whether the model is a prediction with independent evidence or merely a restatement of its input measurements. Write the most restrictive assumption in the margin of the calculation, then revise the interpretation if that assumption fails under the case-study operating conditions.

### 4. Measurement, uncertainty and experimental integrity

**Measurement and evidence plan:** Use teardown, wear measurement, trend statistics and controlled endurance protocols. Before any data are collected, define a consistent sample clock, an equipment configuration record and at least one repeated baseline run. Identify how the instrument is calibrated and what its resolution excludes. Put all conversions in the analysis code rather than transcribing rounded values manually. Where the quantity is derived from several measurements, propagate uncertainty through the formula or use an appropriate perturbation study. A graph should show its reference conditions and measurement units. Unsupported interpolation between sparse engine-map points is not experimental evidence.

**Scale and sensitivity:** Scaling a geometric or thermal parameter is not a free performance gain. With every scale change, ask which transport time, stress, temperature, pressure ratio or nondimensional group changes with it. If the underlying response is nonlinear, quote a local sensitivity around the stated operating point instead of applying a single proportional rule across an engine map. A careful research report can hold two ideas at once: the simplified result is internally correct and it is insufficient for system approval. This is not a weakness of mathematical modeling; it is the reason engineering uses progressive verification against measurements.

### 5. Engineering decision and integration

**Design implication:** Never infer lifetime certification from a brief synthetic acceleration test. This lesson addresses only one component of the unit's problem: A long-duration duty cycle causes elevated coolant temperature and increasing friction at fixed torque. Changes that look beneficial locally can increase pumping loss, friction, catalyst warm-up time, thermal stress or control complexity elsewhere. Accordingly, the correct engineering decision requires a second comparison at an off-design state and a list of constraints that cannot be traded away. The next simulation or experiment should be chosen to resolve the most consequential unknown, not simply to make the improvement look larger.

A useful extension is to reverse the calculation: choose an output target, estimate the input it would require and then test whether the implied operating point satisfies the engine's load, temperature, fuel and emissions constraints. Reverse calculations frequently uncover impossible combinations that are obscured by forward examples. Record the result as a conditional design feasibility statement, not a claim of guaranteed machine performance.

### 6. Practice and assessment

1. **Conceptual:** Explain why the relation `A simple Miner sum D = sum(n_i/N_i) is an empirical screening tool for fatigue.` is meaningful for this lesson. Name two necessary assumptions and a physical regime in which one fails.
2. **Calculation:** Reproduce and verify the worked case: A block with 10000 cycles at a nominal endurance of 100000 gives damage fraction 0.1. Show units at every intermediate stage and carry at least one input uncertainty through the output.
3. **Diagnostic:** A team reports a performance improvement after changing one input. Construct an alternative explanation using a measurement error, thermal shift or controller response. What single observation would discriminate between them?
4. **Design:** In the case “A long-duration duty cycle causes elevated coolant temperature and increasing friction at fixed torque.”, propose one legitimate design change and one nonnegotiable constraint. Never infer lifetime certification from a brief synthetic acceleration test.
5. **Research practice:** Give a file naming and metadata convention that would allow another student to reproduce the analysis, including configuration, units and calibration state.

**Worked-answer checking guide.** For question 2, the reference result is described in the assumed numerical case; a correct submission must also specify the formula, the explicit units and the idealizations. For question 3, credit is earned for a falsifiable alternative mechanism and a measurement that can separate it from the original claim. For question 4, a design that ignores the nonnegotiable constraint is rejected even if its calculated objective improves.

**Further investigation.** Repeat the reasoning at two additional operating points: lower speed and higher intake temperature, or cold start and warmed-up operation where relevant. Describe why the same input perturbation might have a different result under those conditions. Decide which hypothesis can be evaluated safely using the offline numerical model and which requires qualified laboratory equipment.



---

