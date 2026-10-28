# Unit 04: Combined Cycles and Cogeneration

**Course Code**: PPE 304 · **Level**: Advanced Undergraduate Engineering

## Unit Overview & Physical Foundations

This comprehensive university textbook unit covers the theoretical framework, physical modeling, mathematical governing equations, and engineering applications of **Combined Cycles and Cogeneration**.

# Unit 04, Lesson 01 — Heat-recovery steam generators

**Core topic:** gas-to-water energy recovery. **Representative relation:** `Q_HRSG = m_dot_g*cp_g*(T_g,in-T_g,out)`. **Case context:** unfired exhaust heat exchanger.

The central question in this lesson is how to evaluate **gas-to-water energy recovery** when the engineer is given measurements from **unfired exhaust heat exchanger**. First decide what quantity the result is supposed to describe. A thermodynamic component may have a local performance metric, while the whole plant has different inputs, outputs, auxiliaries and losses. Naming the metric prevents an apparently precise equation from addressing the wrong question. The representative relation is `Q_HRSG = m_dot_g*cp_g*(T_g,in-T_g,out)`. This expression is a teaching starting point, not a complete design specification. Before putting values into it, define every term, identify the device boundary, and write its units. Where a symbol can have multiple interpretations, the label on the measurement sheet must be explicit.

### 1. Physical interpretation and scope

The phenomenon in focus is **gas-to-water energy recovery**. In a gas turbine coupled to a heat-recovery steam generator and supplementary district or industrial process heat offtake, a measured value will depend on the actual arrangement of equipment, the time interval over which it is averaged and the physical states entering each component. If an engineer isolates unfired exhaust heat exchanger, the analysis should start by drawing arrows for all relevant energy or material streams and recording their directions. The next question is which measurements are direct and which come from a calculated property, manufacturer map, inferred coefficient or operational assumption. This distinction is more consequential than the number of decimal places in a spreadsheet.

A conservation equation and a constitutive relation serve different roles. Conservation says what the flows must sum to; a heat-transfer coefficient, turbomachinery efficiency, combustion model or empirical performance map helps explain how the flows divide in a specific design. When the calculation requires an unmeasured coefficient, report an explicit assumed range rather than disguising it as an observed constant. A reliable answer reports the sign of work and heat, the unit system and why a steady-state approximation is reasonable—or why it may be inadequate.

### 2. Derivation and use of the central relation

Begin with `Q_HRSG = m_dot_g*cp_g*(T_g,in-T_g,out)` and identify the physical quantity on each side. A useful calculation is dimensionally self-consistent: for example MW equals MJ/s, mass flow in kg/s times a specific energy in kJ/kg produces kW, and the ratio of energies or rates is dimensionless only when numerator and denominator use comparable bases. Temperatures added in a balance can be Celsius differences; temperatures divided in ideal-gas or second-law relations must use kelvin. Pressure ratios use absolute pressure; a gauge-pressure reading must be converted before use in a physical ratio.

For gas-to-water energy recovery, specify whether the result assumes constant properties, negligible kinetic-energy changes, no stored-energy rate, or a fixed device efficiency. Each of these is an engineering hypothesis that can be tested or relaxed. When working from field data, reduce readings in the order: raw instrument value, calibrated engineering unit, time alignment, derived state quantity, physical balance, performance ratio. This audit trail allows a second engineer to repeat the estimate.

A special caution in this lesson is that **heat loss and heat-exchanger approach impose realistic limits**. Explain exactly which algebraic term or measurement would be affected by that mistake. For a model with several serial components, a plausible local estimate may still be incompatible with the surrounding plant energy balance. Reconcile the result against the larger system. A model that demands more energy at the outlet than enters without storage, external work or a defined additional source should be rejected rather than patched by an unexplained correction factor.

### 3. Applied worked example — Heat-recovery steam generators

An HRSG receives 220 kg/s of exhaust gas, with assumed cp = 1.1 kJ/(kg K), entering at 560 °C and leaving at 160 °C. Sensible heat lost by gas is 220 × 1.1 × 400 = **96.8 MW(th)**. Actual heat delivered to steam is lower if there are heat losses or bypass streams.

**Verification and limitations.** Finite temperature approach, material limits and stack condensation rules constrain real recovery. The result is illustrative and does not replace equipment-specific property data, measurements or professional review.

### 7. Exercises and discussion

1. **Derive.** Start from an explicit control volume for unfired exhaust heat exchanger. Derive `Q_HRSG = m_dot_g*cp_g*(T_g,in-T_g,out)` or identify its idealizing assumptions. Label every term and check dimensional homogeneity.
2. **Calculate.** Construct an internally consistent SI example for gas-to-water energy recovery using values from a standard property table or clearly declared synthetic inputs. Calculate the nominal result and an output range when the dominant uncertain input is perturbed by ±5%.
3. **Diagnose.** A team reports an unexpected improvement while its fuel, electricity or fluid meters are undergoing maintenance. Form two measurement-error hypotheses and one physical-process hypothesis, then identify evidence that would discriminate among them.
4. **Compare.** Evaluate whether lower stack temperature is not always safer or economically optimal. Discuss at least one benefit, one new risk and a plant-level quantity that may offset the local benefit.
5. **Communicate.** Write a one-page engineering note distinguishing your numerical result, its assumptions, the source of each input, and the actions that require external professional review.

**Answer-check guidance.** A defensible solution shows its boundary, substitutions and units, not just the final numerical value. For a ±5% sensitivity, recompute the original equation at both input limits rather than automatically declaring the output to have the same percentage uncertainty. For evidence questions, name the actual sensor or log to examine and the expected sign of each competing effect. Qualitative trade-offs need a stated criterion—net export, fuel use, water, safety margin or total cost—rather than a vague ranking.

### 8. Research extension

Design a small, reproducible computational experiment about gas-to-water energy recovery. Define a physically reasonable input range and record why the range was chosen; collect a baseline output; sweep one independent variable; and export the results with units and assumptions. Explain where the educational calculator in this book is too simple for the proposed study. Contrast its output with published technology characterizations or a documented manufacturer's map *without copying proprietary material*. Include a limitations paragraph on extrapolation, scale effects and evidence quality. A negative finding, such as failure to improve net plant performance despite an attractive component calculation, is a valid outcome when the assumptions are clear.


---

# Unit 04, Lesson 02 — Combined-cycle net efficiency

**Core topic:** system electric performance. **Representative relation:** `eta_CC = (P_GT+P_ST-P_aux)/Q_fuel`. **Case context:** gas and steam generator gross meters.

The central question in this lesson is how to evaluate **system electric performance** when the engineer is given measurements from **gas and steam generator gross meters**. First decide what quantity the result is supposed to describe. A thermodynamic component may have a local performance metric, while the whole plant has different inputs, outputs, auxiliaries and losses. Naming the metric prevents an apparently precise equation from addressing the wrong question. The representative relation is `eta_CC = (P_GT+P_ST-P_aux)/Q_fuel`. This expression is a teaching starting point, not a complete design specification. Before putting values into it, define every term, identify the device boundary, and write its units. Where a symbol can have multiple interpretations, the label on the measurement sheet must be explicit.

### 1. Physical interpretation and scope

The phenomenon in focus is **system electric performance**. In a gas turbine coupled to a heat-recovery steam generator and supplementary district or industrial process heat offtake, a measured value will depend on the actual arrangement of equipment, the time interval over which it is averaged and the physical states entering each component. If an engineer isolates gas and steam generator gross meters, the analysis should start by drawing arrows for all relevant energy or material streams and recording their directions. The next question is which measurements are direct and which come from a calculated property, manufacturer map, inferred coefficient or operational assumption. This distinction is more consequential than the number of decimal places in a spreadsheet.

A conservation equation and a constitutive relation serve different roles. Conservation says what the flows must sum to; a heat-transfer coefficient, turbomachinery efficiency, combustion model or empirical performance map helps explain how the flows divide in a specific design. When the calculation requires an unmeasured coefficient, report an explicit assumed range rather than disguising it as an observed constant. A reliable answer reports the sign of work and heat, the unit system and why a steady-state approximation is reasonable—or why it may be inadequate.

### 2. Derivation and use of the central relation

Begin with `eta_CC = (P_GT+P_ST-P_aux)/Q_fuel` and identify the physical quantity on each side. A useful calculation is dimensionally self-consistent: for example MW equals MJ/s, mass flow in kg/s times a specific energy in kJ/kg produces kW, and the ratio of energies or rates is dimensionless only when numerator and denominator use comparable bases. Temperatures added in a balance can be Celsius differences; temperatures divided in ideal-gas or second-law relations must use kelvin. Pressure ratios use absolute pressure; a gauge-pressure reading must be converted before use in a physical ratio.

For system electric performance, specify whether the result assumes constant properties, negligible kinetic-energy changes, no stored-energy rate, or a fixed device efficiency. Each of these is an engineering hypothesis that can be tested or relaxed. When working from field data, reduce readings in the order: raw instrument value, calibrated engineering unit, time alignment, derived state quantity, physical balance, performance ratio. This audit trail allows a second engineer to repeat the estimate.

A special caution in this lesson is that **avoid double-counting recovered heat as fresh fuel input**. Explain exactly which algebraic term or measurement would be affected by that mistake. For a model with several serial components, a plausible local estimate may still be incompatible with the surrounding plant energy balance. Reconcile the result against the larger system. A model that demands more energy at the outlet than enters without storage, external work or a defined additional source should be rejected rather than patched by an unexplained correction factor.

### 3. Applied worked example — Combined-cycle net efficiency

A gas turbine produces 180 MW(e), a downstream steam turbine 90 MW(e), and auxiliaries consume 12 MW(e), with 450 MW(th) primary fuel input. Net output is 258 MW(e) and overall net efficiency is 258/450 = **57.33%**. The fuel denominator already supplied the gas turbine; recovered exhaust is not counted as a second fuel source.

**Verification and limitations.** This is an illustrative operating point; ambient conditions and part-load behavior change real performance. The result is illustrative and does not replace equipment-specific property data, measurements or professional review.

### 7. Exercises and discussion

1. **Derive.** Start from an explicit control volume for gas and steam generator gross meters. Derive `eta_CC = (P_GT+P_ST-P_aux)/Q_fuel` or identify its idealizing assumptions. Label every term and check dimensional homogeneity.
2. **Calculate.** Construct an internally consistent SI example for system electric performance using values from a standard property table or clearly declared synthetic inputs. Calculate the nominal result and an output range when the dominant uncertain input is perturbed by ±5%.
3. **Diagnose.** A team reports an unexpected improvement while its fuel, electricity or fluid meters are undergoing maintenance. Form two measurement-error hypotheses and one physical-process hypothesis, then identify evidence that would discriminate among them.
4. **Compare.** Evaluate whether a high steam turbine output can be offset by cooling and pumping parasitics. Discuss at least one benefit, one new risk and a plant-level quantity that may offset the local benefit.
5. **Communicate.** Write a one-page engineering note distinguishing your numerical result, its assumptions, the source of each input, and the actions that require external professional review.

**Answer-check guidance.** A defensible solution shows its boundary, substitutions and units, not just the final numerical value. For a ±5% sensitivity, recompute the original equation at both input limits rather than automatically declaring the output to have the same percentage uncertainty. For evidence questions, name the actual sensor or log to examine and the expected sign of each competing effect. Qualitative trade-offs need a stated criterion—net export, fuel use, water, safety margin or total cost—rather than a vague ranking.

### 8. Research extension

Design a small, reproducible computational experiment about system electric performance. Define a physically reasonable input range and record why the range was chosen; collect a baseline output; sweep one independent variable; and export the results with units and assumptions. Explain where the educational calculator in this book is too simple for the proposed study. Contrast its output with published technology characterizations or a documented manufacturer's map *without copying proprietary material*. Include a limitations paragraph on extrapolation, scale effects and evidence quality. A negative finding, such as failure to improve net plant performance despite an attractive component calculation, is a valid outcome when the assumptions are clear.


---

# Unit 04, Lesson 03 — CHP total fuel utilization

**Core topic:** simultaneous heat and electric services. **Representative relation:** `U_CHP = (P_e+Q_useful)/Q_fuel`. **Case context:** industrial process steam demand.

The central question in this lesson is how to evaluate **simultaneous heat and electric services** when the engineer is given measurements from **industrial process steam demand**. First decide what quantity the result is supposed to describe. A thermodynamic component may have a local performance metric, while the whole plant has different inputs, outputs, auxiliaries and losses. Naming the metric prevents an apparently precise equation from addressing the wrong question. The representative relation is `U_CHP = (P_e+Q_useful)/Q_fuel`. This expression is a teaching starting point, not a complete design specification. Before putting values into it, define every term, identify the device boundary, and write its units. Where a symbol can have multiple interpretations, the label on the measurement sheet must be explicit.

### 1. Physical interpretation and scope

The phenomenon in focus is **simultaneous heat and electric services**. In a gas turbine coupled to a heat-recovery steam generator and supplementary district or industrial process heat offtake, a measured value will depend on the actual arrangement of equipment, the time interval over which it is averaged and the physical states entering each component. If an engineer isolates industrial process steam demand, the analysis should start by drawing arrows for all relevant energy or material streams and recording their directions. The next question is which measurements are direct and which come from a calculated property, manufacturer map, inferred coefficient or operational assumption. This distinction is more consequential than the number of decimal places in a spreadsheet.

A conservation equation and a constitutive relation serve different roles. Conservation says what the flows must sum to; a heat-transfer coefficient, turbomachinery efficiency, combustion model or empirical performance map helps explain how the flows divide in a specific design. When the calculation requires an unmeasured coefficient, report an explicit assumed range rather than disguising it as an observed constant. A reliable answer reports the sign of work and heat, the unit system and why a steady-state approximation is reasonable—or why it may be inadequate.

### 2. Derivation and use of the central relation

Begin with `U_CHP = (P_e+Q_useful)/Q_fuel` and identify the physical quantity on each side. A useful calculation is dimensionally self-consistent: for example MW equals MJ/s, mass flow in kg/s times a specific energy in kJ/kg produces kW, and the ratio of energies or rates is dimensionless only when numerator and denominator use comparable bases. Temperatures added in a balance can be Celsius differences; temperatures divided in ideal-gas or second-law relations must use kelvin. Pressure ratios use absolute pressure; a gauge-pressure reading must be converted before use in a physical ratio.

For simultaneous heat and electric services, specify whether the result assumes constant properties, negligible kinetic-energy changes, no stored-energy rate, or a fixed device efficiency. Each of these is an engineering hypothesis that can be tested or relaxed. When working from field data, reduce readings in the order: raw instrument value, calibrated engineering unit, time alignment, derived state quantity, physical balance, performance ratio. This audit trail allows a second engineer to repeat the estimate.

A special caution in this lesson is that **useful exported heat must be valued and metered separately**. Explain exactly which algebraic term or measurement would be affected by that mistake. For a model with several serial components, a plausible local estimate may still be incompatible with the surrounding plant energy balance. Reconcile the result against the larger system. A model that demands more energy at the outlet than enters without storage, external work or a defined additional source should be rejected rather than patched by an unexplained correction factor.

### 3. Applied worked example — CHP total fuel utilization

A CHP plant produces 30 MW(e) and delivers 40 MW(th) of genuinely useful heat while consuming 100 MW(th) primary fuel. Total fuel utilization is (30 + 40)/100 = **70%**. Its electric-only ratio remains 30%; a different customer heat-demand profile could substantially reduce the annual useful-heat credit.

**Verification and limitations.** Measure heat at the customer export boundary rather than counting internal steam circulation. The result is illustrative and does not replace equipment-specific property data, measurements or professional review.

### 7. Exercises and discussion

1. **Derive.** Start from an explicit control volume for industrial process steam demand. Derive `U_CHP = (P_e+Q_useful)/Q_fuel` or identify its idealizing assumptions. Label every term and check dimensional homogeneity.
2. **Calculate.** Construct an internally consistent SI example for simultaneous heat and electric services using values from a standard property table or clearly declared synthetic inputs. Calculate the nominal result and an output range when the dominant uncertain input is perturbed by ±5%.
3. **Diagnose.** A team reports an unexpected improvement while its fuel, electricity or fluid meters are undergoing maintenance. Form two measurement-error hypotheses and one physical-process hypothesis, then identify evidence that would discriminate among them.
4. **Compare.** Evaluate whether high utilization does not prove economic competitiveness when heat demand is seasonal. Discuss at least one benefit, one new risk and a plant-level quantity that may offset the local benefit.
5. **Communicate.** Write a one-page engineering note distinguishing your numerical result, its assumptions, the source of each input, and the actions that require external professional review.

**Answer-check guidance.** A defensible solution shows its boundary, substitutions and units, not just the final numerical value. For a ±5% sensitivity, recompute the original equation at both input limits rather than automatically declaring the output to have the same percentage uncertainty. For evidence questions, name the actual sensor or log to examine and the expected sign of each competing effect. Qualitative trade-offs need a stated criterion—net export, fuel use, water, safety margin or total cost—rather than a vague ranking.

### 8. Research extension

Design a small, reproducible computational experiment about simultaneous heat and electric services. Define a physically reasonable input range and record why the range was chosen; collect a baseline output; sweep one independent variable; and export the results with units and assumptions. Explain where the educational calculator in this book is too simple for the proposed study. Contrast its output with published technology characterizations or a documented manufacturer's map *without copying proprietary material*. Include a limitations paragraph on extrapolation, scale effects and evidence quality. A negative finding, such as failure to improve net plant performance despite an attractive component calculation, is a valid outcome when the assumptions are clear.


---

# Unit 04, Lesson 04 — Pinch, approach and exhaust constraints

**Core topic:** thermal contact and exchanger sizing. **Representative relation:** `DeltaT_pinch = T_g,evap_out-T_sat`. **Case context:** single-pressure HRSG temperature sketch.

The central question in this lesson is how to evaluate **thermal contact and exchanger sizing** when the engineer is given measurements from **single-pressure HRSG temperature sketch**. First decide what quantity the result is supposed to describe. A thermodynamic component may have a local performance metric, while the whole plant has different inputs, outputs, auxiliaries and losses. Naming the metric prevents an apparently precise equation from addressing the wrong question. The representative relation is `DeltaT_pinch = T_g,evap_out-T_sat`. This expression is a teaching starting point, not a complete design specification. Before putting values into it, define every term, identify the device boundary, and write its units. Where a symbol can have multiple interpretations, the label on the measurement sheet must be explicit.

### 1. Physical interpretation and scope

The phenomenon in focus is **thermal contact and exchanger sizing**. In a gas turbine coupled to a heat-recovery steam generator and supplementary district or industrial process heat offtake, a measured value will depend on the actual arrangement of equipment, the time interval over which it is averaged and the physical states entering each component. If an engineer isolates single-pressure HRSG temperature sketch, the analysis should start by drawing arrows for all relevant energy or material streams and recording their directions. The next question is which measurements are direct and which come from a calculated property, manufacturer map, inferred coefficient or operational assumption. This distinction is more consequential than the number of decimal places in a spreadsheet.

A conservation equation and a constitutive relation serve different roles. Conservation says what the flows must sum to; a heat-transfer coefficient, turbomachinery efficiency, combustion model or empirical performance map helps explain how the flows divide in a specific design. When the calculation requires an unmeasured coefficient, report an explicit assumed range rather than disguising it as an observed constant. A reliable answer reports the sign of work and heat, the unit system and why a steady-state approximation is reasonable—or why it may be inadequate.

### 2. Derivation and use of the central relation

Begin with `DeltaT_pinch = T_g,evap_out-T_sat` and identify the physical quantity on each side. A useful calculation is dimensionally self-consistent: for example MW equals MJ/s, mass flow in kg/s times a specific energy in kJ/kg produces kW, and the ratio of energies or rates is dimensionless only when numerator and denominator use comparable bases. Temperatures added in a balance can be Celsius differences; temperatures divided in ideal-gas or second-law relations must use kelvin. Pressure ratios use absolute pressure; a gauge-pressure reading must be converted before use in a physical ratio.

For thermal contact and exchanger sizing, specify whether the result assumes constant properties, negligible kinetic-energy changes, no stored-energy rate, or a fixed device efficiency. Each of these is an engineering hypothesis that can be tested or relaxed. When working from field data, reduce readings in the order: raw instrument value, calibrated engineering unit, time alignment, derived state quantity, physical balance, performance ratio. This audit trail allows a second engineer to repeat the estimate.

A special caution in this lesson is that **zero pinch would demand infinite area in an idealized heat exchanger**. Explain exactly which algebraic term or measurement would be affected by that mistake. For a model with several serial components, a plausible local estimate may still be incompatible with the surrounding plant energy balance. Reconcile the result against the larger system. A model that demands more energy at the outlet than enters without storage, external work or a defined additional source should be rejected rather than patched by an unexplained correction factor.

### 3. Applied worked example — Pinch, approach and exhaust constraints

In a schematic HRSG, the gas temperature leaving the evaporator is 195 °C and steam saturation temperature is 175 °C at that section. Pinch temperature difference is **20 K**. Reducing this difference would generally require greater heat-transfer area or different design; it cannot be reduced to zero in a finite exchanger for finite heat transfer.

**Verification and limitations.** A local pinch value does not describe the complete multi-pressure temperature profile or acid-dew-point limits. The result is illustrative and does not replace equipment-specific property data, measurements or professional review.

### 7. Exercises and discussion

1. **Derive.** Start from an explicit control volume for single-pressure HRSG temperature sketch. Derive `DeltaT_pinch = T_g,evap_out-T_sat` or identify its idealizing assumptions. Label every term and check dimensional homogeneity.
2. **Calculate.** Construct an internally consistent SI example for thermal contact and exchanger sizing using values from a standard property table or clearly declared synthetic inputs. Calculate the nominal result and an output range when the dominant uncertain input is perturbed by ±5%.
3. **Diagnose.** A team reports an unexpected improvement while its fuel, electricity or fluid meters are undergoing maintenance. Form two measurement-error hypotheses and one physical-process hypothesis, then identify evidence that would discriminate among them.
4. **Compare.** Evaluate whether high recovery may require costly surface area and attention to acid condensation. Discuss at least one benefit, one new risk and a plant-level quantity that may offset the local benefit.
5. **Communicate.** Write a one-page engineering note distinguishing your numerical result, its assumptions, the source of each input, and the actions that require external professional review.

**Answer-check guidance.** A defensible solution shows its boundary, substitutions and units, not just the final numerical value. For a ±5% sensitivity, recompute the original equation at both input limits rather than automatically declaring the output to have the same percentage uncertainty. For evidence questions, name the actual sensor or log to examine and the expected sign of each competing effect. Qualitative trade-offs need a stated criterion—net export, fuel use, water, safety margin or total cost—rather than a vague ranking.

### 8. Research extension

Design a small, reproducible computational experiment about thermal contact and exchanger sizing. Define a physically reasonable input range and record why the range was chosen; collect a baseline output; sweep one independent variable; and export the results with units and assumptions. Explain where the educational calculator in this book is too simple for the proposed study. Contrast its output with published technology characterizations or a documented manufacturer's map *without copying proprietary material*. Include a limitations paragraph on extrapolation, scale effects and evidence quality. A negative finding, such as failure to improve net plant performance despite an attractive component calculation, is a valid outcome when the assumptions are clear.


---

# Unit 04, Lesson 05 — Integrated part-load operation

**Core topic:** coupled equipment at variable demand. **Representative relation:** `P_net = P_GT(load)+P_ST(load)-P_aux(load)`. **Case context:** daily dispatch and ambient-temperature variation.

The central question in this lesson is how to evaluate **coupled equipment at variable demand** when the engineer is given measurements from **daily dispatch and ambient-temperature variation**. First decide what quantity the result is supposed to describe. A thermodynamic component may have a local performance metric, while the whole plant has different inputs, outputs, auxiliaries and losses. Naming the metric prevents an apparently precise equation from addressing the wrong question. The representative relation is `P_net = P_GT(load)+P_ST(load)-P_aux(load)`. This expression is a teaching starting point, not a complete design specification. Before putting values into it, define every term, identify the device boundary, and write its units. Where a symbol can have multiple interpretations, the label on the measurement sheet must be explicit.

### 1. Physical interpretation and scope

The phenomenon in focus is **coupled equipment at variable demand**. In a gas turbine coupled to a heat-recovery steam generator and supplementary district or industrial process heat offtake, a measured value will depend on the actual arrangement of equipment, the time interval over which it is averaged and the physical states entering each component. If an engineer isolates daily dispatch and ambient-temperature variation, the analysis should start by drawing arrows for all relevant energy or material streams and recording their directions. The next question is which measurements are direct and which come from a calculated property, manufacturer map, inferred coefficient or operational assumption. This distinction is more consequential than the number of decimal places in a spreadsheet.

A conservation equation and a constitutive relation serve different roles. Conservation says what the flows must sum to; a heat-transfer coefficient, turbomachinery efficiency, combustion model or empirical performance map helps explain how the flows divide in a specific design. When the calculation requires an unmeasured coefficient, report an explicit assumed range rather than disguising it as an observed constant. A reliable answer reports the sign of work and heat, the unit system and why a steady-state approximation is reasonable—or why it may be inadequate.

### 2. Derivation and use of the central relation

Begin with `P_net = P_GT(load)+P_ST(load)-P_aux(load)` and identify the physical quantity on each side. A useful calculation is dimensionally self-consistent: for example MW equals MJ/s, mass flow in kg/s times a specific energy in kJ/kg produces kW, and the ratio of energies or rates is dimensionless only when numerator and denominator use comparable bases. Temperatures added in a balance can be Celsius differences; temperatures divided in ideal-gas or second-law relations must use kelvin. Pressure ratios use absolute pressure; a gauge-pressure reading must be converted before use in a physical ratio.

For coupled equipment at variable demand, specify whether the result assumes constant properties, negligible kinetic-energy changes, no stored-energy rate, or a fixed device efficiency. Each of these is an engineering hypothesis that can be tested or relaxed. When working from field data, reduce readings in the order: raw instrument value, calibrated engineering unit, time alignment, derived state quantity, physical balance, performance ratio. This audit trail allows a second engineer to repeat the estimate.

A special caution in this lesson is that **component response is nonlinear and startup constraints matter**. Explain exactly which algebraic term or measurement would be affected by that mistake. For a model with several serial components, a plausible local estimate may still be incompatible with the surrounding plant energy balance. Reconcile the result against the larger system. A model that demands more energy at the outlet than enters without storage, external work or a defined additional source should be rejected rather than patched by an unexplained correction factor.

### 3. Applied worked example — Integrated part-load operation

At a particular dispatch point, gas and steam turbines produce 150 and 70 MW(e), and station service consumes 10 MW(e). Net export is **210 MW(e)**. A 10% gas-turbine reduction need not yield an immediate 10% steam-turbine reduction because exhaust temperature, steam storage, controls and time response all matter.

**Verification and limitations.** Do not use a fixed rated steam-to-gas power ratio to predict part-load output. The result is illustrative and does not replace equipment-specific property data, measurements or professional review.

### 7. Exercises and discussion

1. **Derive.** Start from an explicit control volume for daily dispatch and ambient-temperature variation. Derive `P_net = P_GT(load)+P_ST(load)-P_aux(load)` or identify its idealizing assumptions. Label every term and check dimensional homogeneity.
2. **Calculate.** Construct an internally consistent SI example for coupled equipment at variable demand using values from a standard property table or clearly declared synthetic inputs. Calculate the nominal result and an output range when the dominant uncertain input is perturbed by ±5%.
3. **Diagnose.** A team reports an unexpected improvement while its fuel, electricity or fluid meters are undergoing maintenance. Form two measurement-error hypotheses and one physical-process hypothesis, then identify evidence that would discriminate among them.
4. **Compare.** Evaluate whether rated design-point efficiency cannot be assumed for every operating hour. Discuss at least one benefit, one new risk and a plant-level quantity that may offset the local benefit.
5. **Communicate.** Write a one-page engineering note distinguishing your numerical result, its assumptions, the source of each input, and the actions that require external professional review.

**Answer-check guidance.** A defensible solution shows its boundary, substitutions and units, not just the final numerical value. For a ±5% sensitivity, recompute the original equation at both input limits rather than automatically declaring the output to have the same percentage uncertainty. For evidence questions, name the actual sensor or log to examine and the expected sign of each competing effect. Qualitative trade-offs need a stated criterion—net export, fuel use, water, safety margin or total cost—rather than a vague ranking.

### 8. Research extension

Design a small, reproducible computational experiment about coupled equipment at variable demand. Define a physically reasonable input range and record why the range was chosen; collect a baseline output; sweep one independent variable; and export the results with units and assumptions. Explain where the educational calculator in this book is too simple for the proposed study. Contrast its output with published technology characterizations or a documented manufacturer's map *without copying proprietary material*. Include a limitations paragraph on extrapolation, scale effects and evidence quality. A negative finding, such as failure to improve net plant performance despite an attractive component calculation, is a valid outcome when the assumptions are clear.


---

