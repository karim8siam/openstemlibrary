# Unit 1: Thermodynamic Systems, Properties, and State Postulate

# Unit 1, Lesson 1 — System boundaries and control masses

**Learning goals.** Explain the physical meaning of the stated relationship; use the example to reconstruct a verifiable answer; identify at least two model limitations; and propose an independent check.

## 1. Physical question and conceptual model

A closed system exchanges energy across its boundary but not mass. Boundaries may move, deform or transfer heat; choosing them clarifies the work term and the appropriate energy balance. A control volume is generally preferred for compressors, nozzles and turbines where inlet and exit mass flows are observable.


**Professional use.** Use a process sketch showing the physical system, dashed mass-flow arrows and solid heat/work arrows. Avoid jumping from a property value to a performance guarantee: the former describes an assumed state, and the latter depends on losses, materials, reliability and operating limits.

## 2. Build the mathematical relationship

**Governing statement:** `ΔU + ΔKE + ΔPE = Q − W (closed system)`.


**Model qualification.** The equation is meaningful only when its state and process assumptions are satisfied. Some equations are conservation balances that remain exact for their declared boundary; others are constitutive approximations, such as an ideal-gas relation, a constant heat capacity or an isentropic reference process. Determine which category this statement belongs to. Explain whether extra phenomena such as a moving boundary, leakage, heat loss, multiphase conditions, kinetic energy, electrical work or chemical reaction would add terms or require a different property source. If the process is transient, ask whether an accumulation term is missing.

## 3. Worked teaching example

A sealed rigid tank receives 45 kJ of heat and performs no work; with negligible kinetic and potential energy change, ΔU = +45 kJ.


**Interpretive check.** Does the result increase or decrease when the principal driving condition becomes stronger? Does the prediction approach a sensible limit when the temperature difference, flow rate, state change or relevant force approaches zero? Such limiting tests are not substitutes for a measurement, but they are effective at rejecting a broken model before the expensive stage of building apparatus or selecting equipment.

## 4. Failure analysis and engineering judgement

**A tempting but incorrect shortcut:** Calling the tank open merely because a heater wire penetrates its enclosure; leakage, not electric connection, decides whether mass crosses.

Investigate what this shortcut assumes about the device or material. Predict whether it would overstate useful work, misstate the phase, hide a heat leak or suppress a needed transport term. Estimate the direction of the bias before estimating its size. A numerical calculation that conserves energy can still violate the second law; similarly, a temperature prediction can be inconsistent with phase equilibrium. Test both conservation and state feasibility. Where the model is an ideal upper or lower bound, identify which side of the bound a real machine should occupy under comparable conditions.

**Engineering context.** Use a process sketch showing the physical system, dashed mass-flow arrows and solid heat/work arrows. A useful report would specify the relevant operating range, which properties are tabulated or calculated, and which assumptions are supported by evidence. It would not claim that an attractive textbook efficiency, coefficient of performance or output power proves achievable production performance.

## 5. Verification and measurement protocol

Design a simple check of **system boundaries and control masses**. Specify a control volume or control mass, boundary conditions, primary observations and sampling interval. Report whether the observation is direct (temperature, mass, voltage, volumetric flow), indirectly inferred (enthalpy, dryness fraction, exergy), or fitted from an empirical relation. Distinguish repeatability from model validity: a repeatable sensor can be wrongly calibrated, and a perfectly reproducible computer program can implement the wrong equation. Identify one test in which the idealization should perform reasonably, and a second test where a named assumption may break down. If you use fluid property tables or software, record its provenance, units, reference state and interpolation method.


## 6. Questions and answer criteria

**Exercise A — Reconstruct.** Reproduce the stated worked example with symbols, units and at least one limiting check. *Answer criterion:* obtain the stated value within rounding and explain each term in `ΔU + ΔKE + ΔPE = Q − W (closed system)`.

**Exercise B — Predict.** Select one physically independent input, change it by 10%, and predict the response before calculation. *Answer criterion:* state whether a linear, reciprocal, logarithmic or state-dependent relationship is being used, and explain why it is valid over the selected interval.

**Exercise C — Diagnose.** Evaluate this proposed shortcut: "Calling the tank open merely because a heater wire penetrates its enclosure; leakage, not electric connection, decides whether mass crosses." *Answer criterion:* identify the missing assumption, specify a condition where the shortcut fails, and propose one measurement or alternate model that would expose the error.

## 7. Extended case and reproducible handover

Return to the **sealed electrical test cell** case that motivates this unit. The safety question is whether pressure may rise beyond vessel rating during controlled heating. Use this lesson's principle to create a two-column comparison between a minimal classroom calculation and a safer engineering estimate. The classroom side should contain only quantities supported by the basic model; the engineering side should add sensor placement, thermal uniformity, pressure reference and electrical power calibration. For each added quantity, say whether it is known, must be measured, can be estimated from trustworthy property data, or is impossible to infer from the current information. Where a value is unknown, retain a symbol or range instead of fabricating a precise number.


## 8. Closing self-test

Without viewing your notes, explain why the same physical device can be modeled with different boundaries, which quantities change accordingly and which conservation principles remain unchanged. Explain the relationship in your own words before quoting its symbols. If you cannot distinguish a property from a path function, or theoretical limit from verified behavior, revisit the model formulation rather than memorizing the numerical answer.


---

# Unit 1, Lesson 2 — Properties, path functions, and intensive variables

**Learning goals.** Explain the physical meaning of the stated relationship; use the example to reconstruct a verifiable answer; identify at least two model limitations; and propose an independent check.

## 1. Physical question and conceptual model

Mass, volume and internal energy are extensive. Pressure, temperature and specific internal energy are intensive under the usual equilibrium description. A differential change of state is path independent, while a heat-transfer integral must specify the path. Ratios such as specific volume v=V/m make comparisons across system sizes possible.


**Professional use.** Separate measured pressure, temperature and mass from inferred energy and phase information. Avoid jumping from a property value to a performance guarantee: the former describes an assumed state, and the latter depends on losses, materials, reliability and operating limits.

## 2. Build the mathematical relationship

**Governing statement:** `v=V/m, ρ=m/V=1/v`.


**Model qualification.** The equation is meaningful only when its state and process assumptions are satisfied. Some equations are conservation balances that remain exact for their declared boundary; others are constitutive approximations, such as an ideal-gas relation, a constant heat capacity or an isentropic reference process. Determine which category this statement belongs to. Explain whether extra phenomena such as a moving boundary, leakage, heat loss, multiphase conditions, kinetic energy, electrical work or chemical reaction would add terms or require a different property source. If the process is transient, ask whether an accumulation term is missing.

## 3. Worked teaching example

A 2.0 kg sample occupying 0.50 m³ has specific volume 0.25 m³/kg and density 4.0 kg/m³.


**Interpretive check.** Does the result increase or decrease when the principal driving condition becomes stronger? Does the prediction approach a sensible limit when the temperature difference, flow rate, state change or relevant force approaches zero? Such limiting tests are not substitutes for a measurement, but they are effective at rejecting a broken model before the expensive stage of building apparatus or selecting equipment.

## 4. Failure analysis and engineering judgement

**A tempting but incorrect shortcut:** Treating heat supplied as though it were an intrinsic property listed in a thermodynamic table.

Investigate what this shortcut assumes about the device or material. Predict whether it would overstate useful work, misstate the phase, hide a heat leak or suppress a needed transport term. Estimate the direction of the bias before estimating its size. A numerical calculation that conserves energy can still violate the second law; similarly, a temperature prediction can be inconsistent with phase equilibrium. Test both conservation and state feasibility. Where the model is an ideal upper or lower bound, identify which side of the bound a real machine should occupy under comparable conditions.

**Engineering context.** Separate measured pressure, temperature and mass from inferred energy and phase information. A useful report would specify the relevant operating range, which properties are tabulated or calculated, and which assumptions are supported by evidence. It would not claim that an attractive textbook efficiency, coefficient of performance or output power proves achievable production performance.

## 5. Verification and measurement protocol

Design a simple check of **properties, path functions, and intensive variables**. Specify a control volume or control mass, boundary conditions, primary observations and sampling interval. Report whether the observation is direct (temperature, mass, voltage, volumetric flow), indirectly inferred (enthalpy, dryness fraction, exergy), or fitted from an empirical relation. Distinguish repeatability from model validity: a repeatable sensor can be wrongly calibrated, and a perfectly reproducible computer program can implement the wrong equation. Identify one test in which the idealization should perform reasonably, and a second test where a named assumption may break down. If you use fluid property tables or software, record its provenance, units, reference state and interpolation method.


## 6. Questions and answer criteria

**Exercise A — Reconstruct.** Reproduce the stated worked example with symbols, units and at least one limiting check. *Answer criterion:* obtain the stated value within rounding and explain each term in `v=V/m, ρ=m/V=1/v`.

**Exercise B — Predict.** Select one physically independent input, change it by 10%, and predict the response before calculation. *Answer criterion:* state whether a linear, reciprocal, logarithmic or state-dependent relationship is being used, and explain why it is valid over the selected interval.

**Exercise C — Diagnose.** Evaluate this proposed shortcut: "Treating heat supplied as though it were an intrinsic property listed in a thermodynamic table." *Answer criterion:* identify the missing assumption, specify a condition where the shortcut fails, and propose one measurement or alternate model that would expose the error.

## 7. Extended case and reproducible handover

Return to the **sealed electrical test cell** case that motivates this unit. The safety question is whether pressure may rise beyond vessel rating during controlled heating. Use this lesson's principle to create a two-column comparison between a minimal classroom calculation and a safer engineering estimate. The classroom side should contain only quantities supported by the basic model; the engineering side should add sensor placement, thermal uniformity, pressure reference and electrical power calibration. For each added quantity, say whether it is known, must be measured, can be estimated from trustworthy property data, or is impossible to infer from the current information. Where a value is unknown, retain a symbol or range instead of fabricating a precise number.


## 8. Closing self-test

Without viewing your notes, explain why the same physical device can be modeled with different boundaries, which quantities change accordingly and which conservation principles remain unchanged. Explain the relationship in your own words before quoting its symbols. If you cannot distinguish a property from a path function, or theoretical limit from verified behavior, revisit the model formulation rather than memorizing the numerical answer.


---

# Unit 1, Lesson 3 — Equilibrium, reversible approximations, and processes

**Learning goals.** Explain the physical meaning of the stated relationship; use the example to reconstruct a verifiable answer; identify at least two model limitations; and propose an independent check.

## 1. Physical question and conceptual model

Thermal, mechanical and phase equilibrium are conceptually distinct. A path consisting of equilibrium states is a quasistatic idealization; it need not be reversible if sliding friction, finite thermal gradients or electrical resistance generate entropy. Reversibility is a stronger criterion that permits both system and surroundings to return to their initial states.


**Professional use.** Identify friction, temperature differences and free expansion as tests of reversibility. Avoid jumping from a property value to a performance guarantee: the former describes an assumed state, and the latter depends on losses, materials, reliability and operating limits.

## 2. Build the mathematical relationship

**Governing statement:** `δW_b=p_ext dV; for quasistatic simple-compressible systems δW_b=p dV`.


**Model qualification.** The equation is meaningful only when its state and process assumptions are satisfied. Some equations are conservation balances that remain exact for their declared boundary; others are constitutive approximations, such as an ideal-gas relation, a constant heat capacity or an isentropic reference process. Determine which category this statement belongs to. Explain whether extra phenomena such as a moving boundary, leakage, heat loss, multiphase conditions, kinetic energy, electrical work or chemical reaction would add terms or require a different property source. If the process is transient, ask whether an accumulation term is missing.

## 3. Worked teaching example

An expansion under constant external pressure of 150 kPa through 0.020 m³ produces 3.0 kJ of boundary work.


**Interpretive check.** Does the result increase or decrease when the principal driving condition becomes stronger? Does the prediction approach a sensible limit when the temperature difference, flow rate, state change or relevant force approaches zero? Such limiting tests are not substitutes for a measurement, but they are effective at rejecting a broken model before the expensive stage of building apparatus or selecting equipment.

## 4. Failure analysis and engineering judgement

**A tempting but incorrect shortcut:** Using the gas pressure in p dV when an actual fast expansion is strongly nonuniform.

Investigate what this shortcut assumes about the device or material. Predict whether it would overstate useful work, misstate the phase, hide a heat leak or suppress a needed transport term. Estimate the direction of the bias before estimating its size. A numerical calculation that conserves energy can still violate the second law; similarly, a temperature prediction can be inconsistent with phase equilibrium. Test both conservation and state feasibility. Where the model is an ideal upper or lower bound, identify which side of the bound a real machine should occupy under comparable conditions.

**Engineering context.** Identify friction, temperature differences and free expansion as tests of reversibility. A useful report would specify the relevant operating range, which properties are tabulated or calculated, and which assumptions are supported by evidence. It would not claim that an attractive textbook efficiency, coefficient of performance or output power proves achievable production performance.

## 5. Verification and measurement protocol

Design a simple check of **equilibrium, reversible approximations, and processes**. Specify a control volume or control mass, boundary conditions, primary observations and sampling interval. Report whether the observation is direct (temperature, mass, voltage, volumetric flow), indirectly inferred (enthalpy, dryness fraction, exergy), or fitted from an empirical relation. Distinguish repeatability from model validity: a repeatable sensor can be wrongly calibrated, and a perfectly reproducible computer program can implement the wrong equation. Identify one test in which the idealization should perform reasonably, and a second test where a named assumption may break down. If you use fluid property tables or software, record its provenance, units, reference state and interpolation method.


## 6. Questions and answer criteria

**Exercise A — Reconstruct.** Reproduce the stated worked example with symbols, units and at least one limiting check. *Answer criterion:* obtain the stated value within rounding and explain each term in `δW_b=p_ext dV; for quasistatic simple-compressible systems δW_b=p dV`.

**Exercise B — Predict.** Select one physically independent input, change it by 10%, and predict the response before calculation. *Answer criterion:* state whether a linear, reciprocal, logarithmic or state-dependent relationship is being used, and explain why it is valid over the selected interval.

**Exercise C — Diagnose.** Evaluate this proposed shortcut: "Using the gas pressure in p dV when an actual fast expansion is strongly nonuniform." *Answer criterion:* identify the missing assumption, specify a condition where the shortcut fails, and propose one measurement or alternate model that would expose the error.

## 7. Extended case and reproducible handover

Return to the **sealed electrical test cell** case that motivates this unit. The safety question is whether pressure may rise beyond vessel rating during controlled heating. Use this lesson's principle to create a two-column comparison between a minimal classroom calculation and a safer engineering estimate. The classroom side should contain only quantities supported by the basic model; the engineering side should add sensor placement, thermal uniformity, pressure reference and electrical power calibration. For each added quantity, say whether it is known, must be measured, can be estimated from trustworthy property data, or is impossible to infer from the current information. Where a value is unknown, retain a symbol or range instead of fabricating a precise number.


## 8. Closing self-test

Without viewing your notes, explain why the same physical device can be modeled with different boundaries, which quantities change accordingly and which conservation principles remain unchanged. Explain the relationship in your own words before quoting its symbols. If you cannot distinguish a property from a path function, or theoretical limit from verified behavior, revisit the model formulation rather than memorizing the numerical answer.


---

# Unit 1, Lesson 4 — Temperature scales and the zeroth law

**Learning goals.** Explain the physical meaning of the stated relationship; use the example to reconstruct a verifiable answer; identify at least two model limitations; and propose an independent check.

## 1. Physical question and conceptual model

Two bodies separately in thermal equilibrium with a third are in thermal equilibrium with each other. This operational zeroth-law statement makes temperature calibration possible. Celsius differences and kelvin differences have equal magnitude, but temperature ratios demand absolute temperature. A sensor usually reads locally, so mounting location and response time matter.


**Professional use.** Document instrument calibration points, immersion depth and time lag when reporting temperature. Avoid jumping from a property value to a performance guarantee: the former describes an assumed state, and the latter depends on losses, materials, reliability and operating limits.

## 2. Build the mathematical relationship

**Governing statement:** `T[K]=t[°C]+273.15`.


**Model qualification.** The equation is meaningful only when its state and process assumptions are satisfied. Some equations are conservation balances that remain exact for their declared boundary; others are constitutive approximations, such as an ideal-gas relation, a constant heat capacity or an isentropic reference process. Determine which category this statement belongs to. Explain whether extra phenomena such as a moving boundary, leakage, heat loss, multiphase conditions, kinetic energy, electrical work or chemical reaction would add terms or require a different property source. If the process is transient, ask whether an accumulation term is missing.

## 3. Worked teaching example

A sensor at 26.85 °C indicates 300.00 K; doubling 26.85 °C is not doubling thermodynamic temperature.


**Interpretive check.** Does the result increase or decrease when the principal driving condition becomes stronger? Does the prediction approach a sensible limit when the temperature difference, flow rate, state change or relevant force approaches zero? Such limiting tests are not substitutes for a measurement, but they are effective at rejecting a broken model before the expensive stage of building apparatus or selecting equipment.

## 4. Failure analysis and engineering judgement

**A tempting but incorrect shortcut:** Substituting Celsius temperature into a gas-law ratio or Carnot efficiency.

Investigate what this shortcut assumes about the device or material. Predict whether it would overstate useful work, misstate the phase, hide a heat leak or suppress a needed transport term. Estimate the direction of the bias before estimating its size. A numerical calculation that conserves energy can still violate the second law; similarly, a temperature prediction can be inconsistent with phase equilibrium. Test both conservation and state feasibility. Where the model is an ideal upper or lower bound, identify which side of the bound a real machine should occupy under comparable conditions.

**Engineering context.** Document instrument calibration points, immersion depth and time lag when reporting temperature. A useful report would specify the relevant operating range, which properties are tabulated or calculated, and which assumptions are supported by evidence. It would not claim that an attractive textbook efficiency, coefficient of performance or output power proves achievable production performance.

## 5. Verification and measurement protocol

Design a simple check of **temperature scales and the zeroth law**. Specify a control volume or control mass, boundary conditions, primary observations and sampling interval. Report whether the observation is direct (temperature, mass, voltage, volumetric flow), indirectly inferred (enthalpy, dryness fraction, exergy), or fitted from an empirical relation. Distinguish repeatability from model validity: a repeatable sensor can be wrongly calibrated, and a perfectly reproducible computer program can implement the wrong equation. Identify one test in which the idealization should perform reasonably, and a second test where a named assumption may break down. If you use fluid property tables or software, record its provenance, units, reference state and interpolation method.


## 6. Questions and answer criteria

**Exercise A — Reconstruct.** Reproduce the stated worked example with symbols, units and at least one limiting check. *Answer criterion:* obtain the stated value within rounding and explain each term in `T[K]=t[°C]+273.15`.

**Exercise B — Predict.** Select one physically independent input, change it by 10%, and predict the response before calculation. *Answer criterion:* state whether a linear, reciprocal, logarithmic or state-dependent relationship is being used, and explain why it is valid over the selected interval.

**Exercise C — Diagnose.** Evaluate this proposed shortcut: "Substituting Celsius temperature into a gas-law ratio or Carnot efficiency." *Answer criterion:* identify the missing assumption, specify a condition where the shortcut fails, and propose one measurement or alternate model that would expose the error.

## 7. Extended case and reproducible handover

Return to the **sealed electrical test cell** case that motivates this unit. The safety question is whether pressure may rise beyond vessel rating during controlled heating. Use this lesson's principle to create a two-column comparison between a minimal classroom calculation and a safer engineering estimate. The classroom side should contain only quantities supported by the basic model; the engineering side should add sensor placement, thermal uniformity, pressure reference and electrical power calibration. For each added quantity, say whether it is known, must be measured, can be estimated from trustworthy property data, or is impossible to infer from the current information. Where a value is unknown, retain a symbol or range instead of fabricating a precise number.


## 8. Closing self-test

Without viewing your notes, explain why the same physical device can be modeled with different boundaries, which quantities change accordingly and which conservation principles remain unchanged. Explain the relationship in your own words before quoting its symbols. If you cannot distinguish a property from a path function, or theoretical limit from verified behavior, revisit the model formulation rather than memorizing the numerical answer.


---

# Unit 1, Lesson 5 — Thermodynamic data, units and uncertainty

**Learning goals.** Explain the physical meaning of the stated relationship; use the example to reconstruct a verifiable answer; identify at least two model limitations; and propose an independent check.

## 1. Physical question and conceptual model

An exact-looking calculation cannot repair imprecise inputs. Atmospheric pressure, ambient temperature, mass flow and composition often dominate uncertainty. Use consistent significant figures; keep additional precision internally until the final report. Where a relation involves measured products and quotients, relative input uncertainty can be propagated to first order.


**Professional use.** Build an uncertainty budget naming instruments, assumed correlations and missing systematic errors. Avoid jumping from a property value to a performance guarantee: the former describes an assumed state, and the latter depends on losses, materials, reliability and operating limits.

## 2. Build the mathematical relationship

**Governing statement:** `For y=ab/c, (σ_y/y)²≈(σ_a/a)²+(σ_b/b)²+(σ_c/c)² (independent inputs)`.


**Model qualification.** The equation is meaningful only when its state and process assumptions are satisfied. Some equations are conservation balances that remain exact for their declared boundary; others are constitutive approximations, such as an ideal-gas relation, a constant heat capacity or an isentropic reference process. Determine which category this statement belongs to. Explain whether extra phenomena such as a moving boundary, leakage, heat loss, multiphase conditions, kinetic energy, electrical work or chemical reaction would add terms or require a different property source. If the process is transient, ask whether an accumulation term is missing.

## 3. Worked teaching example

With a 2% flow-rate uncertainty and 1% enthalpy-difference uncertainty, power uncertainty is approximately √5% = 2.24%.


**Interpretive check.** Does the result increase or decrease when the principal driving condition becomes stronger? Does the prediction approach a sensible limit when the temperature difference, flow rate, state change or relevant force approaches zero? Such limiting tests are not substitutes for a measurement, but they are effective at rejecting a broken model before the expensive stage of building apparatus or selecting equipment.

## 4. Failure analysis and engineering judgement

**A tempting but incorrect shortcut:** Presenting a model prediction to six decimals without considering sensor or property-table precision.

Investigate what this shortcut assumes about the device or material. Predict whether it would overstate useful work, misstate the phase, hide a heat leak or suppress a needed transport term. Estimate the direction of the bias before estimating its size. A numerical calculation that conserves energy can still violate the second law; similarly, a temperature prediction can be inconsistent with phase equilibrium. Test both conservation and state feasibility. Where the model is an ideal upper or lower bound, identify which side of the bound a real machine should occupy under comparable conditions.

**Engineering context.** Build an uncertainty budget naming instruments, assumed correlations and missing systematic errors. A useful report would specify the relevant operating range, which properties are tabulated or calculated, and which assumptions are supported by evidence. It would not claim that an attractive textbook efficiency, coefficient of performance or output power proves achievable production performance.

## 5. Verification and measurement protocol

Design a simple check of **thermodynamic data, units and uncertainty**. Specify a control volume or control mass, boundary conditions, primary observations and sampling interval. Report whether the observation is direct (temperature, mass, voltage, volumetric flow), indirectly inferred (enthalpy, dryness fraction, exergy), or fitted from an empirical relation. Distinguish repeatability from model validity: a repeatable sensor can be wrongly calibrated, and a perfectly reproducible computer program can implement the wrong equation. Identify one test in which the idealization should perform reasonably, and a second test where a named assumption may break down. If you use fluid property tables or software, record its provenance, units, reference state and interpolation method.


## 6. Questions and answer criteria

**Exercise A — Reconstruct.** Reproduce the stated worked example with symbols, units and at least one limiting check. *Answer criterion:* obtain the stated value within rounding and explain each term in `For y=ab/c, (σ_y/y)²≈(σ_a/a)²+(σ_b/b)²+(σ_c/c)² (independent inputs)`.

**Exercise B — Predict.** Select one physically independent input, change it by 10%, and predict the response before calculation. *Answer criterion:* state whether a linear, reciprocal, logarithmic or state-dependent relationship is being used, and explain why it is valid over the selected interval.

**Exercise C — Diagnose.** Evaluate this proposed shortcut: "Presenting a model prediction to six decimals without considering sensor or property-table precision." *Answer criterion:* identify the missing assumption, specify a condition where the shortcut fails, and propose one measurement or alternate model that would expose the error.

## 7. Extended case and reproducible handover

Return to the **sealed electrical test cell** case that motivates this unit. The safety question is whether pressure may rise beyond vessel rating during controlled heating. Use this lesson's principle to create a two-column comparison between a minimal classroom calculation and a safer engineering estimate. The classroom side should contain only quantities supported by the basic model; the engineering side should add sensor placement, thermal uniformity, pressure reference and electrical power calibration. For each added quantity, say whether it is known, must be measured, can be estimated from trustworthy property data, or is impossible to infer from the current information. Where a value is unknown, retain a symbol or range instead of fabricating a precise number.


## 8. Closing self-test

Without viewing your notes, explain why the same physical device can be modeled with different boundaries, which quantities change accordingly and which conservation principles remain unchanged. Explain the relationship in your own words before quoting its symbols. If you cannot distinguish a property from a path function, or theoretical limit from verified behavior, revisit the model formulation rather than memorizing the numerical answer.


---

