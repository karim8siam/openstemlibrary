# Unit 7: Corrosion testing, monitoring and failure analysis

**Guiding question:** How can a test result support a real operating decision rather than become a misleading laboratory number?

## System view and mechanism boundaries

An accelerated test ranks two candidate materials opposite to their field history. Design an evidence audit, sampling program, and cautious decision. The investigation begins with a defined material and state, a particular environment and the time-dependent physical response. Distinguish metal-dissolution, oxide formation, product transport and structural weakening rather than compressing all visible changes into one category. Separate a possible reaction from a verified rate and a local failure mode from an area-averaged measurement. For this unit, a useful answer must identify an observable that would falsify a favored account and an independent observation that constrains the competing mechanism. Neither ideal electrochemical equations nor visual inspection alone resolves all ambiguities.

## Case for comparative investigation

An accelerated test ranks two candidate materials opposite to their field history. Design an evidence audit, sampling program, and cautious decision. Draw a decision tree with a first measurement, one targeted control and one observation that would reject the initial theory. Explain why an attractive laboratory result can be irrelevant if the critical field failure occurs on a different length scale or in a different environmental regime. State the uncertainty that a qualified engineer would need to resolve before authorizing a mitigation or reuse decision.

## Lesson 7.1 — Immersion mass-loss tests and reporting quality

### Physical account: governing process and critical limits

Gravimetric immersion tests quantify mass loss over a defined exposed area and interval, after a specified product-removal method. Cleaning may remove base metal, leave scale behind or contaminate mass measurements. Geometry, test vessel, gas exchange, solution renewal, flow, duration and temperature can determine the outcome. ASTM G31 is a guide to controlling and documenting such variables and explicitly warns that accelerated tests may mislead.

**Working relation.** CR(mm/y)=87.6 W/(ρ A t), where W mg, ρ g/cm³, A cm², t h for ideal general metal loss.

### A concrete case: competing mechanisms

A laboratory reports six decimal places for corrosion rate without specimen area or cleaning description. Identify which data are missing.

### Synthetic calculation and guided interpretation

For this lesson use the **Gravimetric corrosion-rate conversion** formula card, with the input variable **Measured metal mass loss** measured in mg. Its declared computational expression is `87.6*W/(7.85*20*168)`. At an illustrative input of 33 mg, the output is 0.109599636 mm/year; at 116 mg, it is 0.385259327 mm/year. The two-point secant sensitivity is 0.0033212011 mm/year per mg. Interpret the sign and magnitude and then compute a third point without the website to check the calculation. A larger output is not necessarily higher corrosion risk: the meaning of the output depends on whether it is an equilibrium potential, a transport flux, an interfacial response, a thickness margin or an inspection-detection probability.

**Model domain for Immersion mass-loss tests and reporting quality:** Pure density 7.85 g/cm³, area 20 cm², 168 h; consistent cleaned mass loss; general corrosion only. Calculate independently before generalizing. Any service claim requires evidence that the model assumptions remain valid under the intended operating conditions.

### Investigation: evidence quality, sampling and controls

For **Immersion mass-loss tests and reporting quality**, document **independent tests with instrument and specimen controls**, with **measurement reference, sample cleaning, repeat lot, raw signals, data treatment and response thresholds**. Challenge the primary conclusion using **field specimens, parallel methods and blind review of the damage map**. Keep independently sampled specimens distinct from repeat readings on the same material, and match environmental histories across treatment groups.

### Diagnostic warning and alternative outcome

Converting total mass change directly to local pit depth confuses averaged and worst-case degradation.

### Assessment: three substantive exercises

**Exercise 1 — mechanism and dimensional reasoning.** Derive or explain the relation `CR(mm/y)=87.6 W/(ρ A t), where W mg, ρ g/cm³, A cm², t h for ideal general metal loss.` using its physical assumptions. Assign units to the terms that are actually quantitative; for a qualitative relation, replace it with a measurable definition. Distinguish what can be calculated from a textbook constant from what would require a service-specific measurement. *Answer guidance:* every conversion must declare the material, reacting species, coordinate or control volume and environmental state; reject interpretations whose quantities are at incompatible scales.

**Exercise 2 — independent numerical verification.** Recalculate the synthetic pair (33, 0.10959964) and (116, 0.38525933) with proper units, then choose a small change near the first point and estimate sensitivity. Discuss how input uncertainty and a violation of **gravimetric corrosion-rate conversion** assumptions would affect a claimed engineering conclusion. *Answer guidance:* calculate from the declared ideal expression, preserve units, and do not convert a formula-generated result into fictional laboratory evidence.

**Exercise 3 — disconfirming experiment.** For the case “A laboratory reports six decimal places for corrosion rate without specimen area or cleaning description. Identify which data are missing.” specify a target measurement, a matched control, at least three distinct physical specimens when meaningful, an uncertainty source and a criterion that would reject the proposed cause. *Answer guidance:* distinguish damage depth from area-averaged loss, distinguish reaction-driving force from rate, and make sure the independent test is not based on the same unverified assumption.

### Decision exercise and transferable principle

Check blank cleaning loss, specimen repetitions and post-test pit profiles before reporting service relevance. Write a short decision memo: what is observed; what is inferred; what has not been measured; what alternative still fits; and which further evidence would justify action. Do not mistake a source with scientific-looking units for a calibrated material result. The goal is not to name as many corrosion forms as possible, but to explain precisely how a physical mechanism could produce the observed failure and how another mechanism could be ruled out.

## Lesson 7.2 — Electrochemical impedance and time-constant interpretation

### Physical account: governing process and critical limits

Electrochemical impedance spectroscopy observes a system response over frequency at suitably small perturbations. Simple equivalent circuits can aid interpretation of solution resistance, charge-transfer response, film capacitance and dispersion, but more than one physical network can yield similar spectra. A fitted constant-phase element is a mathematical representation, not automatically a film thickness. Stationarity, perturbation amplitude and model identifiability must be checked.

**Working relation.** For a simple parallel R–C branch, |Z_C|=1/(2π f C); actual coatings may show distributed response.

### A concrete case: competing mechanisms

A painted steel panel exhibits rising low-frequency impedance after curing; an engineer declares a proportional rise in service life. Examine the claim.

### Synthetic calculation and guided interpretation

For this lesson use the **Idealized R–C capacitive magnitude** formula card, with the input variable **Signal frequency** measured in Hz. Its declared computational expression is `1/(2*Math.PI*f*0.0001)`. At an illustrative input of 205.0795 Hz, the output is 7.76064614 Ω; at 615.0385 Hz, it is 2.58772326 Ω. The two-point secant sensitivity is -0.012618147 Ω per Hz. Interpret the sign and magnitude and then compute a third point without the website to check the calculation. A larger output is not necessarily higher corrosion risk: the meaning of the output depends on whether it is an equilibrium potential, a transport flux, an interfacial response, a thickness margin or an inspection-detection probability.

**Model domain for Electrochemical impedance and time-constant interpretation:** Pure capacitor C=100 µF, sinusoidal linear signal; no pore network, nonideal capacitance or corrosion circuit inference. Calculate independently before generalizing. Any service claim requires evidence that the model assumptions remain valid under the intended operating conditions.

### Investigation: evidence quality, sampling and controls

For **Electrochemical impedance and time-constant interpretation**, document **independent tests with instrument and specimen controls**, with **measurement reference, sample cleaning, repeat lot, raw signals, data treatment and response thresholds**. Challenge the primary conclusion using **field specimens, parallel methods and blind review of the damage map**. Keep independently sampled specimens distinct from repeat readings on the same material, and match environmental histories across treatment groups.

### Diagnostic warning and alternative outcome

Excellent curve fits do not uniquely prove the chosen corrosion mechanism.

### Assessment: three substantive exercises

**Exercise 1 — mechanism and dimensional reasoning.** Derive or explain the relation `For a simple parallel R–C branch, |Z_C|=1/(2π f C); actual coatings may show distributed response.` using its physical assumptions. Assign units to the terms that are actually quantitative; for a qualitative relation, replace it with a measurable definition. Distinguish what can be calculated from a textbook constant from what would require a service-specific measurement. *Answer guidance:* every conversion must declare the material, reacting species, coordinate or control volume and environmental state; reject interpretations whose quantities are at incompatible scales.

**Exercise 2 — independent numerical verification.** Recalculate the synthetic pair (205.0795, 7.7606461) and (615.0385, 2.5877233) with proper units, then choose a small change near the first point and estimate sensitivity. Discuss how input uncertainty and a violation of **idealized r–c capacitive magnitude** assumptions would affect a claimed engineering conclusion. *Answer guidance:* calculate from the declared ideal expression, preserve units, and do not convert a formula-generated result into fictional laboratory evidence.

**Exercise 3 — disconfirming experiment.** For the case “A painted steel panel exhibits rising low-frequency impedance after curing; an engineer declares a proportional rise in service life. Examine the claim.” specify a target measurement, a matched control, at least three distinct physical specimens when meaningful, an uncertainty source and a criterion that would reject the proposed cause. *Answer guidance:* distinguish damage depth from area-averaged loss, distinguish reaction-driving force from rate, and make sure the independent test is not based on the same unverified assumption.

### Decision exercise and transferable principle

Compare measured spectra before and after controlled defect introduction with microscopy and mass-loss evidence. Write a short decision memo: what is observed; what is inferred; what has not been measured; what alternative still fits; and which further evidence would justify action. Do not mistake a source with scientific-looking units for a calibrated material result. The goal is not to name as many corrosion forms as possible, but to explain precisely how a physical mechanism could produce the observed failure and how another mechanism could be ruled out.

<!-- MODEL_12 -->

## Lesson 7.3 — Accelerated exposures and relevance of salt spray

### Physical account: governing process and critical limits

Salt spray and cyclic accelerated weathering expose materials to repeatable stressors but do not provide universal clocks for natural service. Continuous spray can suppress realistic drying or alter corrosion-product formation compared with intermittent wetting. Relative rankings may change with coating system, alloy and environment. Test objectives should be explicit: defect screening, batch comparison or site-life prediction require different evidence.

**Working relation.** Acceleration factor = field time/test time only when a validated common damage endpoint and mechanism exist.

### A concrete case: competing mechanisms

Two painted fastener finishes rank opposite under continuous salt spray and an outdoor coastal rack. Propose why neither result automatically invalidates the other.

### Synthetic calculation and guided interpretation

For this lesson use the **Gravimetric corrosion-rate conversion** formula card, with the input variable **Measured metal mass loss** measured in mg. Its declared computational expression is `87.6*W/(7.85*20*168)`. At an illustrative input of 51 mg, the output is 0.169381256 mm/year; at 130 mg, it is 0.431756142 mm/year. The two-point secant sensitivity is 0.0033212011 mm/year per mg. Interpret the sign and magnitude and then compute a third point without the website to check the calculation. A larger output is not necessarily higher corrosion risk: the meaning of the output depends on whether it is an equilibrium potential, a transport flux, an interfacial response, a thickness margin or an inspection-detection probability.

**Model domain for Accelerated exposures and relevance of salt spray:** Pure density 7.85 g/cm³, area 20 cm², 168 h; consistent cleaned mass loss; general corrosion only. Calculate independently before generalizing. Any service claim requires evidence that the model assumptions remain valid under the intended operating conditions.

### Investigation: evidence quality, sampling and controls

For **Accelerated exposures and relevance of salt spray**, document **independent tests with instrument and specimen controls**, with **measurement reference, sample cleaning, repeat lot, raw signals, data treatment and response thresholds**. Challenge the primary conclusion using **field specimens, parallel methods and blind review of the damage map**. Keep independently sampled specimens distinct from repeat readings on the same material, and match environmental histories across treatment groups.

### Diagnostic warning and alternative outcome

Claiming 1000 test hours equal a precise number of service years without correlation is unjustified.

### Assessment: three substantive exercises

**Exercise 1 — mechanism and dimensional reasoning.** Derive or explain the relation `Acceleration factor = field time/test time only when a validated common damage endpoint and mechanism exist.` using its physical assumptions. Assign units to the terms that are actually quantitative; for a qualitative relation, replace it with a measurable definition. Distinguish what can be calculated from a textbook constant from what would require a service-specific measurement. *Answer guidance:* every conversion must declare the material, reacting species, coordinate or control volume and environmental state; reject interpretations whose quantities are at incompatible scales.

**Exercise 2 — independent numerical verification.** Recalculate the synthetic pair (51, 0.16938126) and (130, 0.43175614) with proper units, then choose a small change near the first point and estimate sensitivity. Discuss how input uncertainty and a violation of **gravimetric corrosion-rate conversion** assumptions would affect a claimed engineering conclusion. *Answer guidance:* calculate from the declared ideal expression, preserve units, and do not convert a formula-generated result into fictional laboratory evidence.

**Exercise 3 — disconfirming experiment.** For the case “Two painted fastener finishes rank opposite under continuous salt spray and an outdoor coastal rack. Propose why neither result automatically invalidates the other.” specify a target measurement, a matched control, at least three distinct physical specimens when meaningful, an uncertainty source and a criterion that would reject the proposed cause. *Answer guidance:* distinguish damage depth from area-averaged loss, distinguish reaction-driving force from rate, and make sure the independent test is not based on the same unverified assumption.

### Decision exercise and transferable principle

Pair accelerated protocols with outdoor exposure or documented field benchmarks using the same failure metrics. Write a short decision memo: what is observed; what is inferred; what has not been measured; what alternative still fits; and which further evidence would justify action. Do not mistake a source with scientific-looking units for a calibrated material result. The goal is not to name as many corrosion forms as possible, but to explain precisely how a physical mechanism could produce the observed failure and how another mechanism could be ruled out.

## Lesson 7.4 — Nondestructive monitoring and localization probability

### Physical account: governing process and critical limits

In situ monitoring combines thickness, corrosion probes, electrochemical potential, acoustic methods and environmental data, each sampling different features and volumes. A sensor can show low corrosion at its location while a distant crevice grows. Inspection strategy should reflect defect detectability, access, condition and cost; dense data do not eliminate systematic blind spots. Trending requires stable calibration and the ability to distinguish real deterioration from sensor drift.

**Working relation.** P(detect ≥1)=1−(1−p)^n only if events are independent and detection is perfect.

### A concrete case: competing mechanisms

A pipeline has hundreds of stable corrosion-monitoring readings yet one under-deposit leak. Explain the sampling failure.

### Synthetic calculation and guided interpretation

For this lesson use the **Idealized R–C capacitive magnitude** formula card, with the input variable **Signal frequency** measured in Hz. Its declared computational expression is `1/(2*Math.PI*f*0.0001)`. At an illustrative input of 295.0705 Hz, the output is 5.39379379 Ω; at 685.0315 Hz, it is 2.32332299 Ω. The two-point secant sensitivity is -0.0078737894 Ω per Hz. Interpret the sign and magnitude and then compute a third point without the website to check the calculation. A larger output is not necessarily higher corrosion risk: the meaning of the output depends on whether it is an equilibrium potential, a transport flux, an interfacial response, a thickness margin or an inspection-detection probability.

**Model domain for Nondestructive monitoring and localization probability:** Pure capacitor C=100 µF, sinusoidal linear signal; no pore network, nonideal capacitance or corrosion circuit inference. Calculate independently before generalizing. Any service claim requires evidence that the model assumptions remain valid under the intended operating conditions.

### Investigation: evidence quality, sampling and controls

For **Nondestructive monitoring and localization probability**, document **independent tests with instrument and specimen controls**, with **measurement reference, sample cleaning, repeat lot, raw signals, data treatment and response thresholds**. Challenge the primary conclusion using **field specimens, parallel methods and blind review of the damage map**. Keep independently sampled specimens distinct from repeat readings on the same material, and match environmental histories across treatment groups.

### Diagnostic warning and alternative outcome

Treating a probability model with independent sites as a guarantee for clustered defects overstates coverage.

### Assessment: three substantive exercises

**Exercise 1 — mechanism and dimensional reasoning.** Derive or explain the relation `P(detect ≥1)=1−(1−p)^n only if events are independent and detection is perfect.` using its physical assumptions. Assign units to the terms that are actually quantitative; for a qualitative relation, replace it with a measurable definition. Distinguish what can be calculated from a textbook constant from what would require a service-specific measurement. *Answer guidance:* every conversion must declare the material, reacting species, coordinate or control volume and environmental state; reject interpretations whose quantities are at incompatible scales.

**Exercise 2 — independent numerical verification.** Recalculate the synthetic pair (295.0705, 5.3937938) and (685.0315, 2.323323) with proper units, then choose a small change near the first point and estimate sensitivity. Discuss how input uncertainty and a violation of **idealized r–c capacitive magnitude** assumptions would affect a claimed engineering conclusion. *Answer guidance:* calculate from the declared ideal expression, preserve units, and do not convert a formula-generated result into fictional laboratory evidence.

**Exercise 3 — disconfirming experiment.** For the case “A pipeline has hundreds of stable corrosion-monitoring readings yet one under-deposit leak. Explain the sampling failure.” specify a target measurement, a matched control, at least three distinct physical specimens when meaningful, an uncertainty source and a criterion that would reject the proposed cause. *Answer guidance:* distinguish damage depth from area-averaged loss, distinguish reaction-driving force from rate, and make sure the independent test is not based on the same unverified assumption.

### Decision exercise and transferable principle

Sample high-risk geometries deliberately and validate sensor readings with direct inspection. Write a short decision memo: what is observed; what is inferred; what has not been measured; what alternative still fits; and which further evidence would justify action. Do not mistake a source with scientific-looking units for a calibrated material result. The goal is not to name as many corrosion forms as possible, but to explain precisely how a physical mechanism could produce the observed failure and how another mechanism could be ruled out.

<!-- MODEL_13 -->

## Lesson 7.5 — Fractography, root cause and evidence grading

### Physical account: governing process and critical limits

A credible corrosion failure analysis reconstructs load history, environment, geometry, material condition and timing before concluding mechanism. Fracture-surface photographs can support hypotheses but are rarely unique signatures in isolation. Metallography and chemistry must be integrated with maintenance records and control samples. Root cause may be a chain: design trap, poor material control, inadequate monitoring and abnormal process conditions, rather than one named corrosion type.

**Working relation.** Inference confidence increases when independent predicted observations converge; no universal scalar root-cause equation exists.

### A concrete case: competing mechanisms

A failed shaft contains both rust and fatigue-like striations. Determine whether rust caused initiation or invaded a crack after failure.

### Synthetic calculation and guided interpretation

For this lesson use the **Gravimetric corrosion-rate conversion** formula card, with the input variable **Measured metal mass loss** measured in mg. Its declared computational expression is `87.6*W/(7.85*20*168)`. At an illustrative input of 69 mg, the output is 0.229162875 mm/year; at 144 mg, it is 0.478252957 mm/year. The two-point secant sensitivity is 0.0033212011 mm/year per mg. Interpret the sign and magnitude and then compute a third point without the website to check the calculation. A larger output is not necessarily higher corrosion risk: the meaning of the output depends on whether it is an equilibrium potential, a transport flux, an interfacial response, a thickness margin or an inspection-detection probability.

**Model domain for Fractography, root cause and evidence grading:** Pure density 7.85 g/cm³, area 20 cm², 168 h; consistent cleaned mass loss; general corrosion only. Calculate independently before generalizing. Any service claim requires evidence that the model assumptions remain valid under the intended operating conditions.

### Investigation: evidence quality, sampling and controls

For **Fractography, root cause and evidence grading**, document **independent tests with instrument and specimen controls**, with **measurement reference, sample cleaning, repeat lot, raw signals, data treatment and response thresholds**. Challenge the primary conclusion using **field specimens, parallel methods and blind review of the damage map**. Keep independently sampled specimens distinct from repeat readings on the same material, and match environmental histories across treatment groups.

### Diagnostic warning and alternative outcome

Post-failure oxidation can be mistaken for the initiating cause if sequence is not reconstructed.

### Assessment: three substantive exercises

**Exercise 1 — mechanism and dimensional reasoning.** Derive or explain the relation `Inference confidence increases when independent predicted observations converge; no universal scalar root-cause equation exists.` using its physical assumptions. Assign units to the terms that are actually quantitative; for a qualitative relation, replace it with a measurable definition. Distinguish what can be calculated from a textbook constant from what would require a service-specific measurement. *Answer guidance:* every conversion must declare the material, reacting species, coordinate or control volume and environmental state; reject interpretations whose quantities are at incompatible scales.

**Exercise 2 — independent numerical verification.** Recalculate the synthetic pair (69, 0.22916288) and (144, 0.47825296) with proper units, then choose a small change near the first point and estimate sensitivity. Discuss how input uncertainty and a violation of **gravimetric corrosion-rate conversion** assumptions would affect a claimed engineering conclusion. *Answer guidance:* calculate from the declared ideal expression, preserve units, and do not convert a formula-generated result into fictional laboratory evidence.

**Exercise 3 — disconfirming experiment.** For the case “A failed shaft contains both rust and fatigue-like striations. Determine whether rust caused initiation or invaded a crack after failure.” specify a target measurement, a matched control, at least three distinct physical specimens when meaningful, an uncertainty source and a criterion that would reject the proposed cause. *Answer guidance:* distinguish damage depth from area-averaged loss, distinguish reaction-driving force from rate, and make sure the independent test is not based on the same unverified assumption.

### Decision exercise and transferable principle

Compare protected fracture surfaces, crack origins, operating loads and unfailed sister components. Write a short decision memo: what is observed; what is inferred; what has not been measured; what alternative still fits; and which further evidence would justify action. Do not mistake a source with scientific-looking units for a calibrated material result. The goal is not to name as many corrosion forms as possible, but to explain precisely how a physical mechanism could produce the observed failure and how another mechanism could be ruled out.

## Unit 7 capstone — evidence and engineering defense

**Complex case:** An accelerated test ranks two candidate materials opposite to their field history. Design an evidence audit, sampling program, and cautious decision.

1. **System definition for Corrosion testing, monitoring and failure analysis:** Sketch the material, phase boundaries, electrolyte or gas paths, stressed features, wet–dry or thermal cycles and measurement locations. State precisely whether the main concern is uniform thinning, maximum pit depth, a crack, surface-electrical function or loss of protective scale.
2. **Two competing mechanisms:** Construct a table with initiating cause, expected spatial pattern, predicted time dependence, contrary evidence and an orthogonal method. Identify which mechanism might operate after rather than before the observed damage.
3. **Numerical audit:** Recalculate both of this unit's models at their default inputs and at the limits of the slider range. Describe the units and whether the model concerns driving force, rate, geometry, or inspection uncertainty. Show at least one reason the model might not apply to the given case.
4. **Sampling and uncertainty:** Build a hierarchy of independent assets or coupons, repeated measurements and local map points. Include instrument calibration, specimen differences, exposure mismatch and the possibility that a rare maximum is missed by ordinary sampling.
5. **Decision note:** Produce a 400-word recommendation with immediate safety implications separated from follow-up research, a repair or monitor option, a cost of wrong inference, and the exact evidence that would change the ranking. Do not claim service life from synthetic data.

### Connecting this unit to materials engineering

A corrosion investigation improves when it preserves the distinction between an electrochemical mechanism, the spatial manifestation of damage, an instrument response and a decision on whether equipment remains fit for service. In **corrosion testing, monitoring and failure analysis**, a defensible conclusion follows a chain of falsifiable physical claims rather than a single parameter selected because it is easy to compute. The mathematics should expose sensitivity and uncertainty, while site observations determine whether the equations apply at all. The companion models are an instructional starting point; professional asset decisions need controlled tests, standards and real-world verification.
