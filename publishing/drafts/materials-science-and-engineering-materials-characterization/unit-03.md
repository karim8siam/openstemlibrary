# Unit 3: X-ray diffraction, scattering and phase quantification

**Core research question.** What structural information is encoded in diffraction peaks, and what cannot be deduced without a defensible instrument model?

## Physical context and prerequisite reasoning

Diffraction samples periodic order through constructive interference; peak positions reflect lattice spacings, peak widths reflect several broadening mechanisms, and intensities combine structure, texture, absorption, geometry and instrument response. Scattering patterns can reveal periodicity or nanoscale morphology without uniquely reconstructing the atomic arrangement. Radiation safety and instrument authorization matter for any real laboratory demonstration. This unit distinguishes crystallographic inference from convenient profile fitting.

A fundamental distinction in **X-ray diffraction, scattering and phase quantification** is the difference between what the instrument records and what one wants to infer. Design a chain of explanation containing a specimen with a known history, a measurable interaction, a recorded signal, one or more corrections, a model or reference, and the qualified property estimate. State which component could change when the operator selects another location, detector or processing program. In materials science an instrument often averages over a volume, while a proposed mechanism may live at an interface or individual defect. That mismatch can make a precise measurement irrelevant. This unit therefore emphasizes independent samples, documented acquisition conditions and physical counterexamples rather than applying formulae mechanically.

## Investigative exercise for the entire unit

Two batches of oxide powder show broader diffraction peaks after milling. Determine whether smaller coherent domains, residual strain, instrument broadening, altered texture or phase changes could explain the observation.

## Lesson 3.1 — Bragg diffraction and reciprocal-space geometry

### Physical mechanism and its measurable signature

Constructive interference from a family of lattice planes requires a path-length difference consistent with an integer wavelength. In powder diffractometry a detector typically reports intensity versus scattering angle 2θ; the Bragg angle θ is half the listed angle. Interplanar spacing depends on wavelength and angle, while a reciprocal-lattice description handles more complex scattering geometries. A tiny zero offset or sample displacement may shift many peaks together. Indexing a peak requires multiple reflections and consistent symmetry, not matching a single isolated maximum to a database value. Peak assignment should also consider fluorescence and amorphous contributions.

**Explicit defining relation.** First-order Bragg relation: 2 d sin θ=λ; for reported 2θ, use θ=(2θ)/2 before computing d.

### Concrete materials-characterization problem

An undergraduate uses a 44-degree 2θ peak as if 44 degrees were θ. Compute how this error changes the inferred spacing and phase assignment.

### Reproducible synthetic worked example

The nearby interactive card titled **Bragg interplanar spacing** changes **Scattering angle 2θ**. The declared calculation is `1.5406/(2*Math.sin(twoTheta*Math.PI/360))`; the model returns 2.36601765 Å at 38 degrees and 2.03433993 Å at 44.5 degrees. Thus as the displayed input grows across these two test settings, the calculated output decreases. The secant sensitivity over this interval is -0.051027342 Å per degrees. Check the sign from the governing equation rather than trusting the plotted curve, and confirm dimensional consistency before copying results to the case table. The method is a pedagogical sensitivity test, not a calibrated measurement of a commercial or laboratory specimen.

### Independent experimental and calibration plan

A realistic measurement study of **bragg diffraction and reciprocal-space geometry** would begin with **powder or film X-ray diffraction with instrument reference**, retaining **2θ, intensity, instrumental peak shape, beam wavelength, holder background and sample displacement**. An independent check would use **internal standard, alternative measurement geometry and orthogonal compositional check**.

### Threats to interpretation and a failure mode

One d-spacing is rarely unique to one mineral or crystalline phase. Background peaks from holders and K-alpha doublets complicate matching.

### Exercises with solution guidance

**Exercise A — physical inference.** Starting from First-order Bragg relation: 2 d sin θ=λ; for reported 2θ, use θ=(2θ)/2 before computing d. explain what is measured, what is inferred, the unit of every symbol and which environmental or microstructural assumption is most fragile. Then describe why the result of one carefully chosen field against randomized spatial fields might not be directly comparable. *Answer guide:* define the measurand before the apparatus, identify one calibration-dependent term, and test an alternative physical cause rather than listing properties of the equipment.

**Exercise B — numerical and uncertainty check.** Independently calculate the two numbers in **Bragg interplanar spacing: 38 degrees → 2.3660177 Å; 44.5 degrees → 2.0343399 Å** and estimate the local sensitivity at the midpoint. Choose an illustrative input standard uncertainty and propagate it using a first-order derivative; identify at least one source of model uncertainty not included by this arithmetic. *Answer guide:* use the model's stated units and bounds, do not round intermediate conversions prematurely, and explicitly label every calculated number synthetic.

**Exercise C — falsification and control.** Design a modest experiment for **bragg diffraction and reciprocal-space geometry** with a procedural blank or reference, three independent physical specimens where meaningful, one orthogonal measurement and a predefined exclusion rule. State a possible observation that makes your favored inference untenable. *Answer guide:* record material processing and measurement history, separate technical repeats from sample repeats, and require that the independent test distinguishes competing hypotheses.

**Discussion and decision.** Specify a calibration scan and a second reflection that could falsify the proposed cubic lattice parameter. Give one conclusion supported directly by a detector observable, one conclusion requiring a fitted model, and one conclusion that cannot yet be made at all. Finish with a single high-value next measurement and explain why its expected information is worth the cost.

## Lesson 3.2 — Powder patterns, indexing and lattice parameters

### Physical mechanism and its measurable signature

An ideal powder contains many randomly oriented crystallites and presents diffraction rings or peaks from families of lattice planes. Preferred orientation reweights intensities, while finite particle statistics can produce poor averaging in coarse powders. Cubic lattice spacing obeys 1/d_hkl²=(h²+k²+l²)/a², but lower symmetry requires the appropriate metric tensor. Peak identification proceeds with a consistent list of reflections, systematic absences and a plausible chemical system. An internal standard can help reveal sample displacement and instrumental zero shift, provided it is truly inert toward the specimen.

**Explicit defining relation.** For a cubic crystal, a=d_hkl sqrt(h²+k²+l²); the assigned Miller indices must be crystallographically allowed.

### Concrete materials-characterization problem

A powder pattern apparently indexes as face-centered cubic, but a weak forbidden peak remains. Test impurity, contamination, symmetry and detector artifact explanations.

### Reproducible synthetic worked example

The nearby interactive card titled **Scherrer coherent-domain peak width** changes **Coherent domain length**. The declared calculation is `(0.9*0.15406/(L*Math.cos(20*Math.PI/180)))*(180/Math.PI)`; the model returns 0.196607809 degrees of 2θ at 43 nm and 0.15655807 degrees of 2θ at 54 nm. Thus as the displayed input grows across these two test settings, the calculated output decreases. The secant sensitivity over this interval is -0.0036408854 degrees of 2θ per nm. Check the sign from the governing equation rather than trusting the plotted curve, and confirm dimensional consistency before copying results to the case table. The method is a pedagogical sensitivity test, not a calibrated measurement of a commercial or laboratory specimen.

### Independent experimental and calibration plan

A realistic measurement study of **powder patterns, indexing and lattice parameters** would begin with **powder or film X-ray diffraction with instrument reference**, retaining **2θ, intensity, instrumental peak shape, beam wavelength, holder background and sample displacement**. An independent check would use **internal standard, alternative measurement geometry and orthogonal compositional check**.

### Threats to interpretation and a failure mode

Successful fitting of the largest peaks is not sufficient for an unambiguous structure solution. Unknown texture can spoil quantitative intensity comparisons.

### Exercises with solution guidance

**Exercise A — physical inference.** Starting from For a cubic crystal, a=d_hkl sqrt(h²+k²+l²); the assigned Miller indices must be crystallographically allowed. explain what is measured, what is inferred, the unit of every symbol and which environmental or microstructural assumption is most fragile. Then describe why the result of one instrument mode against a complementary physical mode might not be directly comparable. *Answer guide:* define the measurand before the apparatus, identify one calibration-dependent term, and test an alternative physical cause rather than listing properties of the equipment.

**Exercise B — numerical and uncertainty check.** Independently calculate the two numbers in **Scherrer coherent-domain peak width: 43 nm → 0.19660781 degrees of 2θ; 54 nm → 0.15655807 degrees of 2θ** and estimate the local sensitivity at the midpoint. Choose an illustrative input standard uncertainty and propagate it using a first-order derivative; identify at least one source of model uncertainty not included by this arithmetic. *Answer guide:* use the model's stated units and bounds, do not round intermediate conversions prematurely, and explicitly label every calculated number synthetic.

**Exercise C — falsification and control.** Design a modest experiment for **powder patterns, indexing and lattice parameters** with a procedural blank or reference, three independent physical specimens where meaningful, one orthogonal measurement and a predefined exclusion rule. State a possible observation that makes your favored inference untenable. *Answer guide:* record material processing and measurement history, separate technical repeats from sample repeats, and require that the independent test distinguishes competing hypotheses.

**Discussion and decision.** How would rotating a coarse-grained specimen expose a non-random orientation distribution? Give one conclusion supported directly by a detector observable, one conclusion requiring a fitted model, and one conclusion that cannot yet be made at all. Finish with a single high-value next measurement and explain why its expected information is worth the cost.

<!-- MODEL_4 -->

## Lesson 3.3 — Peak width, crystallite domains and microstrain

### Physical mechanism and its measurable signature

Finite coherent scattering domains broaden peaks in a manner inversely related to characteristic domain size, while strain distributions can introduce additional angle-dependent broadening. Instrument resolution must be removed using an appropriate line-shape model before assigning sample broadening. The Scherrer relation estimates coherent domain extent, not necessarily whole particle diameter; a polycrystalline aggregate can be much larger than one coherent domain. Williamson–Hall style approximations separate some size and strain trends only under model assumptions. Peak asymmetry, anisotropic size, stacking faults and K-alpha splitting can invalidate simplistic linear plots.

**Explicit defining relation.** In an idealized size-broadening model β≈Kλ/(L cos θ), with β in radians, K a shape factor and L a coherent-domain length.

### Concrete materials-characterization problem

An SEM micrograph shows 600 nm agglomerates while Scherrer analysis gives 25 nm. Explain why the methods need not disagree and what TEM evidence could clarify domains.

### Reproducible synthetic worked example

The nearby interactive card titled **Bragg interplanar spacing** changes **Scattering angle 2θ**. The declared calculation is `1.5406/(2*Math.sin(twoTheta*Math.PI/360))`; the model returns 1.78926863 Å at 51 degrees and 1.6014927 Å at 57.5 degrees. Thus as the displayed input grows across these two test settings, the calculated output decreases. The secant sensitivity over this interval is -0.028888605 Å per degrees. Check the sign from the governing equation rather than trusting the plotted curve, and confirm dimensional consistency before copying results to the case table. The method is a pedagogical sensitivity test, not a calibrated measurement of a commercial or laboratory specimen.

### Independent experimental and calibration plan

A realistic measurement study of **peak width, crystallite domains and microstrain** would begin with **powder or film X-ray diffraction with instrument reference**, retaining **2θ, intensity, instrumental peak shape, beam wavelength, holder background and sample displacement**. An independent check would use **internal standard, alternative measurement geometry and orthogonal compositional check**.

### Threats to interpretation and a failure mode

Raw full width at half maximum cannot be inserted as sample-only broadening without subtracting instrument contributions using a justified profile model.

### Exercises with solution guidance

**Exercise A — physical inference.** Starting from In an idealized size-broadening model β≈Kλ/(L cos θ), with β in radians, K a shape factor and L a coherent-domain length. explain what is measured, what is inferred, the unit of every symbol and which environmental or microstructural assumption is most fragile. Then describe why the result of two independent specimens against repeated readings of one specimen might not be directly comparable. *Answer guide:* define the measurand before the apparatus, identify one calibration-dependent term, and test an alternative physical cause rather than listing properties of the equipment.

**Exercise B — numerical and uncertainty check.** Independently calculate the two numbers in **Bragg interplanar spacing: 51 degrees → 1.7892686 Å; 57.5 degrees → 1.6014927 Å** and estimate the local sensitivity at the midpoint. Choose an illustrative input standard uncertainty and propagate it using a first-order derivative; identify at least one source of model uncertainty not included by this arithmetic. *Answer guide:* use the model's stated units and bounds, do not round intermediate conversions prematurely, and explicitly label every calculated number synthetic.

**Exercise C — falsification and control.** Design a modest experiment for **peak width, crystallite domains and microstrain** with a procedural blank or reference, three independent physical specimens where meaningful, one orthogonal measurement and a predefined exclusion rule. State a possible observation that makes your favored inference untenable. *Answer guide:* record material processing and measurement history, separate technical repeats from sample repeats, and require that the independent test distinguishes competing hypotheses.

**Discussion and decision.** Design a standard-specimen scan that would distinguish a sample broadening effect from instrumental resolution. Give one conclusion supported directly by a detector observable, one conclusion requiring a fitted model, and one conclusion that cannot yet be made at all. Finish with a single high-value next measurement and explain why its expected information is worth the cost.

## Lesson 3.4 — Whole-pattern refinement and quantitative phase analysis

### Physical mechanism and its measurable signature

Whole-pattern fitting uses a structural or profile model over an angular range and adjusts parameters such as lattice constants, peak shapes, background and scale factors. A low residual does not prove unique phase identification: excessive parameters can absorb incorrect structures, preferred orientation or noncrystalline background. Rietveld refinement uses crystal structures, whereas methods such as Pawley fitting can handle peak positions and profiles without atomic structure factors. Quantitative phase fractions require reliable absorption and intensity models, and may need an internal standard for amorphous content. Refinement uncertainty estimates can be optimistic when structural model inadequacy is ignored.

**Explicit defining relation.** Weighted profile residual R_wp=[Σ w_i(y_i,obs−y_i,calc)²/Σ w_i y_i,obs²]^(1/2), meaningful only with the fitting assumptions and weights disclosed.

### Concrete materials-characterization problem

A refinement reports 98% crystalline phase A, yet microscopy reveals amorphous glass between grains. Explain how an internal standard may reveal the missing fraction.

### Reproducible synthetic worked example

The nearby interactive card titled **Scherrer coherent-domain peak width** changes **Coherent domain length**. The declared calculation is `(0.9*0.15406/(L*Math.cos(20*Math.PI/180)))*(180/Math.PI)`; the model returns 0.130063627 degrees of 2θ at 65 nm and 0.111238629 degrees of 2θ at 76 nm. Thus as the displayed input grows across these two test settings, the calculated output decreases. The secant sensitivity over this interval is -0.0017113635 degrees of 2θ per nm. Check the sign from the governing equation rather than trusting the plotted curve, and confirm dimensional consistency before copying results to the case table. The method is a pedagogical sensitivity test, not a calibrated measurement of a commercial or laboratory specimen.

### Independent experimental and calibration plan

A realistic measurement study of **whole-pattern refinement and quantitative phase analysis** would begin with **powder or film X-ray diffraction with instrument reference**, retaining **2θ, intensity, instrumental peak shape, beam wavelength, holder background and sample displacement**. An independent check would use **internal standard, alternative measurement geometry and orthogonal compositional check**.

### Threats to interpretation and a failure mode

A visually excellent fit can be achieved with incorrect parameter correlations, background models and physically impossible occupancies.

### Exercises with solution guidance

**Exercise A — physical inference.** Starting from Weighted profile residual R_wp=[Σ w_i(y_i,obs−y_i,calc)²/Σ w_i y_i,obs²]^(1/2), meaningful only with the fitting assumptions and weights disclosed. explain what is measured, what is inferred, the unit of every symbol and which environmental or microstructural assumption is most fragile. Then describe why the result of a shallow probe against a volume-sensitive probe might not be directly comparable. *Answer guide:* define the measurand before the apparatus, identify one calibration-dependent term, and test an alternative physical cause rather than listing properties of the equipment.

**Exercise B — numerical and uncertainty check.** Independently calculate the two numbers in **Scherrer coherent-domain peak width: 65 nm → 0.13006363 degrees of 2θ; 76 nm → 0.11123863 degrees of 2θ** and estimate the local sensitivity at the midpoint. Choose an illustrative input standard uncertainty and propagate it using a first-order derivative; identify at least one source of model uncertainty not included by this arithmetic. *Answer guide:* use the model's stated units and bounds, do not round intermediate conversions prematurely, and explicitly label every calculated number synthetic.

**Exercise C — falsification and control.** Design a modest experiment for **whole-pattern refinement and quantitative phase analysis** with a procedural blank or reference, three independent physical specimens where meaningful, one orthogonal measurement and a predefined exclusion rule. State a possible observation that makes your favored inference untenable. *Answer guide:* record material processing and measurement history, separate technical repeats from sample repeats, and require that the independent test distinguishes competing hypotheses.

**Discussion and decision.** Which held-out reflection region or independent chemical method would most effectively challenge a fitted phase fraction? Give one conclusion supported directly by a detector observable, one conclusion requiring a fitted model, and one conclusion that cannot yet be made at all. Finish with a single high-value next measurement and explain why its expected information is worth the cost.

<!-- MODEL_5 -->

## Lesson 3.5 — Thin films, reflectometry and small-angle scattering

### Physical mechanism and its measurable signature

X-ray reflectometry estimates layered electron-density profiles using interference fringes and model-dependent roughness terms. It is sensitive to thickness, density contrast and interfaces but can exhibit parameter tradeoffs. Grazing-incidence diffraction changes penetration and orientation sensitivity for thin coatings; small-angle scattering probes nanoscale contrast and statistical morphology rather than directly producing a unique particle image. Sample curvature and background subtracting matter for weak films, and a distribution of shapes can generate similar scattering curves. A microscopy-based thickness cross-check makes fitted values less ambiguous.

**Explicit defining relation.** For ideal interference from a uniform film, approximate thickness t≈2π/Δq_z for fringe spacing Δq_z in reciprocal length.

### Concrete materials-characterization problem

A film reflectivity curve supports two fits: a thicker low-density layer and a thinner denser layer. Propose independent ellipsometry or cross-section measurements.

### Reproducible synthetic worked example

The nearby interactive card titled **Bragg interplanar spacing** changes **Scattering angle 2θ**. The declared calculation is `1.5406/(2*Math.sin(twoTheta*Math.PI/360))`; the model returns 1.45361766 Å at 64 degrees and 1.33467282 Å at 70.5 degrees. Thus as the displayed input grows across these two test settings, the calculated output decreases. The secant sensitivity over this interval is -0.018299205 Å per degrees. Check the sign from the governing equation rather than trusting the plotted curve, and confirm dimensional consistency before copying results to the case table. The method is a pedagogical sensitivity test, not a calibrated measurement of a commercial or laboratory specimen.

### Independent experimental and calibration plan

A realistic measurement study of **thin films, reflectometry and small-angle scattering** would begin with **powder or film X-ray diffraction with instrument reference**, retaining **2θ, intensity, instrumental peak shape, beam wavelength, holder background and sample displacement**. An independent check would use **internal standard, alternative measurement geometry and orthogonal compositional check**.

### Threats to interpretation and a failure mode

Specular reflection assumes suitable lateral homogeneity and a tractable layer model; roughness and compositional intermixing may be correlated in fits.

### Exercises with solution guidance

**Exercise A — physical inference.** Starting from For ideal interference from a uniform film, approximate thickness t≈2π/Δq_z for fringe spacing Δq_z in reciprocal length. explain what is measured, what is inferred, the unit of every symbol and which environmental or microstructural assumption is most fragile. Then describe why the result of a model-generated trend against an actual controlled test might not be directly comparable. *Answer guide:* define the measurand before the apparatus, identify one calibration-dependent term, and test an alternative physical cause rather than listing properties of the equipment.

**Exercise B — numerical and uncertainty check.** Independently calculate the two numbers in **Bragg interplanar spacing: 64 degrees → 1.4536177 Å; 70.5 degrees → 1.3346728 Å** and estimate the local sensitivity at the midpoint. Choose an illustrative input standard uncertainty and propagate it using a first-order derivative; identify at least one source of model uncertainty not included by this arithmetic. *Answer guide:* use the model's stated units and bounds, do not round intermediate conversions prematurely, and explicitly label every calculated number synthetic.

**Exercise C — falsification and control.** Design a modest experiment for **thin films, reflectometry and small-angle scattering** with a procedural blank or reference, three independent physical specimens where meaningful, one orthogonal measurement and a predefined exclusion rule. State a possible observation that makes your favored inference untenable. *Answer guide:* record material processing and measurement history, separate technical repeats from sample repeats, and require that the independent test distinguishes competing hypotheses.

**Discussion and decision.** What observation would force the use of a graded-density profile instead of a single uniform film? Give one conclusion supported directly by a detector observable, one conclusion requiring a fitted model, and one conclusion that cannot yet be made at all. Finish with a single high-value next measurement and explain why its expected information is worth the cost.

## Unit 3 capstone — evidence review and design defense

**Investigation.** Two batches of oxide powder show broader diffraction peaks after milling. Determine whether smaller coherent domains, residual strain, instrument broadening, altered texture or phase changes could explain the observation.

1. **Specify a measurable claim.** Define the target parameter and where the specimens come from. Identify why the sampling population rather than the number of images matters for the engineering claim.
2. **Build a methods matrix.** Choose at least three complementary measurements for **x-ray diffraction, scattering and phase quantification**. For each report the instrument signal, calibration, spatial or information depth, most likely artifact and an orthogonal verification strategy.
3. **Audit two numerical models.** For both cards, calculate the default value, an endpoint and a sensitivity. Mark every quantity synthetic. Explain why agreement with its ideal formula is not sufficient for independent validation.
4. **Budget uncertainty and confounders.** Separate repeatability, reference calibration, specimen variability, geometry and data-reduction sensitivity. Include a possible correlated error and a case where a high pixel count is misleading.
5. **Make an evidence-limited decision.** Write 250 words separating directly supported observations from inferred structure or function. State precisely what additional result would reverse the proposed interpretation.

### Synthesis and transferable reasoning

A characterization workflow is useful when it turns a defined problem into falsifiable evidence. The same specimen can look different when probe volume, preparation, temperature, analysis background or inversion model changes. In **x-ray diffraction, scattering and phase quantification**, the central skill is not knowing a long list of instruments; it is matching each claim to a physically appropriate observable and understanding how to challenge that inference. A laboratory report should acknowledge the subset of the population sampled, not imply that a selected image or a synthetic curve describes every possible specimen. Favor a chain of traceable data over a single polished figure.

