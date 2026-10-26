# Unit 4: Gravity, Elevation and Vertical Reference Systems

## Guiding problem

Why are a GNSS height and an engineering elevation different and how are heights maintained?

**Fictional investigation:** A fictional floodplain project joins GNSS, leveling, gravity and an altimeter. Some points lie above a historical local tide datum; others use ellipsoidal height and require a declared geoid model.

## Scientific scope

Height systems connect geometry to Earth’s gravity potential. Conversions may look like simple subtraction but rely on specific geoid models, datum realizations, time changes and terrain-dependent corrections. Whenever positions, ranges, elevations or images are compared, uncertainty must be attached to a specified measurand and an explicitly identified reference. The word accurate is incomplete unless the reader can state accurate relative to what, over which interval and for which population of conditions. A local fit may be adequate for instruction without being an operationally defensible geodetic product.

## Unit practical: Height survey integration

Connect a leveling loop to two benchmarks and overlay ellipsoidal heights from GNSS after selecting a compatible geoid. Clearly identify height type and model release for every column.

Test whether the observed differences could arise from geoid error, benchmark movement, tides or local leveling systematics. A single discrepancy does not distinguish these mechanisms.

Decide what additional gravity or control observations would make the chosen elevation interpretation more defensible.

## Data notebook requirements

Create a plain-text notebook containing input columns, units, a source/provenance statement, treatment of missing records, computational steps and at least one independent check. All datasets in this unit are manufactured for learning rather than sampled from nature. When reporting an estimated number, write out the assumptions connecting the number with the claimed physical variable. Note whether uncertainty is random, systematic or model-based. Provide a short explanation of what the number *cannot* tell us. The purpose is to practice disciplined geodetic reasoning as well as numerical computation.

## Lesson 4.1: Gravity field and geopotential

### Physical model and vocabulary

Gravity includes gravitation and the effect of Earth rotation in a rotating frame. Geopotential surfaces represent equal potential, and the geoid is one selected reference equipotential. A useful physical statement explicitly identifies the quantity being observed, the idealizations needed to interpret it, and at least one phenomenon excluded by the model. Write a small equation or a structured dependency diagram before processing numbers. If two physical mechanisms can generate the same measurement, the inverse problem is not unique without a further constraint. The correct level of modeling depends on the consequence of the intended decision; an approximation acceptable in a classroom is not automatically acceptable in cadastral surveying, flood warnings or infrastructure monitoring.

### Observation design and instrumentation

Compare repeat gravity observations with instrument drift estimates and nearby benchmark elevations before interpreting a spatial anomaly. For this lesson, use the following common unit protocol as an explicit checklist: Connect a leveling loop to two benchmarks and overlay ellipsoidal heights from GNSS after selecting a compatible geoid. Clearly identify height type and model release for every column. Record the raw observable, its units, its collection conditions and any correction applied before deriving the displayed result. Distinguish a physically measured range, image intensity or height difference from a parameter that software estimated after applying assumptions. The same nominal output may be produced by different measurement procedures with different covariance and failure modes. Create a versioned log of those differences before comparing datasets.

### Worked numerical case 4.1: Orthometric conversion

**Given:** 45 m ellipsoidal height. **Calculation rule:** With a fixed, compatible geoid undulation N=+27.6 m, H≈h−N. **Computed result:** 17.4 m. Report enough significant digits to show the underlying arithmetic, but do not claim that all displayed digits are measured information. The worked quantity is hypothetical and intentionally idealized. Recalculate it using original units rather than mentally switching between millimeters, meters, kilometers and degrees. Then double-check dimensions and evaluate whether a physically reasonable change in input produces the expected direction of change.

**Sensitivity test.** Rerun the given calculation with a modestly changed input, preferably increasing the magnitude by ten percent while keeping all other assumptions fixed. Describe both the absolute and relative output change. This isolates sensitivity to one variable only; it is not a total uncertainty budget. If a source has correlated errors, do not combine them with independent-error root-sum-of-squares unless independence is justified. A credible interpretation explains which input is a field observation, which is a normative constant and which is a teaching assumption.

### Confounding and alternative explanation

**Frequent mistake:** Do not treat a gravity anomaly map as a direct unambiguous map of rock type; geometry and density assumptions influence the inverse interpretation. Test whether the observed differences could arise from geoid error, benchmark movement, tides or local leveling systematics. A single discrepancy does not distinguish these mechanisms. Construct a competing explanation and decide which new observation would discriminate between the two. Avoid evaluating success by how smooth a graphic looks. Negative controls, repeated occupations, held-out locations and cross-sensor checks can be more informative than extra decimals. Classify each candidate error as one of reference mismatch, geometry, calibration, atmospheric or environmental variability, temporal sampling or inference-model misspecification. Explain why that distinction matters for the specific conclusion being attempted.

### Applied case and decision quality

Assess whether gravity data can help distinguish regional groundwater change from instrument bias. Decide what additional gravity or control observations would make the chosen elevation interpretation more defensible. In your written response, first state the decision being supported. Then give a physically meaningful result with units and coordinate conventions. Follow it with the strongest alternative explanation and an observation that could overturn your current interpretation. If uncertainty overlaps the stakeholder threshold, report that ambiguity rather than assigning unwarranted confidence to either choice. This discipline connects a numerical model to a traceable claim about the world.

### Guided questions and independent exercise

1. Which variables in this lesson are directly observed, and which are inferred after applying a physical model? Give the relevant units and reference conventions.
2. Recalculate the worked case after changing the controlling input by 10%; explain the direction of the resulting change and what assumption remained fixed.
3. Explain why the following pitfall matters for the current scientific claim: Do not treat a gravity anomaly map as a direct unambiguous map of rock type; geometry and density assumptions influence the inverse interpretation.
4. Propose one independent measurement or hold-out test that could reveal a systematic error not visible in the original calculation.
5. Write a three-sentence risk statement separating the demonstrated calculation from an application it is not qualified to support.

## Lesson 4.2: Leveling and height differences

### Physical model and vocabulary

Precise leveling transfers local height differences through lines of sight and repeated setups. Corrections, closure and datum connection determine whether the reported heights are comparable. A useful physical statement explicitly identifies the quantity being observed, the idealizations needed to interpret it, and at least one phenomenon excluded by the model. Write a small equation or a structured dependency diagram before processing numbers. If two physical mechanisms can generate the same measurement, the inverse problem is not unique without a further constraint. The correct level of modeling depends on the consequence of the intended decision; an approximation acceptable in a classroom is not automatically acceptable in cadastral surveying, flood warnings or infrastructure monitoring.

### Observation design and instrumentation

Design a closed leveling loop with forward and reverse observations, balanced sight lengths and a closure report. Evaluate systematic rather than only random errors. For this lesson, use the following common unit protocol as an explicit checklist: Connect a leveling loop to two benchmarks and overlay ellipsoidal heights from GNSS after selecting a compatible geoid. Clearly identify height type and model release for every column. Record the raw observable, its units, its collection conditions and any correction applied before deriving the displayed result. Distinguish a physically measured range, image intensity or height difference from a parameter that software estimated after applying assumptions. The same nominal output may be produced by different measurement procedures with different covariance and failure modes. Create a versioned log of those differences before comparing datasets.

### Worked numerical case 4.2: Geoid undulation

**Given:** 15 m orthometric height. **Calculation rule:** Given synthetic h=H+31.2 m, N=h−H; a deliberately simple consistency test. **Computed result:** 31.2 m. Report enough significant digits to show the underlying arithmetic, but do not claim that all displayed digits are measured information. The worked quantity is hypothetical and intentionally idealized. Recalculate it using original units rather than mentally switching between millimeters, meters, kilometers and degrees. Then double-check dimensions and evaluate whether a physically reasonable change in input produces the expected direction of change.

**Sensitivity test.** Rerun the given calculation with a modestly changed input, preferably increasing the magnitude by ten percent while keeping all other assumptions fixed. Describe both the absolute and relative output change. This isolates sensitivity to one variable only; it is not a total uncertainty budget. If a source has correlated errors, do not combine them with independent-error root-sum-of-squares unless independence is justified. A credible interpretation explains which input is a field observation, which is a normative constant and which is a teaching assumption.

### Confounding and alternative explanation

**Frequent mistake:** A leveling traverse with small closure does not establish its absolute datum, and refraction effects can accumulate systematically. Test whether the observed differences could arise from geoid error, benchmark movement, tides or local leveling systematics. A single discrepancy does not distinguish these mechanisms. Construct a competing explanation and decide which new observation would discriminate between the two. Avoid evaluating success by how smooth a graphic looks. Negative controls, repeated occupations, held-out locations and cross-sensor checks can be more informative than extra decimals. Classify each candidate error as one of reference mismatch, geometry, calibration, atmospheric or environmental variability, temporal sampling or inference-model misspecification. Explain why that distinction matters for the specific conclusion being attempted.

### Applied case and decision quality

Plan a road survey across a low-gradient floodplain where centimeter errors affect drainage. Decide what additional gravity or control observations would make the chosen elevation interpretation more defensible. In your written response, first state the decision being supported. Then give a physically meaningful result with units and coordinate conventions. Follow it with the strongest alternative explanation and an observation that could overturn your current interpretation. If uncertainty overlaps the stakeholder threshold, report that ambiguity rather than assigning unwarranted confidence to either choice. This discipline connects a numerical model to a traceable claim about the world.

### Guided questions and independent exercise

1. Which variables in this lesson are directly observed, and which are inferred after applying a physical model? Give the relevant units and reference conventions.
2. Recalculate the worked case after changing the controlling input by 10%; explain the direction of the resulting change and what assumption remained fixed.
3. Explain why the following pitfall matters for the current scientific claim: A leveling traverse with small closure does not establish its absolute datum, and refraction effects can accumulate systematically.
4. Propose one independent measurement or hold-out test that could reveal a systematic error not visible in the original calculation.
5. Write a three-sentence risk statement separating the demonstrated calculation from an application it is not qualified to support.

## Lesson 4.3: Ellipsoidal and orthometric heights

### Physical model and vocabulary

A commonly used relationship is h approximately equal to H plus N, where h denotes ellipsoidal height, H orthometric height and N geoid undulation under consistent conventions. A useful physical statement explicitly identifies the quantity being observed, the idealizations needed to interpret it, and at least one phenomenon excluded by the model. Write a small equation or a structured dependency diagram before processing numbers. If two physical mechanisms can generate the same measurement, the inverse problem is not unique without a further constraint. The correct level of modeling depends on the consequence of the intended decision; an approximation acceptable in a classroom is not automatically acceptable in cadastral surveying, flood warnings or infrastructure monitoring.

### Observation design and instrumentation

Combine a fictional GNSS ellipsoidal height with a documented geoid-model value and test the sensitivity of derived elevation to a one-decimeter geoid error. For this lesson, use the following common unit protocol as an explicit checklist: Connect a leveling loop to two benchmarks and overlay ellipsoidal heights from GNSS after selecting a compatible geoid. Clearly identify height type and model release for every column. Record the raw observable, its units, its collection conditions and any correction applied before deriving the displayed result. Distinguish a physically measured range, image intensity or height difference from a parameter that software estimated after applying assumptions. The same nominal output may be produced by different measurement procedures with different covariance and failure modes. Create a versioned log of those differences before comparing datasets.

### Worked numerical case 4.3: Slab attraction

**Given:** 180 m slab thickness. **Calculation rule:** Infinite slab gravity = 2πGρt converted from m/s² to mGal. **Computed result:** 20.1544 mGal. Report enough significant digits to show the underlying arithmetic, but do not claim that all displayed digits are measured information. The worked quantity is hypothetical and intentionally idealized. Recalculate it using original units rather than mentally switching between millimeters, meters, kilometers and degrees. Then double-check dimensions and evaluate whether a physically reasonable change in input produces the expected direction of change.

**Sensitivity test.** Rerun the given calculation with a modestly changed input, preferably increasing the magnitude by ten percent while keeping all other assumptions fixed. Describe both the absolute and relative output change. This isolates sensitivity to one variable only; it is not a total uncertainty budget. If a source has correlated errors, do not combine them with independent-error root-sum-of-squares unless independence is justified. A credible interpretation explains which input is a field observation, which is a normative constant and which is a teaching assumption.

### Confounding and alternative explanation

**Frequent mistake:** Blindly subtracting a geoid height from a GNSS value without checking realization and tidal system can introduce misleading biases. Test whether the observed differences could arise from geoid error, benchmark movement, tides or local leveling systematics. A single discrepancy does not distinguish these mechanisms. Construct a competing explanation and decide which new observation would discriminate between the two. Avoid evaluating success by how smooth a graphic looks. Negative controls, repeated occupations, held-out locations and cross-sensor checks can be more informative than extra decimals. Classify each candidate error as one of reference mismatch, geometry, calibration, atmospheric or environmental variability, temporal sampling or inference-model misspecification. Explain why that distinction matters for the specific conclusion being attempted.

### Applied case and decision quality

Make a public elevation data product with an explicit vertical datum, units, geoid model and epoch. Decide what additional gravity or control observations would make the chosen elevation interpretation more defensible. In your written response, first state the decision being supported. Then give a physically meaningful result with units and coordinate conventions. Follow it with the strongest alternative explanation and an observation that could overturn your current interpretation. If uncertainty overlaps the stakeholder threshold, report that ambiguity rather than assigning unwarranted confidence to either choice. This discipline connects a numerical model to a traceable claim about the world.

### Guided questions and independent exercise

1. Which variables in this lesson are directly observed, and which are inferred after applying a physical model? Give the relevant units and reference conventions.
2. Recalculate the worked case after changing the controlling input by 10%; explain the direction of the resulting change and what assumption remained fixed.
3. Explain why the following pitfall matters for the current scientific claim: Blindly subtracting a geoid height from a GNSS value without checking realization and tidal system can introduce misleading biases.
4. Propose one independent measurement or hold-out test that could reveal a systematic error not visible in the original calculation.
5. Write a three-sentence risk statement separating the demonstrated calculation from an application it is not qualified to support.

## Lesson 4.4: Gravity anomalies and regional models

### Physical model and vocabulary

Free-air and Bouguer reductions are related but answer different geophysical questions; density assumptions influence Bouguer estimates and interpretation. A useful physical statement explicitly identifies the quantity being observed, the idealizations needed to interpret it, and at least one phenomenon excluded by the model. Write a small equation or a structured dependency diagram before processing numbers. If two physical mechanisms can generate the same measurement, the inverse problem is not unique without a further constraint. The correct level of modeling depends on the consequence of the intended decision; an approximation acceptable in a classroom is not automatically acceptable in cadastral surveying, flood warnings or infrastructure monitoring.

### Observation design and instrumentation

Calculate the attraction of an idealized horizontal slab, vary assumed density and thickness, and evaluate whether independent geological observations reduce ambiguity. For this lesson, use the following common unit protocol as an explicit checklist: Connect a leveling loop to two benchmarks and overlay ellipsoidal heights from GNSS after selecting a compatible geoid. Clearly identify height type and model release for every column. Record the raw observable, its units, its collection conditions and any correction applied before deriving the displayed result. Distinguish a physically measured range, image intensity or height difference from a parameter that software estimated after applying assumptions. The same nominal output may be produced by different measurement procedures with different covariance and failure modes. Create a versioned log of those differences before comparing datasets.

### Worked numerical case 4.4: Relative sea-level contribution

**Given:** 2.4 mm/year land subsidence. **Calculation rule:** Land sinking relative to a fixed ocean surface produces an equal positive relative-water-level trend for 12 years. **Computed result:** 28.8 mm. Report enough significant digits to show the underlying arithmetic, but do not claim that all displayed digits are measured information. The worked quantity is hypothetical and intentionally idealized. Recalculate it using original units rather than mentally switching between millimeters, meters, kilometers and degrees. Then double-check dimensions and evaluate whether a physically reasonable change in input produces the expected direction of change.

**Sensitivity test.** Rerun the given calculation with a modestly changed input, preferably increasing the magnitude by ten percent while keeping all other assumptions fixed. Describe both the absolute and relative output change. This isolates sensitivity to one variable only; it is not a total uncertainty budget. If a source has correlated errors, do not combine them with independent-error root-sum-of-squares unless independence is justified. A credible interpretation explains which input is a field observation, which is a normative constant and which is a teaching assumption.

### Confounding and alternative explanation

**Frequent mistake:** A strong Bouguer contrast alone does not uniquely determine subsurface structure; buried mass distributions are nonunique. Test whether the observed differences could arise from geoid error, benchmark movement, tides or local leveling systematics. A single discrepancy does not distinguish these mechanisms. Construct a competing explanation and decide which new observation would discriminate between the two. Avoid evaluating success by how smooth a graphic looks. Negative controls, repeated occupations, held-out locations and cross-sensor checks can be more informative than extra decimals. Classify each candidate error as one of reference mismatch, geometry, calibration, atmospheric or environmental variability, temporal sampling or inference-model misspecification. Explain why that distinction matters for the specific conclusion being attempted.

### Applied case and decision quality

Prepare an exploration feasibility memo that specifies limitations of gravity-only inversion. Decide what additional gravity or control observations would make the chosen elevation interpretation more defensible. In your written response, first state the decision being supported. Then give a physically meaningful result with units and coordinate conventions. Follow it with the strongest alternative explanation and an observation that could overturn your current interpretation. If uncertainty overlaps the stakeholder threshold, report that ambiguity rather than assigning unwarranted confidence to either choice. This discipline connects a numerical model to a traceable claim about the world.

### Guided questions and independent exercise

1. Which variables in this lesson are directly observed, and which are inferred after applying a physical model? Give the relevant units and reference conventions.
2. Recalculate the worked case after changing the controlling input by 10%; explain the direction of the resulting change and what assumption remained fixed.
3. Explain why the following pitfall matters for the current scientific claim: A strong Bouguer contrast alone does not uniquely determine subsurface structure; buried mass distributions are nonunique.
4. Propose one independent measurement or hold-out test that could reveal a systematic error not visible in the original calculation.
5. Write a three-sentence risk statement separating the demonstrated calculation from an application it is not qualified to support.

## Lesson 4.5: Tides, dynamic surfaces and sea-level reference

### Physical model and vocabulary

Tidal datums are statistics of water-level observations over defined epochs, not universal equivalents of a geoid. Relative sea-level change combines ocean behavior and vertical land motion. A useful physical statement explicitly identifies the quantity being observed, the idealizations needed to interpret it, and at least one phenomenon excluded by the model. Write a small equation or a structured dependency diagram before processing numbers. If two physical mechanisms can generate the same measurement, the inverse problem is not unique without a further constraint. The correct level of modeling depends on the consequence of the intended decision; an approximation acceptable in a classroom is not automatically acceptable in cadastral surveying, flood warnings or infrastructure monitoring.

### Observation design and instrumentation

Compare a synthetic tide-gauge trend with colocated GNSS vertical velocity. Show explicitly how a sinking land benchmark changes the apparent relative trend. For this lesson, use the following common unit protocol as an explicit checklist: Connect a leveling loop to two benchmarks and overlay ellipsoidal heights from GNSS after selecting a compatible geoid. Clearly identify height type and model release for every column. Record the raw observable, its units, its collection conditions and any correction applied before deriving the displayed result. Distinguish a physically measured range, image intensity or height difference from a parameter that software estimated after applying assumptions. The same nominal output may be produced by different measurement procedures with different covariance and failure modes. Create a versioned log of those differences before comparing datasets.

### Worked numerical case 4.5: Gravity potential difference

**Given:** 0.9 m elevation change. **Calculation rule:** Small-height potential difference ≈ mean g × height change. **Computed result:** 8.829 m²/s². Report enough significant digits to show the underlying arithmetic, but do not claim that all displayed digits are measured information. The worked quantity is hypothetical and intentionally idealized. Recalculate it using original units rather than mentally switching between millimeters, meters, kilometers and degrees. Then double-check dimensions and evaluate whether a physically reasonable change in input produces the expected direction of change.

**Sensitivity test.** Rerun the given calculation with a modestly changed input, preferably increasing the magnitude by ten percent while keeping all other assumptions fixed. Describe both the absolute and relative output change. This isolates sensitivity to one variable only; it is not a total uncertainty budget. If a source has correlated errors, do not combine them with independent-error root-sum-of-squares unless independence is justified. A credible interpretation explains which input is a field observation, which is a normative constant and which is a teaching assumption.

### Confounding and alternative explanation

**Frequent mistake:** Comparing heights across tide stations without a transformation model confuses local tidal reference surfaces with global height systems. Test whether the observed differences could arise from geoid error, benchmark movement, tides or local leveling systematics. A single discrepancy does not distinguish these mechanisms. Construct a competing explanation and decide which new observation would discriminate between the two. Avoid evaluating success by how smooth a graphic looks. Negative controls, repeated occupations, held-out locations and cross-sensor checks can be more informative than extra decimals. Classify each candidate error as one of reference mismatch, geometry, calibration, atmospheric or environmental variability, temporal sampling or inference-model misspecification. Explain why that distinction matters for the specific conclusion being attempted.

### Applied case and decision quality

Design a coastal flood-map data dictionary that protects users from silent datum mixing. Decide what additional gravity or control observations would make the chosen elevation interpretation more defensible. In your written response, first state the decision being supported. Then give a physically meaningful result with units and coordinate conventions. Follow it with the strongest alternative explanation and an observation that could overturn your current interpretation. If uncertainty overlaps the stakeholder threshold, report that ambiguity rather than assigning unwarranted confidence to either choice. This discipline connects a numerical model to a traceable claim about the world.

### Guided questions and independent exercise

1. Which variables in this lesson are directly observed, and which are inferred after applying a physical model? Give the relevant units and reference conventions.
2. Recalculate the worked case after changing the controlling input by 10%; explain the direction of the resulting change and what assumption remained fixed.
3. Explain why the following pitfall matters for the current scientific claim: Comparing heights across tide stations without a transformation model confuses local tidal reference surfaces with global height systems.
4. Propose one independent measurement or hold-out test that could reveal a systematic error not visible in the original calculation.
5. Write a three-sentence risk statement separating the demonstrated calculation from an application it is not qualified to support.

## Unit synthesis and interpretive assessment

A fictional floodplain project joins GNSS, leveling, gravity and an altimeter. Some points lie above a historical local tide datum; others use ellipsoidal height and require a declared geoid model. Develop a compact research plan with a clear inference target, observational geometry, sampling strategy, numerical cross-check and validation design. Present one figure that retains units and reference-frame metadata. Describe a case in which apparent agreement across measurements may still result from shared bias. What additional independent measurement would break that dependence?

The main theme is this: Height systems connect geometry to Earth’s gravity potential. Conversions may look like simple subtraction but rely on specific geoid models, datum realizations, time changes and terrain-dependent corrections. Before using the unit result to guide a practical choice, ask whether the error bar reflects the true sources of uncertainty or only the variation inside a simplified numerical procedure. Define the population and period in which the conclusion is intended to hold. A consistent interpretation must remain intelligible without dependence on a proprietary figure or a hidden processing step.

