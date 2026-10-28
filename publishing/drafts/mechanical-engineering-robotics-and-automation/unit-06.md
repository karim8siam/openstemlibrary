# Unit 06: Perception, Navigation and Decision-Making

**Course Code**: ROB 406 · **Level**: Advanced Undergraduate Engineering

## Unit Overview & Physical Foundations

This comprehensive university textbook unit covers the theoretical framework, physical modeling, mathematical governing equations, and engineering applications of **Perception, Navigation and Decision-Making**.

# U06-L01 — Cameras, depth sensors and calibration

**OpenSTEM Mechanical Engineering · Book 12: Robotics and Automation · Unit 6: Perception, Navigation and Decision-Making.** Educational draft. All worked numbers are illustrative unless stated otherwise; do not use the calculations alone to certify a physical robot or protective system.

## Learning goal and context

This lesson asks how **cameras, depth sensors and calibration** affects a realistic robotic system. Its running design problem is: A mobile manipulator locates items on shelves and chooses a feasible retrieval order. Connect measurements to decisions while quantifying false detections, environmental variability and planning uncertainty. Students must explain the physical mechanism, calculate an interpretable quantity, identify an assumption that could fail, and propose an observation that would distinguish competing explanations.

**Entry-level reasoning.** Intrinsic camera calibration maps rays to pixels; extrinsic calibration locates the camera frame relative to the robot. Depth triangulation depends on geometry and surface quality, and occlusion is not absence. Plan calibration checks across operating distance. In practice, begin with the machine boundary and mark the frames, joint connections, sensing path and source of power. If a controller reports a requested value, determine whether the value is a command, a filtered estimate, an independently measured result or an offline ideal prediction. These are not interchangeable. Write a short claim that would be falsified by an observed counterexample, rather than a claim that can be rescued by changing assumptions after the experiment.

## Derivation, model and interpretation

A compact starting equation or relationship is **`Z = f * baseline / disparity for ideal rectified stereo`**. Define every symbol, include appropriate physical units and interpret the input and output quantities. The displayed relationship may be exact within an ideal geometry, a simplification of more complete dynamics, or a statistical approximation. Its status must be recorded. When the formula requires constant dimensions or a fixed reference frame, note these conditions explicitly. A coordinate-dependent result is meaningless until frame orientation and origin are identified.

**Operational consequence.** A robot cell has no isolated subsystem outcomes. A high-accuracy reach solution can be invalidated by perception latency, a good gripper can fail on a different surface, and a fast conveyor can overwhelm fault handling. Preserve interface specifications and model uncertainty across design stages. In this lesson, look specifically at **cameras, depth sensors and calibration** rather than copying a generic control diagram. Ask which model terms could be measured directly. For each unmeasured quantity, give a method for identification and state what additional assumptions that method requires.

**Submodel and system boundary.** Inference under observation limits Distinguish the ideal mathematical transformation from the mechanical or software device implementing it. For example, a calculated path requires a motion executor, a sensor-based termination rule and an independently assessed response to loss of communication. A fully specified algorithm can still be unsuitable for hardware when the necessary observations arrive too late.

## Worked calculation and numerical judgment

For f=500 pixel, baseline=0.10 m and disparity=50 pixel, depth is 1.0 m in the ideal model. Reproduce the substitution on paper, carry units through each stage and check the scale with an independent estimate. Precision in displayed decimal places does not demonstrate precise knowledge of link lengths, accelerations, friction coefficients or camera calibration. If inputs are rounded or synthetic, the outputs inherit those limitations; do not label them as measured robot performance.

**Discretization audit.** Choose a simulation step that resolves the fastest physical phenomenon of interest. Check convergence with a smaller step and confirm that numerical artifacts do not explain apparent stability or contact behavior. Sampling rates must exceed the bandwidth of the phenomena they are claimed to detect. Extend the example by sweeping one independent input through a realistic range. Predict the qualitative trend before computing. Then change another input in a separate run; explain why changing both simultaneously would make causal interpretation weaker. Document any singular, discontinuous or saturating regime instead of hiding it by clipping a plot without explanation.

## Engineering interpretation and practical alternatives

The principal design trade-off is between algorithmic or mechanical capability and the evidence needed to operate it reliably. A high-speed option may increase throughput but increase motor heating and the consequence of a delayed stop. A sophisticated estimator may reduce drift under good lighting but fail abruptly when landmarks disappear. A carefully bounded simpler system can therefore outperform a more elaborate system under the actual operating conditions.

**Specific failure mechanism.** Reflective packaging yields unreliable disparity that is incorrectly treated as precise depth. Do not respond automatically by increasing controller gain or changing a threshold. State what instrument or independent observation would reveal the difference between a bad model, incorrect calibration, measurement delay and a mechanical fault. Consider the consequences for neighboring subsystems: sensing errors affect grasp decisions, trajectory errors affect collision risk, and recovery behavior affects throughput.

**Integration perspective.** Treat measurements as evidence with false alarms and missed detections, not perfect world state. Report class distributions and the conditions under which confidence is calibrated. Planning has a safety boundary independent of nominal vision output. For this topic, explicitly identify the preceding system function that supplies information and the following function that consumes the output. Give those interfaces names and units. State whether data is real time, sampled, batch-produced or only available after an operation ends. Wrong timing semantics can invalidate a mathematically correct equation.

## Verification protocol and evidence quality

A falsifiable check is: **Measure depth error on independent flat and textured targets across the intended working range.** Establish independent observations whenever practical. Define an input range, number of trials, logging rate, expected trend, calibration reference and an acceptance threshold selected before analysis. At minimum include a nominal trial, a limiting case and an innocuous fault or missing-data condition. Physically hazardous failure injection requires qualified supervision and appropriate containment; otherwise conduct the test virtually and describe that limitation.

**Failure analysis.** Changing lighting and product mix are distinct sources of distribution shift. Test held-out object materials, multiple camera positions and delayed detections before trusting any automation claim. When recorded evidence contradicts a prediction, preserve the discrepancy. Consider sensor bias, frame mismatch, uncontrolled load, aliasing, model order, compliance and operator intervention as competing explanations. One favorable trace does not validate a complete operating envelope. A reliable result needs repeatability across changed initial conditions and traceability to the configuration used for the test.

**Laboratory record.** Save model revision, input parameter table, raw data, units, frame definitions, timestamps, plot-generating script, calculated sensitivity and unsuccessful cases. Attach a short statement distinguishing simulation evidence from physical measurement and from a safety-related assessment. If equipment access is unavailable, provide a transparent synthetic test with expected results and avoid representing it as laboratory measurement.

## Exercises and design investigation

1. **Interpretation:** Derive or explain `Z = f * baseline / disparity for ideal rectified stereo` from relevant geometry, conservation laws or probability assumptions. Define all quantities, directions and units. Name a realistic boundary where it loses validity.
2. **Calculation:** Recompute the worked example without copying its result. Change the most important input by 10%; compare the resulting change against the original prediction, and explain when a first-order approximation is inadequate.
3. **Independent validation:** Construct a test of cameras, depth sensors and calibration using an independent reference. State three potential sources of measurement error and which observable can isolate at least two of them.
4. **Failure and safety:** Using the specified failure mechanism, write an expected fault signature, a detection threshold and a controlled fallback response. Distinguish the operating controller from a separately evaluated safety function.
5. **Applied synthesis:** For the unit's running case, document one viable alternative architecture, what it costs in complexity, and what evidence would justify choosing it over the baseline.

## Lesson summary and transfer

The central skill is to connect **cameras, depth sensors and calibration** to a physically meaningful model and a test that could disprove it. Carry the same units, coordinate conventions, uncertainty bounds and versioned acceptance criteria into the next lesson. Robot performance is judged by reproducible task outcomes under constrained conditions, not by an appealing ideal plot or the correctness of a single formula.


---

# U06-L02 — Detection confidence and classification

**OpenSTEM Mechanical Engineering · Book 12: Robotics and Automation · Unit 6: Perception, Navigation and Decision-Making.** Educational draft. All worked numbers are illustrative unless stated otherwise; do not use the calculations alone to certify a physical robot or protective system.

## Learning goal and context

This lesson asks how **detection confidence and classification** affects a realistic robotic system. Its running design problem is: A mobile manipulator locates items on shelves and chooses a feasible retrieval order. Connect measurements to decisions while quantifying false detections, environmental variability and planning uncertainty. Students must explain the physical mechanism, calculate an interpretable quantity, identify an assumption that could fail, and propose an observation that would distinguish competing explanations.

**Entry-level reasoning.** A neural classifier score is not automatically a calibrated probability. Detection threshold trades false positives against missed objects, influenced by lighting, distribution shift and unseen product families. Split evaluation data by operating condition, not merely random frames. In practice, begin with the machine boundary and mark the frames, joint connections, sensing path and source of power. If a controller reports a requested value, determine whether the value is a command, a filtered estimate, an independently measured result or an offline ideal prediction. These are not interchangeable. Write a short claim that would be falsified by an observed counterexample, rather than a claim that can be rescued by changing assumptions after the experiment.

## Derivation, model and interpretation

A compact starting equation or relationship is **`precision=TP/(TP+FP)`**. Define every symbol, include appropriate physical units and interpret the input and output quantities. The displayed relationship may be exact within an ideal geometry, a simplification of more complete dynamics, or a statistical approximation. Its status must be recorded. When the formula requires constant dimensions or a fixed reference frame, note these conditions explicitly. A coordinate-dependent result is meaningless until frame orientation and origin are identified.

**Physical interpretation.** Place the governing relationship beside a sketch with vectors, directions and units. Identify which terms are geometry, which describe dynamics, and which are sensor-derived approximations. The useful question is not simply whether software returns a number, but whether the quantity corresponds to a well-defined physical observation. In this lesson, look specifically at **detection confidence and classification** rather than copying a generic control diagram. Ask which model terms could be measured directly. For each unmeasured quantity, give a method for identification and state what additional assumptions that method requires.

**Submodel and system boundary.** Inference under observation limits Distinguish the ideal mathematical transformation from the mechanical or software device implementing it. For example, a calculated path requires a motion executor, a sensor-based termination rule and an independently assessed response to loss of communication. A fully specified algorithm can still be unsuitable for hardware when the necessary observations arrive too late.

## Worked calculation and numerical judgment

With 80 true positives and 20 false positives, sample precision is 0.80; this does not measure recall without false negatives. Reproduce the substitution on paper, carry units through each stage and check the scale with an independent estimate. Precision in displayed decimal places does not demonstrate precise knowledge of link lengths, accelerations, friction coefficients or camera calibration. If inputs are rounded or synthetic, the outputs inherit those limitations; do not label them as measured robot performance.

**Uncertainty audit.** Differentiate precision from accuracy: repeated values near one another may share a systematic offset. Use replicated trials and a calibration reference, and consider correlations when combining uncertainties. An error bound must be linked to a defined operating range. Extend the example by sweeping one independent input through a realistic range. Predict the qualitative trend before computing. Then change another input in a separate run; explain why changing both simultaneously would make causal interpretation weaker. Document any singular, discontinuous or saturating regime instead of hiding it by clipping a plot without explanation.

## Engineering interpretation and practical alternatives

The principal design trade-off is between algorithmic or mechanical capability and the evidence needed to operate it reliably. A high-speed option may increase throughput but increase motor heating and the consequence of a delayed stop. A sophisticated estimator may reduce drift under good lighting but fail abruptly when landmarks disappear. A carefully bounded simpler system can therefore outperform a more elaborate system under the actual operating conditions.

**Specific failure mechanism.** Training and testing on near-duplicate frames exaggerates real-world recognition reliability. Do not respond automatically by increasing controller gain or changing a threshold. State what instrument or independent observation would reveal the difference between a bad model, incorrect calibration, measurement delay and a mechanical fault. Consider the consequences for neighboring subsystems: sensing errors affect grasp decisions, trajectory errors affect collision risk, and recovery behavior affects throughput.

**Integration perspective.** Treat measurements as evidence with false alarms and missed detections, not perfect world state. Report class distributions and the conditions under which confidence is calibrated. Planning has a safety boundary independent of nominal vision output. For this topic, explicitly identify the preceding system function that supplies information and the following function that consumes the output. Give those interfaces names and units. State whether data is real time, sampled, batch-produced or only available after an operation ends. Wrong timing semantics can invalidate a mathematically correct equation.

## Verification protocol and evidence quality

A falsifiable check is: **Report confusion matrices by object type and lighting condition on held-out sessions.** Establish independent observations whenever practical. Define an input range, number of trials, logging rate, expected trend, calibration reference and an acceptance threshold selected before analysis. At minimum include a nominal trial, a limiting case and an innocuous fault or missing-data condition. Physically hazardous failure injection requires qualified supervision and appropriate containment; otherwise conduct the test virtually and describe that limitation.

**Failure analysis.** Changing lighting and product mix are distinct sources of distribution shift. Test held-out object materials, multiple camera positions and delayed detections before trusting any automation claim. When recorded evidence contradicts a prediction, preserve the discrepancy. Consider sensor bias, frame mismatch, uncontrolled load, aliasing, model order, compliance and operator intervention as competing explanations. One favorable trace does not validate a complete operating envelope. A reliable result needs repeatability across changed initial conditions and traceability to the configuration used for the test.

**Laboratory record.** Save model revision, input parameter table, raw data, units, frame definitions, timestamps, plot-generating script, calculated sensitivity and unsuccessful cases. Attach a short statement distinguishing simulation evidence from physical measurement and from a safety-related assessment. If equipment access is unavailable, provide a transparent synthetic test with expected results and avoid representing it as laboratory measurement.

## Exercises and design investigation

1. **Interpretation:** Derive or explain `precision=TP/(TP+FP)` from relevant geometry, conservation laws or probability assumptions. Define all quantities, directions and units. Name a realistic boundary where it loses validity.
2. **Calculation:** Recompute the worked example without copying its result. Change the most important input by 10%; compare the resulting change against the original prediction, and explain when a first-order approximation is inadequate.
3. **Independent validation:** Construct a test of detection confidence and classification using an independent reference. State three potential sources of measurement error and which observable can isolate at least two of them.
4. **Failure and safety:** Using the specified failure mechanism, write an expected fault signature, a detection threshold and a controlled fallback response. Distinguish the operating controller from a separately evaluated safety function.
5. **Applied synthesis:** For the unit's running case, document one viable alternative architecture, what it costs in complexity, and what evidence would justify choosing it over the baseline.

## Lesson summary and transfer

The central skill is to connect **detection confidence and classification** to a physically meaningful model and a test that could disprove it. Carry the same units, coordinate conventions, uncertainty bounds and versioned acceptance criteria into the next lesson. Robot performance is judged by reproducible task outcomes under constrained conditions, not by an appealing ideal plot or the correctness of a single formula.


---

# U06-L03 — Graph and grid path planning

**OpenSTEM Mechanical Engineering · Book 12: Robotics and Automation · Unit 6: Perception, Navigation and Decision-Making.** Educational draft. All worked numbers are illustrative unless stated otherwise; do not use the calculations alone to certify a physical robot or protective system.

## Learning goal and context

This lesson asks how **graph and grid path planning** affects a realistic robotic system. Its running design problem is: A mobile manipulator locates items on shelves and chooses a feasible retrieval order. Connect measurements to decisions while quantifying false detections, environmental variability and planning uncertainty. Students must explain the physical mechanism, calculate an interpretable quantity, identify an assumption that could fail, and propose an observation that would distinguish competing explanations.

**Entry-level reasoning.** Dijkstra search finds shortest paths with nonnegative edge costs; A* can use an admissible heuristic to guide search without sacrificing optimality under its assumptions. A waypoint graph is only as complete as its collision-validated edges. In practice, begin with the machine boundary and mark the frames, joint connections, sensing path and source of power. If a controller reports a requested value, determine whether the value is a command, a filtered estimate, an independently measured result or an offline ideal prediction. These are not interchangeable. Write a short claim that would be falsified by an observed counterexample, rather than a claim that can be rescued by changing assumptions after the experiment.

## Derivation, model and interpretation

A compact starting equation or relationship is **`h_manhattan=abs(dx)+abs(dy) on four-neighbor unit grid`**. Define every symbol, include appropriate physical units and interpret the input and output quantities. The displayed relationship may be exact within an ideal geometry, a simplification of more complete dynamics, or a statistical approximation. Its status must be recorded. When the formula requires constant dimensions or a fixed reference frame, note these conditions explicitly. A coordinate-dependent result is meaningless until frame orientation and origin are identified.

**Failure boundaries.** Derive a nominal prediction, then ask how it changes near a singularity, saturation threshold, sensor outage or geometric boundary. Mathematical formulas sometimes remain numerically defined after their physical hypotheses are violated. The validity envelope should be written before any plot is treated as a performance forecast. In this lesson, look specifically at **graph and grid path planning** rather than copying a generic control diagram. Ask which model terms could be measured directly. For each unmeasured quantity, give a method for identification and state what additional assumptions that method requires.

**Submodel and system boundary.** Inference under observation limits Distinguish the ideal mathematical transformation from the mechanical or software device implementing it. For example, a calculated path requires a motion executor, a sensor-based termination rule and an independently assessed response to loss of communication. A fully specified algorithm can still be unsuitable for hardware when the necessary observations arrive too late.

## Worked calculation and numerical judgment

For relative cell offsets dx=4, dy=3, Manhattan lower bound is seven unit moves when diagonal actions are disallowed. Reproduce the substitution on paper, carry units through each stage and check the scale with an independent estimate. Precision in displayed decimal places does not demonstrate precise knowledge of link lengths, accelerations, friction coefficients or camera calibration. If inputs are rounded or synthetic, the outputs inherit those limitations; do not label them as measured robot performance.

**Traceable Verification audit.** Record firmware or model version, sensor calibration, test fixture revision and all rejected trials. Set acceptance thresholds before viewing the final traces. If a physical trial cannot be carried out safely, use simulation only and write the missing validation item explicitly. Extend the example by sweeping one independent input through a realistic range. Predict the qualitative trend before computing. Then change another input in a separate run; explain why changing both simultaneously would make causal interpretation weaker. Document any singular, discontinuous or saturating regime instead of hiding it by clipping a plot without explanation.

## Engineering interpretation and practical alternatives

The principal design trade-off is between algorithmic or mechanical capability and the evidence needed to operate it reliably. A high-speed option may increase throughput but increase motor heating and the consequence of a delayed stop. A sophisticated estimator may reduce drift under good lighting but fail abruptly when landmarks disappear. A carefully bounded simpler system can therefore outperform a more elaborate system under the actual operating conditions.

**Specific failure mechanism.** Allowing diagonal movements while keeping an incompatible heuristic breaks the optimality argument. Do not respond automatically by increasing controller gain or changing a threshold. State what instrument or independent observation would reveal the difference between a bad model, incorrect calibration, measurement delay and a mechanical fault. Consider the consequences for neighboring subsystems: sensing errors affect grasp decisions, trajectory errors affect collision risk, and recovery behavior affects throughput.

**Integration perspective.** Treat measurements as evidence with false alarms and missed detections, not perfect world state. Report class distributions and the conditions under which confidence is calibrated. Planning has a safety boundary independent of nominal vision output. For this topic, explicitly identify the preceding system function that supplies information and the following function that consumes the output. Give those interfaces names and units. State whether data is real time, sampled, batch-produced or only available after an operation ends. Wrong timing semantics can invalidate a mathematically correct equation.

## Verification protocol and evidence quality

A falsifiable check is: **Compare routes against exhaustive small-grid shortest paths including blocked corners.** Establish independent observations whenever practical. Define an input range, number of trials, logging rate, expected trend, calibration reference and an acceptance threshold selected before analysis. At minimum include a nominal trial, a limiting case and an innocuous fault or missing-data condition. Physically hazardous failure injection requires qualified supervision and appropriate containment; otherwise conduct the test virtually and describe that limitation.

**Failure analysis.** Changing lighting and product mix are distinct sources of distribution shift. Test held-out object materials, multiple camera positions and delayed detections before trusting any automation claim. When recorded evidence contradicts a prediction, preserve the discrepancy. Consider sensor bias, frame mismatch, uncontrolled load, aliasing, model order, compliance and operator intervention as competing explanations. One favorable trace does not validate a complete operating envelope. A reliable result needs repeatability across changed initial conditions and traceability to the configuration used for the test.

**Laboratory record.** Save model revision, input parameter table, raw data, units, frame definitions, timestamps, plot-generating script, calculated sensitivity and unsuccessful cases. Attach a short statement distinguishing simulation evidence from physical measurement and from a safety-related assessment. If equipment access is unavailable, provide a transparent synthetic test with expected results and avoid representing it as laboratory measurement.

## Exercises and design investigation

1. **Interpretation:** Derive or explain `h_manhattan=abs(dx)+abs(dy) on four-neighbor unit grid` from relevant geometry, conservation laws or probability assumptions. Define all quantities, directions and units. Name a realistic boundary where it loses validity.
2. **Calculation:** Recompute the worked example without copying its result. Change the most important input by 10%; compare the resulting change against the original prediction, and explain when a first-order approximation is inadequate.
3. **Independent validation:** Construct a test of graph and grid path planning using an independent reference. State three potential sources of measurement error and which observable can isolate at least two of them.
4. **Failure and safety:** Using the specified failure mechanism, write an expected fault signature, a detection threshold and a controlled fallback response. Distinguish the operating controller from a separately evaluated safety function.
5. **Applied synthesis:** For the unit's running case, document one viable alternative architecture, what it costs in complexity, and what evidence would justify choosing it over the baseline.

## Lesson summary and transfer

The central skill is to connect **graph and grid path planning** to a physically meaningful model and a test that could disprove it. Carry the same units, coordinate conventions, uncertainty bounds and versioned acceptance criteria into the next lesson. Robot performance is judged by reproducible task outcomes under constrained conditions, not by an appealing ideal plot or the correctness of a single formula.


---

# U06-L04 — Reactive obstacle avoidance

**OpenSTEM Mechanical Engineering · Book 12: Robotics and Automation · Unit 6: Perception, Navigation and Decision-Making.** Educational draft. All worked numbers are illustrative unless stated otherwise; do not use the calculations alone to certify a physical robot or protective system.

## Learning goal and context

This lesson asks how **reactive obstacle avoidance** affects a realistic robotic system. Its running design problem is: A mobile manipulator locates items on shelves and chooses a feasible retrieval order. Connect measurements to decisions while quantifying false detections, environmental variability and planning uncertainty. Students must explain the physical mechanism, calculate an interpretable quantity, identify an assumption that could fail, and propose an observation that would distinguish competing explanations.

**Entry-level reasoning.** Reactive control uses immediate observations to reduce collision likelihood; it cannot guarantee global goal reachability. Braking distance, observation delay, field of view and moving obstacles define a dynamic safety envelope. Keep independent protective functions separate. In practice, begin with the machine boundary and mark the frames, joint connections, sensing path and source of power. If a controller reports a requested value, determine whether the value is a command, a filtered estimate, an independently measured result or an offline ideal prediction. These are not interchangeable. Write a short claim that would be falsified by an observed counterexample, rather than a claim that can be rescued by changing assumptions after the experiment.

## Derivation, model and interpretation

A compact starting equation or relationship is **`d_stop=v*latency+v^2/(2*a)`**. Define every symbol, include appropriate physical units and interpret the input and output quantities. The displayed relationship may be exact within an ideal geometry, a simplification of more complete dynamics, or a statistical approximation. Its status must be recorded. When the formula requires constant dimensions or a fixed reference frame, note these conditions explicitly. A coordinate-dependent result is meaningless until frame orientation and origin are identified.

**Identification and calibration.** A single fitted parameter can conceal bias in a different component. If friction, encoder scale and controller gain all change together, the resulting trace does not identify their separate causes. Change a controlled input and compare with an independent instrument where possible. In this lesson, look specifically at **reactive obstacle avoidance** rather than copying a generic control diagram. Ask which model terms could be measured directly. For each unmeasured quantity, give a method for identification and state what additional assumptions that method requires.

**Submodel and system boundary.** Inference under observation limits Distinguish the ideal mathematical transformation from the mechanical or software device implementing it. For example, a calculated path requires a motion executor, a sensor-based termination rule and an independently assessed response to loss of communication. A fully specified algorithm can still be unsuitable for hardware when the necessary observations arrive too late.

## Worked calculation and numerical judgment

At speed 0.80 m/s, delay 0.10 s and deceleration 1.0 m/s², ideal stop distance is 0.40 m before uncertainties. Reproduce the substitution on paper, carry units through each stage and check the scale with an independent estimate. Precision in displayed decimal places does not demonstrate precise knowledge of link lengths, accelerations, friction coefficients or camera calibration. If inputs are rounded or synthetic, the outputs inherit those limitations; do not label them as measured robot performance.

**Dimensional Balance audit.** Perform a units check by substituting SI base units and showing both sides match. For angles, state that trigonometric functions expect radians unless explicitly converted. For probabilities, check output within [0,1], and for lengths or times reject negative values when the model defines only positive quantities. Extend the example by sweeping one independent input through a realistic range. Predict the qualitative trend before computing. Then change another input in a separate run; explain why changing both simultaneously would make causal interpretation weaker. Document any singular, discontinuous or saturating regime instead of hiding it by clipping a plot without explanation.

## Engineering interpretation and practical alternatives

The principal design trade-off is between algorithmic or mechanical capability and the evidence needed to operate it reliably. A high-speed option may increase throughput but increase motor heating and the consequence of a delayed stop. A sophisticated estimator may reduce drift under good lighting but fail abruptly when landmarks disappear. A carefully bounded simpler system can therefore outperform a more elaborate system under the actual operating conditions.

**Specific failure mechanism.** A sensor sees the obstacle only after it has entered the modeled stopping distance. Do not respond automatically by increasing controller gain or changing a threshold. State what instrument or independent observation would reveal the difference between a bad model, incorrect calibration, measurement delay and a mechanical fault. Consider the consequences for neighboring subsystems: sensing errors affect grasp decisions, trajectory errors affect collision risk, and recovery behavior affects throughput.

**Integration perspective.** Treat measurements as evidence with false alarms and missed detections, not perfect world state. Report class distributions and the conditions under which confidence is calibrated. Planning has a safety boundary independent of nominal vision output. For this topic, explicitly identify the preceding system function that supplies information and the following function that consumes the output. Give those interfaces names and units. State whether data is real time, sampled, batch-produced or only available after an operation ends. Wrong timing semantics can invalidate a mathematically correct equation.

## Verification protocol and evidence quality

A falsifiable check is: **Use contained low-energy simulations across obstacle distances and independently evaluate detection latency.** Establish independent observations whenever practical. Define an input range, number of trials, logging rate, expected trend, calibration reference and an acceptance threshold selected before analysis. At minimum include a nominal trial, a limiting case and an innocuous fault or missing-data condition. Physically hazardous failure injection requires qualified supervision and appropriate containment; otherwise conduct the test virtually and describe that limitation.

**Failure analysis.** Changing lighting and product mix are distinct sources of distribution shift. Test held-out object materials, multiple camera positions and delayed detections before trusting any automation claim. When recorded evidence contradicts a prediction, preserve the discrepancy. Consider sensor bias, frame mismatch, uncontrolled load, aliasing, model order, compliance and operator intervention as competing explanations. One favorable trace does not validate a complete operating envelope. A reliable result needs repeatability across changed initial conditions and traceability to the configuration used for the test.

**Laboratory record.** Save model revision, input parameter table, raw data, units, frame definitions, timestamps, plot-generating script, calculated sensitivity and unsuccessful cases. Attach a short statement distinguishing simulation evidence from physical measurement and from a safety-related assessment. If equipment access is unavailable, provide a transparent synthetic test with expected results and avoid representing it as laboratory measurement.

## Exercises and design investigation

1. **Interpretation:** Derive or explain `d_stop=v*latency+v^2/(2*a)` from relevant geometry, conservation laws or probability assumptions. Define all quantities, directions and units. Name a realistic boundary where it loses validity.
2. **Calculation:** Recompute the worked example without copying its result. Change the most important input by 10%; compare the resulting change against the original prediction, and explain when a first-order approximation is inadequate.
3. **Independent validation:** Construct a test of reactive obstacle avoidance using an independent reference. State three potential sources of measurement error and which observable can isolate at least two of them.
4. **Failure and safety:** Using the specified failure mechanism, write an expected fault signature, a detection threshold and a controlled fallback response. Distinguish the operating controller from a separately evaluated safety function.
5. **Applied synthesis:** For the unit's running case, document one viable alternative architecture, what it costs in complexity, and what evidence would justify choosing it over the baseline.

## Lesson summary and transfer

The central skill is to connect **reactive obstacle avoidance** to a physically meaningful model and a test that could disprove it. Carry the same units, coordinate conventions, uncertainty bounds and versioned acceptance criteria into the next lesson. Robot performance is judged by reproducible task outcomes under constrained conditions, not by an appealing ideal plot or the correctness of a single formula.


---

# U06-L05 — Task planning and finite-state execution

**OpenSTEM Mechanical Engineering · Book 12: Robotics and Automation · Unit 6: Perception, Navigation and Decision-Making.** Educational draft. All worked numbers are illustrative unless stated otherwise; do not use the calculations alone to certify a physical robot or protective system.

## Learning goal and context

This lesson asks how **task planning and finite-state execution** affects a realistic robotic system. Its running design problem is: A mobile manipulator locates items on shelves and chooses a feasible retrieval order. Connect measurements to decisions while quantifying false detections, environmental variability and planning uncertainty. Students must explain the physical mechanism, calculate an interpretable quantity, identify an assumption that could fail, and propose an observation that would distinguish competing explanations.

**Entry-level reasoning.** A complete task includes approach, confirmation, grasp, verification, transfer, release and recovery. State transitions should require bounded timeouts, sensor evidence and idempotent commands; retries can worsen a jam unless they are limited. In practice, begin with the machine boundary and mark the frames, joint connections, sensing path and source of power. If a controller reports a requested value, determine whether the value is a command, a filtered estimate, an independently measured result or an offline ideal prediction. These are not interchangeable. Write a short claim that would be falsified by an observed counterexample, rather than a claim that can be rescued by changing assumptions after the experiment.

## Derivation, model and interpretation

A compact starting equation or relationship is **`expected_attempts=1/p_success for independent trials`**. Define every symbol, include appropriate physical units and interpret the input and output quantities. The displayed relationship may be exact within an ideal geometry, a simplification of more complete dynamics, or a statistical approximation. Its status must be recorded. When the formula requires constant dimensions or a fixed reference frame, note these conditions explicitly. A coordinate-dependent result is meaningless until frame orientation and origin are identified.

**Implementation choice.** The lightest controller or cheapest sensor is not automatically the best solution. Complexity can improve diagnostics yet add failure modes and maintenance obligations. Define what a more advanced method would need to prove under representative loads, timing, environment and budget. In this lesson, look specifically at **task planning and finite-state execution** rather than copying a generic control diagram. Ask which model terms could be measured directly. For each unmeasured quantity, give a method for identification and state what additional assumptions that method requires.

**Submodel and system boundary.** Inference under observation limits Distinguish the ideal mathematical transformation from the mechanical or software device implementing it. For example, a calculated path requires a motion executor, a sensor-based termination rule and an independently assessed response to loss of communication. A fully specified algorithm can still be unsuitable for hardware when the necessary observations arrive too late.

## Worked calculation and numerical judgment

With per-attempt success probability 0.80, expected attempts are 1.25 only if trials are independent and identical. Reproduce the substitution on paper, carry units through each stage and check the scale with an independent estimate. Precision in displayed decimal places does not demonstrate precise knowledge of link lengths, accelerations, friction coefficients or camera calibration. If inputs are rounded or synthetic, the outputs inherit those limitations; do not label them as measured robot performance.

**Boundary Cases audit.** Check a zero-input limit, a typical operating point and a maximum planned input. Where derivatives exist, estimate local sensitivity to a 5% change. If the result changes sharply, prioritize a measurement of the sensitive parameter rather than increasing numerical precision elsewhere. Extend the example by sweeping one independent input through a realistic range. Predict the qualitative trend before computing. Then change another input in a separate run; explain why changing both simultaneously would make causal interpretation weaker. Document any singular, discontinuous or saturating regime instead of hiding it by clipping a plot without explanation.

## Engineering interpretation and practical alternatives

The principal design trade-off is between algorithmic or mechanical capability and the evidence needed to operate it reliably. A high-speed option may increase throughput but increase motor heating and the consequence of a delayed stop. A sophisticated estimator may reduce drift under good lighting but fail abruptly when landmarks disappear. A carefully bounded simpler system can therefore outperform a more elaborate system under the actual operating conditions.

**Specific failure mechanism.** The controller loops indefinitely on a failed grasp and blocks other urgent requests. Do not respond automatically by increasing controller gain or changing a threshold. State what instrument or independent observation would reveal the difference between a bad model, incorrect calibration, measurement delay and a mechanical fault. Consider the consequences for neighboring subsystems: sensing errors affect grasp decisions, trajectory errors affect collision risk, and recovery behavior affects throughput.

**Integration perspective.** Treat measurements as evidence with false alarms and missed detections, not perfect world state. Report class distributions and the conditions under which confidence is calibrated. Planning has a safety boundary independent of nominal vision output. For this topic, explicitly identify the preceding system function that supplies information and the following function that consumes the output. Give those interfaces names and units. State whether data is real time, sampled, batch-produced or only available after an operation ends. Wrong timing semantics can invalidate a mathematically correct equation.

## Verification protocol and evidence quality

A falsifiable check is: **Inject missing, delayed and contradictory object-present signals and examine resulting state traces.** Establish independent observations whenever practical. Define an input range, number of trials, logging rate, expected trend, calibration reference and an acceptance threshold selected before analysis. At minimum include a nominal trial, a limiting case and an innocuous fault or missing-data condition. Physically hazardous failure injection requires qualified supervision and appropriate containment; otherwise conduct the test virtually and describe that limitation.

**Failure analysis.** Changing lighting and product mix are distinct sources of distribution shift. Test held-out object materials, multiple camera positions and delayed detections before trusting any automation claim. When recorded evidence contradicts a prediction, preserve the discrepancy. Consider sensor bias, frame mismatch, uncontrolled load, aliasing, model order, compliance and operator intervention as competing explanations. One favorable trace does not validate a complete operating envelope. A reliable result needs repeatability across changed initial conditions and traceability to the configuration used for the test.

**Laboratory record.** Save model revision, input parameter table, raw data, units, frame definitions, timestamps, plot-generating script, calculated sensitivity and unsuccessful cases. Attach a short statement distinguishing simulation evidence from physical measurement and from a safety-related assessment. If equipment access is unavailable, provide a transparent synthetic test with expected results and avoid representing it as laboratory measurement.

## Exercises and design investigation

1. **Interpretation:** Derive or explain `expected_attempts=1/p_success for independent trials` from relevant geometry, conservation laws or probability assumptions. Define all quantities, directions and units. Name a realistic boundary where it loses validity.
2. **Calculation:** Recompute the worked example without copying its result. Change the most important input by 10%; compare the resulting change against the original prediction, and explain when a first-order approximation is inadequate.
3. **Independent validation:** Construct a test of task planning and finite-state execution using an independent reference. State three potential sources of measurement error and which observable can isolate at least two of them.
4. **Failure and safety:** Using the specified failure mechanism, write an expected fault signature, a detection threshold and a controlled fallback response. Distinguish the operating controller from a separately evaluated safety function.
5. **Applied synthesis:** For the unit's running case, document one viable alternative architecture, what it costs in complexity, and what evidence would justify choosing it over the baseline.

## Lesson summary and transfer

The central skill is to connect **task planning and finite-state execution** to a physically meaningful model and a test that could disprove it. Carry the same units, coordinate conventions, uncertainty bounds and versioned acceptance criteria into the next lesson. Robot performance is judged by reproducible task outcomes under constrained conditions, not by an appealing ideal plot or the correctness of a single formula.


---

