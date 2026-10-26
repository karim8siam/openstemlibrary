# Unit 2: Coordinates, Projections and Geospatial Computation

## Guiding problem

How can latitude, longitude and elevation become reliable distances, maps and engineering coordinates?

**Fictional investigation:** A fictitious regional mapping project compares coastal GNSS control, an engineering grid, and a global satellite scene. Each product uses different coordinates, while ground distances and areas must agree within survey tolerance.

## Scientific scope

Coordinates are not distances. All physical interpretation depends on coordinate definitions, map distortion, units and the sequence of transformations. The projected result may appear precise while still being displaced if input datums or axis order are misunderstood. Whenever positions, ranges, elevations or images are compared, uncertainty must be attached to a specified measurand and an explicitly identified reference. The word accurate is incomplete unless the reader can state accurate relative to what, over which interval and for which population of conditions. A local fit may be adequate for instruction without being an operationally defensible geodetic product.

## Unit practical: Spatial coordinate audit

Assemble a miniature transformation ledger from longitude and latitude through a local east-north-up frame to a chosen map projection. Include sign conventions, length units, projection scale and any approximation to Earth curvature.

Repeat one inverse transform and compare with the original input. A round trip close to zero demonstrates computational consistency, but a shared wrong datum can still survive that test.

Compare local distortion with the decision threshold instead of treating all projections as equivalent.

## Data notebook requirements

Create a plain-text notebook containing input columns, units, a source/provenance statement, treatment of missing records, computational steps and at least one independent check. All datasets in this unit are manufactured for learning rather than sampled from nature. When reporting an estimated number, write out the assumptions connecting the number with the claimed physical variable. Note whether uncertainty is random, systematic or model-based. Provide a short explanation of what the number *cannot* tell us. The purpose is to practice disciplined geodetic reasoning as well as numerical computation.

## Lesson 2.1: Geodetic latitude, longitude and height

### Physical model and vocabulary

Geodetic latitude is defined with respect to the ellipsoid normal rather than the geocentric radius; the distinction matters in rigorous conversions. Ellipsoidal height is measured along that normal. A useful physical statement explicitly identifies the quantity being observed, the idealizations needed to interpret it, and at least one phenomenon excluded by the model. Write a small equation or a structured dependency diagram before processing numbers. If two physical mechanisms can generate the same measurement, the inverse problem is not unique without a further constraint. The correct level of modeling depends on the consequence of the intended decision; an approximation acceptable in a classroom is not automatically acceptable in cadastral surveying, flood warnings or infrastructure monitoring.

### Observation design and instrumentation

Convert a test station from geodetic latitude, longitude and ellipsoid height to Earth-centered Cartesian coordinates and back; retain enough digits to detect rounding error. For this lesson, use the following common unit protocol as an explicit checklist: Assemble a miniature transformation ledger from longitude and latitude through a local east-north-up frame to a chosen map projection. Include sign conventions, length units, projection scale and any approximation to Earth curvature. Record the raw observable, its units, its collection conditions and any correction applied before deriving the displayed result. Distinguish a physically measured range, image intensity or height difference from a parameter that software estimated after applying assumptions. The same nominal output may be produced by different measurement procedures with different covariance and failure modes. Create a versioned log of those differences before comparing datasets.

### Worked numerical case 2.1: Approximate east displacement

**Given:** 0.02 degrees longitude. **Calculation rule:** Multiply longitude difference in degrees by nominal distance per degree and cosine latitude. **Computed result:** 2.01554 km. Report enough significant digits to show the underlying arithmetic, but do not claim that all displayed digits are measured information. The worked quantity is hypothetical and intentionally idealized. Recalculate it using original units rather than mentally switching between millimeters, meters, kilometers and degrees. Then double-check dimensions and evaluate whether a physically reasonable change in input produces the expected direction of change.

**Sensitivity test.** Rerun the given calculation with a modestly changed input, preferably increasing the magnitude by ten percent while keeping all other assumptions fixed. Describe both the absolute and relative output change. This isolates sensitivity to one variable only; it is not a total uncertainty budget. If a source has correlated errors, do not combine them with independent-error root-sum-of-squares unless independence is justified. A credible interpretation explains which input is a field observation, which is a normative constant and which is a teaching assumption.

### Confounding and alternative explanation

**Frequent mistake:** Applying spherical trigonometry to ellipsoidal positions may be suitable for rough distances but not precise network coordinate transfer. Repeat one inverse transform and compare with the original input. A round trip close to zero demonstrates computational consistency, but a shared wrong datum can still survive that test. Construct a competing explanation and decide which new observation would discriminate between the two. Avoid evaluating success by how smooth a graphic looks. Negative controls, repeated occupations, held-out locations and cross-sensor checks can be more informative than extra decimals. Classify each candidate error as one of reference mismatch, geometry, calibration, atmospheric or environmental variability, temporal sampling or inference-model misspecification. Explain why that distinction matters for the specific conclusion being attempted.

### Applied case and decision quality

Write a coordinate interchange note with axis order, angular units, ellipsoid identifier and sign convention. Compare local distortion with the decision threshold instead of treating all projections as equivalent. In your written response, first state the decision being supported. Then give a physically meaningful result with units and coordinate conventions. Follow it with the strongest alternative explanation and an observation that could overturn your current interpretation. If uncertainty overlaps the stakeholder threshold, report that ambiguity rather than assigning unwarranted confidence to either choice. This discipline connects a numerical model to a traceable claim about the world.

### Guided questions and independent exercise

1. Which variables in this lesson are directly observed, and which are inferred after applying a physical model? Give the relevant units and reference conventions.
2. Recalculate the worked case after changing the controlling input by 10%; explain the direction of the resulting change and what assumption remained fixed.
3. Explain why the following pitfall matters for the current scientific claim: Applying spherical trigonometry to ellipsoidal positions may be suitable for rough distances but not precise network coordinate transfer.
4. Propose one independent measurement or hold-out test that could reveal a systematic error not visible in the original calculation.
5. Write a three-sentence risk statement separating the demonstrated calculation from an application it is not qualified to support.

## Lesson 2.2: ECEF Cartesian coordinates

### Physical model and vocabulary

Earth-centered Earth-fixed coordinates use three Cartesian components referred to an origin, orientation and scale. The components must be tied to a reference frame and epoch; otherwise they cannot be compared across campaigns. A useful physical statement explicitly identifies the quantity being observed, the idealizations needed to interpret it, and at least one phenomenon excluded by the model. Write a small equation or a structured dependency diagram before processing numbers. If two physical mechanisms can generate the same measurement, the inverse problem is not unique without a further constraint. The correct level of modeling depends on the consequence of the intended decision; an approximation acceptable in a classroom is not automatically acceptable in cadastral surveying, flood warnings or infrastructure monitoring.

### Observation design and instrumentation

Take two synthetic neighboring stations, compute their ECEF difference vector, then rotate into a local east-north-up basis for engineering interpretation. For this lesson, use the following common unit protocol as an explicit checklist: Assemble a miniature transformation ledger from longitude and latitude through a local east-north-up frame to a chosen map projection. Include sign conventions, length units, projection scale and any approximation to Earth curvature. Record the raw observable, its units, its collection conditions and any correction applied before deriving the displayed result. Distinguish a physically measured range, image intensity or height difference from a parameter that software estimated after applying assumptions. The same nominal output may be produced by different measurement procedures with different covariance and failure modes. Create a versioned log of those differences before comparing datasets.

### Worked numerical case 2.2: North displacement

**Given:** 0.06 degrees latitude. **Calculation rule:** An approximate spherical north distance uses 111.195 km per degree latitude. **Computed result:** 6.6717 km. Report enough significant digits to show the underlying arithmetic, but do not claim that all displayed digits are measured information. The worked quantity is hypothetical and intentionally idealized. Recalculate it using original units rather than mentally switching between millimeters, meters, kilometers and degrees. Then double-check dimensions and evaluate whether a physically reasonable change in input produces the expected direction of change.

**Sensitivity test.** Rerun the given calculation with a modestly changed input, preferably increasing the magnitude by ten percent while keeping all other assumptions fixed. Describe both the absolute and relative output change. This isolates sensitivity to one variable only; it is not a total uncertainty budget. If a source has correlated errors, do not combine them with independent-error root-sum-of-squares unless independence is justified. A credible interpretation explains which input is a field observation, which is a normative constant and which is a teaching assumption.

### Confounding and alternative explanation

**Frequent mistake:** ECEF X, Y and Z are not projected eastings and northings and should not be read as local displacement directions. Repeat one inverse transform and compare with the original input. A round trip close to zero demonstrates computational consistency, but a shared wrong datum can still survive that test. Construct a competing explanation and decide which new observation would discriminate between the two. Avoid evaluating success by how smooth a graphic looks. Negative controls, repeated occupations, held-out locations and cross-sensor checks can be more informative than extra decimals. Classify each candidate error as one of reference mismatch, geometry, calibration, atmospheric or environmental variability, temporal sampling or inference-model misspecification. Explain why that distinction matters for the specific conclusion being attempted.

### Applied case and decision quality

Design a handoff from a GNSS processing package to a structural-monitoring engineer. Compare local distortion with the decision threshold instead of treating all projections as equivalent. In your written response, first state the decision being supported. Then give a physically meaningful result with units and coordinate conventions. Follow it with the strongest alternative explanation and an observation that could overturn your current interpretation. If uncertainty overlaps the stakeholder threshold, report that ambiguity rather than assigning unwarranted confidence to either choice. This discipline connects a numerical model to a traceable claim about the world.

### Guided questions and independent exercise

1. Which variables in this lesson are directly observed, and which are inferred after applying a physical model? Give the relevant units and reference conventions.
2. Recalculate the worked case after changing the controlling input by 10%; explain the direction of the resulting change and what assumption remained fixed.
3. Explain why the following pitfall matters for the current scientific claim: ECEF X, Y and Z are not projected eastings and northings and should not be read as local displacement directions.
4. Propose one independent measurement or hold-out test that could reveal a systematic error not visible in the original calculation.
5. Write a three-sentence risk statement separating the demonstrated calculation from an application it is not qualified to support.

## Lesson 2.3: Local tangent-plane navigation

### Physical model and vocabulary

The local east-north-up frame expresses short baselines in familiar directions. The rotation depends on reference latitude and longitude, and the approximation must be tested for long transects. A useful physical statement explicitly identifies the quantity being observed, the idealizations needed to interpret it, and at least one phenomenon excluded by the model. Write a small equation or a structured dependency diagram before processing numbers. If two physical mechanisms can generate the same measurement, the inverse problem is not unique without a further constraint. The correct level of modeling depends on the consequence of the intended decision; an approximation acceptable in a classroom is not automatically acceptable in cadastral surveying, flood warnings or infrastructure monitoring.

### Observation design and instrumentation

Generate short synthetic baseline vectors and compare the local-tangent approximation with full geodetic endpoints as distance grows. For this lesson, use the following common unit protocol as an explicit checklist: Assemble a miniature transformation ledger from longitude and latitude through a local east-north-up frame to a chosen map projection. Include sign conventions, length units, projection scale and any approximation to Earth curvature. Record the raw observable, its units, its collection conditions and any correction applied before deriving the displayed result. Distinguish a physically measured range, image intensity or height difference from a parameter that software estimated after applying assumptions. The same nominal output may be produced by different measurement procedures with different covariance and failure modes. Create a versioned log of those differences before comparing datasets.

### Worked numerical case 2.3: Coordinate scale factor

**Given:** 650 m grid distance. **Calculation rule:** The approximate ground distance is grid distance divided by a fixed map scale factor. **Computed result:** 650.26 m ground distance. Report enough significant digits to show the underlying arithmetic, but do not claim that all displayed digits are measured information. The worked quantity is hypothetical and intentionally idealized. Recalculate it using original units rather than mentally switching between millimeters, meters, kilometers and degrees. Then double-check dimensions and evaluate whether a physically reasonable change in input produces the expected direction of change.

**Sensitivity test.** Rerun the given calculation with a modestly changed input, preferably increasing the magnitude by ten percent while keeping all other assumptions fixed. Describe both the absolute and relative output change. This isolates sensitivity to one variable only; it is not a total uncertainty budget. If a source has correlated errors, do not combine them with independent-error root-sum-of-squares unless independence is justified. A credible interpretation explains which input is a field observation, which is a normative constant and which is a teaching assumption.

### Confounding and alternative explanation

**Frequent mistake:** A convenient local plane is not flat-Earth evidence, and coordinate curvature becomes important for sufficiently extended networks. Repeat one inverse transform and compare with the original input. A round trip close to zero demonstrates computational consistency, but a shared wrong datum can still survive that test. Construct a competing explanation and decide which new observation would discriminate between the two. Avoid evaluating success by how smooth a graphic looks. Negative controls, repeated occupations, held-out locations and cross-sensor checks can be more informative than extra decimals. Classify each candidate error as one of reference mismatch, geometry, calibration, atmospheric or environmental variability, temporal sampling or inference-model misspecification. Explain why that distinction matters for the specific conclusion being attempted.

### Applied case and decision quality

Select a coordinate system for an airport runway survey, stating its length-scale validity. Compare local distortion with the decision threshold instead of treating all projections as equivalent. In your written response, first state the decision being supported. Then give a physically meaningful result with units and coordinate conventions. Follow it with the strongest alternative explanation and an observation that could overturn your current interpretation. If uncertainty overlaps the stakeholder threshold, report that ambiguity rather than assigning unwarranted confidence to either choice. This discipline connects a numerical model to a traceable claim about the world.

### Guided questions and independent exercise

1. Which variables in this lesson are directly observed, and which are inferred after applying a physical model? Give the relevant units and reference conventions.
2. Recalculate the worked case after changing the controlling input by 10%; explain the direction of the resulting change and what assumption remained fixed.
3. Explain why the following pitfall matters for the current scientific claim: A convenient local plane is not flat-Earth evidence, and coordinate curvature becomes important for sufficiently extended networks.
4. Propose one independent measurement or hold-out test that could reveal a systematic error not visible in the original calculation.
5. Write a three-sentence risk statement separating the demonstrated calculation from an application it is not qualified to support.

## Lesson 2.4: Map projections and distortion

### Physical model and vocabulary

Flattening a curved surface requires distortion in shape, area, distance or direction. Projection choice is a measurement design decision, not merely a cartographic style preference. A useful physical statement explicitly identifies the quantity being observed, the idealizations needed to interpret it, and at least one phenomenon excluded by the model. Write a small equation or a structured dependency diagram before processing numbers. If two physical mechanisms can generate the same measurement, the inverse problem is not unique without a further constraint. The correct level of modeling depends on the consequence of the intended decision; an approximation acceptable in a classroom is not automatically acceptable in cadastral surveying, flood warnings or infrastructure monitoring.

### Observation design and instrumentation

Evaluate scale factors along a synthetic corridor in two candidate projections; quantify accumulated distance error from ignoring the scale factor. For this lesson, use the following common unit protocol as an explicit checklist: Assemble a miniature transformation ledger from longitude and latitude through a local east-north-up frame to a chosen map projection. Include sign conventions, length units, projection scale and any approximation to Earth curvature. Record the raw observable, its units, its collection conditions and any correction applied before deriving the displayed result. Distinguish a physically measured range, image intensity or height difference from a parameter that software estimated after applying assumptions. The same nominal output may be produced by different measurement procedures with different covariance and failure modes. Create a versioned log of those differences before comparing datasets.

### Worked numerical case 2.4: Height-related grid correction

**Given:** 650 m ground distance. **Calculation rule:** A fixed map scale multiplies a ground distance to produce approximate grid distance. **Computed result:** 649.74 m grid distance. Report enough significant digits to show the underlying arithmetic, but do not claim that all displayed digits are measured information. The worked quantity is hypothetical and intentionally idealized. Recalculate it using original units rather than mentally switching between millimeters, meters, kilometers and degrees. Then double-check dimensions and evaluate whether a physically reasonable change in input produces the expected direction of change.

**Sensitivity test.** Rerun the given calculation with a modestly changed input, preferably increasing the magnitude by ten percent while keeping all other assumptions fixed. Describe both the absolute and relative output change. This isolates sensitivity to one variable only; it is not a total uncertainty budget. If a source has correlated errors, do not combine them with independent-error root-sum-of-squares unless independence is justified. A credible interpretation explains which input is a field observation, which is a normative constant and which is a teaching assumption.

### Confounding and alternative explanation

**Frequent mistake:** Universal Transverse Mercator coordinates are not automatically ground distances and UTM zones should not be silently mixed. Repeat one inverse transform and compare with the original input. A round trip close to zero demonstrates computational consistency, but a shared wrong datum can still survive that test. Construct a competing explanation and decide which new observation would discriminate between the two. Avoid evaluating success by how smooth a graphic looks. Negative controls, repeated occupations, held-out locations and cross-sensor checks can be more informative than extra decimals. Classify each candidate error as one of reference mismatch, geometry, calibration, atmospheric or environmental variability, temporal sampling or inference-model misspecification. Explain why that distinction matters for the specific conclusion being attempted.

### Applied case and decision quality

Recommend a mapping projection for a long east-west river basin while reporting the residual distortion. Compare local distortion with the decision threshold instead of treating all projections as equivalent. In your written response, first state the decision being supported. Then give a physically meaningful result with units and coordinate conventions. Follow it with the strongest alternative explanation and an observation that could overturn your current interpretation. If uncertainty overlaps the stakeholder threshold, report that ambiguity rather than assigning unwarranted confidence to either choice. This discipline connects a numerical model to a traceable claim about the world.

### Guided questions and independent exercise

1. Which variables in this lesson are directly observed, and which are inferred after applying a physical model? Give the relevant units and reference conventions.
2. Recalculate the worked case after changing the controlling input by 10%; explain the direction of the resulting change and what assumption remained fixed.
3. Explain why the following pitfall matters for the current scientific claim: Universal Transverse Mercator coordinates are not automatically ground distances and UTM zones should not be silently mixed.
4. Propose one independent measurement or hold-out test that could reveal a systematic error not visible in the original calculation.
5. Write a three-sentence risk statement separating the demonstrated calculation from an application it is not qualified to support.

## Lesson 2.5: Transformation pipelines and QA

### Physical model and vocabulary

Coordinate transformation may involve datum shifts, time-dependent velocities, geographic transforms, map projection and height conversion. Their order and definitions determine the result. A useful physical statement explicitly identifies the quantity being observed, the idealizations needed to interpret it, and at least one phenomenon excluded by the model. Write a small equation or a structured dependency diagram before processing numbers. If two physical mechanisms can generate the same measurement, the inverse problem is not unique without a further constraint. The correct level of modeling depends on the consequence of the intended decision; an approximation acceptable in a classroom is not automatically acceptable in cadastral surveying, flood warnings or infrastructure monitoring.

### Observation design and instrumentation

Build a reproducible pipeline from raw control metadata to final engineering output. Include round-trip tests, known check points, axis-order checks and an uncertainty budget. For this lesson, use the following common unit protocol as an explicit checklist: Assemble a miniature transformation ledger from longitude and latitude through a local east-north-up frame to a chosen map projection. Include sign conventions, length units, projection scale and any approximation to Earth curvature. Record the raw observable, its units, its collection conditions and any correction applied before deriving the displayed result. Distinguish a physically measured range, image intensity or height difference from a parameter that software estimated after applying assumptions. The same nominal output may be produced by different measurement procedures with different covariance and failure modes. Create a versioned log of those differences before comparing datasets.

### Worked numerical case 2.5: Planimetric check RMSE

**Given:** 0.8 m last checkpoint residual. **Calculation rule:** Root mean square uses four independent held-out check-point residual magnitudes. **Computed result:** 0.504975 m. Report enough significant digits to show the underlying arithmetic, but do not claim that all displayed digits are measured information. The worked quantity is hypothetical and intentionally idealized. Recalculate it using original units rather than mentally switching between millimeters, meters, kilometers and degrees. Then double-check dimensions and evaluate whether a physically reasonable change in input produces the expected direction of change.

**Sensitivity test.** Rerun the given calculation with a modestly changed input, preferably increasing the magnitude by ten percent while keeping all other assumptions fixed. Describe both the absolute and relative output change. This isolates sensitivity to one variable only; it is not a total uncertainty budget. If a source has correlated errors, do not combine them with independent-error root-sum-of-squares unless independence is justified. A credible interpretation explains which input is a field observation, which is a normative constant and which is a teaching assumption.

### Confounding and alternative explanation

**Frequent mistake:** A successful software execution or visual overlap on a basemap does not establish that the coordinates share the same geodetic realization. Repeat one inverse transform and compare with the original input. A round trip close to zero demonstrates computational consistency, but a shared wrong datum can still survive that test. Construct a competing explanation and decide which new observation would discriminate between the two. Avoid evaluating success by how smooth a graphic looks. Negative controls, repeated occupations, held-out locations and cross-sensor checks can be more informative than extra decimals. Classify each candidate error as one of reference mismatch, geometry, calibration, atmospheric or environmental variability, temporal sampling or inference-model misspecification. Explain why that distinction matters for the specific conclusion being attempted.

### Applied case and decision quality

Audit a contractor file that uses unlabeled EPSG numbers and no frame epoch. Compare local distortion with the decision threshold instead of treating all projections as equivalent. In your written response, first state the decision being supported. Then give a physically meaningful result with units and coordinate conventions. Follow it with the strongest alternative explanation and an observation that could overturn your current interpretation. If uncertainty overlaps the stakeholder threshold, report that ambiguity rather than assigning unwarranted confidence to either choice. This discipline connects a numerical model to a traceable claim about the world.

### Guided questions and independent exercise

1. Which variables in this lesson are directly observed, and which are inferred after applying a physical model? Give the relevant units and reference conventions.
2. Recalculate the worked case after changing the controlling input by 10%; explain the direction of the resulting change and what assumption remained fixed.
3. Explain why the following pitfall matters for the current scientific claim: A successful software execution or visual overlap on a basemap does not establish that the coordinates share the same geodetic realization.
4. Propose one independent measurement or hold-out test that could reveal a systematic error not visible in the original calculation.
5. Write a three-sentence risk statement separating the demonstrated calculation from an application it is not qualified to support.

## Unit synthesis and interpretive assessment

A fictitious regional mapping project compares coastal GNSS control, an engineering grid, and a global satellite scene. Each product uses different coordinates, while ground distances and areas must agree within survey tolerance. Develop a compact research plan with a clear inference target, observational geometry, sampling strategy, numerical cross-check and validation design. Present one figure that retains units and reference-frame metadata. Describe a case in which apparent agreement across measurements may still result from shared bias. What additional independent measurement would break that dependence?

The main theme is this: Coordinates are not distances. All physical interpretation depends on coordinate definitions, map distortion, units and the sequence of transformations. The projected result may appear precise while still being displaced if input datums or axis order are misunderstood. Before using the unit result to guide a practical choice, ask whether the error bar reflects the true sources of uncertainty or only the variation inside a simplified numerical procedure. Define the population and period in which the conclusion is intended to hold. A consistent interpretation must remain intelligible without dependence on a proprietary figure or a hidden processing step.

