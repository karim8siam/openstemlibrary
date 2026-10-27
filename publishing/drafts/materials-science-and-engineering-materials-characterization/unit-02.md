# Unit 2: Optical microscopy and scanning electron methods

**Core research question.** How can images and local chemical signals be converted into quantitative microstructure evidence without mistaking contrast for composition?

## Physical context and prerequisite reasoning

Microscopy uses interactions of waves or particle beams with a prepared specimen. Contrast can depend on topography, refractive index, absorption, crystallographic orientation, atomic number, charging and detector geometry. A visually striking change may indicate a different acquisition setting rather than a different material. Reporting requires accelerating voltage or optical illumination, probe conditions, working distance, detector, calibration, specimen preparation, field coordinates, magnification, pixel size, and representative sampling.

A fundamental distinction in **Optical microscopy and scanning electron methods** is the difference between what the instrument records and what one wants to infer. Design a chain of explanation containing a specimen with a known history, a measurable interaction, a recorded signal, one or more corrections, a model or reference, and the qualified property estimate. State which component could change when the operator selects another location, detector or processing program. In materials science an instrument often averages over a volume, while a proposed mechanism may live at an interface or individual defect. That mismatch can make a precise measurement irrelevant. This unit therefore emphasizes independent samples, documented acquisition conditions and physical counterexamples rather than applying formulae mechanically.

## Investigative exercise for the entire unit

A fractured metal sample presents dark spots in scanning electron images. Devise a workflow to determine whether the spots are pores, pull-outs, inclusions, contamination or detector-shadow artifacts, using microscopy and chemical mapping.

## Lesson 2.1 — Optical microscopy and contrast mechanisms

### Physical mechanism and its measurable signature

Bright-field, dark-field, polarized-light and differential-interference approaches reveal different parts of a specimen's optical response. Reflected-light metallography reveals grain boundaries after suitable contrast development, but boundary visibility can depend strongly on etch time and illumination. A microscope objective is characterized by numerical aperture, wavelength-dependent diffraction response and working distance; magnification without sufficient numerical aperture makes larger blurry images rather than new information. Quantitative micrographs require a scale traceable to a stage or optical calibration and a declared segmentation rule. The same polished sample may contain scratches whose apparent orientation mimics microstructural alignment.

**Explicit defining relation.** For ideal incoherent diffraction-limited imaging, lateral resolution is often approximated by d≈0.61 λ/NA, with wavelength and d in the same units.

### Concrete materials-characterization problem

Two metallographic laboratories report different grain sizes after changing etchant, exposure time and objective NA. Identify which differences could be photographic rather than physical.

### Reproducible synthetic worked example

The nearby interactive card titled **Diffraction-limited optical lateral resolution** changes **Illumination wavelength**. The declared calculation is `0.61*lambda_nm/0.8`; the model returns 358.375 nm at 470 nm and 385.0625 nm at 505 nm. Thus as the displayed input grows across these two test settings, the calculated output increases. The secant sensitivity over this interval is 0.7625 nm per nm. Check the sign from the governing equation rather than trusting the plotted curve, and confirm dimensional consistency before copying results to the case table. The method is a pedagogical sensitivity test, not a calibrated measurement of a commercial or laboratory specimen.

### Independent experimental and calibration plan

A realistic measurement study of **optical microscopy and contrast mechanisms** would begin with **optical and electron images with matched sample coordinates**, retaining **beam and detector settings, image scale, step size, image raw format and surface preparation**. An independent check would use **replicate random fields, reference grating and complementary detector modes**.

### Threats to interpretation and a failure mode

A resolved grain boundary in a selected field does not prove a homogeneous grain-size distribution across the specimen. Optical contrast is not chemical identification.

### Exercises with solution guidance

**Exercise A — physical inference.** Starting from For ideal incoherent diffraction-limited imaging, lateral resolution is often approximated by d≈0.61 λ/NA, with wavelength and d in the same units. explain what is measured, what is inferred, the unit of every symbol and which environmental or microstructural assumption is most fragile. Then describe why the result of a calibration control against an unknown sample might not be directly comparable. *Answer guide:* define the measurand before the apparatus, identify one calibration-dependent term, and test an alternative physical cause rather than listing properties of the equipment.

**Exercise B — numerical and uncertainty check.** Independently calculate the two numbers in **Diffraction-limited optical lateral resolution: 470 nm → 358.375 nm; 505 nm → 385.0625 nm** and estimate the local sensitivity at the midpoint. Choose an illustrative input standard uncertainty and propagate it using a first-order derivative; identify at least one source of model uncertainty not included by this arithmetic. *Answer guide:* use the model's stated units and bounds, do not round intermediate conversions prematurely, and explicitly label every calculated number synthetic.

**Exercise C — falsification and control.** Design a modest experiment for **optical microscopy and contrast mechanisms** with a procedural blank or reference, three independent physical specimens where meaningful, one orthogonal measurement and a predefined exclusion rule. State a possible observation that makes your favored inference untenable. *Answer guide:* record material processing and measurement history, separate technical repeats from sample repeats, and require that the independent test distinguishes competing hypotheses.

**Discussion and decision.** How can a stage micrometer and a known microstructure standard be used to challenge a claimed feature size? Give one conclusion supported directly by a detector observable, one conclusion requiring a fitted model, and one conclusion that cannot yet be made at all. Finish with a single high-value next measurement and explain why its expected information is worth the cost.

## Lesson 2.2 — Scanning electron microscopy and electron–solid interactions

### Physical mechanism and its measurable signature

A focused primary electron beam generates secondary electrons, backscattered electrons and characteristic X-rays across a finite interaction volume. Secondary-electron signals usually emphasize surface morphology while backscattered-electron contrast can be influenced by composition and crystal orientation. Lower accelerating voltage may reduce interaction depth for some materials but can also worsen signal, charge accumulation or detector efficiency. Working distance, tilt, beam current, scan dwell and stage stability change apparent sharpness and contrast. An insulating surface can charge, shifting emitted trajectories and producing streaks or false brightness; coatings applied to reduce charging can obscure surface chemistry.

**Explicit defining relation.** Detector counts in a stationary linear regime can scale as N≈R t for count rate R and acquisition dwell t, while counting noise is approximately sqrt(N).

### Concrete materials-characterization problem

A polymer surface appears striped at high magnification but the stripes move after changing scan direction. Decide whether charging or drift is more plausible than manufacturing texture.

### Reproducible synthetic worked example

The nearby interactive card titled **Sampling pixel pitch** changes **Image field width**. The declared calculation is `1000*W/2048`; the model returns 36.1328125 nm/pixel at 74 µm and 44.921875 nm/pixel at 92 µm. Thus as the displayed input grows across these two test settings, the calculated output increases. The secant sensitivity over this interval is 0.48828125 nm/pixel per µm. Check the sign from the governing equation rather than trusting the plotted curve, and confirm dimensional consistency before copying results to the case table. The method is a pedagogical sensitivity test, not a calibrated measurement of a commercial or laboratory specimen.

### Independent experimental and calibration plan

A realistic measurement study of **scanning electron microscopy and electron–solid interactions** would begin with **optical and electron images with matched sample coordinates**, retaining **beam and detector settings, image scale, step size, image raw format and surface preparation**. An independent check would use **replicate random fields, reference grating and complementary detector modes**.

### Threats to interpretation and a failure mode

Backscattered-bright regions are not automatically a unique phase; morphology, orientation, topography and charging can influence detector response.

### Exercises with solution guidance

**Exercise A — physical inference.** Starting from Detector counts in a stationary linear regime can scale as N≈R t for count rate R and acquisition dwell t, while counting noise is approximately sqrt(N). explain what is measured, what is inferred, the unit of every symbol and which environmental or microstructural assumption is most fragile. Then describe why the result of one carefully chosen field against randomized spatial fields might not be directly comparable. *Answer guide:* define the measurand before the apparatus, identify one calibration-dependent term, and test an alternative physical cause rather than listing properties of the equipment.

**Exercise B — numerical and uncertainty check.** Independently calculate the two numbers in **Sampling pixel pitch: 74 µm → 36.132812 nm/pixel; 92 µm → 44.921875 nm/pixel** and estimate the local sensitivity at the midpoint. Choose an illustrative input standard uncertainty and propagate it using a first-order derivative; identify at least one source of model uncertainty not included by this arithmetic. *Answer guide:* use the model's stated units and bounds, do not round intermediate conversions prematurely, and explicitly label every calculated number synthetic.

**Exercise C — falsification and control.** Design a modest experiment for **scanning electron microscopy and electron–solid interactions** with a procedural blank or reference, three independent physical specimens where meaningful, one orthogonal measurement and a predefined exclusion rule. State a possible observation that makes your favored inference untenable. *Answer guide:* record material processing and measurement history, separate technical repeats from sample repeats, and require that the independent test distinguishes competing hypotheses.

**Discussion and decision.** Specify a beam-voltage series and a scan reversal that would expose an imaging artifact. Give one conclusion supported directly by a detector observable, one conclusion requiring a fitted model, and one conclusion that cannot yet be made at all. Finish with a single high-value next measurement and explain why its expected information is worth the cost.

<!-- MODEL_2 -->

## Lesson 2.3 — EDS and wavelength-dispersive microanalysis

### Physical mechanism and its measurable signature

Energy-dispersive X-ray spectroscopy detects characteristic radiation and its continuum background. Peak positions support elemental assignments while peak areas require background removal, detector-efficiency correction and matrix-dependent absorption, fluorescence and atomic-number corrections for reliable quantification. Overlapping lines, low-energy absorption, rough surfaces and a large interaction volume complicate microanalysis. Wavelength-dispersive methods can provide superior spectral resolution at different acquisition and instrumentation costs. When comparing a particle and its matrix, image the beam footprint and report whether the interaction volume extends beyond the particle.

**Explicit defining relation.** In an idealized count-limited channel, relative counting uncertainty scales approximately as 1/sqrt(N) for net independent counts N; background subtraction adds uncertainty.

### Concrete materials-characterization problem

A small dark inclusion gives a strong oxygen signal and a carbon signal, but the sample was carbon-coated and mounted in epoxy. Decide which conclusions require controls.

### Reproducible synthetic worked example

The nearby interactive card titled **Diffraction-limited optical lateral resolution** changes **Illumination wavelength**. The declared calculation is `0.61*lambda_nm/0.8`; the model returns 411.75 nm at 540 nm and 438.4375 nm at 575 nm. Thus as the displayed input grows across these two test settings, the calculated output increases. The secant sensitivity over this interval is 0.7625 nm per nm. Check the sign from the governing equation rather than trusting the plotted curve, and confirm dimensional consistency before copying results to the case table. The method is a pedagogical sensitivity test, not a calibrated measurement of a commercial or laboratory specimen.

### Independent experimental and calibration plan

A realistic measurement study of **eds and wavelength-dispersive microanalysis** would begin with **optical and electron images with matched sample coordinates**, retaining **beam and detector settings, image scale, step size, image raw format and surface preparation**. An independent check would use **replicate random fields, reference grating and complementary detector modes**.

### Threats to interpretation and a failure mode

EDS generally cannot determine oxidation state solely from an element peak; an apparently precise atomic percentage can hide large matrix errors.

### Exercises with solution guidance

**Exercise A — physical inference.** Starting from In an idealized count-limited channel, relative counting uncertainty scales approximately as 1/sqrt(N) for net independent counts N; background subtraction adds uncertainty. explain what is measured, what is inferred, the unit of every symbol and which environmental or microstructural assumption is most fragile. Then describe why the result of one instrument mode against a complementary physical mode might not be directly comparable. *Answer guide:* define the measurand before the apparatus, identify one calibration-dependent term, and test an alternative physical cause rather than listing properties of the equipment.

**Exercise B — numerical and uncertainty check.** Independently calculate the two numbers in **Diffraction-limited optical lateral resolution: 540 nm → 411.75 nm; 575 nm → 438.4375 nm** and estimate the local sensitivity at the midpoint. Choose an illustrative input standard uncertainty and propagate it using a first-order derivative; identify at least one source of model uncertainty not included by this arithmetic. *Answer guide:* use the model's stated units and bounds, do not round intermediate conversions prematurely, and explicitly label every calculated number synthetic.

**Exercise C — falsification and control.** Design a modest experiment for **eds and wavelength-dispersive microanalysis** with a procedural blank or reference, three independent physical specimens where meaningful, one orthogonal measurement and a predefined exclusion rule. State a possible observation that makes your favored inference untenable. *Answer guide:* record material processing and measurement history, separate technical repeats from sample repeats, and require that the independent test distinguishes competing hypotheses.

**Discussion and decision.** What reference and blank measurements would help separate carbon from the coating, mounting medium and actual inclusion? Give one conclusion supported directly by a detector observable, one conclusion requiring a fitted model, and one conclusion that cannot yet be made at all. Finish with a single high-value next measurement and explain why its expected information is worth the cost.

## Lesson 2.4 — EBSD orientation maps and grain-boundary analysis

### Physical mechanism and its measurable signature

Electron backscatter diffraction uses Kikuchi patterns to infer local crystal orientation and sometimes phase. A map comprises indexed points with step size, confidence metrics, pattern quality and a chosen grain reconstruction threshold. Polishing deformation, surface damage, crystal symmetry, beam geometry and pseudosymmetry affect indexing. An orientation map can show texture, misorientation and geometrically necessary lattice curvature, but it does not directly count dislocation density without substantial modeling assumptions. A grain boundary angle threshold can merge or divide grains; published grain sizes must disclose threshold and cleanup operations.

**Explicit defining relation.** For a reconstructed grain map, area-equivalent diameter is d_eq=sqrt(4A/π); A depends on segmentation and sampling.

### Concrete materials-characterization problem

An EBSD map shows fine grains only after aggressive interpolation removes unindexed points. Construct a sensitivity analysis on cleanup settings and step size.

### Reproducible synthetic worked example

The nearby interactive card titled **Sampling pixel pitch** changes **Image field width**. The declared calculation is `1000*W/2048`; the model returns 53.7109375 nm/pixel at 110 µm and 62.5 nm/pixel at 128 µm. Thus as the displayed input grows across these two test settings, the calculated output increases. The secant sensitivity over this interval is 0.48828125 nm/pixel per µm. Check the sign from the governing equation rather than trusting the plotted curve, and confirm dimensional consistency before copying results to the case table. The method is a pedagogical sensitivity test, not a calibrated measurement of a commercial or laboratory specimen.

### Independent experimental and calibration plan

A realistic measurement study of **ebsd orientation maps and grain-boundary analysis** would begin with **optical and electron images with matched sample coordinates**, retaining **beam and detector settings, image scale, step size, image raw format and surface preparation**. An independent check would use **replicate random fields, reference grating and complementary detector modes**.

### Threats to interpretation and a failure mode

Color in an inverse-pole-figure map represents orientation under a selected convention, not intrinsic chemical phase composition.

### Exercises with solution guidance

**Exercise A — physical inference.** Starting from For a reconstructed grain map, area-equivalent diameter is d_eq=sqrt(4A/π); A depends on segmentation and sampling. explain what is measured, what is inferred, the unit of every symbol and which environmental or microstructural assumption is most fragile. Then describe why the result of two independent specimens against repeated readings of one specimen might not be directly comparable. *Answer guide:* define the measurand before the apparatus, identify one calibration-dependent term, and test an alternative physical cause rather than listing properties of the equipment.

**Exercise B — numerical and uncertainty check.** Independently calculate the two numbers in **Sampling pixel pitch: 110 µm → 53.710938 nm/pixel; 128 µm → 62.5 nm/pixel** and estimate the local sensitivity at the midpoint. Choose an illustrative input standard uncertainty and propagate it using a first-order derivative; identify at least one source of model uncertainty not included by this arithmetic. *Answer guide:* use the model's stated units and bounds, do not round intermediate conversions prematurely, and explicitly label every calculated number synthetic.

**Exercise C — falsification and control.** Design a modest experiment for **ebsd orientation maps and grain-boundary analysis** with a procedural blank or reference, three independent physical specimens where meaningful, one orthogonal measurement and a predefined exclusion rule. State a possible observation that makes your favored inference untenable. *Answer guide:* record material processing and measurement history, separate technical repeats from sample repeats, and require that the independent test distinguishes competing hypotheses.

**Discussion and decision.** What alternative electron or optical measurement can test whether the EBSD grain size is artificially reduced? Give one conclusion supported directly by a detector observable, one conclusion requiring a fitted model, and one conclusion that cannot yet be made at all. Finish with a single high-value next measurement and explain why its expected information is worth the cost.

<!-- MODEL_3 -->

## Lesson 2.5 — Stereology, segmentation and unbiased image analysis

### Physical mechanism and its measurable signature

A two-dimensional slice samples a three-dimensional microstructure. Area fraction may estimate volume fraction for appropriate unbiased sections and sampling schemes, but particle number or diameter distributions cannot be recovered without geometric assumptions. Thresholding changes the fraction assigned to a phase; morphological opening can delete thin ligaments, and edge exclusion changes particle counts. Quantitative workflows should store raw files, preprocessing parameters, pixel calibration, analysis scripts and uncertainty due to region selection. A blinded threshold sensitivity analysis prevents tuning solely toward the expected answer. When a property depends on connectivity, simple phase fraction cannot replace topology measurements.

**Explicit defining relation.** For segmented area fraction f=A_phase/A_total, report the sampled area and positional variability, not merely a large pixel count.

### Concrete materials-characterization problem

Compare a coating with isolated rounded voids and another with the same segmented black area concentrated in a through-thickness crack.

### Reproducible synthetic worked example

The nearby interactive card titled **Diffraction-limited optical lateral resolution** changes **Illumination wavelength**. The declared calculation is `0.61*lambda_nm/0.8`; the model returns 465.125 nm at 610 nm and 491.8125 nm at 645 nm. Thus as the displayed input grows across these two test settings, the calculated output increases. The secant sensitivity over this interval is 0.7625 nm per nm. Check the sign from the governing equation rather than trusting the plotted curve, and confirm dimensional consistency before copying results to the case table. The method is a pedagogical sensitivity test, not a calibrated measurement of a commercial or laboratory specimen.

### Independent experimental and calibration plan

A realistic measurement study of **stereology, segmentation and unbiased image analysis** would begin with **optical and electron images with matched sample coordinates**, retaining **beam and detector settings, image scale, step size, image raw format and surface preparation**. An independent check would use **replicate random fields, reference grating and complementary detector modes**.

### Threats to interpretation and a failure mode

A 2D void area fraction is not evidence for 3D permeation path connectivity. Segmentation algorithms can create pores at scratches and shadow boundaries.

### Exercises with solution guidance

**Exercise A — physical inference.** Starting from For segmented area fraction f=A_phase/A_total, report the sampled area and positional variability, not merely a large pixel count. explain what is measured, what is inferred, the unit of every symbol and which environmental or microstructural assumption is most fragile. Then describe why the result of a shallow probe against a volume-sensitive probe might not be directly comparable. *Answer guide:* define the measurand before the apparatus, identify one calibration-dependent term, and test an alternative physical cause rather than listing properties of the equipment.

**Exercise B — numerical and uncertainty check.** Independently calculate the two numbers in **Diffraction-limited optical lateral resolution: 610 nm → 465.125 nm; 645 nm → 491.8125 nm** and estimate the local sensitivity at the midpoint. Choose an illustrative input standard uncertainty and propagate it using a first-order derivative; identify at least one source of model uncertainty not included by this arithmetic. *Answer guide:* use the model's stated units and bounds, do not round intermediate conversions prematurely, and explicitly label every calculated number synthetic.

**Exercise C — falsification and control.** Design a modest experiment for **stereology, segmentation and unbiased image analysis** with a procedural blank or reference, three independent physical specimens where meaningful, one orthogonal measurement and a predefined exclusion rule. State a possible observation that makes your favored inference untenable. *Answer guide:* record material processing and measurement history, separate technical repeats from sample repeats, and require that the independent test distinguishes competing hypotheses.

**Discussion and decision.** What 3D or serial-section test would invalidate a conclusion drawn from one polished cross section? Give one conclusion supported directly by a detector observable, one conclusion requiring a fitted model, and one conclusion that cannot yet be made at all. Finish with a single high-value next measurement and explain why its expected information is worth the cost.

## Unit 2 capstone — evidence review and design defense

**Investigation.** A fractured metal sample presents dark spots in scanning electron images. Devise a workflow to determine whether the spots are pores, pull-outs, inclusions, contamination or detector-shadow artifacts, using microscopy and chemical mapping.

1. **Specify a measurable claim.** Define the target parameter and where the specimens come from. Identify why the sampling population rather than the number of images matters for the engineering claim.
2. **Build a methods matrix.** Choose at least three complementary measurements for **optical microscopy and scanning electron methods**. For each report the instrument signal, calibration, spatial or information depth, most likely artifact and an orthogonal verification strategy.
3. **Audit two numerical models.** For both cards, calculate the default value, an endpoint and a sensitivity. Mark every quantity synthetic. Explain why agreement with its ideal formula is not sufficient for independent validation.
4. **Budget uncertainty and confounders.** Separate repeatability, reference calibration, specimen variability, geometry and data-reduction sensitivity. Include a possible correlated error and a case where a high pixel count is misleading.
5. **Make an evidence-limited decision.** Write 250 words separating directly supported observations from inferred structure or function. State precisely what additional result would reverse the proposed interpretation.

### Synthesis and transferable reasoning

A characterization workflow is useful when it turns a defined problem into falsifiable evidence. The same specimen can look different when probe volume, preparation, temperature, analysis background or inversion model changes. In **optical microscopy and scanning electron methods**, the central skill is not knowing a long list of instruments; it is matching each claim to a physically appropriate observable and understanding how to challenge that inference. A laboratory report should acknowledge the subset of the population sampled, not imply that a selected image or a synthetic curve describes every possible specimen. Favor a chain of traceable data over a single polished figure.

