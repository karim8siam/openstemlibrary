# Unit 05: Cams, Followers and Indexing Mechanisms

**Course Code**: TMM 205 · **Level**: Advanced Undergraduate Engineering

## Unit Overview & Physical Foundations

This comprehensive university textbook unit covers the theoretical framework, physical modeling, mathematical governing equations, and engineering applications of **Cams, Followers and Indexing Mechanisms**.

# U05-L01 — Cam nomenclature, lift and dwell

**Unit 5: Cams, Followers and Indexing Mechanisms · University-level learning draft · All examples synthetic**

## Engineering question and geometry

**Question:** What part of a cam cycle actually moves a follower?

**Scenario:** A packaging cam rises for 120 degrees and dwells before returning. Begin by drawing the machine in one reference configuration, identifying the ground, the input actuator and the intended output variable. Treat the device as a rigid planar assembly only if its geometry and operating conditions justify that approximation. Mark fixed points, moving joints, relevant dimensions, motion signs and any physical stop or contact condition. A computer animation is useful for communicating the proposed motion, but it cannot demonstrate that the physical parts have sufficient clearance or that the arrangement is safe.

## Principle, constraints and derivation

**Governing relation:** `s(θ)=h(1−cos(πθ/β))/2 during simple-harmonic rise`.

A motion schedule is kinematic; the cam profile additionally depends on roller radius, follower type and pressure angle. A motion program comprises rise, dwell, return and dwell segments; its derivatives determine severity. Differentiate with respect to cam angle first, then multiply by angular speed according to the chain rule. If cam speed changes with time, acceleration includes a separate angular-acceleration term. A continuous displacement profile can have a velocity jump at an interval boundary unless the rise law is carefully chosen. Follower contact requires a compressive normal reaction and acceptable pressure angle. A purely prescribed follower path does not show that spring preload, gravity and inertia maintain contact. Indexing mechanisms add impact and dwell stability questions absent from a steady speed ratio.

Define each independent quantity and units before substitution. If a formula contains an angle derivative, convert degrees to radians and apply the chain rule to move from angle to time. For a constrained mechanism, first solve position closure and then differentiate to obtain velocity and acceleration. For a loaded mechanism, separate the purely kinematic result from required contact reactions and input torque. Identify when the formula assumes a fixed pivot, a constant input speed, a continuously engaged contact, or one assembly branch. A physically meaningful calculation states its domain, not just its output.

## Worked numerical case

**Illustrative inputs:** Lift 12 mm; half-way through simple harmonic rise.

**Calculation — Harmonic cam half-rise displacement:** **0.006 m**. These values were chosen for teaching, not measured from machinery. Put each input and its unit on a separate line in a reproducible calculation sheet, then verify the arithmetic with an independent computation. The sign of a rotational quantity indicates orientation; it does not imply an error. When the output is a force, check the implied work and reaction path. When it is a geometric dimension, check the assembly envelope and the full intended motion cycle, not only the illustrated pose.

**Sanity test:** Vary one relevant parameter by 10% and classify the resulting trend as linear, inverse, quadratic or configuration-dependent. Consider a near-limit case and ask which assumption would fail first. The calculation cannot independently prove its own assumptions: a derived value must eventually be compared with a separate observation, compatible published reference or physically grounded second model.

## Engineering interpretation and counterexample

**Frequent mistake:** Treating a dwell as motion with nonzero derivative or confusing cam base radius with lift.

**Specific sensitivity investigation:** Change cam rise angle while keeping lift fixed. Deduce the resulting velocity and acceleration scaling with the shortened rise interval. State what is held fixed, what changes and whether the output should be continuous. For closed-loop linkages, a second numerical solution may correspond to a different assembly branch; continuous angle tracking and a small closure residual are essential. For cams, belts, transmissions and vibration models, identify contact state, speed range and sources of energy dissipation. If a model produces exceptionally high speed or force near an ideal singularity, report the sensitivity and stop short of treating an unbounded prediction as achievable hardware performance.

A result matters when it can influence an engineering decision: mechanism selection, operating speed, joint configuration, allowable tolerance or actuator requirement. Always distinguish theoretical feasibility from reliability over many cycles. Geometry can be correct while friction, wear, fatigue, excessive contact stress or dynamic instability invalidates the design. A response that is numerically precise but sensitive to unmeasured clearances should be given as a qualified estimate rather than a certified value.

## Test and reproducibility plan

**Investigation:** Trace follower displacement versus cam angle using a dial indicator on a supervised bench device. Record the drawing and initial settings before running the test. An appropriate student exercise can use slow, guarded motion, video tracking, or a separate numerical implementation; an energized high-speed experiment needs professional safety controls. Document reference length, sampling interval, calibration method and expected uncertainty. Compare at least three configurations, including a near-boundary case if it can be studied safely. Keep synthetic values separated from measured observations, and do not count the same input data as independent validation.

The report should contain a labeled schematic, equations, raw input table, one calculated output and its units, a sensitivity result and a discrepancy explanation. If an observed path differs from the model, consider perspective error, misidentified joints, slippage, structural flexibility, bearing clearance and unintended motion. Decide which extra measurement would distinguish the most plausible causes. A useful verification plan explains not only what evidence would support a model but what evidence would require it to be revised.

## Exercises and assessment

1. **Numerical variation:** Recalculate the worked example after changing one driving parameter by 15%. State the new answer, its units and the percentage change. Identify any hidden domain restriction, such as a minimum rod length or positive stiffness.
2. **Mechanism reasoning:** What part of a cam cycle actually moves a follower? Contrast the original situation with a changed link, joint, contact condition or speed regime. Draw the new physical picture and explain which equation remains valid, requires modification or fails.
3. **Model critique:** Design an independent test for the proposed investigation, including measured variables, instrument calibration, repeatability, one confounding factor and a rejection criterion.

## Design review conclusion

**Cam nomenclature, lift and dwell** provides one part of a complete machine analysis. Deliver a brief calculation memo with an explicit operating range and at least one technical limitation. Evaluate the result against mechanism geometry and energy conservation, and list any unresolved requirements for guards, rated components, fatigue testing, maintenance or industrial standards before suggesting construction. A model is only one line of evidence; physical tests and responsible engineering judgment remain necessary.


---

# U05-L02 — Cam velocity and acceleration laws

**Unit 5: Cams, Followers and Indexing Mechanisms · University-level learning draft · All examples synthetic**

## Engineering question and geometry

**Question:** Why does the follower accelerate more violently as the cam spins faster?

**Scenario:** A feeder cam doubles running speed while preserving the same lift curve. Begin by drawing the machine in one reference configuration, identifying the ground, the input actuator and the intended output variable. Treat the device as a rigid planar assembly only if its geometry and operating conditions justify that approximation. Mark fixed points, moving joints, relevant dimensions, motion signs and any physical stop or contact condition. A computer animation is useful for communicating the proposed motion, but it cannot demonstrate that the physical parts have sufficient clearance or that the arrangement is safe.

## Principle, constraints and derivation

**Governing relation:** `v=ω ds/dθ and a=ω²d²s/dθ² for constant ω`.

A twice-as-fast cam doubles ideal velocity but quadruples ideal acceleration at the same angle when acceleration of the cam itself is zero. A motion program comprises rise, dwell, return and dwell segments; its derivatives determine severity. Differentiate with respect to cam angle first, then multiply by angular speed according to the chain rule. If cam speed changes with time, acceleration includes a separate angular-acceleration term. A continuous displacement profile can have a velocity jump at an interval boundary unless the rise law is carefully chosen. Follower contact requires a compressive normal reaction and acceptable pressure angle. A purely prescribed follower path does not show that spring preload, gravity and inertia maintain contact. Indexing mechanisms add impact and dwell stability questions absent from a steady speed ratio.

Define each independent quantity and units before substitution. If a formula contains an angle derivative, convert degrees to radians and apply the chain rule to move from angle to time. For a constrained mechanism, first solve position closure and then differentiate to obtain velocity and acceleration. For a loaded mechanism, separate the purely kinematic result from required contact reactions and input torque. Identify when the formula assumes a fixed pivot, a constant input speed, a continuously engaged contact, or one assembly branch. A physically meaningful calculation states its domain, not just its output.

## Worked numerical case

**Illustrative inputs:** Lift 12 mm, rise angle 120 degrees = 2π/3 radians, speed 40 rad/s.

**Calculation — SHM cam acceleration at start:** **21.6 m/s²**. These values were chosen for teaching, not measured from machinery. Put each input and its unit on a separate line in a reproducible calculation sheet, then verify the arithmetic with an independent computation. The sign of a rotational quantity indicates orientation; it does not imply an error. When the output is a force, check the implied work and reaction path. When it is a geometric dimension, check the assembly envelope and the full intended motion cycle, not only the illustrated pose.

**Sanity test:** Vary one relevant parameter by 10% and classify the resulting trend as linear, inverse, quadratic or configuration-dependent. Consider a near-limit case and ask which assumption would fail first. The calculation cannot independently prove its own assumptions: a derived value must eventually be compared with a separate observation, compatible published reference or physically grounded second model.

## Engineering interpretation and counterexample

**Frequent mistake:** Assuming doubling rotational speed only doubles dynamic follower force.

**Specific sensitivity investigation:** Hold rise law and lift fixed but double cam speed. Compare ideal velocity and acceleration and assess follower contact risk. State what is held fixed, what changes and whether the output should be continuous. For closed-loop linkages, a second numerical solution may correspond to a different assembly branch; continuous angle tracking and a small closure residual are essential. For cams, belts, transmissions and vibration models, identify contact state, speed range and sources of energy dissipation. If a model produces exceptionally high speed or force near an ideal singularity, report the sensitivity and stop short of treating an unbounded prediction as achievable hardware performance.

A result matters when it can influence an engineering decision: mechanism selection, operating speed, joint configuration, allowable tolerance or actuator requirement. Always distinguish theoretical feasibility from reliability over many cycles. Geometry can be correct while friction, wear, fatigue, excessive contact stress or dynamic instability invalidates the design. A response that is numerically precise but sensitive to unmeasured clearances should be given as a qualified estimate rather than a certified value.

## Test and reproducibility plan

**Investigation:** Compute derivatives for several rpm values and compare acceleration peaks. Record the drawing and initial settings before running the test. An appropriate student exercise can use slow, guarded motion, video tracking, or a separate numerical implementation; an energized high-speed experiment needs professional safety controls. Document reference length, sampling interval, calibration method and expected uncertainty. Compare at least three configurations, including a near-boundary case if it can be studied safely. Keep synthetic values separated from measured observations, and do not count the same input data as independent validation.

The report should contain a labeled schematic, equations, raw input table, one calculated output and its units, a sensitivity result and a discrepancy explanation. If an observed path differs from the model, consider perspective error, misidentified joints, slippage, structural flexibility, bearing clearance and unintended motion. Decide which extra measurement would distinguish the most plausible causes. A useful verification plan explains not only what evidence would support a model but what evidence would require it to be revised.

## Exercises and assessment

1. **Numerical variation:** Recalculate the worked example after changing one driving parameter by 15%. State the new answer, its units and the percentage change. Identify any hidden domain restriction, such as a minimum rod length or positive stiffness.
2. **Mechanism reasoning:** Why does the follower accelerate more violently as the cam spins faster? Contrast the original situation with a changed link, joint, contact condition or speed regime. Draw the new physical picture and explain which equation remains valid, requires modification or fails.
3. **Model critique:** Design an independent test for the proposed investigation, including measured variables, instrument calibration, repeatability, one confounding factor and a rejection criterion.

## Design review conclusion

**Cam velocity and acceleration laws** provides one part of a complete machine analysis. Deliver a brief calculation memo with an explicit operating range and at least one technical limitation. Evaluate the result against mechanism geometry and energy conservation, and list any unresolved requirements for guards, rated components, fatigue testing, maintenance or industrial standards before suggesting construction. A model is only one line of evidence; physical tests and responsible engineering judgment remain necessary.


---

# U05-L03 — Cycloidal motion laws and jerk

**Unit 5: Cams, Followers and Indexing Mechanisms · University-level learning draft · All examples synthetic**

## Engineering question and geometry

**Question:** Why do designers compare rise laws rather than only final displacement?

**Scenario:** A printer mechanism requires smooth pickup motion and low excitation near rise boundaries. Begin by drawing the machine in one reference configuration, identifying the ground, the input actuator and the intended output variable. Treat the device as a rigid planar assembly only if its geometry and operating conditions justify that approximation. Mark fixed points, moving joints, relevant dimensions, motion signs and any physical stop or contact condition. A computer animation is useful for communicating the proposed motion, but it cannot demonstrate that the physical parts have sufficient clearance or that the arrangement is safe.

## Principle, constraints and derivation

**Governing relation:** `s=h[θ/β−sin(2πθ/β)/(2π)] during rise`.

Cycloidal rise has zero velocity and acceleration at its ends but nonzero end jerk; continuous jerk across adjacent dwells is not automatic. A motion program comprises rise, dwell, return and dwell segments; its derivatives determine severity. Differentiate with respect to cam angle first, then multiply by angular speed according to the chain rule. If cam speed changes with time, acceleration includes a separate angular-acceleration term. A continuous displacement profile can have a velocity jump at an interval boundary unless the rise law is carefully chosen. Follower contact requires a compressive normal reaction and acceptable pressure angle. A purely prescribed follower path does not show that spring preload, gravity and inertia maintain contact. Indexing mechanisms add impact and dwell stability questions absent from a steady speed ratio.

Define each independent quantity and units before substitution. If a formula contains an angle derivative, convert degrees to radians and apply the chain rule to move from angle to time. For a constrained mechanism, first solve position closure and then differentiate to obtain velocity and acceleration. For a loaded mechanism, separate the purely kinematic result from required contact reactions and input torque. Identify when the formula assumes a fixed pivot, a constant input speed, a continuously engaged contact, or one assembly branch. A physically meaningful calculation states its domain, not just its output.

## Worked numerical case

**Illustrative inputs:** Lift 10 mm, quarter of cycloidal rise.

**Calculation — Cycloidal lift at quarter rise:** **0.000908451 m**. These values were chosen for teaching, not measured from machinery. Put each input and its unit on a separate line in a reproducible calculation sheet, then verify the arithmetic with an independent computation. The sign of a rotational quantity indicates orientation; it does not imply an error. When the output is a force, check the implied work and reaction path. When it is a geometric dimension, check the assembly envelope and the full intended motion cycle, not only the illustrated pose.

**Sanity test:** Vary one relevant parameter by 10% and classify the resulting trend as linear, inverse, quadratic or configuration-dependent. Consider a near-limit case and ask which assumption would fail first. The calculation cannot independently prove its own assumptions: a derived value must eventually be compared with a separate observation, compatible published reference or physically grounded second model.

## Engineering interpretation and counterexample

**Frequent mistake:** Calling a motion profile smooth without checking acceleration and jerk continuity.

**Specific sensitivity investigation:** Compare the endpoint acceleration of a cycloidal rise to a half-cosine rise. Discuss continuity at the transition to dwell. State what is held fixed, what changes and whether the output should be continuous. For closed-loop linkages, a second numerical solution may correspond to a different assembly branch; continuous angle tracking and a small closure residual are essential. For cams, belts, transmissions and vibration models, identify contact state, speed range and sources of energy dissipation. If a model produces exceptionally high speed or force near an ideal singularity, report the sensitivity and stop short of treating an unbounded prediction as achievable hardware performance.

A result matters when it can influence an engineering decision: mechanism selection, operating speed, joint configuration, allowable tolerance or actuator requirement. Always distinguish theoretical feasibility from reliability over many cycles. Geometry can be correct while friction, wear, fatigue, excessive contact stress or dynamic instability invalidates the design. A response that is numerically precise but sensitive to unmeasured clearances should be given as a qualified estimate rather than a certified value.

## Test and reproducibility plan

**Investigation:** Plot displacement, first, second and third derivatives over one rise segment. Record the drawing and initial settings before running the test. An appropriate student exercise can use slow, guarded motion, video tracking, or a separate numerical implementation; an energized high-speed experiment needs professional safety controls. Document reference length, sampling interval, calibration method and expected uncertainty. Compare at least three configurations, including a near-boundary case if it can be studied safely. Keep synthetic values separated from measured observations, and do not count the same input data as independent validation.

The report should contain a labeled schematic, equations, raw input table, one calculated output and its units, a sensitivity result and a discrepancy explanation. If an observed path differs from the model, consider perspective error, misidentified joints, slippage, structural flexibility, bearing clearance and unintended motion. Decide which extra measurement would distinguish the most plausible causes. A useful verification plan explains not only what evidence would support a model but what evidence would require it to be revised.

## Exercises and assessment

1. **Numerical variation:** Recalculate the worked example after changing one driving parameter by 15%. State the new answer, its units and the percentage change. Identify any hidden domain restriction, such as a minimum rod length or positive stiffness.
2. **Mechanism reasoning:** Why do designers compare rise laws rather than only final displacement? Contrast the original situation with a changed link, joint, contact condition or speed regime. Draw the new physical picture and explain which equation remains valid, requires modification or fails.
3. **Model critique:** Design an independent test for the proposed investigation, including measured variables, instrument calibration, repeatability, one confounding factor and a rejection criterion.

## Design review conclusion

**Cycloidal motion laws and jerk** provides one part of a complete machine analysis. Deliver a brief calculation memo with an explicit operating range and at least one technical limitation. Evaluate the result against mechanism geometry and energy conservation, and list any unresolved requirements for guards, rated components, fatigue testing, maintenance or industrial standards before suggesting construction. A model is only one line of evidence; physical tests and responsible engineering judgment remain necessary.


---

# U05-L04 — Pressure angle and follower contact

**Unit 5: Cams, Followers and Indexing Mechanisms · University-level learning draft · All examples synthetic**

## Engineering question and geometry

**Question:** Why can a high-speed cam experience excessive side thrust?

**Scenario:** A narrow reciprocating guide rubs strongly against its support at certain cam angles. Begin by drawing the machine in one reference configuration, identifying the ground, the input actuator and the intended output variable. Treat the device as a rigid planar assembly only if its geometry and operating conditions justify that approximation. Mark fixed points, moving joints, relevant dimensions, motion signs and any physical stop or contact condition. A computer animation is useful for communicating the proposed motion, but it cannot demonstrate that the physical parts have sufficient clearance or that the arrangement is safe.

## Principle, constraints and derivation

**Governing relation:** `tanφ depends on follower displacement slope and pitch-curve geometry`.

Pressure angle depends on pitch geometry and offset; its acceptable limit depends on contact, guides and load, not a single universal threshold. A motion program comprises rise, dwell, return and dwell segments; its derivatives determine severity. Differentiate with respect to cam angle first, then multiply by angular speed according to the chain rule. If cam speed changes with time, acceleration includes a separate angular-acceleration term. A continuous displacement profile can have a velocity jump at an interval boundary unless the rise law is carefully chosen. Follower contact requires a compressive normal reaction and acceptable pressure angle. A purely prescribed follower path does not show that spring preload, gravity and inertia maintain contact. Indexing mechanisms add impact and dwell stability questions absent from a steady speed ratio.

Define each independent quantity and units before substitution. If a formula contains an angle derivative, convert degrees to radians and apply the chain rule to move from angle to time. For a constrained mechanism, first solve position closure and then differentiate to obtain velocity and acceleration. For a loaded mechanism, separate the purely kinematic result from required contact reactions and input torque. Identify when the formula assumes a fixed pivot, a constant input speed, a continuously engaged contact, or one assembly branch. A physically meaningful calculation states its domain, not just its output.

## Worked numerical case

**Illustrative inputs:** Pitch-curve radial slope 6 mm/radian and effective radius 40 mm; simplified radial-follower proxy.

**Calculation — Slope-derived pressure-angle proxy:** **8.53077 degrees**. These values were chosen for teaching, not measured from machinery. Put each input and its unit on a separate line in a reproducible calculation sheet, then verify the arithmetic with an independent computation. The sign of a rotational quantity indicates orientation; it does not imply an error. When the output is a force, check the implied work and reaction path. When it is a geometric dimension, check the assembly envelope and the full intended motion cycle, not only the illustrated pose.

**Sanity test:** Vary one relevant parameter by 10% and classify the resulting trend as linear, inverse, quadratic or configuration-dependent. Consider a near-limit case and ask which assumption would fail first. The calculation cannot independently prove its own assumptions: a derived value must eventually be compared with a separate observation, compatible published reference or physically grounded second model.

## Engineering interpretation and counterexample

**Frequent mistake:** Assuming a nominally round cam always creates normal forces aligned with follower travel.

**Specific sensitivity investigation:** Increase base-circle size at the same follower lift schedule. Qualitatively compare pressure-angle reduction against packaging size. State what is held fixed, what changes and whether the output should be continuous. For closed-loop linkages, a second numerical solution may correspond to a different assembly branch; continuous angle tracking and a small closure residual are essential. For cams, belts, transmissions and vibration models, identify contact state, speed range and sources of energy dissipation. If a model produces exceptionally high speed or force near an ideal singularity, report the sensitivity and stop short of treating an unbounded prediction as achievable hardware performance.

A result matters when it can influence an engineering decision: mechanism selection, operating speed, joint configuration, allowable tolerance or actuator requirement. Always distinguish theoretical feasibility from reliability over many cycles. Geometry can be correct while friction, wear, fatigue, excessive contact stress or dynamic instability invalidates the design. A response that is numerically precise but sensitive to unmeasured clearances should be given as a qualified estimate rather than a certified value.

## Test and reproducibility plan

**Investigation:** Compare side-load proxy against cam angle for two base-circle sizes. Record the drawing and initial settings before running the test. An appropriate student exercise can use slow, guarded motion, video tracking, or a separate numerical implementation; an energized high-speed experiment needs professional safety controls. Document reference length, sampling interval, calibration method and expected uncertainty. Compare at least three configurations, including a near-boundary case if it can be studied safely. Keep synthetic values separated from measured observations, and do not count the same input data as independent validation.

The report should contain a labeled schematic, equations, raw input table, one calculated output and its units, a sensitivity result and a discrepancy explanation. If an observed path differs from the model, consider perspective error, misidentified joints, slippage, structural flexibility, bearing clearance and unintended motion. Decide which extra measurement would distinguish the most plausible causes. A useful verification plan explains not only what evidence would support a model but what evidence would require it to be revised.

## Exercises and assessment

1. **Numerical variation:** Recalculate the worked example after changing one driving parameter by 15%. State the new answer, its units and the percentage change. Identify any hidden domain restriction, such as a minimum rod length or positive stiffness.
2. **Mechanism reasoning:** Why can a high-speed cam experience excessive side thrust? Contrast the original situation with a changed link, joint, contact condition or speed regime. Draw the new physical picture and explain which equation remains valid, requires modification or fails.
3. **Model critique:** Design an independent test for the proposed investigation, including measured variables, instrument calibration, repeatability, one confounding factor and a rejection criterion.

## Design review conclusion

**Pressure angle and follower contact** provides one part of a complete machine analysis. Deliver a brief calculation memo with an explicit operating range and at least one technical limitation. Evaluate the result against mechanism geometry and energy conservation, and list any unresolved requirements for guards, rated components, fatigue testing, maintenance or industrial standards before suggesting construction. A model is only one line of evidence; physical tests and responsible engineering judgment remain necessary.


---

# U05-L05 — Geneva drives and intermittent indexing

**Unit 5: Cams, Followers and Indexing Mechanisms · University-level learning draft · All examples synthetic**

## Engineering question and geometry

**Question:** How can a rotating crank produce an indexed output with dwell?

**Scenario:** A packaging table indexes between six equally spaced stations. Begin by drawing the machine in one reference configuration, identifying the ground, the input actuator and the intended output variable. Treat the device as a rigid planar assembly only if its geometry and operating conditions justify that approximation. Mark fixed points, moving joints, relevant dimensions, motion signs and any physical stop or contact condition. A computer animation is useful for communicating the proposed motion, but it cannot demonstrate that the physical parts have sufficient clearance or that the arrangement is safe.

## Principle, constraints and derivation

**Governing relation:** `Index step angle=2π/N for N equally spaced slots`.

Slot impact and high accelerations can limit speed; practical designs require guards and shock and wear analysis. A motion program comprises rise, dwell, return and dwell segments; its derivatives determine severity. Differentiate with respect to cam angle first, then multiply by angular speed according to the chain rule. If cam speed changes with time, acceleration includes a separate angular-acceleration term. A continuous displacement profile can have a velocity jump at an interval boundary unless the rise law is carefully chosen. Follower contact requires a compressive normal reaction and acceptable pressure angle. A purely prescribed follower path does not show that spring preload, gravity and inertia maintain contact. Indexing mechanisms add impact and dwell stability questions absent from a steady speed ratio.

Define each independent quantity and units before substitution. If a formula contains an angle derivative, convert degrees to radians and apply the chain rule to move from angle to time. For a constrained mechanism, first solve position closure and then differentiate to obtain velocity and acceleration. For a loaded mechanism, separate the purely kinematic result from required contact reactions and input torque. Identify when the formula assumes a fixed pivot, a constant input speed, a continuously engaged contact, or one assembly branch. A physically meaningful calculation states its domain, not just its output.

## Worked numerical case

**Illustrative inputs:** Geneva output wheel with six equally spaced index slots.

**Calculation — Index step for six slots:** **60 degrees**. These values were chosen for teaching, not measured from machinery. Put each input and its unit on a separate line in a reproducible calculation sheet, then verify the arithmetic with an independent computation. The sign of a rotational quantity indicates orientation; it does not imply an error. When the output is a force, check the implied work and reaction path. When it is a geometric dimension, check the assembly envelope and the full intended motion cycle, not only the illustrated pose.

**Sanity test:** Vary one relevant parameter by 10% and classify the resulting trend as linear, inverse, quadratic or configuration-dependent. Consider a near-limit case and ask which assumption would fail first. The calculation cannot independently prove its own assumptions: a derived value must eventually be compared with a separate observation, compatible published reference or physically grounded second model.

## Engineering interpretation and counterexample

**Frequent mistake:** Treating a Geneva wheel as moving at constant angular speed during each index.

**Specific sensitivity investigation:** Increase the Geneva slot count from six to eight. Compare index step and the possible impact on dwell and mechanism geometry. State what is held fixed, what changes and whether the output should be continuous. For closed-loop linkages, a second numerical solution may correspond to a different assembly branch; continuous angle tracking and a small closure residual are essential. For cams, belts, transmissions and vibration models, identify contact state, speed range and sources of energy dissipation. If a model produces exceptionally high speed or force near an ideal singularity, report the sensitivity and stop short of treating an unbounded prediction as achievable hardware performance.

A result matters when it can influence an engineering decision: mechanism selection, operating speed, joint configuration, allowable tolerance or actuator requirement. Always distinguish theoretical feasibility from reliability over many cycles. Geometry can be correct while friction, wear, fatigue, excessive contact stress or dynamic instability invalidates the design. A response that is numerically precise but sensitive to unmeasured clearances should be given as a qualified estimate rather than a certified value.

## Test and reproducibility plan

**Investigation:** Measure dwell angle and index time for a six-slot demonstrator. Record the drawing and initial settings before running the test. An appropriate student exercise can use slow, guarded motion, video tracking, or a separate numerical implementation; an energized high-speed experiment needs professional safety controls. Document reference length, sampling interval, calibration method and expected uncertainty. Compare at least three configurations, including a near-boundary case if it can be studied safely. Keep synthetic values separated from measured observations, and do not count the same input data as independent validation.

The report should contain a labeled schematic, equations, raw input table, one calculated output and its units, a sensitivity result and a discrepancy explanation. If an observed path differs from the model, consider perspective error, misidentified joints, slippage, structural flexibility, bearing clearance and unintended motion. Decide which extra measurement would distinguish the most plausible causes. A useful verification plan explains not only what evidence would support a model but what evidence would require it to be revised.

## Exercises and assessment

1. **Numerical variation:** Recalculate the worked example after changing one driving parameter by 15%. State the new answer, its units and the percentage change. Identify any hidden domain restriction, such as a minimum rod length or positive stiffness.
2. **Mechanism reasoning:** How can a rotating crank produce an indexed output with dwell? Contrast the original situation with a changed link, joint, contact condition or speed regime. Draw the new physical picture and explain which equation remains valid, requires modification or fails.
3. **Model critique:** Design an independent test for the proposed investigation, including measured variables, instrument calibration, repeatability, one confounding factor and a rejection criterion.

## Design review conclusion

**Geneva drives and intermittent indexing** provides one part of a complete machine analysis. Deliver a brief calculation memo with an explicit operating range and at least one technical limitation. Evaluate the result against mechanism geometry and energy conservation, and list any unresolved requirements for guards, rated components, fatigue testing, maintenance or industrial standards before suggesting construction. A model is only one line of evidence; physical tests and responsible engineering judgment remain necessary.


---

