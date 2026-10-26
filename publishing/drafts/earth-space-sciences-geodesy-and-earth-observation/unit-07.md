# Unit 7: Earth Observation Retrievals and Surface Mapping

## Guiding problem

How do reflected, emitted and returned signals become defensible estimates of environmental conditions?

**Fictional investigation:** A fictional coastal catchment has two optical images, an interferometric radar pair, an altimetry crossing and limited field observations. Students design change maps while keeping sensor physics and ground reference independent.

## Scientific scope

Remote sensing retrievals infer surface properties from sensor measurements that are influenced by illumination, atmosphere, geometry, surface composition and time. A useful retrieval requires calibration, correction and validation rather than only a plausible color display. Whenever positions, ranges, elevations or images are compared, uncertainty must be attached to a specified measurand and an explicitly identified reference. The word accurate is incomplete unless the reader can state accurate relative to what, over which interval and for which population of conditions. A local fit may be adequate for instruction without being an operationally defensible geodetic product.

## Unit practical: Sensor comparison design

Select complementary optical, radar, altimetry and GNSS observations for a fictional environmental target. Require common geolocation metadata and non-overlapping validation points.

Quantify which claimed changes are actually observable: optical indices follow spectral contrasts, radar phase follows line-of-sight motion, and altimetry follows travel-time range.

Avoid substituting high-resolution appearance for causal understanding when combining sensors.

## Data notebook requirements

Create a plain-text notebook containing input columns, units, a source/provenance statement, treatment of missing records, computational steps and at least one independent check. All datasets in this unit are manufactured for learning rather than sampled from nature. When reporting an estimated number, write out the assumptions connecting the number with the claimed physical variable. Note whether uncertainty is random, systematic or model-based. Provide a short explanation of what the number *cannot* tell us. The purpose is to practice disciplined geodetic reasoning as well as numerical computation.

## Lesson 7.1: Radiometric calibration and atmosphere

### Physical model and vocabulary

Raw instrument digital numbers are not equivalent to calibrated physical radiance or land-surface reflectance. Conversion depends on sensor gain, offsets, acquisition geometry, atmospheric scattering and absorption. A useful physical statement explicitly identifies the quantity being observed, the idealizations needed to interpret it, and at least one phenomenon excluded by the model. Write a small equation or a structured dependency diagram before processing numbers. If two physical mechanisms can generate the same measurement, the inverse problem is not unique without a further constraint. The correct level of modeling depends on the consequence of the intended decision; an approximation acceptable in a classroom is not automatically acceptable in cadastral surveying, flood warnings or infrastructure monitoring.

### Observation design and instrumentation

Compare fictional top-of-atmosphere measurements with corrected reflectances under two aerosol conditions and evaluate sensitivity to cloud-adjacent pixels. For this lesson, use the following common unit protocol as an explicit checklist: Select complementary optical, radar, altimetry and GNSS observations for a fictional environmental target. Require common geolocation metadata and non-overlapping validation points. Record the raw observable, its units, its collection conditions and any correction applied before deriving the displayed result. Distinguish a physically measured range, image intensity or height difference from a parameter that software estimated after applying assumptions. The same nominal output may be produced by different measurement procedures with different covariance and failure modes. Create a versioned log of those differences before comparing datasets.

### Worked numerical case 7.1: Normalized spectral index

**Given:** 0.31 near-infrared reflectance. **Calculation rule:** Surface NIR reflectance and fixed red reflectance of 0.12 in normalized difference. **Computed result:** 0.44186 NDVI. Report enough significant digits to show the underlying arithmetic, but do not claim that all displayed digits are measured information. The worked quantity is hypothetical and intentionally idealized. Recalculate it using original units rather than mentally switching between millimeters, meters, kilometers and degrees. Then double-check dimensions and evaluate whether a physically reasonable change in input produces the expected direction of change.

**Sensitivity test.** Rerun the given calculation with a modestly changed input, preferably increasing the magnitude by ten percent while keeping all other assumptions fixed. Describe both the absolute and relative output change. This isolates sensitivity to one variable only; it is not a total uncertainty budget. If a source has correlated errors, do not combine them with independent-error root-sum-of-squares unless independence is justified. A credible interpretation explains which input is a field observation, which is a normative constant and which is a teaching assumption.

### Confounding and alternative explanation

**Frequent mistake:** A difference in raw brightness between dates may reflect atmosphere or Sun angle rather than vegetation or land-cover change. Quantify which claimed changes are actually observable: optical indices follow spectral contrasts, radar phase follows line-of-sight motion, and altimetry follows travel-time range. Construct a competing explanation and decide which new observation would discriminate between the two. Avoid evaluating success by how smooth a graphic looks. Negative controls, repeated occupations, held-out locations and cross-sensor checks can be more informative than extra decimals. Classify each candidate error as one of reference mismatch, geometry, calibration, atmospheric or environmental variability, temporal sampling or inference-model misspecification. Explain why that distinction matters for the specific conclusion being attempted.

### Applied case and decision quality

Specify the preprocessing steps required before using an optical image in a drought assessment. Avoid substituting high-resolution appearance for causal understanding when combining sensors. In your written response, first state the decision being supported. Then give a physically meaningful result with units and coordinate conventions. Follow it with the strongest alternative explanation and an observation that could overturn your current interpretation. If uncertainty overlaps the stakeholder threshold, report that ambiguity rather than assigning unwarranted confidence to either choice. This discipline connects a numerical model to a traceable claim about the world.

### Guided questions and independent exercise

1. Which variables in this lesson are directly observed, and which are inferred after applying a physical model? Give the relevant units and reference conventions.
2. Recalculate the worked case after changing the controlling input by 10%; explain the direction of the resulting change and what assumption remained fixed.
3. Explain why the following pitfall matters for the current scientific claim: A difference in raw brightness between dates may reflect atmosphere or Sun angle rather than vegetation or land-cover change.
4. Propose one independent measurement or hold-out test that could reveal a systematic error not visible in the original calculation.
5. Write a three-sentence risk statement separating the demonstrated calculation from an application it is not qualified to support.

## Lesson 7.2: Vegetation and water spectral indices

### Physical model and vocabulary

A normalized two-band ratio such as NDVI summarizes spectral contrast; it is not a direct measurement of biomass, forest health or crop yield. Water indices have different assumptions and may confuse wet soil and shadows. A useful physical statement explicitly identifies the quantity being observed, the idealizations needed to interpret it, and at least one phenomenon excluded by the model. Write a small equation or a structured dependency diagram before processing numbers. If two physical mechanisms can generate the same measurement, the inverse problem is not unique without a further constraint. The correct level of modeling depends on the consequence of the intended decision; an approximation acceptable in a classroom is not automatically acceptable in cadastral surveying, flood warnings or infrastructure monitoring.

### Observation design and instrumentation

Compute indices from synthetic red and near-infrared values and compare a vegetated field with water, bare soil and a cloud-shadow pixel using quality masks. For this lesson, use the following common unit protocol as an explicit checklist: Select complementary optical, radar, altimetry and GNSS observations for a fictional environmental target. Require common geolocation metadata and non-overlapping validation points. Record the raw observable, its units, its collection conditions and any correction applied before deriving the displayed result. Distinguish a physically measured range, image intensity or height difference from a parameter that software estimated after applying assumptions. The same nominal output may be produced by different measurement procedures with different covariance and failure modes. Create a versioned log of those differences before comparing datasets.

### Worked numerical case 7.2: Radiance gain calibration

**Given:** 132 digital number. **Calculation rule:** Simplified L=0.0075 DN+0.1 sensor calibration, purely fictional coefficients. **Computed result:** 1.09 W/(m² sr μm). Report enough significant digits to show the underlying arithmetic, but do not claim that all displayed digits are measured information. The worked quantity is hypothetical and intentionally idealized. Recalculate it using original units rather than mentally switching between millimeters, meters, kilometers and degrees. Then double-check dimensions and evaluate whether a physically reasonable change in input produces the expected direction of change.

**Sensitivity test.** Rerun the given calculation with a modestly changed input, preferably increasing the magnitude by ten percent while keeping all other assumptions fixed. Describe both the absolute and relative output change. This isolates sensitivity to one variable only; it is not a total uncertainty budget. If a source has correlated errors, do not combine them with independent-error root-sum-of-squares unless independence is justified. A credible interpretation explains which input is a field observation, which is a normative constant and which is a teaching assumption.

### Confounding and alternative explanation

**Frequent mistake:** Index saturation, soil background and atmospheric correction can produce very different biophysical interpretations at equal index values. Quantify which claimed changes are actually observable: optical indices follow spectral contrasts, radar phase follows line-of-sight motion, and altimetry follows travel-time range. Construct a competing explanation and decide which new observation would discriminate between the two. Avoid evaluating success by how smooth a graphic looks. Negative controls, repeated occupations, held-out locations and cross-sensor checks can be more informative than extra decimals. Classify each candidate error as one of reference mismatch, geometry, calibration, atmospheric or environmental variability, temporal sampling or inference-model misspecification. Explain why that distinction matters for the specific conclusion being attempted.

### Applied case and decision quality

Choose a field-validation design for crop classification across irrigation seasons. Avoid substituting high-resolution appearance for causal understanding when combining sensors. In your written response, first state the decision being supported. Then give a physically meaningful result with units and coordinate conventions. Follow it with the strongest alternative explanation and an observation that could overturn your current interpretation. If uncertainty overlaps the stakeholder threshold, report that ambiguity rather than assigning unwarranted confidence to either choice. This discipline connects a numerical model to a traceable claim about the world.

### Guided questions and independent exercise

1. Which variables in this lesson are directly observed, and which are inferred after applying a physical model? Give the relevant units and reference conventions.
2. Recalculate the worked case after changing the controlling input by 10%; explain the direction of the resulting change and what assumption remained fixed.
3. Explain why the following pitfall matters for the current scientific claim: Index saturation, soil background and atmospheric correction can produce very different biophysical interpretations at equal index values.
4. Propose one independent measurement or hold-out test that could reveal a systematic error not visible in the original calculation.
5. Write a three-sentence risk statement separating the demonstrated calculation from an application it is not qualified to support.

## Lesson 7.3: SAR coherence and radar phase

### Physical model and vocabulary

Complex radar acquisitions allow interferometric comparison when acquisition geometry and scattering remain sufficiently consistent. Phase difference contains contributions from displacement, topography, atmosphere and orbital modeling. A useful physical statement explicitly identifies the quantity being observed, the idealizations needed to interpret it, and at least one phenomenon excluded by the model. Write a small equation or a structured dependency diagram before processing numbers. If two physical mechanisms can generate the same measurement, the inverse problem is not unique without a further constraint. The correct level of modeling depends on the consequence of the intended decision; an approximation acceptable in a classroom is not automatically acceptable in cadastral surveying, flood warnings or infrastructure monitoring.

### Observation design and instrumentation

Analyze a synthetic radar phase pair with masks for layover and decorrelation; convert unwrapped phase to an illustrative range change only after checking geometry. For this lesson, use the following common unit protocol as an explicit checklist: Select complementary optical, radar, altimetry and GNSS observations for a fictional environmental target. Require common geolocation metadata and non-overlapping validation points. Record the raw observable, its units, its collection conditions and any correction applied before deriving the displayed result. Distinguish a physically measured range, image intensity or height difference from a parameter that software estimated after applying assumptions. The same nominal output may be produced by different measurement procedures with different covariance and failure modes. Create a versioned log of those differences before comparing datasets.

### Worked numerical case 7.3: Radar phase-to-LOS range

**Given:** 1.2 rad unwrapped phase. **Calculation rule:** Unwrapped phase gives λφ/(4π), λ=5.6 cm, sign convention specified. **Computed result:** 0.534761 cm. Report enough significant digits to show the underlying arithmetic, but do not claim that all displayed digits are measured information. The worked quantity is hypothetical and intentionally idealized. Recalculate it using original units rather than mentally switching between millimeters, meters, kilometers and degrees. Then double-check dimensions and evaluate whether a physically reasonable change in input produces the expected direction of change.

**Sensitivity test.** Rerun the given calculation with a modestly changed input, preferably increasing the magnitude by ten percent while keeping all other assumptions fixed. Describe both the absolute and relative output change. This isolates sensitivity to one variable only; it is not a total uncertainty budget. If a source has correlated errors, do not combine them with independent-error root-sum-of-squares unless independence is justified. A credible interpretation explains which input is a field observation, which is a normative constant and which is a teaching assumption.

### Confounding and alternative explanation

**Frequent mistake:** The radar phase sign convention and spatial unwrapping are indispensable; treating wrapped phase as a unique displacement is invalid. Quantify which claimed changes are actually observable: optical indices follow spectral contrasts, radar phase follows line-of-sight motion, and altimetry follows travel-time range. Construct a competing explanation and decide which new observation would discriminate between the two. Avoid evaluating success by how smooth a graphic looks. Negative controls, repeated occupations, held-out locations and cross-sensor checks can be more informative than extra decimals. Classify each candidate error as one of reference mismatch, geometry, calibration, atmospheric or environmental variability, temporal sampling or inference-model misspecification. Explain why that distinction matters for the specific conclusion being attempted.

### Applied case and decision quality

Determine which complementary GNSS observations would constrain an urban subsidence signal. Avoid substituting high-resolution appearance for causal understanding when combining sensors. In your written response, first state the decision being supported. Then give a physically meaningful result with units and coordinate conventions. Follow it with the strongest alternative explanation and an observation that could overturn your current interpretation. If uncertainty overlaps the stakeholder threshold, report that ambiguity rather than assigning unwarranted confidence to either choice. This discipline connects a numerical model to a traceable claim about the world.

### Guided questions and independent exercise

1. Which variables in this lesson are directly observed, and which are inferred after applying a physical model? Give the relevant units and reference conventions.
2. Recalculate the worked case after changing the controlling input by 10%; explain the direction of the resulting change and what assumption remained fixed.
3. Explain why the following pitfall matters for the current scientific claim: The radar phase sign convention and spatial unwrapping are indispensable; treating wrapped phase as a unique displacement is invalid.
4. Propose one independent measurement or hold-out test that could reveal a systematic error not visible in the original calculation.
5. Write a three-sentence risk statement separating the demonstrated calculation from an application it is not qualified to support.

## Lesson 7.4: Altimetry and water or ice elevation

### Physical model and vocabulary

Microwave and laser altimeters estimate range to a reflecting surface, with inferred elevation depending on satellite orbit and corrections. Retracking and mixed footprints matter along coastlines and steep terrain. A useful physical statement explicitly identifies the quantity being observed, the idealizations needed to interpret it, and at least one phenomenon excluded by the model. Write a small equation or a structured dependency diagram before processing numbers. If two physical mechanisms can generate the same measurement, the inverse problem is not unique without a further constraint. The correct level of modeling depends on the consequence of the intended decision; an approximation acceptable in a classroom is not automatically acceptable in cadastral surveying, flood warnings or infrastructure monitoring.

### Observation design and instrumentation

Create a synthetic reservoir transect showing how footprint mixing influences returned range; compare repeat heights after making tidal and atmosphere corrections explicit. For this lesson, use the following common unit protocol as an explicit checklist: Select complementary optical, radar, altimetry and GNSS observations for a fictional environmental target. Require common geolocation metadata and non-overlapping validation points. Record the raw observable, its units, its collection conditions and any correction applied before deriving the displayed result. Distinguish a physically measured range, image intensity or height difference from a parameter that software estimated after applying assumptions. The same nominal output may be produced by different measurement procedures with different covariance and failure modes. Create a versioned log of those differences before comparing datasets.

### Worked numerical case 7.4: Altimeter range residual

**Given:** 699.62 km measured range. **Calculation rule:** A simple 700 km nominal orbit minus instrument range, with corrections omitted. **Computed result:** 380 m. Report enough significant digits to show the underlying arithmetic, but do not claim that all displayed digits are measured information. The worked quantity is hypothetical and intentionally idealized. Recalculate it using original units rather than mentally switching between millimeters, meters, kilometers and degrees. Then double-check dimensions and evaluate whether a physically reasonable change in input produces the expected direction of change.

**Sensitivity test.** Rerun the given calculation with a modestly changed input, preferably increasing the magnitude by ten percent while keeping all other assumptions fixed. Describe both the absolute and relative output change. This isolates sensitivity to one variable only; it is not a total uncertainty budget. If a source has correlated errors, do not combine them with independent-error root-sum-of-squares unless independence is justified. A credible interpretation explains which input is a field observation, which is a normative constant and which is a teaching assumption.

### Confounding and alternative explanation

**Frequent mistake:** A radar return from an ice shelf or coastal water surface need not represent the same physical feature on repeated overpasses. Quantify which claimed changes are actually observable: optical indices follow spectral contrasts, radar phase follows line-of-sight motion, and altimetry follows travel-time range. Construct a competing explanation and decide which new observation would discriminate between the two. Avoid evaluating success by how smooth a graphic looks. Negative controls, repeated occupations, held-out locations and cross-sensor checks can be more informative than extra decimals. Classify each candidate error as one of reference mismatch, geometry, calibration, atmospheric or environmental variability, temporal sampling or inference-model misspecification. Explain why that distinction matters for the specific conclusion being attempted.

### Applied case and decision quality

Evaluate the detectability of seasonal water-level changes with repeat altimetry and field gauge data. Avoid substituting high-resolution appearance for causal understanding when combining sensors. In your written response, first state the decision being supported. Then give a physically meaningful result with units and coordinate conventions. Follow it with the strongest alternative explanation and an observation that could overturn your current interpretation. If uncertainty overlaps the stakeholder threshold, report that ambiguity rather than assigning unwarranted confidence to either choice. This discipline connects a numerical model to a traceable claim about the world.

### Guided questions and independent exercise

1. Which variables in this lesson are directly observed, and which are inferred after applying a physical model? Give the relevant units and reference conventions.
2. Recalculate the worked case after changing the controlling input by 10%; explain the direction of the resulting change and what assumption remained fixed.
3. Explain why the following pitfall matters for the current scientific claim: A radar return from an ice shelf or coastal water surface need not represent the same physical feature on repeated overpasses.
4. Propose one independent measurement or hold-out test that could reveal a systematic error not visible in the original calculation.
5. Write a three-sentence risk statement separating the demonstrated calculation from an application it is not qualified to support.

## Lesson 7.5: Retrieval validation and spatial support

### Physical model and vocabulary

Classification maps, elevation models and deformation products have distinct spatial resolution, effective support and correlated errors. Independent field samples are essential for accuracy statements. A useful physical statement explicitly identifies the quantity being observed, the idealizations needed to interpret it, and at least one phenomenon excluded by the model. Write a small equation or a structured dependency diagram before processing numbers. If two physical mechanisms can generate the same measurement, the inverse problem is not unique without a further constraint. The correct level of modeling depends on the consequence of the intended decision; an approximation acceptable in a classroom is not automatically acceptable in cadastral surveying, flood warnings or infrastructure monitoring.

### Observation design and instrumentation

Stratify fictional validation points across land-cover classes and coast-distance bands; compute class-specific failures and map where uncertainty is greatest. For this lesson, use the following common unit protocol as an explicit checklist: Select complementary optical, radar, altimetry and GNSS observations for a fictional environmental target. Require common geolocation metadata and non-overlapping validation points. Record the raw observable, its units, its collection conditions and any correction applied before deriving the displayed result. Distinguish a physically measured range, image intensity or height difference from a parameter that software estimated after applying assumptions. The same nominal output may be produced by different measurement procedures with different covariance and failure modes. Create a versioned log of those differences before comparing datasets.

### Worked numerical case 7.5: Validation accuracy

**Given:** 77 correct classifications. **Calculation rule:** Synthetic independent set of 100 image pixels; overall accuracy=correct/total. **Computed result:** 0.77 fraction. Report enough significant digits to show the underlying arithmetic, but do not claim that all displayed digits are measured information. The worked quantity is hypothetical and intentionally idealized. Recalculate it using original units rather than mentally switching between millimeters, meters, kilometers and degrees. Then double-check dimensions and evaluate whether a physically reasonable change in input produces the expected direction of change.

**Sensitivity test.** Rerun the given calculation with a modestly changed input, preferably increasing the magnitude by ten percent while keeping all other assumptions fixed. Describe both the absolute and relative output change. This isolates sensitivity to one variable only; it is not a total uncertainty budget. If a source has correlated errors, do not combine them with independent-error root-sum-of-squares unless independence is justified. A credible interpretation explains which input is a field observation, which is a normative constant and which is a teaching assumption.

### Confounding and alternative explanation

**Frequent mistake:** Pixel agreement against data used for training, co-registration or calibration is not independent validation. Quantify which claimed changes are actually observable: optical indices follow spectral contrasts, radar phase follows line-of-sight motion, and altimetry follows travel-time range. Construct a competing explanation and decide which new observation would discriminate between the two. Avoid evaluating success by how smooth a graphic looks. Negative controls, repeated occupations, held-out locations and cross-sensor checks can be more informative than extra decimals. Classify each candidate error as one of reference mismatch, geometry, calibration, atmospheric or environmental variability, temporal sampling or inference-model misspecification. Explain why that distinction matters for the specific conclusion being attempted.

### Applied case and decision quality

Design an auditable satellite-derived land-change product with a stated resolution, uncertainty and temporal domain. Avoid substituting high-resolution appearance for causal understanding when combining sensors. In your written response, first state the decision being supported. Then give a physically meaningful result with units and coordinate conventions. Follow it with the strongest alternative explanation and an observation that could overturn your current interpretation. If uncertainty overlaps the stakeholder threshold, report that ambiguity rather than assigning unwarranted confidence to either choice. This discipline connects a numerical model to a traceable claim about the world.

### Guided questions and independent exercise

1. Which variables in this lesson are directly observed, and which are inferred after applying a physical model? Give the relevant units and reference conventions.
2. Recalculate the worked case after changing the controlling input by 10%; explain the direction of the resulting change and what assumption remained fixed.
3. Explain why the following pitfall matters for the current scientific claim: Pixel agreement against data used for training, co-registration or calibration is not independent validation.
4. Propose one independent measurement or hold-out test that could reveal a systematic error not visible in the original calculation.
5. Write a three-sentence risk statement separating the demonstrated calculation from an application it is not qualified to support.

## Unit synthesis and interpretive assessment

A fictional coastal catchment has two optical images, an interferometric radar pair, an altimetry crossing and limited field observations. Students design change maps while keeping sensor physics and ground reference independent. Develop a compact research plan with a clear inference target, observational geometry, sampling strategy, numerical cross-check and validation design. Present one figure that retains units and reference-frame metadata. Describe a case in which apparent agreement across measurements may still result from shared bias. What additional independent measurement would break that dependence?

The main theme is this: Remote sensing retrievals infer surface properties from sensor measurements that are influenced by illumination, atmosphere, geometry, surface composition and time. A useful retrieval requires calibration, correction and validation rather than only a plausible color display. Before using the unit result to guide a practical choice, ask whether the error bar reflects the true sources of uncertainty or only the variation inside a simplified numerical procedure. Define the population and period in which the conclusion is intended to hold. A consistent interpretation must remain intelligible without dependence on a proprietary figure or a hidden processing step.

