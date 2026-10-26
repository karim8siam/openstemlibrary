# Unit 8: Integrated Earth Observation and Responsible Decisions

## Guiding problem

How are geodetic and remotely sensed products turned into defensible, reproducible decisions?

**Fictional investigation:** A fictional coastal megacity needs a land-subsidence and flood-risk assessment. Students integrate control stations, tide gauges, radar interferometry, optical imagery and field elevation checks while avoiding false precision.

## Scientific scope

The final goal is evidence integration rather than sensor enthusiasm. One instrument may supply precise geometry and another spatial coverage; agreement is meaningful only with independent error models and common coordinate definitions. Whenever positions, ranges, elevations or images are compared, uncertainty must be attached to a specified measurand and an explicitly identified reference. The word accurate is incomplete unless the reader can state accurate relative to what, over which interval and for which population of conditions. A local fit may be adequate for instruction without being an operationally defensible geodetic product.

## Unit practical: Decision and reproducibility protocol

Define an explicit target variable, stakeholder decision threshold and error cost before viewing a map. Hold out reference observations and version every transformation and filter.

Compare a simple baseline with a more complex model using the same independent test data. Discuss failure cases and unrepresented communities, not just one summary accuracy score.

Write a reproducible release note giving the physical limitations and foreseeable misuse of the output.

## Data notebook requirements

Create a plain-text notebook containing input columns, units, a source/provenance statement, treatment of missing records, computational steps and at least one independent check. All datasets in this unit are manufactured for learning rather than sampled from nature. When reporting an estimated number, write out the assumptions connecting the number with the claimed physical variable. Note whether uncertainty is random, systematic or model-based. Provide a short explanation of what the number *cannot* tell us. The purpose is to practice disciplined geodetic reasoning as well as numerical computation.

## Lesson 8.1: Multisensor registration and fusion

### Physical model and vocabulary

Co-registering satellite scenes and field control requires a declared frame, epoch, image geometry and spatial uncertainty model. Fusion can improve interpretation but also propagate correlated errors. A useful physical statement explicitly identifies the quantity being observed, the idealizations needed to interpret it, and at least one phenomenon excluded by the model. Write a small equation or a structured dependency diagram before processing numbers. If two physical mechanisms can generate the same measurement, the inverse problem is not unique without a further constraint. The correct level of modeling depends on the consequence of the intended decision; an approximation acceptable in a classroom is not automatically acceptable in cadastral surveying, flood warnings or infrastructure monitoring.

### Observation design and instrumentation

Perform a synthetic ground-control residual analysis using held-out points and compare the fused product with each sensor alone. For this lesson, use the following common unit protocol as an explicit checklist: Define an explicit target variable, stakeholder decision threshold and error cost before viewing a map. Hold out reference observations and version every transformation and filter. Record the raw observable, its units, its collection conditions and any correction applied before deriving the displayed result. Distinguish a physically measured range, image intensity or height difference from a parameter that software estimated after applying assumptions. The same nominal output may be produced by different measurement procedures with different covariance and failure modes. Create a versioned log of those differences before comparing datasets.

### Worked numerical case 8.1: Point-check RMSE

**Given:** 0.4 m final residual. **Calculation rule:** RMSE from four held-out horizontal residual magnitudes in meters. **Computed result:** 0.367423 m. Report enough significant digits to show the underlying arithmetic, but do not claim that all displayed digits are measured information. The worked quantity is hypothetical and intentionally idealized. Recalculate it using original units rather than mentally switching between millimeters, meters, kilometers and degrees. Then double-check dimensions and evaluate whether a physically reasonable change in input produces the expected direction of change.

**Sensitivity test.** Rerun the given calculation with a modestly changed input, preferably increasing the magnitude by ten percent while keeping all other assumptions fixed. Describe both the absolute and relative output change. This isolates sensitivity to one variable only; it is not a total uncertainty budget. If a source has correlated errors, do not combine them with independent-error root-sum-of-squares unless independence is justified. A credible interpretation explains which input is a field observation, which is a normative constant and which is a teaching assumption.

### Confounding and alternative explanation

**Frequent mistake:** Matching image edges visually does not prove geodetic alignment; two data products may share the same systematic control error. Compare a simple baseline with a more complex model using the same independent test data. Discuss failure cases and unrepresented communities, not just one summary accuracy score. Construct a competing explanation and decide which new observation would discriminate between the two. Avoid evaluating success by how smooth a graphic looks. Negative controls, repeated occupations, held-out locations and cross-sensor checks can be more informative than extra decimals. Classify each candidate error as one of reference mismatch, geometry, calibration, atmospheric or environmental variability, temporal sampling or inference-model misspecification. Explain why that distinction matters for the specific conclusion being attempted.

### Applied case and decision quality

Draft acceptance criteria for a city mapping procurement using independent checkpoints. Write a reproducible release note giving the physical limitations and foreseeable misuse of the output. In your written response, first state the decision being supported. Then give a physically meaningful result with units and coordinate conventions. Follow it with the strongest alternative explanation and an observation that could overturn your current interpretation. If uncertainty overlaps the stakeholder threshold, report that ambiguity rather than assigning unwarranted confidence to either choice. This discipline connects a numerical model to a traceable claim about the world.

### Guided questions and independent exercise

1. Which variables in this lesson are directly observed, and which are inferred after applying a physical model? Give the relevant units and reference conventions.
2. Recalculate the worked case after changing the controlling input by 10%; explain the direction of the resulting change and what assumption remained fixed.
3. Explain why the following pitfall matters for the current scientific claim: Matching image edges visually does not prove geodetic alignment; two data products may share the same systematic control error.
4. Propose one independent measurement or hold-out test that could reveal a systematic error not visible in the original calculation.
5. Write a three-sentence risk statement separating the demonstrated calculation from an application it is not qualified to support.

## Lesson 8.2: Change detection and false alarms

### Physical model and vocabulary

Difference images mix physical change with illumination, orbit geometry, sensor calibration, seasonal cycles and processing effects. Formal change detection needs stable comparison units and thresholds. A useful physical statement explicitly identifies the quantity being observed, the idealizations needed to interpret it, and at least one phenomenon excluded by the model. Write a small equation or a structured dependency diagram before processing numbers. If two physical mechanisms can generate the same measurement, the inverse problem is not unique without a further constraint. The correct level of modeling depends on the consequence of the intended decision; an approximation acceptable in a classroom is not automatically acceptable in cadastral surveying, flood warnings or infrastructure monitoring.

### Observation design and instrumentation

Build a two-date synthetic land-cover table and investigate the false-positive rate using manually reviewed samples. For this lesson, use the following common unit protocol as an explicit checklist: Define an explicit target variable, stakeholder decision threshold and error cost before viewing a map. Hold out reference observations and version every transformation and filter. Record the raw observable, its units, its collection conditions and any correction applied before deriving the displayed result. Distinguish a physically measured range, image intensity or height difference from a parameter that software estimated after applying assumptions. The same nominal output may be produced by different measurement procedures with different covariance and failure modes. Create a versioned log of those differences before comparing datasets.

### Worked numerical case 8.2: Classification recall

**Given:** 48 true flood detections. **Calculation rule:** Recall=TP/(TP+FN), with 18 fixed missed flooded samples. **Computed result:** 0.727273 fraction. Report enough significant digits to show the underlying arithmetic, but do not claim that all displayed digits are measured information. The worked quantity is hypothetical and intentionally idealized. Recalculate it using original units rather than mentally switching between millimeters, meters, kilometers and degrees. Then double-check dimensions and evaluate whether a physically reasonable change in input produces the expected direction of change.

**Sensitivity test.** Rerun the given calculation with a modestly changed input, preferably increasing the magnitude by ten percent while keeping all other assumptions fixed. Describe both the absolute and relative output change. This isolates sensitivity to one variable only; it is not a total uncertainty budget. If a source has correlated errors, do not combine them with independent-error root-sum-of-squares unless independence is justified. A credible interpretation explains which input is a field observation, which is a normative constant and which is a teaching assumption.

### Confounding and alternative explanation

**Frequent mistake:** A dramatic red change map can exaggerate statistically weak differences, especially when multiple thresholds are explored after seeing the result. Compare a simple baseline with a more complex model using the same independent test data. Discuss failure cases and unrepresented communities, not just one summary accuracy score. Construct a competing explanation and decide which new observation would discriminate between the two. Avoid evaluating success by how smooth a graphic looks. Negative controls, repeated occupations, held-out locations and cross-sensor checks can be more informative than extra decimals. Classify each candidate error as one of reference mismatch, geometry, calibration, atmospheric or environmental variability, temporal sampling or inference-model misspecification. Explain why that distinction matters for the specific conclusion being attempted.

### Applied case and decision quality

Choose a monitoring protocol for coastal erosion that separates seasonal variability from multi-year retreat. Write a reproducible release note giving the physical limitations and foreseeable misuse of the output. In your written response, first state the decision being supported. Then give a physically meaningful result with units and coordinate conventions. Follow it with the strongest alternative explanation and an observation that could overturn your current interpretation. If uncertainty overlaps the stakeholder threshold, report that ambiguity rather than assigning unwarranted confidence to either choice. This discipline connects a numerical model to a traceable claim about the world.

### Guided questions and independent exercise

1. Which variables in this lesson are directly observed, and which are inferred after applying a physical model? Give the relevant units and reference conventions.
2. Recalculate the worked case after changing the controlling input by 10%; explain the direction of the resulting change and what assumption remained fixed.
3. Explain why the following pitfall matters for the current scientific claim: A dramatic red change map can exaggerate statistically weak differences, especially when multiple thresholds are explored after seeing the result.
4. Propose one independent measurement or hold-out test that could reveal a systematic error not visible in the original calculation.
5. Write a three-sentence risk statement separating the demonstrated calculation from an application it is not qualified to support.

## Lesson 8.3: Time series and uncertainty propagation

### Physical model and vocabulary

Measurements across years can reveal slow trends only if data versions, sensor transitions and time-dependent frames are handled explicitly. Confidence intervals depend on residual correlation and model assumptions. A useful physical statement explicitly identifies the quantity being observed, the idealizations needed to interpret it, and at least one phenomenon excluded by the model. Write a small equation or a structured dependency diagram before processing numbers. If two physical mechanisms can generate the same measurement, the inverse problem is not unique without a further constraint. The correct level of modeling depends on the consequence of the intended decision; an approximation acceptable in a classroom is not automatically acceptable in cadastral surveying, flood warnings or infrastructure monitoring.

### Observation design and instrumentation

Fit a synthetic sea-level or subsidence series with missing months; compare naive independent-error standard errors to a block-bootstrap estimate. For this lesson, use the following common unit protocol as an explicit checklist: Define an explicit target variable, stakeholder decision threshold and error cost before viewing a map. Hold out reference observations and version every transformation and filter. Record the raw observable, its units, its collection conditions and any correction applied before deriving the displayed result. Distinguish a physically measured range, image intensity or height difference from a parameter that software estimated after applying assumptions. The same nominal output may be produced by different measurement procedures with different covariance and failure modes. Create a versioned log of those differences before comparing datasets.

### Worked numerical case 8.3: Change-detection precision

**Given:** 51 true changes. **Calculation rule:** Precision=TP/(TP+FP), with 12 false alarms in a fictional validation set. **Computed result:** 0.809524 fraction. Report enough significant digits to show the underlying arithmetic, but do not claim that all displayed digits are measured information. The worked quantity is hypothetical and intentionally idealized. Recalculate it using original units rather than mentally switching between millimeters, meters, kilometers and degrees. Then double-check dimensions and evaluate whether a physically reasonable change in input produces the expected direction of change.

**Sensitivity test.** Rerun the given calculation with a modestly changed input, preferably increasing the magnitude by ten percent while keeping all other assumptions fixed. Describe both the absolute and relative output change. This isolates sensitivity to one variable only; it is not a total uncertainty budget. If a source has correlated errors, do not combine them with independent-error root-sum-of-squares unless independence is justified. A credible interpretation explains which input is a field observation, which is a normative constant and which is a teaching assumption.

### Confounding and alternative explanation

**Frequent mistake:** Adding more observations does not always yield proportionally more independent information when consecutive errors are autocorrelated. Compare a simple baseline with a more complex model using the same independent test data. Discuss failure cases and unrepresented communities, not just one summary accuracy score. Construct a competing explanation and decide which new observation would discriminate between the two. Avoid evaluating success by how smooth a graphic looks. Negative controls, repeated occupations, held-out locations and cross-sensor checks can be more informative than extra decimals. Classify each candidate error as one of reference mismatch, geometry, calibration, atmospheric or environmental variability, temporal sampling or inference-model misspecification. Explain why that distinction matters for the specific conclusion being attempted.

### Applied case and decision quality

Produce a trend statement for public communication that resists converting uncertainty bounds into a deterministic forecast. Write a reproducible release note giving the physical limitations and foreseeable misuse of the output. In your written response, first state the decision being supported. Then give a physically meaningful result with units and coordinate conventions. Follow it with the strongest alternative explanation and an observation that could overturn your current interpretation. If uncertainty overlaps the stakeholder threshold, report that ambiguity rather than assigning unwarranted confidence to either choice. This discipline connects a numerical model to a traceable claim about the world.

### Guided questions and independent exercise

1. Which variables in this lesson are directly observed, and which are inferred after applying a physical model? Give the relevant units and reference conventions.
2. Recalculate the worked case after changing the controlling input by 10%; explain the direction of the resulting change and what assumption remained fixed.
3. Explain why the following pitfall matters for the current scientific claim: Adding more observations does not always yield proportionally more independent information when consecutive errors are autocorrelated.
4. Propose one independent measurement or hold-out test that could reveal a systematic error not visible in the original calculation.
5. Write a three-sentence risk statement separating the demonstrated calculation from an application it is not qualified to support.

## Lesson 8.4: Validation, ethics and decision thresholds

### Physical model and vocabulary

Validation compares products against evidence independent of model training and parameter tuning. Decisions also require cost, impact, equity, privacy and uncertainty beyond statistical accuracy. A useful physical statement explicitly identifies the quantity being observed, the idealizations needed to interpret it, and at least one phenomenon excluded by the model. Write a small equation or a structured dependency diagram before processing numbers. If two physical mechanisms can generate the same measurement, the inverse problem is not unique without a further constraint. The correct level of modeling depends on the consequence of the intended decision; an approximation acceptable in a classroom is not automatically acceptable in cadastral surveying, flood warnings or infrastructure monitoring.

### Observation design and instrumentation

Construct a confusion matrix for fictional flood classification and evaluate precision, recall and consequences of missed flood exposure. For this lesson, use the following common unit protocol as an explicit checklist: Define an explicit target variable, stakeholder decision threshold and error cost before viewing a map. Hold out reference observations and version every transformation and filter. Record the raw observable, its units, its collection conditions and any correction applied before deriving the displayed result. Distinguish a physically measured range, image intensity or height difference from a parameter that software estimated after applying assumptions. The same nominal output may be produced by different measurement procedures with different covariance and failure modes. Create a versioned log of those differences before comparing datasets.

### Worked numerical case 8.4: Linear trend estimate

**Given:** 15 mm cumulative change. **Calculation rule:** Rate is change over six years, assuming linearity and no abrupt offsets. **Computed result:** 2.5 mm/year. Report enough significant digits to show the underlying arithmetic, but do not claim that all displayed digits are measured information. The worked quantity is hypothetical and intentionally idealized. Recalculate it using original units rather than mentally switching between millimeters, meters, kilometers and degrees. Then double-check dimensions and evaluate whether a physically reasonable change in input produces the expected direction of change.

**Sensitivity test.** Rerun the given calculation with a modestly changed input, preferably increasing the magnitude by ten percent while keeping all other assumptions fixed. Describe both the absolute and relative output change. This isolates sensitivity to one variable only; it is not a total uncertainty budget. If a source has correlated errors, do not combine them with independent-error root-sum-of-squares unless independence is justified. A credible interpretation explains which input is a field observation, which is a normative constant and which is a teaching assumption.

### Confounding and alternative explanation

**Frequent mistake:** An accuracy percentage can conceal failure on rare but consequential events or on communities poorly sampled by the reference dataset. Compare a simple baseline with a more complex model using the same independent test data. Discuss failure cases and unrepresented communities, not just one summary accuracy score. Construct a competing explanation and decide which new observation would discriminate between the two. Avoid evaluating success by how smooth a graphic looks. Negative controls, repeated occupations, held-out locations and cross-sensor checks can be more informative than extra decimals. Classify each candidate error as one of reference mismatch, geometry, calibration, atmospheric or environmental variability, temporal sampling or inference-model misspecification. Explain why that distinction matters for the specific conclusion being attempted.

### Applied case and decision quality

Explain how uncertainty and false alarms should influence emergency warnings without obscuring high-consequence exposure. Write a reproducible release note giving the physical limitations and foreseeable misuse of the output. In your written response, first state the decision being supported. Then give a physically meaningful result with units and coordinate conventions. Follow it with the strongest alternative explanation and an observation that could overturn your current interpretation. If uncertainty overlaps the stakeholder threshold, report that ambiguity rather than assigning unwarranted confidence to either choice. This discipline connects a numerical model to a traceable claim about the world.

### Guided questions and independent exercise

1. Which variables in this lesson are directly observed, and which are inferred after applying a physical model? Give the relevant units and reference conventions.
2. Recalculate the worked case after changing the controlling input by 10%; explain the direction of the resulting change and what assumption remained fixed.
3. Explain why the following pitfall matters for the current scientific claim: An accuracy percentage can conceal failure on rare but consequential events or on communities poorly sampled by the reference dataset.
4. Propose one independent measurement or hold-out test that could reveal a systematic error not visible in the original calculation.
5. Write a three-sentence risk statement separating the demonstrated calculation from an application it is not qualified to support.

## Lesson 8.5: Reproducible workflows and open data

### Physical model and vocabulary

A defensible workflow stores input provenance, licensed use, software versions, datum transformations, quality masks, parameter files and reproducible figures. Versioned products require backward traceability. A useful physical statement explicitly identifies the quantity being observed, the idealizations needed to interpret it, and at least one phenomenon excluded by the model. Write a small equation or a structured dependency diagram before processing numbers. If two physical mechanisms can generate the same measurement, the inverse problem is not unique without a further constraint. The correct level of modeling depends on the consequence of the intended decision; an approximation acceptable in a classroom is not automatically acceptable in cadastral surveying, flood warnings or infrastructure monitoring.

### Observation design and instrumentation

Build a minimal pipeline manifest and rerun a toy subsidence analysis from synthetic CSV files, recording checksums, model choices and a held-out test. For this lesson, use the following common unit protocol as an explicit checklist: Define an explicit target variable, stakeholder decision threshold and error cost before viewing a map. Hold out reference observations and version every transformation and filter. Record the raw observable, its units, its collection conditions and any correction applied before deriving the displayed result. Distinguish a physically measured range, image intensity or height difference from a parameter that software estimated after applying assumptions. The same nominal output may be produced by different measurement procedures with different covariance and failure modes. Create a versioned log of those differences before comparing datasets.

### Worked numerical case 8.5: Independent error combination

**Given:** 0.35 m second error. **Calculation rule:** Independent random uncertainties combine by square-root of summed variances. **Computed result:** 0.413401 m. Report enough significant digits to show the underlying arithmetic, but do not claim that all displayed digits are measured information. The worked quantity is hypothetical and intentionally idealized. Recalculate it using original units rather than mentally switching between millimeters, meters, kilometers and degrees. Then double-check dimensions and evaluate whether a physically reasonable change in input produces the expected direction of change.

**Sensitivity test.** Rerun the given calculation with a modestly changed input, preferably increasing the magnitude by ten percent while keeping all other assumptions fixed. Describe both the absolute and relative output change. This isolates sensitivity to one variable only; it is not a total uncertainty budget. If a source has correlated errors, do not combine them with independent-error root-sum-of-squares unless independence is justified. A credible interpretation explains which input is a field observation, which is a normative constant and which is a teaching assumption.

### Confounding and alternative explanation

**Frequent mistake:** A notebook that runs on one computer is not fully reproducible if external web services, hidden credentials or mutable downloads are not documented. Compare a simple baseline with a more complex model using the same independent test data. Discuss failure cases and unrepresented communities, not just one summary accuracy score. Construct a competing explanation and decide which new observation would discriminate between the two. Avoid evaluating success by how smooth a graphic looks. Negative controls, repeated occupations, held-out locations and cross-sensor checks can be more informative than extra decimals. Classify each candidate error as one of reference mismatch, geometry, calibration, atmospheric or environmental variability, temporal sampling or inference-model misspecification. Explain why that distinction matters for the specific conclusion being attempted.

### Applied case and decision quality

Prepare a research artifact handover suitable for independent checking and later updates. Write a reproducible release note giving the physical limitations and foreseeable misuse of the output. In your written response, first state the decision being supported. Then give a physically meaningful result with units and coordinate conventions. Follow it with the strongest alternative explanation and an observation that could overturn your current interpretation. If uncertainty overlaps the stakeholder threshold, report that ambiguity rather than assigning unwarranted confidence to either choice. This discipline connects a numerical model to a traceable claim about the world.

### Guided questions and independent exercise

1. Which variables in this lesson are directly observed, and which are inferred after applying a physical model? Give the relevant units and reference conventions.
2. Recalculate the worked case after changing the controlling input by 10%; explain the direction of the resulting change and what assumption remained fixed.
3. Explain why the following pitfall matters for the current scientific claim: A notebook that runs on one computer is not fully reproducible if external web services, hidden credentials or mutable downloads are not documented.
4. Propose one independent measurement or hold-out test that could reveal a systematic error not visible in the original calculation.
5. Write a three-sentence risk statement separating the demonstrated calculation from an application it is not qualified to support.

## Unit synthesis and interpretive assessment

A fictional coastal megacity needs a land-subsidence and flood-risk assessment. Students integrate control stations, tide gauges, radar interferometry, optical imagery and field elevation checks while avoiding false precision. Develop a compact research plan with a clear inference target, observational geometry, sampling strategy, numerical cross-check and validation design. Present one figure that retains units and reference-frame metadata. Describe a case in which apparent agreement across measurements may still result from shared bias. What additional independent measurement would break that dependence?

The main theme is this: The final goal is evidence integration rather than sensor enthusiasm. One instrument may supply precise geometry and another spatial coverage; agreement is meaningful only with independent error models and common coordinate definitions. Before using the unit result to guide a practical choice, ask whether the error bar reflects the true sources of uncertainty or only the variation inside a simplified numerical procedure. Define the population and period in which the conclusion is intended to hold. A consistent interpretation must remain intelligible without dependence on a proprietary figure or a hidden processing step.

