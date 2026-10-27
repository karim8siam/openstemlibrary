# Unit 1: Electrochemical thermodynamics and corrosion cells

**Guiding question:** Which thermodynamic forces enable corrosion and what can potentials establish without claiming a rate?

## System view and mechanism boundaries

A mixed-metal water-handling assembly fails soon after a new fitting is introduced. Determine whether the available evidence supports galvanic interaction, deposit-related aeration, or an unrelated design fault. The investigation begins with a defined material and state, a particular environment and the time-dependent physical response. Distinguish metal-dissolution, oxide formation, product transport and structural weakening rather than compressing all visible changes into one category. Separate a possible reaction from a verified rate and a local failure mode from an area-averaged measurement. For this unit, a useful answer must identify an observable that would falsify a favored account and an independent observation that constrains the competing mechanism. Neither ideal electrochemical equations nor visual inspection alone resolves all ambiguities.

## Case for comparative investigation

A mixed-metal water-handling assembly fails soon after a new fitting is introduced. Determine whether the available evidence supports galvanic interaction, deposit-related aeration, or an unrelated design fault. Draw a decision tree with a first measurement, one targeted control and one observation that would reject the initial theory. Explain why an attractive laboratory result can be irrelevant if the critical field failure occurs on a different length scale or in a different environmental regime. State the uncertainty that a qualified engineer would need to resolve before authorizing a mitigation or reuse decision.

## Lesson 1.1 — Chemical potential, Gibbs energy and corrosion driving force

### Physical account: governing process and critical limits

For a reaction at fixed temperature and pressure the change in Gibbs free energy determines the direction of spontaneous reaction, not its speed. Electrons exchange chemical work with an external circuit, allowing the useful relation ΔG = −nFE for a specified overall electrochemical reaction. Formation of a corrosion product can be thermodynamically favored while a passive film causes a very low observed rate. Reference potentials are attached to defined half-reactions and activities; they are not material constants independent of the environment.

**Working relation.** ΔG = −n F E_cell; F ≈ 96485 C mol⁻¹; use activities and a declared electrode reference.

### A concrete case: competing mechanisms

A zinc-coated steel guardrail becomes scratched. Compare whether zinc loss and exposed iron loss are both thermodynamically allowed in rainwater, and explain why a voltage alone cannot report penetration depth.

### Synthetic calculation and guided interpretation

For this lesson use the **Iron Faraday uniform penetration** formula card, with the input variable **Dissolution current density** measured in µA/cm². Its declared computational expression is `i*0.01*0.055845/(2*96485.33212*7850)*31557600000`. At an illustrative input of 4.884 µA/cm², the output is 0.0568202276 mm/year; at 17.442 µA/cm², it is 0.202919412 mm/year. The two-point secant sensitivity is 0.011633953 mm/year per µA/cm². Interpret the sign and magnitude and then compute a third point without the website to check the calculation. A larger output is not necessarily higher corrosion risk: the meaning of the output depends on whether it is an equilibrium potential, a transport flux, an interfacial response, a thickness margin or an inspection-detection probability.

**Model domain for Chemical potential, Gibbs energy and corrosion driving force:** Pure Fe, Fe→Fe²⁺, density 7850 kg/m³, 100% dissolution efficiency and perfectly uniform attack; not a pit-depth forecast. Calculate independently before generalizing. Any service claim requires evidence that the model assumptions remain valid under the intended operating conditions.

### Investigation: evidence quality, sampling and controls

For **Chemical potential, Gibbs energy and corrosion driving force**, document **paired electrochemical and compositional maps**, with **reference-electrode type, specimen chemistry, solution composition, temperature and wetting history**. Challenge the primary conclusion using **surface chemistry, local damage and coupled-current monitoring**. Keep independently sampled specimens distinct from repeat readings on the same material, and match environmental histories across treatment groups.

### Diagnostic warning and alternative outcome

Using an equilibrium-potential table as a universal corrosion-rate ranking ignores kinetic polarization, films and chemical speciation.

### Assessment: three substantive exercises

**Exercise 1 — mechanism and dimensional reasoning.** Derive or explain the relation `ΔG = −n F E_cell; F ≈ 96485 C mol⁻¹; use activities and a declared electrode reference.` using its physical assumptions. Assign units to the terms that are actually quantitative; for a qualitative relation, replace it with a measurable definition. Distinguish what can be calculated from a textbook constant from what would require a service-specific measurement. *Answer guidance:* every conversion must declare the material, reacting species, coordinate or control volume and environmental state; reject interpretations whose quantities are at incompatible scales.

**Exercise 2 — independent numerical verification.** Recalculate the synthetic pair (4.884, 0.056820228) and (17.442, 0.20291941) with proper units, then choose a small change near the first point and estimate sensitivity. Discuss how input uncertainty and a violation of **iron faraday uniform penetration** assumptions would affect a claimed engineering conclusion. *Answer guidance:* calculate from the declared ideal expression, preserve units, and do not convert a formula-generated result into fictional laboratory evidence.

**Exercise 3 — disconfirming experiment.** For the case “A zinc-coated steel guardrail becomes scratched. Compare whether zinc loss and exposed iron loss are both thermodynamically allowed in rainwater, and explain why a voltage alone cannot report penetration depth.” specify a target measurement, a matched control, at least three distinct physical specimens when meaningful, an uncertainty source and a criterion that would reject the proposed cause. *Answer guidance:* distinguish damage depth from area-averaged loss, distinguish reaction-driving force from rate, and make sure the independent test is not based on the same unverified assumption.

### Decision exercise and transferable principle

Compare measured potential with coupled current and a surface map before concluding the observed metal loss is galvanic. Write a short decision memo: what is observed; what is inferred; what has not been measured; what alternative still fits; and which further evidence would justify action. Do not mistake a source with scientific-looking units for a calibrated material result. The goal is not to name as many corrosion forms as possible, but to explain precisely how a physical mechanism could produce the observed failure and how another mechanism could be ruled out.

## Lesson 1.2 — Anodic dissolution and cathodic reduction half-reactions

### Physical account: governing process and critical limits

Corrosion of metal entails oxidation at anodic regions and balancing reduction reactions elsewhere. In aerated neutral water oxygen reduction is often important; in acid media hydrogen evolution may contribute, subject to kinetics. Electron current flows through a conducting metallic path and ionic current through the electrolyte. Both reactions can occur on a nominally uniform alloy surface at different microscopic sites. Rust is a product family, not a stoichiometric single-phase certificate.

**Working relation.** Anodic: M → Mᶻ⁺ + z e⁻; cathodic example: O₂ + 2H₂O + 4e⁻ → 4OH⁻.

### A concrete case: competing mechanisms

An iron pipe corrodes near a deposit while nearby clean metal remains comparatively intact. Draw anodic and cathodic locations and describe how oxygen access may change the local balance.

### Synthetic calculation and guided interpretation

For this lesson use the **Nernst iron-ion potential vs SHE** formula card, with the input variable **Fe²⁺ activity** measured in dimensionless. Its declared computational expression is `-0.44+(8.314462618*298.15/(2*96485.33212))*Math.log(a)`. At an illustrative input of 0.2050795 dimensionless, the output is -0.460353116 V vs SHE; at 0.6150385 dimensionless, it is -0.446244201 V vs SHE. The two-point secant sensitivity is 0.034415429 V vs SHE per dimensionless. Interpret the sign and magnitude and then compute a third point without the website to check the calculation. A larger output is not necessarily higher corrosion risk: the meaning of the output depends on whether it is an equilibrium potential, a transport flux, an interfacial response, a thickness margin or an inspection-detection probability.

**Model domain for Anodic dissolution and cathodic reduction half-reactions:** Ideal Fe²⁺/Fe equilibrium at 298.15 K; illustrative E°=-0.44 V vs SHE, no complexation or junction potential. Calculate independently before generalizing. Any service claim requires evidence that the model assumptions remain valid under the intended operating conditions.

### Investigation: evidence quality, sampling and controls

For **Anodic dissolution and cathodic reduction half-reactions**, document **paired electrochemical and compositional maps**, with **reference-electrode type, specimen chemistry, solution composition, temperature and wetting history**. Challenge the primary conclusion using **surface chemistry, local damage and coupled-current monitoring**. Keep independently sampled specimens distinct from repeat readings on the same material, and match environmental histories across treatment groups.

### Diagnostic warning and alternative outcome

An apparent absence of visible hydrogen does not eliminate cathodic reactions or charge conservation.

### Assessment: three substantive exercises

**Exercise 1 — mechanism and dimensional reasoning.** Derive or explain the relation `Anodic: M → Mᶻ⁺ + z e⁻; cathodic example: O₂ + 2H₂O + 4e⁻ → 4OH⁻.` using its physical assumptions. Assign units to the terms that are actually quantitative; for a qualitative relation, replace it with a measurable definition. Distinguish what can be calculated from a textbook constant from what would require a service-specific measurement. *Answer guidance:* every conversion must declare the material, reacting species, coordinate or control volume and environmental state; reject interpretations whose quantities are at incompatible scales.

**Exercise 2 — independent numerical verification.** Recalculate the synthetic pair (0.2050795, -0.46035312) and (0.6150385, -0.4462442) with proper units, then choose a small change near the first point and estimate sensitivity. Discuss how input uncertainty and a violation of **nernst iron-ion potential vs she** assumptions would affect a claimed engineering conclusion. *Answer guidance:* calculate from the declared ideal expression, preserve units, and do not convert a formula-generated result into fictional laboratory evidence.

**Exercise 3 — disconfirming experiment.** For the case “An iron pipe corrodes near a deposit while nearby clean metal remains comparatively intact. Draw anodic and cathodic locations and describe how oxygen access may change the local balance.” specify a target measurement, a matched control, at least three distinct physical specimens when meaningful, an uncertainty source and a criterion that would reject the proposed cause. *Answer guidance:* distinguish damage depth from area-averaged loss, distinguish reaction-driving force from rate, and make sure the independent test is not based on the same unverified assumption.

### Decision exercise and transferable principle

Record local chemistry, deposits and potential mapping; test whether an oxygen-transport explanation predicts the attack location. Write a short decision memo: what is observed; what is inferred; what has not been measured; what alternative still fits; and which further evidence would justify action. Do not mistake a source with scientific-looking units for a calibrated material result. The goal is not to name as many corrosion forms as possible, but to explain precisely how a physical mechanism could produce the observed failure and how another mechanism could be ruled out.

<!-- MODEL_0 -->

## Lesson 1.3 — Nernst equation and the role of activities

### Physical account: governing process and critical limits

Electrode equilibrium potential depends on temperature and the reaction quotient through the Nernst equation. The frequently quoted 59 mV per decade factor is specific to a one-electron process at about 298 K; the factor scales inversely with electron count. Concentrations may approximate activities only for appropriately dilute solutions, and redox reactions can involve proton activity or dissolved gas pressure. A voltmeter records a difference from a reference electrode with its own temperature and junction effects.

**Working relation.** E = E° − (RT/nF) ln Q, for the reaction and sign convention as written.

### A concrete case: competing mechanisms

A copper-ion half-cell shows a changing potential after salt is introduced. Distinguish genuine activity changes from altered liquid-junction potential and instrument drift.

### Synthetic calculation and guided interpretation

For this lesson use the **Iron Faraday uniform penetration** formula card, with the input variable **Dissolution current density** measured in µA/cm². Its declared computational expression is `i*0.01*0.055845/(2*96485.33212*7850)*31557600000`. At an illustrative input of 7.575 µA/cm², the output is 0.0881271958 mm/year; at 19.535 µA/cm², it is 0.227269277 mm/year. The two-point secant sensitivity is 0.011633953 mm/year per µA/cm². Interpret the sign and magnitude and then compute a third point without the website to check the calculation. A larger output is not necessarily higher corrosion risk: the meaning of the output depends on whether it is an equilibrium potential, a transport flux, an interfacial response, a thickness margin or an inspection-detection probability.

**Model domain for Nernst equation and the role of activities:** Pure Fe, Fe→Fe²⁺, density 7850 kg/m³, 100% dissolution efficiency and perfectly uniform attack; not a pit-depth forecast. Calculate independently before generalizing. Any service claim requires evidence that the model assumptions remain valid under the intended operating conditions.

### Investigation: evidence quality, sampling and controls

For **Nernst equation and the role of activities**, document **paired electrochemical and compositional maps**, with **reference-electrode type, specimen chemistry, solution composition, temperature and wetting history**. Challenge the primary conclusion using **surface chemistry, local damage and coupled-current monitoring**. Keep independently sampled specimens distinct from repeat readings on the same material, and match environmental histories across treatment groups.

### Diagnostic warning and alternative outcome

Inserting molarity into an activity expression without checking solution nonideality can shift expected potentials.

### Assessment: three substantive exercises

**Exercise 1 — mechanism and dimensional reasoning.** Derive or explain the relation `E = E° − (RT/nF) ln Q, for the reaction and sign convention as written.` using its physical assumptions. Assign units to the terms that are actually quantitative; for a qualitative relation, replace it with a measurable definition. Distinguish what can be calculated from a textbook constant from what would require a service-specific measurement. *Answer guidance:* every conversion must declare the material, reacting species, coordinate or control volume and environmental state; reject interpretations whose quantities are at incompatible scales.

**Exercise 2 — independent numerical verification.** Recalculate the synthetic pair (7.575, 0.088127196) and (19.535, 0.22726928) with proper units, then choose a small change near the first point and estimate sensitivity. Discuss how input uncertainty and a violation of **iron faraday uniform penetration** assumptions would affect a claimed engineering conclusion. *Answer guidance:* calculate from the declared ideal expression, preserve units, and do not convert a formula-generated result into fictional laboratory evidence.

**Exercise 3 — disconfirming experiment.** For the case “A copper-ion half-cell shows a changing potential after salt is introduced. Distinguish genuine activity changes from altered liquid-junction potential and instrument drift.” specify a target measurement, a matched control, at least three distinct physical specimens when meaningful, an uncertainty source and a criterion that would reject the proposed cause. *Answer guidance:* distinguish damage depth from area-averaged loss, distinguish reaction-driving force from rate, and make sure the independent test is not based on the same unverified assumption.

### Decision exercise and transferable principle

Change ionic strength under controlled conditions while measuring a stable reference and independently characterizing ionic composition. Write a short decision memo: what is observed; what is inferred; what has not been measured; what alternative still fits; and which further evidence would justify action. Do not mistake a source with scientific-looking units for a calibrated material result. The goal is not to name as many corrosion forms as possible, but to explain precisely how a physical mechanism could produce the observed failure and how another mechanism could be ruled out.

## Lesson 1.4 — Pourbaix diagrams and the limits of equilibrium maps

### Physical account: governing process and critical limits

An E–pH diagram places candidate stability domains for dissolved species, metal and solid phases under chosen activities at equilibrium. It can identify where a film may be thermodynamically possible but it does not report porosity, adhesion, film growth rate, metastable pitting, localized crevice chemistry or breakdown under cyclic stress. A line shifts if activities, temperature or reaction species change. Reading the diagram requires checking its reference electrode and the actual local rather than nominal bulk pH.

**Working relation.** For a redox boundary, E(pH) follows a Nernst relation; activity choices define the plotted line.

### A concrete case: competing mechanisms

An aluminum part appears in a passive domain on a simplified diagram but pits in chloride solution. Explain why the diagram is not logically contradicted.

### Synthetic calculation and guided interpretation

For this lesson use the **Nernst iron-ion potential vs SHE** formula card, with the input variable **Fe²⁺ activity** measured in dimensionless. Its declared computational expression is `-0.44+(8.314462618*298.15/(2*96485.33212))*Math.log(a)`. At an illustrative input of 0.2950705 dimensionless, the output is -0.455679423 V vs SHE; at 0.6850315 dimensionless, it is -0.444859629 V vs SHE. The two-point secant sensitivity is 0.027745836 V vs SHE per dimensionless. Interpret the sign and magnitude and then compute a third point without the website to check the calculation. A larger output is not necessarily higher corrosion risk: the meaning of the output depends on whether it is an equilibrium potential, a transport flux, an interfacial response, a thickness margin or an inspection-detection probability.

**Model domain for Pourbaix diagrams and the limits of equilibrium maps:** Ideal Fe²⁺/Fe equilibrium at 298.15 K; illustrative E°=-0.44 V vs SHE, no complexation or junction potential. Calculate independently before generalizing. Any service claim requires evidence that the model assumptions remain valid under the intended operating conditions.

### Investigation: evidence quality, sampling and controls

For **Pourbaix diagrams and the limits of equilibrium maps**, document **paired electrochemical and compositional maps**, with **reference-electrode type, specimen chemistry, solution composition, temperature and wetting history**. Challenge the primary conclusion using **surface chemistry, local damage and coupled-current monitoring**. Keep independently sampled specimens distinct from repeat readings on the same material, and match environmental histories across treatment groups.

### Diagnostic warning and alternative outcome

Mistaking a diagram of equilibrium stability for a guarantee of corrosion immunity is a fundamental category error.

### Assessment: three substantive exercises

**Exercise 1 — mechanism and dimensional reasoning.** Derive or explain the relation `For a redox boundary, E(pH) follows a Nernst relation; activity choices define the plotted line.` using its physical assumptions. Assign units to the terms that are actually quantitative; for a qualitative relation, replace it with a measurable definition. Distinguish what can be calculated from a textbook constant from what would require a service-specific measurement. *Answer guidance:* every conversion must declare the material, reacting species, coordinate or control volume and environmental state; reject interpretations whose quantities are at incompatible scales.

**Exercise 2 — independent numerical verification.** Recalculate the synthetic pair (0.2950705, -0.45567942) and (0.6850315, -0.44485963) with proper units, then choose a small change near the first point and estimate sensitivity. Discuss how input uncertainty and a violation of **nernst iron-ion potential vs she** assumptions would affect a claimed engineering conclusion. *Answer guidance:* calculate from the declared ideal expression, preserve units, and do not convert a formula-generated result into fictional laboratory evidence.

**Exercise 3 — disconfirming experiment.** For the case “An aluminum part appears in a passive domain on a simplified diagram but pits in chloride solution. Explain why the diagram is not logically contradicted.” specify a target measurement, a matched control, at least three distinct physical specimens when meaningful, an uncertainty source and a criterion that would reject the proposed cause. *Answer guidance:* distinguish damage depth from area-averaged loss, distinguish reaction-driving force from rate, and make sure the independent test is not based on the same unverified assumption.

### Decision exercise and transferable principle

Combine potential and local pit-solution measurements with film characterization to test a proposed breakdown mechanism. Write a short decision memo: what is observed; what is inferred; what has not been measured; what alternative still fits; and which further evidence would justify action. Do not mistake a source with scientific-looking units for a calibrated material result. The goal is not to name as many corrosion forms as possible, but to explain precisely how a physical mechanism could produce the observed failure and how another mechanism could be ruled out.

<!-- MODEL_1 -->

## Lesson 1.5 — Galvanic couples, geometry and area ratio

### Physical account: governing process and critical limits

When dissimilar electrochemical surfaces are electrically connected through a shared electrolyte, the mixed potential of the assembly is determined by their current–potential behaviors and exposed areas. A large cathode paired with a small active anode can increase the anodic current density, but the effect also depends on polarization, electrolyte resistance and location. A galvanic series is meaningful only for the specified environmental conditions and surface states. Electrical isolation can interrupt the electronic path even when the materials remain wet.

**Working relation.** A_anode · i_anode + A_cathode · i_cathode = 0 at a steady open-circuit mixed potential.

### A concrete case: competing mechanisms

A small aluminum rivet joins an extensive stainless panel near seawater. Compare the local risk if the rivet and panel areas were reversed.

### Synthetic calculation and guided interpretation

For this lesson use the **Iron Faraday uniform penetration** formula card, with the input variable **Dissolution current density** measured in µA/cm². Its declared computational expression is `i*0.01*0.055845/(2*96485.33212*7850)*31557600000`. At an illustrative input of 10.266 µA/cm², the output is 0.119434164 mm/year; at 21.628 µA/cm², it is 0.251619141 mm/year. The two-point secant sensitivity is 0.011633953 mm/year per µA/cm². Interpret the sign and magnitude and then compute a third point without the website to check the calculation. A larger output is not necessarily higher corrosion risk: the meaning of the output depends on whether it is an equilibrium potential, a transport flux, an interfacial response, a thickness margin or an inspection-detection probability.

**Model domain for Galvanic couples, geometry and area ratio:** Pure Fe, Fe→Fe²⁺, density 7850 kg/m³, 100% dissolution efficiency and perfectly uniform attack; not a pit-depth forecast. Calculate independently before generalizing. Any service claim requires evidence that the model assumptions remain valid under the intended operating conditions.

### Investigation: evidence quality, sampling and controls

For **Galvanic couples, geometry and area ratio**, document **paired electrochemical and compositional maps**, with **reference-electrode type, specimen chemistry, solution composition, temperature and wetting history**. Challenge the primary conclusion using **surface chemistry, local damage and coupled-current monitoring**. Keep independently sampled specimens distinct from repeat readings on the same material, and match environmental histories across treatment groups.

### Diagnostic warning and alternative outcome

Predicting corrosion from standard-electrode potential difference alone ignores real polarization curves.

### Assessment: three substantive exercises

**Exercise 1 — mechanism and dimensional reasoning.** Derive or explain the relation `A_anode · i_anode + A_cathode · i_cathode = 0 at a steady open-circuit mixed potential.` using its physical assumptions. Assign units to the terms that are actually quantitative; for a qualitative relation, replace it with a measurable definition. Distinguish what can be calculated from a textbook constant from what would require a service-specific measurement. *Answer guidance:* every conversion must declare the material, reacting species, coordinate or control volume and environmental state; reject interpretations whose quantities are at incompatible scales.

**Exercise 2 — independent numerical verification.** Recalculate the synthetic pair (10.266, 0.11943416) and (21.628, 0.25161914) with proper units, then choose a small change near the first point and estimate sensitivity. Discuss how input uncertainty and a violation of **iron faraday uniform penetration** assumptions would affect a claimed engineering conclusion. *Answer guidance:* calculate from the declared ideal expression, preserve units, and do not convert a formula-generated result into fictional laboratory evidence.

**Exercise 3 — disconfirming experiment.** For the case “A small aluminum rivet joins an extensive stainless panel near seawater. Compare the local risk if the rivet and panel areas were reversed.” specify a target measurement, a matched control, at least three distinct physical specimens when meaningful, an uncertainty source and a criterion that would reject the proposed cause. *Answer guidance:* distinguish damage depth from area-averaged loss, distinguish reaction-driving force from rate, and make sure the independent test is not based on the same unverified assumption.

### Decision exercise and transferable principle

Use assembly-specific area measurements and a coupled-current monitor under representative wetting conditions. Write a short decision memo: what is observed; what is inferred; what has not been measured; what alternative still fits; and which further evidence would justify action. Do not mistake a source with scientific-looking units for a calibrated material result. The goal is not to name as many corrosion forms as possible, but to explain precisely how a physical mechanism could produce the observed failure and how another mechanism could be ruled out.

## Unit 1 capstone — evidence and engineering defense

**Complex case:** A mixed-metal water-handling assembly fails soon after a new fitting is introduced. Determine whether the available evidence supports galvanic interaction, deposit-related aeration, or an unrelated design fault.

1. **System definition for Electrochemical thermodynamics and corrosion cells:** Sketch the material, phase boundaries, electrolyte or gas paths, stressed features, wet–dry or thermal cycles and measurement locations. State precisely whether the main concern is uniform thinning, maximum pit depth, a crack, surface-electrical function or loss of protective scale.
2. **Two competing mechanisms:** Construct a table with initiating cause, expected spatial pattern, predicted time dependence, contrary evidence and an orthogonal method. Identify which mechanism might operate after rather than before the observed damage.
3. **Numerical audit:** Recalculate both of this unit's models at their default inputs and at the limits of the slider range. Describe the units and whether the model concerns driving force, rate, geometry, or inspection uncertainty. Show at least one reason the model might not apply to the given case.
4. **Sampling and uncertainty:** Build a hierarchy of independent assets or coupons, repeated measurements and local map points. Include instrument calibration, specimen differences, exposure mismatch and the possibility that a rare maximum is missed by ordinary sampling.
5. **Decision note:** Produce a 400-word recommendation with immediate safety implications separated from follow-up research, a repair or monitor option, a cost of wrong inference, and the exact evidence that would change the ranking. Do not claim service life from synthetic data.

### Connecting this unit to materials engineering

A corrosion investigation improves when it preserves the distinction between an electrochemical mechanism, the spatial manifestation of damage, an instrument response and a decision on whether equipment remains fit for service. In **electrochemical thermodynamics and corrosion cells**, a defensible conclusion follows a chain of falsifiable physical claims rather than a single parameter selected because it is easy to compute. The mathematics should expose sensitivity and uncertainty, while site observations determine whether the equations apply at all. The companion models are an instructional starting point; professional asset decisions need controlled tests, standards and real-world verification.
