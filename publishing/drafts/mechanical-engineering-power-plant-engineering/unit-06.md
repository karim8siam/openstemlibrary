# Unit 06: Nonfossil Generation and Hybrid Power Systems

**Course Code**: PPE 306 · **Level**: Advanced Undergraduate Engineering

## Unit Overview & Physical Foundations

This comprehensive university textbook unit covers the theoretical framework, physical modeling, mathematical governing equations, and engineering applications of **Nonfossil Generation and Hybrid Power Systems**.

# Unit 06, Lesson 01 — Hydroelectric conversion and head

**Core topic:** hydraulic potential to electric power. **Representative relation:** `P_h = rho*g*Q*H*eta`. **Case context:** reservoir release with known head.

The central question in this lesson is how to evaluate **hydraulic potential to electric power** when the engineer is given measurements from **reservoir release with known head**. First decide what quantity the result is supposed to describe. A thermodynamic component may have a local performance metric, while the whole plant has different inputs, outputs, auxiliaries and losses. Naming the metric prevents an apparently precise equation from addressing the wrong question. The representative relation is `P_h = rho*g*Q*H*eta`. This expression is a teaching starting point, not a complete design specification. Before putting values into it, define every term, identify the device boundary, and write its units. Where a symbol can have multiple interpretations, the label on the measurement sheet must be explicit.

### 1. Physical interpretation and scope

The phenomenon in focus is **hydraulic potential to electric power**. In a grid region evaluating thermal station replacement, variable renewable support and flexible generation, a measured value will depend on the actual arrangement of equipment, the time interval over which it is averaged and the physical states entering each component. If an engineer isolates reservoir release with known head, the analysis should start by drawing arrows for all relevant energy or material streams and recording their directions. The next question is which measurements are direct and which come from a calculated property, manufacturer map, inferred coefficient or operational assumption. This distinction is more consequential than the number of decimal places in a spreadsheet.

A conservation equation and a constitutive relation serve different roles. Conservation says what the flows must sum to; a heat-transfer coefficient, turbomachinery efficiency, combustion model or empirical performance map helps explain how the flows divide in a specific design. When the calculation requires an unmeasured coefficient, report an explicit assumed range rather than disguising it as an observed constant. A reliable answer reports the sign of work and heat, the unit system and why a steady-state approximation is reasonable—or why it may be inadequate.

### 2. Derivation and use of the central relation

Begin with `P_h = rho*g*Q*H*eta` and identify the physical quantity on each side. A useful calculation is dimensionally self-consistent: for example MW equals MJ/s, mass flow in kg/s times a specific energy in kJ/kg produces kW, and the ratio of energies or rates is dimensionless only when numerator and denominator use comparable bases. Temperatures added in a balance can be Celsius differences; temperatures divided in ideal-gas or second-law relations must use kelvin. Pressure ratios use absolute pressure; a gauge-pressure reading must be converted before use in a physical ratio.

For hydraulic potential to electric power, specify whether the result assumes constant properties, negligible kinetic-energy changes, no stored-energy rate, or a fixed device efficiency. Each of these is an engineering hypothesis that can be tested or relaxed. When working from field data, reduce readings in the order: raw instrument value, calibrated engineering unit, time alignment, derived state quantity, physical balance, performance ratio. This audit trail allows a second engineer to repeat the estimate.

A special caution in this lesson is that **net head and turbine-generator efficiency must be distinguished**. Explain exactly which algebraic term or measurement would be affected by that mistake. For a model with several serial components, a plausible local estimate may still be incompatible with the surrounding plant energy balance. Reconcile the result against the larger system. A model that demands more energy at the outlet than enters without storage, external work or a defined additional source should be rejected rather than patched by an unexplained correction factor.

### 3. Applied worked example — Hydroelectric conversion and head

Take water density 1000 kg/m³, g = 9.81 m/s², flow 40 m³/s, net head 75 m and total efficiency 0.90. Hydropower is 1000 × 9.81 × 40 × 75 × 0.90 = **26.487 MW(e)**. Actual output also depends on reservoir conditions, permitted releases and seasonal flow.

**Verification and limitations.** Using gross rather than net head causes a systematic overestimate of delivered power. The result is illustrative and does not replace equipment-specific property data, measurements or professional review.

### 7. Exercises and discussion

1. **Derive.** Start from an explicit control volume for reservoir release with known head. Derive `P_h = rho*g*Q*H*eta` or identify its idealizing assumptions. Label every term and check dimensional homogeneity.
2. **Calculate.** Construct an internally consistent SI example for hydraulic potential to electric power using values from a standard property table or clearly declared synthetic inputs. Calculate the nominal result and an output range when the dominant uncertain input is perturbed by ±5%.
3. **Diagnose.** A team reports an unexpected improvement while its fuel, electricity or fluid meters are undergoing maintenance. Form two measurement-error hypotheses and one physical-process hypothesis, then identify evidence that would discriminate among them.
4. **Compare.** Evaluate whether drought and ecological constraints can dominate rated power. Discuss at least one benefit, one new risk and a plant-level quantity that may offset the local benefit.
5. **Communicate.** Write a one-page engineering note distinguishing your numerical result, its assumptions, the source of each input, and the actions that require external professional review.

**Answer-check guidance.** A defensible solution shows its boundary, substitutions and units, not just the final numerical value. For a ±5% sensitivity, recompute the original equation at both input limits rather than automatically declaring the output to have the same percentage uncertainty. For evidence questions, name the actual sensor or log to examine and the expected sign of each competing effect. Qualitative trade-offs need a stated criterion—net export, fuel use, water, safety margin or total cost—rather than a vague ranking.

### 8. Research extension

Design a small, reproducible computational experiment about hydraulic potential to electric power. Define a physically reasonable input range and record why the range was chosen; collect a baseline output; sweep one independent variable; and export the results with units and assumptions. Explain where the educational calculator in this book is too simple for the proposed study. Contrast its output with published technology characterizations or a documented manufacturer's map *without copying proprietary material*. Include a limitations paragraph on extrapolation, scale effects and evidence quality. A negative finding, such as failure to improve net plant performance despite an attractive component calculation, is a valid outcome when the assumptions are clear.


---

# Unit 06, Lesson 02 — Wind and variable-power capture

**Core topic:** wind-energy flux and rotor capture. **Representative relation:** `P_w = 0.5*rho_air*A*V**3*Cp`. **Case context:** wind farm performance estimate.

The central question in this lesson is how to evaluate **wind-energy flux and rotor capture** when the engineer is given measurements from **wind farm performance estimate**. First decide what quantity the result is supposed to describe. A thermodynamic component may have a local performance metric, while the whole plant has different inputs, outputs, auxiliaries and losses. Naming the metric prevents an apparently precise equation from addressing the wrong question. The representative relation is `P_w = 0.5*rho_air*A*V**3*Cp`. This expression is a teaching starting point, not a complete design specification. Before putting values into it, define every term, identify the device boundary, and write its units. Where a symbol can have multiple interpretations, the label on the measurement sheet must be explicit.

### 1. Physical interpretation and scope

The phenomenon in focus is **wind-energy flux and rotor capture**. In a grid region evaluating thermal station replacement, variable renewable support and flexible generation, a measured value will depend on the actual arrangement of equipment, the time interval over which it is averaged and the physical states entering each component. If an engineer isolates wind farm performance estimate, the analysis should start by drawing arrows for all relevant energy or material streams and recording their directions. The next question is which measurements are direct and which come from a calculated property, manufacturer map, inferred coefficient or operational assumption. This distinction is more consequential than the number of decimal places in a spreadsheet.

A conservation equation and a constitutive relation serve different roles. Conservation says what the flows must sum to; a heat-transfer coefficient, turbomachinery efficiency, combustion model or empirical performance map helps explain how the flows divide in a specific design. When the calculation requires an unmeasured coefficient, report an explicit assumed range rather than disguising it as an observed constant. A reliable answer reports the sign of work and heat, the unit system and why a steady-state approximation is reasonable—or why it may be inadequate.

### 2. Derivation and use of the central relation

Begin with `P_w = 0.5*rho_air*A*V**3*Cp` and identify the physical quantity on each side. A useful calculation is dimensionally self-consistent: for example MW equals MJ/s, mass flow in kg/s times a specific energy in kJ/kg produces kW, and the ratio of energies or rates is dimensionless only when numerator and denominator use comparable bases. Temperatures added in a balance can be Celsius differences; temperatures divided in ideal-gas or second-law relations must use kelvin. Pressure ratios use absolute pressure; a gauge-pressure reading must be converted before use in a physical ratio.

For wind-energy flux and rotor capture, specify whether the result assumes constant properties, negligible kinetic-energy changes, no stored-energy rate, or a fixed device efficiency. Each of these is an engineering hypothesis that can be tested or relaxed. When working from field data, reduce readings in the order: raw instrument value, calibrated engineering unit, time alignment, derived state quantity, physical balance, performance ratio. This audit trail allows a second engineer to repeat the estimate.

A special caution in this lesson is that **power coefficient varies with speed and control settings**. Explain exactly which algebraic term or measurement would be affected by that mistake. For a model with several serial components, a plausible local estimate may still be incompatible with the surrounding plant energy balance. Reconcile the result against the larger system. A model that demands more energy at the outlet than enters without storage, external work or a defined additional source should be rejected rather than patched by an unexplained correction factor.

### 3. Applied worked example — Wind and variable-power capture

For air density 1.2 kg/m³, swept area 5000 m², wind speed 8 m/s and power coefficient 0.42, idealized captured power is 0.5 × 1.2 × 5000 × 8³ × 0.42 = **0.645 MW**. Because wind power scales as the cube of speed, using the arithmetic mean wind speed in this formula cannot generally reproduce annual energy.

**Verification and limitations.** Do not assume Cp constant across wind speeds or disregard cut-in and cut-out limits. The result is illustrative and does not replace equipment-specific property data, measurements or professional review.

### 7. Exercises and discussion

1. **Derive.** Start from an explicit control volume for wind farm performance estimate. Derive `P_w = 0.5*rho_air*A*V**3*Cp` or identify its idealizing assumptions. Label every term and check dimensional homogeneity.
2. **Calculate.** Construct an internally consistent SI example for wind-energy flux and rotor capture using values from a standard property table or clearly declared synthetic inputs. Calculate the nominal result and an output range when the dominant uncertain input is perturbed by ±5%.
3. **Diagnose.** A team reports an unexpected improvement while its fuel, electricity or fluid meters are undergoing maintenance. Form two measurement-error hypotheses and one physical-process hypothesis, then identify evidence that would discriminate among them.
4. **Compare.** Evaluate whether single wind-speed estimates cannot predict annual output. Discuss at least one benefit, one new risk and a plant-level quantity that may offset the local benefit.
5. **Communicate.** Write a one-page engineering note distinguishing your numerical result, its assumptions, the source of each input, and the actions that require external professional review.

**Answer-check guidance.** A defensible solution shows its boundary, substitutions and units, not just the final numerical value. For a ±5% sensitivity, recompute the original equation at both input limits rather than automatically declaring the output to have the same percentage uncertainty. For evidence questions, name the actual sensor or log to examine and the expected sign of each competing effect. Qualitative trade-offs need a stated criterion—net export, fuel use, water, safety margin or total cost—rather than a vague ranking.

### 8. Research extension

Design a small, reproducible computational experiment about wind-energy flux and rotor capture. Define a physically reasonable input range and record why the range was chosen; collect a baseline output; sweep one independent variable; and export the results with units and assumptions. Explain where the educational calculator in this book is too simple for the proposed study. Contrast its output with published technology characterizations or a documented manufacturer's map *without copying proprietary material*. Include a limitations paragraph on extrapolation, scale effects and evidence quality. A negative finding, such as failure to improve net plant performance despite an attractive component calculation, is a valid outcome when the assumptions are clear.


---

# Unit 06, Lesson 03 — Solar photovoltaics and solar thermal

**Core topic:** incident irradiance and AC derating. **Representative relation:** `P_PV = G*A*eta_module*PR`. **Case context:** rooftop module versus utility-scale array.

The central question in this lesson is how to evaluate **incident irradiance and AC derating** when the engineer is given measurements from **rooftop module versus utility-scale array**. First decide what quantity the result is supposed to describe. A thermodynamic component may have a local performance metric, while the whole plant has different inputs, outputs, auxiliaries and losses. Naming the metric prevents an apparently precise equation from addressing the wrong question. The representative relation is `P_PV = G*A*eta_module*PR`. This expression is a teaching starting point, not a complete design specification. Before putting values into it, define every term, identify the device boundary, and write its units. Where a symbol can have multiple interpretations, the label on the measurement sheet must be explicit.

### 1. Physical interpretation and scope

The phenomenon in focus is **incident irradiance and AC derating**. In a grid region evaluating thermal station replacement, variable renewable support and flexible generation, a measured value will depend on the actual arrangement of equipment, the time interval over which it is averaged and the physical states entering each component. If an engineer isolates rooftop module versus utility-scale array, the analysis should start by drawing arrows for all relevant energy or material streams and recording their directions. The next question is which measurements are direct and which come from a calculated property, manufacturer map, inferred coefficient or operational assumption. This distinction is more consequential than the number of decimal places in a spreadsheet.

A conservation equation and a constitutive relation serve different roles. Conservation says what the flows must sum to; a heat-transfer coefficient, turbomachinery efficiency, combustion model or empirical performance map helps explain how the flows divide in a specific design. When the calculation requires an unmeasured coefficient, report an explicit assumed range rather than disguising it as an observed constant. A reliable answer reports the sign of work and heat, the unit system and why a steady-state approximation is reasonable—or why it may be inadequate.

### 2. Derivation and use of the central relation

Begin with `P_PV = G*A*eta_module*PR` and identify the physical quantity on each side. A useful calculation is dimensionally self-consistent: for example MW equals MJ/s, mass flow in kg/s times a specific energy in kJ/kg produces kW, and the ratio of energies or rates is dimensionless only when numerator and denominator use comparable bases. Temperatures added in a balance can be Celsius differences; temperatures divided in ideal-gas or second-law relations must use kelvin. Pressure ratios use absolute pressure; a gauge-pressure reading must be converted before use in a physical ratio.

For incident irradiance and AC derating, specify whether the result assumes constant properties, negligible kinetic-energy changes, no stored-energy rate, or a fixed device efficiency. Each of these is an engineering hypothesis that can be tested or relaxed. When working from field data, reduce readings in the order: raw instrument value, calibrated engineering unit, time alignment, derived state quantity, physical balance, performance ratio. This audit trail allows a second engineer to repeat the estimate.

A special caution in this lesson is that **rating conditions do not match every outdoor temperature**. Explain exactly which algebraic term or measurement would be affected by that mistake. For a model with several serial components, a plausible local estimate may still be incompatible with the surrounding plant energy balance. Reconcile the result against the larger system. A model that demands more energy at the outlet than enters without storage, external work or a defined additional source should be rejected rather than patched by an unexplained correction factor.

### 3. Applied worked example — Solar photovoltaics and solar thermal

A 5000 m² PV array receives irradiance 800 W/m², has an assumed module efficiency of 20% and an overall performance ratio of 0.85. Net illustrative output is 800 × 5000 × 0.20 × 0.85 = **680 kW**. This is an instantaneous representative condition, not an annual yield estimate.

**Verification and limitations.** Shading, inverter clipping, temperature and soiling require more complete modeling. The result is illustrative and does not replace equipment-specific property data, measurements or professional review.

### 7. Exercises and discussion

1. **Derive.** Start from an explicit control volume for rooftop module versus utility-scale array. Derive `P_PV = G*A*eta_module*PR` or identify its idealizing assumptions. Label every term and check dimensional homogeneity.
2. **Calculate.** Construct an internally consistent SI example for incident irradiance and AC derating using values from a standard property table or clearly declared synthetic inputs. Calculate the nominal result and an output range when the dominant uncertain input is perturbed by ±5%.
3. **Diagnose.** A team reports an unexpected improvement while its fuel, electricity or fluid meters are undergoing maintenance. Form two measurement-error hypotheses and one physical-process hypothesis, then identify evidence that would discriminate among them.
4. **Compare.** Evaluate whether inverter limits and weather create nonlinear annual performance. Discuss at least one benefit, one new risk and a plant-level quantity that may offset the local benefit.
5. **Communicate.** Write a one-page engineering note distinguishing your numerical result, its assumptions, the source of each input, and the actions that require external professional review.

**Answer-check guidance.** A defensible solution shows its boundary, substitutions and units, not just the final numerical value. For a ±5% sensitivity, recompute the original equation at both input limits rather than automatically declaring the output to have the same percentage uncertainty. For evidence questions, name the actual sensor or log to examine and the expected sign of each competing effect. Qualitative trade-offs need a stated criterion—net export, fuel use, water, safety margin or total cost—rather than a vague ranking.

### 8. Research extension

Design a small, reproducible computational experiment about incident irradiance and AC derating. Define a physically reasonable input range and record why the range was chosen; collect a baseline output; sweep one independent variable; and export the results with units and assumptions. Explain where the educational calculator in this book is too simple for the proposed study. Contrast its output with published technology characterizations or a documented manufacturer's map *without copying proprietary material*. Include a limitations paragraph on extrapolation, scale effects and evidence quality. A negative finding, such as failure to improve net plant performance despite an attractive component calculation, is a valid outcome when the assumptions are clear.


---

# Unit 06, Lesson 04 — Geothermal and nuclear thermal boundaries

**Core topic:** thermal-source-to-electric conversion. **Representative relation:** `eta_thermal = P_e/Q_source`. **Case context:** geothermal brine loop and nuclear steam generator comparison.

The central question in this lesson is how to evaluate **thermal-source-to-electric conversion** when the engineer is given measurements from **geothermal brine loop and nuclear steam generator comparison**. First decide what quantity the result is supposed to describe. A thermodynamic component may have a local performance metric, while the whole plant has different inputs, outputs, auxiliaries and losses. Naming the metric prevents an apparently precise equation from addressing the wrong question. The representative relation is `eta_thermal = P_e/Q_source`. This expression is a teaching starting point, not a complete design specification. Before putting values into it, define every term, identify the device boundary, and write its units. Where a symbol can have multiple interpretations, the label on the measurement sheet must be explicit.

### 1. Physical interpretation and scope

The phenomenon in focus is **thermal-source-to-electric conversion**. In a grid region evaluating thermal station replacement, variable renewable support and flexible generation, a measured value will depend on the actual arrangement of equipment, the time interval over which it is averaged and the physical states entering each component. If an engineer isolates geothermal brine loop and nuclear steam generator comparison, the analysis should start by drawing arrows for all relevant energy or material streams and recording their directions. The next question is which measurements are direct and which come from a calculated property, manufacturer map, inferred coefficient or operational assumption. This distinction is more consequential than the number of decimal places in a spreadsheet.

A conservation equation and a constitutive relation serve different roles. Conservation says what the flows must sum to; a heat-transfer coefficient, turbomachinery efficiency, combustion model or empirical performance map helps explain how the flows divide in a specific design. When the calculation requires an unmeasured coefficient, report an explicit assumed range rather than disguising it as an observed constant. A reliable answer reports the sign of work and heat, the unit system and why a steady-state approximation is reasonable—or why it may be inadequate.

### 2. Derivation and use of the central relation

Begin with `eta_thermal = P_e/Q_source` and identify the physical quantity on each side. A useful calculation is dimensionally self-consistent: for example MW equals MJ/s, mass flow in kg/s times a specific energy in kJ/kg produces kW, and the ratio of energies or rates is dimensionless only when numerator and denominator use comparable bases. Temperatures added in a balance can be Celsius differences; temperatures divided in ideal-gas or second-law relations must use kelvin. Pressure ratios use absolute pressure; a gauge-pressure reading must be converted before use in a physical ratio.

For thermal-source-to-electric conversion, specify whether the result assumes constant properties, negligible kinetic-energy changes, no stored-energy rate, or a fixed device efficiency. Each of these is an engineering hypothesis that can be tested or relaxed. When working from field data, reduce readings in the order: raw instrument value, calibrated engineering unit, time alignment, derived state quantity, physical balance, performance ratio. This audit trail allows a second engineer to repeat the estimate.

A special caution in this lesson is that **heat-source availability and operational licensing differ fundamentally**. Explain exactly which algebraic term or measurement would be affected by that mistake. For a model with several serial components, a plausible local estimate may still be incompatible with the surrounding plant energy balance. Reconcile the result against the larger system. A model that demands more energy at the outlet than enters without storage, external work or a defined additional source should be rejected rather than patched by an unexplained correction factor.

### 3. Applied worked example — Geothermal and nuclear thermal boundaries

A thermal system receives 90 MW(th) and exports 25 MW(e). Its thermal-to-electric ratio is 25/90 = **27.78%** under the stated boundary. This value cannot establish whether the heat came from geothermal fluid, nuclear fission, concentrated solar heat or industrial waste heat, nor can it establish any source-specific safety conclusion.

**Verification and limitations.** Only source-specific professional studies can establish nuclear safety or geothermal sustainability. The result is illustrative and does not replace equipment-specific property data, measurements or professional review.

### 7. Exercises and discussion

1. **Derive.** Start from an explicit control volume for geothermal brine loop and nuclear steam generator comparison. Derive `eta_thermal = P_e/Q_source` or identify its idealizing assumptions. Label every term and check dimensional homogeneity.
2. **Calculate.** Construct an internally consistent SI example for thermal-source-to-electric conversion using values from a standard property table or clearly declared synthetic inputs. Calculate the nominal result and an output range when the dominant uncertain input is perturbed by ±5%.
3. **Diagnose.** A team reports an unexpected improvement while its fuel, electricity or fluid meters are undergoing maintenance. Form two measurement-error hypotheses and one physical-process hypothesis, then identify evidence that would discriminate among them.
4. **Compare.** Evaluate whether do not infer reactor safety, radiation risk or geothermal sustainability from cycle efficiency. Discuss at least one benefit, one new risk and a plant-level quantity that may offset the local benefit.
5. **Communicate.** Write a one-page engineering note distinguishing your numerical result, its assumptions, the source of each input, and the actions that require external professional review.

**Answer-check guidance.** A defensible solution shows its boundary, substitutions and units, not just the final numerical value. For a ±5% sensitivity, recompute the original equation at both input limits rather than automatically declaring the output to have the same percentage uncertainty. For evidence questions, name the actual sensor or log to examine and the expected sign of each competing effect. Qualitative trade-offs need a stated criterion—net export, fuel use, water, safety margin or total cost—rather than a vague ranking.

### 8. Research extension

Design a small, reproducible computational experiment about thermal-source-to-electric conversion. Define a physically reasonable input range and record why the range was chosen; collect a baseline output; sweep one independent variable; and export the results with units and assumptions. Explain where the educational calculator in this book is too simple for the proposed study. Contrast its output with published technology characterizations or a documented manufacturer's map *without copying proprietary material*. Include a limitations paragraph on extrapolation, scale effects and evidence quality. A negative finding, such as failure to improve net plant performance despite an attractive component calculation, is a valid outcome when the assumptions are clear.


---

# Unit 06, Lesson 05 — Hybrid storage, flexibility and capacity value

**Core topic:** duration and round-trip losses. **Representative relation:** `E_store = P_discharge*t_discharge`. **Case context:** solar plus battery and dispatchable reserve.

The central question in this lesson is how to evaluate **duration and round-trip losses** when the engineer is given measurements from **solar plus battery and dispatchable reserve**. First decide what quantity the result is supposed to describe. A thermodynamic component may have a local performance metric, while the whole plant has different inputs, outputs, auxiliaries and losses. Naming the metric prevents an apparently precise equation from addressing the wrong question. The representative relation is `E_store = P_discharge*t_discharge`. This expression is a teaching starting point, not a complete design specification. Before putting values into it, define every term, identify the device boundary, and write its units. Where a symbol can have multiple interpretations, the label on the measurement sheet must be explicit.

### 1. Physical interpretation and scope

The phenomenon in focus is **duration and round-trip losses**. In a grid region evaluating thermal station replacement, variable renewable support and flexible generation, a measured value will depend on the actual arrangement of equipment, the time interval over which it is averaged and the physical states entering each component. If an engineer isolates solar plus battery and dispatchable reserve, the analysis should start by drawing arrows for all relevant energy or material streams and recording their directions. The next question is which measurements are direct and which come from a calculated property, manufacturer map, inferred coefficient or operational assumption. This distinction is more consequential than the number of decimal places in a spreadsheet.

A conservation equation and a constitutive relation serve different roles. Conservation says what the flows must sum to; a heat-transfer coefficient, turbomachinery efficiency, combustion model or empirical performance map helps explain how the flows divide in a specific design. When the calculation requires an unmeasured coefficient, report an explicit assumed range rather than disguising it as an observed constant. A reliable answer reports the sign of work and heat, the unit system and why a steady-state approximation is reasonable—or why it may be inadequate.

### 2. Derivation and use of the central relation

Begin with `E_store = P_discharge*t_discharge` and identify the physical quantity on each side. A useful calculation is dimensionally self-consistent: for example MW equals MJ/s, mass flow in kg/s times a specific energy in kJ/kg produces kW, and the ratio of energies or rates is dimensionless only when numerator and denominator use comparable bases. Temperatures added in a balance can be Celsius differences; temperatures divided in ideal-gas or second-law relations must use kelvin. Pressure ratios use absolute pressure; a gauge-pressure reading must be converted before use in a physical ratio.

For duration and round-trip losses, specify whether the result assumes constant properties, negligible kinetic-energy changes, no stored-energy rate, or a fixed device efficiency. Each of these is an engineering hypothesis that can be tested or relaxed. When working from field data, reduce readings in the order: raw instrument value, calibrated engineering unit, time alignment, derived state quantity, physical balance, performance ratio. This audit trail allows a second engineer to repeat the estimate.

A special caution in this lesson is that **state-of-charge and efficiency constraints affect effective output**. Explain exactly which algebraic term or measurement would be affected by that mistake. For a model with several serial components, a plausible local estimate may still be incompatible with the surrounding plant energy balance. Reconcile the result against the larger system. A model that demands more energy at the outlet than enters without storage, external work or a defined additional source should be rejected rather than patched by an unexplained correction factor.

### 3. Applied worked example — Hybrid storage, flexibility and capacity value

A battery is rated 20 MW discharge power for four hours of its nominal usable energy. The ideal delivered energy is 20 × 4 = **80 MWh**. An 88% round-trip efficiency means that cycling 80 MWh of delivered energy requires approximately 80/0.88 = **90.9 MWh** charge input under the simplified model.

**Verification and limitations.** Energy storage shifts delivery time and has losses; it is not a generator of net energy. The result is illustrative and does not replace equipment-specific property data, measurements or professional review.

### 7. Exercises and discussion

1. **Derive.** Start from an explicit control volume for solar plus battery and dispatchable reserve. Derive `E_store = P_discharge*t_discharge` or identify its idealizing assumptions. Label every term and check dimensional homogeneity.
2. **Calculate.** Construct an internally consistent SI example for duration and round-trip losses using values from a standard property table or clearly declared synthetic inputs. Calculate the nominal result and an output range when the dominant uncertain input is perturbed by ±5%.
3. **Diagnose.** A team reports an unexpected improvement while its fuel, electricity or fluid meters are undergoing maintenance. Form two measurement-error hypotheses and one physical-process hypothesis, then identify evidence that would discriminate among them.
4. **Compare.** Evaluate whether storage shifts energy in time rather than creating net energy. Discuss at least one benefit, one new risk and a plant-level quantity that may offset the local benefit.
5. **Communicate.** Write a one-page engineering note distinguishing your numerical result, its assumptions, the source of each input, and the actions that require external professional review.

**Answer-check guidance.** A defensible solution shows its boundary, substitutions and units, not just the final numerical value. For a ±5% sensitivity, recompute the original equation at both input limits rather than automatically declaring the output to have the same percentage uncertainty. For evidence questions, name the actual sensor or log to examine and the expected sign of each competing effect. Qualitative trade-offs need a stated criterion—net export, fuel use, water, safety margin or total cost—rather than a vague ranking.

### 8. Research extension

Design a small, reproducible computational experiment about duration and round-trip losses. Define a physically reasonable input range and record why the range was chosen; collect a baseline output; sweep one independent variable; and export the results with units and assumptions. Explain where the educational calculator in this book is too simple for the proposed study. Contrast its output with published technology characterizations or a documented manufacturer's map *without copying proprietary material*. Include a limitations paragraph on extrapolation, scale effects and evidence quality. A negative finding, such as failure to improve net plant performance despite an attractive component calculation, is a valid outcome when the assumptions are clear.


---

