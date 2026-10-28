# Unit 02: Time Response and Performance Specifications

**Course Code**: CSE 302 · **Level**: Advanced Undergraduate Engineering

## Unit Overview & Physical Foundations

This comprehensive university textbook unit covers the theoretical framework, physical modeling, mathematical governing equations, and engineering applications of **Time Response and Performance Specifications**.

# U02-L01 — First-order steps and time constants

**Mechanical Engineering · Control Systems Engineering · Unit 2: Time Response and Performance Specifications.**  This is an unreviewed instructional chapter; none of its calculations alone justifies commissioning machinery.

## What you should be able to do

Explain **first-order steps and time constants** without confusing measured variables, hidden dynamics and desired behavior; write the main equation and derive its assumptions; reproduce the numerical illustration; diagnose at least two ways the model may mislead; and propose a practical, limited-risk verification experiment.

## Physical interpretation

For G(s)=K/(τs+1), a unit step beginning from equilibrium produces y(t)=K(1−exp(−t/τ)); after one τ the response has reached 63.2% of the final change. The response is monotone only in the ideal positive-gain single-pole model.

**System context.** A laboratory servo must reach a commanded angle quickly without overshooting a mechanical end stop. The objective in this lesson is not an abstract good-looking response: Translate performance requirements into characteristic times and transient response, not just a visually attractive plot. Establish whether the lesson concerns the plant itself, the mathematical input/output map, an estimator, a controller, or a test method. Those roles cannot be interchanged. A controller parameter may improve the command-response plot and simultaneously create unacceptable actuator current, mechanical strain or sensor-noise transmission.

## Derivation and use

Derive the response from τ ẏ+y=Ku0 by multiplying by an integrating factor. At t=3τ the residual deviation is e⁻³≈5%, and at t≈4τ it is ≈1.8%. Measurements at one time should not be confused with an identified τ.

**Dimensional and sign audit.** Before substituting values, define an input and output in physical units, choose a positive direction, identify zero or equilibrium conditions, and make sure both sides of any differential or algebraic equation have the same dimensions. For first-order steps and time constants, changing coordinates or the chosen sensor location can reverse the sign or modify the apparent dynamics. A formula for ideal negative feedback must not be used when actual wiring implements positive feedback. Explicitly distinguish a continuous-time differential equation from a discrete update at sample index k.

## Worked numerical illustration

A valve opens and flow increases from 0 to 80 L/min with τ=6 s. At t=12 s, y≈80(1−e⁻²)=69.17 L/min.

**Reproduction protocol.** Write the givens and units in a table, compute any derived time scales or gains, substitute into the displayed model and calculate the result with more precision than required for the final reported value. Compare against a limiting case: zero disturbance, zero controller gain, vanishing sample time, or a stationary equilibrium as appropriate. If a calculation predicts infinite control force, negative dissipation, or motion through a hard stop, that is an indication to revisit assumptions, not a valid operating instruction.

## What the calculation does not establish

Transport delay must be added separately; treating delay as an increased time constant can mislead controller tuning.

This limitation matters particularly for **first-order steps and time constants**. The simplified example contains no manufacturing tolerances, no equipment-specific safety certification, and no direct evidence about the chosen hardware. Extra physics—sensor lag, actuator limits, cross-coupling, higher modes, friction, temperature drift or sampling delay—must be assessed according to the application. A model can be mathematically stable while the experiment violates the permitted range of current, speed, force or temperature.

## Practical reasoning and validation

1. **Define the measurement.** For this lesson, identify the smallest set of sensors that can distinguish the predicted mechanism from an alternative explanation. Record calibration, range, resolution, sampling rate and timestamps. Do not use commanded actuator signals as though they were measured actuator output.

2. **Plan excitation.** Choose a reversible stimulus small enough to respect the independent safety limits in the case: A laboratory servo must reach a commanded angle quickly without overshooting a mechanical end stop. A step, ramp, chirp, frequency sweep or deliberate small load perturbation may be appropriate, but there is no universal safe test amplitude. Start with the smallest informative test.

3. **Predict first.** Use the selected model to forecast the direction, scale and timing of at least one observation. Include what would refute the prediction. Predictions recorded before an experiment reduce the temptation to tune the story after seeing the result.

4. **Collect independent evidence.** Compare the predicted and measured quantities at more than one operating condition, including a held-out condition not used to fit parameters. Report transients, steady behavior and the actuator command on separate channels. Record uncertainty and do not hide residual patterns by averaging them away.

5. **Revise and document.** If the data disagree, consider model order, omitted delay, calibration bias, nonlinearity or incorrect sign before raising controller gain. Save the model version, parameter ranges, test date, and outstanding safety questions.

## Guided problems

**Problem A — definitions.** Draw the complete signal path for a system that must demonstrate first-order steps and time constants. Mark the reference, measured output, actual output, process disturbance and actuator constraint. State which quantities can be directly measured and which must be estimated.

**Problem B — quantitative reproduction.** Rework the example in this lesson using SI units, then change one numerical input by 10%. Report the result and a dimensionless sensitivity ratio. Explain whether a first-order approximation is appropriate.

**Problem C — alternate assumption.** Repeat the reasoning after adding either finite sample time, sensor bias or actuator saturation. Identify precisely which mathematical step is no longer valid and whether the expected effect is on stability, steady-state error or transient response.

**Problem D — experiment design.** Write a one-page safe bench-test protocol covering instrument checks, recorded variables, stimulus limits, shutdown logic and criteria for rejecting a fitted model. You must distinguish acceptance of a numerical model from approval to operate equipment.

**Problem E — peer challenge.** Argue against a proposed design that optimizes only one metric (such as settling time). Name at least two competing metrics and explain why evidence from the running case might change the preferred design.

## Worked answer path (not a substitute for a full design)

For A, write a block diagram with sensor noise entering the measurement channel and the disturbance entering the correct physical location; this prevents confusion between feedback error and actual tracking error. For B, compute the baseline result, recompute at 1.10 times the chosen parameter, and use sensitivity approximately (Δoutput/output)/(Δparameter/parameter), describing sign and any nonlinear dependence. For C, identify the changed assumption first; do not silently reuse the nominal transfer function. For D, report a test trace and a safety boundary independently. For E, make the tradeoff explicit rather than calling the fastest response automatically best.

## Reflection and next step

Check the controller command and all constrained internal states, not merely the output. Identify a single observation that would make you question the conclusion about **first-order steps and time constants**. At the end of the lesson record one corrected assumption, one remaining unknown and one measurable next action. The next section extends this reasoning to another part of the control loop; keep the previous model as a baseline for comparison.


---

# U02-L02 — Second-order modes, damping and overshoot

**Mechanical Engineering · Control Systems Engineering · Unit 2: Time Response and Performance Specifications.**  This is an unreviewed instructional chapter; none of its calculations alone justifies commissioning machinery.

## What you should be able to do

Explain **second-order modes, damping and overshoot** without confusing measured variables, hidden dynamics and desired behavior; write the main equation and derive its assumptions; reproduce the numerical illustration; diagnose at least two ways the model may mislead; and propose a practical, limited-risk verification experiment.

## Physical interpretation

The standard second-order denominator s²+2ζω_n s+ω_n² introduces natural frequency ω_n and damping ratio ζ. For 0<ζ<1, a step can overshoot; ζ near zero produces oscillatory behavior, while ζ≥1 eliminates oscillatory poles.

**System context.** A laboratory servo must reach a commanded angle quickly without overshooting a mechanical end stop. The objective in this lesson is not an abstract good-looking response: Translate performance requirements into characteristic times and transient response, not just a visually attractive plot. Establish whether the lesson concerns the plant itself, the mathematical input/output map, an estimator, a controller, or a test method. Those roles cannot be interchanged. A controller parameter may improve the command-response plot and simultaneously create unacceptable actuator current, mechanical strain or sensor-noise transmission.

## Derivation and use

The ideal percentage overshoot is 100 exp(−πζ/√(1−ζ²)). Peak time is π/(ω_n√(1−ζ²)). Near critically damped conditions the approximation for 2% settling time 4/(ζω_n) becomes less accurate.

**Dimensional and sign audit.** Before substituting values, define an input and output in physical units, choose a positive direction, identify zero or equilibrium conditions, and make sure both sides of any differential or algebraic equation have the same dimensions. For second-order modes, damping and overshoot, changing coordinates or the chosen sensor location can reverse the sign or modify the apparent dynamics. A formula for ideal negative feedback must not be used when actual wiring implements positive feedback. Explicitly distinguish a continuous-time differential equation from a discrete update at sample index k.

## Worked numerical illustration

With ζ=0.5 and ω_n=8 rad/s, ideal overshoot is ≈16.3%, peak time ≈0.453 s and approximate 2% settling time 1 s.

**Reproduction protocol.** Write the givens and units in a table, compute any derived time scales or gains, substitute into the displayed model and calculate the result with more precision than required for the final reported value. Compare against a limiting case: zero disturbance, zero controller gain, vanishing sample time, or a stationary equilibrium as appropriate. If a calculation predicts infinite control force, negative dissipation, or motion through a hard stop, that is an indication to revisit assumptions, not a valid operating instruction.

## What the calculation does not establish

Real plants with zeros, delay, saturations or higher modes do not necessarily obey this formula.

This limitation matters particularly for **second-order modes, damping and overshoot**. The simplified example contains no manufacturing tolerances, no equipment-specific safety certification, and no direct evidence about the chosen hardware. Extra physics—sensor lag, actuator limits, cross-coupling, higher modes, friction, temperature drift or sampling delay—must be assessed according to the application. A model can be mathematically stable while the experiment violates the permitted range of current, speed, force or temperature.

## Practical reasoning and validation

1. **Define the measurement.** For this lesson, identify the smallest set of sensors that can distinguish the predicted mechanism from an alternative explanation. Record calibration, range, resolution, sampling rate and timestamps. Do not use commanded actuator signals as though they were measured actuator output.

2. **Plan excitation.** Choose a reversible stimulus small enough to respect the independent safety limits in the case: A laboratory servo must reach a commanded angle quickly without overshooting a mechanical end stop. A step, ramp, chirp, frequency sweep or deliberate small load perturbation may be appropriate, but there is no universal safe test amplitude. Start with the smallest informative test.

3. **Predict first.** Use the selected model to forecast the direction, scale and timing of at least one observation. Include what would refute the prediction. Predictions recorded before an experiment reduce the temptation to tune the story after seeing the result.

4. **Collect independent evidence.** Compare the predicted and measured quantities at more than one operating condition, including a held-out condition not used to fit parameters. Report transients, steady behavior and the actuator command on separate channels. Record uncertainty and do not hide residual patterns by averaging them away.

5. **Revise and document.** If the data disagree, consider model order, omitted delay, calibration bias, nonlinearity or incorrect sign before raising controller gain. Save the model version, parameter ranges, test date, and outstanding safety questions.

## Guided problems

**Problem A — definitions.** Draw the complete signal path for a system that must demonstrate second-order modes, damping and overshoot. Mark the reference, measured output, actual output, process disturbance and actuator constraint. State which quantities can be directly measured and which must be estimated.

**Problem B — quantitative reproduction.** Rework the example in this lesson using SI units, then change one numerical input by 10%. Report the result and a dimensionless sensitivity ratio. Explain whether a first-order approximation is appropriate.

**Problem C — alternate assumption.** Repeat the reasoning after adding either finite sample time, sensor bias or actuator saturation. Identify precisely which mathematical step is no longer valid and whether the expected effect is on stability, steady-state error or transient response.

**Problem D — experiment design.** Write a one-page safe bench-test protocol covering instrument checks, recorded variables, stimulus limits, shutdown logic and criteria for rejecting a fitted model. You must distinguish acceptance of a numerical model from approval to operate equipment.

**Problem E — peer challenge.** Argue against a proposed design that optimizes only one metric (such as settling time). Name at least two competing metrics and explain why evidence from the running case might change the preferred design.

## Worked answer path (not a substitute for a full design)

For A, write a block diagram with sensor noise entering the measurement channel and the disturbance entering the correct physical location; this prevents confusion between feedback error and actual tracking error. For B, compute the baseline result, recompute at 1.10 times the chosen parameter, and use sensitivity approximately (Δoutput/output)/(Δparameter/parameter), describing sign and any nonlinear dependence. For C, identify the changed assumption first; do not silently reuse the nominal transfer function. For D, report a test trace and a safety boundary independently. For E, make the tradeoff explicit rather than calling the fastest response automatically best.

## Reflection and next step

Use the result as a foundation for a decision with a stated uncertainty interval. Identify a single observation that would make you question the conclusion about **second-order modes, damping and overshoot**. At the end of the lesson record one corrected assumption, one remaining unknown and one measurable next action. The next section extends this reasoning to another part of the control loop; keep the previous model as a baseline for comparison.


---

# U02-L03 — Rise time, settling time and specification tradeoffs

**Mechanical Engineering · Control Systems Engineering · Unit 2: Time Response and Performance Specifications.**  This is an unreviewed instructional chapter; none of its calculations alone justifies commissioning machinery.

## What you should be able to do

Explain **rise time, settling time and specification tradeoffs** without confusing measured variables, hidden dynamics and desired behavior; write the main equation and derive its assumptions; reproduce the numerical illustration; diagnose at least two ways the model may mislead; and propose a practical, limited-risk verification experiment.

## Physical interpretation

Rise time, peak time, percentage overshoot, steady-state error and settling time are different descriptors. Rise time depends on the chosen 10–90% or 0–100% convention; report the convention and the stimulus amplitude.

**System context.** A laboratory servo must reach a commanded angle quickly without overshooting a mechanical end stop. The objective in this lesson is not an abstract good-looking response: Translate performance requirements into characteristic times and transient response, not just a visually attractive plot. Establish whether the lesson concerns the plant itself, the mathematical input/output map, an estimator, a controller, or a test method. Those roles cannot be interchanged. A controller parameter may improve the command-response plot and simultaneously create unacceptable actuator current, mechanical strain or sensor-noise transmission.

## Derivation and use

A response can have a fast rise but a long settling tail if lightly damped. Increased loop gain may speed an initial response while creating overshoot and noise amplification. A specification without disturbance and input amplitudes is incomplete.

**Dimensional and sign audit.** Before substituting values, define an input and output in physical units, choose a positive direction, identify zero or equilibrium conditions, and make sure both sides of any differential or algebraic equation have the same dimensions. For rise time, settling time and specification tradeoffs, changing coordinates or the chosen sensor location can reverse the sign or modify the apparent dynamics. A formula for ideal negative feedback must not be used when actual wiring implements positive feedback. Explicitly distinguish a continuous-time differential equation from a discrete update at sample index k.

## Worked numerical illustration

A servo required to settle within ±1° after a 20° step needs a 5% band relative to the step. It is not the same test as a ±2% criterion.

**Reproduction protocol.** Write the givens and units in a table, compute any derived time scales or gains, substitute into the displayed model and calculate the result with more precision than required for the final reported value. Compare against a limiting case: zero disturbance, zero controller gain, vanishing sample time, or a stationary equilibrium as appropriate. If a calculation predicts infinite control force, negative dissipation, or motion through a hard stop, that is an indication to revisit assumptions, not a valid operating instruction.

## What the calculation does not establish

When the output sticks due to friction, a textbook settling band based on linear modes may hide an unacceptably large dead zone.

This limitation matters particularly for **rise time, settling time and specification tradeoffs**. The simplified example contains no manufacturing tolerances, no equipment-specific safety certification, and no direct evidence about the chosen hardware. Extra physics—sensor lag, actuator limits, cross-coupling, higher modes, friction, temperature drift or sampling delay—must be assessed according to the application. A model can be mathematically stable while the experiment violates the permitted range of current, speed, force or temperature.

## Practical reasoning and validation

1. **Define the measurement.** For this lesson, identify the smallest set of sensors that can distinguish the predicted mechanism from an alternative explanation. Record calibration, range, resolution, sampling rate and timestamps. Do not use commanded actuator signals as though they were measured actuator output.

2. **Plan excitation.** Choose a reversible stimulus small enough to respect the independent safety limits in the case: A laboratory servo must reach a commanded angle quickly without overshooting a mechanical end stop. A step, ramp, chirp, frequency sweep or deliberate small load perturbation may be appropriate, but there is no universal safe test amplitude. Start with the smallest informative test.

3. **Predict first.** Use the selected model to forecast the direction, scale and timing of at least one observation. Include what would refute the prediction. Predictions recorded before an experiment reduce the temptation to tune the story after seeing the result.

4. **Collect independent evidence.** Compare the predicted and measured quantities at more than one operating condition, including a held-out condition not used to fit parameters. Report transients, steady behavior and the actuator command on separate channels. Record uncertainty and do not hide residual patterns by averaging them away.

5. **Revise and document.** If the data disagree, consider model order, omitted delay, calibration bias, nonlinearity or incorrect sign before raising controller gain. Save the model version, parameter ranges, test date, and outstanding safety questions.

## Guided problems

**Problem A — definitions.** Draw the complete signal path for a system that must demonstrate rise time, settling time and specification tradeoffs. Mark the reference, measured output, actual output, process disturbance and actuator constraint. State which quantities can be directly measured and which must be estimated.

**Problem B — quantitative reproduction.** Rework the example in this lesson using SI units, then change one numerical input by 10%. Report the result and a dimensionless sensitivity ratio. Explain whether a first-order approximation is appropriate.

**Problem C — alternate assumption.** Repeat the reasoning after adding either finite sample time, sensor bias or actuator saturation. Identify precisely which mathematical step is no longer valid and whether the expected effect is on stability, steady-state error or transient response.

**Problem D — experiment design.** Write a one-page safe bench-test protocol covering instrument checks, recorded variables, stimulus limits, shutdown logic and criteria for rejecting a fitted model. You must distinguish acceptance of a numerical model from approval to operate equipment.

**Problem E — peer challenge.** Argue against a proposed design that optimizes only one metric (such as settling time). Name at least two competing metrics and explain why evidence from the running case might change the preferred design.

## Worked answer path (not a substitute for a full design)

For A, write a block diagram with sensor noise entering the measurement channel and the disturbance entering the correct physical location; this prevents confusion between feedback error and actual tracking error. For B, compute the baseline result, recompute at 1.10 times the chosen parameter, and use sensitivity approximately (Δoutput/output)/(Δparameter/parameter), describing sign and any nonlinear dependence. For C, identify the changed assumption first; do not silently reuse the nominal transfer function. For D, report a test trace and a safety boundary independently. For E, make the tradeoff explicit rather than calling the fastest response automatically best.

## Reflection and next step

Identify the cause of the response, not only the observed waveform. Identify a single observation that would make you question the conclusion about **rise time, settling time and specification tradeoffs**. At the end of the lesson record one corrected assumption, one remaining unknown and one measurable next action. The next section extends this reasoning to another part of the control loop; keep the previous model as a baseline for comparison.


---

# U02-L04 — Pole locations, zeros and transient shape

**Mechanical Engineering · Control Systems Engineering · Unit 2: Time Response and Performance Specifications.**  This is an unreviewed instructional chapter; none of its calculations alone justifies commissioning machinery.

## What you should be able to do

Explain **pole locations, zeros and transient shape** without confusing measured variables, hidden dynamics and desired behavior; write the main equation and derive its assumptions; reproduce the numerical illustration; diagnose at least two ways the model may mislead; and propose a practical, limited-risk verification experiment.

## Physical interpretation

Stable continuous-time real poles lie in the left half-plane. Complex poles −σ±jω_d produce exponentially decaying oscillations; right-half-plane poles produce growth. Zeros shape the response and may produce undershoot or initial peaking.

**System context.** A laboratory servo must reach a commanded angle quickly without overshooting a mechanical end stop. The objective in this lesson is not an abstract good-looking response: Translate performance requirements into characteristic times and transient response, not just a visually attractive plot. Establish whether the lesson concerns the plant itself, the mathematical input/output map, an estimator, a controller, or a test method. Those roles cannot be interchanged. A controller parameter may improve the command-response plot and simultaneously create unacceptable actuator current, mechanical strain or sensor-noise transmission.

## Derivation and use

Do not infer exact transient behavior from only the dominant pole if a nearby zero or other pole has comparable residue. Compare pole location with physical mode shapes and sensor locations. In nonminimum-phase plants, pushing the response faster can increase initial inverse movement.

**Dimensional and sign audit.** Before substituting values, define an input and output in physical units, choose a positive direction, identify zero or equilibrium conditions, and make sure both sides of any differential or algebraic equation have the same dimensions. For pole locations, zeros and transient shape, changing coordinates or the chosen sensor location can reverse the sign or modify the apparent dynamics. A formula for ideal negative feedback must not be used when actual wiring implements positive feedback. Explicitly distinguish a continuous-time differential equation from a discrete update at sample index k.

## Worked numerical illustration

For poles at −2±j6 rad/s, the modal envelope decays as e⁻²ᵗ and the oscillation frequency is 6/(2π)=0.955 Hz.

**Reproduction protocol.** Write the givens and units in a table, compute any derived time scales or gains, substitute into the displayed model and calculate the result with more precision than required for the final reported value. Compare against a limiting case: zero disturbance, zero controller gain, vanishing sample time, or a stationary equilibrium as appropriate. If a calculation predicts infinite control force, negative dissipation, or motion through a hard stop, that is an indication to revisit assumptions, not a valid operating instruction.

## What the calculation does not establish

Pole-zero cancellation of an unstable internal mode does not guarantee an internally safe system.

This limitation matters particularly for **pole locations, zeros and transient shape**. The simplified example contains no manufacturing tolerances, no equipment-specific safety certification, and no direct evidence about the chosen hardware. Extra physics—sensor lag, actuator limits, cross-coupling, higher modes, friction, temperature drift or sampling delay—must be assessed according to the application. A model can be mathematically stable while the experiment violates the permitted range of current, speed, force or temperature.

## Practical reasoning and validation

1. **Define the measurement.** For this lesson, identify the smallest set of sensors that can distinguish the predicted mechanism from an alternative explanation. Record calibration, range, resolution, sampling rate and timestamps. Do not use commanded actuator signals as though they were measured actuator output.

2. **Plan excitation.** Choose a reversible stimulus small enough to respect the independent safety limits in the case: A laboratory servo must reach a commanded angle quickly without overshooting a mechanical end stop. A step, ramp, chirp, frequency sweep or deliberate small load perturbation may be appropriate, but there is no universal safe test amplitude. Start with the smallest informative test.

3. **Predict first.** Use the selected model to forecast the direction, scale and timing of at least one observation. Include what would refute the prediction. Predictions recorded before an experiment reduce the temptation to tune the story after seeing the result.

4. **Collect independent evidence.** Compare the predicted and measured quantities at more than one operating condition, including a held-out condition not used to fit parameters. Report transients, steady behavior and the actuator command on separate channels. Record uncertainty and do not hide residual patterns by averaging them away.

5. **Revise and document.** If the data disagree, consider model order, omitted delay, calibration bias, nonlinearity or incorrect sign before raising controller gain. Save the model version, parameter ranges, test date, and outstanding safety questions.

## Guided problems

**Problem A — definitions.** Draw the complete signal path for a system that must demonstrate pole locations, zeros and transient shape. Mark the reference, measured output, actual output, process disturbance and actuator constraint. State which quantities can be directly measured and which must be estimated.

**Problem B — quantitative reproduction.** Rework the example in this lesson using SI units, then change one numerical input by 10%. Report the result and a dimensionless sensitivity ratio. Explain whether a first-order approximation is appropriate.

**Problem C — alternate assumption.** Repeat the reasoning after adding either finite sample time, sensor bias or actuator saturation. Identify precisely which mathematical step is no longer valid and whether the expected effect is on stability, steady-state error or transient response.

**Problem D — experiment design.** Write a one-page safe bench-test protocol covering instrument checks, recorded variables, stimulus limits, shutdown logic and criteria for rejecting a fitted model. You must distinguish acceptance of a numerical model from approval to operate equipment.

**Problem E — peer challenge.** Argue against a proposed design that optimizes only one metric (such as settling time). Name at least two competing metrics and explain why evidence from the running case might change the preferred design.

## Worked answer path (not a substitute for a full design)

For A, write a block diagram with sensor noise entering the measurement channel and the disturbance entering the correct physical location; this prevents confusion between feedback error and actual tracking error. For B, compute the baseline result, recompute at 1.10 times the chosen parameter, and use sensitivity approximately (Δoutput/output)/(Δparameter/parameter), describing sign and any nonlinear dependence. For C, identify the changed assumption first; do not silently reuse the nominal transfer function. For D, report a test trace and a safety boundary independently. For E, make the tradeoff explicit rather than calling the fastest response automatically best.

## Reflection and next step

Keep each parameter attached to its physical units and measured provenance. Identify a single observation that would make you question the conclusion about **pole locations, zeros and transient shape**. At the end of the lesson record one corrected assumption, one remaining unknown and one measurable next action. The next section extends this reasoning to another part of the control loop; keep the previous model as a baseline for comparison.


---

# U02-L05 — Experimental step tests and system identification

**Mechanical Engineering · Control Systems Engineering · Unit 2: Time Response and Performance Specifications.**  This is an unreviewed instructional chapter; none of its calculations alone justifies commissioning machinery.

## What you should be able to do

Explain **experimental step tests and system identification** without confusing measured variables, hidden dynamics and desired behavior; write the main equation and derive its assumptions; reproduce the numerical illustration; diagnose at least two ways the model may mislead; and propose a practical, limited-risk verification experiment.

## Physical interpretation

Step tests estimate gain, lag, delay and repeatability but should not be performed blindly on equipment with safety limits. Detrend initial offsets; identify the actual actuator step rather than assuming the command occurred at the requested timestamp.

**System context.** A laboratory servo must reach a commanded angle quickly without overshooting a mechanical end stop. The objective in this lesson is not an abstract good-looking response: Translate performance requirements into characteristic times and transient response, not just a visually attractive plot. Establish whether the lesson concerns the plant itself, the mathematical input/output map, an estimator, a controller, or a test method. Those roles cannot be interchanged. A controller parameter may improve the command-response plot and simultaneously create unacceptable actuator current, mechanical strain or sensor-noise transmission.

## Derivation and use

A fitted first-order-plus-dead-time model uses K, τ and L. Compare predictions against a second held-out step; inspect residual autocorrelation and dependence on amplitude. Record confidence intervals when sensor noise and disturbance variation materially affect the estimate.

**Dimensional and sign audit.** Before substituting values, define an input and output in physical units, choose a positive direction, identify zero or equilibrium conditions, and make sure both sides of any differential or algebraic equation have the same dimensions. For experimental step tests and system identification, changing coordinates or the chosen sensor location can reverse the sign or modify the apparent dynamics. A formula for ideal negative feedback must not be used when actual wiring implements positive feedback. Explicitly distinguish a continuous-time differential equation from a discrete update at sample index k.

## Worked numerical illustration

When a 2 V step changes steady temperature by 10°C, the static gain is 5°C/V. If the response begins only after 3 s, the delay is approximately 3 s, separate from the thermal time constant.

**Reproduction protocol.** Write the givens and units in a table, compute any derived time scales or gains, substitute into the displayed model and calculate the result with more precision than required for the final reported value. Compare against a limiting case: zero disturbance, zero controller gain, vanishing sample time, or a stationary equilibrium as appropriate. If a calculation predicts infinite control force, negative dissipation, or motion through a hard stop, that is an indication to revisit assumptions, not a valid operating instruction.

## What the calculation does not establish

A step test cannot identify all hidden dynamics when several models reproduce the same observed output.

This limitation matters particularly for **experimental step tests and system identification**. The simplified example contains no manufacturing tolerances, no equipment-specific safety certification, and no direct evidence about the chosen hardware. Extra physics—sensor lag, actuator limits, cross-coupling, higher modes, friction, temperature drift or sampling delay—must be assessed according to the application. A model can be mathematically stable while the experiment violates the permitted range of current, speed, force or temperature.

## Practical reasoning and validation

1. **Define the measurement.** For this lesson, identify the smallest set of sensors that can distinguish the predicted mechanism from an alternative explanation. Record calibration, range, resolution, sampling rate and timestamps. Do not use commanded actuator signals as though they were measured actuator output.

2. **Plan excitation.** Choose a reversible stimulus small enough to respect the independent safety limits in the case: A laboratory servo must reach a commanded angle quickly without overshooting a mechanical end stop. A step, ramp, chirp, frequency sweep or deliberate small load perturbation may be appropriate, but there is no universal safe test amplitude. Start with the smallest informative test.

3. **Predict first.** Use the selected model to forecast the direction, scale and timing of at least one observation. Include what would refute the prediction. Predictions recorded before an experiment reduce the temptation to tune the story after seeing the result.

4. **Collect independent evidence.** Compare the predicted and measured quantities at more than one operating condition, including a held-out condition not used to fit parameters. Report transients, steady behavior and the actuator command on separate channels. Record uncertainty and do not hide residual patterns by averaging them away.

5. **Revise and document.** If the data disagree, consider model order, omitted delay, calibration bias, nonlinearity or incorrect sign before raising controller gain. Save the model version, parameter ranges, test date, and outstanding safety questions.

## Guided problems

**Problem A — definitions.** Draw the complete signal path for a system that must demonstrate experimental step tests and system identification. Mark the reference, measured output, actual output, process disturbance and actuator constraint. State which quantities can be directly measured and which must be estimated.

**Problem B — quantitative reproduction.** Rework the example in this lesson using SI units, then change one numerical input by 10%. Report the result and a dimensionless sensitivity ratio. Explain whether a first-order approximation is appropriate.

**Problem C — alternate assumption.** Repeat the reasoning after adding either finite sample time, sensor bias or actuator saturation. Identify precisely which mathematical step is no longer valid and whether the expected effect is on stability, steady-state error or transient response.

**Problem D — experiment design.** Write a one-page safe bench-test protocol covering instrument checks, recorded variables, stimulus limits, shutdown logic and criteria for rejecting a fitted model. You must distinguish acceptance of a numerical model from approval to operate equipment.

**Problem E — peer challenge.** Argue against a proposed design that optimizes only one metric (such as settling time). Name at least two competing metrics and explain why evidence from the running case might change the preferred design.

## Worked answer path (not a substitute for a full design)

For A, write a block diagram with sensor noise entering the measurement channel and the disturbance entering the correct physical location; this prevents confusion between feedback error and actual tracking error. For B, compute the baseline result, recompute at 1.10 times the chosen parameter, and use sensitivity approximately (Δoutput/output)/(Δparameter/parameter), describing sign and any nonlinear dependence. For C, identify the changed assumption first; do not silently reuse the nominal transfer function. For D, report a test trace and a safety boundary independently. For E, make the tradeoff explicit rather than calling the fastest response automatically best.

## Reflection and next step

Separate the equation derived under assumptions from the test that could challenge it. Identify a single observation that would make you question the conclusion about **experimental step tests and system identification**. At the end of the lesson record one corrected assumption, one remaining unknown and one measurable next action. The next section extends this reasoning to another part of the control loop; keep the previous model as a baseline for comparison.


---

