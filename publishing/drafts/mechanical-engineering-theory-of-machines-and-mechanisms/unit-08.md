# Unit 08: Mechanism Synthesis, Measurement and Design Verification

**Course Code**: TMM 208 · **Level**: Advanced Undergraduate Engineering

## Unit Overview & Physical Foundations

This comprehensive university textbook unit covers the theoretical framework, physical modeling, mathematical governing equations, and engineering applications of **Mechanism Synthesis, Measurement and Design Verification**.

# U08-L01 — Mechanism dimensional synthesis

**Unit 8: Mechanism Synthesis, Measurement and Design Verification · University-level learning draft · All examples synthetic**

## Engineering question and geometry

**Question:** How can designers trade workspace, force transmission and manufacturability?

**Scenario:** A parcel diverter must move a pusher between two stations without striking a nearby guard. Begin by drawing the machine in one reference configuration, identifying the ground, the input actuator and the intended output variable. Treat the device as a rigid planar assembly only if its geometry and operating conditions justify that approximation. Mark fixed points, moving joints, relevant dimensions, motion signs and any physical stop or contact condition. A computer animation is useful for communicating the proposed motion, but it cannot demonstrate that the physical parts have sufficient clearance or that the arrangement is safe.

## Principle, constraints and derivation

**Governing relation:** `Choose link dimensions to satisfy prescribed endpoint and path constraints`.

Two positions rarely determine a unique design; constraints, tolerances and manufacturable joints must be stated. Synthesis begins with constraints: required displacement, timing, mechanism footprint, allowable force, service access and failure consequences. Compare alternative topologies before refining one geometry. Once the geometry is fixed, a solver should demonstrate small closure residuals, consistent branches and convergence under smaller angular steps. A sensitivity study should alter measured dimensions within their documented uncertainties rather than adding arbitrary noise without justification. Evidence for selection should combine mechanical performance, duty cycle, maintainability and guarding; no numerical fitness value substitutes for an actual machine hazard assessment or standards-compliant testing.

Define each independent quantity and units before substitution. If a formula contains an angle derivative, convert degrees to radians and apply the chain rule to move from angle to time. For a constrained mechanism, first solve position closure and then differentiate to obtain velocity and acceleration. For a loaded mechanism, separate the purely kinematic result from required contact reactions and input torque. Identify when the formula assumes a fixed pivot, a constant input speed, a continuously engaged contact, or one assembly branch. A physically meaningful calculation states its domain, not just its output.

## Worked numerical case

**Illustrative inputs:** Required motion envelope 0.22 m and available mechanism clearance 0.25 m.

**Calculation — Stroke target margin:** **0.03 m**. These values were chosen for teaching, not measured from machinery. Put each input and its unit on a separate line in a reproducible calculation sheet, then verify the arithmetic with an independent computation. The sign of a rotational quantity indicates orientation; it does not imply an error. When the output is a force, check the implied work and reaction path. When it is a geometric dimension, check the assembly envelope and the full intended motion cycle, not only the illustrated pose.

**Sanity test:** Vary one relevant parameter by 10% and classify the resulting trend as linear, inverse, quadratic or configuration-dependent. Consider a near-limit case and ask which assumption would fail first. The calculation cannot independently prove its own assumptions: a derived value must eventually be compared with a separate observation, compatible published reference or physically grounded second model.

## Engineering interpretation and counterexample

**Frequent mistake:** Selecting link lengths only for reach while ignoring inaccessible assembly paths.

**Specific sensitivity investigation:** Impose a new housing constraint without changing the target stroke. Assess which mechanism concepts become infeasible and why. State what is held fixed, what changes and whether the output should be continuous. For closed-loop linkages, a second numerical solution may correspond to a different assembly branch; continuous angle tracking and a small closure residual are essential. For cams, belts, transmissions and vibration models, identify contact state, speed range and sources of energy dissipation. If a model produces exceptionally high speed or force near an ideal singularity, report the sensitivity and stop short of treating an unbounded prediction as achievable hardware performance.

A result matters when it can influence an engineering decision: mechanism selection, operating speed, joint configuration, allowable tolerance or actuator requirement. Always distinguish theoretical feasibility from reliability over many cycles. Geometry can be correct while friction, wear, fatigue, excessive contact stress or dynamic instability invalidates the design. A response that is numerically precise but sensitive to unmeasured clearances should be given as a qualified estimate rather than a certified value.

## Test and reproducibility plan

**Investigation:** Sketch multiple candidate mechanisms and compare swept envelopes before optimizing. Record the drawing and initial settings before running the test. An appropriate student exercise can use slow, guarded motion, video tracking, or a separate numerical implementation; an energized high-speed experiment needs professional safety controls. Document reference length, sampling interval, calibration method and expected uncertainty. Compare at least three configurations, including a near-boundary case if it can be studied safely. Keep synthetic values separated from measured observations, and do not count the same input data as independent validation.

The report should contain a labeled schematic, equations, raw input table, one calculated output and its units, a sensitivity result and a discrepancy explanation. If an observed path differs from the model, consider perspective error, misidentified joints, slippage, structural flexibility, bearing clearance and unintended motion. Decide which extra measurement would distinguish the most plausible causes. A useful verification plan explains not only what evidence would support a model but what evidence would require it to be revised.

## Exercises and assessment

1. **Numerical variation:** Recalculate the worked example after changing one driving parameter by 15%. State the new answer, its units and the percentage change. Identify any hidden domain restriction, such as a minimum rod length or positive stiffness.
2. **Mechanism reasoning:** How can designers trade workspace, force transmission and manufacturability? Contrast the original situation with a changed link, joint, contact condition or speed regime. Draw the new physical picture and explain which equation remains valid, requires modification or fails.
3. **Model critique:** Design an independent test for the proposed investigation, including measured variables, instrument calibration, repeatability, one confounding factor and a rejection criterion.

## Design review conclusion

**Mechanism dimensional synthesis** provides one part of a complete machine analysis. Deliver a brief calculation memo with an explicit operating range and at least one technical limitation. Evaluate the result against mechanism geometry and energy conservation, and list any unresolved requirements for guards, rated components, fatigue testing, maintenance or industrial standards before suggesting construction. A model is only one line of evidence; physical tests and responsible engineering judgment remain necessary.


---

# U08-L02 — Tolerances and sensitivity

**Unit 8: Mechanism Synthesis, Measurement and Design Verification · University-level learning draft · All examples synthetic**

## Engineering question and geometry

**Question:** Why do small pin-location errors produce large output errors near toggles?

**Scenario:** A stamping machine's nominal pin distances vary by a fraction of a millimeter. Begin by drawing the machine in one reference configuration, identifying the ground, the input actuator and the intended output variable. Treat the device as a rigid planar assembly only if its geometry and operating conditions justify that approximation. Mark fixed points, moving joints, relevant dimensions, motion signs and any physical stop or contact condition. A computer animation is useful for communicating the proposed motion, but it cannot demonstrate that the physical parts have sufficient clearance or that the arrangement is safe.

## Principle, constraints and derivation

**Governing relation:** `Δy≈(∂y/∂x)Δx locally`.

Linear sensitivity fails when tolerance excursions cross a singularity or assembly branch boundary. Synthesis begins with constraints: required displacement, timing, mechanism footprint, allowable force, service access and failure consequences. Compare alternative topologies before refining one geometry. Once the geometry is fixed, a solver should demonstrate small closure residuals, consistent branches and convergence under smaller angular steps. A sensitivity study should alter measured dimensions within their documented uncertainties rather than adding arbitrary noise without justification. Evidence for selection should combine mechanical performance, duty cycle, maintainability and guarding; no numerical fitness value substitutes for an actual machine hazard assessment or standards-compliant testing.

Define each independent quantity and units before substitution. If a formula contains an angle derivative, convert degrees to radians and apply the chain rule to move from angle to time. For a constrained mechanism, first solve position closure and then differentiate to obtain velocity and acceleration. For a loaded mechanism, separate the purely kinematic result from required contact reactions and input torque. Identify when the formula assumes a fixed pivot, a constant input speed, a continuously engaged contact, or one assembly branch. A physically meaningful calculation states its domain, not just its output.

## Worked numerical case

**Illustrative inputs:** Local sensitivity dy/dx=4; dimensional tolerance ±0.25 mm.

**Calculation — Linear tolerance amplification:** **0.001 m**. These values were chosen for teaching, not measured from machinery. Put each input and its unit on a separate line in a reproducible calculation sheet, then verify the arithmetic with an independent computation. The sign of a rotational quantity indicates orientation; it does not imply an error. When the output is a force, check the implied work and reaction path. When it is a geometric dimension, check the assembly envelope and the full intended motion cycle, not only the illustrated pose.

**Sanity test:** Vary one relevant parameter by 10% and classify the resulting trend as linear, inverse, quadratic or configuration-dependent. Consider a near-limit case and ask which assumption would fail first. The calculation cannot independently prove its own assumptions: a derived value must eventually be compared with a separate observation, compatible published reference or physically grounded second model.

## Engineering interpretation and counterexample

**Frequent mistake:** Using nominal geometry as proof of repeatable output placement.

**Specific sensitivity investigation:** Perturb two linkage dimensions together with correlated manufacturing error. Discuss why independent-error summation may underestimate the output change. State what is held fixed, what changes and whether the output should be continuous. For closed-loop linkages, a second numerical solution may correspond to a different assembly branch; continuous angle tracking and a small closure residual are essential. For cams, belts, transmissions and vibration models, identify contact state, speed range and sources of energy dissipation. If a model produces exceptionally high speed or force near an ideal singularity, report the sensitivity and stop short of treating an unbounded prediction as achievable hardware performance.

A result matters when it can influence an engineering decision: mechanism selection, operating speed, joint configuration, allowable tolerance or actuator requirement. Always distinguish theoretical feasibility from reliability over many cycles. Geometry can be correct while friction, wear, fatigue, excessive contact stress or dynamic instability invalidates the design. A response that is numerically precise but sensitive to unmeasured clearances should be given as a qualified estimate rather than a certified value.

## Test and reproducibility plan

**Investigation:** Perturb each length independently in a closure solver and report output variation. Record the drawing and initial settings before running the test. An appropriate student exercise can use slow, guarded motion, video tracking, or a separate numerical implementation; an energized high-speed experiment needs professional safety controls. Document reference length, sampling interval, calibration method and expected uncertainty. Compare at least three configurations, including a near-boundary case if it can be studied safely. Keep synthetic values separated from measured observations, and do not count the same input data as independent validation.

The report should contain a labeled schematic, equations, raw input table, one calculated output and its units, a sensitivity result and a discrepancy explanation. If an observed path differs from the model, consider perspective error, misidentified joints, slippage, structural flexibility, bearing clearance and unintended motion. Decide which extra measurement would distinguish the most plausible causes. A useful verification plan explains not only what evidence would support a model but what evidence would require it to be revised.

## Exercises and assessment

1. **Numerical variation:** Recalculate the worked example after changing one driving parameter by 15%. State the new answer, its units and the percentage change. Identify any hidden domain restriction, such as a minimum rod length or positive stiffness.
2. **Mechanism reasoning:** Why do small pin-location errors produce large output errors near toggles? Contrast the original situation with a changed link, joint, contact condition or speed regime. Draw the new physical picture and explain which equation remains valid, requires modification or fails.
3. **Model critique:** Design an independent test for the proposed investigation, including measured variables, instrument calibration, repeatability, one confounding factor and a rejection criterion.

## Design review conclusion

**Tolerances and sensitivity** provides one part of a complete machine analysis. Deliver a brief calculation memo with an explicit operating range and at least one technical limitation. Evaluate the result against mechanism geometry and energy conservation, and list any unresolved requirements for guards, rated components, fatigue testing, maintenance or industrial standards before suggesting construction. A model is only one line of evidence; physical tests and responsible engineering judgment remain necessary.


---

# U08-L03 — Numerical constraint solving

**Unit 8: Mechanism Synthesis, Measurement and Design Verification · University-level learning draft · All examples synthetic**

## Engineering question and geometry

**Question:** How do numerical solvers track a mechanism through an angle sweep?

**Scenario:** A four-bar simulation must keep the same physical assembly branch over hundreds of time steps. Begin by drawing the machine in one reference configuration, identifying the ground, the input actuator and the intended output variable. Treat the device as a rigid planar assembly only if its geometry and operating conditions justify that approximation. Mark fixed points, moving joints, relevant dimensions, motion signs and any physical stop or contact condition. A computer animation is useful for communicating the proposed motion, but it cannot demonstrate that the physical parts have sufficient clearance or that the arrangement is safe.

## Principle, constraints and derivation

**Governing relation:** `Newton update: Δq=−J(q)⁻¹f(q) when J is nonsingular`.

Near singular positions Newton iterations may stall or jump branches; continuation and a residual threshold are essential. Synthesis begins with constraints: required displacement, timing, mechanism footprint, allowable force, service access and failure consequences. Compare alternative topologies before refining one geometry. Once the geometry is fixed, a solver should demonstrate small closure residuals, consistent branches and convergence under smaller angular steps. A sensitivity study should alter measured dimensions within their documented uncertainties rather than adding arbitrary noise without justification. Evidence for selection should combine mechanical performance, duty cycle, maintainability and guarding; no numerical fitness value substitutes for an actual machine hazard assessment or standards-compliant testing.

Define each independent quantity and units before substitution. If a formula contains an angle derivative, convert degrees to radians and apply the chain rule to move from angle to time. For a constrained mechanism, first solve position closure and then differentiate to obtain velocity and acceleration. For a loaded mechanism, separate the purely kinematic result from required contact reactions and input torque. Identify when the formula assumes a fixed pivot, a constant input speed, a continuously engaged contact, or one assembly branch. A physically meaningful calculation states its domain, not just its output.

## Worked numerical case

**Illustrative inputs:** Iterative solution updates Δθ1=0.0002 and Δθ2=0.0004 radians.

**Calculation — Newton coordinate correction norm:** **0.000447214 rad**. These values were chosen for teaching, not measured from machinery. Put each input and its unit on a separate line in a reproducible calculation sheet, then verify the arithmetic with an independent computation. The sign of a rotational quantity indicates orientation; it does not imply an error. When the output is a force, check the implied work and reaction path. When it is a geometric dimension, check the assembly envelope and the full intended motion cycle, not only the illustrated pose.

**Sanity test:** Vary one relevant parameter by 10% and classify the resulting trend as linear, inverse, quadratic or configuration-dependent. Consider a near-limit case and ask which assumption would fail first. The calculation cannot independently prove its own assumptions: a derived value must eventually be compared with a separate observation, compatible published reference or physically grounded second model.

## Engineering interpretation and counterexample

**Frequent mistake:** Accepting convergence based only on coordinate changes instead of constraint residual.

**Specific sensitivity investigation:** Change the initial guess in a nonlinear closure solver. Explain why both converged residual and branch continuity are required. State what is held fixed, what changes and whether the output should be continuous. For closed-loop linkages, a second numerical solution may correspond to a different assembly branch; continuous angle tracking and a small closure residual are essential. For cams, belts, transmissions and vibration models, identify contact state, speed range and sources of energy dissipation. If a model produces exceptionally high speed or force near an ideal singularity, report the sensitivity and stop short of treating an unbounded prediction as achievable hardware performance.

A result matters when it can influence an engineering decision: mechanism selection, operating speed, joint configuration, allowable tolerance or actuator requirement. Always distinguish theoretical feasibility from reliability over many cycles. Geometry can be correct while friction, wear, fatigue, excessive contact stress or dynamic instability invalidates the design. A response that is numerically precise but sensitive to unmeasured clearances should be given as a qualified estimate rather than a certified value.

## Test and reproducibility plan

**Investigation:** Run coarse and fine angular sweeps and compare maximum closure residual and branch continuity. Record the drawing and initial settings before running the test. An appropriate student exercise can use slow, guarded motion, video tracking, or a separate numerical implementation; an energized high-speed experiment needs professional safety controls. Document reference length, sampling interval, calibration method and expected uncertainty. Compare at least three configurations, including a near-boundary case if it can be studied safely. Keep synthetic values separated from measured observations, and do not count the same input data as independent validation.

The report should contain a labeled schematic, equations, raw input table, one calculated output and its units, a sensitivity result and a discrepancy explanation. If an observed path differs from the model, consider perspective error, misidentified joints, slippage, structural flexibility, bearing clearance and unintended motion. Decide which extra measurement would distinguish the most plausible causes. A useful verification plan explains not only what evidence would support a model but what evidence would require it to be revised.

## Exercises and assessment

1. **Numerical variation:** Recalculate the worked example after changing one driving parameter by 15%. State the new answer, its units and the percentage change. Identify any hidden domain restriction, such as a minimum rod length or positive stiffness.
2. **Mechanism reasoning:** How do numerical solvers track a mechanism through an angle sweep? Contrast the original situation with a changed link, joint, contact condition or speed regime. Draw the new physical picture and explain which equation remains valid, requires modification or fails.
3. **Model critique:** Design an independent test for the proposed investigation, including measured variables, instrument calibration, repeatability, one confounding factor and a rejection criterion.

## Design review conclusion

**Numerical constraint solving** provides one part of a complete machine analysis. Deliver a brief calculation memo with an explicit operating range and at least one technical limitation. Evaluate the result against mechanism geometry and energy conservation, and list any unresolved requirements for guards, rated components, fatigue testing, maintenance or industrial standards before suggesting construction. A model is only one line of evidence; physical tests and responsible engineering judgment remain necessary.


---

# U08-L04 — Measurement, calibration and uncertainty

**Unit 8: Mechanism Synthesis, Measurement and Design Verification · University-level learning draft · All examples synthetic**

## Engineering question and geometry

**Question:** How can uncertainty in dimensions and encoder readings affect inferred motion?

**Scenario:** A linkage lab uses a digital caliper, rotary encoder and phone camera with different precision. Begin by drawing the machine in one reference configuration, identifying the ground, the input actuator and the intended output variable. Treat the device as a rigid planar assembly only if its geometry and operating conditions justify that approximation. Mark fixed points, moving joints, relevant dimensions, motion signs and any physical stop or contact condition. A computer animation is useful for communicating the proposed motion, but it cannot demonstrate that the physical parts have sufficient clearance or that the arrangement is safe.

## Principle, constraints and derivation

**Governing relation:** `u_y²≈Σ(∂y/∂x_i)²u_i² for independent inputs`.

The propagation formula is first order and assumes independent small errors; shared bias and nonlinear extremes need separate treatment. Synthesis begins with constraints: required displacement, timing, mechanism footprint, allowable force, service access and failure consequences. Compare alternative topologies before refining one geometry. Once the geometry is fixed, a solver should demonstrate small closure residuals, consistent branches and convergence under smaller angular steps. A sensitivity study should alter measured dimensions within their documented uncertainties rather than adding arbitrary noise without justification. Evidence for selection should combine mechanical performance, duty cycle, maintainability and guarding; no numerical fitness value substitutes for an actual machine hazard assessment or standards-compliant testing.

Define each independent quantity and units before substitution. If a formula contains an angle derivative, convert degrees to radians and apply the chain rule to move from angle to time. For a constrained mechanism, first solve position closure and then differentiate to obtain velocity and acceleration. For a loaded mechanism, separate the purely kinematic result from required contact reactions and input torque. Identify when the formula assumes a fixed pivot, a constant input speed, a continuously engaged contact, or one assembly branch. A physically meaningful calculation states its domain, not just its output.

## Worked numerical case

**Illustrative inputs:** Two independent displacement contributions of 0.4 and 0.3 mm.

**Calculation — Combined independent displacement uncertainty:** **0.0005 m**. These values were chosen for teaching, not measured from machinery. Put each input and its unit on a separate line in a reproducible calculation sheet, then verify the arithmetic with an independent computation. The sign of a rotational quantity indicates orientation; it does not imply an error. When the output is a force, check the implied work and reaction path. When it is a geometric dimension, check the assembly envelope and the full intended motion cycle, not only the illustrated pose.

**Sanity test:** Vary one relevant parameter by 10% and classify the resulting trend as linear, inverse, quadratic or configuration-dependent. Consider a near-limit case and ask which assumption would fail first. The calculation cannot independently prove its own assumptions: a derived value must eventually be compared with a separate observation, compatible published reference or physically grounded second model.

## Engineering interpretation and counterexample

**Frequent mistake:** Reporting solver digits as if they were experimental certainty.

**Specific sensitivity investigation:** Move a camera sideways relative to a planar linkage. Show how perspective bias can mimic apparent out-of-plane motion. State what is held fixed, what changes and whether the output should be continuous. For closed-loop linkages, a second numerical solution may correspond to a different assembly branch; continuous angle tracking and a small closure residual are essential. For cams, belts, transmissions and vibration models, identify contact state, speed range and sources of energy dissipation. If a model produces exceptionally high speed or force near an ideal singularity, report the sensitivity and stop short of treating an unbounded prediction as achievable hardware performance.

A result matters when it can influence an engineering decision: mechanism selection, operating speed, joint configuration, allowable tolerance or actuator requirement. Always distinguish theoretical feasibility from reliability over many cycles. Geometry can be correct while friction, wear, fatigue, excessive contact stress or dynamic instability invalidates the design. A response that is numerically precise but sensitive to unmeasured clearances should be given as a qualified estimate rather than a certified value.

## Test and reproducibility plan

**Investigation:** Create an uncertainty budget, repeat a measurement and check instrument zero and scale. Record the drawing and initial settings before running the test. An appropriate student exercise can use slow, guarded motion, video tracking, or a separate numerical implementation; an energized high-speed experiment needs professional safety controls. Document reference length, sampling interval, calibration method and expected uncertainty. Compare at least three configurations, including a near-boundary case if it can be studied safely. Keep synthetic values separated from measured observations, and do not count the same input data as independent validation.

The report should contain a labeled schematic, equations, raw input table, one calculated output and its units, a sensitivity result and a discrepancy explanation. If an observed path differs from the model, consider perspective error, misidentified joints, slippage, structural flexibility, bearing clearance and unintended motion. Decide which extra measurement would distinguish the most plausible causes. A useful verification plan explains not only what evidence would support a model but what evidence would require it to be revised.

## Exercises and assessment

1. **Numerical variation:** Recalculate the worked example after changing one driving parameter by 15%. State the new answer, its units and the percentage change. Identify any hidden domain restriction, such as a minimum rod length or positive stiffness.
2. **Mechanism reasoning:** How can uncertainty in dimensions and encoder readings affect inferred motion? Contrast the original situation with a changed link, joint, contact condition or speed regime. Draw the new physical picture and explain which equation remains valid, requires modification or fails.
3. **Model critique:** Design an independent test for the proposed investigation, including measured variables, instrument calibration, repeatability, one confounding factor and a rejection criterion.

## Design review conclusion

**Measurement, calibration and uncertainty** provides one part of a complete machine analysis. Deliver a brief calculation memo with an explicit operating range and at least one technical limitation. Evaluate the result against mechanism geometry and energy conservation, and list any unresolved requirements for guards, rated components, fatigue testing, maintenance or industrial standards before suggesting construction. A model is only one line of evidence; physical tests and responsible engineering judgment remain necessary.


---

# U08-L05 — Integrated mechanism design review

**Unit 8: Mechanism Synthesis, Measurement and Design Verification · University-level learning draft · All examples synthetic**

## Engineering question and geometry

**Question:** What evidence is sufficient to select and commission a mechanism concept?

**Scenario:** Three designs satisfy the required stroke but differ in power demand, guarding and assembly complexity. Begin by drawing the machine in one reference configuration, identifying the ground, the input actuator and the intended output variable. Treat the device as a rigid planar assembly only if its geometry and operating conditions justify that approximation. Mark fixed points, moving joints, relevant dimensions, motion signs and any physical stop or contact condition. A computer animation is useful for communicating the proposed motion, but it cannot demonstrate that the physical parts have sufficient clearance or that the arrangement is safe.

## Principle, constraints and derivation

**Governing relation:** `Decision score=Σw_i s_i, with documented comparable criteria`.

A weighted score organizes discussion but cannot replace legal safety assessment, physical verification or lifecycle cost evidence. Synthesis begins with constraints: required displacement, timing, mechanism footprint, allowable force, service access and failure consequences. Compare alternative topologies before refining one geometry. Once the geometry is fixed, a solver should demonstrate small closure residuals, consistent branches and convergence under smaller angular steps. A sensitivity study should alter measured dimensions within their documented uncertainties rather than adding arbitrary noise without justification. Evidence for selection should combine mechanical performance, duty cycle, maintainability and guarding; no numerical fitness value substitutes for an actual machine hazard assessment or standards-compliant testing.

Define each independent quantity and units before substitution. If a formula contains an angle derivative, convert degrees to radians and apply the chain rule to move from angle to time. For a constrained mechanism, first solve position closure and then differentiate to obtain velocity and acceleration. For a loaded mechanism, separate the purely kinematic result from required contact reactions and input torque. Identify when the formula assumes a fixed pivot, a constant input speed, a continuously engaged contact, or one assembly branch. A physically meaningful calculation states its domain, not just its output.

## Worked numerical case

**Illustrative inputs:** Weights 0.40, 0.35, 0.25; normalized scores 0.80, 0.70, 0.90.

**Calculation — Weighted concept score:** **0.79 dimensionless**. These values were chosen for teaching, not measured from machinery. Put each input and its unit on a separate line in a reproducible calculation sheet, then verify the arithmetic with an independent computation. The sign of a rotational quantity indicates orientation; it does not imply an error. When the output is a force, check the implied work and reaction path. When it is a geometric dimension, check the assembly envelope and the full intended motion cycle, not only the illustrated pose.

**Sanity test:** Vary one relevant parameter by 10% and classify the resulting trend as linear, inverse, quadratic or configuration-dependent. Consider a near-limit case and ask which assumption would fail first. The calculation cannot independently prove its own assumptions: a derived value must eventually be compared with a separate observation, compatible published reference or physically grounded second model.

## Engineering interpretation and counterexample

**Frequent mistake:** Choosing the highest score before testing the assumptions behind each score.

**Specific sensitivity investigation:** Reweight guarding and maintenance more heavily than maximum speed. Explain how a transparent selection matrix changes the concept ranking. State what is held fixed, what changes and whether the output should be continuous. For closed-loop linkages, a second numerical solution may correspond to a different assembly branch; continuous angle tracking and a small closure residual are essential. For cams, belts, transmissions and vibration models, identify contact state, speed range and sources of energy dissipation. If a model produces exceptionally high speed or force near an ideal singularity, report the sensitivity and stop short of treating an unbounded prediction as achievable hardware performance.

A result matters when it can influence an engineering decision: mechanism selection, operating speed, joint configuration, allowable tolerance or actuator requirement. Always distinguish theoretical feasibility from reliability over many cycles. Geometry can be correct while friction, wear, fatigue, excessive contact stress or dynamic instability invalidates the design. A response that is numerically precise but sensitive to unmeasured clearances should be given as a qualified estimate rather than a certified value.

## Test and reproducibility plan

**Investigation:** Write a design verification matrix linking each requirement to model, inspection or test. Record the drawing and initial settings before running the test. An appropriate student exercise can use slow, guarded motion, video tracking, or a separate numerical implementation; an energized high-speed experiment needs professional safety controls. Document reference length, sampling interval, calibration method and expected uncertainty. Compare at least three configurations, including a near-boundary case if it can be studied safely. Keep synthetic values separated from measured observations, and do not count the same input data as independent validation.

The report should contain a labeled schematic, equations, raw input table, one calculated output and its units, a sensitivity result and a discrepancy explanation. If an observed path differs from the model, consider perspective error, misidentified joints, slippage, structural flexibility, bearing clearance and unintended motion. Decide which extra measurement would distinguish the most plausible causes. A useful verification plan explains not only what evidence would support a model but what evidence would require it to be revised.

## Exercises and assessment

1. **Numerical variation:** Recalculate the worked example after changing one driving parameter by 15%. State the new answer, its units and the percentage change. Identify any hidden domain restriction, such as a minimum rod length or positive stiffness.
2. **Mechanism reasoning:** What evidence is sufficient to select and commission a mechanism concept? Contrast the original situation with a changed link, joint, contact condition or speed regime. Draw the new physical picture and explain which equation remains valid, requires modification or fails.
3. **Model critique:** Design an independent test for the proposed investigation, including measured variables, instrument calibration, repeatability, one confounding factor and a rejection criterion.

## Design review conclusion

**Integrated mechanism design review** provides one part of a complete machine analysis. Deliver a brief calculation memo with an explicit operating range and at least one technical limitation. Evaluate the result against mechanism geometry and energy conservation, and list any unresolved requirements for guards, rated components, fatigue testing, maintenance or industrial standards before suggesting construction. A model is only one line of evidence; physical tests and responsible engineering judgment remain necessary.


---

