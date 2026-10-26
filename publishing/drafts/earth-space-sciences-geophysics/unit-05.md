# Unit 5: Magnetics and paleomagnetic inference

## Central question: How do induced and remanent magnetization affect crustal magnetic anomalies?

**Fictional unit investigation:** A fictitious basalt terrain contains dikes, remanence directions and a slow-changing regional field. Learners compare corrected anomaly profiles and ask whether variations reflect susceptibility, depth, direction or acquisition artefacts.

## Geophysical foundation and the measurement-to-model chain

The measured total magnetic field combines core field, time-dependent external contributions and crustal magnetization. Rock response includes induced magnetization proportional to susceptibility and, in many rocks, remanent magnetization that can dominate or oppose the induced component. Reduction to pole, continuation and derivative transformations depend on assumptions and can amplify noise. Diurnal basestation corrections and position control are necessary before geological interpretation. Polarity patterns support tectonic reconstructions only when the relevant age and magnetization history is independently justified. The reference model removes a major-scale field, not all environmental interference or crustal complexity.

## Five lessons: hypotheses, observables and field checks

For each lesson the forward physics and observation type are explicit. The lesson is complete only when the student can name a competing explanation, check units in the worked calculation and explain a measurement that could reject the preferred interpretation. Every stated numerical value is invented for this textbook; none is a field station or an operational parameter.

## Lesson 5.1: Geomagnetic field components and reference frames

### The physical mechanism and its measurable consequence

Earth's main magnetic field changes with position and time; inclination, declination and vector components follow a defined coordinate convention. A reference model is appropriate for particular epochs and purposes, not a universal correction for local crustal anomalies.

### Acquisition protocol and observable variables

Record location, date, height, heading, sensor orientation, total intensity and whether a reference model was used. Verify magnetic units nT and angular convention.

### The inverse ambiguity: alternative explanations

A field change caused by temporal external activity can be misidentified as a lithologic anomaly; heading errors also create spurious gradients.

### Worked calculation: synthetic classroom data

**Question — Magnetic angle.** Given north component 20,000 nT and east component 5,000 nT; compute horizontal azimuth in degrees.

**Explicit computation:** `math.degrees(math.atan2(5000,20000))` = **14.03624 degrees**. Express the result in the units requested; perform any conversion before substituting into the equation rather than concealing a factor of one thousand in a final sentence. A rounded answer should not imply accuracy better than the synthetic inputs. This arithmetic operation provides a physical scale, not a certified subsurface interpretation.

**Why the calculation matters.** Declination direction follows the stated coordinate convention. **Boundary of validity:** Not a substitute for up-to-date local geomagnetic modelling. For an independent sensitivity check, change one stated input by ten percent, leaving others fixed. Explain how the result responds, and whether a plausible alternative hypothesis could produce the same scalar.

### Practical: an observation that could disprove the preferred model

Compare a survey loop before and after time-base-station correction while retaining a record of the removed signal.

**Competing models.** Choose two different geologic or instrumental explanations for the observation and write one numerical or spatial prediction on which they disagree. Reserve a new observation as a prospective test. Draw a table containing at least two testable predictions, the needed instrument reading, its physical units, and one reason the observation might be biased.

### Analysis note: how to decide whether the interpretation survives

**Inspect the observation footprint.** Ask which wavelengths and parts of the Earth contribute to the instrument. Potential fields integrate over substantial volumes, seismic picks follow ray paths and electrode arrays have diffuse sensitivity; a pixel-sized interpretation usually exceeds the resolving claim. In the context of **geomagnetic field components and reference frames**, explain what a reviewer should expect to see in raw data if the mechanism is credible, and what unexpected pattern would require a revised geological model.

### Synthesis and interpretation checkpoint

Write a short technical conclusion that separates three items: (1) what the instrument directly records in the magnetics and paleomagnetic inference problem; (2) the material property or process inferred from it; and (3) a geological claim that would still be unsupported. The exercise is not passed merely by obtaining 14.03624 degrees. Explain why the uncertainty in the assumptions can exceed calculator precision and identify a discriminating field observation.

## Lesson 5.2: Magnetic susceptibility and remanence

### The physical mechanism and its measurable consequence

Induced magnetization responds to applied field and magnetic susceptibility, but remanent magnetization records geological history and may not align with today's inducing field. Total magnetization can differ in direction and magnitude from the induced part.

### Acquisition protocol and observable variables

Measure bulk susceptibility and, where possible, oriented laboratory natural remanent magnetization. Combine vector data with field anomalies.

### The inverse ambiguity: alternative explanations

A low susceptibility rock can produce a strong anomaly because of remanence; an anomaly sign does not directly identify polarity or depth.

### Worked calculation: synthetic classroom data

**Question — Induced magnetization.** Assume dimensionless susceptibility 0.02 and H=40 A/m; compute induced magnetization M=kH.

**Explicit computation:** `0.02*40` = **0.8 A/m**. Express the result in the units requested; perform any conversion before substituting into the equation rather than concealing a factor of one thousand in a final sentence. A rounded answer should not imply accuracy better than the synthetic inputs. This arithmetic operation provides a physical scale, not a certified subsurface interpretation.

**Why the calculation matters.** Ideal isotropic linear induced response. **Boundary of validity:** Remanence may dominate the actual total magnetization. For an independent sensitivity check, change one stated input by ten percent, leaving others fixed. Explain how the result responds, and whether a plausible alternative hypothesis could produce the same scalar.

### Practical: an observation that could disprove the preferred model

Construct two equally strong dipoles with opposed directions and compare anomaly profiles along and across strike.

**Error budget.** Separate repeatability, calibration bias, position error and model uncertainty in a table with units. Decide which uncertainty dominates the interpretation and what extra information would shrink it. Draw a table containing at least two testable predictions, the needed instrument reading, its physical units, and one reason the observation might be biased.

### Analysis note: how to decide whether the interpretation survives

**State the forward equation and its domain.** Write the physical equation together with geometry, units and assumed constants. List a realistic departure that changes the prediction and distinguish a useful approximation from an unjustified physical claim. In the context of **magnetic susceptibility and remanence**, explain what a reviewer should expect to see in raw data if the mechanism is credible, and what unexpected pattern would require a revised geological model.

### Synthesis and interpretation checkpoint

Write a short technical conclusion that separates three items: (1) what the instrument directly records in the magnetics and paleomagnetic inference problem; (2) the material property or process inferred from it; and (3) a geological claim that would still be unsupported. The exercise is not passed merely by obtaining 0.8 A/m. Explain why the uncertainty in the assumptions can exceed calculator precision and identify a discriminating field observation.

## Lesson 5.3: Magnetic anomaly filtering and continuation

### The physical mechanism and its measurable consequence

Magnetic analytical signal, derivatives and continuation are transformations that emphasize different spatial scales. Low-altitude surveys are more sensitive to shallow bodies but also to cultural noise. Filtering can enhance lineaments while obscuring source depth information.

### Acquisition protocol and observable variables

Document flight or walk height, traverse direction, tie-line correction, diurnal correction and gridding parameters. Examine a profile before and after filtering.

### The inverse ambiguity: alternative explanations

A derivative peak may shift relative to its geological source; reduction to pole can be unstable at low magnetic inclinations under certain methods.

### Worked calculation: synthetic classroom data

**Question — Altitude effect.** An anomaly is 90 nT at 100 m height and an ideal dipole response scales as r^-3; estimate at 200 m.

**Explicit computation:** `90*(100/200)**3` = **11.25 nT**. Express the result in the units requested; perform any conversion before substituting into the equation rather than concealing a factor of one thousand in a final sentence. A rounded answer should not imply accuracy better than the synthetic inputs. This arithmetic operation provides a physical scale, not a certified subsurface interpretation.

**Why the calculation matters.** The rapid depth decay is a useful idealization. **Boundary of validity:** Altitude is not generally total dipole distance. For an independent sensitivity check, change one stated input by ten percent, leaving others fixed. Explain how the result responds, and whether a plausible alternative hypothesis could produce the same scalar.

### Practical: an observation that could disprove the preferred model

Design a crossing-line test where a supposed dike anomaly persists after independent gridding directions.

**Sensitivity study.** Alter the assumed physical-property contrast, source depth or acquisition spacing. Determine whether the sign of the conclusion persists or whether the interpretation is contingent on a narrow prior. Draw a table containing at least two testable predictions, the needed instrument reading, its physical units, and one reason the observation might be biased.

### Analysis note: how to decide whether the interpretation survives

**Decide a safe intended use.** Clarify whether the result is a numerical exercise, exploratory screening, academic interpretation or professional decision product. Educational calculations do not confer authority to make engineering, emergency or environmental determinations. In the context of **magnetic anomaly filtering and continuation**, explain what a reviewer should expect to see in raw data if the mechanism is credible, and what unexpected pattern would require a revised geological model.

### Synthesis and interpretation checkpoint

Write a short technical conclusion that separates three items: (1) what the instrument directly records in the magnetics and paleomagnetic inference problem; (2) the material property or process inferred from it; and (3) a geological claim that would still be unsupported. The exercise is not passed merely by obtaining 11.25 nT. Explain why the uncertainty in the assumptions can exceed calculator precision and identify a discriminating field observation.

## Lesson 5.4: Magnetostratigraphy and paleomagnetic directions

### The physical mechanism and its measurable consequence

Magnetic minerals may acquire thermoremanent, detrital or chemical remanence at different geological times. Stepwise demagnetization separates some components, but overprinting, inclination shallowing and structural rotation alter observed directions. Reversal correlations require reliable chronology.

### Acquisition protocol and observable variables

Collect oriented samples with bedding attitude, laboratory demagnetization path and uncertainty cones. Compare polarity transitions with independent stratigraphic ages.

### The inverse ambiguity: alternative explanations

A polarity sequence may be remagnetized or miscorrelated if the record is incomplete; a strong component is not automatically primary.

### Worked calculation: synthetic classroom data

**Question — Ages and reversal bands.** A 72 km half-spreading distance formed over 3 Ma; compute half rate in km/Ma.

**Explicit computation:** `72/3` = **24 km/Ma**. Express the result in the units requested; perform any conversion before substituting into the equation rather than concealing a factor of one thousand in a final sentence. A rounded answer should not imply accuracy better than the synthetic inputs. This arithmetic operation provides a physical scale, not a certified subsurface interpretation.

**Why the calculation matters.** Distance divided by age gives an interval average. **Boundary of validity:** Field polarity correlation and age uncertainties omitted. For an independent sensitivity check, change one stated input by ten percent, leaving others fixed. Explain how the result responds, and whether a plausible alternative hypothesis could produce the same scalar.

### Practical: an observation that could disprove the preferred model

Construct an age–polarity diagram with an unrecognized hiatus, then find which independent date reveals the wrong correlation.

**Blind crosscheck.** Give the input series and quality flags to another analyst while hiding the preferred interpretation. Compare their residual and inferred structure with the original and preserve genuine disagreements. Draw a table containing at least two testable predictions, the needed instrument reading, its physical units, and one reason the observation might be biased.

### Analysis note: how to decide whether the interpretation survives

**Track the reference frame.** Coordinates, vertical datums, event origin times, magnetic epochs and polarity conventions are parts of the measurement. Confusing reference frames can shift all stations coherently without producing conspicuous random residuals. In the context of **magnetostratigraphy and paleomagnetic directions**, explain what a reviewer should expect to see in raw data if the mechanism is credible, and what unexpected pattern would require a revised geological model.

### Synthesis and interpretation checkpoint

Write a short technical conclusion that separates three items: (1) what the instrument directly records in the magnetics and paleomagnetic inference problem; (2) the material property or process inferred from it; and (3) a geological claim that would still be unsupported. The exercise is not passed merely by obtaining 24 km/Ma. Explain why the uncertainty in the assumptions can exceed calculator precision and identify a discriminating field observation.

## Lesson 5.5: Integrating magnetics with geology

### The physical mechanism and its measurable consequence

A magnetic lineament can map an intrusive contact, fault offset, alteration boundary or man-made object. The geophysical response measures magnetization contrast rather than rock identity. Survey interpretation improves with structural and geochemical tests.

### Acquisition protocol and observable variables

Compare magnetic strikes with mapped dike traces, cross-cutting relations and samples. Distinguish field observations from lineaments traced only on imagery.

### The inverse ambiguity: alternative explanations

Two parallel magnetic highs may reflect separate bodies, induced field geometry or remanence rotation. Fault displacement inferred from a single magnetic image is uncertain.

### Worked calculation: synthetic classroom data

**Question — Magnetic anomaly magnitude.** Observed total field 48,300 nT, reference model 47,950 nT; find residual.

**Explicit computation:** `48300-47950` = **350 nT**. Express the result in the units requested; perform any conversion before substituting into the equation rather than concealing a factor of one thousand in a final sentence. A rounded answer should not imply accuracy better than the synthetic inputs. This arithmetic operation provides a physical scale, not a certified subsurface interpretation.

**Why the calculation matters.** Difference is not necessarily all crustal magnetism. **Boundary of validity:** Temporal external and instrumental effects remain. For an independent sensitivity check, change one stated input by ten percent, leaving others fixed. Explain how the result responds, and whether a plausible alternative hypothesis could produce the same scalar.

### Practical: an observation that could disprove the preferred model

Rank three possible trench locations by predicted disagreement between magnetic and mapping hypotheses rather than anomaly amplitude alone.

**Instrument validation.** Compare a repeat transect, crossing line or reciprocal reading with original acquisition. Explain what kind of systematic effect the check is capable of detecting and what remains invisible. Draw a table containing at least two testable predictions, the needed instrument reading, its physical units, and one reason the observation might be biased.

### Analysis note: how to decide whether the interpretation survives

**Use a withheld test.** Fit the parameters with one subset and predict genuinely unobserved measurements. Spatial clustering, repeated use of validation stations or tuning after inspecting the holdout exaggerates predictive evidence. In the context of **integrating magnetics with geology**, explain what a reviewer should expect to see in raw data if the mechanism is credible, and what unexpected pattern would require a revised geological model.

### Synthesis and interpretation checkpoint

Write a short technical conclusion that separates three items: (1) what the instrument directly records in the magnetics and paleomagnetic inference problem; (2) the material property or process inferred from it; and (3) a geological claim that would still be unsupported. The exercise is not passed merely by obtaining 350 nT. Explain why the uncertainty in the assumptions can exceed calculator precision and identify a discriminating field observation.

## Research clinic — why magnetic highs are not always basalt

Magnetization combines induced response with remanence left by earlier thermal, depositional or chemical processes. In a hypothetical dike province, two bodies with similar magnetite abundance can generate different field shapes if their remanent vectors point in different directions. A strong positive total-field anomaly can also be changed by flight-line orientation, survey latitude and source geometry. Merely looking for magnetic highs may therefore misclassify lithology and structural position.

Start with the uncorrected total-field track and base-station record. Identify periods of external temporal variation, heading changes and crossing-line disagreement. Subtract an appropriate reference main-field model at the correct epoch and location, but remember that such a model does not remove all crustal or external contributions. A regional baseline and source rock magnetization are separate interpretive decisions. Maintain a record of each version rather than overwriting the measurements with the preferred anomaly grid.

Transformations such as upward continuation or gradient calculation clarify certain scales and suppress others. Upward continuation usually reduces short-wavelength effects but sacrifices shallow resolution. Derivatives highlight sharper contrasts while magnifying high-frequency noise. Reduction-to-pole style processing requires magnetic direction assumptions; it can behave poorly in some low-inclination contexts. Always compare a proposed geological lineament across raw and transformed maps and show where the interpretation is method-dependent.

Paleomagnetism adds time information but requires oriented specimens and a credible isolation of primary remanence. Structural rotation and later remagnetization can mimic changes in ancient field direction. A polarity band cannot be assigned to a specific reversal solely by matching stripe appearance; it also needs independent age controls and structural context. Students should label three separate claims in their report: current measured field anomaly, inferred rock magnetization, and historical reconstruction. These are distinct levels of evidence with distinct uncertainty.


## Unit investigation: reproducible synthetic dataset and experimental design

**Research aim.** The invented scenario is: A fictitious basalt terrain contains dikes, remanence directions and a slow-changing regional field. Learners compare corrected anomaly profiles and ask whether variations reflect susceptibility, depth, direction or acquisition artefacts. Treat `datasets/unit-05.csv` as forty fictional rows deliberately designed to exercise quality control and model criticism. Read the file header before drawing any map. Plot the two relevant measured fields from unit 5; display the `quality_flag` column rather than deleting all flagged stations silently. The synthetic table contains no geographic coordinate reference system or real site identifiers and cannot be used to identify a place.

**Part A — raw measurements and dimensions.** Read each column as a quantity, not as a decorative label. For magnetics and paleomagnetic inference, check whether the stated units are compatible with its equation and record which columns represent observed signals, instrument corrections, independent controls or model-derived quantities. Identify missing information such as date, site geology, true coordinate system, instrument orientation or calibration. If those omissions prevent a physical inversion, state the limitation and limit the task to transparent exploratory analysis. This is a stronger result than assigning fictitious precision.

**Part B — repeat and quality flags.** Count the rows marked `review`. Compare summary statistics, plotted gradients and model parameters with all forty records against the subset that passes the flag. Document every change; flags indicate inspection priority, not a universal mandate to delete. Check whether questionable values cluster along position or signal amplitude, because exclusions can introduce bias. If the noise appears correlated, do not assume a root-sum-square independent-error formula without a justification.

**Part C — model competition.** Describe two geophysical models that explain the synthetic observations in magnetics and paleomagnetic inference; they must differ in physical property, geometry or forcing rather than just parameter precision. For each hypothesis make an observable prediction about station response, uncertainty pattern, external control or independent method. Select one new measurement that would best discriminate them, and explain its predicted signal under both hypotheses. A new dense sample from the same short profile may add less independent information than a crossing line or sample.

**Part D — numerical sensitivity.** Recompute one of the unit worked cases with the principal input increased by 10% and decreased by 10%. Check if the response is linear, inverse, logarithmic, quadratic or subject to another nonlinearity. Show a table with input, computed output, unit and physical assumption. Do not claim a sensitivity of the geological interpretation itself if only the toy forward equation was changed; the inverse solution may have a much broader family of possibilities.

**Part E — out-of-sample prediction and reporting.** Split the synthetic observations by physical position, retaining a contiguous group as a blind holdout. Fit a deliberately simple forward trend to remaining rows and predict the held-out quantity without retuning. Compare predictive error with a baseline that uses a constant mean. State why geographic separation can be a stronger test than random point withholding. Report all transformations, quality flags, fitted parameters, residual plots and failure modes in a compact methods appendix.

**Unit-specific evidence synthesis.** The measured total magnetic field combines core field, time-dependent external contributions and crustal magnetization. Rock response includes induced magnetization proportional to susceptibility and, in many rocks, remanent magnetization that can dominate or oppose the induced component. Reduction to pole, continuation and derivative transformations depend on assumptions and can amplify noise. Diurnal basestation corrections and position control are necessary before geological interpretation. Polarity patterns support tectonic reconstructions only when the relevant age and magnetization history is independently justified. The reference model removes a major-scale field, not all environmental interference or crustal complexity. Map the chain of evidence from sensor to interpretation; highlight an uncertainty not reducible by extra decimal places. In your conclusion, indicate which measurement you would acquire next if the synthetic experiment were replaced with licensed real-world data. Keep any real data sourced from the references separate from these forty invented rows.

**Suggested report.** Submit a transparent CSV-reading script or spreadsheet calculation, one raw-data figure, a sensitivity plot, two candidate geological explanations, a withheld-test result and a one-page uncertainty ledger. Grade on conceptual correctness (25%), numerical units and reproducibility (25%), alternate hypotheses (20%), validation logic (20%) and scientific communication (10%). Never reward a map for appearing more certain than its underlying observations.

## End-of-unit reflection and problems

1. Identify which part of **magnetics and paleomagnetic inference** would remain ambiguous even if measurement noise were reduced to zero. Explain how the survey geometry or parameter relationship creates that ambiguity.

2. Find a case where a large change in the observed signal would not imply a proportionally large change in target size. Write the forward relation, name fixed parameters, and state why inversion differs from prediction.

3. Propose a new survey that would risk rejecting the preferred geological interpretation. Its value should be based on discriminating predictions rather than its technological sophistication.

4. Draw a data lineage chart from raw instrument data through correction, inversion and geological claim. Underline any operation that assumes a material property not measured in the original dataset.

5. Explain why the synthetic data and interactive sliders are educational examples and cannot support emergency warnings, ground-investigation certification, resource appraisal or environmental enforcement.

## Additional reading and independent replication

Use `REFERENCES.md` to find a genuine program or open repository relevant to magnetics and paleomagnetic inference. Before downloading any data, check the provider documentation, citation requirements, usage permissions and the time period represented. Record the instrument type, station metadata and acquisition geometry, then reproduce one simple physical calculation from scratch. The objective is not to match a published colored inversion image exactly; it is to understand the observable and give a defensible account of differences.


## Interactive physical-model explanations

Open this chapter in the HTML reader to change one controlled physical variable at a time. Each model is a simplified *forward* calculation, not an inversion or a real-world estimator.

### Induced magnetization

Input quantity: Magnetic field strength measured in A/m; demonstration range 0–70, initial setting 40. Output: A/m. Computed from `0.02*x`.

**Unmodelled influences and interpretation boundary:** Scalar susceptibility fixed at 0.02; remanence absent. Students should articulate a case where this formula yields a numerically precise but physically misleading answer and state an independently measurable quantity needed for a more complete model.

### Half-spreading distance

Input quantity: Duration measured in Ma; demonstration range 0–20, initial setting 3. Output: km. Computed from `24*x`.

**Unmodelled influences and interpretation boundary:** Fixed 24 km/Ma rate; no reversal-correlation error. Students should articulate a case where this formula yields a numerically precise but physically misleading answer and state an independently measurable quantity needed for a more complete model.
