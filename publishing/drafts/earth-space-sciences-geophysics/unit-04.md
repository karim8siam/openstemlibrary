# Unit 4: Gravity surveying and the Earth's gravity field

## Central question: Which density distributions are consistent with a measured gravitational anomaly?

**Fictional unit investigation:** A classroom gravity transect crosses a notional buried intrusion and an adjacent basin. The observed change contains instrument drift, free-air and latitude effects as well as possible density variations; a unique body depth cannot be assumed.

## Geophysical foundation and the measurement-to-model chain

Gravity measurements encode mass distribution and distance, not rock names. The observed acceleration contains latitude, elevation, tides, instrumental drift and local topographic mass as well as subsurface heterogeneity. Bouguer and terrain corrections are model-based conventions that must be documented; incorrect density assumptions can shift anomaly magnitude and interpretation. Regional-residual separation changes what features appear significant. A dense shallow body can mimic a larger deeper body; gravity inversion therefore benefits from independent constraints on geometry and density. A residual small enough for publication is not proof of a unique body shape.

## Five lessons: hypotheses, observables and field checks

For each lesson the forward physics and observation type are explicit. The lesson is complete only when the student can name a competing explanation, check units in the worked calculation and explain a measurement that could reject the preferred interpretation. Every stated numerical value is invented for this textbook; none is a field station or an operational parameter.

## Lesson 4.1: Gravitational potential, acceleration and units

### The physical mechanism and its measurable consequence

Newtonian gravity relates mass to acceleration through inverse-square distance. Gravity surveys often report anomalies in mGal, a much smaller unit than m/s squared. Interpretation requires a carefully defined reference field and measurement height.

### Acquisition protocol and observable variables

Record gravimeter raw readings, spring-meter scale, base ties, station elevation, time and instrument serial number. Convert acceleration between SI and mGal.

### The inverse ambiguity: alternative explanations

An apparent anomaly can reflect tide, instrument drift or an omitted topographic correction rather than a density body.

### Worked calculation: synthetic classroom data

**Question — Inverse-square gravity.** Point mass=1e11 kg at r=200 m; find acceleration G M/r² in mGal.

**Explicit computation:** `6.67430e-11*1e11/200**2*1e5` = **16.68575 mGal**. Express the result in the units requested; perform any conversion before substituting into the equation rather than concealing a factor of one thousand in a final sentence. A rounded answer should not imply accuracy better than the synthetic inputs. This arithmetic operation provides a physical scale, not a certified subsurface interpretation.

**Why the calculation matters.** Point-mass geometry illustrates gravitational distance dependence. **Boundary of validity:** A buried extended body is not a point source. For an independent sensitivity check, change one stated input by ten percent, leaving others fixed. Explain how the result responds, and whether a plausible alternative hypothesis could produce the same scalar.

### Practical: an observation that could disprove the preferred model

Write a station-by-station correction table and check the sign of every contribution using a simple elevated-station thought experiment.

**Sensitivity study.** Alter the assumed physical-property contrast, source depth or acquisition spacing. Determine whether the sign of the conclusion persists or whether the interpretation is contingent on a narrow prior. Draw a table containing at least two testable predictions, the needed instrument reading, its physical units, and one reason the observation might be biased.

### Analysis note: how to decide whether the interpretation survives

**Inspect the observation footprint.** Ask which wavelengths and parts of the Earth contribute to the instrument. Potential fields integrate over substantial volumes, seismic picks follow ray paths and electrode arrays have diffuse sensitivity; a pixel-sized interpretation usually exceeds the resolving claim. In the context of **gravitational potential, acceleration and units**, explain what a reviewer should expect to see in raw data if the mechanism is credible, and what unexpected pattern would require a revised geological model.

### Synthesis and interpretation checkpoint

Write a short technical conclusion that separates three items: (1) what the instrument directly records in the gravity surveying and the earth's gravity field problem; (2) the material property or process inferred from it; and (3) a geological claim that would still be unsupported. The exercise is not passed merely by obtaining 16.68575 mGal. Explain why the uncertainty in the assumptions can exceed calculator precision and identify a discriminating field observation.

## Lesson 4.2: Free-air, Bouguer and terrain corrections

### The physical mechanism and its measurable consequence

Free-air correction approximates change of gravity with height; a Bouguer slab approximates gravitational attraction of intervening topographic mass. Terrain corrections account for departures from the slab. These are conventions with approximations and chosen density.

### Acquisition protocol and observable variables

Compute consistent heights and use a documented density assumption for Bouguer adjustment. Separate observed reading, theoretical gravity and each correction term.

### The inverse ambiguity: alternative explanations

A wrong elevation datum or rock-density assumption can create false regional gradients, especially in steep terrain.

### Worked calculation: synthetic classroom data

**Question — Free-air elevation.** A station rises 300 m; use 0.3086 mGal/m as first-order vertical gravity gradient; find correction magnitude.

**Explicit computation:** `0.3086*300` = **92.58 mGal**. Express the result in the units requested; perform any conversion before substituting into the equation rather than concealing a factor of one thousand in a final sentence. A rounded answer should not imply accuracy better than the synthetic inputs. This arithmetic operation provides a physical scale, not a certified subsurface interpretation.

**Why the calculation matters.** This is the magnitude of a standard approximate free-air correction. **Boundary of validity:** Sign depends on convention and datum. For an independent sensitivity check, change one stated input by ten percent, leaving others fixed. Explain how the result responds, and whether a plausible alternative hypothesis could produce the same scalar.

### Practical: an observation that could disprove the preferred model

Evaluate the apparent anomaly for two assumed reduction densities and explain why a single geological color scale is overconfident.

**Blind crosscheck.** Give the input series and quality flags to another analyst while hiding the preferred interpretation. Compare their residual and inferred structure with the original and preserve genuine disagreements. Draw a table containing at least two testable predictions, the needed instrument reading, its physical units, and one reason the observation might be biased.

### Analysis note: how to decide whether the interpretation survives

**State the forward equation and its domain.** Write the physical equation together with geometry, units and assumed constants. List a realistic departure that changes the prediction and distinguish a useful approximation from an unjustified physical claim. In the context of **free-air, bouguer and terrain corrections**, explain what a reviewer should expect to see in raw data if the mechanism is credible, and what unexpected pattern would require a revised geological model.

### Synthesis and interpretation checkpoint

Write a short technical conclusion that separates three items: (1) what the instrument directly records in the gravity surveying and the earth's gravity field problem; (2) the material property or process inferred from it; and (3) a geological claim that would still be unsupported. The exercise is not passed merely by obtaining 92.58 mGal. Explain why the uncertainty in the assumptions can exceed calculator precision and identify a discriminating field observation.

## Lesson 4.3: Simple body anomalies and source depth

### The physical mechanism and its measurable consequence

The gravity field of a sphere depends on total excess mass and source geometry. Smooth broad profiles may indicate greater depth, but density and shape trade off. Upward continuation smooths shallow variations and reduces noise at the cost of resolution.

### Acquisition protocol and observable variables

Forward-model a buried sphere at several depths and compare spatial profile width and peak. Use only geometries where the observation points lie outside the body.

### The inverse ambiguity: alternative explanations

An elongated dike or shallow basin edge may approximate a sphere over a short line; a best-fit radius cannot be treated as a discovered lithologic contact.

### Worked calculation: synthetic classroom data

**Question — Bouguer slab.** Density=2670 kg/m³ and height=150 m; compute ideal slab attraction 2πGρh in mGal.

**Explicit computation:** `2*math.pi*6.67430e-11*2670*150*1e5` = **16.79531 mGal**. Express the result in the units requested; perform any conversion before substituting into the equation rather than concealing a factor of one thousand in a final sentence. A rounded answer should not imply accuracy better than the synthetic inputs. This arithmetic operation provides a physical scale, not a certified subsurface interpretation.

**Why the calculation matters.** An infinite-slab value helps demonstrate mass correction. **Boundary of validity:** Terrain deviations and curvature omitted. For an independent sensitivity check, change one stated input by ten percent, leaving others fixed. Explain how the result responds, and whether a plausible alternative hypothesis could produce the same scalar.

### Practical: an observation that could disprove the preferred model

Place stations beyond the anomaly flanks, then compare which model family loses its apparent equivalence.

**Instrument validation.** Compare a repeat transect, crossing line or reciprocal reading with original acquisition. Explain what kind of systematic effect the check is capable of detecting and what remains invisible. Draw a table containing at least two testable predictions, the needed instrument reading, its physical units, and one reason the observation might be biased.

### Analysis note: how to decide whether the interpretation survives

**Decide a safe intended use.** Clarify whether the result is a numerical exercise, exploratory screening, academic interpretation or professional decision product. Educational calculations do not confer authority to make engineering, emergency or environmental determinations. In the context of **simple body anomalies and source depth**, explain what a reviewer should expect to see in raw data if the mechanism is credible, and what unexpected pattern would require a revised geological model.

### Synthesis and interpretation checkpoint

Write a short technical conclusion that separates three items: (1) what the instrument directly records in the gravity surveying and the earth's gravity field problem; (2) the material property or process inferred from it; and (3) a geological claim that would still be unsupported. The exercise is not passed merely by obtaining 16.79531 mGal. Explain why the uncertainty in the assumptions can exceed calculator precision and identify a discriminating field observation.

## Lesson 4.4: Regional-residual separation and gradients

### The physical mechanism and its measurable consequence

Long-wavelength gravity may arise from crustal thickness or distant structures, while short-wavelength anomalies can reflect near-surface densities. Detrending is mathematically convenient but can remove real geology. Horizontal derivatives emphasize boundaries yet amplify noise.

### Acquisition protocol and observable variables

Plot raw, fitted regional and residual signals together. Vary polynomial order and filter wavelength; retain the processing history.

### The inverse ambiguity: alternative explanations

The same body can appear positive or negative relative to different chosen backgrounds. A false contact may appear at a filter edge.

### Worked calculation: synthetic classroom data

**Question — Sphere peak gravity.** An excess mass 2e11 kg at 1000 m depth gives GM/z²; calculate mGal.

**Explicit computation:** `6.67430e-11*2e11/(1000**2)*1e5` = **1.33486 mGal**. Express the result in the units requested; perform any conversion before substituting into the equation rather than concealing a factor of one thousand in a final sentence. A rounded answer should not imply accuracy better than the synthetic inputs. This arithmetic operation provides a physical scale, not a certified subsurface interpretation.

**Why the calculation matters.** Peak anomaly depends on both mass and burial depth. **Boundary of validity:** Shape and lateral position unresolved. For an independent sensitivity check, change one stated input by ten percent, leaving others fixed. Explain how the result responds, and whether a plausible alternative hypothesis could produce the same scalar.

### Practical: an observation that could disprove the preferred model

Perform two interpretations with different defensible filters and retain only structural claims robust to both.

**Physical sanity test.** Evaluate the model at an extreme but admissible input and check dimensions, sign, limiting behaviour and plausibility. A correct arithmetic result with a broken physical assumption is not a sound geological conclusion. Draw a table containing at least two testable predictions, the needed instrument reading, its physical units, and one reason the observation might be biased.

### Analysis note: how to decide whether the interpretation survives

**Track the reference frame.** Coordinates, vertical datums, event origin times, magnetic epochs and polarity conventions are parts of the measurement. Confusing reference frames can shift all stations coherently without producing conspicuous random residuals. In the context of **regional-residual separation and gradients**, explain what a reviewer should expect to see in raw data if the mechanism is credible, and what unexpected pattern would require a revised geological model.

### Synthesis and interpretation checkpoint

Write a short technical conclusion that separates three items: (1) what the instrument directly records in the gravity surveying and the earth's gravity field problem; (2) the material property or process inferred from it; and (3) a geological claim that would still be unsupported. The exercise is not passed merely by obtaining 1.33486 mGal. Explain why the uncertainty in the assumptions can exceed calculator precision and identify a discriminating field observation.

## Lesson 4.5: Gravity interpretation with independent constraints

### The physical mechanism and its measurable consequence

Gravity and seismic velocity respond differently to composition, porosity and pressure. A joint inversion may reduce ambiguity when the relation between density and velocity is justified, but an assumed relation can force an incorrect geological answer.

### Acquisition protocol and observable variables

Validate rock-density priors with samples, check velocity calibration independently and reserve a survey line for testing.

### The inverse ambiguity: alternative explanations

A small joint misfit can be manufactured by over-weighting uncertain data or imposing a rigid petrophysical relation.

### Worked calculation: synthetic classroom data

**Question — Density contrast.** A target density=2850, background=2600 kg/m³; calculate excess density.

**Explicit computation:** `2850-2600` = **250 kg/m³**. Express the result in the units requested; perform any conversion before substituting into the equation rather than concealing a factor of one thousand in a final sentence. A rounded answer should not imply accuracy better than the synthetic inputs. This arithmetic operation provides a physical scale, not a certified subsurface interpretation.

**Why the calculation matters.** Density contrast sets anomaly sign under simple geometry. **Boundary of validity:** Real rocks have porosity and mixed mineralogy. For an independent sensitivity check, change one stated input by ten percent, leaving others fixed. Explain how the result responds, and whether a plausible alternative hypothesis could produce the same scalar.

### Practical: an observation that could disprove the preferred model

Report an ensemble of acceptable density structures and the drilling result that would most efficiently discriminate them.

**Data stewardship.** Document synthetic status, provenance, coordinates, units, processing version, license and intended use. Keep measurements in a separate file from interpolated or inversion-derived quantities. Draw a table containing at least two testable predictions, the needed instrument reading, its physical units, and one reason the observation might be biased.

### Analysis note: how to decide whether the interpretation survives

**Use a withheld test.** Fit the parameters with one subset and predict genuinely unobserved measurements. Spatial clustering, repeated use of validation stations or tuning after inspecting the holdout exaggerates predictive evidence. In the context of **gravity interpretation with independent constraints**, explain what a reviewer should expect to see in raw data if the mechanism is credible, and what unexpected pattern would require a revised geological model.

### Synthesis and interpretation checkpoint

Write a short technical conclusion that separates three items: (1) what the instrument directly records in the gravity surveying and the earth's gravity field problem; (2) the material property or process inferred from it; and (3) a geological claim that would still be unsupported. The exercise is not passed merely by obtaining 250 kg/m³. Explain why the uncertainty in the assumptions can exceed calculator precision and identify a discriminating field observation.

## Research clinic — the invisible gravity source family

A spherical excess mass under a gravity profile gives a simple analytic forward experiment. The peak acceleration depends on excess mass divided by squared distance. If observed peak is fixed, increasing depth and excess mass together can preserve much of the central anomaly. Profile width partly constrains depth, but limited station extent leaves broad parameter families viable. A textbook inversion that returns exactly one depth and radius should show what prior or bounds eliminated the others.

Field corrections are not optional decoration. Gravity varies with elevation, geographic position and time. A gravimeter can drift; Earth's tides change local readings. A free-air correction adjusts for first-order height difference, while the ideal Bouguer slab accounts approximately for rock mass between the station and datum. The slab approximation does not represent a canyon or mountain wall. Confusing the sign or applied density of these corrections can create large coherent errors that a geological inversion will then misinterpret as a buried source.

An instructive exercise constructs two anomaly profiles from the same invented body: one before reduction and one after a deliberately incorrect elevation correction. Students should identify the calibration error from base-station ties and independent elevation records before attempting any geological story. If only the processed anomaly is given, error detection becomes difficult; that is why raw readings and processing metadata must accompany published maps.

Regional-residual separation deserves its own uncertainty experiment. Fit a first-order trend, a second-order trend and a smoothing spline to exactly the same station set. Show how each choice changes the sign and amplitude of remaining anomalies. The plotted residual is mathematically real but its geological meaning depends on the removed reference. Interpret only features robust to multiple defensible reductions, or clearly show the dependence. Geological samples and seismic constraints should restrict the density assumptions before gravity alone is used to claim an intrusive structure.


## Unit investigation: reproducible synthetic dataset and experimental design

**Research aim.** The invented scenario is: A classroom gravity transect crosses a notional buried intrusion and an adjacent basin. The observed change contains instrument drift, free-air and latitude effects as well as possible density variations; a unique body depth cannot be assumed. Treat `datasets/unit-04.csv` as forty fictional rows deliberately designed to exercise quality control and model criticism. Read the file header before drawing any map. Plot the two relevant measured fields from unit 4; display the `quality_flag` column rather than deleting all flagged stations silently. The synthetic table contains no geographic coordinate reference system or real site identifiers and cannot be used to identify a place.

**Part A — raw measurements and dimensions.** Read each column as a quantity, not as a decorative label. For gravity surveying and the earth's gravity field, check whether the stated units are compatible with its equation and record which columns represent observed signals, instrument corrections, independent controls or model-derived quantities. Identify missing information such as date, site geology, true coordinate system, instrument orientation or calibration. If those omissions prevent a physical inversion, state the limitation and limit the task to transparent exploratory analysis. This is a stronger result than assigning fictitious precision.

**Part B — repeat and quality flags.** Count the rows marked `review`. Compare summary statistics, plotted gradients and model parameters with all forty records against the subset that passes the flag. Document every change; flags indicate inspection priority, not a universal mandate to delete. Check whether questionable values cluster along position or signal amplitude, because exclusions can introduce bias. If the noise appears correlated, do not assume a root-sum-square independent-error formula without a justification.

**Part C — model competition.** Describe two geophysical models that explain the synthetic observations in gravity surveying and the earth's gravity field; they must differ in physical property, geometry or forcing rather than just parameter precision. For each hypothesis make an observable prediction about station response, uncertainty pattern, external control or independent method. Select one new measurement that would best discriminate them, and explain its predicted signal under both hypotheses. A new dense sample from the same short profile may add less independent information than a crossing line or sample.

**Part D — numerical sensitivity.** Recompute one of the unit worked cases with the principal input increased by 10% and decreased by 10%. Check if the response is linear, inverse, logarithmic, quadratic or subject to another nonlinearity. Show a table with input, computed output, unit and physical assumption. Do not claim a sensitivity of the geological interpretation itself if only the toy forward equation was changed; the inverse solution may have a much broader family of possibilities.

**Part E — out-of-sample prediction and reporting.** Split the synthetic observations by physical position, retaining a contiguous group as a blind holdout. Fit a deliberately simple forward trend to remaining rows and predict the held-out quantity without retuning. Compare predictive error with a baseline that uses a constant mean. State why geographic separation can be a stronger test than random point withholding. Report all transformations, quality flags, fitted parameters, residual plots and failure modes in a compact methods appendix.

**Unit-specific evidence synthesis.** Gravity measurements encode mass distribution and distance, not rock names. The observed acceleration contains latitude, elevation, tides, instrumental drift and local topographic mass as well as subsurface heterogeneity. Bouguer and terrain corrections are model-based conventions that must be documented; incorrect density assumptions can shift anomaly magnitude and interpretation. Regional-residual separation changes what features appear significant. A dense shallow body can mimic a larger deeper body; gravity inversion therefore benefits from independent constraints on geometry and density. A residual small enough for publication is not proof of a unique body shape. Map the chain of evidence from sensor to interpretation; highlight an uncertainty not reducible by extra decimal places. In your conclusion, indicate which measurement you would acquire next if the synthetic experiment were replaced with licensed real-world data. Keep any real data sourced from the references separate from these forty invented rows.

**Suggested report.** Submit a transparent CSV-reading script or spreadsheet calculation, one raw-data figure, a sensitivity plot, two candidate geological explanations, a withheld-test result and a one-page uncertainty ledger. Grade on conceptual correctness (25%), numerical units and reproducibility (25%), alternate hypotheses (20%), validation logic (20%) and scientific communication (10%). Never reward a map for appearing more certain than its underlying observations.

## End-of-unit reflection and problems

1. Identify which part of **gravity surveying and the earth's gravity field** would remain ambiguous even if measurement noise were reduced to zero. Explain how the survey geometry or parameter relationship creates that ambiguity.

2. Find a case where a large change in the observed signal would not imply a proportionally large change in target size. Write the forward relation, name fixed parameters, and state why inversion differs from prediction.

3. Propose a new survey that would risk rejecting the preferred geological interpretation. Its value should be based on discriminating predictions rather than its technological sophistication.

4. Draw a data lineage chart from raw instrument data through correction, inversion and geological claim. Underline any operation that assumes a material property not measured in the original dataset.

5. Explain why the synthetic data and interactive sliders are educational examples and cannot support emergency warnings, ground-investigation certification, resource appraisal or environmental enforcement.

## Additional reading and independent replication

Use `REFERENCES.md` to find a genuine program or open repository relevant to gravity surveying and the earth's gravity field. Before downloading any data, check the provider documentation, citation requirements, usage permissions and the time period represented. Record the instrument type, station metadata and acquisition geometry, then reproduce one simple physical calculation from scratch. The objective is not to match a published colored inversion image exactly; it is to understand the observable and give a defensible account of differences.


## Interactive physical-model explanations

Open this chapter in the HTML reader to change one controlled physical variable at a time. Each model is a simplified *forward* calculation, not an inversion or a real-world estimator.

### Free-air correction magnitude

Input quantity: Height above datum measured in m; demonstration range 0–1000, initial setting 300. Output: mGal. Computed from `0.3086*x`.

**Unmodelled influences and interpretation boundary:** First-order 0.3086 mGal/m magnitude only; correction sign set by reduction convention. Students should articulate a case where this formula yields a numerically precise but physically misleading answer and state an independently measurable quantity needed for a more complete model.

### Bouguer slab attraction magnitude

Input quantity: Height of slab measured in m; demonstration range 0–500, initial setting 150. Output: mGal. Computed from `2*Math.PI*6.67430e-11*2670*x*100000`.

**Unmodelled influences and interpretation boundary:** Infinite slab and density 2670 kg/m³, omits terrain. Students should articulate a case where this formula yields a numerically precise but physically misleading answer and state an independently measurable quantity needed for a more complete model.
