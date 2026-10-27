# Unit 8: Data fusion, validation and reproducible scientific reporting

**Core research question.** How do multiple characterization methods jointly support a conclusion, and what evidence would still be missing?

## Physical context and prerequisite reasoning

Reliable characterization ends in a transparent inference, not in a collection of high-resolution figures. Every primary result should be connected to raw signal, preprocessing, controls, uncertainty, specimen identity and the decision it can actually support. Cross-method agreement is most valuable when techniques have different bias mechanisms. A complete evidence ledger records observed data, fitted quantities, model assumptions, uncertainty and plausible competing interpretations. A publishable report lets an independent reader see how the material was sampled and how the final claim was qualified.

A fundamental distinction in **Data fusion, validation and reproducible scientific reporting** is the difference between what the instrument records and what one wants to infer. Design a chain of explanation containing a specimen with a known history, a measurable interaction, a recorded signal, one or more corrections, a model or reference, and the qualified property estimate. State which component could change when the operator selects another location, detector or processing program. In materials science an instrument often averages over a volume, while a proposed mechanism may live at an interface or individual defect. That mismatch can make a precise measurement irrelevant. This unit therefore emphasizes independent samples, documented acquisition conditions and physical counterexamples rather than applying formulae mechanically.

## Investigative exercise for the entire unit

A university team claims a novel multifunctional nanocomposite from XRD, SEM, Raman and tensile tests. Audit the data lineage and propose the smallest extra experiment that could overturn the central claim.

## Lesson 8.1 — Constructing and propagating an uncertainty budget

### Physical mechanism and its measurable signature

An uncertainty budget lists contributions from repeatability, calibration, dimensions, background subtraction, sample positioning, model selection and environmental variation. Standard uncertainties should use consistent units and refer to the same measurand. For a smooth function of several inputs, first-order propagation uses sensitivity coefficients and covariance terms, not simply the square root of all instrument specifications. Correlated calibrations may dominate when both numerator and denominator share a reference; ignoring their covariance can over- or underestimate uncertainty. For highly nonlinear models or bounded parameters, Monte Carlo propagation and diagnostic plots may be more faithful than a linear approximation.

**Explicit defining relation.** For independent inputs x_i, u_c²(y)≈Σ(∂f/∂x_i)²u²(x_i); covariance terms are required when inputs are correlated.

### Concrete materials-characterization problem

An optical thickness model depends on refractive index and measured interference period. Determine whether assuming a fixed refractive index hides a larger uncertainty than spectral noise.

### Reproducible synthetic worked example

The nearby interactive card titled **Independent quadrature uncertainty** changes **Type A standard uncertainty**. The declared calculation is `Math.sqrt(u*u+4)`; the model returns 2.27297162 units at 1.08 units and 2.54261676 units at 1.57 units. Thus as the displayed input grows across these two test settings, the calculated output increases. The secant sensitivity over this interval is 0.5502962 units per units. Check the sign from the governing equation rather than trusting the plotted curve, and confirm dimensional consistency before copying results to the case table. The method is a pedagogical sensitivity test, not a calibrated measurement of a commercial or laboratory specimen.

### Independent experimental and calibration plan

A realistic measurement study of **constructing and propagating an uncertainty budget** would begin with **traceable cross-method report with retained raw files**, retaining **complete provenance, hierarchical sample identifiers, control records, uncertainty model and reviewer checklist**. An independent check would use **blind reanalysis, hold-out specimen, process variation and an independent detection mode**.

### Threats to interpretation and a failure mode

Reporting 0.1% repeatability does not justify 0.1% total accuracy when calibration and model contributions are larger.

### Exercises with solution guidance

**Exercise A — physical inference.** Starting from For independent inputs x_i, u_c²(y)≈Σ(∂f/∂x_i)²u²(x_i); covariance terms are required when inputs are correlated. explain what is measured, what is inferred, the unit of every symbol and which environmental or microstructural assumption is most fragile. Then describe why the result of a response measured across two excitation or environmental conditions might not be directly comparable. *Answer guide:* define the measurand before the apparatus, identify one calibration-dependent term, and test an alternative physical cause rather than listing properties of the equipment.

**Exercise B — numerical and uncertainty check.** Independently calculate the two numbers in **Independent quadrature uncertainty: 1.08 units → 2.2729716 units; 1.57 units → 2.5426168 units** and estimate the local sensitivity at the midpoint. Choose an illustrative input standard uncertainty and propagate it using a first-order derivative; identify at least one source of model uncertainty not included by this arithmetic. *Answer guide:* use the model's stated units and bounds, do not round intermediate conversions prematurely, and explicitly label every calculated number synthetic.

**Exercise C — falsification and control.** Design a modest experiment for **constructing and propagating an uncertainty budget** with a procedural blank or reference, three independent physical specimens where meaningful, one orthogonal measurement and a predefined exclusion rule. State a possible observation that makes your favored inference untenable. *Answer guide:* record material processing and measurement history, separate technical repeats from sample repeats, and require that the independent test distinguishes competing hypotheses.

**Discussion and decision.** Which correlation or calibration experiment would change the declared uncertainty budget most strongly? Give one conclusion supported directly by a detector observable, one conclusion requiring a fitted model, and one conclusion that cannot yet be made at all. Finish with a single high-value next measurement and explain why its expected information is worth the cost.

## Lesson 8.2 — Design of experiments, controls and batch replication

### Physical mechanism and its measurable signature

A planned experimental design allocates measurements to factors such as processing temperature, annealing time, sample lot, position and instrument day. Randomization mitigates order effects, while blocks isolate batch or run-to-run variation. A control may be a known reference, an unprocessed material, a procedural blank or an independent method; each rejects a different artifact. Factorial designs can reveal interactions missed by one-variable-at-a-time comparisons, but replication and adequate sample size are still needed. Preregistration of primary metrics and exclusion rules reduces selective interpretation. Laboratory time is scarce, so the correct design maximizes information for the stated engineering decision.

**Explicit defining relation.** In a two-factor linear model y=β0+β1 A+β2 B+β3 AB+ε, the interaction β3 tests whether the effect of A depends on B.

### Concrete materials-characterization problem

Three operators each test specimens from one processing lot and claim reproducibility. Revise the plan to test future production lots without pseudoreplication.

### Reproducible synthetic worked example

The nearby interactive card titled **Probability of at least one detected rare defect** changes **Independent specimens**. The declared calculation is `100*(1-Math.pow(0.97,n))`; the model returns 61.1023144 % at 31 specimens and 71.3159081 % at 41 specimens. Thus as the displayed input grows across these two test settings, the calculated output increases. The secant sensitivity over this interval is 1.0213594 % per specimens. Check the sign from the governing equation rather than trusting the plotted curve, and confirm dimensional consistency before copying results to the case table. The method is a pedagogical sensitivity test, not a calibrated measurement of a commercial or laboratory specimen.

### Independent experimental and calibration plan

A realistic measurement study of **design of experiments, controls and batch replication** would begin with **traceable cross-method report with retained raw files**, retaining **complete provenance, hierarchical sample identifiers, control records, uncertainty model and reviewer checklist**. An independent check would use **blind reanalysis, hold-out specimen, process variation and an independent detection mode**.

### Threats to interpretation and a failure mode

Repeated instrument readings on one specimen do not demonstrate lot-level robustness, and a significant factor may be caused by measurement order.

### Exercises with solution guidance

**Exercise A — physical inference.** Starting from In a two-factor linear model y=β0+β1 A+β2 B+β3 AB+ε, the interaction β3 tests whether the effect of A depends on B. explain what is measured, what is inferred, the unit of every symbol and which environmental or microstructural assumption is most fragile. Then describe why the result of the same specimen measured before and after surface preparation might not be directly comparable. *Answer guide:* define the measurand before the apparatus, identify one calibration-dependent term, and test an alternative physical cause rather than listing properties of the equipment.

**Exercise B — numerical and uncertainty check.** Independently calculate the two numbers in **Probability of at least one detected rare defect: 31 specimens → 61.102314 %; 41 specimens → 71.315908 %** and estimate the local sensitivity at the midpoint. Choose an illustrative input standard uncertainty and propagate it using a first-order derivative; identify at least one source of model uncertainty not included by this arithmetic. *Answer guide:* use the model's stated units and bounds, do not round intermediate conversions prematurely, and explicitly label every calculated number synthetic.

**Exercise C — falsification and control.** Design a modest experiment for **design of experiments, controls and batch replication** with a procedural blank or reference, three independent physical specimens where meaningful, one orthogonal measurement and a predefined exclusion rule. State a possible observation that makes your favored inference untenable. *Answer guide:* record material processing and measurement history, separate technical repeats from sample repeats, and require that the independent test distinguishes competing hypotheses.

**Discussion and decision.** What randomized blocked design can distinguish processing batch from instrument-day drift? Give one conclusion supported directly by a detector observable, one conclusion requiring a fitted model, and one conclusion that cannot yet be made at all. Finish with a single high-value next measurement and explain why its expected information is worth the cost.

<!-- MODEL_14 -->

## Lesson 8.3 — Multimodal evidence and orthogonal validation

### Physical mechanism and its measurable signature

Combining XRD, microscopy, spectroscopy and property testing can reduce ambiguity only when each method addresses a different inference. XRD supports long-range order; XPS probes a surface-sensitive chemical environment; electron imaging probes local morphology; mechanical testing probes response of a specimen volume and geometry. Agreement among plots created from the same segmentation or baseline algorithm is not independent validation. When measurements conflict, first compare sampling depths, specimen state, time and the underlying operational definitions. Define a falsification matrix listing predictions under each plausible material mechanism and each artifact mechanism.

**Explicit defining relation.** Posterior odds ∝ prior odds × likelihood ratio is a conceptual framing for evidence updates, not a substitute for a specified statistical model.

### Concrete materials-characterization problem

A sample looks phase-pure by XRD, chemically mixed by XPS and heterogeneous by SEM. Explain how amorphous interfaces and measurement depths can coexist.

### Reproducible synthetic worked example

The nearby interactive card titled **Independent quadrature uncertainty** changes **Type A standard uncertainty**. The declared calculation is `Math.sqrt(u*u+4)`; the model returns 2.87116701 units at 2.06 units and 3.24075608 units at 2.55 units. Thus as the displayed input grows across these two test settings, the calculated output increases. The secant sensitivity over this interval is 0.75426342 units per units. Check the sign from the governing equation rather than trusting the plotted curve, and confirm dimensional consistency before copying results to the case table. The method is a pedagogical sensitivity test, not a calibrated measurement of a commercial or laboratory specimen.

### Independent experimental and calibration plan

A realistic measurement study of **multimodal evidence and orthogonal validation** would begin with **traceable cross-method report with retained raw files**, retaining **complete provenance, hierarchical sample identifiers, control records, uncertainty model and reviewer checklist**. An independent check would use **blind reanalysis, hold-out specimen, process variation and an independent detection mode**.

### Threats to interpretation and a failure mode

Using many instruments does not compensate for measuring only the most favorable specimen or for shared calibration bias.

### Exercises with solution guidance

**Exercise A — physical inference.** Starting from Posterior odds ∝ prior odds × likelihood ratio is a conceptual framing for evidence updates, not a substitute for a specified statistical model. explain what is measured, what is inferred, the unit of every symbol and which environmental or microstructural assumption is most fragile. Then describe why the result of a calibration control against an unknown sample might not be directly comparable. *Answer guide:* define the measurand before the apparatus, identify one calibration-dependent term, and test an alternative physical cause rather than listing properties of the equipment.

**Exercise B — numerical and uncertainty check.** Independently calculate the two numbers in **Independent quadrature uncertainty: 2.06 units → 2.871167 units; 2.55 units → 3.2407561 units** and estimate the local sensitivity at the midpoint. Choose an illustrative input standard uncertainty and propagate it using a first-order derivative; identify at least one source of model uncertainty not included by this arithmetic. *Answer guide:* use the model's stated units and bounds, do not round intermediate conversions prematurely, and explicitly label every calculated number synthetic.

**Exercise C — falsification and control.** Design a modest experiment for **multimodal evidence and orthogonal validation** with a procedural blank or reference, three independent physical specimens where meaningful, one orthogonal measurement and a predefined exclusion rule. State a possible observation that makes your favored inference untenable. *Answer guide:* record material processing and measurement history, separate technical repeats from sample repeats, and require that the independent test distinguishes competing hypotheses.

**Discussion and decision.** Name one truly orthogonal result that would change the preferred explanation rather than merely repeat the same observation. Give one conclusion supported directly by a detector observable, one conclusion requiring a fitted model, and one conclusion that cannot yet be made at all. Finish with a single high-value next measurement and explain why its expected information is worth the cost.

## Lesson 8.4 — Fitting, model selection and overinterpretation

### Physical mechanism and its measurable signature

Fitting translates measured signals into parameters only through assumptions about peak shapes, baseline, noise and physical constraints. Overparameterization produces strong-looking residual statistics and weak identifiability. Fit diagnostics should include residual structure, confidence or credible regions, parameter correlations and a physical plausibility check. Hold-out samples or alternative acquisition conditions can test model prediction instead of descriptive interpolation. For peaks near detector resolution, a fitted narrow width may be controlled almost entirely by the instrument kernel. Where multiple models fit equally well, report the ambiguity rather than promoting a single elegant explanation.

**Explicit defining relation.** Weighted least squares minimizes χ²=Σ[(y_i−f(x_i;θ))/σ_i]² when σ_i credibly describes independent measurement uncertainty.

### Concrete materials-characterization problem

A three-peak Raman deconvolution fits better than two peaks, but the extra peak varies unpredictably with smoothing window. Test whether the parameter is identifiable.

### Reproducible synthetic worked example

The nearby interactive card titled **Probability of at least one detected rare defect** changes **Independent specimens**. The declared calculation is `100*(1-Math.pow(0.97,n))`; the model returns 78.1934625 % at 50 specimens and 83.9193331 % at 60 specimens. Thus as the displayed input grows across these two test settings, the calculated output increases. The secant sensitivity over this interval is 0.57258706 % per specimens. Check the sign from the governing equation rather than trusting the plotted curve, and confirm dimensional consistency before copying results to the case table. The method is a pedagogical sensitivity test, not a calibrated measurement of a commercial or laboratory specimen.

### Independent experimental and calibration plan

A realistic measurement study of **fitting, model selection and overinterpretation** would begin with **traceable cross-method report with retained raw files**, retaining **complete provenance, hierarchical sample identifiers, control records, uncertainty model and reviewer checklist**. An independent check would use **blind reanalysis, hold-out specimen, process variation and an independent detection mode**.

### Threats to interpretation and a failure mode

A small residual does not guarantee that each fitted component is a real chemical species or a stable physical parameter.

### Exercises with solution guidance

**Exercise A — physical inference.** Starting from Weighted least squares minimizes χ²=Σ[(y_i−f(x_i;θ))/σ_i]² when σ_i credibly describes independent measurement uncertainty. explain what is measured, what is inferred, the unit of every symbol and which environmental or microstructural assumption is most fragile. Then describe why the result of one carefully chosen field against randomized spatial fields might not be directly comparable. *Answer guide:* define the measurand before the apparatus, identify one calibration-dependent term, and test an alternative physical cause rather than listing properties of the equipment.

**Exercise B — numerical and uncertainty check.** Independently calculate the two numbers in **Probability of at least one detected rare defect: 50 specimens → 78.193462 %; 60 specimens → 83.919333 %** and estimate the local sensitivity at the midpoint. Choose an illustrative input standard uncertainty and propagate it using a first-order derivative; identify at least one source of model uncertainty not included by this arithmetic. *Answer guide:* use the model's stated units and bounds, do not round intermediate conversions prematurely, and explicitly label every calculated number synthetic.

**Exercise C — falsification and control.** Design a modest experiment for **fitting, model selection and overinterpretation** with a procedural blank or reference, three independent physical specimens where meaningful, one orthogonal measurement and a predefined exclusion rule. State a possible observation that makes your favored inference untenable. *Answer guide:* record material processing and measurement history, separate technical repeats from sample repeats, and require that the independent test distinguishes competing hypotheses.

**Discussion and decision.** Which residual plot and independent acquisition condition would invalidate the preferred peak model? Give one conclusion supported directly by a detector observable, one conclusion requiring a fitted model, and one conclusion that cannot yet be made at all. Finish with a single high-value next measurement and explain why its expected information is worth the cost.

<!-- MODEL_15 -->

## Lesson 8.5 — FAIR records, safety, peer review and responsible publication

### Physical mechanism and its measurable signature

A characterization report should preserve raw datasets, sample metadata, software versions, processing notebooks, calibration records, uncertainty budgets and a map of which figure derives from which file. Machine-readable tables require units, column definitions and explicit provenance; synthetic examples must be permanently labeled as synthetic. FAIR principles improve discovery and reuse but do not guarantee scientific validity. Handle radioactive sources, X-rays, electron beams, vacuum systems, cryogens, strong magnets, lasers, chemical etchants and solvents under the appropriate approved laboratory procedures. Peer review and uncertainty disclosure protect subsequent researchers from treating unvalidated computational exercises as empirical reference data.

**Explicit defining relation.** A complete measurement record links specimen ID → acquisition file → calibration → preprocessing → inference → uncertainty → final claim.

### Concrete materials-characterization problem

A team proposes to publish an XPS phase map with only processed JPEGs and no acquisition log. Write a minimal corrective data-release checklist.

### Reproducible synthetic worked example

The nearby interactive card titled **Independent quadrature uncertainty** changes **Type A standard uncertainty**. The declared calculation is `Math.sqrt(u*u+4)`; the model returns 3.63890093 units at 3.04 units and 4.05720347 units at 3.53 units. Thus as the displayed input grows across these two test settings, the calculated output increases. The secant sensitivity over this interval is 0.85367865 units per units. Check the sign from the governing equation rather than trusting the plotted curve, and confirm dimensional consistency before copying results to the case table. The method is a pedagogical sensitivity test, not a calibrated measurement of a commercial or laboratory specimen.

### Independent experimental and calibration plan

A realistic measurement study of **fair records, safety, peer review and responsible publication** would begin with **traceable cross-method report with retained raw files**, retaining **complete provenance, hierarchical sample identifiers, control records, uncertainty model and reviewer checklist**. An independent check would use **blind reanalysis, hold-out specimen, process variation and an independent detection mode**.

### Threats to interpretation and a failure mode

Public figures without raw signal and sample identifiers are difficult to audit; even open datasets can be irreproducible if calibration and fitting choices are undocumented.

### Exercises with solution guidance

**Exercise A — physical inference.** Starting from A complete measurement record links specimen ID → acquisition file → calibration → preprocessing → inference → uncertainty → final claim. explain what is measured, what is inferred, the unit of every symbol and which environmental or microstructural assumption is most fragile. Then describe why the result of one instrument mode against a complementary physical mode might not be directly comparable. *Answer guide:* define the measurand before the apparatus, identify one calibration-dependent term, and test an alternative physical cause rather than listing properties of the equipment.

**Exercise B — numerical and uncertainty check.** Independently calculate the two numbers in **Independent quadrature uncertainty: 3.04 units → 3.6389009 units; 3.53 units → 4.0572035 units** and estimate the local sensitivity at the midpoint. Choose an illustrative input standard uncertainty and propagate it using a first-order derivative; identify at least one source of model uncertainty not included by this arithmetic. *Answer guide:* use the model's stated units and bounds, do not round intermediate conversions prematurely, and explicitly label every calculated number synthetic.

**Exercise C — falsification and control.** Design a modest experiment for **fair records, safety, peer review and responsible publication** with a procedural blank or reference, three independent physical specimens where meaningful, one orthogonal measurement and a predefined exclusion rule. State a possible observation that makes your favored inference untenable. *Answer guide:* record material processing and measurement history, separate technical repeats from sample repeats, and require that the independent test distinguishes competing hypotheses.

**Discussion and decision.** Specify the smallest independently reproducible evidence package required to support the main result of the capstone. Give one conclusion supported directly by a detector observable, one conclusion requiring a fitted model, and one conclusion that cannot yet be made at all. Finish with a single high-value next measurement and explain why its expected information is worth the cost.

## Unit 8 capstone — evidence review and design defense

**Investigation.** A university team claims a novel multifunctional nanocomposite from XRD, SEM, Raman and tensile tests. Audit the data lineage and propose the smallest extra experiment that could overturn the central claim.

1. **Specify a measurable claim.** Define the target parameter and where the specimens come from. Identify why the sampling population rather than the number of images matters for the engineering claim.
2. **Build a methods matrix.** Choose at least three complementary measurements for **data fusion, validation and reproducible scientific reporting**. For each report the instrument signal, calibration, spatial or information depth, most likely artifact and an orthogonal verification strategy.
3. **Audit two numerical models.** For both cards, calculate the default value, an endpoint and a sensitivity. Mark every quantity synthetic. Explain why agreement with its ideal formula is not sufficient for independent validation.
4. **Budget uncertainty and confounders.** Separate repeatability, reference calibration, specimen variability, geometry and data-reduction sensitivity. Include a possible correlated error and a case where a high pixel count is misleading.
5. **Make an evidence-limited decision.** Write 250 words separating directly supported observations from inferred structure or function. State precisely what additional result would reverse the proposed interpretation.

### Synthesis and transferable reasoning

A characterization workflow is useful when it turns a defined problem into falsifiable evidence. The same specimen can look different when probe volume, preparation, temperature, analysis background or inversion model changes. In **data fusion, validation and reproducible scientific reporting**, the central skill is not knowing a long list of instruments; it is matching each claim to a physically appropriate observable and understanding how to challenge that inference. A laboratory report should acknowledge the subset of the population sampled, not imply that a selected image or a synthetic curve describes every possible specimen. Favor a chain of traceable data over a single polished figure.

