# Unit 5: Deformation, Reference Frames and Earth Dynamics

## Guiding problem

How can repeated position estimates reveal tectonic motion while avoiding false deformation?

**Fictional investigation:** A fictional active margin has GNSS stations, an earthquake displacement step, seasonal loading, and an InSAR satellite track. Learners test whether a reported displacement is tectonic, hydrological, instrumental or reference-frame driven.

## Scientific scope

Deformation monitoring is fundamentally a time-series inference problem. Observations must be registered to consistent coordinates and separated into continuous motion, discrete offsets, periodic effects and uncertainty. Whenever positions, ranges, elevations or images are compared, uncertainty must be attached to a specified measurand and an explicitly identified reference. The word accurate is incomplete unless the reader can state accurate relative to what, over which interval and for which population of conditions. A local fit may be adequate for instruction without being an operationally defensible geodetic product.

## Unit practical: Time-series decomposition

Model position as a linear trend plus seasonal terms, discrete offsets and residual noise. Flag changed receivers, storms and seismic events. Fit both a minimal and an expanded model using held-out time intervals.

Compare the resulting velocity and its uncertainty. If an apparent acceleration disappears after adding a station jump, avoid describing it as new tectonic activity.

Use residual diagnostic plots and document sensitivity to missing observations and autocorrelation.

## Data notebook requirements

Create a plain-text notebook containing input columns, units, a source/provenance statement, treatment of missing records, computational steps and at least one independent check. All datasets in this unit are manufactured for learning rather than sampled from nature. When reporting an estimated number, write out the assumptions connecting the number with the claimed physical variable. Note whether uncertainty is random, systematic or model-based. Provide a short explanation of what the number *cannot* tell us. The purpose is to practice disciplined geodetic reasoning as well as numerical computation.

## Lesson 5.1: Crustal motion and plate velocities

### Physical model and vocabulary

Long-term horizontal station velocities reflect plate motion plus local deformation. The fitted trend depends on the reference frame, velocity model and interruptions in the record. A useful physical statement explicitly identifies the quantity being observed, the idealizations needed to interpret it, and at least one phenomenon excluded by the model. Write a small equation or a structured dependency diagram before processing numbers. If two physical mechanisms can generate the same measurement, the inverse problem is not unique without a further constraint. The correct level of modeling depends on the consequence of the intended decision; an approximation acceptable in a classroom is not automatically acceptable in cadastral surveying, flood warnings or infrastructure monitoring.

### Observation design and instrumentation

Fit a synthetic northing time series over several years and compare a linear-only model with one including annual cycles. Propagate an omitted earthquake offset through the trend. For this lesson, use the following common unit protocol as an explicit checklist: Model position as a linear trend plus seasonal terms, discrete offsets and residual noise. Flag changed receivers, storms and seismic events. Fit both a minimal and an expanded model using held-out time intervals. Record the raw observable, its units, its collection conditions and any correction applied before deriving the displayed result. Distinguish a physically measured range, image intensity or height difference from a parameter that software estimated after applying assumptions. The same nominal output may be produced by different measurement procedures with different covariance and failure modes. Create a versioned log of those differences before comparing datasets.

### Worked numerical case 5.1: Plate motion prediction

**Given:** 7 years. **Calculation rule:** Assume a constant 8 mm/year velocity and multiply by years. **Computed result:** 56 mm. Report enough significant digits to show the underlying arithmetic, but do not claim that all displayed digits are measured information. The worked quantity is hypothetical and intentionally idealized. Recalculate it using original units rather than mentally switching between millimeters, meters, kilometers and degrees. Then double-check dimensions and evaluate whether a physically reasonable change in input produces the expected direction of change.

**Sensitivity test.** Rerun the given calculation with a modestly changed input, preferably increasing the magnitude by ten percent while keeping all other assumptions fixed. Describe both the absolute and relative output change. This isolates sensitivity to one variable only; it is not a total uncertainty budget. If a source has correlated errors, do not combine them with independent-error root-sum-of-squares unless independence is justified. A credible interpretation explains which input is a field observation, which is a normative constant and which is a teaching assumption.

### Confounding and alternative explanation

**Frequent mistake:** A long-term average velocity should not be mistaken for instantaneous slip on a nearby fault or a short-term deterministic forecast. Compare the resulting velocity and its uncertainty. If an apparent acceleration disappears after adding a station jump, avoid describing it as new tectonic activity. Construct a competing explanation and decide which new observation would discriminate between the two. Avoid evaluating success by how smooth a graphic looks. Negative controls, repeated occupations, held-out locations and cross-sensor checks can be more informative than extra decimals. Classify each candidate error as one of reference mismatch, geometry, calibration, atmospheric or environmental variability, temporal sampling or inference-model misspecification. Explain why that distinction matters for the specific conclusion being attempted.

### Applied case and decision quality

Prepare a regional map caption that states frame, velocity interval, uncertainties and exclusions. Use residual diagnostic plots and document sensitivity to missing observations and autocorrelation. In your written response, first state the decision being supported. Then give a physically meaningful result with units and coordinate conventions. Follow it with the strongest alternative explanation and an observation that could overturn your current interpretation. If uncertainty overlaps the stakeholder threshold, report that ambiguity rather than assigning unwarranted confidence to either choice. This discipline connects a numerical model to a traceable claim about the world.

### Guided questions and independent exercise

1. Which variables in this lesson are directly observed, and which are inferred after applying a physical model? Give the relevant units and reference conventions.
2. Recalculate the worked case after changing the controlling input by 10%; explain the direction of the resulting change and what assumption remained fixed.
3. Explain why the following pitfall matters for the current scientific claim: A long-term average velocity should not be mistaken for instantaneous slip on a nearby fault or a short-term deterministic forecast.
4. Propose one independent measurement or hold-out test that could reveal a systematic error not visible in the original calculation.
5. Write a three-sentence risk statement separating the demonstrated calculation from an application it is not qualified to support.

## Lesson 5.2: Strain from station networks

### Physical model and vocabulary

Strain quantifies relative deformation, and baseline-length change divided by length is an elementary one-dimensional measure. Networks in two dimensions require an appropriate deformation gradient model. A useful physical statement explicitly identifies the quantity being observed, the idealizations needed to interpret it, and at least one phenomenon excluded by the model. Write a small equation or a structured dependency diagram before processing numbers. If two physical mechanisms can generate the same measurement, the inverse problem is not unique without a further constraint. The correct level of modeling depends on the consequence of the intended decision; an approximation acceptable in a classroom is not automatically acceptable in cadastral surveying, flood warnings or infrastructure monitoring.

### Observation design and instrumentation

Estimate extension in a fictional geodetic baseline and compare millimeter signals against independently estimated measurement noise. For this lesson, use the following common unit protocol as an explicit checklist: Model position as a linear trend plus seasonal terms, discrete offsets and residual noise. Flag changed receivers, storms and seismic events. Fit both a minimal and an expanded model using held-out time intervals. Record the raw observable, its units, its collection conditions and any correction applied before deriving the displayed result. Distinguish a physically measured range, image intensity or height difference from a parameter that software estimated after applying assumptions. The same nominal output may be produced by different measurement procedures with different covariance and failure modes. Create a versioned log of those differences before comparing datasets.

### Worked numerical case 5.2: Baseline strain

**Given:** 8 mm baseline extension. **Calculation rule:** Engineering strain is length change divided by a fixed 5 km baseline. **Computed result:** 1.6e-06 strain. Report enough significant digits to show the underlying arithmetic, but do not claim that all displayed digits are measured information. The worked quantity is hypothetical and intentionally idealized. Recalculate it using original units rather than mentally switching between millimeters, meters, kilometers and degrees. Then double-check dimensions and evaluate whether a physically reasonable change in input produces the expected direction of change.

**Sensitivity test.** Rerun the given calculation with a modestly changed input, preferably increasing the magnitude by ten percent while keeping all other assumptions fixed. Describe both the absolute and relative output change. This isolates sensitivity to one variable only; it is not a total uncertainty budget. If a source has correlated errors, do not combine them with independent-error root-sum-of-squares unless independence is justified. A credible interpretation explains which input is a field observation, which is a normative constant and which is a teaching assumption.

### Confounding and alternative explanation

**Frequent mistake:** A change in absolute coordinates can arise from translation alone; it is not sufficient evidence of internal strain. Compare the resulting velocity and its uncertainty. If an apparent acceleration disappears after adding a station jump, avoid describing it as new tectonic activity. Construct a competing explanation and decide which new observation would discriminate between the two. Avoid evaluating success by how smooth a graphic looks. Negative controls, repeated occupations, held-out locations and cross-sensor checks can be more informative than extra decimals. Classify each candidate error as one of reference mismatch, geometry, calibration, atmospheric or environmental variability, temporal sampling or inference-model misspecification. Explain why that distinction matters for the specific conclusion being attempted.

### Applied case and decision quality

Decide where to place additional stations to constrain a fault-perpendicular strain field. Use residual diagnostic plots and document sensitivity to missing observations and autocorrelation. In your written response, first state the decision being supported. Then give a physically meaningful result with units and coordinate conventions. Follow it with the strongest alternative explanation and an observation that could overturn your current interpretation. If uncertainty overlaps the stakeholder threshold, report that ambiguity rather than assigning unwarranted confidence to either choice. This discipline connects a numerical model to a traceable claim about the world.

### Guided questions and independent exercise

1. Which variables in this lesson are directly observed, and which are inferred after applying a physical model? Give the relevant units and reference conventions.
2. Recalculate the worked case after changing the controlling input by 10%; explain the direction of the resulting change and what assumption remained fixed.
3. Explain why the following pitfall matters for the current scientific claim: A change in absolute coordinates can arise from translation alone; it is not sufficient evidence of internal strain.
4. Propose one independent measurement or hold-out test that could reveal a systematic error not visible in the original calculation.
5. Write a three-sentence risk statement separating the demonstrated calculation from an application it is not qualified to support.

## Lesson 5.3: Coseismic and postseismic change

### Physical model and vocabulary

Earthquakes may cause permanent offsets, followed by evolving afterslip, viscoelastic relaxation or other transient responses. Data gaps and reference-frame breaks can masquerade as physical steps. A useful physical statement explicitly identifies the quantity being observed, the idealizations needed to interpret it, and at least one phenomenon excluded by the model. Write a small equation or a structured dependency diagram before processing numbers. If two physical mechanisms can generate the same measurement, the inverse problem is not unique without a further constraint. The correct level of modeling depends on the consequence of the intended decision; an approximation acceptable in a classroom is not automatically acceptable in cadastral surveying, flood warnings or infrastructure monitoring.

### Observation design and instrumentation

Fit a synthetic time series with a step plus a simple decay, then compare held-out residuals against a linear-only interpretation. For this lesson, use the following common unit protocol as an explicit checklist: Model position as a linear trend plus seasonal terms, discrete offsets and residual noise. Flag changed receivers, storms and seismic events. Fit both a minimal and an expanded model using held-out time intervals. Record the raw observable, its units, its collection conditions and any correction applied before deriving the displayed result. Distinguish a physically measured range, image intensity or height difference from a parameter that software estimated after applying assumptions. The same nominal output may be produced by different measurement procedures with different covariance and failure modes. Create a versioned log of those differences before comparing datasets.

### Worked numerical case 5.3: Coseismic step amplitude

**Given:** 20 mm step. **Calculation rule:** Convert a modeled permanent station offset from millimeters to centimeters. **Computed result:** 2 cm. Report enough significant digits to show the underlying arithmetic, but do not claim that all displayed digits are measured information. The worked quantity is hypothetical and intentionally idealized. Recalculate it using original units rather than mentally switching between millimeters, meters, kilometers and degrees. Then double-check dimensions and evaluate whether a physically reasonable change in input produces the expected direction of change.

**Sensitivity test.** Rerun the given calculation with a modestly changed input, preferably increasing the magnitude by ten percent while keeping all other assumptions fixed. Describe both the absolute and relative output change. This isolates sensitivity to one variable only; it is not a total uncertainty budget. If a source has correlated errors, do not combine them with independent-error root-sum-of-squares unless independence is justified. A credible interpretation explains which input is a field observation, which is a normative constant and which is a teaching assumption.

### Confounding and alternative explanation

**Frequent mistake:** The quality of a curve fit does not uniquely identify the underlying mechanism; physical inferences require independent geologic and seismic evidence. Compare the resulting velocity and its uncertainty. If an apparent acceleration disappears after adding a station jump, avoid describing it as new tectonic activity. Construct a competing explanation and decide which new observation would discriminate between the two. Avoid evaluating success by how smooth a graphic looks. Negative controls, repeated occupations, held-out locations and cross-sensor checks can be more informative than extra decimals. Classify each candidate error as one of reference mismatch, geometry, calibration, atmospheric or environmental variability, temporal sampling or inference-model misspecification. Explain why that distinction matters for the specific conclusion being attempted.

### Applied case and decision quality

Draft a technical monitoring report that distinguishes measured displacement from cause assignment. Use residual diagnostic plots and document sensitivity to missing observations and autocorrelation. In your written response, first state the decision being supported. Then give a physically meaningful result with units and coordinate conventions. Follow it with the strongest alternative explanation and an observation that could overturn your current interpretation. If uncertainty overlaps the stakeholder threshold, report that ambiguity rather than assigning unwarranted confidence to either choice. This discipline connects a numerical model to a traceable claim about the world.

### Guided questions and independent exercise

1. Which variables in this lesson are directly observed, and which are inferred after applying a physical model? Give the relevant units and reference conventions.
2. Recalculate the worked case after changing the controlling input by 10%; explain the direction of the resulting change and what assumption remained fixed.
3. Explain why the following pitfall matters for the current scientific claim: The quality of a curve fit does not uniquely identify the underlying mechanism; physical inferences require independent geologic and seismic evidence.
4. Propose one independent measurement or hold-out test that could reveal a systematic error not visible in the original calculation.
5. Write a three-sentence risk statement separating the demonstrated calculation from an application it is not qualified to support.

## Lesson 5.4: InSAR line-of-sight displacement

### Physical model and vocabulary

Radar interferometry measures phase change related primarily to displacement projected into the radar line of sight, after atmospheric, topographic and orbital corrections. A useful physical statement explicitly identifies the quantity being observed, the idealizations needed to interpret it, and at least one phenomenon excluded by the model. Write a small equation or a structured dependency diagram before processing numbers. If two physical mechanisms can generate the same measurement, the inverse problem is not unique without a further constraint. The correct level of modeling depends on the consequence of the intended decision; an approximation acceptable in a classroom is not automatically acceptable in cadastral surveying, flood warnings or infrastructure monitoring.

### Observation design and instrumentation

Convert a deliberately unwrapped radar phase difference to a candidate line-of-sight displacement and discuss how incidence geometry controls interpretation. For this lesson, use the following common unit protocol as an explicit checklist: Model position as a linear trend plus seasonal terms, discrete offsets and residual noise. Flag changed receivers, storms and seismic events. Fit both a minimal and an expanded model using held-out time intervals. Record the raw observable, its units, its collection conditions and any correction applied before deriving the displayed result. Distinguish a physically measured range, image intensity or height difference from a parameter that software estimated after applying assumptions. The same nominal output may be produced by different measurement procedures with different covariance and failure modes. Create a versioned log of those differences before comparing datasets.

### Worked numerical case 5.4: InSAR phase displacement

**Given:** 2 rad unwrapped phase. **Calculation rule:** LOS displacement = λφ/(4π) with assumed radar wavelength 5.6 cm. **Computed result:** 0.891268 cm. Report enough significant digits to show the underlying arithmetic, but do not claim that all displayed digits are measured information. The worked quantity is hypothetical and intentionally idealized. Recalculate it using original units rather than mentally switching between millimeters, meters, kilometers and degrees. Then double-check dimensions and evaluate whether a physically reasonable change in input produces the expected direction of change.

**Sensitivity test.** Rerun the given calculation with a modestly changed input, preferably increasing the magnitude by ten percent while keeping all other assumptions fixed. Describe both the absolute and relative output change. This isolates sensitivity to one variable only; it is not a total uncertainty budget. If a source has correlated errors, do not combine them with independent-error root-sum-of-squares unless independence is justified. A credible interpretation explains which input is a field observation, which is a normative constant and which is a teaching assumption.

### Confounding and alternative explanation

**Frequent mistake:** A single line-of-sight measurement cannot uniquely determine three-dimensional ground motion; atmospheric delay can imitate deformation. Compare the resulting velocity and its uncertainty. If an apparent acceleration disappears after adding a station jump, avoid describing it as new tectonic activity. Construct a competing explanation and decide which new observation would discriminate between the two. Avoid evaluating success by how smooth a graphic looks. Negative controls, repeated occupations, held-out locations and cross-sensor checks can be more informative than extra decimals. Classify each candidate error as one of reference mismatch, geometry, calibration, atmospheric or environmental variability, temporal sampling or inference-model misspecification. Explain why that distinction matters for the specific conclusion being attempted.

### Applied case and decision quality

Specify independent GNSS checks for subsidence inferred around a metropolitan pumping district. Use residual diagnostic plots and document sensitivity to missing observations and autocorrelation. In your written response, first state the decision being supported. Then give a physically meaningful result with units and coordinate conventions. Follow it with the strongest alternative explanation and an observation that could overturn your current interpretation. If uncertainty overlaps the stakeholder threshold, report that ambiguity rather than assigning unwarranted confidence to either choice. This discipline connects a numerical model to a traceable claim about the world.

### Guided questions and independent exercise

1. Which variables in this lesson are directly observed, and which are inferred after applying a physical model? Give the relevant units and reference conventions.
2. Recalculate the worked case after changing the controlling input by 10%; explain the direction of the resulting change and what assumption remained fixed.
3. Explain why the following pitfall matters for the current scientific claim: A single line-of-sight measurement cannot uniquely determine three-dimensional ground motion; atmospheric delay can imitate deformation.
4. Propose one independent measurement or hold-out test that could reveal a systematic error not visible in the original calculation.
5. Write a three-sentence risk statement separating the demonstrated calculation from an application it is not qualified to support.

## Lesson 5.5: Loading, groundwater and local motion

### Physical model and vocabulary

Seasonal groundwater, snow, reservoir loading and monument instability may all influence station position. Interpretation therefore needs auxiliary hydroclimate records and instrument history. A useful physical statement explicitly identifies the quantity being observed, the idealizations needed to interpret it, and at least one phenomenon excluded by the model. Write a small equation or a structured dependency diagram before processing numbers. If two physical mechanisms can generate the same measurement, the inverse problem is not unique without a further constraint. The correct level of modeling depends on the consequence of the intended decision; an approximation acceptable in a classroom is not automatically acceptable in cadastral surveying, flood warnings or infrastructure monitoring.

### Observation design and instrumentation

Compare synthetic vertical GNSS fluctuations with a modeled water-storage series at lagged and contemporaneous times; calculate whether the association survives detrending. For this lesson, use the following common unit protocol as an explicit checklist: Model position as a linear trend plus seasonal terms, discrete offsets and residual noise. Flag changed receivers, storms and seismic events. Fit both a minimal and an expanded model using held-out time intervals. Record the raw observable, its units, its collection conditions and any correction applied before deriving the displayed result. Distinguish a physically measured range, image intensity or height difference from a parameter that software estimated after applying assumptions. The same nominal output may be produced by different measurement procedures with different covariance and failure modes. Create a versioned log of those differences before comparing datasets.

### Worked numerical case 5.5: Deformation rate

**Given:** 35 mm cumulative motion. **Calculation rule:** Average five-year velocity = displacement divided by elapsed time; ignores steps. **Computed result:** 7 mm/year. Report enough significant digits to show the underlying arithmetic, but do not claim that all displayed digits are measured information. The worked quantity is hypothetical and intentionally idealized. Recalculate it using original units rather than mentally switching between millimeters, meters, kilometers and degrees. Then double-check dimensions and evaluate whether a physically reasonable change in input produces the expected direction of change.

**Sensitivity test.** Rerun the given calculation with a modestly changed input, preferably increasing the magnitude by ten percent while keeping all other assumptions fixed. Describe both the absolute and relative output change. This isolates sensitivity to one variable only; it is not a total uncertainty budget. If a source has correlated errors, do not combine them with independent-error root-sum-of-squares unless independence is justified. A credible interpretation explains which input is a field observation, which is a normative constant and which is a teaching assumption.

### Confounding and alternative explanation

**Frequent mistake:** Correlation between water storage and elevation does not by itself establish causation, especially when regional forcing affects both. Compare the resulting velocity and its uncertainty. If an apparent acceleration disappears after adding a station jump, avoid describing it as new tectonic activity. Construct a competing explanation and decide which new observation would discriminate between the two. Avoid evaluating success by how smooth a graphic looks. Negative controls, repeated occupations, held-out locations and cross-sensor checks can be more informative than extra decimals. Classify each candidate error as one of reference mismatch, geometry, calibration, atmospheric or environmental variability, temporal sampling or inference-model misspecification. Explain why that distinction matters for the specific conclusion being attempted.

### Applied case and decision quality

Choose a strategy for monitoring a dam that separates structural response from site-wide loading. Use residual diagnostic plots and document sensitivity to missing observations and autocorrelation. In your written response, first state the decision being supported. Then give a physically meaningful result with units and coordinate conventions. Follow it with the strongest alternative explanation and an observation that could overturn your current interpretation. If uncertainty overlaps the stakeholder threshold, report that ambiguity rather than assigning unwarranted confidence to either choice. This discipline connects a numerical model to a traceable claim about the world.

### Guided questions and independent exercise

1. Which variables in this lesson are directly observed, and which are inferred after applying a physical model? Give the relevant units and reference conventions.
2. Recalculate the worked case after changing the controlling input by 10%; explain the direction of the resulting change and what assumption remained fixed.
3. Explain why the following pitfall matters for the current scientific claim: Correlation between water storage and elevation does not by itself establish causation, especially when regional forcing affects both.
4. Propose one independent measurement or hold-out test that could reveal a systematic error not visible in the original calculation.
5. Write a three-sentence risk statement separating the demonstrated calculation from an application it is not qualified to support.

## Unit synthesis and interpretive assessment

A fictional active margin has GNSS stations, an earthquake displacement step, seasonal loading, and an InSAR satellite track. Learners test whether a reported displacement is tectonic, hydrological, instrumental or reference-frame driven. Develop a compact research plan with a clear inference target, observational geometry, sampling strategy, numerical cross-check and validation design. Present one figure that retains units and reference-frame metadata. Describe a case in which apparent agreement across measurements may still result from shared bias. What additional independent measurement would break that dependence?

The main theme is this: Deformation monitoring is fundamentally a time-series inference problem. Observations must be registered to consistent coordinates and separated into continuous motion, discrete offsets, periodic effects and uncertainty. Before using the unit result to guide a practical choice, ask whether the error bar reflects the true sources of uncertainty or only the variation inside a simplified numerical procedure. Define the population and period in which the conclusion is intended to hold. A consistent interpretation must remain intelligible without dependence on a proprietary figure or a hidden processing step.

