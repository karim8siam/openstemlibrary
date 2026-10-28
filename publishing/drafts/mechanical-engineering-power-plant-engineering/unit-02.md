# Unit 02: Steam-Cycle Power Generation

**Course Code**: PPE 302 · **Level**: Advanced Undergraduate Engineering

## Unit Overview & Physical Foundations

This comprehensive university textbook unit covers the theoretical framework, physical modeling, mathematical governing equations, and engineering applications of **Steam-Cycle Power Generation**.

# Unit 02, Lesson 01 — Rankine states and thermal conversion

**Core topic:** net cycle work and heat input. **Representative relation:** `eta_R = (w_t - w_p) / q_in`. **Case context:** four-state saturated cycle.

The central question in this lesson is how to evaluate **net cycle work and heat input** when the engineer is given measurements from **four-state saturated cycle**. First decide what quantity the result is supposed to describe. A thermodynamic component may have a local performance metric, while the whole plant has different inputs, outputs, auxiliaries and losses. Naming the metric prevents an apparently precise equation from addressing the wrong question. The representative relation is `eta_R = (w_t - w_p) / q_in`. This expression is a teaching starting point, not a complete design specification. Before putting values into it, define every term, identify the device boundary, and write its units. Where a symbol can have multiple interpretations, the label on the measurement sheet must be explicit.

### 1. Physical interpretation and scope

The phenomenon in focus is **net cycle work and heat input**. In a steam station with a boiler, high-pressure turbine, reheat section, condenser and feedwater pumps, a measured value will depend on the actual arrangement of equipment, the time interval over which it is averaged and the physical states entering each component. If an engineer isolates four-state saturated cycle, the analysis should start by drawing arrows for all relevant energy or material streams and recording their directions. The next question is which measurements are direct and which come from a calculated property, manufacturer map, inferred coefficient or operational assumption. This distinction is more consequential than the number of decimal places in a spreadsheet.

A conservation equation and a constitutive relation serve different roles. Conservation says what the flows must sum to; a heat-transfer coefficient, turbomachinery efficiency, combustion model or empirical performance map helps explain how the flows divide in a specific design. When the calculation requires an unmeasured coefficient, report an explicit assumed range rather than disguising it as an observed constant. A reliable answer reports the sign of work and heat, the unit system and why a steady-state approximation is reasonable—or why it may be inadequate.

### 2. Derivation and use of the central relation

Begin with `eta_R = (w_t - w_p) / q_in` and identify the physical quantity on each side. A useful calculation is dimensionally self-consistent: for example MW equals MJ/s, mass flow in kg/s times a specific energy in kJ/kg produces kW, and the ratio of energies or rates is dimensionless only when numerator and denominator use comparable bases. Temperatures added in a balance can be Celsius differences; temperatures divided in ideal-gas or second-law relations must use kelvin. Pressure ratios use absolute pressure; a gauge-pressure reading must be converted before use in a physical ratio.

For net cycle work and heat input, specify whether the result assumes constant properties, negligible kinetic-energy changes, no stored-energy rate, or a fixed device efficiency. Each of these is an engineering hypothesis that can be tested or relaxed. When working from field data, reduce readings in the order: raw instrument value, calibrated engineering unit, time alignment, derived state quantity, physical balance, performance ratio. This audit trail allows a second engineer to repeat the estimate.

A special caution in this lesson is that **state enthalpies must come from a consistent property source**. Explain exactly which algebraic term or measurement would be affected by that mistake. For a model with several serial components, a plausible local estimate may still be incompatible with the surrounding plant energy balance. Reconcile the result against the larger system. A model that demands more energy at the outlet than enters without storage, external work or a defined additional source should be rejected rather than patched by an unexplained correction factor.

### 3. Applied worked example — Rankine states and thermal conversion

Take idealized cycle enthalpies of 192 kJ/kg at pump inlet, 202 after pumping, 3450 after the boiler, and 2300 at turbine exit. Turbine work is 1150 kJ/kg, pump work is 10 kJ/kg, and heat supplied is 3248 kJ/kg; ideal thermal efficiency is (1150 − 10)/3248 = **35.10%**. These are a synthetic set of enthalpies, not a verified steam-table operating point.

**Verification and limitations.** Detailed state selection must satisfy actual pressure and entropy constraints; arbitrary enthalpies cannot validate a real cycle. The result is illustrative and does not replace equipment-specific property data, measurements or professional review.

### 7. Exercises and discussion

1. **Derive.** Start from an explicit control volume for four-state saturated cycle. Derive `eta_R = (w_t - w_p) / q_in` or identify its idealizing assumptions. Label every term and check dimensional homogeneity.
2. **Calculate.** Construct an internally consistent SI example for net cycle work and heat input using values from a standard property table or clearly declared synthetic inputs. Calculate the nominal result and an output range when the dominant uncertain input is perturbed by ±5%.
3. **Diagnose.** A team reports an unexpected improvement while its fuel, electricity or fluid meters are undergoing maintenance. Form two measurement-error hypotheses and one physical-process hypothesis, then identify evidence that would discriminate among them.
4. **Compare.** Evaluate whether thermal efficiency is not the same as second-law efficiency. Discuss at least one benefit, one new risk and a plant-level quantity that may offset the local benefit.
5. **Communicate.** Write a one-page engineering note distinguishing your numerical result, its assumptions, the source of each input, and the actions that require external professional review.

**Answer-check guidance.** A defensible solution shows its boundary, substitutions and units, not just the final numerical value. For a ±5% sensitivity, recompute the original equation at both input limits rather than automatically declaring the output to have the same percentage uncertainty. For evidence questions, name the actual sensor or log to examine and the expected sign of each competing effect. Qualitative trade-offs need a stated criterion—net export, fuel use, water, safety margin or total cost—rather than a vague ranking.

### 8. Research extension

Design a small, reproducible computational experiment about net cycle work and heat input. Define a physically reasonable input range and record why the range was chosen; collect a baseline output; sweep one independent variable; and export the results with units and assumptions. Explain where the educational calculator in this book is too simple for the proposed study. Contrast its output with published technology characterizations or a documented manufacturer's map *without copying proprietary material*. Include a limitations paragraph on extrapolation, scale effects and evidence quality. A negative finding, such as failure to improve net plant performance despite an attractive component calculation, is a valid outcome when the assumptions are clear.


---

# Unit 02, Lesson 02 — Steam turbine expansion and extraction

**Core topic:** enthalpy work and internal efficiency. **Representative relation:** `W_t = m_dot*(h_in-h_out)`. **Case context:** high-pressure turbine with a bleed stream.

The central question in this lesson is how to evaluate **enthalpy work and internal efficiency** when the engineer is given measurements from **high-pressure turbine with a bleed stream**. First decide what quantity the result is supposed to describe. A thermodynamic component may have a local performance metric, while the whole plant has different inputs, outputs, auxiliaries and losses. Naming the metric prevents an apparently precise equation from addressing the wrong question. The representative relation is `W_t = m_dot*(h_in-h_out)`. This expression is a teaching starting point, not a complete design specification. Before putting values into it, define every term, identify the device boundary, and write its units. Where a symbol can have multiple interpretations, the label on the measurement sheet must be explicit.

### 1. Physical interpretation and scope

The phenomenon in focus is **enthalpy work and internal efficiency**. In a steam station with a boiler, high-pressure turbine, reheat section, condenser and feedwater pumps, a measured value will depend on the actual arrangement of equipment, the time interval over which it is averaged and the physical states entering each component. If an engineer isolates high-pressure turbine with a bleed stream, the analysis should start by drawing arrows for all relevant energy or material streams and recording their directions. The next question is which measurements are direct and which come from a calculated property, manufacturer map, inferred coefficient or operational assumption. This distinction is more consequential than the number of decimal places in a spreadsheet.

A conservation equation and a constitutive relation serve different roles. Conservation says what the flows must sum to; a heat-transfer coefficient, turbomachinery efficiency, combustion model or empirical performance map helps explain how the flows divide in a specific design. When the calculation requires an unmeasured coefficient, report an explicit assumed range rather than disguising it as an observed constant. A reliable answer reports the sign of work and heat, the unit system and why a steady-state approximation is reasonable—or why it may be inadequate.

### 2. Derivation and use of the central relation

Begin with `W_t = m_dot*(h_in-h_out)` and identify the physical quantity on each side. A useful calculation is dimensionally self-consistent: for example MW equals MJ/s, mass flow in kg/s times a specific energy in kJ/kg produces kW, and the ratio of energies or rates is dimensionless only when numerator and denominator use comparable bases. Temperatures added in a balance can be Celsius differences; temperatures divided in ideal-gas or second-law relations must use kelvin. Pressure ratios use absolute pressure; a gauge-pressure reading must be converted before use in a physical ratio.

For enthalpy work and internal efficiency, specify whether the result assumes constant properties, negligible kinetic-energy changes, no stored-energy rate, or a fixed device efficiency. Each of these is an engineering hypothesis that can be tested or relaxed. When working from field data, reduce readings in the order: raw instrument value, calibrated engineering unit, time alignment, derived state quantity, physical balance, performance ratio. This audit trail allows a second engineer to repeat the estimate.

A special caution in this lesson is that **use mass-weighted balances across extraction branches**. Explain exactly which algebraic term or measurement would be affected by that mistake. For a model with several serial components, a plausible local estimate may still be incompatible with the surrounding plant energy balance. Reconcile the result against the larger system. A model that demands more energy at the outlet than enters without storage, external work or a defined additional source should be rejected rather than patched by an unexplained correction factor.

### 3. Applied worked example — Steam turbine expansion and extraction

With steam flow of 30 kg/s and inlet/outlet enthalpies 3410 and 2550 kJ/kg, an ideal steady turbine power estimate is 30(3410 − 2550) = **25,800 kW**, or 25.8 MW. A real extraction turbine must apply this balance separately to every branch rather than using the full inlet flow across all stages.

**Verification and limitations.** The estimate excludes mechanical losses, leakage and the small kinetic-energy terms until their significance is checked. The result is illustrative and does not replace equipment-specific property data, measurements or professional review.

### 7. Exercises and discussion

1. **Derive.** Start from an explicit control volume for high-pressure turbine with a bleed stream. Derive `W_t = m_dot*(h_in-h_out)` or identify its idealizing assumptions. Label every term and check dimensional homogeneity.
2. **Calculate.** Construct an internally consistent SI example for enthalpy work and internal efficiency using values from a standard property table or clearly declared synthetic inputs. Calculate the nominal result and an output range when the dominant uncertain input is perturbed by ±5%.
3. **Diagnose.** A team reports an unexpected improvement while its fuel, electricity or fluid meters are undergoing maintenance. Form two measurement-error hypotheses and one physical-process hypothesis, then identify evidence that would discriminate among them.
4. **Compare.** Evaluate whether assuming inlet mass flow equals final exhaust mass flow overstates low-pressure work. Discuss at least one benefit, one new risk and a plant-level quantity that may offset the local benefit.
5. **Communicate.** Write a one-page engineering note distinguishing your numerical result, its assumptions, the source of each input, and the actions that require external professional review.

**Answer-check guidance.** A defensible solution shows its boundary, substitutions and units, not just the final numerical value. For a ±5% sensitivity, recompute the original equation at both input limits rather than automatically declaring the output to have the same percentage uncertainty. For evidence questions, name the actual sensor or log to examine and the expected sign of each competing effect. Qualitative trade-offs need a stated criterion—net export, fuel use, water, safety margin or total cost—rather than a vague ranking.

### 8. Research extension

Design a small, reproducible computational experiment about enthalpy work and internal efficiency. Define a physically reasonable input range and record why the range was chosen; collect a baseline output; sweep one independent variable; and export the results with units and assumptions. Explain where the educational calculator in this book is too simple for the proposed study. Contrast its output with published technology characterizations or a documented manufacturer's map *without copying proprietary material*. Include a limitations paragraph on extrapolation, scale effects and evidence quality. A negative finding, such as failure to improve net plant performance despite an attractive component calculation, is a valid outcome when the assumptions are clear.


---

# Unit 02, Lesson 03 — Condenser duty and backpressure

**Core topic:** heat rejection from wet exhaust. **Representative relation:** `Q_cond = m_dot*(h_in-h_out)`. **Case context:** surface condenser in a humid climate.

The central question in this lesson is how to evaluate **heat rejection from wet exhaust** when the engineer is given measurements from **surface condenser in a humid climate**. First decide what quantity the result is supposed to describe. A thermodynamic component may have a local performance metric, while the whole plant has different inputs, outputs, auxiliaries and losses. Naming the metric prevents an apparently precise equation from addressing the wrong question. The representative relation is `Q_cond = m_dot*(h_in-h_out)`. This expression is a teaching starting point, not a complete design specification. Before putting values into it, define every term, identify the device boundary, and write its units. Where a symbol can have multiple interpretations, the label on the measurement sheet must be explicit.

### 1. Physical interpretation and scope

The phenomenon in focus is **heat rejection from wet exhaust**. In a steam station with a boiler, high-pressure turbine, reheat section, condenser and feedwater pumps, a measured value will depend on the actual arrangement of equipment, the time interval over which it is averaged and the physical states entering each component. If an engineer isolates surface condenser in a humid climate, the analysis should start by drawing arrows for all relevant energy or material streams and recording their directions. The next question is which measurements are direct and which come from a calculated property, manufacturer map, inferred coefficient or operational assumption. This distinction is more consequential than the number of decimal places in a spreadsheet.

A conservation equation and a constitutive relation serve different roles. Conservation says what the flows must sum to; a heat-transfer coefficient, turbomachinery efficiency, combustion model or empirical performance map helps explain how the flows divide in a specific design. When the calculation requires an unmeasured coefficient, report an explicit assumed range rather than disguising it as an observed constant. A reliable answer reports the sign of work and heat, the unit system and why a steady-state approximation is reasonable—or why it may be inadequate.

### 2. Derivation and use of the central relation

Begin with `Q_cond = m_dot*(h_in-h_out)` and identify the physical quantity on each side. A useful calculation is dimensionally self-consistent: for example MW equals MJ/s, mass flow in kg/s times a specific energy in kJ/kg produces kW, and the ratio of energies or rates is dimensionless only when numerator and denominator use comparable bases. Temperatures added in a balance can be Celsius differences; temperatures divided in ideal-gas or second-law relations must use kelvin. Pressure ratios use absolute pressure; a gauge-pressure reading must be converted before use in a physical ratio.

For heat rejection from wet exhaust, specify whether the result assumes constant properties, negligible kinetic-energy changes, no stored-energy rate, or a fixed device efficiency. Each of these is an engineering hypothesis that can be tested or relaxed. When working from field data, reduce readings in the order: raw instrument value, calibrated engineering unit, time alignment, derived state quantity, physical balance, performance ratio. This audit trail allows a second engineer to repeat the estimate.

A special caution in this lesson is that **steam quality and noncondensable gases change performance**. Explain exactly which algebraic term or measurement would be affected by that mistake. For a model with several serial components, a plausible local estimate may still be incompatible with the surrounding plant energy balance. Reconcile the result against the larger system. A model that demands more energy at the outlet than enters without storage, external work or a defined additional source should be rejected rather than patched by an unexplained correction factor.

### 3. Applied worked example — Condenser duty and backpressure

A condenser receives 42 kg/s of wet exhaust at specific enthalpy 2400 kJ/kg and discharges condensate at 220 kJ/kg. Condenser thermal duty is 42(2400 − 220) = **91,560 kW**. This heat must reach a cooling medium, subject to nonzero temperature approach and finite transfer area.

**Verification and limitations.** A lower condensing temperature may improve ideal cycle output but can increase cooling demand or air-leakage sensitivity. The result is illustrative and does not replace equipment-specific property data, measurements or professional review.

### 7. Exercises and discussion

1. **Derive.** Start from an explicit control volume for surface condenser in a humid climate. Derive `Q_cond = m_dot*(h_in-h_out)` or identify its idealizing assumptions. Label every term and check dimensional homogeneity.
2. **Calculate.** Construct an internally consistent SI example for heat rejection from wet exhaust using values from a standard property table or clearly declared synthetic inputs. Calculate the nominal result and an output range when the dominant uncertain input is perturbed by ±5%.
3. **Diagnose.** A team reports an unexpected improvement while its fuel, electricity or fluid meters are undergoing maintenance. Form two measurement-error hypotheses and one physical-process hypothesis, then identify evidence that would discriminate among them.
4. **Compare.** Evaluate whether low condenser pressure can improve ideal work while worsening air-inleakage risk. Discuss at least one benefit, one new risk and a plant-level quantity that may offset the local benefit.
5. **Communicate.** Write a one-page engineering note distinguishing your numerical result, its assumptions, the source of each input, and the actions that require external professional review.

**Answer-check guidance.** A defensible solution shows its boundary, substitutions and units, not just the final numerical value. For a ±5% sensitivity, recompute the original equation at both input limits rather than automatically declaring the output to have the same percentage uncertainty. For evidence questions, name the actual sensor or log to examine and the expected sign of each competing effect. Qualitative trade-offs need a stated criterion—net export, fuel use, water, safety margin or total cost—rather than a vague ranking.

### 8. Research extension

Design a small, reproducible computational experiment about heat rejection from wet exhaust. Define a physically reasonable input range and record why the range was chosen; collect a baseline output; sweep one independent variable; and export the results with units and assumptions. Explain where the educational calculator in this book is too simple for the proposed study. Contrast its output with published technology characterizations or a documented manufacturer's map *without copying proprietary material*. Include a limitations paragraph on extrapolation, scale effects and evidence quality. A negative finding, such as failure to improve net plant performance despite an attractive component calculation, is a valid outcome when the assumptions are clear.


---

# Unit 02, Lesson 04 — Feedwater pumps and boiler input

**Core topic:** liquid-pump work and steam-generator duty. **Representative relation:** `w_p ≈ v*(p_out-p_in)`. **Case context:** multistage feedwater train.

The central question in this lesson is how to evaluate **liquid-pump work and steam-generator duty** when the engineer is given measurements from **multistage feedwater train**. First decide what quantity the result is supposed to describe. A thermodynamic component may have a local performance metric, while the whole plant has different inputs, outputs, auxiliaries and losses. Naming the metric prevents an apparently precise equation from addressing the wrong question. The representative relation is `w_p ≈ v*(p_out-p_in)`. This expression is a teaching starting point, not a complete design specification. Before putting values into it, define every term, identify the device boundary, and write its units. Where a symbol can have multiple interpretations, the label on the measurement sheet must be explicit.

### 1. Physical interpretation and scope

The phenomenon in focus is **liquid-pump work and steam-generator duty**. In a steam station with a boiler, high-pressure turbine, reheat section, condenser and feedwater pumps, a measured value will depend on the actual arrangement of equipment, the time interval over which it is averaged and the physical states entering each component. If an engineer isolates multistage feedwater train, the analysis should start by drawing arrows for all relevant energy or material streams and recording their directions. The next question is which measurements are direct and which come from a calculated property, manufacturer map, inferred coefficient or operational assumption. This distinction is more consequential than the number of decimal places in a spreadsheet.

A conservation equation and a constitutive relation serve different roles. Conservation says what the flows must sum to; a heat-transfer coefficient, turbomachinery efficiency, combustion model or empirical performance map helps explain how the flows divide in a specific design. When the calculation requires an unmeasured coefficient, report an explicit assumed range rather than disguising it as an observed constant. A reliable answer reports the sign of work and heat, the unit system and why a steady-state approximation is reasonable—or why it may be inadequate.

### 2. Derivation and use of the central relation

Begin with `w_p ≈ v*(p_out-p_in)` and identify the physical quantity on each side. A useful calculation is dimensionally self-consistent: for example MW equals MJ/s, mass flow in kg/s times a specific energy in kJ/kg produces kW, and the ratio of energies or rates is dimensionless only when numerator and denominator use comparable bases. Temperatures added in a balance can be Celsius differences; temperatures divided in ideal-gas or second-law relations must use kelvin. Pressure ratios use absolute pressure; a gauge-pressure reading must be converted before use in a physical ratio.

For liquid-pump work and steam-generator duty, specify whether the result assumes constant properties, negligible kinetic-energy changes, no stored-energy rate, or a fixed device efficiency. Each of these is an engineering hypothesis that can be tested or relaxed. When working from field data, reduce readings in the order: raw instrument value, calibrated engineering unit, time alignment, derived state quantity, physical balance, performance ratio. This audit trail allows a second engineer to repeat the estimate.

A special caution in this lesson is that **pressure must be in pascals with SI specific volume**. Explain exactly which algebraic term or measurement would be affected by that mistake. For a model with several serial components, a plausible local estimate may still be incompatible with the surrounding plant energy balance. Reconcile the result against the larger system. A model that demands more energy at the outlet than enters without storage, external work or a defined additional source should be rejected rather than patched by an unexplained correction factor.

### 3. Applied worked example — Feedwater pumps and boiler input

Using near-incompressible liquid specific volume 0.0011 m³/kg and pressure increase 11 MPa, ideal pump work per kilogram is approximately 0.0011 × 11,000,000 = **12,100 J/kg**, or 12.1 kJ/kg. A 75%-efficient pump requires approximately 16.1 kJ/kg shaft input, excluding other losses.

**Verification and limitations.** Convert pressure to pascals before multiplying by m³/kg; this dimensional check prevents a thousand-fold error. The result is illustrative and does not replace equipment-specific property data, measurements or professional review.

### 7. Exercises and discussion

1. **Derive.** Start from an explicit control volume for multistage feedwater train. Derive `w_p ≈ v*(p_out-p_in)` or identify its idealizing assumptions. Label every term and check dimensional homogeneity.
2. **Calculate.** Construct an internally consistent SI example for liquid-pump work and steam-generator duty using values from a standard property table or clearly declared synthetic inputs. Calculate the nominal result and an output range when the dominant uncertain input is perturbed by ±5%.
3. **Diagnose.** A team reports an unexpected improvement while its fuel, electricity or fluid meters are undergoing maintenance. Form two measurement-error hypotheses and one physical-process hypothesis, then identify evidence that would discriminate among them.
4. **Compare.** Evaluate whether ignoring boiler feed pump power makes net output too optimistic. Discuss at least one benefit, one new risk and a plant-level quantity that may offset the local benefit.
5. **Communicate.** Write a one-page engineering note distinguishing your numerical result, its assumptions, the source of each input, and the actions that require external professional review.

**Answer-check guidance.** A defensible solution shows its boundary, substitutions and units, not just the final numerical value. For a ±5% sensitivity, recompute the original equation at both input limits rather than automatically declaring the output to have the same percentage uncertainty. For evidence questions, name the actual sensor or log to examine and the expected sign of each competing effect. Qualitative trade-offs need a stated criterion—net export, fuel use, water, safety margin or total cost—rather than a vague ranking.

### 8. Research extension

Design a small, reproducible computational experiment about liquid-pump work and steam-generator duty. Define a physically reasonable input range and record why the range was chosen; collect a baseline output; sweep one independent variable; and export the results with units and assumptions. Explain where the educational calculator in this book is too simple for the proposed study. Contrast its output with published technology characterizations or a documented manufacturer's map *without copying proprietary material*. Include a limitations paragraph on extrapolation, scale effects and evidence quality. A negative finding, such as failure to improve net plant performance despite an attractive component calculation, is a valid outcome when the assumptions are clear.


---

# Unit 02, Lesson 05 — Reheat and regenerative feedwater heating

**Core topic:** cycle efficiency and moisture management. **Representative relation:** `Q_added = sum(m_dot*delta_h) across heated streams`. **Case context:** one reheat stage with closed feedwater heater.

The central question in this lesson is how to evaluate **cycle efficiency and moisture management** when the engineer is given measurements from **one reheat stage with closed feedwater heater**. First decide what quantity the result is supposed to describe. A thermodynamic component may have a local performance metric, while the whole plant has different inputs, outputs, auxiliaries and losses. Naming the metric prevents an apparently precise equation from addressing the wrong question. The representative relation is `Q_added = sum(m_dot*delta_h) across heated streams`. This expression is a teaching starting point, not a complete design specification. Before putting values into it, define every term, identify the device boundary, and write its units. Where a symbol can have multiple interpretations, the label on the measurement sheet must be explicit.

### 1. Physical interpretation and scope

The phenomenon in focus is **cycle efficiency and moisture management**. In a steam station with a boiler, high-pressure turbine, reheat section, condenser and feedwater pumps, a measured value will depend on the actual arrangement of equipment, the time interval over which it is averaged and the physical states entering each component. If an engineer isolates one reheat stage with closed feedwater heater, the analysis should start by drawing arrows for all relevant energy or material streams and recording their directions. The next question is which measurements are direct and which come from a calculated property, manufacturer map, inferred coefficient or operational assumption. This distinction is more consequential than the number of decimal places in a spreadsheet.

A conservation equation and a constitutive relation serve different roles. Conservation says what the flows must sum to; a heat-transfer coefficient, turbomachinery efficiency, combustion model or empirical performance map helps explain how the flows divide in a specific design. When the calculation requires an unmeasured coefficient, report an explicit assumed range rather than disguising it as an observed constant. A reliable answer reports the sign of work and heat, the unit system and why a steady-state approximation is reasonable—or why it may be inadequate.

### 2. Derivation and use of the central relation

Begin with `Q_added = sum(m_dot*delta_h) across heated streams` and identify the physical quantity on each side. A useful calculation is dimensionally self-consistent: for example MW equals MJ/s, mass flow in kg/s times a specific energy in kJ/kg produces kW, and the ratio of energies or rates is dimensionless only when numerator and denominator use comparable bases. Temperatures added in a balance can be Celsius differences; temperatures divided in ideal-gas or second-law relations must use kelvin. Pressure ratios use absolute pressure; a gauge-pressure reading must be converted before use in a physical ratio.

For cycle efficiency and moisture management, specify whether the result assumes constant properties, negligible kinetic-energy changes, no stored-energy rate, or a fixed device efficiency. Each of these is an engineering hypothesis that can be tested or relaxed. When working from field data, reduce readings in the order: raw instrument value, calibrated engineering unit, time alignment, derived state quantity, physical balance, performance ratio. This audit trail allows a second engineer to repeat the estimate.

A special caution in this lesson is that **bleed steam increases heater inlet temperature but reduces flow through later turbine stages**. Explain exactly which algebraic term or measurement would be affected by that mistake. For a model with several serial components, a plausible local estimate may still be incompatible with the surrounding plant energy balance. Reconcile the result against the larger system. A model that demands more energy at the outlet than enters without storage, external work or a defined additional source should be rejected rather than patched by an unexplained correction factor.

### 3. Applied worked example — Reheat and regenerative feedwater heating

A reheat section raises specific enthalpy of 45 kg/s of steam by 580 kJ/kg. Assuming negligible external heat loss, reheat duty is 45 × 580 = **26.1 MW(th)**. Whether reheat improves overall cycle efficiency depends on the resulting turbine expansion and heat-supply conditions, not duty alone.

**Verification and limitations.** For regenerative systems, a steam bleed lowers the downstream mass flow; use branch-by-branch energy balances. The result is illustrative and does not replace equipment-specific property data, measurements or professional review.

### 7. Exercises and discussion

1. **Derive.** Start from an explicit control volume for one reheat stage with closed feedwater heater. Derive `Q_added = sum(m_dot*delta_h) across heated streams` or identify its idealizing assumptions. Label every term and check dimensional homogeneity.
2. **Calculate.** Construct an internally consistent SI example for cycle efficiency and moisture management using values from a standard property table or clearly declared synthetic inputs. Calculate the nominal result and an output range when the dominant uncertain input is perturbed by ±5%.
3. **Diagnose.** A team reports an unexpected improvement while its fuel, electricity or fluid meters are undergoing maintenance. Form two measurement-error hypotheses and one physical-process hypothesis, then identify evidence that would discriminate among them.
4. **Compare.** Evaluate whether higher efficiency does not automatically justify additional complexity or capital cost. Discuss at least one benefit, one new risk and a plant-level quantity that may offset the local benefit.
5. **Communicate.** Write a one-page engineering note distinguishing your numerical result, its assumptions, the source of each input, and the actions that require external professional review.

**Answer-check guidance.** A defensible solution shows its boundary, substitutions and units, not just the final numerical value. For a ±5% sensitivity, recompute the original equation at both input limits rather than automatically declaring the output to have the same percentage uncertainty. For evidence questions, name the actual sensor or log to examine and the expected sign of each competing effect. Qualitative trade-offs need a stated criterion—net export, fuel use, water, safety margin or total cost—rather than a vague ranking.

### 8. Research extension

Design a small, reproducible computational experiment about cycle efficiency and moisture management. Define a physically reasonable input range and record why the range was chosen; collect a baseline output; sweep one independent variable; and export the results with units and assumptions. Explain where the educational calculator in this book is too simple for the proposed study. Contrast its output with published technology characterizations or a documented manufacturer's map *without copying proprietary material*. Include a limitations paragraph on extrapolation, scale effects and evidence quality. A negative finding, such as failure to improve net plant performance despite an attractive component calculation, is a valid outcome when the assumptions are clear.


---

