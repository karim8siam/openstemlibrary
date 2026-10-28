# Unit 01: System Architecture and Multidisciplinary Design

**Course Code**: MCT 401 · **Level**: Advanced Undergraduate Engineering

## Unit Overview & Physical Foundations

This comprehensive university textbook unit covers the theoretical framework, physical modeling, mathematical governing equations, and engineering applications of **System Architecture and Multidisciplinary Design**.

# U01-L01 — Requirements and verification traceability

**OpenSTEM Mechanical Engineering · Book 11: Mechatronics Engineering · Unit 1: System Architecture and Multidisciplinary Design.** Educational draft for university study; no hardware-specific safety certification is implied.

## Learning outcome and engineering question

Explain the physical mechanism behind **requirements and verification traceability** and identify the quantities that can be measured independently. Starting from a realistic unit model, calculate a nominal prediction, check what happens when the governing assumptions break down and propose a discriminating experiment. This lesson is part of a progressive integrated task: An automated inspection gate must classify objects, move them safely and leave a defensible record of its decisions.

**What success looks like.** By the end you should be able to defend the selected equation, label its physical units, derive or justify the result, explain a dominant failure mode, and design an observable test with an explicit acceptance criterion. Separate ideal mathematical behavior from calibration error, deadband, quantization and machine-level uncertainty. The purpose is a model that can be challenged, not an elegant formula without operational meaning.

## Conceptual model

A statement such as “fast sorting” cannot be tested until it specifies object spacing, decision latency, allowable misses, stop distance, and ambient conditions. Allocate measurable requirements to mechanisms, sensors, firmware and power electronics. A requirement is not verified merely because a demonstration looks convincing. This particular concept belongs to the broader unit theme: Design a system from a traceable physical requirement rather than picking electronics first. Make a small system diagram showing where the relevant signal, mechanical load, power or timing variable enters and where its effect is actually observable. The diagram must distinguish the real plant from its estimate or representation.

**Why the distinction matters.** Trace the flow of matter, information and energy. For the integrated example, split a station into sensor, embedded controller, actuator driver and guarded mechanics. establish a signal and unit table before firmware implementation; mark the direction of every command and measurement. A plausible result can remain wrong if the coordinate frame, timing origin, sign convention or instrumentation location is inconsistent with the assembled machine.

## Mathematical representation and assumptions

A useful starting relationship is **`t_available = d / v`**. Read each term aloud with physical dimensions. The expression is a compact model, not a universal constitutive law: its assumptions are the governing physical regime, parameter definition and measurement method described above. State whether the relationship is exact within a defined idealization, an approximation, or an empirical fit.

A derived relationship should be dimensionally homogeneous. If an angular quantity is used, declare whether trigonometric routines take radians. Distinguish electrical input power from useful output power. Next, identify at least one quantity in the expression that is independent and one that is dependent. If two independent inputs vary together, a single trial cannot identify their separate effects. List what remains constant in your derivation.

**Boundary check.** Consider reducing the principal input toward zero and increasing it within the permitted physical range. Does the result approach a sensible limit? Note when the formula would produce an unbounded, negative, or otherwise nonphysical output. Even a well-defined mathematical result should be rejected if it implies operation beyond an actuator limit or mechanical stop.

## Worked example with units

For object spacing d = 0.240 m and belt speed v = 0.80 m/s, the decision budget is 0.300 s before accounting for network, actuator and safety margins. Rewrite the given numbers before substitution; explicitly carry their units through the equation. Compare the answer to a rough mental estimate and state a sensible number of significant figures. Do not interpret the displayed precision as measured accuracy. The calculation is synthetic unless independently verified against a particular device.

**Sensitivity experiment.** Repeat the calculation after changing one controlling quantity by +10% while keeping other stated inputs fixed. For a linear relationship, expect a proportional response in the appropriate variable; for a nonlinear one, compute the actual change and compare it with the local slope. Explain whether the chosen perturbation is realistic for the application.

**Dimensional audit.** Convert angles, voltages, forces, lengths and time to an explicitly declared convention before putting them in code. A numerical answer with the wrong units is not a small editorial error: it can change the actual machine motion or power demands by large factors. Record the conversion and the numerical rounding separately.

## Engineering integration and trade-offs

Architecture choices should be evaluated against worst-case throughput, environmental exposure, reset behavior and the ability to test the system without connecting hazardous mechanisms. Design reviews should ask which interfaces are shared between independent protective systems, because common-cause failures defeat apparent redundancy. For **requirements and verification traceability**, choose a realistic engineering constraint: supply capacity, maximum permissible temperature, mechanical clearance, sensor bandwidth, task deadline or acceptable uncertainty. Identify how the model interfaces with the preceding and following functions. For example, a correct sensor estimate may still arrive after the actuator can use it.

**Critical failure mode.** Confusing desired throughput with guaranteed throughput hides worst-case delay and jam recovery. Identify which physical measurements could distinguish this failure from an equally plausible alternative. Do not silently compensate for a failed measurement by increasing controller gains. When an estimate is suspect, favor a defined restricted state and transparent diagnostics.

**Design trade study.** Compare a simple implementation with a more instrumented one. The simple version may lower cost and code complexity; the instrumented version may expose hidden failure modes but increases wiring, calibration and software overhead. State the evidence that would justify the additional complexity, not a blanket preference for more sensors.

## Verification and reproducibility

A specific, falsifiable check is: Test at maximum belt speed and smallest allowed spacing with separately timestamped detection, decision and actuation. Define the measured output, sensor range, stimulus, trial count, recording rate and acceptance threshold. Include the expected direction of change before collecting data, and record every rejected measurement with an explanation.

**Robustness check.** Vary one parameter at a time during fault isolation; note that real production environments may combine several disturbances. Repeat under at least two operating conditions and one benign fault. The fault test must not rely on unsafe contact with unguarded moving equipment. If laboratory hardware is unavailable, build a transparent simulation and state that physical validation remains unresolved.

**Suggested notebook entries.** Record the schematic version, parameter values and uncertainties, code or model revision, independent measurement reference, raw-data location, plots, limit-case result and outstanding assumptions. This creates a reproducible chain from requirement to model to observation. A screenshot without settings and raw observations is insufficient evidence.

## Questions and design exercises

1. **Conceptual distinction.** Describe the physical meaning of the central quantities in `t_available = d / v`. Which are commands, which are direct measurements and which require an estimate? Explain one realistic condition where the relationship should not be trusted.
2. **Quantitative extension.** Reproduce this lesson’s worked calculation from a blank page. Perturb the dominant input by 10% and compute the new prediction with units; estimate the sensitivity ratio and explain whether the effect is linear.
3. **Failure diagnosis.** Suppose a trial contradicts the predicted effect. Design two measurements that could separate the failure described above from a second cause, such as measurement bias, saturation, delay, friction or wiring reversal. Explain why merely repeating the same trial is inconclusive.
4. **Verification design.** Propose a bench or simulation protocol for requirements and verification traceability: variables held fixed, a sweep range, at least one held-out point, a pass/fail criterion, an independently observed quantity and a defined stop or abort condition. State which conclusions could not be supported by the resulting data.

## Study summary and next connection

A successful treatment of **requirements and verification traceability** includes the physical mechanism, transparent equation, numerical prediction, dimensional sanity check, uncertainty discussion and a falsifiable test. The next lesson changes part of the system, so retain a stable definition of the measured variable and the underlying coordinate or timing convention.


---

# U01-L02 — Functional decomposition and interface contracts

**OpenSTEM Mechanical Engineering · Book 11: Mechatronics Engineering · Unit 1: System Architecture and Multidisciplinary Design.** Educational draft for university study; no hardware-specific safety certification is implied.

## Learning outcome and engineering question

Explain the physical mechanism behind **functional decomposition and interface contracts** and identify the quantities that can be measured independently. Starting from a realistic unit model, calculate a nominal prediction, check what happens when the governing assumptions break down and propose a discriminating experiment. This lesson is part of a progressive integrated task: An automated inspection gate must classify objects, move them safely and leave a defensible record of its decisions.

**What success looks like.** By the end you should be able to defend the selected equation, label its physical units, derive or justify the result, explain a dominant failure mode, and design an observable test with an explicit acceptance criterion. Show what happens at a limiting case before relying on an intermediate operating point. The purpose is a model that can be challenged, not an elegant formula without operational meaning.

## Conceptual model

Model sensing, computing, actuation and mechanical motion as functions connected by information and energy. For every interface specify units, pin direction, voltage, grounding, polarity, sampling and error states. An interface table prevents the common error of treating a high-level software name as a physical signal. This particular concept belongs to the broader unit theme: Design a system from a traceable physical requirement rather than picking electronics first. Make a small system diagram showing where the relevant signal, mechanical load, power or timing variable enters and where its effect is actually observable. The diagram must distinguish the real plant from its estimate or representation.

**Why the distinction matters.** Trace the flow of matter, information and energy. For the integrated example, split a station into sensor, embedded controller, actuator driver and guarded mechanics. establish a signal and unit table before firmware implementation; mark the direction of every command and measurement. A plausible result can remain wrong if the coordinate frame, timing origin, sign convention or instrumentation location is inconsistent with the assembled machine.

## Mathematical representation and assumptions

A useful starting relationship is **`P = V I`**. Read each term aloud with physical dimensions. The expression is a compact model, not a universal constitutive law: its assumptions are the governing physical regime, parameter definition and measurement method described above. State whether the relationship is exact within a defined idealization, an approximation, or an empirical fit.

An equation is only as good as its measurement model. Quantities denoted with a command subscript are not automatically the same as physical values recorded at a sensor. Next, identify at least one quantity in the expression that is independent and one that is dependent. If two independent inputs vary together, a single trial cannot identify their separate effects. List what remains constant in your derivation.

**Boundary check.** Consider reducing the principal input toward zero and increasing it within the permitted physical range. Does the result approach a sensible limit? Note when the formula would produce an unbounded, negative, or otherwise nonphysical output. Even a well-defined mathematical result should be rejected if it implies operation beyond an actuator limit or mechanical stop.

## Worked example with units

At 24 V and 1.8 A, the electrical input is 43.2 W; the mechanical shaft output must be less after conversion losses. Rewrite the given numbers before substitution; explicitly carry their units through the equation. Compare the answer to a rough mental estimate and state a sensible number of significant figures. Do not interpret the displayed precision as measured accuracy. The calculation is synthetic unless independently verified against a particular device.

**Sensitivity experiment.** Repeat the calculation after changing one controlling quantity by +10% while keeping other stated inputs fixed. For a linear relationship, expect a proportional response in the appropriate variable; for a nonlinear one, compute the actual change and compare it with the local slope. Explain whether the chosen perturbation is realistic for the application.

**Dimensional audit.** Convert angles, voltages, forces, lengths and time to an explicitly declared convention before putting them in code. A numerical answer with the wrong units is not a small editorial error: it can change the actual machine motion or power demands by large factors. Record the conversion and the numerical rounding separately.

## Engineering integration and trade-offs

Architecture choices should be evaluated against worst-case throughput, environmental exposure, reset behavior and the ability to test the system without connecting hazardous mechanisms. Design reviews should ask which interfaces are shared between independent protective systems, because common-cause failures defeat apparent redundancy. For **functional decomposition and interface contracts**, choose a realistic engineering constraint: supply capacity, maximum permissible temperature, mechanical clearance, sensor bandwidth, task deadline or acceptable uncertainty. Identify how the model interfaces with the preceding and following functions. For example, a correct sensor estimate may still arrive after the actuator can use it.

**Critical failure mode.** A digital pin may provide a logical command but cannot drive a 24 V coil directly. Identify which physical measurements could distinguish this failure from an equally plausible alternative. Do not silently compensate for a failed measurement by increasing controller gains. When an estimate is suspect, favor a defined restricted state and transparent diagnostics.

**Design trade study.** Compare a simple implementation with a more instrumented one. The simple version may lower cost and code complexity; the instrumented version may expose hidden failure modes but increases wiring, calibration and software overhead. State the evidence that would justify the additional complexity, not a blanket preference for more sensors.

## Verification and reproducibility

A specific, falsifiable check is: Bench-test each sensor and driver independently with current limits before connecting moving hardware. Define the measured output, sensor range, stimulus, trial count, recording rate and acceptance threshold. Include the expected direction of change before collecting data, and record every rejected measurement with an explanation.

**Robustness check.** Predefine the pass/fail criterion and archive unsuccessful traces. Changing the limit after viewing the data removes the meaning of acceptance testing. Repeat under at least two operating conditions and one benign fault. The fault test must not rely on unsafe contact with unguarded moving equipment. If laboratory hardware is unavailable, build a transparent simulation and state that physical validation remains unresolved.

**Suggested notebook entries.** Record the schematic version, parameter values and uncertainties, code or model revision, independent measurement reference, raw-data location, plots, limit-case result and outstanding assumptions. This creates a reproducible chain from requirement to model to observation. A screenshot without settings and raw observations is insufficient evidence.

## Questions and design exercises

1. **Conceptual distinction.** Describe the physical meaning of the central quantities in `P = V I`. Which are commands, which are direct measurements and which require an estimate? Explain one realistic condition where the relationship should not be trusted.
2. **Quantitative extension.** Reproduce this lesson’s worked calculation from a blank page. Perturb the dominant input by 10% and compute the new prediction with units; estimate the sensitivity ratio and explain whether the effect is linear.
3. **Failure diagnosis.** Suppose a trial contradicts the predicted effect. Design two measurements that could separate the failure described above from a second cause, such as measurement bias, saturation, delay, friction or wiring reversal. Explain why merely repeating the same trial is inconclusive.
4. **Verification design.** Propose a bench or simulation protocol for functional decomposition and interface contracts: variables held fixed, a sweep range, at least one held-out point, a pass/fail criterion, an independently observed quantity and a defined stop or abort condition. State which conclusions could not be supported by the resulting data.

## Study summary and next connection

A successful treatment of **functional decomposition and interface contracts** includes the physical mechanism, transparent equation, numerical prediction, dimensional sanity check, uncertainty discussion and a falsifiable test. The next lesson changes part of the system, so retain a stable definition of the measured variable and the underlying coordinate or timing convention.


---

# U01-L03 — Cross-domain energy and bond reasoning

**OpenSTEM Mechanical Engineering · Book 11: Mechatronics Engineering · Unit 1: System Architecture and Multidisciplinary Design.** Educational draft for university study; no hardware-specific safety certification is implied.

## Learning outcome and engineering question

Explain the physical mechanism behind **cross-domain energy and bond reasoning** and identify the quantities that can be measured independently. Starting from a realistic unit model, calculate a nominal prediction, check what happens when the governing assumptions break down and propose a discriminating experiment. This lesson is part of a progressive integrated task: An automated inspection gate must classify objects, move them safely and leave a defensible record of its decisions.

**What success looks like.** By the end you should be able to defend the selected equation, label its physical units, derive or justify the result, explain a dominant failure mode, and design an observable test with an explicit acceptance criterion. Use two independent ways of checking a result: dimensional reasoning and either a measurement or a numerical reproduction. The purpose is a model that can be challenged, not an elegant formula without operational meaning.

## Conceptual model

Mechanical rotation, electrical current and thermal rise share conservation laws. In a motor, current produces torque and speed produces back electromotive force; losses warm coils and bearings. Start with an energy-flow sketch and find all storage and dissipation elements before assigning controller gains. This particular concept belongs to the broader unit theme: Design a system from a traceable physical requirement rather than picking electronics first. Make a small system diagram showing where the relevant signal, mechanical load, power or timing variable enters and where its effect is actually observable. The diagram must distinguish the real plant from its estimate or representation.

**Why the distinction matters.** Trace the flow of matter, information and energy. For the integrated example, split a station into sensor, embedded controller, actuator driver and guarded mechanics. establish a signal and unit table before firmware implementation; mark the direction of every command and measurement. A plausible result can remain wrong if the coordinate frame, timing origin, sign convention or instrumentation location is inconsistent with the assembled machine.

## Mathematical representation and assumptions

A useful starting relationship is **`P_shaft = tau omega`**. Read each term aloud with physical dimensions. The expression is a compact model, not a universal constitutive law: its assumptions are the governing physical regime, parameter definition and measurement method described above. State whether the relationship is exact within a defined idealization, an approximation, or an empirical fit.

Model coefficients and initial conditions need uncertainty bounds. The sensitivity of a result to these inputs matters as much as its nominal numerical value. Next, identify at least one quantity in the expression that is independent and one that is dependent. If two independent inputs vary together, a single trial cannot identify their separate effects. List what remains constant in your derivation.

**Boundary check.** Consider reducing the principal input toward zero and increasing it within the permitted physical range. Does the result approach a sensible limit? Note when the formula would produce an unbounded, negative, or otherwise nonphysical output. Even a well-defined mathematical result should be rejected if it implies operation beyond an actuator limit or mechanical stop.

## Worked example with units

A motor producing 0.50 N m at 40 rad/s delivers 20 W mechanical power. Rewrite the given numbers before substitution; explicitly carry their units through the equation. Compare the answer to a rough mental estimate and state a sensible number of significant figures. Do not interpret the displayed precision as measured accuracy. The calculation is synthetic unless independently verified against a particular device.

**Sensitivity experiment.** Repeat the calculation after changing one controlling quantity by +10% while keeping other stated inputs fixed. For a linear relationship, expect a proportional response in the appropriate variable; for a nonlinear one, compute the actual change and compare it with the local slope. Explain whether the chosen perturbation is realistic for the application.

**Dimensional audit.** Convert angles, voltages, forces, lengths and time to an explicitly declared convention before putting them in code. A numerical answer with the wrong units is not a small editorial error: it can change the actual machine motion or power demands by large factors. Record the conversion and the numerical rounding separately.

## Engineering integration and trade-offs

Architecture choices should be evaluated against worst-case throughput, environmental exposure, reset behavior and the ability to test the system without connecting hazardous mechanisms. Design reviews should ask which interfaces are shared between independent protective systems, because common-cause failures defeat apparent redundancy. For **cross-domain energy and bond reasoning**, choose a realistic engineering constraint: supply capacity, maximum permissible temperature, mechanical clearance, sensor bandwidth, task deadline or acceptable uncertainty. Identify how the model interfaces with the preceding and following functions. For example, a correct sensor estimate may still arrive after the actuator can use it.

**Critical failure mode.** Neglecting winding resistance, friction or heating makes an actuator appear more capable than it is. Identify which physical measurements could distinguish this failure from an equally plausible alternative. Do not silently compensate for a failed measurement by increasing controller gains. When an estimate is suspect, favor a defined restricted state and transparent diagnostics.

**Design trade study.** Compare a simple implementation with a more instrumented one. The simple version may lower cost and code complexity; the instrumented version may expose hidden failure modes but increases wiring, calibration and software overhead. State the evidence that would justify the additional complexity, not a blanket preference for more sensors.

## Verification and reproducibility

A specific, falsifiable check is: Measure input voltage, current, rotor speed and temperature at multiple load levels, then balance power within measurement uncertainty. Define the measured output, sensor range, stimulus, trial count, recording rate and acceptance threshold. Include the expected direction of change before collecting data, and record every rejected measurement with an explanation.

**Robustness check.** Test shutdown and restart explicitly. Recovering to a safe known state is part of functionality, not an optional maintenance feature. Repeat under at least two operating conditions and one benign fault. The fault test must not rely on unsafe contact with unguarded moving equipment. If laboratory hardware is unavailable, build a transparent simulation and state that physical validation remains unresolved.

**Suggested notebook entries.** Record the schematic version, parameter values and uncertainties, code or model revision, independent measurement reference, raw-data location, plots, limit-case result and outstanding assumptions. This creates a reproducible chain from requirement to model to observation. A screenshot without settings and raw observations is insufficient evidence.

## Questions and design exercises

1. **Conceptual distinction.** Describe the physical meaning of the central quantities in `P_shaft = tau omega`. Which are commands, which are direct measurements and which require an estimate? Explain one realistic condition where the relationship should not be trusted.
2. **Quantitative extension.** Reproduce this lesson’s worked calculation from a blank page. Perturb the dominant input by 10% and compute the new prediction with units; estimate the sensitivity ratio and explain whether the effect is linear.
3. **Failure diagnosis.** Suppose a trial contradicts the predicted effect. Design two measurements that could separate the failure described above from a second cause, such as measurement bias, saturation, delay, friction or wiring reversal. Explain why merely repeating the same trial is inconclusive.
4. **Verification design.** Propose a bench or simulation protocol for cross-domain energy and bond reasoning: variables held fixed, a sweep range, at least one held-out point, a pass/fail criterion, an independently observed quantity and a defined stop or abort condition. State which conclusions could not be supported by the resulting data.

## Study summary and next connection

A successful treatment of **cross-domain energy and bond reasoning** includes the physical mechanism, transparent equation, numerical prediction, dimensional sanity check, uncertainty discussion and a falsifiable test. The next lesson changes part of the system, so retain a stable definition of the measured variable and the underlying coordinate or timing convention.


---

# U01-L04 — Time budgets and real-time behavior

**OpenSTEM Mechanical Engineering · Book 11: Mechatronics Engineering · Unit 1: System Architecture and Multidisciplinary Design.** Educational draft for university study; no hardware-specific safety certification is implied.

## Learning outcome and engineering question

Explain the physical mechanism behind **time budgets and real-time behavior** and identify the quantities that can be measured independently. Starting from a realistic unit model, calculate a nominal prediction, check what happens when the governing assumptions break down and propose a discriminating experiment. This lesson is part of a progressive integrated task: An automated inspection gate must classify objects, move them safely and leave a defensible record of its decisions.

**What success looks like.** By the end you should be able to defend the selected equation, label its physical units, derive or justify the result, explain a dominant failure mode, and design an observable test with an explicit acceptance criterion. Begin with a physical free-body, energy-flow or signal-flow representation before introducing a numerical model. The purpose is a model that can be challenged, not an elegant formula without operational meaning.

## Conceptual model

Total response is a chain of sample acquisition, filtering, queuing, computing, bus transfer, driver response and mechanical motion. Average execution time is insufficient when safety depends on the worst case. Specify jitter, priority inversion and watchdog behavior. This particular concept belongs to the broader unit theme: Design a system from a traceable physical requirement rather than picking electronics first. Make a small system diagram showing where the relevant signal, mechanical load, power or timing variable enters and where its effect is actually observable. The diagram must distinguish the real plant from its estimate or representation.

**Why the distinction matters.** Trace the flow of matter, information and energy. For the integrated example, split a station into sensor, embedded controller, actuator driver and guarded mechanics. establish a signal and unit table before firmware implementation; mark the direction of every command and measurement. A plausible result can remain wrong if the coordinate frame, timing origin, sign convention or instrumentation location is inconsistent with the assembled machine.

## Mathematical representation and assumptions

A useful starting relationship is **`t_total = sum(t_i)`**. Read each term aloud with physical dimensions. The expression is a compact model, not a universal constitutive law: its assumptions are the governing physical regime, parameter definition and measurement method described above. State whether the relationship is exact within a defined idealization, an approximation, or an empirical fit.

For sampled systems, timestamp the input and output to distinguish propagation delay from genuine plant dynamics. An unmeasured delay can invalidate an otherwise sound formula. Next, identify at least one quantity in the expression that is independent and one that is dependent. If two independent inputs vary together, a single trial cannot identify their separate effects. List what remains constant in your derivation.

**Boundary check.** Consider reducing the principal input toward zero and increasing it within the permitted physical range. Does the result approach a sensible limit? Note when the formula would produce an unbounded, negative, or otherwise nonphysical output. Even a well-defined mathematical result should be rejected if it implies operation beyond an actuator limit or mechanical stop.

## Worked example with units

With delays of 4, 2, 5, 3 and 16 ms, nominal action latency is 30 ms, before any jitter margin. Rewrite the given numbers before substitution; explicitly carry their units through the equation. Compare the answer to a rough mental estimate and state a sensible number of significant figures. Do not interpret the displayed precision as measured accuracy. The calculation is synthetic unless independently verified against a particular device.

**Sensitivity experiment.** Repeat the calculation after changing one controlling quantity by +10% while keeping other stated inputs fixed. For a linear relationship, expect a proportional response in the appropriate variable; for a nonlinear one, compute the actual change and compare it with the local slope. Explain whether the chosen perturbation is realistic for the application.

**Dimensional audit.** Convert angles, voltages, forces, lengths and time to an explicitly declared convention before putting them in code. A numerical answer with the wrong units is not a small editorial error: it can change the actual machine motion or power demands by large factors. Record the conversion and the numerical rounding separately.

## Engineering integration and trade-offs

Architecture choices should be evaluated against worst-case throughput, environmental exposure, reset behavior and the ability to test the system without connecting hazardous mechanisms. Design reviews should ask which interfaces are shared between independent protective systems, because common-cause failures defeat apparent redundancy. For **time budgets and real-time behavior**, choose a realistic engineering constraint: supply capacity, maximum permissible temperature, mechanical clearance, sensor bandwidth, task deadline or acceptable uncertainty. Identify how the model interfaces with the preceding and following functions. For example, a correct sensor estimate may still arrive after the actuator can use it.

**Critical failure mode.** An occasional blocked serial logging call can violate a nominally fast feedback period. Identify which physical measurements could distinguish this failure from an equally plausible alternative. Do not silently compensate for a failed measurement by increasing controller gains. When an estimate is suspect, favor a defined restricted state and transparent diagnostics.

**Design trade study.** Compare a simple implementation with a more instrumented one. The simple version may lower cost and code complexity; the instrumented version may expose hidden failure modes but increases wiring, calibration and software overhead. State the evidence that would justify the additional complexity, not a blanket preference for more sensors.

## Verification and reproducibility

A specific, falsifiable check is: Capture timestamps around every stage and inspect maximum, percentile and fault-triggered latency, not only the mean. Define the measured output, sensor range, stimulus, trial count, recording rate and acceptance threshold. Include the expected direction of change before collecting data, and record every rejected measurement with an explanation.

**Robustness check.** Record the maximum as well as the average. A machine that misses one deadline in a hundred may be unusable when every item must be sorted. Repeat under at least two operating conditions and one benign fault. The fault test must not rely on unsafe contact with unguarded moving equipment. If laboratory hardware is unavailable, build a transparent simulation and state that physical validation remains unresolved.

**Suggested notebook entries.** Record the schematic version, parameter values and uncertainties, code or model revision, independent measurement reference, raw-data location, plots, limit-case result and outstanding assumptions. This creates a reproducible chain from requirement to model to observation. A screenshot without settings and raw observations is insufficient evidence.

## Questions and design exercises

1. **Conceptual distinction.** Describe the physical meaning of the central quantities in `t_total = sum(t_i)`. Which are commands, which are direct measurements and which require an estimate? Explain one realistic condition where the relationship should not be trusted.
2. **Quantitative extension.** Reproduce this lesson’s worked calculation from a blank page. Perturb the dominant input by 10% and compute the new prediction with units; estimate the sensitivity ratio and explain whether the effect is linear.
3. **Failure diagnosis.** Suppose a trial contradicts the predicted effect. Design two measurements that could separate the failure described above from a second cause, such as measurement bias, saturation, delay, friction or wiring reversal. Explain why merely repeating the same trial is inconclusive.
4. **Verification design.** Propose a bench or simulation protocol for time budgets and real-time behavior: variables held fixed, a sweep range, at least one held-out point, a pass/fail criterion, an independently observed quantity and a defined stop or abort condition. State which conclusions could not be supported by the resulting data.

## Study summary and next connection

A successful treatment of **time budgets and real-time behavior** includes the physical mechanism, transparent equation, numerical prediction, dimensional sanity check, uncertainty discussion and a falsifiable test. The next lesson changes part of the system, so retain a stable definition of the measured variable and the underlying coordinate or timing convention.


---

# U01-L05 — Hazards, interlocks and fail-safe states

**OpenSTEM Mechanical Engineering · Book 11: Mechatronics Engineering · Unit 1: System Architecture and Multidisciplinary Design.** Educational draft for university study; no hardware-specific safety certification is implied.

## Learning outcome and engineering question

Explain the physical mechanism behind **hazards, interlocks and fail-safe states** and identify the quantities that can be measured independently. Starting from a realistic unit model, calculate a nominal prediction, check what happens when the governing assumptions break down and propose a discriminating experiment. This lesson is part of a progressive integrated task: An automated inspection gate must classify objects, move them safely and leave a defensible record of its decisions.

**What success looks like.** By the end you should be able to defend the selected equation, label its physical units, derive or justify the result, explain a dominant failure mode, and design an observable test with an explicit acceptance criterion. Convert the verbal specification into variables with declared units, coordinate directions and an operating envelope. The purpose is a model that can be challenged, not an elegant formula without operational meaning.

## Conceptual model

A software stop command is different from a safety-rated independent stop path. Design normally de-energized outputs where appropriate, detect plausible stuck-on commands and ensure fault states are defined for communication loss and sensor disagreement. Safety claims need system-specific assessment. This particular concept belongs to the broader unit theme: Design a system from a traceable physical requirement rather than picking electronics first. Make a small system diagram showing where the relevant signal, mechanical load, power or timing variable enters and where its effect is actually observable. The diagram must distinguish the real plant from its estimate or representation.

**Why the distinction matters.** Trace the flow of matter, information and energy. For the integrated example, split a station into sensor, embedded controller, actuator driver and guarded mechanics. establish a signal and unit table before firmware implementation; mark the direction of every command and measurement. A plausible result can remain wrong if the coordinate frame, timing origin, sign convention or instrumentation location is inconsistent with the assembled machine.

## Mathematical representation and assumptions

A useful starting relationship is **`E_k = 0.5 m v^2`**. Read each term aloud with physical dimensions. The expression is a compact model, not a universal constitutive law: its assumptions are the governing physical regime, parameter definition and measurement method described above. State whether the relationship is exact within a defined idealization, an approximation, or an empirical fit.

In a design calculation, rounding should occur at reporting time. Retain guard digits during intermediate steps so that resolution errors are not mistaken for physical discrepancies. Next, identify at least one quantity in the expression that is independent and one that is dependent. If two independent inputs vary together, a single trial cannot identify their separate effects. List what remains constant in your derivation.

**Boundary check.** Consider reducing the principal input toward zero and increasing it within the permitted physical range. Does the result approach a sensible limit? Note when the formula would produce an unbounded, negative, or otherwise nonphysical output. Even a well-defined mathematical result should be rejected if it implies operation beyond an actuator limit or mechanical stop.

## Worked example with units

A 2.0 kg carriage moving at 1.5 m/s contains 2.25 J translational kinetic energy, not including rotating components. Rewrite the given numbers before substitution; explicitly carry their units through the equation. Compare the answer to a rough mental estimate and state a sensible number of significant figures. Do not interpret the displayed precision as measured accuracy. The calculation is synthetic unless independently verified against a particular device.

**Sensitivity experiment.** Repeat the calculation after changing one controlling quantity by +10% while keeping other stated inputs fixed. For a linear relationship, expect a proportional response in the appropriate variable; for a nonlinear one, compute the actual change and compare it with the local slope. Explain whether the chosen perturbation is realistic for the application.

**Dimensional audit.** Convert angles, voltages, forces, lengths and time to an explicitly declared convention before putting them in code. A numerical answer with the wrong units is not a small editorial error: it can change the actual machine motion or power demands by large factors. Record the conversion and the numerical rounding separately.

## Engineering integration and trade-offs

Architecture choices should be evaluated against worst-case throughput, environmental exposure, reset behavior and the ability to test the system without connecting hazardous mechanisms. Design reviews should ask which interfaces are shared between independent protective systems, because common-cause failures defeat apparent redundancy. For **hazards, interlocks and fail-safe states**, choose a realistic engineering constraint: supply capacity, maximum permissible temperature, mechanical clearance, sensor bandwidth, task deadline or acceptable uncertainty. Identify how the model interfaces with the preceding and following functions. For example, a correct sensor estimate may still arrive after the actuator can use it.

**Critical failure mode.** Assuming power removal causes immediate mechanical stopping ignores stored energy and inertia. Identify which physical measurements could distinguish this failure from an equally plausible alternative. Do not silently compensate for a failed measurement by increasing controller gains. When an estimate is suspect, favor a defined restricted state and transparent diagnostics.

**Design trade study.** Compare a simple implementation with a more instrumented one. The simple version may lower cost and code complexity; the instrumented version may expose hidden failure modes but increases wiring, calibration and software overhead. State the evidence that would justify the additional complexity, not a blanket preference for more sensors.

## Verification and reproducibility

A specific, falsifiable check is: Exercise limit-switch failure, emergency stop, watchdog timeout and power recovery with hazards physically contained. Define the measured output, sensor range, stimulus, trial count, recording rate and acceptance threshold. Include the expected direction of change before collecting data, and record every rejected measurement with an explanation.

**Robustness check.** Use an independently calibrated reference if possible. Comparing two software values derived from one biased sensor does not validate the measurement. Repeat under at least two operating conditions and one benign fault. The fault test must not rely on unsafe contact with unguarded moving equipment. If laboratory hardware is unavailable, build a transparent simulation and state that physical validation remains unresolved.

**Suggested notebook entries.** Record the schematic version, parameter values and uncertainties, code or model revision, independent measurement reference, raw-data location, plots, limit-case result and outstanding assumptions. This creates a reproducible chain from requirement to model to observation. A screenshot without settings and raw observations is insufficient evidence.

## Questions and design exercises

1. **Conceptual distinction.** Describe the physical meaning of the central quantities in `E_k = 0.5 m v^2`. Which are commands, which are direct measurements and which require an estimate? Explain one realistic condition where the relationship should not be trusted.
2. **Quantitative extension.** Reproduce this lesson’s worked calculation from a blank page. Perturb the dominant input by 10% and compute the new prediction with units; estimate the sensitivity ratio and explain whether the effect is linear.
3. **Failure diagnosis.** Suppose a trial contradicts the predicted effect. Design two measurements that could separate the failure described above from a second cause, such as measurement bias, saturation, delay, friction or wiring reversal. Explain why merely repeating the same trial is inconclusive.
4. **Verification design.** Propose a bench or simulation protocol for hazards, interlocks and fail-safe states: variables held fixed, a sweep range, at least one held-out point, a pass/fail criterion, an independently observed quantity and a defined stop or abort condition. State which conclusions could not be supported by the resulting data.

## Study summary and next connection

A successful treatment of **hazards, interlocks and fail-safe states** includes the physical mechanism, transparent equation, numerical prediction, dimensional sanity check, uncertainty discussion and a falsifiable test. The next lesson changes part of the system, so retain a stable definition of the measured variable and the underlying coordinate or timing convention.


---

