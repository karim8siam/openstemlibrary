# Unit 6: Transmission electron microscopy, scanning probes and three-dimensional imaging

**Core research question.** What added structural information arises from atomic-scale and volume-sensitive methods, and how do preparation and inversion assumptions restrict it?

## Physical context and prerequisite reasoning

Sub-nanometre microscopy, surface probes and tomography probe different physical quantities. TEM is a projection sensitive to thickness and diffraction; AFM follows tip–surface forces; computed tomography reconstructs an attenuation or phase contrast field from projections. Atomic resolution in one imaging mode does not make chemical composition or three-dimensional connectivity automatically known. Every reconstruction has transfer functions, missing information and finite dose or probing forces. The goal is to combine spatial resolution with defensible uncertainty and representative sampling.

A fundamental distinction in **Transmission electron microscopy, scanning probes and three-dimensional imaging** is the difference between what the instrument records and what one wants to infer. Design a chain of explanation containing a specimen with a known history, a measurable interaction, a recorded signal, one or more corrections, a model or reference, and the qualified property estimate. State which component could change when the operator selects another location, detector or processing program. In materials science an instrument often averages over a volume, while a proposed mechanism may live at an interface or individual defect. That mismatch can make a precise measurement irrelevant. This unit therefore emphasizes independent samples, documented acquisition conditions and physical counterexamples rather than applying formulae mechanically.

## Investigative exercise for the entire unit

An aerospace composite contains suspected nanovoids and a damaged interface. Choose a multiscale sequence of CT, TEM, AFM or spectroscopy that tests extent and cause while minimizing destructive selection bias.

## Lesson 6.1 — TEM, STEM and specimen thinning artifacts

### Physical mechanism and its measurable signature

Transmission electron microscopes pass high-energy electrons through a thin specimen; image contrast results from scattering, phase and detector geometry. Bright-field and dark-field TEM, scanning TEM detectors and analytical modes emphasize different structures. Specimen preparation may include focused ion beam thinning, mechanical thinning or ion milling, each of which can implant ions, amorphize regions or alter stress. Thickness variations and bending contours can resemble phase contrast. Strong electron doses can transform beam-sensitive materials; acquisition sequences should monitor dose and use a lower-dose reference when possible.

**Explicit defining relation.** A simple electron wavelength estimate uses λ=h/p in the de Broglie relation, with relativistic momentum at microscopy acceleration potentials.

### Concrete materials-characterization problem

A lamella shows an amorphous layer that grows between repeated TEM exposures. Separate as-manufactured damage, FIB preparation and beam-induced disorder.

### Reproducible synthetic worked example

The nearby interactive card titled **Calibrated AFM cantilever force** changes **Cantilever deflection**. The declared calculation is `2*delta`; the model returns 33.6 nN at 16.8 nm and 49.4 nN at 24.7 nm. Thus as the displayed input grows across these two test settings, the calculated output increases. The secant sensitivity over this interval is 2 nN per nm. Check the sign from the governing equation rather than trusting the plotted curve, and confirm dimensional consistency before copying results to the case table. The method is a pedagogical sensitivity test, not a calibrated measurement of a commercial or laboratory specimen.

### Independent experimental and calibration plan

A realistic measurement study of **tem, stem and specimen thinning artifacts** would begin with **dose or force calibrated nanoscale imaging and 3D reconstruction**, retaining **image transfer, specimen thickness, probing force, voxel pitch, dose, reconstruction and segmentation settings**. An independent check would use **different specimen preparation, imaging mode and independent spatial cross-section**.

### Threats to interpretation and a failure mode

A thin lamella is not necessarily representative of the bulk, and an image dark fringe is not automatically a grain boundary or defect plane.

### Exercises with solution guidance

**Exercise A — physical inference.** Starting from A simple electron wavelength estimate uses λ=h/p in the de Broglie relation, with relativistic momentum at microscopy acceleration potentials. explain what is measured, what is inferred, the unit of every symbol and which environmental or microstructural assumption is most fragile. Then describe why the result of a shallow probe against a volume-sensitive probe might not be directly comparable. *Answer guide:* define the measurand before the apparatus, identify one calibration-dependent term, and test an alternative physical cause rather than listing properties of the equipment.

**Exercise B — numerical and uncertainty check.** Independently calculate the two numbers in **Calibrated AFM cantilever force: 16.8 nm → 33.6 nN; 24.7 nm → 49.4 nN** and estimate the local sensitivity at the midpoint. Choose an illustrative input standard uncertainty and propagate it using a first-order derivative; identify at least one source of model uncertainty not included by this arithmetic. *Answer guide:* use the model's stated units and bounds, do not round intermediate conversions prematurely, and explicitly label every calculated number synthetic.

**Exercise C — falsification and control.** Design a modest experiment for **tem, stem and specimen thinning artifacts** with a procedural blank or reference, three independent physical specimens where meaningful, one orthogonal measurement and a predefined exclusion rule. State a possible observation that makes your favored inference untenable. *Answer guide:* record material processing and measurement history, separate technical repeats from sample repeats, and require that the independent test distinguishes competing hypotheses.

**Discussion and decision.** What low-dose or alternate-preparation comparison would most clearly expose microscopy-induced damage? Give one conclusion supported directly by a detector observable, one conclusion requiring a fitted model, and one conclusion that cannot yet be made at all. Finish with a single high-value next measurement and explain why its expected information is worth the cost.

## Lesson 6.2 — Electron diffraction and atomic-resolution imaging

### Physical mechanism and its measurable signature

Selected-area and nanobeam diffraction reveal projected reciprocal-space information and local crystallographic orientation. High-resolution images contain phase-contrast fringes influenced by defocus, thickness and aberrations, not direct photographs of nuclei. A Fourier transform can reveal periodic components but needs indexing and calibration. Distinguish measured lattice-fringe spacing from crystal structure assignment; multiple crystals or dynamic scattering may generate complex spot patterns. Simulated contrast and thickness series help test a structural interpretation, particularly when comparing lattice fringes at buried interfaces.

**Explicit defining relation.** The reciprocal-vector magnitude g_hkl=1/d_hkl; diffraction-camera calibration converts pixel radius to scattering vector.

### Concrete materials-characterization problem

A researcher identifies a new crystalline phase from two lattice fringes in one high-resolution image. Specify the required independent evidence.

### Reproducible synthetic worked example

The nearby interactive card titled **Tomography nominal voxel pitch** changes **Reconstruction field of view**. The declared calculation is `1000*W/1024`; the model returns 9.47265625 µm/voxel at 9.7 mm and 12.3046875 µm/voxel at 12.6 mm. Thus as the displayed input grows across these two test settings, the calculated output increases. The secant sensitivity over this interval is 0.9765625 µm/voxel per mm. Check the sign from the governing equation rather than trusting the plotted curve, and confirm dimensional consistency before copying results to the case table. The method is a pedagogical sensitivity test, not a calibrated measurement of a commercial or laboratory specimen.

### Independent experimental and calibration plan

A realistic measurement study of **electron diffraction and atomic-resolution imaging** would begin with **dose or force calibrated nanoscale imaging and 3D reconstruction**, retaining **image transfer, specimen thickness, probing force, voxel pitch, dose, reconstruction and segmentation settings**. An independent check would use **different specimen preparation, imaging mode and independent spatial cross-section**.

### Threats to interpretation and a failure mode

Contrast inversions caused by defocus can make dark and bright atomic-column sites swap appearance, so brightness cannot be read as atom count without modeling.

### Exercises with solution guidance

**Exercise A — physical inference.** Starting from The reciprocal-vector magnitude g_hkl=1/d_hkl; diffraction-camera calibration converts pixel radius to scattering vector. explain what is measured, what is inferred, the unit of every symbol and which environmental or microstructural assumption is most fragile. Then describe why the result of a model-generated trend against an actual controlled test might not be directly comparable. *Answer guide:* define the measurand before the apparatus, identify one calibration-dependent term, and test an alternative physical cause rather than listing properties of the equipment.

**Exercise B — numerical and uncertainty check.** Independently calculate the two numbers in **Tomography nominal voxel pitch: 9.7 mm → 9.4726562 µm/voxel; 12.6 mm → 12.304688 µm/voxel** and estimate the local sensitivity at the midpoint. Choose an illustrative input standard uncertainty and propagate it using a first-order derivative; identify at least one source of model uncertainty not included by this arithmetic. *Answer guide:* use the model's stated units and bounds, do not round intermediate conversions prematurely, and explicitly label every calculated number synthetic.

**Exercise C — falsification and control.** Design a modest experiment for **electron diffraction and atomic-resolution imaging** with a procedural blank or reference, three independent physical specimens where meaningful, one orthogonal measurement and a predefined exclusion rule. State a possible observation that makes your favored inference untenable. *Answer guide:* record material processing and measurement history, separate technical repeats from sample repeats, and require that the independent test distinguishes competing hypotheses.

**Discussion and decision.** How would specimen tilt, a selected-area pattern and an independent chemistry map falsify the alleged new phase? Give one conclusion supported directly by a detector observable, one conclusion requiring a fitted model, and one conclusion that cannot yet be made at all. Finish with a single high-value next measurement and explain why its expected information is worth the cost.

<!-- MODEL_10 -->

## Lesson 6.3 — Atomic force microscopy and force spectroscopy

### Physical mechanism and its measurable signature

An AFM cantilever senses tip–sample interactions while a feedback loop records apparent surface height or a related signal. Topographic images are convolutions of true geometry and finite tip shape; narrow trenches often appear wider or shallower than they are. Contact, tapping and force-mapping modes differ in sample disturbance and measurement response. Cantilever spring constants and optical-lever sensitivity require calibration before force curves can yield quantitative stiffness or adhesion. Capillary forces and humidity can dominate apparently simple ambient measurements; soft samples may deform under the tip.

**Explicit defining relation.** Small-deflection Hooke approximation F=kδ for cantilever stiffness k and deflection δ, prior to nonlinear contact effects.

### Concrete materials-characterization problem

An AFM image shows 15 nm particles but the size grows as the probe wears. Show how reference gratings and tip imaging separate growth from convolution.

### Reproducible synthetic worked example

The nearby interactive card titled **Calibrated AFM cantilever force** changes **Cantilever deflection**. The declared calculation is `2*delta`; the model returns 65.2 nN at 32.6 nm and 81 nN at 40.5 nm. Thus as the displayed input grows across these two test settings, the calculated output increases. The secant sensitivity over this interval is 2 nN per nm. Check the sign from the governing equation rather than trusting the plotted curve, and confirm dimensional consistency before copying results to the case table. The method is a pedagogical sensitivity test, not a calibrated measurement of a commercial or laboratory specimen.

### Independent experimental and calibration plan

A realistic measurement study of **atomic force microscopy and force spectroscopy** would begin with **dose or force calibrated nanoscale imaging and 3D reconstruction**, retaining **image transfer, specimen thickness, probing force, voxel pitch, dose, reconstruction and segmentation settings**. An independent check would use **different specimen preparation, imaging mode and independent spatial cross-section**.

### Threats to interpretation and a failure mode

A topographic height map should not be described as an atomically resolved chemical map; lateral dimensions are broadened by probe geometry.

### Exercises with solution guidance

**Exercise A — physical inference.** Starting from Small-deflection Hooke approximation F=kδ for cantilever stiffness k and deflection δ, prior to nonlinear contact effects. explain what is measured, what is inferred, the unit of every symbol and which environmental or microstructural assumption is most fragile. Then describe why the result of a response measured across two excitation or environmental conditions might not be directly comparable. *Answer guide:* define the measurand before the apparatus, identify one calibration-dependent term, and test an alternative physical cause rather than listing properties of the equipment.

**Exercise B — numerical and uncertainty check.** Independently calculate the two numbers in **Calibrated AFM cantilever force: 32.6 nm → 65.2 nN; 40.5 nm → 81 nN** and estimate the local sensitivity at the midpoint. Choose an illustrative input standard uncertainty and propagate it using a first-order derivative; identify at least one source of model uncertainty not included by this arithmetic. *Answer guide:* use the model's stated units and bounds, do not round intermediate conversions prematurely, and explicitly label every calculated number synthetic.

**Exercise C — falsification and control.** Design a modest experiment for **atomic force microscopy and force spectroscopy** with a procedural blank or reference, three independent physical specimens where meaningful, one orthogonal measurement and a predefined exclusion rule. State a possible observation that makes your favored inference untenable. *Answer guide:* record material processing and measurement history, separate technical repeats from sample repeats, and require that the independent test distinguishes competing hypotheses.

**Discussion and decision.** Which repeated reference grating and force-curve check would reveal a damaged or poorly calibrated tip? Give one conclusion supported directly by a detector observable, one conclusion requiring a fitted model, and one conclusion that cannot yet be made at all. Finish with a single high-value next measurement and explain why its expected information is worth the cost.

## Lesson 6.4 — X-ray computed tomography and voxel segmentation

### Physical mechanism and its measurable signature

CT reconstructs a volumetric attenuation field from multiple angular projections. Voxel dimension depends on geometry, but effective spatial resolution is governed by detector blur, source spot, reconstruction and sample motion. Beam hardening produces artificial density gradients in polychromatic systems, while rings can come from detector nonuniformity. Segmentation determines measured pore volumes and connectivity, and conclusions can change rapidly near the resolution limit. A representative volume element must contain sufficient structural variability; scanning an attractive corner of the sample is not an unbiased characterization of a complete part.

**Explicit defining relation.** For reconstructed field of view W and N voxels along an axis, nominal pitch is Δx=W/N; physical resolving power is generally worse than one pitch.

### Concrete materials-characterization problem

A printed metal lattice reports 1% porosity by CT, but metallography reports 3%. Determine whether sub-voxel pores and threshold choices can reconcile the measurements.

### Reproducible synthetic worked example

The nearby interactive card titled **Tomography nominal voxel pitch** changes **Reconstruction field of view**. The declared calculation is `1000*W/1024`; the model returns 15.1367188 µm/voxel at 15.5 mm and 17.96875 µm/voxel at 18.4 mm. Thus as the displayed input grows across these two test settings, the calculated output increases. The secant sensitivity over this interval is 0.9765625 µm/voxel per mm. Check the sign from the governing equation rather than trusting the plotted curve, and confirm dimensional consistency before copying results to the case table. The method is a pedagogical sensitivity test, not a calibrated measurement of a commercial or laboratory specimen.

### Independent experimental and calibration plan

A realistic measurement study of **x-ray computed tomography and voxel segmentation** would begin with **dose or force calibrated nanoscale imaging and 3D reconstruction**, retaining **image transfer, specimen thickness, probing force, voxel pitch, dose, reconstruction and segmentation settings**. An independent check would use **different specimen preparation, imaging mode and independent spatial cross-section**.

### Threats to interpretation and a failure mode

An empty-looking voxel does not guarantee the absence of smaller voids. A reconstruction with small voxels is not necessarily a high-resolution measurement.

### Exercises with solution guidance

**Exercise A — physical inference.** Starting from For reconstructed field of view W and N voxels along an axis, nominal pitch is Δx=W/N; physical resolving power is generally worse than one pitch. explain what is measured, what is inferred, the unit of every symbol and which environmental or microstructural assumption is most fragile. Then describe why the result of the same specimen measured before and after surface preparation might not be directly comparable. *Answer guide:* define the measurand before the apparatus, identify one calibration-dependent term, and test an alternative physical cause rather than listing properties of the equipment.

**Exercise B — numerical and uncertainty check.** Independently calculate the two numbers in **Tomography nominal voxel pitch: 15.5 mm → 15.136719 µm/voxel; 18.4 mm → 17.96875 µm/voxel** and estimate the local sensitivity at the midpoint. Choose an illustrative input standard uncertainty and propagate it using a first-order derivative; identify at least one source of model uncertainty not included by this arithmetic. *Answer guide:* use the model's stated units and bounds, do not round intermediate conversions prematurely, and explicitly label every calculated number synthetic.

**Exercise C — falsification and control.** Design a modest experiment for **x-ray computed tomography and voxel segmentation** with a procedural blank or reference, three independent physical specimens where meaningful, one orthogonal measurement and a predefined exclusion rule. State a possible observation that makes your favored inference untenable. *Answer guide:* record material processing and measurement history, separate technical repeats from sample repeats, and require that the independent test distinguishes competing hypotheses.

**Discussion and decision.** How can a manufactured pore phantom and destructive slice series establish a realistic CT detection threshold? Give one conclusion supported directly by a detector observable, one conclusion requiring a fitted model, and one conclusion that cannot yet be made at all. Finish with a single high-value next measurement and explain why its expected information is worth the cost.

<!-- MODEL_11 -->

## Lesson 6.5 — Atom probe tomography and nanoscale chemistry maps

### Physical mechanism and its measurable signature

Atom probe tomography reconstructs ion positions from field evaporation and time-of-flight mass-to-charge measurements. It can reveal nanoscale composition and clustering but depends on detector efficiency, trajectory reconstruction, field conditions, multiple-hit behavior and specimen shape assumptions. Preferential evaporation or local magnification can distort spatial positions; a reconstructed interface thickness is not automatically a true physical thickness. Correlative TEM and atom probe measurements are particularly useful for identifying precipitates and segregation. Because the analyzed volume is tiny, systematic specimen targeting and separate tips are needed before claiming representative bulk statistics.

**Explicit defining relation.** Local nominal concentration c=N_species/N_total depends on detection and identification efficiencies; a binomial error model needs independence and uniform selection.

### Concrete materials-characterization problem

An atom probe map shows a solute-rich cluster at one grain boundary. Develop a test to see if the finding generalizes to other boundaries or reflects reconstruction.

### Reproducible synthetic worked example

The nearby interactive card titled **Calibrated AFM cantilever force** changes **Cantilever deflection**. The declared calculation is `2*delta`; the model returns 96.8 nN at 48.4 nm and 112.6 nN at 56.3 nm. Thus as the displayed input grows across these two test settings, the calculated output increases. The secant sensitivity over this interval is 2 nN per nm. Check the sign from the governing equation rather than trusting the plotted curve, and confirm dimensional consistency before copying results to the case table. The method is a pedagogical sensitivity test, not a calibrated measurement of a commercial or laboratory specimen.

### Independent experimental and calibration plan

A realistic measurement study of **atom probe tomography and nanoscale chemistry maps** would begin with **dose or force calibrated nanoscale imaging and 3D reconstruction**, retaining **image transfer, specimen thickness, probing force, voxel pitch, dose, reconstruction and segmentation settings**. An independent check would use **different specimen preparation, imaging mode and independent spatial cross-section**.

### Threats to interpretation and a failure mode

Raw ion counts and reconstructed atom positions cannot be treated as complete 100%-detection occupancy maps; detector efficiency and mass overlaps matter.

### Exercises with solution guidance

**Exercise A — physical inference.** Starting from Local nominal concentration c=N_species/N_total depends on detection and identification efficiencies; a binomial error model needs independence and uniform selection. explain what is measured, what is inferred, the unit of every symbol and which environmental or microstructural assumption is most fragile. Then describe why the result of a calibration control against an unknown sample might not be directly comparable. *Answer guide:* define the measurand before the apparatus, identify one calibration-dependent term, and test an alternative physical cause rather than listing properties of the equipment.

**Exercise B — numerical and uncertainty check.** Independently calculate the two numbers in **Calibrated AFM cantilever force: 48.4 nm → 96.8 nN; 56.3 nm → 112.6 nN** and estimate the local sensitivity at the midpoint. Choose an illustrative input standard uncertainty and propagate it using a first-order derivative; identify at least one source of model uncertainty not included by this arithmetic. *Answer guide:* use the model's stated units and bounds, do not round intermediate conversions prematurely, and explicitly label every calculated number synthetic.

**Exercise C — falsification and control.** Design a modest experiment for **atom probe tomography and nanoscale chemistry maps** with a procedural blank or reference, three independent physical specimens where meaningful, one orthogonal measurement and a predefined exclusion rule. State a possible observation that makes your favored inference untenable. *Answer guide:* record material processing and measurement history, separate technical repeats from sample repeats, and require that the independent test distinguishes competing hypotheses.

**Discussion and decision.** Which multiple-tip and correlative microscopy measurements would most challenge a proposed solute-segregation mechanism? Give one conclusion supported directly by a detector observable, one conclusion requiring a fitted model, and one conclusion that cannot yet be made at all. Finish with a single high-value next measurement and explain why its expected information is worth the cost.

## Unit 6 capstone — evidence review and design defense

**Investigation.** An aerospace composite contains suspected nanovoids and a damaged interface. Choose a multiscale sequence of CT, TEM, AFM or spectroscopy that tests extent and cause while minimizing destructive selection bias.

1. **Specify a measurable claim.** Define the target parameter and where the specimens come from. Identify why the sampling population rather than the number of images matters for the engineering claim.
2. **Build a methods matrix.** Choose at least three complementary measurements for **transmission electron microscopy, scanning probes and three-dimensional imaging**. For each report the instrument signal, calibration, spatial or information depth, most likely artifact and an orthogonal verification strategy.
3. **Audit two numerical models.** For both cards, calculate the default value, an endpoint and a sensitivity. Mark every quantity synthetic. Explain why agreement with its ideal formula is not sufficient for independent validation.
4. **Budget uncertainty and confounders.** Separate repeatability, reference calibration, specimen variability, geometry and data-reduction sensitivity. Include a possible correlated error and a case where a high pixel count is misleading.
5. **Make an evidence-limited decision.** Write 250 words separating directly supported observations from inferred structure or function. State precisely what additional result would reverse the proposed interpretation.

### Synthesis and transferable reasoning

A characterization workflow is useful when it turns a defined problem into falsifiable evidence. The same specimen can look different when probe volume, preparation, temperature, analysis background or inversion model changes. In **transmission electron microscopy, scanning probes and three-dimensional imaging**, the central skill is not knowing a long list of instruments; it is matching each claim to a physically appropriate observable and understanding how to challenge that inference. A laboratory report should acknowledge the subset of the population sampled, not imply that a selected image or a synthetic curve describes every possible specimen. Favor a chain of traceable data over a single polished figure.

