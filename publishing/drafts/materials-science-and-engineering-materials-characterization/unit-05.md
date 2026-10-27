# Unit 5: Thermal analysis and mechanical property measurements

**Core research question.** When does an apparent transition, hardness value or loss modulus measure a material property rather than a testing artifact?

## Physical context and prerequisite reasoning

Thermal and mechanical characterization requires coupled knowledge of specimen dimensions, heating or loading histories, thermal contact, instrument dynamics and constitutive assumptions. Heating rate and environment can shift transitions; indentation area may be estimated from a tip model; viscoelastic response changes with frequency and temperature. A reproducible protocol can give reproducible numbers that are irrelevant to service conditions if strain rate, moisture or chemistry differs.

A fundamental distinction in **Thermal analysis and mechanical property measurements** is the difference between what the instrument records and what one wants to infer. Design a chain of explanation containing a specimen with a known history, a measurable interaction, a recorded signal, one or more corrections, a model or reference, and the qualified property estimate. State which component could change when the operator selects another location, detector or processing program. In materials science an instrument often averages over a volume, while a proposed mechanism may live at an interface or individual defect. That mismatch can make a precise measurement irrelevant. This unit therefore emphasizes independent samples, documented acquisition conditions and physical counterexamples rather than applying formulae mechanically.

## Investigative exercise for the entire unit

An injection-molded polymer has different stiffness values from DMA and quasi-static tension and a broad heat-flow peak. Construct a consistent interpretation without selecting only the most favorable result.

## Lesson 5.1 — Differential scanning calorimetry and enthalpy changes

### Physical mechanism and its measurable signature

DSC measures a difference in heat flow associated with a programmed temperature history. Features may arise from glass transition heat capacity changes, melting, crystallization, curing or other energetic processes. Integrating a baseline-corrected peak yields enthalpy per mass under calibration assumptions, but sample mass, pan seal, thermal lag and baseline choice contribute uncertainty. A faster heating ramp can shift kinetic transitions while a reversing heat-capacity signal may behave differently. Reporting a single transition temperature without defining onset, midpoint or peak criterion makes interlaboratory comparisons difficult.

**Explicit defining relation.** For constant effective heat capacity C_p and mass m, programmed sensible-heat flow is approximately q_dot=m C_p (dT/dt), after unit conversion.

### Concrete materials-characterization problem

Two DSC runs show melting peaks at different temperatures and enthalpies after changing heating rate and sample mass. Decide whether the material must have changed.

### Reproducible synthetic worked example

The nearby interactive card titled **Programmed DSC sensible heat flow** changes **Heating rate**. The declared calculation is `10*1.2*beta/60`; the model returns 1.36 mW at 6.8 K/min and 1.94 mW at 9.7 K/min. Thus as the displayed input grows across these two test settings, the calculated output increases. The secant sensitivity over this interval is 0.2 mW per K/min. Check the sign from the governing equation rather than trusting the plotted curve, and confirm dimensional consistency before copying results to the case table. The method is a pedagogical sensitivity test, not a calibrated measurement of a commercial or laboratory specimen.

### Independent experimental and calibration plan

A realistic measurement study of **differential scanning calorimetry and enthalpy changes** would begin with **controlled heating or load protocol with instrument standards**, retaining **sample mass and geometry, ramp or load rate, thermal contact, atmosphere, displacement and baseline**. An independent check would use **empty-pan/reference specimen, unloading or multiple-rate series, physical post-test micrograph**.

### Threats to interpretation and a failure mode

Heat-flow baseline subtraction and thermal lag can move a reported onset. A peak area is not automatically the fraction crystalline without reference enthalpy and mixture corrections.

### Exercises with solution guidance

**Exercise A — physical inference.** Starting from For constant effective heat capacity C_p and mass m, programmed sensible-heat flow is approximately q_dot=m C_p (dT/dt), after unit conversion. explain what is measured, what is inferred, the unit of every symbol and which environmental or microstructural assumption is most fragile. Then describe why the result of two independent specimens against repeated readings of one specimen might not be directly comparable. *Answer guide:* define the measurand before the apparatus, identify one calibration-dependent term, and test an alternative physical cause rather than listing properties of the equipment.

**Exercise B — numerical and uncertainty check.** Independently calculate the two numbers in **Programmed DSC sensible heat flow: 6.8 K/min → 1.36 mW; 9.7 K/min → 1.94 mW** and estimate the local sensitivity at the midpoint. Choose an illustrative input standard uncertainty and propagate it using a first-order derivative; identify at least one source of model uncertainty not included by this arithmetic. *Answer guide:* use the model's stated units and bounds, do not round intermediate conversions prematurely, and explicitly label every calculated number synthetic.

**Exercise C — falsification and control.** Design a modest experiment for **differential scanning calorimetry and enthalpy changes** with a procedural blank or reference, three independent physical specimens where meaningful, one orthogonal measurement and a predefined exclusion rule. State a possible observation that makes your favored inference untenable. *Answer guide:* record material processing and measurement history, separate technical repeats from sample repeats, and require that the independent test distinguishes competing hypotheses.

**Discussion and decision.** What empty-pan and independent calibration scans would challenge a measured enthalpy difference? Give one conclusion supported directly by a detector observable, one conclusion requiring a fitted model, and one conclusion that cannot yet be made at all. Finish with a single high-value next measurement and explain why its expected information is worth the cost.

## Lesson 5.2 — Thermogravimetric analysis and evolved-gas studies

### Physical mechanism and its measurable signature

TGA records mass as a function of temperature or time in a stated purge atmosphere. Mass losses can indicate water, solvent, decomposition or volatilization, but derivative peak temperatures are kinetic and depend on heating rate, crucible geometry and gas transport. Oxygen versus inert purge can change mechanism, while buoyancy drift and baseline instability imitate small mass changes. Coupling to FTIR or mass spectrometry can help attribute evolved gases but requires transfer-line, background and fragmentation controls. A single TGA curve is not a shelf-life forecast.

**Explicit defining relation.** Mass fraction remaining w(T)=m(T)/m0; derivative dm/dT depends on the programmed rate and apparatus response.

### Concrete materials-characterization problem

A ceramic powder loses 1% mass below 150 °C. Distinguish physisorbed water, binder solvent, hydroxyl loss and balance drift.

### Reproducible synthetic worked example

The nearby interactive card titled **Ideal contact hardness by fixed area** changes **Peak normal load**. The declared calculation is `P*1e-3/(2e-12)/1e9`; the model returns 1.535 GPa at 3.07 mN and 2.03 GPa at 4.06 mN. Thus as the displayed input grows across these two test settings, the calculated output increases. The secant sensitivity over this interval is 0.5 GPa per mN. Check the sign from the governing equation rather than trusting the plotted curve, and confirm dimensional consistency before copying results to the case table. The method is a pedagogical sensitivity test, not a calibrated measurement of a commercial or laboratory specimen.

### Independent experimental and calibration plan

A realistic measurement study of **thermogravimetric analysis and evolved-gas studies** would begin with **controlled heating or load protocol with instrument standards**, retaining **sample mass and geometry, ramp or load rate, thermal contact, atmosphere, displacement and baseline**. An independent check would use **empty-pan/reference specimen, unloading or multiple-rate series, physical post-test micrograph**.

### Threats to interpretation and a failure mode

Residual mass is not necessarily pure inorganic filler; oxidation or reactions can increase mass during some runs.

### Exercises with solution guidance

**Exercise A — physical inference.** Starting from Mass fraction remaining w(T)=m(T)/m0; derivative dm/dT depends on the programmed rate and apparatus response. explain what is measured, what is inferred, the unit of every symbol and which environmental or microstructural assumption is most fragile. Then describe why the result of a shallow probe against a volume-sensitive probe might not be directly comparable. *Answer guide:* define the measurand before the apparatus, identify one calibration-dependent term, and test an alternative physical cause rather than listing properties of the equipment.

**Exercise B — numerical and uncertainty check.** Independently calculate the two numbers in **Ideal contact hardness by fixed area: 3.07 mN → 1.535 GPa; 4.06 mN → 2.03 GPa** and estimate the local sensitivity at the midpoint. Choose an illustrative input standard uncertainty and propagate it using a first-order derivative; identify at least one source of model uncertainty not included by this arithmetic. *Answer guide:* use the model's stated units and bounds, do not round intermediate conversions prematurely, and explicitly label every calculated number synthetic.

**Exercise C — falsification and control.** Design a modest experiment for **thermogravimetric analysis and evolved-gas studies** with a procedural blank or reference, three independent physical specimens where meaningful, one orthogonal measurement and a predefined exclusion rule. State a possible observation that makes your favored inference untenable. *Answer guide:* record material processing and measurement history, separate technical repeats from sample repeats, and require that the independent test distinguishes competing hypotheses.

**Discussion and decision.** How would a repeated dry sample, blank crucible and evolved-gas monitor test a water-loss interpretation? Give one conclusion supported directly by a detector observable, one conclusion requiring a fitted model, and one conclusion that cannot yet be made at all. Finish with a single high-value next measurement and explain why its expected information is worth the cost.

<!-- MODEL_8 -->

## Lesson 5.3 — Dynamic mechanical analysis and viscoelastic time scales

### Physical mechanism and its measurable signature

A dynamic mechanical test imposes sinusoidal force or deformation and records the in-phase storage response and out-of-phase dissipation. Storage modulus, loss modulus and loss tangent depend on frequency, temperature, strain amplitude and geometry. In linear viscoelasticity these quantities can be related to relaxation mechanisms, but nonlinear slip, poor gripping and temperature gradients produce misleading phase lags. Time–temperature superposition is approximate and may fail for aging, multiple transition mechanisms or chemically changing materials. Define the linear viscoelastic region experimentally instead of assuming every oscillation amplitude qualifies.

**Explicit defining relation.** For sinusoidal small strain ε=ε0 sin ωt, stress may be written σ=ε0[E′ sin ωt+E″ cos ωt], with tanδ=E″/E′.

### Concrete materials-characterization problem

A polymer exhibits a shifted tan-delta peak when tested at tenfold frequency. Explain why this does not uniquely prove a changed glass transition chemistry.

### Reproducible synthetic worked example

The nearby interactive card titled **Programmed DSC sensible heat flow** changes **Heating rate**. The declared calculation is `10*1.2*beta/60`; the model returns 2.52 mW at 12.6 K/min and 3.1 mW at 15.5 K/min. Thus as the displayed input grows across these two test settings, the calculated output increases. The secant sensitivity over this interval is 0.2 mW per K/min. Check the sign from the governing equation rather than trusting the plotted curve, and confirm dimensional consistency before copying results to the case table. The method is a pedagogical sensitivity test, not a calibrated measurement of a commercial or laboratory specimen.

### Independent experimental and calibration plan

A realistic measurement study of **dynamic mechanical analysis and viscoelastic time scales** would begin with **controlled heating or load protocol with instrument standards**, retaining **sample mass and geometry, ramp or load rate, thermal contact, atmosphere, displacement and baseline**. An independent check would use **empty-pan/reference specimen, unloading or multiple-rate series, physical post-test micrograph**.

### Threats to interpretation and a failure mode

DMA modulus is not directly interchangeable with a static Young modulus or a tensile value measured at another strain rate.

### Exercises with solution guidance

**Exercise A — physical inference.** Starting from For sinusoidal small strain ε=ε0 sin ωt, stress may be written σ=ε0[E′ sin ωt+E″ cos ωt], with tanδ=E″/E′. explain what is measured, what is inferred, the unit of every symbol and which environmental or microstructural assumption is most fragile. Then describe why the result of a model-generated trend against an actual controlled test might not be directly comparable. *Answer guide:* define the measurand before the apparatus, identify one calibration-dependent term, and test an alternative physical cause rather than listing properties of the equipment.

**Exercise B — numerical and uncertainty check.** Independently calculate the two numbers in **Programmed DSC sensible heat flow: 12.6 K/min → 2.52 mW; 15.5 K/min → 3.1 mW** and estimate the local sensitivity at the midpoint. Choose an illustrative input standard uncertainty and propagate it using a first-order derivative; identify at least one source of model uncertainty not included by this arithmetic. *Answer guide:* use the model's stated units and bounds, do not round intermediate conversions prematurely, and explicitly label every calculated number synthetic.

**Exercise C — falsification and control.** Design a modest experiment for **dynamic mechanical analysis and viscoelastic time scales** with a procedural blank or reference, three independent physical specimens where meaningful, one orthogonal measurement and a predefined exclusion rule. State a possible observation that makes your favored inference untenable. *Answer guide:* record material processing and measurement history, separate technical repeats from sample repeats, and require that the independent test distinguishes competing hypotheses.

**Discussion and decision.** Which amplitude sweep would reveal whether an apparent phase lag comes from material damping or grip slippage? Give one conclusion supported directly by a detector observable, one conclusion requiring a fitted model, and one conclusion that cannot yet be made at all. Finish with a single high-value next measurement and explain why its expected information is worth the cost.

## Lesson 5.4 — Indentation, hardness and contact mechanics

### Physical mechanism and its measurable signature

Instrumented indentation converts a measured load–displacement record into contact stiffness and projected contact area through a contact model and calibrated indenter area function. Surface roughness, pile-up, sink-in, elastic recovery and thermal drift can alter hardness and modulus. Indentation size effects make the result load-dependent, and a thin film often reflects substrate support at larger penetration depths. Reference samples and optical or electron imaging can challenge the inferred contact area. Compare the tested volume to grain size and inclusion dimensions before claiming the result represents a bulk material.

**Explicit defining relation.** Projected-contact hardness H=P_max/A_c, with consistent units and a calibrated contact area A_c.

### Concrete materials-characterization problem

A nanoindentation map shows unexpectedly hard pixels near a polishing scratch; test whether topography, contact-area errors or actual microstructural hardening dominate.

### Reproducible synthetic worked example

The nearby interactive card titled **Ideal contact hardness by fixed area** changes **Peak normal load**. The declared calculation is `P*1e-3/(2e-12)/1e9`; the model returns 2.525 GPa at 5.05 mN and 3.02 GPa at 6.04 mN. Thus as the displayed input grows across these two test settings, the calculated output increases. The secant sensitivity over this interval is 0.5 GPa per mN. Check the sign from the governing equation rather than trusting the plotted curve, and confirm dimensional consistency before copying results to the case table. The method is a pedagogical sensitivity test, not a calibrated measurement of a commercial or laboratory specimen.

### Independent experimental and calibration plan

A realistic measurement study of **indentation, hardness and contact mechanics** would begin with **controlled heating or load protocol with instrument standards**, retaining **sample mass and geometry, ramp or load rate, thermal contact, atmosphere, displacement and baseline**. An independent check would use **empty-pan/reference specimen, unloading or multiple-rate series, physical post-test micrograph**.

### Threats to interpretation and a failure mode

Hardness numbers depend on test method and load; an indentation modulus estimate is model-dependent and can be wrong with substantial pile-up.

### Exercises with solution guidance

**Exercise A — physical inference.** Starting from Projected-contact hardness H=P_max/A_c, with consistent units and a calibrated contact area A_c. explain what is measured, what is inferred, the unit of every symbol and which environmental or microstructural assumption is most fragile. Then describe why the result of a response measured across two excitation or environmental conditions might not be directly comparable. *Answer guide:* define the measurand before the apparatus, identify one calibration-dependent term, and test an alternative physical cause rather than listing properties of the equipment.

**Exercise B — numerical and uncertainty check.** Independently calculate the two numbers in **Ideal contact hardness by fixed area: 5.05 mN → 2.525 GPa; 6.04 mN → 3.02 GPa** and estimate the local sensitivity at the midpoint. Choose an illustrative input standard uncertainty and propagate it using a first-order derivative; identify at least one source of model uncertainty not included by this arithmetic. *Answer guide:* use the model's stated units and bounds, do not round intermediate conversions prematurely, and explicitly label every calculated number synthetic.

**Exercise C — falsification and control.** Design a modest experiment for **indentation, hardness and contact mechanics** with a procedural blank or reference, three independent physical specimens where meaningful, one orthogonal measurement and a predefined exclusion rule. State a possible observation that makes your favored inference untenable. *Answer guide:* record material processing and measurement history, separate technical repeats from sample repeats, and require that the independent test distinguishes competing hypotheses.

**Discussion and decision.** What cross-sectional imaging or independent depth series could demonstrate a substrate effect in a thin coating? Give one conclusion supported directly by a detector observable, one conclusion requiring a fitted model, and one conclusion that cannot yet be made at all. Finish with a single high-value next measurement and explain why its expected information is worth the cost.

<!-- MODEL_9 -->

## Lesson 5.5 — Tension, fatigue and environmental conditioning

### Physical mechanism and its measurable signature

A tensile test determines a stress–strain relation using measured load and geometry, yet engineering and true stress definitions differ after large deformation. Extensometer selection, alignment, gripping, strain rate and temperature matter. For fatigue, cycles-to-failure distributions depend on surface condition, mean stress, frequency and environment; a single surviving specimen does not define a fatigue limit. Conditioning changes polymers and composites through moisture uptake, physical aging or oxidation. Fractography provides a useful post-test mechanism check, but it does not replace proper stress control and sample replication.

**Explicit defining relation.** Nominal engineering stress σ_eng=F/A0; nominal strain ε_eng=ΔL/L0, subject to homogeneous gauge and alignment assumptions.

### Concrete materials-characterization problem

Two lots pass the same ultimate tensile strength target but fail at different cyclic lifetimes after humid conditioning. Design tests to separate chemistry, surface defects and stress ratio.

### Reproducible synthetic worked example

The nearby interactive card titled **Programmed DSC sensible heat flow** changes **Heating rate**. The declared calculation is `10*1.2*beta/60`; the model returns 3.68 mW at 18.4 K/min and 4.26 mW at 21.3 K/min. Thus as the displayed input grows across these two test settings, the calculated output increases. The secant sensitivity over this interval is 0.2 mW per K/min. Check the sign from the governing equation rather than trusting the plotted curve, and confirm dimensional consistency before copying results to the case table. The method is a pedagogical sensitivity test, not a calibrated measurement of a commercial or laboratory specimen.

### Independent experimental and calibration plan

A realistic measurement study of **tension, fatigue and environmental conditioning** would begin with **controlled heating or load protocol with instrument standards**, retaining **sample mass and geometry, ramp or load rate, thermal contact, atmosphere, displacement and baseline**. An independent check would use **empty-pan/reference specimen, unloading or multiple-rate series, physical post-test micrograph**.

### Threats to interpretation and a failure mode

A high tensile strength in a monotonic dry test does not establish reliability under cyclic humid service or variable loading direction.

### Exercises with solution guidance

**Exercise A — physical inference.** Starting from Nominal engineering stress σ_eng=F/A0; nominal strain ε_eng=ΔL/L0, subject to homogeneous gauge and alignment assumptions. explain what is measured, what is inferred, the unit of every symbol and which environmental or microstructural assumption is most fragile. Then describe why the result of the same specimen measured before and after surface preparation might not be directly comparable. *Answer guide:* define the measurand before the apparatus, identify one calibration-dependent term, and test an alternative physical cause rather than listing properties of the equipment.

**Exercise B — numerical and uncertainty check.** Independently calculate the two numbers in **Programmed DSC sensible heat flow: 18.4 K/min → 3.68 mW; 21.3 K/min → 4.26 mW** and estimate the local sensitivity at the midpoint. Choose an illustrative input standard uncertainty and propagate it using a first-order derivative; identify at least one source of model uncertainty not included by this arithmetic. *Answer guide:* use the model's stated units and bounds, do not round intermediate conversions prematurely, and explicitly label every calculated number synthetic.

**Exercise C — falsification and control.** Design a modest experiment for **tension, fatigue and environmental conditioning** with a procedural blank or reference, three independent physical specimens where meaningful, one orthogonal measurement and a predefined exclusion rule. State a possible observation that makes your favored inference untenable. *Answer guide:* record material processing and measurement history, separate technical repeats from sample repeats, and require that the independent test distinguishes competing hypotheses.

**Discussion and decision.** Which combination of strain measurement, fractography and controlled conditioning could reject a simple strength-only lifetime model? Give one conclusion supported directly by a detector observable, one conclusion requiring a fitted model, and one conclusion that cannot yet be made at all. Finish with a single high-value next measurement and explain why its expected information is worth the cost.

## Unit 5 capstone — evidence review and design defense

**Investigation.** An injection-molded polymer has different stiffness values from DMA and quasi-static tension and a broad heat-flow peak. Construct a consistent interpretation without selecting only the most favorable result.

1. **Specify a measurable claim.** Define the target parameter and where the specimens come from. Identify why the sampling population rather than the number of images matters for the engineering claim.
2. **Build a methods matrix.** Choose at least three complementary measurements for **thermal analysis and mechanical property measurements**. For each report the instrument signal, calibration, spatial or information depth, most likely artifact and an orthogonal verification strategy.
3. **Audit two numerical models.** For both cards, calculate the default value, an endpoint and a sensitivity. Mark every quantity synthetic. Explain why agreement with its ideal formula is not sufficient for independent validation.
4. **Budget uncertainty and confounders.** Separate repeatability, reference calibration, specimen variability, geometry and data-reduction sensitivity. Include a possible correlated error and a case where a high pixel count is misleading.
5. **Make an evidence-limited decision.** Write 250 words separating directly supported observations from inferred structure or function. State precisely what additional result would reverse the proposed interpretation.

### Synthesis and transferable reasoning

A characterization workflow is useful when it turns a defined problem into falsifiable evidence. The same specimen can look different when probe volume, preparation, temperature, analysis background or inversion model changes. In **thermal analysis and mechanical property measurements**, the central skill is not knowing a long list of instruments; it is matching each claim to a physically appropriate observable and understanding how to challenge that inference. A laboratory report should acknowledge the subset of the population sampled, not imply that a selected image or a synthetic curve describes every possible specimen. Favor a chain of traceable data over a single polished figure.

