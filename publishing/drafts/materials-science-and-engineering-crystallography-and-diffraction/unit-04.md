# Unit 4: Powder diffraction and phase identification

**Guiding question:** How do we move from a raw detector trace to an appropriately qualified phase claim?

This unit connects powder measurement and phase analysis to an observable experiment. Every example is fictional and intentionally simplified. The sequence is designed so that the first two lessons provide definitions, the middle lessons test consequences, and the fifth lesson confronts ambiguity. Read plots as conditional calculations rather than laboratory observations.

## Investigation framework: Powder measurement and phase analysis





### Unit-wide reasoning objective




## Lesson 4.1 — Powder specimen preparation

### 1. Physical picture and mathematical meaning

A powder pattern approximates a sum over many crystallites with nearly random orientations. Crushing, sieving, particle size, sample displacement and texture influence observed intensities and line shapes. A flat plate can favor certain grains while capillary transmission may reduce some texture effects. Preparation may itself create strain or change hydration state in sensitive phases.


### 2. What to measure and what it means

Document grinding duration, sample holder, fill depth, spinning mode and conditioning temperature. Compare patterns collected after gentle and aggressive preparation. Look for peak broadening or intensity-ratio changes, and resist attributing differences to a new phase until preparation artifacts are excluded.


Consider the targeted decision **whether a phase candidate predicts several independent strong lines**. Specify one null hypothesis that competes with the preferred explanation and design a control that could falsify it. Make a small table of predicted features for both interpretations before inspecting any synthetic data. Such predeclared contrasts reduce the temptation to keep only peaks that favor the desired material narrative. Calibration, specimen preparation and the physics of scattering should be assessed before microstructure claims are written.

### 3. Interpretation, alternative explanations and boundaries

Sample preparation is part of the measurement chain; a claimed improvement in crystallinity can result from changed packing or holder alignment rather than a real structural transformation.


One competing explanation to test here is **holder contamination**. This is not a guaranteed cause, but it deserves a clear discrimination experiment. Decide whether a changed scan range, an independent standard, a different specimen orientation or a second probe would expose that alternative. Also ask whether the proposed test changes one parameter at a time. An experiment that simultaneously changes wavelength, mounting and background correction may produce a new curve without clarifying why it changed.

### 4. Fully specified synthetic calculation

The linked model is **Cubic 200 peak position**. Its one-variable input is **cubic a** (nm), the selected demonstration value is **0.355**, and the computed value is **51.4398 degrees**. The exact model expression is `2*Math.asin(0.15406/a)*180/Math.PI` using the variable shown; this is intentionally a classroom-level forward relationship. Model assumptions: Cu-like λ=0.15406 nm; cubic d200 = a/2.


| Input (nm) | Predicted degrees | Interpretation |
|---:|---:|---|
| 0.365 | 49.9322 | Low-side comparison under fixed assumptions |
| 0.405 | 44.7163 | Reference setting for sensitivity |
| 0.47 | 38.269 | High-side comparison under fixed assumptions |


### 5. Data collection and reproducibility protocol

Design a comparison that measures **calibrated one-dimensional diffraction pattern** while holding specimen state and geometry as steady as possible. Record **sample-holder reference; reference standard; measured 2θ peaks**. Repeat an independent reference and state what result would support **whether a phase candidate predicts several independent strong lines**. Record the decision rule before looking at a fitted pattern.

### 6. Diagnostic failure mode

A visually smooth diffraction trace is not proof that the sample was random, homogeneous or uncontaminated.

In the current unit, a particularly relevant practical trap is **overfitting one phase and hiding residual peaks in the baseline**. An analyst who ignores it can obtain a mathematically self-consistent answer from the wrong inputs. Diagnose the trap by returning to an invariant: a reference specimen, multiple indexed reflections, a repeated geometry, a known scattering convention or an independent probe. If the disagreement persists, report it as an unresolved limitation. Do not change a correction parameter solely to force a desirable phase or property estimate.


### 7. Knowledge-check and discussion questions

- **Explain:** What is the physical distinction between the quantity named in **Powder specimen preparation** and the observable used to estimate it? Give one explicit assumption.
- **Calculate:** Reproduce case MSE-C16 and evaluate how the output changes when the slider parameter moves from 0.365 to 0.47 nm.
- **Challenge:** Could **holder contamination** explain the observed feature? State a discriminating control rather than merely saying that more data are required.



## Lesson 4.2 — Instrument optics and angular calibration

### 1. Physical picture and mathematical meaning

The incident-beam spectrum, divergence optics, sample geometry, detector acceptance and position calibration determine the instrument response. A monochromator, filter or energy-discriminating detector changes spectral artifacts differently. Zero-angle offset and sample displacement can generate systematic peak-position trends that resemble changes in lattice parameters. Resolution must be considered before diagnosing splitting.


### 2. What to measure and what it means

Use a certified reference material according to its instructions to estimate the instrument angular offset. Fit multiple peaks across the scan range rather than calibrating from one point. Store the raw reference pattern, fitting method and residual plot with the unknown sample results.



### 3. Interpretation, alternative explanations and boundaries

Corrected positions should be reproducible within stated uncertainty. A fitted lattice constant obtained from just one uncalibrated peak is not a defensible basis for small-strain claims.


One competing explanation to test here is **sample-height shift**. This is not a guaranteed cause, but it deserves a clear discrimination experiment. Decide whether a changed scan range, an independent standard, a different specimen orientation or a second probe would expose that alternative. Also ask whether the proposed test changes one parameter at a time. An experiment that simultaneously changes wavelength, mounting and background correction may produce a new curve without clarifying why it changed.

### 4. Fully specified synthetic calculation

The linked model is **Two-phase calibrated intensity fraction**. Its one-variable input is **phase A corrected integrated intensity** (counts), the selected demonstration value is **38**, and the computed value is **0.487179 fraction**. The exact model expression is `I/(I+40)` using the variable shown; this is intentionally a classroom-level forward relationship. Model assumptions: Toy proportional-intensity model with phase B corrected intensity fixed at 40; not general Rietveld quantification.


| Input (counts) | Predicted fraction | Interpretation |
|---:|---:|---|
| 36 | 0.473684 | Low-side comparison under fixed assumptions |
| 60 | 0.6 | Reference setting for sensitivity |
| 80 | 0.666667 | High-side comparison under fixed assumptions |


### 5. Data collection and reproducibility protocol



### 6. Diagnostic failure mode

Do not silently tune a calibration shift until a favored database reference appears to match.




### 7. Knowledge-check and discussion questions

- **Explain:** What is the physical distinction between the quantity named in **Instrument optics and angular calibration** and the observable used to estimate it? Give one explicit assumption.
- **Calculate:** Reproduce case MSE-C17 and evaluate how the output changes when the slider parameter moves from 36 to 80 counts.
- **Challenge:** Could **sample-height shift** explain the observed feature? State a discriminating control rather than merely saying that more data are required.



## Lesson 4.3 — Peak search and baseline estimation

### 1. Physical picture and mathematical meaning

A raw diffraction pattern includes sample scattering, background, instrumental contributions, counting noise and possible fluorescence. Smoothing suppresses high-frequency fluctuations but may also erase real narrow peaks or create artificial shoulders. A baseline model must not pass through broad sample features merely to make the residual visually small. Peak positions, integrated intensities and widths should carry uncertainty.


### 2. What to measure and what it means

Compare a rolling minimum, a smooth polynomial and a manually constrained baseline against the same synthetic trace. Inject known narrow and broad peaks and quantify whether the procedure recovers their areas. Inspect residuals for correlated deviations that betray a poor background model.



### 3. Interpretation, alternative explanations and boundaries

A candidate peak below the local detection threshold remains uncertain; a software peak-picker flag is not itself evidence of a phase.


One competing explanation to test here is **preferred orientation**. This is not a guaranteed cause, but it deserves a clear discrimination experiment. Decide whether a changed scan range, an independent standard, a different specimen orientation or a second probe would expose that alternative. Also ask whether the proposed test changes one parameter at a time. An experiment that simultaneously changes wavelength, mounting and background correction may produce a new curve without clarifying why it changed.

### 4. Fully specified synthetic calculation

The linked model is **Cubic 200 peak position**. Its one-variable input is **cubic a** (nm), the selected demonstration value is **0.425**, and the computed value is **42.5069 degrees**. The exact model expression is `2*Math.asin(0.15406/a)*180/Math.PI` using the variable shown; this is intentionally a classroom-level forward relationship. Model assumptions: Cu-like λ=0.15406 nm; cubic d200 = a/2.


| Input (nm) | Predicted degrees | Interpretation |
|---:|---:|---|
| 0.365 | 49.9322 | Low-side comparison under fixed assumptions |
| 0.405 | 44.7163 | Reference setting for sensitivity |
| 0.47 | 38.269 | High-side comparison under fixed assumptions |


### 5. Data collection and reproducibility protocol



### 6. Diagnostic failure mode

Reporting only peaks retained after arbitrary threshold adjustment creates biased phase claims and hides the analysis trail.




### 7. Knowledge-check and discussion questions

- **Explain:** What is the physical distinction between the quantity named in **Peak search and baseline estimation** and the observable used to estimate it? Give one explicit assumption.
- **Calculate:** Reproduce case MSE-C18 and evaluate how the output changes when the slider parameter moves from 0.365 to 0.47 nm.
- **Challenge:** Could **preferred orientation** explain the observed feature? State a discriminating control rather than merely saying that more data are required.



## Lesson 4.4 — Qualitative phase matching

### 1. Physical picture and mathematical meaning

A phase identification begins by considering a plausible list of crystalline phases and comparing multiple peak positions and relative intensities. Instrument wavelength, chemistry, sample processing and potential polymorphs constrain the search. Peak overlap, preferred orientation and minor-phase concentration limits affect confidence. Database matching is a hypothesis-generation tool, not a chemical assay.


### 2. What to measure and what it means

Construct a phase-match table with three or more high-confidence reflections for each candidate and annotate absent predicted peaks. Test a rival phase model and describe whether its unmatched peaks would have been detectable under the measurement conditions. Use a sample blank to detect holder peaks.



### 3. Interpretation, alternative explanations and boundaries

When two candidate phases share reflections, a unique isolated line or independent chemical result may be decisive. Ambiguous patterns should be reported as such rather than forced into one catalog hit.


One competing explanation to test here is **mixed-phase overlap**. This is not a guaranteed cause, but it deserves a clear discrimination experiment. Decide whether a changed scan range, an independent standard, a different specimen orientation or a second probe would expose that alternative. Also ask whether the proposed test changes one parameter at a time. An experiment that simultaneously changes wavelength, mounting and background correction may produce a new curve without clarifying why it changed.

### 4. Fully specified synthetic calculation

The linked model is **Two-phase calibrated intensity fraction**. Its one-variable input is **phase A corrected integrated intensity** (counts), the selected demonstration value is **66**, and the computed value is **0.622642 fraction**. The exact model expression is `I/(I+40)` using the variable shown; this is intentionally a classroom-level forward relationship. Model assumptions: Toy proportional-intensity model with phase B corrected intensity fixed at 40; not general Rietveld quantification.


| Input (counts) | Predicted fraction | Interpretation |
|---:|---:|---|
| 36 | 0.473684 | Low-side comparison under fixed assumptions |
| 60 | 0.6 | Reference setting for sensitivity |
| 80 | 0.666667 | High-side comparison under fixed assumptions |


### 5. Data collection and reproducibility protocol



### 6. Diagnostic failure mode

One impressive match score is not equivalent to a validated phase assignment, especially in mixtures.




### 7. Knowledge-check and discussion questions

- **Explain:** What is the physical distinction between the quantity named in **Qualitative phase matching** and the observable used to estimate it? Give one explicit assumption.
- **Calculate:** Reproduce case MSE-C19 and evaluate how the output changes when the slider parameter moves from 36 to 80 counts.
- **Challenge:** Could **mixed-phase overlap** explain the observed feature? State a discriminating control rather than merely saying that more data are required.



## Lesson 4.5 — Quantitative phase analysis and refinement

### 1. Physical picture and mathematical meaning

Whole-pattern modeling refines lattice parameters, scale factors, profile functions, background and possibly structural parameters against many measured intensities. Quantitative phase fraction estimates depend on structure factors, absorption contrast, crystallinity and preferred orientation. The Rietveld method is powerful but risks parameter correlation and overfitting if many free terms absorb model defects.


### 2. What to measure and what it means

Fit the same simulated mixture with a minimal phase list and a more complex model. Track Rwp or another residual metric while checking difference patterns, parameter stability and physical plausibility. Report which structural parameters were fixed, restrained or freely refined.



### 3. Interpretation, alternative explanations and boundaries

A small residual is necessary for a good description but not sufficient for a correct physical model. Independent chemistry and microscopy can validate the phase interpretation.


One competing explanation to test here is **an amorphous minority fraction**. This is not a guaranteed cause, but it deserves a clear discrimination experiment. Decide whether a changed scan range, an independent standard, a different specimen orientation or a second probe would expose that alternative. Also ask whether the proposed test changes one parameter at a time. An experiment that simultaneously changes wavelength, mounting and background correction may produce a new curve without clarifying why it changed.

### 4. Fully specified synthetic calculation

The linked model is **Cubic 200 peak position**. Its one-variable input is **cubic a** (nm), the selected demonstration value is **0.49**, and the computed value is **36.6502 degrees**. The exact model expression is `2*Math.asin(0.15406/a)*180/Math.PI` using the variable shown; this is intentionally a classroom-level forward relationship. Model assumptions: Cu-like λ=0.15406 nm; cubic d200 = a/2.


| Input (nm) | Predicted degrees | Interpretation |
|---:|---:|---|
| 0.365 | 49.9322 | Low-side comparison under fixed assumptions |
| 0.405 | 44.7163 | Reference setting for sensitivity |
| 0.47 | 38.269 | High-side comparison under fixed assumptions |


### 5. Data collection and reproducibility protocol



### 6. Diagnostic failure mode

Do not call mass fractions absolute if amorphous phases or unmodeled components could be present.




### 7. Knowledge-check and discussion questions

- **Explain:** What is the physical distinction between the quantity named in **Quantitative phase analysis and refinement** and the observable used to estimate it? Give one explicit assumption.
- **Calculate:** Reproduce case MSE-C20 and evaluate how the output changes when the slider parameter moves from 0.365 to 0.47 nm.
- **Challenge:** Could **an amorphous minority fraction** explain the observed feature? State a discriminating control rather than merely saying that more data are required.



## Explore two independent interactive model families

<!-- MODEL_6 -->

<!-- MODEL_7 -->

## Integrated investigation: A two-phase oxide with a hidden amorphous fraction

### Evidence brief

A powder analyst fits two crystalline phases with excellent residuals and reports 70% A and 30% B by mass. Independent microscopy suggests glassy regions, which the crystalline phases alone cannot account for.



### Proposed analysis

Develop a synthetic two-phase peak list and a flat plus sloping background. Test the effect of texture by modifying the intensity of only one reflection family. Add an internal standard of known quantity in a hypothetical measurement plan and discuss what information would be required for amorphous quantification.



### Evaluation of the competing explanations

Rietveld scale factors can describe relative crystalline contributions when assumptions hold, but unmodeled amorphous material prevents interpreting them as all-material mass fractions. Results should distinguish relative crystalline percentages from absolute sample composition.



### Limitations and ethical interpretation

The exercise uses simplified proportional intensities and must not be used for quantitative phase certification or safety decisions.



### Assessment rubric





## Unit research commentary — evidence across scales

Powder diffraction is particularly vulnerable to a superficially convincing database match. Imagine a specimen formed by heating a two-phase ceramic under a new atmosphere. The scan contains one sharp dominant peak, several broad features, and a weak line near a holder reflection. An automated matcher proposes a famous oxide polymorph. The correct first task is to verify instrument wavelength and peak scale, subtract or model the holder contribution, and identify at least three predicted lines that could test the proposal independently. A phase assignment supported only by the most prominent line is not ready to report.

The second task is to quantify what the scan cannot show. A crystalline phase below the detection limit may still affect material properties; a glassy fraction may add a broad background rather than a separable list of Bragg peaks. An apparently precise crystalline-phase percentage can therefore overstate absolute composition if amorphous material was not measured. Model refinements may also correlate scale, preferred orientation, thermal displacement and particle absorption. A low residual is useful but must be tested alongside parameter stability, physically plausible chemistry and independent characterization.

Develop an analysis plan with a calibration standard, sample blank, predeclared phase candidates and a holdout set of reflection predictions. Record residuals at predicted-but-unobserved peaks as carefully as matched peaks. Evaluate whether a preferred orientation correction removes physically interpretable intensity differences or merely hides an incorrect phase model. If a minority phase remains ambiguous, state a concentration bound tied to the actual noise, rather than claiming an absolute absence. The practical engineering recommendation may be to acquire a different geometry, extend scan range or use complementary spectroscopy before deciding whether the heat treatment achieved its intended transformation. The point of phase identification is an evidence-based decision, not a visually impressive match score.

### End-of-unit examiner challenge: Powder diffraction and phase identification

Write an evidence-based defense of **whether a phase candidate predicts several independent strong lines**. Begin by defining how **calibrated one-dimensional diffraction pattern** would be measured and listing the necessary independent controls for **sample-holder reference; reference standard; measured 2θ peaks**. Then name a physically distinct mechanism that could imitate the preferred explanation: **overfitting one phase and hiding residual peaks in the baseline**. The response must show why that mechanism is plausible, rather than merely listing it as a caveat. Select one follow-up measurement that makes different predictions for the rival models; state what a negative result would mean. Finally prepare an annotated calculation from the two teaching formulas associated with this unit and explain why exact numerical agreement with a forward equation does not validate the specimen interpretation. Include an uncertainty estimate and say whether the proposed material conclusion is supported, conditional or unresolved. This is a reasoning task using synthetic evidence, not an authorization to operate an instrument.
