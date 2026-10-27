# Unit 1: Lattices, cells, and symmetry

**Guiding question:** How do we specify periodic order without confusing a mathematical lattice with an actual arrangement of atoms?

This unit connects cell geometry and symmetry to an observable experiment. Every example is fictional and intentionally simplified. The sequence is designed so that the first two lessons provide definitions, the middle lessons test consequences, and the fifth lesson confronts ambiguity. Read plots as conditional calculations rather than laboratory observations.

## Investigation framework: Cell geometry and symmetry

The practical challenge is not merely to manipulate symbols. A dataset enters analysis through a chain that includes specimen history, geometry, instrument settings, forward physics and an interpretation rule. A useful inference must survive more than one observation, especially when two physical mechanisms produce nearly the same result. For this unit, write down the object that is repeated or transformed, decide what the instrument actually detects, and list the necessary assumptions before assigning any crystal property.

A minimal lab notebook should separate **specimen description**, **known settings**, **raw observations**, **derived quantities**, and **claims requiring a model**. Those columns prevent a common mistake in diffraction studies: treating a plausible lattice assignment as if it had been read directly from a detector. Use the numerical models to ask what changes when a parameter moves across its permitted range and what measurements remain invariant. Measurements and synthetic predictions should never be merged into the same column without an explicit flag.

### Unit-wide reasoning objective

Begin with a competing-model question: what different cause could produce the same observed pattern? Select an additional reflection, calibration scan or complementary measurement that would discriminate those causes. A strong argument predicts not just a feature that agrees with the preferred explanation, but at least one feature that would expose a wrong explanation. Prefer controlled falsification to catalog-score maximization. All results in this book remain classroom exercises; an industrial acceptance rule must be independently documented and verified.


## Lesson 1.1 — Lattice versus basis

### 1. Physical picture and mathematical meaning

A lattice is a set of equivalent translational points; a crystal structure attaches an atom or a group of atoms to each such point. Two structures can therefore share a Bravais lattice yet have different chemistry and scattering intensities. A conventional cell is often selected to expose symmetry even when a smaller primitive cell exists. Periodicity can be represented with three independent translation vectors, while local coordination depends on the basis.


### 2. What to measure and what it means

Build a planar point lattice and add two differently colored basis markers. Translate by whole lattice vectors and compare the entire repeated motif. Then change a basis coordinate without changing any translation vector; the diffraction selection rules can change despite the unchanged lattice.


Consider the targeted decision **whether a physically equivalent cell description changes any measurable quantity**. Specify one null hypothesis that competes with the preferred explanation and design a control that could falsify it. Make a small table of predicted features for both interpretations before inspecting any synthetic data. Such predeclared contrasts reduce the temptation to keep only peaks that favor the desired material narrative. Calibration, specimen preparation and the physics of scattering should be assessed before microstructure claims are written.

### 3. Interpretation, alternative explanations and boundaries

An observed pattern cannot uniquely identify chemical occupancy from peak positions alone. Peak positions encode metric periodicity; intensities incorporate basis, scattering factors, disorder and experimental corrections.


One competing explanation to test here is **different origin choices**. This is not a guaranteed cause, but it deserves a clear discrimination experiment. Decide whether a changed scan range, an independent standard, a different specimen orientation or a second probe would expose that alternative. Also ask whether the proposed test changes one parameter at a time. An experiment that simultaneously changes wavelength, mounting and background correction may produce a new curve without clarifying why it changed.

### 4. Fully specified synthetic calculation

The linked model is **Cubic cell volume**. Its one-variable input is **cell edge a** (nm), the selected demonstration value is **0.35**, and the computed value is **0.042875 nm³**. The exact model expression is `a*a*a` using the variable shown; this is intentionally a classroom-level forward relationship. Model assumptions: Cubic geometry only; no thermal expansion.


| Input (nm) | Predicted nm³ | Interpretation |
|---:|---:|---|
| 0.32 | 0.032768 | Low-side comparison under fixed assumptions |
| 0.4 | 0.064 | Reference setting for sensitivity |
| 0.62 | 0.238328 | High-side comparison under fixed assumptions |


### 5. Data collection and reproducibility protocol

Design a comparison that measures **integer lattice point accounting** while holding specimen state and geometry as steady as possible. Record **cell length; site occupancy; chosen setting**. Repeat an independent reference and state what result would support **whether a physically equivalent cell description changes any measurable quantity**. Record the decision rule before looking at a fitted pattern.

### 6. Diagnostic failure mode

A decorative repeating drawing is not a proof that a three-dimensional lattice has been correctly identified.

In the current unit, a particularly relevant practical trap is **a mismatched atom count or incorrect assignment of a centering operation**. An analyst who ignores it can obtain a mathematically self-consistent answer from the wrong inputs. Diagnose the trap by returning to an invariant: a reference specimen, multiple indexed reflections, a repeated geometry, a known scattering convention or an independent probe. If the disagreement persists, report it as an unresolved limitation. Do not change a correction parameter solely to force a desirable phase or property estimate.


### 7. Knowledge-check and discussion questions

- **Explain:** What is the physical distinction between the quantity named in **Lattice versus basis** and the observable used to estimate it? Give one explicit assumption.
- **Calculate:** Reproduce case MSE-C01 and evaluate how the output changes when the slider parameter moves from 0.32 to 0.62 nm.
- **Challenge:** Could **different origin choices** explain the observed feature? State a discriminating control rather than merely saying that more data are required.



## Lesson 1.2 — Primitive and conventional unit cells

### 1. Physical picture and mathematical meaning

A primitive unit cell contains exactly one lattice point when fractional boundary contributions are counted. Conventional cells may include several lattice points because centering makes crystal symmetry visually simpler. For a cubic face-centered lattice, eight corners contribute one lattice point and six faces contribute three, producing four lattice points per conventional cell. For a body-centered cube, the corners plus the body center produce two.


### 2. What to measure and what it means

Compare a parallelepiped primitive construction with a conventional centered cell. Account for corner, face, edge and interior contributions using their sharing fractions. Check that volume multiplied by lattice point density gives one for any primitive cell.



### 3. Interpretation, alternative explanations and boundaries

Different cell settings may describe the same underlying crystal. Report the selected setting, units, fractional basis coordinates and symmetry conventions so another analyst can reproduce the indexing.


One competing explanation to test here is **non-primitive basis**. This is not a guaranteed cause, but it deserves a clear discrimination experiment. Decide whether a changed scan range, an independent standard, a different specimen orientation or a second probe would expose that alternative. Also ask whether the proposed test changes one parameter at a time. An experiment that simultaneously changes wavelength, mounting and background correction may produce a new curve without clarifying why it changed.

### 4. Fully specified synthetic calculation

The linked model is **Monatomic FCC theoretical density**. Its one-variable input is **cell edge a** (nm), the selected demonstration value is **0.38**, and the computed value is **3.26607 g/cm³**. The exact model expression is `4*26.9815385/(6.02214076e23*Math.pow(a*1e-7,3))` using the variable shown; this is intentionally a classroom-level forward relationship. Model assumptions: Al-like molar mass and 4 atoms per FCC conventional cell; excludes vacancies.


| Input (nm) | Predicted g/cm³ | Interpretation |
|---:|---:|---|
| 0.365 | 3.68551 | Low-side comparison under fixed assumptions |
| 0.405 | 2.69781 | Reference setting for sensitivity |
| 0.45 | 1.9667 | High-side comparison under fixed assumptions |


### 5. Data collection and reproducibility protocol



### 6. Diagnostic failure mode

Do not call every atom a lattice point: a basis can contain multiple atoms, vacancies, or occupancy fractions.




### 7. Knowledge-check and discussion questions

- **Explain:** What is the physical distinction between the quantity named in **Primitive and conventional unit cells** and the observable used to estimate it? Give one explicit assumption.
- **Calculate:** Reproduce case MSE-C02 and evaluate how the output changes when the slider parameter moves from 0.365 to 0.45 nm.
- **Challenge:** Could **non-primitive basis** explain the observed feature? State a discriminating control rather than merely saying that more data are required.



## Lesson 1.3 — The seven crystal systems

### 1. Physical picture and mathematical meaning

Crystal systems group crystallographic point-group symmetries, and their conventional cell metric restrictions depend on the system. Cubic cells have equal edges and right angles; tetragonal cells have two equal edges; orthorhombic cells have three mutually perpendicular but generally unequal edges. Monoclinic cells have one non-right conventional angle, while triclinic structures impose no fixed right-angle conditions. Hexagonal, trigonal and rhombohedral settings require careful distinction.


### 2. What to measure and what it means

Inspect simulated diffraction metric fits obtained under cubic, tetragonal and orthorhombic assumptions. Note how a small departure from cubic symmetry may split formerly degenerate reflections. Test whether peak widths and resolution support the more complex model.



### 3. Interpretation, alternative explanations and boundaries

The choice of metric symmetry is a model-comparison exercise constrained by uncertainty. A lattice with nearly equal edges is not automatically cubic if intensity symmetry and peak splitting contradict that interpretation.


One competing explanation to test here is **vacancy occupancy**. This is not a guaranteed cause, but it deserves a clear discrimination experiment. Decide whether a changed scan range, an independent standard, a different specimen orientation or a second probe would expose that alternative. Also ask whether the proposed test changes one parameter at a time. An experiment that simultaneously changes wavelength, mounting and background correction may produce a new curve without clarifying why it changed.

### 4. Fully specified synthetic calculation

The linked model is **Cubic cell volume**. Its one-variable input is **cell edge a** (nm), the selected demonstration value is **0.53**, and the computed value is **0.148877 nm³**. The exact model expression is `a*a*a` using the variable shown; this is intentionally a classroom-level forward relationship. Model assumptions: Cubic geometry only; no thermal expansion.


| Input (nm) | Predicted nm³ | Interpretation |
|---:|---:|---|
| 0.32 | 0.032768 | Low-side comparison under fixed assumptions |
| 0.4 | 0.064 | Reference setting for sensitivity |
| 0.62 | 0.238328 | High-side comparison under fixed assumptions |


### 5. Data collection and reproducibility protocol



### 6. Diagnostic failure mode

A numerical fit with more free lattice parameters nearly always fits better; that alone is insufficient evidence for lower symmetry.




### 7. Knowledge-check and discussion questions

- **Explain:** What is the physical distinction between the quantity named in **The seven crystal systems** and the observable used to estimate it? Give one explicit assumption.
- **Calculate:** Reproduce case MSE-C03 and evaluate how the output changes when the slider parameter moves from 0.32 to 0.62 nm.
- **Challenge:** Could **vacancy occupancy** explain the observed feature? State a discriminating control rather than merely saying that more data are required.



## Lesson 1.4 — Point symmetry and site symmetry

### 1. Physical picture and mathematical meaning

Rotation, reflection, inversion and rotoinversion operations define crystallographic point symmetry. Only rotational orders compatible with ordinary periodic lattices appear as crystallographic lattice rotations; fivefold symmetry instead suggests different symmetry categories, including quasiperiodic materials. The local point symmetry of an atomic site can be higher than that of a generic position. Symmetry reduces independent atomic coordinates and constrains observable tensors.


### 2. What to measure and what it means

Apply a fourfold rotation to a set of fractional coordinates and observe which positions remain equivalent. Compare transformation of a displacement vector with transformation of a scalar occupancy. Use a second operation to test whether the assumed set of operations closes consistently.



### 3. Interpretation, alternative explanations and boundaries

Material anisotropy, optical behavior and systematic degeneracies should be interpreted together with point symmetry rather than inferred from a single polished crystal face.


One competing explanation to test here is **an alternate conventional setting**. This is not a guaranteed cause, but it deserves a clear discrimination experiment. Decide whether a changed scan range, an independent standard, a different specimen orientation or a second probe would expose that alternative. Also ask whether the proposed test changes one parameter at a time. An experiment that simultaneously changes wavelength, mounting and background correction may produce a new curve without clarifying why it changed.

### 4. Fully specified synthetic calculation

The linked model is **Monatomic FCC theoretical density**. Its one-variable input is **cell edge a** (nm), the selected demonstration value is **0.43**, and the computed value is **2.25409 g/cm³**. The exact model expression is `4*26.9815385/(6.02214076e23*Math.pow(a*1e-7,3))` using the variable shown; this is intentionally a classroom-level forward relationship. Model assumptions: Al-like molar mass and 4 atoms per FCC conventional cell; excludes vacancies.


| Input (nm) | Predicted g/cm³ | Interpretation |
|---:|---:|---|
| 0.365 | 3.68551 | Low-side comparison under fixed assumptions |
| 0.405 | 2.69781 | Reference setting for sensitivity |
| 0.45 | 1.9667 | High-side comparison under fixed assumptions |


### 5. Data collection and reproducibility protocol



### 6. Diagnostic failure mode

Do not use molecular symmetry labels as substitutes for crystallographic space-group information.




### 7. Knowledge-check and discussion questions

- **Explain:** What is the physical distinction between the quantity named in **Point symmetry and site symmetry** and the observable used to estimate it? Give one explicit assumption.
- **Calculate:** Reproduce case MSE-C04 and evaluate how the output changes when the slider parameter moves from 0.365 to 0.45 nm.
- **Challenge:** Could **an alternate conventional setting** explain the observed feature? State a discriminating control rather than merely saying that more data are required.



## Lesson 1.5 — Space groups, origins, and settings

### 1. Physical picture and mathematical meaning

Space-group operations include translations and may contain screws and glides that combine point operations with fractional translations. An origin shift can alter listed coordinates while leaving the physical crystal unchanged. Standard settings facilitate comparison and database exchange, yet some materials are reported in nonstandard cells for physical reasons. A complete structure description needs lattice, symmetry operators, atomic fractional positions and occupancies.


### 2. What to measure and what it means

Start from a small fractional-coordinate list and generate symmetry-equivalent positions under selected operations. Wrap coordinates back into the interval zero to one and remove equivalent duplicates within tolerance. Document which origin and axis convention were used.



### 3. Interpretation, alternative explanations and boundaries

Space-group candidates are constrained by extinction patterns and observed intensity symmetry, but ambiguous powder data frequently leave alternatives. Later chemical plausibility and refinement are part of the evidence.


One competing explanation to test here is **a pseudo-symmetry assignment**. This is not a guaranteed cause, but it deserves a clear discrimination experiment. Decide whether a changed scan range, an independent standard, a different specimen orientation or a second probe would expose that alternative. Also ask whether the proposed test changes one parameter at a time. An experiment that simultaneously changes wavelength, mounting and background correction may produce a new curve without clarifying why it changed.

### 4. Fully specified synthetic calculation

The linked model is **Cubic cell volume**. Its one-variable input is **cell edge a** (nm), the selected demonstration value is **0.71**, and the computed value is **0.357911 nm³**. The exact model expression is `a*a*a` using the variable shown; this is intentionally a classroom-level forward relationship. Model assumptions: Cubic geometry only; no thermal expansion.


| Input (nm) | Predicted nm³ | Interpretation |
|---:|---:|---|
| 0.32 | 0.032768 | Low-side comparison under fixed assumptions |
| 0.4 | 0.064 | Reference setting for sensitivity |
| 0.62 | 0.238328 | High-side comparison under fixed assumptions |


### 5. Data collection and reproducibility protocol



### 6. Diagnostic failure mode

Never infer a definitive space group from one absent peak; overlap, preferred orientation or poor signal may hide a reflection.




### 7. Knowledge-check and discussion questions

- **Explain:** What is the physical distinction between the quantity named in **Space groups, origins, and settings** and the observable used to estimate it? Give one explicit assumption.
- **Calculate:** Reproduce case MSE-C05 and evaluate how the output changes when the slider parameter moves from 0.32 to 0.62 nm.
- **Challenge:** Could **a pseudo-symmetry assignment** explain the observed feature? State a discriminating control rather than merely saying that more data are required.



## Explore two independent interactive model families

<!-- MODEL_0 -->

<!-- MODEL_1 -->

## Integrated investigation: Cell indexing under a symmetry trap

### Evidence brief

A manufacturing team reports a phase transition after a batch furnace adjustment because one cubic peak seems split. You have an illustrative cell-fit worksheet and three simulated patterns: a well-calibrated cubic reference, a strained cubic powder and a slightly tetragonal powder. A plausible claim has to separate a real reduction in symmetry from instrumental broadening, heterogeneous strain and temperature drift.

The deliverable is not simply a graph or a plausible fit. Prepare a decision record containing the hypothesis, what quantity would be independently measured, expected direction of a change, possible instrumental error, and a practical follow-up observation. Use a clearly labelled hypothetical specimen identifier and synthetic numeric inputs. A reader should be able to identify the point at which raw data would enter the workflow if the investigation were ever conducted with real diffraction measurements.

### Proposed analysis

Create a model hierarchy: identical cubic lines, cubic lines with hkl-dependent width, and tetragonal lines with explicitly assigned (hkl) families. Collect at least three nonoverlapping high-angle peaks where splitting is predicted to be discernible; inspect the instrument reference collected before and after the batch. Make a table of peak centroids with standard errors, width and tentative indexing.

As a reproducibility check, keep the following artifacts: a plain-language data dictionary, a list of reflections or fitted features, a machine-readable calculation table, a plot with physical units and a short uncertainty statement. An analysis note should say whether calculations use the first-order Bragg relation, an ideal cubic geometry, a crystal-orientation transform, or some broader forward model. If the resulting claims would change after an unknown calibration offset, propose a standard measurement before drawing conclusions.

### Evaluation of the competing explanations

A convincing tetragonal assignment should predict several new relationships among reflections, not merely explain one visual shoulder. Failure to resolve predicted splitting is a bound on distortion at the achieved resolution, not definitive proof of cubic symmetry.

Make an evidence matrix with four columns: observation, expectation from the preferred model, expectation from the strongest alternative model, and an additional test. The final column matters because two models may fit the synthetic examples equally well. Compare what each model predicts **outside the fitted measurements**; such out-of-sample predictions are more informative than inspecting only the peaks used to set model parameters.

### Limitations and ethical interpretation

The simulated table deliberately omits real instrumental drift, absorption and actual atom scattering factors. The conclusion must therefore remain conditional, with a control-based follow-up rather than a yes/no phase certification.

No numerical exercise in this unit is a certified diffraction standard or a substitute for actual experimental metrology. If the claimed result could influence structural integrity, regulated products or high-consequence materials selection, report that the simulated evidence is inadequate for such a decision. A research-quality paper would require real datasets, calibration, transparent sample provenance, repeat experiments and qualified scientific review.

### Assessment rubric

| Criterion | Full-credit evidence | Warning sign |
|---|---|---|
| Physical correctness | Correct equations, dimensions, reciprocal-space conventions | Confuses θ and 2θ or treats index labels as units |
| Model adequacy | At least one named, testable rival mechanism | Declares a phase using one convenient peak |
| Numerical reproducibility | Equations, assumptions and files allow independent recomputation | Only a rounded calculator screenshot |
| Interpretation | Says which quantities were observed and which were inferred | Calls synthetic data a laboratory finding |
| Scope and ethics | Gives uncertainty, limitations and next measurement | Makes a safety or commercial certification claim |



## Unit research commentary — evidence across scales

A symmetry challenge begins with two lists of fractional positions in the same cubic cell. One list contains 000 and ½½½; the other contains 000 and a chemically distinct occupant at ½½½. A learner can draw identical conventional boxes for both without proving that the same centering symmetry applies to the full electron-density distribution. Translating by the centering vector maps an atom onto a different species in the second case. Unless the scattering density and physical structure are invariant, the corresponding extinction rule cannot be claimed. Use this thought experiment to distinguish a mathematical grid of possible points from a valid symmetry operation of an actual decorated structure.

Next compare primitive and conventional volumes without calculating any diffraction angle. The primitive description and centered conventional description must predict the same number of lattice points per physical volume. An apparently different density may reveal that the student counted atoms as whole corner contributions or used a formula-unit mass inconsistent with the chosen cell. Once the lattice point accounting is corrected, vary occupancy to determine which observations would change: cell geometry may remain nearly constant, while mass density and some relative intensities can change. That distinction motivates measuring multiple complementary properties.

For a small research exercise, label three synthetic specimens as fully occupied, vacancy-bearing, and chemically ordered. Do not assign real diffraction patterns to them. Predict qualitatively which inferred structural variables require intensity data and which are constrained mostly by peak positions. Explain why a conventional cell is a representation, not a unique microscopic object, and why a good indexing fit is insufficient to confirm atomic occupancy. A defensible report records the lattice setting, the basis, and the experimental assumptions independently. The concluding question is not whether a drawing looks periodic, but which symmetry action leaves the entire physical motif invariant and how a measurable interference pattern could test that invariance.

### End-of-unit examiner challenge: Lattices, cells, and symmetry

Write an evidence-based defense of **whether a physically equivalent cell description changes any measurable quantity**. Begin by defining how **integer lattice point accounting** would be measured and listing the necessary independent controls for **cell length; site occupancy; chosen setting**. Then name a physically distinct mechanism that could imitate the preferred explanation: **a mismatched atom count or incorrect assignment of a centering operation**. The response must show why that mechanism is plausible, rather than merely listing it as a caveat. Select one follow-up measurement that makes different predictions for the rival models; state what a negative result would mean. Finally prepare an annotated calculation from the two teaching formulas associated with this unit and explain why exact numerical agreement with a forward equation does not validate the specimen interpretation. Include an uncertainty estimate and say whether the proposed material conclusion is supported, conditional or unresolved. This is a reasoning task using synthetic evidence, not an authorization to operate an instrument.
