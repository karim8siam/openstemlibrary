# Unit 03: Axial Compressors and Aerodynamic Stability

**Course Code**: TBM 303 · **Level**: Advanced Undergraduate Engineering

## Unit Overview & Physical Foundations

This comprehensive university textbook unit covers the theoretical framework, physical modeling, mathematical governing equations, and engineering applications of **Axial Compressors and Aerodynamic Stability**.

## U03-L01 — Axial compressor flow passages

**Outcome.** Use conservation laws and appropriate reference stations to analyze **axial compressor flow passages**; solve a traceable numerical example; expose model limitations; and justify a provisional engineering choice. This is Unit 03, **Axial Compressors and Aerodynamic Stability**.

### 1. Physical setting and governing reasoning

An engineer should be able to explain the direction of power transfer before touching a calculator. In this lesson the system boundary encloses the relevant machine component; the chosen inlet and outlet stations are part of the model, not details added after computing a value. The shared design brief is: A multistage air compressor is asked to deliver a pressure ratio across wide inlet conditions, while its blades must keep attached flow and the system must avoid surge. This particular lesson tests how axial compressor flow passages influences the balance among useful power, operating stability, mechanical limits and lifetime expense. The model applies only to its stated fluid and duty conditions.

**Physical mechanism:** The annular area accounts for the hub and casing; radial distribution and endwall boundary layers change useful throughflow. Mark the control-volume stations, flow direction, shaft boundary and whether the stated measurements use absolute or relative velocity, total or static state.

### 2. Model and derivation

**Core equation:** `m_dot=rho A Vax`.

The equation follows from the appropriate balance of energy, mass or angular momentum. Define the inlet, outlet and reference frame first; state whether an efficiency uses fluid, shaft or electric power and whether a pressure is static or total.

Axial blade-row losses depend on boundary layers, secondary motion, leakage and shock formation. Diffusion and incidence must be treated as a coupled aerodynamic constraint, not independent checklist items. A radial traverse reveals endwall effects masked by a single midspan probe.

Check dimensions: J/kg = m²/s², hydraulic head uses metres, efficiency is dimensionless, and torque times rad/s gives watts.

### 3. Worked example and sensitivity

**Teaching case:** With density 1.1 kg/m3, annulus area 0.12 m2 and axial velocity 115 m/s, the flow is 15.18 kg/s.

**Explicit substitution:** m_dot = 1.1×0.12×115; therefore **15.18 kg/s**. The area is the annulus, not the full casing disk.

Check arithmetic independently. Then perturb one input by 10%: linear, quadratic and cubic factors become 1.1, 1.21 and 1.331, respectively. Recompute nonlinear property relationships. An algebraic change is not evidence of a new real-machine operating point.

### 4. Loss mechanisms, diagnostics and design limits

**Critical misconception:** Using full casing circular area overestimates mass flow and understates stage loading. Consider off-design incidence, leakage, wakes and local mechanical or thermal limits; different machine types have distinct damage mechanisms.

**Test evidence:** Survey hub-to-tip geometry and measure total temperature, pressure and radial velocity profiles. Record calibration and uncertainty, check the station definitions, and separate real losses from sensor or operating-point differences. A classroom correlation is not a qualification standard. The transition from calculation to product release requires traceable material data, instrument calibration, component testing and safety review. Where code compliance applies, record its edition and jurisdiction instead of claiming that an illustrative number confers approval.

**Provisional decision:** Change mean annulus radius or blade height to respect tip-speed and Mach constraints. Revise this recommendation if an independently verified safety or stability constraint is violated.

### 5. Assessment (five tasks)

1. **Calculation:** Using `m_dot=rho A Vax`, reproduce **15.18 kg/s** and show every unit conversion. Explain why the chosen sign convention is necessary.
2. **Design variation:** Perturb the dominant flow, temperature, speed or head input by 10% and recompute. Which physical assumption fails first at a very different duty point?
3. **Failure investigation:** Use this misconception as the starting hypothesis: Using full casing circular area overestimates mass flow and understates stage loading. Propose an alternative explanation and one observation that distinguishes the two.
4. **Measurement plan:** Operationalize this requirement: Survey hub-to-tip geometry and measure total temperature, pressure and radial velocity profiles. State one calibration check, one expected systematic error and how results are normalized to the same operating state.
5. **Decision memo:** Evaluate the provisional change: Change mean annulus radius or blade height to respect tip-speed and Mach constraints. Identify a constraint or observation that would force the opposite decision.

### 6. Worked-answer guidance

**1.** The substitution is **m_dot = 1.1×0.12×115**, yielding **15.18 kg/s** under the stated simplifications. The area is the annulus, not the full casing disk. A complete answer identifies pressure, temperature and rotor-frame conventions where relevant.

**2.** Apply the functional dependence of the displayed relation and calculate the changed case. State whether the perturbation preserves the real operating point; update thermodynamic properties if needed.

**3–4.** The annular area accounts for the hub and casing; radial distribution and endwall boundary layers change useful throughflow. Survey hub-to-tip geometry and measure total temperature, pressure and radial velocity profiles. Link one cause to an independent measurement and report uncertainty.

**5.** Change mean annulus radius or blade height to respect tip-speed and Mach constraints. It is provisional pending independent safety, structural and performance review.

**Status:** All values are invented classroom inputs; this chapter is not a measured field study, machine certification or safe operating procedure.


---

## U03-L02 — Incidence, turning and cascade losses

**Outcome.** Use conservation laws and appropriate reference stations to analyze **incidence, turning and cascade losses**; solve a traceable numerical example; expose model limitations; and justify a provisional engineering choice. This is Unit 03, **Axial Compressors and Aerodynamic Stability**.

### 1. Physical setting and governing reasoning

The first challenge is to connect the observed state to a physical balance. A pressure, velocity or temperature measurement alone is incomplete until the flow direction, station definition and performance quantity have been fixed. The shared design brief is: A multistage air compressor is asked to deliver a pressure ratio across wide inlet conditions, while its blades must keep attached flow and the system must avoid surge. This particular lesson tests how incidence, turning and cascade losses influences the balance among useful power, operating stability, mechanical limits and lifetime expense. The model applies only to its stated fluid and duty conditions.

**Physical mechanism:** Blade turning requires a pressure distribution that a boundary layer can withstand without separation. Mark the control-volume stations, flow direction, shaft boundary and whether the stated measurements use absolute or relative velocity, total or static state.

### 2. Model and derivation

**Core equation:** `incidence = beta_inlet_flow - beta_metal`.

The equation follows from the appropriate balance of energy, mass or angular momentum. Define the inlet, outlet and reference frame first; state whether an efficiency uses fluid, shaft or electric power and whether a pressure is static or total.

A map uses corrected flow and speed with defined inlet reference conditions. An operating line that approaches rotating stall or system surge is a dynamic hazard; steady map separation alone is not sufficient for protection or transient guarantee.

Check dimensions: J/kg = m²/s², hydraulic head uses metres, efficiency is dimensionless, and torque times rad/s gives watts.

### 3. Worked example and sensitivity

**Teaching case:** A relative flow angle of -41 degrees at the leading edge and a metal angle of -45 degrees implies +4 degrees incidence.

**Explicit substitution:** incidence = (−41°)−(−45°); therefore **+4°**. Opposite sign convention would need a corresponding interpretation change.

Check arithmetic independently. Then perturb one input by 10%: linear, quadratic and cubic factors become 1.1, 1.21 and 1.331, respectively. Recompute nonlinear property relationships. An algebraic change is not evidence of a new real-machine operating point.

### 4. Loss mechanisms, diagnostics and design limits

**Critical misconception:** Treating an isolated airfoil lift curve as a cascade loss correlation ignores neighboring blades. Consider off-design incidence, leakage, wakes and local mechanical or thermal limits; different machine types have distinct damage mechanisms.

**Test evidence:** Use traverse data before and after a blade row and report circumferential averaging method. Record calibration and uncertainty, check the station definitions, and separate real losses from sensor or operating-point differences. Identify every mass stream crossing the control volume, including leakage, bleed and cooling injections. For a steady insulated machine, power transfer is tied to the change in stagnation enthalpy, but heat leakage and unsteady stored energy can matter in a real test. If the energy residual is large, do not force it into an unexplained efficiency factor.

**Provisional decision:** Adjust variable inlet guide vanes to reduce off-design incidence. Revise this recommendation if an independently verified safety or stability constraint is violated.

### 5. Assessment (five tasks)

1. **Calculation:** Using `incidence = beta_inlet_flow - beta_metal`, reproduce **+4°** and show every unit conversion. Explain why the chosen sign convention is necessary.
2. **Design variation:** Perturb the dominant flow, temperature, speed or head input by 10% and recompute. Which physical assumption fails first at a very different duty point?
3. **Failure investigation:** Use this misconception as the starting hypothesis: Treating an isolated airfoil lift curve as a cascade loss correlation ignores neighboring blades. Propose an alternative explanation and one observation that distinguishes the two.
4. **Measurement plan:** Operationalize this requirement: Use traverse data before and after a blade row and report circumferential averaging method. State one calibration check, one expected systematic error and how results are normalized to the same operating state.
5. **Decision memo:** Evaluate the provisional change: Adjust variable inlet guide vanes to reduce off-design incidence. Identify a constraint or observation that would force the opposite decision.

### 6. Worked-answer guidance

**1.** The substitution is **incidence = (−41°)−(−45°)**, yielding **+4°** under the stated simplifications. Opposite sign convention would need a corresponding interpretation change. A complete answer identifies pressure, temperature and rotor-frame conventions where relevant.

**2.** Apply the functional dependence of the displayed relation and calculate the changed case. State whether the perturbation preserves the real operating point; update thermodynamic properties if needed.

**3–4.** Blade turning requires a pressure distribution that a boundary layer can withstand without separation. Use traverse data before and after a blade row and report circumferential averaging method. Link one cause to an independent measurement and report uncertainty.

**5.** Adjust variable inlet guide vanes to reduce off-design incidence. It is provisional pending independent safety, structural and performance review.

**Status:** All values are invented classroom inputs; this chapter is not a measured field study, machine certification or safe operating procedure.


---

## U03-L03 — Degree of reaction in an axial stage

**Outcome.** Use conservation laws and appropriate reference stations to analyze **degree of reaction in an axial stage**; solve a traceable numerical example; expose model limitations; and justify a provisional engineering choice. This is Unit 03, **Axial Compressors and Aerodynamic Stability**.

### 1. Physical setting and governing reasoning

An apparently simple equipment decision becomes difficult when the operating envelope shifts. Work from conservation laws to a tractable approximation, and only then decide what constitutes evidence for the performance claim. The shared design brief is: A multistage air compressor is asked to deliver a pressure ratio across wide inlet conditions, while its blades must keep attached flow and the system must avoid surge. This particular lesson tests how degree of reaction in an axial stage influences the balance among useful power, operating stability, mechanical limits and lifetime expense. The model applies only to its stated fluid and duty conditions.

**Physical mechanism:** Reaction distributes static enthalpy changes across rotor and stator; reference stations must be stated clearly. Mark the control-volume stations, flow direction, shaft boundary and whether the stated measurements use absolute or relative velocity, total or static state.

### 2. Model and derivation

**Core equation:** `R=Delta_h_static_rotor/Delta_h_static_stage with specified stations`.

The equation follows from the appropriate balance of energy, mass or angular momentum. Define the inlet, outlet and reference frame first; state whether an efficiency uses fluid, shaft or electric power and whether a pressure is static or total.

A compressor stage repeatedly adds stagnation enthalpy and raises total pressure while stators recover dynamic pressure and set the next row inlet angle. A positive pressure ratio requires shaft power and generally heats the gas. For an ideal gas, T02s/T01=pi^((gamma-1)/gamma); actual T02 is larger at equal exit total pressure.

Check dimensions: J/kg = m²/s², hydraulic head uses metres, efficiency is dimensionless, and torque times rad/s gives watts.

### 3. Worked example and sensitivity

**Teaching case:** If rotor static enthalpy increases 10 kJ/kg and the whole stage increases 22 kJ/kg, the reaction is about 0.455.

**Explicit substitution:** R = 10/22; therefore **0.4545**. Rotor and stage static enthalpy stations must be stated.

Check arithmetic independently. Then perturb one input by 10%: linear, quadratic and cubic factors become 1.1, 1.21 and 1.331, respectively. Recompute nonlinear property relationships. An algebraic change is not evidence of a new real-machine operating point.

### 4. Loss mechanisms, diagnostics and design limits

**Critical misconception:** Applying one reaction convention to all turbine and compressor texts creates apparent contradictions. Consider off-design incidence, leakage, wakes and local mechanical or thermal limits; different machine types have distinct damage mechanisms.

**Test evidence:** Use static and stagnation thermodynamic stations and verify rotor/stator boundaries. Record calibration and uncertainty, check the station definitions, and separate real losses from sensor or operating-point differences. The best-efficiency point is merely one location on a map. Startup, shutdown, reduced duty, elevated temperature and equipment aging may create more restrictive limits. A specification should include allowable flow, speed, vibration, pressure and temperature, with a defined trip or mitigation strategy.

**Provisional decision:** Decide how stage loading is split to control diffusion and blade-row losses. Revise this recommendation if an independently verified safety or stability constraint is violated.

### 5. Assessment (five tasks)

1. **Calculation:** Using `R=Delta_h_static_rotor/Delta_h_static_stage with specified stations`, reproduce **0.4545** and show every unit conversion. Explain why the chosen sign convention is necessary.
2. **Design variation:** Perturb the dominant flow, temperature, speed or head input by 10% and recompute. Which physical assumption fails first at a very different duty point?
3. **Failure investigation:** Use this misconception as the starting hypothesis: Applying one reaction convention to all turbine and compressor texts creates apparent contradictions. Propose an alternative explanation and one observation that distinguishes the two.
4. **Measurement plan:** Operationalize this requirement: Use static and stagnation thermodynamic stations and verify rotor/stator boundaries. State one calibration check, one expected systematic error and how results are normalized to the same operating state.
5. **Decision memo:** Evaluate the provisional change: Decide how stage loading is split to control diffusion and blade-row losses. Identify a constraint or observation that would force the opposite decision.

### 6. Worked-answer guidance

**1.** The substitution is **R = 10/22**, yielding **0.4545** under the stated simplifications. Rotor and stage static enthalpy stations must be stated. A complete answer identifies pressure, temperature and rotor-frame conventions where relevant.

**2.** Apply the functional dependence of the displayed relation and calculate the changed case. State whether the perturbation preserves the real operating point; update thermodynamic properties if needed.

**3–4.** Reaction distributes static enthalpy changes across rotor and stator; reference stations must be stated clearly. Use static and stagnation thermodynamic stations and verify rotor/stator boundaries. Link one cause to an independent measurement and report uncertainty.

**5.** Decide how stage loading is split to control diffusion and blade-row losses. It is provisional pending independent safety, structural and performance review.

**Status:** All values are invented classroom inputs; this chapter is not a measured field study, machine certification or safe operating procedure.


---

## U03-L04 — Compressor pressure ratio and isentropic efficiency

**Outcome.** Use conservation laws and appropriate reference stations to analyze **compressor pressure ratio and isentropic efficiency**; solve a traceable numerical example; expose model limitations; and justify a provisional engineering choice. This is Unit 03, **Axial Compressors and Aerodynamic Stability**.

### 1. Physical setting and governing reasoning

Every turbomachine exchanges energy and momentum through moving surfaces. This lesson isolates one effect while retaining enough of the surrounding machine to prevent an unrealistic interpretation of its result. The shared design brief is: A multistage air compressor is asked to deliver a pressure ratio across wide inlet conditions, while its blades must keep attached flow and the system must avoid surge. This particular lesson tests how compressor pressure ratio and isentropic efficiency influences the balance among useful power, operating stability, mechanical limits and lifetime expense. The model applies only to its stated fluid and duty conditions.

**Physical mechanism:** Isentropic efficiency compares ideal enthalpy rise to actual rise at the same pressure ratio. Mark the control-volume stations, flow direction, shaft boundary and whether the stated measurements use absolute or relative velocity, total or static state.

### 2. Model and derivation

**Core equation:** `eta_c=(pi^((gamma-1)/gamma)-1)/(T02/T01-1)`.

The equation follows from the appropriate balance of energy, mass or angular momentum. Define the inlet, outlet and reference frame first; state whether an efficiency uses fluid, shaft or electric power and whether a pressure is static or total.

Axial blade-row losses depend on boundary layers, secondary motion, leakage and shock formation. Diffusion and incidence must be treated as a coupled aerodynamic constraint, not independent checklist items. A radial traverse reveals endwall effects masked by a single midspan probe.

Check dimensions: J/kg = m²/s², hydraulic head uses metres, efficiency is dimensionless, and torque times rad/s gives watts.

### 3. Worked example and sensitivity

**Teaching case:** Air with pi=2.5, gamma=1.4, T01=300 K and T02=415 K has eta_c≈0.780.

**Explicit substitution:** eta_c = [2.5^(0.4/1.4)−1]/(415/300−1); therefore **0.7807**. T temperatures are in kelvin and actual rise exceeds isentropic rise.

Check arithmetic independently. Then perturb one input by 10%: linear, quadratic and cubic factors become 1.1, 1.21 and 1.331, respectively. Recompute nonlinear property relationships. An algebraic change is not evidence of a new real-machine operating point.

### 4. Loss mechanisms, diagnostics and design limits

**Critical misconception:** Using Celsius temperatures inside ratios or applying turbine efficiency direction gives false results. Consider off-design incidence, leakage, wakes and local mechanical or thermal limits; different machine types have distinct damage mechanisms.

**Test evidence:** Measure total T and p with calibrated probes and evaluate uncertainty from small temperature rises. Record calibration and uncertainty, check the station definitions, and separate real losses from sensor or operating-point differences. An adverse trend can result from fouling, poor installation, instrumentation drift or genuine wear. Avoid replacing components on the basis of one efficiency number. Compare independent signals such as vibration, temperature, flow, differential pressure and operating history before diagnosing cause.

**Provisional decision:** Decide whether another stage or intercooling is preferable to a higher single-stage ratio. Revise this recommendation if an independently verified safety or stability constraint is violated.

### 5. Assessment (five tasks)

1. **Calculation:** Using `eta_c=(pi^((gamma-1)/gamma)-1)/(T02/T01-1)`, reproduce **0.7807** and show every unit conversion. Explain why the chosen sign convention is necessary.
2. **Design variation:** Perturb the dominant flow, temperature, speed or head input by 10% and recompute. Which physical assumption fails first at a very different duty point?
3. **Failure investigation:** Use this misconception as the starting hypothesis: Using Celsius temperatures inside ratios or applying turbine efficiency direction gives false results. Propose an alternative explanation and one observation that distinguishes the two.
4. **Measurement plan:** Operationalize this requirement: Measure total T and p with calibrated probes and evaluate uncertainty from small temperature rises. State one calibration check, one expected systematic error and how results are normalized to the same operating state.
5. **Decision memo:** Evaluate the provisional change: Decide whether another stage or intercooling is preferable to a higher single-stage ratio. Identify a constraint or observation that would force the opposite decision.

### 6. Worked-answer guidance

**1.** The substitution is **eta_c = [2.5^(0.4/1.4)−1]/(415/300−1)**, yielding **0.7807** under the stated simplifications. T temperatures are in kelvin and actual rise exceeds isentropic rise. A complete answer identifies pressure, temperature and rotor-frame conventions where relevant.

**2.** Apply the functional dependence of the displayed relation and calculate the changed case. State whether the perturbation preserves the real operating point; update thermodynamic properties if needed.

**3–4.** Isentropic efficiency compares ideal enthalpy rise to actual rise at the same pressure ratio. Measure total T and p with calibrated probes and evaluate uncertainty from small temperature rises. Link one cause to an independent measurement and report uncertainty.

**5.** Decide whether another stage or intercooling is preferable to a higher single-stage ratio. It is provisional pending independent safety, structural and performance review.

**Status:** All values are invented classroom inputs; this chapter is not a measured field study, machine certification or safe operating procedure.


---

## U03-L05 — Stall and surge as distinct instabilities

**Outcome.** Use conservation laws and appropriate reference stations to analyze **stall and surge as distinct instabilities**; solve a traceable numerical example; expose model limitations; and justify a provisional engineering choice. This is Unit 03, **Axial Compressors and Aerodynamic Stability**.

### 1. Physical setting and governing reasoning

Consider the difference between predicting a single performance number and qualifying a rotating machine. This lesson develops one measurable calculation, then asks which assumptions fail outside the demonstration state. The shared design brief is: A multistage air compressor is asked to deliver a pressure ratio across wide inlet conditions, while its blades must keep attached flow and the system must avoid surge. This particular lesson tests how stall and surge as distinct instabilities influences the balance among useful power, operating stability, mechanical limits and lifetime expense. The model applies only to its stated fluid and duty conditions.

**Physical mechanism:** Rotating stall involves local blade-row flow breakdown; surge is a system-level unsteady flow and pressure oscillation. Mark the control-volume stations, flow direction, shaft boundary and whether the stated measurements use absolute or relative velocity, total or static state.

### 2. Model and derivation

**Core equation:** `surge_margin=(PR_surge-PR_operating)/PR_operating at a defined corrected flow`.

The equation follows from the appropriate balance of energy, mass or angular momentum. Define the inlet, outlet and reference frame first; state whether an efficiency uses fluid, shaft or electric power and whether a pressure is static or total.

A map uses corrected flow and speed with defined inlet reference conditions. An operating line that approaches rotating stall or system surge is a dynamic hazard; steady map separation alone is not sufficient for protection or transient guarantee.

Check dimensions: J/kg = m²/s², hydraulic head uses metres, efficiency is dimensionless, and torque times rad/s gives watts.

### 3. Worked example and sensitivity

**Teaching case:** At common corrected flow, PR_surge=3.1 and PR_operating=2.8 give a nominal 10.7% ratio margin.

**Explicit substitution:** (3.1−2.8)/2.8×100; therefore **10.71% pressure-ratio margin**. A static scalar margin does not resolve transient surge risk.

Check arithmetic independently. Then perturb one input by 10%: linear, quadratic and cubic factors become 1.1, 1.21 and 1.331, respectively. Recompute nonlinear property relationships. An algebraic change is not evidence of a new real-machine operating point.

### 4. Loss mechanisms, diagnostics and design limits

**Critical misconception:** Treating a single scalar margin as proof of safety across transient speeds is unacceptable. Consider off-design incidence, leakage, wakes and local mechanical or thermal limits; different machine types have distinct damage mechanisms.

**Test evidence:** Use manufacturer maps, dynamic pressure measurements and validated transient control simulations. Record calibration and uncertainty, check the station definitions, and separate real losses from sensor or operating-point differences. Real flow deviates from uniform one-dimensional pictures because of wakes, secondary flow, wall boundary layers and tip leakage. An equation that gives a plausible central value does not establish the distribution over the blade span. This is why credible performance assessment combines integrated measurements with local diagnostics and a transparent loss model.

**Provisional decision:** Set anti-surge recycle and variable geometry policies with conservative operating boundaries. Revise this recommendation if an independently verified safety or stability constraint is violated.

### 5. Assessment (five tasks)

1. **Calculation:** Using `surge_margin=(PR_surge-PR_operating)/PR_operating at a defined corrected flow`, reproduce **10.71% pressure-ratio margin** and show every unit conversion. Explain why the chosen sign convention is necessary.
2. **Design variation:** Perturb the dominant flow, temperature, speed or head input by 10% and recompute. Which physical assumption fails first at a very different duty point?
3. **Failure investigation:** Use this misconception as the starting hypothesis: Treating a single scalar margin as proof of safety across transient speeds is unacceptable. Propose an alternative explanation and one observation that distinguishes the two.
4. **Measurement plan:** Operationalize this requirement: Use manufacturer maps, dynamic pressure measurements and validated transient control simulations. State one calibration check, one expected systematic error and how results are normalized to the same operating state.
5. **Decision memo:** Evaluate the provisional change: Set anti-surge recycle and variable geometry policies with conservative operating boundaries. Identify a constraint or observation that would force the opposite decision.

### 6. Worked-answer guidance

**1.** The substitution is **(3.1−2.8)/2.8×100**, yielding **10.71% pressure-ratio margin** under the stated simplifications. A static scalar margin does not resolve transient surge risk. A complete answer identifies pressure, temperature and rotor-frame conventions where relevant.

**2.** Apply the functional dependence of the displayed relation and calculate the changed case. State whether the perturbation preserves the real operating point; update thermodynamic properties if needed.

**3–4.** Rotating stall involves local blade-row flow breakdown; surge is a system-level unsteady flow and pressure oscillation. Use manufacturer maps, dynamic pressure measurements and validated transient control simulations. Link one cause to an independent measurement and report uncertainty.

**5.** Set anti-surge recycle and variable geometry policies with conservative operating boundaries. It is provisional pending independent safety, structural and performance review.

**Status:** All values are invented classroom inputs; this chapter is not a measured field study, machine certification or safe operating procedure.


---

