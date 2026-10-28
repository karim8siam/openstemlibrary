# Unit 03: Refrigerants, Compressors and Heat Exchangers

**Course Code**: RAC 303 · **Level**: Advanced Undergraduate Engineering

## Unit Overview & Physical Foundations

This comprehensive university textbook unit covers the theoretical framework, physical modeling, mathematical governing equations, and engineering applications of **Refrigerants, Compressors and Heat Exchangers**.

## U03-L01 — Refrigerant classes and environmental metrics

**Outcome:** Interpret refrigerant classes and environmental metrics, perform a traceable estimate, diagnose a limitation, and explain how evidence could change the associated engineering decision.

### 1. Engineering problem and purpose

A replacement refrigerant or compressor is considered for an existing cold-storage machine. Pressures, oil compatibility, capacities, operating envelope and safety requirements must be reviewed together. The specific issue here is **refrigerant classes and environmental metrics**. Interpret component duties and the constraints imposed by properties, pressure ratios, refrigerant choice and control hardware. This problem matters because a mechanical design must perform across several operating states rather than just one conveniently chosen measurement. A useful first result is a quantity with clear units, an identified system boundary and a stated purpose; it is not a prediction for arbitrary buildings or products.

### 2. Governing idea and modeling assumptions

**Working relation:** `Direct mass released = charge × leakage fraction`.

This equation should be interpreted together with its reference states. Write down every independent variable, with its numerical units, and keep any temperature-difference term separate from an absolute thermodynamic temperature. For a steady-flow energy equation, indicate the mass-flow definition; for a moist-air relation, specify whether the denominator is dry-air mass; for a performance ratio, ensure numerator and denominator cover the same test period. If the result is dimensionless, explain what physical quantities were compared.

Low global-warming potential does not automatically imply low total impact, easy availability or harmless operation. This is a reason to retain the equation's scope in every answer. A classroom relation may assume ideal-gas behavior, constant specific heat, steady mass balance, uniform mixing, negligible leakage, or a fixed equipment efficiency. Real systems can violate several of these assumptions simultaneously, particularly during a changing load. The correct response is to identify the assumption and collect appropriate evidence, rather than silently adding correction factors whose source is unclear.

### 3. Fully specified numerical teaching example

**Assumed inputs and computed answer:** A hypothetical 4 kg system losing 5% of its charge releases 0.20 kg of refrigerant; climate weighting additionally requires verified refrigerant-specific data.

Reproduce the result using the equation rather than copying the displayed answer. Convert all values to compatible units before substitution. Distinguish kW from kWh, kPa from Pa, and a percentage from a dimensionless fraction. Then perform three small checks: does the output have the expected dimensions, is its sign physically meaningful for the chosen reference direction, and does it approach a sensible limiting value when the driving difference or mass flow tends toward zero? If a limiting case gives a contradiction, examine the equation and model boundary before trusting the decimals.

### 4. Physical interpretation and failure analysis

The immediate diagnostic trap in this lesson is the following: Low global-warming potential does not automatically imply low total impact, easy availability or harmless operation. Construct a counterexample where the displayed calculation remains arithmetically correct but no longer explains the actual operating behavior. Identify which state variable or energy stream has been excluded, whether the error would tend to make the prediction high or low, and which observation could reveal the discrepancy. Where the sign of the discrepancy depends on coupled effects, give both plausible directions instead of selecting one without evidence.

### 5. Measurement and independent verification

**Suggested evidence:** Record identity, charge, leak records, servicing conditions and end-of-life recovery. Define instrument location, calibration state, sample rate, expected operating condition and averaging period. Record the physical configuration, controller state, weather or ambient condition and any recent service changes. Establish a repeated baseline where practical; a one-off value can be distorted by transient heat storage or instrument delay. Preserve raw observations separately from processed plots so a different analyst can independently reproduce the result.

For uncertainty, start with a bounded input sensitivity calculation. Identify the most influential parameter and estimate how its uncertainty propagates through the working relation. If the input depends on other measured quantities, note their correlation instead of automatically treating errors as independent. Keep the measurement units and calibration references attached to each row in the results table. A plotted model curve is not experimental data; if both are presented, label them differently and show measurement points with their uncertainty where available.

### 6. Design choice and engineering trade-offs

**Decision problem:** Apply relevant current safety and environmental requirements; the textbook does not endorse a retrofit. Translate this into a decision matrix with at least one primary performance measure and one hard constraint. State whether the option is being evaluated for capacity, comfort, electricity consumption, reliability, lifecycle cost or emissions. Some options improve one objective while increasing fan power, refrigerant charge, maintenance burden or control complexity. Do not call the option superior without declaring the weighted objective or the nonnegotiable constraint.

### 7. Practice and assessment

1. **Concept:** Explain the physical meaning of `Direct mass released = charge × leakage fraction` and identify at least two assumptions necessary for its use.
2. **Numerical:** Repeat the example with all units shown: A hypothetical 4 kg system losing 5% of its charge releases 0.20 kg of refrigerant; climate weighting additionally requires verified refrigerant-specific data. State an answer at a precision justified by the input values.
4. **Diagnosis:** Design a plausible scenario in which the original result is misleading because of: Low global-warming potential does not automatically imply low total impact, easy availability or harmless operation. Specify an independent observation to test the explanation.
5. **Experiment:** Convert the suggested verification into a small data-collection plan: Record identity, charge, leak records, servicing conditions and end-of-life recovery.
6. **Decision:** Defend a recommendation using the lesson's trade-off: Apply relevant current safety and environmental requirements; the textbook does not endorse a retrofit. Identify one operating condition that might reverse your conclusion.

**Checking rubric:** Give credit for a correct model boundary and quantities, transparent unit conversion, dimensional reasonableness, explicit limitations and a falsifiable verification strategy. Do not award full credit for copying a plausible-looking number without explaining what it measures. For an open-ended design response, alternative answers may be valid when their constraints and evidence are coherent.


---

## U03-L02 — Compressor work and isentropic benchmarks

**Outcome:** Interpret compressor work and isentropic benchmarks, perform a traceable estimate, diagnose a limitation, and explain how evidence could change the associated engineering decision.

### 1. Engineering problem and purpose

A replacement refrigerant or compressor is considered for an existing cold-storage machine. Pressures, oil compatibility, capacities, operating envelope and safety requirements must be reviewed together. The specific issue here is **compressor work and isentropic benchmarks**. Interpret component duties and the constraints imposed by properties, pressure ratios, refrigerant choice and control hardware. This problem matters because a mechanical design must perform across several operating states rather than just one conveniently chosen measurement. A useful first result is a quantity with clear units, an identified system boundary and a stated purpose; it is not a prediction for arbitrary buildings or products.

### 2. Governing idea and modeling assumptions

**Working relation:** `eta_is = (h2s−h1)/(h2−h1)`.

This equation should be interpreted together with its reference states. Write down every independent variable, with its numerical units, and keep any temperature-difference term separate from an absolute thermodynamic temperature. For a steady-flow energy equation, indicate the mass-flow definition; for a moist-air relation, specify whether the denominator is dry-air mass; for a performance ratio, ensure numerator and denominator cover the same test period. If the result is dimensionless, explain what physical quantities were compared.

Isentropic efficiency ignores motor, drive, shell, and oil-related losses unless explicitly defined. This is a reason to retain the equation's scope in every answer. A classroom relation may assume ideal-gas behavior, constant specific heat, steady mass balance, uniform mixing, negligible leakage, or a fixed equipment efficiency. Real systems can violate several of these assumptions simultaneously, particularly during a changing load. The correct response is to identify the assumption and collect appropriate evidence, rather than silently adding correction factors whose source is unclear.

### 3. Fully specified numerical teaching example

**Assumed inputs and computed answer:** With ideal enthalpy rise 36 kJ/kg and actual rise 48 kJ/kg, the simplified isentropic efficiency is 0.75.

Reproduce the result using the equation rather than copying the displayed answer. Convert all values to compatible units before substitution. Distinguish kW from kWh, kPa from Pa, and a percentage from a dimensionless fraction. Then perform three small checks: does the output have the expected dimensions, is its sign physically meaningful for the chosen reference direction, and does it approach a sensible limiting value when the driving difference or mass flow tends toward zero? If a limiting case gives a contradiction, examine the equation and model boundary before trusting the decimals.

### 4. Physical interpretation and failure analysis

The immediate diagnostic trap in this lesson is the following: Isentropic efficiency ignores motor, drive, shell, and oil-related losses unless explicitly defined. Construct a counterexample where the displayed calculation remains arithmetically correct but no longer explains the actual operating behavior. Identify which state variable or energy stream has been excluded, whether the error would tend to make the prediction high or low, and which observation could reveal the discrepancy. Where the sign of the discrepancy depends on coupled effects, give both plausible directions instead of selecting one without evidence.

### 5. Measurement and independent verification

**Suggested evidence:** Compare suction/discharge state data with an evaluated property model and electric power. Define instrument location, calibration state, sample rate, expected operating condition and averaging period. Record the physical configuration, controller state, weather or ambient condition and any recent service changes. Establish a repeated baseline where practical; a one-off value can be distorted by transient heat storage or instrument delay. Preserve raw observations separately from processed plots so a different analyst can independently reproduce the result.

For uncertainty, start with a bounded input sensitivity calculation. Identify the most influential parameter and estimate how its uncertainty propagates through the working relation. If the input depends on other measured quantities, note their correlation instead of automatically treating errors as independent. Keep the measurement units and calibration references attached to each row in the results table. A plotted model curve is not experimental data; if both are presented, label them differently and show measurement points with their uncertainty where available.

### 6. Design choice and engineering trade-offs

**Decision problem:** Avoid choosing a compressor from one efficiency point when the operating envelope changes. Translate this into a decision matrix with at least one primary performance measure and one hard constraint. State whether the option is being evaluated for capacity, comfort, electricity consumption, reliability, lifecycle cost or emissions. Some options improve one objective while increasing fan power, refrigerant charge, maintenance burden or control complexity. Do not call the option superior without declaring the weighted objective or the nonnegotiable constraint.

### 7. Practice and assessment

1. **Concept:** Explain the physical meaning of `eta_is = (h2s−h1)/(h2−h1)` and identify at least two assumptions necessary for its use.
2. **Numerical:** Repeat the example with all units shown: With ideal enthalpy rise 36 kJ/kg and actual rise 48 kJ/kg, the simplified isentropic efficiency is 0.75. State an answer at a precision justified by the input values.
4. **Diagnosis:** Design a plausible scenario in which the original result is misleading because of: Isentropic efficiency ignores motor, drive, shell, and oil-related losses unless explicitly defined. Specify an independent observation to test the explanation.
5. **Experiment:** Convert the suggested verification into a small data-collection plan: Compare suction/discharge state data with an evaluated property model and electric power.
6. **Decision:** Defend a recommendation using the lesson's trade-off: Avoid choosing a compressor from one efficiency point when the operating envelope changes. Identify one operating condition that might reverse your conclusion.

**Checking rubric:** Give credit for a correct model boundary and quantities, transparent unit conversion, dimensional reasonableness, explicit limitations and a falsifiable verification strategy. Do not award full credit for copying a plausible-looking number without explaining what it measures. For an open-ended design response, alternative answers may be valid when their constraints and evidence are coherent.


---

## U03-L03 — Condenser capacity and temperature approach

**Outcome:** Interpret condenser capacity and temperature approach, perform a traceable estimate, diagnose a limitation, and explain how evidence could change the associated engineering decision.

### 1. Engineering problem and purpose

A replacement refrigerant or compressor is considered for an existing cold-storage machine. Pressures, oil compatibility, capacities, operating envelope and safety requirements must be reviewed together. The specific issue here is **condenser capacity and temperature approach**. Interpret component duties and the constraints imposed by properties, pressure ratios, refrigerant choice and control hardware. This problem matters because a mechanical design must perform across several operating states rather than just one conveniently chosen measurement. A useful first result is a quantity with clear units, an identified system boundary and a stated purpose; it is not a prediction for arbitrary buildings or products.

### 2. Governing idea and modeling assumptions

**Working relation:** `Q_cond = Q_evap+W_comp for a steady ideal energy boundary`.

This equation should be interpreted together with its reference states. Write down every independent variable, with its numerical units, and keep any temperature-difference term separate from an absolute thermodynamic temperature. For a steady-flow energy equation, indicate the mass-flow definition; for a moist-air relation, specify whether the denominator is dry-air mass; for a performance ratio, ensure numerator and denominator cover the same test period. If the result is dimensionless, explain what physical quantities were compared.

The condenser rejects more heat than the evaporator absorbs when compressor work is positive. This is a reason to retain the equation's scope in every answer. A classroom relation may assume ideal-gas behavior, constant specific heat, steady mass balance, uniform mixing, negligible leakage, or a fixed equipment efficiency. Real systems can violate several of these assumptions simultaneously, particularly during a changing load. The correct response is to identify the assumption and collect appropriate evidence, rather than silently adding correction factors whose source is unclear.

### 3. Fully specified numerical teaching example

**Assumed inputs and computed answer:** An evaporator removing 12 kW and compressor adding 3.5 kW reject approximately 15.5 kW at the condenser before ancillary adjustments.

Reproduce the result using the equation rather than copying the displayed answer. Convert all values to compatible units before substitution. Distinguish kW from kWh, kPa from Pa, and a percentage from a dimensionless fraction. Then perform three small checks: does the output have the expected dimensions, is its sign physically meaningful for the chosen reference direction, and does it approach a sensible limiting value when the driving difference or mass flow tends toward zero? If a limiting case gives a contradiction, examine the equation and model boundary before trusting the decimals.

### 4. Physical interpretation and failure analysis

The immediate diagnostic trap in this lesson is the following: The condenser rejects more heat than the evaporator absorbs when compressor work is positive. Construct a counterexample where the displayed calculation remains arithmetically correct but no longer explains the actual operating behavior. Identify which state variable or energy stream has been excluded, whether the error would tend to make the prediction high or low, and which observation could reveal the discrepancy. Where the sign of the discrepancy depends on coupled effects, give both plausible directions instead of selecting one without evidence.

### 5. Measurement and independent verification

**Suggested evidence:** Measure heat-rejection stream flow and temperature differences at representative loads. Define instrument location, calibration state, sample rate, expected operating condition and averaging period. Record the physical configuration, controller state, weather or ambient condition and any recent service changes. Establish a repeated baseline where practical; a one-off value can be distorted by transient heat storage or instrument delay. Preserve raw observations separately from processed plots so a different analyst can independently reproduce the result.

For uncertainty, start with a bounded input sensitivity calculation. Identify the most influential parameter and estimate how its uncertainty propagates through the working relation. If the input depends on other measured quantities, note their correlation instead of automatically treating errors as independent. Keep the measurement units and calibration references attached to each row in the results table. A plotted model curve is not experimental data; if both are presented, label them differently and show measurement points with their uncertainty where available.

### 6. Design choice and engineering trade-offs

**Decision problem:** Check fouling, ambient temperature and flow limitations before upsizing the condenser. Translate this into a decision matrix with at least one primary performance measure and one hard constraint. State whether the option is being evaluated for capacity, comfort, electricity consumption, reliability, lifecycle cost or emissions. Some options improve one objective while increasing fan power, refrigerant charge, maintenance burden or control complexity. Do not call the option superior without declaring the weighted objective or the nonnegotiable constraint.

### 7. Practice and assessment

1. **Concept:** Explain the physical meaning of `Q_cond = Q_evap+W_comp for a steady ideal energy boundary` and identify at least two assumptions necessary for its use.
2. **Numerical:** Repeat the example with all units shown: An evaporator removing 12 kW and compressor adding 3.5 kW reject approximately 15.5 kW at the condenser before ancillary adjustments. State an answer at a precision justified by the input values.
4. **Diagnosis:** Design a plausible scenario in which the original result is misleading because of: The condenser rejects more heat than the evaporator absorbs when compressor work is positive. Specify an independent observation to test the explanation.
5. **Experiment:** Convert the suggested verification into a small data-collection plan: Measure heat-rejection stream flow and temperature differences at representative loads.
6. **Decision:** Defend a recommendation using the lesson's trade-off: Check fouling, ambient temperature and flow limitations before upsizing the condenser. Identify one operating condition that might reverse your conclusion.

**Checking rubric:** Give credit for a correct model boundary and quantities, transparent unit conversion, dimensional reasonableness, explicit limitations and a falsifiable verification strategy. Do not award full credit for copying a plausible-looking number without explaining what it measures. For an open-ended design response, alternative answers may be valid when their constraints and evidence are coherent.


---

## U03-L04 — Evaporator effectiveness and frosting

**Outcome:** Interpret evaporator effectiveness and frosting, perform a traceable estimate, diagnose a limitation, and explain how evidence could change the associated engineering decision.

### 1. Engineering problem and purpose

A replacement refrigerant or compressor is considered for an existing cold-storage machine. Pressures, oil compatibility, capacities, operating envelope and safety requirements must be reviewed together. The specific issue here is **evaporator effectiveness and frosting**. Interpret component duties and the constraints imposed by properties, pressure ratios, refrigerant choice and control hardware. This problem matters because a mechanical design must perform across several operating states rather than just one conveniently chosen measurement. A useful first result is a quantity with clear units, an identified system boundary and a stated purpose; it is not a prediction for arbitrary buildings or products.

### 2. Governing idea and modeling assumptions

**Working relation:** `epsilon = Q_actual/Q_max for a consistently defined exchanger limit`.

This equation should be interpreted together with its reference states. Write down every independent variable, with its numerical units, and keep any temperature-difference term separate from an absolute thermodynamic temperature. For a steady-flow energy equation, indicate the mass-flow definition; for a moist-air relation, specify whether the denominator is dry-air mass; for a performance ratio, ensure numerator and denominator cover the same test period. If the result is dimensionless, explain what physical quantities were compared.

Frost, condensate and fan heat alter performance; effectiveness is not a substitute for coil manufacturer curves. This is a reason to retain the equation's scope in every answer. A classroom relation may assume ideal-gas behavior, constant specific heat, steady mass balance, uniform mixing, negligible leakage, or a fixed equipment efficiency. Real systems can violate several of these assumptions simultaneously, particularly during a changing load. The correct response is to identify the assumption and collect appropriate evidence, rather than silently adding correction factors whose source is unclear.

### 3. Fully specified numerical teaching example

**Assumed inputs and computed answer:** A simplified exchanger delivering 6 kW against a maximum theoretical 7.5 kW has effectiveness 0.80.

Reproduce the result using the equation rather than copying the displayed answer. Convert all values to compatible units before substitution. Distinguish kW from kWh, kPa from Pa, and a percentage from a dimensionless fraction. Then perform three small checks: does the output have the expected dimensions, is its sign physically meaningful for the chosen reference direction, and does it approach a sensible limiting value when the driving difference or mass flow tends toward zero? If a limiting case gives a contradiction, examine the equation and model boundary before trusting the decimals.

### 4. Physical interpretation and failure analysis

The immediate diagnostic trap in this lesson is the following: Frost, condensate and fan heat alter performance; effectiveness is not a substitute for coil manufacturer curves. Construct a counterexample where the displayed calculation remains arithmetically correct but no longer explains the actual operating behavior. Identify which state variable or energy stream has been excluded, whether the error would tend to make the prediction high or low, and which observation could reveal the discrepancy. Where the sign of the discrepancy depends on coupled effects, give both plausible directions instead of selecting one without evidence.

### 5. Measurement and independent verification

**Suggested evidence:** Track air-side pressure drop, frost accumulation, condensate and exit state. Define instrument location, calibration state, sample rate, expected operating condition and averaging period. Record the physical configuration, controller state, weather or ambient condition and any recent service changes. Establish a repeated baseline where practical; a one-off value can be distorted by transient heat storage or instrument delay. Preserve raw observations separately from processed plots so a different analyst can independently reproduce the result.

For uncertainty, start with a bounded input sensitivity calculation. Identify the most influential parameter and estimate how its uncertainty propagates through the working relation. If the input depends on other measured quantities, note their correlation instead of automatically treating errors as independent. Keep the measurement units and calibration references attached to each row in the results table. A plotted model curve is not experimental data; if both are presented, label them differently and show measurement points with their uncertainty where available.

### 6. Design choice and engineering trade-offs

**Decision problem:** Include defrost intervals and food-safe requirements when estimating a cold room load. Translate this into a decision matrix with at least one primary performance measure and one hard constraint. State whether the option is being evaluated for capacity, comfort, electricity consumption, reliability, lifecycle cost or emissions. Some options improve one objective while increasing fan power, refrigerant charge, maintenance burden or control complexity. Do not call the option superior without declaring the weighted objective or the nonnegotiable constraint.

### 7. Practice and assessment

1. **Concept:** Explain the physical meaning of `epsilon = Q_actual/Q_max for a consistently defined exchanger limit` and identify at least two assumptions necessary for its use.
2. **Numerical:** Repeat the example with all units shown: A simplified exchanger delivering 6 kW against a maximum theoretical 7.5 kW has effectiveness 0.80. State an answer at a precision justified by the input values.
4. **Diagnosis:** Design a plausible scenario in which the original result is misleading because of: Frost, condensate and fan heat alter performance; effectiveness is not a substitute for coil manufacturer curves. Specify an independent observation to test the explanation.
5. **Experiment:** Convert the suggested verification into a small data-collection plan: Track air-side pressure drop, frost accumulation, condensate and exit state.
6. **Decision:** Defend a recommendation using the lesson's trade-off: Include defrost intervals and food-safe requirements when estimating a cold room load. Identify one operating condition that might reverse your conclusion.

**Checking rubric:** Give credit for a correct model boundary and quantities, transparent unit conversion, dimensional reasonableness, explicit limitations and a falsifiable verification strategy. Do not award full credit for copying a plausible-looking number without explaining what it measures. For an open-ended design response, alternative answers may be valid when their constraints and evidence are coherent.


---

## U03-L05 — Expansion devices and refrigerant inventory

**Outcome:** Interpret expansion devices and refrigerant inventory, perform a traceable estimate, diagnose a limitation, and explain how evidence could change the associated engineering decision.

### 1. Engineering problem and purpose

A replacement refrigerant or compressor is considered for an existing cold-storage machine. Pressures, oil compatibility, capacities, operating envelope and safety requirements must be reviewed together. The specific issue here is **expansion devices and refrigerant inventory**. Interpret component duties and the constraints imposed by properties, pressure ratios, refrigerant choice and control hardware. This problem matters because a mechanical design must perform across several operating states rather than just one conveniently chosen measurement. A useful first result is a quantity with clear units, an identified system boundary and a stated purpose; it is not a prediction for arbitrary buildings or products.

### 2. Governing idea and modeling assumptions

**Working relation:** `Q_L = m_dot_ref (h1−h4)`.

This equation should be interpreted together with its reference states. Write down every independent variable, with its numerical units, and keep any temperature-difference term separate from an absolute thermodynamic temperature. For a steady-flow energy equation, indicate the mass-flow definition; for a moist-air relation, specify whether the denominator is dry-air mass; for a performance ratio, ensure numerator and denominator cover the same test period. If the result is dimensionless, explain what physical quantities were compared.

Changing the valve can shift superheat and distribution rather than simply increasing mass flow. This is a reason to retain the equation's scope in every answer. A classroom relation may assume ideal-gas behavior, constant specific heat, steady mass balance, uniform mixing, negligible leakage, or a fixed equipment efficiency. Real systems can violate several of these assumptions simultaneously, particularly during a changing load. The correct response is to identify the assumption and collect appropriate evidence, rather than silently adding correction factors whose source is unclear.

### 3. Fully specified numerical teaching example

**Assumed inputs and computed answer:** At 0.04 kg/s and 145 kJ/kg evaporator enthalpy difference, idealized cooling capacity is 5.8 kW.

Reproduce the result using the equation rather than copying the displayed answer. Convert all values to compatible units before substitution. Distinguish kW from kWh, kPa from Pa, and a percentage from a dimensionless fraction. Then perform three small checks: does the output have the expected dimensions, is its sign physically meaningful for the chosen reference direction, and does it approach a sensible limiting value when the driving difference or mass flow tends toward zero? If a limiting case gives a contradiction, examine the equation and model boundary before trusting the decimals.

### 4. Physical interpretation and failure analysis

The immediate diagnostic trap in this lesson is the following: Changing the valve can shift superheat and distribution rather than simply increasing mass flow. Construct a counterexample where the displayed calculation remains arithmetically correct but no longer explains the actual operating behavior. Identify which state variable or energy stream has been excluded, whether the error would tend to make the prediction high or low, and which observation could reveal the discrepancy. Where the sign of the discrepancy depends on coupled effects, give both plausible directions instead of selecting one without evidence.

### 5. Measurement and independent verification

**Suggested evidence:** Use inlet/outlet pressure, measured temperature, and appropriate refrigerant property estimates. Define instrument location, calibration state, sample rate, expected operating condition and averaging period. Record the physical configuration, controller state, weather or ambient condition and any recent service changes. Establish a repeated baseline where practical; a one-off value can be distorted by transient heat storage or instrument delay. Preserve raw observations separately from processed plots so a different analyst can independently reproduce the result.

For uncertainty, start with a bounded input sensitivity calculation. Identify the most influential parameter and estimate how its uncertainty propagates through the working relation. If the input depends on other measured quantities, note their correlation instead of automatically treating errors as independent. Keep the measurement units and calibration references attached to each row in the results table. A plotted model curve is not experimental data; if both are presented, label them differently and show measurement points with their uncertainty where available.

### 6. Design choice and engineering trade-offs

**Decision problem:** Treat charge and liquid management as specialist service tasks, not classroom experiments. Translate this into a decision matrix with at least one primary performance measure and one hard constraint. State whether the option is being evaluated for capacity, comfort, electricity consumption, reliability, lifecycle cost or emissions. Some options improve one objective while increasing fan power, refrigerant charge, maintenance burden or control complexity. Do not call the option superior without declaring the weighted objective or the nonnegotiable constraint.

### 7. Practice and assessment

1. **Concept:** Explain the physical meaning of `Q_L = m_dot_ref (h1−h4)` and identify at least two assumptions necessary for its use.
2. **Numerical:** Repeat the example with all units shown: At 0.04 kg/s and 145 kJ/kg evaporator enthalpy difference, idealized cooling capacity is 5.8 kW. State an answer at a precision justified by the input values.
4. **Diagnosis:** Design a plausible scenario in which the original result is misleading because of: Changing the valve can shift superheat and distribution rather than simply increasing mass flow. Specify an independent observation to test the explanation.
5. **Experiment:** Convert the suggested verification into a small data-collection plan: Use inlet/outlet pressure, measured temperature, and appropriate refrigerant property estimates.
6. **Decision:** Defend a recommendation using the lesson's trade-off: Treat charge and liquid management as specialist service tasks, not classroom experiments. Identify one operating condition that might reverse your conclusion.

**Checking rubric:** Give credit for a correct model boundary and quantities, transparent unit conversion, dimensional reasonableness, explicit limitations and a falsifiable verification strategy. Do not award full credit for copying a plausible-looking number without explaining what it measures. For an open-ended design response, alternative answers may be valid when their constraints and evidence are coherent.


---

