# Unit 2: Interfacial kinetics, transport and measurement

**Guiding question:** How do charge transfer, transport, and instrumental resistance shape the observed corrosion response?

## System view and mechanism boundaries

Two electrodes have similar measured open-circuit potentials but exhibit very different mass loss. Establish a defensible test program before assigning corrosion rates. The investigation begins with a defined material and state, a particular environment and the time-dependent physical response. Distinguish metal-dissolution, oxide formation, product transport and structural weakening rather than compressing all visible changes into one category. Separate a possible reaction from a verified rate and a local failure mode from an area-averaged measurement. For this unit, a useful answer must identify an observable that would falsify a favored account and an independent observation that constrains the competing mechanism. Neither ideal electrochemical equations nor visual inspection alone resolves all ambiguities.

## Case for comparative investigation

Two electrodes have similar measured open-circuit potentials but exhibit very different mass loss. Establish a defensible test program before assigning corrosion rates. Draw a decision tree with a first measurement, one targeted control and one observation that would reject the initial theory. Explain why an attractive laboratory result can be irrelevant if the critical field failure occurs on a different length scale or in a different environmental regime. State the uncertainty that a qualified engineer would need to resolve before authorizing a mitigation or reuse decision.

## Lesson 2.1 — Activation polarization and charge-transfer barriers

### Physical account: governing process and critical limits

An electrochemical reaction must overcome interfacial activation barriers even if thermodynamics favors it. Butler–Volmer kinetics relates net faradaic current density to overpotential in a simplified reversible-electrode setting, while anodic and cathodic Tafel regions emerge only when a single exponential dominates. Exchange current density and transfer coefficients depend on surface chemistry, temperature and the reaction; fit parameters need reported uncertainty. Surface films and multiple parallel reactions may violate textbook assumptions.

**Working relation.** i = i₀[exp(αₐnFη/RT) − exp(−α꜀nFη/RT)] in a single-reaction model.

### A concrete case: competing mechanisms

Two polished steel coupons develop the same potential but different current responses after surface conditioning. Diagnose which kinetic quantities may have changed.

### Synthetic calculation and guided interpretation

For this lesson use the **Single-branch anodic Tafel current** formula card, with the input variable **Anodic overpotential** measured in V. Its declared computational expression is `0.5*Math.pow(10,eta/0.12)`. At an illustrative input of 0.0288 V, the output is 0.868900414 µA/cm²; at 0.1044 V, it is 3.70655121 µA/cm². The two-point secant sensitivity is 37.535063 µA/cm² per V. Interpret the sign and magnitude and then compute a third point without the website to check the calculation. A larger output is not necessarily higher corrosion risk: the meaning of the output depends on whether it is an equilibrium potential, a transport flux, an interfacial response, a thickness margin or an inspection-detection probability.

**Model domain for Activation polarization and charge-transfer barriers:** Anodic Tafel branch only, exchange-scale 0.5 µA/cm², 0.12 V/decade; excludes reverse, mass transfer and film effects. Calculate independently before generalizing. Any service claim requires evidence that the model assumptions remain valid under the intended operating conditions.

### Investigation: evidence quality, sampling and controls

For **Activation polarization and charge-transfer barriers**, document **steady-state electrical responses and independent gravimetry**, with **open-circuit stabilization, polarization window, solution resistance, area, flow and transient current**. Challenge the primary conclusion using **matched mass-loss and localized depth profiles**. Keep independently sampled specimens distinct from repeat readings on the same material, and match environmental histories across treatment groups.

### Diagnostic warning and alternative outcome

Forcing a straight Tafel line through capacitive or mass-transport-limited data creates unjustified corrosion currents.

### Assessment: three substantive exercises

**Exercise 1 — mechanism and dimensional reasoning.** Derive or explain the relation `i = i₀[exp(αₐnFη/RT) − exp(−α꜀nFη/RT)] in a single-reaction model.` using its physical assumptions. Assign units to the terms that are actually quantitative; for a qualitative relation, replace it with a measurable definition. Distinguish what can be calculated from a textbook constant from what would require a service-specific measurement. *Answer guidance:* every conversion must declare the material, reacting species, coordinate or control volume and environmental state; reject interpretations whose quantities are at incompatible scales.

**Exercise 2 — independent numerical verification.** Recalculate the synthetic pair (0.0288, 0.86890041) and (0.1044, 3.7065512) with proper units, then choose a small change near the first point and estimate sensitivity. Discuss how input uncertainty and a violation of **single-branch anodic tafel current** assumptions would affect a claimed engineering conclusion. *Answer guidance:* calculate from the declared ideal expression, preserve units, and do not convert a formula-generated result into fictional laboratory evidence.

**Exercise 3 — disconfirming experiment.** For the case “Two polished steel coupons develop the same potential but different current responses after surface conditioning. Diagnose which kinetic quantities may have changed.” specify a target measurement, a matched control, at least three distinct physical specimens when meaningful, an uncertainty source and a criterion that would reject the proposed cause. *Answer guidance:* distinguish damage depth from area-averaged loss, distinguish reaction-driving force from rate, and make sure the independent test is not based on the same unverified assumption.

### Decision exercise and transferable principle

Check forward and reverse scans, stabilization and the extent of linear log-current regions before interpreting a fit. Write a short decision memo: what is observed; what is inferred; what has not been measured; what alternative still fits; and which further evidence would justify action. Do not mistake a source with scientific-looking units for a calibrated material result. The goal is not to name as many corrosion forms as possible, but to explain precisely how a physical mechanism could produce the observed failure and how another mechanism could be ruled out.

## Lesson 2.2 — Mixed-potential theory and corrosion-current estimates

### Physical account: governing process and critical limits

A freely corroding electrode operates where the net external faradaic current is approximately zero, not where anodic metal dissolution has stopped. The local metal-dissolution and cathodic currents balance, allowing potentially significant corrosion under zero net measured current. For a simplified single anodic and cathodic couple, the intersection of kinetic branches gives a corrosion potential and reaction current. More reactions, transport limits and heterogeneous surfaces require a richer description.

**Working relation.** i_total(E_corr) = i_anodic(E_corr) + i_cathodic(E_corr) = 0; i_corr is a partial current magnitude.

### A concrete case: competing mechanisms

An immersed alloy has a stable open-circuit potential yet progressively loses mass. Explain the conservation of current without invoking a measurement defect.

### Synthetic calculation and guided interpretation

For this lesson use the **Stern–Geary estimated corrosion current** formula card, with the input variable **Polarization resistance** measured in Ω·cm². Its declared computational expression is `26000/Rp`. At an illustrative input of 6945 Ω·cm², the output is 3.7437005 µA/cm²; at 18835 Ω·cm², it is 1.38040881 µA/cm². The two-point secant sensitivity is -0.00019876297 µA/cm² per Ω·cm². Interpret the sign and magnitude and then compute a third point without the website to check the calculation. A larger output is not necessarily higher corrosion risk: the meaning of the output depends on whether it is an equilibrium potential, a transport flux, an interfacial response, a thickness margin or an inspection-detection probability.

**Model domain for Mixed-potential theory and corrosion-current estimates:** Illustrative coefficient B=26 mV and valid small-signal activation-controlled conditions; Rp excludes uncompensated solution resistance. Calculate independently before generalizing. Any service claim requires evidence that the model assumptions remain valid under the intended operating conditions.

### Investigation: evidence quality, sampling and controls

For **Mixed-potential theory and corrosion-current estimates**, document **steady-state electrical responses and independent gravimetry**, with **open-circuit stabilization, polarization window, solution resistance, area, flow and transient current**. Challenge the primary conclusion using **matched mass-loss and localized depth profiles**. Keep independently sampled specimens distinct from repeat readings on the same material, and match environmental histories across treatment groups.

### Diagnostic warning and alternative outcome

Confusing an open-circuit net current of zero with an actual corrosion rate of zero obscures the main phenomenon.

### Assessment: three substantive exercises

**Exercise 1 — mechanism and dimensional reasoning.** Derive or explain the relation `i_total(E_corr) = i_anodic(E_corr) + i_cathodic(E_corr) = 0; i_corr is a partial current magnitude.` using its physical assumptions. Assign units to the terms that are actually quantitative; for a qualitative relation, replace it with a measurable definition. Distinguish what can be calculated from a textbook constant from what would require a service-specific measurement. *Answer guidance:* every conversion must declare the material, reacting species, coordinate or control volume and environmental state; reject interpretations whose quantities are at incompatible scales.

**Exercise 2 — independent numerical verification.** Recalculate the synthetic pair (6945, 3.7437005) and (18835, 1.3804088) with proper units, then choose a small change near the first point and estimate sensitivity. Discuss how input uncertainty and a violation of **stern–geary estimated corrosion current** assumptions would affect a claimed engineering conclusion. *Answer guidance:* calculate from the declared ideal expression, preserve units, and do not convert a formula-generated result into fictional laboratory evidence.

**Exercise 3 — disconfirming experiment.** For the case “An immersed alloy has a stable open-circuit potential yet progressively loses mass. Explain the conservation of current without invoking a measurement defect.” specify a target measurement, a matched control, at least three distinct physical specimens when meaningful, an uncertainty source and a criterion that would reject the proposed cause. *Answer guidance:* distinguish damage depth from area-averaged loss, distinguish reaction-driving force from rate, and make sure the independent test is not based on the same unverified assumption.

### Decision exercise and transferable principle

Compare gravimetric change with electrochemical current estimates and identify reactions not captured by the minimal model. Write a short decision memo: what is observed; what is inferred; what has not been measured; what alternative still fits; and which further evidence would justify action. Do not mistake a source with scientific-looking units for a calibrated material result. The goal is not to name as many corrosion forms as possible, but to explain precisely how a physical mechanism could produce the observed failure and how another mechanism could be ruled out.

<!-- MODEL_2 -->

## Lesson 2.3 — Linear polarization resistance and Stern–Geary

### Physical account: governing process and critical limits

Near a steady corrosion potential, the small-signal slope of electrode potential against current density defines a polarization resistance. In appropriate activation-controlled systems, a Stern–Geary coefficient connects resistance to corrosion current density. The coefficient depends on anodic and cathodic Tafel slopes and is not universal. Uncompensated solution resistance, double-layer charging, nonstationary films and localized corrosion can bias the apparent result; the technique most directly relates to general corrosion.

**Working relation.** i_corr = B/R_p; with B=βₐβ꜀/[2.303(βₐ+β꜀)] for compatible slope units.

### A concrete case: competing mechanisms

An engineer extrapolates a coupon penetration rate from a single short polarization scan and uses it to predict the deepest pit. Evaluate this inference.

### Synthetic calculation and guided interpretation

For this lesson use the **Single-branch anodic Tafel current** formula card, with the input variable **Anodic overpotential** measured in V. Its declared computational expression is `0.5*Math.pow(10,eta/0.12)`. At an illustrative input of 0.045 V, the output is 1.18568685 µA/cm²; at 0.117 V, it is 4.72030438 µA/cm². The two-point secant sensitivity is 49.09191 µA/cm² per V. Interpret the sign and magnitude and then compute a third point without the website to check the calculation. A larger output is not necessarily higher corrosion risk: the meaning of the output depends on whether it is an equilibrium potential, a transport flux, an interfacial response, a thickness margin or an inspection-detection probability.

**Model domain for Linear polarization resistance and Stern–Geary:** Anodic Tafel branch only, exchange-scale 0.5 µA/cm², 0.12 V/decade; excludes reverse, mass transfer and film effects. Calculate independently before generalizing. Any service claim requires evidence that the model assumptions remain valid under the intended operating conditions.

### Investigation: evidence quality, sampling and controls

For **Linear polarization resistance and Stern–Geary**, document **steady-state electrical responses and independent gravimetry**, with **open-circuit stabilization, polarization window, solution resistance, area, flow and transient current**. Challenge the primary conclusion using **matched mass-loss and localized depth profiles**. Keep independently sampled specimens distinct from repeat readings on the same material, and match environmental histories across treatment groups.

### Diagnostic warning and alternative outcome

A fixed coefficient borrowed from another alloy/environment may dominate error even if R_p is precisely measured.

### Assessment: three substantive exercises

**Exercise 1 — mechanism and dimensional reasoning.** Derive or explain the relation `i_corr = B/R_p; with B=βₐβ꜀/[2.303(βₐ+β꜀)] for compatible slope units.` using its physical assumptions. Assign units to the terms that are actually quantitative; for a qualitative relation, replace it with a measurable definition. Distinguish what can be calculated from a textbook constant from what would require a service-specific measurement. *Answer guidance:* every conversion must declare the material, reacting species, coordinate or control volume and environmental state; reject interpretations whose quantities are at incompatible scales.

**Exercise 2 — independent numerical verification.** Recalculate the synthetic pair (0.045, 1.1856869) and (0.117, 4.7203044) with proper units, then choose a small change near the first point and estimate sensitivity. Discuss how input uncertainty and a violation of **single-branch anodic tafel current** assumptions would affect a claimed engineering conclusion. *Answer guidance:* calculate from the declared ideal expression, preserve units, and do not convert a formula-generated result into fictional laboratory evidence.

**Exercise 3 — disconfirming experiment.** For the case “An engineer extrapolates a coupon penetration rate from a single short polarization scan and uses it to predict the deepest pit. Evaluate this inference.” specify a target measurement, a matched control, at least three distinct physical specimens when meaningful, an uncertainty source and a criterion that would reject the proposed cause. *Answer guidance:* distinguish damage depth from area-averaged loss, distinguish reaction-driving force from rate, and make sure the independent test is not based on the same unverified assumption.

### Decision exercise and transferable principle

Validate instrument resistance correction and compare electrochemical estimates to mass-loss coupons over matched exposure. Write a short decision memo: what is observed; what is inferred; what has not been measured; what alternative still fits; and which further evidence would justify action. Do not mistake a source with scientific-looking units for a calibrated material result. The goal is not to name as many corrosion forms as possible, but to explain precisely how a physical mechanism could produce the observed failure and how another mechanism could be ruled out.

## Lesson 2.4 — Transport-limited oxygen reduction and boundary layers

### Physical account: governing process and critical limits

When reactants must cross a stagnant film or diffuse through porous deposits, transport can cap the cathodic current. A simple planar diffusion-film approximation gives limiting current proportional to bulk concentration and inversely proportional to the diffusion-layer thickness. Agitation, temperature, gas content and geometry may change this layer. In a real pipe turbulent near-wall structure, deposits and biofilms can defeat the planar picture and cause localized gradients.

**Working relation.** i_lim = n F D C/δ for an ideal planar steady diffusion layer with consistent SI dimensions.

### A concrete case: competing mechanisms

A pumping change accelerates attack at some bends while other regions improve. Identify why the dependence on flow cannot be monotonic in every regime.

### Synthetic calculation and guided interpretation

For this lesson use the **Stern–Geary estimated corrosion current** formula card, with the input variable **Polarization resistance** measured in Ω·cm². Its declared computational expression is `26000/Rp`. At an illustrative input of 9555 Ω·cm², the output is 2.72108844 µA/cm²; at 20865 Ω·cm², it is 1.24610592 µA/cm². The two-point secant sensitivity is -0.00013041402 µA/cm² per Ω·cm². Interpret the sign and magnitude and then compute a third point without the website to check the calculation. A larger output is not necessarily higher corrosion risk: the meaning of the output depends on whether it is an equilibrium potential, a transport flux, an interfacial response, a thickness margin or an inspection-detection probability.

**Model domain for Transport-limited oxygen reduction and boundary layers:** Illustrative coefficient B=26 mV and valid small-signal activation-controlled conditions; Rp excludes uncompensated solution resistance. Calculate independently before generalizing. Any service claim requires evidence that the model assumptions remain valid under the intended operating conditions.

### Investigation: evidence quality, sampling and controls

For **Transport-limited oxygen reduction and boundary layers**, document **steady-state electrical responses and independent gravimetry**, with **open-circuit stabilization, polarization window, solution resistance, area, flow and transient current**. Challenge the primary conclusion using **matched mass-loss and localized depth profiles**. Keep independently sampled specimens distinct from repeat readings on the same material, and match environmental histories across treatment groups.

### Diagnostic warning and alternative outcome

An extrapolated transport-limited current cannot be assigned as metal dissolution current without charge-balance context.

### Assessment: three substantive exercises

**Exercise 1 — mechanism and dimensional reasoning.** Derive or explain the relation `i_lim = n F D C/δ for an ideal planar steady diffusion layer with consistent SI dimensions.` using its physical assumptions. Assign units to the terms that are actually quantitative; for a qualitative relation, replace it with a measurable definition. Distinguish what can be calculated from a textbook constant from what would require a service-specific measurement. *Answer guidance:* every conversion must declare the material, reacting species, coordinate or control volume and environmental state; reject interpretations whose quantities are at incompatible scales.

**Exercise 2 — independent numerical verification.** Recalculate the synthetic pair (9555, 2.7210884) and (20865, 1.2461059) with proper units, then choose a small change near the first point and estimate sensitivity. Discuss how input uncertainty and a violation of **stern–geary estimated corrosion current** assumptions would affect a claimed engineering conclusion. *Answer guidance:* calculate from the declared ideal expression, preserve units, and do not convert a formula-generated result into fictional laboratory evidence.

**Exercise 3 — disconfirming experiment.** For the case “A pumping change accelerates attack at some bends while other regions improve. Identify why the dependence on flow cannot be monotonic in every regime.” specify a target measurement, a matched control, at least three distinct physical specimens when meaningful, an uncertainty source and a criterion that would reject the proposed cause. *Answer guidance:* distinguish damage depth from area-averaged loss, distinguish reaction-driving force from rate, and make sure the independent test is not based on the same unverified assumption.

### Decision exercise and transferable principle

Map dissolved oxygen and flow regime and compare exposed vs shielded coupons before interpreting a plateau. Write a short decision memo: what is observed; what is inferred; what has not been measured; what alternative still fits; and which further evidence would justify action. Do not mistake a source with scientific-looking units for a calibrated material result. The goal is not to name as many corrosion forms as possible, but to explain precisely how a physical mechanism could produce the observed failure and how another mechanism could be ruled out.

<!-- MODEL_3 -->

## Lesson 2.5 — Faraday law, equivalent weight and penetration rate

### Physical account: governing process and critical limits

Faraday law equates electric charge to moles of electrons transferred, allowing a hypothetical uniform metal loss to be computed from a known dissolution current density. Alloy equivalent weight depends on assumed dissolving species and valence, and density connects removed mass to an average thickness. This rate is an area-averaged quantity, which may have little relevance to the deepest active pit. Product-film redox currents must not be automatically treated as net metal consumption.

**Working relation.** Uniform penetration v = i M/(n F ρ), with current density in A m⁻² and ρ in kg m⁻³, giving m s⁻¹.

### A concrete case: competing mechanisms

A uniform carbon-steel plate and a passivated stainless-steel plate show similar transient currents over one minute. Test why long-term wastage could differ.

### Synthetic calculation and guided interpretation

For this lesson use the **Single-branch anodic Tafel current** formula card, with the input variable **Anodic overpotential** measured in V. Its declared computational expression is `0.5*Math.pow(10,eta/0.12)`. At an illustrative input of 0.0612 V, the output is 1.61796828 µA/cm²; at 0.1296 V, it is 6.01132217 µA/cm². The two-point secant sensitivity is 64.23032 µA/cm² per V. Interpret the sign and magnitude and then compute a third point without the website to check the calculation. A larger output is not necessarily higher corrosion risk: the meaning of the output depends on whether it is an equilibrium potential, a transport flux, an interfacial response, a thickness margin or an inspection-detection probability.

**Model domain for Faraday law, equivalent weight and penetration rate:** Anodic Tafel branch only, exchange-scale 0.5 µA/cm², 0.12 V/decade; excludes reverse, mass transfer and film effects. Calculate independently before generalizing. Any service claim requires evidence that the model assumptions remain valid under the intended operating conditions.

### Investigation: evidence quality, sampling and controls

For **Faraday law, equivalent weight and penetration rate**, document **steady-state electrical responses and independent gravimetry**, with **open-circuit stabilization, polarization window, solution resistance, area, flow and transient current**. Challenge the primary conclusion using **matched mass-loss and localized depth profiles**. Keep independently sampled specimens distinct from repeat readings on the same material, and match environmental histories across treatment groups.

### Diagnostic warning and alternative outcome

Confusing microampere per square centimeter with ampere per square meter can introduce a factor of ten or more.

### Assessment: three substantive exercises

**Exercise 1 — mechanism and dimensional reasoning.** Derive or explain the relation `Uniform penetration v = i M/(n F ρ), with current density in A m⁻² and ρ in kg m⁻³, giving m s⁻¹.` using its physical assumptions. Assign units to the terms that are actually quantitative; for a qualitative relation, replace it with a measurable definition. Distinguish what can be calculated from a textbook constant from what would require a service-specific measurement. *Answer guidance:* every conversion must declare the material, reacting species, coordinate or control volume and environmental state; reject interpretations whose quantities are at incompatible scales.

**Exercise 2 — independent numerical verification.** Recalculate the synthetic pair (0.0612, 1.6179683) and (0.1296, 6.0113222) with proper units, then choose a small change near the first point and estimate sensitivity. Discuss how input uncertainty and a violation of **single-branch anodic tafel current** assumptions would affect a claimed engineering conclusion. *Answer guidance:* calculate from the declared ideal expression, preserve units, and do not convert a formula-generated result into fictional laboratory evidence.

**Exercise 3 — disconfirming experiment.** For the case “A uniform carbon-steel plate and a passivated stainless-steel plate show similar transient currents over one minute. Test why long-term wastage could differ.” specify a target measurement, a matched control, at least three distinct physical specimens when meaningful, an uncertainty source and a criterion that would reject the proposed cause. *Answer guidance:* distinguish damage depth from area-averaged loss, distinguish reaction-driving force from rate, and make sure the independent test is not based on the same unverified assumption.

### Decision exercise and transferable principle

Use independent mass balance and mapped depth measurements to challenge the assumed dissolution efficiency. Write a short decision memo: what is observed; what is inferred; what has not been measured; what alternative still fits; and which further evidence would justify action. Do not mistake a source with scientific-looking units for a calibrated material result. The goal is not to name as many corrosion forms as possible, but to explain precisely how a physical mechanism could produce the observed failure and how another mechanism could be ruled out.

## Unit 2 capstone — evidence and engineering defense

**Complex case:** Two electrodes have similar measured open-circuit potentials but exhibit very different mass loss. Establish a defensible test program before assigning corrosion rates.

1. **System definition for Interfacial kinetics, transport and measurement:** Sketch the material, phase boundaries, electrolyte or gas paths, stressed features, wet–dry or thermal cycles and measurement locations. State precisely whether the main concern is uniform thinning, maximum pit depth, a crack, surface-electrical function or loss of protective scale.
2. **Two competing mechanisms:** Construct a table with initiating cause, expected spatial pattern, predicted time dependence, contrary evidence and an orthogonal method. Identify which mechanism might operate after rather than before the observed damage.
3. **Numerical audit:** Recalculate both of this unit's models at their default inputs and at the limits of the slider range. Describe the units and whether the model concerns driving force, rate, geometry, or inspection uncertainty. Show at least one reason the model might not apply to the given case.
4. **Sampling and uncertainty:** Build a hierarchy of independent assets or coupons, repeated measurements and local map points. Include instrument calibration, specimen differences, exposure mismatch and the possibility that a rare maximum is missed by ordinary sampling.
5. **Decision note:** Produce a 400-word recommendation with immediate safety implications separated from follow-up research, a repair or monitor option, a cost of wrong inference, and the exact evidence that would change the ranking. Do not claim service life from synthetic data.

### Connecting this unit to materials engineering

A corrosion investigation improves when it preserves the distinction between an electrochemical mechanism, the spatial manifestation of damage, an instrument response and a decision on whether equipment remains fit for service. In **interfacial kinetics, transport and measurement**, a defensible conclusion follows a chain of falsifiable physical claims rather than a single parameter selected because it is easy to compute. The mathematics should expose sensitivity and uncertainty, while site observations determine whether the equations apply at all. The companion models are an instructional starting point; professional asset decisions need controlled tests, standards and real-world verification.
