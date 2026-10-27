# Unit 8: Advanced probes, analysis integrity and applications

**Guiding question:** How should diffraction evidence enter engineering decisions, open datasets and reproducible research?

This unit connects integrated experimental design to an observable experiment. Every example is fictional and intentionally simplified. The sequence is designed so that the first two lessons provide definitions, the middle lessons test consequences, and the fifth lesson confronts ambiguity. Read plots as conditional calculations rather than laboratory observations.

## Investigation framework: Integrated experimental design





### Unit-wide reasoning objective




## Lesson 8.1 — Neutron and synchrotron diffraction

### 1. Physical picture and mathematical meaning

Neutrons interact with atomic nuclei and, when relevant, magnetic moments; X-rays primarily interact with electrons. Synchrotron X-rays provide intense, tunable radiation and often enable time-resolved or high-energy measurements. Probe selection depends on penetration depth, isotope contrast, sample environment, flux and instrument availability. Neither method automatically outperforms laboratory X-ray diffraction for every material problem.


### 2. What to measure and what it means

Compare the information required to locate a light-element sublattice against that needed for rapid routine screening. Build a decision matrix for resolution, sample volume, contrast, access time and sample damage. Explicitly separate scattering physics from logistics.


Consider the targeted decision **whether another researcher can reconstruct every inferential step**. Specify one null hypothesis that competes with the preferred explanation and design a control that could falsify it. Make a small table of predicted features for both interpretations before inspecting any synthetic data. Such predeclared contrasts reduce the temptation to keep only peaks that favor the desired material narrative. Calibration, specimen preparation and the physics of scattering should be assessed before microstructure claims are written.

### 3. Interpretation, alternative explanations and boundaries

Complementary probes resolve correlated structural parameters by measuring different contrasts, but datasets must be co-registered to sample state and temperature.


One competing explanation to test here is **probe penetration mismatch**. This is not a guaranteed cause, but it deserves a clear discrimination experiment. Decide whether a changed scan range, an independent standard, a different specimen orientation or a second probe would expose that alternative. Also ask whether the proposed test changes one parameter at a time. An experiment that simultaneously changes wavelength, mounting and background correction may produce a new curve without clarifying why it changed.

### 4. Fully specified synthetic calculation

The linked model is **Thermal neutron wavelength**. Its one-variable input is **neutron speed** (m/s), the selected demonstration value is **1350**, and the computed value is **2.9304 Å**. The exact model expression is `(6.62607015e-34/(1.67492749804e-27*v))*1e10` using the variable shown; this is intentionally a classroom-level forward relationship. Model assumptions: Nonrelativistic free neutron; ignores neutron energy distribution and instrument timing.


| Input (m/s) | Predicted Å | Interpretation |
|---:|---:|---|
| 1550 | 2.55228 | Low-side comparison under fixed assumptions |
| 2200 | 1.7982 | Reference setting for sensitivity |
| 2850 | 1.38808 | High-side comparison under fixed assumptions |


### 5. Data collection and reproducibility protocol

Design a comparison that measures **complementary probe contrast and machine-readable record** while holding specimen state and geometry as steady as possible. Record **beam identity; wavelength; sample state; instrument geometry**. Repeat an independent reference and state what result would support **whether another researcher can reconstruct every inferential step**. Record the decision rule before looking at a fitted pattern.

### 6. Diagnostic failure mode

Avoid treating any technique as an unconditional ground truth; each measurement has its own forward model and corrections.

In the current unit, a particularly relevant practical trap is **equating validation of a file format with validation of the physical result**. An analyst who ignores it can obtain a mathematically self-consistent answer from the wrong inputs. Diagnose the trap by returning to an invariant: a reference specimen, multiple indexed reflections, a repeated geometry, a known scattering convention or an independent probe. If the disagreement persists, report it as an unresolved limitation. Do not change a correction parameter solely to force a desirable phase or property estimate.


### 7. Knowledge-check and discussion questions

- **Explain:** What is the physical distinction between the quantity named in **Neutron and synchrotron diffraction** and the observable used to estimate it? Give one explicit assumption.
- **Calculate:** Reproduce case MSE-C36 and evaluate how the output changes when the slider parameter moves from 1550 to 2850 m/s.
- **Challenge:** Could **probe penetration mismatch** explain the observed feature? State a discriminating control rather than merely saying that more data are required.



## Lesson 8.2 — Electron diffraction and dynamical effects

### 1. Physical picture and mathematical meaning

High-energy electrons have short de Broglie wavelengths and interact strongly with matter, enabling nanoscale selected-area diffraction. Multiple scattering may be significant, especially in thicker crystalline specimens, so kinematic intensity interpretation can fail. Camera length calibration and zone-axis indexing constrain spot positions. Diffraction contrast in electron microscopy also depends on bending and thickness.


### 2. What to measure and what it means

Estimate an electron wavelength under an explicitly nonrelativistic teaching approximation and note when a relativistic expression is needed. Simulate spot spacing changes after camera calibration and check the specimen thickness assumption for a proposed intensity analysis.



### 3. Interpretation, alternative explanations and boundaries

Electron diffraction provides local crystallographic information inaccessible to bulk powder measurements, but indexing a spot pattern alone does not reveal all site occupancies.


One competing explanation to test here is **neutron isotope contrast**. This is not a guaranteed cause, but it deserves a clear discrimination experiment. Decide whether a changed scan range, an independent standard, a different specimen orientation or a second probe would expose that alternative. Also ask whether the proposed test changes one parameter at a time. An experiment that simultaneously changes wavelength, mounting and background correction may produce a new curve without clarifying why it changed.

### 4. Fully specified synthetic calculation

The linked model is **Debye-Waller relative attenuation**. Its one-variable input is **isotropic B** (Å²), the selected demonstration value is **1.3**, and the computed value is **0.760274 intensity ratio**. The exact model expression is `Math.exp(-2*B*Math.pow(Math.sin(30*Math.PI/180)/1.54,2))` using the variable shown; this is intentionally a classroom-level forward relationship. Model assumptions: Isotropic convention I/I0=exp[-2B(sinθ/λ)²], λ=1.54 Å and θ=30°.


| Input (Å²) | Predicted intensity ratio | Interpretation |
|---:|---:|---|
| 0.5 | 0.899952 | Low-side comparison under fixed assumptions |
| 1 | 0.809913 | Reference setting for sensitivity |
| 2.5 | 0.590332 | High-side comparison under fixed assumptions |


### 5. Data collection and reproducibility protocol



### 6. Diagnostic failure mode

Do not quantitatively refine thick-crystal electron spot intensities using an uncorrected single-scattering approximation.




### 7. Knowledge-check and discussion questions

- **Explain:** What is the physical distinction between the quantity named in **Electron diffraction and dynamical effects** and the observable used to estimate it? Give one explicit assumption.
- **Calculate:** Reproduce case MSE-C37 and evaluate how the output changes when the slider parameter moves from 0.5 to 2.5 Å².
- **Challenge:** Could **neutron isotope contrast** explain the observed feature? State a discriminating control rather than merely saying that more data are required.



## Lesson 8.3 — Total scattering and pair distribution functions

### 1. Physical picture and mathematical meaning

Conventional Bragg diffraction emphasizes long-range periodicity, whereas total scattering measures both Bragg and diffuse components. Fourier transformation of corrected scattering data yields a pair distribution function that constrains local interatomic distances. Finite maximum scattering-vector range and imperfect background normalization generate artifacts. Amorphous and nanoscale structures can show local peaks without sharp Bragg order.


### 2. What to measure and what it means

Use an illustrative finite Q range to estimate approximate real-space resolution and discuss oscillatory termination artifacts. Compare two models with equal first-neighbor distances but different medium-range order and determine which measurements could separate them.



### 3. Interpretation, alternative explanations and boundaries

A real-space peak should be assigned only within measurement resolution and an appropriate scattering-weighted model.


One competing explanation to test here is **dynamical electron scattering**. This is not a guaranteed cause, but it deserves a clear discrimination experiment. Decide whether a changed scan range, an independent standard, a different specimen orientation or a second probe would expose that alternative. Also ask whether the proposed test changes one parameter at a time. An experiment that simultaneously changes wavelength, mounting and background correction may produce a new curve without clarifying why it changed.

### 4. Fully specified synthetic calculation

The linked model is **Thermal neutron wavelength**. Its one-variable input is **neutron speed** (m/s), the selected demonstration value is **2100**, and the computed value is **1.88383 Å**. The exact model expression is `(6.62607015e-34/(1.67492749804e-27*v))*1e10` using the variable shown; this is intentionally a classroom-level forward relationship. Model assumptions: Nonrelativistic free neutron; ignores neutron energy distribution and instrument timing.


| Input (m/s) | Predicted Å | Interpretation |
|---:|---:|---|
| 1550 | 2.55228 | Low-side comparison under fixed assumptions |
| 2200 | 1.7982 | Reference setting for sensitivity |
| 2850 | 1.38808 | High-side comparison under fixed assumptions |


### 5. Data collection and reproducibility protocol



### 6. Diagnostic failure mode

Do not confuse a pair distribution function with a simple histogram of photographed atomic separations.




### 7. Knowledge-check and discussion questions

- **Explain:** What is the physical distinction between the quantity named in **Total scattering and pair distribution functions** and the observable used to estimate it? Give one explicit assumption.
- **Calculate:** Reproduce case MSE-C38 and evaluate how the output changes when the slider parameter moves from 1550 to 2850 m/s.
- **Challenge:** Could **dynamical electron scattering** explain the observed feature? State a discriminating control rather than merely saying that more data are required.



## Lesson 8.4 — CIF files and reproducible crystallographic data

### 1. Physical picture and mathematical meaning

The IUCr Crystallographic Information Framework provides controlled, machine-readable data dictionaries and validation conventions. A shareable crystallographic report should connect cell parameters, symmetry, atomic positions, occupancies, displacement parameters, measurement conditions and refinement quality. A CIF file is a structured report, not an automatic guarantee that the refined structure is correct.


### 2. What to measure and what it means

Create an intentionally minimal teaching CIF-like checklist and identify which required data fields depend on method and structure type. Track provenance from raw detector frames through integration, scaling, indexing, refinement and validation. Preserve software versions and processing parameters.



### 3. Interpretation, alternative explanations and boundaries

Machine-readable exchange reduces ambiguity and enables secondary analysis when raw data, units and parameter uncertainty are preserved.


One competing explanation to test here is **transformation truncation effects**. This is not a guaranteed cause, but it deserves a clear discrimination experiment. Decide whether a changed scan range, an independent standard, a different specimen orientation or a second probe would expose that alternative. Also ask whether the proposed test changes one parameter at a time. An experiment that simultaneously changes wavelength, mounting and background correction may produce a new curve without clarifying why it changed.

### 4. Fully specified synthetic calculation

The linked model is **Debye-Waller relative attenuation**. Its one-variable input is **isotropic B** (Å²), the selected demonstration value is **2.5**, and the computed value is **0.590332 intensity ratio**. The exact model expression is `Math.exp(-2*B*Math.pow(Math.sin(30*Math.PI/180)/1.54,2))` using the variable shown; this is intentionally a classroom-level forward relationship. Model assumptions: Isotropic convention I/I0=exp[-2B(sinθ/λ)²], λ=1.54 Å and θ=30°.


| Input (Å²) | Predicted intensity ratio | Interpretation |
|---:|---:|---|
| 0.5 | 0.899952 | Low-side comparison under fixed assumptions |
| 1 | 0.809913 | Reference setting for sensitivity |
| 2.5 | 0.590332 | High-side comparison under fixed assumptions |


### 5. Data collection and reproducibility protocol



### 6. Diagnostic failure mode

Do not publish private sample identifiers or confidential experimental metadata through an open archive without authorization.




### 7. Knowledge-check and discussion questions

- **Explain:** What is the physical distinction between the quantity named in **CIF files and reproducible crystallographic data** and the observable used to estimate it? Give one explicit assumption.
- **Calculate:** Reproduce case MSE-C39 and evaluate how the output changes when the slider parameter moves from 0.5 to 2.5 Å².
- **Challenge:** Could **transformation truncation effects** explain the observed feature? State a discriminating control rather than merely saying that more data are required.



## Lesson 8.5 — Case-study synthesis and engineering judgment

### 1. Physical picture and mathematical meaning

The final interpretation of diffraction must answer a materials question: which phase formed, which crystal directions are aligned, how much strain exists, or whether a microstructure changed after processing. Each question requires different constraints and validation. Diffraction alone may be sufficient for a narrow metric claim but not for functional safety, chemical composition or service lifetime.


### 2. What to measure and what it means

Prepare a miniature investigation comparing two synthetic heat-treatment states, including expected peak locations, texture observations, corrected breadths and a complementary hardness measurement. Write a decision memo separating direct observations, model-derived quantities and unresolved alternatives.



### 3. Interpretation, alternative explanations and boundaries

A useful result makes clear what was actually measured, what is inferred by a specific model and what remains unknown.


One competing explanation to test here is **missing provenance metadata**. This is not a guaranteed cause, but it deserves a clear discrimination experiment. Decide whether a changed scan range, an independent standard, a different specimen orientation or a second probe would expose that alternative. Also ask whether the proposed test changes one parameter at a time. An experiment that simultaneously changes wavelength, mounting and background correction may produce a new curve without clarifying why it changed.

### 4. Fully specified synthetic calculation

The linked model is **Thermal neutron wavelength**. Its one-variable input is **neutron speed** (m/s), the selected demonstration value is **2900**, and the computed value is **1.36415 Å**. The exact model expression is `(6.62607015e-34/(1.67492749804e-27*v))*1e10` using the variable shown; this is intentionally a classroom-level forward relationship. Model assumptions: Nonrelativistic free neutron; ignores neutron energy distribution and instrument timing.


| Input (m/s) | Predicted Å | Interpretation |
|---:|---:|---|
| 1550 | 2.55228 | Low-side comparison under fixed assumptions |
| 2200 | 1.7982 | Reference setting for sensitivity |
| 2850 | 1.38808 | High-side comparison under fixed assumptions |


### 5. Data collection and reproducibility protocol



### 6. Diagnostic failure mode

Avoid conclusions about component safety or commercial quality based only on attractive diffraction plots.




### 7. Knowledge-check and discussion questions

- **Explain:** What is the physical distinction between the quantity named in **Case-study synthesis and engineering judgment** and the observable used to estimate it? Give one explicit assumption.
- **Calculate:** Reproduce case MSE-C40 and evaluate how the output changes when the slider parameter moves from 1550 to 2850 m/s.
- **Challenge:** Could **missing provenance metadata** explain the observed feature? State a discriminating control rather than merely saying that more data are required.



## Explore two independent interactive model families

<!-- MODEL_14 -->

<!-- MODEL_15 -->

## Integrated investigation: Open diffraction dataset and decision memo

### Evidence brief

A team wants to publish a diffraction-supported heat-treatment claim with insufficient metadata: the raw frames have no wavelength record, the sample IDs changed and the plotted peak position lacks angular calibration.



### Proposed analysis

Draft a provenance graph connecting specimen batch, processing treatment, raw frames, sample geometry, wavelength, instrument standard, peak fitting code, structural model and exported CIF. Mark mandatory versus optional fields for the actual method and assign a versioned analysis identifier.



### Evaluation of the competing explanations

Reproducibility improves when independent readers can reconstruct the same pattern and see where assumptions entered. Absence of required metadata may make even a polished plot uninterpretable.



### Limitations and ethical interpretation

CIF validation checks structure and consistency; it cannot prove that a sample was represented, honestly measured or appropriate for its intended application.



### Assessment rubric





## Unit research commentary — evidence across scales

Advanced diffraction begins by selecting the probe for the information gap. Conventional X-rays are sensitive to electron distribution, while nuclear neutron scattering lengths depend on isotope and may offer a different kind of elemental contrast. Magnetic neutron diffraction can reveal magnetic arrangements when the measurement conditions and model support that purpose. High-energy electron diffraction provides tiny-area structural information, but multiple scattering can undermine a simple kinematic intensity interpretation in thick crystalline specimens. A suitable experiment therefore follows from the target parameter and the specimen constraints, not from the prestige of an instrument.

Local disorder presents a related modeling choice. Broad total scattering contains information beyond sharply indexed Bragg peaks, but recovering a pair distribution function requires corrections and a finite reciprocal-space window. A local-neighbor peak does not uniquely identify one crystal structure, and oscillatory artifacts from a truncated transform can resemble additional correlations. The analyst must track the measured Q range, subtraction procedures, scattering weights and real-space resolution. Comparing an ordered and disordered model should emphasize features that are predicted independently of the adjustable normalization.

The final exercise focuses on an open report. Invent a traceable set of file names linking an actual specimen identifier, raw detector frames, calibration reference, indexing output, fitted peak table, structure model and final CIF. Indicate exactly which metadata are observed, user-entered or software-derived. Ask another student to reproduce one result without oral explanations; every missing wavelength, axis convention and specimen state should appear as a reproducibility defect. The IUCr framework helps standardize structure information, but checking a CIF cannot establish sample authenticity or scientific correctness. The strongest final deliverable is a modest claim whose numerical steps can be rebuilt, whose physical limits are explicit, and whose remaining uncertainty informs the next experiment.

### End-of-unit examiner challenge: Advanced probes, analysis integrity and applications

Write an evidence-based defense of **whether another researcher can reconstruct every inferential step**. Begin by defining how **complementary probe contrast and machine-readable record** would be measured and listing the necessary independent controls for **beam identity; wavelength; sample state; instrument geometry**. Then name a physically distinct mechanism that could imitate the preferred explanation: **equating validation of a file format with validation of the physical result**. The response must show why that mechanism is plausible, rather than merely listing it as a caveat. Select one follow-up measurement that makes different predictions for the rival models; state what a negative result would mean. Finally prepare an annotated calculation from the two teaching formulas associated with this unit and explain why exact numerical agreement with a forward equation does not validate the specimen interpretation. Include an uncertainty estimate and say whether the proposed material conclusion is supported, conditional or unresolved. This is a reasoning task using synthetic evidence, not an authorization to operate an instrument.
