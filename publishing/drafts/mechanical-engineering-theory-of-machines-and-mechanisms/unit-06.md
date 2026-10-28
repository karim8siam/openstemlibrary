# Unit 06: Machine Forces, Inertia and Energy

**Course Code**: TMM 206 · **Level**: Advanced Undergraduate Engineering

## Unit Overview & Physical Foundations

This comprehensive university textbook unit covers the theoretical framework, physical modeling, mathematical governing equations, and engineering applications of **Machine Forces, Inertia and Energy**.

# U06-L01 — Inertial torque of a rotor

**Unit 6: Machine Forces, Inertia and Energy · University-level learning draft · All examples synthetic**

## Engineering question and geometry

**Question:** What torque is required just to accelerate a machine component?

**Scenario:** A flywheel with moment of inertia 0.12 kg m² accelerates from rest at 20 rad/s². Begin by drawing the machine in one reference configuration, identifying the ground, the input actuator and the intended output variable. Treat the device as a rigid planar assembly only if its geometry and operating conditions justify that approximation. Mark fixed points, moving joints, relevant dimensions, motion signs and any physical stop or contact condition. A computer animation is useful for communicating the proposed motion, but it cannot demonstrate that the physical parts have sufficient clearance or that the arrangement is safe.

## Principle, constraints and derivation

**Governing relation:** `T_inertia=Iα`.

I is measured about the chosen rotational axis; parallel-axis corrections matter when the axis changes. Forces must be mapped onto the correctly accelerated bodies. Draw each free-body diagram with joint reactions, weight, actuator input, external load and friction where relevant; then use Newton–Euler equations consistently. Moment of inertia is defined about the actual rotation axis and should not be confused with the area second moment used in beam bending. Virtual work offers a useful check of torque and output force when an instantaneous displacement ratio is known. Work–energy provides a cycle-level audit: kinetic energy changes cannot be hidden inside a claimed motor efficiency. A flywheel stores and releases energy over a cycle; it does not add net cycle work.

Define each independent quantity and units before substitution. If a formula contains an angle derivative, convert degrees to radians and apply the chain rule to move from angle to time. For a constrained mechanism, first solve position closure and then differentiate to obtain velocity and acceleration. For a loaded mechanism, separate the purely kinematic result from required contact reactions and input torque. Identify when the formula assumes a fixed pivot, a constant input speed, a continuously engaged contact, or one assembly branch. A physically meaningful calculation states its domain, not just its output.

## Worked numerical case

**Illustrative inputs:** Moment of inertia 0.12 kg·m²; angular acceleration 20 rad/s².

**Calculation — Rotor accelerating torque:** **2.4 N·m**. These values were chosen for teaching, not measured from machinery. Put each input and its unit on a separate line in a reproducible calculation sheet, then verify the arithmetic with an independent computation. The sign of a rotational quantity indicates orientation; it does not imply an error. When the output is a force, check the implied work and reaction path. When it is a geometric dimension, check the assembly envelope and the full intended motion cycle, not only the illustrated pose.

**Sanity test:** Vary one relevant parameter by 10% and classify the resulting trend as linear, inverse, quadratic or configuration-dependent. Consider a near-limit case and ask which assumption would fail first. The calculation cannot independently prove its own assumptions: a derived value must eventually be compared with a separate observation, compatible published reference or physically grounded second model.

## Engineering interpretation and counterexample

**Frequent mistake:** Using the body's mass instead of its mass moment of inertia about the axis.

**Specific sensitivity investigation:** Double the rotor moment of inertia at fixed angular acceleration. Interpret the torque increase and energy consequence. State what is held fixed, what changes and whether the output should be continuous. For closed-loop linkages, a second numerical solution may correspond to a different assembly branch; continuous angle tracking and a small closure residual are essential. For cams, belts, transmissions and vibration models, identify contact state, speed range and sources of energy dissipation. If a model produces exceptionally high speed or force near an ideal singularity, report the sensitivity and stop short of treating an unbounded prediction as achievable hardware performance.

A result matters when it can influence an engineering decision: mechanism selection, operating speed, joint configuration, allowable tolerance or actuator requirement. Always distinguish theoretical feasibility from reliability over many cycles. Geometry can be correct while friction, wear, fatigue, excessive contact stress or dynamic instability invalidates the design. A response that is numerically precise but sensitive to unmeasured clearances should be given as a qualified estimate rather than a certified value.

## Test and reproducibility plan

**Investigation:** Measure rotor angular acceleration from encoder data and compare motor-current trend. Record the drawing and initial settings before running the test. An appropriate student exercise can use slow, guarded motion, video tracking, or a separate numerical implementation; an energized high-speed experiment needs professional safety controls. Document reference length, sampling interval, calibration method and expected uncertainty. Compare at least three configurations, including a near-boundary case if it can be studied safely. Keep synthetic values separated from measured observations, and do not count the same input data as independent validation.

The report should contain a labeled schematic, equations, raw input table, one calculated output and its units, a sensitivity result and a discrepancy explanation. If an observed path differs from the model, consider perspective error, misidentified joints, slippage, structural flexibility, bearing clearance and unintended motion. Decide which extra measurement would distinguish the most plausible causes. A useful verification plan explains not only what evidence would support a model but what evidence would require it to be revised.

## Exercises and assessment

1. **Numerical variation:** Recalculate the worked example after changing one driving parameter by 15%. State the new answer, its units and the percentage change. Identify any hidden domain restriction, such as a minimum rod length or positive stiffness.
2. **Mechanism reasoning:** What torque is required just to accelerate a machine component? Contrast the original situation with a changed link, joint, contact condition or speed regime. Draw the new physical picture and explain which equation remains valid, requires modification or fails.
3. **Model critique:** Design an independent test for the proposed investigation, including measured variables, instrument calibration, repeatability, one confounding factor and a rejection criterion.

## Design review conclusion

**Inertial torque of a rotor** provides one part of a complete machine analysis. Deliver a brief calculation memo with an explicit operating range and at least one technical limitation. Evaluate the result against mechanism geometry and energy conservation, and list any unresolved requirements for guards, rated components, fatigue testing, maintenance or industrial standards before suggesting construction. A model is only one line of evidence; physical tests and responsible engineering judgment remain necessary.


---

# U06-L02 — D'Alembert's principle

**Unit 6: Machine Forces, Inertia and Energy · University-level learning draft · All examples synthetic**

## Engineering question and geometry

**Question:** How can a dynamic problem be drawn like a static free-body problem?

**Scenario:** An offset tool carriage accelerates under a motor force and guide reaction. Begin by drawing the machine in one reference configuration, identifying the ground, the input actuator and the intended output variable. Treat the device as a rigid planar assembly only if its geometry and operating conditions justify that approximation. Mark fixed points, moving joints, relevant dimensions, motion signs and any physical stop or contact condition. A computer animation is useful for communicating the proposed motion, but it cannot demonstrate that the physical parts have sufficient clearance or that the arrangement is safe.

## Principle, constraints and derivation

**Governing relation:** `ΣF−ma=0 and ΣM−Iα=0 in inertial form`.

Inertial terms are a bookkeeping device, not contact forces; use one sign convention consistently. Forces must be mapped onto the correctly accelerated bodies. Draw each free-body diagram with joint reactions, weight, actuator input, external load and friction where relevant; then use Newton–Euler equations consistently. Moment of inertia is defined about the actual rotation axis and should not be confused with the area second moment used in beam bending. Virtual work offers a useful check of torque and output force when an instantaneous displacement ratio is known. Work–energy provides a cycle-level audit: kinetic energy changes cannot be hidden inside a claimed motor efficiency. A flywheel stores and releases energy over a cycle; it does not add net cycle work.

Define each independent quantity and units before substitution. If a formula contains an angle derivative, convert degrees to radians and apply the chain rule to move from angle to time. For a constrained mechanism, first solve position closure and then differentiate to obtain velocity and acceleration. For a loaded mechanism, separate the purely kinematic result from required contact reactions and input torque. Identify when the formula assumes a fixed pivot, a constant input speed, a continuously engaged contact, or one assembly branch. A physically meaningful calculation states its domain, not just its output.

## Worked numerical case

**Illustrative inputs:** Translating body 8 kg, acceleration magnitude 3.5 m/s².

**Calculation — Inertial force magnitude:** **28 N**. These values were chosen for teaching, not measured from machinery. Put each input and its unit on a separate line in a reproducible calculation sheet, then verify the arithmetic with an independent computation. The sign of a rotational quantity indicates orientation; it does not imply an error. When the output is a force, check the implied work and reaction path. When it is a geometric dimension, check the assembly envelope and the full intended motion cycle, not only the illustrated pose.

**Sanity test:** Vary one relevant parameter by 10% and classify the resulting trend as linear, inverse, quadratic or configuration-dependent. Consider a near-limit case and ask which assumption would fail first. The calculation cannot independently prove its own assumptions: a derived value must eventually be compared with a separate observation, compatible published reference or physically grounded second model.

## Engineering interpretation and counterexample

**Frequent mistake:** Adding an inertia force but also retaining ma on the opposite side inconsistently.

**Specific sensitivity investigation:** Write the accelerating-body equation both with ΣF=ma and in inertia-force equilibrium form; reconcile the signs. State what is held fixed, what changes and whether the output should be continuous. For closed-loop linkages, a second numerical solution may correspond to a different assembly branch; continuous angle tracking and a small closure residual are essential. For cams, belts, transmissions and vibration models, identify contact state, speed range and sources of energy dissipation. If a model produces exceptionally high speed or force near an ideal singularity, report the sensitivity and stop short of treating an unbounded prediction as achievable hardware performance.

A result matters when it can influence an engineering decision: mechanism selection, operating speed, joint configuration, allowable tolerance or actuator requirement. Always distinguish theoretical feasibility from reliability over many cycles. Geometry can be correct while friction, wear, fatigue, excessive contact stress or dynamic instability invalidates the design. A response that is numerically precise but sensitive to unmeasured clearances should be given as a qualified estimate rather than a certified value.

## Test and reproducibility plan

**Investigation:** Create separate real-force and inertia-force diagrams and reconcile the two equations. Record the drawing and initial settings before running the test. An appropriate student exercise can use slow, guarded motion, video tracking, or a separate numerical implementation; an energized high-speed experiment needs professional safety controls. Document reference length, sampling interval, calibration method and expected uncertainty. Compare at least three configurations, including a near-boundary case if it can be studied safely. Keep synthetic values separated from measured observations, and do not count the same input data as independent validation.

The report should contain a labeled schematic, equations, raw input table, one calculated output and its units, a sensitivity result and a discrepancy explanation. If an observed path differs from the model, consider perspective error, misidentified joints, slippage, structural flexibility, bearing clearance and unintended motion. Decide which extra measurement would distinguish the most plausible causes. A useful verification plan explains not only what evidence would support a model but what evidence would require it to be revised.

## Exercises and assessment

1. **Numerical variation:** Recalculate the worked example after changing one driving parameter by 15%. State the new answer, its units and the percentage change. Identify any hidden domain restriction, such as a minimum rod length or positive stiffness.
2. **Mechanism reasoning:** How can a dynamic problem be drawn like a static free-body problem? Contrast the original situation with a changed link, joint, contact condition or speed regime. Draw the new physical picture and explain which equation remains valid, requires modification or fails.
3. **Model critique:** Design an independent test for the proposed investigation, including measured variables, instrument calibration, repeatability, one confounding factor and a rejection criterion.

## Design review conclusion

**D'Alembert's principle** provides one part of a complete machine analysis. Deliver a brief calculation memo with an explicit operating range and at least one technical limitation. Evaluate the result against mechanism geometry and energy conservation, and list any unresolved requirements for guards, rated components, fatigue testing, maintenance or industrial standards before suggesting construction. A model is only one line of evidence; physical tests and responsible engineering judgment remain necessary.


---

# U06-L03 — Virtual work and generalized force

**Unit 6: Machine Forces, Inertia and Energy · University-level learning draft · All examples synthetic**

## Engineering question and geometry

**Question:** How can a linear output load be converted into an input-shaft torque?

**Scenario:** A crank must lift a load through a linkage whose instantaneous displacement ratio varies. Begin by drawing the machine in one reference configuration, identifying the ground, the input actuator and the intended output variable. Treat the device as a rigid planar assembly only if its geometry and operating conditions justify that approximation. Mark fixed points, moving joints, relevant dimensions, motion signs and any physical stop or contact condition. A computer animation is useful for communicating the proposed motion, but it cannot demonstrate that the physical parts have sufficient clearance or that the arrangement is safe.

## Principle, constraints and derivation

**Governing relation:** `Qθ=F·(dr/dθ), with sign from virtual displacement`.

At a singularity the displacement ratio and force transmission can change sharply; friction and compliance are excluded in the ideal result. Forces must be mapped onto the correctly accelerated bodies. Draw each free-body diagram with joint reactions, weight, actuator input, external load and friction where relevant; then use Newton–Euler equations consistently. Moment of inertia is defined about the actual rotation axis and should not be confused with the area second moment used in beam bending. Virtual work offers a useful check of torque and output force when an instantaneous displacement ratio is known. Work–energy provides a cycle-level audit: kinetic energy changes cannot be hidden inside a claimed motor efficiency. A flywheel stores and releases energy over a cycle; it does not add net cycle work.

Define each independent quantity and units before substitution. If a formula contains an angle derivative, convert degrees to radians and apply the chain rule to move from angle to time. For a constrained mechanism, first solve position closure and then differentiate to obtain velocity and acceleration. For a loaded mechanism, separate the purely kinematic result from required contact reactions and input torque. Identify when the formula assumes a fixed pivot, a constant input speed, a continuously engaged contact, or one assembly branch. A physically meaningful calculation states its domain, not just its output.

## Worked numerical case

**Illustrative inputs:** Useful output force 500 N; local displacement ratio dr/dθ=0.023 m/rad.

**Calculation — Virtual-work shaft torque:** **11.5 N·m**. These values were chosen for teaching, not measured from machinery. Put each input and its unit on a separate line in a reproducible calculation sheet, then verify the arithmetic with an independent computation. The sign of a rotational quantity indicates orientation; it does not imply an error. When the output is a force, check the implied work and reaction path. When it is a geometric dimension, check the assembly envelope and the full intended motion cycle, not only the illustrated pose.

**Sanity test:** Vary one relevant parameter by 10% and classify the resulting trend as linear, inverse, quadratic or configuration-dependent. Consider a near-limit case and ask which assumption would fail first. The calculation cannot independently prove its own assumptions: a derived value must eventually be compared with a separate observation, compatible published reference or physically grounded second model.

## Engineering interpretation and counterexample

**Frequent mistake:** Multiplying force by crank radius when the output motion is not tangential to that crank.

**Specific sensitivity investigation:** Decrease the mechanism output-displacement gradient near a dead center. Predict how the ideal input torque required for a fixed output force changes. State what is held fixed, what changes and whether the output should be continuous. For closed-loop linkages, a second numerical solution may correspond to a different assembly branch; continuous angle tracking and a small closure residual are essential. For cams, belts, transmissions and vibration models, identify contact state, speed range and sources of energy dissipation. If a model produces exceptionally high speed or force near an ideal singularity, report the sensitivity and stop short of treating an unbounded prediction as achievable hardware performance.

A result matters when it can influence an engineering decision: mechanism selection, operating speed, joint configuration, allowable tolerance or actuator requirement. Always distinguish theoretical feasibility from reliability over many cycles. Geometry can be correct while friction, wear, fatigue, excessive contact stress or dynamic instability invalidates the design. A response that is numerically precise but sensitive to unmeasured clearances should be given as a qualified estimate rather than a certified value.

## Test and reproducibility plan

**Investigation:** Measure the output displacement per small input angle and compare virtual-work torque. Record the drawing and initial settings before running the test. An appropriate student exercise can use slow, guarded motion, video tracking, or a separate numerical implementation; an energized high-speed experiment needs professional safety controls. Document reference length, sampling interval, calibration method and expected uncertainty. Compare at least three configurations, including a near-boundary case if it can be studied safely. Keep synthetic values separated from measured observations, and do not count the same input data as independent validation.

The report should contain a labeled schematic, equations, raw input table, one calculated output and its units, a sensitivity result and a discrepancy explanation. If an observed path differs from the model, consider perspective error, misidentified joints, slippage, structural flexibility, bearing clearance and unintended motion. Decide which extra measurement would distinguish the most plausible causes. A useful verification plan explains not only what evidence would support a model but what evidence would require it to be revised.

## Exercises and assessment

1. **Numerical variation:** Recalculate the worked example after changing one driving parameter by 15%. State the new answer, its units and the percentage change. Identify any hidden domain restriction, such as a minimum rod length or positive stiffness.
2. **Mechanism reasoning:** How can a linear output load be converted into an input-shaft torque? Contrast the original situation with a changed link, joint, contact condition or speed regime. Draw the new physical picture and explain which equation remains valid, requires modification or fails.
3. **Model critique:** Design an independent test for the proposed investigation, including measured variables, instrument calibration, repeatability, one confounding factor and a rejection criterion.

## Design review conclusion

**Virtual work and generalized force** provides one part of a complete machine analysis. Deliver a brief calculation memo with an explicit operating range and at least one technical limitation. Evaluate the result against mechanism geometry and energy conservation, and list any unresolved requirements for guards, rated components, fatigue testing, maintenance or industrial standards before suggesting construction. A model is only one line of evidence; physical tests and responsible engineering judgment remain necessary.


---

# U06-L04 — Work and energy of a mechanism

**Unit 6: Machine Forces, Inertia and Energy · University-level learning draft · All examples synthetic**

## Engineering question and geometry

**Question:** Why may a motor need high instantaneous torque even when average power is modest?

**Scenario:** An indexing table accelerates and brakes heavy tooling twice per cycle. Begin by drawing the machine in one reference configuration, identifying the ground, the input actuator and the intended output variable. Treat the device as a rigid planar assembly only if its geometry and operating conditions justify that approximation. Mark fixed points, moving joints, relevant dimensions, motion signs and any physical stop or contact condition. A computer animation is useful for communicating the proposed motion, but it cannot demonstrate that the physical parts have sufficient clearance or that the arrangement is safe.

## Principle, constraints and derivation

**Governing relation:** `ΔK=W_input−W_losses−W_load`.

The balance can predict energy demand but not contact stress without additional geometry and force analysis. Forces must be mapped onto the correctly accelerated bodies. Draw each free-body diagram with joint reactions, weight, actuator input, external load and friction where relevant; then use Newton–Euler equations consistently. Moment of inertia is defined about the actual rotation axis and should not be confused with the area second moment used in beam bending. Virtual work offers a useful check of torque and output force when an instantaneous displacement ratio is known. Work–energy provides a cycle-level audit: kinetic energy changes cannot be hidden inside a claimed motor efficiency. A flywheel stores and releases energy over a cycle; it does not add net cycle work.

Define each independent quantity and units before substitution. If a formula contains an angle derivative, convert degrees to radians and apply the chain rule to move from angle to time. For a constrained mechanism, first solve position closure and then differentiate to obtain velocity and acceleration. For a loaded mechanism, separate the purely kinematic result from required contact reactions and input torque. Identify when the formula assumes a fixed pivot, a constant input speed, a continuously engaged contact, or one assembly branch. A physically meaningful calculation states its domain, not just its output.

## Worked numerical case

**Illustrative inputs:** Rotational inertia 0.25 kg·m², accelerated from 20 to 30 rad/s.

**Calculation — Energy increase:** **62.5 J**. These values were chosen for teaching, not measured from machinery. Put each input and its unit on a separate line in a reproducible calculation sheet, then verify the arithmetic with an independent computation. The sign of a rotational quantity indicates orientation; it does not imply an error. When the output is a force, check the implied work and reaction path. When it is a geometric dimension, check the assembly envelope and the full intended motion cycle, not only the illustrated pose.

**Sanity test:** Vary one relevant parameter by 10% and classify the resulting trend as linear, inverse, quadratic or configuration-dependent. Consider a near-limit case and ask which assumption would fail first. The calculation cannot independently prove its own assumptions: a derived value must eventually be compared with a separate observation, compatible published reference or physically grounded second model.

## Engineering interpretation and counterexample

**Frequent mistake:** Dividing total work by cycle time and assuming the result determines peak torque.

**Specific sensitivity investigation:** Compare a steady-speed indexer with an accelerate–dwell–decelerate program; show why equal net work does not imply equal peak demand. State what is held fixed, what changes and whether the output should be continuous. For closed-loop linkages, a second numerical solution may correspond to a different assembly branch; continuous angle tracking and a small closure residual are essential. For cams, belts, transmissions and vibration models, identify contact state, speed range and sources of energy dissipation. If a model produces exceptionally high speed or force near an ideal singularity, report the sensitivity and stop short of treating an unbounded prediction as achievable hardware performance.

A result matters when it can influence an engineering decision: mechanism selection, operating speed, joint configuration, allowable tolerance or actuator requirement. Always distinguish theoretical feasibility from reliability over many cycles. Geometry can be correct while friction, wear, fatigue, excessive contact stress or dynamic instability invalidates the design. A response that is numerically precise but sensitive to unmeasured clearances should be given as a qualified estimate rather than a certified value.

## Test and reproducibility plan

**Investigation:** Compare measured instantaneous electrical power and angular speed over a complete cycle. Record the drawing and initial settings before running the test. An appropriate student exercise can use slow, guarded motion, video tracking, or a separate numerical implementation; an energized high-speed experiment needs professional safety controls. Document reference length, sampling interval, calibration method and expected uncertainty. Compare at least three configurations, including a near-boundary case if it can be studied safely. Keep synthetic values separated from measured observations, and do not count the same input data as independent validation.

The report should contain a labeled schematic, equations, raw input table, one calculated output and its units, a sensitivity result and a discrepancy explanation. If an observed path differs from the model, consider perspective error, misidentified joints, slippage, structural flexibility, bearing clearance and unintended motion. Decide which extra measurement would distinguish the most plausible causes. A useful verification plan explains not only what evidence would support a model but what evidence would require it to be revised.

## Exercises and assessment

1. **Numerical variation:** Recalculate the worked example after changing one driving parameter by 15%. State the new answer, its units and the percentage change. Identify any hidden domain restriction, such as a minimum rod length or positive stiffness.
2. **Mechanism reasoning:** Why may a motor need high instantaneous torque even when average power is modest? Contrast the original situation with a changed link, joint, contact condition or speed regime. Draw the new physical picture and explain which equation remains valid, requires modification or fails.
3. **Model critique:** Design an independent test for the proposed investigation, including measured variables, instrument calibration, repeatability, one confounding factor and a rejection criterion.

## Design review conclusion

**Work and energy of a mechanism** provides one part of a complete machine analysis. Deliver a brief calculation memo with an explicit operating range and at least one technical limitation. Evaluate the result against mechanism geometry and energy conservation, and list any unresolved requirements for guards, rated components, fatigue testing, maintenance or industrial standards before suggesting construction. A model is only one line of evidence; physical tests and responsible engineering judgment remain necessary.


---

# U06-L05 — Flywheel energy storage and speed regulation

**Unit 6: Machine Forces, Inertia and Energy · University-level learning draft · All examples synthetic**

## Engineering question and geometry

**Question:** How can a flywheel moderate speed fluctuation without supplying net cycle energy?

**Scenario:** A mechanical press has a brief high-demand segment in each cycle. Begin by drawing the machine in one reference configuration, identifying the ground, the input actuator and the intended output variable. Treat the device as a rigid planar assembly only if its geometry and operating conditions justify that approximation. Mark fixed points, moving joints, relevant dimensions, motion signs and any physical stop or contact condition. A computer animation is useful for communicating the proposed motion, but it cannot demonstrate that the physical parts have sufficient clearance or that the arrangement is safe.

## Principle, constraints and derivation

**Governing relation:** `E=0.5Iω²`.

Only the difference between maximum and minimum kinetic energy is available for smoothing under a chosen speed tolerance. Forces must be mapped onto the correctly accelerated bodies. Draw each free-body diagram with joint reactions, weight, actuator input, external load and friction where relevant; then use Newton–Euler equations consistently. Moment of inertia is defined about the actual rotation axis and should not be confused with the area second moment used in beam bending. Virtual work offers a useful check of torque and output force when an instantaneous displacement ratio is known. Work–energy provides a cycle-level audit: kinetic energy changes cannot be hidden inside a claimed motor efficiency. A flywheel stores and releases energy over a cycle; it does not add net cycle work.

Define each independent quantity and units before substitution. If a formula contains an angle derivative, convert degrees to radians and apply the chain rule to move from angle to time. For a constrained mechanism, first solve position closure and then differentiate to obtain velocity and acceleration. For a loaded mechanism, separate the purely kinematic result from required contact reactions and input torque. Identify when the formula assumes a fixed pivot, a constant input speed, a continuously engaged contact, or one assembly branch. A physically meaningful calculation states its domain, not just its output.

## Worked numerical case

**Illustrative inputs:** Flywheel inertia 0.4 kg·m² and shaft speed 24 rad/s.

**Calculation — Flywheel stored kinetic energy:** **115.2 J**. These values were chosen for teaching, not measured from machinery. Put each input and its unit on a separate line in a reproducible calculation sheet, then verify the arithmetic with an independent computation. The sign of a rotational quantity indicates orientation; it does not imply an error. When the output is a force, check the implied work and reaction path. When it is a geometric dimension, check the assembly envelope and the full intended motion cycle, not only the illustrated pose.

**Sanity test:** Vary one relevant parameter by 10% and classify the resulting trend as linear, inverse, quadratic or configuration-dependent. Consider a near-limit case and ask which assumption would fail first. The calculation cannot independently prove its own assumptions: a derived value must eventually be compared with a separate observation, compatible published reference or physically grounded second model.

## Engineering interpretation and counterexample

**Frequent mistake:** Equating flywheel kinetic energy with useful energy released while ignoring minimum speed.

**Specific sensitivity investigation:** Decrease flywheel speed by ten percent and quantify why available kinetic energy falls faster than speed itself. State what is held fixed, what changes and whether the output should be continuous. For closed-loop linkages, a second numerical solution may correspond to a different assembly branch; continuous angle tracking and a small closure residual are essential. For cams, belts, transmissions and vibration models, identify contact state, speed range and sources of energy dissipation. If a model produces exceptionally high speed or force near an ideal singularity, report the sensitivity and stop short of treating an unbounded prediction as achievable hardware performance.

A result matters when it can influence an engineering decision: mechanism selection, operating speed, joint configuration, allowable tolerance or actuator requirement. Always distinguish theoretical feasibility from reliability over many cycles. Geometry can be correct while friction, wear, fatigue, excessive contact stress or dynamic instability invalidates the design. A response that is numerically precise but sensitive to unmeasured clearances should be given as a qualified estimate rather than a certified value.

## Test and reproducibility plan

**Investigation:** Record flywheel speed at several points and compute the difference in stored kinetic energy. Record the drawing and initial settings before running the test. An appropriate student exercise can use slow, guarded motion, video tracking, or a separate numerical implementation; an energized high-speed experiment needs professional safety controls. Document reference length, sampling interval, calibration method and expected uncertainty. Compare at least three configurations, including a near-boundary case if it can be studied safely. Keep synthetic values separated from measured observations, and do not count the same input data as independent validation.

The report should contain a labeled schematic, equations, raw input table, one calculated output and its units, a sensitivity result and a discrepancy explanation. If an observed path differs from the model, consider perspective error, misidentified joints, slippage, structural flexibility, bearing clearance and unintended motion. Decide which extra measurement would distinguish the most plausible causes. A useful verification plan explains not only what evidence would support a model but what evidence would require it to be revised.

## Exercises and assessment

1. **Numerical variation:** Recalculate the worked example after changing one driving parameter by 15%. State the new answer, its units and the percentage change. Identify any hidden domain restriction, such as a minimum rod length or positive stiffness.
2. **Mechanism reasoning:** How can a flywheel moderate speed fluctuation without supplying net cycle energy? Contrast the original situation with a changed link, joint, contact condition or speed regime. Draw the new physical picture and explain which equation remains valid, requires modification or fails.
3. **Model critique:** Design an independent test for the proposed investigation, including measured variables, instrument calibration, repeatability, one confounding factor and a rejection criterion.

## Design review conclusion

**Flywheel energy storage and speed regulation** provides one part of a complete machine analysis. Deliver a brief calculation memo with an explicit operating range and at least one technical limitation. Evaluate the result against mechanism geometry and energy conservation, and list any unresolved requirements for guards, rated components, fatigue testing, maintenance or industrial standards before suggesting construction. A model is only one line of evidence; physical tests and responsible engineering judgment remain necessary.


---

