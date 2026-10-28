# Unit 7: Gas Power, Vapor Power, and Combined Thermodynamic Cycles

# Unit 7, Lesson 1 — Otto cycle and compression ratio

**Learning goals.** Explain the physical meaning of the stated relationship; use the example to reconstruct a verifiable answer; identify at least two model limitations; and propose an independent check.

## 1. Physical question and conceptual model

The cold-air-standard Otto cycle consists of isentropic compression, constant-volume heat addition, isentropic expansion and constant-volume heat rejection. Under constant k=c_p/c_v, its thermal efficiency is 1−1/r^(k−1). It rises with compression ratio but real engines face knock, emissions, heat transfer and pumping losses.


**Professional use.** Investigate how variable cp and allowable peak pressure constrain realistic operation. Avoid jumping from a property value to a performance guarantee: the former describes an assumed state, and the latter depends on losses, materials, reliability and operating limits.

## 2. Build the mathematical relationship

**Governing statement:** `η_Otto=1−1/r^(k−1)`.


**Model qualification.** The equation is meaningful only when its state and process assumptions are satisfied. Some equations are conservation balances that remain exact for their declared boundary; others are constitutive approximations, such as an ideal-gas relation, a constant heat capacity or an isentropic reference process. Determine which category this statement belongs to. Explain whether extra phenomena such as a moving boundary, leakage, heat loss, multiphase conditions, kinetic energy, electrical work or chemical reaction would add terms or require a different property source. If the process is transient, ask whether an accumulation term is missing.

## 3. Worked teaching example

For r=8 and k=1.4, ideal Otto efficiency ≈56.5%.


**Interpretive check.** Does the result increase or decrease when the principal driving condition becomes stronger? Does the prediction approach a sensible limit when the temperature difference, flow rate, state change or relevant force approaches zero? Such limiting tests are not substitutes for a measurement, but they are effective at rejecting a broken model before the expensive stage of building apparatus or selecting equipment.

## 4. Failure analysis and engineering judgement

**A tempting but incorrect shortcut:** Substituting this ideal thermal efficiency as the measured fuel-to-shaft efficiency of a road engine.

Investigate what this shortcut assumes about the device or material. Predict whether it would overstate useful work, misstate the phase, hide a heat leak or suppress a needed transport term. Estimate the direction of the bias before estimating its size. A numerical calculation that conserves energy can still violate the second law; similarly, a temperature prediction can be inconsistent with phase equilibrium. Test both conservation and state feasibility. Where the model is an ideal upper or lower bound, identify which side of the bound a real machine should occupy under comparable conditions.

**Engineering context.** Investigate how variable cp and allowable peak pressure constrain realistic operation. A useful report would specify the relevant operating range, which properties are tabulated or calculated, and which assumptions are supported by evidence. It would not claim that an attractive textbook efficiency, coefficient of performance or output power proves achievable production performance.

## 5. Verification and measurement protocol

Design a simple check of **otto cycle and compression ratio**. Specify a control volume or control mass, boundary conditions, primary observations and sampling interval. Report whether the observation is direct (temperature, mass, voltage, volumetric flow), indirectly inferred (enthalpy, dryness fraction, exergy), or fitted from an empirical relation. Distinguish repeatability from model validity: a repeatable sensor can be wrongly calibrated, and a perfectly reproducible computer program can implement the wrong equation. Identify one test in which the idealization should perform reasonably, and a second test where a named assumption may break down. If you use fluid property tables or software, record its provenance, units, reference state and interpolation method.


## 6. Questions and answer criteria

**Exercise A — Reconstruct.** Reproduce the stated worked example with symbols, units and at least one limiting check. *Answer criterion:* obtain the stated value within rounding and explain each term in `η_Otto=1−1/r^(k−1)`.

**Exercise B — Predict.** Select one physically independent input, change it by 10%, and predict the response before calculation. *Answer criterion:* state whether a linear, reciprocal, logarithmic or state-dependent relationship is being used, and explain why it is valid over the selected interval.

**Exercise C — Diagnose.** Evaluate this proposed shortcut: "Substituting this ideal thermal efficiency as the measured fuel-to-shaft efficiency of a road engine." *Answer criterion:* identify the missing assumption, specify a condition where the shortcut fails, and propose one measurement or alternate model that would expose the error.

## 7. Extended case and reproducible handover

Return to the **refrigeration system** case that motivates this unit. The engineering requirement is cooling delivery at a specified temperature lift and ambient condition. Use this lesson's principle to create a two-column comparison between a minimal classroom calculation and a safer engineering estimate. The classroom side should contain only quantities supported by the basic model; the engineering side should add refrigerant safety, compressor cycling, ice and off-design pressure drop. For each added quantity, say whether it is known, must be measured, can be estimated from trustworthy property data, or is impossible to infer from the current information. Where a value is unknown, retain a symbol or range instead of fabricating a precise number.


## 8. Closing self-test

Without viewing your notes, explain why the same physical device can be modeled with different boundaries, which quantities change accordingly and which conservation principles remain unchanged. Explain the relationship in your own words before quoting its symbols. If you cannot distinguish a property from a path function, or theoretical limit from verified behavior, revisit the model formulation rather than memorizing the numerical answer.


---

# Unit 7, Lesson 2 — Diesel and dual-cycle representations

**Learning goals.** Explain the physical meaning of the stated relationship; use the example to reconstruct a verifiable answer; identify at least two model limitations; and propose an independent check.

## 1. Physical question and conceptual model

The ideal Diesel cycle models heat addition at constant pressure, leading to a cutoff ratio that influences ideal efficiency. A dual cycle divides idealized heat addition between constant-volume and constant-pressure steps. Real engines display finite-duration combustion and heat transfer rather than perfectly prescribed ideal paths.


**Professional use.** Compare cycles using the same maximum pressure or compression ratio, and state which comparison is being made. Avoid jumping from a property value to a performance guarantee: the former describes an assumed state, and the latter depends on losses, materials, reliability and operating limits.

## 2. Build the mathematical relationship

**Governing statement:** `η_Diesel=1−[1/r^(k−1)]×[(r_c^k−1)/(k(r_c−1))]`.


**Model qualification.** The equation is meaningful only when its state and process assumptions are satisfied. Some equations are conservation balances that remain exact for their declared boundary; others are constitutive approximations, such as an ideal-gas relation, a constant heat capacity or an isentropic reference process. Determine which category this statement belongs to. Explain whether extra phenomena such as a moving boundary, leakage, heat loss, multiphase conditions, kinetic energy, electrical work or chemical reaction would add terms or require a different property source. If the process is transient, ask whether an accumulation term is missing.

## 3. Worked teaching example

With r=16, cutoff ratio r_c=2 and k=1.4, ideal Diesel efficiency is about 61.4%.


**Interpretive check.** Does the result increase or decrease when the principal driving condition becomes stronger? Does the prediction approach a sensible limit when the temperature difference, flow rate, state change or relevant force approaches zero? Such limiting tests are not substitutes for a measurement, but they are effective at rejecting a broken model before the expensive stage of building apparatus or selecting equipment.

## 4. Failure analysis and engineering judgement

**A tempting but incorrect shortcut:** Interpreting the word Diesel as a statement about real fuel chemistry in an air-standard calculation.

Investigate what this shortcut assumes about the device or material. Predict whether it would overstate useful work, misstate the phase, hide a heat leak or suppress a needed transport term. Estimate the direction of the bias before estimating its size. A numerical calculation that conserves energy can still violate the second law; similarly, a temperature prediction can be inconsistent with phase equilibrium. Test both conservation and state feasibility. Where the model is an ideal upper or lower bound, identify which side of the bound a real machine should occupy under comparable conditions.

**Engineering context.** Compare cycles using the same maximum pressure or compression ratio, and state which comparison is being made. A useful report would specify the relevant operating range, which properties are tabulated or calculated, and which assumptions are supported by evidence. It would not claim that an attractive textbook efficiency, coefficient of performance or output power proves achievable production performance.

## 5. Verification and measurement protocol

Design a simple check of **diesel and dual-cycle representations**. Specify a control volume or control mass, boundary conditions, primary observations and sampling interval. Report whether the observation is direct (temperature, mass, voltage, volumetric flow), indirectly inferred (enthalpy, dryness fraction, exergy), or fitted from an empirical relation. Distinguish repeatability from model validity: a repeatable sensor can be wrongly calibrated, and a perfectly reproducible computer program can implement the wrong equation. Identify one test in which the idealization should perform reasonably, and a second test where a named assumption may break down. If you use fluid property tables or software, record its provenance, units, reference state and interpolation method.


## 6. Questions and answer criteria

**Exercise A — Reconstruct.** Reproduce the stated worked example with symbols, units and at least one limiting check. *Answer criterion:* obtain the stated value within rounding and explain each term in `η_Diesel=1−[1/r^(k−1)]×[(r_c^k−1)/(k(r_c−1))]`.

**Exercise B — Predict.** Select one physically independent input, change it by 10%, and predict the response before calculation. *Answer criterion:* state whether a linear, reciprocal, logarithmic or state-dependent relationship is being used, and explain why it is valid over the selected interval.

**Exercise C — Diagnose.** Evaluate this proposed shortcut: "Interpreting the word Diesel as a statement about real fuel chemistry in an air-standard calculation." *Answer criterion:* identify the missing assumption, specify a condition where the shortcut fails, and propose one measurement or alternate model that would expose the error.

## 7. Extended case and reproducible handover

Return to the **refrigeration system** case that motivates this unit. The engineering requirement is cooling delivery at a specified temperature lift and ambient condition. Use this lesson's principle to create a two-column comparison between a minimal classroom calculation and a safer engineering estimate. The classroom side should contain only quantities supported by the basic model; the engineering side should add refrigerant safety, compressor cycling, ice and off-design pressure drop. For each added quantity, say whether it is known, must be measured, can be estimated from trustworthy property data, or is impossible to infer from the current information. Where a value is unknown, retain a symbol or range instead of fabricating a precise number.


## 8. Closing self-test

Without viewing your notes, explain why the same physical device can be modeled with different boundaries, which quantities change accordingly and which conservation principles remain unchanged. Explain the relationship in your own words before quoting its symbols. If you cannot distinguish a property from a path function, or theoretical limit from verified behavior, revisit the model formulation rather than memorizing the numerical answer.


---

# Unit 7, Lesson 3 — Brayton gas-turbine cycle

**Learning goals.** Explain the physical meaning of the stated relationship; use the example to reconstruct a verifiable answer; identify at least two model limitations; and propose an independent check.

## 1. Physical question and conceptual model

The simple ideal Brayton cycle uses isentropic compression and expansion with constant-pressure heat addition and rejection. For a cold-air-standard idealization η≈1−1/r_p^((k−1)/k), where r_p is compressor pressure ratio. Actual turbine inlet temperature, compressor efficiency and cooling flows strongly affect net output.


**Professional use.** Sketch compressor and turbine contributions separately, then evaluate net shaft power. Avoid jumping from a property value to a performance guarantee: the former describes an assumed state, and the latter depends on losses, materials, reliability and operating limits.

## 2. Build the mathematical relationship

**Governing statement:** `η_Brayton=1−r_p^(-(k−1)/k)`.


**Model qualification.** The equation is meaningful only when its state and process assumptions are satisfied. Some equations are conservation balances that remain exact for their declared boundary; others are constitutive approximations, such as an ideal-gas relation, a constant heat capacity or an isentropic reference process. Determine which category this statement belongs to. Explain whether extra phenomena such as a moving boundary, leakage, heat loss, multiphase conditions, kinetic energy, electrical work or chemical reaction would add terms or require a different property source. If the process is transient, ask whether an accumulation term is missing.

## 3. Worked teaching example

For r_p=8 and k=1.4, the ideal efficiency is about 44.8%.


**Interpretive check.** Does the result increase or decrease when the principal driving condition becomes stronger? Does the prediction approach a sensible limit when the temperature difference, flow rate, state change or relevant force approaches zero? Such limiting tests are not substitutes for a measurement, but they are effective at rejecting a broken model before the expensive stage of building apparatus or selecting equipment.

## 4. Failure analysis and engineering judgement

**A tempting but incorrect shortcut:** Assuming pressure ratio can grow indefinitely while retaining positive specific net work.

Investigate what this shortcut assumes about the device or material. Predict whether it would overstate useful work, misstate the phase, hide a heat leak or suppress a needed transport term. Estimate the direction of the bias before estimating its size. A numerical calculation that conserves energy can still violate the second law; similarly, a temperature prediction can be inconsistent with phase equilibrium. Test both conservation and state feasibility. Where the model is an ideal upper or lower bound, identify which side of the bound a real machine should occupy under comparable conditions.

**Engineering context.** Sketch compressor and turbine contributions separately, then evaluate net shaft power. A useful report would specify the relevant operating range, which properties are tabulated or calculated, and which assumptions are supported by evidence. It would not claim that an attractive textbook efficiency, coefficient of performance or output power proves achievable production performance.

## 5. Verification and measurement protocol

Design a simple check of **brayton gas-turbine cycle**. Specify a control volume or control mass, boundary conditions, primary observations and sampling interval. Report whether the observation is direct (temperature, mass, voltage, volumetric flow), indirectly inferred (enthalpy, dryness fraction, exergy), or fitted from an empirical relation. Distinguish repeatability from model validity: a repeatable sensor can be wrongly calibrated, and a perfectly reproducible computer program can implement the wrong equation. Identify one test in which the idealization should perform reasonably, and a second test where a named assumption may break down. If you use fluid property tables or software, record its provenance, units, reference state and interpolation method.


## 6. Questions and answer criteria

**Exercise A — Reconstruct.** Reproduce the stated worked example with symbols, units and at least one limiting check. *Answer criterion:* obtain the stated value within rounding and explain each term in `η_Brayton=1−r_p^(-(k−1)/k)`.

**Exercise B — Predict.** Select one physically independent input, change it by 10%, and predict the response before calculation. *Answer criterion:* state whether a linear, reciprocal, logarithmic or state-dependent relationship is being used, and explain why it is valid over the selected interval.

**Exercise C — Diagnose.** Evaluate this proposed shortcut: "Assuming pressure ratio can grow indefinitely while retaining positive specific net work." *Answer criterion:* identify the missing assumption, specify a condition where the shortcut fails, and propose one measurement or alternate model that would expose the error.

## 7. Extended case and reproducible handover

Return to the **refrigeration system** case that motivates this unit. The engineering requirement is cooling delivery at a specified temperature lift and ambient condition. Use this lesson's principle to create a two-column comparison between a minimal classroom calculation and a safer engineering estimate. The classroom side should contain only quantities supported by the basic model; the engineering side should add refrigerant safety, compressor cycling, ice and off-design pressure drop. For each added quantity, say whether it is known, must be measured, can be estimated from trustworthy property data, or is impossible to infer from the current information. Where a value is unknown, retain a symbol or range instead of fabricating a precise number.


## 8. Closing self-test

Without viewing your notes, explain why the same physical device can be modeled with different boundaries, which quantities change accordingly and which conservation principles remain unchanged. Explain the relationship in your own words before quoting its symbols. If you cannot distinguish a property from a path function, or theoretical limit from verified behavior, revisit the model formulation rather than memorizing the numerical answer.


---

# Unit 7, Lesson 4 — Rankine vapor-power cycle

**Learning goals.** Explain the physical meaning of the stated relationship; use the example to reconstruct a verifiable answer; identify at least two model limitations; and propose an independent check.

## 1. Physical question and conceptual model

A basic Rankine cycle pumps condensed liquid to high pressure, adds heat to generate steam, expands steam in a turbine, and condenses the exhaust. Pump work is often much smaller than turbine work per kilogram, but not literally zero. Pressure loss, wet steam and condenser cooling impose practical limits.


**Professional use.** Use a T–s diagram to reason about reheating and regeneration without pretending these remove all losses. Avoid jumping from a property value to a performance guarantee: the former describes an assumed state, and the latter depends on losses, materials, reliability and operating limits.

## 2. Build the mathematical relationship

**Governing statement:** `η_th=(w_t−w_p)/q_in`.


**Model qualification.** The equation is meaningful only when its state and process assumptions are satisfied. Some equations are conservation balances that remain exact for their declared boundary; others are constitutive approximations, such as an ideal-gas relation, a constant heat capacity or an isentropic reference process. Determine which category this statement belongs to. Explain whether extra phenomena such as a moving boundary, leakage, heat loss, multiphase conditions, kinetic energy, electrical work or chemical reaction would add terms or require a different property source. If the process is transient, ask whether an accumulation term is missing.

## 3. Worked teaching example

If turbine work=900 kJ/kg, pump work=10 kJ/kg and boiler heat input=2500 kJ/kg, efficiency is 35.6%.


**Interpretive check.** Does the result increase or decrease when the principal driving condition becomes stronger? Does the prediction approach a sensible limit when the temperature difference, flow rate, state change or relevant force approaches zero? Such limiting tests are not substitutes for a measurement, but they are effective at rejecting a broken model before the expensive stage of building apparatus or selecting equipment.

## 4. Failure analysis and engineering judgement

**A tempting but incorrect shortcut:** Neglecting feedwater pump work and assuming the turbine exit cannot contain moisture.

Investigate what this shortcut assumes about the device or material. Predict whether it would overstate useful work, misstate the phase, hide a heat leak or suppress a needed transport term. Estimate the direction of the bias before estimating its size. A numerical calculation that conserves energy can still violate the second law; similarly, a temperature prediction can be inconsistent with phase equilibrium. Test both conservation and state feasibility. Where the model is an ideal upper or lower bound, identify which side of the bound a real machine should occupy under comparable conditions.

**Engineering context.** Use a T–s diagram to reason about reheating and regeneration without pretending these remove all losses. A useful report would specify the relevant operating range, which properties are tabulated or calculated, and which assumptions are supported by evidence. It would not claim that an attractive textbook efficiency, coefficient of performance or output power proves achievable production performance.

## 5. Verification and measurement protocol

Design a simple check of **rankine vapor-power cycle**. Specify a control volume or control mass, boundary conditions, primary observations and sampling interval. Report whether the observation is direct (temperature, mass, voltage, volumetric flow), indirectly inferred (enthalpy, dryness fraction, exergy), or fitted from an empirical relation. Distinguish repeatability from model validity: a repeatable sensor can be wrongly calibrated, and a perfectly reproducible computer program can implement the wrong equation. Identify one test in which the idealization should perform reasonably, and a second test where a named assumption may break down. If you use fluid property tables or software, record its provenance, units, reference state and interpolation method.


## 6. Questions and answer criteria

**Exercise A — Reconstruct.** Reproduce the stated worked example with symbols, units and at least one limiting check. *Answer criterion:* obtain the stated value within rounding and explain each term in `η_th=(w_t−w_p)/q_in`.

**Exercise B — Predict.** Select one physically independent input, change it by 10%, and predict the response before calculation. *Answer criterion:* state whether a linear, reciprocal, logarithmic or state-dependent relationship is being used, and explain why it is valid over the selected interval.

**Exercise C — Diagnose.** Evaluate this proposed shortcut: "Neglecting feedwater pump work and assuming the turbine exit cannot contain moisture." *Answer criterion:* identify the missing assumption, specify a condition where the shortcut fails, and propose one measurement or alternate model that would expose the error.

## 7. Extended case and reproducible handover

Return to the **refrigeration system** case that motivates this unit. The engineering requirement is cooling delivery at a specified temperature lift and ambient condition. Use this lesson's principle to create a two-column comparison between a minimal classroom calculation and a safer engineering estimate. The classroom side should contain only quantities supported by the basic model; the engineering side should add refrigerant safety, compressor cycling, ice and off-design pressure drop. For each added quantity, say whether it is known, must be measured, can be estimated from trustworthy property data, or is impossible to infer from the current information. Where a value is unknown, retain a symbol or range instead of fabricating a precise number.


## 8. Closing self-test

Without viewing your notes, explain why the same physical device can be modeled with different boundaries, which quantities change accordingly and which conservation principles remain unchanged. Explain the relationship in your own words before quoting its symbols. If you cannot distinguish a property from a path function, or theoretical limit from verified behavior, revisit the model formulation rather than memorizing the numerical answer.


---

# Unit 7, Lesson 5 — Vapor-compression refrigeration and heat pumps

**Learning goals.** Explain the physical meaning of the stated relationship; use the example to reconstruct a verifiable answer; identify at least two model limitations; and propose an independent check.

## 1. Physical question and conceptual model

A simple vapor-compression cycle includes an evaporator, compressor, condenser and throttling device. Refrigerant evaporates while absorbing heat, is compressed, rejects heat while condensing, then expands approximately isoenthalpically. Compressor power and evaporator cooling duty define COP_R; refrigerant state tables are needed for credible equipment selection.


**Professional use.** Identify superheat, subcooling, ice formation, leakage and refrigerant safety constraints. Avoid jumping from a property value to a performance guarantee: the former describes an assumed state, and the latter depends on losses, materials, reliability and operating limits.

## 2. Build the mathematical relationship

**Governing statement:** `COP_R=(h1−h4)/(h2−h1)`.


**Model qualification.** The equation is meaningful only when its state and process assumptions are satisfied. Some equations are conservation balances that remain exact for their declared boundary; others are constitutive approximations, such as an ideal-gas relation, a constant heat capacity or an isentropic reference process. Determine which category this statement belongs to. Explain whether extra phenomena such as a moving boundary, leakage, heat loss, multiphase conditions, kinetic energy, electrical work or chemical reaction would add terms or require a different property source. If the process is transient, ask whether an accumulation term is missing.

## 3. Worked teaching example

If evaporator specific cooling is 160 kJ/kg and compressor input is 40 kJ/kg, COP_R=4.


**Interpretive check.** Does the result increase or decrease when the principal driving condition becomes stronger? Does the prediction approach a sensible limit when the temperature difference, flow rate, state change or relevant force approaches zero? Such limiting tests are not substitutes for a measurement, but they are effective at rejecting a broken model before the expensive stage of building apparatus or selecting equipment.

## 4. Failure analysis and engineering judgement

**A tempting but incorrect shortcut:** Using a fixed refrigerant COP independent of ambient temperature or operating pressures.

Investigate what this shortcut assumes about the device or material. Predict whether it would overstate useful work, misstate the phase, hide a heat leak or suppress a needed transport term. Estimate the direction of the bias before estimating its size. A numerical calculation that conserves energy can still violate the second law; similarly, a temperature prediction can be inconsistent with phase equilibrium. Test both conservation and state feasibility. Where the model is an ideal upper or lower bound, identify which side of the bound a real machine should occupy under comparable conditions.

**Engineering context.** Identify superheat, subcooling, ice formation, leakage and refrigerant safety constraints. A useful report would specify the relevant operating range, which properties are tabulated or calculated, and which assumptions are supported by evidence. It would not claim that an attractive textbook efficiency, coefficient of performance or output power proves achievable production performance.

## 5. Verification and measurement protocol

Design a simple check of **vapor-compression refrigeration and heat pumps**. Specify a control volume or control mass, boundary conditions, primary observations and sampling interval. Report whether the observation is direct (temperature, mass, voltage, volumetric flow), indirectly inferred (enthalpy, dryness fraction, exergy), or fitted from an empirical relation. Distinguish repeatability from model validity: a repeatable sensor can be wrongly calibrated, and a perfectly reproducible computer program can implement the wrong equation. Identify one test in which the idealization should perform reasonably, and a second test where a named assumption may break down. If you use fluid property tables or software, record its provenance, units, reference state and interpolation method.


## 6. Questions and answer criteria

**Exercise A — Reconstruct.** Reproduce the stated worked example with symbols, units and at least one limiting check. *Answer criterion:* obtain the stated value within rounding and explain each term in `COP_R=(h1−h4)/(h2−h1)`.

**Exercise B — Predict.** Select one physically independent input, change it by 10%, and predict the response before calculation. *Answer criterion:* state whether a linear, reciprocal, logarithmic or state-dependent relationship is being used, and explain why it is valid over the selected interval.

**Exercise C — Diagnose.** Evaluate this proposed shortcut: "Using a fixed refrigerant COP independent of ambient temperature or operating pressures." *Answer criterion:* identify the missing assumption, specify a condition where the shortcut fails, and propose one measurement or alternate model that would expose the error.

## 7. Extended case and reproducible handover

Return to the **refrigeration system** case that motivates this unit. The engineering requirement is cooling delivery at a specified temperature lift and ambient condition. Use this lesson's principle to create a two-column comparison between a minimal classroom calculation and a safer engineering estimate. The classroom side should contain only quantities supported by the basic model; the engineering side should add refrigerant safety, compressor cycling, ice and off-design pressure drop. For each added quantity, say whether it is known, must be measured, can be estimated from trustworthy property data, or is impossible to infer from the current information. Where a value is unknown, retain a symbol or range instead of fabricating a precise number.


## 8. Closing self-test

Without viewing your notes, explain why the same physical device can be modeled with different boundaries, which quantities change accordingly and which conservation principles remain unchanged. Explain the relationship in your own words before quoting its symbols. If you cannot distinguish a property from a path function, or theoretical limit from verified behavior, revisit the model formulation rather than memorizing the numerical answer.


---

