# Unit 3: Seismic reflection and refraction imaging

## Central question: How are subsurface interfaces estimated from transmitted and reflected elastic energy?

**Fictional unit investigation:** A fictional basin has a shallow high-velocity layer, uncertain weathering thickness and steep strata. Students compare first-arrival refraction, common-midpoint reflection and a well log while acknowledging resolution limits.

## Geophysical foundation and the measurement-to-model chain

Active seismic methods launch controlled elastic energy and record travel times and amplitudes. Refraction favours early arrivals along sufficiently fast pathways, whereas reflection exploits impedance contrasts and two-way travel. Acquisition geometry, near-surface statics, anisotropy, multiples, attenuation and velocity error may each produce misleading structure. A reflector is an impedance boundary, not necessarily a lithologic boundary or single time horizon. Depth migration requires a suitable velocity field. Vertical resolution depends partly on wavelength and bandwidth; a visually sharp processed line need not mean decimeter-scale depth accuracy. Boreholes and geological mapping provide critical, though local, ground truth.

## Five lessons: hypotheses, observables and field checks

For each lesson the forward physics and observation type are explicit. The lesson is complete only when the student can name a competing explanation, check units in the worked calculation and explain a measurement that could reject the preferred interpretation. Every stated numerical value is invented for this textbook; none is a field station or an operational parameter.

## Lesson 3.1: Seismic impedance and reflection coefficients

### The physical mechanism and its measurable consequence

At normal incidence, the elastic acoustic reflection approximation uses the contrast in impedance Z=rho v. Positive and negative amplitudes can indicate impedance contrasts, but amplitude polarity may change with instrument or processing conventions. Oblique incidence and converted waves require more complete elastic treatments.

### Acquisition protocol and observable variables

Estimate density and compressional velocity from logs or samples, compute predicted interface polarity and inspect wavelet phase on traces.

### The inverse ambiguity: alternative explanations

A strong reflector might indicate fluid, porosity, lithology or thin-bed tuning; amplitude alone does not reveal a unique rock boundary.

### Worked calculation: synthetic classroom data

**Question — Normal-incidence reflection.** For impedances 10 and 15 MRayl, compute reflection coefficient (Z2-Z1)/(Z2+Z1).

**Explicit computation:** `(15-10)/(15+10)` = **0.2 ratio**. Express the result in the units requested; perform any conversion before substituting into the equation rather than concealing a factor of one thousand in a final sentence. A rounded answer should not imply accuracy better than the synthetic inputs. This arithmetic operation provides a physical scale, not a certified subsurface interpretation.

**Why the calculation matters.** Positive reflection coefficient follows the chosen polarity convention. **Boundary of validity:** Elastic oblique-wave effects omitted. For an independent sensitivity check, change one stated input by ten percent, leaving others fixed. Explain how the result responds, and whether a plausible alternative hypothesis could produce the same scalar.

### Practical: an observation that could disprove the preferred model

Construct two layered sequences with identical normal-incidence reflection coefficient and different underlying lithologies.

**Instrument validation.** Compare a repeat transect, crossing line or reciprocal reading with original acquisition. Explain what kind of systematic effect the check is capable of detecting and what remains invisible. Draw a table containing at least two testable predictions, the needed instrument reading, its physical units, and one reason the observation might be biased.

### Analysis note: how to decide whether the interpretation survives

**Inspect the observation footprint.** Ask which wavelengths and parts of the Earth contribute to the instrument. Potential fields integrate over substantial volumes, seismic picks follow ray paths and electrode arrays have diffuse sensitivity; a pixel-sized interpretation usually exceeds the resolving claim. In the context of **seismic impedance and reflection coefficients**, explain what a reviewer should expect to see in raw data if the mechanism is credible, and what unexpected pattern would require a revised geological model.

### Synthesis and interpretation checkpoint

Write a short technical conclusion that separates three items: (1) what the instrument directly records in the seismic reflection and refraction imaging problem; (2) the material property or process inferred from it; and (3) a geological claim that would still be unsupported. The exercise is not passed merely by obtaining 0.2 ratio. Explain why the uncertainty in the assumptions can exceed calculator precision and identify a discriminating field observation.

## Lesson 3.2: First-arrival refraction and critical rays

### The physical mechanism and its measurable consequence

Refraction surveys infer velocity layering from travel-time branches if deeper layers sufficiently exceed shallow velocities. Head-wave intercept methods assume simplified planar layers. Hidden low-velocity layers or lateral velocity changes can evade this inference.

### Acquisition protocol and observable variables

Pick first-breaks over a wide offset range. Plot t versus x for multiple shots and inspect whether reversed shots give consistent velocities.

### The inverse ambiguity: alternative explanations

A crossover interpreted as a deeper layer may be a lateral change or poor pick. A low-speed layer may be invisible to classical head-wave methods.

### Worked calculation: synthetic classroom data

**Question — Refraction crossover.** Direct-wave t=x/2 km/s; head-wave t=0.25+x/4 km/s; solve crossover in km.

**Explicit computation:** `0.25/(1/2-1/4)` = **1 km**. Express the result in the units requested; perform any conversion before substituting into the equation rather than concealing a factor of one thousand in a final sentence. A rounded answer should not imply accuracy better than the synthetic inputs. This arithmetic operation provides a physical scale, not a certified subsurface interpretation.

**Why the calculation matters.** The branch crossover can help constrain ideal layers. **Boundary of validity:** Real profiles can conceal low-velocity layers. For an independent sensitivity check, change one stated input by ten percent, leaving others fixed. Explain how the result responds, and whether a plausible alternative hypothesis could produce the same scalar.

### Practical: an observation that could disprove the preferred model

Compare a two-layer analytical curve with synthetic offsets truncated before the crossover; explain the loss of identifiability.

**Physical sanity test.** Evaluate the model at an extreme but admissible input and check dimensions, sign, limiting behaviour and plausibility. A correct arithmetic result with a broken physical assumption is not a sound geological conclusion. Draw a table containing at least two testable predictions, the needed instrument reading, its physical units, and one reason the observation might be biased.

### Analysis note: how to decide whether the interpretation survives

**State the forward equation and its domain.** Write the physical equation together with geometry, units and assumed constants. List a realistic departure that changes the prediction and distinguish a useful approximation from an unjustified physical claim. In the context of **first-arrival refraction and critical rays**, explain what a reviewer should expect to see in raw data if the mechanism is credible, and what unexpected pattern would require a revised geological model.

### Synthesis and interpretation checkpoint

Write a short technical conclusion that separates three items: (1) what the instrument directly records in the seismic reflection and refraction imaging problem; (2) the material property or process inferred from it; and (3) a geological claim that would still be unsupported. The exercise is not passed merely by obtaining 1 km. Explain why the uncertainty in the assumptions can exceed calculator precision and identify a discriminating field observation.

## Lesson 3.3: Common-midpoint stacking and NMO

### The physical mechanism and its measurable consequence

Normal moveout corrects offset-dependent reflection times using an effective stacking velocity under idealized assumptions. Common-midpoint stacking improves coherent signal but can suppress real dipping events or obscure small features when bins are wide. Multiple reflections create false geological horizons unless treated carefully.

### Acquisition protocol and observable variables

Store source and receiver coordinates, fold and offset distributions. Compare gathers before and after velocity analysis with a documented mute.

### The inverse ambiguity: alternative explanations

An erroneously high stacking velocity flattens a different event; repeated multiples can appear as genuine deeper strata.

### Worked calculation: synthetic classroom data

**Question — Reflection depth.** Uniform v=2500 m/s and two-way time=0.8 s; calculate vertical reflector depth.

**Explicit computation:** `2500*0.8/2` = **1000 m**. Express the result in the units requested; perform any conversion before substituting into the equation rather than concealing a factor of one thousand in a final sentence. A rounded answer should not imply accuracy better than the synthetic inputs. This arithmetic operation provides a physical scale, not a certified subsurface interpretation.

**Why the calculation matters.** Depth conversion uses half the two-way time. **Boundary of validity:** Velocity heterogeneity and dip omitted. For an independent sensitivity check, change one stated input by ten percent, leaving others fixed. Explain how the result responds, and whether a plausible alternative hypothesis could produce the same scalar.

### Practical: an observation that could disprove the preferred model

Change assumed moveout velocity on a synthetic gather and quantify residual curvature rather than judging the display visually.

**Data stewardship.** Document synthetic status, provenance, coordinates, units, processing version, license and intended use. Keep measurements in a separate file from interpolated or inversion-derived quantities. Draw a table containing at least two testable predictions, the needed instrument reading, its physical units, and one reason the observation might be biased.

### Analysis note: how to decide whether the interpretation survives

**Decide a safe intended use.** Clarify whether the result is a numerical exercise, exploratory screening, academic interpretation or professional decision product. Educational calculations do not confer authority to make engineering, emergency or environmental determinations. In the context of **common-midpoint stacking and nmo**, explain what a reviewer should expect to see in raw data if the mechanism is credible, and what unexpected pattern would require a revised geological model.

### Synthesis and interpretation checkpoint

Write a short technical conclusion that separates three items: (1) what the instrument directly records in the seismic reflection and refraction imaging problem; (2) the material property or process inferred from it; and (3) a geological claim that would still be unsupported. The exercise is not passed merely by obtaining 1000 m. Explain why the uncertainty in the assumptions can exceed calculator precision and identify a discriminating field observation.

## Lesson 3.4: Resolution, attenuation and migration

### The physical mechanism and its measurable consequence

Finite wavelet bandwidth limits separability of interfaces. Attenuation and scattering preferentially remove high frequencies and may change apparent reflection amplitude. Migration repositions events using a velocity model, but cannot manufacture frequencies never recorded.

### Acquisition protocol and observable variables

Estimate dominant frequency and velocity, state vertical tuning thickness and cross-line spacing. Compare migration results under alternative plausible velocity fields.

### The inverse ambiguity: alternative explanations

A crisp reflection may be a migration artefact. Interference between closely spaced layers can generate apparent amplitude anomalies.

### Worked calculation: synthetic classroom data

**Question — Quarter-wavelength.** At speed 3000 m/s and dominant frequency 50 Hz, compute v/(4f).

**Explicit computation:** `3000/(4*50)` = **15 m**. Express the result in the units requested; perform any conversion before substituting into the equation rather than concealing a factor of one thousand in a final sentence. A rounded answer should not imply accuracy better than the synthetic inputs. This arithmetic operation provides a physical scale, not a certified subsurface interpretation.

**Why the calculation matters.** The quarter-wavelength scale is a rule of thumb for thin-bed tuning. **Boundary of validity:** Actual resolvability depends on bandwidth and noise. For an independent sensitivity check, change one stated input by ten percent, leaving others fixed. Explain how the result responds, and whether a plausible alternative hypothesis could produce the same scalar.

### Practical: an observation that could disprove the preferred model

Model a thin bed at one-eighth, one-quarter and half wavelength and identify when two interfaces are no longer independently resolved.

**Acquisition design.** Define the physical source, sensor property, site geometry and independent calibration needed before collecting data. State which raw channels must survive processing and what a second researcher could reproduce. Draw a table containing at least two testable predictions, the needed instrument reading, its physical units, and one reason the observation might be biased.

### Analysis note: how to decide whether the interpretation survives

**Track the reference frame.** Coordinates, vertical datums, event origin times, magnetic epochs and polarity conventions are parts of the measurement. Confusing reference frames can shift all stations coherently without producing conspicuous random residuals. In the context of **resolution, attenuation and migration**, explain what a reviewer should expect to see in raw data if the mechanism is credible, and what unexpected pattern would require a revised geological model.

### Synthesis and interpretation checkpoint

Write a short technical conclusion that separates three items: (1) what the instrument directly records in the seismic reflection and refraction imaging problem; (2) the material property or process inferred from it; and (3) a geological claim that would still be unsupported. The exercise is not passed merely by obtaining 15 m. Explain why the uncertainty in the assumptions can exceed calculator precision and identify a discriminating field observation.

## Lesson 3.5: Borehole logs and seismic ties

### The physical mechanism and its measurable consequence

Sonic and density logging may help predict reflection impedance, while a vertical seismic profile connects depth-domain well observations with seismic time. Log quality, borehole conditions, anisotropy and scale mismatches complicate ties. Calibration at one well does not prove that facies remain continuous across the survey.

### Acquisition protocol and observable variables

Build a synthetic seismogram from property contrasts, align it to a reference trace and report phase, checkshot and depth corrections.

### The inverse ambiguity: alternative explanations

A correlation selected by eye may match the wrong event. A well samples a narrow volume while seismic traces average over a larger Fresnel zone.

### Worked calculation: synthetic classroom data

**Question — Acoustic impedance.** Density=2400 kg/m³, speed=3000 m/s; compute impedance in MRayl.

**Explicit computation:** `2400*3000/1e6` = **7.2 MRayl**. Express the result in the units requested; perform any conversion before substituting into the equation rather than concealing a factor of one thousand in a final sentence. A rounded answer should not imply accuracy better than the synthetic inputs. This arithmetic operation provides a physical scale, not a certified subsurface interpretation.

**Why the calculation matters.** The quantity is density times phase speed. **Boundary of validity:** Other elastic parameters enter angle-dependent reflectivity. For an independent sensitivity check, change one stated input by ten percent, leaving others fixed. Explain how the result responds, and whether a plausible alternative hypothesis could produce the same scalar.

### Practical: an observation that could disprove the preferred model

Propose a blind test using a withheld well and state which interval correlations survive without retuning.

**Competing models.** Choose two different geologic or instrumental explanations for the observation and write one numerical or spatial prediction on which they disagree. Reserve a new observation as a prospective test. Draw a table containing at least two testable predictions, the needed instrument reading, its physical units, and one reason the observation might be biased.

### Analysis note: how to decide whether the interpretation survives

**Use a withheld test.** Fit the parameters with one subset and predict genuinely unobserved measurements. Spatial clustering, repeated use of validation stations or tuning after inspecting the holdout exaggerates predictive evidence. In the context of **borehole logs and seismic ties**, explain what a reviewer should expect to see in raw data if the mechanism is credible, and what unexpected pattern would require a revised geological model.

### Synthesis and interpretation checkpoint

Write a short technical conclusion that separates three items: (1) what the instrument directly records in the seismic reflection and refraction imaging problem; (2) the material property or process inferred from it; and (3) a geological claim that would still be unsupported. The exercise is not passed merely by obtaining 7.2 MRayl. Explain why the uncertainty in the assumptions can exceed calculator precision and identify a discriminating field observation.

## Research clinic — reflection image versus rock geometry

In a fictional basin survey, a reflection at 0.8 seconds two-way time is mapped as a continuous bright event. Converting 0.8 seconds to meters at 2500 m/s produces 1000 m, but the implied depth is conditional on an average vertical velocity model. If the true speed were 2000 m/s, the same measured time would imply 800 m. The acoustic travel time is observed; depth is inferred. The velocity error is not a minor typographic detail when one interpretation labels an important geological boundary.

A reflector also need not be a single lithologic contact. Thin beds, fluid-related changes, pore-pressure effects and tuning can create amplitudes without a clean material boundary. An apparent fault on an unmigrated section might shift after an improved velocity model. Migration itself can cause artefacts if the assumed velocity is poor. Inspect the pre-stack gathers and the acquisition fold before drawing a cross-section: a beautiful final section can hide suppressed noise and mispositioned energy.

First-arrival refraction and normal-incidence reflection are complementary but not interchangeable. A low-velocity layer may be almost invisible to ideal two-layer head-wave analysis; a reflection interface can be prominent because impedance changes even if the net speed change is modest. Compare two synthetic two-layer Earth models with the same top speed and different lower density. Their refraction branch may look similar while their reflection coefficient changes. Conversely the same impedance could result from different combinations of density and velocity. Use this to motivate physical-property logging.

In the practical report, reserve a well or independent line and withhold it until after the seismic interpretation is written. Predict reflector depth and velocity at that location, then compare with the independent result. State if the discrepancy is random, systematic, or evidence that the geological model should be rejected. The objective is to learn how an image becomes a testable hypothesis rather than an apparently authoritative underground photograph.


## Unit investigation: reproducible synthetic dataset and experimental design

**Research aim.** The invented scenario is: A fictional basin has a shallow high-velocity layer, uncertain weathering thickness and steep strata. Students compare first-arrival refraction, common-midpoint reflection and a well log while acknowledging resolution limits. Treat `datasets/unit-03.csv` as forty fictional rows deliberately designed to exercise quality control and model criticism. Read the file header before drawing any map. Plot the two relevant measured fields from unit 3; display the `quality_flag` column rather than deleting all flagged stations silently. The synthetic table contains no geographic coordinate reference system or real site identifiers and cannot be used to identify a place.

**Part A — raw measurements and dimensions.** Read each column as a quantity, not as a decorative label. For seismic reflection and refraction imaging, check whether the stated units are compatible with its equation and record which columns represent observed signals, instrument corrections, independent controls or model-derived quantities. Identify missing information such as date, site geology, true coordinate system, instrument orientation or calibration. If those omissions prevent a physical inversion, state the limitation and limit the task to transparent exploratory analysis. This is a stronger result than assigning fictitious precision.

**Part B — repeat and quality flags.** Count the rows marked `review`. Compare summary statistics, plotted gradients and model parameters with all forty records against the subset that passes the flag. Document every change; flags indicate inspection priority, not a universal mandate to delete. Check whether questionable values cluster along position or signal amplitude, because exclusions can introduce bias. If the noise appears correlated, do not assume a root-sum-square independent-error formula without a justification.

**Part C — model competition.** Describe two geophysical models that explain the synthetic observations in seismic reflection and refraction imaging; they must differ in physical property, geometry or forcing rather than just parameter precision. For each hypothesis make an observable prediction about station response, uncertainty pattern, external control or independent method. Select one new measurement that would best discriminate them, and explain its predicted signal under both hypotheses. A new dense sample from the same short profile may add less independent information than a crossing line or sample.

**Part D — numerical sensitivity.** Recompute one of the unit worked cases with the principal input increased by 10% and decreased by 10%. Check if the response is linear, inverse, logarithmic, quadratic or subject to another nonlinearity. Show a table with input, computed output, unit and physical assumption. Do not claim a sensitivity of the geological interpretation itself if only the toy forward equation was changed; the inverse solution may have a much broader family of possibilities.

**Part E — out-of-sample prediction and reporting.** Split the synthetic observations by physical position, retaining a contiguous group as a blind holdout. Fit a deliberately simple forward trend to remaining rows and predict the held-out quantity without retuning. Compare predictive error with a baseline that uses a constant mean. State why geographic separation can be a stronger test than random point withholding. Report all transformations, quality flags, fitted parameters, residual plots and failure modes in a compact methods appendix.

**Unit-specific evidence synthesis.** Active seismic methods launch controlled elastic energy and record travel times and amplitudes. Refraction favours early arrivals along sufficiently fast pathways, whereas reflection exploits impedance contrasts and two-way travel. Acquisition geometry, near-surface statics, anisotropy, multiples, attenuation and velocity error may each produce misleading structure. A reflector is an impedance boundary, not necessarily a lithologic boundary or single time horizon. Depth migration requires a suitable velocity field. Vertical resolution depends partly on wavelength and bandwidth; a visually sharp processed line need not mean decimeter-scale depth accuracy. Boreholes and geological mapping provide critical, though local, ground truth. Map the chain of evidence from sensor to interpretation; highlight an uncertainty not reducible by extra decimal places. In your conclusion, indicate which measurement you would acquire next if the synthetic experiment were replaced with licensed real-world data. Keep any real data sourced from the references separate from these forty invented rows.

**Suggested report.** Submit a transparent CSV-reading script or spreadsheet calculation, one raw-data figure, a sensitivity plot, two candidate geological explanations, a withheld-test result and a one-page uncertainty ledger. Grade on conceptual correctness (25%), numerical units and reproducibility (25%), alternate hypotheses (20%), validation logic (20%) and scientific communication (10%). Never reward a map for appearing more certain than its underlying observations.

## End-of-unit reflection and problems

1. Identify which part of **seismic reflection and refraction imaging** would remain ambiguous even if measurement noise were reduced to zero. Explain how the survey geometry or parameter relationship creates that ambiguity.

2. Find a case where a large change in the observed signal would not imply a proportionally large change in target size. Write the forward relation, name fixed parameters, and state why inversion differs from prediction.

3. Propose a new survey that would risk rejecting the preferred geological interpretation. Its value should be based on discriminating predictions rather than its technological sophistication.

4. Draw a data lineage chart from raw instrument data through correction, inversion and geological claim. Underline any operation that assumes a material property not measured in the original dataset.

5. Explain why the synthetic data and interactive sliders are educational examples and cannot support emergency warnings, ground-investigation certification, resource appraisal or environmental enforcement.

## Additional reading and independent replication

Use `REFERENCES.md` to find a genuine program or open repository relevant to seismic reflection and refraction imaging. Before downloading any data, check the provider documentation, citation requirements, usage permissions and the time period represented. Record the instrument type, station metadata and acquisition geometry, then reproduce one simple physical calculation from scratch. The objective is not to match a published colored inversion image exactly; it is to understand the observable and give a defensible account of differences.


## Interactive physical-model explanations

Open this chapter in the HTML reader to change one controlled physical variable at a time. Each model is a simplified *forward* calculation, not an inversion or a real-world estimator.

### Normal-incidence acoustic reflectivity

Input quantity: Second impedance measured in MRayl; demonstration range 5–30, initial setting 15. Output: ratio. Computed from `(x-10)/(x+10)`.

**Unmodelled influences and interpretation boundary:** First impedance fixed at 10 MRayl; simple normal-incidence acoustic case. Students should articulate a case where this formula yields a numerically precise but physically misleading answer and state an independently measurable quantity needed for a more complete model.

### Two-way-time seismic depth

Input quantity: Two-way travel time measured in s; demonstration range 0.1–3, initial setting 0.8. Output: m. Computed from `2500*x/2`.

**Unmodelled influences and interpretation boundary:** Constant 2500 m/s vertical speed; no dips or anisotropy. Students should articulate a case where this formula yields a numerically precise but physically misleading answer and state an independently measurable quantity needed for a more complete model.
