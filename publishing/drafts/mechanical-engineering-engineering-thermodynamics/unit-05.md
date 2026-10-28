# Unit 5: Second Law of Thermodynamics, Heat Engines, and Reversibility

# Unit 5, Lesson 1 — Thermal engines and reservoirs

**Learning goals.** Explain the physical meaning of the stated relationship; use the example to reconstruct a verifiable answer; identify at least two model limitations; and propose an independent check.

## 1. Physical question and conceptual model

A heat engine receives energy from a high-temperature source, yields net cyclic work and rejects heat to a lower-temperature sink. Energy conservation requires W_net=Q_H−Q_C. The source temperature is not the same as combustion-gas peak temperature unless the boundary and temperature histories justify that idealization.


**Professional use.** Compare device input, useful output and rejected heat in an energy flow diagram. Avoid jumping from a property value to a performance guarantee: the former describes an assumed state, and the latter depends on losses, materials, reliability and operating limits.

## 2. Build the mathematical relationship

**Governing statement:** `η_th=W_net/Q_H=1−Q_C/Q_H`.


**Model qualification.** The equation is meaningful only when its state and process assumptions are satisfied. Some equations are conservation balances that remain exact for their declared boundary; others are constitutive approximations, such as an ideal-gas relation, a constant heat capacity or an isentropic reference process. Determine which category this statement belongs to. Explain whether extra phenomena such as a moving boundary, leakage, heat loss, multiphase conditions, kinetic energy, electrical work or chemical reaction would add terms or require a different property source. If the process is transient, ask whether an accumulation term is missing.

## 3. Worked teaching example

An engine receives 1000 kJ and rejects 650 kJ per cycle; W=350 kJ and efficiency is 35%.


**Interpretive check.** Does the result increase or decrease when the principal driving condition becomes stronger? Does the prediction approach a sensible limit when the temperature difference, flow rate, state change or relevant force approaches zero? Such limiting tests are not substitutes for a measurement, but they are effective at rejecting a broken model before the expensive stage of building apparatus or selecting equipment.

## 4. Failure analysis and engineering judgement

**A tempting but incorrect shortcut:** Computing efficiency as Q_C/Q_H or treating all fuel chemical energy as delivered heat without specifying a boundary.

Investigate what this shortcut assumes about the device or material. Predict whether it would overstate useful work, misstate the phase, hide a heat leak or suppress a needed transport term. Estimate the direction of the bias before estimating its size. A numerical calculation that conserves energy can still violate the second law; similarly, a temperature prediction can be inconsistent with phase equilibrium. Test both conservation and state feasibility. Where the model is an ideal upper or lower bound, identify which side of the bound a real machine should occupy under comparable conditions.

**Engineering context.** Compare device input, useful output and rejected heat in an energy flow diagram. A useful report would specify the relevant operating range, which properties are tabulated or calculated, and which assumptions are supported by evidence. It would not claim that an attractive textbook efficiency, coefficient of performance or output power proves achievable production performance.

## 5. Verification and measurement protocol

Design a simple check of **thermal engines and reservoirs**. Specify a control volume or control mass, boundary conditions, primary observations and sampling interval. Report whether the observation is direct (temperature, mass, voltage, volumetric flow), indirectly inferred (enthalpy, dryness fraction, exergy), or fitted from an empirical relation. Distinguish repeatability from model validity: a repeatable sensor can be wrongly calibrated, and a perfectly reproducible computer program can implement the wrong equation. Identify one test in which the idealization should perform reasonably, and a second test where a named assumption may break down. If you use fluid property tables or software, record its provenance, units, reference state and interpolation method.


## 6. Questions and answer criteria

**Exercise A — Reconstruct.** Reproduce the stated worked example with symbols, units and at least one limiting check. *Answer criterion:* obtain the stated value within rounding and explain each term in `η_th=W_net/Q_H=1−Q_C/Q_H`.

**Exercise B — Predict.** Select one physically independent input, change it by 10%, and predict the response before calculation. *Answer criterion:* state whether a linear, reciprocal, logarithmic or state-dependent relationship is being used, and explain why it is valid over the selected interval.

**Exercise C — Diagnose.** Evaluate this proposed shortcut: "Computing efficiency as Q_C/Q_H or treating all fuel chemical energy as delivered heat without specifying a boundary." *Answer criterion:* identify the missing assumption, specify a condition where the shortcut fails, and propose one measurement or alternate model that would expose the error.

## 7. Extended case and reproducible handover

Return to the **industrial waste-heat engine** case that motivates this unit. The proposal must respect a reversible ceiling before return-on-investment claims. Use this lesson's principle to create a two-column comparison between a minimal classroom calculation and a safer engineering estimate. The classroom side should contain only quantities supported by the basic model; the engineering side should add heat exchanger approach, cooling-water temperature and auxiliary pumping. For each added quantity, say whether it is known, must be measured, can be estimated from trustworthy property data, or is impossible to infer from the current information. Where a value is unknown, retain a symbol or range instead of fabricating a precise number.


## 8. Closing self-test

Without viewing your notes, explain why the same physical device can be modeled with different boundaries, which quantities change accordingly and which conservation principles remain unchanged. Explain the relationship in your own words before quoting its symbols. If you cannot distinguish a property from a path function, or theoretical limit from verified behavior, revisit the model formulation rather than memorizing the numerical answer.


---

# Unit 5, Lesson 2 — Kelvin–Planck and Clausius statements

**Learning goals.** Explain the physical meaning of the stated relationship; use the example to reconstruct a verifiable answer; identify at least two model limitations; and propose an independent check.

## 1. Physical question and conceptual model

The Kelvin–Planck statement rules out a cyclic device whose sole effect is extraction of heat from one reservoir and complete conversion to work. The Clausius statement forbids heat flow from cold to hot without any other effect. They are logically linked by combining hypothetical violations with permitted devices.


**Professional use.** State the surrounding reservoirs and all other effects when testing an extraordinary claim. Avoid jumping from a property value to a performance guarantee: the former describes an assumed state, and the latter depends on losses, materials, reliability and operating limits.

## 2. Build the mathematical relationship

**Governing statement:** `Q_H=W_net+Q_C for an engine cycle`.


**Model qualification.** The equation is meaningful only when its state and process assumptions are satisfied. Some equations are conservation balances that remain exact for their declared boundary; others are constitutive approximations, such as an ideal-gas relation, a constant heat capacity or an isentropic reference process. Determine which category this statement belongs to. Explain whether extra phenomena such as a moving boundary, leakage, heat loss, multiphase conditions, kinetic energy, electrical work or chemical reaction would add terms or require a different property source. If the process is transient, ask whether an accumulation term is missing.

## 3. Worked teaching example

An asserted one-reservoir engine taking 500 kJ of heat and producing 500 kJ net cyclic work violates Kelvin–Planck, even though it conserves energy.


**Interpretive check.** Does the result increase or decrease when the principal driving condition becomes stronger? Does the prediction approach a sensible limit when the temperature difference, flow rate, state change or relevant force approaches zero? Such limiting tests are not substitutes for a measurement, but they are effective at rejecting a broken model before the expensive stage of building apparatus or selecting equipment.

## 4. Failure analysis and engineering judgement

**A tempting but incorrect shortcut:** Concluding that energy conservation alone establishes feasibility.

Investigate what this shortcut assumes about the device or material. Predict whether it would overstate useful work, misstate the phase, hide a heat leak or suppress a needed transport term. Estimate the direction of the bias before estimating its size. A numerical calculation that conserves energy can still violate the second law; similarly, a temperature prediction can be inconsistent with phase equilibrium. Test both conservation and state feasibility. Where the model is an ideal upper or lower bound, identify which side of the bound a real machine should occupy under comparable conditions.

**Engineering context.** State the surrounding reservoirs and all other effects when testing an extraordinary claim. A useful report would specify the relevant operating range, which properties are tabulated or calculated, and which assumptions are supported by evidence. It would not claim that an attractive textbook efficiency, coefficient of performance or output power proves achievable production performance.

## 5. Verification and measurement protocol

Design a simple check of **kelvin–planck and clausius statements**. Specify a control volume or control mass, boundary conditions, primary observations and sampling interval. Report whether the observation is direct (temperature, mass, voltage, volumetric flow), indirectly inferred (enthalpy, dryness fraction, exergy), or fitted from an empirical relation. Distinguish repeatability from model validity: a repeatable sensor can be wrongly calibrated, and a perfectly reproducible computer program can implement the wrong equation. Identify one test in which the idealization should perform reasonably, and a second test where a named assumption may break down. If you use fluid property tables or software, record its provenance, units, reference state and interpolation method.


## 6. Questions and answer criteria

**Exercise A — Reconstruct.** Reproduce the stated worked example with symbols, units and at least one limiting check. *Answer criterion:* obtain the stated value within rounding and explain each term in `Q_H=W_net+Q_C for an engine cycle`.

**Exercise B — Predict.** Select one physically independent input, change it by 10%, and predict the response before calculation. *Answer criterion:* state whether a linear, reciprocal, logarithmic or state-dependent relationship is being used, and explain why it is valid over the selected interval.

**Exercise C — Diagnose.** Evaluate this proposed shortcut: "Concluding that energy conservation alone establishes feasibility." *Answer criterion:* identify the missing assumption, specify a condition where the shortcut fails, and propose one measurement or alternate model that would expose the error.

## 7. Extended case and reproducible handover

Return to the **industrial waste-heat engine** case that motivates this unit. The proposal must respect a reversible ceiling before return-on-investment claims. Use this lesson's principle to create a two-column comparison between a minimal classroom calculation and a safer engineering estimate. The classroom side should contain only quantities supported by the basic model; the engineering side should add heat exchanger approach, cooling-water temperature and auxiliary pumping. For each added quantity, say whether it is known, must be measured, can be estimated from trustworthy property data, or is impossible to infer from the current information. Where a value is unknown, retain a symbol or range instead of fabricating a precise number.


## 8. Closing self-test

Without viewing your notes, explain why the same physical device can be modeled with different boundaries, which quantities change accordingly and which conservation principles remain unchanged. Explain the relationship in your own words before quoting its symbols. If you cannot distinguish a property from a path function, or theoretical limit from verified behavior, revisit the model formulation rather than memorizing the numerical answer.


---

# Unit 5, Lesson 3 — Reversible cycles and Carnot efficiency

**Learning goals.** Explain the physical meaning of the stated relationship; use the example to reconstruct a verifiable answer; identify at least two model limitations; and propose an independent check.

## 1. Physical question and conceptual model

A reversible engine between fixed hot and cold thermal reservoirs defines the largest possible efficiency for any cyclic engine between those temperatures. It is a mathematical comparison standard; practical machines must transfer heat at finite rates, which typically needs finite temperature differences and destroys reversibility.


**Professional use.** Determine whether a reported machine efficiency exceeds the reversible upper bound. Avoid jumping from a property value to a performance guarantee: the former describes an assumed state, and the latter depends on losses, materials, reliability and operating limits.

## 2. Build the mathematical relationship

**Governing statement:** `η_C=1−T_C/T_H`.


**Model qualification.** The equation is meaningful only when its state and process assumptions are satisfied. Some equations are conservation balances that remain exact for their declared boundary; others are constitutive approximations, such as an ideal-gas relation, a constant heat capacity or an isentropic reference process. Determine which category this statement belongs to. Explain whether extra phenomena such as a moving boundary, leakage, heat loss, multiphase conditions, kinetic energy, electrical work or chemical reaction would add terms or require a different property source. If the process is transient, ask whether an accumulation term is missing.

## 3. Worked teaching example

For T_H=600 K and T_C=300 K, Carnot efficiency is 50%.


**Interpretive check.** Does the result increase or decrease when the principal driving condition becomes stronger? Does the prediction approach a sensible limit when the temperature difference, flow rate, state change or relevant force approaches zero? Such limiting tests are not substitutes for a measurement, but they are effective at rejecting a broken model before the expensive stage of building apparatus or selecting equipment.

## 4. Failure analysis and engineering judgement

**A tempting but incorrect shortcut:** Inserting degrees Celsius directly, which can produce nonsensical ratios.

Investigate what this shortcut assumes about the device or material. Predict whether it would overstate useful work, misstate the phase, hide a heat leak or suppress a needed transport term. Estimate the direction of the bias before estimating its size. A numerical calculation that conserves energy can still violate the second law; similarly, a temperature prediction can be inconsistent with phase equilibrium. Test both conservation and state feasibility. Where the model is an ideal upper or lower bound, identify which side of the bound a real machine should occupy under comparable conditions.

**Engineering context.** Determine whether a reported machine efficiency exceeds the reversible upper bound. A useful report would specify the relevant operating range, which properties are tabulated or calculated, and which assumptions are supported by evidence. It would not claim that an attractive textbook efficiency, coefficient of performance or output power proves achievable production performance.

## 5. Verification and measurement protocol

Design a simple check of **reversible cycles and carnot efficiency**. Specify a control volume or control mass, boundary conditions, primary observations and sampling interval. Report whether the observation is direct (temperature, mass, voltage, volumetric flow), indirectly inferred (enthalpy, dryness fraction, exergy), or fitted from an empirical relation. Distinguish repeatability from model validity: a repeatable sensor can be wrongly calibrated, and a perfectly reproducible computer program can implement the wrong equation. Identify one test in which the idealization should perform reasonably, and a second test where a named assumption may break down. If you use fluid property tables or software, record its provenance, units, reference state and interpolation method.


## 6. Questions and answer criteria

**Exercise A — Reconstruct.** Reproduce the stated worked example with symbols, units and at least one limiting check. *Answer criterion:* obtain the stated value within rounding and explain each term in `η_C=1−T_C/T_H`.

**Exercise B — Predict.** Select one physically independent input, change it by 10%, and predict the response before calculation. *Answer criterion:* state whether a linear, reciprocal, logarithmic or state-dependent relationship is being used, and explain why it is valid over the selected interval.

**Exercise C — Diagnose.** Evaluate this proposed shortcut: "Inserting degrees Celsius directly, which can produce nonsensical ratios." *Answer criterion:* identify the missing assumption, specify a condition where the shortcut fails, and propose one measurement or alternate model that would expose the error.

## 7. Extended case and reproducible handover

Return to the **industrial waste-heat engine** case that motivates this unit. The proposal must respect a reversible ceiling before return-on-investment claims. Use this lesson's principle to create a two-column comparison between a minimal classroom calculation and a safer engineering estimate. The classroom side should contain only quantities supported by the basic model; the engineering side should add heat exchanger approach, cooling-water temperature and auxiliary pumping. For each added quantity, say whether it is known, must be measured, can be estimated from trustworthy property data, or is impossible to infer from the current information. Where a value is unknown, retain a symbol or range instead of fabricating a precise number.


## 8. Closing self-test

Without viewing your notes, explain why the same physical device can be modeled with different boundaries, which quantities change accordingly and which conservation principles remain unchanged. Explain the relationship in your own words before quoting its symbols. If you cannot distinguish a property from a path function, or theoretical limit from verified behavior, revisit the model formulation rather than memorizing the numerical answer.


---

# Unit 5, Lesson 4 — Refrigerators and heat pumps

**Learning goals.** Explain the physical meaning of the stated relationship; use the example to reconstruct a verifiable answer; identify at least two model limitations; and propose an independent check.

## 1. Physical question and conceptual model

A refrigerator uses work to extract Q_L from a cold space. A heat pump uses work to deliver Q_H to a warm space; the same reversed device can be described from either viewpoint. COP_R=Q_L/W and COP_HP=Q_H/W, so for the same idealized energy flows COP_HP=COP_R+1.


**Professional use.** Track electrical demand, cycling losses and finite-temperature heat exchanger approaches. Avoid jumping from a property value to a performance guarantee: the former describes an assumed state, and the latter depends on losses, materials, reliability and operating limits.

## 2. Build the mathematical relationship

**Governing statement:** `COP_R=Q_L/W, COP_HP=Q_H/W`.


**Model qualification.** The equation is meaningful only when its state and process assumptions are satisfied. Some equations are conservation balances that remain exact for their declared boundary; others are constitutive approximations, such as an ideal-gas relation, a constant heat capacity or an isentropic reference process. Determine which category this statement belongs to. Explain whether extra phenomena such as a moving boundary, leakage, heat loss, multiphase conditions, kinetic energy, electrical work or chemical reaction would add terms or require a different property source. If the process is transient, ask whether an accumulation term is missing.

## 3. Worked teaching example

A refrigerator removing 8 kJ while using 2 kJ of work has COP_R=4 and COP_HP=5 if condenser heat is useful.


**Interpretive check.** Does the result increase or decrease when the principal driving condition becomes stronger? Does the prediction approach a sensible limit when the temperature difference, flow rate, state change or relevant force approaches zero? Such limiting tests are not substitutes for a measurement, but they are effective at rejecting a broken model before the expensive stage of building apparatus or selecting equipment.

## 4. Failure analysis and engineering judgement

**A tempting but incorrect shortcut:** Calling a COP greater than one a perpetual motion machine; COP is not an energy-conversion efficiency.

Investigate what this shortcut assumes about the device or material. Predict whether it would overstate useful work, misstate the phase, hide a heat leak or suppress a needed transport term. Estimate the direction of the bias before estimating its size. A numerical calculation that conserves energy can still violate the second law; similarly, a temperature prediction can be inconsistent with phase equilibrium. Test both conservation and state feasibility. Where the model is an ideal upper or lower bound, identify which side of the bound a real machine should occupy under comparable conditions.

**Engineering context.** Track electrical demand, cycling losses and finite-temperature heat exchanger approaches. A useful report would specify the relevant operating range, which properties are tabulated or calculated, and which assumptions are supported by evidence. It would not claim that an attractive textbook efficiency, coefficient of performance or output power proves achievable production performance.

## 5. Verification and measurement protocol

Design a simple check of **refrigerators and heat pumps**. Specify a control volume or control mass, boundary conditions, primary observations and sampling interval. Report whether the observation is direct (temperature, mass, voltage, volumetric flow), indirectly inferred (enthalpy, dryness fraction, exergy), or fitted from an empirical relation. Distinguish repeatability from model validity: a repeatable sensor can be wrongly calibrated, and a perfectly reproducible computer program can implement the wrong equation. Identify one test in which the idealization should perform reasonably, and a second test where a named assumption may break down. If you use fluid property tables or software, record its provenance, units, reference state and interpolation method.


## 6. Questions and answer criteria

**Exercise A — Reconstruct.** Reproduce the stated worked example with symbols, units and at least one limiting check. *Answer criterion:* obtain the stated value within rounding and explain each term in `COP_R=Q_L/W, COP_HP=Q_H/W`.

**Exercise B — Predict.** Select one physically independent input, change it by 10%, and predict the response before calculation. *Answer criterion:* state whether a linear, reciprocal, logarithmic or state-dependent relationship is being used, and explain why it is valid over the selected interval.

**Exercise C — Diagnose.** Evaluate this proposed shortcut: "Calling a COP greater than one a perpetual motion machine; COP is not an energy-conversion efficiency." *Answer criterion:* identify the missing assumption, specify a condition where the shortcut fails, and propose one measurement or alternate model that would expose the error.

## 7. Extended case and reproducible handover

Return to the **industrial waste-heat engine** case that motivates this unit. The proposal must respect a reversible ceiling before return-on-investment claims. Use this lesson's principle to create a two-column comparison between a minimal classroom calculation and a safer engineering estimate. The classroom side should contain only quantities supported by the basic model; the engineering side should add heat exchanger approach, cooling-water temperature and auxiliary pumping. For each added quantity, say whether it is known, must be measured, can be estimated from trustworthy property data, or is impossible to infer from the current information. Where a value is unknown, retain a symbol or range instead of fabricating a precise number.


## 8. Closing self-test

Without viewing your notes, explain why the same physical device can be modeled with different boundaries, which quantities change accordingly and which conservation principles remain unchanged. Explain the relationship in your own words before quoting its symbols. If you cannot distinguish a property from a path function, or theoretical limit from verified behavior, revisit the model formulation rather than memorizing the numerical answer.


---

# Unit 5, Lesson 5 — Thermal irreversibility and finite driving forces

**Learning goals.** Explain the physical meaning of the stated relationship; use the example to reconstruct a verifiable answer; identify at least two model limitations; and propose an independent check.

## 1. Physical question and conceptual model

Heat transfer across a finite temperature difference produces entropy; more work could in principle be recovered if the exchange were made less irreversible. Friction dissipates organized mechanical motion. Mixing and free expansion are further sources of irreversibility. The second law states that total entropy generation is nonnegative for an actual process.


**Professional use.** Estimate lost work as a consequence of generation under a specified ambient temperature. Avoid jumping from a property value to a performance guarantee: the former describes an assumed state, and the latter depends on losses, materials, reliability and operating limits.

## 2. Build the mathematical relationship

**Governing statement:** `S_gen=Q(1/T_C−1/T_H) for heat Q from T_H to T_C`.


**Model qualification.** The equation is meaningful only when its state and process assumptions are satisfied. Some equations are conservation balances that remain exact for their declared boundary; others are constitutive approximations, such as an ideal-gas relation, a constant heat capacity or an isentropic reference process. Determine which category this statement belongs to. Explain whether extra phenomena such as a moving boundary, leakage, heat loss, multiphase conditions, kinetic energy, electrical work or chemical reaction would add terms or require a different property source. If the process is transient, ask whether an accumulation term is missing.

## 3. Worked teaching example

Transferring 100 kJ from 500 K to 300 K generates about 0.1333 kJ/K in the combined two-reservoir system.


**Interpretive check.** Does the result increase or decrease when the principal driving condition becomes stronger? Does the prediction approach a sensible limit when the temperature difference, flow rate, state change or relevant force approaches zero? Such limiting tests are not substitutes for a measurement, but they are effective at rejecting a broken model before the expensive stage of building apparatus or selecting equipment.

## 4. Failure analysis and engineering judgement

**A tempting but incorrect shortcut:** Calculating Q/T using Celsius temperatures or counting boundary entropy transfer as generated entropy.

Investigate what this shortcut assumes about the device or material. Predict whether it would overstate useful work, misstate the phase, hide a heat leak or suppress a needed transport term. Estimate the direction of the bias before estimating its size. A numerical calculation that conserves energy can still violate the second law; similarly, a temperature prediction can be inconsistent with phase equilibrium. Test both conservation and state feasibility. Where the model is an ideal upper or lower bound, identify which side of the bound a real machine should occupy under comparable conditions.

**Engineering context.** Estimate lost work as a consequence of generation under a specified ambient temperature. A useful report would specify the relevant operating range, which properties are tabulated or calculated, and which assumptions are supported by evidence. It would not claim that an attractive textbook efficiency, coefficient of performance or output power proves achievable production performance.

## 5. Verification and measurement protocol

Design a simple check of **thermal irreversibility and finite driving forces**. Specify a control volume or control mass, boundary conditions, primary observations and sampling interval. Report whether the observation is direct (temperature, mass, voltage, volumetric flow), indirectly inferred (enthalpy, dryness fraction, exergy), or fitted from an empirical relation. Distinguish repeatability from model validity: a repeatable sensor can be wrongly calibrated, and a perfectly reproducible computer program can implement the wrong equation. Identify one test in which the idealization should perform reasonably, and a second test where a named assumption may break down. If you use fluid property tables or software, record its provenance, units, reference state and interpolation method.


## 6. Questions and answer criteria

**Exercise A — Reconstruct.** Reproduce the stated worked example with symbols, units and at least one limiting check. *Answer criterion:* obtain the stated value within rounding and explain each term in `S_gen=Q(1/T_C−1/T_H) for heat Q from T_H to T_C`.

**Exercise B — Predict.** Select one physically independent input, change it by 10%, and predict the response before calculation. *Answer criterion:* state whether a linear, reciprocal, logarithmic or state-dependent relationship is being used, and explain why it is valid over the selected interval.

**Exercise C — Diagnose.** Evaluate this proposed shortcut: "Calculating Q/T using Celsius temperatures or counting boundary entropy transfer as generated entropy." *Answer criterion:* identify the missing assumption, specify a condition where the shortcut fails, and propose one measurement or alternate model that would expose the error.

## 7. Extended case and reproducible handover

Return to the **industrial waste-heat engine** case that motivates this unit. The proposal must respect a reversible ceiling before return-on-investment claims. Use this lesson's principle to create a two-column comparison between a minimal classroom calculation and a safer engineering estimate. The classroom side should contain only quantities supported by the basic model; the engineering side should add heat exchanger approach, cooling-water temperature and auxiliary pumping. For each added quantity, say whether it is known, must be measured, can be estimated from trustworthy property data, or is impossible to infer from the current information. Where a value is unknown, retain a symbol or range instead of fabricating a precise number.


## 8. Closing self-test

Without viewing your notes, explain why the same physical device can be modeled with different boundaries, which quantities change accordingly and which conservation principles remain unchanged. Explain the relationship in your own words before quoting its symbols. If you cannot distinguish a property from a path function, or theoretical limit from verified behavior, revisit the model formulation rather than memorizing the numerical answer.


---

