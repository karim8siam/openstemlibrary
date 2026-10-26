# Unit 2: Seismology and earthquake source physics

## Central question: What can wave arrival times and source measurements actually reveal?

**Fictional unit investigation:** A synthetic earthquake sequence is recorded by a sparse network. P and S picks have uncertain onset times; station geometry is asymmetric and shallow site effects influence amplitudes. Competing earthquake locations and magnitudes need to be tested.

## Geophysical foundation and the measurement-to-model chain

Earthquake hypocenters are located with travel-time observations and a velocity model. A P wave is generally faster than an S wave in an ordinary elastic solid, but heterogeneous three-dimensional Earth structure makes single-velocity calculations approximate. Event magnitude describes a source-related scale, not directly the damage at one building. Local shaking depends on source distance, rupture directivity, path attenuation, near-surface conditions and structures. First motion polarity, waveform spectra and geodetic displacement help constrain source processes, but trade-offs and station geometry remain. Do not treat a classroom location algorithm as a warning system or a validated seismic-hazard model.

## Five lessons: hypotheses, observables and field checks

For each lesson the forward physics and observation type are explicit. The lesson is complete only when the student can name a competing explanation, check units in the worked calculation and explain a measurement that could reject the preferred interpretation. Every stated numerical value is invented for this textbook; none is a field station or an operational parameter.

## Lesson 2.1: P and S wave propagation

### The physical mechanism and its measurable consequence

P waves involve compressional elastic motion, while S waves carry shear deformation and cannot propagate as body shear waves through an ideal fluid. Speeds depend on elastic moduli and density, and gradients bend seismic rays. A single constant speed is an instructive first approximation but rarely a complete Earth model.

### Acquisition protocol and observable variables

Identify first arrivals on three-component seismograms, estimate pickup uncertainty, and use distance-dependent travel-time curves to compare phases.

### The inverse ambiguity: alternative explanations

An impulsive anthropogenic source may resemble an earthquake. A waveform pick can attach to the wrong seismic phase, especially where noise masks onset.

### Worked calculation: synthetic classroom data

**Question — Wave-speed ratio.** P and S speeds are 6.0 and 3.5 km/s; calculate P/S speed ratio.

**Explicit computation:** `6.0/3.5` = **1.714286 ratio**. Express the result in the units requested; perform any conversion before substituting into the equation rather than concealing a factor of one thousand in a final sentence. A rounded answer should not imply accuracy better than the synthetic inputs. This arithmetic operation provides a physical scale, not a certified subsurface interpretation.

**Why the calculation matters.** P speed exceeds S speed in the assumed medium. **Boundary of validity:** The ratio does not locate an event or determine all elastic moduli. For an independent sensitivity check, change one stated input by ten percent, leaving others fixed. Explain how the result responds, and whether a plausible alternative hypothesis could produce the same scalar.

### Practical: an observation that could disprove the preferred model

Plot travel-time predictions for two source distances and discuss how an incorrect S-wave identification biases the estimated distance.

**Data stewardship.** Document synthetic status, provenance, coordinates, units, processing version, license and intended use. Keep measurements in a separate file from interpolated or inversion-derived quantities. Draw a table containing at least two testable predictions, the needed instrument reading, its physical units, and one reason the observation might be biased.

### Analysis note: how to decide whether the interpretation survives

**Inspect the observation footprint.** Ask which wavelengths and parts of the Earth contribute to the instrument. Potential fields integrate over substantial volumes, seismic picks follow ray paths and electrode arrays have diffuse sensitivity; a pixel-sized interpretation usually exceeds the resolving claim. In the context of **p and s wave propagation**, explain what a reviewer should expect to see in raw data if the mechanism is credible, and what unexpected pattern would require a revised geological model.

### Synthesis and interpretation checkpoint

Write a short technical conclusion that separates three items: (1) what the instrument directly records in the seismology and earthquake source physics problem; (2) the material property or process inferred from it; and (3) a geological claim that would still be unsupported. The exercise is not passed merely by obtaining 1.714286 ratio. Explain why the uncertainty in the assumptions can exceed calculator precision and identify a discriminating field observation.

## Lesson 2.2: Earthquake origin time and hypocenter location

### The physical mechanism and its measurable consequence

Travel-time inversion estimates source position and origin time jointly. A network of stations concentrated on one side of an event has weak azimuthal coverage and may have larger location uncertainties perpendicular to the array. A three-dimensional velocity structure can bias locations obtained with a one-dimensional model.

### Acquisition protocol and observable variables

Record P arrival time, station elevation, pick uncertainty, network geometry and reference Earth model. Compare location results after removing one station or changing velocity.

### The inverse ambiguity: alternative explanations

A small residual does not imply the absolute epicenter is exact when all travel times share the same model bias. Depth may be especially weakly constrained.

### Worked calculation: synthetic classroom data

**Question — S–P lag.** A source is 42 km away; vP=6 km/s, vS=3.5 km/s; calculate S minus P arrival lag.

**Explicit computation:** `42/3.5-42/6` = **5 s**. Express the result in the units requested; perform any conversion before substituting into the equation rather than concealing a factor of one thousand in a final sentence. A rounded answer should not imply accuracy better than the synthetic inputs. This arithmetic operation provides a physical scale, not a certified subsurface interpretation.

**Why the calculation matters.** The lag is a rough distance cue. **Boundary of validity:** Straight ray paths and uniform medium assumed. For an independent sensitivity check, change one stated input by ten percent, leaving others fixed. Explain how the result responds, and whether a plausible alternative hypothesis could produce the same scalar.

### Practical: an observation that could disprove the preferred model

Simulate a move of the hypocenter by 10 km and inspect which station supplies the strongest added travel-time leverage.

**Acquisition design.** Define the physical source, sensor property, site geometry and independent calibration needed before collecting data. State which raw channels must survive processing and what a second researcher could reproduce. Draw a table containing at least two testable predictions, the needed instrument reading, its physical units, and one reason the observation might be biased.

### Analysis note: how to decide whether the interpretation survives

**State the forward equation and its domain.** Write the physical equation together with geometry, units and assumed constants. List a realistic departure that changes the prediction and distinguish a useful approximation from an unjustified physical claim. In the context of **earthquake origin time and hypocenter location**, explain what a reviewer should expect to see in raw data if the mechanism is credible, and what unexpected pattern would require a revised geological model.

### Synthesis and interpretation checkpoint

Write a short technical conclusion that separates three items: (1) what the instrument directly records in the seismology and earthquake source physics problem; (2) the material property or process inferred from it; and (3) a geological claim that would still be unsupported. The exercise is not passed merely by obtaining 5 s. Explain why the uncertainty in the assumptions can exceed calculator precision and identify a discriminating field observation.

## Lesson 2.3: Magnitude, moment and intensity

### The physical mechanism and its measurable consequence

Seismic moment relates rigidity, rupture area and average slip. Moment magnitude uses a logarithmic scale derived from seismic moment in SI units. Intensity describes observed shaking consequences at locations and is not identical to magnitude. Energy statements require careful definitions and should not equate every magnitude increment with a fixed engineering impact.

### Acquisition protocol and observable variables

Distinguish moment tensor estimates from local amplitude magnitudes; specify instrument response, bandwidth and reference convention. Map intensity reports independently from magnitudes.

### The inverse ambiguity: alternative explanations

Saturated magnitude scales, attenuation and soil amplification may cause inconsistent estimates. Media reports may conflate event size with damage.

### Worked calculation: synthetic classroom data

**Question — Moment magnitude.** Moment M0=1e18 N m; compute Mw=(2/3)(log10 M0-9.1).

**Explicit computation:** `(2/3)*(math.log10(1e18)-9.1)` = **5.933333 Mw**. Express the result in the units requested; perform any conversion before substituting into the equation rather than concealing a factor of one thousand in a final sentence. A rounded answer should not imply accuracy better than the synthetic inputs. This arithmetic operation provides a physical scale, not a certified subsurface interpretation.

**Why the calculation matters.** The scale is logarithmic; the units convention is N m. **Boundary of validity:** A given magnitude does not forecast individual-site damage. For an independent sensitivity check, change one stated input by ten percent, leaving others fixed. Explain how the result responds, and whether a plausible alternative hypothesis could produce the same scalar.

### Practical: an observation that could disprove the preferred model

Write a public summary stating which source property was measured and which outcomes cannot be predicted from magnitude alone.

**Competing models.** Choose two different geologic or instrumental explanations for the observation and write one numerical or spatial prediction on which they disagree. Reserve a new observation as a prospective test. Draw a table containing at least two testable predictions, the needed instrument reading, its physical units, and one reason the observation might be biased.

### Analysis note: how to decide whether the interpretation survives

**Decide a safe intended use.** Clarify whether the result is a numerical exercise, exploratory screening, academic interpretation or professional decision product. Educational calculations do not confer authority to make engineering, emergency or environmental determinations. In the context of **magnitude, moment and intensity**, explain what a reviewer should expect to see in raw data if the mechanism is credible, and what unexpected pattern would require a revised geological model.

### Synthesis and interpretation checkpoint

Write a short technical conclusion that separates three items: (1) what the instrument directly records in the seismology and earthquake source physics problem; (2) the material property or process inferred from it; and (3) a geological claim that would still be unsupported. The exercise is not passed merely by obtaining 5.933333 Mw. Explain why the uncertainty in the assumptions can exceed calculator precision and identify a discriminating field observation.

## Lesson 2.4: Source mechanisms, faults and rupture

### The physical mechanism and its measurable consequence

Double-couple moment tensors describe ideal shear dislocation; nodal-plane ambiguity means first motion patterns alone can yield two candidate planes. Directivity, rupture speed and finite fault geometry affect radiation and shaking patterns. The focal mechanism is not an automatically mapped surface rupture.

### Acquisition protocol and observable variables

Map polarities with takeoff angles and uncertainties; compare centroid moment tensor solutions with local fault traces and aftershock patterns.

### The inverse ambiguity: alternative explanations

A nodal plane is not necessarily the actual rupture plane. Poor station coverage can obscure non-double-couple components and change interpreted rake.

### Worked calculation: synthetic classroom data

**Question — Rupture moment.** Take rigidity 30 GPa, area 20 km² and average slip 0.5 m; find M0 in N m.

**Explicit computation:** `30e9*(20e6)*0.5` = **3e+17 N m**. Express the result in the units requested; perform any conversion before substituting into the equation rather than concealing a factor of one thousand in a final sentence. A rounded answer should not imply accuracy better than the synthetic inputs. This arithmetic operation provides a physical scale, not a certified subsurface interpretation.

**Why the calculation matters.** Moment is shear modulus times rupture area times average slip. **Boundary of validity:** Uniform slip and elastic properties are idealized. For an independent sensitivity check, change one stated input by ten percent, leaving others fixed. Explain how the result responds, and whether a plausible alternative hypothesis could produce the same scalar.

### Practical: an observation that could disprove the preferred model

Sketch two candidate fault planes and list field or geodetic observations that could discriminate the actual rupture surface.

**Error budget.** Separate repeatability, calibration bias, position error and model uncertainty in a table with units. Decide which uncertainty dominates the interpretation and what extra information would shrink it. Draw a table containing at least two testable predictions, the needed instrument reading, its physical units, and one reason the observation might be biased.

### Analysis note: how to decide whether the interpretation survives

**Track the reference frame.** Coordinates, vertical datums, event origin times, magnetic epochs and polarity conventions are parts of the measurement. Confusing reference frames can shift all stations coherently without producing conspicuous random residuals. In the context of **source mechanisms, faults and rupture**, explain what a reviewer should expect to see in raw data if the mechanism is credible, and what unexpected pattern would require a revised geological model.

### Synthesis and interpretation checkpoint

Write a short technical conclusion that separates three items: (1) what the instrument directly records in the seismology and earthquake source physics problem; (2) the material property or process inferred from it; and (3) a geological claim that would still be unsupported. The exercise is not passed merely by obtaining 3e+17 N m. Explain why the uncertainty in the assumptions can exceed calculator precision and identify a discriminating field observation.

## Lesson 2.5: Seismic site effects and hazard boundaries

### The physical mechanism and its measurable consequence

Soft sedimentary basins can trap and amplify certain frequencies, while near-surface shear speed and impedance contrasts influence site response. Shaking intensity depends on source, path and site, and many other variables affect structural outcomes. A classroom amplification ratio is not a code-compliant site classification.

### Acquisition protocol and observable variables

Compare rock and soil sensor spectra using compatible calibration and frequency windows. Record local geology, soil thickness and basin geometry.

### The inverse ambiguity: alternative explanations

Differing source azimuths, sensor installation or near-field effects can appear as site amplification. A single event cannot define a long-term hazard spectrum.

### Worked calculation: synthetic classroom data

**Question — Period.** A surface shaking frequency is 2.5 Hz; calculate the period.

**Explicit computation:** `1/2.5` = **0.4 s**. Express the result in the units requested; perform any conversion before substituting into the equation rather than concealing a factor of one thousand in a final sentence. A rounded answer should not imply accuracy better than the synthetic inputs. This arithmetic operation provides a physical scale, not a certified subsurface interpretation.

**Why the calculation matters.** Period and frequency are reciprocal. **Boundary of validity:** Building resonance is more complex than one period. For an independent sensitivity check, change one stated input by ten percent, leaving others fixed. Explain how the result responds, and whether a plausible alternative hypothesis could produce the same scalar.

### Practical: an observation that could disprove the preferred model

Develop a paired-station analysis with at least two events and explain why extrapolation to building safety is inappropriate.

**Sensitivity study.** Alter the assumed physical-property contrast, source depth or acquisition spacing. Determine whether the sign of the conclusion persists or whether the interpretation is contingent on a narrow prior. Draw a table containing at least two testable predictions, the needed instrument reading, its physical units, and one reason the observation might be biased.

### Analysis note: how to decide whether the interpretation survives

**Use a withheld test.** Fit the parameters with one subset and predict genuinely unobserved measurements. Spatial clustering, repeated use of validation stations or tuning after inspecting the holdout exaggerates predictive evidence. In the context of **seismic site effects and hazard boundaries**, explain what a reviewer should expect to see in raw data if the mechanism is credible, and what unexpected pattern would require a revised geological model.

### Synthesis and interpretation checkpoint

Write a short technical conclusion that separates three items: (1) what the instrument directly records in the seismology and earthquake source physics problem; (2) the material property or process inferred from it; and (3) a geological claim that would still be unsupported. The exercise is not passed merely by obtaining 0.4 s. Explain why the uncertainty in the assumptions can exceed calculator precision and identify a discriminating field observation.

## Research clinic — what seismic arrival times cannot promise

A synthetic network records a sharp onset at five stations, but only two stations lie south of the source. Assign arrival-pick uncertainty and derive a family of possible source locations under a reference velocity model. The least-squares minimum may be precise in one direction and elongated in another. Instead of drawing a circle around a single epicenter, draw the confidence region implied by station geometry and model uncertainty. Model errors shared by all ray paths cannot be eliminated by treating picks as independent.

P-to-S time difference provides a transparent classroom estimate of range under uniform isotropic velocities. In reality, ray bending, discontinuities and phase misidentification change the relationship between distance and time. A student should therefore keep the approximate lag calculation separate from network relocation and regional travel-time tables. For a poorly instrumented region, estimating a location with decimals that exceed the model's information is especially misleading.

Earthquake magnitude and local intensity must never be merged. A moment-magnitude estimate attempts to characterize seismic source size, whereas observed shaking at a site depends on numerous physical and human variables. A larger event can produce weaker motion at a distant rock site than a smaller nearby event at soft soil. Demonstrate this using two hypothetical stations with different soil conditions, but do not turn the classroom comparison into a site-specific hazard assessment. Official hazard products combine long-term seismicity, fault recurrence assumptions, attenuation models and uncertainty.

Focal-mechanism diagrams show possible shear-source orientations. They are not photographs of the actual ruptured fault. Nodal-plane ambiguity remains until geological or geodetic evidence distinguishes the candidate plane. Require an evidence table in which waveform polarity, aftershock alignment, mapped faults and satellite displacement are separate rows. Two rows originating from the same waveform inversion do not count as independent confirmation. The outcome may remain a pair of candidate source models, which is a scientifically legitimate result.


## Unit investigation: reproducible synthetic dataset and experimental design

**Research aim.** The invented scenario is: A synthetic earthquake sequence is recorded by a sparse network. P and S picks have uncertain onset times; station geometry is asymmetric and shallow site effects influence amplitudes. Competing earthquake locations and magnitudes need to be tested. Treat `datasets/unit-02.csv` as forty fictional rows deliberately designed to exercise quality control and model criticism. Read the file header before drawing any map. Plot the two relevant measured fields from unit 2; display the `quality_flag` column rather than deleting all flagged stations silently. The synthetic table contains no geographic coordinate reference system or real site identifiers and cannot be used to identify a place.

**Part A — raw measurements and dimensions.** Read each column as a quantity, not as a decorative label. For seismology and earthquake source physics, check whether the stated units are compatible with its equation and record which columns represent observed signals, instrument corrections, independent controls or model-derived quantities. Identify missing information such as date, site geology, true coordinate system, instrument orientation or calibration. If those omissions prevent a physical inversion, state the limitation and limit the task to transparent exploratory analysis. This is a stronger result than assigning fictitious precision.

**Part B — repeat and quality flags.** Count the rows marked `review`. Compare summary statistics, plotted gradients and model parameters with all forty records against the subset that passes the flag. Document every change; flags indicate inspection priority, not a universal mandate to delete. Check whether questionable values cluster along position or signal amplitude, because exclusions can introduce bias. If the noise appears correlated, do not assume a root-sum-square independent-error formula without a justification.

**Part C — model competition.** Describe two geophysical models that explain the synthetic observations in seismology and earthquake source physics; they must differ in physical property, geometry or forcing rather than just parameter precision. For each hypothesis make an observable prediction about station response, uncertainty pattern, external control or independent method. Select one new measurement that would best discriminate them, and explain its predicted signal under both hypotheses. A new dense sample from the same short profile may add less independent information than a crossing line or sample.

**Part D — numerical sensitivity.** Recompute one of the unit worked cases with the principal input increased by 10% and decreased by 10%. Check if the response is linear, inverse, logarithmic, quadratic or subject to another nonlinearity. Show a table with input, computed output, unit and physical assumption. Do not claim a sensitivity of the geological interpretation itself if only the toy forward equation was changed; the inverse solution may have a much broader family of possibilities.

**Part E — out-of-sample prediction and reporting.** Split the synthetic observations by physical position, retaining a contiguous group as a blind holdout. Fit a deliberately simple forward trend to remaining rows and predict the held-out quantity without retuning. Compare predictive error with a baseline that uses a constant mean. State why geographic separation can be a stronger test than random point withholding. Report all transformations, quality flags, fitted parameters, residual plots and failure modes in a compact methods appendix.

**Unit-specific evidence synthesis.** Earthquake hypocenters are located with travel-time observations and a velocity model. A P wave is generally faster than an S wave in an ordinary elastic solid, but heterogeneous three-dimensional Earth structure makes single-velocity calculations approximate. Event magnitude describes a source-related scale, not directly the damage at one building. Local shaking depends on source distance, rupture directivity, path attenuation, near-surface conditions and structures. First motion polarity, waveform spectra and geodetic displacement help constrain source processes, but trade-offs and station geometry remain. Do not treat a classroom location algorithm as a warning system or a validated seismic-hazard model. Map the chain of evidence from sensor to interpretation; highlight an uncertainty not reducible by extra decimal places. In your conclusion, indicate which measurement you would acquire next if the synthetic experiment were replaced with licensed real-world data. Keep any real data sourced from the references separate from these forty invented rows.

**Suggested report.** Submit a transparent CSV-reading script or spreadsheet calculation, one raw-data figure, a sensitivity plot, two candidate geological explanations, a withheld-test result and a one-page uncertainty ledger. Grade on conceptual correctness (25%), numerical units and reproducibility (25%), alternate hypotheses (20%), validation logic (20%) and scientific communication (10%). Never reward a map for appearing more certain than its underlying observations.

## End-of-unit reflection and problems

1. Identify which part of **seismology and earthquake source physics** would remain ambiguous even if measurement noise were reduced to zero. Explain how the survey geometry or parameter relationship creates that ambiguity.

2. Find a case where a large change in the observed signal would not imply a proportionally large change in target size. Write the forward relation, name fixed parameters, and state why inversion differs from prediction.

3. Propose a new survey that would risk rejecting the preferred geological interpretation. Its value should be based on discriminating predictions rather than its technological sophistication.

4. Draw a data lineage chart from raw instrument data through correction, inversion and geological claim. Underline any operation that assumes a material property not measured in the original dataset.

5. Explain why the synthetic data and interactive sliders are educational examples and cannot support emergency warnings, ground-investigation certification, resource appraisal or environmental enforcement.

## Additional reading and independent replication

Use `REFERENCES.md` to find a genuine program or open repository relevant to seismology and earthquake source physics. Before downloading any data, check the provider documentation, citation requirements, usage permissions and the time period represented. Record the instrument type, station metadata and acquisition geometry, then reproduce one simple physical calculation from scratch. The objective is not to match a published colored inversion image exactly; it is to understand the observable and give a defensible account of differences.


## Interactive physical-model explanations

Open this chapter in the HTML reader to change one controlled physical variable at a time. Each model is a simplified *forward* calculation, not an inversion or a real-world estimator.

### S minus P arrival lag

Input quantity: Source distance measured in km; demonstration range 1–200, initial setting 42. Output: s. Computed from `x/3.5-x/6`.

**Unmodelled influences and interpretation boundary:** Homogeneous straight-ray approximation only. Students should articulate a case where this formula yields a numerically precise but physically misleading answer and state an independently measurable quantity needed for a more complete model.

### Moment magnitude from seismic moment

Input quantity: Seismic moment in 10^18 N m measured in 10¹⁸ N m; demonstration range 0.01–200, initial setting 1. Output: Mw. Computed from `(2/3)*(Math.log10(x*1e18)-9.1)`.

**Unmodelled influences and interpretation boundary:** Magnitude expression uses SI N m and fixed convention. Students should articulate a case where this formula yields a numerically precise but physically misleading answer and state an independently measurable quantity needed for a more complete model.
