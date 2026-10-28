# Unit 02: Ideal Cycles, Real Cycles and Thermodynamic Limits

**Course Code**: ICE 202 · **Level**: Advanced Undergraduate Engineering

## Unit Overview & Physical Foundations

This comprehensive university textbook unit covers the theoretical framework, physical modeling, mathematical governing equations, and engineering applications of **Ideal Cycles, Real Cycles and Thermodynamic Limits**.

# Internal Combustion Engines — U02-L01


## U02-L01 — Closed-system energy balances

**Learning target.** At the end of this lesson, a reader should interpret the governing relation, reproduce a worked estimate, identify the limiting assumption and plan an independent verification of the engineering claim.

### 1. Physical question and context

Consider an engineer who is evaluating **closed-system energy balances** in the following setting: An engineer compares compression-ratio changes against fuel economy, peak temperature and knock risk. The analytical priority is not to maximize the number of equations. It is to identify the correct conserved quantity, select a boundary and state the outcome that the instrument or simulation actually reports. Ideal cycle analysis requires explicit system boundaries and internally consistent sign conventions. Two measurements that share a unit may still refer to different control volumes, time windows or reference states.

### 2. Governing calculation and its domain

Use `For a closed cycle Delta U = Q_in - W_out; over a full cycle Delta U is zero.` as the initial closure relation. It is tempting to interpret the number as a design guarantee; instead define a reference operating point, perturb each independent input separately and observe the output response. Check whether apparently independent variables are actually correlated by conservation or control logic. Treat a high-sensitivity variable as a candidate for better measurement. If the result requires a parameter measured by the same output that is being predicted, the model is partly circular and its validation requires an independent observation.

**Assumed numerical case:** If a closed ideal cycle receives 800 J and rejects 480 J, the ideal net work is 320 J.

**Calculation walkthrough:** For one full cycle the closed-system internal energy returns to its initial value. From 0 = Q_in − Q_out − W_net, obtain W_net = 800 − 480 = 320 J. The ideal cycle efficiency is 320/800 = 0.40, or 40%. Real combustion energy and real heat rejection require different measurement boundaries.

The stated values form a hypothetical teaching example and should be recalculated by hand. First write the governing relation, then translate the inputs to SI, then perform substitution before rounding the displayed output. Check the sign and order of magnitude against a physical limiting case. Finally, ask which measured input would dominate an uncertainty interval. A large discrepancy from an independently computed check is grounds to revise the work, not to adjust the accepted answer without explanation.

### 3. Interpret the result, including failures

**Critical interpretation:** The ideal heat addition is not identical to chemical energy release in an actual cylinder. A misleading numerical result can arise even when the arithmetic is perfect: the problem may be a wrong system boundary, an inappropriate reference property, a time-averaged signal used for a crank-angle event, or an unrecorded controller response. State which of those failure mechanisms is most likely here. Think about the change that would be observed in cylinder pressure, exhaust temperature, manifold state, or brake output if the explanatory mechanism were genuinely active rather than merely correlated with an unrelated change.

**Conservation audit:** Start by marking the system boundary on a sketch. Separate fuel energy entering the cylinder from indicated work on the piston and brake work at the shaft. A computed improvement that violates energy conservation is a mistake, not a new engine phenomenon. Where an experimental result seems to contradict the calculation, investigate calibration, hidden storage, auxiliary loads and the interpretation of reference conditions before adding complexity to the model. Applied to **closed-system energy balances**, this discipline helps decide whether the model is a prediction with independent evidence or merely a restatement of its input measurements. Write the most restrictive assumption in the margin of the calculation, then revise the interpretation if that assumption fails under the case-study operating conditions.

### 4. Measurement, uncertainty and experimental integrity

**Measurement and evidence plan:** Draw each state boundary and audit the integrated p-V loop for consistent work signs. Before any data are collected, define a consistent sample clock, an equipment configuration record and at least one repeated baseline run. Identify how the instrument is calibrated and what its resolution excludes. Put all conversions in the analysis code rather than transcribing rounded values manually. Where the quantity is derived from several measurements, propagate uncertainty through the formula or use an appropriate perturbation study. A graph should show its reference conditions and measurement units. Unsupported interpolation between sparse engine-map points is not experimental evidence.

**Time dependence:** Engines operate through rapid events and slowly changing component states simultaneously. A crank-angle snapshot can describe the valve position but not warm-up; an averaged steady flow can describe laboratory demand but hide combustion variability. State the time scale to which each measured quantity belongs before comparing it with a model prediction. A careful research report can hold two ideas at once: the simplified result is internally correct and it is insufficient for system approval. This is not a weakness of mathematical modeling; it is the reason engineering uses progressive verification against measurements.

### 5. Engineering decision and integration

**Design implication:** Reject model results that violate energy conservation before pursuing calibration changes. This lesson addresses only one component of the unit's problem: An engineer compares compression-ratio changes against fuel economy, peak temperature and knock risk. Changes that look beneficial locally can increase pumping loss, friction, catalyst warm-up time, thermal stress or control complexity elsewhere. Accordingly, the correct engineering decision requires a second comparison at an off-design state and a list of constraints that cannot be traded away. The next simulation or experiment should be chosen to resolve the most consequential unknown, not simply to make the improvement look larger.

A useful extension is to reverse the calculation: choose an output target, estimate the input it would require and then test whether the implied operating point satisfies the engine's load, temperature, fuel and emissions constraints. Reverse calculations frequently uncover impossible combinations that are obscured by forward examples. Record the result as a conditional design feasibility statement, not a claim of guaranteed machine performance.

### 6. Practice and assessment

1. **Conceptual:** Explain why the relation `For a closed cycle Delta U = Q_in - W_out; over a full cycle Delta U is zero.` is meaningful for this lesson. Name two necessary assumptions and a physical regime in which one fails.
2. **Calculation:** Reproduce and verify the worked case: If a closed ideal cycle receives 800 J and rejects 480 J, the ideal net work is 320 J. Show units at every intermediate stage and carry at least one input uncertainty through the output.
3. **Diagnostic:** A team reports a performance improvement after changing one input. Construct an alternative explanation using a measurement error, thermal shift or controller response. What single observation would discriminate between them?
4. **Design:** In the case “An engineer compares compression-ratio changes against fuel economy, peak temperature and knock risk.”, propose one legitimate design change and one nonnegotiable constraint. Reject model results that violate energy conservation before pursuing calibration changes.
5. **Research practice:** Give a file naming and metadata convention that would allow another student to reproduce the analysis, including configuration, units and calibration state.

**Worked-answer checking guide.** For question 2, the reference result is described in the assumed numerical case; a correct submission must also specify the formula, the explicit units and the idealizations. For question 3, credit is earned for a falsifiable alternative mechanism and a measurement that can separate it from the original claim. For question 4, a design that ignores the nonnegotiable constraint is rejected even if its calculated objective improves.

**Further investigation.** Repeat the reasoning at two additional operating points: lower speed and higher intake temperature, or cold start and warmed-up operation where relevant. Describe why the same input perturbation might have a different result under those conditions. Decide which hypothesis can be evaluated safely using the offline numerical model and which requires qualified laboratory equipment.



---

# Internal Combustion Engines — U02-L02


## U02-L02 — Otto-cycle compression and expansion

**Learning target.** At the end of this lesson, a reader should interpret the governing relation, reproduce a worked estimate, identify the limiting assumption and plan an independent verification of the engineering claim.

### 1. Physical question and context

The central issue in **otto-cycle compression and expansion** is not memorizing a formula but knowing when its use is justified. The constant-volume heat-addition cycle isolates how isentropic compression ratio affects ideal efficiency. A model's apparent precision depends on measurement resolution, parameter provenance and the operating envelope. At the outset specify whether a statement refers to a single cylinder, all cylinders, indicated work, brake shaft work, intake flow or exhaust flow. Changing that definition silently can invalidate a numerical answer while leaving its arithmetic flawless.

### 2. Governing calculation and its domain

The working relation used here is `eta_Otto = 1 - r_c^(1-gamma) for constant gamma and ideal gas.`. Define every variable before substitution, keep a single system of units, and check whether its result should increase or decrease when an input changes. Ask which assumptions make the expression possible: steady conditions, a perfect gas, constant properties, a lumped state, negligible pressure loss or an ideal mechanical linkage may be necessary. If an assumption does not hold in the intended application, identify the direction of the expected deviation when physics permits. When that direction is not clear, do not guess; schedule a measurement or use a higher-fidelity calculation.

**Assumed numerical case:** For r_c=10 and gamma=1.4, eta is about 60.2% in the air-standard model.

**Calculation walkthrough:** For compression ratio r=10 and γ=1.4, use η = 1 − 1/10^0.4. Because 10^0.4 ≈ 2.5119, η ≈ 1 − 0.3981 = 0.6019 or 60.19%. The result is an ideal air-standard sensitivity estimate; it cannot be read as a measured brake thermal efficiency.

The stated values form a hypothetical teaching example and should be recalculated by hand. First write the governing relation, then translate the inputs to SI, then perform substitution before rounding the displayed output. Check the sign and order of magnitude against a physical limiting case. Finally, ask which measured input would dominate an uncertainty interval. A large discrepancy from an independently computed check is grounds to revise the work, not to adjust the accepted answer without explanation.

### 3. Interpret the result, including failures

**Critical interpretation:** Actual brake efficiency is lower because combustion, heat transfer, pumping and friction are omitted. A misleading numerical result can arise even when the arithmetic is perfect: the problem may be a wrong system boundary, an inappropriate reference property, a time-averaged signal used for a crank-angle event, or an unrecorded controller response. State which of those failure mechanisms is most likely here. Think about the change that would be observed in cylinder pressure, exhaust temperature, manifold state, or brake output if the explanatory mechanism were genuinely active rather than merely correlated with an unrelated change.

**Scale and sensitivity:** Scaling a geometric or thermal parameter is not a free performance gain. With every scale change, ask which transport time, stress, temperature, pressure ratio or nondimensional group changes with it. If the underlying response is nonlinear, quote a local sensitivity around the stated operating point instead of applying a single proportional rule across an engine map. Applied to **otto-cycle compression and expansion**, this discipline helps decide whether the model is a prediction with independent evidence or merely a restatement of its input measurements. Write the most restrictive assumption in the margin of the calculation, then revise the interpretation if that assumption fails under the case-study operating conditions.

### 4. Measurement, uncertainty and experimental integrity

**Measurement and evidence plan:** Compare the analytic expression with a numerically integrated four-state ideal p-V loop. Before any data are collected, define a consistent sample clock, an equipment configuration record and at least one repeated baseline run. Identify how the instrument is calibrated and what its resolution excludes. Put all conversions in the analysis code rather than transcribing rounded values manually. Where the quantity is derived from several measurements, propagate uncertainty through the formula or use an appropriate perturbation study. A graph should show its reference conditions and measurement units. Unsupported interpolation between sparse engine-map points is not experimental evidence.

**Experimental identifiability:** A neat equation does not imply that each parameter can be determined from available measurements. Two unknown effects may create the same measured output, especially when only torque and speed are logged. Design an independent measurement that distinguishes the competing explanations; when this is impossible, report a bounded family of plausible parameter values rather than a falsely precise single answer. A careful research report can hold two ideas at once: the simplified result is internally correct and it is insufficient for system approval. This is not a weakness of mathematical modeling; it is the reason engineering uses progressive verification against measurements.

### 5. Engineering decision and integration

**Design implication:** Use the result to reason about sensitivity, not to predict a production-engine fuel bill. This lesson addresses only one component of the unit's problem: An engineer compares compression-ratio changes against fuel economy, peak temperature and knock risk. Changes that look beneficial locally can increase pumping loss, friction, catalyst warm-up time, thermal stress or control complexity elsewhere. Accordingly, the correct engineering decision requires a second comparison at an off-design state and a list of constraints that cannot be traded away. The next simulation or experiment should be chosen to resolve the most consequential unknown, not simply to make the improvement look larger.

A useful extension is to reverse the calculation: choose an output target, estimate the input it would require and then test whether the implied operating point satisfies the engine's load, temperature, fuel and emissions constraints. Reverse calculations frequently uncover impossible combinations that are obscured by forward examples. Record the result as a conditional design feasibility statement, not a claim of guaranteed machine performance.

### 6. Practice and assessment

1. **Conceptual:** Explain why the relation `eta_Otto = 1 - r_c^(1-gamma) for constant gamma and ideal gas.` is meaningful for this lesson. Name two necessary assumptions and a physical regime in which one fails.
2. **Calculation:** Reproduce and verify the worked case: For r_c=10 and gamma=1.4, eta is about 60.2% in the air-standard model. Show units at every intermediate stage and carry at least one input uncertainty through the output.
3. **Diagnostic:** A team reports a performance improvement after changing one input. Construct an alternative explanation using a measurement error, thermal shift or controller response. What single observation would discriminate between them?
4. **Design:** In the case “An engineer compares compression-ratio changes against fuel economy, peak temperature and knock risk.”, propose one legitimate design change and one nonnegotiable constraint. Use the result to reason about sensitivity, not to predict a production-engine fuel bill.
5. **Research practice:** Give a file naming and metadata convention that would allow another student to reproduce the analysis, including configuration, units and calibration state.

**Worked-answer checking guide.** For question 2, the reference result is described in the assumed numerical case; a correct submission must also specify the formula, the explicit units and the idealizations. For question 3, credit is earned for a falsifiable alternative mechanism and a measurement that can separate it from the original claim. For question 4, a design that ignores the nonnegotiable constraint is rejected even if its calculated objective improves.

**Further investigation.** Repeat the reasoning at two additional operating points: lower speed and higher intake temperature, or cold start and warmed-up operation where relevant. Describe why the same input perturbation might have a different result under those conditions. Decide which hypothesis can be evaluated safely using the offline numerical model and which requires qualified laboratory equipment.



---

# Internal Combustion Engines — U02-L03


## U02-L03 — Diesel-cycle cutoff ratio and heat addition

**Learning target.** At the end of this lesson, a reader should interpret the governing relation, reproduce a worked estimate, identify the limiting assumption and plan an independent verification of the engineering claim.

### 1. Physical question and context

A defensible treatment of **diesel-cycle cutoff ratio and heat addition** begins by separating observable behavior from explanatory mechanism. Heat addition at nominally constant pressure gives a different idealized thermodynamic path. In an internal combustion engine this distinction is especially important because the same output can be produced by changes in fueling, volumetric efficiency, combustion phase, wall heat transfer or mechanical loss. The lesson therefore treats a compact formula as a hypothesis to be tested, not as an exact engine description.

### 2. Governing calculation and its domain

The smallest useful model is `eta_Diesel=1-(1/r_c^(gamma-1))*((rho^gamma-1)/(gamma*(rho-1))).`. Write it first in symbols because symbols expose which quantities are inputs and which are derived. Conduct a dimensional check. For example, an energy rate must have dimensions of power, and a dimensionless efficiency must not quietly carry a pressure unit. Then inspect the limiting cases. A vanishing input, a zero flow or an impossible temperature ratio should trigger a validity warning rather than a numerically polished answer. The equation belongs to the assumptions stated with it, not to every engine.

**Assumed numerical case:** At fixed compression ratio, a larger ideal cutoff ratio generally reduces efficiency in this simple model.

**Calculation walkthrough:** Consider the air-standard relation at r=17, γ=1.4 and cutoff ρ=2. The compression factor is 17^0.4 ≈ 3.106, while the heat-addition factor is (2^1.4−1)/(1.4×(2−1)) ≈ 1.1708. Hence η ≈ 1 − 1.1708/3.106 ≈ 0.623. Compare another cutoff at the same compression ratio rather than changing two assumptions at once.

The stated values form a hypothetical teaching example and should be recalculated by hand. First write the governing relation, then translate the inputs to SI, then perform substitution before rounding the displayed output. Check the sign and order of magnitude against a physical limiting case. Finally, ask which measured input would dominate an uncertainty interval. A large discrepancy from an independently computed check is grounds to revise the work, not to adjust the accepted answer without explanation.

### 3. Interpret the result, including failures

**Critical interpretation:** Real compression-ignition heat release is not constant-pressure and is shaped by mixing. A misleading numerical result can arise even when the arithmetic is perfect: the problem may be a wrong system boundary, an inappropriate reference property, a time-averaged signal used for a crank-angle event, or an unrecorded controller response. State which of those failure mechanisms is most likely here. Think about the change that would be observed in cylinder pressure, exhaust temperature, manifold state, or brake output if the explanatory mechanism were genuinely active rather than merely correlated with an unrelated change.

**Time dependence:** Engines operate through rapid events and slowly changing component states simultaneously. A crank-angle snapshot can describe the valve position but not warm-up; an averaged steady flow can describe laboratory demand but hide combustion variability. State the time scale to which each measured quantity belongs before comparing it with a model prediction. Applied to **diesel-cycle cutoff ratio and heat addition**, this discipline helps decide whether the model is a prediction with independent evidence or merely a restatement of its input measurements. Write the most restrictive assumption in the margin of the calculation, then revise the interpretation if that assumption fails under the case-study operating conditions.

### 4. Measurement, uncertainty and experimental integrity

**Measurement and evidence plan:** Plot pressure and volume with matched compression ratio and gamma for both ideal cycles. Before any data are collected, define a consistent sample clock, an equipment configuration record and at least one repeated baseline run. Identify how the instrument is calibrated and what its resolution excludes. Put all conversions in the analysis code rather than transcribing rounded values manually. Where the quantity is derived from several measurements, propagate uncertainty through the formula or use an appropriate perturbation study. A graph should show its reference conditions and measurement units. Unsupported interpolation between sparse engine-map points is not experimental evidence.

**Operating-envelope reasoning:** Any model can look successful at its calibration point. The meaningful question is whether its error stays acceptably small at cold start, hot idle, high load, low ambient pressure, and during rapid change. Define this intended envelope explicitly, keep data from some points for validation, and reject extrapolation outside known physical or measurement limits. A careful research report can hold two ideas at once: the simplified result is internally correct and it is insufficient for system approval. This is not a weakness of mathematical modeling; it is the reason engineering uses progressive verification against measurements.

### 5. Engineering decision and integration

**Design implication:** Avoid treating ideal Otto versus Diesel efficiency as a ranking of commercial engines. This lesson addresses only one component of the unit's problem: An engineer compares compression-ratio changes against fuel economy, peak temperature and knock risk. Changes that look beneficial locally can increase pumping loss, friction, catalyst warm-up time, thermal stress or control complexity elsewhere. Accordingly, the correct engineering decision requires a second comparison at an off-design state and a list of constraints that cannot be traded away. The next simulation or experiment should be chosen to resolve the most consequential unknown, not simply to make the improvement look larger.

A useful extension is to reverse the calculation: choose an output target, estimate the input it would require and then test whether the implied operating point satisfies the engine's load, temperature, fuel and emissions constraints. Reverse calculations frequently uncover impossible combinations that are obscured by forward examples. Record the result as a conditional design feasibility statement, not a claim of guaranteed machine performance.

### 6. Practice and assessment

1. **Conceptual:** Explain why the relation `eta_Diesel=1-(1/r_c^(gamma-1))*((rho^gamma-1)/(gamma*(rho-1))).` is meaningful for this lesson. Name two necessary assumptions and a physical regime in which one fails.
2. **Calculation:** Reproduce and verify the worked case: At fixed compression ratio, a larger ideal cutoff ratio generally reduces efficiency in this simple model. Show units at every intermediate stage and carry at least one input uncertainty through the output.
3. **Diagnostic:** A team reports a performance improvement after changing one input. Construct an alternative explanation using a measurement error, thermal shift or controller response. What single observation would discriminate between them?
4. **Design:** In the case “An engineer compares compression-ratio changes against fuel economy, peak temperature and knock risk.”, propose one legitimate design change and one nonnegotiable constraint. Avoid treating ideal Otto versus Diesel efficiency as a ranking of commercial engines.
5. **Research practice:** Give a file naming and metadata convention that would allow another student to reproduce the analysis, including configuration, units and calibration state.

**Worked-answer checking guide.** For question 2, the reference result is described in the assumed numerical case; a correct submission must also specify the formula, the explicit units and the idealizations. For question 3, credit is earned for a falsifiable alternative mechanism and a measurement that can separate it from the original claim. For question 4, a design that ignores the nonnegotiable constraint is rejected even if its calculated objective improves.

**Further investigation.** Repeat the reasoning at two additional operating points: lower speed and higher intake temperature, or cold start and warmed-up operation where relevant. Describe why the same input perturbation might have a different result under those conditions. Decide which hypothesis can be evaluated safely using the offline numerical model and which requires qualified laboratory equipment.



---

# Internal Combustion Engines — U02-L04


## U02-L04 — Air-standard versus fuel-air cycle assumptions

**Learning target.** At the end of this lesson, a reader should interpret the governing relation, reproduce a worked estimate, identify the limiting assumption and plan an independent verification of the engineering claim.

### 1. Physical question and context

Begin with the question of what can legitimately be inferred about **air-standard versus fuel-air cycle assumptions** from a few laboratory numbers. Temperature-dependent heat capacities and changing composition alter heat addition and compression estimates. The distinction between a physical quantity and a convenient proxy matters because an engine is simultaneously a chemical reactor, a flow machine, a heat exchanger and an oscillating mechanism. A simple classroom calculation is useful when it makes this distinction precise. It becomes dangerous to reasoning when its hidden assumptions are forgotten.

### 2. Governing calculation and its domain

Use `For ideal gas mixtures, Delta h = integral cp(T,composition) dT.` as the initial closure relation. It is tempting to interpret the number as a design guarantee; instead define a reference operating point, perturb each independent input separately and observe the output response. Check whether apparently independent variables are actually correlated by conservation or control logic. Treat a high-sensitivity variable as a candidate for better measurement. If the result requires a parameter measured by the same output that is being predicted, the model is partly circular and its validation requires an independent observation.

**Assumed numerical case:** Holding cp constant through a very large temperature rise can produce appreciable energy error.

**Calculation walkthrough:** For a 100 K heating interval, a constant 1.0 kJ/(kg·K) heat capacity predicts 100 kJ/kg enthalpy rise. If heat capacity varies significantly over that interval, the correct calculation is the area under cp(T): integrate, do not multiply by an arbitrarily chosen endpoint cp. This distinction becomes critical when temperature spans are very large.

The stated values form a hypothetical teaching example and should be recalculated by hand. First write the governing relation, then translate the inputs to SI, then perform substitution before rounding the displayed output. Check the sign and order of magnitude against a physical limiting case. Finally, ask which measured input would dominate an uncertainty interval. A large discrepancy from an independently computed check is grounds to revise the work, not to adjust the accepted answer without explanation.

### 3. Interpret the result, including failures

**Critical interpretation:** Dissociation, residual gas and nonuniformity mean a single gamma is at best a screening parameter. A misleading numerical result can arise even when the arithmetic is perfect: the problem may be a wrong system boundary, an inappropriate reference property, a time-averaged signal used for a crank-angle event, or an unrecorded controller response. State which of those failure mechanisms is most likely here. Think about the change that would be observed in cylinder pressure, exhaust temperature, manifold state, or brake output if the explanatory mechanism were genuinely active rather than merely correlated with an unrelated change.

**Experimental identifiability:** A neat equation does not imply that each parameter can be determined from available measurements. Two unknown effects may create the same measured output, especially when only torque and speed are logged. Design an independent measurement that distinguishes the competing explanations; when this is impossible, report a bounded family of plausible parameter values rather than a falsely precise single answer. Applied to **air-standard versus fuel-air cycle assumptions**, this discipline helps decide whether the model is a prediction with independent evidence or merely a restatement of its input measurements. Write the most restrictive assumption in the margin of the calculation, then revise the interpretation if that assumption fails under the case-study operating conditions.

### 4. Measurement, uncertainty and experimental integrity

**Measurement and evidence plan:** Use property tables or verified thermochemical routines to recalculate representative states. Before any data are collected, define a consistent sample clock, an equipment configuration record and at least one repeated baseline run. Identify how the instrument is calibrated and what its resolution excludes. Put all conversions in the analysis code rather than transcribing rounded values manually. Where the quantity is derived from several measurements, propagate uncertainty through the formula or use an appropriate perturbation study. A graph should show its reference conditions and measurement units. Unsupported interpolation between sparse engine-map points is not experimental evidence.

**Conservation audit:** Start by marking the system boundary on a sketch. Separate fuel energy entering the cylinder from indicated work on the piston and brake work at the shaft. A computed improvement that violates energy conservation is a mistake, not a new engine phenomenon. Where an experimental result seems to contradict the calculation, investigate calibration, hidden storage, auxiliary loads and the interpretation of reference conditions before adding complexity to the model. A careful research report can hold two ideas at once: the simplified result is internally correct and it is insufficient for system approval. This is not a weakness of mathematical modeling; it is the reason engineering uses progressive verification against measurements.

### 5. Engineering decision and integration

**Design implication:** Record the validity temperature range and fuel-air composition with each comparison. This lesson addresses only one component of the unit's problem: An engineer compares compression-ratio changes against fuel economy, peak temperature and knock risk. Changes that look beneficial locally can increase pumping loss, friction, catalyst warm-up time, thermal stress or control complexity elsewhere. Accordingly, the correct engineering decision requires a second comparison at an off-design state and a list of constraints that cannot be traded away. The next simulation or experiment should be chosen to resolve the most consequential unknown, not simply to make the improvement look larger.

A useful extension is to reverse the calculation: choose an output target, estimate the input it would require and then test whether the implied operating point satisfies the engine's load, temperature, fuel and emissions constraints. Reverse calculations frequently uncover impossible combinations that are obscured by forward examples. Record the result as a conditional design feasibility statement, not a claim of guaranteed machine performance.

### 6. Practice and assessment

1. **Conceptual:** Explain why the relation `For ideal gas mixtures, Delta h = integral cp(T,composition) dT.` is meaningful for this lesson. Name two necessary assumptions and a physical regime in which one fails.
2. **Calculation:** Reproduce and verify the worked case: Holding cp constant through a very large temperature rise can produce appreciable energy error. Show units at every intermediate stage and carry at least one input uncertainty through the output.
3. **Diagnostic:** A team reports a performance improvement after changing one input. Construct an alternative explanation using a measurement error, thermal shift or controller response. What single observation would discriminate between them?
4. **Design:** In the case “An engineer compares compression-ratio changes against fuel economy, peak temperature and knock risk.”, propose one legitimate design change and one nonnegotiable constraint. Record the validity temperature range and fuel-air composition with each comparison.
5. **Research practice:** Give a file naming and metadata convention that would allow another student to reproduce the analysis, including configuration, units and calibration state.

**Worked-answer checking guide.** For question 2, the reference result is described in the assumed numerical case; a correct submission must also specify the formula, the explicit units and the idealizations. For question 3, credit is earned for a falsifiable alternative mechanism and a measurement that can separate it from the original claim. For question 4, a design that ignores the nonnegotiable constraint is rejected even if its calculated objective improves.

**Further investigation.** Repeat the reasoning at two additional operating points: lower speed and higher intake temperature, or cold start and warmed-up operation where relevant. Describe why the same input perturbation might have a different result under those conditions. Decide which hypothesis can be evaluated safely using the offline numerical model and which requires qualified laboratory equipment.



---

# Internal Combustion Engines — U02-L05


## U02-L05 — Exergy, irreversibility and real-engine efficiency

**Learning target.** At the end of this lesson, a reader should interpret the governing relation, reproduce a worked estimate, identify the limiting assumption and plan an independent verification of the engineering claim.

### 1. Physical question and context

Consider an engineer who is evaluating **exergy, irreversibility and real-engine efficiency** in the following setting: An engineer compares compression-ratio changes against fuel economy, peak temperature and knock risk. The analytical priority is not to maximize the number of equations. It is to identify the correct conserved quantity, select a boundary and state the outcome that the instrument or simulation actually reports. The second law distinguishes where energy is transferred from where useful work potential is destroyed. Two measurements that share a unit may still refer to different control volumes, time windows or reference states.

### 2. Governing calculation and its domain

The working relation used here is `Exergy destruction = T_0 * S_generated for a fixed environmental reference temperature.`. Define every variable before substitution, keep a single system of units, and check whether its result should increase or decrease when an input changes. Ask which assumptions make the expression possible: steady conditions, a perfect gas, constant properties, a lumped state, negligible pressure loss or an ideal mechanical linkage may be necessary. If an assumption does not hold in the intended application, identify the direction of the expected deviation when physics permits. When that direction is not clear, do not guess; schedule a measurement or use a higher-fidelity calculation.

**Assumed numerical case:** An entropy generation of 0.20 kJ/K at T0=300 K corresponds to 60 kJ destroyed exergy.

**Calculation walkthrough:** The destruction relation has the structure I = T0 S_gen. At 300 K reference temperature and 0.20 kJ/K entropy generation, I = 60 kJ. Energy was not destroyed; the capability to convert it into useful work was reduced. The reference environment must be stated or two exergy calculations may disagree while both are internally consistent.

The stated values form a hypothetical teaching example and should be recalculated by hand. First write the governing relation, then translate the inputs to SI, then perform substitution before rounding the displayed output. Check the sign and order of magnitude against a physical limiting case. Finally, ask which measured input would dominate an uncertainty interval. A large discrepancy from an independently computed check is grounds to revise the work, not to adjust the accepted answer without explanation.

### 3. Interpret the result, including failures

**Critical interpretation:** Lost work cannot always be recovered by simply adding a bigger heat exchanger. A misleading numerical result can arise even when the arithmetic is perfect: the problem may be a wrong system boundary, an inappropriate reference property, a time-averaged signal used for a crank-angle event, or an unrecorded controller response. State which of those failure mechanisms is most likely here. Think about the change that would be observed in cylinder pressure, exhaust temperature, manifold state, or brake output if the explanatory mechanism were genuinely active rather than merely correlated with an unrelated change.

**Operating-envelope reasoning:** Any model can look successful at its calibration point. The meaningful question is whether its error stays acceptably small at cold start, hot idle, high load, low ambient pressure, and during rapid change. Define this intended envelope explicitly, keep data from some points for validation, and reject extrapolation outside known physical or measurement limits. Applied to **exergy, irreversibility and real-engine efficiency**, this discipline helps decide whether the model is a prediction with independent evidence or merely a restatement of its input measurements. Write the most restrictive assumption in the margin of the calculation, then revise the interpretation if that assumption fails under the case-study operating conditions.

### 4. Measurement, uncertainty and experimental integrity

**Measurement and evidence plan:** Prepare separate energy and exergy flow diagrams with measured inlet and outlet states. Before any data are collected, define a consistent sample clock, an equipment configuration record and at least one repeated baseline run. Identify how the instrument is calibrated and what its resolution excludes. Put all conversions in the analysis code rather than transcribing rounded values manually. Where the quantity is derived from several measurements, propagate uncertainty through the formula or use an appropriate perturbation study. A graph should show its reference conditions and measurement units. Unsupported interpolation between sparse engine-map points is not experimental evidence.

**Scale and sensitivity:** Scaling a geometric or thermal parameter is not a free performance gain. With every scale change, ask which transport time, stress, temperature, pressure ratio or nondimensional group changes with it. If the underlying response is nonlinear, quote a local sensitivity around the stated operating point instead of applying a single proportional rule across an engine map. A careful research report can hold two ideas at once: the simplified result is internally correct and it is insufficient for system approval. This is not a weakness of mathematical modeling; it is the reason engineering uses progressive verification against measurements.

### 5. Engineering decision and integration

**Design implication:** Prioritize interventions against the largest feasible losses, not the largest visual arrow. This lesson addresses only one component of the unit's problem: An engineer compares compression-ratio changes against fuel economy, peak temperature and knock risk. Changes that look beneficial locally can increase pumping loss, friction, catalyst warm-up time, thermal stress or control complexity elsewhere. Accordingly, the correct engineering decision requires a second comparison at an off-design state and a list of constraints that cannot be traded away. The next simulation or experiment should be chosen to resolve the most consequential unknown, not simply to make the improvement look larger.

A useful extension is to reverse the calculation: choose an output target, estimate the input it would require and then test whether the implied operating point satisfies the engine's load, temperature, fuel and emissions constraints. Reverse calculations frequently uncover impossible combinations that are obscured by forward examples. Record the result as a conditional design feasibility statement, not a claim of guaranteed machine performance.

### 6. Practice and assessment

1. **Conceptual:** Explain why the relation `Exergy destruction = T_0 * S_generated for a fixed environmental reference temperature.` is meaningful for this lesson. Name two necessary assumptions and a physical regime in which one fails.
2. **Calculation:** Reproduce and verify the worked case: An entropy generation of 0.20 kJ/K at T0=300 K corresponds to 60 kJ destroyed exergy. Show units at every intermediate stage and carry at least one input uncertainty through the output.
3. **Diagnostic:** A team reports a performance improvement after changing one input. Construct an alternative explanation using a measurement error, thermal shift or controller response. What single observation would discriminate between them?
4. **Design:** In the case “An engineer compares compression-ratio changes against fuel economy, peak temperature and knock risk.”, propose one legitimate design change and one nonnegotiable constraint. Prioritize interventions against the largest feasible losses, not the largest visual arrow.
5. **Research practice:** Give a file naming and metadata convention that would allow another student to reproduce the analysis, including configuration, units and calibration state.

**Worked-answer checking guide.** For question 2, the reference result is described in the assumed numerical case; a correct submission must also specify the formula, the explicit units and the idealizations. For question 3, credit is earned for a falsifiable alternative mechanism and a measurement that can separate it from the original claim. For question 4, a design that ignores the nonnegotiable constraint is rejected even if its calculated objective improves.

**Further investigation.** Repeat the reasoning at two additional operating points: lower speed and higher intake temperature, or cold start and warmed-up operation where relevant. Describe why the same input perturbation might have a different result under those conditions. Decide which hypothesis can be evaluated safely using the offline numerical model and which requires qualified laboratory equipment.



---

