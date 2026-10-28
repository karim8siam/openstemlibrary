# Unit 01: Thermal Comfort, Energy Balances and Refrigeration Fundamentals

**Course Code**: RAC 301 · **Level**: Advanced Undergraduate Engineering

## Unit Overview & Physical Foundations

This comprehensive university textbook unit covers the theoretical framework, physical modeling, mathematical governing equations, and engineering applications of **Thermal Comfort, Energy Balances and Refrigeration Fundamentals**.

## U01-L01 — Heat, temperature and the system boundary

**Outcome:** Interpret heat, temperature and the system boundary, perform a traceable estimate, diagnose a limitation, and explain how evidence could change the associated engineering decision.

### 1. Engineering problem and purpose

A small learning laboratory has a varying outdoor temperature, computer heat gains, and a requirement to maintain a defined indoor comfort range. The engineer must identify the load, energy boundary and control objective before selecting equipment. The specific issue here is **heat, temperature and the system boundary**. Distinguish heat flow, cooling capacity, thermal comfort, power, and stored energy. This problem matters because a mechanical design must perform across several operating states rather than just one conveniently chosen measurement. A useful first result is a quantity with clear units, an identified system boundary and a stated purpose; it is not a prediction for arbitrary buildings or products.

### 2. Governing idea and modeling assumptions

**Working relation:** `Q_dot = m_dot c_p (T_out−T_in) for a flowing single-phase stream`.

This equation should be interpreted together with its reference states. Write down every independent variable, with its numerical units, and keep any temperature-difference term separate from an absolute thermodynamic temperature. For a steady-flow energy equation, indicate the mass-flow definition; for a moist-air relation, specify whether the denominator is dry-air mass; for a performance ratio, ensure numerator and denominator cover the same test period. If the result is dimensionless, explain what physical quantities were compared.

Temperature is a state variable; heat is energy crossing a boundary. A thermostat reading does not directly reveal room cooling capacity. This is a reason to retain the equation's scope in every answer. A classroom relation may assume ideal-gas behavior, constant specific heat, steady mass balance, uniform mixing, negligible leakage, or a fixed equipment efficiency. Real systems can violate several of these assumptions simultaneously, particularly during a changing load. The correct response is to identify the assumption and collect appropriate evidence, rather than silently adding correction factors whose source is unclear.

### 3. Fully specified numerical teaching example

**Assumed inputs and computed answer:** At 0.25 kg/s, 1.005 kJ/(kg K) and an 8 K temperature rise, the sensible heat rate is approximately 2.01 kW.

Reproduce the result using the equation rather than copying the displayed answer. Convert all values to compatible units before substitution. Distinguish kW from kWh, kPa from Pa, and a percentage from a dimensionless fraction. Then perform three small checks: does the output have the expected dimensions, is its sign physically meaningful for the chosen reference direction, and does it approach a sensible limiting value when the driving difference or mass flow tends toward zero? If a limiting case gives a contradiction, examine the equation and model boundary before trusting the decimals.

### 4. Physical interpretation and failure analysis

The immediate diagnostic trap in this lesson is the following: Temperature is a state variable; heat is energy crossing a boundary. A thermostat reading does not directly reveal room cooling capacity. Construct a counterexample where the displayed calculation remains arithmetically correct but no longer explains the actual operating behavior. Identify which state variable or energy stream has been excluded, whether the error would tend to make the prediction high or low, and which observation could reveal the discrepancy. Where the sign of the discrepancy depends on coupled effects, give both plausible directions instead of selecting one without evidence.

### 5. Measurement and independent verification

**Suggested evidence:** Measure inlet and outlet temperatures, air mass flow and sensor location at the same time. Define instrument location, calibration state, sample rate, expected operating condition and averaging period. Record the physical configuration, controller state, weather or ambient condition and any recent service changes. Establish a repeated baseline where practical; a one-off value can be distorted by transient heat storage or instrument delay. Preserve raw observations separately from processed plots so a different analyst can independently reproduce the result.

For uncertainty, start with a bounded input sensitivity calculation. Identify the most influential parameter and estimate how its uncertainty propagates through the working relation. If the input depends on other measured quantities, note their correlation instead of automatically treating errors as independent. Keep the measurement units and calibration references attached to each row in the results table. A plotted model curve is not experimental data; if both are presented, label them differently and show measurement points with their uncertainty where available.

### 6. Design choice and engineering trade-offs

**Decision problem:** Specify whether fan heat and outdoor-air load belong inside the selected system boundary. Translate this into a decision matrix with at least one primary performance measure and one hard constraint. State whether the option is being evaluated for capacity, comfort, electricity consumption, reliability, lifecycle cost or emissions. Some options improve one objective while increasing fan power, refrigerant charge, maintenance burden or control complexity. Do not call the option superior without declaring the weighted objective or the nonnegotiable constraint.

### 7. Practice and assessment

1. **Concept:** Explain the physical meaning of `Q_dot = m_dot c_p (T_out−T_in) for a flowing single-phase stream` and identify at least two assumptions necessary for its use.
2. **Numerical:** Repeat the example with all units shown: At 0.25 kg/s, 1.005 kJ/(kg K) and an 8 K temperature rise, the sensible heat rate is approximately 2.01 kW. State an answer at a precision justified by the input values.
4. **Diagnosis:** Design a plausible scenario in which the original result is misleading because of: Temperature is a state variable; heat is energy crossing a boundary. A thermostat reading does not directly reveal room cooling capacity. Specify an independent observation to test the explanation.
5. **Experiment:** Convert the suggested verification into a small data-collection plan: Measure inlet and outlet temperatures, air mass flow and sensor location at the same time.
6. **Decision:** Defend a recommendation using the lesson's trade-off: Specify whether fan heat and outdoor-air load belong inside the selected system boundary. Identify one operating condition that might reverse your conclusion.

**Checking rubric:** Give credit for a correct model boundary and quantities, transparent unit conversion, dimensional reasonableness, explicit limitations and a falsifiable verification strategy. Do not award full credit for copying a plausible-looking number without explaining what it measures. For an open-ended design response, alternative answers may be valid when their constraints and evidence are coherent.


---

## U01-L02 — Sensible and latent heat components

**Outcome:** Interpret sensible and latent heat components, perform a traceable estimate, diagnose a limitation, and explain how evidence could change the associated engineering decision.

### 1. Engineering problem and purpose

A small learning laboratory has a varying outdoor temperature, computer heat gains, and a requirement to maintain a defined indoor comfort range. The engineer must identify the load, energy boundary and control objective before selecting equipment. The specific issue here is **sensible and latent heat components**. Distinguish heat flow, cooling capacity, thermal comfort, power, and stored energy. This problem matters because a mechanical design must perform across several operating states rather than just one conveniently chosen measurement. A useful first result is a quantity with clear units, an identified system boundary and a stated purpose; it is not a prediction for arbitrary buildings or products.

### 2. Governing idea and modeling assumptions

**Working relation:** `Q_total = Q_sensible + Q_latent`.

This equation should be interpreted together with its reference states. Write down every independent variable, with its numerical units, and keep any temperature-difference term separate from an absolute thermodynamic temperature. For a steady-flow energy equation, indicate the mass-flow definition; for a moist-air relation, specify whether the denominator is dry-air mass; for a performance ratio, ensure numerator and denominator cover the same test period. If the result is dimensionless, explain what physical quantities were compared.

A coil can satisfy dry-bulb temperature but leave humidity unacceptable if its latent capacity is insufficient. This is a reason to retain the equation's scope in every answer. A classroom relation may assume ideal-gas behavior, constant specific heat, steady mass balance, uniform mixing, negligible leakage, or a fixed equipment efficiency. Real systems can violate several of these assumptions simultaneously, particularly during a changing load. The correct response is to identify the assumption and collect appropriate evidence, rather than silently adding correction factors whose source is unclear.

### 3. Fully specified numerical teaching example

**Assumed inputs and computed answer:** A zone with 3.2 kW sensible gain and 0.9 kW moisture-related gain needs 4.1 kW of instantaneous heat removal in this simplified balance.

Reproduce the result using the equation rather than copying the displayed answer. Convert all values to compatible units before substitution. Distinguish kW from kWh, kPa from Pa, and a percentage from a dimensionless fraction. Then perform three small checks: does the output have the expected dimensions, is its sign physically meaningful for the chosen reference direction, and does it approach a sensible limiting value when the driving difference or mass flow tends toward zero? If a limiting case gives a contradiction, examine the equation and model boundary before trusting the decimals.

### 4. Physical interpretation and failure analysis

The immediate diagnostic trap in this lesson is the following: A coil can satisfy dry-bulb temperature but leave humidity unacceptable if its latent capacity is insufficient. Construct a counterexample where the displayed calculation remains arithmetically correct but no longer explains the actual operating behavior. Identify which state variable or energy stream has been excluded, whether the error would tend to make the prediction high or low, and which observation could reveal the discrepancy. Where the sign of the discrepancy depends on coupled effects, give both plausible directions instead of selecting one without evidence.

### 5. Measurement and independent verification

**Suggested evidence:** Record dry-bulb, dew point, water condensate and coil entering conditions. Define instrument location, calibration state, sample rate, expected operating condition and averaging period. Record the physical configuration, controller state, weather or ambient condition and any recent service changes. Establish a repeated baseline where practical; a one-off value can be distorted by transient heat storage or instrument delay. Preserve raw observations separately from processed plots so a different analyst can independently reproduce the result.

For uncertainty, start with a bounded input sensitivity calculation. Identify the most influential parameter and estimate how its uncertainty propagates through the working relation. If the input depends on other measured quantities, note their correlation instead of automatically treating errors as independent. Keep the measurement units and calibration references attached to each row in the results table. A plotted model curve is not experimental data; if both are presented, label them differently and show measurement points with their uncertainty where available.

### 6. Design choice and engineering trade-offs

**Decision problem:** Compare a dehumidification option against further overcooling and reheat. Translate this into a decision matrix with at least one primary performance measure and one hard constraint. State whether the option is being evaluated for capacity, comfort, electricity consumption, reliability, lifecycle cost or emissions. Some options improve one objective while increasing fan power, refrigerant charge, maintenance burden or control complexity. Do not call the option superior without declaring the weighted objective or the nonnegotiable constraint.

### 7. Practice and assessment

1. **Concept:** Explain the physical meaning of `Q_total = Q_sensible + Q_latent` and identify at least two assumptions necessary for its use.
2. **Numerical:** Repeat the example with all units shown: A zone with 3.2 kW sensible gain and 0.9 kW moisture-related gain needs 4.1 kW of instantaneous heat removal in this simplified balance. State an answer at a precision justified by the input values.
4. **Diagnosis:** Design a plausible scenario in which the original result is misleading because of: A coil can satisfy dry-bulb temperature but leave humidity unacceptable if its latent capacity is insufficient. Specify an independent observation to test the explanation.
5. **Experiment:** Convert the suggested verification into a small data-collection plan: Record dry-bulb, dew point, water condensate and coil entering conditions.
6. **Decision:** Defend a recommendation using the lesson's trade-off: Compare a dehumidification option against further overcooling and reheat. Identify one operating condition that might reverse your conclusion.

**Checking rubric:** Give credit for a correct model boundary and quantities, transparent unit conversion, dimensional reasonableness, explicit limitations and a falsifiable verification strategy. Do not award full credit for copying a plausible-looking number without explaining what it measures. For an open-ended design response, alternative answers may be valid when their constraints and evidence are coherent.


---

## U01-L03 — Steady energy conservation in an air handler

**Outcome:** Interpret steady energy conservation in an air handler, perform a traceable estimate, diagnose a limitation, and explain how evidence could change the associated engineering decision.

### 1. Engineering problem and purpose

A small learning laboratory has a varying outdoor temperature, computer heat gains, and a requirement to maintain a defined indoor comfort range. The engineer must identify the load, energy boundary and control objective before selecting equipment. The specific issue here is **steady energy conservation in an air handler**. Distinguish heat flow, cooling capacity, thermal comfort, power, and stored energy. This problem matters because a mechanical design must perform across several operating states rather than just one conveniently chosen measurement. A useful first result is a quantity with clear units, an identified system boundary and a stated purpose; it is not a prediction for arbitrary buildings or products.

### 2. Governing idea and modeling assumptions

**Working relation:** `Q_coil + W_fan + m_dot(h_in−h_out) = 0 with consistent signed directions`.

This equation should be interpreted together with its reference states. Write down every independent variable, with its numerical units, and keep any temperature-difference term separate from an absolute thermodynamic temperature. For a steady-flow energy equation, indicate the mass-flow definition; for a moist-air relation, specify whether the denominator is dry-air mass; for a performance ratio, ensure numerator and denominator cover the same test period. If the result is dimensionless, explain what physical quantities were compared.

A sign convention matters; indoor mixing and upstream fan work can change the required coil duty. This is a reason to retain the equation's scope in every answer. A classroom relation may assume ideal-gas behavior, constant specific heat, steady mass balance, uniform mixing, negligible leakage, or a fixed equipment efficiency. Real systems can violate several of these assumptions simultaneously, particularly during a changing load. The correct response is to identify the assumption and collect appropriate evidence, rather than silently adding correction factors whose source is unclear.

### 3. Fully specified numerical teaching example

**Assumed inputs and computed answer:** A 0.8 kg/s dry-air stream losing 12 kJ/kg of moist-air enthalpy represents 9.6 kW before explicit fan and leakage corrections.

Reproduce the result using the equation rather than copying the displayed answer. Convert all values to compatible units before substitution. Distinguish kW from kWh, kPa from Pa, and a percentage from a dimensionless fraction. Then perform three small checks: does the output have the expected dimensions, is its sign physically meaningful for the chosen reference direction, and does it approach a sensible limiting value when the driving difference or mass flow tends toward zero? If a limiting case gives a contradiction, examine the equation and model boundary before trusting the decimals.

### 4. Physical interpretation and failure analysis

The immediate diagnostic trap in this lesson is the following: A sign convention matters; indoor mixing and upstream fan work can change the required coil duty. Construct a counterexample where the displayed calculation remains arithmetically correct but no longer explains the actual operating behavior. Identify which state variable or energy stream has been excluded, whether the error would tend to make the prediction high or low, and which observation could reveal the discrepancy. Where the sign of the discrepancy depends on coupled effects, give both plausible directions instead of selecting one without evidence.

### 5. Measurement and independent verification

**Suggested evidence:** Locate a control volume and instrument temperatures and humidity at each boundary port. Define instrument location, calibration state, sample rate, expected operating condition and averaging period. Record the physical configuration, controller state, weather or ambient condition and any recent service changes. Establish a repeated baseline where practical; a one-off value can be distorted by transient heat storage or instrument delay. Preserve raw observations separately from processed plots so a different analyst can independently reproduce the result.

For uncertainty, start with a bounded input sensitivity calculation. Identify the most influential parameter and estimate how its uncertainty propagates through the working relation. If the input depends on other measured quantities, note their correlation instead of automatically treating errors as independent. Keep the measurement units and calibration references attached to each row in the results table. A plotted model curve is not experimental data; if both are presented, label them differently and show measurement points with their uncertainty where available.

### 6. Design choice and engineering trade-offs

**Decision problem:** Separate useful room cooling from electrical input and supply-fan heat. Translate this into a decision matrix with at least one primary performance measure and one hard constraint. State whether the option is being evaluated for capacity, comfort, electricity consumption, reliability, lifecycle cost or emissions. Some options improve one objective while increasing fan power, refrigerant charge, maintenance burden or control complexity. Do not call the option superior without declaring the weighted objective or the nonnegotiable constraint.

### 7. Practice and assessment

1. **Concept:** Explain the physical meaning of `Q_coil + W_fan + m_dot(h_in−h_out) = 0 with consistent signed directions` and identify at least two assumptions necessary for its use.
2. **Numerical:** Repeat the example with all units shown: A 0.8 kg/s dry-air stream losing 12 kJ/kg of moist-air enthalpy represents 9.6 kW before explicit fan and leakage corrections. State an answer at a precision justified by the input values.
4. **Diagnosis:** Design a plausible scenario in which the original result is misleading because of: A sign convention matters; indoor mixing and upstream fan work can change the required coil duty. Specify an independent observation to test the explanation.
5. **Experiment:** Convert the suggested verification into a small data-collection plan: Locate a control volume and instrument temperatures and humidity at each boundary port.
6. **Decision:** Defend a recommendation using the lesson's trade-off: Separate useful room cooling from electrical input and supply-fan heat. Identify one operating condition that might reverse your conclusion.

**Checking rubric:** Give credit for a correct model boundary and quantities, transparent unit conversion, dimensional reasonableness, explicit limitations and a falsifiable verification strategy. Do not award full credit for copying a plausible-looking number without explaining what it measures. For an open-ended design response, alternative answers may be valid when their constraints and evidence are coherent.


---

## U01-L04 — Comfort objectives and operative temperature

**Outcome:** Interpret comfort objectives and operative temperature, perform a traceable estimate, diagnose a limitation, and explain how evidence could change the associated engineering decision.

### 1. Engineering problem and purpose

A small learning laboratory has a varying outdoor temperature, computer heat gains, and a requirement to maintain a defined indoor comfort range. The engineer must identify the load, energy boundary and control objective before selecting equipment. The specific issue here is **comfort objectives and operative temperature**. Distinguish heat flow, cooling capacity, thermal comfort, power, and stored energy. This problem matters because a mechanical design must perform across several operating states rather than just one conveniently chosen measurement. A useful first result is a quantity with clear units, an identified system boundary and a stated purpose; it is not a prediction for arbitrary buildings or products.

### 2. Governing idea and modeling assumptions

**Working relation:** `T_op ≈ (T_air+T_radiant)/2 under restricted low-air-speed conditions`.

This equation should be interpreted together with its reference states. Write down every independent variable, with its numerical units, and keep any temperature-difference term separate from an absolute thermodynamic temperature. For a steady-flow energy equation, indicate the mass-flow definition; for a moist-air relation, specify whether the denominator is dry-air mass; for a performance ratio, ensure numerator and denominator cover the same test period. If the result is dimensionless, explain what physical quantities were compared.

A single dry-bulb number cannot guarantee thermal comfort for every occupant. This is a reason to retain the equation's scope in every answer. A classroom relation may assume ideal-gas behavior, constant specific heat, steady mass balance, uniform mixing, negligible leakage, or a fixed equipment efficiency. Real systems can violate several of these assumptions simultaneously, particularly during a changing load. The correct response is to identify the assumption and collect appropriate evidence, rather than silently adding correction factors whose source is unclear.

### 3. Fully specified numerical teaching example

**Assumed inputs and computed answer:** Air at 25 °C and mean radiant temperature 29 °C gives approximately 27 °C operative temperature under the stated approximation.

Reproduce the result using the equation rather than copying the displayed answer. Convert all values to compatible units before substitution. Distinguish kW from kWh, kPa from Pa, and a percentage from a dimensionless fraction. Then perform three small checks: does the output have the expected dimensions, is its sign physically meaningful for the chosen reference direction, and does it approach a sensible limiting value when the driving difference or mass flow tends toward zero? If a limiting case gives a contradiction, examine the equation and model boundary before trusting the decimals.

### 4. Physical interpretation and failure analysis

The immediate diagnostic trap in this lesson is the following: A single dry-bulb number cannot guarantee thermal comfort for every occupant. Construct a counterexample where the displayed calculation remains arithmetically correct but no longer explains the actual operating behavior. Identify which state variable or energy stream has been excluded, whether the error would tend to make the prediction high or low, and which observation could reveal the discrepancy. Where the sign of the discrepancy depends on coupled effects, give both plausible directions instead of selecting one without evidence.

### 5. Measurement and independent verification

**Suggested evidence:** Measure radiant asymmetry, air speed, clothing assumptions and activity alongside dry-bulb temperature. Define instrument location, calibration state, sample rate, expected operating condition and averaging period. Record the physical configuration, controller state, weather or ambient condition and any recent service changes. Establish a repeated baseline where practical; a one-off value can be distorted by transient heat storage or instrument delay. Preserve raw observations separately from processed plots so a different analyst can independently reproduce the result.

For uncertainty, start with a bounded input sensitivity calculation. Identify the most influential parameter and estimate how its uncertainty propagates through the working relation. If the input depends on other measured quantities, note their correlation instead of automatically treating errors as independent. Keep the measurement units and calibration references attached to each row in the results table. A plotted model curve is not experimental data; if both are presented, label them differently and show measurement points with their uncertainty where available.

### 6. Design choice and engineering trade-offs

**Decision problem:** Keep comfort as a multi-variable constraint rather than a single thermostat setpoint. Translate this into a decision matrix with at least one primary performance measure and one hard constraint. State whether the option is being evaluated for capacity, comfort, electricity consumption, reliability, lifecycle cost or emissions. Some options improve one objective while increasing fan power, refrigerant charge, maintenance burden or control complexity. Do not call the option superior without declaring the weighted objective or the nonnegotiable constraint.

### 7. Practice and assessment

1. **Concept:** Explain the physical meaning of `T_op ≈ (T_air+T_radiant)/2 under restricted low-air-speed conditions` and identify at least two assumptions necessary for its use.
2. **Numerical:** Repeat the example with all units shown: Air at 25 °C and mean radiant temperature 29 °C gives approximately 27 °C operative temperature under the stated approximation. State an answer at a precision justified by the input values.
4. **Diagnosis:** Design a plausible scenario in which the original result is misleading because of: A single dry-bulb number cannot guarantee thermal comfort for every occupant. Specify an independent observation to test the explanation.
5. **Experiment:** Convert the suggested verification into a small data-collection plan: Measure radiant asymmetry, air speed, clothing assumptions and activity alongside dry-bulb temperature.
6. **Decision:** Defend a recommendation using the lesson's trade-off: Keep comfort as a multi-variable constraint rather than a single thermostat setpoint. Identify one operating condition that might reverse your conclusion.

**Checking rubric:** Give credit for a correct model boundary and quantities, transparent unit conversion, dimensional reasonableness, explicit limitations and a falsifiable verification strategy. Do not award full credit for copying a plausible-looking number without explaining what it measures. For an open-ended design response, alternative answers may be valid when their constraints and evidence are coherent.


---

## U01-L05 — Transient zone temperature and thermal storage

**Outcome:** Interpret transient zone temperature and thermal storage, perform a traceable estimate, diagnose a limitation, and explain how evidence could change the associated engineering decision.

### 1. Engineering problem and purpose

A small learning laboratory has a varying outdoor temperature, computer heat gains, and a requirement to maintain a defined indoor comfort range. The engineer must identify the load, energy boundary and control objective before selecting equipment. The specific issue here is **transient zone temperature and thermal storage**. Distinguish heat flow, cooling capacity, thermal comfort, power, and stored energy. This problem matters because a mechanical design must perform across several operating states rather than just one conveniently chosen measurement. A useful first result is a quantity with clear units, an identified system boundary and a stated purpose; it is not a prediction for arbitrary buildings or products.

### 2. Governing idea and modeling assumptions

**Working relation:** `C dT/dt = Q_gain − UA(T−T_out) − Q_cool`.

This equation should be interpreted together with its reference states. Write down every independent variable, with its numerical units, and keep any temperature-difference term separate from an absolute thermodynamic temperature. For a steady-flow energy equation, indicate the mass-flow definition; for a moist-air relation, specify whether the denominator is dry-air mass; for a performance ratio, ensure numerator and denominator cover the same test period. If the result is dimensionless, explain what physical quantities were compared.

A steady load equation cannot predict short cycling or building pre-cooling without storage. This is a reason to retain the equation's scope in every answer. A classroom relation may assume ideal-gas behavior, constant specific heat, steady mass balance, uniform mixing, negligible leakage, or a fixed equipment efficiency. Real systems can violate several of these assumptions simultaneously, particularly during a changing load. The correct response is to identify the assumption and collect appropriate evidence, rather than silently adding correction factors whose source is unclear.

### 3. Fully specified numerical teaching example

**Assumed inputs and computed answer:** A 6 MJ/K thermal mass receiving a net 1 kW for 600 s changes by 0.10 K if other terms are neglected.

Reproduce the result using the equation rather than copying the displayed answer. Convert all values to compatible units before substitution. Distinguish kW from kWh, kPa from Pa, and a percentage from a dimensionless fraction. Then perform three small checks: does the output have the expected dimensions, is its sign physically meaningful for the chosen reference direction, and does it approach a sensible limiting value when the driving difference or mass flow tends toward zero? If a limiting case gives a contradiction, examine the equation and model boundary before trusting the decimals.

### 4. Physical interpretation and failure analysis

The immediate diagnostic trap in this lesson is the following: A steady load equation cannot predict short cycling or building pre-cooling without storage. Construct a counterexample where the displayed calculation remains arithmetically correct but no longer explains the actual operating behavior. Identify which state variable or energy stream has been excluded, whether the error would tend to make the prediction high or low, and which observation could reveal the discrepancy. Where the sign of the discrepancy depends on coupled effects, give both plausible directions instead of selecting one without evidence.

### 5. Measurement and independent verification

**Suggested evidence:** Log indoor temperature and cooling power across a controlled setpoint change. Define instrument location, calibration state, sample rate, expected operating condition and averaging period. Record the physical configuration, controller state, weather or ambient condition and any recent service changes. Establish a repeated baseline where practical; a one-off value can be distorted by transient heat storage or instrument delay. Preserve raw observations separately from processed plots so a different analyst can independently reproduce the result.

For uncertainty, start with a bounded input sensitivity calculation. Identify the most influential parameter and estimate how its uncertainty propagates through the working relation. If the input depends on other measured quantities, note their correlation instead of automatically treating errors as independent. Keep the measurement units and calibration references attached to each row in the results table. A plotted model curve is not experimental data; if both are presented, label them differently and show measurement points with their uncertainty where available.

### 6. Design choice and engineering trade-offs

**Decision problem:** Determine when a steady estimate is adequate and when a transient model is required. Translate this into a decision matrix with at least one primary performance measure and one hard constraint. State whether the option is being evaluated for capacity, comfort, electricity consumption, reliability, lifecycle cost or emissions. Some options improve one objective while increasing fan power, refrigerant charge, maintenance burden or control complexity. Do not call the option superior without declaring the weighted objective or the nonnegotiable constraint.

### 7. Practice and assessment

1. **Concept:** Explain the physical meaning of `C dT/dt = Q_gain − UA(T−T_out) − Q_cool` and identify at least two assumptions necessary for its use.
2. **Numerical:** Repeat the example with all units shown: A 6 MJ/K thermal mass receiving a net 1 kW for 600 s changes by 0.10 K if other terms are neglected. State an answer at a precision justified by the input values.
4. **Diagnosis:** Design a plausible scenario in which the original result is misleading because of: A steady load equation cannot predict short cycling or building pre-cooling without storage. Specify an independent observation to test the explanation.
5. **Experiment:** Convert the suggested verification into a small data-collection plan: Log indoor temperature and cooling power across a controlled setpoint change.
6. **Decision:** Defend a recommendation using the lesson's trade-off: Determine when a steady estimate is adequate and when a transient model is required. Identify one operating condition that might reverse your conclusion.

**Checking rubric:** Give credit for a correct model boundary and quantities, transparent unit conversion, dimensional reasonableness, explicit limitations and a falsifiable verification strategy. Do not award full credit for copying a plausible-looking number without explaining what it measures. For an open-ended design response, alternative answers may be valid when their constraints and evidence are coherent.


---

