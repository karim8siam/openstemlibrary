# Unit 4: Control Volume Mass and Energy Analysis

# Unit 4, Lesson 1 — Control volume boundaries and continuity

**Learning goals.** Explain the physical meaning of the stated relationship; use the example to reconstruct a verifiable answer; identify at least two model limitations; and propose an independent check.

## 1. Physical question and conceptual model

A control volume is a region in space chosen for an engineering analysis; its boundary can coincide with the casing or cross a fluid pipe. The steady-flow approximation means total stored mass is constant, not that all local velocities are zero. At each inlet or outlet, use consistent signs and average mass-flow quantities when appropriate.


**Professional use.** Measure inlet and exit flows separately and assess leaks, condensate and unsteady accumulation. Avoid jumping from a property value to a performance guarantee: the former describes an assumed state, and the latter depends on losses, materials, reliability and operating limits.

## 2. Build the mathematical relationship

**Governing statement:** `d m_CV/dt=Σṁ_in−Σṁ_out`.


**Model qualification.** The equation is meaningful only when its state and process assumptions are satisfied. Some equations are conservation balances that remain exact for their declared boundary; others are constitutive approximations, such as an ideal-gas relation, a constant heat capacity or an isentropic reference process. Determine which category this statement belongs to. Explain whether extra phenomena such as a moving boundary, leakage, heat loss, multiphase conditions, kinetic energy, electrical work or chemical reaction would add terms or require a different property source. If the process is transient, ask whether an accumulation term is missing.

## 3. Worked teaching example

A tank receives 2.5 kg/s and discharges 1.9 kg/s; its mass accumulation rate is 0.6 kg/s.


**Interpretive check.** Does the result increase or decrease when the principal driving condition becomes stronger? Does the prediction approach a sensible limit when the temperature difference, flow rate, state change or relevant force approaches zero? Such limiting tests are not substitutes for a measurement, but they are effective at rejecting a broken model before the expensive stage of building apparatus or selecting equipment.

## 4. Failure analysis and engineering judgement

**A tempting but incorrect shortcut:** Assuming a transient filling tank has equal inflow and outflow just because valves are present.

Investigate what this shortcut assumes about the device or material. Predict whether it would overstate useful work, misstate the phase, hide a heat leak or suppress a needed transport term. Estimate the direction of the bias before estimating its size. A numerical calculation that conserves energy can still violate the second law; similarly, a temperature prediction can be inconsistent with phase equilibrium. Test both conservation and state feasibility. Where the model is an ideal upper or lower bound, identify which side of the bound a real machine should occupy under comparable conditions.

**Engineering context.** Measure inlet and exit flows separately and assess leaks, condensate and unsteady accumulation. A useful report would specify the relevant operating range, which properties are tabulated or calculated, and which assumptions are supported by evidence. It would not claim that an attractive textbook efficiency, coefficient of performance or output power proves achievable production performance.

## 5. Verification and measurement protocol

Design a simple check of **control volume boundaries and continuity**. Specify a control volume or control mass, boundary conditions, primary observations and sampling interval. Report whether the observation is direct (temperature, mass, voltage, volumetric flow), indirectly inferred (enthalpy, dryness fraction, exergy), or fitted from an empirical relation. Distinguish repeatability from model validity: a repeatable sensor can be wrongly calibrated, and a perfectly reproducible computer program can implement the wrong equation. Identify one test in which the idealization should perform reasonably, and a second test where a named assumption may break down. If you use fluid property tables or software, record its provenance, units, reference state and interpolation method.


## 6. Questions and answer criteria

**Exercise A — Reconstruct.** Reproduce the stated worked example with symbols, units and at least one limiting check. *Answer criterion:* obtain the stated value within rounding and explain each term in `d m_CV/dt=Σṁ_in−Σṁ_out`.

**Exercise B — Predict.** Select one physically independent input, change it by 10%, and predict the response before calculation. *Answer criterion:* state whether a linear, reciprocal, logarithmic or state-dependent relationship is being used, and explain why it is valid over the selected interval.

**Exercise C — Diagnose.** Evaluate this proposed shortcut: "Assuming a transient filling tank has equal inflow and outflow just because valves are present." *Answer criterion:* identify the missing assumption, specify a condition where the shortcut fails, and propose one measurement or alternate model that would expose the error.

## 7. Extended case and reproducible handover

Return to the **air-compressor test stand** case that motivates this unit. The objective is to reconcile measured electricity, shaft output and outlet enthalpy. Use this lesson's principle to create a two-column comparison between a minimal classroom calculation and a safer engineering estimate. The classroom side should contain only quantities supported by the basic model; the engineering side should add motor losses, leakage, pulsation, pressure taps and inlet humidity. For each added quantity, say whether it is known, must be measured, can be estimated from trustworthy property data, or is impossible to infer from the current information. Where a value is unknown, retain a symbol or range instead of fabricating a precise number.


## 8. Closing self-test

Without viewing your notes, explain why the same physical device can be modeled with different boundaries, which quantities change accordingly and which conservation principles remain unchanged. Explain the relationship in your own words before quoting its symbols. If you cannot distinguish a property from a path function, or theoretical limit from verified behavior, revisit the model formulation rather than memorizing the numerical answer.


---

# Unit 4, Lesson 2 — Flow work and specific enthalpy

**Learning goals.** Explain the physical meaning of the stated relationship; use the example to reconstruct a verifiable answer; identify at least two model limitations; and propose an independent check.

## 1. Physical question and conceptual model

Mass crossing a pressure boundary carries flow work pv, which combines with internal energy u to form enthalpy h=u+pv. This is a bookkeeping simplification in the flow energy equation rather than an extra independent source of energy. Reference enthalpies may be negative depending on convention; only correctly referenced differences matter.


**Professional use.** Trace where upstream compressor work and downstream pressure drops appear in the accounting. Avoid jumping from a property value to a performance guarantee: the former describes an assumed state, and the latter depends on losses, materials, reliability and operating limits.

## 2. Build the mathematical relationship

**Governing statement:** `h=u+pv`.


**Model qualification.** The equation is meaningful only when its state and process assumptions are satisfied. Some equations are conservation balances that remain exact for their declared boundary; others are constitutive approximations, such as an ideal-gas relation, a constant heat capacity or an isentropic reference process. Determine which category this statement belongs to. Explain whether extra phenomena such as a moving boundary, leakage, heat loss, multiphase conditions, kinetic energy, electrical work or chemical reaction would add terms or require a different property source. If the process is transient, ask whether an accumulation term is missing.

## 3. Worked teaching example

At u=2250 kJ/kg, p=200 kPa and v=0.50 m³/kg, the specific enthalpy is 2350 kJ/kg.


**Interpretive check.** Does the result increase or decrease when the principal driving condition becomes stronger? Does the prediction approach a sensible limit when the temperature difference, flow rate, state change or relevant force approaches zero? Such limiting tests are not substitutes for a measurement, but they are effective at rejecting a broken model before the expensive stage of building apparatus or selecting equipment.

## 4. Failure analysis and engineering judgement

**A tempting but incorrect shortcut:** Adding a separate pv flow-work term after already using h in a steady-flow balance.

Investigate what this shortcut assumes about the device or material. Predict whether it would overstate useful work, misstate the phase, hide a heat leak or suppress a needed transport term. Estimate the direction of the bias before estimating its size. A numerical calculation that conserves energy can still violate the second law; similarly, a temperature prediction can be inconsistent with phase equilibrium. Test both conservation and state feasibility. Where the model is an ideal upper or lower bound, identify which side of the bound a real machine should occupy under comparable conditions.

**Engineering context.** Trace where upstream compressor work and downstream pressure drops appear in the accounting. A useful report would specify the relevant operating range, which properties are tabulated or calculated, and which assumptions are supported by evidence. It would not claim that an attractive textbook efficiency, coefficient of performance or output power proves achievable production performance.

## 5. Verification and measurement protocol

Design a simple check of **flow work and specific enthalpy**. Specify a control volume or control mass, boundary conditions, primary observations and sampling interval. Report whether the observation is direct (temperature, mass, voltage, volumetric flow), indirectly inferred (enthalpy, dryness fraction, exergy), or fitted from an empirical relation. Distinguish repeatability from model validity: a repeatable sensor can be wrongly calibrated, and a perfectly reproducible computer program can implement the wrong equation. Identify one test in which the idealization should perform reasonably, and a second test where a named assumption may break down. If you use fluid property tables or software, record its provenance, units, reference state and interpolation method.


## 6. Questions and answer criteria

**Exercise A — Reconstruct.** Reproduce the stated worked example with symbols, units and at least one limiting check. *Answer criterion:* obtain the stated value within rounding and explain each term in `h=u+pv`.

**Exercise B — Predict.** Select one physically independent input, change it by 10%, and predict the response before calculation. *Answer criterion:* state whether a linear, reciprocal, logarithmic or state-dependent relationship is being used, and explain why it is valid over the selected interval.

**Exercise C — Diagnose.** Evaluate this proposed shortcut: "Adding a separate pv flow-work term after already using h in a steady-flow balance." *Answer criterion:* identify the missing assumption, specify a condition where the shortcut fails, and propose one measurement or alternate model that would expose the error.

## 7. Extended case and reproducible handover

Return to the **air-compressor test stand** case that motivates this unit. The objective is to reconcile measured electricity, shaft output and outlet enthalpy. Use this lesson's principle to create a two-column comparison between a minimal classroom calculation and a safer engineering estimate. The classroom side should contain only quantities supported by the basic model; the engineering side should add motor losses, leakage, pulsation, pressure taps and inlet humidity. For each added quantity, say whether it is known, must be measured, can be estimated from trustworthy property data, or is impossible to infer from the current information. Where a value is unknown, retain a symbol or range instead of fabricating a precise number.


## 8. Closing self-test

Without viewing your notes, explain why the same physical device can be modeled with different boundaries, which quantities change accordingly and which conservation principles remain unchanged. Explain the relationship in your own words before quoting its symbols. If you cannot distinguish a property from a path function, or theoretical limit from verified behavior, revisit the model formulation rather than memorizing the numerical answer.


---

# Unit 4, Lesson 3 — Nozzles, diffusers and kinetic energy

**Learning goals.** Explain the physical meaning of the stated relationship; use the example to reconstruct a verifiable answer; identify at least two model limitations; and propose an independent check.

## 1. Physical question and conceptual model

When a nozzle is adiabatic and has negligible shaft work, a drop in specific enthalpy increases flow kinetic energy. Diffusers do the reverse. Actual devices lose stagnation pressure through friction and shocks. If changes in elevation are modest, speed can be inferred from the enthalpy decrease with a factor of 1000 for kJ/kg to J/kg.


**Professional use.** Compare ideal predicted speed with velocimetry and note shock, friction and heat-loss effects. Avoid jumping from a property value to a performance guarantee: the former describes an assumed state, and the latter depends on losses, materials, reliability and operating limits.

## 2. Build the mathematical relationship

**Governing statement:** `V2²≈V1²+2×1000(h1−h2)`.


**Model qualification.** The equation is meaningful only when its state and process assumptions are satisfied. Some equations are conservation balances that remain exact for their declared boundary; others are constitutive approximations, such as an ideal-gas relation, a constant heat capacity or an isentropic reference process. Determine which category this statement belongs to. Explain whether extra phenomena such as a moving boundary, leakage, heat loss, multiphase conditions, kinetic energy, electrical work or chemical reaction would add terms or require a different property source. If the process is transient, ask whether an accumulation term is missing.

## 3. Worked teaching example

At V1=40 m/s and an enthalpy drop of 20 kJ/kg, V2≈204 m/s.


**Interpretive check.** Does the result increase or decrease when the principal driving condition becomes stronger? Does the prediction approach a sensible limit when the temperature difference, flow rate, state change or relevant force approaches zero? Such limiting tests are not substitutes for a measurement, but they are effective at rejecting a broken model before the expensive stage of building apparatus or selecting equipment.

## 4. Failure analysis and engineering judgement

**A tempting but incorrect shortcut:** Forgetting the 1000 conversion or assuming h2 is always lower in a diffuser.

Investigate what this shortcut assumes about the device or material. Predict whether it would overstate useful work, misstate the phase, hide a heat leak or suppress a needed transport term. Estimate the direction of the bias before estimating its size. A numerical calculation that conserves energy can still violate the second law; similarly, a temperature prediction can be inconsistent with phase equilibrium. Test both conservation and state feasibility. Where the model is an ideal upper or lower bound, identify which side of the bound a real machine should occupy under comparable conditions.

**Engineering context.** Compare ideal predicted speed with velocimetry and note shock, friction and heat-loss effects. A useful report would specify the relevant operating range, which properties are tabulated or calculated, and which assumptions are supported by evidence. It would not claim that an attractive textbook efficiency, coefficient of performance or output power proves achievable production performance.

## 5. Verification and measurement protocol

Design a simple check of **nozzles, diffusers and kinetic energy**. Specify a control volume or control mass, boundary conditions, primary observations and sampling interval. Report whether the observation is direct (temperature, mass, voltage, volumetric flow), indirectly inferred (enthalpy, dryness fraction, exergy), or fitted from an empirical relation. Distinguish repeatability from model validity: a repeatable sensor can be wrongly calibrated, and a perfectly reproducible computer program can implement the wrong equation. Identify one test in which the idealization should perform reasonably, and a second test where a named assumption may break down. If you use fluid property tables or software, record its provenance, units, reference state and interpolation method.


## 6. Questions and answer criteria

**Exercise A — Reconstruct.** Reproduce the stated worked example with symbols, units and at least one limiting check. *Answer criterion:* obtain the stated value within rounding and explain each term in `V2²≈V1²+2×1000(h1−h2)`.

**Exercise B — Predict.** Select one physically independent input, change it by 10%, and predict the response before calculation. *Answer criterion:* state whether a linear, reciprocal, logarithmic or state-dependent relationship is being used, and explain why it is valid over the selected interval.

**Exercise C — Diagnose.** Evaluate this proposed shortcut: "Forgetting the 1000 conversion or assuming h2 is always lower in a diffuser." *Answer criterion:* identify the missing assumption, specify a condition where the shortcut fails, and propose one measurement or alternate model that would expose the error.

## 7. Extended case and reproducible handover

Return to the **air-compressor test stand** case that motivates this unit. The objective is to reconcile measured electricity, shaft output and outlet enthalpy. Use this lesson's principle to create a two-column comparison between a minimal classroom calculation and a safer engineering estimate. The classroom side should contain only quantities supported by the basic model; the engineering side should add motor losses, leakage, pulsation, pressure taps and inlet humidity. For each added quantity, say whether it is known, must be measured, can be estimated from trustworthy property data, or is impossible to infer from the current information. Where a value is unknown, retain a symbol or range instead of fabricating a precise number.


## 8. Closing self-test

Without viewing your notes, explain why the same physical device can be modeled with different boundaries, which quantities change accordingly and which conservation principles remain unchanged. Explain the relationship in your own words before quoting its symbols. If you cannot distinguish a property from a path function, or theoretical limit from verified behavior, revisit the model formulation rather than memorizing the numerical answer.


---

# Unit 4, Lesson 4 — Turbines, compressors and pumps

**Learning goals.** Explain the physical meaning of the stated relationship; use the example to reconstruct a verifiable answer; identify at least two model limitations; and propose an independent check.

## 1. Physical question and conceptual model

For an approximately adiabatic steady turbine with negligible velocity and elevation changes, shaft power out is ṁ(h_in−h_out). A compressor consumes power as stream enthalpy rises. Pumping nearly incompressible liquid permits w_in≈v(p_out−p_in) as an ideal limiting estimate.


**Professional use.** Keep mechanical drive losses separate from the working-fluid first-law power. Avoid jumping from a property value to a performance guarantee: the former describes an assumed state, and the latter depends on losses, materials, reliability and operating limits.

## 2. Build the mathematical relationship

**Governing statement:** `Wdot_t≈ṁ(h_in−h_out)`.


**Model qualification.** The equation is meaningful only when its state and process assumptions are satisfied. Some equations are conservation balances that remain exact for their declared boundary; others are constitutive approximations, such as an ideal-gas relation, a constant heat capacity or an isentropic reference process. Determine which category this statement belongs to. Explain whether extra phenomena such as a moving boundary, leakage, heat loss, multiphase conditions, kinetic energy, electrical work or chemical reaction would add terms or require a different property source. If the process is transient, ask whether an accumulation term is missing.

## 3. Worked teaching example

Steam flows at 3 kg/s and drops 80 kJ/kg in enthalpy; idealized turbine shaft output is about 240 kW.


**Interpretive check.** Does the result increase or decrease when the principal driving condition becomes stronger? Does the prediction approach a sensible limit when the temperature difference, flow rate, state change or relevant force approaches zero? Such limiting tests are not substitutes for a measurement, but they are effective at rejecting a broken model before the expensive stage of building apparatus or selecting equipment.

## 4. Failure analysis and engineering judgement

**A tempting but incorrect shortcut:** Computing shaft power from pressure ratio alone without fluid properties or device efficiency.

Investigate what this shortcut assumes about the device or material. Predict whether it would overstate useful work, misstate the phase, hide a heat leak or suppress a needed transport term. Estimate the direction of the bias before estimating its size. A numerical calculation that conserves energy can still violate the second law; similarly, a temperature prediction can be inconsistent with phase equilibrium. Test both conservation and state feasibility. Where the model is an ideal upper or lower bound, identify which side of the bound a real machine should occupy under comparable conditions.

**Engineering context.** Keep mechanical drive losses separate from the working-fluid first-law power. A useful report would specify the relevant operating range, which properties are tabulated or calculated, and which assumptions are supported by evidence. It would not claim that an attractive textbook efficiency, coefficient of performance or output power proves achievable production performance.

## 5. Verification and measurement protocol

Design a simple check of **turbines, compressors and pumps**. Specify a control volume or control mass, boundary conditions, primary observations and sampling interval. Report whether the observation is direct (temperature, mass, voltage, volumetric flow), indirectly inferred (enthalpy, dryness fraction, exergy), or fitted from an empirical relation. Distinguish repeatability from model validity: a repeatable sensor can be wrongly calibrated, and a perfectly reproducible computer program can implement the wrong equation. Identify one test in which the idealization should perform reasonably, and a second test where a named assumption may break down. If you use fluid property tables or software, record its provenance, units, reference state and interpolation method.


## 6. Questions and answer criteria

**Exercise A — Reconstruct.** Reproduce the stated worked example with symbols, units and at least one limiting check. *Answer criterion:* obtain the stated value within rounding and explain each term in `Wdot_t≈ṁ(h_in−h_out)`.

**Exercise B — Predict.** Select one physically independent input, change it by 10%, and predict the response before calculation. *Answer criterion:* state whether a linear, reciprocal, logarithmic or state-dependent relationship is being used, and explain why it is valid over the selected interval.

**Exercise C — Diagnose.** Evaluate this proposed shortcut: "Computing shaft power from pressure ratio alone without fluid properties or device efficiency." *Answer criterion:* identify the missing assumption, specify a condition where the shortcut fails, and propose one measurement or alternate model that would expose the error.

## 7. Extended case and reproducible handover

Return to the **air-compressor test stand** case that motivates this unit. The objective is to reconcile measured electricity, shaft output and outlet enthalpy. Use this lesson's principle to create a two-column comparison between a minimal classroom calculation and a safer engineering estimate. The classroom side should contain only quantities supported by the basic model; the engineering side should add motor losses, leakage, pulsation, pressure taps and inlet humidity. For each added quantity, say whether it is known, must be measured, can be estimated from trustworthy property data, or is impossible to infer from the current information. Where a value is unknown, retain a symbol or range instead of fabricating a precise number.


## 8. Closing self-test

Without viewing your notes, explain why the same physical device can be modeled with different boundaries, which quantities change accordingly and which conservation principles remain unchanged. Explain the relationship in your own words before quoting its symbols. If you cannot distinguish a property from a path function, or theoretical limit from verified behavior, revisit the model formulation rather than memorizing the numerical answer.


---

# Unit 4, Lesson 5 — Heat exchangers, throttles and mixing

**Learning goals.** Explain the physical meaning of the stated relationship; use the example to reconstruct a verifiable answer; identify at least two model limitations; and propose an independent check.

## 1. Physical question and conceptual model

For a two-stream insulated heat exchanger, energy leaving the hot stream approximately equals energy gained by the cold stream, if other energy terms are small. A throttling valve with negligible heat and shaft work is approximately isoenthalpic, not isothermal. An adiabatic mixing junction conserves mass and inlet enthalpy fluxes.


**Professional use.** Look for two-phase flashing, fouling, pinch constraints and phase-dependent cp. Avoid jumping from a property value to a performance guarantee: the former describes an assumed state, and the latter depends on losses, materials, reliability and operating limits.

## 2. Build the mathematical relationship

**Governing statement:** `Σṁ_in h_in≈Σṁ_out h_out for steady adiabatic mixing`.


**Model qualification.** The equation is meaningful only when its state and process assumptions are satisfied. Some equations are conservation balances that remain exact for their declared boundary; others are constitutive approximations, such as an ideal-gas relation, a constant heat capacity or an isentropic reference process. Determine which category this statement belongs to. Explain whether extra phenomena such as a moving boundary, leakage, heat loss, multiphase conditions, kinetic energy, electrical work or chemical reaction would add terms or require a different property source. If the process is transient, ask whether an accumulation term is missing.

## 3. Worked teaching example

One kg/s at h=400 kJ/kg mixes with 2 kg/s at h=100 kJ/kg; outlet h≈200 kJ/kg.


**Interpretive check.** Does the result increase or decrease when the principal driving condition becomes stronger? Does the prediction approach a sensible limit when the temperature difference, flow rate, state change or relevant force approaches zero? Such limiting tests are not substitutes for a measurement, but they are effective at rejecting a broken model before the expensive stage of building apparatus or selecting equipment.

## 4. Failure analysis and engineering judgement

**A tempting but incorrect shortcut:** Claiming a valve increases enthalpy simply because pressure drops.

Investigate what this shortcut assumes about the device or material. Predict whether it would overstate useful work, misstate the phase, hide a heat leak or suppress a needed transport term. Estimate the direction of the bias before estimating its size. A numerical calculation that conserves energy can still violate the second law; similarly, a temperature prediction can be inconsistent with phase equilibrium. Test both conservation and state feasibility. Where the model is an ideal upper or lower bound, identify which side of the bound a real machine should occupy under comparable conditions.

**Engineering context.** Look for two-phase flashing, fouling, pinch constraints and phase-dependent cp. A useful report would specify the relevant operating range, which properties are tabulated or calculated, and which assumptions are supported by evidence. It would not claim that an attractive textbook efficiency, coefficient of performance or output power proves achievable production performance.

## 5. Verification and measurement protocol

Design a simple check of **heat exchangers, throttles and mixing**. Specify a control volume or control mass, boundary conditions, primary observations and sampling interval. Report whether the observation is direct (temperature, mass, voltage, volumetric flow), indirectly inferred (enthalpy, dryness fraction, exergy), or fitted from an empirical relation. Distinguish repeatability from model validity: a repeatable sensor can be wrongly calibrated, and a perfectly reproducible computer program can implement the wrong equation. Identify one test in which the idealization should perform reasonably, and a second test where a named assumption may break down. If you use fluid property tables or software, record its provenance, units, reference state and interpolation method.


## 6. Questions and answer criteria

**Exercise A — Reconstruct.** Reproduce the stated worked example with symbols, units and at least one limiting check. *Answer criterion:* obtain the stated value within rounding and explain each term in `Σṁ_in h_in≈Σṁ_out h_out for steady adiabatic mixing`.

**Exercise B — Predict.** Select one physically independent input, change it by 10%, and predict the response before calculation. *Answer criterion:* state whether a linear, reciprocal, logarithmic or state-dependent relationship is being used, and explain why it is valid over the selected interval.

**Exercise C — Diagnose.** Evaluate this proposed shortcut: "Claiming a valve increases enthalpy simply because pressure drops." *Answer criterion:* identify the missing assumption, specify a condition where the shortcut fails, and propose one measurement or alternate model that would expose the error.

## 7. Extended case and reproducible handover

Return to the **air-compressor test stand** case that motivates this unit. The objective is to reconcile measured electricity, shaft output and outlet enthalpy. Use this lesson's principle to create a two-column comparison between a minimal classroom calculation and a safer engineering estimate. The classroom side should contain only quantities supported by the basic model; the engineering side should add motor losses, leakage, pulsation, pressure taps and inlet humidity. For each added quantity, say whether it is known, must be measured, can be estimated from trustworthy property data, or is impossible to infer from the current information. Where a value is unknown, retain a symbol or range instead of fabricating a precise number.


## 8. Closing self-test

Without viewing your notes, explain why the same physical device can be modeled with different boundaries, which quantities change accordingly and which conservation principles remain unchanged. Explain the relationship in your own words before quoting its symbols. If you cannot distinguish a property from a path function, or theoretical limit from verified behavior, revisit the model formulation rather than memorizing the numerical answer.


---

