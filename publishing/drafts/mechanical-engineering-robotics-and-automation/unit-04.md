# Unit 04: Motion Planning and Trajectory Generation

**Course Code**: ROB 404 · **Level**: Advanced Undergraduate Engineering

## Unit Overview & Physical Foundations

This comprehensive university textbook unit covers the theoretical framework, physical modeling, mathematical governing equations, and engineering applications of **Motion Planning and Trajectory Generation**.

# U04-L01 — Path versus trajectory

**OpenSTEM Mechanical Engineering · Book 12: Robotics and Automation · Unit 4: Motion Planning and Trajectory Generation.** Educational draft. All worked numbers are illustrative unless stated otherwise; do not use the calculations alone to certify a physical robot or protective system.

## Learning goal and context

This lesson asks how **path versus trajectory** affects a realistic robotic system. Its running design problem is: The robot transfers packages across a tight workcell without clipping bins. Produce smooth, feasible paths and time laws that respect joints, obstacles, forces and observation latency. Students must explain the physical mechanism, calculate an interpretable quantity, identify an assumption that could fail, and propose an observation that would distinguish competing explanations.

**Entry-level reasoning.** A geometric path specifies poses; a trajectory assigns time to those poses. A collision-free path can still violate torque, acceleration or jerk limits when timed aggressively. Time scaling changes velocity and acceleration but does not remove geometric collisions. In practice, begin with the machine boundary and mark the frames, joint connections, sensing path and source of power. If a controller reports a requested value, determine whether the value is a command, a filtered estimate, an independently measured result or an offline ideal prediction. These are not interchangeable. Write a short claim that would be falsified by an observed counterexample, rather than a claim that can be rescued by changing assumptions after the experiment.

## Derivation, model and interpretation

A compact starting equation or relationship is **`v = ds/dt`**. Define every symbol, include appropriate physical units and interpret the input and output quantities. The displayed relationship may be exact within an ideal geometry, a simplification of more complete dynamics, or a statistical approximation. Its status must be recorded. When the formula requires constant dimensions or a fixed reference frame, note these conditions explicitly. A coordinate-dependent result is meaningless until frame orientation and origin are identified.

**Implementation choice.** The lightest controller or cheapest sensor is not automatically the best solution. Complexity can improve diagnostics yet add failure modes and maintenance obligations. Define what a more advanced method would need to prove under representative loads, timing, environment and budget. In this lesson, look specifically at **path versus trajectory** rather than copying a generic control diagram. Ask which model terms could be measured directly. For each unmeasured quantity, give a method for identification and state what additional assumptions that method requires.

**Submodel and system boundary.** Time parameterization Distinguish the ideal mathematical transformation from the mechanical or software device implementing it. For example, a calculated path requires a motion executor, a sensor-based termination rule and an independently assessed response to loss of communication. A fully specified algorithm can still be unsuitable for hardware when the necessary observations arrive too late.

## Worked calculation and numerical judgment

A 0.60 m path traversed in 1.5 s has average path speed 0.40 m/s, not necessarily constant Cartesian velocity. Reproduce the substitution on paper, carry units through each stage and check the scale with an independent estimate. Precision in displayed decimal places does not demonstrate precise knowledge of link lengths, accelerations, friction coefficients or camera calibration. If inputs are rounded or synthetic, the outputs inherit those limitations; do not label them as measured robot performance.

**Dimensional Balance audit.** Perform a units check by substituting SI base units and showing both sides match. For angles, state that trigonometric functions expect radians unless explicitly converted. For probabilities, check output within [0,1], and for lengths or times reject negative values when the model defines only positive quantities. Extend the example by sweeping one independent input through a realistic range. Predict the qualitative trend before computing. Then change another input in a separate run; explain why changing both simultaneously would make causal interpretation weaker. Document any singular, discontinuous or saturating regime instead of hiding it by clipping a plot without explanation.

## Engineering interpretation and practical alternatives

The principal design trade-off is between algorithmic or mechanical capability and the evidence needed to operate it reliably. A high-speed option may increase throughput but increase motor heating and the consequence of a delayed stop. A sophisticated estimator may reduce drift under good lighting but fail abruptly when landmarks disappear. A carefully bounded simpler system can therefore outperform a more elaborate system under the actual operating conditions.

**Specific failure mechanism.** A robot is approved using joint-angle waypoints without checking swept volume between them. Do not respond automatically by increasing controller gain or changing a threshold. State what instrument or independent observation would reveal the difference between a bad model, incorrect calibration, measurement delay and a mechanical fault. Consider the consequences for neighboring subsystems: sensing errors affect grasp decisions, trajectory errors affect collision risk, and recovery behavior affects throughput.

**Integration perspective.** Check both geometry and time. Velocity is the first derivative of path, acceleration its second derivative and jerk its third; short paths can be acceleration-limited rather than velocity-limited. Replanning must preserve already guaranteed mechanical constraints. For this topic, explicitly identify the preceding system function that supplies information and the following function that consumes the output. Give those interfaces names and units. State whether data is real time, sampled, batch-produced or only available after an operation ends. Wrong timing semantics can invalidate a mathematically correct equation.

## Verification protocol and evidence quality

A falsifiable check is: **Interpolate densely along every segment and run independent swept-volume interference checks.** Establish independent observations whenever practical. Define an input range, number of trials, logging rate, expected trend, calibration reference and an acceptance threshold selected before analysis. At minimum include a nominal trial, a limiting case and an innocuous fault or missing-data condition. Physically hazardous failure injection requires qualified supervision and appropriate containment; otherwise conduct the test virtually and describe that limitation.

**Failure analysis.** Controllers can track simulated paths while real mechanics exceed torque limits or excite flexible resonances. Record actual following error and motor current rather than judging only smooth plots. When recorded evidence contradicts a prediction, preserve the discrepancy. Consider sensor bias, frame mismatch, uncontrolled load, aliasing, model order, compliance and operator intervention as competing explanations. One favorable trace does not validate a complete operating envelope. A reliable result needs repeatability across changed initial conditions and traceability to the configuration used for the test.

**Laboratory record.** Save model revision, input parameter table, raw data, units, frame definitions, timestamps, plot-generating script, calculated sensitivity and unsuccessful cases. Attach a short statement distinguishing simulation evidence from physical measurement and from a safety-related assessment. If equipment access is unavailable, provide a transparent synthetic test with expected results and avoid representing it as laboratory measurement.

## Exercises and design investigation

1. **Interpretation:** Derive or explain `v = ds/dt` from relevant geometry, conservation laws or probability assumptions. Define all quantities, directions and units. Name a realistic boundary where it loses validity.
2. **Calculation:** Recompute the worked example without copying its result. Change the most important input by 10%; compare the resulting change against the original prediction, and explain when a first-order approximation is inadequate.
3. **Independent validation:** Construct a test of path versus trajectory using an independent reference. State three potential sources of measurement error and which observable can isolate at least two of them.
4. **Failure and safety:** Using the specified failure mechanism, write an expected fault signature, a detection threshold and a controlled fallback response. Distinguish the operating controller from a separately evaluated safety function.
5. **Applied synthesis:** For the unit's running case, document one viable alternative architecture, what it costs in complexity, and what evidence would justify choosing it over the baseline.

## Lesson summary and transfer

The central skill is to connect **path versus trajectory** to a physically meaningful model and a test that could disprove it. Carry the same units, coordinate conventions, uncertainty bounds and versioned acceptance criteria into the next lesson. Robot performance is judged by reproducible task outcomes under constrained conditions, not by an appealing ideal plot or the correctness of a single formula.


---

# U04-L02 — Trapezoidal and triangular velocity profiles

**OpenSTEM Mechanical Engineering · Book 12: Robotics and Automation · Unit 4: Motion Planning and Trajectory Generation.** Educational draft. All worked numbers are illustrative unless stated otherwise; do not use the calculations alone to certify a physical robot or protective system.

## Learning goal and context

This lesson asks how **trapezoidal and triangular velocity profiles** affects a realistic robotic system. Its running design problem is: The robot transfers packages across a tight workcell without clipping bins. Produce smooth, feasible paths and time laws that respect joints, obstacles, forces and observation latency. Students must explain the physical mechanism, calculate an interpretable quantity, identify an assumption that could fail, and propose an observation that would distinguish competing explanations.

**Entry-level reasoning.** For rest-to-rest one-dimensional travel with speed cap vmax and acceleration cap a, a triangular profile occurs when the travel distance is too short to attain vmax. The minimum ideal time depends on this branch condition. In practice, begin with the machine boundary and mark the frames, joint connections, sensing path and source of power. If a controller reports a requested value, determine whether the value is a command, a filtered estimate, an independently measured result or an offline ideal prediction. These are not interchangeable. Write a short claim that would be falsified by an observed counterexample, rather than a claim that can be rescued by changing assumptions after the experiment.

## Derivation, model and interpretation

A compact starting equation or relationship is **`t=2*sqrt(d/a) if d<=vmax^2/a else d/vmax+vmax/a`**. Define every symbol, include appropriate physical units and interpret the input and output quantities. The displayed relationship may be exact within an ideal geometry, a simplification of more complete dynamics, or a statistical approximation. Its status must be recorded. When the formula requires constant dimensions or a fixed reference frame, note these conditions explicitly. A coordinate-dependent result is meaningless until frame orientation and origin are identified.

**Operational consequence.** A robot cell has no isolated subsystem outcomes. A high-accuracy reach solution can be invalidated by perception latency, a good gripper can fail on a different surface, and a fast conveyor can overwhelm fault handling. Preserve interface specifications and model uncertainty across design stages. In this lesson, look specifically at **trapezoidal and triangular velocity profiles** rather than copying a generic control diagram. Ask which model terms could be measured directly. For each unmeasured quantity, give a method for identification and state what additional assumptions that method requires.

**Submodel and system boundary.** Time parameterization Distinguish the ideal mathematical transformation from the mechanical or software device implementing it. For example, a calculated path requires a motion executor, a sensor-based termination rule and an independently assessed response to loss of communication. A fully specified algorithm can still be unsuitable for hardware when the necessary observations arrive too late.

## Worked calculation and numerical judgment

For d=0.20 m, a=1 m/s² and vmax=1 m/s, the triangular profile takes about 0.894 s. Reproduce the substitution on paper, carry units through each stage and check the scale with an independent estimate. Precision in displayed decimal places does not demonstrate precise knowledge of link lengths, accelerations, friction coefficients or camera calibration. If inputs are rounded or synthetic, the outputs inherit those limitations; do not label them as measured robot performance.

**Boundary Cases audit.** Check a zero-input limit, a typical operating point and a maximum planned input. Where derivatives exist, estimate local sensitivity to a 5% change. If the result changes sharply, prioritize a measurement of the sensitive parameter rather than increasing numerical precision elsewhere. Extend the example by sweeping one independent input through a realistic range. Predict the qualitative trend before computing. Then change another input in a separate run; explain why changing both simultaneously would make causal interpretation weaker. Document any singular, discontinuous or saturating regime instead of hiding it by clipping a plot without explanation.

## Engineering interpretation and practical alternatives

The principal design trade-off is between algorithmic or mechanical capability and the evidence needed to operate it reliably. A high-speed option may increase throughput but increase motor heating and the consequence of a delayed stop. A sophisticated estimator may reduce drift under good lighting but fail abruptly when landmarks disappear. A carefully bounded simpler system can therefore outperform a more elaborate system under the actual operating conditions.

**Specific failure mechanism.** Applying the trapezoidal formula to a short move predicts an impossible cruising segment. Do not respond automatically by increasing controller gain or changing a threshold. State what instrument or independent observation would reveal the difference between a bad model, incorrect calibration, measurement delay and a mechanical fault. Consider the consequences for neighboring subsystems: sensing errors affect grasp decisions, trajectory errors affect collision risk, and recovery behavior affects throughput.

**Integration perspective.** Check both geometry and time. Velocity is the first derivative of path, acceleration its second derivative and jerk its third; short paths can be acceleration-limited rather than velocity-limited. Replanning must preserve already guaranteed mechanical constraints. For this topic, explicitly identify the preceding system function that supplies information and the following function that consumes the output. Give those interfaces names and units. State whether data is real time, sampled, batch-produced or only available after an operation ends. Wrong timing semantics can invalidate a mathematically correct equation.

## Verification protocol and evidence quality

A falsifiable check is: **Log commanded and measured velocity, marking the acceleration boundary and saturation.** Establish independent observations whenever practical. Define an input range, number of trials, logging rate, expected trend, calibration reference and an acceptance threshold selected before analysis. At minimum include a nominal trial, a limiting case and an innocuous fault or missing-data condition. Physically hazardous failure injection requires qualified supervision and appropriate containment; otherwise conduct the test virtually and describe that limitation.

**Failure analysis.** Controllers can track simulated paths while real mechanics exceed torque limits or excite flexible resonances. Record actual following error and motor current rather than judging only smooth plots. When recorded evidence contradicts a prediction, preserve the discrepancy. Consider sensor bias, frame mismatch, uncontrolled load, aliasing, model order, compliance and operator intervention as competing explanations. One favorable trace does not validate a complete operating envelope. A reliable result needs repeatability across changed initial conditions and traceability to the configuration used for the test.

**Laboratory record.** Save model revision, input parameter table, raw data, units, frame definitions, timestamps, plot-generating script, calculated sensitivity and unsuccessful cases. Attach a short statement distinguishing simulation evidence from physical measurement and from a safety-related assessment. If equipment access is unavailable, provide a transparent synthetic test with expected results and avoid representing it as laboratory measurement.

## Exercises and design investigation

1. **Interpretation:** Derive or explain `t=2*sqrt(d/a) if d<=vmax^2/a else d/vmax+vmax/a` from relevant geometry, conservation laws or probability assumptions. Define all quantities, directions and units. Name a realistic boundary where it loses validity.
2. **Calculation:** Recompute the worked example without copying its result. Change the most important input by 10%; compare the resulting change against the original prediction, and explain when a first-order approximation is inadequate.
3. **Independent validation:** Construct a test of trapezoidal and triangular velocity profiles using an independent reference. State three potential sources of measurement error and which observable can isolate at least two of them.
4. **Failure and safety:** Using the specified failure mechanism, write an expected fault signature, a detection threshold and a controlled fallback response. Distinguish the operating controller from a separately evaluated safety function.
5. **Applied synthesis:** For the unit's running case, document one viable alternative architecture, what it costs in complexity, and what evidence would justify choosing it over the baseline.

## Lesson summary and transfer

The central skill is to connect **trapezoidal and triangular velocity profiles** to a physically meaningful model and a test that could disprove it. Carry the same units, coordinate conventions, uncertainty bounds and versioned acceptance criteria into the next lesson. Robot performance is judged by reproducible task outcomes under constrained conditions, not by an appealing ideal plot or the correctness of a single formula.


---

# U04-L03 — Jerk-limited motion profiles

**OpenSTEM Mechanical Engineering · Book 12: Robotics and Automation · Unit 4: Motion Planning and Trajectory Generation.** Educational draft. All worked numbers are illustrative unless stated otherwise; do not use the calculations alone to certify a physical robot or protective system.

## Learning goal and context

This lesson asks how **jerk-limited motion profiles** affects a realistic robotic system. Its running design problem is: The robot transfers packages across a tight workcell without clipping bins. Produce smooth, feasible paths and time laws that respect joints, obstacles, forces and observation latency. Students must explain the physical mechanism, calculate an interpretable quantity, identify an assumption that could fail, and propose an observation that would distinguish competing explanations.

**Entry-level reasoning.** Jerk is time derivative of acceleration; bounded jerk reduces abrupt torque demands and excitation of flexible mechanisms. For a smooth fifth-order polynomial, position, velocity and acceleration can be zero at the endpoints, but peak values depend on the chosen duration. In practice, begin with the machine boundary and mark the frames, joint connections, sensing path and source of power. If a controller reports a requested value, determine whether the value is a command, a filtered estimate, an independently measured result or an offline ideal prediction. These are not interchangeable. Write a short claim that would be falsified by an observed counterexample, rather than a claim that can be rescued by changing assumptions after the experiment.

## Derivation, model and interpretation

A compact starting equation or relationship is **`j = d(a)/dt`**. Define every symbol, include appropriate physical units and interpret the input and output quantities. The displayed relationship may be exact within an ideal geometry, a simplification of more complete dynamics, or a statistical approximation. Its status must be recorded. When the formula requires constant dimensions or a fixed reference frame, note these conditions explicitly. A coordinate-dependent result is meaningless until frame orientation and origin are identified.

**Physical interpretation.** Place the governing relationship beside a sketch with vectors, directions and units. Identify which terms are geometry, which describe dynamics, and which are sensor-derived approximations. The useful question is not simply whether software returns a number, but whether the quantity corresponds to a well-defined physical observation. In this lesson, look specifically at **jerk-limited motion profiles** rather than copying a generic control diagram. Ask which model terms could be measured directly. For each unmeasured quantity, give a method for identification and state what additional assumptions that method requires.

**Submodel and system boundary.** Time parameterization Distinguish the ideal mathematical transformation from the mechanical or software device implementing it. For example, a calculated path requires a motion executor, a sensor-based termination rule and an independently assessed response to loss of communication. A fully specified algorithm can still be unsuitable for hardware when the necessary observations arrive too late.

## Worked calculation and numerical judgment

Changing acceleration from 0 to 2 m/s² over 0.20 s gives mean jerk magnitude 10 m/s³ under a linear ramp. Reproduce the substitution on paper, carry units through each stage and check the scale with an independent estimate. Precision in displayed decimal places does not demonstrate precise knowledge of link lengths, accelerations, friction coefficients or camera calibration. If inputs are rounded or synthetic, the outputs inherit those limitations; do not label them as measured robot performance.

**Discretization audit.** Choose a simulation step that resolves the fastest physical phenomenon of interest. Check convergence with a smaller step and confirm that numerical artifacts do not explain apparent stability or contact behavior. Sampling rates must exceed the bandwidth of the phenomena they are claimed to detect. Extend the example by sweeping one independent input through a realistic range. Predict the qualitative trend before computing. Then change another input in a separate run; explain why changing both simultaneously would make causal interpretation weaker. Document any singular, discontinuous or saturating regime instead of hiding it by clipping a plot without explanation.

## Engineering interpretation and practical alternatives

The principal design trade-off is between algorithmic or mechanical capability and the evidence needed to operate it reliably. A high-speed option may increase throughput but increase motor heating and the consequence of a delayed stop. A sophisticated estimator may reduce drift under good lighting but fail abruptly when landmarks disappear. A carefully bounded simpler system can therefore outperform a more elaborate system under the actual operating conditions.

**Specific failure mechanism.** A low nominal acceleration trajectory contains discontinuous changes that excite vibration. Do not respond automatically by increasing controller gain or changing a threshold. State what instrument or independent observation would reveal the difference between a bad model, incorrect calibration, measurement delay and a mechanical fault. Consider the consequences for neighboring subsystems: sensing errors affect grasp decisions, trajectory errors affect collision risk, and recovery behavior affects throughput.

**Integration perspective.** Check both geometry and time. Velocity is the first derivative of path, acceleration its second derivative and jerk its third; short paths can be acceleration-limited rather than velocity-limited. Replanning must preserve already guaranteed mechanical constraints. For this topic, explicitly identify the preceding system function that supplies information and the following function that consumes the output. Give those interfaces names and units. State whether data is real time, sampled, batch-produced or only available after an operation ends. Wrong timing semantics can invalidate a mathematically correct equation.

## Verification protocol and evidence quality

A falsifiable check is: **Compare power spectrum, peak following error and settling time for trapezoidal and jerk-limited commands.** Establish independent observations whenever practical. Define an input range, number of trials, logging rate, expected trend, calibration reference and an acceptance threshold selected before analysis. At minimum include a nominal trial, a limiting case and an innocuous fault or missing-data condition. Physically hazardous failure injection requires qualified supervision and appropriate containment; otherwise conduct the test virtually and describe that limitation.

**Failure analysis.** Controllers can track simulated paths while real mechanics exceed torque limits or excite flexible resonances. Record actual following error and motor current rather than judging only smooth plots. When recorded evidence contradicts a prediction, preserve the discrepancy. Consider sensor bias, frame mismatch, uncontrolled load, aliasing, model order, compliance and operator intervention as competing explanations. One favorable trace does not validate a complete operating envelope. A reliable result needs repeatability across changed initial conditions and traceability to the configuration used for the test.

**Laboratory record.** Save model revision, input parameter table, raw data, units, frame definitions, timestamps, plot-generating script, calculated sensitivity and unsuccessful cases. Attach a short statement distinguishing simulation evidence from physical measurement and from a safety-related assessment. If equipment access is unavailable, provide a transparent synthetic test with expected results and avoid representing it as laboratory measurement.

## Exercises and design investigation

1. **Interpretation:** Derive or explain `j = d(a)/dt` from relevant geometry, conservation laws or probability assumptions. Define all quantities, directions and units. Name a realistic boundary where it loses validity.
2. **Calculation:** Recompute the worked example without copying its result. Change the most important input by 10%; compare the resulting change against the original prediction, and explain when a first-order approximation is inadequate.
3. **Independent validation:** Construct a test of jerk-limited motion profiles using an independent reference. State three potential sources of measurement error and which observable can isolate at least two of them.
4. **Failure and safety:** Using the specified failure mechanism, write an expected fault signature, a detection threshold and a controlled fallback response. Distinguish the operating controller from a separately evaluated safety function.
5. **Applied synthesis:** For the unit's running case, document one viable alternative architecture, what it costs in complexity, and what evidence would justify choosing it over the baseline.

## Lesson summary and transfer

The central skill is to connect **jerk-limited motion profiles** to a physically meaningful model and a test that could disprove it. Carry the same units, coordinate conventions, uncertainty bounds and versioned acceptance criteria into the next lesson. Robot performance is judged by reproducible task outcomes under constrained conditions, not by an appealing ideal plot or the correctness of a single formula.


---

# U04-L04 — Joint-space and Cartesian interpolation

**OpenSTEM Mechanical Engineering · Book 12: Robotics and Automation · Unit 4: Motion Planning and Trajectory Generation.** Educational draft. All worked numbers are illustrative unless stated otherwise; do not use the calculations alone to certify a physical robot or protective system.

## Learning goal and context

This lesson asks how **joint-space and cartesian interpolation** affects a realistic robotic system. Its running design problem is: The robot transfers packages across a tight workcell without clipping bins. Produce smooth, feasible paths and time laws that respect joints, obstacles, forces and observation latency. Students must explain the physical mechanism, calculate an interpretable quantity, identify an assumption that could fail, and propose an observation that would distinguish competing explanations.

**Entry-level reasoning.** Linear interpolation of joint angles does not generally trace a straight Cartesian line. Conversely, linear Cartesian motion may require nonlinear joint trajectories, and singularities complicate speed tracking. Choose the space according to the task constraint. In practice, begin with the machine boundary and mark the frames, joint connections, sensing path and source of power. If a controller reports a requested value, determine whether the value is a command, a filtered estimate, an independently measured result or an offline ideal prediction. These are not interchangeable. Write a short claim that would be falsified by an observed counterexample, rather than a claim that can be rescued by changing assumptions after the experiment.

## Derivation, model and interpretation

A compact starting equation or relationship is **`q(s)=(1-s)*q0+s*q1`**. Define every symbol, include appropriate physical units and interpret the input and output quantities. The displayed relationship may be exact within an ideal geometry, a simplification of more complete dynamics, or a statistical approximation. Its status must be recorded. When the formula requires constant dimensions or a fixed reference frame, note these conditions explicitly. A coordinate-dependent result is meaningless until frame orientation and origin are identified.

**Failure boundaries.** Derive a nominal prediction, then ask how it changes near a singularity, saturation threshold, sensor outage or geometric boundary. Mathematical formulas sometimes remain numerically defined after their physical hypotheses are violated. The validity envelope should be written before any plot is treated as a performance forecast. In this lesson, look specifically at **joint-space and cartesian interpolation** rather than copying a generic control diagram. Ask which model terms could be measured directly. For each unmeasured quantity, give a method for identification and state what additional assumptions that method requires.

**Submodel and system boundary.** Time parameterization Distinguish the ideal mathematical transformation from the mechanical or software device implementing it. For example, a calculated path requires a motion executor, a sensor-based termination rule and an independently assessed response to loss of communication. A fully specified algorithm can still be unsuitable for hardware when the necessary observations arrive too late.

## Worked calculation and numerical judgment

At s=0.25 between 20° and 60°, a single interpolated joint is 30°; intermediate tool positions depend on all other joints. Reproduce the substitution on paper, carry units through each stage and check the scale with an independent estimate. Precision in displayed decimal places does not demonstrate precise knowledge of link lengths, accelerations, friction coefficients or camera calibration. If inputs are rounded or synthetic, the outputs inherit those limitations; do not label them as measured robot performance.

**Uncertainty audit.** Differentiate precision from accuracy: repeated values near one another may share a systematic offset. Use replicated trials and a calibration reference, and consider correlations when combining uncertainties. An error bound must be linked to a defined operating range. Extend the example by sweeping one independent input through a realistic range. Predict the qualitative trend before computing. Then change another input in a separate run; explain why changing both simultaneously would make causal interpretation weaker. Document any singular, discontinuous or saturating regime instead of hiding it by clipping a plot without explanation.

## Engineering interpretation and practical alternatives

The principal design trade-off is between algorithmic or mechanical capability and the evidence needed to operate it reliably. A high-speed option may increase throughput but increase motor heating and the consequence of a delayed stop. A sophisticated estimator may reduce drift under good lighting but fail abruptly when landmarks disappear. A carefully bounded simpler system can therefore outperform a more elaborate system under the actual operating conditions.

**Specific failure mechanism.** A straight-looking joint command scrapes the tool along a fixture during insertion. Do not respond automatically by increasing controller gain or changing a threshold. State what instrument or independent observation would reveal the difference between a bad model, incorrect calibration, measurement delay and a mechanical fault. Consider the consequences for neighboring subsystems: sensing errors affect grasp decisions, trajectory errors affect collision risk, and recovery behavior affects throughput.

**Integration perspective.** Check both geometry and time. Velocity is the first derivative of path, acceleration its second derivative and jerk its third; short paths can be acceleration-limited rather than velocity-limited. Replanning must preserve already guaranteed mechanical constraints. For this topic, explicitly identify the preceding system function that supplies information and the following function that consumes the output. Give those interfaces names and units. State whether data is real time, sampled, batch-produced or only available after an operation ends. Wrong timing semantics can invalidate a mathematically correct equation.

## Verification protocol and evidence quality

A falsifiable check is: **Plot Cartesian tip coordinates and obstacle distance for densely sampled interpolation paths.** Establish independent observations whenever practical. Define an input range, number of trials, logging rate, expected trend, calibration reference and an acceptance threshold selected before analysis. At minimum include a nominal trial, a limiting case and an innocuous fault or missing-data condition. Physically hazardous failure injection requires qualified supervision and appropriate containment; otherwise conduct the test virtually and describe that limitation.

**Failure analysis.** Controllers can track simulated paths while real mechanics exceed torque limits or excite flexible resonances. Record actual following error and motor current rather than judging only smooth plots. When recorded evidence contradicts a prediction, preserve the discrepancy. Consider sensor bias, frame mismatch, uncontrolled load, aliasing, model order, compliance and operator intervention as competing explanations. One favorable trace does not validate a complete operating envelope. A reliable result needs repeatability across changed initial conditions and traceability to the configuration used for the test.

**Laboratory record.** Save model revision, input parameter table, raw data, units, frame definitions, timestamps, plot-generating script, calculated sensitivity and unsuccessful cases. Attach a short statement distinguishing simulation evidence from physical measurement and from a safety-related assessment. If equipment access is unavailable, provide a transparent synthetic test with expected results and avoid representing it as laboratory measurement.

## Exercises and design investigation

1. **Interpretation:** Derive or explain `q(s)=(1-s)*q0+s*q1` from relevant geometry, conservation laws or probability assumptions. Define all quantities, directions and units. Name a realistic boundary where it loses validity.
2. **Calculation:** Recompute the worked example without copying its result. Change the most important input by 10%; compare the resulting change against the original prediction, and explain when a first-order approximation is inadequate.
3. **Independent validation:** Construct a test of joint-space and cartesian interpolation using an independent reference. State three potential sources of measurement error and which observable can isolate at least two of them.
4. **Failure and safety:** Using the specified failure mechanism, write an expected fault signature, a detection threshold and a controlled fallback response. Distinguish the operating controller from a separately evaluated safety function.
5. **Applied synthesis:** For the unit's running case, document one viable alternative architecture, what it costs in complexity, and what evidence would justify choosing it over the baseline.

## Lesson summary and transfer

The central skill is to connect **joint-space and cartesian interpolation** to a physically meaningful model and a test that could disprove it. Carry the same units, coordinate conventions, uncertainty bounds and versioned acceptance criteria into the next lesson. Robot performance is judged by reproducible task outcomes under constrained conditions, not by an appealing ideal plot or the correctness of a single formula.


---

# U04-L05 — Collision checking and replanning

**OpenSTEM Mechanical Engineering · Book 12: Robotics and Automation · Unit 4: Motion Planning and Trajectory Generation.** Educational draft. All worked numbers are illustrative unless stated otherwise; do not use the calculations alone to certify a physical robot or protective system.

## Learning goal and context

This lesson asks how **collision checking and replanning** affects a realistic robotic system. Its running design problem is: The robot transfers packages across a tight workcell without clipping bins. Produce smooth, feasible paths and time laws that respect joints, obstacles, forces and observation latency. Students must explain the physical mechanism, calculate an interpretable quantity, identify an assumption that could fail, and propose an observation that would distinguish competing explanations.

**Entry-level reasoning.** Obstacle representations include bounding volumes, grids, signed distance fields and exact meshes. Conservative collision margins must cover model and sensing uncertainty. Replanning needs defined latency bounds and a safe fallback when no feasible path remains. In practice, begin with the machine boundary and mark the frames, joint connections, sensing path and source of power. If a controller reports a requested value, determine whether the value is a command, a filtered estimate, an independently measured result or an offline ideal prediction. These are not interchangeable. Write a short claim that would be falsified by an observed counterexample, rather than a claim that can be rescued by changing assumptions after the experiment.

## Derivation, model and interpretation

A compact starting equation or relationship is **`clearance_effective=clearance_geometric-margin`**. Define every symbol, include appropriate physical units and interpret the input and output quantities. The displayed relationship may be exact within an ideal geometry, a simplification of more complete dynamics, or a statistical approximation. Its status must be recorded. When the formula requires constant dimensions or a fixed reference frame, note these conditions explicitly. A coordinate-dependent result is meaningless until frame orientation and origin are identified.

**Identification and calibration.** A single fitted parameter can conceal bias in a different component. If friction, encoder scale and controller gain all change together, the resulting trace does not identify their separate causes. Change a controlled input and compare with an independent instrument where possible. In this lesson, look specifically at **collision checking and replanning** rather than copying a generic control diagram. Ask which model terms could be measured directly. For each unmeasured quantity, give a method for identification and state what additional assumptions that method requires.

**Submodel and system boundary.** Time parameterization Distinguish the ideal mathematical transformation from the mechanical or software device implementing it. For example, a calculated path requires a motion executor, a sensor-based termination rule and an independently assessed response to loss of communication. A fully specified algorithm can still be unsuitable for hardware when the necessary observations arrive too late.

## Worked calculation and numerical judgment

With predicted clearance 15 mm and combined safety margin 7 mm, the remaining modeled clearance is 8 mm, subject to calibration validity. Reproduce the substitution on paper, carry units through each stage and check the scale with an independent estimate. Precision in displayed decimal places does not demonstrate precise knowledge of link lengths, accelerations, friction coefficients or camera calibration. If inputs are rounded or synthetic, the outputs inherit those limitations; do not label them as measured robot performance.

**Traceable Verification audit.** Record firmware or model version, sensor calibration, test fixture revision and all rejected trials. Set acceptance thresholds before viewing the final traces. If a physical trial cannot be carried out safely, use simulation only and write the missing validation item explicitly. Extend the example by sweeping one independent input through a realistic range. Predict the qualitative trend before computing. Then change another input in a separate run; explain why changing both simultaneously would make causal interpretation weaker. Document any singular, discontinuous or saturating regime instead of hiding it by clipping a plot without explanation.

## Engineering interpretation and practical alternatives

The principal design trade-off is between algorithmic or mechanical capability and the evidence needed to operate it reliably. A high-speed option may increase throughput but increase motor heating and the consequence of a delayed stop. A sophisticated estimator may reduce drift under good lighting but fail abruptly when landmarks disappear. A carefully bounded simpler system can therefore outperform a more elaborate system under the actual operating conditions.

**Specific failure mechanism.** A planner reports clearance to an outdated obstacle pose. Do not respond automatically by increasing controller gain or changing a threshold. State what instrument or independent observation would reveal the difference between a bad model, incorrect calibration, measurement delay and a mechanical fault. Consider the consequences for neighboring subsystems: sensing errors affect grasp decisions, trajectory errors affect collision risk, and recovery behavior affects throughput.

**Integration perspective.** Check both geometry and time. Velocity is the first derivative of path, acceleration its second derivative and jerk its third; short paths can be acceleration-limited rather than velocity-limited. Replanning must preserve already guaranteed mechanical constraints. For this topic, explicitly identify the preceding system function that supplies information and the following function that consumes the output. Give those interfaces names and units. State whether data is real time, sampled, batch-produced or only available after an operation ends. Wrong timing semantics can invalidate a mathematically correct equation.

## Verification protocol and evidence quality

A falsifiable check is: **Recheck obstacle timestamp, geometry revision and clearance on a withheld set of trajectories.** Establish independent observations whenever practical. Define an input range, number of trials, logging rate, expected trend, calibration reference and an acceptance threshold selected before analysis. At minimum include a nominal trial, a limiting case and an innocuous fault or missing-data condition. Physically hazardous failure injection requires qualified supervision and appropriate containment; otherwise conduct the test virtually and describe that limitation.

**Failure analysis.** Controllers can track simulated paths while real mechanics exceed torque limits or excite flexible resonances. Record actual following error and motor current rather than judging only smooth plots. When recorded evidence contradicts a prediction, preserve the discrepancy. Consider sensor bias, frame mismatch, uncontrolled load, aliasing, model order, compliance and operator intervention as competing explanations. One favorable trace does not validate a complete operating envelope. A reliable result needs repeatability across changed initial conditions and traceability to the configuration used for the test.

**Laboratory record.** Save model revision, input parameter table, raw data, units, frame definitions, timestamps, plot-generating script, calculated sensitivity and unsuccessful cases. Attach a short statement distinguishing simulation evidence from physical measurement and from a safety-related assessment. If equipment access is unavailable, provide a transparent synthetic test with expected results and avoid representing it as laboratory measurement.

## Exercises and design investigation

1. **Interpretation:** Derive or explain `clearance_effective=clearance_geometric-margin` from relevant geometry, conservation laws or probability assumptions. Define all quantities, directions and units. Name a realistic boundary where it loses validity.
2. **Calculation:** Recompute the worked example without copying its result. Change the most important input by 10%; compare the resulting change against the original prediction, and explain when a first-order approximation is inadequate.
3. **Independent validation:** Construct a test of collision checking and replanning using an independent reference. State three potential sources of measurement error and which observable can isolate at least two of them.
4. **Failure and safety:** Using the specified failure mechanism, write an expected fault signature, a detection threshold and a controlled fallback response. Distinguish the operating controller from a separately evaluated safety function.
5. **Applied synthesis:** For the unit's running case, document one viable alternative architecture, what it costs in complexity, and what evidence would justify choosing it over the baseline.

## Lesson summary and transfer

The central skill is to connect **collision checking and replanning** to a physically meaningful model and a test that could disprove it. Carry the same units, coordinate conventions, uncertainty bounds and versioned acceptance criteria into the next lesson. Robot performance is judged by reproducible task outcomes under constrained conditions, not by an appealing ideal plot or the correctness of a single formula.


---

