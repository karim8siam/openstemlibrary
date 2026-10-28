# Unit 05: Cooling Systems, Water and Environmental Constraints

**Course Code**: PPE 305 · **Level**: Advanced Undergraduate Engineering

## Unit Overview & Physical Foundations

This comprehensive university textbook unit covers the theoretical framework, physical modeling, mathematical governing equations, and engineering applications of **Cooling Systems, Water and Environmental Constraints**.

# Unit 05, Lesson 01 — Condenser heat-rejection accounting

**Core topic:** water-side calorimetry. **Representative relation:** `Q_reject = m_dot_cw*cp*DeltaT`. **Case context:** condenser cooling-water loop.

The central question in this lesson is how to evaluate **water-side calorimetry** when the engineer is given measurements from **condenser cooling-water loop**. First decide what quantity the result is supposed to describe. A thermodynamic component may have a local performance metric, while the whole plant has different inputs, outputs, auxiliaries and losses. Naming the metric prevents an apparently precise equation from addressing the wrong question. The representative relation is `Q_reject = m_dot_cw*cp*DeltaT`. This expression is a teaching starting point, not a complete design specification. Before putting values into it, define every term, identify the device boundary, and write its units. Where a symbol can have multiple interpretations, the label on the measurement sheet must be explicit.

### 1. Physical interpretation and scope

The phenomenon in focus is **water-side calorimetry**. In a river-adjacent station comparing once-through cooling, recirculating towers and a dry condenser, a measured value will depend on the actual arrangement of equipment, the time interval over which it is averaged and the physical states entering each component. If an engineer isolates condenser cooling-water loop, the analysis should start by drawing arrows for all relevant energy or material streams and recording their directions. The next question is which measurements are direct and which come from a calculated property, manufacturer map, inferred coefficient or operational assumption. This distinction is more consequential than the number of decimal places in a spreadsheet.

A conservation equation and a constitutive relation serve different roles. Conservation says what the flows must sum to; a heat-transfer coefficient, turbomachinery efficiency, combustion model or empirical performance map helps explain how the flows divide in a specific design. When the calculation requires an unmeasured coefficient, report an explicit assumed range rather than disguising it as an observed constant. A reliable answer reports the sign of work and heat, the unit system and why a steady-state approximation is reasonable—or why it may be inadequate.

### 2. Derivation and use of the central relation

Begin with `Q_reject = m_dot_cw*cp*DeltaT` and identify the physical quantity on each side. A useful calculation is dimensionally self-consistent: for example MW equals MJ/s, mass flow in kg/s times a specific energy in kJ/kg produces kW, and the ratio of energies or rates is dimensionless only when numerator and denominator use comparable bases. Temperatures added in a balance can be Celsius differences; temperatures divided in ideal-gas or second-law relations must use kelvin. Pressure ratios use absolute pressure; a gauge-pressure reading must be converted before use in a physical ratio.

For water-side calorimetry, specify whether the result assumes constant properties, negligible kinetic-energy changes, no stored-energy rate, or a fixed device efficiency. Each of these is an engineering hypothesis that can be tested or relaxed. When working from field data, reduce readings in the order: raw instrument value, calibrated engineering unit, time alignment, derived state quantity, physical balance, performance ratio. This audit trail allows a second engineer to repeat the estimate.

A special caution in this lesson is that **temperature sensors and large flows require uncertainty evaluation**. Explain exactly which algebraic term or measurement would be affected by that mistake. For a model with several serial components, a plausible local estimate may still be incompatible with the surrounding plant energy balance. Reconcile the result against the larger system. A model that demands more energy at the outlet than enters without storage, external work or a defined additional source should be rejected rather than patched by an unexplained correction factor.

### 3. Applied worked example — Condenser heat-rejection accounting

A cooling-water loop carries 2600 kg/s with assumed cp = 4.18 kJ/(kg K) and temperature rise 7 K. Heat duty is 2600 × 4.18 × 7 = **76,076 kW**, or 76.076 MW(th). A 0.2 K sensor offset would change the inferred duty by about 2.17 MW, so calibration matters.

**Verification and limitations.** This single-phase sensible estimate does not include independent condenser steam-side validation. The result is illustrative and does not replace equipment-specific property data, measurements or professional review.

### 7. Exercises and discussion

1. **Derive.** Start from an explicit control volume for condenser cooling-water loop. Derive `Q_reject = m_dot_cw*cp*DeltaT` or identify its idealizing assumptions. Label every term and check dimensional homogeneity.
2. **Calculate.** Construct an internally consistent SI example for water-side calorimetry using values from a standard property table or clearly declared synthetic inputs. Calculate the nominal result and an output range when the dominant uncertain input is perturbed by ±5%.
3. **Diagnose.** A team reports an unexpected improvement while its fuel, electricity or fluid meters are undergoing maintenance. Form two measurement-error hypotheses and one physical-process hypothesis, then identify evidence that would discriminate among them.
4. **Compare.** Evaluate whether a small temperature offset becomes a large apparent duty error at high flow. Discuss at least one benefit, one new risk and a plant-level quantity that may offset the local benefit.
5. **Communicate.** Write a one-page engineering note distinguishing your numerical result, its assumptions, the source of each input, and the actions that require external professional review.

**Answer-check guidance.** A defensible solution shows its boundary, substitutions and units, not just the final numerical value. For a ±5% sensitivity, recompute the original equation at both input limits rather than automatically declaring the output to have the same percentage uncertainty. For evidence questions, name the actual sensor or log to examine and the expected sign of each competing effect. Qualitative trade-offs need a stated criterion—net export, fuel use, water, safety margin or total cost—rather than a vague ranking.

### 8. Research extension

Design a small, reproducible computational experiment about water-side calorimetry. Define a physically reasonable input range and record why the range was chosen; collect a baseline output; sweep one independent variable; and export the results with units and assumptions. Explain where the educational calculator in this book is too simple for the proposed study. Contrast its output with published technology characterizations or a documented manufacturer's map *without copying proprietary material*. Include a limitations paragraph on extrapolation, scale effects and evidence quality. A negative finding, such as failure to improve net plant performance despite an attractive component calculation, is a valid outcome when the assumptions are clear.


---

# Unit 05, Lesson 02 — Cooling towers and ambient boundaries

**Core topic:** approach, range and wet-bulb influence. **Representative relation:** `Range = T_hot-T_cold`. **Case context:** forced-draft evaporative cooling tower.

The central question in this lesson is how to evaluate **approach, range and wet-bulb influence** when the engineer is given measurements from **forced-draft evaporative cooling tower**. First decide what quantity the result is supposed to describe. A thermodynamic component may have a local performance metric, while the whole plant has different inputs, outputs, auxiliaries and losses. Naming the metric prevents an apparently precise equation from addressing the wrong question. The representative relation is `Range = T_hot-T_cold`. This expression is a teaching starting point, not a complete design specification. Before putting values into it, define every term, identify the device boundary, and write its units. Where a symbol can have multiple interpretations, the label on the measurement sheet must be explicit.

### 1. Physical interpretation and scope

The phenomenon in focus is **approach, range and wet-bulb influence**. In a river-adjacent station comparing once-through cooling, recirculating towers and a dry condenser, a measured value will depend on the actual arrangement of equipment, the time interval over which it is averaged and the physical states entering each component. If an engineer isolates forced-draft evaporative cooling tower, the analysis should start by drawing arrows for all relevant energy or material streams and recording their directions. The next question is which measurements are direct and which come from a calculated property, manufacturer map, inferred coefficient or operational assumption. This distinction is more consequential than the number of decimal places in a spreadsheet.

A conservation equation and a constitutive relation serve different roles. Conservation says what the flows must sum to; a heat-transfer coefficient, turbomachinery efficiency, combustion model or empirical performance map helps explain how the flows divide in a specific design. When the calculation requires an unmeasured coefficient, report an explicit assumed range rather than disguising it as an observed constant. A reliable answer reports the sign of work and heat, the unit system and why a steady-state approximation is reasonable—or why it may be inadequate.

### 2. Derivation and use of the central relation

Begin with `Range = T_hot-T_cold` and identify the physical quantity on each side. A useful calculation is dimensionally self-consistent: for example MW equals MJ/s, mass flow in kg/s times a specific energy in kJ/kg produces kW, and the ratio of energies or rates is dimensionless only when numerator and denominator use comparable bases. Temperatures added in a balance can be Celsius differences; temperatures divided in ideal-gas or second-law relations must use kelvin. Pressure ratios use absolute pressure; a gauge-pressure reading must be converted before use in a physical ratio.

For approach, range and wet-bulb influence, specify whether the result assumes constant properties, negligible kinetic-energy changes, no stored-energy rate, or a fixed device efficiency. Each of these is an engineering hypothesis that can be tested or relaxed. When working from field data, reduce readings in the order: raw instrument value, calibrated engineering unit, time alignment, derived state quantity, physical balance, performance ratio. This audit trail allows a second engineer to repeat the estimate.

A special caution in this lesson is that **air wet-bulb temperature bounds feasible evaporative cooling**. Explain exactly which algebraic term or measurement would be affected by that mistake. For a model with several serial components, a plausible local estimate may still be incompatible with the surrounding plant energy balance. Reconcile the result against the larger system. A model that demands more energy at the outlet than enters without storage, external work or a defined additional source should be rejected rather than patched by an unexplained correction factor.

### 3. Applied worked example — Cooling towers and ambient boundaries

A cooling tower returns water at 29 °C after receiving hot water at 36 °C. Cooling range is **7 K**. If ambient wet-bulb temperature is 25 °C, the cold-water approach is **4 K**. Neither number alone specifies evaporation, electrical fan demand or biological treatment requirements.

**Verification and limitations.** Cooling-tower performance changes with humidity, air flow and water chemistry. The result is illustrative and does not replace equipment-specific property data, measurements or professional review.

### 7. Exercises and discussion

1. **Derive.** Start from an explicit control volume for forced-draft evaporative cooling tower. Derive `Range = T_hot-T_cold` or identify its idealizing assumptions. Label every term and check dimensional homogeneity.
2. **Calculate.** Construct an internally consistent SI example for approach, range and wet-bulb influence using values from a standard property table or clearly declared synthetic inputs. Calculate the nominal result and an output range when the dominant uncertain input is perturbed by ±5%.
3. **Diagnose.** A team reports an unexpected improvement while its fuel, electricity or fluid meters are undergoing maintenance. Form two measurement-error hypotheses and one physical-process hypothesis, then identify evidence that would discriminate among them.
4. **Compare.** Evaluate whether raising cooling duty increases evaporation and treatment demand. Discuss at least one benefit, one new risk and a plant-level quantity that may offset the local benefit.
5. **Communicate.** Write a one-page engineering note distinguishing your numerical result, its assumptions, the source of each input, and the actions that require external professional review.

**Answer-check guidance.** A defensible solution shows its boundary, substitutions and units, not just the final numerical value. For a ±5% sensitivity, recompute the original equation at both input limits rather than automatically declaring the output to have the same percentage uncertainty. For evidence questions, name the actual sensor or log to examine and the expected sign of each competing effect. Qualitative trade-offs need a stated criterion—net export, fuel use, water, safety margin or total cost—rather than a vague ranking.

### 8. Research extension

Design a small, reproducible computational experiment about approach, range and wet-bulb influence. Define a physically reasonable input range and record why the range was chosen; collect a baseline output; sweep one independent variable; and export the results with units and assumptions. Explain where the educational calculator in this book is too simple for the proposed study. Contrast its output with published technology characterizations or a documented manufacturer's map *without copying proprietary material*. Include a limitations paragraph on extrapolation, scale effects and evidence quality. A negative finding, such as failure to improve net plant performance despite an attractive component calculation, is a valid outcome when the assumptions are clear.


---

# Unit 05, Lesson 03 — Water consumption and blowdown

**Core topic:** cycles of concentration and water budgets. **Representative relation:** `COC = C_circulating/C_makeup`. **Case context:** cooling tower makeup, drift and blowdown records.

The central question in this lesson is how to evaluate **cycles of concentration and water budgets** when the engineer is given measurements from **cooling tower makeup, drift and blowdown records**. First decide what quantity the result is supposed to describe. A thermodynamic component may have a local performance metric, while the whole plant has different inputs, outputs, auxiliaries and losses. Naming the metric prevents an apparently precise equation from addressing the wrong question. The representative relation is `COC = C_circulating/C_makeup`. This expression is a teaching starting point, not a complete design specification. Before putting values into it, define every term, identify the device boundary, and write its units. Where a symbol can have multiple interpretations, the label on the measurement sheet must be explicit.

### 1. Physical interpretation and scope

The phenomenon in focus is **cycles of concentration and water budgets**. In a river-adjacent station comparing once-through cooling, recirculating towers and a dry condenser, a measured value will depend on the actual arrangement of equipment, the time interval over which it is averaged and the physical states entering each component. If an engineer isolates cooling tower makeup, drift and blowdown records, the analysis should start by drawing arrows for all relevant energy or material streams and recording their directions. The next question is which measurements are direct and which come from a calculated property, manufacturer map, inferred coefficient or operational assumption. This distinction is more consequential than the number of decimal places in a spreadsheet.

A conservation equation and a constitutive relation serve different roles. Conservation says what the flows must sum to; a heat-transfer coefficient, turbomachinery efficiency, combustion model or empirical performance map helps explain how the flows divide in a specific design. When the calculation requires an unmeasured coefficient, report an explicit assumed range rather than disguising it as an observed constant. A reliable answer reports the sign of work and heat, the unit system and why a steady-state approximation is reasonable—or why it may be inadequate.

### 2. Derivation and use of the central relation

Begin with `COC = C_circulating/C_makeup` and identify the physical quantity on each side. A useful calculation is dimensionally self-consistent: for example MW equals MJ/s, mass flow in kg/s times a specific energy in kJ/kg produces kW, and the ratio of energies or rates is dimensionless only when numerator and denominator use comparable bases. Temperatures added in a balance can be Celsius differences; temperatures divided in ideal-gas or second-law relations must use kelvin. Pressure ratios use absolute pressure; a gauge-pressure reading must be converted before use in a physical ratio.

For cycles of concentration and water budgets, specify whether the result assumes constant properties, negligible kinetic-energy changes, no stored-energy rate, or a fixed device efficiency. Each of these is an engineering hypothesis that can be tested or relaxed. When working from field data, reduce readings in the order: raw instrument value, calibrated engineering unit, time alignment, derived state quantity, physical balance, performance ratio. This audit trail allows a second engineer to repeat the estimate.

A special caution in this lesson is that **water chemistry cannot be characterized by one scalar alone**. Explain exactly which algebraic term or measurement would be affected by that mistake. For a model with several serial components, a plausible local estimate may still be incompatible with the surrounding plant energy balance. Reconcile the result against the larger system. A model that demands more energy at the outlet than enters without storage, external work or a defined additional source should be rejected rather than patched by an unexplained correction factor.

### 3. Applied worked example — Water consumption and blowdown

A concentration proxy is 1800 mg/L circulating-water dissolved solids divided by 300 mg/L makeup-water solids, giving **6 cycles of concentration**. This simplified ratio assumes consistent species behavior and mixing; chemical reaction and selective precipitation break the scalar approximation.

**Verification and limitations.** A plant water budget also requires evaporation, blowdown, drift and leak measurements. The result is illustrative and does not replace equipment-specific property data, measurements or professional review.

### 7. Exercises and discussion

1. **Derive.** Start from an explicit control volume for cooling tower makeup, drift and blowdown records. Derive `COC = C_circulating/C_makeup` or identify its idealizing assumptions. Label every term and check dimensional homogeneity.
2. **Calculate.** Construct an internally consistent SI example for cycles of concentration and water budgets using values from a standard property table or clearly declared synthetic inputs. Calculate the nominal result and an output range when the dominant uncertain input is perturbed by ±5%.
3. **Diagnose.** A team reports an unexpected improvement while its fuel, electricity or fluid meters are undergoing maintenance. Form two measurement-error hypotheses and one physical-process hypothesis, then identify evidence that would discriminate among them.
4. **Compare.** Evaluate whether scaling risk rises if dissolved solids exceed controlled treatment ranges. Discuss at least one benefit, one new risk and a plant-level quantity that may offset the local benefit.
5. **Communicate.** Write a one-page engineering note distinguishing your numerical result, its assumptions, the source of each input, and the actions that require external professional review.

**Answer-check guidance.** A defensible solution shows its boundary, substitutions and units, not just the final numerical value. For a ±5% sensitivity, recompute the original equation at both input limits rather than automatically declaring the output to have the same percentage uncertainty. For evidence questions, name the actual sensor or log to examine and the expected sign of each competing effect. Qualitative trade-offs need a stated criterion—net export, fuel use, water, safety margin or total cost—rather than a vague ranking.

### 8. Research extension

Design a small, reproducible computational experiment about cycles of concentration and water budgets. Define a physically reasonable input range and record why the range was chosen; collect a baseline output; sweep one independent variable; and export the results with units and assumptions. Explain where the educational calculator in this book is too simple for the proposed study. Contrast its output with published technology characterizations or a documented manufacturer's map *without copying proprietary material*. Include a limitations paragraph on extrapolation, scale effects and evidence quality. A negative finding, such as failure to improve net plant performance despite an attractive component calculation, is a valid outcome when the assumptions are clear.


---

# Unit 05, Lesson 04 — Dry and hybrid cooling

**Core topic:** heat-exchanger effectiveness and climate effects. **Representative relation:** `Q = UA*LMTD`. **Case context:** air-cooled condenser under hot weather.

The central question in this lesson is how to evaluate **heat-exchanger effectiveness and climate effects** when the engineer is given measurements from **air-cooled condenser under hot weather**. First decide what quantity the result is supposed to describe. A thermodynamic component may have a local performance metric, while the whole plant has different inputs, outputs, auxiliaries and losses. Naming the metric prevents an apparently precise equation from addressing the wrong question. The representative relation is `Q = UA*LMTD`. This expression is a teaching starting point, not a complete design specification. Before putting values into it, define every term, identify the device boundary, and write its units. Where a symbol can have multiple interpretations, the label on the measurement sheet must be explicit.

### 1. Physical interpretation and scope

The phenomenon in focus is **heat-exchanger effectiveness and climate effects**. In a river-adjacent station comparing once-through cooling, recirculating towers and a dry condenser, a measured value will depend on the actual arrangement of equipment, the time interval over which it is averaged and the physical states entering each component. If an engineer isolates air-cooled condenser under hot weather, the analysis should start by drawing arrows for all relevant energy or material streams and recording their directions. The next question is which measurements are direct and which come from a calculated property, manufacturer map, inferred coefficient or operational assumption. This distinction is more consequential than the number of decimal places in a spreadsheet.

A conservation equation and a constitutive relation serve different roles. Conservation says what the flows must sum to; a heat-transfer coefficient, turbomachinery efficiency, combustion model or empirical performance map helps explain how the flows divide in a specific design. When the calculation requires an unmeasured coefficient, report an explicit assumed range rather than disguising it as an observed constant. A reliable answer reports the sign of work and heat, the unit system and why a steady-state approximation is reasonable—or why it may be inadequate.

### 2. Derivation and use of the central relation

Begin with `Q = UA*LMTD` and identify the physical quantity on each side. A useful calculation is dimensionally self-consistent: for example MW equals MJ/s, mass flow in kg/s times a specific energy in kJ/kg produces kW, and the ratio of energies or rates is dimensionless only when numerator and denominator use comparable bases. Temperatures added in a balance can be Celsius differences; temperatures divided in ideal-gas or second-law relations must use kelvin. Pressure ratios use absolute pressure; a gauge-pressure reading must be converted before use in a physical ratio.

For heat-exchanger effectiveness and climate effects, specify whether the result assumes constant properties, negligible kinetic-energy changes, no stored-energy rate, or a fixed device efficiency. Each of these is an engineering hypothesis that can be tested or relaxed. When working from field data, reduce readings in the order: raw instrument value, calibrated engineering unit, time alignment, derived state quantity, physical balance, performance ratio. This audit trail allows a second engineer to repeat the estimate.

A special caution in this lesson is that **pinch and finite air temperature differences govern design**. Explain exactly which algebraic term or measurement would be affected by that mistake. For a model with several serial components, a plausible local estimate may still be incompatible with the surrounding plant energy balance. Reconcile the result against the larger system. A model that demands more energy at the outlet than enters without storage, external work or a defined additional source should be rejected rather than patched by an unexplained correction factor.

### 3. Applied worked example — Dry and hybrid cooling

A simplified air-cooled exchanger has UA = 250 kW/K and a log-mean temperature difference of 16 K. Its idealized rate is **4.0 MW(th)**. Real UA varies with fouling, air velocity, fin condition and operating temperature, so a hot-day prediction requires actual equipment data.

**Verification and limitations.** An assumed fixed temperature approach can conceal a high-temperature derating risk. The result is illustrative and does not replace equipment-specific property data, measurements or professional review.

### 7. Exercises and discussion

1. **Derive.** Start from an explicit control volume for air-cooled condenser under hot weather. Derive `Q = UA*LMTD` or identify its idealizing assumptions. Label every term and check dimensional homogeneity.
2. **Calculate.** Construct an internally consistent SI example for heat-exchanger effectiveness and climate effects using values from a standard property table or clearly declared synthetic inputs. Calculate the nominal result and an output range when the dominant uncertain input is perturbed by ±5%.
3. **Diagnose.** A team reports an unexpected improvement while its fuel, electricity or fluid meters are undergoing maintenance. Form two measurement-error hypotheses and one physical-process hypothesis, then identify evidence that would discriminate among them.
4. **Compare.** Evaluate whether water savings may entail lower summer generation and higher fan electricity. Discuss at least one benefit, one new risk and a plant-level quantity that may offset the local benefit.
5. **Communicate.** Write a one-page engineering note distinguishing your numerical result, its assumptions, the source of each input, and the actions that require external professional review.

**Answer-check guidance.** A defensible solution shows its boundary, substitutions and units, not just the final numerical value. For a ±5% sensitivity, recompute the original equation at both input limits rather than automatically declaring the output to have the same percentage uncertainty. For evidence questions, name the actual sensor or log to examine and the expected sign of each competing effect. Qualitative trade-offs need a stated criterion—net export, fuel use, water, safety margin or total cost—rather than a vague ranking.

### 8. Research extension

Design a small, reproducible computational experiment about heat-exchanger effectiveness and climate effects. Define a physically reasonable input range and record why the range was chosen; collect a baseline output; sweep one independent variable; and export the results with units and assumptions. Explain where the educational calculator in this book is too simple for the proposed study. Contrast its output with published technology characterizations or a documented manufacturer's map *without copying proprietary material*. Include a limitations paragraph on extrapolation, scale effects and evidence quality. A negative finding, such as failure to improve net plant performance despite an attractive component calculation, is a valid outcome when the assumptions are clear.


---

# Unit 05, Lesson 05 — Environmental evaluation and monitoring

**Core topic:** resource intensity across a reporting boundary. **Representative relation:** `I_water = V_consumed/E_net`. **Case context:** monthly plant water balance.

The central question in this lesson is how to evaluate **resource intensity across a reporting boundary** when the engineer is given measurements from **monthly plant water balance**. First decide what quantity the result is supposed to describe. A thermodynamic component may have a local performance metric, while the whole plant has different inputs, outputs, auxiliaries and losses. Naming the metric prevents an apparently precise equation from addressing the wrong question. The representative relation is `I_water = V_consumed/E_net`. This expression is a teaching starting point, not a complete design specification. Before putting values into it, define every term, identify the device boundary, and write its units. Where a symbol can have multiple interpretations, the label on the measurement sheet must be explicit.

### 1. Physical interpretation and scope

The phenomenon in focus is **resource intensity across a reporting boundary**. In a river-adjacent station comparing once-through cooling, recirculating towers and a dry condenser, a measured value will depend on the actual arrangement of equipment, the time interval over which it is averaged and the physical states entering each component. If an engineer isolates monthly plant water balance, the analysis should start by drawing arrows for all relevant energy or material streams and recording their directions. The next question is which measurements are direct and which come from a calculated property, manufacturer map, inferred coefficient or operational assumption. This distinction is more consequential than the number of decimal places in a spreadsheet.

A conservation equation and a constitutive relation serve different roles. Conservation says what the flows must sum to; a heat-transfer coefficient, turbomachinery efficiency, combustion model or empirical performance map helps explain how the flows divide in a specific design. When the calculation requires an unmeasured coefficient, report an explicit assumed range rather than disguising it as an observed constant. A reliable answer reports the sign of work and heat, the unit system and why a steady-state approximation is reasonable—or why it may be inadequate.

### 2. Derivation and use of the central relation

Begin with `I_water = V_consumed/E_net` and identify the physical quantity on each side. A useful calculation is dimensionally self-consistent: for example MW equals MJ/s, mass flow in kg/s times a specific energy in kJ/kg produces kW, and the ratio of energies or rates is dimensionless only when numerator and denominator use comparable bases. Temperatures added in a balance can be Celsius differences; temperatures divided in ideal-gas or second-law relations must use kelvin. Pressure ratios use absolute pressure; a gauge-pressure reading must be converted before use in a physical ratio.

For resource intensity across a reporting boundary, specify whether the result assumes constant properties, negligible kinetic-energy changes, no stored-energy rate, or a fixed device efficiency. Each of these is an engineering hypothesis that can be tested or relaxed. When working from field data, reduce readings in the order: raw instrument value, calibrated engineering unit, time alignment, derived state quantity, physical balance, performance ratio. This audit trail allows a second engineer to repeat the estimate.

A special caution in this lesson is that **withdrawals and consumption are different quantities**. Explain exactly which algebraic term or measurement would be affected by that mistake. For a model with several serial components, a plausible local estimate may still be incompatible with the surrounding plant energy balance. Reconcile the result against the larger system. A model that demands more energy at the outlet than enters without storage, external work or a defined additional source should be rejected rather than patched by an unexplained correction factor.

### 3. Applied worked example — Environmental evaluation and monitoring

A plant consumes 500,000 m³ of water while exporting 700,000 MWh(e) over the same annual period. Consumptive intensity is 500,000/700,000 = **0.714 m³/MWh**. Withdrawal volume could be much larger; report the two separately and document where water is returned.

**Verification and limitations.** This accounting value is not a license to withdraw water or discharge heated effluent. The result is illustrative and does not replace equipment-specific property data, measurements or professional review.

### 7. Exercises and discussion

1. **Derive.** Start from an explicit control volume for monthly plant water balance. Derive `I_water = V_consumed/E_net` or identify its idealizing assumptions. Label every term and check dimensional homogeneity.
2. **Calculate.** Construct an internally consistent SI example for resource intensity across a reporting boundary using values from a standard property table or clearly declared synthetic inputs. Calculate the nominal result and an output range when the dominant uncertain input is perturbed by ±5%.
3. **Diagnose.** A team reports an unexpected improvement while its fuel, electricity or fluid meters are undergoing maintenance. Form two measurement-error hypotheses and one physical-process hypothesis, then identify evidence that would discriminate among them.
4. **Compare.** Evaluate whether less withdrawal may not imply less total environmental impact. Discuss at least one benefit, one new risk and a plant-level quantity that may offset the local benefit.
5. **Communicate.** Write a one-page engineering note distinguishing your numerical result, its assumptions, the source of each input, and the actions that require external professional review.

**Answer-check guidance.** A defensible solution shows its boundary, substitutions and units, not just the final numerical value. For a ±5% sensitivity, recompute the original equation at both input limits rather than automatically declaring the output to have the same percentage uncertainty. For evidence questions, name the actual sensor or log to examine and the expected sign of each competing effect. Qualitative trade-offs need a stated criterion—net export, fuel use, water, safety margin or total cost—rather than a vague ranking.

### 8. Research extension

Design a small, reproducible computational experiment about resource intensity across a reporting boundary. Define a physically reasonable input range and record why the range was chosen; collect a baseline output; sweep one independent variable; and export the results with units and assumptions. Explain where the educational calculator in this book is too simple for the proposed study. Contrast its output with published technology characterizations or a documented manufacturer's map *without copying proprietary material*. Include a limitations paragraph on extrapolation, scale effects and evidence quality. A negative finding, such as failure to improve net plant performance despite an attractive component calculation, is a valid outcome when the assumptions are clear.


---

