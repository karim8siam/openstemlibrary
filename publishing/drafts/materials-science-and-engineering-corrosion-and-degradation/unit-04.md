# Unit 4: Passivation, alloy selection and microstructure

**Guiding question:** What creates a protective surface film and when can manufacturing history defeat it?

## System view and mechanism boundaries

A welded stainless-steel vessel exhibits attack near the weld rather than across its smooth parent plate. Separate chemistry, microstructure and service causes. The investigation begins with a defined material and state, a particular environment and the time-dependent physical response. Distinguish metal-dissolution, oxide formation, product transport and structural weakening rather than compressing all visible changes into one category. Separate a possible reaction from a verified rate and a local failure mode from an area-averaged measurement. For this unit, a useful answer must identify an observable that would falsify a favored account and an independent observation that constrains the competing mechanism. Neither ideal electrochemical equations nor visual inspection alone resolves all ambiguities.

## Case for comparative investigation

A welded stainless-steel vessel exhibits attack near the weld rather than across its smooth parent plate. Separate chemistry, microstructure and service causes. Draw a decision tree with a first measurement, one targeted control and one observation that would reject the initial theory. Explain why an attractive laboratory result can be irrelevant if the critical field failure occurs on a different length scale or in a different environmental regime. State the uncertainty that a qualified engineer would need to resolve before authorizing a mitigation or reuse decision.

## Lesson 4.1 — Passive-film formation, composition and defect structure

### Physical account: governing process and critical limits

Passivity describes a low dissolution-current regime sustained by a surface film and associated interfacial processes. Film thickness can be nanometric and its composition may be graded or heterogeneous; composition and defect transport influence repair and breakdown. Chromium-rich stainless passive films, aluminum oxides and titanium oxides differ in chemistry and exposure sensitivity. Measuring low current is supportive but not proof of a uniform impermeable barrier.

**Working relation.** Film growth often couples field-assisted ion migration and interfacial reactions; a measured passive current is a kinetic quantity.

### A concrete case: competing mechanisms

A polished stainless sheet repassivates after brief abrasion while a chloride-exposed crevice does not. Reconcile the observations.

### Synthetic calculation and guided interpretation

For this lesson use the **Composition-only stainless PREN screening** formula card, with the input variable **Nitrogen content** measured in wt%. Its declared computational expression is `18+3.3*2+16*N`. At an illustrative input of 0.048 wt%, the output is 25.368 index; at 0.174 wt%, it is 27.384 index. The two-point secant sensitivity is 16 index per wt%. Interpret the sign and magnitude and then compute a third point without the website to check the calculation. A larger output is not necessarily higher corrosion risk: the meaning of the output depends on whether it is an equilibrium potential, a transport flux, an interfacial response, a thickness margin or an inspection-detection probability.

**Model domain for Passive-film formation, composition and defect structure:** Assumed 18 wt% chromium, 2 wt% molybdenum; empirical composition index limited to certain stainless families and not a life predictor. Calculate independently before generalizing. Any service claim requires evidence that the model assumptions remain valid under the intended operating conditions.

### Investigation: evidence quality, sampling and controls

For **Passive-film formation, composition and defect structure**, document **cross-sectional metallurgy and surface-film methods**, with **alloy certificate, heat history, inclusions, film condition, finishing, weld geometry and temperature**. Challenge the primary conclusion using **alternate surface preparation, reference alloy and microstructural comparison**. Keep independently sampled specimens distinct from repeat readings on the same material, and match environmental histories across treatment groups.

### Diagnostic warning and alternative outcome

Treating passivity as invulnerability can hide defects or locally aggressive solution conditions.

### Assessment: three substantive exercises

**Exercise 1 — mechanism and dimensional reasoning.** Derive or explain the relation `Film growth often couples field-assisted ion migration and interfacial reactions; a measured passive current is a kinetic quantity.` using its physical assumptions. Assign units to the terms that are actually quantitative; for a qualitative relation, replace it with a measurable definition. Distinguish what can be calculated from a textbook constant from what would require a service-specific measurement. *Answer guidance:* every conversion must declare the material, reacting species, coordinate or control volume and environmental state; reject interpretations whose quantities are at incompatible scales.

**Exercise 2 — independent numerical verification.** Recalculate the synthetic pair (0.048, 25.368) and (0.174, 27.384) with proper units, then choose a small change near the first point and estimate sensitivity. Discuss how input uncertainty and a violation of **composition-only stainless pren screening** assumptions would affect a claimed engineering conclusion. *Answer guidance:* calculate from the declared ideal expression, preserve units, and do not convert a formula-generated result into fictional laboratory evidence.

**Exercise 3 — disconfirming experiment.** For the case “A polished stainless sheet repassivates after brief abrasion while a chloride-exposed crevice does not. Reconcile the observations.” specify a target measurement, a matched control, at least three distinct physical specimens when meaningful, an uncertainty source and a criterion that would reject the proposed cause. *Answer guidance:* distinguish damage depth from area-averaged loss, distinguish reaction-driving force from rate, and make sure the independent test is not based on the same unverified assumption.

### Decision exercise and transferable principle

Use surface-sensitive spectroscopy plus localized electrochemical observations before inferring a protective mechanism. Write a short decision memo: what is observed; what is inferred; what has not been measured; what alternative still fits; and which further evidence would justify action. Do not mistake a source with scientific-looking units for a calibrated material result. The goal is not to name as many corrosion forms as possible, but to explain precisely how a physical mechanism could produce the observed failure and how another mechanism could be ruled out.

## Lesson 4.2 — Stainless steels, chromium and alloying effects

### Physical account: governing process and critical limits

Stainless steels rely on an adequate chromium supply and appropriately formed surface films, but corrosion performance also depends on nickel, molybdenum, nitrogen, inclusions, processing and microstructure. Simplified pitting-resistance equivalents help compare some alloys within restricted families; they do not replace qualification in service. High chloride temperature, concentration and crevices can defeat alloys known to be corrosion resistant in ordinary water.

**Working relation.** PREN ≈ wt%Cr + 3.3 wt%Mo + 16 wt%N is a screening index, not an absolute predicted service life.

### A concrete case: competing mechanisms

A procurement table favors an alloy with a higher nominal pitting index, but one supplier has unacceptable inclusions. Decide what additional evidence is necessary.

### Synthetic calculation and guided interpretation

For this lesson use the **Simple protective-scale growth** formula card, with the input variable **Isothermal exposure** measured in hours. Its declared computational expression is `Math.sqrt(0.02*t)`. At an illustrative input of 206 hours, the output is 2.02977831 mg/cm²; at 615 hours, it is 3.50713558 mg/cm². The two-point secant sensitivity is 0.0036121205 mg/cm² per hours. Interpret the sign and magnitude and then compute a third point without the website to check the calculation. A larger output is not necessarily higher corrosion risk: the meaning of the output depends on whether it is an equilibrium potential, a transport flux, an interfacial response, a thickness margin or an inspection-detection probability.

**Model domain for Stainless steels, chromium and alloying effects:** Ideal positive parabolic mass-gain law with kₚ=0.02 (mg/cm²)²/h; no spallation, transient oxidation or gas effects. Calculate independently before generalizing. Any service claim requires evidence that the model assumptions remain valid under the intended operating conditions.

### Investigation: evidence quality, sampling and controls

For **Stainless steels, chromium and alloying effects**, document **cross-sectional metallurgy and surface-film methods**, with **alloy certificate, heat history, inclusions, film condition, finishing, weld geometry and temperature**. Challenge the primary conclusion using **alternate surface preparation, reference alloy and microstructural comparison**. Keep independently sampled specimens distinct from repeat readings on the same material, and match environmental histories across treatment groups.

### Diagnostic warning and alternative outcome

Ranking disparate alloy families by a single composition index ignores processing, surface, crevices and test environment.

### Assessment: three substantive exercises

**Exercise 1 — mechanism and dimensional reasoning.** Derive or explain the relation `PREN ≈ wt%Cr + 3.3 wt%Mo + 16 wt%N is a screening index, not an absolute predicted service life.` using its physical assumptions. Assign units to the terms that are actually quantitative; for a qualitative relation, replace it with a measurable definition. Distinguish what can be calculated from a textbook constant from what would require a service-specific measurement. *Answer guidance:* every conversion must declare the material, reacting species, coordinate or control volume and environmental state; reject interpretations whose quantities are at incompatible scales.

**Exercise 2 — independent numerical verification.** Recalculate the synthetic pair (206, 2.0297783) and (615, 3.5071356) with proper units, then choose a small change near the first point and estimate sensitivity. Discuss how input uncertainty and a violation of **simple protective-scale growth** assumptions would affect a claimed engineering conclusion. *Answer guidance:* calculate from the declared ideal expression, preserve units, and do not convert a formula-generated result into fictional laboratory evidence.

**Exercise 3 — disconfirming experiment.** For the case “A procurement table favors an alloy with a higher nominal pitting index, but one supplier has unacceptable inclusions. Decide what additional evidence is necessary.” specify a target measurement, a matched control, at least three distinct physical specimens when meaningful, an uncertainty source and a criterion that would reject the proposed cause. *Answer guidance:* distinguish damage depth from area-averaged loss, distinguish reaction-driving force from rate, and make sure the independent test is not based on the same unverified assumption.

### Decision exercise and transferable principle

Run comparable susceptibility tests and inspect inclusion statistics and surface condition before selection. Write a short decision memo: what is observed; what is inferred; what has not been measured; what alternative still fits; and which further evidence would justify action. Do not mistake a source with scientific-looking units for a calibrated material result. The goal is not to name as many corrosion forms as possible, but to explain precisely how a physical mechanism could produce the observed failure and how another mechanism could be ruled out.

<!-- MODEL_6 -->

## Lesson 4.3 — Sensitization, welding and heat-affected zones

### Physical account: governing process and critical limits

Heat treatment and welding can alter grain-boundary chemistry, precipitate phases, create residual stress and change surface oxide condition. Some stainless steels may become susceptible to intergranular attack when chromium-depleting carbide precipitation occurs within particular thermal histories; stabilization and low-carbon choices are relevant but not universal remedies. Welds also create geometric crevices and rough regions that can dominate localization independently of sensitization.

**Working relation.** Thermal exposure changes precipitation kinetics; local corrosion follows the resulting composition–microstructure–environment interaction.

### A concrete case: competing mechanisms

Attack runs parallel to a weld heat-affected zone, yet a control sample with the same composition resists corrosion. Design tests to separate metallurgical and geometric factors.

### Synthetic calculation and guided interpretation

For this lesson use the **Composition-only stainless PREN screening** formula card, with the input variable **Nitrogen content** measured in wt%. Its declared computational expression is `18+3.3*2+16*N`. At an illustrative input of 0.075 wt%, the output is 25.8 index; at 0.195 wt%, it is 27.72 index. The two-point secant sensitivity is 16 index per wt%. Interpret the sign and magnitude and then compute a third point without the website to check the calculation. A larger output is not necessarily higher corrosion risk: the meaning of the output depends on whether it is an equilibrium potential, a transport flux, an interfacial response, a thickness margin or an inspection-detection probability.

**Model domain for Sensitization, welding and heat-affected zones:** Assumed 18 wt% chromium, 2 wt% molybdenum; empirical composition index limited to certain stainless families and not a life predictor. Calculate independently before generalizing. Any service claim requires evidence that the model assumptions remain valid under the intended operating conditions.

### Investigation: evidence quality, sampling and controls

For **Sensitization, welding and heat-affected zones**, document **cross-sectional metallurgy and surface-film methods**, with **alloy certificate, heat history, inclusions, film condition, finishing, weld geometry and temperature**. Challenge the primary conclusion using **alternate surface preparation, reference alloy and microstructural comparison**. Keep independently sampled specimens distinct from repeat readings on the same material, and match environmental histories across treatment groups.

### Diagnostic warning and alternative outcome

Attributing any weld-adjacent attack exclusively to carbide sensitization ignores welding consumable, pickling and stress conditions.

### Assessment: three substantive exercises

**Exercise 1 — mechanism and dimensional reasoning.** Derive or explain the relation `Thermal exposure changes precipitation kinetics; local corrosion follows the resulting composition–microstructure–environment interaction.` using its physical assumptions. Assign units to the terms that are actually quantitative; for a qualitative relation, replace it with a measurable definition. Distinguish what can be calculated from a textbook constant from what would require a service-specific measurement. *Answer guidance:* every conversion must declare the material, reacting species, coordinate or control volume and environmental state; reject interpretations whose quantities are at incompatible scales.

**Exercise 2 — independent numerical verification.** Recalculate the synthetic pair (0.075, 25.8) and (0.195, 27.72) with proper units, then choose a small change near the first point and estimate sensitivity. Discuss how input uncertainty and a violation of **composition-only stainless pren screening** assumptions would affect a claimed engineering conclusion. *Answer guidance:* calculate from the declared ideal expression, preserve units, and do not convert a formula-generated result into fictional laboratory evidence.

**Exercise 3 — disconfirming experiment.** For the case “Attack runs parallel to a weld heat-affected zone, yet a control sample with the same composition resists corrosion. Design tests to separate metallurgical and geometric factors.” specify a target measurement, a matched control, at least three distinct physical specimens when meaningful, an uncertainty source and a criterion that would reject the proposed cause. *Answer guidance:* distinguish damage depth from area-averaged loss, distinguish reaction-driving force from rate, and make sure the independent test is not based on the same unverified assumption.

### Decision exercise and transferable principle

Map grain-boundary attack, microhardness and chemical distribution and compare properly prepared weld coupons. Write a short decision memo: what is observed; what is inferred; what has not been measured; what alternative still fits; and which further evidence would justify action. Do not mistake a source with scientific-looking units for a calibrated material result. The goal is not to name as many corrosion forms as possible, but to explain precisely how a physical mechanism could produce the observed failure and how another mechanism could be ruled out.

## Lesson 4.4 — Selective leaching and intergranular degradation

### Physical account: governing process and critical limits

Dealloying can preferentially remove the more reactive component of an alloy, leaving a weakened porous region without proportional external section loss. Classic brass dezincification is one example, but mechanisms vary between alloys. Intergranular attack follows boundaries of differing composition, potential or precipitation state and can severely reduce cohesion. A fracture surface may appear metallic even though subsurface pathways are weakened.

**Working relation.** Mass balance of selectively lost component differs from direct cross-section loss, so area-averaged penetration is not uniquely defined.

### A concrete case: competing mechanisms

A brass valve looks dimensionally intact but leaks and becomes fragile. Decide why weighing the part is inadequate.

### Synthetic calculation and guided interpretation

For this lesson use the **Simple protective-scale growth** formula card, with the input variable **Isothermal exposure** measured in hours. Its declared computational expression is `Math.sqrt(0.02*t)`. At an illustrative input of 296 hours, the output is 2.43310501 mg/cm²; at 685 hours, it is 3.7013511 mg/cm². The two-point secant sensitivity is 0.0032602727 mg/cm² per hours. Interpret the sign and magnitude and then compute a third point without the website to check the calculation. A larger output is not necessarily higher corrosion risk: the meaning of the output depends on whether it is an equilibrium potential, a transport flux, an interfacial response, a thickness margin or an inspection-detection probability.

**Model domain for Selective leaching and intergranular degradation:** Ideal positive parabolic mass-gain law with kₚ=0.02 (mg/cm²)²/h; no spallation, transient oxidation or gas effects. Calculate independently before generalizing. Any service claim requires evidence that the model assumptions remain valid under the intended operating conditions.

### Investigation: evidence quality, sampling and controls

For **Selective leaching and intergranular degradation**, document **cross-sectional metallurgy and surface-film methods**, with **alloy certificate, heat history, inclusions, film condition, finishing, weld geometry and temperature**. Challenge the primary conclusion using **alternate surface preparation, reference alloy and microstructural comparison**. Keep independently sampled specimens distinct from repeat readings on the same material, and match environmental histories across treatment groups.

### Diagnostic warning and alternative outcome

Confusing porous dealloyed metal with a protective surface film can reverse a safety conclusion.

### Assessment: three substantive exercises

**Exercise 1 — mechanism and dimensional reasoning.** Derive or explain the relation `Mass balance of selectively lost component differs from direct cross-section loss, so area-averaged penetration is not uniquely defined.` using its physical assumptions. Assign units to the terms that are actually quantitative; for a qualitative relation, replace it with a measurable definition. Distinguish what can be calculated from a textbook constant from what would require a service-specific measurement. *Answer guidance:* every conversion must declare the material, reacting species, coordinate or control volume and environmental state; reject interpretations whose quantities are at incompatible scales.

**Exercise 2 — independent numerical verification.** Recalculate the synthetic pair (296, 2.433105) and (685, 3.7013511) with proper units, then choose a small change near the first point and estimate sensitivity. Discuss how input uncertainty and a violation of **simple protective-scale growth** assumptions would affect a claimed engineering conclusion. *Answer guidance:* calculate from the declared ideal expression, preserve units, and do not convert a formula-generated result into fictional laboratory evidence.

**Exercise 3 — disconfirming experiment.** For the case “A brass valve looks dimensionally intact but leaks and becomes fragile. Decide why weighing the part is inadequate.” specify a target measurement, a matched control, at least three distinct physical specimens when meaningful, an uncertainty source and a criterion that would reject the proposed cause. *Answer guidance:* distinguish damage depth from area-averaged loss, distinguish reaction-driving force from rate, and make sure the independent test is not based on the same unverified assumption.

### Decision exercise and transferable principle

Use metallographic cross-sections and composition profiles across intact and damaged regions. Write a short decision memo: what is observed; what is inferred; what has not been measured; what alternative still fits; and which further evidence would justify action. Do not mistake a source with scientific-looking units for a calibrated material result. The goal is not to name as many corrosion forms as possible, but to explain precisely how a physical mechanism could produce the observed failure and how another mechanism could be ruled out.

<!-- MODEL_7 -->

## Lesson 4.5 — Microstructure, inclusions and additive-manufactured surfaces

### Physical account: governing process and critical limits

Grain size, second phases, segregation, inclusions and porosity create local potential, film and transport heterogeneity. Additive manufacturing may introduce roughness, unmelted particles, pore networks, residual stress and distinctive phase structures whose effects cannot be inferred from alloy name alone. Surface finishing changes wetting and crevice geometry as well as appearance. Corrosion comparisons must record process history and, where relevant, build orientation.

**Working relation.** An observed effect = composition + microstructure + surface state + environment + interactions; it is not separable without a design.

### A concrete case: competing mechanisms

Two nominally identical nickel-alloy specimens, one wrought and one printed, corrode differently in the same bath. Design a controlled microstructure comparison.

### Synthetic calculation and guided interpretation

For this lesson use the **Composition-only stainless PREN screening** formula card, with the input variable **Nitrogen content** measured in wt%. Its declared computational expression is `18+3.3*2+16*N`. At an illustrative input of 0.102 wt%, the output is 26.232 index; at 0.216 wt%, it is 28.056 index. The two-point secant sensitivity is 16 index per wt%. Interpret the sign and magnitude and then compute a third point without the website to check the calculation. A larger output is not necessarily higher corrosion risk: the meaning of the output depends on whether it is an equilibrium potential, a transport flux, an interfacial response, a thickness margin or an inspection-detection probability.

**Model domain for Microstructure, inclusions and additive-manufactured surfaces:** Assumed 18 wt% chromium, 2 wt% molybdenum; empirical composition index limited to certain stainless families and not a life predictor. Calculate independently before generalizing. Any service claim requires evidence that the model assumptions remain valid under the intended operating conditions.

### Investigation: evidence quality, sampling and controls

For **Microstructure, inclusions and additive-manufactured surfaces**, document **cross-sectional metallurgy and surface-film methods**, with **alloy certificate, heat history, inclusions, film condition, finishing, weld geometry and temperature**. Challenge the primary conclusion using **alternate surface preparation, reference alloy and microstructural comparison**. Keep independently sampled specimens distinct from repeat readings on the same material, and match environmental histories across treatment groups.

### Diagnostic warning and alternative outcome

A single polished coupon may erase the actual manufactured surface features driving field behavior.

### Assessment: three substantive exercises

**Exercise 1 — mechanism and dimensional reasoning.** Derive or explain the relation `An observed effect = composition + microstructure + surface state + environment + interactions; it is not separable without a design.` using its physical assumptions. Assign units to the terms that are actually quantitative; for a qualitative relation, replace it with a measurable definition. Distinguish what can be calculated from a textbook constant from what would require a service-specific measurement. *Answer guidance:* every conversion must declare the material, reacting species, coordinate or control volume and environmental state; reject interpretations whose quantities are at incompatible scales.

**Exercise 2 — independent numerical verification.** Recalculate the synthetic pair (0.102, 26.232) and (0.216, 28.056) with proper units, then choose a small change near the first point and estimate sensitivity. Discuss how input uncertainty and a violation of **composition-only stainless pren screening** assumptions would affect a claimed engineering conclusion. *Answer guidance:* calculate from the declared ideal expression, preserve units, and do not convert a formula-generated result into fictional laboratory evidence.

**Exercise 3 — disconfirming experiment.** For the case “Two nominally identical nickel-alloy specimens, one wrought and one printed, corrode differently in the same bath. Design a controlled microstructure comparison.” specify a target measurement, a matched control, at least three distinct physical specimens when meaningful, an uncertainty source and a criterion that would reject the proposed cause. *Answer guidance:* distinguish damage depth from area-averaged loss, distinguish reaction-driving force from rate, and make sure the independent test is not based on the same unverified assumption.

### Decision exercise and transferable principle

Compare as-built and finished surfaces while matching exposed area, preparation history, and defect maps. Write a short decision memo: what is observed; what is inferred; what has not been measured; what alternative still fits; and which further evidence would justify action. Do not mistake a source with scientific-looking units for a calibrated material result. The goal is not to name as many corrosion forms as possible, but to explain precisely how a physical mechanism could produce the observed failure and how another mechanism could be ruled out.

## Unit 4 capstone — evidence and engineering defense

**Complex case:** A welded stainless-steel vessel exhibits attack near the weld rather than across its smooth parent plate. Separate chemistry, microstructure and service causes.

1. **System definition for Passivation, alloy selection and microstructure:** Sketch the material, phase boundaries, electrolyte or gas paths, stressed features, wet–dry or thermal cycles and measurement locations. State precisely whether the main concern is uniform thinning, maximum pit depth, a crack, surface-electrical function or loss of protective scale.
2. **Two competing mechanisms:** Construct a table with initiating cause, expected spatial pattern, predicted time dependence, contrary evidence and an orthogonal method. Identify which mechanism might operate after rather than before the observed damage.
3. **Numerical audit:** Recalculate both of this unit's models at their default inputs and at the limits of the slider range. Describe the units and whether the model concerns driving force, rate, geometry, or inspection uncertainty. Show at least one reason the model might not apply to the given case.
4. **Sampling and uncertainty:** Build a hierarchy of independent assets or coupons, repeated measurements and local map points. Include instrument calibration, specimen differences, exposure mismatch and the possibility that a rare maximum is missed by ordinary sampling.
5. **Decision note:** Produce a 400-word recommendation with immediate safety implications separated from follow-up research, a repair or monitor option, a cost of wrong inference, and the exact evidence that would change the ranking. Do not claim service life from synthetic data.

### Connecting this unit to materials engineering

A corrosion investigation improves when it preserves the distinction between an electrochemical mechanism, the spatial manifestation of damage, an instrument response and a decision on whether equipment remains fit for service. In **passivation, alloy selection and microstructure**, a defensible conclusion follows a chain of falsifiable physical claims rather than a single parameter selected because it is easy to compute. The mathematics should expose sensitivity and uncertainty, while site observations determine whether the equations apply at all. The companion models are an instructional starting point; professional asset decisions need controlled tests, standards and real-world verification.
