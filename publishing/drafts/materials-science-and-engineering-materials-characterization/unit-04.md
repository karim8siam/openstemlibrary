# Unit 4: Spectroscopy, surface analysis and chemical identity

**Core research question.** How can spectroscopy identify elements, bonds and interfaces while controlling for depth sensitivity, charging and spectral overlap?

## Physical context and prerequisite reasoning

Spectroscopic signals are convolutions of material response and an instrument transfer function. Binding energy, vibrational frequency, absorption and optical emission depend on selection rules and environment. Peak identities are hypotheses supported by reference data and sample-specific controls, not automatic outputs of peak-fitting software. Surface-sensitive methods must identify contamination from air exposure, cleaning and sputtering; bulk spectra can mask a chemically thin layer that drives corrosion or adhesion.

A fundamental distinction in **Spectroscopy, surface analysis and chemical identity** is the difference between what the instrument records and what one wants to infer. Design a chain of explanation containing a specimen with a known history, a measurable interaction, a recorded signal, one or more corrections, a model or reference, and the qualified property estimate. State which component could change when the operator selects another location, detector or processing program. In materials science an instrument often averages over a volume, while a proposed mechanism may live at an interface or individual defect. That mismatch can make a precise measurement irrelevant. This unit therefore emphasizes independent samples, documented acquisition conditions and physical counterexamples rather than applying formulae mechanically.

## Investigative exercise for the entire unit

A polymer coating fails an adhesion test after storage. Compare outer-surface XPS, vibrational spectroscopy and cross-sectional evidence to distinguish oxidation, contamination and interfacial defects.

## Lesson 4.1 — X-ray photoelectron spectroscopy: composition and chemical states

### Physical mechanism and its measurable signature

XPS irradiates a near-surface region with X-rays and analyzes photoelectron kinetic energies. Binding energies are inferred from photon energy, measured kinetic energy and work-function conventions; chemical shifts can reflect bonding but also charging and final-state effects. Depth sensitivity depends on attenuation length, emission angle, overlayer composition and roughness. Survey spectra identify elements in favorable conditions while high-resolution spectra resolve overlapping chemical states only with appropriate line-shape constraints and calibration. Adventitious carbon referencing is not universally reliable; the analyst should disclose the actual energy-reference method.

**Explicit defining relation.** Simplified overlayer attenuation: I/I0≈exp[−t/(λ_eff cos α)], where α is emission angle relative to surface normal and roughness is neglected.

### Concrete materials-characterization problem

An oxide film shows a peak shifted toward higher binding energy after roughening. Test whether chemistry changed or nonuniform charging shifted the spectrum.

### Reproducible synthetic worked example

The nearby interactive card titled **Surface-photoelectron overlayer attenuation** changes **Overlayer thickness**. The declared calculation is `100*Math.exp(-t/(2.5*Math.cos(30*Math.PI/180)))`; the model returns 25.0163482 % remaining signal at 3 nm and 12.5122632 % remaining signal at 4.5 nm. Thus as the displayed input grows across these two test settings, the calculated output decreases. The secant sensitivity over this interval is -8.3360567 % remaining signal per nm. Check the sign from the governing equation rather than trusting the plotted curve, and confirm dimensional consistency before copying results to the case table. The method is a pedagogical sensitivity test, not a calibrated measurement of a commercial or laboratory specimen.

### Independent experimental and calibration plan

A realistic measurement study of **x-ray photoelectron spectroscopy: composition and chemical states** would begin with **survey and high-resolution spectra under calibrated conditions**, retaining **signal and background, spectral resolution, instrument energy axis, beam dose and overlayer history**. An independent check would use **chemical reference, low-damage acquisition and complementary surface or bulk-sensitive method**.

### Threats to interpretation and a failure mode

A fitted chemical component without physically justified constraints and reference spectra can reflect noise, backgrounds or charging rather than new bonding.

### Exercises with solution guidance

**Exercise A — physical inference.** Starting from Simplified overlayer attenuation: I/I0≈exp[−t/(λ_eff cos α)], where α is emission angle relative to surface normal and roughness is neglected. explain what is measured, what is inferred, the unit of every symbol and which environmental or microstructural assumption is most fragile. Then describe why the result of one instrument mode against a complementary physical mode might not be directly comparable. *Answer guide:* define the measurand before the apparatus, identify one calibration-dependent term, and test an alternative physical cause rather than listing properties of the equipment.

**Exercise B — numerical and uncertainty check.** Independently calculate the two numbers in **Surface-photoelectron overlayer attenuation: 3 nm → 25.016348 % remaining signal; 4.5 nm → 12.512263 % remaining signal** and estimate the local sensitivity at the midpoint. Choose an illustrative input standard uncertainty and propagate it using a first-order derivative; identify at least one source of model uncertainty not included by this arithmetic. *Answer guide:* use the model's stated units and bounds, do not round intermediate conversions prematurely, and explicitly label every calculated number synthetic.

**Exercise C — falsification and control.** Design a modest experiment for **x-ray photoelectron spectroscopy: composition and chemical states** with a procedural blank or reference, three independent physical specimens where meaningful, one orthogonal measurement and a predefined exclusion rule. State a possible observation that makes your favored inference untenable. *Answer guide:* record material processing and measurement history, separate technical repeats from sample repeats, and require that the independent test distinguishes competing hypotheses.

**Discussion and decision.** What conductive reference or instrument check can separate a global charge shift from a genuine chemical-state shift? Give one conclusion supported directly by a detector observable, one conclusion requiring a fitted model, and one conclusion that cannot yet be made at all. Finish with a single high-value next measurement and explain why its expected information is worth the cost.

## Lesson 4.2 — Auger spectroscopy, SIMS and depth profiling

### Physical mechanism and its measurable signature

Auger-electron spectroscopy uses electron kinetic energies associated with atomic relaxation and can provide local surface chemical information. Secondary-ion mass spectrometry ejects and analyzes ionic species, offering sensitive depth-dependent signatures but strong matrix effects and fragmentation. Quantitative concentration profiles require standards and sputter-rate calibration that match composition and structure. Ion bombardment can mix interfaces, preferentially sputter components, alter chemistry and roughen the surface. Apparent interdiffusion widths may therefore be instrument-limited rather than intrinsic material gradients.

**Explicit defining relation.** Depth estimate z≈r_sputter t assumes a steady sputter rate r_sputter, which can vary with layer composition and crater geometry.

### Concrete materials-characterization problem

SIMS shows a 20 nm-wide interface in a multilayer while TEM suggests an abrupt transition. Separate ion-beam mixing and true diffusion with altered sputtering conditions.

### Reproducible synthetic worked example

The nearby interactive card titled **Ideal Beer–Lambert absorbance** changes **Solute concentration**. The declared calculation is `25*c*1`; the model returns 0.75 absorbance at 0.03 mol/L and 1 absorbance at 0.04 mol/L. Thus as the displayed input grows across these two test settings, the calculated output increases. The secant sensitivity over this interval is 25 absorbance per mol/L. Check the sign from the governing equation rather than trusting the plotted curve, and confirm dimensional consistency before copying results to the case table. The method is a pedagogical sensitivity test, not a calibrated measurement of a commercial or laboratory specimen.

### Independent experimental and calibration plan

A realistic measurement study of **auger spectroscopy, sims and depth profiling** would begin with **survey and high-resolution spectra under calibrated conditions**, retaining **signal and background, spectral resolution, instrument energy axis, beam dose and overlayer history**. An independent check would use **chemical reference, low-damage acquisition and complementary surface or bulk-sensitive method**.

### Threats to interpretation and a failure mode

Ion count intensity is not automatically molar concentration; relative sensitivity factors and matrix chemistry must be validated.

### Exercises with solution guidance

**Exercise A — physical inference.** Starting from Depth estimate z≈r_sputter t assumes a steady sputter rate r_sputter, which can vary with layer composition and crater geometry. explain what is measured, what is inferred, the unit of every symbol and which environmental or microstructural assumption is most fragile. Then describe why the result of two independent specimens against repeated readings of one specimen might not be directly comparable. *Answer guide:* define the measurand before the apparatus, identify one calibration-dependent term, and test an alternative physical cause rather than listing properties of the equipment.

**Exercise B — numerical and uncertainty check.** Independently calculate the two numbers in **Ideal Beer–Lambert absorbance: 0.03 mol/L → 0.75 absorbance; 0.04 mol/L → 1 absorbance** and estimate the local sensitivity at the midpoint. Choose an illustrative input standard uncertainty and propagate it using a first-order derivative; identify at least one source of model uncertainty not included by this arithmetic. *Answer guide:* use the model's stated units and bounds, do not round intermediate conversions prematurely, and explicitly label every calculated number synthetic.

**Exercise C — falsification and control.** Design a modest experiment for **auger spectroscopy, sims and depth profiling** with a procedural blank or reference, three independent physical specimens where meaningful, one orthogonal measurement and a predefined exclusion rule. State a possible observation that makes your favored inference untenable. *Answer guide:* record material processing and measurement history, separate technical repeats from sample repeats, and require that the independent test distinguishes competing hypotheses.

**Discussion and decision.** What independent depth-calibration method could reveal preferential sputtering or nonuniform crater erosion? Give one conclusion supported directly by a detector observable, one conclusion requiring a fitted model, and one conclusion that cannot yet be made at all. Finish with a single high-value next measurement and explain why its expected information is worth the cost.

<!-- MODEL_6 -->

## Lesson 4.3 — Infrared and Raman vibrational spectroscopy

### Physical mechanism and its measurable signature

Infrared absorption requires a change in dipole moment, while Raman scattering probes a change in polarizability; their different selection rules make the methods complementary. Vibrational bands respond to bonding, phase, local strain, hydrogen bonding and temperature. ATR-FTIR penetration depth varies with wavelength, refractive indices and incidence angle, so sampling depth is not fixed across the spectrum. Raman spectra can be distorted by fluorescence, local laser heating or strongly varying collection geometry. Baseline removal and peak fitting should be reported transparently to avoid generating spectral features algorithmically.

**Explicit defining relation.** For a vibration with wavenumber ṽ in cm⁻¹, frequency is f=c ṽ when c is expressed in cm/s.

### Concrete materials-characterization problem

A polymer shows a new Raman band after laser exposure but the band disappears at lower illumination power. Diagnose heating, photochemistry and noise possibilities.

### Reproducible synthetic worked example

The nearby interactive card titled **Surface-photoelectron overlayer attenuation** changes **Overlayer thickness**. The declared calculation is `100*Math.exp(-t/(2.5*Math.cos(30*Math.PI/180)))`; the model returns 6.25817678 % remaining signal at 6 nm and 3.13011132 % remaining signal at 7.5 nm. Thus as the displayed input grows across these two test settings, the calculated output decreases. The secant sensitivity over this interval is -2.085377 % remaining signal per nm. Check the sign from the governing equation rather than trusting the plotted curve, and confirm dimensional consistency before copying results to the case table. The method is a pedagogical sensitivity test, not a calibrated measurement of a commercial or laboratory specimen.

### Independent experimental and calibration plan

A realistic measurement study of **infrared and raman vibrational spectroscopy** would begin with **survey and high-resolution spectra under calibrated conditions**, retaining **signal and background, spectral resolution, instrument energy axis, beam dose and overlayer history**. An independent check would use **chemical reference, low-damage acquisition and complementary surface or bulk-sensitive method**.

### Threats to interpretation and a failure mode

A single shared peak may not identify a compound; spectral libraries are supports rather than substitutes for independent physical constraints.

### Exercises with solution guidance

**Exercise A — physical inference.** Starting from For a vibration with wavenumber ṽ in cm⁻¹, frequency is f=c ṽ when c is expressed in cm/s. explain what is measured, what is inferred, the unit of every symbol and which environmental or microstructural assumption is most fragile. Then describe why the result of a shallow probe against a volume-sensitive probe might not be directly comparable. *Answer guide:* define the measurand before the apparatus, identify one calibration-dependent term, and test an alternative physical cause rather than listing properties of the equipment.

**Exercise B — numerical and uncertainty check.** Independently calculate the two numbers in **Surface-photoelectron overlayer attenuation: 6 nm → 6.2581768 % remaining signal; 7.5 nm → 3.1301113 % remaining signal** and estimate the local sensitivity at the midpoint. Choose an illustrative input standard uncertainty and propagate it using a first-order derivative; identify at least one source of model uncertainty not included by this arithmetic. *Answer guide:* use the model's stated units and bounds, do not round intermediate conversions prematurely, and explicitly label every calculated number synthetic.

**Exercise C — falsification and control.** Design a modest experiment for **infrared and raman vibrational spectroscopy** with a procedural blank or reference, three independent physical specimens where meaningful, one orthogonal measurement and a predefined exclusion rule. State a possible observation that makes your favored inference untenable. *Answer guide:* record material processing and measurement history, separate technical repeats from sample repeats, and require that the independent test distinguishes competing hypotheses.

**Discussion and decision.** Design a laser-power dependence and an FTIR cross-check to test for measurement-induced damage. Give one conclusion supported directly by a detector observable, one conclusion requiring a fitted model, and one conclusion that cannot yet be made at all. Finish with a single high-value next measurement and explain why its expected information is worth the cost.

## Lesson 4.4 — UV–visible optical absorption and photoluminescence

### Physical mechanism and its measurable signature

Transmission and reflectance measurements estimate light loss by absorption, scattering and surface reflections. Beer–Lambert absorbance is a useful model for homogeneous non-scattering solutions but fails when particle scattering, fluorescence, concentration-dependent chemistry or detector stray light matters. Photoluminescence intensity also depends on excitation flux, quantum yield, reabsorption, sample thickness and detector spectral response. An optical onset in a disordered solid may not uniquely identify an electronic band gap without a valid transition model. Time-resolved emission can distinguish radiative and nonradiative relaxation only with instrument-response considerations.

**Explicit defining relation.** Ideal absorbance A=log10(I0/I)=ε c ℓ, for a non-scattering homogeneous path and consistent concentration units.

### Concrete materials-characterization problem

Two nanoparticle dispersions give different apparent optical gaps, but one is visibly turbid. Propose integrating-sphere or dilution tests to distinguish absorption from scattering.

### Reproducible synthetic worked example

The nearby interactive card titled **Ideal Beer–Lambert absorbance** changes **Solute concentration**. The declared calculation is `25*c*1`; the model returns 1.25 absorbance at 0.05 mol/L and 1.5 absorbance at 0.06 mol/L. Thus as the displayed input grows across these two test settings, the calculated output increases. The secant sensitivity over this interval is 25 absorbance per mol/L. Check the sign from the governing equation rather than trusting the plotted curve, and confirm dimensional consistency before copying results to the case table. The method is a pedagogical sensitivity test, not a calibrated measurement of a commercial or laboratory specimen.

### Independent experimental and calibration plan

A realistic measurement study of **uv–visible optical absorption and photoluminescence** would begin with **survey and high-resolution spectra under calibrated conditions**, retaining **signal and background, spectral resolution, instrument energy axis, beam dose and overlayer history**. An independent check would use **chemical reference, low-damage acquisition and complementary surface or bulk-sensitive method**.

### Threats to interpretation and a failure mode

A fitted Tauc intercept is model-dependent and should not be reported as an unquestionable direct band-gap measurement.

### Exercises with solution guidance

**Exercise A — physical inference.** Starting from Ideal absorbance A=log10(I0/I)=ε c ℓ, for a non-scattering homogeneous path and consistent concentration units. explain what is measured, what is inferred, the unit of every symbol and which environmental or microstructural assumption is most fragile. Then describe why the result of a model-generated trend against an actual controlled test might not be directly comparable. *Answer guide:* define the measurand before the apparatus, identify one calibration-dependent term, and test an alternative physical cause rather than listing properties of the equipment.

**Exercise B — numerical and uncertainty check.** Independently calculate the two numbers in **Ideal Beer–Lambert absorbance: 0.05 mol/L → 1.25 absorbance; 0.06 mol/L → 1.5 absorbance** and estimate the local sensitivity at the midpoint. Choose an illustrative input standard uncertainty and propagate it using a first-order derivative; identify at least one source of model uncertainty not included by this arithmetic. *Answer guide:* use the model's stated units and bounds, do not round intermediate conversions prematurely, and explicitly label every calculated number synthetic.

**Exercise C — falsification and control.** Design a modest experiment for **uv–visible optical absorption and photoluminescence** with a procedural blank or reference, three independent physical specimens where meaningful, one orthogonal measurement and a predefined exclusion rule. State a possible observation that makes your favored inference untenable. *Answer guide:* record material processing and measurement history, separate technical repeats from sample repeats, and require that the independent test distinguishes competing hypotheses.

**Discussion and decision.** How would independent path-length and concentration measurements help falsify the Beer–Lambert interpretation? Give one conclusion supported directly by a detector observable, one conclusion requiring a fitted model, and one conclusion that cannot yet be made at all. Finish with a single high-value next measurement and explain why its expected information is worth the cost.

<!-- MODEL_7 -->

## Lesson 4.5 — Wetting, contact angles and surface contamination

### Physical mechanism and its measurable signature

The apparent contact angle of a liquid droplet depends on surface chemistry, roughness, heterogeneity, droplet size, contamination, evaporation and pinning. A single static angle does not uniquely specify surface free energy or adhesion performance. Advancing and receding measurements reveal hysteresis and metastability; the Wenzel and Cassie–Baxter descriptions apply in particular geometrical regimes. High-surface-energy substrates rapidly acquire airborne contaminants, changing apparent wetting during storage. Surface analysis and dynamic contact angle tests can be more informative together than either alone.

**Explicit defining relation.** Young relation for an ideal smooth homogeneous equilibrium surface: γ_SV−γ_SL=γ_LV cos θ; rough or hysteretic surfaces violate its simple interpretation.

### Concrete materials-characterization problem

A plasma-treated polymer initially wets water but recovers a high contact angle after a week. Distinguish molecular rearrangement from airborne adsorption.

### Reproducible synthetic worked example

The nearby interactive card titled **Surface-photoelectron overlayer attenuation** changes **Overlayer thickness**. The declared calculation is `100*Math.exp(-t/(2.5*Math.cos(30*Math.PI/180)))`; the model returns 1.5655673 % remaining signal at 9 nm and 0.783039549 % remaining signal at 10.5 nm. Thus as the displayed input grows across these two test settings, the calculated output decreases. The secant sensitivity over this interval is -0.52168516 % remaining signal per nm. Check the sign from the governing equation rather than trusting the plotted curve, and confirm dimensional consistency before copying results to the case table. The method is a pedagogical sensitivity test, not a calibrated measurement of a commercial or laboratory specimen.

### Independent experimental and calibration plan

A realistic measurement study of **wetting, contact angles and surface contamination** would begin with **survey and high-resolution spectra under calibrated conditions**, retaining **signal and background, spectral resolution, instrument energy axis, beam dose and overlayer history**. An independent check would use **chemical reference, low-damage acquisition and complementary surface or bulk-sensitive method**.

### Threats to interpretation and a failure mode

One contact-angle value cannot justify a universal claim of hydrophilicity, biocompatibility or durable adhesion under actual process conditions.

### Exercises with solution guidance

**Exercise A — physical inference.** Starting from Young relation for an ideal smooth homogeneous equilibrium surface: γ_SV−γ_SL=γ_LV cos θ; rough or hysteretic surfaces violate its simple interpretation. explain what is measured, what is inferred, the unit of every symbol and which environmental or microstructural assumption is most fragile. Then describe why the result of a response measured across two excitation or environmental conditions might not be directly comparable. *Answer guide:* define the measurand before the apparatus, identify one calibration-dependent term, and test an alternative physical cause rather than listing properties of the equipment.

**Exercise B — numerical and uncertainty check.** Independently calculate the two numbers in **Surface-photoelectron overlayer attenuation: 9 nm → 1.5655673 % remaining signal; 10.5 nm → 0.78303955 % remaining signal** and estimate the local sensitivity at the midpoint. Choose an illustrative input standard uncertainty and propagate it using a first-order derivative; identify at least one source of model uncertainty not included by this arithmetic. *Answer guide:* use the model's stated units and bounds, do not round intermediate conversions prematurely, and explicitly label every calculated number synthetic.

**Exercise C — falsification and control.** Design a modest experiment for **wetting, contact angles and surface contamination** with a procedural blank or reference, three independent physical specimens where meaningful, one orthogonal measurement and a predefined exclusion rule. State a possible observation that makes your favored inference untenable. *Answer guide:* record material processing and measurement history, separate technical repeats from sample repeats, and require that the independent test distinguishes competing hypotheses.

**Discussion and decision.** How could a time series under controlled storage and a chemically independent test discriminate contamination from intrinsic surface recovery? Give one conclusion supported directly by a detector observable, one conclusion requiring a fitted model, and one conclusion that cannot yet be made at all. Finish with a single high-value next measurement and explain why its expected information is worth the cost.

## Unit 4 capstone — evidence review and design defense

**Investigation.** A polymer coating fails an adhesion test after storage. Compare outer-surface XPS, vibrational spectroscopy and cross-sectional evidence to distinguish oxidation, contamination and interfacial defects.

1. **Specify a measurable claim.** Define the target parameter and where the specimens come from. Identify why the sampling population rather than the number of images matters for the engineering claim.
2. **Build a methods matrix.** Choose at least three complementary measurements for **spectroscopy, surface analysis and chemical identity**. For each report the instrument signal, calibration, spatial or information depth, most likely artifact and an orthogonal verification strategy.
3. **Audit two numerical models.** For both cards, calculate the default value, an endpoint and a sensitivity. Mark every quantity synthetic. Explain why agreement with its ideal formula is not sufficient for independent validation.
4. **Budget uncertainty and confounders.** Separate repeatability, reference calibration, specimen variability, geometry and data-reduction sensitivity. Include a possible correlated error and a case where a high pixel count is misleading.
5. **Make an evidence-limited decision.** Write 250 words separating directly supported observations from inferred structure or function. State precisely what additional result would reverse the proposed interpretation.

### Synthesis and transferable reasoning

A characterization workflow is useful when it turns a defined problem into falsifiable evidence. The same specimen can look different when probe volume, preparation, temperature, analysis background or inversion model changes. In **spectroscopy, surface analysis and chemical identity**, the central skill is not knowing a long list of instruments; it is matching each claim to a physically appropriate observable and understanding how to challenge that inference. A laboratory report should acknowledge the subset of the population sampled, not imply that a selected image or a synthetic curve describes every possible specimen. Favor a chain of traceable data over a single polished figure.

