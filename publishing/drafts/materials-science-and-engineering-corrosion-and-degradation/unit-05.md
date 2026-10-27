# Unit 5: High-temperature oxidation and nonaqueous degradation

**Guiding question:** When do protective scales slow oxidation, and when do thermal cycling or reactive gases change the mechanism?

## System view and mechanism boundaries

A furnace part loses strength after hundreds of hot cycles. Determine which observations distinguish oxide growth, scale spallation and mechanical fatigue. The investigation begins with a defined material and state, a particular environment and the time-dependent physical response. Distinguish metal-dissolution, oxide formation, product transport and structural weakening rather than compressing all visible changes into one category. Separate a possible reaction from a verified rate and a local failure mode from an area-averaged measurement. For this unit, a useful answer must identify an observable that would falsify a favored account and an independent observation that constrains the competing mechanism. Neither ideal electrochemical equations nor visual inspection alone resolves all ambiguities.

## Case for comparative investigation

A furnace part loses strength after hundreds of hot cycles. Determine which observations distinguish oxide growth, scale spallation and mechanical fatigue. Draw a decision tree with a first measurement, one targeted control and one observation that would reject the initial theory. Explain why an attractive laboratory result can be irrelevant if the critical field failure occurs on a different length scale or in a different environmental regime. State the uncertainty that a qualified engineer would need to resolve before authorizing a mitigation or reuse decision.

## Lesson 5.1 — Parabolic versus linear oxidation rate laws

### Physical account: governing process and critical limits

High-temperature metals often grow scales through ion and electron transport in oxides. Diffusion-controlled growth commonly produces approximately parabolic thickness or mass-gain-squared behavior over an applicable regime, whereas reaction-limited or nonprotective conditions can approach linear growth. Incubation, transient oxides and spallation complicate observed mass histories. The sign of net mass change does not by itself indicate whether metal consumption or oxide growth dominated.

**Working relation.** (Δm/A)² = k_p t is an ideal parabolic mass-gain form; define units of k_p.

### A concrete case: competing mechanisms

A thermogravimetric trace initially increases smoothly then declines after thermal cycling. Determine whether kinetics changed or product detached.

### Synthetic calculation and guided interpretation

For this lesson use the **Oxide thermal mismatch elastic stress** formula card, with the input variable **Temperature change magnitude** measured in K. Its declared computational expression is `0.001*100*3*dT`. At an illustrative input of 120 K, the output is 36 MPa; at 410 K, it is 123 MPa. The two-point secant sensitivity is 0.3 MPa per K. Interpret the sign and magnitude and then compute a third point without the website to check the calculation. A larger output is not necessarily higher corrosion risk: the meaning of the output depends on whether it is an equilibrium potential, a transport flux, an interfacial response, a thickness margin or an inspection-detection probability.

**Model domain for Parabolic versus linear oxidation rate laws:** Unrelaxed linear-elastic mismatch estimate Eeff=100 GPa, Δα=3 ppm/K, geometry ignored; not an adhesion or failure criterion. Calculate independently before generalizing. Any service claim requires evidence that the model assumptions remain valid under the intended operating conditions.

### Investigation: evidence quality, sampling and controls

For **Parabolic versus linear oxidation rate laws**, document **scale cross-sections and controlled thermal histories**, with **temperature cycling, atmosphere, oxide phases, mass gain, dislodged scale, and strain history**. Challenge the primary conclusion using **micrographs before/after representative cycles and deposit characterization**. Keep independently sampled specimens distinct from repeat readings on the same material, and match environmental histories across treatment groups.

### Diagnostic warning and alternative outcome

Fitting a single parabolic slope across episodes of scale fracture creates misleading transport parameters.

### Assessment: three substantive exercises

**Exercise 1 — mechanism and dimensional reasoning.** Derive or explain the relation `(Δm/A)² = k_p t is an ideal parabolic mass-gain form; define units of k_p.` using its physical assumptions. Assign units to the terms that are actually quantitative; for a qualitative relation, replace it with a measurable definition. Distinguish what can be calculated from a textbook constant from what would require a service-specific measurement. *Answer guidance:* every conversion must declare the material, reacting species, coordinate or control volume and environmental state; reject interpretations whose quantities are at incompatible scales.

**Exercise 2 — independent numerical verification.** Recalculate the synthetic pair (120, 36) and (410, 123) with proper units, then choose a small change near the first point and estimate sensitivity. Discuss how input uncertainty and a violation of **oxide thermal mismatch elastic stress** assumptions would affect a claimed engineering conclusion. *Answer guidance:* calculate from the declared ideal expression, preserve units, and do not convert a formula-generated result into fictional laboratory evidence.

**Exercise 3 — disconfirming experiment.** For the case “A thermogravimetric trace initially increases smoothly then declines after thermal cycling. Determine whether kinetics changed or product detached.” specify a target measurement, a matched control, at least three distinct physical specimens when meaningful, an uncertainty source and a criterion that would reject the proposed cause. *Answer guidance:* distinguish damage depth from area-averaged loss, distinguish reaction-driving force from rate, and make sure the independent test is not based on the same unverified assumption.

### Decision exercise and transferable principle

Compare continuous mass data with post-test cross-sectional oxide thickness and collected spalled products. Write a short decision memo: what is observed; what is inferred; what has not been measured; what alternative still fits; and which further evidence would justify action. Do not mistake a source with scientific-looking units for a calibrated material result. The goal is not to name as many corrosion forms as possible, but to explain precisely how a physical mechanism could produce the observed failure and how another mechanism could be ruled out.

## Lesson 5.2 — Oxide-scale adhesion, thermal mismatch and spallation

### Physical account: governing process and critical limits

A protective oxide must remain continuous during repeated thermal expansion and contraction. Differences in expansion coefficients between metal and oxide generate stresses, while growth stresses, vacancies and defects influence adhesion. Spallation exposes fresh metal and may reset oxidation kinetics. Mass gain alone is especially misleading if a scale can detach before weighing; both coating and substrate must be inspected.

**Working relation.** An illustrative elastic mismatch stress is σ≈E_eff Δα ΔT before plastic relaxation and geometry corrections.

### A concrete case: competing mechanisms

A turbine shield meets average oxidation mass-gain limits but loses sections of protective scale during cool-down. Explain the mismatch.

### Synthetic calculation and guided interpretation

For this lesson use the **Illustrative thermal activation multiplier** formula card, with the input variable **Absolute temperature** measured in K. Its declared computational expression is `Math.exp((80000/8.314462618)*(1/600-1/T))`. At an illustrative input of 662 K, the output is 4.49016943 relative to 600 K; at 784 K, it is 43.1043843 relative to 600 K. The two-point secant sensitivity is 0.31650996 relative to 600 K per K. Interpret the sign and magnitude and then compute a third point without the website to check the calculation. A larger output is not necessarily higher corrosion risk: the meaning of the output depends on whether it is an equilibrium potential, a transport flux, an interfacial response, a thickness margin or an inspection-detection probability.

**Model domain for Oxide-scale adhesion, thermal mismatch and spallation:** Arrhenius Q=80 kJ/mol relative to 600 K and unchanged mechanism; not validated for cycling, phases or service aging. Calculate independently before generalizing. Any service claim requires evidence that the model assumptions remain valid under the intended operating conditions.

### Investigation: evidence quality, sampling and controls

For **Oxide-scale adhesion, thermal mismatch and spallation**, document **scale cross-sections and controlled thermal histories**, with **temperature cycling, atmosphere, oxide phases, mass gain, dislodged scale, and strain history**. Challenge the primary conclusion using **micrographs before/after representative cycles and deposit characterization**. Keep independently sampled specimens distinct from repeat readings on the same material, and match environmental histories across treatment groups.

### Diagnostic warning and alternative outcome

Using an ideal mismatch stress to predict exact spallation time ignores toughness, roughness and cyclic plasticity.

### Assessment: three substantive exercises

**Exercise 1 — mechanism and dimensional reasoning.** Derive or explain the relation `An illustrative elastic mismatch stress is σ≈E_eff Δα ΔT before plastic relaxation and geometry corrections.` using its physical assumptions. Assign units to the terms that are actually quantitative; for a qualitative relation, replace it with a measurable definition. Distinguish what can be calculated from a textbook constant from what would require a service-specific measurement. *Answer guidance:* every conversion must declare the material, reacting species, coordinate or control volume and environmental state; reject interpretations whose quantities are at incompatible scales.

**Exercise 2 — independent numerical verification.** Recalculate the synthetic pair (662, 4.4901694) and (784, 43.104384) with proper units, then choose a small change near the first point and estimate sensitivity. Discuss how input uncertainty and a violation of **illustrative thermal activation multiplier** assumptions would affect a claimed engineering conclusion. *Answer guidance:* calculate from the declared ideal expression, preserve units, and do not convert a formula-generated result into fictional laboratory evidence.

**Exercise 3 — disconfirming experiment.** For the case “A turbine shield meets average oxidation mass-gain limits but loses sections of protective scale during cool-down. Explain the mismatch.” specify a target measurement, a matched control, at least three distinct physical specimens when meaningful, an uncertainty source and a criterion that would reject the proposed cause. *Answer guidance:* distinguish damage depth from area-averaged loss, distinguish reaction-driving force from rate, and make sure the independent test is not based on the same unverified assumption.

### Decision exercise and transferable principle

Image the scale before and after cycling, quantify spall area, and inspect bond-interface fracture. Write a short decision memo: what is observed; what is inferred; what has not been measured; what alternative still fits; and which further evidence would justify action. Do not mistake a source with scientific-looking units for a calibrated material result. The goal is not to name as many corrosion forms as possible, but to explain precisely how a physical mechanism could produce the observed failure and how another mechanism could be ruled out.

<!-- MODEL_8 -->

## Lesson 5.3 — Reactive gases, sulfidation and hot corrosion

### Physical account: governing process and critical limits

High-temperature degradation is shaped by oxygen potential and other species such as sulfur-bearing gases or deposits. Protective oxide stability can be undermined by environmental chemistry, fluxing and composition gradients; the precise mechanism depends on alloy, temperature and deposits. A generic oxidation curve from clean air cannot be transferred to complex exhaust or industrial atmospheres. Sampling and chemical analysis of deposits are often pivotal.

**Working relation.** Chemical potentials of gaseous species govern possible phases; kinetics additionally requires transport and interface reactions.

### A concrete case: competing mechanisms

A heat-exchanger tube survives dry-air trials but pits beneath deposits in service. Assess the evidence needed to characterize the attack.

### Synthetic calculation and guided interpretation

For this lesson use the **Oxide thermal mismatch elastic stress** formula card, with the input variable **Temperature change magnitude** measured in K. Its declared computational expression is `0.001*100*3*dT`. At an illustrative input of 182 K, the output is 54.6 MPa; at 458 K, it is 137.4 MPa. The two-point secant sensitivity is 0.3 MPa per K. Interpret the sign and magnitude and then compute a third point without the website to check the calculation. A larger output is not necessarily higher corrosion risk: the meaning of the output depends on whether it is an equilibrium potential, a transport flux, an interfacial response, a thickness margin or an inspection-detection probability.

**Model domain for Reactive gases, sulfidation and hot corrosion:** Unrelaxed linear-elastic mismatch estimate Eeff=100 GPa, Δα=3 ppm/K, geometry ignored; not an adhesion or failure criterion. Calculate independently before generalizing. Any service claim requires evidence that the model assumptions remain valid under the intended operating conditions.

### Investigation: evidence quality, sampling and controls

For **Reactive gases, sulfidation and hot corrosion**, document **scale cross-sections and controlled thermal histories**, with **temperature cycling, atmosphere, oxide phases, mass gain, dislodged scale, and strain history**. Challenge the primary conclusion using **micrographs before/after representative cycles and deposit characterization**. Keep independently sampled specimens distinct from repeat readings on the same material, and match environmental histories across treatment groups.

### Diagnostic warning and alternative outcome

Equating the presence of a sulfur-rich deposit with proof of a unique sulfidation mechanism exceeds the evidence.

### Assessment: three substantive exercises

**Exercise 1 — mechanism and dimensional reasoning.** Derive or explain the relation `Chemical potentials of gaseous species govern possible phases; kinetics additionally requires transport and interface reactions.` using its physical assumptions. Assign units to the terms that are actually quantitative; for a qualitative relation, replace it with a measurable definition. Distinguish what can be calculated from a textbook constant from what would require a service-specific measurement. *Answer guidance:* every conversion must declare the material, reacting species, coordinate or control volume and environmental state; reject interpretations whose quantities are at incompatible scales.

**Exercise 2 — independent numerical verification.** Recalculate the synthetic pair (182, 54.6) and (458, 137.4) with proper units, then choose a small change near the first point and estimate sensitivity. Discuss how input uncertainty and a violation of **oxide thermal mismatch elastic stress** assumptions would affect a claimed engineering conclusion. *Answer guidance:* calculate from the declared ideal expression, preserve units, and do not convert a formula-generated result into fictional laboratory evidence.

**Exercise 3 — disconfirming experiment.** For the case “A heat-exchanger tube survives dry-air trials but pits beneath deposits in service. Assess the evidence needed to characterize the attack.” specify a target measurement, a matched control, at least three distinct physical specimens when meaningful, an uncertainty source and a criterion that would reject the proposed cause. *Answer guidance:* distinguish damage depth from area-averaged loss, distinguish reaction-driving force from rate, and make sure the independent test is not based on the same unverified assumption.

### Decision exercise and transferable principle

Characterize deposits, depth profiles and scale phases from damaged and unaffected sites. Write a short decision memo: what is observed; what is inferred; what has not been measured; what alternative still fits; and which further evidence would justify action. Do not mistake a source with scientific-looking units for a calibrated material result. The goal is not to name as many corrosion forms as possible, but to explain precisely how a physical mechanism could produce the observed failure and how another mechanism could be ruled out.

## Lesson 5.4 — Diffusion barriers, coatings and thermal cycling

### Physical account: governing process and critical limits

Diffusion-resistant coatings and bond coats can improve high-temperature lifetime but can introduce interdiffusion zones, phase changes and residual stresses. A coating stack is a multilayer mechanical and chemical system rather than an immutable shield. Thermal cycles and process impurities can change oxide growth paths and interface toughness. Service qualification therefore requires both thermal exposure and structural integrity testing.

**Working relation.** For a first-order diffusion length estimate, ℓ≈sqrt(Dt), under constant D and appropriate geometry.

### A concrete case: competing mechanisms

A coated component fails after repeated starts although it passes a long constant-temperature furnace test. Propose what each protocol overlooks.

### Synthetic calculation and guided interpretation

For this lesson use the **Illustrative thermal activation multiplier** formula card, with the input variable **Absolute temperature** measured in K. Its declared computational expression is `Math.exp((80000/8.314462618)*(1/600-1/T))`. At an illustrative input of 688 K, the output is 7.77688943 relative to 600 K; at 806 K, it is 60.2565495 relative to 600 K. The two-point secant sensitivity is 0.44474288 relative to 600 K per K. Interpret the sign and magnitude and then compute a third point without the website to check the calculation. A larger output is not necessarily higher corrosion risk: the meaning of the output depends on whether it is an equilibrium potential, a transport flux, an interfacial response, a thickness margin or an inspection-detection probability.

**Model domain for Diffusion barriers, coatings and thermal cycling:** Arrhenius Q=80 kJ/mol relative to 600 K and unchanged mechanism; not validated for cycling, phases or service aging. Calculate independently before generalizing. Any service claim requires evidence that the model assumptions remain valid under the intended operating conditions.

### Investigation: evidence quality, sampling and controls

For **Diffusion barriers, coatings and thermal cycling**, document **scale cross-sections and controlled thermal histories**, with **temperature cycling, atmosphere, oxide phases, mass gain, dislodged scale, and strain history**. Challenge the primary conclusion using **micrographs before/after representative cycles and deposit characterization**. Keep independently sampled specimens distinct from repeat readings on the same material, and match environmental histories across treatment groups.

### Diagnostic warning and alternative outcome

Extending a constant-temperature lifetime to cycling ignores initiation and loss of barrier integrity.

### Assessment: three substantive exercises

**Exercise 1 — mechanism and dimensional reasoning.** Derive or explain the relation `For a first-order diffusion length estimate, ℓ≈sqrt(Dt), under constant D and appropriate geometry.` using its physical assumptions. Assign units to the terms that are actually quantitative; for a qualitative relation, replace it with a measurable definition. Distinguish what can be calculated from a textbook constant from what would require a service-specific measurement. *Answer guidance:* every conversion must declare the material, reacting species, coordinate or control volume and environmental state; reject interpretations whose quantities are at incompatible scales.

**Exercise 2 — independent numerical verification.** Recalculate the synthetic pair (688, 7.7768894) and (806, 60.25655) with proper units, then choose a small change near the first point and estimate sensitivity. Discuss how input uncertainty and a violation of **illustrative thermal activation multiplier** assumptions would affect a claimed engineering conclusion. *Answer guidance:* calculate from the declared ideal expression, preserve units, and do not convert a formula-generated result into fictional laboratory evidence.

**Exercise 3 — disconfirming experiment.** For the case “A coated component fails after repeated starts although it passes a long constant-temperature furnace test. Propose what each protocol overlooks.” specify a target measurement, a matched control, at least three distinct physical specimens when meaningful, an uncertainty source and a criterion that would reject the proposed cause. *Answer guidance:* distinguish damage depth from area-averaged loss, distinguish reaction-driving force from rate, and make sure the independent test is not based on the same unverified assumption.

### Decision exercise and transferable principle

Cross-section coating interfaces before and after representative cycles and record failure origin. Write a short decision memo: what is observed; what is inferred; what has not been measured; what alternative still fits; and which further evidence would justify action. Do not mistake a source with scientific-looking units for a calibrated material result. The goal is not to name as many corrosion forms as possible, but to explain precisely how a physical mechanism could produce the observed failure and how another mechanism could be ruled out.

<!-- MODEL_9 -->

## Lesson 5.5 — Temperature dependence and accelerated testing

### Physical account: governing process and critical limits

Arrhenius-type rate sensitivity is often useful over a limited mechanism-preserving temperature range, but activation energies inferred from a narrow test set may not extrapolate through phase transitions or changing oxygen potentials. Thermal acceleration can alter the controlling mechanism, not merely its speed. Rates from accelerated tests should be viewed as conditional hypotheses and checked against credible service observations.

**Working relation.** k(T) = k₀ exp(−Q/RT) assumes a dominant activation barrier over the fitted range.

### A concrete case: competing mechanisms

A material accelerated at 900 °C appears better than another, while 600 °C field components show the opposite ranking. Identify possible mechanism changes.

### Synthetic calculation and guided interpretation

For this lesson use the **Oxide thermal mismatch elastic stress** formula card, with the input variable **Temperature change magnitude** measured in K. Its declared computational expression is `0.001*100*3*dT`. At an illustrative input of 245 K, the output is 73.5 MPa; at 507 K, it is 152.1 MPa. The two-point secant sensitivity is 0.3 MPa per K. Interpret the sign and magnitude and then compute a third point without the website to check the calculation. A larger output is not necessarily higher corrosion risk: the meaning of the output depends on whether it is an equilibrium potential, a transport flux, an interfacial response, a thickness margin or an inspection-detection probability.

**Model domain for Temperature dependence and accelerated testing:** Unrelaxed linear-elastic mismatch estimate Eeff=100 GPa, Δα=3 ppm/K, geometry ignored; not an adhesion or failure criterion. Calculate independently before generalizing. Any service claim requires evidence that the model assumptions remain valid under the intended operating conditions.

### Investigation: evidence quality, sampling and controls

For **Temperature dependence and accelerated testing**, document **scale cross-sections and controlled thermal histories**, with **temperature cycling, atmosphere, oxide phases, mass gain, dislodged scale, and strain history**. Challenge the primary conclusion using **micrographs before/after representative cycles and deposit characterization**. Keep independently sampled specimens distinct from repeat readings on the same material, and match environmental histories across treatment groups.

### Diagnostic warning and alternative outcome

Blind extrapolation across a phase change or critical environmental threshold can invert material selection.

### Assessment: three substantive exercises

**Exercise 1 — mechanism and dimensional reasoning.** Derive or explain the relation `k(T) = k₀ exp(−Q/RT) assumes a dominant activation barrier over the fitted range.` using its physical assumptions. Assign units to the terms that are actually quantitative; for a qualitative relation, replace it with a measurable definition. Distinguish what can be calculated from a textbook constant from what would require a service-specific measurement. *Answer guidance:* every conversion must declare the material, reacting species, coordinate or control volume and environmental state; reject interpretations whose quantities are at incompatible scales.

**Exercise 2 — independent numerical verification.** Recalculate the synthetic pair (245, 73.5) and (507, 152.1) with proper units, then choose a small change near the first point and estimate sensitivity. Discuss how input uncertainty and a violation of **oxide thermal mismatch elastic stress** assumptions would affect a claimed engineering conclusion. *Answer guidance:* calculate from the declared ideal expression, preserve units, and do not convert a formula-generated result into fictional laboratory evidence.

**Exercise 3 — disconfirming experiment.** For the case “A material accelerated at 900 °C appears better than another, while 600 °C field components show the opposite ranking. Identify possible mechanism changes.” specify a target measurement, a matched control, at least three distinct physical specimens when meaningful, an uncertainty source and a criterion that would reject the proposed cause. *Answer guidance:* distinguish damage depth from area-averaged loss, distinguish reaction-driving force from rate, and make sure the independent test is not based on the same unverified assumption.

### Decision exercise and transferable principle

Test multiple temperatures and inspect oxidation products and morphology for mechanistic continuity. Write a short decision memo: what is observed; what is inferred; what has not been measured; what alternative still fits; and which further evidence would justify action. Do not mistake a source with scientific-looking units for a calibrated material result. The goal is not to name as many corrosion forms as possible, but to explain precisely how a physical mechanism could produce the observed failure and how another mechanism could be ruled out.

## Unit 5 capstone — evidence and engineering defense

**Complex case:** A furnace part loses strength after hundreds of hot cycles. Determine which observations distinguish oxide growth, scale spallation and mechanical fatigue.

1. **System definition for High-temperature oxidation and nonaqueous degradation:** Sketch the material, phase boundaries, electrolyte or gas paths, stressed features, wet–dry or thermal cycles and measurement locations. State precisely whether the main concern is uniform thinning, maximum pit depth, a crack, surface-electrical function or loss of protective scale.
2. **Two competing mechanisms:** Construct a table with initiating cause, expected spatial pattern, predicted time dependence, contrary evidence and an orthogonal method. Identify which mechanism might operate after rather than before the observed damage.
3. **Numerical audit:** Recalculate both of this unit's models at their default inputs and at the limits of the slider range. Describe the units and whether the model concerns driving force, rate, geometry, or inspection uncertainty. Show at least one reason the model might not apply to the given case.
4. **Sampling and uncertainty:** Build a hierarchy of independent assets or coupons, repeated measurements and local map points. Include instrument calibration, specimen differences, exposure mismatch and the possibility that a rare maximum is missed by ordinary sampling.
5. **Decision note:** Produce a 400-word recommendation with immediate safety implications separated from follow-up research, a repair or monitor option, a cost of wrong inference, and the exact evidence that would change the ranking. Do not claim service life from synthetic data.

### Connecting this unit to materials engineering

A corrosion investigation improves when it preserves the distinction between an electrochemical mechanism, the spatial manifestation of damage, an instrument response and a decision on whether equipment remains fit for service. In **high-temperature oxidation and nonaqueous degradation**, a defensible conclusion follows a chain of falsifiable physical claims rather than a single parameter selected because it is easy to compute. The mathematics should expose sensitivity and uncertainty, while site observations determine whether the equations apply at all. The companion models are an instructional starting point; professional asset decisions need controlled tests, standards and real-world verification.
