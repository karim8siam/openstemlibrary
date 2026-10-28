# Unit 01: Foundations of Energy Transfer in Rotating Flow

**Course Code**: TBM 301 · **Level**: Advanced Undergraduate Engineering

## Unit Overview & Physical Foundations

This comprehensive university textbook unit covers the theoretical framework, physical modeling, mathematical governing equations, and engineering applications of **Foundations of Energy Transfer in Rotating Flow**.

## U01-L01 — Rotor control volumes and machine classification

**Outcome.** Use conservation laws and appropriate reference stations to analyze **rotor control volumes and machine classification**; solve a traceable numerical example; expose model limitations; and justify a provisional engineering choice. This is Unit 01, **Foundations of Energy Transfer in Rotating Flow**.

### 1. Physical setting and governing reasoning

An engineer should be able to explain the direction of power transfer before touching a calculator. In this lesson the system boundary encloses the relevant machine component; the chosen inlet and outlet stations are part of the model, not details added after computing a value. The shared design brief is: A water test bench and an air supply rig demonstrate that a rotating machine can exchange energy with fluid even when the inlet and outlet static pressures do not alone reveal its shaft duty. This particular lesson tests how rotor control volumes and machine classification influences the balance among useful power, operating stability, mechanical limits and lifetime expense. The model applies only to its stated fluid and duty conditions.

**Physical mechanism:** A rotor transmits torque through blade surface forces; a stator may turn or diffuse the flow but does no steady shaft work. Mark the control-volume stations, flow direction, shaft boundary and whether the stated measurements use absolute or relative velocity, total or static state.

### 2. Model and derivation

**Core equation:** `P_shaft = m_dot (h02-h01) for steady adiabatic compressor with negligible mechanical loss`.

The equation follows from the appropriate balance of energy, mass or angular momentum. Define the inlet, outlet and reference frame first; state whether an efficiency uses fluid, shaft or electric power and whether a pressure is static or total.

Start with a torque balance around the rotor axis and name positive rotation. The steady angular-momentum balance connects torque to mass flow times change in r Vtheta. Multiplication by angular velocity yields the ideal Euler work equation. Because U=omega r, this is not a mysterious empirical correlation. It is a specific form of angular momentum conservation.

Check dimensions: J/kg = m²/s², hydraulic head uses metres, efficiency is dimensionless, and torque times rad/s gives watts.

### 3. Worked example and sensitivity

**Teaching case:** An air stream of 3.0 kg/s receiving 18 kJ/kg of stagnation enthalpy requires 54 kW of ideal fluid power.

**Explicit substitution:** 3.0 kg/s × 18 kJ/kg = 54 kJ/s; therefore **54 kW**. A compressor needs fluid energy input, with greater actual shaft input if mechanical losses occur.

Check arithmetic independently. Then perturb one input by 10%: linear, quadratic and cubic factors become 1.1, 1.21 and 1.331, respectively. Recompute nonlinear property relationships. An algebraic change is not evidence of a new real-machine operating point.

### 4. Loss mechanisms, diagnostics and design limits

**Critical misconception:** Reading a large static-pressure rise as proof of equal shaft work ignores kinetic energy change and heat transfer. Consider off-design incidence, leakage, wakes and local mechanical or thermal limits; different machine types have distinct damage mechanisms.

**Test evidence:** Record torque, rotational speed, total temperatures and mass flow simultaneously across an insulated test section. Record calibration and uncertainty, check the station definitions, and separate real losses from sensor or operating-point differences. When comparing before-and-after tests, hold corrected flow or an equivalent meaningful operating state close enough that changing duty does not masquerade as better hardware. Temperature and gas composition influence corrected variables, while a hydraulic network may change substantially with valve setting. State the comparison tolerance rather than assuming curves can be overlaid without adjustment.

**Provisional decision:** Decide whether a radial pump, axial fan or positive-displacement machine matches the demanded pressure and flow regime. Revise this recommendation if an independently verified safety or stability constraint is violated.

### 5. Assessment (five tasks)

1. **Calculation:** Using `P_shaft = m_dot (h02-h01) for steady adiabatic compressor with negligible mechanical loss`, reproduce **54 kW** and show every unit conversion. Explain why the chosen sign convention is necessary.
2. **Design variation:** Perturb the dominant flow, temperature, speed or head input by 10% and recompute. Which physical assumption fails first at a very different duty point?
3. **Failure investigation:** Use this misconception as the starting hypothesis: Reading a large static-pressure rise as proof of equal shaft work ignores kinetic energy change and heat transfer. Propose an alternative explanation and one observation that distinguishes the two.
4. **Measurement plan:** Operationalize this requirement: Record torque, rotational speed, total temperatures and mass flow simultaneously across an insulated test section. State one calibration check, one expected systematic error and how results are normalized to the same operating state.
5. **Decision memo:** Evaluate the provisional change: Decide whether a radial pump, axial fan or positive-displacement machine matches the demanded pressure and flow regime. Identify a constraint or observation that would force the opposite decision.

### 6. Worked-answer guidance

**1.** The substitution is **3.0 kg/s × 18 kJ/kg = 54 kJ/s**, yielding **54 kW** under the stated simplifications. A compressor needs fluid energy input, with greater actual shaft input if mechanical losses occur. A complete answer identifies pressure, temperature and rotor-frame conventions where relevant.

**2.** Apply the functional dependence of the displayed relation and calculate the changed case. State whether the perturbation preserves the real operating point; update thermodynamic properties if needed.

**3–4.** A rotor transmits torque through blade surface forces; a stator may turn or diffuse the flow but does no steady shaft work. Record torque, rotational speed, total temperatures and mass flow simultaneously across an insulated test section. Link one cause to an independent measurement and report uncertainty.

**5.** Decide whether a radial pump, axial fan or positive-displacement machine matches the demanded pressure and flow regime. It is provisional pending independent safety, structural and performance review.

**Status:** All values are invented classroom inputs; this chapter is not a measured field study, machine certification or safe operating procedure.


---

## U01-L02 — Angular momentum and Euler specific work

**Outcome.** Use conservation laws and appropriate reference stations to analyze **angular momentum and euler specific work**; solve a traceable numerical example; expose model limitations; and justify a provisional engineering choice. This is Unit 01, **Foundations of Energy Transfer in Rotating Flow**.

### 1. Physical setting and governing reasoning

The first challenge is to connect the observed state to a physical balance. A pressure, velocity or temperature measurement alone is incomplete until the flow direction, station definition and performance quantity have been fixed. The shared design brief is: A water test bench and an air supply rig demonstrate that a rotating machine can exchange energy with fluid even when the inlet and outlet static pressures do not alone reveal its shaft duty. This particular lesson tests how angular momentum and euler specific work influences the balance among useful power, operating stability, mechanical limits and lifetime expense. The model applies only to its stated fluid and duty conditions.

**Physical mechanism:** Tangential momentum change produces torque; the absolute and relative frames must not be mixed in the moment balance. Mark the control-volume stations, flow direction, shaft boundary and whether the stated measurements use absolute or relative velocity, total or static state.

### 2. Model and derivation

**Core equation:** `w_on = U2 Vtheta2 - U1 Vtheta1`.

The equation follows from the appropriate balance of energy, mass or angular momentum. Define the inlet, outlet and reference frame first; state whether an efficiency uses fluid, shaft or electric power and whether a pressure is static or total.

Before substituting numbers, draw velocity triangles: V is absolute, U is tangential blade velocity and W=V-U is relative. Record whether Vtheta is co-rotating or counter-rotating. Total enthalpy h0=h+V^2/2 is appropriate for energy accounting across an adiabatic rotating row, but total pressure can decrease because entropy increases.

Check dimensions: J/kg = m²/s², hydraulic head uses metres, efficiency is dimensionless, and torque times rad/s gives watts.

### 3. Worked example and sensitivity

**Teaching case:** With U1=100 m/s, Vtheta1=8 m/s, U2=160 m/s and Vtheta2=48 m/s, ideal specific input is 6880 J/kg.

**Explicit substitution:** 160×48 − 100×8 = 7680 − 800; therefore **6880 J/kg**. Exit whirl is taken positive with the rotor; reversing it changes the sign.

Check arithmetic independently. Then perturb one input by 10%: linear, quadratic and cubic factors become 1.1, 1.21 and 1.331, respectively. Recompute nonlinear property relationships. An algebraic change is not evidence of a new real-machine operating point.

### 4. Loss mechanisms, diagnostics and design limits

**Critical misconception:** Using velocity magnitude instead of the tangential component can reverse the sign or invent work. Consider off-design incidence, leakage, wakes and local mechanical or thermal limits; different machine types have distinct damage mechanisms.

**Test evidence:** Determine radius and whirl direction at both measurement planes and compare shaft torque with fluid angular momentum flux. Record calibration and uncertainty, check the station definitions, and separate real losses from sensor or operating-point differences. Estimate which measured inputs dominate the output by perturbing them individually. If a 1% sensor shift changes a design recommendation, the decision is not robust without calibration and repeat testing. Report the measurement chain and the test range, not only the final digits.

**Provisional decision:** Choose blade exit direction that delivers required specific work without excessive swirl loss. Revise this recommendation if an independently verified safety or stability constraint is violated.

### 5. Assessment (five tasks)

1. **Calculation:** Using `w_on = U2 Vtheta2 - U1 Vtheta1`, reproduce **6880 J/kg** and show every unit conversion. Explain why the chosen sign convention is necessary.
2. **Design variation:** Perturb the dominant flow, temperature, speed or head input by 10% and recompute. Which physical assumption fails first at a very different duty point?
3. **Failure investigation:** Use this misconception as the starting hypothesis: Using velocity magnitude instead of the tangential component can reverse the sign or invent work. Propose an alternative explanation and one observation that distinguishes the two.
4. **Measurement plan:** Operationalize this requirement: Determine radius and whirl direction at both measurement planes and compare shaft torque with fluid angular momentum flux. State one calibration check, one expected systematic error and how results are normalized to the same operating state.
5. **Decision memo:** Evaluate the provisional change: Choose blade exit direction that delivers required specific work without excessive swirl loss. Identify a constraint or observation that would force the opposite decision.

### 6. Worked-answer guidance

**1.** The substitution is **160×48 − 100×8 = 7680 − 800**, yielding **6880 J/kg** under the stated simplifications. Exit whirl is taken positive with the rotor; reversing it changes the sign. A complete answer identifies pressure, temperature and rotor-frame conventions where relevant.

**2.** Apply the functional dependence of the displayed relation and calculate the changed case. State whether the perturbation preserves the real operating point; update thermodynamic properties if needed.

**3–4.** Tangential momentum change produces torque; the absolute and relative frames must not be mixed in the moment balance. Determine radius and whirl direction at both measurement planes and compare shaft torque with fluid angular momentum flux. Link one cause to an independent measurement and report uncertainty.

**5.** Choose blade exit direction that delivers required specific work without excessive swirl loss. It is provisional pending independent safety, structural and performance review.

**Status:** All values are invented classroom inputs; this chapter is not a measured field study, machine certification or safe operating procedure.


---

## U01-L03 — Velocity triangles and blade angles

**Outcome.** Use conservation laws and appropriate reference stations to analyze **velocity triangles and blade angles**; solve a traceable numerical example; expose model limitations; and justify a provisional engineering choice. This is Unit 01, **Foundations of Energy Transfer in Rotating Flow**.

### 1. Physical setting and governing reasoning

An apparently simple equipment decision becomes difficult when the operating envelope shifts. Work from conservation laws to a tractable approximation, and only then decide what constitutes evidence for the performance claim. The shared design brief is: A water test bench and an air supply rig demonstrate that a rotating machine can exchange energy with fluid even when the inlet and outlet static pressures do not alone reveal its shaft duty. This particular lesson tests how velocity triangles and blade angles influences the balance among useful power, operating stability, mechanical limits and lifetime expense. The model applies only to its stated fluid and duty conditions.

**Physical mechanism:** A blade encounters relative flow, whereas a stationary probe measures absolute velocity; incidence depends on the relative angle. Mark the control-volume stations, flow direction, shaft boundary and whether the stated measurements use absolute or relative velocity, total or static state.

### 2. Model and derivation

**Core equation:** `Wtheta = Vtheta - U; tan(beta)=Wtheta/Vax`.

The equation follows from the appropriate balance of energy, mass or angular momentum. Define the inlet, outlet and reference frame first; state whether an efficiency uses fluid, shaft or electric power and whether a pressure is static or total.

A reliable preliminary design separates an inviscid rotor idealization from real loss estimates. Reynolds number, relative Mach number, clearances and blade incidence affect similarity. At the next stage, the engineer must interpret compressor sign conventions differently from turbine extraction without reusing one equation carelessly.

Check dimensions: J/kg = m²/s², hydraulic head uses metres, efficiency is dimensionless, and torque times rad/s gives watts.

### 3. Worked example and sensitivity

**Teaching case:** Air with U=150 m/s, Vtheta=35 m/s and Vax=70 m/s has Wtheta=-115 m/s and beta approximately -58.7 degrees.

**Explicit substitution:** Wtheta = 35 − 150 = −115 m/s; beta = atan2(−115,70); therefore **−58.7°**. Use signed components, not unsigned velocity magnitudes.

Check arithmetic independently. Then perturb one input by 10%: linear, quadratic and cubic factors become 1.1, 1.21 and 1.331, respectively. Recompute nonlinear property relationships. An algebraic change is not evidence of a new real-machine operating point.

### 4. Loss mechanisms, diagnostics and design limits

**Critical misconception:** Subtracting speed magnitudes rather than vector components falsely predicts incidence and shock loss. Consider off-design incidence, leakage, wakes and local mechanical or thermal limits; different machine types have distinct damage mechanisms.

**Test evidence:** Estimate Vax, Vtheta and U at a common radius; report sign convention and angular uncertainty. Record calibration and uncertainty, check the station definitions, and separate real losses from sensor or operating-point differences. A classroom correlation is not a qualification standard. The transition from calculation to product release requires traceable material data, instrument calibration, component testing and safety review. Where code compliance applies, record its edition and jurisdiction instead of claiming that an illustrative number confers approval.

**Provisional decision:** Set stagger and inlet guide vane angle for a specified incidence band rather than a single point. Revise this recommendation if an independently verified safety or stability constraint is violated.

### 5. Assessment (five tasks)

1. **Calculation:** Using `Wtheta = Vtheta - U; tan(beta)=Wtheta/Vax`, reproduce **−58.7°** and show every unit conversion. Explain why the chosen sign convention is necessary.
2. **Design variation:** Perturb the dominant flow, temperature, speed or head input by 10% and recompute. Which physical assumption fails first at a very different duty point?
3. **Failure investigation:** Use this misconception as the starting hypothesis: Subtracting speed magnitudes rather than vector components falsely predicts incidence and shock loss. Propose an alternative explanation and one observation that distinguishes the two.
4. **Measurement plan:** Operationalize this requirement: Estimate Vax, Vtheta and U at a common radius; report sign convention and angular uncertainty. State one calibration check, one expected systematic error and how results are normalized to the same operating state.
5. **Decision memo:** Evaluate the provisional change: Set stagger and inlet guide vane angle for a specified incidence band rather than a single point. Identify a constraint or observation that would force the opposite decision.

### 6. Worked-answer guidance

**1.** The substitution is **Wtheta = 35 − 150 = −115 m/s; beta = atan2(−115,70)**, yielding **−58.7°** under the stated simplifications. Use signed components, not unsigned velocity magnitudes. A complete answer identifies pressure, temperature and rotor-frame conventions where relevant.

**2.** Apply the functional dependence of the displayed relation and calculate the changed case. State whether the perturbation preserves the real operating point; update thermodynamic properties if needed.

**3–4.** A blade encounters relative flow, whereas a stationary probe measures absolute velocity; incidence depends on the relative angle. Estimate Vax, Vtheta and U at a common radius; report sign convention and angular uncertainty. Link one cause to an independent measurement and report uncertainty.

**5.** Set stagger and inlet guide vane angle for a specified incidence band rather than a single point. It is provisional pending independent safety, structural and performance review.

**Status:** All values are invented classroom inputs; this chapter is not a measured field study, machine certification or safe operating procedure.


---

## U01-L04 — Flow, head and loading coefficients

**Outcome.** Use conservation laws and appropriate reference stations to analyze **flow, head and loading coefficients**; solve a traceable numerical example; expose model limitations; and justify a provisional engineering choice. This is Unit 01, **Foundations of Energy Transfer in Rotating Flow**.

### 1. Physical setting and governing reasoning

Every turbomachine exchanges energy and momentum through moving surfaces. This lesson isolates one effect while retaining enough of the surrounding machine to prevent an unrealistic interpretation of its result. The shared design brief is: A water test bench and an air supply rig demonstrate that a rotating machine can exchange energy with fluid even when the inlet and outlet static pressures do not alone reveal its shaft duty. This particular lesson tests how flow, head and loading coefficients influences the balance among useful power, operating stability, mechanical limits and lifetime expense. The model applies only to its stated fluid and duty conditions.

**Physical mechanism:** Nondimensional parameters permit meaningful comparison of geometrically similar machines when Reynolds and Mach effects are controlled. Mark the control-volume stations, flow direction, shaft boundary and whether the stated measurements use absolute or relative velocity, total or static state.

### 2. Model and derivation

**Core equation:** `phi=Vax/U; psi=Delta_h0/U^2`.

The equation follows from the appropriate balance of energy, mass or angular momentum. Define the inlet, outlet and reference frame first; state whether an efficiency uses fluid, shaft or electric power and whether a pressure is static or total.

Start with a torque balance around the rotor axis and name positive rotation. The steady angular-momentum balance connects torque to mass flow times change in r Vtheta. Multiplication by angular velocity yields the ideal Euler work equation. Because U=omega r, this is not a mysterious empirical correlation. It is a specific form of angular momentum conservation.

Check dimensions: J/kg = m²/s², hydraulic head uses metres, efficiency is dimensionless, and torque times rad/s gives watts.

### 3. Worked example and sensitivity

**Teaching case:** A stage with Vax=90 m/s, U=180 m/s and Delta_h0=19.4 kJ/kg has phi=0.50 and psi=0.599.

**Explicit substitution:** phi = 90/180; psi=19,400/180²; therefore **phi=0.500; psi=0.5988**. Specific work uses joules per kilogram, not kilojoules per kilogram.

Check arithmetic independently. Then perturb one input by 10%: linear, quadratic and cubic factors become 1.1, 1.21 and 1.331, respectively. Recompute nonlinear property relationships. An algebraic change is not evidence of a new real-machine operating point.

### 4. Loss mechanisms, diagnostics and design limits

**Critical misconception:** Assuming identical phi and psi guarantees identical efficiency despite surface roughness or compressibility mismatch. Consider off-design incidence, leakage, wakes and local mechanical or thermal limits; different machine types have distinct damage mechanisms.

**Test evidence:** Calculate coefficients over measured speed and flow sweeps with geometry and temperature documented. Record calibration and uncertainty, check the station definitions, and separate real losses from sensor or operating-point differences. Identify every mass stream crossing the control volume, including leakage, bleed and cooling injections. For a steady insulated machine, power transfer is tied to the change in stagnation enthalpy, but heat leakage and unsteady stored energy can matter in a real test. If the energy residual is large, do not force it into an unexplained efficiency factor.

**Provisional decision:** Compare a proposed design to a plausible stage-loading range before specifying blade count. Revise this recommendation if an independently verified safety or stability constraint is violated.

### 5. Assessment (five tasks)

1. **Calculation:** Using `phi=Vax/U; psi=Delta_h0/U^2`, reproduce **phi=0.500; psi=0.5988** and show every unit conversion. Explain why the chosen sign convention is necessary.
2. **Design variation:** Perturb the dominant flow, temperature, speed or head input by 10% and recompute. Which physical assumption fails first at a very different duty point?
3. **Failure investigation:** Use this misconception as the starting hypothesis: Assuming identical phi and psi guarantees identical efficiency despite surface roughness or compressibility mismatch. Propose an alternative explanation and one observation that distinguishes the two.
4. **Measurement plan:** Operationalize this requirement: Calculate coefficients over measured speed and flow sweeps with geometry and temperature documented. State one calibration check, one expected systematic error and how results are normalized to the same operating state.
5. **Decision memo:** Evaluate the provisional change: Compare a proposed design to a plausible stage-loading range before specifying blade count. Identify a constraint or observation that would force the opposite decision.

### 6. Worked-answer guidance

**1.** The substitution is **phi = 90/180; psi=19,400/180²**, yielding **phi=0.500; psi=0.5988** under the stated simplifications. Specific work uses joules per kilogram, not kilojoules per kilogram. A complete answer identifies pressure, temperature and rotor-frame conventions where relevant.

**2.** Apply the functional dependence of the displayed relation and calculate the changed case. State whether the perturbation preserves the real operating point; update thermodynamic properties if needed.

**3–4.** Nondimensional parameters permit meaningful comparison of geometrically similar machines when Reynolds and Mach effects are controlled. Calculate coefficients over measured speed and flow sweeps with geometry and temperature documented. Link one cause to an independent measurement and report uncertainty.

**5.** Compare a proposed design to a plausible stage-loading range before specifying blade count. It is provisional pending independent safety, structural and performance review.

**Status:** All values are invented classroom inputs; this chapter is not a measured field study, machine certification or safe operating procedure.


---

## U01-L05 — Similarity and corrected operating conditions

**Outcome.** Use conservation laws and appropriate reference stations to analyze **similarity and corrected operating conditions**; solve a traceable numerical example; expose model limitations; and justify a provisional engineering choice. This is Unit 01, **Foundations of Energy Transfer in Rotating Flow**.

### 1. Physical setting and governing reasoning

Consider the difference between predicting a single performance number and qualifying a rotating machine. This lesson develops one measurable calculation, then asks which assumptions fail outside the demonstration state. The shared design brief is: A water test bench and an air supply rig demonstrate that a rotating machine can exchange energy with fluid even when the inlet and outlet static pressures do not alone reveal its shaft duty. This particular lesson tests how similarity and corrected operating conditions influences the balance among useful power, operating stability, mechanical limits and lifetime expense. The model applies only to its stated fluid and duty conditions.

**Physical mechanism:** Similarity preserves nondimensional operating state, not an arbitrary fixed-system intersection. Mark the control-volume stations, flow direction, shaft boundary and whether the stated measurements use absolute or relative velocity, total or static state.

### 2. Model and derivation

**Core equation:** `Q2/Q1≈N2/N1 at fixed geometry and similarity for incompressible machines`.

The equation follows from the appropriate balance of energy, mass or angular momentum. Define the inlet, outlet and reference frame first; state whether an efficiency uses fluid, shaft or electric power and whether a pressure is static or total.

Before substituting numbers, draw velocity triangles: V is absolute, U is tangential blade velocity and W=V-U is relative. Record whether Vtheta is co-rotating or counter-rotating. Total enthalpy h0=h+V^2/2 is appropriate for energy accounting across an adiabatic rotating row, but total pressure can decrease because entropy increases.

Check dimensions: J/kg = m²/s², hydraulic head uses metres, efficiency is dimensionless, and torque times rad/s gives watts.

### 3. Worked example and sensitivity

**Teaching case:** Raising a pump speed from 1200 to 1440 rpm predicts flow multiplication by 1.20 near corresponding operating points.

**Explicit substitution:** N2/N1=1440/1200; therefore **1.20 × corresponding flow**. Recompute actual operating point against system curve containing static head.

Check arithmetic independently. Then perturb one input by 10%: linear, quadratic and cubic factors become 1.1, 1.21 and 1.331, respectively. Recompute nonlinear property relationships. An algebraic change is not evidence of a new real-machine operating point.

### 4. Loss mechanisms, diagnostics and design limits

**Critical misconception:** Applying the affinity law to a pump at fixed static head without recomputing system intersection is misleading. Consider off-design incidence, leakage, wakes and local mechanical or thermal limits; different machine types have distinct damage mechanisms.

**Test evidence:** Overlay measured pump curves and system curves at both speeds; check density and viscosity variation. Record calibration and uncertainty, check the station definitions, and separate real losses from sensor or operating-point differences. The best-efficiency point is merely one location on a map. Startup, shutdown, reduced duty, elevated temperature and equipment aging may create more restrictive limits. A specification should include allowable flow, speed, vibration, pressure and temperature, with a defined trip or mitigation strategy.

**Provisional decision:** Decide whether a VFD can achieve the required flow without operating in an unstable or low-efficiency range. Revise this recommendation if an independently verified safety or stability constraint is violated.

### 5. Assessment (five tasks)

1. **Calculation:** Using `Q2/Q1≈N2/N1 at fixed geometry and similarity for incompressible machines`, reproduce **1.20 × corresponding flow** and show every unit conversion. Explain why the chosen sign convention is necessary.
2. **Design variation:** Perturb the dominant flow, temperature, speed or head input by 10% and recompute. Which physical assumption fails first at a very different duty point?
3. **Failure investigation:** Use this misconception as the starting hypothesis: Applying the affinity law to a pump at fixed static head without recomputing system intersection is misleading. Propose an alternative explanation and one observation that distinguishes the two.
4. **Measurement plan:** Operationalize this requirement: Overlay measured pump curves and system curves at both speeds; check density and viscosity variation. State one calibration check, one expected systematic error and how results are normalized to the same operating state.
5. **Decision memo:** Evaluate the provisional change: Decide whether a VFD can achieve the required flow without operating in an unstable or low-efficiency range. Identify a constraint or observation that would force the opposite decision.

### 6. Worked-answer guidance

**1.** The substitution is **N2/N1=1440/1200**, yielding **1.20 × corresponding flow** under the stated simplifications. Recompute actual operating point against system curve containing static head. A complete answer identifies pressure, temperature and rotor-frame conventions where relevant.

**2.** Apply the functional dependence of the displayed relation and calculate the changed case. State whether the perturbation preserves the real operating point; update thermodynamic properties if needed.

**3–4.** Similarity preserves nondimensional operating state, not an arbitrary fixed-system intersection. Overlay measured pump curves and system curves at both speeds; check density and viscosity variation. Link one cause to an independent measurement and report uncertainty.

**5.** Decide whether a VFD can achieve the required flow without operating in an unstable or low-efficiency range. It is provisional pending independent safety, structural and performance review.

**Status:** All values are invented classroom inputs; this chapter is not a measured field study, machine certification or safe operating procedure.


---

