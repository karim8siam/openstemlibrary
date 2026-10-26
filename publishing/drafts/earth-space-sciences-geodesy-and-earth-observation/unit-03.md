# Unit 3: Satellite Positioning and GNSS Data Quality

## Guiding problem

How do signals from orbiting spacecraft become ground coordinates, and what limits their trustworthiness?

**Fictional investigation:** A synthetic GNSS campaign measures a reservoir rim during multipath conditions. Learners compare code ranges and carrier phase, identify clock and atmospheric effects, and evaluate an alternate observing schedule.

## Scientific scope

GNSS estimates are solutions of models linking satellite orbits and clocks, Earth rotation, atmospheric delays, antenna behavior and measurement noise. The number of visible satellites is not a stand-in for solution integrity. Whenever positions, ranges, elevations or images are compared, uncertainty must be attached to a specified measurand and an explicitly identified reference. The word accurate is incomplete unless the reader can state accurate relative to what, over which interval and for which population of conditions. A local fit may be adequate for instruction without being an operationally defensible geodetic product.

## Unit practical: GNSS observation design

Choose observing times and satellite elevations for a hypothetical reference station and rover. Make a table separating code observables, carrier phases, clock estimates, atmospheric corrections, multipath, antenna geometry and covariance.

Perform two independent occupations with changed satellite geometry; compare observed closure with propagated uncertainty. A persistent offset may indicate systematics rather than improved precision.

Present a rejected data window along with the reasons for rejection; do not conceal adverse evidence.

## Data notebook requirements

Create a plain-text notebook containing input columns, units, a source/provenance statement, treatment of missing records, computational steps and at least one independent check. All datasets in this unit are manufactured for learning rather than sampled from nature. When reporting an estimated number, write out the assumptions connecting the number with the claimed physical variable. Note whether uncertainty is random, systematic or model-based. Provide a short explanation of what the number *cannot* tell us. The purpose is to practice disciplined geodetic reasoning as well as numerical computation.

## Lesson 3.1: GNSS observables and ranges

### Physical model and vocabulary

Code observables approximate geometric range plus satellite and receiver clock terms, atmosphere and hardware biases. Carrier phase enables precise relative positioning, but introduces unknown integer-cycle ambiguities. A useful physical statement explicitly identifies the quantity being observed, the idealizations needed to interpret it, and at least one phenomenon excluded by the model. Write a small equation or a structured dependency diagram before processing numbers. If two physical mechanisms can generate the same measurement, the inverse problem is not unique without a further constraint. The correct level of modeling depends on the consequence of the intended decision; an approximation acceptable in a classroom is not automatically acceptable in cadastral surveying, flood warnings or infrastructure monitoring.

### Observation design and instrumentation

Label all terms in a synthetic pseudorange record and convert a receiver clock offset into its equivalent range bias. Note the difference between observation and estimated state. For this lesson, use the following common unit protocol as an explicit checklist: Choose observing times and satellite elevations for a hypothetical reference station and rover. Make a table separating code observables, carrier phases, clock estimates, atmospheric corrections, multipath, antenna geometry and covariance. Record the raw observable, its units, its collection conditions and any correction applied before deriving the displayed result. Distinguish a physically measured range, image intensity or height difference from a parameter that software estimated after applying assumptions. The same nominal output may be produced by different measurement procedures with different covariance and failure modes. Create a versioned log of those differences before comparing datasets.

### Worked numerical case 3.1: Clock-to-range conversion

**Given:** 12 ns clock bias. **Calculation rule:** Convert nanoseconds to seconds and multiply by vacuum light speed. **Computed result:** 3.59751 m. Report enough significant digits to show the underlying arithmetic, but do not claim that all displayed digits are measured information. The worked quantity is hypothetical and intentionally idealized. Recalculate it using original units rather than mentally switching between millimeters, meters, kilometers and degrees. Then double-check dimensions and evaluate whether a physically reasonable change in input produces the expected direction of change.

**Sensitivity test.** Rerun the given calculation with a modestly changed input, preferably increasing the magnitude by ten percent while keeping all other assumptions fixed. Describe both the absolute and relative output change. This isolates sensitivity to one variable only; it is not a total uncertainty budget. If a source has correlated errors, do not combine them with independent-error root-sum-of-squares unless independence is justified. A credible interpretation explains which input is a field observation, which is a normative constant and which is a teaching assumption.

### Confounding and alternative explanation

**Frequent mistake:** Treating a code pseudorange as the true physical distance to a satellite neglects clock and propagation corrections. Perform two independent occupations with changed satellite geometry; compare observed closure with propagated uncertainty. A persistent offset may indicate systematics rather than improved precision. Construct a competing explanation and decide which new observation would discriminate between the two. Avoid evaluating success by how smooth a graphic looks. Negative controls, repeated occupations, held-out locations and cross-sensor checks can be more informative than extra decimals. Classify each candidate error as one of reference mismatch, geometry, calibration, atmospheric or environmental variability, temporal sampling or inference-model misspecification. Explain why that distinction matters for the specific conclusion being attempted.

### Applied case and decision quality

Explain why a smartphone position cannot simply be upgraded to survey accuracy by printing more decimals. Present a rejected data window along with the reasons for rejection; do not conceal adverse evidence. In your written response, first state the decision being supported. Then give a physically meaningful result with units and coordinate conventions. Follow it with the strongest alternative explanation and an observation that could overturn your current interpretation. If uncertainty overlaps the stakeholder threshold, report that ambiguity rather than assigning unwarranted confidence to either choice. This discipline connects a numerical model to a traceable claim about the world.

### Guided questions and independent exercise

1. Which variables in this lesson are directly observed, and which are inferred after applying a physical model? Give the relevant units and reference conventions.
2. Recalculate the worked case after changing the controlling input by 10%; explain the direction of the resulting change and what assumption remained fixed.
3. Explain why the following pitfall matters for the current scientific claim: Treating a code pseudorange as the true physical distance to a satellite neglects clock and propagation corrections.
4. Propose one independent measurement or hold-out test that could reveal a systematic error not visible in the original calculation.
5. Write a three-sentence risk statement separating the demonstrated calculation from an application it is not qualified to support.

## Lesson 3.2: Satellite geometry and dilution

### Physical model and vocabulary

Navigation quality depends on the geometry of line-of-sight vectors as well as noise. Poorly distributed satellites can yield unstable direction estimates despite high counts. A useful physical statement explicitly identifies the quantity being observed, the idealizations needed to interpret it, and at least one phenomenon excluded by the model. Write a small equation or a structured dependency diagram before processing numbers. If two physical mechanisms can generate the same measurement, the inverse problem is not unique without a further constraint. The correct level of modeling depends on the consequence of the intended decision; an approximation acceptable in a classroom is not automatically acceptable in cadastral surveying, flood warnings or infrastructure monitoring.

### Observation design and instrumentation

Construct a simple design matrix for alternate synthetic constellations and compare geometry indicators while holding observation noise approximately fixed. For this lesson, use the following common unit protocol as an explicit checklist: Choose observing times and satellite elevations for a hypothetical reference station and rover. Make a table separating code observables, carrier phases, clock estimates, atmospheric corrections, multipath, antenna geometry and covariance. Record the raw observable, its units, its collection conditions and any correction applied before deriving the displayed result. Distinguish a physically measured range, image intensity or height difference from a parameter that software estimated after applying assumptions. The same nominal output may be produced by different measurement procedures with different covariance and failure modes. Create a versioned log of those differences before comparing datasets.

### Worked numerical case 3.2: First-order ionosphere L1

**Given:** 9 TECU. **Calculation rule:** Group delay = 40.3 TEC/f², with TEC in electrons/m² and frequency in Hz. **Computed result:** 1.46135 m. Report enough significant digits to show the underlying arithmetic, but do not claim that all displayed digits are measured information. The worked quantity is hypothetical and intentionally idealized. Recalculate it using original units rather than mentally switching between millimeters, meters, kilometers and degrees. Then double-check dimensions and evaluate whether a physically reasonable change in input produces the expected direction of change.

**Sensitivity test.** Rerun the given calculation with a modestly changed input, preferably increasing the magnitude by ten percent while keeping all other assumptions fixed. Describe both the absolute and relative output change. This isolates sensitivity to one variable only; it is not a total uncertainty budget. If a source has correlated errors, do not combine them with independent-error root-sum-of-squares unless independence is justified. A credible interpretation explains which input is a field observation, which is a normative constant and which is a teaching assumption.

### Confounding and alternative explanation

**Frequent mistake:** DOP is not position error itself; multipath, orbit biases and local interference may dominate in nominally favorable geometry. Perform two independent occupations with changed satellite geometry; compare observed closure with propagated uncertainty. A persistent offset may indicate systematics rather than improved precision. Construct a competing explanation and decide which new observation would discriminate between the two. Avoid evaluating success by how smooth a graphic looks. Negative controls, repeated occupations, held-out locations and cross-sensor checks can be more informative than extra decimals. Classify each candidate error as one of reference mismatch, geometry, calibration, atmospheric or environmental variability, temporal sampling or inference-model misspecification. Explain why that distinction matters for the specific conclusion being attempted.

### Applied case and decision quality

Choose an observation window for an urban canyon campaign and document why geometry is only one factor. Present a rejected data window along with the reasons for rejection; do not conceal adverse evidence. In your written response, first state the decision being supported. Then give a physically meaningful result with units and coordinate conventions. Follow it with the strongest alternative explanation and an observation that could overturn your current interpretation. If uncertainty overlaps the stakeholder threshold, report that ambiguity rather than assigning unwarranted confidence to either choice. This discipline connects a numerical model to a traceable claim about the world.

### Guided questions and independent exercise

1. Which variables in this lesson are directly observed, and which are inferred after applying a physical model? Give the relevant units and reference conventions.
2. Recalculate the worked case after changing the controlling input by 10%; explain the direction of the resulting change and what assumption remained fixed.
3. Explain why the following pitfall matters for the current scientific claim: DOP is not position error itself; multipath, orbit biases and local interference may dominate in nominally favorable geometry.
4. Propose one independent measurement or hold-out test that could reveal a systematic error not visible in the original calculation.
5. Write a three-sentence risk statement separating the demonstrated calculation from an application it is not qualified to support.

## Lesson 3.3: Ionosphere and troposphere

### Physical model and vocabulary

Microwave GNSS observations are delayed by the neutral atmosphere, and first-order ionospheric range delay scales approximately with inverse square of carrier frequency. Dual-frequency measurements help isolate dispersive terms. A useful physical statement explicitly identifies the quantity being observed, the idealizations needed to interpret it, and at least one phenomenon excluded by the model. Write a small equation or a structured dependency diagram before processing numbers. If two physical mechanisms can generate the same measurement, the inverse problem is not unique without a further constraint. The correct level of modeling depends on the consequence of the intended decision; an approximation acceptable in a classroom is not automatically acceptable in cadastral surveying, flood warnings or infrastructure monitoring.

### Observation design and instrumentation

Compare a modeled path delay under low and high elevation angles and identify which parts are estimated, externally corrected or left in the residuals. For this lesson, use the following common unit protocol as an explicit checklist: Choose observing times and satellite elevations for a hypothetical reference station and rover. Make a table separating code observables, carrier phases, clock estimates, atmospheric corrections, multipath, antenna geometry and covariance. Record the raw observable, its units, its collection conditions and any correction applied before deriving the displayed result. Distinguish a physically measured range, image intensity or height difference from a parameter that software estimated after applying assumptions. The same nominal output may be produced by different measurement procedures with different covariance and failure modes. Create a versioned log of those differences before comparing datasets.

### Worked numerical case 3.3: Slant delay illustration

**Given:** 2.7 m zenith wet delay. **Calculation rule:** Approximate slant delay from a fixed mapping factor of 1/0.75; real maps depend on elevation and atmosphere. **Computed result:** 3.6 m. Report enough significant digits to show the underlying arithmetic, but do not claim that all displayed digits are measured information. The worked quantity is hypothetical and intentionally idealized. Recalculate it using original units rather than mentally switching between millimeters, meters, kilometers and degrees. Then double-check dimensions and evaluate whether a physically reasonable change in input produces the expected direction of change.

**Sensitivity test.** Rerun the given calculation with a modestly changed input, preferably increasing the magnitude by ten percent while keeping all other assumptions fixed. Describe both the absolute and relative output change. This isolates sensitivity to one variable only; it is not a total uncertainty budget. If a source has correlated errors, do not combine them with independent-error root-sum-of-squares unless independence is justified. A credible interpretation explains which input is a field observation, which is a normative constant and which is a teaching assumption.

### Confounding and alternative explanation

**Frequent mistake:** An ionospheric correction does not eliminate wet-tropospheric uncertainty, while a tropospheric model cannot remove multipath from nearby buildings. Perform two independent occupations with changed satellite geometry; compare observed closure with propagated uncertainty. A persistent offset may indicate systematics rather than improved precision. Construct a competing explanation and decide which new observation would discriminate between the two. Avoid evaluating success by how smooth a graphic looks. Negative controls, repeated occupations, held-out locations and cross-sensor checks can be more informative than extra decimals. Classify each candidate error as one of reference mismatch, geometry, calibration, atmospheric or environmental variability, temporal sampling or inference-model misspecification. Explain why that distinction matters for the specific conclusion being attempted.

### Applied case and decision quality

Prepare a field protocol for tropical humidity and rapidly changing ionospheric conditions. Present a rejected data window along with the reasons for rejection; do not conceal adverse evidence. In your written response, first state the decision being supported. Then give a physically meaningful result with units and coordinate conventions. Follow it with the strongest alternative explanation and an observation that could overturn your current interpretation. If uncertainty overlaps the stakeholder threshold, report that ambiguity rather than assigning unwarranted confidence to either choice. This discipline connects a numerical model to a traceable claim about the world.

### Guided questions and independent exercise

1. Which variables in this lesson are directly observed, and which are inferred after applying a physical model? Give the relevant units and reference conventions.
2. Recalculate the worked case after changing the controlling input by 10%; explain the direction of the resulting change and what assumption remained fixed.
3. Explain why the following pitfall matters for the current scientific claim: An ionospheric correction does not eliminate wet-tropospheric uncertainty, while a tropospheric model cannot remove multipath from nearby buildings.
4. Propose one independent measurement or hold-out test that could reveal a systematic error not visible in the original calculation.
5. Write a three-sentence risk statement separating the demonstrated calculation from an application it is not qualified to support.

## Lesson 3.4: Differential GNSS and RTK

### Physical model and vocabulary

Relative positioning uses a base station or reference network to mitigate shared errors and estimate short-baseline ambiguities. Real-time kinematic fixes depend on communication, geometry and solution validation. A useful physical statement explicitly identifies the quantity being observed, the idealizations needed to interpret it, and at least one phenomenon excluded by the model. Write a small equation or a structured dependency diagram before processing numbers. If two physical mechanisms can generate the same measurement, the inverse problem is not unique without a further constraint. The correct level of modeling depends on the consequence of the intended decision; an approximation acceptable in a classroom is not automatically acceptable in cadastral surveying, flood warnings or infrastructure monitoring.

### Observation design and instrumentation

Analyze a synthetic rover trajectory with solution-status flags, base-to-rover distance and check-point residuals. Reject segments inconsistent with independent control. For this lesson, use the following common unit protocol as an explicit checklist: Choose observing times and satellite elevations for a hypothetical reference station and rover. Make a table separating code observables, carrier phases, clock estimates, atmospheric corrections, multipath, antenna geometry and covariance. Record the raw observable, its units, its collection conditions and any correction applied before deriving the displayed result. Distinguish a physically measured range, image intensity or height difference from a parameter that software estimated after applying assumptions. The same nominal output may be produced by different measurement procedures with different covariance and failure modes. Create a versioned log of those differences before comparing datasets.

### Worked numerical case 3.4: Dilution illustration

**Given:** 0.9 m range-equivalent scatter. **Calculation rule:** Illustrative DOP-like factor 2.3 × scalar input; not a complete covariance solution. **Computed result:** 2.07 m position-equivalent scatter. Report enough significant digits to show the underlying arithmetic, but do not claim that all displayed digits are measured information. The worked quantity is hypothetical and intentionally idealized. Recalculate it using original units rather than mentally switching between millimeters, meters, kilometers and degrees. Then double-check dimensions and evaluate whether a physically reasonable change in input produces the expected direction of change.

**Sensitivity test.** Rerun the given calculation with a modestly changed input, preferably increasing the magnitude by ten percent while keeping all other assumptions fixed. Describe both the absolute and relative output change. This isolates sensitivity to one variable only; it is not a total uncertainty budget. If a source has correlated errors, do not combine them with independent-error root-sum-of-squares unless independence is justified. A credible interpretation explains which input is a field observation, which is a normative constant and which is a teaching assumption.

### Confounding and alternative explanation

**Frequent mistake:** A reported fixed ambiguity solution can still be wrong; use repeat occupations and external checks rather than trusting the status label alone. Perform two independent occupations with changed satellite geometry; compare observed closure with propagated uncertainty. A persistent offset may indicate systematics rather than improved precision. Construct a competing explanation and decide which new observation would discriminate between the two. Avoid evaluating success by how smooth a graphic looks. Negative controls, repeated occupations, held-out locations and cross-sensor checks can be more informative than extra decimals. Classify each candidate error as one of reference mismatch, geometry, calibration, atmospheric or environmental variability, temporal sampling or inference-model misspecification. Explain why that distinction matters for the specific conclusion being attempted.

### Applied case and decision quality

Evaluate whether an RTK survey is suitable for deformation monitoring near a construction excavation. Present a rejected data window along with the reasons for rejection; do not conceal adverse evidence. In your written response, first state the decision being supported. Then give a physically meaningful result with units and coordinate conventions. Follow it with the strongest alternative explanation and an observation that could overturn your current interpretation. If uncertainty overlaps the stakeholder threshold, report that ambiguity rather than assigning unwarranted confidence to either choice. This discipline connects a numerical model to a traceable claim about the world.

### Guided questions and independent exercise

1. Which variables in this lesson are directly observed, and which are inferred after applying a physical model? Give the relevant units and reference conventions.
2. Recalculate the worked case after changing the controlling input by 10%; explain the direction of the resulting change and what assumption remained fixed.
3. Explain why the following pitfall matters for the current scientific claim: A reported fixed ambiguity solution can still be wrong; use repeat occupations and external checks rather than trusting the status label alone.
4. Propose one independent measurement or hold-out test that could reveal a systematic error not visible in the original calculation.
5. Write a three-sentence risk statement separating the demonstrated calculation from an application it is not qualified to support.

## Lesson 3.5: Precise point positioning and networks

### Physical model and vocabulary

PPP uses precise orbit and clock products together with detailed observation models; network solutions distribute reference information across stations. Convergence, temporal stability and frame realization matter. A useful physical statement explicitly identifies the quantity being observed, the idealizations needed to interpret it, and at least one phenomenon excluded by the model. Write a small equation or a structured dependency diagram before processing numbers. If two physical mechanisms can generate the same measurement, the inverse problem is not unique without a further constraint. The correct level of modeling depends on the consequence of the intended decision; an approximation acceptable in a classroom is not automatically acceptable in cadastral surveying, flood warnings or infrastructure monitoring.

### Observation design and instrumentation

Compare synthetic coordinate estimates at different convergence times and test whether reported uncertainty covers held-out station differences. For this lesson, use the following common unit protocol as an explicit checklist: Choose observing times and satellite elevations for a hypothetical reference station and rover. Make a table separating code observables, carrier phases, clock estimates, atmospheric corrections, multipath, antenna geometry and covariance. Record the raw observable, its units, its collection conditions and any correction applied before deriving the displayed result. Distinguish a physically measured range, image intensity or height difference from a parameter that software estimated after applying assumptions. The same nominal output may be produced by different measurement procedures with different covariance and failure modes. Create a versioned log of those differences before comparing datasets.

### Worked numerical case 3.5: Two-sigma code error

**Given:** 2.4 m standard deviation. **Calculation rule:** A Gaussian 2σ interval uses two times the assumed standard deviation; it is not a guaranteed bound. **Computed result:** 4.8 m. Report enough significant digits to show the underlying arithmetic, but do not claim that all displayed digits are measured information. The worked quantity is hypothetical and intentionally idealized. Recalculate it using original units rather than mentally switching between millimeters, meters, kilometers and degrees. Then double-check dimensions and evaluate whether a physically reasonable change in input produces the expected direction of change.

**Sensitivity test.** Rerun the given calculation with a modestly changed input, preferably increasing the magnitude by ten percent while keeping all other assumptions fixed. Describe both the absolute and relative output change. This isolates sensitivity to one variable only; it is not a total uncertainty budget. If a source has correlated errors, do not combine them with independent-error root-sum-of-squares unless independence is justified. A credible interpretation explains which input is a field observation, which is a normative constant and which is a teaching assumption.

### Confounding and alternative explanation

**Frequent mistake:** A long occupation does not repair a mislabeled antenna offset, omitted cycle slip or reference-frame mismatch. Perform two independent occupations with changed satellite geometry; compare observed closure with propagated uncertainty. A persistent offset may indicate systematics rather than improved precision. Construct a competing explanation and decide which new observation would discriminate between the two. Avoid evaluating success by how smooth a graphic looks. Negative controls, repeated occupations, held-out locations and cross-sensor checks can be more informative than extra decimals. Classify each candidate error as one of reference mismatch, geometry, calibration, atmospheric or environmental variability, temporal sampling or inference-model misspecification. Explain why that distinction matters for the specific conclusion being attempted.

### Applied case and decision quality

Design an archive for a repeatable continental positioning experiment over multiple years. Present a rejected data window along with the reasons for rejection; do not conceal adverse evidence. In your written response, first state the decision being supported. Then give a physically meaningful result with units and coordinate conventions. Follow it with the strongest alternative explanation and an observation that could overturn your current interpretation. If uncertainty overlaps the stakeholder threshold, report that ambiguity rather than assigning unwarranted confidence to either choice. This discipline connects a numerical model to a traceable claim about the world.

### Guided questions and independent exercise

1. Which variables in this lesson are directly observed, and which are inferred after applying a physical model? Give the relevant units and reference conventions.
2. Recalculate the worked case after changing the controlling input by 10%; explain the direction of the resulting change and what assumption remained fixed.
3. Explain why the following pitfall matters for the current scientific claim: A long occupation does not repair a mislabeled antenna offset, omitted cycle slip or reference-frame mismatch.
4. Propose one independent measurement or hold-out test that could reveal a systematic error not visible in the original calculation.
5. Write a three-sentence risk statement separating the demonstrated calculation from an application it is not qualified to support.

## Unit synthesis and interpretive assessment

A synthetic GNSS campaign measures a reservoir rim during multipath conditions. Learners compare code ranges and carrier phase, identify clock and atmospheric effects, and evaluate an alternate observing schedule. Develop a compact research plan with a clear inference target, observational geometry, sampling strategy, numerical cross-check and validation design. Present one figure that retains units and reference-frame metadata. Describe a case in which apparent agreement across measurements may still result from shared bias. What additional independent measurement would break that dependence?

The main theme is this: GNSS estimates are solutions of models linking satellite orbits and clocks, Earth rotation, atmospheric delays, antenna behavior and measurement noise. The number of visible satellites is not a stand-in for solution integrity. Before using the unit result to guide a practical choice, ask whether the error bar reflects the true sources of uncertainty or only the variation inside a simplified numerical procedure. Define the population and period in which the conclusion is intended to hold. A consistent interpretation must remain intelligible without dependence on a proprietary figure or a hidden processing step.

