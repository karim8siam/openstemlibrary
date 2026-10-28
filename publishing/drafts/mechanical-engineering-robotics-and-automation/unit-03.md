# Unit 03: Robot Dynamics, Actuation and Contacts

**Course Code**: ROB 403 · **Level**: Advanced Undergraduate Engineering

## Unit Overview & Physical Foundations

This comprehensive university textbook unit covers the theoretical framework, physical modeling, mathematical governing equations, and engineering applications of **Robot Dynamics, Actuation and Contacts**.

# U03-L01 — Newton–Euler balance for links

**OpenSTEM Mechanical Engineering · Book 12: Robotics and Automation · Unit 3: Robot Dynamics, Actuation and Contacts.** Educational draft. All worked numbers are illustrative unless stated otherwise; do not use the calculations alone to certify a physical robot or protective system.

## Learning goal and context

This lesson asks how **newton–euler balance for links** affects a realistic robotic system. Its running design problem is: A small arm repeatedly lifts and positions a 1.5 kg payload. Connect joint motion and contacts to mass, inertia, gravity, friction, actuator limits and thermal constraints. Students must explain the physical mechanism, calculate an interpretable quantity, identify an assumption that could fail, and propose an observation that would distinguish competing explanations.

**Entry-level reasoning.** Link mass, angular momentum, force transmission and center-of-mass geometry determine joint load. Recursive Newton–Euler reasoning sums transmitted wrenches, while simplified free-body models can expose sign errors before coding full multibody dynamics. In practice, begin with the machine boundary and mark the frames, joint connections, sensing path and source of power. If a controller reports a requested value, determine whether the value is a command, a filtered estimate, an independently measured result or an offline ideal prediction. These are not interchangeable. Write a short claim that would be falsified by an observed counterexample, rather than a claim that can be rescued by changing assumptions after the experiment.

## Derivation, model and interpretation

A compact starting equation or relationship is **`tau = I*alpha for an isolated rigid axis`**. Define every symbol, include appropriate physical units and interpret the input and output quantities. The displayed relationship may be exact within an ideal geometry, a simplification of more complete dynamics, or a statistical approximation. Its status must be recorded. When the formula requires constant dimensions or a fixed reference frame, note these conditions explicitly. A coordinate-dependent result is meaningless until frame orientation and origin are identified.

**Physical interpretation.** Place the governing relationship beside a sketch with vectors, directions and units. Identify which terms are geometry, which describe dynamics, and which are sensor-derived approximations. The useful question is not simply whether software returns a number, but whether the quantity corresponds to a well-defined physical observation. In this lesson, look specifically at **newton–euler balance for links** rather than copying a generic control diagram. Ask which model terms could be measured directly. For each unmeasured quantity, give a method for identification and state what additional assumptions that method requires.

**Submodel and system boundary.** Loads and physical interfaces Distinguish the ideal mathematical transformation from the mechanical or software device implementing it. For example, a calculated path requires a motion executor, a sensor-based termination rule and an independently assessed response to loss of communication. A fully specified algorithm can still be unsuitable for hardware when the necessary observations arrive too late.

## Worked calculation and numerical judgment

With I=0.060 kg·m² and angular acceleration 4 rad/s², an ideal isolated axis needs 0.24 N·m acceleration torque before gravity and friction. Reproduce the substitution on paper, carry units through each stage and check the scale with an independent estimate. Precision in displayed decimal places does not demonstrate precise knowledge of link lengths, accelerations, friction coefficients or camera calibration. If inputs are rounded or synthetic, the outputs inherit those limitations; do not label them as measured robot performance.

**Traceable Verification audit.** Record firmware or model version, sensor calibration, test fixture revision and all rejected trials. Set acceptance thresholds before viewing the final traces. If a physical trial cannot be carried out safely, use simulation only and write the missing validation item explicitly. Extend the example by sweeping one independent input through a realistic range. Predict the qualitative trend before computing. Then change another input in a separate run; explain why changing both simultaneously would make causal interpretation weaker. Document any singular, discontinuous or saturating regime instead of hiding it by clipping a plot without explanation.

## Engineering interpretation and practical alternatives

The principal design trade-off is between algorithmic or mechanical capability and the evidence needed to operate it reliably. A high-speed option may increase throughput but increase motor heating and the consequence of a delayed stop. A sophisticated estimator may reduce drift under good lighting but fail abruptly when landmarks disappear. A carefully bounded simpler system can therefore outperform a more elaborate system under the actual operating conditions.

**Specific failure mechanism.** A model equates motor rotor inertia with reflected complete joint inertia. Do not respond automatically by increasing controller gain or changing a threshold. State what instrument or independent observation would reveal the difference between a bad model, incorrect calibration, measurement delay and a mechanical fault. Consider the consequences for neighboring subsystems: sensing errors affect grasp decisions, trajectory errors affect collision risk, and recovery behavior affects throughput.

**Integration perspective.** Draw free-body diagrams for tool, payload and actuator shaft. For an accelerating robot, static holding torque is not sufficient; distinguish inertial, gravitational, contact and friction terms. Thermal capacity can be more restrictive than a one-cycle peak torque calculation. For this topic, explicitly identify the preceding system function that supplies information and the following function that consumes the output. Give those interfaces names and units. State whether data is real time, sampled, batch-produced or only available after an operation ends. Wrong timing semantics can invalidate a mathematically correct equation.

## Verification protocol and evidence quality

A falsifiable check is: **Compare measured current-derived torque during low-speed acceleration ramps in both directions.** Establish independent observations whenever practical. Define an input range, number of trials, logging rate, expected trend, calibration reference and an acceptance threshold selected before analysis. At minimum include a nominal trial, a limiting case and an innocuous fault or missing-data condition. Physically hazardous failure injection requires qualified supervision and appropriate containment; otherwise conduct the test virtually and describe that limitation.

**Failure analysis.** A gripper may hold a nominal object but slip on a contaminated surface or under acceleration. Mechanical fail-safe behavior cannot be established from ideal friction values or one demonstration. When recorded evidence contradicts a prediction, preserve the discrepancy. Consider sensor bias, frame mismatch, uncontrolled load, aliasing, model order, compliance and operator intervention as competing explanations. One favorable trace does not validate a complete operating envelope. A reliable result needs repeatability across changed initial conditions and traceability to the configuration used for the test.

**Laboratory record.** Save model revision, input parameter table, raw data, units, frame definitions, timestamps, plot-generating script, calculated sensitivity and unsuccessful cases. Attach a short statement distinguishing simulation evidence from physical measurement and from a safety-related assessment. If equipment access is unavailable, provide a transparent synthetic test with expected results and avoid representing it as laboratory measurement.

## Exercises and design investigation

1. **Interpretation:** Derive or explain `tau = I*alpha for an isolated rigid axis` from relevant geometry, conservation laws or probability assumptions. Define all quantities, directions and units. Name a realistic boundary where it loses validity.
2. **Calculation:** Recompute the worked example without copying its result. Change the most important input by 10%; compare the resulting change against the original prediction, and explain when a first-order approximation is inadequate.
3. **Independent validation:** Construct a test of newton–euler balance for links using an independent reference. State three potential sources of measurement error and which observable can isolate at least two of them.
4. **Failure and safety:** Using the specified failure mechanism, write an expected fault signature, a detection threshold and a controlled fallback response. Distinguish the operating controller from a separately evaluated safety function.
5. **Applied synthesis:** For the unit's running case, document one viable alternative architecture, what it costs in complexity, and what evidence would justify choosing it over the baseline.

## Lesson summary and transfer

The central skill is to connect **newton–euler balance for links** to a physically meaningful model and a test that could disprove it. Carry the same units, coordinate conventions, uncertainty bounds and versioned acceptance criteria into the next lesson. Robot performance is judged by reproducible task outcomes under constrained conditions, not by an appealing ideal plot or the correctness of a single formula.


---

# U03-L02 — Lagrange formulation and energy

**OpenSTEM Mechanical Engineering · Book 12: Robotics and Automation · Unit 3: Robot Dynamics, Actuation and Contacts.** Educational draft. All worked numbers are illustrative unless stated otherwise; do not use the calculations alone to certify a physical robot or protective system.

## Learning goal and context

This lesson asks how **lagrange formulation and energy** affects a realistic robotic system. Its running design problem is: A small arm repeatedly lifts and positions a 1.5 kg payload. Connect joint motion and contacts to mass, inertia, gravity, friction, actuator limits and thermal constraints. Students must explain the physical mechanism, calculate an interpretable quantity, identify an assumption that could fail, and propose an observation that would distinguish competing explanations.

**Entry-level reasoning.** Lagrange equations use kinetic minus potential energy and generalized coordinates to obtain coupled joint equations. Mass matrices vary with posture; centrifugal and Coriolis terms can dominate during rapid motion. Correct modeling preserves positive kinetic energy. In practice, begin with the machine boundary and mark the frames, joint connections, sensing path and source of power. If a controller reports a requested value, determine whether the value is a command, a filtered estimate, an independently measured result or an offline ideal prediction. These are not interchangeable. Write a short claim that would be falsified by an observed counterexample, rather than a claim that can be rescued by changing assumptions after the experiment.

## Derivation, model and interpretation

A compact starting equation or relationship is **`M(q)*qdd + C(q,qd)*qd + g(q)=tau`**. Define every symbol, include appropriate physical units and interpret the input and output quantities. The displayed relationship may be exact within an ideal geometry, a simplification of more complete dynamics, or a statistical approximation. Its status must be recorded. When the formula requires constant dimensions or a fixed reference frame, note these conditions explicitly. A coordinate-dependent result is meaningless until frame orientation and origin are identified.

**Failure boundaries.** Derive a nominal prediction, then ask how it changes near a singularity, saturation threshold, sensor outage or geometric boundary. Mathematical formulas sometimes remain numerically defined after their physical hypotheses are violated. The validity envelope should be written before any plot is treated as a performance forecast. In this lesson, look specifically at **lagrange formulation and energy** rather than copying a generic control diagram. Ask which model terms could be measured directly. For each unmeasured quantity, give a method for identification and state what additional assumptions that method requires.

**Submodel and system boundary.** Loads and physical interfaces Distinguish the ideal mathematical transformation from the mechanical or software device implementing it. For example, a calculated path requires a motion executor, a sensor-based termination rule and an independently assessed response to loss of communication. A fully specified algorithm can still be unsuitable for hardware when the necessary observations arrive too late.

## Worked calculation and numerical judgment

For a single rigid link with I=0.08 kg·m², angular acceleration 2 rad/s² gives 0.16 N·m inertia torque in the gravity-free idealization. Reproduce the substitution on paper, carry units through each stage and check the scale with an independent estimate. Precision in displayed decimal places does not demonstrate precise knowledge of link lengths, accelerations, friction coefficients or camera calibration. If inputs are rounded or synthetic, the outputs inherit those limitations; do not label them as measured robot performance.

**Dimensional Balance audit.** Perform a units check by substituting SI base units and showing both sides match. For angles, state that trigonometric functions expect radians unless explicitly converted. For probabilities, check output within [0,1], and for lengths or times reject negative values when the model defines only positive quantities. Extend the example by sweeping one independent input through a realistic range. Predict the qualitative trend before computing. Then change another input in a separate run; explain why changing both simultaneously would make causal interpretation weaker. Document any singular, discontinuous or saturating regime instead of hiding it by clipping a plot without explanation.

## Engineering interpretation and practical alternatives

The principal design trade-off is between algorithmic or mechanical capability and the evidence needed to operate it reliably. A high-speed option may increase throughput but increase motor heating and the consequence of a delayed stop. A sophisticated estimator may reduce drift under good lighting but fail abruptly when landmarks disappear. A carefully bounded simpler system can therefore outperform a more elaborate system under the actual operating conditions.

**Specific failure mechanism.** Joint-by-joint independent models miss dynamic coupling at higher acceleration. Do not respond automatically by increasing controller gain or changing a threshold. State what instrument or independent observation would reveal the difference between a bad model, incorrect calibration, measurement delay and a mechanical fault. Consider the consequences for neighboring subsystems: sensing errors affect grasp decisions, trajectory errors affect collision risk, and recovery behavior affects throughput.

**Integration perspective.** Draw free-body diagrams for tool, payload and actuator shaft. For an accelerating robot, static holding torque is not sufficient; distinguish inertial, gravitational, contact and friction terms. Thermal capacity can be more restrictive than a one-cycle peak torque calculation. For this topic, explicitly identify the preceding system function that supplies information and the following function that consumes the output. Give those interfaces names and units. State whether data is real time, sampled, batch-produced or only available after an operation ends. Wrong timing semantics can invalidate a mathematically correct equation.

## Verification protocol and evidence quality

A falsifiable check is: **Check energy consistency and compare predictions with slowly and rapidly executed trajectories.** Establish independent observations whenever practical. Define an input range, number of trials, logging rate, expected trend, calibration reference and an acceptance threshold selected before analysis. At minimum include a nominal trial, a limiting case and an innocuous fault or missing-data condition. Physically hazardous failure injection requires qualified supervision and appropriate containment; otherwise conduct the test virtually and describe that limitation.

**Failure analysis.** A gripper may hold a nominal object but slip on a contaminated surface or under acceleration. Mechanical fail-safe behavior cannot be established from ideal friction values or one demonstration. When recorded evidence contradicts a prediction, preserve the discrepancy. Consider sensor bias, frame mismatch, uncontrolled load, aliasing, model order, compliance and operator intervention as competing explanations. One favorable trace does not validate a complete operating envelope. A reliable result needs repeatability across changed initial conditions and traceability to the configuration used for the test.

**Laboratory record.** Save model revision, input parameter table, raw data, units, frame definitions, timestamps, plot-generating script, calculated sensitivity and unsuccessful cases. Attach a short statement distinguishing simulation evidence from physical measurement and from a safety-related assessment. If equipment access is unavailable, provide a transparent synthetic test with expected results and avoid representing it as laboratory measurement.

## Exercises and design investigation

1. **Interpretation:** Derive or explain `M(q)*qdd + C(q,qd)*qd + g(q)=tau` from relevant geometry, conservation laws or probability assumptions. Define all quantities, directions and units. Name a realistic boundary where it loses validity.
2. **Calculation:** Recompute the worked example without copying its result. Change the most important input by 10%; compare the resulting change against the original prediction, and explain when a first-order approximation is inadequate.
3. **Independent validation:** Construct a test of lagrange formulation and energy using an independent reference. State three potential sources of measurement error and which observable can isolate at least two of them.
4. **Failure and safety:** Using the specified failure mechanism, write an expected fault signature, a detection threshold and a controlled fallback response. Distinguish the operating controller from a separately evaluated safety function.
5. **Applied synthesis:** For the unit's running case, document one viable alternative architecture, what it costs in complexity, and what evidence would justify choosing it over the baseline.

## Lesson summary and transfer

The central skill is to connect **lagrange formulation and energy** to a physically meaningful model and a test that could disprove it. Carry the same units, coordinate conventions, uncertainty bounds and versioned acceptance criteria into the next lesson. Robot performance is judged by reproducible task outcomes under constrained conditions, not by an appealing ideal plot or the correctness of a single formula.


---

# U03-L03 — Motor and gear selection

**OpenSTEM Mechanical Engineering · Book 12: Robotics and Automation · Unit 3: Robot Dynamics, Actuation and Contacts.** Educational draft. All worked numbers are illustrative unless stated otherwise; do not use the calculations alone to certify a physical robot or protective system.

## Learning goal and context

This lesson asks how **motor and gear selection** affects a realistic robotic system. Its running design problem is: A small arm repeatedly lifts and positions a 1.5 kg payload. Connect joint motion and contacts to mass, inertia, gravity, friction, actuator limits and thermal constraints. Students must explain the physical mechanism, calculate an interpretable quantity, identify an assumption that could fail, and propose an observation that would distinguish competing explanations.

**Entry-level reasoning.** A gearbox trades speed and torque but adds backlash, friction and inertia reflection. Motor selection depends on RMS continuous torque, peak acceleration demand, duty cycle, cooling and shaft limits. A catalog stall-torque value is not a continuous operating rating. In practice, begin with the machine boundary and mark the frames, joint connections, sensing path and source of power. If a controller reports a requested value, determine whether the value is a command, a filtered estimate, an independently measured result or an offline ideal prediction. These are not interchangeable. Write a short claim that would be falsified by an observed counterexample, rather than a claim that can be rescued by changing assumptions after the experiment.

## Derivation, model and interpretation

A compact starting equation or relationship is **`tau_out = eta * G * tau_motor`**. Define every symbol, include appropriate physical units and interpret the input and output quantities. The displayed relationship may be exact within an ideal geometry, a simplification of more complete dynamics, or a statistical approximation. Its status must be recorded. When the formula requires constant dimensions or a fixed reference frame, note these conditions explicitly. A coordinate-dependent result is meaningless until frame orientation and origin are identified.

**Identification and calibration.** A single fitted parameter can conceal bias in a different component. If friction, encoder scale and controller gain all change together, the resulting trace does not identify their separate causes. Change a controlled input and compare with an independent instrument where possible. In this lesson, look specifically at **motor and gear selection** rather than copying a generic control diagram. Ask which model terms could be measured directly. For each unmeasured quantity, give a method for identification and state what additional assumptions that method requires.

**Submodel and system boundary.** Loads and physical interfaces Distinguish the ideal mathematical transformation from the mechanical or software device implementing it. For example, a calculated path requires a motion executor, a sensor-based termination rule and an independently assessed response to loss of communication. A fully specified algorithm can still be unsuitable for hardware when the necessary observations arrive too late.

## Worked calculation and numerical judgment

For gear ratio 12, efficiency 0.80 and motor torque 0.15 N·m, output torque is 1.44 N·m under the assumed point-efficiency. Reproduce the substitution on paper, carry units through each stage and check the scale with an independent estimate. Precision in displayed decimal places does not demonstrate precise knowledge of link lengths, accelerations, friction coefficients or camera calibration. If inputs are rounded or synthetic, the outputs inherit those limitations; do not label them as measured robot performance.

**Boundary Cases audit.** Check a zero-input limit, a typical operating point and a maximum planned input. Where derivatives exist, estimate local sensitivity to a 5% change. If the result changes sharply, prioritize a measurement of the sensitive parameter rather than increasing numerical precision elsewhere. Extend the example by sweeping one independent input through a realistic range. Predict the qualitative trend before computing. Then change another input in a separate run; explain why changing both simultaneously would make causal interpretation weaker. Document any singular, discontinuous or saturating regime instead of hiding it by clipping a plot without explanation.

## Engineering interpretation and practical alternatives

The principal design trade-off is between algorithmic or mechanical capability and the evidence needed to operate it reliably. A high-speed option may increase throughput but increase motor heating and the consequence of a delayed stop. A sophisticated estimator may reduce drift under good lighting but fail abruptly when landmarks disappear. A carefully bounded simpler system can therefore outperform a more elaborate system under the actual operating conditions.

**Specific failure mechanism.** Selecting by peak output torque alone overheats the motor during repetitive holding. Do not respond automatically by increasing controller gain or changing a threshold. State what instrument or independent observation would reveal the difference between a bad model, incorrect calibration, measurement delay and a mechanical fault. Consider the consequences for neighboring subsystems: sensing errors affect grasp decisions, trajectory errors affect collision risk, and recovery behavior affects throughput.

**Integration perspective.** Draw free-body diagrams for tool, payload and actuator shaft. For an accelerating robot, static holding torque is not sufficient; distinguish inertial, gravitational, contact and friction terms. Thermal capacity can be more restrictive than a one-cycle peak torque calculation. For this topic, explicitly identify the preceding system function that supplies information and the following function that consumes the output. Give those interfaces names and units. State whether data is real time, sampled, batch-produced or only available after an operation ends. Wrong timing semantics can invalidate a mathematically correct equation.

## Verification protocol and evidence quality

A falsifiable check is: **Measure current and winding temperature during a full representative duty cycle; compare with derated ratings.** Establish independent observations whenever practical. Define an input range, number of trials, logging rate, expected trend, calibration reference and an acceptance threshold selected before analysis. At minimum include a nominal trial, a limiting case and an innocuous fault or missing-data condition. Physically hazardous failure injection requires qualified supervision and appropriate containment; otherwise conduct the test virtually and describe that limitation.

**Failure analysis.** A gripper may hold a nominal object but slip on a contaminated surface or under acceleration. Mechanical fail-safe behavior cannot be established from ideal friction values or one demonstration. When recorded evidence contradicts a prediction, preserve the discrepancy. Consider sensor bias, frame mismatch, uncontrolled load, aliasing, model order, compliance and operator intervention as competing explanations. One favorable trace does not validate a complete operating envelope. A reliable result needs repeatability across changed initial conditions and traceability to the configuration used for the test.

**Laboratory record.** Save model revision, input parameter table, raw data, units, frame definitions, timestamps, plot-generating script, calculated sensitivity and unsuccessful cases. Attach a short statement distinguishing simulation evidence from physical measurement and from a safety-related assessment. If equipment access is unavailable, provide a transparent synthetic test with expected results and avoid representing it as laboratory measurement.

## Exercises and design investigation

1. **Interpretation:** Derive or explain `tau_out = eta * G * tau_motor` from relevant geometry, conservation laws or probability assumptions. Define all quantities, directions and units. Name a realistic boundary where it loses validity.
2. **Calculation:** Recompute the worked example without copying its result. Change the most important input by 10%; compare the resulting change against the original prediction, and explain when a first-order approximation is inadequate.
3. **Independent validation:** Construct a test of motor and gear selection using an independent reference. State three potential sources of measurement error and which observable can isolate at least two of them.
4. **Failure and safety:** Using the specified failure mechanism, write an expected fault signature, a detection threshold and a controlled fallback response. Distinguish the operating controller from a separately evaluated safety function.
5. **Applied synthesis:** For the unit's running case, document one viable alternative architecture, what it costs in complexity, and what evidence would justify choosing it over the baseline.

## Lesson summary and transfer

The central skill is to connect **motor and gear selection** to a physically meaningful model and a test that could disprove it. Carry the same units, coordinate conventions, uncertainty bounds and versioned acceptance criteria into the next lesson. Robot performance is judged by reproducible task outcomes under constrained conditions, not by an appealing ideal plot or the correctness of a single formula.


---

# U03-L04 — Grasp force, friction and object variability

**OpenSTEM Mechanical Engineering · Book 12: Robotics and Automation · Unit 3: Robot Dynamics, Actuation and Contacts.** Educational draft. All worked numbers are illustrative unless stated otherwise; do not use the calculations alone to certify a physical robot or protective system.

## Learning goal and context

This lesson asks how **grasp force, friction and object variability** affects a realistic robotic system. Its running design problem is: A small arm repeatedly lifts and positions a 1.5 kg payload. Connect joint motion and contacts to mass, inertia, gravity, friction, actuator limits and thermal constraints. Students must explain the physical mechanism, calculate an interpretable quantity, identify an assumption that could fail, and propose an observation that would distinguish competing explanations.

**Entry-level reasoning.** Parallel-jaw holding depends on normal force, friction, load direction, contact geometry and acceleration. A simple symmetric model gives two contacts each with friction μN; introduce a conservative margin but do not use a single coefficient for textured, oily or deformable parts. In practice, begin with the machine boundary and mark the frames, joint connections, sensing path and source of power. If a controller reports a requested value, determine whether the value is a command, a filtered estimate, an independently measured result or an offline ideal prediction. These are not interchangeable. Write a short claim that would be falsified by an observed counterexample, rather than a claim that can be rescued by changing assumptions after the experiment.

## Derivation, model and interpretation

A compact starting equation or relationship is **`2*mu*N >= m*(g+a)`**. Define every symbol, include appropriate physical units and interpret the input and output quantities. The displayed relationship may be exact within an ideal geometry, a simplification of more complete dynamics, or a statistical approximation. Its status must be recorded. When the formula requires constant dimensions or a fixed reference frame, note these conditions explicitly. A coordinate-dependent result is meaningless until frame orientation and origin are identified.

**Implementation choice.** The lightest controller or cheapest sensor is not automatically the best solution. Complexity can improve diagnostics yet add failure modes and maintenance obligations. Define what a more advanced method would need to prove under representative loads, timing, environment and budget. In this lesson, look specifically at **grasp force, friction and object variability** rather than copying a generic control diagram. Ask which model terms could be measured directly. For each unmeasured quantity, give a method for identification and state what additional assumptions that method requires.

**Submodel and system boundary.** Loads and physical interfaces Distinguish the ideal mathematical transformation from the mechanical or software device implementing it. For example, a calculated path requires a motion executor, a sensor-based termination rule and an independently assessed response to loss of communication. A fully specified algorithm can still be unsuitable for hardware when the necessary observations arrive too late.

## Worked calculation and numerical judgment

For m=1 kg, μ=0.50 and upward acceleration 1 m/s², each jaw needs at least 10.81 N in the ideal symmetric model. Reproduce the substitution on paper, carry units through each stage and check the scale with an independent estimate. Precision in displayed decimal places does not demonstrate precise knowledge of link lengths, accelerations, friction coefficients or camera calibration. If inputs are rounded or synthetic, the outputs inherit those limitations; do not label them as measured robot performance.

**Discretization audit.** Choose a simulation step that resolves the fastest physical phenomenon of interest. Check convergence with a smaller step and confirm that numerical artifacts do not explain apparent stability or contact behavior. Sampling rates must exceed the bandwidth of the phenomena they are claimed to detect. Extend the example by sweeping one independent input through a realistic range. Predict the qualitative trend before computing. Then change another input in a separate run; explain why changing both simultaneously would make causal interpretation weaker. Document any singular, discontinuous or saturating regime instead of hiding it by clipping a plot without explanation.

## Engineering interpretation and practical alternatives

The principal design trade-off is between algorithmic or mechanical capability and the evidence needed to operate it reliably. A high-speed option may increase throughput but increase motor heating and the consequence of a delayed stop. A sophisticated estimator may reduce drift under good lighting but fail abruptly when landmarks disappear. A carefully bounded simpler system can therefore outperform a more elaborate system under the actual operating conditions.

**Specific failure mechanism.** A nominal friction coefficient measured on clean samples fails on dusty cartons. Do not respond automatically by increasing controller gain or changing a threshold. State what instrument or independent observation would reveal the difference between a bad model, incorrect calibration, measurement delay and a mechanical fault. Consider the consequences for neighboring subsystems: sensing errors affect grasp decisions, trajectory errors affect collision risk, and recovery behavior affects throughput.

**Integration perspective.** Draw free-body diagrams for tool, payload and actuator shaft. For an accelerating robot, static holding torque is not sufficient; distinguish inertial, gravitational, contact and friction terms. Thermal capacity can be more restrictive than a one-cycle peak torque calculation. For this topic, explicitly identify the preceding system function that supplies information and the following function that consumes the output. Give those interfaces names and units. State whether data is real time, sampled, batch-produced or only available after an operation ends. Wrong timing semantics can invalidate a mathematically correct equation.

## Verification protocol and evidence quality

A falsifiable check is: **Test a range of representative surfaces at guarded low energy while measuring slip and clamping damage.** Establish independent observations whenever practical. Define an input range, number of trials, logging rate, expected trend, calibration reference and an acceptance threshold selected before analysis. At minimum include a nominal trial, a limiting case and an innocuous fault or missing-data condition. Physically hazardous failure injection requires qualified supervision and appropriate containment; otherwise conduct the test virtually and describe that limitation.

**Failure analysis.** A gripper may hold a nominal object but slip on a contaminated surface or under acceleration. Mechanical fail-safe behavior cannot be established from ideal friction values or one demonstration. When recorded evidence contradicts a prediction, preserve the discrepancy. Consider sensor bias, frame mismatch, uncontrolled load, aliasing, model order, compliance and operator intervention as competing explanations. One favorable trace does not validate a complete operating envelope. A reliable result needs repeatability across changed initial conditions and traceability to the configuration used for the test.

**Laboratory record.** Save model revision, input parameter table, raw data, units, frame definitions, timestamps, plot-generating script, calculated sensitivity and unsuccessful cases. Attach a short statement distinguishing simulation evidence from physical measurement and from a safety-related assessment. If equipment access is unavailable, provide a transparent synthetic test with expected results and avoid representing it as laboratory measurement.

## Exercises and design investigation

1. **Interpretation:** Derive or explain `2*mu*N >= m*(g+a)` from relevant geometry, conservation laws or probability assumptions. Define all quantities, directions and units. Name a realistic boundary where it loses validity.
2. **Calculation:** Recompute the worked example without copying its result. Change the most important input by 10%; compare the resulting change against the original prediction, and explain when a first-order approximation is inadequate.
3. **Independent validation:** Construct a test of grasp force, friction and object variability using an independent reference. State three potential sources of measurement error and which observable can isolate at least two of them.
4. **Failure and safety:** Using the specified failure mechanism, write an expected fault signature, a detection threshold and a controlled fallback response. Distinguish the operating controller from a separately evaluated safety function.
5. **Applied synthesis:** For the unit's running case, document one viable alternative architecture, what it costs in complexity, and what evidence would justify choosing it over the baseline.

## Lesson summary and transfer

The central skill is to connect **grasp force, friction and object variability** to a physically meaningful model and a test that could disprove it. Carry the same units, coordinate conventions, uncertainty bounds and versioned acceptance criteria into the next lesson. Robot performance is judged by reproducible task outcomes under constrained conditions, not by an appealing ideal plot or the correctness of a single formula.


---

# U03-L05 — Collision impulse and compliant contact

**OpenSTEM Mechanical Engineering · Book 12: Robotics and Automation · Unit 3: Robot Dynamics, Actuation and Contacts.** Educational draft. All worked numbers are illustrative unless stated otherwise; do not use the calculations alone to certify a physical robot or protective system.

## Learning goal and context

This lesson asks how **collision impulse and compliant contact** affects a realistic robotic system. Its running design problem is: A small arm repeatedly lifts and positions a 1.5 kg payload. Connect joint motion and contacts to mass, inertia, gravity, friction, actuator limits and thermal constraints. Students must explain the physical mechanism, calculate an interpretable quantity, identify an assumption that could fail, and propose an observation that would distinguish competing explanations.

**Entry-level reasoning.** Contact force depends on deceleration history, surface stiffness and control response. Impulse relates the integral of force to momentum change; kinetic energy alone does not specify a safe impact force. Compliance and protective devices require formal evaluation. In practice, begin with the machine boundary and mark the frames, joint connections, sensing path and source of power. If a controller reports a requested value, determine whether the value is a command, a filtered estimate, an independently measured result or an offline ideal prediction. These are not interchangeable. Write a short claim that would be falsified by an observed counterexample, rather than a claim that can be rescued by changing assumptions after the experiment.

## Derivation, model and interpretation

A compact starting equation or relationship is **`J = m * (v_after-v_before)`**. Define every symbol, include appropriate physical units and interpret the input and output quantities. The displayed relationship may be exact within an ideal geometry, a simplification of more complete dynamics, or a statistical approximation. Its status must be recorded. When the formula requires constant dimensions or a fixed reference frame, note these conditions explicitly. A coordinate-dependent result is meaningless until frame orientation and origin are identified.

**Operational consequence.** A robot cell has no isolated subsystem outcomes. A high-accuracy reach solution can be invalidated by perception latency, a good gripper can fail on a different surface, and a fast conveyor can overwhelm fault handling. Preserve interface specifications and model uncertainty across design stages. In this lesson, look specifically at **collision impulse and compliant contact** rather than copying a generic control diagram. Ask which model terms could be measured directly. For each unmeasured quantity, give a method for identification and state what additional assumptions that method requires.

**Submodel and system boundary.** Loads and physical interfaces Distinguish the ideal mathematical transformation from the mechanical or software device implementing it. For example, a calculated path requires a motion executor, a sensor-based termination rule and an independently assessed response to loss of communication. A fully specified algorithm can still be unsuitable for hardware when the necessary observations arrive too late.

## Worked calculation and numerical judgment

A 2 kg object stopped from 0.5 m/s experiences 1 N·s magnitude impulse regardless of how quickly it is stopped. Reproduce the substitution on paper, carry units through each stage and check the scale with an independent estimate. Precision in displayed decimal places does not demonstrate precise knowledge of link lengths, accelerations, friction coefficients or camera calibration. If inputs are rounded or synthetic, the outputs inherit those limitations; do not label them as measured robot performance.

**Uncertainty audit.** Differentiate precision from accuracy: repeated values near one another may share a systematic offset. Use replicated trials and a calibration reference, and consider correlations when combining uncertainties. An error bound must be linked to a defined operating range. Extend the example by sweeping one independent input through a realistic range. Predict the qualitative trend before computing. Then change another input in a separate run; explain why changing both simultaneously would make causal interpretation weaker. Document any singular, discontinuous or saturating regime instead of hiding it by clipping a plot without explanation.

## Engineering interpretation and practical alternatives

The principal design trade-off is between algorithmic or mechanical capability and the evidence needed to operate it reliably. A high-speed option may increase throughput but increase motor heating and the consequence of a delayed stop. A sophisticated estimator may reduce drift under good lighting but fail abruptly when landmarks disappear. A carefully bounded simpler system can therefore outperform a more elaborate system under the actual operating conditions.

**Specific failure mechanism.** Assuming a low-speed command guarantees low peak force ignores rigid contact and sensor delay. Do not respond automatically by increasing controller gain or changing a threshold. State what instrument or independent observation would reveal the difference between a bad model, incorrect calibration, measurement delay and a mechanical fault. Consider the consequences for neighboring subsystems: sensing errors affect grasp decisions, trajectory errors affect collision risk, and recovery behavior affects throughput.

**Integration perspective.** Draw free-body diagrams for tool, payload and actuator shaft. For an accelerating robot, static holding torque is not sufficient; distinguish inertial, gravitational, contact and friction terms. Thermal capacity can be more restrictive than a one-cycle peak torque calculation. For this topic, explicitly identify the preceding system function that supplies information and the following function that consumes the output. Give those interfaces names and units. State whether data is real time, sampled, batch-produced or only available after an operation ends. Wrong timing semantics can invalidate a mathematically correct equation.

## Verification protocol and evidence quality

A falsifiable check is: **Observe force-time traces in a low-energy contained test with a conservative hardware force limit.** Establish independent observations whenever practical. Define an input range, number of trials, logging rate, expected trend, calibration reference and an acceptance threshold selected before analysis. At minimum include a nominal trial, a limiting case and an innocuous fault or missing-data condition. Physically hazardous failure injection requires qualified supervision and appropriate containment; otherwise conduct the test virtually and describe that limitation.

**Failure analysis.** A gripper may hold a nominal object but slip on a contaminated surface or under acceleration. Mechanical fail-safe behavior cannot be established from ideal friction values or one demonstration. When recorded evidence contradicts a prediction, preserve the discrepancy. Consider sensor bias, frame mismatch, uncontrolled load, aliasing, model order, compliance and operator intervention as competing explanations. One favorable trace does not validate a complete operating envelope. A reliable result needs repeatability across changed initial conditions and traceability to the configuration used for the test.

**Laboratory record.** Save model revision, input parameter table, raw data, units, frame definitions, timestamps, plot-generating script, calculated sensitivity and unsuccessful cases. Attach a short statement distinguishing simulation evidence from physical measurement and from a safety-related assessment. If equipment access is unavailable, provide a transparent synthetic test with expected results and avoid representing it as laboratory measurement.

## Exercises and design investigation

1. **Interpretation:** Derive or explain `J = m * (v_after-v_before)` from relevant geometry, conservation laws or probability assumptions. Define all quantities, directions and units. Name a realistic boundary where it loses validity.
2. **Calculation:** Recompute the worked example without copying its result. Change the most important input by 10%; compare the resulting change against the original prediction, and explain when a first-order approximation is inadequate.
3. **Independent validation:** Construct a test of collision impulse and compliant contact using an independent reference. State three potential sources of measurement error and which observable can isolate at least two of them.
4. **Failure and safety:** Using the specified failure mechanism, write an expected fault signature, a detection threshold and a controlled fallback response. Distinguish the operating controller from a separately evaluated safety function.
5. **Applied synthesis:** For the unit's running case, document one viable alternative architecture, what it costs in complexity, and what evidence would justify choosing it over the baseline.

## Lesson summary and transfer

The central skill is to connect **collision impulse and compliant contact** to a physically meaningful model and a test that could disprove it. Carry the same units, coordinate conventions, uncertainty bounds and versioned acceptance criteria into the next lesson. Robot performance is judged by reproducible task outcomes under constrained conditions, not by an appealing ideal plot or the correctness of a single formula.


---

