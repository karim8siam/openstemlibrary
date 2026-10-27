# Unit 6: Line profiles, defects and deformation

**Guiding question:** How can broadening and peak shifts inform microstructure without overinterpreting a single fitted width?

This unit connects line shape and defect analysis to an observable experiment. Every example is fictional and intentionally simplified. The sequence is designed so that the first two lessons provide definitions, the middle lessons test consequences, and the fifth lesson confronts ambiguity. Read plots as conditional calculations rather than laboratory observations.

## Investigation framework: Line shape and defect analysis





### Unit-wide reasoning objective




## Lesson 6.1 — Instrument broadening versus sample broadening

### 1. Physical picture and mathematical meaning

Every diffractometer records peaks broadened by spectral width, optical resolution and detector response as well as the sample. A measured FWHM is not automatically a crystallite-size measurement. Gaussian and Lorentzian components combine differently, and a pseudo-Voigt fit is only an approximation. Instrumental profiles should be established with an appropriate reference at similar angles.


### 2. What to measure and what it means

Collect a synthetic reference with negligible specimen contribution and compare its widths to those of a nanocrystalline sample. Apply Gaussian quadrature only to widths modeled as Gaussian, and show that an incompatible profile assumption changes the corrected breadth.


Consider the targeted decision **whether size and strain explanations are separable from angular trends**. Specify one null hypothesis that competes with the preferred explanation and design a control that could falsify it. Make a small table of predicted features for both interpretations before inspecting any synthetic data. Such predeclared contrasts reduce the temptation to keep only peaks that favor the desired material narrative. Calibration, specimen preparation and the physics of scattering should be assessed before microstructure claims are written.

### 3. Interpretation, alternative explanations and boundaries

The most robust report records raw widths, instrument-correction method, profile function and uncertainty. Small sample broadening near the instrument limit is especially uncertain.


One competing explanation to test here is **instrument profile asymmetry**. This is not a guaranteed cause, but it deserves a clear discrimination experiment. Decide whether a changed scan range, an independent standard, a different specimen orientation or a second probe would expose that alternative. Also ask whether the proposed test changes one parameter at a time. An experiment that simultaneously changes wavelength, mounting and background correction may produce a new curve without clarifying why it changed.

### 4. Fully specified synthetic calculation

The linked model is **Scherrer coherent domain size**. Its one-variable input is **sample FWHM beta** (degrees 2θ), the selected demonstration value is **0.3**, and the computed value is **28.1805 nm**. The exact model expression is `0.9*0.15406/((beta*Math.PI/180)*Math.cos(20*Math.PI/180))` using the variable shown; this is intentionally a classroom-level forward relationship. Model assumptions: K=0.9, λ=0.15406 nm, θ=20°, beta corrected for instrument; strain ignored.


| Input (degrees 2θ) | Predicted nm | Interpretation |
|---:|---:|---|
| 0.24 | 35.2256 | Low-side comparison under fixed assumptions |
| 0.35 | 24.1547 | Reference setting for sensitivity |
| 0.78 | 10.8386 | High-side comparison under fixed assumptions |


### 5. Data collection and reproducibility protocol

Design a comparison that measures **angular line width and corrected profile** while holding specimen state and geometry as steady as possible. Record **observed FWHM; instrumental FWHM; crystal directions**. Repeat an independent reference and state what result would support **whether size and strain explanations are separable from angular trends**. Record the decision rule before looking at a fitted pattern.

### 6. Diagnostic failure mode

Never subtract arbitrary FWHM values as though all peak shapes had the same convolution rule.

In the current unit, a particularly relevant practical trap is **using degrees where radians are required or applying wrong convolution law**. An analyst who ignores it can obtain a mathematically self-consistent answer from the wrong inputs. Diagnose the trap by returning to an invariant: a reference specimen, multiple indexed reflections, a repeated geometry, a known scattering convention or an independent probe. If the disagreement persists, report it as an unresolved limitation. Do not change a correction parameter solely to force a desirable phase or property estimate.


### 7. Knowledge-check and discussion questions

- **Explain:** What is the physical distinction between the quantity named in **Instrument broadening versus sample broadening** and the observable used to estimate it? Give one explicit assumption.
- **Calculate:** Reproduce case MSE-C26 and evaluate how the output changes when the slider parameter moves from 0.24 to 0.78 degrees 2θ.
- **Challenge:** Could **instrument profile asymmetry** explain the observed feature? State a discriminating control rather than merely saying that more data are required.



## Lesson 6.2 — Scherrer crystallite-size estimation

### 1. Physical picture and mathematical meaning

The Scherrer relation D approximately equals Kλ divided by beta cosθ, where beta is sample-related broadening in radians of 2θ and K is a shape factor. It estimates the coherent domain size under assumptions that other broadening sources are negligible or separately accounted for. Physical particles may contain several coherent domains; thus domain size and particle diameter are different quantities.


### 2. What to measure and what it means

Estimate coherent domain size from synthetic corrected angular breadths at two reflections. Vary K over a plausible shape-dependent range to show sensitivity. Compare with a hypothetical electron micrograph particle diameter and identify why the two measures may differ.



### 3. Interpretation, alternative explanations and boundaries

The result is an order-of-magnitude structural descriptor unless the instrument profile, shape, strain and anisotropy have been handled carefully.


One competing explanation to test here is **residual microstrain**. This is not a guaranteed cause, but it deserves a clear discrimination experiment. Decide whether a changed scan range, an independent standard, a different specimen orientation or a second probe would expose that alternative. Also ask whether the proposed test changes one parameter at a time. An experiment that simultaneously changes wavelength, mounting and background correction may produce a new curve without clarifying why it changed.

### 4. Fully specified synthetic calculation

The linked model is **Williamson-Hall breadth**. Its one-variable input is **isotropic microstrain ε** (dimensionless), the selected demonstration value is **0.002**, and the computed value is **0.564362 degrees 2θ**. The exact model expression is `(0.9*0.15406/25+4*eps*Math.sin(25*Math.PI/180))/Math.cos(25*Math.PI/180)*180/Math.PI` using the variable shown; this is intentionally a classroom-level forward relationship. Model assumptions: D=25 nm, θ=25°, simplified Cauchy breadth; not instrumental convolution.


| Input (dimensionless) | Predicted degrees 2θ | Interpretation |
|---:|---:|---|
| 0.001 | 0.457492 | Low-side comparison under fixed assumptions |
| 0.002 | 0.564362 | Reference setting for sensitivity |
| 0.004 | 0.778101 | High-side comparison under fixed assumptions |


### 5. Data collection and reproducibility protocol



### 6. Diagnostic failure mode

A Scherrer estimate from a single noisy peak should not be presented with nanometer-level certainty.




### 7. Knowledge-check and discussion questions

- **Explain:** What is the physical distinction between the quantity named in **Scherrer crystallite-size estimation** and the observable used to estimate it? Give one explicit assumption.
- **Calculate:** Reproduce case MSE-C27 and evaluate how the output changes when the slider parameter moves from 0.001 to 0.004 dimensionless.
- **Challenge:** Could **residual microstrain** explain the observed feature? State a discriminating control rather than merely saying that more data are required.



## Lesson 6.3 — Microstrain and Williamson–Hall plots

### 1. Physical picture and mathematical meaning

Distribution of lattice spacings can broaden diffraction peaks even when coherent domains are large. In a simple isotropic size-plus-strain approximation, beta cosθ is plotted against 4 sinθ; the intercept is associated with coherent size and slope with microstrain. The assumptions neglect anisotropy and complex dislocation fields. Negative fitted intercepts reveal model or data limitations rather than a physically negative size.


### 2. What to measure and what it means

Use four synthetic reflections over a wide angular range and plot corrected beta cosθ versus 4 sinθ. Fit a line, examine uncertainties and compare the inferred strain with an alternative anisotropic broadening model.



### 3. Interpretation, alternative explanations and boundaries

A convincing Williamson–Hall trend requires enough clean, correctly indexed peaks. Good line fit does not prove that the underlying broadening mechanisms were identified uniquely.


One competing explanation to test here is **coherent size anisotropy**. This is not a guaranteed cause, but it deserves a clear discrimination experiment. Decide whether a changed scan range, an independent standard, a different specimen orientation or a second probe would expose that alternative. Also ask whether the proposed test changes one parameter at a time. An experiment that simultaneously changes wavelength, mounting and background correction may produce a new curve without clarifying why it changed.

### 4. Fully specified synthetic calculation

The linked model is **Scherrer coherent domain size**. Its one-variable input is **sample FWHM beta** (degrees 2θ), the selected demonstration value is **0.62**, and the computed value is **13.6357 nm**. The exact model expression is `0.9*0.15406/((beta*Math.PI/180)*Math.cos(20*Math.PI/180))` using the variable shown; this is intentionally a classroom-level forward relationship. Model assumptions: K=0.9, λ=0.15406 nm, θ=20°, beta corrected for instrument; strain ignored.


| Input (degrees 2θ) | Predicted nm | Interpretation |
|---:|---:|---|
| 0.24 | 35.2256 | Low-side comparison under fixed assumptions |
| 0.35 | 24.1547 | Reference setting for sensitivity |
| 0.78 | 10.8386 | High-side comparison under fixed assumptions |


### 5. Data collection and reproducibility protocol



### 6. Diagnostic failure mode

Do not mix degrees with radians when constructing a Williamson–Hall diagram.




### 7. Knowledge-check and discussion questions

- **Explain:** What is the physical distinction between the quantity named in **Microstrain and Williamson–Hall plots** and the observable used to estimate it? Give one explicit assumption.
- **Calculate:** Reproduce case MSE-C28 and evaluate how the output changes when the slider parameter moves from 0.24 to 0.78 degrees 2θ.
- **Challenge:** Could **coherent size anisotropy** explain the observed feature? State a discriminating control rather than merely saying that more data are required.



## Lesson 6.4 — Residual stress by sin-squared-psi method

### 1. Physical picture and mathematical meaning

Elastic strain changes interplanar spacing, and sample tilts probe differently oriented plane normals. Under specific assumptions of stress state and diffraction elastic constants, d-spacing can vary approximately linearly with sin²ψ. The slope depends on stress and the selected reflection, while gradients and texture may violate the simple linear model. Stress-free spacing is often uncertain.


### 2. What to measure and what it means

Plan psi tilts in positive and negative directions to check alignment and shear effects. Estimate slope uncertainty and use a suitable diffraction elastic constant supplied from an independent source. Compare loading and unloading scans to detect irreversible deformation.



### 3. Interpretation, alternative explanations and boundaries

Residual-stress conclusions require a transparent elastic model, calibration and sample geometry. The sign of an inferred stress should be checked against a physically meaningful convention.


One competing explanation to test here is **stacking faults**. This is not a guaranteed cause, but it deserves a clear discrimination experiment. Decide whether a changed scan range, an independent standard, a different specimen orientation or a second probe would expose that alternative. Also ask whether the proposed test changes one parameter at a time. An experiment that simultaneously changes wavelength, mounting and background correction may produce a new curve without clarifying why it changed.

### 4. Fully specified synthetic calculation

The linked model is **Williamson-Hall breadth**. Its one-variable input is **isotropic microstrain ε** (dimensionless), the selected demonstration value is **0.0038**, and the computed value is **0.756728 degrees 2θ**. The exact model expression is `(0.9*0.15406/25+4*eps*Math.sin(25*Math.PI/180))/Math.cos(25*Math.PI/180)*180/Math.PI` using the variable shown; this is intentionally a classroom-level forward relationship. Model assumptions: D=25 nm, θ=25°, simplified Cauchy breadth; not instrumental convolution.


| Input (dimensionless) | Predicted degrees 2θ | Interpretation |
|---:|---:|---|
| 0.001 | 0.457492 | Low-side comparison under fixed assumptions |
| 0.002 | 0.564362 | Reference setting for sensitivity |
| 0.004 | 0.778101 | High-side comparison under fixed assumptions |


### 5. Data collection and reproducibility protocol



### 6. Diagnostic failure mode

A peak shift observed between two samples is not automatically residual stress; composition and temperature alter lattice parameters too.




### 7. Knowledge-check and discussion questions

- **Explain:** What is the physical distinction between the quantity named in **Residual stress by sin-squared-psi method** and the observable used to estimate it? Give one explicit assumption.
- **Calculate:** Reproduce case MSE-C29 and evaluate how the output changes when the slider parameter moves from 0.001 to 0.004 dimensionless.
- **Challenge:** Could **stacking faults** explain the observed feature? State a discriminating control rather than merely saying that more data are required.



## Lesson 6.5 — Defects, stacking faults and diffuse patterns

### 1. Physical picture and mathematical meaning

Dislocations, stacking faults, antiphase boundaries and finite correlation lengths can produce anisotropic peak broadening, asymmetric profiles or diffuse scattering. Different defects often create similar signatures in a limited measurement range. Pair distribution function analysis and complementary imaging can constrain local order, but data transformations introduce termination ripples and sensitivity to normalization.


### 2. What to measure and what it means

Compare simulated patterns with isotropic peak width increase, hkl-dependent broadening and asymmetric shoulders. Create a model-selection table that states which additional reflections and microscopy observations would discriminate explanations.



### 3. Interpretation, alternative explanations and boundaries

Defect characterization is a convergence of evidence from diffraction, processing history and microscopy rather than a one-parameter inversion.


One competing explanation to test here is **dislocation-density gradients**. This is not a guaranteed cause, but it deserves a clear discrimination experiment. Decide whether a changed scan range, an independent standard, a different specimen orientation or a second probe would expose that alternative. Also ask whether the proposed test changes one parameter at a time. An experiment that simultaneously changes wavelength, mounting and background correction may produce a new curve without clarifying why it changed.

### 4. Fully specified synthetic calculation

The linked model is **Scherrer coherent domain size**. Its one-variable input is **sample FWHM beta** (degrees 2θ), the selected demonstration value is **0.96**, and the computed value is **8.80639 nm**. The exact model expression is `0.9*0.15406/((beta*Math.PI/180)*Math.cos(20*Math.PI/180))` using the variable shown; this is intentionally a classroom-level forward relationship. Model assumptions: K=0.9, λ=0.15406 nm, θ=20°, beta corrected for instrument; strain ignored.


| Input (degrees 2θ) | Predicted nm | Interpretation |
|---:|---:|---|
| 0.24 | 35.2256 | Low-side comparison under fixed assumptions |
| 0.35 | 24.1547 | Reference setting for sensitivity |
| 0.78 | 10.8386 | High-side comparison under fixed assumptions |


### 5. Data collection and reproducibility protocol



### 6. Diagnostic failure mode

Calling an asymmetric line a stacking-fault measurement without a calibrated physical model overstates the evidence.




### 7. Knowledge-check and discussion questions

- **Explain:** What is the physical distinction between the quantity named in **Defects, stacking faults and diffuse patterns** and the observable used to estimate it? Give one explicit assumption.
- **Calculate:** Reproduce case MSE-C30 and evaluate how the output changes when the slider parameter moves from 0.24 to 0.78 degrees 2θ.
- **Challenge:** Could **dislocation-density gradients** explain the observed feature? State a discriminating control rather than merely saying that more data are required.



## Explore two independent interactive model families

<!-- MODEL_10 -->

<!-- MODEL_11 -->

## Integrated investigation: Nanocrystal size versus residual strain

### Evidence brief

Two batches of nanocrystalline alloy show broader peaks after mechanical milling. The process can reduce coherent domain size while introducing elastic microstrain and changing texture. A single Scherrer result would confound these causes.



### Proposed analysis

Build a table of instrumental widths, measured FWHM and corrected breadth at several 2θ positions. Try both Scherrer and simplified Williamson–Hall analyses, record residuals and include a mock TEM grain-size distribution for comparison.



### Evaluation of the competing explanations

The two methods estimate related but different structural attributes; neither directly measures the particle diameter distribution. Agreement is supportive but cannot eliminate anisotropic defect broadening.



### Limitations and ethical interpretation

Near the resolution limit, small errors in instrument subtraction propagate strongly to size estimates. Report credible ranges rather than falsely precise sizes.



### Assessment rubric





## Unit research commentary — evidence across scales

Diffraction profile analysis requires an explicit statement of what is being fitted. A measured broad line may combine the instrument spectral response, optical divergence, coherent domain size, lattice microstrain, defects and stacking statistics. If a student inserts the observed FWHM directly into the Scherrer expression, the resulting number often looks credible because the units can still be made consistent. The mistake is physical, not merely arithmetic: the model expects a sample-broadening contribution under its assumptions. Obtain an appropriate instrument reference and choose a profile model before estimating specimen properties.

The simplest teaching correction for Gaussian widths uses quadrature subtraction. A Lorentzian model instead has different convolution behavior, and a real pattern may require a pseudo-Voigt or instrument-specific function. Once corrected widths are available for several accurately indexed reflections, compare a size-only hypothesis with an isotropic Williamson–Hall size-plus-strain hypothesis. Examine whether the angular trend is coherent across reflections and whether errors are similar enough to justify an ordinary unweighted fit. An apparently negative fitted domain-size intercept has no valid physical meaning; it signals an inadequate model or noisy data.

Now consider a nanocrystalline coating with elongated grains. Different hkl peaks may broaden differently because the coherent domains and strains are direction-dependent. The isotropic size model can return one effective number while hiding a distribution of domain shapes. Complementary microscopy is not necessarily a definitive replacement: it images particle morphology, which may contain several coherently diffracting subdomains. A careful report distinguishes crystallite or coherent domain size from particle diameter and explains how both techniques sample the specimen. The assessment goal is to produce a credible range, identify at least two plausible line-broadening mechanisms and propose a measurement that would discriminate them rather than declaring one exact nanometre size.

### End-of-unit examiner challenge: Line profiles, defects and deformation

Write an evidence-based defense of **whether size and strain explanations are separable from angular trends**. Begin by defining how **angular line width and corrected profile** would be measured and listing the necessary independent controls for **observed FWHM; instrumental FWHM; crystal directions**. Then name a physically distinct mechanism that could imitate the preferred explanation: **using degrees where radians are required or applying wrong convolution law**. The response must show why that mechanism is plausible, rather than merely listing it as a caveat. Select one follow-up measurement that makes different predictions for the rival models; state what a negative result would mean. Finally prepare an annotated calculation from the two teaching formulas associated with this unit and explain why exact numerical agreement with a forward equation does not validate the specimen interpretation. Include an uncertainty estimate and say whether the proposed material conclusion is supported, conditional or unresolved. This is a reasoning task using synthetic evidence, not an authorization to operate an instrument.
