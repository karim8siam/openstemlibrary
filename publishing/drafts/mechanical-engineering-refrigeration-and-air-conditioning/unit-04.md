# Unit 04: Moist Air, Psychrometrics and Air Treatment

**Course Code**: RAC 304 · **Level**: Advanced Undergraduate Engineering

## Unit Overview & Physical Foundations

This comprehensive university textbook unit covers the theoretical framework, physical modeling, mathematical governing equations, and engineering applications of **Moist Air, Psychrometrics and Air Treatment**.

## U04-L01 — Humidity ratio and vapor partial pressure

**Outcome:** Interpret humidity ratio and vapor partial pressure, perform a traceable estimate, diagnose a limitation, and explain how evidence could change the associated engineering decision.

### 1. Engineering problem and purpose

An air handler mixes outdoor and return air, cools it, removes condensed water, and supplies air to a classroom. Wet-bulb, humidity ratio and coil bypass effects all influence comfort. The specific issue here is **humidity ratio and vapor partial pressure**. Calculate moist-air properties and distinguish sensible heating/cooling from latent moisture removal. This problem matters because a mechanical design must perform across several operating states rather than just one conveniently chosen measurement. A useful first result is a quantity with clear units, an identified system boundary and a stated purpose; it is not a prediction for arbitrary buildings or products.

### 2. Governing idea and modeling assumptions

**Working relation:** `w = 0.62198 p_v/(P−p_v)`.

This equation should be interpreted together with its reference states. Write down every independent variable, with its numerical units, and keep any temperature-difference term separate from an absolute thermodynamic temperature. For a steady-flow energy equation, indicate the mass-flow definition; for a moist-air relation, specify whether the denominator is dry-air mass; for a performance ratio, ensure numerator and denominator cover the same test period. If the result is dimensionless, explain what physical quantities were compared.

Humidity ratio is mass per dry-air mass; it is not equal to relative humidity or mass fraction of total air. This is a reason to retain the equation's scope in every answer. A classroom relation may assume ideal-gas behavior, constant specific heat, steady mass balance, uniform mixing, negligible leakage, or a fixed equipment efficiency. Real systems can violate several of these assumptions simultaneously, particularly during a changing load. The correct response is to identify the assumption and collect appropriate evidence, rather than silently adding correction factors whose source is unclear.

### 3. Fully specified numerical teaching example

**Assumed inputs and computed answer:** With total pressure 101.3 kPa and water-vapor partial pressure 2.0 kPa, humidity ratio is approximately 0.0125 kg water/kg dry air.

Reproduce the result using the equation rather than copying the displayed answer. Convert all values to compatible units before substitution. Distinguish kW from kWh, kPa from Pa, and a percentage from a dimensionless fraction. Then perform three small checks: does the output have the expected dimensions, is its sign physically meaningful for the chosen reference direction, and does it approach a sensible limiting value when the driving difference or mass flow tends toward zero? If a limiting case gives a contradiction, examine the equation and model boundary before trusting the decimals.

### 4. Physical interpretation and failure analysis

The immediate diagnostic trap in this lesson is the following: Humidity ratio is mass per dry-air mass; it is not equal to relative humidity or mass fraction of total air. Construct a counterexample where the displayed calculation remains arithmetically correct but no longer explains the actual operating behavior. Identify which state variable or energy stream has been excluded, whether the error would tend to make the prediction high or low, and which observation could reveal the discrepancy. Where the sign of the discrepancy depends on coupled effects, give both plausible directions instead of selecting one without evidence.

### 5. Measurement and independent verification

**Suggested evidence:** Pair humidity sensors with temperature and barometric pressure; calibrate against appropriate references. Define instrument location, calibration state, sample rate, expected operating condition and averaging period. Record the physical configuration, controller state, weather or ambient condition and any recent service changes. Establish a repeated baseline where practical; a one-off value can be distorted by transient heat storage or instrument delay. Preserve raw observations separately from processed plots so a different analyst can independently reproduce the result.

For uncertainty, start with a bounded input sensitivity calculation. Identify the most influential parameter and estimate how its uncertainty propagates through the working relation. If the input depends on other measured quantities, note their correlation instead of automatically treating errors as independent. Keep the measurement units and calibration references attached to each row in the results table. A plotted model curve is not experimental data; if both are presented, label them differently and show measurement points with their uncertainty where available.

### 6. Design choice and engineering trade-offs

**Decision problem:** Use moisture mass balances for mixed-air problems rather than averaging relative humidity. Translate this into a decision matrix with at least one primary performance measure and one hard constraint. State whether the option is being evaluated for capacity, comfort, electricity consumption, reliability, lifecycle cost or emissions. Some options improve one objective while increasing fan power, refrigerant charge, maintenance burden or control complexity. Do not call the option superior without declaring the weighted objective or the nonnegotiable constraint.

### 7. Practice and assessment

1. **Concept:** Explain the physical meaning of `w = 0.62198 p_v/(P−p_v)` and identify at least two assumptions necessary for its use.
2. **Numerical:** Repeat the example with all units shown: With total pressure 101.3 kPa and water-vapor partial pressure 2.0 kPa, humidity ratio is approximately 0.0125 kg water/kg dry air. State an answer at a precision justified by the input values.
4. **Diagnosis:** Design a plausible scenario in which the original result is misleading because of: Humidity ratio is mass per dry-air mass; it is not equal to relative humidity or mass fraction of total air. Specify an independent observation to test the explanation.
5. **Experiment:** Convert the suggested verification into a small data-collection plan: Pair humidity sensors with temperature and barometric pressure; calibrate against appropriate references.
6. **Decision:** Defend a recommendation using the lesson's trade-off: Use moisture mass balances for mixed-air problems rather than averaging relative humidity. Identify one operating condition that might reverse your conclusion.

**Checking rubric:** Give credit for a correct model boundary and quantities, transparent unit conversion, dimensional reasonableness, explicit limitations and a falsifiable verification strategy. Do not award full credit for copying a plausible-looking number without explaining what it measures. For an open-ended design response, alternative answers may be valid when their constraints and evidence are coherent.


---

## U04-L02 — Relative humidity and saturation

**Outcome:** Interpret relative humidity and saturation, perform a traceable estimate, diagnose a limitation, and explain how evidence could change the associated engineering decision.

### 1. Engineering problem and purpose

An air handler mixes outdoor and return air, cools it, removes condensed water, and supplies air to a classroom. Wet-bulb, humidity ratio and coil bypass effects all influence comfort. The specific issue here is **relative humidity and saturation**. Calculate moist-air properties and distinguish sensible heating/cooling from latent moisture removal. This problem matters because a mechanical design must perform across several operating states rather than just one conveniently chosen measurement. A useful first result is a quantity with clear units, an identified system boundary and a stated purpose; it is not a prediction for arbitrary buildings or products.

### 2. Governing idea and modeling assumptions

**Working relation:** `phi = p_v/p_sat(T) for idealized moist air`.

This equation should be interpreted together with its reference states. Write down every independent variable, with its numerical units, and keep any temperature-difference term separate from an absolute thermodynamic temperature. For a steady-flow energy equation, indicate the mass-flow definition; for a moist-air relation, specify whether the denominator is dry-air mass; for a performance ratio, ensure numerator and denominator cover the same test period. If the result is dimensionless, explain what physical quantities were compared.

The saturation pressure changes strongly with temperature, so warming air reduces relative humidity without removing water. This is a reason to retain the equation's scope in every answer. A classroom relation may assume ideal-gas behavior, constant specific heat, steady mass balance, uniform mixing, negligible leakage, or a fixed equipment efficiency. Real systems can violate several of these assumptions simultaneously, particularly during a changing load. The correct response is to identify the assumption and collect appropriate evidence, rather than silently adding correction factors whose source is unclear.

### 3. Fully specified numerical teaching example

**Assumed inputs and computed answer:** At 25 °C and saturation vapor pressure about 3.17 kPa, partial pressure of 1.585 kPa corresponds to roughly 50% relative humidity.

Reproduce the result using the equation rather than copying the displayed answer. Convert all values to compatible units before substitution. Distinguish kW from kWh, kPa from Pa, and a percentage from a dimensionless fraction. Then perform three small checks: does the output have the expected dimensions, is its sign physically meaningful for the chosen reference direction, and does it approach a sensible limiting value when the driving difference or mass flow tends toward zero? If a limiting case gives a contradiction, examine the equation and model boundary before trusting the decimals.

### 4. Physical interpretation and failure analysis

The immediate diagnostic trap in this lesson is the following: The saturation pressure changes strongly with temperature, so warming air reduces relative humidity without removing water. Construct a counterexample where the displayed calculation remains arithmetically correct but no longer explains the actual operating behavior. Identify which state variable or energy stream has been excluded, whether the error would tend to make the prediction high or low, and which observation could reveal the discrepancy. Where the sign of the discrepancy depends on coupled effects, give both plausible directions instead of selecting one without evidence.

### 5. Measurement and independent verification

**Suggested evidence:** Observe dew point and dry-bulb together during a heating-only test. Define instrument location, calibration state, sample rate, expected operating condition and averaging period. Record the physical configuration, controller state, weather or ambient condition and any recent service changes. Establish a repeated baseline where practical; a one-off value can be distorted by transient heat storage or instrument delay. Preserve raw observations separately from processed plots so a different analyst can independently reproduce the result.

For uncertainty, start with a bounded input sensitivity calculation. Identify the most influential parameter and estimate how its uncertainty propagates through the working relation. If the input depends on other measured quantities, note their correlation instead of automatically treating errors as independent. Keep the measurement units and calibration references attached to each row in the results table. A plotted model curve is not experimental data; if both are presented, label them differently and show measurement points with their uncertainty where available.

### 6. Design choice and engineering trade-offs

**Decision problem:** Select controls that can independently manage humidity when required. Translate this into a decision matrix with at least one primary performance measure and one hard constraint. State whether the option is being evaluated for capacity, comfort, electricity consumption, reliability, lifecycle cost or emissions. Some options improve one objective while increasing fan power, refrigerant charge, maintenance burden or control complexity. Do not call the option superior without declaring the weighted objective or the nonnegotiable constraint.

### 7. Practice and assessment

1. **Concept:** Explain the physical meaning of `phi = p_v/p_sat(T) for idealized moist air` and identify at least two assumptions necessary for its use.
2. **Numerical:** Repeat the example with all units shown: At 25 °C and saturation vapor pressure about 3.17 kPa, partial pressure of 1.585 kPa corresponds to roughly 50% relative humidity. State an answer at a precision justified by the input values.
4. **Diagnosis:** Design a plausible scenario in which the original result is misleading because of: The saturation pressure changes strongly with temperature, so warming air reduces relative humidity without removing water. Specify an independent observation to test the explanation.
5. **Experiment:** Convert the suggested verification into a small data-collection plan: Observe dew point and dry-bulb together during a heating-only test.
6. **Decision:** Defend a recommendation using the lesson's trade-off: Select controls that can independently manage humidity when required. Identify one operating condition that might reverse your conclusion.

**Checking rubric:** Give credit for a correct model boundary and quantities, transparent unit conversion, dimensional reasonableness, explicit limitations and a falsifiable verification strategy. Do not award full credit for copying a plausible-looking number without explaining what it measures. For an open-ended design response, alternative answers may be valid when their constraints and evidence are coherent.


---

## U04-L03 — Moist-air enthalpy per dry-air mass

**Outcome:** Interpret moist-air enthalpy per dry-air mass, perform a traceable estimate, diagnose a limitation, and explain how evidence could change the associated engineering decision.

### 1. Engineering problem and purpose

An air handler mixes outdoor and return air, cools it, removes condensed water, and supplies air to a classroom. Wet-bulb, humidity ratio and coil bypass effects all influence comfort. The specific issue here is **moist-air enthalpy per dry-air mass**. Calculate moist-air properties and distinguish sensible heating/cooling from latent moisture removal. This problem matters because a mechanical design must perform across several operating states rather than just one conveniently chosen measurement. A useful first result is a quantity with clear units, an identified system boundary and a stated purpose; it is not a prediction for arbitrary buildings or products.

### 2. Governing idea and modeling assumptions

**Working relation:** `h ≈ 1.006 T + w(2501+1.86T), kJ/kg dry air, T in °C`.

This equation should be interpreted together with its reference states. Write down every independent variable, with its numerical units, and keep any temperature-difference term separate from an absolute thermodynamic temperature. For a steady-flow energy equation, indicate the mass-flow definition; for a moist-air relation, specify whether the denominator is dry-air mass; for a performance ratio, ensure numerator and denominator cover the same test period. If the result is dimensionless, explain what physical quantities were compared.

Mixing temperature alone does not track total sensible-plus-latent cooling duty. This is a reason to retain the equation's scope in every answer. A classroom relation may assume ideal-gas behavior, constant specific heat, steady mass balance, uniform mixing, negligible leakage, or a fixed equipment efficiency. Real systems can violate several of these assumptions simultaneously, particularly during a changing load. The correct response is to identify the assumption and collect appropriate evidence, rather than silently adding correction factors whose source is unclear.

### 3. Fully specified numerical teaching example

**Assumed inputs and computed answer:** For T=25 °C and w=0.010 kg/kg dry air, the approximation gives 50.58 kJ/kg dry air.

Reproduce the result using the equation rather than copying the displayed answer. Convert all values to compatible units before substitution. Distinguish kW from kWh, kPa from Pa, and a percentage from a dimensionless fraction. Then perform three small checks: does the output have the expected dimensions, is its sign physically meaningful for the chosen reference direction, and does it approach a sensible limiting value when the driving difference or mass flow tends toward zero? If a limiting case gives a contradiction, examine the equation and model boundary before trusting the decimals.

### 4. Physical interpretation and failure analysis

The immediate diagnostic trap in this lesson is the following: Mixing temperature alone does not track total sensible-plus-latent cooling duty. Construct a counterexample where the displayed calculation remains arithmetically correct but no longer explains the actual operating behavior. Identify which state variable or energy stream has been excluded, whether the error would tend to make the prediction high or low, and which observation could reveal the discrepancy. Where the sign of the discrepancy depends on coupled effects, give both plausible directions instead of selecting one without evidence.

### 5. Measurement and independent verification

**Suggested evidence:** Use matched dry-air flow and measured inlet/outlet psychrometric states. Define instrument location, calibration state, sample rate, expected operating condition and averaging period. Record the physical configuration, controller state, weather or ambient condition and any recent service changes. Establish a repeated baseline where practical; a one-off value can be distorted by transient heat storage or instrument delay. Preserve raw observations separately from processed plots so a different analyst can independently reproduce the result.

For uncertainty, start with a bounded input sensitivity calculation. Identify the most influential parameter and estimate how its uncertainty propagates through the working relation. If the input depends on other measured quantities, note their correlation instead of automatically treating errors as independent. Keep the measurement units and calibration references attached to each row in the results table. A plotted model curve is not experimental data; if both are presented, label them differently and show measurement points with their uncertainty where available.

### 6. Design choice and engineering trade-offs

**Decision problem:** Compare cooling coils using enthalpy differences and water removal, not solely supply temperature. Translate this into a decision matrix with at least one primary performance measure and one hard constraint. State whether the option is being evaluated for capacity, comfort, electricity consumption, reliability, lifecycle cost or emissions. Some options improve one objective while increasing fan power, refrigerant charge, maintenance burden or control complexity. Do not call the option superior without declaring the weighted objective or the nonnegotiable constraint.

### 7. Practice and assessment

1. **Concept:** Explain the physical meaning of `h ≈ 1.006 T + w(2501+1.86T), kJ/kg dry air, T in °C` and identify at least two assumptions necessary for its use.
2. **Numerical:** Repeat the example with all units shown: For T=25 °C and w=0.010 kg/kg dry air, the approximation gives 50.58 kJ/kg dry air. State an answer at a precision justified by the input values.
4. **Diagnosis:** Design a plausible scenario in which the original result is misleading because of: Mixing temperature alone does not track total sensible-plus-latent cooling duty. Specify an independent observation to test the explanation.
5. **Experiment:** Convert the suggested verification into a small data-collection plan: Use matched dry-air flow and measured inlet/outlet psychrometric states.
6. **Decision:** Defend a recommendation using the lesson's trade-off: Compare cooling coils using enthalpy differences and water removal, not solely supply temperature. Identify one operating condition that might reverse your conclusion.

**Checking rubric:** Give credit for a correct model boundary and quantities, transparent unit conversion, dimensional reasonableness, explicit limitations and a falsifiable verification strategy. Do not award full credit for copying a plausible-looking number without explaining what it measures. For an open-ended design response, alternative answers may be valid when their constraints and evidence are coherent.


---

## U04-L04 — Air mixing and outdoor-air fraction

**Outcome:** Interpret air mixing and outdoor-air fraction, perform a traceable estimate, diagnose a limitation, and explain how evidence could change the associated engineering decision.

### 1. Engineering problem and purpose

An air handler mixes outdoor and return air, cools it, removes condensed water, and supplies air to a classroom. Wet-bulb, humidity ratio and coil bypass effects all influence comfort. The specific issue here is **air mixing and outdoor-air fraction**. Calculate moist-air properties and distinguish sensible heating/cooling from latent moisture removal. This problem matters because a mechanical design must perform across several operating states rather than just one conveniently chosen measurement. A useful first result is a quantity with clear units, an identified system boundary and a stated purpose; it is not a prediction for arbitrary buildings or products.

### 2. Governing idea and modeling assumptions

**Working relation:** `h_mix = x h_out+(1−x)h_return, with dry-air mass fraction x`.

This equation should be interpreted together with its reference states. Write down every independent variable, with its numerical units, and keep any temperature-difference term separate from an absolute thermodynamic temperature. For a steady-flow energy equation, indicate the mass-flow definition; for a moist-air relation, specify whether the denominator is dry-air mass; for a performance ratio, ensure numerator and denominator cover the same test period. If the result is dimensionless, explain what physical quantities were compared.

Volume fractions and dry-air mass fractions are not interchangeable in all conditions. This is a reason to retain the equation's scope in every answer. A classroom relation may assume ideal-gas behavior, constant specific heat, steady mass balance, uniform mixing, negligible leakage, or a fixed equipment efficiency. Real systems can violate several of these assumptions simultaneously, particularly during a changing load. The correct response is to identify the assumption and collect appropriate evidence, rather than silently adding correction factors whose source is unclear.

### 3. Fully specified numerical teaching example

**Assumed inputs and computed answer:** For x=0.30, outside enthalpy 70 and return enthalpy 50 kJ/kg dry air, mixed enthalpy is 56 kJ/kg.

Reproduce the result using the equation rather than copying the displayed answer. Convert all values to compatible units before substitution. Distinguish kW from kWh, kPa from Pa, and a percentage from a dimensionless fraction. Then perform three small checks: does the output have the expected dimensions, is its sign physically meaningful for the chosen reference direction, and does it approach a sensible limiting value when the driving difference or mass flow tends toward zero? If a limiting case gives a contradiction, examine the equation and model boundary before trusting the decimals.

### 4. Physical interpretation and failure analysis

The immediate diagnostic trap in this lesson is the following: Volume fractions and dry-air mass fractions are not interchangeable in all conditions. Construct a counterexample where the displayed calculation remains arithmetically correct but no longer explains the actual operating behavior. Identify which state variable or energy stream has been excluded, whether the error would tend to make the prediction high or low, and which observation could reveal the discrepancy. Where the sign of the discrepancy depends on coupled effects, give both plausible directions instead of selecting one without evidence.

### 5. Measurement and independent verification

**Suggested evidence:** Measure intake damper position only as an indicator; infer actual fraction from calibrated mass-flow or tracer data. Define instrument location, calibration state, sample rate, expected operating condition and averaging period. Record the physical configuration, controller state, weather or ambient condition and any recent service changes. Establish a repeated baseline where practical; a one-off value can be distorted by transient heat storage or instrument delay. Preserve raw observations separately from processed plots so a different analyst can independently reproduce the result.

For uncertainty, start with a bounded input sensitivity calculation. Identify the most influential parameter and estimate how its uncertainty propagates through the working relation. If the input depends on other measured quantities, note their correlation instead of automatically treating errors as independent. Keep the measurement units and calibration references attached to each row in the results table. A plotted model curve is not experimental data; if both are presented, label them differently and show measurement points with their uncertainty where available.

### 6. Design choice and engineering trade-offs

**Decision problem:** Consider economizer benefit, pollutant levels, and ventilation minima simultaneously. Translate this into a decision matrix with at least one primary performance measure and one hard constraint. State whether the option is being evaluated for capacity, comfort, electricity consumption, reliability, lifecycle cost or emissions. Some options improve one objective while increasing fan power, refrigerant charge, maintenance burden or control complexity. Do not call the option superior without declaring the weighted objective or the nonnegotiable constraint.

### 7. Practice and assessment

1. **Concept:** Explain the physical meaning of `h_mix = x h_out+(1−x)h_return, with dry-air mass fraction x` and identify at least two assumptions necessary for its use.
2. **Numerical:** Repeat the example with all units shown: For x=0.30, outside enthalpy 70 and return enthalpy 50 kJ/kg dry air, mixed enthalpy is 56 kJ/kg. State an answer at a precision justified by the input values.
4. **Diagnosis:** Design a plausible scenario in which the original result is misleading because of: Volume fractions and dry-air mass fractions are not interchangeable in all conditions. Specify an independent observation to test the explanation.
5. **Experiment:** Convert the suggested verification into a small data-collection plan: Measure intake damper position only as an indicator; infer actual fraction from calibrated mass-flow or tracer data.
6. **Decision:** Defend a recommendation using the lesson's trade-off: Consider economizer benefit, pollutant levels, and ventilation minima simultaneously. Identify one operating condition that might reverse your conclusion.

**Checking rubric:** Give credit for a correct model boundary and quantities, transparent unit conversion, dimensional reasonableness, explicit limitations and a falsifiable verification strategy. Do not award full credit for copying a plausible-looking number without explaining what it measures. For an open-ended design response, alternative answers may be valid when their constraints and evidence are coherent.


---

## U04-L05 — Cooling-coil dehumidification

**Outcome:** Interpret cooling-coil dehumidification, perform a traceable estimate, diagnose a limitation, and explain how evidence could change the associated engineering decision.

### 1. Engineering problem and purpose

An air handler mixes outdoor and return air, cools it, removes condensed water, and supplies air to a classroom. Wet-bulb, humidity ratio and coil bypass effects all influence comfort. The specific issue here is **cooling-coil dehumidification**. Calculate moist-air properties and distinguish sensible heating/cooling from latent moisture removal. This problem matters because a mechanical design must perform across several operating states rather than just one conveniently chosen measurement. A useful first result is a quantity with clear units, an identified system boundary and a stated purpose; it is not a prediction for arbitrary buildings or products.

### 2. Governing idea and modeling assumptions

**Working relation:** `m_dot_w = m_dot_da (w_in−w_out)`.

This equation should be interpreted together with its reference states. Write down every independent variable, with its numerical units, and keep any temperature-difference term separate from an absolute thermodynamic temperature. For a steady-flow energy equation, indicate the mass-flow definition; for a moist-air relation, specify whether the denominator is dry-air mass; for a performance ratio, ensure numerator and denominator cover the same test period. If the result is dimensionless, explain what physical quantities were compared.

Condensation is not inevitable whenever dry-bulb temperature falls; the surface must cool below dew point. This is a reason to retain the equation's scope in every answer. A classroom relation may assume ideal-gas behavior, constant specific heat, steady mass balance, uniform mixing, negligible leakage, or a fixed equipment efficiency. Real systems can violate several of these assumptions simultaneously, particularly during a changing load. The correct response is to identify the assumption and collect appropriate evidence, rather than silently adding correction factors whose source is unclear.

### 3. Fully specified numerical teaching example

**Assumed inputs and computed answer:** With 0.9 kg/s dry air, w_in=0.014 and w_out=0.009 kg/kg, condensate rate is 0.0045 kg/s, about 16.2 kg/h.

Reproduce the result using the equation rather than copying the displayed answer. Convert all values to compatible units before substitution. Distinguish kW from kWh, kPa from Pa, and a percentage from a dimensionless fraction. Then perform three small checks: does the output have the expected dimensions, is its sign physically meaningful for the chosen reference direction, and does it approach a sensible limiting value when the driving difference or mass flow tends toward zero? If a limiting case gives a contradiction, examine the equation and model boundary before trusting the decimals.

### 4. Physical interpretation and failure analysis

The immediate diagnostic trap in this lesson is the following: Condensation is not inevitable whenever dry-bulb temperature falls; the surface must cool below dew point. Construct a counterexample where the displayed calculation remains arithmetically correct but no longer explains the actual operating behavior. Identify which state variable or energy stream has been excluded, whether the error would tend to make the prediction high or low, and which observation could reveal the discrepancy. Where the sign of the discrepancy depends on coupled effects, give both plausible directions instead of selecting one without evidence.

### 5. Measurement and independent verification

**Suggested evidence:** Observe condensate drainage, coil surface conditions, and psychrometric state changes. Define instrument location, calibration state, sample rate, expected operating condition and averaging period. Record the physical configuration, controller state, weather or ambient condition and any recent service changes. Establish a repeated baseline where practical; a one-off value can be distorted by transient heat storage or instrument delay. Preserve raw observations separately from processed plots so a different analyst can independently reproduce the result.

For uncertainty, start with a bounded input sensitivity calculation. Identify the most influential parameter and estimate how its uncertainty propagates through the working relation. If the input depends on other measured quantities, note their correlation instead of automatically treating errors as independent. Keep the measurement units and calibration references attached to each row in the results table. A plotted model curve is not experimental data; if both are presented, label them differently and show measurement points with their uncertainty where available.

### 6. Design choice and engineering trade-offs

**Decision problem:** Avoid falsely treating water removal as equivalent to a fixed dry-bulb temperature drop. Translate this into a decision matrix with at least one primary performance measure and one hard constraint. State whether the option is being evaluated for capacity, comfort, electricity consumption, reliability, lifecycle cost or emissions. Some options improve one objective while increasing fan power, refrigerant charge, maintenance burden or control complexity. Do not call the option superior without declaring the weighted objective or the nonnegotiable constraint.

### 7. Practice and assessment

1. **Concept:** Explain the physical meaning of `m_dot_w = m_dot_da (w_in−w_out)` and identify at least two assumptions necessary for its use.
2. **Numerical:** Repeat the example with all units shown: With 0.9 kg/s dry air, w_in=0.014 and w_out=0.009 kg/kg, condensate rate is 0.0045 kg/s, about 16.2 kg/h. State an answer at a precision justified by the input values.
4. **Diagnosis:** Design a plausible scenario in which the original result is misleading because of: Condensation is not inevitable whenever dry-bulb temperature falls; the surface must cool below dew point. Specify an independent observation to test the explanation.
5. **Experiment:** Convert the suggested verification into a small data-collection plan: Observe condensate drainage, coil surface conditions, and psychrometric state changes.
6. **Decision:** Defend a recommendation using the lesson's trade-off: Avoid falsely treating water removal as equivalent to a fixed dry-bulb temperature drop. Identify one operating condition that might reverse your conclusion.

**Checking rubric:** Give credit for a correct model boundary and quantities, transparent unit conversion, dimensional reasonableness, explicit limitations and a falsifiable verification strategy. Do not award full credit for copying a plausible-looking number without explaining what it measures. For an open-ended design response, alternative answers may be valid when their constraints and evidence are coherent.


---

