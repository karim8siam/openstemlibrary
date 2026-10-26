# Unit 7: Heat flow, geodesy and integrated Earth processes

## Central question: How can temperature gradients, deformation and physical budgets constrain active geological systems?

**Fictional unit investigation:** A synthetic rift segment contains borehole temperature logs, GPS displacement vectors and an incomplete heat-flow transect. The team compares competing tectonic and hydrologic models before interpreting hazard or energy potential.

## Geophysical foundation and the measurement-to-model chain

Conductive terrestrial heat flow is conventionally approximated by Fourier's law, but advective groundwater flow, transient climate histories and heterogeneity modify observed temperature profiles. Satellite and GNSS deformation offer geometric changes with differing sampling and error structures, not an automatic label for fault slip. InSAR phase depends on displacement toward the satellite as well as atmospheric path delay, orbital effects and surface decorrelation. Thermo-mechanical models relate heat, stress and kinematics, but fitted parameters may trade off strongly. Risk, geothermal resource capacity and fault activity require independent data, validated modelling and appropriate professional review.

## Five lessons: hypotheses, observables and field checks

For each lesson the forward physics and observation type are explicit. The lesson is complete only when the student can name a competing explanation, check units in the worked calculation and explain a measurement that could reject the preferred interpretation. Every stated numerical value is invented for this textbook; none is a field station or an operational parameter.

## Lesson 7.1: Conductive heat flow and gradients

### The physical mechanism and its measurable consequence

Fourier's law connects conductive heat flux with thermal conductivity and temperature gradient in a one-dimensional approximation. Heat-flow direction is opposite increasing temperature under the chosen coordinate sign; surface heat flux may have topographic and climatic transients.

### Acquisition protocol and observable variables

Record calibrated borehole temperatures versus equilibrium depth, thermal conductivity measurements and groundwater indicators.

### The inverse ambiguity: alternative explanations

Advective flow, recent drilling disturbance and paleoclimate can bend a temperature log; linear fits are not universally valid.

### Worked calculation: synthetic classroom data

**Question — Conductive heat flow.** Take conductivity 2.5 W/(m K), temperature increase 25 K/km; compute flux magnitude W/m².

**Explicit computation:** `2.5*25/1000` = **0.0625 W/m²**. Express the result in the units requested; perform any conversion before substituting into the equation rather than concealing a factor of one thousand in a final sentence. A rounded answer should not imply accuracy better than the synthetic inputs. This arithmetic operation provides a physical scale, not a certified subsurface interpretation.

**Why the calculation matters.** Magnitude is conductivity times thermal gradient. **Boundary of validity:** Pure one-dimensional steady conduction assumed. For an independent sensitivity check, change one stated input by ten percent, leaving others fixed. Explain how the result responds, and whether a plausible alternative hypothesis could produce the same scalar.

### Practical: an observation that could disprove the preferred model

Compare two conductivity assumptions and compute the implied heat flux without interpreting the result as a certified geothermal reserve.

**Instrument validation.** Compare a repeat transect, crossing line or reciprocal reading with original acquisition. Explain what kind of systematic effect the check is capable of detecting and what remains invisible. Draw a table containing at least two testable predictions, the needed instrument reading, its physical units, and one reason the observation might be biased.

### Analysis note: how to decide whether the interpretation survives

**Inspect the observation footprint.** Ask which wavelengths and parts of the Earth contribute to the instrument. Potential fields integrate over substantial volumes, seismic picks follow ray paths and electrode arrays have diffuse sensitivity; a pixel-sized interpretation usually exceeds the resolving claim. In the context of **conductive heat flow and gradients**, explain what a reviewer should expect to see in raw data if the mechanism is credible, and what unexpected pattern would require a revised geological model.

### Synthesis and interpretation checkpoint

Write a short technical conclusion that separates three items: (1) what the instrument directly records in the heat flow, geodesy and integrated earth processes problem; (2) the material property or process inferred from it; and (3) a geological claim that would still be unsupported. The exercise is not passed merely by obtaining 0.0625 W/m². Explain why the uncertainty in the assumptions can exceed calculator precision and identify a discriminating field observation.

## Lesson 7.2: Geothermal gradients and groundwater advection

### The physical mechanism and its measurable consequence

Heat transport may combine conduction with fluid motion, producing curvature or local anomalies in borehole profiles. Rock heterogeneity and temperature-dependent properties further complicate inference. A single borehole may not describe a geothermal reservoir.

### Acquisition protocol and observable variables

Sample multiple depths after thermal equilibration; log groundwater movement and lithology. Evaluate whether a linear temperature model holds above and below a permeable interval.

### The inverse ambiguity: alternative explanations

Shallow warm water may derive from flow paths rather than high deep heat production; high heat gradient does not specify sustainable extraction rate.

### Worked calculation: synthetic classroom data

**Question — Thermal gradient.** Downhole temperature increases from 15 to 65 C over 2 km; compute C/km.

**Explicit computation:** `(65-15)/2` = **25 C/km**. Express the result in the units requested; perform any conversion before substituting into the equation rather than concealing a factor of one thousand in a final sentence. A rounded answer should not imply accuracy better than the synthetic inputs. This arithmetic operation provides a physical scale, not a certified subsurface interpretation.

**Why the calculation matters.** A temperature difference gradient is simple arithmetic. **Boundary of validity:** Borehole equilibration, advection and depth reference matter. For an independent sensitivity check, change one stated input by ten percent, leaving others fixed. Explain how the result responds, and whether a plausible alternative hypothesis could produce the same scalar.

### Practical: an observation that could disprove the preferred model

Fit a piecewise linear profile and identify where additional hydraulic measurements would most change the interpretation.

**Physical sanity test.** Evaluate the model at an extreme but admissible input and check dimensions, sign, limiting behaviour and plausibility. A correct arithmetic result with a broken physical assumption is not a sound geological conclusion. Draw a table containing at least two testable predictions, the needed instrument reading, its physical units, and one reason the observation might be biased.

### Analysis note: how to decide whether the interpretation survives

**State the forward equation and its domain.** Write the physical equation together with geometry, units and assumed constants. List a realistic departure that changes the prediction and distinguish a useful approximation from an unjustified physical claim. In the context of **geothermal gradients and groundwater advection**, explain what a reviewer should expect to see in raw data if the mechanism is credible, and what unexpected pattern would require a revised geological model.

### Synthesis and interpretation checkpoint

Write a short technical conclusion that separates three items: (1) what the instrument directly records in the heat flow, geodesy and integrated earth processes problem; (2) the material property or process inferred from it; and (3) a geological claim that would still be unsupported. The exercise is not passed merely by obtaining 25 C/km. Explain why the uncertainty in the assumptions can exceed calculator precision and identify a discriminating field observation.

## Lesson 7.3: GNSS displacement and strain rates

### The physical mechanism and its measurable consequence

Repeated GNSS positions constrain surface motion relative to a declared reference frame. Plate velocities, local subsidence and monument motion can all contribute. Extension rate over a baseline provides average strain under a simple geometry but not the full tensor field.

### Acquisition protocol and observable variables

Record station time series, monument stability, antenna changes and common-mode motion. Account for seasonal signals and reference frame changes.

### The inverse ambiguity: alternative explanations

Apparent tectonic displacement can come from groundwater extraction, equipment replacement or reference-frame shifts. A short series is vulnerable to transient bias.

### Worked calculation: synthetic classroom data

**Question — GNSS strain.** Two stations 50 km apart separate at 2 mm/yr; compute 1D strain rate per yr.

**Explicit computation:** `0.002/50000` = **4e-08 1/yr**. Express the result in the units requested; perform any conversion before substituting into the equation rather than concealing a factor of one thousand in a final sentence. A rounded answer should not imply accuracy better than the synthetic inputs. This arithmetic operation provides a physical scale, not a certified subsurface interpretation.

**Why the calculation matters.** Baseline change divided by length gives mean extension strain rate. **Boundary of validity:** Reference frame and three-dimensional strain unresolved. For an independent sensitivity check, change one stated input by ten percent, leaving others fixed. Explain how the result responds, and whether a plausible alternative hypothesis could produce the same scalar.

### Practical: an observation that could disprove the preferred model

Compute baseline extension for a synthetic pair of stations and discuss how a third noncollinear station would change inference.

**Data stewardship.** Document synthetic status, provenance, coordinates, units, processing version, license and intended use. Keep measurements in a separate file from interpolated or inversion-derived quantities. Draw a table containing at least two testable predictions, the needed instrument reading, its physical units, and one reason the observation might be biased.

### Analysis note: how to decide whether the interpretation survives

**Decide a safe intended use.** Clarify whether the result is a numerical exercise, exploratory screening, academic interpretation or professional decision product. Educational calculations do not confer authority to make engineering, emergency or environmental determinations. In the context of **gnss displacement and strain rates**, explain what a reviewer should expect to see in raw data if the mechanism is credible, and what unexpected pattern would require a revised geological model.

### Synthesis and interpretation checkpoint

Write a short technical conclusion that separates three items: (1) what the instrument directly records in the heat flow, geodesy and integrated earth processes problem; (2) the material property or process inferred from it; and (3) a geological claim that would still be unsupported. The exercise is not passed merely by obtaining 4e-08 1/yr. Explain why the uncertainty in the assumptions can exceed calculator precision and identify a discriminating field observation.

## Lesson 7.4: InSAR deformation and line-of-sight ambiguity

### The physical mechanism and its measurable consequence

Interferometric radar phase can reveal line-of-sight displacement but is affected by atmosphere, topography, orbital errors and phase unwrapping. One viewing geometry measures one projection of three-dimensional displacement, so vertical and horizontal components trade off.

### Acquisition protocol and observable variables

Record acquisition geometry, coherence, wavelength, orbital information and atmospheric screening. Compare ascending and descending looks where available.

### The inverse ambiguity: alternative explanations

Vegetation decorrelation and tropospheric delay can resemble geological deformation. A displacement color map does not by itself identify the driving fault.

### Worked calculation: synthetic classroom data

**Question — InSAR line-of-sight.** A 25 mm upward displacement projects onto a line of sight tilted 35 degrees from vertical; find LOS magnitude.

**Explicit computation:** `25*math.cos(math.radians(35))` = **20.4788 mm**. Express the result in the units requested; perform any conversion before substituting into the equation rather than concealing a factor of one thousand in a final sentence. A rounded answer should not imply accuracy better than the synthetic inputs. This arithmetic operation provides a physical scale, not a certified subsurface interpretation.

**Why the calculation matters.** Projection reports only one directional component. **Boundary of validity:** Sign convention and horizontal motion unspecified. For an independent sensitivity check, change one stated input by ten percent, leaving others fixed. Explain how the result responds, and whether a plausible alternative hypothesis could produce the same scalar.

### Practical: an observation that could disprove the preferred model

Project a known displacement vector onto two look directions and show which third component remains poorly observed.

**Acquisition design.** Define the physical source, sensor property, site geometry and independent calibration needed before collecting data. State which raw channels must survive processing and what a second researcher could reproduce. Draw a table containing at least two testable predictions, the needed instrument reading, its physical units, and one reason the observation might be biased.

### Analysis note: how to decide whether the interpretation survives

**Track the reference frame.** Coordinates, vertical datums, event origin times, magnetic epochs and polarity conventions are parts of the measurement. Confusing reference frames can shift all stations coherently without producing conspicuous random residuals. In the context of **insar deformation and line-of-sight ambiguity**, explain what a reviewer should expect to see in raw data if the mechanism is credible, and what unexpected pattern would require a revised geological model.

### Synthesis and interpretation checkpoint

Write a short technical conclusion that separates three items: (1) what the instrument directly records in the heat flow, geodesy and integrated earth processes problem; (2) the material property or process inferred from it; and (3) a geological claim that would still be unsupported. The exercise is not passed merely by obtaining 20.4788 mm. Explain why the uncertainty in the assumptions can exceed calculator precision and identify a discriminating field observation.

## Lesson 7.5: Thermo-mechanical coupling and Earth systems

### The physical mechanism and its measurable consequence

Lithospheric strength depends on stress state, temperature, material properties, fluid pressure and time. Elastic plate flexure, viscous relaxation and brittle faulting respond differently to loading histories. A single fitted effective elastic thickness is a scale-dependent simplification.

### Acquisition protocol and observable variables

Combine heat-flow transects, topographic loading, geodesy and seismic constraints, checking whether each has independent sensitivity.

### The inverse ambiguity: alternative explanations

Similar surface deflection can arise from different rigidity–load combinations; high temperature is not proof of imminent rupture.

### Worked calculation: synthetic classroom data

**Question — Flexural stiffness scaling.** For equal E and nu, plate thickness grows 2 to 3 km; calculate stiffness ratio (3/2)^3.

**Explicit computation:** `(3/2)**3` = **3.375 ratio**. Express the result in the units requested; perform any conversion before substituting into the equation rather than concealing a factor of one thousand in a final sentence. A rounded answer should not imply accuracy better than the synthetic inputs. This arithmetic operation provides a physical scale, not a certified subsurface interpretation.

**Why the calculation matters.** Plate rigidity is strongly thickness-dependent in thin elastic theory. **Boundary of validity:** Lithospheric effective thickness not identical to actual single layer. For an independent sensitivity check, change one stated input by ten percent, leaving others fixed. Explain how the result responds, and whether a plausible alternative hypothesis could produce the same scalar.

### Practical: an observation that could disprove the preferred model

Design a model comparison where predicted curvature, thermal gradient and seismicity differ between two competing rift models.

**Competing models.** Choose two different geologic or instrumental explanations for the observation and write one numerical or spatial prediction on which they disagree. Reserve a new observation as a prospective test. Draw a table containing at least two testable predictions, the needed instrument reading, its physical units, and one reason the observation might be biased.

### Analysis note: how to decide whether the interpretation survives

**Use a withheld test.** Fit the parameters with one subset and predict genuinely unobserved measurements. Spatial clustering, repeated use of validation stations or tuning after inspecting the holdout exaggerates predictive evidence. In the context of **thermo-mechanical coupling and earth systems**, explain what a reviewer should expect to see in raw data if the mechanism is credible, and what unexpected pattern would require a revised geological model.

### Synthesis and interpretation checkpoint

Write a short technical conclusion that separates three items: (1) what the instrument directly records in the heat flow, geodesy and integrated earth processes problem; (2) the material property or process inferred from it; and (3) a geological claim that would still be unsupported. The exercise is not passed merely by obtaining 3.375 ratio. Explain why the uncertainty in the assumptions can exceed calculator precision and identify a discriminating field observation.

## Research clinic — heat and deformation are records of several processes

A geothermal gradient from two points does not determine recoverable geothermal power. Fourier's relation assumes conductive, often steady, transport with known thermal conductivity. Groundwater advection can move heat in ways that make the log curved or locally anomalous; topography, recent climate and drilling disturbance also influence temperature. A heat-flux estimate should therefore name the sampled depth interval, equilibrium status and conductivity method. Treat a one-dimensional calculation as a first physical scale check, not a resource certification.

Similarly, the difference between two GNSS station velocities indicates relative motion along a baseline in a particular reference frame. It cannot by itself identify a fault plane, assign the movement to plate tectonics or recover a full strain tensor. Seasonal loading, groundwater pumping and unstable monuments may create apparent trends. For a rift, a noncollinear third station improves geometry, but interpreting the deformation still needs independent context and time coverage.

InSAR makes apparent ground motion easier to see over wide areas, yet its interferometric phase captures displacement projected into satellite line of sight plus multiple nondeformation contributions. If only one viewing geometry is available, a single displacement value cannot reconstruct the three-dimensional vector. Phase unwrapping errors and atmospheric delays may create dramatic patterns that resemble uplift or subsidence. Use GNSS and atmospheric diagnostics to check the pattern and describe coherence masks transparently.

In a coupled tectonic interpretation, ask whether elevated heat flow could arise from crustal thinning, focused groundwater flow or recent magmatism, and whether observed extension reflects a regional plate process or localized subsidence. Each explanation predicts different temperature profiles, fault behavior, geochemical signatures and spatial deformation. The strongest conclusion may be that available data support several models; quantify what next observation would have the greatest power to separate them.


## Unit investigation: reproducible synthetic dataset and experimental design

**Research aim.** The invented scenario is: A synthetic rift segment contains borehole temperature logs, GPS displacement vectors and an incomplete heat-flow transect. The team compares competing tectonic and hydrologic models before interpreting hazard or energy potential. Treat `datasets/unit-07.csv` as forty fictional rows deliberately designed to exercise quality control and model criticism. Read the file header before drawing any map. Plot the two relevant measured fields from unit 7; display the `quality_flag` column rather than deleting all flagged stations silently. The synthetic table contains no geographic coordinate reference system or real site identifiers and cannot be used to identify a place.

**Part A — raw measurements and dimensions.** Read each column as a quantity, not as a decorative label. For heat flow, geodesy and integrated earth processes, check whether the stated units are compatible with its equation and record which columns represent observed signals, instrument corrections, independent controls or model-derived quantities. Identify missing information such as date, site geology, true coordinate system, instrument orientation or calibration. If those omissions prevent a physical inversion, state the limitation and limit the task to transparent exploratory analysis. This is a stronger result than assigning fictitious precision.

**Part B — repeat and quality flags.** Count the rows marked `review`. Compare summary statistics, plotted gradients and model parameters with all forty records against the subset that passes the flag. Document every change; flags indicate inspection priority, not a universal mandate to delete. Check whether questionable values cluster along position or signal amplitude, because exclusions can introduce bias. If the noise appears correlated, do not assume a root-sum-square independent-error formula without a justification.

**Part C — model competition.** Describe two geophysical models that explain the synthetic observations in heat flow, geodesy and integrated earth processes; they must differ in physical property, geometry or forcing rather than just parameter precision. For each hypothesis make an observable prediction about station response, uncertainty pattern, external control or independent method. Select one new measurement that would best discriminate them, and explain its predicted signal under both hypotheses. A new dense sample from the same short profile may add less independent information than a crossing line or sample.

**Part D — numerical sensitivity.** Recompute one of the unit worked cases with the principal input increased by 10% and decreased by 10%. Check if the response is linear, inverse, logarithmic, quadratic or subject to another nonlinearity. Show a table with input, computed output, unit and physical assumption. Do not claim a sensitivity of the geological interpretation itself if only the toy forward equation was changed; the inverse solution may have a much broader family of possibilities.

**Part E — out-of-sample prediction and reporting.** Split the synthetic observations by physical position, retaining a contiguous group as a blind holdout. Fit a deliberately simple forward trend to remaining rows and predict the held-out quantity without retuning. Compare predictive error with a baseline that uses a constant mean. State why geographic separation can be a stronger test than random point withholding. Report all transformations, quality flags, fitted parameters, residual plots and failure modes in a compact methods appendix.

**Unit-specific evidence synthesis.** Conductive terrestrial heat flow is conventionally approximated by Fourier's law, but advective groundwater flow, transient climate histories and heterogeneity modify observed temperature profiles. Satellite and GNSS deformation offer geometric changes with differing sampling and error structures, not an automatic label for fault slip. InSAR phase depends on displacement toward the satellite as well as atmospheric path delay, orbital effects and surface decorrelation. Thermo-mechanical models relate heat, stress and kinematics, but fitted parameters may trade off strongly. Risk, geothermal resource capacity and fault activity require independent data, validated modelling and appropriate professional review. Map the chain of evidence from sensor to interpretation; highlight an uncertainty not reducible by extra decimal places. In your conclusion, indicate which measurement you would acquire next if the synthetic experiment were replaced with licensed real-world data. Keep any real data sourced from the references separate from these forty invented rows.

**Suggested report.** Submit a transparent CSV-reading script or spreadsheet calculation, one raw-data figure, a sensitivity plot, two candidate geological explanations, a withheld-test result and a one-page uncertainty ledger. Grade on conceptual correctness (25%), numerical units and reproducibility (25%), alternate hypotheses (20%), validation logic (20%) and scientific communication (10%). Never reward a map for appearing more certain than its underlying observations.

## End-of-unit reflection and problems

1. Identify which part of **heat flow, geodesy and integrated earth processes** would remain ambiguous even if measurement noise were reduced to zero. Explain how the survey geometry or parameter relationship creates that ambiguity.

2. Find a case where a large change in the observed signal would not imply a proportionally large change in target size. Write the forward relation, name fixed parameters, and state why inversion differs from prediction.

3. Propose a new survey that would risk rejecting the preferred geological interpretation. Its value should be based on discriminating predictions rather than its technological sophistication.

4. Draw a data lineage chart from raw instrument data through correction, inversion and geological claim. Underline any operation that assumes a material property not measured in the original dataset.

5. Explain why the synthetic data and interactive sliders are educational examples and cannot support emergency warnings, ground-investigation certification, resource appraisal or environmental enforcement.

## Additional reading and independent replication

Use `REFERENCES.md` to find a genuine program or open repository relevant to heat flow, geodesy and integrated earth processes. Before downloading any data, check the provider documentation, citation requirements, usage permissions and the time period represented. Record the instrument type, station metadata and acquisition geometry, then reproduce one simple physical calculation from scratch. The objective is not to match a published colored inversion image exactly; it is to understand the observable and give a defensible account of differences.


## Interactive physical-model explanations

Open this chapter in the HTML reader to change one controlled physical variable at a time. Each model is a simplified *forward* calculation, not an inversion or a real-world estimator.

### Conduction heat-flux magnitude

Input quantity: Geothermal gradient measured in K/km; demonstration range 1–60, initial setting 25. Output: W/m². Computed from `2.5*x/1000`.

**Unmodelled influences and interpretation boundary:** One-dimensional steady-state conduction; fixed thermal conductivity 2.5 W/(m K). Students should articulate a case where this formula yields a numerically precise but physically misleading answer and state an independently measurable quantity needed for a more complete model.

### Baseline extension strain rate

Input quantity: Annual separation measured in mm/yr; demonstration range 0–10, initial setting 2. Output: 1/yr. Computed from `(x/1000)/50000`.

**Unmodelled influences and interpretation boundary:** 50 km static baseline, one-dimensional rate only. Students should articulate a case where this formula yields a numerically precise but physically misleading answer and state an independently measurable quantity needed for a more complete model.
