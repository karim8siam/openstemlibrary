# Unit 6: Space Geodesy, Satellite Orbits and Imaging

## Guiding problem

What can orbiting platforms measure about Earth’s geometry and its changing surface?

**Fictional investigation:** A fictional Earth-observation mission covers a mountain basin using multi-orbit optical imagery, radar, laser altimetry and GNSS control. Students track whether each measurement is a range, angle, intensity or inferred terrain variable.

## Scientific scope

Satellite measurements are not maps by themselves. Platform ephemerides, timing, viewing geometry, radiometric calibration and retrieval algorithms transform electromagnetic observations into geophysical products. Their uncertainties differ by sensor and surface. Whenever positions, ranges, elevations or images are compared, uncertainty must be attached to a specified measurand and an explicitly identified reference. The word accurate is incomplete unless the reader can state accurate relative to what, over which interval and for which population of conditions. A local fit may be adequate for instruction without being an operationally defensible geodetic product.

## Unit practical: Orbit and retrieval verification

For two fictional satellite passes, state orbit height, viewing geometry, footprint, spectral response, timing, product processing level and mask criteria. Separate a measured signal from the derived geophysical quantity.

Ask whether a detected seasonal pattern survives a different viewing geometry or a second sensor. Divergent measurements may reflect response physics rather than one platform being defective.

Assess representativeness: a satellite footprint can be larger than a field plot or blend multiple land-cover types.

## Data notebook requirements

Create a plain-text notebook containing input columns, units, a source/provenance statement, treatment of missing records, computational steps and at least one independent check. All datasets in this unit are manufactured for learning rather than sampled from nature. When reporting an estimated number, write out the assumptions connecting the number with the claimed physical variable. Note whether uncertainty is random, systematic or model-based. Provide a short explanation of what the number *cannot* tell us. The purpose is to practice disciplined geodetic reasoning as well as numerical computation.

## Lesson 6.1: Orbital geometry and repeat coverage

### Physical model and vocabulary

Low Earth orbit motion is governed principally by gravity, while repeat observations depend on orbit inclination, swath, instrument pointing and ground-track geometry. Actual orbit prediction needs perturbation modeling. A useful physical statement explicitly identifies the quantity being observed, the idealizations needed to interpret it, and at least one phenomenon excluded by the model. Write a small equation or a structured dependency diagram before processing numbers. If two physical mechanisms can generate the same measurement, the inverse problem is not unique without a further constraint. The correct level of modeling depends on the consequence of the intended decision; an approximation acceptable in a classroom is not automatically acceptable in cadastral surveying, flood warnings or infrastructure monitoring.

### Observation design and instrumentation

Estimate an ideal circular orbital period at two hypothetical altitudes and explain why these calculations are not adequate for precise satellite ephemerides. For this lesson, use the following common unit protocol as an explicit checklist: For two fictional satellite passes, state orbit height, viewing geometry, footprint, spectral response, timing, product processing level and mask criteria. Separate a measured signal from the derived geophysical quantity. Record the raw observable, its units, its collection conditions and any correction applied before deriving the displayed result. Distinguish a physically measured range, image intensity or height difference from a parameter that software estimated after applying assumptions. The same nominal output may be produced by different measurement procedures with different covariance and failure modes. Create a versioned log of those differences before comparing datasets.

### Worked numerical case 6.1: Circular orbital period

**Given:** 450 km orbital altitude. **Calculation rule:** Two-body ideal circular orbital period; Earth radius ≈6371 km. **Computed result:** 93.4398 minutes. Report enough significant digits to show the underlying arithmetic, but do not claim that all displayed digits are measured information. The worked quantity is hypothetical and intentionally idealized. Recalculate it using original units rather than mentally switching between millimeters, meters, kilometers and degrees. Then double-check dimensions and evaluate whether a physically reasonable change in input produces the expected direction of change.

**Sensitivity test.** Rerun the given calculation with a modestly changed input, preferably increasing the magnitude by ten percent while keeping all other assumptions fixed. Describe both the absolute and relative output change. This isolates sensitivity to one variable only; it is not a total uncertainty budget. If a source has correlated errors, do not combine them with independent-error root-sum-of-squares unless independence is justified. A credible interpretation explains which input is a field observation, which is a normative constant and which is a teaching assumption.

### Confounding and alternative explanation

**Frequent mistake:** A nominal revisit interval is not the same as cloud-free acquisition frequency or usable phase-coherent radar coverage. Ask whether a detected seasonal pattern survives a different viewing geometry or a second sensor. Divergent measurements may reflect response physics rather than one platform being defective. Construct a competing explanation and decide which new observation would discriminate between the two. Avoid evaluating success by how smooth a graphic looks. Negative controls, repeated occupations, held-out locations and cross-sensor checks can be more informative than extra decimals. Classify each candidate error as one of reference mismatch, geometry, calibration, atmospheric or environmental variability, temporal sampling or inference-model misspecification. Explain why that distinction matters for the specific conclusion being attempted.

### Applied case and decision quality

Select an acquisition schedule for seasonal wetlands and identify likely missing-observation biases. Assess representativeness: a satellite footprint can be larger than a field plot or blend multiple land-cover types. In your written response, first state the decision being supported. Then give a physically meaningful result with units and coordinate conventions. Follow it with the strongest alternative explanation and an observation that could overturn your current interpretation. If uncertainty overlaps the stakeholder threshold, report that ambiguity rather than assigning unwarranted confidence to either choice. This discipline connects a numerical model to a traceable claim about the world.

### Guided questions and independent exercise

1. Which variables in this lesson are directly observed, and which are inferred after applying a physical model? Give the relevant units and reference conventions.
2. Recalculate the worked case after changing the controlling input by 10%; explain the direction of the resulting change and what assumption remained fixed.
3. Explain why the following pitfall matters for the current scientific claim: A nominal revisit interval is not the same as cloud-free acquisition frequency or usable phase-coherent radar coverage.
4. Propose one independent measurement or hold-out test that could reveal a systematic error not visible in the original calculation.
5. Write a three-sentence risk statement separating the demonstrated calculation from an application it is not qualified to support.

## Lesson 6.2: Optical sensors and spectral signatures

### Physical model and vocabulary

Passive optical instruments measure reflected solar radiation or emitted thermal radiation through particular response bands. Surface reflectance estimation requires calibration and atmospheric correction. A useful physical statement explicitly identifies the quantity being observed, the idealizations needed to interpret it, and at least one phenomenon excluded by the model. Write a small equation or a structured dependency diagram before processing numbers. If two physical mechanisms can generate the same measurement, the inverse problem is not unique without a further constraint. The correct level of modeling depends on the consequence of the intended decision; an approximation acceptable in a classroom is not automatically acceptable in cadastral surveying, flood warnings or infrastructure monitoring.

### Observation design and instrumentation

Compare fictional reflectance spectra for vegetation, bare soil and water in red and near-infrared bands while keeping cloud and shadow flags visible. For this lesson, use the following common unit protocol as an explicit checklist: For two fictional satellite passes, state orbit height, viewing geometry, footprint, spectral response, timing, product processing level and mask criteria. Separate a measured signal from the derived geophysical quantity. Record the raw observable, its units, its collection conditions and any correction applied before deriving the displayed result. Distinguish a physically measured range, image intensity or height difference from a parameter that software estimated after applying assumptions. The same nominal output may be produced by different measurement procedures with different covariance and failure modes. Create a versioned log of those differences before comparing datasets.

### Worked numerical case 6.2: Vegetation spectral index

**Given:** 0.43 NIR reflectance. **Calculation rule:** Red surface reflectance is fixed at 0.14; both bands dimensionless. **Computed result:** 0.508772 NDVI. Report enough significant digits to show the underlying arithmetic, but do not claim that all displayed digits are measured information. The worked quantity is hypothetical and intentionally idealized. Recalculate it using original units rather than mentally switching between millimeters, meters, kilometers and degrees. Then double-check dimensions and evaluate whether a physically reasonable change in input produces the expected direction of change.

**Sensitivity test.** Rerun the given calculation with a modestly changed input, preferably increasing the magnitude by ten percent while keeping all other assumptions fixed. Describe both the absolute and relative output change. This isolates sensitivity to one variable only; it is not a total uncertainty budget. If a source has correlated errors, do not combine them with independent-error root-sum-of-squares unless independence is justified. A credible interpretation explains which input is a field observation, which is a normative constant and which is a teaching assumption.

### Confounding and alternative explanation

**Frequent mistake:** A bright pixel may arise from illumination, atmosphere, adjacency or surface properties; spectral labels are not self-evident land-cover classes. Ask whether a detected seasonal pattern survives a different viewing geometry or a second sensor. Divergent measurements may reflect response physics rather than one platform being defective. Construct a competing explanation and decide which new observation would discriminate between the two. Avoid evaluating success by how smooth a graphic looks. Negative controls, repeated occupations, held-out locations and cross-sensor checks can be more informative than extra decimals. Classify each candidate error as one of reference mismatch, geometry, calibration, atmospheric or environmental variability, temporal sampling or inference-model misspecification. Explain why that distinction matters for the specific conclusion being attempted.

### Applied case and decision quality

Plan a vegetation-monitoring baseline that includes ground observations and consistent acquisition season. Assess representativeness: a satellite footprint can be larger than a field plot or blend multiple land-cover types. In your written response, first state the decision being supported. Then give a physically meaningful result with units and coordinate conventions. Follow it with the strongest alternative explanation and an observation that could overturn your current interpretation. If uncertainty overlaps the stakeholder threshold, report that ambiguity rather than assigning unwarranted confidence to either choice. This discipline connects a numerical model to a traceable claim about the world.

### Guided questions and independent exercise

1. Which variables in this lesson are directly observed, and which are inferred after applying a physical model? Give the relevant units and reference conventions.
2. Recalculate the worked case after changing the controlling input by 10%; explain the direction of the resulting change and what assumption remained fixed.
3. Explain why the following pitfall matters for the current scientific claim: A bright pixel may arise from illumination, atmosphere, adjacency or surface properties; spectral labels are not self-evident land-cover classes.
4. Propose one independent measurement or hold-out test that could reveal a systematic error not visible in the original calculation.
5. Write a three-sentence risk statement separating the demonstrated calculation from an application it is not qualified to support.

## Lesson 6.3: Radar imaging and scattering

### Physical model and vocabulary

Active synthetic aperture radar senses microwave backscatter governed by geometry, surface roughness, dielectric properties and polarization. Microwave penetration depends on wavelength and medium. A useful physical statement explicitly identifies the quantity being observed, the idealizations needed to interpret it, and at least one phenomenon excluded by the model. Write a small equation or a structured dependency diagram before processing numbers. If two physical mechanisms can generate the same measurement, the inverse problem is not unique without a further constraint. The correct level of modeling depends on the consequence of the intended decision; an approximation acceptable in a classroom is not automatically acceptable in cadastral surveying, flood warnings or infrastructure monitoring.

### Observation design and instrumentation

Compare two synthetic scenes before and after heavy rainfall while holding incidence angle approximately constant and recording coherence and layover masks. For this lesson, use the following common unit protocol as an explicit checklist: For two fictional satellite passes, state orbit height, viewing geometry, footprint, spectral response, timing, product processing level and mask criteria. Separate a measured signal from the derived geophysical quantity. Record the raw observable, its units, its collection conditions and any correction applied before deriving the displayed result. Distinguish a physically measured range, image intensity or height difference from a parameter that software estimated after applying assumptions. The same nominal output may be produced by different measurement procedures with different covariance and failure modes. Create a versioned log of those differences before comparing datasets.

### Worked numerical case 6.3: Swath footprint illustration

**Given:** 9 degrees full view-angle. **Calculation rule:** Flat-ground field-of-view width ≈2 h tan(full angle/2) at 700 km height. **Computed result:** 110.182 km. Report enough significant digits to show the underlying arithmetic, but do not claim that all displayed digits are measured information. The worked quantity is hypothetical and intentionally idealized. Recalculate it using original units rather than mentally switching between millimeters, meters, kilometers and degrees. Then double-check dimensions and evaluate whether a physically reasonable change in input produces the expected direction of change.

**Sensitivity test.** Rerun the given calculation with a modestly changed input, preferably increasing the magnitude by ten percent while keeping all other assumptions fixed. Describe both the absolute and relative output change. This isolates sensitivity to one variable only; it is not a total uncertainty budget. If a source has correlated errors, do not combine them with independent-error root-sum-of-squares unless independence is justified. A credible interpretation explains which input is a field observation, which is a normative constant and which is a teaching assumption.

### Confounding and alternative explanation

**Frequent mistake:** A backscatter increase cannot be assigned uniquely to soil moisture without ruling out vegetation, geometry and calibration differences. Ask whether a detected seasonal pattern survives a different viewing geometry or a second sensor. Divergent measurements may reflect response physics rather than one platform being defective. Construct a competing explanation and decide which new observation would discriminate between the two. Avoid evaluating success by how smooth a graphic looks. Negative controls, repeated occupations, held-out locations and cross-sensor checks can be more informative than extra decimals. Classify each candidate error as one of reference mismatch, geometry, calibration, atmospheric or environmental variability, temporal sampling or inference-model misspecification. Explain why that distinction matters for the specific conclusion being attempted.

### Applied case and decision quality

Propose an approach for mapping floodwater when optical imagery is unavailable due to clouds. Assess representativeness: a satellite footprint can be larger than a field plot or blend multiple land-cover types. In your written response, first state the decision being supported. Then give a physically meaningful result with units and coordinate conventions. Follow it with the strongest alternative explanation and an observation that could overturn your current interpretation. If uncertainty overlaps the stakeholder threshold, report that ambiguity rather than assigning unwarranted confidence to either choice. This discipline connects a numerical model to a traceable claim about the world.

### Guided questions and independent exercise

1. Which variables in this lesson are directly observed, and which are inferred after applying a physical model? Give the relevant units and reference conventions.
2. Recalculate the worked case after changing the controlling input by 10%; explain the direction of the resulting change and what assumption remained fixed.
3. Explain why the following pitfall matters for the current scientific claim: A backscatter increase cannot be assigned uniquely to soil moisture without ruling out vegetation, geometry and calibration differences.
4. Propose one independent measurement or hold-out test that could reveal a systematic error not visible in the original calculation.
5. Write a three-sentence risk statement separating the demonstrated calculation from an application it is not qualified to support.

## Lesson 6.4: Laser and radar altimetry

### Physical model and vocabulary

Satellite altimeters and laser ranging estimate ranges through travel time, then combine orbit information and corrections to infer height or surface elevation. Water, ice and land require different retracking logic. A useful physical statement explicitly identifies the quantity being observed, the idealizations needed to interpret it, and at least one phenomenon excluded by the model. Write a small equation or a structured dependency diagram before processing numbers. If two physical mechanisms can generate the same measurement, the inverse problem is not unique without a further constraint. The correct level of modeling depends on the consequence of the intended decision; an approximation acceptable in a classroom is not automatically acceptable in cadastral surveying, flood warnings or infrastructure monitoring.

### Observation design and instrumentation

For a synthetic satellite range and orbit altitude, compute a first-pass surface height and list corrections for atmosphere, tides and geophysical variability. For this lesson, use the following common unit protocol as an explicit checklist: For two fictional satellite passes, state orbit height, viewing geometry, footprint, spectral response, timing, product processing level and mask criteria. Separate a measured signal from the derived geophysical quantity. Record the raw observable, its units, its collection conditions and any correction applied before deriving the displayed result. Distinguish a physically measured range, image intensity or height difference from a parameter that software estimated after applying assumptions. The same nominal output may be produced by different measurement procedures with different covariance and failure modes. Create a versioned log of those differences before comparing datasets.

### Worked numerical case 6.4: Satellite altimeter first pass

**Given:** 699.96 km measured range. **Calculation rule:** Subtract range from a nominal 700 km satellite height; geophysical corrections omitted. **Computed result:** 40 m apparent height. Report enough significant digits to show the underlying arithmetic, but do not claim that all displayed digits are measured information. The worked quantity is hypothetical and intentionally idealized. Recalculate it using original units rather than mentally switching between millimeters, meters, kilometers and degrees. Then double-check dimensions and evaluate whether a physically reasonable change in input produces the expected direction of change.

**Sensitivity test.** Rerun the given calculation with a modestly changed input, preferably increasing the magnitude by ten percent while keeping all other assumptions fixed. Describe both the absolute and relative output change. This isolates sensitivity to one variable only; it is not a total uncertainty budget. If a source has correlated errors, do not combine them with independent-error root-sum-of-squares unless independence is justified. A credible interpretation explains which input is a field observation, which is a normative constant and which is a teaching assumption.

### Confounding and alternative explanation

**Frequent mistake:** A range-derived height is not automatically orthometric elevation, and instrument footprint can mix different surface types. Ask whether a detected seasonal pattern survives a different viewing geometry or a second sensor. Divergent measurements may reflect response physics rather than one platform being defective. Construct a competing explanation and decide which new observation would discriminate between the two. Avoid evaluating success by how smooth a graphic looks. Negative controls, repeated occupations, held-out locations and cross-sensor checks can be more informative than extra decimals. Classify each candidate error as one of reference mismatch, geometry, calibration, atmospheric or environmental variability, temporal sampling or inference-model misspecification. Explain why that distinction matters for the specific conclusion being attempted.

### Applied case and decision quality

Assess whether repeat altimetry could detect reservoir volume change and what bathymetry would still be needed. Assess representativeness: a satellite footprint can be larger than a field plot or blend multiple land-cover types. In your written response, first state the decision being supported. Then give a physically meaningful result with units and coordinate conventions. Follow it with the strongest alternative explanation and an observation that could overturn your current interpretation. If uncertainty overlaps the stakeholder threshold, report that ambiguity rather than assigning unwarranted confidence to either choice. This discipline connects a numerical model to a traceable claim about the world.

### Guided questions and independent exercise

1. Which variables in this lesson are directly observed, and which are inferred after applying a physical model? Give the relevant units and reference conventions.
2. Recalculate the worked case after changing the controlling input by 10%; explain the direction of the resulting change and what assumption remained fixed.
3. Explain why the following pitfall matters for the current scientific claim: A range-derived height is not automatically orthometric elevation, and instrument footprint can mix different surface types.
4. Propose one independent measurement or hold-out test that could reveal a systematic error not visible in the original calculation.
5. Write a three-sentence risk statement separating the demonstrated calculation from an application it is not qualified to support.

## Lesson 6.5: Resolution, sampling and uncertainty

### Physical model and vocabulary

Spatial pixel size, optical point-spread function, radar resolution and geolocation accuracy are different properties. The temporal and spectral dimensions also constrain useful environmental inference. A useful physical statement explicitly identifies the quantity being observed, the idealizations needed to interpret it, and at least one phenomenon excluded by the model. Write a small equation or a structured dependency diagram before processing numbers. If two physical mechanisms can generate the same measurement, the inverse problem is not unique without a further constraint. The correct level of modeling depends on the consequence of the intended decision; an approximation acceptable in a classroom is not automatically acceptable in cadastral surveying, flood warnings or infrastructure monitoring.

### Observation design and instrumentation

Resample a synthetic coarse grid to finer cells and compare the number of independent observations before and after interpolation. For this lesson, use the following common unit protocol as an explicit checklist: For two fictional satellite passes, state orbit height, viewing geometry, footprint, spectral response, timing, product processing level and mask criteria. Separate a measured signal from the derived geophysical quantity. Record the raw observable, its units, its collection conditions and any correction applied before deriving the displayed result. Distinguish a physically measured range, image intensity or height difference from a parameter that software estimated after applying assumptions. The same nominal output may be produced by different measurement procedures with different covariance and failure modes. Create a versioned log of those differences before comparing datasets.

### Worked numerical case 6.5: Sampling scale

**Given:** 30 m image pixel width. **Calculation rule:** Area of a square image cell equals pixel width squared; says nothing about optical resolution. **Computed result:** 900 m². Report enough significant digits to show the underlying arithmetic, but do not claim that all displayed digits are measured information. The worked quantity is hypothetical and intentionally idealized. Recalculate it using original units rather than mentally switching between millimeters, meters, kilometers and degrees. Then double-check dimensions and evaluate whether a physically reasonable change in input produces the expected direction of change.

**Sensitivity test.** Rerun the given calculation with a modestly changed input, preferably increasing the magnitude by ten percent while keeping all other assumptions fixed. Describe both the absolute and relative output change. This isolates sensitivity to one variable only; it is not a total uncertainty budget. If a source has correlated errors, do not combine them with independent-error root-sum-of-squares unless independence is justified. A credible interpretation explains which input is a field observation, which is a normative constant and which is a teaching assumption.

### Confounding and alternative explanation

**Frequent mistake:** Upsampling makes more pixels but does not create new physical detail; a high-resolution basemap is not a ground-truth label. Ask whether a detected seasonal pattern survives a different viewing geometry or a second sensor. Divergent measurements may reflect response physics rather than one platform being defective. Construct a competing explanation and decide which new observation would discriminate between the two. Avoid evaluating success by how smooth a graphic looks. Negative controls, repeated occupations, held-out locations and cross-sensor checks can be more informative than extra decimals. Classify each candidate error as one of reference mismatch, geometry, calibration, atmospheric or environmental variability, temporal sampling or inference-model misspecification. Explain why that distinction matters for the specific conclusion being attempted.

### Applied case and decision quality

Write metadata for a satellite-derived hazard layer communicating resolution and uncertainty separately. Assess representativeness: a satellite footprint can be larger than a field plot or blend multiple land-cover types. In your written response, first state the decision being supported. Then give a physically meaningful result with units and coordinate conventions. Follow it with the strongest alternative explanation and an observation that could overturn your current interpretation. If uncertainty overlaps the stakeholder threshold, report that ambiguity rather than assigning unwarranted confidence to either choice. This discipline connects a numerical model to a traceable claim about the world.

### Guided questions and independent exercise

1. Which variables in this lesson are directly observed, and which are inferred after applying a physical model? Give the relevant units and reference conventions.
2. Recalculate the worked case after changing the controlling input by 10%; explain the direction of the resulting change and what assumption remained fixed.
3. Explain why the following pitfall matters for the current scientific claim: Upsampling makes more pixels but does not create new physical detail; a high-resolution basemap is not a ground-truth label.
4. Propose one independent measurement or hold-out test that could reveal a systematic error not visible in the original calculation.
5. Write a three-sentence risk statement separating the demonstrated calculation from an application it is not qualified to support.

## Unit synthesis and interpretive assessment

A fictional Earth-observation mission covers a mountain basin using multi-orbit optical imagery, radar, laser altimetry and GNSS control. Students track whether each measurement is a range, angle, intensity or inferred terrain variable. Develop a compact research plan with a clear inference target, observational geometry, sampling strategy, numerical cross-check and validation design. Present one figure that retains units and reference-frame metadata. Describe a case in which apparent agreement across measurements may still result from shared bias. What additional independent measurement would break that dependence?

The main theme is this: Satellite measurements are not maps by themselves. Platform ephemerides, timing, viewing geometry, radiometric calibration and retrieval algorithms transform electromagnetic observations into geophysical products. Their uncertainties differ by sensor and surface. Before using the unit result to guide a practical choice, ask whether the error bar reflects the true sources of uncertainty or only the variation inside a simplified numerical procedure. Define the population and period in which the conclusion is intended to hold. A consistent interpretation must remain intelligible without dependence on a proprietary figure or a hidden processing step.

