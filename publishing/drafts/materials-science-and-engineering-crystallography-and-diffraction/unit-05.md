# Unit 5: Single crystals, orientation and texture

**Guiding question:** What extra information becomes available when specimen orientation is controlled, and how can orientation bias mislead us?

This unit connects orientation and crystallographic mapping to an observable experiment. Every example is fictional and intentionally simplified. The sequence is designed so that the first two lessons provide definitions, the middle lessons test consequences, and the fifth lesson confronts ambiguity. Read plots as conditional calculations rather than laboratory observations.

## Investigation framework: Orientation and crystallographic mapping





### Unit-wide reasoning objective




## Lesson 5.1 — Single-crystal diffraction strategy

### 1. Physical picture and mathematical meaning

Single-crystal data record discrete reflection intensities as a crystal is rotated through different orientations. Redundancy, completeness, detector coverage, absorption and radiation damage control the reliability of derived electron density. A strong spot array can still reflect twinning or multiple domains. Unit-cell indexing precedes structural refinement and must be checked for alternative choices.


### 2. What to measure and what it means

Propose a rotation sequence that covers multiple equivalent reflections and includes a reference orientation after the scan. Monitor reflection intensity drift and spot shape over time. Document wavelength, detector geometry, exposure and crystal dimensions.


Consider the targeted decision **whether a claimed epitaxial relation survives independent azimuthal scans**. Specify one null hypothesis that competes with the preferred explanation and design a control that could falsify it. Make a small table of predicted features for both interpretations before inspecting any synthetic data. Such predeclared contrasts reduce the temptation to keep only peaks that favor the desired material narrative. Calibration, specimen preparation and the physics of scattering should be assessed before microstructure claims are written.

### 3. Interpretation, alternative explanations and boundaries

Three-dimensional reflection intensities can determine more structural detail than a one-dimensional powder trace, but model completeness and data quality still constrain uniqueness.


One competing explanation to test here is **twinned domains**. This is not a guaranteed cause, but it deserves a clear discrimination experiment. Decide whether a changed scan range, an independent standard, a different specimen orientation or a second probe would expose that alternative. Also ask whether the proposed test changes one parameter at a time. An experiment that simultaneously changes wavelength, mounting and background correction may produce a new curve without clarifying why it changed.

### 4. Fully specified synthetic calculation

The linked model is **Diffraction-camera radial distance**. Its one-variable input is **scattering angle 2θ** (degrees), the selected demonstration value is **5.5**, and the computed value is **9.6289 mm**. The exact model expression is `100*Math.tan(twoTheta*Math.PI/180)` using the variable shown; this is intentionally a classroom-level forward relationship. Model assumptions: Flat detector 100 mm from sample, ideal geometry.


| Input (degrees) | Predicted mm | Interpretation |
|---:|---:|---|
| 4.5 | 7.87017 | Low-side comparison under fixed assumptions |
| 8 | 14.0541 | Reference setting for sensitivity |
| 18 | 32.492 | High-side comparison under fixed assumptions |


### 5. Data collection and reproducibility protocol

Design a comparison that measures **crystal orientation distribution** while holding specimen state and geometry as steady as possible. Record **specimen tilt; rocking angle; detector coordinate frame**. Repeat an independent reference and state what result would support **whether a claimed epitaxial relation survives independent azimuthal scans**. Record the decision rule before looking at a fitted pattern.

### 6. Diagnostic failure mode

A high-quality refinement agreement factor does not by itself exclude a wrong absolute structure or overlooked twin law.

In the current unit, a particularly relevant practical trap is **treating a single preferred out-of-plane direction as full epitaxy**. An analyst who ignores it can obtain a mathematically self-consistent answer from the wrong inputs. Diagnose the trap by returning to an invariant: a reference specimen, multiple indexed reflections, a repeated geometry, a known scattering convention or an independent probe. If the disagreement persists, report it as an unresolved limitation. Do not change a correction parameter solely to force a desirable phase or property estimate.


### 7. Knowledge-check and discussion questions

- **Explain:** What is the physical distinction between the quantity named in **Single-crystal diffraction strategy** and the observable used to estimate it? Give one explicit assumption.
- **Calculate:** Reproduce case MSE-C21 and evaluate how the output changes when the slider parameter moves from 4.5 to 18 degrees.
- **Challenge:** Could **twinned domains** explain the observed feature? State a discriminating control rather than merely saying that more data are required.



## Lesson 5.2 — Orientation matrices and reciprocal mapping

### 1. Physical picture and mathematical meaning

An orientation matrix transforms reciprocal lattice indices into laboratory-frame scattering vectors; it combines the unit-cell metric with crystal orientation. Indexing observed spots estimates this transformation and reveals possible mosaicity or multiple grains. Reciprocal-space maps can separate strain from angular tilt only if geometry and reference frame are handled consistently.


### 2. What to measure and what it means

Generate three noncoplanar reference reflections from a known cubic test cell and imagine solving for the orientation. Apply a small rigid-body rotation and distinguish it from changing the cell edge. Use a fixed detector reference and record any changed instrument axes.



### 3. Interpretation, alternative explanations and boundaries

An orientation map is a coordinate transformation plus inferred crystal metric; confusing laboratory and crystal coordinates leads to false mosaic spread or strain gradients.


One competing explanation to test here is **rocking-curve instrument width**. This is not a guaranteed cause, but it deserves a clear discrimination experiment. Decide whether a changed scan range, an independent standard, a different specimen orientation or a second probe would expose that alternative. Also ask whether the proposed test changes one parameter at a time. An experiment that simultaneously changes wavelength, mounting and background correction may produce a new curve without clarifying why it changed.

### 4. Fully specified synthetic calculation

The linked model is **Rocking-curve intensity envelope**. Its one-variable input is **rocking offset ω** (degrees), the selected demonstration value is **-1.1**, and the computed value is **0.432847 relative intensity**. The exact model expression is `Math.exp(-Math.pow(omega/0.85,2)/2)` using the variable shown; this is intentionally a classroom-level forward relationship. Model assumptions: Toy Gaussian distribution of angular offsets; not a quantitative texture inversion.


| Input (degrees) | Predicted relative intensity | Interpretation |
|---:|---:|---|
| -1.5 | 0.210748 | Low-side comparison under fixed assumptions |
| 0 | 1 | Reference setting for sensitivity |
| 1.5 | 0.210748 | High-side comparison under fixed assumptions |


### 5. Data collection and reproducibility protocol



### 6. Diagnostic failure mode

Do not interpret a diffuse streak as unique evidence of a single defect type without considering instrument resolution and dynamical scattering.




### 7. Knowledge-check and discussion questions

- **Explain:** What is the physical distinction between the quantity named in **Orientation matrices and reciprocal mapping** and the observable used to estimate it? Give one explicit assumption.
- **Calculate:** Reproduce case MSE-C22 and evaluate how the output changes when the slider parameter moves from -1.5 to 1.5 degrees.
- **Challenge:** Could **rocking-curve instrument width** explain the observed feature? State a discriminating control rather than merely saying that more data are required.



## Lesson 5.3 — Texture and pole figures

### 1. Physical picture and mathematical meaning

Preferred orientation in a polycrystal causes nonrandom distributions of crystal directions relative to the specimen frame. Pole figures sample directional density, while an orientation distribution function describes the full statistical orientation distribution. Rolling, extrusion, deposition and additive manufacturing often create strong texture. Texture influences mechanical anisotropy and also biases powder diffraction intensity.


### 2. What to measure and what it means

Compare relative pole densities at several tilt and rotation angles for a random test population and an aligned population. Identify whether sample symmetry permits averaging. Keep track of how many orientations were actually sampled before extrapolating a full distribution.



### 3. Interpretation, alternative explanations and boundaries

Texture may reveal processing history, but predicting a mechanical property requires an appropriate constitutive or averaging model, not merely a bright pole-figure maximum.


One competing explanation to test here is **surface-sensitive sampling**. This is not a guaranteed cause, but it deserves a clear discrimination experiment. Decide whether a changed scan range, an independent standard, a different specimen orientation or a second probe would expose that alternative. Also ask whether the proposed test changes one parameter at a time. An experiment that simultaneously changes wavelength, mounting and background correction may produce a new curve without clarifying why it changed.

### 4. Fully specified synthetic calculation

The linked model is **Diffraction-camera radial distance**. Its one-variable input is **scattering angle 2θ** (degrees), the selected demonstration value is **13.5**, and the computed value is **24.0079 mm**. The exact model expression is `100*Math.tan(twoTheta*Math.PI/180)` using the variable shown; this is intentionally a classroom-level forward relationship. Model assumptions: Flat detector 100 mm from sample, ideal geometry.


| Input (degrees) | Predicted mm | Interpretation |
|---:|---:|---|
| 4.5 | 7.87017 | Low-side comparison under fixed assumptions |
| 8 | 14.0541 | Reference setting for sensitivity |
| 18 | 32.492 | High-side comparison under fixed assumptions |


### 5. Data collection and reproducibility protocol



### 6. Diagnostic failure mode

A surface measurement may not represent through-thickness texture in a heavily processed plate.




### 7. Knowledge-check and discussion questions

- **Explain:** What is the physical distinction between the quantity named in **Texture and pole figures** and the observable used to estimate it? Give one explicit assumption.
- **Calculate:** Reproduce case MSE-C23 and evaluate how the output changes when the slider parameter moves from 4.5 to 18 degrees.
- **Challenge:** Could **surface-sensitive sampling** explain the observed feature? State a discriminating control rather than merely saying that more data are required.



## Lesson 5.4 — Electron backscatter diffraction

### 1. Physical picture and mathematical meaning

EBSD in a scanning electron microscope indexes Kikuchi patterns to estimate near-surface crystallographic orientation. Surface preparation, beam settings, detector geometry and phase library quality affect pattern indexing. Grain boundary maps use angular misorientation thresholds that must be disclosed. EBSD is largely a near-surface method and is sensitive to deformation introduced by polishing.


### 2. What to measure and what it means

Plan an EBSD grid spacing fine enough to resolve the smallest grain of interest. Quantify indexed fraction, confidence metrics, boundary thresholds and likely unindexed regions. Compare one as-polished and one final-cleaned area before interpreting a local strain proxy.



### 3. Interpretation, alternative explanations and boundaries

A colorful inverse-pole-figure map is a reconstructed statistical dataset, not direct photographic evidence of atomic columns.


One competing explanation to test here is **detector tilt**. This is not a guaranteed cause, but it deserves a clear discrimination experiment. Decide whether a changed scan range, an independent standard, a different specimen orientation or a second probe would expose that alternative. Also ask whether the proposed test changes one parameter at a time. An experiment that simultaneously changes wavelength, mounting and background correction may produce a new curve without clarifying why it changed.

### 4. Fully specified synthetic calculation

The linked model is **Rocking-curve intensity envelope**. Its one-variable input is **rocking offset ω** (degrees), the selected demonstration value is **0.7**, and the computed value is **0.712411 relative intensity**. The exact model expression is `Math.exp(-Math.pow(omega/0.85,2)/2)` using the variable shown; this is intentionally a classroom-level forward relationship. Model assumptions: Toy Gaussian distribution of angular offsets; not a quantitative texture inversion.


| Input (degrees) | Predicted relative intensity | Interpretation |
|---:|---:|---|
| -1.5 | 0.210748 | Low-side comparison under fixed assumptions |
| 0 | 1 | Reference setting for sensitivity |
| 1.5 | 0.210748 | High-side comparison under fixed assumptions |


### 5. Data collection and reproducibility protocol



### 6. Diagnostic failure mode

Do not interpret every nonindexed pixel as amorphous material; roughness, shadowing and overlapping phases may explain failure.




### 7. Knowledge-check and discussion questions

- **Explain:** What is the physical distinction between the quantity named in **Electron backscatter diffraction** and the observable used to estimate it? Give one explicit assumption.
- **Calculate:** Reproduce case MSE-C24 and evaluate how the output changes when the slider parameter moves from -1.5 to 1.5 degrees.
- **Challenge:** Could **detector tilt** explain the observed feature? State a discriminating control rather than merely saying that more data are required.



## Lesson 5.5 — Thin films, epitaxy and grazing incidence

### 1. Physical picture and mathematical meaning

Thin films may have preferred out-of-plane orientation, residual stress, nanoscale domain size and substrate peaks much stronger than film peaks. Grazing-incidence geometries alter penetration depth and separate in-plane from out-of-plane information. Epitaxial alignment is more restrictive than generic texture and requires appropriate angular scans. Instrument footprint and refraction effects may matter at very small incidence angles.


### 2. What to measure and what it means

Plan an out-of-plane scan, a rocking curve and an in-plane measurement for a hypothetical film. Compare a bare-substrate control with coated sample data, keeping beam footprint consistent. Discuss which independent observation would support epitaxy rather than merely fiber texture.



### 3. Interpretation, alternative explanations and boundaries

A narrow rocking curve may indicate small orientation spread, but strain gradients, instrumental broadening and mosaic domains complicate that interpretation.


One competing explanation to test here is **thin-film interference**. This is not a guaranteed cause, but it deserves a clear discrimination experiment. Decide whether a changed scan range, an independent standard, a different specimen orientation or a second probe would expose that alternative. Also ask whether the proposed test changes one parameter at a time. An experiment that simultaneously changes wavelength, mounting and background correction may produce a new curve without clarifying why it changed.

### 4. Fully specified synthetic calculation

The linked model is **Diffraction-camera radial distance**. Its one-variable input is **scattering angle 2θ** (degrees), the selected demonstration value is **22**, and the computed value is **40.4026 mm**. The exact model expression is `100*Math.tan(twoTheta*Math.PI/180)` using the variable shown; this is intentionally a classroom-level forward relationship. Model assumptions: Flat detector 100 mm from sample, ideal geometry.


| Input (degrees) | Predicted mm | Interpretation |
|---:|---:|---|
| 4.5 | 7.87017 | Low-side comparison under fixed assumptions |
| 8 | 14.0541 | Reference setting for sensitivity |
| 18 | 32.492 | High-side comparison under fixed assumptions |


### 5. Data collection and reproducibility protocol



### 6. Diagnostic failure mode

Avoid extracting film thickness from peak fringes without checking roughness, coherence and substrate interference assumptions.




### 7. Knowledge-check and discussion questions

- **Explain:** What is the physical distinction between the quantity named in **Thin films, epitaxy and grazing incidence** and the observable used to estimate it? Give one explicit assumption.
- **Calculate:** Reproduce case MSE-C25 and evaluate how the output changes when the slider parameter moves from 4.5 to 18 degrees.
- **Challenge:** Could **thin-film interference** explain the observed feature? State a discriminating control rather than merely saying that more data are required.



## Explore two independent interactive model families

<!-- MODEL_8 -->

<!-- MODEL_9 -->

## Integrated investigation: Thin-film diffraction with a strong substrate

### Evidence brief

An epitaxial film may produce only a small shoulder beside an intense single-crystal substrate reflection. In one scan the film seems absent, although a reciprocal-space map reveals an offset feature.



### Proposed analysis

Compare a symmetric scan, asymmetric map and rocking scan. Outline how a bare substrate reference and the same beam footprint affect interpretability. Quantify simulated film-to-substrate peak ratio and track whether sample tilt or detector masking removes the shoulder.



### Evaluation of the competing explanations

One-dimensional absence is not evidence of missing film. A measured epitaxial relationship needs both out-of-plane and in-plane orientation information with uncertainties.



### Limitations and ethical interpretation

The teaching model neglects full wave interference, dynamical scattering, absorption and possible film relaxation gradients.



### Assessment rubric





## Unit research commentary — evidence across scales

Orientation-controlled diffraction should be understood as a three-dimensional sampling problem. In a single crystal, a reflection may be absent from the detector because that orientation does not satisfy the scattering condition. Rotating the crystal changes the set of reciprocal points intersecting the measurement geometry without changing the intrinsic lattice. A powder scan approximates rotational averaging, but strong texture violates the random-orientation assumption. Thus an orientation-dependent intensity change is not automatically a chemical phase change, and an absent spot can be geometrically inaccessible rather than symmetry-forbidden.

Consider a deposited film on a crystalline substrate. In a symmetric out-of-plane scan, one family of film planes may appear beautifully aligned with the substrate, yet the film could remain rotationally disordered around the surface normal. A full epitaxial claim needs an appropriate in-plane relationship, established by azimuthal or reciprocal-space measurements. Rocking curves characterize angular spread with instrumental contributions and possible specimen curvature. A narrow curve might be consistent with low mosaicity, but its meaning depends on geometry and controls. In a polycrystalline sheet, EBSD can provide local near-surface orientations but has different sampling limitations from bulk diffraction.

An applied case asks whether a rolled alloy is isotropic enough for a planned forming process. Draw a minimal orientation measurement plan over the sheet thickness and along orthogonal rolling directions, then identify likely sampling biases. If an orientation map and bulk peak-intensity ratios disagree, investigate preparation, depth sensitivity, grain size and geometry before selecting a preferred result. Finally separate two questions: what is the orientation distribution, and how does that distribution affect the engineering response? Answering the second requires mechanics or transport information that is not provided by texture measurement alone. The unit’s key deliverable is a geometrically correct, reproducible orientation argument with stated depth and volume sensitivity.

### End-of-unit examiner challenge: Single crystals, orientation and texture

Write an evidence-based defense of **whether a claimed epitaxial relation survives independent azimuthal scans**. Begin by defining how **crystal orientation distribution** would be measured and listing the necessary independent controls for **specimen tilt; rocking angle; detector coordinate frame**. Then name a physically distinct mechanism that could imitate the preferred explanation: **treating a single preferred out-of-plane direction as full epitaxy**. The response must show why that mechanism is plausible, rather than merely listing it as a caveat. Select one follow-up measurement that makes different predictions for the rival models; state what a negative result would mean. Finally prepare an annotated calculation from the two teaching formulas associated with this unit and explain why exact numerical agreement with a forward equation does not validate the specimen interpretation. Include an uncertainty estimate and say whether the proposed material conclusion is supported, conditional or unresolved. This is a reasoning task using synthetic evidence, not an authorization to operate an instrument.
