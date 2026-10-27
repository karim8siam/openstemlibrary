# Unit 2: Crystal planes and reciprocal space

**Guiding question:** Why do diffraction measurements naturally describe waves and planes in reciprocal rather than direct space?

This unit connects direct and reciprocal geometry to an observable experiment. Every example is fictional and intentionally simplified. The sequence is designed so that the first two lessons provide definitions, the middle lessons test consequences, and the fifth lesson confronts ambiguity. Read plots as conditional calculations rather than laboratory observations.

## Investigation framework: Direct and reciprocal geometry





### Unit-wide reasoning objective




## Lesson 2.1 — Directions and Miller indices

### 1. Physical picture and mathematical meaning

A crystal direction is an oriented vector, typically written [uvw], while a plane is represented by Miller indices (hkl). A family of symmetry-equivalent planes uses braces. In a cubic cell, [hkl] happens to be perpendicular to (hkl), but that shortcut does not generally hold for noncubic lattices. Integer indexing encodes orientation, not physical distances by itself.


### 2. What to measure and what it means

Sketch a plane through intercepts a, b/2 and infinity, take reciprocals of the intercept multiples and reduce them to a triplet. Cross-check its normal using the reciprocal basis. Rotate the sketch into a monoclinic setting to expose the limits of the cubic shortcut.


Consider the targeted decision **whether multiple nonoverlapping reflections can share one consistent cell metric**. Specify one null hypothesis that competes with the preferred explanation and design a control that could falsify it. Make a small table of predicted features for both interpretations before inspecting any synthetic data. Such predeclared contrasts reduce the temptation to keep only peaks that favor the desired material narrative. Calibration, specimen preparation and the physics of scattering should be assessed before microstructure claims are written.

### 3. Interpretation, alternative explanations and boundaries

Correctly assigned indices allow comparison of measured peaks, slip systems and texture, but a single reflection typically does not establish the entire orientation matrix.


One competing explanation to test here is **mistaken plane indices**. This is not a guaranteed cause, but it deserves a clear discrimination experiment. Decide whether a changed scan range, an independent standard, a different specimen orientation or a second probe would expose that alternative. Also ask whether the proposed test changes one parameter at a time. An experiment that simultaneously changes wavelength, mounting and background correction may produce a new curve without clarifying why it changed.

### 4. Fully specified synthetic calculation

The linked model is **Cubic 111 spacing**. Its one-variable input is **cubic a** (nm), the selected demonstration value is **0.38**, and the computed value is **0.219393 nm**. The exact model expression is `a/Math.sqrt(3)` using the variable shown; this is intentionally a classroom-level forward relationship. Model assumptions: Only for cubic (111); identical 2π conventions not required.


| Input (nm) | Predicted nm | Interpretation |
|---:|---:|---|
| 0.38 | 0.219393 | Low-side comparison under fixed assumptions |
| 0.45 | 0.259808 | Reference setting for sensitivity |
| 0.62 | 0.357957 | High-side comparison under fixed assumptions |


### 5. Data collection and reproducibility protocol

Design a comparison that measures **lattice metric and plane-normal orientation** while holding specimen state and geometry as steady as possible. Record **h, k, l; angular indexing; cell parameters**. Repeat an independent reference and state what result would support **whether multiple nonoverlapping reflections can share one consistent cell metric**. Record the decision rule before looking at a fitted pattern.

### 6. Diagnostic failure mode

Do not confuse a crystallographic plane with an arbitrarily chosen external polished surface.

In the current unit, a particularly relevant practical trap is **a reciprocal convention mismatch or falsely cubic interpretation**. An analyst who ignores it can obtain a mathematically self-consistent answer from the wrong inputs. Diagnose the trap by returning to an invariant: a reference specimen, multiple indexed reflections, a repeated geometry, a known scattering convention or an independent probe. If the disagreement persists, report it as an unresolved limitation. Do not change a correction parameter solely to force a desirable phase or property estimate.


### 7. Knowledge-check and discussion questions

- **Explain:** What is the physical distinction between the quantity named in **Directions and Miller indices** and the observable used to estimate it? Give one explicit assumption.
- **Calculate:** Reproduce case MSE-C06 and evaluate how the output changes when the slider parameter moves from 0.38 to 0.62 nm.
- **Challenge:** Could **mistaken plane indices** explain the observed feature? State a discriminating control rather than merely saying that more data are required.



## Lesson 2.2 — Metric tensors and cell volume

### 1. Physical picture and mathematical meaning

The metric tensor records dot products of direct lattice vectors and therefore contains all cell lengths and angles. With non-orthogonal axes, reciprocal spacing follows from the inverse metric tensor rather than the cubic square-root formula. Cell volume equals the absolute scalar triple product of the direct vectors, which becomes abc only when axes are orthogonal. The determinant tests whether the three basis vectors span a nonzero volume.


### 2. What to measure and what it means

Calculate a simulated monoclinic cell volume from a, b, c and the non-right beta angle. Compare it with the product abc and quantify the difference. Independently compute plane spacings using a reciprocal-metric expression and verify the expected cubic limit when all angles become right angles.



### 3. Interpretation, alternative explanations and boundaries

Metric formalism prevents a subtle systematic bias when analyzing strained, low-symmetry or temperature-dependent structures. A wrong metric may still produce smooth curves but misidentify reflections.


One competing explanation to test here is **wrong 2π reciprocal convention**. This is not a guaranteed cause, but it deserves a clear discrimination experiment. Decide whether a changed scan range, an independent standard, a different specimen orientation or a second probe would expose that alternative. Also ask whether the proposed test changes one parameter at a time. An experiment that simultaneously changes wavelength, mounting and background correction may produce a new curve without clarifying why it changed.

### 4. Fully specified synthetic calculation

The linked model is **Reciprocal length |G111|**. Its one-variable input is **cubic a** (nm), the selected demonstration value is **0.46**, and the computed value is **23.6583 nm⁻¹**. The exact model expression is `2*Math.PI*Math.sqrt(3)/a` using the variable shown; this is intentionally a classroom-level forward relationship. Model assumptions: Physics reciprocal convention includes factor 2π.


| Input (nm) | Predicted nm⁻¹ | Interpretation |
|---:|---:|---|
| 0.38 | 28.6389 | Low-side comparison under fixed assumptions |
| 0.45 | 24.184 | Reference setting for sensitivity |
| 0.62 | 17.5529 | High-side comparison under fixed assumptions |


### 5. Data collection and reproducibility protocol



### 6. Diagnostic failure mode

Never substitute an orthogonal geometry relation merely because the graphical cell looks almost rectangular.




### 7. Knowledge-check and discussion questions

- **Explain:** What is the physical distinction between the quantity named in **Metric tensors and cell volume** and the observable used to estimate it? Give one explicit assumption.
- **Calculate:** Reproduce case MSE-C07 and evaluate how the output changes when the slider parameter moves from 0.38 to 0.62 nm.
- **Challenge:** Could **wrong 2π reciprocal convention** explain the observed feature? State a discriminating control rather than merely saying that more data are required.



## Lesson 2.3 — Reciprocal lattice construction

### 1. Physical picture and mathematical meaning

A reciprocal basis is defined through dual dot products with the direct basis. Under the convention a-star dot a equals one, reciprocal lengths have units of inverse distance; under a physics convention incorporating 2π, reciprocal vectors are scaled accordingly. This convention choice changes numerical labels but not measurable diffraction angles. Reciprocal points represent families of equally spaced crystal planes.


### 2. What to measure and what it means

Construct a two-dimensional direct lattice on grid paper and draw a corresponding reciprocal grid with normals to the direct plane families. Check the product of d-spacing and reciprocal normal magnitude for the specified convention. Mark explicitly whether the 2π factor is present.



### 3. Interpretation, alternative explanations and boundaries

A reciprocal-space map is an organized geometry of scattering conditions, not a literal microscopic image of atoms. Measured intensities at reciprocal points encode the Fourier transform of the scattering density.


One competing explanation to test here is **non-orthogonal lattice angles**. This is not a guaranteed cause, but it deserves a clear discrimination experiment. Decide whether a changed scan range, an independent standard, a different specimen orientation or a second probe would expose that alternative. Also ask whether the proposed test changes one parameter at a time. An experiment that simultaneously changes wavelength, mounting and background correction may produce a new curve without clarifying why it changed.

### 4. Fully specified synthetic calculation

The linked model is **Cubic 111 spacing**. Its one-variable input is **cubic a** (nm), the selected demonstration value is **0.53**, and the computed value is **0.305996 nm**. The exact model expression is `a/Math.sqrt(3)` using the variable shown; this is intentionally a classroom-level forward relationship. Model assumptions: Only for cubic (111); identical 2π conventions not required.


| Input (nm) | Predicted nm | Interpretation |
|---:|---:|---|
| 0.38 | 0.219393 | Low-side comparison under fixed assumptions |
| 0.45 | 0.259808 | Reference setting for sensitivity |
| 0.62 | 0.357957 | High-side comparison under fixed assumptions |


### 5. Data collection and reproducibility protocol



### 6. Diagnostic failure mode

Mixing reciprocal conventions is a frequent source of hidden factors of 2π in equations and software.




### 7. Knowledge-check and discussion questions

- **Explain:** What is the physical distinction between the quantity named in **Reciprocal lattice construction** and the observable used to estimate it? Give one explicit assumption.
- **Calculate:** Reproduce case MSE-C08 and evaluate how the output changes when the slider parameter moves from 0.38 to 0.62 nm.
- **Challenge:** Could **non-orthogonal lattice angles** explain the observed feature? State a discriminating control rather than merely saying that more data are required.



## Lesson 2.4 — d-spacing and crystal symmetry

### 1. Physical picture and mathematical meaning

For cubic lattices the interplanar spacing is a divided by the square root of h²+k²+l². In tetragonal cells the reciprocal-square spacing separates in-plane indices from the c-axis index. Reflection multiplicity counts symmetry-equivalent planes and can affect powder intensity. A strain field may perturb d-spacing differently along different directions and broaden or shift peaks.


### 2. What to measure and what it means

Index a synthetic cubic powder dataset using ratios of sin²(theta). Reconstruct a lattice parameter from each indexed peak and compare consistency. Then impose a slight tetragonal distortion in the simulated list; observe which formerly coincident peaks separate and whether the splitting exceeds instrumental resolution.



### 3. Interpretation, alternative explanations and boundaries

Multiple indexed reflections strengthen a phase assignment because they test a common unit cell, whereas matching one peak is weak evidence.


One competing explanation to test here is **unresolved peak overlap**. This is not a guaranteed cause, but it deserves a clear discrimination experiment. Decide whether a changed scan range, an independent standard, a different specimen orientation or a second probe would expose that alternative. Also ask whether the proposed test changes one parameter at a time. An experiment that simultaneously changes wavelength, mounting and background correction may produce a new curve without clarifying why it changed.

### 4. Fully specified synthetic calculation

The linked model is **Reciprocal length |G111|**. Its one-variable input is **cubic a** (nm), the selected demonstration value is **0.61**, and the computed value is **17.8406 nm⁻¹**. The exact model expression is `2*Math.PI*Math.sqrt(3)/a` using the variable shown; this is intentionally a classroom-level forward relationship. Model assumptions: Physics reciprocal convention includes factor 2π.


| Input (nm) | Predicted nm⁻¹ | Interpretation |
|---:|---:|---|
| 0.38 | 28.6389 | Low-side comparison under fixed assumptions |
| 0.45 | 24.184 | Reference setting for sensitivity |
| 0.62 | 17.5529 | High-side comparison under fixed assumptions |


### 5. Data collection and reproducibility protocol



### 6. Diagnostic failure mode

Peak positions alone do not distinguish all polymorphs or determine site occupancy and elemental concentrations.




### 7. Knowledge-check and discussion questions

- **Explain:** What is the physical distinction between the quantity named in **d-spacing and crystal symmetry** and the observable used to estimate it? Give one explicit assumption.
- **Calculate:** Reproduce case MSE-C09 and evaluate how the output changes when the slider parameter moves from 0.38 to 0.62 nm.
- **Challenge:** Could **unresolved peak overlap** explain the observed feature? State a discriminating control rather than merely saying that more data are required.



## Lesson 2.5 — Ewald sphere and diffraction geometry

### 1. Physical picture and mathematical meaning

Elastic scattering conserves the magnitude of the wave vector, so incident and outgoing wave vectors have equal length. Their difference is the scattering vector, which meets a reciprocal-lattice point at a diffraction condition. The Ewald construction visualizes why rotating a single crystal brings different reciprocal points into reflection. Detector position, wavelength and sample orientation collectively determine what is accessible.


### 2. What to measure and what it means

Draw incident and diffracted beam arrows with the same wavelength-dependent magnitude and calculate the scattering-vector length versus angle. Move the crystal orientation in the sketch and identify which reflections become reachable. Compare fixed-wavelength scans with variable-energy measurements.



### 3. Interpretation, alternative explanations and boundaries

A geometrically forbidden measurement angle need not imply that a particular crystal plane is absent. Data collection strategy must cover orientation and detector limitations before invoking crystallographic extinction.


One competing explanation to test here is **orientation-matrix mismatch**. This is not a guaranteed cause, but it deserves a clear discrimination experiment. Decide whether a changed scan range, an independent standard, a different specimen orientation or a second probe would expose that alternative. Also ask whether the proposed test changes one parameter at a time. An experiment that simultaneously changes wavelength, mounting and background correction may produce a new curve without clarifying why it changed.

### 4. Fully specified synthetic calculation

The linked model is **Cubic 111 spacing**. Its one-variable input is **cubic a** (nm), the selected demonstration value is **0.68**, and the computed value is **0.392598 nm**. The exact model expression is `a/Math.sqrt(3)` using the variable shown; this is intentionally a classroom-level forward relationship. Model assumptions: Only for cubic (111); identical 2π conventions not required.


| Input (nm) | Predicted nm | Interpretation |
|---:|---:|---|
| 0.38 | 0.219393 | Low-side comparison under fixed assumptions |
| 0.45 | 0.259808 | Reference setting for sensitivity |
| 0.62 | 0.357957 | High-side comparison under fixed assumptions |


### 5. Data collection and reproducibility protocol



### 6. Diagnostic failure mode

The Ewald sphere must be drawn using one consistent reciprocal-vector magnitude convention throughout.




### 7. Knowledge-check and discussion questions

- **Explain:** What is the physical distinction between the quantity named in **Ewald sphere and diffraction geometry** and the observable used to estimate it? Give one explicit assumption.
- **Calculate:** Reproduce case MSE-C10 and evaluate how the output changes when the slider parameter moves from 0.38 to 0.62 nm.
- **Challenge:** Could **orientation-matrix mismatch** explain the observed feature? State a discriminating control rather than merely saying that more data are required.



## Explore two independent interactive model families

<!-- MODEL_2 -->

<!-- MODEL_3 -->

## Integrated investigation: Monoclinic metric from three plane families

### Evidence brief

A low-symmetry synthetic oxide is indexed by a student who uses the cubic d-spacing formula. Their inferred cell parameter varies between reflections, and they conclude that the powder is a multiphase mixture. The interpretation neglects the true metric tensor.



### Proposed analysis

Write the direct metric for a monoclinic cell and compute reciprocal magnitudes numerically. Fit cell lengths and beta only to peaks with consistent assignments. Compare predicted 2θ values for unused reflections against the recorded peaks, reserving them as out-of-fit validation.



### Evaluation of the competing explanations

A coherent noncubic metric that explains multiple lines may be more parsimonious than inventing several phases. Uncertainty and peak overlap still limit the claim, so use a residual plot rather than a verbal assertion of fit.



### Limitations and ethical interpretation

This exercise cannot uniquely determine the atom positions or space group. Wrong centering conditions or a second phase can still produce a deceptively good metric fit.



### Assessment rubric





## Unit research commentary — evidence across scales

Noncubic indexing benefits from an explicit coordinate-system audit. Suppose three basis vectors form a monoclinic cell, with only the angle between a and c different from ninety degrees. A student measuring a synthetic high-angle peak inserts its indices into the cubic formula, then interprets the disagreeing parameter estimates as evidence that the specimen contains extra crystalline phases. The first corrective step is to calculate direct-vector dot products and form the metric tensor. The inverse metric relates plane indices to spacing. A set of genuinely consistent monoclinic reflections should obey one such metric across a range of indices.

A second audit checks reciprocal normalization. Some crystallographic software reports reciprocal lengths in inverse ångströms without 2π, while solid-state physics expressions for momentum transfer include 2π. If an analyst silently combines those conventions, a scale error affects every fitted reciprocal vector. To expose it, compute one orthogonal simple-cubic example where the expected spacing is obvious, then reproduce the same answer using the general metric method. State the vector dimensions at every step. This unit test is much cheaper than attempting a sophisticated refinement on inconsistent coordinates.

Finally design an indexing validation that does not reuse all available peaks as adjustable fitting targets. Reserve several well-resolved reflections for prediction and check both positions and systematic absence plausibility. A well-fitting cell metric constrains geometry; it does not independently establish occupancy or eliminate minor phases. If the test reflections disagree, consider wrong indexing, accidental overlap, instrument offset and symmetry lowering before raising model complexity. In the final answer explain why reflections with different combinations of h,k,l constrain cell axes differently, and why higher-angle peaks can increase sensitivity to small metric changes but also complicate reliable peak detection. A diffraction report should separate the chosen reference frame, lattice setting, model residual and genuinely independent test reflections.

### End-of-unit examiner challenge: Crystal planes and reciprocal space

Write an evidence-based defense of **whether multiple nonoverlapping reflections can share one consistent cell metric**. Begin by defining how **lattice metric and plane-normal orientation** would be measured and listing the necessary independent controls for **h, k, l; angular indexing; cell parameters**. Then name a physically distinct mechanism that could imitate the preferred explanation: **a reciprocal convention mismatch or falsely cubic interpretation**. The response must show why that mechanism is plausible, rather than merely listing it as a caveat. Select one follow-up measurement that makes different predictions for the rival models; state what a negative result would mean. Finally prepare an annotated calculation from the two teaching formulas associated with this unit and explain why exact numerical agreement with a forward equation does not validate the specimen interpretation. Include an uncertainty estimate and say whether the proposed material conclusion is supported, conditional or unresolved. This is a reasoning task using synthetic evidence, not an authorization to operate an instrument.
