# Unit 02: Manipulators and Robot Kinematics

**Course Code**: ROB 402 · **Level**: Advanced Undergraduate Engineering

## Unit Overview & Physical Foundations

This comprehensive university textbook unit covers the theoretical framework, physical modeling, mathematical governing equations, and engineering applications of **Manipulators and Robot Kinematics**.

# U02-L01 — Homogeneous transformations and chains

**OpenSTEM Mechanical Engineering · Book 12: Robotics and Automation · Unit 2: Manipulators and Robot Kinematics.** Educational draft. All worked numbers are illustrative unless stated otherwise; do not use the calculations alone to certify a physical robot or protective system.

## Learning goal and context

This lesson asks how **homogeneous transformations and chains** affects a realistic robotic system. Its running design problem is: A two-link inspection robot must reach several sampling wells without touching the fixture. Derive forward and inverse relationships between joint states and task-space pose, then identify physical limits. Students must explain the physical mechanism, calculate an interpretable quantity, identify an assumption that could fail, and propose an observation that would distinguish competing explanations.

**Entry-level reasoning.** A rigid transform consists of a 3×3 orthonormal rotation and a translation vector, represented in a 4×4 homogeneous matrix. Chaining transforms links each joint frame to the tool; reversing a transform requires a matrix inverse, not negating position alone. In practice, begin with the machine boundary and mark the frames, joint connections, sensing path and source of power. If a controller reports a requested value, determine whether the value is a command, a filtered estimate, an independently measured result or an offline ideal prediction. These are not interchangeable. Write a short claim that would be falsified by an observed counterexample, rather than a claim that can be rescued by changing assumptions after the experiment.

## Derivation, model and interpretation

A compact starting equation or relationship is **`T_0_tool = T_0_1 * T_1_2 * ... * T_n_tool`**. Define every symbol, include appropriate physical units and interpret the input and output quantities. The displayed relationship may be exact within an ideal geometry, a simplification of more complete dynamics, or a statistical approximation. Its status must be recorded. When the formula requires constant dimensions or a fixed reference frame, note these conditions explicitly. A coordinate-dependent result is meaningless until frame orientation and origin are identified.

**Identification and calibration.** A single fitted parameter can conceal bias in a different component. If friction, encoder scale and controller gain all change together, the resulting trace does not identify their separate causes. Change a controlled input and compare with an independent instrument where possible. In this lesson, look specifically at **homogeneous transformations and chains** rather than copying a generic control diagram. Ask which model terms could be measured directly. For each unmeasured quantity, give a method for identification and state what additional assumptions that method requires.

**Submodel and system boundary.** Geometry and identification Distinguish the ideal mathematical transformation from the mechanical or software device implementing it. For example, a calculated path requires a motion executor, a sensor-based termination rule and an independently assessed response to loss of communication. A fully specified algorithm can still be unsuitable for hardware when the necessary observations arrive too late.

## Worked calculation and numerical judgment

Two aligned 0.30 m and 0.20 m links at zero joint angle place a planar tip 0.50 m from the first joint center. Reproduce the substitution on paper, carry units through each stage and check the scale with an independent estimate. Precision in displayed decimal places does not demonstrate precise knowledge of link lengths, accelerations, friction coefficients or camera calibration. If inputs are rounded or synthetic, the outputs inherit those limitations; do not label them as measured robot performance.

**Uncertainty audit.** Differentiate precision from accuracy: repeated values near one another may share a systematic offset. Use replicated trials and a calibration reference, and consider correlations when combining uncertainties. An error bound must be linked to a defined operating range. Extend the example by sweeping one independent input through a realistic range. Predict the qualitative trend before computing. Then change another input in a separate run; explain why changing both simultaneously would make causal interpretation weaker. Document any singular, discontinuous or saturating regime instead of hiding it by clipping a plot without explanation.

## Engineering interpretation and practical alternatives

The principal design trade-off is between algorithmic or mechanical capability and the evidence needed to operate it reliably. A high-speed option may increase throughput but increase motor heating and the consequence of a delayed stop. A sophisticated estimator may reduce drift under good lighting but fail abruptly when landmarks disappear. A carefully bounded simpler system can therefore outperform a more elaborate system under the actual operating conditions.

**Specific failure mechanism.** An incorrect axis ordering makes a trajectory appear mirrored while endpoint distances look reasonable. Do not respond automatically by increasing controller gain or changing a threshold. State what instrument or independent observation would reveal the difference between a bad model, incorrect calibration, measurement delay and a mechanical fault. Consider the consequences for neighboring subsystems: sensing errors affect grasp decisions, trajectory errors affect collision risk, and recovery behavior affects throughput.

**Integration perspective.** A coordinate transform is a mapping between explicitly named frames. Keep reference frames and calibrated tool center point in a ledger; use radians internally and specify the sign of every joint angle. Include joint hard stops, back-driving and reachable orientation in the feasibility analysis. For this topic, explicitly identify the preceding system function that supplies information and the following function that consumes the output. Give those interfaces names and units. State whether data is real time, sampled, batch-produced or only available after an operation ends. Wrong timing semantics can invalidate a mathematically correct equation.

## Verification protocol and evidence quality

A falsifiable check is: **Check the zero posture, single-joint rotations and a complete closed transform loop for consistency.** Establish independent observations whenever practical. Define an input range, number of trials, logging rate, expected trend, calibration reference and an acceptance threshold selected before analysis. At minimum include a nominal trial, a limiting case and an innocuous fault or missing-data condition. Physically hazardous failure injection requires qualified supervision and appropriate containment; otherwise conduct the test virtually and describe that limitation.

**Failure analysis.** Calibrating with no payload but operating at full payload can shift tool pose. Characterize systematic bias separately from random error; check the near-singular and workspace-boundary cases deliberately. When recorded evidence contradicts a prediction, preserve the discrepancy. Consider sensor bias, frame mismatch, uncontrolled load, aliasing, model order, compliance and operator intervention as competing explanations. One favorable trace does not validate a complete operating envelope. A reliable result needs repeatability across changed initial conditions and traceability to the configuration used for the test.

**Laboratory record.** Save model revision, input parameter table, raw data, units, frame definitions, timestamps, plot-generating script, calculated sensitivity and unsuccessful cases. Attach a short statement distinguishing simulation evidence from physical measurement and from a safety-related assessment. If equipment access is unavailable, provide a transparent synthetic test with expected results and avoid representing it as laboratory measurement.

## Exercises and design investigation

1. **Interpretation:** Derive or explain `T_0_tool = T_0_1 * T_1_2 * ... * T_n_tool` from relevant geometry, conservation laws or probability assumptions. Define all quantities, directions and units. Name a realistic boundary where it loses validity.
2. **Calculation:** Recompute the worked example without copying its result. Change the most important input by 10%; compare the resulting change against the original prediction, and explain when a first-order approximation is inadequate.
3. **Independent validation:** Construct a test of homogeneous transformations and chains using an independent reference. State three potential sources of measurement error and which observable can isolate at least two of them.
4. **Failure and safety:** Using the specified failure mechanism, write an expected fault signature, a detection threshold and a controlled fallback response. Distinguish the operating controller from a separately evaluated safety function.
5. **Applied synthesis:** For the unit's running case, document one viable alternative architecture, what it costs in complexity, and what evidence would justify choosing it over the baseline.

## Lesson summary and transfer

The central skill is to connect **homogeneous transformations and chains** to a physically meaningful model and a test that could disprove it. Carry the same units, coordinate conventions, uncertainty bounds and versioned acceptance criteria into the next lesson. Robot performance is judged by reproducible task outcomes under constrained conditions, not by an appealing ideal plot or the correctness of a single formula.


---

# U02-L02 — Two-link forward kinematics

**OpenSTEM Mechanical Engineering · Book 12: Robotics and Automation · Unit 2: Manipulators and Robot Kinematics.** Educational draft. All worked numbers are illustrative unless stated otherwise; do not use the calculations alone to certify a physical robot or protective system.

## Learning goal and context

This lesson asks how **two-link forward kinematics** affects a realistic robotic system. Its running design problem is: A two-link inspection robot must reach several sampling wells without touching the fixture. Derive forward and inverse relationships between joint states and task-space pose, then identify physical limits. Students must explain the physical mechanism, calculate an interpretable quantity, identify an assumption that could fail, and propose an observation that would distinguish competing explanations.

**Entry-level reasoning.** For a planar revolute–revolute arm the tip coordinates follow the vector sum of the two links. Take care that the second link angle is relative to the first; cosine and sine use absolute cumulative angle. In practice, begin with the machine boundary and mark the frames, joint connections, sensing path and source of power. If a controller reports a requested value, determine whether the value is a command, a filtered estimate, an independently measured result or an offline ideal prediction. These are not interchangeable. Write a short claim that would be falsified by an observed counterexample, rather than a claim that can be rescued by changing assumptions after the experiment.

## Derivation, model and interpretation

A compact starting equation or relationship is **`x=L1*cos(q1)+L2*cos(q1+q2); y=L1*sin(q1)+L2*sin(q1+q2)`**. Define every symbol, include appropriate physical units and interpret the input and output quantities. The displayed relationship may be exact within an ideal geometry, a simplification of more complete dynamics, or a statistical approximation. Its status must be recorded. When the formula requires constant dimensions or a fixed reference frame, note these conditions explicitly. A coordinate-dependent result is meaningless until frame orientation and origin are identified.

**Implementation choice.** The lightest controller or cheapest sensor is not automatically the best solution. Complexity can improve diagnostics yet add failure modes and maintenance obligations. Define what a more advanced method would need to prove under representative loads, timing, environment and budget. In this lesson, look specifically at **two-link forward kinematics** rather than copying a generic control diagram. Ask which model terms could be measured directly. For each unmeasured quantity, give a method for identification and state what additional assumptions that method requires.

**Submodel and system boundary.** Geometry and identification Distinguish the ideal mathematical transformation from the mechanical or software device implementing it. For example, a calculated path requires a motion executor, a sensor-based termination rule and an independently assessed response to loss of communication. A fully specified algorithm can still be unsuitable for hardware when the necessary observations arrive too late.

## Worked calculation and numerical judgment

For L1=0.30 m, L2=0.20 m, q1=0°, q2=90°, the tip is at (0.30,0.20) m. Reproduce the substitution on paper, carry units through each stage and check the scale with an independent estimate. Precision in displayed decimal places does not demonstrate precise knowledge of link lengths, accelerations, friction coefficients or camera calibration. If inputs are rounded or synthetic, the outputs inherit those limitations; do not label them as measured robot performance.

**Traceable Verification audit.** Record firmware or model version, sensor calibration, test fixture revision and all rejected trials. Set acceptance thresholds before viewing the final traces. If a physical trial cannot be carried out safely, use simulation only and write the missing validation item explicitly. Extend the example by sweeping one independent input through a realistic range. Predict the qualitative trend before computing. Then change another input in a separate run; explain why changing both simultaneously would make causal interpretation weaker. Document any singular, discontinuous or saturating regime instead of hiding it by clipping a plot without explanation.

## Engineering interpretation and practical alternatives

The principal design trade-off is between algorithmic or mechanical capability and the evidence needed to operate it reliably. A high-speed option may increase throughput but increase motor heating and the consequence of a delayed stop. A sophisticated estimator may reduce drift under good lighting but fail abruptly when landmarks disappear. A carefully bounded simpler system can therefore outperform a more elaborate system under the actual operating conditions.

**Specific failure mechanism.** Using q2 as an absolute angle rather than relative joint angle corrupts the mapping. Do not respond automatically by increasing controller gain or changing a threshold. State what instrument or independent observation would reveal the difference between a bad model, incorrect calibration, measurement delay and a mechanical fault. Consider the consequences for neighboring subsystems: sensing errors affect grasp decisions, trajectory errors affect collision risk, and recovery behavior affects throughput.

**Integration perspective.** A coordinate transform is a mapping between explicitly named frames. Keep reference frames and calibrated tool center point in a ledger; use radians internally and specify the sign of every joint angle. Include joint hard stops, back-driving and reachable orientation in the feasibility analysis. For this topic, explicitly identify the preceding system function that supplies information and the following function that consumes the output. Give those interfaces names and units. State whether data is real time, sampled, batch-produced or only available after an operation ends. Wrong timing semantics can invalidate a mathematically correct equation.

## Verification protocol and evidence quality

A falsifiable check is: **Compare predicted tip coordinates against an independently measured grid at at least six joint configurations.** Establish independent observations whenever practical. Define an input range, number of trials, logging rate, expected trend, calibration reference and an acceptance threshold selected before analysis. At minimum include a nominal trial, a limiting case and an innocuous fault or missing-data condition. Physically hazardous failure injection requires qualified supervision and appropriate containment; otherwise conduct the test virtually and describe that limitation.

**Failure analysis.** Calibrating with no payload but operating at full payload can shift tool pose. Characterize systematic bias separately from random error; check the near-singular and workspace-boundary cases deliberately. When recorded evidence contradicts a prediction, preserve the discrepancy. Consider sensor bias, frame mismatch, uncontrolled load, aliasing, model order, compliance and operator intervention as competing explanations. One favorable trace does not validate a complete operating envelope. A reliable result needs repeatability across changed initial conditions and traceability to the configuration used for the test.

**Laboratory record.** Save model revision, input parameter table, raw data, units, frame definitions, timestamps, plot-generating script, calculated sensitivity and unsuccessful cases. Attach a short statement distinguishing simulation evidence from physical measurement and from a safety-related assessment. If equipment access is unavailable, provide a transparent synthetic test with expected results and avoid representing it as laboratory measurement.

## Exercises and design investigation

1. **Interpretation:** Derive or explain `x=L1*cos(q1)+L2*cos(q1+q2); y=L1*sin(q1)+L2*sin(q1+q2)` from relevant geometry, conservation laws or probability assumptions. Define all quantities, directions and units. Name a realistic boundary where it loses validity.
2. **Calculation:** Recompute the worked example without copying its result. Change the most important input by 10%; compare the resulting change against the original prediction, and explain when a first-order approximation is inadequate.
3. **Independent validation:** Construct a test of two-link forward kinematics using an independent reference. State three potential sources of measurement error and which observable can isolate at least two of them.
4. **Failure and safety:** Using the specified failure mechanism, write an expected fault signature, a detection threshold and a controlled fallback response. Distinguish the operating controller from a separately evaluated safety function.
5. **Applied synthesis:** For the unit's running case, document one viable alternative architecture, what it costs in complexity, and what evidence would justify choosing it over the baseline.

## Lesson summary and transfer

The central skill is to connect **two-link forward kinematics** to a physically meaningful model and a test that could disprove it. Carry the same units, coordinate conventions, uncertainty bounds and versioned acceptance criteria into the next lesson. Robot performance is judged by reproducible task outcomes under constrained conditions, not by an appealing ideal plot or the correctness of a single formula.


---

# U02-L03 — Inverse kinematics and reachability

**OpenSTEM Mechanical Engineering · Book 12: Robotics and Automation · Unit 2: Manipulators and Robot Kinematics.** Educational draft. All worked numbers are illustrative unless stated otherwise; do not use the calculations alone to certify a physical robot or protective system.

## Learning goal and context

This lesson asks how **inverse kinematics and reachability** affects a realistic robotic system. Its running design problem is: A two-link inspection robot must reach several sampling wells without touching the fixture. Derive forward and inverse relationships between joint states and task-space pose, then identify physical limits. Students must explain the physical mechanism, calculate an interpretable quantity, identify an assumption that could fail, and propose an observation that would distinguish competing explanations.

**Entry-level reasoning.** Inverse kinematics is a constraint problem that can yield no solution, one degenerate solution or multiple branches. Use the cosine law to solve a planar elbow angle and inspect the chosen branch against joint limits, interference and workspace boundaries. In practice, begin with the machine boundary and mark the frames, joint connections, sensing path and source of power. If a controller reports a requested value, determine whether the value is a command, a filtered estimate, an independently measured result or an offline ideal prediction. These are not interchangeable. Write a short claim that would be falsified by an observed counterexample, rather than a claim that can be rescued by changing assumptions after the experiment.

## Derivation, model and interpretation

A compact starting equation or relationship is **`cos(q2)=(x^2+y^2-L1^2-L2^2)/(2*L1*L2)`**. Define every symbol, include appropriate physical units and interpret the input and output quantities. The displayed relationship may be exact within an ideal geometry, a simplification of more complete dynamics, or a statistical approximation. Its status must be recorded. When the formula requires constant dimensions or a fixed reference frame, note these conditions explicitly. A coordinate-dependent result is meaningless until frame orientation and origin are identified.

**Operational consequence.** A robot cell has no isolated subsystem outcomes. A high-accuracy reach solution can be invalidated by perception latency, a good gripper can fail on a different surface, and a fast conveyor can overwhelm fault handling. Preserve interface specifications and model uncertainty across design stages. In this lesson, look specifically at **inverse kinematics and reachability** rather than copying a generic control diagram. Ask which model terms could be measured directly. For each unmeasured quantity, give a method for identification and state what additional assumptions that method requires.

**Submodel and system boundary.** Geometry and identification Distinguish the ideal mathematical transformation from the mechanical or software device implementing it. For example, a calculated path requires a motion executor, a sensor-based termination rule and an independently assessed response to loss of communication. A fully specified algorithm can still be unsuitable for hardware when the necessary observations arrive too late.

## Worked calculation and numerical judgment

For L1=0.30 m, L2=0.20 m and tip distance 0.40 m, cos(q2)=0.25, giving elbow angles about ±75.52°. Reproduce the substitution on paper, carry units through each stage and check the scale with an independent estimate. Precision in displayed decimal places does not demonstrate precise knowledge of link lengths, accelerations, friction coefficients or camera calibration. If inputs are rounded or synthetic, the outputs inherit those limitations; do not label them as measured robot performance.

**Dimensional Balance audit.** Perform a units check by substituting SI base units and showing both sides match. For angles, state that trigonometric functions expect radians unless explicitly converted. For probabilities, check output within [0,1], and for lengths or times reject negative values when the model defines only positive quantities. Extend the example by sweeping one independent input through a realistic range. Predict the qualitative trend before computing. Then change another input in a separate run; explain why changing both simultaneously would make causal interpretation weaker. Document any singular, discontinuous or saturating regime instead of hiding it by clipping a plot without explanation.

## Engineering interpretation and practical alternatives

The principal design trade-off is between algorithmic or mechanical capability and the evidence needed to operate it reliably. A high-speed option may increase throughput but increase motor heating and the consequence of a delayed stop. A sophisticated estimator may reduce drift under good lighting but fail abruptly when landmarks disappear. A carefully bounded simpler system can therefore outperform a more elaborate system under the actual operating conditions.

**Specific failure mechanism.** Clamping a target outside the annular reach disguises an infeasible request as a valid pose. Do not respond automatically by increasing controller gain or changing a threshold. State what instrument or independent observation would reveal the difference between a bad model, incorrect calibration, measurement delay and a mechanical fault. Consider the consequences for neighboring subsystems: sensing errors affect grasp decisions, trajectory errors affect collision risk, and recovery behavior affects throughput.

**Integration perspective.** A coordinate transform is a mapping between explicitly named frames. Keep reference frames and calibrated tool center point in a ledger; use radians internally and specify the sign of every joint angle. Include joint hard stops, back-driving and reachable orientation in the feasibility analysis. For this topic, explicitly identify the preceding system function that supplies information and the following function that consumes the output. Give those interfaces names and units. State whether data is real time, sampled, batch-produced or only available after an operation ends. Wrong timing semantics can invalidate a mathematically correct equation.

## Verification protocol and evidence quality

A falsifiable check is: **For every inverse candidate, substitute it into forward kinematics and reject joint-limit or obstacle violations.** Establish independent observations whenever practical. Define an input range, number of trials, logging rate, expected trend, calibration reference and an acceptance threshold selected before analysis. At minimum include a nominal trial, a limiting case and an innocuous fault or missing-data condition. Physically hazardous failure injection requires qualified supervision and appropriate containment; otherwise conduct the test virtually and describe that limitation.

**Failure analysis.** Calibrating with no payload but operating at full payload can shift tool pose. Characterize systematic bias separately from random error; check the near-singular and workspace-boundary cases deliberately. When recorded evidence contradicts a prediction, preserve the discrepancy. Consider sensor bias, frame mismatch, uncontrolled load, aliasing, model order, compliance and operator intervention as competing explanations. One favorable trace does not validate a complete operating envelope. A reliable result needs repeatability across changed initial conditions and traceability to the configuration used for the test.

**Laboratory record.** Save model revision, input parameter table, raw data, units, frame definitions, timestamps, plot-generating script, calculated sensitivity and unsuccessful cases. Attach a short statement distinguishing simulation evidence from physical measurement and from a safety-related assessment. If equipment access is unavailable, provide a transparent synthetic test with expected results and avoid representing it as laboratory measurement.

## Exercises and design investigation

1. **Interpretation:** Derive or explain `cos(q2)=(x^2+y^2-L1^2-L2^2)/(2*L1*L2)` from relevant geometry, conservation laws or probability assumptions. Define all quantities, directions and units. Name a realistic boundary where it loses validity.
2. **Calculation:** Recompute the worked example without copying its result. Change the most important input by 10%; compare the resulting change against the original prediction, and explain when a first-order approximation is inadequate.
3. **Independent validation:** Construct a test of inverse kinematics and reachability using an independent reference. State three potential sources of measurement error and which observable can isolate at least two of them.
4. **Failure and safety:** Using the specified failure mechanism, write an expected fault signature, a detection threshold and a controlled fallback response. Distinguish the operating controller from a separately evaluated safety function.
5. **Applied synthesis:** For the unit's running case, document one viable alternative architecture, what it costs in complexity, and what evidence would justify choosing it over the baseline.

## Lesson summary and transfer

The central skill is to connect **inverse kinematics and reachability** to a physically meaningful model and a test that could disprove it. Carry the same units, coordinate conventions, uncertainty bounds and versioned acceptance criteria into the next lesson. Robot performance is judged by reproducible task outcomes under constrained conditions, not by an appealing ideal plot or the correctness of a single formula.


---

# U02-L04 — Jacobians and velocity transmission

**OpenSTEM Mechanical Engineering · Book 12: Robotics and Automation · Unit 2: Manipulators and Robot Kinematics.** Educational draft. All worked numbers are illustrative unless stated otherwise; do not use the calculations alone to certify a physical robot or protective system.

## Learning goal and context

This lesson asks how **jacobians and velocity transmission** affects a realistic robotic system. Its running design problem is: A two-link inspection robot must reach several sampling wells without touching the fixture. Derive forward and inverse relationships between joint states and task-space pose, then identify physical limits. Students must explain the physical mechanism, calculate an interpretable quantity, identify an assumption that could fail, and propose an observation that would distinguish competing explanations.

**Entry-level reasoning.** The task-space velocity is J(q) times joint velocity. Singular configurations lose local motion authority in one direction or require excessive joint rates for a small Cartesian request. Condition numbers help but depend on physical scaling and task coordinates. In practice, begin with the machine boundary and mark the frames, joint connections, sensing path and source of power. If a controller reports a requested value, determine whether the value is a command, a filtered estimate, an independently measured result or an offline ideal prediction. These are not interchangeable. Write a short claim that would be falsified by an observed counterexample, rather than a claim that can be rescued by changing assumptions after the experiment.

## Derivation, model and interpretation

A compact starting equation or relationship is **`det(J)=L1*L2*sin(q2) for a planar 2R arm`**. Define every symbol, include appropriate physical units and interpret the input and output quantities. The displayed relationship may be exact within an ideal geometry, a simplification of more complete dynamics, or a statistical approximation. Its status must be recorded. When the formula requires constant dimensions or a fixed reference frame, note these conditions explicitly. A coordinate-dependent result is meaningless until frame orientation and origin are identified.

**Physical interpretation.** Place the governing relationship beside a sketch with vectors, directions and units. Identify which terms are geometry, which describe dynamics, and which are sensor-derived approximations. The useful question is not simply whether software returns a number, but whether the quantity corresponds to a well-defined physical observation. In this lesson, look specifically at **jacobians and velocity transmission** rather than copying a generic control diagram. Ask which model terms could be measured directly. For each unmeasured quantity, give a method for identification and state what additional assumptions that method requires.

**Submodel and system boundary.** Geometry and identification Distinguish the ideal mathematical transformation from the mechanical or software device implementing it. For example, a calculated path requires a motion executor, a sensor-based termination rule and an independently assessed response to loss of communication. A fully specified algorithm can still be unsuitable for hardware when the necessary observations arrive too late.

## Worked calculation and numerical judgment

At L1=0.30 m, L2=0.20 m, q2=90°, the determinant magnitude is 0.060 m², while at q2=0° it is zero. Reproduce the substitution on paper, carry units through each stage and check the scale with an independent estimate. Precision in displayed decimal places does not demonstrate precise knowledge of link lengths, accelerations, friction coefficients or camera calibration. If inputs are rounded or synthetic, the outputs inherit those limitations; do not label them as measured robot performance.

**Boundary Cases audit.** Check a zero-input limit, a typical operating point and a maximum planned input. Where derivatives exist, estimate local sensitivity to a 5% change. If the result changes sharply, prioritize a measurement of the sensitive parameter rather than increasing numerical precision elsewhere. Extend the example by sweeping one independent input through a realistic range. Predict the qualitative trend before computing. Then change another input in a separate run; explain why changing both simultaneously would make causal interpretation weaker. Document any singular, discontinuous or saturating regime instead of hiding it by clipping a plot without explanation.

## Engineering interpretation and practical alternatives

The principal design trade-off is between algorithmic or mechanical capability and the evidence needed to operate it reliably. A high-speed option may increase throughput but increase motor heating and the consequence of a delayed stop. A sophisticated estimator may reduce drift under good lighting but fail abruptly when landmarks disappear. A carefully bounded simpler system can therefore outperform a more elaborate system under the actual operating conditions.

**Specific failure mechanism.** A tip-speed command near full extension produces an unbounded ideal joint rate demand. Do not respond automatically by increasing controller gain or changing a threshold. State what instrument or independent observation would reveal the difference between a bad model, incorrect calibration, measurement delay and a mechanical fault. Consider the consequences for neighboring subsystems: sensing errors affect grasp decisions, trajectory errors affect collision risk, and recovery behavior affects throughput.

**Integration perspective.** A coordinate transform is a mapping between explicitly named frames. Keep reference frames and calibrated tool center point in a ledger; use radians internally and specify the sign of every joint angle. Include joint hard stops, back-driving and reachable orientation in the feasibility analysis. For this topic, explicitly identify the preceding system function that supplies information and the following function that consumes the output. Give those interfaces names and units. State whether data is real time, sampled, batch-produced or only available after an operation ends. Wrong timing semantics can invalidate a mathematically correct equation.

## Verification protocol and evidence quality

A falsifiable check is: **Sweep q2 and plot singular values or determinant while imposing explicit rate and joint limits.** Establish independent observations whenever practical. Define an input range, number of trials, logging rate, expected trend, calibration reference and an acceptance threshold selected before analysis. At minimum include a nominal trial, a limiting case and an innocuous fault or missing-data condition. Physically hazardous failure injection requires qualified supervision and appropriate containment; otherwise conduct the test virtually and describe that limitation.

**Failure analysis.** Calibrating with no payload but operating at full payload can shift tool pose. Characterize systematic bias separately from random error; check the near-singular and workspace-boundary cases deliberately. When recorded evidence contradicts a prediction, preserve the discrepancy. Consider sensor bias, frame mismatch, uncontrolled load, aliasing, model order, compliance and operator intervention as competing explanations. One favorable trace does not validate a complete operating envelope. A reliable result needs repeatability across changed initial conditions and traceability to the configuration used for the test.

**Laboratory record.** Save model revision, input parameter table, raw data, units, frame definitions, timestamps, plot-generating script, calculated sensitivity and unsuccessful cases. Attach a short statement distinguishing simulation evidence from physical measurement and from a safety-related assessment. If equipment access is unavailable, provide a transparent synthetic test with expected results and avoid representing it as laboratory measurement.

## Exercises and design investigation

1. **Interpretation:** Derive or explain `det(J)=L1*L2*sin(q2) for a planar 2R arm` from relevant geometry, conservation laws or probability assumptions. Define all quantities, directions and units. Name a realistic boundary where it loses validity.
2. **Calculation:** Recompute the worked example without copying its result. Change the most important input by 10%; compare the resulting change against the original prediction, and explain when a first-order approximation is inadequate.
3. **Independent validation:** Construct a test of jacobians and velocity transmission using an independent reference. State three potential sources of measurement error and which observable can isolate at least two of them.
4. **Failure and safety:** Using the specified failure mechanism, write an expected fault signature, a detection threshold and a controlled fallback response. Distinguish the operating controller from a separately evaluated safety function.
5. **Applied synthesis:** For the unit's running case, document one viable alternative architecture, what it costs in complexity, and what evidence would justify choosing it over the baseline.

## Lesson summary and transfer

The central skill is to connect **jacobians and velocity transmission** to a physically meaningful model and a test that could disprove it. Carry the same units, coordinate conventions, uncertainty bounds and versioned acceptance criteria into the next lesson. Robot performance is judged by reproducible task outcomes under constrained conditions, not by an appealing ideal plot or the correctness of a single formula.


---

# U02-L05 — Calibration, payload and workspace uncertainty

**OpenSTEM Mechanical Engineering · Book 12: Robotics and Automation · Unit 2: Manipulators and Robot Kinematics.** Educational draft. All worked numbers are illustrative unless stated otherwise; do not use the calculations alone to certify a physical robot or protective system.

## Learning goal and context

This lesson asks how **calibration, payload and workspace uncertainty** affects a realistic robotic system. Its running design problem is: A two-link inspection robot must reach several sampling wells without touching the fixture. Derive forward and inverse relationships between joint states and task-space pose, then identify physical limits. Students must explain the physical mechanism, calculate an interpretable quantity, identify an assumption that could fail, and propose an observation that would distinguish competing explanations.

**Entry-level reasoning.** Manufacturing tolerances, link bending, bearing backlash, tool-center-point offsets and camera registration shift the real reach from the ideal geometric model. Calibrate in the actual load and temperature envelope, and reserve clearance for worst-case uncertainty. In practice, begin with the machine boundary and mark the frames, joint connections, sensing path and source of power. If a controller reports a requested value, determine whether the value is a command, a filtered estimate, an independently measured result or an offline ideal prediction. These are not interchangeable. Write a short claim that would be falsified by an observed counterexample, rather than a claim that can be rescued by changing assumptions after the experiment.

## Derivation, model and interpretation

A compact starting equation or relationship is **`sigma_x ≈ sqrt((J11*sigma_q1)^2+(J12*sigma_q2)^2)`**. Define every symbol, include appropriate physical units and interpret the input and output quantities. The displayed relationship may be exact within an ideal geometry, a simplification of more complete dynamics, or a statistical approximation. Its status must be recorded. When the formula requires constant dimensions or a fixed reference frame, note these conditions explicitly. A coordinate-dependent result is meaningless until frame orientation and origin are identified.

**Failure boundaries.** Derive a nominal prediction, then ask how it changes near a singularity, saturation threshold, sensor outage or geometric boundary. Mathematical formulas sometimes remain numerically defined after their physical hypotheses are violated. The validity envelope should be written before any plot is treated as a performance forecast. In this lesson, look specifically at **calibration, payload and workspace uncertainty** rather than copying a generic control diagram. Ask which model terms could be measured directly. For each unmeasured quantity, give a method for identification and state what additional assumptions that method requires.

**Submodel and system boundary.** Geometry and identification Distinguish the ideal mathematical transformation from the mechanical or software device implementing it. For example, a calculated path requires a motion executor, a sensor-based termination rule and an independently assessed response to loss of communication. A fully specified algorithm can still be unsuitable for hardware when the necessary observations arrive too late.

## Worked calculation and numerical judgment

With independent contributions 0.4 mm and 0.3 mm to x error, root-sum-square uncertainty is 0.5 mm under the independence approximation. Reproduce the substitution on paper, carry units through each stage and check the scale with an independent estimate. Precision in displayed decimal places does not demonstrate precise knowledge of link lengths, accelerations, friction coefficients or camera calibration. If inputs are rounded or synthetic, the outputs inherit those limitations; do not label them as measured robot performance.

**Discretization audit.** Choose a simulation step that resolves the fastest physical phenomenon of interest. Check convergence with a smaller step and confirm that numerical artifacts do not explain apparent stability or contact behavior. Sampling rates must exceed the bandwidth of the phenomena they are claimed to detect. Extend the example by sweeping one independent input through a realistic range. Predict the qualitative trend before computing. Then change another input in a separate run; explain why changing both simultaneously would make causal interpretation weaker. Document any singular, discontinuous or saturating regime instead of hiding it by clipping a plot without explanation.

## Engineering interpretation and practical alternatives

The principal design trade-off is between algorithmic or mechanical capability and the evidence needed to operate it reliably. A high-speed option may increase throughput but increase motor heating and the consequence of a delayed stop. A sophisticated estimator may reduce drift under good lighting but fail abruptly when landmarks disappear. A carefully bounded simpler system can therefore outperform a more elaborate system under the actual operating conditions.

**Specific failure mechanism.** Calibrating without the production end effector produces systematic placement error under load. Do not respond automatically by increasing controller gain or changing a threshold. State what instrument or independent observation would reveal the difference between a bad model, incorrect calibration, measurement delay and a mechanical fault. Consider the consequences for neighboring subsystems: sensing errors affect grasp decisions, trajectory errors affect collision risk, and recovery behavior affects throughput.

**Integration perspective.** A coordinate transform is a mapping between explicitly named frames. Keep reference frames and calibrated tool center point in a ledger; use radians internally and specify the sign of every joint angle. Include joint hard stops, back-driving and reachable orientation in the feasibility analysis. For this topic, explicitly identify the preceding system function that supplies information and the following function that consumes the output. Give those interfaces names and units. State whether data is real time, sampled, batch-produced or only available after an operation ends. Wrong timing semantics can invalidate a mathematically correct equation.

## Verification protocol and evidence quality

A falsifiable check is: **Use a withheld set of target points to quantify bias, repeatability and drift separately.** Establish independent observations whenever practical. Define an input range, number of trials, logging rate, expected trend, calibration reference and an acceptance threshold selected before analysis. At minimum include a nominal trial, a limiting case and an innocuous fault or missing-data condition. Physically hazardous failure injection requires qualified supervision and appropriate containment; otherwise conduct the test virtually and describe that limitation.

**Failure analysis.** Calibrating with no payload but operating at full payload can shift tool pose. Characterize systematic bias separately from random error; check the near-singular and workspace-boundary cases deliberately. When recorded evidence contradicts a prediction, preserve the discrepancy. Consider sensor bias, frame mismatch, uncontrolled load, aliasing, model order, compliance and operator intervention as competing explanations. One favorable trace does not validate a complete operating envelope. A reliable result needs repeatability across changed initial conditions and traceability to the configuration used for the test.

**Laboratory record.** Save model revision, input parameter table, raw data, units, frame definitions, timestamps, plot-generating script, calculated sensitivity and unsuccessful cases. Attach a short statement distinguishing simulation evidence from physical measurement and from a safety-related assessment. If equipment access is unavailable, provide a transparent synthetic test with expected results and avoid representing it as laboratory measurement.

## Exercises and design investigation

1. **Interpretation:** Derive or explain `sigma_x ≈ sqrt((J11*sigma_q1)^2+(J12*sigma_q2)^2)` from relevant geometry, conservation laws or probability assumptions. Define all quantities, directions and units. Name a realistic boundary where it loses validity.
2. **Calculation:** Recompute the worked example without copying its result. Change the most important input by 10%; compare the resulting change against the original prediction, and explain when a first-order approximation is inadequate.
3. **Independent validation:** Construct a test of calibration, payload and workspace uncertainty using an independent reference. State three potential sources of measurement error and which observable can isolate at least two of them.
4. **Failure and safety:** Using the specified failure mechanism, write an expected fault signature, a detection threshold and a controlled fallback response. Distinguish the operating controller from a separately evaluated safety function.
5. **Applied synthesis:** For the unit's running case, document one viable alternative architecture, what it costs in complexity, and what evidence would justify choosing it over the baseline.

## Lesson summary and transfer

The central skill is to connect **calibration, payload and workspace uncertainty** to a physically meaningful model and a test that could disprove it. Carry the same units, coordinate conventions, uncertainty bounds and versioned acceptance criteria into the next lesson. Robot performance is judged by reproducible task outcomes under constrained conditions, not by an appealing ideal plot or the correctness of a single formula.


---

