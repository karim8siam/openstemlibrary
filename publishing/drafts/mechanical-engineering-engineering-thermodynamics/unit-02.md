# Unit 2: Pure Substances, Phase Diagrams, and Equations of State

# Unit 2, Lesson 1 — Phase diagrams and pure-substance regions

**Learning goals.** Explain the physical meaning of the stated relationship; use the example to reconstruct a verifiable answer; identify at least two model limitations; and propose an independent check.

## 1. Physical question and conceptual model

The p–T coexistence line marks where two phases have equal chemical potential, not where a vessel necessarily contains equal amounts of each phase. In p–v and T–v drawings, the saturation dome separates single-phase states from liquid–vapor mixtures. The critical point marks the end of a distinguishable liquid–vapor boundary.


**Professional use.** Mark saturated-liquid, two-phase, saturated-vapor and superheated regions on a property sketch. Avoid jumping from a property value to a performance guarantee: the former describes an assumed state, and the latter depends on losses, materials, reliability and operating limits.

## 2. Build the mathematical relationship

**Governing statement:** `At saturation for a pure substance, T=T_sat(p)`.


**Model qualification.** The equation is meaningful only when its state and process assumptions are satisfied. Some equations are conservation balances that remain exact for their declared boundary; others are constitutive approximations, such as an ideal-gas relation, a constant heat capacity or an isentropic reference process. Determine which category this statement belongs to. Explain whether extra phenomena such as a moving boundary, leakage, heat loss, multiphase conditions, kinetic energy, electrical work or chemical reaction would add terms or require a different property source. If the process is transient, ask whether an accumulation term is missing.

## 3. Worked teaching example

At about atmospheric pressure, water has a saturation temperature near 100 °C; a sample at this p and T might have any equilibrium quality between zero and one.


**Interpretive check.** Does the result increase or decrease when the principal driving condition becomes stronger? Does the prediction approach a sensible limit when the temperature difference, flow rate, state change or relevant force approaches zero? Such limiting tests are not substitutes for a measurement, but they are effective at rejecting a broken model before the expensive stage of building apparatus or selecting equipment.

## 4. Failure analysis and engineering judgement

**A tempting but incorrect shortcut:** Inferring a unique vapor fraction from saturation temperature alone.

Investigate what this shortcut assumes about the device or material. Predict whether it would overstate useful work, misstate the phase, hide a heat leak or suppress a needed transport term. Estimate the direction of the bias before estimating its size. A numerical calculation that conserves energy can still violate the second law; similarly, a temperature prediction can be inconsistent with phase equilibrium. Test both conservation and state feasibility. Where the model is an ideal upper or lower bound, identify which side of the bound a real machine should occupy under comparable conditions.

**Engineering context.** Mark saturated-liquid, two-phase, saturated-vapor and superheated regions on a property sketch. A useful report would specify the relevant operating range, which properties are tabulated or calculated, and which assumptions are supported by evidence. It would not claim that an attractive textbook efficiency, coefficient of performance or output power proves achievable production performance.

## 5. Verification and measurement protocol

Design a simple check of **phase diagrams and pure-substance regions**. Specify a control volume or control mass, boundary conditions, primary observations and sampling interval. Report whether the observation is direct (temperature, mass, voltage, volumetric flow), indirectly inferred (enthalpy, dryness fraction, exergy), or fitted from an empirical relation. Distinguish repeatability from model validity: a repeatable sensor can be wrongly calibrated, and a perfectly reproducible computer program can implement the wrong equation. Identify one test in which the idealization should perform reasonably, and a second test where a named assumption may break down. If you use fluid property tables or software, record its provenance, units, reference state and interpolation method.


## 6. Questions and answer criteria

**Exercise A — Reconstruct.** Reproduce the stated worked example with symbols, units and at least one limiting check. *Answer criterion:* obtain the stated value within rounding and explain each term in `At saturation for a pure substance, T=T_sat(p)`.

**Exercise B — Predict.** Select one physically independent input, change it by 10%, and predict the response before calculation. *Answer criterion:* state whether a linear, reciprocal, logarithmic or state-dependent relationship is being used, and explain why it is valid over the selected interval.

**Exercise C — Diagnose.** Evaluate this proposed shortcut: "Inferring a unique vapor fraction from saturation temperature alone." *Answer criterion:* identify the missing assumption, specify a condition where the shortcut fails, and propose one measurement or alternate model that would expose the error.

## 7. Extended case and reproducible handover

Return to the **steam accumulator** case that motivates this unit. The operator must know whether withdrawal causes flash evaporation. Use this lesson's principle to create a two-column comparison between a minimal classroom calculation and a safer engineering estimate. The classroom side should contain only quantities supported by the basic model; the engineering side should add mixture stratification, property sources, valve losses and transients. For each added quantity, say whether it is known, must be measured, can be estimated from trustworthy property data, or is impossible to infer from the current information. Where a value is unknown, retain a symbol or range instead of fabricating a precise number.


## 8. Closing self-test

Without viewing your notes, explain why the same physical device can be modeled with different boundaries, which quantities change accordingly and which conservation principles remain unchanged. Explain the relationship in your own words before quoting its symbols. If you cannot distinguish a property from a path function, or theoretical limit from verified behavior, revisit the model formulation rather than memorizing the numerical answer.


---

# Unit 2, Lesson 2 — Steam tables and property lookup

**Learning goals.** Explain the physical meaning of the stated relationship; use the example to reconstruct a verifiable answer; identify at least two model limitations; and propose an independent check.

## 1. Physical question and conceptual model

Property tables typically list specific volume, internal energy, enthalpy and entropy. Selecting an incorrect pressure row creates a systematic modeling error larger than interpolation rounding. Report the source, stated reference conventions and state designation. Internal energy and enthalpy serve different energy-balance roles, especially in flowing systems.


**Professional use.** Explain why an enthalpy value is meaningful only with specified composition, state and convention. Avoid jumping from a property value to a performance guarantee: the former describes an assumed state, and the latter depends on losses, materials, reliability and operating limits.

## 2. Build the mathematical relationship

**Governing statement:** `h=u+pv`.


**Model qualification.** The equation is meaningful only when its state and process assumptions are satisfied. Some equations are conservation balances that remain exact for their declared boundary; others are constitutive approximations, such as an ideal-gas relation, a constant heat capacity or an isentropic reference process. Determine which category this statement belongs to. Explain whether extra phenomena such as a moving boundary, leakage, heat loss, multiphase conditions, kinetic energy, electrical work or chemical reaction would add terms or require a different property source. If the process is transient, ask whether an accumulation term is missing.

## 3. Worked teaching example

For saturated water at 100 °C, taking h_f≈419 and h_fg≈2257 kJ/kg gives h≈1547.5 kJ/kg at x=0.50.


**Interpretive check.** Does the result increase or decrease when the principal driving condition becomes stronger? Does the prediction approach a sensible limit when the temperature difference, flow rate, state change or relevant force approaches zero? Such limiting tests are not substitutes for a measurement, but they are effective at rejecting a broken model before the expensive stage of building apparatus or selecting equipment.

## 4. Failure analysis and engineering judgement

**A tempting but incorrect shortcut:** Mixing saturated-liquid and superheated data from incompatible reference bases.

Investigate what this shortcut assumes about the device or material. Predict whether it would overstate useful work, misstate the phase, hide a heat leak or suppress a needed transport term. Estimate the direction of the bias before estimating its size. A numerical calculation that conserves energy can still violate the second law; similarly, a temperature prediction can be inconsistent with phase equilibrium. Test both conservation and state feasibility. Where the model is an ideal upper or lower bound, identify which side of the bound a real machine should occupy under comparable conditions.

**Engineering context.** Explain why an enthalpy value is meaningful only with specified composition, state and convention. A useful report would specify the relevant operating range, which properties are tabulated or calculated, and which assumptions are supported by evidence. It would not claim that an attractive textbook efficiency, coefficient of performance or output power proves achievable production performance.

## 5. Verification and measurement protocol

Design a simple check of **steam tables and property lookup**. Specify a control volume or control mass, boundary conditions, primary observations and sampling interval. Report whether the observation is direct (temperature, mass, voltage, volumetric flow), indirectly inferred (enthalpy, dryness fraction, exergy), or fitted from an empirical relation. Distinguish repeatability from model validity: a repeatable sensor can be wrongly calibrated, and a perfectly reproducible computer program can implement the wrong equation. Identify one test in which the idealization should perform reasonably, and a second test where a named assumption may break down. If you use fluid property tables or software, record its provenance, units, reference state and interpolation method.


## 6. Questions and answer criteria

**Exercise A — Reconstruct.** Reproduce the stated worked example with symbols, units and at least one limiting check. *Answer criterion:* obtain the stated value within rounding and explain each term in `h=u+pv`.

**Exercise B — Predict.** Select one physically independent input, change it by 10%, and predict the response before calculation. *Answer criterion:* state whether a linear, reciprocal, logarithmic or state-dependent relationship is being used, and explain why it is valid over the selected interval.

**Exercise C — Diagnose.** Evaluate this proposed shortcut: "Mixing saturated-liquid and superheated data from incompatible reference bases." *Answer criterion:* identify the missing assumption, specify a condition where the shortcut fails, and propose one measurement or alternate model that would expose the error.

## 7. Extended case and reproducible handover

Return to the **steam accumulator** case that motivates this unit. The operator must know whether withdrawal causes flash evaporation. Use this lesson's principle to create a two-column comparison between a minimal classroom calculation and a safer engineering estimate. The classroom side should contain only quantities supported by the basic model; the engineering side should add mixture stratification, property sources, valve losses and transients. For each added quantity, say whether it is known, must be measured, can be estimated from trustworthy property data, or is impossible to infer from the current information. Where a value is unknown, retain a symbol or range instead of fabricating a precise number.


## 8. Closing self-test

Without viewing your notes, explain why the same physical device can be modeled with different boundaries, which quantities change accordingly and which conservation principles remain unchanged. Explain the relationship in your own words before quoting its symbols. If you cannot distinguish a property from a path function, or theoretical limit from verified behavior, revisit the model formulation rather than memorizing the numerical answer.


---

# Unit 2, Lesson 3 — Vapor quality and mixture relations

**Learning goals.** Explain the physical meaning of the stated relationship; use the example to reconstruct a verifiable answer; identify at least two model limitations; and propose an independent check.

## 1. Physical question and conceptual model

If a two-phase sample has liquid mass m_f and vapor mass m_g, quality x=m_g/(m_f+m_g). For a specific extensive property y, y=(1−x)y_f+xy_g. Volume fractions require additional weighting because liquid and vapor specific volumes differ dramatically.


**Professional use.** Test a proposed quality by checking 0≤x≤1 and locating the state in the dome. Avoid jumping from a property value to a performance guarantee: the former describes an assumed state, and the latter depends on losses, materials, reliability and operating limits.

## 2. Build the mathematical relationship

**Governing statement:** `x=(h−h_f)/(h_g−h_f)`.


**Model qualification.** The equation is meaningful only when its state and process assumptions are satisfied. Some equations are conservation balances that remain exact for their declared boundary; others are constitutive approximations, such as an ideal-gas relation, a constant heat capacity or an isentropic reference process. Determine which category this statement belongs to. Explain whether extra phenomena such as a moving boundary, leakage, heat loss, multiphase conditions, kinetic energy, electrical work or chemical reaction would add terms or require a different property source. If the process is transient, ask whether an accumulation term is missing.

## 3. Worked teaching example

At h=1547.5 kJ/kg, h_f=419 and h_g=2676 kJ/kg, quality is x≈0.50.


**Interpretive check.** Does the result increase or decrease when the principal driving condition becomes stronger? Does the prediction approach a sensible limit when the temperature difference, flow rate, state change or relevant force approaches zero? Such limiting tests are not substitutes for a measurement, but they are effective at rejecting a broken model before the expensive stage of building apparatus or selecting equipment.

## 4. Failure analysis and engineering judgement

**A tempting but incorrect shortcut:** Treating quality 0.5 as a vessel that is half liquid and half vapor by volume.

Investigate what this shortcut assumes about the device or material. Predict whether it would overstate useful work, misstate the phase, hide a heat leak or suppress a needed transport term. Estimate the direction of the bias before estimating its size. A numerical calculation that conserves energy can still violate the second law; similarly, a temperature prediction can be inconsistent with phase equilibrium. Test both conservation and state feasibility. Where the model is an ideal upper or lower bound, identify which side of the bound a real machine should occupy under comparable conditions.

**Engineering context.** Test a proposed quality by checking 0≤x≤1 and locating the state in the dome. A useful report would specify the relevant operating range, which properties are tabulated or calculated, and which assumptions are supported by evidence. It would not claim that an attractive textbook efficiency, coefficient of performance or output power proves achievable production performance.

## 5. Verification and measurement protocol

Design a simple check of **vapor quality and mixture relations**. Specify a control volume or control mass, boundary conditions, primary observations and sampling interval. Report whether the observation is direct (temperature, mass, voltage, volumetric flow), indirectly inferred (enthalpy, dryness fraction, exergy), or fitted from an empirical relation. Distinguish repeatability from model validity: a repeatable sensor can be wrongly calibrated, and a perfectly reproducible computer program can implement the wrong equation. Identify one test in which the idealization should perform reasonably, and a second test where a named assumption may break down. If you use fluid property tables or software, record its provenance, units, reference state and interpolation method.


## 6. Questions and answer criteria

**Exercise A — Reconstruct.** Reproduce the stated worked example with symbols, units and at least one limiting check. *Answer criterion:* obtain the stated value within rounding and explain each term in `x=(h−h_f)/(h_g−h_f)`.

**Exercise B — Predict.** Select one physically independent input, change it by 10%, and predict the response before calculation. *Answer criterion:* state whether a linear, reciprocal, logarithmic or state-dependent relationship is being used, and explain why it is valid over the selected interval.

**Exercise C — Diagnose.** Evaluate this proposed shortcut: "Treating quality 0.5 as a vessel that is half liquid and half vapor by volume." *Answer criterion:* identify the missing assumption, specify a condition where the shortcut fails, and propose one measurement or alternate model that would expose the error.

## 7. Extended case and reproducible handover

Return to the **steam accumulator** case that motivates this unit. The operator must know whether withdrawal causes flash evaporation. Use this lesson's principle to create a two-column comparison between a minimal classroom calculation and a safer engineering estimate. The classroom side should contain only quantities supported by the basic model; the engineering side should add mixture stratification, property sources, valve losses and transients. For each added quantity, say whether it is known, must be measured, can be estimated from trustworthy property data, or is impossible to infer from the current information. Where a value is unknown, retain a symbol or range instead of fabricating a precise number.


## 8. Closing self-test

Without viewing your notes, explain why the same physical device can be modeled with different boundaries, which quantities change accordingly and which conservation principles remain unchanged. Explain the relationship in your own words before quoting its symbols. If you cannot distinguish a property from a path function, or theoretical limit from verified behavior, revisit the model formulation rather than memorizing the numerical answer.


---

# Unit 2, Lesson 4 — Superheated and compressed states

**Learning goals.** Explain the physical meaning of the stated relationship; use the example to reconstruct a verifiable answer; identify at least two model limitations; and propose an independent check.

## 1. Physical question and conceptual model

At a given pressure, a gas hotter than saturation temperature is superheated vapor; a liquid colder than saturation temperature is subcooled or compressed liquid. Pressure changes at fixed temperature can alter phase classification. State-property interpolation should follow the arrangement of the source table, never a guessed linear temperature dependence of all properties.


**Professional use.** Compare approximation size with latent heat and cite the domain over which c_p was assumed constant. Avoid jumping from a property value to a performance guarantee: the former describes an assumed state, and the latter depends on losses, materials, reliability and operating limits.

## 2. Build the mathematical relationship

**Governing statement:** `Δh≈c_p ΔT for a small single-phase interval when c_p is reasonably constant`.


**Model qualification.** The equation is meaningful only when its state and process assumptions are satisfied. Some equations are conservation balances that remain exact for their declared boundary; others are constitutive approximations, such as an ideal-gas relation, a constant heat capacity or an isentropic reference process. Determine which category this statement belongs to. Explain whether extra phenomena such as a moving boundary, leakage, heat loss, multiphase conditions, kinetic energy, electrical work or chemical reaction would add terms or require a different property source. If the process is transient, ask whether an accumulation term is missing.

## 3. Worked teaching example

For a single-phase fluid with c_p≈2.0 kJ/(kg K), a 15 K increase gives Δh≈30 kJ/kg.


**Interpretive check.** Does the result increase or decrease when the principal driving condition becomes stronger? Does the prediction approach a sensible limit when the temperature difference, flow rate, state change or relevant force approaches zero? Such limiting tests are not substitutes for a measurement, but they are effective at rejecting a broken model before the expensive stage of building apparatus or selecting equipment.

## 4. Failure analysis and engineering judgement

**A tempting but incorrect shortcut:** Applying a constant-c_p estimate while the state crosses a phase boundary.

Investigate what this shortcut assumes about the device or material. Predict whether it would overstate useful work, misstate the phase, hide a heat leak or suppress a needed transport term. Estimate the direction of the bias before estimating its size. A numerical calculation that conserves energy can still violate the second law; similarly, a temperature prediction can be inconsistent with phase equilibrium. Test both conservation and state feasibility. Where the model is an ideal upper or lower bound, identify which side of the bound a real machine should occupy under comparable conditions.

**Engineering context.** Compare approximation size with latent heat and cite the domain over which c_p was assumed constant. A useful report would specify the relevant operating range, which properties are tabulated or calculated, and which assumptions are supported by evidence. It would not claim that an attractive textbook efficiency, coefficient of performance or output power proves achievable production performance.

## 5. Verification and measurement protocol

Design a simple check of **superheated and compressed states**. Specify a control volume or control mass, boundary conditions, primary observations and sampling interval. Report whether the observation is direct (temperature, mass, voltage, volumetric flow), indirectly inferred (enthalpy, dryness fraction, exergy), or fitted from an empirical relation. Distinguish repeatability from model validity: a repeatable sensor can be wrongly calibrated, and a perfectly reproducible computer program can implement the wrong equation. Identify one test in which the idealization should perform reasonably, and a second test where a named assumption may break down. If you use fluid property tables or software, record its provenance, units, reference state and interpolation method.


## 6. Questions and answer criteria

**Exercise A — Reconstruct.** Reproduce the stated worked example with symbols, units and at least one limiting check. *Answer criterion:* obtain the stated value within rounding and explain each term in `Δh≈c_p ΔT for a small single-phase interval when c_p is reasonably constant`.

**Exercise B — Predict.** Select one physically independent input, change it by 10%, and predict the response before calculation. *Answer criterion:* state whether a linear, reciprocal, logarithmic or state-dependent relationship is being used, and explain why it is valid over the selected interval.

**Exercise C — Diagnose.** Evaluate this proposed shortcut: "Applying a constant-c_p estimate while the state crosses a phase boundary." *Answer criterion:* identify the missing assumption, specify a condition where the shortcut fails, and propose one measurement or alternate model that would expose the error.

## 7. Extended case and reproducible handover

Return to the **steam accumulator** case that motivates this unit. The operator must know whether withdrawal causes flash evaporation. Use this lesson's principle to create a two-column comparison between a minimal classroom calculation and a safer engineering estimate. The classroom side should contain only quantities supported by the basic model; the engineering side should add mixture stratification, property sources, valve losses and transients. For each added quantity, say whether it is known, must be measured, can be estimated from trustworthy property data, or is impossible to infer from the current information. Where a value is unknown, retain a symbol or range instead of fabricating a precise number.


## 8. Closing self-test

Without viewing your notes, explain why the same physical device can be modeled with different boundaries, which quantities change accordingly and which conservation principles remain unchanged. Explain the relationship in your own words before quoting its symbols. If you cannot distinguish a property from a path function, or theoretical limit from verified behavior, revisit the model formulation rather than memorizing the numerical answer.


---

# Unit 2, Lesson 5 — Ideal gases, compressibility and real fluids

**Learning goals.** Explain the physical meaning of the stated relationship; use the example to reconstruct a verifiable answer; identify at least two model limitations; and propose an independent check.

## 1. Physical question and conceptual model

The ideal gas model pV=mRT uses a specific gas constant. Its adequacy depends on pressure, temperature and molecular interactions. The compressibility factor Z=pv/(RT) measures departure from ideal-gas behavior. For a defined gas, Z may be estimated from validated real-fluid correlations or software; it is not universally unity.


**Professional use.** Discuss whether high pressure, proximity to condensation or nonideal composition could invalidate Z≈1. Avoid jumping from a property value to a performance guarantee: the former describes an assumed state, and the latter depends on losses, materials, reliability and operating limits.

## 2. Build the mathematical relationship

**Governing statement:** `Z=pv/(RT)`.


**Model qualification.** The equation is meaningful only when its state and process assumptions are satisfied. Some equations are conservation balances that remain exact for their declared boundary; others are constitutive approximations, such as an ideal-gas relation, a constant heat capacity or an isentropic reference process. Determine which category this statement belongs to. Explain whether extra phenomena such as a moving boundary, leakage, heat loss, multiphase conditions, kinetic energy, electrical work or chemical reaction would add terms or require a different property source. If the process is transient, ask whether an accumulation term is missing.

## 3. Worked teaching example

For dry air with R=0.287 kJ/(kg K), p=100 kPa and T=300 K, ideal-gas v=0.861 m³/kg.


**Interpretive check.** Does the result increase or decrease when the principal driving condition becomes stronger? Does the prediction approach a sensible limit when the temperature difference, flow rate, state change or relevant force approaches zero? Such limiting tests are not substitutes for a measurement, but they are effective at rejecting a broken model before the expensive stage of building apparatus or selecting equipment.

## 4. Failure analysis and engineering judgement

**A tempting but incorrect shortcut:** Using the universal molar gas constant with kilograms without dividing by molar mass.

Investigate what this shortcut assumes about the device or material. Predict whether it would overstate useful work, misstate the phase, hide a heat leak or suppress a needed transport term. Estimate the direction of the bias before estimating its size. A numerical calculation that conserves energy can still violate the second law; similarly, a temperature prediction can be inconsistent with phase equilibrium. Test both conservation and state feasibility. Where the model is an ideal upper or lower bound, identify which side of the bound a real machine should occupy under comparable conditions.

**Engineering context.** Discuss whether high pressure, proximity to condensation or nonideal composition could invalidate Z≈1. A useful report would specify the relevant operating range, which properties are tabulated or calculated, and which assumptions are supported by evidence. It would not claim that an attractive textbook efficiency, coefficient of performance or output power proves achievable production performance.

## 5. Verification and measurement protocol

Design a simple check of **ideal gases, compressibility and real fluids**. Specify a control volume or control mass, boundary conditions, primary observations and sampling interval. Report whether the observation is direct (temperature, mass, voltage, volumetric flow), indirectly inferred (enthalpy, dryness fraction, exergy), or fitted from an empirical relation. Distinguish repeatability from model validity: a repeatable sensor can be wrongly calibrated, and a perfectly reproducible computer program can implement the wrong equation. Identify one test in which the idealization should perform reasonably, and a second test where a named assumption may break down. If you use fluid property tables or software, record its provenance, units, reference state and interpolation method.


## 6. Questions and answer criteria

**Exercise A — Reconstruct.** Reproduce the stated worked example with symbols, units and at least one limiting check. *Answer criterion:* obtain the stated value within rounding and explain each term in `Z=pv/(RT)`.

**Exercise B — Predict.** Select one physically independent input, change it by 10%, and predict the response before calculation. *Answer criterion:* state whether a linear, reciprocal, logarithmic or state-dependent relationship is being used, and explain why it is valid over the selected interval.

**Exercise C — Diagnose.** Evaluate this proposed shortcut: "Using the universal molar gas constant with kilograms without dividing by molar mass." *Answer criterion:* identify the missing assumption, specify a condition where the shortcut fails, and propose one measurement or alternate model that would expose the error.

## 7. Extended case and reproducible handover

Return to the **steam accumulator** case that motivates this unit. The operator must know whether withdrawal causes flash evaporation. Use this lesson's principle to create a two-column comparison between a minimal classroom calculation and a safer engineering estimate. The classroom side should contain only quantities supported by the basic model; the engineering side should add mixture stratification, property sources, valve losses and transients. For each added quantity, say whether it is known, must be measured, can be estimated from trustworthy property data, or is impossible to infer from the current information. Where a value is unknown, retain a symbol or range instead of fabricating a precise number.


## 8. Closing self-test

Without viewing your notes, explain why the same physical device can be modeled with different boundaries, which quantities change accordingly and which conservation principles remain unchanged. Explain the relationship in your own words before quoting its symbols. If you cannot distinguish a property from a path function, or theoretical limit from verified behavior, revisit the model formulation rather than memorizing the numerical answer.


---

