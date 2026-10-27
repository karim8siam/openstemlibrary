# Unit 6: Environmental systems and degradation of nonmetals

**Guiding question:** How do soil, atmosphere, biology, concrete and polymers create time-dependent interacting degradation processes?

## System view and mechanism boundaries

A coated reinforced-concrete marine asset develops stains, cracking, and delamination. Establish which degradation path is causal rather than merely concurrent. The investigation begins with a defined material and state, a particular environment and the time-dependent physical response. Distinguish metal-dissolution, oxide formation, product transport and structural weakening rather than compressing all visible changes into one category. Separate a possible reaction from a verified rate and a local failure mode from an area-averaged measurement. For this unit, a useful answer must identify an observable that would falsify a favored account and an independent observation that constrains the competing mechanism. Neither ideal electrochemical equations nor visual inspection alone resolves all ambiguities.

## Case for comparative investigation

A coated reinforced-concrete marine asset develops stains, cracking, and delamination. Establish which degradation path is causal rather than merely concurrent. Draw a decision tree with a first measurement, one targeted control and one observation that would reject the initial theory. Explain why an attractive laboratory result can be irrelevant if the critical field failure occurs on a different length scale or in a different environmental regime. State the uncertainty that a qualified engineer would need to resolve before authorizing a mitigation or reuse decision.

## Lesson 6.1 — Atmospheric exposure and wet–dry cycling

### Physical account: governing process and critical limits

Atmospheric corrosion depends on duration of surface wetness, temperature, deposits, pollutants, salt loading and material-specific corrosion products. Relative humidity alone does not define a complete electrolyte or damage rate. Wet–dry cycling can concentrate species, open and close conductive paths and alter oxide products. Microclimates beneath insulation or at joints may differ dramatically from weather-station records.

**Working relation.** Total damage is conditional on the time history of electrolyte presence and chemistry, not merely calendar exposure.

### A concrete case: competing mechanisms

A coastal bridge joint corrodes faster than the visible open beam despite matching nominal material and regional climate. Predict environmental differences.

### Synthetic calculation and guided interpretation

For this lesson use the **One-dimensional penetration scale** formula card, with the input variable **Exposure duration** measured in days. Its declared computational expression is `1e6*Math.sqrt(2*1e-13*days*86400)`. At an illustrative input of 15 days, the output is 509.116882 µm; at 53 days, it is 956.995298 µm. The two-point secant sensitivity is 11.786274 µm per days. Interpret the sign and magnitude and then compute a third point without the website to check the calculation. A larger output is not necessarily higher corrosion risk: the meaning of the output depends on whether it is an equilibrium potential, a transport flux, an interfacial response, a thickness margin or an inspection-detection probability.

**Model domain for Atmospheric exposure and wet–dry cycling:** Nominal diffusion length √(2Dt) for D=10⁻¹³ m²/s constant; not an actual chloride threshold or concrete service-life model. Calculate independently before generalizing. Any service claim requires evidence that the model assumptions remain valid under the intended operating conditions.

### Investigation: evidence quality, sampling and controls

For **Atmospheric exposure and wet–dry cycling**, document **environmental microclimate and chemistry mapping**, with **wetness, ions, season, cover depth or polymer formulation, local stress and biofilm evidence**. Challenge the primary conclusion using **nearby controls matched in material but different in exposure**. Keep independently sampled specimens distinct from repeat readings on the same material, and match environmental histories across treatment groups.

### Diagnostic warning and alternative outcome

Applying one regional annual corrosion class to a trapped-salt crevice can miss a severe local hotspot.

### Assessment: three substantive exercises

**Exercise 1 — mechanism and dimensional reasoning.** Derive or explain the relation `Total damage is conditional on the time history of electrolyte presence and chemistry, not merely calendar exposure.` using its physical assumptions. Assign units to the terms that are actually quantitative; for a qualitative relation, replace it with a measurable definition. Distinguish what can be calculated from a textbook constant from what would require a service-specific measurement. *Answer guidance:* every conversion must declare the material, reacting species, coordinate or control volume and environmental state; reject interpretations whose quantities are at incompatible scales.

**Exercise 2 — independent numerical verification.** Recalculate the synthetic pair (15, 509.11688) and (53, 956.9953) with proper units, then choose a small change near the first point and estimate sensitivity. Discuss how input uncertainty and a violation of **one-dimensional penetration scale** assumptions would affect a claimed engineering conclusion. *Answer guidance:* calculate from the declared ideal expression, preserve units, and do not convert a formula-generated result into fictional laboratory evidence.

**Exercise 3 — disconfirming experiment.** For the case “A coastal bridge joint corrodes faster than the visible open beam despite matching nominal material and regional climate. Predict environmental differences.” specify a target measurement, a matched control, at least three distinct physical specimens when meaningful, an uncertainty source and a criterion that would reject the proposed cause. *Answer guidance:* distinguish damage depth from area-averaged loss, distinguish reaction-driving force from rate, and make sure the independent test is not based on the same unverified assumption.

### Decision exercise and transferable principle

Compare time-of-wetness sensors, deposited chloride and matched witness coupons across locations. Write a short decision memo: what is observed; what is inferred; what has not been measured; what alternative still fits; and which further evidence would justify action. Do not mistake a source with scientific-looking units for a calibrated material result. The goal is not to name as many corrosion forms as possible, but to explain precisely how a physical mechanism could produce the observed failure and how another mechanism could be ruled out.

## Lesson 6.2 — Soil, water chemistry and buried infrastructure

### Physical account: governing process and critical limits

Soil is spatially heterogeneous in moisture, conductivity, oxygen availability, microbial activity and soluble ions. Buried assets can cross soil layers with different aeration and resistivity, while groundwater movement alters transport. Bulk soil resistivity is a useful exposure descriptor, but it is not a unique corrosion-rate predictor. Electrical interference from nearby systems may introduce additional current paths.

**Working relation.** Ohmic potential drop follows ΔV=IR for a specified current path; field corrosion needs a distributed-current model.

### A concrete case: competing mechanisms

A buried service line loses metal near a boundary between wet clay and dry fill. Design a spatial investigation rather than relying on a single soil sample.

### Synthetic calculation and guided interpretation

For this lesson use the **Hypothetical defect detection probability** formula card, with the input variable **Independent sampled sites** measured in sites. Its declared computational expression is `100*(1-Math.pow(0.97,n))`. At an illustrative input of 21 sites, the output is 47.2519487 %; at 62 sites, it is 84.8697005 %. The two-point secant sensitivity is 0.91750614 % per sites. Interpret the sign and magnitude and then compute a third point without the website to check the calculation. A larger output is not necessarily higher corrosion risk: the meaning of the output depends on whether it is an equilibrium potential, a transport flux, an interfacial response, a thickness margin or an inspection-detection probability.

**Model domain for Soil, water chemistry and buried infrastructure:** Each site has independent p=0.03 chance of a perfectly detectable defect; clustering, varying rates and misses excluded. Calculate independently before generalizing. Any service claim requires evidence that the model assumptions remain valid under the intended operating conditions.

### Investigation: evidence quality, sampling and controls

For **Soil, water chemistry and buried infrastructure**, document **environmental microclimate and chemistry mapping**, with **wetness, ions, season, cover depth or polymer formulation, local stress and biofilm evidence**. Challenge the primary conclusion using **nearby controls matched in material but different in exposure**. Keep independently sampled specimens distinct from repeat readings on the same material, and match environmental histories across treatment groups.

### Diagnostic warning and alternative outcome

Correlating corrosion solely with low soil resistivity mistakes association for a complete kinetic explanation.

### Assessment: three substantive exercises

**Exercise 1 — mechanism and dimensional reasoning.** Derive or explain the relation `Ohmic potential drop follows ΔV=IR for a specified current path; field corrosion needs a distributed-current model.` using its physical assumptions. Assign units to the terms that are actually quantitative; for a qualitative relation, replace it with a measurable definition. Distinguish what can be calculated from a textbook constant from what would require a service-specific measurement. *Answer guidance:* every conversion must declare the material, reacting species, coordinate or control volume and environmental state; reject interpretations whose quantities are at incompatible scales.

**Exercise 2 — independent numerical verification.** Recalculate the synthetic pair (21, 47.251949) and (62, 84.869701) with proper units, then choose a small change near the first point and estimate sensitivity. Discuss how input uncertainty and a violation of **hypothetical defect detection probability** assumptions would affect a claimed engineering conclusion. *Answer guidance:* calculate from the declared ideal expression, preserve units, and do not convert a formula-generated result into fictional laboratory evidence.

**Exercise 3 — disconfirming experiment.** For the case “A buried service line loses metal near a boundary between wet clay and dry fill. Design a spatial investigation rather than relying on a single soil sample.” specify a target measurement, a matched control, at least three distinct physical specimens when meaningful, an uncertainty source and a criterion that would reject the proposed cause. *Answer guidance:* distinguish damage depth from area-averaged loss, distinguish reaction-driving force from rate, and make sure the independent test is not based on the same unverified assumption.

### Decision exercise and transferable principle

Co-register pipe-depth, soil-profile, potential and thickness data with traceable mapping. Write a short decision memo: what is observed; what is inferred; what has not been measured; what alternative still fits; and which further evidence would justify action. Do not mistake a source with scientific-looking units for a calibrated material result. The goal is not to name as many corrosion forms as possible, but to explain precisely how a physical mechanism could produce the observed failure and how another mechanism could be ruled out.

<!-- MODEL_10 -->

## Lesson 6.3 — Microbiologically influenced corrosion

### Physical account: governing process and critical limits

Microbial communities can influence local chemistry, film formation, oxidation and reduction pathways, changing corrosion susceptibility or rate. Biological presence does not by itself prove that microbes caused a given pit; organisms can colonize already corroded regions. Microbial activity varies with nutrients, redox conditions, temperature and flow. Demonstrating mechanism requires evidence from chemistry, microbiology, materials characterization and exposure conditions together.

**Working relation.** An observed association P(pitting | biofilm) is not alone a causal estimate of biofilm-driven corrosion.

### A concrete case: competing mechanisms

A corroded water tank contains biofilm at every pit. Differentiate causal microbial effects from preferential biofilm collection at rough attacked surfaces.

### Synthetic calculation and guided interpretation

For this lesson use the **One-dimensional penetration scale** formula card, with the input variable **Exposure duration** measured in days. Its declared computational expression is `1e6*Math.sqrt(2*1e-13*days*86400)`. At an illustrative input of 23 days, the output is 630.428426 µm; at 59 days, it is 1009.71283 µm. The two-point secant sensitivity is 10.535678 µm per days. Interpret the sign and magnitude and then compute a third point without the website to check the calculation. A larger output is not necessarily higher corrosion risk: the meaning of the output depends on whether it is an equilibrium potential, a transport flux, an interfacial response, a thickness margin or an inspection-detection probability.

**Model domain for Microbiologically influenced corrosion:** Nominal diffusion length √(2Dt) for D=10⁻¹³ m²/s constant; not an actual chloride threshold or concrete service-life model. Calculate independently before generalizing. Any service claim requires evidence that the model assumptions remain valid under the intended operating conditions.

### Investigation: evidence quality, sampling and controls

For **Microbiologically influenced corrosion**, document **environmental microclimate and chemistry mapping**, with **wetness, ions, season, cover depth or polymer formulation, local stress and biofilm evidence**. Challenge the primary conclusion using **nearby controls matched in material but different in exposure**. Keep independently sampled specimens distinct from repeat readings on the same material, and match environmental histories across treatment groups.

### Diagnostic warning and alternative outcome

Claiming a particular organism caused failure from sequencing data alone overstates causation.

### Assessment: three substantive exercises

**Exercise 1 — mechanism and dimensional reasoning.** Derive or explain the relation `An observed association P(pitting | biofilm) is not alone a causal estimate of biofilm-driven corrosion.` using its physical assumptions. Assign units to the terms that are actually quantitative; for a qualitative relation, replace it with a measurable definition. Distinguish what can be calculated from a textbook constant from what would require a service-specific measurement. *Answer guidance:* every conversion must declare the material, reacting species, coordinate or control volume and environmental state; reject interpretations whose quantities are at incompatible scales.

**Exercise 2 — independent numerical verification.** Recalculate the synthetic pair (23, 630.42843) and (59, 1009.7128) with proper units, then choose a small change near the first point and estimate sensitivity. Discuss how input uncertainty and a violation of **one-dimensional penetration scale** assumptions would affect a claimed engineering conclusion. *Answer guidance:* calculate from the declared ideal expression, preserve units, and do not convert a formula-generated result into fictional laboratory evidence.

**Exercise 3 — disconfirming experiment.** For the case “A corroded water tank contains biofilm at every pit. Differentiate causal microbial effects from preferential biofilm collection at rough attacked surfaces.” specify a target measurement, a matched control, at least three distinct physical specimens when meaningful, an uncertainty source and a criterion that would reject the proposed cause. *Answer guidance:* distinguish damage depth from area-averaged loss, distinguish reaction-driving force from rate, and make sure the independent test is not based on the same unverified assumption.

### Decision exercise and transferable principle

Compare matching sterile controls where feasible, metabolic signatures, pit morphology and local chemistry. Write a short decision memo: what is observed; what is inferred; what has not been measured; what alternative still fits; and which further evidence would justify action. Do not mistake a source with scientific-looking units for a calibrated material result. The goal is not to name as many corrosion forms as possible, but to explain precisely how a physical mechanism could produce the observed failure and how another mechanism could be ruled out.

## Lesson 6.4 — Reinforced concrete, carbonation and chloride ingress

### Physical account: governing process and critical limits

Steel in sound alkaline concrete can form a passive surface, but carbonation and chloride ingress may change electrochemical conditions at reinforcement. Concrete permeability, cracking, cover depth, moisture and electrical connectivity influence transport and corrosion progression. Rust volume changes and expansive stresses can cause cover cracking and spalling, so visible damage may lag initiation. Chloride thresholds vary with binding, steel condition and exposure; a single universal concentration is inappropriate.

**Working relation.** A simplified diffusion depth scale ℓ≈sqrt(D_eff t) omits binding, cracks and evolving transport.

### A concrete case: competing mechanisms

A parking structure shows concrete spalling over rebar while adjacent dry bays remain intact. Establish a staged mechanism.

### Synthetic calculation and guided interpretation

For this lesson use the **Hypothetical defect detection probability** formula card, with the input variable **Independent sampled sites** measured in sites. Its declared computational expression is `100*(1-Math.pow(0.97,n))`. At an illustrative input of 30 sites, the output is 59.8992931 %; at 69 sites, it is 87.7749776 %. The two-point secant sensitivity is 0.71476114 % per sites. Interpret the sign and magnitude and then compute a third point without the website to check the calculation. A larger output is not necessarily higher corrosion risk: the meaning of the output depends on whether it is an equilibrium potential, a transport flux, an interfacial response, a thickness margin or an inspection-detection probability.

**Model domain for Reinforced concrete, carbonation and chloride ingress:** Each site has independent p=0.03 chance of a perfectly detectable defect; clustering, varying rates and misses excluded. Calculate independently before generalizing. Any service claim requires evidence that the model assumptions remain valid under the intended operating conditions.

### Investigation: evidence quality, sampling and controls

For **Reinforced concrete, carbonation and chloride ingress**, document **environmental microclimate and chemistry mapping**, with **wetness, ions, season, cover depth or polymer formulation, local stress and biofilm evidence**. Challenge the primary conclusion using **nearby controls matched in material but different in exposure**. Keep independently sampled specimens distinct from repeat readings on the same material, and match environmental histories across treatment groups.

### Diagnostic warning and alternative outcome

One chloride measurement at the surface cannot establish the concentration at reinforcement depth.

### Assessment: three substantive exercises

**Exercise 1 — mechanism and dimensional reasoning.** Derive or explain the relation `A simplified diffusion depth scale ℓ≈sqrt(D_eff t) omits binding, cracks and evolving transport.` using its physical assumptions. Assign units to the terms that are actually quantitative; for a qualitative relation, replace it with a measurable definition. Distinguish what can be calculated from a textbook constant from what would require a service-specific measurement. *Answer guidance:* every conversion must declare the material, reacting species, coordinate or control volume and environmental state; reject interpretations whose quantities are at incompatible scales.

**Exercise 2 — independent numerical verification.** Recalculate the synthetic pair (30, 59.899293) and (69, 87.774978) with proper units, then choose a small change near the first point and estimate sensitivity. Discuss how input uncertainty and a violation of **hypothetical defect detection probability** assumptions would affect a claimed engineering conclusion. *Answer guidance:* calculate from the declared ideal expression, preserve units, and do not convert a formula-generated result into fictional laboratory evidence.

**Exercise 3 — disconfirming experiment.** For the case “A parking structure shows concrete spalling over rebar while adjacent dry bays remain intact. Establish a staged mechanism.” specify a target measurement, a matched control, at least three distinct physical specimens when meaningful, an uncertainty source and a criterion that would reject the proposed cause. *Answer guidance:* distinguish damage depth from area-averaged loss, distinguish reaction-driving force from rate, and make sure the independent test is not based on the same unverified assumption.

### Decision exercise and transferable principle

Combine cover depth, chloride profiles, carbonation depth and targeted corrosion-potential mapping. Write a short decision memo: what is observed; what is inferred; what has not been measured; what alternative still fits; and which further evidence would justify action. Do not mistake a source with scientific-looking units for a calibrated material result. The goal is not to name as many corrosion forms as possible, but to explain precisely how a physical mechanism could produce the observed failure and how another mechanism could be ruled out.

<!-- MODEL_11 -->

## Lesson 6.5 — Polymer aging, stress and environmental cracking

### Physical account: governing process and critical limits

Polymers can degrade by oxidation, hydrolysis, ultraviolet exposure, solvent uptake, plasticizer migration, thermal chain scission or environmental stress cracking. The dominant path depends on formulation, morphology, stress and the actual spectrum of exposure. Color change may be cosmetic while mechanical embrittlement proceeds unseen, or vice versa. Mechanical function should be tested under realistic timescales and environmental cycles.

**Working relation.** Diffusion uptake for simple short-time Fickian conditions often scales approximately with sqrt(t); saturation and damage invalidate it.

### A concrete case: competing mechanisms

A plastic seal becomes brittle in sunlight, while an identical stored seal remains flexible. Identify competing physical and chemical causes.

### Synthetic calculation and guided interpretation

For this lesson use the **One-dimensional penetration scale** formula card, with the input variable **Exposure duration** measured in days. Its declared computational expression is `1e6*Math.sqrt(2*1e-13*days*86400)`. At an illustrative input of 31 days, the output is 731.901633 µm; at 65 days, it is 1059.8113 µm. The two-point secant sensitivity is 9.6444021 µm per days. Interpret the sign and magnitude and then compute a third point without the website to check the calculation. A larger output is not necessarily higher corrosion risk: the meaning of the output depends on whether it is an equilibrium potential, a transport flux, an interfacial response, a thickness margin or an inspection-detection probability.

**Model domain for Polymer aging, stress and environmental cracking:** Nominal diffusion length √(2Dt) for D=10⁻¹³ m²/s constant; not an actual chloride threshold or concrete service-life model. Calculate independently before generalizing. Any service claim requires evidence that the model assumptions remain valid under the intended operating conditions.

### Investigation: evidence quality, sampling and controls

For **Polymer aging, stress and environmental cracking**, document **environmental microclimate and chemistry mapping**, with **wetness, ions, season, cover depth or polymer formulation, local stress and biofilm evidence**. Challenge the primary conclusion using **nearby controls matched in material but different in exposure**. Keep independently sampled specimens distinct from repeat readings on the same material, and match environmental histories across treatment groups.

### Diagnostic warning and alternative outcome

Using a single UV-exposure hour count to predict years of field life ignores wavelength and temperature interactions.

### Assessment: three substantive exercises

**Exercise 1 — mechanism and dimensional reasoning.** Derive or explain the relation `Diffusion uptake for simple short-time Fickian conditions often scales approximately with sqrt(t); saturation and damage invalidate it.` using its physical assumptions. Assign units to the terms that are actually quantitative; for a qualitative relation, replace it with a measurable definition. Distinguish what can be calculated from a textbook constant from what would require a service-specific measurement. *Answer guidance:* every conversion must declare the material, reacting species, coordinate or control volume and environmental state; reject interpretations whose quantities are at incompatible scales.

**Exercise 2 — independent numerical verification.** Recalculate the synthetic pair (31, 731.90163) and (65, 1059.8113) with proper units, then choose a small change near the first point and estimate sensitivity. Discuss how input uncertainty and a violation of **one-dimensional penetration scale** assumptions would affect a claimed engineering conclusion. *Answer guidance:* calculate from the declared ideal expression, preserve units, and do not convert a formula-generated result into fictional laboratory evidence.

**Exercise 3 — disconfirming experiment.** For the case “A plastic seal becomes brittle in sunlight, while an identical stored seal remains flexible. Identify competing physical and chemical causes.” specify a target measurement, a matched control, at least three distinct physical specimens when meaningful, an uncertainty source and a criterion that would reject the proposed cause. *Answer guidance:* distinguish damage depth from area-averaged loss, distinguish reaction-driving force from rate, and make sure the independent test is not based on the same unverified assumption.

### Decision exercise and transferable principle

Compare molecular-weight or chemical signatures and retained mechanical properties after controlled exposure. Write a short decision memo: what is observed; what is inferred; what has not been measured; what alternative still fits; and which further evidence would justify action. Do not mistake a source with scientific-looking units for a calibrated material result. The goal is not to name as many corrosion forms as possible, but to explain precisely how a physical mechanism could produce the observed failure and how another mechanism could be ruled out.

## Unit 6 capstone — evidence and engineering defense

**Complex case:** A coated reinforced-concrete marine asset develops stains, cracking, and delamination. Establish which degradation path is causal rather than merely concurrent.

1. **System definition for Environmental systems and degradation of nonmetals:** Sketch the material, phase boundaries, electrolyte or gas paths, stressed features, wet–dry or thermal cycles and measurement locations. State precisely whether the main concern is uniform thinning, maximum pit depth, a crack, surface-electrical function or loss of protective scale.
2. **Two competing mechanisms:** Construct a table with initiating cause, expected spatial pattern, predicted time dependence, contrary evidence and an orthogonal method. Identify which mechanism might operate after rather than before the observed damage.
3. **Numerical audit:** Recalculate both of this unit's models at their default inputs and at the limits of the slider range. Describe the units and whether the model concerns driving force, rate, geometry, or inspection uncertainty. Show at least one reason the model might not apply to the given case.
4. **Sampling and uncertainty:** Build a hierarchy of independent assets or coupons, repeated measurements and local map points. Include instrument calibration, specimen differences, exposure mismatch and the possibility that a rare maximum is missed by ordinary sampling.
5. **Decision note:** Produce a 400-word recommendation with immediate safety implications separated from follow-up research, a repair or monitor option, a cost of wrong inference, and the exact evidence that would change the ranking. Do not claim service life from synthetic data.

### Connecting this unit to materials engineering

A corrosion investigation improves when it preserves the distinction between an electrochemical mechanism, the spatial manifestation of damage, an instrument response and a decision on whether equipment remains fit for service. In **environmental systems and degradation of nonmetals**, a defensible conclusion follows a chain of falsifiable physical claims rather than a single parameter selected because it is easy to compute. The mathematics should expose sensitivity and uncertainty, while site observations determine whether the equations apply at all. The companion models are an instructional starting point; professional asset decisions need controlled tests, standards and real-world verification.
