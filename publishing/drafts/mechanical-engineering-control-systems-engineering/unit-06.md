# Unit 06: State-Space and Modern Control

**Course Code**: CSE 306 · **Level**: Advanced Undergraduate Engineering

## Unit Overview & Physical Foundations

This comprehensive university textbook unit covers the theoretical framework, physical modeling, mathematical governing equations, and engineering applications of **State-Space and Modern Control**.

# U06-L01 — State variables and linear state models

**Mechanical Engineering · Control Systems Engineering · Unit 6: State-Space and Modern Control.**  This is an unreviewed instructional chapter; none of its calculations alone justifies commissioning machinery.

## What you should be able to do

Explain **state variables and linear state models** without confusing measured variables, hidden dynamics and desired behavior; write the main equation and derive its assumptions; reproduce the numerical illustration; diagnose at least two ways the model may mislead; and propose a practical, limited-risk verification experiment.

## Physical interpretation

A state vector contains the minimum independent dynamic information needed to predict future behavior under an input. A continuous LTI system uses ẋ=Ax+Bu and y=Cx+Du, where state, control and output matrices have specific dimensions.

**System context.** A cart servo moves position and velocity; only position is directly measured. The objective in this lesson is not an abstract good-looking response: Understand internal states and estimator limitations beyond a single transfer function. Establish whether the lesson concerns the plant itself, the mathematical input/output map, an estimator, a controller, or a test method. Those roles cannot be interchanged. A controller parameter may improve the command-response plot and simultaneously create unacceptable actuator current, mechanical strain or sensor-noise transmission.

## Derivation and use

For a mass–spring–damper plant take x=[position, velocity]ᵀ, giving A=[[0,1],[−k/m,−b/m]] and B=[[0],[1/m]], with position output C=[1,0]. This model explicitly exposes initial position and velocity.

**Dimensional and sign audit.** Before substituting values, define an input and output in physical units, choose a positive direction, identify zero or equilibrium conditions, and make sure both sides of any differential or algebraic equation have the same dimensions. For state variables and linear state models, changing coordinates or the chosen sensor location can reverse the sign or modify the apparent dynamics. A formula for ideal negative feedback must not be used when actual wiring implements positive feedback. Explicitly distinguish a continuous-time differential equation from a discrete update at sample index k.

## Worked numerical illustration

For m=2 kg, b=4 N·s/m, k=50 N/m, the state acceleration is −25x1−2x2+0.5u.

**Reproduction protocol.** Write the givens and units in a table, compute any derived time scales or gains, substitute into the displayed model and calculate the result with more precision than required for the final reported value. Compare against a limiting case: zero disturbance, zero controller gain, vanishing sample time, or a stationary equilibrium as appropriate. If a calculation predicts infinite control force, negative dissipation, or motion through a hard stop, that is an indication to revisit assumptions, not a valid operating instruction.

## What the calculation does not establish

An unmodeled friction state or input dead zone may invalidate a globally linear state description.

This limitation matters particularly for **state variables and linear state models**. The simplified example contains no manufacturing tolerances, no equipment-specific safety certification, and no direct evidence about the chosen hardware. Extra physics—sensor lag, actuator limits, cross-coupling, higher modes, friction, temperature drift or sampling delay—must be assessed according to the application. A model can be mathematically stable while the experiment violates the permitted range of current, speed, force or temperature.

## Practical reasoning and validation

1. **Define the measurement.** For this lesson, identify the smallest set of sensors that can distinguish the predicted mechanism from an alternative explanation. Record calibration, range, resolution, sampling rate and timestamps. Do not use commanded actuator signals as though they were measured actuator output.

2. **Plan excitation.** Choose a reversible stimulus small enough to respect the independent safety limits in the case: A cart servo moves position and velocity; only position is directly measured. A step, ramp, chirp, frequency sweep or deliberate small load perturbation may be appropriate, but there is no universal safe test amplitude. Start with the smallest informative test.

3. **Predict first.** Use the selected model to forecast the direction, scale and timing of at least one observation. Include what would refute the prediction. Predictions recorded before an experiment reduce the temptation to tune the story after seeing the result.

4. **Collect independent evidence.** Compare the predicted and measured quantities at more than one operating condition, including a held-out condition not used to fit parameters. Report transients, steady behavior and the actuator command on separate channels. Record uncertainty and do not hide residual patterns by averaging them away.

5. **Revise and document.** If the data disagree, consider model order, omitted delay, calibration bias, nonlinearity or incorrect sign before raising controller gain. Save the model version, parameter ranges, test date, and outstanding safety questions.

## Guided problems

**Problem A — definitions.** Draw the complete signal path for a system that must demonstrate state variables and linear state models. Mark the reference, measured output, actual output, process disturbance and actuator constraint. State which quantities can be directly measured and which must be estimated.

**Problem B — quantitative reproduction.** Rework the example in this lesson using SI units, then change one numerical input by 10%. Report the result and a dimensionless sensitivity ratio. Explain whether a first-order approximation is appropriate.

**Problem C — alternate assumption.** Repeat the reasoning after adding either finite sample time, sensor bias or actuator saturation. Identify precisely which mathematical step is no longer valid and whether the expected effect is on stability, steady-state error or transient response.

**Problem D — experiment design.** Write a one-page safe bench-test protocol covering instrument checks, recorded variables, stimulus limits, shutdown logic and criteria for rejecting a fitted model. You must distinguish acceptance of a numerical model from approval to operate equipment.

**Problem E — peer challenge.** Argue against a proposed design that optimizes only one metric (such as settling time). Name at least two competing metrics and explain why evidence from the running case might change the preferred design.

## Worked answer path (not a substitute for a full design)

For A, write a block diagram with sensor noise entering the measurement channel and the disturbance entering the correct physical location; this prevents confusion between feedback error and actual tracking error. For B, compute the baseline result, recompute at 1.10 times the chosen parameter, and use sensitivity approximately (Δoutput/output)/(Δparameter/parameter), describing sign and any nonlinear dependence. For C, identify the changed assumption first; do not silently reuse the nominal transfer function. For D, report a test trace and a safety boundary independently. For E, make the tradeoff explicit rather than calling the fastest response automatically best.

## Reflection and next step

Separate the equation derived under assumptions from the test that could challenge it. Identify a single observation that would make you question the conclusion about **state variables and linear state models**. At the end of the lesson record one corrected assumption, one remaining unknown and one measurable next action. The next section extends this reasoning to another part of the control loop; keep the previous model as a baseline for comparison.


---

# U06-L02 — Controllability and reachable states

**Mechanical Engineering · Control Systems Engineering · Unit 6: State-Space and Modern Control.**  This is an unreviewed instructional chapter; none of its calculations alone justifies commissioning machinery.

## What you should be able to do

Explain **controllability and reachable states** without confusing measured variables, hidden dynamics and desired behavior; write the main equation and derive its assumptions; reproduce the numerical illustration; diagnose at least two ways the model may mislead; and propose a practical, limited-risk verification experiment.

## Physical interpretation

For ẋ=Ax+Bu, controllability is tested by rank[B,AB,…,A^(n−1)B]=n. Full rank implies arbitrary finite-time state transfers for an unconstrained linear system, not that these transfers are physically safe.

**System context.** A cart servo moves position and velocity; only position is directly measured. The objective in this lesson is not an abstract good-looking response: Understand internal states and estimator limitations beyond a single transfer function. Establish whether the lesson concerns the plant itself, the mathematical input/output map, an estimator, a controller, or a test method. Those roles cannot be interchanged. A controller parameter may improve the command-response plot and simultaneously create unacceptable actuator current, mechanical strain or sensor-noise transmission.

## Derivation and use

A mass-position system with force input directly accelerates its second state and influences the first through integration, yielding a controllable pair. Scaling of states matters when evaluating near-singular numerical controllability.

**Dimensional and sign audit.** Before substituting values, define an input and output in physical units, choose a positive direction, identify zero or equilibrium conditions, and make sure both sides of any differential or algebraic equation have the same dimensions. For controllability and reachable states, changing coordinates or the chosen sensor location can reverse the sign or modify the apparent dynamics. A formula for ideal negative feedback must not be used when actual wiring implements positive feedback. Explicitly distinguish a continuous-time differential equation from a discrete update at sample index k.

## Worked numerical illustration

For double integrator A=[[0,1],[0,0]] and B=[[0],[1]], controllability matrix [B,AB]=[[0,1],[1,0]], rank 2.

**Reproduction protocol.** Write the givens and units in a table, compute any derived time scales or gains, substitute into the displayed model and calculate the result with more precision than required for the final reported value. Compare against a limiting case: zero disturbance, zero controller gain, vanishing sample time, or a stationary equilibrium as appropriate. If a calculation predicts infinite control force, negative dissipation, or motion through a hard stop, that is an indication to revisit assumptions, not a valid operating instruction.

## What the calculation does not establish

Actuator saturation, travel limits and rate constraints can make formally controllable targets unreachable in practice.

This limitation matters particularly for **controllability and reachable states**. The simplified example contains no manufacturing tolerances, no equipment-specific safety certification, and no direct evidence about the chosen hardware. Extra physics—sensor lag, actuator limits, cross-coupling, higher modes, friction, temperature drift or sampling delay—must be assessed according to the application. A model can be mathematically stable while the experiment violates the permitted range of current, speed, force or temperature.

## Practical reasoning and validation

1. **Define the measurement.** For this lesson, identify the smallest set of sensors that can distinguish the predicted mechanism from an alternative explanation. Record calibration, range, resolution, sampling rate and timestamps. Do not use commanded actuator signals as though they were measured actuator output.

2. **Plan excitation.** Choose a reversible stimulus small enough to respect the independent safety limits in the case: A cart servo moves position and velocity; only position is directly measured. A step, ramp, chirp, frequency sweep or deliberate small load perturbation may be appropriate, but there is no universal safe test amplitude. Start with the smallest informative test.

3. **Predict first.** Use the selected model to forecast the direction, scale and timing of at least one observation. Include what would refute the prediction. Predictions recorded before an experiment reduce the temptation to tune the story after seeing the result.

4. **Collect independent evidence.** Compare the predicted and measured quantities at more than one operating condition, including a held-out condition not used to fit parameters. Report transients, steady behavior and the actuator command on separate channels. Record uncertainty and do not hide residual patterns by averaging them away.

5. **Revise and document.** If the data disagree, consider model order, omitted delay, calibration bias, nonlinearity or incorrect sign before raising controller gain. Save the model version, parameter ranges, test date, and outstanding safety questions.

## Guided problems

**Problem A — definitions.** Draw the complete signal path for a system that must demonstrate controllability and reachable states. Mark the reference, measured output, actual output, process disturbance and actuator constraint. State which quantities can be directly measured and which must be estimated.

**Problem B — quantitative reproduction.** Rework the example in this lesson using SI units, then change one numerical input by 10%. Report the result and a dimensionless sensitivity ratio. Explain whether a first-order approximation is appropriate.

**Problem C — alternate assumption.** Repeat the reasoning after adding either finite sample time, sensor bias or actuator saturation. Identify precisely which mathematical step is no longer valid and whether the expected effect is on stability, steady-state error or transient response.

**Problem D — experiment design.** Write a one-page safe bench-test protocol covering instrument checks, recorded variables, stimulus limits, shutdown logic and criteria for rejecting a fitted model. You must distinguish acceptance of a numerical model from approval to operate equipment.

**Problem E — peer challenge.** Argue against a proposed design that optimizes only one metric (such as settling time). Name at least two competing metrics and explain why evidence from the running case might change the preferred design.

## Worked answer path (not a substitute for a full design)

For A, write a block diagram with sensor noise entering the measurement channel and the disturbance entering the correct physical location; this prevents confusion between feedback error and actual tracking error. For B, compute the baseline result, recompute at 1.10 times the chosen parameter, and use sensitivity approximately (Δoutput/output)/(Δparameter/parameter), describing sign and any nonlinear dependence. For C, identify the changed assumption first; do not silently reuse the nominal transfer function. For D, report a test trace and a safety boundary independently. For E, make the tradeoff explicit rather than calling the fastest response automatically best.

## Reflection and next step

Check the controller command and all constrained internal states, not merely the output. Identify a single observation that would make you question the conclusion about **controllability and reachable states**. At the end of the lesson record one corrected assumption, one remaining unknown and one measurable next action. The next section extends this reasoning to another part of the control loop; keep the previous model as a baseline for comparison.


---

# U06-L03 — Observability and sensor selection

**Mechanical Engineering · Control Systems Engineering · Unit 6: State-Space and Modern Control.**  This is an unreviewed instructional chapter; none of its calculations alone justifies commissioning machinery.

## What you should be able to do

Explain **observability and sensor selection** without confusing measured variables, hidden dynamics and desired behavior; write the main equation and derive its assumptions; reproduce the numerical illustration; diagnose at least two ways the model may mislead; and propose a practical, limited-risk verification experiment.

## Physical interpretation

For y=Cx, the observability matrix [C;CA;…;CA^(n−1)] must have full rank to reconstruct the state of a linear system. Sensor placement determines what internal motion is visible, and noise affects practical observability.

**System context.** A cart servo moves position and velocity; only position is directly measured. The objective in this lesson is not an abstract good-looking response: Understand internal states and estimator limitations beyond a single transfer function. Establish whether the lesson concerns the plant itself, the mathematical input/output map, an estimator, a controller, or a test method. Those roles cannot be interchanged. A controller parameter may improve the command-response plot and simultaneously create unacceptable actuator current, mechanical strain or sensor-noise transmission.

## Derivation and use

A position sensor on a double integrator gives C=[1,0] and CA=[0,1], so both position and velocity are mathematically observable. Reconstructed velocity may be noisy when position is quantized.

**Dimensional and sign audit.** Before substituting values, define an input and output in physical units, choose a positive direction, identify zero or equilibrium conditions, and make sure both sides of any differential or algebraic equation have the same dimensions. For observability and sensor selection, changing coordinates or the chosen sensor location can reverse the sign or modify the apparent dynamics. A formula for ideal negative feedback must not be used when actual wiring implements positive feedback. Explicitly distinguish a continuous-time differential equation from a discrete update at sample index k.

## Worked numerical illustration

For A=[[0,1],[0,0]] and C=[1,0], observability determinant is 1, confirming rank 2.

**Reproduction protocol.** Write the givens and units in a table, compute any derived time scales or gains, substitute into the displayed model and calculate the result with more precision than required for the final reported value. Compare against a limiting case: zero disturbance, zero controller gain, vanishing sample time, or a stationary equilibrium as appropriate. If a calculation predicts infinite control force, negative dissipation, or motion through a hard stop, that is an indication to revisit assumptions, not a valid operating instruction.

## What the calculation does not establish

An unobservable unstable internal mode is especially dangerous because its growth may not be seen in the measured output.

This limitation matters particularly for **observability and sensor selection**. The simplified example contains no manufacturing tolerances, no equipment-specific safety certification, and no direct evidence about the chosen hardware. Extra physics—sensor lag, actuator limits, cross-coupling, higher modes, friction, temperature drift or sampling delay—must be assessed according to the application. A model can be mathematically stable while the experiment violates the permitted range of current, speed, force or temperature.

## Practical reasoning and validation

1. **Define the measurement.** For this lesson, identify the smallest set of sensors that can distinguish the predicted mechanism from an alternative explanation. Record calibration, range, resolution, sampling rate and timestamps. Do not use commanded actuator signals as though they were measured actuator output.

2. **Plan excitation.** Choose a reversible stimulus small enough to respect the independent safety limits in the case: A cart servo moves position and velocity; only position is directly measured. A step, ramp, chirp, frequency sweep or deliberate small load perturbation may be appropriate, but there is no universal safe test amplitude. Start with the smallest informative test.

3. **Predict first.** Use the selected model to forecast the direction, scale and timing of at least one observation. Include what would refute the prediction. Predictions recorded before an experiment reduce the temptation to tune the story after seeing the result.

4. **Collect independent evidence.** Compare the predicted and measured quantities at more than one operating condition, including a held-out condition not used to fit parameters. Report transients, steady behavior and the actuator command on separate channels. Record uncertainty and do not hide residual patterns by averaging them away.

5. **Revise and document.** If the data disagree, consider model order, omitted delay, calibration bias, nonlinearity or incorrect sign before raising controller gain. Save the model version, parameter ranges, test date, and outstanding safety questions.

## Guided problems

**Problem A — definitions.** Draw the complete signal path for a system that must demonstrate observability and sensor selection. Mark the reference, measured output, actual output, process disturbance and actuator constraint. State which quantities can be directly measured and which must be estimated.

**Problem B — quantitative reproduction.** Rework the example in this lesson using SI units, then change one numerical input by 10%. Report the result and a dimensionless sensitivity ratio. Explain whether a first-order approximation is appropriate.

**Problem C — alternate assumption.** Repeat the reasoning after adding either finite sample time, sensor bias or actuator saturation. Identify precisely which mathematical step is no longer valid and whether the expected effect is on stability, steady-state error or transient response.

**Problem D — experiment design.** Write a one-page safe bench-test protocol covering instrument checks, recorded variables, stimulus limits, shutdown logic and criteria for rejecting a fitted model. You must distinguish acceptance of a numerical model from approval to operate equipment.

**Problem E — peer challenge.** Argue against a proposed design that optimizes only one metric (such as settling time). Name at least two competing metrics and explain why evidence from the running case might change the preferred design.

## Worked answer path (not a substitute for a full design)

For A, write a block diagram with sensor noise entering the measurement channel and the disturbance entering the correct physical location; this prevents confusion between feedback error and actual tracking error. For B, compute the baseline result, recompute at 1.10 times the chosen parameter, and use sensitivity approximately (Δoutput/output)/(Δparameter/parameter), describing sign and any nonlinear dependence. For C, identify the changed assumption first; do not silently reuse the nominal transfer function. For D, report a test trace and a safety boundary independently. For E, make the tradeoff explicit rather than calling the fastest response automatically best.

## Reflection and next step

Use the result as a foundation for a decision with a stated uncertainty interval. Identify a single observation that would make you question the conclusion about **observability and sensor selection**. At the end of the lesson record one corrected assumption, one remaining unknown and one measurable next action. The next section extends this reasoning to another part of the control loop; keep the previous model as a baseline for comparison.


---

# U06-L04 — State feedback and pole placement

**Mechanical Engineering · Control Systems Engineering · Unit 6: State-Space and Modern Control.**  This is an unreviewed instructional chapter; none of its calculations alone justifies commissioning machinery.

## What you should be able to do

Explain **state feedback and pole placement** without confusing measured variables, hidden dynamics and desired behavior; write the main equation and derive its assumptions; reproduce the numerical illustration; diagnose at least two ways the model may mislead; and propose a practical, limited-risk verification experiment.

## Physical interpretation

State feedback u=−Kx+N r changes the state dynamics to A−BK. When the pair (A,B) is controllable, poles can be assigned in the ideal linear model. Reference precompensation N must be calculated for the selected output and sign convention.

**System context.** A cart servo moves position and velocity; only position is directly measured. The objective in this lesson is not an abstract good-looking response: Understand internal states and estimator limitations beyond a single transfer function. Establish whether the lesson concerns the plant itself, the mathematical input/output map, an estimator, a controller, or a test method. Those roles cannot be interchanged. A controller parameter may improve the command-response plot and simultaneously create unacceptable actuator current, mechanical strain or sensor-noise transmission.

## Derivation and use

Before calculating K, choose reasonable desired poles using physical actuator speed, mechanical resonance and sample period. Verify simulated control effort and robustness to measurement errors; state feedback does not supply state estimates by itself.

**Dimensional and sign audit.** Before substituting values, define an input and output in physical units, choose a positive direction, identify zero or equilibrium conditions, and make sure both sides of any differential or algebraic equation have the same dimensions. For state feedback and pole placement, changing coordinates or the chosen sensor location can reverse the sign or modify the apparent dynamics. A formula for ideal negative feedback must not be used when actual wiring implements positive feedback. Explicitly distinguish a continuous-time differential equation from a discrete update at sample index k.

## Worked numerical illustration

For double integrator ẍ=u, u=−k1x−k2ẋ produces characteristic s²+k2s+k1. Desired poles at −2 and −3 require k2=5 and k1=6.

**Reproduction protocol.** Write the givens and units in a table, compute any derived time scales or gains, substitute into the displayed model and calculate the result with more precision than required for the final reported value. Compare against a limiting case: zero disturbance, zero controller gain, vanishing sample time, or a stationary equilibrium as appropriate. If a calculation predicts infinite control force, negative dissipation, or motion through a hard stop, that is an indication to revisit assumptions, not a valid operating instruction.

## What the calculation does not establish

Pole placement can demand extreme control effort when desired poles are much faster than actuator dynamics.

This limitation matters particularly for **state feedback and pole placement**. The simplified example contains no manufacturing tolerances, no equipment-specific safety certification, and no direct evidence about the chosen hardware. Extra physics—sensor lag, actuator limits, cross-coupling, higher modes, friction, temperature drift or sampling delay—must be assessed according to the application. A model can be mathematically stable while the experiment violates the permitted range of current, speed, force or temperature.

## Practical reasoning and validation

1. **Define the measurement.** For this lesson, identify the smallest set of sensors that can distinguish the predicted mechanism from an alternative explanation. Record calibration, range, resolution, sampling rate and timestamps. Do not use commanded actuator signals as though they were measured actuator output.

2. **Plan excitation.** Choose a reversible stimulus small enough to respect the independent safety limits in the case: A cart servo moves position and velocity; only position is directly measured. A step, ramp, chirp, frequency sweep or deliberate small load perturbation may be appropriate, but there is no universal safe test amplitude. Start with the smallest informative test.

3. **Predict first.** Use the selected model to forecast the direction, scale and timing of at least one observation. Include what would refute the prediction. Predictions recorded before an experiment reduce the temptation to tune the story after seeing the result.

4. **Collect independent evidence.** Compare the predicted and measured quantities at more than one operating condition, including a held-out condition not used to fit parameters. Report transients, steady behavior and the actuator command on separate channels. Record uncertainty and do not hide residual patterns by averaging them away.

5. **Revise and document.** If the data disagree, consider model order, omitted delay, calibration bias, nonlinearity or incorrect sign before raising controller gain. Save the model version, parameter ranges, test date, and outstanding safety questions.

## Guided problems

**Problem A — definitions.** Draw the complete signal path for a system that must demonstrate state feedback and pole placement. Mark the reference, measured output, actual output, process disturbance and actuator constraint. State which quantities can be directly measured and which must be estimated.

**Problem B — quantitative reproduction.** Rework the example in this lesson using SI units, then change one numerical input by 10%. Report the result and a dimensionless sensitivity ratio. Explain whether a first-order approximation is appropriate.

**Problem C — alternate assumption.** Repeat the reasoning after adding either finite sample time, sensor bias or actuator saturation. Identify precisely which mathematical step is no longer valid and whether the expected effect is on stability, steady-state error or transient response.

**Problem D — experiment design.** Write a one-page safe bench-test protocol covering instrument checks, recorded variables, stimulus limits, shutdown logic and criteria for rejecting a fitted model. You must distinguish acceptance of a numerical model from approval to operate equipment.

**Problem E — peer challenge.** Argue against a proposed design that optimizes only one metric (such as settling time). Name at least two competing metrics and explain why evidence from the running case might change the preferred design.

## Worked answer path (not a substitute for a full design)

For A, write a block diagram with sensor noise entering the measurement channel and the disturbance entering the correct physical location; this prevents confusion between feedback error and actual tracking error. For B, compute the baseline result, recompute at 1.10 times the chosen parameter, and use sensitivity approximately (Δoutput/output)/(Δparameter/parameter), describing sign and any nonlinear dependence. For C, identify the changed assumption first; do not silently reuse the nominal transfer function. For D, report a test trace and a safety boundary independently. For E, make the tradeoff explicit rather than calling the fastest response automatically best.

## Reflection and next step

Identify the cause of the response, not only the observed waveform. Identify a single observation that would make you question the conclusion about **state feedback and pole placement**. At the end of the lesson record one corrected assumption, one remaining unknown and one measurable next action. The next section extends this reasoning to another part of the control loop; keep the previous model as a baseline for comparison.


---

# U06-L05 — Observers, Kalman filtering and estimation

**Mechanical Engineering · Control Systems Engineering · Unit 6: State-Space and Modern Control.**  This is an unreviewed instructional chapter; none of its calculations alone justifies commissioning machinery.

## What you should be able to do

Explain **observers, kalman filtering and estimation** without confusing measured variables, hidden dynamics and desired behavior; write the main equation and derive its assumptions; reproduce the numerical illustration; diagnose at least two ways the model may mislead; and propose a practical, limited-risk verification experiment.

## Physical interpretation

A Luenberger observer x̂̇=Ax̂+Bu+L(y−Cx̂) has estimation-error dynamics ė=(A−LC)e under ideal matching. Choosing L requires observability. A Kalman filter additionally uses noise covariance assumptions to balance prediction and measurement.

**System context.** A cart servo moves position and velocity; only position is directly measured. The objective in this lesson is not an abstract good-looking response: Understand internal states and estimator limitations beyond a single transfer function. Establish whether the lesson concerns the plant itself, the mathematical input/output map, an estimator, a controller, or a test method. Those roles cannot be interchanged. A controller parameter may improve the command-response plot and simultaneously create unacceptable actuator current, mechanical strain or sensor-noise transmission.

## Derivation and use

Separate plant-state estimates from actual state measurements. Check initial conditions, sensor bias, sample timing and noise. An extremely fast observer amplifies noise and may require more actuator or computing bandwidth.

**Dimensional and sign audit.** Before substituting values, define an input and output in physical units, choose a positive direction, identify zero or equilibrium conditions, and make sure both sides of any differential or algebraic equation have the same dimensions. For observers, kalman filtering and estimation, changing coordinates or the chosen sensor location can reverse the sign or modify the apparent dynamics. A formula for ideal negative feedback must not be used when actual wiring implements positive feedback. Explicitly distinguish a continuous-time differential equation from a discrete update at sample index k.

## Worked numerical illustration

For scalar ẋ=−2x+u, y=x and observer gain L=4, ideal estimation error decays as ė=−6e; the error time constant is 1/6 s.

**Reproduction protocol.** Write the givens and units in a table, compute any derived time scales or gains, substitute into the displayed model and calculate the result with more precision than required for the final reported value. Compare against a limiting case: zero disturbance, zero controller gain, vanishing sample time, or a stationary equilibrium as appropriate. If a calculation predicts infinite control force, negative dissipation, or motion through a hard stop, that is an indication to revisit assumptions, not a valid operating instruction.

## What the calculation does not establish

Kalman gains are not guaranteed statistically optimal if assumed noise covariances or model dynamics are wrong.

This limitation matters particularly for **observers, kalman filtering and estimation**. The simplified example contains no manufacturing tolerances, no equipment-specific safety certification, and no direct evidence about the chosen hardware. Extra physics—sensor lag, actuator limits, cross-coupling, higher modes, friction, temperature drift or sampling delay—must be assessed according to the application. A model can be mathematically stable while the experiment violates the permitted range of current, speed, force or temperature.

## Practical reasoning and validation

1. **Define the measurement.** For this lesson, identify the smallest set of sensors that can distinguish the predicted mechanism from an alternative explanation. Record calibration, range, resolution, sampling rate and timestamps. Do not use commanded actuator signals as though they were measured actuator output.

2. **Plan excitation.** Choose a reversible stimulus small enough to respect the independent safety limits in the case: A cart servo moves position and velocity; only position is directly measured. A step, ramp, chirp, frequency sweep or deliberate small load perturbation may be appropriate, but there is no universal safe test amplitude. Start with the smallest informative test.

3. **Predict first.** Use the selected model to forecast the direction, scale and timing of at least one observation. Include what would refute the prediction. Predictions recorded before an experiment reduce the temptation to tune the story after seeing the result.

4. **Collect independent evidence.** Compare the predicted and measured quantities at more than one operating condition, including a held-out condition not used to fit parameters. Report transients, steady behavior and the actuator command on separate channels. Record uncertainty and do not hide residual patterns by averaging them away.

5. **Revise and document.** If the data disagree, consider model order, omitted delay, calibration bias, nonlinearity or incorrect sign before raising controller gain. Save the model version, parameter ranges, test date, and outstanding safety questions.

## Guided problems

**Problem A — definitions.** Draw the complete signal path for a system that must demonstrate observers, kalman filtering and estimation. Mark the reference, measured output, actual output, process disturbance and actuator constraint. State which quantities can be directly measured and which must be estimated.

**Problem B — quantitative reproduction.** Rework the example in this lesson using SI units, then change one numerical input by 10%. Report the result and a dimensionless sensitivity ratio. Explain whether a first-order approximation is appropriate.

**Problem C — alternate assumption.** Repeat the reasoning after adding either finite sample time, sensor bias or actuator saturation. Identify precisely which mathematical step is no longer valid and whether the expected effect is on stability, steady-state error or transient response.

**Problem D — experiment design.** Write a one-page safe bench-test protocol covering instrument checks, recorded variables, stimulus limits, shutdown logic and criteria for rejecting a fitted model. You must distinguish acceptance of a numerical model from approval to operate equipment.

**Problem E — peer challenge.** Argue against a proposed design that optimizes only one metric (such as settling time). Name at least two competing metrics and explain why evidence from the running case might change the preferred design.

## Worked answer path (not a substitute for a full design)

For A, write a block diagram with sensor noise entering the measurement channel and the disturbance entering the correct physical location; this prevents confusion between feedback error and actual tracking error. For B, compute the baseline result, recompute at 1.10 times the chosen parameter, and use sensitivity approximately (Δoutput/output)/(Δparameter/parameter), describing sign and any nonlinear dependence. For C, identify the changed assumption first; do not silently reuse the nominal transfer function. For D, report a test trace and a safety boundary independently. For E, make the tradeoff explicit rather than calling the fastest response automatically best.

## Reflection and next step

Keep each parameter attached to its physical units and measured provenance. Identify a single observation that would make you question the conclusion about **observers, kalman filtering and estimation**. At the end of the lesson record one corrected assumption, one remaining unknown and one measurable next action. The next section extends this reasoning to another part of the control loop; keep the previous model as a baseline for comparison.


---

