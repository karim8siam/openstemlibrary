# Unit 3: Localized corrosion and coupled failure

**Guiding question:** Why can a component perforate even though its average loss looks insignificant?

## System view and mechanism boundaries

A chloride-exposed stainless-steel heat-exchanger plate develops isolated pits and leakage. Build competing explanations for initiation, propagation, and leakage. The investigation begins with a defined material and state, a particular environment and the time-dependent physical response. Distinguish metal-dissolution, oxide formation, product transport and structural weakening rather than compressing all visible changes into one category. Separate a possible reaction from a verified rate and a local failure mode from an area-averaged measurement. For this unit, a useful answer must identify an observable that would falsify a favored account and an independent observation that constrains the competing mechanism. Neither ideal electrochemical equations nor visual inspection alone resolves all ambiguities.

## Case for comparative investigation

A chloride-exposed stainless-steel heat-exchanger plate develops isolated pits and leakage. Build competing explanations for initiation, propagation, and leakage. Draw a decision tree with a first measurement, one targeted control and one observation that would reject the initial theory. Explain why an attractive laboratory result can be irrelevant if the critical field failure occurs on a different length scale or in a different environmental regime. State the uncertainty that a qualified engineer would need to resolve before authorizing a mitigation or reuse decision.

## Lesson 3.1 — Uniform corrosion, metal loss and thickness mapping

### Physical account: governing process and critical limits

Uniform corrosion produces approximately distributed loss that may be managed through structural margins and planned inspection, but even apparently uniform attack contains spatial variability. Ultrasound thickness measurements cover discrete paths and can miss a hot spot between sampling points; radiography and scanning methods have their own sensitivity and access limitations. The correct quantity for a pressure boundary is often local remaining wall and its uncertainty, not the average coupon rate.

**Working relation.** For ideal constant uniform loss, remaining thickness t(t_year) = t₀ − v t_year.

### A concrete case: competing mechanisms

A storage tank shows 0.08 mm per year average coupon loss and one isolated thin spot. Decide which result should govern a risk-screening decision.

### Synthetic calculation and guided interpretation

For this lesson use the **Planar dissolved-oxygen diffusion ceiling** formula card, with the input variable **Diffusion-layer thickness** measured in µm. Its declared computational expression is `4*96485.33212*2e-9*0.25/(delta*1e-6)/10`. At an illustrative input of 101 µm, the output is 0.191060064 mA/cm²; at 300 µm, it is 0.0643235547 mA/cm². The two-point secant sensitivity is -0.00063686688 mA/cm² per µm. Interpret the sign and magnitude and then compute a third point without the website to check the calculation. A larger output is not necessarily higher corrosion risk: the meaning of the output depends on whether it is an equilibrium potential, a transport flux, an interfacial response, a thickness margin or an inspection-detection probability.

**Model domain for Uniform corrosion, metal loss and thickness mapping:** Four-electron oxygen reduction, dissolved oxygen 0.25 mol/m³, D=2×10⁻⁹ m²/s, planar stagnant film; faradaic ceiling only. Calculate independently before generalizing. Any service claim requires evidence that the model assumptions remain valid under the intended operating conditions.

### Investigation: evidence quality, sampling and controls

For **Uniform corrosion, metal loss and thickness mapping**, document **geometric maps of pits, crevices and cracks**, with **maximum depth distribution, position relative to fasteners, stresses, deposit chemistry and exposure time**. Challenge the primary conclusion using **matched unaffected cross-sections and isolation controls**. Keep independently sampled specimens distinct from repeat readings on the same material, and match environmental histories across treatment groups.

### Diagnostic warning and alternative outcome

Extrapolating short-duration uniform rates to all future environments ignores process changes and local hazards.

### Assessment: three substantive exercises

**Exercise 1 — mechanism and dimensional reasoning.** Derive or explain the relation `For ideal constant uniform loss, remaining thickness t(t_year) = t₀ − v t_year.` using its physical assumptions. Assign units to the terms that are actually quantitative; for a qualitative relation, replace it with a measurable definition. Distinguish what can be calculated from a textbook constant from what would require a service-specific measurement. *Answer guidance:* every conversion must declare the material, reacting species, coordinate or control volume and environmental state; reject interpretations whose quantities are at incompatible scales.

**Exercise 2 — independent numerical verification.** Recalculate the synthetic pair (101, 0.19106006) and (300, 0.064323555) with proper units, then choose a small change near the first point and estimate sensitivity. Discuss how input uncertainty and a violation of **planar dissolved-oxygen diffusion ceiling** assumptions would affect a claimed engineering conclusion. *Answer guidance:* calculate from the declared ideal expression, preserve units, and do not convert a formula-generated result into fictional laboratory evidence.

**Exercise 3 — disconfirming experiment.** For the case “A storage tank shows 0.08 mm per year average coupon loss and one isolated thin spot. Decide which result should govern a risk-screening decision.” specify a target measurement, a matched control, at least three distinct physical specimens when meaningful, an uncertainty source and a criterion that would reject the proposed cause. *Answer guidance:* distinguish damage depth from area-averaged loss, distinguish reaction-driving force from rate, and make sure the independent test is not based on the same unverified assumption.

### Decision exercise and transferable principle

Repeat co-registered thickness surveys with defensible spatial resolution and correlate anomalies to flow and deposits. Write a short decision memo: what is observed; what is inferred; what has not been measured; what alternative still fits; and which further evidence would justify action. Do not mistake a source with scientific-looking units for a calibrated material result. The goal is not to name as many corrosion forms as possible, but to explain precisely how a physical mechanism could produce the observed failure and how another mechanism could be ruled out.

## Lesson 3.2 — Pitting initiation, repassivation and metastable events

### Physical account: governing process and critical limits

Pit initiation often involves local breakdown of an otherwise protective surface, but not every transient event becomes a stable growing pit. Inclusion chemistry, chloride activity, potential and temperature can affect initiation and repassivation. Potentiodynamic scans may produce operational indicators such as breakdown and repassivation potentials, which depend on experimental conditions. A single scan is not a universal material fingerprint and cannot uniquely establish a long-term probability of perforation.

**Working relation.** Pit growth needs a charge and transport balance; nominal E_pit and E_rep are protocol-dependent observables.

### A concrete case: competing mechanisms

A stainless fitting shows scattered current spikes and sparse shallow pits after exposure. Determine which evidence could establish stable pit propagation.

### Synthetic calculation and guided interpretation

For this lesson use the **Localized pit depth from specified factor** formula card, with the input variable **Pit depth factor** measured in dimensionless. Its declared computational expression is `0.15*pf`. At an illustrative input of 4.895 dimensionless, the output is 0.73425 mm; at 12.685 dimensionless, it is 1.90275 mm. The two-point secant sensitivity is 0.15 mm per dimensionless. Interpret the sign and magnitude and then compute a third point without the website to check the calculation. A larger output is not necessarily higher corrosion risk: the meaning of the output depends on whether it is an equilibrium potential, a transport flux, an interfacial response, a thickness margin or an inspection-detection probability.

**Model domain for Pitting initiation, repassivation and metastable events:** Synthetic assumed 0.15 mm average nominal loss and a chosen pit-depth factor; does NOT predict the factor from alloy or chloride. Calculate independently before generalizing. Any service claim requires evidence that the model assumptions remain valid under the intended operating conditions.

### Investigation: evidence quality, sampling and controls

For **Pitting initiation, repassivation and metastable events**, document **geometric maps of pits, crevices and cracks**, with **maximum depth distribution, position relative to fasteners, stresses, deposit chemistry and exposure time**. Challenge the primary conclusion using **matched unaffected cross-sections and isolation controls**. Keep independently sampled specimens distinct from repeat readings on the same material, and match environmental histories across treatment groups.

### Diagnostic warning and alternative outcome

Equating transient current spikes to one-to-one permanent pits overstates signal specificity.

### Assessment: three substantive exercises

**Exercise 1 — mechanism and dimensional reasoning.** Derive or explain the relation `Pit growth needs a charge and transport balance; nominal E_pit and E_rep are protocol-dependent observables.` using its physical assumptions. Assign units to the terms that are actually quantitative; for a qualitative relation, replace it with a measurable definition. Distinguish what can be calculated from a textbook constant from what would require a service-specific measurement. *Answer guidance:* every conversion must declare the material, reacting species, coordinate or control volume and environmental state; reject interpretations whose quantities are at incompatible scales.

**Exercise 2 — independent numerical verification.** Recalculate the synthetic pair (4.895, 0.73425) and (12.685, 1.90275) with proper units, then choose a small change near the first point and estimate sensitivity. Discuss how input uncertainty and a violation of **localized pit depth from specified factor** assumptions would affect a claimed engineering conclusion. *Answer guidance:* calculate from the declared ideal expression, preserve units, and do not convert a formula-generated result into fictional laboratory evidence.

**Exercise 3 — disconfirming experiment.** For the case “A stainless fitting shows scattered current spikes and sparse shallow pits after exposure. Determine which evidence could establish stable pit propagation.” specify a target measurement, a matched control, at least three distinct physical specimens when meaningful, an uncertainty source and a criterion that would reject the proposed cause. *Answer guidance:* distinguish damage depth from area-averaged loss, distinguish reaction-driving force from rate, and make sure the independent test is not based on the same unverified assumption.

### Decision exercise and transferable principle

Compare time-resolved current with post-test microscopy and the distributions of maximum pit depths. Write a short decision memo: what is observed; what is inferred; what has not been measured; what alternative still fits; and which further evidence would justify action. Do not mistake a source with scientific-looking units for a calibrated material result. The goal is not to name as many corrosion forms as possible, but to explain precisely how a physical mechanism could produce the observed failure and how another mechanism could be ruled out.

<!-- MODEL_4 -->

## Lesson 3.3 — Crevice chemistry and differential aeration

### Physical account: governing process and critical limits

A narrow crevice can restrict replenishment, alter dissolved oxygen, and enable ionic concentration and hydrolysis feedback once metal dissolution begins. The bulk solution can remain relatively benign while local crevice chemistry becomes aggressive. Gap geometry, gasket compression, deposits, temperature and alloy chemistry control susceptibility. An oxygen-concentration cell alone is often too simple to describe subsequent acidification and chloride enrichment.

**Working relation.** Local electroneutrality and diffusion–migration balance determine crevice ion profiles; no single universal gap threshold exists.

### A concrete case: competing mechanisms

A bolted stainless joint corrodes under a washer rather than on the freely exposed flange. Propose a mechanism that predicts the spatial pattern.

### Synthetic calculation and guided interpretation

For this lesson use the **Planar dissolved-oxygen diffusion ceiling** formula card, with the input variable **Diffusion-layer thickness** measured in µm. Its declared computational expression is `4*96485.33212*2e-9*0.25/(delta*1e-6)/10`. At an illustrative input of 144 µm, the output is 0.134007406 mA/cm²; at 334 µm, it is 0.057775648 mA/cm². The two-point secant sensitivity is -0.00040121978 mA/cm² per µm. Interpret the sign and magnitude and then compute a third point without the website to check the calculation. A larger output is not necessarily higher corrosion risk: the meaning of the output depends on whether it is an equilibrium potential, a transport flux, an interfacial response, a thickness margin or an inspection-detection probability.

**Model domain for Crevice chemistry and differential aeration:** Four-electron oxygen reduction, dissolved oxygen 0.25 mol/m³, D=2×10⁻⁹ m²/s, planar stagnant film; faradaic ceiling only. Calculate independently before generalizing. Any service claim requires evidence that the model assumptions remain valid under the intended operating conditions.

### Investigation: evidence quality, sampling and controls

For **Crevice chemistry and differential aeration**, document **geometric maps of pits, crevices and cracks**, with **maximum depth distribution, position relative to fasteners, stresses, deposit chemistry and exposure time**. Challenge the primary conclusion using **matched unaffected cross-sections and isolation controls**. Keep independently sampled specimens distinct from repeat readings on the same material, and match environmental histories across treatment groups.

### Diagnostic warning and alternative outcome

Applying a published critical crevice width without matching surface finish, electrolyte and seal geometry is unreliable.

### Assessment: three substantive exercises

**Exercise 1 — mechanism and dimensional reasoning.** Derive or explain the relation `Local electroneutrality and diffusion–migration balance determine crevice ion profiles; no single universal gap threshold exists.` using its physical assumptions. Assign units to the terms that are actually quantitative; for a qualitative relation, replace it with a measurable definition. Distinguish what can be calculated from a textbook constant from what would require a service-specific measurement. *Answer guidance:* every conversion must declare the material, reacting species, coordinate or control volume and environmental state; reject interpretations whose quantities are at incompatible scales.

**Exercise 2 — independent numerical verification.** Recalculate the synthetic pair (144, 0.13400741) and (334, 0.057775648) with proper units, then choose a small change near the first point and estimate sensitivity. Discuss how input uncertainty and a violation of **planar dissolved-oxygen diffusion ceiling** assumptions would affect a claimed engineering conclusion. *Answer guidance:* calculate from the declared ideal expression, preserve units, and do not convert a formula-generated result into fictional laboratory evidence.

**Exercise 3 — disconfirming experiment.** For the case “A bolted stainless joint corrodes under a washer rather than on the freely exposed flange. Propose a mechanism that predicts the spatial pattern.” specify a target measurement, a matched control, at least three distinct physical specimens when meaningful, an uncertainty source and a criterion that would reject the proposed cause. *Answer guidance:* distinguish damage depth from area-averaged loss, distinguish reaction-driving force from rate, and make sure the independent test is not based on the same unverified assumption.

### Decision exercise and transferable principle

Compare gaskets and crevice-former geometries under the same solution history, including cross-sections and local deposits. Write a short decision memo: what is observed; what is inferred; what has not been measured; what alternative still fits; and which further evidence would justify action. Do not mistake a source with scientific-looking units for a calibrated material result. The goal is not to name as many corrosion forms as possible, but to explain precisely how a physical mechanism could produce the observed failure and how another mechanism could be ruled out.

## Lesson 3.4 — Galvanic localization and deposits

### Physical account: governing process and critical limits

Galvanic coupling can amplify local anodic dissolution, but the affected region depends on electrolyte path resistance and the relative kinetics of exposed surfaces. A corrosion deposit may also create differential chemistry without any dissimilar-metal contact. Distance matters in conductive environments and near small contacts, while large-area design dimensions control current distribution. A clean laboratory couple and a fouled service interface are not necessarily the same system.

**Working relation.** At steady state, integrated anodic and cathodic faradaic currents balance; current density varies spatially.

### A concrete case: competing mechanisms

Attack concentrates around a brass insert in a steel manifold, yet an electrically isolated replica still corrodes beneath deposits. Diagnose multiple mechanisms.

### Synthetic calculation and guided interpretation

For this lesson use the **Localized pit depth from specified factor** formula card, with the input variable **Pit depth factor** measured in dimensionless. Its declared computational expression is `0.15*pf`. At an illustrative input of 6.605 dimensionless, the output is 0.99075 mm; at 14.015 dimensionless, it is 2.10225 mm. The two-point secant sensitivity is 0.15 mm per dimensionless. Interpret the sign and magnitude and then compute a third point without the website to check the calculation. A larger output is not necessarily higher corrosion risk: the meaning of the output depends on whether it is an equilibrium potential, a transport flux, an interfacial response, a thickness margin or an inspection-detection probability.

**Model domain for Galvanic localization and deposits:** Synthetic assumed 0.15 mm average nominal loss and a chosen pit-depth factor; does NOT predict the factor from alloy or chloride. Calculate independently before generalizing. Any service claim requires evidence that the model assumptions remain valid under the intended operating conditions.

### Investigation: evidence quality, sampling and controls

For **Galvanic localization and deposits**, document **geometric maps of pits, crevices and cracks**, with **maximum depth distribution, position relative to fasteners, stresses, deposit chemistry and exposure time**. Challenge the primary conclusion using **matched unaffected cross-sections and isolation controls**. Keep independently sampled specimens distinct from repeat readings on the same material, and match environmental histories across treatment groups.

### Diagnostic warning and alternative outcome

Calling all attack near an attachment galvanic can conceal stagnant crevice and wet–dry cycling causes.

### Assessment: three substantive exercises

**Exercise 1 — mechanism and dimensional reasoning.** Derive or explain the relation `At steady state, integrated anodic and cathodic faradaic currents balance; current density varies spatially.` using its physical assumptions. Assign units to the terms that are actually quantitative; for a qualitative relation, replace it with a measurable definition. Distinguish what can be calculated from a textbook constant from what would require a service-specific measurement. *Answer guidance:* every conversion must declare the material, reacting species, coordinate or control volume and environmental state; reject interpretations whose quantities are at incompatible scales.

**Exercise 2 — independent numerical verification.** Recalculate the synthetic pair (6.605, 0.99075) and (14.015, 2.10225) with proper units, then choose a small change near the first point and estimate sensitivity. Discuss how input uncertainty and a violation of **localized pit depth from specified factor** assumptions would affect a claimed engineering conclusion. *Answer guidance:* calculate from the declared ideal expression, preserve units, and do not convert a formula-generated result into fictional laboratory evidence.

**Exercise 3 — disconfirming experiment.** For the case “Attack concentrates around a brass insert in a steel manifold, yet an electrically isolated replica still corrodes beneath deposits. Diagnose multiple mechanisms.” specify a target measurement, a matched control, at least three distinct physical specimens when meaningful, an uncertainty source and a criterion that would reject the proposed cause. *Answer guidance:* distinguish damage depth from area-averaged loss, distinguish reaction-driving force from rate, and make sure the independent test is not based on the same unverified assumption.

### Decision exercise and transferable principle

Test electrical continuity, isolate the metals, and photograph damage relative to deposits and flow. Write a short decision memo: what is observed; what is inferred; what has not been measured; what alternative still fits; and which further evidence would justify action. Do not mistake a source with scientific-looking units for a calibrated material result. The goal is not to name as many corrosion forms as possible, but to explain precisely how a physical mechanism could produce the observed failure and how another mechanism could be ruled out.

<!-- MODEL_5 -->

## Lesson 3.5 — Stress-corrosion cracking, corrosion fatigue and hydrogen

### Physical account: governing process and critical limits

Environmentally assisted cracks require consideration of stress, material susceptibility and environment acting together. Stress-corrosion cracking can initiate at stresses below monotonic yield in susceptible systems; corrosion fatigue involves cyclic loading and environmentally modified crack growth; hydrogen-assisted damage may alter ductility or cracking pathways depending on alloy and charging history. Surface appearance alone seldom identifies the responsible mechanism. Fractography, load history and metallurgical records are critical.

**Working relation.** Fatigue growth may be summarized phenomenologically as da/dN=C(ΔK)^m only within validated regimes.

### A concrete case: competing mechanisms

A high-strength bolt fractures suddenly after months of service without striking uniform rust. Develop a fracture-mechanism investigation without guessing from color.

### Synthetic calculation and guided interpretation

For this lesson use the **Planar dissolved-oxygen diffusion ceiling** formula card, with the input variable **Diffusion-layer thickness** measured in µm. Its declared computational expression is `4*96485.33212*2e-9*0.25/(delta*1e-6)/10`. At an illustrative input of 186 µm, the output is 0.103747669 mA/cm²; at 367 µm, it is 0.0525805625 mA/cm². The two-point secant sensitivity is -0.0002826912 mA/cm² per µm. Interpret the sign and magnitude and then compute a third point without the website to check the calculation. A larger output is not necessarily higher corrosion risk: the meaning of the output depends on whether it is an equilibrium potential, a transport flux, an interfacial response, a thickness margin or an inspection-detection probability.

**Model domain for Stress-corrosion cracking, corrosion fatigue and hydrogen:** Four-electron oxygen reduction, dissolved oxygen 0.25 mol/m³, D=2×10⁻⁹ m²/s, planar stagnant film; faradaic ceiling only. Calculate independently before generalizing. Any service claim requires evidence that the model assumptions remain valid under the intended operating conditions.

### Investigation: evidence quality, sampling and controls

For **Stress-corrosion cracking, corrosion fatigue and hydrogen**, document **geometric maps of pits, crevices and cracks**, with **maximum depth distribution, position relative to fasteners, stresses, deposit chemistry and exposure time**. Challenge the primary conclusion using **matched unaffected cross-sections and isolation controls**. Keep independently sampled specimens distinct from repeat readings on the same material, and match environmental histories across treatment groups.

### Diagnostic warning and alternative outcome

Assuming every delayed fracture is caused by hydrogen can overlook overload, notches and manufacturing defects.

### Assessment: three substantive exercises

**Exercise 1 — mechanism and dimensional reasoning.** Derive or explain the relation `Fatigue growth may be summarized phenomenologically as da/dN=C(ΔK)^m only within validated regimes.` using its physical assumptions. Assign units to the terms that are actually quantitative; for a qualitative relation, replace it with a measurable definition. Distinguish what can be calculated from a textbook constant from what would require a service-specific measurement. *Answer guidance:* every conversion must declare the material, reacting species, coordinate or control volume and environmental state; reject interpretations whose quantities are at incompatible scales.

**Exercise 2 — independent numerical verification.** Recalculate the synthetic pair (186, 0.10374767) and (367, 0.052580562) with proper units, then choose a small change near the first point and estimate sensitivity. Discuss how input uncertainty and a violation of **planar dissolved-oxygen diffusion ceiling** assumptions would affect a claimed engineering conclusion. *Answer guidance:* calculate from the declared ideal expression, preserve units, and do not convert a formula-generated result into fictional laboratory evidence.

**Exercise 3 — disconfirming experiment.** For the case “A high-strength bolt fractures suddenly after months of service without striking uniform rust. Develop a fracture-mechanism investigation without guessing from color.” specify a target measurement, a matched control, at least three distinct physical specimens when meaningful, an uncertainty source and a criterion that would reject the proposed cause. *Answer guidance:* distinguish damage depth from area-averaged loss, distinguish reaction-driving force from rate, and make sure the independent test is not based on the same unverified assumption.

### Decision exercise and transferable principle

Combine fracture morphology, hardness, residual stress, exposure data and mechanical testing of unaffected controls. Write a short decision memo: what is observed; what is inferred; what has not been measured; what alternative still fits; and which further evidence would justify action. Do not mistake a source with scientific-looking units for a calibrated material result. The goal is not to name as many corrosion forms as possible, but to explain precisely how a physical mechanism could produce the observed failure and how another mechanism could be ruled out.

## Unit 3 capstone — evidence and engineering defense

**Complex case:** A chloride-exposed stainless-steel heat-exchanger plate develops isolated pits and leakage. Build competing explanations for initiation, propagation, and leakage.

1. **System definition for Localized corrosion and coupled failure:** Sketch the material, phase boundaries, electrolyte or gas paths, stressed features, wet–dry or thermal cycles and measurement locations. State precisely whether the main concern is uniform thinning, maximum pit depth, a crack, surface-electrical function or loss of protective scale.
2. **Two competing mechanisms:** Construct a table with initiating cause, expected spatial pattern, predicted time dependence, contrary evidence and an orthogonal method. Identify which mechanism might operate after rather than before the observed damage.
3. **Numerical audit:** Recalculate both of this unit's models at their default inputs and at the limits of the slider range. Describe the units and whether the model concerns driving force, rate, geometry, or inspection uncertainty. Show at least one reason the model might not apply to the given case.
4. **Sampling and uncertainty:** Build a hierarchy of independent assets or coupons, repeated measurements and local map points. Include instrument calibration, specimen differences, exposure mismatch and the possibility that a rare maximum is missed by ordinary sampling.
5. **Decision note:** Produce a 400-word recommendation with immediate safety implications separated from follow-up research, a repair or monitor option, a cost of wrong inference, and the exact evidence that would change the ranking. Do not claim service life from synthetic data.

### Connecting this unit to materials engineering

A corrosion investigation improves when it preserves the distinction between an electrochemical mechanism, the spatial manifestation of damage, an instrument response and a decision on whether equipment remains fit for service. In **localized corrosion and coupled failure**, a defensible conclusion follows a chain of falsifiable physical claims rather than a single parameter selected because it is easy to compute. The mathematics should expose sensitivity and uncertainty, while site observations determine whether the equations apply at all. The companion models are an instructional starting point; professional asset decisions need controlled tests, standards and real-world verification.
