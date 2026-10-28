# Unit 02: Refrigeration Cycles and Thermodynamic Performance

**Course Code**: RAC 302 · **Level**: Advanced Undergraduate Engineering

## Unit Overview & Physical Foundations

This comprehensive university textbook unit covers the theoretical framework, physical modeling, mathematical governing equations, and engineering applications of **Refrigeration Cycles and Thermodynamic Performance**.

## U02-L01 — Vapor-compression cycle states

**Outcome:** Interpret vapor-compression cycle states, perform a traceable estimate, diagnose a limitation, and explain how evidence could change the associated engineering decision.

### 1. Engineering problem and purpose

A refrigeration system must keep a cold room below ambient temperature. The designer compares its useful evaporator heat absorption with compressor input power and rejects comparisons made at different evaporating temperatures. The specific issue here is **vapor-compression cycle states**. Apply first- and second-law reasoning to ideal and actual vapor-compression and alternative refrigeration cycles. This problem matters because a mechanical design must perform across several operating states rather than just one conveniently chosen measurement. A useful first result is a quantity with clear units, an identified system boundary and a stated purpose; it is not a prediction for arbitrary buildings or products.

### 2. Governing idea and modeling assumptions

**Working relation:** `q_e = h_1−h_4; w_c = h_2−h_1`.

This equation should be interpreted together with its reference states. Write down every independent variable, with its numerical units, and keep any temperature-difference term separate from an absolute thermodynamic temperature. For a steady-flow energy equation, indicate the mass-flow definition; for a moist-air relation, specify whether the denominator is dry-air mass; for a performance ratio, ensure numerator and denominator cover the same test period. If the result is dimensionless, explain what physical quantities were compared.

State identification depends on pressure and refrigerant property evaluation; tabulated enthalpy values here are fictional. This is a reason to retain the equation's scope in every answer. A classroom relation may assume ideal-gas behavior, constant specific heat, steady mass balance, uniform mixing, negligible leakage, or a fixed equipment efficiency. Real systems can violate several of these assumptions simultaneously, particularly during a changing load. The correct response is to identify the assumption and collect appropriate evidence, rather than silently adding correction factors whose source is unclear.

### 3. Fully specified numerical teaching example

**Assumed inputs and computed answer:** For h1=398, h4=248 and h2=435 kJ/kg, evaporator uptake is 150 kJ/kg and compressor work is 37 kJ/kg.

Reproduce the result using the equation rather than copying the displayed answer. Convert all values to compatible units before substitution. Distinguish kW from kWh, kPa from Pa, and a percentage from a dimensionless fraction. Then perform three small checks: does the output have the expected dimensions, is its sign physically meaningful for the chosen reference direction, and does it approach a sensible limiting value when the driving difference or mass flow tends toward zero? If a limiting case gives a contradiction, examine the equation and model boundary before trusting the decimals.

### 4. Physical interpretation and failure analysis

The immediate diagnostic trap in this lesson is the following: State identification depends on pressure and refrigerant property evaluation; tabulated enthalpy values here are fictional. Construct a counterexample where the displayed calculation remains arithmetically correct but no longer explains the actual operating behavior. Identify which state variable or energy stream has been excluded, whether the error would tend to make the prediction high or low, and which observation could reveal the discrepancy. Where the sign of the discrepancy depends on coupled effects, give both plausible directions instead of selecting one without evidence.

### 5. Measurement and independent verification

**Suggested evidence:** Use independently measured suction/discharge pressure and temperature with verified property data. Define instrument location, calibration state, sample rate, expected operating condition and averaging period. Record the physical configuration, controller state, weather or ambient condition and any recent service changes. Establish a repeated baseline where practical; a one-off value can be distorted by transient heat storage or instrument delay. Preserve raw observations separately from processed plots so a different analyst can independently reproduce the result.

For uncertainty, start with a bounded input sensitivity calculation. Identify the most influential parameter and estimate how its uncertainty propagates through the working relation. If the input depends on other measured quantities, note their correlation instead of automatically treating errors as independent. Keep the measurement units and calibration references attached to each row in the results table. A plotted model curve is not experimental data; if both are presented, label them differently and show measurement points with their uncertainty where available.

### 6. Design choice and engineering trade-offs

**Decision problem:** Close both mass and energy balances before judging a cycle improvement. Translate this into a decision matrix with at least one primary performance measure and one hard constraint. State whether the option is being evaluated for capacity, comfort, electricity consumption, reliability, lifecycle cost or emissions. Some options improve one objective while increasing fan power, refrigerant charge, maintenance burden or control complexity. Do not call the option superior without declaring the weighted objective or the nonnegotiable constraint.

### 7. Practice and assessment

1. **Concept:** Explain the physical meaning of `q_e = h_1−h_4; w_c = h_2−h_1` and identify at least two assumptions necessary for its use.
2. **Numerical:** Repeat the example with all units shown: For h1=398, h4=248 and h2=435 kJ/kg, evaporator uptake is 150 kJ/kg and compressor work is 37 kJ/kg. State an answer at a precision justified by the input values.
4. **Diagnosis:** Design a plausible scenario in which the original result is misleading because of: State identification depends on pressure and refrigerant property evaluation; tabulated enthalpy values here are fictional. Specify an independent observation to test the explanation.
5. **Experiment:** Convert the suggested verification into a small data-collection plan: Use independently measured suction/discharge pressure and temperature with verified property data.
6. **Decision:** Defend a recommendation using the lesson's trade-off: Close both mass and energy balances before judging a cycle improvement. Identify one operating condition that might reverse your conclusion.

**Checking rubric:** Give credit for a correct model boundary and quantities, transparent unit conversion, dimensional reasonableness, explicit limitations and a falsifiable verification strategy. Do not award full credit for copying a plausible-looking number without explaining what it measures. For an open-ended design response, alternative answers may be valid when their constraints and evidence are coherent.


---

## U02-L02 — Coefficient of performance and limitations

**Outcome:** Interpret coefficient of performance and limitations, perform a traceable estimate, diagnose a limitation, and explain how evidence could change the associated engineering decision.

### 1. Engineering problem and purpose

A refrigeration system must keep a cold room below ambient temperature. The designer compares its useful evaporator heat absorption with compressor input power and rejects comparisons made at different evaporating temperatures. The specific issue here is **coefficient of performance and limitations**. Apply first- and second-law reasoning to ideal and actual vapor-compression and alternative refrigeration cycles. This problem matters because a mechanical design must perform across several operating states rather than just one conveniently chosen measurement. A useful first result is a quantity with clear units, an identified system boundary and a stated purpose; it is not a prediction for arbitrary buildings or products.

### 2. Governing idea and modeling assumptions

**Working relation:** `COP_R = Q_L/W_in`.

This equation should be interpreted together with its reference states. Write down every independent variable, with its numerical units, and keep any temperature-difference term separate from an absolute thermodynamic temperature. For a steady-flow energy equation, indicate the mass-flow definition; for a moist-air relation, specify whether the denominator is dry-air mass; for a performance ratio, ensure numerator and denominator cover the same test period. If the result is dimensionless, explain what physical quantities were compared.

An evaporator-cycle COP, compressor-only COP and whole-system electrical COP cannot be compared without equal boundaries. This is a reason to retain the equation's scope in every answer. A classroom relation may assume ideal-gas behavior, constant specific heat, steady mass balance, uniform mixing, negligible leakage, or a fixed equipment efficiency. Real systems can violate several of these assumptions simultaneously, particularly during a changing load. The correct response is to identify the assumption and collect appropriate evidence, rather than silently adding correction factors whose source is unclear.

### 3. Fully specified numerical teaching example

**Assumed inputs and computed answer:** A system delivering 7.5 kW cooling while consuming 2.5 kW electrical input has an observed system COP of 3.0 if measurement boundaries match.

Reproduce the result using the equation rather than copying the displayed answer. Convert all values to compatible units before substitution. Distinguish kW from kWh, kPa from Pa, and a percentage from a dimensionless fraction. Then perform three small checks: does the output have the expected dimensions, is its sign physically meaningful for the chosen reference direction, and does it approach a sensible limiting value when the driving difference or mass flow tends toward zero? If a limiting case gives a contradiction, examine the equation and model boundary before trusting the decimals.

### 4. Physical interpretation and failure analysis

The immediate diagnostic trap in this lesson is the following: An evaporator-cycle COP, compressor-only COP and whole-system electrical COP cannot be compared without equal boundaries. Construct a counterexample where the displayed calculation remains arithmetically correct but no longer explains the actual operating behavior. Identify which state variable or energy stream has been excluded, whether the error would tend to make the prediction high or low, and which observation could reveal the discrepancy. Where the sign of the discrepancy depends on coupled effects, give both plausible directions instead of selecting one without evidence.

### 5. Measurement and independent verification

**Suggested evidence:** Record power to fans, pumps, defrost and auxiliaries as the chosen boundary requires. Define instrument location, calibration state, sample rate, expected operating condition and averaging period. Record the physical configuration, controller state, weather or ambient condition and any recent service changes. Establish a repeated baseline where practical; a one-off value can be distorted by transient heat storage or instrument delay. Preserve raw observations separately from processed plots so a different analyst can independently reproduce the result.

For uncertainty, start with a bounded input sensitivity calculation. Identify the most influential parameter and estimate how its uncertainty propagates through the working relation. If the input depends on other measured quantities, note their correlation instead of automatically treating errors as independent. Keep the measurement units and calibration references attached to each row in the results table. A plotted model curve is not experimental data; if both are presented, label them differently and show measurement points with their uncertainty where available.

### 6. Design choice and engineering trade-offs

**Decision problem:** Use a measured duty profile rather than one favorable operating point. Translate this into a decision matrix with at least one primary performance measure and one hard constraint. State whether the option is being evaluated for capacity, comfort, electricity consumption, reliability, lifecycle cost or emissions. Some options improve one objective while increasing fan power, refrigerant charge, maintenance burden or control complexity. Do not call the option superior without declaring the weighted objective or the nonnegotiable constraint.

### 7. Practice and assessment

1. **Concept:** Explain the physical meaning of `COP_R = Q_L/W_in` and identify at least two assumptions necessary for its use.
2. **Numerical:** Repeat the example with all units shown: A system delivering 7.5 kW cooling while consuming 2.5 kW electrical input has an observed system COP of 3.0 if measurement boundaries match. State an answer at a precision justified by the input values.
4. **Diagnosis:** Design a plausible scenario in which the original result is misleading because of: An evaporator-cycle COP, compressor-only COP and whole-system electrical COP cannot be compared without equal boundaries. Specify an independent observation to test the explanation.
5. **Experiment:** Convert the suggested verification into a small data-collection plan: Record power to fans, pumps, defrost and auxiliaries as the chosen boundary requires.
6. **Decision:** Defend a recommendation using the lesson's trade-off: Use a measured duty profile rather than one favorable operating point. Identify one operating condition that might reverse your conclusion.

**Checking rubric:** Give credit for a correct model boundary and quantities, transparent unit conversion, dimensional reasonableness, explicit limitations and a falsifiable verification strategy. Do not award full credit for copying a plausible-looking number without explaining what it measures. For an open-ended design response, alternative answers may be valid when their constraints and evidence are coherent.


---

## U02-L03 — Carnot cooling benchmark

**Outcome:** Interpret carnot cooling benchmark, perform a traceable estimate, diagnose a limitation, and explain how evidence could change the associated engineering decision.

### 1. Engineering problem and purpose

A refrigeration system must keep a cold room below ambient temperature. The designer compares its useful evaporator heat absorption with compressor input power and rejects comparisons made at different evaporating temperatures. The specific issue here is **carnot cooling benchmark**. Apply first- and second-law reasoning to ideal and actual vapor-compression and alternative refrigeration cycles. This problem matters because a mechanical design must perform across several operating states rather than just one conveniently chosen measurement. A useful first result is a quantity with clear units, an identified system boundary and a stated purpose; it is not a prediction for arbitrary buildings or products.

### 2. Governing idea and modeling assumptions

**Working relation:** `COP_R,Carnot = T_c/(T_h−T_c) using absolute kelvin`.

This equation should be interpreted together with its reference states. Write down every independent variable, with its numerical units, and keep any temperature-difference term separate from an absolute thermodynamic temperature. For a steady-flow energy equation, indicate the mass-flow definition; for a moist-air relation, specify whether the denominator is dry-air mass; for a performance ratio, ensure numerator and denominator cover the same test period. If the result is dimensionless, explain what physical quantities were compared.

The benchmark is not an achievable catalog rating and says nothing about particular hardware performance. This is a reason to retain the equation's scope in every answer. A classroom relation may assume ideal-gas behavior, constant specific heat, steady mass balance, uniform mixing, negligible leakage, or a fixed equipment efficiency. Real systems can violate several of these assumptions simultaneously, particularly during a changing load. The correct response is to identify the assumption and collect appropriate evidence, rather than silently adding correction factors whose source is unclear.

### 3. Fully specified numerical teaching example

**Assumed inputs and computed answer:** Between 278 K and 308 K the reversible refrigerator COP benchmark is 9.27.

Reproduce the result using the equation rather than copying the displayed answer. Convert all values to compatible units before substitution. Distinguish kW from kWh, kPa from Pa, and a percentage from a dimensionless fraction. Then perform three small checks: does the output have the expected dimensions, is its sign physically meaningful for the chosen reference direction, and does it approach a sensible limiting value when the driving difference or mass flow tends toward zero? If a limiting case gives a contradiction, examine the equation and model boundary before trusting the decimals.

### 4. Physical interpretation and failure analysis

The immediate diagnostic trap in this lesson is the following: The benchmark is not an achievable catalog rating and says nothing about particular hardware performance. Construct a counterexample where the displayed calculation remains arithmetically correct but no longer explains the actual operating behavior. Identify which state variable or energy stream has been excluded, whether the error would tend to make the prediction high or low, and which observation could reveal the discrepancy. Where the sign of the discrepancy depends on coupled effects, give both plausible directions instead of selecting one without evidence.

### 5. Measurement and independent verification

**Suggested evidence:** Compare actual temperature approach differences and compressor pressure ratio over several conditions. Define instrument location, calibration state, sample rate, expected operating condition and averaging period. Record the physical configuration, controller state, weather or ambient condition and any recent service changes. Establish a repeated baseline where practical; a one-off value can be distorted by transient heat storage or instrument delay. Preserve raw observations separately from processed plots so a different analyst can independently reproduce the result.

For uncertainty, start with a bounded input sensitivity calculation. Identify the most influential parameter and estimate how its uncertainty propagates through the working relation. If the input depends on other measured quantities, note their correlation instead of automatically treating errors as independent. Keep the measurement units and calibration references attached to each row in the results table. A plotted model curve is not experimental data; if both are presented, label them differently and show measurement points with their uncertainty where available.

### 6. Design choice and engineering trade-offs

**Decision problem:** Explain why finite heat exchanger temperature differences reduce attainable COP. Translate this into a decision matrix with at least one primary performance measure and one hard constraint. State whether the option is being evaluated for capacity, comfort, electricity consumption, reliability, lifecycle cost or emissions. Some options improve one objective while increasing fan power, refrigerant charge, maintenance burden or control complexity. Do not call the option superior without declaring the weighted objective or the nonnegotiable constraint.

### 7. Practice and assessment

1. **Concept:** Explain the physical meaning of `COP_R,Carnot = T_c/(T_h−T_c) using absolute kelvin` and identify at least two assumptions necessary for its use.
2. **Numerical:** Repeat the example with all units shown: Between 278 K and 308 K the reversible refrigerator COP benchmark is 9.27. State an answer at a precision justified by the input values.
4. **Diagnosis:** Design a plausible scenario in which the original result is misleading because of: The benchmark is not an achievable catalog rating and says nothing about particular hardware performance. Specify an independent observation to test the explanation.
5. **Experiment:** Convert the suggested verification into a small data-collection plan: Compare actual temperature approach differences and compressor pressure ratio over several conditions.
6. **Decision:** Defend a recommendation using the lesson's trade-off: Explain why finite heat exchanger temperature differences reduce attainable COP. Identify one operating condition that might reverse your conclusion.

**Checking rubric:** Give credit for a correct model boundary and quantities, transparent unit conversion, dimensional reasonableness, explicit limitations and a falsifiable verification strategy. Do not award full credit for copying a plausible-looking number without explaining what it measures. For an open-ended design response, alternative answers may be valid when their constraints and evidence are coherent.


---

## U02-L04 — Throttling, expansion and superheat

**Outcome:** Interpret throttling, expansion and superheat, perform a traceable estimate, diagnose a limitation, and explain how evidence could change the associated engineering decision.

### 1. Engineering problem and purpose

A refrigeration system must keep a cold room below ambient temperature. The designer compares its useful evaporator heat absorption with compressor input power and rejects comparisons made at different evaporating temperatures. The specific issue here is **throttling, expansion and superheat**. Apply first- and second-law reasoning to ideal and actual vapor-compression and alternative refrigeration cycles. This problem matters because a mechanical design must perform across several operating states rather than just one conveniently chosen measurement. A useful first result is a quantity with clear units, an identified system boundary and a stated purpose; it is not a prediction for arbitrary buildings or products.

### 2. Governing idea and modeling assumptions

**Working relation:** `h_4 ≈ h_3 across an adiabatic throttling valve`.

This equation should be interpreted together with its reference states. Write down every independent variable, with its numerical units, and keep any temperature-difference term separate from an absolute thermodynamic temperature. For a steady-flow energy equation, indicate the mass-flow definition; for a moist-air relation, specify whether the denominator is dry-air mass; for a performance ratio, ensure numerator and denominator cover the same test period. If the result is dimensionless, explain what physical quantities were compared.

A throttling valve is not a turbine; enthalpy staying approximately constant does not imply temperature is constant. This is a reason to retain the equation's scope in every answer. A classroom relation may assume ideal-gas behavior, constant specific heat, steady mass balance, uniform mixing, negligible leakage, or a fixed equipment efficiency. Real systems can violate several of these assumptions simultaneously, particularly during a changing load. The correct response is to identify the assumption and collect appropriate evidence, rather than silently adding correction factors whose source is unclear.

### 3. Fully specified numerical teaching example

**Assumed inputs and computed answer:** If a liquid leaves the condenser with h3=245 kJ/kg, the ideal throttling estimate sets h4=245 kJ/kg even though pressure falls.

Reproduce the result using the equation rather than copying the displayed answer. Convert all values to compatible units before substitution. Distinguish kW from kWh, kPa from Pa, and a percentage from a dimensionless fraction. Then perform three small checks: does the output have the expected dimensions, is its sign physically meaningful for the chosen reference direction, and does it approach a sensible limiting value when the driving difference or mass flow tends toward zero? If a limiting case gives a contradiction, examine the equation and model boundary before trusting the decimals.

### 4. Physical interpretation and failure analysis

The immediate diagnostic trap in this lesson is the following: A throttling valve is not a turbine; enthalpy staying approximately constant does not imply temperature is constant. Construct a counterexample where the displayed calculation remains arithmetically correct but no longer explains the actual operating behavior. Identify which state variable or energy stream has been excluded, whether the error would tend to make the prediction high or low, and which observation could reveal the discrepancy. Where the sign of the discrepancy depends on coupled effects, give both plausible directions instead of selecting one without evidence.

### 5. Measurement and independent verification

**Suggested evidence:** Observe valve inlet state and evaporator outlet superheat using properly calibrated instrumentation. Define instrument location, calibration state, sample rate, expected operating condition and averaging period. Record the physical configuration, controller state, weather or ambient condition and any recent service changes. Establish a repeated baseline where practical; a one-off value can be distorted by transient heat storage or instrument delay. Preserve raw observations separately from processed plots so a different analyst can independently reproduce the result.

For uncertainty, start with a bounded input sensitivity calculation. Identify the most influential parameter and estimate how its uncertainty propagates through the working relation. If the input depends on other measured quantities, note their correlation instead of automatically treating errors as independent. Keep the measurement units and calibration references attached to each row in the results table. A plotted model curve is not experimental data; if both are presented, label them differently and show measurement points with their uncertainty where available.

### 6. Design choice and engineering trade-offs

**Decision problem:** Select superheat targets only with equipment-specific safeguards and manufacturer data. Translate this into a decision matrix with at least one primary performance measure and one hard constraint. State whether the option is being evaluated for capacity, comfort, electricity consumption, reliability, lifecycle cost or emissions. Some options improve one objective while increasing fan power, refrigerant charge, maintenance burden or control complexity. Do not call the option superior without declaring the weighted objective or the nonnegotiable constraint.

### 7. Practice and assessment

1. **Concept:** Explain the physical meaning of `h_4 ≈ h_3 across an adiabatic throttling valve` and identify at least two assumptions necessary for its use.
2. **Numerical:** Repeat the example with all units shown: If a liquid leaves the condenser with h3=245 kJ/kg, the ideal throttling estimate sets h4=245 kJ/kg even though pressure falls. State an answer at a precision justified by the input values.
4. **Diagnosis:** Design a plausible scenario in which the original result is misleading because of: A throttling valve is not a turbine; enthalpy staying approximately constant does not imply temperature is constant. Specify an independent observation to test the explanation.
5. **Experiment:** Convert the suggested verification into a small data-collection plan: Observe valve inlet state and evaporator outlet superheat using properly calibrated instrumentation.
6. **Decision:** Defend a recommendation using the lesson's trade-off: Select superheat targets only with equipment-specific safeguards and manufacturer data. Identify one operating condition that might reverse your conclusion.

**Checking rubric:** Give credit for a correct model boundary and quantities, transparent unit conversion, dimensional reasonableness, explicit limitations and a falsifiable verification strategy. Do not award full credit for copying a plausible-looking number without explaining what it measures. For an open-ended design response, alternative answers may be valid when their constraints and evidence are coherent.


---

## U02-L05 — Heat pumps, reversibility and second law

**Outcome:** Interpret heat pumps, reversibility and second law, perform a traceable estimate, diagnose a limitation, and explain how evidence could change the associated engineering decision.

### 1. Engineering problem and purpose

A refrigeration system must keep a cold room below ambient temperature. The designer compares its useful evaporator heat absorption with compressor input power and rejects comparisons made at different evaporating temperatures. The specific issue here is **heat pumps, reversibility and second law**. Apply first- and second-law reasoning to ideal and actual vapor-compression and alternative refrigeration cycles. This problem matters because a mechanical design must perform across several operating states rather than just one conveniently chosen measurement. A useful first result is a quantity with clear units, an identified system boundary and a stated purpose; it is not a prediction for arbitrary buildings or products.

### 2. Governing idea and modeling assumptions

**Working relation:** `COP_HP = COP_R+1 when identical boundaries and the same ideal cycle are used`.

This equation should be interpreted together with its reference states. Write down every independent variable, with its numerical units, and keep any temperature-difference term separate from an absolute thermodynamic temperature. For a steady-flow energy equation, indicate the mass-flow definition; for a moist-air relation, specify whether the denominator is dry-air mass; for a performance ratio, ensure numerator and denominator cover the same test period. If the result is dimensionless, explain what physical quantities were compared.

Defrost energy and auxiliary heaters invalidate an unqualified ideal relationship for real seasonal data. This is a reason to retain the equation's scope in every answer. A classroom relation may assume ideal-gas behavior, constant specific heat, steady mass balance, uniform mixing, negligible leakage, or a fixed equipment efficiency. Real systems can violate several of these assumptions simultaneously, particularly during a changing load. The correct response is to identify the assumption and collect appropriate evidence, rather than silently adding correction factors whose source is unclear.

### 3. Fully specified numerical teaching example

**Assumed inputs and computed answer:** If an idealized heat pump removes 6 kW from the outdoor source and needs 2 kW of work, heating delivered is 8 kW and heating COP is 4.

Reproduce the result using the equation rather than copying the displayed answer. Convert all values to compatible units before substitution. Distinguish kW from kWh, kPa from Pa, and a percentage from a dimensionless fraction. Then perform three small checks: does the output have the expected dimensions, is its sign physically meaningful for the chosen reference direction, and does it approach a sensible limiting value when the driving difference or mass flow tends toward zero? If a limiting case gives a contradiction, examine the equation and model boundary before trusting the decimals.

### 4. Physical interpretation and failure analysis

The immediate diagnostic trap in this lesson is the following: Defrost energy and auxiliary heaters invalidate an unqualified ideal relationship for real seasonal data. Construct a counterexample where the displayed calculation remains arithmetically correct but no longer explains the actual operating behavior. Identify which state variable or energy stream has been excluded, whether the error would tend to make the prediction high or low, and which observation could reveal the discrepancy. Where the sign of the discrepancy depends on coupled effects, give both plausible directions instead of selecting one without evidence.

### 5. Measurement and independent verification

**Suggested evidence:** Measure delivered heating, electrical energy and defrost/backup operation separately. Define instrument location, calibration state, sample rate, expected operating condition and averaging period. Record the physical configuration, controller state, weather or ambient condition and any recent service changes. Establish a repeated baseline where practical; a one-off value can be distorted by transient heat storage or instrument delay. Preserve raw observations separately from processed plots so a different analyst can independently reproduce the result.

For uncertainty, start with a bounded input sensitivity calculation. Identify the most influential parameter and estimate how its uncertainty propagates through the working relation. If the input depends on other measured quantities, note their correlation instead of automatically treating errors as independent. Keep the measurement units and calibration references attached to each row in the results table. A plotted model curve is not experimental data; if both are presented, label them differently and show measurement points with their uncertainty where available.

### 6. Design choice and engineering trade-offs

**Decision problem:** Compare heating duty at the lowest design ambient temperature, not only mild weather. Translate this into a decision matrix with at least one primary performance measure and one hard constraint. State whether the option is being evaluated for capacity, comfort, electricity consumption, reliability, lifecycle cost or emissions. Some options improve one objective while increasing fan power, refrigerant charge, maintenance burden or control complexity. Do not call the option superior without declaring the weighted objective or the nonnegotiable constraint.

### 7. Practice and assessment

1. **Concept:** Explain the physical meaning of `COP_HP = COP_R+1 when identical boundaries and the same ideal cycle are used` and identify at least two assumptions necessary for its use.
2. **Numerical:** Repeat the example with all units shown: If an idealized heat pump removes 6 kW from the outdoor source and needs 2 kW of work, heating delivered is 8 kW and heating COP is 4. State an answer at a precision justified by the input values.
4. **Diagnosis:** Design a plausible scenario in which the original result is misleading because of: Defrost energy and auxiliary heaters invalidate an unqualified ideal relationship for real seasonal data. Specify an independent observation to test the explanation.
5. **Experiment:** Convert the suggested verification into a small data-collection plan: Measure delivered heating, electrical energy and defrost/backup operation separately.
6. **Decision:** Defend a recommendation using the lesson's trade-off: Compare heating duty at the lowest design ambient temperature, not only mild weather. Identify one operating condition that might reverse your conclusion.

**Checking rubric:** Give credit for a correct model boundary and quantities, transparent unit conversion, dimensional reasonableness, explicit limitations and a falsifiable verification strategy. Do not award full credit for copying a plausible-looking number without explaining what it measures. For an open-ended design response, alternative answers may be valid when their constraints and evidence are coherent.


---

