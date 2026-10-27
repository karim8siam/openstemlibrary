# Unit 7: Electrical, magnetic and time-resolved characterization

**Core research question.** How can measured voltage, current, magnetic moment or transient light response be connected to physically meaningful functional properties?

## Physical context and prerequisite reasoning

Functional-material measurements are strongly dependent on contacts, frequency, magnetic-field history, temperature and sample geometry. Contact resistance can masquerade as resistivity; an impedance arc can have several equivalent circuits; a hysteresis loop can contain leakage and instrumentation offsets. Frequency-dependent and nonlinear systems should be analyzed over controlled excitation windows, not reduced to one headline parameter. Physical interpretation demands a model and at least one plausible artifact to test.

A fundamental distinction in **Electrical, magnetic and time-resolved characterization** is the difference between what the instrument records and what one wants to infer. Design a chain of explanation containing a specimen with a known history, a measurable interaction, a recorded signal, one or more corrections, a model or reference, and the qualified property estimate. State which component could change when the operator selects another location, detector or processing program. In materials science an instrument often averages over a volume, while a proposed mechanism may live at an interface or individual defect. That mismatch can make a precise measurement irrelevant. This unit therefore emphasizes independent samples, documented acquisition conditions and physical counterexamples rather than applying formulae mechanically.

## Investigative exercise for the entire unit

A thin film is described as simultaneously conductive, ferroelectric and magnetic. Draft a minimal instrument-independent verification sequence that rejects contact artifacts, leakage-current hysteresis and background magnetic signals.

## Lesson 7.1 — Four-point transport and Hall measurements

### Physical mechanism and its measurable signature

A four-terminal measurement separates current injection from voltage sensing to reduce effects of contact resistance, subject to sufficiently high voltmeter impedance and appropriate geometry. Converting resistance to resistivity requires current-path geometry; sheet resistance of a uniform thin film has different conventions from a bulk bar. Hall measurements use transverse voltage under magnetic field and can estimate carrier sign and density in simple one-carrier models. Multiple carrier types, anomalous Hall effects and inhomogeneous conduction complicate interpretation. Reversing current and field can suppress thermoelectric offsets and longitudinal voltage mixing.

**Explicit defining relation.** For a uniform rectangular bar, resistivity ρ=R A/L, with resistance R, cross-sectional area A and electrode spacing L.

### Concrete materials-characterization problem

A metal strip reports a negative Hall coefficient after mounting, but the sign flips after swapping sense contacts. Identify wiring, field reversal and carrier-model tests.

### Reproducible synthetic worked example

The nearby interactive card titled **Uniform-bar electrical resistivity** changes **Measured bar resistance**. The declared calculation is `0.01*R`; the model returns 0.04008 Ω·cm at 4.008 Ω and 0.06007 Ω·cm at 6.007 Ω. Thus as the displayed input grows across these two test settings, the calculated output increases. The secant sensitivity over this interval is 0.01 Ω·cm per Ω. Check the sign from the governing equation rather than trusting the plotted curve, and confirm dimensional consistency before copying results to the case table. The method is a pedagogical sensitivity test, not a calibrated measurement of a commercial or laboratory specimen.

### Independent experimental and calibration plan

A realistic measurement study of **four-point transport and hall measurements** would begin with **four-terminal, frequency-response or field-dependent response testing**, retaining **geometry, temperature, excitation amplitude, contact positions, frequency or field and full raw signal**. An independent check would use **reversed current or field, blank holder, geometry sweep and control sample**.

### Threats to interpretation and a failure mode

A voltage-current slope is not necessarily intrinsic resistivity without geometry and contact verification; one-carrier Hall densities may be invalid in compensated materials.

### Exercises with solution guidance

**Exercise A — physical inference.** Starting from For a uniform rectangular bar, resistivity ρ=R A/L, with resistance R, cross-sectional area A and electrode spacing L. explain what is measured, what is inferred, the unit of every symbol and which environmental or microstructural assumption is most fragile. Then describe why the result of a model-generated trend against an actual controlled test might not be directly comparable. *Answer guide:* define the measurand before the apparatus, identify one calibration-dependent term, and test an alternative physical cause rather than listing properties of the equipment.

**Exercise B — numerical and uncertainty check.** Independently calculate the two numbers in **Uniform-bar electrical resistivity: 4.008 Ω → 0.04008 Ω·cm; 6.007 Ω → 0.06007 Ω·cm** and estimate the local sensitivity at the midpoint. Choose an illustrative input standard uncertainty and propagate it using a first-order derivative; identify at least one source of model uncertainty not included by this arithmetic. *Answer guide:* use the model's stated units and bounds, do not round intermediate conversions prematurely, and explicitly label every calculated number synthetic.

**Exercise C — falsification and control.** Design a modest experiment for **four-point transport and hall measurements** with a procedural blank or reference, three independent physical specimens where meaningful, one orthogonal measurement and a predefined exclusion rule. State a possible observation that makes your favored inference untenable. *Answer guide:* record material processing and measurement history, separate technical repeats from sample repeats, and require that the independent test distinguishes competing hypotheses.

**Discussion and decision.** Which current-reversal and thickness-series results would invalidate a simple bulk conduction interpretation? Give one conclusion supported directly by a detector observable, one conclusion requiring a fitted model, and one conclusion that cannot yet be made at all. Finish with a single high-value next measurement and explain why its expected information is worth the cost.

## Lesson 7.2 — Impedance spectroscopy and dielectric loss

### Physical mechanism and its measurable signature

Complex impedance records frequency-dependent amplitude and phase between voltage and current. Equivalent RC or distributed models can approximate grain, grain-boundary, electrode and ionic contributions, but a similar semicircle may arise from different mechanisms. Reliable interpretation includes instrument open/short calibration, geometric capacitance, frequency window, excitation amplitude and thermal stability. Electrode polarization can dominate low-frequency response, while lead inductance influences high-frequency features. Temperature dependence and sample-thickness scaling often separate bulk and interface signals more effectively than adding fit parameters.

**Explicit defining relation.** For an ideal parallel RC element, Y=1/R+jωC and Z=1/Y; frequency is ω=2πf.

### Concrete materials-characterization problem

A ceramic pellet shows two impedance arcs after changing electrode metal. Decide which arc may come from the contact rather than the grain boundary.

### Reproducible synthetic worked example

The nearby interactive card titled **Illustrative Curie magnetic susceptibility** changes **Temperature**. The declared calculation is `0.03/T`; the model returns 0.000157894737 dimensionless at 190 K and 0.000136363636 dimensionless at 220 K. Thus as the displayed input grows across these two test settings, the calculated output decreases. The secant sensitivity over this interval is -7.1770335e-07 dimensionless per K. Check the sign from the governing equation rather than trusting the plotted curve, and confirm dimensional consistency before copying results to the case table. The method is a pedagogical sensitivity test, not a calibrated measurement of a commercial or laboratory specimen.

### Independent experimental and calibration plan

A realistic measurement study of **impedance spectroscopy and dielectric loss** would begin with **four-terminal, frequency-response or field-dependent response testing**, retaining **geometry, temperature, excitation amplitude, contact positions, frequency or field and full raw signal**. An independent check would use **reversed current or field, blank holder, geometry sweep and control sample**.

### Threats to interpretation and a failure mode

A low least-squares impedance fitting error does not uniquely identify an equivalent circuit or prove the existence of a particular grain boundary layer.

### Exercises with solution guidance

**Exercise A — physical inference.** Starting from For an ideal parallel RC element, Y=1/R+jωC and Z=1/Y; frequency is ω=2πf. explain what is measured, what is inferred, the unit of every symbol and which environmental or microstructural assumption is most fragile. Then describe why the result of a response measured across two excitation or environmental conditions might not be directly comparable. *Answer guide:* define the measurand before the apparatus, identify one calibration-dependent term, and test an alternative physical cause rather than listing properties of the equipment.

**Exercise B — numerical and uncertainty check.** Independently calculate the two numbers in **Illustrative Curie magnetic susceptibility: 190 K → 0.00015789474 dimensionless; 220 K → 0.00013636364 dimensionless** and estimate the local sensitivity at the midpoint. Choose an illustrative input standard uncertainty and propagate it using a first-order derivative; identify at least one source of model uncertainty not included by this arithmetic. *Answer guide:* use the model's stated units and bounds, do not round intermediate conversions prematurely, and explicitly label every calculated number synthetic.

**Exercise C — falsification and control.** Design a modest experiment for **impedance spectroscopy and dielectric loss** with a procedural blank or reference, three independent physical specimens where meaningful, one orthogonal measurement and a predefined exclusion rule. State a possible observation that makes your favored inference untenable. *Answer guide:* record material processing and measurement history, separate technical repeats from sample repeats, and require that the independent test distinguishes competing hypotheses.

**Discussion and decision.** What thickness and electrode-material series would reveal electrode polarization rather than bulk dielectric behavior? Give one conclusion supported directly by a detector observable, one conclusion requiring a fitted model, and one conclusion that cannot yet be made at all. Finish with a single high-value next measurement and explain why its expected information is worth the cost.

<!-- MODEL_12 -->

## Lesson 7.3 — Magnetometry, susceptibility and hysteresis

### Physical mechanism and its measurable signature

Vibrating-sample magnetometers and SQUID-based systems sense sample magnetic moment under controlled field and temperature. Contributions from holders, substrates, surface contamination and unbalanced background fields can be comparable to tiny thin-film moments. Diamagnetic, paramagnetic, ferromagnetic and superparamagnetic systems produce different field and temperature histories; hysteresis alone is not a chemistry fingerprint. Moment per mass, per area and per volume are different normalizations and require accurate sample dimensions. Zero-field-cooled and field-cooled sequences are useful only with their protocols and thermal history disclosed.

**Explicit defining relation.** In an ideal Curie paramagnet at fixed composition and weak field, susceptibility χ=C/T, neglecting interactions and saturation.

### Concrete materials-characterization problem

A millimetre-scale film displays a weak hysteresis loop that disappears when an identical blank substrate is measured. Determine how subtraction and contamination controls affect the claim.

### Reproducible synthetic worked example

The nearby interactive card titled **Uniform-bar electrical resistivity** changes **Measured bar resistance**. The declared calculation is `0.01*R`; the model returns 0.08006 Ω·cm at 8.006 Ω and 0.10005 Ω·cm at 10.005 Ω. Thus as the displayed input grows across these two test settings, the calculated output increases. The secant sensitivity over this interval is 0.01 Ω·cm per Ω. Check the sign from the governing equation rather than trusting the plotted curve, and confirm dimensional consistency before copying results to the case table. The method is a pedagogical sensitivity test, not a calibrated measurement of a commercial or laboratory specimen.

### Independent experimental and calibration plan

A realistic measurement study of **magnetometry, susceptibility and hysteresis** would begin with **four-terminal, frequency-response or field-dependent response testing**, retaining **geometry, temperature, excitation amplitude, contact positions, frequency or field and full raw signal**. An independent check would use **reversed current or field, blank holder, geometry sweep and control sample**.

### Threats to interpretation and a failure mode

A tiny ferromagnetic impurity can dominate the net moment despite low mass fraction; a room-temperature loop does not prove a uniform intrinsic magnetic phase.

### Exercises with solution guidance

**Exercise A — physical inference.** Starting from In an ideal Curie paramagnet at fixed composition and weak field, susceptibility χ=C/T, neglecting interactions and saturation. explain what is measured, what is inferred, the unit of every symbol and which environmental or microstructural assumption is most fragile. Then describe why the result of the same specimen measured before and after surface preparation might not be directly comparable. *Answer guide:* define the measurand before the apparatus, identify one calibration-dependent term, and test an alternative physical cause rather than listing properties of the equipment.

**Exercise B — numerical and uncertainty check.** Independently calculate the two numbers in **Uniform-bar electrical resistivity: 8.006 Ω → 0.08006 Ω·cm; 10.005 Ω → 0.10005 Ω·cm** and estimate the local sensitivity at the midpoint. Choose an illustrative input standard uncertainty and propagate it using a first-order derivative; identify at least one source of model uncertainty not included by this arithmetic. *Answer guide:* use the model's stated units and bounds, do not round intermediate conversions prematurely, and explicitly label every calculated number synthetic.

**Exercise C — falsification and control.** Design a modest experiment for **magnetometry, susceptibility and hysteresis** with a procedural blank or reference, three independent physical specimens where meaningful, one orthogonal measurement and a predefined exclusion rule. State a possible observation that makes your favored inference untenable. *Answer guide:* record material processing and measurement history, separate technical repeats from sample repeats, and require that the independent test distinguishes competing hypotheses.

**Discussion and decision.** Which holder blank, thickness scaling and elemental assay would falsify intrinsic ferromagnetism? Give one conclusion supported directly by a detector observable, one conclusion requiring a fitted model, and one conclusion that cannot yet be made at all. Finish with a single high-value next measurement and explain why its expected information is worth the cost.

## Lesson 7.4 — Ferroelectric switching versus leakage artifacts

### Physical mechanism and its measurable signature

Polarization–electric-field loops estimate charge displacement under a changing electric field, but conducting samples and interfacial capacitive effects can generate open-looking hysteresis without switchable ferroelectric domains. Frequency, temperature, sweep waveform, electrode area, fatigue and retention change the observed loop. Positive-up-negative-down or comparable switching-current protocols can distinguish switching from nonswitching capacitive and leakage contributions under appropriate assumptions. Nanoscale piezoresponse images alone can be distorted by electrostatic forces and ionic migration. A credible conclusion triangulates macroscopic electrical switching with structural evidence and endurance behavior.

**Explicit defining relation.** Ideal capacitor displacement charge Q=C V and polarization estimate P=Q/A, but leakage current must be separated from switchable contribution.

### Concrete materials-characterization problem

A leaky oxide shows a wide P–E loop at one sweep rate but collapses when pulse widths change. Decide what cannot yet be called remanent polarization.

### Reproducible synthetic worked example

The nearby interactive card titled **Illustrative Curie magnetic susceptibility** changes **Temperature**. The declared calculation is `0.03/T`; the model returns 0.00012 dimensionless at 250 K and 0.000107142857 dimensionless at 280 K. Thus as the displayed input grows across these two test settings, the calculated output decreases. The secant sensitivity over this interval is -4.2857143e-07 dimensionless per K. Check the sign from the governing equation rather than trusting the plotted curve, and confirm dimensional consistency before copying results to the case table. The method is a pedagogical sensitivity test, not a calibrated measurement of a commercial or laboratory specimen.

### Independent experimental and calibration plan

A realistic measurement study of **ferroelectric switching versus leakage artifacts** would begin with **four-terminal, frequency-response or field-dependent response testing**, retaining **geometry, temperature, excitation amplitude, contact positions, frequency or field and full raw signal**. An independent check would use **reversed current or field, blank holder, geometry sweep and control sample**.

### Threats to interpretation and a failure mode

A butterfly displacement curve or loop shape alone is not proof of ferroelectric order; electrochemistry and electrostatics can mimic switching.

### Exercises with solution guidance

**Exercise A — physical inference.** Starting from Ideal capacitor displacement charge Q=C V and polarization estimate P=Q/A, but leakage current must be separated from switchable contribution. explain what is measured, what is inferred, the unit of every symbol and which environmental or microstructural assumption is most fragile. Then describe why the result of a calibration control against an unknown sample might not be directly comparable. *Answer guide:* define the measurand before the apparatus, identify one calibration-dependent term, and test an alternative physical cause rather than listing properties of the equipment.

**Exercise B — numerical and uncertainty check.** Independently calculate the two numbers in **Illustrative Curie magnetic susceptibility: 250 K → 0.00012 dimensionless; 280 K → 0.00010714286 dimensionless** and estimate the local sensitivity at the midpoint. Choose an illustrative input standard uncertainty and propagate it using a first-order derivative; identify at least one source of model uncertainty not included by this arithmetic. *Answer guide:* use the model's stated units and bounds, do not round intermediate conversions prematurely, and explicitly label every calculated number synthetic.

**Exercise C — falsification and control.** Design a modest experiment for **ferroelectric switching versus leakage artifacts** with a procedural blank or reference, three independent physical specimens where meaningful, one orthogonal measurement and a predefined exclusion rule. State a possible observation that makes your favored inference untenable. *Answer guide:* record material processing and measurement history, separate technical repeats from sample repeats, and require that the independent test distinguishes competing hypotheses.

**Discussion and decision.** Design a pulse sequence and temperature-dependent leakage control that could reject an apparent polarization claim. Give one conclusion supported directly by a detector observable, one conclusion requiring a fitted model, and one conclusion that cannot yet be made at all. Finish with a single high-value next measurement and explain why its expected information is worth the cost.

<!-- MODEL_13 -->

## Lesson 7.5 — Time-resolved luminescence and transient response

### Physical mechanism and its measurable signature

A time-resolved detector records the convolution of excitation pulse, instrument response and sample relaxation. A single exponential describes one ideal relaxation channel, but a heterogeneous specimen can exhibit multiple rates, diffusion and reabsorption. Finite detector dead time and background shift extracted lifetimes. Changing excitation fluence can reveal trap saturation or nonlinear recombination; an apparent long lifetime may reflect delayed luminescence from another population. Independent steady-state spectra, temperature and power series help connect a lifetime to a physical mechanism.

**Explicit defining relation.** Ideal mono-exponential decay I(t)=I0 exp(−t/τ)+B for a stationary sample and constant background B.

### Concrete materials-characterization problem

Two films give different reported fluorescence lifetimes, but one was measured with lower time resolution and a different instrument-response function. Plan a defensible comparison.

### Reproducible synthetic worked example

The nearby interactive card titled **Uniform-bar electrical resistivity** changes **Measured bar resistance**. The declared calculation is `0.01*R`; the model returns 0.12004 Ω·cm at 12.004 Ω and 0.14003 Ω·cm at 14.003 Ω. Thus as the displayed input grows across these two test settings, the calculated output increases. The secant sensitivity over this interval is 0.01 Ω·cm per Ω. Check the sign from the governing equation rather than trusting the plotted curve, and confirm dimensional consistency before copying results to the case table. The method is a pedagogical sensitivity test, not a calibrated measurement of a commercial or laboratory specimen.

### Independent experimental and calibration plan

A realistic measurement study of **time-resolved luminescence and transient response** would begin with **four-terminal, frequency-response or field-dependent response testing**, retaining **geometry, temperature, excitation amplitude, contact positions, frequency or field and full raw signal**. An independent check would use **reversed current or field, blank holder, geometry sweep and control sample**.

### Threats to interpretation and a failure mode

A fitted biexponential curve is not unique evidence for exactly two chemically distinct emissive species; detector response and distributions of environments matter.

### Exercises with solution guidance

**Exercise A — physical inference.** Starting from Ideal mono-exponential decay I(t)=I0 exp(−t/τ)+B for a stationary sample and constant background B. explain what is measured, what is inferred, the unit of every symbol and which environmental or microstructural assumption is most fragile. Then describe why the result of one carefully chosen field against randomized spatial fields might not be directly comparable. *Answer guide:* define the measurand before the apparatus, identify one calibration-dependent term, and test an alternative physical cause rather than listing properties of the equipment.

**Exercise B — numerical and uncertainty check.** Independently calculate the two numbers in **Uniform-bar electrical resistivity: 12.004 Ω → 0.12004 Ω·cm; 14.003 Ω → 0.14003 Ω·cm** and estimate the local sensitivity at the midpoint. Choose an illustrative input standard uncertainty and propagate it using a first-order derivative; identify at least one source of model uncertainty not included by this arithmetic. *Answer guide:* use the model's stated units and bounds, do not round intermediate conversions prematurely, and explicitly label every calculated number synthetic.

**Exercise C — falsification and control.** Design a modest experiment for **time-resolved luminescence and transient response** with a procedural blank or reference, three independent physical specimens where meaningful, one orthogonal measurement and a predefined exclusion rule. State a possible observation that makes your favored inference untenable. *Answer guide:* record material processing and measurement history, separate technical repeats from sample repeats, and require that the independent test distinguishes competing hypotheses.

**Discussion and decision.** How could reconvolution with measured instrument response and excitation-power variation overturn a claimed trap-lifetime assignment? Give one conclusion supported directly by a detector observable, one conclusion requiring a fitted model, and one conclusion that cannot yet be made at all. Finish with a single high-value next measurement and explain why its expected information is worth the cost.

## Unit 7 capstone — evidence review and design defense

**Investigation.** A thin film is described as simultaneously conductive, ferroelectric and magnetic. Draft a minimal instrument-independent verification sequence that rejects contact artifacts, leakage-current hysteresis and background magnetic signals.

1. **Specify a measurable claim.** Define the target parameter and where the specimens come from. Identify why the sampling population rather than the number of images matters for the engineering claim.
2. **Build a methods matrix.** Choose at least three complementary measurements for **electrical, magnetic and time-resolved characterization**. For each report the instrument signal, calibration, spatial or information depth, most likely artifact and an orthogonal verification strategy.
3. **Audit two numerical models.** For both cards, calculate the default value, an endpoint and a sensitivity. Mark every quantity synthetic. Explain why agreement with its ideal formula is not sufficient for independent validation.
4. **Budget uncertainty and confounders.** Separate repeatability, reference calibration, specimen variability, geometry and data-reduction sensitivity. Include a possible correlated error and a case where a high pixel count is misleading.
5. **Make an evidence-limited decision.** Write 250 words separating directly supported observations from inferred structure or function. State precisely what additional result would reverse the proposed interpretation.

### Synthesis and transferable reasoning

A characterization workflow is useful when it turns a defined problem into falsifiable evidence. The same specimen can look different when probe volume, preparation, temperature, analysis background or inversion model changes. In **electrical, magnetic and time-resolved characterization**, the central skill is not knowing a long list of instruments; it is matching each claim to a physically appropriate observable and understanding how to challenge that inference. A laboratory report should acknowledge the subset of the population sampled, not imply that a selected image or a synthetic curve describes every possible specimen. Favor a chain of traceable data over a single polished figure.

