# Unit 1: Measurement science, sampling and uncertainty

**Core research question.** What does a numerical materials property mean when specimen history, reference calibration and measurement uncertainty are taken seriously?

## Physical context and prerequisite reasoning

Materials characterization is a chain from an explicitly defined measurand to a representative physical specimen, an instrument signal, a calibration model, a numerical estimate and a defensible scientific claim. Distinguish an observable from a latent material property. A peak position, brightness level or detector count is observed; crystallite size or chemical state is inferred under assumptions. A dataset without information about sampling, calibration, detector response and processing is not reproducible. In this first unit the central challenge is to make the definition of an experiment more rigorous than the attractiveness of its plotted result.

A fundamental distinction in **Measurement science, sampling and uncertainty** is the difference between what the instrument records and what one wants to infer. Design a chain of explanation containing a specimen with a known history, a measurable interaction, a recorded signal, one or more corrections, a model or reference, and the qualified property estimate. State which component could change when the operator selects another location, detector or processing program. In materials science an instrument often averages over a volume, while a proposed mechanism may live at an interface or individual defect. That mismatch can make a precise measurement irrelevant. This unit therefore emphasizes independent samples, documented acquisition conditions and physical counterexamples rather than applying formulae mechanically.

## Investigative exercise for the entire unit

Two batches of a heat-treated alloy are reported to have different hardness, but one batch was polished differently and measured on another day. Build a sampling and measurement program that tests whether the batch difference survives specimen preparation, drift, replicate and operator checks.

## Lesson 1.1 — Measurands, observables and operational definitions

### Physical mechanism and its measurable signature

A measurand is the quantity intended to be measured, including its material state, geometry and measurement conditions. The detector may respond to photons, electrons, displacement or voltage while the reported property depends on an interpretation model. For example, an indentation hardness value is load divided by inferred contact area, not a direct measurement of atomic bonding. Define where, when and on which scale the result applies. For multiphase alloys a single specimen-average value can obscure segregation and gradients; for coatings a bulk measurement may miss the relevant outer nanometres. Measurement objectives should therefore name length scale and acceptance criteria before the instrument is selected.

**Explicit defining relation.** Measured result y=f(raw response, calibration, geometry, corrections, environment); a number without the defining function and measurement conditions is incomplete.

### Concrete materials-characterization problem

A coating claims 200 nm thickness. Contrast cross-sectional microscopy, ellipsometric fit thickness and a stylus step-height result, and predict where surface roughness alters their meaning.

### Reproducible synthetic worked example

The nearby interactive card titled **Independent-mean standard error** changes **Independent specimens**. The declared calculation is `8/Math.sqrt(n)`; the model returns 1.66811531 MPa at 23 specimens and 1.39262125 MPa at 33 specimens. Thus as the displayed input grows across these two test settings, the calculated output decreases. The secant sensitivity over this interval is -0.027549406 MPa per specimens. Check the sign from the governing equation rather than trusting the plotted curve, and confirm dimensional consistency before copying results to the case table. The method is a pedagogical sensitivity test, not a calibrated measurement of a commercial or laboratory specimen.

### Independent experimental and calibration plan

A realistic measurement study of **measurands, observables and operational definitions** would begin with **reference standards, duplicate specimen runs and a written sample registry**, retaining **raw response, calibration residuals, date, operator, repeatability, specimen ID and traceability chain**. An independent check would use **a reference item measured blind and a second instrument or operating condition**.

### Threats to interpretation and a failure mode

Different techniques can deliver values with identical units but different operational definitions. Numerical agreement is not necessarily a common physical interpretation.

### Exercises with solution guidance

**Exercise A — physical inference.** Starting from Measured result y=f(raw response, calibration, geometry, corrections, environment); a number without the defining function and measurement conditions is incomplete. explain what is measured, what is inferred, the unit of every symbol and which environmental or microstructural assumption is most fragile. Then describe why the result of the same specimen measured before and after surface preparation might not be directly comparable. *Answer guide:* define the measurand before the apparatus, identify one calibration-dependent term, and test an alternative physical cause rather than listing properties of the equipment.

**Exercise B — numerical and uncertainty check.** Independently calculate the two numbers in **Independent-mean standard error: 23 specimens → 1.6681153 MPa; 33 specimens → 1.3926212 MPa** and estimate the local sensitivity at the midpoint. Choose an illustrative input standard uncertainty and propagate it using a first-order derivative; identify at least one source of model uncertainty not included by this arithmetic. *Answer guide:* use the model's stated units and bounds, do not round intermediate conversions prematurely, and explicitly label every calculated number synthetic.

**Exercise C — falsification and control.** Design a modest experiment for **measurands, observables and operational definitions** with a procedural blank or reference, three independent physical specimens where meaningful, one orthogonal measurement and a predefined exclusion rule. State a possible observation that makes your favored inference untenable. *Answer guide:* record material processing and measurement history, separate technical repeats from sample repeats, and require that the independent test distinguishes competing hypotheses.

**Discussion and decision.** Write a single-sentence operational definition of coating thickness that two laboratories could independently attempt to reproduce. Give one conclusion supported directly by a detector observable, one conclusion requiring a fitted model, and one conclusion that cannot yet be made at all. Finish with a single high-value next measurement and explain why its expected information is worth the cost.

## Lesson 1.2 — Precision, accuracy, bias and reference materials

### Physical mechanism and its measurable signature

Precision concerns the spread of repeated results; systematic bias concerns displacement from an appropriate reference. A tightly clustered sequence can be inaccurate because the scale factor or zero intercept is wrong. Calibrations should be carried out over the actual range of use and accompanied by residuals and drift checks rather than a single reassuring coefficient of determination. Certified reference materials, when appropriate to the method and matrix, connect the signal to independently assigned values and uncertainties. Instrument warm-up, detector linearity and sample matrix effects should be included in the plan. A blank can identify contamination but cannot by itself determine a correct sensitivity factor.

**Explicit defining relation.** A first-order linear calibration is S=a x+b; its inverse x=(S-b)/a propagates uncertainties in S, a and b.

### Concrete materials-characterization problem

A force sensor reports 50.0 N repeatedly for a calibrated reference near 48.5 N. Diagnose which quantity describes repeatability and which describes a correction requirement.

### Reproducible synthetic worked example

The nearby interactive card titled **Linear response and fixed calibration offset** changes **True reference level**. The declared calculation is `1.02*x+1.5`; the model returns 32.1 detector units at 30 arb. unit and 42.3 detector units at 40 arb. unit. Thus as the displayed input grows across these two test settings, the calculated output increases. The secant sensitivity over this interval is 1.02 detector units per arb. unit. Check the sign from the governing equation rather than trusting the plotted curve, and confirm dimensional consistency before copying results to the case table. The method is a pedagogical sensitivity test, not a calibrated measurement of a commercial or laboratory specimen.

### Independent experimental and calibration plan

A realistic measurement study of **precision, accuracy, bias and reference materials** would begin with **reference standards, duplicate specimen runs and a written sample registry**, retaining **raw response, calibration residuals, date, operator, repeatability, specimen ID and traceability chain**. An independent check would use **a reference item measured blind and a second instrument or operating condition**.

### Threats to interpretation and a failure mode

Reproducibility within a laboratory is not equivalent to interlaboratory accuracy. Calibration transfer across probe geometry or sample matrix can fail.

### Exercises with solution guidance

**Exercise A — physical inference.** Starting from A first-order linear calibration is S=a x+b; its inverse x=(S-b)/a propagates uncertainties in S, a and b. explain what is measured, what is inferred, the unit of every symbol and which environmental or microstructural assumption is most fragile. Then describe why the result of a calibration control against an unknown sample might not be directly comparable. *Answer guide:* define the measurand before the apparatus, identify one calibration-dependent term, and test an alternative physical cause rather than listing properties of the equipment.

**Exercise B — numerical and uncertainty check.** Independently calculate the two numbers in **Linear response and fixed calibration offset: 30 arb. unit → 32.1 detector units; 40 arb. unit → 42.3 detector units** and estimate the local sensitivity at the midpoint. Choose an illustrative input standard uncertainty and propagate it using a first-order derivative; identify at least one source of model uncertainty not included by this arithmetic. *Answer guide:* use the model's stated units and bounds, do not round intermediate conversions prematurely, and explicitly label every calculated number synthetic.

**Exercise C — falsification and control.** Design a modest experiment for **precision, accuracy, bias and reference materials** with a procedural blank or reference, three independent physical specimens where meaningful, one orthogonal measurement and a predefined exclusion rule. State a possible observation that makes your favored inference untenable. *Answer guide:* record material processing and measurement history, separate technical repeats from sample repeats, and require that the independent test distinguishes competing hypotheses.

**Discussion and decision.** What pattern in calibration residuals would reject a straight-line conversion even if the fit has high R-squared? Give one conclusion supported directly by a detector observable, one conclusion requiring a fitted model, and one conclusion that cannot yet be made at all. Finish with a single high-value next measurement and explain why its expected information is worth the cost.

<!-- MODEL_0 -->

## Lesson 1.3 — Sampling, specimen preparation and representativeness

### Physical mechanism and its measurable signature

A specimen is only a sample of a material lot, part or device. Cutting, grinding, embedding, polishing, etching, cleaning and sputtering can modify surfaces or create new microstructures. A polished cross section can preferentially remove soft phases and embed hard abrasive particles; a fragile coating can delaminate while being prepared. Spatial heterogeneity determines how many regions, grains and independently produced samples must be measured. The unit of replication must be defined by the inference objective: several pixels from one micrograph do not establish manufacturing reproducibility across lots. A sampling plan should document exclusion criteria before the data are collected.

**Explicit defining relation.** If a population fraction is p, the binomial standard error under independent sampling is approximately sqrt[p(1-p)/n], with independence and segmentation assumptions.

### Concrete materials-characterization problem

An engineer claims porosity is 0.3% after counting ten images of one small zone; test whether the estimate supports the entire casting or only the inspected field.

### Reproducible synthetic worked example

The nearby interactive card titled **Independent-mean standard error** changes **Independent specimens**. The declared calculation is `8/Math.sqrt(n)`; the model returns 1.2344268 MPa at 42 specimens and 1.10940039 MPa at 52 specimens. Thus as the displayed input grows across these two test settings, the calculated output decreases. The secant sensitivity over this interval is -0.012502641 MPa per specimens. Check the sign from the governing equation rather than trusting the plotted curve, and confirm dimensional consistency before copying results to the case table. The method is a pedagogical sensitivity test, not a calibrated measurement of a commercial or laboratory specimen.

### Independent experimental and calibration plan

A realistic measurement study of **sampling, specimen preparation and representativeness** would begin with **reference standards, duplicate specimen runs and a written sample registry**, retaining **raw response, calibration residuals, date, operator, repeatability, specimen ID and traceability chain**. An independent check would use **a reference item measured blind and a second instrument or operating condition**.

### Threats to interpretation and a failure mode

A beautiful representative micrograph may actually be an intentionally selected best-case region. Random or systematic position selection is preferable for population claims.

### Exercises with solution guidance

**Exercise A — physical inference.** Starting from If a population fraction is p, the binomial standard error under independent sampling is approximately sqrt[p(1-p)/n], with independence and segmentation assumptions. explain what is measured, what is inferred, the unit of every symbol and which environmental or microstructural assumption is most fragile. Then describe why the result of one carefully chosen field against randomized spatial fields might not be directly comparable. *Answer guide:* define the measurand before the apparatus, identify one calibration-dependent term, and test an alternative physical cause rather than listing properties of the equipment.

**Exercise B — numerical and uncertainty check.** Independently calculate the two numbers in **Independent-mean standard error: 42 specimens → 1.2344268 MPa; 52 specimens → 1.1094004 MPa** and estimate the local sensitivity at the midpoint. Choose an illustrative input standard uncertainty and propagate it using a first-order derivative; identify at least one source of model uncertainty not included by this arithmetic. *Answer guide:* use the model's stated units and bounds, do not round intermediate conversions prematurely, and explicitly label every calculated number synthetic.

**Exercise C — falsification and control.** Design a modest experiment for **sampling, specimen preparation and representativeness** with a procedural blank or reference, three independent physical specimens where meaningful, one orthogonal measurement and a predefined exclusion rule. State a possible observation that makes your favored inference untenable. *Answer guide:* record material processing and measurement history, separate technical repeats from sample repeats, and require that the independent test distinguishes competing hypotheses.

**Discussion and decision.** How would the conclusion change if defects cluster near a casting edge rather than appearing independently? Give one conclusion supported directly by a detector observable, one conclusion requiring a fitted model, and one conclusion that cannot yet be made at all. Finish with a single high-value next measurement and explain why its expected information is worth the cost.

## Lesson 1.4 — Detection limits, spatial resolution and dynamic range

### Physical mechanism and its measurable signature

Resolution, sensitivity, quantification limit and precision answer different questions. Spatial resolution is the ability to distinguish nearby objects or features; a low detection limit is the ability to reliably identify a signal above background. The pixel spacing of an image is not identical to physical resolution, and an elemental detection limit from one matrix cannot be transferred blindly to another. Dynamic range may be constrained by saturation at high signals and background variation at low signals. State a declared decision threshold, expected false-positive rate and the signal processing used to decide presence or absence. Deconvolution can sharpen an image visually while amplifying noise and producing artificial features.

**Explicit defining relation.** For an ideal independent-noise average, the standard uncertainty of a mean is s/sqrt(n); correlated samples require effective sample size adjustment.

### Concrete materials-characterization problem

A micrograph has 2 nm pixels but a 15 nm interaction volume. Decide which structural claims can be supported without assuming that the pixel pitch is the resolution.

### Reproducible synthetic worked example

The nearby interactive card titled **Linear response and fixed calibration offset** changes **True reference level**. The declared calculation is `1.02*x+1.5`; the model returns 52.5 detector units at 50 arb. unit and 62.7 detector units at 60 arb. unit. Thus as the displayed input grows across these two test settings, the calculated output increases. The secant sensitivity over this interval is 1.02 detector units per arb. unit. Check the sign from the governing equation rather than trusting the plotted curve, and confirm dimensional consistency before copying results to the case table. The method is a pedagogical sensitivity test, not a calibrated measurement of a commercial or laboratory specimen.

### Independent experimental and calibration plan

A realistic measurement study of **detection limits, spatial resolution and dynamic range** would begin with **reference standards, duplicate specimen runs and a written sample registry**, retaining **raw response, calibration residuals, date, operator, repeatability, specimen ID and traceability chain**. An independent check would use **a reference item measured blind and a second instrument or operating condition**.

### Threats to interpretation and a failure mode

Detection failure is not proof of elemental absence. Report upper bounds and method conditions rather than declaring zero concentration.

### Exercises with solution guidance

**Exercise A — physical inference.** Starting from For an ideal independent-noise average, the standard uncertainty of a mean is s/sqrt(n); correlated samples require effective sample size adjustment. explain what is measured, what is inferred, the unit of every symbol and which environmental or microstructural assumption is most fragile. Then describe why the result of one instrument mode against a complementary physical mode might not be directly comparable. *Answer guide:* define the measurand before the apparatus, identify one calibration-dependent term, and test an alternative physical cause rather than listing properties of the equipment.

**Exercise B — numerical and uncertainty check.** Independently calculate the two numbers in **Linear response and fixed calibration offset: 50 arb. unit → 52.5 detector units; 60 arb. unit → 62.7 detector units** and estimate the local sensitivity at the midpoint. Choose an illustrative input standard uncertainty and propagate it using a first-order derivative; identify at least one source of model uncertainty not included by this arithmetic. *Answer guide:* use the model's stated units and bounds, do not round intermediate conversions prematurely, and explicitly label every calculated number synthetic.

**Exercise C — falsification and control.** Design a modest experiment for **detection limits, spatial resolution and dynamic range** with a procedural blank or reference, three independent physical specimens where meaningful, one orthogonal measurement and a predefined exclusion rule. State a possible observation that makes your favored inference untenable. *Answer guide:* record material processing and measurement history, separate technical repeats from sample repeats, and require that the independent test distinguishes competing hypotheses.

**Discussion and decision.** Give one instrumental test that separates actual resolution from magnification or oversampling. Give one conclusion supported directly by a detector observable, one conclusion requiring a fitted model, and one conclusion that cannot yet be made at all. Finish with a single high-value next measurement and explain why its expected information is worth the cost.

<!-- MODEL_1 -->

## Lesson 1.5 — Replicates, statistical intervals and significance

### Physical mechanism and its measurable signature

Repeat readings distinguish short-term instrument noise from specimen-to-specimen variation only when the sampling hierarchy is retained. A nested experiment may contain lots, specimens, regions, images and pixels; treating every pixel as an independent replicate understates uncertainty. Confidence intervals describe properties of an estimation procedure under its assumptions and do not turn observational samples into randomized experiments. A statistically detectable difference may be too small to matter for a design specification, while a scientifically consequential difference may remain uncertain with limited data. Predefine the minimal effect of practical interest and build a plan capable of detecting it.

**Explicit defining relation.** For independent observations with sample standard deviation s and count n, standard error of the mean is s/sqrt(n); do not use this expression for pseudoreplicates.

### Concrete materials-characterization problem

Compare hardness data from five independent billets with 200 indents on one billet; reason about why the larger indentation count cannot replace independent billets.

### Reproducible synthetic worked example

The nearby interactive card titled **Independent-mean standard error** changes **Independent specimens**. The declared calculation is `8/Math.sqrt(n)`; the model returns 1.01600102 MPa at 62 specimens and 0.949425327 MPa at 71 specimens. Thus as the displayed input grows across these two test settings, the calculated output decreases. The secant sensitivity over this interval is -0.0073972988 MPa per specimens. Check the sign from the governing equation rather than trusting the plotted curve, and confirm dimensional consistency before copying results to the case table. The method is a pedagogical sensitivity test, not a calibrated measurement of a commercial or laboratory specimen.

### Independent experimental and calibration plan

A realistic measurement study of **replicates, statistical intervals and significance** would begin with **reference standards, duplicate specimen runs and a written sample registry**, retaining **raw response, calibration residuals, date, operator, repeatability, specimen ID and traceability chain**. An independent check would use **a reference item measured blind and a second instrument or operating condition**.

### Threats to interpretation and a failure mode

A p-value does not measure the probability that the null hypothesis is true; post-hoc exclusion or stopping rules undermine nominal confidence levels.

### Exercises with solution guidance

**Exercise A — physical inference.** Starting from For independent observations with sample standard deviation s and count n, standard error of the mean is s/sqrt(n); do not use this expression for pseudoreplicates. explain what is measured, what is inferred, the unit of every symbol and which environmental or microstructural assumption is most fragile. Then describe why the result of two independent specimens against repeated readings of one specimen might not be directly comparable. *Answer guide:* define the measurand before the apparatus, identify one calibration-dependent term, and test an alternative physical cause rather than listing properties of the equipment.

**Exercise B — numerical and uncertainty check.** Independently calculate the two numbers in **Independent-mean standard error: 62 specimens → 1.016001 MPa; 71 specimens → 0.94942533 MPa** and estimate the local sensitivity at the midpoint. Choose an illustrative input standard uncertainty and propagate it using a first-order derivative; identify at least one source of model uncertainty not included by this arithmetic. *Answer guide:* use the model's stated units and bounds, do not round intermediate conversions prematurely, and explicitly label every calculated number synthetic.

**Exercise C — falsification and control.** Design a modest experiment for **replicates, statistical intervals and significance** with a procedural blank or reference, three independent physical specimens where meaningful, one orthogonal measurement and a predefined exclusion rule. State a possible observation that makes your favored inference untenable. *Answer guide:* record material processing and measurement history, separate technical repeats from sample repeats, and require that the independent test distinguishes competing hypotheses.

**Discussion and decision.** Design a nested replication structure for a claim about manufacturing lot consistency and name the correct experimental unit. Give one conclusion supported directly by a detector observable, one conclusion requiring a fitted model, and one conclusion that cannot yet be made at all. Finish with a single high-value next measurement and explain why its expected information is worth the cost.

## Unit 1 capstone — evidence review and design defense

**Investigation.** Two batches of a heat-treated alloy are reported to have different hardness, but one batch was polished differently and measured on another day. Build a sampling and measurement program that tests whether the batch difference survives specimen preparation, drift, replicate and operator checks.

1. **Specify a measurable claim.** Define the target parameter and where the specimens come from. Identify why the sampling population rather than the number of images matters for the engineering claim.
2. **Build a methods matrix.** Choose at least three complementary measurements for **measurement science, sampling and uncertainty**. For each report the instrument signal, calibration, spatial or information depth, most likely artifact and an orthogonal verification strategy.
3. **Audit two numerical models.** For both cards, calculate the default value, an endpoint and a sensitivity. Mark every quantity synthetic. Explain why agreement with its ideal formula is not sufficient for independent validation.
4. **Budget uncertainty and confounders.** Separate repeatability, reference calibration, specimen variability, geometry and data-reduction sensitivity. Include a possible correlated error and a case where a high pixel count is misleading.
5. **Make an evidence-limited decision.** Write 250 words separating directly supported observations from inferred structure or function. State precisely what additional result would reverse the proposed interpretation.

### Synthesis and transferable reasoning

A characterization workflow is useful when it turns a defined problem into falsifiable evidence. The same specimen can look different when probe volume, preparation, temperature, analysis background or inversion model changes. In **measurement science, sampling and uncertainty**, the central skill is not knowing a long list of instruments; it is matching each claim to a physically appropriate observable and understanding how to challenge that inference. A laboratory report should acknowledge the subset of the population sampled, not imply that a selected image or a synthetic curve describes every possible specimen. Favor a chain of traceable data over a single polished figure.

