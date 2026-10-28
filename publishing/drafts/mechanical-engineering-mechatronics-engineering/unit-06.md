# Unit 06: Robotics, Kinematics and Motion Planning

**Course Code**: MCT 406 · **Level**: Advanced Undergraduate Engineering

## Unit Overview & Physical Foundations

This comprehensive university textbook unit covers the theoretical framework, physical modeling, mathematical governing equations, and engineering applications of **Robotics, Kinematics and Motion Planning**.

# U06-L01 — Two-link forward kinematics

**OpenSTEM Mechanical Engineering · Book 11: Mechatronics Engineering · Unit 6: Robotics, Kinematics and Motion Planning.** Educational draft for university study; no hardware-specific safety certification is implied.

## Learning outcome and engineering question

Explain the physical mechanism behind **two-link forward kinematics** and identify the quantities that can be measured independently. Starting from a realistic unit model, calculate a nominal prediction, check what happens when the governing assumptions break down and propose a discriminating experiment. This lesson is part of a progressive integrated task: A compact two-link arm transports inspection samples without colliding with the station enclosure.

**What success looks like.** By the end you should be able to defend the selected equation, label its physical units, derive or justify the result, explain a dominant failure mode, and design an observable test with an explicit acceptance criterion. Separate ideal mathematical behavior from calibration error, deadband, quantization and machine-level uncertainty. The purpose is a model that can be challenged, not an elegant formula without operational meaning.

## Conceptual model

Planar forward kinematics adds vectors from joint rotations. Joint zero definitions and positive directions must match encoder wiring. The reachable workspace is an annular region for an unconstrained two-link planar arm, but joint limits carve away much of it. This particular concept belongs to the broader unit theme: Relate coordinate transforms and trajectories to real machines with backlash and limits. Make a small system diagram showing where the relevant signal, mechanical load, power or timing variable enters and where its effect is actually observable. The diagram must distinguish the real plant from its estimate or representation.

**Why the distinction matters.** Keep geometric feasibility separate from motion feasibility. For the integrated example, document coordinate frames, joint limits and load cases. use independent end-effector measurements to check the geometric model. A plausible result can remain wrong if the coordinate frame, timing origin, sign convention or instrumentation location is inconsistent with the assembled machine.

## Mathematical representation and assumptions

A useful starting relationship is **`x=L1 cos(q1)+L2 cos(q1+q2)`**. Read each term aloud with physical dimensions. The expression is a compact model, not a universal constitutive law: its assumptions are the governing physical regime, parameter definition and measurement method described above. State whether the relationship is exact within a defined idealization, an approximation, or an empirical fit.

A derived relationship should be dimensionally homogeneous. If an angular quantity is used, declare whether trigonometric routines take radians. Distinguish electrical input power from useful output power. Next, identify at least one quantity in the expression that is independent and one that is dependent. If two independent inputs vary together, a single trial cannot identify their separate effects. List what remains constant in your derivation.

**Boundary check.** Consider reducing the principal input toward zero and increasing it within the permitted physical range. Does the result approach a sensible limit? Note when the formula would produce an unbounded, negative, or otherwise nonphysical output. Even a well-defined mathematical result should be rejected if it implies operation beyond an actuator limit or mechanical stop.

## Worked example with units

For L1=0.30 m, L2=0.20 m, q1=0 and q2=90 degrees, the tip is at (0.30,0.20) m. Rewrite the given numbers before substitution; explicitly carry their units through the equation. Compare the answer to a rough mental estimate and state a sensible number of significant figures. Do not interpret the displayed precision as measured accuracy. The calculation is synthetic unless independently verified against a particular device.

**Sensitivity experiment.** Repeat the calculation after changing one controlling quantity by +10% while keeping other stated inputs fixed. For a linear relationship, expect a proportional response in the appropriate variable; for a nonlinear one, compute the actual change and compare it with the local slope. Explain whether the chosen perturbation is realistic for the application.

**Dimensional audit.** Convert angles, voltages, forces, lengths and time to an explicitly declared convention before putting them in code. A numerical answer with the wrong units is not a small editorial error: it can change the actual machine motion or power demands by large factors. Record the conversion and the numerical rounding separately.

## Engineering integration and trade-offs

A reachable pose may require passing through an obstacle, joint stop or singular configuration. Real accuracy includes gear backlash, compliance and calibration uncertainty even when mathematical coordinate transformations are exact. For **two-link forward kinematics**, choose a realistic engineering constraint: supply capacity, maximum permissible temperature, mechanical clearance, sensor bandwidth, task deadline or acceptable uncertainty. Identify how the model interfaces with the preceding and following functions. For example, a correct sensor estimate may still arrive after the actuator can use it.

**Critical failure mode.** Mixing degrees and radians silently breaks software coordinate calculations. Identify which physical measurements could distinguish this failure from an equally plausible alternative. Do not silently compensate for a failed measurement by increasing controller gains. When an estimate is suspect, favor a defined restricted state and transparent diagnostics.

**Design trade study.** Compare a simple implementation with a more instrumented one. The simple version may lower cost and code complexity; the instrumented version may expose hidden failure modes but increases wiring, calibration and software overhead. State the evidence that would justify the additional complexity, not a blanket preference for more sensors.

## Verification and reproducibility

A specific, falsifiable check is: Check home pose and three known joint configurations using an external length reference. Define the measured output, sensor range, stimulus, trial count, recording rate and acceptance threshold. Include the expected direction of change before collecting data, and record every rejected measurement with an explanation.

**Robustness check.** Vary one parameter at a time during fault isolation; note that real production environments may combine several disturbances. Repeat under at least two operating conditions and one benign fault. The fault test must not rely on unsafe contact with unguarded moving equipment. If laboratory hardware is unavailable, build a transparent simulation and state that physical validation remains unresolved.

**Suggested notebook entries.** Record the schematic version, parameter values and uncertainties, code or model revision, independent measurement reference, raw-data location, plots, limit-case result and outstanding assumptions. This creates a reproducible chain from requirement to model to observation. A screenshot without settings and raw observations is insufficient evidence.

## Questions and design exercises

1. **Conceptual distinction.** Describe the physical meaning of the central quantities in `x=L1 cos(q1)+L2 cos(q1+q2)`. Which are commands, which are direct measurements and which require an estimate? Explain one realistic condition where the relationship should not be trusted.
2. **Quantitative extension.** Reproduce this lesson’s worked calculation from a blank page. Perturb the dominant input by 10% and compute the new prediction with units; estimate the sensitivity ratio and explain whether the effect is linear.
3. **Failure diagnosis.** Suppose a trial contradicts the predicted effect. Design two measurements that could separate the failure described above from a second cause, such as measurement bias, saturation, delay, friction or wiring reversal. Explain why merely repeating the same trial is inconclusive.
4. **Verification design.** Propose a bench or simulation protocol for two-link forward kinematics: variables held fixed, a sweep range, at least one held-out point, a pass/fail criterion, an independently observed quantity and a defined stop or abort condition. State which conclusions could not be supported by the resulting data.

## Study summary and next connection

A successful treatment of **two-link forward kinematics** includes the physical mechanism, transparent equation, numerical prediction, dimensional sanity check, uncertainty discussion and a falsifiable test. The next lesson changes part of the system, so retain a stable definition of the measured variable and the underlying coordinate or timing convention.


---

# U06-L02 — Inverse kinematics and multiple branches

**OpenSTEM Mechanical Engineering · Book 11: Mechatronics Engineering · Unit 6: Robotics, Kinematics and Motion Planning.** Educational draft for university study; no hardware-specific safety certification is implied.

## Learning outcome and engineering question

Explain the physical mechanism behind **inverse kinematics and multiple branches** and identify the quantities that can be measured independently. Starting from a realistic unit model, calculate a nominal prediction, check what happens when the governing assumptions break down and propose a discriminating experiment. This lesson is part of a progressive integrated task: A compact two-link arm transports inspection samples without colliding with the station enclosure.

**What success looks like.** By the end you should be able to defend the selected equation, label its physical units, derive or justify the result, explain a dominant failure mode, and design an observable test with an explicit acceptance criterion. Show what happens at a limiting case before relying on an intermediate operating point. The purpose is a model that can be challenged, not an elegant formula without operational meaning.

## Conceptual model

The same planar tip position can correspond to elbow-up and elbow-down configurations. Derive the cosine relation from the law of cosines and reject unreachable targets before taking an inverse cosine. Resolve branches using collision and joint-limit constraints. This particular concept belongs to the broader unit theme: Relate coordinate transforms and trajectories to real machines with backlash and limits. Make a small system diagram showing where the relevant signal, mechanical load, power or timing variable enters and where its effect is actually observable. The diagram must distinguish the real plant from its estimate or representation.

**Why the distinction matters.** Keep geometric feasibility separate from motion feasibility. For the integrated example, document coordinate frames, joint limits and load cases. use independent end-effector measurements to check the geometric model. A plausible result can remain wrong if the coordinate frame, timing origin, sign convention or instrumentation location is inconsistent with the assembled machine.

## Mathematical representation and assumptions

A useful starting relationship is **`cos(q2)=(x^2+y^2-L1^2-L2^2)/(2 L1 L2)`**. Read each term aloud with physical dimensions. The expression is a compact model, not a universal constitutive law: its assumptions are the governing physical regime, parameter definition and measurement method described above. State whether the relationship is exact within a defined idealization, an approximation, or an empirical fit.

An equation is only as good as its measurement model. Quantities denoted with a command subscript are not automatically the same as physical values recorded at a sensor. Next, identify at least one quantity in the expression that is independent and one that is dependent. If two independent inputs vary together, a single trial cannot identify their separate effects. List what remains constant in your derivation.

**Boundary check.** Consider reducing the principal input toward zero and increasing it within the permitted physical range. Does the result approach a sensible limit? Note when the formula would produce an unbounded, negative, or otherwise nonphysical output. Even a well-defined mathematical result should be rejected if it implies operation beyond an actuator limit or mechanical stop.

## Worked example with units

For L1=0.30 m, L2=0.20 m and target radius 0.40 m, cos(q2)=0.25 and q2≈75.52 degrees in one branch. Rewrite the given numbers before substitution; explicitly carry their units through the equation. Compare the answer to a rough mental estimate and state a sensible number of significant figures. Do not interpret the displayed precision as measured accuracy. The calculation is synthetic unless independently verified against a particular device.

**Sensitivity experiment.** Repeat the calculation after changing one controlling quantity by +10% while keeping other stated inputs fixed. For a linear relationship, expect a proportional response in the appropriate variable; for a nonlinear one, compute the actual change and compare it with the local slope. Explain whether the chosen perturbation is realistic for the application.

**Dimensional audit.** Convert angles, voltages, forces, lengths and time to an explicitly declared convention before putting them in code. A numerical answer with the wrong units is not a small editorial error: it can change the actual machine motion or power demands by large factors. Record the conversion and the numerical rounding separately.

## Engineering integration and trade-offs

A reachable pose may require passing through an obstacle, joint stop or singular configuration. Real accuracy includes gear backlash, compliance and calibration uncertainty even when mathematical coordinate transformations are exact. For **inverse kinematics and multiple branches**, choose a realistic engineering constraint: supply capacity, maximum permissible temperature, mechanical clearance, sensor bandwidth, task deadline or acceptable uncertainty. Identify how the model interfaces with the preceding and following functions. For example, a correct sensor estimate may still arrive after the actuator can use it.

**Critical failure mode.** Clamping a grossly unreachable target hides a planning error instead of making the path feasible. Identify which physical measurements could distinguish this failure from an equally plausible alternative. Do not silently compensate for a failed measurement by increasing controller gains. When an estimate is suspect, favor a defined restricted state and transparent diagnostics.

**Design trade study.** Compare a simple implementation with a more instrumented one. The simple version may lower cost and code complexity; the instrumented version may expose hidden failure modes but increases wiring, calibration and software overhead. State the evidence that would justify the additional complexity, not a blanket preference for more sensors.

## Verification and reproducibility

A specific, falsifiable check is: Plot both inverse solutions and compare predicted end-effector position after forward substitution. Define the measured output, sensor range, stimulus, trial count, recording rate and acceptance threshold. Include the expected direction of change before collecting data, and record every rejected measurement with an explanation.

**Robustness check.** Predefine the pass/fail criterion and archive unsuccessful traces. Changing the limit after viewing the data removes the meaning of acceptance testing. Repeat under at least two operating conditions and one benign fault. The fault test must not rely on unsafe contact with unguarded moving equipment. If laboratory hardware is unavailable, build a transparent simulation and state that physical validation remains unresolved.

**Suggested notebook entries.** Record the schematic version, parameter values and uncertainties, code or model revision, independent measurement reference, raw-data location, plots, limit-case result and outstanding assumptions. This creates a reproducible chain from requirement to model to observation. A screenshot without settings and raw observations is insufficient evidence.

## Questions and design exercises

1. **Conceptual distinction.** Describe the physical meaning of the central quantities in `cos(q2)=(x^2+y^2-L1^2-L2^2)/(2 L1 L2)`. Which are commands, which are direct measurements and which require an estimate? Explain one realistic condition where the relationship should not be trusted.
2. **Quantitative extension.** Reproduce this lesson’s worked calculation from a blank page. Perturb the dominant input by 10% and compute the new prediction with units; estimate the sensitivity ratio and explain whether the effect is linear.
3. **Failure diagnosis.** Suppose a trial contradicts the predicted effect. Design two measurements that could separate the failure described above from a second cause, such as measurement bias, saturation, delay, friction or wiring reversal. Explain why merely repeating the same trial is inconclusive.
4. **Verification design.** Propose a bench or simulation protocol for inverse kinematics and multiple branches: variables held fixed, a sweep range, at least one held-out point, a pass/fail criterion, an independently observed quantity and a defined stop or abort condition. State which conclusions could not be supported by the resulting data.

## Study summary and next connection

A successful treatment of **inverse kinematics and multiple branches** includes the physical mechanism, transparent equation, numerical prediction, dimensional sanity check, uncertainty discussion and a falsifiable test. The next lesson changes part of the system, so retain a stable definition of the measured variable and the underlying coordinate or timing convention.


---

# U06-L03 — Smooth trajectories and jerk tradeoffs

**OpenSTEM Mechanical Engineering · Book 11: Mechatronics Engineering · Unit 6: Robotics, Kinematics and Motion Planning.** Educational draft for university study; no hardware-specific safety certification is implied.

## Learning outcome and engineering question

Explain the physical mechanism behind **smooth trajectories and jerk tradeoffs** and identify the quantities that can be measured independently. Starting from a realistic unit model, calculate a nominal prediction, check what happens when the governing assumptions break down and propose a discriminating experiment. This lesson is part of a progressive integrated task: A compact two-link arm transports inspection samples without colliding with the station enclosure.

**What success looks like.** By the end you should be able to defend the selected equation, label its physical units, derive or justify the result, explain a dominant failure mode, and design an observable test with an explicit acceptance criterion. Use two independent ways of checking a result: dimensional reasoning and either a measurement or a numerical reproduction. The purpose is a model that can be challenged, not an elegant formula without operational meaning.

## Conceptual model

A cubic motion law can ensure zero endpoint velocity; a quintic can also ensure zero endpoint acceleration. Time scaling affects velocity, acceleration and jerk with different powers. Actuator peak constraints must be checked along the entire trajectory. This particular concept belongs to the broader unit theme: Relate coordinate transforms and trajectories to real machines with backlash and limits. Make a small system diagram showing where the relevant signal, mechanical load, power or timing variable enters and where its effect is actually observable. The diagram must distinguish the real plant from its estimate or representation.

**Why the distinction matters.** Keep geometric feasibility separate from motion feasibility. For the integrated example, document coordinate frames, joint limits and load cases. use independent end-effector measurements to check the geometric model. A plausible result can remain wrong if the coordinate frame, timing origin, sign convention or instrumentation location is inconsistent with the assembled machine.

## Mathematical representation and assumptions

A useful starting relationship is **`s(u)=3u^2-2u^3`**. Read each term aloud with physical dimensions. The expression is a compact model, not a universal constitutive law: its assumptions are the governing physical regime, parameter definition and measurement method described above. State whether the relationship is exact within a defined idealization, an approximation, or an empirical fit.

Model coefficients and initial conditions need uncertainty bounds. The sensitivity of a result to these inputs matters as much as its nominal numerical value. Next, identify at least one quantity in the expression that is independent and one that is dependent. If two independent inputs vary together, a single trial cannot identify their separate effects. List what remains constant in your derivation.

**Boundary check.** Consider reducing the principal input toward zero and increasing it within the permitted physical range. Does the result approach a sensible limit? Note when the formula would produce an unbounded, negative, or otherwise nonphysical output. Even a well-defined mathematical result should be rejected if it implies operation beyond an actuator limit or mechanical stop.

## Worked example with units

At normalized time u=0.25 a cubic profile has completed 15.625% of the position change. Rewrite the given numbers before substitution; explicitly carry their units through the equation. Compare the answer to a rough mental estimate and state a sensible number of significant figures. Do not interpret the displayed precision as measured accuracy. The calculation is synthetic unless independently verified against a particular device.

**Sensitivity experiment.** Repeat the calculation after changing one controlling quantity by +10% while keeping other stated inputs fixed. For a linear relationship, expect a proportional response in the appropriate variable; for a nonlinear one, compute the actual change and compare it with the local slope. Explain whether the chosen perturbation is realistic for the application.

**Dimensional audit.** Convert angles, voltages, forces, lengths and time to an explicitly declared convention before putting them in code. A numerical answer with the wrong units is not a small editorial error: it can change the actual machine motion or power demands by large factors. Record the conversion and the numerical rounding separately.

## Engineering integration and trade-offs

A reachable pose may require passing through an obstacle, joint stop or singular configuration. Real accuracy includes gear backlash, compliance and calibration uncertainty even when mathematical coordinate transformations are exact. For **smooth trajectories and jerk tradeoffs**, choose a realistic engineering constraint: supply capacity, maximum permissible temperature, mechanical clearance, sensor bandwidth, task deadline or acceptable uncertainty. Identify how the model interfaces with the preceding and following functions. For example, a correct sensor estimate may still arrive after the actuator can use it.

**Critical failure mode.** A short move time may require excessive peak acceleration despite smooth endpoints. Identify which physical measurements could distinguish this failure from an equally plausible alternative. Do not silently compensate for a failed measurement by increasing controller gains. When an estimate is suspect, favor a defined restricted state and transparent diagnostics.

**Design trade study.** Compare a simple implementation with a more instrumented one. The simple version may lower cost and code complexity; the instrumented version may expose hidden failure modes but increases wiring, calibration and software overhead. State the evidence that would justify the additional complexity, not a blanket preference for more sensors.

## Verification and reproducibility

A specific, falsifiable check is: Simulate position, velocity, acceleration and jerk before executing at reduced speed. Define the measured output, sensor range, stimulus, trial count, recording rate and acceptance threshold. Include the expected direction of change before collecting data, and record every rejected measurement with an explanation.

**Robustness check.** Test shutdown and restart explicitly. Recovering to a safe known state is part of functionality, not an optional maintenance feature. Repeat under at least two operating conditions and one benign fault. The fault test must not rely on unsafe contact with unguarded moving equipment. If laboratory hardware is unavailable, build a transparent simulation and state that physical validation remains unresolved.

**Suggested notebook entries.** Record the schematic version, parameter values and uncertainties, code or model revision, independent measurement reference, raw-data location, plots, limit-case result and outstanding assumptions. This creates a reproducible chain from requirement to model to observation. A screenshot without settings and raw observations is insufficient evidence.

## Questions and design exercises

1. **Conceptual distinction.** Describe the physical meaning of the central quantities in `s(u)=3u^2-2u^3`. Which are commands, which are direct measurements and which require an estimate? Explain one realistic condition where the relationship should not be trusted.
2. **Quantitative extension.** Reproduce this lesson’s worked calculation from a blank page. Perturb the dominant input by 10% and compute the new prediction with units; estimate the sensitivity ratio and explain whether the effect is linear.
3. **Failure diagnosis.** Suppose a trial contradicts the predicted effect. Design two measurements that could separate the failure described above from a second cause, such as measurement bias, saturation, delay, friction or wiring reversal. Explain why merely repeating the same trial is inconclusive.
4. **Verification design.** Propose a bench or simulation protocol for smooth trajectories and jerk tradeoffs: variables held fixed, a sweep range, at least one held-out point, a pass/fail criterion, an independently observed quantity and a defined stop or abort condition. State which conclusions could not be supported by the resulting data.

## Study summary and next connection

A successful treatment of **smooth trajectories and jerk tradeoffs** includes the physical mechanism, transparent equation, numerical prediction, dimensional sanity check, uncertainty discussion and a falsifiable test. The next lesson changes part of the system, so retain a stable definition of the measured variable and the underlying coordinate or timing convention.


---

# U06-L04 — Backlash, compliance and end-effector accuracy

**OpenSTEM Mechanical Engineering · Book 11: Mechatronics Engineering · Unit 6: Robotics, Kinematics and Motion Planning.** Educational draft for university study; no hardware-specific safety certification is implied.

## Learning outcome and engineering question

Explain the physical mechanism behind **backlash, compliance and end-effector accuracy** and identify the quantities that can be measured independently. Starting from a realistic unit model, calculate a nominal prediction, check what happens when the governing assumptions break down and propose a discriminating experiment. This lesson is part of a progressive integrated task: A compact two-link arm transports inspection samples without colliding with the station enclosure.

**What success looks like.** By the end you should be able to defend the selected equation, label its physical units, derive or justify the result, explain a dominant failure mode, and design an observable test with an explicit acceptance criterion. Begin with a physical free-body, energy-flow or signal-flow representation before introducing a numerical model. The purpose is a model that can be challenged, not an elegant formula without operational meaning.

## Conceptual model

Motor-side angle alone cannot reveal backlash at a gearbox output. Elastic deflection adds load-dependent positioning error; mechanical resonance and temperature create further variation. Calibrate at representative loads and directions. This particular concept belongs to the broader unit theme: Relate coordinate transforms and trajectories to real machines with backlash and limits. Make a small system diagram showing where the relevant signal, mechanical load, power or timing variable enters and where its effect is actually observable. The diagram must distinguish the real plant from its estimate or representation.

**Why the distinction matters.** Keep geometric feasibility separate from motion feasibility. For the integrated example, document coordinate frames, joint limits and load cases. use independent end-effector measurements to check the geometric model. A plausible result can remain wrong if the coordinate frame, timing origin, sign convention or instrumentation location is inconsistent with the assembled machine.

## Mathematical representation and assumptions

A useful starting relationship is **`delta = F/k`**. Read each term aloud with physical dimensions. The expression is a compact model, not a universal constitutive law: its assumptions are the governing physical regime, parameter definition and measurement method described above. State whether the relationship is exact within a defined idealization, an approximation, or an empirical fit.

For sampled systems, timestamp the input and output to distinguish propagation delay from genuine plant dynamics. An unmeasured delay can invalidate an otherwise sound formula. Next, identify at least one quantity in the expression that is independent and one that is dependent. If two independent inputs vary together, a single trial cannot identify their separate effects. List what remains constant in your derivation.

**Boundary check.** Consider reducing the principal input toward zero and increasing it within the permitted physical range. Does the result approach a sensible limit? Note when the formula would produce an unbounded, negative, or otherwise nonphysical output. Even a well-defined mathematical result should be rejected if it implies operation beyond an actuator limit or mechanical stop.

## Worked example with units

A 60 N lateral load on a 30,000 N/m equivalent stiffness produces 2 mm deflection. Rewrite the given numbers before substitution; explicitly carry their units through the equation. Compare the answer to a rough mental estimate and state a sensible number of significant figures. Do not interpret the displayed precision as measured accuracy. The calculation is synthetic unless independently verified against a particular device.

**Sensitivity experiment.** Repeat the calculation after changing one controlling quantity by +10% while keeping other stated inputs fixed. For a linear relationship, expect a proportional response in the appropriate variable; for a nonlinear one, compute the actual change and compare it with the local slope. Explain whether the chosen perturbation is realistic for the application.

**Dimensional audit.** Convert angles, voltages, forces, lengths and time to an explicitly declared convention before putting them in code. A numerical answer with the wrong units is not a small editorial error: it can change the actual machine motion or power demands by large factors. Record the conversion and the numerical rounding separately.

## Engineering integration and trade-offs

A reachable pose may require passing through an obstacle, joint stop or singular configuration. Real accuracy includes gear backlash, compliance and calibration uncertainty even when mathematical coordinate transformations are exact. For **backlash, compliance and end-effector accuracy**, choose a realistic engineering constraint: supply capacity, maximum permissible temperature, mechanical clearance, sensor bandwidth, task deadline or acceptable uncertainty. Identify how the model interfaces with the preceding and following functions. For example, a correct sensor estimate may still arrive after the actuator can use it.

**Critical failure mode.** Increasing encoder resolution does not repair a mechanically flexible structure. Identify which physical measurements could distinguish this failure from an equally plausible alternative. Do not silently compensate for a failed measurement by increasing controller gains. When an estimate is suspect, favor a defined restricted state and transparent diagnostics.

**Design trade study.** Compare a simple implementation with a more instrumented one. The simple version may lower cost and code complexity; the instrumented version may expose hidden failure modes but increases wiring, calibration and software overhead. State the evidence that would justify the additional complexity, not a blanket preference for more sensors.

## Verification and reproducibility

A specific, falsifiable check is: Measure bidirectional approach error and load-dependent tip deflection rather than only motor encoder counts. Define the measured output, sensor range, stimulus, trial count, recording rate and acceptance threshold. Include the expected direction of change before collecting data, and record every rejected measurement with an explanation.

**Robustness check.** Record the maximum as well as the average. A machine that misses one deadline in a hundred may be unusable when every item must be sorted. Repeat under at least two operating conditions and one benign fault. The fault test must not rely on unsafe contact with unguarded moving equipment. If laboratory hardware is unavailable, build a transparent simulation and state that physical validation remains unresolved.

**Suggested notebook entries.** Record the schematic version, parameter values and uncertainties, code or model revision, independent measurement reference, raw-data location, plots, limit-case result and outstanding assumptions. This creates a reproducible chain from requirement to model to observation. A screenshot without settings and raw observations is insufficient evidence.

## Questions and design exercises

1. **Conceptual distinction.** Describe the physical meaning of the central quantities in `delta = F/k`. Which are commands, which are direct measurements and which require an estimate? Explain one realistic condition where the relationship should not be trusted.
2. **Quantitative extension.** Reproduce this lesson’s worked calculation from a blank page. Perturb the dominant input by 10% and compute the new prediction with units; estimate the sensitivity ratio and explain whether the effect is linear.
3. **Failure diagnosis.** Suppose a trial contradicts the predicted effect. Design two measurements that could separate the failure described above from a second cause, such as measurement bias, saturation, delay, friction or wiring reversal. Explain why merely repeating the same trial is inconclusive.
4. **Verification design.** Propose a bench or simulation protocol for backlash, compliance and end-effector accuracy: variables held fixed, a sweep range, at least one held-out point, a pass/fail criterion, an independently observed quantity and a defined stop or abort condition. State which conclusions could not be supported by the resulting data.

## Study summary and next connection

A successful treatment of **backlash, compliance and end-effector accuracy** includes the physical mechanism, transparent equation, numerical prediction, dimensional sanity check, uncertainty discussion and a falsifiable test. The next lesson changes part of the system, so retain a stable definition of the measured variable and the underlying coordinate or timing convention.


---

# U06-L05 — Workspace boundaries and collision prevention

**OpenSTEM Mechanical Engineering · Book 11: Mechatronics Engineering · Unit 6: Robotics, Kinematics and Motion Planning.** Educational draft for university study; no hardware-specific safety certification is implied.

## Learning outcome and engineering question

Explain the physical mechanism behind **workspace boundaries and collision prevention** and identify the quantities that can be measured independently. Starting from a realistic unit model, calculate a nominal prediction, check what happens when the governing assumptions break down and propose a discriminating experiment. This lesson is part of a progressive integrated task: A compact two-link arm transports inspection samples without colliding with the station enclosure.

**What success looks like.** By the end you should be able to defend the selected equation, label its physical units, derive or justify the result, explain a dominant failure mode, and design an observable test with an explicit acceptance criterion. Convert the verbal specification into variables with declared units, coordinate directions and an operating envelope. The purpose is a model that can be challenged, not an elegant formula without operational meaning.

## Conceptual model

Software workspace limits are useful but must not replace independent limits in hazardous mechanisms. Consider robot stopping distance, configuration-dependent clearance, payload swing, and encoder uncertainty. Collision checking needs shape and motion uncertainty, not point coordinates only. This particular concept belongs to the broader unit theme: Relate coordinate transforms and trajectories to real machines with backlash and limits. Make a small system diagram showing where the relevant signal, mechanical load, power or timing variable enters and where its effect is actually observable. The diagram must distinguish the real plant from its estimate or representation.

**Why the distinction matters.** Keep geometric feasibility separate from motion feasibility. For the integrated example, document coordinate frames, joint limits and load cases. use independent end-effector measurements to check the geometric model. A plausible result can remain wrong if the coordinate frame, timing origin, sign convention or instrumentation location is inconsistent with the assembled machine.

## Mathematical representation and assumptions

A useful starting relationship is **`d_stop ≈ v^2/(2a)`**. Read each term aloud with physical dimensions. The expression is a compact model, not a universal constitutive law: its assumptions are the governing physical regime, parameter definition and measurement method described above. State whether the relationship is exact within a defined idealization, an approximation, or an empirical fit.

In a design calculation, rounding should occur at reporting time. Retain guard digits during intermediate steps so that resolution errors are not mistaken for physical discrepancies. Next, identify at least one quantity in the expression that is independent and one that is dependent. If two independent inputs vary together, a single trial cannot identify their separate effects. List what remains constant in your derivation.

**Boundary check.** Consider reducing the principal input toward zero and increasing it within the permitted physical range. Does the result approach a sensible limit? Note when the formula would produce an unbounded, negative, or otherwise nonphysical output. Even a well-defined mathematical result should be rejected if it implies operation beyond an actuator limit or mechanical stop.

## Worked example with units

At 0.50 m/s and effective deceleration 2.0 m/s^2, idealized stopping travel is at least 0.0625 m before delays. Rewrite the given numbers before substitution; explicitly carry their units through the equation. Compare the answer to a rough mental estimate and state a sensible number of significant figures. Do not interpret the displayed precision as measured accuracy. The calculation is synthetic unless independently verified against a particular device.

**Sensitivity experiment.** Repeat the calculation after changing one controlling quantity by +10% while keeping other stated inputs fixed. For a linear relationship, expect a proportional response in the appropriate variable; for a nonlinear one, compute the actual change and compare it with the local slope. Explain whether the chosen perturbation is realistic for the application.

**Dimensional audit.** Convert angles, voltages, forces, lengths and time to an explicitly declared convention before putting them in code. A numerical answer with the wrong units is not a small editorial error: it can change the actual machine motion or power demands by large factors. Record the conversion and the numerical rounding separately.

## Engineering integration and trade-offs

A reachable pose may require passing through an obstacle, joint stop or singular configuration. Real accuracy includes gear backlash, compliance and calibration uncertainty even when mathematical coordinate transformations are exact. For **workspace boundaries and collision prevention**, choose a realistic engineering constraint: supply capacity, maximum permissible temperature, mechanical clearance, sensor bandwidth, task deadline or acceptable uncertainty. Identify how the model interfaces with the preceding and following functions. For example, a correct sensor estimate may still arrive after the actuator can use it.

**Critical failure mode.** Assuming instantaneous deceleration ignores controller response time and available braking torque. Identify which physical measurements could distinguish this failure from an equally plausible alternative. Do not silently compensate for a failed measurement by increasing controller gains. When an estimate is suspect, favor a defined restricted state and transparent diagnostics.

**Design trade study.** Compare a simple implementation with a more instrumented one. The simple version may lower cost and code complexity; the instrumented version may expose hidden failure modes but increases wiring, calibration and software overhead. State the evidence that would justify the additional complexity, not a blanket preference for more sensors.

## Verification and reproducibility

A specific, falsifiable check is: Check worst-case workspace approaches with payload, reduced speed, protective barriers and independent stop logic. Define the measured output, sensor range, stimulus, trial count, recording rate and acceptance threshold. Include the expected direction of change before collecting data, and record every rejected measurement with an explanation.

**Robustness check.** Use an independently calibrated reference if possible. Comparing two software values derived from one biased sensor does not validate the measurement. Repeat under at least two operating conditions and one benign fault. The fault test must not rely on unsafe contact with unguarded moving equipment. If laboratory hardware is unavailable, build a transparent simulation and state that physical validation remains unresolved.

**Suggested notebook entries.** Record the schematic version, parameter values and uncertainties, code or model revision, independent measurement reference, raw-data location, plots, limit-case result and outstanding assumptions. This creates a reproducible chain from requirement to model to observation. A screenshot without settings and raw observations is insufficient evidence.

## Questions and design exercises

1. **Conceptual distinction.** Describe the physical meaning of the central quantities in `d_stop ≈ v^2/(2a)`. Which are commands, which are direct measurements and which require an estimate? Explain one realistic condition where the relationship should not be trusted.
2. **Quantitative extension.** Reproduce this lesson’s worked calculation from a blank page. Perturb the dominant input by 10% and compute the new prediction with units; estimate the sensitivity ratio and explain whether the effect is linear.
3. **Failure diagnosis.** Suppose a trial contradicts the predicted effect. Design two measurements that could separate the failure described above from a second cause, such as measurement bias, saturation, delay, friction or wiring reversal. Explain why merely repeating the same trial is inconclusive.
4. **Verification design.** Propose a bench or simulation protocol for workspace boundaries and collision prevention: variables held fixed, a sweep range, at least one held-out point, a pass/fail criterion, an independently observed quantity and a defined stop or abort condition. State which conclusions could not be supported by the resulting data.

## Study summary and next connection

A successful treatment of **workspace boundaries and collision prevention** includes the physical mechanism, transparent equation, numerical prediction, dimensional sanity check, uncertainty discussion and a falsifiable test. The next lesson changes part of the system, so retain a stable definition of the measured variable and the underlying coordinate or timing convention.


---

