# Unit 08: Integrated Design, Commissioning and Sustainability

**Course Code**: RAC 308 · **Level**: Advanced Undergraduate Engineering

## Unit Overview & Physical Foundations

This comprehensive university textbook unit covers the theoretical framework, physical modeling, mathematical governing equations, and engineering applications of **Integrated Design, Commissioning and Sustainability**.

## U08-L01 — Requirements, selection and constraint tracing

**Outcome:** Interpret requirements, selection and constraint tracing, perform a traceable estimate, diagnose a limitation, and explain how evidence could change the associated engineering decision.

### 1. Engineering problem and purpose

A project team hands over a new HVAC installation. Design intent, instrument readings, operator training, refrigerant management and maintenance plans determine whether the modeled benefits occur. The specific issue here is **requirements, selection and constraint tracing**. Evaluate alternatives through reproducible design decisions, commissioning evidence, fault diagnosis, and lifecycle accounting. This problem matters because a mechanical design must perform across several operating states rather than just one conveniently chosen measurement. A useful first result is a quantity with clear units, an identified system boundary and a stated purpose; it is not a prediction for arbitrary buildings or products.

### 2. Governing idea and modeling assumptions

**Working relation:** `Capacity_margin = (Q_selected−Q_design)/Q_design`.

This equation should be interpreted together with its reference states. Write down every independent variable, with its numerical units, and keep any temperature-difference term separate from an absolute thermodynamic temperature. For a steady-flow energy equation, indicate the mass-flow definition; for a moist-air relation, specify whether the denominator is dry-air mass; for a performance ratio, ensure numerator and denominator cover the same test period. If the result is dimensionless, explain what physical quantities were compared.

Oversizing is not free safety; it can worsen humidity control and cycling. This is a reason to retain the equation's scope in every answer. A classroom relation may assume ideal-gas behavior, constant specific heat, steady mass balance, uniform mixing, negligible leakage, or a fixed equipment efficiency. Real systems can violate several of these assumptions simultaneously, particularly during a changing load. The correct response is to identify the assumption and collect appropriate evidence, rather than silently adding correction factors whose source is unclear.

### 3. Fully specified numerical teaching example

**Assumed inputs and computed answer:** Selecting 12 kW against a documented 10 kW design load creates 20% nominal capacity margin, before matching actual rating conditions.

Reproduce the result using the equation rather than copying the displayed answer. Convert all values to compatible units before substitution. Distinguish kW from kWh, kPa from Pa, and a percentage from a dimensionless fraction. Then perform three small checks: does the output have the expected dimensions, is its sign physically meaningful for the chosen reference direction, and does it approach a sensible limiting value when the driving difference or mass flow tends toward zero? If a limiting case gives a contradiction, examine the equation and model boundary before trusting the decimals.

### 4. Physical interpretation and failure analysis

The immediate diagnostic trap in this lesson is the following: Oversizing is not free safety; it can worsen humidity control and cycling. Construct a counterexample where the displayed calculation remains arithmetically correct but no longer explains the actual operating behavior. Identify which state variable or energy stream has been excluded, whether the error would tend to make the prediction high or low, and which observation could reveal the discrepancy. Where the sign of the discrepancy depends on coupled effects, give both plausible directions instead of selecting one without evidence.

### 5. Measurement and independent verification

**Suggested evidence:** Trace each performance claim to a specified rating condition and an independent check. Define instrument location, calibration state, sample rate, expected operating condition and averaging period. Record the physical configuration, controller state, weather or ambient condition and any recent service changes. Establish a repeated baseline where practical; a one-off value can be distorted by transient heat storage or instrument delay. Preserve raw observations separately from processed plots so a different analyst can independently reproduce the result.

For uncertainty, start with a bounded input sensitivity calculation. Identify the most influential parameter and estimate how its uncertainty propagates through the working relation. If the input depends on other measured quantities, note their correlation instead of automatically treating errors as independent. Keep the measurement units and calibration references attached to each row in the results table. A plotted model curve is not experimental data; if both are presented, label them differently and show measurement points with their uncertainty where available.

### 6. Design choice and engineering trade-offs

**Decision problem:** Use a requirement matrix distinguishing nonnegotiable, preferred and uncertain criteria. Translate this into a decision matrix with at least one primary performance measure and one hard constraint. State whether the option is being evaluated for capacity, comfort, electricity consumption, reliability, lifecycle cost or emissions. Some options improve one objective while increasing fan power, refrigerant charge, maintenance burden or control complexity. Do not call the option superior without declaring the weighted objective or the nonnegotiable constraint.

### 7. Practice and assessment

1. **Concept:** Explain the physical meaning of `Capacity_margin = (Q_selected−Q_design)/Q_design` and identify at least two assumptions necessary for its use.
2. **Numerical:** Repeat the example with all units shown: Selecting 12 kW against a documented 10 kW design load creates 20% nominal capacity margin, before matching actual rating conditions. State an answer at a precision justified by the input values.
4. **Diagnosis:** Design a plausible scenario in which the original result is misleading because of: Oversizing is not free safety; it can worsen humidity control and cycling. Specify an independent observation to test the explanation.
5. **Experiment:** Convert the suggested verification into a small data-collection plan: Trace each performance claim to a specified rating condition and an independent check.
6. **Decision:** Defend a recommendation using the lesson's trade-off: Use a requirement matrix distinguishing nonnegotiable, preferred and uncertain criteria. Identify one operating condition that might reverse your conclusion.

**Checking rubric:** Give credit for a correct model boundary and quantities, transparent unit conversion, dimensional reasonableness, explicit limitations and a falsifiable verification strategy. Do not award full credit for copying a plausible-looking number without explaining what it measures. For an open-ended design response, alternative answers may be valid when their constraints and evidence are coherent.


---

## U08-L02 — Commissioning tests and measurement uncertainty

**Outcome:** Interpret commissioning tests and measurement uncertainty, perform a traceable estimate, diagnose a limitation, and explain how evidence could change the associated engineering decision.

### 1. Engineering problem and purpose

A project team hands over a new HVAC installation. Design intent, instrument readings, operator training, refrigerant management and maintenance plans determine whether the modeled benefits occur. The specific issue here is **commissioning tests and measurement uncertainty**. Evaluate alternatives through reproducible design decisions, commissioning evidence, fault diagnosis, and lifecycle accounting. This problem matters because a mechanical design must perform across several operating states rather than just one conveniently chosen measurement. A useful first result is a quantity with clear units, an identified system boundary and a stated purpose; it is not a prediction for arbitrary buildings or products.

### 2. Governing idea and modeling assumptions

**Working relation:** `u_Q/Q ≈ sqrt((u_m/m)^2+(u_dT/dT)^2) for independent first-order relative uncertainties`.

This equation should be interpreted together with its reference states. Write down every independent variable, with its numerical units, and keep any temperature-difference term separate from an absolute thermodynamic temperature. For a steady-flow energy equation, indicate the mass-flow definition; for a moist-air relation, specify whether the denominator is dry-air mass; for a performance ratio, ensure numerator and denominator cover the same test period. If the result is dimensionless, explain what physical quantities were compared.

The root-sum-square formula relies on assumptions about independence and linearization. This is a reason to retain the equation's scope in every answer. A classroom relation may assume ideal-gas behavior, constant specific heat, steady mass balance, uniform mixing, negligible leakage, or a fixed equipment efficiency. Real systems can violate several of these assumptions simultaneously, particularly during a changing load. The correct response is to identify the assumption and collect appropriate evidence, rather than silently adding correction factors whose source is unclear.

### 3. Fully specified numerical teaching example

**Assumed inputs and computed answer:** If flow uncertainty is 3% and temperature-difference uncertainty is 4%, a simple independent RSS estimate is 5% for Q∝mΔT.

Reproduce the result using the equation rather than copying the displayed answer. Convert all values to compatible units before substitution. Distinguish kW from kWh, kPa from Pa, and a percentage from a dimensionless fraction. Then perform three small checks: does the output have the expected dimensions, is its sign physically meaningful for the chosen reference direction, and does it approach a sensible limiting value when the driving difference or mass flow tends toward zero? If a limiting case gives a contradiction, examine the equation and model boundary before trusting the decimals.

### 4. Physical interpretation and failure analysis

The immediate diagnostic trap in this lesson is the following: The root-sum-square formula relies on assumptions about independence and linearization. Construct a counterexample where the displayed calculation remains arithmetically correct but no longer explains the actual operating behavior. Identify which state variable or energy stream has been excluded, whether the error would tend to make the prediction high or low, and which observation could reveal the discrepancy. Where the sign of the discrepancy depends on coupled effects, give both plausible directions instead of selecting one without evidence.

### 5. Measurement and independent verification

**Suggested evidence:** Establish instrumentation calibration, sampling alignment, acceptance conditions and baseline. Define instrument location, calibration state, sample rate, expected operating condition and averaging period. Record the physical configuration, controller state, weather or ambient condition and any recent service changes. Establish a repeated baseline where practical; a one-off value can be distorted by transient heat storage or instrument delay. Preserve raw observations separately from processed plots so a different analyst can independently reproduce the result.

For uncertainty, start with a bounded input sensitivity calculation. Identify the most influential parameter and estimate how its uncertainty propagates through the working relation. If the input depends on other measured quantities, note their correlation instead of automatically treating errors as independent. Keep the measurement units and calibration references attached to each row in the results table. A plotted model curve is not experimental data; if both are presented, label them differently and show measurement points with their uncertainty where available.

### 6. Design choice and engineering trade-offs

**Decision problem:** Reject pass/fail claims that conceal uncertainty or compare incompatible operational states. Translate this into a decision matrix with at least one primary performance measure and one hard constraint. State whether the option is being evaluated for capacity, comfort, electricity consumption, reliability, lifecycle cost or emissions. Some options improve one objective while increasing fan power, refrigerant charge, maintenance burden or control complexity. Do not call the option superior without declaring the weighted objective or the nonnegotiable constraint.

### 7. Practice and assessment

1. **Concept:** Explain the physical meaning of `u_Q/Q ≈ sqrt((u_m/m)^2+(u_dT/dT)^2) for independent first-order relative uncertainties` and identify at least two assumptions necessary for its use.
2. **Numerical:** Repeat the example with all units shown: If flow uncertainty is 3% and temperature-difference uncertainty is 4%, a simple independent RSS estimate is 5% for Q∝mΔT. State an answer at a precision justified by the input values.
4. **Diagnosis:** Design a plausible scenario in which the original result is misleading because of: The root-sum-square formula relies on assumptions about independence and linearization. Specify an independent observation to test the explanation.
5. **Experiment:** Convert the suggested verification into a small data-collection plan: Establish instrumentation calibration, sampling alignment, acceptance conditions and baseline.
6. **Decision:** Defend a recommendation using the lesson's trade-off: Reject pass/fail claims that conceal uncertainty or compare incompatible operational states. Identify one operating condition that might reverse your conclusion.

**Checking rubric:** Give credit for a correct model boundary and quantities, transparent unit conversion, dimensional reasonableness, explicit limitations and a falsifiable verification strategy. Do not award full credit for copying a plausible-looking number without explaining what it measures. For an open-ended design response, alternative answers may be valid when their constraints and evidence are coherent.


---

## U08-L03 — Fault detection and diagnostic hypotheses

**Outcome:** Interpret fault detection and diagnostic hypotheses, perform a traceable estimate, diagnose a limitation, and explain how evidence could change the associated engineering decision.

### 1. Engineering problem and purpose

A project team hands over a new HVAC installation. Design intent, instrument readings, operator training, refrigerant management and maintenance plans determine whether the modeled benefits occur. The specific issue here is **fault detection and diagnostic hypotheses**. Evaluate alternatives through reproducible design decisions, commissioning evidence, fault diagnosis, and lifecycle accounting. This problem matters because a mechanical design must perform across several operating states rather than just one conveniently chosen measurement. A useful first result is a quantity with clear units, an identified system boundary and a stated purpose; it is not a prediction for arbitrary buildings or products.

### 2. Governing idea and modeling assumptions

**Working relation:** `Residual r = y_measured−y_model`.

This equation should be interpreted together with its reference states. Write down every independent variable, with its numerical units, and keep any temperature-difference term separate from an absolute thermodynamic temperature. For a steady-flow energy equation, indicate the mass-flow definition; for a moist-air relation, specify whether the denominator is dry-air mass; for a performance ratio, ensure numerator and denominator cover the same test period. If the result is dimensionless, explain what physical quantities were compared.

The same residual could arise from flow, dirty heat exchangers, sensor bias or incorrect input assumptions. This is a reason to retain the equation's scope in every answer. A classroom relation may assume ideal-gas behavior, constant specific heat, steady mass balance, uniform mixing, negligible leakage, or a fixed equipment efficiency. Real systems can violate several of these assumptions simultaneously, particularly during a changing load. The correct response is to identify the assumption and collect appropriate evidence, rather than silently adding correction factors whose source is unclear.

### 3. Fully specified numerical teaching example

**Assumed inputs and computed answer:** A supply temperature of 17 °C against a model estimate of 14 °C gives a +3 K residual that is evidence of disagreement, not identification of a unique fault.

Reproduce the result using the equation rather than copying the displayed answer. Convert all values to compatible units before substitution. Distinguish kW from kWh, kPa from Pa, and a percentage from a dimensionless fraction. Then perform three small checks: does the output have the expected dimensions, is its sign physically meaningful for the chosen reference direction, and does it approach a sensible limiting value when the driving difference or mass flow tends toward zero? If a limiting case gives a contradiction, examine the equation and model boundary before trusting the decimals.

### 4. Physical interpretation and failure analysis

The immediate diagnostic trap in this lesson is the following: The same residual could arise from flow, dirty heat exchangers, sensor bias or incorrect input assumptions. Construct a counterexample where the displayed calculation remains arithmetically correct but no longer explains the actual operating behavior. Identify which state variable or energy stream has been excluded, whether the error would tend to make the prediction high or low, and which observation could reveal the discrepancy. Where the sign of the discrepancy depends on coupled effects, give both plausible directions instead of selecting one without evidence.

### 5. Measurement and independent verification

**Suggested evidence:** Build a residual signature across pressures, flows, temperatures and power before diagnosis. Define instrument location, calibration state, sample rate, expected operating condition and averaging period. Record the physical configuration, controller state, weather or ambient condition and any recent service changes. Establish a repeated baseline where practical; a one-off value can be distorted by transient heat storage or instrument delay. Preserve raw observations separately from processed plots so a different analyst can independently reproduce the result.

For uncertainty, start with a bounded input sensitivity calculation. Identify the most influential parameter and estimate how its uncertainty propagates through the working relation. If the input depends on other measured quantities, note their correlation instead of automatically treating errors as independent. Keep the measurement units and calibration references attached to each row in the results table. A plotted model curve is not experimental data; if both are presented, label them differently and show measurement points with their uncertainty where available.

### 6. Design choice and engineering trade-offs

**Decision problem:** Use independent verification before recommending maintenance or intrusive adjustments. Translate this into a decision matrix with at least one primary performance measure and one hard constraint. State whether the option is being evaluated for capacity, comfort, electricity consumption, reliability, lifecycle cost or emissions. Some options improve one objective while increasing fan power, refrigerant charge, maintenance burden or control complexity. Do not call the option superior without declaring the weighted objective or the nonnegotiable constraint.

### 7. Practice and assessment

1. **Concept:** Explain the physical meaning of `Residual r = y_measured−y_model` and identify at least two assumptions necessary for its use.
2. **Numerical:** Repeat the example with all units shown: A supply temperature of 17 °C against a model estimate of 14 °C gives a +3 K residual that is evidence of disagreement, not identification of a unique fault. State an answer at a precision justified by the input values.
4. **Diagnosis:** Design a plausible scenario in which the original result is misleading because of: The same residual could arise from flow, dirty heat exchangers, sensor bias or incorrect input assumptions. Specify an independent observation to test the explanation.
5. **Experiment:** Convert the suggested verification into a small data-collection plan: Build a residual signature across pressures, flows, temperatures and power before diagnosis.
6. **Decision:** Defend a recommendation using the lesson's trade-off: Use independent verification before recommending maintenance or intrusive adjustments. Identify one operating condition that might reverse your conclusion.

**Checking rubric:** Give credit for a correct model boundary and quantities, transparent unit conversion, dimensional reasonableness, explicit limitations and a falsifiable verification strategy. Do not award full credit for copying a plausible-looking number without explaining what it measures. For an open-ended design response, alternative answers may be valid when their constraints and evidence are coherent.


---

## U08-L04 — Refrigerant lifecycle and indirect emissions

**Outcome:** Interpret refrigerant lifecycle and indirect emissions, perform a traceable estimate, diagnose a limitation, and explain how evidence could change the associated engineering decision.

### 1. Engineering problem and purpose

A project team hands over a new HVAC installation. Design intent, instrument readings, operator training, refrigerant management and maintenance plans determine whether the modeled benefits occur. The specific issue here is **refrigerant lifecycle and indirect emissions**. Evaluate alternatives through reproducible design decisions, commissioning evidence, fault diagnosis, and lifecycle accounting. This problem matters because a mechanical design must perform across several operating states rather than just one conveniently chosen measurement. A useful first result is a quantity with clear units, an identified system boundary and a stated purpose; it is not a prediction for arbitrary buildings or products.

### 2. Governing idea and modeling assumptions

**Working relation:** `CO2e_direct = m_leaked × GWP with matched definitions and horizon`.

This equation should be interpreted together with its reference states. Write down every independent variable, with its numerical units, and keep any temperature-difference term separate from an absolute thermodynamic temperature. For a steady-flow energy equation, indicate the mass-flow definition; for a moist-air relation, specify whether the denominator is dry-air mass; for a performance ratio, ensure numerator and denominator cover the same test period. If the result is dimensionless, explain what physical quantities were compared.

Refrigerant-specific safety classifications and environmental rules evolve; GWP alone does not select a compliant product. This is a reason to retain the equation's scope in every answer. A classroom relation may assume ideal-gas behavior, constant specific heat, steady mass balance, uniform mixing, negligible leakage, or a fixed equipment efficiency. Real systems can violate several of these assumptions simultaneously, particularly during a changing load. The correct response is to identify the assumption and collect appropriate evidence, rather than silently adding correction factors whose source is unclear.

### 3. Fully specified numerical teaching example

**Assumed inputs and computed answer:** A hypothetical 0.10 kg leak of a refrigerant with assumed GWP 500 represents 50 kg CO2e on that convention; actual metrics need authoritative current values.

Reproduce the result using the equation rather than copying the displayed answer. Convert all values to compatible units before substitution. Distinguish kW from kWh, kPa from Pa, and a percentage from a dimensionless fraction. Then perform three small checks: does the output have the expected dimensions, is its sign physically meaningful for the chosen reference direction, and does it approach a sensible limiting value when the driving difference or mass flow tends toward zero? If a limiting case gives a contradiction, examine the equation and model boundary before trusting the decimals.

### 4. Physical interpretation and failure analysis

The immediate diagnostic trap in this lesson is the following: Refrigerant-specific safety classifications and environmental rules evolve; GWP alone does not select a compliant product. Construct a counterexample where the displayed calculation remains arithmetically correct but no longer explains the actual operating behavior. Identify which state variable or energy stream has been excluded, whether the error would tend to make the prediction high or low, and which observation could reveal the discrepancy. Where the sign of the discrepancy depends on coupled effects, give both plausible directions instead of selecting one without evidence.

### 5. Measurement and independent verification

**Suggested evidence:** Maintain verified refrigerant inventory, leak and recovery records and electricity data. Define instrument location, calibration state, sample rate, expected operating condition and averaging period. Record the physical configuration, controller state, weather or ambient condition and any recent service changes. Establish a repeated baseline where practical; a one-off value can be distorted by transient heat storage or instrument delay. Preserve raw observations separately from processed plots so a different analyst can independently reproduce the result.

For uncertainty, start with a bounded input sensitivity calculation. Identify the most influential parameter and estimate how its uncertainty propagates through the working relation. If the input depends on other measured quantities, note their correlation instead of automatically treating errors as independent. Keep the measurement units and calibration references attached to each row in the results table. A plotted model curve is not experimental data; if both are presented, label them differently and show measurement points with their uncertainty where available.

### 6. Design choice and engineering trade-offs

**Decision problem:** Include both direct leakage and indirect operating energy when comparing system options. Translate this into a decision matrix with at least one primary performance measure and one hard constraint. State whether the option is being evaluated for capacity, comfort, electricity consumption, reliability, lifecycle cost or emissions. Some options improve one objective while increasing fan power, refrigerant charge, maintenance burden or control complexity. Do not call the option superior without declaring the weighted objective or the nonnegotiable constraint.

### 7. Practice and assessment

1. **Concept:** Explain the physical meaning of `CO2e_direct = m_leaked × GWP with matched definitions and horizon` and identify at least two assumptions necessary for its use.
2. **Numerical:** Repeat the example with all units shown: A hypothetical 0.10 kg leak of a refrigerant with assumed GWP 500 represents 50 kg CO2e on that convention; actual metrics need authoritative current values. State an answer at a precision justified by the input values.
4. **Diagnosis:** Design a plausible scenario in which the original result is misleading because of: Refrigerant-specific safety classifications and environmental rules evolve; GWP alone does not select a compliant product. Specify an independent observation to test the explanation.
5. **Experiment:** Convert the suggested verification into a small data-collection plan: Maintain verified refrigerant inventory, leak and recovery records and electricity data.
6. **Decision:** Defend a recommendation using the lesson's trade-off: Include both direct leakage and indirect operating energy when comparing system options. Identify one operating condition that might reverse your conclusion.

**Checking rubric:** Give credit for a correct model boundary and quantities, transparent unit conversion, dimensional reasonableness, explicit limitations and a falsifiable verification strategy. Do not award full credit for copying a plausible-looking number without explaining what it measures. For an open-ended design response, alternative answers may be valid when their constraints and evidence are coherent.


---

## U08-L05 — Lifecycle cost and project decision-making

**Outcome:** Interpret lifecycle cost and project decision-making, perform a traceable estimate, diagnose a limitation, and explain how evidence could change the associated engineering decision.

### 1. Engineering problem and purpose

A project team hands over a new HVAC installation. Design intent, instrument readings, operator training, refrigerant management and maintenance plans determine whether the modeled benefits occur. The specific issue here is **lifecycle cost and project decision-making**. Evaluate alternatives through reproducible design decisions, commissioning evidence, fault diagnosis, and lifecycle accounting. This problem matters because a mechanical design must perform across several operating states rather than just one conveniently chosen measurement. A useful first result is a quantity with clear units, an identified system boundary and a stated purpose; it is not a prediction for arbitrary buildings or products.

### 2. Governing idea and modeling assumptions

**Working relation:** `NPV = C0 + sum_t C_t/(1+r)^t for cost-positive convention`.

This equation should be interpreted together with its reference states. Write down every independent variable, with its numerical units, and keep any temperature-difference term separate from an absolute thermodynamic temperature. For a steady-flow energy equation, indicate the mass-flow definition; for a moist-air relation, specify whether the denominator is dry-air mass; for a performance ratio, ensure numerator and denominator cover the same test period. If the result is dimensionless, explain what physical quantities were compared.

Simple payback omits discounting, maintenance and operating risk, and a low price is not a safety rationale. This is a reason to retain the equation's scope in every answer. A classroom relation may assume ideal-gas behavior, constant specific heat, steady mass balance, uniform mixing, negligible leakage, or a fixed equipment efficiency. Real systems can violate several of these assumptions simultaneously, particularly during a changing load. The correct response is to identify the assumption and collect appropriate evidence, rather than silently adding correction factors whose source is unclear.

### 3. Fully specified numerical teaching example

**Assumed inputs and computed answer:** An upgrade costing $4,000 and saving $900/year for five years at zero discount gives simple net savings $500, excluding maintenance and replacement.

Reproduce the result using the equation rather than copying the displayed answer. Convert all values to compatible units before substitution. Distinguish kW from kWh, kPa from Pa, and a percentage from a dimensionless fraction. Then perform three small checks: does the output have the expected dimensions, is its sign physically meaningful for the chosen reference direction, and does it approach a sensible limiting value when the driving difference or mass flow tends toward zero? If a limiting case gives a contradiction, examine the equation and model boundary before trusting the decimals.

### 4. Physical interpretation and failure analysis

The immediate diagnostic trap in this lesson is the following: Simple payback omits discounting, maintenance and operating risk, and a low price is not a safety rationale. Construct a counterexample where the displayed calculation remains arithmetically correct but no longer explains the actual operating behavior. Identify which state variable or energy stream has been excluded, whether the error would tend to make the prediction high or low, and which observation could reveal the discrepancy. Where the sign of the discrepancy depends on coupled effects, give both plausible directions instead of selecting one without evidence.

### 5. Measurement and independent verification

**Suggested evidence:** Develop matched-service operating scenarios and test energy-price and load sensitivity. Define instrument location, calibration state, sample rate, expected operating condition and averaging period. Record the physical configuration, controller state, weather or ambient condition and any recent service changes. Establish a repeated baseline where practical; a one-off value can be distorted by transient heat storage or instrument delay. Preserve raw observations separately from processed plots so a different analyst can independently reproduce the result.

For uncertainty, start with a bounded input sensitivity calculation. Identify the most influential parameter and estimate how its uncertainty propagates through the working relation. If the input depends on other measured quantities, note their correlation instead of automatically treating errors as independent. Keep the measurement units and calibration references attached to each row in the results table. A plotted model curve is not experimental data; if both are presented, label them differently and show measurement points with their uncertainty where available.

### 6. Design choice and engineering trade-offs

**Decision problem:** Approve only after comfort, compliance, reliability and budget constraints have been separately satisfied. Translate this into a decision matrix with at least one primary performance measure and one hard constraint. State whether the option is being evaluated for capacity, comfort, electricity consumption, reliability, lifecycle cost or emissions. Some options improve one objective while increasing fan power, refrigerant charge, maintenance burden or control complexity. Do not call the option superior without declaring the weighted objective or the nonnegotiable constraint.

### 7. Practice and assessment

1. **Concept:** Explain the physical meaning of `NPV = C0 + sum_t C_t/(1+r)^t for cost-positive convention` and identify at least two assumptions necessary for its use.
2. **Numerical:** Repeat the example with all units shown: An upgrade costing $4,000 and saving $900/year for five years at zero discount gives simple net savings $500, excluding maintenance and replacement. State an answer at a precision justified by the input values.
4. **Diagnosis:** Design a plausible scenario in which the original result is misleading because of: Simple payback omits discounting, maintenance and operating risk, and a low price is not a safety rationale. Specify an independent observation to test the explanation.
5. **Experiment:** Convert the suggested verification into a small data-collection plan: Develop matched-service operating scenarios and test energy-price and load sensitivity.
6. **Decision:** Defend a recommendation using the lesson's trade-off: Approve only after comfort, compliance, reliability and budget constraints have been separately satisfied. Identify one operating condition that might reverse your conclusion.

**Checking rubric:** Give credit for a correct model boundary and quantities, transparent unit conversion, dimensional reasonableness, explicit limitations and a falsifiable verification strategy. Do not award full credit for copying a plausible-looking number without explaining what it measures. For an open-ended design response, alternative answers may be valid when their constraints and evidence are coherent.


---

