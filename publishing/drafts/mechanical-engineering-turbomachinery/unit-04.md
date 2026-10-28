# Unit 04: Centrifugal Compressors and Diffusers

**Course Code**: TBM 304 · **Level**: Advanced Undergraduate Engineering

## Unit Overview & Physical Foundations

This comprehensive university textbook unit covers the theoretical framework, physical modeling, mathematical governing equations, and engineering applications of **Centrifugal Compressors and Diffusers**.

## U04-L01 — Radial impeller energy rise

**Outcome.** Use conservation laws and appropriate reference stations to analyze **radial impeller energy rise**; solve a traceable numerical example; expose model limitations; and justify a provisional engineering choice. This is Unit 04, **Centrifugal Compressors and Diffusers**.

### 1. Physical setting and governing reasoning

An engineer should be able to explain the direction of power transfer before touching a calculator. In this lesson the system boundary encloses the relevant machine component; the chosen inlet and outlet stations are part of the model, not details added after computing a value. The shared design brief is: A process-air package contains an impeller, vaneless or vaned diffuser, return passages and seals; exit swirl and pressure recovery compete with mechanical limits. This particular lesson tests how radial impeller energy rise influences the balance among useful power, operating stability, mechanical limits and lifetime expense. The model applies only to its stated fluid and duty conditions.

**Physical mechanism:** Rotor curvature and finite blade number limit achievable exit swirl relative to ideal infinite-blade models. Mark the control-volume stations, flow direction, shaft boundary and whether the stated measurements use absolute or relative velocity, total or static state.

### 2. Model and derivation

**Core equation:** `Delta_h0=U2 Vtheta2 - U1 Vtheta1`.

The equation follows from the appropriate balance of energy, mass or angular momentum. Define the inlet, outlet and reference frame first; state whether an efficiency uses fluid, shaft or electric power and whether a pressure is static or total.

A radial impeller can impart high work because U increases with radius. Vaneless and vaned diffusers convert some discharge kinetic energy to static pressure without adding shaft work. The ideal enthalpy rise does not determine recovered static pressure if diffuser separation and mixing losses are large.

Check dimensions: J/kg = m²/s², hydraulic head uses metres, efficiency is dimensionless, and torque times rad/s gives watts.

### 3. Worked example and sensitivity

**Teaching case:** At U2=300 m/s, Vtheta2=210 m/s and negligible inlet swirl, the ideal input is 63 kJ/kg.

**Explicit substitution:** Delta h0 =300×210−0; therefore **63,000 J/kg**. Inlet whirl was explicitly assumed negligible.

Check arithmetic independently. Then perturb one input by 10%: linear, quadratic and cubic factors become 1.1, 1.21 and 1.331, respectively. Recompute nonlinear property relationships. An algebraic change is not evidence of a new real-machine operating point.

### 4. Loss mechanisms, diagnostics and design limits

**Critical misconception:** Assuming Vtheta2=U2 for every backswept impeller overpredicts work. Consider off-design incidence, leakage, wakes and local mechanical or thermal limits; different machine types have distinct damage mechanisms.

**Test evidence:** Measure tip radius and speed and use a defensible slip correction supported by data. Record calibration and uncertainty, check the station definitions, and separate real losses from sensor or operating-point differences. Keep hydraulic or aerodynamic useful power separate from shaft power and electric input. It is possible for a component to improve while the entire installation consumes more electricity due to throttling, controls or auxiliary devices. Show each energy boundary and the associated loss.

**Provisional decision:** Trade impeller tip speed against material stress, temperature and diffusion demand. Revise this recommendation if an independently verified safety or stability constraint is violated.

### 5. Assessment (five tasks)

1. **Calculation:** Using `Delta_h0=U2 Vtheta2 - U1 Vtheta1`, reproduce **63,000 J/kg** and show every unit conversion. Explain why the chosen sign convention is necessary.
2. **Design variation:** Perturb the dominant flow, temperature, speed or head input by 10% and recompute. Which physical assumption fails first at a very different duty point?
3. **Failure investigation:** Use this misconception as the starting hypothesis: Assuming Vtheta2=U2 for every backswept impeller overpredicts work. Propose an alternative explanation and one observation that distinguishes the two.
4. **Measurement plan:** Operationalize this requirement: Measure tip radius and speed and use a defensible slip correction supported by data. State one calibration check, one expected systematic error and how results are normalized to the same operating state.
5. **Decision memo:** Evaluate the provisional change: Trade impeller tip speed against material stress, temperature and diffusion demand. Identify a constraint or observation that would force the opposite decision.

### 6. Worked-answer guidance

**1.** The substitution is **Delta h0 =300×210−0**, yielding **63,000 J/kg** under the stated simplifications. Inlet whirl was explicitly assumed negligible. A complete answer identifies pressure, temperature and rotor-frame conventions where relevant.

**2.** Apply the functional dependence of the displayed relation and calculate the changed case. State whether the perturbation preserves the real operating point; update thermodynamic properties if needed.

**3–4.** Rotor curvature and finite blade number limit achievable exit swirl relative to ideal infinite-blade models. Measure tip radius and speed and use a defensible slip correction supported by data. Link one cause to an independent measurement and report uncertainty.

**5.** Trade impeller tip speed against material stress, temperature and diffusion demand. It is provisional pending independent safety, structural and performance review.

**Status:** All values are invented classroom inputs; this chapter is not a measured field study, machine certification or safe operating procedure.


---

## U04-L02 — Slip factor and backswept blades

**Outcome.** Use conservation laws and appropriate reference stations to analyze **slip factor and backswept blades**; solve a traceable numerical example; expose model limitations; and justify a provisional engineering choice. This is Unit 04, **Centrifugal Compressors and Diffusers**.

### 1. Physical setting and governing reasoning

The first challenge is to connect the observed state to a physical balance. A pressure, velocity or temperature measurement alone is incomplete until the flow direction, station definition and performance quantity have been fixed. The shared design brief is: A process-air package contains an impeller, vaneless or vaned diffuser, return passages and seals; exit swirl and pressure recovery compete with mechanical limits. This particular lesson tests how slip factor and backswept blades influences the balance among useful power, operating stability, mechanical limits and lifetime expense. The model applies only to its stated fluid and duty conditions.

**Physical mechanism:** Finite blade number and nonuniform discharge generate deviation from ideal flow guidance. Mark the control-volume stations, flow direction, shaft boundary and whether the stated measurements use absolute or relative velocity, total or static state.

### 2. Model and derivation

**Core equation:** `sigma=Vtheta2_actual/Vtheta2_ideal for explicitly chosen reference`.

The equation follows from the appropriate balance of energy, mass or angular momentum. Define the inlet, outlet and reference frame first; state whether an efficiency uses fluid, shaft or electric power and whether a pressure is static or total.

Slip means the actual exit whirl differs from a perfectly guided idealization. Its definition and correlations depend on blade geometry, backsweep and test convention. Relative and absolute Mach numbers must be evaluated locally, particularly near the shroud and impeller throat.

Check dimensions: J/kg = m²/s², hydraulic head uses metres, efficiency is dimensionless, and torque times rad/s gives watts.

### 3. Worked example and sensitivity

**Teaching case:** If an ideal exit whirl is 235 m/s and measured or modeled whirl is 205 m/s, sigma≈0.872.

**Explicit substitution:** sigma =205/235; therefore **0.8723**. Defined slip factor depends on the specified ideal whirl reference.

Check arithmetic independently. Then perturb one input by 10%: linear, quadratic and cubic factors become 1.1, 1.21 and 1.331, respectively. Recompute nonlinear property relationships. An algebraic change is not evidence of a new real-machine operating point.

### 4. Loss mechanisms, diagnostics and design limits

**Critical misconception:** Reusing a slip correlation outside its geometry or Reynolds regime makes the estimate fragile. Consider off-design incidence, leakage, wakes and local mechanical or thermal limits; different machine types have distinct damage mechanisms.

**Test evidence:** Compare velocity measurements or validated CFD to the same definition of ideal exit whirl. Record calibration and uncertainty, check the station definitions, and separate real losses from sensor or operating-point differences. When comparing before-and-after tests, hold corrected flow or an equivalent meaningful operating state close enough that changing duty does not masquerade as better hardware. Temperature and gas composition influence corrected variables, while a hydraulic network may change substantially with valve setting. State the comparison tolerance rather than assuming curves can be overlaid without adjustment.

**Provisional decision:** Select blade backsweep and count based on combined efficiency and manufacturing constraints. Revise this recommendation if an independently verified safety or stability constraint is violated.

### 5. Assessment (five tasks)

1. **Calculation:** Using `sigma=Vtheta2_actual/Vtheta2_ideal for explicitly chosen reference`, reproduce **0.8723** and show every unit conversion. Explain why the chosen sign convention is necessary.
2. **Design variation:** Perturb the dominant flow, temperature, speed or head input by 10% and recompute. Which physical assumption fails first at a very different duty point?
3. **Failure investigation:** Use this misconception as the starting hypothesis: Reusing a slip correlation outside its geometry or Reynolds regime makes the estimate fragile. Propose an alternative explanation and one observation that distinguishes the two.
4. **Measurement plan:** Operationalize this requirement: Compare velocity measurements or validated CFD to the same definition of ideal exit whirl. State one calibration check, one expected systematic error and how results are normalized to the same operating state.
5. **Decision memo:** Evaluate the provisional change: Select blade backsweep and count based on combined efficiency and manufacturing constraints. Identify a constraint or observation that would force the opposite decision.

### 6. Worked-answer guidance

**1.** The substitution is **sigma =205/235**, yielding **0.8723** under the stated simplifications. Defined slip factor depends on the specified ideal whirl reference. A complete answer identifies pressure, temperature and rotor-frame conventions where relevant.

**2.** Apply the functional dependence of the displayed relation and calculate the changed case. State whether the perturbation preserves the real operating point; update thermodynamic properties if needed.

**3–4.** Finite blade number and nonuniform discharge generate deviation from ideal flow guidance. Compare velocity measurements or validated CFD to the same definition of ideal exit whirl. Link one cause to an independent measurement and report uncertainty.

**5.** Select blade backsweep and count based on combined efficiency and manufacturing constraints. It is provisional pending independent safety, structural and performance review.

**Status:** All values are invented classroom inputs; this chapter is not a measured field study, machine certification or safe operating procedure.


---

## U04-L03 — Diffuser velocity recovery

**Outcome.** Use conservation laws and appropriate reference stations to analyze **diffuser velocity recovery**; solve a traceable numerical example; expose model limitations; and justify a provisional engineering choice. This is Unit 04, **Centrifugal Compressors and Diffusers**.

### 1. Physical setting and governing reasoning

An apparently simple equipment decision becomes difficult when the operating envelope shifts. Work from conservation laws to a tractable approximation, and only then decide what constitutes evidence for the performance claim. The shared design brief is: A process-air package contains an impeller, vaneless or vaned diffuser, return passages and seals; exit swirl and pressure recovery compete with mechanical limits. This particular lesson tests how diffuser velocity recovery influences the balance among useful power, operating stability, mechanical limits and lifetime expense. The model applies only to its stated fluid and duty conditions.

**Physical mechanism:** Deceleration converts kinetic energy to pressure in an ideal diffuser; separation and compressibility reduce actual recovery. Mark the control-volume stations, flow direction, shaft boundary and whether the stated measurements use absolute or relative velocity, total or static state.

### 2. Model and derivation

**Core equation:** `Delta_p_ideal≈rho (V1^2-V2^2)/2 at constant density`.

The equation follows from the appropriate balance of energy, mass or angular momentum. Define the inlet, outlet and reference frame first; state whether an efficiency uses fluid, shaft or electric power and whether a pressure is static or total.

Compressor station conventions should be fixed in the design notebook. Total-inlet and total-outlet properties define a compressor total-to-total pressure ratio; using static exit readings from an unmatched station can imply an impossible improvement.

Check dimensions: J/kg = m²/s², hydraulic head uses metres, efficiency is dimensionless, and torque times rad/s gives watts.

### 3. Worked example and sensitivity

**Teaching case:** With rho=1.2 kg/m3, V1=160 m/s and V2=100 m/s, the ideal static recovery is 9.36 kPa.

**Explicit substitution:** Delta p≈(1.2/2)×(160²−100²); therefore **9360 Pa**. Valid only as a constant-density inviscid recovery idealization.

Check arithmetic independently. Then perturb one input by 10%: linear, quadratic and cubic factors become 1.1, 1.21 and 1.331, respectively. Recompute nonlinear property relationships. An algebraic change is not evidence of a new real-machine operating point.

### 4. Loss mechanisms, diagnostics and design limits

**Critical misconception:** Using the incompressible result for transonic gas flow can be badly inaccurate. Consider off-design incidence, leakage, wakes and local mechanical or thermal limits; different machine types have distinct damage mechanisms.

**Test evidence:** Use stagnation-pressure loss and wall-static pressure distributions to quantify recovery. Record calibration and uncertainty, check the station definitions, and separate real losses from sensor or operating-point differences. Estimate which measured inputs dominate the output by perturbing them individually. If a 1% sensor shift changes a design recommendation, the decision is not robust without calibration and repeat testing. Report the measurement chain and the test range, not only the final digits.

**Provisional decision:** Size diffuser area ratio subject to flow separation and machine packaging. Revise this recommendation if an independently verified safety or stability constraint is violated.

### 5. Assessment (five tasks)

1. **Calculation:** Using `Delta_p_ideal≈rho (V1^2-V2^2)/2 at constant density`, reproduce **9360 Pa** and show every unit conversion. Explain why the chosen sign convention is necessary.
2. **Design variation:** Perturb the dominant flow, temperature, speed or head input by 10% and recompute. Which physical assumption fails first at a very different duty point?
3. **Failure investigation:** Use this misconception as the starting hypothesis: Using the incompressible result for transonic gas flow can be badly inaccurate. Propose an alternative explanation and one observation that distinguishes the two.
4. **Measurement plan:** Operationalize this requirement: Use stagnation-pressure loss and wall-static pressure distributions to quantify recovery. State one calibration check, one expected systematic error and how results are normalized to the same operating state.
5. **Decision memo:** Evaluate the provisional change: Size diffuser area ratio subject to flow separation and machine packaging. Identify a constraint or observation that would force the opposite decision.

### 6. Worked-answer guidance

**1.** The substitution is **Delta p≈(1.2/2)×(160²−100²)**, yielding **9360 Pa** under the stated simplifications. Valid only as a constant-density inviscid recovery idealization. A complete answer identifies pressure, temperature and rotor-frame conventions where relevant.

**2.** Apply the functional dependence of the displayed relation and calculate the changed case. State whether the perturbation preserves the real operating point; update thermodynamic properties if needed.

**3–4.** Deceleration converts kinetic energy to pressure in an ideal diffuser; separation and compressibility reduce actual recovery. Use stagnation-pressure loss and wall-static pressure distributions to quantify recovery. Link one cause to an independent measurement and report uncertainty.

**5.** Size diffuser area ratio subject to flow separation and machine packaging. It is provisional pending independent safety, structural and performance review.

**Status:** All values are invented classroom inputs; this chapter is not a measured field study, machine certification or safe operating procedure.


---

## U04-L04 — Corrected compressor flow and speed

**Outcome.** Use conservation laws and appropriate reference stations to analyze **corrected compressor flow and speed**; solve a traceable numerical example; expose model limitations; and justify a provisional engineering choice. This is Unit 04, **Centrifugal Compressors and Diffusers**.

### 1. Physical setting and governing reasoning

Every turbomachine exchanges energy and momentum through moving surfaces. This lesson isolates one effect while retaining enough of the surrounding machine to prevent an unrealistic interpretation of its result. The shared design brief is: A process-air package contains an impeller, vaneless or vaned diffuser, return passages and seals; exit swirl and pressure recovery compete with mechanical limits. This particular lesson tests how corrected compressor flow and speed influences the balance among useful power, operating stability, mechanical limits and lifetime expense. The model applies only to its stated fluid and duty conditions.

**Physical mechanism:** Corrected quantities compare similar inlet Mach and density effects for a specified gas and reference state. Mark the control-volume stations, flow direction, shaft boundary and whether the stated measurements use absolute or relative velocity, total or static state.

### 2. Model and derivation

**Core equation:** `m_corr=m_dot sqrt(T01/T_ref)/(p01/p_ref)`.

The equation follows from the appropriate balance of energy, mass or angular momentum. Define the inlet, outlet and reference frame first; state whether an efficiency uses fluid, shaft or electric power and whether a pressure is static or total.

A radial impeller can impart high work because U increases with radius. Vaneless and vaned diffusers convert some discharge kinetic energy to static pressure without adding shaft work. The ideal enthalpy rise does not determine recovered static pressure if diffuser separation and mixing losses are large.

Check dimensions: J/kg = m²/s², hydraulic head uses metres, efficiency is dimensionless, and torque times rad/s gives watts.

### 3. Worked example and sensitivity

**Teaching case:** At m_dot=8 kg/s, T01=330 K, Tref=288.15 K, p01=95 kPa and pref=101.325 kPa, corrected flow is about 9.12 kg/s.

**Explicit substitution:** m_corr=8×sqrt(330/288.15)/(95/101.325); therefore **9.12 kg/s corrected**. This is a coordinate for a specified reference state, not physical mass flow.

Check arithmetic independently. Then perturb one input by 10%: linear, quadratic and cubic factors become 1.1, 1.21 and 1.331, respectively. Recompute nonlinear property relationships. An algebraic change is not evidence of a new real-machine operating point.

### 4. Loss mechanisms, diagnostics and design limits

**Critical misconception:** Calling corrected flow a conserved real flow confuses map coordinates with physical throughput. Consider off-design incidence, leakage, wakes and local mechanical or thermal limits; different machine types have distinct damage mechanisms.

**Test evidence:** Record reference conditions, gas properties, total inlet state and uncertainty. Record calibration and uncertainty, check the station definitions, and separate real losses from sensor or operating-point differences. A classroom correlation is not a qualification standard. The transition from calculation to product release requires traceable material data, instrument calibration, component testing and safety review. Where code compliance applies, record its edition and jurisdiction instead of claiming that an illustrative number confers approval.

**Provisional decision:** Match a package compressor to a map without extrapolating beyond supported speed lines. Revise this recommendation if an independently verified safety or stability constraint is violated.

### 5. Assessment (five tasks)

1. **Calculation:** Using `m_corr=m_dot sqrt(T01/T_ref)/(p01/p_ref)`, reproduce **9.12 kg/s corrected** and show every unit conversion. Explain why the chosen sign convention is necessary.
2. **Design variation:** Perturb the dominant flow, temperature, speed or head input by 10% and recompute. Which physical assumption fails first at a very different duty point?
3. **Failure investigation:** Use this misconception as the starting hypothesis: Calling corrected flow a conserved real flow confuses map coordinates with physical throughput. Propose an alternative explanation and one observation that distinguishes the two.
4. **Measurement plan:** Operationalize this requirement: Record reference conditions, gas properties, total inlet state and uncertainty. State one calibration check, one expected systematic error and how results are normalized to the same operating state.
5. **Decision memo:** Evaluate the provisional change: Match a package compressor to a map without extrapolating beyond supported speed lines. Identify a constraint or observation that would force the opposite decision.

### 6. Worked-answer guidance

**1.** The substitution is **m_corr=8×sqrt(330/288.15)/(95/101.325)**, yielding **9.12 kg/s corrected** under the stated simplifications. This is a coordinate for a specified reference state, not physical mass flow. A complete answer identifies pressure, temperature and rotor-frame conventions where relevant.

**2.** Apply the functional dependence of the displayed relation and calculate the changed case. State whether the perturbation preserves the real operating point; update thermodynamic properties if needed.

**3–4.** Corrected quantities compare similar inlet Mach and density effects for a specified gas and reference state. Record reference conditions, gas properties, total inlet state and uncertainty. Link one cause to an independent measurement and report uncertainty.

**5.** Match a package compressor to a map without extrapolating beyond supported speed lines. It is provisional pending independent safety, structural and performance review.

**Status:** All values are invented classroom inputs; this chapter is not a measured field study, machine certification or safe operating procedure.


---

## U04-L05 — Choke and impeller mechanical limits

**Outcome.** Use conservation laws and appropriate reference stations to analyze **choke and impeller mechanical limits**; solve a traceable numerical example; expose model limitations; and justify a provisional engineering choice. This is Unit 04, **Centrifugal Compressors and Diffusers**.

### 1. Physical setting and governing reasoning

Consider the difference between predicting a single performance number and qualifying a rotating machine. This lesson develops one measurable calculation, then asks which assumptions fail outside the demonstration state. The shared design brief is: A process-air package contains an impeller, vaneless or vaned diffuser, return passages and seals; exit swirl and pressure recovery compete with mechanical limits. This particular lesson tests how choke and impeller mechanical limits influences the balance among useful power, operating stability, mechanical limits and lifetime expense. The model applies only to its stated fluid and duty conditions.

**Physical mechanism:** Local throat Mach and relative-frame Mach can constrain maximum flow before whole-machine ratings indicate distress. Mark the control-volume stations, flow direction, shaft boundary and whether the stated measurements use absolute or relative velocity, total or static state.

### 2. Model and derivation

**Core equation:** `M=V/a; a=sqrt(gamma R T) for ideal gas`.

The equation follows from the appropriate balance of energy, mass or angular momentum. Define the inlet, outlet and reference frame first; state whether an efficiency uses fluid, shaft or electric power and whether a pressure is static or total.

Slip means the actual exit whirl differs from a perfectly guided idealization. Its definition and correlations depend on blade geometry, backsweep and test convention. Relative and absolute Mach numbers must be evaluated locally, particularly near the shroud and impeller throat.

Check dimensions: J/kg = m²/s², hydraulic head uses metres, efficiency is dimensionless, and torque times rad/s gives watts.

### 3. Worked example and sensitivity

**Teaching case:** A local absolute flow speed of 340 m/s at 300 K air gives Mach≈0.98 using gamma=1.4, R=287 J/(kg K).

**Explicit substitution:** a=sqrt(1.4×287×300); M=340/a; therefore **a≈347.2 m/s; M≈0.979**. Relative Mach may exceed the absolute Mach and matters at the blade throat.

Check arithmetic independently. Then perturb one input by 10%: linear, quadratic and cubic factors become 1.1, 1.21 and 1.331, respectively. Recompute nonlinear property relationships. An algebraic change is not evidence of a new real-machine operating point.

### 4. Loss mechanisms, diagnostics and design limits

**Critical misconception:** Assuming a casing-average Mach number captures local choking conceals blade passage acceleration. Consider off-design incidence, leakage, wakes and local mechanical or thermal limits; different machine types have distinct damage mechanisms.

**Test evidence:** Compare absolute and relative Mach predictions at hub, mean radius and shroud. Record calibration and uncertainty, check the station definitions, and separate real losses from sensor or operating-point differences. Identify every mass stream crossing the control volume, including leakage, bleed and cooling injections. For a steady insulated machine, power transfer is tied to the change in stagnation enthalpy, but heat leakage and unsteady stored energy can matter in a real test. If the energy residual is large, do not force it into an unexplained efficiency factor.

**Provisional decision:** Reduce demanded flow or modify passage throat rather than forcing operation off the vendor map. Revise this recommendation if an independently verified safety or stability constraint is violated.

### 5. Assessment (five tasks)

1. **Calculation:** Using `M=V/a; a=sqrt(gamma R T) for ideal gas`, reproduce **a≈347.2 m/s; M≈0.979** and show every unit conversion. Explain why the chosen sign convention is necessary.
2. **Design variation:** Perturb the dominant flow, temperature, speed or head input by 10% and recompute. Which physical assumption fails first at a very different duty point?
3. **Failure investigation:** Use this misconception as the starting hypothesis: Assuming a casing-average Mach number captures local choking conceals blade passage acceleration. Propose an alternative explanation and one observation that distinguishes the two.
4. **Measurement plan:** Operationalize this requirement: Compare absolute and relative Mach predictions at hub, mean radius and shroud. State one calibration check, one expected systematic error and how results are normalized to the same operating state.
5. **Decision memo:** Evaluate the provisional change: Reduce demanded flow or modify passage throat rather than forcing operation off the vendor map. Identify a constraint or observation that would force the opposite decision.

### 6. Worked-answer guidance

**1.** The substitution is **a=sqrt(1.4×287×300); M=340/a**, yielding **a≈347.2 m/s; M≈0.979** under the stated simplifications. Relative Mach may exceed the absolute Mach and matters at the blade throat. A complete answer identifies pressure, temperature and rotor-frame conventions where relevant.

**2.** Apply the functional dependence of the displayed relation and calculate the changed case. State whether the perturbation preserves the real operating point; update thermodynamic properties if needed.

**3–4.** Local throat Mach and relative-frame Mach can constrain maximum flow before whole-machine ratings indicate distress. Compare absolute and relative Mach predictions at hub, mean radius and shroud. Link one cause to an independent measurement and report uncertainty.

**5.** Reduce demanded flow or modify passage throat rather than forcing operation off the vendor map. It is provisional pending independent safety, structural and performance review.

**Status:** All values are invented classroom inputs; this chapter is not a measured field study, machine certification or safe operating procedure.


---

