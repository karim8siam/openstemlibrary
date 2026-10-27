# Unit 7: Strain, stress, and time-dependent lattice response

**Guiding question:** How can a reproducible lattice-spacing change inform deformation without confusing it with composition or temperature?

This unit connects strain interpretation and in situ measurement to an observable experiment. Every example is fictional and intentionally simplified. The sequence is designed so that the first two lessons provide definitions, the middle lessons test consequences, and the fifth lesson confronts ambiguity. Read plots as conditional calculations rather than laboratory observations.

## Investigation framework: Strain interpretation and in situ measurement





### Unit-wide reasoning objective




## Lesson 7.1 — Lattice strain and reference spacings

### 1. Physical picture and mathematical meaning

An elastic strain measured along the normal to a chosen diffraction plane is often defined as (d − d0)/d0. The reference d0 must correspond to the relevant stress-free material state and reflection. Local chemistry, temperature, coherent precipitates and a changed composition can all modify d0. If the sample is anisotropic, a macroscopic applied strain is not automatically equal to one measured plane-family strain.


### 2. What to measure and what it means

Compute d from a calibrated peak position in a simulated unstrained coupon and two loaded coupons. Estimate the effect of a small zero-angle error on the inferred strain, and compare the resulting systematic bias with the physical strain signal. Keep the same reflection family and wavelength.


Consider the targeted decision **whether a measured shift persists after corrections and control scans**. Specify one null hypothesis that competes with the preferred explanation and design a control that could falsify it. Make a small table of predicted features for both interpretations before inspecting any synthetic data. Such predeclared contrasts reduce the temptation to keep only peaks that favor the desired material narrative. Calibration, specimen preparation and the physics of scattering should be assessed before microstructure claims are written.

### 3. Interpretation, alternative explanations and boundaries

A consistent shift across several independent reflections and load steps supports a real lattice response, but resolving the mechanical cause still requires geometry and material assumptions.


One competing explanation to test here is **composition-dependent cell parameter**. This is not a guaranteed cause, but it deserves a clear discrimination experiment. Decide whether a changed scan range, an independent standard, a different specimen orientation or a second probe would expose that alternative. Also ask whether the proposed test changes one parameter at a time. An experiment that simultaneously changes wavelength, mounting and background correction may produce a new curve without clarifying why it changed.

### 4. Fully specified synthetic calculation

The linked model is **Uniaxial elastic lattice strain**. Its one-variable input is **elastic strain** (dimensionless), the selected demonstration value is **-0.00325**, and the computed value is **0.19935 nm**. The exact model expression is `0.200*(1+strain)` using the variable shown; this is intentionally a classroom-level forward relationship. Model assumptions: Reference spacing d0=0.200 nm; strain along measured plane normal only.


| Input (dimensionless) | Predicted nm | Interpretation |
|---:|---:|---|
| -0.0025 | 0.1995 | Low-side comparison under fixed assumptions |
| 0 | 0.2 | Reference setting for sensitivity |
| 0.0025 | 0.2005 | High-side comparison under fixed assumptions |


### 5. Data collection and reproducibility protocol

Design a comparison that measures **plane-normal lattice strain** while holding specimen state and geometry as steady as possible. Record **reference d0; specimen tilt; processing state**. Repeat an independent reference and state what result would support **whether a measured shift persists after corrections and control scans**. Record the decision rule before looking at a fitted pattern.

### 6. Diagnostic failure mode

Do not interpret a nonzero lattice-strain calculation as proof of externally applied stress without a defensible stress-free reference.

In the current unit, a particularly relevant practical trap is **assigning every shift to stress rather than chemistry or temperature**. An analyst who ignores it can obtain a mathematically self-consistent answer from the wrong inputs. Diagnose the trap by returning to an invariant: a reference specimen, multiple indexed reflections, a repeated geometry, a known scattering convention or an independent probe. If the disagreement persists, report it as an unresolved limitation. Do not change a correction parameter solely to force a desirable phase or property estimate.


### 7. Knowledge-check and discussion questions

- **Explain:** What is the physical distinction between the quantity named in **Lattice strain and reference spacings** and the observable used to estimate it? Give one explicit assumption.
- **Calculate:** Reproduce case MSE-C31 and evaluate how the output changes when the slider parameter moves from -0.0025 to 0.0025 dimensionless.
- **Challenge:** Could **composition-dependent cell parameter** explain the observed feature? State a discriminating control rather than merely saying that more data are required.



## Lesson 7.2 — Strain tensors and diffraction-vector direction

### 1. Physical picture and mathematical meaning

Small deformation is described by a strain tensor, while a diffraction measurement probes the projection of strain along one scattering-vector direction. Changing specimen tilt or azimuth samples different combinations of tensor components. One longitudinal projection is insufficient to reconstruct a general tensor. Symmetry and engineering loading constraints may reduce the number of unknown components, but their validity must be assessed.


### 2. What to measure and what it means

Plan measurements of at least three noncollinear normal directions in a simple plane-stress training example and construct the corresponding directional strain equations. Check the condition of the resulting inverse problem. Include mirror tilts to reveal alignment errors.



### 3. Interpretation, alternative explanations and boundaries

When the set of measured diffraction-vector directions is geometrically insufficient, a tensor fit may look numerically stable but remain nonunique.


One competing explanation to test here is **temperature drift**. This is not a guaranteed cause, but it deserves a clear discrimination experiment. Decide whether a changed scan range, an independent standard, a different specimen orientation or a second probe would expose that alternative. Also ask whether the proposed test changes one parameter at a time. An experiment that simultaneously changes wavelength, mounting and background correction may produce a new curve without clarifying why it changed.

### 4. Fully specified synthetic calculation

The linked model is **Gaussian FWHM sample correction**. Its one-variable input is **measured FWHM** (degrees 2θ), the selected demonstration value is **0.46**, and the computed value is **0.448999 degrees 2θ**. The exact model expression is `Math.sqrt(Math.max(0,observed*observed-0.10*0.10))` using the variable shown; this is intentionally a classroom-level forward relationship. Model assumptions: Gaussian widths and instrumental FWHM=0.10°; inappropriate for pure Lorentz profiles.


| Input (degrees 2θ) | Predicted degrees 2θ | Interpretation |
|---:|---:|---|
| 0.28 | 0.261534 | Low-side comparison under fixed assumptions |
| 0.45 | 0.438748 | Reference setting for sensitivity |
| 0.82 | 0.81388 | High-side comparison under fixed assumptions |


### 5. Data collection and reproducibility protocol



### 6. Diagnostic failure mode

Do not confuse the direction of the incident beam, plane normal and sample loading axis as though they were always the same.




### 7. Knowledge-check and discussion questions

- **Explain:** What is the physical distinction between the quantity named in **Strain tensors and diffraction-vector direction** and the observable used to estimate it? Give one explicit assumption.
- **Calculate:** Reproduce case MSE-C32 and evaluate how the output changes when the slider parameter moves from 0.28 to 0.82 degrees 2θ.
- **Challenge:** Could **temperature drift** explain the observed feature? State a discriminating control rather than merely saying that more data are required.



## Lesson 7.3 — Thermal expansion using diffraction

### 1. Physical picture and mathematical meaning

Lattice parameters measured over temperature can reveal thermal expansion, phase transformations and anisotropy, provided thermal equilibration and instrument drift are controlled. A linear expansion coefficient is locally the derivative of log length with respect to temperature, not necessarily a constant over a broad temperature range. Different lattice directions may expand by different amounts. Thermally induced stress can occur if expansion is constrained.


### 2. What to measure and what it means

Produce a synthetic a(T) series for a hypothetical cubic specimen, calculate the slope in a limited temperature interval and compare heating with cooling. Use an internal standard or independent thermometer to check instrumental drift. Identify any discontinuity as a candidate for additional study, not proof of a new phase by itself.



### 3. Interpretation, alternative explanations and boundaries

A repeatable temperature-dependent peak shift is a useful thermal descriptor but depends on calibrated sample temperature and a known reflection.


One competing explanation to test here is **uncertain stress-free reference**. This is not a guaranteed cause, but it deserves a clear discrimination experiment. Decide whether a changed scan range, an independent standard, a different specimen orientation or a second probe would expose that alternative. Also ask whether the proposed test changes one parameter at a time. An experiment that simultaneously changes wavelength, mounting and background correction may produce a new curve without clarifying why it changed.

### 4. Fully specified synthetic calculation

The linked model is **Uniaxial elastic lattice strain**. Its one-variable input is **elastic strain** (dimensionless), the selected demonstration value is **-0.00025**, and the computed value is **0.19995 nm**. The exact model expression is `0.200*(1+strain)` using the variable shown; this is intentionally a classroom-level forward relationship. Model assumptions: Reference spacing d0=0.200 nm; strain along measured plane normal only.


| Input (dimensionless) | Predicted nm | Interpretation |
|---:|---:|---|
| -0.0025 | 0.1995 | Low-side comparison under fixed assumptions |
| 0 | 0.2 | Reference setting for sensitivity |
| 0.0025 | 0.2005 | High-side comparison under fixed assumptions |


### 5. Data collection and reproducibility protocol



### 6. Diagnostic failure mode

Never assume that an irreversible change after heating is ordinary reversible expansion; oxidation, phase changes or strain relaxation may have occurred.




### 7. Knowledge-check and discussion questions

- **Explain:** What is the physical distinction between the quantity named in **Thermal expansion using diffraction** and the observable used to estimate it? Give one explicit assumption.
- **Calculate:** Reproduce case MSE-C33 and evaluate how the output changes when the slider parameter moves from -0.0025 to 0.0025 dimensionless.
- **Challenge:** Could **uncertain stress-free reference** explain the observed feature? State a discriminating control rather than merely saying that more data are required.



## Lesson 7.4 — Stress determination and diffraction elastic constants

### 1. Physical picture and mathematical meaning

Converting measured plane strains into stresses requires elastic properties appropriate to the crystal or polycrystal model. The sin-squared-psi method is one specialized reduction under geometric and mechanical assumptions; crystal orientation and texture can change the effective diffraction elastic constants. Residual and applied stress should be distinguished, particularly after surface processing or welding.


### 2. What to measure and what it means

For a hypothetical isotropic biaxial state, prepare d versus sin²ψ data with replicated angles and estimate a slope with uncertainty. Check linearity and symmetry between positive and negative sample tilt. Record how a different modulus assumption would change the stress estimate.



### 3. Interpretation, alternative explanations and boundaries

Reporting a stress value demands both measurement uncertainty and model uncertainty. A narrow regression confidence interval does not cover uncertainty in elastic constants or unknown stress gradients.


One competing explanation to test here is **texture-dependent elastic constants**. This is not a guaranteed cause, but it deserves a clear discrimination experiment. Decide whether a changed scan range, an independent standard, a different specimen orientation or a second probe would expose that alternative. Also ask whether the proposed test changes one parameter at a time. An experiment that simultaneously changes wavelength, mounting and background correction may produce a new curve without clarifying why it changed.

### 4. Fully specified synthetic calculation

The linked model is **Gaussian FWHM sample correction**. Its one-variable input is **measured FWHM** (degrees 2θ), the selected demonstration value is **0.78**, and the computed value is **0.773563 degrees 2θ**. The exact model expression is `Math.sqrt(Math.max(0,observed*observed-0.10*0.10))` using the variable shown; this is intentionally a classroom-level forward relationship. Model assumptions: Gaussian widths and instrumental FWHM=0.10°; inappropriate for pure Lorentz profiles.


| Input (degrees 2θ) | Predicted degrees 2θ | Interpretation |
|---:|---:|---|
| 0.28 | 0.261534 | Low-side comparison under fixed assumptions |
| 0.45 | 0.438748 | Reference setting for sensitivity |
| 0.82 | 0.81388 | High-side comparison under fixed assumptions |


### 5. Data collection and reproducibility protocol



### 6. Diagnostic failure mode

A negative stress result depends on the declared tension/compression convention and is not necessarily an instrument error.




### 7. Knowledge-check and discussion questions

- **Explain:** What is the physical distinction between the quantity named in **Stress determination and diffraction elastic constants** and the observable used to estimate it? Give one explicit assumption.
- **Calculate:** Reproduce case MSE-C34 and evaluate how the output changes when the slider parameter moves from 0.28 to 0.82 degrees 2θ.
- **Challenge:** Could **texture-dependent elastic constants** explain the observed feature? State a discriminating control rather than merely saying that more data are required.



## Lesson 7.5 — In situ diffraction during processing

### 1. Physical picture and mathematical meaning

Time-resolved diffraction can track phase evolution, texture development, elastic response or lattice expansion while a specimen is loaded, cooled, heated or reacted. Measurement timing, detector response, thermal gradients and phase overlap impose temporal and spatial averaging. A sequence of peak positions can reflect simultaneous changes in stress, composition and temperature.


### 2. What to measure and what it means

Design a synthetic compression experiment recording load, time, temperature, several reflections and one independent strain gauge. Mark acquisition timestamps and compare whether diffraction peaks respond reversibly with load or exhibit hysteresis. Propose complementary microscopy for irreversible changes.



### 3. Interpretation, alternative explanations and boundaries

A mechanistic processing narrative is strongest when multiple observables change together in a way predicted before the experiment.


One competing explanation to test here is **inhomogeneous stress gradient**. This is not a guaranteed cause, but it deserves a clear discrimination experiment. Decide whether a changed scan range, an independent standard, a different specimen orientation or a second probe would expose that alternative. Also ask whether the proposed test changes one parameter at a time. An experiment that simultaneously changes wavelength, mounting and background correction may produce a new curve without clarifying why it changed.

### 4. Fully specified synthetic calculation

The linked model is **Uniaxial elastic lattice strain**. Its one-variable input is **elastic strain** (dimensionless), the selected demonstration value is **0.00275**, and the computed value is **0.20055 nm**. The exact model expression is `0.200*(1+strain)` using the variable shown; this is intentionally a classroom-level forward relationship. Model assumptions: Reference spacing d0=0.200 nm; strain along measured plane normal only.


| Input (dimensionless) | Predicted nm | Interpretation |
|---:|---:|---|
| -0.0025 | 0.1995 | Low-side comparison under fixed assumptions |
| 0 | 0.2 | Reference setting for sensitivity |
| 0.0025 | 0.2005 | High-side comparison under fixed assumptions |


### 5. Data collection and reproducibility protocol



### 6. Diagnostic failure mode

Do not present an in situ diffraction movie as a quantitative stress field without adequate calibration and an appropriate constitutive model.




### 7. Knowledge-check and discussion questions

- **Explain:** What is the physical distinction between the quantity named in **In situ diffraction during processing** and the observable used to estimate it? Give one explicit assumption.
- **Calculate:** Reproduce case MSE-C35 and evaluate how the output changes when the slider parameter moves from -0.0025 to 0.0025 dimensionless.
- **Challenge:** Could **inhomogeneous stress gradient** explain the observed feature? State a discriminating control rather than merely saying that more data are required.



## Explore two independent interactive model families

<!-- MODEL_12 -->

<!-- MODEL_13 -->

## Integrated investigation: Residual stress from diffraction plus processing history

### Evidence brief

A welded component is measured at several tilts and exhibits a nominal sin²ψ trend. The part has strong texture and a compositional gradient, challenging the simple isotropic diffraction elastic model.



### Proposed analysis

Prepare a sampling map across the weld and heat-affected zone. For each location collect symmetric positive and negative tilt measurements, thermal history and independent hardness information. Check whether d versus sin²ψ remains linear and whether its intercept drifts across the part.



### Evaluation of the competing explanations

A conditional elastic stress estimate can be made with stated elastic constants and geometry. Nonlinearity may reflect stress gradients, shear components or model failure, and requires additional experimental design.



### Limitations and ethical interpretation

The synthetic data cannot support a weld service-life decision. Real engineering acceptance requires qualified personnel and applicable standards.



### Assessment rubric





## Unit research commentary — evidence across scales

A strain measurement becomes a stress inference only after constitutive assumptions and reference spacing are specified. Imagine two samples of nominally the same alloy, one measured at room temperature and the other measured shortly after heating. A peak-position shift might result from thermal expansion, changed composition, retained elastic strain, sample displacement or several effects together. Calculate directional lattice strain only against an appropriate d0 and then explain which sources of error could mimic it. Small angular offsets can create systematic strain differences even if the peak-fitting algorithm reports tiny statistical uncertainty.

To estimate a tensor, change specimen orientation so different plane normals are sampled. With sufficiently diverse directions, the measured normal strains constrain combinations of the strain components. If all directions are nearly parallel, the inversion becomes poorly conditioned and some components remain essentially unconstrained. When converting strain to stress, crystallographic elastic anisotropy and texture may change the relevant elastic constants. A simple isotropic approximation can illustrate the method, but a welded or highly textured real component may require a more specialized model and independent calibration.

Plan a synthetic in situ heating and loading sequence, recording specimen temperature, external force, acquisition time and at least three indexed reflections. Separate reversible elastic changes from irreversible transformation signatures by comparing repeated load cycles and heating/cooling curves. A credible stress claim should survive the use of positive and negative tilts where geometry warrants them, retain both fitted and raw d-spacing data, and report uncertainty in elastic constants. If several hypotheses remain compatible, the correct conclusion is a qualified strain observation and a proposed control. The book’s calculator cannot certify residual-stress safety, predict fatigue life or replace an applicable engineering standard.

### End-of-unit examiner challenge: Strain, stress, and time-dependent lattice response

Write an evidence-based defense of **whether a measured shift persists after corrections and control scans**. Begin by defining how **plane-normal lattice strain** would be measured and listing the necessary independent controls for **reference d0; specimen tilt; processing state**. Then name a physically distinct mechanism that could imitate the preferred explanation: **assigning every shift to stress rather than chemistry or temperature**. The response must show why that mechanism is plausible, rather than merely listing it as a caveat. Select one follow-up measurement that makes different predictions for the rival models; state what a negative result would mean. Finally prepare an annotated calculation from the two teaching formulas associated with this unit and explain why exact numerical agreement with a forward equation does not validate the specimen interpretation. Include an uncertainty estimate and say whether the proposed material conclusion is supported, conditional or unresolved. This is a reasoning task using synthetic evidence, not an authorization to operate an instrument.
