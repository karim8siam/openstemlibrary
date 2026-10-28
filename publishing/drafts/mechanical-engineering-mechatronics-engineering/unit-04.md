# Unit 04: Embedded Computing and Industrial Interfaces

**Course Code**: MCT 404 · **Level**: Advanced Undergraduate Engineering

## Unit Overview & Physical Foundations

This comprehensive university textbook unit covers the theoretical framework, physical modeling, mathematical governing equations, and engineering applications of **Embedded Computing and Industrial Interfaces**.

# U04-L01 — Scheduling, interrupts and execution budgets

**OpenSTEM Mechanical Engineering · Book 11: Mechatronics Engineering · Unit 4: Embedded Computing and Industrial Interfaces.** Educational draft for university study; no hardware-specific safety certification is implied.

## Learning outcome and engineering question

Explain the physical mechanism behind **scheduling, interrupts and execution budgets** and identify the quantities that can be measured independently. Starting from a realistic unit model, calculate a nominal prediction, check what happens when the governing assumptions break down and propose a discriminating experiment. This lesson is part of a progressive integrated task: The inspection gate communicates between microcontroller, motor drive, sensor board and supervisory computer.

**What success looks like.** By the end you should be able to defend the selected equation, label its physical units, derive or justify the result, explain a dominant failure mode, and design an observable test with an explicit acceptance criterion. Begin with a physical free-body, energy-flow or signal-flow representation before introducing a numerical model. The purpose is a model that can be challenged, not an elegant formula without operational meaning.

## Conceptual model

A periodic task must finish before its next release unless a deliberate overlap policy exists. Priorities, blocking, interrupt service time and shared-resource contention determine worst-case response. Use a monotonic clock for timing measurements. This particular concept belongs to the broader unit theme: Model real-time firmware and communication as physical system components. Make a small system diagram showing where the relevant signal, mechanical load, power or timing variable enters and where its effect is actually observable. The diagram must distinguish the real plant from its estimate or representation.

**Why the distinction matters.** Treat acquisition, computation and communications as a timed chain. For the integrated example, use one timestamp convention, define message age limits and state-machine transition guards, and include deterministic safe output behavior for every fault. A plausible result can remain wrong if the coordinate frame, timing origin, sign convention or instrumentation location is inconsistent with the assembled machine.

## Mathematical representation and assumptions

A useful starting relationship is **`utilization = sum(C_i/T_i)`**. Read each term aloud with physical dimensions. The expression is a compact model, not a universal constitutive law: its assumptions are the governing physical regime, parameter definition and measurement method described above. State whether the relationship is exact within a defined idealization, an approximation, or an empirical fit.

A derived relationship should be dimensionally homogeneous. If an angular quantity is used, declare whether trigonometric routines take radians. Distinguish electrical input power from useful output power. Next, identify at least one quantity in the expression that is independent and one that is dependent. If two independent inputs vary together, a single trial cannot identify their separate effects. List what remains constant in your derivation.

**Boundary check.** Consider reducing the principal input toward zero and increasing it within the permitted physical range. Does the result approach a sensible limit? Note when the formula would produce an unbounded, negative, or otherwise nonphysical output. Even a well-defined mathematical result should be rejected if it implies operation beyond an actuator limit or mechanical stop.

## Worked example with units

Tasks using 1 ms every 5 ms and 2 ms every 10 ms contribute a combined utilization of 0.40. Rewrite the given numbers before substitution; explicitly carry their units through the equation. Compare the answer to a rough mental estimate and state a sensible number of significant figures. Do not interpret the displayed precision as measured accuracy. The calculation is synthetic unless independently verified against a particular device.

**Sensitivity experiment.** Repeat the calculation after changing one controlling quantity by +10% while keeping other stated inputs fixed. For a linear relationship, expect a proportional response in the appropriate variable; for a nonlinear one, compute the actual change and compare it with the local slope. Explain whether the chosen perturbation is realistic for the application.

**Dimensional audit.** Convert angles, voltages, forces, lengths and time to an explicitly declared convention before putting them in code. A numerical answer with the wrong units is not a small editorial error: it can change the actual machine motion or power demands by large factors. Record the conversion and the numerical rounding separately.

## Engineering integration and trade-offs

A controller can compute correct numbers and still fail if it acts on stale data, loses synchronization or restarts in an unsafe state. Build observable diagnostics into the first prototype instead of retrofitting them after a missed deadline. For **scheduling, interrupts and execution budgets**, choose a realistic engineering constraint: supply capacity, maximum permissible temperature, mechanical clearance, sensor bandwidth, task deadline or acceptable uncertainty. Identify how the model interfaces with the preceding and following functions. For example, a correct sensor estimate may still arrive after the actuator can use it.

**Critical failure mode.** A CPU utilization below 100% does not by itself prove a particular real-time scheduling policy is feasible. Identify which physical measurements could distinguish this failure from an equally plausible alternative. Do not silently compensate for a failed measurement by increasing controller gains. When an estimate is suspect, favor a defined restricted state and transparent diagnostics.

**Design trade study.** Compare a simple implementation with a more instrumented one. The simple version may lower cost and code complexity; the instrumented version may expose hidden failure modes but increases wiring, calibration and software overhead. State the evidence that would justify the additional complexity, not a blanket preference for more sensors.

## Verification and reproducibility

A specific, falsifiable check is: Measure worst observed execution and blocking during concurrent sensor, communications and logging load. Define the measured output, sensor range, stimulus, trial count, recording rate and acceptance threshold. Include the expected direction of change before collecting data, and record every rejected measurement with an explanation.

**Robustness check.** Vary one parameter at a time during fault isolation; note that real production environments may combine several disturbances. Repeat under at least two operating conditions and one benign fault. The fault test must not rely on unsafe contact with unguarded moving equipment. If laboratory hardware is unavailable, build a transparent simulation and state that physical validation remains unresolved.

**Suggested notebook entries.** Record the schematic version, parameter values and uncertainties, code or model revision, independent measurement reference, raw-data location, plots, limit-case result and outstanding assumptions. This creates a reproducible chain from requirement to model to observation. A screenshot without settings and raw observations is insufficient evidence.

## Questions and design exercises

1. **Conceptual distinction.** Describe the physical meaning of the central quantities in `utilization = sum(C_i/T_i)`. Which are commands, which are direct measurements and which require an estimate? Explain one realistic condition where the relationship should not be trusted.
2. **Quantitative extension.** Reproduce this lesson’s worked calculation from a blank page. Perturb the dominant input by 10% and compute the new prediction with units; estimate the sensitivity ratio and explain whether the effect is linear.
3. **Failure diagnosis.** Suppose a trial contradicts the predicted effect. Design two measurements that could separate the failure described above from a second cause, such as measurement bias, saturation, delay, friction or wiring reversal. Explain why merely repeating the same trial is inconclusive.
4. **Verification design.** Propose a bench or simulation protocol for scheduling, interrupts and execution budgets: variables held fixed, a sweep range, at least one held-out point, a pass/fail criterion, an independently observed quantity and a defined stop or abort condition. State which conclusions could not be supported by the resulting data.

## Study summary and next connection

A successful treatment of **scheduling, interrupts and execution budgets** includes the physical mechanism, transparent equation, numerical prediction, dimensional sanity check, uncertainty discussion and a falsifiable test. The next lesson changes part of the system, so retain a stable definition of the measured variable and the underlying coordinate or timing convention.


---

# U04-L02 — PWM, H-bridges and current measurement

**OpenSTEM Mechanical Engineering · Book 11: Mechatronics Engineering · Unit 4: Embedded Computing and Industrial Interfaces.** Educational draft for university study; no hardware-specific safety certification is implied.

## Learning outcome and engineering question

Explain the physical mechanism behind **pwm, h-bridges and current measurement** and identify the quantities that can be measured independently. Starting from a realistic unit model, calculate a nominal prediction, check what happens when the governing assumptions break down and propose a discriminating experiment. This lesson is part of a progressive integrated task: The inspection gate communicates between microcontroller, motor drive, sensor board and supervisory computer.

**What success looks like.** By the end you should be able to defend the selected equation, label its physical units, derive or justify the result, explain a dominant failure mode, and design an observable test with an explicit acceptance criterion. Convert the verbal specification into variables with declared units, coordinate directions and an operating envelope. The purpose is a model that can be challenged, not an elegant formula without operational meaning.

## Conceptual model

Pulse-width modulation changes average terminal voltage under assumptions about switching frequency and load dynamics. H-bridges need dead time and protection against shoot-through; current sensing must preserve polarity and accommodate switching ripple. This particular concept belongs to the broader unit theme: Model real-time firmware and communication as physical system components. Make a small system diagram showing where the relevant signal, mechanical load, power or timing variable enters and where its effect is actually observable. The diagram must distinguish the real plant from its estimate or representation.

**Why the distinction matters.** Treat acquisition, computation and communications as a timed chain. For the integrated example, use one timestamp convention, define message age limits and state-machine transition guards, and include deterministic safe output behavior for every fault. A plausible result can remain wrong if the coordinate frame, timing origin, sign convention or instrumentation location is inconsistent with the assembled machine.

## Mathematical representation and assumptions

A useful starting relationship is **`V_avg ≈ D V_bus`**. Read each term aloud with physical dimensions. The expression is a compact model, not a universal constitutive law: its assumptions are the governing physical regime, parameter definition and measurement method described above. State whether the relationship is exact within a defined idealization, an approximation, or an empirical fit.

An equation is only as good as its measurement model. Quantities denoted with a command subscript are not automatically the same as physical values recorded at a sensor. Next, identify at least one quantity in the expression that is independent and one that is dependent. If two independent inputs vary together, a single trial cannot identify their separate effects. List what remains constant in your derivation.

**Boundary check.** Consider reducing the principal input toward zero and increasing it within the permitted physical range. Does the result approach a sensible limit? Note when the formula would produce an unbounded, negative, or otherwise nonphysical output. Even a well-defined mathematical result should be rejected if it implies operation beyond an actuator limit or mechanical stop.

## Worked example with units

For duty ratio 0.35 and a 24 V bus, the idealized average is 8.4 V. Rewrite the given numbers before substitution; explicitly carry their units through the equation. Compare the answer to a rough mental estimate and state a sensible number of significant figures. Do not interpret the displayed precision as measured accuracy. The calculation is synthetic unless independently verified against a particular device.

**Sensitivity experiment.** Repeat the calculation after changing one controlling quantity by +10% while keeping other stated inputs fixed. For a linear relationship, expect a proportional response in the appropriate variable; for a nonlinear one, compute the actual change and compare it with the local slope. Explain whether the chosen perturbation is realistic for the application.

**Dimensional audit.** Convert angles, voltages, forces, lengths and time to an explicitly declared convention before putting them in code. A numerical answer with the wrong units is not a small editorial error: it can change the actual machine motion or power demands by large factors. Record the conversion and the numerical rounding separately.

## Engineering integration and trade-offs

A controller can compute correct numbers and still fail if it acts on stale data, loses synchronization or restarts in an unsafe state. Build observable diagnostics into the first prototype instead of retrofitting them after a missed deadline. For **pwm, h-bridges and current measurement**, choose a realistic engineering constraint: supply capacity, maximum permissible temperature, mechanical clearance, sensor bandwidth, task deadline or acceptable uncertainty. Identify how the model interfaces with the preceding and following functions. For example, a correct sensor estimate may still arrive after the actuator can use it.

**Critical failure mode.** Equating average voltage to instantaneous motor torque neglects current dynamics and back EMF. Identify which physical measurements could distinguish this failure from an equally plausible alternative. Do not silently compensate for a failed measurement by increasing controller gains. When an estimate is suspect, favor a defined restricted state and transparent diagnostics.

**Design trade study.** Compare a simple implementation with a more instrumented one. The simple version may lower cost and code complexity; the instrumented version may expose hidden failure modes but increases wiring, calibration and software overhead. State the evidence that would justify the additional complexity, not a blanket preference for more sensors.

## Verification and reproducibility

A specific, falsifiable check is: Inspect switching edges and measured current with appropriate isolated equipment and safe probing procedures. Define the measured output, sensor range, stimulus, trial count, recording rate and acceptance threshold. Include the expected direction of change before collecting data, and record every rejected measurement with an explanation.

**Robustness check.** Predefine the pass/fail criterion and archive unsuccessful traces. Changing the limit after viewing the data removes the meaning of acceptance testing. Repeat under at least two operating conditions and one benign fault. The fault test must not rely on unsafe contact with unguarded moving equipment. If laboratory hardware is unavailable, build a transparent simulation and state that physical validation remains unresolved.

**Suggested notebook entries.** Record the schematic version, parameter values and uncertainties, code or model revision, independent measurement reference, raw-data location, plots, limit-case result and outstanding assumptions. This creates a reproducible chain from requirement to model to observation. A screenshot without settings and raw observations is insufficient evidence.

## Questions and design exercises

1. **Conceptual distinction.** Describe the physical meaning of the central quantities in `V_avg ≈ D V_bus`. Which are commands, which are direct measurements and which require an estimate? Explain one realistic condition where the relationship should not be trusted.
2. **Quantitative extension.** Reproduce this lesson’s worked calculation from a blank page. Perturb the dominant input by 10% and compute the new prediction with units; estimate the sensitivity ratio and explain whether the effect is linear.
3. **Failure diagnosis.** Suppose a trial contradicts the predicted effect. Design two measurements that could separate the failure described above from a second cause, such as measurement bias, saturation, delay, friction or wiring reversal. Explain why merely repeating the same trial is inconclusive.
4. **Verification design.** Propose a bench or simulation protocol for pwm, h-bridges and current measurement: variables held fixed, a sweep range, at least one held-out point, a pass/fail criterion, an independently observed quantity and a defined stop or abort condition. State which conclusions could not be supported by the resulting data.

## Study summary and next connection

A successful treatment of **pwm, h-bridges and current measurement** includes the physical mechanism, transparent equation, numerical prediction, dimensional sanity check, uncertainty discussion and a falsifiable test. The next lesson changes part of the system, so retain a stable definition of the measured variable and the underlying coordinate or timing convention.


---

# U04-L03 — SPI, I2C, CAN and communication diagnostics

**OpenSTEM Mechanical Engineering · Book 11: Mechatronics Engineering · Unit 4: Embedded Computing and Industrial Interfaces.** Educational draft for university study; no hardware-specific safety certification is implied.

## Learning outcome and engineering question

Explain the physical mechanism behind **spi, i2c, can and communication diagnostics** and identify the quantities that can be measured independently. Starting from a realistic unit model, calculate a nominal prediction, check what happens when the governing assumptions break down and propose a discriminating experiment. This lesson is part of a progressive integrated task: The inspection gate communicates between microcontroller, motor drive, sensor board and supervisory computer.

**What success looks like.** By the end you should be able to defend the selected equation, label its physical units, derive or justify the result, explain a dominant failure mode, and design an observable test with an explicit acceptance criterion. Separate ideal mathematical behavior from calibration error, deadband, quantization and machine-level uncertainty. The purpose is a model that can be challenged, not an elegant formula without operational meaning.

## Conceptual model

SPI, I2C and CAN have different electrical topologies, arbitration and failure characteristics. A message received without a bit error can still be stale or logically inconsistent. Add sequence numbers, timestamps and stale-data policies at the application layer. This particular concept belongs to the broader unit theme: Model real-time firmware and communication as physical system components. Make a small system diagram showing where the relevant signal, mechanical load, power or timing variable enters and where its effect is actually observable. The diagram must distinguish the real plant from its estimate or representation.

**Why the distinction matters.** Treat acquisition, computation and communications as a timed chain. For the integrated example, use one timestamp convention, define message age limits and state-machine transition guards, and include deterministic safe output behavior for every fault. A plausible result can remain wrong if the coordinate frame, timing origin, sign convention or instrumentation location is inconsistent with the assembled machine.

## Mathematical representation and assumptions

A useful starting relationship is **`t_bits = n_bits / bit_rate`**. Read each term aloud with physical dimensions. The expression is a compact model, not a universal constitutive law: its assumptions are the governing physical regime, parameter definition and measurement method described above. State whether the relationship is exact within a defined idealization, an approximation, or an empirical fit.

Model coefficients and initial conditions need uncertainty bounds. The sensitivity of a result to these inputs matters as much as its nominal numerical value. Next, identify at least one quantity in the expression that is independent and one that is dependent. If two independent inputs vary together, a single trial cannot identify their separate effects. List what remains constant in your derivation.

**Boundary check.** Consider reducing the principal input toward zero and increasing it within the permitted physical range. Does the result approach a sensible limit? Note when the formula would produce an unbounded, negative, or otherwise nonphysical output. Even a well-defined mathematical result should be rejected if it implies operation beyond an actuator limit or mechanical stop.

## Worked example with units

A 128-bit payload at an ideal 500 kbit/s occupies at least 0.256 ms before framing and bus arbitration. Rewrite the given numbers before substitution; explicitly carry their units through the equation. Compare the answer to a rough mental estimate and state a sensible number of significant figures. Do not interpret the displayed precision as measured accuracy. The calculation is synthetic unless independently verified against a particular device.

**Sensitivity experiment.** Repeat the calculation after changing one controlling quantity by +10% while keeping other stated inputs fixed. For a linear relationship, expect a proportional response in the appropriate variable; for a nonlinear one, compute the actual change and compare it with the local slope. Explain whether the chosen perturbation is realistic for the application.

**Dimensional audit.** Convert angles, voltages, forces, lengths and time to an explicitly declared convention before putting them in code. A numerical answer with the wrong units is not a small editorial error: it can change the actual machine motion or power demands by large factors. Record the conversion and the numerical rounding separately.

## Engineering integration and trade-offs

A controller can compute correct numbers and still fail if it acts on stale data, loses synchronization or restarts in an unsafe state. Build observable diagnostics into the first prototype instead of retrofitting them after a missed deadline. For **spi, i2c, can and communication diagnostics**, choose a realistic engineering constraint: supply capacity, maximum permissible temperature, mechanical clearance, sensor bandwidth, task deadline or acceptable uncertainty. Identify how the model interfaces with the preceding and following functions. For example, a correct sensor estimate may still arrive after the actuator can use it.

**Critical failure mode.** Ignoring arbitration, retransmission and wiring noise causes overly optimistic deadlines. Identify which physical measurements could distinguish this failure from an equally plausible alternative. Do not silently compensate for a failed measurement by increasing controller gains. When an estimate is suspect, favor a defined restricted state and transparent diagnostics.

**Design trade study.** Compare a simple implementation with a more instrumented one. The simple version may lower cost and code complexity; the instrumented version may expose hidden failure modes but increases wiring, calibration and software overhead. State the evidence that would justify the additional complexity, not a blanket preference for more sensors.

## Verification and reproducibility

A specific, falsifiable check is: Corrupt, delay and suppress messages in a bench test and verify timeout and recovery responses. Define the measured output, sensor range, stimulus, trial count, recording rate and acceptance threshold. Include the expected direction of change before collecting data, and record every rejected measurement with an explanation.

**Robustness check.** Test shutdown and restart explicitly. Recovering to a safe known state is part of functionality, not an optional maintenance feature. Repeat under at least two operating conditions and one benign fault. The fault test must not rely on unsafe contact with unguarded moving equipment. If laboratory hardware is unavailable, build a transparent simulation and state that physical validation remains unresolved.

**Suggested notebook entries.** Record the schematic version, parameter values and uncertainties, code or model revision, independent measurement reference, raw-data location, plots, limit-case result and outstanding assumptions. This creates a reproducible chain from requirement to model to observation. A screenshot without settings and raw observations is insufficient evidence.

## Questions and design exercises

1. **Conceptual distinction.** Describe the physical meaning of the central quantities in `t_bits = n_bits / bit_rate`. Which are commands, which are direct measurements and which require an estimate? Explain one realistic condition where the relationship should not be trusted.
2. **Quantitative extension.** Reproduce this lesson’s worked calculation from a blank page. Perturb the dominant input by 10% and compute the new prediction with units; estimate the sensitivity ratio and explain whether the effect is linear.
3. **Failure diagnosis.** Suppose a trial contradicts the predicted effect. Design two measurements that could separate the failure described above from a second cause, such as measurement bias, saturation, delay, friction or wiring reversal. Explain why merely repeating the same trial is inconclusive.
4. **Verification design.** Propose a bench or simulation protocol for spi, i2c, can and communication diagnostics: variables held fixed, a sweep range, at least one held-out point, a pass/fail criterion, an independently observed quantity and a defined stop or abort condition. State which conclusions could not be supported by the resulting data.

## Study summary and next connection

A successful treatment of **spi, i2c, can and communication diagnostics** includes the physical mechanism, transparent equation, numerical prediction, dimensional sanity check, uncertainty discussion and a falsifiable test. The next lesson changes part of the system, so retain a stable definition of the measured variable and the underlying coordinate or timing convention.


---

# U04-L04 — ADC quantization, references and ground design

**OpenSTEM Mechanical Engineering · Book 11: Mechatronics Engineering · Unit 4: Embedded Computing and Industrial Interfaces.** Educational draft for university study; no hardware-specific safety certification is implied.

## Learning outcome and engineering question

Explain the physical mechanism behind **adc quantization, references and ground design** and identify the quantities that can be measured independently. Starting from a realistic unit model, calculate a nominal prediction, check what happens when the governing assumptions break down and propose a discriminating experiment. This lesson is part of a progressive integrated task: The inspection gate communicates between microcontroller, motor drive, sensor board and supervisory computer.

**What success looks like.** By the end you should be able to defend the selected equation, label its physical units, derive or justify the result, explain a dominant failure mode, and design an observable test with an explicit acceptance criterion. Show what happens at a limiting case before relying on an intermediate operating point. The purpose is a model that can be challenged, not an elegant formula without operational meaning.

## Conceptual model

An ADC number is meaningful only with its reference voltage, gain, offset and analog bandwidth. Quantization noise is often less important than supply ripple, input impedance or grounding. Signal conditioning and layout matter. This particular concept belongs to the broader unit theme: Model real-time firmware and communication as physical system components. Make a small system diagram showing where the relevant signal, mechanical load, power or timing variable enters and where its effect is actually observable. The diagram must distinguish the real plant from its estimate or representation.

**Why the distinction matters.** Treat acquisition, computation and communications as a timed chain. For the integrated example, use one timestamp convention, define message age limits and state-machine transition guards, and include deterministic safe output behavior for every fault. A plausible result can remain wrong if the coordinate frame, timing origin, sign convention or instrumentation location is inconsistent with the assembled machine.

## Mathematical representation and assumptions

A useful starting relationship is **`LSB = V_ref/2^n`**. Read each term aloud with physical dimensions. The expression is a compact model, not a universal constitutive law: its assumptions are the governing physical regime, parameter definition and measurement method described above. State whether the relationship is exact within a defined idealization, an approximation, or an empirical fit.

For sampled systems, timestamp the input and output to distinguish propagation delay from genuine plant dynamics. An unmeasured delay can invalidate an otherwise sound formula. Next, identify at least one quantity in the expression that is independent and one that is dependent. If two independent inputs vary together, a single trial cannot identify their separate effects. List what remains constant in your derivation.

**Boundary check.** Consider reducing the principal input toward zero and increasing it within the permitted physical range. Does the result approach a sensible limit? Note when the formula would produce an unbounded, negative, or otherwise nonphysical output. Even a well-defined mathematical result should be rejected if it implies operation beyond an actuator limit or mechanical stop.

## Worked example with units

For a 12-bit converter with 3.3 V reference, the nominal ideal step is about 0.806 mV. Rewrite the given numbers before substitution; explicitly carry their units through the equation. Compare the answer to a rough mental estimate and state a sensible number of significant figures. Do not interpret the displayed precision as measured accuracy. The calculation is synthetic unless independently verified against a particular device.

**Sensitivity experiment.** Repeat the calculation after changing one controlling quantity by +10% while keeping other stated inputs fixed. For a linear relationship, expect a proportional response in the appropriate variable; for a nonlinear one, compute the actual change and compare it with the local slope. Explain whether the chosen perturbation is realistic for the application.

**Dimensional audit.** Convert angles, voltages, forces, lengths and time to an explicitly declared convention before putting them in code. A numerical answer with the wrong units is not a small editorial error: it can change the actual machine motion or power demands by large factors. Record the conversion and the numerical rounding separately.

## Engineering integration and trade-offs

A controller can compute correct numbers and still fail if it acts on stale data, loses synchronization or restarts in an unsafe state. Build observable diagnostics into the first prototype instead of retrofitting them after a missed deadline. For **adc quantization, references and ground design**, choose a realistic engineering constraint: supply capacity, maximum permissible temperature, mechanical clearance, sensor bandwidth, task deadline or acceptable uncertainty. Identify how the model interfaces with the preceding and following functions. For example, a correct sensor estimate may still arrive after the actuator can use it.

**Critical failure mode.** Treating the number of ADC bits as effective resolution ignores noise and integral nonlinearity. Identify which physical measurements could distinguish this failure from an equally plausible alternative. Do not silently compensate for a failed measurement by increasing controller gains. When an estimate is suspect, favor a defined restricted state and transparent diagnostics.

**Design trade study.** Compare a simple implementation with a more instrumented one. The simple version may lower cost and code complexity; the instrumented version may expose hidden failure modes but increases wiring, calibration and software overhead. State the evidence that would justify the additional complexity, not a blanket preference for more sensors.

## Verification and reproducibility

A specific, falsifiable check is: Short the input to a clean reference and sweep calibrated voltages to estimate effective noise and nonlinearity. Define the measured output, sensor range, stimulus, trial count, recording rate and acceptance threshold. Include the expected direction of change before collecting data, and record every rejected measurement with an explanation.

**Robustness check.** Record the maximum as well as the average. A machine that misses one deadline in a hundred may be unusable when every item must be sorted. Repeat under at least two operating conditions and one benign fault. The fault test must not rely on unsafe contact with unguarded moving equipment. If laboratory hardware is unavailable, build a transparent simulation and state that physical validation remains unresolved.

**Suggested notebook entries.** Record the schematic version, parameter values and uncertainties, code or model revision, independent measurement reference, raw-data location, plots, limit-case result and outstanding assumptions. This creates a reproducible chain from requirement to model to observation. A screenshot without settings and raw observations is insufficient evidence.

## Questions and design exercises

1. **Conceptual distinction.** Describe the physical meaning of the central quantities in `LSB = V_ref/2^n`. Which are commands, which are direct measurements and which require an estimate? Explain one realistic condition where the relationship should not be trusted.
2. **Quantitative extension.** Reproduce this lesson’s worked calculation from a blank page. Perturb the dominant input by 10% and compute the new prediction with units; estimate the sensitivity ratio and explain whether the effect is linear.
3. **Failure diagnosis.** Suppose a trial contradicts the predicted effect. Design two measurements that could separate the failure described above from a second cause, such as measurement bias, saturation, delay, friction or wiring reversal. Explain why merely repeating the same trial is inconclusive.
4. **Verification design.** Propose a bench or simulation protocol for adc quantization, references and ground design: variables held fixed, a sweep range, at least one held-out point, a pass/fail criterion, an independently observed quantity and a defined stop or abort condition. State which conclusions could not be supported by the resulting data.

## Study summary and next connection

A successful treatment of **adc quantization, references and ground design** includes the physical mechanism, transparent equation, numerical prediction, dimensional sanity check, uncertainty discussion and a falsifiable test. The next lesson changes part of the system, so retain a stable definition of the measured variable and the underlying coordinate or timing convention.


---

# U04-L05 — State machines, watchdogs and fault recovery

**OpenSTEM Mechanical Engineering · Book 11: Mechatronics Engineering · Unit 4: Embedded Computing and Industrial Interfaces.** Educational draft for university study; no hardware-specific safety certification is implied.

## Learning outcome and engineering question

Explain the physical mechanism behind **state machines, watchdogs and fault recovery** and identify the quantities that can be measured independently. Starting from a realistic unit model, calculate a nominal prediction, check what happens when the governing assumptions break down and propose a discriminating experiment. This lesson is part of a progressive integrated task: The inspection gate communicates between microcontroller, motor drive, sensor board and supervisory computer.

**What success looks like.** By the end you should be able to defend the selected equation, label its physical units, derive or justify the result, explain a dominant failure mode, and design an observable test with an explicit acceptance criterion. Use two independent ways of checking a result: dimensional reasoning and either a measurement or a numerical reproduction. The purpose is a model that can be challenged, not an elegant formula without operational meaning.

## Conceptual model

State machines make preconditions explicit: idle, homing, enabled, running, fault, and recovery. A watchdog detects certain software stalls but not incorrect control decisions. Recovery requires a known physical state and must not automatically re-enable hazardous motion. This particular concept belongs to the broader unit theme: Model real-time firmware and communication as physical system components. Make a small system diagram showing where the relevant signal, mechanical load, power or timing variable enters and where its effect is actually observable. The diagram must distinguish the real plant from its estimate or representation.

**Why the distinction matters.** Treat acquisition, computation and communications as a timed chain. For the integrated example, use one timestamp convention, define message age limits and state-machine transition guards, and include deterministic safe output behavior for every fault. A plausible result can remain wrong if the coordinate frame, timing origin, sign convention or instrumentation location is inconsistent with the assembled machine.

## Mathematical representation and assumptions

A useful starting relationship is **`t_fault = t_detect + t_disable`**. Read each term aloud with physical dimensions. The expression is a compact model, not a universal constitutive law: its assumptions are the governing physical regime, parameter definition and measurement method described above. State whether the relationship is exact within a defined idealization, an approximation, or an empirical fit.

In a design calculation, rounding should occur at reporting time. Retain guard digits during intermediate steps so that resolution errors are not mistaken for physical discrepancies. Next, identify at least one quantity in the expression that is independent and one that is dependent. If two independent inputs vary together, a single trial cannot identify their separate effects. List what remains constant in your derivation.

**Boundary check.** Consider reducing the principal input toward zero and increasing it within the permitted physical range. Does the result approach a sensible limit? Note when the formula would produce an unbounded, negative, or otherwise nonphysical output. Even a well-defined mathematical result should be rejected if it implies operation beyond an actuator limit or mechanical stop.

## Worked example with units

If detection takes 12 ms and output disable takes 8 ms, fault command latency is 20 ms, excluding mechanical stopping. Rewrite the given numbers before substitution; explicitly carry their units through the equation. Compare the answer to a rough mental estimate and state a sensible number of significant figures. Do not interpret the displayed precision as measured accuracy. The calculation is synthetic unless independently verified against a particular device.

**Sensitivity experiment.** Repeat the calculation after changing one controlling quantity by +10% while keeping other stated inputs fixed. For a linear relationship, expect a proportional response in the appropriate variable; for a nonlinear one, compute the actual change and compare it with the local slope. Explain whether the chosen perturbation is realistic for the application.

**Dimensional audit.** Convert angles, voltages, forces, lengths and time to an explicitly declared convention before putting them in code. A numerical answer with the wrong units is not a small editorial error: it can change the actual machine motion or power demands by large factors. Record the conversion and the numerical rounding separately.

## Engineering integration and trade-offs

A controller can compute correct numbers and still fail if it acts on stale data, loses synchronization or restarts in an unsafe state. Build observable diagnostics into the first prototype instead of retrofitting them after a missed deadline. For **state machines, watchdogs and fault recovery**, choose a realistic engineering constraint: supply capacity, maximum permissible temperature, mechanical clearance, sensor bandwidth, task deadline or acceptable uncertainty. Identify how the model interfaces with the preceding and following functions. For example, a correct sensor estimate may still arrive after the actuator can use it.

**Critical failure mode.** A reboot that restores motion without re-homing can turn stale coordinates into dangerous commands. Identify which physical measurements could distinguish this failure from an equally plausible alternative. Do not silently compensate for a failed measurement by increasing controller gains. When an estimate is suspect, favor a defined restricted state and transparent diagnostics.

**Design trade study.** Compare a simple implementation with a more instrumented one. The simple version may lower cost and code complexity; the instrumented version may expose hidden failure modes but increases wiring, calibration and software overhead. State the evidence that would justify the additional complexity, not a blanket preference for more sensors.

## Verification and reproducibility

A specific, falsifiable check is: Exercise every illegal transition, reset during motion and power-up with damaged sensor data. Define the measured output, sensor range, stimulus, trial count, recording rate and acceptance threshold. Include the expected direction of change before collecting data, and record every rejected measurement with an explanation.

**Robustness check.** Use an independently calibrated reference if possible. Comparing two software values derived from one biased sensor does not validate the measurement. Repeat under at least two operating conditions and one benign fault. The fault test must not rely on unsafe contact with unguarded moving equipment. If laboratory hardware is unavailable, build a transparent simulation and state that physical validation remains unresolved.

**Suggested notebook entries.** Record the schematic version, parameter values and uncertainties, code or model revision, independent measurement reference, raw-data location, plots, limit-case result and outstanding assumptions. This creates a reproducible chain from requirement to model to observation. A screenshot without settings and raw observations is insufficient evidence.

## Questions and design exercises

1. **Conceptual distinction.** Describe the physical meaning of the central quantities in `t_fault = t_detect + t_disable`. Which are commands, which are direct measurements and which require an estimate? Explain one realistic condition where the relationship should not be trusted.
2. **Quantitative extension.** Reproduce this lesson’s worked calculation from a blank page. Perturb the dominant input by 10% and compute the new prediction with units; estimate the sensitivity ratio and explain whether the effect is linear.
3. **Failure diagnosis.** Suppose a trial contradicts the predicted effect. Design two measurements that could separate the failure described above from a second cause, such as measurement bias, saturation, delay, friction or wiring reversal. Explain why merely repeating the same trial is inconclusive.
4. **Verification design.** Propose a bench or simulation protocol for state machines, watchdogs and fault recovery: variables held fixed, a sweep range, at least one held-out point, a pass/fail criterion, an independently observed quantity and a defined stop or abort condition. State which conclusions could not be supported by the resulting data.

## Study summary and next connection

A successful treatment of **state machines, watchdogs and fault recovery** includes the physical mechanism, transparent equation, numerical prediction, dimensional sanity check, uncertainty discussion and a falsifiable test. The next lesson changes part of the system, so retain a stable definition of the measured variable and the underlying coordinate or timing convention.


---

