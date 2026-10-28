# Unit 08: Integrated Mechatronic Applications

**Course Code**: MCT 408 · **Level**: Advanced Undergraduate Engineering

## Unit Overview & Physical Foundations

This comprehensive university textbook unit covers the theoretical framework, physical modeling, mathematical governing equations, and engineering applications of **Integrated Mechatronic Applications**.

# U08-L01 — Photoelectric sorting conveyor

**OpenSTEM Mechanical Engineering · Book 11: Mechatronics Engineering · Unit 8: Integrated Mechatronic Applications.** Educational draft for university study; no hardware-specific safety certification is implied.

## Learning outcome and engineering question

Explain the physical mechanism behind **photoelectric sorting conveyor** and identify the quantities that can be measured independently. Starting from a realistic unit model, calculate a nominal prediction, check what happens when the governing assumptions break down and propose a discriminating experiment. This lesson is part of a progressive integrated task: Complete design studies with verifiable calculations, data logs and independent safety controls.

**What success looks like.** By the end you should be able to defend the selected equation, label its physical units, derive or justify the result, explain a dominant failure mode, and design an observable test with an explicit acceptance criterion. Use two independent ways of checking a result: dimensional reasoning and either a measurement or a numerical reproduction. The purpose is a model that can be challenged, not an elegant formula without operational meaning.

## Conceptual model

Sorting depends on object arrival, camera or sensor delay, classification and gate dynamics. Combine transport speed, sensor placement, actuator travel and uncertainty into one timing diagram. Background light and overlapping objects require detection and reject-state policies. This particular concept belongs to the broader unit theme: Integrate mechanics, electronics and software under stated evidence limits. Make a small system diagram showing where the relevant signal, mechanical load, power or timing variable enters and where its effect is actually observable. The diagram must distinguish the real plant from its estimate or representation.

**Why the distinction matters.** Demonstrate complete operating cycles including exceptional states. For the integrated example, treat the application as an engineering case study. complete timing diagrams, unit tables, controlled simulations, fault injection and deployment limitations. A plausible result can remain wrong if the coordinate frame, timing origin, sign convention or instrumentation location is inconsistent with the assembled machine.

## Mathematical representation and assumptions

A useful starting relationship is **`t_lead = distance / belt_speed`**. Read each term aloud with physical dimensions. The expression is a compact model, not a universal constitutive law: its assumptions are the governing physical regime, parameter definition and measurement method described above. State whether the relationship is exact within a defined idealization, an approximation, or an empirical fit.

A derived relationship should be dimensionally homogeneous. If an angular quantity is used, declare whether trigonometric routines take radians. Distinguish electrical input power from useful output power. Next, identify at least one quantity in the expression that is independent and one that is dependent. If two independent inputs vary together, a single trial cannot identify their separate effects. List what remains constant in your derivation.

**Boundary check.** Consider reducing the principal input toward zero and increasing it within the permitted physical range. Does the result approach a sensible limit? Note when the formula would produce an unbounded, negative, or otherwise nonphysical output. Even a well-defined mathematical result should be rejected if it implies operation beyond an actuator limit or mechanical stop.

## Worked example with units

A diverter 0.60 m downstream of detection at 0.75 m/s has a nominal 0.80 s travel interval. Rewrite the given numbers before substitution; explicitly carry their units through the equation. Compare the answer to a rough mental estimate and state a sensible number of significant figures. Do not interpret the displayed precision as measured accuracy. The calculation is synthetic unless independently verified against a particular device.

**Sensitivity experiment.** Repeat the calculation after changing one controlling quantity by +10% while keeping other stated inputs fixed. For a linear relationship, expect a proportional response in the appropriate variable; for a nonlinear one, compute the actual change and compare it with the local slope. Explain whether the chosen perturbation is realistic for the application.

**Dimensional audit.** Convert angles, voltages, forces, lengths and time to an explicitly declared convention before putting them in code. A numerical answer with the wrong units is not a small editorial error: it can change the actual machine motion or power demands by large factors. Record the conversion and the numerical rounding separately.

## Engineering integration and trade-offs

Systems thinking requires connecting sensing errors, motion latency, material variability, operator access and maintenance. Performance metrics must include rejected parts, interrupted operation and recovery time; successful output alone is an incomplete measure. For **photoelectric sorting conveyor**, choose a realistic engineering constraint: supply capacity, maximum permissible temperature, mechanical clearance, sensor bandwidth, task deadline or acceptable uncertainty. Identify how the model interfaces with the preceding and following functions. For example, a correct sensor estimate may still arrive after the actuator can use it.

**Critical failure mode.** A late gate that still appears to move correctly during slow demonstrations can cause collisions at production speed. Identify which physical measurements could distinguish this failure from an equally plausible alternative. Do not silently compensate for a failed measurement by increasing controller gains. When an estimate is suspect, favor a defined restricted state and transparent diagnostics.

**Design trade study.** Compare a simple implementation with a more instrumented one. The simple version may lower cost and code complexity; the instrumented version may expose hidden failure modes but increases wiring, calibration and software overhead. State the evidence that would justify the additional complexity, not a blanket preference for more sensors.

## Verification and reproducibility

A specific, falsifiable check is: Test maximum item density, missing detections, gate jams and safe rejects with protective containment. Define the measured output, sensor range, stimulus, trial count, recording rate and acceptance threshold. Include the expected direction of change before collecting data, and record every rejected measurement with an explanation.

**Robustness check.** Vary one parameter at a time during fault isolation; note that real production environments may combine several disturbances. Repeat under at least two operating conditions and one benign fault. The fault test must not rely on unsafe contact with unguarded moving equipment. If laboratory hardware is unavailable, build a transparent simulation and state that physical validation remains unresolved.

**Suggested notebook entries.** Record the schematic version, parameter values and uncertainties, code or model revision, independent measurement reference, raw-data location, plots, limit-case result and outstanding assumptions. This creates a reproducible chain from requirement to model to observation. A screenshot without settings and raw observations is insufficient evidence.

## Questions and design exercises

1. **Conceptual distinction.** Describe the physical meaning of the central quantities in `t_lead = distance / belt_speed`. Which are commands, which are direct measurements and which require an estimate? Explain one realistic condition where the relationship should not be trusted.
2. **Quantitative extension.** Reproduce this lesson’s worked calculation from a blank page. Perturb the dominant input by 10% and compute the new prediction with units; estimate the sensitivity ratio and explain whether the effect is linear.
3. **Failure diagnosis.** Suppose a trial contradicts the predicted effect. Design two measurements that could separate the failure described above from a second cause, such as measurement bias, saturation, delay, friction or wiring reversal. Explain why merely repeating the same trial is inconclusive.
4. **Verification design.** Propose a bench or simulation protocol for photoelectric sorting conveyor: variables held fixed, a sweep range, at least one held-out point, a pass/fail criterion, an independently observed quantity and a defined stop or abort condition. State which conclusions could not be supported by the resulting data.

## Study summary and next connection

A successful treatment of **photoelectric sorting conveyor** includes the physical mechanism, transparent equation, numerical prediction, dimensional sanity check, uncertainty discussion and a falsifiable test. The next lesson changes part of the system, so retain a stable definition of the measured variable and the underlying coordinate or timing convention.


---

# U08-L02 — Precision linear positioning stage

**OpenSTEM Mechanical Engineering · Book 11: Mechatronics Engineering · Unit 8: Integrated Mechatronic Applications.** Educational draft for university study; no hardware-specific safety certification is implied.

## Learning outcome and engineering question

Explain the physical mechanism behind **precision linear positioning stage** and identify the quantities that can be measured independently. Starting from a realistic unit model, calculate a nominal prediction, check what happens when the governing assumptions break down and propose a discriminating experiment. This lesson is part of a progressive integrated task: Complete design studies with verifiable calculations, data logs and independent safety controls.

**What success looks like.** By the end you should be able to defend the selected equation, label its physical units, derive or justify the result, explain a dominant failure mode, and design an observable test with an explicit acceptance criterion. Begin with a physical free-body, energy-flow or signal-flow representation before introducing a numerical model. The purpose is a model that can be challenged, not an elegant formula without operational meaning.

## Conceptual model

A screw-driven stage links motor angle to carriage travel through lead and mechanical efficiency. Backlash, compliance and thermal growth limit final accuracy. Specify repeatability separately from absolute accuracy and choose measurement points near the payload. This particular concept belongs to the broader unit theme: Integrate mechanics, electronics and software under stated evidence limits. Make a small system diagram showing where the relevant signal, mechanical load, power or timing variable enters and where its effect is actually observable. The diagram must distinguish the real plant from its estimate or representation.

**Why the distinction matters.** Demonstrate complete operating cycles including exceptional states. For the integrated example, treat the application as an engineering case study. complete timing diagrams, unit tables, controlled simulations, fault injection and deployment limitations. A plausible result can remain wrong if the coordinate frame, timing origin, sign convention or instrumentation location is inconsistent with the assembled machine.

## Mathematical representation and assumptions

A useful starting relationship is **`x = lead theta/(2*pi)`**. Read each term aloud with physical dimensions. The expression is a compact model, not a universal constitutive law: its assumptions are the governing physical regime, parameter definition and measurement method described above. State whether the relationship is exact within a defined idealization, an approximation, or an empirical fit.

An equation is only as good as its measurement model. Quantities denoted with a command subscript are not automatically the same as physical values recorded at a sensor. Next, identify at least one quantity in the expression that is independent and one that is dependent. If two independent inputs vary together, a single trial cannot identify their separate effects. List what remains constant in your derivation.

**Boundary check.** Consider reducing the principal input toward zero and increasing it within the permitted physical range. Does the result approach a sensible limit? Note when the formula would produce an unbounded, negative, or otherwise nonphysical output. Even a well-defined mathematical result should be rejected if it implies operation beyond an actuator limit or mechanical stop.

## Worked example with units

A 5 mm/revolution screw rotating through 3 full turns advances ideally 15 mm. Rewrite the given numbers before substitution; explicitly carry their units through the equation. Compare the answer to a rough mental estimate and state a sensible number of significant figures. Do not interpret the displayed precision as measured accuracy. The calculation is synthetic unless independently verified against a particular device.

**Sensitivity experiment.** Repeat the calculation after changing one controlling quantity by +10% while keeping other stated inputs fixed. For a linear relationship, expect a proportional response in the appropriate variable; for a nonlinear one, compute the actual change and compare it with the local slope. Explain whether the chosen perturbation is realistic for the application.

**Dimensional audit.** Convert angles, voltages, forces, lengths and time to an explicitly declared convention before putting them in code. A numerical answer with the wrong units is not a small editorial error: it can change the actual machine motion or power demands by large factors. Record the conversion and the numerical rounding separately.

## Engineering integration and trade-offs

Systems thinking requires connecting sensing errors, motion latency, material variability, operator access and maintenance. Performance metrics must include rejected parts, interrupted operation and recovery time; successful output alone is an incomplete measure. For **precision linear positioning stage**, choose a realistic engineering constraint: supply capacity, maximum permissible temperature, mechanical clearance, sensor bandwidth, task deadline or acceptable uncertainty. Identify how the model interfaces with the preceding and following functions. For example, a correct sensor estimate may still arrive after the actuator can use it.

**Critical failure mode.** Motor-shaft position may appear perfect while the carriage is displaced by load-dependent elastic deformation. Identify which physical measurements could distinguish this failure from an equally plausible alternative. Do not silently compensate for a failed measurement by increasing controller gains. When an estimate is suspect, favor a defined restricted state and transparent diagnostics.

**Design trade study.** Compare a simple implementation with a more instrumented one. The simple version may lower cost and code complexity; the instrumented version may expose hidden failure modes but increases wiring, calibration and software overhead. State the evidence that would justify the additional complexity, not a blanket preference for more sensors.

## Verification and reproducibility

A specific, falsifiable check is: Measure commanded versus external carriage displacement for forward and reverse approaches. Define the measured output, sensor range, stimulus, trial count, recording rate and acceptance threshold. Include the expected direction of change before collecting data, and record every rejected measurement with an explanation.

**Robustness check.** Predefine the pass/fail criterion and archive unsuccessful traces. Changing the limit after viewing the data removes the meaning of acceptance testing. Repeat under at least two operating conditions and one benign fault. The fault test must not rely on unsafe contact with unguarded moving equipment. If laboratory hardware is unavailable, build a transparent simulation and state that physical validation remains unresolved.

**Suggested notebook entries.** Record the schematic version, parameter values and uncertainties, code or model revision, independent measurement reference, raw-data location, plots, limit-case result and outstanding assumptions. This creates a reproducible chain from requirement to model to observation. A screenshot without settings and raw observations is insufficient evidence.

## Questions and design exercises

1. **Conceptual distinction.** Describe the physical meaning of the central quantities in `x = lead theta/(2*pi)`. Which are commands, which are direct measurements and which require an estimate? Explain one realistic condition where the relationship should not be trusted.
2. **Quantitative extension.** Reproduce this lesson’s worked calculation from a blank page. Perturb the dominant input by 10% and compute the new prediction with units; estimate the sensitivity ratio and explain whether the effect is linear.
3. **Failure diagnosis.** Suppose a trial contradicts the predicted effect. Design two measurements that could separate the failure described above from a second cause, such as measurement bias, saturation, delay, friction or wiring reversal. Explain why merely repeating the same trial is inconclusive.
4. **Verification design.** Propose a bench or simulation protocol for precision linear positioning stage: variables held fixed, a sweep range, at least one held-out point, a pass/fail criterion, an independently observed quantity and a defined stop or abort condition. State which conclusions could not be supported by the resulting data.

## Study summary and next connection

A successful treatment of **precision linear positioning stage** includes the physical mechanism, transparent equation, numerical prediction, dimensional sanity check, uncertainty discussion and a falsifiable test. The next lesson changes part of the system, so retain a stable definition of the measured variable and the underlying coordinate or timing convention.


---

# U08-L03 — Balancing robot simulation and stability

**OpenSTEM Mechanical Engineering · Book 11: Mechatronics Engineering · Unit 8: Integrated Mechatronic Applications.** Educational draft for university study; no hardware-specific safety certification is implied.

## Learning outcome and engineering question

Explain the physical mechanism behind **balancing robot simulation and stability** and identify the quantities that can be measured independently. Starting from a realistic unit model, calculate a nominal prediction, check what happens when the governing assumptions break down and propose a discriminating experiment. This lesson is part of a progressive integrated task: Complete design studies with verifiable calculations, data logs and independent safety controls.

**What success looks like.** By the end you should be able to defend the selected equation, label its physical units, derive or justify the result, explain a dominant failure mode, and design an observable test with an explicit acceptance criterion. Convert the verbal specification into variables with declared units, coordinate directions and an operating envelope. The purpose is a model that can be challenged, not an elegant formula without operational meaning.

## Conceptual model

An inverted-pendulum robot is unstable near upright equilibrium and couples pitch to wheel torque. Linearized simulation is useful for controller understanding, but it does not make an unguarded physical build safe. Sensor delay, wheel slip and saturation change behavior. This particular concept belongs to the broader unit theme: Integrate mechanics, electronics and software under stated evidence limits. Make a small system diagram showing where the relevant signal, mechanical load, power or timing variable enters and where its effect is actually observable. The diagram must distinguish the real plant from its estimate or representation.

**Why the distinction matters.** Demonstrate complete operating cycles including exceptional states. For the integrated example, treat the application as an engineering case study. complete timing diagrams, unit tables, controlled simulations, fault injection and deployment limitations. A plausible result can remain wrong if the coordinate frame, timing origin, sign convention or instrumentation location is inconsistent with the assembled machine.

## Mathematical representation and assumptions

A useful starting relationship is **`tau_g ≈ m g l theta`**. Read each term aloud with physical dimensions. The expression is a compact model, not a universal constitutive law: its assumptions are the governing physical regime, parameter definition and measurement method described above. State whether the relationship is exact within a defined idealization, an approximation, or an empirical fit.

Model coefficients and initial conditions need uncertainty bounds. The sensitivity of a result to these inputs matters as much as its nominal numerical value. Next, identify at least one quantity in the expression that is independent and one that is dependent. If two independent inputs vary together, a single trial cannot identify their separate effects. List what remains constant in your derivation.

**Boundary check.** Consider reducing the principal input toward zero and increasing it within the permitted physical range. Does the result approach a sensible limit? Note when the formula would produce an unbounded, negative, or otherwise nonphysical output. Even a well-defined mathematical result should be rejected if it implies operation beyond an actuator limit or mechanical stop.

## Worked example with units

For m=1.5 kg, l=0.12 m and small pitch 0.10 rad, gravity moment is approximately 0.177 N m. Rewrite the given numbers before substitution; explicitly carry their units through the equation. Compare the answer to a rough mental estimate and state a sensible number of significant figures. Do not interpret the displayed precision as measured accuracy. The calculation is synthetic unless independently verified against a particular device.

**Sensitivity experiment.** Repeat the calculation after changing one controlling quantity by +10% while keeping other stated inputs fixed. For a linear relationship, expect a proportional response in the appropriate variable; for a nonlinear one, compute the actual change and compare it with the local slope. Explain whether the chosen perturbation is realistic for the application.

**Dimensional audit.** Convert angles, voltages, forces, lengths and time to an explicitly declared convention before putting them in code. A numerical answer with the wrong units is not a small editorial error: it can change the actual machine motion or power demands by large factors. Record the conversion and the numerical rounding separately.

## Engineering integration and trade-offs

Systems thinking requires connecting sensing errors, motion latency, material variability, operator access and maintenance. Performance metrics must include rejected parts, interrupted operation and recovery time; successful output alone is an incomplete measure. For **balancing robot simulation and stability**, choose a realistic engineering constraint: supply capacity, maximum permissible temperature, mechanical clearance, sensor bandwidth, task deadline or acceptable uncertainty. Identify how the model interfaces with the preceding and following functions. For example, a correct sensor estimate may still arrive after the actuator can use it.

**Critical failure mode.** The small-angle approximation fails for large tilts, especially while recovering from a fall. Identify which physical measurements could distinguish this failure from an equally plausible alternative. Do not silently compensate for a failed measurement by increasing controller gains. When an estimate is suspect, favor a defined restricted state and transparent diagnostics.

**Design trade study.** Compare a simple implementation with a more instrumented one. The simple version may lower cost and code complexity; the instrumented version may expose hidden failure modes but increases wiring, calibration and software overhead. State the evidence that would justify the additional complexity, not a blanket preference for more sensors.

## Verification and reproducibility

A specific, falsifiable check is: Use a simulated robot and a secured test fixture; log pitch, current and protective-stop responses. Define the measured output, sensor range, stimulus, trial count, recording rate and acceptance threshold. Include the expected direction of change before collecting data, and record every rejected measurement with an explanation.

**Robustness check.** Test shutdown and restart explicitly. Recovering to a safe known state is part of functionality, not an optional maintenance feature. Repeat under at least two operating conditions and one benign fault. The fault test must not rely on unsafe contact with unguarded moving equipment. If laboratory hardware is unavailable, build a transparent simulation and state that physical validation remains unresolved.

**Suggested notebook entries.** Record the schematic version, parameter values and uncertainties, code or model revision, independent measurement reference, raw-data location, plots, limit-case result and outstanding assumptions. This creates a reproducible chain from requirement to model to observation. A screenshot without settings and raw observations is insufficient evidence.

## Questions and design exercises

1. **Conceptual distinction.** Describe the physical meaning of the central quantities in `tau_g ≈ m g l theta`. Which are commands, which are direct measurements and which require an estimate? Explain one realistic condition where the relationship should not be trusted.
2. **Quantitative extension.** Reproduce this lesson’s worked calculation from a blank page. Perturb the dominant input by 10% and compute the new prediction with units; estimate the sensitivity ratio and explain whether the effect is linear.
3. **Failure diagnosis.** Suppose a trial contradicts the predicted effect. Design two measurements that could separate the failure described above from a second cause, such as measurement bias, saturation, delay, friction or wiring reversal. Explain why merely repeating the same trial is inconclusive.
4. **Verification design.** Propose a bench or simulation protocol for balancing robot simulation and stability: variables held fixed, a sweep range, at least one held-out point, a pass/fail criterion, an independently observed quantity and a defined stop or abort condition. State which conclusions could not be supported by the resulting data.

## Study summary and next connection

A successful treatment of **balancing robot simulation and stability** includes the physical mechanism, transparent equation, numerical prediction, dimensional sanity check, uncertainty discussion and a falsifiable test. The next lesson changes part of the system, so retain a stable definition of the measured variable and the underlying coordinate or timing convention.


---

# U08-L04 — Fluid dosing and process instrumentation

**OpenSTEM Mechanical Engineering · Book 11: Mechatronics Engineering · Unit 8: Integrated Mechatronic Applications.** Educational draft for university study; no hardware-specific safety certification is implied.

## Learning outcome and engineering question

Explain the physical mechanism behind **fluid dosing and process instrumentation** and identify the quantities that can be measured independently. Starting from a realistic unit model, calculate a nominal prediction, check what happens when the governing assumptions break down and propose a discriminating experiment. This lesson is part of a progressive integrated task: Complete design studies with verifiable calculations, data logs and independent safety controls.

**What success looks like.** By the end you should be able to defend the selected equation, label its physical units, derive or justify the result, explain a dominant failure mode, and design an observable test with an explicit acceptance criterion. Separate ideal mathematical behavior from calibration error, deadband, quantization and machine-level uncertainty. The purpose is a model that can be challenged, not an elegant formula without operational meaning.

## Conceptual model

A dosing station requires accurate flow measurement, pump control, valve closure timing and contamination-aware design. Integrate volume by measured flow only within the sensor calibration range; density and viscosity may affect measurement. This particular concept belongs to the broader unit theme: Integrate mechanics, electronics and software under stated evidence limits. Make a small system diagram showing where the relevant signal, mechanical load, power or timing variable enters and where its effect is actually observable. The diagram must distinguish the real plant from its estimate or representation.

**Why the distinction matters.** Demonstrate complete operating cycles including exceptional states. For the integrated example, treat the application as an engineering case study. complete timing diagrams, unit tables, controlled simulations, fault injection and deployment limitations. A plausible result can remain wrong if the coordinate frame, timing origin, sign convention or instrumentation location is inconsistent with the assembled machine.

## Mathematical representation and assumptions

A useful starting relationship is **`V = Q t`**. Read each term aloud with physical dimensions. The expression is a compact model, not a universal constitutive law: its assumptions are the governing physical regime, parameter definition and measurement method described above. State whether the relationship is exact within a defined idealization, an approximation, or an empirical fit.

For sampled systems, timestamp the input and output to distinguish propagation delay from genuine plant dynamics. An unmeasured delay can invalidate an otherwise sound formula. Next, identify at least one quantity in the expression that is independent and one that is dependent. If two independent inputs vary together, a single trial cannot identify their separate effects. List what remains constant in your derivation.

**Boundary check.** Consider reducing the principal input toward zero and increasing it within the permitted physical range. Does the result approach a sensible limit? Note when the formula would produce an unbounded, negative, or otherwise nonphysical output. Even a well-defined mathematical result should be rejected if it implies operation beyond an actuator limit or mechanical stop.

## Worked example with units

At an idealized 0.002 L/s for 150 s, delivered volume is 0.300 L. Rewrite the given numbers before substitution; explicitly carry their units through the equation. Compare the answer to a rough mental estimate and state a sensible number of significant figures. Do not interpret the displayed precision as measured accuracy. The calculation is synthetic unless independently verified against a particular device.

**Sensitivity experiment.** Repeat the calculation after changing one controlling quantity by +10% while keeping other stated inputs fixed. For a linear relationship, expect a proportional response in the appropriate variable; for a nonlinear one, compute the actual change and compare it with the local slope. Explain whether the chosen perturbation is realistic for the application.

**Dimensional audit.** Convert angles, voltages, forces, lengths and time to an explicitly declared convention before putting them in code. A numerical answer with the wrong units is not a small editorial error: it can change the actual machine motion or power demands by large factors. Record the conversion and the numerical rounding separately.

## Engineering integration and trade-offs

Systems thinking requires connecting sensing errors, motion latency, material variability, operator access and maintenance. Performance metrics must include rejected parts, interrupted operation and recovery time; successful output alone is an incomplete measure. For **fluid dosing and process instrumentation**, choose a realistic engineering constraint: supply capacity, maximum permissible temperature, mechanical clearance, sensor bandwidth, task deadline or acceptable uncertainty. Identify how the model interfaces with the preceding and following functions. For example, a correct sensor estimate may still arrive after the actuator can use it.

**Critical failure mode.** Relying solely on commanded pump speed does not detect blocked flow or tubing leaks. Identify which physical measurements could distinguish this failure from an equally plausible alternative. Do not silently compensate for a failed measurement by increasing controller gains. When an estimate is suspect, favor a defined restricted state and transparent diagnostics.

**Design trade study.** Compare a simple implementation with a more instrumented one. The simple version may lower cost and code complexity; the instrumented version may expose hidden failure modes but increases wiring, calibration and software overhead. State the evidence that would justify the additional complexity, not a blanket preference for more sensors.

## Verification and reproducibility

A specific, falsifiable check is: Cross-check gravimetric delivered mass, leakage and timeout responses across fluid temperatures. Define the measured output, sensor range, stimulus, trial count, recording rate and acceptance threshold. Include the expected direction of change before collecting data, and record every rejected measurement with an explanation.

**Robustness check.** Record the maximum as well as the average. A machine that misses one deadline in a hundred may be unusable when every item must be sorted. Repeat under at least two operating conditions and one benign fault. The fault test must not rely on unsafe contact with unguarded moving equipment. If laboratory hardware is unavailable, build a transparent simulation and state that physical validation remains unresolved.

**Suggested notebook entries.** Record the schematic version, parameter values and uncertainties, code or model revision, independent measurement reference, raw-data location, plots, limit-case result and outstanding assumptions. This creates a reproducible chain from requirement to model to observation. A screenshot without settings and raw observations is insufficient evidence.

## Questions and design exercises

1. **Conceptual distinction.** Describe the physical meaning of the central quantities in `V = Q t`. Which are commands, which are direct measurements and which require an estimate? Explain one realistic condition where the relationship should not be trusted.
2. **Quantitative extension.** Reproduce this lesson’s worked calculation from a blank page. Perturb the dominant input by 10% and compute the new prediction with units; estimate the sensitivity ratio and explain whether the effect is linear.
3. **Failure diagnosis.** Suppose a trial contradicts the predicted effect. Design two measurements that could separate the failure described above from a second cause, such as measurement bias, saturation, delay, friction or wiring reversal. Explain why merely repeating the same trial is inconclusive.
4. **Verification design.** Propose a bench or simulation protocol for fluid dosing and process instrumentation: variables held fixed, a sweep range, at least one held-out point, a pass/fail criterion, an independently observed quantity and a defined stop or abort condition. State which conclusions could not be supported by the resulting data.

## Study summary and next connection

A successful treatment of **fluid dosing and process instrumentation** includes the physical mechanism, transparent equation, numerical prediction, dimensional sanity check, uncertainty discussion and a falsifiable test. The next lesson changes part of the system, so retain a stable definition of the measured variable and the underlying coordinate or timing convention.


---

# U08-L05 — Capstone design review and reproducibility

**OpenSTEM Mechanical Engineering · Book 11: Mechatronics Engineering · Unit 8: Integrated Mechatronic Applications.** Educational draft for university study; no hardware-specific safety certification is implied.

## Learning outcome and engineering question

Explain the physical mechanism behind **capstone design review and reproducibility** and identify the quantities that can be measured independently. Starting from a realistic unit model, calculate a nominal prediction, check what happens when the governing assumptions break down and propose a discriminating experiment. This lesson is part of a progressive integrated task: Complete design studies with verifiable calculations, data logs and independent safety controls.

**What success looks like.** By the end you should be able to defend the selected equation, label its physical units, derive or justify the result, explain a dominant failure mode, and design an observable test with an explicit acceptance criterion. Show what happens at a limiting case before relying on an intermediate operating point. The purpose is a model that can be challenged, not an elegant formula without operational meaning.

## Conceptual model

An integrated capstone must have a reproducible bill of materials, wiring and mechanical drawings, firmware version, unit tests and a falsifiable performance claim. A polished interface is not proof of reliability. Define the tests that could disprove the design. This particular concept belongs to the broader unit theme: Integrate mechanics, electronics and software under stated evidence limits. Make a small system diagram showing where the relevant signal, mechanical load, power or timing variable enters and where its effect is actually observable. The diagram must distinguish the real plant from its estimate or representation.

**Why the distinction matters.** Demonstrate complete operating cycles including exceptional states. For the integrated example, treat the application as an engineering case study. complete timing diagrams, unit tables, controlled simulations, fault injection and deployment limitations. A plausible result can remain wrong if the coordinate frame, timing origin, sign convention or instrumentation location is inconsistent with the assembled machine.

## Mathematical representation and assumptions

A useful starting relationship is **`availability = uptime/(uptime+downtime)`**. Read each term aloud with physical dimensions. The expression is a compact model, not a universal constitutive law: its assumptions are the governing physical regime, parameter definition and measurement method described above. State whether the relationship is exact within a defined idealization, an approximation, or an empirical fit.

In a design calculation, rounding should occur at reporting time. Retain guard digits during intermediate steps so that resolution errors are not mistaken for physical discrepancies. Next, identify at least one quantity in the expression that is independent and one that is dependent. If two independent inputs vary together, a single trial cannot identify their separate effects. List what remains constant in your derivation.

**Boundary check.** Consider reducing the principal input toward zero and increasing it within the permitted physical range. Does the result approach a sensible limit? Note when the formula would produce an unbounded, negative, or otherwise nonphysical output. Even a well-defined mathematical result should be rejected if it implies operation beyond an actuator limit or mechanical stop.

## Worked example with units

If a hypothetical system ran 95 h and was unavailable for 5 h, observed availability is 95%, without evidence of long-term reliability. Rewrite the given numbers before substitution; explicitly carry their units through the equation. Compare the answer to a rough mental estimate and state a sensible number of significant figures. Do not interpret the displayed precision as measured accuracy. The calculation is synthetic unless independently verified against a particular device.

**Sensitivity experiment.** Repeat the calculation after changing one controlling quantity by +10% while keeping other stated inputs fixed. For a linear relationship, expect a proportional response in the appropriate variable; for a nonlinear one, compute the actual change and compare it with the local slope. Explain whether the chosen perturbation is realistic for the application.

**Dimensional audit.** Convert angles, voltages, forces, lengths and time to an explicitly declared convention before putting them in code. A numerical answer with the wrong units is not a small editorial error: it can change the actual machine motion or power demands by large factors. Record the conversion and the numerical rounding separately.

## Engineering integration and trade-offs

Systems thinking requires connecting sensing errors, motion latency, material variability, operator access and maintenance. Performance metrics must include rejected parts, interrupted operation and recovery time; successful output alone is an incomplete measure. For **capstone design review and reproducibility**, choose a realistic engineering constraint: supply capacity, maximum permissible temperature, mechanical clearance, sensor bandwidth, task deadline or acceptable uncertainty. Identify how the model interfaces with the preceding and following functions. For example, a correct sensor estimate may still arrive after the actuator can use it.

**Critical failure mode.** Selective reporting of successful demonstrations hides faults and underestimates the cost of maintenance. Identify which physical measurements could distinguish this failure from an equally plausible alternative. Do not silently compensate for a failed measurement by increasing controller gains. When an estimate is suspect, favor a defined restricted state and transparent diagnostics.

**Design trade study.** Compare a simple implementation with a more instrumented one. The simple version may lower cost and code complexity; the instrumented version may expose hidden failure modes but increases wiring, calibration and software overhead. State the evidence that would justify the additional complexity, not a blanket preference for more sensors.

## Verification and reproducibility

A specific, falsifiable check is: Publish a de-identified log of every test, with failures, safety exceptions, software commits and uncertainty. Define the measured output, sensor range, stimulus, trial count, recording rate and acceptance threshold. Include the expected direction of change before collecting data, and record every rejected measurement with an explanation.

**Robustness check.** Use an independently calibrated reference if possible. Comparing two software values derived from one biased sensor does not validate the measurement. Repeat under at least two operating conditions and one benign fault. The fault test must not rely on unsafe contact with unguarded moving equipment. If laboratory hardware is unavailable, build a transparent simulation and state that physical validation remains unresolved.

**Suggested notebook entries.** Record the schematic version, parameter values and uncertainties, code or model revision, independent measurement reference, raw-data location, plots, limit-case result and outstanding assumptions. This creates a reproducible chain from requirement to model to observation. A screenshot without settings and raw observations is insufficient evidence.

## Questions and design exercises

1. **Conceptual distinction.** Describe the physical meaning of the central quantities in `availability = uptime/(uptime+downtime)`. Which are commands, which are direct measurements and which require an estimate? Explain one realistic condition where the relationship should not be trusted.
2. **Quantitative extension.** Reproduce this lesson’s worked calculation from a blank page. Perturb the dominant input by 10% and compute the new prediction with units; estimate the sensitivity ratio and explain whether the effect is linear.
3. **Failure diagnosis.** Suppose a trial contradicts the predicted effect. Design two measurements that could separate the failure described above from a second cause, such as measurement bias, saturation, delay, friction or wiring reversal. Explain why merely repeating the same trial is inconclusive.
4. **Verification design.** Propose a bench or simulation protocol for capstone design review and reproducibility: variables held fixed, a sweep range, at least one held-out point, a pass/fail criterion, an independently observed quantity and a defined stop or abort condition. State which conclusions could not be supported by the resulting data.

## Study summary and next connection

A successful treatment of **capstone design review and reproducibility** includes the physical mechanism, transparent equation, numerical prediction, dimensional sanity check, uncertainty discussion and a falsifiable test. The next lesson changes part of the system, so retain a stable definition of the measured variable and the underlying coordinate or timing convention.


---

