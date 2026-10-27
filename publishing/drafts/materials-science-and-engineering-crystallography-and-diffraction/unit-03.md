# Unit 3: Wave scattering and structure factors

**Guiding question:** What physically makes a diffraction peak strong, weak, extinct, or distorted?

This unit connects interference and scattering amplitudes to an observable experiment. Every example is fictional and intentionally simplified. The sequence is designed so that the first two lessons provide definitions, the middle lessons test consequences, and the fifth lesson confronts ambiguity. Read plots as conditional calculations rather than laboratory observations.

## Investigation framework: Interference and scattering amplitudes





### Unit-wide reasoning objective




## Lesson 3.1 — Wave phase and Bragg law

### 1. Physical picture and mathematical meaning

Diffraction intensity arises from coherent phase differences among waves scattered from ordered material. Bragg’s relation nλ = 2d sinθ expresses constructive interference for equally spaced planes. In the conventional powder-diffraction display, the reported horizontal angle is generally 2θ, not θ. Order n may also be viewed through higher-index reflections.


### 2. What to measure and what it means

Choose an illustrative X-ray wavelength and three plane spacings. Predict whether the first-order Bragg angle exists and locate peaks on a 2θ scale. Double one spacing and compare the new angle. Record that the instrument geometry, sample height and calibration affect measured positions.


Consider the targeted decision **whether predicted extinctions agree with detected and nondetected reflections**. Specify one null hypothesis that competes with the preferred explanation and design a control that could falsify it. Make a small table of predicted features for both interpretations before inspecting any synthetic data. Such predeclared contrasts reduce the temptation to keep only peaks that favor the desired material narrative. Calibration, specimen preparation and the physics of scattering should be assessed before microstructure claims are written.

### 3. Interpretation, alternative explanations and boundaries

Bragg’s law translates an angular measurement into spacing only if the wavelength and geometry are known. Peak maxima may also shift under stress, sample displacement and profile asymmetry.


One competing explanation to test here is **different basis scattering factors**. This is not a guaranteed cause, but it deserves a clear discrimination experiment. Decide whether a changed scan range, an independent standard, a different specimen orientation or a second probe would expose that alternative. Also ask whether the proposed test changes one parameter at a time. An experiment that simultaneously changes wavelength, mounting and background correction may produce a new curve without clarifying why it changed.

### 4. Fully specified synthetic calculation

The linked model is **First-order Bragg peak 2θ**. Its one-variable input is **plane spacing d** (nm), the selected demonstration value is **0.175**, and the computed value is **52.2296 degrees**. The exact model expression is `2*Math.asin(0.15406/(2*d))*180/Math.PI` using the variable shown; this is intentionally a classroom-level forward relationship. Model assumptions: Monochromatic λ=0.15406 nm; first order; sample displacement ignored.


| Input (nm) | Predicted degrees | Interpretation |
|---:|---:|---|
| 0.185 | 49.2123 | Low-side comparison under fixed assumptions |
| 0.24 | 37.4418 | Reference setting for sensitivity |
| 0.32 | 27.8579 | High-side comparison under fixed assumptions |


### 5. Data collection and reproducibility protocol

Design a comparison that measures **coherent scattering amplitude and detector intensity** while holding specimen state and geometry as steady as possible. Record **wavelength; scattering angle; atomic basis; reflection family**. Repeat an independent reference and state what result would support **whether predicted extinctions agree with detected and nondetected reflections**. Record the decision rule before looking at a fitted pattern.

### 6. Diagnostic failure mode

Do not insert 2θ into sinθ or attempt arcsin with an argument greater than one.

In the current unit, a particularly relevant practical trap is **mistaking a weak or masked line for an exact symmetry extinction**. An analyst who ignores it can obtain a mathematically self-consistent answer from the wrong inputs. Diagnose the trap by returning to an invariant: a reference specimen, multiple indexed reflections, a repeated geometry, a known scattering convention or an independent probe. If the disagreement persists, report it as an unresolved limitation. Do not change a correction parameter solely to force a desirable phase or property estimate.


### 7. Knowledge-check and discussion questions

- **Explain:** What is the physical distinction between the quantity named in **Wave phase and Bragg law** and the observable used to estimate it? Give one explicit assumption.
- **Calculate:** Reproduce case MSE-C11 and evaluate how the output changes when the slider parameter moves from 0.185 to 0.32 nm.
- **Challenge:** Could **different basis scattering factors** explain the observed feature? State a discriminating control rather than merely saying that more data are required.



## Lesson 3.2 — Scattering factors and atomic species

### 1. Physical picture and mathematical meaning

An atomic scattering factor is the coherent amplitude from electrons for conventional X-ray scattering; it depends on scattering angle and atomic electron distribution. Neutron nuclear scattering lengths follow different isotope-dependent rules, and magnetic neutron scattering adds other information. Consequently, contrast cannot be generalized from X-rays to neutrons merely by atomic number. Resonant X-ray measurements near absorption edges can modify elemental sensitivity.


### 2. What to measure and what it means

Simulate two atomic sites with different real scattering strengths and vary their relative occupancy while preserving lattice dimensions. Compare relative structure factors for several reflections. State that numerical factors are illustrative and not tabulated atomic form factors.



### 3. Interpretation, alternative explanations and boundaries

Reflection intensities may support site substitution, occupancy or ordering, but scale, absorption, thermal displacement and preferred orientation introduce correlations.


One competing explanation to test here is **multiple diffraction**. This is not a guaranteed cause, but it deserves a clear discrimination experiment. Decide whether a changed scan range, an independent standard, a different specimen orientation or a second probe would expose that alternative. Also ask whether the proposed test changes one parameter at a time. An experiment that simultaneously changes wavelength, mounting and background correction may produce a new curve without clarifying why it changed.

### 4. Fully specified synthetic calculation

The linked model is **BCC two-site intensity proxy**. Its one-variable input is **relative second-site scattering** (relative), the selected demonstration value is **0.5**, and the computed value is **0.25 relative intensity**. The exact model expression is `Math.pow(1-f,2)` using the variable shown; this is intentionally a classroom-level forward relationship. Model assumptions: For 100 reflection with basis sites 000 and ½½½, unit first scattering amplitude, real scalar factors.


| Input (relative) | Predicted relative intensity | Interpretation |
|---:|---:|---|
| 0.5 | 0.25 | Low-side comparison under fixed assumptions |
| 1 | 0 | Reference setting for sensitivity |
| 1.25 | 0.0625 | High-side comparison under fixed assumptions |


### 5. Data collection and reproducibility protocol



### 6. Diagnostic failure mode

A peak-height ratio cannot usually be converted directly into a chemical composition without a calibrated intensity model.




### 7. Knowledge-check and discussion questions

- **Explain:** What is the physical distinction between the quantity named in **Scattering factors and atomic species** and the observable used to estimate it? Give one explicit assumption.
- **Calculate:** Reproduce case MSE-C12 and evaluate how the output changes when the slider parameter moves from 0.5 to 1.25 relative.
- **Challenge:** Could **multiple diffraction** explain the observed feature? State a discriminating control rather than merely saying that more data are required.



## Lesson 3.3 — Structure factors and systematic absences

### 1. Physical picture and mathematical meaning

The unit-cell structure factor sums atomic scattering amplitudes multiplied by position-dependent phase factors. Centering operations can cancel contributions for particular hkl combinations. In an ideal monoatomic body-centered cubic motif with identical scatterers, h+k+l odd gives zero; in an ideal face-centered motif, h, k and l must be all odd or all even. Glide and screw operations impose additional reflection conditions.


### 2. What to measure and what it means

Use explicit complex phases for a centered pair and calculate amplitudes for 100, 110, 111 and 200 reflections. Then change one site scattering factor; an extinction derived from two identical sites is no longer guaranteed if that change destroys the assumed structure symmetry.



### 3. Interpretation, alternative explanations and boundaries

Systematic absence rules help narrow symmetry but should be tested over a representative set of available peaks, with detection limits documented.


One competing explanation to test here is **polarization and absorption**. This is not a guaranteed cause, but it deserves a clear discrimination experiment. Decide whether a changed scan range, an independent standard, a different specimen orientation or a second probe would expose that alternative. Also ask whether the proposed test changes one parameter at a time. An experiment that simultaneously changes wavelength, mounting and background correction may produce a new curve without clarifying why it changed.

### 4. Fully specified synthetic calculation

The linked model is **First-order Bragg peak 2θ**. Its one-variable input is **plane spacing d** (nm), the selected demonstration value is **0.255**, and the computed value is **35.165 degrees**. The exact model expression is `2*Math.asin(0.15406/(2*d))*180/Math.PI` using the variable shown; this is intentionally a classroom-level forward relationship. Model assumptions: Monochromatic λ=0.15406 nm; first order; sample displacement ignored.


| Input (nm) | Predicted degrees | Interpretation |
|---:|---:|---|
| 0.185 | 49.2123 | Low-side comparison under fixed assumptions |
| 0.24 | 37.4418 | Reference setting for sensitivity |
| 0.32 | 27.8579 | High-side comparison under fixed assumptions |


### 5. Data collection and reproducibility protocol



### 6. Diagnostic failure mode

Real disorder, resonant effects, multiple diffraction and indexing mistakes can complicate simple extinction-based diagnoses.




### 7. Knowledge-check and discussion questions

- **Explain:** What is the physical distinction between the quantity named in **Structure factors and systematic absences** and the observable used to estimate it? Give one explicit assumption.
- **Calculate:** Reproduce case MSE-C13 and evaluate how the output changes when the slider parameter moves from 0.185 to 0.32 nm.
- **Challenge:** Could **polarization and absorption** explain the observed feature? State a discriminating control rather than merely saying that more data are required.



## Lesson 3.4 — Peak multiplicity, polarization and Lorentz factors

### 1. Physical picture and mathematical meaning

Measured diffraction intensity combines structure factor, number of equivalent planes, geometrical exposure, incident-beam polarization and detector efficiency. Powder diffractometers sample diffraction rings differently from single-crystal experiments; the correction formula depends on geometry and analysis method. Peak integration is more robust than raw height when broadening differs between specimens.


### 2. What to measure and what it means

Take two reflections with the same hypothetical squared structure factor and apply different known multiplicities. Then alter broadening while conserving integrated area to show why comparing maximum intensity alone is misleading. Keep calibration data and the exact instrumental mode in the record.



### 3. Interpretation, alternative explanations and boundaries

A defensible intensity comparison includes background subtraction, scale, geometry, absorption and texture assumptions, rather than attributing all differences to atom positions.


One competing explanation to test here is **thermal displacement**. This is not a guaranteed cause, but it deserves a clear discrimination experiment. Decide whether a changed scan range, an independent standard, a different specimen orientation or a second probe would expose that alternative. Also ask whether the proposed test changes one parameter at a time. An experiment that simultaneously changes wavelength, mounting and background correction may produce a new curve without clarifying why it changed.

### 4. Fully specified synthetic calculation

The linked model is **BCC two-site intensity proxy**. Its one-variable input is **relative second-site scattering** (relative), the selected demonstration value is **0.95**, and the computed value is **0.0025 relative intensity**. The exact model expression is `Math.pow(1-f,2)` using the variable shown; this is intentionally a classroom-level forward relationship. Model assumptions: For 100 reflection with basis sites 000 and ½½½, unit first scattering amplitude, real scalar factors.


| Input (relative) | Predicted relative intensity | Interpretation |
|---:|---:|---|
| 0.5 | 0.25 | Low-side comparison under fixed assumptions |
| 1 | 0 | Reference setting for sensitivity |
| 1.25 | 0.0625 | High-side comparison under fixed assumptions |


### 5. Data collection and reproducibility protocol



### 6. Diagnostic failure mode

Never transplant one textbook Lorentz-polarization correction uncritically between reflection and transmission geometries.




### 7. Knowledge-check and discussion questions

- **Explain:** What is the physical distinction between the quantity named in **Peak multiplicity, polarization and Lorentz factors** and the observable used to estimate it? Give one explicit assumption.
- **Calculate:** Reproduce case MSE-C14 and evaluate how the output changes when the slider parameter moves from 0.5 to 1.25 relative.
- **Challenge:** Could **thermal displacement** explain the observed feature? State a discriminating control rather than merely saying that more data are required.



## Lesson 3.5 — Debye-Waller disorder and diffuse scattering

### 1. Physical picture and mathematical meaning

Thermal vibrations attenuate coherent Bragg intensity with increasing scattering-vector magnitude, while static positional disorder can modify both Bragg peaks and diffuse intensity. Isotropic displacement parameters summarize a limited model; anisotropic motion requires a tensor and can correlate with occupancy in refinement. A measured broad diffuse halo may reflect amorphous content or disorder rather than a complete absence of local atomic organization.


### 2. What to measure and what it means

Generate intensity curves with illustrative exp(−B sin²θ/λ²) dependence and compare moderate and large angles. Assess which intensity ratios would be sensitive to displacement parameters if the incident flux and scattering factors were otherwise controlled.



### 3. Interpretation, alternative explanations and boundaries

A strong high-angle intensity decay is compatible with increased disorder but is not unique evidence of higher temperature. Absorption and instrumental sensitivity can also change angular profiles.


One competing explanation to test here is **diffuse scattering background**. This is not a guaranteed cause, but it deserves a clear discrimination experiment. Decide whether a changed scan range, an independent standard, a different specimen orientation or a second probe would expose that alternative. Also ask whether the proposed test changes one parameter at a time. An experiment that simultaneously changes wavelength, mounting and background correction may produce a new curve without clarifying why it changed.

### 4. Fully specified synthetic calculation

The linked model is **First-order Bragg peak 2θ**. Its one-variable input is **plane spacing d** (nm), the selected demonstration value is **0.34**, and the computed value is **26.1891 degrees**. The exact model expression is `2*Math.asin(0.15406/(2*d))*180/Math.PI` using the variable shown; this is intentionally a classroom-level forward relationship. Model assumptions: Monochromatic λ=0.15406 nm; first order; sample displacement ignored.


| Input (nm) | Predicted degrees | Interpretation |
|---:|---:|---|
| 0.185 | 49.2123 | Low-side comparison under fixed assumptions |
| 0.24 | 37.4418 | Reference setting for sensitivity |
| 0.32 | 27.8579 | High-side comparison under fixed assumptions |


### 5. Data collection and reproducibility protocol



### 6. Diagnostic failure mode

Interpreting a single fitted B as a precise atomic displacement requires careful convention, resolution and refinement correlations.




### 7. Knowledge-check and discussion questions

- **Explain:** What is the physical distinction between the quantity named in **Debye-Waller disorder and diffuse scattering** and the observable used to estimate it? Give one explicit assumption.
- **Calculate:** Reproduce case MSE-C15 and evaluate how the output changes when the slider parameter moves from 0.185 to 0.32 nm.
- **Challenge:** Could **diffuse scattering background** explain the observed feature? State a discriminating control rather than merely saying that more data are required.



## Explore two independent interactive model families

<!-- MODEL_4 -->

<!-- MODEL_5 -->

## Integrated investigation: Systematic absences with misleading intensities

### Evidence brief

An indexed powder set shows strong 110 and 200 lines but an almost undetectable 100. A quick note labels the material BCC without considering the detection threshold or whether the chemical basis is identical at the centered sites.



### Proposed analysis

Calculate the two-site structure factor for even and odd h+k+l; vary the second-site scattering strength in the interactive model. Compare predicted intensity ratios with a simulated measured detection threshold and background variance. List alternative mechanisms: preferred orientation, elemental ordering or a different extinction mechanism.



### Evaluation of the competing explanations

The h+k+l rule follows from a specific centering symmetry and should be corroborated over multiple reflections. If nominally forbidden peaks appear reproducibly, test contamination, multiple scattering, symmetry breaking or wrong indexing.



### Limitations and ethical interpretation

The amplitude proxy is deliberately simplistic. It is not a substitute for angle-dependent atomic form factors, absorption corrections or full refinement.



### Assessment rubric





## Unit research commentary — evidence across scales

Coherent-scattering predictions make an ideal controlled contrast between geometric and chemical information. Fix two scattering centers in a nominal BCC-like arrangement and use complex phases to sum amplitudes for several reflection families. When the same scattering factor is assigned to both sites, odd h+k+l reflections cancel in the model. Change the hypothetical scattering contrast and observe that the cancellation may disappear when the underlying assumption of full translation equivalence is broken. This teaches an important constraint: selection rules are attached to the symmetry of the entire scattering-density motif, not simply to where two points appear in a sketch.

Now separate structure-factor magnitude from detector counts. A detector captures intensity after the structure factor has been multiplied or modified by multiplicity, illumination, polarization, absorption and instrument response. Even perfect mathematical agreement with an idealized structure factor does not guarantee a matching raw peak-height ratio. A physically motivated test compares integrated intensities after appropriate corrections, using a consistent geometry and uncertainty model. Relative high-angle intensity loss may indicate thermal or static disorder, but without controls it could also reflect detector sensitivity or angular absorption effects.

A research group may be tempted to interpret one weak reflection as an exact symmetry extinction. Write a response stating what detection threshold would have been necessary to support that conclusion. Then select at least two other predicted absent and present reflection families for verification. Include a scenario where a weak contaminant peak overlaps the forbidden position. The desired conclusion should identify whether the observation is compatible with a candidate structure, whether competing motifs remain possible, and which independent chemical or structural measurement would most efficiently narrow them. Numerical phase cancellation is a powerful lesson, but a real structure solution requires a coherent set of reflections, a defined beam contrast and a physically supported structural model.

### End-of-unit examiner challenge: Wave scattering and structure factors

Write an evidence-based defense of **whether predicted extinctions agree with detected and nondetected reflections**. Begin by defining how **coherent scattering amplitude and detector intensity** would be measured and listing the necessary independent controls for **wavelength; scattering angle; atomic basis; reflection family**. Then name a physically distinct mechanism that could imitate the preferred explanation: **mistaking a weak or masked line for an exact symmetry extinction**. The response must show why that mechanism is plausible, rather than merely listing it as a caveat. Select one follow-up measurement that makes different predictions for the rival models; state what a negative result would mean. Finally prepare an annotated calculation from the two teaching formulas associated with this unit and explain why exact numerical agreement with a forward equation does not validate the specimen interpretation. Include an uncertainty estimate and say whether the proposed material conclusion is supported, conditional or unresolved. This is a reasoning task using synthetic evidence, not an authorization to operate an instrument.
