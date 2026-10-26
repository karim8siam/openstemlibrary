# Unit 1: The inverse problem and geophysical observables

## Central question: How does a physical measurement constrain a geological model without uniquely determining it?

**Fictional unit investigation:** A fictional volcanic plateau is crossed by two short survey lines. Students receive elevation, instrument drift, measurement error and an incomplete geology map; they must distinguish response calibration from geological interpretation.

## Geophysical foundation and the measurement-to-model chain

Geophysics estimates otherwise inaccessible properties by measuring fields and wave responses at accessible positions. The forward problem predicts observations from a specified model; the inverse problem asks what models might produce an observation. Sources, material properties, sensor geometry, boundary conditions and noise all influence the prediction. A low-residual model is not automatically the only acceptable subsurface explanation. State which variables were observed, which were assumed and which were regularized. Resolution varies with sampling density, instrument bandwidth and model physics. A map pixel inherits assumptions from calibration and interpolation, not merely precision from its file format. A defensible interpretation predicts measurements at a location withheld from the inversion and makes alternatives visible.

## Five lessons: hypotheses, observables and field checks

For each lesson the forward physics and observation type are explicit. The lesson is complete only when the student can name a competing explanation, check units in the worked calculation and explain a measurement that could reject the preferred interpretation. Every stated numerical value is invented for this textbook; none is a field station or an operational parameter.

## Lesson 1.1: Signals, fields and measurement support

### The physical mechanism and its measurable consequence

A field survey samples a spatially varying physical quantity with sensors integrating over an actual footprint, orientation and time interval. Potential fields are different from ray travel times: they obey different superposition and depth-sensitivity rules. A geological target may affect multiple fields, but the responses need not be independent.

### Acquisition protocol and observable variables

Record location, height, coordinate datum, acquisition time, instrument orientation, bandwidth, calibration constant and line spacing. Compare point support with gridded or filtered support; examine raw values before interpolation.

### The inverse ambiguity: alternative explanations

A sensor drift may resemble a regional gradient; a high-pass filter may create paired positive and negative features. Two measurements collected by the same instrument may share systematic errors.

### Worked calculation: synthetic classroom data

**Question — Potential-field contrast.** Two gravity values are 9.8120 and 9.8123 m/s²; find their difference in mGal.

**Explicit computation:** `(9.8123-9.8120)*1e5` = **30 mGal**. Express the result in the units requested; perform any conversion before substituting into the equation rather than concealing a factor of one thousand in a final sentence. A rounded answer should not imply accuracy better than the synthetic inputs. This arithmetic operation provides a physical scale, not a certified subsurface interpretation.

**Why the calculation matters.** The difference is 30 mGal, not evidence of a particular body. **Boundary of validity:** Time, height, latitude and reduction errors have not been removed. For an independent sensitivity check, change one stated input by ten percent, leaving others fixed. Explain how the result responds, and whether a plausible alternative hypothesis could produce the same scalar.

### Practical: an observation that could disprove the preferred model

Design a two-day repeat survey and decide which field signatures are stable under changed temperature and instrument placement.

**Competing models.** Choose two different geologic or instrumental explanations for the observation and write one numerical or spatial prediction on which they disagree. Reserve a new observation as a prospective test. Draw a table containing at least two testable predictions, the needed instrument reading, its physical units, and one reason the observation might be biased.

### Analysis note: how to decide whether the interpretation survives

**Inspect the observation footprint.** Ask which wavelengths and parts of the Earth contribute to the instrument. Potential fields integrate over substantial volumes, seismic picks follow ray paths and electrode arrays have diffuse sensitivity; a pixel-sized interpretation usually exceeds the resolving claim. In the context of **signals, fields and measurement support**, explain what a reviewer should expect to see in raw data if the mechanism is credible, and what unexpected pattern would require a revised geological model.

### Synthesis and interpretation checkpoint

Write a short technical conclusion that separates three items: (1) what the instrument directly records in the the inverse problem and geophysical observables problem; (2) the material property or process inferred from it; and (3) a geological claim that would still be unsupported. The exercise is not passed merely by obtaining 30 mGal. Explain why the uncertainty in the assumptions can exceed calculator precision and identify a discriminating field observation.

## Lesson 1.2: Physical-property contrast and detectability

### The physical mechanism and its measurable consequence

Geophysical anomalies arise when a body changes wave speed, impedance, density, magnetization, conductivity or temperature relative to the surrounding medium. Detectability depends on contrast, dimensions, burial depth, source-receiver geometry and measurement noise. A missing anomaly does not prove a target is absent.

### Acquisition protocol and observable variables

Specify a plausible property range and forward-predict anomaly shapes for a small shallow and large deep candidate target. Test several instrument spacings and signal-to-noise levels.

### The inverse ambiguity: alternative explanations

A true property contrast can be undetectable because the survey lacks wavelength sensitivity. Conversely a shallow cultural object may dominate the natural geological response.

### Worked calculation: synthetic classroom data

**Question — Signal-to-noise.** A synthetic anomaly is 18 nT and one-sigma instrument noise is 3 nT; find amplitude-to-noise ratio.

**Explicit computation:** `18/3` = **6 ratio**. Express the result in the units requested; perform any conversion before substituting into the equation rather than concealing a factor of one thousand in a final sentence. A rounded answer should not imply accuracy better than the synthetic inputs. This arithmetic operation provides a physical scale, not a certified subsurface interpretation.

**Why the calculation matters.** A numerical ratio provides a detection scale. **Boundary of validity:** Correlated environmental noise and multiple testing are omitted. For an independent sensitivity check, change one stated input by ten percent, leaving others fixed. Explain how the result responds, and whether a plausible alternative hypothesis could produce the same scalar.

### Practical: an observation that could disprove the preferred model

Create a sensitivity diagram with target depth on one axis and acquisition spacing on the other; label domains where resolution is only hypothetical.

**Error budget.** Separate repeatability, calibration bias, position error and model uncertainty in a table with units. Decide which uncertainty dominates the interpretation and what extra information would shrink it. Draw a table containing at least two testable predictions, the needed instrument reading, its physical units, and one reason the observation might be biased.

### Analysis note: how to decide whether the interpretation survives

**State the forward equation and its domain.** Write the physical equation together with geometry, units and assumed constants. List a realistic departure that changes the prediction and distinguish a useful approximation from an unjustified physical claim. In the context of **physical-property contrast and detectability**, explain what a reviewer should expect to see in raw data if the mechanism is credible, and what unexpected pattern would require a revised geological model.

### Synthesis and interpretation checkpoint

Write a short technical conclusion that separates three items: (1) what the instrument directly records in the the inverse problem and geophysical observables problem; (2) the material property or process inferred from it; and (3) a geological claim that would still be unsupported. The exercise is not passed merely by obtaining 6 ratio. Explain why the uncertainty in the assumptions can exceed calculator precision and identify a discriminating field observation.

## Lesson 1.3: Sampling, aliasing and spatial interpolation

### The physical mechanism and its measurable consequence

Sampling a smooth field with large station spacing can miss a narrow source or misrepresent its spatial wavelength. The Nyquist idea supplies a necessary sampling condition for band-limited signals, but real geological fields and noise are not neatly band-limited. Interpolation fills a display gap rather than generating new evidence.

### Acquisition protocol and observable variables

Compute track spacing, survey azimuth and measurement footprint. Repeat line collection at crossing points and retain gaps instead of silently smoothing them away.

### The inverse ambiguity: alternative explanations

A contour drawn by cubic interpolation can invent a closed high between sparse stations. Cultural noise at periodic spacing can alias into a plausible structural trend.

### Worked calculation: synthetic classroom data

**Question — Wavelength sampling.** A sinusoidal magnetic signal has 240 m wavelength; find half-wavelength sample separation.

**Explicit computation:** `240/2` = **120 m**. Express the result in the units requested; perform any conversion before substituting into the equation rather than concealing a factor of one thousand in a final sentence. A rounded answer should not imply accuracy better than the synthetic inputs. This arithmetic operation provides a physical scale, not a certified subsurface interpretation.

**Why the calculation matters.** Sampling more finely than this is needed for ideal band-limited reconstruction. **Boundary of validity:** Real fields require margin, survey layout and anti-aliasing. For an independent sensitivity check, change one stated input by ten percent, leaving others fixed. Explain how the result responds, and whether a plausible alternative hypothesis could produce the same scalar.

### Practical: an observation that could disprove the preferred model

Use an explicitly known synthetic cosine field at two sampling intervals and determine which features remain observable without looking at the original continuous curve.

**Sensitivity study.** Alter the assumed physical-property contrast, source depth or acquisition spacing. Determine whether the sign of the conclusion persists or whether the interpretation is contingent on a narrow prior. Draw a table containing at least two testable predictions, the needed instrument reading, its physical units, and one reason the observation might be biased.

### Analysis note: how to decide whether the interpretation survives

**Decide a safe intended use.** Clarify whether the result is a numerical exercise, exploratory screening, academic interpretation or professional decision product. Educational calculations do not confer authority to make engineering, emergency or environmental determinations. In the context of **sampling, aliasing and spatial interpolation**, explain what a reviewer should expect to see in raw data if the mechanism is credible, and what unexpected pattern would require a revised geological model.

### Synthesis and interpretation checkpoint

Write a short technical conclusion that separates three items: (1) what the instrument directly records in the the inverse problem and geophysical observables problem; (2) the material property or process inferred from it; and (3) a geological claim that would still be unsupported. The exercise is not passed merely by obtaining 120 m. Explain why the uncertainty in the assumptions can exceed calculator precision and identify a discriminating field observation.

## Lesson 1.4: Forward models and non-unique inversions

### The physical mechanism and its measurable consequence

A forward model maps geological parameters through physical equations to predicted instrument readings. Its inverse is often non-unique because multiple combinations of depth, geometry and property contrast fit observations. Regularization makes one solution preferable but does not make it universally true.

### Acquisition protocol and observable variables

Specify model geometry and units, calculate a response, then perturb parameters along a trade-off curve. Save fit residuals and the regularization choice.

### The inverse ambiguity: alternative explanations

Minimizing squared error can overfit unmodelled drift. A physically impossible geometry can still fit a sparse data series if constraints are weak.

### Worked calculation: synthetic classroom data

**Question — Residual RMS.** Four travel-time residuals are 0.02,-0.01,0.03,-0.02 s; calculate RMS.

**Explicit computation:** `((0.02**2+(-0.01)**2+0.03**2+(-0.02)**2)/4)**0.5` = **0.0212132 s**. Express the result in the units requested; perform any conversion before substituting into the equation rather than concealing a factor of one thousand in a final sentence. A rounded answer should not imply accuracy better than the synthetic inputs. This arithmetic operation provides a physical scale, not a certified subsurface interpretation.

**Why the calculation matters.** RMS summarizes misfit magnitude. **Boundary of validity:** Residual correlation and degrees of freedom matter. For an independent sensitivity check, change one stated input by ten percent, leaving others fixed. Explain how the result responds, and whether a plausible alternative hypothesis could produce the same scalar.

### Practical: an observation that could disprove the preferred model

Produce two different models fitting the same synthetic five-station profile and propose a new station able to distinguish them.

**Blind crosscheck.** Give the input series and quality flags to another analyst while hiding the preferred interpretation. Compare their residual and inferred structure with the original and preserve genuine disagreements. Draw a table containing at least two testable predictions, the needed instrument reading, its physical units, and one reason the observation might be biased.

### Analysis note: how to decide whether the interpretation survives

**Track the reference frame.** Coordinates, vertical datums, event origin times, magnetic epochs and polarity conventions are parts of the measurement. Confusing reference frames can shift all stations coherently without producing conspicuous random residuals. In the context of **forward models and non-unique inversions**, explain what a reviewer should expect to see in raw data if the mechanism is credible, and what unexpected pattern would require a revised geological model.

### Synthesis and interpretation checkpoint

Write a short technical conclusion that separates three items: (1) what the instrument directly records in the the inverse problem and geophysical observables problem; (2) the material property or process inferred from it; and (3) a geological claim that would still be unsupported. The exercise is not passed merely by obtaining 0.0212132 s. Explain why the uncertainty in the assumptions can exceed calculator precision and identify a discriminating field observation.

## Lesson 1.5: Uncertainty budgets and reproducibility

### The physical mechanism and its measurable consequence

Random repeatability, calibration bias, wrong physics, coordinate error and incomplete prior knowledge have different meanings. A standard deviation inferred from repeats estimates one source of error, not total uncertainty. Correlated residuals make naive independent-error arithmetic misleading.

### Acquisition protocol and observable variables

Create a measurement log, repeat three control readings, compare independent standards and include model-choice and positional uncertainty in a separate ledger.

### The inverse ambiguity: alternative explanations

A small formal uncertainty from a linearized inverse matrix may understate multimodal geological uncertainty. Precision of a display label is not an accuracy claim.

### Worked calculation: synthetic classroom data

**Question — Independent uncertainty.** Independent timing uncertainties are 0.03 and 0.04 s; compute quadrature sum.

**Explicit computation:** `(0.03**2+0.04**2)**0.5` = **0.05 s**. Express the result in the units requested; perform any conversion before substituting into the equation rather than concealing a factor of one thousand in a final sentence. A rounded answer should not imply accuracy better than the synthetic inputs. This arithmetic operation provides a physical scale, not a certified subsurface interpretation.

**Why the calculation matters.** A combined random timing scale follows the assumed independence. **Boundary of validity:** A shared clock shift does not average away. For an independent sensitivity check, change one stated input by ten percent, leaving others fixed. Explain how the result responds, and whether a plausible alternative hypothesis could produce the same scalar.

### Practical: an observation that could disprove the preferred model

Run a blind repeat where a second team receives raw data and a calibration protocol but no final geological interpretation.

**Instrument validation.** Compare a repeat transect, crossing line or reciprocal reading with original acquisition. Explain what kind of systematic effect the check is capable of detecting and what remains invisible. Draw a table containing at least two testable predictions, the needed instrument reading, its physical units, and one reason the observation might be biased.

### Analysis note: how to decide whether the interpretation survives

**Use a withheld test.** Fit the parameters with one subset and predict genuinely unobserved measurements. Spatial clustering, repeated use of validation stations or tuning after inspecting the holdout exaggerates predictive evidence. In the context of **uncertainty budgets and reproducibility**, explain what a reviewer should expect to see in raw data if the mechanism is credible, and what unexpected pattern would require a revised geological model.

### Synthesis and interpretation checkpoint

Write a short technical conclusion that separates three items: (1) what the instrument directly records in the the inverse problem and geophysical observables problem; (2) the material property or process inferred from it; and (3) a geological claim that would still be unsupported. The exercise is not passed merely by obtaining 0.05 s. Explain why the uncertainty in the assumptions can exceed calculator precision and identify a discriminating field observation.

## Research clinic — choosing a survey rather than buying an answer

Consider a hypothetical contact between basalt and sediment with an irregular surface. A magnetometer may detect magnetization contrasts, a gravity meter senses integrated density differences, and seismic travel times respond to elastic velocity. The strongest response on a demonstration slide is not necessarily the most informative instrument for the true target. Before fieldwork, name a minimum detectable contrast, its likely lateral wavelength and its expected depth. This forces the researcher to compare required field precision and station density with realistic constraints.

Suppose one model places a small highly magnetic dike 100 m deep and another places a much larger, weakly magnetized intrusion 500 m deep. Both might fit a short traversed anomaly. A second parallel line may merely repeat the ambiguity. A long line extending beyond the flanks, independent susceptibility samples, or measurement at another elevation could have higher discriminating power. The new observation should be selected according to how differently the two models predict it. That is an experiment, not an argument from visual appeal.

Represent each measurement with the original support volume, not just the interpolated point displayed in software. A seismic pick has a window and bandwidth; a potential-field observation reflects a broad distributed source; a resistivity datum samples a sensitivity kernel that overlaps many electrodes. Equal pixel dimensions on final maps do not imply equal spatial resolution. If geophysical data are gridded at a finer spacing than their independent information content, the extra cells are an illustration convention, not additional measurements.

An efficient student report first shows a map of observation locations with uncertainty and coverage. Next it shows raw traces or readings before aggressive filtering. Only then does it show a forward prediction and alternative model. It ends with an uncollected measurement most likely to reject an incorrect explanation. This sequence remains useful even if the original hypothesis is not supported; a valid negative result has experimental value.


## Unit investigation: reproducible synthetic dataset and experimental design

**Research aim.** The invented scenario is: A fictional volcanic plateau is crossed by two short survey lines. Students receive elevation, instrument drift, measurement error and an incomplete geology map; they must distinguish response calibration from geological interpretation. Treat `datasets/unit-01.csv` as forty fictional rows deliberately designed to exercise quality control and model criticism. Read the file header before drawing any map. Plot the two relevant measured fields from unit 1; display the `quality_flag` column rather than deleting all flagged stations silently. The synthetic table contains no geographic coordinate reference system or real site identifiers and cannot be used to identify a place.

**Part A — raw measurements and dimensions.** Read each column as a quantity, not as a decorative label. For the inverse problem and geophysical observables, check whether the stated units are compatible with its equation and record which columns represent observed signals, instrument corrections, independent controls or model-derived quantities. Identify missing information such as date, site geology, true coordinate system, instrument orientation or calibration. If those omissions prevent a physical inversion, state the limitation and limit the task to transparent exploratory analysis. This is a stronger result than assigning fictitious precision.

**Part B — repeat and quality flags.** Count the rows marked `review`. Compare summary statistics, plotted gradients and model parameters with all forty records against the subset that passes the flag. Document every change; flags indicate inspection priority, not a universal mandate to delete. Check whether questionable values cluster along position or signal amplitude, because exclusions can introduce bias. If the noise appears correlated, do not assume a root-sum-square independent-error formula without a justification.

**Part C — model competition.** Describe two geophysical models that explain the synthetic observations in the inverse problem and geophysical observables; they must differ in physical property, geometry or forcing rather than just parameter precision. For each hypothesis make an observable prediction about station response, uncertainty pattern, external control or independent method. Select one new measurement that would best discriminate them, and explain its predicted signal under both hypotheses. A new dense sample from the same short profile may add less independent information than a crossing line or sample.

**Part D — numerical sensitivity.** Recompute one of the unit worked cases with the principal input increased by 10% and decreased by 10%. Check if the response is linear, inverse, logarithmic, quadratic or subject to another nonlinearity. Show a table with input, computed output, unit and physical assumption. Do not claim a sensitivity of the geological interpretation itself if only the toy forward equation was changed; the inverse solution may have a much broader family of possibilities.

**Part E — out-of-sample prediction and reporting.** Split the synthetic observations by physical position, retaining a contiguous group as a blind holdout. Fit a deliberately simple forward trend to remaining rows and predict the held-out quantity without retuning. Compare predictive error with a baseline that uses a constant mean. State why geographic separation can be a stronger test than random point withholding. Report all transformations, quality flags, fitted parameters, residual plots and failure modes in a compact methods appendix.

**Unit-specific evidence synthesis.** Geophysics estimates otherwise inaccessible properties by measuring fields and wave responses at accessible positions. The forward problem predicts observations from a specified model; the inverse problem asks what models might produce an observation. Sources, material properties, sensor geometry, boundary conditions and noise all influence the prediction. A low-residual model is not automatically the only acceptable subsurface explanation. State which variables were observed, which were assumed and which were regularized. Resolution varies with sampling density, instrument bandwidth and model physics. A map pixel inherits assumptions from calibration and interpolation, not merely precision from its file format. A defensible interpretation predicts measurements at a location withheld from the inversion and makes alternatives visible. Map the chain of evidence from sensor to interpretation; highlight an uncertainty not reducible by extra decimal places. In your conclusion, indicate which measurement you would acquire next if the synthetic experiment were replaced with licensed real-world data. Keep any real data sourced from the references separate from these forty invented rows.

**Suggested report.** Submit a transparent CSV-reading script or spreadsheet calculation, one raw-data figure, a sensitivity plot, two candidate geological explanations, a withheld-test result and a one-page uncertainty ledger. Grade on conceptual correctness (25%), numerical units and reproducibility (25%), alternate hypotheses (20%), validation logic (20%) and scientific communication (10%). Never reward a map for appearing more certain than its underlying observations.

## End-of-unit reflection and problems

1. Identify which part of **the inverse problem and geophysical observables** would remain ambiguous even if measurement noise were reduced to zero. Explain how the survey geometry or parameter relationship creates that ambiguity.

2. Find a case where a large change in the observed signal would not imply a proportionally large change in target size. Write the forward relation, name fixed parameters, and state why inversion differs from prediction.

3. Propose a new survey that would risk rejecting the preferred geological interpretation. Its value should be based on discriminating predictions rather than its technological sophistication.

4. Draw a data lineage chart from raw instrument data through correction, inversion and geological claim. Underline any operation that assumes a material property not measured in the original dataset.

5. Explain why the synthetic data and interactive sliders are educational examples and cannot support emergency warnings, ground-investigation certification, resource appraisal or environmental enforcement.

## Additional reading and independent replication

Use `REFERENCES.md` to find a genuine program or open repository relevant to the inverse problem and geophysical observables. Before downloading any data, check the provider documentation, citation requirements, usage permissions and the time period represented. Record the instrument type, station metadata and acquisition geometry, then reproduce one simple physical calculation from scratch. The objective is not to match a published colored inversion image exactly; it is to understand the observable and give a defensible account of differences.


## Interactive physical-model explanations

Open this chapter in the HTML reader to change one controlled physical variable at a time. Each model is a simplified *forward* calculation, not an inversion or a real-world estimator.

### Acceleration difference

Input quantity: Change in acceleration measured in m/s²; demonstration range 0–0.001, initial setting 0.0003. Output: mGal. Computed from `x*100000`.

**Unmodelled influences and interpretation boundary:** Exactly 1 mGal equals 10^-5 m/s²; reference effects ignored. Students should articulate a case where this formula yields a numerically precise but physically misleading answer and state an independently measurable quantity needed for a more complete model.

### Ideal sampling requirement

Input quantity: Wavelength measured in m; demonstration range 50–1000, initial setting 240. Output: m. Computed from `x/2`.

**Unmodelled influences and interpretation boundary:** Nyquist half-wavelength threshold for ideal bandlimited signals, not guaranteed field resolution. Students should articulate a case where this formula yields a numerically precise but physically misleading answer and state an independently measurable quantity needed for a more complete model.
