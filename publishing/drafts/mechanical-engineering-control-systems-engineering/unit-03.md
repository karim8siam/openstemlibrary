# Unit 03: Stability, Error, and Robustness

**Course Code**: CSE 303 · **Level**: Advanced Undergraduate Engineering

## Unit Overview & Physical Foundations

This comprehensive university textbook unit covers the theoretical framework, physical modeling, mathematical governing equations, and engineering applications of **Stability, Error, and Robustness**.

# U03-L01 — Closed-loop characteristic equations

**Mechanical Engineering · Control Systems Engineering · Unit 3: Stability, Error, and Robustness.**  This is an unreviewed instructional chapter; none of its calculations alone justifies commissioning machinery.

## What you should be able to do

Explain **closed-loop characteristic equations** without confusing measured variables, hidden dynamics and desired behavior; write the main equation and derive its assumptions; reproduce the numerical illustration; diagnose at least two ways the model may mislead; and propose a practical, limited-risk verification experiment.

## Physical interpretation

Closed-loop poles are roots of 1+C(s)G(s)=0 after assembling the actual loop. For rational functions, multiply through correctly and check physically meaningful gains and stable hidden modes.

**System context.** An adjustable-speed drive appears fast in simulation but oscillates with a longer cable and a heavier inertia load. The objective in this lesson is not an abstract good-looking response: Check internal stability before interpreting tracking plots or increasing gains. Establish whether the lesson concerns the plant itself, the mathematical input/output map, an estimator, a controller, or a test method. Those roles cannot be interchanged. A controller parameter may improve the command-response plot and simultaneously create unacceptable actuator current, mechanical strain or sensor-noise transmission.

## Derivation and use

The denominator of the closed-loop transfer function is not enough if unstable modes are canceled algebraically between numerator and denominator. Internal stability asks whether all relevant internal signals remain bounded for bounded disturbances.

**Dimensional and sign audit.** Before substituting values, define an input and output in physical units, choose a positive direction, identify zero or equilibrium conditions, and make sure both sides of any differential or algebraic equation have the same dimensions. For closed-loop characteristic equations, changing coordinates or the chosen sensor location can reverse the sign or modify the apparent dynamics. A formula for ideal negative feedback must not be used when actual wiring implements positive feedback. Explicitly distinguish a continuous-time differential equation from a discrete update at sample index k.

## Worked numerical illustration

With G(s)=1/(s(s+2)) and C(s)=K, the characteristic polynomial is s²+2s+K; K>0 gives stable second-order poles.

**Reproduction protocol.** Write the givens and units in a table, compute any derived time scales or gains, substitute into the displayed model and calculate the result with more precision than required for the final reported value. Compare against a limiting case: zero disturbance, zero controller gain, vanishing sample time, or a stationary equilibrium as appropriate. If a calculation predicts infinite control force, negative dissipation, or motion through a hard stop, that is an indication to revisit assumptions, not a valid operating instruction.

## What the calculation does not establish

Sign mistakes in encoder direction or motor torque can convert negative feedback into dangerous positive feedback.

This limitation matters particularly for **closed-loop characteristic equations**. The simplified example contains no manufacturing tolerances, no equipment-specific safety certification, and no direct evidence about the chosen hardware. Extra physics—sensor lag, actuator limits, cross-coupling, higher modes, friction, temperature drift or sampling delay—must be assessed according to the application. A model can be mathematically stable while the experiment violates the permitted range of current, speed, force or temperature.

## Practical reasoning and validation

1. **Define the measurement.** For this lesson, identify the smallest set of sensors that can distinguish the predicted mechanism from an alternative explanation. Record calibration, range, resolution, sampling rate and timestamps. Do not use commanded actuator signals as though they were measured actuator output.

2. **Plan excitation.** Choose a reversible stimulus small enough to respect the independent safety limits in the case: An adjustable-speed drive appears fast in simulation but oscillates with a longer cable and a heavier inertia load. A step, ramp, chirp, frequency sweep or deliberate small load perturbation may be appropriate, but there is no universal safe test amplitude. Start with the smallest informative test.

3. **Predict first.** Use the selected model to forecast the direction, scale and timing of at least one observation. Include what would refute the prediction. Predictions recorded before an experiment reduce the temptation to tune the story after seeing the result.

4. **Collect independent evidence.** Compare the predicted and measured quantities at more than one operating condition, including a held-out condition not used to fit parameters. Report transients, steady behavior and the actuator command on separate channels. Record uncertainty and do not hide residual patterns by averaging them away.

5. **Revise and document.** If the data disagree, consider model order, omitted delay, calibration bias, nonlinearity or incorrect sign before raising controller gain. Save the model version, parameter ranges, test date, and outstanding safety questions.

## Guided problems

**Problem A — definitions.** Draw the complete signal path for a system that must demonstrate closed-loop characteristic equations. Mark the reference, measured output, actual output, process disturbance and actuator constraint. State which quantities can be directly measured and which must be estimated.

**Problem B — quantitative reproduction.** Rework the example in this lesson using SI units, then change one numerical input by 10%. Report the result and a dimensionless sensitivity ratio. Explain whether a first-order approximation is appropriate.

**Problem C — alternate assumption.** Repeat the reasoning after adding either finite sample time, sensor bias or actuator saturation. Identify precisely which mathematical step is no longer valid and whether the expected effect is on stability, steady-state error or transient response.

**Problem D — experiment design.** Write a one-page safe bench-test protocol covering instrument checks, recorded variables, stimulus limits, shutdown logic and criteria for rejecting a fitted model. You must distinguish acceptance of a numerical model from approval to operate equipment.

**Problem E — peer challenge.** Argue against a proposed design that optimizes only one metric (such as settling time). Name at least two competing metrics and explain why evidence from the running case might change the preferred design.

## Worked answer path (not a substitute for a full design)

For A, write a block diagram with sensor noise entering the measurement channel and the disturbance entering the correct physical location; this prevents confusion between feedback error and actual tracking error. For B, compute the baseline result, recompute at 1.10 times the chosen parameter, and use sensitivity approximately (Δoutput/output)/(Δparameter/parameter), describing sign and any nonlinear dependence. For C, identify the changed assumption first; do not silently reuse the nominal transfer function. For D, report a test trace and a safety boundary independently. For E, make the tradeoff explicit rather than calling the fastest response automatically best.

## Reflection and next step

Use the result as a foundation for a decision with a stated uncertainty interval. Identify a single observation that would make you question the conclusion about **closed-loop characteristic equations**. At the end of the lesson record one corrected assumption, one remaining unknown and one measurable next action. The next section extends this reasoning to another part of the control loop; keep the previous model as a baseline for comparison.


---

# U03-L02 — Routh–Hurwitz stability screening

**Mechanical Engineering · Control Systems Engineering · Unit 3: Stability, Error, and Robustness.**  This is an unreviewed instructional chapter; none of its calculations alone justifies commissioning machinery.

## What you should be able to do

Explain **routh–hurwitz stability screening** without confusing measured variables, hidden dynamics and desired behavior; write the main equation and derive its assumptions; reproduce the numerical illustration; diagnose at least two ways the model may mislead; and propose a practical, limited-risk verification experiment.

## Physical interpretation

For a continuous-time cubic s³+a₂s²+a₁s+a₀ with positive leading coefficient, necessary and sufficient Hurwitz conditions are a₂>0, a₁>0, a₀>0 and a₂a₁>a₀. Routh arrays extend this algebraic test to higher-order real polynomials.

**System context.** An adjustable-speed drive appears fast in simulation but oscillates with a longer cable and a heavier inertia load. The objective in this lesson is not an abstract good-looking response: Check internal stability before interpreting tracking plots or increasing gains. Establish whether the lesson concerns the plant itself, the mathematical input/output map, an estimator, a controller, or a test method. Those roles cannot be interchanged. A controller parameter may improve the command-response plot and simultaneously create unacceptable actuator current, mechanical strain or sensor-noise transmission.

## Derivation and use

Construct the table using exact coefficients and interpret sign changes in its first column. Special cases with zero first-column elements or zero rows require additional treatment rather than division by zero.

**Dimensional and sign audit.** Before substituting values, define an input and output in physical units, choose a positive direction, identify zero or equilibrium conditions, and make sure both sides of any differential or algebraic equation have the same dimensions. For routh–hurwitz stability screening, changing coordinates or the chosen sensor location can reverse the sign or modify the apparent dynamics. A formula for ideal negative feedback must not be used when actual wiring implements positive feedback. Explicitly distinguish a continuous-time differential equation from a discrete update at sample index k.

## Worked numerical illustration

For p(s)=s³+4s²+5s+K, stable operation for positive K requires 0<K<20. At K=20 the system is marginal and needs further analysis.

**Reproduction protocol.** Write the givens and units in a table, compute any derived time scales or gains, substitute into the displayed model and calculate the result with more precision than required for the final reported value. Compare against a limiting case: zero disturbance, zero controller gain, vanishing sample time, or a stationary equilibrium as appropriate. If a calculation predicts infinite control force, negative dissipation, or motion through a hard stop, that is an indication to revisit assumptions, not a valid operating instruction.

## What the calculation does not establish

The Routh test says whether poles enter the right-half plane; it does not quantify acceptable tracking or margin against uncertainty.

This limitation matters particularly for **routh–hurwitz stability screening**. The simplified example contains no manufacturing tolerances, no equipment-specific safety certification, and no direct evidence about the chosen hardware. Extra physics—sensor lag, actuator limits, cross-coupling, higher modes, friction, temperature drift or sampling delay—must be assessed according to the application. A model can be mathematically stable while the experiment violates the permitted range of current, speed, force or temperature.

## Practical reasoning and validation

1. **Define the measurement.** For this lesson, identify the smallest set of sensors that can distinguish the predicted mechanism from an alternative explanation. Record calibration, range, resolution, sampling rate and timestamps. Do not use commanded actuator signals as though they were measured actuator output.

2. **Plan excitation.** Choose a reversible stimulus small enough to respect the independent safety limits in the case: An adjustable-speed drive appears fast in simulation but oscillates with a longer cable and a heavier inertia load. A step, ramp, chirp, frequency sweep or deliberate small load perturbation may be appropriate, but there is no universal safe test amplitude. Start with the smallest informative test.

3. **Predict first.** Use the selected model to forecast the direction, scale and timing of at least one observation. Include what would refute the prediction. Predictions recorded before an experiment reduce the temptation to tune the story after seeing the result.

4. **Collect independent evidence.** Compare the predicted and measured quantities at more than one operating condition, including a held-out condition not used to fit parameters. Report transients, steady behavior and the actuator command on separate channels. Record uncertainty and do not hide residual patterns by averaging them away.

5. **Revise and document.** If the data disagree, consider model order, omitted delay, calibration bias, nonlinearity or incorrect sign before raising controller gain. Save the model version, parameter ranges, test date, and outstanding safety questions.

## Guided problems

**Problem A — definitions.** Draw the complete signal path for a system that must demonstrate routh–hurwitz stability screening. Mark the reference, measured output, actual output, process disturbance and actuator constraint. State which quantities can be directly measured and which must be estimated.

**Problem B — quantitative reproduction.** Rework the example in this lesson using SI units, then change one numerical input by 10%. Report the result and a dimensionless sensitivity ratio. Explain whether a first-order approximation is appropriate.

**Problem C — alternate assumption.** Repeat the reasoning after adding either finite sample time, sensor bias or actuator saturation. Identify precisely which mathematical step is no longer valid and whether the expected effect is on stability, steady-state error or transient response.

**Problem D — experiment design.** Write a one-page safe bench-test protocol covering instrument checks, recorded variables, stimulus limits, shutdown logic and criteria for rejecting a fitted model. You must distinguish acceptance of a numerical model from approval to operate equipment.

**Problem E — peer challenge.** Argue against a proposed design that optimizes only one metric (such as settling time). Name at least two competing metrics and explain why evidence from the running case might change the preferred design.

## Worked answer path (not a substitute for a full design)

For A, write a block diagram with sensor noise entering the measurement channel and the disturbance entering the correct physical location; this prevents confusion between feedback error and actual tracking error. For B, compute the baseline result, recompute at 1.10 times the chosen parameter, and use sensitivity approximately (Δoutput/output)/(Δparameter/parameter), describing sign and any nonlinear dependence. For C, identify the changed assumption first; do not silently reuse the nominal transfer function. For D, report a test trace and a safety boundary independently. For E, make the tradeoff explicit rather than calling the fastest response automatically best.

## Reflection and next step

Identify the cause of the response, not only the observed waveform. Identify a single observation that would make you question the conclusion about **routh–hurwitz stability screening**. At the end of the lesson record one corrected assumption, one remaining unknown and one measurable next action. The next section extends this reasoning to another part of the control loop; keep the previous model as a baseline for comparison.


---

# U03-L03 — Root locus and gain selection

**Mechanical Engineering · Control Systems Engineering · Unit 3: Stability, Error, and Robustness.**  This is an unreviewed instructional chapter; none of its calculations alone justifies commissioning machinery.

## What you should be able to do

Explain **root locus and gain selection** without confusing measured variables, hidden dynamics and desired behavior; write the main equation and derive its assumptions; reproduce the numerical illustration; diagnose at least two ways the model may mislead; and propose a practical, limited-risk verification experiment.

## Physical interpretation

A root locus tracks closed-loop pole locations as a real scalar gain changes. It begins at open-loop poles and ends at open-loop zeros or infinity under standard assumptions. The characteristic equation supplies the actual result; sketches are diagnostic, not proof.

**System context.** An adjustable-speed drive appears fast in simulation but oscillates with a longer cable and a heavier inertia load. The objective in this lesson is not an abstract good-looking response: Check internal stability before interpreting tracking plots or increasing gains. Establish whether the lesson concerns the plant itself, the mathematical input/output map, an estimator, a controller, or a test method. Those roles cannot be interchanged. A controller parameter may improve the command-response plot and simultaneously create unacceptable actuator current, mechanical strain or sensor-noise transmission.

## Derivation and use

Identify poles, zeros, real-axis branches, asymptotes and breakaway points before choosing gain. Verify candidate gains numerically and check whether unmodeled high-frequency modes are affected.

**Dimensional and sign audit.** Before substituting values, define an input and output in physical units, choose a positive direction, identify zero or equilibrium conditions, and make sure both sides of any differential or algebraic equation have the same dimensions. For root locus and gain selection, changing coordinates or the chosen sensor location can reverse the sign or modify the apparent dynamics. A formula for ideal negative feedback must not be used when actual wiring implements positive feedback. Explicitly distinguish a continuous-time differential equation from a discrete update at sample index k.

## Worked numerical illustration

For 1/(s(s+2)) with gain K, poles solve s²+2s+K=0. At K=1 the poles coincide at −1; for K>1 they are complex with real part −1.

**Reproduction protocol.** Write the givens and units in a table, compute any derived time scales or gains, substitute into the displayed model and calculate the result with more precision than required for the final reported value. Compare against a limiting case: zero disturbance, zero controller gain, vanishing sample time, or a stationary equilibrium as appropriate. If a calculation predicts infinite control force, negative dissipation, or motion through a hard stop, that is an indication to revisit assumptions, not a valid operating instruction.

## What the calculation does not establish

A root locus derived for a nominal zero-delay transfer function may be misleading after adding actuator lag or transport delay.

This limitation matters particularly for **root locus and gain selection**. The simplified example contains no manufacturing tolerances, no equipment-specific safety certification, and no direct evidence about the chosen hardware. Extra physics—sensor lag, actuator limits, cross-coupling, higher modes, friction, temperature drift or sampling delay—must be assessed according to the application. A model can be mathematically stable while the experiment violates the permitted range of current, speed, force or temperature.

## Practical reasoning and validation

1. **Define the measurement.** For this lesson, identify the smallest set of sensors that can distinguish the predicted mechanism from an alternative explanation. Record calibration, range, resolution, sampling rate and timestamps. Do not use commanded actuator signals as though they were measured actuator output.

2. **Plan excitation.** Choose a reversible stimulus small enough to respect the independent safety limits in the case: An adjustable-speed drive appears fast in simulation but oscillates with a longer cable and a heavier inertia load. A step, ramp, chirp, frequency sweep or deliberate small load perturbation may be appropriate, but there is no universal safe test amplitude. Start with the smallest informative test.

3. **Predict first.** Use the selected model to forecast the direction, scale and timing of at least one observation. Include what would refute the prediction. Predictions recorded before an experiment reduce the temptation to tune the story after seeing the result.

4. **Collect independent evidence.** Compare the predicted and measured quantities at more than one operating condition, including a held-out condition not used to fit parameters. Report transients, steady behavior and the actuator command on separate channels. Record uncertainty and do not hide residual patterns by averaging them away.

5. **Revise and document.** If the data disagree, consider model order, omitted delay, calibration bias, nonlinearity or incorrect sign before raising controller gain. Save the model version, parameter ranges, test date, and outstanding safety questions.

## Guided problems

**Problem A — definitions.** Draw the complete signal path for a system that must demonstrate root locus and gain selection. Mark the reference, measured output, actual output, process disturbance and actuator constraint. State which quantities can be directly measured and which must be estimated.

**Problem B — quantitative reproduction.** Rework the example in this lesson using SI units, then change one numerical input by 10%. Report the result and a dimensionless sensitivity ratio. Explain whether a first-order approximation is appropriate.

**Problem C — alternate assumption.** Repeat the reasoning after adding either finite sample time, sensor bias or actuator saturation. Identify precisely which mathematical step is no longer valid and whether the expected effect is on stability, steady-state error or transient response.

**Problem D — experiment design.** Write a one-page safe bench-test protocol covering instrument checks, recorded variables, stimulus limits, shutdown logic and criteria for rejecting a fitted model. You must distinguish acceptance of a numerical model from approval to operate equipment.

**Problem E — peer challenge.** Argue against a proposed design that optimizes only one metric (such as settling time). Name at least two competing metrics and explain why evidence from the running case might change the preferred design.

## Worked answer path (not a substitute for a full design)

For A, write a block diagram with sensor noise entering the measurement channel and the disturbance entering the correct physical location; this prevents confusion between feedback error and actual tracking error. For B, compute the baseline result, recompute at 1.10 times the chosen parameter, and use sensitivity approximately (Δoutput/output)/(Δparameter/parameter), describing sign and any nonlinear dependence. For C, identify the changed assumption first; do not silently reuse the nominal transfer function. For D, report a test trace and a safety boundary independently. For E, make the tradeoff explicit rather than calling the fastest response automatically best.

## Reflection and next step

Keep each parameter attached to its physical units and measured provenance. Identify a single observation that would make you question the conclusion about **root locus and gain selection**. At the end of the lesson record one corrected assumption, one remaining unknown and one measurable next action. The next section extends this reasoning to another part of the control loop; keep the previous model as a baseline for comparison.


---

# U03-L04 — Steady-state error and system type

**Mechanical Engineering · Control Systems Engineering · Unit 3: Stability, Error, and Robustness.**  This is an unreviewed instructional chapter; none of its calculations alone justifies commissioning machinery.

## What you should be able to do

Explain **steady-state error and system type** without confusing measured variables, hidden dynamics and desired behavior; write the main equation and derive its assumptions; reproduce the numerical illustration; diagnose at least two ways the model may mislead; and propose a practical, limited-risk verification experiment.

## Physical interpretation

For unity feedback with loop transfer L(s), step-tracking error can be found with the final value theorem only when its stability conditions hold. A type-0 loop commonly retains a finite step offset; an integrator can remove constant error but creates additional stability and windup concerns.

**System context.** An adjustable-speed drive appears fast in simulation but oscillates with a longer cable and a heavier inertia load. The objective in this lesson is not an abstract good-looking response: Check internal stability before interpreting tracking plots or increasing gains. Establish whether the lesson concerns the plant itself, the mathematical input/output map, an estimator, a controller, or a test method. Those roles cannot be interchanged. A controller parameter may improve the command-response plot and simultaneously create unacceptable actuator current, mechanical strain or sensor-noise transmission.

## Derivation and use

Compute E(s)=R(s)/(1+L(s)) and then e_ss=lim sE(s) for stable closed-loop behavior. Disturbance errors depend on where disturbances enter. The statement “integral action gives zero error” is false when the actuator saturates indefinitely or the loop is unstable.

**Dimensional and sign audit.** Before substituting values, define an input and output in physical units, choose a positive direction, identify zero or equilibrium conditions, and make sure both sides of any differential or algebraic equation have the same dimensions. For steady-state error and system type, changing coordinates or the chosen sensor location can reverse the sign or modify the apparent dynamics. A formula for ideal negative feedback must not be used when actual wiring implements positive feedback. Explicitly distinguish a continuous-time differential equation from a discrete update at sample index k.

## Worked numerical illustration

For G=1/(s+1), C=3 and unity feedback, step reference error tends to 1/(1+3)=0.25. Adding integral action can remove that ideal offset.

**Reproduction protocol.** Write the givens and units in a table, compute any derived time scales or gains, substitute into the displayed model and calculate the result with more precision than required for the final reported value. Compare against a limiting case: zero disturbance, zero controller gain, vanishing sample time, or a stationary equilibrium as appropriate. If a calculation predicts infinite control force, negative dissipation, or motion through a hard stop, that is an indication to revisit assumptions, not a valid operating instruction.

## What the calculation does not establish

Do not apply the final value theorem to an oscillating or unstable response.

This limitation matters particularly for **steady-state error and system type**. The simplified example contains no manufacturing tolerances, no equipment-specific safety certification, and no direct evidence about the chosen hardware. Extra physics—sensor lag, actuator limits, cross-coupling, higher modes, friction, temperature drift or sampling delay—must be assessed according to the application. A model can be mathematically stable while the experiment violates the permitted range of current, speed, force or temperature.

## Practical reasoning and validation

1. **Define the measurement.** For this lesson, identify the smallest set of sensors that can distinguish the predicted mechanism from an alternative explanation. Record calibration, range, resolution, sampling rate and timestamps. Do not use commanded actuator signals as though they were measured actuator output.

2. **Plan excitation.** Choose a reversible stimulus small enough to respect the independent safety limits in the case: An adjustable-speed drive appears fast in simulation but oscillates with a longer cable and a heavier inertia load. A step, ramp, chirp, frequency sweep or deliberate small load perturbation may be appropriate, but there is no universal safe test amplitude. Start with the smallest informative test.

3. **Predict first.** Use the selected model to forecast the direction, scale and timing of at least one observation. Include what would refute the prediction. Predictions recorded before an experiment reduce the temptation to tune the story after seeing the result.

4. **Collect independent evidence.** Compare the predicted and measured quantities at more than one operating condition, including a held-out condition not used to fit parameters. Report transients, steady behavior and the actuator command on separate channels. Record uncertainty and do not hide residual patterns by averaging them away.

5. **Revise and document.** If the data disagree, consider model order, omitted delay, calibration bias, nonlinearity or incorrect sign before raising controller gain. Save the model version, parameter ranges, test date, and outstanding safety questions.

## Guided problems

**Problem A — definitions.** Draw the complete signal path for a system that must demonstrate steady-state error and system type. Mark the reference, measured output, actual output, process disturbance and actuator constraint. State which quantities can be directly measured and which must be estimated.

**Problem B — quantitative reproduction.** Rework the example in this lesson using SI units, then change one numerical input by 10%. Report the result and a dimensionless sensitivity ratio. Explain whether a first-order approximation is appropriate.

**Problem C — alternate assumption.** Repeat the reasoning after adding either finite sample time, sensor bias or actuator saturation. Identify precisely which mathematical step is no longer valid and whether the expected effect is on stability, steady-state error or transient response.

**Problem D — experiment design.** Write a one-page safe bench-test protocol covering instrument checks, recorded variables, stimulus limits, shutdown logic and criteria for rejecting a fitted model. You must distinguish acceptance of a numerical model from approval to operate equipment.

**Problem E — peer challenge.** Argue against a proposed design that optimizes only one metric (such as settling time). Name at least two competing metrics and explain why evidence from the running case might change the preferred design.

## Worked answer path (not a substitute for a full design)

For A, write a block diagram with sensor noise entering the measurement channel and the disturbance entering the correct physical location; this prevents confusion between feedback error and actual tracking error. For B, compute the baseline result, recompute at 1.10 times the chosen parameter, and use sensitivity approximately (Δoutput/output)/(Δparameter/parameter), describing sign and any nonlinear dependence. For C, identify the changed assumption first; do not silently reuse the nominal transfer function. For D, report a test trace and a safety boundary independently. For E, make the tradeoff explicit rather than calling the fastest response automatically best.

## Reflection and next step

Separate the equation derived under assumptions from the test that could challenge it. Identify a single observation that would make you question the conclusion about **steady-state error and system type**. At the end of the lesson record one corrected assumption, one remaining unknown and one measurable next action. The next section extends this reasoning to another part of the control loop; keep the previous model as a baseline for comparison.


---

# U03-L05 — Uncertainty, robustness and actuator limits

**Mechanical Engineering · Control Systems Engineering · Unit 3: Stability, Error, and Robustness.**  This is an unreviewed instructional chapter; none of its calculations alone justifies commissioning machinery.

## What you should be able to do

Explain **uncertainty, robustness and actuator limits** without confusing measured variables, hidden dynamics and desired behavior; write the main equation and derive its assumptions; reproduce the numerical illustration; diagnose at least two ways the model may mislead; and propose a practical, limited-risk verification experiment.

## Physical interpretation

A controller must tolerate parameter drift, neglected modes, sensor noise, delay, output limits and anti-alias filters. Nominal stability is only one check. Sensitivity peaks indicate how disturbances and model errors may be amplified near crossover.

**System context.** An adjustable-speed drive appears fast in simulation but oscillates with a longer cable and a heavier inertia load. The objective in this lesson is not an abstract good-looking response: Check internal stability before interpreting tracking plots or increasing gains. Establish whether the lesson concerns the plant itself, the mathematical input/output map, an estimator, a controller, or a test method. Those roles cannot be interchanged. A controller parameter may improve the command-response plot and simultaneously create unacceptable actuator current, mechanical strain or sensor-noise transmission.

## Derivation and use

Assess at least low/nominal/high plant gain, inertia, delay and sample period. Measure saturation duty cycle, track recovery from disturbances and define safe fallback actions. Distinguish gain margin and phase margin from guarantees of complete nonlinear robustness.

**Dimensional and sign audit.** Before substituting values, define an input and output in physical units, choose a positive direction, identify zero or equilibrium conditions, and make sure both sides of any differential or algebraic equation have the same dimensions. For uncertainty, robustness and actuator limits, changing coordinates or the chosen sensor location can reverse the sign or modify the apparent dynamics. A formula for ideal negative feedback must not be used when actual wiring implements positive feedback. Explicitly distinguish a continuous-time differential equation from a discrete update at sample index k.

## Worked numerical illustration

If a thermal plant gain varies from 1.0 to 1.8°C/% heater due to airflow, a single nominal controller setting may deliver very different overshoot and settling.

**Reproduction protocol.** Write the givens and units in a table, compute any derived time scales or gains, substitute into the displayed model and calculate the result with more precision than required for the final reported value. Compare against a limiting case: zero disturbance, zero controller gain, vanishing sample time, or a stationary equilibrium as appropriate. If a calculation predicts infinite control force, negative dissipation, or motion through a hard stop, that is an indication to revisit assumptions, not a valid operating instruction.

## What the calculation does not establish

Unmodeled unstable dynamics, nonminimum-phase zeros or flexible modes limit what aggressive tuning can safely achieve.

This limitation matters particularly for **uncertainty, robustness and actuator limits**. The simplified example contains no manufacturing tolerances, no equipment-specific safety certification, and no direct evidence about the chosen hardware. Extra physics—sensor lag, actuator limits, cross-coupling, higher modes, friction, temperature drift or sampling delay—must be assessed according to the application. A model can be mathematically stable while the experiment violates the permitted range of current, speed, force or temperature.

## Practical reasoning and validation

1. **Define the measurement.** For this lesson, identify the smallest set of sensors that can distinguish the predicted mechanism from an alternative explanation. Record calibration, range, resolution, sampling rate and timestamps. Do not use commanded actuator signals as though they were measured actuator output.

2. **Plan excitation.** Choose a reversible stimulus small enough to respect the independent safety limits in the case: An adjustable-speed drive appears fast in simulation but oscillates with a longer cable and a heavier inertia load. A step, ramp, chirp, frequency sweep or deliberate small load perturbation may be appropriate, but there is no universal safe test amplitude. Start with the smallest informative test.

3. **Predict first.** Use the selected model to forecast the direction, scale and timing of at least one observation. Include what would refute the prediction. Predictions recorded before an experiment reduce the temptation to tune the story after seeing the result.

4. **Collect independent evidence.** Compare the predicted and measured quantities at more than one operating condition, including a held-out condition not used to fit parameters. Report transients, steady behavior and the actuator command on separate channels. Record uncertainty and do not hide residual patterns by averaging them away.

5. **Revise and document.** If the data disagree, consider model order, omitted delay, calibration bias, nonlinearity or incorrect sign before raising controller gain. Save the model version, parameter ranges, test date, and outstanding safety questions.

## Guided problems

**Problem A — definitions.** Draw the complete signal path for a system that must demonstrate uncertainty, robustness and actuator limits. Mark the reference, measured output, actual output, process disturbance and actuator constraint. State which quantities can be directly measured and which must be estimated.

**Problem B — quantitative reproduction.** Rework the example in this lesson using SI units, then change one numerical input by 10%. Report the result and a dimensionless sensitivity ratio. Explain whether a first-order approximation is appropriate.

**Problem C — alternate assumption.** Repeat the reasoning after adding either finite sample time, sensor bias or actuator saturation. Identify precisely which mathematical step is no longer valid and whether the expected effect is on stability, steady-state error or transient response.

**Problem D — experiment design.** Write a one-page safe bench-test protocol covering instrument checks, recorded variables, stimulus limits, shutdown logic and criteria for rejecting a fitted model. You must distinguish acceptance of a numerical model from approval to operate equipment.

**Problem E — peer challenge.** Argue against a proposed design that optimizes only one metric (such as settling time). Name at least two competing metrics and explain why evidence from the running case might change the preferred design.

## Worked answer path (not a substitute for a full design)

For A, write a block diagram with sensor noise entering the measurement channel and the disturbance entering the correct physical location; this prevents confusion between feedback error and actual tracking error. For B, compute the baseline result, recompute at 1.10 times the chosen parameter, and use sensitivity approximately (Δoutput/output)/(Δparameter/parameter), describing sign and any nonlinear dependence. For C, identify the changed assumption first; do not silently reuse the nominal transfer function. For D, report a test trace and a safety boundary independently. For E, make the tradeoff explicit rather than calling the fastest response automatically best.

## Reflection and next step

Check the controller command and all constrained internal states, not merely the output. Identify a single observation that would make you question the conclusion about **uncertainty, robustness and actuator limits**. At the end of the lesson record one corrected assumption, one remaining unknown and one measurable next action. The next section extends this reasoning to another part of the control loop; keep the previous model as a baseline for comparison.


---

