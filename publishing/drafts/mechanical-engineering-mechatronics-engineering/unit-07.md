# Unit 07: Integration, Diagnostics and Verification

**Course Code**: MCT 407 · **Level**: Advanced Undergraduate Engineering

## Unit Overview & Physical Foundations

This comprehensive university textbook unit covers the theoretical framework, physical modeling, mathematical governing equations, and engineering applications of **Integration, Diagnostics and Verification**.

# U07-L01 — Requirements-based verification matrix

**OpenSTEM Mechanical Engineering · Book 11: Mechatronics Engineering · Unit 7: Integration, Diagnostics and Verification.** Educational draft for university study; no hardware-specific safety certification is implied.

## Learning outcome and engineering question

Explain the physical mechanism behind **requirements-based verification matrix** and identify the quantities that can be measured independently. Starting from a realistic unit model, calculate a nominal prediction, check what happens when the governing assumptions break down and propose a discriminating experiment. This lesson is part of a progressive integrated task: A benchtop automation prototype must withstand startup transients, noisy signals, mechanical alignment and recovery from faults.

**What success looks like.** By the end you should be able to defend the selected equation, label its physical units, derive or justify the result, explain a dominant failure mode, and design an observable test with an explicit acceptance criterion. Show what happens at a limiting case before relying on an intermediate operating point. The purpose is a model that can be challenged, not an elegant formula without operational meaning.

## Conceptual model

Verification links each measurable requirement to a method, equipment, acceptance threshold and recorded result. Use inspection for wiring identity, analysis for derived margins, tests for observed response, and demonstrations only where performance is directly observable. This particular concept belongs to the broader unit theme: A verified subsystem does not imply a verified integrated machine. Make a small system diagram showing where the relevant signal, mechanical load, power or timing variable enters and where its effect is actually observable. The diagram must distinguish the real plant from its estimate or representation.

**Why the distinction matters.** Make each claim falsifiable by a named test and acceptance threshold. For the integrated example, create a traceability table that links each observed failure to a candidate mechanism, controlled change, retest and revised requirement. A plausible result can remain wrong if the coordinate frame, timing origin, sign convention or instrumentation location is inconsistent with the assembled machine.

## Mathematical representation and assumptions

A useful starting relationship is **`margin = limit - measured`**. Read each term aloud with physical dimensions. The expression is a compact model, not a universal constitutive law: its assumptions are the governing physical regime, parameter definition and measurement method described above. State whether the relationship is exact within a defined idealization, an approximation, or an empirical fit.

A derived relationship should be dimensionally homogeneous. If an angular quantity is used, declare whether trigonometric routines take radians. Distinguish electrical input power from useful output power. Next, identify at least one quantity in the expression that is independent and one that is dependent. If two independent inputs vary together, a single trial cannot identify their separate effects. List what remains constant in your derivation.

**Boundary check.** Consider reducing the principal input toward zero and increasing it within the permitted physical range. Does the result approach a sensible limit? Note when the formula would produce an unbounded, negative, or otherwise nonphysical output. Even a well-defined mathematical result should be rejected if it implies operation beyond an actuator limit or mechanical stop.

## Worked example with units

If allowed position error is 0.50 mm and the measured worst test error is 0.32 mm, observed margin is 0.18 mm for that test, not proof of all environments. Rewrite the given numbers before substitution; explicitly carry their units through the equation. Compare the answer to a rough mental estimate and state a sensible number of significant figures. Do not interpret the displayed precision as measured accuracy. The calculation is synthetic unless independently verified against a particular device.

**Sensitivity experiment.** Repeat the calculation after changing one controlling quantity by +10% while keeping other stated inputs fixed. For a linear relationship, expect a proportional response in the appropriate variable; for a nonlinear one, compute the actual change and compare it with the local slope. Explain whether the chosen perturbation is realistic for the application.

**Dimensional audit.** Convert angles, voltages, forces, lengths and time to an explicitly declared convention before putting them in code. A numerical answer with the wrong units is not a small editorial error: it can change the actual machine motion or power demands by large factors. Record the conversion and the numerical rounding separately.

## Engineering integration and trade-offs

Testing only at nominal operating conditions creates fragile systems. Design margins need confidence intervals, calibration references and explicit handling of failed runs; a dataset without its firmware version and wiring revision is difficult to reproduce. For **requirements-based verification matrix**, choose a realistic engineering constraint: supply capacity, maximum permissible temperature, mechanical clearance, sensor bandwidth, task deadline or acceptable uncertainty. Identify how the model interfaces with the preceding and following functions. For example, a correct sensor estimate may still arrive after the actuator can use it.

**Critical failure mode.** A single successful run lacks statistically meaningful coverage of variations and defects. Identify which physical measurements could distinguish this failure from an equally plausible alternative. Do not silently compensate for a failed measurement by increasing controller gains. When an estimate is suspect, favor a defined restricted state and transparent diagnostics.

**Design trade study.** Compare a simple implementation with a more instrumented one. The simple version may lower cost and code complexity; the instrumented version may expose hidden failure modes but increases wiring, calibration and software overhead. State the evidence that would justify the additional complexity, not a blanket preference for more sensors.

## Verification and reproducibility

A specific, falsifiable check is: Create a requirement-ID table with tests for nominal, boundary, fault and restart conditions. Define the measured output, sensor range, stimulus, trial count, recording rate and acceptance threshold. Include the expected direction of change before collecting data, and record every rejected measurement with an explanation.

**Robustness check.** Vary one parameter at a time during fault isolation; note that real production environments may combine several disturbances. Repeat under at least two operating conditions and one benign fault. The fault test must not rely on unsafe contact with unguarded moving equipment. If laboratory hardware is unavailable, build a transparent simulation and state that physical validation remains unresolved.

**Suggested notebook entries.** Record the schematic version, parameter values and uncertainties, code or model revision, independent measurement reference, raw-data location, plots, limit-case result and outstanding assumptions. This creates a reproducible chain from requirement to model to observation. A screenshot without settings and raw observations is insufficient evidence.

## Questions and design exercises

1. **Conceptual distinction.** Describe the physical meaning of the central quantities in `margin = limit - measured`. Which are commands, which are direct measurements and which require an estimate? Explain one realistic condition where the relationship should not be trusted.
2. **Quantitative extension.** Reproduce this lesson’s worked calculation from a blank page. Perturb the dominant input by 10% and compute the new prediction with units; estimate the sensitivity ratio and explain whether the effect is linear.
3. **Failure diagnosis.** Suppose a trial contradicts the predicted effect. Design two measurements that could separate the failure described above from a second cause, such as measurement bias, saturation, delay, friction or wiring reversal. Explain why merely repeating the same trial is inconclusive.
4. **Verification design.** Propose a bench or simulation protocol for requirements-based verification matrix: variables held fixed, a sweep range, at least one held-out point, a pass/fail criterion, an independently observed quantity and a defined stop or abort condition. State which conclusions could not be supported by the resulting data.

## Study summary and next connection

A successful treatment of **requirements-based verification matrix** includes the physical mechanism, transparent equation, numerical prediction, dimensional sanity check, uncertainty discussion and a falsifiable test. The next lesson changes part of the system, so retain a stable definition of the measured variable and the underlying coordinate or timing convention.


---

# U07-L02 — Hardware-in-the-loop and plant emulation

**OpenSTEM Mechanical Engineering · Book 11: Mechatronics Engineering · Unit 7: Integration, Diagnostics and Verification.** Educational draft for university study; no hardware-specific safety certification is implied.

## Learning outcome and engineering question

Explain the physical mechanism behind **hardware-in-the-loop and plant emulation** and identify the quantities that can be measured independently. Starting from a realistic unit model, calculate a nominal prediction, check what happens when the governing assumptions break down and propose a discriminating experiment. This lesson is part of a progressive integrated task: A benchtop automation prototype must withstand startup transients, noisy signals, mechanical alignment and recovery from faults.

**What success looks like.** By the end you should be able to defend the selected equation, label its physical units, derive or justify the result, explain a dominant failure mode, and design an observable test with an explicit acceptance criterion. Use two independent ways of checking a result: dimensional reasoning and either a measurement or a numerical reproduction. The purpose is a model that can be challenged, not an elegant formula without operational meaning.

## Conceptual model

Hardware-in-the-loop connects actual controller hardware to a real-time simulated plant. It enables deliberate fault injection, but emulator latency and idealized sensor models can conceal problems. Map I/O levels and sampling timing accurately. This particular concept belongs to the broader unit theme: A verified subsystem does not imply a verified integrated machine. Make a small system diagram showing where the relevant signal, mechanical load, power or timing variable enters and where its effect is actually observable. The diagram must distinguish the real plant from its estimate or representation.

**Why the distinction matters.** Make each claim falsifiable by a named test and acceptance threshold. For the integrated example, create a traceability table that links each observed failure to a candidate mechanism, controlled change, retest and revised requirement. A plausible result can remain wrong if the coordinate frame, timing origin, sign convention or instrumentation location is inconsistent with the assembled machine.

## Mathematical representation and assumptions

A useful starting relationship is **`phase_lag ≈ omega T_d`**. Read each term aloud with physical dimensions. The expression is a compact model, not a universal constitutive law: its assumptions are the governing physical regime, parameter definition and measurement method described above. State whether the relationship is exact within a defined idealization, an approximation, or an empirical fit.

An equation is only as good as its measurement model. Quantities denoted with a command subscript are not automatically the same as physical values recorded at a sensor. Next, identify at least one quantity in the expression that is independent and one that is dependent. If two independent inputs vary together, a single trial cannot identify their separate effects. List what remains constant in your derivation.

**Boundary check.** Consider reducing the principal input toward zero and increasing it within the permitted physical range. Does the result approach a sensible limit? Note when the formula would produce an unbounded, negative, or otherwise nonphysical output. Even a well-defined mathematical result should be rejected if it implies operation beyond an actuator limit or mechanical stop.

## Worked example with units

At 10 rad/s and 5 ms delay, extra phase lag is approximately 0.05 rad, or 2.86 degrees. Rewrite the given numbers before substitution; explicitly carry their units through the equation. Compare the answer to a rough mental estimate and state a sensible number of significant figures. Do not interpret the displayed precision as measured accuracy. The calculation is synthetic unless independently verified against a particular device.

**Sensitivity experiment.** Repeat the calculation after changing one controlling quantity by +10% while keeping other stated inputs fixed. For a linear relationship, expect a proportional response in the appropriate variable; for a nonlinear one, compute the actual change and compare it with the local slope. Explain whether the chosen perturbation is realistic for the application.

**Dimensional audit.** Convert angles, voltages, forces, lengths and time to an explicitly declared convention before putting them in code. A numerical answer with the wrong units is not a small editorial error: it can change the actual machine motion or power demands by large factors. Record the conversion and the numerical rounding separately.

## Engineering integration and trade-offs

Testing only at nominal operating conditions creates fragile systems. Design margins need confidence intervals, calibration references and explicit handling of failed runs; a dataset without its firmware version and wiring revision is difficult to reproduce. For **hardware-in-the-loop and plant emulation**, choose a realistic engineering constraint: supply capacity, maximum permissible temperature, mechanical clearance, sensor bandwidth, task deadline or acceptable uncertainty. Identify how the model interfaces with the preceding and following functions. For example, a correct sensor estimate may still arrive after the actuator can use it.

**Critical failure mode.** An emulator that updates too slowly can validate the wrong control behavior. Identify which physical measurements could distinguish this failure from an equally plausible alternative. Do not silently compensate for a failed measurement by increasing controller gains. When an estimate is suspect, favor a defined restricted state and transparent diagnostics.

**Design trade study.** Compare a simple implementation with a more instrumented one. The simple version may lower cost and code complexity; the instrumented version may expose hidden failure modes but increases wiring, calibration and software overhead. State the evidence that would justify the additional complexity, not a blanket preference for more sensors.

## Verification and reproducibility

A specific, falsifiable check is: Cross-check emulator response and input/output timing against independent plant measurements. Define the measured output, sensor range, stimulus, trial count, recording rate and acceptance threshold. Include the expected direction of change before collecting data, and record every rejected measurement with an explanation.

**Robustness check.** Predefine the pass/fail criterion and archive unsuccessful traces. Changing the limit after viewing the data removes the meaning of acceptance testing. Repeat under at least two operating conditions and one benign fault. The fault test must not rely on unsafe contact with unguarded moving equipment. If laboratory hardware is unavailable, build a transparent simulation and state that physical validation remains unresolved.

**Suggested notebook entries.** Record the schematic version, parameter values and uncertainties, code or model revision, independent measurement reference, raw-data location, plots, limit-case result and outstanding assumptions. This creates a reproducible chain from requirement to model to observation. A screenshot without settings and raw observations is insufficient evidence.

## Questions and design exercises

1. **Conceptual distinction.** Describe the physical meaning of the central quantities in `phase_lag ≈ omega T_d`. Which are commands, which are direct measurements and which require an estimate? Explain one realistic condition where the relationship should not be trusted.
2. **Quantitative extension.** Reproduce this lesson’s worked calculation from a blank page. Perturb the dominant input by 10% and compute the new prediction with units; estimate the sensitivity ratio and explain whether the effect is linear.
3. **Failure diagnosis.** Suppose a trial contradicts the predicted effect. Design two measurements that could separate the failure described above from a second cause, such as measurement bias, saturation, delay, friction or wiring reversal. Explain why merely repeating the same trial is inconclusive.
4. **Verification design.** Propose a bench or simulation protocol for hardware-in-the-loop and plant emulation: variables held fixed, a sweep range, at least one held-out point, a pass/fail criterion, an independently observed quantity and a defined stop or abort condition. State which conclusions could not be supported by the resulting data.

## Study summary and next connection

A successful treatment of **hardware-in-the-loop and plant emulation** includes the physical mechanism, transparent equation, numerical prediction, dimensional sanity check, uncertainty discussion and a falsifiable test. The next lesson changes part of the system, so retain a stable definition of the measured variable and the underlying coordinate or timing convention.


---

# U07-L03 — Failure modes, effects and fault containment

**OpenSTEM Mechanical Engineering · Book 11: Mechatronics Engineering · Unit 7: Integration, Diagnostics and Verification.** Educational draft for university study; no hardware-specific safety certification is implied.

## Learning outcome and engineering question

Explain the physical mechanism behind **failure modes, effects and fault containment** and identify the quantities that can be measured independently. Starting from a realistic unit model, calculate a nominal prediction, check what happens when the governing assumptions break down and propose a discriminating experiment. This lesson is part of a progressive integrated task: A benchtop automation prototype must withstand startup transients, noisy signals, mechanical alignment and recovery from faults.

**What success looks like.** By the end you should be able to defend the selected equation, label its physical units, derive or justify the result, explain a dominant failure mode, and design an observable test with an explicit acceptance criterion. Begin with a physical free-body, energy-flow or signal-flow representation before introducing a numerical model. The purpose is a model that can be challenged, not an elegant formula without operational meaning.

## Conceptual model

Failure-mode analysis starts from credible component and interface failures. Severity, occurrence and detection ratings are prioritization aids, not proof of safety. Independent fault containment reduces the chance that one defect defeats every protective function. This particular concept belongs to the broader unit theme: A verified subsystem does not imply a verified integrated machine. Make a small system diagram showing where the relevant signal, mechanical load, power or timing variable enters and where its effect is actually observable. The diagram must distinguish the real plant from its estimate or representation.

**Why the distinction matters.** Make each claim falsifiable by a named test and acceptance threshold. For the integrated example, create a traceability table that links each observed failure to a candidate mechanism, controlled change, retest and revised requirement. A plausible result can remain wrong if the coordinate frame, timing origin, sign convention or instrumentation location is inconsistent with the assembled machine.

## Mathematical representation and assumptions

A useful starting relationship is **`risk_priority = S O D`**. Read each term aloud with physical dimensions. The expression is a compact model, not a universal constitutive law: its assumptions are the governing physical regime, parameter definition and measurement method described above. State whether the relationship is exact within a defined idealization, an approximation, or an empirical fit.

Model coefficients and initial conditions need uncertainty bounds. The sensitivity of a result to these inputs matters as much as its nominal numerical value. Next, identify at least one quantity in the expression that is independent and one that is dependent. If two independent inputs vary together, a single trial cannot identify their separate effects. List what remains constant in your derivation.

**Boundary check.** Consider reducing the principal input toward zero and increasing it within the permitted physical range. Does the result approach a sensible limit? Note when the formula would produce an unbounded, negative, or otherwise nonphysical output. Even a well-defined mathematical result should be rejected if it implies operation beyond an actuator limit or mechanical stop.

## Worked example with units

Illustrative ratings S=8, O=3 and D=4 multiply to 96; this is only an internal screening index. Rewrite the given numbers before substitution; explicitly carry their units through the equation. Compare the answer to a rough mental estimate and state a sensible number of significant figures. Do not interpret the displayed precision as measured accuracy. The calculation is synthetic unless independently verified against a particular device.

**Sensitivity experiment.** Repeat the calculation after changing one controlling quantity by +10% while keeping other stated inputs fixed. For a linear relationship, expect a proportional response in the appropriate variable; for a nonlinear one, compute the actual change and compare it with the local slope. Explain whether the chosen perturbation is realistic for the application.

**Dimensional audit.** Convert angles, voltages, forces, lengths and time to an explicitly declared convention before putting them in code. A numerical answer with the wrong units is not a small editorial error: it can change the actual machine motion or power demands by large factors. Record the conversion and the numerical rounding separately.

## Engineering integration and trade-offs

Testing only at nominal operating conditions creates fragile systems. Design margins need confidence intervals, calibration references and explicit handling of failed runs; a dataset without its firmware version and wiring revision is difficult to reproduce. For **failure modes, effects and fault containment**, choose a realistic engineering constraint: supply capacity, maximum permissible temperature, mechanical clearance, sensor bandwidth, task deadline or acceptable uncertainty. Identify how the model interfaces with the preceding and following functions. For example, a correct sensor estimate may still arrive after the actuator can use it.

**Critical failure mode.** A low subjective risk score cannot justify ignoring an inherently severe hazard. Identify which physical measurements could distinguish this failure from an equally plausible alternative. Do not silently compensate for a failed measurement by increasing controller gains. When an estimate is suspect, favor a defined restricted state and transparent diagnostics.

**Design trade study.** Compare a simple implementation with a more instrumented one. The simple version may lower cost and code complexity; the instrumented version may expose hidden failure modes but increases wiring, calibration and software overhead. State the evidence that would justify the additional complexity, not a blanket preference for more sensors.

## Verification and reproducibility

A specific, falsifiable check is: Inject sensor disconnection, stuck outputs, supply brownout and watchdog faults while verifying defined safe states. Define the measured output, sensor range, stimulus, trial count, recording rate and acceptance threshold. Include the expected direction of change before collecting data, and record every rejected measurement with an explanation.

**Robustness check.** Test shutdown and restart explicitly. Recovering to a safe known state is part of functionality, not an optional maintenance feature. Repeat under at least two operating conditions and one benign fault. The fault test must not rely on unsafe contact with unguarded moving equipment. If laboratory hardware is unavailable, build a transparent simulation and state that physical validation remains unresolved.

**Suggested notebook entries.** Record the schematic version, parameter values and uncertainties, code or model revision, independent measurement reference, raw-data location, plots, limit-case result and outstanding assumptions. This creates a reproducible chain from requirement to model to observation. A screenshot without settings and raw observations is insufficient evidence.

## Questions and design exercises

1. **Conceptual distinction.** Describe the physical meaning of the central quantities in `risk_priority = S O D`. Which are commands, which are direct measurements and which require an estimate? Explain one realistic condition where the relationship should not be trusted.
2. **Quantitative extension.** Reproduce this lesson’s worked calculation from a blank page. Perturb the dominant input by 10% and compute the new prediction with units; estimate the sensitivity ratio and explain whether the effect is linear.
3. **Failure diagnosis.** Suppose a trial contradicts the predicted effect. Design two measurements that could separate the failure described above from a second cause, such as measurement bias, saturation, delay, friction or wiring reversal. Explain why merely repeating the same trial is inconclusive.
4. **Verification design.** Propose a bench or simulation protocol for failure modes, effects and fault containment: variables held fixed, a sweep range, at least one held-out point, a pass/fail criterion, an independently observed quantity and a defined stop or abort condition. State which conclusions could not be supported by the resulting data.

## Study summary and next connection

A successful treatment of **failure modes, effects and fault containment** includes the physical mechanism, transparent equation, numerical prediction, dimensional sanity check, uncertainty discussion and a falsifiable test. The next lesson changes part of the system, so retain a stable definition of the measured variable and the underlying coordinate or timing convention.


---

# U07-L04 — Integration troubleshooting with evidence

**OpenSTEM Mechanical Engineering · Book 11: Mechatronics Engineering · Unit 7: Integration, Diagnostics and Verification.** Educational draft for university study; no hardware-specific safety certification is implied.

## Learning outcome and engineering question

Explain the physical mechanism behind **integration troubleshooting with evidence** and identify the quantities that can be measured independently. Starting from a realistic unit model, calculate a nominal prediction, check what happens when the governing assumptions break down and propose a discriminating experiment. This lesson is part of a progressive integrated task: A benchtop automation prototype must withstand startup transients, noisy signals, mechanical alignment and recovery from faults.

**What success looks like.** By the end you should be able to defend the selected equation, label its physical units, derive or justify the result, explain a dominant failure mode, and design an observable test with an explicit acceptance criterion. Convert the verbal specification into variables with declared units, coordinate directions and an operating envelope. The purpose is a model that can be challenged, not an elegant formula without operational meaning.

## Conceptual model

Debugging proceeds by hypothesis, measurement and isolation. Distinguish incorrect software units, timing, power sag, grounding interference, backlash and mechanical misalignment. Preserve failing traces instead of repeatedly modifying software without a baseline. This particular concept belongs to the broader unit theme: A verified subsystem does not imply a verified integrated machine. Make a small system diagram showing where the relevant signal, mechanical load, power or timing variable enters and where its effect is actually observable. The diagram must distinguish the real plant from its estimate or representation.

**Why the distinction matters.** Make each claim falsifiable by a named test and acceptance threshold. For the integrated example, create a traceability table that links each observed failure to a candidate mechanism, controlled change, retest and revised requirement. A plausible result can remain wrong if the coordinate frame, timing origin, sign convention or instrumentation location is inconsistent with the assembled machine.

## Mathematical representation and assumptions

A useful starting relationship is **`residual = measured - predicted`**. Read each term aloud with physical dimensions. The expression is a compact model, not a universal constitutive law: its assumptions are the governing physical regime, parameter definition and measurement method described above. State whether the relationship is exact within a defined idealization, an approximation, or an empirical fit.

For sampled systems, timestamp the input and output to distinguish propagation delay from genuine plant dynamics. An unmeasured delay can invalidate an otherwise sound formula. Next, identify at least one quantity in the expression that is independent and one that is dependent. If two independent inputs vary together, a single trial cannot identify their separate effects. List what remains constant in your derivation.

**Boundary check.** Consider reducing the principal input toward zero and increasing it within the permitted physical range. Does the result approach a sensible limit? Note when the formula would produce an unbounded, negative, or otherwise nonphysical output. Even a well-defined mathematical result should be rejected if it implies operation beyond an actuator limit or mechanical stop.

## Worked example with units

If expected displacement is 4.0 mm and measured is 3.4 mm, residual is -0.6 mm; both sensor bias and mechanical slip remain candidates. Rewrite the given numbers before substitution; explicitly carry their units through the equation. Compare the answer to a rough mental estimate and state a sensible number of significant figures. Do not interpret the displayed precision as measured accuracy. The calculation is synthetic unless independently verified against a particular device.

**Sensitivity experiment.** Repeat the calculation after changing one controlling quantity by +10% while keeping other stated inputs fixed. For a linear relationship, expect a proportional response in the appropriate variable; for a nonlinear one, compute the actual change and compare it with the local slope. Explain whether the chosen perturbation is realistic for the application.

**Dimensional audit.** Convert angles, voltages, forces, lengths and time to an explicitly declared convention before putting them in code. A numerical answer with the wrong units is not a small editorial error: it can change the actual machine motion or power demands by large factors. Record the conversion and the numerical rounding separately.

## Engineering integration and trade-offs

Testing only at nominal operating conditions creates fragile systems. Design margins need confidence intervals, calibration references and explicit handling of failed runs; a dataset without its firmware version and wiring revision is difficult to reproduce. For **integration troubleshooting with evidence**, choose a realistic engineering constraint: supply capacity, maximum permissible temperature, mechanical clearance, sensor bandwidth, task deadline or acceptable uncertainty. Identify how the model interfaces with the preceding and following functions. For example, a correct sensor estimate may still arrive after the actuator can use it.

**Critical failure mode.** Changing several gains and filter settings simultaneously destroys causal attribution. Identify which physical measurements could distinguish this failure from an equally plausible alternative. Do not silently compensate for a failed measurement by increasing controller gains. When an estimate is suspect, favor a defined restricted state and transparent diagnostics.

**Design trade study.** Compare a simple implementation with a more instrumented one. The simple version may lower cost and code complexity; the instrumented version may expose hidden failure modes but increases wiring, calibration and software overhead. State the evidence that would justify the additional complexity, not a blanket preference for more sensors.

## Verification and reproducibility

A specific, falsifiable check is: Use single-variable controlled tests and a saved, reproducible fault log. Define the measured output, sensor range, stimulus, trial count, recording rate and acceptance threshold. Include the expected direction of change before collecting data, and record every rejected measurement with an explanation.

**Robustness check.** Record the maximum as well as the average. A machine that misses one deadline in a hundred may be unusable when every item must be sorted. Repeat under at least two operating conditions and one benign fault. The fault test must not rely on unsafe contact with unguarded moving equipment. If laboratory hardware is unavailable, build a transparent simulation and state that physical validation remains unresolved.

**Suggested notebook entries.** Record the schematic version, parameter values and uncertainties, code or model revision, independent measurement reference, raw-data location, plots, limit-case result and outstanding assumptions. This creates a reproducible chain from requirement to model to observation. A screenshot without settings and raw observations is insufficient evidence.

## Questions and design exercises

1. **Conceptual distinction.** Describe the physical meaning of the central quantities in `residual = measured - predicted`. Which are commands, which are direct measurements and which require an estimate? Explain one realistic condition where the relationship should not be trusted.
2. **Quantitative extension.** Reproduce this lesson’s worked calculation from a blank page. Perturb the dominant input by 10% and compute the new prediction with units; estimate the sensitivity ratio and explain whether the effect is linear.
3. **Failure diagnosis.** Suppose a trial contradicts the predicted effect. Design two measurements that could separate the failure described above from a second cause, such as measurement bias, saturation, delay, friction or wiring reversal. Explain why merely repeating the same trial is inconclusive.
4. **Verification design.** Propose a bench or simulation protocol for integration troubleshooting with evidence: variables held fixed, a sweep range, at least one held-out point, a pass/fail criterion, an independently observed quantity and a defined stop or abort condition. State which conclusions could not be supported by the resulting data.

## Study summary and next connection

A successful treatment of **integration troubleshooting with evidence** includes the physical mechanism, transparent equation, numerical prediction, dimensional sanity check, uncertainty discussion and a falsifiable test. The next lesson changes part of the system, so retain a stable definition of the measured variable and the underlying coordinate or timing convention.


---

# U07-L05 — Reliability growth and maintenance planning

**OpenSTEM Mechanical Engineering · Book 11: Mechatronics Engineering · Unit 7: Integration, Diagnostics and Verification.** Educational draft for university study; no hardware-specific safety certification is implied.

## Learning outcome and engineering question

Explain the physical mechanism behind **reliability growth and maintenance planning** and identify the quantities that can be measured independently. Starting from a realistic unit model, calculate a nominal prediction, check what happens when the governing assumptions break down and propose a discriminating experiment. This lesson is part of a progressive integrated task: A benchtop automation prototype must withstand startup transients, noisy signals, mechanical alignment and recovery from faults.

**What success looks like.** By the end you should be able to defend the selected equation, label its physical units, derive or justify the result, explain a dominant failure mode, and design an observable test with an explicit acceptance criterion. Separate ideal mathematical behavior from calibration error, deadband, quantization and machine-level uncertainty. The purpose is a model that can be challenged, not an elegant formula without operational meaning.

## Conceptual model

Repeated cycles, temperature shifts and connectors can degrade performance after initial acceptance. Weibull or exponential lifetime models require appropriate evidence; short demonstrations cannot establish long lifetime. Define serviceable parts and observable degradation indicators. This particular concept belongs to the broader unit theme: A verified subsystem does not imply a verified integrated machine. Make a small system diagram showing where the relevant signal, mechanical load, power or timing variable enters and where its effect is actually observable. The diagram must distinguish the real plant from its estimate or representation.

**Why the distinction matters.** Make each claim falsifiable by a named test and acceptance threshold. For the integrated example, create a traceability table that links each observed failure to a candidate mechanism, controlled change, retest and revised requirement. A plausible result can remain wrong if the coordinate frame, timing origin, sign convention or instrumentation location is inconsistent with the assembled machine.

## Mathematical representation and assumptions

A useful starting relationship is **`R(t)=exp(-lambda t)`**. Read each term aloud with physical dimensions. The expression is a compact model, not a universal constitutive law: its assumptions are the governing physical regime, parameter definition and measurement method described above. State whether the relationship is exact within a defined idealization, an approximation, or an empirical fit.

In a design calculation, rounding should occur at reporting time. Retain guard digits during intermediate steps so that resolution errors are not mistaken for physical discrepancies. Next, identify at least one quantity in the expression that is independent and one that is dependent. If two independent inputs vary together, a single trial cannot identify their separate effects. List what remains constant in your derivation.

**Boundary check.** Consider reducing the principal input toward zero and increasing it within the permitted physical range. Does the result approach a sensible limit? Note when the formula would produce an unbounded, negative, or otherwise nonphysical output. Even a well-defined mathematical result should be rejected if it implies operation beyond an actuator limit or mechanical stop.

## Worked example with units

At an assumed constant hazard rate 0.0001 per hour, idealized reliability over 100 hours is about 0.99005. Rewrite the given numbers before substitution; explicitly carry their units through the equation. Compare the answer to a rough mental estimate and state a sensible number of significant figures. Do not interpret the displayed precision as measured accuracy. The calculation is synthetic unless independently verified against a particular device.

**Sensitivity experiment.** Repeat the calculation after changing one controlling quantity by +10% while keeping other stated inputs fixed. For a linear relationship, expect a proportional response in the appropriate variable; for a nonlinear one, compute the actual change and compare it with the local slope. Explain whether the chosen perturbation is realistic for the application.

**Dimensional audit.** Convert angles, voltages, forces, lengths and time to an explicitly declared convention before putting them in code. A numerical answer with the wrong units is not a small editorial error: it can change the actual machine motion or power demands by large factors. Record the conversion and the numerical rounding separately.

## Engineering integration and trade-offs

Testing only at nominal operating conditions creates fragile systems. Design margins need confidence intervals, calibration references and explicit handling of failed runs; a dataset without its firmware version and wiring revision is difficult to reproduce. For **reliability growth and maintenance planning**, choose a realistic engineering constraint: supply capacity, maximum permissible temperature, mechanical clearance, sensor bandwidth, task deadline or acceptable uncertainty. Identify how the model interfaces with the preceding and following functions. For example, a correct sensor estimate may still arrive after the actuator can use it.

**Critical failure mode.** Using a constant failure rate for wear-out mechanisms misrepresents aging. Identify which physical measurements could distinguish this failure from an equally plausible alternative. Do not silently compensate for a failed measurement by increasing controller gains. When an estimate is suspect, favor a defined restricted state and transparent diagnostics.

**Design trade study.** Compare a simple implementation with a more instrumented one. The simple version may lower cost and code complexity; the instrumented version may expose hidden failure modes but increases wiring, calibration and software overhead. State the evidence that would justify the additional complexity, not a blanket preference for more sensors.

## Verification and reproducibility

A specific, falsifiable check is: Track duty cycles, fault counts, thermal events, calibration drift and replacements during endurance testing. Define the measured output, sensor range, stimulus, trial count, recording rate and acceptance threshold. Include the expected direction of change before collecting data, and record every rejected measurement with an explanation.

**Robustness check.** Use an independently calibrated reference if possible. Comparing two software values derived from one biased sensor does not validate the measurement. Repeat under at least two operating conditions and one benign fault. The fault test must not rely on unsafe contact with unguarded moving equipment. If laboratory hardware is unavailable, build a transparent simulation and state that physical validation remains unresolved.

**Suggested notebook entries.** Record the schematic version, parameter values and uncertainties, code or model revision, independent measurement reference, raw-data location, plots, limit-case result and outstanding assumptions. This creates a reproducible chain from requirement to model to observation. A screenshot without settings and raw observations is insufficient evidence.

## Questions and design exercises

1. **Conceptual distinction.** Describe the physical meaning of the central quantities in `R(t)=exp(-lambda t)`. Which are commands, which are direct measurements and which require an estimate? Explain one realistic condition where the relationship should not be trusted.
2. **Quantitative extension.** Reproduce this lesson’s worked calculation from a blank page. Perturb the dominant input by 10% and compute the new prediction with units; estimate the sensitivity ratio and explain whether the effect is linear.
3. **Failure diagnosis.** Suppose a trial contradicts the predicted effect. Design two measurements that could separate the failure described above from a second cause, such as measurement bias, saturation, delay, friction or wiring reversal. Explain why merely repeating the same trial is inconclusive.
4. **Verification design.** Propose a bench or simulation protocol for reliability growth and maintenance planning: variables held fixed, a sweep range, at least one held-out point, a pass/fail criterion, an independently observed quantity and a defined stop or abort condition. State which conclusions could not be supported by the resulting data.

## Study summary and next connection

A successful treatment of **reliability growth and maintenance planning** includes the physical mechanism, transparent equation, numerical prediction, dimensional sanity check, uncertainty discussion and a falsifiable test. The next lesson changes part of the system, so retain a stable definition of the measured variable and the underlying coordinate or timing convention.


---

