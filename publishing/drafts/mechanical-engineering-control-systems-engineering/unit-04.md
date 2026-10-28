# Unit 04: Frequency-Domain Analysis

**Course Code**: CSE 304 · **Level**: Advanced Undergraduate Engineering

## Unit Overview & Physical Foundations

This comprehensive university textbook unit covers the theoretical framework, physical modeling, mathematical governing equations, and engineering applications of **Frequency-Domain Analysis**.

# U04-L01 — Sinusoidal steady-state and frequency response

**Mechanical Engineering · Control Systems Engineering · Unit 4: Frequency-Domain Analysis.**  This is an unreviewed instructional chapter; none of its calculations alone justifies commissioning machinery.

## What you should be able to do

Explain **sinusoidal steady-state and frequency response** without confusing measured variables, hidden dynamics and desired behavior; write the main equation and derive its assumptions; reproduce the numerical illustration; diagnose at least two ways the model may mislead; and propose a practical, limited-risk verification experiment.

## Physical interpretation

For a stable LTI system driven by u=A cos(ωt), the long-time sinusoidal output has amplitude A|G(jω)| and phase shift arg G(jω). Magnitude and phase must be interpreted together. Transient terms can dominate before steady state settles.

**System context.** A motor experiences low-frequency load variations and high-frequency encoder noise; a single gain cannot suppress both freely. The objective in this lesson is not an abstract good-looking response: Use frequency response to expose bandwidth, disturbance rejection and stability margins across operating frequencies. Establish whether the lesson concerns the plant itself, the mathematical input/output map, an estimator, a controller, or a test method. Those roles cannot be interchanged. A controller parameter may improve the command-response plot and simultaneously create unacceptable actuator current, mechanical strain or sensor-noise transmission.

## Derivation and use

Compute G(jω) by replacing s with jω. The result depends on measured physical units; dB is 20 log10 of an amplitude ratio. Use 10 log10 only for power ratios.

**Dimensional and sign audit.** Before substituting values, define an input and output in physical units, choose a positive direction, identify zero or equilibrium conditions, and make sure both sides of any differential or algebraic equation have the same dimensions. For sinusoidal steady-state and frequency response, changing coordinates or the chosen sensor location can reverse the sign or modify the apparent dynamics. A formula for ideal negative feedback must not be used when actual wiring implements positive feedback. Explicitly distinguish a continuous-time differential equation from a discrete update at sample index k.

## Worked numerical illustration

For G=1/(1+0.5s) at ω=4 rad/s, magnitude=1/√5≈0.447 and phase=−arctan 2≈−63.4°.

**Reproduction protocol.** Write the givens and units in a table, compute any derived time scales or gains, substitute into the displayed model and calculate the result with more precision than required for the final reported value. Compare against a limiting case: zero disturbance, zero controller gain, vanishing sample time, or a stationary equilibrium as appropriate. If a calculation predicts infinite control force, negative dissipation, or motion through a hard stop, that is an indication to revisit assumptions, not a valid operating instruction.

## What the calculation does not establish

A sine sweep through a resonance can violate actuator travel or thermal limits; test amplitudes must be controlled.

This limitation matters particularly for **sinusoidal steady-state and frequency response**. The simplified example contains no manufacturing tolerances, no equipment-specific safety certification, and no direct evidence about the chosen hardware. Extra physics—sensor lag, actuator limits, cross-coupling, higher modes, friction, temperature drift or sampling delay—must be assessed according to the application. A model can be mathematically stable while the experiment violates the permitted range of current, speed, force or temperature.

## Practical reasoning and validation

1. **Define the measurement.** For this lesson, identify the smallest set of sensors that can distinguish the predicted mechanism from an alternative explanation. Record calibration, range, resolution, sampling rate and timestamps. Do not use commanded actuator signals as though they were measured actuator output.

2. **Plan excitation.** Choose a reversible stimulus small enough to respect the independent safety limits in the case: A motor experiences low-frequency load variations and high-frequency encoder noise; a single gain cannot suppress both freely. A step, ramp, chirp, frequency sweep or deliberate small load perturbation may be appropriate, but there is no universal safe test amplitude. Start with the smallest informative test.

3. **Predict first.** Use the selected model to forecast the direction, scale and timing of at least one observation. Include what would refute the prediction. Predictions recorded before an experiment reduce the temptation to tune the story after seeing the result.

4. **Collect independent evidence.** Compare the predicted and measured quantities at more than one operating condition, including a held-out condition not used to fit parameters. Report transients, steady behavior and the actuator command on separate channels. Record uncertainty and do not hide residual patterns by averaging them away.

5. **Revise and document.** If the data disagree, consider model order, omitted delay, calibration bias, nonlinearity or incorrect sign before raising controller gain. Save the model version, parameter ranges, test date, and outstanding safety questions.

## Guided problems

**Problem A — definitions.** Draw the complete signal path for a system that must demonstrate sinusoidal steady-state and frequency response. Mark the reference, measured output, actual output, process disturbance and actuator constraint. State which quantities can be directly measured and which must be estimated.

**Problem B — quantitative reproduction.** Rework the example in this lesson using SI units, then change one numerical input by 10%. Report the result and a dimensionless sensitivity ratio. Explain whether a first-order approximation is appropriate.

**Problem C — alternate assumption.** Repeat the reasoning after adding either finite sample time, sensor bias or actuator saturation. Identify precisely which mathematical step is no longer valid and whether the expected effect is on stability, steady-state error or transient response.

**Problem D — experiment design.** Write a one-page safe bench-test protocol covering instrument checks, recorded variables, stimulus limits, shutdown logic and criteria for rejecting a fitted model. You must distinguish acceptance of a numerical model from approval to operate equipment.

**Problem E — peer challenge.** Argue against a proposed design that optimizes only one metric (such as settling time). Name at least two competing metrics and explain why evidence from the running case might change the preferred design.

## Worked answer path (not a substitute for a full design)

For A, write a block diagram with sensor noise entering the measurement channel and the disturbance entering the correct physical location; this prevents confusion between feedback error and actual tracking error. For B, compute the baseline result, recompute at 1.10 times the chosen parameter, and use sensitivity approximately (Δoutput/output)/(Δparameter/parameter), describing sign and any nonlinear dependence. For C, identify the changed assumption first; do not silently reuse the nominal transfer function. For D, report a test trace and a safety boundary independently. For E, make the tradeoff explicit rather than calling the fastest response automatically best.

## Reflection and next step

Identify the cause of the response, not only the observed waveform. Identify a single observation that would make you question the conclusion about **sinusoidal steady-state and frequency response**. At the end of the lesson record one corrected assumption, one remaining unknown and one measurable next action. The next section extends this reasoning to another part of the control loop; keep the previous model as a baseline for comparison.


---

# U04-L02 — Bode plots, slopes and break frequencies

**Mechanical Engineering · Control Systems Engineering · Unit 4: Frequency-Domain Analysis.**  This is an unreviewed instructional chapter; none of its calculations alone justifies commissioning machinery.

## What you should be able to do

Explain **bode plots, slopes and break frequencies** without confusing measured variables, hidden dynamics and desired behavior; write the main equation and derive its assumptions; reproduce the numerical illustration; diagnose at least two ways the model may mislead; and propose a practical, limited-risk verification experiment.

## Physical interpretation

A first-order pole contributes approximately −20 dB per decade beyond its corner and approaches −90° phase lag. An integrator has a −20 dB/decade slope across the logarithmic frequency range and constant −90° phase.

**System context.** A motor experiences low-frequency load variations and high-frequency encoder noise; a single gain cannot suppress both freely. The objective in this lesson is not an abstract good-looking response: Use frequency response to expose bandwidth, disturbance rejection and stability margins across operating frequencies. Establish whether the lesson concerns the plant itself, the mathematical input/output map, an estimator, a controller, or a test method. Those roles cannot be interchanged. A controller parameter may improve the command-response plot and simultaneously create unacceptable actuator current, mechanical strain or sensor-noise transmission.

## Derivation and use

Sketch asymptotes only as a check. The exact magnitude near a break frequency differs by about 3.01 dB from the high/low asymptote for a single pole. Multiple nearby factors interact; summing their exact phase contributions is safer.

**Dimensional and sign audit.** Before substituting values, define an input and output in physical units, choose a positive direction, identify zero or equilibrium conditions, and make sure both sides of any differential or algebraic equation have the same dimensions. For bode plots, slopes and break frequencies, changing coordinates or the chosen sensor location can reverse the sign or modify the apparent dynamics. A formula for ideal negative feedback must not be used when actual wiring implements positive feedback. Explicitly distinguish a continuous-time differential equation from a discrete update at sample index k.

## Worked numerical illustration

For a pole at 10 rad/s, ω=10 rad/s gives amplitude 1/√2≈0.707 and phase −45° relative to low-frequency gain.

**Reproduction protocol.** Write the givens and units in a table, compute any derived time scales or gains, substitute into the displayed model and calculate the result with more precision than required for the final reported value. Compare against a limiting case: zero disturbance, zero controller gain, vanishing sample time, or a stationary equilibrium as appropriate. If a calculation predicts infinite control force, negative dissipation, or motion through a hard stop, that is an indication to revisit assumptions, not a valid operating instruction.

## What the calculation does not establish

Pure delay adds −ωL radians of phase without changing ideal magnitude, and can destroy stability margins invisibly on a magnitude-only plot.

This limitation matters particularly for **bode plots, slopes and break frequencies**. The simplified example contains no manufacturing tolerances, no equipment-specific safety certification, and no direct evidence about the chosen hardware. Extra physics—sensor lag, actuator limits, cross-coupling, higher modes, friction, temperature drift or sampling delay—must be assessed according to the application. A model can be mathematically stable while the experiment violates the permitted range of current, speed, force or temperature.

## Practical reasoning and validation

1. **Define the measurement.** For this lesson, identify the smallest set of sensors that can distinguish the predicted mechanism from an alternative explanation. Record calibration, range, resolution, sampling rate and timestamps. Do not use commanded actuator signals as though they were measured actuator output.

2. **Plan excitation.** Choose a reversible stimulus small enough to respect the independent safety limits in the case: A motor experiences low-frequency load variations and high-frequency encoder noise; a single gain cannot suppress both freely. A step, ramp, chirp, frequency sweep or deliberate small load perturbation may be appropriate, but there is no universal safe test amplitude. Start with the smallest informative test.

3. **Predict first.** Use the selected model to forecast the direction, scale and timing of at least one observation. Include what would refute the prediction. Predictions recorded before an experiment reduce the temptation to tune the story after seeing the result.

4. **Collect independent evidence.** Compare the predicted and measured quantities at more than one operating condition, including a held-out condition not used to fit parameters. Report transients, steady behavior and the actuator command on separate channels. Record uncertainty and do not hide residual patterns by averaging them away.

5. **Revise and document.** If the data disagree, consider model order, omitted delay, calibration bias, nonlinearity or incorrect sign before raising controller gain. Save the model version, parameter ranges, test date, and outstanding safety questions.

## Guided problems

**Problem A — definitions.** Draw the complete signal path for a system that must demonstrate bode plots, slopes and break frequencies. Mark the reference, measured output, actual output, process disturbance and actuator constraint. State which quantities can be directly measured and which must be estimated.

**Problem B — quantitative reproduction.** Rework the example in this lesson using SI units, then change one numerical input by 10%. Report the result and a dimensionless sensitivity ratio. Explain whether a first-order approximation is appropriate.

**Problem C — alternate assumption.** Repeat the reasoning after adding either finite sample time, sensor bias or actuator saturation. Identify precisely which mathematical step is no longer valid and whether the expected effect is on stability, steady-state error or transient response.

**Problem D — experiment design.** Write a one-page safe bench-test protocol covering instrument checks, recorded variables, stimulus limits, shutdown logic and criteria for rejecting a fitted model. You must distinguish acceptance of a numerical model from approval to operate equipment.

**Problem E — peer challenge.** Argue against a proposed design that optimizes only one metric (such as settling time). Name at least two competing metrics and explain why evidence from the running case might change the preferred design.

## Worked answer path (not a substitute for a full design)

For A, write a block diagram with sensor noise entering the measurement channel and the disturbance entering the correct physical location; this prevents confusion between feedback error and actual tracking error. For B, compute the baseline result, recompute at 1.10 times the chosen parameter, and use sensitivity approximately (Δoutput/output)/(Δparameter/parameter), describing sign and any nonlinear dependence. For C, identify the changed assumption first; do not silently reuse the nominal transfer function. For D, report a test trace and a safety boundary independently. For E, make the tradeoff explicit rather than calling the fastest response automatically best.

## Reflection and next step

Keep each parameter attached to its physical units and measured provenance. Identify a single observation that would make you question the conclusion about **bode plots, slopes and break frequencies**. At the end of the lesson record one corrected assumption, one remaining unknown and one measurable next action. The next section extends this reasoning to another part of the control loop; keep the previous model as a baseline for comparison.


---

# U04-L03 — Nyquist criterion and encirclements

**Mechanical Engineering · Control Systems Engineering · Unit 4: Frequency-Domain Analysis.**  This is an unreviewed instructional chapter; none of its calculations alone justifies commissioning machinery.

## What you should be able to do

Explain **nyquist criterion and encirclements** without confusing measured variables, hidden dynamics and desired behavior; write the main equation and derive its assumptions; reproduce the numerical illustration; diagnose at least two ways the model may mislead; and propose a practical, limited-risk verification experiment.

## Physical interpretation

Nyquist stability reasoning relates open-loop right-half-plane poles and the contour behavior of L(s) around −1+j0. Precise sign conventions are essential. The common short form assumes an open-loop-stable plant, for which avoiding destabilizing encirclements is the key concern.

**System context.** A motor experiences low-frequency load variations and high-frequency encoder noise; a single gain cannot suppress both freely. The objective in this lesson is not an abstract good-looking response: Use frequency response to expose bandwidth, disturbance rejection and stability margins across operating frequencies. Establish whether the lesson concerns the plant itself, the mathematical input/output map, an estimator, a controller, or a test method. Those roles cannot be interchanged. A controller parameter may improve the command-response plot and simultaneously create unacceptable actuator current, mechanical strain or sensor-noise transmission.

## Derivation and use

For difficult contours, identify right-half-plane open-loop poles, handle imaginary-axis poles with indentations, and verify numerical results with direct closed-loop roots. A hand-drawn Nyquist curve near −1 cannot resolve small margins.

**Dimensional and sign audit.** Before substituting values, define an input and output in physical units, choose a positive direction, identify zero or equilibrium conditions, and make sure both sides of any differential or algebraic equation have the same dimensions. For nyquist criterion and encirclements, changing coordinates or the chosen sensor location can reverse the sign or modify the apparent dynamics. A formula for ideal negative feedback must not be used when actual wiring implements positive feedback. Explicitly distinguish a continuous-time differential equation from a discrete update at sample index k.

## Worked numerical illustration

For L(jω)=K/(1+jωτ), positive K and τ produce phase between 0 and −90°, so the simple unity-feedback loop has no crossing of −180°.

**Reproduction protocol.** Write the givens and units in a table, compute any derived time scales or gains, substitute into the displayed model and calculate the result with more precision than required for the final reported value. Compare against a limiting case: zero disturbance, zero controller gain, vanishing sample time, or a stationary equilibrium as appropriate. If a calculation predicts infinite control force, negative dissipation, or motion through a hard stop, that is an indication to revisit assumptions, not a valid operating instruction.

## What the calculation does not establish

Delay and resonant plants can introduce extra winding even when a first-order sketch suggests ample margin.

This limitation matters particularly for **nyquist criterion and encirclements**. The simplified example contains no manufacturing tolerances, no equipment-specific safety certification, and no direct evidence about the chosen hardware. Extra physics—sensor lag, actuator limits, cross-coupling, higher modes, friction, temperature drift or sampling delay—must be assessed according to the application. A model can be mathematically stable while the experiment violates the permitted range of current, speed, force or temperature.

## Practical reasoning and validation

1. **Define the measurement.** For this lesson, identify the smallest set of sensors that can distinguish the predicted mechanism from an alternative explanation. Record calibration, range, resolution, sampling rate and timestamps. Do not use commanded actuator signals as though they were measured actuator output.

2. **Plan excitation.** Choose a reversible stimulus small enough to respect the independent safety limits in the case: A motor experiences low-frequency load variations and high-frequency encoder noise; a single gain cannot suppress both freely. A step, ramp, chirp, frequency sweep or deliberate small load perturbation may be appropriate, but there is no universal safe test amplitude. Start with the smallest informative test.

3. **Predict first.** Use the selected model to forecast the direction, scale and timing of at least one observation. Include what would refute the prediction. Predictions recorded before an experiment reduce the temptation to tune the story after seeing the result.

4. **Collect independent evidence.** Compare the predicted and measured quantities at more than one operating condition, including a held-out condition not used to fit parameters. Report transients, steady behavior and the actuator command on separate channels. Record uncertainty and do not hide residual patterns by averaging them away.

5. **Revise and document.** If the data disagree, consider model order, omitted delay, calibration bias, nonlinearity or incorrect sign before raising controller gain. Save the model version, parameter ranges, test date, and outstanding safety questions.

## Guided problems

**Problem A — definitions.** Draw the complete signal path for a system that must demonstrate nyquist criterion and encirclements. Mark the reference, measured output, actual output, process disturbance and actuator constraint. State which quantities can be directly measured and which must be estimated.

**Problem B — quantitative reproduction.** Rework the example in this lesson using SI units, then change one numerical input by 10%. Report the result and a dimensionless sensitivity ratio. Explain whether a first-order approximation is appropriate.

**Problem C — alternate assumption.** Repeat the reasoning after adding either finite sample time, sensor bias or actuator saturation. Identify precisely which mathematical step is no longer valid and whether the expected effect is on stability, steady-state error or transient response.

**Problem D — experiment design.** Write a one-page safe bench-test protocol covering instrument checks, recorded variables, stimulus limits, shutdown logic and criteria for rejecting a fitted model. You must distinguish acceptance of a numerical model from approval to operate equipment.

**Problem E — peer challenge.** Argue against a proposed design that optimizes only one metric (such as settling time). Name at least two competing metrics and explain why evidence from the running case might change the preferred design.

## Worked answer path (not a substitute for a full design)

For A, write a block diagram with sensor noise entering the measurement channel and the disturbance entering the correct physical location; this prevents confusion between feedback error and actual tracking error. For B, compute the baseline result, recompute at 1.10 times the chosen parameter, and use sensitivity approximately (Δoutput/output)/(Δparameter/parameter), describing sign and any nonlinear dependence. For C, identify the changed assumption first; do not silently reuse the nominal transfer function. For D, report a test trace and a safety boundary independently. For E, make the tradeoff explicit rather than calling the fastest response automatically best.

## Reflection and next step

Separate the equation derived under assumptions from the test that could challenge it. Identify a single observation that would make you question the conclusion about **nyquist criterion and encirclements**. At the end of the lesson record one corrected assumption, one remaining unknown and one measurable next action. The next section extends this reasoning to another part of the control loop; keep the previous model as a baseline for comparison.


---

# U04-L04 — Gain margin, phase margin and bandwidth

**Mechanical Engineering · Control Systems Engineering · Unit 4: Frequency-Domain Analysis.**  This is an unreviewed instructional chapter; none of its calculations alone justifies commissioning machinery.

## What you should be able to do

Explain **gain margin, phase margin and bandwidth** without confusing measured variables, hidden dynamics and desired behavior; write the main equation and derive its assumptions; reproduce the numerical illustration; diagnose at least two ways the model may mislead; and propose a practical, limited-risk verification experiment.

## Physical interpretation

Phase margin is 180°+arg L(jω_gc) at a gain crossover |L|=1. Gain margin is the reciprocal of |L| where the phase reaches −180°, under standard definitions. Bandwidth is a closed-loop property and depends on the criterion used.

**System context.** A motor experiences low-frequency load variations and high-frequency encoder noise; a single gain cannot suppress both freely. The objective in this lesson is not an abstract good-looking response: Use frequency response to expose bandwidth, disturbance rejection and stability margins across operating frequencies. Establish whether the lesson concerns the plant itself, the mathematical input/output map, an estimator, a controller, or a test method. Those roles cannot be interchanged. A controller parameter may improve the command-response plot and simultaneously create unacceptable actuator current, mechanical strain or sensor-noise transmission.

## Derivation and use

Do not report an “infinite” margin without specifying the considered frequency interval and model class. More bandwidth improves response to reference changes and low-frequency disturbances but tends to transmit more high-frequency noise and uncover delay.

**Dimensional and sign audit.** Before substituting values, define an input and output in physical units, choose a positive direction, identify zero or equilibrium conditions, and make sure both sides of any differential or algebraic equation have the same dimensions. For gain margin, phase margin and bandwidth, changing coordinates or the chosen sensor location can reverse the sign or modify the apparent dynamics. A formula for ideal negative feedback must not be used when actual wiring implements positive feedback. Explicitly distinguish a continuous-time differential equation from a discrete update at sample index k.

## Worked numerical illustration

At crossover, a measured open-loop phase of −135° implies about 45° phase margin. If extra delay adds 0.15 rad at crossover, the margin drops by ≈8.6°.

**Reproduction protocol.** Write the givens and units in a table, compute any derived time scales or gains, substitute into the displayed model and calculate the result with more precision than required for the final reported value. Compare against a limiting case: zero disturbance, zero controller gain, vanishing sample time, or a stationary equilibrium as appropriate. If a calculation predicts infinite control force, negative dissipation, or motion through a hard stop, that is an indication to revisit assumptions, not a valid operating instruction.

## What the calculation does not establish

Margins based on one input/output loop do not fully cover multivariable interactions, saturation, structural uncertainty or hidden unstable modes.

This limitation matters particularly for **gain margin, phase margin and bandwidth**. The simplified example contains no manufacturing tolerances, no equipment-specific safety certification, and no direct evidence about the chosen hardware. Extra physics—sensor lag, actuator limits, cross-coupling, higher modes, friction, temperature drift or sampling delay—must be assessed according to the application. A model can be mathematically stable while the experiment violates the permitted range of current, speed, force or temperature.

## Practical reasoning and validation

1. **Define the measurement.** For this lesson, identify the smallest set of sensors that can distinguish the predicted mechanism from an alternative explanation. Record calibration, range, resolution, sampling rate and timestamps. Do not use commanded actuator signals as though they were measured actuator output.

2. **Plan excitation.** Choose a reversible stimulus small enough to respect the independent safety limits in the case: A motor experiences low-frequency load variations and high-frequency encoder noise; a single gain cannot suppress both freely. A step, ramp, chirp, frequency sweep or deliberate small load perturbation may be appropriate, but there is no universal safe test amplitude. Start with the smallest informative test.

3. **Predict first.** Use the selected model to forecast the direction, scale and timing of at least one observation. Include what would refute the prediction. Predictions recorded before an experiment reduce the temptation to tune the story after seeing the result.

4. **Collect independent evidence.** Compare the predicted and measured quantities at more than one operating condition, including a held-out condition not used to fit parameters. Report transients, steady behavior and the actuator command on separate channels. Record uncertainty and do not hide residual patterns by averaging them away.

5. **Revise and document.** If the data disagree, consider model order, omitted delay, calibration bias, nonlinearity or incorrect sign before raising controller gain. Save the model version, parameter ranges, test date, and outstanding safety questions.

## Guided problems

**Problem A — definitions.** Draw the complete signal path for a system that must demonstrate gain margin, phase margin and bandwidth. Mark the reference, measured output, actual output, process disturbance and actuator constraint. State which quantities can be directly measured and which must be estimated.

**Problem B — quantitative reproduction.** Rework the example in this lesson using SI units, then change one numerical input by 10%. Report the result and a dimensionless sensitivity ratio. Explain whether a first-order approximation is appropriate.

**Problem C — alternate assumption.** Repeat the reasoning after adding either finite sample time, sensor bias or actuator saturation. Identify precisely which mathematical step is no longer valid and whether the expected effect is on stability, steady-state error or transient response.

**Problem D — experiment design.** Write a one-page safe bench-test protocol covering instrument checks, recorded variables, stimulus limits, shutdown logic and criteria for rejecting a fitted model. You must distinguish acceptance of a numerical model from approval to operate equipment.

**Problem E — peer challenge.** Argue against a proposed design that optimizes only one metric (such as settling time). Name at least two competing metrics and explain why evidence from the running case might change the preferred design.

## Worked answer path (not a substitute for a full design)

For A, write a block diagram with sensor noise entering the measurement channel and the disturbance entering the correct physical location; this prevents confusion between feedback error and actual tracking error. For B, compute the baseline result, recompute at 1.10 times the chosen parameter, and use sensitivity approximately (Δoutput/output)/(Δparameter/parameter), describing sign and any nonlinear dependence. For C, identify the changed assumption first; do not silently reuse the nominal transfer function. For D, report a test trace and a safety boundary independently. For E, make the tradeoff explicit rather than calling the fastest response automatically best.

## Reflection and next step

Check the controller command and all constrained internal states, not merely the output. Identify a single observation that would make you question the conclusion about **gain margin, phase margin and bandwidth**. At the end of the lesson record one corrected assumption, one remaining unknown and one measurable next action. The next section extends this reasoning to another part of the control loop; keep the previous model as a baseline for comparison.


---

# U04-L05 — Sensitivity, disturbances and sensor noise

**Mechanical Engineering · Control Systems Engineering · Unit 4: Frequency-Domain Analysis.**  This is an unreviewed instructional chapter; none of its calculations alone justifies commissioning machinery.

## What you should be able to do

Explain **sensitivity, disturbances and sensor noise** without confusing measured variables, hidden dynamics and desired behavior; write the main equation and derive its assumptions; reproduce the numerical illustration; diagnose at least two ways the model may mislead; and propose a practical, limited-risk verification experiment.

## Physical interpretation

For loop L=CG, sensitivity S=1/(1+L) and complementary sensitivity T=L/(1+L), hence S+T=1. Their frequency behavior creates a fundamental tradeoff: low-frequency rejection of output disturbances favors small |S|, while high-frequency sensor-noise rejection favors small |T|.

**System context.** A motor experiences low-frequency load variations and high-frequency encoder noise; a single gain cannot suppress both freely. The objective in this lesson is not an abstract good-looking response: Use frequency response to expose bandwidth, disturbance rejection and stability margins across operating frequencies. Establish whether the lesson concerns the plant itself, the mathematical input/output map, an estimator, a controller, or a test method. Those roles cannot be interchanged. A controller parameter may improve the command-response plot and simultaneously create unacceptable actuator current, mechanical strain or sensor-noise transmission.

## Derivation and use

Plot both curves, not just plant output. Distinguish disturbances injected at plant input, plant output and sensor measurement. Avoid tuning a controller solely for the reference step; controlled-variable variance under real disturbances may be the dominant performance criterion.

**Dimensional and sign audit.** Before substituting values, define an input and output in physical units, choose a positive direction, identify zero or equilibrium conditions, and make sure both sides of any differential or algebraic equation have the same dimensions. For sensitivity, disturbances and sensor noise, changing coordinates or the chosen sensor location can reverse the sign or modify the apparent dynamics. A formula for ideal negative feedback must not be used when actual wiring implements positive feedback. Explicitly distinguish a continuous-time differential equation from a discrete update at sample index k.

## Worked numerical illustration

With L(jω)=9 at a very low frequency, S≈0.1 and T≈0.9 for this real loop value. Large high-frequency loop gain instead passes measurement noise into the output.

**Reproduction protocol.** Write the givens and units in a table, compute any derived time scales or gains, substitute into the displayed model and calculate the result with more precision than required for the final reported value. Compare against a limiting case: zero disturbance, zero controller gain, vanishing sample time, or a stationary equilibrium as appropriate. If a calculation predicts infinite control force, negative dissipation, or motion through a hard stop, that is an indication to revisit assumptions, not a valid operating instruction.

## What the calculation does not establish

Waterbed-like sensitivity tradeoffs prevent arbitrarily low sensitivity across all frequencies in realistic constrained systems.

This limitation matters particularly for **sensitivity, disturbances and sensor noise**. The simplified example contains no manufacturing tolerances, no equipment-specific safety certification, and no direct evidence about the chosen hardware. Extra physics—sensor lag, actuator limits, cross-coupling, higher modes, friction, temperature drift or sampling delay—must be assessed according to the application. A model can be mathematically stable while the experiment violates the permitted range of current, speed, force or temperature.

## Practical reasoning and validation

1. **Define the measurement.** For this lesson, identify the smallest set of sensors that can distinguish the predicted mechanism from an alternative explanation. Record calibration, range, resolution, sampling rate and timestamps. Do not use commanded actuator signals as though they were measured actuator output.

2. **Plan excitation.** Choose a reversible stimulus small enough to respect the independent safety limits in the case: A motor experiences low-frequency load variations and high-frequency encoder noise; a single gain cannot suppress both freely. A step, ramp, chirp, frequency sweep or deliberate small load perturbation may be appropriate, but there is no universal safe test amplitude. Start with the smallest informative test.

3. **Predict first.** Use the selected model to forecast the direction, scale and timing of at least one observation. Include what would refute the prediction. Predictions recorded before an experiment reduce the temptation to tune the story after seeing the result.

4. **Collect independent evidence.** Compare the predicted and measured quantities at more than one operating condition, including a held-out condition not used to fit parameters. Report transients, steady behavior and the actuator command on separate channels. Record uncertainty and do not hide residual patterns by averaging them away.

5. **Revise and document.** If the data disagree, consider model order, omitted delay, calibration bias, nonlinearity or incorrect sign before raising controller gain. Save the model version, parameter ranges, test date, and outstanding safety questions.

## Guided problems

**Problem A — definitions.** Draw the complete signal path for a system that must demonstrate sensitivity, disturbances and sensor noise. Mark the reference, measured output, actual output, process disturbance and actuator constraint. State which quantities can be directly measured and which must be estimated.

**Problem B — quantitative reproduction.** Rework the example in this lesson using SI units, then change one numerical input by 10%. Report the result and a dimensionless sensitivity ratio. Explain whether a first-order approximation is appropriate.

**Problem C — alternate assumption.** Repeat the reasoning after adding either finite sample time, sensor bias or actuator saturation. Identify precisely which mathematical step is no longer valid and whether the expected effect is on stability, steady-state error or transient response.

**Problem D — experiment design.** Write a one-page safe bench-test protocol covering instrument checks, recorded variables, stimulus limits, shutdown logic and criteria for rejecting a fitted model. You must distinguish acceptance of a numerical model from approval to operate equipment.

**Problem E — peer challenge.** Argue against a proposed design that optimizes only one metric (such as settling time). Name at least two competing metrics and explain why evidence from the running case might change the preferred design.

## Worked answer path (not a substitute for a full design)

For A, write a block diagram with sensor noise entering the measurement channel and the disturbance entering the correct physical location; this prevents confusion between feedback error and actual tracking error. For B, compute the baseline result, recompute at 1.10 times the chosen parameter, and use sensitivity approximately (Δoutput/output)/(Δparameter/parameter), describing sign and any nonlinear dependence. For C, identify the changed assumption first; do not silently reuse the nominal transfer function. For D, report a test trace and a safety boundary independently. For E, make the tradeoff explicit rather than calling the fastest response automatically best.

## Reflection and next step

Use the result as a foundation for a decision with a stated uncertainty interval. Identify a single observation that would make you question the conclusion about **sensitivity, disturbances and sensor noise**. At the end of the lesson record one corrected assumption, one remaining unknown and one measurable next action. The next section extends this reasoning to another part of the control loop; keep the previous model as a baseline for comparison.


---

