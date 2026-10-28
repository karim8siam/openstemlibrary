# Unit 07: Balancing, Vibrations and Dynamic Response

**Course Code**: TMM 207 · **Level**: Advanced Undergraduate Engineering

## Unit Overview & Physical Foundations

This comprehensive university textbook unit covers the theoretical framework, physical modeling, mathematical governing equations, and engineering applications of **Balancing, Vibrations and Dynamic Response**.

# U07-L01 — Static unbalance force

**Unit 7: Balancing, Vibrations and Dynamic Response · University-level learning draft · All examples synthetic**

## Engineering question and geometry

**Question:** Why can tiny rotor eccentricity cause large loads at high speed?

**Scenario:** A wheel has 0.02 kg unbalanced equivalent mass at 8 mm radius while spinning rapidly. Begin by drawing the machine in one reference configuration, identifying the ground, the input actuator and the intended output variable. Treat the device as a rigid planar assembly only if its geometry and operating conditions justify that approximation. Mark fixed points, moving joints, relevant dimensions, motion signs and any physical stop or contact condition. A computer animation is useful for communicating the proposed motion, but it cannot demonstrate that the physical parts have sufficient clearance or that the arrangement is safe.

## Principle, constraints and derivation

**Governing relation:** `F=meω²`.

A single force approximation cannot fully represent couple unbalance or flexible-rotor modes. An equivalent single-degree-of-freedom oscillator captures one dominant mode but not an entire flexible structure. Establish measured mass, restoring stiffness, damping mechanism and excitation spectrum. Convert between angular frequency and cycles per second before comparing machine rpm with mode frequencies. Unbalance excitation grows as speed squared, so high-speed validation is safety-critical even for a small eccentricity. Balancing vectors require both magnitude and angular phase. Isolation must be evaluated over the whole startup and run-down speed range because a soft mount may pass through a resonant region. Real foundations and bearings can couple horizontal, vertical and torsional modes.

Define each independent quantity and units before substitution. If a formula contains an angle derivative, convert degrees to radians and apply the chain rule to move from angle to time. For a constrained mechanism, first solve position closure and then differentiate to obtain velocity and acceleration. For a loaded mechanism, separate the purely kinematic result from required contact reactions and input torque. Identify when the formula assumes a fixed pivot, a constant input speed, a continuously engaged contact, or one assembly branch. A physically meaningful calculation states its domain, not just its output.

## Worked numerical case

**Illustrative inputs:** Unbalance equivalent mass 0.02 kg at eccentricity 8 mm and speed 100 rad/s.

**Calculation — Unbalance centrifugal force:** **1.6 N**. These values were chosen for teaching, not measured from machinery. Put each input and its unit on a separate line in a reproducible calculation sheet, then verify the arithmetic with an independent computation. The sign of a rotational quantity indicates orientation; it does not imply an error. When the output is a force, check the implied work and reaction path. When it is a geometric dimension, check the assembly envelope and the full intended motion cycle, not only the illustrated pose.

**Sanity test:** Vary one relevant parameter by 10% and classify the resulting trend as linear, inverse, quadratic or configuration-dependent. Consider a near-limit case and ask which assumption would fail first. The calculation cannot independently prove its own assumptions: a derived value must eventually be compared with a separate observation, compatible published reference or physically grounded second model.

## Engineering interpretation and counterexample

**Frequent mistake:** Assuming unbalance force rises linearly, rather than quadratically, with rotational speed.

**Specific sensitivity investigation:** Double rotation speed with the same eccentric mass and radius. Deduce the fourfold increase in the simplified unbalance force. State what is held fixed, what changes and whether the output should be continuous. For closed-loop linkages, a second numerical solution may correspond to a different assembly branch; continuous angle tracking and a small closure residual are essential. For cams, belts, transmissions and vibration models, identify contact state, speed range and sources of energy dissipation. If a model produces exceptionally high speed or force near an ideal singularity, report the sensitivity and stop short of treating an unbounded prediction as achievable hardware performance.

A result matters when it can influence an engineering decision: mechanism selection, operating speed, joint configuration, allowable tolerance or actuator requirement. Always distinguish theoretical feasibility from reliability over many cycles. Geometry can be correct while friction, wear, fatigue, excessive contact stress or dynamic instability invalidates the design. A response that is numerically precise but sensitive to unmeasured clearances should be given as a qualified estimate rather than a certified value.

## Test and reproducibility plan

**Investigation:** Using a safely enclosed low-speed test rig, measure excitation trend with shaft speed. Record the drawing and initial settings before running the test. An appropriate student exercise can use slow, guarded motion, video tracking, or a separate numerical implementation; an energized high-speed experiment needs professional safety controls. Document reference length, sampling interval, calibration method and expected uncertainty. Compare at least three configurations, including a near-boundary case if it can be studied safely. Keep synthetic values separated from measured observations, and do not count the same input data as independent validation.

The report should contain a labeled schematic, equations, raw input table, one calculated output and its units, a sensitivity result and a discrepancy explanation. If an observed path differs from the model, consider perspective error, misidentified joints, slippage, structural flexibility, bearing clearance and unintended motion. Decide which extra measurement would distinguish the most plausible causes. A useful verification plan explains not only what evidence would support a model but what evidence would require it to be revised.

## Exercises and assessment

1. **Numerical variation:** Recalculate the worked example after changing one driving parameter by 15%. State the new answer, its units and the percentage change. Identify any hidden domain restriction, such as a minimum rod length or positive stiffness.
2. **Mechanism reasoning:** Why can tiny rotor eccentricity cause large loads at high speed? Contrast the original situation with a changed link, joint, contact condition or speed regime. Draw the new physical picture and explain which equation remains valid, requires modification or fails.
3. **Model critique:** Design an independent test for the proposed investigation, including measured variables, instrument calibration, repeatability, one confounding factor and a rejection criterion.

## Design review conclusion

**Static unbalance force** provides one part of a complete machine analysis. Deliver a brief calculation memo with an explicit operating range and at least one technical limitation. Evaluate the result against mechanism geometry and energy conservation, and list any unresolved requirements for guards, rated components, fatigue testing, maintenance or industrial standards before suggesting construction. A model is only one line of evidence; physical tests and responsible engineering judgment remain necessary.


---

# U07-L02 — Rotating balancing vectors

**Unit 7: Balancing, Vibrations and Dynamic Response · University-level learning draft · All examples synthetic**

## Engineering question and geometry

**Question:** How should several eccentric masses be compensated in one plane?

**Scenario:** Two weights on a rotor are placed at different angles and need an equivalent correction mass. Begin by drawing the machine in one reference configuration, identifying the ground, the input actuator and the intended output variable. Treat the device as a rigid planar assembly only if its geometry and operating conditions justify that approximation. Mark fixed points, moving joints, relevant dimensions, motion signs and any physical stop or contact condition. A computer animation is useful for communicating the proposed motion, but it cannot demonstrate that the physical parts have sufficient clearance or that the arrangement is safe.

## Principle, constraints and derivation

**Governing relation:** `Σ(m_i r_i e^{jθ_i})=0 for one-plane static balance`.

One-plane correction addresses resultant mass eccentricity, not the couple generated by separated axial planes. An equivalent single-degree-of-freedom oscillator captures one dominant mode but not an entire flexible structure. Establish measured mass, restoring stiffness, damping mechanism and excitation spectrum. Convert between angular frequency and cycles per second before comparing machine rpm with mode frequencies. Unbalance excitation grows as speed squared, so high-speed validation is safety-critical even for a small eccentricity. Balancing vectors require both magnitude and angular phase. Isolation must be evaluated over the whole startup and run-down speed range because a soft mount may pass through a resonant region. Real foundations and bearings can couple horizontal, vertical and torsional modes.

Define each independent quantity and units before substitution. If a formula contains an angle derivative, convert degrees to radians and apply the chain rule to move from angle to time. For a constrained mechanism, first solve position closure and then differentiate to obtain velocity and acceleration. For a loaded mechanism, separate the purely kinematic result from required contact reactions and input torque. Identify when the formula assumes a fixed pivot, a constant input speed, a continuously engaged contact, or one assembly branch. A physically meaningful calculation states its domain, not just its output.

## Worked numerical case

**Illustrative inputs:** Existing unbalance mass 0.03 kg at 20 mm; balancing radius 40 mm; opposite phase.

**Calculation — Balancing equivalent correction mass:** **0.015 kg**. These values were chosen for teaching, not measured from machinery. Put each input and its unit on a separate line in a reproducible calculation sheet, then verify the arithmetic with an independent computation. The sign of a rotational quantity indicates orientation; it does not imply an error. When the output is a force, check the implied work and reaction path. When it is a geometric dimension, check the assembly envelope and the full intended motion cycle, not only the illustrated pose.

**Sanity test:** Vary one relevant parameter by 10% and classify the resulting trend as linear, inverse, quadratic or configuration-dependent. Consider a near-limit case and ask which assumption would fail first. The calculation cannot independently prove its own assumptions: a derived value must eventually be compared with a separate observation, compatible published reference or physically grounded second model.

## Engineering interpretation and counterexample

**Frequent mistake:** Adding eccentricities as scalars instead of phasors.

**Specific sensitivity investigation:** Change the angular position of a correction mass by ninety degrees; show that scalar magnitude matching no longer guarantees balance. State what is held fixed, what changes and whether the output should be continuous. For closed-loop linkages, a second numerical solution may correspond to a different assembly branch; continuous angle tracking and a small closure residual are essential. For cams, belts, transmissions and vibration models, identify contact state, speed range and sources of energy dissipation. If a model produces exceptionally high speed or force near an ideal singularity, report the sensitivity and stop short of treating an unbounded prediction as achievable hardware performance.

A result matters when it can influence an engineering decision: mechanism selection, operating speed, joint configuration, allowable tolerance or actuator requirement. Always distinguish theoretical feasibility from reliability over many cycles. Geometry can be correct while friction, wear, fatigue, excessive contact stress or dynamic instability invalidates the design. A response that is numerically precise but sensitive to unmeasured clearances should be given as a qualified estimate rather than a certified value.

## Test and reproducibility plan

**Investigation:** Construct a polar unbalance diagram and compare a bench rotor's heavy spot. Record the drawing and initial settings before running the test. An appropriate student exercise can use slow, guarded motion, video tracking, or a separate numerical implementation; an energized high-speed experiment needs professional safety controls. Document reference length, sampling interval, calibration method and expected uncertainty. Compare at least three configurations, including a near-boundary case if it can be studied safely. Keep synthetic values separated from measured observations, and do not count the same input data as independent validation.

The report should contain a labeled schematic, equations, raw input table, one calculated output and its units, a sensitivity result and a discrepancy explanation. If an observed path differs from the model, consider perspective error, misidentified joints, slippage, structural flexibility, bearing clearance and unintended motion. Decide which extra measurement would distinguish the most plausible causes. A useful verification plan explains not only what evidence would support a model but what evidence would require it to be revised.

## Exercises and assessment

1. **Numerical variation:** Recalculate the worked example after changing one driving parameter by 15%. State the new answer, its units and the percentage change. Identify any hidden domain restriction, such as a minimum rod length or positive stiffness.
2. **Mechanism reasoning:** How should several eccentric masses be compensated in one plane? Contrast the original situation with a changed link, joint, contact condition or speed regime. Draw the new physical picture and explain which equation remains valid, requires modification or fails.
3. **Model critique:** Design an independent test for the proposed investigation, including measured variables, instrument calibration, repeatability, one confounding factor and a rejection criterion.

## Design review conclusion

**Rotating balancing vectors** provides one part of a complete machine analysis. Deliver a brief calculation memo with an explicit operating range and at least one technical limitation. Evaluate the result against mechanism geometry and energy conservation, and list any unresolved requirements for guards, rated components, fatigue testing, maintenance or industrial standards before suggesting construction. A model is only one line of evidence; physical tests and responsible engineering judgment remain necessary.


---

# U07-L03 — Free vibration natural frequency

**Unit 7: Balancing, Vibrations and Dynamic Response · University-level learning draft · All examples synthetic**

## Engineering question and geometry

**Question:** Why does making a support stiffer shift rather than remove resonance?

**Scenario:** A small motor mount has an assumed equivalent stiffness and vibrating mass. Begin by drawing the machine in one reference configuration, identifying the ground, the input actuator and the intended output variable. Treat the device as a rigid planar assembly only if its geometry and operating conditions justify that approximation. Mark fixed points, moving joints, relevant dimensions, motion signs and any physical stop or contact condition. A computer animation is useful for communicating the proposed motion, but it cannot demonstrate that the physical parts have sufficient clearance or that the arrangement is safe.

## Principle, constraints and derivation

**Governing relation:** `ω_n=sqrt(k/m) for linear SDOF`.

Natural frequency depends on both mass and stiffness; nonlinear, distributed structures have multiple modes and amplitudes. An equivalent single-degree-of-freedom oscillator captures one dominant mode but not an entire flexible structure. Establish measured mass, restoring stiffness, damping mechanism and excitation spectrum. Convert between angular frequency and cycles per second before comparing machine rpm with mode frequencies. Unbalance excitation grows as speed squared, so high-speed validation is safety-critical even for a small eccentricity. Balancing vectors require both magnitude and angular phase. Isolation must be evaluated over the whole startup and run-down speed range because a soft mount may pass through a resonant region. Real foundations and bearings can couple horizontal, vertical and torsional modes.

Define each independent quantity and units before substitution. If a formula contains an angle derivative, convert degrees to radians and apply the chain rule to move from angle to time. For a constrained mechanism, first solve position closure and then differentiate to obtain velocity and acceleration. For a loaded mechanism, separate the purely kinematic result from required contact reactions and input torque. Identify when the formula assumes a fixed pivot, a constant input speed, a continuously engaged contact, or one assembly branch. A physically meaningful calculation states its domain, not just its output.

## Worked numerical case

**Illustrative inputs:** Equivalent mass 20 kg and linear stiffness 80,000 N/m.

**Calculation — Natural angular frequency:** **63.2456 rad/s**. These values were chosen for teaching, not measured from machinery. Put each input and its unit on a separate line in a reproducible calculation sheet, then verify the arithmetic with an independent computation. The sign of a rotational quantity indicates orientation; it does not imply an error. When the output is a force, check the implied work and reaction path. When it is a geometric dimension, check the assembly envelope and the full intended motion cycle, not only the illustrated pose.

**Sanity test:** Vary one relevant parameter by 10% and classify the resulting trend as linear, inverse, quadratic or configuration-dependent. Consider a near-limit case and ask which assumption would fail first. The calculation cannot independently prove its own assumptions: a derived value must eventually be compared with a separate observation, compatible published reference or physically grounded second model.

## Engineering interpretation and counterexample

**Frequent mistake:** Comparing frequencies in Hz and rad/s without the factor 2π.

**Specific sensitivity investigation:** Double stiffness of the support with unchanged mass. Show the square-root rise in natural frequency and its implications for excitation. State what is held fixed, what changes and whether the output should be continuous. For closed-loop linkages, a second numerical solution may correspond to a different assembly branch; continuous angle tracking and a small closure residual are essential. For cams, belts, transmissions and vibration models, identify contact state, speed range and sources of energy dissipation. If a model produces exceptionally high speed or force near an ideal singularity, report the sensitivity and stop short of treating an unbounded prediction as achievable hardware performance.

A result matters when it can influence an engineering decision: mechanism selection, operating speed, joint configuration, allowable tolerance or actuator requirement. Always distinguish theoretical feasibility from reliability over many cycles. Geometry can be correct while friction, wear, fatigue, excessive contact stress or dynamic instability invalidates the design. A response that is numerically precise but sensitive to unmeasured clearances should be given as a qualified estimate rather than a certified value.

## Test and reproducibility plan

**Investigation:** Measure period after a small displacement and estimate stiffness from a static load. Record the drawing and initial settings before running the test. An appropriate student exercise can use slow, guarded motion, video tracking, or a separate numerical implementation; an energized high-speed experiment needs professional safety controls. Document reference length, sampling interval, calibration method and expected uncertainty. Compare at least three configurations, including a near-boundary case if it can be studied safely. Keep synthetic values separated from measured observations, and do not count the same input data as independent validation.

The report should contain a labeled schematic, equations, raw input table, one calculated output and its units, a sensitivity result and a discrepancy explanation. If an observed path differs from the model, consider perspective error, misidentified joints, slippage, structural flexibility, bearing clearance and unintended motion. Decide which extra measurement would distinguish the most plausible causes. A useful verification plan explains not only what evidence would support a model but what evidence would require it to be revised.

## Exercises and assessment

1. **Numerical variation:** Recalculate the worked example after changing one driving parameter by 15%. State the new answer, its units and the percentage change. Identify any hidden domain restriction, such as a minimum rod length or positive stiffness.
2. **Mechanism reasoning:** Why does making a support stiffer shift rather than remove resonance? Contrast the original situation with a changed link, joint, contact condition or speed regime. Draw the new physical picture and explain which equation remains valid, requires modification or fails.
3. **Model critique:** Design an independent test for the proposed investigation, including measured variables, instrument calibration, repeatability, one confounding factor and a rejection criterion.

## Design review conclusion

**Free vibration natural frequency** provides one part of a complete machine analysis. Deliver a brief calculation memo with an explicit operating range and at least one technical limitation. Evaluate the result against mechanism geometry and energy conservation, and list any unresolved requirements for guards, rated components, fatigue testing, maintenance or industrial standards before suggesting construction. A model is only one line of evidence; physical tests and responsible engineering judgment remain necessary.


---

# U07-L04 — Viscous damping ratio

**Unit 7: Balancing, Vibrations and Dynamic Response · University-level learning draft · All examples synthetic**

## Engineering question and geometry

**Question:** When does damping reduce oscillation amplitude without changing static stiffness?

**Scenario:** A test mass on a damper takes several cycles to settle after a small release. Begin by drawing the machine in one reference configuration, identifying the ground, the input actuator and the intended output variable. Treat the device as a rigid planar assembly only if its geometry and operating conditions justify that approximation. Mark fixed points, moving joints, relevant dimensions, motion signs and any physical stop or contact condition. A computer animation is useful for communicating the proposed motion, but it cannot demonstrate that the physical parts have sufficient clearance or that the arrangement is safe.

## Principle, constraints and derivation

**Governing relation:** `ζ=c/(2sqrt(km)) for linear SDOF`.

Viscous damping is an idealization; Coulomb friction and hysteretic damping yield different response envelopes. An equivalent single-degree-of-freedom oscillator captures one dominant mode but not an entire flexible structure. Establish measured mass, restoring stiffness, damping mechanism and excitation spectrum. Convert between angular frequency and cycles per second before comparing machine rpm with mode frequencies. Unbalance excitation grows as speed squared, so high-speed validation is safety-critical even for a small eccentricity. Balancing vectors require both magnitude and angular phase. Isolation must be evaluated over the whole startup and run-down speed range because a soft mount may pass through a resonant region. Real foundations and bearings can couple horizontal, vertical and torsional modes.

Define each independent quantity and units before substitution. If a formula contains an angle derivative, convert degrees to radians and apply the chain rule to move from angle to time. For a constrained mechanism, first solve position closure and then differentiate to obtain velocity and acceleration. For a loaded mechanism, separate the purely kinematic result from required contact reactions and input torque. Identify when the formula assumes a fixed pivot, a constant input speed, a continuously engaged contact, or one assembly branch. A physically meaningful calculation states its domain, not just its output.

## Worked numerical case

**Illustrative inputs:** c=400 N·s/m, k=80,000 N/m, m=20 kg.

**Calculation — Viscous damping ratio:** **0.158114 dimensionless**. These values were chosen for teaching, not measured from machinery. Put each input and its unit on a separate line in a reproducible calculation sheet, then verify the arithmetic with an independent computation. The sign of a rotational quantity indicates orientation; it does not imply an error. When the output is a force, check the implied work and reaction path. When it is a geometric dimension, check the assembly envelope and the full intended motion cycle, not only the illustrated pose.

**Sanity test:** Vary one relevant parameter by 10% and classify the resulting trend as linear, inverse, quadratic or configuration-dependent. Consider a near-limit case and ask which assumption would fail first. The calculation cannot independently prove its own assumptions: a derived value must eventually be compared with a separate observation, compatible published reference or physically grounded second model.

## Engineering interpretation and counterexample

**Frequent mistake:** Assuming a lower decay rate necessarily means the spring became softer.

**Specific sensitivity investigation:** Double damping coefficient in the same linear oscillator. Discuss what changes in decay and what static deflection remains unchanged. State what is held fixed, what changes and whether the output should be continuous. For closed-loop linkages, a second numerical solution may correspond to a different assembly branch; continuous angle tracking and a small closure residual are essential. For cams, belts, transmissions and vibration models, identify contact state, speed range and sources of energy dissipation. If a model produces exceptionally high speed or force near an ideal singularity, report the sensitivity and stop short of treating an unbounded prediction as achievable hardware performance.

A result matters when it can influence an engineering decision: mechanism selection, operating speed, joint configuration, allowable tolerance or actuator requirement. Always distinguish theoretical feasibility from reliability over many cycles. Geometry can be correct while friction, wear, fatigue, excessive contact stress or dynamic instability invalidates the design. A response that is numerically precise but sensitive to unmeasured clearances should be given as a qualified estimate rather than a certified value.

## Test and reproducibility plan

**Investigation:** Fit exponential decay to successive displacement peaks and compare with a linear SDOF model. Record the drawing and initial settings before running the test. An appropriate student exercise can use slow, guarded motion, video tracking, or a separate numerical implementation; an energized high-speed experiment needs professional safety controls. Document reference length, sampling interval, calibration method and expected uncertainty. Compare at least three configurations, including a near-boundary case if it can be studied safely. Keep synthetic values separated from measured observations, and do not count the same input data as independent validation.

The report should contain a labeled schematic, equations, raw input table, one calculated output and its units, a sensitivity result and a discrepancy explanation. If an observed path differs from the model, consider perspective error, misidentified joints, slippage, structural flexibility, bearing clearance and unintended motion. Decide which extra measurement would distinguish the most plausible causes. A useful verification plan explains not only what evidence would support a model but what evidence would require it to be revised.

## Exercises and assessment

1. **Numerical variation:** Recalculate the worked example after changing one driving parameter by 15%. State the new answer, its units and the percentage change. Identify any hidden domain restriction, such as a minimum rod length or positive stiffness.
2. **Mechanism reasoning:** When does damping reduce oscillation amplitude without changing static stiffness? Contrast the original situation with a changed link, joint, contact condition or speed regime. Draw the new physical picture and explain which equation remains valid, requires modification or fails.
3. **Model critique:** Design an independent test for the proposed investigation, including measured variables, instrument calibration, repeatability, one confounding factor and a rejection criterion.

## Design review conclusion

**Viscous damping ratio** provides one part of a complete machine analysis. Deliver a brief calculation memo with an explicit operating range and at least one technical limitation. Evaluate the result against mechanism geometry and energy conservation, and list any unresolved requirements for guards, rated components, fatigue testing, maintenance or industrial standards before suggesting construction. A model is only one line of evidence; physical tests and responsible engineering judgment remain necessary.


---

# U07-L05 — Forced vibration and resonance

**Unit 7: Balancing, Vibrations and Dynamic Response · University-level learning draft · All examples synthetic**

## Engineering question and geometry

**Question:** How does a periodic force create a large response near a system mode?

**Scenario:** An electric motor generates a harmonic shaft force and the support has a nearby natural frequency. Begin by drawing the machine in one reference configuration, identifying the ground, the input actuator and the intended output variable. Treat the device as a rigid planar assembly only if its geometry and operating conditions justify that approximation. Mark fixed points, moving joints, relevant dimensions, motion signs and any physical stop or contact condition. A computer animation is useful for communicating the proposed motion, but it cannot demonstrate that the physical parts have sufficient clearance or that the arrangement is safe.

## Principle, constraints and derivation

**Governing relation:** `X=F0/sqrt((k−mω²)²+(cω)²)`.

The expression assumes a linear one-degree-of-freedom oscillator under steady harmonic forcing; startup transients and higher modes need extra modeling. An equivalent single-degree-of-freedom oscillator captures one dominant mode but not an entire flexible structure. Establish measured mass, restoring stiffness, damping mechanism and excitation spectrum. Convert between angular frequency and cycles per second before comparing machine rpm with mode frequencies. Unbalance excitation grows as speed squared, so high-speed validation is safety-critical even for a small eccentricity. Balancing vectors require both magnitude and angular phase. Isolation must be evaluated over the whole startup and run-down speed range because a soft mount may pass through a resonant region. Real foundations and bearings can couple horizontal, vertical and torsional modes.

Define each independent quantity and units before substitution. If a formula contains an angle derivative, convert degrees to radians and apply the chain rule to move from angle to time. For a constrained mechanism, first solve position closure and then differentiate to obtain velocity and acceleration. For a loaded mechanism, separate the purely kinematic result from required contact reactions and input torque. Identify when the formula assumes a fixed pivot, a constant input speed, a continuously engaged contact, or one assembly branch. A physically meaningful calculation states its domain, not just its output.

## Worked numerical case

**Illustrative inputs:** Harmonic force 50 N; m=20 kg, k=80 kN/m, c=400 N·s/m, ω=50 rad/s.

**Calculation — Forced vibration amplitude:** **0.00138675 m**. These values were chosen for teaching, not measured from machinery. Put each input and its unit on a separate line in a reproducible calculation sheet, then verify the arithmetic with an independent computation. The sign of a rotational quantity indicates orientation; it does not imply an error. When the output is a force, check the implied work and reaction path. When it is a geometric dimension, check the assembly envelope and the full intended motion cycle, not only the illustrated pose.

**Sanity test:** Vary one relevant parameter by 10% and classify the resulting trend as linear, inverse, quadratic or configuration-dependent. Consider a near-limit case and ask which assumption would fail first. The calculation cannot independently prove its own assumptions: a derived value must eventually be compared with a separate observation, compatible published reference or physically grounded second model.

## Engineering interpretation and counterexample

**Frequent mistake:** Assuming resonant amplitude is infinite in every real damped mechanism.

**Specific sensitivity investigation:** Move excitation frequency toward and then beyond natural frequency. Map the rise and eventual decline in the damped response magnitude. State what is held fixed, what changes and whether the output should be continuous. For closed-loop linkages, a second numerical solution may correspond to a different assembly branch; continuous angle tracking and a small closure residual are essential. For cams, belts, transmissions and vibration models, identify contact state, speed range and sources of energy dissipation. If a model produces exceptionally high speed or force near an ideal singularity, report the sensitivity and stop short of treating an unbounded prediction as achievable hardware performance.

A result matters when it can influence an engineering decision: mechanism selection, operating speed, joint configuration, allowable tolerance or actuator requirement. Always distinguish theoretical feasibility from reliability over many cycles. Geometry can be correct while friction, wear, fatigue, excessive contact stress or dynamic instability invalidates the design. A response that is numerically precise but sensitive to unmeasured clearances should be given as a qualified estimate rather than a certified value.

## Test and reproducibility plan

**Investigation:** Sweep safe excitation frequency and plot measured displacement amplitude. Record the drawing and initial settings before running the test. An appropriate student exercise can use slow, guarded motion, video tracking, or a separate numerical implementation; an energized high-speed experiment needs professional safety controls. Document reference length, sampling interval, calibration method and expected uncertainty. Compare at least three configurations, including a near-boundary case if it can be studied safely. Keep synthetic values separated from measured observations, and do not count the same input data as independent validation.

The report should contain a labeled schematic, equations, raw input table, one calculated output and its units, a sensitivity result and a discrepancy explanation. If an observed path differs from the model, consider perspective error, misidentified joints, slippage, structural flexibility, bearing clearance and unintended motion. Decide which extra measurement would distinguish the most plausible causes. A useful verification plan explains not only what evidence would support a model but what evidence would require it to be revised.

## Exercises and assessment

1. **Numerical variation:** Recalculate the worked example after changing one driving parameter by 15%. State the new answer, its units and the percentage change. Identify any hidden domain restriction, such as a minimum rod length or positive stiffness.
2. **Mechanism reasoning:** How does a periodic force create a large response near a system mode? Contrast the original situation with a changed link, joint, contact condition or speed regime. Draw the new physical picture and explain which equation remains valid, requires modification or fails.
3. **Model critique:** Design an independent test for the proposed investigation, including measured variables, instrument calibration, repeatability, one confounding factor and a rejection criterion.

## Design review conclusion

**Forced vibration and resonance** provides one part of a complete machine analysis. Deliver a brief calculation memo with an explicit operating range and at least one technical limitation. Evaluate the result against mechanism geometry and energy conservation, and list any unresolved requirements for guards, rated components, fatigue testing, maintenance or industrial standards before suggesting construction. A model is only one line of evidence; physical tests and responsible engineering judgment remain necessary.


---

