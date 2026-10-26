# Unit 1: Earth as a Measured Body and Geodetic Reference

## Guiding problem

What constitutes a terrestrial position if Earth is not a perfect sphere and its crust moves?

**Fictional investigation:** A fictional nationwide survey joins monument locations from different decades, including a harbor tide gauge and a mountain GNSS station. Students must reconcile reference frame, epoch, height surface, geometry and uncertainty before comparing coordinates.

## Scientific scope

Geodesy makes an operational distinction among a physical Earth, its mathematical reference ellipsoid and a realized terrestrial reference frame. A datum name without its realization and observation epoch is often incomplete. The fundamental problem is not only finding an Earth-fixed number but making that number reproducible by another observer. Whenever positions, ranges, elevations or images are compared, uncertainty must be attached to a specified measurand and an explicitly identified reference. The word accurate is incomplete unless the reader can state accurate relative to what, over which interval and for which population of conditions. A local fit may be adequate for instruction without being an operationally defensible geodetic product.

## Unit practical: Frame reconciliation protocol

Construct two coordinate sets for the same fictional monuments. Record each station identifier, realization, reference epoch, coordinate uncertainty and possible velocity. Refuse to calculate a displacement until both position sets have been expressed at one epoch in one declared frame.

Evaluate two plausible error models: an unmodeled common translation and independent local site motion. Both can produce coordinate differences, but only the second corresponds to differential deformation among nearby points.

Distinguish Earth-fixed axes from the instantaneous positions of features and explain why a map’s apparent stability is partly a coordinate convention.

## Data notebook requirements

Create a plain-text notebook containing input columns, units, a source/provenance statement, treatment of missing records, computational steps and at least one independent check. All datasets in this unit are manufactured for learning rather than sampled from nature. When reporting an estimated number, write out the assumptions connecting the number with the claimed physical variable. Note whether uncertainty is random, systematic or model-based. Provide a short explanation of what the number *cannot* tell us. The purpose is to practice disciplined geodetic reasoning as well as numerical computation.

## Lesson 1.1: Earth shape and the geoid

### Physical model and vocabulary

Earth has topography, an equipotential surface of its gravity field and a smooth reference ellipsoid; the three should not be conflated. Gravity and rotation help shape the geoid, while maps need computationally tractable surfaces. A useful physical statement explicitly identifies the quantity being observed, the idealizations needed to interpret it, and at least one phenomenon excluded by the model. Write a small equation or a structured dependency diagram before processing numbers. If two physical mechanisms can generate the same measurement, the inverse problem is not unique without a further constraint. The correct level of modeling depends on the consequence of the intended decision; an approximation acceptable in a classroom is not automatically acceptable in cadastral surveying, flood warnings or infrastructure monitoring.

### Observation design and instrumentation

Compare measured spirit-level height differences with ellipsoidal heights from repeated GNSS occupations and an independently specified geoid model. Check whether apparent discrepancies vary systematically with location. For this lesson, use the following common unit protocol as an explicit checklist: Construct two coordinate sets for the same fictional monuments. Record each station identifier, realization, reference epoch, coordinate uncertainty and possible velocity. Refuse to calculate a displacement until both position sets have been expressed at one epoch in one declared frame. Record the raw observable, its units, its collection conditions and any correction applied before deriving the displayed result. Distinguish a physically measured range, image intensity or height difference from a parameter that software estimated after applying assumptions. The same nominal output may be produced by different measurement procedures with different covariance and failure modes. Create a versioned log of those differences before comparing datasets.

### Worked numerical case 1.1: Spherical arc estimate

**Given:** 2 degrees. **Calculation rule:** Arc length = radius × central angle in radians, approximating Earth by a sphere. **Computed result:** 222.39 km. Report enough significant digits to show the underlying arithmetic, but do not claim that all displayed digits are measured information. The worked quantity is hypothetical and intentionally idealized. Recalculate it using original units rather than mentally switching between millimeters, meters, kilometers and degrees. Then double-check dimensions and evaluate whether a physically reasonable change in input produces the expected direction of change.

**Sensitivity test.** Rerun the given calculation with a modestly changed input, preferably increasing the magnitude by ten percent while keeping all other assumptions fixed. Describe both the absolute and relative output change. This isolates sensitivity to one variable only; it is not a total uncertainty budget. If a source has correlated errors, do not combine them with independent-error root-sum-of-squares unless independence is justified. A credible interpretation explains which input is a field observation, which is a normative constant and which is a teaching assumption.

### Confounding and alternative explanation

**Frequent mistake:** Calling the geoid mean sea level everywhere hides ocean circulation and datum realization issues. A local tide gauge does not define a global equipotential surface by itself. Evaluate two plausible error models: an unmodeled common translation and independent local site motion. Both can produce coordinate differences, but only the second corresponds to differential deformation among nearby points. Construct a competing explanation and decide which new observation would discriminate between the two. Avoid evaluating success by how smooth a graphic looks. Negative controls, repeated occupations, held-out locations and cross-sensor checks can be more informative than extra decimals. Classify each candidate error as one of reference mismatch, geometry, calibration, atmospheric or environmental variability, temporal sampling or inference-model misspecification. Explain why that distinction matters for the specific conclusion being attempted.

### Applied case and decision quality

Advise a harbor engineer how to prevent a tide-derived elevation from being interpreted as ellipsoidal height. Distinguish Earth-fixed axes from the instantaneous positions of features and explain why a map’s apparent stability is partly a coordinate convention. In your written response, first state the decision being supported. Then give a physically meaningful result with units and coordinate conventions. Follow it with the strongest alternative explanation and an observation that could overturn your current interpretation. If uncertainty overlaps the stakeholder threshold, report that ambiguity rather than assigning unwarranted confidence to either choice. This discipline connects a numerical model to a traceable claim about the world.

### Guided questions and independent exercise

1. Which variables in this lesson are directly observed, and which are inferred after applying a physical model? Give the relevant units and reference conventions.
2. Recalculate the worked case after changing the controlling input by 10%; explain the direction of the resulting change and what assumption remained fixed.
3. Explain why the following pitfall matters for the current scientific claim: Calling the geoid mean sea level everywhere hides ocean circulation and datum realization issues. A local tide gauge does not define a global equipotential surface by itself.
4. Propose one independent measurement or hold-out test that could reveal a systematic error not visible in the original calculation.
5. Write a three-sentence risk statement separating the demonstrated calculation from an application it is not qualified to support.

## Lesson 1.2: Reference ellipsoid parameters

### Physical model and vocabulary

An oblate reference ellipsoid is specified by semi-major axis and flattening. Its geometry provides coordinates, local curvature and normal gravity approximations, but it is not a model of terrain. A useful physical statement explicitly identifies the quantity being observed, the idealizations needed to interpret it, and at least one phenomenon excluded by the model. Write a small equation or a structured dependency diagram before processing numbers. If two physical mechanisms can generate the same measurement, the inverse problem is not unique without a further constraint. The correct level of modeling depends on the consequence of the intended decision; an approximation acceptable in a classroom is not automatically acceptable in cadastral surveying, flood warnings or infrastructure monitoring.

### Observation design and instrumentation

Record the adopted ellipsoid, semimajor axis, flattening and units beside the survey output. Compare a spherical approximation with an ellipsoidal calculation at middle latitude. For this lesson, use the following common unit protocol as an explicit checklist: Construct two coordinate sets for the same fictional monuments. Record each station identifier, realization, reference epoch, coordinate uncertainty and possible velocity. Refuse to calculate a displacement until both position sets have been expressed at one epoch in one declared frame. Record the raw observable, its units, its collection conditions and any correction applied before deriving the displayed result. Distinguish a physically measured range, image intensity or height difference from a parameter that software estimated after applying assumptions. The same nominal output may be produced by different measurement procedures with different covariance and failure modes. Create a versioned log of those differences before comparing datasets.

### Worked numerical case 1.2: Ellipsoid flattening

**Given:** 296.4 inverse flattening. **Calculation rule:** Minor semi-axis b=a(1-f), where f=1/inverse flattening. **Computed result:** 6356.62 km. Report enough significant digits to show the underlying arithmetic, but do not claim that all displayed digits are measured information. The worked quantity is hypothetical and intentionally idealized. Recalculate it using original units rather than mentally switching between millimeters, meters, kilometers and degrees. Then double-check dimensions and evaluate whether a physically reasonable change in input produces the expected direction of change.

**Sensitivity test.** Rerun the given calculation with a modestly changed input, preferably increasing the magnitude by ten percent while keeping all other assumptions fixed. Describe both the absolute and relative output change. This isolates sensitivity to one variable only; it is not a total uncertainty budget. If a source has correlated errors, do not combine them with independent-error root-sum-of-squares unless independence is justified. A credible interpretation explains which input is a field observation, which is a normative constant and which is a teaching assumption.

### Confounding and alternative explanation

**Frequent mistake:** An ellipsoid parameter changes the coordinate map; it does not prove the Earth is composed of a uniform-density flattened shell. Evaluate two plausible error models: an unmodeled common translation and independent local site motion. Both can produce coordinate differences, but only the second corresponds to differential deformation among nearby points. Construct a competing explanation and decide which new observation would discriminate between the two. Avoid evaluating success by how smooth a graphic looks. Negative controls, repeated occupations, held-out locations and cross-sensor checks can be more informative than extra decimals. Classify each candidate error as one of reference mismatch, geometry, calibration, atmospheric or environmental variability, temporal sampling or inference-model misspecification. Explain why that distinction matters for the specific conclusion being attempted.

### Applied case and decision quality

Decide when a low-accuracy field sketch can use a sphere and when cadastral work needs rigorous geometry. Distinguish Earth-fixed axes from the instantaneous positions of features and explain why a map’s apparent stability is partly a coordinate convention. In your written response, first state the decision being supported. Then give a physically meaningful result with units and coordinate conventions. Follow it with the strongest alternative explanation and an observation that could overturn your current interpretation. If uncertainty overlaps the stakeholder threshold, report that ambiguity rather than assigning unwarranted confidence to either choice. This discipline connects a numerical model to a traceable claim about the world.

### Guided questions and independent exercise

1. Which variables in this lesson are directly observed, and which are inferred after applying a physical model? Give the relevant units and reference conventions.
2. Recalculate the worked case after changing the controlling input by 10%; explain the direction of the resulting change and what assumption remained fixed.
3. Explain why the following pitfall matters for the current scientific claim: An ellipsoid parameter changes the coordinate map; it does not prove the Earth is composed of a uniform-density flattened shell.
4. Propose one independent measurement or hold-out test that could reveal a systematic error not visible in the original calculation.
5. Write a three-sentence risk statement separating the demonstrated calculation from an application it is not qualified to support.

## Lesson 1.3: Datums, frames and realizations

### Physical model and vocabulary

An ideal reference system states conventions, while a realized frame provides estimated coordinates and velocities of actual stations. Local geodetic datums may differ from geocentric global frames by translation, rotation, scale and deformation. A useful physical statement explicitly identifies the quantity being observed, the idealizations needed to interpret it, and at least one phenomenon excluded by the model. Write a small equation or a structured dependency diagram before processing numbers. If two physical mechanisms can generate the same measurement, the inverse problem is not unique without a further constraint. The correct level of modeling depends on the consequence of the intended decision; an approximation acceptable in a classroom is not automatically acceptable in cadastral surveying, flood warnings or infrastructure monitoring.

### Observation design and instrumentation

Inspect a station coordinate file for reference-frame name, solution release, measurement epoch, antenna reference point and transformation history. Produce a provenance log. For this lesson, use the following common unit protocol as an explicit checklist: Construct two coordinate sets for the same fictional monuments. Record each station identifier, realization, reference epoch, coordinate uncertainty and possible velocity. Refuse to calculate a displacement until both position sets have been expressed at one epoch in one declared frame. Record the raw observable, its units, its collection conditions and any correction applied before deriving the displayed result. Distinguish a physically measured range, image intensity or height difference from a parameter that software estimated after applying assumptions. The same nominal output may be produced by different measurement procedures with different covariance and failure modes. Create a versioned log of those differences before comparing datasets.

### Worked numerical case 1.3: Frame translation

**Given:** 5 years. **Calculation rule:** A fixed 12 mm/year eastward velocity accumulates linearly over a hypothetical interval. **Computed result:** 60 mm. Report enough significant digits to show the underlying arithmetic, but do not claim that all displayed digits are measured information. The worked quantity is hypothetical and intentionally idealized. Recalculate it using original units rather than mentally switching between millimeters, meters, kilometers and degrees. Then double-check dimensions and evaluate whether a physically reasonable change in input produces the expected direction of change.

**Sensitivity test.** Rerun the given calculation with a modestly changed input, preferably increasing the magnitude by ten percent while keeping all other assumptions fixed. Describe both the absolute and relative output change. This isolates sensitivity to one variable only; it is not a total uncertainty budget. If a source has correlated errors, do not combine them with independent-error root-sum-of-squares unless independence is justified. A credible interpretation explains which input is a field observation, which is a normative constant and which is a teaching assumption.

### Confounding and alternative explanation

**Frequent mistake:** The words GPS coordinates are not a complete datum description, and a GIS reprojection does not automatically account for tectonic movement. Evaluate two plausible error models: an unmodeled common translation and independent local site motion. Both can produce coordinate differences, but only the second corresponds to differential deformation among nearby points. Construct a competing explanation and decide which new observation would discriminate between the two. Avoid evaluating success by how smooth a graphic looks. Negative controls, repeated occupations, held-out locations and cross-sensor checks can be more informative than extra decimals. Classify each candidate error as one of reference mismatch, geometry, calibration, atmospheric or environmental variability, temporal sampling or inference-model misspecification. Explain why that distinction matters for the specific conclusion being attempted.

### Applied case and decision quality

Prepare a coordinate-delivery contract that remains interpretable a decade after the field campaign. Distinguish Earth-fixed axes from the instantaneous positions of features and explain why a map’s apparent stability is partly a coordinate convention. In your written response, first state the decision being supported. Then give a physically meaningful result with units and coordinate conventions. Follow it with the strongest alternative explanation and an observation that could overturn your current interpretation. If uncertainty overlaps the stakeholder threshold, report that ambiguity rather than assigning unwarranted confidence to either choice. This discipline connects a numerical model to a traceable claim about the world.

### Guided questions and independent exercise

1. Which variables in this lesson are directly observed, and which are inferred after applying a physical model? Give the relevant units and reference conventions.
2. Recalculate the worked case after changing the controlling input by 10%; explain the direction of the resulting change and what assumption remained fixed.
3. Explain why the following pitfall matters for the current scientific claim: The words GPS coordinates are not a complete datum description, and a GIS reprojection does not automatically account for tectonic movement.
4. Propose one independent measurement or hold-out test that could reveal a systematic error not visible in the original calculation.
5. Write a three-sentence risk statement separating the demonstrated calculation from an application it is not qualified to support.

## Lesson 1.4: Epochs and station velocities

### Physical model and vocabulary

Positions in a global terrestrial frame change with plate motion and local deformation. A station can have coordinates at a reference epoch and a velocity vector, whereas a static point label can be misleading. A useful physical statement explicitly identifies the quantity being observed, the idealizations needed to interpret it, and at least one phenomenon excluded by the model. Write a small equation or a structured dependency diagram before processing numbers. If two physical mechanisms can generate the same measurement, the inverse problem is not unique without a further constraint. The correct level of modeling depends on the consequence of the intended decision; an approximation acceptable in a classroom is not automatically acceptable in cadastral surveying, flood warnings or infrastructure monitoring.

### Observation design and instrumentation

Plot a three-component time series and fit a line after flagging coseismic offsets and seasonal excursions. Examine sensitivity to the start and end dates. For this lesson, use the following common unit protocol as an explicit checklist: Construct two coordinate sets for the same fictional monuments. Record each station identifier, realization, reference epoch, coordinate uncertainty and possible velocity. Refuse to calculate a displacement until both position sets have been expressed at one epoch in one declared frame. Record the raw observable, its units, its collection conditions and any correction applied before deriving the displayed result. Distinguish a physically measured range, image intensity or height difference from a parameter that software estimated after applying assumptions. The same nominal output may be produced by different measurement procedures with different covariance and failure modes. Create a versioned log of those differences before comparing datasets.

### Worked numerical case 1.4: Station epoch propagation

**Given:** 8 years. **Calculation rule:** At constant velocity, displacement equals velocity multiplied by elapsed years. **Computed result:** 140 mm. Report enough significant digits to show the underlying arithmetic, but do not claim that all displayed digits are measured information. The worked quantity is hypothetical and intentionally idealized. Recalculate it using original units rather than mentally switching between millimeters, meters, kilometers and degrees. Then double-check dimensions and evaluate whether a physically reasonable change in input produces the expected direction of change.

**Sensitivity test.** Rerun the given calculation with a modestly changed input, preferably increasing the magnitude by ten percent while keeping all other assumptions fixed. Describe both the absolute and relative output change. This isolates sensitivity to one variable only; it is not a total uncertainty budget. If a source has correlated errors, do not combine them with independent-error root-sum-of-squares unless independence is justified. A credible interpretation explains which input is a field observation, which is a normative constant and which is a teaching assumption.

### Confounding and alternative explanation

**Frequent mistake:** Subtracting positions from different years without propagating them to a common epoch can manufacture an apparent survey error. Evaluate two plausible error models: an unmodeled common translation and independent local site motion. Both can produce coordinate differences, but only the second corresponds to differential deformation among nearby points. Construct a competing explanation and decide which new observation would discriminate between the two. Avoid evaluating success by how smooth a graphic looks. Negative controls, repeated occupations, held-out locations and cross-sensor checks can be more informative than extra decimals. Classify each candidate error as one of reference mismatch, geometry, calibration, atmospheric or environmental variability, temporal sampling or inference-model misspecification. Explain why that distinction matters for the specific conclusion being attempted.

### Applied case and decision quality

Assess a transboundary pipeline survey that mixes archived control with contemporary GNSS. Distinguish Earth-fixed axes from the instantaneous positions of features and explain why a map’s apparent stability is partly a coordinate convention. In your written response, first state the decision being supported. Then give a physically meaningful result with units and coordinate conventions. Follow it with the strongest alternative explanation and an observation that could overturn your current interpretation. If uncertainty overlaps the stakeholder threshold, report that ambiguity rather than assigning unwarranted confidence to either choice. This discipline connects a numerical model to a traceable claim about the world.

### Guided questions and independent exercise

1. Which variables in this lesson are directly observed, and which are inferred after applying a physical model? Give the relevant units and reference conventions.
2. Recalculate the worked case after changing the controlling input by 10%; explain the direction of the resulting change and what assumption remained fixed.
3. Explain why the following pitfall matters for the current scientific claim: Subtracting positions from different years without propagating them to a common epoch can manufacture an apparent survey error.
4. Propose one independent measurement or hold-out test that could reveal a systematic error not visible in the original calculation.
5. Write a three-sentence risk statement separating the demonstrated calculation from an application it is not qualified to support.

## Lesson 1.5: Scale, traceability and uncertainty

### Physical model and vocabulary

Geodetic products carry uncertainty from instruments, atmospheric propagation, models, reference-frame constraints and processing choices. High numeric precision is not evidence of high accuracy. A useful physical statement explicitly identifies the quantity being observed, the idealizations needed to interpret it, and at least one phenomenon excluded by the model. Write a small equation or a structured dependency diagram before processing numbers. If two physical mechanisms can generate the same measurement, the inverse problem is not unique without a further constraint. The correct level of modeling depends on the consequence of the intended decision; an approximation acceptable in a classroom is not automatically acceptable in cadastral surveying, flood warnings or infrastructure monitoring.

### Observation design and instrumentation

Read a complete adjustment report, covariance matrix and quality flags. Distinguish repeatability of coordinate estimates from accuracy relative to the declared frame. For this lesson, use the following common unit protocol as an explicit checklist: Construct two coordinate sets for the same fictional monuments. Record each station identifier, realization, reference epoch, coordinate uncertainty and possible velocity. Refuse to calculate a displacement until both position sets have been expressed at one epoch in one declared frame. Record the raw observable, its units, its collection conditions and any correction applied before deriving the displayed result. Distinguish a physically measured range, image intensity or height difference from a parameter that software estimated after applying assumptions. The same nominal output may be produced by different measurement procedures with different covariance and failure modes. Create a versioned log of those differences before comparing datasets.

### Worked numerical case 1.5: Independent uncertainty combination

**Given:** 3 mm secondary uncertainty. **Calculation rule:** Independent one-sigma components combine by root-sum-of-squares. **Computed result:** 4.38634 mm. Report enough significant digits to show the underlying arithmetic, but do not claim that all displayed digits are measured information. The worked quantity is hypothetical and intentionally idealized. Recalculate it using original units rather than mentally switching between millimeters, meters, kilometers and degrees. Then double-check dimensions and evaluate whether a physically reasonable change in input produces the expected direction of change.

**Sensitivity test.** Rerun the given calculation with a modestly changed input, preferably increasing the magnitude by ten percent while keeping all other assumptions fixed. Describe both the absolute and relative output change. This isolates sensitivity to one variable only; it is not a total uncertainty budget. If a source has correlated errors, do not combine them with independent-error root-sum-of-squares unless independence is justified. A credible interpretation explains which input is a field observation, which is a normative constant and which is a teaching assumption.

### Confounding and alternative explanation

**Frequent mistake:** A small least-squares residual may coexist with an incorrect antenna height, omitted bias or datum mismatch. Evaluate two plausible error models: an unmodeled common translation and independent local site motion. Both can produce coordinate differences, but only the second corresponds to differential deformation among nearby points. Construct a competing explanation and decide which new observation would discriminate between the two. Avoid evaluating success by how smooth a graphic looks. Negative controls, repeated occupations, held-out locations and cross-sensor checks can be more informative than extra decimals. Classify each candidate error as one of reference mismatch, geometry, calibration, atmospheric or environmental variability, temporal sampling or inference-model misspecification. Explain why that distinction matters for the specific conclusion being attempted.

### Applied case and decision quality

Specify traceable acceptance criteria for a bridge alignment that uses multiple survey teams. Distinguish Earth-fixed axes from the instantaneous positions of features and explain why a map’s apparent stability is partly a coordinate convention. In your written response, first state the decision being supported. Then give a physically meaningful result with units and coordinate conventions. Follow it with the strongest alternative explanation and an observation that could overturn your current interpretation. If uncertainty overlaps the stakeholder threshold, report that ambiguity rather than assigning unwarranted confidence to either choice. This discipline connects a numerical model to a traceable claim about the world.

### Guided questions and independent exercise

1. Which variables in this lesson are directly observed, and which are inferred after applying a physical model? Give the relevant units and reference conventions.
2. Recalculate the worked case after changing the controlling input by 10%; explain the direction of the resulting change and what assumption remained fixed.
3. Explain why the following pitfall matters for the current scientific claim: A small least-squares residual may coexist with an incorrect antenna height, omitted bias or datum mismatch.
4. Propose one independent measurement or hold-out test that could reveal a systematic error not visible in the original calculation.
5. Write a three-sentence risk statement separating the demonstrated calculation from an application it is not qualified to support.

## Unit synthesis and interpretive assessment

A fictional nationwide survey joins monument locations from different decades, including a harbor tide gauge and a mountain GNSS station. Students must reconcile reference frame, epoch, height surface, geometry and uncertainty before comparing coordinates. Develop a compact research plan with a clear inference target, observational geometry, sampling strategy, numerical cross-check and validation design. Present one figure that retains units and reference-frame metadata. Describe a case in which apparent agreement across measurements may still result from shared bias. What additional independent measurement would break that dependence?

The main theme is this: Geodesy makes an operational distinction among a physical Earth, its mathematical reference ellipsoid and a realized terrestrial reference frame. A datum name without its realization and observation epoch is often incomplete. The fundamental problem is not only finding an Earth-fixed number but making that number reproducible by another observer. Before using the unit result to guide a practical choice, ask whether the error bar reflects the true sources of uncertainty or only the variation inside a simplified numerical procedure. Define the population and period in which the conclusion is intended to hold. A consistent interpretation must remain intelligible without dependence on a proprietary figure or a hidden processing step.

